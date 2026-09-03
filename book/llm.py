"""Shared LLM provider selection for book scripts. Credentials stay in book/.env."""

from __future__ import annotations

import os
import time
from dataclasses import dataclass
from pathlib import Path

import requests

ENV_PATH = Path(__file__).resolve().parent / ".env"

LLM_ALIASES = {
    "grok": "xai",
    "x-ai": "xai",
    "x_ai": "xai",
}

LLM_PROVIDERS: dict[str, dict[str, object]] = {
    "xai": {
        "label": "xAI Grok",
        "kind": "openai_compat",
        "key_envs": ("XAI_API_KEY", "GROK_API_KEY"),
        "base_envs": ("XAI_BASE_URL", "XAI_API_BASE", "GROK_BASE_URL"),
        "model_envs": ("XAI_MODEL", "GROK_MODEL"),
        "default_base": "https://api.x.ai/v1",
        "default_model": "grok-4",
    },
    "openai": {
        "label": "OpenAI",
        "kind": "openai_compat",
        "key_envs": ("OPENAI_API_KEY",),
        "base_envs": ("OPENAI_BASE_URL",),
        "model_envs": ("OPENAI_MODEL",),
        "default_base": "https://api.openai.com/v1",
        "default_model": "gpt-4o-mini",
    },
    "anthropic": {
        "label": "Anthropic",
        "kind": "anthropic",
        "key_envs": ("ANTHROPIC_API_KEY",),
        "base_envs": ("ANTHROPIC_BASE_URL",),
        "model_envs": ("ANTHROPIC_MODEL",),
        "default_base": "https://api.anthropic.com",
        "default_model": "claude-sonnet-4-5",
    },
    "poe": {
        "label": "Poe",
        "kind": "openai_compat",
        "key_envs": ("POE_API_KEY",),
        "base_envs": ("POE_BASE_URL",),
        "model_envs": ("POE_BASE_MODEL", "POE_MODEL"),
        "default_base": "https://api.poe.com/v1",
        "default_model": "grok-4",
    },
    "deepseek": {
        "label": "DeepSeek",
        "kind": "openai_compat",
        "key_envs": ("DEEPSEEK_API_KEY",),
        "base_envs": ("DEEPSEEK_BASE_URL",),
        "model_envs": ("DEEPSEEK_MODEL",),
        "default_base": "https://api.deepseek.com/v1",
        "default_model": "deepseek-chat",
    },
}

LLM_CHOICES = tuple(sorted({*LLM_PROVIDERS, *LLM_ALIASES}))


def canonicalize_llm(name: str) -> str:
    text = (name or "").strip().lower()
    if text in LLM_ALIASES:
        return LLM_ALIASES[text]
    if text in LLM_PROVIDERS:
        return text
    raise ValueError(
        f"unknown LLM {name!r}; choose one of: {', '.join(LLM_CHOICES)}"
    )


def _first_env(names: tuple[str, ...]) -> str:
    for name in names:
        value = os.getenv(name, "").strip()
        if value:
            return value
    return ""


@dataclass(frozen=True)
class LlmClient:
    provider: str
    label: str
    kind: str
    api_key: str
    base_url: str
    model: str


def resolve_llm(name: str, model: str | None = None) -> LlmClient:
    provider = canonicalize_llm(name)
    spec = LLM_PROVIDERS[provider]
    api_key = _first_env(spec["key_envs"])  # type: ignore[arg-type]
    if not api_key:
        keys = ", ".join(spec["key_envs"])  # type: ignore[arg-type]
        raise ValueError(f"{keys} not found in {ENV_PATH} for LLM {provider}")
    base = _first_env(spec["base_envs"]) or str(spec["default_base"])  # type: ignore[arg-type]
    chosen_model = (model or "").strip() or _first_env(spec["model_envs"]) or str(spec["default_model"])  # type: ignore[arg-type]
    return LlmClient(
        provider=provider,
        label=str(spec["label"]),
        kind=str(spec["kind"]),
        api_key=api_key,
        base_url=base.rstrip("/"),
        model=chosen_model,
    )


def add_llm_args(parser) -> None:
    parser.add_argument(
        "--llm",
        type=str.lower,
        default=(os.getenv("BOOK_LLM") or "xai").lower(),
        choices=LLM_CHOICES,
        help="LLM provider from book/.env: xai, grok, openai, anthropic, poe, deepseek "
        "(default xai, or $BOOK_LLM)",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="override the provider model (else provider MODEL env, else catalog default)",
    )


def complete(
    client: LlmClient,
    system_prompt: str,
    user_content: str,
    *,
    temperature: float,
    timeout: int = 180,
    max_retries: int = 4,
) -> str:
    last_error: Exception | None = None
    for attempt in range(1, max_retries + 1):
        try:
            if client.kind == "anthropic":
                return _complete_anthropic(
                    client, system_prompt, user_content, temperature=temperature, timeout=timeout
                )
            return _complete_openai_compat(
                client, system_prompt, user_content, temperature=temperature, timeout=timeout
            )
        except Exception as exc:
            last_error = exc
            if attempt >= max_retries:
                break
            wait = min(2**attempt, 20)
            status = getattr(getattr(exc, "response", None), "status_code", None)
            print(f"    retry {attempt}/{max_retries} status={status} wait={wait}s: {exc}")
            time.sleep(wait)
    raise last_error if last_error else RuntimeError("LLM call failed")


def _complete_openai_compat(
    client: LlmClient,
    system_prompt: str,
    user_content: str,
    *,
    temperature: float,
    timeout: int,
) -> str:
    url = f"{client.base_url}/chat/completions"
    headers = {
        "Authorization": f"Bearer {client.api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": client.model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        "temperature": temperature,
    }
    resp = requests.post(url, headers=headers, json=payload, timeout=timeout)
    if resp.status_code == 429 or resp.status_code >= 500:
        raise requests.HTTPError(f"HTTP {resp.status_code}: {resp.text[:300]}", response=resp)
    resp.raise_for_status()
    data = resp.json()
    choices = data.get("choices") or []
    if not choices:
        raise ValueError(f"Unexpected API response: {data}")
    return str((choices[0].get("message") or {}).get("content") or "").strip()


def _complete_anthropic(
    client: LlmClient,
    system_prompt: str,
    user_content: str,
    *,
    temperature: float,
    timeout: int,
) -> str:
    base = client.base_url.rstrip("/")
    if not base.endswith("/v1"):
        url = f"{base}/v1/messages"
    else:
        url = f"{base}/messages"
    headers = {
        "x-api-key": client.api_key,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json",
    }
    payload = {
        "model": client.model,
        "max_tokens": 8192,
        "temperature": temperature,
        "system": system_prompt,
        "messages": [{"role": "user", "content": user_content}],
    }
    resp = requests.post(url, headers=headers, json=payload, timeout=timeout)
    if resp.status_code == 429 or resp.status_code >= 500:
        raise requests.HTTPError(f"HTTP {resp.status_code}: {resp.text[:300]}", response=resp)
    resp.raise_for_status()
    data = resp.json()
    blocks = data.get("content") or []
    text = "".join(str(block.get("text") or "") for block in blocks if isinstance(block, dict))
    if not text.strip():
        raise ValueError(f"Unexpected API response: {data}")
    return text.strip()
