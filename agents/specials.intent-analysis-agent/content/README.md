# Operator content — `specials.intent-analysis-agent`

This folder is **operator study**. The host still loads:

| Host file | Role |
|---|---|
| `prompts/primary.md` | Packed Chat/Run system (`## System` … `## Developer`) |
| `sources/study/domain_knowledge.md` | Cited domain notes |
| `evals/fixtures/*.json` | `casops.testcase.v1` CHARACTERIZATION cases |
| `agent_spec.json` | Fail-closed gates |

`content/` is not a second runtime. Skill `casops.skill.intent.speech-act` is **declared** and **not host-granted** (`permissions/register.json` skills/tools empty for this agent). Tools, network, plugins, memory writes, and production stay off.

## Layout

```
content/
  README.md                 # this file
  research/sources.md       # arXiv / xAI / YouTube map
  tests/chat/               # NLU edge chat scripts (paste into Chat)
  tests/api/                # /api/v3 samples (valid, malformed, mutation, run)
  tests/multi-agent/        # name-only bus paste-in (not fetched)
  test_guide.md             # three-tier validation + honest success criteria
```

Host-loadable copies of the NLU chat cases also live at `evals/fixtures/chat-nlu-*.json` (same schema as `chat-tc*.json`). API samples that are not Chat/Run fixtures stay here: the host fixture `path` enum is only `chat` | `run`.
