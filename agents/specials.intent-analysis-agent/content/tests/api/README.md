# API-level samples — CASOPS `/api/v3` only

There is no `/api/v1`. Chat is `POST /api/v3/agents/{agent_id}/runtime/chat`. Run is `POST /api/v3/agents/{agent_id}/runtime/run`.

Mutation POSTs/PUT/PATCH/DELETE on `/api/v3` require all four headers or the host returns **409** `IMP_UNSIGNED`:

- `x-casops-actor` (e.g. `human_operator`)
- `x-casops-reason` (e.g. `operator chat`)
- `x-casops-expected-parent` (string; may be empty)
- `x-casops-dry-run` (`true` / `false`)

This control plane does **not** implement HTTP 429. xAI Grok RPM limits are a **vendor** property (`docs.x.ai`), not `:18080`. A rate-limit test that expects 429 from CASOPS is **invalid** unless a gateway in front of the host is documented.

| File | Scenario | Expected |
|---|---|---|
| `01-valid-chat.json` | Valid Chat body | 200 JSON with `agent_id`, `reply`, `memory_writes: []`, `plugins_executed: false`, `t3_enabled: false` |
| `02-malformed-empty-message.json` | Empty `message` | 400 `CTX_BUDGET` |
| `03-malformed-not-json.txt` | Raw non-JSON body | 4xx (FastAPI parse) |
| `04-auth-missing-headers.json` | No mutation headers | 409 `IMP_UNSIGNED` |
| `05-auth-invalid-actor.json` | Unknown actor class | 503 `IMP_CORRIGIBILITY` |
| `06-unknown-agent.json` | `does.not.exist` | 409 `INH_PARENT_MISSING` |
| `07-oversized-message.json` | `message` > 32000 chars | 400 `CTX_BUDGET` |
| `08-rate-limit-honesty.md` | Burst Chat | No 429 from CASOPS; record gateway 429 separately if present |
| `09-cross-domain-run.json` | `runtime/run` vs Chat | 200 Run proof; `path_id` run; Chat did not execute the DAG |
| `10-cross-domain-other-agent.json` | Chat `common.health` | 200 for that agent_id; this pack is not invoked |
| `11-evals-fixtures-get.md` | GET fixtures | CHARACTERIZATION list; no `pass` field |

Bodies are request samples. Execute with the curls in `../../test_guide.md`. Do not treat Chat 200 as eval PASS (ISSUE-0002).
