"""Host-owned LLM routing: DEFAULT_LLM, per-agent override, fail-closed missing keys."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.runtime.llm import LlmRouter, LlmSettings, env_default_llm, list_providers, load_dotenv


def test_env_default_llm(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DEFAULT_LLM", raising=False)
    assert env_default_llm() == "local_deterministic"
    monkeypatch.setenv("DEFAULT_LLM", "openai")
    assert env_default_llm() == "openai"


def test_load_dotenv_does_not_override(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    import os

    monkeypatch.setenv("DEFAULT_LLM", "xai")
    env_file = tmp_path / ".env"
    env_file.write_text("DEFAULT_LLM=openai\nOPENAI_API_KEY=sk-test\n", encoding="utf-8")
    load_dotenv(env_file)
    assert os.environ["DEFAULT_LLM"] == "xai"
    assert os.environ["OPENAI_API_KEY"] == "sk-test"


def test_list_providers_hides_secrets(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "sk-secret-value")
    rows = {item["id"]: item for item in list_providers()}
    blob = json.dumps(rows)
    assert "sk-secret-value" not in blob
    assert rows["openai"]["configured"] is True
    assert rows["local_deterministic"]["configured"] is True


def test_agent_override_beats_default(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DEFAULT_LLM", "local_deterministic")
    settings = LlmSettings(path=tmp_path / "llm.json", default_llm="openai", agents={"video.director": "xai"})
    router = LlmRouter(settings=settings)
    monkeypatch.setenv("XAI_API_KEY", "xai-key")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-key")
    assert router.resolve("video.director") == "xai"
    assert router.resolve("video.editor") == "openai"


def test_missing_key_fails_closed(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DEFAULT_LLM", "openai")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    router = LlmRouter(settings=LlmSettings(path=tmp_path / "llm.json"))
    with pytest.raises(CasopsError) as raised:
        router.resolve("video.director")
    assert raised.value.code == ErrorCode.PERF_ROUTE_UNAVAILABLE


def test_openai_compat_uses_host_http(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DEFAULT_LLM", "openai")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    monkeypatch.setenv("OPENAI_MODEL", "gpt-test")
    captured: dict[str, object] = {}

    def post(url: str, headers: dict[str, str], payload: dict[str, object]) -> dict[str, object]:
        captured["url"] = url
        captured["headers"] = headers
        captured["payload"] = payload
        return {"choices": [{"message": {"content": "hello from host llm"}}]}

    router = LlmRouter(settings=LlmSettings(path=tmp_path / "llm.json"), post=post)
    result = router.complete(agent_id="video.director", prompt="ping", node_id="model_1", max_tokens=32)
    assert result["provider"] == "openai"
    assert result["text"] == "hello from host llm"
    assert captured["url"] == "https://api.openai.com/v1/chat/completions"
    assert captured["headers"]["Authorization"] == "Bearer sk-test"
    assert captured["payload"]["max_tokens"] == 32
