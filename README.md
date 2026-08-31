# common-agent-swarm-ops (CASOPS host)

Greenfield host for `casops.common_agent.v3` / schema `3.0`.

Source specification: `common_agent_structure.md` (`CASOPS-FS-COMMON-AGENT-STRUCTURE-V3A`).
Implementation plan: `implementation_plan.md` (`CASOPS-IP-COMMON-AGENT-STRUCTURE-V3A-002`).

The only public HTTP plane is FastAPI under `/api/v3/`. There is no second control plane.

## Layout

- `src/casops/` — shared library
- `services/` — separately deployed processes
- `agents/_template_v3/` — `baseline_safe` folder contract
- `errors/catalogue.json` — 12-field error catalogue (spec §20)
- `schemas/` — JSON Schemas
- `docs/adr/` — architecture decision defaults

## Develop

```text
python -m pip install -e ".[dev]"
python -m pytest
```

## Profiles

- `baseline_safe` — first shippable slice
- `production_candidate` — later waves
- `experimental` / `research_only` — never in a release dossier without confirmatory gates
"# common-agent-structure" 
