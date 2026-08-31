"""Capability assertion vs verification (spec §9)."""

from __future__ import annotations

import json
from enum import Enum
from pathlib import Path
from typing import Any

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


class CapabilityStatus(str, Enum):
    VERIFIED = "VERIFIED"
    REFUTED = "REFUTED"
    ASSERTED_UNVERIFIED = "ASSERTED_UNVERIFIED"


def _load(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {"assertions": []}
    return json.loads(path.read_text(encoding="utf-8"))


def verify_folder(folder: Path) -> dict[str, Any]:
    spec = json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))
    provider = (spec.get("model_policy") or {}).get("provider")
    assertions = _load(folder / "protocols" / "capability_assertions.json").get("assertions") or []
    matrix: list[dict[str, Any]] = []
    if provider == "local_deterministic":
        matrix.append(
            {
                "capability": "model.local_deterministic",
                "status": CapabilityStatus.VERIFIED.value,
            }
        )
    for assertion in assertions:
        name = str(assertion.get("capability") or assertion.get("id") or "unknown")
        claimed = assertion.get("status")
        if provider == "local_deterministic" and name.startswith("model."):
            status = CapabilityStatus.VERIFIED
        elif claimed == "refute" or assertion.get("refute"):
            status = CapabilityStatus.REFUTED
        else:
            status = CapabilityStatus.ASSERTED_UNVERIFIED
        matrix.append({"capability": name, "status": status.value, "assertion": assertion})
    if not matrix:
        matrix.append(
            {
                "capability": "undeclared",
                "status": CapabilityStatus.ASSERTED_UNVERIFIED.value,
            }
        )
    return {
        "agent_id": spec.get("agent_id"),
        "matrix": matrix,
        "production_bindable": all(
            item["status"] == CapabilityStatus.VERIFIED.value for item in matrix
        ),
    }


def require_verified_for_production(matrix: dict[str, Any]) -> None:
    if not matrix.get("production_bindable"):
        raise CasopsError(ErrorCode.CMP_ASSERTED_UNVERIFIED)
