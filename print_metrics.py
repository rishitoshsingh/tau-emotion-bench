# Copyright Sierra

import argparse
import json
from math import comb
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print average reward and Pass^k from a saved benchmark results JSON."
    )
    parser.add_argument(
        "results_path",
        type=Path,
        help="Path to a saved results JSON file.",
    )
    parser.add_argument(
        "--num-trials",
        type=int,
        default=None,
        help="Optional expected number of trials. Defaults to inferring from the saved trial ids.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    with args.results_path.open("r") as f:
        payload = json.load(f)

    if not isinstance(payload, list):
        raise ValueError(f"{args.results_path} does not contain a JSON list of results.")

    display_metrics(payload, expected_num_trials=args.num_trials)


def display_metrics(
    results: list[dict], expected_num_trials: int | None = None
) -> None:
    def is_successful(reward: float) -> bool:
        return (1 - 1e-6) <= reward <= (1 + 1e-6)

    if not results:
        print("🏆 No results to score.")
        return

    inferred = len({result["trial"] for result in results})
    num_trials = (
        expected_num_trials
        if expected_num_trials is not None and expected_num_trials > 0
        else inferred
    )
    if num_trials <= 0:
        print("🏆 No results to score.")
        return

    rewards = [result["reward"] for result in results]
    avg_reward = sum(rewards) / len(rewards)
    c_per_task_id: dict[int, int] = {}
    for result in results:
        task_id = result["task_id"]
        reward = result["reward"]
        if task_id not in c_per_task_id:
            c_per_task_id[task_id] = 1 if is_successful(reward) else 0
        else:
            c_per_task_id[task_id] += 1 if is_successful(reward) else 0

    n_tasks = len(c_per_task_id)
    if n_tasks == 0:
        print("🏆 Average reward: (no tasks in results)")
        return

    print(f"🏆 Average reward: {avg_reward}")
    print("📈 Pass^k")
    for k in range(1, num_trials + 1):
        denom = comb(num_trials, k)
        sum_task_pass_hat_k = 0.0
        for c in c_per_task_id.values():
            if c >= k:
                sum_task_pass_hat_k += comb(c, k) / denom
        print(f"  k={k}: {sum_task_pass_hat_k / n_tasks}")


if __name__ == "__main__":
    main()

