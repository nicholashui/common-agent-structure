"""Trainer-bridge rejects unsigned adapters and never applies serving gradients."""

from __future__ import annotations

from pathlib import Path

import pytest

from casops.corrigibility.store import InvariantStore
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.improvement.trainer import TrainerBridge
from casops.runtime.executor import Runtime

REPO = Path(__file__).resolve().parents[2]


def test_unsigned_import_rejected() -> None:
    bridge = TrainerBridge()
    with pytest.raises(CasopsError) as raised:
        bridge.import_adapter(digest="abc", signature="00")
    assert raised.value.code == ErrorCode.IMP_UNSIGNED
    assert bridge.gradient_updates_in_serving == 0


def test_export_and_signed_import() -> None:
    runtime = Runtime(agents_root=REPO / "agents", store=InvariantStore.with_host_defaults())
    result = runtime.execute("casops.template.baseline_safe")
    bridge = TrainerBridge()
    envelope = bridge.export_trajectory(result)
    imported = bridge.import_adapter(digest=envelope["digest"], signature=envelope["signature"])
    assert imported["applied_gradient_in_serving"] is False
    assert bridge.gradient_updates_in_serving == 0
