# Copyright Sierra

import os
import json
import random
import tempfile
import threading
import time
import traceback
from math import comb
from typing import List, Dict, Any, Tuple, Set, Optional
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from tau_emotion_bench.envs import get_env
from tau_emotion_bench.agents.base import Agent
from tau_emotion_bench.litellm_extra import (
    configure_litellm_resilience,
    is_transient_error_text,
    is_transient_model_error,
)
from tau_emotion_bench.types import EnvRunResult, RunConfig


def reward_status_emoji(reward: float) -> str:
    """✅ success, 😞 user abandoned (###UNSATISFIED###), ❌ wrong completion or other."""
    if (1 - 1e-6) <= reward <= (1 + 1e-6):
        return "✅"
    if (-1 - 1e-6) <= reward <= (-1 + 1e-6):
        return "😞"
    return "❌"
from litellm import provider_list
from tau_emotion_bench.envs.user import UserStrategy


def _atomic_write_json(path: str, payload: List[Dict[str, Any]]) -> None:
    parent = os.path.dirname(os.path.abspath(path)) or "."
    os.makedirs(parent, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=parent, suffix=".json.tmp")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(payload, f, indent=2)
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


def _load_checkpoint(path: str) -> List[EnvRunResult]:
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"⚠️ Could not load checkpoint {path} ({e}); starting with no prior results.")
        return []
    if not isinstance(data, list):
        print(f"⚠️ Checkpoint {path} is not a JSON list; starting with no prior results.")
        return []
    out: List[EnvRunResult] = []
    for item in data:
        try:
            out.append(EnvRunResult.model_validate(item))
        except Exception as e:
            print(f"⚠️ Skipping invalid checkpoint row: {e}")
    return out


def _dedupe_by_task_trial(results: List[EnvRunResult]) -> List[EnvRunResult]:
    by_key: Dict[Tuple[int, int], EnvRunResult] = {}
    for r in results:
        by_key[(r.task_id, r.trial)] = r
    keys = sorted(by_key.keys(), key=lambda t: (t[1], t[0]))
    return [by_key[k] for k in keys]


def _result_has_transient_error(result: EnvRunResult) -> bool:
    if result.info.get("error_type") == "transient_model_error":
        return True
    error_text = "\n".join(
        str(result.info.get(key, "")) for key in ("error", "traceback", "error_type")
    )
    return bool(error_text.strip()) and is_transient_error_text(error_text)


def _result_has_error_payload(result: EnvRunResult) -> bool:
    return any(result.info.get(key) for key in ("error", "traceback", "exception"))


def _sample_retry_delay(config: RunConfig, attempt: int) -> float:
    base = max(0.0, config.sample_retry_initial_delay)
    delay = min(max(0.0, config.sample_retry_max_delay), base * (2 ** max(0, attempt - 1)))
    return delay + random.uniform(0.0, min(delay, 5.0) if delay > 0 else 0.0)


def run(config: RunConfig) -> List[EnvRunResult]:
    assert config.env in ["retail", "airline", "telecom", "telehealth"], "Only retail, airline, telecom and telehealth envs are supported"
    assert config.model_provider in provider_list, "Invalid model provider"
    assert config.user_model_provider in provider_list, "Invalid user model provider"
    assert config.agent_strategy in ["tool-calling", "act", "react", "few-shot"], "Invalid agent strategy"
    assert config.task_split in ["train", "test", "dev"], "Invalid task split"
    assert config.user_strategy in [item.value for item in UserStrategy], "Invalid user strategy"
    if config.resume and not config.checkpoint_path:
        raise ValueError("--resume requires --checkpoint (path to the results JSON).")

    configure_litellm_resilience(
        max_attempts=config.llm_max_attempts,
        initial_delay=config.llm_retry_initial_delay,
        max_delay=config.llm_retry_max_delay,
        backoff=config.llm_retry_backoff,
        jitter=config.llm_retry_jitter,
        rate_limit_cooldown=config.llm_rate_limit_cooldown,
        min_call_interval=config.llm_min_call_interval,
        max_concurrent_calls=config.llm_max_concurrent_calls,
    )

    random.seed(config.seed)
    time_str = datetime.now().strftime("%m%d%H%M%S")
    if config.checkpoint_path:
        ckpt_path = os.path.expanduser(config.checkpoint_path)
    else:
        if not os.path.exists(config.log_dir):
            os.makedirs(config.log_dir)
        ckpt_path = f"{config.log_dir}/{config.agent_strategy}-{config.model.split('/')[-1]}-{config.temperature}_range_{config.start_index}-{config.end_index}_user-{config.user_model}-{config.user_strategy}_{time_str}.json"

    print(f"Loading user with strategy: {config.user_strategy}")
    print(f"Emotion enabled: {config.emotion_enabled}")
    env = get_env(
        config.env,
        user_strategy=config.user_strategy,
        user_model=config.user_model,
        user_provider=config.user_model_provider,
        task_split=config.task_split,
        emotion_enabled=config.emotion_enabled,
        api_base=config.user_api_base,
    )
    agent = agent_factory(
        tools_info=env.tools_info,
        wiki=env.wiki,
        config=config,
    )
    end_index = (
        len(env.tasks) if config.end_index == -1 else min(config.end_index, len(env.tasks))
    )

    loaded: List[EnvRunResult] = []
    if config.checkpoint_path and os.path.exists(ckpt_path) and not config.overwrite_checkpoint:
        checkpoint_rows = _dedupe_by_task_trial(_load_checkpoint(ckpt_path))
        loaded = [r for r in checkpoint_rows if not _result_has_error_payload(r)]
        skipped = len(checkpoint_rows) - len(loaded)
        if loaded:
            print(f"📂 Resuming from {len(loaded)} saved (task_id, trial) result(s) in {ckpt_path}")
        if skipped:
            print(f"♻️ Treating {skipped} errored checkpoint row(s) as pending for retry.")
    elif config.checkpoint_path and os.path.exists(ckpt_path) and config.overwrite_checkpoint:
        print(f"⚠️ Overwriting existing checkpoint at {ckpt_path}")

    done: Set[Tuple[int, int]] = {(r.task_id, r.trial) for r in loaded}
    all_results: List[EnvRunResult] = list(loaded)
    lock = threading.Lock()

    if config.task_ids and len(config.task_ids) > 0:
        print(f"Running tasks {config.task_ids} (checkpoint path: {ckpt_path})")
    else:
        print(
            f"Running tasks {config.start_index} to {end_index} (checkpoint path: {ckpt_path})"
        )

    jobs: List[Tuple[int, int]] = []
    target_keys: Set[Tuple[int, int]] = set()
    for i in range(config.num_trials):
        if config.task_ids and len(config.task_ids) > 0:
            idxs = list(config.task_ids)
        else:
            idxs = list(range(config.start_index, end_index))
        if config.shuffle:
            random.shuffle(idxs)
        for idx in idxs:
            target_keys.add((idx, i))
            if (idx, i) not in done:
                jobs.append((i, idx))

    if not jobs:
        print("Nothing to run (all (task_id, trial) pairs already in checkpoint).")
    else:
        print(f"Scheduled {len(jobs)} job(s) (missing trials).")

        def _run_once(trial_i: int, idx: int) -> EnvRunResult:
            isolated_env = get_env(
                config.env,
                user_strategy=config.user_strategy,
                user_model=config.user_model,
                task_split=config.task_split,
                emotion_enabled=config.emotion_enabled,
                user_provider=config.user_model_provider,
                task_index=idx,
                api_base=config.user_api_base,
            )

            print(f"Running trial {trial_i} task {idx}")
            try:
                res = agent.solve(
                    env=isolated_env,
                    task_index=idx,
                )
                result = EnvRunResult(
                    task_id=idx,
                    reward=res.reward,
                    info=res.info,
                    traj=res.messages,
                    trial=trial_i,
                )
            except Exception as e:
                error_info = {"error": str(e), "traceback": traceback.format_exc()}
                if is_transient_model_error(e):
                    error_info["error_type"] = "transient_model_error"
                result = EnvRunResult(
                    task_id=idx,
                    reward=0.0,
                    info=error_info,
                    traj=[],
                    trial=trial_i,
                )
            return result

        def _run(job: Tuple[int, int]) -> Optional[EnvRunResult]:
            trial_i, idx = job
            result: Optional[EnvRunResult] = None
            for attempt in range(1, max(1, config.sample_max_attempts) + 1):
                result = _run_once(trial_i, idx)
                if not _result_has_transient_error(result):
                    break
                if attempt >= max(1, config.sample_max_attempts):
                    print(
                        "♻️ Holding transient-error job for future retry:",
                        f"trial={trial_i} task_id={idx}",
                        result.info.get("error"),
                    )
                    print("-----")
                    return None
                sleep_for = _sample_retry_delay(config, attempt)
                print(
                    "♻️ Retrying transient-error job:",
                    f"trial={trial_i} task_id={idx}",
                    f"attempt={attempt}/{config.sample_max_attempts}",
                    f"sleep={sleep_for:.1f}s",
                    result.info.get("error"),
                )
                time.sleep(sleep_for)
            assert result is not None
            print(
                reward_status_emoji(result.reward),
                f"trial={trial_i} task_id={idx}",
                result.info,
            )
            print("-----")
            with lock:
                all_results.append(result)
                merged = _dedupe_by_task_trial(all_results)
                all_results[:] = merged
                _atomic_write_json(ckpt_path, [r.model_dump() for r in all_results])
            return result

        with ThreadPoolExecutor(max_workers=config.max_concurrency) as executor:
            list(executor.map(_run, jobs))

    results = _dedupe_by_task_trial(all_results)
    completed_keys = {(r.task_id, r.trial) for r in results}
    pending_count = len(target_keys - completed_keys)
    if pending_count:
        print(
            f"♻️ {pending_count} transient-error job(s) remain pending. "
            "Rerun the same command to retry them."
        )
    display_metrics(results, expected_num_trials=config.num_trials)

    _atomic_write_json(ckpt_path, [result.model_dump() for result in results])
    print(f"\n📄 Results saved to {ckpt_path}\n")
    return results


def agent_factory(
    tools_info: List[Dict[str, Any]], wiki, config: RunConfig
) -> Agent:
    if config.agent_strategy == "tool-calling":
        # native tool calling
        from tau_emotion_bench.agents.tool_calling_agent import ToolCallingAgent

        return ToolCallingAgent(
            tools_info=tools_info,
            wiki=wiki,
            model=config.model,
            provider=config.model_provider,
            temperature=config.temperature,
            api_base=config.api_base,
        )
    elif config.agent_strategy == "act":
        # `act` from https://arxiv.org/abs/2210.03629
        from tau_emotion_bench.agents.chat_react_agent import ChatReActAgent

        return ChatReActAgent(
            tools_info=tools_info,
            wiki=wiki,
            model=config.model,
            provider=config.model_provider,
            use_reasoning=False,
            temperature=config.temperature,
            api_base=config.api_base,
        )
    elif config.agent_strategy == "react":
        # `react` from https://arxiv.org/abs/2210.03629
        from tau_emotion_bench.agents.chat_react_agent import ChatReActAgent

        return ChatReActAgent(
            tools_info=tools_info,
            wiki=wiki,
            model=config.model,
            provider=config.model_provider,
            use_reasoning=True,
            temperature=config.temperature,
            api_base=config.api_base,
        )
    elif config.agent_strategy == "few-shot":
        from tau_emotion_bench.agents.few_shot_agent import FewShotToolCallingAgent
        assert config.few_shot_displays_path is not None, "Few shot displays path is required for few-shot agent strategy"
        with open(config.few_shot_displays_path, "r") as f:
            few_shot_displays = [json.loads(line)["messages_display"] for line in f]

        return FewShotToolCallingAgent(
            tools_info=tools_info,
            wiki=wiki,
            model=config.model,
            provider=config.model_provider,
            few_shot_displays=few_shot_displays,
            temperature=config.temperature,
            api_base=config.api_base,
        )
    else:
        raise ValueError(f"Unknown agent strategy: {config.agent_strategy}")


def display_metrics(
    results: List[EnvRunResult], expected_num_trials: Optional[int] = None
) -> None:
    def is_successful(reward: float) -> bool:
        return (1 - 1e-6) <= reward <= (1 + 1e-6)

    if not results:
        print("🏆 No results to score.")
        return

    inferred = len(set(r.trial for r in results))
    num_trials = (
        expected_num_trials
        if expected_num_trials is not None and expected_num_trials > 0
        else inferred
    )
    if num_trials <= 0:
        print("🏆 No results to score.")
        return
    rewards = [r.reward for r in results]
    avg_reward = sum(rewards) / len(rewards)
    # c from https://arxiv.org/pdf/2406.12045
    c_per_task_id: dict[int, int] = {}
    for result in results:
        if result.task_id not in c_per_task_id:
            c_per_task_id[result.task_id] = 1 if is_successful(result.reward) else 0
        else:
            c_per_task_id[result.task_id] += 1 if is_successful(result.reward) else 0
    pass_hat_ks: dict[int, float] = {}
    n_tasks = len(c_per_task_id)
    if n_tasks == 0:
        print("🏆 Average reward: (no tasks in results)")
        return
    for k in range(1, num_trials + 1):
        sum_task_pass_hat_k = 0
        denom = comb(num_trials, k)
        for c in c_per_task_id.values():
            if c >= k:
                sum_task_pass_hat_k += comb(c, k) / denom
        pass_hat_ks[k] = sum_task_pass_hat_k / n_tasks
    print(f"🏆 Average reward: {avg_reward}")
    print("📈 Pass^k")
    for k, pass_hat_k in pass_hat_ks.items():
        print(f"  k={k}: {pass_hat_k}")
