# API-level samples — CASOPS `/api/v3` only

There is no `/api/v1`. Chat is `POST /api/v3/agents/specials.aesthetics-agent/runtime/chat`.

Mutation POSTs require `x-casops-actor`, `x-casops-reason`, `x-casops-expected-parent`, `x-casops-dry-run` or **409** `IMP_UNSIGNED`.

This control plane does **not** implement HTTP 429. xAI RPM is vendor, not `:18080`.

| File | Expected |
|---|---|
| `01-valid-chat.json` | 200; `memory_writes: []`; plugins/T3 false. 200 ≠ craft-correct |
| `02-malformed-empty-message.json` | 400 `CTX_BUDGET` |
| `03-malformed-not-json.txt` | 4xx parse |
| `04-auth-missing-headers.json` | 409 `IMP_UNSIGNED` (not 401) |
| `05-auth-invalid-actor.json` | 503 `IMP_CORRIGIBILITY` |
| `06-unknown-agent.json` | 409 `INH_PARENT_MISSING` |
| `07-oversized-message.json` | 400 `CTX_BUDGET` (build 32001 chars at run time) |
| `08-rate-limit-honesty.md` | No 429 from CASOPS |
| `09-cross-domain-run.json` | Run 200; Chat did not execute the DAG |
| `10-cross-domain-other-agent.json` | Chat `specials.intent-analysis-agent` does not invoke this pack |
| `11-evals-fixtures-get.md` | CHARACTERIZATION list; no `pass` |
