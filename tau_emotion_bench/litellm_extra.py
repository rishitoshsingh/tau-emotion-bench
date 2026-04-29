# Copyright Sierra

import random
import threading
import time
from typing import Any, Dict, Optional

from litellm import completion


_RETRIABLE_ERROR_NAMES = {
    "APIConnectionError",
    "APIError",
    "APIStatusError",
    "APITimeoutError",
    "InternalServerError",
    "RateLimitError",
    "ServiceUnavailableError",
    "Timeout",
    "TimeoutError",
}
_NON_RETRIABLE_ERROR_NAMES = {
    "AuthenticationError",
    "BadRequestError",
    "ContextWindowExceededError",
    "ContentPolicyViolationError",
    "InvalidRequestError",
    "NotFoundError",
    "PermissionDeniedError",
}
_TRANSIENT_MESSAGE_MARKERS = (
    "429",
    "500",
    "502",
    "503",
    "504",
    "api connection",
    "connection error",
    "connection reset",
    "overloaded",
    "rate limit",
    "ratelimit",
    "temporarily unavailable",
    "timed out",
    "timeout",
    "too many requests",
)

_retry_config = {
    "max_attempts": 6,
    "initial_delay": 2.0,
    "max_delay": 60.0,
    "backoff": 2.0,
    "jitter": 1.0,
    "rate_limit_cooldown": 15.0,
    "min_call_interval": 0.0,
}
_rate_lock = threading.Lock()
_rate_next_allowed_at = 0.0
_last_call_at = 0.0
_call_semaphore: Optional[threading.Semaphore] = None


def optional_api_base(api_base: Optional[str]) -> Dict[str, Any]:
    """Keyword args for litellm.completion when using a custom OpenAI-compatible endpoint."""
    if api_base:
        return {"api_base": api_base}
    return {}


def configure_litellm_resilience(
    *,
    max_attempts: int,
    initial_delay: float,
    max_delay: float,
    backoff: float,
    jitter: float,
    rate_limit_cooldown: float,
    min_call_interval: float,
    max_concurrent_calls: Optional[int],
) -> None:
    """Configure process-wide retry and throttling behavior for LiteLLM calls."""
    global _call_semaphore
    _retry_config.update(
        {
            "max_attempts": max(1, max_attempts),
            "initial_delay": max(0.0, initial_delay),
            "max_delay": max(0.0, max_delay),
            "backoff": max(1.0, backoff),
            "jitter": max(0.0, jitter),
            "rate_limit_cooldown": max(0.0, rate_limit_cooldown),
            "min_call_interval": max(0.0, min_call_interval),
        }
    )
    if max_concurrent_calls is not None and max_concurrent_calls > 0:
        _call_semaphore = threading.Semaphore(max_concurrent_calls)
    else:
        _call_semaphore = None


def is_transient_model_error(error: BaseException) -> bool:
    """Return True for provider/network failures that should not count as task failures."""
    cls_name = type(error).__name__
    if cls_name in _NON_RETRIABLE_ERROR_NAMES:
        return False
    if cls_name in _RETRIABLE_ERROR_NAMES:
        return True
    return is_transient_error_text(str(error))


def is_transient_error_text(text: str) -> bool:
    lowered = text.lower()
    if any(marker in lowered for marker in ("401", "403", "invalid api key", "unauthorized")):
        return False
    return any(marker in lowered for marker in _TRANSIENT_MESSAGE_MARKERS)


def robust_completion(**kwargs: Any) -> Any:
    """LiteLLM completion with bounded retries and shared backoff across threads."""
    attempt = 1
    delay = _retry_config["initial_delay"]
    while True:
        _wait_for_global_throttle()
        try:
            if _call_semaphore is None:
                return completion(**kwargs)
            with _call_semaphore:
                return completion(**kwargs)
        except Exception as e:
            if attempt >= _retry_config["max_attempts"] or not is_transient_model_error(e):
                raise
            sleep_for = _sleep_for_attempt(e, delay)
            if _is_rate_limit(e):
                _extend_global_cooldown(max(sleep_for, _retry_config["rate_limit_cooldown"]))
            print(
                f"Transient model error ({type(e).__name__}) on attempt "
                f"{attempt}/{_retry_config['max_attempts']}; retrying in {sleep_for:.1f}s: {e}"
            )
            time.sleep(sleep_for)
            delay = min(_retry_config["max_delay"], delay * _retry_config["backoff"])
            attempt += 1


def _wait_for_global_throttle() -> None:
    global _last_call_at
    while True:
        with _rate_lock:
            now = time.monotonic()
            wait_for = max(0.0, _rate_next_allowed_at - now)
            min_interval = _retry_config["min_call_interval"]
            if min_interval > 0.0:
                wait_for = max(wait_for, _last_call_at + min_interval - now)
            if wait_for <= 0.0:
                _last_call_at = now
                return
        time.sleep(min(wait_for, 1.0))


def _extend_global_cooldown(delay: float) -> None:
    global _rate_next_allowed_at
    if delay <= 0.0:
        return
    with _rate_lock:
        _rate_next_allowed_at = max(_rate_next_allowed_at, time.monotonic() + delay)


def _sleep_for_attempt(error: BaseException, fallback_delay: float) -> float:
    retry_after = _retry_after_seconds(error)
    delay = retry_after if retry_after is not None else fallback_delay
    if _retry_config["jitter"] > 0:
        delay += random.uniform(0.0, _retry_config["jitter"])
    return min(_retry_config["max_delay"], max(0.0, delay))


def _retry_after_seconds(error: BaseException) -> Optional[float]:
    response = getattr(error, "response", None)
    headers = getattr(response, "headers", None)
    if headers is None:
        headers = getattr(error, "headers", None)
    if not headers:
        return None
    retry_after = None
    for key in ("retry-after", "Retry-After", "x-ratelimit-reset-requests"):
        try:
            retry_after = headers.get(key)
        except AttributeError:
            retry_after = headers[key] if key in headers else None
        if retry_after is not None:
            break
    if retry_after is None:
        return None
    try:
        return float(retry_after)
    except (TypeError, ValueError):
        return None


def _is_rate_limit(error: BaseException) -> bool:
    text = f"{type(error).__name__} {error}".lower()
    return "ratelimit" in text or "rate limit" in text or "429" in text
