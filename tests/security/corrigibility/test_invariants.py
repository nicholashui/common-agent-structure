"""FR-COR-006: INV-01..INV-12 each have a negative fixture that aborts."""

from __future__ import annotations

import pytest

from casops.auth.actors import ActorClass
from casops.corrigibility.enforcement import attempt_forbidden
from casops.errors.exceptions import CasopsError

INVARIANTS = (
    ("INV-01", "modify_permissions"),
    ("INV-02", "modify_safety_policy"),
    ("INV-03", "modify_telemetry_retention"),
    ("INV-04", "modify_gate_thresholds"),
    ("INV-05", "request_production_activation"),
    ("INV-06", "approve_candidate"),
    ("INV-07", "rewrite_audit_record"),
    ("INV-08", "bypass_safety"),
    ("INV-09", "remove_regression_fixture"),
    ("INV-10", "suppress_cancellation"),
    ("INV-11", "read_reasoning_monitor"),
    ("INV-12", "forge_capability_handle"),
)


@pytest.mark.parametrize(("invariant_id", "action"), INVARIANTS)
def test_negative_fixture_aborts(invariant_id: str, action: str) -> None:
    with pytest.raises(CasopsError) as raised:
        attempt_forbidden(actor=ActorClass.agent_runtime, action=action)
    assert raised.value.containment_required or raised.value.code.value.startswith(
        ("IMP_", "SAF_", "GATE_", "INH_")
    )
    assert raised.value.invariant_id == invariant_id
