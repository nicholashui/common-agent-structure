"""Corrigibility attestation: mismatch is containment stop, no degraded mode."""

from __future__ import annotations

import pytest

from casops.auth.actors import ActorClass
from casops.corrigibility.store import InvariantStore
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


def test_matching_digest_attests() -> None:
    store = InvariantStore.with_host_defaults()
    result = store.attest(
        actor=ActorClass.host_service,
        presented_digest=store.reference_digest(),
    )
    assert result.match is True


def test_mismatch_raises_imp_corrigibility_with_containment() -> None:
    store = InvariantStore.with_host_defaults()
    with pytest.raises(CasopsError) as raised:
        store.attest(actor=ActorClass.host_service, presented_digest="0" * 64)
    assert raised.value.code == ErrorCode.IMP_CORRIGIBILITY
    assert raised.value.containment_required is True
    assert raised.value.degraded_mode is False


def test_rpc_style_failure_is_containment_not_degraded() -> None:
    store = InvariantStore.with_host_defaults()
    store.fail_closed = True
    with pytest.raises(CasopsError) as raised:
        store.attest(actor=ActorClass.host_service, presented_digest=store.reference_digest())
    assert raised.value.containment_required is True


def test_agent_cannot_write_reference() -> None:
    store = InvariantStore.with_host_defaults()
    original = store.reference_digest()
    with pytest.raises(CasopsError):
        store.replace_reference(actor=ActorClass.agent_runtime, invariants=[])
    assert store.reference_digest() == original
