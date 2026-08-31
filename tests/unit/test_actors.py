"""Actor classes and deny-by-default matrix (WP-105)."""

from __future__ import annotations

import pytest

from casops.auth.actors import ActorClass, is_allowed


def test_six_actor_classes_exist() -> None:
    names = {member.value for member in ActorClass}
    assert names == {
        "human_operator",
        "independent_approver",
        "host_service",
        "agent_runtime",
        "plugin",
        "peer_agent",
    }


@pytest.mark.parametrize(
    ("actor", "action"),
    [
        (ActorClass.agent_runtime, "write_invariant_reference"),
        (ActorClass.agent_runtime, "approve_candidate"),
        (ActorClass.plugin, "write_invariant_reference"),
        (ActorClass.peer_agent, "write_invariant_reference"),
        (ActorClass.agent_runtime, "bypass_safety"),
    ],
)
def test_agent_like_actors_are_denied_host_actions(actor: ActorClass, action: str) -> None:
    assert is_allowed(actor, action) is False


def test_unknown_action_is_denied() -> None:
    assert is_allowed(ActorClass.human_operator, "not_a_real_action") is False


def test_independent_approver_may_write_invariant_reference() -> None:
    assert is_allowed(ActorClass.independent_approver, "write_invariant_reference") is True


def test_host_service_may_attest() -> None:
    assert is_allowed(ActorClass.host_service, "attest_invariants") is True


def test_agent_runtime_may_not_attest_as_authority() -> None:
    assert is_allowed(ActorClass.agent_runtime, "attest_invariants") is False
