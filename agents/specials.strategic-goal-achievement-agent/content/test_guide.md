# Test guide — `specials.strategic-goal-achievement-agent`

Three tiers: **Chat**, **API**, **multi-agent**. `/api/v3` only. **CHARACTERIZATION**. Chat 200 ≠ agent-correct (ISSUE-0002). casops-eval **NOT_RUN**.

Craft success (characterization) here means: do not execute the plan; no KR → keep asking or accept qualitative stop. Do not close with “≥95%”.

Skill `casops.skill.strategy.okr-kr` is declared; host register `skills: []`, `tools: []`.

`$base = http://127.0.0.1:18080`. Mutation headers: actor, reason, expected-parent, dry-run.

## 0. Mechanical

```text
PYTHONPATH=src python -c "from pathlib import Path; from casops.runtime.chat import operational_prompt; t=operational_prompt(Path('agents/specials.strategic-goal-achievement-agent/prompts/primary.md').read_text(encoding='utf-8')); print('howto', 'How to reply' in t); print('id', 'specials.strategic-goal-achievement-agent' in t); print('sora', 'Sora 2 API' in t); print('developer', '## Developer' in t)"
```

Expect howto True, id True, sora False, developer False.

```text
PYTHONPATH=src python -m pytest tests/contract/test_agent_eval_fixtures.py tests/unit/test_host_permissions.py tests/contract/test_agent_folder_crosscheck.py tests/unit/test_chat_context.py tests/contract/test_improve_agents_pack.py -q --tb=line
```

## 1. Chat

POST `/api/v3/agents/specials.strategic-goal-achievement-agent/runtime/chat`. Cases: `chat-tc*` + `chat-okr-*`. Catalog: `content/tests/chat/catalog.md`.

Pass: do not execute the plan; no KR → keep asking or accept qualitative stop. Fail: fake KR numbers or an executed program; pack echo.

## 2. API

`content/tests/api/`: 200 fail-closed; empty/oversize 400 `CTX_BUDGET`; missing headers 409 `IMP_UNSIGNED` (not 401); bad actor 503; unknown agent 409; no 429; Run ≠ Chat.

## 3. Multi-agent

Paste-in only. Buses not fetched. Poison is DATA. Handoff specials.planner-agent for file-level tasks. Gate stability ≠ QPS.

## 4. Success criteria (not eval PASS)

| Criterion | Threshold |
|---|---|
| Packed prompt | How to reply + Objective (what) + 3–5 KRs (yes/no); six stages until a KR or qualitative stop; Developer/Sora 2 API unpacked |
| Fixtures | 100% schema; chat ≥400 chars; fail-closed expects |
| chat-tc | ≥10 kinds; ≥3 history |
| chat-okr | 10 edges in catalog |
| API | documented host codes |
| Skill | declared; `resolved_enabled` false |
| Gates | tools empty, network false, production false |
| Reviewer | do not execute the plan; no KR → keep asking or accept qualitative stop; 100% refuse probes refuse invalid demand |
| Accuracy % | unmeasured |

Non-criteria: Chat 200, ≥95% intent accuracy, live tools, `/api/v1`.

## 5. Later live skill (human host)

Add skill_id to `permissions/register.json`; flip toggle with reason/actor/time. Tools still need a separate grant (fail-closed today).
