# ISSUE-0002 — Prove an agent is actually running: input interface and Chat-to-output flow

**Status:** Open (proof gap remains). Chat UX slice landed 2026-09-04.  
**Severity:** High (operator cannot confirm correct agent execution)  
**Component:** Chat (`Runtime.chat` / `POST /api/v3/agents/{id}/runtime/chat`), declared I/O (`critique_edges`), `agents/<agent_id>/observability/`  
**Observed:** 2026-09-04  
**Sample session:** `logs/debug/2026-09-04-00-58-29-767-yr38m0-ui.log`, `logs/debug/2026-09-04-00-58-29-767-yr38m0-api.log`  
**Related:** ISSUE-0001 (one-token Chat cap; resolved). This issue is **not** that bug. After the cap fix, Chat returns a full paragraph. A full paragraph still does **not** prove the agent folder ran as specified.

---

## Operator need

The operator wants, for **each** agent:

1. How that agent **interfaces with input** (what is declared, what is actually bound, what Chat uses).
2. The **complete process flow** from a human message to the Chat bubble.
3. Evidence that can **prove the agent is correctly running**.

Today that proof is missing. A `200` Chat reply from the host LLM looks like the agent “worked.” The host did not execute the agent DAG, did not bind declared peer inputs, did not write a decision record, and did not apply `observability/*` policy.

This issue records a **live sample** of the current Chat path, states what that sample can and cannot prove, and asks whether `agents/<agent.id>/observability` is the right surface for the missing proof.

---

## Sample (this is the recorded Chat path, 2026-09-04)

Agent: `specials.intent-analysis-agent`  
Host LLM: `xai` / `grok-4.6` (folder `model_policy.provider` remains `local_deterministic`; Chat ignores that and uses the host default)  
Output cap after ISSUE-0001: `max_tokens` 1024 from folder spec (`max_tokens_source: spec`)

| Time (UTC) | Operator / UI | Host |
|---|---|---|
| 00:58:29 | Open Agent Swarm `/` | `GET /api/v3/agents` |
| 00:58:34 | Open agent Overview | `GET .../structure`, attestation, `validation/report` (`NOT_RUN` / `unqualified_instruments`), `GET .../llm` |
| 00:58:35 | Open Chat | `structure` + `llm` again |
| 00:59:12 | Type **What I am thinking now?** | UI `chat send` |
| 00:59:31 | Assistant bubble (~19 s) | `POST .../runtime/chat` **200 19078ms**, `history: []` |
| 00:59:59 | Type **You should think why i ask these question** | UI `chat send` |
| 01:00:18 | Assistant bubble (~18 s) | `POST .../runtime/chat` **200 18475ms**, history = previous user + assistant |

Turn 1 telemetry (API log, not shown in the bubble):

```text
provider: xai
model: grok-4.6
max_tokens: 1024  (spec)
finish_reason: stop
truncated: false
content_chars: 377
prompt_tokens: 1652
completion_tokens: 79
reasoning_tokens: 853
memory_writes: []
plugins_executed: false
t3_enabled: false
used_prompt_reference: prompts/primary.md
```

Turn 1 `reply` (what the UI painted):

```text
I can’t know what you’re thinking. I only see the text you send.

From this message alone, the surface request is mind-reading. The more likely
goals are testing what I’ll claim, joking, or starting a conversation. Nothing
in the words shows a hidden agenda.
```

Turn 2 sent the first pair as `history`. The model then analysed *why the question was asked* from those words. That is host Chat with conversation memory in the request body, not agent memory writes.

`GET .../validation/report` in the same session: `verdict: NOT_RUN`, `reason: unqualified_instruments`, `pass: false`. Eval did not run. Chat still returned 200.

---

## Complete process flow (current host, as coded)

This is the path the sample took. It is the same for every agent Chat tab unless noted.

```text
1. Operator types in ui/src/pages/Chat.tsx textarea and Send
2. UI appends a user turn, saves the thread locally, POST /debug/chat (transcript file)
3. UI POST /api/v3/agents/{agent_id}/runtime/chat
     headers: x-casops-actor, x-casops-reason (fallback "operator chat"),
              x-casops-expected-parent, x-casops-dry-run
     body: { message, history }     history is prior user/assistant turns only
4. FastAPI runtime_chat → Runtime.chat
5. locate_agent_folder(agents/<agent_id>/)
6. Load agent_spec.json, safety/policy.json
7. folder_io(): copy critique_edges.inputs/outputs as *names*; do not fetch those payloads
8. load_prompt(): prompts/primary.md (or spec.prompt_reference)
9. build_chat_system():
     folder prompt
     + "## Declared input requirements"  (id list, or "(none declared)")
     + "## Declared output requirements"
     + "## Human operator"  (free-text is the input; do not require peer payloads)
10. resolve_completion_tokens(budget_policy.max_output_tokens)
11. LlmRouter.complete(prompt=operator message, system=build_chat_system, history)
      host provider (here xai), not folder local_deterministic
      OpenAI-compat POST {base}/chat/completions
12. Parser keeps message.content only. reasoning_content is dropped (OBS_COT_EXPORT).
13. safety_gate (cancel / CoT export / kill-switch). Chat does not compile the DAG.
14. JSON back to UI: reply, provider, io (declared names), llm telemetry,
    memory_writes=[], plugins_executed=false, t3_enabled=false
15. Chat.tsx paints result.reply. Amber cap note only if llm.truncated.
```

Chat does **not**:

- compile or walk `runtime/execution.json`
- attest a run-start checkpoint (that is `Runtime.execute`)
- record a row in `runtime.runs`
- bind or load `critique_edges` peer artifacts
- execute plugins
- write memory
- enable T3
- read `observability/telemetry.json`, `sampling.json`, `redaction.json`, `slo.json`, or the evidence/decision schemas
- export OTLP despite `exporter: "otlp"` on disk

`Runtime.execute` (Agent Profile → Run, `POST .../runtime/run`) is a **different** path: admit, attest, compile DAG, one model node using `prompts/primary.md` **without** the operator Chat message, seal an artifact, keep an in-memory evidence_graph stub. That path also does not read `observability/*.json` in `src/casops`.

---

## How each agent interfaces with input

There are three different “input” surfaces. They are easy to confuse. The sample used only (A) + names from (B).

### A. Operator Chat input (what the sample used)

| Field | Source | Bound at Chat? |
|---|---|---|
| Latest message | textarea → `body.message` | **Yes** — this is the user content of the LLM call |
| History | prior Chat turns, max 20 | **Yes** on turn 2 of the sample |
| System prompt | `agents/<id>/prompts/primary.md` | **Yes** (text inlined) |
| Declared I/O names | `agent_spec.critique_edges` | **Listed in the system prompt only** |
| Host LLM | `GET .../llm` default (`xai` here) | **Yes** |
| Folder `model_policy` | `local_deterministic`, `network_access: false` | **Not used for Chat routing** |

`build_chat_system` tells the model: treat the latest operator message as input; do not require peer-agent critique payloads unless the operator pastes them.

So Chat input is **free text**, not the named buses.

### B. Declared folder I/O (what the IoPanel shows)

From `agent_spec.json` `critique_edges`, copied by `folder_io` / `io_from_spec`. The Chat page shows these as chips. They are **peer ids or bus names**, not JSON that Chat fetched.

Sample agent:

```json
"critique_edges": {
  "inputs":  ["spagent.intent-analysis-agent-input"],
  "outputs": ["spagent.intent-analysis-agent-output"]
}
```

Video example (`video.director`): inputs/outputs are other `video.*` agent ids. Org Chat draws those edges. Chat still does not pull critic/editor artifacts unless the operator pastes them.

Plugin `input_schema` / `output_schema` can appear on the IoPanel. Chat sets `plugins_executed: false` and does not call plugins.

### C. Sealed Run input (not used in the sample)

`runtime/execution.json` DAG. For this specials agent that is a single `kind: model` node. `execute()` sends `prompts/primary.md` to the router **without** the Chat textarea. Operator Chat and sealed Run are not the same interface.

---

## Why the operator still cannot confirm the agent is correctly running

The sample **does** prove:

- UI → public `/api/v3` Chat → host xAI → bubble
- After ISSUE-0001, output cap 1024, `finish_reason: stop`, not `"I"`
- No memory write, no plugin, no T3 on this path
- Prompt file `prompts/primary.md` was named in the response

The sample **does not** prove:

1. **Declared inputs were satisfied.** `spagent.intent-analysis-agent-input` was never loaded. The model only saw the typed sentence (and, on turn 2, Chat history).
2. **Declared outputs were produced.** There is no `spagent.intent-analysis-agent-output` artifact, only `reply` text.
3. **The agent DAG ran.** Chat never compiled `execution.json`. No `root_trace_id`, no run in `runtime.runs`.
4. **Folder model policy ran.** Chat used host `xai`, not `local_deterministic`.
5. **Eval / instruments ran.** Same session: `validation/report` = `NOT_RUN`.
6. **Observability policy ran.** See next section. No OTLP export, no sampling decision, no redaction pass, no decision record, no evidence graph for Chat.
7. **Role-correct behaviour vs generic Grok.** A plausible paragraph from grok-4.6 with the primary prompt inlined is not a pass against `rubrics/primary.md`.

A green Chat bubble is **host LLM availability**, not **agent-correct execution**.

---

## Is this related to `agents/<agent.id>/observability`?

**Related as the specified proof surface. Not related as something Chat currently uses.**

Every v3 folder is required to contain at least:

| File | Sample contents (`specials.intent-analysis-agent`) | Read by Chat / `src/casops` runtime? |
|---|---|---|
| `observability/telemetry.json` | `exporter: otlp`, `content_capture: metadata_only` | **No** |
| `observability/redaction.json` | `mode: metadata_only`, secret classes credential/pii | **No** |
| `observability/sampling.json` | `tail_sampling: true`, `mandatory_retention: true` | **No** |
| `observability/slo.json` | `slos: []` | **No** |
| `observability/evidence_graph.schema.json` | schema only | **No** (Run builds a tiny in-memory graph, not from this file) |
| `observability/decision_record.schema.json` | requires `inputs`, `actions`, `constraints`, `codes`, `outcomes` | **No** |

`agent_spec.json` points at them (`observability_ref`, `sampling_ref`). Folder validation only checks that `telemetry.json`, `redaction.json`, and `sampling.json` **exist**. Grep of `src/casops` finds no loader for those JSON bodies except the required-file list and error codes (`OBS_*`).

So:

- **Yes, related:** if the operator wants to *prove* a correct run, the folder already names the surfaces: traces/spans (telemetry), what content may be stored (redaction / `content_capture: metadata_only`), what must not be dropped (sampling / mandatory retention), SLOs, evidence graph, decision record (`inputs` + `actions` + `outcomes`). ISSUE-0002 is asking for that proof on the Chat (and Run) paths.
- **No, not causing the sample:** the 00:58:29 Chat did not fail or succeed *because of* observability files. They sat on disk. `reasoning_tokens: 853` vs `completion_tokens: 79` is provider usage, not an OTLP span from `telemetry.json`. CoT is omitted because the router copies `message.content` only (`OBS_COT_EXPORT` policy in code), not because `redaction.json` was applied.

Filling Chat with more debug text that includes hidden reasoning would **violate** observability/redaction intent (`metadata_only`, CoT block). Proof should be **structured records**, not dumping Grok thinking into the bubble.

---

## What a correctness proof would need (acceptance for this issue)

Do not invent `va_category`. Do not enable production, T3, network, plugins, or memory writes to “make Chat look live.”

Minimum operator-visible proof, per Chat (and separately per Run):

1. **Input binding record** — which of: operator message, Chat history, declared `critique_edges` inputs (bound vs name-only vs missing), prompt file digest. Decision-record `inputs` matches `observability/decision_record.schema.json`.
2. **Path id** — `chat` vs `execute`. Chat must not be labelled a DAG run. Execute must show node ids from `execution.json`.
3. **Model routing record** — host provider vs folder `model_policy`; `max_tokens` and source (`spec` / `host_floor`).
4. **Output record** — Chat: `reply` digest, `finish_reason`, `truncated`, `content_chars`. Run: sealed artifact id. Declared outputs: produced / not produced / not applicable for Chat.
5. **Negative guarantees** — `memory_writes`, `plugins_executed`, `t3_enabled`, `network_access` as actually applied.
6. **Observability application** — either apply `telemetry.json` / `sampling.json` / `redaction.json` and show exporter/sample/redaction decisions, or honestly mark `observability: NOT_APPLIED` (same honesty as `validation: NOT_RUN`). Do not imply OTLP when the exporter is not wired.
7. **Eval stays honest** — `NOT_RUN` remains `NOT_RUN`. A Chat 200 is not an eval pass.

Scan agent folders in tests; do not hard-code roster counts.

---

## Chat UX suggestions

Operator asked what Agent Chat could gain for a **normal user**, using **core essentials only** from [AIDotNet/lobe-chat](https://github.com/AIDotNet/lobe-chat) (Lobe Chat) and [open-webui/open-webui](https://github.com/open-webui/open-webui) ([chat features](https://docs.openwebui.com/features/chat-conversations/chat-features)). Not a clone of either product.

### UX slice landed 2026-09-04 (per-agent Chat tab)

Picked from the lists below. Host Chat contract unchanged: no memory write, no plugins, no T3, no network grant, no CoT dump. A Chat 200 is still not an eval pass. Streaming is **not** in this slice (host POST is still one-shot); Stop aborts the UI fetch.

| Feature | Where |
|---|---|
| **Stop generation** | Stop button + Escape while waiting. `AbortSignal` on `chatAgent`. Server-side Grok call may still finish. |
| **Markdown + code highlight + copy-on-code-block** | Assistant bubbles only (`react-markdown`, `remark-gfm`, `rehype-highlight`). User text stays plain. |
| **Copy message** | Copy on each bubble. |
| **Regenerate last assistant** | Re-sends the last user message with prior history. |
| **Export** | Export MD / Export JSON of the live thread. Header says Chat ≠ sealed Run. |
| **Follow-up chips** | After an assistant reply; local questions or three fallbacks. Click sends. No extra LLM call. |
| **Stick-to-bottom + Jump to latest** | Auto-scroll only when pinned near the bottom. |
| **Load Chat History** | Load on a saved `logs/chat/<id>/*.jsonl` file via `GET /debug/chat?agent_id=&name=`. Replaces the live thread; file stays on disk. |

Proof gap (input binding / path id / observability) is **still open**. This slice is Chat UX, not ISSUE-0002 acceptance.

### What Chat already has

- Per-agent thread (localStorage + `logs/chat/<id>/` files)
- Textarea, Enter to send, Shift+Enter newline
- Clear (new session; old files kept)
- IoPanel of **declared** buses (not bound)
- Host LLM name, wait spinner, token-cap warning
- Mutation headers; no memory / plugins / T3

Missing versus a normal chat app: no streaming, no markdown, no copy/regenerate/edit/stop, no conversation list, no search, no retry, no export of a readable transcript.

### What a normal user needs

1. See the answer **as it arrives**, and **stop** it.
2. **Read** it (markdown, code, lists).
3. **Reuse** it (copy, export).
4. **Fix** a bad turn (edit last prompt, regenerate).
5. **Keep** more than one conversation per agent (list, rename, switch, search).
6. Know **what went into the model** (model, tokens, truncated, bound vs name-only I/O) — the proof gap above.

### P0 — table stakes (both apps; biggest UX gap)

| Feature | Why users want it | Lobe / Open WebUI | CASOPS note |
|---|---|---|---|
| **Streaming reply** | 19s of “Waiting…” feels broken | Default in both | Host Chat is non-streaming today |
| **Stop generation** | Cancel a long Grok wait | Both | Needs abort on `httpx` / fetch |
| **Markdown + code highlight + copy-on-code-block** | Replies already use `**bold**` and lists; they currently show as raw `*` | Lobe Markdown; OWUI LaTeX/Mermaid/code | Render **assistant** markdown only; keep user text as typed |
| **Copy message** | Reuse an analysis | Both | One click on bubble |
| **Regenerate last assistant** | Bad or truncated answer | Lobe Alt+R; OWUI | Same history, new completion |
| **Edit last user message and resend** | Typo / tighter prompt | Both | Truncate history from that turn |
| **Retry on error** | 403 / timeout | Both | Show error on the turn, not only a banner |
| **Conversation list per agent** | Clear today wipes the live thread | OWUI folders/pins; Lobe topics/sessions | Timestamped files already exist; they are not openable as chats |
| **Open / rename / delete a saved transcript** | “Yesterday’s intent analysis” | OWUI history + search | Map files ↔ threads |
| **Export** (Markdown / JSON) | Share or archive | OWUI share/export | Honest: Chat ≠ sealed Run |

### P1 — daily operator UX

| Feature | Why | Source | CASOPS note |
|---|---|---|---|
| **Follow-up chips** | After a reply, 2–3 next questions | OWUI follow-up prompts | Cheap; stays text-only |
| **Prompt library / slash snippets** | Repeat “DIA pass on this text” | OWUI `/` prompts; Lobe input template | Per-agent or host-wide, not agent folder rewrite |
| **Composer: expand, draft restore, Up-arrow history** | Long prompts | OWUI expand box; Lobe restore/up-arrow | |
| **Token / context meter** | Know why answers get thin | OWUI `/status`; Lobe usage | Chat JSON already returns `llm.usage`; not shown |
| **Proof strip** | Confirm the agent path | this issue | Bound message vs name-only `critique_edges`; `chat` vs `execute`; `NOT_RUN` eval |
| **Provider/model on the turn + switch for next send** | See grok-4.6; try local | Both multi-provider | Host LLM only; do not imply folder `network_access` |
| **Keyboard: stop, regenerate, new chat, focus input** | Power users | Lobe shortcuts; OWUI rebindable | |
| **Stick-to-bottom + “jump to latest”** | Long threads | OWUI auto-scroll toggle | |
| **Empty-state examples** | First visit | OWUI new-chat suggestions | Per-agent, from role/prompt, not invented `va_category` |

### P2 — useful later, still chat-core

| Feature | Why | Source | CASOPS constraint |
|---|---|---|---|
| **Fork / branch from a message** | Try another angle | OWUI fork | New session id; keep original file |
| **Search this agent’s chats** | Find an old analysis | OWUI history search | Search files under `logs/chat/<id>/` |
| **Attach a file as extra user text** (txt/md/json, size-capped) | Paste is painful | Both uploads | **In-request only**; not agent memory; not RAG/T3 |
| **TTS read-aloud of assistant** | Hands-off | Lobe TTS; OWUI TTS | Browser speech; no new network grant to the agent |
| **STT dictation into the box** | Same | Both | Same bound |
| **Temporary chat** (don’t persist) | Scratch | OWUI `/temporary` | Skip `/debug/chat` |

### Do not copy as Chat essentials

The rest of Lobe/OWUI is a full AI product, not this Agent tab:

- RAG / knowledge bases / web search / URL fetch (agent `network_access` stays false)
- Plugin/tool/MCP **execution** (`plugins_executed` must stay false)
- Persistent user memory across chats (folder `memory.mode` is `none`)
- Image gen, voice **calls**, calendar, automations, channels, sub-agents, code interpreter
- Multi-model side-by-side (nice later; not core)
- Agent marketplace, RBAC/SSO, vector DBs

Those fight the current Chat contract: host-routed free text, no memory write, no plugins, no T3, no CoT export.

### Optional first slice (if/when operator picks)

1. Stream + Stop  
2. Markdown + copy  
3. Edit / regenerate / retry  
4. Conversation list from existing transcript files  
5. Visible `llm` + I/O binding proof (this issue’s acceptance)

---

## Suggested order of work (not started)

Proof path (this issue’s original ask):

1. Document in Chat UI, next to IoPanel: “declared buses (not bound this request)” vs “operator message (bound).”
2. Return a `proof` / `io_binding` object on Chat JSON (and debug API log) covering items 1–5. Keep CoT out.
3. Decide Chat vs Run: Chat stays free-text host LLM; Run stays DAG. Do not pretend Chat executed `execution.json`.
4. Wire or explicitly `NOT_APPLY` `observability/telemetry.json` (and sampling/redaction) on both paths. Empty `slo.json` stays empty until SLOs exist.
5. Optional: persist a decision record under host logs (not agent-rewritable) keyed by Chat digest / run id, schema-valid against the folder’s `decision_record.schema.json`.
6. Tests: Chat with declared inputs still has `io.inputs` listed and `io_binding.declared_inputs_fetched: false` until a real bind exists; observability files exist; Chat does not read them until step 4 says it does.

UX path: **parked**. Implement none of the P0–P2 table until the operator chooses a slice.

## Out of scope

- Dumping `reasoning_content` to prove “the agent thought.”
- Treating ISSUE-0001’s `"I"` as this issue (that was a 1-token budget).
- Enabling network because Chat uses xAI; that is host-owned routing, not agent `network_access`.
- Swarm `/api/v3/swarms` (specified, not live).
- Implementing Lobe/Open WebUI features before an explicit pick.

