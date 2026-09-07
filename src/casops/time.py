"""Hong Kong civil time (UTC+8, no DST) for operator-facing timestamps."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

HKT = timezone(timedelta(hours=8), name="HKT")


def as_hkt(value: datetime | None = None) -> datetime:
    clock = value or datetime.now(timezone.utc)
    if clock.tzinfo is None:
        clock = clock.replace(tzinfo=timezone.utc)
    return clock.astimezone(HKT)


def now_hkt() -> datetime:
    return datetime.now(HKT)


def isoformat_hkt(value: datetime | None = None) -> str:
    return as_hkt(value).isoformat()


def stamp_hkt(value: datetime | None = None) -> str:
    return as_hkt(value).strftime("%Y-%m-%d-%H-%M-%S")
