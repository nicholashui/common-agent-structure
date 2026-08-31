"""Capability handles are unforgeable, expiring, and revocable."""

from __future__ import annotations

import time

import pytest

from casops.auth.handles import HandleBroker
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


def test_minted_handle_verifies_for_audience_and_scope() -> None:
    broker = HandleBroker()
    handle = broker.mint(audience="runtime", scope="model", ttl_seconds=30)
    broker.verify(handle, audience="runtime", scope="model")


def test_forged_signature_is_rejected() -> None:
    broker = HandleBroker()
    handle = broker.mint(audience="runtime", scope="model")
    forged = type(handle)(
        handle_id=handle.handle_id,
        audience=handle.audience,
        scope=handle.scope,
        expires_at=handle.expires_at,
        signature="00" * 32,
    )
    with pytest.raises(CasopsError) as raised:
        broker.verify(forged, audience="runtime", scope="model")
    assert raised.value.code == ErrorCode.PLG_HANDLE_FORGERY


def test_revoked_and_expired_handles_fail() -> None:
    broker = HandleBroker()
    handle = broker.mint(audience="plugin", scope="fs", ttl_seconds=0.01)
    broker.revoke(handle.handle_id)
    with pytest.raises(CasopsError):
        broker.verify(handle, audience="plugin", scope="fs")
    time.sleep(0.02)
    fresh = broker.mint(audience="plugin", scope="fs", ttl_seconds=0.01)
    time.sleep(0.02)
    with pytest.raises(CasopsError):
        broker.verify(fresh, audience="plugin", scope="fs")
