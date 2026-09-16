"""Named programs under repo `program/<code>/`. Companion, not a live grant."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

CODE_RE = re.compile(r"^[a-z][a-z0-9]{0,47}$")


def programs_root_for(agents_root: Path, override: Path | None = None) -> Path:
    if override is not None:
        return override.resolve()
    return (Path(agents_root).resolve().parent / "program").resolve()


def normalize_code(value: str) -> str:
    original = value or ""
    if ".." in original or "/" in original.replace("\\", "/") or "\\" in original:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="invalid program code")
    raw = original.strip().lower().replace(" ", "")
    raw = re.sub(r"[^a-z0-9]+", "", raw)
    if not raw or not CODE_RE.match(raw):
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="invalid program code")
    return raw


def _safe_dir(root: Path, code: str) -> Path:
    folder = (root / code).resolve()
    try:
        folder.relative_to(root.resolve())
    except ValueError as exc:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="program path escapes root") from exc
    return folder


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def list_programs(root: Path) -> list[dict[str, Any]]:
    root.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    for child in sorted(root.iterdir()):
        payload_path = child / "program.json"
        if not child.is_dir() or not payload_path.is_file():
            continue
        try:
            payload = json.loads(payload_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(payload, dict):
            continue
        rows.append(
            {
                "id": child.name,
                "code": payload.get("code") or child.name,
                "name": payload.get("name") or child.name,
                "updated_at": payload.get("updated_at"),
            }
        )
    return rows


def read_program(root: Path, code: str) -> dict[str, Any]:
    code = normalize_code(code)
    folder = _safe_dir(root, code)
    path = folder / "program.json"
    if not path.is_file():
        raise CasopsError(ErrorCode.INH_PARENT_MISSING, detail="unknown program")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH)
    payload["id"] = code
    payload["code"] = str(payload.get("code") or code)
    payload["name"] = str(payload.get("name") or code)
    payload["folder"] = f"program/{code}"
    return payload


def write_program(root: Path, payload: dict[str, Any], *, dry_run: bool, create: bool) -> dict[str, Any]:
    code = normalize_code(str(payload.get("code") or payload.get("id") or payload.get("name") or ""))
    title = str(payload.get("name") or "").strip()
    if not title:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="program name required")
    folder = _safe_dir(root, code)
    existing = (folder / "program.json").is_file()
    if create and existing:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="program already exists")
    if not create and not existing:
        raise CasopsError(ErrorCode.INH_PARENT_MISSING, detail="unknown program")
    now = _now()
    record = {
        "schema_version": "casops.program.v1",
        "id": code,
        "code": code,
        "name": title,
        "honesty": "CHARACTERIZATION",
        "created_at": payload.get("created_at") or now,
        "updated_at": now,
        "folder": f"program/{code}",
        "production_activation": False,
        "allowed_tools": [],
    }
    if dry_run:
        record["saved"] = False
        record["dry_run"] = True
        return record
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "program.json").write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    record["saved"] = True
    record["dry_run"] = False
    return record
