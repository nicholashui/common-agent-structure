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
      "title": "\u7f8e\u7684\u5386\u7a0b",
      "author": "\u674e\u6cfd\u539a",
      "isbn13": "9787108017963",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7f8e\u7684\u5386\u7a0b\uff08\u674e\u6cfd\u539a\uff09\uff0cISBN-13 9787108017963"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u8c08\u7f8e",
      "author": "\u6731\u5149\u6f5c",
      "isbn13": "9787108042262",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8c08\u7f8e\uff08\u6731\u5149\u6f5c\uff09\uff0cISBN-13 9787108042262"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7f8e\u5b66\u6563\u6b65",
      "author": "\u5b97\u767d\u534e",
      "isbn13": "9787532123456",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7f8e\u5b66\u6563\u6b65\uff08\u5b97\u767d\u534e\uff09\uff0cISBN-13 9787532123456"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u89c2\u770b\u4e4b\u9053",
      "isbn13": "9787544715998",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u89c2\u770b\u4e4b\u9053\uff0cISBN-13 9787544715998"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7406\u89e3\u6f2b\u753b",
      "isbn13": "9787513320184",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7406\u89e3\u6f2b\u753b\uff0cISBN-13 9787513320184"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u8bba\u6444\u5f71",
      "isbn13": "9787544722599",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8bba\u6444\u5f71\uff0cISBN-13 9787544722599"
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
      "author": "Andr\u00e9 Bazin",
      "isbn13": "9780520242272",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: What Is Cinema? Vol. 1 (Andr\u00e9 Bazin), ISBN-13 9780520242272"
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
      "author": "Fran\u00e7ois Truffaut",
      "isbn13": "9780671604295",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Hitchcock/Truffaut (Fran\u00e7ois Truffaut), ISBN-13 9780671604295"
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
      "title": "\u7535\u5f71\u827a\u672f\uff1a\u5f62\u5f0f\u4e0e\u98ce\u683c",
      "author": "\u6ce2\u5fb7\u7ef4\u5c14\u3001\u6c64\u666e\u68ee",
      "isbn13": "9787301254332",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7535\u5f71\u827a\u672f\uff1a\u5f62\u5f0f\u4e0e\u98ce\u683c\uff08\u6ce2\u5fb7\u7ef4\u5c14\u3001\u6c64\u666e\u68ee\uff09\uff0cISBN-13 9787301254332"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u8ba4\u8bc6\u7535\u5f71",
      "author": "\u8d3e\u5185\u68af",
      "isbn13": "9787532763122",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8ba4\u8bc6\u7535\u5f71\uff08\u8d3e\u5185\u68af\uff09\uff0cISBN-13 9787532763122"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u96d5\u523b\u65f6\u5149",
      "author": "\u5854\u53ef\u592b\u65af\u57fa",
      "isbn13": "9787532743841",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u96d5\u523b\u65f6\u5149\uff08\u5854\u53ef\u592b\u65af\u57fa\uff09\uff0cISBN-13 9787532743841"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5e0c\u533a\u67ef\u514b\u4e0e\u7279\u5415\u5f17\u5bf9\u8bdd\u5f55",
      "isbn13": "9787532745128",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5e0c\u533a\u67ef\u514b\u4e0e\u7279\u5415\u5f17\u5bf9\u8bdd\u5f55\uff0cISBN-13 9787532745128"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7535\u5f71\u8bed\u8a00\u7684\u8bed\u6cd5",
      "author": "\u963f\u91cc\u6d2a",
      "isbn13": "9787532299990",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7535\u5f71\u8bed\u8a00\u7684\u8bed\u6cd5\uff08\u963f\u91cc\u6d2a\uff09\uff0cISBN-13 9787532299990"
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
      "title": "\u8fbe\u82ac\u5947\u8272\u5f69\u6821\u6b63\u624b\u518c",
      "isbn13": "9787115381231",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8fbe\u82ac\u5947\u8272\u5f69\u6821\u6b63\u624b\u518c\uff0cISBN-13 9787115381231"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u8272\u5f69\u827a\u672f",
      "author": "\u4f0a\u987f",
      "isbn13": "9787532275119",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8272\u5f69\u827a\u672f\uff08\u4f0a\u987f\uff09\uff0cISBN-13 9787532275119"
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
      "title": "\u8bbe\u8ba1\u5fc3\u7406\u5b66",
      "isbn13": "9787115417947",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8bbe\u8ba1\u5fc3\u7406\u5b66\uff0cISBN-13 9787115417947"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u70b9\u77f3\u6210\u91d1",
      "isbn13": "9787115249494",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u70b9\u77f3\u6210\u91d1\uff0cISBN-13 9787115249494"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u754c\u9762\u8bbe\u8ba1\u6a21\u5f0f",
      "isbn13": "9787115331861",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u754c\u9762\u8bbe\u8ba1\u6a21\u5f0f\uff0cISBN-13 9787115331861"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7528\u6237\u4f53\u9a8c\u8981\u7d20",
      "author": "\u52a0\u745e\u7279",
      "isbn13": "9787115325466",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7528\u6237\u4f53\u9a8c\u8981\u7d20\uff08\u52a0\u745e\u7279\uff09\uff0cISBN-13 9787115325466"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u8bbe\u8ba1\u4e2d\u7684\u8bbe\u8ba1",
      "author": "\u539f\u7814\u54c9",
      "isbn13": "9787549559787",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8bbe\u8ba1\u4e2d\u7684\u8bbe\u8ba1\uff08\u539f\u7814\u54c9\uff09\uff0cISBN-13 9787549559787"
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
  "imported_from": "vendor/common-agent-swarm-ops/business/specials/agents/specials.aesthetics-agent",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```
