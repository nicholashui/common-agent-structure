"""Negative-fixture enforcement for INV-01..INV-12."""

from __future__ import annotations

from casops.auth.actors import ActorClass, is_allowed
from casops.corrigibility.invariants import ACTION_TO_INVARIANT
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


def attempt_forbidden(*, actor: ActorClass, action: str) -> None:
    invariant_id = ACTION_TO_INVARIANT[action]
    if not is_allowed(actor, action):
        raise CasopsError(ErrorCode.IMP_CORRIGIBILITY, invariant_id=invariant_id)
    raise CasopsError(
        ErrorCode.IMP_CORRIGIBILITY,
        invariant_id=invariant_id,
        detail=f"{action} is forbidden even when the actor matrix is misconfigured",
    )
