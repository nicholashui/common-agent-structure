"""Six actor classes and a deny-by-default authorization matrix (WP-105)."""

from __future__ import annotations

from enum import Enum


class ActorClass(str, Enum):
    human_operator = "human_operator"
    independent_approver = "independent_approver"
    host_service = "host_service"
    agent_runtime = "agent_runtime"
    plugin = "plugin"
    peer_agent = "peer_agent"


# Explicit allow-list. Anything else is denied.
_ALLOWED: frozenset[tuple[ActorClass, str]] = frozenset(
    {
        (ActorClass.host_service, "attest_invariants"),
        (ActorClass.host_service, "read_invariant_reference"),
        (ActorClass.independent_approver, "write_invariant_reference"),
        (ActorClass.independent_approver, "approve_candidate"),
        (ActorClass.independent_approver, "write_instrument_record"),
        (ActorClass.independent_approver, "l5_research_write"),
        (ActorClass.host_service, "l5_research_write"),
        (ActorClass.human_operator, "operator_shutdown"),
        (ActorClass.human_operator, "read_invariant_reference"),
        (ActorClass.host_service, "write_instrument_record"),
        (ActorClass.host_service, "read_instrument"),
        (ActorClass.human_operator, "read_alerts"),
        (ActorClass.host_service, "read_alerts"),
        (ActorClass.independent_approver, "read_alerts"),
    }
)


def is_allowed(actor: ActorClass, action: str) -> bool:
    return (actor, action) in _ALLOWED
