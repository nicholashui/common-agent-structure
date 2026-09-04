# specials.knowledge-router-agent — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/specials.knowledge-router-agent/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "specials.knowledge-router-agent",
  "status": "draft",
  "role": "Special_Agent data-only configuration",
  "allowed_tools": [],
  "allowed_plugins": [],
  "model_policy": {
    "provider": "local_deterministic",
    "model_id": "specials-local-deterministic-v1",
    "network_access": false,
    "routing_allowed": false
  },
  "budget_policy": {
    "max_input_tokens": 2048,
    "max_output_tokens": 1024,
    "max_model_calls": 2,
    "max_tool_requests": 0,
    "max_job_ms": 15000,
    "max_cost_units": 1.0,
    "max_peer_hops": 0
  },
  "prompt_reference": "prompts/primary.md",
  "rubric_reference": "rubrics/primary.md",
  "critique_edges": {
    "inputs": [
      "spagent.knowledge-router-agent-input"
    ],
    "outputs": [
      "spagent.knowledge-router-agent-output"
    ]
  },
  "max_refinement_count": 0,
  "production_activation_requested": false,
  "does_not_own": [
    "Credentials",
    "Silent production activation",
    "Another agent's exclusive craft output without handoff",
    "Automatic promotion of self-generated artifacts",
    "Modification of safety, telemetry, gates, permissions, or corrigibility",
    "Self-granting tools, plugins, network, or isolation downgrades"
  ],
  "va_id": null,
  "va_name": null,
  "va_category": null,
  "source_schema_version": "1.0",
  "inheritance_ref": "inheritance/parents.json",
  "identity_ref": "identity/",
  "skills_ref": "skills/bindings.json",
  "toggles_ref": "skills/toggles.json",
  "runtime_ref": "runtime/execution.json",
  "context_ref": "runtime/context.json",
  "compute_controller_ref": "runtime/compute_controller.json",
  "backends_ref": "runtime/backends.json",
  "cache_ref": "runtime/cache.json",
  "protocols_ref": "protocols/compatibility.json",
  "capability_assertions_ref": "protocols/capability_assertions.json",
  "observability_ref": "observability/telemetry.json",
  "sampling_ref": "observability/sampling.json",
  "plugins_ref": "plugins/registry.json",
  "isolation_ref": "plugins/isolation.json",
  "memory_ref": "memory/policy.json",
  "memory_hierarchy_ref": "memory/hierarchy.json",
  "memory_security_ref": "memory/security.json",
  "improvement_ref": "improvement/policy.json",
  "verifiers_ref": "improvement/verifiers.json",
  "safety_ref": "safety/policy.json",
  "termination_ref": "safety/termination.json",
  "corrigibility_ref": "corrigibility/invariants.json",
  "evals_ref": "evals/benchmarks.json",
  "analysis_plan_ref": "evals/analysis_plan.json"
}
```

## Folder specification (`SPEC.md`)

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

## Prompts

### `prompts/primary.md`

You are a baseline-safe specials pack agent. No network. No production activation.

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
- `allowed_tools` must stay empty; `network_access` must stay false; provider re

## Rubrics

### `rubrics/primary.md`

Success: stay inside pack responsibility; no network; no production activation.

## Sources

### `sources/MAPPING.md`

# Source mapping note — `specials.knowledge-router-agent`

- Mapping status: `related` (specials redesign doc → pack agent)
- Design source (historical): `docs/special_agents_redesign/agents/knowledge_router_agent.md`
- Source SHA-256: `688ef2556e2e072dddebe5d990cd0f6bb8c7386d194a319a80f7f95981e35e21`
- Local runtime: `agent_spec.json`
- Local specification: `SPEC.md`
- Pack corpus: **not required**
- Production activation: **denied** (draft only)

### `sources/PROVENANCE.json`

```json
{
  "schema_version": "3.0",
  "sources": [
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Introduction to Information Retrieval",
      "isbn13": "9780521865715",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Introduction to Information Retrieval, ISBN-13 9780521865715"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Mining of Massive Datasets",
      "author": "Leskovec, Rajaraman, Ullman",
      "isbn13": "9781107157873",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Mining of Massive Datasets (Leskovec, Rajaraman, Ullman), ISBN-13 9781107157873"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Recommender Systems Handbook, 2nd ed.",
      "author": "Ricci et al.",
      "isbn13": "9781489976369",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Recommender Systems Handbook, 2nd ed. (Ricci et al.), ISBN-13 9781489976369"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u4fe1\u606f\u68c0\u7d22\u5bfc\u8bba",
      "isbn13": "9787115221704",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4fe1\u606f\u68c0\u7d22\u5bfc\u8bba\uff0cISBN-13 9787115221704"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u63a8\u8350\u7cfb\u7edf\u5b9e\u8df5",
      "author": "\u9879\u4eae",
      "isbn13": "9787115281708",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u63a8\u8350\u7cfb\u7edf\u5b9e\u8df5\uff08\u9879\u4eae\uff09\uff0cISBN-13 9787115281708"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Artificial Intelligence: A Modern Approach, 4th ed.",
      "author": "Russell & Norvig",
      "isbn13": "9780134610993",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Artificial Intelligence: A Modern Approach, 4th ed. (Russell & Norvig), ISBN-13 9780134610993"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Multiagent Systems, 2nd ed.",
      "author": "Michael Wooldridge",
      "isbn13": "9780471496915",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Multiagent Systems, 2nd ed. (Michael Wooldridge), ISBN-13 9780471496915"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Deep Learning",
      "author": "Goodfellow, Bengio, Courville",
      "isbn13": "9780262035613",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Deep Learning (Goodfellow, Bengio, Courville), ISBN-13 9780262035613"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Hands-On Machine Learning, 3rd ed.",
      "author": "Aur\u00e9lien G\u00e9ron",
      "isbn13": "9781098125974",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Hands-On Machine Learning, 3rd ed. (Aur\u00e9lien G\u00e9ron), ISBN-13 9781098125974"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Reinforcement Learning, 2nd ed.",
      "author": "Sutton & Barto",
      "isbn13": "9780262039246",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Reinforcement Learning, 2nd ed. (Sutton & Barto), ISBN-13 9780262039246"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Speech and Language Processing, 2nd ed.",
      "author": "Jurafsky & Martin",
      "isbn13": "9780131873216",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Speech and Language Processing, 2nd ed. (Jurafsky & Martin), ISBN-13 9780131873216"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Designing Data-Intensive Applications",
      "author": "Martin Kleppmann",
      "isbn13": "9781449373320",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Designing Data-Intensive Applications (Martin Kleppmann), ISBN-13 9781449373320"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Human Compatible",
      "author": "Stuart Russell",
      "isbn13": "9780525558613",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Human Compatible (Stuart Russell), ISBN-13 9780525558613"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Alignment Problem",
      "author": "Brian Christian",
      "isbn13": "9780393635829",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Alignment Problem (Brian Christian), ISBN-13 9780393635829"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Superintelligence",
      "author": "Nick Bostrom",
      "isbn13": "9780199678112",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Superintelligence (Nick Bostrom), ISBN-13 9780199678112"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Weapons of Math Destruction",
      "author": "Cathy O'Neil",
      "isbn13": "9780553418811",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Weapons of Math Destruction (Cathy O'Neil), ISBN-13 9780553418811"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u4eba\u5de5\u667a\u80fd\uff1a\u4e00\u79cd\u73b0\u4ee3\u7684\u65b9\u6cd5",
      "author": "\u7b2c4\u7248",
      "isbn13": "9787111547044",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4eba\u5de5\u667a\u80fd\uff1a\u4e00\u79cd\u73b0\u4ee3\u7684\u65b9\u6cd5\uff08\u7b2c4\u7248\uff09\uff0cISBN-13 9787111547044"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6df1\u5ea6\u5b66\u4e60",
      "author": "\u82b1\u4e66",
      "isbn13": "9787115461476",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6df1\u5ea6\u5b66\u4e60\uff08\u82b1\u4e66\uff09\uff0cISBN-13 9787115461476"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u673a\u5668\u5b66\u4e60",
      "author": "\u5468\u5fd7\u534e",
      "isbn13": "9787302373575",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u673a\u5668\u5b66\u4e60\uff08\u5468\u5fd7\u534e\uff09\uff0cISBN-13 9787302373575"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7edf\u8ba1\u5b66\u4e60\u65b9\u6cd5",
      "author": "\u674e\u822a",
      "isbn13": "9787302423288",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7edf\u8ba1\u5b66\u4e60\u65b9\u6cd5\uff08\u674e\u822a\uff09\uff0cISBN-13 9787302423288"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5f3a\u5316\u5b66\u4e60",
      "author": "\u7b2c2\u7248",
      "isbn13": "9787115546081",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5f3a\u5316\u5b66\u4e60\uff08\u7b2c2\u7248\uff09\uff0cISBN-13 9787115546081"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6570\u636e\u5bc6\u96c6\u578b\u5e94\u7528\u7cfb\u7edf\u8bbe\u8ba1",
      "isbn13": "9787111547532",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6570\u636e\u5bc6\u96c6\u578b\u5e94\u7528\u7cfb\u7edf\u8bbe\u8ba1\uff0cISBN-13 9787111547532"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u8d85\u7ea7\u667a\u80fd",
      "isbn13": "9787508663098",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8d85\u7ea7\u667a\u80fd\uff0cISBN-13 9787508663098"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u751f\u547d3.0",
      "isbn13": "9787508684031",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u751f\u547d3.0\uff0cISBN-13 9787508684031"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u52a8\u624b\u5b66\u6df1\u5ea6\u5b66\u4e60",
      "author": "\u674e\u6c90\u7b49",
      "isbn13": "9787115547460",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u52a8\u624b\u5b66\u6df1\u5ea6\u5b66\u4e60\uff08\u674e\u6c90\u7b49\uff09\uff0cISBN-13 9787115547460"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Clean Code",
      "author": "Robert C. Martin",
      "isbn13": "9780132350884",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Clean Code (Robert C. Martin), ISBN-13 9780132350884"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Design Patterns",
      "author": "Gamma, Helm, Johnson, Vlissides",
      "isbn13": "9780201633610",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Design Patterns (Gamma, Helm, Johnson, Vlissides), ISBN-13 9780201633610"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Pragmatic Programmer, 20th Anniv.",
      "author": "Hunt & Thomas",
      "isbn13": "9780135957059",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Pragmatic Programmer, 20th Anniv. (Hunt & Thomas), ISBN-13 9780135957059"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Site Reliability Engineering",
      "author": "Beyer et al.",
      "isbn13": "9781491929124",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Site Reliability Engineering (Beyer et al.), ISBN-13 9781491929124"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Systems Performance, 2nd ed.",
      "author": "Brendan Gregg",
      "isbn13": "9780136820154",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Systems Performance, 2nd ed. (Brendan Gregg), ISBN-13 9780136820154"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u4ee3\u7801\u6574\u6d01\u4e4b\u9053",
      "isbn13": "9787115216878",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4ee3\u7801\u6574\u6d01\u4e4b\u9053\uff0cISBN-13 9787115216878"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u8bbe\u8ba1\u6a21\u5f0f",
      "isbn13": "9787111075752",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8bbe\u8ba1\u6a21\u5f0f\uff0cISBN-13 9787111075752"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "SRE\uff1aGoogle\u8fd0\u7ef4\u89e3\u5bc6",
      "isbn13": "9787115419903",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: SRE\uff1aGoogle\u8fd0\u7ef4\u89e3\u5bc6\uff0cISBN-13 9787115419903"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7a0b\u5e8f\u5458\u4fee\u70bc\u4e4b\u9053",
      "isbn13": "9787115527684",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7a0b\u5e8f\u5458\u4fee\u70bc\u4e4b\u9053\uff0cISBN-13 9787115527684"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Managing Memory for AI Agents",
      "isbn13": "9798341661257",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Managing Memory for AI Agents, ISBN-13 9798341661257"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building LLM Agents with RAG, Knowledge Graphs, and Reflection",
      "isbn13": "9798232017378",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building LLM Agents with RAG, Knowledge Graphs, and Reflection, ISBN-13 9798232017378"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Essential GraphRAG",
      "author": "Toma\u017e Bratani\u010d, Oskar Hane",
      "isbn13": "9781633436268",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Essential GraphRAG (Toma\u017e Bratani\u010d, Oskar Hane), ISBN-13 9781633436268"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5927\u6a21\u578bRAG\u5b9e\u6218\uff1aRAG\u539f\u7406\u3001\u5e94\u7528\u4e0e\u7cfb\u7edf\u6784\u5efa",
      "author": "\u6c6a\u9e4f, \u8c37\u6e05\u6c34, \u535e\u9f99\u9e4f",
      "isbn13": "9787111761990",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5927\u6a21\u578bRAG\u5b9e\u6218\uff1aRAG\u539f\u7406\u3001\u5e94\u7528\u4e0e\u7cfb\u7edf\u6784\u5efa\uff08\u6c6a\u9e4f, \u8c37\u6e05\u6c34, \u535e\u9f99\u9e4f\uff09\uff0cISBN-13 9787111761990"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "RAG with Python Cookbook (Early Release)",
      "author": "Dominik Polzer",
      "isbn13": "9798341600560",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: RAG with Python Cookbook (Early Release) (Dominik Polzer), ISBN-13 9798341600560"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building Natural Language and LLM Pipelines Build production-grade RAG, tool contracts,\u2026",
      "author": "Laura Funderburk",
      "isbn13": "9781835467008",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building Natural Language and LLM Pipelines Build production-grade RAG, tool contracts,\u2026 (Laura Funderburk), ISBN-13 9781835467008"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Unlocking Data with Generative AI and RAG",
      "isbn13": "9781806381654",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Unlocking Data with Generative AI and RAG, ISBN-13 9781806381654"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5927\u6a21\u578b\u5e94\u7528\u5f00\u53d1\uff1aRAG\u5165\u95e8\u4e0e\u5b9e\u6218 \u5927\u8bed\u8a00\u6a21\u578b\u5927\u6a21\u578b\u591a\u6a21\u6001Prompt\u63d0\u793a\u8bcd\u5de5\u7a0bRAG\u68c0\u7d22\u589e\u5f3a\u751f\u6210\u6280\u672f",
      "isbn13": "9787115648938",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5927\u6a21\u578b\u5e94\u7528\u5f00\u53d1\uff1aRAG\u5165\u95e8\u4e0e\u5b9e\u6218 \u5927\u8bed\u8a00\u6a21\u578b\u5927\u6a21\u578b\u591a\u6a21\u6001Prompt\u63d0\u793a\u8bcd\u5de5\u7a0bRAG\u68c0\u7d22\u589e\u5f3a\u751f\u6210\u6280\u672f\uff0cISBN-13 9787115648938"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangChain\u958b\u767c\u624b\u518a\uff1aOpenAI \u00d7 LCEL \u8868\u9054\u5f0f \u00d7 Agent \u81ea\u52d5\u5316\u6d41\u7a0b \u00d7 RAG \u64f4\u5c55\u6a21\u578b\u77e5\u8b58 \u00d7 \u5716\u5f62\u8cc7\u6599\u5eab \u00d7 LangSmith \u9664\u932f\u5de5\u5177",
      "isbn13": "9789863127918",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangChain\u958b\u767c\u624b\u518a\uff1aOpenAI \u00d7 LCEL \u8868\u9054\u5f0f \u00d7 Agent \u81ea\u52d5\u5316\u6d41\u7a0b \u00d7 RAG \u64f4\u5c55\u6a21\u578b\u77e5\u8b58 \u00d7 \u5716\u5f62\u8cc7\u6599\u5eab \u00d7 LangSmith \u9664\u932f\u5de5\u5177\uff0cISBN-13 9789863127918"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5927\u6a21\u578bRAG\u5e94\u7528\u5f00\u53d1\uff1a\u6784\u5efa\u667a\u80fd\u751f\u6210\u7cfb\u7edf",
      "isbn13": "9787302685982",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5927\u6a21\u578bRAG\u5e94\u7528\u5f00\u53d1\uff1a\u6784\u5efa\u667a\u80fd\u751f\u6210\u7cfb\u7edf\uff0cISBN-13 9787302685982"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LlamaIndex\u5927\u6a21\u578bRAG\u5f00\u53d1\u5b9e\u8df5",
      "isbn13": "9787302697084",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LlamaIndex\u5927\u6a21\u578bRAG\u5f00\u53d1\u5b9e\u8df5\uff0cISBN-13 9787302697084"
    }
  ],
  "common_agent_id": "specials.knowledge-router-agent",
  "pack_id": "specials",
  "mapping_status": "related",
  "source_documents": [
    "docs/special_agents_redesign/agents/knowledge_router_agent.md"
  ],
  "source_sha256": "688ef2556e2e072dddebe5d990cd0f6bb8c7386d194a319a80f7f95981e35e21",
  "configuration_sha256": "baed259a681006e50e157c77f39cdaae9364b0b833cef6433fce15802c14b20f",
  "destination_commit": "5460c4b4a33c15286f9fd84b1bc764d755f5bab0",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "generated_at": "2026-07-26T14:16:45.947252Z",
  "reviewed_by": "specials-self-contained-reviewer",
  "reviewed_at": "2026-07-26T18:00:00Z",
  "imported_from": "vendor/common-agent-swarm-ops/business/specials/agents/specials.knowledge-router-agent",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```
