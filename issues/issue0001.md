# ISSUE-0001 — Chat reply is a single token (`"I"`) on specials agents

**Status:** Resolved  
**Severity:** High (Chat unusable for the specials pack)  
**Component:** `Runtime.chat` / host LLM router / specials `budget_policy`  
**Observed:** 2026-09-04  
**Resolved:** 2026-09-04  
**Evidence:** `logs/debug/2026-09-04-00-31-56-499-g4dmcm-ui.log`, `logs/debug/2026-09-04-00-31-56-499-g4dmcm-api.log`

---

## Symptom

On Agent Profile → Chat for `specials.intent-analysis-agent`, the operator sent:

```text
what you are thinking?
```

The UI showed only:

```text
I
```

This is **not** a frontend truncation bug. The control plane already returned a one-character reply.

## Evidence

UI (`…-g4dmcm-ui.log`):

```text
chat send specials.intent-analysis-agent    what you are thinking?
chat reply specials.intent-analysis-agent xai    I
```

API (`…-g4dmcm-api.log`):

```text
POST /api/v3/agents/specials.intent-analysis-agent/runtime/chat 200 13617ms
request:  {"message":"what you are thinking?","history":[]}
response.reply: "I"
response.provider: "xai"
```

Host LLM at that moment: provider `xai`, model `grok-4.6` (from `GET /api/v3/agents/specials.intent-analysis-agent/llm`). Latency ~13.6s for one visible token.

`ui/src/pages/Chat.tsx` renders `result.reply` unchanged. The one-token string is produced in `src/casops/runtime/llm.py` from `choices[0].message.content`.

## Root cause

`Runtime.chat` copies `agent_spec.budget_policy.max_output_tokens` into the provider `max_tokens` field:

```python
# src/casops/runtime/executor.py  (Runtime.chat)
budget = spec.get("budget_policy") or {}
max_tokens = int(budget.get("max_output_tokens") or 512)
router.complete(..., max_tokens=max_tokens, ...)
```

`agents/specials.intent-analysis-agent/agent_spec.json` is a draft, data-only folder. Its copied budget is:

```json
"budget_policy": {
  "max_input_tokens": 1,
  "max_output_tokens": 1,
  "max_model_calls": 2,
  "max_tool_requests": 0,
  "max_job_ms": 15000,
  "max_cost_units": 1.0,
  "max_peer_hops": 0
}
```

The host therefore called xAI with `max_tokens: 1`. Grok-4.6 spent ~13s on internal reasoning, then was allowed **one** completion token. The first token of a normal English reply is `"I"`. Provider `finish_reason` was almost certainly `length`. That field is not logged today.

The same `max_output_tokens: 1` value is on every imported specials agent:

- `specials.aesthetics-agent`
- `specials.agent-loop-creator`
- `specials.agentic-rag-agent`
- `specials.autotelic-agent`
- `specials.complex-problem-solution-process-model`
- `specials.controller-agent`
- `specials.general-creative-agent`
- `specials.intent-analysis-agent`
- `specials.knowledge-router-agent`
- `specials.llm-usage`
- `specials.optimization-agent`
- `specials.planner-agent`
- `specials.podcast-agent`
- `specials.psychological-profile-agent`
- `specials.psychological-recommendation-agent`
- `specials.research-agent`
- `specials.screenwriter-strategic-goal-achievement-agent`
- `specials.strategic-goal-achievement-agent`
- `specials.techology-advisor-agent`

Video agents (example: `video.performancemarketer`) declare `max_output_tokens: 1024`, so the same Chat path does not collapse there.

Import copies the source integer when it is non-zero:

```python
# tools/import_video_agents.py  (also used by tools/import_specials_agents.py)
"max_output_tokens": int(budget.get("max_output_tokens") or 1024),
```

Source specials folders ship `1`. That is truthy, so the fallback `1024` never applies.

`model_policy.provider` on the folder is still `local_deterministic`. Chat ignores that and uses the **host** default (`xai` in this session). That host-LLM default is intentional. The bug is applying a one-token *draft* budget to a live completion.

## Related gaps (not the `"I"`, but they hide it)

1. **No raw completion telemetry.** `/debug/logs` stores the already-parsed `reply`. It does not store `finish_reason`, `usage`, `model`, or content length. Operators cannot see `length` vs empty-content vs parse error.
2. **Reasoning text is discarded.** OpenAI-compat reasoning models may put thinking in `message.reasoning_content` (or equivalent) and only the final answer in `content`. The router reads `content` only. That is correct under CoT-export policy (`OBS_COT_EXPORT`): Chat must not dump chain-of-thought. The operator question “what you are thinking?” therefore cannot be answered from hidden reasoning even after the token cap is fixed.
3. **`max_input_tokens: 1` is declared but not enforced** on Chat. The system prompt from `prompts/primary.md` still goes to the provider. Only the output cap is applied. Do not “fix” this by truncating the system prompt to one token.

## Why this is a program defect

The host is mechanically faithful to the folder field, and the folder field is a **data-only stub**, not an operator chat budget. The public Chat surface then looks broken: a 13s spinner and a single letter.

Schema `minimum: 1` on `max_output_tokens` is valid JSON. Validity is not usability. Chat against a host LLM with `max_tokens < ~16` cannot produce a readable reply.

## Constraints for any fix

- Do not invent `va_category`.
- Do not enable production activation, T3, network, plugins, or memory writes.
- Do not dump provider reasoning / chain-of-thought into Chat or debug logs.
- Do not treat live `135` (or any other roster count) as a magic constant in tests; scan folders.
- Keep mutation headers on writes. This issue is a host read-path / budget-application change plus optional folder re-import.
- Copy live roster ids; do not rename specials folders.

---

## Suggested resolution

Do **not** start by rewriting every specials `agent_spec.json` by hand. Fix the host so draft budgets cannot make Chat emit one token, then optionally re-import with a documented floor.

### 1. Host Chat completion floor (required)

In `Runtime.chat` (and only Chat, not sealed `execute` unless the same defect is proven there), resolve output tokens as:

- Use `budget_policy.max_output_tokens` when it is an integer **≥ 16** (or another documented floor; 16 is enough to fail closed on stubs without pretending a 1-token draft is a chat budget).
- Otherwise use the existing host default **512** (`int(budget.get("max_output_tokens") or 512)` already intends “missing → 512”; extend that to “unusable stub → 512”).

Keep `execute` on the folder budget if sealed runs must remain budget-honest. Chat is a free-text operator surface on the host LLM; a 1-token stub must not win.

Return `max_tokens` used (and the source: `spec` vs `host_floor`) on the Chat JSON so the UI can show “output cap 512 (folder declared 1)” without implying the folder was rewritten.

### 2. Import floor for stub budgets (required on next specials import)

In `tools/import_video_agents.py` `casops_spec()` (shared by specials import):

```text
raw = int(budget.get("max_output_tokens") or 0)
max_output_tokens = raw if raw >= 16 else 1024
```

Same idea for `max_input_tokens` if the source value is `1` and the host still sends the full prompt: do **not** silently raise input budget unless Chat/run actually enforces it. Prefer documenting “declared 1, not enforced” over inventing a new input cap.

Re-run specials import only after the importer change. Do not invent new `va_category` or role strings; keep copied live fields.

### 3. Completion telemetry without CoT (required for diagnosis)

In `LlmRouter.complete`, after a successful provider call, keep:

- `finish_reason` / Anthropic `stop_reason`
- `usage` prompt / completion / reasoning token counts when present
- `model`
- `content_chars`

Pass a short `llm` object through Chat (and debug API log). **Do not** persist `reasoning_content`, hidden thinking, or full provider payload.

If `finish_reason == "length"` or `content_chars` is tiny relative to `max_tokens`, Chat UI should show an amber note: reply hit the output token cap. That would have made `"I"` self-explanatory.

### 4. Tests (required)

- Unit: Chat with a temp agent whose spec has `max_output_tokens: 1` must call the router with the host floor (512), not 1. Mock `post`; never hit `api.openai.com` / `api.x.ai`. Pin `DEFAULT_LLM=local_deterministic` or inject `LlmRouter(post=...)`.
- Unit: Chat with `max_output_tokens: 1024` still sends 1024.
- Contract: specials Chat (mocked provider) does not return a one-character cap when the folder still says 1, once the host floor lands — or, after re-import, scanned specials specs have `max_output_tokens >= 16`. Scan folders; do not hard-code 19.
- LLM parser: when `message.content` is `"I"` and `finish_reason` is `length`, the Chat body still includes that finish reason.

### 5. Out of scope / do not do

- Do not answer “what you are thinking?” by returning Grok `reasoning_content`. CoT stays off.
- Do not raise `max_job_ms` or enable network because of this issue.
- Do not change video agents that already declare 1024.
- Do not treat this as an xAI 403 / pytest offline issue (that is a separate test pin).

## Acceptance

1. Repeat the logged Chat on `specials.intent-analysis-agent` with host LLM `xai` / `grok-4.6`: reply is a normal paragraph, not `"I"`.
2. Debug API log for that POST includes `finish_reason` and `max_tokens` actually sent, still without reasoning text.
3. `python -m pytest tests` stays offline (no live `httpx` to OpenAI/xAI from unit/contract tests).
4. Folder `va_category` values remain whatever the live specs already contain (empty/null for these specials).

## Suggested order of work

1. Host Chat floor + tests (`executor.py`, `test_runtime.py` / new chat budget test).
2. Router telemetry (`llm.py`, Chat response shape, debug log).
3. UI amber cap notice (`Chat.tsx`) using the new fields.
4. Importer floor + re-import specials (optional if step 1 already makes Chat usable without rewriting folders).

## What landed (2026-09-04)

Host:

- `resolve_completion_tokens` floors declared output tokens below 16 to 512 (`host_floor`). Used by `Runtime.chat` and model nodes in `Runtime.execute`.
- Chat JSON includes `llm`: `max_tokens`, `max_tokens_source`, `declared_max_output_tokens`, `finish_reason`, `content_chars`, `model`, `truncated`, optional numeric `usage`. `reasoning_content` is never copied.

Folders (scan, not a hard-coded count): every loaded `agent_spec.json` with `max_output_tokens` or `max_input_tokens` below 16 was raised to the video import defaults **1024 / 2048**. That was the 19 `specials.*` agents only. Video, template, and `common.health` were left unchanged.

Import: `tools/import_video_agents.py` `casops_spec()` (also used by specials import) floors stub token budgets the same way so a re-import cannot copy `1` again.

UI: assistant bubbles show an amber “Reply hit the output token cap.” when `llm.truncated` or `finish_reason` is `length` / `max_tokens`.

Tests: host floor with mocked HTTP; video 1024 still sent as 1024; parser drops reasoning text; scanned folders must have usable budgets; `casops_spec` floors stubs.
