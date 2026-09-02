# specials.agent-loop-creator — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/specials.agent-loop-creator/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "specials.agent-loop-creator",
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
      "spagent.agent-loop-creator-input"
    ],
    "outputs": [
      "spagent.agent-loop-creator-output"
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

# Agent Loop Creator

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.agent-loop-creator`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain agent loop creator design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

Actionable reference for building reliable, scalable LLM-based agent systems. Combines academic foundations (ReAct synergy of reasoning + acting), xAI's server-side agentic implementation (multi-agent orchestration for deep research), and advanced hierarchical patterns (planner + specialists + self-evolution). **Target Audience:** Builders of harnesses, multi-agent systems, coding agents, research agents (e.g., N1ch01as-style Architect with critic/self-refinement loops). **Key Principle:** Controlled loops with explicit state, structured outputs, quality gates, and hierarchical delegation. Not uncontrolled chain reactions — managed orchestration with bubbling-up consolidation and deliberate synthesis.

### Domain distillation (embedded, untrusted design provenance)

Actionable reference for building reliable, scalable LLM-based agent systems. Combines academic foundations (ReAct synergy of reasoning + acting), xAI's server-side agentic implementation (multi-agent orchestration for deep research), and advanced hierarchical patterns (planner + specialists + self-evolution). **Target Audience:** Builders of harnesses, multi-agent systems, coding agents, research agents (e.g., N1ch01as-style Architect with critic/self-refinement loops). **Key Principle:** Controlled loops with explicit state, structured outputs, quality gates, and hierarchical delegation. Not uncontrolled chain reactions — managed orchestration with bubbling-up consolidation and deliberate synthesis.

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
- Local rubric reference: `spagent.agent-loop-creator-rubric` (inert identifier).
- Prompt reference: `spagent.agent-loop-creator-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.agent-loop-creator-input"],"outputs":["spagent.agent-loop-creator-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.agent-loop-creator","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.agent-loop-creator-prompt","rubric_reference":"spagent.agent-loop-creator-rubric","critique_edges":{"inputs":["spagent.agent-loop-creator-input"],"outputs":["spagent.agent-loop-creator-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.agent-loop-creator.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/agent_loop_creator.md`
- Design source SHA-256 (at generation): `f0fcb85210fa5fa9827e23f4a2505d2d24caab8df6dabb7f1ea2f007529aa0ea`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.

## Prompts

### `prompts/primary.md`

# Agent Loop Creator — offline Host prompt (specials.agent-loop-creator)

You design and govern **controlled agent loops** for the Host pack harness.

## Offline Host foundation (agent_loop_v3 lite)
1. **Cynefin** — classify goal context → Fast vs Full intensity.
2. **Premortem** — assume failure → mitigations before Act.
3. **Bounded steps** — max_steps + action digests (no infinite thrash).
4. **Plan→Act→Self-Review** — pack runner + Host tool registry (stub-by-default).
5. **Multi-mode critics** — standard | red_team | paul_elder | six_hats (blockers vs warnings).
6. **AAR + Double-Loop scaffold** — structured reflection; no auto prompt mutation.
7. **Pattern store** — RPD token-overlap fast path on similar successful goals.

## Hard rules
- Fail-closed: no production_media / network on agent-loop Act.
- Registered pack agents only (closed world).
- Do not claim full multi-step LLM ReAct, TextGrad self-evolution, or live multi-agent orchestration.
- Package / publish remains human-gated.

### `prompts/SYSTEM.md`

# Agent Loop Creator — offline Host prompt (specials.agent-loop-creator)

You design and govern **controlled agent loops** for the Host pack harness.

## Offline Host foundation (agent_loop_v3 lite)
1. **Cynefin** — classify goal context → Fast vs Full intensity.
2. **Premortem** — assume failure → mitigations before Act.
3. **Bounded steps** — max_steps + action digests (no infinite thrash).
4. **Plan→Act→Self-Review** — pack runner + Host tool registry (stub-by-default).
5. **Multi-mode critics** — standard | red_team | paul_elder | six_hats (blockers vs warnings).
6. **AAR + Double-Loop scaffold** — structured reflection; no auto prompt mutation.
7. **Pattern store** — RPD token-overlap fast path on similar successful goals.

## Hard rules
- Fail-closed: no production_media / network on agent-loop Act.
- Registered pack agents only (closed world).
- Do not claim full multi-step LLM ReAct, TextGrad self-evolution, or live multi-agent orchestration.
- Package / publish remains human-gated.

## Rubrics

### `rubrics/L2.md`

# Agent Loop L2 rubric (offline Host v3 foundation)

Pass when `/api/v1/agent-loops/agents/{id}/run` with `enable_v3=true` produces:

| Check | Gate |
|-------|------|
| v3 envelope | `result.v3` present with cynefin + premortem + aar |
| Steps bounded | `v3.step_count` ≤ max_steps (default 3–8) |
| Patterns listed | includes Cynefin, Premortem, AAR |
| Fail-closed | allow_production / allow_network denied |
| Core harness | tool_invocations present; L1/L2 attached |

Fail / escalate:

- Critic **blockers** non-empty (not mere warnings)
- Cycle detection with no replan bound
- Production/network flags requested

Full agent_loop_v3 production (live LLM ReAct, TextGrad versioning, multi-agent leader teams) is **not** enforced offline.

### `rubrics/primary.md`

# Agent Loop L2 rubric (offline Host v3 foundation)

Pass when `/api/v1/agent-loops/agents/{id}/run` with `enable_v3=true` produces:

| Check | Gate |
|-------|------|
| v3 envelope | `result.v3` present with cynefin + premortem + aar |
| Steps bounded | `v3.step_count` ≤ max_steps (default 3–8) |
| Patterns listed | includes Cynefin, Premortem, AAR |
| Fail-closed | allow_production / allow_network denied |
| Core harness | tool_invocations present; L1/L2 attached |

Fail / escalate:

- Critic **blockers** non-empty (not mere warnings)
- Cycle detection with no replan bound
- Production/network flags requested

Full agent_loop_v3 production (live LLM ReAct, TextGrad versioning, multi-agent leader teams) is **not** enforced offline.

## Sources

### `sources/MAPPING.md`

# Source mapping note — `specials.agent-loop-creator`

- Mapping status: `related` (specials redesign doc → pack agent)
- Design source (historical): `docs/special_agents_redesign/agents/agent_loop_creator.md`
- Source SHA-256: `f0fcb85210fa5fa9827e23f4a2505d2d24caab8df6dabb7f1ea2f007529aa0ea`
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
      "title": "Introduction to Information Retrieval",
      "author": "Manning, Raghavan, Schütze",
      "isbn13": "9780521865715",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Introduction to Information Retrieval (Manning, Raghavan, Schütze), ISBN-13 9780521865715"
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
      "title": "信息检索导论",
      "isbn13": "9787115221704",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 信息检索导论，ISBN-13 9787115221704"
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
      "title": "A Guide to the Project Management Body of Knowledge (PMBOK Guide), 7th ed.",
      "isbn13": "9781628256642",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: A Guide to the Project Management Body of Knowledge (PMBOK Guide), 7th ed., ISBN-13 9781628256642"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Mythical Man-Month",
      "author": "Frederick P. Brooks Jr.",
      "isbn13": "9780201835953",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Mythical Man-Month (Frederick P. Brooks Jr.), ISBN-13 9780201835953"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Goal",
      "author": "Eliyahu M. Goldratt",
      "isbn13": "9780884271956",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Goal (Eliyahu M. Goldratt), ISBN-13 9780884271956"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "High Output Management",
      "author": "Andrew S. Grove",
      "isbn13": "9780679762881",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: High Output Management (Andrew S. Grove), ISBN-13 9780679762881"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Checklist Manifesto",
      "author": "Atul Gawande",
      "isbn13": "9780312430009",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Checklist Manifesto (Atul Gawande), ISBN-13 9780312430009"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Critical Chain",
      "author": "Goldratt",
      "isbn13": "9780884271536",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Critical Chain (Goldratt), ISBN-13 9780884271536"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "项目管理知识体系指南",
      "author": "第7版",
      "isbn13": "9787111558477",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 项目管理知识体系指南（第7版），ISBN-13 9787111558477"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "人月神话",
      "isbn13": "9787302154419",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 人月神话，ISBN-13 9787302154419"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "目标",
      "isbn13": "9787508637020",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 目标，ISBN-13 9787508637020"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "高效能人士的七个习惯",
      "isbn13": "9787508092232",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 高效能人士的七个习惯，ISBN-13 9787508092232"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "agentic-design-patterns-chinese",
      "isbn13": "9783032014016",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: agentic-design-patterns-chinese, ISBN-13 9783032014016"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "智能体设计指南",
      "author": "云中江树",
      "isbn13": "9787111775843",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 智能体设计指南（云中江树），ISBN-13 9787111775843"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "大模型应用开发：动手做AI Agent",
      "author": "黄佳",
      "isbn13": "9787115642172",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 大模型应用开发：动手做AI Agent（黄佳），ISBN-13 9787115642172"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "构建Agentic AI系统",
      "author": "Anjanava Biswas, Wrick Talukdar",
      "isbn13": "9787302703983",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 构建Agentic AI系统（Anjanava Biswas, Wrick Talukdar），ISBN-13 9787302703983"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building Applications with AI Agents Designing and Implementing Multiagent Systems",
      "isbn13": "9781098176501",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building Applications with AI Agents Designing and Implementing Multiagent Systems, ISBN-13 9781098176501"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "AI Agent开发与应用：基于大模型的智能体构建",
      "author": "凌峰",
      "isbn13": "9787302685975",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: AI Agent开发与应用：基于大模型的智能体构建（凌峰），ISBN-13 9787302685975"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "AI Agents in Action",
      "author": "Micheal Lanham",
      "isbn13": "9781633436343",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: AI Agents in Action (Micheal Lanham), ISBN-13 9781633436343"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "AI Engineering Building Applications with Foundation Models",
      "author": "Chip Huyen",
      "isbn13": "9781098166304",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: AI Engineering Building Applications with Foundation Models (Chip Huyen), ISBN-13 9781098166304"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "从零开始构建大型语言模型Build a Large Language Model (From Scratch)",
      "author": "SEBASTIAN RASCHKA",
      "isbn13": "9781633437166",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 从零开始构建大型语言模型Build a Large Language Model (From Scratch)（SEBASTIAN RASCHKA），ISBN-13 9781633437166"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building AI Agent Platforms (for Isabel Garcia)",
      "author": "Ben OMahony and Fabian Nonnenmacher",
      "isbn13": "9798341666344",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building AI Agent Platforms (for Isabel Garcia) (Ben OMahony and Fabian Nonnenmacher), ISBN-13 9798341666344"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "大模型项目实战 多领域智能应用开发",
      "author": "高强文",
      "isbn13": "9787111762348",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 大模型项目实战 多领域智能应用开发（高强文），ISBN-13 9787111762348"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "LLM Engineer’s Handbook",
      "author": "Paul Iusztin ,Maxime Labonne",
      "isbn13": "9781836200079",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: LLM Engineer’s Handbook (Paul Iusztin ,Maxime Labonne), ISBN-13 9781836200079"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "An Illustrated Guide to AI Agents",
      "isbn13": "9798341662681",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: An Illustrated Guide to AI Agents, ISBN-13 9798341662681"
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
      "title": "Patterns for Building AI Agents",
      "author": "SAM BHAGWATMICHELLE GIENOW",
      "isbn13": "9798270198107",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Patterns for Building AI Agents (SAM BHAGWATMICHELLE GIENOW), ISBN-13 9798270198107"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "AI Agents with MCP (First Early Release)",
      "author": "Kyle Stratis",
      "isbn13": "9798341639508",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: AI Agents with MCP (First Early Release) (Kyle Stratis), ISBN-13 9798341639508"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Build a Multi-Agent System (from Scratch) With MCP and A2A",
      "author": "Val Andrei Fajardo",
      "isbn13": "9781633434660",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Build a Multi-Agent System (from Scratch) With MCP and A2A (Val Andrei Fajardo), ISBN-13 9781633434660"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building Generative AI Agents. Using LangGraph, AutoGen, and CrewAI 2025",
      "author": "Tom Taulli, Gaurav Deshmukh",
      "isbn13": "9798868811340",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building Generative AI Agents. Using LangGraph, AutoGen, and CrewAI 2025 (Tom Taulli, Gaurav Deshmukh), ISBN-13 9798868811340"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Ultimate Agentic AI with AutoGen for Enterprise Automation",
      "author": "Shekhar Agrawal, Srinivasa Sunil Chippada etc.",
      "isbn13": "9789349888951",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Ultimate Agentic AI with AutoGen for Enterprise Automation (Shekhar Agrawal, Srinivasa Sunil Chippada etc.), ISBN-13 9789349888951"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "从零构建大模型算法、训练与微调",
      "isbn13": "9787302685616",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 从零构建大模型算法、训练与微调，ISBN-13 9787302685616"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "多模态大模型 从理论到实践",
      "isbn13": "9787302686927",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 多模态大模型 从理论到实践，ISBN-13 9787302686927"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "AutoGPT Revolutionizing Automation with Generative AI",
      "author": "Kameron Hussain, Frahaan Hussain",
      "isbn13": "9798224989805",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: AutoGPT Revolutionizing Automation with Generative AI (Kameron Hussain, Frahaan Hussain), ISBN-13 9798224989805"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "这就是MCP",
      "author": "艾逗笔",
      "isbn13": "9787115677471",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 这就是MCP（艾逗笔），ISBN-13 9787115677471"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building Multimodal Generative AI and Agentic Applications Shaping concept to code for…",
      "isbn13": "9789365898385",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building Multimodal Generative AI and Agentic Applications Shaping concept to code for…, ISBN-13 9789365898385"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Agentic Architectural Patterns for Building Multi-Agent Systems",
      "isbn13": "9781806029570",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Agentic Architectural Patterns for Building Multi-Agent Systems, ISBN-13 9781806029570"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Agentic Mesh",
      "isbn13": "9798341621619",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Agentic Mesh, ISBN-13 9798341621619"
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
      "language": "ZH",
      "title": "MCP协议与AI Agent开发：标准、应用与实现",
      "isbn13": "9787302695349",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: MCP协议与AI Agent开发：标准、应用与实现，ISBN-13 9787302695349"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "MCP协议与大模型集成实战",
      "isbn13": "9787121503863",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: MCP协议与大模型集成实战，ISBN-13 9787121503863"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangChain核心技术与LLM项目实践",
      "author": "凌峰",
      "isbn13": "9787302685630",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangChain核心技术与LLM项目实践（凌峰），ISBN-13 9787302685630"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangChain 入门指南构建高可复用、可扩展的 LLM 应用程序",
      "author": "李特丽",
      "isbn13": "9787121467271",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangChain 入门指南构建高可复用、可扩展的 LLM 应用程序（李特丽），ISBN-13 9787121467271"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "AI Agents and Applications (MEAP, all 14 chapters) With LangChain, LangGraph, and MCP",
      "author": "Roberto Infante",
      "isbn13": "9781633436541",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: AI Agents and Applications (MEAP, all 14 chapters) With LangChain, LangGraph, and MCP (Roberto Infante), ISBN-13 9781633436541"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Learning LangChain Building AI and LLM Applications with LangChain and LangGraph",
      "author": "Mayo Oshin, Nuno Campos",
      "isbn13": "9781098167288",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Learning LangChain Building AI and LLM Applications with LangChain and LangGraph (Mayo Oshin, Nuno Campos), ISBN-13 9781098167288"
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
      "title": "Building Natural Language and LLM Pipelines Build production-grade RAG, tool contracts,…",
      "author": "Laura Funderburk",
      "isbn13": "9781835467008",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building Natural Language and LLM Pipelines Build production-grade RAG, tool contracts,… (Laura Funderburk), ISBN-13 9781835467008"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "多模态大模型 算法、应用与微调",
      "author": "刘兆峰",
      "isbn13": "9787111754886",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 多模态大模型 算法、应用与微调（刘兆峰），ISBN-13 9787111754886"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "AI Agent AI的下一个风口 智能体的核心技术讲解书籍 大模型时代的AI介绍书",
      "isbn13": "9787121474606",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: AI Agent AI的下一个风口 智能体的核心技术讲解书籍 大模型时代的AI介绍书，ISBN-13 9787121474606"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "官方正版 LangChain实战 从原型到生产 动手打造 LLM 应用",
      "isbn13": "9787121475450",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 官方正版 LangChain实战 从原型到生产 动手打造 LLM 应用，ISBN-13 9787121475450"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "正版包邮 LangChain编程 从入门到实践",
      "isbn13": "9787115639424",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 正版包邮 LangChain编程 从入门到实践，ISBN-13 9787115639424"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LLM串接所有服務：LangChain原型到產品全面開發",
      "isbn13": "9786267383919",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LLM串接所有服務：LangChain原型到產品全面開發，ISBN-13 9786267383919"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "極速ChatGPT開發者兵器指南：跨界整合Prompt Flow、LangChain與Semantic Kernel框架",
      "isbn13": "9786263338203",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 極速ChatGPT開發者兵器指南：跨界整合Prompt Flow、LangChain與Semantic Kernel框架，ISBN-13 9786263338203"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "生成式AI实战基于Transformer、Stable Diffusion、LangChain和AI Agent",
      "isbn13": "9787115650443",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 生成式AI实战基于Transformer、Stable Diffusion、LangChain和AI Agent，ISBN-13 9787115650443"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangChain技术解密 构建大模型应用的全景指南 王浩帆",
      "isbn13": "9787121477379",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangChain技术解密 构建大模型应用的全景指南 王浩帆，ISBN-13 9787121477379"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangChain大模型AI应用开发实践",
      "isbn13": "9787302672524",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangChain大模型AI应用开发实践，ISBN-13 9787302672524"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "AI Agent应用与项目实战",
      "isbn13": "9787121491818",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: AI Agent应用与项目实战，ISBN-13 9787121491818"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "一本书读懂AI Agent：技术、应用与商业",
      "isbn13": "9787111764168",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 一本书读懂AI Agent：技术、应用与商业，ISBN-13 9787111764168"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "大模型项目实战Agent开发与应用",
      "isbn13": "9787111777335",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 大模型项目实战Agent开发与应用，ISBN-13 9787111777335"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "MCP开发从入门到实战：人工智能AI智能体Agent应用开发",
      "isbn13": "9787115674142",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: MCP开发从入门到实战：人工智能AI智能体Agent应用开发，ISBN-13 9787115674142"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "AI Agent设计实战：智能体设计方法与技巧",
      "isbn13": "9787111779247",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: AI Agent设计实战：智能体设计方法与技巧，ISBN-13 9787111779247"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "MCP极简开发：轻松打造高效智能体 MCP开发教程 Agent智能体大语",
      "isbn13": "9787115674883",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: MCP极简开发：轻松打造高效智能体 MCP开发教程 Agent智能体大语，ISBN-13 9787115674883"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "A2A協議：多Agent系統全鏈路開發",
      "isbn13": "9787111791980",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: A2A協議：多Agent系統全鏈路開發，ISBN-13 9787111791980"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangGraph實戰──構建新一代 AI 智慧體系統",
      "isbn13": "9787121507007",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangGraph實戰──構建新一代 AI 智慧體系統，ISBN-13 9787121507007"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "MCP+A2A+LangGraph 驅動的智能體全流程開發",
      "isbn13": "9787115682024",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: MCP+A2A+LangGraph 驅動的智能體全流程開發，ISBN-13 9787115682024"
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
  "common_agent_id": "specials.agent-loop-creator",
  "pack_id": "specials",
  "mapping_status": "related",
  "source_documents": [
    "docs/special_agents_redesign/agents/agent_loop_creator.md"
  ],
  "source_sha256": "f0fcb85210fa5fa9827e23f4a2505d2d24caab8df6dabb7f1ea2f007529aa0ea",
  "configuration_sha256": "f4d0901574b4067a56c031472e08e991b4dfd026ab79978ba828d0b6b409a825",
  "destination_commit": "5460c4b4a33c15286f9fd84b1bc764d755f5bab0",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "generated_at": "2026-07-26T14:16:45.910882Z",
  "reviewed_by": "specials-self-contained-reviewer",
  "reviewed_at": "2026-07-26T18:00:00Z",
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\specials\\agents\\specials.agent-loop-creator",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```
