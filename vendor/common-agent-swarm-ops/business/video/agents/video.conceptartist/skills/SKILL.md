---
name: video-conceptartist
description: Role harness for video.conceptartist — Pre-pro world/character design
version: 1.0.0
agent_id: video.conceptartist
---

# Skill — `video.conceptartist`

## When to use
Load this skill when the host routes a task to `video.conceptartist` or when composing a swarm step that requires this craft role.

## Instructions
1. Load prompt `video.prompt.conceptartist.v1` from `../prompts/`.
2. Load rubric `video.rubric.conceptartist.v1` from `../rubrics/`.
3. Ground only on `../sources/` and host memory namespaces.
4. Execute architecture patterns: Self-Refine, Agent Skills.
5. Emit the JSON output schema from the prompt; fail closed without tools/credentials.
6. On critique: refine ≤ max_refinement_count then escalate.

## Harness
- **Runner kind:** graph-node | tool-loop (host decides)
- **Entry:** pack agent `video.conceptartist` via host agent runner
- **Timeouts:** host default unless agent_spec budget_policy overrides
- **Network:** only if model_policy.network_access and production flags allow

## Bindings
Shared pack special_skills (optional): (none required)

## Research patterns
- **Self-Refine**: Madaan et al. — iterative critique/refine loop with rubric
- **Agent Skills**: Anthropic Agent Skills standard — SKILL.md frontmatter + harness

## Tests
- Offline golden: `business/video/evals/agents/video.conceptartist/golden.json`
- Must not require live network for L1 pass when tools are mocked.

<!-- RETHINK_100:start -->
## RETHINK_100 harness notes

Source: `business/video/corpus/study/ui/RETHINK_100_IMPROVEMENTS.md` (applied ids: 2, 8, 12, 13, 15, 21, 26, 30, 31, 33, 37, 38, 47, 48, 59, 63, 81, 87, 88, 93…).

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
- Agent: `video.conceptartist`
<!-- RETHINK_100:end -->
