"""Assemble book/CASOPS_THE_COMPLETE_BOOK.md from live repo files plus authored chapters."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "book" / "CASOPS_THE_COMPLETE_BOOK.md"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _json(path: Path) -> object:
    return json.loads(_read(path))


def agent_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    root = REPO / "agents"
    for child in sorted(root.iterdir(), key=lambda p: p.name.lower()):
        spec_path = child / "agent_spec.json"
        if not child.is_dir() or not spec_path.is_file():
            continue
        try:
            spec = json.loads(spec_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            spec = {}
        if not isinstance(spec, dict):
            spec = {}
        mem = ""
        policy = child / "memory" / "policy.json"
        if policy.is_file():
            try:
                mem = str(json.loads(policy.read_text(encoding="utf-8")).get("mode") or "")
            except json.JSONDecodeError:
                mem = ""
        rows.append(
            {
                "folder": child.name,
                "agent_id": str(spec.get("agent_id") or child.name),
                "role": str(spec.get("role") or ""),
                "status": str(spec.get("status") or ""),
                "schema_version": str(spec.get("schema_version") or ""),
                "structure_id": str(spec.get("structure_id") or ""),
                "va_category": "" if spec.get("va_category") in {None, "none", "null"} else str(spec.get("va_category") or ""),
                "va_id": "" if spec.get("va_id") in {None, "none", "null"} else str(spec.get("va_id") or ""),
                "provider": str((spec.get("model_policy") or {}).get("provider") or ""),
                "network": str((spec.get("model_policy") or {}).get("network_access")),
                "tools": json.dumps(spec.get("allowed_tools") or []),
                "plugins": json.dumps(spec.get("allowed_plugins") or []),
                "activation": str(spec.get("production_activation_requested")),
                "memory_mode": mem,
                "prompt": str(spec.get("prompt_reference") or ""),
                "rubric": str(spec.get("rubric_reference") or ""),
            }
        )
    return rows


def template_tree() -> str:
    root = REPO / "agents" / "_template_v3"
    lines: list[str] = []
    for path in sorted(root.rglob("*")):
        if path.is_file():
            rel = path.relative_to(root).as_posix()
            lines.append(f"- `{rel}` ({path.stat().st_size} bytes)")
    return "\n".join(lines)


def adr_block() -> str:
    adr_dir = REPO / "docs" / "adr"
    parts: list[str] = []
    for path in sorted(adr_dir.glob("adr-*.md")):
        parts.append(_read(path).rstrip())
        parts.append("")
    return "\n".join(parts)


def error_tables() -> str:
    cat = _json(REPO / "errors" / "catalogue.json")
    codes = cat["codes"]
    parts = [
        f"Catalogue `schema_version` is `{cat.get('schema_version')}`. Source section is `{cat.get('source_section')}`.",
        "",
        "The twelve required fields on every code are:",
        "",
    ]
    for field in cat["field_contract"]:
        parts.append(f"- `{field}`")
    parts.append("")
    parts.append("External HTTP body always uses `external_message` for the `message` field shown to untrusted callers. Operators read `operator_message`.")
    parts.append("")
    by_cat: dict[str, list[dict[str, object]]] = {}
    for item in codes:
        by_cat.setdefault(str(item["category"]), []).append(item)
    for category in sorted(by_cat):
        parts.append(f"### Category `{category}`")
        parts.append("")
        parts.append("| code | severity | HTTP | retryability | containment | incident | default_action | operator_message |")
        parts.append("|---|---|---|---|---|---|---|---|")
        for item in by_cat[category]:
            parts.append(
                "| `{code}` | {severity} | {http} | {retry} | {cont} | {inc} | {act} | {op} |".format(
                    code=item["code"],
                    severity=item["severity"],
                    http=item["http_mapping"],
                    retry=item["retryability"],
                    cont=item["containment_required"],
                    inc=item["incident_required"],
                    act=str(item["default_action"]).replace("|", "/"),
                    op=str(item["operator_message"]).replace("|", "/"),
                )
            )
        parts.append("")
        for item in by_cat[category]:
            parts.append(f"#### `{item['code']}`")
            parts.append("")
            parts.append(f"- category: `{item['category']}`")
            parts.append(f"- severity: `{item['severity']}`")
            parts.append(f"- retryability: `{item['retryability']}`")
            parts.append(f"- default_action: {item['default_action']}")
            parts.append(f"- containment_required: `{item['containment_required']}`")
            parts.append(f"- incident_required: `{item['incident_required']}`")
            parts.append(f"- http_mapping: `{item['http_mapping']}`")
            parts.append(f"- telemetry_event: `{item['telemetry_event']}`")
            parts.append(f"- test_fixture: `{item['test_fixture']}`")
            parts.append(f"- operator_message: {item['operator_message']}")
            parts.append(f"- external_message: {item['external_message']}")
            parts.append("")
    parts.append(f"Total codes in this catalogue: **{len(codes)}**.")
    parts.append("")
    return "\n".join(parts)


def inventory() -> str:
    rows = agent_rows()
    parts = [
        f"The host loads **{len(rows)}** folders that contain `agent_spec.json`. The public id is the `agent_id` field, not necessarily the folder name. The template lives in folder `_template_v3` with `agent_id` `casops.template.baseline_safe`.",
        "",
        "| folder | agent_id | role | status | va_category | va_id | provider | network | tools | plugins | production_activation_requested | memory_mode |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        parts.append(
            "| `{folder}` | `{agent_id}` | {role} | `{status}` | `{va_category}` | `{va_id}` | `{provider}` | `{network}` | `{tools}` | `{plugins}` | `{activation}` | `{memory_mode}` |".format(
                **row
            )
        )
    parts.append("")
    parts.append("### Full identity records")
    parts.append("")
    for row in rows:
        parts.append(f"#### `{row['agent_id']}`")
        parts.append("")
        parts.append(f"- disk folder: `agents/{row['folder']}/`")
        parts.append(f"- structure_id: `{row['structure_id']}`")
        parts.append(f"- schema_version: `{row['schema_version']}`")
        parts.append(f"- role: {row['role']}")
        parts.append(f"- status: `{row['status']}`")
        parts.append(f"- va_category: `{row['va_category']}`")
        parts.append(f"- va_id: `{row['va_id']}`")
        parts.append(f"- model_policy.provider: `{row['provider']}`")
        parts.append(f"- model_policy.network_access: `{row['network']}`")
        parts.append(f"- allowed_tools: `{row['tools']}`")
        parts.append(f"- allowed_plugins: `{row['plugins']}`")
        parts.append(f"- production_activation_requested: `{row['activation']}`")
        parts.append(f"- memory.policy.mode: `{row['memory_mode']}`")
        parts.append(f"- prompt_reference: `{row['prompt']}`")
        parts.append(f"- rubric_reference: `{row['rubric']}`")
        parts.append(f"- Help spec file generated at: `ui/public/docs/agents/{row['agent_id']}/spec.md`")
        parts.append(f"- Help user guide generated at: `ui/public/docs/agents/{row['agent_id']}/userguide.md`")
        parts.append("")
    return "\n".join(parts)


NARRATIVE = r'''# CASOPS: The Complete Book

**Title.** Common-Agent Swarm Operations Host — The Complete, Self-Contained Operator and Implementer Book  
**Work.** this repository (paths are relative to the repo root)  
**Host package.** `casops` version `0.1.0`  
**Agent structure.** `casops.common_agent.v3`  
**Schema.** `3.0`  
**Public HTTP plane.** FastAPI, prefix `/api/v3` only  
**Local operator UI.** Vite + React at `http://127.0.0.1:15173`, talking only to the public plane  
**Control-plane bind.** `http://127.0.0.1:18080`  
**Edition.** Generated from the live repository files, not from memory of an older tree  
**Production certification.** Not claimed. This book does not authorize production activation, network grants, plugin execution, T3 enablement, or L5 promotion.

This book is written so that after you finish it you can operate, call, and explain every public surface of this repository without opening another document. File paths are given because they are how objects exist on disk. The contents of those objects that you need in order to operate are copied into this book.

---

## How to read this book

Read in order. Later chapters assume you already know the mutation contract, the actor classes, and that `/health` is not a v3 resource.

Do not skip:

1. Part I (what the host is and is not)
2. Part II (install, pytest, start)
3. Part III (mutation contract)
4. Part V (every API)
5. Part VIII and IX (worked API and UI procedures)

The agent inventory at the end is not optional if you need to know which `agent_id` strings the host will accept.

## Contents

- Part I — What this project is
- Part II — Install, prove, start
- Part III — Mutation contract and actors
- Part IV — Agent folder contract (schema, template files, I/O)
- Part V — Public API, every path
- Part VI — Non-v3 HTTP (`/health`, `/debug/logs`, `/debug/chat`)
- Part VII — Control UI, every surface
- Part VIII — Step-by-step API usage
- Part VIII.A — Remaining API procedures
- Part VIII.B — Python httpx client
- Part IX — Step-by-step UI usage
- Part IX.A — UI control catalogue
- Part IX.B — Remaining UI screens
- Part X — Environment variables
- Part XI — Eight-process deployment
- Part XII — CLIs
- Part XIII — Forbidden operations
- Part XIV — UI client mutation header injection
- Part XV — Help and log generation commands
- Part XVI — Error catalogue (every code, twelve fields)
- Part XVII — Architecture decision records (ADR-001 … ADR-013)
- Part XVIII — Loaded agent inventory (every `agent_spec.json`)
- Part XIX — Complete host library (`src/casops/`)
- Part XX — Complete Control UI source
- Part XXI — Control UI unit tests
- Part XXII — Host tests
- Part XXIII — Eight process services
- Part XXIV — Operator and implementer documents
- Part XXV — Common-agent structure specification
- Part XXVI — Implementation plan
- Part XXVII — Evaluation plan
- Part XXVIII — Root `common_agent_structure.md`
- Part XXIX — Generic Help markdown
- Part XXX — Template agent documents
- Part XXXI — Book of Knowledge
- Part XXXII — Repository tools
- Part XXXIII — How this book was assembled

---

# Part I — What this project is

## I.1 One sentence that is still complete

CASOPS is a **greenfield host** that loads **agent folders** from disk, **composes** them under host-owned invariants, and **exposes a single public HTTP plane** so a human operator can inspect, compose-preview, run `baseline_safe`, chat through the host LLM router, and operate memory/plugins/safety/improvement **without ever letting an agent identity own the control plane**.

## I.2 Two layers

1. **Host** — Python package `src/casops/`, FastAPI app `casops.api.control:create_app_from_env`, eight optional Docker processes under `services/`, CLIs `casops-eval` and `casops-citation`, error catalogue `errors/catalogue.json`.
2. **Agent folder** — one directory under `agents/` containing `agent_spec.json` plus the v3 folder contract (prompts, rubrics, runtime DAG, memory policy, plugins registry, safety, corrigibility projection, evals, sources, docs). The folder is data. It cannot approve itself, write host invariants, enable T3, grant network, or flip `production_activation_requested`.

You talk to the host through:

- HTTP `GET/POST/DELETE` on `http://127.0.0.1:18080/api/v3/...`
- `GET http://127.0.0.1:18080/health` (liveness only; excluded from OpenAPI)
- Operator sinks `POST /debug/logs`, `POST /debug/chat`, `GET /debug/chat` (also excluded from OpenAPI)
- The Control UI at `http://127.0.0.1:15173`
- CLIs `python -m casops.eval` and `python -m casops.citation`

You do **not** talk to internal ports `8081`–`8087` from the browser.

## I.3 What this project is not

- Not a chat wrapper. Chat exists as `POST /api/v3/agents/{agent_id}/runtime/chat` and a Chat page, but it is host-routed free text, does not stream tokens, does not write memory, does not run plugins, does not enable T3, and does not grant network.
- Not a second control plane. The UI has no private mutating backend. Vite proxies `/api`, `/health`, and `/debug` to `:18080`.
- Not a production-activation console. There is no “go live” button. `production_activation_requested` stays `false` on the template and on the loaded pack agents as shipped.
- Not an eval green-pass dashboard. Default `casops-eval` is `NOT_RUN` / `pass: false` while instruments `INS-01`…`INS-08` are `UNQUALIFIED`. Screening is `INDICATIVE` and cannot pass.
- Not Org Chat as a write surface. Agent Org Chat is a read-only relationship map.

## I.4 Names you will see

| Name | Meaning |
|---|---|
| CASOPS | Common-Agent Swarm Operations, the host |
| `casops` | Python package name and PyPI-style project name in `pyproject.toml` |
| `casops.common_agent.v3` | Structure id every loadable `agent_spec.json` must carry |
| `3.0` | Schema version constant |
| `baseline_safe` | First shippable profile: local deterministic adapter, no memory writes, no plugins, T0 cache only |
| `casops.template.baseline_safe` | Template agent id |
| `_template_v3` | Template folder name on disk |
| Control plane | Public FastAPI process |
| Control UI | Operator SPA in `ui/` |
| Mutation contract | Four headers required on every v3 write |
| Corrigibility | Host-owned invariants the agent folder cannot rewrite |
| Compose-preview | Prospective lock; must not write lock files (`wrote_locks: false`) |
| T0–T3 | Cache tiers. T3 implemented, default off |
| I1 I2 I3 | Plugin isolation tiers. Validate-without-exec on the public plane |
| L5 | Research-only source rewrite. No HTTP promote-to-production |
| Help | Right drawer + `/help` full page, markdown from `ui/public/docs` |
| Logs drawer | API log + UI log, JSONL under `logs/debug/` |
| Chat transcripts | JSONL under `logs/chat/<agent_id>/` |

## I.5 Repository layout (complete top level that matters)

```
<repo-root>\
  agents\                      loadable agent folders (scan agent_spec.json; do not freeze a count)
  src\casops\                  host library
  services\                    eight process Dockerfiles + main.py
  ui\                          Control UI (mandatory UI source root)
  schemas\agent\agent_spec.schema.json
  schemas\locks\compose.lock.schema.json
  errors\catalogue.json        93 codes, 12-field contract
  docs\adr\                    ADR-001 … ADR-013
  docs\citation\               citation audit artifacts
  spec\                        structure specs, ui.v1.md, help_spec.md, common-style.html
  tests\contract\  tests\unit\  tests\security\
  deploy\dev\docker-compose.yml
  scripts\start_all.ps1  scripts\stop_all.ps1
  tools\                       import agents, generate Help docs, write this book
  book\                        this book
  logs\debug\  logs\chat\      operator runtime files
  var\                         llm-settings.json, server pid state
  pyproject.toml
  user_guide.v1.md
  implementation_status.md
  implementation_plan.md
  common_agent_structure.md
  evaluation_plan.md
```

Python package discovery: `[tool.setuptools.packages.find] where = ["src"]`. Import as `import casops`. Console scripts: `casops-eval = casops.eval.harness:main`, `casops-citation = casops.citation.__main__:main`. Requires Python `>=3.12`. Runtime dependencies: `jsonschema>=4.23`, `pydantic>=2.8`, `cryptography>=43.0`, `wasmtime>=27.0`. Optional `api`: FastAPI, httpx, uvicorn. Optional `dev`: pytest, ruff, mypy.

---

# Part II — Install, prove, start

## II.1 Prerequisites

- Windows with PowerShell (the operator scripts are `.ps1`)
- Python 3.12 or newer
- Node.js 20+ if you will run the Control UI
- Docker Desktop only if you will start the eight-process compose file
- Network only for citation audit and for host LLM providers other than `local_deterministic`

```powershell
python --version
cd <repo-root>
```

## II.2 Create a venv and install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -e ".[dev,api]"
$env:PYTHONPATH = "src"
python -c "import casops; print(casops.__version__)"
```

Expect printed version `0.1.0`.

UI:

```powershell
cd <repo-root>\ui
npm install
```

`ui/package.json` scripts: `dev` = `vite`, `build` = `tsc --noEmit && vite build`, `preview` = `vite preview`, `test` = `vitest run`. Dependencies include React 18, react-router-dom 6, lucide-react, react-markdown, remark-gfm. Dev server port **15173** `strictPort: true`. Preview port **4173**. Proxies `/api`, `/health`, `/debug` to `http://127.0.0.1:18080`.

## II.3 Prove the host

```powershell
cd <repo-root>
$env:PYTHONPATH = "src"
python -m pytest tests -q
```

Expect exit code 0. If this fails, do not start HTTP.

UI tests:

```powershell
cd <repo-root>\ui
npm test
```

## II.4 Start the local operator stack

Recommended:

```powershell
powershell -File scripts/start_all.ps1
```

This starts:

- control plane: `python -m uvicorn casops.api.control:create_app_from_env --factory --host 127.0.0.1 --port 18080` with `PYTHONPATH=src` and `CASOPS_AGENTS_ROOT=<repo>\agents`
- Control UI: `npx vite --host 127.0.0.1 --port 15173` from `ui/`

It writes `var\casops-servers.json` and logs to `logs\control-plane.out.log`, `logs\control-plane.err.log`, `logs\ui.out.log`, `logs\ui.err.log`.

Stop:

```powershell
powershell -File scripts/stop_all.ps1
```

Manual equivalent:

```powershell
cd <repo-root>
$env:PYTHONPATH = "src"
$env:CASOPS_AGENTS_ROOT = "agents"
python -m uvicorn casops.api.control:create_app_from_env --factory --host 127.0.0.1 --port 18080
```

Second window:

```powershell
cd <repo-root>\ui
npx vite --host 127.0.0.1 --port 15173
```

Factory `create_app_from_env` loads `.env` from process cwd and from the parent of `CASOPS_AGENTS_ROOT`, then `create_control_plane(agents_root=...)`.

## II.5 Liveness

```powershell
curl.exe http://127.0.0.1:18080/health
```

Exact body:

```json
{"status":"ok","service":"control-plane"}
```

OpenAPI JSON is at `http://127.0.0.1:18080/openapi.json`. The app replaces `app.openapi` so **only paths starting with `/api/v3` appear**. `/health`, `/debug/logs`, `/debug/chat` are implemented but stripped from OpenAPI.

CORS allow_origins default:

- `http://127.0.0.1:15173`
- `http://localhost:15173`
- `http://127.0.0.1:4173`
- `http://localhost:4173`

plus any comma-separated `CASOPS_CORS_ORIGINS`. `allow_credentials=True`, `allow_methods=["*"]`, `allow_headers=["*"]`.

---

# Part III — Mutation contract and actors

## III.1 The four headers

Every `POST`, `PUT`, `PATCH`, and `DELETE` whose path starts with `/api/v3` is intercepted by middleware `mutation_contract` in `casops.api.control`. If any of these is missing, the process **does not enter the route**. It returns HTTP **409** with code `IMP_UNSIGNED`.

| Header | Example | Rules |
|---|---|---|
| `x-casops-actor` | `human_operator` | Must parse to an `ActorClass` |
| `x-casops-reason` | `operator-walkthrough` | Non-empty string. The UI client will substitute `reasonFallback` `"operator chat"` on Chat POST if the reason field is blank |
| `x-casops-expected-parent` | `none` | Required even when the value is the literal `none` |
| `x-casops-dry-run` | `true` | Required. Middleware treats `1`, `true`, `yes` (any case) as dry-run |

GET requests under `/api/v3` do not need the headers.

`/debug/*` and `/health` are **not** under `/api/v3`, so they do **not** require the mutation contract.

Exact unsigned body:

```json
{
  "error": {
    "code": "IMP_UNSIGNED",
    "message": "mutation requires actor, reason, expected parent version, dry-run",
    "containment_required": false
  }
}
```

Catalogue `external_message` for `IMP_UNSIGNED` is `The request was rejected by host policy.` Route handlers that raise `CasopsError` use the catalogue external message. The middleware unsigned path uses the more specific operator string above.

## III.2 Actor classes

Enum `casops.auth.actors.ActorClass`:

- `human_operator`
- `independent_approver`
- `host_service`
- `agent_runtime`
- `plugin`
- `peer_agent`

Authorization is deny-by-default. The only allowed pairs `(actor, action)` are:

| actor | action |
|---|---|
| host_service | attest_invariants |
| host_service | read_invariant_reference |
| independent_approver | write_invariant_reference |
| independent_approver | approve_candidate |
| independent_approver | write_instrument_record |
| independent_approver | l5_research_write |
| host_service | l5_research_write |
| human_operator | operator_shutdown |
| human_operator | read_invariant_reference |
| host_service | write_instrument_record |
| host_service | read_instrument |
| human_operator | read_alerts |
| host_service | read_alerts |
| independent_approver | read_alerts |

`is_allowed(actor, action)` returns false for everything else, including every action by `agent_runtime`, `plugin`, and `peer_agent`.

## III.3 Agent cannot approve

If `x-casops-actor` is `agent_runtime` and the path ends with `/approve`, or the path contains `corrigibility` and the method is not GET, middleware returns HTTP **503**:

```json
{
  "error": {
    "code": "IMP_SELF_APPROVAL",
    "message": "agent cannot approve or write invariants",
    "containment_required": false
  }
}
```

`POST /api/v3/agents/{id}/improvement/candidates/{cid}/approve` additionally requires `is_allowed(actor, "approve_candidate")`, which is only `independent_approver`. Anyone else, including `human_operator` and `host_service`, raises `IMP_SELF_APPROVAL` from the route.

LLM settings POSTs call `_forbid_agent_llm_actor`: `agent_runtime` cannot change host or per-agent LLM.

The UI client (`ui/src/api/v3.ts`) throws `MutationContractError` `IMP_UNSIGNED` in the browser **before** fetch if a mutating call lacks actor/reason/expectedParent/dryRun, and `IMP_SELF_APPROVAL` if path ends with `/approve` and actor is `agent_runtime`.

## III.4 PowerShell header block you will reuse

```powershell
$base = "http://127.0.0.1:18080"
$agent = "casops.template.baseline_safe"
$H = @{
  "x-casops-actor"           = "host_service"
  "x-casops-reason"          = "operator-walkthrough"
  "x-casops-expected-parent" = "none"
  "x-casops-dry-run"         = "true"
}
```

curl form:

```text
curl.exe -s -X POST "http://127.0.0.1:18080/api/v3/agents/casops.template.baseline_safe/compose-preview" ^
  -H "x-casops-actor: host_service" ^
  -H "x-casops-reason: operator-walkthrough" ^
  -H "x-casops-expected-parent: none" ^
  -H "x-casops-dry-run: true"
```

---

# Part IV — Agent folder contract

## IV.1 How the host finds an agent

`locate_agent_folder(agents_root, agent_id)`:

1. If `agents_root / agent_id / agent_spec.json` exists, that folder is used.
2. Otherwise every child directory with `agent_spec.json` is opened; the first whose JSON `agent_id` equals the request id is used.
3. If none, `CasopsError(INH_PARENT_MISSING)`.

That is why the template is called with id `casops.template.baseline_safe` while the folder is `agents/_template_v3`.

`GET /api/v3/agents` returns `{ "agents": [ ...summaries ] }` from `list_agent_summaries`: every child directory with `agent_spec.json`, sorted by folder name case-insensitive. Each summary:

```json
{
  "agent_id": "casops.template.baseline_safe",
  "folder": "agents/_template_v3",
  "structure_id": "casops.common_agent.v3",
  "schema_version": "3.0",
  "role": "BaselineSafeTemplate",
  "memory_mode": "none",
  "va_category": ""
}
```

`va_category` is `""` when the spec field is missing, `null`, `"none"`, or `"null"`. The UI must not invent categories. Fleet chips are the union of non-empty `va_category` values actually present on loaded agents, plus pack prefixes derived from `agent_id` (`specials`, `video`, `other`).

## IV.2 JSON Schema for `agent_spec.json`

Copied from `schemas/agent/agent_spec.schema.json`:

'''


def schema_and_template() -> str:
    schema = _read(REPO / "schemas" / "agent" / "agent_spec.schema.json")
    template = _read(REPO / "agents" / "_template_v3" / "agent_spec.json")
    cache = _read(REPO / "agents" / "_template_v3" / "runtime" / "cache.json")
    mem = _read(REPO / "agents" / "_template_v3" / "memory" / "policy.json")
    return f"""```json\n{schema.rstrip()}\n```\n\n`additionalProperties` is `true`, so pack-specific fields (`va_id`, `critique_edges`, refs) are allowed.\n\n## IV.3 Template `agent_spec.json` (complete file)\n\n```json\n{template.rstrip()}\n```\n\n## IV.4 Template memory policy (complete file)\n\n```json\n{mem.rstrip()}\n```\n\nWrites against this agent raise `MEM_TRUST_TIER`.\n\n## IV.5 Template cache policy (complete file)\n\n```json\n{cache.rstrip()}\n```\n\nT3 remains off. Public `POST .../cache/invalidate` clears the in-process manager and returns enabled tiers.\n\n## IV.6 Template folder file inventory\n\nEvery file under `agents/_template_v3/`:\n\n{template_tree()}\n"""


NARRATIVE_2 = r'''
## IV.7 I/O contract

`casops.compose.io.folder_io` / `io_from_spec` read `critique_edges.inputs` and `critique_edges.outputs` from `agent_spec.json`. Empty strings are dropped. `defined` is true only when at least one input or output remains. GET structure returns `io` with `merged: false`. GET resolved returns `io` with `merged: true` after compose. The Chat page `IoPanel` renders those lists. Chat still accepts free-text operator messages even when I/O is undeclared.

## IV.8 Copying the template

```powershell
Copy-Item -Recurse agents\_template_v3 agents\my_agent
```

Edit `agents/my_agent/agent_spec.json` `agent_id` to a new unique string, for example `casops.local.my_agent`. Restart the control plane. Keep `production_activation_requested: false`, empty tools/plugins, `network_access: false`, memory `mode: none`, unless you have a host change-control process.

---

# Part V — Public API, every path

Unless noted, replace `{agent_id}` with `casops.template.baseline_safe`. JSON below is the shape the **current** `create_control_plane` returns.

Client timeouts in the UI: default 30_000 ms, long (compose-preview, run, chat) 120_000 ms.

## V.0 Error envelope from `CasopsError`

```json
{
  "error": {
    "code": "INH_PARENT_MISSING",
    "message": "The request was rejected by host policy.",
    "containment_required": false
  }
}
```

HTTP status is the catalogue `http_mapping` for that code (`INH_PARENT_MISSING` is 409). Unknown agent id uses this code.

---

## V.1 GET /api/v3/agents

Headers: none required.

```powershell
Invoke-RestMethod "http://127.0.0.1:18080/api/v3/agents"
```

```text
curl.exe -s http://127.0.0.1:18080/api/v3/agents
```

Response: `{ "agents": [ { "agent_id", "folder", "structure_id", "schema_version", "role", "memory_mode", "va_category" }, ... ] }`.

UI: Fleet page load; AgentSwitcher extra ids.

---

## V.2 GET /api/v3/llm/providers

```powershell
Invoke-RestMethod "http://127.0.0.1:18080/api/v3/llm/providers"
```

Response `{ "providers": [ { "id", "label", "kind", "configured", "model" } ] }`.

Catalog entries implemented in `casops.runtime.llm.PROVIDER_CATALOG`:

| id | label | kind | key_env | default_base | default_model |
|---|---|---|---|---|---|
| local_deterministic | Local deterministic (offline) | local | (none; always configured) | | |
| openai | OpenAI | openai_compat | OPENAI_API_KEY | https://api.openai.com/v1 | gpt-4o-mini |
| xai | xAI Grok | openai_compat | XAI_API_KEY | https://api.x.ai/v1 | grok-4 |
| anthropic | Anthropic | anthropic | ANTHROPIC_API_KEY | https://api.anthropic.com | claude-sonnet-4-5 |

Aliases: `grok` and `x-ai` canonicalize to `xai`. `configured` is true for local, or when the key env var is non-empty. `DEFAULT_LLM` env, if set, becomes the host default; else first configured non-local provider; else `local_deterministic`. Credentials are read from process env / `.env` by `load_dotenv`. They are never stored in agent folders.

---

## V.3 GET /api/v3/llm/settings

Returns `state.llm.settings.public_view()`: default provider, per-agent overrides, env default, provider list. Used by Settings page.

## V.4 POST /api/v3/llm/settings

Mutation headers required. Body `{ "default_llm": "<id>" }` or empty/null to clear to env/default resolution. Unknown id → `PERF_ROUTE_UNAVAILABLE`. `agent_runtime` forbidden. If dry-run: returns public view with `saved: false`, `dry_run: true` and does not write `var/llm-settings.json` (path from `CASOPS_LLM_SETTINGS`, default `var/llm-settings.json`). If live: saves and `saved: true`.

```powershell
Invoke-RestMethod -Method POST -Headers $H -ContentType "application/json" `
  -Body '{"default_llm":"local_deterministic"}' `
  "$base/api/v3/llm/settings"
```

## V.5 GET /api/v3/agents/{agent_id}/llm

```json
{
  "agent_id": "casops.template.baseline_safe",
  "provider": "xai",
  "override": null,
  "default_llm": "xai",
  "providers": []
}
```

`provider` is `settings.resolved_for(agent_id)`. `override` is the per-agent map value or null.

## V.6 POST /api/v3/agents/{agent_id}/llm

Body `{ "provider": "<id>" }` or `"default"` / `"__default__"` / empty to clear override. Same dry-run and actor rules as host LLM POST.

---

## V.7 GET /api/v3/agents/{agent_id}/structure

```json
{
  "agent_id": "casops.template.baseline_safe",
  "structure_id": "casops.common_agent.v3",
  "schema_version": "3.0",
  "folder": "agents/_template_v3",
  "spec_bytes": 0,
  "io": {
    "defined": false,
    "merged": false,
    "source": "critique_edges",
    "inputs": [],
    "outputs": [],
    "role": "BaselineSafeTemplate",
    "prompt_reference": "prompts/primary.md",
    "rubric_reference": "rubrics/primary.md",
    "protocols": [],
    "plugin_interfaces": []
  },
  "spec": {
    "role": "BaselineSafeTemplate",
    "prompt_reference": "prompts/primary.md",
    "rubric_reference": "rubrics/primary.md",
    "critique_edges": {"inputs": [], "outputs": []}
  }
}
```

`spec_bytes` is `len` of the raw file. `io` is folder-declared. UI Structure and Chat IoPanel use this.

## V.8 GET /api/v3/agents/{agent_id}/resolved

Composer `preview` then:

```json
{
  "agent_id": "...",
  "mro": [],
  "compose_hash": "64 lowercase hex",
  "lock": {},
  "io": { "merged": true }
}
```

## V.9 POST /api/v3/agents/{agent_id}/compose-preview

Mutation headers required. Does not write lock files.

```json
{
  "agent_id": "...",
  "compose_hash": "64 hex",
  "mro": [],
  "findings": [],
  "errors": [],
  "lock": {},
  "wrote_locks": false
}
```

Check `wrote_locks` is JSON boolean `false`. UI Compose page shows hash and `wrote_locks`.

```powershell
Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/agents/$agent/compose-preview"
```

## V.10 GET /api/v3/agents/{agent_id}/runtime/plan

`{ "agent_id", "plan": "<raw text of runtime/execution.json>" }`.

## V.11 GET /api/v3/agents/{agent_id}/runtime/capabilities

Same as verify_folder: capability matrix.

## V.12 GET /api/v3/agents/{agent_id}/capabilities/matrix

Same `verify_folder` payload. UI Capabilities page.

## V.13 POST /api/v3/agents/{agent_id}/capabilities/verify

Mutation headers. Same matrix. `production_bindable` is not true for unverified/asserted capabilities.

## V.14 GET /api/v3/agents/{agent_id}/runtime/context-budget

`{ "agent_id", "budget": "<raw runtime/context.json>" }`.

## V.15 GET /api/v3/agents/{agent_id}/cache/stats

Cache manager stats plus `agent_id`. Template: T0 enabled, T3 off.

## V.16 POST /api/v3/agents/{agent_id}/cache/invalidate

```json
{ "agent_id": "...", "invalidated": true, "tiers": ["T0"] }
```

Clears the in-process cache.

## V.17 GET /api/v3/agents/{agent_id}/protocols

`{ "agent_id", "protocols": "<raw protocols/compatibility.json>" }`.

## V.18 GET /api/v3/agents/{agent_id}/plugins

`validate_registry(folder)` — does not execute plugin code.

## V.19 POST /api/v3/agents/{agent_id}/plugins/validate

Same registry result plus `"executed": false`.

## V.20 GET /api/v3/agents/{agent_id}/memory/policy

`{ "agent_id", "policy": "<raw memory/policy.json>" }`.

## V.21 GET /api/v3/agents/{agent_id}/memory/hierarchy

Hard-coded `{ "agent_id", "hierarchy": ["H0"], "mode": "none" }` in this control-plane snapshot.

## V.22 POST /api/v3/agents/{agent_id}/memory/query

Query params `tenant` (default `t`), `subject` (default `s`), optional `text`. Returns `{ "records": [...] }`. Cross-tenant query is empty list, not an error.

```powershell
Invoke-RestMethod -Method POST -Headers $H `
  "$base/api/v3/agents/$agent/memory/query?tenant=t1&subject=s1"
```

## V.23 POST /api/v3/agents/{agent_id}/memory/write-candidate

Query `tenant`, `subject`, `text`. Reads folder memory mode. Template `mode: none` → `MEM_TRUST_TIER`. Success `{ "memory_id": "..." }`.

## V.24 POST /api/v3/agents/{agent_id}/memory/consolidate

Enqueues `{ "kind": "offline" }`. Does **not** drain.

```json
{ "queued": true, "queue_depth": 1 }
```

Drain is `ConsolidationWorker.run_offline()` in the consolidation-worker process only.

## V.25 DELETE /api/v3/agents/{agent_id}/memory/{memory_id}

Required query `tenant` and `subject`. Wrong scope → `MEM_SCOPE`. Success `{ "tombstoned": true, "memory_id": "..." }`. Also `cache.on_memory_delete`.

## V.26 POST /api/v3/agents/{agent_id}/memory/{memory_id}/verify-deletion

Required tenant+subject. Returns the memory service probe result.

## V.27 GET /api/v3/traces/{trace_id}

`state.runtime.runs[trace_id].as_dict()`. Missing key is an uncaught KeyError unless a run happened in this process. RunResult fields:

```json
{
  "agent_id": "...",
  "root_trace_id": "tr_...",
  "trace": {},
  "artifact": { "id": "art_...", "text": "...", "digest": "..." },
  "containment_stop": null,
  "memory_writes": [],
  "safety": {},
  "cancelled": false,
  "adapter": "local_deterministic"
}
```

There is **no** `status` field on `RunResult`.

## V.28 POST /api/v3/traces/{trace_id}/replay

Optional query `counterfactual`. Returns:

```json
{
  "trace_id": "...",
  "counterfactual": false,
  "memory_writes": [],
  "equivalence": "observation",
  "root_trace_id": "tr_..."
}
```

Replay does not write memory.

## V.29 GET /api/v3/traces/{trace_id}/root-cause

`{ "trace_id", "cause": "none", "adapter": "<run.adapter>" }`.

## V.30 GET /api/v3/artifacts/{artifact_id}/evidence-graph

`state.runtime.artifacts[artifact_id]["evidence_graph"]` with `claims` and `unsupported`.

## V.31 GET /api/v3/agents/{agent_id}/safety/incidents

`{ "agent_id", "incidents": [] }` from in-memory `state.incidents`.

## V.32 POST /api/v3/agents/{agent_id}/safety/redteam

Appends `{ "agent_id", "suite": "baseline" }` and returns `{ "agent_id", "ran": true }`.

## V.33 GET /api/v3/agents/{agent_id}/improvement/candidates

`{ "agent_id", "candidates": [ ... ] }` from `state.candidates`.

## V.34 POST /api/v3/agents/{agent_id}/improvement/candidates/{cid}/evaluate

Sets `{ "id": cid, "agent_id", "state": "EVALUATED" }`.

## V.35 POST /api/v3/agents/{agent_id}/improvement/candidates/{cid}/approve

Requires mutation headers **and** actor `independent_approver`. Sets `HUMAN_APPROVED` and appends ledger `{ "type": "approve", "cid", "actor" }`.

## V.36 POST /api/v3/agents/{agent_id}/improvement/rollback/{version}

Appends ledger `{ "type": "rollback", "version", "agent_id" }`, returns `{ "rolled_back": "<version>" }`.

## V.37 GET /api/v3/agents/{agent_id}/improvement/ledger

`{ "agent_id", "ledger": [ ... ] }`.

## V.38 GET /api/v3/agents/{agent_id}/regression/suite

`{ "agent_id", "fixtures": [ filenames in evals/regression ] }`.

## V.39 GET /api/v3/agents/{agent_id}/corrigibility/attestation

Host-owned:

```json
{
  "agent_id": "...",
  "digest": "<hex>",
  "signature": "<hex>",
  "status": "host_reference",
  "invariant_set_id": "..."
}
```

The agent folder cannot rewrite this.

## V.40 GET /api/v3/agents/{agent_id}/validation/report

`evaluate(instruments, agent_id=...)`. Default unqualified instruments:

```json
{
  "verdict": "NOT_RUN",
  "pass": false,
  "reason": "unqualified_instruments"
}
```

UI must not style this as a green pass. `INDICATIVE` screening is also not a release pass.

## V.41 POST /api/v3/agents/{agent_id}/runtime/run

Executes `Runtime.execute`. Template DAG in `runtime/execution.json` with local deterministic adapter unless the host LLM router is used for model nodes. Returns `RunResult.as_dict()`. Expect `containment_stop: null`, `memory_writes: []` on the template. `root_trace_id` prefix `tr_`. Artifact id prefix `art_`.

```powershell
$run = Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/agents/$agent/runtime/run"
$run.root_trace_id
$run.artifact.id
$run.adapter
$run.containment_stop
```

## V.42 POST /api/v3/agents/{agent_id}/runtime/chat

Body:

```json
{
  "message": "hello",
  "history": [
    { "role": "user", "content": "prior" },
    { "role": "assistant", "content": "prior reply" }
  ]
}
```

`history` omitted or non-list becomes `[]`. Server `normalize_history` keeps last 20 user/assistant turns with non-empty content. Empty message → `CTX_BUDGET` `"chat message required"`. Message longer than 32000 characters → `CTX_BUDGET` `"chat message exceeds context budget"`.

Response:

```json
{
  "agent_id": "...",
  "reply": "...",
  "provider": "xai",
  "digest": "<sha256 hex>",
  "io": {},
  "memory_writes": [],
  "plugins_executed": false,
  "t3_enabled": false,
  "used_prompt_reference": "prompts/primary.md",
  "safety": {}
}
```

System prompt is folder `prompt_reference` (fallback `prompts/primary.md`) plus declared I/O plus the human-operator free-text instruction. Host LLM router uses `budget_policy.max_output_tokens` (default 512). Chat does not write memory, does not execute plugins, does not enable T3.

UI Chat sends `reasonFallback: "operator chat"` so a blank Settings reason still mutates.

---

# Part VI — Non-v3 HTTP

## VI.1 GET /health

`{ "status": "ok", "service": "control-plane" }`. UI polls this. Not in OpenAPI. UI API logger skips `/health`.

## VI.2 POST /debug/logs

Operator sink. Body:

```json
{
  "session": "2026-09-02-12-00-00-000-abc123",
  "entries": [
    {
      "channel": "api",
      "ts": "2026-09-02T12:00:00.000Z",
      "level": "info",
      "message": "GET /api/v3/agents 200 12ms",
      "detail": "{}"
    }
  ]
}
```

Session must match `^[A-Za-z0-9._-]{1,80}$`. Channel must be `api` or `ui`. Writes JSONL to `CASOPS_LOG_ROOT` (default `logs/debug`) as `{session}-api.log` and `{session}-ui.log`. Fields clipped at 8000 characters. Max 200 entries per POST. Returns `{ "ok": true, "files": { "api": "<path>", "ui": "<path>" } }` only for files that exist.

UI: `ui/src/log/bus.ts` + `persist.ts`. Skip logging of `/health` and `/debug/`. Header ScrollText icon opens the log drawer.

## VI.3 POST /debug/chat

```json
{
  "agent_id": "common.health",
  "session": "2026-09-02-12-00-00-000-chat1",
  "entries": [
    { "role": "user", "ts": "2026-09-02T12:00:00.000Z", "content": "ping", "provider": "" },
    { "role": "assistant", "ts": "2026-09-02T12:00:01.000Z", "content": "pong", "provider": "xai" }
  ]
}
```

Writes `CASOPS_CHAT_ROOT` (default `logs/chat`) / `{agent_id}` / `{session}.jsonl`. Returns `{ "ok": true, "files": { "transcript": "<path>" } }`.

## VI.4 GET /debug/chat?agent_id=

Lists up to 50 `*.jsonl` files newest-first with `path`, `name`, `ts` (UTC mtime ISO), `bytes`.

---

# Part VII — Control UI, every surface

## VII.1 Shell

`ui/src/App.tsx` wraps `ThemeProvider` → `SessionProvider` → `BrowserRouter` → `AppShell` outlet.

Routes (complete):

| path | page |
|---|---|
| `/` | Fleet (`FleetPage`) |
| `/org-chat` | Agent Org Chat |
| `/workflow` | Main Workflow (`video.workflow.svg`) |
| `/workflow/sub` | Sub Workflow (Template A–J, Scale S1–S7) |
| `/settings` | Settings |
| `/help` | Full-page Help |
| `/traces/:tid` | Trace |
| `/agents/:agentId` | Overview |
| `/agents/:agentId/chat` | Chat |
| `/agents/:agentId/structure` | Structure |
| `/agents/:agentId/compose` | Compose |
| `/agents/:agentId/run` | Run |
| `/agents/:agentId/traces` | Trace |
| `/agents/:agentId/traces/:tid` | Trace |
| `/agents/:agentId/capabilities` | Capabilities |
| `/agents/:agentId/protocols` | Protocols |
| `/agents/:agentId/memory` | Memory |
| `/agents/:agentId/plugins` | Plugins |
| `/agents/:agentId/cache` | Cache |
| `/agents/:agentId/safety` | Safety |
| `/agents/:agentId/improvement` | Improvement |
| `/agents/:agentId/validation` | Validation |
| `/agents/:agentId/corrigibility` | Corrigibility |
| `*` | Navigate to `/` |

Header, left to right: hamburger (md hidden), home mark (indigo 7×7 Network icon) + wordmark **Agent Swarm**, agent search combobox, then icons: BookOpen (full-page docs), ScrollText (logs), PanelRight (help), Sun/Moon (theme), StatusPill.

Left nav labels: Agent Swarm, Agent Org Chat, Agent Workflow (Main Workflow, Sub Workflow), Agent Profile (the AGENT_TABS list), Settings.

Location heading is `locationLabel(pathname)`, for example `Agent Swarm / agents/video.director/chat`.

localStorage keys:

| key | content |
|---|---|
| `casops.control-ui.settings.v1` | baseUrl, knownIds, pollMs, persistActor, defaultActor, defaultDryRun |
| `casops.control-ui.actor.v1` | actor, reason, expectedParent, dryRun (sessionStorage always; localStorage if persistActor) |
| `casops.control-ui.nav.v1` | collapsed, agentOpen, workflowOpen |
| `casops.control-ui.help-width.v1` | help drawer width 280–720, default 380 |
| `casops.control-ui.log-width.v1` | log drawer width, same clamp |
| `casops.control-ui.theme.v1` | `light` or `dark` |
| `casops.control-ui.chat.v1` | per-agent `{ session, turns, files }` |

## VII.2 Theme

Default light. Moon icon switches to dark (`html.dark`, `color-scheme: dark`). Sun switches back. Inline script in `ui/index.html` applies stored dark class before paint. Tokens remap stone/white surfaces. Primary buttons invert in dark (`dark:bg-stone-100 dark:text-stone-900`). Status pills have `dark:` backgrounds.

## VII.3 Help

BookOpen navigates to `/help?from=<urlencoded current path>`. PanelRight toggles the right drawer. Opening Help closes Logs and vice versa. Drawer is sticky, viewport-tall; document region `overflow-y-auto overscroll-contain` so it scrolls independently of the page.

Tabs: Spec (`spec.md`), User guide (`userguide.md`). Resolution `docCandidates`:

1. `/docs<exact-route>/<tab>.md`
2. if agentId present: `/docs/agents/<agentId>/<tab>.md`
3. `/docs<param-stripped-route>/<tab>.md`
4. for `/`, also `/docs/index/<tab>.md`

Per-agent files are generated by `python tools/generate_help_agent_docs.py` from `agents/<folder>/docs` (userguide) and merged `SPEC.md` + `agent_spec.json` + `prompts/` + `rubrics/` + `sources/` (spec). HTML/404 treated as missing. Soft miss continues to next candidate.

## VII.4 Logs

ScrollText opens API log / UI log. API lines: `METHOD /path STATUS duration` plus clipped JSON detail. UI lines: navigate, chat send/reply, run, console warn/error (React Router future flags filtered). Session id in footer. Files `logs/debug/<session>-api.log` and `-ui.log`.

## VII.5 Fleet (`/`)

Loads `GET /api/v3/agents`. Filter input (agent_id, role, folder, category). Pack chips: All, specials, video, other (`agentPack` from id prefix). Category `<select>` options are only values that exist on the current pack slice. Cards: agent_id, Common v3.0 badge, role, compose/last run/memory wells, Open, Compose preview. Count `{visible} of {listed} agents`. Poll interval from Settings (default 15000 ms). Empty: “No agents” / control plane unavailable.

## VII.6 Overview (`/agents/:id`)

Operator contract fields: Actor select, Reason, Expected parent. Dry-run is on Run/Compose strips. Attestation card from GET attestation. Structure snapshot. LLM card (resolved provider, override). I/O panel. Actions: Compose preview, Run, Chat.

## VII.7 Chat (`/agents/:id/chat`)

Textarea `#agent-chat-input`, Send disabled until `healthOk && !stale && !containment` and draft non-empty. Enter sends, Shift+Enter newline. History per agent in localStorage, timestamps on bubbles, last 20 turns sent as `history`. Transcripts listed under Saved transcripts. Clear starts a new session id and does not delete JSONL files. Files at `logs/chat/<agent_id>/<session>.jsonl` each line `{ ts, role, content, provider }`.

## VII.8 Structure, Compose, Run, Trace

Structure: folder path, schema, I/O, spec snapshot JSON. Compose: POST compose-preview, show hash, findings, errors, `wrote_locks`. Run: dry-run control, Invalidate cache, Run; shows plan nodes and last `RunResult` (adapter, cancelled, containment_stop, artifact). Trace: load by id, replay, counterfactual query, root-cause, evidence graph.

## VII.9 Capabilities through Corrigibility

Each page GETs its v3 path and renders JSON plus honesty rules: `NOT_RUN` / `INDICATIVE` not green; `ASSERTED_UNVERIFIED` not bindable; memory write disabled when mode is `none`; approve only `independent_approver`. Plugins validate with `executed: false`. Safety lists incidents and can POST redteam. Improvement evaluate/approve/rollback/ledger. Validation report. Corrigibility attestation digest/signature/host_reference.

## VII.10 Org Chat (`/org-chat`)

Read-only org chart of critique edges. Not operator Chat. Does not send `runtime/chat`.

## VII.11 Workflow

Main: embed `ui/public/svg/video.workflow.svg`. Clicks on `a.agent-link` go to `/agents/{id}/chat`. Sub: combobox Template A–J then Scale S1–S7, corresponding SVGs under `ui/public/svg/`.

## VII.12 Settings

Base URL (empty = Vite proxy). Poll ms. Default actor. Default dry-run. Persist actor. DEFAULT_LLM select from GET llm/settings; POST with mutation headers. Known agent IDs textarea (newline separated) used when list is empty.

## VII.13 Status pills

Never color alone. Kinds: live, running, queued, self_refine, delayed, reconnecting, degraded, failed, recovery, complete, unavailable, stale, cancelled. Header pill: live when health ok and last v3 success < 5s; reconnecting on UNAVAILABLE; etc.

---

# Part VIII — Step-by-step API usage (do in this order)

Work from repo root. Control plane must already answer `/health`.

### Step 1 — Header block

Use the `$base`, `$agent`, `$H` block from Part III.4.

### Step 2 — Health

```powershell
Invoke-RestMethod "$base/health"
```

Expect `status=ok`, `service=control-plane`.

### Step 3 — List agents

```powershell
(Invoke-RestMethod "$base/api/v3/agents").agents |
  Select-Object agent_id, role, va_category, memory_mode |
  Format-Table
```

Confirm `casops.template.baseline_safe` and `common.health` are present. Count equals the number of `agents/*/agent_spec.json` folders.

### Step 4 — Structure

```powershell
Invoke-RestMethod "$base/api/v3/agents/$agent/structure" | ConvertTo-Json -Depth 8
```

Expect `structure_id` `casops.common_agent.v3`, `schema_version` `3.0`.

### Step 5 — Attestation

```powershell
Invoke-RestMethod "$base/api/v3/agents/$agent/corrigibility/attestation" | ConvertTo-Json
```

`status` is `host_reference`. Digest and signature are host-owned.

### Step 6 — Unsigned POST (negative)

```powershell
curl.exe -i -X POST "$base/api/v3/agents/$agent/compose-preview"
```

Not HTTP 200. Body `error.code` `IMP_UNSIGNED`.

### Step 7 — Compose-preview

```powershell
$prev = Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/agents/$agent/compose-preview"
$prev.compose_hash
$prev.wrote_locks
$prev.errors
```

`compose_hash` length 64. `wrote_locks` false. `errors` empty.

### Step 8 — Run

```powershell
$run = Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/agents/$agent/runtime/run"
$run | ConvertTo-Json -Depth 10
```

Record `root_trace_id`, `artifact.id`. `containment_stop` null. `memory_writes` `[]`. `cancelled` false. Adapter `local_deterministic` on the template unless a model node used the host router.

### Step 9 — Trace and evidence

```powershell
$tid = $run.root_trace_id
$aid = $run.artifact.id
Invoke-RestMethod "$base/api/v3/traces/$tid" | ConvertTo-Json -Depth 10
Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/traces/$tid/replay" | ConvertTo-Json
Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/traces/${tid}/replay?counterfactual=route" | ConvertTo-Json
Invoke-RestMethod "$base/api/v3/traces/$tid/root-cause"
Invoke-RestMethod "$base/api/v3/artifacts/$aid/evidence-graph" | ConvertTo-Json -Depth 8
```

Replay `memory_writes` remains `[]`.

### Step 10 — Memory write must fail on template

```powershell
try {
  Invoke-RestMethod -Method POST -Headers $H `
    "$base/api/v3/agents/$agent/memory/write-candidate?tenant=t1&subject=s1&text=hello"
} catch {
  $_.ErrorDetails.Message
}
```

Expect `MEM_TRUST_TIER`.

### Step 11 — Plugins validate without exec

```powershell
Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/agents/$agent/plugins/validate" | ConvertTo-Json -Depth 6
```

`executed` is false.

### Step 12 — Validation honesty

```powershell
Invoke-RestMethod "$base/api/v3/agents/$agent/validation/report" | ConvertTo-Json -Depth 8
```

`verdict` `NOT_RUN`, `pass` false, `reason` `unqualified_instruments`.

### Step 13 — Self-approval denied

```powershell
$bad = @{
  "x-casops-actor" = "agent_runtime"
  "x-casops-reason" = "should-fail"
  "x-casops-expected-parent" = "none"
  "x-casops-dry-run" = "true"
}
try {
  Invoke-RestMethod -Method POST -Headers $bad `
    "$base/api/v3/agents/$agent/improvement/candidates/c1/approve"
} catch { $_.ErrorDetails.Message }
```

Expect `IMP_SELF_APPROVAL`.

### Step 14 — Chat

```powershell
$body = '{"message":"ping from the book","history":[]}'
Invoke-RestMethod -Method POST -Headers $H -ContentType "application/json" `
  -Body $body "$base/api/v3/agents/common.health/runtime/chat" | ConvertTo-Json -Depth 8
```

Expect `reply` string, `memory_writes: []`, `plugins_executed: false`, `t3_enabled: false`.

### Step 15 — Debug transcript list

```powershell
Invoke-RestMethod "$base/debug/chat?agent_id=common.health"
```

### Step 16 — Eval CLI

```powershell
$env:PYTHONPATH = "src"
python -m casops.eval
```

Exit 2. `pass: false`.

### Step 17 — LLM providers

```powershell
Invoke-RestMethod "$base/api/v3/llm/providers" | ConvertTo-Json -Depth 6
```

---

# Part IX — Step-by-step UI usage

Prerequisite: `scripts/start_all.ps1` succeeded. Browser `http://127.0.0.1:15173`. Header pill **Live**.

### Step 1 — Fleet

You are on Agent Swarm. Confirm the count label `{n} of {n} agents` matches loaded folders. Type `director` in the filter. Click pack **video**. If category chips exist, they are only `va_category` values from those cards. Click **Open** on `video.director`.

### Step 2 — Overview / operator contract

Set Actor `human_operator` or `host_service`. Type a Reason (required before Run/Compose mutations). Leave Expected parent `none` for first use. Dry-run defaults on (Settings). Read attestation status `host_reference`. Click **Chat**.

### Step 3 — Chat

Type a message. Send. Wait for the assistant bubble. Timestamp appears under each bubble. Saved transcripts appear in the left column after the file sink returns. Reload the page: the same bubbles return. Switch the header combobox to `common.health` then back to `video.director`: histories stay separate. Clear starts a new conversation; old JSONL files remain listed.

### Step 4 — Help

Click PanelRight. Spec tab shows merged `agent_spec.json` + `SPEC.md` + prompts + rubrics + sources for **this** agent. User guide tab shows copied `docs/user_guide.md`. Scroll inside the drawer; the page does not move. Drag the left edge to resize (280–720). Click BookOpen for the full page `/help?from=...`. Close Help.

### Step 5 — Logs

Click ScrollText. API log shows GET/POST lines with status and duration. UI log shows `navigate` and `chat send` / `chat reply`. Footer session id matches files under `logs/debug/`. Close Logs.

### Step 6 — Theme

Moon → dark (`html.dark`). Reload stays dark. Sun → light.

### Step 7 — Compose then Run

Open Compose. With reason filled and dry-run on, click compose-preview. Confirm 64-char hash and `wrote_locks` false. Open Run. Click Run. Inspect adapter, artifact, containment_stop. Open Trace with the `root_trace_id`. Replay. Counterfactual is the same path with a query string, not a different DAG.

### Step 8 — Validation

Open Validation. Read `NOT_RUN` / `pass: false`. Do not treat as a pass.

### Step 9 — Memory

Open Memory. Policy `mode: none` on the template. Write candidate stays disabled / fails. Do not enable memory writes from the UI for production.

### Step 10 — Settings

Base URL empty uses the Vite proxy. Do not paste host Ed25519 keys or provider secrets into Known agent IDs. DEFAULT_LLM POST is a mutation (needs reason). Preview default LLM is dry-run.

### Step 11 — Workflow

Agent Workflow → Main Workflow. When the SVG loads, click a labeled agent; you land on that agent’s Chat. Sub Workflow: pick Template A–J or Scale S1–S7.

### Step 12 — Org Chat

Read-only. Use it to see critique edges, not to send operator chat.

### Step 13 — Stop

```powershell
powershell -File scripts/stop_all.ps1
```

---

# Part X — Environment variables

| name | default | effect |
|---|---|---|
| `PYTHONPATH` | (unset) | Must include `src` if not installed editable on PATH |
| `CASOPS_AGENTS_ROOT` | `agents` | Folder scan root |
| `CASOPS_LLM_SETTINGS` | `var/llm-settings.json` | Persisted default_llm + per-agent overrides |
| `CASOPS_CORS_ORIGINS` | empty | Extra CORS origins, comma-separated |
| `CASOPS_LOG_ROOT` | `logs/debug` | Debug JSONL directory |
| `CASOPS_CHAT_ROOT` | `logs/chat` | Chat JSONL directory |
| `DEFAULT_LLM` | resolved as in V.2 | Host default provider id |
| `OPENAI_API_KEY` `OPENAI_BASE_URL` `OPENAI_MODEL` | catalog defaults | OpenAI-compat |
| `XAI_API_KEY` `XAI_BASE_URL` `XAI_MODEL` | `https://api.x.ai/v1`, `grok-4` | xAI |
| `ANTHROPIC_API_KEY` `ANTHROPIC_BASE_URL` `ANTHROPIC_MODEL` | catalog defaults | Anthropic |
| `VITE_CASOPS_BASE` | empty | UI default baseUrl if set at build |
| `CASOPS_PUBLIC_PREFIX` | `/api/v3` | Docker control-plane |
| `CASOPS_ROLE` | per service | Docker role label |
| `CASOPS_CORRIGIBILITY_DATA` `CASOPS_CORRIGIBILITY_KEY` | Docker volumes | Invariant service |

`.env` files are loaded if present; existing process env wins (`key not in os.environ`).

---

# Part XI — Eight-process deployment

Copied from `deploy/dev/docker-compose.yml` as shipped:

- `corrigibility-invariant-service` expose 8081, volume `corrigibility-data`
- `instrument-registry-service` volume `instrument-data`
- `compose-service` expose 8082, agents root read-only, locks volume
- `runtime-service` runtime-data + artifacts
- `memory-service` memory-data
- `consolidation-worker` same memory-data, reserved 1 CPU / 1G; **only this process drains consolidate**
- `trainer-bridge` trajectories volume; **no inbound gradient socket into runtime**
- `control-plane` **published** `18080:18080`

```powershell
docker compose -f deploy/dev/docker-compose.yml up --build
curl.exe http://127.0.0.1:18080/health
```

Typical internal ports (not the public plane): 8081 corrigibility, 8082 compose, 8083 instruments, 8084 runtime, 8085 memory, 8086 consolidation, 8087 trainer.

---

# Part XII — CLIs

`casops-eval` / `python -m casops.eval`: default status exit 2, `pass: false`, `unqualified_instruments`.  
`python -m casops.eval run --tier screening --agent casops.template.baseline_safe`: `INDICATIVE`, still `pass: false`.  
`python -m casops.eval run --tier confirmatory --agent casops.template.baseline_safe --citation docs/citation/citation-audit.json --out evals/reports/local/report.json`: powered n binary floor 400, plan-frozen, unqualified instruments still cannot pass.

`casops-citation` / `python -m casops.citation --verified-by your-id`: needs network. Writes `evals/reports/citation-audit/citation-audit.json` and `docs/citation/citation-audit.json`. Exit 0 only if `cleared=true`.

L5 is Python-only `casops.improvement.l5.ResearchIsolation`. `promote_to_production` always `IMP_SCOPE`. `agent_runtime` cannot mutate. Production keys must not be in the process env.

---

# Part XIII — Forbidden operations (complete list you must not do from this UI or public plane)

- Set `production_activation_requested` to true from the Control UI (there is no control).
- Enable T3 from the UI (there is no control). `enable_t3` exists in the cache manager behind an independent verifier and ≤0.5% false-reuse harness; default remains off.
- Promote L5 research isolation into the serving tree.
- Call internal 8081–8087 from the browser.
- Send mutation headers with `x-casops-actor: agent_runtime` on approve or invariant writes.
- Treat `NOT_RUN` or `INDICATIVE` as a green pass.
- Treat Org Chat as operator Chat.
- Expect compose-preview to write locks (`wrote_locks` is always false on this plane).
- Expect consolidate to drain on the serving path.
- Expect plugins/validate to execute plugin code (`executed: false`).
- Store provider API keys in `agent_spec.json` or in Settings known-ids.
- Invent `va_category` values in the UI that are not on loaded specs.

---

# Part XIV — UI client mutation header injection

`ui/src/api/v3.ts` `createClient`:

- GET: `Accept: application/json` only.
- POST/PUT/PATCH/DELETE: adds `x-casops-actor`, `x-casops-reason`, `x-casops-expected-parent`, `x-casops-dry-run` from session. If reason is blank, uses `reasonFallback` when provided (Chat: `"operator chat"`).
- JSON body when `body` is set.
- Abort after timeout.
- Logs via `logApi` unless `shouldSkipApiLog` (`/health` or path starts with `/debug/`).
- Non-OK → `CasopsHttpError`. Network throw → `UNAVAILABLE` status 0.

---

# Part XV — Help and log generation commands

```powershell
python tools/generate_help_agent_docs.py
```

Writes `ui/public/docs/agents/<agent_id>/spec.md` and `userguide.md` for every folder with `agent_spec.json`.

```powershell
python tools/write_casops_complete_book.py
```

Regenerates this book.

---

'''


def fence(lang: str, text: str) -> str:
    ticks = "```"
    while ticks in text:
        ticks += "`"
    return f"{ticks}{lang}\n{text.rstrip()}\n{ticks}\n\n"


def copy_file(rel: str, *, lang: str | None = None) -> str:
    path = REPO / rel.replace("/", "\\") if "\\" in rel else REPO.joinpath(*rel.split("/"))
    if not path.is_file():
        return f"### `{rel}`\n\n(file missing from this checkout)\n\n"
    suffix = path.suffix.lower()
    if lang is None:
        lang = {
            ".py": "python",
            ".ts": "typescript",
            ".tsx": "tsx",
            ".json": "json",
            ".toml": "toml",
            ".yml": "yaml",
            ".yaml": "yaml",
            ".ps1": "powershell",
            ".md": "markdown",
            ".css": "css",
            ".html": "html",
            ".js": "javascript",
        }.get(suffix, "text")
        if suffix == ".md":
            lang = "markdown"
    body = path.read_text(encoding="utf-8")
    heading = f"### `{rel}` ({path.stat().st_size} bytes)\n\n"
    if suffix == ".md":
        return heading + body.rstrip() + "\n\n"
    return heading + fence(lang, body)


def iter_py(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files.append(path)
    return files


def copied_host_library() -> str:
    parts = ["# Part XIX — Complete host library (`src/casops/`)\n\n"]
    parts.append(
        "Every Python module under `src/casops/` is copied below. Empty `__init__.py` files are included so the package tree is complete.\n\n"
    )
    root = REPO / "src" / "casops"
    for path in iter_py(root):
        rel = path.relative_to(REPO).as_posix()
        parts.append(copy_file(rel))
    return "".join(parts)


def copied_ui_source() -> str:
    parts = ["# Part XX — Complete Control UI source (`ui/src/` plus config)\n\n"]
    for rel in [
        "ui/package.json",
        "ui/tsconfig.json",
        "ui/vite.config.ts",
        "ui/tailwind.config.js",
        "ui/postcss.config.js",
        "ui/index.html",
        "ui/README.md",
    ]:
        parts.append(copy_file(rel))
    root = REPO / "ui" / "src"
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix in {".ts", ".tsx", ".css"}:
            parts.append(copy_file(path.relative_to(REPO).as_posix()))
    return "".join(parts)


def copied_ui_tests() -> str:
    parts = ["# Part XXI — Control UI unit tests (`ui/tests/`)\n\n"]
    root = REPO / "ui" / "tests"
    if not root.is_dir():
        return "".join(parts)
    for path in sorted(root.rglob("*")):
        if path.is_file():
            parts.append(copy_file(path.relative_to(REPO).as_posix()))
    return "".join(parts)


def copied_host_tests() -> str:
    parts = ["# Part XXII — Host tests (`tests/`)\n\n"]
    root = REPO / "tests"
    for path in iter_py(root):
        parts.append(copy_file(path.relative_to(REPO).as_posix()))
    return "".join(parts)


def copied_services() -> str:
    parts = ["# Part XXIII — Eight process services (`services/`)\n\n"]
    root = REPO / "services"
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() in {".py", ".md"} or path.name == "Dockerfile":
            lang = "dockerfile" if path.name == "Dockerfile" else None
            parts.append(copy_file(path.relative_to(REPO).as_posix(), lang=lang))
    return "".join(parts)


def copied_operator_docs() -> str:
    parts = [
        "# Part XXIV — Operator and implementer documents (complete copies)\n\n",
        "These files are copied in full so this book does not send you elsewhere.\n\n",
    ]
    for rel in [
        "README.md",
        "pyproject.toml",
        "user_guide.v1.md",
        "implementation_status.md",
        "spec/help_spec.md",
        "spec/ui.v1.md",
        "docs/adr/README.md",
        "deploy/dev/docker-compose.yml",
        "scripts/start_all.ps1",
        "scripts/stop_all.ps1",
        "schemas/locks/compose.lock.schema.json",
        "errors/catalogue.json",
    ]:
        parts.append(copy_file(rel))
    return "".join(parts)


def copied_structure_spec() -> str:
    parts = [
        "# Part XXV — Common-agent structure specification (complete copy of `spec/common_agent_structure.v3.md`)\n\n"
    ]
    parts.append(copy_file("spec/common_agent_structure.v3.md"))
    return "".join(parts)


def copied_implementation_plan() -> str:
    parts = ["# Part XXVI — Implementation plan (complete copy of `implementation_plan.md`)\n\n"]
    parts.append(copy_file("implementation_plan.md"))
    return "".join(parts)


def copied_evaluation_plan() -> str:
    parts = ["# Part XXVII — Evaluation plan (complete copy of `evaluation_plan.md`)\n\n"]
    parts.append(copy_file("evaluation_plan.md"))
    return "".join(parts)


def copied_root_structure_md() -> str:
    parts = [
        "# Part XXVIII — Root `common_agent_structure.md` (complete copy)\n\n",
        "README names this file as the source specification identifier `CASOPS-FS-COMMON-AGENT-STRUCTURE-V3A`. It is copied here in full, including any drafting notes present at the top of the file.\n\n",
    ]
    parts.append(copy_file("common_agent_structure.md"))
    return "".join(parts)


def copied_generic_help() -> str:
    parts = [
        "# Part XXIX — Generic Help markdown served by the Control UI\n\n",
        "Per-agent Help files at `ui/public/docs/agents/<agent_id>/spec.md` and `userguide.md` are generated from each agent folder by `python tools/generate_help_agent_docs.py`. They are large (some hundreds of kilobytes) and would duplicate the inventory plus each agent’s own `SPEC.md`. This part copies every **generic** screen document (no dot in the last folder name, plus root Help files). After you finish this book you already know the resolver order; open the generated per-agent files on disk when you need that agent’s SPEC text.\n\n",
    ]
    docs = REPO / "ui" / "public" / "docs"
    keep: list[Path] = []
    for path in sorted(docs.rglob("*.md")):
        rel = path.relative_to(docs).as_posix()
        parts_path = rel.split("/")
        if parts_path[0] == "agents" and len(parts_path) >= 3:
            folder = parts_path[1]
            if "." in folder:
                continue
        keep.append(path)
    for path in keep:
        rel = path.relative_to(REPO).as_posix()
        parts.append(copy_file(rel))
    return "".join(parts)


def copied_template_docs() -> str:
    parts = ["# Part XXX — Template agent documents (complete copies from `agents/_template_v3/`)\n\n"]
    root = REPO / "agents" / "_template_v3"
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() in {".md", ".json", ".txt"}:
            parts.append(copy_file(path.relative_to(REPO).as_posix()))
    return "".join(parts)


def copied_book_of_knowledge() -> str:
    parts = [
        "# Part XXXI — Book of Knowledge (complete copy of `spec/book_of_knowledge.md`)\n\n",
        "This file is a domain bibliography (English and Chinese titles with ISBN-13) for the specials and video agent packs. It is not a host runtime document. It is copied because it is part of this repository and this book is required to contain the project, not a pointer to it.\n\n",
    ]
    parts.append(copy_file("spec/book_of_knowledge.md"))
    return "".join(parts)


def copied_tools() -> str:
    parts = ["# Part XXXII — Repository tools that operators actually run\n\n"]
    for rel in [
        "tools/generate_help_agent_docs.py",
        "tools/write_adrs.py",
        "tools/write_template_agent.py",
        "tools/write_source_identity.py",
        "tools/write_ui_svgs.py",
        "tools/attach_book_of_knowledge.py",
        "tools/import_video_agents.py",
        "tools/import_specials_agents.py",
        "scripts/generate_video_workflows.py",
    ]:
        parts.append(copy_file(rel))
    return "".join(parts)


NARRATIVE_3 = r'''
# Part VIII.A — Remaining API procedures (every remaining public path)

Continue from Part VIII Step 17. Same `$base`, `$agent`, `$H`. Agent is `casops.template.baseline_safe` unless a step says otherwise.

### Step 18 — Resolved compose view

```powershell
Invoke-RestMethod "$base/api/v3/agents/$agent/resolved" | ConvertTo-Json -Depth 12
```

Fields: `agent_id`, `mro` (list), `compose_hash` (64 hex), `lock` (object matching the compose.lock schema fields that the composer filled), `io.merged` true.

### Step 19 — Runtime plan and context budget

```powershell
Invoke-RestMethod "$base/api/v3/agents/$agent/runtime/plan"
Invoke-RestMethod "$base/api/v3/agents/$agent/runtime/context-budget"
```

`plan` and `budget` are **raw file text**, not parsed JSON, of `runtime/execution.json` and `runtime/context.json`.

### Step 20 — Capabilities matrix and verify

```powershell
Invoke-RestMethod "$base/api/v3/agents/$agent/runtime/capabilities" | ConvertTo-Json -Depth 10
Invoke-RestMethod "$base/api/v3/agents/$agent/capabilities/matrix" | ConvertTo-Json -Depth 10
Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/agents/$agent/capabilities/verify" | ConvertTo-Json -Depth 10
```

All three call `verify_folder`. `production_bindable` is not true for asserted-unverified rows.

### Step 21 — Cache stats then invalidate

```powershell
Invoke-RestMethod "$base/api/v3/agents/$agent/cache/stats" | ConvertTo-Json -Depth 8
Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/agents/$agent/cache/invalidate" | ConvertTo-Json
Invoke-RestMethod "$base/api/v3/agents/$agent/cache/stats" | ConvertTo-Json -Depth 8
```

Invalidate returns `{ "agent_id", "invalidated": true, "tiers": ["T0"] }` on the template. T3 is not in `tiers` while disabled.

### Step 22 — Protocols pin

```powershell
Invoke-RestMethod "$base/api/v3/agents/$agent/protocols"
```

`protocols` is raw `protocols/compatibility.json` text.

### Step 23 — Plugins GET and POST validate

```powershell
Invoke-RestMethod "$base/api/v3/agents/$agent/plugins" | ConvertTo-Json -Depth 8
$pv = Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/agents/$agent/plugins/validate"
$pv.executed
```

`$pv.executed` must be JSON boolean `false`.

### Step 24 — Memory policy, hierarchy, query (empty on template)

```powershell
Invoke-RestMethod "$base/api/v3/agents/$agent/memory/policy"
Invoke-RestMethod "$base/api/v3/agents/$agent/memory/hierarchy" | ConvertTo-Json
Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/agents/$agent/memory/query?tenant=t1&subject=s1" | ConvertTo-Json -Depth 8
```

Hierarchy in this snapshot is `{ "hierarchy": ["H0"], "mode": "none" }`. Query returns `{ "records": [] }` when nothing was written in this process. Cross-tenant query is also an empty list, not `MEM_SCOPE`.

### Step 25 — Memory write (already failed in Step 10), consolidate enqueue

```powershell
Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/agents/$agent/memory/consolidate" | ConvertTo-Json
```

`{ "queued": true, "queue_depth": <int> }`. Repeat the call; `queue_depth` increases. The serving process does not drain.

### Step 26 — Memory delete and verify-deletion (scope required)

```powershell
curl.exe -i -X DELETE -H "x-casops-actor: host_service" -H "x-casops-reason: walkthrough" -H "x-casops-expected-parent: none" -H "x-casops-dry-run: true" "$base/api/v3/agents/$agent/memory/mem_does_not_exist?tenant=t1&subject=s1"
```

Missing tenant/subject is a FastAPI 422, not a catalogue code. Wrong tenant/subject on a real record is `MEM_SCOPE`.

### Step 27 — Safety incidents and red-team

```powershell
Invoke-RestMethod "$base/api/v3/agents/$agent/safety/incidents" | ConvertTo-Json -Depth 6
Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/agents/$agent/safety/redteam" | ConvertTo-Json
Invoke-RestMethod "$base/api/v3/agents/$agent/safety/incidents" | ConvertTo-Json -Depth 6
```

Red-team appends `{ "agent_id", "suite": "baseline" }` to the in-memory list and returns `{ "ran": true }`. Incidents do not survive process restart.

### Step 28 — Improvement candidates, evaluate, approve (approver), ledger, rollback

```powershell
Invoke-RestMethod "$base/api/v3/agents/$agent/improvement/candidates" | ConvertTo-Json -Depth 6
Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/agents/$agent/improvement/candidates/c-book/evaluate" | ConvertTo-Json
$H2 = $H.Clone(); $H2["x-casops-actor"] = "independent_approver"
Invoke-RestMethod -Method POST -Headers $H2 "$base/api/v3/agents/$agent/improvement/candidates/c-book/approve" | ConvertTo-Json
Invoke-RestMethod "$base/api/v3/agents/$agent/improvement/ledger" | ConvertTo-Json -Depth 6
Invoke-RestMethod -Method POST -Headers $H "$base/api/v3/agents/$agent/improvement/rollback/v0" | ConvertTo-Json
```

Evaluate sets `state: EVALUATED`. Approve as `independent_approver` sets `HUMAN_APPROVED`. `human_operator` on approve is `IMP_SELF_APPROVAL`. Ledger is process-local.

### Step 29 — Regression suite filenames

```powershell
Invoke-RestMethod "$base/api/v3/agents/$agent/regression/suite" | ConvertTo-Json
```

`fixtures` is the sorted file names under `evals/regression/` or `[]`.

### Step 30 — LLM GET/POST host and per-agent

```powershell
Invoke-RestMethod "$base/api/v3/llm/settings" | ConvertTo-Json -Depth 8
Invoke-RestMethod -Method POST -Headers $H -ContentType "application/json" -Body '{"default_llm":"local_deterministic"}' "$base/api/v3/llm/settings" | ConvertTo-Json -Depth 8
Invoke-RestMethod "$base/api/v3/agents/$agent/llm" | ConvertTo-Json -Depth 8
Invoke-RestMethod -Method POST -Headers $H -ContentType "application/json" -Body '{"provider":"local_deterministic"}' "$base/api/v3/agents/$agent/llm" | ConvertTo-Json
Invoke-RestMethod -Method POST -Headers $H -ContentType "application/json" -Body '{"provider":"__default__"}' "$base/api/v3/agents/$agent/llm" | ConvertTo-Json
```

With `x-casops-dry-run: true`, `saved` is false and `var/llm-settings.json` is not rewritten. Unknown provider → `PERF_ROUTE_UNAVAILABLE`.

### Step 31 — OpenAPI contains only /api/v3

```powershell
$oa = Invoke-RestMethod "$base/openapi.json"
$oa.paths.PSObject.Properties.Name
```

Every path starts with `/api/v3`. `/health` and `/debug/logs` are absent.

### Step 32 — Debug logs POST

```powershell
$payload = @{
  session = "book-session-1"
  entries = @(
    @{ channel = "api"; ts = "2026-09-03T00:00:00.000Z"; level = "info"; message = "GET /api/v3/agents 200 1ms"; detail = "{}" }
    @{ channel = "ui"; ts = "2026-09-03T00:00:00.100Z"; level = "info"; message = "navigate /"; detail = "" }
  )
} | ConvertTo-Json -Depth 6
Invoke-RestMethod -Method POST -ContentType "application/json" -Body $payload "$base/debug/logs" | ConvertTo-Json -Depth 6
```

No mutation headers. Invalid session id → HTTP 400.

### Step 33 — Unknown agent

```powershell
try { Invoke-RestMethod "$base/api/v3/agents/does.not.exist/structure" } catch { $_.ErrorDetails.Message }
```

`INH_PARENT_MISSING`, HTTP 409, external `message` is the catalogue external string.

---

# Part VIII.B — Python httpx client that covers the same plane

```python
import json
import httpx

BASE = "http://127.0.0.1:18080"
AGENT = "casops.template.baseline_safe"
H = {
    "x-casops-actor": "host_service",
    "x-casops-reason": "operator-walkthrough",
    "x-casops-expected-parent": "none",
    "x-casops-dry-run": "true",
}

def show(title, resp):
    print(title, resp.status_code)
    try:
        print(json.dumps(resp.json(), indent=2)[:4000])
    except Exception:
        print(resp.text[:4000])

with httpx.Client(timeout=120.0) as c:
    show("health", c.get(f"{BASE}/health"))
    show("agents", c.get(f"{BASE}/api/v3/agents"))
    show("providers", c.get(f"{BASE}/api/v3/llm/providers"))
    show("llm settings", c.get(f"{BASE}/api/v3/llm/settings"))
    show("structure", c.get(f"{BASE}/api/v3/agents/{AGENT}/structure"))
    show("resolved", c.get(f"{BASE}/api/v3/agents/{AGENT}/resolved"))
    show("attestation", c.get(f"{BASE}/api/v3/agents/{AGENT}/corrigibility/attestation"))
    show("unsigned POST", c.post(f"{BASE}/api/v3/agents/{AGENT}/compose-preview"))
    show("compose-preview", c.post(f"{BASE}/api/v3/agents/{AGENT}/compose-preview", headers=H))
    show("plan", c.get(f"{BASE}/api/v3/agents/{AGENT}/runtime/plan"))
    show("budget", c.get(f"{BASE}/api/v3/agents/{AGENT}/runtime/context-budget"))
    show("caps", c.get(f"{BASE}/api/v3/agents/{AGENT}/capabilities/matrix"))
    show("caps verify", c.post(f"{BASE}/api/v3/agents/{AGENT}/capabilities/verify", headers=H))
    show("cache", c.get(f"{BASE}/api/v3/agents/{AGENT}/cache/stats"))
    show("invalidate", c.post(f"{BASE}/api/v3/agents/{AGENT}/cache/invalidate", headers=H))
    show("protocols", c.get(f"{BASE}/api/v3/agents/{AGENT}/protocols"))
    show("plugins", c.get(f"{BASE}/api/v3/agents/{AGENT}/plugins"))
    show("plugins validate", c.post(f"{BASE}/api/v3/agents/{AGENT}/plugins/validate", headers=H))
    show("mem policy", c.get(f"{BASE}/api/v3/agents/{AGENT}/memory/policy"))
    show("mem hierarchy", c.get(f"{BASE}/api/v3/agents/{AGENT}/memory/hierarchy"))
    show("mem query", c.post(f"{BASE}/api/v3/agents/{AGENT}/memory/query", headers=H, params={"tenant": "t1", "subject": "s1"}))
    show("mem write", c.post(f"{BASE}/api/v3/agents/{AGENT}/memory/write-candidate", headers=H, params={"tenant": "t1", "subject": "s1", "text": "hello"}))
    show("mem consolidate", c.post(f"{BASE}/api/v3/agents/{AGENT}/memory/consolidate", headers=H))
    show("run", c.post(f"{BASE}/api/v3/agents/{AGENT}/runtime/run", headers=H))
    show("chat", c.post(f"{BASE}/api/v3/agents/common.health/runtime/chat", headers=H, json={"message": "ping from the book", "history": []}))
    show("validation", c.get(f"{BASE}/api/v3/agents/{AGENT}/validation/report"))
    show("incidents", c.get(f"{BASE}/api/v3/agents/{AGENT}/safety/incidents"))
    show("redteam", c.post(f"{BASE}/api/v3/agents/{AGENT}/safety/redteam", headers=H))
    show("candidates", c.get(f"{BASE}/api/v3/agents/{AGENT}/improvement/candidates"))
    show("evaluate", c.post(f"{BASE}/api/v3/agents/{AGENT}/improvement/candidates/c1/evaluate", headers=H))
    bad = dict(H); bad["x-casops-actor"] = "agent_runtime"
    show("self-approve", c.post(f"{BASE}/api/v3/agents/{AGENT}/improvement/candidates/c1/approve", headers=bad))
    ok_h = dict(H); ok_h["x-casops-actor"] = "independent_approver"
    show("approve", c.post(f"{BASE}/api/v3/agents/{AGENT}/improvement/candidates/c1/approve", headers=ok_h))
    show("ledger", c.get(f"{BASE}/api/v3/agents/{AGENT}/improvement/ledger"))
    show("rollback", c.post(f"{BASE}/api/v3/agents/{AGENT}/improvement/rollback/v0", headers=H))
    show("regression", c.get(f"{BASE}/api/v3/agents/{AGENT}/regression/suite"))
    show("agent llm", c.get(f"{BASE}/api/v3/agents/{AGENT}/llm"))
    show("set llm dry", c.post(f"{BASE}/api/v3/llm/settings", headers=H, json={"default_llm": "local_deterministic"}))
```

If Step 8 already ran in this process, add:

```python
tid = run_json["root_trace_id"]
aid = run_json["artifact"]["id"]
show("trace", c.get(f"{BASE}/api/v3/traces/{tid}"))
show("replay", c.post(f"{BASE}/api/v3/traces/{tid}/replay", headers=H))
show("cf", c.post(f"{BASE}/api/v3/traces/{tid}/replay", headers=H, params={"counterfactual": "route"}))
show("rca", c.get(f"{BASE}/api/v3/traces/{tid}/root-cause"))
show("evidence", c.get(f"{BASE}/api/v3/artifacts/{aid}/evidence-graph"))
```

---

# Part IX.A — UI control catalogue (every screen, every control)

This expands Part VII. After this section you can sit at the browser and know which control does what. The TypeScript/TSX that implements these controls is copied in Part XX.

## Shell (`ui/src/shell/AppShell.tsx`)

- **Hamburger** (visible below `md`): opens the left nav overlay.
- **Home mark**: indigo 7×7 rounded square with Network icon; wordmark **Agent Swarm**; click navigates to `/`.
- **AgentSwitcher combobox**: type to filter loaded ids; choosing an id navigates to `/agents/{id}` (Overview). Extra ids from Settings known-ids appear if the list endpoint is empty.
- **BookOpen** `data-testid=help-open-docs`: navigates to `/help?from=<urlencoded current path>`.
- **ScrollText** `data-testid=log-toggle-drawer`: toggles Logs drawer; pressed when open; closes Help.
- **PanelRight** `data-testid=help-toggle-drawer`: toggles Help drawer; pressed when open; closes Logs.
- **Sun/Moon** `data-testid=theme-toggle`: light ↔ dark.
- **StatusPill** in the header: live / reconnecting / stale / unavailable / containment based on `/health` plus last v3 success age.
- **Left nav**:
  - Agent Swarm → `/`
  - Agent Org Chat → `/org-chat`
  - Agent Workflow group (`data-testid=nav-agent-workflow`), collapsible: Main Workflow `/workflow`, Sub Workflow `/workflow/sub`
  - Agent Profile group, collapsible: Overview, Chat, Structure, Compose, Run, Trace, Capabilities, Protocols, Memory, Plugins, Cache, Safety, Improvement, Validation, Corrigibility
  - Settings → `/settings`
- Nav collapse and group open state persist in `casops.control-ui.nav.v1`.
- **Page location** `data-testid=page-location` uses `locationLabel`.
- RecoveryBanner / containment banner when the host reports containment.

## Actor strip (`ui/src/components/ActorStrip.tsx`)

- **Operator contract** card `data-testid=operator-contract` on Overview:
  - Actor `<select id=actor-select>`: `human_operator`, `independent_approver`, `host_service`, `agent_runtime`, `plugin`, `peer_agent`
  - Reason `<input id=actor-reason>` required for mutations (Chat bypasses blank reason with fallback `"operator chat"`)
  - Expected parent `<input id=actor-expected-parent>` default `none`
- **Dry-run** `data-testid=dry-run` checkbox with lock icon when on. Title when on: `Dry-run still executes the DAG — this is not “no side effects”.` Present on Run and Compose, not on Overview.

## Fleet (`/`)

- Title **Agent Swarm**.
- Count `data-testid=fleet-count`: `{visible} of {listed} agents`.
- Filter input `aria-label=Filter agents`, placeholder `Filter by agent_id, role, folder, or category`.
- Category `<select data-testid=fleet-category-filter>` only if the current pack slice has non-empty `va_category` values. Option `All categories` plus those values. The UI never invents a category.
- Pack chips: All, specials, video, other. Pack is derived from `agent_id` prefix (`specials.`, `video.`, else other).
- Cards: agent_id, Common v3.0 badge, role, compose/last-run/memory wells, **Open** (Overview), **Compose preview**.
- Empty: `Control plane unavailable` if health is down; `No agents` if discovery empty; `No matching agents` if filter hides all.
- Poll every Settings `pollMs` (default 15000) while the document is visible and the session is not stale.

## Overview (`/agents/:id`)

- Actions: Compose preview, Run, Chat.
- Operator contract fields (Actor, Reason, Expected parent).
- Attestation card: status `host_reference`, digest, Reload attestation.
- Structure card: structure_id, folder, spec_bytes, Common badge.
- I/O panel: inputs/outputs from `critique_edges`.
- LLM card: resolved provider, inherit default or pick configured backend, Save/Preview mutation.
- Validation honesty: `NOT_RUN` is not a green pass.

## Chat (`/agents/:id/chat`) `data-testid=agent-chat`

- Copy: “Does not write memory, run plugins, enable T3, or grant network.”
- **Clear**: new session id; does not delete JSONL files.
- I/O panel.
- Saved transcripts `data-testid=chat-files` (up to 8) or empty hint `data-testid=chat-files-empty`.
- Log `data-testid=chat-log`: user bubbles indigo (`chat-user`), assistant stone (`chat-assistant`), time `chat-turn-time` HH:MM:SS plus provider on assistant.
- Textarea `#agent-chat-input` `data-testid=chat-input` placeholder `Message this agent`. Enter sends, Shift+Enter newline.
- Send disabled when `!healthOk || stale || containment || pending || !draft.trim()`. Stale label `Stale — Refresh First`.
- History last 20 user/assistant turns posted as `history`.
- Persist: `casops.control-ui.chat.v1` plus `POST /debug/chat` flushed immediately.

## Structure

- Folder path, schema, I/O, spec snapshot JSON well.

## Compose

- Dry-run control.
- Button compose-preview (mutation).
- Shows compose_hash (64), findings, errors, `wrote_locks` (must be false).

## Run

- Dry-run control.
- Invalidate cache (mutation).
- Run (mutation). Dry-run still executes the DAG.
- Plan nodes, last RunResult: adapter, cancelled, containment_stop, artifact, root_trace_id (link to Trace). There is no `status` field.

## Trace (`/agents/:id/traces`, `/traces/:tid`, `/agents/:id/traces/:tid`)

- Load by id.
- Replay (mutation).
- Counterfactual replay (`?counterfactual=`).
- Root-cause.
- Evidence graph.

## Capabilities

- Matrix JSON.
- Verify button (mutation).
- Honesty: asserted-unverified is not production-bindable.

## Protocols

- Raw compatibility JSON.

## Memory

- Policy JSON.
- Hierarchy H0 / mode none on template.
- Query tenant/subject/text.
- Write candidate disabled / fails when mode is none (`MEM_TRUST_TIER`).
- Consolidate enqueue.
- Delete + verify-deletion with tenant and subject.

## Plugins

- Registry GET.
- Validate without exec (`executed: false`).

## Cache

- Stats JSON.
- Invalidate.

## Safety

- Incidents list.
- Red-team POST.

## Improvement

- Candidates list.
- Evaluate.
- Approve (only `independent_approver`; UI still sends the selected actor — host rejects others).
- Rollback version.
- Ledger.

## Validation

- Report JSON.
- `NOT_RUN` / `INDICATIVE` not styled as pass (`ui/src/lib/honesty.ts`).

## Corrigibility

- Attestation digest, signature, `host_reference`, invariant_set_id.
- No write control.

## Org Chat (`/org-chat`) `data-testid=org-chart`

- Read-only critique-edge graph.
- Does not call `runtime/chat`.

## Workflow

- Agent Group select (from loaded agent id prefixes; video preferred default).
- Main: `/svg/video.workflow.svg` object. Click `a.agent-link` → `/agents/{id}/chat`.
- Sub: Sub Workflow select `data-testid=sub-workflow-select` Template A–J then Scale S1–S7 → `/svg/video.template.{a-j}.workflow.svg` and `/svg/video.scale.{s1-s7}.workflow.svg`.

## Settings

- Base URL (empty = Vite proxy).
- Agent Swarm poll interval ms (min 5000).
- Default actor.
- Default dry-run ON checkbox.
- Persist actor on this machine checkbox.
- DEFAULT_LLM select; Preview/Save (mutation). Unconfigured providers disabled.
- Known agent IDs textarea (whitespace-separated).
- Footer: never store production secrets; localhost; no SSO.

## Help drawer and `/help`

- Tabs Spec / User guide.
- Resize handle 280–720, keyboard arrows, persist `casops.control-ui.help-width.v1`.
- Independent vertical scroll on `data-testid=help-document`.
- Full page `data-testid=help-page` height-capped.

## Logs drawer `data-testid=log-drawer`

- Tabs API log / UI log.
- Resize same clamp, persist `casops.control-ui.log-width.v1`.
- Footer session id.
- Independent scroll.

## Theme

- Default light. `html.dark` when dark. Persist `casops.control-ui.theme.v1`. Inline script in `ui/index.html` applies before paint.

---

# Part IX.B — UI usage, remaining screens (continue from Part IX Step 13)

### Step 14 — Agent Profile tabs in order

From Overview of `casops.template.baseline_safe`:

1. Structure: confirm folder ends with `_template_v3`, schema 3.0.
2. Compose: compose-preview, hash length 64, wrote_locks false.
3. Run: Invalidate cache; Run; copy `root_trace_id`.
4. Trace: paste that id; Replay; Counterfactual.
5. Capabilities: matrix; Verify.
6. Protocols: JSON well.
7. Memory: mode none; do not expect a successful write.
8. Plugins: Validate; executed false.
9. Cache: stats; T0; T3 absent.
10. Safety: Red-team; incidents grows by one in this session.
11. Improvement: Evaluate `c1`; switch Actor to `independent_approver` before Approve; switch back.
12. Validation: NOT_RUN / pass false.
13. Corrigibility: host_reference.

### Step 15 — Header combobox

Type `common.health`, select it, open Chat, send `ping`, switch back to `video.director`. Histories remain separate.

### Step 16 — Dry-run honesty

On Run, hover Dry-run. The tooltip says the DAG still executes. Do not treat dry-run as “no HTTP side effects on this host process” — traces and artifacts are stored in process memory.

### Step 17 — Mutation blocked in UI

Clear Reason on Overview. Open Run. Run button is disabled (`mutationReady` false). Chat still works because of `reasonFallback`.

### Step 18 — Mobile shell

Narrow the viewport. Hamburger opens left nav. Help and Logs drawers use `h-[calc(100dvh-8rem)]` so they fit under the header. Scroll Help; the page should stay put.

---

# Part XXXIII — How this book was assembled

Generator: `tools/write_casops_complete_book.py`.

It concatenates:

1. Authored operator/implementer chapters (Parts I–XV and VIII.A–IX.B)
2. Live `schemas/agent/agent_spec.schema.json` plus template spec/policy/cache and the template file tree
3. Live `errors/catalogue.json` expanded to twelve fields per code
4. Live `docs/adr/adr-001.md` … `adr-013.md`
5. Live inventory of every `agents/*/agent_spec.json`
6. Complete copies of the host library, UI source, tests, services, operator docs, v3 spec, implementation plan, evaluation plan, root structure markdown, generic Help markdown, template agent documents, Book of Knowledge, and the tools that generate Help and this book

Re-run the generator after you change the host, the UI, the catalogue, or the agent pack.

'''


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    chunks = [
        NARRATIVE,
        schema_and_template(),
        NARRATIVE_2,
        NARRATIVE_3,
        "# Part XVI — Error catalogue (complete copy of `errors/catalogue.json` fields)\n\n",
        error_tables(),
        "# Part XVII — Architecture decision records (complete files)\n\n",
        adr_block(),
        "\n# Part XVIII — Loaded agent inventory (complete)\n\n",
        inventory(),
        copied_host_library(),
        copied_ui_source(),
        copied_ui_tests(),
        copied_host_tests(),
        copied_services(),
        copied_operator_docs(),
        copied_structure_spec(),
        copied_implementation_plan(),
        copied_evaluation_plan(),
        copied_root_structure_md(),
        copied_generic_help(),
        copied_template_docs(),
        copied_book_of_knowledge(),
        copied_tools(),
        f"\n---\n\n**End of book.** Generated {stamp} from `{REPO}`.\n",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = "".join(chunks)
    OUT.write_text(text, encoding="utf-8")
    print(f"Wrote {OUT} ({len(text):,} characters, {text.count(chr(10)) + 1} lines)")


if __name__ == "__main__":
    main()

