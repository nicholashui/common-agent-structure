---
name: video-productiondesign
description: Role harness for video.productiondesign — Sets, locations, world look
version: 1.0.0
agent_id: video.productiondesign
---

# Skill — `video.productiondesign`

## When to use
Load this skill when the host routes a task to `video.productiondesign` or when composing a swarm step that requires this craft role.

## Instructions
1. Load prompt `video.prompt.productiondesign.v1` from `../prompts/`.
2. Load rubric `video.rubric.productiondesign.v1` from `../rubrics/`.
3. Ground only on `../sources/` and host memory namespaces.
4. Execute architecture patterns: Reflexion, Agent Skills.
5. Emit the JSON output schema from the prompt; fail closed without tools/credentials.
6. On critique: refine ≤ max_refinement_count then escalate.

## Harness
- **Runner kind:** graph-node | tool-loop (host decides)
- **Entry:** pack agent `video.productiondesign` via host agent runner
- **Timeouts:** host default unless agent_spec budget_policy overrides
- **Network:** only if model_policy.network_access and production flags allow

## Bindings
Shared pack special_skills (optional): (none required)

## Research patterns
- **Reflexion**: Shinn et al. — verbal RL + episodic memory of failures
- **Agent Skills**: Anthropic Agent Skills standard — SKILL.md frontmatter + harness

## Tests
- Offline golden: `business/video/evals/agents/video.productiondesign/golden.json`
- Must not require live network for L1 pass when tools are mocked.

<!-- RETHINK_100:start -->
## RETHINK_100 harness notes

Source: `business/video/corpus/study/ui/RETHINK_100_IMPROVEMENTS.md` (applied ids: 2, 15, 21, 26, 30, 31, 33, 34, 37, 38, 44, 48, 59, 63, 84, 87, 88, 93, 94).

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
- Verify intermediate narrative/script artifacts before advancing downstream handoffs.

### Evidence
- Machine record: `sources/RETHINK_100_APPLIED.json`
- Agent: `video.productiondesign`
<!-- RETHINK_100:end -->
