"""ACP process debug files: logs/acp/<agent_id>.*.log. No prompt/thought/secret text."""

from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Any

from casops.debuglog import acp_log_paths, acp_log_stamp, clip_field
from casops.time import isoformat_hkt

_DENY = {
    "prompt",
    "text",
    "system",
    "history",
    "content",
    "token",
    "authorization",
    "secret",
    "password",
    "cached_token",
}


class AcpProcessLog:
    def __init__(self, agent_id: str) -> None:
        stamp = acp_log_stamp()
        paths = acp_log_paths(agent_id, stamp)
        self.agent_id = agent_id
        self.stamp = stamp
        self.host_path = paths["host"]
        self.stderr_path = paths["stderr"]
        self.host_path.parent.mkdir(parents=True, exist_ok=True)
        self._host = self.host_path.open("a", encoding="utf-8")
        self._stderr = self.stderr_path.open("a", encoding="utf-8")
        self._lock = threading.Lock()
        self._pump: threading.Thread | None = None

    def event(self, name: str, **fields: Any) -> None:
        record: dict[str, Any] = {
            "ts": isoformat_hkt(),
            "agent_id": self.agent_id,
            "event": name,
        }
        for key, value in fields.items():
            if str(key).lower() in _DENY:
                continue
            record[str(key)] = clip_field(value)
        line = json.dumps(record, ensure_ascii=False, default=str)
        with self._lock:
            self._host.write(line + "\n")
            self._host.flush()

    def attach_stderr(self, proc: Any) -> None:
        self._pump = threading.Thread(target=self._pump_stderr, args=(proc,), daemon=True)
        self._pump.start()

    def close(self) -> None:
        pump = self._pump
        if pump is not None:
            pump.join(timeout=2)
        with self._lock:
            for handle in (self._host, self._stderr):
                try:
                    handle.close()
                except OSError:
                    pass

    def _pump_stderr(self, proc: Any) -> None:
        stream = getattr(proc, "stderr", None)
        if stream is None:
            return
        while True:
            try:
                line = stream.readline()
            except UnicodeDecodeError:
                continue
            except OSError:
                return
            if line in ("", b""):
                return
            if isinstance(line, bytes):
                decoded = line.decode("utf-8", errors="replace")
            else:
                decoded = line
            ts = isoformat_hkt()
            text = clip_field(decoded.rstrip("\r\n"))
            with self._lock:
                try:
                    self._stderr.write(f"{ts} {text}\n")
                    self._stderr.flush()
                except OSError:
                    return
