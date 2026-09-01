# Agentic Rag Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.agentic-rag-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain agentic rag agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

** Initial Prompt to task.md from Creator **
```
# How to create backend services
FIRST:
Conduct a comprehensive analysis and research of the task.md file to fully understand all requirements, specifications, 
and technical details. Based on this analysis, design and implement a complete backend server architecture that fulfills 
all outlined requirements. The backend server must be created within a dedicated 'backend' folder structure. Ensure the 
implementation includes proper API endpoints, database schema design, authentication mechanisms, error handling, logging 
systems, and follows RESTful principles. Document all API endpoints with clear specifications, implement comprehensive 
unit and integration tests, and verify that the server handles all edge cases and scalability requirements mentioned in 
task.md.
THEN:
Configure the application to integrate with GROK from x.ai by utilizing the environment variables defined in backend/.env  . 
Update all relevant codebase components to establish GROK as the primary Large Language Model (LLM) provider. This includes 
modifying API connection configurations, authentication parameters, model endpoints, and any existing LLM integration code 
to ensure seamless communication with GROK services. Implement proper error handling, rate limiting, and fallback mechanisms.
Verify the integration by testing all LLM-dependent features including text generation, chat completions, and any custom 
model interactions. Document the configuration changes and ensure backward compatibility where applicable. ```
**Task Owner:** Coding Agent  
**Priority:** Critical  
**Estimated Effort:** 10–14 days (MVP core in 6 days; full scale, hybrid integration, wiki compounding, observability & benchmarks in remaining days)  
**Goal:** Deliver a **complete, production-ready, observable, evaluable, extensible, and benchmarked Agentic RAG system** that **precisely** implements the **4 Core Agentic Design Patterns** and **7 Architectural Elements** from the survey paper "Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG" (arXiv:2501.09136, v4 as of April 2026) and the YouTube video "Agentic RAG Overview: 4 Core Principles and 7 Architectural Elements!" (https://youtu.be/MT3DM82PRLc).

### Domain distillation (embedded, untrusted design provenance)

** Initial Prompt to task.md from Creator **
```
# How to create backend services
FIRST:
Conduct a comprehensive analysis and research of the task.md file to fully understand all requirements, specifications, 
and technical details. Based on this analysis, design and implement a complete backend server architecture that fulfills 
all outlined requirements. The backend server must be created within a dedicated 'backend' folder structure. Ensure the 
implementation includes proper API endpoints, database schema design, authentication mechanisms, error handling, logging 
systems, and follows RESTful principles. Document all API endpoints with clear specifications, implement comprehensive 
unit and integration tests, and verify that the server handles all edge cases and scalability requirements mentioned in 
task.md.
THEN:
Configure the application to integrate with GROK from x.ai by utilizing the environment variables defined in backend/.env  . 
Update all relevant codebase components to establish GROK as the primary Large Language Model (LLM) provider. This includes 
modifying API connection configurations, authentication parameters, model endpoints, and any existing LLM integration code 
to ensure seamless communication with GROK services. Implement proper error handling, rate limiting, and fallback mechanisms.
Verify the integration by testing all LLM-dependent features including text generation, chat completions, and any custom 
model interactions. Document the configuration changes and ensure backward compatibility where applicable. ```
**Task Owner:** Coding Agent  
**Priority:** Critical  
**Estimated Effort:** 10–14 days (MVP core in 6 days; full scale, hybrid integration, wiki compounding, observability & benchmarks in remaining days)  
**Goal:** Deliver a **complete, production-ready, observable, evaluable, extensible, and benchmarked Agentic RAG system** that **precisely** implements the **4 Core Agentic Design Patterns** and **7 Architectural Elements** fro

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
- Local rubric reference: `spagent.agentic-rag-agent-rubric` (inert identifier).
- Prompt reference: `spagent.agentic-rag-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.agentic-rag-agent-input"],"outputs":["spagent.agentic-rag-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.agentic-rag-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.agentic-rag-agent-prompt","rubric_reference":"spagent.agentic-rag-agent-rubric","critique_edges":{"inputs":["spagent.agentic-rag-agent-input"],"outputs":["spagent.agentic-rag-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.agentic-rag-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/agentic_rag_agent.md`
- Design source SHA-256 (at generation): `7478e9fe106a7f750c76f90eeb45f44f46946facd2516e88bb3cb52e71cfb829`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.
