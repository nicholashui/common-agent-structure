"""Host-owned LLM routing. Credentials stay in process env / .env, never in agent folders."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from casops.contracts.canonical import sha256_json
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.runtime.adapter import DeterministicAdapter

PostFn = Callable[[str, dict[str, str], dict[str, Any]], dict[str, Any]]

PROVIDER_CATALOG: dict[str, dict[str, str]] = {
    "local_deterministic": {
        "id": "local_deterministic",
        "label": "Local deterministic (offline)",
        "kind": "local",
    },
    "openai": {
        "id": "openai",
        "label": "OpenAI",
        "kind": "openai_compat",
        "key_env": "OPENAI_API_KEY",
        "base_env": "OPENAI_BASE_URL",
        "model_env": "OPENAI_MODEL",
        "default_base": "https://api.openai.com/v1",
        "default_model": "gpt-4o-mini",
    },
    "xai": {
        "id": "xai",
        "label": "xAI Grok",
        "kind": "openai_compat",
        "key_env": "XAI_API_KEY",
        "base_env": "XAI_BASE_URL",
        "model_env": "XAI_MODEL",
        "default_base": "https://api.x.ai/v1",
        "default_model": "grok-4",
    },
    "anthropic": {
        "id": "anthropic",
        "label": "Anthropic",
        "kind": "anthropic",
        "key_env": "ANTHROPIC_API_KEY",
        "base_env": "ANTHROPIC_BASE_URL",
        "model_env": "ANTHROPIC_MODEL",
        "default_base": "https://api.anthropic.com",
        "default_model": "claude-sonnet-4-5",
    },
}


def load_dotenv(path: Path) -> None:
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key and key not in os.environ:
            os.environ[key] = value


_PROVIDER_ALIASES = {
    "grok": "xai",
    "x-ai": "xai",
}


def canonicalize_provider(value: str | None) -> str:
    text = (value or "").strip()
    if not text:
        return ""
    lowered = text.lower()
    if lowered in _PROVIDER_ALIASES:
        return _PROVIDER_ALIASES[lowered]
    if lowered in PROVIDER_CATALOG:
        return lowered
    for key in PROVIDER_CATALOG:
        if key.lower() == lowered:
            return key
    return text


MIN_USABLE_COMPLETION_TOKENS = 16
DEFAULT_COMPLETION_TOKENS = 512
IMPORT_DEFAULT_OUTPUT_TOKENS = 1024
IMPORT_DEFAULT_INPUT_TOKENS = 2048
_LENGTH_FINISH_REASONS = {"length", "max_tokens", "max_output_tokens"}


def parse_token_count(value: Any) -> int | None:
    if value is None or value == "":
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def resolve_completion_tokens(
    declared: Any,
    *,
    default: int = DEFAULT_COMPLETION_TOKENS,
    floor: int = MIN_USABLE_COMPLETION_TOKENS,
) -> tuple[int, str]:
    raw = parse_token_count(declared)
    if raw is None:
        return default, "host_default"
    if raw < floor:
        return default, "host_floor"
    return raw, "spec"


def resolve_import_token_budget(value: Any, *, default: int) -> int:
    raw = parse_token_count(value)
    if raw is None or raw < MIN_USABLE_COMPLETION_TOKENS:
        return default
    return raw


def _message_content_text(message: dict[str, Any]) -> str:
    content = message.get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict):
                parts.append(str(block.get("text") or ""))
        return "".join(parts)
    return ""


def _public_usage(body: dict[str, Any]) -> dict[str, int]:
    usage = body.get("usage") if isinstance(body.get("usage"), dict) else {}
    public: dict[str, int] = {}
    for key in ("prompt_tokens", "completion_tokens", "total_tokens", "input_tokens", "output_tokens"):
        value = usage.get(key)
        if isinstance(value, int):
            public[key] = value
    details = usage.get("completion_tokens_details")
    if isinstance(details, dict):
        reasoning = details.get("reasoning_tokens")
        if isinstance(reasoning, int):
            public["reasoning_tokens"] = reasoning
    return public


def truncated_finish(reason: str | None) -> bool:
    return (reason or "").strip().lower() in _LENGTH_FINISH_REASONS


def public_llm_view(
    completion: dict[str, Any],
    *,
    max_tokens: int,
    max_tokens_source: str,
    declared_max_output_tokens: int | None,
) -> dict[str, Any]:
    finish = str(completion.get("finish_reason") or "")
    text = str(completion.get("text") or "")
    view: dict[str, Any] = {
        "max_tokens": max_tokens,
        "max_tokens_source": max_tokens_source,
        "declared_max_output_tokens": declared_max_output_tokens,
        "finish_reason": finish,
        "content_chars": int(completion.get("content_chars") or len(text)),
        "model": str(completion.get("model") or ""),
        "truncated": bool(completion.get("truncated")) or truncated_finish(finish),
    }
    usage = completion.get("usage")
    if isinstance(usage, dict) and usage:
        view["usage"] = usage
    return view


def env_default_llm() -> str:
    canonical = canonicalize_provider(os.environ.get("DEFAULT_LLM"))
    if canonical:
        return canonical
    for item in PROVIDER_CATALOG.values():
        if item["kind"] != "local" and _secret_configured(item.get("key_env")):
            return item["id"]
    return "local_deterministic"


def _secret_configured(key_env: str | None) -> bool:
    if not key_env:
        return True
    return bool(os.environ.get(key_env, "").strip())


def list_providers() -> list[dict[str, Any]]:
    rows = []
    for item in PROVIDER_CATALOG.values():
        key_env = item.get("key_env")
        rows.append(
            {
                "id": item["id"],
                "label": item["label"],
                "kind": item["kind"],
                "configured": _secret_configured(key_env),
                "model": os.environ.get(item["model_env"], item.get("default_model", "")) if item.get("model_env") else "",
            }
        )
    return rows


@dataclass
class LlmSettings:
    path: Path
    default_llm: str | None = None
    agents: dict[str, str] = field(default_factory=dict)

    @classmethod
    def load(cls, path: Path) -> "LlmSettings":
        if not path.is_file():
            return cls(path=path)
        payload = json.loads(path.read_text(encoding="utf-8"))
        agents = payload.get("agents") or {}
        cleaned = {
            str(key): canonicalize_provider(str(value))
            for key, value in agents.items()
            if value
        }
        default = payload.get("default_llm")
        return cls(
            path=path,
            default_llm=canonicalize_provider(str(default)) if default else None,
            agents=cleaned,
        )

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps({"default_llm": self.default_llm, "agents": self.agents}, indent=2) + "\n",
            encoding="utf-8",
        )

    def resolved_default(self) -> str:
        return canonicalize_provider(self.default_llm) or env_default_llm()

    def resolved_for(self, agent_id: str) -> str:
        override = canonicalize_provider(self.agents.get(agent_id))
        if override:
            return override
        return self.resolved_default()

    def public_view(self) -> dict[str, Any]:
        return {
            "env_default": env_default_llm(),
            "default_llm": self.resolved_default(),
            "default_source": "operator" if self.default_llm else "DEFAULT_LLM",
            "agents": dict(self.agents),
            "providers": list_providers(),
        }


def _http_post(url: str, headers: dict[str, str], payload: dict[str, Any]) -> dict[str, Any]:
    try:
        import httpx
    except ImportError as exc:
        raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="httpx is required for external LLM routes") from exc
    try:
        response = httpx.post(url, headers=headers, json=payload, timeout=60.0)
        response.raise_for_status()
        body = response.json()
        if not isinstance(body, dict):
            raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="LLM response was not an object")
        return body
    except CasopsError:
        raise
    except Exception as exc:
        raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="external LLM route failed") from exc


def _chat_turns(
    *,
    prompt: str,
    system: str = "",
    history: list[dict[str, str]] | None = None,
) -> list[dict[str, str]]:
    turns: list[dict[str, str]] = []
    if system.strip():
        turns.append({"role": "system", "content": system.strip()})
    for item in history or []:
        role = str(item.get("role") or "").strip().lower()
        content = str(item.get("content") or "").strip()
        if role in {"user", "assistant"} and content:
            turns.append({"role": role, "content": content})
    turns.append({"role": "user", "content": prompt})
    return turns


@dataclass
class LlmRouter:
    settings: LlmSettings = field(default_factory=lambda: LlmSettings(path=Path("var/llm-settings.json")))
    post: PostFn = field(default=_http_post)
    local: DeterministicAdapter = field(default_factory=DeterministicAdapter)

    def resolve(self, agent_id: str) -> str:
        provider = canonicalize_provider(self.settings.resolved_for(agent_id))
        if provider not in PROVIDER_CATALOG:
            raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail=f"unknown LLM provider {provider}")
        spec = PROVIDER_CATALOG[provider]
        if spec["kind"] != "local" and not _secret_configured(spec.get("key_env")):
            raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail=f"{provider} is not configured in .env")
        return provider

    def complete(
        self,
        *,
        agent_id: str,
        prompt: str,
        node_id: str,
        max_tokens: int = 512,
        system: str = "",
        history: list[dict[str, str]] | None = None,
    ) -> dict[str, Any]:
        provider = self.resolve(agent_id)
        turns = _chat_turns(prompt=prompt, system=system, history=history)
        if provider == "local_deterministic":
            blob = "\n\n".join(f"{turn['role']}: {turn['content']}" for turn in turns)
            local = self.local.complete(prompt=blob, node_id=node_id, agent_id=agent_id)
            text = str(local.get("text") or "")
            local["model"] = "local_deterministic"
            local["finish_reason"] = "stop"
            local["content_chars"] = len(text)
            local["truncated"] = False
            return local
        spec = PROVIDER_CATALOG[provider]
        key = os.environ.get(spec["key_env"], "").strip()
        base = (os.environ.get(spec.get("base_env", ""), "") or spec.get("default_base") or "").rstrip("/")
        model = os.environ.get(spec.get("model_env", ""), "") or spec.get("default_model") or "unknown"
        finish_reason = ""
        usage: dict[str, int] = {}
        if spec["kind"] == "openai_compat":
            body = self.post(
                f"{base}/chat/completions",
                {"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                {
                    "model": model,
                    "messages": turns,
                    "max_tokens": max_tokens,
                },
            )
            choices = body.get("choices") or []
            choice = choices[0] if choices and isinstance(choices[0], dict) else {}
            message = choice.get("message") if isinstance(choice.get("message"), dict) else {}
            text = _message_content_text(message)
            finish_reason = str(choice.get("finish_reason") or "")
            usage = _public_usage(body)
        elif spec["kind"] == "anthropic":
            system_text = "\n\n".join(
                turn["content"] for turn in turns if turn["role"] == "system"
            )
            payload: dict[str, Any] = {
                "model": model,
                "max_tokens": max_tokens,
                "messages": [turn for turn in turns if turn["role"] != "system"],
            }
            if system_text:
                payload["system"] = system_text
            body = self.post(
                f"{base}/v1/messages",
                {
                    "x-api-key": key,
                    "anthropic-version": "2023-06-01",
                    "Content-Type": "application/json",
                },
                payload,
            )
            blocks = body.get("content") or []
            text = "".join(str(block.get("text") or "") for block in blocks if isinstance(block, dict))
            finish_reason = str(body.get("stop_reason") or "")
            usage = _public_usage(body)
        else:
            raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail=f"unsupported LLM kind {spec['kind']}")
        digest = sha256_json({"provider": provider, "model": model, "text": text, "agent_id": agent_id})
        result: dict[str, Any] = {
            "provider": provider,
            "model": model,
            "node_id": node_id,
            "text": text,
            "digest": digest,
            "finish_reason": finish_reason,
            "content_chars": len(text),
            "truncated": truncated_finish(finish_reason),
        }
        if usage:
            result["usage"] = usage
        return result
