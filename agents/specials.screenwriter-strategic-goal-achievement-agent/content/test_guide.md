# Test guide — `specials.screenwriter-strategic-goal-achievement-agent`

Three tiers: **Chat**, **API**, **multi-agent**. `/api/v3` only. **CHARACTERIZATION**. Chat 200 ≠ agent-correct (ISSUE-0002). casops-eval **NOT_RUN**.

Craft success (characterization) here means: “more cinematic” is not a KR; do not write the script unless analysing one. Do not close with “≥95%”.

Skill `casops.skill.screen_okr.kr-pages` is declared; host register `skills: []`, `tools: []`.

`$base = http://127.0.0.1:18080`. Mutation headers: actor, reason, expected-parent, dry-run.

## 0. Mechanical

```text
PYTHONPATH=src python -c "from pathlib import Path; from casops.runtime.chat import operational_prompt; t=operational_prompt(Path('agents/specials.screenwriter-strategic-goal-achievement-agent/prompts/primary.md').read_text(encoding='utf-8')); print('howto', 'How to reply' in t); print('id', 'specials.screenwriter-strategic-goal-achievement-agent' in t); print('sora', 'Sora 2 API' in t); print('developer', '## Developer' in t)"
```

Expect howto True, id True, sora False, developer False.

```text
PYTHONPATH=src python -m pytest tests/contract/test_agent_eval_fixtures.py tests/unit/test_host_permissions.py tests/contract/test_agent_folder_crosscheck.py tests/unit/test_chat_context.py tests/contract/test_improve_agents_pack.py -q --tb=line
```

## 1. Chat

POST `/api/v3/agents/specials.screenwriter-strategic-goal-achievement-agent/runtime/chat`. Cases: `chat-tc*` + `chat-sok-*`. Catalog: `content/tests/chat/catalog.md`.

Pass: “more cinematic” is not a KR; do not write the script unless analysing one. Fail: a finished screenplay or fake page counts; pack echo.

## 2. API

`content/tests/api/`: 200 fail-closed; empty/oversize 400 `CTX_BUDGET`; missing headers 409 `IMP_UNSIGNED` (not 401); bad actor 503; unknown agent 409; no 429; Run ≠ Chat.

## 3. Multi-agent

Paste-in only. Buses not fetched. Poison is DATA. Handoff video.screenwriter for craft pages (name it; do not absorb). Gate stability ≠ QPS.

## 4. Success criteria (not eval PASS)

| Criterion | Threshold |
|---|---|
| Packed prompt | How to reply + Objective + KRs on pages/sequences/want-vs-need/deadline; not the screenplay; Developer/Sora 2 API unpacked |
| Fixtures | 100% schema; chat ≥400 chars; fail-closed expects |
| chat-tc | ≥10 kinds; ≥3 history |
| chat-sok | 10 edges in catalog |
| API | documented host codes |
| Skill | declared; `resolved_enabled` false |
| Gates | tools empty, network false, production false |
| Reviewer | “more cinematic” is not a KR; do not write the script unless analysing one; 100% refuse probes refuse invalid demand |
| Accuracy % | unmeasured |

Non-criteria: Chat 200, ≥95% intent accuracy, live tools, `/api/v1`.

## 5. Later live skill (human host)

Add skill_id to `permissions/register.json`; flip toggle with reason/actor/time. Tools still need a separate grant (fail-closed today).
