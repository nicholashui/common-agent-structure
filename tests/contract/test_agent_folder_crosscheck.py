"""Scan every agents/*/agent_spec.json folder and cross-check host contract + Chat packing."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema

from casops.compose.folders import list_agent_ids, locate_agent_folder
from casops.registry.folder import validate_required_files
from casops.runtime.chat import operational_prompt

_UNTRUSTED_LIVE = ("production-ready", "production-grade")


def _spec_research_and_distillation(text: str) -> tuple[str, str]:
    if "### Domain knowledge (research)" not in text:
        return "", ""
    after = text.split("### Domain knowledge (research)", 1)[1]
    if "### Domain distillation" not in after:
        return after.strip(), ""
    research, dist = after.split("### Domain distillation", 1)
    dist_body = dist.split("\n", 1)[-1]
    if "\n## " in dist_body:
        dist_body = dist_body.split("\n## ", 1)[0]
    return research.strip(), dist_body.strip()


def _first_paragraph(text: str) -> str:
    for block in text.split("\n\n"):
        block = block.strip()
        if block:
            return " ".join(block.split())
    return ""

REPO = Path(__file__).resolve().parents[2]
SCHEMA = json.loads((REPO / "schemas" / "agent" / "agent_spec.schema.json").read_text(encoding="utf-8"))


def test_every_scanned_agent_folder_matches_fail_closed_contract() -> None:
    agents_root = REPO / "agents"
    ids = list_agent_ids(agents_root)
    assert ids, "scan found no agents"
    bad: list[str] = []
    seen: set[str] = set()
    for agent_id in ids:
        if agent_id in seen:
            bad.append(f"{agent_id}:duplicate agent_id")
        seen.add(agent_id)
        folder = locate_agent_folder(agents_root, agent_id)
        if folder is None:
            bad.append(f"{agent_id}:unlocated")
            continue
        check = validate_required_files(folder)
        if not check.ok:
            bad.append(f"{agent_id}:required:{','.join(check.missing)}")
        spec = json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))
        try:
            jsonschema.validate(spec, SCHEMA)
        except jsonschema.ValidationError as exc:
            bad.append(f"{agent_id}:schema:{exc.message}")
        if spec.get("agent_id") != agent_id:
            bad.append(f"{agent_id}:spec_id:{spec.get('agent_id')}")
        if spec.get("production_activation_requested") is not False:
            bad.append(f"{agent_id}:production")
        if spec.get("allowed_tools") != []:
            bad.append(f"{agent_id}:tools")
        if spec.get("allowed_plugins") != []:
            bad.append(f"{agent_id}:plugins")
        if (spec.get("model_policy") or {}).get("network_access") is not False:
            bad.append(f"{agent_id}:network")
        if (spec.get("model_policy") or {}).get("provider") != "local_deterministic":
            bad.append(f"{agent_id}:provider")
        if agent_id.startswith("specials.") and spec.get("va_category") not in (None, "", "null"):
            bad.append(f"{agent_id}:va_category")
        memory = json.loads((folder / "memory" / "policy.json").read_text(encoding="utf-8"))
        if memory.get("mode") != "none":
            bad.append(f"{agent_id}:memory_mode")
        plugins = json.loads((folder / "plugins" / "registry.json").read_text(encoding="utf-8"))
        if plugins.get("plugins") != []:
            bad.append(f"{agent_id}:plugin_registry")
        cache = json.loads((folder / "runtime" / "cache.json").read_text(encoding="utf-8"))
        if cache.get("t3_enabled") is True or "T3" in (cache.get("tiers") or []):
            bad.append(f"{agent_id}:t3")
        ctx = json.loads((folder / "runtime" / "context.json").read_text(encoding="utf-8"))
        segs = ctx.get("segments") or {}
        if segs.get("memory") not in (0, None) or segs.get("tools") not in (0, None):
            bad.append(f"{agent_id}:context_budgets")
        bindings = json.loads((folder / "skills" / "bindings.json").read_text(encoding="utf-8"))
        if bindings.get("special_skills") not in ([], None):
            bad.append(f"{agent_id}:special_skills")
        rows = bindings.get("bindings") or []
        if rows:
            from casops.compose.skills import resolve_skills

            resolved = resolve_skills([folder])
            if resolved.get("enabled"):
                bad.append(f"{agent_id}:skills_resolved_enabled")
            for item in resolved.get("bindings") or []:
                if item.get("resolved_enabled"):
                    bad.append(f"{agent_id}:skill_live:{item.get('skill_id')}")
                if item.get("host_permission"):
                    bad.append(f"{agent_id}:host_permission_grant:{item.get('skill_id')}")
                extra_tools = [str(t) for t in (item.get("tools") or []) if str(t).strip()]
                if extra_tools:
                    bad.append(f"{agent_id}:skill_tools:{item.get('skill_id')}")
            raw_tools = []
            for raw in rows:
                if isinstance(raw, dict):
                    raw_tools.extend(str(t) for t in (raw.get("tools") or []) if str(t).strip())
            if raw_tools:
                bad.append(f"{agent_id}:binding_tools")
        integ_path = folder / "skills" / "integration.json"
        if integ_path.is_file():
            integ = json.loads(integ_path.read_text(encoding="utf-8"))
            if isinstance(integ, dict) and integ.get("bindings") not in ([], None):
                bad.append(f"{agent_id}:integration_bindings")
        prompt = (folder / str(spec.get("prompt_reference") or "prompts/primary.md")).read_text(encoding="utf-8")
        packed = operational_prompt(prompt)
        if "Sora 2 API" in packed or "## Developer" in packed:
            bad.append(f"{agent_id}:packed_developer")
        if "How to reply" not in packed:
            bad.append(f"{agent_id}:packed_howto")
        if "Domain knowledge" not in packed:
            bad.append(f"{agent_id}:packed_domain")
        if agent_id not in packed and agent_id not in (folder / "SPEC.md").read_text(encoding="utf-8"):
            bad.append(f"{agent_id}:identity_unnamed")
        study = folder / "sources" / "study" / "domain_knowledge.md"
        if not study.is_file():
            bad.append(f"{agent_id}:no_study")
        compute = json.loads((folder / "runtime" / "compute_controller.json").read_text(encoding="utf-8"))
        if compute.get("agent_id") not in (None, agent_id):
            bad.append(f"{agent_id}:compute_id")
    assert bad == []


def test_specials_spec_research_is_not_untrusted_dump() -> None:
    """Help Spec Domain knowledge is cited craft only; vendor dumps stay under Domain distillation."""
    agents_root = REPO / "agents"
    ids = [agent_id for agent_id in list_agent_ids(agents_root) if agent_id.startswith("specials.")]
    assert ids, "scan found no specials"
    bad: list[str] = []
    for agent_id in ids:
        folder = locate_agent_folder(agents_root, agent_id)
        assert folder is not None
        text = (folder / "SPEC.md").read_text(encoding="utf-8")
        research, distillation = _spec_research_and_distillation(text)
        if not research:
            bad.append(f"{agent_id}:missing_research")
            continue
        lowered = research.lower()
        for token in _UNTRUSTED_LIVE:
            if token in lowered and "untrusted" not in lowered:
                bad.append(f"{agent_id}:{token}")
        needle = _first_paragraph(distillation)[:80]
        if len(needle) >= 40 and needle in " ".join(research.split()):
            bad.append(f"{agent_id}:research_duplicates_distillation")
    assert bad == []
