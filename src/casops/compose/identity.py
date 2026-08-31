"""Identity and disclosure checks (spec §16.2)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


def _load(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def validate_identity(folder: Path) -> None:
    persona = _load(folder / "identity" / "persona.json")
    background = _load(folder / "identity" / "background.json")
    mode = persona.get("mode", "grounded")
    if mode != "grounded" and not (folder / "identity" / "DISCLOSURE.md").is_file():
        raise CasopsError(ErrorCode.IDN_DISCLOSURE_MISSING)
    if persona.get("named_person") and not persona.get("approval_id"):
        raise CasopsError(ErrorCode.IDN_NAMED_PERSON)
    if persona.get("claims_real_license") or background.get("claims_real_license"):
        raise CasopsError(ErrorCode.IDN_LICENSE_CLAIM)
