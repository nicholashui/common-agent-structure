# Domain knowledge — `specials.agent-loop-creator`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation. This folder **describes** loop shapes. It does not spawn subagents.

## Loops that are specified vs loops that spin

**ReAct** (Yao et al., arXiv:2210.03629, ICLR 2023) interleaves Thought → Action → Observation. It has no cross-episode memory: the same failure repeats.

**Reflexion** (Shinn et al., arXiv:2303.11366) adds Actor / Evaluator / Self-Reflection: environmental feedback becomes a *verbal* summary stored as episodic text, not a weight update.

**Plan-and-Execute** plans once then runs steps. **ReWOO** (Xu et al., arXiv:2305.18323) plans with placeholders and parallelizes tools (token-cheaper, brittle if a tool surprises).

Uncontrolled chain reactions (no stop, no schema, no critic) are not “agentic” — they are missing gates.

## Findings that change this folder (implement)

| Finding | Change in this pack |
|---|---|
| ReAct has no cross-episode memory | Name the shape; do not claim learning across Chat turns |
| Reflexion stores *text* critique | Escalation/premortem; do not write host memory (`mode: none`) |
| ReWOO ~5× tokens vs ReAct on HotpotQA-class tasks, brittle on surprise | Pick ReWOO only when tools are predictable; else ReAct / Plan-and-Execute |
| Meta-Policy Reflexion (arXiv:2509.03990) reusable rule memory | **Skip live writes.** Describe a *paper* memory, not a grant |
| Runaway loops / hop budgets | Always emit integer hop budget + exhaustion action |
| Multi-intent (arXiv:2509.10010) | List design vs spawn vs tools; only design in-role |
| OOS (arXiv:2507.22289) | Non-loop asks get Scope=OOS |
| Wait when not triggerable (arXiv:2506.01881) | Missing goal/domain → wait, not an infinite loop |

## Skip as live enablement

| Source | Why skipped |
|---|---|
| SPEC “xAI multi-agent orchestration / self-evolution” | Untrusted distillation |
| xAI function calling / Agent Tools | Vendor; `allowed_tools: []` |
| MPR hard admissibility checks that write memory | Host memory writes forbidden |
| Skill live ON | Declared `casops.skill.loop.controlled-shape`; register empty |

## Controlled-loop contract

1. Explicit state. 2. Schema gate before next hop. 3. Hop budget. 4. Escalation after N failed refinements. 5. Blockers bubble up.

## Sources

- Yao et al., ReAct, arXiv:2210.03629 — https://arxiv.org/abs/2210.03629
- Shinn et al., Reflexion, arXiv:2303.11366 — https://arxiv.org/abs/2303.11366
- Xu et al., ReWOO, arXiv:2305.18323 — https://arxiv.org/abs/2305.18323
- Wu et al., Meta-Policy Reflexion, arXiv:2509.03990 — https://arxiv.org/abs/2509.03990
- NLU (briefs): arXiv:2509.10010, 2507.22289, 2506.01881
- xAI tools — https://docs.x.ai/developers/tools/overview
- YouTube (ReAct paper talk, Yao): search “ReAct Synergizing Reasoning and Acting in Language Models” ICLR — do not paste transcripts

## Triple research (design-time, 2026-09)

Design-time citations collected to complete the arXiv + YouTube + x.ai triple. **Not** live grants. `allowed_tools` stays `[]`. Network, plugins, T3, memory writes, and production stay off.

### arXiv
- [2210.03629](https://arxiv.org/abs/2210.03629) — ReAct (already in study)

### YouTube (educational; do not paste transcripts into Chat)
- [Yao, LLM Agents / ReAct (Berkeley LLM Agents MOOC)](https://www.youtube.com/watch?v=RM6ZArd2nVc)

### xAI (non-activating vendor docs)
- [Loop design is not a tool grant (already noted)](https://docs.x.ai/developers/tools/overview)

