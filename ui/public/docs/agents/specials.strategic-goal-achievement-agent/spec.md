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
      "title": "\u7ade\u4e89\u6218\u7565",
      "isbn13": "9787508633749",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7ade\u4e89\u6218\u7565\uff0cISBN-13 9787508633749"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u597d\u6218\u7565\uff0c\u574f\u6218\u7565",
      "isbn13": "9787508643427",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u597d\u6218\u7565\uff0c\u574f\u6218\u7565\uff0cISBN-13 9787508643427"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u8fd9\u5c31\u662fOKR",
      "isbn13": "9787521702330",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8fd9\u5c31\u662fOKR\uff0cISBN-13 9787521702330"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u521b\u65b0\u8005\u7684\u7a98\u5883",
      "isbn13": "9787508633336",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u521b\u65b0\u8005\u7684\u7a98\u5883\uff0cISBN-13 9787508633336"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7cfb\u7edf\u4e4b\u7f8e",
      "isbn13": "9787508640114",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7cfb\u7edf\u4e4b\u7f8e\uff0cISBN-13 9787508640114"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7b2c\u4e94\u9879\u4fee\u70bc",
      "isbn13": "9787508631332",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7b2c\u4e94\u9879\u4fee\u70bc\uff0cISBN-13 9787508631332"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u8d85\u9884\u6d4b",
      "isbn13": "9787508663098",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8d85\u9884\u6d4b\uff0cISBN-13 9787508663098"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u91d1\u5b57\u5854\u539f\u7406",
      "isbn13": "9787508633732",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u91d1\u5b57\u5854\u539f\u7406\uff0cISBN-13 9787508633732"
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
      "title": "\u9879\u76ee\u7ba1\u7406\u77e5\u8bc6\u4f53\u7cfb\u6307\u5357",
      "author": "\u7b2c7\u7248",
      "isbn13": "9787111558477",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u9879\u76ee\u7ba1\u7406\u77e5\u8bc6\u4f53\u7cfb\u6307\u5357\uff08\u7b2c7\u7248\uff09\uff0cISBN-13 9787111558477"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u4eba\u6708\u795e\u8bdd",
      "isbn13": "9787302154419",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4eba\u6708\u795e\u8bdd\uff0cISBN-13 9787302154419"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u76ee\u6807",
      "isbn13": "9787508637020",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u76ee\u6807\uff0cISBN-13 9787508637020"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u9ad8\u6548\u80fd\u4eba\u58eb\u7684\u4e03\u4e2a\u4e60\u60ef",
      "isbn13": "9787508092232",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u9ad8\u6548\u80fd\u4eba\u58eb\u7684\u4e03\u4e2a\u4e60\u60ef\uff0cISBN-13 9787508092232"
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
      "title": "\u601d\u8003\uff0c\u5feb\u4e0e\u6162",
      "isbn13": "9787508633565",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u601d\u8003\uff0c\u5feb\u4e0e\u6162\uff0cISBN-13 9787508633565"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5f71\u54cd\u529b",
      "isbn13": "9787508622163",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5f71\u54cd\u529b\uff0cISBN-13 9787508622163"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u602a\u8bde\u884c\u4e3a\u5b66",
      "isbn13": "9787508615824",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u602a\u8bde\u884c\u4e3a\u5b66\uff0cISBN-13 9787508615824"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u52a9\u63a8",
      "isbn13": "9787508641238",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u52a9\u63a8\uff0cISBN-13 9787508641238"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5fc3\u6d41",
      "isbn13": "9787508660721",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5fc3\u6d41\uff0cISBN-13 9787508660721"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u9a71\u52a8\u529b",
      "isbn13": "9787508621753",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u9a71\u52a8\u529b\uff0cISBN-13 9787508621753"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u793e\u4f1a\u5fc3\u7406\u5b66",
      "author": "\u8fc8\u5c14\u65af",
      "isbn13": "9787115412393",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u793e\u4f1a\u5fc3\u7406\u5b66\uff08\u8fc8\u5c14\u65af\uff09\uff0cISBN-13 9787115412393"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "TRIZ\u8fdb\u9636\u53ca\u5b9e\u6218",
      "author": "\u8d75\u654f \u5f20\u6b66\u57ce \u738b\u51a0\u6b8a",
      "isbn13": "9787111518488",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: TRIZ\u8fdb\u9636\u53ca\u5b9e\u6218\uff08\u8d75\u654f \u5f20\u6b66\u57ce \u738b\u51a0\u6b8a\uff09\uff0cISBN-13 9787111518488"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u521b\u65b0\u601d\u7ef4\u4e0eTRIZ\u521b\u65b0\u65b9\u6cd5",
      "isbn13": "9787302500117",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u521b\u65b0\u601d\u7ef4\u4e0eTRIZ\u521b\u65b0\u65b9\u6cd5\uff0cISBN-13 9787302500117"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u56e0\u679c\u63a8\u7406\uff1a\u57fa\u7840\u4e0e\u5b66\u4e60\u7b97\u6cd5",
      "author": "Jonas Peters, Dominik Janzing etc.",
      "isbn13": "9787111640301",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u56e0\u679c\u63a8\u7406\uff1a\u57fa\u7840\u4e0e\u5b66\u4e60\u7b97\u6cd5\uff08Jonas Peters, Dominik Janzing etc.\uff09\uff0cISBN-13 9787111640301"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5982\u4f55\u7cfb\u7edf\u601d\u8003",
      "author": "\u90b1\u662d\u826f",
      "isbn13": "9787111585893",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5982\u4f55\u7cfb\u7edf\u601d\u8003\uff08\u90b1\u662d\u826f\uff09\uff0cISBN-13 9787111585893"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u601d\u7ef4\u6a21\u578b",
      "author": "\u5f7c\u5f97\u00b7\u970d\u6797\u65af (Peter Hollins)",
      "isbn13": "9787515360744",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u601d\u7ef4\u6a21\u578b (\u5f7c\u5f97\u00b7\u970d\u6797\u65af (Peter Hollins))\uff0cISBN-13 9787515360744"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u628a\u554f\u984c\u5316\u7e41\u70ba\u7c21\u7684\u601d\u8003\u67b6\u69cb\u5716\u9451",
      "isbn13": "9789865070885",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u628a\u554f\u984c\u5316\u7e41\u70ba\u7c21\u7684\u601d\u8003\u67b6\u69cb\u5716\u9451\uff0cISBN-13 9789865070885"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6848\u4f8b\u89e3\u6790\uff01\u8d85\u9ad8\u6548\u5fc3\u667a\u5716\u6cd5\u5165\u9580",
      "author": "\u5b6b\u6613\u65b0",
      "isbn13": "9789862729496",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6848\u4f8b\u89e3\u6790\uff01\u8d85\u9ad8\u6548\u5fc3\u667a\u5716\u6cd5\u5165\u9580\uff08\u5b6b\u6613\u65b0\uff09\uff0cISBN-13 9789862729496"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6a21\u578b\u601d\u7ef4 The Model Thinker",
      "author": "\u65af\u79d1\u7279\u00b7\u4f69\u5947 Scott E. Page",
      "isbn13": "9787213095436",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6a21\u578b\u601d\u7ef4 The Model Thinker\uff08\u65af\u79d1\u7279\u00b7\u4f69\u5947 Scott E. Page\uff09\uff0cISBN-13 9787213095436"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7070\u5ea6\u51b3\u7b56\uff1a\u5982\u4f55\u5904\u7406\u590d\u6742\u3001\u68d8\u624b\u3001\u9ad8\u98ce\u9669\u7684\u96be\u9898",
      "author": "\u5c0f\u7ea6\u745f\u592b\u00b7\u5df4\u8fbe\u62c9\u514b",
      "isbn13": "9787111584643",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7070\u5ea6\u51b3\u7b56\uff1a\u5982\u4f55\u5904\u7406\u590d\u6742\u3001\u68d8\u624b\u3001\u9ad8\u98ce\u9669\u7684\u96be\u9898\uff08\u5c0f\u7ea6\u745f\u592b\u00b7\u5df4\u8fbe\u62c9\u514b\uff09\uff0cISBN-13 9787111584643"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u79d1\u5b66\u5206\u6790--\u903b\u8f91\u4e0e\u79d1\u5b66\u6f14\u7ece\u65b9\u6cd5",
      "author": "\u5468\u5efa\u6b66",
      "isbn13": "9787122371232",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u79d1\u5b66\u5206\u6790--\u903b\u8f91\u4e0e\u79d1\u5b66\u6f14\u7ece\u65b9\u6cd5\uff08\u5468\u5efa\u6b66\uff09\uff0cISBN-13 9787122371232"
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
      "title": "\u4e25\u5bc6\u7cfb\u7edf\u8bbe\u8ba1-\u65b9\u6cd5\u3001\u8d8b\u52bf\u4e0e\u6311\u6218",
      "author": "\u3010\u6cd5\u3011\u3010\u5e0c\u814a\u3011\u7ea6\u745f\u592b\u00b7\u5e0c\u53d1\u57fa\u601d",
      "isbn13": "9787121467653",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4e25\u5bc6\u7cfb\u7edf\u8bbe\u8ba1-\u65b9\u6cd5\u3001\u8d8b\u52bf\u4e0e\u6311\u6218\uff08\u3010\u6cd5\u3011\u3010\u5e0c\u814a\u3011\u7ea6\u745f\u592b\u00b7\u5e0c\u53d1\u57fa\u601d\uff09\uff0cISBN-13 9787121467653"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "TRIZ\uff1a\u4ea7\u54c1\u521b\u65b0\u8bbe\u8ba1",
      "author": "\u9ad8\u5e38\u9752",
      "isbn13": "9787111610298",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: TRIZ\uff1a\u4ea7\u54c1\u521b\u65b0\u8bbe\u8ba1\uff08\u9ad8\u5e38\u9752\uff09\uff0cISBN-13 9787111610298"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u67b6\u6784\u5e08\u542f\u793a\u5f55-\u77e5\u8bc6\u6a21\u578b\u3001\u843d\u5730\u65b9\u6cd5\u4e0e\u601d\u7ef4\u6a21\u5f0f",
      "author": "\u7075\u7280",
      "isbn13": "9787111749080",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u67b6\u6784\u5e08\u542f\u793a\u5f55-\u77e5\u8bc6\u6a21\u578b\u3001\u843d\u5730\u65b9\u6cd5\u4e0e\u601d\u7ef4\u6a21\u5f0f\uff08\u7075\u7280\uff09\uff0cISBN-13 9787111749080"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6a21\u578b\u601d\u7ef4\u7b80\u5316\u4e16\u754c\u7684\u4eba\u5de5\u667a\u80fd\u6a21\u578b",
      "author": "\u9f9a\u624d\u6625",
      "isbn13": "9787121408984",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6a21\u578b\u601d\u7ef4\u7b80\u5316\u4e16\u754c\u7684\u4eba\u5de5\u667a\u80fd\u6a21\u578b\uff08\u9f9a\u624d\u6625\uff09\uff0cISBN-13 9787121408984"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5206\u6790\u601d\u7ef4\u7684\u51c6\u5219",
      "isbn13": "9787573917065",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5206\u6790\u601d\u7ef4\u7684\u51c6\u5219\uff0cISBN-13 9787573917065"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6218\u7565\u601d\u7ef4\u7684\u516d\u9879\u4fee\u70bc",
      "isbn13": "9787521773033",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6218\u7565\u601d\u7ef4\u7684\u516d\u9879\u4fee\u70bc\uff0cISBN-13 9787521773033"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7b2c\u4e00\u6027\u539f\u7406\uff1a21\u5802\u79d1\u5b66\u901a\u8bc6\u8bfe",
      "isbn13": "9787523605103",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7b2c\u4e00\u6027\u539f\u7406\uff1a21\u5802\u79d1\u5b66\u901a\u8bc6\u8bfe\uff0cISBN-13 9787523605103"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u767e\u77e5\u601d\u7ef4\u6a21\u578b\u4ece\u6a21\u578b\u5e94\u7528\u5230\u601d\u7ef4\u63a2\u6e90",
      "author": "\u5706\u4e2d",
      "isbn13": "9787572295386",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u767e\u77e5\u601d\u7ef4\u6a21\u578b\u4ece\u6a21\u578b\u5e94\u7528\u5230\u601d\u7ef4\u63a2\u6e90\uff08\u5706\u4e2d\uff09\uff0cISBN-13 9787572295386"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "100+\u601d\u7ef4\u6a21\u578b\u5408\u96c6",
      "author": "\u6a21\u578b\u601d\u7ef4",
      "isbn13": "9787115652201",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 100+\u601d\u7ef4\u6a21\u578b\u5408\u96c6\uff08\u6a21\u578b\u601d\u7ef4\uff09\uff0cISBN-13 9787115652201"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7a77\u67e5\u7406\u5b9d\u5178\uff1a\u67e5\u7406\u00b7\u8292\u683c\u667a\u6167\u7bb4\u8a00\u5f55\uff08\u5168\u65b0\u589e\u8ba2\u672c\uff09\uff08\u4ef7\u503c\u6295\u8d44\u5723\u7ecf\uff0c\u4eba\u751f\u667a\u6167\u5b9d\u5178\u3002\u5168\u65b0\u5347\u7ea7\u7248\u53d1\u5e03\uff0197\u5c81\u7684\u67e5\u7406\u2022\u8292\u683c\u8fd8\u5728\u4e0d\u65ad\u5b66\u4e60\u7cbe\u8fdb \u6211\u4eec\u600e\u4e48...",
      "isbn13": "9787521730401",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7a77\u67e5\u7406\u5b9d\u5178\uff1a\u67e5\u7406\u00b7\u8292\u683c\u667a\u6167\u7bb4\u8a00\u5f55\uff08\u5168\u65b0\u589e\u8ba2\u672c\uff09\uff08\u4ef7\u503c\u6295\u8d44\u5723\u7ecf\uff0c\u4eba\u751f\u667a\u6167\u5b9d\u5178\u3002\u5168\u65b0\u5347\u7ea7\u7248\u53d1\u5e03\uff0197\u5c81\u7684\u67e5\u7406\u2022\u8292\u683c\u8fd8\u5728\u4e0d\u65ad\u5b66\u4e60\u7cbe\u8fdb \u6211\u4eec\u600e\u4e48...\uff0cISBN-13 9787521730401"
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
  "imported_from": "vendor/common-agent-swarm-ops/business/specials/agents/specials.strategic-goal-achievement-agent",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```
