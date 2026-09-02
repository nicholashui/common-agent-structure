"""Operator debug log files. Not part of the public /api/v3 contract."""

from __future__ import annotations

import json
import os
import re
import threading
from pathlib import Path
from typing import Any

_SESSION = re.compile(r"^[A-Za-z0-9._-]{1,80}$")
_CHANNELS = {"api", "ui"}
_LOCK = threading.Lock()
_MAX_ENTRIES = 200
_MAX_FIELD = 8000


def log_root() -> Path:
    raw = os.environ.get("CASOPS_LOG_ROOT", str(Path.cwd() / "logs" / "debug"))
    path = Path(raw)
    path.mkdir(parents=True, exist_ok=True)
    return path


def _clip(value: Any) -> str:
    text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, default=str)
    if len(text) > _MAX_FIELD:
        return f"{text[:_MAX_FIELD]}…(+{len(text) - _MAX_FIELD}b)"
    return text


def write_debug_logs(payload: dict[str, Any]) -> dict[str, str]:
    session = str(payload.get("session") or "")
    if not _SESSION.fullmatch(session):
        raise ValueError("invalid session id")
    raw_entries = payload.get("entries")
    if not isinstance(raw_entries, list) or not raw_entries:
        raise ValueError("entries required")
    if len(raw_entries) > _MAX_ENTRIES:
        raise ValueError("too many entries")

    files = {
        "api": log_root() / f"{session}-api.log",
        "ui": log_root() / f"{session}-ui.log",
    }
    buckets: dict[str, list[str]] = {"api": [], "ui": []}
    for item in raw_entries:
        if not isinstance(item, dict):
            continue
        channel = str(item.get("channel") or "")
        if channel not in _CHANNELS:
            raise ValueError("invalid channel")
        record = {
            "ts": _clip(item.get("ts") or ""),
            "level": _clip(item.get("level") or "info"),
            "message": _clip(item.get("message") or ""),
            "detail": _clip(item.get("detail") or ""),
        }
        buckets[channel].append(json.dumps(record, ensure_ascii=False))

    with _LOCK:
        for channel, lines in buckets.items():
            if not lines:
                continue
            path = files[channel]
            with path.open("a", encoding="utf-8") as handle:
                handle.write("\n".join(lines) + "\n")
                handle.flush()

    return {channel: str(path) for channel, path in files.items() if path.exists()}
