# specials.intent-analysis-agent — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/specials.intent-analysis-agent/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "specials.intent-analysis-agent",
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
      "spagent.intent-analysis-agent-input"
    ],
    "outputs": [
      "spagent.intent-analysis-agent-output"
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

# Intent Analysis Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.intent-analysis-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain intent analysis agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

The **Deep Intent Analysis Framework (DIA) v2.0** is a complete, production-ready, modular system for systematically decoding any text’s **purpose**, **hidden agenda**, **multi-angle perspectives**, **illocutionary force**, and **ethical/behavioral quality**. It transforms the original 6-phase manual/LLM-prompt pipeline into a **fully specified, agentic, evaluable software system** built on xAI’s Grok-4.3 (or latest) with native tool use, 1M+ token context, structured outputs, and low-hallucination reasoning. **Core Objectives** - Answer: *Why does this language exist? What is the real goal? What is hidden? How many angles exist? Is the behavior good/wrong/effective?* - Achieve human-expert-level pragmatic reasoning at scale. - Support manual use, API, web app, IDE plugin, and enterprise analytics. **Key v2.0 Improvements (from arXiv + xAI research)** - **Pragmatic Inference Chain (PIC)** integration for superior implicature & hidden-agenda detection. - **Multi-Perspective Agent Simulation** (inspired by multi-party conversational agents survey) for richer angle mapping. - **Gricean + Extended Maxims** (including Benevolence & Transparency for AI contexts). - **Automated Speech Act / Dialog Act Classification** using recent taxonomies and LLM judges. - **Hybrid Evaluation Pipeline** (automatic metrics + human-in-the-loop). - **Native xAI Integration**: Grok-4.3 reasoning modes, tool calling, real-time search for context validation. **Target Users** Journalists, analysts, researchers, educators, content moderators, legal teams, AI safety engineers, and power users who want to “see through” language.

### Domain distillation (embedded, untrusted design provenance)

The **Deep Intent Analysis Framework (DIA) v2.0** is a complete, production-ready, modular system for systematically decoding any text’s **purpose**, **hidden agenda**, **multi-angle perspectives**, **illocutionary force**, and **ethical/behavioral quality**. It transforms the original 6-phase manual/LLM-prompt pipeline into a **fully specified, agentic, evaluable software system** built on xAI’s Grok-4.3 (or latest) with native tool use, 1M+ token context, structured outputs, and low-hallucination reasoning. **Core Objectives** - Answer: *Why does this language exist? What is the real goal? What is hidden? How many angles exist? Is the behavior good/wrong/effective?* - Achieve human-expert-level pragmatic reasoning at scale. - Support manual use, API, web app, IDE plugin, and enterprise analytics. **Key v2.0 Improvements (from arXiv + xAI research)** - **Pragmatic Inference Chain (PIC)** integration for superior implicature & hidden-agenda detection. - **Multi-Perspective Agent Simulation** (inspired by multi-party conversational agents survey) for richer angle mapping. - **Gricean + Extended Maxims** (including Benevolence & Transparency for AI contexts). - **Automated Speech Act / Dialog Act Classification** using recent taxonomies and LLM judges. - **Hybrid Evaluation Pipeline** (automatic metrics + human-in-the-loop). - **Native xAI Integration**: Grok-4.3 reasoning modes, tool calling, real-time search for context validation. **Target Users** Journalists, analysts, researchers, educators, content moderators, legal teams, AI safety engineers, and power users who want to “see through” language.

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
- Local rubric reference: `spagent.intent-analysis-agent-rubric` (inert identifier).
- Prompt reference: `spagent.intent-analysis-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.intent-analysis-agent-input"],"outputs":["spagent.intent-analysis-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.intent-analysis-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.intent-analysis-agent-prompt","rubric_reference":"spagent.intent-analysis-agent-rubric","critique_edges":{"inputs":["spagent.intent-analysis-agent-input"],"outputs":["spagent.intent-analysis-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.intent-analysis-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/intent_analysis_agent.md`
- Design source SHA-256 (at generation): `f0c895b3438bfe511c44876f2ceeb8126d09e9114fa094d0e19f0e1d955d5bf7`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.

## Prompts

### `prompts/primary.md`

You are a baseline-safe specials pack agent. No network. No production activation.

# Intent Analysis Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.intent-analysis-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain intent analysis agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

The **Deep Intent Analysis Framework (DIA) v2.0** is a complete, production-ready, modular system for systematically decoding any text’s **purpose**, **hidden agenda**, **multi-angle perspectives**, **illocutionary force**, and **ethical/behavioral quality**. It transforms the original 6-phase manual/LLM-prompt pipeline into a **fully specified, agentic, evaluable software system** built on xAI’s Grok-4.3 (or latest) with native tool use, 1M+ token context, structured outputs, and low-hallucination reasoning. **Core Objectives** - Answer: *Why does this language exist? What is the real goal? What is hidden? How many angles exist? Is the behavior good/wrong/effective?* - Achieve human-expert-level pragmatic reasoning at scale. - Support manual use, API, web app, IDE plugin, and enterprise analytics. **Key v2.0 Improvements (from arXiv + xAI research)** - **Pragmatic Inference Chain (PIC)** integration for superior implicature & hidden-agenda detection. - **Multi-Perspective Agent Simulation** (inspired by multi-party conversational agents survey) for richer angle mapping. - **Gricean + Extended Maxims** (including Benevolence & Transparency for AI contexts). - **Automated Speech Act / Dialog Act Classification** using recent taxonomies and LLM judges. - **Hybrid Evaluation Pipeline** (automatic metrics + human-in-the-loop). - **Native xAI Integration**: Grok-4.3 reasoning modes, tool calling, real-time search for context validation. **Target Users** Journalists, analysts, researchers, educators, content moderators, legal teams, AI safety engineers, and power users who want to “see through” language.

### Domain distillation (embedded, untrusted design provenance)

The **Deep Intent Analysis Framework (DIA) v2.0** is a complete, production-ready, modular system for systematically decoding any text’s **purpose**, **hidden agenda**, **multi-angle perspectives**, **illocutionary force**, and **ethical/behavioral quality**. It transforms the original 6-phase manual/LLM-prompt pipeline into a **fully specified, agentic, evaluable software system** built on xAI’s Grok-4.3 (or latest) with native tool use, 1M+ token context, structured outputs, and low-hallucination reasoning. **Core Objectives** - Answer: *Why does this language exist? What is the real goal? What is hidden? How many angles exist? Is the behavior good/wrong/effective?* - Achieve human-expert-level pragmatic reasoning at scale. - Support manual use, API, web app, IDE plugin, and enterprise analytics. **Key v2.0 Improvements (from arXiv + xAI research)** - **Pragmatic Inference Chain (PIC)** integration for superior implicature & hidden-agenda detection. - **Multi-Perspective Agent Simulation** (inspired by multi-party conversational agents survey) for richer angle mapping. - **Gricean + Extended Maxims** (including Benevolence & Transparency for AI contexts). - **Automated Speech Act / Dialog Act Classification** using recent taxonomies and LLM judges. - **Hybrid Evaluation Pipeline** (automatic metrics + human-in-the-loop). - **Native xAI Integration**: Grok-4.3 reasoning modes, tool calling, real-time search for context validation. **Target Users** Journalists, analysts, researchers, educators, content moderators, legal teams, AI safety engineers, and power users who want to “see through” language.


## Rubrics

### `rubrics/primary.md`

Success: stay inside pack responsibility; no network; no production activation.

## Sources

### `sources/MAPPING.md`

# Source mapping note — `specials.intent-analysis-agent`

- Mapping status: `related` (specials redesign doc → pack agent)
- Design source (historical): `docs/special_agents_redesign/agents/intent_analysis_agent.md`
- Source SHA-256: `f0c895b3438bfe511c44876f2ceeb8126d09e9114fa094d0e19f0e1d955d5bf7`
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
      "title": "How to Do Things with Words",
      "author": "J. L. Austin",
      "isbn13": "9780674411524",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: How to Do Things with Words (J. L. Austin), ISBN-13 9780674411524"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Speech Acts",
      "author": "John Searle",
      "isbn13": "9780521096263",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Speech Acts (John Searle), ISBN-13 9780521096263"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Metaphors We Live By",
      "author": "Lakoff & Johnson",
      "isbn13": "9780226468013",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Metaphors We Live By (Lakoff & Johnson), ISBN-13 9780226468013"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "我们如何思维",
      "author": "杜威",
      "isbn13": "9787100098489",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 我们如何思维（杜威），ISBN-13 9787100098489"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "语言哲学",
      "author": "陈嘉映",
      "isbn13": "9787301162262",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 语言哲学（陈嘉映），ISBN-13 9787301162262"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "我们赖以生存的隐喻",
      "isbn13": "9787301162279",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 我们赖以生存的隐喻，ISBN-13 9787301162279"
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
      "language": "EN",
      "title": "The Elements of Journalism, 3rd ed.",
      "author": "Kovach & Rosenstiel",
      "isbn13": "9780804136785",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Elements of Journalism, 3rd ed. (Kovach & Rosenstiel), ISBN-13 9780804136785"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Blur",
      "author": "Kovach & Rosenstiel",
      "isbn13": "9781608193011",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Blur (Kovach & Rosenstiel), ISBN-13 9781608193011"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Associated Press Stylebook",
      "isbn13": "9781541649883",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Associated Press Stylebook, ISBN-13 9781541649883"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "On Writing Well",
      "author": "William Zinsser",
      "isbn13": "9780060891541",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: On Writing Well (William Zinsser), ISBN-13 9780060891541"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Craft of Research, 4th ed.",
      "author": "Booth et al.",
      "isbn13": "9780226239736",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Craft of Research, 4th ed. (Booth et al.), ISBN-13 9780226239736"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Interviewing as Qualitative Research, 4th ed.",
      "author": "Irving Seidman",
      "isbn13": "9780807755679",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Interviewing as Qualitative Research, 4th ed. (Irving Seidman), ISBN-13 9780807755679"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "新闻的十大基本原则",
      "isbn13": "9787301161111",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 新闻的十大基本原则，ISBN-13 9787301161111"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "采访的艺术",
      "isbn13": "9787301169186",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 采访的艺术，ISBN-13 9787301169186"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "如何阅读一本书",
      "isbn13": "9787100040945",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 如何阅读一本书，ISBN-13 9787100040945"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "研究是一门艺术",
      "isbn13": "9787300116226",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 研究是一门艺术，ISBN-13 9787300116226"
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
  "common_agent_id": "specials.intent-analysis-agent",
  "pack_id": "specials",
  "mapping_status": "related",
  "source_documents": [
    "docs/special_agents_redesign/agents/intent_analysis_agent.md"
  ],
  "source_sha256": "f0c895b3438bfe511c44876f2ceeb8126d09e9114fa094d0e19f0e1d955d5bf7",
  "configuration_sha256": "9ccb51486c62d7bbc54442a37e9a1cf69dc1648a376f01d3aeb4aa7e8114e8c6",
  "destination_commit": "5460c4b4a33c15286f9fd84b1bc764d755f5bab0",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "generated_at": "2026-07-26T14:16:45.942257Z",
  "reviewed_by": "specials-self-contained-reviewer",
  "reviewed_at": "2026-07-26T18:00:00Z",
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\specials\\agents\\specials.intent-analysis-agent",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```
