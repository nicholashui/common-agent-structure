"""Typed CASOPS errors bound to the catalogue."""

from __future__ import annotations

from casops.errors.catalogue import load_catalogue
from casops.errors.codes import ErrorCode


def _entry(code: ErrorCode | str) -> dict:
    value = code.value if isinstance(code, ErrorCode) else code
    for item in load_catalogue()["codes"]:
        if item["code"] == value:
            return item
    raise KeyError(value)


class CasopsError(Exception):
    def __init__(
        self,
        code: ErrorCode,
        *,
        invariant_id: str | None = None,
        degraded_mode: bool = False,
        detail: str | None = None,
    ) -> None:
        entry = _entry(code)
        self.code = code
        self.invariant_id = invariant_id
        self.degraded_mode = False if entry["containment_required"] else degraded_mode
        self.containment_required = bool(entry["containment_required"])
        self.http_mapping = int(entry["http_mapping"])
        self.operator_message = detail or entry["operator_message"]
        self.external_message = entry["external_message"]
        super().__init__(self.operator_message)
