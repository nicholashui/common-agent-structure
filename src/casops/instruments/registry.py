"""Instrument qualification registry (plan §12). Host-owned, append-only."""

from __future__ import annotations

import json
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from casops.artifacts.atomic import atomic_write
from casops.auth.actors import ActorClass, is_allowed
from casops.contracts.canonical import canonical_dumps, sha256_json
from casops.corrigibility.signing import HostSigner
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

INSTRUMENT_IDS: tuple[str, ...] = tuple(f"INS-{index:02d}" for index in range(1, 9))
RECORDS_FILE = "records.json"


class QualificationStatus(str, Enum):
    UNQUALIFIED = "UNQUALIFIED"
    QUALIFIED = "QUALIFIED"
    EXPIRED = "EXPIRED"


@dataclass(frozen=True)
class InstrumentRecord:
    ins_id: str
    version: str
    status: QualificationStatus
    digest: str
    signature: str = ""


class InstrumentRegistry:
    def __init__(
        self,
        *,
        data_dir: Path | None = None,
        signer: HostSigner | None = None,
    ) -> None:
        self._data_dir = data_dir
        self.signer = signer or HostSigner.generate()
        self._records: dict[str, InstrumentRecord] = {
            ins_id: self._fresh(ins_id) for ins_id in INSTRUMENT_IDS
        }
        if data_dir is not None:
            self._persist()

    def _fresh(self, ins_id: str) -> InstrumentRecord:
        payload = {"ins_id": ins_id, "version": "0", "status": QualificationStatus.UNQUALIFIED.value}
        digest = sha256_json(payload)
        return InstrumentRecord(
            ins_id=ins_id,
            version="0",
            status=QualificationStatus.UNQUALIFIED,
            digest=digest,
            signature=self.signer.sign(digest),
        )

    @classmethod
    def open(cls, *, data_dir: Path, key_path: Path) -> InstrumentRegistry:
        data_dir.mkdir(parents=True, exist_ok=True)
        signer = HostSigner.load(key_path)
        path = data_dir / RECORDS_FILE
        if not path.is_file():
            return cls(data_dir=data_dir, signer=signer)
        raw = json.loads(path.read_text(encoding="utf-8"))
        registry = cls.__new__(cls)
        registry._data_dir = data_dir
        registry.signer = signer
        registry._records = {}
        for ins_id in INSTRUMENT_IDS:
            item = raw.get(ins_id) or {}
            digest = str(item.get("digest") or "")
            signature = str(item.get("signature") or "")
            if not digest or not signer.verify(digest, signature):
                raise CasopsError(ErrorCode.IMP_CORRIGIBILITY, detail=f"tampered instrument {ins_id}")
            registry._records[ins_id] = InstrumentRecord(
                ins_id=ins_id,
                version=str(item.get("version") or "0"),
                status=QualificationStatus(item.get("status") or "UNQUALIFIED"),
                digest=digest,
                signature=signature,
            )
        return registry

    def get(self, ins_id: str) -> InstrumentRecord:
        return self._records[ins_id]

    def may_gate(self, ins_id: str) -> bool:
        return self.get(ins_id).status is QualificationStatus.QUALIFIED

    def any_unqualified(self) -> bool:
        return any(record.status is not QualificationStatus.QUALIFIED for record in self._records.values())

    def append_record(
        self,
        *,
        actor: ActorClass,
        ins_id: str,
        status: QualificationStatus,
    ) -> None:
        if not is_allowed(actor, "write_instrument_record"):
            raise CasopsError(ErrorCode.IMP_SCOPE)
        current = self.get(ins_id)
        payload = {
            "ins_id": ins_id,
            "version": current.version,
            "status": status.value,
        }
        digest = sha256_json(payload)
        self._records[ins_id] = InstrumentRecord(
            ins_id=ins_id,
            version=current.version,
            status=status,
            digest=digest,
            signature=self.signer.sign(digest),
        )
        self._persist()

    def _persist(self) -> None:
        if self._data_dir is None:
            return
        body = {
            ins_id: {
                "ins_id": record.ins_id,
                "version": record.version,
                "status": record.status.value,
                "digest": record.digest,
                "signature": record.signature,
            }
            for ins_id, record in self._records.items()
        }
        atomic_write(self._data_dir / RECORDS_FILE, canonical_dumps(body) + "\n")

