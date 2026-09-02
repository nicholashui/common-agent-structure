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
    "max_input_tokens": 1,
    "max_output_tokens": 1,
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
      "title": "信息检索导论",
      "isbn13": "9787115221704",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 信息检索导论，ISBN-13 9787115221704"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "推荐系统实践",
      "author": "项亮",
      "isbn13": "9787115281708",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 推荐系统实践（项亮），ISBN-13 9787115281708"
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
      "author": "Aurélien Géron",
      "isbn13": "9781098125974",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Hands-On Machine Learning, 3rd ed. (Aurélien Géron), ISBN-13 9781098125974"
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
      "title": "人工智能：一种现代的方法",
      "author": "第4版",
      "isbn13": "9787111547044",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 人工智能：一种现代的方法（第4版），ISBN-13 9787111547044"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "深度学习",
      "author": "花书",
      "isbn13": "9787115461476",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 深度学习（花书），ISBN-13 9787115461476"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "机器学习",
      "author": "周志华",
      "isbn13": "9787302373575",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 机器学习（周志华），ISBN-13 9787302373575"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "统计学习方法",
      "author": "李航",
      "isbn13": "9787302423288",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 统计学习方法（李航），ISBN-13 9787302423288"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "强化学习",
      "author": "第2版",
      "isbn13": "9787115546081",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 强化学习（第2版），ISBN-13 9787115546081"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "数据密集型应用系统设计",
      "isbn13": "9787111547532",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 数据密集型应用系统设计，ISBN-13 9787111547532"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "超级智能",
      "isbn13": "9787508663098",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 超级智能，ISBN-13 9787508663098"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "生命3.0",
      "isbn13": "9787508684031",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 生命3.0，ISBN-13 9787508684031"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "动手学深度学习",
      "author": "李沐等",
      "isbn13": "9787115547460",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 动手学深度学习（李沐等），ISBN-13 9787115547460"
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
      "title": "代码整洁之道",
      "isbn13": "9787115216878",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 代码整洁之道，ISBN-13 9787115216878"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "设计模式",
      "isbn13": "9787111075752",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 设计模式，ISBN-13 9787111075752"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "SRE：Google运维解密",
      "isbn13": "9787115419903",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: SRE：Google运维解密，ISBN-13 9787115419903"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "程序员修炼之道",
      "isbn13": "9787115527684",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 程序员修炼之道，ISBN-13 9787115527684"
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
      "author": "Tomaž Bratanič, Oskar Hane",
      "isbn13": "9781633436268",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Essential GraphRAG (Tomaž Bratanič, Oskar Hane), ISBN-13 9781633436268"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "大模型RAG实战：RAG原理、应用与系统构建",
      "author": "汪鹏, 谷清水, 卞龙鹏",
      "isbn13": "9787111761990",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 大模型RAG实战：RAG原理、应用与系统构建（汪鹏, 谷清水, 卞龙鹏），ISBN-13 9787111761990"
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
      "title": "Building Natural Language and LLM Pipelines Build production-grade RAG, tool contracts,…",
      "author": "Laura Funderburk",
      "isbn13": "9781835467008",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building Natural Language and LLM Pipelines Build production-grade RAG, tool contracts,… (Laura Funderburk), ISBN-13 9781835467008"
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
      "title": "大模型应用开发：RAG入门与实战 大语言模型大模型多模态Prompt提示词工程RAG检索增强生成技术",
      "isbn13": "9787115648938",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 大模型应用开发：RAG入门与实战 大语言模型大模型多模态Prompt提示词工程RAG检索增强生成技术，ISBN-13 9787115648938"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangChain開發手冊：OpenAI × LCEL 表達式 × Agent 自動化流程 × RAG 擴展模型知識 × 圖形資料庫 × LangSmith 除錯工具",
      "isbn13": "9789863127918",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangChain開發手冊：OpenAI × LCEL 表達式 × Agent 自動化流程 × RAG 擴展模型知識 × 圖形資料庫 × LangSmith 除錯工具，ISBN-13 9789863127918"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "大模型RAG应用开发：构建智能生成系统",
      "isbn13": "9787302685982",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 大模型RAG应用开发：构建智能生成系统，ISBN-13 9787302685982"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LlamaIndex大模型RAG开发实践",
      "isbn13": "9787302697084",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LlamaIndex大模型RAG开发实践，ISBN-13 9787302697084"
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
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\specials\\agents\\specials.knowledge-router-agent",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```
