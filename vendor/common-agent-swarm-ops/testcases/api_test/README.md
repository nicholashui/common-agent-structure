# API tests — every video pack agent + specials

Each agent has a folder named by **agent id** with **3 API test cases**.

```text
api_test/
  video.planner/cases.json
  specials.intent_analysis_agent/cases.json
  ...
  generate_agent_api_tests.py   # regenerate all cases
  run_all_api_tests.py          # execute all cases, write report
  reports/latest.json
```

## Generate cases

```bash
cd testcases/api_test
python generate_agent_api_tests.py
```

Creates ~114 pack agents + ~19 specials × 3 cases each.

## Run all tests

Host must be up. Prefer:

```text
CASOPS_DEV_TRUST=1
```

```powershell
cd C:\Project\common-agent-swarm-ops\testcases\api_test
python generate_agent_api_tests.py
python run_all_api_tests.py --host http://127.0.0.1:8000 --mint
python render_run_status.py
```

Options:

| Flag | Meaning |
|------|---------|
| `--only video.planner` | One agent |
| `--only specials.` | All specials |
| `--limit-agents 10` | First N agent folders |
| `--report reports/my_run.json` | Custom report path |
| `--fail-fast` | Optional: stop on first **product** FAIL |
| `--bearer casops_...` | Use existing key (no mint) |
| `--sleep 0.35` | Pause between cases (default **0.35s**) |
| `--max-429-retries 5` | Extra tries after 429 (default 5) |
| `--batch-size 80` / `--batch-pause 5` | Pause after every N cases |
| `--rate-limit-is-fail` | Treat exhausted 429 as FAIL (default: **SKIP_429**) |

**Continue-on-error (default):** FAIL / SKIP / exception → record and go to next case.

**Outcomes:**
| Tag | Meaning | Exit code impact |
|-----|---------|------------------|
| PASS | Success criteria met | OK |
| FAIL | Product/logic failure | exit 1 |
| SKIP_429 | Rate limited after retries | **not** exit 1 |

## Case shape (`cases.json`)

```json
{
  "agent_id": "video.planner",
  "kind": "pack",
  "cases": [
    {
      "id": "tc1",
      "name": "...",
      "method": "POST",
      "path": "/api/v1/agent-loops/agents/video.planner/run",
      "body": { "goal": "...", "enable_v3": true, "max_steps": 3 },
      "success_criteria": {
        "http_status": [200],
        "json_equals": { "agent_id": "video.planner" },
        "required_keys_any": ["ok", "v3", "phases", "status"]
      }
    }
  ]
}
```

## Success criteria (default)

| Kind | Pass when |
|------|-----------|
| **Pack `video.*`** | HTTP 200, `agent_id` matches, at least one of `ok`/`v3`/`phases`/`status`/`run_id` |
| **Specials** | HTTP 200 and domain keys (varies by service) |

Offline only: samples keep `allow_production` / `allow_network` / live flags **false**.

## Report

Written to `reports/run_<timestamp>.json` and `reports/latest.json` with per-agent pass/fail and failure messages.
