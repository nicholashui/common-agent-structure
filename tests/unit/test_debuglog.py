"""Operator debug log files written by POST /debug/logs."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from casops.debuglog import list_chat_files, write_chat_turns, write_debug_logs


def test_write_debug_logs_appends_jsonl(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_LOG_ROOT", str(tmp_path))
    session = "2026-09-02-12-00-00-000-abc123"
    files = write_debug_logs(
        {
            "session": session,
            "entries": [
                {
                    "channel": "api",
                    "ts": "2026-09-02T12:00:00.001Z",
                    "level": "info",
                    "message": "GET /api/v3/agents 200 12ms",
                    "detail": '{"ok":true}',
                },
                {
                    "channel": "ui",
                    "ts": "2026-09-02T12:00:01.002Z",
                    "level": "info",
                    "message": "chat send video.director",
                    "detail": "hello",
                },
            ],
        }
    )
    api_path = tmp_path / f"{session}-api.log"
    ui_path = tmp_path / f"{session}-ui.log"
    assert files["api"] == str(api_path)
    assert files["ui"] == str(ui_path)
    api = json.loads(api_path.read_text(encoding="utf-8").splitlines()[0])
    ui = json.loads(ui_path.read_text(encoding="utf-8").splitlines()[0])
    assert api["ts"] == "2026-09-02T12:00:00.001Z"
    assert api["message"] == "GET /api/v3/agents 200 12ms"
    assert ui["message"] == "chat send video.director"
    write_debug_logs(
        {
            "session": session,
            "entries": [
                {
                    "channel": "api",
                    "ts": "2026-09-02T12:00:02.000Z",
                    "level": "error",
                    "message": "POST /api/v3/agents/x/runtime/chat 500",
                    "detail": "",
                }
            ],
        }
    )
    assert len(api_path.read_text(encoding="utf-8").splitlines()) == 2


def test_write_debug_logs_rejects_bad_session(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_LOG_ROOT", str(tmp_path))
    with pytest.raises(ValueError, match="invalid session"):
        write_debug_logs({"session": "../escape", "entries": [{"channel": "ui", "message": "x"}]})


def test_write_debug_logs_skips_missing_channel_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_LOG_ROOT", str(tmp_path))
    files = write_debug_logs(
        {
            "session": "only-ui-session",
            "entries": [{"channel": "ui", "ts": "t", "level": "info", "message": "navigate /", "detail": ""}],
        }
    )
    assert "ui" in files
    assert "api" not in files
    assert (tmp_path / "only-ui-session-ui.log").is_file()
    assert not (tmp_path / "only-ui-session-api.log").exists()


def test_write_chat_turns_saves_timestamped_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_CHAT_ROOT", str(tmp_path))
    session = "2026-09-02-12-00-00-000-chat1"
    files = write_chat_turns(
        {
            "agent_id": "common.health",
            "session": session,
            "entries": [
                {
                    "role": "user",
                    "ts": "2026-09-02T12:00:00.000Z",
                    "content": "ping",
                    "provider": "",
                },
                {
                    "role": "assistant",
                    "ts": "2026-09-02T12:00:01.000Z",
                    "content": "pong",
                    "provider": "xai",
                },
            ],
        }
    )
    path = tmp_path / "common.health" / f"{session}.jsonl"
    assert files["transcript"] == str(path)
    lines = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
    assert lines[0]["ts"] == "2026-09-02T12:00:00.000Z"
    assert lines[0]["role"] == "user"
    assert lines[1]["content"] == "pong"
    listed = list_chat_files("common.health")
    assert listed[0]["name"] == f"{session}.jsonl"
    assert listed[0]["ts"]


def test_write_chat_turns_rejects_bad_agent(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_CHAT_ROOT", str(tmp_path))
    with pytest.raises(ValueError, match="invalid agent"):
        write_chat_turns(
            {
                "agent_id": "../escape",
                "session": "ok-session",
                "entries": [{"role": "user", "content": "x"}],
            }
        )
