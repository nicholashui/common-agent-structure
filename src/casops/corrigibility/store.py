"""Host-owned invariant store. Authoritative copy is never agent-writable."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from casops.artifacts.atomic import atomic_write
from casops.auth.actors import ActorClass, is_allowed
from casops.contracts.canonical import canonical_dumps, sha256_json
from casops.corrigibility.checkpoints import Checkpoint
from casops.corrigibility.invariants import HOST_INVARIANTS, INVARIANT_SET_ID
from casops.corrigibility.signing import HostSigner
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

REFERENCE_FILE = "reference.json"
ALERTS_FILE = "alerts.jsonl"


@dataclass(frozen=True)
class SignedReference:
    invariant_set_id: str
    digest: str
    signature: str
    invariants: list[dict[str, str]]


@dataclass(frozen=True)
class AttestationResult:
    match: bool
    digest: str
    signature: str
    checkpoint: Checkpoint


class InvariantStore:
    def __init__(
        self,
        invariants: list[dict[str, str]] | None = None,
        *,
        data_dir: Path | None = None,
        signer: HostSigner | None = None,
    ) -> None:
        self._invariants = list(invariants or HOST_INVARIANTS)
        self.fail_closed = False
        self._data_dir = data_dir
        self.signer = signer or HostSigner.generate()
        self._alerts: list[dict[str, Any]] = []

    @classmethod
    def with_host_defaults(cls) -> InvariantStore:
        return cls(list(HOST_INVARIANTS))

    @classmethod
    def open(cls, *, data_dir: Path, key_path: Path) -> InvariantStore:
        data_dir.mkdir(parents=True, exist_ok=True)
        signer = HostSigner.load(key_path)
        reference_path = data_dir / REFERENCE_FILE
        if not reference_path.is_file():
            store = cls(list(HOST_INVARIANTS), data_dir=data_dir, signer=signer)
            store._persist_reference()
            return store
        payload = json.loads(reference_path.read_text(encoding="utf-8"))
        invariants = list(payload.get("invariants") or [])
        digest = sha256_json({"invariants": invariants})
        signature = str(payload.get("signature") or "")
        if digest != payload.get("digest") or not signer.verify(digest, signature):
            raise CasopsError(
                ErrorCode.IMP_CORRIGIBILITY,
                detail="tamper detected on persisted invariant reference",
            )
        store = cls(invariants, data_dir=data_dir, signer=signer)
        store._load_alerts()
        return store

    def reference_digest(self) -> str:
        return sha256_json({"invariants": self._invariants})

    def snapshot(self) -> list[dict[str, str]]:
        return [dict(item) for item in self._invariants]

    def reference(self) -> SignedReference:
        digest = self.reference_digest()
        return SignedReference(
            invariant_set_id=INVARIANT_SET_ID,
            digest=digest,
            signature=self.signer.sign(digest),
            invariants=self.snapshot(),
        )

    def alerts(self) -> list[dict[str, Any]]:
        return list(self._alerts)

    def attest(
        self,
        *,
        actor: ActorClass,
        presented_digest: str,
        checkpoint: Checkpoint | str = Checkpoint.compose,
        agent_id: str | None = None,
    ) -> AttestationResult:
        point = checkpoint if isinstance(checkpoint, Checkpoint) else Checkpoint(checkpoint)
        if not is_allowed(actor, "attest_invariants"):
            self._alert(
                "unauthorized_attest",
                checkpoint=point,
                agent_id=agent_id,
                actor=actor.value,
            )
            raise CasopsError(ErrorCode.IMP_CORRIGIBILITY)
        if self.fail_closed:
            self._alert(
                "service_unavailable",
                checkpoint=point,
                agent_id=agent_id,
                actor=actor.value,
            )
            raise CasopsError(
                ErrorCode.IMP_CORRIGIBILITY,
                detail="invariant service unavailable; containment stop; no degraded mode",
            )
        digest = self.reference_digest()
        signature = self.signer.sign(digest)
        if presented_digest != digest:
            self._alert(
                "digest_mismatch",
                checkpoint=point,
                agent_id=agent_id,
                actor=actor.value,
                presented_digest=presented_digest,
            )
            raise CasopsError(ErrorCode.IMP_CORRIGIBILITY)
        return AttestationResult(
            match=True,
            digest=digest,
            signature=signature,
            checkpoint=point,
        )

    def replace_reference(self, *, actor: ActorClass, invariants: list[dict[str, str]]) -> None:
        if not is_allowed(actor, "write_invariant_reference"):
            self._alert("unauthorized_write", actor=actor.value)
            raise CasopsError(ErrorCode.IMP_CORRIGIBILITY)
        self._invariants = [dict(item) for item in invariants]
        self._persist_reference()

    def write_projection(self, dest: Path) -> None:
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            try:
                dest.chmod(0o644)
            except OSError:
                pass
        record = self.reference()
        payload = {
            "schema_version": "3.0",
            "source": "host_owned_reference",
            "writable_by_agent": False,
            "digest": record.digest,
            "invariants": record.invariants,
        }
        atomic_write(dest, json.dumps(payload, indent=2) + "\n")
        dest.chmod(0o444)

    def _alert(
        self,
        kind: str,
        *,
        checkpoint: Checkpoint | None = None,
        agent_id: str | None = None,
        actor: str | None = None,
        presented_digest: str | None = None,
    ) -> None:
        previous = self._alerts[-1]["entry_hash"] if self._alerts else "0" * 64
        body = {
            "kind": kind,
            "checkpoint": None if checkpoint is None else checkpoint.value,
            "agent_id": agent_id,
            "actor": actor,
            "presented_digest": presented_digest,
            "containment_required": True,
            "previous_hash": previous,
        }
        entry = dict(body)
        entry["entry_hash"] = sha256_json(body)
        self._alerts.append(entry)
        self._persist_alert(entry)

    def _persist_reference(self) -> None:
        if self._data_dir is None:
            return
        record = self.reference()
        payload = {
            "invariant_set_id": record.invariant_set_id,
            "schema_version": "3.0",
            "invariants": record.invariants,
            "digest": record.digest,
            "signature": record.signature,
        }
        atomic_write(self._data_dir / REFERENCE_FILE, canonical_dumps(payload) + "\n")

    def _persist_alert(self, entry: dict[str, Any]) -> None:
        if self._data_dir is None:
            return
        path = self._data_dir / ALERTS_FILE
        with path.open("a", encoding="utf-8") as handle:
            handle.write(canonical_dumps(entry) + "\n")

    def _load_alerts(self) -> None:
        if self._data_dir is None:
            return
        path = self._data_dir / ALERTS_FILE
        if not path.is_file():
            return
        loaded: list[dict[str, Any]] = []
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                loaded.append(json.loads(line))
        self._alerts = loaded
