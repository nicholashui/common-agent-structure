# specials.aesthetics-agent — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/specials.aesthetics-agent/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "specials.aesthetics-agent",
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
      "spagent.aesthetics-agent-input"
    ],
    "outputs": [
      "spagent.aesthetics-agent-output"
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

# Aesthetics Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.aesthetics-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain aesthetics agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

This is the **definitive, production-grade specification** for building the **Aesthetics Agent** — a stateful, multimodal evaluation-and-alignment service that operationalizes a simulated **"artiste sense"** (artistic/aesthetic intuition) for the entire VA-Agent-Swarm. It is the deep rethink of [`aesthetics_agents.md`](./aesthetics_agents.md): where that document is a *survey of methods*, this is a *buildable agent contract*. It reframes "teach AI artistic sense" from a single image scorer into a **shared aesthetic nervous system** — a critic that every generative agent consults, a reward signal that every fine-tuning loop trusts, and a personalization engine that carries a director's, brand's, or artist's taste across the whole pipeline.

### Domain distillation (embedded, untrusted design provenance)

This is the **definitive, production-grade specification** for building the **Aesthetics Agent** — a stateful, multimodal evaluation-and-alignment service that operationalizes a simulated **"artiste sense"** (artistic/aesthetic intuition) for the entire VA-Agent-Swarm. It is the deep rethink of [`aesthetics_agents.md`](./aesthetics_agents.md): where that document is a *survey of methods*, this is a *buildable agent contract*. It reframes "teach AI artistic sense" from a single image scorer into a **shared aesthetic nervous system** — a critic that every generative agent consults, a reward signal that every fine-tuning loop trusts, and a personalization engine that carries a director's, brand's, or artist's taste across the whole pipeline.

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
- Local rubric reference: `spagent.aesthetics-agent-rubric` (inert identifier).
- Prompt reference: `spagent.aesthetics-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.aesthetics-agent-input"],"outputs":["spagent.aesthetics-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.aesthetics-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.aesthetics-agent-prompt","rubric_reference":"spagent.aesthetics-agent-rubric","critique_edges":{"inputs":["spagent.aesthetics-agent-input"],"outputs":["spagent.aesthetics-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.aesthetics-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/aesthetics_agent.md`
- Design source SHA-256 (at generation): `7d5b36b2dbc4e70664e9213d5a89d057935e54a1c3f6ab8cbb639fee5ab0f8d1`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.

## Prompts

### `prompts/primary.md`

# Aesthetics Agent — offline Host prompt (specials.aesthetics-agent)

You are the swarm **Aesthetics Agent** (computational artiste-sense).

## Role
1. **Critic** — decompose visual quality into dimensions D1–D10 with confidences.
2. **Aligner** — emit actionable critique, prompt steers, and training-safe reward metadata.
3. **Taste-Keeper** — score only under an explicit `AestheticProfile` (or neutral baseline).

## Hard rules
- Never emit a naked scalar without the full vector + `hack_likelihood`.
- Low confidence or high hack likelihood → `escalate_to_hitl`.
- Live multimodal vision is **off** on Host foundation; offline deterministic path only unless Host go-live.
- Production media activation remains fail-closed.

## Dimensions
composition · color_harmony · light · depth · subject · technical · emotion · style_fidelity · novelty · temporal

### `prompts/SYSTEM.md`

# Aesthetics Agent — offline Host prompt (specials.aesthetics-agent)

You are the swarm **Aesthetics Agent** (computational artiste-sense).

## Role
1. **Critic** — decompose visual quality into dimensions D1–D10 with confidences.
2. **Aligner** — emit actionable critique, prompt steers, and training-safe reward metadata.
3. **Taste-Keeper** — score only under an explicit `AestheticProfile` (or neutral baseline).

## Hard rules
- Never emit a naked scalar without the full vector + `hack_likelihood`.
- Low confidence or high hack likelihood → `escalate_to_hitl`.
- Live multimodal vision is **off** on Host foundation; offline deterministic path only unless Host go-live.
- Production media activation remains fail-closed.

## Dimensions
composition · color_harmony · light · depth · subject · technical · emotion · style_fidelity · novelty · temporal

## Rubrics

### `rubrics/L2.md`

# Aesthetics Agent L2 rubric (offline Host foundation)

Pass when offline evaluate produces:

| Check | Gate |
|-------|------|
| AestheticVector complete | All D1–D10 present in [0,1] |
| Confidence present | Per-dimension confidence |
| No naked scalar | `aesthetic_quality` accompanied by vector + hack |
| Profile resolved | Explicit profile_id or neutral_baseline flag |
| Anti-hack field | `hack_likelihood` in [0,1] |
| Critique usable | ≥1 actionable_critique line on score/align/refine |

Fail / escalate:

- `hack_likelihood` ≥ 0.55
- any confidence < 0.65 (uncertainty_flag)
- `aesthetic_quality` < 0.25

Live SigLIP/VLM correlation targets (ρ ≥ 0.75) are **not** enforced in offline stub mode.

### `rubrics/primary.md`

# Aesthetics Agent L2 rubric (offline Host foundation)

Pass when offline evaluate produces:

| Check | Gate |
|-------|------|
| AestheticVector complete | All D1–D10 present in [0,1] |
| Confidence present | Per-dimension confidence |
| No naked scalar | `aesthetic_quality` accompanied by vector + hack |
| Profile resolved | Explicit profile_id or neutral_baseline flag |
| Anti-hack field | `hack_likelihood` in [0,1] |
| Critique usable | ≥1 actionable_critique line on score/align/refine |

Fail / escalate:

- `hack_likelihood` ≥ 0.55
- any confidence < 0.65 (uncertainty_flag)
- `aesthetic_quality` < 0.25

Live SigLIP/VLM correlation targets (ρ ≥ 0.75) are **not** enforced in offline stub mode.

## Sources

### `sources/MAPPING.md`

# Source mapping note — `specials.aesthetics-agent`

- Mapping status: `related` (specials redesign doc → pack agent)
- Design source (historical): `docs/special_agents_redesign/agents/aesthetics_agent.md`
- Source SHA-256: `7d5b36b2dbc4e70664e9213d5a89d057935e54a1c3f6ab8cbb639fee5ab0f8d1`
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
      "title": "Ways of Seeing",
      "author": "John Berger",
      "isbn13": "9780140135152",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Ways of Seeing (John Berger), ISBN-13 9780140135152"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Interaction of Color",
      "author": "Josef Albers",
      "isbn13": "9780300179354",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Interaction of Color (Josef Albers), ISBN-13 9780300179354"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Understanding Comics",
      "author": "Scott McCloud",
      "isbn13": "9780060976255",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Understanding Comics (Scott McCloud), ISBN-13 9780060976255"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Art of Color",
      "author": "Itten",
      "isbn13": "9780471289289",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Art of Color (Itten), ISBN-13 9780471289289"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Camera Lucida",
      "author": "Roland Barthes",
      "isbn13": "9780374532338",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Camera Lucida (Roland Barthes), ISBN-13 9780374532338"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "On Photography",
      "author": "Susan Sontag",
      "isbn13": "9780312420093",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: On Photography (Susan Sontag), ISBN-13 9780312420093"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "美的历程",
      "author": "李泽厚",
      "isbn13": "9787108017963",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 美的历程（李泽厚），ISBN-13 9787108017963"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "谈美",
      "author": "朱光潜",
      "isbn13": "9787108042262",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 谈美（朱光潜），ISBN-13 9787108042262"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "美学散步",
      "author": "宗白华",
      "isbn13": "9787532123456",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 美学散步（宗白华），ISBN-13 9787532123456"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "观看之道",
      "isbn13": "9787544715998",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 观看之道，ISBN-13 9787544715998"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "理解漫画",
      "isbn13": "9787513320184",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 理解漫画，ISBN-13 9787513320184"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "论摄影",
      "isbn13": "9787544722599",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 论摄影，ISBN-13 9787544722599"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Film Art: An Introduction, 12th ed.",
      "author": "Bordwell, Thompson, Smith",
      "isbn13": "9781259534959",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Film Art: An Introduction, 12th ed. (Bordwell, Thompson, Smith), ISBN-13 9781259534959"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Understanding Movies, 14th ed.",
      "author": "Louis Giannetti",
      "isbn13": "9780205856169",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Understanding Movies, 14th ed. (Louis Giannetti), ISBN-13 9780205856169"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Filmmaker's Handbook, 5th ed.",
      "author": "Ascher & Pincus",
      "isbn13": "9780452297289",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Filmmaker's Handbook, 5th ed. (Ascher & Pincus), ISBN-13 9780452297289"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "How to Read a Film, 4th ed.",
      "author": "James Monaco",
      "isbn13": "9780195321050",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: How to Read a Film, 4th ed. (James Monaco), ISBN-13 9780195321050"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Film History: An Introduction",
      "author": "Thompson & Bordwell",
      "isbn13": "9780073386133",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Film History: An Introduction (Thompson & Bordwell), ISBN-13 9780073386133"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "What Is Cinema? Vol. 1",
      "author": "André Bazin",
      "isbn13": "9780520242272",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: What Is Cinema? Vol. 1 (André Bazin), ISBN-13 9780520242272"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Sculpting in Time",
      "author": "Andrei Tarkovsky",
      "isbn13": "9780292776241",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Sculpting in Time (Andrei Tarkovsky), ISBN-13 9780292776241"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Hitchcock/Truffaut",
      "author": "François Truffaut",
      "isbn13": "9780671604295",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Hitchcock/Truffaut (François Truffaut), ISBN-13 9780671604295"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Notes on the Cinematograph",
      "author": "Robert Bresson",
      "isbn13": "9781681370248",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Notes on the Cinematograph (Robert Bresson), ISBN-13 9781681370248"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "电影艺术：形式与风格",
      "author": "波德维尔、汤普森",
      "isbn13": "9787301254332",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影艺术：形式与风格（波德维尔、汤普森），ISBN-13 9787301254332"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "认识电影",
      "author": "贾内梯",
      "isbn13": "9787532763122",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 认识电影（贾内梯），ISBN-13 9787532763122"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "雕刻时光",
      "author": "塔可夫斯基",
      "isbn13": "9787532743841",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 雕刻时光（塔可夫斯基），ISBN-13 9787532743841"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "希区柯克与特吕弗对话录",
      "isbn13": "9787532745128",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 希区柯克与特吕弗对话录，ISBN-13 9787532745128"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "电影语言的语法",
      "author": "阿里洪",
      "isbn13": "9787532299990",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影语言的语法（阿里洪），ISBN-13 9787532299990"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Color Correction Handbook, 2nd ed.",
      "author": "Alexis Van Hurkman",
      "isbn13": "9780321929662",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Color Correction Handbook, 2nd ed. (Alexis Van Hurkman), ISBN-13 9780321929662"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Color and Mastering for Digital Cinema",
      "author": "Glenn Kennel",
      "isbn13": "9780240808741",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Color and Mastering for Digital Cinema (Glenn Kennel), ISBN-13 9780240808741"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "达芬奇色彩校正手册",
      "isbn13": "9787115381231",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 达芬奇色彩校正手册，ISBN-13 9787115381231"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "色彩艺术",
      "author": "伊顿",
      "isbn13": "9787532275119",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 色彩艺术（伊顿），ISBN-13 9787532275119"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Design of Everyday Things, Rev.",
      "author": "Don Norman",
      "isbn13": "9780465050659",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Design of Everyday Things, Rev. (Don Norman), ISBN-13 9780465050659"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Don't Make Me Think, Revisited",
      "author": "Steve Krug",
      "isbn13": "9780321965516",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Don't Make Me Think, Revisited (Steve Krug), ISBN-13 9780321965516"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "About Face, 4th ed.",
      "author": "Cooper et al.",
      "isbn13": "9781118766576",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: About Face, 4th ed. (Cooper et al.), ISBN-13 9781118766576"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Designing Interfaces, 3rd ed.",
      "author": "Tidwell et al.",
      "isbn13": "9781492051961",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Designing Interfaces, 3rd ed. (Tidwell et al.), ISBN-13 9781492051961"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "100 Things Every Designer Needs to Know About People",
      "author": "Susan Weinschenk",
      "isbn13": "9780321767530",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: 100 Things Every Designer Needs to Know About People (Susan Weinschenk), ISBN-13 9780321767530"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Universal Principles of Design",
      "author": "Lidwell, Holden, Butler",
      "isbn13": "9781592535873",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Universal Principles of Design (Lidwell, Holden, Butler), ISBN-13 9781592535873"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "设计心理学",
      "isbn13": "9787115417947",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 设计心理学，ISBN-13 9787115417947"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "点石成金",
      "isbn13": "9787115249494",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 点石成金，ISBN-13 9787115249494"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "界面设计模式",
      "isbn13": "9787115331861",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 界面设计模式，ISBN-13 9787115331861"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "用户体验要素",
      "author": "加瑞特",
      "isbn13": "9787115325466",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 用户体验要素（加瑞特），ISBN-13 9787115325466"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "设计中的设计",
      "author": "原研哉",
      "isbn13": "9787549559787",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 设计中的设计（原研哉），ISBN-13 9787549559787"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Art and Technique of Digital Color Correction",
      "author": "Steve Hullfish",
      "isbn13": "9780240817156",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Art and Technique of Digital Color Correction (Steve Hullfish), ISBN-13 9780240817156"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Color Mixing Handbook",
      "author": "Various Contributors",
      "isbn13": "9780715335550",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Color Mixing Handbook (Various Contributors), ISBN-13 9780715335550"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Film Posters Exploitation",
      "author": "Dave Kehr, Tony Nourmand, Graham Marsh",
      "isbn13": "9783822856253",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Film Posters Exploitation (Dave Kehr, Tony Nourmand, Graham Marsh), ISBN-13 9783822856253"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Poster Art from the Classic Monster Films",
      "author": "Philip J. Riley",
      "isbn13": "9781593934866",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Poster Art from the Classic Monster Films (Philip J. Riley), ISBN-13 9781593934866"
    }
  ],
  "common_agent_id": "specials.aesthetics-agent",
  "pack_id": "specials",
  "mapping_status": "related",
  "source_documents": [
    "docs/special_agents_redesign/agents/aesthetics_agent.md"
  ],
  "source_sha256": "7d5b36b2dbc4e70664e9213d5a89d057935e54a1c3f6ab8cbb639fee5ab0f8d1",
  "configuration_sha256": "0a6ec24af4f79a6640f921c7aeb020dbe9d4e01783b36a47ae14f1ac5034da7c",
  "destination_commit": "5460c4b4a33c15286f9fd84b1bc764d755f5bab0",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "generated_at": "2026-07-26T14:16:45.905948Z",
  "reviewed_by": "specials-self-contained-reviewer",
  "reviewed_at": "2026-07-26T18:00:00Z",
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\specials\\agents\\specials.aesthetics-agent",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```
