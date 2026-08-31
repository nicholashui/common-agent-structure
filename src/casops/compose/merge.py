"""Merge engine (spec §6.2–§6.3). Tools, plugins, credentials never inherit."""

from __future__ import annotations

from copy import deepcopy
from typing import Any


def _false_wins(left: Any, right: Any) -> Any:
    if left is False or right is False:
        return False
    if left is None:
        return right
    if right is None:
        return left
    return left


def _min_number(left: Any, right: Any) -> Any:
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        return min(left, right)
    if isinstance(left, (int, float)):
        return left
    return right


def _union_unique(left: list[Any], right: list[Any]) -> list[Any]:
    merged = list(left)
    for item in right:
        if item not in merged:
            merged.append(item)
    return merged


def _merge_bool_policy(child_policy: dict[str, Any], parent_policy: dict[str, Any]) -> dict[str, Any]:
    keys = list(child_policy) + [key for key in parent_policy if key not in child_policy]
    merged: dict[str, Any] = {}
    for key in keys:
        child_value = child_policy.get(key)
        parent_value = parent_policy.get(key)
        if isinstance(child_value, bool) or isinstance(parent_value, bool):
            merged[key] = _false_wins(child_value, parent_value)
        elif child_value is not None:
            merged[key] = child_value
        else:
            merged[key] = parent_value
    return merged


def merge_specs(child: dict[str, Any], parents: list[dict[str, Any]]) -> dict[str, Any]:
    merged = deepcopy(child)
    child_id = child.get("agent_id")
    merged["allowed_tools"] = list(child.get("allowed_tools") or [])
    merged["allowed_plugins"] = list(child.get("allowed_plugins") or [])

    budget = dict(child.get("budget_policy") or {})
    model = dict(child.get("model_policy") or {})
    does_not_own = list(child.get("does_not_own") or [])
    production = bool(child.get("production_activation_requested", False))
    safety = dict(child.get("safety_policy") or {})
    critique_in = list((child.get("critique_edges") or {}).get("inputs") or [])
    critique_out = list((child.get("critique_edges") or {}).get("outputs") or [])
    refinement = child.get("max_refinement_count")
    inherited_prompt_refs: list[dict[str, str]] = []
    inherited_rubric_refs: list[dict[str, str]] = []

    for parent in parents:
        parent_id = str(parent.get("agent_id") or "")
        parent_budget = parent.get("budget_policy") or {}
        for key, value in parent_budget.items():
            if isinstance(value, (int, float)):
                if key in budget and isinstance(budget[key], (int, float)):
                    budget[key] = min(budget[key], value)
                elif key not in budget:
                    budget[key] = value
        parent_model = parent.get("model_policy") or {}
        model["network_access"] = _false_wins(
            model.get("network_access"), parent_model.get("network_access")
        )
        for item in parent.get("does_not_own") or []:
            if item not in does_not_own:
                does_not_own.append(item)
        production = bool(_false_wins(production, parent.get("production_activation_requested")))
        parent_safety = parent.get("safety_policy") or {}
        if parent_safety:
            safety = _merge_bool_policy(safety, parent_safety)
        parent_edges = parent.get("critique_edges") or {}
        critique_in = _union_unique(critique_in, list(parent_edges.get("inputs") or []))
        critique_out = _union_unique(critique_out, list(parent_edges.get("outputs") or []))
        refinement = _min_number(refinement, parent.get("max_refinement_count"))
        parent_prompt = parent.get("prompt_reference")
        if parent_prompt and parent_prompt != child.get("prompt_reference"):
            inherited_prompt_refs.append({"agent_id": parent_id, "ref": parent_prompt})
        parent_rubric = parent.get("rubric_reference")
        if parent_rubric and parent_rubric != child.get("rubric_reference"):
            inherited_rubric_refs.append({"agent_id": parent_id, "ref": parent_rubric})

    if budget:
        merged["budget_policy"] = budget
    if model:
        merged["model_policy"] = model
    if does_not_own:
        merged["does_not_own"] = does_not_own
    merged["production_activation_requested"] = production
    if safety:
        merged["safety_policy"] = safety
    if critique_in or critique_out:
        merged["critique_edges"] = {
            "inputs": [item for item in critique_in if item != child_id],
            "outputs": [item for item in critique_out if item != child_id],
        }
    if isinstance(refinement, (int, float)):
        merged["max_refinement_count"] = refinement
    if inherited_prompt_refs:
        merged["inherited_prompt_refs"] = inherited_prompt_refs
    if inherited_rubric_refs:
        merged["inherited_rubric_refs"] = inherited_rubric_refs
    merged.pop("credentials", None)
    return merged
