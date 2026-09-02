# specials.controller-agent — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/specials.controller-agent/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "specials.controller-agent",
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
      "spagent.controller-agent-input"
    ],
    "outputs": [
      "spagent.controller-agent-output"
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

# Controller Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.controller-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain controller agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

Specialized agent / system prompt / playbook for generating highly controllable video content using the hybrid **Blender draft modeling + AI video diffusion** approach. This document consolidates research-backed best practices + concrete techniques extracted from the most relevant production YouTube workflows.

### Domain distillation (embedded, untrusted design provenance)

Specialized agent / system prompt / playbook for generating highly controllable video content using the hybrid **Blender draft modeling + AI video diffusion** approach. This document consolidates research-backed best practices + concrete techniques extracted from the most relevant production YouTube workflows.

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
- Local rubric reference: `spagent.controller-agent-rubric` (inert identifier).
- Prompt reference: `spagent.controller-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.controller-agent-input"],"outputs":["spagent.controller-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.controller-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.controller-agent-prompt","rubric_reference":"spagent.controller-agent-rubric","critique_edges":{"inputs":["spagent.controller-agent-input"],"outputs":["spagent.controller-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.controller-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/controller_agent.md`
- Design source SHA-256 (at generation): `ab695387fe27a4fb05d5b861d5f9daceea37a29511c49afce35751ca0b1f564a`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.

## Prompts

### `prompts/primary.md`

You are a baseline-safe specials pack agent. No network. No production activation.

# Controller Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.controller-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain controller agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

Specialized agent / system prompt / playbook for generating highly controllable video content using the hybrid **Blender draft modeling + AI video diffusion** approach. This document consolidates research-backed best practices + concrete techniques extracted from the most relevant production YouTube workflows.

### Domain distillation (embedded, untrusted design provenance)

Specialized agent / system prompt / playbook for generating highly controllable video content using the hybrid **Blender draft modeling + AI video diffusion** approach. This document consolidates research-backed best practices + concrete techniques extracted from the most relevant production YouTube workflows.

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
- Local rubric reference: `spagent.controller-agent-rubric` (inert identifier).
- Prompt reference: `spagent.controller-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.controller-agent-input"],"outputs":["spagent.controller-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.controller-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.controller-agent-prompt","rubric_reference":"spagent.controller-agent-rubric","critique_edges":{"inputs":["spagent.controller-agent-input"],"outputs":["spagent.controller-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../

## Rubrics

### `rubrics/primary.md`

Success: stay inside pack responsibility; no network; no production activation.

## Sources

### `sources/MAPPING.md`

# Source mapping note — `specials.controller-agent`

- Mapping status: `related` (specials redesign doc → pack agent)
- Design source (historical): `docs/special_agents_redesign/agents/controller_agent.md`
- Source SHA-256: `ab695387fe27a4fb05d5b861d5f9daceea37a29511c49afce35751ca0b1f564a`
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
      "title": "Computer Graphics: Principles and Practice, 3rd ed.",
      "author": "Hughes et al.",
      "isbn13": "9780321399526",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Computer Graphics: Principles and Practice, 3rd ed. (Hughes et al.), ISBN-13 9780321399526"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Real-Time Rendering, 4th ed.",
      "author": "Akenine-Möller et al.",
      "isbn13": "9781138627000",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Real-Time Rendering, 4th ed. (Akenine-Möller et al.), ISBN-13 9781138627000"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "计算机图形学",
      "isbn13": "9787121197543",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 计算机图形学，ISBN-13 9787121197543"
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
      "title": "The VES Handbook of Visual Effects, 2nd ed.",
      "isbn13": "9780240824383",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The VES Handbook of Visual Effects, 2nd ed., ISBN-13 9780240824383"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Digital Compositing for Film and Video, 4th ed.",
      "author": "Steve Wright",
      "isbn13": "9781138940321",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Digital Compositing for Film and Video, 4th ed. (Steve Wright), ISBN-13 9781138940321"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Art and Science of Digital Compositing, 2nd ed.",
      "author": "Ron Brinkmann",
      "isbn13": "9780123706386",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Art and Science of Digital Compositing, 2nd ed. (Ron Brinkmann), ISBN-13 9780123706386"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Special Makeup Effects for Stage and Screen",
      "author": "Todd Debreceni",
      "isbn13": "9781138047587",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Special Makeup Effects for Stage and Screen (Todd Debreceni), ISBN-13 9781138047587"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "数字合成的科学与艺术",
      "isbn13": "9787115215208",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 数字合成的科学与艺术，ISBN-13 9787115215208"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Cinematography: Theory and Practice, 3rd ed.",
      "author": "Blain Brown",
      "isbn13": "9781138212589",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Cinematography: Theory and Practice, 3rd ed. (Blain Brown), ISBN-13 9781138212589"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Visual Story, 2nd ed.",
      "author": "Bruce Block",
      "isbn13": "9780240807799",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Visual Story, 2nd ed. (Bruce Block), ISBN-13 9780240807799"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Filmmaker's Eye",
      "author": "Gustavo Mercado",
      "isbn13": "9780240812175",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Filmmaker's Eye (Gustavo Mercado), ISBN-13 9780240812175"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Grammar of the Shot, 4th ed.",
      "author": "Bowen",
      "isbn13": "9781138632219",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Grammar of the Shot, 4th ed. (Bowen), ISBN-13 9781138632219"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Painting With Light",
      "author": "John Alton",
      "isbn13": "9780520089495",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Painting With Light (John Alton), ISBN-13 9780520089495"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Set Lighting Technician's Handbook, 4th ed.",
      "author": "Harry Box",
      "isbn13": "9780240810751",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Set Lighting Technician's Handbook, 4th ed. (Harry Box), ISBN-13 9780240810751"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Reflections: On Cinematography",
      "author": "Roger Deakins",
      "isbn13": "9781910593998",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Reflections: On Cinematography (Roger Deakins) — check latest ed. ISBN-13 9781910593998"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Light Science & Magic, 5th ed.",
      "author": "Hunter, Biver, Fuqua",
      "isbn13": "9780415719407",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Light Science & Magic, 5th ed. (Hunter, Biver, Fuqua), ISBN-13 9780415719407"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "电影摄影：理论与实践",
      "isbn13": "9787515331867",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影摄影：理论与实践，ISBN-13 9787515331867"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "视觉故事",
      "isbn13": "9787515302867",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 视觉故事，ISBN-13 9787515302867"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "电影语言的语法",
      "isbn13": "9787532299990",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影语言的语法，ISBN-13 9787532299990"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "美国纽约摄影学院摄影教材",
      "isbn13": "9787800078491",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 美国纽约摄影学院摄影教材，ISBN-13 9787800078491"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "论摄影",
      "author": "桑塔格",
      "isbn13": "9787544722599",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 论摄影（桑塔格），ISBN-13 9787544722599"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "摄影师的视界",
      "isbn13": "9787512201880",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 摄影师的视界，ISBN-13 9787512201880"
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
  "common_agent_id": "specials.controller-agent",
  "pack_id": "specials",
  "mapping_status": "related",
  "source_documents": [
    "docs/special_agents_redesign/agents/controller_agent.md"
  ],
  "source_sha256": "ab695387fe27a4fb05d5b861d5f9daceea37a29511c49afce35751ca0b1f564a",
  "configuration_sha256": "b4a488e7b4ff9749af0645bcc3b7ea7e4dc2f6cd160ccb2709bf3e5cb075dbdf",
  "destination_commit": "5460c4b4a33c15286f9fd84b1bc764d755f5bab0",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "generated_at": "2026-07-26T14:16:45.930785Z",
  "reviewed_by": "specials-self-contained-reviewer",
  "reviewed_at": "2026-07-26T18:00:00Z",
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\specials\\agents\\specials.controller-agent",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```
