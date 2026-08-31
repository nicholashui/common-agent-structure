"""Validate plugin manifests without loading or executing code (WP-421)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

_EXEC_KEYS = ("entry", "module", "import", "code", "script")
_VALID_TIERS = {"I0", "I1", "I2", "I3", "none", ""}


def isolation_of(manifest: dict[str, Any]) -> str:
    field = manifest.get("isolation")
    if isinstance(field, dict):
        return str(field.get("tier") or "I0")
    return str(field or manifest.get("tier") or "I0")


def _resolve_under_agent_folder(folder: Path, ref: str) -> Path:
    candidate = Path(ref)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise CasopsError(ErrorCode.PLG_MANIFEST_INVALID)
    root = folder.resolve()
    target = (folder / candidate).resolve()
    try:
        target.relative_to(root)
    except ValueError as exc:
        raise CasopsError(ErrorCode.PLG_MANIFEST_INVALID) from exc
    return target


def validate_registry(folder: Path) -> dict[str, Any]:
    path = folder / "plugins" / "registry.json"
    payload = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {"plugins": []}
    plugins = list(payload.get("plugins") or [])
    validated: list[dict[str, Any]] = []
    for plugin in plugins:
        validated.append(validate_manifest(plugin, folder=folder))
    return {"plugins": validated, "count": len(validated)}


def validate_manifest(manifest: dict[str, Any], *, folder: Path | None = None) -> dict[str, Any]:
    if not isinstance(manifest, dict):
        raise CasopsError(ErrorCode.PLG_MANIFEST_INVALID)
    plugin_id = manifest.get("id") or manifest.get("plugin_id")
    if not plugin_id:
        raise CasopsError(ErrorCode.PLG_MANIFEST_INVALID)
    for key in _EXEC_KEYS:
        if key in manifest:
            # Presence of a code pointer is allowed as data; we never import it.
            pass
    isolation = isolation_of(manifest)
    if isolation not in _VALID_TIERS:
        raise CasopsError(ErrorCode.PLG_ISOLATION_TIER)
    origin = str(manifest.get("origin") or "first_party")
    signed = bool(manifest.get("signed", origin == "first_party"))
    if (origin != "first_party" or not signed) and isolation in {"I0", "I1", "none", ""}:
        raise CasopsError(ErrorCode.PLG_ISOLATION_TIER)
    permissions = manifest.get("permissions") or {}
    network = bool(permissions.get("network")) if isinstance(permissions, dict) else False
    if network and isolation != "I3":
        raise CasopsError(ErrorCode.PLG_ISOLATION_TIER)
    if folder is not None:
        ref = manifest.get("manifest")
        if ref:
            target = _resolve_under_agent_folder(folder, str(ref))
            if target.suffix.lower() in {".py", ".so", ".dll", ".exe"}:
                raise CasopsError(ErrorCode.PLG_MANIFEST_INVALID)
            if target.is_file() and target.suffix.lower() == ".json":
                json.loads(target.read_text(encoding="utf-8"))
    return {
        "id": plugin_id,
        "isolation": isolation or "I0",
        "validated": True,
        "executed": False,
    }
