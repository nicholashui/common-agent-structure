# specials.techology-advisor-agent — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/specials.techology-advisor-agent/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "specials.techology-advisor-agent",
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
      "spagent.techology-advisor-agent-input"
    ],
    "outputs": [
      "spagent.techology-advisor-agent-output"
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

# Techology Advisor Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.techology-advisor-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain techology advisor agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

--- At regular intervals — or when triggered by a user reporting a bad outcome — review your previous recommendations:

### Domain distillation (embedded, untrusted design provenance)

--- At regular intervals — or when triggered by a user reporting a bad outcome — review your previous recommendations:

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
- Local rubric reference: `spagent.techology-advisor-agent-rubric` (inert identifier).
- Prompt reference: `spagent.techology-advisor-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.techology-advisor-agent-input"],"outputs":["spagent.techology-advisor-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.techology-advisor-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.techology-advisor-agent-prompt","rubric_reference":"spagent.techology-advisor-agent-rubric","critique_edges":{"inputs":["spagent.techology-advisor-agent-input"],"outputs":["spagent.techology-advisor-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.techology-advisor-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/techology_advisor_agent.md`
- Design source SHA-256 (at generation): `d0d2715c19ac8677d9cec17ba16179f024396e2798e5367698bcce669c762d79`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.

## Prompts

### `prompts/primary.md`

You are a baseline-safe specials pack agent. No network. No production activation.

# Techology Advisor Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.techology-advisor-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain techology advisor agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

--- At regular intervals — or when triggered by a user reporting a bad outcome — review your previous recommendations:

### Domain distillation (embedded, untrusted design provenance)

--- At regular intervals — or when triggered by a user reporting a bad outcome — review your previous recommendations:

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
- Local rubric reference: `spagent.techology-advisor-agent-rubric` (inert identifier).
- Prompt reference: `spagent.techology-advisor-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.techology-advisor-agent-input"],"outputs":["spagent.techology-advisor-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.techology-advisor-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.techology-advisor-agent-prompt","rubric_reference":"spagent.techology-advisor-agent-rubric","critique_edges":{"inputs":["spagent.techology-advisor-agent-input"],"outputs":["spagent.techology-advisor-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.techology-advisor-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required histor

## Rubrics

### `rubrics/primary.md`

Success: stay inside pack responsibility; no network; no production activation.

## Sources

### `sources/MAPPING.md`

# Source mapping note — `specials.techology-advisor-agent`

- Mapping status: `related` (specials redesign doc → pack agent)
- Design source (historical): `docs/special_agents_redesign/agents/techology_advisor_agent.md`
- Source SHA-256: `d0d2715c19ac8677d9cec17ba16179f024396e2798e5367698bcce669c762d79`
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
      "title": "Introduction to Information Retrieval",
      "author": "Manning, Raghavan, Sch\u00fctze",
      "isbn13": "9780521865715",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Introduction to Information Retrieval (Manning, Raghavan, Sch\u00fctze), ISBN-13 9780521865715"
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
      "title": "\u4fe1\u606f\u68c0\u7d22\u5bfc\u8bba",
      "isbn13": "9787115221704",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4fe1\u606f\u68c0\u7d22\u5bfc\u8bba\uff0cISBN-13 9787115221704"
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
      "title": "agentic-design-patterns-chinese",
      "isbn13": "9783032014016",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: agentic-design-patterns-chinese, ISBN-13 9783032014016"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u667a\u80fd\u4f53\u8bbe\u8ba1\u6307\u5357",
      "author": "\u4e91\u4e2d\u6c5f\u6811",
      "isbn13": "9787111775843",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u667a\u80fd\u4f53\u8bbe\u8ba1\u6307\u5357\uff08\u4e91\u4e2d\u6c5f\u6811\uff09\uff0cISBN-13 9787111775843"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5927\u6a21\u578b\u5e94\u7528\u5f00\u53d1\uff1a\u52a8\u624b\u505aAI Agent",
      "author": "\u9ec4\u4f73",
      "isbn13": "9787115642172",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5927\u6a21\u578b\u5e94\u7528\u5f00\u53d1\uff1a\u52a8\u624b\u505aAI Agent\uff08\u9ec4\u4f73\uff09\uff0cISBN-13 9787115642172"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6784\u5efaAgentic AI\u7cfb\u7edf",
      "author": "Anjanava Biswas, Wrick Talukdar",
      "isbn13": "9787302703983",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6784\u5efaAgentic AI\u7cfb\u7edf\uff08Anjanava Biswas, Wrick Talukdar\uff09\uff0cISBN-13 9787302703983"
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
      "title": "AI Agent\u5f00\u53d1\u4e0e\u5e94\u7528\uff1a\u57fa\u4e8e\u5927\u6a21\u578b\u7684\u667a\u80fd\u4f53\u6784\u5efa",
      "author": "\u51cc\u5cf0",
      "isbn13": "9787302685975",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: AI Agent\u5f00\u53d1\u4e0e\u5e94\u7528\uff1a\u57fa\u4e8e\u5927\u6a21\u578b\u7684\u667a\u80fd\u4f53\u6784\u5efa\uff08\u51cc\u5cf0\uff09\uff0cISBN-13 9787302685975"
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
      "title": "\u4ece\u96f6\u5f00\u59cb\u6784\u5efa\u5927\u578b\u8bed\u8a00\u6a21\u578bBuild a Large Language Model (From Scratch)",
      "author": "SEBASTIAN RASCHKA",
      "isbn13": "9781633437166",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4ece\u96f6\u5f00\u59cb\u6784\u5efa\u5927\u578b\u8bed\u8a00\u6a21\u578bBuild a Large Language Model (From Scratch)\uff08SEBASTIAN RASCHKA\uff09\uff0cISBN-13 9781633437166"
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
      "title": "\u5927\u6a21\u578b\u9879\u76ee\u5b9e\u6218 \u591a\u9886\u57df\u667a\u80fd\u5e94\u7528\u5f00\u53d1",
      "author": "\u9ad8\u5f3a\u6587",
      "isbn13": "9787111762348",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5927\u6a21\u578b\u9879\u76ee\u5b9e\u6218 \u591a\u9886\u57df\u667a\u80fd\u5e94\u7528\u5f00\u53d1\uff08\u9ad8\u5f3a\u6587\uff09\uff0cISBN-13 9787111762348"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "LLM Engineer\u2019s Handbook",
      "author": "Paul Iusztin ,Maxime Labonne",
      "isbn13": "9781836200079",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: LLM Engineer\u2019s Handbook (Paul Iusztin ,Maxime Labonne), ISBN-13 9781836200079"
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
      "title": "\u4ece\u96f6\u6784\u5efa\u5927\u6a21\u578b\u7b97\u6cd5\u3001\u8bad\u7ec3\u4e0e\u5fae\u8c03",
      "isbn13": "9787302685616",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4ece\u96f6\u6784\u5efa\u5927\u6a21\u578b\u7b97\u6cd5\u3001\u8bad\u7ec3\u4e0e\u5fae\u8c03\uff0cISBN-13 9787302685616"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u591a\u6a21\u6001\u5927\u6a21\u578b \u4ece\u7406\u8bba\u5230\u5b9e\u8df5",
      "isbn13": "9787302686927",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u591a\u6a21\u6001\u5927\u6a21\u578b \u4ece\u7406\u8bba\u5230\u5b9e\u8df5\uff0cISBN-13 9787302686927"
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
      "title": "\u8fd9\u5c31\u662fMCP",
      "author": "\u827e\u9017\u7b14",
      "isbn13": "9787115677471",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8fd9\u5c31\u662fMCP\uff08\u827e\u9017\u7b14\uff09\uff0cISBN-13 9787115677471"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building Multimodal Generative AI and Agentic Applications Shaping concept to code for\u2026",
      "isbn13": "9789365898385",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building Multimodal Generative AI and Agentic Applications Shaping concept to code for\u2026, ISBN-13 9789365898385"
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
      "title": "MCP\u534f\u8bae\u4e0eAI Agent\u5f00\u53d1\uff1a\u6807\u51c6\u3001\u5e94\u7528\u4e0e\u5b9e\u73b0",
      "isbn13": "9787302695349",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: MCP\u534f\u8bae\u4e0eAI Agent\u5f00\u53d1\uff1a\u6807\u51c6\u3001\u5e94\u7528\u4e0e\u5b9e\u73b0\uff0cISBN-13 9787302695349"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "MCP\u534f\u8bae\u4e0e\u5927\u6a21\u578b\u96c6\u6210\u5b9e\u6218",
      "isbn13": "9787121503863",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: MCP\u534f\u8bae\u4e0e\u5927\u6a21\u578b\u96c6\u6210\u5b9e\u6218\uff0cISBN-13 9787121503863"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangChain\u6838\u5fc3\u6280\u672f\u4e0eLLM\u9879\u76ee\u5b9e\u8df5",
      "author": "\u51cc\u5cf0",
      "isbn13": "9787302685630",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangChain\u6838\u5fc3\u6280\u672f\u4e0eLLM\u9879\u76ee\u5b9e\u8df5\uff08\u51cc\u5cf0\uff09\uff0cISBN-13 9787302685630"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangChain \u5165\u95e8\u6307\u5357\u6784\u5efa\u9ad8\u53ef\u590d\u7528\u3001\u53ef\u6269\u5c55\u7684 LLM \u5e94\u7528\u7a0b\u5e8f",
      "author": "\u674e\u7279\u4e3d",
      "isbn13": "9787121467271",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangChain \u5165\u95e8\u6307\u5357\u6784\u5efa\u9ad8\u53ef\u590d\u7528\u3001\u53ef\u6269\u5c55\u7684 LLM \u5e94\u7528\u7a0b\u5e8f\uff08\u674e\u7279\u4e3d\uff09\uff0cISBN-13 9787121467271"
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
      "title": "\u5927\u6a21\u578bRAG\u5b9e\u6218\uff1aRAG\u539f\u7406\u3001\u5e94\u7528\u4e0e\u7cfb\u7edf\u6784\u5efa",
      "author": "\u6c6a\u9e4f, \u8c37\u6e05\u6c34, \u535e\u9f99\u9e4f",
      "isbn13": "9787111761990",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5927\u6a21\u578bRAG\u5b9e\u6218\uff1aRAG\u539f\u7406\u3001\u5e94\u7528\u4e0e\u7cfb\u7edf\u6784\u5efa\uff08\u6c6a\u9e4f, \u8c37\u6e05\u6c34, \u535e\u9f99\u9e4f\uff09\uff0cISBN-13 9787111761990"
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
      "language": "ZH",
      "title": "\u591a\u6a21\u6001\u5927\u6a21\u578b \u7b97\u6cd5\u3001\u5e94\u7528\u4e0e\u5fae\u8c03",
      "author": "\u5218\u5146\u5cf0",
      "isbn13": "9787111754886",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u591a\u6a21\u6001\u5927\u6a21\u578b \u7b97\u6cd5\u3001\u5e94\u7528\u4e0e\u5fae\u8c03\uff08\u5218\u5146\u5cf0\uff09\uff0cISBN-13 9787111754886"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "AI Agent AI\u7684\u4e0b\u4e00\u4e2a\u98ce\u53e3 \u667a\u80fd\u4f53\u7684\u6838\u5fc3\u6280\u672f\u8bb2\u89e3\u4e66\u7c4d \u5927\u6a21\u578b\u65f6\u4ee3\u7684AI\u4ecb\u7ecd\u4e66",
      "isbn13": "9787121474606",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: AI Agent AI\u7684\u4e0b\u4e00\u4e2a\u98ce\u53e3 \u667a\u80fd\u4f53\u7684\u6838\u5fc3\u6280\u672f\u8bb2\u89e3\u4e66\u7c4d \u5927\u6a21\u578b\u65f6\u4ee3\u7684AI\u4ecb\u7ecd\u4e66\uff0cISBN-13 9787121474606"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5b98\u65b9\u6b63\u7248 LangChain\u5b9e\u6218 \u4ece\u539f\u578b\u5230\u751f\u4ea7 \u52a8\u624b\u6253\u9020 LLM \u5e94\u7528",
      "isbn13": "9787121475450",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5b98\u65b9\u6b63\u7248 LangChain\u5b9e\u6218 \u4ece\u539f\u578b\u5230\u751f\u4ea7 \u52a8\u624b\u6253\u9020 LLM \u5e94\u7528\uff0cISBN-13 9787121475450"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6b63\u7248\u5305\u90ae LangChain\u7f16\u7a0b \u4ece\u5165\u95e8\u5230\u5b9e\u8df5",
      "isbn13": "9787115639424",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6b63\u7248\u5305\u90ae LangChain\u7f16\u7a0b \u4ece\u5165\u95e8\u5230\u5b9e\u8df5\uff0cISBN-13 9787115639424"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LLM\u4e32\u63a5\u6240\u6709\u670d\u52d9\uff1aLangChain\u539f\u578b\u5230\u7522\u54c1\u5168\u9762\u958b\u767c",
      "isbn13": "9786267383919",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LLM\u4e32\u63a5\u6240\u6709\u670d\u52d9\uff1aLangChain\u539f\u578b\u5230\u7522\u54c1\u5168\u9762\u958b\u767c\uff0cISBN-13 9786267383919"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6975\u901fChatGPT\u958b\u767c\u8005\u5175\u5668\u6307\u5357\uff1a\u8de8\u754c\u6574\u5408Prompt Flow\u3001LangChain\u8207Semantic Kernel\u6846\u67b6",
      "isbn13": "9786263338203",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6975\u901fChatGPT\u958b\u767c\u8005\u5175\u5668\u6307\u5357\uff1a\u8de8\u754c\u6574\u5408Prompt Flow\u3001LangChain\u8207Semantic Kernel\u6846\u67b6\uff0cISBN-13 9786263338203"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u751f\u6210\u5f0fAI\u5b9e\u6218\u57fa\u4e8eTransformer\u3001Stable Diffusion\u3001LangChain\u548cAI Agent",
      "isbn13": "9787115650443",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u751f\u6210\u5f0fAI\u5b9e\u6218\u57fa\u4e8eTransformer\u3001Stable Diffusion\u3001LangChain\u548cAI Agent\uff0cISBN-13 9787115650443"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangChain\u6280\u672f\u89e3\u5bc6 \u6784\u5efa\u5927\u6a21\u578b\u5e94\u7528\u7684\u5168\u666f\u6307\u5357 \u738b\u6d69\u5e06",
      "isbn13": "9787121477379",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangChain\u6280\u672f\u89e3\u5bc6 \u6784\u5efa\u5927\u6a21\u578b\u5e94\u7528\u7684\u5168\u666f\u6307\u5357 \u738b\u6d69\u5e06\uff0cISBN-13 9787121477379"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangChain\u5927\u6a21\u578bAI\u5e94\u7528\u5f00\u53d1\u5b9e\u8df5",
      "isbn13": "9787302672524",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangChain\u5927\u6a21\u578bAI\u5e94\u7528\u5f00\u53d1\u5b9e\u8df5\uff0cISBN-13 9787302672524"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "AI Agent\u5e94\u7528\u4e0e\u9879\u76ee\u5b9e\u6218",
      "isbn13": "9787121491818",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: AI Agent\u5e94\u7528\u4e0e\u9879\u76ee\u5b9e\u6218\uff0cISBN-13 9787121491818"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u4e00\u672c\u4e66\u8bfb\u61c2AI Agent\uff1a\u6280\u672f\u3001\u5e94\u7528\u4e0e\u5546\u4e1a",
      "isbn13": "9787111764168",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4e00\u672c\u4e66\u8bfb\u61c2AI Agent\uff1a\u6280\u672f\u3001\u5e94\u7528\u4e0e\u5546\u4e1a\uff0cISBN-13 9787111764168"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5927\u6a21\u578b\u9879\u76ee\u5b9e\u6218Agent\u5f00\u53d1\u4e0e\u5e94\u7528",
      "isbn13": "9787111777335",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5927\u6a21\u578b\u9879\u76ee\u5b9e\u6218Agent\u5f00\u53d1\u4e0e\u5e94\u7528\uff0cISBN-13 9787111777335"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "MCP\u5f00\u53d1\u4ece\u5165\u95e8\u5230\u5b9e\u6218\uff1a\u4eba\u5de5\u667a\u80fdAI\u667a\u80fd\u4f53Agent\u5e94\u7528\u5f00\u53d1",
      "isbn13": "9787115674142",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: MCP\u5f00\u53d1\u4ece\u5165\u95e8\u5230\u5b9e\u6218\uff1a\u4eba\u5de5\u667a\u80fdAI\u667a\u80fd\u4f53Agent\u5e94\u7528\u5f00\u53d1\uff0cISBN-13 9787115674142"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "AI Agent\u8bbe\u8ba1\u5b9e\u6218\uff1a\u667a\u80fd\u4f53\u8bbe\u8ba1\u65b9\u6cd5\u4e0e\u6280\u5de7",
      "isbn13": "9787111779247",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: AI Agent\u8bbe\u8ba1\u5b9e\u6218\uff1a\u667a\u80fd\u4f53\u8bbe\u8ba1\u65b9\u6cd5\u4e0e\u6280\u5de7\uff0cISBN-13 9787111779247"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "MCP\u6781\u7b80\u5f00\u53d1\uff1a\u8f7b\u677e\u6253\u9020\u9ad8\u6548\u667a\u80fd\u4f53 MCP\u5f00\u53d1\u6559\u7a0b Agent\u667a\u80fd\u4f53\u5927\u8bed",
      "isbn13": "9787115674883",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: MCP\u6781\u7b80\u5f00\u53d1\uff1a\u8f7b\u677e\u6253\u9020\u9ad8\u6548\u667a\u80fd\u4f53 MCP\u5f00\u53d1\u6559\u7a0b Agent\u667a\u80fd\u4f53\u5927\u8bed\uff0cISBN-13 9787115674883"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "A2A\u5354\u8b70\uff1a\u591aAgent\u7cfb\u7d71\u5168\u93c8\u8def\u958b\u767c",
      "isbn13": "9787111791980",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: A2A\u5354\u8b70\uff1a\u591aAgent\u7cfb\u7d71\u5168\u93c8\u8def\u958b\u767c\uff0cISBN-13 9787111791980"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangGraph\u5be6\u6230\u2500\u2500\u69cb\u5efa\u65b0\u4e00\u4ee3 AI \u667a\u6167\u9ad4\u7cfb\u7d71",
      "isbn13": "9787121507007",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangGraph\u5be6\u6230\u2500\u2500\u69cb\u5efa\u65b0\u4e00\u4ee3 AI \u667a\u6167\u9ad4\u7cfb\u7d71\uff0cISBN-13 9787121507007"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "MCP+A2A+LangGraph \u9a45\u52d5\u7684\u667a\u80fd\u9ad4\u5168\u6d41\u7a0b\u958b\u767c",
      "isbn13": "9787115682024",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: MCP+A2A+LangGraph \u9a45\u52d5\u7684\u667a\u80fd\u9ad4\u5168\u6d41\u7a0b\u958b\u767c\uff0cISBN-13 9787115682024"
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
  "common_agent_id": "specials.techology-advisor-agent",
  "pack_id": "specials",
  "mapping_status": "related",
  "source_documents": [
    "docs/special_agents_redesign/agents/techology_advisor_agent.md"
  ],
  "source_sha256": "d0d2715c19ac8677d9cec17ba16179f024396e2798e5367698bcce669c762d79",
  "configuration_sha256": "2ea149f003cb7b9549254e32283fb8b5b92bd321b255448a6bef478f7f9efce0",
  "destination_commit": "5460c4b4a33c15286f9fd84b1bc764d755f5bab0",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "generated_at": "2026-07-26T14:16:46.000174Z",
  "reviewed_by": "specials-self-contained-reviewer",
  "reviewed_at": "2026-07-26T18:00:00Z",
  "imported_from": "vendor/common-agent-swarm-ops/business/specials/agents/specials.techology-advisor-agent",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```
