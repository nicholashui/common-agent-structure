"""POST /debug/logs is an operator sink, not public /api/v3."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from casops.api.apps import create_control_plane

REPO = Path(__file__).resolve().parents[2]


def test_debug_logs_not_in_openapi() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    spec = client.get("/openapi.json").json()
    assert "/debug/logs" not in spec["paths"]
    assert "/health" not in spec["paths"]
    assert all(path.startswith("/api/v3") for path in spec["paths"])


def test_debug_logs_writes_files(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_LOG_ROOT", str(tmp_path))
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    session = "2026-09-02-12-34-56-000-ui1"
    response = client.post(
        "/debug/logs",
        json={
            "session": session,
            "entries": [
                {
                    "channel": "api",
                    "ts": "2026-09-02T12:34:56.000Z",
                    "level": "info",
                    "message": "GET /api/v3/agents 200 8ms",
                    "detail": "{}",
                },
                {
                    "channel": "ui",
                    "ts": "2026-09-02T12:34:56.100Z",
                    "level": "info",
                    "message": "run common.health",
                    "detail": "",
                },
            ],
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["ok"] is True
    api_path = tmp_path / f"{session}-api.log"
    ui_path = tmp_path / f"{session}-ui.log"
    assert body["files"]["api"] == str(api_path)
    assert body["files"]["ui"] == str(ui_path)
    api = json.loads(api_path.read_text(encoding="utf-8").splitlines()[0])
    ui = json.loads(ui_path.read_text(encoding="utf-8").splitlines()[0])
    assert api["ts"] == "2026-09-02T12:34:56.000Z"
    assert "GET /api/v3/agents" in api["message"]
    assert ui["message"] == "run common.health"


def test_debug_logs_invalid_session_is_400(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_LOG_ROOT", str(tmp_path))
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    response = client.post(
        "/debug/logs",
        json={"session": "bad session", "entries": [{"channel": "ui", "message": "x"}]},
    )
    assert response.status_code == 400


def test_debug_logs_does_not_require_mutation_headers(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_LOG_ROOT", str(tmp_path))
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    response = client.post(
        "/debug/logs",
        json={
            "session": "no-mutation-needed",
            "entries": [{"channel": "ui", "ts": "t", "level": "debug", "message": "navigate /settings", "detail": ""}],
        },
    )
    assert response.status_code == 200
    assert response.json()["ok"] is True


def test_debug_chat_writes_and_lists_files(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CASOPS_CHAT_ROOT", str(tmp_path))
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    session = "2026-09-02-13-00-00-000-c1"
    response = client.post(
        "/debug/chat",
        json={
            "agent_id": "video.director",
            "session": session,
            "entries": [
                {"role": "user", "ts": "2026-09-02T13:00:00.000Z", "content": "hello", "provider": ""},
                {"role": "assistant", "ts": "2026-09-02T13:00:01.000Z", "content": "hi", "provider": "xai"},
            ],
        },
    )
    assert response.status_code == 200
    path = tmp_path / "video.director" / f"{session}.jsonl"
    assert response.json()["files"]["transcript"] == str(path)
    listed = client.get("/debug/chat", params={"agent_id": "video.director"})
    assert listed.status_code == 200
    files = listed.json()["files"]
    assert files[0]["name"] == f"{session}.jsonl"
    spec = client.get("/openapi.json").json()
    assert "/debug/chat" not in spec["paths"]
    loaded = client.get("/debug/chat", params={"agent_id": "video.director", "name": f"{session}.jsonl"})
    assert loaded.status_code == 200
    turns = loaded.json()["turns"]
    assert turns[0]["content"] == "hello"
    assert turns[1]["provider"] == "xai"
    escaped = client.get("/debug/chat", params={"agent_id": "video.director", "name": "../secret.jsonl"})
    assert escaped.status_code == 400
