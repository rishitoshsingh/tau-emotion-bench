# Copyright Sierra

import os
from typing import Any, Dict, Optional


def optional_api_base(api_base: Optional[str]) -> Dict[str, Any]:
    """Keyword args for litellm.completion when using a custom OpenAI-compatible endpoint."""
    if api_base:
        return {"api_base": api_base}
    return {}


def optional_sampling_params() -> Dict[str, Any]:
    """Extra sampling params read from env vars. Set during training, absent during testing."""
    mapping = {
        "LITELLM_TOP_P": "top_p",
        "LITELLM_TOP_K": "top_k",
        "LITELLM_MIN_P": "min_p",
        "LITELLM_MAX_TOKENS": "max_tokens",
        "LITELLM_REPETITION_PENALTY": "repetition_penalty",
    }
    return {
        param_key: float(val)
        for env_key, param_key in mapping.items()
        if (val := os.environ.get(env_key)) is not None
    }
