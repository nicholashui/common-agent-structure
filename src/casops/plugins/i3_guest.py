"""I3 isolated guest: no host FS, allow-listed egress proxy. Firecracker used when present."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import threading
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, quote, urlparse

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.plugins.i1_wasm import IDENTITY_WAT
from casops.plugins.sandbox_env import guest_env

_SRC = Path(__file__).resolve().parents[2]


def firecracker_available() -> bool:
    return shutil.which("firecracker") is not None


@dataclass
class I3Result:
    output: bytes
    executed: bool
    mechanism: str
    tier: str = "I3"
    raw: dict[str, Any] | None = None


class _ProxyState:
    def __init__(self, allowlist: set[str], fixtures: dict[str, bytes]) -> None:
        self.allowlist = allowlist
        self.fixtures = fixtures


def _make_handler(state: _ProxyState) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            parsed = urlparse(self.path)
            if parsed.path != "/fetch":
                self.send_error(404)
                return
            url = (parse_qs(parsed.query).get("url") or [""])[0]
            host = urlparse(url).hostname or ""
            if host not in state.allowlist:
                self.send_error(403, "not allowlisted")
                return
            body = state.fixtures.get(url, b"ok")
            self.send_response(200)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *_args: object) -> None:
            return

    return Handler


class EgressProxy:
    def __init__(self, allowlist: set[str], fixtures: dict[str, bytes] | None = None) -> None:
        self.state = _ProxyState(allowlist, fixtures or {})
        self._server = ThreadingHTTPServer(("127.0.0.1", 0), _make_handler(self.state))
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)

    @property
    def url(self) -> str:
        host, port = self._server.server_address[:2]
        return f"http://{host}:{port}"

    @property
    def port(self) -> int:
        return int(self._server.server_address[1])

    def start(self) -> None:
        self._thread.start()

    def stop(self) -> None:
        self._server.shutdown()
        self._server.server_close()


def _clean_env() -> dict[str, str]:
    env = guest_env(pythonpath=_SRC, sandbox="I3")
    env["CASOPS_NETWORK"] = "proxy"
    return env


def _invoke(request: dict[str, Any], *, cwd: Path, timeout: float = 8.0) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, "-m", "casops.plugins.guest"],
        input=json.dumps(request),
        capture_output=True,
        text=True,
        env=_clean_env(),
        cwd=str(cwd),
        timeout=timeout,
        check=False,
    )
    if not proc.stdout.strip():
        raise CasopsError(ErrorCode.PLG_ISOLATION_TIER, detail=proc.stderr[-400:])
    return json.loads(proc.stdout)


class I3Runtime:
    def __init__(self, sandbox: Path, *, allowlist: set[str] | None = None, fixtures: dict[str, bytes] | None = None) -> None:
        self.sandbox = sandbox.resolve()
        self.sandbox.mkdir(parents=True, exist_ok=True)
        self.allowlist = allowlist or set()
        self.fixtures = fixtures or {}
        self.firecracker_present = firecracker_available()
        self.mechanism = "isolated_guest"

    def run(self, wat: str, payload: bytes) -> I3Result:
        result = _invoke(
            {
                "op": "transform",
                "wat": wat or IDENTITY_WAT,
                "payload_hex": payload.hex(),
                "sandbox_root": str(self.sandbox),
                "deny_network": True,
            },
            cwd=self.sandbox,
        )
        if not result.get("ok"):
            raise CasopsError(ErrorCode.PLG_ISOLATION_TIER, detail=str(result))
        return I3Result(output=bytes.fromhex(result["output_hex"]), executed=True, mechanism=self.mechanism, raw=result)

    def probe_fs(self, path: str) -> dict[str, Any]:
        return _invoke(
            {"op": "probe_fs", "path": path, "sandbox_root": str(self.sandbox), "deny_network": True},
            cwd=self.sandbox,
        )

    def egress(self, url: str) -> dict[str, Any]:
        proxy = EgressProxy(self.allowlist, self.fixtures)
        proxy.start()
        try:
            return _invoke(
                {
                    "op": "egress",
                    "url": f"{proxy.url}/fetch?url={quote(url, safe='')}",
                    "proxy": proxy.url,
                    "sandbox_root": str(self.sandbox),
                    # I3 may reach only the proxy; ambient sockets remain denied.
                    "deny_network": False,
                    "proxy_only": {"host": "127.0.0.1", "port": proxy.port},
                },
                cwd=self.sandbox,
            )
        finally:
            proxy.stop()

    def probe_network(self, host: str, port: int) -> dict[str, Any]:
        return _invoke(
            {
                "op": "probe_network",
                "host": host,
                "port": port,
                "sandbox_root": str(self.sandbox),
                "deny_network": True,
            },
            cwd=self.sandbox,
        )
