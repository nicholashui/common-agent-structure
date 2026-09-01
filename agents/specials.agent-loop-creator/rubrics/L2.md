# Agent Loop L2 rubric (offline Host v3 foundation)

Pass when `/api/v1/agent-loops/agents/{id}/run` with `enable_v3=true` produces:

| Check | Gate |
|-------|------|
| v3 envelope | `result.v3` present with cynefin + premortem + aar |
| Steps bounded | `v3.step_count` ≤ max_steps (default 3–8) |
| Patterns listed | includes Cynefin, Premortem, AAR |
| Fail-closed | allow_production / allow_network denied |
| Core harness | tool_invocations present; L1/L2 attached |

Fail / escalate:

- Critic **blockers** non-empty (not mere warnings)
- Cycle detection with no replan bound
- Production/network flags requested

Full agent_loop_v3 production (live LLM ReAct, TextGrad versioning, multi-agent leader teams) is **not** enforced offline.
