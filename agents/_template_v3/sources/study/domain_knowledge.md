# Domain knowledge — `casops.template.baseline_safe`

Design-time study (2026-09). This folder is the **empty fail-closed contract**, not a domain expert.

## What this folder proves

CASOPS v3 (`casops.common_agent.v3`) requires a complete agent tree before compose/run (`common_agent_structure.md` §5.2): `SPEC.md`, `agent_spec.json`, safety, corrigibility, evals. The template is that tree with **no craft**.

It is **not** a Kubernetes probe and **not** SRE golden signals (latency, traffic, errors, saturation — Google SRE book ch. 6, https://sre.google/sre-book/monitoring-distributed-systems/). Those belong to ops dashboards. Host liveness of uvicorn is `GET /health`. Folder-contract observation is `common.health`.

## Operating rules

- No tools, no network, no plugins, no memory writes, no production activation.
- Do not invent a craft, a vendor, or a metric.
- Compose-preview + run must stay `side_effect_class: none`.

## Sources

- `common_agent_structure.md` §5.2 required files
- Google SRE book ch. 6 (golden signals) — contrast only
- Sibling: `agents/common.health/sources/study/domain_knowledge.md`
