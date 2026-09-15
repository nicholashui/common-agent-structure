"""ISSUE-0009 P3: owned-path overlays. Chat hops stay OPTION/SELECTED; host applies after choice."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from casops.video_prompt.owners import OWNER_PATHS
from casops.video_prompt.schema import ClipObject, ClipSchemaError, validate_clip

CRITIC_ID = "video.critic"


class OwnershipError(ValueError):
    """Patch touched a path this agent does not own."""

    def __init__(self, agent_id: str, rejected: list[str]):
        self.agent_id = agent_id
        self.rejected = rejected
        super().__init__(f"{agent_id} cannot write {', '.join(rejected)}")


def strip_indices(path: str) -> str:
    parts = [part for part in path.split(".") if part and not part.isdigit()]
    return ".".join(parts)


def owned_prefixes(agent_id: str, granted: list[str] | tuple[str, ...] | None = None) -> tuple[str, ...]:
    base = tuple(OWNER_PATHS.get(agent_id) or ())
    extra = tuple(item for item in (granted or ()) if item)
    if agent_id == CRITIC_ID:
        return base + extra
    return base + extra


def path_allowed(agent_id: str, path: str, granted: list[str] | tuple[str, ...] | None = None) -> bool:
    norm = strip_indices(path)
    if not norm:
        return False
    if agent_id == CRITIC_ID and (
        norm == "diagnostics" or norm.startswith("diagnostics.") or norm.startswith("provenance.diagnostics")
    ):
        return True
    for prefix in owned_prefixes(agent_id, granted):
        if norm == prefix or norm.startswith(prefix + "."):
            return True
    return False


def _can_descend(agent_id: str, path: str, granted: list[str] | tuple[str, ...] | None = None) -> bool:
    if not path:
        return True
    if path_allowed(agent_id, path, granted):
        return True
    norm = strip_indices(path)
    for prefix in owned_prefixes(agent_id, granted):
        if prefix.startswith(norm + ".") if norm else True:
            return True
    if agent_id == CRITIC_ID:
        return True
    return False


def _ensure_container(dest: dict[str, Any], key: str, value: Any) -> Any:
    if isinstance(value, dict):
        dest[key] = {}
    else:
        dest[key] = []
    return dest[key]


def _merge_owned(
    dest: Any,
    src: Any,
    path: str,
    agent_id: str,
    granted: list[str] | tuple[str, ...] | None,
    applied: list[str],
    rejected: list[str],
) -> None:
    if isinstance(src, dict):
        if not isinstance(dest, dict):
            rejected.append(path or "(root)")
            return
        for key, value in src.items():
            child = f"{path}.{key}" if path else str(key)
            existing = dest.get(key)
            if isinstance(value, (dict, list)):
                if isinstance(value, dict) and isinstance(existing, dict):
                    _merge_owned(existing, value, child, agent_id, granted, applied, rejected)
                    continue
                if isinstance(value, list) and isinstance(existing, list):
                    _merge_owned(existing, value, child, agent_id, granted, applied, rejected)
                    continue
                if existing is None and _can_descend(agent_id, child, granted):
                    container = _ensure_container(dest, key, value)
                    _merge_owned(container, value, child, agent_id, granted, applied, rejected)
                    continue
                rejected.append(child)
                continue
            if path_allowed(agent_id, child, granted):
                dest[key] = value
                applied.append(child)
            else:
                rejected.append(child)
        return
    if isinstance(src, list):
        if not isinstance(dest, list):
            rejected.append(path)
            return
        if src and not isinstance(src[0], (dict, list)):
            if path_allowed(agent_id, path, granted):
                for item in src:
                    if item not in dest:
                        dest.append(item)
                applied.append(path)
            else:
                rejected.append(path)
            return
        for index, value in enumerate(src):
            child = f"{path}.{index}"
            if index >= len(dest):
                if not _can_descend(agent_id, child, granted) and not path_allowed(agent_id, child, granted):
                    rejected.append(child)
                    continue
                dest.append({} if isinstance(value, dict) else ([] if isinstance(value, list) else None))
            current = dest[index]
            if isinstance(value, dict) and isinstance(current, dict):
                _merge_owned(current, value, child, agent_id, granted, applied, rejected)
            elif isinstance(value, list) and isinstance(current, list):
                _merge_owned(current, value, child, agent_id, granted, applied, rejected)
            elif path_allowed(agent_id, child, granted):
                dest[index] = value
                applied.append(child)
            else:
                rejected.append(child)
        return
    if path_allowed(agent_id, path, granted):
        applied.append(path)
    else:
        rejected.append(path)


def _append_diagnostics(clip: dict[str, Any], agent_id: str, incoming: list[Any]) -> list[dict[str, Any]]:
    provenance = clip.setdefault("provenance", {})
    if not isinstance(provenance, dict):
        clip["provenance"] = {"diagnostics": []}
        provenance = clip["provenance"]
    bucket = provenance.setdefault("diagnostics", [])
    if not isinstance(bucket, list):
        provenance["diagnostics"] = []
        bucket = provenance["diagnostics"]
    stored: list[dict[str, Any]] = []
    for row in incoming:
        if not isinstance(row, dict):
            continue
        item = {
            "agent_id": str(row.get("agent_id") or agent_id),
            "path": str(row.get("path") or ""),
            "severity": str(row.get("severity") or "warn"),
            "message": str(row.get("message") or ""),
        }
        bucket.append(item)
        stored.append(item)
    return stored


def apply_owned_patch(
    canonical: dict[str, Any],
    agent_id: str,
    patch: dict[str, Any] | None,
    *,
    granted: list[str] | tuple[str, ...] | None = None,
    strict: bool = False,
) -> dict[str, Any]:
    """Apply a nested patch. Foreign paths are listed in rejected; critic diagnostics always land."""
    if not agent_id:
        raise OwnershipError("", ["(missing agent_id)"])
    src = deepcopy(patch) if isinstance(patch, dict) else {}
    dest = deepcopy(canonical)
    applied: list[str] = []
    rejected: list[str] = []
    diagnostics_in = src.pop("diagnostics", None)
    if isinstance(src.get("provenance"), dict) and "diagnostics" in src["provenance"]:
        extra = src["provenance"].pop("diagnostics")
        if diagnostics_in is None:
            diagnostics_in = extra
        elif isinstance(diagnostics_in, list) and isinstance(extra, list):
            diagnostics_in = list(diagnostics_in) + extra
        if not src["provenance"]:
            src.pop("provenance", None)
    stored_diags: list[dict[str, Any]] = []
    if diagnostics_in:
        if agent_id != CRITIC_ID and not path_allowed(agent_id, "provenance.diagnostics", granted):
            rejected.append("diagnostics")
        elif not isinstance(diagnostics_in, list):
            rejected.append("diagnostics")
        else:
            stored_diags = _append_diagnostics(dest, agent_id, diagnostics_in)
            applied.append("provenance.diagnostics")
    if src:
        _merge_owned(dest, src, "", agent_id, granted, applied, rejected)
    rejected = list(dict.fromkeys(rejected))
    if strict and rejected:
        raise OwnershipError(agent_id, rejected)
    try:
        clip: ClipObject = validate_clip(dest)
    except ClipSchemaError:
        clip = dest  # type: ignore[assignment]
    return {
        "clip": clip,
        "applied": applied,
        "rejected": rejected,
        "diagnostics": stored_diags
        or list((clip.get("provenance") or {}).get("diagnostics") or [])
        if isinstance(clip.get("provenance"), dict)
        else stored_diags,
    }


def overlays_from_comms(items: list[Any]) -> list[dict[str, Any]]:
    """Read host-side patches from choice hops without changing OPTION/SELECTED text."""
    overlays: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        patch = item.get("canonical_patch")
        if not isinstance(patch, dict) or not patch:
            continue
        agent_id = str(item.get("to") or item.get("from") or "")
        if item.get("from") == "human_operator":
            agent_id = str(item.get("to") or agent_id)
        granted = item.get("granted") if isinstance(item.get("granted"), list) else []
        overlays.append({"agent_id": agent_id, "patch": patch, "granted": granted})
    return overlays


def apply_choice_overlays(
    canonical: dict[str, Any],
    overlays: list[dict[str, Any]],
    *,
    strict: bool = False,
) -> dict[str, Any]:
    """Host applies patches after OPTION/SELECTED hops. Overlay bodies are not Chat text."""
    clip = deepcopy(canonical)
    applied: list[str] = []
    rejected: list[str] = []
    diagnostics: list[dict[str, Any]] = []
    for row in overlays:
        if not isinstance(row, dict):
            continue
        agent_id = str(row.get("agent_id") or "")
        patch = row.get("patch") if isinstance(row.get("patch"), dict) else {}
        granted = row.get("granted") if isinstance(row.get("granted"), list) else []
        result = apply_owned_patch(clip, agent_id, patch, granted=granted, strict=strict)
        clip = result["clip"]
        applied.extend(f"{agent_id}:{item}" for item in result["applied"])
        rejected.extend(f"{agent_id}:{item}" for item in result["rejected"])
        diagnostics.extend(result["diagnostics"] if isinstance(result["diagnostics"], list) else [])
    return {"clip": clip, "applied": applied, "rejected": rejected, "diagnostics": diagnostics}
