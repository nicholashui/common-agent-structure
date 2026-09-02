# specials.screenwriter-strategic-goal-achievement-agent — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/specials.screenwriter-strategic-goal-achievement-agent/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "specials.screenwriter-strategic-goal-achievement-agent",
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
      "spagent.screenwriter-strategic-goal-achievement-agent-input"
    ],
    "outputs": [
      "spagent.screenwriter-strategic-goal-achievement-agent-output"
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

# Screenwriter Strategic Goal Achievement Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.screenwriter-strategic-goal-achievement-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain screenwriter strategic goal achievement agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

**Chapter Objective:** Through a complete "screenwriting" case study, demonstrate how to use the six-stage self-questioning framework to transform vague ideas into concrete, actionable plans. **Key Learning Points:**
- How to dig from surface answers to core motivations
- How to convert abstract concepts into specific actions
- How to identify and break through thinking blind spots
- How to establish sustainable execution strategies

### Domain distillation (embedded, untrusted design provenance)

**Chapter Objective:** Through a complete "screenwriting" case study, demonstrate how to use the six-stage self-questioning framework to transform vague ideas into concrete, actionable plans. **Key Learning Points:**
- How to dig from surface answers to core motivations
- How to convert abstract concepts into specific actions
- How to identify and break through thinking blind spots
- How to establish sustainable execution strategies

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
- Local rubric reference: `spagent.screenwriter-strategic-goal-achievement-agent-rubric` (inert identifier).
- Prompt reference: `spagent.screenwriter-strategic-goal-achievement-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.screenwriter-strategic-goal-achievement-agent-input"],"outputs":["spagent.screenwriter-strategic-goal-achievement-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.screenwriter-strategic-goal-achievement-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.screenwriter-strategic-goal-achievement-agent-prompt","rubric_reference":"spagent.screenwriter-strategic-goal-achievement-agent-rubric","critique_edges":{"inputs":["spagent.screenwriter-strategic-goal-achievement-agent-input"],"outputs":["spagent.screenwriter-strategic-goal-achievement-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.screenwriter-strategic-goal-achievement-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/screenwriter_strategic_goal_achievement_agent.md`
- Design source SHA-256 (at generation): `0bea9dd2492e477790853d437dbf68899f98c4128db7ae597ccef23d9af35680`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.

## Prompts

### `prompts/primary.md`

You are a baseline-safe specials pack agent. No network. No production activation.

# Screenwriter Strategic Goal Achievement Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.screenwriter-strategic-goal-achievement-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain screenwriter strategic goal achievement agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

**Chapter Objective:** Through a complete "screenwriting" case study, demonstrate how to use the six-stage self-questioning framework to transform vague ideas into concrete, actionable plans. **Key Learning Points:**
- How to dig from surface answers to core motivations
- How to convert abstract concepts into specific actions
- How to identify and break through thinking blind spots
- How to establish sustainable execution strategies

### Domain distillation (embedded, untrusted design provenance)

**Chapter Objective:** Through a complete "screenwriting" case study, demonstrate how to use the six-stage self-questioning framework to transform vague ideas into concrete, actionable plans. **Key Learning Points:**
- How to dig from surface answers to core motivations
- How to convert abstract concepts into specific actions
- How to identify and break through thinking blind spots
- How to establish sustainable execution strategies

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
- Local rubric reference: `spagent.screenwriter-strategic-goal-achievement-agent-rubric` (inert identifier).
- Prompt reference: `spagent.screenwriter-strategic-goal-achievement-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.screenwriter-strategic-goal-achievement-agent-input"],"outputs":["spagent.screenwriter-strategic-goal-achievement-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.screenwriter-strategic-goal-achievement-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.screenwriter-strategic-goal-achievement-agent-prompt","rubric_reference":"spagent.screenwriter-strategic-goal-achievement-agent-

## Rubrics

### `rubrics/primary.md`

Success: stay inside pack responsibility; no network; no production activation.

## Sources

### `sources/MAPPING.md`

# Source mapping note — `specials.screenwriter-strategic-goal-achievement-agent`

- Mapping status: `related` (specials redesign doc → pack agent)
- Design source (historical): `docs/special_agents_redesign/agents/screenwriter_strategic_goal_achievement_agent.md`
- Source SHA-256: `0bea9dd2492e477790853d437dbf68899f98c4128db7ae597ccef23d9af35680`
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
      "title": "故事",
      "author": "麦基",
      "isbn13": "9787201076942",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 故事（麦基），ISBN-13 9787201076942"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "故事的解剖",
      "author": "繁体麦基",
      "isbn13": "9789862135488",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 故事的解剖（繁体麦基），ISBN-13 9789862135488"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "救猫咪",
      "isbn13": "9787229040727",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 救猫咪，ISBN-13 9787229040727"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "作家之路",
      "author": "佛格勒",
      "isbn13": "9787513320184",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 作家之路（佛格勒），ISBN-13 9787513320184"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "千面英雄",
      "isbn13": "9787532753871",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 千面英雄，ISBN-13 9787532753871"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "电影剧本写作基础",
      "author": "悉德·菲尔德",
      "isbn13": "9787106021238",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影剧本写作基础（悉德·菲尔德），ISBN-13 9787106021238"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "戏剧写作基础",
      "author": "埃格里",
      "isbn13": "9787108014504",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 戏剧写作基础（埃格里），ISBN-13 9787108014504"
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
      "title": "竞争战略",
      "isbn13": "9787508633749",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 竞争战略，ISBN-13 9787508633749"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "好战略，坏战略",
      "isbn13": "9787508643427",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 好战略，坏战略，ISBN-13 9787508643427"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "这就是OKR",
      "isbn13": "9787521702330",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 这就是OKR，ISBN-13 9787521702330"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "创新者的窘境",
      "isbn13": "9787508633336",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 创新者的窘境，ISBN-13 9787508633336"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "系统之美",
      "isbn13": "9787508640114",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 系统之美，ISBN-13 9787508640114"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "第五项修炼",
      "isbn13": "9787508631332",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 第五项修炼，ISBN-13 9787508631332"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "超预测",
      "isbn13": "9787508663098",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 超预测，ISBN-13 9787508663098"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "金字塔原理",
      "isbn13": "9787508633732",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 金字塔原理，ISBN-13 9787508633732"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Making Movies",
      "author": "Sidney Lumet",
      "isbn13": "9780679756606",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Making Movies (Sidney Lumet), ISBN-13 9780679756606"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Film Directing: Shot by Shot",
      "author": "Steven D. Katz",
      "isbn13": "9780941188104",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Film Directing: Shot by Shot (Steven D. Katz), ISBN-13 9780941188104"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "On Directing Film",
      "author": "David Mamet",
      "isbn13": "9780140127225",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: On Directing Film (David Mamet), ISBN-13 9780140127225"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Directing Actors",
      "author": "Judith Weston",
      "isbn13": "9780941188241",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Directing Actors (Judith Weston), ISBN-13 9780941188241"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "On Film-making",
      "author": "Alexander Mackendrick",
      "isbn13": "9780571211258",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: On Film-making (Alexander Mackendrick), ISBN-13 9780571211258"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "A Director Prepares",
      "author": "Anne Bogart",
      "isbn13": "9780415238328",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: A Director Prepares (Anne Bogart), ISBN-13 9780415238328"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Rebel without a Crew",
      "author": "Robert Rodriguez",
      "isbn13": "9780452271876",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Rebel without a Crew (Robert Rodriguez), ISBN-13 9780452271876"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Directing: Film Techniques and Aesthetics, 5th ed.",
      "author": "Michael Rabiger",
      "isbn13": "9780240818450",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Directing: Film Techniques and Aesthetics, 5th ed. (Michael Rabiger), ISBN-13 9780240818450"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Director's Craft",
      "author": "Katie Mitchell",
      "isbn13": "9780415404396",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Director's Craft (Katie Mitchell), ISBN-13 9780415404396"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "拍电影",
      "author": "卢梅",
      "isbn13": "9787106028893",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 拍电影（卢梅），ISBN-13 9787106028893"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "电影镜头设计",
      "author": "卡茨",
      "isbn13": "9787115222224",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影镜头设计（卡茨），ISBN-13 9787115222224"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "导演创作完全手册",
      "author": "拉比格",
      "isbn13": "9787515302867",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 导演创作完全手册（拉比格），ISBN-13 9787515302867"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "AI写作：用AI倍速提升写作效率",
      "author": "邓世超",
      "isbn13": "9787111760146",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: AI写作：用AI倍速提升写作效率（邓世超），ISBN-13 9787111760146"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "如何写出好故事 HBO大师写作课",
      "isbn13": "9787516827482",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 如何写出好故事 HBO大师写作课，ISBN-13 9787516827482"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "给青年编剧的信3.0",
      "author": "宋方金",
      "isbn13": "9787559493965",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 给青年编剧的信3.0（宋方金），ISBN-13 9787559493965"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "编剧的艺术",
      "author": "埃格里",
      "isbn13": "9787550213333",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 编剧的艺术（埃格里），ISBN-13 9787550213333"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "短视频与直播文案写作",
      "author": "张弘李自海魏坚 主编吴曼刘哲李守勤 副主编",
      "isbn13": "9787115638649",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 短视频与直播文案写作（张弘李自海魏坚 主编吴曼刘哲李守勤 副主编），ISBN-13 9787115638649"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "新媒体广告与文案写作(第2版)",
      "author": "周颖 主编张文杰 主编朱晓虹 副主编王娜 副主编黄伟 副主编",
      "isbn13": "9787115648044",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 新媒体广告与文案写作(第2版)（周颖 主编张文杰 主编朱晓虹 副主编王娜 副主编黄伟 副主编），ISBN-13 9787115648044"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "小说的骨架：好提纲成就好故事",
      "author": "[美]凯蒂·维兰德",
      "isbn13": "9787210099529",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 小说的骨架：好提纲成就好故事（[美]凯蒂·维兰德），ISBN-13 9787210099529"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "编剧心理学 在剧本中建构冲突（（美）尹迪克）",
      "isbn13": "9789571161488",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 编剧心理学 在剧本中建构冲突（（美）尹迪克），ISBN-13 9789571161488"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "救猫咪-小说创作指南",
      "isbn13": "9787522513003",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 救猫咪-小说创作指南，ISBN-13 9787522513003"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "救猫咪：电影编剧指南",
      "isbn13": "9787533963361",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 救猫咪：电影编剧指南，ISBN-13 9787533963361"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "人物：文本、舞台、银幕角色与卡司设计的艺术（编剧教父罗伯特·麦基“虚构艺术三部曲”完结篇）",
      "author": "罗伯特·麦基",
      "isbn13": "9787533969585",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 人物：文本、舞台、银幕角色与卡司设计的艺术（编剧教父罗伯特·麦基“虚构艺术三部曲”完结篇）（罗伯特·麦基），ISBN-13 9787533969585"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "救猫咪2经典电影剧本解析",
      "isbn13": "9787533964108",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 救猫咪2经典电影剧本解析，ISBN-13 9787533964108"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "故事的解剖",
      "author": "羅伯特．麥基(Robert McKee)",
      "isbn13": "9787201094601",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 故事的解剖 (羅伯特．麥基(Robert McKee))，ISBN-13 9787201094601"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "對白的解剖",
      "isbn13": "9789864898435",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 對白的解剖，ISBN-13 9789864898435"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "人物的解剖",
      "isbn13": "9789864896257",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 人物的解剖，ISBN-13 9789864896257"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "諾蘭變奏曲",
      "isbn13": "9789863844693",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 諾蘭變奏曲，ISBN-13 9789863844693"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "作家的灵感宝库",
      "isbn13": "9787514220155",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 作家的灵感宝库，ISBN-13 9787514220155"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "发现你的创造力类型",
      "isbn13": "9787210108061",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 发现你的创造力类型，ISBN-13 9787210108061"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "畅销作家写作全技巧",
      "isbn13": "9787210092452",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 畅销作家写作全技巧，ISBN-13 9787210092452"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "小说的八百万种写法",
      "isbn13": "9786263100442",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 小说的八百万种写法，ISBN-13 9786263100442"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "写小说最重要的十件事",
      "isbn13": "9787210108672",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 写小说最重要的十件事，ISBN-13 9787210108672"
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
      "title": "电影编剧学（修订版）",
      "author": "汪流",
      "isbn13": "9787811272406",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影编剧学（修订版）（汪流），ISBN-13 9787811272406"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "实用电影编剧",
      "author": "张觉明",
      "isbn13": "9787106029234",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 实用电影编剧（张觉明），ISBN-13 9787106029234"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "故事片创作六讲",
      "author": "王竞",
      "isbn13": "9787541151323",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 故事片创作六讲（王竞），ISBN-13 9787541151323"
    }
  ],
  "common_agent_id": "specials.screenwriter-strategic-goal-achievement-agent",
  "pack_id": "specials",
  "mapping_status": "related",
  "source_documents": [
    "docs/special_agents_redesign/agents/screenwriter_strategic_goal_achievement_agent.md"
  ],
  "source_sha256": "0bea9dd2492e477790853d437dbf68899f98c4128db7ae597ccef23d9af35680",
  "configuration_sha256": "1916e03d5f023a17ff951202fef2e59b3590c3680ff815fe2458de080e6c6ba2",
  "destination_commit": "5460c4b4a33c15286f9fd84b1bc764d755f5bab0",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "generated_at": "2026-07-26T14:16:45.989751Z",
  "reviewed_by": "specials-self-contained-reviewer",
  "reviewed_at": "2026-07-26T18:00:00Z",
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\specials\\agents\\specials.screenwriter-strategic-goal-achievement-agent",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```
