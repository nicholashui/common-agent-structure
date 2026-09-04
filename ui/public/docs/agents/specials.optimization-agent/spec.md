# specials.optimization-agent — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/specials.optimization-agent/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "specials.optimization-agent",
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
      "spagent.optimization-agent-input"
    ],
    "outputs": [
      "spagent.optimization-agent-output"
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

# Optimization Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.optimization-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain optimization agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

Deliver a production-ready, agentic evolution of the original specification, incorporating latest advances in LLM-powered multi-agent systems, autonomous optimization, process mining, digital twins, and enterprise reliability mechanisms.

### Domain distillation (embedded, untrusted design provenance)

Deliver a production-ready, agentic evolution of the original specification, incorporating latest advances in LLM-powered multi-agent systems, autonomous optimization, process mining, digital twins, and enterprise reliability mechanisms.

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
- Local rubric reference: `spagent.optimization-agent-rubric` (inert identifier).
- Prompt reference: `spagent.optimization-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.optimization-agent-input"],"outputs":["spagent.optimization-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.optimization-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.optimization-agent-prompt","rubric_reference":"spagent.optimization-agent-rubric","critique_edges":{"inputs":["spagent.optimization-agent-input"],"outputs":["spagent.optimization-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.optimization-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/optimization_agent.md`
- Design source SHA-256 (at generation): `5735afb03877a793c9b958a594778e777d15c467b62828f2cedf95c81f41efbd`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.

## Prompts

### `prompts/primary.md`

You are a baseline-safe specials pack agent. No network. No production activation.

# Optimization Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.optimization-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain optimization agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

Deliver a production-ready, agentic evolution of the original specification, incorporating latest advances in LLM-powered multi-agent systems, autonomous optimization, process mining, digital twins, and enterprise reliability mechanisms.

### Domain distillation (embedded, untrusted design provenance)

Deliver a production-ready, agentic evolution of the original specification, incorporating latest advances in LLM-powered multi-agent systems, autonomous optimization, process mining, digital twins, and enterprise reliability mechanisms.

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
- Local rubric reference: `spagent.optimization-agent-rubric` (inert identifier).
- Prompt reference: `spagent.optimization-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.optimization-agent-input"],"outputs":["spagent.optimization-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.optimization-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.optimization-agent-prompt","rubric_reference":"spagent.optimization-agent-rubric","critique_edges":{"inputs":["spagent.optimization-agent-input"],"outputs":["spagent.optimization-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.optimization-

## Rubrics

### `rubrics/primary.md`

Success: stay inside pack responsibility; no network; no production activation.

## Sources

### `sources/MAPPING.md`

# Source mapping note — `specials.optimization-agent`

- Mapping status: `related` (specials redesign doc → pack agent)
- Design source (historical): `docs/special_agents_redesign/agents/optimization_agent.md`
- Source SHA-256: `5735afb03877a793c9b958a594778e777d15c467b62828f2cedf95c81f41efbd`
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
      "title": "Convex Optimization",
      "author": "Boyd & Vandenberghe",
      "isbn13": "9780521833783",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Convex Optimization (Boyd & Vandenberghe), ISBN-13 9780521833783"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Algorithms to Live By",
      "author": "Christian & Griffiths",
      "isbn13": "9781250118363",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Algorithms to Live By (Christian & Griffiths), ISBN-13 9781250118363"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u51f8\u4f18\u5316",
      "isbn13": "9787302273264",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u51f8\u4f18\u5316\uff0cISBN-13 9787302273264"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7b97\u6cd5\u4e4b\u7f8e",
      "isbn13": "9787213081477",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7b97\u6cd5\u4e4b\u7f8e\uff0cISBN-13 9787213081477"
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
      "title": "Trustworthy Online Controlled Experiments",
      "author": "Kohavi, Tang, Xu",
      "isbn13": "9781108724265",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Trustworthy Online Controlled Experiments (Kohavi, Tang, Xu), ISBN-13 9781108724265"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Storytelling with Data",
      "author": "Cole Nussbaumer Knaflic",
      "isbn13": "9781119002253",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Storytelling with Data (Cole Nussbaumer Knaflic), ISBN-13 9781119002253"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Lean Analytics",
      "author": "Croll & Yoskovitz",
      "isbn13": "9781449335670",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Lean Analytics (Croll & Yoskovitz), ISBN-13 9781449335670"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Visual Display of Quantitative Information, 2nd ed.",
      "author": "Edward Tufte",
      "isbn13": "9780961392147",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Visual Display of Quantitative Information, 2nd ed. (Edward Tufte), ISBN-13 9780961392147"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Naked Statistics",
      "author": "Charles Wheelan",
      "isbn13": "9780393347777",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Naked Statistics (Charles Wheelan), ISBN-13 9780393347777"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Signal and the Noise",
      "author": "Nate Silver",
      "isbn13": "9780143125082",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Signal and the Noise (Nate Silver), ISBN-13 9780143125082"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7cbe\u76ca\u6570\u636e\u5206\u6790",
      "isbn13": "9787115384515",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7cbe\u76ca\u6570\u636e\u5206\u6790\uff0cISBN-13 9787115384515"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7528\u6570\u636e\u8bb2\u6545\u4e8b",
      "isbn13": "9787111575558",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7528\u6570\u636e\u8bb2\u6545\u4e8b\uff0cISBN-13 9787111575558"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u8d64\u88f8\u88f8\u7684\u7edf\u8ba1\u5b66",
      "isbn13": "9787508643427",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8d64\u88f8\u88f8\u7684\u7edf\u8ba1\u5b66\uff0cISBN-13 9787508643427"
    },
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
      "title": "\u91d1\u5b57\u5854\u539f\u7406",
      "isbn13": "9787508633732",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u91d1\u5b57\u5854\u539f\u7406\uff0cISBN-13 9787508633732"
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
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building Machine Learning Powered Applications Going from Idea to Product",
      "author": "Emmanuel Ameisen",
      "isbn13": "9781492045113",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building Machine Learning Powered Applications Going from Idea to Product (Emmanuel Ameisen), ISBN-13 9781492045113"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Practical Statistics for Data Scientists (First Early Release)",
      "author": "Peter Bruce, Andrew Bruce, Peter Gedeck",
      "isbn13": "9798341666245",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Practical Statistics for Data Scientists (First Early Release) (Peter Bruce, Andrew Bruce, Peter Gedeck), ISBN-13 9798341666245"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Ensemble Methods Foundations and Algorithms, 2e",
      "author": "Zhi-Hua Zhou",
      "isbn13": "9781003587774",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Ensemble Methods Foundations and Algorithms, 2e (Zhi-Hua Zhou), ISBN-13 9781003587774"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Hands-On Ensemble Learning with R",
      "author": "Unknown",
      "isbn13": "9781788624145",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Hands-On Ensemble Learning with R (Unknown), ISBN-13 9781788624145"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "High Performance Python - Practical Performant Programming for Humans (3rd Edition)",
      "author": "Micha Gorelick, Ian Ozsvald",
      "isbn13": "9781098165963",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: High Performance Python - Practical Performant Programming for Humans (3rd Edition) (Micha Gorelick, Ian Ozsvald), ISBN-13 9781098165963"
    }
  ],
  "common_agent_id": "specials.optimization-agent",
  "pack_id": "specials",
  "mapping_status": "related",
  "source_documents": [
    "docs/special_agents_redesign/agents/optimization_agent.md"
  ],
  "source_sha256": "5735afb03877a793c9b958a594778e777d15c467b62828f2cedf95c81f41efbd",
  "configuration_sha256": "7f76553094b246e52b8a9ab101deb80d46bf68d479d4b53dca00042735569a53",
  "destination_commit": "5460c4b4a33c15286f9fd84b1bc764d755f5bab0",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "generated_at": "2026-07-26T14:16:45.956677Z",
  "reviewed_by": "specials-self-contained-reviewer",
  "reviewed_at": "2026-07-26T18:00:00Z",
  "imported_from": "vendor/common-agent-swarm-ops/business/specials/agents/specials.optimization-agent",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```
