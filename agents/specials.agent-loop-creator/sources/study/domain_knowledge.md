# Domain knowledge — `specials.agent-loop-creator`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation.

## Loops that are specified vs loops that spin

**ReAct** (Yao et al., arXiv:2210.03629, ICLR 2023) interleaves Thought → Action → Observation so reasoning is grounded in tool results. It has no cross-episode memory: the same failure repeats.

**Reflexion** (Shinn et al.) adds Actor / Evaluator / Self-Reflection: environmental feedback becomes a *verbal* summary stored as episodic text, not a weight update. That is the difference between a retry and a learning loop.

**Plan-and-Execute** plans once then runs steps; **ReWOO** plans with placeholders and parallelizes tools (token-cheaper, brittle if a tool surprises). Uncontrolled chain reactions (no stop, no schema, no critic) are not “agentic” — they are missing gates.

## Controlled-loop contract (this host)

A loop is admissible only with:

1. Explicit state (what is known, what is blocked).
2. Structured outputs that validate before the next hop.
3. A quality gate (schema / rubric / tests) that can fail closed.
4. A hop budget (`max_peer_hops`, `max_model_calls`) and a human escalation after N failed refinements.
5. Hierarchical delegation that *bubbles up* blockers instead of silently absorbing them.

This folder remains draft: it describes loop shapes. It does not grant tool use or spawn subagents.

## Sources

- Yao et al., ReAct, arXiv:2210.03629
- Shinn et al., Reflexion (Actor–Evaluator–Self-Reflection)
- Plan-and-Execute vs ReWOO vs Reflexion pattern notes (AI Engineer, 2026)
