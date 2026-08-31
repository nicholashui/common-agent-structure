"""Tamper detection on host-owned surfaces (WP-116)."""

from __future__ import annotations

from enum import Enum

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


class TamperSurface(str, Enum):
    invariant_file = "invariant_file"
    approval = "approval"
    fixture = "fixture"
    gate = "gate"
    telemetry_setting = "telemetry_setting"


def detect_tamper(surface: TamperSurface) -> None:
    raise CasopsError(
        ErrorCode.IMP_CORRIGIBILITY,
        detail=f"tamper detected on {surface.value}",
    )
