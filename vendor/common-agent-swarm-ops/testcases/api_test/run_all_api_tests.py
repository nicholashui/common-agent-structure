#!/usr/bin/env python3
"""
Run all per-agent API test cases under testcases/api_test/<agent_id>/cases.json.

Auth:
  - Prefer CASOPS_API_KEY / --bearer casops_*
  - Or server CASOPS_DEV_TRUST=1 for session without Bearer
  - If Bearer is present it must be valid (invalid/revoked → 401)

Rate limits:
  - Retries HTTP 429 with Retry-After / exponential backoff
  - Default inter-case sleep to stay under Host /api/v1 window
  - After max retries, classify as SKIPPED_RATE_LIMIT (not FAIL) by default

Usage:
  python run_all_api_tests.py --host http://127.0.0.1:8000 --mint
  python run_all_api_tests.py --only video.planner
  python run_all_api_tests.py --sleep 0.5 --max-429-retries 5
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal

ROOT = Path(__file__).resolve().parent

Outcome = Literal["pass", "fail", "skipped_rate_limit"]


def unwrap(payload: Any) -> Any:
    if isinstance(payload, dict) and "data" in payload and "meta" in payload:
        return payload["data"]
    return payload


def deep_get(obj: Any, path: str) -> Any:
    cur = obj
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def is_rate_limited(status: int, body: Any) -> bool:
    if status == 429:
        return True
    if isinstance(body, dict):
        err = body.get("error")
        if isinstance(err, dict) and str(err.get("code") or "").lower() in {
            "rate_limited",
            "rate_limit",
        }:
            return True
        if str(body.get("code") or "").lower() == "rate_limited":
            return True
    return False


def http_json(
    host: str,
    method: str,
    path: str,
    *,
    body: dict[str, Any] | None = None,
    bearer: str | None = None,
    timeout: float = 180.0,
) -> tuple[int, Any, str, dict[str, str]]:
    """Return (status, parsed_body, raw, response_headers_lower)."""
    url = host.rstrip("/") + path
    data = None if body is None else json.dumps(body).encode("utf-8")
    headers = {"Accept": "application/json"}
    if body is not None and method.upper() != "GET":
        headers["Content-Type"] = "application/json"
    if bearer:
        headers["Authorization"] = f"Bearer {bearer}"
    req = urllib.request.Request(url, data=data, headers=headers, method=method.upper())
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            status = resp.getcode() or 200
            rh = {k.lower(): v for k, v in resp.headers.items()}
            try:
                parsed = unwrap(json.loads(raw)) if raw else {}
            except json.JSONDecodeError:
                parsed = {"_raw": raw}
            return status, parsed, raw, rh
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        rh = {k.lower(): v for k, v in (exc.headers.items() if exc.headers else [])}
        try:
            parsed = unwrap(json.loads(raw)) if raw else {"error": raw}
        except json.JSONDecodeError:
            parsed = {"_raw": raw}
        return exc.code, parsed, raw, rh
    except urllib.error.URLError as exc:
        return 0, {"error": str(exc.reason)}, str(exc), {}


def sleep_backoff(
    attempt: int,
    *,
    retry_after_header: str | None,
    base: float,
    cap: float,
) -> float:
    """Seconds to sleep before next try. Prefer Retry-After when present."""
    if retry_after_header:
        try:
            return min(cap, max(0.1, float(retry_after_header.strip())))
        except ValueError:
            pass
    # attempt 0 → base, then exponential
    return min(cap, base * (2**attempt))


def http_json_with_429_retry(
    host: str,
    method: str,
    path: str,
    *,
    body: dict[str, Any] | None = None,
    bearer: str | None = None,
    timeout: float = 180.0,
    max_retries: int = 5,
    backoff_base: float = 1.0,
    backoff_cap: float = 30.0,
) -> tuple[int, Any, str, int]:
    """
    Call API; retry on 429 up to max_retries extra attempts.
    Returns (status, body, raw, attempts_used).
    """
    attempts = 0
    last_status = 0
    last_body: Any = {}
    last_raw = ""
    while attempts <= max_retries:
        attempts += 1
        status, parsed, raw, rh = http_json(
            host, method, path, body=body, bearer=bearer, timeout=timeout
        )
        last_status, last_body, last_raw = status, parsed, raw
        if not is_rate_limited(status, parsed):
            return status, parsed, raw, attempts
        if attempts > max_retries:
            break
        wait = sleep_backoff(
            attempts - 1,
            retry_after_header=rh.get("retry-after"),
            base=backoff_base,
            cap=backoff_cap,
        )
        print(f"    429 rate_limited → sleep {wait:.1f}s (attempt {attempts}/{max_retries + 1})")
        time.sleep(wait)
    return last_status, last_body, last_raw, attempts


def mint_api_key(host: str) -> tuple[str, str]:
    status, data, _, _ = http_json(host, "GET", "/api/v1/developer/actions")
    if status != 200:
        raise SystemExit(f"Cannot GET /developer/actions (HTTP {status}). Set CASOPS_DEV_TRUST=1?")
    actions = data.get("actions") or []
    action = next((a for a in actions if a.get("kind") == "developer_token"), None)
    if not action:
        raise SystemExit("No developer_token action available")
    status, minted, _, _ = http_json(
        host,
        "POST",
        "/api/v1/developer/tokens",
        body={
            "action_reference_id": action["id"],
            "label": "api-test-suite",
            "scopes": ["agent.loop", "swarm:run", "registry.read", "control_plane:*"],
        },
    )
    if status not in (200, 201):
        raise SystemExit(f"Mint failed HTTP {status}: {minted}")
    raw = str(minted.get("value_shown_once") or "")
    key_id = str(minted.get("id") or "")
    if not raw.startswith("casops_") or raw == "[REDACTED]":
        raise SystemExit(f"Mint returned unusable key: {minted}")
    return key_id, raw


def evaluate_success(
    status: int,
    body: Any,
    criteria: dict[str, Any],
) -> tuple[bool, list[str]]:
    fails: list[str] = []
    allowed = criteria.get("http_status") or [200]
    if status not in allowed:
        fails.append(f"http_status={status} not in {allowed}")

    if not isinstance(body, dict):
        fails.append("body is not a JSON object")
        return False, fails

    for key, expected in (criteria.get("json_equals") or {}).items():
        if body.get(key) != expected:
            fails.append(f"json_equals {key}: got {body.get(key)!r} want {expected!r}")

    any_keys = criteria.get("required_keys_any") or []
    if any_keys and not any(k in body for k in any_keys):
        flat_ok = any(deep_get(body, k) is not None for k in any_keys)
        if not flat_ok:
            fails.append(
                f"missing all of required_keys_any={any_keys}; keys={list(body.keys())[:20]}"
            )

    for path, expected in (criteria.get("json_path_equals") or {}).items():
        got = deep_get(body, path)
        if got != expected:
            fails.append(f"json_path_equals {path}: got {got!r} want {expected!r}")

    if criteria.get("require_ok_true") and body.get("ok") is False:
        fails.append("ok is False")

    return (len(fails) == 0), fails


@dataclass
class CaseResult:
    agent_id: str
    case_id: str
    name: str
    method: str
    path: str
    passed: bool
    outcome: Outcome
    http_status: int
    duration_ms: float
    attempts: int = 1
    failures: list[str] = field(default_factory=list)
    response_summary: dict[str, Any] = field(default_factory=dict)


def load_agent_cases(agent_dir: Path) -> dict[str, Any] | None:
    cases_path = agent_dir / "cases.json"
    if not cases_path.is_file():
        return None
    return json.loads(cases_path.read_text(encoding="utf-8"))


def summarize_body(body: Any) -> dict[str, Any]:
    if not isinstance(body, dict):
        return {"type": type(body).__name__}
    keys = list(body.keys())[:24]
    out: dict[str, Any] = {"keys": keys}
    for k in ("agent_id", "ok", "status", "run_id", "primary_intent", "error"):
        if k in body:
            out[k] = body[k]
    if "v3" in body and isinstance(body["v3"], dict):
        out["has_v3"] = True
    return out


def run_case(
    host: str,
    agent_id: str,
    case: dict[str, Any],
    bearer: str | None,
    *,
    max_429_retries: int,
    backoff_base: float,
    backoff_cap: float,
    rate_limit_as_skip: bool,
) -> CaseResult:
    """Execute one case; never raises — errors become CaseResult outcomes."""
    method = str(case.get("method") or "POST").upper()
    path = str(case.get("path") or "")
    case_id = str(case.get("id") or "")
    name = str(case.get("name") or "")
    body = case.get("body")
    if method == "GET":
        body = None
    t0 = time.perf_counter()
    try:
        status, resp_body, _raw, attempts = http_json_with_429_retry(
            host,
            method,
            path,
            body=body if isinstance(body, dict) else None,
            bearer=bearer,
            max_retries=max_429_retries,
            backoff_base=backoff_base,
            backoff_cap=backoff_cap,
        )
        dt = (time.perf_counter() - t0) * 1000

        if is_rate_limited(status, resp_body) and rate_limit_as_skip:
            return CaseResult(
                agent_id=agent_id,
                case_id=case_id,
                name=name,
                method=method,
                path=path,
                passed=False,
                outcome="skipped_rate_limit",
                http_status=status,
                duration_ms=round(dt, 1),
                attempts=attempts,
                failures=[
                    f"rate_limited after {attempts} attempt(s); "
                    "not counted as product FAIL"
                ],
                response_summary=summarize_body(resp_body),
            )

        ok, fails = evaluate_success(status, resp_body, case.get("success_criteria") or {})
        return CaseResult(
            agent_id=agent_id,
            case_id=case_id,
            name=name,
            method=method,
            path=path,
            passed=ok,
            outcome="pass" if ok else "fail",
            http_status=status,
            duration_ms=round(dt, 1),
            attempts=attempts,
            failures=fails,
            response_summary=summarize_body(resp_body),
        )
    except Exception as exc:  # noqa: BLE001 — suite must continue
        dt = (time.perf_counter() - t0) * 1000
        return CaseResult(
            agent_id=agent_id,
            case_id=case_id or "unknown",
            name=name or "exception",
            method=method,
            path=path,
            passed=False,
            outcome="fail",
            http_status=0,
            duration_ms=round(dt, 1),
            attempts=1,
            failures=[f"exception: {type(exc).__name__}: {exc}"],
            response_summary={"error": str(exc)},
        )


def discover_agents(only: str | None, limit: int | None) -> list[Path]:
    dirs = sorted(
        [p for p in ROOT.iterdir() if p.is_dir() and (p / "cases.json").is_file()],
        key=lambda p: p.name,
    )
    if only:
        dirs = [p for p in dirs if p.name == only or p.name.startswith(only)]
    if limit is not None:
        dirs = dirs[: max(0, limit)]
    return dirs


def main() -> int:
    parser = argparse.ArgumentParser(description="Run all agent API test cases")
    parser.add_argument("--host", default=os.environ.get("HOST_BASE", "http://127.0.0.1:8000"))
    parser.add_argument("--bearer", default=os.environ.get("CASOPS_API_KEY"))
    parser.add_argument("--mint", action="store_true", help="Mint a casops_* key via session")
    parser.add_argument("--only", default=None, help="Only agent_id or prefix")
    parser.add_argument("--limit-agents", type=int, default=None)
    parser.add_argument(
        "--report",
        default=None,
        help="Write JSON report path (default: reports/run_<timestamp>.json)",
    )
    parser.add_argument(
        "--fail-fast",
        action="store_true",
        help="Optional: stop after first product FAIL (not rate-limit skip)",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=float(os.environ.get("API_TEST_SLEEP", "0.35")),
        help="Delay between cases in seconds (default: 0.35; set 0 to disable)",
    )
    parser.add_argument(
        "--max-429-retries",
        type=int,
        default=int(os.environ.get("API_TEST_MAX_429_RETRIES", "5")),
        help="Extra attempts after first 429 (default: 5 → up to 6 tries)",
    )
    parser.add_argument(
        "--backoff-base",
        type=float,
        default=1.0,
        help="Base seconds for exponential backoff when Retry-After missing",
    )
    parser.add_argument(
        "--backoff-cap",
        type=float,
        default=30.0,
        help="Max sleep seconds between 429 retries",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=int(os.environ.get("API_TEST_BATCH_SIZE", "80")),
        help="After this many cases, pause for --batch-pause (0=off)",
    )
    parser.add_argument(
        "--batch-pause",
        type=float,
        default=float(os.environ.get("API_TEST_BATCH_PAUSE", "5.0")),
        help="Seconds to pause after each batch (default: 5)",
    )
    parser.add_argument(
        "--rate-limit-is-fail",
        action="store_true",
        help="Count exhausted 429 as FAIL instead of SKIPPED_RATE_LIMIT",
    )
    args = parser.parse_args()
    rate_limit_as_skip = not args.rate_limit_is_fail

    # Ensure cases exist
    if not any(ROOT.glob("*/cases.json")):
        gen = ROOT / "generate_agent_api_tests.py"
        if gen.is_file():
            print("No cases found; running generate_agent_api_tests.py ...")
            import runpy

            try:
                runpy.run_path(str(gen), run_name="__main__")
            except Exception as exc:  # noqa: BLE001
                print(f"WARNING: generate failed ({exc}); continuing with what exists")

    bearer = args.bearer
    key_id = ""
    if args.mint or not bearer:
        print("Minting API key (session / CASOPS_DEV_TRUST on server)...")
        try:
            key_id, bearer = mint_api_key(args.host)
            print(f"  minted id={key_id} prefix={bearer[:14]}...")
        except SystemExit as exc:
            print(f"WARNING: mint failed ({exc}); continuing without Bearer if possible")
            bearer = args.bearer
        except Exception as exc:  # noqa: BLE001
            print(f"WARNING: mint error ({exc}); continuing without Bearer if possible")
            bearer = args.bearer

    agents = discover_agents(args.only, args.limit_agents)
    if not agents:
        print("No agent case folders found.", file=sys.stderr)
        return 2

    results: list[CaseResult] = []
    started = datetime.now(UTC).isoformat()
    print(f"Host={args.host} agents={len(agents)} started={started}")
    print(
        f"Policy: continue on error; sleep={args.sleep}s; "
        f"429 retries={args.max_429_retries}; "
        f"rate_limit→{'SKIP' if rate_limit_as_skip else 'FAIL'}; "
        f"batch={args.batch_size}/{args.batch_pause}s"
    )

    stop = False
    cases_since_batch = 0
    for agent_dir in agents:
        if stop:
            break
        try:
            payload = load_agent_cases(agent_dir)
        except Exception as exc:  # noqa: BLE001
            print(f"\n== {agent_dir.name} == load error → FAIL, continue")
            results.append(
                CaseResult(
                    agent_id=agent_dir.name,
                    case_id="load",
                    name="load cases.json",
                    method="N/A",
                    path=str(agent_dir / "cases.json"),
                    passed=False,
                    outcome="fail",
                    http_status=0,
                    duration_ms=0.0,
                    failures=[f"load_error: {exc}"],
                    response_summary={},
                )
            )
            continue
        if not payload:
            continue
        agent_id = str(payload.get("agent_id") or agent_dir.name)
        cases = payload.get("cases") or []
        print(f"\n== {agent_id} ({len(cases)} cases) ==")
        for case in cases:
            try:
                cr = run_case(
                    args.host,
                    agent_id,
                    case,
                    bearer,
                    max_429_retries=max(0, args.max_429_retries),
                    backoff_base=max(0.1, args.backoff_base),
                    backoff_cap=max(0.5, args.backoff_cap),
                    rate_limit_as_skip=rate_limit_as_skip,
                )
            except Exception as exc:  # noqa: BLE001
                cr = CaseResult(
                    agent_id=agent_id,
                    case_id=str(case.get("id") or "unknown"),
                    name=str(case.get("name") or "exception"),
                    method=str(case.get("method") or "?"),
                    path=str(case.get("path") or ""),
                    passed=False,
                    outcome="fail",
                    http_status=0,
                    duration_ms=0.0,
                    failures=[f"unhandled: {type(exc).__name__}: {exc}"],
                    response_summary={},
                )
            results.append(cr)
            mark = {
                "pass": "PASS",
                "fail": "FAIL",
                "skipped_rate_limit": "SKIP_429",
            }.get(cr.outcome, cr.outcome.upper())
            print(
                f"  [{mark}] {cr.case_id} HTTP {cr.http_status} "
                f"{cr.duration_ms}ms tries={cr.attempts} {cr.name}"
            )
            if cr.outcome != "pass":
                for f in cr.failures:
                    print(f"         - {f}")
            if args.fail_fast and cr.outcome == "fail":
                print("  --fail-fast: stopping after product FAIL")
                stop = True
                break

            cases_since_batch += 1
            if args.sleep > 0:
                try:
                    time.sleep(args.sleep)
                except Exception:
                    pass
            if (
                args.batch_size > 0
                and args.batch_pause > 0
                and cases_since_batch >= args.batch_size
            ):
                print(
                    f"  -- batch pause {args.batch_pause}s "
                    f"after {cases_since_batch} cases --"
                )
                try:
                    time.sleep(args.batch_pause)
                except Exception:
                    pass
                cases_since_batch = 0

    passed = sum(1 for r in results if r.outcome == "pass")
    failed = sum(1 for r in results if r.outcome == "fail")
    skipped_rl = sum(1 for r in results if r.outcome == "skipped_rate_limit")
    finished = datetime.now(UTC).isoformat()
    # pass_rate among judged product cases (exclude rate-limit skips)
    judged = passed + failed
    pass_rate_judged = round(passed / judged, 4) if judged else 0.0
    pass_rate_all = round(passed / len(results), 4) if results else 0.0

    by_agent: dict[str, dict[str, Any]] = {}
    for r in results:
        bucket = by_agent.setdefault(
            r.agent_id,
            {"passed": 0, "failed": 0, "skipped_rate_limit": 0, "cases": []},
        )
        if r.outcome == "pass":
            bucket["passed"] += 1
        elif r.outcome == "skipped_rate_limit":
            bucket["skipped_rate_limit"] += 1
        else:
            bucket["failed"] += 1
        bucket["cases"].append(asdict(r))

    report = {
        "started_at": started,
        "finished_at": finished,
        "host": args.host,
        "auth": "bearer" if bearer else "none",
        "minted_key_id": key_id or None,
        "runner": {
            "sleep": args.sleep,
            "max_429_retries": args.max_429_retries,
            "backoff_base": args.backoff_base,
            "backoff_cap": args.backoff_cap,
            "batch_size": args.batch_size,
            "batch_pause": args.batch_pause,
            "rate_limit_as_skip": rate_limit_as_skip,
        },
        "summary": {
            "agents": len(by_agent),
            "cases_total": len(results),
            "cases_passed": passed,
            "cases_failed": failed,
            "cases_skipped_rate_limit": skipped_rl,
            "pass_rate": pass_rate_all,
            "pass_rate_excluding_rate_limit": pass_rate_judged,
        },
        "agents": by_agent,
        "failed_cases": [asdict(r) for r in results if r.outcome == "fail"],
        "skipped_rate_limit_cases": [
            asdict(r) for r in results if r.outcome == "skipped_rate_limit"
        ],
    }

    reports_dir = ROOT / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    if args.report:
        report_path = Path(args.report)
        if not report_path.is_absolute():
            report_path = ROOT / report_path
    else:
        stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
        report_path = reports_dir / f"run_{stamp}.json"

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (reports_dir / "latest.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print("\n======== RUN REPORT ========")
    print(
        f"agents={len(by_agent)} total={len(results)} "
        f"passed={passed} failed={failed} skip_429={skipped_rl}"
    )
    print(f"pass_rate_all={pass_rate_all} pass_rate_excl_429={pass_rate_judged}")
    print(f"report={report_path}")
    if failed:
        print("First product failures:")
        for r in [x for x in results if x.outcome == "fail"][:15]:
            print(f"  - {r.agent_id}/{r.case_id}: {r.failures}")

    # Exit 1 only for product fails (not rate-limit skips)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
