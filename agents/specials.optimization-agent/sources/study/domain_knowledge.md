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
