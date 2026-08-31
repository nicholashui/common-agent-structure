"""Screening cannot pass; confirmatory is powered, paired, and plan-frozen."""

from __future__ import annotations

import pytest

from casops.eval.confirmatory import AnalysisPlan, run_confirmatory, run_screening
from casops.eval.harness import evaluate
from casops.eval.power import required_n
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.instruments.registry import InstrumentRegistry, QualificationStatus
from casops.auth.actors import ActorClass


def test_screening_is_indicative_and_cannot_pass() -> None:
    plan = AnalysisPlan.register()
    report = run_screening(plan)
    assert report["honesty"] == "INDICATIVE"
    assert report["pass"] is False
    assert report["n"] == plan.screening_n


def test_confirmatory_uses_powered_n_and_rejects_plan_drift() -> None:
    plan = AnalysisPlan.register(claims=("binary_success",))
    assert plan.confirmatory_n >= required_n("binary_success").n
    measured = run_confirmatory(plan, recorded_digest=plan.digest)
    assert measured["tier"] == "confirmatory"
    assert measured["n"] == plan.confirmatory_n
    assert measured["honesty"] == "MEASURED_LOCAL"
    assert measured["pass"] is True
    with pytest.raises(CasopsError) as raised:
        run_confirmatory(plan, recorded_digest="0" * 64)
    assert raised.value.code == ErrorCode.VAL_PLAN_DRIFT


def test_eval_blocks_unqualified_even_if_confirmatory_would_pass() -> None:
    plan = AnalysisPlan.register()
    measured = run_confirmatory(plan, recorded_digest=plan.digest)
    report = evaluate(InstrumentRegistry(), confirmatory=measured, tier="confirmatory")
    assert report["pass"] is False
    assert report["verdict"] == "NOT_RUN"


def test_eval_confirmatory_pass_requires_qualified_instruments() -> None:
    registry = InstrumentRegistry()
    for ins_id in tuple(registry._records):
        registry.append_record(actor=ActorClass.host_service, ins_id=ins_id, status=QualificationStatus.QUALIFIED)
    plan = AnalysisPlan.register()
    measured = run_confirmatory(plan, recorded_digest=plan.digest)
    report = evaluate(registry, confirmatory=measured, tier="confirmatory")
    assert report["pass"] is True
    assert report["verdict"] == "MEASURED_LOCAL"
