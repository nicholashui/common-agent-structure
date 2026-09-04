#!/usr/bin/env python3
"""Render reports/latest.json → run_status.md (human-readable tables)."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "reports" / "latest.json"
OUT = ROOT / "run_status.md"


def agent_status(v: dict) -> str:
    """PASS only when no product fails (rate-limit skips allowed)."""
    failed = int(v.get("failed") or 0)
    passed = int(v.get("passed") or 0)
    skipped = int(v.get("skipped_rate_limit") or 0)
    if failed == 0 and passed > 0:
        return "PASS"
    if failed == 0 and passed == 0 and skipped > 0:
        return "SKIP_429"
    if passed == 0 and failed > 0:
        return "FAIL"
    if failed > 0 and (passed > 0 or skipped > 0):
        return "PARTIAL"
    return "PARTIAL"


def kind_stats(m: dict) -> tuple[int, int, int, int]:
    p = sum(1 for v in m.values() if agent_status(v) == "PASS")
    f = sum(1 for v in m.values() if agent_status(v) == "FAIL")
    t = sum(1 for v in m.values() if agent_status(v) == "PARTIAL")
    return len(m), p, f, t


def bucket_reason(msg: str) -> str:
    if not msg:
        return "unknown"
    if "http_status" in msg:
        return "http_status mismatch"
    if "required_keys" in msg:
        return "required_keys_any missing"
    if "json_equals" in msg:
        return "json_equals mismatch"
    if "exception" in msg.lower() or "unhandled" in msg.lower():
        return "exception"
    return msg.split(":")[0][:80]


def main() -> None:
    if not SRC.is_file():
        raise SystemExit(f"Missing report: {SRC}")
    d = json.loads(SRC.read_text(encoding="utf-8"))
    s = d.get("summary") or {}
    agents: dict = d.get("agents") or {}
    failed_cases: list = d.get("failed_cases") or []
    # Prefer explicit product fails; fall back to non-pass cases without skip outcome
    if not failed_cases:
        for v in agents.values():
            for c in v.get("cases") or []:
                if c.get("outcome") == "fail" or (
                    not c.get("passed") and c.get("outcome") not in ("skipped_rate_limit", "pass")
                ):
                    if c.get("outcome") != "skipped_rate_limit":
                        failed_cases.append(c)

    pack = {k: v for k, v in agents.items() if k.startswith("video.")}
    specials = {k: v for k, v in agents.items() if k.startswith("specials.")}

    status_ctr: Counter[int | str] = Counter()
    fail_reason_ctr: Counter[str] = Counter()
    for fc in failed_cases:
        if fc.get("outcome") == "skipped_rate_limit":
            continue
        status_ctr[fc.get("http_status")] += 1
        fails = fc.get("failures") or []
        fail_reason_ctr[bucket_reason(fails[0] if fails else "")] += 1

    full_pass = sum(1 for v in agents.values() if agent_status(v) == "PASS")
    full_fail = sum(1 for v in agents.values() if agent_status(v) == "FAIL")
    partial = sum(1 for v in agents.values() if agent_status(v) == "PARTIAL")
    skip_only = sum(1 for v in agents.values() if agent_status(v) == "SKIP_429")
    pr = float(s.get("pass_rate") or 0)
    pr_ex = float(s.get("pass_rate_excluding_rate_limit") or pr)
    skipped_rl = int(s.get("cases_skipped_rate_limit") or 0)
    # Also count skipped from agent buckets if summary missing
    if not skipped_rl:
        skipped_rl = sum(int(v.get("skipped_rate_limit") or 0) for v in agents.values())
    # Count SKIPPED outcomes from cases if present
    skip_from_cases = 0
    for v in agents.values():
        for c in v.get("cases") or []:
            if c.get("outcome") == "skipped_rate_limit" or c.get("http_status") == 429:
                # only count as skip if outcome says so (new reports)
                if c.get("outcome") == "skipped_rate_limit":
                    skip_from_cases += 1
    if skip_from_cases and not s.get("cases_skipped_rate_limit"):
        skipped_rl = skip_from_cases

    runner = d.get("runner") or {}

    lines: list[str] = []
    lines += [
        "# API test run status",
        "",
        "Source: `testcases/api_test/reports/latest.json`",
        "",
        "## Summary",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| **Started** | {d.get('started_at', '')} |",
        f"| **Finished** | {d.get('finished_at', '')} |",
        f"| **Host** | `{d.get('host', '')}` |",
        f"| **Auth** | {d.get('auth', '')} |",
        f"| **Minted key id** | `{d.get('minted_key_id') or '—'}` |",
        f"| **Agents** | {s.get('agents', 0)} |",
        f"| **Cases total** | {s.get('cases_total', 0)} |",
        f"| **Cases passed** | {s.get('cases_passed', 0)} |",
        f"| **Cases failed (product)** | {s.get('cases_failed', 0)} |",
        f"| **Cases skipped (429)** | {skipped_rl} |",
        f"| **Pass rate (all cases)** | {pr:.1%} |",
        f"| **Pass rate (excl. 429 skip)** | {pr_ex:.1%} |",
        "",
        "## Runner settings (if present)",
        "",
        "| Setting | Value |",
        "|---------|-------|",
        f"| sleep | {runner.get('sleep', '—')} |",
        f"| max_429_retries | {runner.get('max_429_retries', '—')} |",
        f"| batch_size / batch_pause | {runner.get('batch_size', '—')} / {runner.get('batch_pause', '—')} |",
        f"| rate_limit_as_skip | {runner.get('rate_limit_as_skip', '—')} |",
        "",
        "## Agent rollup",
        "",
        "| Status | Meaning | Count |",
        "|--------|---------|------:|",
        f"| **PASS** | No product fails (skips OK) | {full_pass} |",
        f"| **PARTIAL** | Mix of pass/fail/skip | {partial} |",
        f"| **FAIL** | Only product fails | {full_fail} |",
        f"| **SKIP_429** | Only rate-limit skips | {skip_only} |",
        f"| **Total agents** | | {len(agents)} |",
        "",
        "## By kind",
        "",
        "| Kind | Agents | Full PASS | Full FAIL | PARTIAL |",
        "|------|-------:|----------:|----------:|--------:|",
    ]
    n, p, f, t = kind_stats(pack)
    lines.append(f"| Pack (`video.*`) | {n} | {p} | {f} | {t} |")
    n, p, f, t = kind_stats(specials)
    lines.append(f"| Specials (`specials.*`) | {n} | {p} | {f} | {t} |")
    lines += [
        "",
        "## Failure HTTP status breakdown (product FAIL only)",
        "",
        "| HTTP status | Failed cases |",
        "|------------:|-------------:|",
    ]
    for code, cnt in sorted(status_ctr.items(), key=lambda x: (-x[1], str(x[0]))):
        lines.append(f"| {code} | {cnt} |")

    lines += [
        "",
        "## Failure reason buckets (product FAIL only)",
        "",
        "| Reason | Count |",
        "|--------|------:|",
    ]
    for reason, cnt in fail_reason_ctr.most_common(20):
        lines.append(f"| {reason} | {cnt} |")

    lines += [
        "",
        "## All agents (pass / fail / skip counts)",
        "",
        "| Agent id | Kind | Passed | Failed | Skip 429 | Status |",
        "|----------|------|-------:|-------:|---------:|--------|",
    ]
    for aid in sorted(agents.keys()):
        v = agents[aid]
        if aid.startswith("video."):
            kind = "pack"
        elif aid.startswith("specials."):
            kind = "special"
        else:
            kind = "other"
        st = agent_status(v)
        lines.append(
            f"| `{aid}` | {kind} | {v.get('passed', 0)} | {v.get('failed', 0)} | "
            f"{v.get('skipped_rate_limit', 0)} | **{st}** |"
        )

    lines += [
        "",
        "## Specials — case detail",
        "",
        "| Agent | Case | Name | HTTP | Result | Duration (ms) |",
        "|-------|------|------|-----:|--------|--------------:|",
    ]
    for aid in sorted(specials.keys()):
        for c in specials[aid].get("cases") or []:
            outcome = c.get("outcome")
            if outcome == "pass" or (outcome is None and c.get("passed")):
                res = "PASS"
            elif outcome == "skipped_rate_limit":
                res = "SKIP_429"
            else:
                res = "FAIL"
            lines.append(
                f"| `{aid}` | {c.get('case_id')} | {c.get('name', '')} | "
                f"{c.get('http_status')} | **{res}** | {c.get('duration_ms', 0)} |"
            )

    lines += [
        "",
        "## Failed cases (all)",
        "",
        "| Agent | Case | Name | HTTP | Failures |",
        "|-------|------|------|-----:|----------|",
    ]
    for c in failed_cases:
        fails = "; ".join(c.get("failures") or []).replace("|", "\\|")
        if len(fails) > 140:
            fails = fails[:137] + "..."
        lines.append(
            f"| `{c.get('agent_id')}` | {c.get('case_id')} | {c.get('name', '')} | "
            f"{c.get('http_status')} | {fails} |"
        )

    lines += [
        "",
        "## How to re-run",
        "",
        "```powershell",
        "cd C:\\Project\\common-agent-swarm-ops\\testcases\\api_test",
        "python run_all_api_tests.py --host http://127.0.0.1:8000 --mint",
        "python render_run_status.py",
        "```",
        "",
        "---",
        "",
        "*Generated from `reports/latest.json` by `render_run_status.py`.*",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes, {len(lines)} lines)")


if __name__ == "__main__":
    main()
