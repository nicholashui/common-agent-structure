---
name: video-dronepilot
description: Role harness for video.dronepilot — Aerial cinematography (simulated or real)
version: 1.0.0
agent_id: video.dronepilot
---

# Skill — `video.dronepilot`

## When to use
Load this skill when the host routes a task to `video.dronepilot` or when composing a swarm step that requires this craft role.

## Instructions
1. Load prompt `video.prompt.dronepilot.v1` from `../prompts/`.
2. Load rubric `video.rubric.dronepilot.v1` from `../rubrics/`.
3. Ground only on `../sources/` and host memory namespaces.
4. Execute architecture patterns: Constitutional AI, Agent Skills.
5. Emit the JSON output schema from the prompt; fail closed without tools/credentials.
6. On critique: refine ≤ max_refinement_count then escalate.

## Harness
- **Runner kind:** graph-node | tool-loop (host decides)
- **Entry:** pack agent `video.dronepilot` via host agent runner
- **Timeouts:** host default unless agent_spec budget_policy overrides
- **Network:** only if model_policy.network_access and production flags allow

## Bindings
Shared pack special_skills (optional): (none required)

## Research patterns
- **Constitutional AI**: Bai et al. / RLAIF — principles as constitution for self-check
- **Agent Skills**: Anthropic Agent Skills standard — SKILL.md frontmatter + harness

## Tests
- Offline golden: `business/video/evals/agents/video.dronepilot/golden.json`
- Must not require live network for L1 pass when tools are mocked.

<!-- RETHINK_100:start -->
## RETHINK_100 harness notes

Source: `business/video/corpus/study/ui/RETHINK_100_IMPROVEMENTS.md` (applied ids: 2, 6, 12, 13, 15, 21, 26, 30, 31, 35, 37, 38, 43, 47, 48, 59, 63, 87, 88, 90…).

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
- Consider previous and next shot adjacency (pacing, eyeline, continuity) before finalizing shot intents or cuts.

### Evidence
- Machine record: `sources/RETHINK_100_APPLIED.json`
- Agent: `video.dronepilot`
<!-- RETHINK_100:end -->
