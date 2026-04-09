#!/usr/bin/env bash
cd "$(dirname "$0")"

python run.py \
  --env airline \
  --task-split dev \
  --model qwen3-235b-a22b-instruct-2507 \
  --model-provider hosted_vllm \
  --user-model qwen3-235b-a22b-instruct-2507 \
  --user-model-provider hosted_vllm \
  --api-base "https://openai.rc.asu.edu/v1"
