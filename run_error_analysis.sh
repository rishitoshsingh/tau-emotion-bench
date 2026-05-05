#!/bin/bash
set -euo pipefail

# ---- judge model (litellm-compatible OpenAI endpoint) ----
MODEL="${MODEL:-qwen3-235b-a22b-instruct-2507}"
API_BASE="${API_BASE:-https://openai.rc.asu.edu/v1}"
PLATFORM="${PLATFORM:-vllm-chat}"

# Load API key from .env (HOSTED_VLLM_API_KEY for the litellm proxy).
ENV_FILE="${ENV_FILE:-$(dirname "$0")/.env}"
if [[ -f "$ENV_FILE" ]]; then
    set -a
    # shellcheck disable=SC1090
    source "$ENV_FILE"
    set +a
fi
if [[ -z "${HOSTED_VLLM_API_KEY:-}" && -z "${OPENAI_API_KEY:-}" ]]; then
    echo "ERROR: no API key found. Set HOSTED_VLLM_API_KEY (or OPENAI_API_KEY) in $ENV_FILE." >&2
    exit 1
fi
export HOSTED_VLLM_API_KEY VLLM_API_KEY OPENAI_API_KEY

# ---- io ----
RESULTS_DIR="${RESULTS_DIR:-./results}"
OUTPUT_DIR="${OUTPUT_DIR:-./error_analysis}"
MAX_CONCURRENCY="${MAX_CONCURRENCY:-5}"
MAX_FAILED="${MAX_FAILED:-}"   # optional cap, e.g. MAX_FAILED=20

DOMAINS=("airline" "retail" "telecom" "telehealth")

mkdir -p "$OUTPUT_DIR"

for DOMAIN in "${DOMAINS[@]}"; do
    RESULTS_PATH="${RESULTS_DIR}/${DOMAIN}.json"
    OUTPUT_PATH="${OUTPUT_DIR}/${DOMAIN}_error_analysis.json"

    if [[ ! -f "$RESULTS_PATH" ]]; then
        echo "[skip] $DOMAIN — results file not found: $RESULTS_PATH"
        continue
    fi

    echo "=== Running error analysis for $DOMAIN ==="
    echo "  results: $RESULTS_PATH"
    echo "  output:  $OUTPUT_PATH"

    EXTRA_ARGS=()
    if [[ -n "$MAX_FAILED" ]]; then
        EXTRA_ARGS+=(--max-num-failed-results "$MAX_FAILED")
    fi

    python auto_error_identification.py \
        --env "$DOMAIN" \
        --results-path "$RESULTS_PATH" \
        --output-path "$OUTPUT_PATH" \
        --max-concurrency "$MAX_CONCURRENCY" \
        --model "$MODEL" \
        --base-url "$API_BASE" \
        "${EXTRA_ARGS[@]}"
done

echo "Done. Outputs in $OUTPUT_DIR"
