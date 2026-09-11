# video.judge

CASOPS v3 import of `vendor/common-agent-swarm-ops/business/video/agents/video.judge` as `baseline_safe`.
Local deterministic adapter only. Not production-certified.

# `video.judge`

VA-aligned Domain Pack agent (common host).

| File | Purpose |
|------|----------|
| `SPEC.md` | VA/generic depth + host binding |
| `agent_spec.json` | Fail-closed runtime |
| `sources/` | Provenance / mapping |

Operator study and three-tier tests: `content/test_guide.md`. Skill `casops.skill.video.judge.llm-as-judge` declared, not host-granted.
