---
name: video-journalist
description: Role harness for video.journalist — Reporting + ethical framing
version: 1.0.0
agent_id: video.journalist
---

# Skill — `video.journalist`

## When to use
Load this skill when the host routes a task to `video.journalist` or when composing a swarm step that requires this craft role.

## Instructions
1. Load prompt `video.prompt.journalist.v1` from `../prompts/`.
2. Load rubric `video.rubric.journalist.v1` from `../rubrics/`.
3. Ground only on `../sources/` and host memory namespaces.
4. Execute architecture patterns: Reflexion, Agent Skills.
5. Emit the JSON output schema from the prompt; fail closed without tools/credentials.
6. On critique: refine ≤ max_refinement_count then escalate.

## Harness
- **Runner kind:** graph-node | tool-loop (host decides)
- **Entry:** pack agent `video.journalist` via host agent runner
- **Timeouts:** host default unless agent_spec budget_policy overrides
- **Network:** only if model_policy.network_access and production flags allow

## Bindings
Shared pack special_skills (optional): (none required)

## Research patterns
- **Reflexion**: Shinn et al. — verbal RL + episodic memory of failures
- **Agent Skills**: Anthropic Agent Skills standard — SKILL.md frontmatter + harness

## Tests
- Offline golden: `business/video/evals/agents/video.journalist/golden.json`
- Must not require live network for L1 pass when tools are mocked.

<!-- RETHINK_100:start -->
## RETHINK_100 harness notes

Source: `business/video/corpus/study/ui/RETHINK_100_IMPROVEMENTS.md` (applied ids: 12, 15, 21, 26, 30, 31, 32, 33, 37, 38, 42, 59, 63, 80, 87, 88, 93, 94).

### Fail-closed
- Do not treat design-time model names as enabled APIs.
- Runtime: `allowed_tools` + host production flags only.

### Operator-facing quality
- Host control plane owns orchestration; this agent never opens a second control plane.
- Runtime tools remain agent_spec.allowed_tools only; RETHINK model names are design-time.
- Fail closed when tools/providers are unavailable (circuit-breaker posture).
- Prefer iterative verify → refine ≤ max_refinement_count → HiTL over silent pass.
- Emit plain-English reasoning summary in artifacts for operator trust.
- Attach provenance / correlation_id / evidence_refs on every handoff.
- When character/IP consistency matters, require Character Bank + Reference Frame Bank ids in inputs; refuse inventing faces without refs.
- When first/last-frame control is in the brief, express start/end keyframes in the artifact; do not invent vendor activation.

### Evidence
- Machine record: `sources/RETHINK_100_APPLIED.json`
- Agent: `video.journalist`
<!-- RETHINK_100:end -->
