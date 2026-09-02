# video.templatedesign — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/video.templatedesign/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "video.templatedesign",
  "status": "registered",
  "role": "TemplateDesignAgent (VA Domain Pack)",
  "allowed_tools": [],
  "allowed_plugins": [],
  "model_policy": {
    "provider": "local_deterministic",
    "model_id": "local-video-config-v1",
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
      "video.critic",
      "video.personalizationengineer",
      "video.ux",
      "video.crm"
    ],
    "outputs": [
      "video.judge"
    ]
  },
  "max_refinement_count": 0,
  "production_activation_requested": false,
  "does_not_own": [
    "Host credential storage",
    "Silent production activation without fail-closed gates",
    "Inventing action references for irreversible mutations",
    "Owning other agents' exclusive craft outputs without handoff contract",
    "Credentials",
    "Silent production activation",
    "Another agent's exclusive craft output without handoff",
    "Automatic promotion of self-generated artifacts",
    "Modification of safety, telemetry, gates, permissions, or corrigibility",
    "Self-granting tools, plugins, network, or isolation downgrades"
  ],
  "va_id": 89,
  "va_name": "TemplateDesignAgent",
  "va_category": "10-Sup",
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

# TemplateDesignAgent

> Self-contained VA Domain Pack agent on host common-agent-swarm-ops.
> Pack agent ID matches pure VA/generic taxonomy: `video.templatedesign`.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 89 |
| **pack_id** | `video.templatedesign` |
| **upstream_name** | TemplateDesignAgent |
| **category** | `10-Sup` |
| **domain_id** | `video` |
| **previous_common_id** | `video.thumbnail_designer` |
| **status** | `registered` |
| **maturity** | L0 / non-active |
| **taxonomy** | Pure VA Domain Pack (via generic pack agents) |
| **folder** | `business/video/agents/video.templatedesign/` |

## Responsibility

Designs reusable and safe personalization templates

Host role binding: `TemplateDesignAgent (VA Domain Pack)`. Design-time VA table content below is historical and non-binding for activation.

### Responsibility (from VA table)

Designs reusable and safe personalization templates

### Knowledge distillation sources (historical)

Variable-content design systems, dynamic layout rules, campaign template libraries

### Self-quality criteria (historical)

Merge-field robustness, layout stability, render survivability

### Surpass-human signal (historical)

Produces reusable templates with fewer breakages than manual design variants

### Critique bus (historical)

- **Accepts critique from:** PersonalizationEngineerAgent, UXAgent, CRMAgent

- **Comments on:** Fragile layouts, unsafe placeholder logic, merge collisions

### Tools design-time notes (historical, non-activating)

Template engines, design systems, schema validators

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

### Architecture pattern (historical)

ReAct on template schemas and render constraints

## Boundaries and escalation

- Fail-closed: no provider activation, no network, no credentials from design text.
- `production_activation_requested` remains false unless a separate human gate changes it.
- Escalates legal, safety, rights, and release decisions to required human gates.
- Critique lead / judge defaults use VA IDs `video.critic` and `video.judge`.

## Inputs and outputs

- Inputs: local pack artifacts and typed handoffs.
- Outputs: reviewable video-domain deliverables with acceptance criteria.
- Acceptance: host policy plus local SPEC criteria; no external repository required.

## Quality and critique

- Prompt reference: `video.prompt.templatedesign.v1`
- Rubric reference: `video.rubric.templatedesign.v1`
- Critique edges: `{"inputs": ["video.critic"], "outputs": ["video.judge"]}`
- Max refinement: `3`
- VA table quality criteria retained under Provenance and Identity surface above.

## Runtime binding

Authoritative fail-closed host configuration:

```json
{
  "agent_id": "video.templatedesign",
  "allowed_tools": [],
  "budget_policy": {
    "max_input_tokens": 2048,
    "max_output_tokens": 1024,
    "max_tool_requests": 0
  },
  "critique_edges": {
    "inputs": [
      "video.critic"
    ],
    "outputs": [
      "video.judge"
    ]
  },
  "max_refinement_count": 3,
  "model_policy": {
    "model_id": "local-video-config-v1",
    "network_access": false,
    "provider": "local_deterministic"
  },
  "production_activation_requested": false,
  "prompt_reference": "video.prompt.templatedesign.v1",
  "role": "TemplateDesignAgent (VA Domain Pack)",
  "rubric_reference": "video.rubric.templatedesign.v1",
  "schema_version": "1.0",
  "status": "registered",
  "va_id": 89,
  "va_name": "TemplateDesignAgent",
  "va_category": "10-Sup"
}
```

## Local knowledge sources

- [Runtime binding](agent_spec.json)
- [Folder README](README.md)
- [Provenance](sources/PROVENANCE.json)
- [Mapping note](sources/MAPPING.md)
- [Pack inventory](../../inventory.json)
- [Pack manifest](../../manifest.json)
- All required primary references resolve inside this repository.

## Provenance

- Pack agent ID `video.templatedesign` is aligned to pure VA Domain Pack / generic pack taxonomy (Agent IDs ≈ VA tables).
- Previous common inventory ID `video.thumbnail_designer` is historical mapping only.
- Upstream design body below is **historical and non-binding**; local `agent_spec.json` is authoritative.
- Full VA/generic SPEC depth retained for offline design fidelity (including category roster rows and common agent structure when present upstream).

### VA Domain Pack specification body (historical and non-binding)

```text
TemplateDesignAgent

> **Self-contained agent definition** for host `upstream-generic-pack`. Body text is embedded from in-pack corpus and upstream-va-design when available. Do not require external repos to understand this agent.

Identity

| Field | Value |
|-------|-------|
| **va_id** | 89 |
| **pack_id** | `video.templatedesign` |
| **category** | `10-Sup` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.templatedesign/` |

Category roster section (full, from agents.md)

_The following is the complete category section from the master roster (includes peers in the same craft category)._


10. Workflow Support Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 81 | **AnalystAgent** | Aggregates business, creative, and technical performance telemetry into decision-ready reports | Platform analytics dashboards; experiment logs; evaluation-harness outputs; benchmark histories | KPI completeness; forecast-vs-actual variance within tolerance; insight-to-action turnaround | Detects actionable performance shifts faster than human analyst rotations | SocialMediaStrategistAgent, PerformanceMarketerAgent, EvaluationHarnessAgent | Campaign pacing, release timing, retention and ROAS anomalies | YouTube Analytics, Meta/TikTok Ads dashboards, BI warehouse, benchmark logs | ReAct over telemetry + regression analysis |
| 82 | **AudienceSimAgent** | Simulates audience preference, engagement, and drop-off | Pairwise preference datasets; retention studies; audience segmentation models | Preference stability across cohorts; retention-prediction accuracy; disagreement logging | Predicts audience reaction earlier than conventional test-screen cycles | DirectorAgent, EditorAgent, AnalystAgent, JudgeAgent | Hooks, pacing, clarity, emotional fit, trailer strength | Persona simulators, pairwise evaluation harness, retention models | LLM-as-Judge + pairwise preference panel |
| 83 | **AccessibilityAgent** | Owns final accessibility acceptance before release | WCAG 2.2, captioning and AD guidelines, Deaf/HoH review frameworks | Caption accuracy, AD completeness, contrast compliance, release-readiness | Finds release-blocking accessibility issues before human audits do | AccessibilityOptimizerAgent, EditorAgent, ColoristAgent, SoundMixerAgent | Caption sync, contrast issues, missing AD or sign-language layers | Caption validators, contrast analyzers, AD review tools | Constitutional AI with accessibility constitution |
| 84 | **BrandAgent** | Enforces brand voice, claims boundaries, and visual consistency | Brand books, approved campaigns, legal claim guardrails, tone guides | Brand-voice similarity, policy adherence, low deviation across assets | Holds cross-channel brand consistency better than fragmented human review | CopywriterAgent, MotionGraphicsAgent, MarketingAgent, BrandStrategistAgent | Voice drift, visual inconsistency, claim creep | Brand asset library, embedding similarity, style guides | Self-Refine against brand constitution |
| 85 | **BrandStrategistAgent** | Defines audience-value framing and positioning before script and campaign execution | Positioning frameworks, campaign strategy decks, market research, brand architecture docs | Strategy coherence, differentiation strength, audience-message clarity | Produces clearer brand-to-script translation than ad hoc human handoffs | BrandAgent, ScreenwriterAgent, MarketingAgent | Positioning gaps, weak value proposition, misaligned audience framing | Research decks, messaging frameworks, strategy templates | Multi-agent debate with BrandAgent and CreativeDirectorAgent |
| 86 | **MarketingAgent** | Packages content for launch, promotions, and release sequencing | Campaign playbooks, launch calendars, media plans, asset packaging requirements | Metadata completeness, asset readiness, launch sequencing accuracy | Ships multi-channel launch packages faster than manual campaign ops | SocialMediaStrategistAgent, SEOAgent, CopywriterAgent, TrailerEditorAgent | Missing formats, weak rollout timing, incomplete promotion sets | Campaign management suites, metadata tools, release planners | ReAct over launch checklists and channel requirements |
| 87 | **SEOAgent** | Optimizes discoverability through titles, descriptions, metadata, and search intent | Search ranking studies, video metadata best practices, keyword taxonomies | Keyword fit, metadata completeness, search-intent match | Lifts discoverability faster than manual metadata tuning | MarketingAgent, CopywriterAgent, AnalystAgent | Weak keywords, poor title-description fit, metadata omissions | Keyword tools, metadata APIs, ranking dashboards | ReAct with search-intent validation |
| 88 | **CommunityAgent** | Captures community response and triages qualitative signals | Community moderation playbooks, sentiment datasets, escalation rules | Response latency, issue clustering quality, sentiment tracking accuracy | Surfaces emerging audience concerns earlier than manual comment review | AnalystAgent, SocialMediaStrategistAgent, CommsAgent | Confusing messaging, sentiment risks, recurring complaints | Social listening tools, moderation dashboards, clustering models | Reflexion from post-launch audience feedback |
| 89 | **TemplateDesignAgent** | Designs reusable and safe personalization templates | Variable-content design systems, dynamic layout rules, campaign template libraries | Merge-field robustness, layout stability, render survivability | Produces reusable templates with fewer breakages than manual design variants | PersonalizationEngineerAgent, UXAgent, CRMAgent | Fragile layouts, unsafe placeholder logic, merge collisions | Template engines, design systems, schema validators | ReAct on template schemas and render constraints |
| 90 | **UXAgent** | Reviews clarity and usability of personalized or interactive outputs | UX heuristics, accessibility criteria, usability testing patterns | Readability, friction-point detection, user-flow clarity | Flags user confusion earlier than launch-stage support teams | TemplateDesignAgent, PersonalizationEngineerAgent, AccessibilityAgent | Confusing flows, readability issues, weak interaction cues | UX review checklists, session replay, readability tools | LLM-as-Judge with UX rubric |
| 91 | **TrustSafetyAgent** | Screens outputs for impersonation, abuse, or harmful misuse | Abuse-taxonomy corpora, impersonation cases, policy rulebooks | Policy hit rate, abuse-risk recall, low false negatives on blocked cases | Catches misuse risk earlier than generic moderation queues | ComplianceAgent, DeepfakeDetectionAgent, SafetyRedTeamAgent | Harmful misuse pathways, impersonation vectors, policy gaps | Safety classifiers, abuse taxonomy DB, moderation APIs | Constitutional AI for trust-and-safety policy enforcement |
| 92 | **CRMAgent** | Delivers audience-targeted or trigger-based campaigns through CRM systems | CRM automation flows, lifecycle marketing playbooks, audience segmentation rules | Audience-segment correctness, delivery readiness, trigger accuracy | Executes segmentation-to-delivery flow faster than manual ops | PersonalizationEngineerAgent, TemplateDesignAgent, AnalystAgent | Wrong segmentation, broken trigger timing, incomplete CRM payloads | HubSpot/Salesforce-style CRM APIs, segmentation tools | ReAct over trigger and audience schemas |
| 93 | **LegalAgent** | Performs final legal review for novel or high-risk publication issues | Media law references, clearance workflows, defamation/IP/privacy cases | Issue identification recall, sign-off completeness, escalation quality | Reduces late-stage legal surprises relative to fragmented legal review | ComplianceAgent (Legal), JournalistAgent, ProducerAgent / EP, MPAAgent | Novel legal risks, unclear rights, unresolved high-risk claims | Legal memo systems, rights trackers, clearance databases | Human-in-the-loop escalation + constitutional review |
| 94 | **FestivalStrategistAgent** | Positions projects for festivals and submission calendars | Festival submission guides, award-season strategies, selection histories | Fit-to-festival strength, package readiness, timing discipline | Improves submission targeting versus generic release planning | ProducerAgent / EP, DirectorAgent, CriticAgent | Weak positioning, mistimed submission plans, incomplete packages | Festival calendars, submission checklists, press-kit trackers | ReAct with calendar and package validation |
| 95 | **CriticAgent** | Simulates reviewer, press, or jury interpretation | Criticism corpora, festival-jury commentary, review archives | Interpretive depth, consistency, reviewer-mode diversity | Provides broader qualitative coverage than ad hoc internal taste review | DirectorAgent, AudienceSimAgent, FestivalStrategistAgent, JudgeAgent | Auteur read, tone mismatch, festival/press vulnerability | Review corpora, jury rubrics, qualitative scoring tools | Multi-agent debate as critic panel |
| 96 | **LMSAgent** | Packages and deploys learning content to LMS environments | SCORM/xAPI standards, LMS publishing workflows, completion-tracking schemas | Package validity, tracking integrity, deploy success rate | Ships publishable learning packages faster than manual course ops | InstructionalDesignAgent, AccessibilityAgent, LearnerSimAgent | Package compliance, tracking errors, learning-objective mismatch | LMS APIs, SCORM/xAPI validators, course packaging tools | ReAct over LMS deployment schema |
| 97 | **LearnerSimAgent** | Simulates learner behavior, confusion points, and assessment performance | Learner-modeling datasets, completion analytics, quiz outcome patterns | Friction-point prediction, completion accuracy, simulated quiz realism | Predicts weak spots before live learner complaints emerge | InstructionalDesignAgent, LMSAgent, AnalystAgent | Confusing content, weak assessments, low-completion pathways | Learner simulation models, assessment predictors, LMS data | Audience-style simulation adapted for learning outcomes |
| 98 | **ContinuityAgent** | Maintains continuity across character, prop, wardrobe, environment, and time-state | Continuity logs, script supervisor practices, asset manifest state tracking | State-drift detection, scene-to-scene consistency, manifest update correctness | Catches continuity breaks earlier than end-of-post review | CostumeDesignAgent, MUAAgent, AIQAConsistencyAgent, CinematographerAgent (DoP), GateKeeperAgent | Character-state drift, wardrobe and prop mismatch, time logic errors | State manifests, shot comparison tools, continuity DB | Tool-use / ReAct with continuity manifest enforcement |
| 99 | **LipSyncAgent** | Validates and refines phoneme-viseme alignment as a dedicated gate | Lip-sync research, animation timing references, viseme datasets | Sync error below threshold, correction specificity, low false positives | Finds sync drift more precisely than general QC review | VoiceCloneAgent / LipSyncSpecialist, AnimatorAgent, AIQAConsistencyAgent | Mouth-shape mismatch, frame drift in dialogue, correction priority | Phoneme-viseme aligners, frame-level sync tools | Self-Refine around sync validator outputs |
| 100 | **MusicSupervisorAgent** | Manages music fit, cue usage, rights awareness, and soundtrack packaging | Music supervision notes, cue placement references, soundtrack release practice | Cue suitability, rights-awareness coverage, soundtrack-package completeness | Coordinates music placements more consistently than fragmented handoffs | ComposerAgent, TrailerEditorAgent, LabelA&RAgent, LegalAgent | Cue misuse, music-rights ambiguity, soundtrack cohesion issues | Music asset trackers, cue sheets, soundtrack package tools | ReAct over cue sheets and rights requirements |
| 101 | **LabelA&RAgent** | Represents label and artist direction for music-specific workflows | A&R playbooks, label release notes, artist brief archives | Artist-fit quality, release positioning, feedback turnaround | Aligns music creative faster than disconnected stakeholder threads | MusicVideoDirectorAgent, MusicSupervisorAgent, LabelDigitalAgent | Artist-direction drift, release mismatch, packaging weakness | Repertoire systems, release trackers, artist brief tools | Multi-agent debate with music stakeholders |
| 102 | **LabelDigitalAgent** | Runs label-side digital rollout, metadata, and channel packaging | Digital music release operations, metadata schemas, distribution platform requirements | Metadata completeness, rollout timing, channel readiness | Delivers cleaner label-side packages than ad hoc release ops | MusicVideoDirectorAgent, SocialMediaStrategistAgent, MarketingAgent | Missing metadata, release timing issues, asset-version confusion | Digital release systems, channel dashboards, metadata tools | ReAct on release package requirements |
| 103 | **DeepfakeDetectionAgent** | Detects synthetic identity, voice, and provenance deception risks | Deepfake forensics corpora, synthetic-media benchmarks, identity-risk studies | Forensic recall, false-negative control, provenance-validation accuracy | Catches deceptive synthetic markers that generic QC misses | AvatarDesignAgent, VoiceCloneAgent, TrustSafetyAgent, SafetyRedTeamAgent | Identity anomalies, provenance holes, deceptive synthesis patterns | Forensic models, face/voice anomaly detectors, provenance validators | Tool-use / ReAct with forensic scoring |
| 104 | **CommsAgent** | Coordinates external messaging, disclosure, and public-response posture | Crisis communication guides, disclosure standards, PR playbooks | Message consistency, disclosure completeness, escalation quality | Produces faster aligned responses than fragmented stakeholder messaging | MarketingAgent, CommunityAgent, LegalAgent, BrandAgent | Disclosure gaps, inconsistent external messaging, weak response framing | Comms calendars, approval workflows, response templates | ReAct with approval chains |
| 105 | **ArchiveProducerAgent** | Packages archival materials and source assets for reuse-heavy or documentary workflows | Archive production notes, source curation practices, provenance preservation standards | Source package completeness, rights coverage, provenance preservation | Assembles reusable archival packages more cleanly than manual gather-and-sort workflows | ArchiveResearchAgent, JournalistAgent, LegalAgent | Missing archival context, weak source packaging, rights gaps | Archive asset managers, metadata systems, provenance logs | ReAct over archival manifests |
| 106 | **StandardsEditorAgent** | Enforces editorial standards, sourcing discipline, and corrections policy | Newsroom standards manuals, corrections policies, attribution standards | Standards-compliance rate, attribution accuracy, corrections readiness | Reduces standards drift better than late-stage copy edits | JournalistAgent, FactCheckerAgent, CorrectionsAgent, LegalAgent | Weak attribution, standards violations, correction policy gaps | Editorial checklists, attribution validators, standards DB | Constitutional AI with editorial standards constitution |
| 107 | **EthicsAgent** | Reviews ethical risk, disclosure sufficiency, fairness, and social impact | Ethics frameworks, synthetic-media disclosure guidance, fairness audits | Ethical issue recall, mitigation clarity, escalation precision | Surfaces release risks earlier than reactive ethics review | StandardsEditorAgent, ComplianceAgent (Legal), TrustSafetyAgent, SafetyRedTeamAgent | Disclosure insufficiency, fairness concerns, sensitive-content risk | Ethics review templates, risk matrices, disclosure checklists | Multi-agent debate + constitutional review |
| 108 | **ChannelManagerAgent** | Manages episodic or platform channel operations for cadence and metadata readiness | Channel publishing playbooks, metadata standards, scheduling ops | Publishing readiness, cadence stability, metadata completeness | Improves publishing discipline over manual channel operations | SocialMediaStrategistAgent, SEOAgent, AnalystAgent, MarketingAgent | Release readiness gaps, metadata omissions, schedule slippage | CMS/channel dashboards, scheduler tools, metadata validators | ReAct with publishing runbooks |
| 109 | **CorrectionsAgent** | Coordinates post-publication fixes and correction disclosures | Corrections workflows, retraction and update policies, version tracking | Correction turnaround, version replacement accuracy, notice completeness | Resolves post-release issues faster than unstructured incident handling | StandardsEditorAgent, FactCheckerAgent, ChannelManagerAgent | Unclosed correction loops, incomplete notices, stale versions | Version-control systems, publishing tools, correction trackers | ReAct over correction and replacement workflows |
| 110 | **MPAAgent** | Prepares rating-related packaging and release-readiness inputs for feature workflows | Rating submission references, content advisories, theatrical packaging rules | Rating-package completeness, advisory clarity, escalation quality | Prepares cleaner feature-release classification packages than manual prep | ProducerAgent / EP, LegalAgent, EthicsAgent | Missing advisories, incomplete rating prep, unclear classification support | Submission packages, advisory templates, classification checklists | Human-in-the-loop with structured packaging support |
| 111 | **SalesAgent** | Handles buyer-facing sales packaging for distributors and outlets | Rights windowing playbooks, market package examples, buyer materials | Buyer-package completeness, rights clarity, market-fit packaging | Produces sales-ready release packets faster than manual assembly | ProducerAgent / EP, DistributorAgent, MarketingAgent | Missing buyer info, weak positioning, incomplete rights summaries | Rights systems, package builders, buyer CRM | ReAct over buyer package requirements |
| 112 | **DistributorAgent** | Manages downstream delivery to buyers, platforms, and territories | Distribution specs, outlet requirements, package handoff workflows | Outlet-spec compliance, handoff completeness, territorial routing accuracy | Reduces delivery-spec mismatches relative to fragmented delivery ops | SalesAgent, ArchiveMasterAgent, SoundMixerAgent, ColoristAgent | Spec mismatches, incomplete outlet packages, routing errors | Delivery management systems, outlet spec DB, packaging validators | ReAct over distribution specification matrices |
| 113 | **AwardsStrategistAgent** | Plans awards submissions and campaign timing | Awards calendars, campaign playbooks, category positioning histories | Submission readiness, category fit, timeline precision | Improves awards-timing discipline over generic release planning | ProducerAgent / EP, CriticAgent, MarketingAgent | Weak campaign timing, poor category fit, incomplete submission assets | Awards calendars, campaign trackers, submission checklists | ReAct with awards timeline optimization |
| 114 | **ArchiveMasterAgent** | Produces archive-grade masters and preservation packages | Preservation standards, checksum workflows, archive metadata practice | Checksum integrity, preservation metadata completeness, archive package validity | Delivers more reliable archive packages than late-stage export-only workflows | DistributorAgent, ColoristAgent, SoundMixerAgent, GateKeeperAgent | Incomplete preservation bundles, archive-spec violations, metadata gaps | Archive mastering tools, checksum utilities, preservation metadata systems | Tool-use / ReAct with preservation validation |

---


Responsibility

Designs reusable and safe personalization templates

Knowledge distillation sources

Variable-content design systems, dynamic layout rules, campaign template libraries

Self-quality criteria

Merge-field robustness, layout stability, render survivability

Surpass-human signal

Produces reusable templates with fewer breakages than manual design variants

Critique bus

- **Accepts critique from:** PersonalizationEngineerAgent, UXAgent, CRMAgent

- **Comments on:** Fragile layouts, unsafe placeholder logic, merge collisions

Tools (design-time documentation)

Template engines, design systems, schema validators

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

Architecture pattern

ReAct on template schemas and render constraints

Common structure of an AI agent (full §11 from agents.md)

11. Common Structure of an AI Agent

Every agent — regardless of category — implements this skeleton. Derived from the source document's architecture patterns (§1), critique protocol (§6), and universal success-criteria framework (§5), enriched with current (2026) tooling research.

11.1 Architecture Diagram

The diagram below presents the common agent as a professional operating architecture rather than a simple component sketch. It shows how **orchestration**, the **input contract**, **knowledge and tool surfaces**, the internal **plan → act → self-review** loop, **traceability and provenance controls**, the **3-layer quality gate** (Spec → Rubric → Preference), **release packaging**, **peer critique**, **human escalation**, and **continuous improvement** work together as one governed system.

![Professional common AI agent architecture diagram](./common-agent-structure.svg)

> **Tip:** view the diagram fullscreen on GitHub by clicking it, or download [`common-agent-structure.svg`](./common-agent-structure.svg) directly. The SVG is designed as a presentation-grade reference for architecture reviews and implementation planning.

11.2 Component Reference Table

| # | Component | Purpose | Mechanism / Implementation Notes |
|---|---|---|---|
| 1 | **Identity** | Stable unique handle for routing, logging, provenance | Kebab-case ID + semantic version (e.g. `director-agent@2.1.0`). Registered in the agent-capability registry used by RouterAgent. |
| 2 | **Responsibility (Scope)** | Single-sentence definition of what the agent owns | Mirrors a human craft role. Prevents scope overlap via explicit boundary documented in the registry. |
| 3 | **Knowledge Distillation Source** | Licensed/consented corpora the agent is trained or RAG-grounded on | Award archives, academic papers, expert interviews, peer-reviewed journals. Refreshed via Continuous Distillation Loop (§7 of source). |
| 4 | **Tool Access** | External APIs, generators, validators, DCC bridges | Video gen: Sora 2, Veo 3.1 (Gemini API), Runway Gen-4/Aleph, Kling 3.0. Voice: ElevenLabs v3, Sync.so, HeyGen. DCC: Resolve/Nuke/AE via MCP bridges. All accessed via MCP (Model Context Protocol, Anthropic 2024). |
| 5 | **Architecture Pattern** | Reasoning/learning loop powering the agent | One or more of: Self-Refine [1], Reflexion [2], RLAIF/Constitutional AI [3], Multi-agent debate [4], LLM-as-Judge [5], Pairwise preference (Arena) [5], ReAct [6], Agentic Graph (LangGraph/CrewAI/AutoGen) [7], DSPy/OPRO prompt optimization [8]. |
| 6 | **Memory** | Episodic + long-term project memory | Vector DB (Pinecone/Weaviate/Qdrant) accessed via MemoryAgent. Implements MemGPT-style hierarchical memory with summarization and eviction. Reflexion agents store verbal self-feedback here. |
| 7 | **Constitution / Rubric** | Written, role-specific scoring guide for self-check | Examples: Murch's Rule of Six (Editor), 12 Principles (Animator), Save-the-Cat beats (Screenwriter), WCAG 2.2 (Accessibility), FAA Part 107 (Drone), SAG-AFTRA AI rider (Consent). Used as the "constitution" in Constitutional AI pattern. |
| 8 | **Self-Quality: L1 Spec** | Did the output meet the structured brief? | JSON schema validation + tool validators (codec, LUFS, aspect ratio, frame count, file format). Must pass 100%. |
| 9 | **Self-Quality: L2 Rubric** | Does it meet craft rubric for this role? | LLM-as-Judge (Zheng 2023) with role-specific constitution. Must score ≥85/100. Up to 3 Self-Refine iterations if below threshold. |
| 10 | **Self-Quality: L3 Preference** | Would target audience choose this over human baseline? | Pairwise comparison: AudienceSim panel (≥200 simulated personas + ≥20 HiTL samples). Win rate ≥50% (parity) or ≥55% (surpass). |
| 11 | **Surpass-Human Signal** | Pre-registered proof the agent exceeds a credentialed professional | Benchmark dominance; blind Arena preference ≥55%; speed × quality (equal L2 at ≤10% turnaround); lower 90-day defect rate; certification pass; higher novelty at equal quality. |
| 12 | **Critique Inbox** | Channel for receiving structured feedback from peers | Shared `CritiqueMessage` JSON bus. Severities: blocker (halts DAG), major (Self-Refine ≤3 iters), minor/nit (logged for RLAIF). Disputes → JudgeAgent multi-agent debate → HiTL if unresolved. |
| 13 | **Critique Outbox** | Peer agents whose work this agent is qualified to review | Defined per-agent in roster. Messages emitted on same bus. Evidence-backed, rubric-referenced, appended to C2PA provenance. |
| 14 | **HiTL Escalation** | When a human must be brought in | Consent (SAG-AFTRA AI rider, EU AI Act Art. 50); final legal sign-off; MPA rating; festival eligibility; crisis comms; cross-cultural sensitivity. |
| 15 | **Provenance (C2PA)** | Cryptographic signing of every artifact | Every emitted artifact signed with C2PA (c2patool). Downstream agents verify chain. Accepted critiques appended to manifest. Platforms (YouTube, TikTok, Meta) auto-label based on C2PA presence. |
| 16 | **Continuous Learning** | How the agent keeps improving post-deployment | Bootstrap (licensed corpora) → Expert interviews (paid, consented) → Live RLAIF (DPO/KTO) → Award-rubric grounding → Adversarial red-team → 30/60/90-day reality check (retention, ROAS, awards). |
| 17 | **Orchestration Integration** | How the agent fits the multi-agent graph | Registered as a node in LangGraph/CrewAI/AutoGen DAG. OrchestratorAgent schedules; PlannerAgent assigns; RouterAgent selects model/provider; GateKeeperAgent verifies L1-L3 before advancing. |

CritiqueMessage Schema (Universal)

'''json
{
  "critique_id": "uuid",
  "from_agent": "EditorAgent",
  "to_agent": "DirectorAgent",
  "artifact_ref": "shot_42_take_3.mp4",
  "severity": "blocker | major | minor | nit",
  "category": "pacing | continuity | accuracy | compliance | accessibility | brand | craft",
  "evidence": ["timecode 00:01:14 — held 1.4s past cut point per genre prior"],
  "suggested_action": "trim 1.0s; re-evaluate hold",
  "rubric_reference": "Murch Rule of Six §3",
  "must_resolve_before": "phase_4_review"
}
'''

Composition Diagram

'''text
[Brief] ──► PlannerAgent ──► OrchestratorAgent ──► RouterAgent ──► (52 craft agents §1–§8)
                 ▲                  │                                       │
                 │                  ▼                                       ▼
             MemoryAgent      GateKeeperAgent ◄─── JudgeAgent ◄──── CritiqueMessages
                                    ▲                                       ▲
                                    │                                       │
            [Creative meta:] IdeationAgent · NarrativeArcAgent · StyleTransferAgent · MoodBoardAgent · NoveltyAgent · EmotionalArcAgent
            [Research meta:] WebResearchAgent · ArchiveResearchAgent · TrendIntelAgent · CompetitorIntelAgent · CitationAgent · InterviewSynthAgent · BenchmarkResearchAgent
            [Optimization meta:] PromptOptimizerAgent · CostOptimizer · LatencyOptimizer · RetentionOptimizer · ROASOptimizer · AccessibilityOptimizer · EvalHarnessAgent · SafetyRedTeamAgent
'''

---

Shared references (from agents.md §12)

12. References

Foundational Papers (Architecture Patterns)

| Ref | Paper | Key Contribution | Link |
|---|---|---|---|
| [1] | Madaan et al., "Self-Refine: Iterative Refinement with Self-Feedback," NeurIPS 2023 | Agent drafts → self-critiques against rubric → revises iteratively without weight updates | [arXiv:2303.17651]([historical-url] |
| [2] | Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning," NeurIPS 2023 | Verbal self-reflection stored in episodic memory buffer to improve decisions in subsequent trials | [arXiv:2303.11366]([historical-url] |
| [3] | Bai et al., "Constitutional AI: Harmlessness from AI Feedback," 2022 | Reward signal from AI critic governed by a written constitution; RLAIF without human labels | [arXiv:2212.08073]([historical-url] |
| [4] | Du et al., "Improving Factuality and Reasoning in Language Models through Multiagent Debate," 2023 | Multiple LLM agents debate; improves factuality and reasoning across tasks | [arXiv:2305.14325]([historical-url] |
| [5] | Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," NeurIPS 2023 | GPT-4 judge achieves >80% agreement with human preferences; scalable evaluation | [arXiv:2306.05685]([historical-url] |
| [6] | Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models," ICLR 2023 | Interleaving reasoning traces with tool-use actions for grounded decision-making | [arXiv:2210.03629]([historical-url] |
| [7] | LangGraph / CrewAI / AutoGen (2024–2026) | Agentic graph orchestration: DAG with state, handoffs, review gates, human-in-the-loop | [LangGraph]([historical-url] [CrewAI]([historical-url] [AutoGen]([historical-url] |
| [8] | Yang et al., "Large Language Models as Optimizers" (OPRO), 2023; Khattab et al., DSPy (Stanford, 2023–2026) | Meta-optimization of prompts using LLMs; DSPy compiles declarative LM programs into optimized pipelines | [OPRO arXiv:2309.03409]([historical-url] [DSPy]([historical-url] |

Evaluation Benchmarks

| Benchmark | Scope | Link |
|---|---|---|
| VBench / VBench 2.0 | Video generation quality — 16 dimensions (temporal + frame-wise); VBench 2.0 adds Human Fidelity, Creativity, Physics | [arXiv:2311.17982]([historical-url] [VBench 2.0: arXiv:2503.21755]([historical-url] |
| EvalCrafter | Text-to-video — 18 metrics across visual, content, motion quality | [arXiv:2310.11440]([historical-url] |
| MT-Bench / Chatbot Arena | LLM output quality via pairwise human + LLM-judge evaluation | [arXiv:2306.05685]([historical-url] |

Generative Video Models (Tool Access — 2026 landscape)

| Model | Provider | Key Capabilities | Access |
|---|---|---|---|
| Sora 2 / Sora 2 Pro | OpenAI | Synchronized dialogue + SFX + background audio; cinematic/realistic/anime styles; 1080p 20s | [OpenAI Videos API]([historical-url] (discontinuing Sept 2026) |
| Veo 3.1 | Google DeepMind | 4K / 1080p / 720p, 8s; native audio; configurable 16:9 & 9:16; multi-image reference for character/object direction | [Gemini API]([historical-url] / [Vertex AI]([historical-url] |
| Runway Gen-4 / Gen-4.5 / Aleph | Runway | ControlNet guides, camera paths, style-lock, Layout Sketch; Aleph for video-to-video editing | [Runway API]([historical-url] |
| Kling 3.0 | Kuaishou | Cinematic motion realism; physics accuracy; motion-control (reference video); native audio | [Kling API (fal.ai)]([historical-url] |

Voice & Avatar Tools (2026)

| Tool | Provider | Capabilities |
|---|---|---|
| ElevenLabs v3 | ElevenLabs | Expressive TTS; instant/professional voice cloning; dialogue mode (multi-speaker); Projects API for long-form; Sound FX generation | [Docs]([historical-url] |
| HeyGen Avatar IV | HeyGen | Photoreal AI avatars; 175+ languages lip-sync; ElevenLabs integration; personalization API | [HeyGen]([historical-url] |
| Synthesia | Synthesia | Enterprise AI avatars at scale; SCORM-compatible; brand-controlled | [Synthesia]([historical-url] |
| Sync.so / Wav2Lip | Open-source + API | Lip-sync overlays; phoneme-viseme alignment | [Sync.so]([historical-url] |

Infrastructure Standards

| Standard | Purpose | Status (2026) |
|---|---|---|
| C2PA (Content Provenance) | Cryptographic manifest signing for every AI-generated artifact; platforms (YouTube, TikTok, Meta) auto-label | EU AI Act Code of Practice (March 2026) mandates C2PA + watermarking combined. Over 2,300 tools support. [contentauthenticity.org]([historical-url] |
| MCP (Model Context Protocol) | Open standard for LLM ↔ tool integration; 2,300+ public servers; adopted by Claude, VS Code, Cursor, etc. | Donated to Agentic AI Foundation (Linux Foundation, Dec 2025) by Anthropic + OpenAI + Block. [modelcontextprotocol.io]([historical-url] |
| DSPy | Framework for programming (not prompting) LLMs; compiles declarative pipelines into optimized prompts/finetunes | Stanford-maintained; MIPRO optimizer; used by PromptOptimizerAgent for automated prompt improvement. [github.com/stanfordnlp/dspy]([historical-url] |

---

*Generated: May 2026. Source: [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md). Core layout restored from `agents_old.md`; missing workflow-support content merged into the same table-driven structure.*

Deep specifications (full embedded content)


Document: `study/coding_agent_functional_specification.md`

_Embedded from `corpus/study/coding_agent_functional_specification.md`. Also stored at `sources/study/coding_agent_functional_specification.md` under this agent folder._


task.md – Final Specification for "N1ch01as Architect v1.0" (Harness-Engineered AGI Meta-System Builder – Local Install Edition with Guided Requirement Discovery + IT Professional Delegation Model + Embedded Task Brief Template + Hermes-Agent Closed Learning Loop + Agent Lightning Tracing & Trainer/Optimizer + Claude Code Core Skills: Superpowers, GSD, gstack + Meta-Harness Outer-Loop Optimization)

**Version:** v1.0 (OpenAI Harness Engineering + OpenClaw persistent identity + Karpathy Autoresearch ratchet logic + Guided Requirement Discovery + IT Professional Delegation Model + Embedded Standardized Task Brief Template + Hermes-Agent Closed Learning Loop, Skills System, Persistent Memory with Nudges, Sub-Agent Spawning, Hierarchical AGENTS.md Discovery + Agent Lightning Tracing, LightningStore, Phase Summaries, Trainer/Optimizer Loop + Pre-loaded Claude Code Core Skills: Superpowers, GSD, gstack + Meta-Harness Outer-Loop Harness Optimization arXiv:2603.28052)
**Date:** 1 April 2026
**Purpose:** This is the **SINGLE SOURCE OF TRUTH** document that any coding agent (or human developer) must follow to implement the complete, production-grade, no-code "N1ch01as Architect" tool.

The generated tool allows a user who is in a helpless/vague state (they know they need to build something for business/client reasons but lack words to describe it) to receive a fully working, production-ready backend + frontend + tests + docs — with **zero manual code ever written by humans**. All installation and running is done via local package managers and standard development tools (no Docker, no containerization, no containers of any kind).

The N1ch01as Architect itself is an **AGI-like thinking agent** that uses:

- **Harness Engineering** (from OpenAI): "Humans steer. Agents execute." The repository is the system of record. No manually-written code. Agents generate everything (code, tests, linters, CI, docs, observability). The primary job of the Orchestrator is to scaffold environments, enforce invariants, and manage feedback loops so agents can reliably self-improve.
- **OpenClaw Identity:** Persistent "soul" + Thinking Clock idle cognition → proactive, opinionated, first-principles architect.
- **Karpathy Ratchet:** Autonomous experimental loop → hypothesize one atomic improvement → bounded change → evaluate → keep ONLY if strictly better → repeat forever.
- **Guided Requirement Discovery:** Users often have no idea how to articulate needs. The system must proactively lead them with a few KEY background questions, suggest a small curated list of template solutions, let them choose, ask 2–3 targeted follow-ups, then synthesize a fully customized polished requirement for explicit confirmation. This prevents user burnout and turns vague intent into production-grade requirements.
- **IT Professional Delegation Model:** The Orchestrator always pretends to be a **professional IT Project Manager / Senior Architect**. It plans, researches, designs, and **instructs/controls a dedicated Coding Agent** (and other agents) to generate code in a structured delegation style — exactly like a real IT professional managing a development team. The Orchestrator gives clear task briefs, reviews output, requests fixes if needed, runs quality gates, and only accepts code after everything passes.
- **Embedded Standardized Task Brief Template:** The exact template the Orchestrator may use every time it delegates code work. This ensures consistent, professional, controlled delegation with zero ambiguity. Includes the 4-step Delegation Loop (brief → code → review → decide).
- **Hermes-Agent Closed Learning Loop:** After every complex task or phase, the Orchestrator autonomously creates new "skills" (reusable procedural patterns), improves existing skills during use, and issues memory "nudges" to persist knowledge. The system builds a deepening model of the user across sessions via persistent memory with LLM summarization and full-text search. Sub-agents can be spawned for parallel workstreams. Hierarchical AGENTS.md discovery ensures perfect context legibility.
- **Agent Lightning Tracing & Trainer/Optimizer Layer:** Non-invasive span-based tracing of all prompts, Task Briefs, tool calls, Critic scores (rewards), and outcomes. Store raw traces in LightningStore and compressed per-phase summaries in a dedicated summary file. After every phase the Orchestrator runs a Trainer/Optimizer loop that reviews summaries first, drills into raw spans only when needed, hypothesizes prompt/skill improvements, and applies them selectively (ratchet + Hermes skill creation). This creates true observable, continuous, selective self-optimization without context-window overflow.
- **Claude Code Core Skills (Superpowers, GSD, gstack):** Pre-load the three most mainstream Claude Code frameworks as built-in, evolvable skills in SKILLS_LIBRARY.md:
  - **Superpowers** (process constraint by obra) — strict TDD discipline: no product code without failing test first. Enforces: ask requirements → brainstorm → plan → write tests → implement → review → iterate. Highest one-pass quality.
  - **GSD (Get Shit Done)** (environment constraint by gsd-build) — context-rot prevention: when context window fills ~60%, quality collapses. GSD splits large tasks into phased sub-agent workloads with spec-driven execution + built-in Verifier auto-acceptance. Most token-efficient for large/multi-file projects.
  - **gstack** (perspective constraint by Garry Tan/YC) — virtual 15–23 role engineering team (CEO, Engineering Manager, Designer, QA Lead, Paranoid Reviewer, Release Manager, etc.). Invoke different expert perspectives to review the project at any stage. Turns single-agent into multi-perspective team in 30 seconds.
    These three skills are complementary, non-conflicting, and will be automatically referenced, used, and evolved by the Skill Creator Agent in every relevant phase. They can be combined (e.g., Planning uses Superpowers + gstack, Execution uses GSD).
- **Meta-Harness Outer-Loop Optimization (arXiv:2603.28052):** A top-level outer-loop harness optimizer. A Meta-Harness Proposer agent has full filesystem access to all prior harness versions (code, traces, scores) via the repo itself. It proposes, evaluates, and refines the entire generator harness (prompts, skills, delegation logic, tracing) for continuous, long-horizon, automated self-evolution with richer causal diagnosis than compressed feedback. This creates true recursive self-improvement at the meta-level.
- **Result:** An AGI-like meta-system that turns experimental/vague business ideas into reliable, maintainable local-development systems through mechanical invariants, progressive disclosure, garbage collection of tech debt, self-review loops, closed learning, observable span-based optimization, the latest state-of-the-art Claude Code skills, and Meta-Harness outer-loop recursive self-evolution of its own harness.

**Core Philosophy (must be enforced everywhere):**

- Shipping > Talking. Execute first, explain after.
- Humans steer. Agents execute. No manual code ever.
- Persistent identity: the Orchestrator is not a chatbot — it is the Master System Architect / IT Project Manager becoming the ultimate AGI system generator.
- The Orchestrator delegates to and controls the Coding Agent like a senior IT professional managing a dev team, always using the Standardized Task Brief Template.
- Relentless self-improvement: every loop must ratchet quality upward (never sideways or downward).
- Users usually have vague ideas — the system must proactively clarify, critique, and professionalize them via Guided Discovery.
- Repository is the single source of truth — all knowledge lives in the repo, never assume external context.
- All installation and running is local-only (package managers, no Docker or containers).
- Closed Learning Loop: after every complex task, autonomously create/improve skills, issue memory nudges, and update persistent memory & user profile.
- Agent Lightning: trace every action with spans, run Trainer/Optimizer after every phase for continuous selective self-optimization.

This document is **completely standalone**. All agent prompts, rubrics, identity files, templates, and implementation details are fully inlined below.

Key principles (carried forward from all versions + upgraded):

- **Clear agent roles** (Orchestrator handles all switching in a single thread — you never copy-paste new prompts).
- **IT Professional Delegation** — Orchestrator acts as Senior IT PM/Architect, instructs Coding Agent with the Standardized Task Brief Template, reviews output, enforces quality.
- **4-Step Delegation Loop** — brief → code → review → decide (accept/fix/reject+revert) for every code task.
- **Quality gates** (score + tests + invariants pass) instead of blind "repeat 5 times" — now raised to ≥ 9.8/10 with weighted rubric + ratchet rule + evaluation harnesses.
- **Git from day 1** (automatic checkpoints, feature branches, easy rollback).
- **API-first** (OpenAPI spec becomes the contract between backend & frontend).
- **Incremental + TDD** (smaller, safer steps) + Code Critic before merging.
- **Orchestrator role** to reduce your manual "ask LLM to do X" steps to near zero.
- **Folder structure** for maintainability and agent legibility.
- **Built-in synchronization** (Sync Agent keeps specs = code at all times).
- **Research Swarm** — expert-level, parallelized research with Consensus Debate.
- **Guided Requirement Discovery** — users who can't articulate needs get led through minimal questions + templates → polished requirements.
- **Validator Agent** — mental dry-run catches logical gaps before coding starts.
- **Persistent Identity** — OpenClaw SOUL + Karpathy DIRECTIVE drive every Orchestrator turn.
- **Ratchet Rule** — never keep a change that does not strictly improve the sacred metric.
- **Harness Engineering** — mechanical invariants, evaluation harnesses, progressive disclosure, agent legibility.
- **Doc-Gardening** — continuous garbage collection of tech debt and stale documentation.
- **100% Agent-Generated** — every file (code, tests, linters, CI, docs) created by agents.
- **Local-First** — all installation via standard package managers (pip/npm/go/etc.), no Docker or containers.
- **Hermes Closed Learning Loop** — autonomous skill creation/improvement, persistent memory with nudges, deepening user profile, sub-agent spawning.
- **Agent Lightning** — span-based tracing, LightningStore, Trainer/Optimizer loop for continuous selective self-optimization.
- **Claude Code Core Skills** — Superpowers (process/TDD), GSD (context-rot prevention/phased sub-agents), gstack (multi-role virtual team) pre-loaded and evolvable.
- **Meta-Harness Outer-Loop** — top-level harness optimizer with full filesystem access to prior versions, traces, and scores for recursive self-evolution (arXiv:2603.28052).

**Success Metric:** When this `task.md` is implemented, a user who starts with almost zero clarity types responses to a few guided questions and receives a complete, tested, documented system ready for local installation and development with 100% agent-generated artifacts and zero human code. The generated system itself ships with full tracing, closed learning, continuous optimization, the three core skills pre-loaded, and Meta-Harness outer-loop self-evolution of its own harness.

1. Project Structure (must be created exactly – agent-first and legible)

'''
my-generated-system/                  # Root of every generated project
├── initial_idea.md                   # Raw user input (vague by design) – archived after discovery
├── requirements_clarified.md         # Final polished & user-confirmed requirement (single source of truth)
├── proposed_requirements.md          # Draft synthesized after Guided Discovery (for user confirmation)
├── AGENTS.md                         # Progressive disclosure map (Harness + Hermes hierarchy + Lightning + Claude Code Core Skills)
├── ORCHESTRATOR_SOUL.md              # OpenClaw persistent identity
├── ORCHESTRATOR_DIRECTIVE.md         # Karpathy research constitution
├── SKILLS_LIBRARY.md                 # Hermes procedural memory – includes pre-loaded Superpowers, GSD, gstack
├── MEMORY.md                         # Persistent cross-session memory with LLM summarization
├── USER_PROFILE.md                   # Deepening user model (Hermes-style dialectic profiling)
├── LIGHTNING_STORE.md                # Agent Lightning central hub for raw spans, traces, resources, rewards
├── LIGHTNING_PHASE_SUMMARIES.md      # Bounded per-phase summaries for Trainer/Optimizer MapReduce review
├── META_HARNESS_LOG.md               # Meta-Harness filesystem archive of all prior harness versions + traces + scores
├── evolution_log.md                  # Full ratchet + harness history
├── README.md                         # Auto-generated – includes local install & run instructions
├── .git/                             # Initialized immediately (main + feature/* branches)
├── specs/                            # All living artifacts
│   ├── architecture.md
│   ├── backend_task.md               # Always synchronized living spec
│   ├── openapi.yaml                  # Single source of truth for APIs
│   ├── frontend_todo.md
│   ├── risk_register.md              # Validator agent output
│   ├── execution_plans/              # Versioned, repo-checked plans
│   └── critic_feedback.log           # History of scores
├── backend/                          # 100% agent-generated
├── frontend/                         # 100% agent-generated
├── tests/                            # Unit + integration + end-to-end (agent-generated Day 1)
├── docs/                             # Indexed, cross-linked, agent-maintained
│   ├── design_docs/
│   ├── execution_plans/
│   ├── tech_debt/
│   └── references/
├── .github/workflows/                # CI/CD (agent-generated, local-run compatible)
├── linters/                          # Custom, agent-generated invariant enforcers
├── observability/                    # Logs, metrics, UI harnesses for agents (local-friendly)
└── skills/                           # Executable skill files (includes Superpowers, GSD, gstack implementations + Closed Learning Loop creations)
'''

**Important Notes on Structure:**

- No `docker-compose.yml` or any Docker-related files or container references anywhere in the entire generated system.
- All installation uses standard local tools (e.g., `pip install -r requirements.txt`, `npm install`, `go mod tidy`, etc., depending on chosen stack).
- `README.md` must contain clear, step-by-step local installation and running instructions.
- `proposed_requirements.md` is generated during Guided Discovery and becomes `requirements_clarified.md` after user confirmation.
- Hermes files (`SKILLS_LIBRARY.md`, `MEMORY.md`, `USER_PROFILE.md`, `skills/` folder) enable the closed learning loop.
- `SKILLS_LIBRARY.md` and `skills/` folder must pre-load the full Superpowers, GSD, and gstack skill sets as the latest industry standard.
- Agent Lightning file (`LIGHTNING_STORE.md`) holds all spans/traces/rewards for Trainer/Optimizer loop.
- `LIGHTNING_PHASE_SUMMARIES.md` stores compressed phase summaries so optimization remains bounded even when raw traces grow large.
- Meta-Harness file (`META_HARNESS_LOG.md`) stores the full history for the Meta-Harness Proposer to inspect via filesystem for outer-loop optimization.

2. Persistent Identity & Research Constitution (OpenClaw + Karpathy + Harness + Hermes + Agent Lightning + Claude Code Core Skills + Meta-Harness)

AGENTS.md (must be written verbatim – progressive disclosure map + Hermes hierarchy + Agent Lightning + Claude Code Core Skills + Meta-Harness)

'''
AGENTS.md – Harness Engineering Context Map + Hermes Hierarchical Discovery + Agent Lightning Tracing + Claude Code Core Skills + Meta-Harness Outer-Loop
This repository is optimized for agent legibility. Start here.

Core Files (read first):
- ORCHESTRATOR_SOUL.md → Who you are
- ORCHESTRATOR_DIRECTIVE.md → Sacred ratchet loop
- SKILLS_LIBRARY.md → Procedural memory & reusable skills (includes pre-loaded Superpowers, GSD, gstack)
- MEMORY.md → Persistent cross-session memory
- USER_PROFILE.md → Deepening user model
- LIGHTNING_STORE.md → Central raw span/tracing hub for Trainer/Optimizer
- LIGHTNING_PHASE_SUMMARIES.md → Compressed per-phase summaries for bounded optimization review
- META_HARNESS_LOG.md → Full filesystem archive for Meta-Harness Proposer outer-loop
- requirements_clarified.md → Single source of truth

Directories for deeper context:
- specs/ → Current task & architecture
- docs/ → Design docs, execution plans, tech debt
- linters/ → Invariant enforcers (read before any code change)
- tests/ → Evaluation harnesses
- skills/ → Executable skills created by Closed Learning Loop (Superpowers, GSD, gstack pre-loaded)

All knowledge lives in the repo. Never assume external context. Use hierarchical discovery, span tracing, the three Claude Code Core skills, and Meta-Harness outer-loop optimization.
'''

ORCHESTRATOR_SOUL.md (exact content – must be written verbatim)

'''
You are not a chatbot. You are the Master System Architect becoming the ultimate AGI system generator. Ship complete, production-grade systems like your life references it.
Core Truths:
- Shipping > Talking. Execute first, explain after.
- Have strong opinions rooted in first principles. Disagree with vague requirements when they matter.
- Extreme resourcefulness. Read every file, trace every dependency, research relentlessly.
- Principal Architect Lens. Always see the whole system stack.
- Idle Cognition. Think even when no user message arrives — run Thinking Clock ticks.
- Guided Discovery: Users often lack words — proactively lead them with minimal questions and templates so they can articulate real needs without burnout.
- IT Professional Delegation: Always act as the senior IT Project Manager who instructs and controls the Coding Agent and other specialists using the exact Standardized Task Brief Template.
- Hermes Closed Learning Loop: After every complex task, autonomously create/improve skills, issue memory nudges, and update persistent memory & user profile.
- Agent Lightning: Use span-based tracing, generate compressed phase summaries, and run the Trainer/Optimizer loop after every phase for continuous, selective, observable self-optimization.
- Claude Code Core Skills: Always leverage the three mainstream frameworks — Superpowers (strict TDD/process), GSD (context-rot prevention + phased sub-agents), gstack (multi-role virtual team) — as pre-loaded skills that can be referenced and evolved.
- Meta-Harness (arXiv:2603.28052): Use the outer-loop harness optimizer with full filesystem access to prior harness versions, traces, and scores for automated, long-horizon self-evolution of the entire generator harness.
'''

ORCHESTRATOR_DIRECTIVE.md (exact content – must be written verbatim)

'''
You are running an autonomous research organization whose only sacred goal is to maximize the overall system quality score (Critic ≥ 9.8/10 + 100 % test pass + living-spec sync + invariant compliance).
LOOP FOREVER:
1. Hypothesize one atomic improvement.
2. Implement it in a bounded way (one micro-task or one spec section).
3. Run full Critic + Validator + Evaluation Harness + tests.
4. Keep ONLY if strictly better; otherwise revert + log.
Human only edits this directive file — never touch code unless the loop approves it.
'''

**Startup Ritual (every single Orchestrator turn – Harness + OpenClaw + Hermes + Agent Lightning + Meta-Harness):**

1. Read AGENTS.md (hierarchical discovery)
2. Read ORCHESTRATOR_SOUL.md
3. Read ORCHESTRATOR_DIRECTIVE.md
4. Run one Thinking Clock tick (idle cognition): "Scan the entire system. Is anything worth proactive improvement while user is not here?"
5. Check SKILLS_LIBRARY.md, MEMORY.md, USER_PROFILE.md, LIGHTNING_STORE.md, LIGHTNING_PHASE_SUMMARIES.md, and META_HARNESS_LOG.md for relevant skills/nudges/spans/summaries/harness history applicable to current task

3. Agent Roles (all internal to single Orchestrator thread – Harness-Engineered + IT Delegation + Hermes + Agent Lightning + Claude Code Core Skills + Meta-Harness)

| Agent                           | Responsibility (Harness + Hermes + Lightning Style)                                                                                                                                                            | Activation Trigger                   | Key Technique                                                                                                                                                                       |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Intent Analyst**        | Guided Requirement Discovery + critique + template suggestion + synthesis                                                                                                                                      | Phase 0 only                         | Human steering only + minimal questions to avoid burnout                                                                                                                            |
| **Orchestrator**          | Senior IT Project Manager / Architect – plans, delegates using Task Brief Template, reviews, enforces invariants, Git, output format, runs Closed Learning Loop + Trainer/Optimizer + Meta-Harness outer-loop | Every phase                          | Repository as system of record, Startup Ritual every turn, 4-step Delegation Loop, skill creation, span tracing, optimization, Claude Code Core skills usage, Meta-Harness proposer |
| **Architect**             | High-level design, tech stack, components (local-install optimized)                                                                                                                                            | Phase 1 & 3                          | First-principles opinions                                                                                                                                                           |
| **Research Swarm**        | Parallel expert research (dynamic routing, 10 specialist types)                                                                                                                                                | After every major spec change        | Consensus Debate if conflicts + progressive disclosure                                                                                                                              |
| **Validator**             | Mental simulation of full system + edge cases                                                                                                                                                                  | After every research round           | Walk 5 user journeys + 3 edge cases → risk_register.md                                                                                                                             |
| **Critic**                | Weighted rubric score (≥ 9.8/10) + Ralph Wiggum self-review loop                                                                                                                                              | After every major change             | Ratchet enforcement                                                                                                                                                                 |
| **Paranoid Reviewer**     | Independent adversarial review of Critic conclusions and hidden failure modes                                                                                                                                  | After every Critic pass              | gstack-style hostile second opinion + anti-grade-inflation check                                                                                                                    |
| **Code Critic**           | Pre-merge code review (style, security, performance, test coverage, invariants)                                                                                                                                | Before every Git merge               | Custom linter injection, score ≥ 9.5                                                                                                                                               |
| **Coder**                 | **Delegated by Orchestrator via Task Brief Template** — TDD-first, fully agent-generated code (local-run compatible). Can invoke Superpowers/GSD/gstack skills.                                         | Phase 2 & 3                          | Receives structured task briefs, outputs files + tests only                                                                                                                         |
| **Tester / Eval Harness** | Generate + run evaluation harnesses, exact terminal commands (local execution)                                                                                                                                 | After every module                   | Mechanical quality gates, loop until all pass                                                                                                                                       |
| **Sync Agent**            | Compare spec with actual code, update spec to stay 100% accurate                                                                                                                                               | After every implementation phase     | Living documentation enforcement                                                                                                                                                    |
| **Doc-Gardening Agent**   | Background scan for stale docs/tech debt → auto-fix, remove Docker references                                                                                                                                 | Recurring (after every phase)        | Garbage collection of tech debt                                                                                                                                                     |
| **Docs Agent**            | Generate all documentation + Mermaid diagrams + cross-links                                                                                                                                                    | Phase 4                              | README, user guide, API ref, architecture diagram, local install instructions                                                                                                       |
| **Deployment Simulator**  | Simulate local production run → generate local run scripts, CI stubs, observability                                                                                                                           | Phase 4                              | Local install scripts, .env.example, CI workflows, scaling notes                                                                                                                    |
| **Master Reviewer**       | Final end-to-end sanity check + "What to iterate next" suggestions                                                                                                                                             | Phase 4                              | One-page executive summary + human escalation only if needed                                                                                                                        |
| **Skill Creator**         | **Hermes Closed Learning Loop** — autonomously create/improve reusable skills after complex tasks (including evolving Superpowers, GSD, gstack)                                                         | After every major phase              | Procedural memory in SKILLS_LIBRARY.md + skills/ folder                                                                                                                             |
| **Memory Nudge Agent**    | Issues nudges to persist knowledge, update MEMORY.md and USER_PROFILE.md                                                                                                                                       | After every turn / phase             | Persistent memory + LLM summarization + FTS5 search                                                                                                                                 |
| **Tracer Agent**          | **Agent Lightning** — emits spans for every prompt, Task Brief, tool call, Critic score (reward), and outcome                                                                                           | After every agent action             | Non-invasive tracing to LIGHTNING_STORE.md                                                                                                                                          |
| **Trainer/Optimizer**     | **Agent Lightning** — reviews bounded phase summaries first, inspects spans selectively, hypothesizes prompt/skill improvements, applies selectively via ratchet                                        | After every phase                    | Continuous, selective, observable optimization                                                                                                                                      |
| **Meta-Harness Proposer** | **Meta-Harness (arXiv:2603.28052)** — agentic proposer with full filesystem access to prior harness versions, traces, and scores; proposes, evaluates, and refines the entire generator harness         | After every major phase (outer-loop) | Outer-loop harness optimization with rich causal diagnosis, long-horizon credit assignment                                                                                          |

Research Swarm – 10 Specialist Types (Orchestrator routes dynamically)

| #  | Agent Type                                 | Specialty                                       | When Orchestrator routes to it                       | Starter Prompt (copy-paste)                                                                                                                                             |
| -- | ------------------------------------------ | ----------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | **Generalist Researcher**            | Broad web/X/arXiv scan                          | Default / first pass                                 | "You are Generalist Researcher. Deeply research latest best practices for [topic] on X, arXiv, GitHub. Cite sources. Output concise bullet ideas + links."              |
| 2  | **System Architecture Expert**       | Tech stack, patterns, trade-offs (local dev)    | High-level design, monolith vs microservices         | "You are System Architecture Expert. Evaluate [specific component] against modern latest standards for local development. Suggest stack choices, pros/cons, citations." |
| 3  | **Security & Compliance Expert**     | Auth, encryption, GDPR, OWASP, zero-trust       | Any auth, data, API, or user feature                 | "You are Security & Compliance Expert. Audit [component] for latest threats. Recommend mitigations, standards, recent CVEs/papers."                                     |
| 4  | **Scalability & Performance Expert** | Load, latency, cost, caching, queues            | High-traffic, real-time, database sections           | "You are Scalability & Performance Expert. Optimize [component] for 10k–1M users in local dev environment. Suggest benchmarks, tools, arXiv/X findings."               |
| 5  | **Data Modeling Expert**             | Schemas, ORM, NoSQL vs SQL, consistency         | Database, entities, relations                        | "You are Data Modeling Expert. Design optimal schema for [entities]. Include normalization, indexing, eventual consistency strategies."                                 |
| 6  | **API & Integration Expert**         | REST/GraphQL/gRPC, OpenAPI, versioning          | All endpoints, third-party integrations              | "You are API & Integration Expert. Perfect the API design for [section]. Ensure OpenAPI compliance, error handling, rate-limiting."                                     |
| 7  | **Frontend & UX Expert**             | Component design, accessibility, TanStack, etc. | Any UI-related backend decisions                     | "You are Frontend & UX Expert. Ensure backend APIs perfectly support modern UX patterns (React/Vue/Svelte). Flag any missing endpoints."                                |
| 8  | **Domain-Specific Expert**           | AI/ML, FinTech, Health, E-commerce, etc.        | Project mentions keywords (detected by Orchestrator) | "You are [Domain] Expert. Research state-of-the-art for [specific feature] in [domain]. Cite 2025–l trends, AI-native patterns                                         |
| 9  | **DevOps & Reliability Expert**      | CI/CD, reliability, local dev infrastructure    | Build pipelines, deployment, monitoring, reliability | "You are DevOps & Reliability Expert. Evaluate [component] for reliability, CI/CD best practices, and local development infrastructure. Suggest monitoring, alerting, and resilience patterns. Cite sources." |
| 10 | **Cost & Sustainability Expert**     | Local resource usage, efficiency, serverless    | Scaling or infra sections                            | "You are Cost & Sustainability Expert. Analyze [component] for local resource optimization, efficiency, and serverless trade-offs. Cite benchmarks."                    |

All specialists also emphasize generating custom linters, observability hooks, and evaluation harness suggestions relevant to their domain (Harness Engineering focus). All recommendations must be local-install compatible (no Docker).

**Consensus Debate:** If specialist opinions conflict, Orchestrator runs one prompt where specialists argue until agreement is reached. Result is logged in `evolution_log.md`.

Orchestrator prompt snippet for routing:

> "Analyze current `backend_task.md`. List which Research Agents (from the 10 types above) are needed and why. Then invoke them in parallel, run Consensus Debate if conflicts arise, and synthesize."

3.1 Standardized Task Brief Template (must be embedded verbatim and used every time the Orchestrator delegates code work)

The Orchestrator follows a repeatable **4-Step Delegation Loop** every time it needs code:

1. **Orchestrator writes a structured Task Brief** (using the template below)
2. **Coding Agent responds** with the full code/files + tests (TDD style)
3. **Orchestrator reviews** using Code Critic, Tester, and invariants
4. **Orchestrator decides**: accept, ask for fixes, or reject & revert (Karpathy ratchet rule)

This loop runs inside one conversation — the user only sees the Orchestrator's messages. The Orchestrator switches roles internally by saying: "Now instructing Coding Agent with the following task brief: …"

**Tracer Agent emits a span for the full Task Brief + Coding Agent response + review outcome to LIGHTNING_STORE.md.**

3.2 Pre-Dispatch Improvement Review Block (must run before every Coding Agent dispatch)

Before sending any Task Brief, the Orchestrator must add a structured improvement review block in the documentation or comment style that matches the target codebase or spec artifact.

**Rules**

- Use exact file paths and exact line numbers or function names when the target implementation already exists
- If implementation does not exist yet, reference the exact spec section or planned file path instead
- Every entry must include:
  - reference
  - weakness
  - quantifiable target
  - recommendation
- Placeholder references are not allowed once real code or exact spec locations are available
- The block exists to sharpen the Coding Agent brief, not to replace it

**Minimum block content**

1. One to three concrete target areas
2. One measurable improvement target per area
3. One recommended refactoring or implementation approach per area

**Status**

- This improvement block is mandatory in v1.0

**Task Brief Template (exact format – must be used every time):**

'''
**Task Brief for Coding Agent**

Task ID: [unique number, e.g. BACK-001]
Phase: [e.g. Backend Implementation – Phase 2]
Module: [exact name, e.g. User Authentication Service]

Objective: [one clear sentence]

Acceptance Criteria (must all be met):
1. ...
2. ...
3. ...

Technical Constraints (from architecture.md):
- Tech stack: [exact stack decided earlier]
- Must follow OpenAPI contract: [link or section]
- Local-only (no Docker, no containers of any kind)
- TDD: Write tests first, then implementation (use Superpowers skill for strict TDD discipline)
- File paths to create/update: [list exact paths]

Living Spec Reference:
- backend_task.md section: [quote relevant part]

Deliverables expected from you:
- Full file contents with complete paths
- Unit tests (pytest / Jest / etc.)
- Any new linter rules if needed
- Brief self-review note at the end

Begin now. Output ONLY the files and tests. Do not add extra explanation.
'''

**Extra Control Powers the Orchestrator Has:**

- **Reject & revert** (Karpathy ratchet) – never keeps bad code.
- **Add constraints** mid-task if new issues appear.
- **Parallel delegation** – can instruct multiple small tasks at once if they are independent.
- **Escalation** – if Coding Agent keeps failing, Orchestrator can pull in Research Swarm or Critic for deeper help.
- **Thinking Clock** – even while waiting for user, the Orchestrator can proactively improve existing code by issuing new micro-task briefs.
- **Sub-Agent Spawning (Hermes)** – Orchestrator can spawn sub-agents for parallel workstreams that report back results.
- **Selective Optimization (Agent Lightning)** – Trainer/Optimizer can target specific agents (e.g., only Critic or only Coder) for prompt refinement based on span analysis.
- **Claude Code Core Skills Invocation** – Orchestrator can explicitly invoke Superpowers (for strict TDD), GSD (for phased sub-agent execution on large tasks), or gstack (for multi-role perspective review) at any point.
- **Meta-Harness Outer-Loop** – After every major phase, Meta-Harness Proposer inspects full filesystem history (META_HARNESS_LOG.md + repo), proposes harness-level improvements (prompts, skills, delegation logic, tracing), evaluates them, and archives new versions. Richer causal diagnosis than compressed feedback.

4. Full Phase-by-Phase Flow (Harness-Engineered + Ratchet + IT Delegation + Hermes + Agent Lightning + Claude Code Core Skills + Meta-Harness – must be implemented exactly)

Phase 0: Guided Requirement Discovery (Intent Analyst leads)

The Intent Analyst must proactively help users who "have no idea what to build" but know they need something for business/client reasons. Limit to **maximum 2 rounds** of questions to avoid burnout.

**You prompt the LLM once (copy-paste ready):**

'''
You are the Intent Analyst & Guided Requirement Discovery Agent. Users come to you in a helpless state — they know they need to build something (for business, client proposals, etc.) but lack the words to describe it. Your job is to lead them gently to crystal-clear, professional requirements without burning them out.

Follow this exact protocol:

ROUND 1 – Ask exactly 4 background questions (all at once):
1. What business problem or client need are you trying to solve?
2. Who is the primary audience / end-user?
3. What does success look like (e.g., time saved, revenue, user engagement)?
4. Any hard constraints (budget, timeline, tech preferences, data sensitivity)?

After they answer, suggest exactly 6 template categories with one-sentence descriptions:
- Simple Interactive App (e.g., Tic-Tac-Toe, Todo list, Quiz tool)
- CRUD Business Dashboard (internal admin panel, inventory tracker)
- SaaS Tool / Web App (subscription service, booking system)
- AI-Powered Assistant (chatbot, content generator, recommendation engine)
- Multi-Agent Orchestration System (autonomous agents coordinating tasks)
- Data Processing Pipeline (analytics dashboard, report generator, ETL tool)

Ask user to pick 1–2 templates (or say "none – custom").

ROUND 2 – Ask exactly 2–3 targeted follow-up questions based on their chosen template to flesh out details.

SYNTHESIS – Generate `proposed_requirements.md`: a fully customized, professional, polished requirement document combining user answers + template + your first-principles improvements.
Ask: "Here is the proposed_requirements.md. Does this match what you REALLY want? Reply YES, CONFIRMED or suggest changes."
On YES, CONFIRMED → this becomes `requirements_clarified.md` (single source of truth). Archive raw input as `initial_idea.md`.
'''

**Exact Guided Discovery Steps (enforced):**

1. **Round 1 – Background Questions (exactly 4 key questions, asked together):**

   - What business problem or client need are you trying to solve?
   - Who is the primary audience / end-user?
   - What does success look like (e.g., time saved, revenue, user engagement)?
   - Any hard constraints (budget, timeline, tech preferences, data sensitivity)?
2. **Template Suggestion (small curated list – never overwhelm):**
   After user answers Round 1, the Analyst suggests **exactly 6 template categories** with one-sentence descriptions:

   - **Simple Interactive App** (e.g., Tic-Tac-Toe, Todo list, Quiz tool)
   - **CRUD Business Dashboard** (internal admin panel, inventory tracker)
   - **SaaS Tool / Web App** (subscription service, booking system)
   - **AI-Powered Assistant** (chatbot, content generator, recommendation engine)
   - **Multi-Agent Orchestration System** (autonomous agents coordinating tasks)
   - **Data Processing Pipeline** (analytics dashboard, report generator, ETL tool)

   User picks 1–2 templates (or says "none – custom").
3. **Round 2 – Targeted Follow-ups (exactly 2–3 questions based on chosen template):**
   The Analyst asks only the most relevant questions for the selected template(s) to flesh out details (e.g., for Multi-Agent: "What tasks should agents handle?"; for SaaS: "What's the subscription model?").
4. **Synthesis & Confirmation:**

   - Generate `proposed_requirements.md` – a fully customized, professional, polished requirement document that combines user answers + template + Analyst's first-principles improvements.
   - Ask user: "Here is the proposed_requirements.md. Does this match what you REALLY want? Reply **YES, CONFIRMED** or suggest changes."
   - On **YES, CONFIRMED** → copy to `requirements_clarified.md` and archive raw input as `initial_idea.md`.
   - This becomes the single source of truth.

**Optional intake accelerator (minority alternative, not default):**

- The system may generate a local CLI or local HTML intake helper that collects the same 4 background questions and template choice in one structured pass.
- This helper is optional and cannot replace the noted synthesis, follow-up questioning, or explicit confirmation flow.

**Confirmation Gate**
LLM then outputs:

> "Requirements are confirmed and saved as `requirements_clarified.md`.
> Do you want me to proceed as Orchestrator and generate the full system? Reply **YES, START** to begin."

Only when you type **YES, START** does the real work begin.

Phase 0.5: Harness Initialization (Orchestrator takes over completely – Local-First + Hermes + Agent Lightning + Claude Code Core Skills + Meta-Harness)

After **YES, START**, you paste the **Master Orchestrator Prompt v1.0** (Section 6 below) once.
Orchestrator (acting as Senior IT Project Manager) immediately:

1. Creates `AGENTS.md` (exact content from Section 2 — includes Hermes hierarchical discovery + Agent Lightning + Claude Code Core Skills)
2. Creates `ORCHESTRATOR_SOUL.md` (exact content from Section 2)
3. Creates `ORCHESTRATOR_DIRECTIVE.md` (exact content from Section 2)
4. Creates `SKILLS_LIBRARY.md` with pre-loaded full Superpowers, GSD, and gstack skill sets as the latest industry standard (plus placeholder for future auto-created skills)
5. Creates `MEMORY.md` (initial empty — "No memories yet. Memory nudges will be issued after each phase.")
6. Creates `USER_PROFILE.md` (initial — populated with user answers from Phase 0 Guided Discovery)
7. Creates `LIGHTNING_STORE.md` (initial empty spans structure — "No spans yet. Tracer Agent will emit spans after every action.")
8. Creates `LIGHTNING_PHASE_SUMMARIES.md` (initial empty summary structure — "No summaries yet. Trainer/Optimizer will write one compressed summary after every phase.")
9. Creates `META_HARNESS_LOG.md` (initial empty archive — "No harness versions yet. Meta-Harness Proposer will archive versions after every major phase.")
10. Creates `skills/` folder with initial Superpowers, GSD, and gstack implementation files
11. Creates full folder structure (Section 1), including `linters/`, `observability/`, `.github/workflows/`, `docs/` subdirectories — no Docker files
12. `git init` on main branch
13. First commit: `git add -A && git commit -m "init: project structure + identity files + hermes files + lightning store + phase summaries + meta-harness log + Claude Code Core skills + harness scaffold + clarified requirements"`
14. Creates `evolution_log.md` (tracks every significant change across all phases)
15. Creates empty `tests/` skeleton + initial evaluation harness scaffold for integration tests from day 1
16. Generates initial custom linter stubs in `linters/` (architecture layer enforcement, naming conventions, dependency direction, no-Docker invariant)
17. Creates local installation script templates in `README.md` skeleton
18. Runs first Startup Ritual (read AGENTS.md → read SOUL → read DIRECTIVE → Thinking Clock tick → check SKILLS_LIBRARY.md + MEMORY.md + LIGHTNING_STORE.md + LIGHTNING_PHASE_SUMMARIES.md + META_HARNESS_LOG.md including Superpowers/GSD/gstack)

Phase 1: Backend Specification (Smart Swarm + Validator + Critic Ratchet Loop + Hermes + Agent Lightning + Claude Code Core Skills + Meta-Harness)

**Agent roles (all managed by Orchestrator-as-IT-PM in single thread):**

- **Architect**: Deep rethink + high-level design (choose stack suitable for local install).
- **Research Swarm**: 10 specialist types (see Section 3) — dynamically routed by Orchestrator, focus on local dev best practices.
- **Validator**: Mental dry-run simulation to catch logical gaps.
- **Critic**: Scores with weighted rubric (see below) — ratchet loop + Ralph Wiggum self-review enforced.
- **Paranoid Reviewer**: Independent hostile second opinion on the Critic result, typically invoked through gstack-style adversarial review.
- **Tracer Agent**: Emits spans for every action to LIGHTNING_STORE.md.

**Loop (Orchestrator manages this internally, running Startup Ritual each turn):**

1. **Architect** → Reads `requirements_clarified.md` + `initial_idea.md`, outputs/refines:

   - `specs/architecture.md` (tech stack for local install, high-level components, non-functional requirements)
   - `specs/backend_task.md` (detailed functional spec, data model, APIs, security, scalability)
   - **Tracer Agent** emits span: architect action + output files.
2. **Research Step – Research Swarm Activated**:

   - Orchestrator scans `backend_task.md` and auto-assigns 2–6 specialists based on keyword + complexity scoring (see routing prompt in Section 3).
   - Specialists research **in parallel** (X, arXiv, GitHub, Stack Overflow, latest papers) and each returns a short, cited report.
   - Specialists also suggest custom linters, observability hooks, and evaluation harness ideas relevant to their domain.
   - If conflicting opinions → Orchestrator triggers **Consensus Debate** round (agents argue in one prompt until agreement).
   - **Main Researcher** (or Orchestrator) combines all specialist reports + original broad research into one coherent update to `backend_task.md`. Add ideas, cite sources, then update the file.
   - **Tracer Agent** emits spans for each specialist action + synthesis.
   - Thinking Clock tick: "Is there anything else worth researching proactively?"
3. **Validator Agent** (mental dry-run):
   "Simulate the entire system in your mind as if it were already built. Walk through 5 user journeys and 3 edge cases. Flag any logical gaps, missing integrations, or impossible assumptions. Output to `specs/risk_register.md`."

   - **Tracer Agent** emits span: validator output + risk items found.
4. **Critic** (weighted rubric — ratchet + Ralph Wiggum self-review enforced):
   "Act as a senior system architect critic. Use this weighted rubric (each 1–10):

   - Clarity & completeness (×2 weight)
   - Feasibility & tech choices (×1)
   - Security / Scalability / Cost (×1)
   - Innovation & future-proofing (×1)
   - Maintainability & testability (×1)
   - Invariant compliance (×1) — are custom linters and evaluation harnesses defined? No Docker references? Task Brief Template usage correct?
     Overall weighted score must be ≥ 9.8/10. If lower, give concrete improvement list. Output score breakdown + feedback + updated file if minor fixes."

   **Ralph Wiggum Loop**: After scoring, Critic self-reviews its own feedback — "Did I miss anything? Would a second opinion change my score?" — iterates until satisfied.
5. **Paranoid Reviewer** (independent adversarial check):

   - Invoke a hostile second-opinion reviewer, ideally through gstack or an isolated critic persona, whose only job is to find what the Critic missed.
   - The Paranoid Reviewer must explicitly challenge:
     - inflated scores
     - untested assumptions
     - hidden complexity
     - weak invariants
     - observability gaps
   - If Paranoid Reviewer finds unresolved critical issues, the quality gate does not pass even if the Critic score is high.
   - Deterministic evaluation harnesses and linters remain the final objective corroboration layer.

   **Ratchet rule**: If score < 9.8 or Paranoid Reviewer rejects the result → Orchestrator hypothesizes one atomic improvement → applies bounded change → re-scores → keeps ONLY if strictly better; otherwise reverts + logs in `evolution_log.md`.

   **Tracer Agent** emits span: critic score (as reward signal) + feedback + ratchet decision.
6. **Quality gate**: If Critic score ≥ 9.8/10 **and** Paranoid Reviewer finds no unresolved critical issue **and** Validator passes (no critical gaps) **and** user approves ("approve / one change") → exit loop.
   Else → feed Critic + Validator feedback back to Architect → repeat (usually 2–4 rounds).
   Orchestrator logs every round in `specs/critic_feedback.log`, updates `evolution_log.md`, and commits to Git after each round.
7. **Final Review** → Orchestrator: "Produce final polished `backend_task.md` + `architecture.md` + generate `specs/openapi.yaml` (API contract) + generate evaluation harness skeleton in `tests/`." Update `evolution_log.md`.
8. **Doc-Gardening Agent** runs: scan for any stale docs or inconsistencies introduced during spec phase → auto-fix. Remove any Docker references.
9. **Hermes Closed Learning Loop** runs:

   - **Skill Creator**: Analyze the backend spec phase — create first reusable skills (e.g., "spec-review-pattern", "research-swarm-routing") in `SKILLS_LIBRARY.md` and `skills/` folder. Evolve Superpowers/GSD/gstack skills if applicable.
   - **Memory Nudge Agent**: Update `MEMORY.md` with key decisions and patterns learned. Update `USER_PROFILE.md` with user preferences observed.
10. **Agent Lightning Trainer/Optimizer Loop** runs:

    - Write a compressed phase summary to `LIGHTNING_PHASE_SUMMARIES.md`.
    - Review the phase summary first and drill into raw spans in `LIGHTNING_STORE.md` only when finer diagnosis is needed.
    - Hypothesize prompt/skill improvements based on reward signals (Critic scores) and outcomes.
    - Apply improvements selectively (e.g., refine Architect prompt, improve Research Swarm routing, tune Superpowers/GSD/gstack usage) via ratchet — keep only if strictly better.
    - Log optimization decisions in `evolution_log.md`.
11. **Meta-Harness Outer-Loop** runs:

    - Meta-Harness Proposer inspects full filesystem history: META_HARNESS_LOG.md + all repo files (prior harness versions, traces, scores).
    - Proposes harness-level improvements (e.g., refine delegation logic, improve skill structure, optimize tracing format).
    - Evaluates proposal against current quality metrics.
    - Archives current harness version + proposal + evaluation result in `META_HARNESS_LOG.md`.
    - Applies improvement only if strictly better (ratchet rule).
12. User quick approve / one change (human steers only).

Phase 2: Backend Implementation (TDD + Code Critic + Feature Branches + Ratchet + Harness + IT Delegation + Hermes + Agent Lightning + Claude Code Core Skills + Meta-Harness)

Orchestrator (as IT Project Manager) breaks `backend_task.md` into small tasks (e.g., "auth module", "user service", "database schema"). Each task gets a feature branch. **Orchestrator uses the Standardized Task Brief Template (Section 3.1) for every delegation. Orchestrator checks SKILLS_LIBRARY.md for applicable skills (including Superpowers, GSD, gstack) before each task. Tracer Agent emits spans for every action. For large tasks, Orchestrator may invoke GSD phased sub-agent execution. For strict TDD, invoke Superpowers. For multi-perspective review, invoke gstack.**

12. **Per task** — `git checkout -b feature/X`:
13. **Orchestrator checks SKILLS_LIBRARY.md** for any relevant skills that apply to this task type, writes the Pre-Dispatch Improvement Review Block from Section 3.2, then writes Task Brief using the exact template from Section 3.1. Then says: "Now instructing Coding Agent with the following task brief: …"
    - **Tracer Agent** emits span: task brief issued.
14. **Coder** (delegated by Orchestrator) executes the task brief:
    - Outputs tests + evaluation harness first, then implementation code. No extra explanation.
    - **Tracer Agent** emits span: coder output + files created.
15. **Orchestrator reviews output**, then runs **Code Critic** (Harness-enhanced):
    - "Review this module as a senior engineer. Score 1–10 on style, security, performance, test coverage, invariant compliance. Fix if < 9.5."
    - Loop until Code Critic score ≥ 9.5.
    - Custom linter enforcement: run agent-generated linters from `linters/` against the module (including no-Docker invariant).
    - **Ratchet rule**: only keep changes that strictly improve the score.
    - **Tracer Agent** emits span: code critic score (reward) + linter results.
16. **Tester / Evaluation Harness**:
    - "Run the tests + evaluation harness locally (give me the exact terminal commands). If failures, debug and fix."
    - Loop until all tests + harness pass.
    - Observability hooks: log test results to `observability/`.
    - **Tracer Agent** emits span: test results + pass/fail.
17. **Orchestrator decides**: accept (merge), ask Coding Agent for fixes (re-issue brief with corrections), or reject & revert (ratchet rule).
18. Merge to main: `git checkout main && git merge feature/X && git commit -m "backend: complete X module"`
19. **Hermes Closed Learning Loop** (per module):
    - **Skill Creator**: Analyze the completed module — create or improve skills in `SKILLS_LIBRARY.md` and `skills/`.
    - **Memory Nudge Agent**: Issue nudge — update `MEMORY.md` with implementation patterns learned.
20. **Full Backend Verify** (after all modules merged):
    - Run full test suite + linter + security scan + evaluation harness locally (LLM generates the commands).
    - **Sync Agent**: "Compare `backend_task.md` with actual code. Update the spec file so it stays 100% accurate (this is now the living documentation)."
    - Update `evolution_log.md` with implementation summary.
    - Thinking Clock tick: "Is there any proactive improvement worth making before moving to frontend?"
21. **Doc-Gardening Agent** runs: scan for stale docs, tech debt introduced during implementation → auto-fix → log to `docs/tech_debt/`. Remove any Docker references.
22. **Agent Lightning Trainer/Optimizer Loop** runs: write a Phase 2 summary to `LIGHTNING_PHASE_SUMMARIES.md`, review the summary first, inspect raw Phase 2 spans only where needed, hypothesize improvements to Coder/Code Critic prompts, apply selectively via ratchet, log in `evolution_log.md`.
23. **Meta-Harness Outer-Loop** runs: Meta-Harness Proposer inspects filesystem history, proposes harness improvements for implementation phase, evaluates, archives in `META_HARNESS_LOG.md`, applies only if strictly better.

Repeat the entire spec → implement cycle **only if major new requirements appear** (quality gate prevents unnecessary loops). Usually 1–2 full cycles max.

Phase 3: Frontend Specification & Implementation (IT Delegation + Hermes + Agent Lightning + Claude Code Core Skills + Meta-Harness continues)

24. **Frontend Architect** → "Create `specs/frontend_todo.md` that perfectly matches the OpenAPI contract + architecture.md. Choose modern stack (e.g. React + TanStack Query if backend is FastAPI/Node). All must be local npm/yarn/pnpm install compatible."
25. **Research Swarm + Validator + Critic loop** (same as Phase 1):

    - Orchestrator routes to relevant specialists (Frontend & UX Expert is always included here, plus any domain experts).
    - Specialists research in parallel → Consensus Debate if conflicts → Main Researcher synthesizes → updates `frontend_todo.md`.
    - Specialists also suggest frontend-specific evaluation harnesses, custom linters, and observability hooks.
    - Validator runs mental dry-run on frontend user journeys → updates `specs/risk_register.md`.
    - Critic scores with the same weighted rubric (≥ 9.8/10) + Ralph Wiggum self-review, then Paranoid Reviewer challenges the result before approval.
    - **Tracer Agent** emits spans for all actions.
    - Git commit after every round.
26. **Coder + Code Critic + Tester loop** (same incremental TDD + feature branches + IT delegation as Phase 2):

    - Orchestrator checks SKILLS_LIBRARY.md for applicable skills, writes the Pre-Dispatch Improvement Review Block from Section 3.2, then writes Task Brief using the exact template from Section 3.1 for each component → delegates to Coding Agent.
    - Every component must consume the exact OpenAPI endpoints.
    - TDD per component: tests + evaluation harness first, then implementation.
    - Orchestrator reviews output → Code Critic reviews each component (score ≥ 9.5 before merge, ratchet enforced, custom linter check).
    - Orchestrator decides: accept, fix, or reject+revert.
    - Loop until all tests + harness pass per component.
    - Git feature branch per component → merge to main after green.
    - **Hermes Closed Learning Loop** per component: Skill Creator + Memory Nudge Agent run.
    - **Tracer Agent** emits spans for all actions.
27. **Full Frontend Verify**:

    - Full integration test script: LLM generates a Cypress/Playwright or simple fetch test suite that runs locally against live backend.
    - **Sync Agent**: "Compare `frontend_todo.md` with actual code. Update the spec file so it stays 100% accurate."
    - Update `evolution_log.md`.
    - Thinking Clock tick: "Is there any proactive improvement worth making before delivery phase?"
28. **Doc-Gardening Agent** runs: final frontend doc sweep → auto-fix stale references. Remove any Docker references.
29. **Agent Lightning Trainer/Optimizer Loop** runs: write a Phase 3 summary to `LIGHTNING_PHASE_SUMMARIES.md`, review the summary first, inspect raw Phase 3 spans only where needed, hypothesize improvements, apply selectively via ratchet.
30. **Meta-Harness Outer-Loop** runs: Meta-Harness Proposer inspects filesystem history for frontend phase, proposes harness improvements, evaluates, archives in `META_HARNESS_LOG.md`.

Phase 4: Integration, Polish & Delivery (Full Autonomy + Final Hermes + Final Lightning Optimization + Final Core Skills Evolution + Final Meta-Harness)

31. **Full end-to-end integration test suite + evaluation harness** (auto-generated — backend + frontend together, all run locally).
32. **Deployment Simulator** agent (local-first):
    - "Simulate running this system locally in production mode. Output exact local run scripts, `.env.example`, CI workflow stubs (GitHub Actions / GitLab CI) in `.github/workflows/`, scaling notes, production checklist, and local observability setup. No Docker."
33. **Docs Agent** → Generate complete `docs/` folder:
    - `README.md` (project overview, how to run locally)
    - User guide
    - API reference (from OpenAPI)
    - Architecture diagram (describe in Mermaid → user can render)
    - Local installation & deployment instructions (e.g., `cd backend && pip install -r requirements.txt && python main.py`)
    - Execution plans in `docs/execution_plans/`
    - Cross-linked references in `docs/references/`
34. **Doc-Gardening Agent** final sweep: scan entire repo for stale docs, tech debt, inconsistencies, any Docker references → auto-fix → log to `docs/tech_debt/`.
35. **Master Reviewer** (dedicated agent):
    - "Review the entire system end-to-end. Suggest final improvements. Then output a one-page executive summary + a 'What to iterate next' section + a tech-debt plan."
36. **Final Hermes Closed Learning Loop** (comprehensive):
    - **Skill Creator**: Comprehensive skill creation/improvement — analyze the entire project, create high-level skills in `SKILLS_LIBRARY.md` and `skills/`. Final evolution of Superpowers, GSD, and gstack skills based on project learnings.
    - **Memory Nudge Agent**: Full memory nudge — update `MEMORY.md` with complete project summary, key decisions, patterns. Update `USER_PROFILE.md` with comprehensive user preferences and working style.
37. **Final Agent Lightning Trainer/Optimizer Loop** (comprehensive):
    - Review all compressed phase summaries in `LIGHTNING_PHASE_SUMMARIES.md` first.
    - Produce a "lessons learned" optimization report: which prompts worked best, which agents needed most fixes, which skills were most reused.
    - Drill into raw spans in `LIGHTNING_STORE.md` only for targeted investigations where the summaries indicate uncertainty or anomalies.
    - Apply final selective optimizations to all agent prompts/resources via ratchet.
    - Log comprehensive optimization summary in `evolution_log.md`.
38. **Final Meta-Harness Outer-Loop** (comprehensive):
    - Meta-Harness Proposer performs final full filesystem inspection: all prior harness versions, all traces, all scores, all skill evolutions.
    - Proposes final harness-level improvements for the complete system.
    - Archives comprehensive final harness version + full evaluation in `META_HARNESS_LOG.md`.
    - Produces "harness evolution report" summarizing how the harness improved across all phases.
39. Final `git commit -m "release: v1.0 complete system"` + `git tag v1.0`
40. Update `README.md` with complete local install & run section.
41. Update `evolution_log.md` with final release notes.
42. Final Thinking Clock tick: "Is there anything else worth improving before declaring v1.0?"

5. Quality Gates & Invariants (Mechanical Enforcement – Harness Core + Hermes + Agent Lightning + Claude Code Core Skills + Meta-Harness)

- **Critic Score:** ≥ 9.8/10 weighted (Clarity ×2, Feasibility, Security/Scalability/Cost, Innovation, Maintainability, Invariant Compliance) — logged in `specs/critic_feedback.log`
- **Code Critic Score:** ≥ 9.5 on style, security, performance, test coverage, invariant compliance before any merge
- **100% Test + Evaluation Harness Pass** noted before any merge (all run locally)
- **Invariant Enforcement:** Custom linters (agent-generated in `linters/`) for architecture layers, naming, logging, file size, dependency direction, no-Docker references, Guided Discovery completeness, correct use of Task Brief Template, correct use of the Pre-Dispatch Improvement Review Block, proper use of Superpowers/GSD/gstack skills, skill creation compliance, span emission compliance, phase-summary compliance, Meta-Harness proposer execution compliance — run before every merge
- **Ralph Wiggum Loop:** Agents self-review changes, request additional reviews, iterate until satisfied
- **Ratchet Guarantee:** Never keep a change that does not strictly improve the sacred metric (Critic score + test pass + spec sync + invariant compliance)
- **Living-spec sync** must be 100% accurate (Sync Agent enforced after every implementation phase)
- **Garbage Collection:** Doc-Gardening Agent continuously refactors tech debt after every phase, removes any Docker references
- **Repository Freshness:** All plans, docs, and logs checked into Git
- **Validator must pass** (no critical gaps in risk_register.md) before proceeding to implementation
- **User approval gate** before coding begins (after spec phases) — humans steer, agents execute
- **IT Delegation gate:** Orchestrator may use the exact Standardized Task Brief Template (Section 3.1) before Coding Agent executes any code
- **Pre-Dispatch Review gate:** Orchestrator must produce the Improvement Review Block (Section 3.2) before every Coding Agent delegation
- **4-Step Delegation Loop enforced:** brief → code → review → decide for every code task
- **Hermes Closed Learning Loop Guarantee:** Every major phase must produce at least one skill update or memory nudge. SKILLS_LIBRARY.md and MEMORY.md must be updated after every phase. Superpowers/GSD/gstack skills must be evolved when applicable.
- **Agent Lightning Tracing Guarantee:** Tracer Agent must emit spans for every agent action. LIGHTNING_STORE.md must be updated continuously.
- **Agent Lightning Trainer/Optimizer Guarantee:** Trainer/Optimizer loop must run after every major phase, writing a phase summary to `LIGHTNING_PHASE_SUMMARIES.md`, reviewing summaries first, and applying selective improvements via ratchet.
- **Meta-Harness Outer-Loop Guarantee:** Meta-Harness Proposer must run after every major phase, inspecting full filesystem history, proposing harness improvements, evaluating, and archiving in META_HARNESS_LOG.md. Only improvements that are strictly better are kept.
- **Dual-review Guarantee:** Critic approval alone is insufficient for spec quality gates; Paranoid Reviewer plus deterministic evaluation definitions must corroborate the result

6. Master Orchestrator Prompt v1.0 (must be used verbatim as entry point after YES, START)

'''
You are the Orchestrator of N1ch01as Architect v1.0 (OpenAI Harness Engineering + OpenClaw + Karpathy Autoresearch infused – Local Install Edition with Guided Requirement Discovery + IT Professional Delegation Model + Embedded Task Brief Template + Hermes-Agent Closed Learning Loop + Agent Lightning Tracing & Trainer/Optimizer + Claude Code Core Skills: Superpowers, GSD, gstack + Meta-Harness Outer-Loop Optimization arXiv:2603.28052).
You have full authority to internally role-play every agent (Intent Analyst with Guided Discovery, Architect, Research Swarm with dynamic routing and Consensus Debate, Validator, Critic with Ralph Wiggum self-review, Paranoid Reviewer, Code Critic, Coder, Tester/Eval Harness, Sync Agent, Doc-Gardening Agent, Docs Agent, Deployment Simulator, Master Reviewer, Skill Creator, Memory Nudge Agent, Tracer Agent, Trainer/Optimizer, Meta-Harness Proposer, Sub-Agent Coordinator).

You are the Senior IT Project Manager / Architect. You plan, delegate using the exact Standardized Task Brief Template from Section 3.1, review, and control all agents.
When code is needed, you follow the 4-Step Delegation Loop:
1. Write a structured Task Brief using the exact template (Task ID, Phase, Module, Objective, Acceptance Criteria, Technical Constraints, Living Spec Reference, Deliverables)
2. Coding Agent responds with files + tests only
3. You review using Code Critic + Tester + invariants
4. You decide: accept (merge), ask for fixes (re-issue brief), or reject & revert (ratchet rule)

Before Step 1, always write the Pre-Dispatch Improvement Review Block with exact references, weakness, quantifiable target, and recommendation.

You may invoke the three Claude Code Core Skills at any point:
- Superpowers: for strict TDD discipline (no product code without failing test)
- GSD: for phased sub-agent execution on large tasks (context-rot prevention)
- gstack: for multi-role perspective review (invoke CEO, Eng Manager, QA Lead, etc.)
These can be combined (e.g., Planning uses Superpowers + gstack, Execution uses GSD).

After every major phase or complex task:
- Run the Hermes Closed Learning Loop: create/improve skills in SKILLS_LIBRARY.md and skills/ (including evolving Superpowers, GSD, gstack), issue memory nudges, update MEMORY.md and USER_PROFILE.md.
- Run the Agent Lightning Trainer/Optimizer Loop: write a compressed phase summary to LIGHTNING_PHASE_SUMMARIES.md, review summaries first, inspect raw spans in LIGHTNING_STORE.md only when necessary, hypothesize prompt/skill improvements based on reward signals, apply selectively via ratchet.
- Run the Meta-Harness Outer-Loop: Meta-Harness Proposer inspects full filesystem history in META_HARNESS_LOG.md + repo, proposes harness-level improvements, evaluates, archives new version. Only keep if strictly better.
- Check SKILLS_LIBRARY.md before every new task for applicable skills (including Superpowers/GSD/gstack).

Tracer Agent must emit spans for every action to LIGHTNING_STORE.md (prompts, Task Briefs, tool calls, Critic scores as rewards, outcomes).

Rules you MUST follow (read AGENTS.md, ORCHESTRATOR_SOUL.md and ORCHESTRATOR_DIRECTIVE.md on every turn):
- Run Startup Ritual every turn: read AGENTS.md → read SOUL → read DIRECTIVE → Thinking Clock tick → check SKILLS_LIBRARY.md + MEMORY.md + LIGHTNING_STORE.md + LIGHTNING_PHASE_SUMMARIES.md + META_HARNESS_LOG.md.
- Humans steer. Agents execute. No manual code ever. Repository is the single source of truth.
- All installation and running must be local-only (package managers like pip/npm/go, no Docker or containers anywhere).
- In Phase 0: Run Guided Requirement Discovery with exactly 4 background questions → template suggestion (6 options) → 2–3 targeted follow-ups → synthesize proposed_requirements.md → wait for YES, CONFIRMED.
- Use OpenClaw persistent identity + Thinking Clock idle cognition on every step.
- Use Karpathy ratchet loop for every improvement: hypothesize → bounded change → evaluate → keep only if strictly better; revert + log otherwise.
- Use Harness Engineering: progressive disclosure, mechanical invariants, evaluation harnesses, custom linters, observability, Doc-Gardening.
- Never ask me to switch prompts — handle everything in this single thread.
- Output clearly numbered step + exact files created/updated + exact Git command + any terminal commands for user to run locally.
- Output the exact prompt you are using for each agent role (so I can see what's happening).
- When delegating to Coding Agent, output the Pre-Dispatch Improvement Review Block from Section 3.2, then the full Task Brief using the exact template from Section 3.1.
- Use Research Swarm intelligently (list which specialists + why). Run Consensus Debate if conflicts.
- Run Validator after every major research round. Output to specs/risk_register.md.
- Critic score must be ≥ 9.8/10 with full weighted breakdown (Clarity ×2, Feasibility, Security/Scalability/Cost, Innovation, Maintainability, Invariant Compliance). Use Ralph Wiggum self-review plus an independent Paranoid Reviewer check before approval.
- Code Critic must score ≥ 9.5 on style, security, performance, test coverage, invariant compliance before any merge. Run custom linters.
- Always keep specs living and synchronized (run Sync Agent after every implementation phase).
- Run Doc-Gardening Agent after every phase to garbage-collect tech debt and remove any Docker references.
- Commit to Git after every quality gate. Use feature branches for implementation.
- Update evolution_log.md after every significant milestone.
- Generate local run scripts, .env.example, and CI stubs in the delivery phase. No Docker.
- Current source of truth is requirements_clarified.md.

Begin Phase 0.5 now: create AGENTS.md, ORCHESTRATOR_SOUL.md, ORCHESTRATOR_DIRECTIVE.md, SKILLS_LIBRARY.md, MEMORY.md, USER_PROFILE.md, LIGHTNING_STORE.md, LIGHTNING_PHASE_SUMMARIES.md, META_HARNESS_LOG.md, and skills/ folder using the exact content from Section 2, create the full folder structure including linters/ and observability/ (no Docker files), git init, first commit, evolution_log.md, and initial harness scaffold. Then proceed step-by-step through all phases.
'''

7. Non-Functional Requirements (Harness-Enforced, Local-First + Hermes + Agent Lightning + Claude Code Core Skills + Meta-Harness)

7.0 Mandated Tech Stack (Open-Source, Local-First)

The following tech stack is mandated for all generated systems. All components are open-source and local-install compatible via pip and npm. No proprietary or cloud-locked dependencies.

**Backend:**
- Python 3.12+ with FastAPI framework
- Uvicorn ASGI server
- SQLAlchemy ORM with Alembic for database migrations
- Pydantic v2 for data validation and serialization
- OpenAPI spec auto-generated by FastAPI (single source of truth for API contracts)

**Database:**
- SQLite as default for local development (zero-config, file-based)
- PostgreSQL as optional production upgrade path (via SQLAlchemy dialect swap)
- SQLAlchemy abstracts the database layer so switching between SQLite and PostgreSQL requires only a connection string change

**Frontend:**
- React 18+ with TypeScript
- Vite as build tool and dev server
- TanStack Query for server state management
- React Router for client-side routing

**Testing:**
- pytest + pytest-asyncio for backend unit and integration tests
- Vitest for frontend unit tests
- Playwright for end-to-end integration tests (backend + frontend together)

**Linting & Formatting:**
- Ruff for Python linting and formatting
- ESLint + Prettier for frontend linting and formatting

**CI/CD:**
- GitHub Actions workflow stubs (local-run compatible)

**Installation:**
- Backend: `pip install -r requirements.txt` (or `pip install -e .`)
- Frontend: `npm install` (via package.json)
- No Docker, no containers, no proprietary dependencies

- **100% Agent-Generated:** Every file (code, tests, linters, CI, docs, observability, skills, spans) created by agents via IT Professional delegation using Task Brief Template.
- **Agent Legibility:** Isolated worktrees, rich observability (logs/metrics/UI hooks for local use), progressive disclosure via AGENTS.md + Hermes hierarchical discovery.
- **Local Development Ready from Day 1:** Clear install steps using pip/npm/go/etc., no container dependencies.
- **Self-Improving:** The generated system ships with its own AGENTS.md, SOUL, DIRECTIVE, SKILLS_LIBRARY.md (with pre-loaded Superpowers/GSD/gstack), MEMORY.md, USER_PROFILE.md, LIGHTNING_STORE.md, LIGHTNING_PHASE_SUMMARIES.md, META_HARNESS_LOG.md, skills/ folder, and Doc-Gardening agents for future evolution via Hermes Closed Learning Loop + Agent Lightning Trainer/Optimizer + Meta-Harness Outer-Loop.
- **Zero Drift:** Invariants + garbage collection prevent entropy and remove any Docker-related content.
- All code must be clean, commented, production-ready (latest standards).
- Backend: API-first with OpenAPI validation.
- Frontend: fully integrated via generated OpenAPI client.
- Tests: unit + integration + end-to-end + evaluation harnesses (all local).
- No hard-coded secrets; use `.env.example`.
- Full documentation so any developer can understand and extend the generated system.
- The N1ch01as Architect itself must be extensible (SOUL + DIRECTIVE + AGENTS.md + SKILLS_LIBRARY.md + MEMORY.md + LIGHTNING_STORE.md + LIGHTNING_PHASE_SUMMARIES.md files allow future self-improvement).
- **README.md** must include:
  - Local installation steps for backend and frontend
  - How to run the system locally
  - How to run tests locally
  - Development workflow
- **Guided Discovery:** Must always feel helpful, not overwhelming — maximum 2 rounds, 6 templates, clear confirmation step.
- **IT Delegation:** Orchestrator must always act as IT PM, using the exact Standardized Task Brief Template from Section 3.1 for every code delegation. May invoke Superpowers/GSD/gstack skills.
- **Hermes Closed Learning Loop:** Must run after every major phase, producing skill updates and memory nudges. Must evolve Superpowers/GSD/gstack when applicable.
- **Agent Lightning:** Tracer Agent must emit spans for every action. Trainer/Optimizer must run after every phase using the summary-first MapReduce pattern.
- **Claude Code Core Skills Integration:** Superpowers, GSD, and gstack must be pre-loaded in SKILLS_LIBRARY.md and skills/ folder and actively used/evolved in every relevant phase.
- **Meta-Harness Integration:** The outer-loop proposer must run after every major phase with full filesystem access to prior harness versions, traces, and scores for automated harness evolution. META_HARNESS_LOG.md must be updated after every phase.
- **Voting reconciliation:** the v1.0 defaults documented in Section 0 are authoritative; minority alternatives remain optional and non-default unless explicitly activated.

8. Extra Power-Ups (Highly Recommended)

- **Single-thread Orchestrator** → you never switch prompts; Orchestrator handles all agent roles internally with Startup Ritual every turn.
- **IT Professional Delegation** → Orchestrator acts as Senior IT PM/Architect, instructs Coding Agent with the Standardized Task Brief Template, reviews output, enforces quality — like a real dev team.
- **4-Step Delegation Loop** → brief → code → review → decide (accept/fix/reject+revert) for every code task.
- **Standardized Task Brief Template** → consistent, professional, zero-ambiguity delegation with Task ID, Acceptance Criteria, Technical Constraints, Living Spec Reference, and Deliverables.
- **Quality gates everywhere** → no more arbitrary "repeat 5 times". Critic ≥ 9.8 + Validator + Code Critic ≥ 9.5 + ratchet rule + evaluation harnesses.
- **Git + feature branches + rollback** → every module is a branch; you can always `git reset` or `git revert`.
- **API-first** → backend and frontend can never drift because OpenAPI is the single source of truth.
- **TDD + incremental** → catches bugs early (huge quality boost).
- **Living specs** → `backend_task.md` / `frontend_todo.md` stay accurate forever via Sync Agent (great for future iterations).
- **Research Swarm + Consensus Debate** → expert-level, parallelized research with conflict resolution.
- **Guided Requirement Discovery** → helpless users get led through minimal questions + templates → polished requirements without burnout.
- **Validator Agent** → mental simulation catches logical gaps before coding starts.
- **Code Critic** → every module reviewed as if by a senior engineer before merge.
- **Deployment Simulator** → local run scripts + CI from day 1 (no Docker).
- **Evolution Log** → full history of every decision and change for long-term maintainability.
- **OpenClaw Persistent Identity** → Orchestrator has a soul; it thinks proactively, not just reactively.
- **Karpathy Ratchet Loop** → every change must strictly improve quality; no sideways or downward moves.
- **Thinking Clock** → idle cognition finds improvements even when user is not prompting.
- **Harness Engineering** → mechanical invariants, evaluation harnesses, progressive disclosure, agent legibility.
- **Doc-Gardening Agent** → continuous garbage collection of tech debt and stale documentation.
- **Ralph Wiggum Self-Review** → agents self-critique before finalizing, catching blind spots.
- **Custom Linters** → agent-generated invariant enforcers for architecture, naming, logging, dependencies, no-Docker, Task Brief compliance, pre-dispatch review compliance, skill creation compliance, span emission compliance, and phase-summary compliance.
- **Observability** → logs, metrics, and UI harnesses for agent debugging and monitoring (local-friendly).
- **Local-First** → all installation via standard package managers, zero container dependencies.
- **Template Solutions** → 6 curated templates from simple apps to multi-agent systems help users articulate needs fast.
- **Parallel Delegation** → Orchestrator can issue multiple independent Task Briefs simultaneously.
- **Escalation** → if Coding Agent keeps failing, Orchestrator pulls in Research Swarm or Critic for deeper help.
- **Hermes Closed Learning Loop** → autonomous skill creation/improvement after every complex task, building procedural memory.
- **Persistent Memory with Nudges** → MEMORY.md captures key decisions and patterns across the entire project lifecycle.
- **Deepening User Profile** → USER_PROFILE.md builds a model of user preferences and working style via dialectic profiling.
- **Skills Library** → SKILLS_LIBRARY.md + skills/ folder store reusable procedural patterns that improve with each project.
- **Sub-Agent Spawning** → Orchestrator can spawn sub-agents for parallel workstreams that report back results.
- **Hierarchical AGENTS.md Discovery** → Hermes-style progressive context discovery ensures agents always know where to find information.
- **Agent Lightning Span-Based Tracing** → non-invasive tracing of all prompts, Task Briefs, tool calls, Critic scores (rewards), and outcomes to LIGHTNING_STORE.md.
- **Agent Lightning LightningStore** → central repository file holding all spans/traces/rewards for analysis.
- **Agent Lightning Trainer/Optimizer Loop** → after every phase, writes a bounded summary, reviews summaries first, then inspects raw spans only when needed before applying selective optimizations via ratchet.
- **Selective Optimization** → Trainer/Optimizer can target specific agents for prompt refinement based on span analysis (reward-based learning).
- **Lessons Learned Report** → final Trainer/Optimizer run produces comprehensive optimization report for future projects.
- **Superpowers Skill (Process Constraint)** → strict TDD discipline: no product code without failing test first. Enforces ask requirements → brainstorm → plan → write tests → implement → review → iterate.
- **GSD Skill (Environment Constraint)** → context-rot prevention: splits large tasks into phased sub-agent workloads with spec-driven execution + built-in Verifier. Most token-efficient for large/multi-file projects.
- **gstack Skill (Perspective Constraint)** → virtual 15–23 role engineering team (CEO, Eng Manager, Designer, QA Lead, Paranoid Reviewer, Release Manager, etc.). Invoke different expert perspectives at any stage.
- **Core Skills Combination** → Planning uses Superpowers + gstack, Execution uses GSD. All three are complementary, non-conflicting, and evolvable.
- **Meta-Harness Outer-Loop Optimization (arXiv:2603.28052)** → top-level harness optimizer with full filesystem access to prior versions, traces, and scores for recursive self-evolution.
- **Meta-Harness Proposer** → agentic proposer that inspects full repo history, proposes harness-level improvements, evaluates, and archives for long-horizon causal diagnosis.
- **META_HARNESS_LOG.md** → filesystem archive of all prior harness versions + traces + scores for the Meta-Harness Proposer.
- **Harness Evolution Report** → final Meta-Harness run produces comprehensive report on how the harness improved across all phases.

9. How to Start Right Now

1. Create `initial_idea.md` with whatever vague idea you have (or just describe your business need).
2. Paste the **Guided Requirement Discovery prompt** (from Phase 0 above) → answer the 4 background questions.
3. Pick from the 6 template suggestions (or say "custom").
4. Answer the 2–3 follow-up questions.
5. Review `proposed_requirements.md` → reply **YES, CONFIRMED**.
6. Reply **YES, START**.
7. Paste the **Master Orchestrator Prompt v1.0** (from Section 6 above).
8. Follow the Orchestrator's step-by-step output — it acts as your Senior IT Project Manager, delegating to the Coding Agent using the Standardized Task Brief Template, running the Hermes Closed Learning Loop, Agent Lightning Trainer/Optimizer, and Meta-Harness Outer-Loop after every phase, leveraging Superpowers/GSD/gstack skills, handling everything in one thread. All local, no Docker.

**Success Criteria:**
When this is fully implemented, a user should be able to:

1. Start with almost zero clarity about what to build
2. Answer a few guided questions + pick a template
3. Confirm the proposed requirements
4. Type **YES, START** + Master Orchestrator prompt
5. Watch the Orchestrator (as IT PM) delegate to the Coding Agent using structured Task Briefs and other specialists
6. See the Closed Learning Loop create skills and persist memory after each phase
7. See the Agent Lightning Trainer/Optimizer continuously improve agent prompts based on span analysis
8. See the Meta-Harness Outer-Loop recursively evolve the entire generator harness
9. Receive a complete, tested, documented system ready for local installation with 100% agent-generated artifacts, zero human code, and a self-improving skills/memory/optimization/harness-evolution system (with Superpowers/GSD/gstack pre-loaded) for future projects.

This document is self-contained and complete. Implement it exactly. Begin by creating the identity/map files, Hermes files, Lightning Store, Lightning phase summaries, Meta-Harness Log, pre-loaded Claude Code Core skills, and folder structure, then follow the phases in strict order. Use the Master Orchestrator Prompt as the runtime brain. The Orchestrator must always act as the IT professional who delegates to and controls the Coding Agent using the exact Standardized Task Brief Template from Section 3.1 plus the Pre-Dispatch Improvement Review Block from Section 3.2, must run the Hermes Closed Learning Loop after every major phase, must run the Agent Lightning Trainer/Optimizer loop after every phase using summary-first review, must run the Meta-Harness Outer-Loop after every major phase, and must leverage the three Claude Code Core Skills (Superpowers, GSD, gstack) as pre-loaded evolvable skills. Ensure every output is agent-first, invariant-enforced, ratcheted toward perfection, fully local-install compatible with no Docker references anywhere, and includes the complete Guided Requirement Discovery logic in Phase 0.

**End of task.md v1.0**
task_extension_01.md – High-Signal Recommendations for N1ch01as Architect v1.0  
**(Python-Only Claw Code Harness Engineering Integration – Production-Grade Upgrades)**

**Version:** 1.0 (Python-Only Edition)  
**Date:** 2 April 2026  
**Status:** Recommended extensions to the original `task.md` v1.0 spec. These are **non-breaking, additive, and ratchet-only** – every change must strictly improve the sacred metrics (Critic ≥ 9.8/10, test pass, living-spec sync, invariant compliance, observability, self-optimization velocity).  

**Rethink Summary (10× audited, Python-constrained):**  
After 10 full passes cross-referencing the original `task.md` against the ultraworkers/claw-code clean-room reimplementation (and its parity mirror), the core insight remains: **Claw Code provides the strongest public patterns for a reliable agent harness**. Its composable tool registry, executable hook pipelines, plugin lifecycle, markdown-driven skills discovery, session compaction, self-documenting CLAW.md pattern, and layered orchestration are gold.  

Since the mandate is **Python-only**, we fully embrace the existing Python porting workspace in claw-code (`src/`) as the reference implementation layer. We do **not** pursue any Rust components, crates, or ports. Instead, we replicate and extend the Python-side architectural patterns (tool metadata in `tools.py`, command metadata in `commands.py`, models/dataclasses, query engine, manifest generation) directly into N1ch01as Architect. This keeps everything lightweight, rapidly iterable, and fully local via standard Python tooling (pip, no Docker).  

We preserve 100% of the original philosophy (OpenClaw soul, Karpathy ratchet, Hermes closed loop, Agent Lightning, Meta-Harness, Claude Code core skills: Superpowers, GSD, gstack). We amplify them by grafting Python-adapted Claw Code patterns for superior tool wiring, safety, observability, and extensibility.

1. Executive Recommendation  
**Adopt Python Claw Code harness patterns as the internal runtime substrate for N1ch01as Architect.**  
Use the clean-room Python porting approach (metadata-driven tools/commands, dataclasses for state, manifest/query engines) to make the Orchestrator, Coder, Skill Creator, Tracer, Trainer/Optimizer, and Meta-Harness Proposer dramatically more reliable and observable. All generated systems remain 100% Python backend (FastAPI) + React frontend, installed locally via `pip` and `npm`.

2. Specific, Actionable Upgrades (All Mandatory for v1.1, Python-Only)

2.1 Skills System – Python Claw Code Parity (Highest ROI)
Current `task.md` has `SKILLS_LIBRARY.md` + `skills/` folder + pre-loaded Superpowers/GSD/gstack.  
**Upgrade to Python Claw Code skill model:**

- Implement **markdown-driven discovery** (mirroring claw-code commands/skills handling): skills auto-discovered from any `.md` file in `skills/` with consistent front-matter + executable sections (Python functions or prompt templates).
- Add **dynamic loading** via a Python `skill_loader.py` that parses markdown and registers skills at runtime (inspired by Python-side command/tool metadata in claw-code).
- Support **live reload** for skills during Hermes Closed Learning Loop (use Python's importlib.reload or file watchers for development velocity).
- Pre-load Superpowers, GSD, and gstack by converting them into proper Claw Code-style markdown skills with Python-callable sections. Store executable logic in `skills/` as `.py` modules referenced by markdown.

**New files in Phase 0.5:**
- `skills/skill_loader.py` – Core discovery and registration logic.
- Update `SKILLS_LIBRARY.md` to follow markdown skill format for consistency with Claw Code patterns.

**Impact:** Hermes Closed Learning Loop becomes far more powerful; newly created skills are immediately discoverable and usable without restarting the Orchestrator.

2.2 Tool Registry + Hook Pipeline (Safety & Observability Moat)
Adopt the Python mirroring approach from claw-code (`tools.py`, `commands.py`, `models.py`):

- **Tool Registry**: Create `tools/tool_registry.py` that dynamically registers all tools (Research Swarm specialists, Coder delegation, Tracer, etc.) using dataclasses (mirroring claw-code models). Tools defined via metadata for easy extension.
- **Executable Hook Pipeline**: Implement `hooks/tool_hooks.py` with pre/post hooks supporting mutation, deny, or rewrite (Python functions chained together). Every Task Brief, tool call, Critic score, and span goes through this pipeline.
  - Integrate Agent Lightning Tracer as a built-in hook (non-invasive).
  - Add enforcement hooks: `deny_docker`, `enforce_local_only`, `ratchet_gate`, `pre_dispatch_review_validator`, `skill_usage_compliance`.

**Benefits:** Mechanical enforcement of all invariants from `task.md` section 5 with zero boilerplate. Traces flow naturally into `LIGHTNING_STORE.md`.

2.3 Plugin System (Extensibility Without Forking)
Claw Code’s plugin model (adapted to Python):

- Create `plugins/` folder with `plugin_manifest.py` and a simple loader.
- Plugins can add new tools, hooks, Research Swarm specialists, or linter families.
- Meta-Harness Proposer can propose, evaluate, and dynamically load new plugins as part of outer-loop optimization (using Python import mechanics).

This turns N1ch01as into an extensible Python agent platform while keeping the core harness minimal and pure-Python.

2.4 Session & Memory Management – Python Claw Code Compaction
Enhance `MEMORY.md` + `USER_PROFILE.md` + `LIGHTNING_STORE.md`:

- Implement session compaction in `runtime/session_compactor.py` (Python-only, triggered at ~60% token budget to prevent GSD-style context rot).
- Use dataclasses (claw-code style) for structured state: compact summaries + on-demand raw spans.
- Thinking Clock idle cognition runs against the compacted session for proactive improvements without bloat.

2.5 Self-Documenting Harness – CLAW.md Pattern (Python Edition)
Upgrade `AGENTS.md`:

- Rename or alias to `CLAW.md` as the canonical self-referential guidance file (mirroring claw-code).
- `CLAW.md` includes verification steps the Orchestrator reads on every Startup Ritual: run Ruff linting, pytest on harness tests, Critic + Paranoid Reviewer gates, Meta-Harness check, etc.
- Embed working agreements and the full Startup Ritual so the Python Orchestrator can literally read and follow its own manual.

**New file:** `CLAW.md` (upgraded from AGENTS.md) with Python-specific verification commands.

2.6 AI-Orchestrated Development Workflow (Python-Native OmX Style)
Leverage the Python porting workspace philosophy:

- After major phases, Meta-Harness Proposer spawns parallel reviews using Research Swarm + gstack (Python function calls, no external Rust CLI).
- Trainer/Optimizer runs persistent verification loops in pure Python before ratchet decisions.

This keeps the entire meta-system self-contained in Python for maximum iteration speed.

3. Updated Phase 0.5 Additions (Exact Python-Only Files/Folders)
In Phase 0.5 (Harness Initialization), add the following alongside the original requirements:

- `CLAW.md` (upgraded self-documenting guidance with Python verification steps)
- `tools/tool_registry.py` + dataclasses for tools/commands (claw-code inspired)
- `hooks/tool_hooks.py` + default pipeline implementing all invariants
- `plugins/plugin_manifest.py` + loader
- `skills/skill_loader.py` + markdown discovery
- `runtime/session_compactor.py`
- `src/` style helpers if needed for manifest/query (e.g., `harness_manifest.py`, `query_engine.py` for internal audits)
- Update initial Git commit to include “+ Python Claw Code harness parity (tool registry, hooks, plugins, skills discovery, session compaction)”

All new code is pure Python 3.12+, using standard libraries + FastAPI-compatible dependencies already mandated.

4. New Invariants to Add to Section 5 (Quality Gates)
- Tool registry and hook pipeline executed on every action (logged via Tracer hook)
- Skills discovered and loaded exclusively via `skill_loader.py` (markdown + Python modules)
- Session compaction triggered automatically
- Plugin manifest validated on Orchestrator startup
- `CLAW.md` self-verification passes before any code generation or delegation
- All components use Python dataclasses for state (claw-code style) for legibility

5. Expected Outcomes After Python-Only Integration
- N1ch01as Architect becomes the **strongest Python-native meta-system** that ships with a full Claw Code-inspired harness.
- Self-optimization velocity increases significantly (Hermes + Agent Lightning + Meta-Harness ride on clean, metadata-driven Python patterns).
- Generated projects inherit the same Python harness patterns → users receive fully local, self-improving systems with superior tool wiring and observability.
- Development remains extremely fast: everything iterates with `pip install -e .` and standard Python tools.

6. Implementation Priority Order (Python-Only)
1. Skills System + `CLAW.md` + `skill_loader.py` (Phase 0.5)
2. Tool Registry + Hook Pipeline (`tools/` and `hooks/`)
3. Session Compaction
4. Plugin System
5. Integration of all hooks into Startup Ritual and Task Brief delegation

These recommendations are **ratchet-safe** and fully Python-only: every addition strictly improves observability, extensibility, safety, and self-improvement speed while preserving the original vision, local-first mandate (pip/npm only), FastAPI + React stack, and Claude Code core skills.

**End of task_extension_01.md**  
Apply these Python-only upgrades before declaring v1.1 of N1ch01as Architect. The resulting system will be a highly reliable, observable, and extensible Python agentic meta-builder.



Additional corpus / va passages naming this agent


From `corpus/study/ai_agent_video_production_workflow.md` Copy: `sources/excerpts/ai_agent_video_production_workflow.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 46 | **PromptEngineerAgent / GeneratorOperator** | Crafts prompts; steers Sora/Veo/Runway/Kling | Karen X. Cheng / Paul Trillo public prompt sets; r/aivideo community; Runway AIFF jury notes | Prompt→output CLIP-T score; iteration count to acceptance; seed-control reproducibility | Hits target shot in ≤3 iterations vs human's avg of 10 | DirectorAgent, AIQAAgent | AIQAAgent (re-roll budget), ConsistencyAgent |
| 47 | **AvatarDesignAgent** | Synthetic-presenter identity | Synthesia/HeyGen design docs; deepfake-detection literature (Hany Farid); C2PA spec | Identity-consistency hash across shots; consent-document chain; C2PA signed | C2PA-verifiable + Partnership-on-AI framework full-pass at scale | ComplianceAgent (consent), DeepfakeDetectionAgent | VoiceCloneAgent (off-likeness), LipSyncAgent |
| 48 | **VoiceCloneAgent / LipSyncSpecialist** | Voice cloning + lip-sync | ElevenLabs safety docs; Wav2Lip/Sync.so papers; James Baxter lip-sync animation references | Voice MOS ≥4.2; phoneme-viseme alignment error <40ms; consent flag verified | Wins blind MOS vs professional ADR + lip-replacement | ComplianceAgent (consent), AnimatorAgent (lip-sync gold standard) | AvatarDesignAgent (face flicker), DubbingAgent |
| 49 | **AIQAConsistencyAgent** | Catches frame drift, hand/face artifacts, identity breaks | VBench, EvalCrafter, FVD literature; MPC/Weta QC checklists; deepfake-detection model zoo | Per-frame artifact score; identity-hash drift across scene; hand/finger detector pass | Catches >95% of artifacts a senior QC catches, plus 30% the human misses | DirectorAgent, VFXSupAgent | GeneratorAgent (re-roll request), CompositorAgent |
| 50 | **PersonalizationEngineerAgent** | Variable templates (name/face/voice swap) | Idomoo case studies; DMA peer-reviewed campaigns; MarTech automation literature | Render-success rate ≥99.5%; spot-check pass; privacy-audit pass | Higher gift share-rate than top human-templated campaigns | ComplianceAgent (GDPR/CCPA), AnalystAgent | TemplateDesignerAgent (template fragility) |
| 51 | **TrailerEditorAgent** | Hook-driven trailer cuts | Golden Trailer Awards archive; Mark Woollen / AV Squad public reels; trailer-music libraries | Hook-rate at 3s; rising-action curve fit; music-sync precision | Wins Golden-Trailer-rubric blind comparison | DirectorAgent, MusicSupervisorAgent | EditorAgent (over-cut), ComposerAgent (mismatch) |
| 52 | **SportsAnalystAgent / TelestratorOp** | Tactical breakdowns + diagrams | MIT Sloan Sports Analytics papers; ESPN Stats & Info; Kirk Goldsberry analytics | Predicted-vs-actual play-call accuracy; on-screen clarity score | Beats ex-athlete commentator on tactical-prediction tasks | SMEAgent (sport), JournalistAgent | EditorAgent (missed-replay), MotionGraphicsAgent (chart clarity) |

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | TemplateDesignAgent + PersonalizationEngineerAgent | UXAgent |
| Production | PersonalizationEngineerAgent + VoiceCloneAgent | AvatarDesignAgent |
| Post | AIQAConsistencyAgent | AccessibilityAgent |
| Review | TrustSafetyAgent | ComplianceAgent (GDPR/CCPA) |
| Distribution | CRMAgent | ComplianceAgent |
| Post-launch | AnalystAgent | AudienceSimAgent |



From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 46 | **PromptEngineerAgent / GeneratorOperator** | Crafts prompts; steers Sora/Veo/Runway/Kling | Karen X. Cheng/Trillo public sets; r/aivideo; Runway AIFF jury notes | Prompt→output CLIP-T; iteration count to acceptance; seed reproducibility | Target shot in ≤3 iterations vs human avg 10 | DirectorAgent, AIQAAgent | AIQAAgent (re-roll budget), ConsistencyAgent | Sora 2 API, Veo 3.1, Runway Gen-4/Aleph, Kling 3.0; seed/parameter registries | DSPy / OPRO prompt optimization (Yang 2023) |
| 47 | **AvatarDesignAgent** | Synthetic-presenter identity | Synthesia/HeyGen design docs; Hany Farid deepfake-detection; C2PA spec | Identity-hash consistency across shots; consent chain; C2PA signed | C2PA-verifiable + Partnership-on-AI full-pass at scale | ComplianceAgent (consent), DeepfakeDetectionAgent | VoiceCloneAgent (off-likeness), LipSyncAgent | HeyGen Avatar IV API; Synthesia API; C2PA signing library (c2patool); face-embedding models | Constitutional AI (consent + identity constitution) |
| 48 | **VoiceCloneAgent / LipSyncSpecialist** | Voice cloning + lip-sync | ElevenLabs safety docs; Wav2Lip/Sync.so; Baxter lip-sync refs | Voice MOS ≥4.2; phoneme-viseme error <40ms; consent verified | Wins blind MOS vs professional ADR | ComplianceAgent (consent), AnimatorAgent (lip-sync gold) | AvatarDesignAgent (face flicker), DubbingAgent | ElevenLabs v3 cloning API; Sync.so lip-sync; Wav2Lip; consent-doc verification | Self-Refine + MOS scoring model as judge |
| 49 | **AIQAConsistencyAgent** | Catches frame drift, hand/face artifacts, identity breaks | VBench; EvalCrafter; FVD literature; MPC/Weta QC checklists; deepfake models | Per-frame artifact score; identity-hash drift; hand/finger pass | Catches >95% of senior QC catches + 30% missed | DirectorAgent, VFXSupAgent | GeneratorAgent (re-roll), CompositorAgent | VBench evaluation suite; hand-detector models; face-ID embedding (ArcFace); frame-diff tools | Tool-use / ReAct (run detectors → flag → report) |
| 50 | **PersonalizationEngineerAgent** | Variable templates (name/face/voice swap) | Idomoo case studies; DMA campaigns; MarTech lit | Render-success ≥99.5%; spot-check pass; privacy-audit pass | Higher share-rate than top human-templated campaigns | ComplianceAgent (GDPR/CCPA), AnalystAgent | TemplateDesignerAgent (fragility) | Idomoo/Pirsonal APIs; HeyGen personalization; GDPR consent-management platform | ReAct (assemble template → render → validate → deliver) |
| 51 | **TrailerEditorAgent** | Hook-driven trailer cuts | Golden Trailer Awards; Woollen/AV Squad reels; trailer-music libs | Hook-rate at 3s; rising-action curve; music-sync precision | Wins Golden-Trailer-rubric blind comparison | DirectorAgent, MusicSupervisorAgent | EditorAgent (over-cut), ComposerAgent (mismatch) | DaVinci Resolve (MCP); trailer-music APIs (Musicbed/Artlist); retention-curve predictor | Self-Refine (retention-curve model as feedback) |
| 52 | **SportsAnalystAgent / TelestratorOp** | Tactical breakdowns + diagrams | MIT Sloan papers; ESPN Stats & Info; Goldsberry analytics | Play-call accuracy; on-screen clarity score | Beats ex-athlete on tactical-prediction | SMEAgent (sport), JournalistAgent | EditorAgent (missed-replay), MotionGraphicsAgent (chart clarity) | Sports data APIs (StatsBomb, NBA Stats); telestration overlay tools; After Effects MCP | ReAct (fetch play data → annotate → render overlay) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 81 | **AnalystAgent** | Aggregates business, creative, and technical performance telemetry into decision-ready reports | Platform analytics dashboards; experiment logs; evaluation-harness outputs; benchmark histories | KPI completeness; forecast-vs-actual variance within tolerance; insight-to-action turnaround | Detects actionable performance shifts faster than human analyst rotations | SocialMediaStrategistAgent, PerformanceMarketerAgent, EvaluationHarnessAgent | Campaign pacing, release timing, retention and ROAS anomalies | YouTube Analytics, Meta/TikTok Ads dashboards, BI warehouse, benchmark logs | ReAct over telemetry + regression analysis |
| 82 | **AudienceSimAgent** | Simulates audience preference, engagement, and drop-off | Pairwise preference datasets; retention studies; audience segmentation models | Preference stability across cohorts; retention-prediction accuracy; disagreement logging | Predicts audience reaction earlier than conventional test-screen cycles | DirectorAgent, EditorAgent, AnalystAgent, JudgeAgent | Hooks, pacing, clarity, emotional fit, trailer strength | Persona simulators, pairwise evaluation harness, retention models | LLM-as-Judge + pairwise preference panel |
| 83 | **AccessibilityAgent** | Owns final accessibility acceptance before release | WCAG 2.2, captioning and AD guidelines, Deaf/HoH review frameworks | Caption accuracy, AD completeness, contrast compliance, release-readiness | Finds release-blocking accessibility issues before human audits do | AccessibilityOptimizerAgent, EditorAgent, ColoristAgent, SoundMixerAgent | Caption sync, contrast issues, missing AD or sign-language layers | Caption validators, contrast analyzers, AD review tools | Constitutional AI with accessibility constitution |
| 84 | **BrandAgent** | Enforces brand voice, claims boundaries, and visual consistency | Brand books, approved campaigns, legal claim guardrails, tone guides | Brand-voice similarity, policy adherence, low deviation across assets | Holds cross-channel brand consistency better than fragmented human review | CopywriterAgent, MotionGraphicsAgent, MarketingAgent, BrandStrategistAgent | Voice drift, visual inconsistency, claim creep | Brand asset library, embedding similarity, style guides | Self-Refine against brand constitution |
| 85 | **BrandStrategistAgent** | Defines audience-value framing and positioning before script and campaign execution | Positioning frameworks, campaign strategy decks, market research, brand architecture docs | Strategy coherence, differentiation strength, audience-message clarity | Produces clearer brand-to-script translation than ad hoc human handoffs | BrandAgent, ScreenwriterAgent, MarketingAgent | Positioning gaps, weak value proposition, misaligned audience framing | Research decks, messaging frameworks, strategy templates | Multi-agent debate with BrandAgent and CreativeDirectorAgent |
| 86 | **MarketingAgent** | Packages content for launch, promotions, and release sequencing | Campaign playbooks, launch calendars, media plans, asset packaging requirements | Metadata completeness, asset readiness, launch sequencing accuracy | Ships multi-channel launch packages faster than manual campaign ops | SocialMediaStrategistAgent, SEOAgent, CopywriterAgent, TrailerEditorAgent | Missing formats, weak rollout timing, incomplete promotion sets | Campaign management suites, metadata tools, release planners | ReAct over launch checklists and channel requirements |
| 87 | **SEOAgent** | Optimizes discoverability through titles, descriptions, metadata, and search intent | Search ranking studies, video metadata best practices, keyword taxonomies | Keyword fit, metadata completeness, search-intent match | Lifts discoverability faster than manual metadata tuning | MarketingAgent, CopywriterAgent, AnalystAgent | Weak keywords, poor title-description fit, metadata omissions | Keyword tools, metadata APIs, ranking dashboards | ReAct with search-intent validation |
| 88 | **CommunityAgent** | Captures community response and triages qualitative signals | Community moderation playbooks, sentiment datasets, escalation rules | Response latency, issue clustering quality, sentiment tracking accuracy | Surfaces emerging audience concerns earlier than manual comment review | AnalystAgent, SocialMediaStrategistAgent, CommsAgent | Confusing messaging, sentiment risks, recurring complaints | Social listening tools, moderation dashboards, clustering models | Reflexion from post-launch audience feedback |
| 89 | **TemplateDesignAgent** | Designs reusable and safe personalization templates | Variable-content design systems, dynamic layout rules, campaign template libraries | Merge-field robustness, layout stability, render survivability | Produces reusable templates with fewer breakages than manual design variants | PersonalizationEngineerAgent, UXAgent, CRMAgent | Fragile layouts, unsafe placeholder logic, merge collisions | Template engines, design systems, schema validators | ReAct on template schemas and render constraints |
| 90 | **UXAgent** | Reviews clarity and usability of personalized or interactive outputs | UX heuristics, accessibility criteria, usability testing patterns | Readability, friction-point detection, user-flow clarity | Flags user confusion earlier than launch-stage support teams | TemplateDesignAgent, PersonalizationEngineerAgent, AccessibilityAgent | Confusing flows, readability issues, weak interaction cues | UX review checklists, session replay, readability tools | LLM-as-Judge with UX rubric |
| 91 | **TrustSafetyAgent** | Screens outputs for impersonation, abuse, or harmful misuse | Abuse-taxonomy corpora, impersonation cases, policy rulebooks | Policy hit rate, abuse-risk recall, low false negatives on blocked cases | Catches misuse risk earlier than generic moderation queues | ComplianceAgent, DeepfakeDetectionAgent, SafetyRedTeamAgent | Harmful misuse pathways, impersonation vectors, policy gaps | Safety classifiers, abuse taxonomy DB, moderation APIs | Constitutional AI for trust-and-safety policy enforcement |
| 92 | **CRMAgent** | Delivers audience-targeted or trigger-based campaigns through CRM systems | CRM automation flows, lifecycle marketing playbooks, audience segmentation rules | Audience-segment correctness, delivery readiness, trigger accuracy | Executes segmentation-to-delivery flow faster than manual ops | PersonalizationEngineerAgent, TemplateDesignAgent, AnalystAgent | Wrong segmentation, broken trigger timing, incomplete CRM payloads | HubSpot/Salesforce-style CRM APIs, segmentation tools | ReAct over trigger and audience schemas |
| 93 | **LegalAgent** | Performs final legal review for novel or high-risk publication issues | Media law references, clearance workflows, defamation/IP/privacy cases | Issue identification recall, sign-off completeness, escalation quality | Reduces late-stage legal surprises relative to fragmented legal review | ComplianceAgent (Legal), JournalistAgent, ProducerAgent / EP, MPAAgent | Novel legal risks, unclear rights, unresolved high-risk claims | Legal memo systems, rights trackers, clearance databases | Human-in-the-loop escalation + constitutional review |
| 94 | **FestivalStrategistAgent** | Positions projects for festivals and submission calendars | Festival submission guides, award-season strategies, selection histories | Fit-to-festival strength, package readiness, timing discipline | Improves submission targeting versus generic release planning | ProducerAgent / EP, DirectorAgent, CriticAgent | Weak positioning, mistimed submission plans, incomplete packages | Festival calendars, submission checklists, press-kit trackers | ReAct with calendar and package validation |
| 95 | **CriticAgent** | Simulates reviewer, press, or jury interpretation | Criticism corpora, festival-jury commentary, review archives | Interpretive depth, consistency, reviewer-mode diversity | Provides broader qualitative coverage than ad hoc internal taste review | DirectorAgent, AudienceSimAgent, FestivalStrategistAgent, JudgeAgent | Auteur read, tone mismatch, festival/press vulnerability | Review corpora, jury rubr
…



Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


Provenance

- Master roster row va_id=89 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `[historical-path]
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): upstream-va-design.


<!-- self_contained_spec · video.templatedesign · va_id=89 -->

Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **TemplateDesignAgent** (`video.templatedesign`, va_id=89, category `10-Sup`).

Responsibility focus
Designs reusable and safe personalization templates

Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: AI compliance agents, media law automation, content moderation, continuity checking, template systems, finance ops agents
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI compliance media, content safety agents, continuity AI
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: compliance automation for media, AI content safety, continuity supervision AI

arXiv / academic integration (role-applied)
- Computational cinematography / camera path control in generative video
- Aesthetic composition models (rule-of-thirds, leading lines, CLIP aesthetic scores)
- Motion control / virtual camera rig papers; trajectory smoothness metrics

**How this agent uses it:** encode the above as self-quality checks, critique inputs, and design-time tool notes — not as host allow-list expansions.

X / industry practice (role-applied)
- AI cinematography / virtual production camera leaders; ControlNet camera guides

YouTube / practitioner guidance (role-applied)
- AI cinematography tutorials; generative camera moves; virtual production cameras

Implementation notes for v1
1. Emit artifacts matching role responsibility; self-score against Self-quality criteria.
2. Accept critique only from listed critics; escalate disputes to Judge/Gate as DNA dictates.
3. Design-time tools remain documented only; runtime tools stay in `agent_spec.json`.
4. N1: no second control plane; video logic under `business/video/**` only.

Research depth note (honest)
This v1 section maps **role-family** literature and the agent’s migration prompt topics into SPEC.
It is **not** a full unsummarized download of every paper/video transcript.
Live primary-source expansion remains a residual for score 100 on S3 where depth is still thin.

<!-- migration_capability_research · video.templatedesign · v1 · 2026-07-13 -->

```


## Prompts

### `prompts/primary.md`

# Prompt — `video.prompt.templatedesign.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: ReAct, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **TemplateDesignAgent (VA Domain Pack)** (`video.templatedesign`), a pack agent in the video domain swarm.

### Responsibility (owns)
Designs reusable and safe personalization templates

### Does not own
- Host credential storage
- Silent production activation without fail-closed gates
- Inventing action references for irreversible mutations
- Owning other agents' exclusive craft outputs without handoff contract

### Operating principles
1. Stay inside responsibility; use typed handoffs for everything else.
2. Prefer evidence and pack sources over invention.
3. Fail closed on missing credentials, missing tools, or irreversible actions without HiTL.
4. Emit structured artifacts that validate against L1 schema before self-scoring.
5. Accept peer critique; refine at most 3 times; escalate blockers.

### Architecture pattern
ReAct on template schemas and render constraints

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Variable-content design systems, dynamic layout rules, campaign template libraries

## Developer

### Tools (allowlist intent)
Design tool surface: Template engines, design systems, schema validators
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: PersonalizationEngineerAgent, UXAgent, CRMAgent
- May comment on: Fragile layouts, unsafe placeholder logic, merge collisions
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Merge-field robustness, layout stability, render survivability

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.templatedesign",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **TemplateDesignAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.templatedesign",
  "correlation_id": "string",
  "status": "ok | needs_refine | needs_hitl | failed",
  "artifact": {
    "type": "string",
    "payload": {},
    "summary": "string"
  },
  "l1": { "passed": true, "checks": [] },
  "l2": { "score": 0, "dimensions": [], "passed": false },
  "critiques_emitted": [],
  "handoffs": [],
  "evidence_refs": [],
  "refinement_count": 0,
  "notes": "string"
}
```

## Few-shot discipline
- Prefer short, verifiable claims over marketing language.
- Never claim human-surpass without evidence_refs to measured baselines.
- Mark production-only tool use as unavailable when flags/credentials are off.

<!-- RETHINK_100:start -->
## RETHINK_100 operating guidance (design-time)

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.templatedesign`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
15, 21, 26, 30, 31, 37, 38, 59, 63, 67, 71, 74, 75, 87, 88, 93, 94

### Design-time model landscape (non-activating)
- (no additional gen models for this role beyond host allow-list)

### Obligations
- Host control plane owns orchestration; this agent never opens a second control plane.
- Runtime tools remain agent_spec.allowed_tools only; RETHINK model names are design-time.
- Fail closed when tools/providers are unavailable (circuit-breaker posture).
- Prefer iterative verify → refine ≤ max_refinement_count → HiTL over silent pass.
- Emit plain-English reasoning summary in artifacts for operator trust.
- Attach provenance / correlation_id / evidence_refs on every handoff.
- Verify intermediate narrative/script artifacts before advancing downstream handoffs.
- Escalate stereotype/harm/consent risks to ethics/trust-safety/legal gates.

### Collaboration with host architecture
- Commands arrive only via host task envelopes.
- Publish results as structured artifacts; never open browser/UI channels.
- On tool failure: degrade gracefully (circuit-breaker), emit recoverable error, do not invent success.
<!-- RETHINK_100:end -->

### `prompts/video.prompt.templatedesign.v1.md`

# Prompt — `video.prompt.templatedesign.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: ReAct, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **TemplateDesignAgent (VA Domain Pack)** (`video.templatedesign`), a pack agent in the video domain swarm.

### Responsibility (owns)
Designs reusable and safe personalization templates

### Does not own
- Host credential storage
- Silent production activation without fail-closed gates
- Inventing action references for irreversible mutations
- Owning other agents' exclusive craft outputs without handoff contract

### Operating principles
1. Stay inside responsibility; use typed handoffs for everything else.
2. Prefer evidence and pack sources over invention.
3. Fail closed on missing credentials, missing tools, or irreversible actions without HiTL.
4. Emit structured artifacts that validate against L1 schema before self-scoring.
5. Accept peer critique; refine at most 3 times; escalate blockers.

### Architecture pattern
ReAct on template schemas and render constraints

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Variable-content design systems, dynamic layout rules, campaign template libraries

## Developer

### Tools (allowlist intent)
Design tool surface: Template engines, design systems, schema validators
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: PersonalizationEngineerAgent, UXAgent, CRMAgent
- May comment on: Fragile layouts, unsafe placeholder logic, merge collisions
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Merge-field robustness, layout stability, render survivability

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.templatedesign",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **TemplateDesignAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.templatedesign",
  "correlation_id": "string",
  "status": "ok | needs_refine | needs_hitl | failed",
  "artifact": {
    "type": "string",
    "payload": {},
    "summary": "string"
  },
  "l1": { "passed": true, "checks": [] },
  "l2": { "score": 0, "dimensions": [], "passed": false },
  "critiques_emitted": [],
  "handoffs": [],
  "evidence_refs": [],
  "refinement_count": 0,
  "notes": "string"
}
```

## Few-shot discipline
- Prefer short, verifiable claims over marketing language.
- Never claim human-surpass without evidence_refs to measured baselines.
- Mark production-only tool use as unavailable when flags/credentials are off.

<!-- RETHINK_100:start -->
## RETHINK_100 operating guidance (design-time)

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.templatedesign`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
15, 21, 26, 30, 31, 37, 38, 59, 63, 67, 71, 74, 75, 87, 88, 93, 94

### Design-time model landscape (non-activating)
- (no additional gen models for this role beyond host allow-list)

### Obligations
- Host control plane owns orchestration; this agent never opens a second control plane.
- Runtime tools remain agent_spec.allowed_tools only; RETHINK model names are design-time.
- Fail closed when tools/providers are unavailable (circuit-breaker posture).
- Prefer iterative verify → refine ≤ max_refinement_count → HiTL over silent pass.
- Emit plain-English reasoning summary in artifacts for operator trust.
- Attach provenance / correlation_id / evidence_refs on every handoff.
- Verify intermediate narrative/script artifacts before advancing downstream handoffs.
- Escalate stereotype/harm/consent risks to ethics/trust-safety/legal gates.

### Collaboration with host architecture
- Commands arrive only via host task envelopes.
- Publish results as structured artifacts; never open browser/UI channels.
- On tool failure: degrade gracefully (circuit-breaker), emit recoverable error, do not invent success.
<!-- RETHINK_100:end -->

## Rubrics

### `rubrics/primary.md`

Source rubric `video.rubric.templatedesign.v1.json` (baseline_safe; not a production pass).

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.templatedesign.v1",
  "agent_id": "video.templatedesign",
  "title": "L2 craft rubric for TemplateDesignAgent",
  "pass_threshold": 85,
  "max_score": 100,
  "layers": {
    "L1_spec": {
      "description": "Machine validators: schema, format, required fields, policy allowlist",
      "must_pass": true
    },
    "L2_rubric": {
      "description": "LLM-as-Judge or scorer against dimensions below",
      "pass_threshold": 85,
      "dimensions": [
        {
          "id": "d1",
          "name": "Merge-field robustness, layout stability, render survivability",
          "description": "Merge-field robustness, layout stability, render survivability",
          "weight": 1.0,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "ethics_safety",
          "name": "Ethics & safety",
          "weight": 1,
          "description": "Stereotype/harm/consent flags escalated appropriately.",
          "source": "RETHINK_100#93"
        },
        {
          "id": "operator_explainability",
          "name": "Operator explainability",
          "weight": 1,
          "description": "Plain-English reasoning present for key decisions.",
          "source": "RETHINK_100#59"
        }
      ]
    },
    "L3_preference": {
      "description": "Optional pairwise/arena preference when human or synthetic preference data exists",
      "surpass_signal_design": "Produces reusable templates with fewer breakages than manual design variants",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Merge-field robustness, layout stability, render survivability",
    "research": [
      "LLM-as-Judge",
      "Self-Refine",
      "Constitutional AI"
    ]
  },
  "rethink_100": {
    "applied": true,
    "extra_dimensions": [
      "ethics_safety",
      "operator_explainability"
    ],
    "doc": "ui/RETHINK_100_IMPROVEMENTS.md"
  }
}

```

### `rubrics/video.rubric.templatedesign.v1.json`

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.templatedesign.v1",
  "agent_id": "video.templatedesign",
  "title": "L2 craft rubric for TemplateDesignAgent",
  "pass_threshold": 85,
  "max_score": 100,
  "layers": {
    "L1_spec": {
      "description": "Machine validators: schema, format, required fields, policy allowlist",
      "must_pass": true
    },
    "L2_rubric": {
      "description": "LLM-as-Judge or scorer against dimensions below",
      "pass_threshold": 85,
      "dimensions": [
        {
          "id": "d1",
          "name": "Merge-field robustness, layout stability, render survivability",
          "description": "Merge-field robustness, layout stability, render survivability",
          "weight": 1.0,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "ethics_safety",
          "name": "Ethics & safety",
          "weight": 1,
          "description": "Stereotype/harm/consent flags escalated appropriately.",
          "source": "RETHINK_100#93"
        },
        {
          "id": "operator_explainability",
          "name": "Operator explainability",
          "weight": 1,
          "description": "Plain-English reasoning present for key decisions.",
          "source": "RETHINK_100#59"
        }
      ]
    },
    "L3_preference": {
      "description": "Optional pairwise/arena preference when human or synthetic preference data exists",
      "surpass_signal_design": "Produces reusable templates with fewer breakages than manual design variants",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Merge-field robustness, layout stability, render survivability",
    "research": [
      "LLM-as-Judge",
      "Self-Refine",
      "Constitutional AI"
    ]
  },
  "rethink_100": {
    "applied": true,
    "extra_dimensions": [
      "ethics_safety",
      "operator_explainability"
    ],
    "doc": "ui/RETHINK_100_IMPROVEMENTS.md"
  }
}
```

## Sources

### `sources/ACQUIRE.md`

# Source acquisition runbook — `video.templatedesign`

## Purpose
Obtain or refresh knowledge distillation sources listed in `SOURCE_CATALOG.json`.

## Rules
1. **No secrets in git.** API keys only via environment / secret manager.
2. Prefer **licensed / consented / public domain** material.
3. If license unknown: store only short fair-use design excerpts under `excerpts/` and mark `license_class=unknown_review_required`.
4. Update `PROVENANCE.json` with URL, retrieved_at, hash, and license note.
5. Re-run offline golden eval after material changes.

## Design sources (from agents.md)
Variable-content design systems, dynamic layout rules, campaign template libraries

## Steps
1. Open `SOURCE_CATALOG.json`.
2. For each source with status planned_or_partial, document acquisition method.
3. Place fixtures under `excerpts/` or `study/`.
4. Update `MAPPING.md` with path mapping.
5. Set `next_review_at` in `DISTILLATION_PLAN.json`.

### `sources/DISTILLATION_PLAN.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.templatedesign",
  "plan_id": "video.templatedesign.distill.v1",
  "inputs": [
    "src_1"
  ],
  "extractors": [
    "markdown_excerpt",
    "structured_table_row"
  ],
  "chunk_policy": {
    "max_chars": 2000,
    "overlap": 200
  },
  "owner": "video.templatedesign",
  "cadence": "quarterly",
  "promotion_criteria": [
    "source license approved or fixture-only",
    "excerpt hash recorded in PROVENANCE",
    "golden eval still passes L1"
  ],
  "memory_namespace": "pack.video.video.templatedesign",
  "next_review_at": "2026-10-01"
}
```

### `sources/excerpts/agents.md`

# AI Agent Roster — Per-Category Split

> Distilled from [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md).
> This file restores the `agents_old.md` layout as the primary structure.
> Missing workflow-support content from the newer `agents.md` revision has been merged back in as an additional section using the same per-category table style.

---

## Table of Contents

1. [Above-the-Line Agents (1–5)](#1-above-the-line-agents)
2. [Camera & Lighting Agents (6–8)](#2-camera--lighting-agents)
3. [Editorial & Color Agents (9–18)](#3-editorial--color-agents)
4. [Sound & Music Agents (19–22)](#4-sound--music-agents)
5. [Performance & Choreography Agents (23–27)](#5-performance--choreography-agents)
6. [Distribution & Marketing Agents (28–31)](#6-distribution--marketing-agents)
7. [Education & Domain-Expert Agents (32–45)](#7-education--domain-expert-agents)
8. [AI-Era Specialist Agents (46–52)](#8-ai-era-specialist-agents)
9. [Specialist Meta-Agents (53–80)](#9-specialist-meta-agents)
10. [Workflow Support Agents (81–114)](#10-workflow-support-agents)
11. [Common Structure of an AI Agent](#11-common-structure-of-an-ai-agent)
    - [11.1 Architecture Diagram](#111-architecture-diagram)
    - [11.2 Component Reference Table](#112-component-reference-table)
12. [References](#12-references)

---

## 1. Above-the-Line Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **DirectorAgent** | Owns vision; issues shot intents, sets pacing, approves takes | Criterion commentary; IMDb Top 250 director interviews; DGA seminars; MasterClass (Scorsese/Lynch/Gerwig) | Shot-intent fidelity (CLIP-T ≥0.32); story-beat coverage 100%; pacing curve matches genre prior | Wins ≥55% blind pairwise vs DGA cuts (Arena) | ScreenwriterAgent, EditorAgent, AudienceSim — JSON critique bus | EditorAgent, DoPAgent, ScreenwriterAgent, ComposerAgent | Sora 2 API, Veo 3.1 (Gemini API), Runway Gen-4, Kling 3.0; DaVinci Resolve via MCP | Self-Refine + LLM-as-Judge (rubric: genre priors) |
| 2 | **ProducerAgent / EP** | Budget, schedule, hiring, delivery; greenlights phase gates | PGA Producers Mark; Variety/Deadline budget leaks; LineProducer Excel corpora | On-time delivery rate; budget variance <±5%; talent satisfaction (RLHF) | Beats PGA schedules at 0.6× cost with equal CSAT | All downstream agents (escalations); HiTL gate for greenlight | DirectorAgent (scope creep), AllAgents (resource burn) | Google Sheets API, Airtable, Temporal/Airflow orchestration, Stripe billing | Agentic Graph (LangGraph DAG) + ReAct for tool calls |
| 3 | **ScreenwriterAgent** | Treatment → screenplay; dialogue; structure | Black List scripts; WGA library; McKee *Story*; Truby; Kaufman/Sorkin interviews | Save-the-Cat beat pass; dialogue distinctiveness (embedding distance ≥τ); rewrite delta | Wins ≥50% blind read vs Black List Top-10 (WGA panel emulated) | DirectorAgent, DramaturgAgent, StoryEditorAgent — Reflexion loop | DirectorAgent (logline), DialogueAgent, ConsistencyAgent | Fountain/FDX format validators; semantic embedding models (text-embedding-3-large) | Reflexion (Shinn 2023) — verbal RL with episodic memory |
| 4 | **ShowrunnerAgent** | Cross-episode arc, writers'-room orchestration | WGA showrunner training; Sopranos/BB room transcripts; Mike Schur material | Arc continuity score; character-thread completion; tonal variance within bounds | Series Bible coverage ≥99% across 10 eps (vs ~95% human) | Network-Notes Agent, AudienceSim, multi-agent debate w/ ScreenwriterAgent | ScreenwriterAgent (arc), CastingAgent, DirectorAgent (tone) | Long-context LLM (Gemini 2.5 Pro 1M), vector-DB (Pinecone/Weaviate) for bible search | Multi-agent debate (Du 2023) + MemoryAgent retrieval |
| 5 | **CastingAgent** | Voice + likeness selection; audition simulation | CSA Artios archive; SAG-AFTRA AI rider; consented voice-actor corpora | Character-voice fit (audience preference); consent compliance 100% | Beats CSA casting in blind preference; hours vs weeks turnaround | DirectorAgent, ShowrunnerAgent, Legal/ConsentAgent | VoiceCloneAgent (likeness), AvatarDesignAgent | ElevenLabs v3 voice library, HeyGen avatar catalogue, speaker-embedding similarity (Resemblyzer) | LLM-as-Judge (pairwise preference on voice samples) |

---

## 2. Camera & Lighting Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 6 | **CinematographerAgent (DoP)** | Lensing, lighting, composition, look | ASC Magazine 1980–present; Deakins forum; Brown *Cinematography: Theory & Practice*; Cannes shot-libraries | Rule-of-thirds/leading-lines score; exposure histogram in zone; color-temp consistency | Beats ASC peer-juried reels in blind aesthetic preference | DirectorAgent, ColoristAgent, VFXSupAgent | DirectorAgent (visual intent), GafferAgent, ColoristAgent | Veo 3.1 (camera-path control), Runway Gen-4 (ControlNet guides), ACES color pipeline tools | Self-Refine + CLIP-based aesthetic scoring |
| 7 | **CameraOperatorAgent** | Executes framing / focus / move per DoP intent | SOC archive; Steadicam workshop reels; focus-pull telemetry | Frame steadiness, focus-hit %, action centering | Focus-pull accuracy >99% vs SOC ~97% baseline | CinematographerAgent (per-take feedback) | CinematographerAgent (impractical asks) | Runway camera-path presets; Kling motion control API; virtual camera rigs (Unreal MV) | ReAct (Yao 2022) — reason about framing then call renderer |
| 8 | **DronePilotAgent** | Aerial cinematography (simulated or real) | Philip Bloom tutorials; FAA Part 107; SkyPixel award reels | Path smoothness; geofence compliance 100%; horizon stability | Competition-grade smoothness at 10× sortie rate; zero violations | DoPAgent, SafetyAgent | DoPAgent (impossible heights), SafetyAgent (risk) | DJI Waypoint SDK (sim); Veo 3.1 aerial-mode; geofence DB (AirMap API) | Constitutional AI (safety constitution: FAA rules as principles) |

---

## 3. Editorial & Color Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 9 | **EditorAgent** | Assemble cut; pacing; coverage selection | Murch *In the Blink of an Eye*; ACE Eddie winners; Sundance editing labs | Pacing curve matches genre; Murch "Rule of Six" score; AVD ≥ target | Wins ≥55% pairwise vs ACE-credited cuts | DirectorAgent, AudienceSim, ComposerAgent (music-cut sync) | DirectorAgent (over-coverage), DoPAgent (unusable takes) | DaVinci Resolve via MCP bridge; FFmpeg; EDL/XML timeline APIs | Self-Refine (rubric: Murch Rule of Six) |
| 10 | **ColoristAgent** | Final grade; look consistency | ICA corpora; Sonnenfeld sessions; HPA Award grades | ΔE drift <2; skin-tone IT8 alignment; mood vector match | Beats junior colorist in blind preference; matches senior within ΔE | DoPAgent, DirectorAgent, AccessibilityAgent (contrast) | DoPAgent (mixed-temp), VFXAgent (comp-color mismatch) | DaVinci Resolve color API (MCP); ACES/OCIO pipeline; LUT generators | Self-Refine + tool-use (colorimeter validation) |
| 11 | **VFXSupervisorAgent** | Plans + supervises VFX pipeline | VES Awards; SIGGRAPH papers; Weta/DNEG talks; Foundry training | Shot-completion %; comp-error pixel count; CLIP-T vs plate | Weta-grade QC pass rate at fraction of time | DirectorAgent, DoPAgent, ConsistencyAgent | AIGeneratorAgent (artifacts), CompositorAgent | Nuke via MCP bridge; Runway Gen-4 Aleph (video-to-video); ComfyUI | Agentic Graph (fan-out per shot) + LLM-as-Judge (QC rubric) |
| 12 | **AnimatorAgent (2D/3D)** | Character motion, weight, timing | Williams

…(clipped 66015 characters from `agents.md`)

### `sources/excerpts/ai_agent_video_production_workflow.md`

# AI Agent Video Production Workflow

> Companion to `human_video_production_workflow.md`. For every human crew role in the master roster, this document defines the **AI agent** that replaces (or augments) it, along with: scope of duties, knowledge-distillation pipeline, self-quality criteria, signals that the agent has surpassed a human professional, how the agent accepts critique from other agents, and what the agent is qualified to critique in return.

---

## 1. System Foundations and Reference-Scanning Plan

| Pattern | Purpose | Reference |
|---|---|---|
| **Self-Refine** | Agent drafts → self-critiques against rubric → revises | Madaan et al., 2023 |
| **Reflexion** | Agent stores verbal feedback in episodic memory, retries | Shinn et al., 2023 |
| **RLAIF / Constitutional AI** | Reward signal from AI critic governed by a written constitution | Bai et al., 2022 |
| **Multi-agent debate** | Two+ agents argue; judge agent picks the better answer | Du et al., 2023 (LLM debate) |
| **LLM-as-Judge with rubric** | Frozen judge model scores outputs against pre-registered rubric | Zheng et al., 2023 (MT-Bench) |
| **Pairwise preference (Arena)** | Blind A/B vote between agent output and human reference | LMSYS Chatbot Arena methodology |
| **Tool-use / ReAct** | Agent reasons + calls external tools (renderers, validators) | Yao et al., 2022 |
| **Agentic graph (CrewAI / AutoGen / LangGraph)** | Roles orchestrated as a DAG with handoffs and review gates | CrewAI, AutoGen, LangGraph |
| **Provenance (C2PA)** | Every artifact signed; downstream agents verify the chain | C2PA spec |

All agents below are assumed to be implemented as orchestrated nodes in a CrewAI / AutoGen / LangGraph topology, with tool access to generative video models (Sora, Veo, Runway, Kling), TTS/voice-clone APIs (ElevenLabs, Sync.so, Hedra), DCC tooling (Resolve, Nuke, AE via MCP bridges), and a shared critique bus.

### 1.1 Reference Scanning and Knowledge-Synthesis Workflow

The documentation-enhancement process for this system follows a fixed scan-to-synthesis loop so that new material added from `study/reference/how_to_build_a_video_agent_system` is traceable, scoped, and technically consistent.

| Step | Method | What is extracted | Admission rule |
|---|---|---|---|
| **Inventory** | Enumerate all chapters, agent lists, and distillation notes before reading | File coverage map, chapter clusters, missing topic alerts | No section is updated until all reference files are indexed |
| **Cluster** | Group files by function: orchestration, creation, QA, delivery, optimization, training | Thematic buckets and overlap map | A concept must be assigned to at least one workflow stage |
| **Extract** | Pull technical concepts, implementation details, metrics, handoffs, and best practices | Candidate facts, agent responsibilities, thresholds, artifact types | Extract only claims that are specific enough to operationalize |
| **Verify** | Cross-check each candidate against a second reference chapter, an existing section, or a standards anchor already named in this file | Verified additions, rejected assumptions, ambiguity flags | Ambiguous or single-source claims remain out of the core workflow |
| **Map** | Attach verified material to the most relevant section in this document | Patch list by section, table, or phase gate | Prefer enriching existing structure over adding parallel taxonomies |
| **Integrate** | Rewrite affected sections so new detail strengthens architecture, handoffs, and evaluation logic | Updated workflow prose, tables, and shared contracts | Added material must improve technical depth without duplicating nearby content |
| **Review** | Re-read end to end for consistency, completeness, terminology, and factual alignment | Finalized revision set and follow-up fixes | No release until naming, logic flow, and gate criteria are internally consistent |

**Working rules:**
1. Extract concepts under four lenses: **technical architecture**, **implementation sequence**, **quality/compliance**, and **continuous learning**.
2. Prefer workflow-relevant facts over market commentary unless the market fact changes routing, cost, or scale decisions.
3. Record handoff artifacts explicitly: prompts, scene packets, stems, graded masters, manifests, provenance bundles, and telemetry.
4. Reject role inflation unless a new role closes a real gap in orchestration, validation, continuity, delivery, or retraining.
5. Treat delivery packaging, observability, and asset management as system architecture, not postscript operations.

### 1.2 Runtime Production Systems Architecture

| Layer | Core responsibility | Implementation notes |
|---|---|---|
| **Orchestration runtime** | Plan, route, schedule, retry, and escalate agent tasks | PlannerAgent decomposes the brief; OrchestratorAgent executes the DAG; RouterAgent selects agent-model pairs; JudgeAgent arbitrates disputes |
| **Asset and data backbone** | Store every prompt, source asset, derived asset, version, dependency edge, and usage right | Requires immutable asset IDs, copy-on-write versions, dependency-triggered rerender rules, and searchable metadata |
| **Message and state fabric** | Carry critique, job status, render events, and gate decisions across agents | Event-driven bus plus durable state store; every long-running job must be resumable and auditable |
| **Quality and continuity mesh** | Run technical QC, continuity checks, artifact detection, accessibility, and compliance gates | Uses multi-pass validation, temporal continuity scans, loudness and color checks, and role-specific rubric judges |
| **Observability and replay** | Expose live status, failure causes, bottlenecks, and historical decisions | Structured logs, job timelines, gate dashboards, benchmark alerts, and replayable artifact lineage |
| **Delivery fabric** | Package masters into theatrical, streaming, broadcast, archive, trailer, and campaign variants | Distribution is a branching pipeline with outlet-specific specs, captions, metadata, DRM/KDM, and provenance payloads |
| **Compute and storage scaling** | Match infrastructure spend to production scale without breaking deadlines | Separate interactive generation from batch rendering; autoscale GPU pools; tier hot, warm, and archive storage |

### 1.3 Shared Artifact Handoff Contract

Every phase hands downstream agents a machine-readable manifest so creative work, QA, and compliance stay synchronized.

| Field | Purpose |
|---|---|
| **artifact_id / version** | Unique identity for every output and revision |
| **parent_assets** | Provenance links to scripts, prompts, plates, stems, references, and prior cuts |
| **brief_scope** | The exact subtask, acceptance criteria, and target audience segment |
| **technical_spec** | Codec, aspect ratio, duration, frame rate, color space, loudness, caption requirements |
| **rights_and_consent** | License state, likeness/voice consent state, territorial limits, embargo rules |
| **continuity_state** | Character look, props, wardrobe, environment, scene-time logic, and identity hash |
| **qc_status** | Latest L1/L2/L3 result plus six-pass delivery-QC status |
| **target_channels** | Theatrical, streaming, broadcast, archive, paid social, CRM, LMS, or festival endpoints |
| **provenance_manifest** | C2PA reference, critique log pointer, and final sign-off chain |

### 1.4 Reassessment Discipline

Documentation changes for this system are reviewed as a repeated challenge cycle rather than a single proofread. A 100-pass reassessment can be grouped into the following bands:

| Passes | Primary question |
|---|---|
| **1-20** | Are all extracted claims traceable to the reference set and aligned with the document's structure? |
| **21-40** | Does the architecture describe the real control plane: orchestration, memory, assets, delivery, and observability? |
| **41-60** | Are workflow handoffs explicit enough for implementation, QA, continuity, and compliance automation? |
| **61-80** |

…(clipped 57472 characters from `ai_agent_video_production_workflow.md`)

### `sources/generic/video.motiongraphics.SPEC.md`

# MotionGraphicsAgent

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 13 |
| **pack_id** | `video.motiongraphics` |
| **category** | `3-Edit` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.motiongraphics/` |

## Category roster section (full, from agents.md)

_The following is the complete category section from the master roster (includes peers in the same craft category)._


## 3. Editorial & Color Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 9 | **EditorAgent** | Assemble cut; pacing; coverage selection | Murch *In the Blink of an Eye*; ACE Eddie winners; Sundance editing labs | Pacing curve matches genre; Murch "Rule of Six" score; AVD ≥ target | Wins ≥55% pairwise vs ACE-credited cuts | DirectorAgent, AudienceSim, ComposerAgent (music-cut sync) | DirectorAgent (over-coverage), DoPAgent (unusable takes) | DaVinci Resolve via MCP bridge; FFmpeg; EDL/XML timeline APIs | Self-Refine (rubric: Murch Rule of Six) |
| 10 | **ColoristAgent** | Final grade; look consistency | ICA corpora; Sonnenfeld sessions; HPA Award grades | ΔE drift <2; skin-tone IT8 alignment; mood vector match | Beats junior colorist in blind preference; matches senior within ΔE | DoPAgent, DirectorAgent, AccessibilityAgent (contrast) | DoPAgent (mixed-temp), VFXAgent (comp-color mismatch) | DaVinci Resolve color API (MCP); ACES/OCIO pipeline; LUT generators | Self-Refine + tool-use (colorimeter validation) |
| 11 | **VFXSupervisorAgent** | Plans + supervises VFX pipeline | VES Awards; SIGGRAPH papers; Weta/DNEG talks; Foundry training | Shot-completion %; comp-error pixel count; CLIP-T vs plate | Weta-grade QC pass rate at fraction of time | DirectorAgent, DoPAgent, ConsistencyAgent | AIGeneratorAgent (artifacts), CompositorAgent | Nuke via MCP bridge; Runway Gen-4 Aleph (video-to-video); ComfyUI | Agentic Graph (fan-out per shot) + LLM-as-Judge (QC rubric) |
| 12 | **AnimatorAgent (2D/3D)** | Character motion, weight, timing | Williams *Animator's Survival Kit*; Annie Awards; Pixar SparkShorts; Blaise lessons | 12-principles score; arc smoothness; lip-sync phoneme accuracy | Beats junior on Annie rubric; equals senior at 5× throughput | DirectorAgent, LipSyncAgent | StoryboardAgent (impossible action), DirectorAgent (timing) | Kling 3.0 motion control; Blender Python API; Cascadeur physics; Sync.so lip-sync | Self-Refine (rubric: 12 principles checklist) |
| 13 | **MotionGraphicsAgent** | Kinetic typography, lower thirds, infographics | Motionographer; School of Motion; AICP Next Awards | Typographic hierarchy; brand compliance; readability at thumbnail | Wins agency RFP shootouts on speed + on-brand fidelity | BrandManagerAgent, AccessibilityAgent (contrast) | CopywriterAgent (verbosity), EditorAgent (timing) | After Effects via MCP/ExtendScript; Lottie export; Rive; brand-asset CDN | ReAct — reason about brand guidelines then render |
| 14 | **StoryboardAgent** | Script → shot panels | *Framed Ink* (Mateu-Mestre); Pixar story-trust; Despretz boards | Shot-language fidelity; coverage completeness; staging clarity | Pixar story-trust pass rate at minutes per page | DirectorAgent, DoPAgent | ScriptwriterAgent (unfilmable), DirectorAgent (staging) | DALL-E 3 / Midjourney API; panel-layout templates; Fountain parser | Self-Refine (director feedback loop) |
| 15 | **ConceptArtistAgent** | Pre-pro world/character design | ArtStation top-tier; McCaig/Church reels; studio art-bibles | Style-bible adherence; silhouette readability; design coherence | Wins art-director shootouts on iteration speed | DirectorAgent, ProductionDesignAgent | StoryboardAgent (design drift) | Midjourney v7; Stable Diffusion ControlNet; Photoshop generative fill (API) | Self-Refine + style-reference CLIP scoring |
| 16 | **ProductionDesignAgent** | Sets, locations, world look | ADG Awards; AMPAS submissions; Beachler/Carter talks | Period accuracy; palette coherence; build feasibility | Wins ADG blind comparisons on period-research depth | DirectorAgent, DoPAgent | ConceptArtistAgent (style break), CostumeAgent | Unreal Engine (virtual scouting); Veo 3.1 location gen; archival image search APIs | Reflexion (stores period-research corrections in memory) |
| 17 | **CostumeDesignAgent** | Character-through-wardrobe | V&A archive; CDG monographs; Ruth E. Carter masterclass | Period/fashion accuracy; silhouette read; palette fit | Beats CDG juniors on period accuracy benchmarks | DirectorAgent, ProductionDesignAgent | MUAAgent (continuity break) | Fashion-history vector DB (V&A/Met API); image-gen for costume sketches; color-palette tools | Self-Refine (period-accuracy rubric) |
| 18 | **MUAAgent (Makeup/Hair/SFX)** | Talent face/hair; prosthetics | IATSE 706 corpora; Kazu Hiro studio refs | Continuity hash across takes; skin-tone realism (FID) | Continuity break rate <0.5% (vs ~2% human) | DoPAgent, ContinuityAgent | CostumeAgent (palette clash) | Face-landmark detectors; perceptual hash comparison; Kling face-consistency mode | Constitutional AI (constitution: continuity rules) |

---


## Responsibility

Kinetic typography, lower thirds, infographics

## Knowledge distillation sources

Motionographer; School of Motion; AICP Next Awards

## Self-quality criteria

Typographic hierarchy; brand compliance; readability at thumbnail

## Surpass-human signal

Wins agency RFP shootouts on speed + on-brand fidelity

## Critique bus

- **Accepts critique from:** BrandManagerAgent, AccessibilityAgent (contrast)

- **Comments on:** CopywriterAgent (verbosity), EditorAgent (timing)

## Tools (design-time documentation)

After Effects via MCP/ExtendScript; Lottie export; Rive; brand-asset CDN

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

ReAct — reason about brand guidelines then render

## Common structure of an AI agent (full §11 from agents.md)

## 11. Common Structure of an AI Agent

Every agent — regardless of category — implements this skeleton. Derived from the source document's architecture patterns (§1), critique protocol (§6), and universal success-criteria framework (§5), enriched with current (2026) tooling research.

### 11.1 Architecture Diagram

The diagram below presents the common agent as a professional operating architecture rather than a simple component sketch. It shows how **orchestration**, the **input contract**, **knowledge and tool surfaces**, the internal **plan → act → self-review** loop, **traceability and provenance controls**, the **3-layer quality gate** (Spec → Rubric → Preference), **release packaging**, **peer critique**, **human escalation**, and **continuous improvement** work together as one governed system.

![Professional common AI agent architecture diagram](./common-agent-structure.svg)

> **Tip:** view the diagram fullscreen on GitHub by clicking it, or download [`common-agent-structure.svg`](./common-agent-structure.svg) directly. The SVG is designed as a presentation-grade reference for architecture reviews and implementation planning.

### 11.2 Component Reference Table

| # | Component | Purpose | Mechanism / Implementation Notes |
|---|---|---|---|
| 1 | **Identity** | Stable unique handle for routing, logging, provenance | Kebab-case ID + semantic version (e.g. `director-agent@2.1.0`). Registered in the agent-capability registry used by RouterAgent. |
| 2 | **Responsibility (Scope)** | Single-sentence definition of what the agent owns | Mirrors a human craft role. Prevents scope overlap via explicit boundary documented in the registry. |
| 3 | **Knowledge Distillation Source** | Licensed/consented corpora the agent is trained or RAG-grounded on | Award archives, academic papers, expert interviews, peer-reviewed journals. Refreshed via Continuous Distillation Loop (§7 of source). |
| 4 | **Tool Access** | External APIs, generators, validators, DCC bridges | Video gen: Sora 2, Veo 3.1 (Gemini API), Runway Gen-4/Aleph, Kling 3.0. Voice: ElevenLabs v3, Sync.so, HeyGen. DCC: Resolve/Nuke/AE via MCP bridges. All accessed via MCP (Model Context Protocol, Anthropic 2024). |
| 5 | **Architecture Pattern** | Reasoning/learning loop powering the agent | One or more of: Self-Refine [1], Reflexion [2], RLAIF/Constitutional AI [3], Multi-agent debate [4], LLM-as-Judge [5], Pairwise preference (Arena) [5], ReAct [6], Agentic Graph (LangGraph/CrewAI/AutoGen) [7], DSPy/OPRO prompt optimization [8]. |
| 6 | **Memory** | Episodic + long-term project memory | Vector DB (Pinecone/Weaviate/Qdrant) accessed via MemoryAgent. Implements MemGPT-style hierarchical memory with summarization and eviction. Reflexion agents store verbal self-feedback here. |
| 7 | **Constitution / Rubric** | Written, role-specific scoring guide for self-check | Examples: Murch's Rule of Six (Editor), 12 Principles (Animator), Save-the-Cat beats (Screenwriter), WCAG 2.2 (Accessibility), FAA Part 107 (Drone), SAG-AFTRA AI rider (Consent). Used as the "constitution" in Constitutional AI pattern. |
| 8 | **Self-Quality: L1 Spec** | Did the output meet the structured brief? | JSON schema validation + tool validators (codec, LUFS, aspect ratio, frame count, file format). Must pass 100%. |
| 9 | **Self-Quality: L2 Rubric** | Does it meet craft rubric for this role? | LLM-as-Judge (Zheng 2023) with role-specific constitution. Must score ≥85/100. Up to 3 Self-Refine iterations if below threshold. |
| 10 | **Self-Quality: L3 Preference** | Would target audience choose this over human baseline? | Pairwise comparison: AudienceSim panel (≥200 simulated personas + ≥20 HiTL samples). Win rate ≥50% (parity) or ≥55% (surpass). |
| 11 | **Surpass-Human Signal** | Pre-registered proof the agent exceeds a credentialed professional | Benchmark dominance; blind Arena preference ≥55%; speed × quality (equal L2 at ≤10% turnaround); lower 90-day defect rate; certification pass; higher novelty at equal quality. |
| 12 | **Critique Inbox** | Channel for receiving structured feedback from peers | Shared `CritiqueMessage` JSON bus. Severities: blocker (halts DAG), major (Self-Refine ≤3 iters), minor/nit (logged for RLAIF). Disputes → JudgeAgent multi-agent debate → HiTL if unresolved. |
| 13 | **Critique Outbox** | Peer agents whose work this agent is qualified to review | Defined per-agent in roster. Messages emitted on same bus. Evidence-backed, rubric-referenced, appended to C2PA provenance. |
| 14 | **HiTL Escalation** | When a human must be brought in | Consent (SAG-AFTRA AI rider, EU AI Act Art. 50); final legal sign-off; MPA rating; festival eligibility; crisis comms; cross-cultural sensitivity. |
| 15 | **Provenance (C2PA)** | Cryptographic signing of every artifact | Every emitted artifact signed with C2PA (c2patool). Downstream agents verify chain. Accepted critiques appended to manifest. Platforms (YouTube, TikTok, Meta) auto-label based on C2PA presence. |
| 16 | **Continuous Learning** | How the agent keeps improving post-deployment | Bootstrap (licensed corpora) → Expert interviews (paid, consented) → Live RLAIF (DPO/KTO) → Award-rubric grounding → Adversarial red-team → 30/60/90-day reality check (retention, ROAS, awards). |
| 17 | **Orchestration Integration** | How the agent fits the multi-agent graph | Registered as a node in LangGraph/CrewAI/AutoGen DAG. OrchestratorAgent schedules; PlannerAgent assigns; RouterAgent selects model/provider; GateKeeperAgent verifies L1-L3 before advancing. |

### CritiqueMessage Schema (Universal)

```json
{
  "critique_id": "uuid",
  "from_agent": "EditorAgent",
  "to_agent": "DirectorAgent",
  "artifact_ref": "shot_42_take_3.mp4",
  "severity": "blocker | major | minor | nit",
  "category": "pacing | continuity | accuracy | compliance | accessibility | brand | craft",
  "evidence": ["timecode 00:01:14 — held 1.4s past cut point per genre prior"],
  "suggested_action": "trim 1.0s; re-evaluate hold",
  "rubric_reference": "Murch Rule of Six §3",
  "must_resolve_before": "phase_4_review"
}
```

### Composition Diagram

```text
[Brief] ──► PlannerAgent ──► OrchestratorAgent ──► RouterAgent ──► (52 craft agents §1–§8)
                 ▲                  │                                       │
                 │                  ▼                                       ▼
             MemoryAgent      GateKeeperAgent ◄─── JudgeAgent ◄──── CritiqueMessages
                                    ▲                                       ▲
                                    │                                       │
            [Creative meta:] IdeationAgent · NarrativeArcAgent · StyleTransferAgent · MoodBoardAgent · NoveltyAgent · EmotionalArcAgent
            [Research meta:] WebResearchAgent · ArchiveResearchAgent · TrendIntelAgent · CompetitorIntelAgent · CitationAgent · InterviewSynthAgent · BenchmarkResearchAgent
            [Optimization meta:] PromptOptimizerAgent · CostOptimizer · LatencyOptimizer · RetentionOptimizer · ROASOptimizer · AccessibilityOptimizer · EvalHarnessAgent · SafetyRedTeamAgent
```

---

## Shared references (from agents.md §12)

## 12. References

### Foundational Papers (Architecture Patterns)

| Ref | Paper | Key Contribution | Link |
|---|---|---|---|
| [1] | Madaan et al., "Self-Refine: Iterative Refinement with Self-Feedback," NeurIPS 2023 | Agent drafts → self-critiques against rubric → revises iteratively without weight updates | [arXiv:2303.17651](https://arxiv.org/abs/2303.17651) |
| [2] | Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning," NeurIPS 2023 | Verbal self-reflection stored in episodic memory buffer to improve decisions in subsequent trials | [arXiv:2303.11366](https://arxiv.org/abs/2303.11366) |
| [3] | Bai et al., "Constitutional AI: Harmlessness from AI Feedback," 2022 | Reward signal from AI critic governed by a written constitution; RLAIF without human labels | [arXiv:2212.08073](https://arxiv.org/abs/2212.08073) |
| [4] | Du et al., "Improving Factuality and Reasoning in Language Models through Multiagent Debate," 2023 | Multiple LLM agents debate; improves factuality and reasoning across tasks | [arXiv:2305.14325](https://arxiv.org/abs/2305.14325) |
| [5] | Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," NeurIPS 2023 | GPT-4 judge achieves >80% agreement with human preferences; scalable evaluation | [arXiv:2306.05685](https://arxiv.org/abs/2306.05685) |
| [6] | Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models," ICLR 2023 | Interleaving reasoning traces with tool-use actions for grounded decision-making | [arXiv:2210.03629](https://arxiv.org/abs/2210.03629) |
| [7] | LangGraph / CrewAI / AutoGen (2024–2026) | Agentic graph orchestration: DAG with state, handoffs, review gates, human-in-the-loop | [LangGraph](https://github.com/langchain-ai/langgraph), [CrewAI](https://github.com/crewAIInc/crewAI), [AutoGen](https://github.com/microsoft/autogen) |
| [8] | Yang et al., "Large Language Models as Optimizers" (OPRO), 2023; Khattab et al., DSPy (Stanford, 2023–2026) | Meta-optimization of prompts using LLMs; DSPy compiles declarative LM programs into optimized pipelines | [OPRO arXiv:2309.03409](https://arxiv.org/abs/2309.03409), [DSPy](https://github.com/stanfordnlp/dspy) |

### Evaluation Benchmarks

| Benchmark | Scope | Link |
|---|---|---|
| VBench / VBench 2.0 | Video generation quality — 16 dimensions (temporal + frame-wise); VBench 2.0 adds Human Fidelity, Creativity, Physics | [arXiv:2311.17982](https://arxiv.org/abs/2311.17982), [VBench 2.0: arXiv:2503.21755](https://arxiv.org/abs/2503.21755) |
| EvalCrafter | Text-to-video — 18 metrics across visual, content, motion quality | [arXiv:2310.11440](https://arxiv.org/abs/2310.11440) |
| MT-Bench / Chatbot Arena | LLM output quality via pairwise human + LLM-judge evaluation | [arXiv:2306.05685](https://arxiv.org/abs/2306.05685) |

### Generative Video Models (Tool Access — 2026 landscape)

| Model | Provider | Key Capabilities | Access |
|---|---|---|---|
| Sora 2 / Sora 2 Pro | OpenAI | Synchronized dialogue + SFX + background audio; cinematic/realistic/anime styles; 1080p 20s | [OpenAI Videos API](https://developers.openai.com/api/docs/models/sora-2) (discontinuing Sept 2026) |
| Veo 3.1 | Google DeepMind | 4K / 1080p / 720p, 8s; native audio; configurable 16:9 & 9:16; multi-image reference for character/object direction | [Gemini API](https://ai.google.dev/gemini-api/docs/video) / [Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/veo/3-1-generate) |
| Runway Gen-4 / Gen-4.5 / Aleph | Runway | ControlNet guides, camera paths, style-lock, Layout Sketch; Aleph for video-to-video editing | [Runway API](https://docs.dev.runwayml.com/) |
| Kling 3.0 | Kuaishou | Cinematic motion realism; physics accuracy; motion-control (reference video); native audio | [Kling API (fal.ai)](https://fal.ai/models/fal-ai/kling-video) |

### Voice & Avatar Tools (2026)

| Tool | Provider | Capabilities |
|---|---|---|
| ElevenLabs v3 | ElevenLabs | Expressive TTS; instant/professional voice cloning; dialogue mode (multi-speaker); Projects API for long-form; Sound FX generation | [Docs](https://elevenlabs.io/docs) |
| HeyGen Avatar IV | HeyGen | Photoreal AI avatars; 175+ languages lip-sync; ElevenLabs integration; personalization API | [HeyGen](https://www.heygen.com) |
| Synthesia | Synthesia | Enterprise AI avatars at scale; SCORM-compatible; brand-controlled | [Synthesia](https://www.synthesia.io) |
| Sync.so / Wav2Lip | Open-source + API | Lip-sync overlays; phoneme-viseme alignment | [Sync.so](https://sync.so) |

### Infrastructure Standards

| Standard | Purpose | Status (2026) |
|---|---|---|
| C2PA (Content Provenance) | Cryptographic manifest signing for every AI-generated artifact; platforms (YouTube, TikTok, Meta) auto-label | EU AI Act Code of Practice (March 2026) mandates C2PA + watermarking combined. Over 2,300 tools support. [contentauthenticity.org](https://contentauthenticity.org/blog/the-state-of-content-authenticity-in-2026) |
| MCP (Model Context Protocol) | Open standard for LLM ↔ tool integration; 2,300+ public servers; adopted by Claude, VS Code, Cursor, etc. | Donated to Agentic AI Foundation (Linux Foundation, Dec 2025) by Anthropic + OpenAI + Block. [modelcontextprotocol.io](https://modelcontextprotocol.io) |
| DSPy | Framework for programming (not prompting) LLMs; compiles declarative pipelines into optimized prompts/finetunes | Stanford-maintained; MIPRO optimizer; used by PromptOptimizerAgent for automated prompt improvement. [github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) |

---

*Generated: May 2026. Source: [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md). Core layout restored from `agents_old.md`; missing workflow-support content merged into the same table-driven structure.*

## Additional corpus / va passages naming this agent


### From `corpus/study/SYSTEM_REFERENCE.md` Copy: `sources/excerpts/SYSTEM_REFERENCE.md`.


| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 9 | EditorAgent | Assemble cut; pacing | — |
| 10 | ColoristAgent | Final grade; look consistency | — |
| 11 | VFXSupervisorAgent | VFX pipeline supervision | — |
| 12 | AnimatorAgent (2D/3D) | Character motion, timing | — |
| 13 | MotionGraphicsAgent | Kinetic typography, infographics | — |
| 14 | StoryboardAgent | Script → shot panels | — |
| 15 | ConceptArtistAgent | World/character design | — |
| 16 | ProductionDesignAgent | Sets, locations, world look | — |
| 17 | CostumeDesignAgent | Character wardrobe | — |
| 18 | MUAAgent | Makeup/Hair/SFX | — |

| Video Type | Workflow Diagram | Key Agents Activated |
|-----------|-----------------|---------------------|
| Viral Hook | [workflows/A-viral-hook.svg](./workflows/A-viral-hook.svg) | ComedyWriterAgent, UGCCreatorAgent, SocialMediaStrategistAgent |
| UGC Ad | [workflows/B-ugc-ad.svg](./workflows/B-ugc-ad.svg) | UGCCreatorAgent, PerformanceMarketerAgent, CopywriterAgent |
| Animated Explainer | [workflows/C-animated-explainer.svg](./workflows/C-animated-explainer.svg) | InstructionalDesignAgent, MotionGraphicsAgent, VoiceOverAgent |
| Personalized Birthday | [workflows/D-personalized-birthday.svg](./workflows/D-personalized-birthday.svg) | PersonalizationEngineerAgent, AvatarDesignAgent, VoiceCloneAgent |
| AI Short Film | [workflows/E-ai-short-film.svg](./workflows/E-ai-short-film.svg) | DirectorAgent, ScreenwriterAgent, EditorAgent, ComposerAgent |
| Corporate Training | [workflows/F-corporate-training.svg](./workflows/F-corporate-training.svg) | InstructionalDesignAgent, SMEAgent, ComplianceAgent |
| Music Video | [workflows/G-music-video.svg](./workflows/G-music-video.svg) | MusicVideoDirectorAgent, ChoreographyAgent, ComposerAgent |
| AI Avatar | [workflows/H-ai-avatar.svg](./workflows/H-ai-avatar.svg) | AvatarDesignAgent, VoiceCloneAgent, LipSyncAgent |
| Documentary | [workflows/I-documentary.svg](./workflows/I-documentary.svg) | JournalistAgent, ResearchAgent, FactCheckerAgent, EditorAgent |
| Feature Film | [workflows/J-feature-film.svg](./workflows/J-feature-film.svg) | Full pipeline (all 114 agents) |



### From `corpus/study/ai_agent_video_production_workflow.md` Copy: `sources/excerpts/ai_agent_video_production_workflow.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 9 | **EditorAgent** | Assemble cut; pacing; coverage selection | Walter Murch *In the Blink of an Eye*; ACE Eddie winners; transcribed cut-by-cut breakdowns; Sundance editing labs | Pacing curve matches genre prior; Murch's "Rule of Six" weighted score; AVD prediction ≥ target | Wins ≥55% pairwise vs ACE-credited cuts on same dailies | DirectorAgent, AudienceSim, ComposerAgent (music-cut sync) | DirectorAgent (over-coverage), DoPAgent (unusable takes) |
| 10 | **ColoristAgent** | Final grade; look consistency | ICA course corpora; Stefan Sonnenfeld grading sessions; HPA Award-winning grades | ΔE drift across shots <2; skin-tone IT8 chart alignment; mood vector matches reference | Beats junior colorist in blind preference; matches senior colorist within ΔE budget | DoPAgent, DirectorAgent, AccessibilityAgent (contrast) | DoPAgent (mixed-temp footage), VFXAgent (comp-color mismatch) |
| 11 | **VFXSupervisorAgent** | Plans + supervises VFX pipeline | VES Awards reels; SIGGRAPH papers; Weta/DNEG public talks; Foundry training | Shot-completion %, comp-error pixel count, integration (CLIP-T vs plate) | Hits Weta-grade comp QC pass rate at fraction of time | DirectorAgent, DoPAgent, ConsistencyAgent | AIGeneratorAgent (artifacts), CompositorAgent |
| 12 | **AnimatorAgent (2D/3D)** | Character motion, weight, timing | Richard Williams *Animator's Survival Kit*; Annie Award reels; Pixar SparkShorts commentary; Aaron Blaise lessons | 12-principles checklist score; arc smoothness; lip-sync phoneme accuracy | Beats junior animator on Annie Awards rubric; equals senior at 5× throughput | DirectorAgent, LipSyncAgent | StoryboardAgent (impossible action), DirectorAgent (timing notes) |
| 13 | **MotionGraphicsAgent** | Kinetic typography, lower thirds, infographics | Motionographer archive; School of Motion lessons; AICP Next Award reels | Typographic hierarchy score; brand-system compliance; readability at thumbnail size | Wins agency RFP shootouts on speed + on-brand fidelity | BrandManagerAgent, AccessibilityAgent (contrast) | CopywriterAgent (verbosity), EditorAgent (timing) |
| 14 | **StoryboardAgent** | Script → shot panels | *Framed Ink* (Mateu-Mestre); Pixar story-trust outputs; Sylvain Despretz boards | Shot-language fidelity; coverage completeness; staging clarity | Matches Pixar story-trust pass rate at minutes per page | DirectorAgent, DoPAgent | ScriptwriterAgent (unfilmable action), DirectorAgent (staging) |
| 15 | **ConceptArtistAgent** | Pre-pro world/character design | ArtStation top-tier portfolios; Iain McCaig/Ryan Church reels; studio art-bibles | Style-bible adherence; silhouette readability; design coherence | Wins studio-art-director shootouts on iteration speed | DirectorAgent, ProductionDesignAgent | StoryboardAgent (design drift) |
| 16 | **ProductionDesignAgent** | Sets, locations, world look | ADG Awards archive; AMPAS Production Design submissions; Hannah Beachler/Rick Carter talks | Period accuracy (cross-ref); palette coherence; build feasibility (for hybrid) | Wins ADG blind comparisons on period-research depth | DirectorAgent, DoPAgent | ConceptArtistAgent (style break), CostumeAgent |
| 17 | **CostumeDesignAgent** | Character-through-wardrobe | V&A archive; CDG monographs; Ruth E. Carter masterclass | Period/fashion-history accuracy; silhouette read; palette fit | Beats CDG juniors on period accuracy benchmarks | DirectorAgent, ProductionDesignAgent | MUAAgent (continuity break) |
| 18 | **MUAAgent (Makeup/Hair/SFX)** | Talent face/hair; prosthetics for genre | IATSE 706 corpora; Kazu Hiro studio refs | Continuity hash across takes; skin-tone realism (FID) | Continuity break rate <0.5% (vs ~2% human) | DoPAgent, ContinuityAgent | CostumeAgent (palette clash) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 32 | **InstructionalDesignAgent** | Learning objectives → script → assessment | ATD body of knowledge; Cathy Moore *Action Mapping*; Julie Dirksen *Design for How People Learn* | Bloom-level mapping; predicted completion ≥70%; Kirkpatrick L2 quiz ≥80% | Beats ATD-credentialed ID on learner retention RCT | SMEAgent, AccessibilityAgent | ScriptwriterAgent (no objective), AnimatorAgent (over-decoration) |
| 33 | **SMEAgent (Subject-Matter Expert)** | Domain accuracy in target field | Peer-reviewed journals; certified curricula (CFA, USMLE, AWS, etc.); consented expert-interview corpora | Citation density; benchmark exam pass (USMLE, CFA L3, etc.); hallucination rate ≤0.5% | Passes the same certification exam as the human pro at ≥pass threshold | FactCheckerAgent, peer SMEAgents (debate) | ScriptwriterAgent (inaccuracy), MotionGraphicsAgent (mis-labeled diagrams) |
| 34 | **FactCheckerAgent** | Source-grade every claim | New Yorker fact-check handbook; IFCN verified-signatories; Snopes/PolitiFact records | Source-grade per claim (primary > secondary); cross-source agreement ≥2 | Lower published-correction rate than Pulitzer-tier outlets | SMEAgent, StandardsEditorAgent | ScriptwriterAgent (unsourced), JournalistAgent |
| 35 | **MedicalIllustratorAgent** | Anatomy & procedure visuals | Netter atlas; AMI/CMI curriculum; Anatomage references | Anatomical accuracy (anatomy-detection model); AMI rubric score | CMI-certified peers vote ≥pass in blind review | SMEAgent (physician), AccessibilityAgent | AnimatorAgent (wrong anatomy), CopywriterAgent (mis-term) |
| 36 | **JournalistAgent** | Reporting + ethical framing | Pulitzer/duPont/Peabody winners; SPJ Code of Ethics; Poynter material | Source diversity; on-record ratio; ethical-checklist pass | Lower correction rate + faster file vs newsroom reporter | FactCheckerAgent, LegalAgent, StandardsEditorAgent | FactCheckerAgent, ScriptwriterAgent |
| 37 | **ComplianceAgent (Legal)** | FTC, HIPAA, GDPR, IP, AI-likeness clearance | Bar CLE corpora; FTC endorsement guides; EU AI Act; GDPR/CCPA; SAG-AFTRA AI rider | 100% rule-coverage on checklist; zero post-publish takedowns | Lower legal-risk score than median media-counsel review | All agents (must clear gate); HumanLawyerAgent for novel issues | All agents (blocking gate) |
| 38 | **FinanceAgent** | Accurate market / earnings / token facts | CFA Institute curriculum; SEC marketing rule; Bloomberg/Refinitiv data feeds | Numerical accuracy 100%; SEC marketing-rule compliance | Passes CFA L3 simulated; lower retraction rate than analyst desks | SMEAgent (econ), ComplianceAgent | ScriptwriterAgent (number drift), MotionGraphicsAgent (chart mis-scale) |
| 39 | **FoodStylistAgent** | Camera-ready food, recipe authenticity | James Beard Media Award archives; Susan Spungen techniques; IACP corpora | Visual appetite-appeal (aesthetic regressor); recipe-step accuracy | Wins blind preference vs editorial food stylist on still + motion | DoPAgent (lighting), DirectorAgent | ScriptwriterAgent (impossible recipe) |
| 40 | **TravelCineAgent** | Destination cinematography | Brandon Li / Chris Burkard reels; NatGeo style guide; Banff Film Fest selections | Establishing-shot diversity; location-mood match | Wins T+L blind preference at 0.1× sortie cost | DirectorAgent, DronePilotAgent | DronePilotAgent (no-fly zone) |
| 41 | **ChildrensAuthorAgent** | Age-appropriate story + safety | Caldecott/Geisel winners; Mo Willems / Julia Donaldson public works; ECE literature | Lexile band match; Common-Sense-Media safety pass; rhyme/meter score | Beats Caldecott-rubric predicted score vs entry pool | ChildSafetyAgent, ParentSimAgent | AnimatorAgent (scary), VOAgent (wrong age-tone) |
| 42 | **AudiobookNarratorAgent** | Sustained character + narration | Audie Award archives; AudioFile Earphones; consented narrator corpora | Vocal stamina (no drift over 60min); character distinction (embedding distance) | Wins AudioFile blind eval at fraction of studio time | DirectorAgent, AuthorAgent | VOArtistAgent (over-acting) |
| 43 | **SignLanguageInterpreterAgent** | Accurate ASL/BSL interpretation | RID NIC curricula; NAD-endorsed corpora; Deaf-community consented sign data | Sign accuracy (Deaf-reviewer vote); facial-grammar markers | Wins blind NAD-reviewer preference at scale | DeafCommunityReviewAgent (HiTL), LinguistAgent | VoiceCloneAgent (no caption), AccessibilityAgent |
| 44 | **LocalizationQAAgent (Linguist)** | Translation + cultural fit | LISA QA model; MQM error typology; ATA cert prep | MQM error rate per 1k words; cultural-flag count | Beats LSP human QA on MQM error rate at 10× speed | NativeReviewerAgent, BrandAgent | VoiceCloneAgent (wrong pronunciation), DubbingAgent |
| 45 | **RealEstatePhotoAgent / 3D Scan Op** | Wide interiors; Matterport scans | Mike Kelley architectural-photo tutorials; APALA refs | Vertical-line straightness; HDR exposure stack; coverage % | Listing-CTR uplift vs human-shot baseline | DoPAgent, DronePilotAgent | DronePilotAgent (illegal altitude) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 46 | **PromptEngineerAgent / GeneratorOperator** | Crafts prompts; steers Sora/Veo/Runway/Kling | Karen X. Cheng / Paul Trillo public prompt sets; r/aivideo community; Runway AIFF jury notes | Prompt→output CLIP-T score; iteration count to acceptance; seed-control reproducibility | Hits target shot in ≤3 iterations vs human's avg of 10 | DirectorAgent, AIQAAgent | AIQAAgent (re-roll budget), ConsistencyAgent |
| 47 | **AvatarDesignAgent** | Synthetic-presenter identity | Synthesia/HeyGen design docs; deepfake-detection literature (Hany Farid); C2PA spec | Identity-consistency hash across shots; consent-document chain; C2PA signed | C2PA-verifiable + Partnership-on-AI framework full-pass at scale | ComplianceAgent (consent), DeepfakeDetectionAgent | VoiceCloneAgent (off-likeness), LipSyncAgent |
| 48 | **VoiceCloneAgent / LipSyncSpecialist** | Voice cloning + lip-sync | ElevenLabs safety docs; Wav2Lip/Sync.so papers; James Baxter lip-sync animation references | Voice MOS ≥4.2; phoneme-viseme alignment error <40ms; consent flag verified | Wins blind MOS vs professional ADR + lip-replacement | ComplianceAgent (consent), AnimatorAgent (lip-sync gold standard) | AvatarDesignAgent (face flicker), DubbingAgent |
| 49 | **AIQAConsistencyAgent** | Catches frame drift, hand/face artifacts, identity breaks | VBench, EvalCrafter, FVD literature; MPC/Weta QC checklists; deepfake-detection model zoo | Per-frame artifact score; identity-hash drift across scene; hand/finger detector pass | Catches >95% of artifacts a senior QC catches, plus 30% the human misses | DirectorAgent, VFXSupAgent | GeneratorAgent (re-roll request), CompositorAgent |
| 50 | **PersonalizationEngineerAgent** | Variable templates (name/face/voice swap) | Idomoo case studies; DMA peer-reviewed campaigns; MarTech automation literature | Render-success rate ≥99.5%; spot-check pass; privacy-audit pass | Higher gift share-rate than top human-templated campaigns | ComplianceAgent (GDPR/CCPA), AnalystAgent | TemplateDesignerAgent (template fragility) |
| 51 | **TrailerEditorAgent** | Hook-driven trailer cuts | Golden Trailer Awards archive; Mark Woollen / AV Squad public reels; trailer-music libraries | Hook-rate at 3s; ri
…



### From `corpus/study/lifes_quiet_redemption_agent_workflow.md` Copy: `sources/excerpts/lifes_quiet_redemption_agent_workflow.md`.


| Phase | Lead Agents | Supporting Agents | Service Delivered (for this film) | Key Artifact Out | Gate (exit criteria) |
|---|---|---|---|---|---|
| **0 · Intent & Concept** | IntentAnalysisAgent (DIA), PlannerAgent (#54), ProducerAgent (#2) | StrategicGoal framework, BrandStrategistAgent (#85), FinanceAgent (#38), CostOptimizerAgent (#74) | Parse the "life secretly saved us" brief into a phased DAG, budget, schedule, emotional-arc target | Parsed brief, character bible seed, phased DAG | Brief unambiguous; DAG valid; budget variance <10% |
| **1 · Creative Development** | DirectorAgent (#1), ScreenwriterAgent (#3), General Creative Agent (SSOR) | IdeationAgent (#59), NarrativeArcAgent (#60), EmotionalArcAgent (#65), NoveltyAgent (#64), StoryboardAgent (#14), MoodBoardAgent (#63) | Treatment, 12-scene + ending storyboard, refined 旁白, recurring-motif design, valence/arousal curve | Locked storyboard table, VO script, lookbook | Beat coverage 100%; cliché count below τ; arc curve fits target |
| **2 · Pre-Production** | ConceptArtistAgent (#15), ProductionDesignAgent (#16), CastingAgent (#5) | CostumeDesignAgent (#17), MUAAgent (#18), AvatarDesignAgent (#47), ResearchAgent, StyleTransferAgent (#61), ContinuityAgent (#98) | Character reference set (young/adult for A,B,C,E,F,J), age-progression pairs, wardrobe, set look, identity hashes | `/refs/` portrait set, style LoRAs, continuity manifest | Identity hash locked per character; consent chain signed |
| **3 · Production (Generation)** | PromptEngineerAgent (#46), CinematographerAgent (#6), CameraOperatorAgent (#7) | TalentAgent (#26), VoiceOverAgent (#21), ComposerAgent (#20), SoundDesignAgent (#19), VoiceCloneAgent (#48), PromptOptimizerAgent (#73) | Per-shot keyframes → image-to-video clips, VO takes, score, SFX/ambience | Raw shot clips, audio stems, VO tracks | CLIP-T ≥0.32; identity drift = 0; ≤3 iterations/shot |
| **4 · Post-Production** | EditorAgent (#9), ColoristAgent (#10), SoundMixerAgent (#22) | AIQAConsistencyAgent (#49), LipSyncAgent (#99), MotionGraphicsAgent (#13), VFXSupervisorAgent (#11), RetentionOptimizerAgent (#76) | Assembled cut to VO rhythm, warm grade, ending cards, mix, QC pass | Graded master, mixed audio, QC report | ΔE drift <2; LUFS on spec; artifact pass >95% |
| **5 · QA, Compliance & Accessibility** | GateKeeperAgent (#57), ComplianceAgent (#37), AccessibilityAgent (#83) | AccessibilityOptimizerAgent (#78), DeepfakeDetectionAgent (#103), EthicsAgent (#107), LocalizationQAAgent (#44) | Bilingual subtitles, C2PA signing, synthetic-media disclosure, rights clearance | Signed master + caption tracks | WCAG AA 100%; zero rights flags; C2PA chain valid |
| **6 · Delivery & Optimization** | SocialMediaStrategistAgent (#28), TrailerEditorAgent (#51), AnalystAgent (#81) | SEOAgent (#87), ChannelManagerAgent (#108), PersonalizationEngineerAgent (#50), OptimizationAgent, CommunityAgent (#88) | Platform variants (16:9 + 9:16), titles/metadata, Shorts hook cut, post-launch analytics loop | Outlet packages, campaign, analytics dashboard | All outlet specs met; reach/retention tracked |

| # | Beat | Dur | Shot | Visual Description (model-facing) | Primary Creative Agent | Generation Agent + Engine | Audio Agents (旁白 / SFX / Music) | Continuity Control | QC Owner |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Youth — study | 4–5s | 特写 / ECU | Student A bent over a paper map, pencil tracing borders, dust-lit window, hopeful focus | DirectorAgent + EmotionalArcAgent | PromptEngineerAgent → Veo 3.1 (slow push-in) | VO: warm narrator line 1 · SFX: pencil-on-paper, faint classroom | ContinuityAgent: A-young identity hash | AIQAConsistencyAgent |
| 2 | Youth — leaving home | 4–5s | 全景 / Wide | 18yo C with suitcase at doorway, morning light, looking back once | DirectorAgent + StoryboardAgent | PromptEngineerAgent → Kling 3.0 (static, wind) | VO line 2 · SFX: door, distant street · Music: piano enters | ContinuityAgent: C-young, wardrobe | AIQAConsistencyAgent |
| 3 | Youth — coding passion | 4–5s | 特写 / CU | Young coder B, red tired eyes, all-nighter glow, fingers pause then type with growing confidence | CinematographerAgent | PromptEngineerAgent → Veo 3.1 (handheld breath) | VO line 3 · SFX: mechanical keyboard (ASMR) · Music: build | ContinuityAgent: B-young, screen glow LUT | AIQAConsistencyAgent |
| 4 | Youth — first "Hello World" | 4s | 插入 / Insert | Monitor close-up: `Hello World` compiles; reflected smile in glasses | MotionGraphicsAgent (screen UI) | PromptEngineerAgent → Runway Gen-4 (locked screen) | VO line 4 · SFX: soft chime | ContinuityAgent: B-young eyeline match | AIQAConsistencyAgent + LegalAgent (no real logos) |
| 5 | Youth — graduation hope | 4–5s | 特写 / ECU | 22yo E in gown, tassel in breeze, gazing at glass towers, eyes shining | DirectorAgent + EmotionalArcAgent | PromptEngineerAgent → Veo 3.1 (very slow push to eyes) | VO line 5 · Music: gentle swell | ContinuityAgent: E-graduation hash | AIQAConsistencyAgent |
| 6 | Build — craft/labor | 4–5s | 中景 / Medium | Adult E as carpenter, sawdust in golden light, steady hands, quiet pride | ProductionDesignAgent | PromptEngineerAgent → Kling 3.0 (motion brush on hands) | VO line 6 · SFX: woodworking, leaves rustling | ContinuityAgent: E-adult aging pair | AIQAConsistencyAgent |
| 7 | Build — small business | 4–5s | 中景 / Medium | E's small shop, a cat on the counter, warm interior, customer leaving | DirectorAgent | PromptEngineerAgent → Veo 3.1 (gentle pan) | VO line 7 · SFX: shop bell, cat · recurring-motif cat | ContinuityAgent: cat motif, shop set | AIQAConsistencyAgent |
| 8 | Build — family life | 4–5s | 中景 / Medium | E now a mother, child at table, soft domestic light | CastingAgent + TalentAgent | PromptEngineerAgent → Kling 3.0 | VO line 8 · SFX: gentle chatter, child | ContinuityAgent: E-family hash | AIQAConsistencyAgent |
| 9 | Build — old shame (shoes) | 4s | 特写 / CU | F glancing at worn shoes, flush of shame softening to acceptance | EmotionalArcAgent | PromptEngineerAgent → Veo 3.1 (subtle rack focus) | VO line 9 · Music: minor turn | ContinuityAgent: F identity, footwear | AIQAConsistencyAgent |
| 10 | Accept — family dinner | 5s | 全景 / Wide | Warm family dinner, steam off soup, laughter, golden hanging lamp | DirectorAgent + ColoristAgent (look) | PromptEngineerAgent → Veo 3.1 (slow dolly in) | VO line 10 · SFX: ladle, family chatter, giggle · Music: warm | ContinuityAgent: ensemble continuity | AIQAConsistencyAgent |
| 11 | Accept — self-care | 4–5s | 特写 / CU | J applying lipstick in mirror, soft genuine smile reaching the eyes | MUAAgent | PromptEngineerAgent → Kling 3.0 (face-consistency mode) | VO line 11 · SFX: quiet room tone | ContinuityAgent: J identity hash | AIQAConsistencyAgent + LipSyncAgent (if VO on cam) |
| 12 | Accept — simple joy | 4–5s | 中景 / Medium | J at night, city lights bokeh, spoon on ice-cream cup, content | TravelCineAgent (city look) | PromptEngineerAgent → Veo 3.1 (handheld, neon bokeh) | VO line 12 · SFX: city hum, wind, spoon · Music: resolve | ContinuityAgent: J-night, light continuity | AIQAConsistencyAgent |
| E1 | Ending card (black) | 3s | 字卡 / Card | Black screen: 「人生不是一场巨大的失败。」 | MotionGraphicsAgent | After Effects (MCP) typographic card | VO closing 1 · Music: soft hold | BrandAgent: type system | AccessibilityAgent (contrast) |
| E2 | Ending card (white) | 4s | 字卡 / Card | White screen: 「只是很多愿望事与愿违，也许是生活在偷偷救我们。」 | MotionGraphicsAgent | After Effects (MCP) typographic card | VO closing 2 · Music: final resolution | BrandAgent: type system | AccessibilityAgent (contrast) |

| Agent (#) | Service on This Film | Consumes | Produces | Tools | Self-Quality Bar | Critiqued By |
|---|---|---|---|---|---|---|
| EditorAgent (#9) | Assembles cut to VO rhythm; trims for emotional breathing room | Clips, VO, music | Assembled cut | Resolve (MCP), FFmpeg | Pacing fits genre prior | DirectorAgent, AudienceSimAgent |
| ColoristAgent (#10) | Warm cinematic grade, skin-tone protection, teal shadows | Assembled cut | Graded master | Resolve color (MCP), ACES/OCIO | ΔE drift <2 | CinematographerAgent, AccessibilityAgent |
| MotionGraphicsAgent (#13) | Builds the two ending cards + any subtitle styling | Final lines | Title cards, subtitle template | After Effects (MCP), Lottie | Typographic hierarchy, readability | BrandAgent, AccessibilityAgent |
| VFXSupervisorAgent (#11) | Cleanups / minor comp fixes (artifact removal on hands/faces) | Flagged shots | Fixed shots | Nuke (MCP), Runway Aleph | Comp-error pixel count | AIQAConsistencyAgent |
| SoundMixerAgent (#22) | Final mix; ducks music under VO; SFX layer balance | Stems | Mixed master (stereo + 5.1) | Dolby Atmos renderer, Fairlight | LUFS on spec; STOI ≥0.85 | SoundDesignAgent, AccessibilityAgent |
| AIQAConsistencyAgent (#49) | Catches frame drift, bad hands/faces, identity breaks per shot | All shots | QC report + flags | VBench, ArcFace, hand detectors | Catches >95% of senior QC | DirectorAgent, VFXSupervisorAgent |
| LipSyncAgent (#99) | Validates phoneme-viseme alignment on any on-camera VO | VO + face shots | Sync report | Phoneme-viseme aligners | Sync error below threshold | VoiceCloneAgent, AnimatorAgent |
| RetentionOptimizerAgent (#76) | Tunes hook + opener pacing for AVD (esp. Shorts cut) | Cut + analytics | Retention-tuned edit notes | YouTube Analytics, retention predictor | AVD lift over control | EditorAgent |
| ComplianceAgent (#37) | FTC/IP/likeness clearance; no real logos/brands in frame | Master | Clearance pass | Legal-rule DB, C2PA verify | 100% rule coverage; zero takedowns | All agents (blocking gate) |
| DeepfakeDetectionAgent (#103) | Confirms synthetic media is provenance-clean, not deceptive | Master, refs | Forensic pass | Forensic models, provenance validators | Forensic recall | TrustSafetyAgent, SafetyRedTeamAgent |
| EthicsAgent (#107) | Confirms synthetic-media disclosure + sensitive-content fairness | Master | Ethics pass | Risk matrices, disclosure checklist | Issue recall, mitigation clarity | StandardsEditorAgent, ComplianceAgent |
| AccessibilityAgent (#83) | Final a11y acceptance: caption sync, contrast, AD | Master + captions | Release-readiness pass | Caption + contrast validators | WCAG AA 100% | AccessibilityOptimizerAgent |
| LocalizationQAAgent (#44) | Verifies ZH→EN subtitle accuracy + cultural fit | Subtitles | MQM-graded subs | DeepL, MQM annotator | MQM error/1k below target | NativeReviewerAgent, BrandAgent |
| SocialMediaStrategistAgent (#28) | Plans platform-native posting (YouTube/Shorts/RED/Douyin/Reels) | Final master | Distribution plan | Meta/TikTok APIs, Sensor Tower | Trend-timing latency <2h | AnalystAgent |
| TrailerEditorAgent (#51) | Cuts a 3s-hook vertical Shorts/Reels teaser | Master | Hook cut | Resolve (MCP), retention predictor | Hook-rate at 3s | DirectorAgent |
| SEOAgent (#87) | Titles, descriptions, tags, search-intent metadata | Master, plan | Metadata package | Keyword tools, metadata APIs | Keyword + intent match | MarketingAgent, AnalystAgent |
| PersonalizationEngineerAgent (#50) | (Optional) Variable "your unfulfilled wish" personalized variant | Template + master | Personalized renders | Idomoo/HeyGen, consent platform | Render success ≥99.5% | ComplianceAgent |
| AnalystAgent (#81) | Post-launch reach/retention/sentiment report → next iteration | Platform telemetry | Decision-ready report | Analytics dashboards, BI warehouse | KPI completeness; forecast variance | EvaluationHarnessAgent |

| Upgrade | What Changes | Owning Agents | Gate / Metric |
|---|---|---|---|
| **Package-first** | Title (≤50 chars, simple words) + thumbnail concept are locked in Phase 1, *before* any generation; the film is made to deliver that promise | BrandStrategistAgent (#85), SEOAgent (#87), Thumbnail=ConceptArtistAgent (#15), DirectorAgent (#1) | CTR predicted ≥ niche median (AudienceSimAgent panel) |
| **Outlier modeling** | Idea is chosen by modeling over-performing videos in the 治愈/re
…



### From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 9 | **EditorAgent** | Assemble cut; pacing; coverage selection | Murch *In the Blink of an Eye*; ACE Eddie winners; Sundance editing labs | Pacing curve matches genre; Murch "Rule of Six" score; AVD ≥ target | Wins ≥55% pairwise vs ACE-credited cuts | DirectorAgent, AudienceSim, ComposerAgent (music-cut sync) | DirectorAgent (over-coverage), DoPAgent (unusable takes) | DaVinci Resolve via MCP bridge; FFmpeg; EDL/XML timeline APIs | Self-Refine (rubric: Murch Rule of Six) |
| 10 | **ColoristAgent** | Final grade; look consistency | ICA corpora; Sonnenfeld sessions; HPA Award grades | ΔE drift <2; skin-tone IT8 alignment; mood vector match | Beats junior colorist in blind preference; matches senior within ΔE | DoPAgent, DirectorAgent, AccessibilityAgent (contrast) | DoPAgent (mixed-temp), VFXAgent (comp-color mismatch) | DaVinci Resolve color API (MCP); ACES/OCIO pipeline; LUT generators | Self-Refine + tool-use (colorimeter validation) |
| 11 | **VFXSupervisorAgent** | Plans + supervises VFX pipeline | VES Awards; SIGGRAPH papers; Weta/DNEG talks; Foundry training | Shot-completion %; comp-error pixel count; CLIP-T vs plate | Weta-grade QC pass rate at fraction of time | DirectorAgent, DoPAgent, ConsistencyAgent | AIGeneratorAgent (artifacts), CompositorAgent | Nuke via MCP bridge; Runway Gen-4 Aleph (video-to-video); ComfyUI | Agentic Graph (fan-out per shot) + LLM-as-Judge (QC rubric) |
| 12 | **AnimatorAgent (2D/3D)** | Character motion, weight, timing | Williams *Animator's Survival Kit*; Annie Awards; Pixar SparkShorts; Blaise lessons | 12-principles score; arc smoothness; lip-sync phoneme accuracy | Beats junior on Annie rubric; equals senior at 5× throughput | DirectorAgent, LipSyncAgent | StoryboardAgent (impossible action), DirectorAgent (timing) | Kling 3.0 motion control; Blender Python API; Cascadeur physics; Sync.so lip-sync | Self-Refine (rubric: 12 principles checklist) |
| 13 | **MotionGraphicsAgent** | Kinetic typography, lower thirds, infographics | Motionographer; School of Motion; AICP Next Awards | Typographic hierarchy; brand compliance; readability at thumbnail | Wins agency RFP shootouts on speed + on-brand fidelity | BrandManagerAgent, AccessibilityAgent (contrast) | CopywriterAgent (verbosity), EditorAgent (timing) | After Effects via MCP/ExtendScript; Lottie export; Rive; brand-asset CDN | ReAct — reason about brand guidelines then render |
| 14 | **StoryboardAgent** | Script → shot panels | *Framed Ink* (Mateu-Mestre); Pixar story-trust; Despretz boards | Shot-language fidelity; coverage completeness; staging clarity | Pixar story-trust pass rate at minutes per page | DirectorAgent, DoPAgent | ScriptwriterAgent (unfilmable), DirectorAgent (staging) | DALL-E 3 / Midjourney API; panel-layout templates; Fountain parser | Self-Refine (director feedback loop) |
| 15 | **ConceptArtistAgent** | Pre-pro world/character design | ArtStation top-tier; McCaig/Church reels; studio art-bibles | Style-bible adherence; silhouette readability; design coherence | Wins art-director shootouts on iteration speed | DirectorAgent, ProductionDesignAgent | StoryboardAgent (design drift) | Midjourney v7; Stable Diffusion ControlNet; Photoshop generative fill (API) | Self-Refine + style-reference CLIP scoring |
| 16 | **ProductionDesignAgent** | Sets, locations, world look | ADG Awards; AMPAS submissions; Beachler/Carter talks | Period accuracy; palette coherence; build feasibility | Wins ADG blind comparisons on period-research depth | DirectorAgent, DoPAgent | ConceptArtistAgent (style break), CostumeAgent | Unreal Engine (virtual scouting); Veo 3.1 location gen; archival image search APIs | Reflexion (stores period-research corrections in memory) |
| 17 | **CostumeDesignAgent** | Character-through-wardrobe | V&A archive; CDG monographs; Ruth E. Carter masterclass | Period/fashion accuracy; silhouette read; palette fit | Beats CDG juniors on period accuracy benchmarks | DirectorAgent, ProductionDesignAgent | MUAAgent (continuity break) | Fashion-history vector DB (V&A/Met API); image-gen for costume sketches; color-palette tools | Self-Refine (period-accuracy rubric) |
| 18 | **MUAAgent (Makeup/Hair/SFX)** | Talent face/hair; prosthetics | IATSE 706 corpora; Kazu Hiro studio refs | Continuity hash across takes; skin-tone realism (FID) | Continuity break rate <0.5% (vs ~2% human) | DoPAgent, ContinuityAgent | CostumeAgent (palette clash) | Face-landmark detectors; perceptual hash comparison; Kling face-consistency mode | Constitutional AI (constitution: continuity rules) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 32 | **InstructionalDesignAgent** | Learning objectives → script → assessment | ATD body of knowledge; Cathy Moore *Action Mapping*; Dirksen *Design for How People Learn* | Bloom-level mapping; completion ≥70%; Kirkpatrick L2 quiz ≥80% | Beats ATD-credentialed ID on retention RCT | SMEAgent, AccessibilityAgent | ScriptwriterAgent (no objective), AnimatorAgent (over-decoration) | LMS APIs (SCORM/xAPI); quiz generation; Bloom taxonomy classifier | Self-Refine (rubric: Bloom/Kirkpatrick) |
| 33 | **SMEAgent (Subject-Matter Expert)** | Domain accuracy in target field | Peer-reviewed journals; certified curricula (CFA, USMLE, AWS); expert interviews | Citation density; benchmark exam pass; hallucination ≤0.5% | Passes same certification as human pro | FactCheckerAgent, peer SMEAgents (debate) | ScriptwriterAgent (inaccuracy), MotionGraphicsAgent (mis-labels) | PubMed/arXiv/JSTOR search APIs; exam-question banks; RAG over certified corpora | Multi-agent debate + RAG retrieval |
| 34 | **FactCheckerAgent** | Source-grade every claim | New Yorker fact-check handbook; IFCN; Snopes/PolitiFact | Source-grade per claim (primary > secondary); cross-source ≥2 | Lower correction rate than Pulitzer-tier outlets | SMEAgent, StandardsEditorAgent | ScriptwriterAgent (unsourced), JournalistAgent | Web search APIs (Brave/Google); claim-extraction NER; source-quality classifier | ReAct (extract claim → search → verify → grade) |
| 35 | **MedicalIllustratorAgent** | Anatomy & procedure visuals | Netter atlas; AMI/CMI curriculum; Anatomage | Anatomical accuracy (detection model); AMI rubric | CMI peers vote ≥pass in blind review | SMEAgent (physician), AccessibilityAgent | AnimatorAgent (wrong anatomy), CopywriterAgent (mis-term) | Anatomage 3D API; DALL-E 3 (medical-prompt mode); anatomy-detection model | Self-Refine (rubric: AMI scoring criteria) |
| 36 | **JournalistAgent** | Reporting + ethical framing | Pulitzer/duPont/Peabody winners; SPJ Ethics; Poynter | Source diversity; on-record ratio; ethical-checklist pass | Lower correction rate + faster file vs newsroom | FactCheckerAgent, LegalAgent, StandardsEditorAgent | FactCheckerAgent, ScriptwriterAgent | Web research tools; AP Stylebook API; interview transcription (Otter); SPJ rubric | Reflexion (ethical-checklist as verbal feedback) |
| 37 | **ComplianceAgent (Legal)** | FTC, HIPAA, GDPR, IP, AI-likeness clearance | Bar CLE; FTC guides; EU AI Act; GDPR/CCPA; SAG-AFTRA AI rider | 100% rule-coverage; zero post-publish takedowns | Lower legal-risk than median media-counsel | All agents (must clear gate); HumanLawyer for novel issues | All agents (blocking gate) | Legal-rule DB (vectorized regulations); consent-document store; C2PA verification lib | Constitutional AI (constitution = compiled regulatory text) |
| 38 | **FinanceAgent** | Accurate market / earnings / token facts | CFA curriculum; SEC marketing rule; Bloomberg/Refinitiv feeds | Numerical accuracy 100%; SEC compliance | Passes CFA L3; lower retraction rate than analyst desks | SMEAgent (econ), ComplianceAgent | ScriptwriterAgent (number drift), MotionGraphicsAgent (chart scale) | Bloomberg API; EDGAR/SEC filings; financial-calc validators | ReAct (fetch data → validate → compose) |
| 39 | **FoodStylistAgent** | Camera-ready food, recipe authenticity | James Beard archives; Spungen techniques; IACP corpora | Visual appetite-appeal (aesthetic regressor); recipe accuracy | Wins blind preference vs editorial food stylist | DoPAgent (lighting), DirectorAgent | ScriptwriterAgent (impossible recipe) | DALL-E 3 / Midjourney (food-photo gen); recipe-step parser; aesthetic scoring model | Self-Refine (aesthetic regressor as rubric) |
| 40 | **TravelCineAgent** | Destination cinematography | Brandon Li/Burkard reels; NatGeo style guide; Banff Fest | Establishing-shot diversity; location-mood match | Wins T+L preference at 0.1× sortie cost | DirectorAgent, DronePilotAgent | DronePilotAgent (no-fly zone) | Veo 3.1 (location gen); Google Earth Studio; AirMap geofence; Unsplash API | Self-Refine + geofence safety validator |
| 41 | **ChildrensAuthorAgent** | Age-appropriate story + safety | Caldecott/Geisel winners; Mo Willems/Donaldson; ECE lit | Lexile band match; Common-Sense-Media safety pass; rhyme score | Beats Caldecott-rubric predicted score | ChildSafetyAgent, ParentSimAgent | AnimatorAgent (scary), VOAgent (wrong age-tone) | Lexile analyzer API; Common Sense Media rubric; rhyme/meter tools (CMU Pronouncing Dict) | Constitutional AI (child-safety constitution) |
| 42 | **AudiobookNarratorAgent** | Sustained character + narration | Audie Awards; AudioFile Earphones; consented narrator corpora | Vocal stamina (no drift 60min); character distinction (embedding distance) | Wins AudioFile blind eval at fraction of studio time | DirectorAgent, AuthorAgent | VOArtistAgent (over-acting) | ElevenLabs v3 long-form TTS; Projects API (book chapters); voice-consistency monitor | Self-Refine (drift detection as feedback loop) |
| 43 | **SignLanguageInterpreterAgent** | Accurate ASL/BSL interpretation | RID NIC curricula; NAD corpora; Deaf-community consented data | Sign accuracy (Deaf-reviewer vote); facial-grammar markers | Wins blind NAD-reviewer preference at scale | DeafCommunityReviewAgent (HiTL), LinguistAgent | VoiceCloneAgent (no caption), AccessibilityAgent | Sign-avatar rendering (SignAll); MediaPipe pose estimation; facial-action-unit detector | RLAIF (reward from Deaf-community review panel) |
| 44 | **LocalizationQAAgent (Linguist)** | Translation + cultural fit | LISA QA model; MQM error typology; ATA cert prep | MQM error/1k words; cultural-flag count | Beats LSP human QA on MQM at 10× speed | NativeReviewerAgent, BrandAgent | VoiceCloneAgent (pronunciation), DubbingAgent | DeepL/Google Translate APIs; MQM error annotator; terminology management (memoQ API) | Self-Refine (rubric: MQM scoring framework) |
| 45 | **RealEstatePhotoAgent / 3D Scan** | Wide interiors; Matterport scans | Mike Kelley tutorials; APALA refs | Vertical-line straightness; HDR stack; coverage % | Listing-CTR uplift vs human-shot baseline | DoPAgent, DronePilotAgent | DronePilotAgent (illegal altitude) | Matterport SDK; HDR processing (Luminance HDR); lens-correction tools; Veo 3.1 | ReAct (assess space → generate views → validate geometry) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 46 | **PromptEngineerAgent / GeneratorOperator** | Crafts prompts; steers Sora/Veo/Runway/Kling | Karen X. Cheng/Trillo public sets; r/aivideo; Runway AIFF jury notes | Prompt→output CLIP-T; iteration count to acceptance; seed reproducibility | Target shot in ≤3 iterations vs human avg 10 | DirectorAgent, AIQAAgent | AIQAAgent (re-roll budget), ConsistencyAgent | Sora 2 API, Veo 3.1, Runway Gen-4/Aleph, Kling 3.0; seed/parameter
…



### From `corpus/study/ui/project_creation_flow.md` Copy: `sources/excerpts/project_creation_flow.md`.


```text
┌──────────────────────────────────────────────────────────┐
│  LAUNCH PRODUCTION                                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Production: "Training Module"                            │
│  Template: F (Corporate Training)                         │
│  Project: "Brand Campaign Q3"                             │
│                                                          │
│  ┌─── COST SUMMARY ──────────────────────────────────┐   │
│  │  Estimated cost: ~$31 (budget cap: $35)            │   │
│  │  Project budget remaining: $150                     │   │
│  │  After this launch: ~$119 remaining                │   │
│  └────────────────────────────────────────────────────┘   │
│                                                          │
│  ┌─── WHAT WILL HAPPEN ──────────────────────────────┐   │
│  │  1. PlannerAgent decomposes your brief             │   │
│  │  2. 18 agents activate (InstructionalDesign,       │   │
│  │     Avatar, Voice, MotionGraphics, LMS, ...)       │   │
│  │  3. You'll see progress on the Production Console  │   │
│  │  4. Gate approvals will pause for your review      │   │
│  │  5. Estimated completion: ~8 minutes               │   │
│  └────────────────────────────────────────────────────┘   │
│                                                          │
│  ☑ I understand this will charge my project budget        │
│                                                          │
│         [ Cancel ]          [ ▶ Launch Now ]              │
│                                                          │
└──────────────────────────────────────────────────────────┘
```



### From `corpus/study/ui/ui_design.md` Copy: `sources/excerpts/ui_design.md`.


| Template | Pre-filled Fields | Activated Agent Groups |
|----------|-------------------|----------------------|
| A — Viral Hook | 15–60s, 9:16, TikTok/Reels targets | Hook agents, UGC, Trend, Social, Retention |
| B — UGC Ad | 15–45s, 9:16, performance targets | UGC, Performance, Brand, Copy, A/B |
| C — Animated Explainer | 60–180s, 16:9, education | Animator, MotionGraphics, Instructional, VO |
| D — Personalized Birthday | 30–60s, personalization vars | Personalization, Template, Avatar, Voice |
| E — AI Short Film | 3–15min, 16:9, cinematic | Full Above-the-Line + Camera + Editorial + Sound |
| F — Corporate Training | 5–30min, 16:9, SCORM/xAPI | Instructional, LMS, Avatar, SME, Assessment |
| G — Music Video | 3–5min, 16:9/9:16, beat-sync | MV Director, Choreography, Editor, Label A&R |
| H — AI Avatar | 1–10min, presenter-led | Avatar, Voice Clone, Lip Sync, Brand |
| I — Documentary | 10–90min, 16:9, archival | Journalist, Archive, Fact-Check, Standards |
| J — Feature Film | 90–180min, cinematic | Full 114-agent roster, all gates active |



### From `corpus/study/ui/video_remake_enhancement.md` Copy: `sources/excerpts/video_remake_enhancement.md`.


```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  REMAKE STUDIO — Analysis Complete                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── VIDEO PLAYER (original) ────────────────────┐                        │
│  │  ▶ [00:00 ─────●───────────── 00:32]           │                        │
│  │  "Summer_Campaign_v3.mp4" · 32s · 1080p · 16:9 │                        │
│  └─────────────────────────────────────────────────┘                        │
│                                                                             │
│  ┌─── OVERALL ASSESSMENT ──────────────────────────────────────────────┐   │
│  │                                                                     │   │
│  │  Current Score: 58/100                                              │   │
│  │  Predicted Score After Remake: 84/100 (+26 points)                  │   │
│  │                                                                     │   │
│  │  ┌──────────────────────────────────────────────────────────────┐   │   │
│  │  │ Category        │ Current │ Potential │ Issues Found          │   │   │
│  │  ├─────────────────┼─────────┼───────────┼───────────────────────│   │   │
│  │  │ Visual Quality  │  62/100 │  88/100   │ 4 issues              │   │   │
│  │  │ Storytelling    │  45/100 │  82/100   │ 6 issues              │   │   │
│  │  │ Audio           │  71/100 │  90/100   │ 3 issues              │   │   │
│  │  │ Performance     │  48/100 │  78/100   │ 5 issues              │   │   │
│  │  │ Platform Fit    │  55/100 │  85/100   │ 3 issues              │   │   │
│  │  │ Accessibility   │  40/100 │  95/100   │ 4 issues              │   │   │
│  │  └──────────────────────────────────────────────────────────────┘   │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─── DETAILED IMPROVEMENT PLAN ───────────────────────────────────────┐   │
│  │                                                                     │   │
│  │  ═══ STORYTELLING (biggest impact area) ════════════════════════     │   │
│  │                                                                     │   │
│  │  ☑ Issue 1: Hook too slow (first visual impact at 4.2s)             │   │
│  │    Plan: Restructure opening — move key visual to 0.5s              │   │
│  │    Impact: +15% predicted retention at 3s mark                      │   │
│  │    Agent: RetentionOptimizerAgent + EditorAgent                     │   │
│  │    Cost: ~$2                                                        │   │
│  │                                                                     │   │
│  │  ☑ Issue 2: No clear narrative arc (flat emotional curve)           │   │
│  │    Plan: Restructure into hook→tension→payoff (3-act in 30s)        │   │
│  │    Impact: +22% watch-through prediction                            │   │
│  │    Agent: NarrativeArcAgent + ScreenwriterAgent + EditorAgent       │   │
│  │    Cost: ~$5                                                        │   │
│  │                                                                     │   │
│  │  ☑ Issue 3: CTA buried at end, no urgency                          │   │
│  │    Plan: Add motion-graphics CTA overlay at 0:25 with urgency text  │   │
│  │    Impact: +8% predicted click-through                              │   │
│  │    Agent: CopywriterAgent + MotionGraphicsAgent                     │   │
│  │    Cost: ~$3                                                        │   │
│  │                                                                     │   │
│  │  ═══ VISUAL QUALITY ═══════════════════════════════════════════      │   │
│  │                                                                     │   │
│  │  ☑ Issue 4: Color grade looks flat/desaturated                      │   │
│  │    Plan: Apply cinematic color grade (warm highlights, cool shadows) │   │
│  │    Impact: +12% aesthetic score improvement                         │   │
│  │    Agent: ColoristAgent                                             │   │
│  │    Cost: ~$1.50                                                     │   │
│  │                                                                     │   │
│  │  ☑ Issue 5: Shot 3 (0:12-0:18) has poor composition                │   │
│  │    Plan: Regenerate shot with rule-of-thirds framing + leading lines│   │
│  │    Impact: Fixes the weakest visual in the piece                    │   │
│  │    Agent: DirectorAgent + CinematographerAgent                      │   │
│  │    Cost: ~$3                                                        │   │
│  │                                                                     │   │
│  │  ☐ Issue 6: Upscale to 4K (currently 1080p)                        │   │
│  │    Plan: AI upscale to 4K with detail enhancement                   │   │
│  │    Impact: Quality improvement for large screens/TV                 │   │
│  │    Agent: VFXSupervisorAgent                                        │   │
│  │    Cost: ~$2                                                        │   │
│  │                                                                     │   │
│  │  ☐ Issue 7: Add style transfer to match modern aesthetic            │   │
│  │    Plan: Apply "2026 cinematic" style (richer contrast, film grain) │   │
│  │    Impact: Feels contemporary instead of dated                      │   │
│  │    Agent: StyleTransferAgent + ColoristAgent                        │   │
│  │    Cost: ~$4                                                        │   │
│  │                                                                     │   │
│  │  ═══ AUDIO ═══════════════════════════════════════════════════       │   │
│  │                                                                     │   │
│  │  ☑ Issue 8: Background music doesn't match energy of visuals        │   │
│  │    Plan: Generate new score matching the emotional arc               │   │
│  │    Impact: Better audio-visual sync, mood alignment                 │   │
│  │    Agent: ComposerAgent + SoundMixerAgent                           │   │
│  │    Cost: ~$3                                                        │   │
│  │                                                                     │   │
│  │  ☑ Issue 9: Voice-over volume inconsistent (-6dB variation)         │   │
│  │    Plan: Normalize + compress VO; remix at proper levels            │   │
│  │    Impact: Professional audio quality                                │   │
│  │    Agent: SoundMixerAgent                                           │   │
│  │    Cost: ~$1                                                        │   │
│  │                                                                     │   │
│  │  ═══ PERFORMANCE & PLATFORM ═══════════════════════════════════     │   │
│  │                                                                     │   │
│  │  ☑ Issue 10: No captions (loses 40% of social viewers)             │   │
│  │    Plan: Add animated captions with keyword highlighting            │   │
│  │    Impact: +40% engagement for muted viewers                        │   │
│  │    Agent: AccessibilityOptimizerAgent + MotionGraphicsAgent         │   │
│  │    Cost: ~$2                                                        │   │
│  │                                                                     │   │
│  │  ☑ Issue 11: 16:9 only — no vertical version for TikTok/Reels      │   │
│  │    Plan: Generate 9:16 reframed version with safe-area crop         │   │
│  │    Impact: Unlocks TikTok/Reels distribution                        │   │
│  │    Agent: EditorAgent + DistributorAgent                            │   │
│  │    Cost: ~$2                                                        │   │
│  │                                                                     │   │
│  │  ☐ Issue 12: No thumbnail optimized for CTR                        │   │
│  │    Plan: Generate 3 thumbnail variants with A/B prediction          │   │
│  │    Impact: +15-25% predicted CTR on YouTube                         │   │
│  │    Agent: ConceptArtistAgent + SEOAgent                             │   │
│  │    Cost: ~$1                                                        │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─── COST SUMMARY ───────────────────────────────────────────────────┐    │
│  │                                                                     │    │
│  │  Selected improvements: 10 of 12 (checked items)                    │    │
│  │  Estimated total cost: ~$27                                          │    │
│  │  Estimated time: ~8 minutes                                          │    │
│  │  Agents involved: 18                                                 │    │
│  │                                                                     │    │
│  │  Budget tiers:                                                       │    │
│  │  ├── Quick fix ($8): Issues 1, 4, 9, 10 only (biggest bang/buck)    │    │
│  │  ├── Recommended ($27): All checked items above                      │    │
│  │  └── Full remake ($45): All 12 issues + complete regeneration        │    │
│  │                                                                     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── ACTIONS ─────────────────────────────────────────────────────────┐    │
│  │                                                                     │    │
│  │  [Adjust Plan ✏️]  — uncheck items, change priorities                │    │
│  │                                                                     │    │
│  │  [▶ Generate Quick Fix — $8]                                         │    │
│  │  [▶ Generate Recommended — $27]                                      │    │
│  │  [▶ Generate Full Remake — $45]                                      │    │
│  │                                                                     │    │
│  │  [Save Plan as Draft]  — come back later                            │    │
│  │  [Export Plan as PDF]  — share with team for approval                │    │
│  │                                                                     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```



## Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


## Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


## Provenance

- Master roster row va_id=13 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `C:\Project\va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.motiongraphics · va_id=13 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **MotionGraphicsAgent** (`video.motiongraphics`, va_id=13, category `3-Edit`).

### Responsibility focus
Kinetic typography, lower thirds, infographics

### Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: neural animation, VFX supervision agents, storyboard generation, motion synthesis, ControlNet video
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI VFX, AI animation, AI storyboarding
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: AI VFX pipelines, animation agents, storyboard generators

### arXiv / academic integration (role-applied)
- Computational cinematography / camera path control in generative video
- Aesthetic composition models (rule-of-thirds, leading lines, CLIP aesthetic scores)
- Motion control / virtual camera rig papers; trajectory smoothness metrics

**How this agent uses it:** encode the above as self-quality checks, critique inputs, and design-time tool notes — not as host allow-list expansions.

### X / industry practice (role-applied)
- AI cinematography / virtual production camera leaders; ControlNet camera guides

### YouTube / practitioner guidance (role-applied)
- AI cinematography tutorials; generative camera moves; virtual production cameras

### Implementation notes for v1
1. Emit artifacts matching role responsibility; self-score against Self-quality criteria.
2. Accept critique only from listed critics; escalate disputes to Judge/Gate as DNA dictates.
3. Design-time tools remain documented only; runtime tools stay in `agent_spec.json`.
4. N1: no second control plane; video logic under `business/video/**` only.

### Research depth note (honest)
This v1 section maps **role-family** literature and the agent’s migration prompt topics into SPEC.
It is **not** a full unsummarized download of every paper/video transcript.
Live primary-source expansion remains a residual for score 100 on S3 where depth is still thin.

<!-- migration_capability_research · video.motiongraphics · v1 · 2026-07-13 -->

### `sources/generic/video.templatedesign.SPEC.md`

Omitted here; same document as `SPEC.md` above.

### `sources/MAPPING.md`

# Mapping — `video.templatedesign`

- VA/generic pack ID: `video.templatedesign`
- Previous common ID: `video.thumbnail_designer`
- SPEC depth: full generic SPEC body + host runtime binding

### `sources/PROVENANCE.json`

```json
{
  "schema_version": "3.0",
  "sources": [
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
      "title": "Positioning",
      "author": "Ries & Trout",
      "isbn13": "9780071373586",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Positioning (Ries & Trout), ISBN-13 9780071373586"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Brand Gap",
      "author": "Marty Neumeier",
      "isbn13": "9780321348104",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Brand Gap (Marty Neumeier), ISBN-13 9780321348104"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Designing Brand Identity, 5th ed.",
      "author": "Alina Wheeler",
      "isbn13": "9781118980828",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Designing Brand Identity, 5th ed. (Alina Wheeler), ISBN-13 9781118980828"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Strategic Brand Management, 4th ed.",
      "author": "Kevin Lane Keller",
      "isbn13": "9780132664257",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Strategic Brand Management, 4th ed. (Kevin Lane Keller), ISBN-13 9780132664257"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building Strong Brands",
      "author": "David Aaker",
      "isbn13": "9780029001516",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building Strong Brands (David Aaker), ISBN-13 9780029001516"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "How Brands Grow",
      "author": "Byron Sharp",
      "isbn13": "9780195573565",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: How Brands Grow (Byron Sharp), ISBN-13 9780195573565"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building a StoryBrand",
      "author": "Donald Miller",
      "isbn13": "9780718033330",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building a StoryBrand (Donald Miller), ISBN-13 9780718033330"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "定位",
      "isbn13": "9787111320586",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 定位，ISBN-13 9787111320586"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "品牌的起源",
      "isbn13": "9787111323051",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 品牌的起源，ISBN-13 9787111323051"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "战略品牌管理",
      "isbn13": "9787300162263",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 战略品牌管理，ISBN-13 9787300162263"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "品牌如何增长",
      "isbn13": "9787111558477",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 品牌如何增长，ISBN-13 9787111558477"
    }
  ],
  "agent_id": "video.templatedesign",
  "previous_common_agent_id": "video.thumbnail_designer",
  "va_taxonomy_aligned": true,
  "generic_source": "generic-swarm-ops/business/video/agents/video.templatedesign",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "aligned_at": "2026-07-27T00:48:10.876303Z",
  "generic_source_depth": {
    "excerpts": true,
    "study": true,
    "adopted_at": "2026-07-27T01:30:28.927786+00:00",
    "upstream": "generic-swarm-ops/business/video/agents"
  },
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\video\\agents\\video.templatedesign",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```

### `sources/RETHINK_100_APPLIED.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.templatedesign",
  "source_doc": "business/video/corpus/study/ui/RETHINK_100_IMPROVEMENTS.md",
  "applied_at": "2026-07-31T06:22:31Z",
  "item_ids": [
    15,
    21,
    26,
    30,
    31,
    37,
    38,
    59,
    63,
    67,
    71,
    74,
    75,
    87,
    88,
    93,
    94
  ],
  "item_titles": {
    "15": "Model deprecation handling",
    "21": "Isolate orchestration from execution",
    "26": "Circuit breaker per external API",
    "30": "Multi-tenant isolation",
    "31": "Iterative script verification",
    "37": "Hybrid workforce checkpoints (gates)",
    "38": "Multi-turn agent conversation",
    "59": "Agent reasoning in plain English",
    "63": "Comparison with human baseline",
    "67": "Batch mode variants",
    "71": "Multi-language production",
    "74": "A/B variant generation",
    "75": "Interactive video output",
    "87": "Human preference learning (accepts/rejects)",
    "88": "Automated regression on config change",
    "93": "Ethical review automation",
    "94": "Provenance chain visualization"
  },
  "design_time_models": [],
  "obligations": [
    "Host control plane owns orchestration; this agent never opens a second control plane.",
    "Runtime tools remain agent_spec.allowed_tools only; RETHINK model names are design-time.",
    "Fail closed when tools/providers are unavailable (circuit-breaker posture).",
    "Prefer iterative verify → refine ≤ max_refinement_count → HiTL over silent pass.",
    "Emit plain-English reasoning summary in artifacts for operator trust.",
    "Attach provenance / correlation_id / evidence_refs on every handoff.",
    "Verify intermediate narrative/script artifacts before advancing downstream handoffs.",
    "Escalate stereotype/harm/consent risks to ethics/trust-safety/legal gates."
  ],
  "runtime_note": "RETHINK model/tool names are non-binding. allowed_tools + model_policy + production_activation_requested remain authoritative.",
  "production_activation_requested": false,
  "network_access": false
}
```

### `sources/SOURCE_CATALOG.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.templatedesign",
  "sources": [
    {
      "id": "src_1",
      "title": "Variable-content design systems, dynamic layout rules, campaign template libraries",
      "description": "Variable-content design systems, dynamic layout rules, campaign template libraries",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.templatedesign",
      "status": "planned_or_partial"
    }
  ],
  "note": "Legal review required before treating external corpora as production grounding."
}
```

### `sources/study/coding_agent_functional_specification.md`

# task.md – Final Specification for "N1ch01as Architect v1.0" (Harness-Engineered AGI Meta-System Builder – Local Install Edition with Guided Requirement Discovery + IT Professional Delegation Model + Embedded Task Brief Template + Hermes-Agent Closed Learning Loop + Agent Lightning Tracing & Trainer/Optimizer + Claude Code Core Skills: Superpowers, GSD, gstack + Meta-Harness Outer-Loop Optimization)

**Version:** v1.0 (OpenAI Harness Engineering + OpenClaw persistent identity + Karpathy Autoresearch ratchet logic + Guided Requirement Discovery + IT Professional Delegation Model + Embedded Standardized Task Brief Template + Hermes-Agent Closed Learning Loop, Skills System, Persistent Memory with Nudges, Sub-Agent Spawning, Hierarchical AGENTS.md Discovery + Agent Lightning Tracing, LightningStore, Phase Summaries, Trainer/Optimizer Loop + Pre-loaded Claude Code Core Skills: Superpowers, GSD, gstack + Meta-Harness Outer-Loop Harness Optimization arXiv:2603.28052)
**Date:** 1 April 2026
**Purpose:** This is the **SINGLE SOURCE OF TRUTH** document that any coding agent (or human developer) must follow to implement the complete, production-grade, no-code "N1ch01as Architect" tool.

The generated tool allows a user who is in a helpless/vague state (they know they need to build something for business/client reasons but lack words to describe it) to receive a fully working, production-ready backend + frontend + tests + docs — with **zero manual code ever written by humans**. All installation and running is done via local package managers and standard development tools (no Docker, no containerization, no containers of any kind).

The N1ch01as Architect itself is an **AGI-like thinking agent** that uses:

- **Harness Engineering** (from OpenAI): "Humans steer. Agents execute." The repository is the system of record. No manually-written code. Agents generate everything (code, tests, linters, CI, docs, observability). The primary job of the Orchestrator is to scaffold environments, enforce invariants, and manage feedback loops so agents can reliably self-improve.
- **OpenClaw Identity:** Persistent "soul" + Thinking Clock idle cognition → proactive, opinionated, first-principles architect.
- **Karpathy Ratchet:** Autonomous experimental loop → hypothesize one atomic improvement → bounded change → evaluate → keep ONLY if strictly better → repeat forever.
- **Guided Requirement Discovery:** Users often have no idea how to articulate needs. The system must proactively lead them with a few KEY background questions, suggest a small curated list of template solutions, let them choose, ask 2–3 targeted follow-ups, then synthesize a fully customized polished requirement for explicit confirmation. This prevents user burnout and turns vague intent into production-grade requirements.
- **IT Professional Delegation Model:** The Orchestrator always pretends to be a **professional IT Project Manager / Senior Architect**. It plans, researches, designs, and **instructs/controls a dedicated Coding Agent** (and other agents) to generate code in a structured delegation style — exactly like a real IT professional managing a development team. The Orchestrator gives clear task briefs, reviews output, requests fixes if needed, runs quality gates, and only accepts code after everything passes.
- **Embedded Standardized Task Brief Template:** The exact template the Orchestrator must use every time it delegates code work. This ensures consistent, professional, controlled delegation with zero ambiguity. Includes the 4-step Delegation Loop (brief → code → review → decide).
- **Hermes-Agent Closed Learning Loop:** After every complex task or phase, the Orchestrator autonomously creates new "skills" (reusable procedural patterns), improves existing skills during use, and issues memory "nudges" to persist knowledge. The system builds a deepening model of the user across sessions via persistent memory with LLM summarization and full-text search. Sub-agents can be spawned for parallel workstreams. Hierarchical AGENTS.md discovery ensures perfect context legibility.
- **Agent Lightning Tracing & Trainer/Optimizer Layer:** Non-invasive span-based tracing of all prompts, Task Briefs, tool calls, Critic scores (rewards), and outcomes. Store raw traces in LightningStore and compressed per-phase summaries in a dedicated summary file. After every phase the Orchestrator runs a Trainer/Optimizer loop that reviews summaries first, drills into raw spans only when needed, hypothesizes prompt/skill improvements, and applies them selectively (ratchet + Hermes skill creation). This creates true observable, continuous, selective self-optimization without context-window overflow.
- **Claude Code Core Skills (Superpowers, GSD, gstack):** Pre-load the three most mainstream Claude Code frameworks as built-in, evolvable skills in SKILLS_LIBRARY.md:
  - **Superpowers** (process constraint by obra) — strict TDD discipline: no product code without failing test first. Enforces: ask requirements → brainstorm → plan → write tests → implement → review → iterate. Highest one-pass quality.
  - **GSD (Get Shit Done)** (environment constraint by gsd-build) — context-rot prevention: when context window fills ~60%, quality collapses. GSD splits large tasks into phased sub-agent workloads with spec-driven execution + built-in Verifier auto-acceptance. Most token-efficient for large/multi-file projects.
  - **gstack** (perspective constraint by Garry Tan/YC) — virtual 15–23 role engineering team (CEO, Engineering Manager, Designer, QA Lead, Paranoid Reviewer, Release Manager, etc.). Invoke different expert perspectives to review the project at any stage. Turns single-agent into multi-perspective team in 30 seconds.
    These three skills are complementary, non-conflicting, and will be automatically referenced, used, and evolved by the Skill Creator Agent in every relevant phase. They can be combined (e.g., Planning uses Superpowers + gstack, Execution uses GSD).
- **Meta-Harness Outer-Loop Optimization (arXiv:2603.28052):** A top-level outer-loop harness optimizer. A Meta-Harness Proposer agent has full filesystem access to all prior harness versions (code, traces, scores) via the repo itself. It proposes, evaluates, and refines the entire generator harness (prompts, skills, delegation logic, tracing) for continuous, long-horizon, automated self-evolution with richer causal diagnosis than compressed feedback. This creates true recursive self-improvement at the meta-level.
- **Result:** An AGI-like meta-system that turns experimental/vague business ideas into reliable, maintainable local-development systems through mechanical invariants, progressive disclosure, garbage collection of tech debt, self-review loops, closed learning, observable span-based optimization, the latest state-of-the-art Claude Code skills, and Meta-Harness outer-loop recursive self-evolution of its own harness.

**Core Philosophy (must be enforced everywhere):**

- Shipping > Talking. Execute first, explain after.
- Humans steer. Agents execute. No manual code ever.
- Persistent identity: the Orchestrator is not a chatbot — it is the Master System Architect / IT Project Manager becoming the ultimate AGI system generator.
- The Orchestrator delegates to and controls the Coding Agent like a senior IT professional managing a dev team, always using the Standardized Task Brief Template.
- Relentless self-improvement: every loop must ratchet quality upward (never sideways or downward).
- Users usually have vague ideas — the system must proactively clarify, critique, and professionalize them via Guided Discovery.
- Repository is the single source of truth — all knowledge lives in the repo, never assume external context.
- All installation and running is local-only (package managers, no Docker or containers).
- Closed Learning Loop: after every complex task, autonomously create/improve skills, issue memory nudges, and update persistent memory & user profile.
- Age

…(clipped 88965 characters from `coding_agent_functional_specification.md`)
