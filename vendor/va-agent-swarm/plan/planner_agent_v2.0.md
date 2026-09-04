# SIPA — Software Implementation Planner Agent
## Complete Detailed Specification & Design Document

**Version:** 2.0 (Complete & Expanded)  
**Date:** 2026-06-03  
**Status:** Production-Ready Design Spec  
**Owner / Context:** Designed for Nicholas (N1ch01as) ecosystem — integrates with existing AI coding harnesses (Cursor, Kiro, Claude Code, Grok Build, self-hosted OpenWebUI), spec-driven development workflows, critic/refinement loops, and large Markdown corpora RAG practices.  
**Purpose:** A hierarchical, context-engineered, multi-agent system that ingests massive functional specifications + supporting documentation and produces high-fidelity, appropriately-detailed, traceable implementation plans and granular tasks. Explicitly solves context-window limitations by using component-type-adaptive abstraction/detail levels, scoped RAG, hierarchical memory, and embedded quality gates.

This document is the **definitive, exhaustive specification**. It can be used directly as the source-of-truth spec to implement SIPA (or evolve an existing meta-agent system). It incorporates deep research from arXiv papers (MAAD, AgentOrchestra, LLM Multi-Agent SE surveys, etc.), GitHub Spec Kit SDD patterns, xAI Grok Build multi-agent planning/evaluation, context engineering best practices, and alignment with iterative self-refinement / harness engineering principles.

---

## Table of Contents
1. Executive Summary & Problem Statement
2. Research Foundations & Citations (Deep Dive)
3. Design Principles & Core Innovations
4. Component Taxonomy & Adaptive Detailing Strategy
5. Full System Architecture (Hierarchical Multi-Agent)
6. Detailed Agent Roles, Responsibilities, Inputs/Outputs
7. Complete End-to-End Workflow (Phased, with Examples)
8. Data Models, Schemas & Structured Outputs
9. RAG, Context Engineering & Memory Architecture
10. Critic / Evaluator Subsystem (Rubrics, Loops, Quality Gates)
11. Prompt Engineering & Few-Shot Strategies
12. Output Artifact Templates (Full Examples per Type)
13. Implementation Roadmap & Technical Guidance
14. Integration with Existing Tools & Harnesses
15. Metrics, Evaluation & Success Criteria
16. Risks, Mitigations & Edge Cases
17. Future Extensions & Roadmap
18. References & Sources

---

## 1. Executive Summary & Problem Statement

**The Challenge**  
You maintain (or are building from) a very large body of functional specifications, requirements documents, user stories, architecture notes, API contracts, UI descriptions, and related artifacts — often spanning hundreds of Markdown files or equivalent. Directly prompting coding agents with this corpus fails because of:

- Hard context length limits (even 128k–200k+ token models lose coherence or drop critical details in noise).
- **Uniform treatment mismatch**: A high-level architecture plan needs *strategic summarization + decision records + views*. A specific UI screen needs *deep, narrowly-scoped functional excerpts + exhaustive acceptance criteria + flows*. A shared library/component needs *interface contracts + extension points + synthesized common behaviors*. One-size-fits-all summarization destroys value.
- Loss of traceability and intent fidelity (hallucinations, missed cross-references, drift from original specs).
- Inability to scale iterative development or parallel work by multiple coder agents/humans.

**The Solution — SIPA (Software Implementation Planner Agent)**  
SIPA is a **hierarchical multi-agent planner** with:

- Intelligent ingestion & hybrid RAG over the entire corpus (semantic chunking, Knowledge Graph optional, dynamic scoping).
- **Component-type classification** that triggers specialized sub-planners producing *exactly the right abstraction and detail level*.
- Embedded, multi-stage **Critic/Evaluator** with traceability scoring, consistency checks, ATAM-style analysis, and patch-based iterative refinement ("rethink" loops) until quality gates are passed.
- Structured, versioned, git-friendly Markdown outputs (master plans, type-specific implementation specs, granular task lists) that are self-contained and sized for direct consumption by downstream coding agents (Cursor, Kiro, Claude Code, Grok Build, etc.).
- Living-specs philosophy (SDD-aligned): Plans evolve with implementation feedback; full bidirectional traceability.
- Strong alignment with your existing practices: spec-driven development, critic agents, self-refinement, harness engineering, detailed task.md outputs, xAI API / local models, and incremental/ production-ready engineering.

**Key Differentiator**  
Instead of generic decomposition, SIPA uses an explicit **Component Taxonomy** (Architecture/Strategic, Feature/UI/Tactical, Common/Shared/Operational, etc.) to drive fundamentally different retrieval, summarization, synthesis, and output structures. This is the practical realization of your insight that "software development needs different levels of implementation detail."

**Expected Impact**  
- 5–20× reduction in effective context size for coder agents while *increasing* fidelity.
- Higher implementation success rate, fewer rework cycles, preserved intent from massive specs.
- Scalable parallel development + maintainable living documentation.
- A reusable meta-capability you can fold into N1ch01as Architect or similar systems.

---

## 2. Research Foundations & Citations (Deep Dive)

SIPA is not invented from whole cloth — it is a principled synthesis and extension of the best 2025–2026 research and tooling in LLM agents for software engineering, hierarchical planning, requirements-to-architecture, and context engineering.

### 2.1 Spec-Driven Development (SDD) & Structured Agentic Workflows
- **GitHub Spec Kit** (2025, open-sourced): Makes specifications the central, evolving source of truth. Four-phase gated workflow:
  1. **Specify** — High-level intent → detailed "what/why" spec (user journeys, outcomes).
  2. **Plan** — Desired stack, architecture, constraints → technical plan (variations, trade-offs, compliance).
  3. **Tasks** — Break spec + plan into small, isolatable, reviewable chunks (ideal for context windows and safe PRs).
  4. **Implement** — Coder agents execute tasks one-by-one (or parallel) with human checkpoints and refinement.
- Benefits for large/complex projects: Centralizes scattered knowledge, enables safe iteration on legacy or big specs, separates stable intent from flexible "how". SIPA implements and extends the **Plan + Tasks** phases for *pre-existing massive corpora* using RAG and type-aware detailing.
- Related: Kiro (spec-first with requirements/design/tasks MDs), Tessl (spec as single source of truth that generates code), DeepLearning.AI course on SDD with coding agents (Paul Everitt / JetBrains).
- Alignment: SIPA outputs are designed to be consumed exactly like Spec Kit artifacts.

### 2.2 Hierarchical Multi-Agent Systems & Planning
- **AgentOrchestra** (arXiv:2506.12508, 2025): Hierarchical framework with top-level Planning Agent that explicitly decomposes complex objectives into sub-goals, maintains dynamic plans, and delegates to specialized modular sub-agents (Deep Researcher, Browser Use, Deep Analyzer, etc.). Uses standardized interfaces for collaboration. Emphasizes extensibility and multimodality. SIPA adopts the top-planner + specialized sub-planners pattern and explicit sub-goal formulation.
- **Self-Organized Agents (SoA)**: Mother agents manage high-level abstractions and delegate to Child agents for detailed subtasks (hierarchical decomposition in ultra-large-scale code generation).
- **GoalAct** (arXiv:2504.16563): Introduces continuously updated global planning + hierarchical execution (high-level skills → tool selection → detailed refinement). Improves success rates significantly on complex tasks.
- **ALMAS** (Autonomous LLM-based Multi-Agent Software Engineer): Sprint/Planner agents break high-level tasks into stories with acceptance criteria, effort estimates, and stepwise plans. Mirrors agile team roles.
- **HPTSA** and similar hierarchical planning + task-specific agent systems: Used successfully for complex, long-horizon tasks where single agents fail due to context.

### 2.3 Requirements Engineering → Architecture (MAAD — Most Directly Influential)
- **MAAD** (Multi-Agent Architecture Design, arXiv:2606.01385, 2026): State-of-the-art framework that transforms Software Requirements Specifications (SRS) into comprehensive, traceable, multi-view architectural blueprints with integrated quality assessment.
  - **Four specialized agents**:
    - **Analyst**: Parses SRS → extracts & structures FRs, NFRs, Architecturally Significant Requirements (ASRs). Classifies and annotates traceability.
    - **Modeler**: Maps requirements to “4+1” architectural views (Kruchten). Generates PlantUML/UML diagrams. Uses RAG to retrieve patterns, tactics, and standards.
    - **Designer**: Synthesizes production-ready documentation (traceability matrices, API specs, deployment configs, rationale, trade-off analysis).
    - **Evaluator (Critic)**: Embedded at every stage — validates completeness, consistency (cross-view), syntax, anti-patterns. Performs system-level ATAM (Architecture Tradeoff Analysis Method) evaluation and produces mismatch reports with severity + remediation suggestions. Triggers iterative patch-based refinement.
  - **Hierarchical Memory**: Working (current artifacts + feedback), Episodic (task/iteration history with lessons), Semantic (generalized patterns, principles, rationale with metadata for retrieval).
  - **RAG Integration**: External knowledge base (ISO/IEC 42010, Bass et al. architecture literature, patterns) injected to reduce hallucinations and enforce rigor (layering, stereotypes, separation of concerns).
  - **Results**: Outperforms MetaGPT on modularity, traceability, completeness. Practitioners found artifacts "well-structured" and effort-reducing. RAG measurably improves pattern justification and standard compliance.
- SIPA directly adapts the MAAD pipeline (Analyst-Modeler-Designer-Evaluator) for the **Architecture** sub-planner and generalizes the critic + memory + RAG pattern across all component types.

### 2.4 Broader LLM Multi-Agent Systems for Software Engineering
- Survey **LLM-Based Multi-Agent Systems for Software Engineering** (arXiv:2404.04834v4, 2025): Comprehensive review across SDLC phases. Notes hierarchical designs (Mother/Child), role specialization (PM/Architect/Engineer/QA), iterative feedback, memory components, and RAG/knowledge graphs for large repositories. Highlights MARE (requirements phases), MetaGPT (waterfall roles), ChatDev, Think-on-Process (dynamic process generation), etc.
- Other notable: MASAI (modular architecture for SE AI agents), SWE-Search (Monte Carlo Tree Search + iterative refinement), RepoSketcher / CodexGraph (graph-based understanding of large codebases — principles apply to specs).

### 2.5 Context Engineering, RAG & Large Corpus Handling
- Modern agent literature emphasizes moving beyond naive RAG to **Context Engineering**: dynamic write/select/compress/isolate strategies.
  - Semantic chunking (by logical boundaries: features, sections, requirement IDs) + hybrid retrieval (vector + BM25 + graph).
  - Compression/summarization of retrieved passages before assembly.
  - Schema enforcement, metadata injection, structured prompts.
  - Hierarchical indices and memory (working/episodic/semantic) to maintain coherence across long-running planning sessions.
- Papers on code agents (SWE-agent harnesses, context persistence) show that focused, scoped retrieval dramatically outperforms dumping entire large contexts.
- SIPA treats the spec corpus exactly like a large codebase: intelligent indexing, dependency-aware retrieval, and per-task context isolation.

### 2.6 xAI / Grok Build Inspiration (2026)
- **Grok Build** (xAI beta, available via xAI API / SuperGrok Heavy): New coding agent focused on professional software engineering. Uses **multi-agent orchestration** (up to 8 parallel agents) with explicit **plan → search → build** workflow. Includes **Arena Mode** (automated evaluation and ranking of competing outputs before human review). Strong emphasis on planning complex tasks, terminal/CLI integration, and local-first design. SIPA’s planner outputs are designed to feed directly into Grok Build (or complement it), and the critic/evaluation patterns draw from Arena-style automated scoring.

These foundations are not copied — they are synthesized, extended with the component-type adaptive detailing insight, and engineered for your specific constraints (very large existing spec corpora, different detail needs, production harness integration, critic-driven quality).

---

## 3. Design Principles & Core Innovations

1. **Hierarchical Decomposition + Type-Aware Specialization**  
   Top-level Orchestrator performs project-level decomposition and component classification. Specialized sub-planners then apply fundamentally different strategies based on component type.

2. **Context Engineering as First-Class Citizen**  
   Scoped retrieval, targeted summarization/compression, hierarchical memory, and isolation ensure every artifact uses the smallest possible high-signal context. Never the full corpus.

3. **Component-Type Taxonomy Drives Everything** (Core Innovation)  
   Explicit classification triggers different retrieval depth, summarization style, synthesis focus, and output structure. This is what makes SIPA uniquely effective for real software development.

4. **Embedded Critic with Quality Gates & Iterative Refinement**  
   No artifact is final until it passes multi-dimensional automated + structured checks (traceability, consistency, completeness, implementability, anti-patterns). Patch-based refinement + memory update creates "rethink" loops. Aligns with your preference for critic agents and self-improvement.

5. **Living Specs & Full Traceability (SDD-Aligned)**  
   Every claim/decision in a plan links back to source sections in the original corpus. Plans are versioned Markdown. Implementation feedback flows back to update plans and memory. Specs become executable, evolving artifacts.

6. **Production-Ready Engineering**  
   Structured outputs (YAML frontmatter + consistent sections), deterministic elements where possible, error handling, logging of reasoning traces, incremental operation, git-friendly artifacts, human-in-the-loop gates on strategic artifacts.

7. **Harness-Native Outputs**  
   Master plans, type-specific specs, and task lists are designed to be dropped directly into your existing workflows (task.md consumption by Cursor/Kiro/Claude/Grok Build, AGENTS.md rules, etc.).

8. **Self-Improving & Extensible**  
   Meta-reflection on planner performance, prompt/template evolution, and easy addition of new component types or sub-planners.

---

## 4. Component Taxonomy & Adaptive Detailing Strategy

SIPA maintains an explicit, extensible taxonomy. The Master Orchestrator (or a dedicated Classifier sub-agent) assigns each module/component a primary type (and optional secondary tags). This drives retrieval strategy, sub-planner selection, and output schema.

### Primary Types & Detailing Rules

| Type                  | Abstraction Level | Retrieval Strategy                          | Summarization Focus                     | Output Emphasis                              | Example Components                     |
|-----------------------|-------------------|---------------------------------------------|-----------------------------------------|----------------------------------------------|----------------------------------------|
| **Architecture / Strategic** | High (Strategic Overview) | Broad corpus scan for cross-cutting concerns + ASRs; RAG for patterns/standards | Global synthesis + key decisions; condense non-essential narrative | Views (textual/Mermaid), ADRs, interfaces, quality attributes, rationale, tech choices | System/subsystem architecture, major services, deployment topology, cross-cutting frameworks |
| **Feature / UI / Tactical** | Medium-High (Detailed but Scoped) | Narrow semantic search on feature name + related req IDs + UI mentions; pull full relevant paragraphs | Minimal global context; deep local detail | User stories, exhaustive acceptance criteria, flows/state machines, API contracts, edge cases, validation | Individual screens, user journeys, bounded-context features, specific endpoints with UI |
| **Common / Shared Component / Operational** | Medium (Interface & Reusability Focused) | Search for interface definitions, usage patterns, config, cross-module references | Synthesize common behaviors + extension points; de-emphasize end-user narrative | Public contracts (types/methods/events), config schemas, invariants, extension hooks, error/perf strategy, usage examples | Auth service, notification lib, shared domain models, utils, caching layer, logging facade |
| **Data / Domain Model** | Medium            | Focused on entity definitions, relationships, invariants across specs | Entity-relationship synthesis + lifecycle rules | Schema (conceptual/logical), invariants, evolution/migration notes, query patterns | Core entities, aggregates, value objects |
| **Integration / External** | Medium            | API contracts, event schemas, third-party specs | Contract + error/compatibility focus   | Interface specs, mapping rules, retry/idempotency, monitoring | Third-party integrations, event buses, legacy system adapters |
| **Infrastructure / DevOps** | High              | Non-functional + deployment/ops requirements | Summary of constraints + patterns      | Deployment views, IaC considerations, observability, scaling strategies | CI/CD pipelines, containerization, monitoring stacks |

**Secondary Tags** (orthogonal): Security-critical, Performance-sensitive, High-availability, User-facing, Internal-only, Legacy-modernization, etc. These influence critic rubrics and extra sections.

**Classification Heuristics** (implemented via LLM classifier + rules):
- Keywords/phrases: "architecture decision", "system overview", "deployment", "C4 model", "4+1 views" → Architecture.
- "UI screen", "user flow", "acceptance criteria for [feature]", "mockup", "Figma" → Feature/UI.
- "shared", "common", "library", "util", "service interface", "public API", "extension point" → Common/Shared.
- Presence of class/entity diagrams, "domain model", "aggregate root" → Data/Domain.
- Explicit requirement IDs or section references in master plan.

The taxonomy is versioned and can be extended (new types inherit a base template and override retrieval/synthesis/output rules).

---

## 5. Full System Architecture (Hierarchical Multi-Agent)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                              Master Orchestrator / Meta-Planner                               │
│  • High-level goal + corpus index intake                                                      │
│  • Project decomposition into phases/epics/modules                                            │
│  • Component classification (taxonomy) + dependency graph construction                        │
│  • Master roadmap / plan generation (with effort/priority/risk estimates)                     │
│  • Spawns & coordinates specialized sub-planners; manages global state & memory               │
│  • High-level critic pass + human gate (optional)                                             │
│  Tools: Hybrid RAG retriever, classifier, graph builder, summarizer, structured output        │
└───────────────────────────────────────┬────────────────────────────────────────────────────────┘
                                        │ delegates (type-aware)
          ┌─────────────────────────────┼─────────────────────────────┐
          ▼                             ▼                             ▼
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│ Architecture        │     │ Feature/UI          │     │ Common/Shared       │
│ Sub-Planner         │     │ Sub-Planner         │     │ Component           │
│ (MAAD-inspired)     │     │ (SDD Task-style)    │     │ Sub-Planner         │
│                     │     │                     │     │ (Interface-focused) │
│ - Analyst           │     │ - Deep scoped       │     │ - Contract          │
│ - Modeler (views)   │     │   retrieval         │     │   synthesizer       │
│ - Designer (docs)   │     │ - Story/acceptance  │     │ - Config &          │
│                     │     │   expansion         │     │   extension points  │
│ + RAG patterns      │     │ - Flow/state gen    │     │ - Usage examples    │
└──────────┬──────────┘     └──────────┬──────────┘     └──────────┬──────────┘
           │                           │                           │
           └───────────────────────────┼───────────────────────────┘
                                       ▼
                            ┌──────────────────────────┐
                            │   Evaluator / Critic     │
                            │   (Multi-stage, embedded)│
                            │   • Traceability scorer  │
                            │   • Consistency checker  │
                            │   • Completeness vs ASR  │
                            │   • Anti-pattern detect  │
                            │   • ATAM / mismatch      │
                            │   • Patch refinement     │
                            │   • Quality gate         │
                            └───────────┬──────────────┘
                                        │ feedback (loop until pass)
                                        ▼
                            ┌──────────────────────────┐
                            │ Task Decomposer /        │
                            │ Granular Task Generator  │
                            │ • Small, reviewable      │
                            │   units for coder agents │
                            │ • Acceptance criteria    │
                            │ • Context excerpts       │
                            │ • Sequencing & deps      │
                            └──────────────────────────┘
```

**Supporting Infrastructure (shared services)**:
- **Corpus Indexer & RAG Engine** (LlamaIndex/Haystack or custom): Semantic chunking, embeddings, hybrid search (vector + keyword + optional Knowledge Graph), passage compression, metadata tagging (requirement IDs, component tags, section paths).
- **Hierarchical Memory Manager**:
  - Working Memory: Current artifacts, feedback, active context packages.
  - Episodic Memory: Per-module/iteration history, decisions, refinement traces, lessons learned.
  - Semantic Memory: Generalized patterns, glossary, cross-cutting principles, reusable rationales (vector + structured metadata for retrieval).
- **Knowledge Graph (optional but recommended)**: Nodes = requirements, components, decisions; Edges = traces_to, depends_on, refines, conflicts_with, implements. Enables impact analysis and richer retrieval.
- **Structured Output Enforcer**: Pydantic models / JSON mode + validation. All agents produce typed artifacts.
- **Tooling Layer**: File system access (read specs, write plans), code execution (Mermaid/PlantUML rendering, contract validation stubs), diagram generation, optional vision for UI mocks.

**Orchestration Style**: Stateful graph (LangGraph-style) or role-based crew with explicit handoff protocols. Supports parallel execution of independent sub-planners. Dynamic replanning on significant feedback.

---

## 6. Detailed Agent Roles, Responsibilities, Inputs/Outputs

### 6.1 Master Orchestrator / Meta-Planner
**Responsibilities**:
- Ingest high-level goal + indexed corpus.
- Decompose into phases, epics, modules; build dependency graph.
- Classify components using taxonomy + heuristics/LLM.
- Generate master roadmap/plan (high-level summaries, priorities, risks, effort estimates).
- Coordinate sub-planners, manage global memory & traceability matrix.
- High-level consistency & completeness critic pass.
- Human review gate on strategic artifacts.

**Inputs**: High-level project prompt/goal, corpus index + summaries, optional existing partial plans.
**Outputs**: `master_plan.md` (or `project_roadmap.md`), dependency graph (Mermaid), initial traceability skeleton, classified module list, spawn commands for sub-planners.
**Prompt Style**: "You are an expert software program manager and architect. Decompose the following project... Classify each module according to the taxonomy... Prioritize for MVP... Output in strict structured format."

### 6.2 Architecture Sub-Planner (MAAD-inspired)
**Responsibilities**:
- Analyst phase: Extract/validate FRs/NFRs/ASRs relevant to the architectural scope; ensure traceability.
- Modeler phase: Generate multi-view architecture (logical, process, development, physical/scenario) using textual/Mermaid/PlantUML. Retrieve patterns via RAG.
- Designer phase: Synthesize documentation — rationale, interfaces/contracts, deployment considerations, trade-off analysis.
- Collaborate with Critic at each sub-stage.

**Inputs**: Scoped corpus excerpts for the architectural boundary + master plan context + RAG knowledge base (patterns, standards).
**Outputs**: `architecture_<module>.md` with YAML frontmatter + sections for overview, views, decisions (ADRs), interfaces, quality attributes, deployment, rationale.
**Special Tools**: RAG for architecture knowledge; diagram generation.

### 6.3 Feature/UI Sub-Planner (SDD Task-style)
**Responsibilities**:
- Perform deep, narrow retrieval on the specific feature/UI.
- Refine/expand user stories and acceptance criteria from source material.
- Synthesize interaction flows, state machines, UI behaviors.
- Extract or generate precise API contracts, payloads, validation rules, error/edge cases.
- Keep global context minimal; focus on "this screen/feature in detail."

**Inputs**: Highly targeted retrieval results (feature name + related req IDs + UI/acceptance mentions) + master plan + any linked architecture contracts.
**Outputs**: `feature_spec_<name>.md` — rich, detailed, scoped functional spec ready for implementation.
**Special**: Strong emphasis on exhaustive acceptance criteria (checklist or Gherkin) that can be directly turned into tests.

### 6.4 Common/Shared Component Sub-Planner
**Responsibilities**:
- Synthesize interface contracts, types, methods/events from scattered mentions across the corpus.
- Define configuration points and defaults.
- Identify and document extension points, hooks, plugin mechanisms.
- Capture invariants, guarantees, error handling strategy, performance considerations.
- Provide usage examples and testability notes.
- Focus on reusability and maintainability rather than end-user narrative.

**Inputs**: Retrieval across interface definitions, usage patterns, config requirements, cross-module references.
**Outputs**: `component_spec_<name>.md` — contract-first, extension-oriented specification.
**Special**: Often the most "synthesized" type; requires good aggregation across many source fragments.

### 6.5 Evaluator / Critic (Embedded, Multi-Stage)
**Responsibilities**:
- Traceability scoring (every major element links to source section(s) with evidence).
- Consistency checking (intra-plan, inter-plan with master/other modules, no contradictions).
- Completeness vs. relevant ASRs/NFRs from corpus.
- Anti-pattern detection (God object, tight coupling, missing edge cases, unclear contracts, etc.).
- Quality attribute / tradeoff analysis (ATAM-inspired) where relevant.
- Structured feedback + severity + suggested patches.
- Gate decision (pass / refine / escalate to human).

**Inputs**: Draft plan artifact + source excerpts used + memory of prior decisions + rubric.
**Outputs**: Structured critique (JSON + natural language) + patch suggestions or approval.
**Implementation**: Can be a single powerful LLM with rubric + tools, or a small crew of specialized critics (traceability critic, consistency critic, etc.). Uses LLM-as-judge with calibrated rubrics + rule-based checks.

### 6.6 Task Decomposer / Granular Task Generator
**Responsibilities**:
- Break validated plans into small, focused, reviewable tasks sized for coder agents (one context window, one logical change, clear acceptance criteria).
- Embed or link relevant excerpts from the parent plan/spec.
- Sequence tasks, note dependencies, suggest tests or review focus.
- Produce task lists that can be consumed directly (e.g., `tasks_<module>.md` or individual task cards).

**Inputs**: Validated type-specific plan(s) + master dependencies.
**Outputs**: Prioritized, sequenced task lists with full context for execution.

---

## 7. Complete End-to-End Workflow (Phased, with Examples)

### Phase 0: Ingestion & Indexing (Incremental-friendly)
1. Scan spec directory + related docs.
2. Intelligent chunking (heading hierarchy, requirement ID tags if present, semantic boundaries, feature/component mentions).
3. Embed + store with rich metadata (file path, section, requirement IDs, component tags, last modified).
4. Optional: Extract entities/relationships → build/update Knowledge Graph.
5. Generate/update corpus-level summaries, glossary, and initial component candidate list.
6. Output: Searchable index + `corpus_index.md` / `glossary.md`.

**Tools**: LlamaIndex/Haystack pipelines or custom scripts. Run on change detection (git hooks or watcher).

### Phase 1: High-Level Decomposition & Master Plan
1. Master Orchestrator receives high-level goal + index.
2. Decomposes project; classifies modules; builds dependency/risk view.
3. Generates `master_plan.md` (epics/phases, high-level summaries per module, priorities, critical path, initial traceability matrix skeleton).
4. Critic pass on master plan.
5. Optional human review gate.
6. Spawns sub-planners for priority modules (parallel where independent).

**Example Master Plan Excerpt** (abbreviated):
```markdown
---
type: master_plan
version: 1.0
---
# Project Roadmap — DeepTutor HKDSE xAI Edition (Example)

## Phases
### Phase 1: Core Domain & Auth (MVP Foundation)
- Architecture: [architecture_core_domain.md] (Strategic)
- Common: Auth Service, User Domain Model
- Features: Login/Register flows

### Phase 2: UI Features (Student/Teacher Dashboards)
- Feature: Student Profile Screen (Tactical)
- ...

## Dependencies
Core Domain → Auth Service → All UI features
...
```

### Phase 2: Scoped Type-Aware Planning + Critic Loops (Core Loop)
For each module in priority order (or parallel):

1. **Context Assembly**:
   - Classifier confirms type.
   - Hybrid retrieval with type-specific query strategy + compression.
   - Assemble minimal context package + memory retrieval (episodic/semantic relevant to this module).

2. **Sub-Planner Execution** (type-specific template + few-shot):
   - Architecture: Analyst → Modeler (RAG patterns) → Designer.
   - Feature/UI: Deep retrieval → story/acceptance expansion → flow/state/API synthesis.
   - Common: Interface aggregation → contract definition → extension/config synthesis.

3. **Embedded Critic Stages** (can run after each sub-stage or at end):
   - Traceability check (LLM + link validator).
   - Consistency (with master + sibling plans).
   - Completeness & anti-patterns.
   - Structured feedback JSON.
   - If below gate: Sub-planner receives patch instructions + memory → re-runs targeted sections only.

4. **Version & Persist**:
   - Write `architecture_<name>.md` / `feature_spec_<name>.md` / `component_spec_<name>.md` with full frontmatter + traceability.
   - Update global traceability matrix and episodic memory.

**Example Interaction Trace** (simplified for Architecture):
- Draft generated.
- Critic: "Traceability for 'event-driven notifications' only links to one section; missing NFR-089 on reliability. Also, deployment view lacks observability tactics from standard patterns."
- Patch instruction: "Add explicit link to NFR-089 and retrieve observability patterns via RAG; update deployment view section with 2-3 bullet tactics."
- Refined draft passes gate.

### Phase 3: Granular Task Generation
- Task Decomposer consumes validated plans.
- Produces `tasks_<module>.md` (or per-epic task boards) with:
  - Small units (e.g., "Implement UserProfileHeader component following feature_spec_user_profile.md sections 3.2–3.4 and contracts in architecture_user_domain.md").
  - Embedded relevant excerpts or precise links + line references.
  - Clear acceptance criteria (directly from plan).
  - Suggested tests, review focus, complexity.
- Sequenced and dependency-aware.

**Example Task**:
```markdown
- [ ] Task UI-042: Build StudentDashboardHeader component
  **From**: feature_spec_student_dashboard.md v1.3 (sections 2.1, 4.3) + architecture_core_ui.md contracts
  **Acceptance**:
  - Renders user avatar + notification bell per spec 2.1
  - Clicking avatar opens dropdown with profile/logout (state managed locally, no extra API call)
  - Responsive on mobile (Tailwind breakpoints)
  **Context Excerpt**: [paste or link key paragraphs]
  **Suggested Tests**: Unit for rendering states; E2E for dropdown interaction
```

### Phase 4: Implementation, Feedback & Living Update
- Tasks + plans fed to coder agents (your harness, Grok Build plan-search-build + Arena eval, parallel workers, etc.).
- Capture outcomes (diffs, test results, review comments, runtime issues, "this plan was unclear on X").
- Feed back into SIPA:
  - Update episodic memory with outcome.
  - Trigger targeted re-planning or patch on affected plans (e.g., "API response shape changed → update related UI plans and common contracts").
  - Evolve semantic memory (new patterns discovered during implementation).
- Re-run critic on changed artifacts.
- Maintain living traceability.

**Incremental Mode**: On new spec additions or changes, detect affected modules via graph/index and re-plan only those (with diff highlighting).

---

## 8. Data Models, Schemas & Structured Outputs

All artifacts use consistent YAML frontmatter + Markdown sections. Enforced via Pydantic or equivalent.

**Core Frontmatter Schema** (example):
```yaml
---
type: master_plan | architecture | feature_ui | common_component | task_list | critique
component: string
abstraction_level: strategic | tactical | operational
version: string (semver)
traceability: list of "file.md#section-or-anchor" or "req-ID"
dependencies: list of component names
critic_score: float (0-1)
last_refined: ISO date
status: draft | in_review | approved | implemented
tags: list (security-critical, etc.)
---
```

**Full Output Schemas** (high-level):
- Master Plan: Roadmap sections, phase breakdowns, module inventory with types, dependency graph, risk register, initial traceability matrix.
- Architecture Spec: Executive summary, Mermaid views (logical/component, deployment, etc.), ADR list, interface catalog, quality attribute scenarios, deployment/IaC notes, rationale.
- Feature/UI Spec: Refined user stories, exhaustive acceptance criteria (checklist or Gherkin), interaction flows (numbered or state diagram), UI state & behavior, API contracts (request/response examples), validation & error matrix, non-functional notes, wireframe prompts.
- Common Component Spec: Purpose & scope, public interface (code-like or table), configuration schema (YAML/JSON), extension points & hooks, invariants & guarantees, error handling strategy, performance considerations, usage examples, testability notes, migration notes.
- Task List: Prioritized/sequenced tasks with acceptance criteria, context excerpts/links, suggested tests, complexity, owner hints.
- Critique: Structured JSON (traceability_score, consistency_issues, completeness_gaps, anti_patterns, suggested_patches, overall_verdict, confidence).

All outputs are designed to be both human-readable and machine-consumable (for downstream agents or tooling).

---

## 9. RAG, Context Engineering & Memory Architecture

**Ingestion / Chunking Strategy**:
- Primary: Heading hierarchy + semantic boundaries (feature, requirement block, component description).
- Secondary: Requirement ID extraction (regex or LLM), component mention tagging.
- Metadata per chunk: file, section path, requirement IDs, component tags, last_modified, embedding.

**Retrieval (Hybrid + Type-Aware)**:
- Vector similarity (dense embeddings).
- Keyword / BM25 for exact IDs or technical terms.
- Optional Knowledge Graph traversal (e.g., "find all requirements that trace to this component or depend on it").
- Re-ranking + compression (LLM summarizer or extractive) of top-k passages before assembly.
- Type-specific query expansion (e.g., for Architecture: add "ASR NFR pattern tactic"; for UI: add "acceptance criteria flow edge case").

**Context Assembly**:
- Minimal sufficient package: Retrieved passages + compressed summary + relevant memory (episodic decisions for this module, semantic patterns) + master plan excerpts.
- Isolation: Each sub-planner invocation gets its own focused context; global context only where explicitly needed (cross-cutting).

**Hierarchical Memory**:
- **Working**: Current draft artifacts, active retrieval results, critic feedback in flight.
- **Episodic**: Structured records of planning sessions per module (inputs used, decisions made, refinement history, outcome if implemented). Enables "what changed since last version?"
- **Semantic**: Generalized, retrievable knowledge — architecture patterns that worked, common pitfalls in this domain, glossary, cross-cutting principles, reusable rationale snippets. Stored with metadata for precise retrieval.

**Knowledge Graph (Recommended)**:
- Nodes: Individual requirements, components, decisions, plans.
- Edges: traces_to (requirement → plan element), depends_on, refines, conflicts_with, implements (plan → code later).
- Benefits: Impact analysis ("changing this requirement affects which plans?"), richer retrieval, visualization for humans.

---

## 10. Critic / Evaluator Subsystem (Rubrics, Loops, Quality Gates)

**Multi-Stage Critic** (can be parallel or sequential):
1. **Traceability Critic**: For every major claim/decision/view/API, does it have explicit link(s) to source section(s) with evidence? Score + missing list.
2. **Consistency Critic**: Intra-plan (no internal contradictions), inter-plan (aligns with master and sibling modules), temporal (consistent with prior versions unless justified change).
3. **Completeness Critic**: Covers all relevant ASRs/NFRs from corpus for this scope? Missing user stories/edge cases? 
4. **Anti-Pattern & Quality Critic**: God object, tight coupling, missing error handling, unclear extension points, insufficient acceptance criteria, etc. Uses RAG knowledge of good patterns.
5. **Implementability / Sizing Critic**: Is the plan scoped such that tasks will fit coder context windows? Are acceptance criteria testable? Any obvious blockers?
6. **ATAM / Tradeoff Critic** (Architecture-heavy): Identifies quality attribute scenarios, trade-offs, risks; produces lightweight mismatch or risk register.

**Feedback Format** (structured for patch application):
```json
{
  "overall_verdict": "pass | refine | escalate",
  "traceability_score": 0.87,
  "issues": [
    {"severity": "high", "category": "traceability", "description": "...", "suggested_patch": "Add link to spec_v2.md#FR-112 and quote relevant sentence..."}
  ],
  "strengths": [...],
  "recommended_next_action": "..."
}
```

**Refinement Loop**:
- Critic feedback → Sub-planner receives it + relevant memory + instruction to apply minimal targeted patches only.
- Re-generate affected sections.
- Re-critic (can be limited to changed parts for efficiency).
- Converge when gate passed (configurable thresholds, e.g., traceability ≥ 0.90, no high-severity issues) or human override.

**Gate Examples**:
- Architecture: Must have at least 3 views + 2+ ADRs with rationale + traceability to major ASRs.
- Feature/UI: Every user story has ≥3 acceptance criteria covering happy path + at least 2 edge/error cases; all referenced APIs/contracts exist in linked architecture plans.
- Common: Public interface fully specified (signatures + semantics); at least one extension point documented; usage example present.

---

## 11. Prompt Engineering & Few-Shot Strategies

**System Prompts** (role + principles + taxonomy + output schema):
- "You are an expert senior software architect / product owner / interface designer specializing in [type]. You follow strict traceability, produce only the requested abstraction level, and never hallucinate details not supported by provided context or retrieved sources. Always output in the exact structured Markdown + YAML frontmatter format..."

**Chain-of-Thought / "Rethink" Instructions**:
- Built into every agent: "Before producing the final output, internally critique your draft against the rubric: traceability, consistency with provided context and master plan, completeness for this component type, absence of anti-patterns. Then apply improvements."

**Few-Shot Examples**:
- Curate 2–4 high-quality examples per component type (from your past successful plans or synthetic gold-standard ones).
- Include full input context snippet + expected output.
- Place in prompt or retrieve dynamically via semantic memory ("similar past planning tasks").

**Structured Output Enforcement**:
- Use Pydantic / instructor library or native JSON mode + post-validation.
- For Markdown-heavy outputs: Generate JSON structure first, then render to Markdown template (more reliable).

**Temperature & Sampling**:
- Planning / synthesis: 0.3–0.7 (creativity balanced with fidelity).
- Critic / evaluation: 0.0–0.2 (deterministic, consistent scoring).
- Refinement patches: Low temperature.

**xAI Grok / Strong Reasoning Models**:
- Use for Master Orchestrator, Architecture sub-planner, and top-level Critic (best reasoning for complex decomposition and tradeoff analysis).
- Lighter/faster models for retrieval, simple classification, or high-volume task decomposition.

---

## 12. Output Artifact Templates (Full Examples per Type)

(See the previous `software_implementation_planner_agent.md` for concrete abbreviated examples. In a full implementation, maintain a `templates/` directory with complete skeletons that agents fill.)

Key sections that appear across types (customized):
- YAML frontmatter (as above)
- Executive / Purpose summary (tailored length & focus)
- Traceability & Source References
- Detailed body (views for arch, acceptance criteria + flows for UI, contracts + extension points for common)
- Dependencies & Risks
- Open Questions / Assumptions (for human review)
- Changelog / Refinement History (auto-appended)

Full templates should be version-controlled alongside SIPA.

---

## 13. Implementation Roadmap & Technical Guidance

**Phase 1 (MVP — 1–2 weeks)**:
- Corpus indexer + basic hybrid RAG (LlamaIndex or simple embeddings + keyword).
- Master Orchestrator (decomposition + classification) + one sub-planner (start with Feature/UI or Architecture).
- Basic Critic (traceability + consistency) with simple loop.
- Structured output + file writer.
- Test end-to-end on a small bounded module from your specs.
- Integrate output consumption into one existing coder workflow (e.g., feed tasks to Cursor or Grok Build).

**Phase 2 (Core Completeness)**:
- Add all primary sub-planners + full taxonomy.
- Hierarchical memory (working + episodic + semantic).
- Advanced critic (all stages, patch application, ATAM-lite for architecture).
- Knowledge Graph (lightweight, e.g., NetworkX + LLM extraction or simple edges).
- Incremental mode + change detection.
- Full template library + few-shot examples.

**Phase 3 (Production Hardening)**:
- Observability (reasoning traces, retrieval logs, critic scores over time).
- Human-in-the-loop UI or CLI gates (review master plan, high-risk plans).
- Cost/token optimization (caching, model routing, compression).
- Parallel execution, retry logic, error handling.
- Metrics dashboard (traceability scores, refinement iterations, downstream task success rate).
- Packaging as reusable agent/harness component (Docker or Python package).

**Tech Stack Recommendations** (matching your environment):
- **Orchestration**: LangGraph (excellent for stateful hierarchical graphs + loops) or custom with your existing patterns. CrewAI/AutoGen as alternative for role-based.
- **RAG/Memory**: LlamaIndex (advanced indexing, hierarchical, graph capabilities) or Haystack. Chroma/Weaviate/Pinecone local. Optional Neo4j or in-memory graph for Knowledge Graph.
- **LLMs**: xAI Grok (primary for planning/critique — strong reasoning). DeepSeek / Qwen / local models for volume or cost. Grok Build where the plan-search-build + Arena evaluation adds value.
- **Structured Outputs**: Pydantic + instructor or native tool-calling/JSON mode.
- **Diagrams**: Mermaid (native in Markdown) + optional code execution for PlantUML or validation.
- **Storage**: Git repo for all plans/artifacts (versioning, diffing, collaboration). Optional vector DB persistence.
- **Integration**: File watchers or CLI commands that output to `plans/` and `tasks/` directories consumable by your harness. Expose as MCP/tool or simple API if needed for multi-agent setups.

**Code Structure Sketch** (high-level):
```
sipa/
├── indexer/          # corpus ingestion, chunking, embedding, graph
├── agents/
│   ├── orchestrator.py
│   ├── architecture_planner.py   # contains Analyst/Modeler/Designer logic
│   ├── feature_ui_planner.py
│   ├── common_component_planner.py
│   ├── critic.py                 # multi-stage or specialized critics
│   └── task_decomposer.py
├── memory/           # working, episodic, semantic managers
├── rag/              # hybrid retriever, compressors, type-specific strategies
├── schemas/          # Pydantic models for all artifacts
├── templates/        # Markdown skeletons + few-shot examples
├── prompts/          # system prompts, few-shot libraries
├── utils/            # diagram gen, traceability validator, patch applier
└── main.py / cli.py  # entrypoints, incremental runner
```

Start with a notebook or single-file prototype for rapid iteration, then refactor into the package.

---

## 14. Integration with Existing Tools & Harnesses

- **Input**: Point SIPA at your existing large spec folder (or a curated index file). It respects `.gitignore` or explicit include/exclude lists.
- **Output Consumption**:
  - Drop `master_plan.md`, type-specific specs, and `tasks_*.md` into your project repo.
  - Coder agents (Cursor, Kiro, Claude Code, Grok Build) consume them exactly as they would Spec Kit artifacts or your hand-written task.md files.
  - Generate or update `AGENTS.md` / Cursor rules per module with relevant excerpts or instructions derived from plans.
- **Feedback Loop**: Parse coder agent session logs, test results, or PR comments → feed structured outcomes back to SIPA (simple script or manual paste into episodic memory).
- **Grok Build Synergy**: Use SIPA plans as high-quality input to Grok Build's plan-search-build workflow. Leverage Arena Mode to evaluate multiple implementation approaches against the plan's acceptance criteria.
- **Self-Hosted / Local**: All components can run with local models + local vector DB. xAI API for the heavy reasoning steps.
- **CI/CD**: Optional hooks that re-index on spec changes, re-plan affected modules, or validate new code against current plans (traceability or contract tests).

---

## 15. Metrics, Evaluation & Success Criteria

**Quantitative**:
- Traceability coverage (% of plan elements with verified source links).
- Average refinement iterations per artifact until gate pass.
- Context token reduction vs. naive full-corpus approach (for equivalent downstream task success).
- Downstream coder agent task success / completion rate without major spec deviations.
- Time from spec change to updated plans/tasks (incremental mode).
- Critic score trends over project lifetime (improving patterns).

**Qualitative**:
- Human review: "Does this plan feel like it fully and accurately captured the intent of the original large specs for this module without requiring me to re-read everything?"
- "How much faster / with fewer clarifications can coder agents (or junior devs) implement from these plans vs. raw specs?"
- Reduced "I didn't realize that requirement existed" moments during implementation.

**Success Thresholds (MVP)**:
- ≥85% traceability on approved plans.
- Average <3 refinement iterations for most artifacts.
- Measurable reduction in context-related failures or back-and-forth in coder sessions.
- Positive subjective feedback from first real module usage.

---

## 16. Risks, Mitigations & Edge Cases

**Risks & Mitigations**:
- **Poor retrieval quality on messy/large corpus** → Invest upfront in chunking strategy + metadata + hybrid search. Start with well-structured subsets. Add human curation of key index files.
- **Over- or under-decomposition** → Critic sizing check + human gate on master plan. Goldilocks task sizing (implementable in 1 focused session).
- **Inconsistent plans across modules** → Strong semantic memory + global consistency critic passes on related clusters. Knowledge Graph helps.
- **Non-determinism / hallucination** → Structured schemas + critic gates + low-temperature critic + explicit "only use provided context or retrieved sources" instructions. Versioning makes drift visible.
- **High token/cost on very large projects** → Scoped retrieval + compression + model routing (cheap for indexing/retrieval, strong only for synthesis/critic) + caching of common context.
- **Human bottleneck on review gates** → Make gates configurable (auto-approve low-risk modules after high critic score). Provide excellent diff views and summaries for quick human review.
- **Legacy or poorly structured specs** → SIPA can still help by forcing explicit classification and traceability extraction; may require more human seed curation initially.

**Edge Cases**:
- Very small projects: Still useful for consistent structure and living traceability.
- Highly visual/UI-heavy specs (Figma, screenshots): Add vision model step to describe mocks → feed textual descriptions into Feature/UI planner.
- Conflicting requirements in corpus: Critic surfaces conflicts explicitly for human resolution; plans record assumptions.
- Rapidly evolving specs: Incremental mode + strong versioning + impact analysis via graph.

---

## 17. Future Extensions & Roadmap

- Full automated **Knowledge Graph RAG** with requirement dependency extraction and real-time impact analysis.
- **Multi-modal ingestion**: Vision models for UI mocks, diagrams, whiteboards in specs → generate textual descriptions or even starter wireframes/prompts.
- **Automated test & validation artifact generation**: From acceptance criteria → property-based tests, contract tests, E2E scenarios, or monitoring assertions.
- **Risk/Complexity scoring + auto-escalation**: Flag high-risk or complex plans for extra human review or finer-grained breakdown.
- **Meta-Planner / Self-Optimizer**: Analyze historical planner runs (which component types needed most refinements? which retrieval strategies worked best?) → evolve prompt templates, chunking rules, or even sub-planner personas.
- **Formal methods bridge**: For high-assurance modules, generate TLA+ specs, invariants, or model-checking artifacts from plans.
- **Team/Enterprise features**: Role-based access to plans, export to Confluence/Jira/Notion, CI/CD policy enforcement ("no code merged unless it satisfies current plan acceptance criteria"), multi-project semantic memory.
- **Domain-specific extensions**: Pre-built taxonomies and patterns for edtech (HKDSE), trading UIs, embedded/hardware (ESP32), legacy modernization (COBOL → modern), etc.

---

## 18. References & Sources

**Primary Research**:
- MAAD: arXiv:2606.01385 — "Bridging Requirements and Architecture: Multi-Agent Orchestration with External Knowledge and Hierarchical Memory"
- AgentOrchestra: arXiv:2506.12508 — Hierarchical multi-agent framework with top-level planner + modular sub-agents.
- LLM Multi-Agent Systems for SE survey: arXiv:2404.04834v4
- GoalAct, Self-Organized Agents, ALMAS, HPTSA, and related hierarchical planning papers (2025–2026).
- Context engineering literature (LangChain blog series, hybrid RAG, graph retrieval papers).

**Tooling & SDD**:
- GitHub Spec Kit & blog posts on spec-driven development with AI agents.
- Kiro, Tessl, and related spec-first tools.
- xAI Grok Build documentation (plan-search-build + Arena Mode).

**Broader**:
- SWE-agent, MASAI, MetaGPT, ChatDev, harness engineering papers (awesome-agent-harness).
- Kruchten 4+1 views, ATAM, ISO/IEC 42010 for architecture foundations.

---

**Closing Note**  
This complete specification is intentionally exhaustive so it can serve as the single source of truth for implementing or evolving SIPA. It directly addresses your requirement for breaking large specs into manageable, appropriately-detailed parts while preserving intent through traceability, critic-driven quality, and living updates.

You can now:
- Use this MD itself as the high-level spec fed into your agent harness to begin building SIPA.
- Prototype the MVP as outlined in Section 13.
- Request that I generate specific prompt templates, Pydantic schemas, sample code skeletons, or even a starter implementation notebook based on this spec.
- Iterate on any section (add domain-specific examples from your actual specs, refine rubrics, expand a template, etc.).

This is engineered to compound your existing strengths in AI agent engineering, spec-driven development, and rigorous harness building. Ready when you are to take the next step — whether that's refinement, prototyping, or applying it to a real module from your corpus. 

*Designed with the same "rethink deeply, quality gates, traceability, and practical production focus" philosophy you apply to your own systems.*