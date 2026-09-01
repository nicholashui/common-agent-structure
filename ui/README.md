# CASOPS Control UI

Operator UI for the public control plane (`/api/v3`). Source for this app lives only in `ui/`. Style tokens come from `spec/common-style.html`. Behavior is specified in `spec/ui.v1.md`.

This is not a chat wrapper, not a T3 enablement console, and not a production-activation panel.

## Prerequisites

- Node.js 20+
- The control plane on `http://127.0.0.1:8080`

From the repo root:

```powershell
$env:PYTHONPATH = "src"
$env:CASOPS_AGENTS_ROOT = "agents"
python -m uvicorn casops.api.control:create_app_from_env --factory --host 127.0.0.1 --port 8080
```

## Install and run

```powershell
cd ui
npm install
npm run dev
```

Open `http://127.0.0.1:5173`. The Vite dev server proxies `/api` and `/health` to `:8080`. Leave **Settings → Base URL** empty to use that proxy.

To call the host directly (CORS is enabled for Vite origins):

- Set Base URL to `http://127.0.0.1:8080`
- Or start with `VITE_CASOPS_BASE=http://127.0.0.1:8080`

## Tests

```powershell
cd ui
npm test
npm run build
```

`tests/api-contract.test.ts` checks every spec §19 `/api/v3` path has a client binding. `tests/mutation-headers.test.ts` checks POST/DELETE always send the four mutation headers and that `agent_runtime` cannot approve.

## Operator notes

- Dry-run defaults **on**. Reason is required before mutations.
- Approve is only enabled for `independent_approver` (host allow-list).
- Template memory `mode: none` disables Write candidate.
- `NOT_RUN` / `INDICATIVE` are never styled as a green pass.
- There is no Enable T3 control and no promote-to-production control.
