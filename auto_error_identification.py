# Copyright Sierra

import json
import argparse
from collections import Counter
from enum import Enum
from pydantic import BaseModel, Field
from tau_emotion_bench.model_utils import default_api_from_args, API
from tau_emotion_bench.envs.airline.tasks_test import TASKS as AIRLINE_TASKS
from tau_emotion_bench.envs.retail.tasks_test import TASKS as RETAIL_TASKS
from tau_emotion_bench.envs.telecom.tasks_test import TASKS as TELECOM_TASKS
from tau_emotion_bench.envs.telehealth.tasks_test import TASKS as TELEHEALTH_TASKS
from tau_emotion_bench.model_utils.args import api_parser
from tau_emotion_bench.types import Task, Action
from typing import List, Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor

def get_args() -> argparse.Namespace:
    parser = api_parser()
    for action in parser._actions:
        if action.dest == "platform":
            action.required = False
            action.default = "vllm-chat"
            break
    parser.add_argument("--env", type=str, required=True, choices=["airline", "retail", "telecom", "telehealth"], help="The environment that the original trajectories are from (used to fetch the user instructions)")
    parser.add_argument("--results-path", type=str, help="Path to the results file")
    parser.add_argument("--max-concurrency", type=int, default=1, help="Maximum number of concurrent API calls")
    parser.add_argument("--output-path", type=str, required=True, help="Path to the output file")
    parser.add_argument("--max-num-failed-results", "-n", type=int, help="Maximum number of failed results to analyze")
    return parser.parse_args()

class OriginalResult(BaseModel):
    task_id: int
    user_instruction: str
    traj: List[Dict[str, Any]]
    ground_truth_actions: List[Action]
    ground_truth_outputs: List[str]

class FaultAuthor(str, Enum):
    USER = "user"
    AGENT = "agent"
    ENVIRONMENT = "environment"

class FaultCategory(str, Enum):
    MISSING_OR_EXTRA_ACTION = "missing_or_extra_action"
    WRONG_TOOL_CALL         = "wrong_tool_call"
    INCOMPLETE              = "incomplete"
    INTEGRITY               = "integrity"
    META                    = "meta"

class FaultSubtype(str, Enum):
    # MISSING_OR_EXTRA_ACTION
    MISSING_REQUIRED_ACTION   = "missing_required_action"
    EXTRA_UNAUTHORIZED_ACTION = "extra_unauthorized_action"
    WRONG_ACTION_ORDER        = "wrong_action_order"
    # WRONG_TOOL_CALL
    CALLED_WRONG_TOOL              = "called_wrong_tool"
    WRONG_VALUE                    = "wrong_value"
    WRONG_PAYMENT_OR_REFUND_TARGET = "wrong_payment_or_refund_target"
    WRONG_RECIPIENT_OR_ACCOUNT     = "wrong_recipient_or_account"
    # INCOMPLETE
    GOAL_PARTIALLY_COMPLETED   = "goal_partially_completed"
    MISINTERPRETED_USER_INTENT = "misinterpreted_user_intent"
    # INTEGRITY
    HALLUCINATED_TOOL_RESULT = "hallucinated_tool_result"
    AUTHENTICATION_FAILURE   = "authentication_failure"
    # META
    FALSE_POSITIVE_FAULT = "false_positive_fault"

SUBTYPE_TO_CATEGORY: Dict[FaultSubtype, FaultCategory] = {
    FaultSubtype.MISSING_REQUIRED_ACTION:        FaultCategory.MISSING_OR_EXTRA_ACTION,
    FaultSubtype.EXTRA_UNAUTHORIZED_ACTION:      FaultCategory.MISSING_OR_EXTRA_ACTION,
    FaultSubtype.WRONG_ACTION_ORDER:             FaultCategory.MISSING_OR_EXTRA_ACTION,
    FaultSubtype.CALLED_WRONG_TOOL:              FaultCategory.WRONG_TOOL_CALL,
    FaultSubtype.WRONG_VALUE:                    FaultCategory.WRONG_TOOL_CALL,
    FaultSubtype.WRONG_PAYMENT_OR_REFUND_TARGET: FaultCategory.WRONG_TOOL_CALL,
    FaultSubtype.WRONG_RECIPIENT_OR_ACCOUNT:     FaultCategory.WRONG_TOOL_CALL,
    FaultSubtype.GOAL_PARTIALLY_COMPLETED:       FaultCategory.INCOMPLETE,
    FaultSubtype.MISINTERPRETED_USER_INTENT:     FaultCategory.INCOMPLETE,
    FaultSubtype.HALLUCINATED_TOOL_RESULT:       FaultCategory.INTEGRITY,
    FaultSubtype.AUTHENTICATION_FAILURE:         FaultCategory.INTEGRITY,
    FaultSubtype.FALSE_POSITIVE_FAULT:           FaultCategory.META,
}

class EmotionalOutcome(str, Enum):
    NONE                = "none"
    USER_ABANDONED      = "user_abandoned"

class EmotionalSubreason(str, Enum):
    NONE                = "none"
    DISMISSIVE_TONE     = "dismissive_tone"
    STEAMROLLED_CUES    = "steamrolled_cues"
    PROCEDURAL_FRICTION = "procedural_friction"
    EMOTIONAL_NEGLECT   = "emotional_neglect"

class FaultInstance(BaseModel):
    subtype: FaultSubtype = Field(..., description="The specific fault subtype that best describes this fault.")
    message_index: int = Field(..., description="0-indexed position in the (non-system) trajectory messages where this fault first manifests.")
    description: str = Field(..., description="One-sentence justification grounded in the functional difference between trajectory and ground truth.")

class JudgeResult(BaseModel):
    faults: List[FaultInstance] = Field(default_factory=list, description="All distinct faults present in the trajectory. Empty list means the trajectory is correct.")
    emotional_outcome: EmotionalOutcome = Field(..., description="Whether the simulated user abandoned the conversation due to the agent's emotional/relational handling.")
    emotional_subreason: EmotionalSubreason = Field(EmotionalSubreason.NONE, description="If emotional_outcome is user_abandoned, the dominant reason. Otherwise 'none'.")

class FaultAssignmentResult(BaseModel):
    task_id: int
    author: FaultAuthor
    description: str

    def model_dump(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "author": self.author.value,
            "description": self.description,
        }

class FaultTypeResult(BaseModel):
    task_id: int
    faults: List[FaultInstance] = Field(default_factory=list)
    emotional_outcome: EmotionalOutcome = EmotionalOutcome.NONE
    emotional_subreason: EmotionalSubreason = EmotionalSubreason.NONE

    def model_dump(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "faults": [
                {
                    "category": SUBTYPE_TO_CATEGORY[f.subtype].value,
                    "subtype": f.subtype.value,
                    "message_index": f.message_index,
                    "description": f.description,
                }
                for f in self.faults
            ],
            "emotional_outcome": self.emotional_outcome.value,
            "emotional_subreason": self.emotional_subreason.value,
        }

class GradingStrategy(Enum):
    ACTIONS = "actions"
    OUTPUTS = "outputs"

def context_description(grading_strategy: GradingStrategy) -> str:
    if grading_strategy == GradingStrategy.ACTIONS:
        return """You will be given a user instruction, the ground truth action sequence, and a trajectory.
- The user instruction is the instruction given to the simulated user.
- The ground truth action sequence is one example of a valid sequence of actions that lead to the goal state (the sequence of actions could be empty, meaning that no action should have been taken).
- The trajectory is the sequence of messages between the user and the agent.
- The trajectory has been determined to have a fault."""
    return """You will be given a user instruction, the set of required agent response outputs, and a trajectory.
- The user instruction is the instruction given to the simulated user.
- The required agent response outputs are the set of outputs that the agent is expected to communicate to the user.
- The trajectory is the sequence of messages between the user and the agent.
- The trajectory has been determined to have a fault."""

def display_traj(traj: List[Dict[str, Any]]) -> str:
    if len(traj) == 0:
        raise ValueError("Trajectory is empty")
    stripped_traj = [item for item in traj if item["role"] != "system"]
    return "\n".join([f"[{i}] {item['role'].capitalize()}: {item['content']}" for i, item in enumerate(stripped_traj)])

def display_actions(actions: List[Action]) -> str:
    return json.dumps([action.model_dump() for action in actions], indent=4)

def display_context(user_instruction: str, ground_truth_actions: List[Action], ground_truth_outputs: List[str], trajectory: List[Dict[str, Any]]) -> str:
    traj_display = display_traj(trajectory)
    context = f"""----- start user instruction -----
{user_instruction}
----- end user instruction -----"""
    if len(ground_truth_outputs) > 0:
        context += f"""

----- start required outputs -----
{ground_truth_outputs}
----- end required outputs -----"""
    else:
        context += f"""

----- start ground truth action sequence -----
{display_actions(ground_truth_actions)}
----- end ground truth action sequence -----

----- start trajectory -----
{traj_display}
----- end trajectory -----\n"""
    return context

FAULT_SUBTYPE_GUIDE = """Fault subtype definitions (each fault must use exactly one subtype):

MISSING_OR_EXTRA_ACTION:
  - missing_required_action: a tool call required by the ground truth was not made.
  - extra_unauthorized_action: the agent made a state-changing tool call not present in the ground truth.
  - wrong_action_order: the right tools were called but in an order that violates a required prerequisite.
WRONG_TOOL_CALL:
  - called_wrong_tool: the agent invoked a tool different from the one required.
  - wrong_value: correct tool, but a wrong literal value (date, amount, id, etc.).
  - wrong_payment_or_refund_target: payment or refund routed to the wrong method/destination.
  - wrong_recipient_or_account: action applied to the wrong user/account/resource.
INCOMPLETE:
  - goal_partially_completed: some required outcomes were achieved but the goal is not fully met.
  - misinterpreted_user_intent: agent followed the user's literal phrasing in a way that contradicted the underlying instruction goal.
INTEGRITY:
  - hallucinated_tool_result: agent stated a tool outcome (e.g. "no interactions found") without actually calling the tool, or fabricated tool output.
  - authentication_failure: agent skipped, mishandled, or wrongly rejected user authentication.
META:
  - false_positive_fault: after careful review, the trajectory is actually functionally correct and matches the ground truth; no real fault exists.

Emit one FaultInstance per distinct fault. If multiple faults of the same subtype occur, emit one instance per occurrence with different message_index values. If the trajectory is functionally correct, return an empty faults list (do NOT emit false_positive_fault unless an upstream signal claimed a fault and you disagree).

Emotional outcome:
  - user_abandoned: the simulated user terminated the conversation early (look for the literal token '###UNSATISFIED###' in a user message, or equivalent abandonment) due to the agent's emotional/relational handling.
  - none: otherwise.
Emotional subreason (only set when emotional_outcome is user_abandoned, else 'none'):
  - dismissive_tone: agent was curt, cold, or invalidating.
  - steamrolled_cues: agent ignored emotional cues the user provided and pushed transactional flow.
  - procedural_friction: excessive redundant questions, circular flow, unexplained delays.
  - emotional_neglect: user expressed need for reassurance/empathy and agent did not address it."""

def fault_assignment_analysis(api: API, results: List[OriginalResult], max_concurrency: int) -> List[FaultAssignmentResult]:
    def assign_fault(task_id: int, user_instruction: str, traj: List[Dict[str, Any]], ground_truth_actions: List[Action], ground_truth_outputs: List[str]) -> FaultAssignmentResult:
        idx_to_author = {
            0: FaultAuthor.USER,
            1: FaultAuthor.AGENT,
            2: FaultAuthor.ENVIRONMENT,
        }
        grading_strategy = GradingStrategy.OUTPUTS if len(ground_truth_outputs) > 0 else GradingStrategy.ACTIONS
        ctx_desc = context_description(grading_strategy)
        context = display_context(user_instruction, ground_truth_actions, ground_truth_outputs, traj)
        res = api.classify(
            instruction=f"{ctx_desc}\n\nDetermine the entity that is responsible for the fault. The user is responsible for the fault if they caused an action that was not grounded in the user instruction. The agent is responsible for the fault if they took an action that was not correct (or took the action with the wrong arguments). The environment is responsible for all other faults.",
            text=context,
            options=["The user", "The agent", "The environment (neither user nor agent)"],
        )
        author = idx_to_author[res]
        description = api.generate(
            instruction=f"{ctx_desc}\n\nDescribe the reason why {author.value} is responsible for the fault in the trajectory. Be concise and only focus on the functional differences between the ground truth and the trajectory.",
            text=context,
        )
        return FaultAssignmentResult(task_id=task_id, author=author, description=description)
    with ThreadPoolExecutor(max_workers=max_concurrency) as executor:
        task_ids = [r.task_id for r in results]
        user_instructions = [r.user_instruction for r in results]
        trajs = [r.traj for r in results]
        ground_truth_actions = [r.ground_truth_actions for r in results]
        ground_truth_outputs = [r.ground_truth_outputs for r in results]
        results = list(executor.map(assign_fault, task_ids, user_instructions, trajs, ground_truth_actions, ground_truth_outputs))
    return results


def fault_type_analysis(api: API, results: List[OriginalResult], max_concurrency: int) -> List[FaultTypeResult]:
    def get_fault_type(task_id: int, user_instruction: str, traj: List[Dict[str, Any]], ground_truth_actions: List[Action], ground_truth_outputs: List[str]) -> FaultTypeResult:
        grading_strategy = GradingStrategy.OUTPUTS if len(ground_truth_outputs) > 0 else GradingStrategy.ACTIONS
        ctx_desc = context_description(grading_strategy)
        context = display_context(user_instruction, ground_truth_actions, ground_truth_outputs, traj)
        instruction = (
            f"{ctx_desc}\n\n"
            "Identify ALL distinct faults the agent committed in this trajectory (multi-label). "
            "List every fault, not only the first. Two faults of the same subtype at different message indices count as two instances.\n\n"
            f"{FAULT_SUBTYPE_GUIDE}"
        )
        judged: JudgeResult = api.parse_force(
            instruction=instruction,
            typ=JudgeResult,
            text=context,
        )
        if isinstance(judged, dict):
            judged = JudgeResult(**judged)
        emo = judged.emotional_outcome
        sub = judged.emotional_subreason if emo == EmotionalOutcome.USER_ABANDONED else EmotionalSubreason.NONE
        return FaultTypeResult(
            task_id=task_id,
            faults=judged.faults,
            emotional_outcome=emo,
            emotional_subreason=sub,
        )
    with ThreadPoolExecutor(max_workers=max_concurrency) as executor:
        task_ids = [r.task_id for r in results]
        user_instructions = [r.user_instruction for r in results]
        trajs = [r.traj for r in results]
        ground_truth_actions = [r.ground_truth_actions for r in results]
        ground_truth_outputs = [r.ground_truth_outputs for r in results]
        results = list(executor.map(get_fault_type, task_ids, user_instructions, trajs, ground_truth_actions, ground_truth_outputs))
    return results

def _pct(n: int, d: int) -> str:
    return f"{round(n / d * 100, 2)}%" if d else "n/a"

def summarize_fault_types(fault_type_results: List[FaultTypeResult]) -> str:
    n_traj = len(fault_type_results)
    if n_traj == 0:
        return "No agent-caused trajectories to analyze."
    subtype_instance_counts: Counter = Counter()
    subtype_traj_counts: Counter = Counter()
    category_traj_counts: Counter = Counter()
    total_instances = 0
    n_with_at_least_one = 0
    for r in fault_type_results:
        if r.faults:
            n_with_at_least_one += 1
        seen_subtypes = set()
        seen_categories = set()
        for f in r.faults:
            total_instances += 1
            subtype_instance_counts[f.subtype] += 1
            seen_subtypes.add(f.subtype)
            seen_categories.add(SUBTYPE_TO_CATEGORY[f.subtype])
        for s in seen_subtypes:
            subtype_traj_counts[s] += 1
        for c in seen_categories:
            category_traj_counts[c] += 1
    emo_counts = Counter(r.emotional_outcome for r in fault_type_results)
    emo_sub_counts = Counter(r.emotional_subreason for r in fault_type_results if r.emotional_outcome == EmotionalOutcome.USER_ABANDONED)
    lines: List[str] = []
    lines.append(f"Trajectories analyzed (agent-caused): {n_traj}")
    lines.append(f"  - With >=1 functional fault: {n_with_at_least_one} ({_pct(n_with_at_least_one, n_traj)})")
    lines.append(f"  - Total fault instances: {total_instances} (avg {round(total_instances / n_traj, 2)} per trajectory)")
    lines.append("")
    lines.append("Functional fault categories (% of trajectories containing >=1 fault of this category):")
    for cat in FaultCategory:
        c = category_traj_counts.get(cat, 0)
        lines.append(f"  - {cat.value}: {c} ({_pct(c, n_traj)})")
    lines.append("")
    lines.append("Functional fault subtypes (trajectory count | instance count):")
    for sub in FaultSubtype:
        t = subtype_traj_counts.get(sub, 0)
        i = subtype_instance_counts.get(sub, 0)
        lines.append(f"  - {sub.value}: {t} traj ({_pct(t, n_traj)}) | {i} instances")
    lines.append("")
    lines.append("Emotional outcome:")
    for outcome in EmotionalOutcome:
        c = emo_counts.get(outcome, 0)
        lines.append(f"  - {outcome.value}: {c} ({_pct(c, n_traj)})")
    abandoned = emo_counts.get(EmotionalOutcome.USER_ABANDONED, 0)
    if abandoned > 0:
        lines.append("")
        lines.append("Emotional subreasons (among user_abandoned):")
        for sub in EmotionalSubreason:
            if sub == EmotionalSubreason.NONE:
                continue
            c = emo_sub_counts.get(sub, 0)
            lines.append(f"  - {sub.value}: {c} ({_pct(c, abandoned)})")
    return "\n".join(lines)

def main() -> None:
    args = get_args()
    api = default_api_from_args(args)
    with open(args.results_path, "r") as f:
        results = json.load(f)
    print(f"Loaded {len(results)} results")
    env = args.env
    if env == "airline":
        tasks: List[Task] = AIRLINE_TASKS
    elif env == "retail":
        tasks: List[Task] = RETAIL_TASKS
    elif env == "telecom":
        tasks: List[Task] = TELECOM_TASKS
    elif env == "telehealth":
        tasks: List[Task] = TELEHEALTH_TASKS
    else:
        raise ValueError(f"Invalid environment: {env}")
    failed_results = [r for r in results if r["reward"] <= 1e-3]
    print(f"Found {len(failed_results)} failed trajectories")
    if args.max_num_failed_results is not None and len(failed_results) > args.max_num_failed_results:
        print(f"Limiting to {args.max_num_failed_results} failed trajectories")
        failed_results = failed_results[:args.max_num_failed_results]
    original_results = []
    for result in failed_results:
        task_id: int = result["task_id"]
        task = tasks[task_id]
        user_instruction = task.instruction
        ground_truth_actions = task.actions
        ground_truth_outputs = task.outputs
        original_result = OriginalResult(task_id=task_id, user_instruction=user_instruction, traj=result["traj"], ground_truth_actions=ground_truth_actions, ground_truth_outputs=ground_truth_outputs)
        original_results.append(original_result)
    print(f"Performing fault assignment analysis on {len(original_results)} failed trajectories with a max concurrency of {args.max_concurrency}...")
    fault_assignment_results = fault_assignment_analysis(api=api, results=original_results, max_concurrency=args.max_concurrency)
    failures_due_to_agent = [original_results[i] for i, r in enumerate(fault_assignment_results) if r.author == FaultAuthor.AGENT]
    print(f"Performing fault type analysis on {len(failures_due_to_agent)} failures that have been marked as being caused by the agent with a max concurrency of {args.max_concurrency}...")
    fault_type_results = fault_type_analysis(api=api, results=failures_due_to_agent, max_concurrency=args.max_concurrency)
    n_total = len(fault_assignment_results)
    print(f"""Reviewed {n_total} trajectories:

Author fault distribution:
  - User: {sum(1 for r in fault_assignment_results if r.author == FaultAuthor.USER)} ({_pct(sum(1 for r in fault_assignment_results if r.author == FaultAuthor.USER), n_total)})
  - Agent: {sum(1 for r in fault_assignment_results if r.author == FaultAuthor.AGENT)} ({_pct(sum(1 for r in fault_assignment_results if r.author == FaultAuthor.AGENT), n_total)})
  - Environment (otherwise case): {sum(1 for r in fault_assignment_results if r.author == FaultAuthor.ENVIRONMENT)} ({_pct(sum(1 for r in fault_assignment_results if r.author == FaultAuthor.ENVIRONMENT), n_total)})

{summarize_fault_types(fault_type_results)}
""")
    with open(args.output_path, "w") as f:
        json.dump({
            "fault_assignment_analysis": [r.model_dump() for r in fault_assignment_results],
            "fault_type_analysis": [r.model_dump() for r in fault_type_results],
        }, f, indent=4)
    print(f"Saved results to {args.output_path}")

if __name__ == "__main__":
    main()
