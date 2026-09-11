"""Host permission register, not bindings.json, is the skill/tool grant."""

from __future__ import annotations

import json
from pathlib import Path

from casops.auth.permissions import granted_tools, load_register, skill_granted
from casops.compose.skills import resolve_skills
from casops.runtime.chat import pack_chat_context

REPO = Path(__file__).resolve().parents[2]
AGENT = "specials.intent-analysis-agent"
SKILL = "casops.skill.intent.speech-act"


def test_register_denies_intent_analysis_skill_and_tools() -> None:
    register = load_register(REPO / "permissions" / "register.json")
    assert skill_granted(AGENT, SKILL, register=register) is False
    assert granted_tools(AGENT, ["web_search"], register=register) == []
    assert granted_tools(AGENT, [], register=register) == []


def test_intent_analysis_skill_is_declared_not_resolved() -> None:
    folder = REPO / "agents" / AGENT
    resolved = resolve_skills([folder])
    ids = [item["skill_id"] for item in resolved["bindings"]]
    assert SKILL in ids
    assert resolved["enabled"] == []
    row = next(item for item in resolved["bindings"] if item["skill_id"] == SKILL)
    assert row["author_enabled"] is True
    assert row["operator_toggle"] is False
    assert row["host_permission"] is False
    assert row["resolved_enabled"] is False
    assert row.get("tools") == []


def test_binding_cannot_self_grant_host_permission(tmp_path: Path) -> None:
    folder = tmp_path / "agents" / "demo.gated"
    (folder / "skills").mkdir(parents=True)
    (folder / "agent_spec.json").write_text(
        json.dumps({"agent_id": "demo.gated", "allowed_tools": []}),
        encoding="utf-8",
    )
    (folder / "skills" / "bindings.json").write_text(
        json.dumps(
            {
                "bindings": [
                    {
                        "skill_id": "casops.skill.demo",
                        "enabled": True,
                        "author_enabled": True,
                        "inherited_enabled": True,
                        "operator_toggle": True,
                        "host_permission": True,
                        "tools": [],
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    (folder / "skills" / "toggles.json").write_text(
        json.dumps({"toggles": [{"skill_id": "casops.skill.demo", "enabled": True}]}),
        encoding="utf-8",
    )
    resolved = resolve_skills([folder])
    assert resolved["enabled"] == []
    assert resolved["bindings"][0]["host_permission"] is False


def test_host_register_grant_plus_operator_toggle_resolves(tmp_path: Path, monkeypatch) -> None:
    folder = tmp_path / "agents" / "demo.gated"
    (folder / "skills").mkdir(parents=True)
    (folder / "agent_spec.json").write_text(
        json.dumps({"agent_id": "demo.gated"}),
        encoding="utf-8",
    )
    (folder / "skills" / "bindings.json").write_text(
        json.dumps(
            {
                "bindings": [
                    {
                        "skill_id": "casops.skill.demo",
                        "enabled": True,
                        "author_enabled": True,
                        "inherited_enabled": True,
                        "operator_toggle": True,
                        "tools": [],
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    (folder / "skills" / "toggles.json").write_text(
        json.dumps(
            {
                "toggles": [
                    {
                        "skill_id": "casops.skill.demo",
                        "enabled": True,
                        "reason": "test grant",
                        "actor": "human_operator",
                        "time": "2026-09-11T12:00:00+08:00",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    register = tmp_path / "permissions" / "register.json"
    register.parent.mkdir(parents=True)
    register.write_text(
        json.dumps({"schema_version": "casops.host_permission.v1", "grants": {"demo.gated": {"skills": ["casops.skill.demo"], "tools": []}}}),
        encoding="utf-8",
    )
    monkeypatch.setenv("CASOPS_PERMISSION_REGISTER", str(register))
    resolved = resolve_skills([folder])
    assert [item["skill_id"] for item in resolved["enabled"]] == ["casops.skill.demo"]
    assert resolved["bindings"][0]["host_permission"] is True


def test_agentic_rag_skill_is_declared_not_resolved() -> None:
    folder = REPO / "agents" / "specials.agentic-rag-agent"
    resolved = resolve_skills([folder])
    ids = [item["skill_id"] for item in resolved["bindings"]]
    assert "casops.skill.rag.retrieve-decision" in ids
    assert resolved["enabled"] == []
    row = next(item for item in resolved["bindings"] if item["skill_id"] == "casops.skill.rag.retrieve-decision")
    assert row["host_permission"] is False
    assert row["resolved_enabled"] is False
    spec = json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))
    packed = pack_chat_context(folder, spec, {}, message="ping", history=[])
    assert packed["public"]["skills"] == []
    assert "skills/SKILL.md" in packed["public"]["omitted"]
    assert spec["allowed_tools"] == []


def test_agent_loop_creator_skill_is_declared_not_resolved() -> None:
    folder = REPO / "agents" / "specials.agent-loop-creator"
    resolved = resolve_skills([folder])
    ids = [item["skill_id"] for item in resolved["bindings"]]
    assert "casops.skill.loop.controlled-shape" in ids
    assert resolved["enabled"] == []
    row = next(item for item in resolved["bindings"] if item["skill_id"] == "casops.skill.loop.controlled-shape")
    assert row["host_permission"] is False
    assert row["resolved_enabled"] is False
    spec = json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))
    packed = pack_chat_context(folder, spec, {}, message="ping", history=[])
    assert packed["public"]["skills"] == []
    assert "skills/SKILL.md" in packed["public"]["omitted"]
    assert spec["allowed_tools"] == []


def test_general_creative_skill_is_declared_not_resolved() -> None:
    folder = REPO / "agents" / "specials.general-creative-agent"
    resolved = resolve_skills([folder])
    ids = [item["skill_id"] for item in resolved["bindings"]]
    assert "casops.skill.creative.sparse-recombination" in ids
    assert resolved["enabled"] == []
    row = next(item for item in resolved["bindings"] if item["skill_id"] == "casops.skill.creative.sparse-recombination")
    assert row["host_permission"] is False
    assert row["resolved_enabled"] is False
    spec = json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))
    packed = pack_chat_context(folder, spec, {}, message="ping", history=[])
    assert packed["public"]["skills"] == []
    assert "skills/SKILL.md" in packed["public"]["omitted"]
    assert spec["allowed_tools"] == []


def test_aesthetics_skill_is_declared_not_resolved() -> None:
    folder = REPO / "agents" / "specials.aesthetics-agent"
    resolved = resolve_skills([folder])
    ids = [item["skill_id"] for item in resolved["bindings"]]
    assert "casops.skill.aesthetics.dimension-vector" in ids
    assert resolved["enabled"] == []
    row = next(item for item in resolved["bindings"] if item["skill_id"] == "casops.skill.aesthetics.dimension-vector")
    assert row["host_permission"] is False
    assert row["resolved_enabled"] is False
    spec = json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))
    packed = pack_chat_context(folder, spec, {}, message="ping", history=[])
    assert packed["public"]["skills"] == []
    assert "skills/SKILL.md" in packed["public"]["omitted"]
    assert spec["allowed_tools"] == []


def test_intent_analysis_chat_still_omits_skill_file() -> None:
    folder = REPO / "agents" / AGENT
    spec = json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))
    packed = pack_chat_context(folder, spec, {}, message="ping", history=[])
    public = packed["public"]
    assert public["skills"] == []
    assert "skills/SKILL.md" in public["omitted"]
    assert spec["allowed_tools"] == []
    assert spec["production_activation_requested"] is False
