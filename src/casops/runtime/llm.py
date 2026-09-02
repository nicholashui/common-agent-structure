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
    ) -> dict[str, str]:
        provider = self.resolve(agent_id)
        turns = _chat_turns(prompt=prompt, system=system, history=history)
        if provider == "local_deterministic":
            blob = "\n\n".join(f"{turn['role']}: {turn['content']}" for turn in turns)
            return self.local.complete(prompt=blob, node_id=node_id, agent_id=agent_id)
        spec = PROVIDER_CATALOG[provider]
        key = os.environ.get(spec["key_env"], "").strip()
        base = (os.environ.get(spec.get("base_env", ""), "") or spec.get("default_base") or "").rstrip("/")
        model = os.environ.get(spec.get("model_env", ""), "") or spec.get("default_model") or "unknown"
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
            message = (choices[0].get("message") or {}) if choices else {}
            text = str(message.get("content") or "")
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
        else:
            raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail=f"unsupported LLM kind {spec['kind']}")
        digest = sha256_json({"provider": provider, "model": model, "text": text, "agent_id": agent_id})
        return {
            "provider": provider,
            "model": model,
            "node_id": node_id,
            "text": text,
            "digest": digest,
        }
