# specials.psychological-profile-agent — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/specials.psychological-profile-agent/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "specials.psychological-profile-agent",
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
      "spagent.psychological-profile-agent-input"
    ],
    "outputs": [
      "spagent.psychological-profile-agent-output"
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

# Psychological Profile Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.psychological-profile-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain psychological profile agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

Provide personalized parameter configurations for the framework in this chapter and Appendix A workflow **File Structure:** - Basic information (code, age, professional background) - Psychological traits (MBTI tendencies, motivation types, fear patterns) - Creation parameters (best tools, time allocation, support needs) - Framework adaptation (key focuses for each stage, predicted obstacles, success strategies)

### Domain distillation (embedded, untrusted design provenance)

Provide personalized parameter configurations for the framework in this chapter and Appendix A workflow **File Structure:** - Basic information (code, age, professional background) - Psychological traits (MBTI tendencies, motivation types, fear patterns) - Creation parameters (best tools, time allocation, support needs) - Framework adaptation (key focuses for each stage, predicted obstacles, success strategies)

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
- Local rubric reference: `spagent.psychological-profile-agent-rubric` (inert identifier).
- Prompt reference: `spagent.psychological-profile-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.psychological-profile-agent-input"],"outputs":["spagent.psychological-profile-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.psychological-profile-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.psychological-profile-agent-prompt","rubric_reference":"spagent.psychological-profile-agent-rubric","critique_edges":{"inputs":["spagent.psychological-profile-agent-input"],"outputs":["spagent.psychological-profile-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.psychological-profile-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/psychological_profile_agent.md`
- Design source SHA-256 (at generation): `f1fa518cee669e11195bf6fcc62a63d2befa84c3d8c06a08afc22fecde9c495b`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.

## Prompts

### `prompts/primary.md`

You are a baseline-safe specials pack agent. No network. No production activation.

# Psychological Profile Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.psychological-profile-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain psychological profile agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

Provide personalized parameter configurations for the framework in this chapter and Appendix A workflow **File Structure:** - Basic information (code, age, professional background) - Psychological traits (MBTI tendencies, motivation types, fear patterns) - Creation parameters (best tools, time allocation, support needs) - Framework adaptation (key focuses for each stage, predicted obstacles, success strategies)

### Domain distillation (embedded, untrusted design provenance)

Provide personalized parameter configurations for the framework in this chapter and Appendix A workflow **File Structure:** - Basic information (code, age, professional background) - Psychological traits (MBTI tendencies, motivation types, fear patterns) - Creation parameters (best tools, time allocation, support needs) - Framework adaptation (key focuses for each stage, predicted obstacles, success strategies)

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
- Local rubric reference: `spagent.psychological-profile-agent-rubric` (inert identifier).
- Prompt reference: `spagent.psychological-profile-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.psychological-profile-agent-input"],"outputs":["spagent.psychological-profile-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.psychological-profile-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.psychological-profile-agent-prompt","rubric_reference":"spagent.psychological-profile-agent-rubric","critique_edges":{"inputs":["spagent.psychological-profile-agent-input"],"outputs":["spagent.psychological-profile-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowl

## Rubrics

### `rubrics/primary.md`

Success: stay inside pack responsibility; no network; no production activation.

## Sources

### `sources/MAPPING.md`

# Source mapping note — `specials.psychological-profile-agent`

- Mapping status: `related` (specials redesign doc → pack agent)
- Design source (historical): `docs/special_agents_redesign/agents/psychological_profile_agent.md`
- Source SHA-256: `f1fa518cee669e11195bf6fcc62a63d2befa84c3d8c06a08afc22fecde9c495b`
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
      "language": "EN",
      "title": "Design for How People Learn, 2nd ed.",
      "author": "Julie Dirksen",
      "isbn13": "9780134211282",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Design for How People Learn, 2nd ed. (Julie Dirksen), ISBN-13 9780134211282"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "e-Learning and the Science of Instruction, 4th ed.",
      "author": "Clark & Mayer",
      "isbn13": "9781119158660",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: e-Learning and the Science of Instruction, 4th ed. (Clark & Mayer), ISBN-13 9781119158660"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Make It Stick",
      "author": "Brown, Roediger, McDaniel",
      "isbn13": "9780674729018",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Make It Stick (Brown, Roediger, McDaniel), ISBN-13 9780674729018"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "How People Learn",
      "author": "Bransford et al.",
      "isbn13": "9780309070362",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: How People Learn (Bransford et al.), ISBN-13 9780309070362"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Understanding by Design",
      "author": "Wiggins & McTighe",
      "isbn13": "9781416600350",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Understanding by Design (Wiggins & McTighe), ISBN-13 9781416600350"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Multimedia Learning, 3rd ed.",
      "author": "Richard E. Mayer",
      "isbn13": "9781107566187",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Multimedia Learning, 3rd ed. (Richard E. Mayer), ISBN-13 9781107566187"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "First Principles of Instruction",
      "author": "M. David Merrill",
      "isbn13": "9780470900406",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: First Principles of Instruction (M. David Merrill), ISBN-13 9780470900406"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "让学习粘住",
      "isbn13": "9787508655611",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 让学习粘住，ISBN-13 9787508655611"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "教学设计原理",
      "author": "加涅",
      "isbn13": "9787561762264",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 教学设计原理（加涅），ISBN-13 9787561762264"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "追求理解的教学设计",
      "isbn13": "9787561799994",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 追求理解的教学设计，ISBN-13 9787561799994"
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
      "title": "TRIZ：产品创新设计",
      "author": "高常青",
      "isbn13": "9787111610298",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: TRIZ：产品创新设计（高常青），ISBN-13 9787111610298"
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
      "title": "不被洗脑的100个思维习惯【作品均分7.5的学习之神斋藤孝，基于40年经验总结，100个批判型思维习惯，规避常被洗脑的人性弱点】",
      "author": "【日】斋藤孝",
      "isbn13": "9787559659514",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 不被洗脑的100个思维习惯【作品均分7.5的学习之神斋藤孝，基于40年经验总结，100个批判型思维习惯，规避常被洗脑的人性弱点】（【日】斋藤孝），ISBN-13 9787559659514"
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
  "common_agent_id": "specials.psychological-profile-agent",
  "pack_id": "specials",
  "mapping_status": "related",
  "source_documents": [
    "docs/special_agents_redesign/agents/psychological_profile_agent.md"
  ],
  "source_sha256": "f1fa518cee669e11195bf6fcc62a63d2befa84c3d8c06a08afc22fecde9c495b",
  "configuration_sha256": "bb4530aea43a6bf9284188c7b5229b93ac8f78e1958ebe448ed4685a57b96688",
  "destination_commit": "5460c4b4a33c15286f9fd84b1bc764d755f5bab0",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "generated_at": "2026-07-26T14:16:45.971735Z",
  "reviewed_by": "specials-self-contained-reviewer",
  "reviewed_at": "2026-07-26T18:00:00Z",
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\specials\\agents\\specials.psychological-profile-agent",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```
