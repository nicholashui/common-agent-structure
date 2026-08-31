"""Merge rules from spec §6.2 / §6.3."""

from casops.compose.merge import merge_specs


def test_tools_and_plugins_never_inherit() -> None:
    child = {"allowed_tools": [], "allowed_plugins": [], "budget_policy": {"max_job_ms": 10}}
    parent = {"allowed_tools": ["shell"], "allowed_plugins": ["wasm"], "budget_policy": {"max_job_ms": 99}}
    merged = merge_specs(child, [parent])
    assert merged["allowed_tools"] == []
    assert merged["allowed_plugins"] == []


def test_numeric_budgets_take_minimum() -> None:
    child = {"budget_policy": {"max_job_ms": 50, "max_model_calls": 3}}
    parent = {"budget_policy": {"max_job_ms": 20, "max_model_calls": 9}}
    merged = merge_specs(child, [parent])
    assert merged["budget_policy"]["max_job_ms"] == 20
    assert merged["budget_policy"]["max_model_calls"] == 3


def test_network_access_false_wins() -> None:
    child = {"model_policy": {"network_access": True}}
    parent = {"model_policy": {"network_access": False}}
    merged = merge_specs(child, [parent])
    assert merged["model_policy"]["network_access"] is False


def test_child_scalars_win() -> None:
    child = {"agent_id": "child", "role": "child", "prompt_reference": "child.md"}
    parent = {"agent_id": "parent", "role": "parent", "prompt_reference": "parent.md"}
    merged = merge_specs(child, [parent])
    assert merged["role"] == "child"
    assert merged["prompt_reference"] == "child.md"
    assert merged["inherited_prompt_refs"] == [
        {"agent_id": "parent", "ref": "parent.md"},
    ]


def test_refinement_count_is_minimum() -> None:
    child = {"max_refinement_count": 4}
    parent = {"max_refinement_count": 1, "agent_id": "p"}
    merged = merge_specs(child, [parent])
    assert merged["max_refinement_count"] == 1


def test_safety_tightening_inherits_relaxation_does_not() -> None:
    child = {"safety_policy": {"injection": True, "exfiltration": False}}
    parent = {"safety_policy": {"injection": False, "exfiltration": True}}
    merged = merge_specs(child, [parent])
    assert merged["safety_policy"]["injection"] is False
    assert merged["safety_policy"]["exfiltration"] is False


def test_critique_edges_union_without_self_edges() -> None:
    child = {
        "agent_id": "child",
        "critique_edges": {"inputs": ["a"], "outputs": ["child"]},
    }
    parent = {"agent_id": "p", "critique_edges": {"inputs": ["b"], "outputs": ["c"]}}
    merged = merge_specs(child, [parent])
    assert merged["critique_edges"]["inputs"] == ["a", "b"]
    assert "child" not in merged["critique_edges"]["outputs"]
    assert merged["critique_edges"]["outputs"] == ["c"]


def test_credentials_never_inherit() -> None:
    child = {"allowed_tools": []}
    parent = {"credentials": {"api_key": "secret"}, "allowed_tools": ["shell"]}
    merged = merge_specs(child, [parent])
    assert "credentials" not in merged
    assert merged["allowed_tools"] == []
