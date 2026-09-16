"""Operator debug log files written by POST /debug/logs."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from casops.debuglog import list_acp_logs, list_chat_files, read_acp_logs, read_chat_file, write_chat_turns, write_debug_logs


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
    assert files["api"].replace("\\", "/").endswith(api_path.name)
    assert files["ui"].replace("\\", "/").endswith(ui_path.name)
    assert not Path(files["api"]).is_absolute()
    assert not Path(files["ui"]).is_absolute()
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
    assert files["transcript"].replace("\\", "/").endswith(f"common.health/{session}.jsonl")
    assert not Path(files["transcript"]).is_absolute()
    lines = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
    assert lines[0]["ts"] == "2026-09-02T12:00:00.000Z"
    assert lines[0]["role"] == "user"
    assert lines[1]["content"] == "pong"
    listed = list_chat_files("common.health")
    assert listed[0]["name"] == f"{session}.jsonl"
    assert listed[0]["ts"]
    assert not Path(listed[0]["path"]).is_absolute()
    assert listed[0]["path"].replace("\\", "/").endswith(f"common.health/{session}.jsonl")
    loaded = read_chat_file("common.health", f"{session}.jsonl")
    assert loaded["session"] == session
    assert loaded["turns"][0]["content"] == "ping"
    assert loaded["turns"][1]["role"] == "assistant"


def test_read_chat_file_rejects_path_escape(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_CHAT_ROOT", str(tmp_path))
    with pytest.raises(ValueError):
        read_chat_file("common.health", "../secret.jsonl")
    with pytest.raises(ValueError):
        read_chat_file("common.health", "missing.jsonl")


def test_acp_logs_list_and_reject_escape(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_ACP_LOG_ROOT", str(tmp_path))
    agent_id = "specials.intent-analysis-agent"
    host = tmp_path / f"{agent_id}.2026-09-06-12-00-00.host.log"
    err = tmp_path / f"{agent_id}.2026-09-06-12-00-00.stderr.log"
    host.write_text('{"event":"spawn","agent_id":"specials.intent-analysis-agent"}\n', encoding="utf-8")
    err.write_text("2026-09-06T12:00:00Z grok stderr line\n", encoding="utf-8")
    listed = list_acp_logs(agent_id)
    names = {row["name"] for row in listed}
    assert host.name in names
    assert err.name in names
    combined = read_acp_logs(agent_id)
    assert "spawn" in combined["text"]
    assert "stderr line" in combined["text"]
    one = read_acp_logs(agent_id, host.name)
    assert "spawn" in one["text"]
    assert "stderr line" not in one["text"]
    with pytest.raises(ValueError):
        read_acp_logs(agent_id, "../secret.log")
    with pytest.raises(ValueError):
        read_acp_logs("../escape")


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
