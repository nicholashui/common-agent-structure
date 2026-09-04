"""Read casops.testcase.v1 files from an agent folder's evals/fixtures/."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "casops.testcase.v1"
HONESTY = "CHARACTERIZATION"
HONESTY_NOTE = (
    "Fixtures are CHARACTERIZATION / policy checks. Not an eval pass. "
    "casops-eval remains NOT_RUN while instruments are unqualified."
)


def list_eval_fixtures(folder: Path, agent_id: str) -> dict[str, Any]:
    directory = folder / "evals" / "fixtures"
    cases: list[dict[str, Any]] = []
    provenance: dict[str, Any] | None = None
    if directory.is_dir():
        for path in sorted(directory.iterdir(), key=lambda item: item.name):
            if not path.is_file() or path.suffix.lower() != ".json":
                continue
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError, json.JSONDecodeError):
                continue
            if not isinstance(payload, dict):
                continue
            if path.name == "provenance.json":
                provenance = payload
                continue
            if payload.get("schema_version") != SCHEMA_VERSION:
                continue
            listed_id = payload.get("agent_id")
            if listed_id not in {None, "", agent_id}:
                continue
            case = dict(payload)
            case["filename"] = path.name
            cases.append(case)
    note = HONESTY_NOTE
    if isinstance(provenance, dict):
        proven_note = provenance.get("note")
        if isinstance(proven_note, str) and proven_note.strip():
            note = proven_note.strip()
    return {
        "agent_id": agent_id,
        "honesty": HONESTY,
        "note": note,
        "fixtures": cases,
        "provenance": provenance,
    }
