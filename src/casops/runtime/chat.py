"""Operator chat prompt: agent prompt + declared I/O + history + message."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

_MAX_HISTORY = 20
_MAX_MESSAGE_CHARS = 32_000


def normalize_history(raw: Any) -> list[dict[str, str]]:
    if not isinstance(raw, list):
        return []
    turns: list[dict[str, str]] = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        role = str(item.get("role") or "").strip().lower()
        content = str(item.get("content") or "").strip()
        if role not in {"user", "assistant"} or not content:
            continue
        turns.append({"role": role, "content": content})
    return turns[-_MAX_HISTORY:]


def require_message(message: str) -> str:
    text = (message or "").strip()
    if not text:
        raise CasopsError(ErrorCode.CTX_BUDGET, detail="chat message required")
    if len(text) > _MAX_MESSAGE_CHARS:
        raise CasopsError(ErrorCode.CTX_BUDGET, detail="chat message exceeds context budget")
    return text


def load_prompt(folder: Path, spec: dict[str, Any]) -> tuple[str, str]:
    ref = str(spec.get("prompt_reference") or "prompts/primary.md")
    candidate = folder / ref
    if candidate.is_file():
        return candidate.read_text(encoding="utf-8"), ref
    primary = folder / "prompts" / "primary.md"
    if primary.is_file():
        return primary.read_text(encoding="utf-8"), "prompts/primary.md"
    return "", ref


def build_chat_system(*, prompt: str, io: dict[str, Any]) -> str:
    parts: list[str] = []
    if prompt.strip():
        parts.append(prompt.strip())
    inputs = io.get("inputs") if isinstance(io.get("inputs"), list) else []
    outputs = io.get("outputs") if isinstance(io.get("outputs"), list) else []
    parts.append("## Declared input requirements")
    parts.append(", ".join(str(item) for item in inputs) if inputs else "(none declared)")
    parts.append("## Declared output requirements")
    parts.append(", ".join(str(item) for item in outputs) if outputs else "(none declared)")
    parts.append("## Human operator")
    parts.append(
        "The operator may send free-text chat messages. Treat the latest operator message as your input "
        "and reply in natural language. Do not require peer-agent critique payloads unless the operator provides them."
    )
    return "\n\n".join(parts)


def build_chat_prompt(
    *,
    system: str,
    io: dict[str, Any],
    history: list[dict[str, str]],
    message: str,
) -> str:
    parts = [build_chat_system(prompt=system, io=io)]
    if history:
        parts.append("## Conversation")
        for turn in history:
            label = "Operator" if turn.get("role") == "user" else "Agent"
            parts.append(f"{label}: {turn.get('content', '')}")
    parts.append("## Operator message")
    parts.append(message)
    return "\n\n".join(parts)
