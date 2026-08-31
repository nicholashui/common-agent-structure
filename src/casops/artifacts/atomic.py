"""Atomic lock writes via temp file + replace (implementation_plan.md §17.2)."""

from __future__ import annotations

import os
from pathlib import Path


def atomic_write(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(data, encoding="utf-8")
    os.replace(tmp, path)
