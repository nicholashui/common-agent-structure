"""casops-eval: screening vs confirmatory; cannot pass while instruments are UNQUALIFIED (IQ-01)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from casops.citation.audit import load_audit
from casops.eval.confirmatory import AnalysisPlan, run_confirmatory, run_screening
from casops.instruments.registry import INSTRUMENT_IDS, InstrumentRegistry, QualificationStatus
from casops.runtime.adapter import DeterministicAdapter


def evaluate(
    registry: InstrumentRegistry,
    *,
    agent_id: str = "",
    citation: dict[str, Any] | None = None,
    confirmatory: dict[str, Any] | None = None,
    tier: str = "default",
) -> dict[str, Any]:
    blocking = [
        ins_id
        for ins_id in INSTRUMENT_IDS
        if registry.get(ins_id).status is not QualificationStatus.QUALIFIED
    ]
    if blocking:
        return {
            "agent_id": agent_id,
            "tier": tier,
            "verdict": "NOT_RUN",
            "reason": "unqualified_instruments",
            "instruments": blocking,
            "pass": False,
        }
    if citation is not None and not citation.get("cleared"):
        return {
            "agent_id": agent_id,
            "tier": tier,
            "verdict": "BLOCKED",
            "reason": "CIT_UNVERIFIED",
            "blocking": citation.get("blocking") or [],
            "pass": False,
        }
    if tier == "screening":
        return {
            "agent_id": agent_id,
            "tier": "screening",
            "verdict": "INDICATIVE",
            "honesty": "INDICATIVE",
            "reason": "screening_never_admissible",
            "pass": False,
        }
    if confirmatory is None:
        return {
            "agent_id": agent_id,
            "tier": tier,
            "verdict": "NOT_RUN",
            "reason": "confirmatory_not_run",
            "pass": False,
        }
    report = dict(confirmatory)
    report["agent_id"] = agent_id
    report["pass"] = bool(confirmatory.get("pass"))
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="casops-eval")
    parser.add_argument("command", nargs="?", default="status")
    parser.add_argument("--tier", choices=("screening", "confirmatory"), default=None)
    parser.add_argument("--agent", default="")
    parser.add_argument("--citation", type=Path, default=None)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args(argv)
    registry = InstrumentRegistry()
    citation = load_audit(args.citation) if args.citation and args.citation.is_file() else None
    confirmatory = None
    if args.command == "run" and args.tier == "screening":
        confirmatory = None
        report = evaluate(registry, agent_id=args.agent, citation=citation, tier="screening")
        plan = AnalysisPlan.register()
        report.update(run_screening(plan))
        report["pass"] = False
    elif args.command == "run" and args.tier == "confirmatory":
        plan = AnalysisPlan.register()
        measured = run_confirmatory(plan, recorded_digest=plan.digest, adapter=DeterministicAdapter())
        report = evaluate(
            registry,
            agent_id=args.agent,
            citation=citation,
            confirmatory=measured,
            tier="confirmatory",
        )
    else:
        report = evaluate(registry, agent_id=args.agent, citation=citation)
    text = json.dumps(report)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if report.get("pass") else 2
