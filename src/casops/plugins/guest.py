"""Isolated plugin guest. Used by I2/I3 subprocesses. No ambient network; optional FS jail."""

from __future__ import annotations

import json
import socket
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from urllib.request import Request, urlopen


def deny_network() -> None:
    def blocked(*_args: object, **_kwargs: object) -> socket.socket:
        raise OSError("ambient network denied")

    socket.socket = blocked  # type: ignore[assignment]


def proxy_only_network(host: str, port: int) -> None:
    real_create = socket.create_connection

    def create_connection(address, *args, **kwargs):  # type: ignore[no-untyped-def]
        target_host, target_port = address[0], address[1]
        if str(target_host) not in {host, "127.0.0.1", "localhost"} or int(target_port) != int(port):
            raise OSError("ambient network denied")
        return real_create(address, *args, **kwargs)

    socket.create_connection = create_connection  # type: ignore[assignment]


def confine_fs(root: Path) -> None:
    import builtins
    import io

    root = root.resolve()
    real_open = io.open

    def jailed_open(file, mode="r", *args, **kwargs):  # type: ignore[no-untyped-def]
        path = Path(str(file)).resolve()
        try:
            path.relative_to(root)
        except ValueError as exc:
            raise PermissionError(f"host FS denied: {path}") from exc
        return real_open(file, mode, *args, **kwargs)

    builtins.open = jailed_open  # type: ignore[assignment]
    io.open = jailed_open  # type: ignore[assignment]


def _transform(wat: str, payload: bytes) -> bytes:
    from casops.plugins.i1_wasm import I1Runtime

    return I1Runtime().run(wat, payload).output


def handle(request: dict[str, Any]) -> dict[str, Any]:
    op = request.get("op")
    if op == "transform":
        payload = bytes.fromhex(request["payload_hex"])
        output = _transform(request["wat"], payload)
        return {"ok": True, "output_hex": output.hex()}
    if op == "probe_network":
        try:
            socket.create_connection((request.get("host") or "127.0.0.1", int(request.get("port") or 1)), timeout=0.3)
            return {"ok": True, "connected": True}
        except OSError as exc:
            return {"ok": False, "connected": False, "error": str(exc)}
    if op == "probe_fs":
        path = request["path"]
        try:
            data = Path(path).read_text(encoding="utf-8")
            return {"ok": True, "data": data}
        except (OSError, PermissionError) as exc:
            return {"ok": False, "error": str(exc)}
    if op == "probe_env":
        import os

        key = request["key"]
        return {"ok": True, "value": os.environ.get(key)}
    if op == "egress":
        url = request["url"]
        proxy = request.get("proxy")
        if not proxy:
            return {"ok": False, "error": "no egress proxy"}
        try:
            req = Request(url, headers={"X-Casops-Proxy": "1"})
            with urlopen(req, timeout=2.0) as response:  # noqa: S310 — guest may only reach the host proxy
                body = response.read()
            return {"ok": True, "body_hex": body.hex(), "status": response.status}
        except OSError as exc:
            return {"ok": False, "error": str(exc)}
    return {"ok": False, "error": f"unknown op {op}"}


def main(argv: list[str] | None = None) -> int:
    del argv
    request = json.loads(sys.stdin.read())
    # Import the WASM runtime before FS jail so host libraries can load.
    if request.get("op") == "transform":
        from casops.plugins import i1_wasm as _i1

        del _i1
    if request.get("deny_network"):
        deny_network()
    proxy_only = request.get("proxy_only") or {}
    if proxy_only.get("host") and proxy_only.get("port"):
        proxy_only_network(str(proxy_only["host"]), int(proxy_only["port"]))
    sandbox = request.get("sandbox_root")
    if sandbox:
        confine_fs(Path(sandbox))
    result = handle(request)
    sys.stdout.write(json.dumps(result))
    sys.stdout.flush()
    return 0 if result.get("ok") else 2


if __name__ == "__main__":
    raise SystemExit(main())
