# Psychological Profile Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.psychological-profile-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain psychological profile agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

Provide personalized parameter configurations for the framework in this chapter and Appendix A workflow **File Structure:** - Basic information (code, age, professional background) - Psychological traits (MBTI tendencies, motivation types, fear patterns) - Creation parameters (best tools, time allocation, support needs) - Framework adaptation (key focuses for each stage, predicted obstacles, success strategies)

### Domain distillation (embedded, untrusted design provenance)

Provide personalized parameter configurations for the framework in this chapter and Appendix A workflow **File Structure:** - Basic information (code, age, professional background) - Psychological traits (MBTI tendencies, motivation types, fear patterns) - Creation parameters (best tools, time allocation, support needs) - Framework adaptation (key focuses for each stage, predicted obstacles, success strategies)

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
- Local rubric reference: `spagent.psychological-profile-agent-rubric` (inert identifier).
- Prompt reference: `spagent.psychological-profile-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.psychological-profile-agent-input"],"outputs":["spagent.psychological-profile-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.psychological-profile-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.psychological-profile-agent-prompt","rubric_reference":"spagent.psychological-profile-agent-rubric","critique_edges":{"inputs":["spagent.psychological-profile-agent-input"],"outputs":["spagent.psychological-profile-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.psychological-profile-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/psychological_profile_agent.md`
- Design source SHA-256 (at generation): `f1fa518cee669e11195bf6fcc62a63d2befa84c3d8c06a08afc22fecde9c495b`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.
