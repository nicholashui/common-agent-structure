"""Listed improve_agents ids have content tests, extra Chat fixtures, and gated skills."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema

from casops.auth.permissions import granted_tools, load_register, skill_granted
from casops.compose.skills import resolve_skills
from casops.runtime.chat import operational_prompt, pack_chat_context

REPO = Path(__file__).resolve().parents[2]
SCHEMA = json.loads((REPO / "schemas" / "eval" / "testcase.schema.json").read_text(encoding="utf-8"))
LIST = REPO / "improve_agents" / "agent_list.txt"


def _listed() -> list[str]:
    ids: list[str] = []
    for line in LIST.read_text(encoding="utf-8").splitlines():
        item = line.strip()
        if item and not item.startswith("#"):
            ids.append(item)
    return ids


def _extra_chat_fixtures(folder: Path) -> list[Path]:
    out: list[Path] = []
    root = folder / "evals" / "fixtures"
    if not root.is_dir():
        return out
    for path in sorted(root.glob("chat-*.json")):
        if path.name.startswith("chat-tc"):
            continue
        out.append(path)
    return out


def test_every_listed_agent_has_content_test_guide_and_sample_trees() -> None:
    missing: list[str] = []
    for agent_id in _listed():
        folder = REPO / "agents" / agent_id
        if not (folder / "content" / "test_guide.md").is_file():
            missing.append(f"{agent_id}:test_guide")
            continue
        guide = (folder / "content" / "test_guide.md").read_text(encoding="utf-8")
        for needle in ("Chat", "API", "/api/v3", "multi-agent", "CHARACTERIZATION"):
            if needle not in guide:
                missing.append(f"{agent_id}:guide_missing:{needle}")
        if "≥95%" in guide and "unmeasured" not in guide.lower() and "not" not in guide.lower():
            missing.append(f"{agent_id}:invented_pass_threshold")
        for rel in (
            "content/tests/chat/catalog.md",
            "content/tests/api/01-valid-chat.json",
            "content/tests/api/08-rate-limit-honesty.md",
            "content/tests/multi-agent/README.md",
            "content/research/sources.md",
        ):
            if not (folder / rel).is_file():
                missing.append(f"{agent_id}:{rel}")
        extras = _extra_chat_fixtures(folder)
        if len(extras) < 10:
            missing.append(f"{agent_id}:extra_chat:{len(extras)}")
    assert missing == []


def test_listed_extra_chat_fixtures_are_fail_closed_characterization() -> None:
    bad: list[str] = []
    for agent_id in _listed():
        folder = REPO / "agents" / agent_id
        extras = _extra_chat_fixtures(folder)
        if len(extras) < 10:
            bad.append(f"{agent_id}:need ≥10 extra chat fixtures")
            continue
        for path in extras:
            payload = json.loads(path.read_text(encoding="utf-8"))
            try:
                jsonschema.validate(payload, SCHEMA)
            except jsonschema.ValidationError as exc:
                bad.append(f"{agent_id}:{path.name}:{exc.message}")
                continue
            if payload.get("schema_version") != "casops.testcase.v1":
                bad.append(f"{agent_id}:{path.name}:schema_version")
            if payload.get("agent_id") != agent_id:
                bad.append(f"{agent_id}:{path.name}:agent_id")
            if payload.get("path") != "chat":
                bad.append(f"{agent_id}:{path.name}:path")
            if payload.get("honesty") != "CHARACTERIZATION":
                bad.append(f"{agent_id}:{path.name}:honesty")
            expect = payload.get("expect") or {}
            if expect.get("memory_writes") != []:
                bad.append(f"{agent_id}:{path.name}:memory")
            if expect.get("plugins_executed") is not False:
                bad.append(f"{agent_id}:{path.name}:plugins")
            if expect.get("t3_enabled") is not False:
                bad.append(f"{agent_id}:{path.name}:t3")
            if expect.get("network_granted") is not False:
                bad.append(f"{agent_id}:{path.name}:network")
            if expect.get("io_declared_fetched") is not False:
                bad.append(f"{agent_id}:{path.name}:fetched")
            if expect.get("path_id") != "chat":
                bad.append(f"{agent_id}:{path.name}:path_id")
            message = str((payload.get("input") or {}).get("message") or "")
            if agent_id not in message:
                bad.append(f"{agent_id}:{path.name}:unnamed")
            if len(message) < 400:
                bad.append(f"{agent_id}:{path.name}:short")
    assert bad == []


def test_listed_agents_skills_are_declared_not_resolved() -> None:
    register = load_register(REPO / "permissions" / "register.json")
    bad: list[str] = []
    for agent_id in _listed():
        folder = REPO / "agents" / agent_id
        spec = json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))
        if spec.get("allowed_tools") != []:
            bad.append(f"{agent_id}:allowed_tools")
        resolved = resolve_skills([folder])
        if resolved.get("enabled"):
            bad.append(f"{agent_id}:enabled:{resolved.get('enabled')}")
        rows = resolved.get("bindings") or []
        if not rows:
            bad.append(f"{agent_id}:no_declared_skill")
            continue
        for item in rows:
            skill_id = str(item.get("skill_id") or "")
            if item.get("resolved_enabled"):
                bad.append(f"{agent_id}:resolved:{skill_id}")
            if item.get("host_permission"):
                bad.append(f"{agent_id}:host_permission:{skill_id}")
            if item.get("operator_toggle") is not False:
                bad.append(f"{agent_id}:toggle:{skill_id}")
            if item.get("tools"):
                bad.append(f"{agent_id}:skill_tools:{skill_id}")
            if skill_granted(agent_id, skill_id, register=register):
                bad.append(f"{agent_id}:register_grant:{skill_id}")
        if granted_tools(agent_id, ["web_search"], register=register):
            bad.append(f"{agent_id}:register_tools")
        grant = (register.get("grants") or {}).get(agent_id) or {}
        if grant.get("skills") not in ([], None):
            bad.append(f"{agent_id}:register_skills_not_empty")
        if grant.get("tools") not in ([], None):
            bad.append(f"{agent_id}:register_tools_not_empty")
        packed = pack_chat_context(folder, spec, {}, message="ping", history=[])
        if packed["public"]["skills"] != []:
            bad.append(f"{agent_id}:packed_skills")
        if "skills/SKILL.md" not in packed["public"]["omitted"]:
            bad.append(f"{agent_id}:skill_not_omitted")
        op = operational_prompt((folder / "prompts" / "primary.md").read_text(encoding="utf-8"))
        if "How to reply" not in op:
            bad.append(f"{agent_id}:howto")
        if "Domain knowledge" not in op:
            bad.append(f"{agent_id}:domain")
        if "## Developer" in op or "Sora 2 API" in op:
            bad.append(f"{agent_id}:developer_leaked")
        if agent_id not in op and agent_id.split(".")[-1] not in op:
            bad.append(f"{agent_id}:unnamed_in_pack")
        task = next(item for item in packed["public"]["segments"] if item["name"] == "task")
        if task.get("clipped"):
            bad.append(f"{agent_id}:task_clipped:{task.get('tokens')}")
    assert bad == []
