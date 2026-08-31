# corrigibility-invariant-service

Host-owned invariant authority (spec §15, FR-COR-001–003, WP-101–103).

Runs as its own process with its own volume and Ed25519 key. It does **not** serve the public `/api/v3` plane.

## Endpoints

| Method | Path | Actor |
|---|---|---|
| GET | `/health` | none |
| GET | `/internal/v1/reference` | `host_service`, `human_operator` |
| PUT | `/internal/v1/reference` | `independent_approver` |
| POST | `/internal/v1/attest` | `host_service` |
| GET | `/internal/v1/alerts` | `human_operator`, `host_service` |

Mismatch, tamper, unavailability, and unauthorized writes invoke containment stop (`IMP_CORRIGIBILITY`). There is no degraded mode.

Attestation checkpoints: `compose`, `run_start`, `production_effect`.

## Environment

- `CASOPS_CORRIGIBILITY_DATA` — persistent volume (default `var/casops/corrigibility`)
- `CASOPS_CORRIGIBILITY_KEY` — Ed25519 PEM (created on first start if missing)

```text
uvicorn casops.corrigibility.bootstrap:create_app_from_env --factory --port 8081
```
