"""Skill enable-AND resolution (spec §16.1)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from casops.auth.permissions import (
    agent_id_from_folder,
    granted_tools,
    load_register,
    register_path,
    skill_granted,
)
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


def _load(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _flag(binding: dict[str, Any], name: str) -> bool:
    if name not in binding:
        return True
    return bool(binding[name])


def _normalize(binding: dict[str, Any]) -> dict[str, Any]:
    enabled = _flag(binding, "enabled")
    author = _flag(binding, "author_enabled")
    inherited = _flag(binding, "inherited_enabled")
    toggle = _flag(binding, "operator_toggle")
    declared = True
    tools = binding.get("tools") if isinstance(binding.get("tools"), list) else []
    return {
        "skill_id": binding["skill_id"],
        "source": binding.get("source"),
        "path": binding.get("path"),
        "enabled": enabled,
        "author_enabled": author,
        "inherited_enabled": inherited,
        "operator_toggle": toggle,
        "host_permission": False,
        "tools": [str(item) for item in tools],
        "resolved_enabled": False,
        "declared": declared,
    }


def _and_merge(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    combined = {
        "skill_id": left["skill_id"],
        "source": left.get("source") or right.get("source"),
        "path": left.get("path") or right.get("path"),
        "enabled": left["enabled"] and right["enabled"],
        "author_enabled": left["author_enabled"] and right["author_enabled"],
        "inherited_enabled": left["inherited_enabled"] and right["inherited_enabled"],
        "operator_toggle": left["operator_toggle"] and right["operator_toggle"],
        "host_permission": False,
        "tools": list(left.get("tools") or []) or list(right.get("tools") or []),
        "declared": True,
    }
    combined["resolved_enabled"] = False
    return combined


def _recompute(item: dict[str, Any]) -> dict[str, Any]:
    item["resolved_enabled"] = all(
        bool(item[name])
        for name in (
            "enabled",
            "author_enabled",
            "inherited_enabled",
            "operator_toggle",
            "host_permission",
        )
    )
    return item


def resolve_skills(folders: list[Path]) -> dict[str, Any]:
    combined: dict[str, dict[str, Any]] = {}
    child = folders[0] if folders else None
    agent_id = agent_id_from_folder(child) if child is not None else ""
    register = load_register(register_path(folder=child) if child is not None else None)
    for folder in folders:
        payload = _load(folder / "skills" / "bindings.json")
        for binding in payload.get("bindings") or []:
            skill_id = binding.get("skill_id")
            if not skill_id:
                raise CasopsError(ErrorCode.SKL_TOGGLE_UNKNOWN)
            normalized = _normalize(binding)
            if skill_id in combined:
                combined[skill_id] = _and_merge(combined[skill_id], normalized)
            else:
                combined[skill_id] = normalized
        toggles = _load(folder / "skills" / "toggles.json")
        for toggle in toggles.get("toggles") or []:
            skill_id = toggle.get("skill_id")
            if skill_id not in combined:
                raise CasopsError(ErrorCode.SKL_TOGGLE_UNKNOWN)
            if "enabled" in toggle:
                combined[skill_id]["operator_toggle"] = bool(toggle["enabled"]) and combined[
                    skill_id
                ]["operator_toggle"]
    for skill_id, item in combined.items():
        item["host_permission"] = skill_granted(agent_id, skill_id, register=register)
        declared_tools = [str(t) for t in (item.get("tools") or []) if str(t).strip()]
        if declared_tools:
            host_tools = granted_tools(agent_id, declared_tools, register=register)
            if host_tools != declared_tools:
                item["host_permission"] = False
        _recompute(item)
    bindings = list(combined.values())
    return {
        "bindings": bindings,
        "enabled": [item for item in bindings if item["resolved_enabled"]],
        "disabled": [item for item in bindings if not item["resolved_enabled"]],
        "agent_id": agent_id,
    }
