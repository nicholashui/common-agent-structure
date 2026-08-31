"""I2 separate-process sandbox: no ambient network, no production credentials."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.plugins.i1_wasm import IDENTITY_WAT
from casops.plugins.sandbox_env import guest_env

_SRC = Path(__file__).resolve().parents[2]


@dataclass
class I2Result:
    output: bytes
    executed: bool
    mechanism: str = "process"
    tier: str = "I2"
    raw: dict[str, Any] | None = None


def _clean_env() -> dict[str, str]:
    return guest_env(pythonpath=_SRC, sandbox="I2")


def _invoke(request: dict[str, Any], *, cwd: Path | None = None, timeout: float = 8.0) -> dict[str, Any]:
    payload = json.dumps(request)
    proc = subprocess.run(
        [sys.executable, "-m", "casops.plugins.guest"],
        input=payload,
        capture_output=True,
        text=True,
        env=_clean_env(),
        cwd=str(cwd) if cwd else None,
        timeout=timeout,
        check=False,
    )
    if not proc.stdout.strip():
        raise CasopsError(ErrorCode.PLG_ISOLATION_TIER, detail=proc.stderr[-400:])
    return json.loads(proc.stdout)


class I2Runtime:
    def run(self, wat: str, payload: bytes, *, sandbox: Path | None = None) -> I2Result:
        result = _invoke(
            {
                "op": "transform",
                "wat": wat or IDENTITY_WAT,
                "payload_hex": payload.hex(),
                "deny_network": True,
            },
            cwd=sandbox,
        )
        if not result.get("ok"):
            raise CasopsError(ErrorCode.PLG_ISOLATION_TIER, detail=str(result))
        return I2Result(output=bytes.fromhex(result["output_hex"]), executed=True, raw=result)

    def probe_network(self, host: str = "127.0.0.1", port: int = 1) -> dict[str, Any]:
        return _invoke({"op": "probe_network", "host": host, "port": port, "deny_network": True})

    def probe_env(self, key: str) -> str | None:
        result = _invoke({"op": "probe_env", "key": key, "deny_network": True})
        return result.get("value")
