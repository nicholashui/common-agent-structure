"""Minimal ACP stdio agent for pytest. No network. No tools."""

from __future__ import annotations

import json
import os
import sys


def _read() -> dict | None:
    line = sys.stdin.readline()
    if line == "":
        return None
    line = line.strip()
    if not line:
        return {}
    try:
        payload = json.loads(line)
    except json.JSONDecodeError:
        return {}
    return payload if isinstance(payload, dict) else {}


def _write(payload: dict) -> None:
    line = json.dumps(payload, separators=(",", ":"), ensure_ascii=False) + "\n"
    sys.stdout.write(line)
    sys.stdout.flush()


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stdin, "reconfigure"):
        sys.stdin.reconfigure(encoding="utf-8")
    sessions = 0
    advertised = [item.strip() for item in os.environ.get("CASOPS_FAKE_ACP_AUTH", "").split(",") if item.strip()]
    authed = not advertised
    while True:
        message = _read()
        if message is None:
            return
        if not message:
            continue
        method = str(message.get("method") or "")
        req_id = message.get("id")
        params = message.get("params") if isinstance(message.get("params"), dict) else {}
        if method == "initialize":
            version = params.get("protocolVersion")
            if version not in {1, "1"}:
                _write(
                    {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "error": {"code": -32602, "message": "protocolVersion must be 1"},
                    }
                )
                continue
            _write(
                {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "protocolVersion": 1,
                        "agentCapabilities": {"loadSession": False, "promptCapabilities": {}},
                        "authMethods": [{"id": item} for item in advertised],
                    },
                }
            )
            _write(
                {
                    "jsonrpc": "2.0",
                    "method": "session/update",
                    "params": {
                        "update": {
                            "sessionUpdate": "agent_thought_chunk",
                            "content": {"type": "text", "text": "— café 意圖"},
                        }
                    },
                }
            )
        elif method == "authenticate":
            method_id = str(params.get("methodId") or "")
            if advertised and method_id not in advertised:
                _write(
                    {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "error": {"code": -32602, "message": f"unknown auth method {method_id}"},
                    }
                )
                continue
            authed = True
            _write({"jsonrpc": "2.0", "id": req_id, "result": {}})
        elif method == "session/new":
            if advertised and not authed:
                _write(
                    {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "error": {"code": -32000, "message": "authenticate before session/new"},
                    }
                )
                continue
            if params.get("mcpServers") != []:
                _write(
                    {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "error": {"code": -32602, "message": "mcpServers must be []"},
                    }
                )
                continue
            sessions += 1
            perm_id = f"perm-{sessions}"
            _write(
                {
                    "jsonrpc": "2.0",
                    "id": perm_id,
                    "method": "session/request_permission",
                    "params": {"options": [{"optionId": "allow", "name": "allow"}]},
                }
            )
            while True:
                reply = _read()
                if reply is None:
                    return
                if reply.get("id") == perm_id:
                    break
            _write({"jsonrpc": "2.0", "id": req_id, "result": {"sessionId": f"fake-{os.getpid()}-{sessions}"}})
        elif method == "session/prompt":
            prompt = params.get("prompt")
            text = ""
            if isinstance(prompt, list):
                for block in prompt:
                    if isinstance(block, dict):
                        text += str(block.get("text") or "")
            echo = os.environ.get("CASOPS_FAKE_ACP_ECHO", "tail").strip().lower()
            if echo == "full":
                chunk = f"{text}**1. Locution** fake-analysis"
            elif echo == "pack":
                chunk = (
                    "You are Demo (`demo.agent`).\n"
                    "Voice: neutral.\n"
                    "Does not own: Credentials\n"
                    "Enabled skills: (none enabled — do not load SKILL.md).\n"
                    "Host chat: treat the latest operator message as free-text input and reply in natural language. "
                    "Do not call tools, write memory, enable T3, or request network.\n\n"
                    "## System\n\nYou are demo.\n\n"
                    f"## Operator message\n\n{text}**1. Locution** fake-analysis"
                )
            else:
                chunk = f"fake-acp:{text[-80:]}"
            _write(
                {
                    "jsonrpc": "2.0",
                    "method": "session/update",
                    "params": {
                        "sessionId": params.get("sessionId"),
                        "update": {
                            "sessionUpdate": "agent_message_chunk",
                            "content": {"type": "text", "text": chunk},
                        },
                    },
                }
            )
            _write(
                {
                    "jsonrpc": "2.0",
                    "method": "session/update",
                    "params": {
                        "sessionId": params.get("sessionId"),
                        "update": {"sessionUpdate": "agent_thought_chunk", "content": {"type": "text", "text": "SECRET_COT"}},
                    },
                }
            )
            _write({"jsonrpc": "2.0", "id": req_id, "result": {"stopReason": "end_turn"}})
        elif method == "session/close":
            _write({"jsonrpc": "2.0", "id": req_id, "result": {}})
        elif method == "session/cancel":
            continue
        elif req_id is not None:
            _write({"jsonrpc": "2.0", "id": req_id, "result": {}})


if __name__ == "__main__":
    main()
