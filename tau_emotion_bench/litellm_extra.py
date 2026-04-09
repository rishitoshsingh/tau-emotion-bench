# Copyright Sierra

from typing import Any, Dict, Optional


def optional_api_base(api_base: Optional[str]) -> Dict[str, Any]:
    """Keyword args for litellm.completion when using a custom OpenAI-compatible endpoint."""
    if api_base:
        return {"api_base": api_base}
    return {}
