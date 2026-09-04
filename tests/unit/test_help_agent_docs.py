"""Per-agent Help docs are copied from agents/<id>/docs and merged from SPEC sources."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))

from generate_help_agent_docs import build_spec, build_userguide, write_agent_docs  # noqa: E402


def test_build_userguide_copies_docs_markdown(tmp_path: Path) -> None:
    folder = tmp_path / "demo.agent"
    docs = folder / "docs"
    docs.mkdir(parents=True)
    (docs / "user_guide.md").write_text("# Operator guide\n\nTalk to this agent./n", encoding="utf-8")
    (docs / "notes.md").write_text("# Extra\n\nMore./n", encoding="utf-8")
    text = build_userguide(folder) or ""
    assert "Copied from `demo.agent/docs`" in text
    assert "Talk to this agent." in text
    assert "Extra" in text


def test_build_spec_merges_spec_json_prompts_rubrics_sources(tmp_path: Path) -> None:
    folder = tmp_path / "demo.agent"
    (folder / "prompts").mkdir(parents=True)
    (folder / "rubrics").mkdir()
    (folder / "sources" / "excerpts").mkdir(parents=True)
    (folder / "agent_spec.json").write_text(
        json.dumps({"agent_id": "demo.agent", "role": "Demo", "production_activation_requested": False}),
        encoding="utf-8",
    )
    (folder / "SPEC.md").write_text("# Demo SPEC\n\nOwns the demo role./n", encoding="utf-8")
    (folder / "prompts" / "primary.md").write_text("You are demo./n", encoding="utf-8")
    (folder / "rubrics" / "primary.md").write_text("Score honesty./n", encoding="utf-8")
    (folder / "sources" / "MAPPING.md").write_text("Mapped from design notes./n", encoding="utf-8")
    (folder / "sources" / "excerpts" / "long.md").write_text("excerpt body\n", encoding="utf-8")
    text = build_spec(folder)
    assert "demo.agent — Spec" in text
    assert "Host contract" in text
    assert '"role": "Demo"' in text
    assert "Owns the demo role." in text
    assert "You are demo." in text
    assert "Score honesty." in text
    assert "Mapped from design notes." in text
    assert "sources/excerpts/long.md" in text
    assert "excerpt body" in text


def test_write_agent_docs_uses_agent_id_folder(tmp_path: Path) -> None:
    folder = tmp_path / "_disk_name"
    docs = folder / "docs"
    docs.mkdir(parents=True)
    (folder / "agent_spec.json").write_text(json.dumps({"agent_id": "pack.real-id"}), encoding="utf-8")
    (folder / "SPEC.md").write_text("# Real\n", encoding="utf-8")
    (docs / "user_guide.md").write_text("# Guide\n", encoding="utf-8")
    out = tmp_path / "docs"
    written = write_agent_docs(folder, out)
    assert (out / "pack.real-id" / "spec.md").is_file()
    assert (out / "pack.real-id" / "userguide.md").is_file()
    assert "Guide" in written["userguide"].read_text(encoding="utf-8")
