"""Instrument registry is host-owned; instruments start UNQUALIFIED (IQ-01/IQ-08)."""

from __future__ import annotations

from pathlib import Path

import pytest

from casops.auth.actors import ActorClass
from casops.errors.exceptions import CasopsError
from casops.instruments.registry import INSTRUMENT_IDS, InstrumentRegistry, QualificationStatus


def test_all_eight_instruments_are_unqualified() -> None:
    registry = InstrumentRegistry()
    assert set(INSTRUMENT_IDS) == {f"INS-{i:02d}" for i in range(1, 9)}
    for ins_id in INSTRUMENT_IDS:
        record = registry.get(ins_id)
        assert record.status is QualificationStatus.UNQUALIFIED


def test_agent_cannot_append_qualification_record() -> None:
    registry = InstrumentRegistry()
    with pytest.raises(CasopsError):
        registry.append_record(
            actor=ActorClass.agent_runtime,
            ins_id="INS-01",
            status=QualificationStatus.QUALIFIED,
        )
    assert registry.get("INS-01").status is QualificationStatus.UNQUALIFIED


def test_unqualified_instrument_may_not_gate() -> None:
    registry = InstrumentRegistry()
    assert registry.may_gate("INS-01") is False


def test_signed_records_survive_reload(tmp_path: Path) -> None:
    from casops.corrigibility.signing import HostSigner

    key_path = tmp_path / "ed25519.pem"
    HostSigner.generate().save(key_path)
    data_dir = tmp_path / "instruments"
    first = InstrumentRegistry.open(data_dir=data_dir, key_path=key_path)
    first.append_record(
        actor=ActorClass.host_service,
        ins_id="INS-03",
        status=QualificationStatus.UNQUALIFIED,
    )
    digest = first.get("INS-01").digest
    signature = first.get("INS-01").signature
    assert digest
    assert signature
    reloaded = InstrumentRegistry.open(data_dir=data_dir, key_path=key_path)
    assert reloaded.get("INS-01").digest == digest
    assert reloaded.get("INS-01").signature == signature
    assert reloaded.get("INS-01").status is QualificationStatus.UNQUALIFIED
    assert reloaded.may_gate("INS-01") is False
    assert reloaded.any_unqualified() is True
