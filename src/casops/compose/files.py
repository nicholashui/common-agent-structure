"""Confined read/write of an agent's on-disk configuration folders."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from casops.artifacts.atomic import atomic_write
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

CONFIG_FOLDERS: tuple[str, ...] = (
    "corrigibility",
    "docs",
    "evals",
    "identity",
    "improvement",
    "inheritance",
    "memory",
    "observability",
    "plugins",
    "prompts",
    "protocols",
    "rubrics",
    "runtime",
    "safety",
    "skills",
    "sources",
)

TEXT_SUFFIXES = {".md", ".json", ".txt", ".svg", ".yml", ".yaml", ".csv", ".html", ".xml", ".hk"}
SKIP_DIR_NAMES = {".git", "__pycache__", "node_modules", ".venv"}
MAX_BYTES = 2 * 1024 * 1024
MAX_FILES = 800
HOST_OWNED_EXACT = frozenset(
    {
        "corrigibility/attestation.json",
        "corrigibility/invariants.json",
        "plugins/lock.json",
    }
)
HOST_OWNED_PREFIXES = ("corrigibility/", "safety/incidents/")


def normalize_rel(path: str) -> str:
    text = str(path or "").replace("\\", "/").strip()
    if not text or text.startswith("/") or ":" in text or "\x00" in text:
        raise CasopsError(ErrorCode.SAF_EXFILTRATION)
    parts: list[str] = []
    for segment in text.split("/"):
        if segment in {"", "."}:
            continue
        if segment == "..":
            raise CasopsError(ErrorCode.SAF_EXFILTRATION)
        if segment.startswith(".") or any(ch in segment for ch in '<>"|?*'):
            raise CasopsError(ErrorCode.INH_SURFACE_UNKNOWN)
        parts.append(segment)
    if not parts:
        raise CasopsError(ErrorCode.INH_SURFACE_UNKNOWN)
    if parts[0] not in CONFIG_FOLDERS:
        raise CasopsError(ErrorCode.INH_SURFACE_UNKNOWN)
    return "/".join(parts)


def confined_path(folder: Path, rel: str) -> Path:
    normalized = normalize_rel(rel)
    root = folder.resolve()
    candidate = (folder / Path(*normalized.split("/"))).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise CasopsError(ErrorCode.SAF_EXFILTRATION) from exc
    return candidate


def host_owned(rel: str) -> bool:
    normalized = normalize_rel(rel)
    if normalized in HOST_OWNED_EXACT:
        return True
    return any(normalized == prefix[:-1] or normalized.startswith(prefix) for prefix in HOST_OWNED_PREFIXES)


def _suffix_kind(name: str) -> str:
    lower = name.lower()
    if lower.endswith(".tmp"):
        return "skip"
    suffix = Path(lower).suffix
    if suffix in TEXT_SUFFIXES:
        return "text"
    return "binary"


def _file_kind(path: Path, size: int) -> str:
    if size > MAX_BYTES:
        return "too_large"
    kind = _suffix_kind(path.name)
    if kind != "text":
        return "binary" if kind != "skip" else "binary"
    try:
        sample = path.read_bytes()[:4096]
    except OSError:
        return "binary"
    if b"\x00" in sample:
        return "binary"
    try:
        sample.decode("utf-8")
    except UnicodeDecodeError:
        return "binary"
    return "text"


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def list_config_files(folder: Path, agent_id: str) -> dict[str, Any]:
    folders: list[dict[str, Any]] = []
    total = 0
    for name in CONFIG_FOLDERS:
        directory = folder / name
        present = directory.is_dir()
        files: list[dict[str, Any]] = []
        if present:
            for path in sorted(directory.rglob("*")):
                if total >= MAX_FILES:
                    break
                if not path.is_file():
                    continue
                if any(part in SKIP_DIR_NAMES or part.startswith(".") for part in path.relative_to(directory).parts[:-1]):
                    continue
                if path.name.startswith(".") or path.suffix.lower() == ".tmp":
                    continue
                try:
                    rel = path.resolve().relative_to(folder.resolve()).as_posix()
                except ValueError:
                    continue
                try:
                    normalize_rel(rel)
                except CasopsError:
                    continue
                size = path.stat().st_size
                kind = _file_kind(path, size)
                files.append(
                    {
                        "path": rel,
                        "bytes": size,
                        "kind": kind,
                        "writable": kind == "text" and not host_owned(rel),
                    }
                )
                total += 1
        folders.append({"name": name, "present": present, "files": files})
    return {"agent_id": agent_id, "folders": folders, "max_bytes": MAX_BYTES}


def read_config_file(folder: Path, agent_id: str, rel: str) -> dict[str, Any]:
    path = confined_path(folder, rel)
    normalized = normalize_rel(rel)
    if not path.is_file():
        raise CasopsError(ErrorCode.INH_PARENT_MISSING)
    size = path.stat().st_size
    kind = _file_kind(path, size)
    owned = host_owned(normalized)
    body: dict[str, Any] = {
        "agent_id": agent_id,
        "path": normalized,
        "bytes": size,
        "kind": kind,
        "writable": kind == "text" and not owned,
        "host_owned": owned,
        "encoding": "utf-8" if kind == "text" else None,
        "content": None,
        "sha256": None,
    }
    if kind != "text":
        return body
    text = path.read_text(encoding="utf-8")
    body["content"] = text
    body["sha256"] = _sha256_text(text)
    return body


def write_config_file(
    folder: Path,
    agent_id: str,
    rel: str,
    content: str,
    *,
    dry_run: bool,
) -> dict[str, Any]:
    if not isinstance(content, str):
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH)
    encoded = content.encode("utf-8")
    if len(encoded) > MAX_BYTES:
        raise CasopsError(ErrorCode.CTX_BUDGET)
    normalized = normalize_rel(rel)
    if host_owned(normalized):
        if normalized.startswith("corrigibility/"):
            raise CasopsError(ErrorCode.IMP_CORRIGIBILITY)
        raise CasopsError(ErrorCode.PLG_PERMISSION)
    if _suffix_kind(normalized.rsplit("/", 1)[-1]) != "text":
        raise CasopsError(ErrorCode.INH_SURFACE_UNKNOWN)
    if normalized.endswith(".json"):
        try:
            json.loads(content)
        except json.JSONDecodeError as exc:
            raise CasopsError(ErrorCode.CMP_JSON_SCHEMA_PROFILE) from exc
    path = confined_path(folder, rel)
    if path.exists() and not path.is_file():
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH)
    if not path.exists() and not path.parent.is_dir():
        raise CasopsError(ErrorCode.INH_PARENT_MISSING)
    try:
        path.parent.resolve().relative_to(folder.resolve())
    except ValueError as exc:
        raise CasopsError(ErrorCode.SAF_EXFILTRATION) from exc
    digest = _sha256_text(content)
    if not dry_run:
        atomic_write(path, content)
    size = path.stat().st_size if path.is_file() and not dry_run else len(encoded)
    return {
        "agent_id": agent_id,
        "path": normalized,
        "saved": not dry_run,
        "dry_run": dry_run,
        "bytes": size,
        "sha256": digest,
        "kind": "text",
        "writable": True,
    }
