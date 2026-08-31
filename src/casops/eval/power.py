"""Prospective power and sample-size floors from spec §21.4.3."""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

FLOORS = {
    "p50_latency": 300,
    "p95_latency": 300,
    "p99_latency": 1000,
    "binary_success": 400,
    "cpst": 300,
    "memory_rate": 400,
    "t3_false_reuse": 598,
}

SCREENING_N = 120
DEFAULT_ALPHA = 0.05
DEFAULT_POWER = 0.80
SAFETY_POWER = 0.90


@dataclass(frozen=True)
class SampleSize:
    claim: str
    floor: int
    powered: int
    n: int
    alpha: float
    power: float
    method: str


def paired_binary_n(*, p_discordant: float = 0.10, alpha: float = DEFAULT_ALPHA, power: float = DEFAULT_POWER) -> int:
    """Normal approximation for McNemar discordance count, converted to pairs.

    Uses z_alpha≈1.645 (one-sided 0.05) and z_power≈0.84 (80%) unless safety power.
    """
    z_a = 1.64485 if abs(alpha - 0.05) < 1e-9 else 1.95996
    z_b = 0.84162 if abs(power - 0.80) < 1e-9 else 1.28155
    p = min(max(p_discordant, 0.01), 0.5)
    # Conservative n for detecting a 5pp paired difference with given discordance.
    delta = 0.05
    n = ((z_a + z_b) ** 2 * p * (1 - p)) / (delta**2)
    return max(1, int(ceil(n)))


def required_n(claim: str, *, powered: int | None = None) -> SampleSize:
    floor = FLOORS.get(claim, 400)
    computed = powered if powered is not None else paired_binary_n()
    n = max(floor, computed)
    power = SAFETY_POWER if claim in {"memory_rate", "t3_false_reuse"} else DEFAULT_POWER
    return SampleSize(
        claim=claim,
        floor=floor,
        powered=computed,
        n=n,
        alpha=DEFAULT_ALPHA,
        power=power,
        method="paired_binary_normal_approx+floor",
    )


def require_powered(claim: str, observed_n: int) -> SampleSize:
    spec = required_n(claim)
    if observed_n < spec.n:
        raise CasopsError(
            ErrorCode.IMP_STAT_UNDERPOWERED,
            detail=f"{claim} n={observed_n} < required {spec.n}",
        )
    return spec
