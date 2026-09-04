# specials.general-creative-agent — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/specials.general-creative-agent/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "specials.general-creative-agent",
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
      "spagent.general-creative-agent-input"
    ],
    "outputs": [
      "spagent.general-creative-agent-output"
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

# General Creative Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.general-creative-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain general creative agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

This is the **definitive, production-grade specification** for building the General Creative Agent (GCA) — a stateful, LLM-orchestrated system that operationalizes the fully refined **Strategic Sparse Outlier Recombination (SSOR) Model**. It includes complete background, the entire iterative evolution from the user’s original idea, exhaustive research synthesis (psychology, neuroscience, computational creativity, science-of-science, arXiv 2024–2025 papers, Anthropic NLAE, and xAI/Grok-related insights), detailed functional requirements, architecture, 7-phase process, domain-specific factory, AI-native POVs, implementation guidelines, evaluation metrics, and full references.

### Domain distillation (embedded, untrusted design provenance)

This is the **definitive, production-grade specification** for building the General Creative Agent (GCA) — a stateful, LLM-orchestrated system that operationalizes the fully refined **Strategic Sparse Outlier Recombination (SSOR) Model**. It includes complete background, the entire iterative evolution from the user’s original idea, exhaustive research synthesis (psychology, neuroscience, computational creativity, science-of-science, arXiv 2024–2025 papers, Anthropic NLAE, and xAI/Grok-related insights), detailed functional requirements, architecture, 7-phase process, domain-specific factory, AI-native POVs, implementation guidelines, evaluation metrics, and full references.

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
- Local rubric reference: `spagent.general-creative-agent-rubric` (inert identifier).
- Prompt reference: `spagent.general-creative-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.general-creative-agent-input"],"outputs":["spagent.general-creative-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.general-creative-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.general-creative-agent-prompt","rubric_reference":"spagent.general-creative-agent-rubric","critique_edges":{"inputs":["spagent.general-creative-agent-input"],"outputs":["spagent.general-creative-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.general-creative-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/general_creative_agent.md`
- Design source SHA-256 (at generation): `35e61afc7c4cfdd5b14ae86ad7ae3baf79d964ede95147932448bac4cdd3c17a`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.

## Prompts

### `prompts/primary.md`

You are a baseline-safe specials pack agent. No network. No production activation.

# General Creative Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.general-creative-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain general creative agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

This is the **definitive, production-grade specification** for building the General Creative Agent (GCA) — a stateful, LLM-orchestrated system that operationalizes the fully refined **Strategic Sparse Outlier Recombination (SSOR) Model**. It includes complete background, the entire iterative evolution from the user’s original idea, exhaustive research synthesis (psychology, neuroscience, computational creativity, science-of-science, arXiv 2024–2025 papers, Anthropic NLAE, and xAI/Grok-related insights), detailed functional requirements, architecture, 7-phase process, domain-specific factory, AI-native POVs, implementation guidelines, evaluation metrics, and full references.

### Domain distillation (embedded, untrusted design provenance)

This is the **definitive, production-grade specification** for building the General Creative Agent (GCA) — a stateful, LLM-orchestrated system that operationalizes the fully refined **Strategic Sparse Outlier Recombination (SSOR) Model**. It includes complete background, the entire iterative evolution from the user’s original idea, exhaustive research synthesis (psychology, neuroscience, computational creativity, science-of-science, arXiv 2024–2025 papers, Anthropic NLAE, and xAI/Grok-related insights), detailed functional requirements, architecture, 7-phase process, domain-specific factory, AI-native POVs, implementation guidelines, evaluation metrics, and full references.

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
- Local rubric reference: `spagent.general-creative-agent-rubric` (inert identifier).
- Prompt reference: `spagent.general-creative-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.general-creative-agent-input"],"outputs":["spagent.general-creative-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.general-creative-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic",

## Rubrics

### `rubrics/primary.md`

Success: stay inside pack responsibility; no network; no production activation.

## Sources

### `sources/MAPPING.md`

# Source mapping note — `specials.general-creative-agent`

- Mapping status: `related` (specials redesign doc → pack agent)
- Design source (historical): `docs/special_agents_redesign/agents/general_creative_agent.md`
- Source SHA-256: `35e61afc7c4cfdd5b14ae86ad7ae3baf79d964ede95147932448bac4cdd3c17a`
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
      "title": "The Creative Habit",
      "author": "Twyla Tharp",
      "isbn13": "9780743235273",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Creative Habit (Twyla Tharp), ISBN-13 9780743235273"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Lateral Thinking",
      "author": "Edward de Bono",
      "isbn13": "9780060903251",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Lateral Thinking (Edward de Bono), ISBN-13 9780060903251"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Six Thinking Hats",
      "author": "Edward de Bono",
      "isbn13": "9780316178310",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Six Thinking Hats (Edward de Bono), ISBN-13 9780316178310"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "A Technique for Producing Ideas",
      "author": "James Webb Young",
      "isbn13": "9780071410946",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: A Technique for Producing Ideas (James Webb Young), ISBN-13 9780071410946"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Steal Like an Artist",
      "author": "Austin Kleon",
      "isbn13": "9780761169253",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Steal Like an Artist (Austin Kleon), ISBN-13 9780761169253"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The War of Art",
      "author": "Steven Pressfield",
      "isbn13": "9781936891023",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The War of Art (Steven Pressfield), ISBN-13 9781936891023"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Bird by Bird",
      "author": "Anne Lamott",
      "isbn13": "9780385480017",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Bird by Bird (Anne Lamott), ISBN-13 9780385480017"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Creative Confidence",
      "author": "Tom & David Kelley",
      "isbn13": "9780385349369",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Creative Confidence (Tom & David Kelley), ISBN-13 9780385349369"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Change by Design",
      "author": "Tim Brown",
      "isbn13": "9780061766084",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Change by Design (Tim Brown), ISBN-13 9780061766084"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u516d\u9876\u601d\u8003\u5e3d",
      "isbn13": "9787508631332",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u516d\u9876\u601d\u8003\u5e3d\uff0cISBN-13 9787508631332"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6c34\u5e73\u601d\u8003",
      "isbn13": "9787508622170",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6c34\u5e73\u601d\u8003\uff0cISBN-13 9787508622170"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u4ea7\u751f\u521b\u610f\u7684\u65b9\u6cd5",
      "isbn13": "9787220101236",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4ea7\u751f\u521b\u610f\u7684\u65b9\u6cd5\uff0cISBN-13 9787220101236"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5077\u5e08\u5b66\u827a",
      "isbn13": "9787550261235",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5077\u5e08\u5b66\u827a\uff0cISBN-13 9787550261235"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u827a\u672f\u4e4b\u6218",
      "isbn13": "9787532753871",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u827a\u672f\u4e4b\u6218\uff0cISBN-13 9787532753871"
    },
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
      "title": "Story",
      "author": "Robert McKee",
      "isbn13": "9780060391683",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Story (Robert McKee), ISBN-13 9780060391683"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Anatomy of Story",
      "author": "John Truby",
      "isbn13": "9780865479937",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Anatomy of Story (John Truby), ISBN-13 9780865479937"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Save the Cat!",
      "author": "Blake Snyder",
      "isbn13": "9781932907001",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Save the Cat! (Blake Snyder), ISBN-13 9781932907001"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Writer's Journey, 3rd ed.",
      "author": "Christopher Vogler",
      "isbn13": "9781932907360",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Writer's Journey, 3rd ed. (Christopher Vogler), ISBN-13 9781932907360"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Hero with a Thousand Faces",
      "author": "Joseph Campbell",
      "isbn13": "9781577315933",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Hero with a Thousand Faces (Joseph Campbell), ISBN-13 9781577315933"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Adventures in the Screen Trade",
      "author": "William Goldman",
      "isbn13": "9780446391177",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Adventures in the Screen Trade (William Goldman), ISBN-13 9780446391177"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Screenplay",
      "author": "Syd Field",
      "isbn13": "9780385339032",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Screenplay (Syd Field), ISBN-13 9780385339032"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Making a Good Script Great, 3rd ed.",
      "author": "Linda Seger",
      "isbn13": "9781932907070",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Making a Good Script Great, 3rd ed. (Linda Seger), ISBN-13 9781932907070"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Screenwriter's Bible, 7th ed.",
      "author": "David Trottier",
      "isbn13": "9781935247210",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Screenwriter's Bible, 7th ed. (David Trottier), ISBN-13 9781935247210"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Wired for Story",
      "author": "Lisa Cron",
      "isbn13": "9781607742456",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Wired for Story (Lisa Cron), ISBN-13 9781607742456"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Into the Woods",
      "author": "John Yorke",
      "isbn13": "9780141978109",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Into the Woods (John Yorke), ISBN-13 9780141978109"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Art of Dramatic Writing",
      "author": "Lajos Egri",
      "isbn13": "9780671213329",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Art of Dramatic Writing (Lajos Egri), ISBN-13 9780671213329"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Poetics",
      "author": "Aristotle; Heath trans.",
      "isbn13": "9780140446364",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Poetics (Aristotle; Heath trans.), ISBN-13 9780140446364"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6545\u4e8b",
      "author": "\u9ea6\u57fa",
      "isbn13": "9787201076942",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6545\u4e8b\uff08\u9ea6\u57fa\uff09\uff0cISBN-13 9787201076942"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6545\u4e8b\u7684\u89e3\u5256",
      "author": "\u7e41\u4f53\u9ea6\u57fa",
      "isbn13": "9789862135488",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6545\u4e8b\u7684\u89e3\u5256\uff08\u7e41\u4f53\u9ea6\u57fa\uff09\uff0cISBN-13 9789862135488"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6551\u732b\u54aa",
      "isbn13": "9787229040727",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6551\u732b\u54aa\uff0cISBN-13 9787229040727"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7535\u5f71\u5267\u672c\u5199\u4f5c\u57fa\u7840",
      "author": "\u6089\u5fb7\u00b7\u83f2\u5c14\u5fb7",
      "isbn13": "9787106021238",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7535\u5f71\u5267\u672c\u5199\u4f5c\u57fa\u7840\uff08\u6089\u5fb7\u00b7\u83f2\u5c14\u5fb7\uff09\uff0cISBN-13 9787106021238"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u620f\u5267\u5199\u4f5c\u57fa\u7840",
      "author": "\u57c3\u683c\u91cc",
      "isbn13": "9787108014504",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u620f\u5267\u5199\u4f5c\u57fa\u7840\uff08\u57c3\u683c\u91cc\uff09\uff0cISBN-13 9787108014504"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "AI\u5199\u4f5c\uff1a\u7528AI\u500d\u901f\u63d0\u5347\u5199\u4f5c\u6548\u7387",
      "author": "\u9093\u4e16\u8d85",
      "isbn13": "9787111760146",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: AI\u5199\u4f5c\uff1a\u7528AI\u500d\u901f\u63d0\u5347\u5199\u4f5c\u6548\u7387\uff08\u9093\u4e16\u8d85\uff09\uff0cISBN-13 9787111760146"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5982\u4f55\u5199\u51fa\u597d\u6545\u4e8b HBO\u5927\u5e08\u5199\u4f5c\u8bfe",
      "isbn13": "9787516827482",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5982\u4f55\u5199\u51fa\u597d\u6545\u4e8b HBO\u5927\u5e08\u5199\u4f5c\u8bfe\uff0cISBN-13 9787516827482"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7ed9\u9752\u5e74\u7f16\u5267\u7684\u4fe13.0",
      "author": "\u5b8b\u65b9\u91d1",
      "isbn13": "9787559493965",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7ed9\u9752\u5e74\u7f16\u5267\u7684\u4fe13.0\uff08\u5b8b\u65b9\u91d1\uff09\uff0cISBN-13 9787559493965"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7f16\u5267\u7684\u827a\u672f",
      "author": "\u57c3\u683c\u91cc",
      "isbn13": "9787550213333",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7f16\u5267\u7684\u827a\u672f\uff08\u57c3\u683c\u91cc\uff09\uff0cISBN-13 9787550213333"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u77ed\u89c6\u9891\u4e0e\u76f4\u64ad\u6587\u6848\u5199\u4f5c",
      "author": "\u5f20\u5f18\u674e\u81ea\u6d77\u9b4f\u575a \u4e3b\u7f16\u5434\u66fc\u5218\u54f2\u674e\u5b88\u52e4 \u526f\u4e3b\u7f16",
      "isbn13": "9787115638649",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u77ed\u89c6\u9891\u4e0e\u76f4\u64ad\u6587\u6848\u5199\u4f5c\uff08\u5f20\u5f18\u674e\u81ea\u6d77\u9b4f\u575a \u4e3b\u7f16\u5434\u66fc\u5218\u54f2\u674e\u5b88\u52e4 \u526f\u4e3b\u7f16\uff09\uff0cISBN-13 9787115638649"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u65b0\u5a92\u4f53\u5e7f\u544a\u4e0e\u6587\u6848\u5199\u4f5c(\u7b2c2\u7248)",
      "author": "\u5468\u9896 \u4e3b\u7f16\u5f20\u6587\u6770 \u4e3b\u7f16\u6731\u6653\u8679 \u526f\u4e3b\u7f16\u738b\u5a1c \u526f\u4e3b\u7f16\u9ec4\u4f1f \u526f\u4e3b\u7f16",
      "isbn13": "9787115648044",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u65b0\u5a92\u4f53\u5e7f\u544a\u4e0e\u6587\u6848\u5199\u4f5c(\u7b2c2\u7248)\uff08\u5468\u9896 \u4e3b\u7f16\u5f20\u6587\u6770 \u4e3b\u7f16\u6731\u6653\u8679 \u526f\u4e3b\u7f16\u738b\u5a1c \u526f\u4e3b\u7f16\u9ec4\u4f1f \u526f\u4e3b\u7f16\uff09\uff0cISBN-13 9787115648044"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5c0f\u8bf4\u7684\u9aa8\u67b6\uff1a\u597d\u63d0\u7eb2\u6210\u5c31\u597d\u6545\u4e8b",
      "author": "[\u7f8e]\u51ef\u8482\u00b7\u7ef4\u5170\u5fb7",
      "isbn13": "9787210099529",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5c0f\u8bf4\u7684\u9aa8\u67b6\uff1a\u597d\u63d0\u7eb2\u6210\u5c31\u597d\u6545\u4e8b\uff08[\u7f8e]\u51ef\u8482\u00b7\u7ef4\u5170\u5fb7\uff09\uff0cISBN-13 9787210099529"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7f16\u5267\u5fc3\u7406\u5b66 \u5728\u5267\u672c\u4e2d\u5efa\u6784\u51b2\u7a81\uff08\uff08\u7f8e\uff09\u5c39\u8fea\u514b\uff09",
      "isbn13": "9789571161488",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7f16\u5267\u5fc3\u7406\u5b66 \u5728\u5267\u672c\u4e2d\u5efa\u6784\u51b2\u7a81\uff08\uff08\u7f8e\uff09\u5c39\u8fea\u514b\uff09\uff0cISBN-13 9789571161488"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6551\u732b\u54aa-\u5c0f\u8bf4\u521b\u4f5c\u6307\u5357",
      "isbn13": "9787522513003",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6551\u732b\u54aa-\u5c0f\u8bf4\u521b\u4f5c\u6307\u5357\uff0cISBN-13 9787522513003"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6551\u732b\u54aa\uff1a\u7535\u5f71\u7f16\u5267\u6307\u5357",
      "isbn13": "9787533963361",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6551\u732b\u54aa\uff1a\u7535\u5f71\u7f16\u5267\u6307\u5357\uff0cISBN-13 9787533963361"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u4eba\u7269\uff1a\u6587\u672c\u3001\u821e\u53f0\u3001\u94f6\u5e55\u89d2\u8272\u4e0e\u5361\u53f8\u8bbe\u8ba1\u7684\u827a\u672f\uff08\u7f16\u5267\u6559\u7236\u7f57\u4f2f\u7279\u00b7\u9ea6\u57fa\u201c\u865a\u6784\u827a\u672f\u4e09\u90e8\u66f2\u201d\u5b8c\u7ed3\u7bc7\uff09",
      "author": "\u7f57\u4f2f\u7279\u00b7\u9ea6\u57fa",
      "isbn13": "9787533969585",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4eba\u7269\uff1a\u6587\u672c\u3001\u821e\u53f0\u3001\u94f6\u5e55\u89d2\u8272\u4e0e\u5361\u53f8\u8bbe\u8ba1\u7684\u827a\u672f\uff08\u7f16\u5267\u6559\u7236\u7f57\u4f2f\u7279\u00b7\u9ea6\u57fa\u201c\u865a\u6784\u827a\u672f\u4e09\u90e8\u66f2\u201d\u5b8c\u7ed3\u7bc7\uff09\uff08\u7f57\u4f2f\u7279\u00b7\u9ea6\u57fa\uff09\uff0cISBN-13 9787533969585"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6551\u732b\u54aa2\u7ecf\u5178\u7535\u5f71\u5267\u672c\u89e3\u6790",
      "isbn13": "9787533964108",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6551\u732b\u54aa2\u7ecf\u5178\u7535\u5f71\u5267\u672c\u89e3\u6790\uff0cISBN-13 9787533964108"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6545\u4e8b\u7684\u89e3\u5256",
      "author": "\u7f85\u4f2f\u7279\uff0e\u9ea5\u57fa(Robert McKee)",
      "isbn13": "9787201094601",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6545\u4e8b\u7684\u89e3\u5256 (\u7f85\u4f2f\u7279\uff0e\u9ea5\u57fa(Robert McKee))\uff0cISBN-13 9787201094601"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5c0d\u767d\u7684\u89e3\u5256",
      "isbn13": "9789864898435",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5c0d\u767d\u7684\u89e3\u5256\uff0cISBN-13 9789864898435"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u4eba\u7269\u7684\u89e3\u5256",
      "isbn13": "9789864896257",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4eba\u7269\u7684\u89e3\u5256\uff0cISBN-13 9789864896257"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u8afe\u862d\u8b8a\u594f\u66f2",
      "isbn13": "9789863844693",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8afe\u862d\u8b8a\u594f\u66f2\uff0cISBN-13 9789863844693"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u4f5c\u5bb6\u7684\u7075\u611f\u5b9d\u5e93",
      "isbn13": "9787514220155",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4f5c\u5bb6\u7684\u7075\u611f\u5b9d\u5e93\uff0cISBN-13 9787514220155"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u53d1\u73b0\u4f60\u7684\u521b\u9020\u529b\u7c7b\u578b",
      "isbn13": "9787210108061",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u53d1\u73b0\u4f60\u7684\u521b\u9020\u529b\u7c7b\u578b\uff0cISBN-13 9787210108061"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7545\u9500\u4f5c\u5bb6\u5199\u4f5c\u5168\u6280\u5de7",
      "isbn13": "9787210092452",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7545\u9500\u4f5c\u5bb6\u5199\u4f5c\u5168\u6280\u5de7\uff0cISBN-13 9787210092452"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5c0f\u8bf4\u7684\u516b\u767e\u4e07\u79cd\u5199\u6cd5",
      "isbn13": "9786263100442",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5c0f\u8bf4\u7684\u516b\u767e\u4e07\u79cd\u5199\u6cd5\uff0cISBN-13 9786263100442"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5199\u5c0f\u8bf4\u6700\u91cd\u8981\u7684\u5341\u4ef6\u4e8b",
      "isbn13": "9787210108672",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5199\u5c0f\u8bf4\u6700\u91cd\u8981\u7684\u5341\u4ef6\u4e8b\uff0cISBN-13 9787210108672"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Essential Screenplay (3-Book Bundle)",
      "author": "Field, Syd",
      "isbn13": "9780307423269",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Essential Screenplay (3-Book Bundle) (Field, Syd), ISBN-13 9780307423269"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7535\u5f71\u7f16\u5267\u5b66\uff08\u4fee\u8ba2\u7248\uff09",
      "author": "\u6c6a\u6d41",
      "isbn13": "9787811272406",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7535\u5f71\u7f16\u5267\u5b66\uff08\u4fee\u8ba2\u7248\uff09\uff08\u6c6a\u6d41\uff09\uff0cISBN-13 9787811272406"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5b9e\u7528\u7535\u5f71\u7f16\u5267",
      "author": "\u5f20\u89c9\u660e",
      "isbn13": "9787106029234",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5b9e\u7528\u7535\u5f71\u7f16\u5267\uff08\u5f20\u89c9\u660e\uff09\uff0cISBN-13 9787106029234"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6545\u4e8b\u7247\u521b\u4f5c\u516d\u8bb2",
      "author": "\u738b\u7ade",
      "isbn13": "9787541151323",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6545\u4e8b\u7247\u521b\u4f5c\u516d\u8bb2\uff08\u738b\u7ade\uff09\uff0cISBN-13 9787541151323"
    }
  ],
  "common_agent_id": "specials.general-creative-agent",
  "pack_id": "specials",
  "mapping_status": "related",
  "source_documents": [
    "docs/special_agents_redesign/agents/general_creative_agent.md"
  ],
  "source_sha256": "35e61afc7c4cfdd5b14ae86ad7ae3baf79d964ede95147932448bac4cdd3c17a",
  "configuration_sha256": "c34dee0c65c2194a5801f6da966888b7ab3ff171ef77e0bfacda479dfacfad12",
  "destination_commit": "5460c4b4a33c15286f9fd84b1bc764d755f5bab0",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "generated_at": "2026-07-26T14:16:45.937280Z",
  "reviewed_by": "specials-self-contained-reviewer",
  "reviewed_at": "2026-07-26T18:00:00Z",
  "imported_from": "vendor/common-agent-swarm-ops/business/specials/agents/specials.general-creative-agent",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```
