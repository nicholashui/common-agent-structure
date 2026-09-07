"""JSON-RPC 2.0 line framing for ACP stdio."""

from __future__ import annotations

import json
from typing import Any


def encode_message(payload: dict[str, Any]) -> str:
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n"


def decode_message(line: str) -> dict[str, Any] | None:
    text = line.strip()
    if not text:
        return None
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        return None
    return payload if isinstance(payload, dict) else None


def request_payload(req_id: int, method: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    body: dict[str, Any] = {"jsonrpc": "2.0", "id": req_id, "method": method}
    if params is not None:
        body["params"] = params
    return body


def notify_payload(method: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    body: dict[str, Any] = {"jsonrpc": "2.0", "method": method}
    if params is not None:
        body["params"] = params
    return body


def result_payload(req_id: Any, result: Any) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": req_id, "result": result}


def error_payload(req_id: Any, code: int, message: str) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": code, "message": message}}


THOUGHT_UPDATES = frozenset({"agent_thought_chunk", "thought_chunk"})


def update_kind(params: dict[str, Any]) -> str:
    update = params.get("update")
    if isinstance(update, dict):
        return str(update.get("sessionUpdate") or update.get("session_update") or "")
    return str(params.get("sessionUpdate") or "")


def text_from_update(params: dict[str, Any]) -> str:
    kind = update_kind(params)
    if kind in THOUGHT_UPDATES:
        return ""
    update = params.get("update") if isinstance(params.get("update"), dict) else params
    if not isinstance(update, dict):
        return ""
    content = update.get("content")
    return _content_text(content)


def _content_text(content: Any) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, dict):
        if content.get("type") in {"text", None} and isinstance(content.get("text"), str):
            return str(content.get("text") or "")
        return _content_text(content.get("content"))
    if isinstance(content, list):
        return "".join(_content_text(item) for item in content)
    return ""
