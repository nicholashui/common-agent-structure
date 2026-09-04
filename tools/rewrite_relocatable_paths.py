"""Rewrite recorded historical drive-letter roots to repo-relative copies. Not junctions."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from reloc import REPO, repo_posix, rewrite_historical_text

SKIP_DIR_NAMES = {
    ".git",
    ".venv",
    "node_modules",
    "__pycache__",
    "vendor",
    "book",
    "issues",
    "dist",
    ".pytest_cache",
}
TEXT_SUFFIXES = {".md", ".txt", ".ps1", ".bat", ".py", ".ts", ".tsx", ".json"}
JSON_PATH_KEYS = {
    "folder",
    "swarm_ops_cases",
    "file",
    "source_folder",
    "imported_from",
}


def _skip_path(path: Path) -> bool:
    rel_parts = path.relative_to(REPO).parts
    return any(part in SKIP_DIR_NAMES for part in rel_parts)


def looks_project_path(value: str) -> bool:
    lowered = value.replace("\\", "/").lower()
    return "c:/project/" in lowered or lowered.startswith("c:\\project\\")


def rewrite_json_value(value: object) -> tuple[object, bool]:
    changed = False
    if isinstance(value, dict):
        out: dict = {}
        for key, item in value.items():
            if key in JSON_PATH_KEYS and isinstance(item, str) and looks_project_path(item):
                nxt = repo_posix(item)
                out[key] = nxt
                changed = changed or nxt != item
            else:
                nxt, inner = rewrite_json_value(item)
                out[key] = nxt
                changed = changed or inner
        return out, changed
    if isinstance(value, list):
        rows = []
        for item in value:
            nxt, inner = rewrite_json_value(item)
            rows.append(nxt)
            changed = changed or inner
        return rows, changed
    if isinstance(value, str) and looks_project_path(value):
        nxt = rewrite_historical_text(value)
        if nxt == value:
            nxt = repo_posix(value)
        return nxt, nxt != value
    return value, False


def rewrite_json_file(path: Path) -> bool:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return False
    nxt, changed = rewrite_json_value(payload)
    if not changed:
        return False
    path.write_text(json.dumps(nxt, indent=2) + "\n", encoding="utf-8")
    return True


def rewrite_text_file(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return False
    nxt = rewrite_historical_text(text)
    if nxt == text:
        return False
    path.write_text(nxt, encoding="utf-8")
    return True


def main() -> None:
    json_n = 0
    text_n = 0
    for path in REPO.rglob("*"):
        if not path.is_file():
            continue
        if _skip_path(path):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = path.relative_to(REPO).as_posix()
        if path.suffix.lower() == ".json":
            if rewrite_json_file(path):
                json_n += 1
            continue
        if path.suffix.lower() == ".py" and rel.startswith("tools/"):
            # Importers are edited by hand; skip sweeping Python that may mention historical siblings.
            continue
        if rewrite_text_file(path):
            text_n += 1
    print(f"rewrote json={json_n} text={text_n}")


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    main()
