"""Operator timestamps are Hong Kong civil time (UTC+8)."""

from __future__ import annotations

from datetime import datetime, timezone

from casops.time import HKT, isoformat_hkt, stamp_hkt


def test_isoformat_hkt_converts_utc() -> None:
    utc = datetime(2026, 9, 7, 0, 0, 0, tzinfo=timezone.utc)
    assert isoformat_hkt(utc) == "2026-09-07T08:00:00+08:00"


def test_stamp_hkt_uses_offset_clock() -> None:
    utc = datetime(2026, 9, 7, 16, 5, 9, tzinfo=timezone.utc)
    assert stamp_hkt(utc) == "2026-09-08-00-05-09"


def test_naive_datetime_treated_as_utc() -> None:
    naive = datetime(2026, 9, 7, 0, 0, 0)
    assert isoformat_hkt(naive).endswith("+08:00")
    assert isoformat_hkt(naive).startswith("2026-09-07T08:00:00")


def test_hkt_zone_name() -> None:
    assert HKT.tzname(None) == "HKT"


def test_isoformat_hkt_now_ends_with_offset() -> None:
    assert isoformat_hkt().endswith("+08:00")
