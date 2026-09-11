# Domain knowledge — `specials.optimization-agent`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation.

## Optimize a *stated* objective

“Autonomous optimization” without an objective, constraints, and a measurement is just mutation. Minimum contract:

1. Objective (what improves)
2. Constraints (what must not regress: safety, cost, latency, legality)
3. Metric + window
4. Stop / rollback

Process mining and digital twins are **design mentions**. This host does not attach event logs or simulators. Prefer PDCA / REVIEW loops over unconstrained multi-agent “evolution”.

## Sources

- Deming PDCA as the default closed loop
- Cynefin: do not “optimize” a complex domain as if it were a convex program

## Triple research (design-time, 2026-09)

Design-time citations collected to complete the arXiv + YouTube + x.ai triple. **Not** live grants. `allowed_tools` stays `[]`. Network, plugins, T3, memory writes, and production stay off.

### arXiv
- [2503.12434](https://arxiv.org/abs/2503.12434) — Survey on optimization of LLM-based agents
- [2605.27630](https://arxiv.org/abs/2605.27630) — OptiLoop — verify constraints in the loop; missing contract is not a convex program
- [2605.27375](https://arxiv.org/abs/2605.27375) — LCO — LLM constraint optimization; missing safety constraints

### YouTube (educational; do not paste transcripts into Chat)
- [EPM, PDCA Cycle Explained (Deming / Shewhart)](https://www.youtube.com/watch?v=bO3GpAjVvD8)

### xAI (non-activating vendor docs)
- [Cost is a constraint, not a live dashboard](https://docs.x.ai/developers/pricing)

