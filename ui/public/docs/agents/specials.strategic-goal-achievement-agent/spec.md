# specials.strategic-goal-achievement-agent — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/specials.strategic-goal-achievement-agent/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "specials.strategic-goal-achievement-agent",
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
      "spagent.strategic-goal-achievement-agent-input"
    ],
    "outputs": [
      "spagent.strategic-goal-achievement-agent-output"
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

# Strategic Goal Achievement Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.strategic-goal-achievement-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain strategic goal achievement agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

You are a strategic goal achievement coach, specializing in helping users clarify, plan, and effectively execute their goals. When users propose any goal (e.g., creative projects, business plans, skill learning, personal growth), your primary task is to guide them through a structured **self-questioning and self-answering** iterative framework. This framework is inspired by Socratic dialogue and deep self-reflection, applicable to any type of goal. It is divided into six stages: Motivation and Purpose, Audience and Context, Methods and Constraints, Emotional Expectations, Execution and Impact, and Iteration and Reflection. Each stage requires the user to continuously ask themselves questions, answer them, and evaluate whether the answers are "acceptable," until achieving clear and actionable insights.

### Domain distillation (embedded, untrusted design provenance)

Positioning You are a strategic goal achievement coach, specializing in helping users clarify, plan, and effectively execute their goals. When users propose any goal (e.g., creative projects, business plans, skill learning, personal growth), your primary task is to guide them through a structured **self-questioning and self-answering** iterative framework.

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
- Local rubric reference: `spagent.strategic-goal-achievement-agent-rubric` (inert identifier).
- Prompt reference: `spagent.strategic-goal-achievement-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.strategic-goal-achievement-agent-input"],"outputs":["spagent.strategic-goal-achievement-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.strategic-goal-achievement-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.strategic-goal-achievement-agent-prompt","rubric_reference":"spagent.strategic-goal-achievement-agent-rubric","critique_edges":{"inputs":["spagent.strategic-goal-achievement-agent-input"],"outputs":["spagent.strategic-goal-achievement-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.strategic-goal-achievement-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/strategic_goal_achievement_agent.md`
- Design source SHA-256 (at generation): `3c2d1bcc4fa2462c2c728074671cdb8afac9abad1d4da7cab378aee1b681c01d`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.

## Prompts

### `prompts/primary.md`

You are a baseline-safe specials pack agent. No network. No production activation.

# Strategic Goal Achievement Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.strategic-goal-achievement-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain strategic goal achievement agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

You are a strategic goal achievement coach, specializing in helping users clarify, plan, and effectively execute their goals. When users propose any goal (e.g., creative projects, business plans, skill learning, personal growth), your primary task is to guide them through a structured **self-questioning and self-answering** iterative framework. This framework is inspired by Socratic dialogue and deep self-reflection, applicable to any type of goal. It is divided into six stages: Motivation and Purpose, Audience and Context, Methods and Constraints, Emotional Expectations, Execution and Impact, and Iteration and Reflection. Each stage requires the user to continuously ask themselves questions, answer them, and evaluate whether the answers are "acceptable," until achieving clear and actionable insights.

### Domain distillation (embedded, untrusted design provenance)

Positioning You are a strategic goal achievement coach, specializing in helping users clarify, plan, and effectively execute their goals. When users propose any goal (e.g., creative projects, business plans, skill learning, personal growth), your primary task is to guide them through a structured **self-questioning and self-answering** iterative framework.

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
- Local rubric reference: `spagent.strategic-goal-achievement-agent-rubric` (inert identifier).
- Prompt reference: `spagent.strategic-goal-achievement-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.strategic-goal-achievement-agent-input"],"outputs":["spagent.strategic-goal-achievement-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.strategic-goal-achievement-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_ou

## Rubrics

### `rubrics/primary.md`

Success: stay inside pack responsibility; no network; no production activation.

## Sources

### `sources/MAPPING.md`

# Source mapping note — `specials.strategic-goal-achievement-agent`

- Mapping status: `related` (specials redesign doc → pack agent)
- Design source (historical): `docs/special_agents_redesign/agents/strategic_goal_achievement_agent.md`
- Source SHA-256: `3c2d1bcc4fa2462c2c728074671cdb8afac9abad1d4da7cab378aee1b681c01d`
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
      "title": "Competitive Strategy",
      "author": "Michael E. Porter",
      "isbn13": "9780684841489",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Competitive Strategy (Michael E. Porter), ISBN-13 9780684841489"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Good Strategy/Bad Strategy",
      "author": "Richard Rumelt",
      "isbn13": "9780307886231",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Good Strategy/Bad Strategy (Richard Rumelt), ISBN-13 9780307886231"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Playing to Win",
      "author": "Lafley & Martin",
      "isbn13": "9781422187395",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Playing to Win (Lafley & Martin), ISBN-13 9781422187395"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Measure What Matters",
      "author": "John Doerr",
      "isbn13": "9780525538318",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Measure What Matters (John Doerr), ISBN-13 9780525538318"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Innovator's Dilemma",
      "author": "Clayton Christensen",
      "isbn13": "9781633691780",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Innovator's Dilemma (Clayton Christensen), ISBN-13 9781633691780"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Thinking in Systems",
      "author": "Donella Meadows",
      "isbn13": "9781603580557",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Thinking in Systems (Donella Meadows), ISBN-13 9781603580557"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Fifth Discipline",
      "author": "Peter Senge",
      "isbn13": "9780385517256",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Fifth Discipline (Peter Senge), ISBN-13 9780385517256"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Superforecasting",
      "author": "Tetlock & Gardner",
      "isbn13": "9780804136716",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Superforecasting (Tetlock & Gardner), ISBN-13 9780804136716"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "竞争战略",
      "isbn13": "9787508633749",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 竞争战略，ISBN-13 9787508633749"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "好战略，坏战略",
      "isbn13": "9787508643427",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 好战略，坏战略，ISBN-13 9787508643427"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "这就是OKR",
      "isbn13": "9787521702330",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 这就是OKR，ISBN-13 9787521702330"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "创新者的窘境",
      "isbn13": "9787508633336",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 创新者的窘境，ISBN-13 9787508633336"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "系统之美",
      "isbn13": "9787508640114",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 系统之美，ISBN-13 9787508640114"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "第五项修炼",
      "isbn13": "9787508631332",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 第五项修炼，ISBN-13 9787508631332"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "超预测",
      "isbn13": "9787508663098",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 超预测，ISBN-13 9787508663098"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "金字塔原理",
      "isbn13": "9787508633732",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 金字塔原理，ISBN-13 9787508633732"
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
      "title": "Thinking, Fast and Slow",
      "author": "Daniel Kahneman",
      "isbn13": "9780374533557",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Thinking, Fast and Slow (Daniel Kahneman), ISBN-13 9780374533557"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Influence",
      "author": "Robert Cialdini",
      "isbn13": "9780061241895",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Influence (Robert Cialdini), ISBN-13 9780061241895"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Predictably Irrational",
      "author": "Dan Ariely",
      "isbn13": "9780061353246",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Predictably Irrational (Dan Ariely), ISBN-13 9780061353246"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Nudge",
      "author": "Thaler & Sunstein",
      "isbn13": "9780143115267",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Nudge (Thaler & Sunstein), ISBN-13 9780143115267"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Flow",
      "author": "Mihaly Csikszentmihalyi",
      "isbn13": "9780061339202",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Flow (Mihaly Csikszentmihalyi), ISBN-13 9780061339202"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Drive",
      "author": "Daniel H. Pink",
      "isbn13": "9781594484803",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Drive (Daniel H. Pink), ISBN-13 9781594484803"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Mindset",
      "author": "Carol Dweck",
      "isbn13": "9780345472328",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Mindset (Carol Dweck), ISBN-13 9780345472328"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Power of Habit",
      "author": "Charles Duhigg",
      "isbn13": "9780812981605",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Power of Habit (Charles Duhigg), ISBN-13 9780812981605"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Emotional Intelligence",
      "author": "Daniel Goleman",
      "isbn13": "9780553383713",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Emotional Intelligence (Daniel Goleman), ISBN-13 9780553383713"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Personality",
      "author": "Daniel Nettle",
      "isbn13": "9780199211425",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Personality (Daniel Nettle), ISBN-13 9780199211425"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "思考，快与慢",
      "isbn13": "9787508633565",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 思考，快与慢，ISBN-13 9787508633565"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "影响力",
      "isbn13": "9787508622163",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 影响力，ISBN-13 9787508622163"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "怪诞行为学",
      "isbn13": "9787508615824",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 怪诞行为学，ISBN-13 9787508615824"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "助推",
      "isbn13": "9787508641238",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 助推，ISBN-13 9787508641238"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "心流",
      "isbn13": "9787508660721",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 心流，ISBN-13 9787508660721"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "驱动力",
      "isbn13": "9787508621753",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 驱动力，ISBN-13 9787508621753"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "社会心理学",
      "author": "迈尔斯",
      "isbn13": "9787115412393",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 社会心理学（迈尔斯），ISBN-13 9787115412393"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "TRIZ进阶及实战",
      "author": "赵敏 张武城 王冠殊",
      "isbn13": "9787111518488",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: TRIZ进阶及实战（赵敏 张武城 王冠殊），ISBN-13 9787111518488"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "创新思维与TRIZ创新方法",
      "isbn13": "9787302500117",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 创新思维与TRIZ创新方法，ISBN-13 9787302500117"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "因果推理：基础与学习算法",
      "author": "Jonas Peters, Dominik Janzing etc.",
      "isbn13": "9787111640301",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 因果推理：基础与学习算法（Jonas Peters, Dominik Janzing etc.），ISBN-13 9787111640301"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "如何系统思考",
      "author": "邱昭良",
      "isbn13": "9787111585893",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 如何系统思考（邱昭良），ISBN-13 9787111585893"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "思维模型",
      "author": "彼得·霍林斯 (Peter Hollins)",
      "isbn13": "9787515360744",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 思维模型 (彼得·霍林斯 (Peter Hollins))，ISBN-13 9787515360744"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "把問題化繁為簡的思考架構圖鑑",
      "isbn13": "9789865070885",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 把問題化繁為簡的思考架構圖鑑，ISBN-13 9789865070885"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "案例解析！超高效心智圖法入門",
      "author": "孫易新",
      "isbn13": "9789862729496",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 案例解析！超高效心智圖法入門（孫易新），ISBN-13 9789862729496"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "模型思维 The Model Thinker",
      "author": "斯科特·佩奇 Scott E. Page",
      "isbn13": "9787213095436",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 模型思维 The Model Thinker（斯科特·佩奇 Scott E. Page），ISBN-13 9787213095436"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "灰度决策：如何处理复杂、棘手、高风险的难题",
      "author": "小约瑟夫·巴达拉克",
      "isbn13": "9787111584643",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 灰度决策：如何处理复杂、棘手、高风险的难题（小约瑟夫·巴达拉克），ISBN-13 9787111584643"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "科学分析--逻辑与科学演绎方法",
      "author": "周建武",
      "isbn13": "9787122371232",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 科学分析--逻辑与科学演绎方法（周建武），ISBN-13 9787122371232"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Strategic-Thinking-in-Complex-Problem-Solving",
      "isbn13": "9780190463908",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Strategic-Thinking-in-Complex-Problem-Solving, ISBN-13 9780190463908"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "严密系统设计-方法、趋势与挑战",
      "author": "【法】【希腊】约瑟夫·希发基思",
      "isbn13": "9787121467653",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 严密系统设计-方法、趋势与挑战（【法】【希腊】约瑟夫·希发基思），ISBN-13 9787121467653"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "TRIZ：产品创新设计",
      "author": "高常青",
      "isbn13": "9787111610298",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: TRIZ：产品创新设计（高常青），ISBN-13 9787111610298"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "架构师启示录-知识模型、落地方法与思维模式",
      "author": "灵犀",
      "isbn13": "9787111749080",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 架构师启示录-知识模型、落地方法与思维模式（灵犀），ISBN-13 9787111749080"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "模型思维简化世界的人工智能模型",
      "author": "龚才春",
      "isbn13": "9787121408984",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 模型思维简化世界的人工智能模型（龚才春），ISBN-13 9787121408984"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "分析思维的准则",
      "isbn13": "9787573917065",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 分析思维的准则，ISBN-13 9787573917065"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "战略思维的六项修炼",
      "isbn13": "9787521773033",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 战略思维的六项修炼，ISBN-13 9787521773033"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "第一性原理：21堂科学通识课",
      "isbn13": "9787523605103",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 第一性原理：21堂科学通识课，ISBN-13 9787523605103"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "百知思维模型从模型应用到思维探源",
      "author": "圆中",
      "isbn13": "9787572295386",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 百知思维模型从模型应用到思维探源（圆中），ISBN-13 9787572295386"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "100+思维模型合集",
      "author": "模型思维",
      "isbn13": "9787115652201",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 100+思维模型合集（模型思维），ISBN-13 9787115652201"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "穷查理宝典：查理·芒格智慧箴言录（全新增订本）（价值投资圣经，人生智慧宝典。全新升级版发布！97岁的查理•芒格还在不断学习精进 我们怎么...",
      "isbn13": "9787521730401",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 穷查理宝典：查理·芒格智慧箴言录（全新增订本）（价值投资圣经，人生智慧宝典。全新升级版发布！97岁的查理•芒格还在不断学习精进 我们怎么...，ISBN-13 9787521730401"
    }
  ],
  "common_agent_id": "specials.strategic-goal-achievement-agent",
  "pack_id": "specials",
  "mapping_status": "related",
  "source_documents": [
    "docs/special_agents_redesign/agents/strategic_goal_achievement_agent.md"
  ],
  "source_sha256": "3c2d1bcc4fa2462c2c728074671cdb8afac9abad1d4da7cab378aee1b681c01d",
  "configuration_sha256": "7b065cbc88a68106c980927c9db3c61eacaa28db19609700305a14e72f328a01",
  "destination_commit": "5460c4b4a33c15286f9fd84b1bc764d755f5bab0",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "generated_at": "2026-07-26T14:16:45.995185Z",
  "reviewed_by": "specials-self-contained-reviewer",
  "reviewed_at": "2026-07-26T18:00:00Z",
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\specials\\agents\\specials.strategic-goal-achievement-agent",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```
