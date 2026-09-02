# CASOPS Control UI

Operator UI for the public control plane (`/api/v3`). Source for this app lives only in `ui/`. Style tokens come from `spec/common-style.html`. Behavior is specified in `spec/ui.v1.md`.

This is not a chat wrapper, not a T3 enablement console, and not a production-activation panel.

## Prerequisites

- Node.js 20+
- The control plane on `http://127.0.0.1:18080`

From the repo root:

```powershell
$env:PYTHONPATH = "src"
$env:CASOPS_AGENTS_ROOT = "agents"
python -m uvicorn casops.api.control:create_app_from_env --factory --host 127.0.0.1 --port 18080
```

## Install and run

```powershell
cd ui
npm install
npm run dev
```

Open `http://127.0.0.1:15173`. The Vite dev server proxies `/api`, `/health`, and `/debug` to `:18080`. Leave **Settings → Base URL** empty to use that proxy.

The header log icon opens a right-side drawer with live **API log** and **UI log** tabs. Each line is also appended as JSONL under `logs/debug/<session>-api.log` and `logs/debug/<session>-ui.log`.

To call the host directly (CORS is enabled for Vite origins):

- Set Base URL to `http://127.0.0.1:18080`
- Or start with `VITE_CASOPS_BASE=http://127.0.0.1:18080`

## Tests

```powershell
cd ui
npm test
npm run build
```

`tests/api-contract.test.ts` checks every spec §19 `/api/v3` path has a client binding. `tests/mutation-headers.test.ts` checks POST/DELETE always send the four mutation headers and that `agent_runtime` cannot approve.

Per-agent Help files under `ui/public/docs/agents/<agent_id>/` are generated from each agent folder. Refresh with:

```powershell
python tools/generate_help_agent_docs.py
```

User guide is copied from `agents/<id>/docs`. Spec is merged from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/`.

## Operator notes

- Dry-run defaults **on**. Reason is required before mutations.
- Approve is only enabled for `independent_approver` (host allow-list).
- Template memory `mode: none` disables Write candidate.
- `NOT_RUN` / `INDICATIVE` are never styled as a green pass.
- There is no Enable T3 control and no promote-to-production control.
