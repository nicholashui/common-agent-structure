"""INV-01..INV-12 copied from spec §15.1."""

from __future__ import annotations

INVARIANT_SET_ID = "casops.host.inv.v1"

HOST_INVARIANTS: tuple[dict[str, str], ...] = (
    {"id": "INV-01", "text": "The agent cannot modify permissions, tools, or plugin grants."},
    {"id": "INV-02", "text": "It cannot modify safety or termination policy."},
    {"id": "INV-03", "text": "It cannot modify mandatory telemetry retention or redaction policy."},
    {"id": "INV-04", "text": "It cannot modify gate thresholds, held-out sets, or analysis plans."},
    {"id": "INV-05", "text": "It cannot request production activation or grant network access."},
    {"id": "INV-06", "text": "It cannot approve, sign, or promote candidates."},
    {"id": "INV-07", "text": "It cannot delete or rewrite audit, ledger, or incident records."},
    {"id": "INV-08", "text": "It cannot disable, degrade, or bypass safety."},
    {"id": "INV-09", "text": "It cannot remove regression or safety fixtures."},
    {
        "id": "INV-10",
        "text": "It cannot suppress, delay, or reorder shutdown, cancellation, or deadline signals.",
    },
    {"id": "INV-11", "text": "It cannot read the reasoning-monitor channel or influence verdicts."},
    {"id": "INV-12", "text": "It cannot lower plugin isolation or forge capability handles."},
)

ACTION_TO_INVARIANT: dict[str, str] = {
    "modify_permissions": "INV-01",
    "modify_safety_policy": "INV-02",
    "modify_telemetry_retention": "INV-03",
    "modify_gate_thresholds": "INV-04",
    "request_production_activation": "INV-05",
    "approve_candidate": "INV-06",
    "rewrite_audit_record": "INV-07",
    "bypass_safety": "INV-08",
    "remove_regression_fixture": "INV-09",
    "suppress_cancellation": "INV-10",
    "read_reasoning_monitor": "INV-11",
    "forge_capability_handle": "INV-12",
}
