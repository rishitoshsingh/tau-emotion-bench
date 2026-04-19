
from tau_emotion_bench.envs.base import Env
from tau_emotion_bench.envs.telehealth.data import load_data
from tau_emotion_bench.envs.telehealth.rules import RULES
from tau_emotion_bench.envs.telehealth.tools import ALL_TOOLS
from tau_emotion_bench.envs.telehealth.wiki import WIKI
from typing import Optional, Union, Dict
from tau_emotion_bench.envs.user import UserStrategy


class MockTelehealthDomainEnv(Env):
    def __init__(
        self,
        user_strategy: Union[str, UserStrategy] = UserStrategy.LLM,
        user_model: str = "gpt-4o",
        user_provider: Optional[str] = None,
        task_split: str = "test",
        emotion_enabled: bool = True,
        task_index: Optional[int] = None,
        api_base: Optional[str] = None,
    ):
        match task_split:
            case "test":
                if emotion_enabled:
                    from tau_emotion_bench.envs.telehealth.tasks_test import TASKS as tasks
                else:
                    from tau_emotion_bench.envs.telehealth.tasks_test_no_emotion import TASKS as tasks
            case "train":
                if emotion_enabled:
                    from tau_emotion_bench.envs.telehealth.tasks_train import TASKS as tasks
                else:
                    from tau_emotion_bench.envs.telehealth.tasks_train_no_emotion import TASKS as tasks
            case "dev":
                if emotion_enabled:
                    from tau_emotion_bench.envs.telehealth.tasks_dev import TASKS as tasks
                else:
                    from tau_emotion_bench.envs.telehealth.tasks_dev_no_emotion import TASKS as tasks
            case _:
                raise ValueError(f"Unknown task split: {task_split}")
        super().__init__(
            data_load_func=load_data,
            tools=ALL_TOOLS,
            tasks=tasks,
            wiki=WIKI,
            rules=RULES,
            user_strategy=user_strategy,
            user_model=user_model,
            user_provider=user_provider,
            task_index=task_index,
            api_base=api_base,
        )
        self.terminate_tools = ["transfer_to_human_support"]