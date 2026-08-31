# compose-service

Folder validation, corrigibility attestation (step 2), MRO, merge, and compose-preview.

Preview is a dry run: it returns findings and a prospective lock and never writes `generated/*.lock.json`.

## Endpoints

| Method | Path |
|---|---|
| GET | `/health` |
| POST | `/internal/v1/compose-preview` |
| POST | `/internal/v1/compose` |

Public `/api/v3/agents/{id}/compose-preview` is served by the control plane.

## Environment

- `CASOPS_AGENTS_ROOT` — agent folder tree
- `CASOPS_CORRIGIBILITY_DATA` / `CASOPS_CORRIGIBILITY_KEY` — optional host invariant store
