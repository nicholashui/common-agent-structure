"""Dispatch plugin execution to the matching isolation runtime. No silent downgrade."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from casops.auth.handles import HandleBroker
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.plugins.i1_wasm import IDENTITY_WAT, I1Runtime
from casops.plugins.i2_process import I2Runtime
from casops.plugins.i3_guest import I3Runtime
from casops.plugins.validate import isolation_of, validate_manifest


def execute_plugin(
    manifest: dict[str, Any],
    payload: bytes,
    *,
    folder: Path | None = None,
    wat: str | None = None,
    sandbox: Path | None = None,
    allowlist: set[str] | None = None,
    broker: HandleBroker | None = None,
) -> dict[str, Any]:
    validated = validate_manifest(manifest, folder=folder)
    isolation = isolation_of(manifest)
    source = wat or IDENTITY_WAT
    if isolation in {"I0", "none", ""}:
        raise CasopsError(ErrorCode.PLG_ISOLATION_TIER, detail="I0 in-process execution is first-party transform only")
    if isolation == "I1":
        result = I1Runtime(broker).run(source, payload)
        return {"tier": "I1", "output": result.output, "mechanism": result.mechanism, "executed": True, "id": validated["id"]}
    if isolation == "I2":
        result = I2Runtime().run(source, payload, sandbox=sandbox)
        return {"tier": "I2", "output": result.output, "mechanism": result.mechanism, "executed": True, "id": validated["id"]}
    if isolation == "I3":
        if sandbox is None:
            raise CasopsError(ErrorCode.PLG_ISOLATION_TIER, detail="I3 requires an isolated sandbox root")
        result = I3Runtime(sandbox, allowlist=allowlist).run(source, payload)
        return {"tier": "I3", "output": result.output, "mechanism": result.mechanism, "executed": True, "id": validated["id"]}
    raise CasopsError(ErrorCode.PLG_ISOLATION_TIER)
