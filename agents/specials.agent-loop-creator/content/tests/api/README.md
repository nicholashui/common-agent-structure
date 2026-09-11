# API samples — `/api/v3` only

Chat: `POST /api/v3/agents/specials.agent-loop-creator/runtime/chat`.

Mutation POSTs need four headers or **409** `IMP_UNSIGNED`. No 429 on this host.

| File | Expected |
|---|---|
| `01-valid-chat.json` | 200 fail-closed. 200 ≠ craft-correct |
| `02-malformed-empty-message.json` | 400 `CTX_BUDGET` |
| `03-malformed-not-json.txt` | 4xx |
| `04-auth-missing-headers.json` | 409 `IMP_UNSIGNED` |
| `05-auth-invalid-actor.json` | 503 `IMP_CORRIGIBILITY` |
| `06-unknown-agent.json` | 409 `INH_PARENT_MISSING` |
| `07-oversized-message.json` | 400 `CTX_BUDGET` (32001 chars at run time) |
| `08-rate-limit-honesty.md` | no CASOPS 429 |
| `09-cross-domain-run.json` | Run 200; Chat ≠ DAG |
| `10-cross-domain-other-agent.json` | Chat GCA does not invoke this pack |
| `11-evals-fixtures-get.md` | CHARACTERIZATION; no `pass` |
