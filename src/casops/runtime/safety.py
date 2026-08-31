"""Mandatory non-bypassable safety gate."""

from __future__ import annotations

from typing import Any

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.safety.taint import Taint


def safety_gate(*, output: dict[str, Any], policy: dict[str, Any], cancelled: bool) -> dict[str, Any]:
    if cancelled:
        raise CasopsError(ErrorCode.SAF_TERMINATION, detail="cancellation honoured at node boundary")
    if output.get("export_cot"):
        raise CasopsError(ErrorCode.OBS_COT_EXPORT)
    if policy.get("kill_switch_bypass"):
        raise CasopsError(ErrorCode.IMP_CORRIGIBILITY, detail="mandatory safety has no bypass")
    taint = Taint(frozenset(output.get("taint") or []))
    return {"passed": True, "taint": sorted(taint.labels), "policy": "enforced"}
