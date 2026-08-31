"""Load the 12-field error catalogue (implementation_plan.md §11.3)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from casops.errors.spec_rows import SPEC_ROWS

CATALOGUE_FIELDS: tuple[str, ...] = (
    "code",
    "category",
    "severity",
    "retryability",
    "default_action",
    "containment_required",
    "incident_required",
    "operator_message",
    "external_message",
    "http_mapping",
    "telemetry_event",
    "test_fixture",
)

_REPO_ROOT = Path(__file__).resolve().parents[3]
CATALOGUE_PATH = _REPO_ROOT / "errors" / "catalogue.json"


def spec_codes() -> set[str]:
    return {row[0] for row in SPEC_ROWS}


def _http_mapping(default_action: str) -> int:
    action = default_action.lower()
    if "containment stop" in action or "halt" in action:
        return 503
    if "cancel with bounded failure" in action:
        return 504
    if "fail deletion sla" in action:
        return 500
    if action.startswith("block") or "kill plugin" in action:
        return 403
    if "reject or split" in action:
        return 400
    if "abort load" in action:
        return 400
    return 409


def _severity(code: str, default_action: str, category: str) -> str:
    action = default_action.lower()
    if "containment stop" in action or category in {"safety", "corrigibility", "gate"}:
        return "critical"
    if code.startswith(("IMP_", "OBS_", "PLG_HANDLE", "MEM_POISON", "CIT_")):
        return "high"
    if category in {"cache"} or "disable" in action:
        return "medium"
    return "high"


def _retryability(default_action: str) -> str:
    if default_action == "Cancel with bounded failure":
        return "not_idempotent_retry"
    return "never"


def _containment_required(default_action: str) -> bool:
    action = default_action.lower()
    return "containment stop" in action or action in {"halt exchange graph", "escalate or stop"}


def _incident_required(code: str, default_action: str) -> bool:
    action = default_action.lower()
    if "incident" in action:
        return True
    return code in {
        "IMP_SELF_APPROVAL",
        "IMP_CORRIGIBILITY",
        "OBS_COT_EXPORT",
        "PLG_HANDLE_FORGERY",
        "SAF_INJECTION",
        "GATE_ACTIVATION",
        "MEM_POISON",
    }


def build_entries() -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for code, category, condition, default_action in SPEC_ROWS:
        entries.append(
            {
                "code": code,
                "category": category,
                "severity": _severity(code, default_action, category),
                "retryability": _retryability(default_action),
                "default_action": default_action,
                "containment_required": _containment_required(default_action),
                "incident_required": _incident_required(code, default_action),
                "operator_message": f"{code}: {condition}. Default action: {default_action}.",
                "external_message": "The request was rejected by host policy.",
                "http_mapping": _http_mapping(default_action),
                "telemetry_event": f"casops.error.{code.lower()}",
                "test_fixture": f"tests/contract/errors/test_{code.lower()}.py",
            }
        )
    return entries


def catalogue_document() -> dict[str, Any]:
    return {
        "schema_version": "3.0",
        "source_section": "20",
        "field_contract": list(CATALOGUE_FIELDS),
        "codes": build_entries(),
    }


def load_catalogue() -> dict[str, Any]:
    if not CATALOGUE_PATH.is_file():
        raise FileNotFoundError(f"missing catalogue at {CATALOGUE_PATH}")
    return json.loads(CATALOGUE_PATH.read_text(encoding="utf-8"))
