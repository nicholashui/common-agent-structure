"""Extract declared agent inputs and outputs from a folder spec."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def as_string_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    items: list[str] = []
    for item in value:
        text = str(item).strip()
        if text and text not in items:
            items.append(text)
    return items


def _load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def plugin_interfaces(folder: Path) -> list[dict[str, str]]:
    payload = _load_json(folder / "plugins" / "registry.json")
    rows: list[dict[str, str]] = []
    for plugin in payload.get("plugins") or []:
        if not isinstance(plugin, dict):
            continue
        plugin_id = str(plugin.get("id") or plugin.get("plugin_id") or "").strip()
        input_schema = str(plugin.get("input_schema") or "").strip()
        output_schema = str(plugin.get("output_schema") or "").strip()
        if not plugin_id or not (input_schema or output_schema):
            continue
        rows.append(
            {
                "id": plugin_id,
                "input_schema": input_schema,
                "output_schema": output_schema,
            }
        )
    return rows


def protocol_names(folder: Path) -> list[str]:
    payload = _load_json(folder / "protocols" / "compatibility.json")
    names: list[str] = []
    for item in payload.get("protocols") or []:
        if isinstance(item, str):
            text = item.strip()
        elif isinstance(item, dict):
            text = str(item.get("id") or item.get("name") or "").strip()
        else:
            text = ""
        if text and text not in names:
            names.append(text)
    return names


def io_from_spec(
    spec: dict[str, Any],
    *,
    folder: Path | None = None,
    merged: bool = False,
) -> dict[str, Any]:
    edges = spec.get("critique_edges") if isinstance(spec.get("critique_edges"), dict) else None
    inputs = as_string_list((edges or {}).get("inputs"))
    outputs = as_string_list((edges or {}).get("outputs"))
    plugins = plugin_interfaces(folder) if folder is not None else []
    protocols = protocol_names(folder) if folder is not None else []
    defined = bool(inputs or outputs or plugins)
    if edges is not None:
        source = "critique_edges"
    elif plugins:
        source = "plugin_interfaces"
    else:
        source = "none"
    return {
        "defined": defined,
        "merged": merged,
        "source": source,
        "inputs": inputs,
        "outputs": outputs,
        "role": str(spec.get("role") or ""),
        "prompt_reference": str(spec.get("prompt_reference") or ""),
        "rubric_reference": str(spec.get("rubric_reference") or ""),
        "protocols": protocols,
        "plugin_interfaces": plugins,
    }


def folder_io(
    folder: Path,
    *,
    spec: dict[str, Any] | None = None,
    merged: bool = False,
) -> dict[str, Any]:
    payload = spec if spec is not None else _load_json(folder / "agent_spec.json")
    return io_from_spec(payload, folder=folder, merged=merged)


def spec_io_snapshot(spec: dict[str, Any]) -> dict[str, Any]:
    edges = spec.get("critique_edges") if isinstance(spec.get("critique_edges"), dict) else {}
    return {
        "role": str(spec.get("role") or ""),
        "prompt_reference": str(spec.get("prompt_reference") or ""),
        "rubric_reference": str(spec.get("rubric_reference") or ""),
        "critique_edges": {
            "inputs": as_string_list(edges.get("inputs")),
            "outputs": as_string_list(edges.get("outputs")),
        },
    }
