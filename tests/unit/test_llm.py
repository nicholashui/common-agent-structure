"""Host-owned LLM routing: DEFAULT_LLM, per-agent override, fail-closed missing keys."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.runtime.llm import (
    DEFAULT_COMPLETION_TOKENS,
    IMPORT_DEFAULT_INPUT_TOKENS,
    IMPORT_DEFAULT_OUTPUT_TOKENS,
    LlmRouter,
    LlmSettings,
    canonicalize_provider,
    env_default_llm,
    list_providers,
    load_dotenv,
    resolve_completion_tokens,
    resolve_import_token_budget,
)


def test_env_default_llm(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DEFAULT_LLM", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("XAI_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    assert env_default_llm() == "local_deterministic"
    monkeypatch.setenv("DEFAULT_LLM", "openai")
    assert env_default_llm() == "openai"


def test_env_default_llm_uses_configured_host_provider(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DEFAULT_LLM", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.setenv("XAI_API_KEY", "xai-key")
    assert env_default_llm() == "xai"


def test_default_llm_case_insensitive(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv("DEFAULT_LLM", "XAI")
    monkeypatch.setenv("XAI_API_KEY", "xai-key")
    assert canonicalize_provider("XAI") == "xai"
    assert env_default_llm() == "xai"
    router = LlmRouter(settings=LlmSettings(path=tmp_path / "llm.json"))
    assert router.resolve("video.director") == "xai"


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
    assert captured["payload"]["messages"] == [{"role": "user", "content": "ping"}]


def test_complete_sends_system_history_and_human_message(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("DEFAULT_LLM", "openai")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    captured: dict[str, object] = {}

    def post(url: str, headers: dict[str, str], payload: dict[str, object]) -> dict[str, object]:
        del url, headers
        captured["payload"] = payload
        return {"choices": [{"message": {"content": "ack"}}]}

    router = LlmRouter(settings=LlmSettings(path=tmp_path / "llm.json"), post=post)
    result = router.complete(
        agent_id="video.director",
        prompt="hello from operator",
        node_id="chat",
        system="You are director.",
        history=[{"role": "user", "content": "hi"}, {"role": "assistant", "content": "hey"}],
    )
    assert result["text"] == "ack"
    assert captured["payload"]["messages"] == [
        {"role": "system", "content": "You are director."},
        {"role": "user", "content": "hi"},
        {"role": "assistant", "content": "hey"},
        {"role": "user", "content": "hello from operator"},
    ]


def test_stub_output_budget_uses_host_floor() -> None:
    tokens, source = resolve_completion_tokens(1)
    assert tokens == DEFAULT_COMPLETION_TOKENS
    assert source == "host_floor"
    tokens, source = resolve_completion_tokens(1024)
    assert tokens == 1024
    assert source == "spec"
    tokens, source = resolve_completion_tokens(None)
    assert tokens == DEFAULT_COMPLETION_TOKENS
    assert source == "host_default"


def test_import_token_budget_floors_stub_values() -> None:
    assert resolve_import_token_budget(1, default=IMPORT_DEFAULT_OUTPUT_TOKENS) == IMPORT_DEFAULT_OUTPUT_TOKENS
    assert resolve_import_token_budget(0, default=IMPORT_DEFAULT_INPUT_TOKENS) == IMPORT_DEFAULT_INPUT_TOKENS
    assert resolve_import_token_budget(1024, default=IMPORT_DEFAULT_OUTPUT_TOKENS) == 1024


def test_openai_compat_omits_reasoning_and_flags_length(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("DEFAULT_LLM", "openai")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")

    def post(url: str, headers: dict[str, str], payload: dict[str, object]) -> dict[str, object]:
        del url, headers, payload
        return {
            "choices": [
                {
                    "finish_reason": "length",
                    "message": {
                        "content": "I",
                        "reasoning_content": "secret chain of thought",
                    },
                }
            ],
            "usage": {
                "prompt_tokens": 40,
                "completion_tokens": 1,
                "total_tokens": 41,
                "completion_tokens_details": {"reasoning_tokens": 200},
            },
        }

    router = LlmRouter(settings=LlmSettings(path=tmp_path / "llm.json"), post=post)
    result = router.complete(agent_id="video.director", prompt="what you are thinking?", node_id="chat")
    assert result["text"] == "I"
    assert result["finish_reason"] == "length"
    assert result["truncated"] is True
    assert result["content_chars"] == 1
    assert result["usage"]["reasoning_tokens"] == 200
    blob = json.dumps(result)
    assert "secret chain of thought" not in blob
    assert "reasoning_content" not in blob
