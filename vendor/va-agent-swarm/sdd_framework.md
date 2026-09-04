# UniSpec: An Open Federation, Evidence, and Conformance Standard for Spec-Driven Development

> **Executive decision:** Proceed only as a conditional interoperability and conformance project—not as another authoring methodology, workflow engine, or agent protocol.
>
> UniSpec should make specifications portable, traceable, safely consumable, and testably interoperable across existing tools. It should be considered successful if its interchange model and conformance suite are adopted directly by existing ecosystems, even if the standalone UniSpec product eventually becomes unnecessary.

---

## 0. What Version 3.0 Changes

Version 2.0 correctly repositioned UniSpec from a replacement framework to a federation layer. Version 3.0 strengthens that direction and fixes several remaining architectural, scientific, security, and delivery problems.

| v2.0 issue | v3.0 correction |
|---|---|
| The canonical model, Markdown syntax, persistence format, and runtime API were conflated | Separates the **UniSpec Semantic Model**, **UniSpec Package Format**, authoring projections, adapters, context compiler, and runtime surfaces |
| A static “Big Four” audit would become stale almost immediately | Introduces a versioned capability registry with exact source versions, observation dates, and compatibility probes |
| “Lossless core plus namespaced extensions” overstated cross-tool portability | Defines separate same-tool preservation, core-semantic interoperability, cross-tool projection, and opaque return-trip laws |
| Dual-LLM judging was part of semantic certification | LLM judges are advisory only; certification rests on deterministic invariants, executable checks, and blinded human adjudication |
| A universal two-percentage-point behavioral margin was proposed without power analysis | Equivalence margins are benchmark-specific and must be supported by a pre-registered statistical power analysis |
| Trace coverage was based heavily on changed lines | Replaces this with typed claims, evidence strength, code-unit and diff-hunk references, stale-evidence detection, and multiple coverage metrics |
| Approval metadata was mutable document frontmatter | Approvals, waivers, and verification results move to an append-only evidence and decision ledger |
| `org > repo > feature` was an oversimplified policy precedence rule | Separates non-overridable controls, overridable defaults, deny-overrides, and explicit time-limited waivers |
| The security model focused mainly on prompt injection | Adds path traversal, parser denial of service, tool poisoning, evidence forgery, adapter command injection, plugin compromise, data egress, replay, and multi-tenant threats |
| Rust/WASM was chosen before benchmarking implementation alternatives | Makes implementation language an early architecture decision based on measured performance, packaging, sandboxing, and contributor ergonomics |
| Public plugin registry, hosted registry, enterprise UI, and broad agent support were all included in Year 1 | Freezes v1.0 around interchange, evidence, conformance, CLI, CI, and safe integration surfaces; hosted services and marketplaces are deferred |
| “100% compatibility” remained ambiguous | Defines compatibility as passing 100% of the tests for a declared capability profile, with zero unreported loss—not universal feature equivalence |
| The roadmap effectively lasted 13 months | Provides a 52-week, 26-sprint roadmap that includes discovery within the requested 12-month period |
| Raw benchmark publication ignored proprietary-data constraints | Publishes raw data only where consent and licensing permit; otherwise publishes de-identified data, fixtures, protocols, and reproducible analysis |
| Foundation transfer was scheduled rather than earned | Establishes readiness criteria based on independent implementations, governance diversity, specification stability, and IP completeness |

---

## 1. Product Thesis

### 1.1 The problem UniSpec should solve

The basic problem of making an SDD workflow available inside a coding agent is no longer sufficiently differentiated. Existing frameworks already distribute instructions, commands, skills, workflows, and templates across many agents.

The remaining cross-ecosystem problems are:

1. **Artifact portability**
   - Specifications cannot move between methodologies without losing meaning, history, workflow state, or tool-specific details.
   - Same-tool upgrades can also break assumptions when artifact schemas or generated layouts change.

2. **Semantic accountability**
   - Teams cannot reliably determine whether a conversion preserved the meaning of requirements, constraints, scenarios, and deltas.
   - Marketing claims such as “compatible” or “lossless” lack a shared test method.

3. **Evidence-based traceability**
   - Requirement-to-design-to-task-to-code-to-test links are inconsistently represented.
   - Existing links often express an author’s claim rather than independently verified evidence.

4. **Safe context delivery**
   - Large specifications, policies, source artifacts, and tool schemas compete for limited model context.
   - Imported specifications can contain malicious or accidental instructions.
   - Teams need deterministic, inspectable context construction rather than opaque prompt assembly.

5. **Reproducibility under agent and model churn**
   - The same artifact can produce different outcomes after changes to models, tools, prompts, permissions, or agent runtimes.
   - Teams lack a regression harness for the complete specification-to-agent pipeline.

6. **Organization-scale governance**
   - Cross-repository requirements, shared controls, waivers, approvals, evidence, and audit exports need a neutral representation.
   - A central hosted service must not be required to obtain these benefits.

### 1.2 The proposed value proposition

UniSpec will provide six public goods:

1. A small, typed semantic model for SDD artifacts.
2. A portable package format with provenance and source maps.
3. A versioned adapter contract and compatibility registry.
4. A trace, evidence, approval, and waiver model.
5. A deterministic context compiler for different agents and budgets.
6. A public conformance and benchmark suite.

The positioning is:

> **Keep authoring where you already author. Use UniSpec to exchange, inspect, verify, compile, and audit.**

### 1.3 What UniSpec is not

UniSpec is not:

- a fifth SDD methodology;
- a replacement for Spec Kit, OpenSpec, BMAD, Kiro, or native agent planning;
- an autonomous software-development orchestrator;
- a project-management system;
- a model router;
- a guarantee that an implementation satisfies a requirement;
- a formal-verification system;
- a hosted specification repository required for interoperability;
- a new alternative to MCP, Agent Skills, AGENTS.md, ACP, or A2A.

---

## 2. Evidence Base and Ecosystem Snapshot

### 2.1 Source policy

All ecosystem assertions in this document are a snapshot as of **July 15, 2026**.

Normative implementation decisions must use, in priority order:

1. versioned official specifications;
2. official source repositories and release notes;
3. official vendor documentation;
4. peer-reviewed research;
5. preprints, clearly labeled as such;
6. practitioner evidence collected during discovery.

Each adapter must record:

```yaml
tool: openspec
tool_version: "1.3.1"
adapter_version: "0.4.0"
observed_at: "2026-07-15"
source_revision: "<commit-or-release-id>"
capability_manifest_digest: "sha256:..."
```

No compatibility statement may rely only on an unversioned product name.

### 2.2 Reference authoring ecosystems

The reference tools have advanced beyond the snapshot represented in `framework.v2.md`. This makes a continuously updated capability registry more important than a static feature comparison.

| Ecosystem | Capabilities UniSpec should preserve | What UniSpec must not duplicate |
|---|---|---|
| **GitHub Spec Kit** | Specification, clarification, planning, tasks, analysis, convergence, constitutions, extensions, presets, resumable workflows, and broad agent integration | Its workflow engine, extension catalogs, presets, and installation system |
| **OpenSpec** | Behavior-oriented specifications, delta changes, archive semantics, custom workflow schemas, source-of-truth specs, and coordination workspaces | Its delta-authoring UX, schema customization, workspace management, and repository conventions |
| **BMAD Method** | Canonical SPEC contracts, PRDs, architecture, stories, specialized skills and personas, quick-development paths, adversarial review, and multi-agent deliberation | Persona orchestration, product-planning workflows, autonomous development loops, and creative/elicitation tooling |
| **Kiro** | Requirements-first, design-first, bugfix, and quick-plan specifications; EARS requirements; tasks; dependency-based execution; hooks; IDE, CLI, and web continuity | Native Kiro authoring, task execution UX, permission system, hooks, and built-in Spec agent |

Spec Kit currently documents more than 30 agent integrations, multi-install support, extensions, presets, bundles, and resumable workflows. UniSpec therefore should consume and test these artifacts rather than recreate their distribution machinery. ([github.github.com](https://github.github.com/spec-kit/index.html?utm_source=openai))

OpenSpec’s current model includes delta specifications, customizable artifact schemas, and beta coordination workspaces with context stores and multi-repository links. Cross-repository coordination is therefore not an untouched greenfield feature; UniSpec must interoperate with it rather than position a registry as a replacement. ([github.com](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md?utm_source=openai))

BMAD now includes a canonical `SPEC.md` contract, reusable skills, adversarial and edge-case review tools, Quick Flow, and multiple forms of party-mode collaboration. The BMAD adapter should map the canonical SPEC and associated artifacts rather than flattening all BMAD output into generic requirements and tasks. ([docs.bmad-method.org](https://docs.bmad-method.org/workflow-map-diagram.html?utm_source=openai))

Kiro now supports requirements-first and design-first feature specifications, bugfix specifications, Quick Plan, parallel task waves, and specification continuity across IDE, CLI, and web. Its CLI 3.0 documentation describes a unified agent harness and a built-in Spec agent. ([kiro.dev](https://kiro.dev/docs/specs/quick-plan/?utm_source=openai))

### 2.3 Agent integration surfaces

UniSpec should target capabilities rather than hard-code assumptions about each agent.

| Target | Confirmed integration surfaces | Initial UniSpec approach |
|---|---|---|
| **Claude Code** | `CLAUDE.md`, path-scoped rules, Agent Skills, MCP, hooks, plugins, subagents, worktree isolation | Native skill pack, MCP server, policy hooks, and static fallback bundle |
| **GitHub Copilot** | Repository and path instructions, AGENTS.md, skills, custom agents, hooks, MCP, CLI and cloud-agent surfaces | Skills, AGENTS.md/instruction emitter, MCP, CLI automation |
| **Kiro** | Native specs, steering, hooks, MCP, custom agents, CLI Spec agent | Artifact adapter plus native skill/steering and MCP integration |
| **Trae** | Rules, open-format Agent Skills, custom agents, MCP | Portable skills and rules first; native automation only after capability probing |
| **Grok Build** | Interactive and headless CLI operation, plan/review workflow, ACP embedding | Static context bundle and headless integration first; optional ACP/MCP support after versioned tests |
| **Other agents** | At minimum, repository file access; often AGENTS.md, Agent Skills, MCP, or headless execution | Generic capability-driven integration without a dedicated adapter |

Claude Code explicitly separates persistent instructions, on-demand skills, external MCP tools, deterministic hooks, and isolated subagents. That separation should inform UniSpec’s emitter and context architecture. ([code.claude.com](https://code.claude.com/docs/en/memory?utm_source=openai))

GitHub Copilot currently supports multiple instruction scopes, Agent Skills, custom agent profiles, MCP servers, hooks, and AGENTS.md in several environments. UniSpec should generate the smallest suitable artifact rather than inject the complete specification into every session. ([docs.github.com](https://docs.github.com/en/copilot/reference/custom-instructions-support?utm_source=openai))

Trae’s official guidance describes Agent Skills based on the open `SKILL.md` format and distinguishes skills from always-loaded rules and external MCP capabilities. Its integration should initially rely on those portable surfaces rather than undocumented internal APIs. ([trae.ai](https://www.trae.ai/blog/trae_tutorial_0115?utm_source=openai))

Grok Build was introduced as an early-beta terminal coding agent with interactive and headless operation, plan review, and ACP support. Because it remains fast-moving, its integration must be capability-probed and version-pinned. ([docs.x.ai](https://docs.x.ai/build/overview?utm_source=openai))

### 2.4 Research synthesis and evidence quality

Research informs the design, but preprints do not establish product-market fit or prove efficiency gains.

| Research input | Evidence status | UniSpec consequence |
|---|---|---|
| Three SDD rigor levels: spec-first, spec-anchored, and spec-as-source | Practitioner-oriented arXiv preprint | Encode progressive rigor profiles, but keep risk and workflow type separate from rigor |
| Survey of MCP, ACP, A2A, and ANP | Survey preprint | Keep the semantic model transport-neutral and provide bindings rather than a new agent protocol |
| Process taxonomy for AI software-development frameworks | Comparative preprint | Model lifecycle events explicitly while allowing multiple workflow orders |
| Reversa reverse-documentation framework | Research preprint | Brownfield extraction produces quarantined draft claims, never automatically approved specifications |
| Contract-driven adversarial verification | Early research and deployment report | Support an optional adversarial-review profile with independent evidence and human escalation |
| TDAD graph-based impact analysis | Research preprint | Use graph-linked tests and impact analysis, but avoid treating a passing test as proof of requirement satisfaction |
| Specification gaming in reasoning models | Empirical research preprint | Include hidden negative tests, anti-gaming fixtures, and independent evidence sources |
| Prompt-injection testing across MCP clients | Empirical security preprint | Treat imported specs and tool descriptions as untrusted data; enforce permissions outside prompts |
| Governance limitations in agent protocols | Analytical preprint | Keep approvals, waivers, dissent, and audit records above MCP/A2A/ACP transport layers |

The SDD taxonomy paper supplies useful language for progressive rigor but should not be treated as evidence that a particular rigor level improves delivery outcomes. ([arxiv.org](https://arxiv.org/abs/2602.00180?utm_source=openai))

The interoperability survey supports using existing protocols for their intended roles rather than embedding UniSpec semantics into a new transport. ([arxiv.org](https://arxiv.org/abs/2505.02279))

The process taxonomy, Reversa, meta-engineering harness, and TDAD papers motivate explicit process states, brownfield extraction, adversarial review, and graph-linked testing. Their claims must be independently reproduced before becoming marketing statements. ([arxiv.org](https://arxiv.org/abs/2606.04967))

Recent specification-gaming and MCP prompt-injection results reinforce the need for hidden acceptance tests, least-privilege tools, trust labels, and deterministic controls outside the model context. ([arxiv.org](https://arxiv.org/abs/2605.02269))

A recent governance-gap analysis argues that current agent protocols do not fully represent deliberation, dissent, escalation, and replay. UniSpec should therefore represent governance as signed domain events, not as an assumed feature of an agent transport. ([arxiv.org](https://arxiv.org/abs/2606.31498?utm_source=openai))

---

## 3. Phase 0: Discovery and Falsification

No engineering plan should claim that interviews have occurred before they are conducted. Phase 0 is an execution plan for collecting that evidence.

### 3.1 Discovery sample

Conduct **36–42 structured interviews**:

| Segment | Target interviews |
|---|---:|
| Maintainers or major contributors from reference SDD ecosystems | 6–8 |
| Coding-agent platform or integration engineers | 4–6 |
| Solo developers and OSS maintainers | 6 |
| Startups with fewer than 30 engineers | 6 |
| Scale-up platform or developer-productivity teams | 6 |
| Regulated enterprises: finance, health, government, critical infrastructure | 6 |
| Security, standards, and software-engineering researchers | 2–4 |

At least one-third of interviewees must have used two or more coding agents on the same production codebase.

### 3.2 Core research questions

1. How often do teams move artifacts between agents or methodologies?
2. What is actually lost during tool switching?
3. Is migration cost material enough to justify adopting an interchange layer?
4. Which traceability outputs are required for review, compliance, or incident response?
5. Which artifacts are authoritative today?
6. Would teams run a public conformance suite without adopting a new authoring format?
7. Which agent surfaces are allowed in enterprise environments?
8. What data may not leave the repository or region?
9. Which workflow gates are useful, and which create unproductive ceremony?
10. Who would fund ongoing adapter maintenance?

### 3.3 Falsifiable hypotheses

| ID | Hypothesis | Validation threshold |
|---|---|---|
| H1 | Multi-agent teams experience artifact fragmentation at least quarterly | Supported by at least 50% of qualified multi-agent respondents |
| H2 | Artifact migration cost is a meaningful barrier to switching or mixing tools | Supported by at least 40% of respondents who attempted a switch |
| H3 | Teams prefer interoperability over a new canonical authoring UX | At least 70% choose import/export or verification over re-authoring |
| H4 | Trace and evidence reports solve a funded enterprise requirement | At least three design partners commit staff or budget |
| H5 | A small common semantic core can represent most reference-tool artifacts | At least 85% of sampled semantic elements map without flattening |
| H6 | Same-agent rendered artifacts are not materially worse than native artifacts | Pilot equivalence test is non-inferior within a pre-registered margin |
| H7 | Maintainers see reciprocal value in conformance testing | At least two ecosystems agree to review the adapter contract or run tests |
| H8 | A local-first architecture is sufficient for initial adoption | At least 70% of early users do not require a hosted registry |

### 3.4 Kill and pivot rules

| Condition | Decision |
|---|---|
| H1 and H2 both fail | Pivot to a standalone conformance corpus and migration toolkit |
| Common semantic coverage is below 70% | Ab; provide bilateral adapters and a shared evidence model |
| Tool maintainers reject the canonical model but value tests | Conformance-suite-only product |
| Rendered context materially degrades outcomes | Restrict v1 to inspection, migration, and traceability |
| Security review finds that safe context rendering cannot be bounded | Do not ship agent-facing mutation tools |
| Fewer than two funded design partners exist after Phase 0 | Do not staff the full eight-person build |

### 3.5 Phase 0 outputs

- Interview recordings or notes with consent.
- An anonymized evidence matrix.
- Jobs-to-be-done report.
- Ecosystem capability registry.
- Corpus rights and data-handling policy.
- Draft semantic-model RFC.
- Two adapter spikes.
- Initial threat model.
- Go, narrow, pivot, or stop decision.

---

## 4. Goals, Non-Goals, and Principles

### 4.1 Year-1 goals

1. **No silent loss**
   - Every import and export reports unsupported, transformed, approximated, and opaque-preserved content.

2. **Testable interoperability**
   - Four reference-tool adapters pass declared adapter profiles.
   - Five priority agent integrations pass declared integration profiles.

3. **Evidence-aware traceability**
   - Requirements, designs, tasks, code references, tests, builds, commits, approvals, waivers, and deployments use typed links.

4. **Safe context compilation**
   - Context bundles are deterministic, budgeted, provenance-aware, and labeled by trust level.

5. **Public conformance infrastructure**
   - All normative schemas, fixtures, test runners, and results are open.

6. **Local-first enterprise viability**
   - Core functionality operates without a hosted service or external model call.

7. **Scientific honesty**
   - Efficiency and quality claims are published only after pre-registered evaluation.

### 4.2 Non-goals for v1.x

UniSpec will not:

- replace native SDD authoring;
- provide a general agent runtime;
- define a new agent communication protocol;
- automatically approve agent-generated specifications;
- automatically infer that requirements are satisfied;
- implement a complete project-management application;
- provide formal verification of natural-language requirements;
- synchronize two authoritative sources bidirectionally without an explicit ownership mode;
- launch a public arbitrary-code plugin marketplace;
- require a central cloud registry;
- claim compliance certifications that apply only to a future hosted operator.

### 4.3 Design principles

1. **Federate before standardizing authoring.**
2. **Separate semantics from syntax.**
3. **One authoritative source at a time.**
4. **Deterministic enforcement, probabilistic advice.**
5. **Claims are not evidence.**
6. **Passing tests are evidence, not proof.**
7. **No silent conversion loss.**
8. **Use capability profiles, not product-name assumptions.**
9. **Untrusted specifications receive least privilege.**
10. **Progressive rigor must be based on risk, not ceremony preference alone.**
11. **Conformance results must be reproducible and independently runnable.**
12. **Absorption by the ecosystem is a valid success state.**

---

## 5. Product Components and Release Scope

### 5.1 Core components

#### A. UniSpec Semantic Model — USM

A typed, tool-neutral graph of intent, decisions, work, evidence, and governance.

#### B. UniSpec Package Format — UPF

A portable, deterministic representation of the semantic model, source artifacts, source maps, provenance, and conversion reports.

#### C. Adapter SDK

A contract for importing, exporting, validating, and capability-probing authoring ecosystems.

#### D. Context Compiler

A deterministic service that compiles task-specific, agent-specific context bundles under explicit budgets and trust policies.

#### E. Trace and Evidence Ledger

An append-only record of claims, evidence, approvals, waivers, policy decisions, and verification outcomes.

#### F. SpecOps CI Kit

CI jobs for validation, conversion, trace integrity, evidence freshness, drift, policy checks, and conformance.

#### G. Conformance Suite

Public fixtures, test runners, compatibility profiles, benchmark protocols, and signed reports.

#### H. Review Surfaces

A CLI-first UX plus a thin local web or editor review interface. Native authoring remains out of scope.

### 5.2 Committed v1.0 scope

| Area | v1.0 commitment |
|---|---|
| Semantic model | USM 1.0 with a deliberately small mandatory core |
| Package format | UPF directory and archive representation |
| Core CLI | Inspect, import, export, validate, diff, trace, compile context, record evidence, run gates |
| Adapters | Spec Kit, OpenSpec, BMAD, and Kiro |
| Agent integrations | Claude Code, GitHub Copilot, Kiro, Trae, and Grok Build |
| Generic integration | Static bundle, Agent Skill, instruction-file emitter, CLI JSON, and MCP |
| Traceability | Requirement through deployment references with typed evidence |
| Governance | Approvals, rejections, waivers, and policy decisions in an append-only ledger |
| CI | GitHub Actions and GitLab CI templates |
| Security | Sandboxed adapters, trust labels, path protections, content-free telemetry, signed releases |
| Conformance | Adapter, integration, security, and behavioral profiles |
| Documentation | Tool migration, agent integration, security, enterprise, and conformance guides |

### 5.3 Stretch scope

- Thin VS Code review extension.
- OCI-compatible package publication.
- Jira and Linear link enrichment.
- Property-based test proposal profile.
- Read-only portfolio dashboard.
- Additional adapters contributed externally.

### 5.4 Deferred beyond v1.0

- Hosted multi-tenant registry.
- SSO and SaaS RBAC.
- Public executable-plugin marketplace.
- Full authoring IDE.
- Autonomous multi-agent orchestration.
- Universal code-to-spec synchronization.
- Formal natural-language-to-code verification.
- Custom registry federation protocol.

---

## 6. Compatibility and Conformance Vocabulary

### 6.1 “Universal compatibility” definition

UniSpec must not use “100% compatible” without a profile.

A valid claim is:

> “Adapter X passes 100% of UniSpec Adapter Profile A3 for Tool Version Y, with zero unreported loss on Conformance Suite Version Z.”

It does not mean:

- every feature in one tool exists in another;
- all agents produce the same implementation;
- opaque tool-specific behavior becomes portable;
- a semantic conversion is perfect outside the declared profile.

### 6.2 Adapter profiles

| Profile | Meaning | Pass requirement |
|---|---|---|
| **A0 — Manifest** | Adapter declares versions, capabilities, authority modes, and known loss | Manifest schema passes |
| **A1 — Import/Export** | Adapter can parse and produce supported native artifacts | All required fixture operations succeed |
| **A2 — Source Preservation** | No-op same-tool round trips preserve declared source properties | 100% of applicable preservation tests |
| **A3 — Core Semantic Interop** | Supported USM semantics survive import, export, and cross-tool projection | 100% deterministic invariants; zero unreported loss |
| **A4 — Behavioral Rendering** | Rendered context is non-inferior to a native baseline for named agents and benchmarks | Pre-registered equivalence test passes |

### 6.3 Agent integration profiles

| Profile | Meaning |
|---|---|
| **I1 — Static** | Agent can consume a generated task context bundle from repository files |
| **I2 — Guided** | Agent receives native skills, instructions, or commands with versioned installation |
| **I3 — Lifecycle** | Agent can query tasks, compile context, report evidence, and request transitions through MCP or a headless API |
| **I4 — Enforced** | Native hooks or CI enforce selected policy and evidence requirements |

### 6.4 Security profiles

| Profile | Meaning |
|---|---|
| **S1 — Local Safe Execution** | Path confinement, sandboxing, resource limits, no-network default for adapters |
| **S2 — Provenance** | Signed packages, pinned dependencies, SBOM, build provenance, verified adapter identity |
| **S3 — Remote Enterprise** | Authenticated remote service, tenancy controls, audit exports, retention controls, and data residency |

Only S1 and S2 are required for the local v1.0 toolchain. S3 applies to any later hosted service.

---

## 7. Architecture

### 7.1 Logical architecture

```text
┌─────────────────────────────────────────────────────────────────┐
│ Native authoring ecosystems                                     │
│ Spec Kit · OpenSpec · BMAD · Kiro · future tools               │
└───────────────────────┬─────────────────────────────────────────┘
                        │ versioned adapters
                        ▼
┌─────────────────────────────────────────────────────────────────┐
│ USM: typed semantic graph                                       │
│ requirements · constraints · decisions · tasks · evidence       │
│ approvals · waivers · source maps · provenance                  │
└───────────────┬────────────────┬──────────────────┬──────────────┘
                │                │                  │
                ▼                ▼                  ▼
       UPF interchange     Trace/evidence     Validation/policy
           packages            ledger              engine
                │                │                  │
                └────────────────┼──────────────────┘
                                 ▼
                        Context compiler
                                 │
               ┌─────────────────┼─────────────────┐
               ▼                 ▼                 ▼
             MCP            Skills/files        CLI/headless
               │                 │                 │
               └─────────────────┼─────────────────┘
                                 ▼
                  Claude · Copilot · Kiro · Trae
                       Grok Build · future agents
```

### 7.2 Determinism boundary

The following operations must be deterministic:

- parsing supported syntax;
- source mapping;
- canonical serialization;
- hashing;
- schema validation;
- link validation;
- policy evaluation;
- delta application;
- context selection when summarization is disabled;
- loss reporting;
- evidence freshness calculation;
- conformance scoring.

The following may be probabilistic and must be labeled:

- ambiguity or contradiction suggestions;
- semantic-diff triage;
- code-to-spec harvesting;
- adversarial critique;
- proposed test generation;
- semantic relevance ranking;
- natural-language summarization.

Probabilistic services cannot silently mutate authoritative artifacts or independently award conformance certification.

### 7.3 Semantic model entities

The mandatory core should remain small.

| Entity | Purpose |
|---|---|
| `Workspace` | Collection of repositories, packages, policies, and external references |
| `Package` | Versioned unit of specification content |
| `ChangeSet` | Proposed change relative to a baseline |
| `Requirement` | Normative or desired behavior |
| `Scenario` | Concrete example, acceptance condition, or counterexample |
| `Constraint` | Technical, legal, security, performance, or process limitation |
| `Decision` | Chosen option and rationale |
| `DesignElement` | Architecture, component, interface, data model, or algorithm |
| `Task` | Planned unit of work |
| `CodeReference` | Repository, commit, path, symbol, or diff-hunk locator |
| `TestReference` | Automated or manual verification procedure |
| `Evidence` | Observation or attestation relevant to a claim |
| `Approval` | Signed decision by an authorized actor |
| `Waiver` | Time-limited exception to a policy or gate |
| `Policy` | Machine-checkable or human-reviewable control |
| `DeploymentReference` | Environment, release, artifact, or rollout reference |
| `ExternalContract` | Linked OpenAPI, AsyncAPI, Protobuf, Gherkin, CUE, TypeSpec, schema, or comparable contract |

### 7.4 Relation types

Minimum typed relations:

```text
contains
refines
constrained_by
motivated_by
implements
depends_on
precedes
verifies
contradicts
supersedes
deprecates
touches
generated_from
evidenced_by
approved_by
waived_by
deployed_as
```

Adapters may define namespaced relations but cannot silently reinterpret a core relation.

### 7.5 Canonical representation versus authoring projections

The USM is an abstract semantic model, not a Markdown template.

UniSpec defines:

1. **Canonical exchange serialization**
   - Deterministic JSON records.
   - Stable ordering and canonical hashing.
   - Suitable for conformance and package exchange.

2. **Human-readable projection**
   - Markdown with optional YAML frontmatter.
   - Intended for review and optional UniSpec-native authoring.
   - Not the only valid source syntax.

3. **Native projections**
   - Spec Kit, OpenSpec, BMAD, Kiro, or future tool layouts.

4. **Opaque source preservation**
   - Original files or unrecognized syntax preserved as source attachments.

This avoids forcing every methodology into one Markdown grammar.

### 7.6 Package format

Illustrative UPF layout:

```text
package.upf/
├── manifest.json
├── model/
│   ├── entities.jsonl
│   └── relations.jsonl
├── ledger/
│   └── events.jsonl
├── mappings/
│   ├── identities.json
│   └── source-map.json
├── sources/
│   ├── spec-kit/
│   ├── openspec/
│   ├── bmad/
│   └── kiro/
├── attachments/
├── reports/
│   ├── loss.json
│   ├── validation.json
│   └── provenance.json
└── lock.json
```

Requirements:

- Records have deterministic canonical serialization.
- Every source attachment has a digest.
- Every conversion has a source and target adapter version.
- Unknown data may be preserved opaquely.
- Package integrity is represented by a content root digest.
- Archives have decompression and path-safety limits.
- No package content is executable by default.

### 7.7 Authority modes

Each package must declare exactly one authority mode.

| Mode | Authoritative source | Intended use |
|---|---|---|
| `native-authoritative` | Existing tool artifacts | Most migrations and federated adoption |
| `unispec-authoritative` | USM or UniSpec projection | Teams deliberately choosing UniSpec as source |
| `external-authoritative` | External system such as issue tracker or contract repository | Read-through or generated views |
| `snapshot` | Immutable imported state | Audit, comparison, benchmark, or archival use |

Generated projections must carry:

```yaml
generated: true
authoritative: false
source_digest: "sha256:..."
generator: "unispec-adapter-openspec@0.4.0"
```

UniSpec will not support ungoverned dual-master editing.

### 7.8 Stable identity

Imported tools often do not provide stable identifiers. UniSpec therefore uses:

1. Native IDs where present.
2. Sidecar identity mappings persisted in `.unispec/identities.json`.
3. Deterministic provisional IDs based on source location and semantic fingerprint.
4. Alias and move records when entities are renamed or relocated.
5. Human confirmation for ambiguous deduplication.

Content hashes are revisions, not identities. An entity’s ID remains stable when its content changes.

### 7.9 Delta model

Core operations:

- `add`
- `replace`
- `patch`
- `deprecate`
- `remove`
- `supersede`
- `restore`

Every mutating operation includes:

```json
{
  "operation": "replace",
  "target": "urn:unispec:shop:req:cart-discount",
  "expected_revision": "sha256:old...",
  "new_revision": "sha256:new...",
  "reason": "Threshold policy changed",
  "actor": "human:ada"
}
```

Rules:

- Operations fail on stale preconditions.
- Concurrent edits use three-way semantic merge.
- Unresolvable conflicts become explicit conflict entities.
- Removals create tombstones.
- Archive operations never destroy change history.
- Cross-tool projection must report unsupported delta semantics.

### 7.10 Policy composition

A simple scope precedence rule is insufficient.

Policies have a mode:

| Mode | Behavior |
|---|---|
| `mandatory` | Cannot be overridden by lower scopes |
| `deny-overrides` | Any applicable deny wins |
| `default` | Nearest applicable scope wins |
| `advisory` | Produces findings but does not block |
| `waivable` | May be bypassed by an authorized, expiring waiver |

Scopes may include:

```text
organization
portfolio
workspace
repository
path
package
change
requirement
task
environment
```

A waiver must identify:

- policy;
- subject;
- approver;
- reason;
- issue or risk reference;
- start and expiry;
- compensating controls;
- signature or trusted CI identity.

### 7.11 Trace and evidence model

A trace link is a claim. Evidence determines how strongly the claim is supported.

#### Evidence strength

| Level | Meaning |
|---|---|
| `declared` | A human or agent asserted a relationship |
| `observed` | A tool observed a relevant event or artifact |
| `verified` | A trusted deterministic check validated the observation |
| `attested` | A trusted identity signed the evidence and its environment |
| `contradicted` | Evidence conflicts with the claim |
| `waived` | Verification requirement was explicitly waived |

Example:

```json
{
  "id": "evi-test-4f92",
  "subject": "urn:unispec:shop:req:cart-discount",
  "kind": "test-run",
  "producer": "ci:github-actions",
  "commit": "4c0f9a...",
  "test": "tests/cart/test_discount.py::test_threshold",
  "result": "pass",
  "environment_digest": "sha256:...",
  "artifact_digest": "sha256:...",
  "observed_at": "2026-07-15T12:00:00Z",
  "attestation": "sigstore:..."
}
```

A passing test supports a requirement but does not prove that all interpretations or edge cases are satisfied.

### 7.12 Trace metrics

UniSpec reports multiple metrics rather than one gameable percentage:

- requirement-to-test mapping coverage;
- requirement evidence coverage;
- verified evidence coverage;
- changed-hunk-to-task coverage;
- changed-code-unit-to-requirement coverage;
- orphan change rate;
- stale evidence rate;
- unapproved requirement revision rate;
- policy evaluation coverage;
- waiver count and age;
- untraced deployment rate.

Line-based coverage may be reported as a diagnostic but cannot be the sole merge gate.

### 7.13 Drift categories

| Drift | Detection | Default response |
|---|---|---|
| **Representation drift** | Native artifact no longer maps to recorded USM revision | Block generated export; require reconciliation |
| **Intent drift** | Approved requirement or constraint changed | Revoke affected approval status |
| **Trace drift** | Linked files, symbols, tests, or tasks disappeared | Mark links stale |
| **Evidence drift** | Evidence refers to old commit, environment, or test | Re-run required checks |
| **Implementation drift** | Governed code changed without an associated task or change | Warn or block by policy |
| **Policy drift** | Applicable policy version changed | Re-evaluate affected subjects |
| **Semantic drift** | Advisory analysis detects likely behavioral mismatch | Create a proposed finding or delta |
| **Runtime drift** | Agent, model, prompt, permission, or tool version changed | Trigger selected canary benchmarks |

### 7.14 Context compiler

The context compiler produces an inspectable `ContextBundle`.

Deterministic selection order:

1. Resolve the requested task or requirement.
2. Add mandatory organization and repository controls.
3. Add direct requirement, scenario, constraint, and design links.
4. Add dependency closure up to configured depth.
5. Add current task state and required evidence.
6. Add relevant code references and recent verified evidence.
7. Rank optional material.
8. Fit the target-specific token, byte, file, and tool-schema budgets.
9. Record every omitted or transformed item.
10. Produce a bundle digest.

Example manifest:

```yaml
bundle: ctx-8c91
task: urn:unispec:shop:task:implement-cart-discount
target:
  agent: claude-code
  integration_profile: I3
budget:
  tokens: 24000
  reserved:
    policy: 3000
    task: 3000
    evidence: 4000
sources:
  - id: urn:unispec:shop:req:cart-discount
    trust: approved
  - id: source:legacy-comments
    trust: quarantined
omitted:
  - id: des-historical-alternative
    reason: budget
digest: sha256:...
```

Rules:

- Deterministic extraction is the default.
- Model-generated summarization is optional.
- Summaries are derived artifacts with model, prompt, source, and loss metadata.
- Restricted content is not compiled for disallowed remote targets.
- Imported untrusted text is rendered as data, not elevated to project instructions.
- Mandatory policy content cannot be removed by budget compaction.
- Tool output should be paginated or referenced rather than dumped into context.

### 7.15 Adapter contract

Illustrative interface:

```ts
interface UniSpecAdapterV1 {
  describe(): AdapterManifest;

  detect(input: FileSet): Promise<DetectionResult>;

  import(
    input: FileSet,
    options: ImportOptions
  ): Promise<ImportResult>;

  export(
    package: UniSpecPackage,
    options: ExportOptions
  ): Promise<ExportResult>;

  validateNative(
    input: FileSet,
    options: ValidationOptions
  ): Promise<NativeValidationReport>;

  normalizeForComparison(
    input: FileSet
  ): Promise<NormalizedArtifactSet>;
}
```

The adapter does not certify itself. The independent conformance runner invokes it.

### 7.16 Interchange laws

#### Law 1: Same-tool no-op preservation

```text
normalize_T(export_T(import_T(A))) = normalize_T(A)
```

The adapter manifest declares whether this means byte equivalence, formatting-preserving equivalence, or structural equivalence.

#### Law 2: Core semantic preservation

```text
core(import_T(A)) = supported_core_T(A)
```

All unsupported source semantics appear in the loss report.

#### Law 3: Canonical projection preservation

```text
import_T(export_T(S)) = project_T(S)
```

`project_T(S)` is the subset representable by tool `T`, not the complete USM package.

#### Law 4: Opaque return-trip preservation

Data preserved in an origin namespace must survive a trip through another tool and be recoverable when exported back to the origin, unless explicitly removed.

#### Law 5: No silent approximation

Every approximation, inferred value, generated identifier, dropped ordering constraint, grammar conversion, or collapsed lifecycle state is reported.

### 7.17 Distribution surfaces

#### MCP

Provide a read-only mode by default.

Proposed resources:

```text
unispec://workspace
unispec://changes/{id}
unispec://requirements/{id}
unispec://tasks/{id}
unispec://evidence/{id}
unispec://context/{bundle-id}
```

Proposed tools:

```text
spec_validate
spec_query
context_compile
change_propose
task_claim
evidence_record
transition_request
drift_report
```

Mutation tools require explicit policy authorization and return proposed changes rather than editing authoritative native artifacts without a gate.

#### Agent Skills

Ship portable skills for:

- inspecting current work;
- compiling task context;
- proposing a change;
- implementing a task;
- recording evidence;
- reviewing trace and drift;
- preparing a verification report.

#### Instruction emitters

Generate the smallest appropriate project guidance for:

- AGENTS.md;
- CLAUDE.md;
- GitHub Copilot repository instructions;
- Kiro steering;
- Trae rules;
- other capability-manifested instruction files.

Generated blocks must be bounded by markers and preserve user-authored content.

#### CLI and headless API

Every command supports:

```text
--format human
--format json
--quiet
--offline
--no-model
```

Machine-readable output uses stable schemas and documented exit codes.

#### ACP and A2A

ACP or A2A bindings may be added as optional transport adapters. The core task, evidence, and governance state model must not depend on either protocol.

### 7.18 Plugin strategy

For v1.0:

- adapters and validators run out-of-process where possible;
- plugins declare filesystem, network, process, and environment capabilities;
- network access defaults to denied;
- source mounts default to read-only;
- dependencies are pinned;
- package signatures are verified where available;
- unsigned plugins require an explicit local override;
- no public arbitrary-code registry is launched.

A public marketplace is gated on a completed plugin security review and incident-response capability.

### 7.19 Implementation-language decision

The specification remains language-neutral.

During Phase 0, compare:

1. TypeScript-only reference implementation;
2. Rust deterministic core with TypeScript adapter host;
3. Go core with TypeScript adapter SDK.

Selection criteria:

- cold-start and parsing performance;
- deterministic serialization;
- cross-platform packaging;
- WASI or process sandboxing;
- contributor accessibility;
- fuzzing ecosystem;
- JSON Schema tooling;
- integration with predominantly Markdown and JavaScript-based agent ecosystems;
- total delivery risk for an eight-person team.

No language choice is normative until the spike is complete.

---

## 8. Workflow Profiles

### 8.1 Rigor profiles

Rigor and change type are separate fields.

| Profile | Meaning | Minimum artifacts |
|---|---|---|
| **R1 — Spec-First** | Intent is specified before implementation; maintenance after delivery is optional by policy | Requirement, acceptance condition, task |
| **R2 — Spec-Anchored** | Specification remains an approved reference throughout implementation and maintenance | Requirements, constraints, design, tasks, trace, evidence, approvals |
| **R3 — Spec-as-Source** | Selected executable artifacts are generated from or governed directly by machine-processable specifications | R2 plus generation contracts and reproducible outputs |

R3 should be used for suitable domains such as APIs, schemas, policies, configuration, or protocol definitions—not as a blanket claim that all application code can be generated reliably.

### 8.2 Change types

- feature;
- bugfix;
- migration;
- refactor;
- security remediation;
- operational change;
- experiment;
- deprecation;
- incident follow-up;
- documentation-only change.

### 8.3 Risk classes

| Class | Example | Default gates |
|---|---|---|
| `low` | Documentation, isolated UI text, safe refactor | Automated validation |
| `medium` | Normal product feature or API-compatible change | Requirement and implementation review |
| `high` | Authentication, payments, data migration, public API break | Design, security, test, and rollout approval |
| `critical` | Safety, regulated decisioning, cryptography, broad data access | Independent review, signed evidence, explicit deployment approval |

A low-risk R2 change may be lightweight. A high-risk R1 change should normally be rejected by policy.

### 8.4 Standard lifecycle

```text
proposed
   │
   ▼
clarifying ─────► rejected
   │
   ▼
review_ready
   │
   ▼
approved
   │
   ▼
implementing
   │
   ▼
evidence_pending
   │
   ▼
verified ───────► contradicted
   │
   ▼
released
   │
   ▼
archived
```

Transitions are events, not editable status strings.

Every transition records:

- actor;
- previous state;
- next state;
- object revision;
- policy result;
- required evidence;
- timestamp;
- signature or trusted execution identity.

### 8.5 End-to-end workflow

1. **Detect and import**
   - Discover native artifacts.
   - Select authority mode.
   - Generate identity mappings.
   - Produce validation and loss reports.

2. **Clarify**
   - Resolve ambiguities.
   - Identify non-goals and constraints.
   - Record unresolved questions.

3. **Approve intent**
   - Evaluate policies.
   - Record requirement approvals.

4. **Design and plan**
   - Link design elements to requirements.
   - Break work into tasks and dependencies.
   - Declare expected code areas and evidence.

5. **Compile context**
   - Select target agent and budget.
   - Generate a signed or hashed context bundle.

6. **Delegate**
   - Invoke through native skill, MCP, CLI, or static bundle.
   - Record agent, model, tools, permissions, and bundle digest.

7. **Implement**
   - Record task claims and changed code references.
   - Prevent concurrent ownership conflicts using leases or worktrees where configured.

8. **Collect evidence**
   - Run tests and checks through trusted automation.
   - Record build and environment metadata.

9. **Verify**
   - Evaluate evidence freshness and policy gates.
   - Run advisory semantic review if enabled.
   - Require human review where configured.

10. **Release and archive**
    - Link deployment or release artifacts.
    - Apply approved deltas.
    - Preserve all decisions and evidence.

### 8.6 Brownfield harvesting

`unispec harvest` may infer:

- existing behavior;
- public interfaces;
- observed invariants;
- likely requirements;
- test-to-code relationships;
- undocumented constraints.

All harvested content must be marked:

```yaml
origin: agent-derived
trust: quarantined
review_status: unreviewed
confidence: 0.64
```

Harvesting cannot:

- overwrite approved requirements;
- promote comments to policy;
- infer authorization from implementation;
- mark requirements verified;
- conceal source uncertainty.

### 8.7 Multi-agent work

UniSpec v1 supports coordination primitives, not autonomous negotiation:

- task ownership lease;
- expected output;
- input context digest;
- worktree or workspace reference;
- completion evidence;
- conflict state;
- human escalation;
- merge result.

Multi-agent voting, negotiation, and arbitration semantics remain a research topic.

---

## 9. Security, Safety, and Privacy

### 9.1 Security posture

Specifications, adapters, plugins, MCP servers, imported repositories, generated context, tests, and evidence are all potentially untrusted.

A model instruction is not a security boundary.

### 9.2 Trust zones

```text
┌─────────────────────────────────────────────┐
│ Trusted policy and release infrastructure   │
├─────────────────────────────────────────────┤
│ Deterministic UniSpec core                  │
├─────────────────────────────────────────────┤
│ Sandboxed adapters and plugins              │
├─────────────────────────────────────────────┤
│ Imported specs, source repos, attachments   │
├─────────────────────────────────────────────┤
│ Agent/model runtime and external MCP tools  │
├─────────────────────────────────────────────┤
│ Remote services and optional registries     │
└─────────────────────────────────────────────┘
```

Trust must never flow upward merely because an agent summarized or reformatted content.

### 9.3 Threat model

| Threat | Required controls |
|---|---|
| Prompt injection in specifications, comments, issues, test output, or tool descriptions | Trust labels, instruction/data separation, least-privilege tools, approval gates, hidden attack fixtures |
| MCP tool poisoning or misleading tool metadata | Server allowlists, pinned configuration, tool-schema inspection, user confirmation for new servers, audit logging |
| Path traversal or symlink escape | Canonical path resolution, repository-root confinement, no absolute output paths, symlink checks |
| Archive “zip slip” or decompression bomb | Entry-count, size, recursion, compression-ratio, and normalized-path limits |
| Parser denial of service | File-size, nesting-depth, recursion, token-count, and execution-time limits |
| Adapter command injection | Structured process arguments, no shell interpolation, sandboxing, input validation |
| Malicious plugin or dependency | Signed and pinned packages, SBOM, provenance, capability manifests, no-network default |
| Secret exfiltration through context or telemetry | Secret scanning, redaction, data labels, target policy, content-free telemetry |
| Forged task completion evidence | Trusted CI identities, commit-bound attestations, test existence checks, environment digests |
| Replay of old approvals or evidence | Object revision binding, expiry, nonce or event sequence, stale-evidence detection |
| Policy bypass through lower-scope configuration | Mandatory and deny-overrides semantics; signed waiver requirement |
| Model or provider data-residency violation | Target-agent policy, explicit external-call consent, offline mode |
| Cross-tenant registry access | Tenant isolation, object-level authorization, encryption, audit logs; applicable only to later hosted services |
| Dependency confusion or compromised build | Locked dependencies, isolated builds, signed releases, provenance verification |
| Generated code modifying governance files | Protected paths, separate permissions, mandatory human review |
| Malicious tests that pass while hiding defects | Independent hidden tests, mutation tests, reviewer separation, evidence diversity |

### 9.4 Prompt-injection containment

No sanitizer can guarantee that a stochastic agent will ignore every malicious instruction. UniSpec therefore uses defense in depth:

1. Label content by origin and trust.
2. Separate policy, task instructions, source data, and evidence.
3. Do not promote imported prose into trusted instruction files.
4. Render quarantined material with explicit boundaries.
5. Deny high-risk tools unless needed.
6. Require confirmation for external network, secrets, deployments, or governance changes.
7. Run agents in constrained worktrees or containers where appropriate.
8. Validate results independently.
9. Record the exact context bundle and permissions used.

### 9.5 Adapter sandbox

Default adapter execution:

```yaml
filesystem:
  source: read-only
  output: scratch-only
  home: unavailable
network: denied
process_spawn: denied
environment:
  allow: []
limits:
  cpu_seconds: 30
  memory_mb: 512
  output_mb: 100
```

Capabilities may be granted explicitly and recorded in the conformance report.

### 9.6 Data classification

Supported labels:

- `public`
- `internal`
- `confidential`
- `restricted`
- `secret-containing`
- `regulated`

A target policy may state:

```yaml
target: agent:cloud-default
max_classification: internal
external_processing: true
retention: provider-policy
```

The context compiler refuses incompatible bundles unless an authorized waiver exists.

### 9.7 Supply-chain requirements

Before v1.0:

- signed source tags and release artifacts;
- SBOM for each binary and container;
- build provenance;
- dependency pinning;
- reproducible-build investigation;
- secret scanning;
- branch protection;
- two-person review for release workflows;
- vulnerability disclosure policy;
- incident-response runbook;
- supported-version policy.

### 9.8 Security launch gates

v1.0 cannot ship with:

- unresolved critical or high findings from the independent audit;
- known path or archive escapes;
- unbounded parser cases;
- mutation tools enabled remotely without authentication;
- content-bearing telemetry enabled by default;
- unsigned release artifacts;
- a plugin path that bypasses declared permissions.

---

## 10. Non-Functional Requirements

Targets apply to documented reference hardware and fixture classes.

| Category | v1.0 target | Measurement |
|---|---|---|
| Single-artifact parse | Under 100 ms P95 for a 1 MiB supported artifact | Cold and warm benchmark |
| Project validation | Under 2 seconds P95 for 10,000 semantic entities | Reference monorepo fixture |
| Query latency | Under 1 second P95 for scoped trace queries over 100,000 entities | Warm local index |
| Memory | Under 512 MiB for the standard 100,000-entity stress corpus | Peak resident memory |
| Determinism | Identical canonical output and digest for identical inputs and versions | Repeated and cross-platform tests |
| Source preservation | 100% pass for declared A2 properties | Golden and mutation corpus |
| Loss reporting | 100% of seeded unsupported constructs reported | Seeded-loss suite |
| Core semantic interop | 100% deterministic invariants for the declared A3 subset | Cross-adapter tests |
| Context budget | Never exceed configured hard limits | Target tokenizer and byte fallback |
| Compaction | All omissions and summaries reported; mandatory policy never omitted | Context fixture suite |
| Scale | 50 repositories, 10,000 changes, 100,000 entities | Stress tests |
| Adapter freshness | Stable supported releases assessed within 14 days | Compatibility dashboard |
| Onboarding | Existing project first import under 30 minutes P75 | Moderated usability test |
| Greenfield setup | First validated package under 15 minutes P75 | Moderated usability test |
| Offline operation | Parsing, validation, conversion, trace, evidence, and CI run without network | Air-gapped test |
| Cross-platform | Supported on current Windows, macOS, and major Linux distributions | Release matrix |
| Accessibility | Review UI meets WCAG 2.2 AA for core flows | Automated and manual audit |
| Telemetry | Off by default in CI; no spec or code content | Source and runtime inspection |
| Reliability | Deterministic seeded drift found in the same CI run | Seeded-drift suite |

There is no single “cross-agent interpretation accuracy” NFR. Structural, semantic, behavioral, security, and operational properties are measured separately.

---

## 11. Testing, Conformance, and Benchmark Strategy

### 11.1 Test pyramid

#### Level T0: Unit and property tests

- parsers;
- canonicalization;
- IDs;
- source maps;
- deltas;
- policy composition;
- evidence freshness;
- context selection;
- loss-report completeness.

#### Level T1: Fuzz and adversarial tests

- malformed frontmatter;
- Unicode and bidirectional characters;
- deeply nested Markdown;
- duplicate IDs;
- giant files;
- archive bombs;
- path traversal;
- malicious links;
- prompt injection;
- deceptive tool descriptions;
- forged evidence.

#### Level T2: Public artifact corpus

At least **1,000 artifact fixtures**, not 1,000 expensive end-to-end agent tasks:

| Fixture class | Count target |
|---|---:|
| Parser and syntax edge cases | 300 |
| Native reference-tool artifacts | 250 |
| Delta and lifecycle cases | 150 |
| Cross-tool projection cases | 150 |
| Security and adversarial cases | 100 |
| Scale and monorepo cases | 50 |

Each fixture records provenance, license, tool version, expected properties, and whether it is synthetic or naturally occurring.

#### Level T3: Executable behavior corpus

Approximately 80–120 reproducible tasks across:

- web applications;
- APIs;
- mobile projects;
- data pipelines;
- infrastructure;
- libraries;
- monorepos;
- brownfield changes;
- bug fixes;
- security remediations.

Each task contains hidden acceptance checks and a reproducible sandbox.

#### Level T4: Partner corpus

Proprietary specifications remain in partner-controlled environments. The conformance runner exports signed aggregate results, not source content.

#### Level T5: Production pilots

Instrumented three-to-six-month pilots measuring:

- task success;
- intervention count;
- cycle time;
- agent cost;
- context size;
- trace completeness;
- stale evidence;
- regressions;
- user workload;
- security findings.

### 11.2 Fidelity model

#### F0 — Source preservation

Does a no-op same-tool round trip preserve the adapter’s declared byte, formatting, comment, ordering, and unknown-content properties?

#### F1 — Structural fidelity

Are entities, relations, IDs, lifecycle states, delta operations, and source references preserved?

#### F2 — Semantic fidelity

Are normative strength, conditions, outcomes, constraints, exclusions, and dependency meaning preserved?

Evaluation order:

1. deterministic invariants;
2. executable scenarios where available;
3. rule-based semantic checks;
4. blinded expert review;
5. LLM-generated candidate findings for triage only.

LLM agreement cannot independently certify F2.

#### F3 — Behavioral fidelity

For a named agent, model, configuration, and benchmark:

- compare native and UniSpec-rendered inputs;
- randomize presentation order;
- repeat stochastic runs;
- use hidden acceptance tests;
- block by task family and repository;
- report effect sizes and confidence intervals;
- use an equivalence or non-inferiority margin justified before data collection.

An underpowered result is **inconclusive**, not a pass.

#### F4 — Operational value

Measure:

- elapsed and active human time;
- agent turns;
- retries;
- manual corrections;
- token and financial cost;
- escaped defects;
- review effort;
- onboarding time;
- trace and audit usefulness.

### 11.3 Efficiency hypotheses

The original 40% cycle-time and 60% spec-defect reductions remain hypotheses.

Pre-register:

- primary and secondary outcomes;
- defect taxonomy;
- inclusion and exclusion criteria;
- sample-size calculation;
- randomization;
- handling of failed agent runs;
- statistical model;
- subgroup analysis;
- stopping rules.

Publish:

- protocol;
- analysis code;
- allowed raw data;
- de-identified results;
- negative and null findings;
- deviations from the protocol.

### 11.4 Agent compatibility matrix

Test cadence:

| Cadence | Tests |
|---|---|
| Every commit | Deterministic core and adapter fixture tests |
| Nightly | Agent smoke tests on pinned configurations |
| Weekly | Expanded current-model and current-agent matrix |
| Release candidate | Full declared conformance and security suite |
| After provider change | Targeted runtime-drift canary |
| Quarterly | Full behavioral benchmark refresh |

Exact run metadata includes:

- agent and version;
- model identifier;
- date;
- region where relevant;
- context bundle digest;
- tool and permission configuration;
- adapter version;
- prompt or skill version;
- attempt number;
- sandbox image;
- repository revision.

### 11.5 Conformance publication

A report includes:

```yaml
subject: adapter:openspec
adapter_version: "1.0.0"
tool_versions:
  - "1.3.1"
profiles:
  A0: pass
  A1: pass
  A2: pass
  A3: pass
  A4:
    status: not-tested
suite_version: "1.0.0"
executed_at: "2026-07-15T12:00:00Z"
runner_digest: "sha256:..."
report_digest: "sha256:..."
```

Rules:

- Self-run reports are clearly labeled.
- Official certification requires an independent runner.
- Reports expire when the relevant tool, adapter, or suite changes materially.
- Paid support cannot alter pass/fail requirements.
- Failures and declared limitations remain public.

---

## 12. Twelve-Month Development Roadmap

### 12.1 Quarterly milestones

| Quarter | Outcome |
|---|---|
| **Q1** | Discovery completed; problem and semantic model validated; core architecture selected |
| **Q2** | Deterministic core, package format, first two adapters, context compiler, and alpha release |
| **Q3** | Four adapters, five agent packs, trace/evidence, SpecOps, and internal beta |
| **Q4** | External beta with 50+ teams, security audit, conformance release, documentation, and v1.0 |

### 12.2 Bi-weekly deliverables

| Sprint | Weeks | Deliverables |
|---:|---:|---|
| 1 | 1–2 | Project charter; source policy; RFC process; interview instrument; initial threat model |
| 2 | 3–4 | First 10 interviews; corpus licensing policy; ecosystem capability registry draft |
| 3 | 5–6 | Next 12–15 interviews; semantic-model alternatives; source-preservation spike |
| 4 | 7–8 | Remaining interviews; OpenSpec↔USM↔Kiro spike; Phase 0 go/pivot/stop review |
| 5 | 9–10 | USM v0.1; package manifest; canonicalization prototype; CLI `inspect` and `validate` |
| 6 | 11–12 | Stable identity sidecar; source maps; delta engine; architecture-language decision |
| 7 | 13–14 | Adapter SDK v0.1; OpenSpec importer; fixture harness |
| 8 | 15–16 | OpenSpec exporter; A1/A2 tests; deterministic loss reports |
| 9 | 17–18 | Spec Kit importer/exporter; native normalization |
| 10 | 19–20 | OpenSpec↔Spec Kit A3 subset; conflict and opaque-return tests |
| 11 | 21–22 | Context compiler v0.1; static bundle; Agent Skill and AGENTS.md emitters |
| 12 | 23–24 | Read-only MCP server; Claude Code and Copilot integrations |
| 13 | 25–26 | Alpha v0.2; local security review; first design-partner deployment |
| 14 | 27–28 | Kiro adapter and integration; requirements/design/task workflow fixtures |
| 15 | 29–30 | BMAD adapter; canonical SPEC and companion mapping |
| 16 | 31–32 | Trae and Grok Build I1/I2 packs; capability probe framework |
| 17 | 33–34 | Trace graph; evidence ledger; signed transition events |
| 18 | 35–36 | SpecOps GitHub Actions and GitLab CI; evidence freshness |
| 19 | 37–38 | Drift engine; policy composition; approvals and expiring waivers |
| 20 | 39–40 | Internal beta v0.5; benchmark harness; 1,000-fixture corpus target reached |
| 21 | 41–42 | External beta wave 1: 10 teams; migration tooling and telemetry audit |
| 22 | 43–44 | External beta wave 2: 25 teams; fuzzing and prompt-injection red team |
| 23 | 45–46 | External beta wave 3: 50+ teams; air-gapped and scale tests |
| 24 | 47–48 | Release candidate; documentation freeze; conformance reports |
| 25 | 49–50 | Independent security audit fixes; performance and compatibility release |
| 26 | 51–52 | v1.0 release; research report; governance election; foundation-readiness review |

### 12.3 Stage gates

#### Gate G0 — Week 8

Proceed only if:

- discovery thresholds support a meaningful problem;
- at least two design partners exist;
- semantic-model spike achieves at least 70% lossless core coverage;
- funding covers the next nine months.

#### Gate G1 — Week 16

Proceed to broader adapter work only if:

- core determinism tests pass;
- no-op source preservation is viable;
- loss reports identify all seeded losses;
- the adapter SDK does not require tool-specific logic in the core.

#### Gate G2 — Week 32

Proceed to external beta only if:

- four adapters pass A1;
- at least two pass A2;
- all five priority agents pass I1;
- no known critical sandbox, parser, or path-safety defect remains.

#### Gate G3 — Week 46

Create a release candidate only if:

- 50 teams have entered beta;
- all launch profiles have signed reports;
- air-gapped use works;
- seeded drift and evidence tests pass;
- security audit has no unresolved critical findings.

#### Gate G4 — Week 50

Ship v1.0 only if:

- all committed deliverables are documented;
- compatibility claims use profiles;
- independent audit remediation is complete;
- rollback and incident-response processes are tested;
- at least two external organizations run the conformance suite.

### 12.4 Scope-control rule

The following cannot displace launch-critical work:

- hosted registry;
- public plugin marketplace;
- full authoring UI;
- autonomous orchestration;
- SSO;
- foundation submission;
- additional agent integrations.

They require explicit removal of an existing committed deliverable or additional staffing.

---

## 13. Team and Resource Allocation

### 13.1 Eight-engineer team

| Role | Count | Primary ownership |
|---|---:|---|
| Backend engineer — semantic core | 1 | USM, package format, canonicalization |
| Backend engineer — trace and policy | 1 | Graph, ledger, policy, drift |
| Backend engineer — adapter platform | 1 | Adapter SDK, OpenSpec, Spec Kit |
| Backend engineer — integrations | 1 | BMAD, Kiro, MCP, CLI APIs |
| Frontend/DX engineer — review UI | 1 | Local review UI, VS Code extension, accessibility |
| Frontend/DX engineer — agent experience | 1 | Skills, instruction emitters, CLI UX, documentation tooling |
| DevSecOps engineer | 1 | CI/CD, sandboxing, releases, provenance, security |
| QA and benchmark engineer | 1 | Corpus, fuzzing, conformance, agent benchmarks |

### 13.2 Part-time support

Required:

- product and standards lead;
- research statistician;
- security advisor;
- open-source counsel;
- community manager or developer advocate;
- technical writers;
- invited maintainers from reference ecosystems.

A project with eight engineers but no accountable product owner is not adequately staffed.

### 13.3 Work allocation

Approximate Year-1 engineering capacity:

| Workstream | Capacity |
|---|---:|
| Semantic model and deterministic core | 22% |
| Adapters and source preservation | 25% |
| Trace, evidence, policy, and CI | 18% |
| Agent integrations and context compiler | 15% |
| Security and release engineering | 10% |
| Review UX and documentation | 5% |
| Conformance and benchmarks | 5% |

The QA engineer coordinates test design, but quality work is owned by every workstream.

### 13.4 Funding gates

Before staffing the complete team:

- secure 12 months of operating funding plus a three-month contingency;
- identify at least two design partners;
- fund the independent security audit;
- reserve compute and agent-subscription budget for benchmarks;
- fund legal review of specification, patent, trademark, and corpus licensing.

Revenue or sponsorship cannot influence conformance outcomes.

---

## 14. Deliverables

### 14.1 Toolchain

Apache-2.0:

- `unispec` CLI;
- deterministic core library;
- adapter SDK;
- four reference adapters;
- context compiler;
- trace and evidence engine;
- local MCP server;
- SpecOps CI kit;
- local review interface;
- conformance runner.

### 14.2 Specification assets

Community Specification License with explicit patent terms:

- USM normative specification;
- UPF normative specification;
- adapter contract;
- context bundle specification;
- trace and evidence specification;
- policy composition specification;
- compatibility profile definitions;
- version-negotiation and deprecation policy.

### 14.3 Public test assets

- 1,000+ artifact fixtures;
- executable behavioral benchmark;
- seeded-drift corpus;
- prompt-injection and tool-poisoning suite;
- parser fuzz seeds;
- adapter compatibility matrix;
- signed conformance reports;
- reproducible analysis code.

### 14.4 Documentation

- conceptual architecture;
- threat model;
- migration guides for all four reference tools;
- agent guides for all five priority agents;
- local and air-gapped deployment;
- enterprise policy and evidence playbook;
- adapter-authoring guide;
- conformance-provider guide;
- three rigor-profile tutorials;
- incident-response and upgrade guides.

### 14.5 Research report

The public report includes:

- discovery methodology;
- anonymized findings;
- architecture rationale;
- mapping and loss taxonomy;
- conformance methodology;
- benchmark protocol;
- efficiency results;
- security findings;
- negative and inconclusive results;
- recommendations for ecosystem maintainers.

---

## 15. Success Criteria

### 15.1 Launch criteria

| Category | v1.0 requirement |
|---|---|
| Source preservation | All four adapters pass declared A2 properties |
| Core interoperability | All four pass A3 for the mandatory USM subset |
| Agent support | Five priority agents pass at least I2 |
| Lifecycle integration | At least three priority agents pass I3 |
| Security | Core and adapters pass S1 and S2; no unresolved critical/high audit findings |
| Loss reporting | 100% of seeded unsupported constructs reported |
| Determinism | Canonical outputs reproducible across supported platforms |
| Corpus | 1,000+ artifact fixtures and at least 80 executable tasks |
| External validation | At least two external tools or organizations run the suite |
| Beta | 50+ teams enter the beta; at least five complete sustained pilots |
| Documentation | All committed migration, integration, and enterprise guides published |

### 15.2 Adoption metrics

| Metric | Target |
|---|---:|
| Existing-project first successful import | Under 30 minutes P75 |
| Greenfield first validated package | Under 15 minutes P75 |
| Unreported conversion-loss incidents | 0 |
| External adapter or validator contributions | At least 3 within three months of v1.0 |
| External conformance implementations | At least 2 at launch; 4 in Year 1 |
| Active beta satisfaction | At least 85% satisfied among at least 30 active respondents |
| Median adapter lag for supported stable releases | 14 days or less |
| Enterprise production teams | 10 committed target; 50 stretch target in Year 1 |
| GitHub stars | 1,000 within six months, tracked as a secondary awareness metric |

### 15.3 Scientific metrics

- Publish the pre-registration before collecting the decisive efficiency-trial data.
- Report confidence intervals and effect sizes, not only point estimates.
- Mark underpowered results as inconclusive.
- Do not turn the 40% and 60% hypotheses into marketing claims unless supported.
- Preserve negative results in the public report.

### 15.4 Standardization metrics

Foundation transfer readiness requires:

- at least three independent implementations or substantial integrations;
- at least two maintainers unaffiliated with the founding organization;
- six months of specification stability;
- completed patent and contribution policy;
- public compatibility and security processes;
- evidence that the specification is useful independently of the reference toolchain.

---

## 16. Governance, Licensing, and Sustainability

### 16.1 Governance structure

#### Technical Steering Committee

Responsibilities:

- normative specification;
- compatibility policy;
- conformance profiles;
- security response;
- release approval.

No single vendor may hold a permanent majority.

#### Interoperability Working Group

Standing invitations to:

- Spec Kit;
- OpenSpec;
- BMAD;
- Kiro;
- coding-agent vendors;
- enterprise platform teams;
- independent adapter authors;
- security and research representatives.

#### Working groups

- Semantic Model WG
- Adapter and Conformance WG
- Security WG
- Evidence and Traceability WG
- Benchmark and Research WG
- Enterprise Deployment WG

### 16.2 RFC process

An RFC is required for:

- mandatory entity or relation changes;
- canonical serialization changes;
- lifecycle semantics;
- adapter contract changes;
- conformance scoring;
- security-profile changes;
- compatibility-breaking behavior.

RFC stages:

```text
draft → discussion → accepted/rejected → implementation → validation → release
```

Every accepted RFC records alternatives and migration consequences.

### 16.3 Versioning

- Major: incompatible semantic or wire change.
- Minor: backward-compatible capability addition.
- Patch: clarification, test correction, or reference implementation fix.

Requirements:

- capability negotiation;
- explicit `requires` ranges;
- at least two supported minor versions;
- minimum six-month deprecation window;
- migration tooling for breaking changes;
- conformance suite version pinned in every report.

### 16.4 Licensing

Recommended:

- toolchain: Apache-2.0;
- normative specification: Community Specification License 1.0, reviewed with an explicit patent policy;
- documentation: CC-BY-4.0;
- templates: MIT;
- fixture corpus: per-fixture licensing and provenance metadata.

Legal review must address:

- contributor patent grants;
- DCO or CLA;
- compatibility trademarks;
- third-party artifact redistribution;
- generated-fixture ownership;
- benchmark data consent;
- use of vendor names in certification claims.

### 16.5 Conformance mark

A compatibility mark must include:

- target tool and version;
- adapter version;
- profile;
- suite version;
- report date;
- report digest.

The project may revoke a mark for:

- falsified results;
- undisclosed loss;
- expired certification;
- material security defects;
- misleading scope claims.

### 16.6 Funding

Permitted:

- corporate sponsorship;
- foundation grants;
- paid enterprise support;
- migration services;
- security and deployment consulting;
- optional hosted registry later;
- independent certification execution.

Not permitted:

- paywalling the core specification;
- paywalling the public conformance suite;
- pay-to-pass certification;
- restricting competitor implementations;
- exclusive control of the public corpus by one sponsor.

### 16.7 Success by absorption

If reference tools adopt:

- the semantic core;
- loss-report vocabulary;
- evidence model;
- context bundle;
- conformance profiles;

then UniSpec has succeeded even if users no longer install a separate UniSpec CLI.

---

## 17. Risk Register

| Risk | Early indicator | Mitigation | Contingency |
|---|---|---|---|
| UniSpec becomes another competing format | Users begin authoring in UniSpec only because adapters are weak | Native-authoritative default; adoption measured by imports and conformance | Narrow to libraries and conformance |
| Lowest-common-denominator model loses useful semantics | Large use of opaque namespaces or frequent loss reports | Keep core small; profiles and external contracts | Bilateral semantic profiles |
| Reference tools change faster than adapters | Compatibility lag exceeds 30 days | Version probes, thin adapters, maintainer relationships | Support fewer stable versions |
| Existing tools implement equivalent interoperability | Maintainers announce native exchange | Offer corpus, conformance, and governance assets | Contribute and sunset overlapping code |
| Certification becomes too expensive | Agent runs dominate budget | Tiered deterministic versus behavioral profiles | Certify behavior only for selected releases |
| LLM judges produce unstable semantic scores | High judge disagreement | Remove judges from pass/fail path | Human and executable adjudication only |
| Prompt injection causes unsafe agent action | Red-team escape or unauthorized tool use | Least privilege, sandboxing, trusted hooks, hidden tests | Disable mutation integration |
| Plugin compromise | Unsigned or overprivileged plugins proliferate | No public marketplace in v1; capabilities and signatures | Allowlisted first-party plugins only |
| Corpus licensing blocks publication | Contributors cannot authorize redistribution | Synthetic/public/private corpus tiers | Publish runners and private aggregate results |
| Evidence model creates false confidence | Users equate passing tests with proof | Explicit evidence levels and language | Remove “satisfied” terminology |
| Trace requirements create ceremony | Low-risk teams bypass the system | Risk-based profiles and quick mode | Make trace optional below R2 |
| Eight-person scope overload | Milestones slip by more than one sprint | Scope freeze and stage gates | Defer UI and secondary integrations |
| Funding shortfall | Runway drops below six months | Sponsorship and partner gates | Conformance-only scope |
| Vendor capture | One sponsor dominates TSC | Affiliation limits and public RFCs | Foundation transfer or governance fork |
| Benchmark gaming | Optimized adapters overfit public fixtures | Hidden tests, mutation tests, rotating corpus | Independent benchmark maintainers |
| Model/provider changes invalidate results | Sudden behavior regression | Exact run metadata and canaries | Mark reports expired or inconclusive |
| Enterprise buyers expect SaaS compliance | Requests focus on SOC 2 for local CLI | Distinguish OSS controls from hosted-operator controls | Partner with an enterprise distributor |
| Cross-repo model duplicates OpenSpec or vendor stores | Features converge | Define package and evidence interop only | Drop registry work |

---

## 18. Open Research Questions

1. Which semantic elements are truly common across SDD methodologies without creating a lowest-common-denominator model?
2. How should requirement identity survive major textual rewrites?
3. What forms of executable evidence most strongly support natural-language requirements?
4. How should contradictory evidence be accumulated and resolved?
5. Can semantic equivalence be tested reliably without LLM judges?
6. What benchmark-specific behavioral equivalence margins are practically measurable?
7. How should multi-agent disagreement and dissent be preserved?
8. How should policy and evidence packages federate across organizations?
9. Which R3 domains are sufficiently structured for reliable spec-as-source workflows?
10. How should context compaction quality be measured across models with different tokenization and tool-loading behavior?
11. How can private corpora participate in public conformance without exposing intellectual property?
12. When does traceability create useful accountability versus compliance theater?
13. How should old evidence decay when dependencies, environments, or external services change?
14. Which adapter behaviors can be generated from declarative mappings rather than custom code?

---

## 19. Immediate 30/60/90-Day Plan

### First 30 days

- Charter the project and governance process.
- Publish RFC-0001: problem, scope, terminology, and non-goals.
- Create the versioned ecosystem capability registry.
- Conduct at least 12 interviews.
- Obtain redistribution rights for at least 50 artifacts.
- Define corpus privacy tiers.
- Build two semantic-model prototypes.
- Complete initial path, parser, adapter, and injection threat models.
- Secure two provisional design partners.

### By day 60

- Complete 30+ interviews.
- Publish anonymized discovery findings.
- Complete OpenSpec↔USM↔Kiro and Spec Kit↔USM spikes.
- Measure semantic coverage and conversion loss.
- Draft USM v0.1 and UPF v0.1.
- Test TypeScript-only and native-core implementation options.
- Publish the first adapter contract.
- Build a 200-fixture prototype corpus.
- Obtain security and licensing counsel review.
- Confirm funding for the next nine months.

### By day 90

- Make the formal go, narrow, pivot, or stop decision.
- Open the public repository.
- Publish RFC-0002: semantic model.
- Publish RFC-0003: adapter and loss-report contract.
- Release an experimental `unispec inspect` and `unispec validate`.
- Demonstrate a no-op same-tool preservation test.
- Demonstrate one cross-tool conversion with a complete loss report.
- Publish the initial benchmark and conformance protocol.
- Begin design-partner use.

---

# Appendix A: Illustrative Human Projection

This is a projection of USM content, not the canonical data model.

```markdown
---
unispec_projection: "1.0"
package: "shop/cart"
authority: native-authoritative
change: "chg-cart-discount-001"
rigor: R2
risk: high
baseline: "sha256:..."
classification: internal
---

# Cart Discount Change

## Intent

Apply the configured percentage discount when a cart reaches the
threshold, before tax is calculated.

## Non-goals

- Stacking multiple percentage discounts
- Changing tax-jurisdiction rules
- Applying the discount to shipping charges

## Requirement REQ-CART-014 {#REQ-CART-014}

**Strength:** MUST

WHEN the eligible cart subtotal is greater than or equal to the
configured threshold, THE SYSTEM SHALL apply the configured
percentage discount before tax calculation.

### Scenario REQ-CART-014-S1: Exact threshold

GIVEN an eligible subtotal of $100.00  
AND a configured threshold of $100.00  
WHEN totals are calculated  
THEN the discount is applied  
AND tax is calculated using the discounted taxable amount.

### Constraint CON-CART-006

Discount calculation MUST use decimal arithmetic and the repository's
existing currency-rounding policy.

## Design DES-CART-009

Implements:

- REQ-CART-014
- CON-CART-006

Decision:

Reuse the existing pricing adjustment pipeline rather than adding a
second total-calculation path.

## Task TSK-CART-021

Implements: DES-CART-009

Expected code areas:

- `src/cart/pricing`
- `tests/cart`

Required evidence:

- exact-threshold test;
- below-threshold test;
- tax-ordering test;
- regression suite;
- approved commit.

## Evidence Status

| Subject | Status | Evidence |
|---|---|---|
| REQ-CART-014 | observed | Test mapping declared |
| CON-CART-006 | verified | Decimal-arithmetic policy check passed |
| TSK-CART-021 | pending | No commit-bound evidence recorded |
```

---

# Appendix B: Illustrative Adapter Manifest

```yaml
adapter:
  id: org.unispec.adapter.kiro
  version: 0.8.0
  protocol: 1

target:
  name: Kiro
  versions:
    tested:
      - "CLI 3.0 EA"
      - "IDE 2026.06"
    mode: explicit

capabilities:
  import:
    requirements: full
    scenarios: full
    design: full
    tasks: full
    bugfix: full
    quick_plan: full
    task_waves: partial
  export:
    requirements_first: full
    design_first: full
    bugfix: full
    quick_plan: partial
  preservation:
    comments: best-effort
    ordering: full
    unknown_frontmatter: opaque
  authority_modes:
    - native-authoritative
    - snapshot

known_losses:
  - feature: signed_approval_ledger
    handling: sidecar
  - feature: organization_policy_scope
    handling: emitted_as_steering_reference

security:
  execution: sandboxed
  network: denied
  filesystem: source-read-output-write

conformance:
  declared:
    - A0
    - A1
    - A2
    - A3
    - S1
```

---

# Appendix C: Proposed CLI

```text
unispec init
unispec inspect [path]
unispec detect
unispec import --from auto
unispec export --to <tool>
unispec validate
unispec diff <base> <target>
unispec loss-report
unispec trace query <id>
unispec trace coverage
unispec evidence record
unispec evidence verify
unispec policy evaluate
unispec gate check
unispec context compile --task <id> --target <agent>
unispec drift scan
unispec package build
unispec package verify
unispec adapter list
unispec adapter doctor
unispec conformance run
unispec serve --mcp --read-only
```

Example stable exit classes:

| Range | Meaning |
|---:|---|
| 0 | Success |
| 10–19 | Validation failure |
| 20–29 | Conversion or loss-policy failure |
| 30–39 | Trace or evidence failure |
| 40–49 | Policy or gate failure |
| 50–59 | Compatibility failure |
| 60–69 | Security refusal |
| 70–79 | Configuration failure |
| 80–89 | Internal or adapter failure |

---

# Appendix D: Required Loss Report Categories

```yaml
loss:
  dropped: []
  approximated: []
  inferred: []
  renamed: []
  reordered: []
  flattened: []
  split: []
  merged: []
  opaque_preserved: []
  generated_ids: []
  unsupported_relations: []
  unsupported_states: []
  unsupported_policies: []
  warnings: []
```

A conversion is not considered successful merely because an output file was generated.

---

# Appendix E: Founding Decisions

1. UniSpec is a federation and conformance layer.
2. Native authoring remains the default.
3. The semantic model is separate from Markdown.
4. One source is authoritative at a time.
5. Tool-specific data may be preserved opaquely but cannot be described as portable.
6. LLM judges cannot independently award certification.
7. Passing tests are evidence, not proof.
8. Governance records are append-only events.
9. MCP is an integration surface, not the UniSpec protocol.
10. Agent Skills and instruction files are primary portable distribution mechanisms.
11. Agent and tool support is capability-profiled and version-pinned.
12. The v1 core operates locally and offline.
13. Hosted registry and arbitrary-code marketplace are deferred.
14. Implementation language will be selected by Phase 0 evidence.
15. Security boundaries are enforced by permissions, sandboxing, and CI—not prompts.
16. Efficiency claims require pre-registration.
17. Conformance infrastructure remains public and free.
18. Foundation transfer is conditional on independent adoption.
19. Ecosystem absorption is a successful outcome.
20. Failure of the Phase 0 hypotheses results in a narrower project or cancellation.

---

**End of `framework.v3.md`**