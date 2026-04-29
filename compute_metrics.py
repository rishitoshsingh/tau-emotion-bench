#!/usr/bin/env python3
"""Compute pass@k and pass^k metrics for all trials in historical_trajectories."""

import json
import re
import math
from pathlib import Path
from collections import defaultdict


def parse_filename(stem):
    """Return (model, domain, emotion_type) from a file stem."""
    m = re.match(r"^(.+?)-(.+?)-(with|without)-emotions$", stem)
    if m:
        return m.group(1), m.group(2), m.group(3)
    return None, None, None


def _comb(n, k):
    """Binomial coefficient C(n, k); returns 0 when k > n."""
    if k > n or n < 0:
        return 0
    return math.comb(n, k)


def compute_pass_at_k(trials, k=1):
    """
    pass@k: unbiased estimator for P(at least 1 of k passes).
    Formula: 1 - C(n-c, k) / C(n, k)
    """
    n = len(trials)
    if n == 0 or k > n:
        return None
    c = sum(1 for t in trials if t["reward"] >= 1.0)
    denom = _comb(n, k)
    if denom == 0:
        return None
    return 1.0 - _comb(n - c, k) / denom


def compute_pass_hat_k(trials, k=1):
    """
    pass^k: unbiased estimator for P(all k pass) — consistency metric.
    Formula: C(c, k) / C(n, k)
    """
    n = len(trials)
    if n == 0 or k > n:
        return None
    c = sum(1 for t in trials if t["reward"] >= 1.0)
    denom = _comb(n, k)
    if denom == 0:
        return None
    return _comb(c, k) / denom


def group_metrics(trials, k_range=None):
    """
    Compute pass@k and pass^k for every k in k_range.

    Args:
        trials: list of trial dicts with "reward" field
        k_range: list of k values to compute for (default: [1, 2, 3, ...] up to n)

    Returns:
        dict with "pass_at_k" and "pass_hat_k" as lists indexed by k
    """
    n = len(trials)
    if n == 0:
        return {"pass_at_k": {}, "pass_hat_k": {}}

    if k_range is None:
        k_range = list(range(1, n + 1))

    pass_at, pass_hat = {}, {}
    for k in k_range:
        at_val = compute_pass_at_k(trials, k=k)
        hat_val = compute_pass_hat_k(trials, k=k)
        if at_val is not None:
            pass_at[k] = round(at_val, 4)
        if hat_val is not None:
            pass_hat[k] = round(hat_val, 4)

    return {"pass_at_k": pass_at, "pass_hat_k": pass_hat}


def main():
    data_dir = Path(__file__).parent / "historical_trajectories"

    # Collect files keyed by (model, domain) -> {'with': path, 'without': path}
    file_map = defaultdict(dict)
    for f in sorted(data_dir.glob("*.json")):
        model, domain, emo = parse_filename(f.stem)
        if model and domain and emo:
            file_map[(model, domain)][emo] = f

    # Process each model/domain pair
    results = {}
    for (model, domain), sides in sorted(file_map.items()):
        if "with" not in sides or "without" not in sides:
            print(f"⚠ Skip {model}/{domain}: missing with/without pair")
            continue

        print(f"Processing {model}/{domain}...", end=" ", flush=True)

        # Load both files
        with open(sides["with"]) as fh:
            with_raw = json.load(fh)
        with open(sides["without"]) as fh:
            without_raw = json.load(fh)

        # Group trials by task_id
        with_tasks = defaultdict(list)
        for item in with_raw:
            with_tasks[item["task_id"]].append(item)

        without_tasks = defaultdict(list)
        for item in without_raw:
            without_tasks[item["task_id"]].append(item)

        # Compute metrics per task, then aggregate
        all_ids = sorted(set(list(with_tasks) + list(without_tasks)))

        with_metrics_list = []
        without_metrics_list = []

        max_n_with = max((len(with_tasks[tid]) for tid in all_ids), default=0)
        max_n_without = max((len(without_tasks[tid]) for tid in all_ids), default=0)

        k_range_with = list(range(1, max_n_with + 1))
        k_range_without = list(range(1, max_n_without + 1))

        for tid in all_ids:
            w_trials = sorted(with_tasks.get(tid, []), key=lambda x: x["trial"])
            wo_trials = sorted(without_tasks.get(tid, []), key=lambda x: x["trial"])

            with_metrics_list.append(group_metrics(w_trials, k_range=k_range_with))
            without_metrics_list.append(group_metrics(wo_trials, k_range=k_range_without))

        # Aggregate across tasks
        def aggregate_metrics(metrics_list):
            agg = {"pass_at_k": {}, "pass_hat_k": {}}

            # Find all k values
            all_k = set()
            for m in metrics_list:
                all_k.update(m["pass_at_k"].keys())
                all_k.update(m["pass_hat_k"].keys())

            for k in sorted(all_k):
                at_vals = [m["pass_at_k"][k] for m in metrics_list if k in m["pass_at_k"]]
                hat_vals = [m["pass_hat_k"][k] for m in metrics_list if k in m["pass_hat_k"]]

                if at_vals:
                    agg["pass_at_k"][k] = round(sum(at_vals) / len(at_vals), 4)
                if hat_vals:
                    agg["pass_hat_k"][k] = round(sum(hat_vals) / len(hat_vals), 4)

            return agg

        results[f"{model}/{domain}"] = {
            "with_emotion": aggregate_metrics(with_metrics_list),
            "without_emotion": aggregate_metrics(without_metrics_list),
        }

        print(f"✓ ({len(all_ids)} tasks)")

    # Print results
    print("\n" + "=" * 80)
    for key in sorted(results.keys()):
        print(f"\n{key}")
        print("-" * 80)

        for emo_type in ["with_emotion", "without_emotion"]:
            data = results[key][emo_type]
            print(f"\n  {emo_type}:")
            print(f"    k  |  pass@k  |  pass^k")
            print(f"    ---+----------+----------")

            all_k = set()
            all_k.update(data["pass_at_k"].keys())
            all_k.update(data["pass_hat_k"].keys())

            for k in sorted(all_k):
                at = data["pass_at_k"].get(k, "-")
                hat = data["pass_hat_k"].get(k, "-")
                print(f"    {k:2} |  {at:7} |  {hat:7}")


if __name__ == "__main__":
    main()
