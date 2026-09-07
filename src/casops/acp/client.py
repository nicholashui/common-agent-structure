"""ACP stdio client. Drops thought chunks. Never logs transport secrets."""

from __future__ import annotations

import os
import subprocess
import threading
import time
from queue import Empty, Queue
from collections.abc import Callable
from typing import Any

from casops.acp.protocol import (
    THOUGHT_UPDATES,
    decode_message,
    encode_message,
    error_payload,
    notify_payload,
    request_payload,
    text_from_update,
    update_kind,
)
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


def resolve_acp_auth_method(auth_ids: set[str], *, env: dict[str, str] | None = None) -> str | None:
    """Pick a headless ACP auth method. Never selects interactive grok.com."""
    ids = {item for item in auth_ids if item}
    if not ids:
        return None
    environ = env if env is not None else os.environ
    if "xai.api_key" in ids and str(environ.get("XAI_API_KEY") or "").strip():
        return "xai.api_key"
    if "cached_token" in ids:
        return "cached_token"
    raise CasopsError(
        ErrorCode.PERF_ROUTE_UNAVAILABLE,
        detail=(
            "ACP auth required: set XAI_API_KEY or log in so Grok offers cached_token. "
            "Interactive grok.com login is not performed."
        ),
    )


class StdioAcpClient:
    def __init__(
        self,
        proc: subprocess.Popen[Any],
        *,
        timeout_s: float = 120.0,
        debug: Callable[..., None] | None = None,
    ) -> None:
        self.proc = proc
        self.timeout_s = timeout_s
        self._debug = debug
        self._next_id = 1
        self._queue: Queue[dict[str, Any]] = Queue()
        self._chunks: list[str] = []
        self._lock = threading.Lock()
        self._reader = threading.Thread(target=self._read_loop, daemon=True)
        self._reader.start()

    def _trace(self, name: str, **fields: Any) -> None:
        if self._debug is None:
            return
        try:
            self._debug(name, **fields)
        except Exception:
            return

    def close(self) -> None:
        if self.proc.poll() is None:
            try:
                if self.proc.stdin:
                    self.proc.stdin.close()
            except OSError:
                pass
            self.proc.terminate()
            try:
                self.proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.proc.kill()

    def initialize(self, *, agent_id: str, extra_meta: dict[str, Any] | None = None) -> dict[str, Any]:
        meta = {"casops": {"host": "casops", "client_role": "orchestrator", "agent_id": agent_id}}
        if extra_meta:
            meta["casops"].update(extra_meta)
        result = self.request(
            "initialize",
            {
                "protocolVersion": 1,
                "clientCapabilities": {},
                "clientInfo": {"name": "casops", "version": "0.1.0"},
                "_meta": meta,
            },
        )
        methods = result.get("authMethods") if isinstance(result.get("authMethods"), list) else []
        ids = {str(item.get("id") or "") for item in methods if isinstance(item, dict)}
        self._trace(
            "initialize",
            protocolVersion=result.get("protocolVersion"),
            auth_ids=sorted(item for item in ids if item),
        )
        method_id = resolve_acp_auth_method(ids)
        if method_id:
            self.request("authenticate", {"methodId": method_id, "_meta": {"headless": True}})
            self._trace("authenticate", methodId=method_id)
        return result

    def session_new(
        self,
        *,
        cwd: str,
        agent_id: str,
        task_id: str,
        extra_casops: dict[str, Any] | None = None,
    ) -> str:
        casops = {
            "agent_id": agent_id,
            "task_id": task_id,
            "taint": {"class": "external_peer", "instruction_authority": False},
        }
        if extra_casops:
            casops.update(extra_casops)
        result = self.request(
            "session/new",
            {
                "cwd": cwd,
                "mcpServers": [],
                "_meta": {
                    "yoloMode": True,
                    "agentProfile": agent_id,
                    "casops": casops,
                },
            },
        )
        session_id = str(result.get("sessionId") or result.get("session_id") or "")
        if not session_id:
            raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="ACP session/new returned no sessionId")
        self._trace("session_new", session_id=session_id)
        return session_id

    def prompt(self, session_id: str, text: str, *, casops: dict[str, Any] | None = None) -> dict[str, Any]:
        with self._lock:
            self._chunks = []
        params: dict[str, Any] = {
            "sessionId": session_id,
            "prompt": [{"type": "text", "text": text}],
        }
        if casops:
            params["_meta"] = {"casops": casops}
        result = self.request("session/prompt", params)
        with self._lock:
            reply = "".join(self._chunks)
        stop_reason = str(result.get("stopReason") or result.get("stop_reason") or "")
        self._trace("session_prompt", session_id=session_id, stop_reason=stop_reason, reply_chars=len(reply))
        return {
            "text": reply or str(result.get("text") or ""),
            "stop_reason": stop_reason,
            "usage": result.get("usage") if isinstance(result.get("usage"), dict) else {},
            "session_id": session_id,
        }

    def cancel(self, session_id: str) -> None:
        self.notify("session/cancel", {"sessionId": session_id})

    def session_close(self, session_id: str) -> None:
        try:
            self.request("session/close", {"sessionId": session_id})
        except CasopsError:
            return

    def request(self, method: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        req_id = self._next_id
        self._next_id += 1
        started = time.monotonic()
        self._write(request_payload(req_id, method, params))
        deadline = time.monotonic() + self.timeout_s
        while time.monotonic() < deadline:
            try:
                message = self._queue.get(timeout=0.1)
            except Empty:
                if self.proc.poll() is not None:
                    self._trace("rpc", method=method, ok=False, error="process exited")
                    raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="ACP process exited")
                continue
            self._handle_incoming(message)
            if message.get("id") == req_id and "result" in message:
                result = message.get("result")
                self._trace("rpc", method=method, ok=True, ms=int((time.monotonic() - started) * 1000))
                return result if isinstance(result, dict) else {}
            if message.get("id") == req_id and "error" in message:
                err = message.get("error") if isinstance(message.get("error"), dict) else {}
                detail = str(err.get("message") or "ACP request failed")
                self._trace("rpc", method=method, ok=False, error=detail, ms=int((time.monotonic() - started) * 1000))
                raise CasopsError(
                    ErrorCode.PERF_ROUTE_UNAVAILABLE,
                    detail=detail,
                )
        self._trace("rpc", method=method, ok=False, error="timeout")
        raise CasopsError(ErrorCode.PERF_DEADLINE, detail=f"ACP {method} timed out")

    def notify(self, method: str, params: dict[str, Any] | None = None) -> None:
        self._write(notify_payload(method, params))

    def _handle_incoming(self, message: dict[str, Any]) -> None:
        method = str(message.get("method") or "")
        params = message.get("params") if isinstance(message.get("params"), dict) else {}
        if method == "session/update":
            kind = update_kind(params)
            if kind in THOUGHT_UPDATES:
                return
            chunk = text_from_update(params)
            if chunk:
                with self._lock:
                    self._chunks.append(chunk)
            return
        req_id = message.get("id")
        if method and req_id is not None and "result" not in message and "error" not in message:
            if method == "session/request_permission":
                self._write({"jsonrpc": "2.0", "id": req_id, "result": {"outcome": "cancelled"}})
                self._trace("peer_rpc", method=method, outcome="cancelled")
                return
            self._write(error_payload(req_id, -32601, "method not found"))
            self._trace("peer_rpc", method=method, outcome="method_not_found")

    def _write(self, payload: dict[str, Any]) -> None:
        stdin = self.proc.stdin
        if stdin is None:
            raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="ACP stdin closed")
        raw = encode_message(payload).encode("utf-8")
        try:
            stdin.write(raw)  # type: ignore[arg-type]
            stdin.flush()
        except TypeError:
            stdin.write(encode_message(payload))
            stdin.flush()
        except OSError as exc:
            raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="ACP write failed") from exc

    def _read_loop(self) -> None:
        stdout = self.proc.stdout
        if stdout is None:
            return
        while True:
            try:
                line = stdout.readline()
            except UnicodeDecodeError:
                self._trace("rpc", method="stdout", ok=False, error="utf8_replace")
                continue
            if line in ("", b""):
                return
            if isinstance(line, bytes):
                text = line.decode("utf-8", errors="replace")
            else:
                text = line
            message = decode_message(text)
            if message is not None:
                self._queue.put(message)
