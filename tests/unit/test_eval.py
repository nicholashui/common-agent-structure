"""casops-eval refuses pass while instruments are UNQUALIFIED."""

from __future__ import annotations

from casops.eval.harness import evaluate, main
from casops.instruments.registry import InstrumentRegistry


def test_eval_does_not_pass_when_unqualified() -> None:
    report = evaluate(InstrumentRegistry(), agent_id="casops.template.baseline_safe")
    assert report["pass"] is False
    assert report["verdict"] == "NOT_RUN"
    assert "INS-01" in report["instruments"]


def test_eval_screening_never_passes() -> None:
    report = evaluate(InstrumentRegistry(), tier="screening")
    # Unqualified instruments still dominate.
    assert report["pass"] is False


def test_main_exits_nonzero() -> None:
    assert main([]) == 2
