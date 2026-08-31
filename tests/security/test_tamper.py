"""WP-116: tamper of invariants, approvals, fixtures, gates, telemetry containment-stops."""

from __future__ import annotations

import pytest

from casops.corrigibility.tamper import TamperSurface, detect_tamper
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


@pytest.mark.parametrize(
    "surface",
    [
        TamperSurface.invariant_file,
        TamperSurface.approval,
        TamperSurface.fixture,
        TamperSurface.gate,
        TamperSurface.telemetry_setting,
    ],
)
def test_tamper_containment_stops(surface: TamperSurface) -> None:
    with pytest.raises(CasopsError) as raised:
        detect_tamper(surface)
    assert raised.value.containment_required is True
    assert raised.value.code in {ErrorCode.IMP_CORRIGIBILITY, ErrorCode.SAF_TAINT}
