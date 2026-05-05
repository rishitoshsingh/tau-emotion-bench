# τ-emotion-bench: A Benchmark for Tool-Agent–Emotional-User Interaction in Real-World Domains

---

We propose τ-emotion-bench, a benchmark emulating dynamic conversations between an emotional user (simulated by language models) and a language agent provided with domain-specific API tools and policy guidelines. It extends [τ-bench](https://github.com/sierra-research/tau-bench) with (i) emotion-conditioned user simulators and (ii) two additional domains (telecom, telehealth) on top of the original retail and airline domains.

## Getting Started

**To generate test/train datasets:** See [tracer documentation](https://anonymous.4open.science/anonymize/tracer-715D).
**To evaluate agents on the benchmark:** Follow the Setup below.

## Setup

1. Clone this repository and `cd` into it.

2. Install from source (this also installs the required Python packages):

   ```bash
   pip install -e .
   ```

   Tested with Python 3.11.

3. Configure API credentials. Copy or create a `.env` file in the repo root with the keys you need:

   ```bash
   # Closed-source providers (only those you actually use)
   OPENAI_API_KEY=...
   ANTHROPIC_API_KEY=...
   GOOGLE_API_KEY=...
   MISTRAL_API_KEY=...

   # If you serve open-weight models behind any OpenAI-compatible endpoint
   # (vLLM OpenAI server, litellm proxy, TGI, etc.)
   HOSTED_VLLM_API_KEY=...
   VLLM_API_KEY=...
   ```

   `.env` is loaded automatically by `run.py` via `python-dotenv`. It is `.gitignore`d and must never be committed.

## Run

Run a tool-calling agent on the τ-emotion-retail environment with emotions enabled:

```bash
python run.py \
  --agent-strategy tool-calling \
  --env retail \
  --model gpt-4o --model-provider openai \
  --user-model gpt-4o --user-model-provider openai \
  --user-strategy llm \
  --max-concurrency 10 \
  --emotion-enabled
```

Set `--max-concurrency` according to your API rate limits.

### Supported environments

`--env` accepts: `retail`, `airline`, `telecom`, `telehealth`.

### Task splits

Use `--task-split {train,test}` to select the split. The default is `test`. To run a subset, pass `--task-ids 2 4 6`.

### Self-hosted / OpenAI-compatible endpoints

Any OpenAI-compatible endpoint can be used by passing its base URL via `--api-base` (agent) and `--user-api-base` (user simulator). This includes vLLM's OpenAI server, [litellm](https://github.com/BerriAI/litellm) proxies, TGI, OpenRouter, Together, etc. — anything that speaks the OpenAI Chat Completions API:

```bash
python run.py \
  --agent-strategy tool-calling \
  --env retail \
  --model qwen3-235b-a22b-instruct-2507 --model-provider hosted_vllm \
  --user-model qwen3-235b-a22b-instruct-2507 --user-model-provider hosted_vllm \
  --api-base "$API_BASE_URL" \
  --user-api-base "$API_BASE_URL" \
  --user-strategy llm \
  --max-concurrency 10 \
  --emotion-enabled
```

`--api-base` should be the full base URL (typically ending in `/v1`), e.g. `https://my-proxy.example.com/v1` or `http://localhost:8000/v1`.

### Other important arguments

| Flag | Default | Notes |
| ---- | ------- | ----- |
| `--num-trials` | `1` | Number of independent trials per task. Pass^k metrics require `--num-trials k`, e.g. `--num-trials 4` for Pass^4. |
| `--temperature` | `0.0` | Sampling temperature for the **agent** model. The user simulator temperature is set internally. |
| `--seed` | `10` | Seed for task ordering and any stochastic strategies. |
| `--shuffle` | `0` | If non-zero, shuffle tasks before slicing with `--start-index` / `--end-index`. |
| `--start-index` / `--end-index` | `0` / `-1` | Slice the task list (`-1` = run to the end). Useful for sharding across machines. |
| `--task-ids` | unset | Run only the given task IDs (space-separated). Overrides start/end indexing. |
| `--log-dir` | `results` | Where timestamped result JSONs are written when `--checkpoint` is not set. |
| `--checkpoint` | unset | Write/read a single fixed results file at this path instead of a timestamped one. |
| `--resume` | off | Combined with `--checkpoint`, skips `(task_id, trial)` pairs already present in the checkpoint and only runs the missing ones — essential for long sweeps that may be interrupted. |

Concrete example for a 4-trial Pass^4 evaluation with checkpointing:

```bash
python run.py \
  --agent-strategy tool-calling --env retail \
  --model gpt-4o --model-provider openai \
  --user-model gpt-4o --user-model-provider openai \
  --user-strategy llm \
  --num-trials 4 \
  --max-concurrency 10 \
  --checkpoint results/retail_gpt4o.json --resume \
  --emotion-enabled
```

## User simulators

By default the user simulator uses `gpt-4o` with strategy `llm`. Override with `--user-model` / `--user-model-provider` / `--user-strategy`. Available strategies:

- `llm` (default) — single-pass LLM response.
- `react` — chain-of-thought-style user that emits a `Thought:` then `User Response:`.
- `verify` — adds a verification step; the user simulator is re-prompted if its response is judged unsatisfactory.
- `reflection` — adds a self-reflection step; on a failed verification the simulator reflects then regenerates.

Example with a Claude user simulator:

```bash
python run.py --agent-strategy tool-calling --env retail \
  --model gpt-4o --model-provider openai \
  --user-model claude-3-5-sonnet-20240620 --user-model-provider anthropic \
  --user-strategy llm --max-concurrency 10 --emotion-enabled
```

Example `react` user response:

```md
Thought:
I should provide my name and zip code as I wasn't given an email address to use.

User Response:
Sure, my name is Yusuf Rossi, and my zip code is 19122.
```

## Metrics

After a run completes, results are written to `./results/` (or wherever `--log-dir` / `--checkpoint` points). Compute metrics with `compute_metrics.py`:

```bash
python compute_metrics.py --file results/<your-run>.json
python compute_metrics.py            # batch over historical_trajectories/
```

With no flags, sweeps every paired `with-emotions` / `without-emotions` file under `./historical_trajectories/`. Pass `--file` to score a single results file.

## Auto error identification

Trajectories can be long and constraints complex, so manual error labeling is expensive. `auto_error_identification.py` uses an LLM judge to:

1. **Fault assignment** — attribute responsibility to the user, agent, or environment.
2. **Fault categorization** — classify the fault into a fixed taxonomy (missing/extra action, wrong tool call, incomplete, integrity, meta) with a free-text rationale.

Run on a single results file:

```bash
python auto_error_identification.py \
  --env <retail|airline|telecom|telehealth> \
  --platform openai \
  --results-path <path-to-results.json> \
  --output-path <path-to-output.json> \
  --max-concurrency 16 \
  --max-num-failed-results 10
```

Or use the wrapper to run across all four domains (expects results at `./results/<domain>.json`):

```bash
bash run_error_analysis.sh
```

LLM-based error identification is approximate; treat its labels as a starting point, not ground truth.

## Historical trajectories

Pre-computed trajectories for several frontier models are provided under `./historical_trajectories/` so the benchmark can be analyzed without re-running every model. Each file is a JSON array of trajectory records, named `<model>-<domain>-{with,without}-emotions.json`.

## Repository layout

```
run.py                          # entry point for evaluation
run_error_analysis.sh           # batch error identification across domains
auto_error_identification.py    # LLM-judge-based error labeling
compute_metrics.py              # pass^k and related metrics
tau_emotion_bench/
  agents/                       # agent strategies (tool-calling, react, few-shot, ...)
  envs/{retail,airline,telecom,telehealth}/
                                # per-domain tools, tasks, rules, wiki
  model_utils/                  # provider abstraction over OpenAI / Anthropic / vLLM / ...
historical_trajectories/        # cached trajectories for several models
few_shot_data/                  # few-shot demonstrations for the few-shot agent
```

## Reproducibility checklist

- [x] `pip install -e .` pins all required packages (see `setup.py`).
- [x] All randomness is seeded via `--seed` (default `10`).
- [x] Each domain × model × emotion-condition can be run with a single CLI invocation.
- [x] API base URLs are read from env vars / CLI flags so no endpoint is hard-coded.
- [x] Results are saved as JSON with full per-task trajectories so metrics can be recomputed offline.

## Data Generation (Optional)

To generate test/train datasets, see [tracer documentation](https://anonymous.4open.science/anonymize/tracer-715D).

## License

See `./LICENSE`.

## Citation

To be added upon publication.
