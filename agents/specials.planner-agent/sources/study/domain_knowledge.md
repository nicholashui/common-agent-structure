# Domain knowledge — `specials.planner-agent`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation.

## Different artifacts need different plans

A strategic architecture note, a UI screen, a schema migration, and a test plan do not share retrieval scope or output schema. Hierarchical planning:

1. Classify the component type.
2. Scope evidence (only the files that type needs).
3. Synthesize with citations to those files.
4. Critic: missing requirement, untraceable task, security-sensitive step.
5. Emit tasks with `file` / `acceptance` links — not a wall of prose.

ReAct/Plan-and-Execute apply to *execution*; this agent **plans**. It must not silently start coding agents or grant tools.

## Sources

- Yao et al., ReAct, arXiv:2210.03629 (execution loops, not this planner’s job)
- Traceability-first: every task cites a source span in the operator corpus

## Triple research (design-time, 2026-09)

Design-time citations collected to complete the arXiv + YouTube + x.ai triple. **Not** live grants. `allowed_tools` stays `[]`. Network, plugins, T3, memory writes, and production stay off.

### arXiv
- [2210.03629](https://arxiv.org/abs/2210.03629) — Yao et al., ReAct — execution loops, not this planner's job (already in study)

### YouTube (educational; do not paste transcripts into Chat)
- [Yao, LLM Agents history & overview (UC Berkeley CS294-196) — ReAct is execution](https://www.youtube.com/watch?v=RM6ZArd2nVc)

### xAI (non-activating vendor docs)
- [Planner emits file+acceptance; it does not spawn tools](https://docs.x.ai/developers/tools/overview)

