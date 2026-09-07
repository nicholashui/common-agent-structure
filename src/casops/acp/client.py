"""ACP stdio client. Drops thought chunks. Never logs transport secrets."""

from __future__ import annotations

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
    notify_payload,
    request_payload,
    text_from_update,
    update_kind,
)
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


class StdioAcpClient:
    def __init__(
        self,
        proc: subprocess.Popen[str],
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
        if "cached_token" in ids:
            self.request("authenticate", {"methodId": "cached_token", "_meta": {"headless": True}})
            self._trace("authenticate", methodId="cached_token")
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
        if method == "session/request_permission" and "id" in message:
            self._write(
                {
                    "jsonrpc": "2.0",
                    "id": message["id"],
                    "result": {"outcome": "cancelled"},
                }
            )

    def _write(self, payload: dict[str, Any]) -> None:
        stdin = self.proc.stdin
        if stdin is None:
            raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="ACP stdin closed")
        try:
            stdin.write(encode_message(payload))
            stdin.flush()
        except OSError as exc:
            raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="ACP write failed") from exc

    def _read_loop(self) -> None:
        stdout = self.proc.stdout
        if stdout is None:
            return
        while True:
            line = stdout.readline()
            if line == "":
                return
            message = decode_message(line)
            if message is not None:
                self._queue.put(message)
