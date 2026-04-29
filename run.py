# Copyright Sierra

import argparse
from tau_emotion_bench.types import RunConfig
from tau_emotion_bench.run import run
from litellm import provider_list
from tau_emotion_bench.envs.user import UserStrategy

from dotenv import load_dotenv
load_dotenv()

def parse_args() -> RunConfig:
    parser = argparse.ArgumentParser()
    parser.add_argument("--num-trials", type=int, default=1)
    parser.add_argument(
        "--env", type=str, choices=["retail", "airline", "telecom", "telehealth"], default="retail"
    )
    parser.add_argument(
        "--model",
        type=str,
        help="The model to use for the agent",
    )
    parser.add_argument(
        "--model-provider",
        type=str,
        choices=provider_list,
        help="The model provider for the agent",
    )
    parser.add_argument(
        "--user-model",
        type=str,
        default="gpt-4o",
        help="The model to use for the user simulator",
    )
    parser.add_argument(
        "--user-model-provider",
        type=str,
        choices=provider_list,
        help="The model provider for the user simulator",
    )
    parser.add_argument(
        "--agent-strategy",
        type=str,
        default="tool-calling",
        choices=["tool-calling", "act", "react", "few-shot"],
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="The sampling temperature for the action model",
    )
    parser.add_argument(
        "--task-split",
        type=str,
        default="test",
        choices=["train", "test", "dev"],
        help="Task split (retail: train/test/dev; airline: test/dev)",
    )
    parser.add_argument(
        "--emotion-enabled",
        action="store_true",
        help="Whether to run the environment with emotion",
    )
    parser.add_argument(
        "--api-base",
        type=str,
        default=None,
        help="Optional OpenAI-compatible API base URL for LiteLLM (agent)",
    )
    parser.add_argument(
        "--user-api-base",
        type=str,
        default=None,
        help="Optional OpenAI-compatible API base URL for LiteLLM (user simulator)",
    )
    parser.add_argument("--start-index", type=int, default=0)
    parser.add_argument("--end-index", type=int, default=-1, help="Run all tasks if -1")
    parser.add_argument("--task-ids", type=int, nargs="+", help="(Optional) run only the tasks with the given IDs")
    parser.add_argument("--log-dir", type=str, default="results")
    parser.add_argument(
        "--checkpoint",
        type=str,
        default=None,
        help="Path to results JSON. If set, this file is used instead of a timestamped name under --log-dir.",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Deprecated compatibility flag. Runs with --checkpoint now resume automatically unless --overwrite-checkpoint is set.",
    )
    parser.add_argument(
        "--overwrite-checkpoint",
        action="store_true",
        help="With --checkpoint: ignore any existing checkpoint and overwrite it.",
    )
    parser.add_argument(
        "--max-concurrency",
        type=int,
        default=1,
        help="Number of tasks to run in parallel",
    )
    parser.add_argument("--seed", type=int, default=10)
    parser.add_argument("--shuffle", type=int, default=0)
    parser.add_argument(
        "--sample-max-attempts",
        type=int,
        default=3,
        help="Maximum whole-sample attempts for transient provider failures before leaving the job pending for a future rerun.",
    )
    parser.add_argument(
        "--sample-retry-initial-delay",
        type=float,
        default=5.0,
        help="Initial delay in seconds between whole-sample retries after transient provider failures.",
    )
    parser.add_argument(
        "--sample-retry-max-delay",
        type=float,
        default=120.0,
        help="Maximum delay in seconds between whole-sample retries.",
    )
    parser.add_argument(
        "--llm-max-attempts",
        type=int,
        default=6,
        help="Maximum attempts for each LiteLLM completion call on transient errors.",
    )
    parser.add_argument(
        "--llm-retry-initial-delay",
        type=float,
        default=2.0,
        help="Initial per-call retry delay in seconds.",
    )
    parser.add_argument(
        "--llm-retry-max-delay",
        type=float,
        default=60.0,
        help="Maximum per-call retry delay in seconds.",
    )
    parser.add_argument(
        "--llm-retry-backoff",
        type=float,
        default=2.0,
        help="Per-call retry exponential backoff multiplier.",
    )
    parser.add_argument(
        "--llm-retry-jitter",
        type=float,
        default=1.0,
        help="Maximum random jitter in seconds added to per-call retry sleeps.",
    )
    parser.add_argument(
        "--llm-rate-limit-cooldown",
        type=float,
        default=15.0,
        help="Shared cooldown in seconds applied to all workers after a rate-limit error.",
    )
    parser.add_argument(
        "--llm-min-call-interval",
        type=float,
        default=0.0,
        help="Optional process-wide minimum seconds between LiteLLM calls.",
    )
    parser.add_argument(
        "--llm-max-concurrent-calls",
        type=int,
        default=None,
        help="Optional process-wide cap on simultaneous LiteLLM calls, independent of --max-concurrency.",
    )
    parser.add_argument("--user-strategy", type=str, default="llm", choices=[item.value for item in UserStrategy])
    parser.add_argument("--few-shot-displays-path", type=str, help="Path to a jsonlines file containing few shot displays")
    args = parser.parse_args()
    print(args)
    return RunConfig(
        model_provider=args.model_provider,
        user_model_provider=args.user_model_provider,
        model=args.model,
        user_model=args.user_model,
        num_trials=args.num_trials,
        env=args.env,
        agent_strategy=args.agent_strategy,
        temperature=args.temperature,
        task_split=args.task_split,
        emotion_enabled=args.emotion_enabled,
        start_index=args.start_index,
        end_index=args.end_index,
        task_ids=args.task_ids,
        log_dir=args.log_dir,
        checkpoint_path=args.checkpoint,
        resume=args.resume,
        overwrite_checkpoint=args.overwrite_checkpoint,
        max_concurrency=args.max_concurrency,
        sample_max_attempts=args.sample_max_attempts,
        sample_retry_initial_delay=args.sample_retry_initial_delay,
        sample_retry_max_delay=args.sample_retry_max_delay,
        llm_max_attempts=args.llm_max_attempts,
        llm_retry_initial_delay=args.llm_retry_initial_delay,
        llm_retry_max_delay=args.llm_retry_max_delay,
        llm_retry_backoff=args.llm_retry_backoff,
        llm_retry_jitter=args.llm_retry_jitter,
        llm_rate_limit_cooldown=args.llm_rate_limit_cooldown,
        llm_min_call_interval=args.llm_min_call_interval,
        llm_max_concurrent_calls=args.llm_max_concurrent_calls,
        seed=args.seed,
        shuffle=args.shuffle,
        user_strategy=args.user_strategy,
        few_shot_displays_path=args.few_shot_displays_path,
        api_base=args.api_base,
        user_api_base=args.user_api_base,
    )


def main():
    config = parse_args()
    run(config)


if __name__ == "__main__":
    main()
