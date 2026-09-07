# ISSUE-0006 — Prove Chat/Run reaches the agent through Grok Build

**Status:** Open (operator transport proof). Not an eval pass.  
**Severity:** High (a fluent Chat 200 still looks like the agent ran)  
**Component:** `src/casops/acp/`, `POST /api/v3/agents/{id}/runtime/chat`, `GET /api/v3/agents/{id}/runtime/adapter`, `scripts/prove_grok_acp.ps1`  
**Asked:** 2026-09-06 — how to prove access to an agent through Grok Build; write the proof and a complete run step.

**Related:** ISSUE-0005 (ACP adapter). ISSUE-0002 (Chat 200 ≠ agent-correct; proof gap stays Open). Do not claim an eval PASS. Production, T3, plugins, and memory writes stay off.

---

## What this issue proves (and what it does not)

This issue proves **transport**:

`UI / curl → CASOPS /api/v3 → one Grok Build ACP stdio process → agents/<id>/`

It does **not** prove the packaged agent answered as specified. A 200 and a fluent reply are not that proof (ISSUE-0002). ACP v2 is not claimed. `generated/acp-binding.lock.json` is not this artifact.

| Claim | This issue |
|---|---|
| Selected adapter is `grok_acp` | Yes |
| Chat `provider` is `grok_acp` | Yes |
| Grok assigned an ACP `sessionId` | Yes (host does not pick it) |
| OS process is `grok.exe` with `--agent-profile var/acp/<id>/profile.md` | Yes |
| `GROK_HOME` is per `agent_id` | Yes (home path) |
| Memory writes / plugins / T3 stayed off | Yes |
| Reply is agent-correct | **No** — ISSUE-0002 |
| Production ACP binding / §23.6 | **No** |

---

## Session id (do not invent one)

You do **not** pass a session id on Chat POST. Grok Build returns it from `session/new`.

| Id | Who creates it | Where |
|---|---|---|
| ACP `sessionId` | Grok Build | Chat JSON `context.session_id` |
| UI transcript session | Chat page `makeChatSessionId()` | `logs/chat/<agent_id>/<stamp>-….jsonl` |

Do not send the UI file name as the ACP session. Fake pytest ACP uses `fake-1`. Live grok uses whatever the binary returns (often a UUID or `sess_…`). Proof is: **non-empty** `context.session_id` plus `provider=grok_acp` plus a live `pid` whose command line is Grok Build.

The host opens one ACP session per Chat turn, then `session/close`. The next Send gets a new id.

---

## Complete run (one command)

From the repo root, with Grok already installed and logged in (`cached_token`):

```powershell
powershell -File scripts/start_all.ps1
powershell -File scripts/prove_grok_acp.ps1
```

Optional agent (default `video.director`):

```powershell
powershell -File scripts/prove_grok_acp.ps1 -AgentId video.director
```

If Settings had pinned `host_llm`, pin the adapter for this proof:

```powershell
powershell -File scripts/prove_grok_acp.ps1 -ForceAdapter
```

The script writes `logs/proof/grok-acp-<agent_id>-<stamp>.json` and exits `0` only on transport PASS.

**Prerequisites**

1. `grok` on PATH (`grok --version`). Auth must already work (`cached_token` / `grok.com`). The host will not complete an interactive login for you.
2. Projected profile: `var/acp/<agent_id>/profile.md`. If missing: `$env:PYTHONPATH='src'; python tools/project_grok_profile.py --agent-id video.director --write-binding`
3. Control plane on `http://127.0.0.1:18080`. `start_all.ps1` starts it if you have not.
4. Do **not** set `CASOPS_CHAT_ADAPTER=host_llm` or `CASOPS_ACP_COMMAND` (that last one is the pytest fake).

---

## Manual steps (same checks as the script)

Replace `video.director` if you are proving another projected id. Mutation headers are required on Chat POST. Dry-run still executes Chat.

### 1. Before Send — adapter

```powershell
Invoke-RestMethod http://127.0.0.1:18080/api/v3/agents/video.director/runtime/adapter
```

Need: `kind=grok_acp`, `grok_available=true`, `profile_ready=true`, `home` ends with `var/acp/video.director`. `pid` may be `null` until the first turn.

UI: Chat composer strip **Adapter grok_acp · profile ready · grok yes** before Send.

### 2. Send one Chat turn

```powershell
$H = @{
  "Content-Type" = "application/json"
  "x-casops-actor" = "human_operator"
  "x-casops-reason" = "ISSUE-0006 grok_acp transport proof"
  "x-casops-expected-parent" = "none"
  "x-casops-dry-run" = "true"
}
$r = Invoke-RestMethod -Method POST -Headers $H -TimeoutSec 180 `
  -Body '{"message":"ISSUE-0006 ping-grok-acp-marker","history":[]}' `
  http://127.0.0.1:18080/api/v3/agents/video.director/runtime/chat
$r.provider
$r.context.adapter
$r.context.pid
$r.context.session_id
$r.memory_writes
$r.plugins_executed
$r.t3_enabled
```

Need:

- `provider` = `grok_acp`
- `context.adapter` = `grok_acp`
- `context.pid` integer
- `context.session_id` non-empty (Grok-assigned; do not predict the string)
- `memory_writes` = `[]`, `plugins_executed` = `false`, `t3_enabled` = `false`
- Reply must not contain host-dropped thought text (`SECRET_COT`)

`host_llm` looks different: `provider` is `xai` / `local_deterministic` / similar, and `context.pid` is missing.

### 3. OS process is Grok Build

```powershell
$a = Invoke-RestMethod http://127.0.0.1:18080/api/v3/agents/video.director/runtime/adapter
$a | Select-Object kind, pid, healthy, home
Get-CimInstance Win32_Process -Filter "ProcessId=$($a.pid)" |
  Select-Object ProcessId, Name, CommandLine
```

Need `Name` like `grok.exe` and `CommandLine` containing:

`grok agent --no-leader … --agent-profile …\var\acp\video.director\profile.md stdio`

That profile is generated (`DO NOT EDIT`, `name: video.director`, `tools: []`). Process cwd is the agent folder. `GROK_HOME` is `var/acp/video.director/grok-home`.

Two agents must not share pid or home.

### 4. Optional CLI (same profile, not the HTTP supervisor)

```powershell
python tools/grok_agent.py chat video.director
```

This launches Grok Build on the projected profile. It is **not** the UI ACP stdio supervisor. Use steps 1–3 for UI → API proof.

---

## Fail closed

| Symptom | Meaning |
|---|---|
| `kind=host_llm` | In-process complete(). Unset `CASOPS_CHAT_ADAPTER` or Settings → `grok_acp` / default |
| Chat `provider` is `xai` / `local_deterministic` | Same — not Grok Build ACP |
| Empty `context.session_id` | `session/new` did not run |
| `pid` null after Chat | Supervisor did not keep a grok process |
| Command line is `python … fake_acp_stdio.py` | Pytest fake, not Grok Build |
| `CASOPS_ACP_COMMAND` set in the server env | Forced fake/override command |
| Auth / initialize error | `grok` not logged in; CHARACTERIZATION handshake is `tests/fixtures/acp_initialize.characterization.json` |

---

## Honesty

- Not an eval PASS. Characterization / transport only.
- ISSUE-0002 stays Open.
- Do not enable production, T3, network, plugins, or memory writes to obtain this proof.
