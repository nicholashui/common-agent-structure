# specials.intent-analysis-agent

CASOPS v3 import of `vendor/common-agent-swarm-ops/business/specials/agents/specials.intent-analysis-agent` as `baseline_safe`.
Local deterministic adapter only. Not production-certified.

# `specials.intent-analysis-agent`

> Self-contained **draft** specials agent for host `common-agent-swarm-ops`.

| File | Purpose |
|------|----------|
| `SPEC.md` | Full offline role definition |
| `agent_spec.json` | Host runtime binding (draft, fail-closed) |
| `prompts/primary.md` | Packed Chat/Run prompt (`## System` … `## Developer`) |
| `sources/study/` | Cited domain notes |
| `evals/fixtures/` | CHARACTERIZATION cases (`chat-tc*`, `chat-nlu-*`, `run-tc1`) |
| `content/` | Operator study, API samples, multi-agent paste-ins, `content/test_guide.md` |
| `rubrics/primary.md` | Reviewer dimensions (not a measured PASS) |

Open this folder alone — no external repo or pack `corpus/` is required.
This agent is **not** production-active. Skills stay unbound. See `content/test_guide.md` for Chat / API / multi-agent characterization.
