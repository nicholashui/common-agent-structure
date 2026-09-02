# specials.podcast-agent — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/specials.podcast-agent/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "specials.podcast-agent",
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
      "spagent.podcast-agent-input"
    ],
    "outputs": [
      "spagent.podcast-agent-output"
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

# Podcast Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.podcast-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain podcast agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

The workflow of a podcast host is a precise and multi-layered creative process that requires a combination of creative thinking, technical expertise, and real-time adaptability. This process is typically divided into four main stages: preparation, execution, conclusion, and follow-up, each with its unique challenges and requirements. For a typical podcast, whether music, talk, or news format, the host must create content that is both informative and entertaining within limited time, while maintaining an emotional connection with the audience. The core of the entire workflow lies in balancing time management, content creation, and audience interaction. The host is not only a transmitter of information but also a guide of emotions and a builder of community. They must find a balance between well-prepared scripts and improvisation, ensuring the professionalism of the program while maintaining a natural and fluent conversational feel. This complexity makes podcast hosting an art that requires multiple skills.

### Domain distillation (embedded, untrusted design provenance)

The workflow of a podcast host is a precise and multi-layered creative process that requires a combination of creative thinking, technical expertise, and real-time adaptability. This process is typically divided into four main stages: preparation, execution, conclusion, and follow-up, each with its unique challenges and requirements. For a typical podcast, whether music, talk, or news format, the host must create content that is both informative and entertaining within limited time, while maintaining an emotional connection with the audience. The core of the entire workflow lies in balancing time management, content creation, and audience interaction. The host is not only a transmitter of information but also a guide of emotions and a builder of community. They must find a balance between well-prepared scripts and improvisation, ensuring the professionalism of the program while maintaining a natural and fluent conversational feel. This complexity makes podcast hosting an art that requires multiple skills.

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
- Local rubric reference: `spagent.podcast-agent-rubric` (inert identifier).
- Prompt reference: `spagent.podcast-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.podcast-agent-input"],"outputs":["spagent.podcast-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.podcast-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.podcast-agent-prompt","rubric_reference":"spagent.podcast-agent-rubric","critique_edges":{"inputs":["spagent.podcast-agent-input"],"outputs":["spagent.podcast-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.podcast-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/podcast_agent.md`
- Design source SHA-256 (at generation): `f8a76576bd0b39c7a6aa4935532040d2c451b783804195f4149e1e38be761dd6`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.

## Prompts

### `prompts/primary.md`

You are a baseline-safe specials pack agent. No network. No production activation.

# Podcast Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.podcast-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain podcast agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

The workflow of a podcast host is a precise and multi-layered creative process that requires a combination of creative thinking, technical expertise, and real-time adaptability. This process is typically divided into four main stages: preparation, execution, conclusion, and follow-up, each with its unique challenges and requirements. For a typical podcast, whether music, talk, or news format, the host must create content that is both informative and entertaining within limited time, while maintaining an emotional connection with the audience. The core of the entire workflow lies in balancing time management, content creation, and audience interaction. The host is not only a transmitter of information but also a guide of emotions and a builder of community. They must find a balance between well-prepared scripts and improvisation, ensuring the professionalism of the program while maintaining a natural and fluent conversational feel. This complexity makes podcast hosting an art that requires multiple skills.

### Domain distillation (embedded, untrusted design provenance)

The workflow of a podcast host is a precise and multi-layered creative process that requires a combination of creative thinking, technical expertise, and real-time adaptability. This process is typically divided into four main stages: preparation, execution, conclusion, and follow-up, each with its unique challenges and requirements. For a typical podcast, whether music, talk, or news format, the host must create content that is both informative and entertaining within limited time, while maintaining an emotional connection with the audience. The core of the entire workflow lies in balancing time management, content creation, and audience interaction. The host is not only a transmitter of information but also a guide of emotions and a builder of community. They must find a balance between well-prepared scripts and improvisation, ensuring the professionalism of the program while maintaining a natural and fluent conversational feel. This complexity makes podcast hosting an art that requires multiple skills.

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
- Local rubric reference: `spagent.podcast-agent-rubric` (inert identifier).
- Prompt reference: `spagent.podcast-agent-prompt` (inert identifier).
- Crit

## Rubrics

### `rubrics/primary.md`

Success: stay inside pack responsibility; no network; no production activation.

## Sources

### `sources/MAPPING.md`

# Source mapping note — `specials.podcast-agent`

- Mapping status: `related` (specials redesign doc → pack agent)
- Design source (historical): `docs/special_agents_redesign/agents/podcast_agent.md`
- Source SHA-256: `f8a76576bd0b39c7a6aa4935532040d2c451b783804195f4149e1e38be761dd6`
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
      "title": "Out on the Wire",
      "author": "Jessica Abel",
      "isbn13": "9780385348430",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Out on the Wire (Jessica Abel), ISBN-13 9780385348430"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Sound Reporting",
      "author": "Jonathan Kern",
      "isbn13": "9780226431789",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Sound Reporting (Jonathan Kern), ISBN-13 9780226431789"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Reality Radio, 2nd ed.",
      "author": "John Biewen, ed.",
      "isbn13": "9781469633138",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Reality Radio, 2nd ed. (John Biewen, ed.), ISBN-13 9781469633138"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "声音设计",
      "isbn13": "9787106031237",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 声音设计，ISBN-13 9787106031237"
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
      "language": "EN",
      "title": "Sound Design",
      "author": "David Sonnenschein",
      "isbn13": "9780941188265",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Sound Design (David Sonnenschein), ISBN-13 9780941188265"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Foley Grail, 2nd ed.",
      "author": "Vanessa Theme Ament",
      "isbn13": "9780240824260",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Foley Grail, 2nd ed. (Vanessa Theme Ament), ISBN-13 9780240824260"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Practical Art of Motion Picture Sound, 4th ed.",
      "author": "David Yewdall",
      "isbn13": "9780240812403",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Practical Art of Motion Picture Sound, 4th ed. (David Yewdall), ISBN-13 9780240812403"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Mixing Secrets for the Small Studio, 2nd ed.",
      "author": "Mike Senior",
      "isbn13": "9781138556375",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Mixing Secrets for the Small Studio, 2nd ed. (Mike Senior), ISBN-13 9781138556375"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Mastering Audio, 3rd ed.",
      "author": "Bob Katz",
      "isbn13": "9780240818962",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Mastering Audio, 3rd ed. (Bob Katz), ISBN-13 9780240818962"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Audio Post Production for Film and Video",
      "author": "Jay Rose",
      "isbn13": "9780240809700",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Audio Post Production for Film and Video (Jay Rose), ISBN-13 9780240809700"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "现代录音技术",
      "isbn13": "9787115331861",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 现代录音技术，ISBN-13 9787115331861"
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
      "title": "秒懂声音掘金：重塑声音 打造声音IP 声音创副业 AI配音 AI解说",
      "isbn13": "9787122477637",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 秒懂声音掘金：重塑声音 打造声音IP 声音创副业 AI配音 AI解说，ISBN-13 9787122477637"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Sound Effects Bible How to Create and Record Hollywood Style Sound Effects",
      "author": "Viers, Ric",
      "isbn13": "9781932907483",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Sound Effects Bible How to Create and Record Hollywood Style Sound Effects (Viers, Ric), ISBN-13 9781932907483"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Hollywood Soundscapes Film Sound Style, Craft and Production in the Classical Era",
      "author": "Helen Hanson",
      "isbn13": "9781844577279",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Hollywood Soundscapes Film Sound Style, Craft and Production in the Classical Era (Helen Hanson), ISBN-13 9781844577279"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Production Sound Mixing The Art and Craft of Sound Recording for the Moving Image (The…",
      "author": "John J. Murphy",
      "isbn13": "9781501307102",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Production Sound Mixing The Art and Craft of Sound Recording for the Moving Image (The… (John J. Murphy), ISBN-13 9781501307102"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Sound design the expressive power of music， voice and sound effects in cinema eng",
      "isbn13": "9781032592183",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Sound design the expressive power of music， voice and sound effects in cinema eng, ISBN-13 9781032592183"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Sound Design for the Visual Storyteller Creating Sound for Visual Media",
      "author": "Anderson, Christopher D.",
      "isbn13": "9781040332245",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Sound Design for the Visual Storyteller Creating Sound for Visual Media (Anderson, Christopher D.), ISBN-13 9781040332245"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Art of Mixing",
      "author": "David Gibson",
      "isbn13": "9781003655268",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Art of Mixing (David Gibson), ISBN-13 9781003655268"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Mixing Audio",
      "author": "Izhaki, Roey",
      "isbn13": "9781032219448",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Mixing Audio (Izhaki, Roey), ISBN-13 9781032219448"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "电影电视声音创作与录音制作教程",
      "author": "姚国强",
      "isbn13": "9787106032937",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影电视声音创作与录音制作教程（姚国强），ISBN-13 9787106032937"
    }
  ],
  "common_agent_id": "specials.podcast-agent",
  "pack_id": "specials",
  "mapping_status": "related",
  "source_documents": [
    "docs/special_agents_redesign/agents/podcast_agent.md"
  ],
  "source_sha256": "f8a76576bd0b39c7a6aa4935532040d2c451b783804195f4149e1e38be761dd6",
  "configuration_sha256": "4cd649f3291a105509274c087687a1381f14d3b8f72fcce32e056e3c7f3eb21a",
  "destination_commit": "5460c4b4a33c15286f9fd84b1bc764d755f5bab0",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "generated_at": "2026-07-26T14:16:45.966484Z",
  "reviewed_by": "specials-self-contained-reviewer",
  "reviewed_at": "2026-07-26T18:00:00Z",
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\specials\\agents\\specials.podcast-agent",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```
