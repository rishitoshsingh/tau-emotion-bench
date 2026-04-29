#!/bin/bash

# Activate conda environment
eval "$(conda shell.bash hook)"
conda activate applied

DOMAINS=("retail" "airline" "telecom" "telehealth")

# Cleanup function for Ctrl+C
cleanup() {
    echo ""
    echo "⚠️ Interrupted. Killing all worker processes..."
    for pid in "${pids[@]}"; do
        if kill -0 "$pid" 2>/dev/null; then
            kill "$pid" 2>/dev/null || true
        fi
    done
    exit 1
}

trap cleanup SIGINT SIGTERM
TRAIN_TRAJ_DIR="${TRAIN_TRAJ_DIR:-./train_traj}"
LOG_DIR="${LOG_DIR:-./logs}"

# Fixed model config
NUM_TRIALS=1
EMOTION_ENABLED="--emotion-enabled"
MODEL="qwen3-235b-a22b-instruct-2507"
MODEL_PROVIDER="hosted_vllm"
USER_MODEL="qwen3-235b-a22b-instruct-2507"
USER_MODEL_PROVIDER="hosted_vllm"
API_BASE="https://openai.rc.asu.edu/v1"
USER_API_BASE="https://openai.rc.asu.edu/v1"

mkdir -p "$LOG_DIR"

echo "Parallel domain runner - independent task processing"
echo "Model: $MODEL (num_trials: $NUM_TRIALS, emotion: enabled)"
echo ""

process_domain() {
    local domain=$1
    local log_file="$LOG_DIR/${domain}.log"

    exec > >(tee -a "$log_file")
    exec 2>&1

    echo "[$(date)] Starting worker for domain: $domain"

    # Count tasks from tasks_train.py
    local task_count=0
    local count_output=$( (python3 -c "import sys; sys.path.insert(0, '.'); from tau_emotion_bench.envs.${domain}.tasks_train import TASKS; print(len(TASKS))" 2>&1) || true)

    if [[ "$count_output" =~ ^[0-9]+$ ]]; then
        task_count=$count_output
    else
        echo "[$(date)] ❌ Failed to load tasks_train.py for $domain"
        echo "[$(date)] Error: $count_output"
        return 1
    fi

    echo "[$(date)] Found $task_count tasks for $domain (task_ids 0-$((task_count - 1)))"

    # Find last completed task_id
    mkdir -p "$TRAIN_TRAJ_DIR/$domain"
    local last_completed=-1

    if ls "$TRAIN_TRAJ_DIR/$domain"/*.json 2>/dev/null | wc -l | grep -q "[1-9]"; then
        last_completed=$(ls "$TRAIN_TRAJ_DIR/$domain"/*.json | sed 's/.*\/\([0-9]*\)\.json/\1/' | sort -n | tail -1)
    fi

    local start_task=$((last_completed + 1))

    if [ $start_task -ge $task_count ]; then
        echo "[$(date)] ✅ All tasks completed for $domain (last: $last_completed)"
        return 0
    fi

    echo "[$(date)] Resuming from task_id=$start_task (last completed: $last_completed)"

    # Run remaining tasks
    for task_id in $(seq $start_task $((task_count - 1))); do
        checkpoint_file="$TRAIN_TRAJ_DIR/$domain/${task_id}.json"

        echo "[$(date)] Processing task_id=$task_id for $domain..."

        if python3 run.py \
            --env "$domain" \
            --task-ids "$task_id" \
            --checkpoint "$checkpoint_file" \
            --resume \
            --task-split train \
            --num-trials $NUM_TRIALS \
            $EMOTION_ENABLED \
            --model "$MODEL" \
            --model-provider "$MODEL_PROVIDER" \
            --user-model "$USER_MODEL" \
            --user-model-provider "$USER_MODEL_PROVIDER" \
            --api-base "$API_BASE" \
            --user-api-base "$USER_API_BASE"; then
            echo "[$(date)] ✅ Completed task_id=$task_id for $domain"
        else
            echo "[$(date)] ❌ Failed task_id=$task_id for $domain (will retry)"
            return 1
        fi
    done

    echo "[$(date)] ✅ All tasks completed for $domain"
}

pids=()
for domain in "${DOMAINS[@]}"; do
    process_domain "$domain" &
    pid=$!
    pids+=($pid)
    echo "Spawned worker for $domain (PID: $pid)"
done

echo ""
echo "All workers spawned. Monitoring..."
echo ""

# Monitor all workers
failed=false
for i in "${!pids[@]}"; do
    pid=${pids[$i]}
    domain=${DOMAINS[$i]}

    if wait $pid; then
        echo "✅ Worker $domain (PID: $pid) completed successfully"
    else
        echo "❌ Worker $domain (PID: $pid) failed"
        failed=true
    fi
done

if [ "$failed" = true ]; then
    echo ""
    echo "⚠️ Some workers failed. Rerun script to retry failed domains."
    exit 1
fi

echo ""
echo "✅ All workers completed successfully!"
