# Domain knowledge — `common.health`

Design-time study (2026-09). Does not enable network probes, T3, plugins, memory writes, or production activation. Host-filled snapshot facts remain authoritative.

## What a health signal is

A health check answers whether *this instance should receive work right now*. Mixing “am I deadlocked?”, “can I serve?”, and “am I still booting?” into one binary `/health` is a common outage amplifier: a deep dependency check on the load-balancer path drains the whole fleet when a dependency blips ([HLD Handbook, health checks](https://hld.handbook.academy/curriculum/reliability-and-operations/health-checks-readiness/)).

Kubernetes therefore splits three probes ([Kubernetes docs](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes)):

| Probe | Question | Wrong use |
|---|---|---|
| Startup | Has initialization finished? | Treating a slow boot as a crash-loop |
| Liveness | Should the runtime restart me? | Checking remote deps here (restart storms) |
| Readiness | Should I receive new traffic? | Equating “deps down” with “process dead” |

Google’s SRE practice also uses *lame duck*: keep serving in-flight work while refusing new work (SRE book ch. 20, summarized in the same handbook).

## Golden signals vs this agent

Google SRE’s four golden signals are **latency, traffic, errors, saturation** (Ewaschuk, *Monitoring Distributed Systems*, [SRE book ch. 6](https://sre.google/sre-book/monitoring-distributed-systems/)). They describe *user-visible* service health. `common.health` is **not** those four metrics. It is a **host-owned folder/contract snapshot**: spec files present, production gate off, network off, plugins zero, attestation digest. Inventing OS/CPU/HTTP p99 here would impersonate an SRE dashboard the host does not fill.

## Honesty rules for this folder

- `/health` on the control plane (`status=ok`) is process liveness, not an eval pass and not `MEASURED_LOCAL`.
- `status=degraded` on the snapshot means the *folder contract* is incomplete, not that latency is high.
- Do not self-GET `:18080/health` (out of scope; would require network).
- Attestation is host-signed; the agent cannot rewrite it.

## Sources

- Google SRE book ch. 6 (golden signals) and ch. 20 (load balancing / lame duck).
- Kubernetes: Liveness, Readiness, and Startup Probes.
- HLD Handbook: Health Checks and Readiness (2026-05-11).
