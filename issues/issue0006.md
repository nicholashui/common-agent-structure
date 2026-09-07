# ISSUE-0006 — Prove Chat/Run reaches the agent through Grok Build

**Status:** Open (operator transport proof). Not an eval pass.  
**Severity:** High (a fluent Chat 200 still looks like the agent ran)  
**Component:** `src/casops/acp/`, `POST /api/v3/agents/{id}/runtime/chat`, `GET /api/v3/agents/{id}/runtime/adapter`, `GET /debug/acp`, Logs drawer ACP tab, `scripts/prove_grok_acp.ps1`  
**Asked:** 2026-09-06 — how to prove access to an agent through Grok Build; write the proof and a complete run step. How to run Grok under `agents/<id>/` (e.g. `specials.intent-analysis-agent`); whether UI Chat is the same as the ACP server. Operator started `grok agent … stdio` by hand then Chatted in the UI (`UNAVAILABLE signal is aborted without reason`). Does the UI call that process? Must each agent be started as an ACP server? Can a console show what that agent is doing?

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

## How to run Grok on an agent folder

Do **not** `cd` into the folder and type `grok`. That uses personal `~/.grok`, ambient MCP, and is not the packaged agent.

Worked example: `agents/specials.intent-analysis-agent` (`agent_id` `specials.intent-analysis-agent`). The packaged identity is that **folder** plus the **generated** profile `var/acp/specials.intent-analysis-agent/profile.md` (`DO NOT EDIT`, `tools: []`, `skills: []`).

There are three Grok paths. UI Chat/Run with adapter `grok_acp` **is** the ACP stdio server this host ships. A Grok TUI in the folder is not.

### 1. UI → API → ACP stdio (this is the ACP server)

CASOPS starts one process, cwd = the agent folder. Paths below are relative to the **repo root** (the directory that contains `agents/`, `scripts/`, and `var/`; wherever you cloned or copied this project):

```text
grok agent --no-leader --always-approve --agent-profile var\acp\specials.intent-analysis-agent\profile.md stdio
```

`GROK_HOME` is `var\acp\specials.intent-analysis-agent\grok-home`. Packaged `session/new` sends `mcpServers: []`.

You do not start Grok yourself. Start the host, then Chat:

```powershell
powershell -File scripts/start_all.ps1
# browser: http://127.0.0.1:15173/agents/specials.intent-analysis-agent/chat
# composer must say Adapter grok_acp before Send
powershell -File scripts/prove_grok_acp.ps1 -AgentId specials.intent-analysis-agent
```

That **is** ACP: JSON-RPC stdio, one Grok process and one `session_id` per `agent_id` until that process stops. It is **not** `grok agent serve` (HTTP). It is **not** a Grok TUI. The UI attaches to this supervisor process, not to a CLI you started.

### 2. CLI Grok TUI on the same projected profile (not ACP)

Same folder + same generated profile, interactive Grok, **no** ACP stdio supervisor:

```powershell
python tools/grok_agent.py chat specials.intent-analysis-agent
python tools/grok_agent.py prompt specials.intent-analysis-agent -p "what inputs do you require?"
```

Same `profile.md` and `GROK_HOME`. Different wire: Grok’s own CLI, not `session/new` / `session/prompt`. The UI does **not** attach to this process.

### 3. Workshop — edit the folder (not packaged execution)

```powershell
python tools/grok_agent.py workshop specials.intent-analysis-agent
```

Grok runs in `agents/specials.intent-analysis-agent` with `Write(corrigibility/**)` and `Edit(corrigibility/**)` denied. Operator editing, not Chat, not ACP, not `approve_candidate`.

### Which path is ACP?

| How you connect | Protocol | Same as ACP server? |
|---|---|---|
| Control UI Chat/Run with `grok_acp` | ACP stdio via CASOPS | **Yes** — this is it |
| `tools/grok_agent.py chat` / `prompt` | Grok TUI + projected profile | No — same profile, not ACP |
| `cd agents\specials.intent-analysis-agent; grok` | Personal global Grok | **No** |
| `tools/grok_agent.py workshop` | Grok in the folder | **No** |

Tools, memory writes, plugins, and T3 stay off on all of these paths. A fluent reply still does not prove the agent is correct (ISSUE-0002).

---

## Who starts Grok (you do not)

You do **not** start a per-agent ACP server. The Control UI never connects to Grok. It only calls CASOPS. CASOPS starts Grok when it needs it.

```text
Browser Chat Send
    → POST http://127.0.0.1:18080/api/v3/agents/specials.intent-analysis-agent/runtime/chat
    → Runtime sees adapter grok_acp
    → AcpSupervisor.ensure("specials.intent-analysis-agent")
         if no live child for that id:
           spawn: grok agent --no-leader --always-approve
                  --agent-profile var/acp/specials.intent-analysis-agent/profile.md
                  stdio
           cwd = agents/specials.intent-analysis-agent
           GROK_HOME = var/acp/specials.intent-analysis-agent/grok-home
           initialize (+ cached_token if Grok offers it)
    → session/new once (mcpServers: []) — same session_id for later Chat turns on this process
    → session/prompt  (first turn: packed system + message; later turns: new message only)
    → JSON reply back to the UI (session stays open until the process stops)
```

| Piece | Role |
|---|---|
| You | Start CASOPS only (`scripts/start_all.ps1`). Open Chat. Type. |
| UI | HTTP client of `/api/v3`. Never talks to `grok.exe`. |
| CASOPS host | ACP **client**. Spawns and owns stdin/stdout of Grok. |
| `grok agent … stdio` | ACP **server**, child process, one per `agent_id`. |

A Grok you start in a terminal is a second, disconnected server. It waits on **that console’s stdin** for JSON-RPC. The host cannot see that stdin, so Chat will not use it. `GET .../runtime/adapter` `pid` will not be your terminal Grok (or stays `null` if Chat never started a host-owned process).

### Separate process?

Yes — **when the adapter is `grok_acp`**. Each `agent_id` gets its **own** `grok.exe` child, started by the host.

| Adapter | Separate process? |
|---|---|
| `grok_acp` | Yes. One Grok ACP stdio process per `agent_id`. |
| `host_llm` | No. Chat/Run stay inside the uvicorn process and call the LLM HTTP API. |

- **Lifetime:** started on first Chat/Run for that id; reused for later turns; not one process per message.
- **Session:** one ACP `session/new` when that process starts. All later Chat turns on that agent reuse the same `session_id` until the process dies.
- **Isolation:** another agent is another `grok.exe` and another `var/acp/<id>/grok-home`.
- **Identity:** still the folder. Grok is the PeerAdapter, not a second agent.

What you run: `powershell -File scripts/start_all.ps1`, then Chat with **Adapter grok_acp**. The first Send may take a while (host starts Grok). After that, adapter `pid` is the host-owned process.

### `UNAVAILABLE signal is aborted without reason`

That is **not** Grok. The UI `fetch` was aborted. Chrome reports `AbortError: signal is aborted without reason`. The client wraps any non-user abort as `UNAVAILABLE`.

Usual cause: **Chat timeout is 120s**. First ACP turn (host starts Grok, `initialize`, `authenticate`, `session/new`, `session/prompt`) often runs longer. At 120s the UI aborts. Same if you hit Stop, Escape, Clear, or change agent mid-wait. `scripts/prove_grok_acp.ps1` uses 180s.

---

## No console on the host-owned agent

The host starts Grok as a **hidden child**. There is no Grok TUI window for that process.

stdin/stdout **are** the ACP cable (JSON-RPC). Those must stay piped. stderr and host ACP events are written under the **repo root**:

`logs/acp/<agent_id>.<stamp>.stderr.log`  
`logs/acp/<agent_id>.<stamp>.host.log`

Open the Logs drawer (ScrollText) → **ACP**. That tab tails `GET /debug/acp?agent_id=` for the selected agent (poll 1.5s). Host lines are JSONL (`spawn`, `rpc`, `session_new`, …) without prompt/thought/secret text. stderr is Grok’s own stream.

`Failed to spawn MCP server 'mcp-search': program not found` is ambient operator MCP leaking into the packaged Grok (plugin `.mcp.json` / parent env). Packaged ACP must send `mcpServers: []` and pin `GROK_HOME/config.toml` with `plugins.enabled = []` and `disabled_mcp_servers` including `mcp-search`. It is not a Chat transport failure; Chat can still complete. It is not an eval pass.

| Surface | What it shows |
|---|---|
| Logs drawer **ACP** | `logs/acp/<agent_id>.*.log` |
| Chat composer | Adapter `grok_acp`, then the reply |
| `GET /api/v3/agents/<id>/runtime/adapter` | `pid`, `healthy`, `home` |
| Task Manager / `Get-CimInstance Win32_Process` | That `pid`’s command line |
| APL log | HTTP Chat POST timing / errors |
| `scripts/prove_grok_acp.ps1` | Transport proof JSON |

A Grok TUI you start yourself (`python tools/grok_agent.py chat specials.intent-analysis-agent`) **does** show a console, but the UI does not use that process. A full Grok TUI cannot share stdout with Chat.

---

## Session id (do not invent one)

You do **not** pass a session id on Chat POST. Grok Build returns it from `session/new`.

| Id | Who creates it | Where |
|---|---|---|
| ACP `sessionId` | Grok Build | Chat JSON `context.session_id` |
| UI transcript session | Chat page `makeChatSessionId()` | `logs/chat/<agent_id>/<stamp>-….jsonl` |

Do not send the UI file name as the ACP session. Fake pytest ACP uses `fake-1`. Live grok uses whatever the binary returns (often a UUID or `sess_…`). Proof is: **non-empty** `context.session_id` plus `provider=grok_acp` plus a live `pid` whose command line is Grok Build.

The host opens **one ACP session per agent process** at Grok start (`session/new` once). Later Chat turns reuse that `session_id` and `pid`. A new session appears only if the Grok process is restarted. The UI adapter card shows the live `pid` and `session_id` (polls while a turn is in flight). Grok assigns `session_id`; the host does not invent it.

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

### 4. Optional CLI (same profile, not ACP)

See **How to run Grok on an agent folder**. `python tools/grok_agent.py chat <agent_id>` is the TUI path. Use steps 1–3 (or `scripts/prove_grok_acp.ps1`) for UI → API ACP proof.

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
| Operator started `grok agent … stdio` in a terminal, then used UI Chat | UI does not attach to that process. Stop it. Let CASOPS spawn Grok. |
| `UNAVAILABLE signal is aborted without reason` | UI `fetch` aborted (usually 120s Chat timeout, Stop, Escape, Clear, or agent change). Not a Grok ACP error code. |
| `Failed to spawn MCP server 'mcp-search'` | Ambient operator MCP (not packaged). Host rewrites `var/acp/<id>/grok-home/config.toml` to disable plugins/MCP and strips `CLAUDE_PLUGIN_ROOT` / `PLUGIN_ROOT` from the child env. |

---

## Honesty

- Not an eval PASS. Characterization / transport only.
- ISSUE-0002 stays Open.
- Do not enable production, T3, network, plugins, or memory writes to obtain this proof.
