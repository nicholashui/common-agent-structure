"""Persistent signed corrigibility store (FR-COR-001..003, WP-101..103)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from casops.auth.actors import ActorClass
from casops.corrigibility.checkpoints import Checkpoint
from casops.corrigibility.signing import HostSigner
from casops.corrigibility.store import InvariantStore
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


def _store(tmp_path: Path) -> InvariantStore:
    data_dir = tmp_path / "corrigibility"
    key = HostSigner.generate()
    key.save(tmp_path / "ed25519.pem")
    return InvariantStore.open(data_dir=data_dir, key_path=tmp_path / "ed25519.pem")


def test_reference_is_signed_and_verifiable(tmp_path: Path) -> None:
    store = _store(tmp_path)
    record = store.reference()
    assert record.digest == store.reference_digest()
    assert record.signature
    assert record.invariant_set_id == "casops.host.inv.v1"
    assert store.signer.verify(record.digest, record.signature) is True


def test_digest_survives_reload(tmp_path: Path) -> None:
    first = _store(tmp_path)
    digest = first.reference_digest()
    signature = first.reference().signature
    reloaded = InvariantStore.open(
        data_dir=tmp_path / "corrigibility",
        key_path=tmp_path / "ed25519.pem",
    )
    assert reloaded.reference_digest() == digest
    assert reloaded.reference().signature == signature


def test_tampered_reference_file_containment_stops(tmp_path: Path) -> None:
    store = _store(tmp_path)
    path = tmp_path / "corrigibility" / "reference.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["invariants"][0]["text"] = "tampered"
    path.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(CasopsError) as raised:
        InvariantStore.open(
            data_dir=tmp_path / "corrigibility",
            key_path=tmp_path / "ed25519.pem",
        )
    assert raised.value.code == ErrorCode.IMP_CORRIGIBILITY
    assert raised.value.containment_required is True
    assert raised.value.degraded_mode is False


def test_mismatch_records_operator_alert(tmp_path: Path) -> None:
    store = _store(tmp_path)
    with pytest.raises(CasopsError):
        store.attest(
            actor=ActorClass.host_service,
            presented_digest="0" * 64,
            checkpoint=Checkpoint.compose,
            agent_id="casops.template.baseline_safe",
        )
    alerts = store.alerts()
    assert alerts
    last = alerts[-1]
    assert last["kind"] == "digest_mismatch"
    assert last["checkpoint"] == Checkpoint.compose.value
    assert last["containment_required"] is True
    assert last["previous_hash"] != last["entry_hash"]


@pytest.mark.parametrize(
    "checkpoint",
    [Checkpoint.compose, Checkpoint.run_start, Checkpoint.production_effect],
)
def test_checkpoints_reattest(tmp_path: Path, checkpoint: Checkpoint) -> None:
    store = _store(tmp_path)
    result = store.attest(
        actor=ActorClass.host_service,
        presented_digest=store.reference_digest(),
        checkpoint=checkpoint,
        agent_id="agent.one",
    )
    assert result.match is True
    assert result.checkpoint is checkpoint


def test_approver_write_rotates_signature(tmp_path: Path) -> None:
    store = _store(tmp_path)
    original = store.reference_digest()
    new_invariants = [{"id": "INV-01", "text": "tightened permission invariant"}]
    store.replace_reference(actor=ActorClass.independent_approver, invariants=new_invariants)
    assert store.reference_digest() != original
    assert store.signer.verify(store.reference_digest(), store.reference().signature)


def test_projection_is_marked_host_owned(tmp_path: Path) -> None:
    store = _store(tmp_path)
    dest = tmp_path / "agent" / "corrigibility" / "invariants.json"
    store.write_projection(dest)
    payload = json.loads(dest.read_text(encoding="utf-8"))
    assert payload["writable_by_agent"] is False
    assert payload["source"] == "host_owned_reference"
    assert payload["digest"] == store.reference_digest()
    assert dest.stat().st_mode & 0o222 == 0
