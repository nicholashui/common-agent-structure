"""list_eval_fixtures reads characterization JSON and skips junk."""

from __future__ import annotations

import json
from pathlib import Path

from casops.eval.fixtures import HONESTY, list_eval_fixtures


def test_list_eval_fixtures_skips_gitkeep_and_malformed(tmp_path: Path) -> None:
    folder = tmp_path / "agent"
    fixtures = folder / "evals" / "fixtures"
    fixtures.mkdir(parents=True)
    (fixtures / ".gitkeep").write_text("", encoding="utf-8")
    (fixtures / "broken.json").write_text("{not-json", encoding="utf-8")
    (fixtures / "other.json").write_text(json.dumps({"schema_version": "other", "id": "x"}), encoding="utf-8")
    (fixtures / "foreign.json").write_text(
        json.dumps(
            {
                "schema_version": "casops.testcase.v1",
                "id": "chat-tc9",
                "agent_id": "someone.else",
                "path": "chat",
                "honesty": "CHARACTERIZATION",
                "input": {"message": "nope"},
                "expect": {},
            }
        ),
        encoding="utf-8",
    )
    (fixtures / "chat-tc1.json").write_text(
        json.dumps(
            {
                "schema_version": "casops.testcase.v1",
                "id": "chat-tc1",
                "agent_id": "demo.agent",
                "path": "chat",
                "honesty": "CHARACTERIZATION",
                "input": {"message": "hello from fixture"},
                "expect": {"agent_id": "demo.agent", "memory_writes": []},
            }
        ),
        encoding="utf-8",
    )
    (fixtures / "provenance.json").write_text(
        json.dumps({"agent_id": "demo.agent", "note": "Characterization only. NOT_RUN."}),
        encoding="utf-8",
    )
    body = list_eval_fixtures(folder, "demo.agent")
    assert body["agent_id"] == "demo.agent"
    assert body["honesty"] == HONESTY
    assert "pass" not in body
    assert "NOT_RUN" in body["note"]
    assert [item["id"] for item in body["fixtures"]] == ["chat-tc1"]
    assert body["fixtures"][0]["filename"] == "chat-tc1.json"
    assert body["fixtures"][0]["input"]["message"] == "hello from fixture"
    assert body["provenance"]["agent_id"] == "demo.agent"


def test_list_eval_fixtures_empty_folder(tmp_path: Path) -> None:
    folder = tmp_path / "empty"
    body = list_eval_fixtures(folder, "empty.agent")
    assert body["fixtures"] == []
    assert body["honesty"] == HONESTY
    assert body["provenance"] is None
    assert "CHARACTERIZATION" in body["note"]
