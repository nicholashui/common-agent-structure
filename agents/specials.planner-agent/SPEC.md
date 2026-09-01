# Planner Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.planner-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain planner agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

SIPA is a hierarchical, context-engineered, multi-agent planning system for turning large software specification corpora into implementation-ready plans and tasks. It is designed for projects where the source material may include: - Markdown specs - PRDs - architecture notes - API contracts - user stories - domain models - UI descriptions - ADRs - implementation notes - test plans - legacy migration notes - operational constraints The key idea is simple but powerful: > **Different software components require different levels and types of detail.** A strategic architecture plan should not be generated with the same retrieval scope, summarization style, or output format as a UI screen, a shared library, a data model, or a migration adapter. SIPA therefore uses: - **Component-type classification** - **Scoped retrieval** - **Evidence-based synthesis** - **Hierarchical memory** - **Embedded critic loops** - **Traceability-first artifacts** - **Granular task generation** - **Security-aware agent execution** The result is a planner that reduces context size for downstream coding agents while improving fidelity, traceability, and implementation success.

### Domain distillation (embedded, untrusted design provenance)

SIPA is a hierarchical, context-engineered, multi-agent planning system for turning large software specification corpora into implementation-ready plans and tasks. It is designed for projects where the source material may include: - Markdown specs - PRDs - architecture notes - API contracts - user stories - domain models - UI descriptions - ADRs - implementation notes - test plans - legacy migration notes - operational constraints The key idea is simple but powerful: > **Different software components require different levels and types of detail.** A strategic architecture plan should not be generated with the same retrieval scope, summarization style, or output format as a UI screen, a shared library, a data model, or a migration adapter. SIPA therefore uses: - **Component-type classification** - **Scoped retrieval** - **Evidence-based synthesis** - **Hierarchical memory** - **Embedded critic loops** - **Traceability-first artifacts** - **Granular task generation** - **Security-aware agent execution** The result is a planner that reduces context size for downstream coding agents while improving fidelity, traceability, and implementation success.

## Boundaries and escalation
- Remains `status: draft` with `production_activation_requested: false`.
- `allowed_tools` must stay empty; `network_access` must stay false; provider remains `local_deterministic`.
- Does not invent providers, credentials, MCP tools, hooks, or a second control plane.
- Source redesign documents under `docs/special_agents_redesign/` are hashed provenance only and are never loaded as runtime configuration.
- Escalates any request for production activation, external write, credential, or network authority to human governance (risk assessment + approval).

## Inputs and outputs
- Input artifact: local pack configuration, governance source-record, and optional design provenance already copied under `./sources/`.
- Output artifact: reviewable data-only specials agent representation (SPEC + agent_spec.json) suitable for catalog and offline review.
- Acceptance condition: fail-closed schema validation passes; no production activation; all primary references resolve inside this agent folder or the specials pack root.

## Quality and critique
- Local rubric reference: `spagent.planner-agent-rubric` (inert identifier).
- Prompt reference: `spagent.planner-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.planner-agent-input"],"outputs":["spagent.planner-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.planner-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.planner-agent-prompt","rubric_reference":"spagent.planner-agent-rubric","critique_edges":{"inputs":["spagent.planner-agent-input"],"outputs":["spagent.planner-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.planner-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/planner_agent.md`
- Design source SHA-256 (at generation): `8b69afb197418ecd41f2af3e502afa70e0b77a355dd511eeffc60151fd01af79`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.
