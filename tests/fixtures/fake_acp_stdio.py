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
    sys.stdout.write(json.dumps(payload, separators=(",", ":")) + "\n")
    sys.stdout.flush()


def main() -> None:
    sessions = 0
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
                        "authMethods": [],
                    },
                }
            )
        elif method == "session/new":
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
            _write({"jsonrpc": "2.0", "id": req_id, "result": {"sessionId": f"fake-{os.getpid()}-{sessions}"}})
        elif method == "session/prompt":
            prompt = params.get("prompt")
            text = ""
            if isinstance(prompt, list):
                for block in prompt:
                    if isinstance(block, dict):
                        text += str(block.get("text") or "")
            _write(
                {
                    "jsonrpc": "2.0",
                    "method": "session/update",
                    "params": {
                        "sessionId": params.get("sessionId"),
                        "update": {
                            "sessionUpdate": "agent_message_chunk",
                            "content": {"type": "text", "text": f"fake-acp:{text[-80:]}"},
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
