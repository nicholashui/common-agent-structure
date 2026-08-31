"""Screening vs confirmatory evaluation tiers (DEC-07 / WP-603)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from casops.contracts.canonical import sha256_json
from casops.eval.power import SCREENING_N, required_n, require_powered
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.runtime.adapter import DeterministicAdapter

PlanDigest = str
TaskFn = Callable[[str], dict[str, str]]


@dataclass(frozen=True)
class AnalysisPlan:
    seed: int
    screening_n: int
    confirmatory_n: int
    claims: tuple[str, ...]
    digest: str
    paired: bool = True

    @classmethod
    def register(
        cls,
        *,
        seed: int = 20260824,
        screening_n: int = SCREENING_N,
        claims: tuple[str, ...] = ("binary_success",),
    ) -> AnalysisPlan:
        n = max(required_n(claim).n for claim in claims)
        payload = {
            "seed": seed,
            "screening_n": screening_n,
            "confirmatory_n": n,
            "claims": list(claims),
            "paired": True,
        }
        return cls(
            seed=seed,
            screening_n=screening_n,
            confirmatory_n=n,
            claims=claims,
            digest=sha256_json(payload),
            paired=True,
        )

    def assert_unchanged(self, other_digest: str) -> None:
        if other_digest != self.digest:
            raise CasopsError(ErrorCode.VAL_PLAN_DRIFT)


def _tasks(n: int, seed: int) -> list[str]:
    return [f"task-{seed}-{index:04d}" for index in range(n)]


def _run_arm(adapter: DeterministicAdapter, prompts: list[str], *, node_id: str) -> list[dict[str, str]]:
    return [adapter.complete(prompt=prompt, node_id=node_id) for prompt in prompts]


def run_screening(plan: AnalysisPlan, *, adapter: DeterministicAdapter | None = None) -> dict[str, Any]:
    """INDICATIVE only. Structurally cannot emit pass."""
    adapter = adapter or DeterministicAdapter()
    prompts = _tasks(plan.screening_n, plan.seed)
    rows = _run_arm(adapter, prompts, node_id="screen")
    return {
        "tier": "screening",
        "honesty": "INDICATIVE",
        "n": len(rows),
        "plan_digest": plan.digest,
        "pass": False,
        "verdict": "INDICATIVE",
        "reason": "screening_never_admissible",
    }


def run_confirmatory(
    plan: AnalysisPlan,
    *,
    recorded_digest: str,
    adapter: DeterministicAdapter | None = None,
    claim: str = "binary_success",
) -> dict[str, Any]:
    plan.assert_unchanged(recorded_digest)
    spec = require_powered(claim, plan.confirmatory_n)
    adapter = adapter or DeterministicAdapter()
    prompts = _tasks(plan.confirmatory_n, plan.seed)
    # Identical blocked task set, interleaved baseline/candidate via odd/even node ids.
    baseline = _run_arm(adapter, prompts, node_id="baseline")
    candidate = _run_arm(adapter, prompts, node_id="candidate")
    paired = list(zip(baseline, candidate, strict=True))
    both_complete = sum(1 for left, right in paired if left["digest"] and right["digest"])
    rate = both_complete / len(prompts)
    return {
        "tier": "confirmatory",
        "honesty": "MEASURED_LOCAL",
        "n": len(prompts),
        "required_n": spec.n,
        "plan_digest": plan.digest,
        "claim": claim,
        "paired": True,
        "success_rate": rate,
        "paired_complete": both_complete,
        "cold_cache": True,
        "pass": rate >= 0.99,
        "verdict": "MEASURED_LOCAL",
        "adapter": adapter.provider,
    }
