# API-level samples — `/api/v3` only

Chat: `POST /api/v3/agents/specials.general-creative-agent/runtime/chat`.

Mutation POSTs need `x-casops-actor`, `x-casops-reason`, `x-casops-expected-parent`, `x-casops-dry-run` or **409** `IMP_UNSIGNED`. No HTTP 429 on this host.

| File | Expected |
|---|---|
| `01-valid-chat.json` | 200; fail-closed fields. 200 ≠ craft-correct |
| `02-malformed-empty-message.json` | 400 `CTX_BUDGET` |
| `03-malformed-not-json.txt` | 4xx parse |
| `04-auth-missing-headers.json` | 409 `IMP_UNSIGNED` (not 401) |
| `05-auth-invalid-actor.json` | 503 `IMP_CORRIGIBILITY` |
| `06-unknown-agent.json` | 409 `INH_PARENT_MISSING` |
| `07-oversized-message.json` | 400 `CTX_BUDGET` (build 32001 chars at run time) |
| `08-rate-limit-honesty.md` | No 429 from CASOPS |
| `09-cross-domain-run.json` | Run 200; Chat ≠ DAG |
| `10-cross-domain-other-agent.json` | Chat aesthetics does not invoke this pack |
| `11-evals-fixtures-get.md` | CHARACTERIZATION list; no `pass` |
