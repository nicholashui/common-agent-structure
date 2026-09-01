# Knowledge Router Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.knowledge-router-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain knowledge router agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

The **Knowledge Router Agent** is the central intelligence layer that ensures every specialized agent in your system (Character Consistency Critic, Video Prompt Optimizer, Multi-Agent Orchestrator Designer, Shot Planning Agent, etc.) receives **precisely the right knowledge** from your growing ~5,000-file `.md` corpus — with minimal noise, high precision, and strong explainability. It draws from 2025–2026 research (AgentRouter’s graph-guided GNN routing with performance supervision, RopMura/RIRS centroid-based + iterative planning, Self-RAG reflection tokens, CRAG corrective retrieval, MasRouter unified routing, and production patterns from xAI Grok multi-agent modes) while being fully generalized for any knowledge-intensive domain. **Core Innovations in This Design** - **Hybrid Routing Stack** (Metadata-first → Cluster/Centroid semantic → Graph traversal → LLM ranker with reflection) - **Dual Planner + Router** for complex multi-hop creative/technical pipelines - **Built-in Multi-Level Critic** (retrieval quality, routing decision, downstream utility) inspired by Self-RAG - **Performance-Supervised Improvement** (soft labels from actual agent success, like AgentRouter) - **Traceable + Explainable** by design - **Training-free bootstrap** (RopMura style) with optional learned components - **Domain packs** for your key agents (Character Consistency, Prompt Engineering for Video, Agentic Video Production, etc.) This spec is ready for direct implementation or feeding into your N1ch01as Architect coding agents.

### Domain distillation (embedded, untrusted design provenance)

The **Knowledge Router Agent** is the central intelligence layer that ensures every specialized agent in your system (Character Consistency Critic, Video Prompt Optimizer, Multi-Agent Orchestrator Designer, Shot Planning Agent, etc.) receives **precisely the right knowledge** from your growing ~5,000-file `.md` corpus — with minimal noise, high precision, and strong explainability. It draws from 2025–2026 research (AgentRouter’s graph-guided GNN routing with performance supervision, RopMura/RIRS centroid-based + iterative planning, Self-RAG reflection tokens, CRAG corrective retrieval, MasRouter unified routing, and production patterns from xAI Grok multi-agent modes) while being fully generalized for any knowledge-intensive domain. **Core Innovations in This Design** - **Hybrid Routing Stack** (Metadata-first → Cluster/Centroid semantic → Graph traversal → LLM ranker with reflection) - **Dual Planner + Router** for complex multi-hop creative/technical pipelines - **Built-in Multi-Level Critic** (retrieval quality, routing decision, downstream utility) inspired by Self-RAG - **Performance-Supervised Improvement** (soft labels from actual agent success, like AgentRouter) - **Traceable + Explainable** by design - **Training-free bootstrap** (RopMura style) with optional learned components - **Domain packs** for your key agents (Character Consistency, Prompt Engineering for Video, Agentic Video Production, etc.) This spec is ready for direct implementation or feeding into your N1ch01as Architect coding agents.

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
- Local rubric reference: `spagent.knowledge-router-agent-rubric` (inert identifier).
- Prompt reference: `spagent.knowledge-router-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.knowledge-router-agent-input"],"outputs":["spagent.knowledge-router-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.knowledge-router-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.knowledge-router-agent-prompt","rubric_reference":"spagent.knowledge-router-agent-rubric","critique_edges":{"inputs":["spagent.knowledge-router-agent-input"],"outputs":["spagent.knowledge-router-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.knowledge-router-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/knowledge_router_agent.md`
- Design source SHA-256 (at generation): `688ef2556e2e072dddebe5d990cd0f6bb8c7386d194a319a80f7f95981e35e21`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.
