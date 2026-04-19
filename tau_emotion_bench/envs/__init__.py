# Copyright Sierra

from typing import Optional, Union
from tau_emotion_bench.envs.base import Env
from tau_emotion_bench.envs.user import UserStrategy


def get_env(
    env_name: str,
    user_strategy: Union[str, UserStrategy],
    user_model: str,
    task_split: str,
    emotion_enabled: bool = True,
    user_provider: Optional[str] = None,
    task_index: Optional[int] = None,
    api_base: Optional[str] = None,
) -> Env:
    if env_name == "retail":
        from tau_emotion_bench.envs.retail import MockRetailDomainEnv

        return MockRetailDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            emotion_enabled=emotion_enabled,
            user_provider=user_provider,
            task_index=task_index,
            api_base=api_base,
        )
    elif env_name == "airline":
        from tau_emotion_bench.envs.airline import MockAirlineDomainEnv

        return MockAirlineDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            emotion_enabled=emotion_enabled,
            user_provider=user_provider,
            task_index=task_index,
            api_base=api_base,
        )
    elif env_name == "telecom":
        from tau_emotion_bench.envs.telecom import MockTelecomDomainEnv

        return MockTelecomDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            emotion_enabled=emotion_enabled,
            user_provider=user_provider,
            task_index=task_index,
            api_base=api_base,
        )
    elif env_name == "telehealth":
        from tau_emotion_bench.envs.telehealth import MockTelehealthDomainEnv

        return MockTelehealthDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            emotion_enabled=emotion_enabled,
            user_provider=user_provider,
            task_index=task_index,
            api_base=api_base,
        )
    else:
        raise ValueError(f"Unknown environment: {env_name}")
