"""Out-of-process trainer bridge: export trajectories, signed adapter import only."""

from __future__ import annotations

from typing import Any

from casops.corrigibility.signing import HostSigner
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.runtime.executor import RunResult


class TrainerBridge:
    def __init__(self, signer: HostSigner | None = None) -> None:
        self.signer = signer or HostSigner.generate()
        self.exports: list[dict[str, Any]] = []
        self.imported: list[dict[str, Any]] = []
        self.gradient_updates_in_serving = 0

    def export_trajectory(self, result: RunResult) -> dict[str, Any]:
        payload = {
            "agent_id": result.agent_id,
            "root_trace_id": result.root_trace_id,
            "artifact": result.artifact,
        }
        digest = result.artifact["digest"]
        envelope = {"trajectory": payload, "digest": digest, "signature": self.signer.sign(digest)}
        self.exports.append(envelope)
        return envelope

    def import_adapter(self, *, digest: str, signature: str, blob: dict[str, Any] | None = None) -> dict[str, Any]:
        if not self.signer.verify(digest, signature):
            raise CasopsError(ErrorCode.IMP_UNSIGNED)
        record = {"digest": digest, "blob": blob or {}, "applied_gradient_in_serving": False}
        self.imported.append(record)
        return record
