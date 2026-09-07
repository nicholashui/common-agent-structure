# ISSUE-0005 — Grok Build ACP execution adapter

**Status:** In progress (fleet projection + Run model nodes, 2026-09-06)  
**Severity:** High (Chat/Run are in-process LLM dumps; sessions are not OS-isolated)  
**Component:** `src/casops/acp/`, `tools/project_grok_profile.py`, `tools/grok_agent.py`, Chat/Run UI  
**Asked:** 2026-09-04 — encapsulate each `agents/<id>/` with Grok Build per `spec/acp_server.v2.md`; UI → API → Grok Build → Agent; one grok process per agent; CLI talk/improve.

**Related:** ISSUE-0002 (Chat 200 ≠ agent-correct; proof gap stays Open). ISSUE-0003 (characterization fixtures). ISSUE-0006 (operator transport proof through Grok Build). Do not claim an eval PASS.

---

## Probe (CHARACTERIZATION, not a production lock)

Installed adapter: `grok 1.0.13` (`grok agent --no-leader stdio`).

`initialize` with `protocolVersion: 1` returned `protocolVersion: 1`. `authMethods` included `cached_token` and `grok.com`. Locked as CHARACTERIZATION at `tests/fixtures/acp_initialize.characterization.json`. This is **not** `generated/acp-binding.lock.json`. ACP v2 is not claimed.

Ambient MCP servers appeared on the probe process. Packaged Chat MUST send `mcpServers: []` on `session/new`. Fake ACP fixture rejects any other value.

---

## First slice (landed)

- Projector: folder → `var/acp/<agent_id>/` profile + config (generated, not identity).
- Bindings: `protocols/acp.binding.json` + `acp.projection.json` on `_template_v3`, `video.director`, `specials.intent-analysis-agent`.
- ACP stdio client + supervisor; fake stdio fixture for pytest.
- Chat adapter flag `host_llm` | `grok_acp` (pytest pins `host_llm`).
- CLI: `python tools/grok_agent.py chat|prompt|workshop <agent_id>`.
- Tools/skills projected empty. Memory writes, plugin exec, T3, production stay off.

---

## Continue slice (this turn)

- Project every scanned agent (`python tools/project_grok_profile.py --all --write-binding`). Count comes from `list_agent_ids`, not a magic number.
- Run DAG model nodes share `Runtime._complete_packed` with Chat (same adapter, packed context, no primary.md dump).
- Chat UI shows adapter kind / grok / profile **before Send**. Run page fetches the same adapter view. Settings saved-unset is `default` (resolved grok_acp when grok + profile exist).
- CHARACTERIZATION initialize lock in `tests/fixtures/acp_initialize.characterization.json`. Not a production §23.6 lock.
- Fake-ACP execute contract: adapter `grok_acp`, memory_writes `[]`, thought chunks dropped.

---

## Not in this slice

- Production binding locks / §23.6 gates.
- Treating `~/.grok/sessions` as CASOPS memory.
- ISSUE-0002 proof gap (Chat 200 ≠ agent-correct). Stays Open.
- Enabling production, T3, network, plugins, or memory writes.
- Operator transport proof that Chat used Grok Build — see ISSUE-0006 (`scripts/prove_grok_acp.ps1`).
