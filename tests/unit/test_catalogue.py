"""Error catalogue contract from spec §20 and implementation_plan.md §11.3."""

from __future__ import annotations

from pathlib import Path

import pytest

from casops.errors.catalogue import CATALOGUE_FIELDS, load_catalogue, spec_codes

REPO = Path(__file__).resolve().parents[2]


def test_every_spec_section_20_code_is_catalogued() -> None:
    catalogue = load_catalogue()
    present = {entry["code"] for entry in catalogue["codes"]}
    missing = spec_codes() - present
    assert missing == set(), f"catalogue missing spec §20 codes: {sorted(missing)}"


def test_catalogue_does_not_invent_codes() -> None:
    catalogue = load_catalogue()
    extra = {entry["code"] for entry in catalogue["codes"]} - spec_codes()
    assert extra == set(), f"catalogue has codes not in spec §20: {sorted(extra)}"


def test_every_entry_has_twelve_field_contract() -> None:
    catalogue = load_catalogue()
    assert catalogue["codes"], "catalogue is empty"
    for entry in catalogue["codes"]:
        missing = [field for field in CATALOGUE_FIELDS if field not in entry]
        assert missing == [], f"{entry.get('code')} missing fields {missing}"
        for field in CATALOGUE_FIELDS:
            assert entry[field] not in (None, ""), f"{entry['code']}.{field} is empty"


def test_codes_are_unique() -> None:
    codes = [entry["code"] for entry in load_catalogue()["codes"]]
    assert len(codes) == len(set(codes))


def test_containment_stop_actions_require_containment_flag() -> None:
    for entry in load_catalogue()["codes"]:
        if "containment stop" in str(entry["default_action"]).lower():
            assert entry["containment_required"] is True, entry["code"]


def test_generated_error_enum_matches_catalogue() -> None:
    from casops.errors.codes import ErrorCode

    catalogue_codes = {entry["code"] for entry in load_catalogue()["codes"]}
    enum_codes = {member.value for member in ErrorCode}
    assert enum_codes == catalogue_codes


def test_catalogue_file_is_the_committed_source() -> None:
    path = REPO / "errors" / "catalogue.json"
    assert path.is_file(), "errors/catalogue.json must exist as the source of truth"


@pytest.mark.parametrize("field", CATALOGUE_FIELDS)
def test_contract_field_name_is_stable(field: str) -> None:
    assert field in CATALOGUE_FIELDS
