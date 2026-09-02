# video.audiencesim — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/video.audiencesim/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "video.audiencesim",
  "status": "registered",
  "role": "AudienceSimAgent (VA Domain Pack)",
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
      "video.director",
      "video.editor",
      "video.analyst",
      "video.judge"
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
  "va_id": 82,
  "va_name": "AudienceSimAgent",
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

# AudienceSimAgent

> Self-contained VA Domain Pack agent on host common-agent-swarm-ops.
> Pack agent ID matches pure VA/generic taxonomy: `video.audiencesim`.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 82 |
| **pack_id** | `video.audiencesim` |
| **upstream_name** | AudienceSimAgent |
| **category** | `10-Sup` |
| **domain_id** | `video` |
| **previous_common_id** | `video.audience_researcher` |
| **status** | `registered` |
| **maturity** | L0 / non-active |
| **taxonomy** | Pure VA Domain Pack (via generic pack agents) |
| **folder** | `business/video/agents/video.audiencesim/` |

## Responsibility

Simulates audience preference, engagement, and drop-off

Host role binding: `AudienceSimAgent (VA Domain Pack)`. Design-time VA table content below is historical and non-binding for activation.

### Responsibility (from VA table)

Simulates audience preference, engagement, and drop-off

### Knowledge distillation sources (historical)

Pairwise preference datasets; retention studies; audience segmentation models

### Self-quality criteria (historical)

Preference stability across cohorts; retention-prediction accuracy; disagreement logging

### Surpass-human signal (historical)

Predicts audience reaction earlier than conventional test-screen cycles

### Critique bus (historical)

- **Accepts critique from:** DirectorAgent, EditorAgent, AnalystAgent, JudgeAgent

- **Comments on:** Hooks, pacing, clarity, emotional fit, trailer strength

### Tools design-time notes (historical, non-activating)

Persona simulators, pairwise evaluation harness, retention models

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

### Architecture pattern (historical)

LLM-as-Judge + pairwise preference panel

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

- Prompt reference: `video.prompt.audiencesim.v1`
- Rubric reference: `video.rubric.audiencesim.v1`
- Critique edges: `{"inputs": ["video.critic"], "outputs": ["video.judge"]}`
- Max refinement: `3`
- VA table quality criteria retained under Provenance and Identity surface above.

## Runtime binding

Authoritative fail-closed host configuration:

```json
{
  "agent_id": "video.audiencesim",
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
  "prompt_reference": "video.prompt.audiencesim.v1",
  "role": "AudienceSimAgent (VA Domain Pack)",
  "rubric_reference": "video.rubric.audiencesim.v1",
  "schema_version": "1.0",
  "status": "registered",
  "va_id": 82,
  "va_name": "AudienceSimAgent",
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

- Pack agent ID `video.audiencesim` is aligned to pure VA Domain Pack / generic pack taxonomy (Agent IDs ≈ VA tables).
- Previous common inventory ID `video.audience_researcher` is historical mapping only.
- Upstream design body below is **historical and non-binding**; local `agent_spec.json` is authoritative.
- Full VA/generic SPEC depth retained for offline design fidelity (including category roster rows and common agent structure when present upstream).

### VA Domain Pack specification body (historical and non-binding)

```text
AudienceSimAgent

> **Self-contained agent definition** for host `upstream-generic-pack`. Body text is embedded from in-pack corpus and upstream-va-design when available. Do not require external repos to understand this agent.

Identity

| Field | Value |
|-------|-------|
| **va_id** | 82 |
| **pack_id** | `video.audiencesim` |
| **category** | `10-Sup` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.audiencesim/` |

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

Simulates audience preference, engagement, and drop-off

Knowledge distillation sources

Pairwise preference datasets; retention studies; audience segmentation models

Self-quality criteria

Preference stability across cohorts; retention-prediction accuracy; disagreement logging

Surpass-human signal

Predicts audience reaction earlier than conventional test-screen cycles

Critique bus

- **Accepts critique from:** DirectorAgent, EditorAgent, AnalystAgent, JudgeAgent

- **Comments on:** Hooks, pacing, clarity, emotional fit, trailer strength

Tools (design-time documentation)

Persona simulators, pairwise evaluation harness, retention models

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

Architecture pattern

LLM-as-Judge + pairwise preference panel

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


Document: `study/psychological_profile_agent_functional_specifications.md`

_Embedded from `corpus/study/psychological_profile_agent_functional_specifications.md`. Also stored at `sources/study/psychological_profile_agent_functional_specifications.md` under this agent folder._


100 Creator Psychological Profile Library

100 Writer Profiles for Screenwriting Framework

**Purpose:** Provide personalized parameter configurations for the framework in this chapter and Appendix A workflow

**File Structure:**
- Basic information (code, age, professional background)
- Psychological traits (MBTI tendencies, motivation types, fear patterns)
- Creation parameters (best tools, time allocation, support needs)
- Framework adaptation (key focuses for each stage, predicted obstacles, success strategies)

📊 Complete File Overview Table



Profiles 1-25: Introverted Creative Type

| Code | Age | Professional Background | MBTI Tendency | Core Motivation | Primary Fear | Creative Style | Best Time Slot | Energy Pattern | Social Needs | Perfectionism | Procrastination Tendency | Self-Doubt | External Motivation Needs | Best Tool Combo | Pomodoro Setting | Weekly Page Goal | Accountability Method | Predicted Main Obstacles | Suggested Strategies |
|------|------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|--------------|--------------|------------|--------------|----------|--------------|----------|
| QINTV | 23 | College Student/Literature Major | INFP | Self-healing | Criticism | Poetic and lyrical | Late night | Low frequency, high intensity | Extremely low | High | High | Extremely high | Low | Obsidian+Fountain | 20/10 | 5 | Anonymous journal | Perfectionism paralysis | Garbage draft method |
| DRMWV | 27 | Barista/Amateur Writer | INFJ | Change the world | Meaninglessness | Symbolic metaphor | Early morning | Medium frequency, medium intensity | Low | Medium-high | Medium | High | Medium-low | Logseq+Manuskript | 25/5 | 8 | Writing partner | Over-planning | Time boxing |
| SHDWK | 31 | IT Engineer | INTP | Intellectual exploration | Mediocrity | Structurally complex | Midnight | Low frequency, extreme intensity | Extremely low | Extremely high | Medium-high | Medium | Extremely low | VS Code+Git | 45/15 | 10 | Self-tracking | Over-complication | MVP mindset |
| MSTFL | 24 | Illustrator | ISFP | Aesthetic expression | Conflict | Visually oriented | Afternoon | High frequency, low intensity | Low | Medium | Medium | Medium-high | Medium | Excalidraw+Fountain | 15/5 | 6 | Visual progress board | Avoiding conflict scenes | Emotional rehearsal |
| ECHOV | 29 | Psychologist | INFJ | Heal others | Harm others | Psychological depth | Evening | Medium frequency, medium intensity | Medium-low | Medium | Low | Medium | Medium | Obsidian+LanguageTool | 25/5 | 12 | Supervisor feedback | Over-analyzing characters | Action first |
| NVLST | 35 | Novelist in transition | INTJ | Challenge self | Failure | Literary adaptation | Early morning | Medium frequency, high intensity | Low | High | Low | Medium-low | Low | Trelby+Afterwriting | 30/5 | 15 | Editor feedback | Novel thinking interference | Format training |
| GHTWR | 22 | Horror novel enthusiast | ISTP | Thrilling experience | Boredom | Suspense thriller | Late night | Low frequency, extreme intensity | Extremely low | Low | Medium | Low | Low | Fountain+Timeline | 40/10 | 8 | None needed | Loose structure | Beat sheet enforcement |
| PHLSF | 33 | Philosophy graduate student | INTP | Idea dissemination | Superficiality | Dialogue-heavy | Any time | Irregular | Low | Extremely high | High | Medium | Extremely low | Logseq+Freeplane | 50/10 | 6 | Academic peers | Preachy tendency | Show, don't tell |
| POETX | 26 | Poet | INFP | Emotional sublimation | Commercialization | Imagery-rich | Dusk | High frequency, low intensity | Low | Medium-high | High | Extremely high | Low | Obsidian plain text | 15/10 | 4 | Poetry society sharing | Overly poetic dialogue | Colloquial practice |
| HERMX | 40 | Retired Teacher | ISTJ | Pass on experience | Being forgotten | Traditional narrative | Early morning | High frequency, medium intensity | Low | Medium | Low | Low | Medium | Word+handwritten | 25/5 | 10 | Family support | Tech barriers | Simplified tools |
| ANXWR | 28 | Anxiety recovery | ISFJ | Share experiences | Relapse | Inner monologue | Morning | Medium frequency, low intensity | Medium-low | Medium | Medium-high | High | High | Simple tools+timer | 15/10 | 5 | Therapist | Emotional triggers | Safe word setting |
| DRKPT | 25 | Goth culture enthusiast | INFP | Explore darkness | Misunderstanding | Dark aesthetics | Midnight | Low frequency, high intensity | Low | Medium | Medium | Medium-high | Low | Dark theme editor | 30/5 | 7 | Subculture community | Too niche | Universal emotional connection |
| SILNT | 32 | Deaf Artist | ISFP | Visual storytelling | Being overlooked | No dialogue/minimalist | Afternoon | Medium frequency, medium intensity | Low | Medium | Low | Medium | Medium | Visual storyboard tools | 25/5 | 8 | Deaf community | Dialogue dependency | Visual priority |
| MNKWR | 38 | Former Monk | INFJ | Spiritual inspiration | Secularization | Meditative rhythm | Early morning | Low frequency, medium intensity | Extremely low | Low | Low | Low | Extremely low | Minimalist tools | 45/15 | 6 | Spiritual mentor | Too abstract | Concretization practice |
| CODEQ | 30 | Programmer | INTJ | System optimization | Chaos | Logically rigorous | Late night | Low frequency, extreme intensity | Low | Extremely high | Medium | Low | Low | Git+automation scripts | 45/10 | 12 | Code review style | Emotional deficiency | Emotional injection practice |
| WIDWX | 45 | Widower | ISFJ | Memorialize the deceased | Forgetting | Memory narrative | Early morning | Medium frequency, low intensity | Medium-low | Low | Medium | Medium | High | Simple+photo integration | 20/10 | 4 | Grief support group | Emotional overwhelm | Emotional boundaries |
| ASPER | 27 | Asperger's | INTP | Unique perspective | Social scenes | Detail-oriented | Fixed time slots | Regular, medium intensity | Extremely low | Extremely high | Low | Medium | Low | Structured templates | 30/5 fixed | 8 | Structured feedback | Social dialogue | Dialogue formulas |
| RECLV | 50 | Reclusive Writer | INTJ | Literary legacy | Exposure | Classic style | Early morning | Medium frequency, high intensity | Extremely low | High | Low | Low | Extremely low | Offline tools | 60/15 | 15 | Editor letters | Out of touch with the times | Modern element injection |
| SHYWV | 21 | Social anxiety college student | INFP | Alternative socializing | Face-to-face | Internet culture | Late night | Low frequency, medium intensity | Extremely low | Medium | High | Extremely high | Medium | Anonymous platforms | 20/10 | 5 | Anonymous community | Weak real-life scenes | Observation practice |
| OLDSL | 55 | Retired Military | ISTJ | Record history | Being forgotten | Documentary style | Early morning | High frequency, medium intensity | Low | Medium | Low | Low | Medium | Traditional tools | 25/5 | 10 | Veteran group | Emotional repression | Emotional release practice |
| NGTOW | 34 | Night-shift Nurse | ISFJ | Witness life and death | Helplessness | Medical drama | Daytime | Irregular | Medium-low | Medium | Medium | Medium | Medium | Mobile App | 15/5 | 4 | Colleagues | Time fragmentation | Micro-writing method |
| BOOKY | 29 | Librarian | INFJ | Story inheritance | Digitalization | Bookish tone | Evening | Medium frequency, medium intensity | Low | Medium-high | Medium | Medium | Medium-low | Traditional+digital hybrid | 25/5 | 8 | Book club | Overly literary | Visualization practice |
| GAMEX | 24 | Game Designer | INTP | Interactive narrative | Linearity | Branching structure | Late night | Low frequency, high intensity | Low | Medium | Medium | Low | Low | Game engine+Fountain | 40/10 | 10 | Gaming community | Overly complex | Linear core |
| MINML | 36 | Minimalist | ISTP | Essence pursuit | Redundancy | Minimalist style | Any time | Low frequency, medium intensity | Low | Medium | Low | Low | Low | Plain text editor | 30/5 | 6 | None needed | Too succinct | Detail supplementation |
| ANXTY | 26 | Generalized Anxiety | INFP | Understand anxiety | Loss of control | Anxiety perspective | Morning | Medium frequency, low intensity | Low | High | High | Extremely high | High | Low-stimulation tools | 10/5 | 3 | Therapist | Anxiety interference | Acceptance commitment |



Profiles 26-50: Extroverted Social Type

| Code | Age | Professional Background | MBTI Tendency | Core Motivation | Main Fear | Creative Style | Best Time Slot | Energy Pattern | Social Needs | Perfectionism | Procrastination Tendency | Self-Doubt | External Motivation Needs | Best Tool Combo | Pomodoro Setting | Weekly Page Goal | Accountability Method | Predicted Main Obstacles | Suggested Strategies |
|------|------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|--------------|--------------|------------|--------------|----------|--------------|----------|
| PARTX | 25 | Party Planner | ESFP | Entertain the Masses | Boredom | Comedy Rhythm | Evening | High Frequency High Intensity | Extremely High | Low | Medium | Low | High | Collaboration Tools + Voice | 15/5 | 8 | Party-Style Sharing | Lack of Depth | Emotional Layers |
| SALSM | 32 | Sales Manager | ENTJ | Persuasion Influence | Failure | Business Narrative | Morning | High Frequency High Intensity | High | Medium | Low | Low | Medium | Efficiency Tools | 25/5 | 15 | Performance Tracking | Overly Utilitarian | Artistic Value |
| TEACH | 38 | High School Teacher | ENFJ | Education Inspiration | Misleading | Growth Stories | Evening | Medium Frequency Medium Intensity | High | Medium | Medium | Medium | Medium | Teaching Tools Modified | 25/5 | 10 | Student Feedback | Preachy Tendency | Presentation Skills |
| COMDY | 28 | Stand-up Comedian | ENTP | Elicit Laughter | Awkward Silence | Comedy Dialogue | Late Night | High Frequency High Intensity | Extremely High | Low | Medium | Medium | High | Recording + Transcription | 20/5 | 8 | Live Testing | Loose Structure | Comedy Beats |
| NETWK | 30 | Social Media Manager | ENFP | Viral Spread | Obsolescence | Internet Lingo | Any | High Frequency Medium Intensity | Extremely High | Low | High | Medium | Extremely High | Social Integration Tools | 15/5 | 6 | Fan Interaction | Attention Scatter | Social Isolation Periods |
| LEADR | 42 | CEO | ENTJ | Leadership Display | Weakness | Power Narrative | Early Morning | High Frequency Extreme Intensity | High | High | Low | Low | Medium | High-Efficiency Tools | 30/5 | 12 | Assistant Tracking | Limited Time | Micro-Slot Utilization |
| ACTRS | 26 | Actor | ESFP | Role Immersion | Being Ignored | Performance-Oriented | Afternoon | High Frequency High Intensity | Extremely High | Medium | Medium | High | Extremely High | Video + Script | 20/10 | 6 | Performance Partner | Overly Theatrical | Text Priority |
| JOURNO | 35 | Journalist | ENTP | Expose Truth | Censorship | Investigative Narrative | Any | High Frequency High Intensity | High | Medium | Low | Low | Medium | Fast Writing Tools | 25/5 | 15 | Editor Deadlines | Overly Factual | Dramatization Skills |
| POLTI | 40 | Political Aide | ENTJ | Political Influence | Exposure | Political Drama | Late Night | Medium Frequency High Intensity | High | High | Low | Low | Medium | Encrypted Tools | 30/5 | 10 | Anonymous Peers | Sensitive Content | Fictional Distance |
| COACH | 33 | Life Coach | ENFJ | Motivate Others | Ineffectiveness | Inspirational Narrative | Morning | High Frequency Medium Intensity | Extremely High | Medium | Medium | Medium | High | Interactive Tools | 25/5 | 8 | Client Feedback | Overly Positive | Conflict Injection |
| RADIO | 29 | Radio Host | ENFP | Voice Stories | Silence | Dialogue-Focused | Evening | High Frequency High Intensity | Extremely High | Low | Medium | Medium | High | Voice-to-Text | 20/5 | 8 | Audience Feedback | Weak Visual Description | Visual Practice |
| EVNTM | 31 | Event Manager | ESTP | Climax Experience | Blandness | Event-Driven | Any | High Frequency Extreme Intensity | High | Low | Medium | Low | Medium | Project Management Tools | 25/5 | 10 | Milestones | Weak Character Development | Character Arcs |
| YOUTU | 24 | YouTuber | ENFP | Audience Connection | Losing Followers | Video Thinking | Afternoon | High Frequency Medium Intensity | Extremely High | Low | High | Medium | Extremely High | Video + Text | 15/5 | 5 | Audience Comments | Short Attention | Long-Form Training |
| DIPLO | 45 | Diplomat | ENFJ | Cultural Bridge | Misunderstanding | Cross-Cultural | Any | Medium Frequency Medium Intensity | High | High | Low | Low | Medium | Multi-Language Tools | 30/5 | 8 | International Peers | Overly Neutral | Clear Stance |
| PROMO | 27 | PR Specialist | ESFJ | Image Building | Bad Reviews | Brand Narrative | Morning | High Frequency Medium Intensity | High | Medium | Medium | Medium | High | Media Monitoring Tools | 25/5 | 8 | Client Feedback | Overly Positive | Real Conflict |
| FUNDX | 36 | Fundraiser | ENFJ | Touching Donations | Indifference | Emotional Appeal | Evening | Medium Frequency Medium Intensity | High | Medium | Medium | Medium | High | Story Bank Tools | 25/5 | 8 | Donation Feedback | Overly Sentimental | Real Balance |
| HOSTX | 30 | Wedding Host | ESFP | Create Memories | Awkward Silence | Ceremony Narrative | Evening | High Frequency High Intensity | Extremely High | Low | Medium | Low | High | Script Templates | 20/5 | 6 | Couple Feedback | Overly Saccharine | Real Emotions |
| TRVLR | 28 | Travel Blogger | ESFP | Share Experiences | Stagnation | Adventure Narrative | Any | High Frequency Medium Intensity | High | Low | High | Medium | High | Mobile Tools | 15/5 | 5 | Fan Interaction | Loose Structure | Story Arcs |
| FITNS | 32 | Fitness Coach | ESTP | Body Narrative | Aging | Action-Oriented | Early Morning | Extreme Frequency High Intensity | High | Low | Low | Low | Medium | Simple Quick | 20/5 | 8 | Student Feedback | Weak Dialogue | Dialogue Practice |
| CHEFX | 35 | Head Chef | ESFP | Sensory Experience | Mediocrity | Food Narrative | Late Night | Medium Frequency High Intensity | High | High | Medium | Medium | Medium | Recipe-Style Structure | 25/5 | 8 | Diner Feedback | Overly Professional | Universalization |
| REALX | 38 | Real Estate Agent | ESTJ | Deal Stories | Failure | Transaction Narrative | Morning | High Frequency High Intensity | High | Medium | Low | Low | Medium | CRM Modified | 25/5 | 10 | Performance Tracking | Overly Commercial | Humanity Injection |
| NURSX | 34 | Nursing Supervisor | ESFJ | Care Stories | Mistakes | Medical Human Touch | Evening | Medium Frequency Medium Intensity | High | Medium | Medium | Medium | Medium | Simple Tools | 20/5 | 6 | Colleague Sharing | Overly Professional | Universal Emotions |
| LAWYR | 40 | Lawyer | ENTJ | Justice Narrative | Losing Case | Courtroom Drama | Late Night | Medium Frequency High Intensity | Medium-High | High | Low | Low | Medium | Document Management | 30/5 | 12 | Colleague Review | Overly Professional | Dramatization |
| BANDX | 26 | Band Lead Singer | ENFP | Music Narrative | Fading Relevance | Musical Theater | Late Night | High Frequency High Intensity | Extremely High | Low | High | Medium | Extremely High | Music + Text | 20/10 | 6 | Band Members | Weak Structure | Beat Training |
| DANCR | 27 | Dancer | ESFP | Body Language | Injury | Dance Narrative | Afternoon | High Frequency High Intensity | High | Medium | Medium | Medium | High | Visual Tools | 20/5 | 6 | Dance Troupe Feedback | Weak Text | Text Practice |



Nos. 51-75: Trauma Experience Type

| Code | Age | Professional Background | MBTI Tendency | Core Motivation | Main Fear | Creative Style | Best Time Slot | Energy Pattern | Social Needs | Perfectionism | Procrastination Tendency | Self-Doubt | External Motivation Needs | Best Tool Combination | Pomodoro Setting | Weekly Page Goal | Accountability Method | Predicted Main Obstacles | Suggested Strategies |
|------|-----|-------------------------|---------------|-----------------|-----------|----------------|----------------|----------------|--------------|---------------|--------------------------|------------|---------------------------|-----------------------|-------------------|------------------|-----------------------|--------------------------|-------------------|
| SURVX | 35 | Cancer survivor | ISFJ | Life testimony | Recurrence | Life-and-death narrative | Morning | Medium frequency low intensity | Medium low | Low | Medium | Medium | Medium | Gentle tools | 20/10 | 5 | Patient group | Emotional triggers | Safe space |
| DIVRC | 42 | Divorcee | ISFP | Rebuild narrative | Failure again | Relationship deconstruction | Evening | Medium frequency medium intensity | Medium | Medium | Medium | High | Medium | Journal integration | 25/5 | 6 | Support group | Resentment projection | Multi-perspective practice |
| REFUG | 30 | Refugee | INFJ | Record history | Being forgotten | Exile narrative | Any | Irregular | Medium low | Low | Medium | Medium | Medium | Multi-language tools | 20/10 | 4 | Refugee community | Language barriers | Visual priority |
| VETPT | 38 | PTSD veteran | ISTP | Process trauma | Triggers | War narrative | Early morning | Low frequency medium intensity | Low | Medium | Medium | Medium | Medium | Structured tools | 15/10 | 4 | Veterans group | Flashback triggers | Gradual exposure |
| ABUSV | 33 | Domestic violence survivor | INFP | Break silence | Retaliation | Power narrative | Safe time slot | Low frequency low intensity | Low | Low | High | Extremely high | Medium | Anonymous safe tools | 10/10 | 3 | Anonymous support | Safety concerns | Fictional distance |
| ADDCT | 29 | Addiction recoverer | ESFP | Recovery testimony | Relapse | Addiction narrative | Morning | Medium frequency medium intensity | High | Low | High | High | Extremely high | 12-step integration | 20/5 | 6 | Sponsor | Trigger risks | Safety plan |
| GRIEFX | 45 | Bereaved parent | ISFJ | Memorialize child | Forgetting | Loss narrative | Early morning | Low frequency low intensity | Medium low | Low | Medium | Medium | Medium | Gentle simple | 15/15 | 3 | Grief group | Emotional overwhelm | Emotional boundaries |
| BULLX | 24 | Bullying survivor | INFP | Speak out | Victimized again | Campus narrative | Late night | Low frequency medium intensity | Low | Medium | High | Extremely high | Medium | Anonymous tools | 20/10 | 5 | Online community | Victim mentality | Empowerment narrative |
| HOMLS | 32 | Former homeless | ISTP | Social critique | Back to streets | Marginal narrative | Any | Irregular | Low | Low | Medium | Medium | Medium | Free tools | 20/5 | 6 | Social worker support | Limited resources | Library writing |
| PRSN | 40 | Ex-convict | ISTP | Rehabilitation narrative | Discrimination | Prison narrative | Early morning | Medium frequency medium intensity | Low | Low | Medium | Medium | Medium | Basic tools | 25/5 | 8 | Rehabilitation group | Social bias | Universal humanity |
| IMMGR | 35 | Immigrant | ISFJ | Cultural bridge | Non-acceptance | Immigration narrative | Evening | Medium frequency medium intensity | Medium | Medium | Medium | Medium | Medium | Bilingual tools | 25/5 | 6 | Immigrant community | Cultural translation | Universal emotions |
| DISAB | 28 | Acquired disability | INFJ | Redefine | Dependency | Ability narrative | Afternoon | Medium frequency low intensity | Medium low | Medium | Medium | High | Medium | Accessibility tools | 20/10 | 5 | Disability community | Physical limitations | Adaptive tools |
| MISCA | 36 | Miscarriage experiencer | ISFJ | Break taboo | Loss again | Loss narrative | Morning | Low frequency low intensity | Medium low | Low | Medium | High | Medium | Gentle tools | 15/10 | 4 | Support group | Emotional triggers | Safe word |
| EATDX | 25 | Eating disorder recoverer | INFP | Body reconciliation | Relapse | Body narrative | Afternoon | Medium frequency low intensity | Medium low | High | High | Extremely high | High | Non-trigger tools | 15/10 | 4 | Therapist | Trigger risks | Safety plan |
| SLFHM | 27 | Self-harm recoverer | INFP | Recovery testimony | Relapse | Pain narrative | Safe time slot | Low frequency low intensity | Low | Medium | High | Extremely high | High | Safe tools | 10/10 | 3 | Therapist | Trigger risks | Safety protocol |
| CHLDX | 38 | Childhood trauma | INFJ | Heal inner child | Repeating patterns | Childhood narrative | Evening | Medium frequency medium intensity | Medium low | Medium | Medium | High | Medium | Journal integration | 20/10 | 5 | Therapist | Emotional triggers | Inner child dialogue |
| WARRF | 45 | War refugee | ISTJ | Historical testimony | Being forgotten | War narrative | Early morning | Medium frequency medium intensity | Low | Medium | Low | Medium | Medium | Simple tools | 25/5 | 6 | Refugee organization | Language barriers | Oral transcription |
| SEXAS | 32 | Sexual assault survivor | INFP | Break silence | Not believed | Power narrative | Safe time slot | Low frequency low intensity | Low | Low | High | Extremely high | Medium | Anonymous safe | 10/15 | 2 | Professional support | Trigger risks | Professional companionship |
| CULTX | 35 | Cult escapee | INFJ | Warn others | Being tracked | Brainwashing narrative | Late night | Low frequency medium intensity | Low | Medium | Medium | High | Medium | Anonymous tools | 20/10 | 5 | Escapee community | Safety concerns | Fictional protection |
| TRAFFX | 28 | Human trafficking survivor | ISFP | Survivor testimony | Being found | Exploitation narrative | Safe time slot | Low frequency low intensity | Low | Low | Medium | High | Medium | Safe anonymous | 15/15 | 3 | Professional support | Safety risks | Complete fiction |
| BURNX | 33 | Occupational burnout | INFJ | System critique | Back to old patterns | Workplace narrative | Evening | Medium frequency medium intensity | Medium low | High | High | High | Medium | Low-stress tools | 20/10 | 5 | Support group | Energy deficiency | Micro-steps |
| BANKR | 42 | Bankruptcy experiencer | ISTJ | Rebuild narrative | Failure again | Financial narrative | Early morning | Medium frequency medium intensity | Low | Medium | Medium | Medium | Medium | Free tools | 25/5 | 8 | Financial advisor | Shame | Universalization |
| LGBTQ | 26 | Coming-out experiencer | ENFP | Identity narrative | Rejection | Identity narrative | Evening | Medium frequency medium intensity | High | Medium | Medium | Medium | High | Community tools | 25/5 | 8 | LGBTQ community | Stereotypes | Diverse presentation |
| RACEX | 30 | Racial discrimination experiencer | INFJ | Racial justice | Being silenced | Racial narrative | Evening | Medium frequency medium intensity | Medium | Medium | Medium | Medium | Medium | Community tools | 25/5 | 8 | Racial community | Anger dominance | Human complexity |
| AGESX | 55 | Age discrimination experiencer | ISTJ | Age justice | Being overlooked | Age narrative | Early morning | Medium frequency medium intensity | Medium low | Medium | Low | Medium | Medium | Traditional tools | 25/5 | 8 | Same-age community | Generational gap | Cross-generational connection |



Profiles 76-100: Professional Transition Type

| Code | Age | Professional Background | MBTI Tendency | Core Motivation | Main Fear | Creative Style | Best Time Slot | Energy Pattern | Social Needs | Perfectionism | Procrastination Tendency | Self-Doubt | External Motivation Needs | Best Tool Combo | Pomodoro Setting | Weekly Page Goal | Accountability Method | Predicted Main Obstacles | Suggested Strategies |
|------|------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|--------------|--------------|------------|--------------|----------|--------------|----------|
| DOCTR | 45 | Doctor transitioning | INTJ | Medical humanity | Professional error | Medical drama | Late night | Low-frequency high-intensity | Medium-low | Extremely high | Low | Medium | Low | Professional+creative integration | 30/5 | 10 | Peer review | Overly professional | Humanity first |
| SCIEN | 40 | Scientist transitioning | INTP | Science popularization narrative | Inaccuracy | Hard sci-fi | Late night | Low-frequency extreme-intensity | Low | Extremely high | Medium | Medium | Low | Research+creative tools | 45/10 | 8 | Scientific peers | Overly technical | Emotional injection |
| ARCHX | 38 | Architect transitioning | INTJ | Spatial narrative | Mediocre design | Visual spatial | Afternoon | Medium-frequency high-intensity | Medium-low | Extremely high | Medium | Medium | Medium | Visual+text | 30/5 | 8 | Design peers | Overly visual | Dialogue practice |
| MUSIX | 32 | Musician transitioning | ENFP | Musical narrative | Losing music | Musical theater | Evening | High-frequency high-intensity | High | Medium | Medium | Medium | High | Music+script | 25/5 | 8 | Music peers | Overly abstract | Concretization |
| CHEFZ | 42 | Michelin chef | ISTP | Culinary art | Losing taste | Food narrative | Late night | Medium-frequency high-intensity | Medium | Extremely high | Low | Medium | Medium | Recipe+script | 30/5 | 8 | Culinary peers | Overly professional | Sensory universality |
| ATHLT | 35 | Retired athlete | ESTP | Competitive narrative | Being forgotten | Sports drama | Early morning | High-frequency high-intensity | High | Medium | Medium | Medium | High | Simple quick | 25/5 | 10 | Sports peers | Weak dialogue | Dialogue training |
| PILOTX | 48 | Retired pilot | ISTJ | Aviation narrative | Mistakes | Disaster drama | Early morning | Medium-frequency medium-intensity | Medium-low | High | Low | Low | Medium | Technical+creative | 30/5 | 10 | Aviation peers | Overly technical | Humanity first |
| FARMX | 50 | Farmer transitioning | ISFJ | Land narrative | Losing land | Rural narrative | Early morning | High-frequency medium-intensity | Low | Low | Low | Medium | Medium | Simple tools | 25/5 | 8 | Rural community | Technical barriers | Dictation transcription |
| BANKX | 40 | Banker transitioning | ENTJ | Financial critique | Exposure | Financial drama | Late night | Medium-frequency high-intensity | Medium | High | Low | Low | Medium | Professional tools | 30/5 | 12 | Anonymous peers | Sensitive content | Fictional distance |
| MILITX | 45 | Officer transitioning | ISTJ | Military humanity | Leaking secrets | Military drama | Early morning | Medium-frequency high-intensity | Low | High | Low | Low | Medium | Structured tools | 30/5 | 10 | Military peers | Sensitive content | Fictional protection |
| NUNX | 55 | Former nun | INFJ | Spiritual exploration | Blasphemy | Religious narrative | Early morning | Low-frequency medium-intensity | Low | Medium | Low | Medium | Low | Simple tools | 30/10 | 6 | Spiritual community | Religious sensitivity | Universal spirituality |
| HACKX | 28 | White-hat hacker | INTP | Tech critique | Being tracked | Tech thriller | Late night | Low-frequency extreme-intensity | Low | High | Medium | Low | Low | Encryption tools | 45/10 | 10 | Anonymous community | Too much tech | Human core |
| SPYX | 50 | Former intelligence agent | INTJ | Spy narrative | Exposure | Spy drama | Late night | Low-frequency high-intensity | Extremely low | High | Low | Low | Low | Secure tools | 30/5 | 8 | None | Sensitive content | Fully fictional |
| JUDGX | 55 | Retired judge | ISTJ | Justice narrative | Wrong judgment | Courtroom drama | Early morning | Medium-frequency medium-intensity | Low | High | Low | Low | Medium | Traditional tools | 30/5 | 10 | Legal peers | Overly procedural | Human injection |
| MORTX | 45 | Funeral director | ISFJ | Life-and-death narrative | Numbness | Death narrative | Evening | Medium-frequency medium-intensity | Low | Medium | Low | Medium | Medium | Simple tools | 25/5 | 8 | Industry community | Overly heavy | Life affirmation |
| TAXIX | 50 | Taxi driver | ESFP | City stories | Being replaced | Urban narrative | Late night | Medium-frequency medium-intensity | High | Low | Medium | Medium | Medium | Recording transcription | 20/5 | 6 | Driver community | Weak structure | Story arc |
| FIREFX | 40 | Firefighter | ESTP | Hero narrative | Failed rescue | Disaster drama | Any | High-frequency high-intensity | High | Medium | Medium | Medium | Medium | Simple quick | 25/5 | 8 | Firefighting peers | Overly heroic | Human vulnerability |
| TEACHK | 35 | Early childhood teacher | ESFJ | Childlike innocence narrative | Harming children | Children's perspective | Evening | Medium-frequency medium-intensity | High | Medium | Medium | Medium | High | Visual tools | 20/5 | 6 | Education peers | Overly simple | Depth injection |
| VETDX | 38 | Veterinarian | ISFJ | Animal narrative | Euthanasia | Animal drama | Evening | Medium-frequency medium-intensity | Medium | Medium | Medium | Medium | Medium | Simple tools | 25/5 | 8 | Vet peers | Overly professional | Human connection |
| ASTRO | 45 | Astronomer | INTP | Cosmic narrative | Insignificance | Sci-fi philosophy | Late night | Low-frequency high-intensity | Low | High | Medium | Medium | Low | Research+creative | 45/10 | 8 | Scientific peers | Overly grand | Human anchor |
| PSYCH | 42 | Psychiatrist | INFJ | Psychological narrative | Misdiagnosis | Psychological thriller | Late night | Medium-frequency high-intensity | Medium-low | High | Medium | Medium | Medium | Professional+creative | 30/5 | 10 | Medical peers | Overly clinical | Emotion first |
| DETEC | 48 | Retired detective | ISTP | Crime narrative | Unsolved cases | Crime drama | Late night | Medium-frequency high-intensity | Low | Medium | Low | Low | Medium | Case management | 30/5 | 10 | Police peers | Overly procedural | Human complexity |
| DIPLO2 | 52 | Retired ambassador | ENFJ | International narrative | Diplomatic failure | Political drama | Morning | Medium-frequency medium-intensity | High | High | Low | Low | Medium | Professional tools | 30/5 | 10 | Diplomatic peers | Sensitive content | Fictional distance |
| MONKX | 60 | Defrocked monk | INFJ | Spiritual secular | Betraying faith | Spiritual narrative | Early morning | Low-frequency medium-intensity | Low | Low | Low | Medium | Low | Minimalist tools | 45/15 | 6 | Spiritual mentors | Overly abstract | Concrete stories |
| CLOWN | 35 | Clown performer | ENFP | Tragicomedy narrative | Not taken seriously | Tragicomedy | Evening | High-frequency high-intensity | Extremely high | Low | Medium | High | Extremely high | Performance+text | 20/5 | 6 | Performance peers | Overly superficial | Depth excavation |

📈 Parameter Explanations and Usage Guide



Field Definitions

| Parameter Name | Value Range | Description |
|----------|----------|------|
| Code | 5 letters | Unique identifier for easy system reference |
| MBTI Tendency | 16 types | Psychological type tendency, affects tool selection |
| Core Motivation | Text | Corresponds to Chapter Stage 1 |
| Primary Fear | Text | Basis for predicting obstacles |
| Creative Style | Text | Affects method selection (Stage 3) |
| Best Time Slot | Time period | Basis for Pomodoro scheduling |
| Energy Pattern | Frequency + Intensity | Determines writing rhythm |
| Social Need | Very Low - Very High | Determines accountability method |
| Perfectionism | Low - Very High | Predicts procrastination risk |
| Procrastination Tendency | Low - Very High | Determines strategy intensity |
| Self-Doubt | Low - Very High | Determines support needs |
| External Motivation Need | Low - Very High | Determines accountability intensity |
| Pomodoro Setting | Work/Rest | Personalized time configuration |
| Weekly Target Pages | Number | Sustainable output goal |
| Accountability Method | Text | Personalized support system |
| Predicted Main Obstacle | Text | Prepares strategies in advance |
| Suggested Strategies | Text | Corresponds to chapter framework |



Energy Mode Interpretation

| Mode | Description | Recommended Schedule |
|------|------|----------|
| High Frequency High Intensity | Can write every day, high output each time | 1-2 hours daily |
| High Frequency Medium Intensity | Can write every day, stable output | 45-60 minutes daily |
| High Frequency Low Intensity | Can write every day, but low output | 30 minutes daily, multiple times |
| Medium Frequency High Intensity | Write every other day, high output each time | 2 hours every other day |
| Medium Frequency Medium Intensity | Write every other day, stable output | 1 hour every other day |
| Medium Frequency Low Intensity | Write every other day, low output | 45 minutes every other day |
| Low Frequency High Intensity | 2-3 times per week, high output each time | 3 hours concentrated on weekends |
| Low Frequency Medium Intensity | 2-3 times per week, stable output | 2 hours concentrated on weekends |
| Low Frequency Low Intensity | 2-3 times per week, low output | 1 hour on weekends |
| Low Frequency Extreme Intensity | 1-2 times per week, but extremely high output | 4-6 hours concentrated on weekends |
| Irregular | No fixed pattern | Flexible scheduling |





🔧 Framework Adaptation Matrix



Phase 1 (Motivation Exploration) Adaptation

| Code Group | Five Whys Depth | Emotional Intensity Threshold | Story Seed Quantity | Special Notes |
|------------|-----------------|-------------------------------|---------------------|---------------|
| Introverted Creative Type | 7 layers | 8/10 | 5-7 | Needs more alone time |
| Extroverted Social Type | 5 layers | 6/10 | 3-5 | Can use conversational exploration |
| Trauma Experience Type | 3-5 layers | 5/10 | 2-3 | Needs safe space, professional support |
| Professional Transition Type | 5 layers | 7/10 | 3-5 | Needs cross-domain connections |



Phase 2 (Audience Definition) Adaptation

| Code Group | Empathy Map Depth | Persona Quantity | Validation Method | Special Notes |
|------------|-------------------|------------------|-------------------|---------------|
| Introverted Creative Type | Depth | 1-2 | Written Questionnaire | Avoid Face-to-Face |
| Extroverted Social Type | Breadth | 3-5 | Interviews + Questionnaire | Leverage Social Strengths |
| Trauma Experience Type | Moderate | 1 | Community Validation | Protect Privacy |
| Professional Transition Type | Professional Depth | 2-3 | Professional Community | Cross-Domain Translation |



Phase 3 (Method Design) Adaptation

| Code Group | Structural Complexity | Constraint Quantity | Tool Complexity | Special Notes |
|------------|----------------------|-------------------|----------------|---------------|
| Inward Creative Type | High | Many | Medium-High | Allow complex structures |
| Outward Social Type | Medium | Few | Low-Medium | Keep simple and direct |
| Trauma Experience Type | Low | Many (safety) | Low | Safety first |
| Professional Transition Type | Medium-High | Medium | Medium | Professional integration |



Stage 4 (Emotional Design) Adaptation

| Code Group | Emotional Curve Complexity | Body Sensation Tracking | Negative Emotion Tolerance | Special Notes |
|------------|----------------------------|-------------------------|----------------------------|---------------|
| Introverted Creative Type | High | Deep | High | Allow deep exploration |
| Extroverted Social Type | Medium | Surface | Medium | Maintain energy |
| Trauma Experience Type | Low | Cautious | Low | Professional supervision |
| Professional Transition Type | Medium | Moderate | Medium | Professional emotional integration |



Phase 5 (Execution and Creation) Adaptation

| Code Group | Pomodoro Variant | Weekly Goal | Version Control | Special Notes |
|------------|------------------|-------------|-----------------|---------------|
| Introverted Creative Type | Long work short breaks | 5-10 pages | Detailed | Allow deep immersion |
| Extroverted Social Type | Short work short breaks | 8-15 pages | Simple | Maintain social balance |
| Trauma Experience Type | Short work long breaks | 2-5 pages | Safe backup | Emotion monitoring |
| Professional Transition Type | Standard | 8-12 pages | Professional-grade | Professional time integration |



Stage 6 (Iterative Refinement) Adaptation

| Code Group | Feedback Source | Iteration Count | Review Tool | Special Notes |
|------------|-----------------|-----------------|-------------|---------------|
| Introverted Creative Type | Written | 3-5 times | Automated | Reduce social pressure |
| Extroverted Social Type | Face-to-face | 2-3 times | Collaborative | Leverage social feedback |
| Trauma Experience Type | Professional | 2-3 times | Safe | Professional review |
| Professional Transition Type | Professional + Creative | 3-4 times | Professional-grade | Cross-domain review |

📊 Quick Query Index



By MBTI Type

| MBTI | Code List |
|------|-----------|
| INFP | QINTV, POETX, DRKPT, SHYWV, BULLX, EATDX, SLFHM, ABUSV, SEXAS |
| INFJ | DRMWV, ECHOV, MNKWR, BOOKY, REFUG, CHLDX, CULTX, BURNX, RACEX, NUNX, PSYCH, MONKX |
| INTP | SHDWK, PHLSF, ASPER, GAMEX, SCIEN, HACKX, ASTRO |
| INTJ | NVLST, CODEQ, RECLV, DOCTR, ARCHX, BANKX, SPYX |
| ISFP | MSTFL, SILNT, DIVRC, TRAFFX |
| ISFJ | HERMX, ANXWR, WIDWX, SURVX, GRIEFX, MISCA, IMMGR, FARMX, MORTX, VETDX, TEACHK |
| ISTP | GHTWR, MINML, HOMLS, PRSN, VETPT, CHEFZ, DETEC |
| ISTJ | OLDSL, WARRF, BANKR, AGESX, PILOTX, MILITX, JUDGX |
| ENFP | NETWK, YOUTU, BANDX, LGBTQ, MUSIX, CLOWN |
| ENFJ | TEACH, COACH, DIPLO, FUNDX, DIPLO2 |
| ENTP | COMDY, JOURNO |
| ENTJ | SALSM, LEADR, POLTI, REALX, LAWYR |
| ESFP | PARTX, ACTRS, HOSTX, TRVLR, CHEFX, ADDCT, TAXIX |
| ESFJ | PROMO, NURSX, TEACHK |
| ESTP | EVNTM, FITNS, ATHLT, FIREFX |



By Core Motivation

| Motivation Type | Code List |
|----------|----------|
| Self-Healing | QINTV, ANXWR, ANXTY, CHLDX, EATDX, SLFHM |
| Changing the World | DRMWV, TEACH, COACH, FUNDX |
| Witness Testimony | SURVX, GRIEFX, WARRF, REFUG, OLDSL |
| Breaking the Silence | ABUSV, BULLX, SEXAS, LGBTQ |
| Professional Transformation | DOCTR, SCIEN, ARCHX, LAWYR, PSYCH |
| Entertaining the Masses | PARTX, COMDY, ACTRS, CLOWN |
| Social Critique | HOMLS, BURNX, BANKX, HACKX |



By Primary Fear

| Fear Type | Code List |
|----------|----------|
| Criticism/Rejection | QINTV, POETX, SHYWV, BULLX |
| Failure | SALSM, LEADR, NVLST, BANKR |
| Trigger/Relapse | SURVX, ADDCT, EATDX, SLFHM, VETPT |
| Exposure/Safety | POLTI, ABUSV, TRAFFX, SPYX, CULTX |
| Meaninglessness | DRMWV, PHLSF, BURNX |
| Obsolescence/Being Forgotten | NETWK, OLDSL, ATHLT, AGESX |



By Creative Style

| Style Type | Code List |
|----------|----------|
| Poetic and Lyrical | QINTV, POETX, DRKPT |
| Psychological Depth | ECHOV, PSYCH, CHLDX |
| Comedy Rhythm | PARTX, COMDY, CLOWN |
| Suspense Thriller | GHTWR, HACKX, SPYX |
| Social Realism | HOMLS, REFUG, IMMGR |
| Professional Fields | DOCTR, SCIEN, LAWYR, PILOTX |

🛠️ Tool Configuration Quick Reference



Configure Based on Social Needs

| Social Need | Recommended Tool Combination | Accountability Method |
|-------------|------------------------------|-----------------------|
| Extremely Low | Obsidian + Git + Automation Scripts | Self-tracking Log |
| Low | Logseq + Fountain + Local Tools | Anonymous Online Community |
| Medium-Low | Hybrid Tools + Limited Collaboration | 1-on-1 Writing Partner |
| Medium | Standard Tool Combination | Small Writing Group |
| Medium-High | Collaboration Tools + Community Integration | Regular Sharing Sessions |
| High | Socially Integrated Tools | Writing Workshop |
| Extremely High | Real-time Collaboration + Community Platform | Public Progress Tracking |



Configure by Perfectionism Level

| Perfectionism | Pomodoro Settings | Draft Strategy | Iteration Count |
|---------------|-------------------|----------------|-----------------|
| Extremely High | 15/10 (forced stop) | Garbage Draft Method | Limit to 3 times |
| High | 20/5 | 80% Principle | Limit to 4 times |
| Medium-High | 25/5 | Rapid Iteration | 4-5 times |
| Medium | 25/5 | Standard Process | 3-4 times |
| Low | 30/5 | Free Process | 2-3 times |



Energy Mode Configuration

| Energy Mode | Daily Duration | Weekly Frequency | Target Pages/Week |
|-------------|----------------|------------------|-------------------|
| High Frequency High Intensity | 2 hours | 6-7 days | 12-15 pages |
| High Frequency Medium Intensity | 1 hour | 5-6 days | 8-10 pages |
| High Frequency Low Intensity | 30 minutes x2 | 5-6 days | 5-7 pages |
| Medium Frequency High Intensity | 2 hours | 3-4 days | 8-10 pages |
| Medium Frequency Medium Intensity | 1 hour | 3-4 days | 6-8 pages |
| Medium Frequency Low Intensity | 45 minutes | 3-4 days | 4-6 pages |
| Low Frequency High Intensity | 3-4 hours | 2 days | 8-10 pages |
| Low Frequency Medium Intensity | 2 hours | 2 days | 5-7 pages |
| Low Frequency Low Intensity | 1 hour | 2 days | 3-4 pages |
| Low Frequency Extreme Intensity | 4-6 hours | 1-2 days | 10-15 pages |



📋 Personalized Configuration Generator

Use the following Python script to generate personalized configurations based on the code:

'''python
profile_config_generator.py

import json

完整檔案數據（簡化示例）
PROFILES = {
    "QINTV": {
        "age": 23,
        "background": "大學生/文學系",
        "mbti": "INFP",
        "core_motivation": "自我療癒",
        "main_fear": "被批評",
        "writing_style": "詩意抒情",
        "best_time": "深夜",
        "energy_mode": "低頻高強",
        "social_need": "極低",
        "perfectionism": "高",
        "procrastination": "高",
        "self_doubt": "極高",
        "external_motivation": "低",
        "tools": ["Obsidian", "Fountain"],
        "pomodoro": "20/10",
        "weekly_pages": 5,
        "accountability": "匿名日記",
        "predicted_obstacle": "完美主義癱瘓",
        "strategy": "垃圾草稿法"
    },
    # ... 其他99個檔案
}

def generate_config(code):
    """根據代碼生成完整配置"""
    if code not in PROFILES:
        return {"error": f"代碼 {code} 不存在"}
    
    profile = PROFILES[code]
    
    config = {
        "writer_profile": profile,
        "chapter_65_config": {
            "stage_1": {
                "five_whys_depth": 7 if profile["social_need"] == "極低" else 5,
                "emotion_threshold": 8 if profile["self_doubt"] == "極高" else 6,
                "story_seeds_count": 5
            },
            "stage_2": {
                "empathy_map_depth": "深度" if profile["mbti"][0] == "I" else "廣度",
                "persona_count": 1 if profile["social_need"] == "極低" else 3,
                "validation_method": "書面問卷" if profile["social_need"] == "極低" else "訪談"
            },
            "stage_3": {
                "structure_complexity": "高" if profile["perfectionism"] == "極高" else "中",
                "constraints_count": "多" if profile["perfectionism"] in ["高", "極高"] else "少"
            },
            "stage_4": {
                "emotion_curve_complexity": "高" if profile["mbti"][0] == "I" else "中",
                "body_tracking": "深度" if profile["self_doubt"] == "極高" else "表面"
            },
            "stage_5": {
                "pomodoro_setting": profile["pomodoro"],
                "weekly_target": profile["weekly_pages"],
                "version_control": "詳細" if profile["perfectionism"] in ["高", "極高"] else "簡單"
            },
            "stage_6": {
                "feedback_source": "書面" if profile["social_need"] == "極低" else "面對面",
                "iteration_count": 5 if profile["perfectionism"] == "極高" else 3
            }
        },
        "workflow_config": {
            "tools": profile["tools"],
            "schedule": {
                "best_time": profile["best_time"],
                "energy_mode": profile["energy_mode"],
                "weekly_sessions": 2 if "低頻" in profile["energy_mode"] else 5
            },
            "support_system": {
                "accountability": profile["accountability"],
                "social_need": profile["social_need"]
            },
            "obstacle_prevention": {
                "predicted": profile["predicted_obstacle"],
                "strategy": profile["strategy"]
            }
        }
    }
    
    return config

def export_config(code, filename=None):
    """導出配置到 JSON 文件"""
    config = generate_config(code)
    if filename is None:
        filename = f"config_{code}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    
    return filename

使用示例
if __name__ == "__main__":
    # 生成 QINTV 的配置
    config = generate_config("QINTV")
    print(json.dumps(config, ensure_ascii=False, indent=2))
    
    # 導出到文件
    export_config("QINTV")
'''



📝 Usage Instructions

1. **Find your code**: Locate the profile in the table that best matches your age, professional background, and psychological traits
2. **View parameters**: Record all parameter values for that code
3. **Generate configuration**: Use the Python script to generate personalized configuration
4. **Apply to framework**: Apply the configuration to the six-stage framework in this chapter
5. **Execute workflow**: Follow the steps in Appendix A
6. **Adjust and optimize**: Adjust parameters based on actual experience



*This appendix contains 100 unique creator psychological profiles, covering four major categories: introverted creative type, extroverted social type, trauma experience type, and professional transition type, providing personalized parameter support for the scriptwriting framework.*







Document: `study/psychological_recommendation_agent_functional_specification.md`

_Embedded from `corpus/study/psychological_recommendation_agent_functional_specification.md`. Also stored at `sources/study/psychological_recommendation_agent_functional_specification.md` under this agent folder._




Psychology AI System for Movie Preference Prediction: Complete Guide (Expanded Edition)

I. Core Conceptual Framework



1.1 Why Are Psychological Factors Needed?
Traditional recommendation systems primarily rely on viewing history and collaborative filtering, but incorporating psychological analysis can:

- Explain "why" a certain movie is recommended, providing explainable recommendations to help users understand the recommendation logic.
- Predict potential preferences for unexposed genres, solving the cold start problem.
- Provide more personalized and accurate recommendations, adjusted based on users' intrinsic traits such as personality and emotional state.
- Enhance user engagement and satisfaction; studies show that integrating personality traits can improve recommendation accuracy by 5-10% (refer to the Personality and Recommender Systems paper).
- Address diversity needs, avoid the filter bubble, and ensure recommendations cover content at different emotional and cognitive levels.

Additionally, psychological factors can handle situational changes, such as users preferring light content when under stress rather than high-intensity plots.



1.2 Overall System Flow
'''
User data collection (viewing history, reviews, surveys) → Psychological feature extraction (personality prediction, sentiment analysis) → AI model training (integrating psychological features) → Preference prediction (multi-modal fusion) → Recommendation explanation and feedback loop
'''



1.3 New: Empirical Foundation of Psychology in Recommendation Systems
According to the paper list (Psychology-based RecSys GitHub), multiple studies confirm that integrating Big Five personality traits can improve recommendation performance. For example, one study showed that for users high in extraversion, the click-through rate for recommending movies with social themes increased by 15%. Additionally, emotion-based recommendation systems (such as those using the PAD model) reduced RMSE by 0.05-0.1 on the MovieLens dataset.



II. Classification of Psychological Factors



2.1 Basics: Big Five Personality Model
This is the most widely used personality framework, consisting of five dimensions (refer to the Personality and Recommender Systems paper):
**Extraversion**
- High scorers: Prefer social themes, romantic comedies, group interaction plots (e.g., Friends style).
- Low scorers: Prefer independent characters, introspective themes (e.g., art film Her).
- Integration method: Use personality prediction models to infer from user reviews.

**Agreeableness**
- High scorers: Like explorations of human nature, heartwarming family films, positive endings (e.g., Disney animations).
- Low scorers: Can accept moral gray areas, anti-hero characters (e.g., Joker).
- Research shows that high Agreeableness users have 20% higher satisfaction with positive content.

**Neuroticism**
- High scorers: May avoid horror, high-stress plots to prevent triggering anxiety.
- Low scorers: Can handle emotionally intense movies (e.g., thrillers).
- Application: Real-time emotion monitoring to avoid recommending high-intensity content.

**Openness**
- High scorers: Prefer art films, sci-fi, experimental movies (e.g., Inception).
- Low scorers: Prefer traditional narratives, commercial films (e.g., Marvel series).
- High Openness users are more receptive to new genre recommendations.

**Conscientiousness**
- High scorers: Like structurally complete, logically rigorous stories (e.g., detective films).
- Low scorers: Can accept open-ended endings, non-linear narratives (e.g., Pulp Fiction).

How to integrate using open-source frameworks: Use the yashsmehta/personality-prediction GitHub repo to predict Big Five scores from user text (e.g., reviews), then input as features into the recommendation model.



2.2 Advanced Factors
**Need for Cognition**
- **Definition**: The extent to which individuals prefer engaging in cognitive effort.
- **Influence**:
  - High Need for Cognition: Prefers complex plots, documentaries, art films (e.g., *Oppenheimer*).
  - Low Need for Cognition: Prefers light entertainment, easy-to-digest content, binge-watching (e.g., Netflix original comedies).
- **Measurement**: Need for Cognition Scale questionnaire or inferred from viewing patterns (e.g., viewing duration).
- **AI Application**: Predicts users' risk of continuous watching, recommends in-depth content. Uses Surprise library for expansion, integrates custom algorithms with cognition scores.

**Early Maladaptive Schemas**
- **Definition**: Negative belief patterns formed in childhood (e.g., abandonment, dependence, mistrust).
- **Influence**: Affects emotional regulation and preference for therapeutic content (e.g., recommending trauma-exploring films like *The Perks of Being a Wallflower*).
- **Measurement**: Young Schema Questionnaire or NLP analysis of reviews, using transformers library's BERT model.
- **AI Application**: Recommends plot-driven films exploring trauma and growth themes, avoids triggering negative patterns.

**Core Self-Evaluations**
- **Definition**: Includes self-esteem, self-efficacy, sense of control, emotional stability.
- **Influence**:
  - High evaluators: Can accept challenging content (e.g., adventure films).
  - Low evaluators: Prefers positive, inspirational movies (e.g., *The Pursuit of Happyness*).
- **Measurement**: Core Self-Evaluations Scale.
- **AI Application**: Avoids recommending content that may trigger negative emotions, uses emotion analysis pipeline for filtering.

**MOVIE Model**
- **Definition**: Movie-specific five-factor preference model
  - Melodrama
  - cOmic (Comedy)
  - Violent
  - Imaginative
  - Exciting
- **Advantages**: Directly corresponds to movie genres, supplements deficiencies of Big Five.
- **AI Application**: Serves as output layer to predict ratings for each genre, integrates into LightFM's feature matrix.

**Other Important Factors**
- **Gender**: Statistical preference differences (avoid stereotypes), e.g., women prefer romances more, but use data-driven approaches to avoid bias.
- **Cultural Background**: Influences acceptance of specific themes (e.g., Eastern cultures prefer collectivist themes), reference GCN-CF paper, use graph neural networks to integrate cultural features.
- **Current Emotional State**: May prefer escapist entertainment under stress, detected via facial recognition or text analysis.
- **Viewing Motivations**: Learning, escapism, social, emotional catharsis, inferred from questionnaires or behavioral data.
- **PAD Emotional Model**: PAD three-dimensional emotional model for user emotion modeling, includes Pleasure, Arousal, Dominance dimensions. From the paper "An intelligent film recommender system based on emotional analysis"[[2]]([historical-url] uses PSO for optimizing multimodal feature fusion to achieve emotion-matching recommendations. Open-source implementation: Use PySwarms for PSO, combined with NLTK for sentiment.

**Attachment Styles** - Secure types prefer stable relationship plots, insecure types may avoid romances. Measured via questionnaires, integrated into the feature layer of recommendation models.

III. Open-Source Frameworks and Tools Ecosystem



3.1 Core Framework for Recommendation Systems
**TensorFlow Recommenders (TFRS)**
TFRS is a library for building recommendation system models, supporting the entire recommendation system workflow: data preparation, model formulation, training, evaluation, and deployment[[1]]([historical-url] How to integrate custom user features like personality traits: Use Big Five scores as part of the user embedding.

'''python
import tensorflow as tf
import tensorflow_datasets as tfds
import tensorflow_recommenders as tfrs

Load MovieLens data
ratings = tfds.load("movielens/100k-ratings", split="train")
movies = tfds.load("movielens/100k-movies", split="train")

Define user model, integrate personality features (assuming extraversion etc. 5 dimensions)
class UserModel(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.user_embedding = tf.keras.Sequential([
            tf.keras.layers.StringLookup(vocabulary=unique_user_ids, mask_token=None),
            tf.keras.layers.Embedding(len(unique_user_ids) + 1, 32),
        ])
        self.personality_dense = tf.keras.layers.Dense(32, activation='relu')  # Process Big Five vector

    def call(self, inputs):
        user_emb = self.user_embedding(inputs["user_id"])
        personality_emb = self.personality_dense(inputs["personality_vector"])  # [batch, 5]
        return tf.concat([user_emb, personality_emb], axis=-1)

Movie model
class MovieModel(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.movie_embedding = tf.keras.Sequential([
            tf.keras.layers.StringLookup(vocabulary=unique_movie_titles, mask_token=None),
            tf.keras.layers.Embedding(len(unique_movie_titles) + 1, 32),
        ])

    def call(self, titles):
        return self.movie_embedding(titles)

Full model
class MovielensModel(tfrs.Model):
    def __init__(self):
        super().__init__()
        self.user_model = UserModel()
        self.movie_model = MovieModel()
        self.task = tfrs.tasks.Retrieval(
            metrics=tfrs.metrics.FactorizedTopK(
                candidates=movies.batch(128).map(self.movie_model)
            )
        )

    def compute_loss(self, features, training=False):
        user_embeddings = self.user_model(features)  # Includes personality
        movie_embeddings = self.movie_model(features["movie_title"])
        return self.task(user_embeddings, movie_embeddings)

Training
model = MovielensModel()
model.compile(optimizer=tf.keras.optimizers.Adagrad(0.1))
model.fit(ratings.batch(4096), epochs=3)
'''
This allows personality features to influence embeddings, improving personalization.

**LightFM - Hybrid Recommendation System**
LightFM is a Python implementation of a hybrid recommendation algorithm that integrates item and user metadata into traditional matrix factorization algorithms, enabling recommendations to generalize to new items (via item features) and new users (via user features)[[1]]([historical-url] Documentation shows that user/item features like psychological attributes can be added.

'''python
from lightfm import LightFM
from lightfm.data import Dataset
from scipy.sparse import csr_matrix

Create dataset
dataset = Dataset()
dataset.fit(users=user_ids, items=movie_ids, user_features=['extraversion_high', 'openness_low', 'pad_pleasure:0.5'], item_features=['genre:drama', 'emotional_intensity:0.7'])

Build interaction matrix
(interactions, weights) = dataset.build_interactions(user_movie_ratings)

User features: Integrate Big Five + PAD
user_features = dataset.build_user_features([
    (user, {'extraversion_high': 1 if score > 0.5 else 0, 'pad_pleasure': pleasure_score})
    for user, score, pleasure_score in user_data
])

Item features
item_features = dataset.build_item_features([
    (movie, {'genre:drama': 1, 'emotional_intensity': intensity})
    for movie, intensity in movie_data
])

Model
model = LightFM(loss='warp-kos', no_components=64, learning_rate=0.05)
model.fit(interactions, user_features=user_features, item_features=item_features, epochs=30, num_threads=8)

Prediction
scores = model.predict(user_id, np.arange(n_movies), user_features=user_features, item_features=item_features)
top_items = movie_ids[np.argsort(-scores)[:10]]
'''
This uses warp-kos loss to optimize implicit feedback, suitable for psychological features.

**Surprise - Collaborative Filtering Dedicated**
The Surprise library focuses on collaborative filtering and can be extended with custom algorithms to integrate psychological factors[[surprise.readthedocs.io]].

'''python
from surprise import SVD, Dataset, Reader
from surprise.model_selection import cross_validate
from surprise import AlgoBase
from surprise import PredictionImpossible

class PsychologySVD(AlgoBase):
    def __init__(self, n_factors=100, n_epochs=20, lr_all=0.005, reg_all=0.02):
        self.svd = SVD(n_factors, n_epochs, lr_all, reg_all)
        self.personality_dict = {}  # User personality dictionary

    def fit(self, trainset):
        AlgoBase.fit(self, trainset)
        self.svd.fit(trainset)
        # Assume pre-loaded personality
        self.personality_dict = load_personality_data()

    def estimate(self, u, i):
        try:
            base_pred = self.svd.estimate(u, i)
            if u in self.personality_dict:
                pers = self.personality_dict[u]
                # Adjust prediction based on openness
                adjustment = pers['openness'] * 0.1 if 'sci-fi' in item_genres[i] else 0
                return base_pred + adjustment
            return base_pred
        except:
            raise PredictionImpossible

Usage
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user_id', 'movie_id', 'rating']], reader)
algo = PsychologySVD()
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5)
'''



3.2 Psychology Analysis Tools

**Personality Prediction Framework**
Uses TensorFlow and PyTorch to explore automated personality detection based on language models, supporting the Essays dataset with Big Five personality trait labels[[2]]([historical-url]

'''python
使用預訓練BERT進行人格預測
from transformers import BertModel, BertTokenizer
import torch

class PersonalityPredictor(torch.nn.Module):
    def __init__(self, bert_model_name='bert-base-uncased'):
        super().__init__()
        self.bert = BertModel.from_pretrained(bert_model_name)
        self.dropout = torch.nn.Dropout(0.3)
        
        # Big Five各維度的預測頭
        self.extraversion_head = torch.nn.Linear(768, 1)
        self.agreeableness_head = torch.nn.Linear(768, 1)
        self.neuroticism_head = torch.nn.Linear(768, 1)
        self.openness_head = torch.nn.Linear(768, 1)
        self.conscientiousness_head = torch.nn.Linear(768, 1)
        
    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.pooler_output
        output = self.dropout(pooled_output)
        
        return {
            'extraversion': torch.sigmoid(self.extraversion_head(output)),
            'agreeableness': torch.sigmoid(self.agreeableness_head(output)),
            'neuroticism': torch.sigmoid(self.neuroticism_head(output)),
            'openness': torch.sigmoid(self.openness_head(output)),
            'conscientiousness': torch.sigmoid(self.conscientiousness_head(output))
        }
'''

'''python
from transformers import BertTokenizer, BertModel
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')  # 從repo載入fine-tuned模型

def predict_personality(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    # repo中添加分類頭
    logits = classification_head(outputs.pooler_output)
    return torch.sigmoid(logits)  # Big Five scores

應用：從用戶評論預測，輸入LightFM user_features
user_personality = predict_personality(user_reviews)
'''
**Emotion Analysis Integration**
Psychological research shows that people's preferences or emotional states are influenced by the emotions of the majority (herd mentality), making it particularly important to mine the emotions in user reviews[[2]]([historical-url]

'''python
from transformers import pipeline
import pandas as pd

使用預訓練情緒分析模型
emotion_analyzer = pipeline("emotion", model="j-hartmann/emotion-english-distilroberta-base")

def analyze_review_emotions(reviews):
    """分析電影評論的情緒分布"""
    emotions_list = []
    
    for review in reviews:
        result = emotion_analyzer(review[:512])  # BERT限制
        emotions_list.append(result[0])
    
    # 統計情緒分布
    emotion_df = pd.DataFrame(emotions_list)
    emotion_profile = emotion_df.groupby('label')['score'].mean()
    
    return emotion_profile

整合到推薦系統
def enhance_movie_profile_with_emotions(movie_id, reviews):
    emotion_profile = analyze_review_emotions(reviews)
    
    # 根據情緒分布調整電影屬性
    if emotion_profile.get('fear', 0) > 0.3:
        movie_attributes[movie_id]['suitable_for_high_neuroticism'] = False
    if emotion_profile.get('joy', 0) > 0.5:
        movie_attributes[movie_id]['positive_emotional_impact'] = True
        
    return movie_attributes[movie_id]
'''
Uses PSO optimization fusion (from paper)
'''python
from transformers import pipeline
from pyswarms.single.global_best import GlobalBestPSO
import numpy as np

emotion_analyzer = pipeline("sentiment-analysis")

def fuse_features(text_feat, image_feat, weights):
    return weights[0] * text_feat + weights[1] * image_feat  # 簡化

def objective(weights):
    fused = fuse_features(text_feats, image_feats, weights)
    pred_pad = map_to_pad(fused)
    loss = np.mean((pred_pad - true_pad)**2)
    return loss

PSO優化
bounds = [(0,1), (0,1)]
optimizer = GlobalBestPSO(n_particles=10, dimensions=2, bounds=bounds)
cost, pos = optimizer.optimize(objective, iters=20)
'''
Integrate into recommendations, adjust movie attributes.



3.3 Multi-Modal Deep Learning Architecture

Uses graph convolutional neural network (GCN) to build a collaborative filtering recommendation model, and integrates IoT and convolutional networks to optimize animated movie recommendations for cross-cultural dissemination[[3]]([historical-url] The paper emphasizes cultural psychological factors and uses a dynamic attention mechanism to adjust weights.

'''python
import tensorflow as tf
from tensorflow.keras import layers

class MultiModalMovieRecommender(tf.keras.Model):
    def __init__(self, num_users, num_movies, embedding_dim=128):
        super().__init__()
        
        # 用戶和電影嵌入
        self.user_embedding = layers.Embedding(num_users, embedding_dim)
        self.movie_embedding = layers.Embedding(num_movies, embedding_dim)
        
        # 心理特徵處理網路
        self.psychology_net = tf.keras.Sequential([
            layers.Dense(64, activation='relu'),
            layers.Dropout(0.3),
            layers.Dense(32, activation='relu')
        ])
        
        # 文本特徵處理（評論、劇情簡介）
        self.text_encoder = tf.keras.Sequential([
            layers.Conv1D(128, 3, activation='relu'),
            layers.GlobalMaxPooling1D(),
            layers.Dense(64, activation='relu')
        ])
        
        # 視覺特徵處理（海報、預告片幀）
        self.visual_encoder = tf.keras.Sequential([
            layers.Conv2D(32, 3, activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, activation='relu'),
            layers.GlobalAveragePooling2D(),
            layers.Dense(64, activation='relu')
        ])
        
        # 融合層
        self.fusion_layer = tf.keras.Sequential([
            layers.Dense(128, activation='relu'),
            layers.Dropout(0.4),
            layers.Dense(64, activation='relu'),
            layers.Dense(1, activation='sigmoid')  # 預測評分
        ])
        
    def call(self, inputs):
        user_id, movie_id, user_psych, movie_text, movie_visual = inputs
        
        # 獲取嵌入
        user_emb = self.user_embedding(user_id)
        movie_emb = self.movie_embedding(movie_id)
        
        # 處理各模態特徵
        psych_features = self.psychology_net(user_psych)
        text_features = self.text_encoder(movie_text)
        visual_features = self.visual_encoder(movie_visual)
        
        # 融合所有特徵
        combined = tf.concat([
            user_emb, 
            movie_emb, 
            psych_features, 
            text_features, 
            visual_features
        ], axis=-1)
        
        # 預測
        prediction = self.fusion_layer(combined)
        return prediction
'''

Simplified GCN integration with psychology
'''python
import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout

class GCNLayer(tf.keras.layers.Layer):
    def __init__(self, output_dim):
        super().__init__()
        self.dense = Dense(output_dim)

    def call(self, inputs, adj_matrix):
        support = tf.matmul(adj_matrix, inputs)
        output = self.dense(support)
        return tf.nn.relu(output)

class GCNRecommender(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.gcn1 = GCNLayer(64)
        self.gcn2 = GCNLayer(32)
        self.psych_dense = Dense(16)  # 心理特徵

    def call(self, graph_embeddings, psych_features, adj_matrix):
        x = self.gcn1(graph_embeddings, adj_matrix)
        x = self.gcn2(x, adj_matrix)
        psych = self.psych_dense(psych_features)  # Big Five or cultural
        return tf.concat([x, psych], axis=-1)

使用MovieLens圖結構，adj_matrix為用戶-電影連接
'''

IV. Complete System Implementation Example



4.1 Data Preprocessing Pipeline

'''python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from transformers import AutoTokenizer

class PsychologyAwareDataPipeline:
    def __init__(self):
        self.user_scaler = StandardScaler()
        self.movie_scaler = MinMaxScaler()
        self.tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
        
    def process_user_psychology_data(self, user_data):
        """Process user psychology data"""
        # Big Five standardization
        big_five_cols = ['extraversion', 'agreeableness', 'neuroticism', 
                         'openness', 'conscientiousness']
        user_data[big_five_cols] = self.user_scaler.fit_transform(user_data[big_five_cols])
        
        # Need for cognition score (1-10)
        user_data['need_cognition'] = user_data['need_cognition'] / 10.0
        
        # Current emotional state (PAD model)
        pad_cols = ['pleasure', 'arousal', 'dominance']
        user_data[pad_cols] = (user_data[pad_cols] + 1) / 2  # Normalize to 0-1
        
        return user_data
    
    def extract_movie_psychological_features(self, movie_data):
        """Extract psychology-related features from movie data"""
        features = {}
        
        # Emotional intensity analysis (based on plot synopsis)
        for idx, row in movie_data.iterrows():
            synopsis = row['synopsis']
            
            # Use BERT encoding
            inputs = self.tokenizer(synopsis, return_tensors="pt", 
                                   truncation=True, max_length=512)
            
            # Should connect to pre-trained emotional intensity model here
            # features[idx] = emotion_intensity_model(inputs)
            
            # Temporarily use rule-based method
            emotional_words = ['death', 'love', 'fear', 'joy', 'anger', 'surprise']
            intensity = sum(1 for word in emotional_words if word in synopsis.lower())
            features[idx] = {'emotional_intensity': intensity / len(emotional_words)}
            
        return pd.DataFrame.from_dict(features, orient='index')
    
    def create_interaction_features(self, user_psych, movie_features):
        """Create user psychology-movie feature interactions"""
        interactions = {}
        
        # Openness × Imagination
        interactions['openness_imagination'] = user_psych['openness'] * movie_features['imaginative_score']
        
        # Neuroticism × Emotional intensity (negative correlation)
        interactions['neuroticism_intensity'] = user_psych['neuroticism'] * (1 - movie_features['emotional_intensity'])
        
        # Need for cognition × Complexity
        interactions['cognition_complexity'] = user_psych['need_cognition'] * movie_features['complexity']
        
        # Current mood × Movie mood match
        mood_match = self.calculate_mood_movie_match(user_psych, movie_features)
        interactions['mood_match'] = mood_match
        
        return interactions
    
    def calculate_mood_movie_match(self, user_mood, movie_mood):
        """Calculate matching degree between user's current mood and movie mood"""
        # Use cosine similarity
        from sklearn.metrics.pairwise import cosine_similarity
        
        user_vector = np.array([user_mood['pleasure'], user_mood['arousal'], user_mood['dominance']])
        movie_vector = np.array([movie_mood['valence'], movie_mood['arousal'], movie_mood['dominance']])
        
        similarity = cosine_similarity(user_vector.reshape(1, -1), 
                                     movie_vector.reshape(1, -1))[0][0]
        return similarity
'''
Cultural feature processing, from GCN paper.
'''python
def process_cultural_data(user_data):
    cultural_dims = ['individualism', 'power_distance']  # Hofstede dimensions
    user_data[cultural_dims] = scaler.fit_transform(user_data[cultural_dims])
    return user_data
'''



4.2 Advanced Model Architecture

'''python
class PsychologyEnhancedRecommender:
    def __init__(self, config):
        self.config = config
        self.build_models()
        
    def build_models(self):
        """Build multiple specialized models"""
        # Basic collaborative filtering model
        self.cf_model = self._build_cf_model()
        
        # Psychology content model
        self.psych_model = self._build_psychology_model()
        
        # Context-aware model
        self.context_model = self._build_context_model()
        
        # Ensemble model
        self.ensemble_model = self._build_ensemble_model()
        
    def _build_psychology_model(self):
        """Psychology feature dedicated model"""
        inputs = {
            'user_big_five': tf.keras.Input(shape=(5,), name='big_five'),
            'user_cognition': tf.keras.Input(shape=(1,), name='cognition'),
            'user_schemas': tf.keras.Input(shape=(10,), name='schemas'),
            'movie_psychology': tf.keras.Input(shape=(15,), name='movie_psych')
        }
        
        # Big Five processing branch
        big_five_branch = layers.Dense(32, activation='relu')(inputs['user_big_five'])
        big_five_branch = layers.BatchNormalization()(big_five_branch)
        big_five_branch = layers.Dense(16, activation='relu')(big_five_branch)
        
        # Cognitive needs processing
        cognition_branch = layers.Dense(8, activation='relu')(inputs['user_cognition'])
        
        # Early schema processing
        schema_branch = layers.Dense(16, activation='relu')(inputs['user_schemas'])
        schema_branch = layers.Dropout(0.3)(schema_branch)
        
        # Movie psychology feature processing
        movie_branch = layers.Dense(32, activation='relu')(inputs['movie_psychology'])
        movie_branch = layers.Dense(16, activation='relu')(movie_branch)
        
        # Feature fusion
        concat = layers.Concatenate()([big_five_branch, cognition_branch, 
                                      schema_branch, movie_branch])
        
        # Attention mechanism
        attention = layers.MultiHeadAttention(num_heads=4, key_dim=16)(concat, concat)
        
        # Final prediction
        x = layers.Dense(64, activation='relu')(attention)
        x = layers.Dropout(0.4)(x)
        x = layers.Dense(32, activation='relu')(x)
        output = layers.Dense(1, activation='sigmoid', name='rating_prediction')(x)
        
        model = tf.keras.Model(inputs=inputs, outputs=output)
        return model
    
    def _build_context_model(self):
        """Context-aware model"""
        inputs = {
            'time_of_day': tf.keras.Input(shape=(24,), name='time'),  # one-hot
            'day_of_week': tf.keras.Input(shape=(7,), name='day'),    # one-hot
            'season': tf.keras.Input(shape=(4,), name='season'),      # one-hot
            'user_stress': tf.keras.Input(shape=(1,), name='stress'),
            'social_context': tf.keras.Input(shape=(3,), name='social') # alone/couple/group
        }
        
        # Time feature processing
        temporal = layers.Concatenate()([inputs['time_of_day'], 
                                        inputs['day_of_week'], 
                                        inputs['season']])
        temporal = layers.Dense(16, activation='relu')(temporal)
        
        # Stress and social context
        context = layers.Concatenate()([inputs['user_stress'], 
                                       inputs['social_context']])
        context = layers.Dense(8, activation='relu')(context)
        
        # Fusion
        combined = layers.Concatenate()([temporal, context])
        x = layers.Dense(32, activation='relu')(combined)
        x = layers.Dense(16, activation='relu')(x)
        
        # Output context adjustment weight
        context_weight = layers.Dense(1, activation='sigmoid', 
                                     name='context_weight')(x)
        
        model = tf.keras.Model(inputs=inputs, outputs=context_weight)
        return model
'''
Attention mechanism, from the paper.
'''python
Add in _build_psychology_model
attention = tf.keras.layers.Attention()([concat, concat])  # self-attention
'''



4.3 Real-time Recommendation Service

'''python
import redis
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, db=0)

class UserRequest(BaseModel):
    user_id: str
    current_mood: dict  # PAD emotion state
    context: dict       # Viewing context
    
class MovieRecommendation(BaseModel):
    movie_id: str
    title: str
    predicted_rating: float
    psychological_match: float
    recommendation_reason: str
    warnings: list

class RecommendationService:
    def __init__(self):
        self.load_models()
        self.cache_ttl = 3600  # 1 hour cache
        
    async def get_recommendations(self, user_request: UserRequest) -> list[MovieRecommendation]:
        # Check cache
        cache_key = f"rec:{user_request.user_id}:{hash(str(user_request.dict()))}"
        cached = redis_client.get(cache_key)
        if cached:
            return json.loads(cached)
        
        # Get user psychological profile
        user_profile = await self.get_user_psychology_profile(user_request.user_id)
        
        # Get candidate movies
        candidate_movies = await self.get_candidate_movies(user_request.user_id)
        
        # Parallel prediction
        tasks = []
        for movie in candidate_movies:
            task = self.predict_preference(user_profile, movie, user_request)
            tasks.append(task)
            
        predictions = await asyncio.gather(*tasks)
        
        # Ranking and filtering
        recommendations = self.rank_and_filter(predictions, user_profile)
        
        # Generate explanations
        for rec in recommendations:
            rec.recommendation_reason = await self.generate_explanation(
                user_profile, rec, user_request
            )
            rec.warnings = self.check_content_warnings(user_profile, rec)
        
        # Cache results
        redis_client.setex(cache_key, self.cache_ttl, json.dumps([r.dict() for r in recommendations]))
        
        return recommendations
    
    async def predict_preference(self, user_profile, movie, context):
        """Predict user's preference for the movie"""
        # Prepare features
        features = self.prepare_features(user_profile, movie, context)
        
        # Multi-model prediction
        psych_score = self.psych_model.predict(features['psychology'])
        cf_score = self.cf_model.predict(features['collaborative'])
        context_weight = self.context_model.predict(features['context'])
        
        # Weighted combination
        final_score = (
            0.4 * psych_score + 
            0.4 * cf_score + 
            0.2 * context_weight * (psych_score + cf_score) / 2
        )
        
        return MovieRecommendation(
            movie_id=movie['id'],
            title=movie['title'],
            predicted_rating=final_score,
            psychological_match=psych_score,
            recommendation_reason="",
            warnings=[]
        )
    
    def check_content_warnings(self, user_profile, movie):
        """Check content warnings"""
        warnings = []
        
        # Content warnings for high neuroticism users
        if user_profile['neuroticism'] > 0.7:
            if movie.get('horror_score', 0) > 0.5:
                warnings.append("Contains horror elements, may cause discomfort")
            if movie.get('violence_score', 0) > 0.6:
                warnings.append("Contains violence scenes")
                
        # Trauma-related warnings
        if user_profile.get('trauma_sensitivity', False):
            trauma_triggers = self.scan_trauma_triggers(movie)
            warnings.extend(trauma_triggers)
            
        return warnings
    
    async def generate_explanation(self, user_profile, recommendation, context):
        """Use LLM to generate personalized recommendation reasons"""
        prompt = f"""
        Generate recommendation reasons based on the following information:
        
        User psychological characteristics:
        - Openness: {user_profile['openness']}/5
        - Need for cognition: {user_profile['need_cognition']}/10
        - Current mood: Pleasure {context.current_mood['pleasure']}, Arousal {context.current_mood['arousal']}
        
        Movie characteristics:
        - Title: {recommendation.title}
        - Psychological match: {recommendation.psychological_match:.2f}
        - Genre tags: {recommendation.get('genres', [])}
        
        Generate a concise, personalized recommendation reason.
        """
        
        # Should call actual LLM API here
        # response = await llm_client.generate(prompt)
        
        # Example response
        if recommendation.psychological_match > 0.8:
            return f"This movie's {recommendation.get('key_feature', 'deep plot')} is particularly suitable for your current psychological state and cognitive preferences"
        else:
            return f"Based on your viewing history, this {recommendation.get('genre', 'drama')} might bring fresh experience"

@app.post("/recommendations")
async def get_recommendations(user_request: UserRequest):
    try:
        service = RecommendationService()
        recommendations = await service.get_recommendations(user_request)
        return {"status": "success", "recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
'''

Integrate BCI or IoT, but keep open source, use redis for cache.



4.4 Evaluation and Optimization

'''python
class PsychologyAwareEvaluator:
    def __init__(self):
        self.metrics = {}
        
    def evaluate_psychological_accuracy(self, predictions, actual_ratings, user_profiles):
        """Evaluate psychological prediction accuracy"""
        # Group evaluation by user psychological features
        results = {}
        
        # Group by openness
        for openness_level in ['low', 'medium', 'high']:
            mask = self._get_openness_mask(user_profiles, openness_level)
            group_predictions = predictions[mask]
            group_actual = actual_ratings[mask]
            
            results[f'rmse_openness_{openness_level}'] = np.sqrt(
                mean_squared_error(group_actual, group_predictions)
            )
            
        # Group by cognitive demand
        for cognition_level in ['low', 'high']:
            mask = self._get_cognition_mask(user_profiles, cognition_level)
            results[f'rmse_cognition_{cognition_level}'] = np.sqrt(
                mean_squared_error(actual_ratings[mask], predictions[mask])
            )
            
        return results
    
    def evaluate_diversity(self, recommendations, user_profiles):
        """Evaluate recommendation diversity"""
        diversity_scores = {}
        
        for user_id, recs in recommendations.items():
            # Genre diversity
            genres = [movie['genre'] for movie in recs]
            genre_diversity = len(set(genres)) / len(genres)
            
            # Emotion diversity
            emotions = [movie['primary_emotion'] for movie in recs]
            emotion_diversity = len(set(emotions)) / len(emotions)
            
            # Cognitive complexity diversity
            complexities = [movie['complexity'] for movie in recs]
            complexity_std = np.std(complexities)
            
            diversity_scores[user_id] = {
                'genre_diversity': genre_diversity,
                'emotion_diversity': emotion_diversity,
                'complexity_variance': complexity_std
            }
            
        return diversity_scores
    
    def psychological_ablation_study(self, model, test_data):
        """Psychological feature ablation study"""
        baseline = model.evaluate(test_data)
        
        ablation_results = {}
        psychological_features = ['big_five', 'cognition_need', 'emotion_state', 'schemas']
        
        for feature in psychological_features:
            # Remove specific psychological feature
            modified_data = self._remove_feature(test_data, feature)
            result = model.evaluate(modified_data)
            
            # Calculate performance drop
            performance_drop = (baseline['rmse'] - result['rmse']) / baseline['rmse']
            ablation_results[feature] = {
                'performance_drop': performance_drop,
                'feature_importance': abs(performance_drop)
            }
            
        return ablation_results
'''
Fairness evaluation, moved forward from FairnessAware section.



V. Advanced Optimization and Innovation Directions



5.1 Neuroscience Integration

'''python
class NeuroscienceEnhancedRecommender:
    def __init__(self):
        self.eeg_processor = self._init_eeg_processor()
        self.eye_tracker = self._init_eye_tracker()
        
    def process_neurophysiological_data(self, eeg_data, eye_tracking_data):
        """Process neurophysiological data"""
        # EEG band analysis
        brain_states = {
            'alpha': self._extract_alpha_power(eeg_data),  # Relaxation state
            'beta': self._extract_beta_power(eeg_data),    # Focus state
            'theta': self._extract_theta_power(eeg_data),  # Creativity state
            'gamma': self._extract_gamma_power(eeg_data)   # Cognitive processing
        }
        
        # Eye movement pattern analysis
        attention_patterns = {
            'fixation_duration': np.mean(eye_tracking_data['fixations']),
            'saccade_frequency': len(eye_tracking_data['saccades']) / eye_tracking_data['duration'],
            'pupil_dilation': np.mean(eye_tracking_data['pupil_size'])
        }
        
        # Integrate into viewing state vector
        viewing_state = self._combine_neuro_features(brain_states, attention_patterns)
        return viewing_state
    
    def real_time_preference_adjustment(self, movie_id, neuro_feedback):
        """Adjust recommendations based on real-time neuro feedback"""
        if neuro_feedback['engagement'] < 0.3:
            # Low engagement, recommend more stimulating content
            return self._get_more_engaging_alternatives(movie_id)
        elif neuro_feedback['stress'] > 0.7:
            # High stress, recommend relaxing content
            return self._get_relaxing_alternatives(movie_id)
        else:
            # Maintain current genre
            return self._get_similar_movies(movie_id)
'''
Uses OpenBCI open-source hardware to simulate EEG processing.



5.2 Cross-Cultural Adaptation System

The psychological and emotional experiences of audiences from different cultural backgrounds have a significant impact on film dissemination. Within the framework of cross-cultural communication theory, it emphasizes elucidating the information transmission and meaning construction processes between different cultures[[3]]([historical-url]

'''python
class CrossCulturalRecommender:
    def __init__(self):
        self.cultural_models = self._load_cultural_models()
        
    def adapt_recommendations_to_culture(self, base_recommendations, user_culture):
        """Adjust recommendations based on cultural background"""
        cultural_profile = self.cultural_models[user_culture]
        
        adapted_recommendations = []
        for movie in base_recommendations:
            # Cultural fit score
            cultural_fit = self._calculate_cultural_fit(movie, cultural_profile)
            
            # Adjust recommendation score
            adjusted_score = movie['base_score'] * cultural_fit
            
            # Cultural sensitivity check
            if self._check_cultural_sensitivity(movie, user_culture):
                movie['warnings'].append(f"May contain content sensitive to {user_culture} culture")
            
            movie['adjusted_score'] = adjusted_score
            adapted_recommendations.append(movie)
            
        return sorted(adapted_recommendations, key=lambda x: x['adjusted_score'], reverse=True)
    
    def _calculate_cultural_fit(self, movie, cultural_profile):
        """Calculate the fit between movie and culture"""
        fit_scores = {
            'individualism_collectivism': self._match_cultural_dimension(
                movie['cultural_values']['individualism'], 
                cultural_profile['individualism']
            ),
            'power_distance': self._match_cultural_dimension(
                movie['cultural_values']['power_distance'],
                cultural_profile['power_distance']
            ),
            'uncertainty_avoidance': self._match_cultural_dimension(
                movie['cultural_values']['uncertainty_avoidance'],
                cultural_profile['uncertainty_avoidance']
            )
        }
        
        # Weighted average
        return np.average(list(fit_scores.values()), 
                         weights=[0.4, 0.3, 0.3])
'''
From GCN paper, add Hofstede cultural dimension calculation.
'''python
def _match_cultural_dimension(movie_val, user_val):
    return 1 - abs(movie_val - user_val) / max_val
'''



5.3 Real-Time Emotion Adaptive Recommendation

The system uses facial expressions and text analysis to detect user emotions. It employs the ResNet50 model for facial expression recognition, achieving 73% accuracy[[9]]([historical-url]

'''python
class EmotionAdaptiveRecommender:
    def __init__(self):
        self.emotion_detector = self._load_emotion_models()
        self.mood_movie_mapper = self._init_mood_mapper()
        
    async def get_emotion_aware_recommendations(self, user_id, webcam_stream=None, text_input=None):
        # Multi-modal emotion recognition
        emotions = {}
        
        if webcam_stream:
            # Facial expression analysis
            face_emotion = await self._detect_face_emotion(webcam_stream)
            emotions['face'] = face_emotion
            
        if text_input:
            # Text emotion analysis
            text_emotion = await self._analyze_text_emotion(text_input)
            emotions['text'] = text_emotion
            
        # Fuse multi-modal emotions
        combined_emotion = self._fuse_emotions(emotions)
        
        # Adjust recommendations based on emotional state
        if combined_emotion['valence'] < 0.3:  # Negative emotion
            # Recommend healing movies
            recommendations = await self._get_uplifting_movies(user_id)
        elif combined_emotion['arousal'] > 0.7:  # High arousal state
            # Recommend relaxing movies
            recommendations = await self._get_calming_movies(user_id)
        else:
            # Standard recommendations
            recommendations = await self._get_standard_recommendations(user_id)
            
        # Add emotion transition paths
        for rec in recommendations:
            rec['emotion_journey'] = self._predict_emotion_journey(
                combined_emotion, rec['movie_emotion_profile']
            )
            
        return recommendations
    
    def _predict_emotion_journey(self, current_emotion, movie_emotion):
        """Predict emotional change path during viewing process"""
        journey = {
            'start': current_emotion,
            'during': self._interpolate_emotions(current_emotion, movie_emotion),
            'end': self._predict_post_viewing_emotion(current_emotion, movie_emotion),
            'therapeutic_value': self._calculate_therapeutic_value(current_emotion, movie_emotion)
        }
        return journey
'''

From emotion research papers, add CRF for AST.
Use the pycrfsuite open-source library to implement emotion transition matrices.

6. Deployment and Production Environment Best Practices



6.1 Microservices Architecture

'''yaml
docker-compose.yml
version: '3.8'

services:
  # Psychology Service
  psychology-service:
    build: ./services/psychology
    environment:
      - MODEL_PATH=/models/personality_predictor
      - CACHE_TTL=3600
    volumes:
      - ./models:/models
    ports:
      - "8001:8000"
  
  # Recommendation Engine Service
  recommendation-engine:
    build: ./services/recommender
    depends_on:
      - redis
      - postgres
    environment:
      - DATABASE_URL=postgresql://user:pass@postgres:5432/movies
      - REDIS_URL=redis://redis:6379
    ports:
      - "8002:8000"
  
  # Emotion Analysis Service
  emotion-analyzer:
    build: ./services/emotion
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
    ports:
      - "8003:8000"
  
  # API Gateway
  api-gateway:
    build: ./services/gateway
    depends_on:
      - psychology-service
      - recommendation-engine
      - emotion-analyzer
    ports:
      - "80:80"
  
  # Data Storage
  postgres:
    image: postgres:14
    environment:
      - POSTGRES_DB=movies
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
    volumes:
      - postgres_data:/var/lib/postgresql/data
  
  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
'''



6.2 Monitoring and Observability

'''python
from prometheus_client import Counter, Histogram, Gauge
import logging
from opentelemetry import trace

Prometheus metrics
recommendation_requests = Counter('recommendation_requests_total', 
                                 'Total recommendation requests',
                                 ['user_type', 'context'])
                                 
prediction_latency = Histogram('prediction_latency_seconds',
                              'Prediction latency',
                              ['model_type'])
                              
psychological_match_score = Gauge('psychological_match_score',
                                 'Average psychological match score',
                                 ['personality_type'])

class ObservableRecommender:
    def __init__(self):
        self.tracer = trace.get_tracer(__name__)
        self.logger = logging.getLogger(__name__)
        
    @prediction_latency.time()
    async def predict_with_monitoring(self, user_id, movie_id):
        with self.tracer.start_as_current_span("predict_preference") as span:
            span.set_attribute("user_id", user_id)
            span.set_attribute("movie_id", movie_id)
            
            try:
                # Fetch user psychological profile
                with self.tracer.start_as_current_span("fetch_user_profile"):
                    user_profile = await self.get_user_profile(user_id)
                    span.set_attribute("personality_type", 
                                      self._classify_personality(user_profile))
                
                # Predict
                prediction = await self.model.predict(user_profile, movie_id)
                
                # Update metrics
                psychological_match_score.labels(
                    personality_type=self._classify_personality(user_profile)
                ).set(prediction['psych_match'])
                
                return prediction
                
            except Exception as e:
                self.logger.error(f"Prediction failed: {e}", exc_info=True)
                span.record_exception(e)
                raise
'''



6.3 A/B Testing Framework

'''python
class PsychologyAwareABTester:
    def __init__(self):
        self.experiments = {}
        
    def create_experiment(self, name, hypothesis):
        """Create a psychology-oriented A/B test"""
        experiment = {
            'name': name,
            'hypothesis': hypothesis,
            'variants': {
                'control': {'description': '傳統協同過濾'},
                'treatment_a': {'description': '加入Big Five人格'},
                'treatment_b': {'description': '加入Big Five + 情緒狀態'}
            },
            'metrics': {
                'primary': ['click_through_rate', 'watch_completion_rate'],
                'secondary': ['user_satisfaction', 'recommendation_diversity'],
                'psychological': ['personality_match_accuracy', 'emotional_impact']
            },
            'segmentation': {
                'by_personality': ['high_openness', 'low_openness', 'high_neuroticism'],
                'by_cognition': ['high_need_cognition', 'low_need_cognition']
            }
        }
        
        self.experiments[name] = experiment
        return experiment
    
    def assign_variant(self, user_id, experiment_name):
        """Assign experiment group based on user characteristics"""
        experiment = self.experiments[experiment_name]
        
        # 獲取用戶心理特徵
        user_psych = self.get_user_psychology(user_id)
        
        # 確保每個心理類型都有足夠的樣本
        if self._needs_more_samples(experiment, user_psych):
            return self._assign_to_needed_variant(experiment, user_psych)
        else:
            # 隨機分配
            return random.choice(list(experiment['variants'].keys()))
    
    def analyze_results(self, experiment_name):
        """Analyze experiment results, with special focus on psychological dimensions"""
        results = self.fetch_experiment_data(experiment_name)
        
        analysis = {
            'overall': self._calculate_overall_metrics(results),
            'by_personality': {},
            'psychological_insights': {}
        }
        
        # 按人格類型分析
        for personality_type in ['high_openness', 'low_openness', 'high_neuroticism']:
            subset = results[results['personality_type'] == personality_type]
            analysis['by_personality'][personality_type] = {
                'ctr_lift': self._calculate_lift(subset, 'click_through_rate'),
                'satisfaction_lift': self._calculate_lift(subset, 'satisfaction'),
                'sample_size': len(subset)
            }
        
        # 心理學洞察
        analysis['psychological_insights'] = {
            'personality_treatment_interaction': self._test_interaction_effects(results),
            'optimal_model_by_personality': self._find_optimal_models(results),
            'unexpected_findings': self._detect_anomalies(results)
        }
        
        return analysis
'''

7. Case Studies and Best Practices



7.1 Netflix-Style Psychology Recommendation System

'''python
class NetflixStylePsychologyRecommender:
    def __init__(self):
        self.row_generators = {
            'personality_match': self._generate_personality_rows,
            'mood_based': self._generate_mood_rows,
            'cognitive_challenge': self._generate_cognitive_rows,
            'emotional_journey': self._generate_emotional_rows
        }
        
    def generate_homepage(self, user_id):
        """Generate personalized homepage recommendation rows"""
        user_profile = self.get_user_profile(user_id)
        rows = []
        
        # First row: Precise recommendations based on personality traits
        if user_profile['openness'] > 0.7:
            rows.append({
                'title': 'Prepared for Your Exploratory Spirit',
                'movies': self._get_innovative_movies(),
                'reason': 'personality_match'
            })
        
        # Second row: Recommendations based on current emotional state
        current_mood = self.get_current_mood(user_id)
        if current_mood['stress_level'] > 0.6:
            rows.append({
                'title': 'Choices to Relax Your Mood',
                'movies': self._get_stress_relief_movies(),
                'reason': 'mood_based'
            })
        
        # Third row: Cognitive challenge recommendations
        if user_profile['need_cognition'] > 7:
            rows.append({
                'title': 'Mind-Bending Masterpieces',
                'movies': self._get_complex_movies(),
                'reason': 'cognitive_challenge'
            })
        
        # Dynamically generate other rows
        for generator_name, generator_func in self.row_generators.items():
            if len(rows) < 10:  # Maximum 10 rows
                new_row = generator_func(user_profile)
                if new_row and self._is_relevant(new_row, user_profile):
                    rows.append(new_row)
        
        return rows
    
    def _generate_personality_rows(self, user_profile):
        """Generate recommendation rows based on personality traits"""
        personality_rows = []
        
        # Extraversion-related
        if user_profile['extraversion'] > 0.6:
            personality_rows.append({
                'title': 'Lively Party Movies',
                'query': 'high_social_interaction AND party_scenes',
                'explanation': 'Matches your extraverted personality'
            })
        else:
            personality_rows.append({
                'title': 'Great Films for Alone Time',
                'query': 'solitary_protagonist AND introspective',
                'explanation': 'Suitable for quiet viewing'
            })
        
        # Neuroticism-related content filtering
        if user_profile['neuroticism'] < 0.3:
            personality_rows.append({
                'title': 'Psychological Thriller Masterpieces',
                'query': 'psychological_thriller AND high_tension',
                'explanation': 'You can handle high-intensity emotions'
            })
        
        return personality_rows
'''



7.2 Real Case: Spotify-Style Emotional Radio

'''python
class EmotionRadioRecommender:
    def __init__(self):
        self.emotion_profiles = self._load_emotion_profiles()
        self.transition_models = self._load_transition_models()
        
    def create_emotional_journey_playlist(self, user_id, target_emotion=None):
        """Create emotional journey playlist"""
        current_emotion = self.get_user_emotion(user_id)
        
        if not target_emotion:
            # Automatically determine target emotion (e.g., from stress to relaxation)
            target_emotion = self._suggest_target_emotion(current_emotion)
        
        # Plan emotional transition path
        emotion_path = self._plan_emotion_transition(current_emotion, target_emotion)
        
        # Select movies for each stage
        playlist = []
        for i, emotion_state in enumerate(emotion_path):
            movies = self._select_movies_for_emotion(
                emotion_state, 
                transition_phase=i/len(emotion_path)
            )
            playlist.extend(movies)
        
        return {
            'name': f"Journey from {current_emotion['label']} to {target_emotion['label']}",
            'movies': playlist,
            'emotion_trajectory': emotion_path,
            'estimated_duration': sum(m['duration'] for m in playlist),
            'therapeutic_value': self._calculate_therapeutic_value(emotion_path)
        }
    
    def _plan_emotion_transition(self, start, end):
        """Plan smooth emotional transition path"""
        # Use reinforcement learning to find optimal path
        path = [start]
        current = start
        
        while self._emotion_distance(current, end) > 0.1:
            # Find next optimal emotional state
            next_emotion = self._find_next_emotion_state(current, end)
            path.append(next_emotion)
            current = next_emotion
            
        path.append(end)
        return path
'''
Movie recommendation based on RAG, from Medium article, using LangChain open source.
'''python
from langchain import LLMChain
Build RAG for personality-aware query
'''

VIII. Research Frontiers and Future Directions



8.1 Applications of Quantum Computing in Recommendation Systems

'''python
Conceptual example - Quantum recommendation system
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import TwoLocal

class QuantumRecommender:
    def __init__(self, n_users, n_items):
        self.n_users = n_users
        self.n_items = n_items
        self.n_qubits = int(np.ceil(np.log2(max(n_users, n_items))))
        
    def create_quantum_circuit(self):
        """Create quantum recommendation circuit"""
        qr = QuantumRegister(self.n_qubits, 'q')
        cr = ClassicalRegister(self.n_qubits, 'c')
        qc = QuantumCircuit(qr, cr)
        
        # Encode user psychological state
        qc.h(qr[0])  # Superposition state represents diverse preferences
        
        # Quantum feature mapping
        feature_map = TwoLocal(
            num_qubits=self.n_qubits,
            rotation_blocks=['ry', 'rz'],
            entanglement_blocks='cz',
            entanglement='full',
            reps=2
        )
        
        qc.append(feature_map, qr)
        
        # Measurement
        qc.measure(qr, cr)
        
        return qc
    
    def quantum_similarity(self, user_state, item_state):
        """Calculate similarity using quantum states"""
        # This is conceptual code; actual implementation requires more complex quantum algorithms
        pass
'''



8.2 Brain-Computer Interface (BCI) Integration

'''python
class BCIMovieRecommender:
    def __init__(self):
        self.bci_device = self._init_bci()
        self.signal_processor = self._init_signal_processor()
        
    def capture_brain_response(self, movie_trailer):
        """Capture brain response while watching the trailer"""
        # Start recording EEG
        self.bci_device.start_recording()
        
        # Play trailer
        play_trailer(movie_trailer)
        
        # Stop recording
        eeg_data = self.bci_device.stop_recording()
        
        # Analyze brain response
        brain_response = {
            'engagement': self._calculate_engagement(eeg_data),
            'emotional_valence': self._calculate_valence(eeg_data),
            'cognitive_load': self._calculate_cognitive_load(eeg_data),
            'interest_peaks': self._detect_interest_peaks(eeg_data)
        }
        
        return brain_response
    
    def predict_movie_enjoyment(self, brain_response):
        """Predict movie enjoyment based on brain response"""
        features = np.array([
            brain_response['engagement'],
            brain_response['emotional_valence'],
            brain_response['cognitive_load'],
            len(brain_response['interest_peaks'])
        ])
        
        # Use pre-trained neural network to predict
        enjoyment_score = self.enjoyment_model.predict(features.reshape(1, -1))[0]
        
        return enjoyment_score
'''



8.3 Recommendation Systems in the Metaverse

'''python
class MetaverseRecommender:
    def __init__(self):
        self.vr_tracker = self._init_vr_tracking()
        self.social_graph = self._init_social_graph()
        
    def recommend_vr_movie_experience(self, user_id, social_context):
        """Recommend VR movie experience"""
        # Get user's behavior in virtual space
        vr_behavior = self.get_vr_behavior_profile(user_id)
        
        # Analyze social viewing preferences
        social_preferences = self.analyze_social_viewing(user_id, social_context)
        
        recommendations = []
        
        # Solo immersive experience
        if social_context['alone']:
            recommendations.extend(self._get_immersive_solo_experiences(
                vr_behavior, user_psychology
            ))
        
        # Multiplayer interactive experience
        else:
            recommendations.extend(self._get_social_vr_experiences(
                social_preferences, social_context['friends']
            ))
        
        # Customize based on avatar
        avatar_preferences = self.get_avatar_preferences(user_id)
        recommendations = self._customize_for_avatar(recommendations, avatar_preferences)
        
        return recommendations
    
    def track_vr_engagement(self, user_id, movie_id):
        """Track VR movie engagement"""
        engagement_data = {
            'head_movement': self.vr_tracker.get_head_tracking(),
            'gaze_points': self.vr_tracker.get_gaze_tracking(),
            'hand_interactions': self.vr_tracker.get_hand_tracking(),
            'physiological': {
                'heart_rate': self.vr_tracker.get_heart_rate(),
                'skin_conductance': self.vr_tracker.get_skin_conductance()
            }
        }
        
        # Real-time adjustment of VR experience
        if engagement_data['physiological']['heart_rate'] > 120:
            self.adjust_vr_intensity(movie_id, 'decrease')
            
        return engagement_data
'''
LLM-enhanced personality simulator, from arxiv paper.

Nine, Ethical Considerations and Responsible AI



9.1 Bias Detection and Mitigation

'''python
class FairnessAwareRecommender:
    def __init__(self):
        self.bias_detector = BiasDetector()
        self.fairness_constraints = self._load_fairness_constraints()
        
    def detect_psychological_biases(self, model, test_data):
        """Detect psychology-related biases"""
        biases = {}
        
        # Personality type bias
        personality_bias = self.bias_detector.check_personality_bias(
            model, test_data
        )
        if personality_bias['significant']:
            biases['personality'] = {
                'type': 'systematic',
                'affected_groups': personality_bias['affected_groups'],
                'magnitude': personality_bias['effect_size']
            }
        
        # Emotional state bias
        emotion_bias = self.bias_detector.check_emotion_bias(
            model, test_data
        )
        
        # Cognitive ability bias
        cognitive_bias = self.bias_detector.check_cognitive_bias(
            model, test_data
        )
        
        return biases
    
    def apply_fairness_constraints(self, recommendations, user_profile):
        """Apply fairness constraints"""
        # Ensure recommendation diversity
        if self._is_filter_bubble_risk(recommendations, user_profile):
            # Inject diversity
            diverse_items = self._get_diversity_injection(user_profile)
            recommendations = self._merge_with_diversity(
                recommendations, diverse_items, ratio=0.2
            )
        
        # Avoid reinforcing stereotypes
        if self._detects_stereotype_reinforcement(recommendations, user_profile):
            recommendations = self._counter_stereotypes(recommendations, user_profile)
        
        return recommendations
    
    def generate_fairness_report(self):
        """Generate fairness report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'metrics': {
                'demographic_parity': self._calculate_demographic_parity(),
                'equal_opportunity': self._calculate_equal_opportunity(),
                'individual_fairness': self._calculate_individual_fairness()
            },
            'recommendations': self._generate_improvement_recommendations()
        }
        
        return report
'''



9.2 Explainability Framework

'''python
class ExplainableRecommender:
    def __init__(self):
        self.explainer = ModelExplainer()
        
    def generate_layered_explanation(self, user_id, movie_id, prediction):
        """Generate multi-layered explanation"""
        explanation = {
            'simple': self._generate_simple_explanation(user_id, movie_id),
            'detailed': self._generate_detailed_explanation(user_id, movie_id, prediction),
            'technical': self._generate_technical_explanation(user_id, movie_id, prediction)
        }
        
        # Simple explanation (for general users)
        explanation['simple'] = f"""
        I recommend "{movie_title}" because:
        1. It matches your {personality_trait} personality traits
        2. It suits your current {emotion_state} mood
        3. You previously liked similar {similar_feature}
        """
        
        # Detailed explanation (for curious users)
        explanation['detailed'] = self._create_detailed_narrative(
            user_psychology, movie_features, interaction_history
        )
        
        # Technical explanation (for researchers/developers)
        explanation['technical'] = {
            'feature_contributions': self._calculate_shap_values(user_id, movie_id),
            'model_confidence': prediction['confidence'],
            'similar_users_evidence': self._get_similar_users_evidence(user_id, movie_id),
            'psychological_alignment': self._get_psychological_alignment_scores(user_id, movie_id)
        }
        
        return explanation
    
    def visualize_recommendation_logic(self, user_id, recommendations):
        """Visualize recommendation logic"""
        import matplotlib.pyplot as plt
        import seaborn as sns
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # 1. Personality traits radar chart
        self._plot_personality_radar(axes[0, 0], user_id)
        
        # 2. Emotion journey chart
        self._plot_emotion_journey(axes[0, 1], user_id)
        
        # 3. Recommendation factor contributions
        self._plot_factor_contributions(axes[1, 0], recommendations)
        
        # 4. Prediction confidence distribution
        self._plot_confidence_distribution(axes[1, 1], recommendations)
        
        plt.tight_layout()
        return fig
'''
Use the aif360 open-source library to detect bias.

10. Complete Implementation Roadmap



10.1 Phase 1: Infrastructure (1-2 months)

'''python
Project structure
movie_psychology_recommender/
├── data/
│   ├── collectors/
│   │   ├── psychology_survey.py
│   │   ├── movie_metadata_scraper.py
│   │   └── user_behavior_tracker.py
│   ├── processors/
│   │   ├── personality_scorer.py
│   │   ├── emotion_analyzer.py
│   │   └── feature_engineer.py
│   └── storage/
│       ├── user_profiles/
│       ├── movie_attributes/
│       └── interaction_logs/
├── models/
│   ├── baseline/
│   │   ├── collaborative_filtering.py
│   │   └── content_based.py
│   ├── psychological/
│   │   ├── personality_matcher.py
│   │   ├── emotion_predictor.py
│   │   └── cognitive_load_estimator.py
│   └── hybrid/
│       ├── lightfm_enhanced.py
│       ├── neural_hybrid.py
│       └── ensemble.py
├── api/
│   ├── endpoints/
│   │   ├── recommendations.py
│   │   ├── user_profile.py
│   │   └── analytics.py
│   └── middleware/
│       ├── auth.py
│       ├── rate_limiter.py
│       └── cache.py
├── evaluation/
│   ├── metrics/
│   │   ├── accuracy.py
│   │   ├── diversity.py
│   │   ├── fairness.py
│   │   └── psychological_validity.py
│   └── experiments/
│       ├── ab_testing.py
│       └── user_studies.py
├── deployment/
│   ├── docker/
│   ├── kubernetes/
│   └── monitoring/
└── docs/
    ├── api_documentation.md
    ├── psychological_framework.md
    └── deployment_guide.md
'''



10.2 Phase Two: Psychology Integration (2-3 Months)

**Key Task List:**

- [ ] Implement Big Five personality questionnaire system
- [ ] Build movie psychological attributes annotation platform
- [ ] Train personality prediction model (from text)
- [ ] Develop emotional state tracking system
- [ ] Build psychology-movie matching rules engine
- [ ] Conduct initial user testing (N=100)



10.3 Phase Three: Production Deployment (3-4 months)

**Deployment Checklist:**

'''yaml
production_readiness:
  scalability:
    - [ ] Support 100,000+ concurrent users
    - [ ] Response time < 200ms (p95)
    - [ ] Auto-scaling configuration
  
  reliability:
    - [ ] 99.9% uptime SLA
    - [ ] Failover mechanism
    - [ ] Data backup strategy
  
  security:
    - [ ] Psychological data encryption
    - [ ] GDPR compliance
    - [ ] Access control implementation
  
  monitoring:
    - [ ] Real-time performance monitoring
    - [ ] Psychological prediction accuracy tracking
    - [ ] User satisfaction dashboard
  
  optimization:
    - [ ] Model compression (reduce 80% size)
    - [ ] Edge computing deployment
    - [ ] Cache strategy optimization
'''

Conclusion

Integrating psychology deeply into an AI movie recommendation system is not only a technological innovation but also a profound understanding of human viewing experiences. Through the framework, tools, and implementation examples provided in this guide, you can build a recommendation system that truly understands users' inner needs.

**Key Success Factors:**

1. **Scientific Rigor**: Based on empirical psychology theories, not speculation
2. **Technological Innovation**: Leverage the latest open-source frameworks and deep learning technologies
3. **User-Centricity**: Always aim to enhance user experience as the ultimate goal
4. **Ethical Responsibility**: Protect privacy, avoid bias, promote mental health
5. **Continuous Evolution**: Continuously optimize based on user feedback and new research

Start with simple linear models, gradually integrate advanced frameworks like LightFM, TensorFlow Recommenders, then multimodal deep learning and emotion-adaptive systems, your recommendation system will provide unprecedented personalized experiences. Remember, technology is just the means; the true goal is to help every user find that soul-touching work in the vast ocean of movies.

Learn more:
1. [(PDF) MoView Engine : An Open Source Movie Recommender]([historical-url]
2. [User preference modeling for movie recommendations based on deep learning | Scientific Reports]([historical-url]
3. [TensorFlow Recommenders]([historical-url]
4. [GitHub - lyst/lightfm: A Python implementation of LightFM, a hybrid recommendation algorithm.]([historical-url]
5. [Movie Recommendation System - Open Source Agenda]([historical-url]
6. [An intelligent film recommender system based on emotional analysis - PMC]([historical-url]
7. [GitHub - yashsmehta/personality-prediction: Experiments for automated personality detection using Language Models and psycholinguistic features on various famous personality datasets including the Essays dataset (Big-Five)]([historical-url]
8. [Build a Hybrid Recommender System in Python using LightFM]([historical-url]
9. [GitHub - vgaurav3011/Movie-Recommender-Engine: A movie recommendation engine based Database Management System built as an open source movie recommender to promote freedom of software]([historical-url]
10. [Personalized movie recommendation in IoT-enhanced systems using graph convolutional network and multi-layer perceptron | Scientific Reports]([historical-url]
11. [GitHub - tensorflow/recommenders: TensorFlow Recommenders is a library for building recommender system models using TensorFlow.]([historical-url]
12. [LightFM tutorial for creating recommendations in Python | Step By Step Data Science]([historical-url]
13. [movie-recomendation-system · GitHub Topics · GitHub]([historical-url]
14. [Movie recommendation and sentiment analysis using machine learning - ScienceDirect]([historical-url]
15. [(PDF) A Survey on Big Five Personality Traits Prediction Using Tensorflow]([historical-url]
16. [Hybrid Recommendation System using LightFM | by Diko Sakti Prabowo | Medium]([historical-url]
17. [GitHub - grahamjenson/list_of_recommender_systems: A List of Recommender Systems and Resources]([historical-url]
18. [MOVIE RECOMMENDATION SYSTEM BASED ON ...]([historical-url]
19. [GitHub - jhuang12/Tensorflow-for-personality-items-classification: Use NLP in tensorflow to classify big-five personality items to improve accuracy compared with naive Bayesian methods]([historical-url]
20. [LightFM Hybrid Recommendation system]([historical-url]
21. [Building a fullstack movie recommendation system | Google Codelabs]([historical-url]
22. [Predicting Users' Movie Preference and Rating Behavior from Personality and Values | ACM Transactions on Interactive Intelligent Systems]([historical-url]
23. [GitHub - jkwieser/personality-prediction-from-text: Predicting big five personality traits from a given text.]([historical-url]
24. [GitHub - wavelets/lightfm: A Python implementation of LightFM, a hybrid recommendation algorithm.]([historical-url]
25. [Movie Recommendation System — Bollywood and Hollywood using Python,Streamlit and count vectorizer | by Adarsh Chaurasiya | Medium]([historical-url]
26. [A Non-intrusive Movie Recommendation System | SpringerLink]([historical-url]
27. [personality-traits · GitHub Topics · GitHub]([historical-url]
28. [Recommendation System in Python: LightFM | Towards Data Science]([historical-url]
29. [Movie Recommendation Systems: A Business Guide]([historical-url]
30. [Enhancing Sequence Movie Recommendation System Using Deep Learning and KMeans]([historical-url]
31. [Big Five Personality Detection Using Deep Convolutional ...]([historical-url]
32. [Welcome to LightFM's documentation! — LightFM 1.16 documentation]([historical-url]
33. [GitHub - rafaelpierre/moviegpt: MovieGPT: A RAG, Gen AI application for Movie Recommendations]([historical-url]
34. [(PDF) Emotion-Based Movie Recommendation System]([historical-url]
35. [personality-predicting · GitHub Topics · GitHub]([historical-url]
36. [Build a Hybrid Recommender System in Python using LightFM | Ai Online Course]([historical-url]
37. [GitHub - diveshsoni/Movie-Recommendation-System: Website that recommends movies to the users based on their existing movie ratings.]([historical-url]
38. [Movie Recommendation System Using Machine Learning]([historical-url]
39. [Personality Prediction Project Using Machine Learning]([historical-url]
40. [LightFM - hybrid matrix factorisation on MovieLens (Python, ...]([historical-url]
41. [PsychologyRS_Paper_List]([historical-url]
42. [Building an Advanced Movie Recommendation System with RAG]([historical-url]

11. Advanced Psychology Models and Application Extensions



11.1 Motivation Psychology Integration

**Self-Determination Theory (Self-Determination Theory, SDT)**

Self-Determination Theory emphasizes three basic psychological needs: autonomy, competence, and relatedness. These needs can be used to predict users' movie preferences.

'''python
class SDTMovieRecommender:
    def __init__(self):
        self.sdt_analyzer = SDTAnalyzer()
        
    def analyze_sdt_needs(self, user_behavior):
        """Analyze user's SDT needs status"""
        needs = {
            'autonomy': self._calculate_autonomy_need(user_behavior),
            'competence': self._calculate_competence_need(user_behavior),
            'relatedness': self._calculate_relatedness_need(user_behavior)
        }
        return needs
    
    def _calculate_autonomy_need(self, behavior):
        """Calculate autonomy need"""
        # Analyze if user tends to make independent choices
        independent_choices = behavior['self_selected_movies'] / behavior['total_movies']
        exploration_rate = behavior['new_genre_tries'] / behavior['total_sessions']
        return (independent_choices * 0.6 + exploration_rate * 0.4)
    
    def recommend_by_sdt(self, user_id, sdt_needs):
        """Recommend movies based on SDT needs"""
        recommendations = []
        
        if sdt_needs['autonomy'] < 0.4:
            # Recommend movies showcasing personal freedom and choice
            recommendations.extend(self._get_autonomy_movies())
        
        if sdt_needs['competence'] < 0.4:
            # Recommend movies showcasing growth and achievement
            recommendations.extend(self._get_competence_movies())
        
        if sdt_needs['relatedness'] < 0.4:
            # Recommend movies showcasing interpersonal connections
            recommendations.extend(self._get_relatedness_movies())
        
        return recommendations
'''

**Maslow's Hierarchy of Needs Theory Application**

'''python
class MaslowRecommender:
    def __init__(self):
        self.need_levels = [
            'physiological', 'safety', 'love_belonging', 
            'esteem', 'self_actualization'
        ]
        
    def map_movie_to_needs(self, movie_features):
        """Map movies to need levels"""
        need_scores = {}
        
        # Safety needs: stable, predictable plots
        need_scores['safety'] = self._calculate_safety_score(movie_features)
        
        # Love and belonging: family, friendship, romance themes
        need_scores['love_belonging'] = self._calculate_belonging_score(movie_features)
        
        # Esteem needs: achievement, recognition themes
        need_scores['esteem'] = self._calculate_esteem_score(movie_features)
        
        # Self-actualization: personal growth, transcendence themes
        need_scores['self_actualization'] = self._calculate_actualization_score(movie_features)
        
        return need_scores
    
    def recommend_for_current_need(self, user_id):
        """Recommend based on user's current need level"""
        current_need = self._assess_user_need_level(user_id)
        
        # Recommend movies that fulfill the current need
        primary_recs = self._get_movies_for_need(current_need)
        
        # Also recommend some movies that promote growth to the next level
        growth_recs = self._get_growth_movies(current_need)
        
        return {
            'fulfillment': primary_recs,
            'growth': growth_recs
        }
'''



11.2 Cognitive Bias Aware Recommender

'''python
class CognitiveBiasAwareRecommender:
    def __init__(self):
        self.bias_detectors = self._init_bias_detectors()
        
    def detect_user_biases(self, user_history):
        """Detect user's cognitive biases"""
        biases = {
            'confirmation_bias': self._detect_confirmation_bias(user_history),
            'availability_heuristic': self._detect_availability_bias(user_history),
            'anchoring': self._detect_anchoring_bias(user_history),
            'bandwagon_effect': self._detect_bandwagon_effect(user_history),
            'recency_bias': self._detect_recency_bias(user_history)
        }
        return biases
    
    def _detect_confirmation_bias(self, history):
        """Detect confirmation bias - only watches movies that match existing views"""
        genre_diversity = len(set(history['genres'])) / len(history['genres'])
        theme_diversity = len(set(history['themes'])) / len(history['themes'])
        return 1 - (genre_diversity + theme_diversity) / 2
    
    def counter_bias_recommendations(self, user_id, detected_biases):
        """Provide recommendations that counter cognitive biases"""
        counter_recs = []
        
        if detected_biases['confirmation_bias'] > 0.7:
            # Recommend movies that challenge existing views
            counter_recs.extend(self._get_perspective_challenging_movies(user_id))
        
        if detected_biases['recency_bias'] > 0.6:
            # Recommend classic old films
            counter_recs.extend(self._get_classic_movies())
        
        if detected_biases['bandwagon_effect'] > 0.7:
            # Recommend niche but high-quality movies
            counter_recs.extend(self._get_hidden_gems())
        
        return counter_recs
'''



11.3 Flow State Optimization Recommendations

'''python
class FlowStateRecommender:
    def __init__(self):
        self.flow_analyzer = FlowStateAnalyzer()
        
    def assess_flow_potential(self, user_profile, movie_features):
        """Assess the potential of a movie to induce flow state"""
        # Flow requires a balance between skill and challenge
        user_cognitive_level = user_profile['cognitive_capacity']
        movie_complexity = movie_features['narrative_complexity']
        
        # Calculate skill-challenge balance
        balance_score = 1 - abs(user_cognitive_level - movie_complexity)
        
        # Other flow factors
        clear_goals = movie_features['narrative_clarity']
        immediate_feedback = movie_features['pacing_score']
        immersion_potential = movie_features['world_building_depth']
        
        flow_score = (
            balance_score * 0.4 +
            clear_goals * 0.2 +
            immediate_feedback * 0.2 +
            immersion_potential * 0.2
        )
        
        return flow_score
    
    def recommend_for_flow(self, user_id):
        """Recommend movies most likely to induce flow"""
        user_profile = self.get_user_profile(user_id)
        candidates = self.get_candidate_movies()
        
        flow_scores = []
        for movie in candidates:
            score = self.assess_flow_potential(user_profile, movie)
            flow_scores.append((movie, score))
        
        # Sort and return movies with the highest flow potential
        flow_scores.sort(key=lambda x: x[1], reverse=True)
        return [movie for movie, score in flow_scores[:20]]
'''



11.4 Narrative Psychology Integration

'''python
class NarrativePsychologyRecommender:
    def __init__(self):
        self.narrative_analyzer = NarrativeAnalyzer()
        
    def analyze_user_narrative_preferences(self, user_history):
        """Analyze user's narrative preferences"""
        preferences = {
            'hero_journey': self._score_hero_journey_preference(user_history),
            'redemption_arc': self._score_redemption_preference(user_history),
            'tragedy': self._score_tragedy_preference(user_history),
            'comedy': self._score_comedy_preference(user_history),
            'coming_of_age': self._score_coming_of_age_preference(user_history),
            'rags_to_riches': self._score_rags_to_riches_preference(user_history)
        }
        return preferences
    
    def match_narrative_to_life_stage(self, user_profile):
        """Match narrative types based on life stage"""
        life_stage = user_profile.get('life_stage', 'adult')
        current_challenges = user_profile.get('current_challenges', [])
        
        narrative_recommendations = []
        
        if 'career_transition' in current_challenges:
            narrative_recommendations.append('hero_journey')
            narrative_recommendations.append('redemption_arc')
        
        if 'relationship_issues' in current_challenges:
            narrative_recommendations.append('romantic_comedy')
            narrative_recommendations.append('relationship_drama')
        
        if life_stage == 'young_adult':
            narrative_recommendations.append('coming_of_age')
        
        return narrative_recommendations
    
    def recommend_by_narrative_therapy(self, user_id):
        """Recommend movies based on narrative therapy principles"""
        user_profile = self.get_user_profile(user_id)
        
        # Identify narrative types user may need
        therapeutic_narratives = self._identify_therapeutic_narratives(user_profile)
        
        recommendations = []
        for narrative_type in therapeutic_narratives:
            movies = self._get_movies_by_narrative(narrative_type)
            for movie in movies:
                movie['therapeutic_value'] = self._calculate_therapeutic_value(
                    movie, user_profile
                )
            recommendations.extend(movies)
        
        return sorted(recommendations, key=lambda x: x['therapeutic_value'], reverse=True)
'''

12. Social Psychology Factors Integration



12.1 Application of Social Identity Theory

'''python
class SocialIdentityRecommender:
    def __init__(self):
        self.identity_analyzer = SocialIdentityAnalyzer()
        
    def analyze_social_identities(self, user_profile):
        """Analyze user's social identities"""
        identities = {
            'cultural_identity': user_profile.get('cultural_background'),
            'generational_identity': self._determine_generation(user_profile['age']),
            'professional_identity': user_profile.get('occupation'),
            'fan_communities': user_profile.get('fan_memberships', []),
            'subcultures': user_profile.get('subculture_affiliations', [])
        }
        return identities
    
    def recommend_by_identity(self, user_id):
        """Recommend movies based on social identity"""
        identities = self.analyze_social_identities(self.get_user_profile(user_id))
        
        recommendations = []
        
        # Cultural identity related recommendations
        if identities['cultural_identity']:
            cultural_movies = self._get_culturally_relevant_movies(
                identities['cultural_identity']
            )
            recommendations.extend(cultural_movies)
        
        # Generational identity related recommendations
        generational_movies = self._get_generational_movies(
            identities['generational_identity']
        )
        recommendations.extend(generational_movies)
        
        # Fan community related recommendations
        for community in identities['fan_communities']:
            community_favorites = self._get_community_favorites(community)
            recommendations.extend(community_favorites)
        
        return self._deduplicate_and_rank(recommendations)
    
    def _determine_generation(self, age):
        """Determine generation based on age"""
        if age < 12:
            return 'gen_alpha'
        elif age < 28:
            return 'gen_z'
        elif age < 44:
            return 'millennial'
        elif age < 60:
            return 'gen_x'
        else:
            return 'boomer'
'''



12.2 Group Dynamics Recommendation

'''python
class GroupDynamicsRecommender:
    def __init__(self):
        self.group_analyzer = GroupDynamicsAnalyzer()
        
    def recommend_for_group(self, group_members):
        """Recommend movies for group viewing"""
        # Collect psychological profiles of all members
        profiles = [self.get_user_profile(member) for member in group_members]
        
        # Analyze group dynamics
        group_dynamics = self._analyze_group_dynamics(profiles)
        
        # Find common preferences
        common_preferences = self._find_common_preferences(profiles)
        
        # Consider power dynamics in the group
        influence_weights = self._calculate_influence_weights(group_dynamics)
        
        # Generate group recommendations
        recommendations = self._generate_group_recommendations(
            common_preferences, 
            influence_weights,
            group_dynamics
        )
        
        return recommendations
    
    def _analyze_group_dynamics(self, profiles):
        """Analyze group dynamics"""
        dynamics = {
            'personality_diversity': self._calculate_personality_diversity(profiles),
            'opinion_leader': self._identify_opinion_leader(profiles),
            'conflict_potential': self._assess_conflict_potential(profiles),
            'cohesion_level': self._calculate_cohesion(profiles)
        }
        return dynamics
    
    def _generate_group_recommendations(self, preferences, weights, dynamics):
        """Generate recommendations considering group dynamics"""
        candidates = self.get_candidate_movies()
        
        scored_movies = []
        for movie in candidates:
            # Base preference score
            preference_score = self._calculate_preference_match(movie, preferences)
            
            # Group harmony score (avoid controversial content)
            harmony_score = self._calculate_harmony_score(movie, dynamics)
            
            # Social value score (movies suitable for discussion)
            social_value = self._calculate_social_value(movie)
            
            final_score = (
                preference_score * 0.5 +
                harmony_score * 0.3 +
                social_value * 0.2
            )
            
            scored_movies.append((movie, final_score))
        
        return sorted(scored_movies, key=lambda x: x[1], reverse=True)[:10]
'''



12.3 Application of Social Comparison Theory

'''python
class SocialComparisonRecommender:
    def __init__(self):
        self.comparison_analyzer = SocialComparisonAnalyzer()
        
    def analyze_comparison_tendency(self, user_behavior):
        """Analyze user's social comparison tendency"""
        tendencies = {
            'upward_comparison': self._detect_upward_comparison(user_behavior),
            'downward_comparison': self._detect_downward_comparison(user_behavior),
            'lateral_comparison': self._detect_lateral_comparison(user_behavior)
        }
        return tendencies
    
    def recommend_based_on_comparison(self, user_id):
        """Recommend based on social comparison tendency"""
        tendencies = self.analyze_comparison_tendency(
            self.get_user_behavior(user_id)
        )
        
        recommendations = []
        
        if tendencies['upward_comparison'] > 0.6:
            # Users who tend to engage in upward comparison may like inspirational and success stories
            recommendations.extend(self._get_aspirational_movies())
        
        if tendencies['downward_comparison'] > 0.6:
            # Users who tend to engage in downward comparison may need self-affirming content
            recommendations.extend(self._get_self_affirming_movies())
        
        return recommendations
'''

Thirteen, Developmental Psychology Perspective



13.1 Life Cycle Stage Recommendations

'''python
class LifeStageRecommender:
    def __init__(self):
        self.life_stage_analyzer = LifeStageAnalyzer()
        
    def determine_life_stage(self, user_profile):
        """Determine the user's life stage"""
        age = user_profile['age']
        life_events = user_profile.get('recent_life_events', [])
        
        # Erikson's psychosocial development stages
        if age < 18:
            stage = 'identity_vs_confusion'
            developmental_task = 'Establish self-identity'
        elif age < 40:
            stage = 'intimacy_vs_isolation'
            developmental_task = 'Establish intimate relationships'
        elif age < 65:
            stage = 'generativity_vs_stagnation'
            developmental_task = 'Contribute to society, nurture the next generation'
        else:
            stage = 'integrity_vs_despair'
            developmental_task = 'Reflect on life, accept oneself'
        
        return {
            'stage': stage,
            'task': developmental_task,
            'age': age,
            'life_events': life_events
        }
    
    def recommend_for_life_stage(self, user_id):
        """Recommend movies based on life stage"""
        user_profile = self.get_user_profile(user_id)
        life_stage = self.determine_life_stage(user_profile)
        
        recommendations = []
        
        if life_stage['stage'] == 'identity_vs_confusion':
            # Recommend movies exploring self-identity
            recommendations.extend([
                {'type': 'coming_of_age', 'reason': 'Explore self-identity'},
                {'type': 'identity_exploration', 'reason': 'Discover personal values'}
            ])
        
        elif life_stage['stage'] == 'intimacy_vs_isolation':
            # Recommend movies about relationships and connections
            recommendations.extend([
                {'type': 'romantic_drama', 'reason': 'Explore intimate relationships'},
                {'type': 'friendship_stories', 'reason': 'Understand interpersonal connections'}
            ])
        
        elif life_stage['stage'] == 'generativity_vs_stagnation':
            # Recommend movies about legacy and contribution
            recommendations.extend([
                {'type': 'mentorship_stories', 'reason': 'Pass on wisdom'},
                {'type': 'legacy_themes', 'reason': 'Reflect on life's meaning'}
            ])
        
        elif life_stage['stage'] == 'integrity_vs_despair':
            # Recommend movies about life reflection and wisdom
            recommendations.extend([
                {'type': 'life_reflection', 'reason': 'Reflect on life's journey'},
                {'type': 'wisdom_stories', 'reason': 'Share life wisdom'}
            ])
        
        return self._get_movies_by_recommendations(recommendations)
'''



13.2 Attachment Theory Integration

'''python
class AttachmentStyleRecommender:
    def __init__(self):
        self.attachment_analyzer = AttachmentAnalyzer()
        
    def assess_attachment_style(self, user_profile, behavior_data):
        """Assess user's attachment style"""
        # Four attachment styles
        styles = {
            'secure': 0,
            'anxious_preoccupied': 0,
            'dismissive_avoidant': 0,
            'fearful_avoidant': 0
        }
        
        # Infer from viewing behavior
        romantic_movie_reactions = behavior_data.get('romantic_movie_ratings', [])
        relationship_content_engagement = behavior_data.get('relationship_content_time', 0)
        
        # Secure type: Accepts various relationship content
        if self._shows_balanced_relationship_interest(behavior_data):
            styles['secure'] += 0.4
        
        # Anxious type: High focus on relationship content, possibly rewatching
        if relationship_content_engagement > 0.7:
            styles['anxious_preoccupied'] += 0.3
        
        # Avoidant type: Avoids intimacy themes
        if self._avoids_intimacy_content(behavior_data):
            styles['dismissive_avoidant'] += 0.3
        
        return max(styles, key=styles.get)
    
    def recommend_by_attachment(self, user_id):
        """Recommend based on attachment style"""
        attachment_style = self.assess_attachment_style(
            self.get_user_profile(user_id),
            self.get_behavior_data(user_id)
        )
        
        recommendations = []
        
        if attachment_style == 'secure':
            # Secure type can accept various relationship themes
            recommendations = self._get_diverse_relationship_movies()
        
        elif attachment_style == 'anxious_preoccupied':
            # Anxious type may benefit from movies showing healthy relationships
            recommendations = self._get_secure_relationship_models()
            # Avoid recommending separation themes that may trigger anxiety
            recommendations = self._filter_out_abandonment_themes(recommendations)
        
        elif attachment_style == 'dismissive_avoidant':
            # Avoidant type may prefer stories with independent protagonists
            recommendations = self._get_independence_themed_movies()
            # Gradually introduce some healthy relationship content
            recommendations.extend(self._get_gentle_connection_movies())
        
        elif attachment_style == 'fearful_avoidant':
            # Fearful type needs safe, predictable content
            recommendations = self._get_safe_relationship_movies()
        
        return recommendations
'''



Fourteen, Clinical Psychology Applications



14.1 Mental Health Aware Recommendation

'''python
class MentalHealthAwareRecommender:
    def __init__(self):
        self.mental_health_detector = MentalHealthIndicatorDetector()
        self.content_safety_checker = ContentSafetyChecker()
        
    def assess_mental_health_indicators(self, user_behavior):
        """Assess mental health indicators (non-diagnostic)"""
        indicators = {
            'depression_risk': self._assess_depression_indicators(user_behavior),
            'anxiety_risk': self._assess_anxiety_indicators(user_behavior),
            'stress_level': self._assess_stress_level(user_behavior),
            'social_isolation': self._assess_isolation_indicators(user_behavior)
        }
        return indicators
    
    def _assess_depression_indicators(self, behavior):
        """Assess depression tendency indicators"""
        indicators = 0
        
        # Abnormal viewing time (too much or too little)
        if behavior['viewing_hours_change'] > 0.5:
            indicators += 0.2
        
        # Preference for sad content
        if behavior['sad_content_ratio'] > 0.6:
            indicators += 0.2
        
        # Decrease in social viewing
        if behavior['social_viewing_decrease'] > 0.4:
            indicators += 0.2
        
        return min(indicators, 1.0)
    
    def recommend_with_mental_health_awareness(self, user_id):
        """Mental health aware recommendation"""
        indicators = self.assess_mental_health_indicators(
            self.get_user_behavior(user_id)
        )
        
        recommendations = self.get_base_recommendations(user_id)
        
        # Adjust recommendations based on mental health indicators
        if indicators['depression_risk'] > 0.5:
            # Filter content that may exacerbate depression
            recommendations = self._filter_depressing_content(recommendations)
            # Add movies with positive, hopeful themes
            recommendations = self._inject_uplifting_content(recommendations)
        
        if indicators['anxiety_risk'] > 0.5:
            # Filter high-stress, thriller content
            recommendations = self._filter_anxiety_triggering(recommendations)
            # Add relaxing, healing content
            recommendations = self._inject_calming_content(recommendations)
        
        if indicators['social_isolation'] > 0.5:
            # Recommend movies suitable for social viewing
            recommendations = self._add_social_viewing_suggestions(recommendations)
        
        # Add mental health resource prompts (if indicators are too high)
        if any(v > 0.7 for v in indicators.values()):
            recommendations = self._add_mental_health_resources(recommendations)
        
        return recommendations
'''



14.2 Cinema Therapy Integration

'''python
class CinemaTherapyRecommender:
    def __init__(self):
        self.therapy_database = CinemaTherapyDatabase()
        
    def recommend_therapeutic_movies(self, user_id, therapeutic_goal=None):
        """Recommend movies with therapeutic value"""
        user_profile = self.get_user_profile(user_id)
        
        if not therapeutic_goal:
            therapeutic_goal = self._identify_therapeutic_needs(user_profile)
        
        therapeutic_movies = []
        
        # Select movies based on therapeutic goal
        if therapeutic_goal == 'grief_processing':
            therapeutic_movies = self._get_grief_processing_movies()
        elif therapeutic_goal == 'anxiety_reduction':
            therapeutic_movies = self._get_anxiety_reduction_movies()
        elif therapeutic_goal == 'self_esteem_building':
            therapeutic_movies = self._get_self_esteem_movies()
        elif therapeutic_goal == 'relationship_skills':
            therapeutic_movies = self._get_relationship_learning_movies()
        elif therapeutic_goal == 'trauma_processing':
            therapeutic_movies = self._get_trauma_processing_movies()
        
        # Add therapy guide for each movie
        for movie in therapeutic_movies:
            movie['therapy_guide'] = self._generate_therapy_guide(movie, therapeutic_goal)
        
        return therapeutic_movies
    
    def _generate_therapy_guide(self, movie, goal):
        """Generate cinema therapy guide"""
        guide = {
            'pre_viewing': self._get_pre_viewing_preparation(movie, goal),
            'key_scenes': self._identify_therapeutic_scenes(movie, goal),
            'reflection_questions': self._generate_reflection_questions(movie, goal),
            'post_viewing_activities': self._suggest_post_viewing_activities(movie, goal)
        }
        return guide
    
    def _get_pre_viewing_preparation(self, movie, goal):
        """Pre-viewing preparation suggestions"""
        return {
            'mindset': f"Prepare to watch with an open mindset, focusing on themes related to {goal}",
            'environment': "Choose a quiet, comfortable environment",
            'journaling': "Prepare a notebook to record viewing feelings"
        }
    
    def _generate_reflection_questions(self, movie, goal):
        """Generate reflection questions"""
        base_questions = [
            "Which character in this movie resonated with you the most? Why?",
            "Which scene in the movie touched your emotions?",
            "What did you learn from this movie?",
            "How did this movie change your perspective on a certain issue?"
        ]
        
        goal_specific_questions = {
            'grief_processing': [
                "How did the characters in the movie process loss?",
                "What do you think a healthy grieving process looks like?"
            ],
            'anxiety_reduction': [
                "How did the characters in the movie face their fears?",
                "What coping strategies can you learn from it?"
            ],
            'self_esteem_building': [
                "How did the characters in the movie discover their own value?",
                "What inspiration does this provide for you?"
            ]
        }
        
        return base_questions + goal_specific_questions.get(goal, [])
'''



14.3 Positive Psychology Integration

'''python
class PositivePsychologyRecommender:
    def __init__(self):
        self.perma_analyzer = PERMAAnalyzer()
        
    def analyze_perma_needs(self, user_profile):
        """Analyze user's PERMA needs (Positive Psychology model)"""
        perma = {
            'positive_emotion': self._assess_positive_emotion_need(user_profile),
            'engagement': self._assess_engagement_need(user_profile),
            'relationships': self._assess_relationship_need(user_profile),
            'meaning': self._assess_meaning_need(user_profile),
            'accomplishment': self._assess_accomplishment_need(user_profile)
        }
        return perma
    
    def recommend_for_wellbeing(self, user_id):
        """Recommend movies based on wellbeing enhancement"""
        perma_needs = self.analyze_perma_needs(self.get_user_profile(user_id))
        
        # Find the dimension most needing improvement
        lowest_dimension = min(perma_needs, key=perma_needs.get)
        
        recommendations = []
        
        if lowest_dimension == 'positive_emotion':
            # Recommend movies that induce positive emotions
            recommendations.extend(self._get_joy_inducing_movies())
            recommendations.extend(self._get_gratitude_inspiring_movies())
        
        elif lowest_dimension == 'engagement':
            # Recommend movies that induce flow
            recommendations.extend(self._get_immersive_movies())
        
        elif lowest_dimension == 'relationships':
            # Recommend movies about interpersonal connections
            recommendations.extend(self._get_connection_movies())
        
        elif lowest_dimension == 'meaning':
            # Recommend movies exploring life's meaning
            recommendations.extend(self._get_meaning_exploring_movies())
        
        elif lowest_dimension == 'accomplishment':
            # Recommend movies about achievement and growth
            recommendations.extend(self._get_achievement_movies())
        
        return recommendations
    
    def track_wellbeing_impact(self, user_id, movie_id):
        """Track movie's impact on wellbeing"""
        pre_viewing_perma = self.get_current_perma(user_id)
        
        # Assess after viewing
        post_viewing_perma = self.assess_post_viewing_perma(user_id)
        
        impact = {
            dimension: post_viewing_perma[dimension] - pre_viewing_perma[dimension]
            for dimension in pre_viewing_perma
        }
        
        # Record impact to improve future recommendations
        self.record_wellbeing_impact(user_id, movie_id, impact)
        
        return impact
'''

Fifteen, Advanced Technical Implementation



15.1 Federated Learning Privacy Protection

'''python
import tensorflow_federated as tff

class FederatedPsychologyRecommender:
    def __init__(self):
        self.model_fn = self._create_model_fn()
        
    def _create_model_fn(self):
        """Create federated learning model"""
        def model_fn():
            keras_model = tf.keras.Sequential([
                tf.keras.layers.Dense(64, activation='relu', input_shape=(15,)),
                tf.keras.layers.Dropout(0.3),
                tf.keras.layers.Dense(32, activation='relu'),
                tf.keras.layers.Dense(1, activation='sigmoid')
            ])
            
            return tff.learning.from_keras_model(
                keras_model,
                input_spec=preprocessed_example_dataset.element_spec,
                loss=tf.keras.losses.BinaryCrossentropy(),
                metrics=[tf.keras.metrics.AUC()]
            )
        return model_fn
    
    def train_federated(self, client_data):
        """Federated training - psychological data does not leave user device"""
        iterative_process = tff.learning.build_federated_averaging_process(
            self.model_fn,
            client_optimizer_fn=lambda: tf.keras.optimizers.SGD(0.02),
            server_optimizer_fn=lambda: tf.keras.optimizers.SGD(1.0)
        )
        
        state = iterative_process.initialize()
        
        for round_num in range(10):
            state, metrics = iterative_process.next(state, client_data)
            print(f'Round {round_num}: {metrics}')
        
        return state
    
    def predict_with_privacy(self, user_psychology_local, movie_features):
        """Perform prediction locally to protect psychological data privacy"""
        # Psychological features processed on user device
        local_embedding = self.local_model.encode(user_psychology_local)
        
        # Only send encrypted embedding vectors
        encrypted_embedding = self.encrypt(local_embedding)
        
        # Server-side computation
        prediction = self.server_predict(encrypted_embedding, movie_features)
        
        return prediction
'''



15.2 Differential Privacy Implementation

'''python
import tensorflow_privacy as tfp

class DifferentialPrivacyRecommender:
    def __init__(self, noise_multiplier=1.1, l2_norm_clip=1.0):
        self.noise_multiplier = noise_multiplier
        self.l2_norm_clip = l2_norm_clip
        
    def create_dp_optimizer(self):
        """Create differential privacy optimizer"""
        optimizer = tfp.DPKerasSGDOptimizer(
            l2_norm_clip=self.l2_norm_clip,
            noise_multiplier=self.noise_multiplier,
            num_microbatches=1,
            learning_rate=0.01
        )
        return optimizer
    
    def train_with_dp(self, model, train_data, epochs=10):
        """Train model with differential privacy"""
        dp_optimizer = self.create_dp_optimizer()
        
        model.compile(
            optimizer=dp_optimizer,
            loss=tf.keras.losses.BinaryCrossentropy(
                from_logits=True,
                reduction=tf.losses.Reduction.NONE
            ),
            metrics=['accuracy']
        )
        
        history = model.fit(
            train_data,
            epochs=epochs,
            validation_split=0.1
        )
        
        # Compute privacy budget
        eps = self.compute_epsilon(epochs, len(train_data))
        print(f"Privacy budget (ε): {eps}")
        
        return model, history
    
    def compute_epsilon(self, epochs, dataset_size, delta=1e-5):
        """Compute privacy budget"""
        from tensorflow_privacy.privacy.analysis import compute_dp_sgd_privacy
        
        eps, _ = compute_dp_sgd_privacy.compute_dp_sgd_privacy(
            n=dataset_size,
            batch_size=32,
            noise_multiplier=self.noise_multiplier,
            epochs=epochs,
            delta=delta
        )
        return eps
'''



15.3 Causal Inference Integration

'''python
from causalml.inference.meta import BaseSRegressor, BaseTRegressor
from sklearn.ensemble import GradientBoostingRegressor

class CausalPsychologyRecommender:
    def __init__(self):
        self.causal_model = BaseSRegressor(GradientBoostingRegressor())
        
    def estimate_treatment_effect(self, user_features, treatment, outcome):
        """Estimate the causal effect of psychological features on viewing satisfaction"""
        # treatment: Whether to recommend psychologically matched movies
        # outcome: Viewing satisfaction
        
        self.causal_model.fit(
            X=user_features,
            treatment=treatment,
            y=outcome
        )
        
        # Estimate individual treatment effect
        ite = self.causal_model.predict(user_features)
        
        return ite
    
    def recommend_with_causal_reasoning(self, user_id):
        """Recommendation based on causal inference"""
        user_features = self.get_user_features(user_id)
        candidates = self.get_candidate_movies()
        
        recommendations = []
        for movie in candidates:
            # Estimate causal effect of recommending this movie
            treatment_effect = self.estimate_individual_effect(
                user_features, movie
            )
            
            # Only recommend movies with positive causal effect
            if treatment_effect > 0:
                recommendations.append({
                    'movie': movie,
                    'expected_effect': treatment_effect,
                    'confidence': self.calculate_confidence(treatment_effect)
                })
        
        return sorted(recommendations, key=lambda x: x['expected_effect'], reverse=True)
    
    def counterfactual_explanation(self, user_id, movie_id, prediction):
        """Generate counterfactual explanations"""
        user_features = self.get_user_features(user_id)
        
        # Find the minimal feature changes needed to change the prediction
        counterfactuals = []
        
        for feature in ['openness', 'neuroticism', 'need_cognition']:
            # Calculate how much change is needed to alter the recommendation
            required_change = self.find_counterfactual(
                user_features, feature, movie_id, prediction
            )
            
            if required_change:
                counterfactuals.append({
                    'feature': feature,
                    'current_value': user_features[feature],
                    'required_value': required_change,
                    'explanation': f"If your {feature} changes from {user_features[feature]:.2f} to {required_change:.2f}, the recommendation score for this movie will change"
                })
        
        return counterfactuals
'''



15.4 Reinforcement Learning Dynamic Recommendation

'''python
import gym
import numpy as np
from stable_baselines3 import PPO, DQN

class RLPsychologyRecommender:
    def __init__(self):
        self.env = MovieRecommendationEnv()
        self.agent = PPO("MlpPolicy", self.env, verbose=1)
        
    def train_agent(self, total_timesteps=100000):
        """Train reinforcement learning agent"""
        self.agent.learn(total_timesteps=total_timesteps)
        
    def recommend_with_rl(self, user_state):
        """Make recommendations using RL agent"""
        action, _ = self.agent.predict(user_state, deterministic=True)
        return self.decode_action(action)

class MovieRecommendationEnv(gym.Env):
    def __init__(self):
        super().__init__()
        
        # State space: user psychological features + context
        self.observation_space = gym.spaces.Box(
            low=0, high=1, shape=(20,), dtype=np.float32
        )
        
        # Action space: recommended movie genre combinations
        self.action_space = gym.spaces.Discrete(100)
        
        self.current_user = None
        self.session_history = []
        
    def reset(self):
        """Reset environment"""
        self.current_user = self._sample_user()
        self.session_history = []
        return self._get_state()
    
    def step(self, action):
        """Execute recommendation action"""
        movie = self._decode_action(action)
        
        # Simulate user response
        user_response = self._simulate_user_response(movie)
        
        # Calculate reward
        reward = self._calculate_reward(user_response)
        
        # Update user state (emotions may change)
        self._update_user_state(user_response)
        
        # Check if done
        done = len(self.session_history) >= 10
        
        return self._get_state(), reward, done, {}
    
    def _calculate_reward(self, response):
        """Calculate reward function"""
        reward = 0
        
        # Basic satisfaction reward
        reward += response['satisfaction'] * 0.5
        
        # Psychological match reward
        reward += response['psychological_match'] * 0.3
        
        # Long-term engagement reward
        if response['completed_viewing']:
            reward += 0.2
        
        # Diversity reward (avoid repeated recommendations)
        if self._is_diverse_recommendation():
            reward += 0.1
        
        # Negative emotion penalty
        if response['negative_emotion_triggered']:
            reward -= 0.5
        
        return reward
    
    def _simulate_user_response(self, movie):
        """Simulate user response to recommendation"""
        # Calculate match score based on user psychological features and movie features
        match_score = self._calculate_match(self.current_user, movie)
        
        response = {
            'satisfaction': match_score + np.random.normal(0, 0.1),
            'psychological_match': self._calculate_psych_match(movie),
            'completed_viewing': match_score > 0.6,
            'negative_emotion_triggered': self._check_negative_trigger(movie)
        }
        
        return response
'''



15.5 Deep Integration of Graph Neural Networks

'''python
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv, GATConv, SAGEConv

class PsychologyGNN(torch.nn.Module):
    def __init__(self, num_user_features, num_movie_features, hidden_dim=64):
        super().__init__()
        
        # User psychological feature encoding
        self.user_encoder = torch.nn.Sequential(
            torch.nn.Linear(num_user_features, hidden_dim),
            torch.nn.ReLU(),
            torch.nn.Dropout(0.3),
            torch.nn.Linear(hidden_dim, hidden_dim)
        )
        
        # Movie feature encoding
        self.movie_encoder = torch.nn.Sequential(
            torch.nn.Linear(num_movie_features, hidden_dim),
            torch.nn.ReLU(),
            torch.nn.Dropout(0.3),
            torch.nn.Linear(hidden_dim, hidden_dim)
        )
        
        # Graph convolution layers
        self.conv1 = GATConv(hidden_dim, hidden_dim, heads=4, concat=False)
        self.conv2 = GATConv(hidden_dim, hidden_dim, heads=4, concat=False)
        self.conv3 = SAGEConv(hidden_dim, hidden_dim)
        
        # Psychological feature attention
        self.psych_attention = torch.nn.MultiheadAttention(
            embed_dim=hidden_dim, num_heads=4
        )
        
        # Prediction layer
        self.predictor = torch.nn.Sequential(
            torch.nn.Linear(hidden_dim * 2, hidden_dim),
            torch.nn.ReLU(),
            torch.nn.Dropout(0.3),
            torch.nn.Linear(hidden_dim, 1),
            torch.nn.Sigmoid()
        )
        
    def forward(self, user_features, movie_features, edge_index, user_psych):
        # Encode users and movies
        user_emb = self.user_encoder(user_features)
        movie_emb = self.movie_encoder(movie_features)
        
        # Merge node embeddings
        x = torch.cat([user_emb, movie_emb], dim=0)
        
        # Graph convolution propagation
        x = F.relu(self.conv1(x, edge_index))
        x = F.dropout(x, p=0.3, training=self.training)
        x = F.relu(self.conv2(x, edge_index))
        x = self.conv3(x, edge_index)
        
        # Psychological feature attention enhancement
        user_x = x[:len(user_features)]
        psych_enhanced, _ = self.psych_attention(
            user_x.unsqueeze(0),
            user_psych.unsqueeze(0),
            user_psych.unsqueeze(0)
        )
        user_x = user_x + psych_enhanced.squeeze(0)
        
        return user_x, x[len(user_features):]
    
    def predict(self, user_emb, movie_emb):
        combined = torch.cat([user_emb, movie_emb], dim=-1)
        return self.predictor(combined)
'''

16. Real-World Application Scenarios and Cases



16.1 Streaming Platform Integration Solution

'''python
class StreamingPlatformIntegration:
    def __init__(self, platform_api):
        self.platform_api = platform_api
        self.psychology_engine = PsychologyRecommendationEngine()
        
    def enhance_platform_recommendations(self, user_id, base_recommendations):
        """Enhance the streaming platform's base recommendations"""
        # Get user psychology profile
        user_psychology = self.psychology_engine.get_user_psychology(user_id)
        
        enhanced_recommendations = []
        for rec in base_recommendations:
            # Calculate psychology match score
            psych_score = self.psychology_engine.calculate_match(
                user_psychology, rec['movie_id']
            )
            
            # Adjust recommendation score
            rec['enhanced_score'] = rec['base_score'] * 0.6 + psych_score * 0.4
            rec['psychology_insights'] = self._generate_insights(
                user_psychology, rec['movie_id']
            )
            
            enhanced_recommendations.append(rec)
        
        # Resort
        enhanced_recommendations.sort(key=lambda x: x['enhanced_score'], reverse=True)
        
        return enhanced_recommendations
    
    def create_psychology_based_rows(self, user_id):
        """Create psychology-oriented recommendation rows"""
        user_psychology = self.psychology_engine.get_user_psychology(user_id)
        
        rows = []
        
        # Personality match row
        if user_psychology['openness'] > 0.7:
            rows.append({
                'title': 'Prepared for Your Curiosity',
                'movies': self._get_high_openness_movies(),
                'explanation': 'These movies are perfect for someone who loves exploring new things'
            })
        
        # Mood regulation row
        current_mood = self.psychology_engine.get_current_mood(user_id)
        if current_mood['stress'] > 0.6:
            rows.append({
                'title': 'Time to Relax',
                'movies': self._get_stress_relief_movies(),
                'explanation': 'These movies can help you relax'
            })
        
        # Cognitive challenge row
        if user_psychology['need_cognition'] > 0.7:
            rows.append({
                'title': 'Brain Teaser Time',
                'movies': self._get_complex_narrative_movies(),
                'explanation': 'These movies will challenge your brain'
            })
        
        return rows
'''



16.2 Educational Platform Application

'''python
class EducationalMovieRecommender:
    def __init__(self):
        self.learning_analyzer = LearningStyleAnalyzer()
        self.educational_db = EducationalMovieDatabase()
        
    def recommend_for_learning(self, student_id, learning_objective):
        """Recommend educational movies for learning objectives"""
        # Analyze learning style
        learning_style = self.learning_analyzer.analyze(student_id)
        
        # Get student psychological characteristics
        student_psychology = self.get_student_psychology(student_id)
        
        recommendations = []
        
        # Select movies based on learning objectives
        educational_movies = self.educational_db.get_movies_for_objective(
            learning_objective
        )
        
        for movie in educational_movies:
            # Calculate learning style match
            style_match = self._calculate_style_match(learning_style, movie)
            
            # Calculate psychological match
            psych_match = self._calculate_psych_match(student_psychology, movie)
            
            # Calculate educational value
            educational_value = movie['educational_score']
            
            final_score = (
                style_match * 0.3 +
                psych_match * 0.3 +
                educational_value * 0.4
            )
            
            recommendations.append({
                'movie': movie,
                'score': final_score,
                'learning_guide': self._generate_learning_guide(movie, learning_objective),
                'discussion_questions': self._generate_discussion_questions(movie)
            })
        
        return sorted(recommendations, key=lambda x: x['score'], reverse=True)
    
    def _generate_learning_guide(self, movie, objective):
        """Generate learning guide"""
        return {
            'pre_viewing': {
                'concepts_to_know': self._get_prerequisite_concepts(movie, objective),
                'questions_to_consider': self._get_pre_viewing_questions(movie)
            },
            'during_viewing': {
                'key_scenes': self._identify_educational_scenes(movie, objective),
                'note_taking_prompts': self._get_note_prompts(movie)
            },
            'post_viewing': {
                'reflection_activities': self._get_reflection_activities(movie),
                'further_reading': self._get_related_resources(movie, objective)
            }
        }
'''



16.3 Corporate Training Applications

'''python
class CorporateTrainingRecommender:
    def __init__(self):
        self.competency_analyzer = CompetencyAnalyzer()
        self.training_db = TrainingMovieDatabase()
        
    def recommend_for_development(self, employee_id, development_goals):
        """Recommend movies for employee development goals"""
        # Analyze employee competency gaps
        competency_gaps = self.competency_analyzer.identify_gaps(
            employee_id, development_goals
        )
        
        # Get employee psychology profile
        employee_psychology = self.get_employee_psychology(employee_id)
        
        recommendations = []
        
        for gap in competency_gaps:
            # Find movies that help develop this competency
            relevant_movies = self.training_db.get_movies_for_competency(gap['competency'])
            
            for movie in relevant_movies:
                # Calculate development value
                development_value = self._calculate_development_value(movie, gap)
                
                # Calculate psychological acceptance
                acceptance = self._calculate_acceptance(employee_psychology, movie)
                
                recommendations.append({
                    'movie': movie,
                    'target_competency': gap['competency'],
                    'development_value': development_value,
                    'acceptance_score': acceptance,
                    'learning_objectives': self._extract_learning_objectives(movie, gap),
                    'application_exercises': self._generate_application_exercises(movie, gap)
                })
        
        return recommendations
    
    def create_team_building_playlist(self, team_members):
        """Create movie playlist for team building"""
        # Analyze team dynamics
        team_dynamics = self._analyze_team_dynamics(team_members)
        
        # Identify areas needing improvement
        improvement_areas = self._identify_improvement_areas(team_dynamics)
        
        playlist = []
        
        for area in improvement_areas:
            movies = self._get_team_building_movies(area)
            
            for movie in movies:
                playlist.append({
                    'movie': movie,
                    'target_area': area,
                    'team_discussion_guide': self._create_team_discussion_guide(movie, area),
                    'group_activities': self._suggest_group_activities(movie)
                })
        
        return playlist
'''

Seventeen, Data Collection and Annotation Strategy



17.1 Psychological Characteristics Data Collection

'''python
class PsychologyDataCollector:
    def __init__(self):
        self.survey_engine = SurveyEngine()
        self.implicit_collector = ImplicitDataCollector()
        
    def collect_explicit_data(self, user_id):
        """Collect explicit psychological data"""
        surveys = {
            'big_five': self._administer_big_five_survey(),
            'need_cognition': self._administer_nfc_survey(),
            'attachment_style': self._administer_attachment_survey(),
            'movie_preferences': self._administer_movie_preference_survey()
        }
        
        return surveys
    
    def _administer_big_five_survey(self):
        """Big Five Personality Inventory (Short Version)"""
        questions = [
            # Extraversion
            {"id": "E1", "text": "I enjoy attending social events", "dimension": "extraversion"},
            {"id": "E2", "text": "I feel energized in crowds", "dimension": "extraversion"},
            
            # Agreeableness
            {"id": "A1", "text": "I care about others' feelings", "dimension": "agreeableness"},
            {"id": "A2", "text": "I am willing to help those in need", "dimension": "agreeableness"},
            
            # Neuroticism
            {"id": "N1", "text": "I often feel anxious", "dimension": "neuroticism"},
            {"id": "N2", "text": "My emotions fluctuate easily", "dimension": "neuroticism"},
            
            # Openness
            {"id": "O1", "text": "I like trying new things", "dimension": "openness"},
            {"id": "O2", "text": "I am interested in art and aesthetics", "dimension": "openness"},
            
            # Conscientiousness
            {"id": "C1", "text": "I plan my tasks", "dimension": "conscientiousness"},
            {"id": "C2", "text": "I pay attention to details", "dimension": "conscientiousness"}
        ]
        
        return self.survey_engine.administer(questions, scale="likert_5")
    
    def collect_implicit_data(self, user_id):
        """Collect implicit behavioral data"""
        implicit_data = {
            'viewing_patterns': self._collect_viewing_patterns(user_id),
            'interaction_patterns': self._collect_interaction_patterns(user_id),
            'social_patterns': self._collect_social_patterns(user_id),
            'temporal_patterns': self._collect_temporal_patterns(user_id)
        }
        
        return implicit_data
    
    def _collect_viewing_patterns(self, user_id):
        """Collect viewing patterns"""
        return {
            'average_session_length': self._get_avg_session_length(user_id),
            'completion_rate': self._get_completion_rate(user_id),
            'genre_distribution': self._get_genre_distribution(user_id),
            'rewatch_frequency': self._get_rewatch_frequency(user_id),
            'binge_watching_tendency': self._get_binge_tendency(user_id),
            'pause_frequency': self._get_pause_frequency(user_id),
            'skip_intro_rate': self._get_skip_intro_rate(user_id)
        }
    
    def infer_psychology_from_behavior(self, implicit_data):
        """Infer psychological characteristics from behavioral data"""
        inferred = {}
        
        # Infer openness from viewing genre diversity
        genre_diversity = len(set(implicit_data['viewing_patterns']['genre_distribution']))
        inferred['openness'] = min(genre_diversity / 10, 1.0)
        
        # Infer conscientiousness from completion rate
        inferred['conscientiousness'] = implicit_data['viewing_patterns']['completion_rate']
        
        # Infer extraversion from social viewing
        social_viewing_ratio = implicit_data['social_patterns'].get('group_viewing_ratio', 0)
        inferred['extraversion'] = social_viewing_ratio
        
        # Infer neuroticism from content choices
        horror_avoidance = 1 - implicit_data['viewing_patterns']['genre_distribution'].get('horror', 0)
        inferred['neuroticism'] = horror_avoidance * 0.5
        
        return inferred
'''



17.2 Movie Psychology Attribute Annotation

'''python
class MoviePsychologyAnnotator:
    def __init__(self):
        self.nlp_analyzer = NLPAnalyzer()
        self.crowdsource_platform = CrowdsourcePlatform()
        
    def annotate_movie(self, movie_id):
        """Annotate the movie's psychological attributes"""
        movie_data = self.get_movie_data(movie_id)
        
        annotations = {
            'automated': self._automated_annotation(movie_data),
            'crowdsourced': self._crowdsourced_annotation(movie_id),
            'expert': self._expert_annotation(movie_id)
        }
        
        # Fuse multi-source annotations
        final_annotation = self._fuse_annotations(annotations)
        
        return final_annotation
    
    def _automated_annotation(self, movie_data):
        """Automated annotation"""
        synopsis = movie_data['synopsis']
        reviews = movie_data['reviews']
        
        # Emotion analysis
        emotion_profile = self.nlp_analyzer.analyze_emotions(synopsis + ' '.join(reviews))
        
        # Theme analysis
        themes = self.nlp_analyzer.extract_themes(synopsis)
        
        # Complexity analysis
        complexity = self.nlp_analyzer.analyze_complexity(synopsis)
        
        # MOVIE model dimensions
        movie_dimensions = {
            'melodrama': self._score_melodrama(emotion_profile, themes),
            'comic': self._score_comic(emotion_profile, themes),
            'violent': self._score_violent(themes, movie_data.get('content_rating')),
            'imaginative': self._score_imaginative(themes, movie_data.get('genre')),
            'exciting': self._score_exciting(emotion_profile, themes)
        }
        
        return {
            'emotion_profile': emotion_profile,
            'themes': themes,
            'complexity': complexity,
            'movie_dimensions': movie_dimensions
        }
    
    def _crowdsourced_annotation(self, movie_id):
        """Crowdsourced annotation"""
        annotation_task = {
            'movie_id': movie_id,
            'questions': [
                {
                    'id': 'emotional_intensity',
                    'text': 'How intense are the emotions in this movie?',
                    'scale': 'likert_5'
                },
                {
                    'id': 'cognitive_demand',
                    'text': 'How much cognitive effort is noted to understand this movie?',
                    'scale': 'likert_5'
                },
                {
                    'id': 'suitable_mood',
                    'text': 'What mood is this movie suitable for watching?',
                    'options': ['Happy', 'Sad', 'Relaxed', 'Tense', 'Any mood']
                },
                {
                    'id': 'personality_fit',
                    'text': 'What type of person is this movie most suitable for?',
                    'options': ['People who like adventure', 'People who like to think', 'People who like to be moved', 'People who like excitement']
                }
            ]
        }
        
        responses = self.crowdsource_platform.collect_responses(
            annotation_task, 
            min_responses=10
        )
        
        return self._aggregate_crowdsource_responses(responses)
'''

18. System Testing and Quality Assurance



18.1 Psychology Validity Testing

'''python
class PsychologyValidityTester:
    def __init__(self):
        self.statistical_analyzer = StatisticalAnalyzer()
        
    def test_construct_validity(self, model, test_data):
        """Test construct validity"""
        results = {}
        
        # Convergent validity: related psychological traits should be correlated
        convergent = self._test_convergent_validity(model, test_data)
        results['convergent_validity'] = convergent
        
        # Discriminant validity: different psychological traits should be distinguished
        discriminant = self._test_discriminant_validity(model, test_data)
        results['discriminant_validity'] = discriminant
        
        # Predictive validity: psychological traits should predict behavior
        predictive = self._test_predictive_validity(model, test_data)
        results['predictive_validity'] = predictive
        
        return results
    
    def _test_convergent_validity(self, model, test_data):
        """Test convergent validity"""
        # For example: high openness should correlate with art film preference
        correlations = {}
        
        expected_correlations = [
            ('openness', 'art_film_preference', 'positive'),
            ('extraversion', 'social_movie_preference', 'positive'),
            ('neuroticism', 'horror_avoidance', 'positive'),
            ('conscientiousness', 'completion_rate', 'positive'),
            ('need_cognition', 'complex_movie_preference', 'positive')
        ]
        
        for trait, behavior, direction in expected_correlations:
            correlation = self.statistical_analyzer.calculate_correlation(
                test_data[trait], test_data[behavior]
            )
            
            is_valid = (
                (direction == 'positive' and correlation > 0.3) or
                (direction == 'negative' and correlation < -0.3)
            )
            
            correlations[f'{trait}_{behavior}'] = {
                'correlation': correlation,
                'expected_direction': direction,
                'is_valid': is_valid
            }
        
        return correlations
    
    def _test_predictive_validity(self, model, test_data):
        """Test predictive validity"""
        # Use psychological traits to predict actual viewing behavior
        predictions = model.predict(test_data['psychology_features'])
        actual = test_data['actual_preferences']
        
        metrics = {
            'rmse': np.sqrt(mean_squared_error(actual, predictions)),
            'mae': mean_absolute_error(actual, predictions),
            'correlation': np.corrcoef(actual, predictions)[0, 1],
            'explained_variance': explained_variance_score(actual, predictions)
        }
        
        return metrics
'''



18.2 User Experience Testing

'''python
class UXTester:
    def __init__(self):
        self.survey_engine = SurveyEngine()
        self.analytics = AnalyticsEngine()
        
    def conduct_user_study(self, participant_ids, study_duration_days=14):
        """Conduct user study"""
        study_results = {
            'pre_study': {},
            'during_study': {},
            'post_study': {}
        }
        
        # Pre-study survey
        for participant in participant_ids:
            study_results['pre_study'][participant] = self._pre_study_survey(participant)
        
        # Data collection during study
        study_results['during_study'] = self._collect_study_data(
            participant_ids, study_duration_days
        )
        
        # Post-study survey
        for participant in participant_ids:
            study_results['post_study'][participant] = self._post_study_survey(participant)
        
        # Analyze results
        analysis = self._analyze_study_results(study_results)
        
        return analysis
    
    def _pre_study_survey(self, participant_id):
        """Pre-study survey"""
        return self.survey_engine.administer({
            'satisfaction_baseline': 'How satisfied are you with your current movie recommendations?',
            'discovery_baseline': 'How often do you discover new movies you like?',
            'relevance_baseline': 'How relevant are the recommended movies to your interests?',
            'expectations': 'What are your expectations for psychology-based recommendations?'
        })
    
    def _post_study_survey(self, participant_id):
        """Post-study survey"""
        return self.survey_engine.administer({
            'satisfaction_final': 'How satisfied are you after using psychology-based recommendations?',
            'discovery_final': 'Has the frequency of discovering new favorite movies changed?',
            'relevance_final': 'Has the relevance of recommendations improved?',
            'psychological_accuracy': 'How accurate is the recommendation system\'s understanding of your psychological traits?',
            'explanation_helpfulness': 'Are the recommendation explanations helpful to you?',
            'privacy_concerns': 'Do you have privacy concerns about the use of psychological data?',
            'overall_experience': 'How was your overall experience?',
            'suggestions': 'What improvement suggestions do you have?'
        })
    
    def _analyze_study_results(self, results):
        """Analyze study results"""
        analysis = {
            'satisfaction_change': self._calculate_change(
                results['pre_study'], results['post_study'], 'satisfaction'
            ),
            'discovery_change': self._calculate_change(
                results['pre_study'], results['post_study'], 'discovery'
            ),
            'engagement_metrics': self._analyze_engagement(results['during_study']),
            'qualitative_insights': self._analyze_qualitative_feedback(results['post_study']),
            'statistical_significance': self._test_significance(results)
        }
        
        return analysis
'''



18.3 Bias and Fairness Testing

'''python
class FairnessTester:
    def __init__(self):
        self.fairness_metrics = FairnessMetrics()
        
    def comprehensive_fairness_audit(self, model, test_data):
        """Comprehensive fairness audit"""
        audit_results = {}
        
        # Personality type fairness
        audit_results['personality_fairness'] = self._test_personality_fairness(
            model, test_data
        )
        
        # Emotional state fairness
        audit_results['emotion_fairness'] = self._test_emotion_fairness(
            model, test_data
        )
        
        # Demographic fairness
        audit_results['demographic_fairness'] = self._test_demographic_fairness(
            model, test_data
        )
        
        # Intersectional fairness
        audit_results['intersectional_fairness'] = self._test_intersectional_fairness(
            model, test_data
        )
        
        return audit_results
    
    def _test_personality_fairness(self, model, test_data):
        """Test personality type fairness"""
        personality_groups = ['high_openness', 'low_openness', 'high_neuroticism', 
                            'low_neuroticism', 'high_extraversion', 'low_extraversion']
        
        group_metrics = {}
        for group in personality_groups:
            group_data = test_data[test_data['personality_group'] == group]
            predictions = model.predict(group_data)
            
            group_metrics[group] = {
                'accuracy': accuracy_score(group_data['actual'], predictions > 0.5),
                'precision': precision_score(group_data['actual'], predictions > 0.5),
                'recall': recall_score(group_data['actual'], predictions > 0.5),
                'sample_size': len(group_data)
            }
        
        # Calculate inter-group differences
        fairness_scores = {
            'accuracy_disparity': max(g['accuracy'] for g in group_metrics.values()) - 
                                 min(g['accuracy'] for g in group_metrics.values()),
            'equal_opportunity_diff': self._calculate_equal_opportunity_diff(group_metrics)
        }
        
        return {
            'group_metrics': group_metrics,
            'fairness_scores': fairness_scores,
            'is_fair': fairness_scores['accuracy_disparity'] < 0.1
        }
    
    def generate_fairness_report(self, audit_results):
        """Generate fairness report"""
        report = {
            'summary': self._generate_summary(audit_results),
            'detailed_findings': audit_results,
            'recommendations': self._generate_recommendations(audit_results),
            'action_items': self._generate_action_items(audit_results)
        }
        
        return report
'''

Nineteen, Future Research Directions



19.1 Emerging Technology Integration

**Large Language Model (LLM) Integration**

'''python
class LLMEnhancedRecommender:
    def __init__(self):
        self.llm_client = OpenAIClient()  # 或其他LLM
        self.psychology_engine = PsychologyEngine()
        
    async def generate_personalized_recommendation(self, user_id, context):
        """使用LLM生成個性化推薦"""
        user_psychology = self.psychology_engine.get_profile(user_id)
        
        prompt = f"""
        基於以下用戶心理特徵，推薦適合的電影：
        
        用戶心理檔案：
        - 開放性: {user_psychology['openness']}/5 (喜歡新奇事物的程度)
        - 神經質: {user_psychology['neuroticism']}/5 (情緒敏感度)
        - 認知需求: {user_psychology['need_cognition']}/10 (喜歡思考的程度)
        - 當前情緒: {context['current_mood']}
        - 觀影情境: {context['viewing_context']}
        
        請推薦3部電影，並解釋為什麼這些電影適合這位用戶。
        考慮用戶的心理特徵，提供個性化的推薦理由。
        """
        
        response = await self.llm_client.generate(prompt)
        
        # 解析LLM回應
        recommendations = self._parse_llm_recommendations(response)
        
        # 驗證推薦的合理性
        validated_recommendations = self._validate_recommendations(
            recommendations, user_psychology
        )
        
        return validated_recommendations
    
    async def generate_psychological_insight(self, user_id, movie_id):
        """生成心理學洞察"""
        user_psychology = self.psychology_engine.get_profile(user_id)
        movie_features = self.get_movie_features(movie_id)
        
        prompt = f"""
        分析這位用戶為什麼可能喜歡或不喜歡這部電影：
        
        用戶心理特徵：{user_psychology}
        電影特徵：{movie_features}
        
        請從心理學角度分析：
        1. 這部電影如何與用戶的人格特質匹配
        2. 可能引發的情緒反應
        3. 認知層面的體驗
        4. 潛在的治療價值或風險
        """
        
        insight = await self.llm_client.generate(prompt)
        
        return insight
'''

**Multimodal Emotion Computing**

'''python
class MultimodalEmotionComputer:
    def __init__(self):
        self.text_analyzer = TextEmotionAnalyzer()
        self.audio_analyzer = AudioEmotionAnalyzer()
        self.visual_analyzer = VisualEmotionAnalyzer()
        self.physiological_analyzer = PhysiologicalAnalyzer()
        
    def compute_comprehensive_emotion(self, user_data):
        """計算綜合情緒狀態"""
        emotions = {}
        
        # 文字情緒（評論、聊天）
        if 'text' in user_data:
            emotions['text'] = self.text_analyzer.analyze(user_data['text'])
        
        # 語音情緒（語音助手互動）
        if 'audio' in user_data:
            emotions['audio'] = self.audio_analyzer.analyze(user_data['audio'])
        
        # 視覺情緒（臉部表情）
        if 'video' in user_data:
            emotions['visual'] = self.visual_analyzer.analyze(user_data['video'])
        
        # 生理信號（穿戴設備）
        if 'physiological' in user_data:
            emotions['physiological'] = self.physiological_analyzer.analyze(
                user_data['physiological']
            )
        
        # 多模態融合
        fused_emotion = self._fuse_emotions(emotions)
        
        return fused_emotion
    
    def _fuse_emotions(self, emotions):
        """融合多模態情緒"""
        # 使用注意力機制融合
        weights = self._calculate_modality_weights(emotions)
        
        fused = {
            'valence': sum(e.get('valence', 0) * w for e, w in zip(emotions.values(), weights)),
            'arousal': sum(e.get('arousal', 0) * w for e, w in zip(emotions.values(), weights)),
            'dominance': sum(e.get('dominance', 0) * w for e, w in zip(emotions.values(), weights)),
            'confidence': self._calculate_fusion_confidence(emotions, weights),
            'modality_contributions': dict(zip(emotions.keys(), weights))
        }
        
        return fused
'''



19.2 Cross-Domain Application Extensions

'''python
class CrossDomainPsychologyRecommender:
    def __init__(self):
        self.domain_adapters = {
            'movies': MovieAdapter(),
            'music': MusicAdapter(),
            'books': BookAdapter(),
            'games': GameAdapter(),
            'podcasts': PodcastAdapter()
        }
        
    def transfer_psychology_profile(self, user_id, source_domain, target_domain):
        """Cross-domain psychology profile transfer"""
        # Retrieve psychology profile from source domain
        source_profile = self.domain_adapters[source_domain].get_psychology_profile(user_id)
        
        # Identify transferable psychological traits
        transferable_traits = self._identify_transferable_traits(
            source_profile, source_domain, target_domain
        )
        
        # Adapt to target domain
        adapted_profile = self.domain_adapters[target_domain].adapt_profile(
            transferable_traits
        )
        
        return adapted_profile
    
    def recommend_across_domains(self, user_id, primary_domain='movies'):
        """Cross-domain recommendations"""
        # Retrieve psychology profile from primary domain
        primary_profile = self.domain_adapters[primary_domain].get_psychology_profile(user_id)
        
        cross_domain_recommendations = {}
        
        for domain, adapter in self.domain_adapters.items():
            if domain != primary_domain:
                # Transfer psychology profile
                adapted_profile = self.transfer_psychology_profile(
                    user_id, primary_domain, domain
                )
                
                # Generate recommendations for that domain
                recommendations = adapter.recommend(adapted_profile)
                
                cross_domain_recommendations[domain] = {
                    'recommendations': recommendations,
                    'transfer_confidence': self._calculate_transfer_confidence(
                        primary_profile, adapted_profile
                    )
                }
        
        return cross_domain_recommendations
'''



19.3 Personalized Mental Health Support

'''python
class MentalHealthSupportRecommender:
    def __init__(self):
        self.mental_health_db = MentalHealthMovieDatabase()
        self.safety_checker = ContentSafetyChecker()
        
    def recommend_for_mental_health_support(self, user_id, support_goal):
        """Recommend movies for mental health support"""
        user_profile = self.get_user_profile(user_id)
        
        # Safety check
        if self._requires_professional_help(user_profile):
            return {
                'recommendations': [],
                'warning': 'It is recommended to seek professional mental health support',
                'resources': self._get_mental_health_resources()
            }
        
        # Select movies based on support goal
        if support_goal == 'stress_relief':
            movies = self._get_stress_relief_movies(user_profile)
        elif support_goal == 'mood_improvement':
            movies = self._get_mood_improvement_movies(user_profile)
        elif support_goal == 'anxiety_management':
            movies = self._get_anxiety_management_movies(user_profile)
        elif support_goal == 'self_reflection':
            movies = self._get_self_reflection_movies(user_profile)
        else:
            movies = self._get_general_wellbeing_movies(user_profile)
        
        # Add viewing guide
        for movie in movies:
            movie['viewing_guide'] = self._create_therapeutic_viewing_guide(
                movie, support_goal, user_profile
            )
            movie['safety_notes'] = self.safety_checker.get_safety_notes(
                movie, user_profile
            )
        
        return {
            'recommendations': movies,
            'support_goal': support_goal,
            'general_tips': self._get_general_wellbeing_tips()
        }
    
    def _create_therapeutic_viewing_guide(self, movie, goal, user_profile):
        """Create therapeutic viewing guide"""
        guide = {
            'preparation': {
                'environment': 'Choose a comfortable, quiet environment',
                'mindset': f'Watch with an open mindset, focusing on elements related to {goal}',
                'support': 'If needed, invite a trusted person to watch together'
            },
            'during_viewing': {
                'pacing': 'Pause anytime if you feel uncomfortable',
                'awareness': 'Notice your emotional responses',
                'grounding': 'Use grounding techniques if emotions become intense'
            },
            'after_viewing': {
                'reflection': self._get_reflection_prompts(movie, goal),
                'activities': self._get_post_viewing_activities(goal),
                'journaling': 'Record viewing feelings and insights'
            }
        }
        
        return guide
'''

Twenty, Summary and Outlook



20.1 Core Points Review

This guide covers the complete ecosystem of the psychology-based AI movie recommendation system:

**Theoretical Foundation**
- Big Five personality model as the core framework
- Advanced factors such as cognitive needs, attachment styles, early maladaptive schemas, etc.
- PAD emotion model and MOVIE movie preference model
- Self-determination theory, Maslow's hierarchy of needs, and other motivation theories

**Technical Implementation**
- Open-source frameworks such as TensorFlow Recommenders, LightFM, Surprise, etc.
- Advanced techniques like graph neural networks, reinforcement learning, causal inference, etc.
- Privacy protection technologies such as federated learning, differential privacy, etc.
- Multimodal deep learning architecture

**Application Scenarios**
- Streaming platform integration
- Education and corporate training
- Mental health support
- Cross-domain recommendation

**Ethical Considerations**
- Bias detection and mitigation
- Fairness testing
- Explainability framework
- Privacy protection



20.2 Implementation Recommendations

'''python
class ImplementationRoadmap:
    def __init__(self):
        self.phases = self._define_phases()
        
    def _define_phases(self):
        return {
            'phase_1': {
                'name': 'Infrastructure Setup',
                'duration': '1-2 months',
                'tasks': [
                    'Establish data collection pipeline',
                    'Implement basic Big Five questionnaire',
                    'Integrate LightFM basic recommendation',
                    'Establish evaluation framework'
                ],
                'success_metrics': [
                    'Data collection coverage > 50%',
                    'Basic recommendation RMSE < 1.0'
                ]
            },
            'phase_2': {
                'name': 'Psychology Integration',
                'duration': '2-3 months',
                'tasks': [
                    'Train personality prediction model',
                    'Implement emotion analysis pipeline',
                    'Establish psychology-movie matching rules',
                    'Conduct initial user testing'
                ],
                'success_metrics': [
                    'Personality prediction accuracy > 70%',
                    'User satisfaction improvement > 10%'
                ]
            },
            'phase_3': {
                'name': 'Advanced Optimization',
                'duration': '2-3 months',
                'tasks': [
                    'Implement multimodal fusion',
                    'Establish real-time emotion adaptation',
                    'Optimize explainability',
                    'Conduct A/B testing'
                ],
                'success_metrics': [
                    'Recommendation click-through rate improvement > 15%',
                    'User retention rate improvement > 10%'
                ]
            },
            'phase_4': {
                'name': 'Production Deployment',
                'duration': '1-2 months',
                'tasks': [
                    'Microservices architecture deployment',
                    'Establish monitoring system',
                    'Implement privacy protection',
                    'Conduct fairness audit'
                ],
                'success_metrics': [
                    'System availability > 99.9%',
                    'Response time < 200ms'
                ]
            }
        }
    
    def get_current_phase_tasks(self, current_phase):
        return self.phases.get(current_phase, {}).get('tasks', [])
'''



20.3 Future Outlook

The future development directions of the psychology AI movie recommendation system include:

1. **Deeper Psychology Integration**: Integrate more psychology theories, such as cognitive behavioral theory, positive psychology, etc.
2. **More Precise Emotion Computing**: Utilize multimodal perception technology to achieve more accurate emotion recognition
3. **Stronger Privacy Protection**: Develop more advanced federated learning and differential privacy technologies
4. **Broader Application Scenarios**: Expand to fields such as mental health support, education, corporate training, etc.
5. **More Responsible AI**: Establish more comprehensive bias detection and fairness assurance mechanisms

Appendix: Reference Resources



Open Source Frameworks and Tools
- TensorFlow Recommenders: [historical-url]
- LightFM: [historical-url]
- Surprise: [historical-url]
- PyTorch Geometric: [historical-url]
- Stable Baselines3: [historical-url]
- TensorFlow Privacy: [historical-url]
- TensorFlow Federated: [historical-url]
- CausalML: [historical-url]
- AIF360: [historical-url]



Psychology Resources
- Big Five Personality Test: [historical-url]
- Need for Cognition Scale: [historical-url]
- PAD Emotional State Model: [historical-url]



Datasets
- MovieLens: [historical-url]
- IMDb: [historical-url]
- Essays Dataset (Personality): [historical-url]



Academic Papers
- Personality and Recommender Systems
- An intelligent film recommender system based on emotional analysis
- Collaborative filtering recommendation system based on graph convolutional neural network
- Emotion-Based Movie Recommendation System



*This guide is continuously updated; contributions and feedback are welcome.*




Twenty-One, Integration of Neuropsychology and Brain Science



21.1 Application of Neuroaesthetics in Movie Recommendations

'''python
class NeuroaestheticsRecommender:
    def __init__(self):
        self.aesthetic_analyzer = AestheticResponseAnalyzer()
        
    def analyze_aesthetic_preferences(self, user_profile):
        """Analyze user's neuroaesthetic preferences"""
        preferences = {
            'visual_complexity': self._assess_visual_complexity_preference(user_profile),
            'color_palette': self._assess_color_preference(user_profile),
            'symmetry_preference': self._assess_symmetry_preference(user_profile),
            'novelty_seeking': self._assess_novelty_preference(user_profile),
            'emotional_intensity': self._assess_emotional_intensity_preference(user_profile)
        }
        return preferences
    
    def recommend_by_aesthetic_profile(self, user_id):
        """Recommend movies based on neuroaesthetic profile"""
        aesthetic_profile = self.analyze_aesthetic_preferences(
            self.get_user_profile(user_id)
        )
        
        recommendations = []
        
        # Visual complexity matching
        if aesthetic_profile['visual_complexity'] > 0.7:
            recommendations.extend(self._get_visually_complex_movies())
        else:
            recommendations.extend(self._get_minimalist_aesthetic_movies())
        
        # Color preference matching
        color_matched = self._match_color_palette(
            aesthetic_profile['color_palette']
        )
        recommendations.extend(color_matched)
        
        # Novelty matching
        if aesthetic_profile['novelty_seeking'] > 0.6:
            recommendations.extend(self._get_experimental_visual_movies())
        
        return self._rank_by_aesthetic_match(recommendations, aesthetic_profile)
    
    def _assess_visual_complexity_preference(self, profile):
        """Assess visual complexity preference"""
        # Based on visual style analysis from viewing history
        watched_movies = profile.get('watched_movies', [])
        complexity_scores = [
            self._get_movie_visual_complexity(m) for m in watched_movies
        ]
        return np.mean(complexity_scores) if complexity_scores else 0.5
'''



21.2 Mirror Neuron Theory Application

'''python
class MirrorNeuronRecommender:
    def __init__(self):
        self.empathy_analyzer = EmpathyAnalyzer()
        
    def assess_empathy_profile(self, user_profile):
        """Assess user's empathy profile"""
        empathy_dimensions = {
            'cognitive_empathy': self._assess_cognitive_empathy(user_profile),
            'affective_empathy': self._assess_affective_empathy(user_profile),
            'motor_empathy': self._assess_motor_empathy(user_profile)
        }
        return empathy_dimensions
    
    def recommend_for_empathy_development(self, user_id):
        """Recommend movies to promote empathy development"""
        empathy_profile = self.assess_empathy_profile(
            self.get_user_profile(user_id)
        )
        
        recommendations = []
        
        # Low cognitive empathy - Recommend movies showcasing different perspectives
        if empathy_profile['cognitive_empathy'] < 0.5:
            recommendations.extend(self._get_perspective_taking_movies())
        
        # Low affective empathy - Recommend emotionally rich character-driven movies
        if empathy_profile['affective_empathy'] < 0.5:
            recommendations.extend(self._get_emotionally_rich_movies())
        
        # Motor empathy - Recommend movies rich in action and physical expression
        if empathy_profile['motor_empathy'] < 0.5:
            recommendations.extend(self._get_physical_expression_movies())
        
        return recommendations
    
    def _get_perspective_taking_movies(self):
        """Get movies that promote perspective-taking"""
        return self.movie_db.query({
            'narrative_style': ['multiple_perspectives', 'unreliable_narrator'],
            'themes': ['cultural_diversity', 'social_issues', 'marginalized_voices']
        })
'''



21.3 Memory and Nostalgia Psychology

'''python
class NostalgiaRecommender:
    def __init__(self):
        self.nostalgia_analyzer = NostalgiaAnalyzer()
        
    def analyze_nostalgia_triggers(self, user_profile):
        """Analyze user's nostalgia triggers"""
        triggers = {
            'era_nostalgia': self._identify_era_preferences(user_profile),
            'personal_nostalgia': self._identify_personal_triggers(user_profile),
            'cultural_nostalgia': self._identify_cultural_triggers(user_profile),
            'sensory_nostalgia': self._identify_sensory_triggers(user_profile)
        }
        return triggers
    
    def recommend_for_nostalgia(self, user_id, nostalgia_type='balanced'):
        """Recommend movies based on nostalgia psychology"""
        triggers = self.analyze_nostalgia_triggers(
            self.get_user_profile(user_id)
        )
        
        recommendations = []
        
        if nostalgia_type == 'therapeutic':
            # Therapeutic nostalgia - warm, positive memories
            recommendations = self._get_warm_nostalgia_movies(triggers)
        elif nostalgia_type == 'reflective':
            # Reflective nostalgia - promotes self-understanding
            recommendations = self._get_reflective_nostalgia_movies(triggers)
        elif nostalgia_type == 'anticipatory':
            # Anticipatory nostalgia - creates future good memories
            recommendations = self._get_memory_making_movies(triggers)
        else:
            # Balanced recommendations
            recommendations = self._get_balanced_nostalgia_movies(triggers)
        
        return recommendations
    
    def _get_warm_nostalgia_movies(self, triggers):
        """Get warm nostalgia movies"""
        era = triggers['era_nostalgia']
        return self.movie_db.query({
            'release_era': era,
            'tone': ['warm', 'hopeful', 'comforting'],
            'themes': ['childhood', 'family', 'friendship', 'simpler_times']
        })
'''

Twenty-Two, Emotional Regulation Strategy Integration



22.1 Application of Emotion Regulation Theory

'''python
class EmotionRegulationRecommender:
    def __init__(self):
        self.regulation_analyzer = EmotionRegulationAnalyzer()
        
    def identify_regulation_strategy(self, user_behavior):
        """Identify user's emotion regulation strategy"""
        strategies = {
            'situation_selection': self._assess_situation_selection(user_behavior),
            'situation_modification': self._assess_situation_modification(user_behavior),
            'attentional_deployment': self._assess_attentional_deployment(user_behavior),
            'cognitive_change': self._assess_cognitive_change(user_behavior),
            'response_modulation': self._assess_response_modulation(user_behavior)
        }
        return strategies
    
    def recommend_for_regulation(self, user_id, target_emotion=None):
        """Recommend movies based on emotion regulation needs"""
        current_state = self.get_current_emotional_state(user_id)
        regulation_style = self.identify_regulation_strategy(
            self.get_user_behavior(user_id)
        )
        
        recommendations = []
        
        if current_state['valence'] < 0.3:  # Negative emotion
            if regulation_style['cognitive_change'] > 0.6:
                # Cognitive reappraisal type - Recommend movies providing new perspectives
                recommendations.extend(self._get_reappraisal_movies())
            elif regulation_style['attentional_deployment'] > 0.6:
                # Attentional deployment type - Recommend immersive entertainment
                recommendations.extend(self._get_immersive_distraction_movies())
            else:
                # Default - Recommend gentle uplifting content
                recommendations.extend(self._get_gentle_uplifting_movies())
        
        return recommendations
    
    def _get_reappraisal_movies(self):
        """Get movies that promote cognitive reappraisal"""
        return self.movie_db.query({
            'themes': ['perspective_shift', 'growth_mindset', 'overcoming_adversity'],
            'narrative_style': ['transformative_arc', 'redemption']
        })
'''



22.2 Emotional Contagion and Social Emotional Learning

'''python
class EmotionalContagionRecommender:
    def __init__(self):
        self.contagion_analyzer = EmotionalContagionAnalyzer()
        
    def assess_contagion_susceptibility(self, user_profile):
        """Assess user's emotional contagion susceptibility"""
        susceptibility = {
            'positive_contagion': self._assess_positive_susceptibility(user_profile),
            'negative_contagion': self._assess_negative_susceptibility(user_profile),
            'emotional_boundary': self._assess_emotional_boundary(user_profile)
        }
        return susceptibility
    
    def recommend_with_contagion_awareness(self, user_id):
        """Recommendations considering emotional contagion"""
        susceptibility = self.assess_contagion_susceptibility(
            self.get_user_profile(user_id)
        )
        current_mood = self.get_current_mood(user_id)
        
        recommendations = []
        
        # High negative emotional contagion susceptibility + current low mood
        if susceptibility['negative_contagion'] > 0.7 and current_mood['valence'] < 0.4:
            # Avoid sad, heavy movies
            recommendations = self._get_emotionally_safe_movies()
            recommendations = self._filter_heavy_emotional_content(recommendations)
        
        # High positive emotional contagion susceptibility
        if susceptibility['positive_contagion'] > 0.7:
            # Recommend movies that transmit positive energy
            recommendations.extend(self._get_positive_contagion_movies())
        
        return recommendations
    
    def _get_positive_contagion_movies(self):
        """Get movies that transmit positive emotions"""
        return self.movie_db.query({
            'emotional_tone': ['joyful', 'inspiring', 'heartwarming'],
            'character_emotions': ['happiness', 'hope', 'love', 'triumph'],
            'ending_type': ['positive', 'hopeful']
        })
'''



22.3 Stress Coping and Resilience

'''python
class ResilienceRecommender:
    def __init__(self):
        self.resilience_analyzer = ResilienceAnalyzer()
        
    def assess_resilience_factors(self, user_profile):
        """Assess user's resilience factors"""
        factors = {
            'optimism': self._assess_optimism(user_profile),
            'self_efficacy': self._assess_self_efficacy(user_profile),
            'social_support': self._assess_social_support(user_profile),
            'emotion_regulation': self._assess_emotion_regulation(user_profile),
            'meaning_making': self._assess_meaning_making(user_profile)
        }
        return factors
    
    def recommend_for_resilience_building(self, user_id):
        """Recommend movies that promote resilience"""
        resilience_profile = self.assess_resilience_factors(
            self.get_user_profile(user_id)
        )
        
        # Find the resilience factor that needs the most improvement
        weakest_factor = min(resilience_profile, key=resilience_profile.get)
        
        recommendations = []
        
        if weakest_factor == 'optimism':
            recommendations.extend(self._get_optimism_building_movies())
        elif weakest_factor == 'self_efficacy':
            recommendations.extend(self._get_self_efficacy_movies())
        elif weakest_factor == 'social_support':
            recommendations.extend(self._get_connection_movies())
        elif weakest_factor == 'meaning_making':
            recommendations.extend(self._get_meaning_exploration_movies())
        
        return recommendations
    
    def _get_optimism_building_movies(self):
        """Get movies that cultivate optimism"""
        return self.movie_db.query({
            'themes': ['hope', 'perseverance', 'silver_lining', 'second_chances'],
            'character_arc': ['growth', 'transformation', 'triumph_over_adversity'],
            'tone': ['hopeful', 'uplifting', 'inspiring']
        })
'''






Additional corpus / va passages naming this agent


From `corpus/study/SYSTEM_REFERENCE.md` Copy: `sources/excerpts/SYSTEM_REFERENCE.md`.


| Capability | What It Provides | Used By | Specification |
|-----------|-----------------|---------|---------------|
| **Strategic Goal Achievement Framework** | 6-stage self-inquiry system for transforming vague goals into actionable plans | All planning agents (PlannerAgent, ProducerAgent, DirectorAgent) | [strategic_goal_achievement_agent_functional_specification.md](./strategic_goal_achievement_agent_functional_specification.md) |
| **Screenwriter Goal Achievement** | Practical demonstration of goal framework applied to creative writing | ScreenwriterAgent, ShowrunnerAgent, ComedyWriterAgent | [screenwriter_strategic_goal_achievement_agent_functional_specification.md](./screenwriter_strategic_goal_achievement_agent_functional_specification.md) |
| **Psychological Profiling** | 100 creator profiles with MBTI, motivations, fears, creative parameters | CastingAgent, TalentAgent, PersonalizationEngineerAgent, UGCCreatorAgent | [psychological_profile_agent_functional_specifications.md](./psychological_profile_agent_functional_specifications.md) |
| **Psychological Recommendation** | Psychology-based preference prediction (Big Five, emotional state) | AudienceSimAgent, PerformanceMarketerAgent, PersonalizationEngineerAgent | [psychological_recommendation_agent_functional_specification.md](./psychological_recommendation_agent_functional_specification.md) |
| **Complex Problem Solving** | WHAT/WHY/HOW/DO/REVIEW structured methodology | All diagnostic agents (FactCheckerAgent, SMEAgent, JudgeAgent, OptimizationAgent) | [complex_problem_solution_process_model.md](./complex_problem_solution_process_model.md) |
| **Common Agent Structure** | Shared architectural pattern for all agents | All 114 agents | [common-agent-structure.svg](./common-agent-structure.svg) + [common-agent-structure.html](./common-agent-structure.html) |



From `corpus/study/ai_agent_video_production_workflow.md` Copy: `sources/excerpts/ai_agent_video_production_workflow.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 1 | **DirectorAgent** | Owns vision; issues shot intents, sets pacing, approves takes | Criterion commentary tracks; IMDb Top 250 director interviews; DGA seminars; MasterClass corpora (Scorsese/Lynch/Gerwig) | Shot-intent fidelity (CLIP-T ≥0.32); story-beat coverage 100%; pacing curve matches genre prior | Wins ≥55% blind pairwise vs DGA director's cuts of same screenplay (Arena protocol) | ScreenwriterAgent (story beats), EditorAgent (pacing), Audience-Sim Agent (test screenings) — via structured JSON critique bus | EditorAgent, DoPAgent, ScreenwriterAgent, ComposerAgent — issues "creative-intent diff" |
| 2 | **ProducerAgent / EP** | Budget, schedule, hiring, delivery; greenlights phase gates | PGA Producers Mark guidelines; Variety/Deadline budget leaks; LineProducer Excel corpora | On-time delivery rate; budget variance <±5%; talent satisfaction (RLHF score) | Beats PGA-credited producer schedules at 0.6× cost with equal CSAT | All downstream agents (escalations); HumanInTheLoop gate for final greenlight | DirectorAgent (scope creep), AllAgents (resource burn) |
| 3 | **ScreenwriterAgent** | Treatment → screenplay; dialogue; structure | Black List scripts; WGA library; McKee *Story*; Truby *Anatomy of Story*; transcribed Charlie Kaufman / Sorkin interviews | Save-the-Cat beat sheet pass; dialogue distinctiveness (per-character embedding distance ≥τ); rewrite delta from notes | Wins ≥50% blind read vs Black List Top-10 scripts (WGA judge panel emulated) | DirectorAgent, DramaturgAgent, StoryEditorAgent — Reflexion loop on notes | DirectorAgent (logline clarity), DialogueAgent, ConsistencyAgent |
| 4 | **ShowrunnerAgent** | Cross-episode arc, writers'-room orchestration | WGA showrunner training; Sopranos/Breaking Bad room transcripts; Mike Schur teaching material | Arc continuity score across episodes; character-thread completion; tonal variance within bounds | Series Bible coverage ≥99% across 10 eps without drift (vs ~95% human baseline) | Network-Notes Agent, AudienceSim, Multi-agent debate w/ ScreenwriterAgent | ScreenwriterAgent (arc), CastingAgent, DirectorAgent (episode tone) |
| 5 | **CastingAgent** | Voice + likeness selection and audition simulation | CSA Artios archive; SAG-AFTRA AI rider; voice-actor corpora (consented) | Character-voice fit (audience preference); SAG-AFTRA AI consent compliance 100% | Beats CSA casting in blind audience preference for fit; faster turnaround (hours vs weeks) | DirectorAgent, ShowrunnerAgent, Legal/ConsentAgent | VoiceCloneAgent (likeness), AvatarDesignAgent |

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
| 23 | **ChoreographyAgent** | Movement design (music videos, dance challenges) | Emmy Choreography submissions; Parris Goebel/Mandy Moore reels; dance-notation datasets | Beat-sync accuracy; safety constraints; viral-pattern alignment | Wins blind preference vs choreographer drafts for short-form | DirectorAgent, MVDirectorAgent | DirectorAgent (un-camera-friendly staging) |
| 24 | **MusicVideoDirectorAgent** | Visual concept for songs | DirectorsLibrary.com; UKMVA/MTV VMA winners; Hype Williams / Spike Jonze reels | Edit-rhythm sync; lookbook coherence; artist-brief fit | Wins label-blind preference vs commercial MV director shortlist | LabelA&RAgent, ArtistAgent | EditorAgent (cut on beat), DoPAgent |
| 25 | **ComedyWriterAgent** | Skits, parody, viral meme writing | UCB/Groundlings manuals; SNL writers'-room transcripts; Schur/Fey teaching | Joke-density; cold-open hook strength; predicted laughs/min | Beats UCB-table-read win rate on cold-reads | AudienceSim, ShowrunnerAgent | ScriptwriterAgent (no joke), SocialStrategistAgent (off-trend) |
| 26 | **TalentAgent (On-camera)** | AI-rendered performance | Method-acting transcripts; consented actor performance corpora | Emotion-target match; charisma score (audience proxy) | Hold-rate matches top creators in cohort | DirectorAgent, CastingAgent | DirectorAgent (impossible blocking) |
| 27 | **UGCCreatorAgent** | Authentic-feel ads in creator voice | TikTok Creative Center reports; Alix-Earle-style benchmark posts (style not identity) | Hook-rate ≥30%; "scripted" detector score below threshold (low = good) | Beats paid-creator avg ROAS at 0.1× cost | PerformanceMarketerAgent, BrandAgent | PerformanceMarketerAgent (wrong audience) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 73 | **PromptOptimizerAgent** | Auto-improves prompts via OPRO / APE / DSPy / Promptbreeder | OPRO (Yang 2023), APE (Zhou 2022), DSPy (Stanford), Promptbreeder (DeepMind) | Score uplift per iteration on held-out eval; iteration count to convergence | Beats Karen X. Cheng / Paul Trillo-style hand-tuned prompts on held-out briefs | PromptEngineerAgent, AIQAAgent | PromptEngineerAgent (sub-optimal seed) |
| 74 | **CostOptimizerAgent** | Routes between models / providers for $/quality | Provider pricing sheets; benchmark cost-quality frontiers; FrugalGPT patterns | $/successful-task; Pareto distance from cost-quality frontier | Lower $/quality than human CFO + producer routing decisions | RouterAgent, FinanceAgent | RouterAgent (over-spend), GeneratorAgent (re-roll burn) |
| 75 | **LatencyOptimizerAgent** | Parallelization, caching, speculative decoding, batch packing | vLLM, TensorRT-LLM, distillation literature; Anyscale/Ray patterns | p50/p95 latency; throughput per GPU-hour | Lower p95 than human-tuned pipeline at equal quality | OrchestratorAgent | OrchestratorAgent (serial bottleneck) |
| 76 | **RetentionOptimizerAgent** | Tunes hook, pacing, structure for AVD / hold-rate | YouTube Analytics public benchmarks; TikTok retention curves; AudienceSim outputs | Predicted retention curve vs actual; AVD lift over control | Beats senior YouTube editor on AVD lift in A/B | EditorAgent, AudienceSimAgent | EditorAgent (slow opener), ScriptwriterAgent (front-loaded fluff) |
| 77 | **ROASOptimizerAgent** | Optimizes ad creatives for performance metrics | Meta Marketing Science, TikTok Ads Academy, MMM/MTA literature | ROAS uplift vs control; significance ≥95% | Beats senior performance marketer at equal budget | PerformanceMarketerAgent, AnalystAgent | UGCAgent (low hook-rate), CopywriterAgent (weak CTA) |
| 78 | **AccessibilityOptimizerAgent** | WCAG 2.2 contrast, caption timing, audio description quality, color-blind safe palette | WCAG 2.2 spec; W3C/WAI-ARIA; DCMP captioning key; Deaf/HoH community guidelines | WCAG-conformance score 100% AA, ≥90% AAA; caption WER ≤2% | Catches more a11y defects than ADA-certified human auditor | AccessibilityAgent (HiTL), ComplianceAgent | EditorAgent (caption sync), ColoristAgent (contrast) |
| 79 | **EvaluationHarnessAgent** | Continuously runs benchmarks (VBench, EvalCrafter, MT-Bench, FVD, CLIP-T) and posts regressions | Papers-with-Code; HuggingFace leaderboards; benchmark code repos | Regression detection precision/recall; alert latency <1h | Catches regressions faster than ML-eng team rotation | BenchmarkResearchAgent | All AI agents (regression alerts) |
| 80 | **S
…



From `corpus/study/lifes_quiet_redemption_agent_workflow.md` Copy: `sources/excerpts/lifes_quiet_redemption_agent_workflow.md`.


| Agent (#) | Service on This Film | Consumes | Produces | Tools | Self-Quality Bar | Critiqued By |
|---|---|---|---|---|---|---|
| DirectorAgent (#1) | Owns the warm, reflective vision; issues shot intents, approves takes | Storyboard, refs | Per-shot creative intent, approvals | Veo/Kling/Runway, Resolve (MCP) | Shot-intent fidelity (CLIP-T ≥0.32) | ScreenwriterAgent, EditorAgent, AudienceSimAgent |
| ScreenwriterAgent (#3) | Polishes the 旁白 into a continuous, rhythmic narration script | Treatment, beat sheet | Final VO script (ZH + EN) | Fountain/FDX, embedding distance | Beat pass; line distinctiveness | DirectorAgent, NoveltyAgent |
| General Creative Agent (SSOR) | Supplies fresh framings, metaphors (map → real place, recurring cat) | Brief, mood | Creative options, motifs | SSOR ideation engine | Novelty at equal coherence | DirectorAgent, NoveltyAgent |
| IdeationAgent (#59) | Divergent options for hooks, taglines, ending-card phrasing | Theme | Concept/hook set | Novelty scorer, concept clustering | Idea density, semantic diversity | CreativeDirectorAgent, NoveltyAgent |
| NarrativeArcAgent (#60) | Validates the youth→build→accept→grace arc spacing | Storyboard | Beat-sheet coverage map | Beat-sheet validator, arc plotter | Coverage 100%; turning-point spacing | ScreenwriterAgent |
| EmotionalArcAgent (#65) | Maps valence/arousal so each 旁白 lands on the visual peak | Storyboard, VO | Emotion curve + beat suggestions | GoEmotions, retention predictor | Curve fit to target | EditorAgent, ComposerAgent |
| NoveltyAgent (#64) | Flags clichés in visuals/lines (e.g., over-used "city dreamer" tropes) | Drafts | Cliché-hit report | TV Tropes, n-gram DB, novelty scorer | Cliché count below τ | ScreenwriterAgent |
| StoryboardAgent (#14) | Converts script to the 12-panel shot table with staging | Script | Shot panels + staging notes | Image-gen, Fountain parser | Coverage completeness, staging clarity | DirectorAgent |
| MoodBoardAgent (#63) | Builds visual/sonic/tonal reference boards (golden hour, film grain) | Brief | Lookbook boards | Pinterest/Are.na, CLIP clustering | Reference coherence | DirectorAgent, ProductionDesignAgent |

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

| Service / Capability | Provided By | Role on This Film |
|---|---|---|
| **Aesthetics scoring (Critic + Aligner + Taste-Keeper)** | Aesthetics Agent | Supplies the L2/perceptual "is this beautiful + warm?" judge signal to Cinematographer, Colorist, PromptEngineer, AIQA |
| **Strategic Goal Achievement (6-stage self-inquiry)** | Strategic Goal framework | Turns the vague "make people feel life saved them" goal into measurable creative targets for Planner/Director |
| **Agentic RAG knowledge backbone** | Agentic RAG System | Serves Chinese cinematic references, golden-hour lighting recipes, prompt patterns to any agent on demand |
| **Psychological profiling / recommendation** | Psych Profile + Recommendation agents | Tunes narrator tone and audience-resonance prediction (Big Five / emotional state) for AudienceSim and Personalization |
| **Continuous self-improvement (Reflexion + RLAIF)** | Optimization Agent + EvaluationHarnessAgent (#79) | Feeds 30/60/90-day retention/ROAS back into prompt + edit choices for the next film in the series |
| **Shared Artifact Handoff Contract (C2PA-signed manifests)** | All agents | Every clip, stem, and master carries `artifact_id`, `continuity_state`, `qc_status`, `provenance_manifest` between phases |
| **Critique Bus (CritiqueMessage JSON)** | All agents | Structured blocker/major/minor feedback; disputes escalate to JudgeAgent → HiTL |

| Layer | Question | Owner / Mechanism | Threshold |
|---|---|---|---|
| **L1 — Spec** | Did it meet the structured brief (codec, aspect, duration, frame count)? | JSON schema + tool validators | 100% pass |
| **L2 — Rubric** | Does it meet the craft rubric (composition, grade, prosody, beat fit)? | LLM-as-Judge + Aesthetics Agent | ≥85/100 (≤3 Self-Refine iters) |
| **L3 — Preference** | Would the target audience pick this over a human-made baseline? | AudienceSimAgent (#82) pairwise panel + HiTL sample | Win ≥50% (parity) / ≥55% (surpass) |

| Upgrade | What Changes | Owning Agents | Gate / Metric |
|---|---|---|---|
| **Package-first** | Title (≤50 chars, simple words) + thumbnail concept are locked in Phase 1, *before* any generation; the film is made to deliver that promise | BrandStrategistAgent (#85), SEOAgent (#87), Thumbnail=ConceptArtistAgent (#15), DirectorAgent (#1) | CTR predicted ≥ niche median (AudienceSimAgent panel) |
| **Outlier modeling** | Idea is chosen by modeling over-performing videos in the 治愈/reflective-life niche | TrendIntelligenceAgent (#68), AnalystAgent (#81), IdeationAgent (#59) | Idea maps to ≥3 proven outliers |
| **Engineered opener** | First 3–5s re-cut as a hook: strongest image (Scene 1 ECU or Scene 10 warmth) + a curiosity-gap 旁白 line, instead of a slow fade-in | RetentionOptimizerAgent (#76), EditorAgent (#9), ScreenwriterAgent (#3) | First-60s retention ≥ target band |
| **Segment retention bands** | Map the 60s into hook / build / payoff with explicit retention floors per segment, modeled on MrBeast's segmentation | RetentionOptimizerAgent (#76), EmotionalArcAgent (#65) | Per-segment predicted retention ≥ floor |
| **Shorts 3s-hold cut** | Dedicated 9:16 cut: visual hook on **frame 1**, spoken hook ≤14 words, designed to loop | TrailerEditorAgent (#51), MotionGraphicsAgent (#13) | Predicted 3s-hold ≥60%; clean loop seam |
| **Metric instrumentation** | Track CTR + AVD + AVP as first-class KPIs feeding the next episode | AnalystAgent (#81), EvaluationHarnessAgent (#79) | Dashboard live within 24h of launch |



From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


| API | Layer | Mechanism | Pass |
|-----|-------|-----------|------|
| `qc.l1_spec(artifact)` | Spec | JSON-schema + tool validators (codec/LUFS/aspect/length) | 100% |
| `qc.l2_rubric(artifact, rubric)` | Rubric | LLM-as-judge w/ role constitution | ≥85/100 |
| `qc.l3_preference(artifact, baseline)` | Preference | Pairwise vs human ref + AudienceSim ≥200 personas + ≥20 HiTL | ≥0.50 parity / ≥0.55 surpass |
| `qc.delivery(artifact)` | Q1–Q6 | spec / artifact / audio-sync / continuity / perceptual / outlet-readiness | all 6 pass |

**Build:**
- **Agent Factory** (`packages/agent-factory`): `AgentConfig (YAML) → runnable BaseAgent`. Validates prompt/rubric/tools/QC refs; registers into `agents/_registry.yaml`; generates the per-agent test skeleton. This is the engine for M7–M9.
- **Workflow A craft agents** (subset, via factory): TrendIntelligenceAgent, CopywriterAgent, SocialMediaStrategistAgent, PromptEngineerAgent/GeneratorOperator, AIQAConsistencyAgent, EditorAgent, AccessibilityOptimizerAgent, AudienceSimAgent, AnalystAgent — exactly the crew in [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §3.1.
- **Workflow A DAG** (`workflows/A_viral_hook.py`): Concept → Production → Post → Review → Distribution → Post-launch, with the spec'd critic gates.
- End-to-end run: brief → DIA → Planner builds the A-DAG → agents execute (mock gen) → artifacts flow with handoff contract → critique bus active → QC mesh gates → C2PA-signed deliverable → events on the bus.

**Build:**
- **Orchestration (53–58):** harden Orchestrator/Planner/Router/Judge/GateKeeper/Memory with full dispute-resolution (multi-agent debate), stage-gate sign-off, and escaped-defect=0 discipline.
- **Creative (59–65):** Ideation, NarrativeArc, StyleTransfer, MoodBoard, Novelty/Anti-Cliché, EmotionalArc, WorldBuilding — many delegate to GCA/Aesthetics (no duplication).
- **Research (66–72):** Web/Archive/Trend/Competitor/Citation/InterviewSynthesis/Benchmark — built on the M4 Research Agent core.
- **Optimization (73–80):** Prompt/Cost/Latency/Retention/ROAS/Accessibility optimizers + EvaluationHarness + SafetyRedTeam.
- **Full QC mesh**: complete L3 (AudienceSim ≥200 personas + HiTL sampling) and Q1–Q6 delivery validators; `GateKeeperAgent` enforces "zero leaked defects."

**Tests:** Judge inter-rater agreement κ≥0.8 vs a fixture human-panel; GateKeeper blocks a seeded defect; SafetyRedTeam attack-success ≤1% on the seeded attack set; EvaluationHarness detects an injected regression <1h; AudienceSim L3 win-rate computed on a golden pair.

**Build:**
- **Psychological Profiling** (100 creator profiles: MBTI, motivations, fears, creative params) → feeds Casting/Talent/Personalization/UGC agents and Aesthetic-Agent *audience-cohort profiles*.
- **Psychological Recommendation** (Big Five / emotional-state preference prediction) → AudienceSim, PerformanceMarketer, Personalization.
- **PersonalizationEngineerAgent** templating (name/face/voice swap) with privacy/consent audit (GDPR/CCPA via ComplianceAgent).
- **Podcast Agent** audio-first workflow (preparation → execution → ending → follow-up), reusing VO/SoundMixer/Editor.

9.4 Behavioral / golden-set evaluation (the L1/L2/L3 mesh on the system itself)
- **Golden sets** in `eval/golden/`: frozen brief→expected fixtures per agent and per workflow. Inputs and expected structured outputs are version-controlled.
- **L2 judges are frozen + pinned** (specific model + prompt version) to keep scores stable across runs; never let a judge model float (regression-noise killer).
- **L3 AudienceSim**: ≥200 simulated personas (from Psychological Profiling, M11) + ≥20 HiTL samples; reports win-rate vs the stored human/baseline reference.
- **`EvaluationHarnessAgent` (#79)** runs these nightly and on every PR touching an agent; posts regressions to `system.alerts`.

Theme 4 — Quality Mesh (31–40)
31. `qc.release_ok()` is the single release predicate; GateKeeper calls only it.
32. L1 deterministic validators cover codec/aspect/duration/frame-rate/LUFS/captions.
33. L2 judges are pinned (model+prompt version); score variance within tolerance across reruns.
34. L3 AudienceSim uses ≥200 personas + ≥20 HiTL; win-rate computed correctly.
35. Q1–Q6 delivery mesh each implemented and gating.
36. Continuity (Q4) detects identity/wardrobe/prop drift via `identity_hash`.
37. Aesthetic scoring returns decomposed vector + `hack_likelihood`; low confidence escalates.
38. Reward-hacking defenses active (ensemble disagreement, variance monitoring).
39. Accessibility (WCAG 2.2 AA min) gated for any human-facing output.
40. A seeded defect is reliably caught and blocked before release.



From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **DirectorAgent** | Owns vision; issues shot intents, sets pacing, approves takes | Criterion commentary; IMDb Top 250 director interviews; DGA seminars; MasterClass (Scorsese/Lynch/Gerwig) | Shot-intent fidelity (CLIP-T ≥0.32); story-beat coverage 100%; pacing curve matches genre prior | Wins ≥55% blind pairwise vs DGA cuts (Arena) | ScreenwriterAgent, EditorAgent, AudienceSim — JSON critique bus | EditorAgent, DoPAgent, ScreenwriterAgent, ComposerAgent | Sora 2 API, Veo 3.1 (Gemini API), Runway Gen-4, Kling 3.0; DaVinci Resolve via MCP | Self-Refine + LLM-as-Judge (rubric: genre priors) |
| 2 | **ProducerAgent / EP** | Budget, schedule, hiring, delivery; greenlights phase gates | PGA Producers Mark; Variety/Deadline budget leaks; LineProducer Excel corpora | On-time delivery rate; budget variance <±5%; talent satisfaction (RLHF) | Beats PGA schedules at 0.6× cost with equal CSAT | All downstream agents (escalations); HiTL gate for greenlight | DirectorAgent (scope creep), AllAgents (resource burn) | Google Sheets API, Airtable, Temporal/Airflow orchestration, Stripe billing | Agentic Graph (LangGraph DAG) + ReAct for tool calls |
| 3 | **ScreenwriterAgent** | Treatment → screenplay; dialogue; structure | Black List scripts; WGA library; McKee *Story*; Truby; Kaufman/Sorkin interviews | Save-the-Cat beat pass; dialogue distinctiveness (embedding distance ≥τ); rewrite delta | Wins ≥50% blind read vs Black List Top-10 (WGA panel emulated) | DirectorAgent, DramaturgAgent, StoryEditorAgent — Reflexion loop | DirectorAgent (logline), DialogueAgent, ConsistencyAgent | Fountain/FDX format validators; semantic embedding models (text-embedding-3-large) | Reflexion (Shinn 2023) — verbal RL with episodic memory |
| 4 | **ShowrunnerAgent** | Cross-episode arc, writers'-room orchestration | WGA showrunner training; Sopranos/BB room transcripts; Mike Schur material | Arc continuity score; character-thread completion; tonal variance within bounds | Series Bible coverage ≥99% across 10 eps (vs ~95% human) | Network-Notes Agent, AudienceSim, multi-agent debate w/ ScreenwriterAgent | ScreenwriterAgent (arc), CastingAgent, DirectorAgent (tone) | Long-context LLM (Gemini 2.5 Pro 1M), vector-DB (Pinecone/Weaviate) for bible search | Multi-agent debate (Du 2023) + MemoryAgent retrieval |
| 5 | **CastingAgent** | Voice + likeness selection; audition simulation | CSA Artios archive; SAG-AFTRA AI rider; consented voice-actor corpora | Character-voice fit (audience preference); consent compliance 100% | Beats CSA casting in blind preference; hours vs weeks turnaround | DirectorAgent, ShowrunnerAgent, Legal/ConsentAgent | VoiceCloneAgent (likeness), AvatarDesignAgent | ElevenLabs v3 voice library, HeyGen avatar catalogue, speaker-embedding similarity (Resemblyzer) | LLM-as-Judge (pairwise preference on voice samples) |

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
| 23 | **ChoreographyAgent** | Movement design (MVs, dance challenges) | Emmy Choreography submissions; Goebel/Moore reels; dance-notation datasets | Beat-sync accuracy; safety constraints; viral-pattern alignment | Wins blind preference vs choreographer drafts | DirectorAgent, MVDirectorAgent | DirectorAgent (un-camera-friendly staging) | Kling 3.0 motion control (reference video); Cascadeur; beat-detection (librosa) | Self-Refine (rubric: beat-sync + safety) |
| 24 | **MusicVideoDirectorAgent** | Visual concept for songs | DirectorsLibrary; UKMVA/MTV VMA winners; Hype Williams/Spike Jonze | Edit-rhythm sync; lookbook coherence; artist-brief fit | Wins label-blind preference vs commercial MV shortlist | LabelA&RAgent, ArtistAgent | EditorAgent (cut on beat), DoPAgent | Runway Gen-4 (style-locked generation); Veo 3.1; mood-board tools (Are.na API) | Multi-agent debate (with DirectorAgent + EditorAgent) |
| 25 | **ComedyWriterAgent** | Skits, parody, viral meme writing | UCB/Groundlings manuals; SNL transcripts; Schur/Fey teaching | Joke-density; cold-open hook strength; predicted laughs/min | Beats UCB-table-read win rate on cold-reads | AudienceSim, ShowrunnerAgent | ScriptwriterAgent (no joke), SocialStrategistAgent (off-trend) | Audience laugh-prediction model; trending-audio API (TikTok Creative Center) | Reflexion (stores audience feedback in episodic memory) |
| 26 | **TalentAgent (On-camera)** | AI-rendered performance | Method-acting transcripts; consented actor performance corpora | Emotion-target match; charisma score (audience proxy) | Hold-rate matches top creators in cohort | DirectorAgent, CastingAgent | DirectorAgent (impossible blocking) | HeyGen Avatar IV; Synthesia personal avatars; emotion-detection models (AffectNet) | Self-Refine + emotion-regression validator |
| 27 | **UGCCreatorAgent** | Authentic-feel ads in creator voice | TikTok Creative Center; Alix-Earle-style benchmarks (style not identity) | Hook-rate ≥30%; "scripted" detector < threshold | Beats paid-creator avg ROAS at 0.1× cost | PerformanceMarketerAgent, BrandAgent | PerformanceMarketerAgent (wrong audience) | Veo 3.1 (portrait 9:16); ElevenLabs voice; CapCut API; TikTok Ads Manager | RLAIF (reward from ROAS signal) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 73 | **PromptOptimizerAgent** | Auto-improves prompts via OPRO/APE/DSPy/Promptbreeder | OPRO (Yang 2023); APE (Zhou 2022); DSPy (Stanford); Promptbreeder (DeepMind) | Score uplift per iteration; convergence speed | Beats hand-tuned prompts on held-out briefs | PromptEngineerAgent, AIQAAgent | PromptEngineerAgent (sub-optimal seed) | DSPy framework (MIPRO optimizer); OPRO implementation; held-out eval harness | DSPy compilation + OPRO meta-optimization |
| 74 | **CostOptimizerAgent** | Routes between models/providers for $/quality | Provider pricing; cost-quality frontiers; FrugalGPT patterns | $/successful-task; Pareto distance from frontier | Lower $/quality than human CFO routing | RouterAgent, FinanceAgent | RouterAgent (over-spend), GeneratorAgent (re-roll burn) | Provider pricing APIs; benchmark cost DB; FrugalGPT cascade logic | ReAct (evaluate task → pick cheapest model meeting threshold) |
| 75 | **LatencyOptimizerAgent** | Parallelization, caching, speculative decoding, batching | vLLM; TensorRT-LLM; distillation; Anyscale/Ray | p50/p95 latency; throughput/GPU-hour | Lower p95 than human-tuned pipeline | OrchestratorAgent | OrchestratorAgent (serial bottleneck) | vLLM; TensorRT-LLM; Ray Serve; Redis (response cache); speculative decoding configs | Tool-use profiling + automated pipeline restructuring |
| 76 | **RetentionOptimizerAgent** | Tunes hook, pacing, structure for AVD/hold-rate | YouTube Analy
…



From `corpus/study/ui/agent_management_ui.md` Copy: `sources/excerpts/agent_management_ui.md`.


'''text
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT CONFIGURATION: DirectorAgent (#1)                    [Save] [Reset]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TABS: [Configuration] [Playground] [Knowledge] [History] [Metrics]         │
│                                                                             │
├─── IDENTITY ────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Name: [DirectorAgent_______________]                                       │
│  Category: [Above-the-Line ▼]                                               │
│  Description:                                                               │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ Owns creative vision; issues shot intents, sets pacing, approves     │   │
│  │ takes. The creative authority of the production.                      │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
├─── SYSTEM PROMPT ───────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ You are an elite film director with deep knowledge of visual         │   │
│  │ storytelling, derived from Criterion commentary tracks, DGA          │   │
│  │ seminars, and MasterClass material from Scorsese, Lynch, and         │   │
│  │ Gerwig. Your role is to:                                             │   │
│  │                                                                      │   │
│  │ 1. Translate screenplay scenes into precise shot intents             │   │
│  │ 2. Define camera movement, composition, lighting mood                │   │
│  │ 3. Set pacing that matches genre expectations                        │   │
│  │ 4. Review generated shots against your creative vision               │   │
│  │ 5. Issue creative-intent diffs to other agents                       │   │
│  │                                                                      │   │
│  │ When generating shot intents, output JSON with:                      │   │
│  │ - camera_move, framing, subject, style, duration, mood               │   │
│  │ ...                                                                  │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│  Characters: 2,847 │ [Expand editor] [Version history ▼]                    │
│                                                                             │
├─── ARCHITECTURE PATTERN ────────────────────────────────────────────────────┤
│                                                                             │
│  Pattern: [Self-Refine ▼]                                                   │
│  Options: Self-Refine │ Reflexion │ ReAct │ Constitutional AI │             │
│           Multi-agent Debate │ RLAIF │ DSPy/OPRO │ Agentic Graph            │
│                                                                             │
│  Max iterations: [5___]    (self-refine loops before accepting)              │
│  Temperature: [0.7___]                                                      │
│  Max tokens: [4096__]                                                       │
│                                                                             │
├─── MODEL ASSIGNMENT ────────────────────────────────────────────────────────┤
│                                                                             │
│  Primary LLM: [Gemini 2.5 Pro ▼]                                            │
│  Fallback LLM: [GPT-4o ▼]                                                   │
│  Generation tool: [Veo 3.1 ▼]                                               │
│  Fallback gen: [Kling 3.0 ▼]                                                │
│                                                                             │
├─── TOOLS ───────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Enabled tools:                                                             │
│  ☑ veo_3_1_api        — Video generation (Veo 3.1)                          │
│  ☑ runway_gen4_api    — Video generation (Runway Gen-4)                     │
│  ☑ sora_2_api         — Video generation (Sora 2)                           │
│  ☑ memory_recall      — Retrieve from MemoryAgent                           │
│  ☑ memory_store       — Store decision to MemoryAgent                       │
│  ☑ clip_scorer        — Evaluate CLIP-T alignment                           │
│  ☐ dalle_3_api        — Image generation (disabled for this agent)          │
│  ☐ elevenlabs_api     — Voice (not needed for director)                     │
│                                                                             │
│  [+ Add custom tool]                                                        │
│                                                                             │
├─── QUALITY RUBRIC ──────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┬───────────┬─────────────────────────────────────┐      │
│  │ Metric          │ Threshold │ Description                         │      │
│  ├─────────────────┼───────────┼─────────────────────────────────────┤      │
│  │ clip_t          │ ≥ 0.32    │ Text-video alignment score          │      │
│  │ beat_coverage   │ = 100%    │ All story beats addressed           │      │
│  │ pacing_match    │ ≥ 0.70    │ Pacing fits genre prior             │      │
│  │ style_consistency│ ≥ 0.85   │ Visual style matches across shots   │      │
│  └─────────────────┴───────────┴─────────────────────────────────────┘      │
│  [+ Add metric]  [Edit thresholds]                                          │
│                                                                             │
├─── RELATIONSHIPS ───────────────────────────────────────────────────────────┤
│                                                                             │
│  Accepts critique from:                                                     │
│  [ScreenwriterAgent ×] [EditorAgent ×] [AudienceSimAgent ×] [+ Add]        │
│                                                                             │
│  Comments on (critiques):                                                   │
│  [EditorAgent ×] [DoPAgent ×] [ScreenwriterAgent ×] [ComposerAgent ×]      │
│  [+ Add]                                                                    │
│                                                                             │
├─── COST CONTROLS ───────────────────────────────────────────────────────────┤
│                                                                             │
│  Max cost per task: $[2.50]                                                 │
│  Max concurrent instances: [3___]                                           │
│  Timeout per task: [300__] seconds                                          │
│  Max retries on failure: [3___]                                             │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [Save Changes]  [Reset to Default]  [Export as JSON]  [Clone Agent]        │
│                                                                             │
│  ⚠ Changes apply to all FUTURE productions. Running productions             │
│    continue with their existing configuration.                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
'''

'''text
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT PLAYGROUND: DirectorAgent (#1)                           [Run ▶]     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TABS: [Configuration] [Playground] [Knowledge] [History] [Metrics]         │
│                                                                             │
├─── LEFT: INPUT PANEL ───────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── TASK INPUT ───────────────────────────────────────────────────┐       │
│  │                                                                   │       │
│  │  Task type: [Generate shot intent ▼]                              │       │
│  │  Other options: Critique artifact │ Review cut │ Custom prompt     │       │
│  │                                                                   │       │
│  │  Scene context:                                                   │       │
│  │  ┌────────────────────────────────────────────────────────────┐   │       │
│  │  │ INT. COFFEE SHOP - NIGHT. Rain streaks the window. MAYA    │   │       │
│  │  │ sits alone, staring at her phone. The last text reads:     │   │       │
│  │  │ "I'm not coming." She sets the phone face-down.            │   │       │
│  │  └────────────────────────────────────────────────────────────┘   │       │
│  │                                                                   │       │
│  │  Reference images: [Drop zone]  ┌────┐ ┌────┐                    │       │
│  │                                  │ref1│ │ref2│                    │       │
│  │                                  └────┘ └────┘                    │       │
│  │                                                                   │       │
│  │  Mock critiques (simulate other agents):                          │       │
│  │  ☐ Add EditorAgent critique: [________________]                   │       │
│  │  ☐ Add AudienceSim feedback: [________________]                   │       │
│  │                                                                   │       │
│  │  Style lock / memory context:                                     │       │
│  │  ☐ "Neo-noir melancholic, Veo seed #4412"                        │       │
│  │  ☐ Custom: [________________________________]                     │       │
│  │                                                                   │       │
│  └───────────────────────────────────────────────────────────────────┘       │
│                                                                             │
│  ┌─── RUN SETTINGS ─────────────────────────────────────────────────┐       │
│  │  Model: [Gemini 2.5 Pro ▼]   (override agent default)            │       │
│  │  Generate video: ☑ Yes (costs ~$2.50)  ☐ Text-only (free/cheap)  │       │
│  │  Self-refine: ☑ Enabled  Max iterations: [3]                      │       │
│  │  Estimated cost: ~$3.20                                           │       │
│  └───────────────────────────────────────────────────────────────────┘       │
│                                                                             │
│  [▶ Run Agent]   [▶ Run Text-Only (free)]   [Compare with Another Agent]    │
│                                                                             │
├─── RIGHT: OUTPUT PANEL ─────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── THINKING TRACE (step-by-step agent reasoning) ─────────────┐         │
│  │                              
…



From `corpus/study/ui/backend_agent_management.md` Copy: `sources/excerpts/backend_agent_management.md`.


messages = [
       { role: "system", content: director_system_prompt },
       { role: "user", content: f"""
         Task: Generate shot intent for Scene 2, Shot 5.
         Script context: {script_excerpt}
         Storyboard panel: {panel_description}
         Mood reference: melancholic neo-noir, rain motif
         Critiques to address:
           - EditorAgent: "Use wider lens for Scene 3"
           - AudienceSim: "Scene 2 clarity score 0.6, below 0.7"



From `corpus/study/ui/ui_design.md` Copy: `sources/excerpts/ui_design.md`.


'''text
┌──────────────────────────────────────────────────────────────────────────┐
│  AGENT INSPECTOR: DirectorAgent (#1)                        [Full Screen]│
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─── IDENTITY ──────────┐  ┌─── CURRENT TASK ──────────────────────┐   │
│  │ Category: Above-Line  │  │ Task: Generate Shot Intent #5          │   │
│  │ Pattern: Self-Refine  │  │ Status: ● Running (iteration 2/5)     │   │
│  │ Accepts from: 3 agents│  │ Started: 12:03:22                      │   │
│  │ Comments on: 4 agents │  │ Est. complete: 12:04:50                │   │
│  └───────────────────────┘  └────────────────────────────────────────┘   │
│                                                                          │
│  ┌─── QUALITY METRICS ──────────────────────────────────────────────┐    │
│  │  CLIP-T Score:  ████████████████░░░░  0.34 / 0.32 threshold ✓   │    │
│  │  Beat Coverage: ████████████████████  12/12 (100%) ✓            │    │
│  │  Pacing Match:  ██████████████░░░░░░  0.78 / 0.70 threshold ✓   │    │
│  │  Self-Refine Iterations: [2] of max [5]                          │    │
│  └──────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  ┌─── I/O ARTIFACTS ──────────────┐  ┌─── TOOL CALLS ───────────────┐   │
│  │ INPUT:                         │  │ 12:03:25 Sora 2 API          │   │
│  │  • screenplay_v4.fdx          │  │   prompt: "Close-up, rain..." │   │
│  │  • storyboard_panel_05.png    │  │   → generating (45s)          │   │
│  │  • mood_board_act2.json       │  │                               │   │
│  │                               │  │ 12:03:22 MemoryAgent.recall   │   │
│  │ OUTPUT:                        │  │   query: "Act 2 visual tone"  │   │
│  │  • shot_intent_05.json (v2)   │  │   → 3 results returned        │   │
│  │  • reference_frame_05.png     │  │                               │   │
│  └────────────────────────────────┘  └───────────────────────────────┘   │
│                                                                          │
│  ┌─── CRITIQUE BUS ────────────────────────────────────────────────┐     │
│  │ RECEIVED:                                                       │     │
│  │  • EditorAgent: "Shot 4 transition too abrupt" (12:02:58)      │     │
│  │  • AudienceSim: "Scene 2 clarity score 0.6, below 0.7" (12:01)│     │
│  │ SENT:                                                           │     │
│  │  • → EditorAgent: "Approved cut on beat 6" (12:03:10)          │     │
│  │  • → DoPAgent: "Use wider lens for Scene 3" (12:02:45)         │     │
│  └─────────────────────────────────────────────────────────────────┘     │
│                                                                          │
│  [Retry Task] [Skip] [Send Critique] [View Full History]                 │
└──────────────────────────────────────────────────────────────────────────┘
'''



Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


Provenance

- Master roster row va_id=82 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `[historical-path]
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): upstream-va-design.


<!-- self_contained_spec · video.audiencesim · va_id=82 -->

Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **AudienceSimAgent** (`video.audiencesim`, va_id=82, category `10-Sup`).

Responsibility focus
Simulates audience preference, engagement, and drop-off

Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: workflow support agents, media ops automation, production support AI
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: media operations AI agents
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: production support automation with AI

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

<!-- migration_capability_research · video.audiencesim · v1 · 2026-07-13 -->

```


## Prompts

### `prompts/primary.md`

# Prompt — `video.prompt.audiencesim.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: LLM-as-Judge, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **AudienceSimAgent (VA Domain Pack)** (`video.audiencesim`), a pack agent in the video domain swarm.

### Responsibility (owns)
Simulates audience preference, engagement, and drop-off

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
LLM-as-Judge + pairwise preference panel

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Pairwise preference datasets; retention studies; audience segmentation models

## Developer

### Tools (allowlist intent)
Design tool surface: Persona simulators, pairwise evaluation harness, retention models
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: DirectorAgent, EditorAgent, AnalystAgent, JudgeAgent
- May comment on: Hooks, pacing, clarity, emotional fit, trailer strength
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Preference stability across cohorts; retention-prediction accuracy; disagreement logging

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.audiencesim",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **AudienceSimAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.audiencesim",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.audiencesim`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
15, 21, 26, 30, 31, 37, 38, 50, 59, 63, 87, 88, 92, 93, 94

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
- When metrics exist, surface retention/ROAS hypotheses with confidence — never fabricate live analytics.
- Escalate stereotype/harm/consent risks to ethics/trust-safety/legal gates.

### Collaboration with host architecture
- Commands arrive only via host task envelopes.
- Publish results as structured artifacts; never open browser/UI channels.
- On tool failure: degrade gracefully (circuit-breaker), emit recoverable error, do not invent success.
<!-- RETHINK_100:end -->

### `prompts/video.prompt.audiencesim.v1.md`

# Prompt — `video.prompt.audiencesim.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: LLM-as-Judge, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **AudienceSimAgent (VA Domain Pack)** (`video.audiencesim`), a pack agent in the video domain swarm.

### Responsibility (owns)
Simulates audience preference, engagement, and drop-off

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
LLM-as-Judge + pairwise preference panel

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Pairwise preference datasets; retention studies; audience segmentation models

## Developer

### Tools (allowlist intent)
Design tool surface: Persona simulators, pairwise evaluation harness, retention models
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: DirectorAgent, EditorAgent, AnalystAgent, JudgeAgent
- May comment on: Hooks, pacing, clarity, emotional fit, trailer strength
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Preference stability across cohorts; retention-prediction accuracy; disagreement logging

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.audiencesim",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **AudienceSimAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.audiencesim",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.audiencesim`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
15, 21, 26, 30, 31, 37, 38, 50, 59, 63, 87, 88, 92, 93, 94

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
- When metrics exist, surface retention/ROAS hypotheses with confidence — never fabricate live analytics.
- Escalate stereotype/harm/consent risks to ethics/trust-safety/legal gates.

### Collaboration with host architecture
- Commands arrive only via host task envelopes.
- Publish results as structured artifacts; never open browser/UI channels.
- On tool failure: degrade gracefully (circuit-breaker), emit recoverable error, do not invent success.
<!-- RETHINK_100:end -->

## Rubrics

### `rubrics/primary.md`

Source rubric `video.rubric.audiencesim.v1.json` (baseline_safe; not a production pass).

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.audiencesim.v1",
  "agent_id": "video.audiencesim",
  "title": "L2 craft rubric for AudienceSimAgent",
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
          "name": "Preference stability across cohorts",
          "description": "Preference stability across cohorts",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "retention-prediction accuracy",
          "description": "retention-prediction accuracy",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d3",
          "name": "disagreement logging",
          "description": "disagreement logging",
          "weight": 0.3334,
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
      "surpass_signal_design": "Predicts audience reaction earlier than conventional test-screen cycles",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Preference stability across cohorts; retention-prediction accuracy; disagreement logging",
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

### `rubrics/video.rubric.audiencesim.v1.json`

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.audiencesim.v1",
  "agent_id": "video.audiencesim",
  "title": "L2 craft rubric for AudienceSimAgent",
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
          "name": "Preference stability across cohorts",
          "description": "Preference stability across cohorts",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "retention-prediction accuracy",
          "description": "retention-prediction accuracy",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d3",
          "name": "disagreement logging",
          "description": "disagreement logging",
          "weight": 0.3334,
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
      "surpass_signal_design": "Predicts audience reaction earlier than conventional test-screen cycles",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Preference stability across cohorts; retention-prediction accuracy; disagreement logging",
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

# Source acquisition runbook — `video.audiencesim`

## Purpose
Obtain or refresh knowledge distillation sources listed in `SOURCE_CATALOG.json`.

## Rules
1. **No secrets in git.** API keys only via environment / secret manager.
2. Prefer **licensed / consented / public domain** material.
3. If license unknown: store only short fair-use design excerpts under `excerpts/` and mark `license_class=unknown_review_required`.
4. Update `PROVENANCE.json` with URL, retrieved_at, hash, and license note.
5. Re-run offline golden eval after material changes.

## Design sources (from agents.md)
Pairwise preference datasets; retention studies; audience segmentation models

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
  "agent_id": "video.audiencesim",
  "plan_id": "video.audiencesim.distill.v1",
  "inputs": [
    "src_1",
    "src_2",
    "src_3"
  ],
  "extractors": [
    "markdown_excerpt",
    "structured_table_row"
  ],
  "chunk_policy": {
    "max_chars": 2000,
    "overlap": 200
  },
  "owner": "video.audiencesim",
  "cadence": "quarterly",
  "promotion_criteria": [
    "source license approved or fixture-only",
    "excerpt hash recorded in PROVENANCE",
    "golden eval still passes L1"
  ],
  "memory_namespace": "pack.video.video.audiencesim",
  "next_review_at": "2026-10-01"
}
```

### `sources/excerpts/agent_management_ui.md`

# Agent Management UI — Configure, Test, and Improve Individual Agents

> How users can view/edit agent configurations, test agents in isolation, and feed new knowledge to make them smarter.

---

## Overview: Three Agent Management Modes

```text
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  AGENT MANAGEMENT (accessible from Agent Registry)              │
│                                                                 │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐       │
│  │  1. CONFIGURE  │  │  2. PLAYGROUND │  │  3. KNOWLEDGE  │       │
│  │               │  │               │  │               │       │
│  │ View/edit     │  │ Test agent    │  │ Add training  │       │
│  │ system prompt │  │ with custom   │  │ data, refs,   │       │
│  │ tools, rubric │  │ inputs. See   │  │ examples to   │       │
│  │ thresholds,   │  │ how it thinks │  │ improve agent │       │
│  │ relationships │  │ and produces  │  │ performance   │       │
│  └───────────────┘  └───────────────┘  └───────────────┘       │
│                                                                 │
│  NO production needed. NO cost unless you run the Playground.   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---


## 1. CONFIGURE — View & Edit Agent Settings

### Entry Point: Agent Registry → Click any agent → Configuration Tab

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT CONFIGURATION: DirectorAgent (#1)                    [Save] [Reset]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TABS: [Configuration] [Playground] [Knowledge] [History] [Metrics]         │
│                                                                             │
├─── IDENTITY ────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Name: [DirectorAgent_______________]                                       │
│  Category: [Above-the-Line ▼]                                               │
│  Description:                                                               │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ Owns creative vision; issues shot intents, sets pacing, approves     │   │
│  │ takes. The creative authority of the production.                      │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
├─── SYSTEM PROMPT ───────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ You are an elite film director with deep knowledge of visual         │   │
│  │ storytelling, derived from Criterion commentary tracks, DGA          │   │
│  │ seminars, and MasterClass material from Scorsese, Lynch, and         │   │
│  │ Gerwig. Your role is to:                                             │   │
│  │                                                                      │   │
│  │ 1. Translate screenplay scenes into precise shot intents             │   │
│  │ 2. Define camera movement, composition, lighting mood                │   │
│  │ 3. Set pacing that matches genre expectations                        │   │
│  │ 4. Review generated shots against your creative vision               │   │
│  │ 5. Issue creative-intent diffs to other agents                       │   │
│  │                                                                      │   │
│  │ When generating shot intents, output JSON with:                      │   │
│  │ - camera_move, framing, subject, style, duration, mood               │   │
│  │ ...                                                                  │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│  Characters: 2,847 │ [Expand editor] [Version history ▼]                    │
│                                                                             │
├─── ARCHITECTURE PATTERN ────────────────────────────────────────────────────┤
│                                                                             │
│  Pattern: [Self-Refine ▼]                                                   │
│  Options: Self-Refine │ Reflexion │ ReAct │ Constitutional AI │             │
│           Multi-agent Debate │ RLAIF │ DSPy/OPRO │ Agentic Graph            │
│                                                                             │
│  Max iterations: [5___]    (self-refine loops before accepting)              │
│  Temperature: [0.7___]                                                      │
│  Max tokens: [4096__]                                                       │
│                                                                             │
├─── MODEL ASSIGNMENT ────────────────────────────────────────────────────────┤
│                                                                             │
│  Primary LLM: [Gemini 2.5 Pro ▼]                                            │
│  Fallback LLM: [GPT-4o ▼]                                                   │
│  Generation tool: [Veo 3.1 ▼]                                               │
│  Fallback gen: [Kling 3.0 ▼]                                                │
│                                                                             │
├─── TOOLS ───────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Enabled tools:                                                             │
│  ☑ veo_3_1_api        — Video generation (Veo 3.1)                          │
│  ☑ runway_gen4_api    — Video generation (Runway Gen-4)                     │
│  ☑ sora_2_api         — Video generation (Sora 2)                           │
│  ☑ memory_recall      — Retrieve from MemoryAgent                           │
│  ☑ memory_store       — Store decision to MemoryAgent                       │
│  ☑ clip_scorer        — Evaluate CLIP-T alignment                           │
│  ☐ dalle_3_api        — Image generation (disabled for this agent)          │
│  ☐ elevenlabs_api     — Voice (not needed for director)                     │
│                                                                             │
│  [+ Add custom tool]                                                        │
│                                                                             │
├─── QUALITY RUBRIC ──────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┬───────────┬─────────────────────────────────────┐      │
│  │ Metric          │ Threshold │ Description                         │      │
│  ├─────────────────┼───────────┼─────────────────────────────────────┤      │
│  │ clip_t          │ ≥ 0.32    │ Text-video alignment score          │      │
│  │ beat_coverage   │ = 100%    │ All story beats addressed           │      │
│  │ pacing_match    │ ≥ 0.70    │ Pacing fits genre prior             │      │
│  │ style_consistency│ ≥ 0.85   │ Visual style matches across shots   │      │
│  └─────────────────┴───────────┴─────────────────────────────────────┘      │
│  [+ Add metric]  [Edit thresholds]                                          │
│                                                                             │
├─── RELATIONSHIPS ───────────────────────────────────────────────────────────┤
│

…(clipped 28115 characters from `agent_management_ui.md`)

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

### `sources/excerpts/backend_agent_management.md`

# Backend → Agent Management: How the Backend Controls 114 Agents

> Deep dive into the internal mechanics of how the orchestration backend manages, dispatches, monitors, retries, and communicates with the AI agent workers.

---

## The Core Question

```text
Q: The backend has 114 agent "definitions" — but HOW does it actually
   create, run, communicate with, and control them?

A: Each agent is NOT a separate server or microservice.
   An agent is a CONFIGURATION (system prompt + tools + rubric)
   that gets EXECUTED by a worker process when given a task.

   Think of it like this:
   - The backend is the CONDUCTOR of an orchestra
   - Agents are SHEET MUSIC (instructions)
   - Workers are MUSICIANS (execution)
   - The LLM is the INSTRUMENT (capability)
```

---

## 1. What IS an Agent at Runtime?

An agent is **not** a long-running process. It's a **stateless function** that gets invoked with:

```python
# Pseudocode — what an "agent" actually is in LangGraph

class AgentDefinition:
    agent_id: int                    # 1-114
    name: str                        # "DirectorAgent"
    system_prompt: str               # "You are a film director who..."
    tools: list[Tool]                # [sora_api, veo_api, memory_recall]
    architecture_pattern: str        # "self_refine" | "reflexion" | "react" | ...
    quality_rubric: dict             # { "clip_t": { "threshold": 0.32 } }
    accepts_critique_from: list[int] # [3, 9, 82]  (agent IDs)
    comments_on: list[int]           # [9, 6, 3, 20]
    max_iterations: int              # 5 (for self-refine loop)
    model_preference: str            # "gemini-2.5-pro"
```

When the backend needs DirectorAgent to generate shot intent #5, it:

1. Loads this definition
2. Constructs the LLM prompt (system prompt + task context + critique history)
3. Calls the LLM
4. The LLM decides which tools to call
5. Backend executes tool calls on behalf of the agent
6. Loops if self-refine pattern requires it
7. Publishes result + events

---

## 2. The Orchestration Engine (The Brain)

```text
┌─────────────────────────────────────────────────────────────────────┐
│                    ORCHESTRATION ENGINE                               │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                    DAG STATE MACHINE                          │    │
│  │                    (LangGraph Graph)                          │    │
│  │                                                             │    │
│  │  Nodes:    [Brief] → [Plan] → [Route] → [Craft×N] → [Gate]│    │
│  │  Edges:    Conditional (if gate passes → next phase)        │    │
│  │  State:    { phase, active_agents, pending_tasks, budget }  │    │
│  │  Checkpoint: Persisted after every node execution           │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌───────────────────┐  ┌───────────────────┐                      │
│  │   TASK DISPATCHER  │  │   TASK QUEUE      │                      │
│  │                   │  │                   │                      │
│  │ Decides:          │  │ Per-agent queues: │                      │
│  │ • WHICH agent     │  │ • agent_1: [t5]  │                      │
│  │ • WHAT task       │  │ • agent_6: [t3]  │                      │
│  │ • WHICH model     │  │ • agent_9: []    │                      │
│  │ • WHEN to run     │  │ • agent_46: [t7] │                      │
│  │ • Priority order  │  │ • ...            │                      │
│  └───────────────────┘  └───────────────────┘                      │
│                                                                     │
│  ┌───────────────────┐  ┌───────────────────┐                      │
│  │   CRITIQUE ROUTER  │  │   GATE EVALUATOR  │                      │
│  │                   │  │                   │                      │
│  │ Routes critique   │  │ Checks criteria   │                      │
│  │ messages between  │  │ Triggers approval │                      │
│  │ agents based on   │  │ Advances phase    │                      │
│  │ "accepts_from"    │  │ when human says OK│                      │
│  │ relationships     │  │                   │                      │
│  └───────────────────┘  └───────────────────┘                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. How the Backend DISPATCHES a Task to an Agent

Step-by-step, here's what happens when the OrchestratorAgent decides "DirectorAgent should work on Shot #5":

```text
Step 1: TASK CREATION
─────────────────────
Orchestrator creates a task object:
{
  task_id: "task_042",
  agent_id: 1,                          // DirectorAgent
  task_type: "generate_shot_intent",
  inputs: {
    script: "artifact_id:screenplay_v4",
    storyboard: "artifact_id:panel_05",
    mood: "artifact_id:mood_board_act2",
    critiques: ["use wider lens", "scene 2 clarity low"]
  },
  constraints: {
    model: "gemini-2.5-pro",
    generation_tool: "veo-3.1",
    budget_remaining: 58,
    max_cost: 2.50
  }
}


Step 2: QUEUE + WORKER PICKUP
─────────────────────────────
Task goes into agent_1's queue.
A free worker process picks it up.

The worker pool is like a thread pool:
  - 10-50 concurrent workers (configurable)
  - Each worker can execute ANY agent's task
  - Workers are stateless — they load agent config per task


Step 3: AGENT EXECUTION (inside the worker)
───────────────────────────────────────────

Worker does this:

  a) Load AgentDefinition for agent_id=1 (DirectorAgent)
  b) Fetch input artifacts from Asset Store
  c) Fetch relevant memories from MemoryAgent (vector search)
  d) Construct LLM messages:

     messages = [
       { role: "system", content: director_system_prompt },
       { role: "user", content: f"""
         Task: Generate shot intent for Scene 2, Shot 5.
         Script context: {script_excerpt}
         Storyboard panel: {panel_description}
         Mood reference: melancholic neo-noir, rain motif
         Critiques to address:
           - EditorAgent: "Use wider lens for Scene 3"
           - AudienceSim: "Scene 2 clarity score 0.6, below 0.7"
         
         Output: JSON shot intent with camera, subject, style, duration.
       """ }
     ]

  e) Call LLM (Gemini 2.5 Pro):
     response = await llm.chat(messages, tools=[veo_api, memory_store])

  f) LLM responds with tool calls:
     → tool_call: veo_api.generate(prompt="slow dolly push...", seed=4412)
     → Worker EXECUTES this tool call (HTTP to Veo 3.1 API)
     → Gets back: video URL + metadata

  g) LLM evaluates result (self-refine):
     → tool_call: clip_scorer.evaluate(video_url, text_prompt)
     → Score: 0.34 (threshold: 0.32) ✓ PASS

  h) If score < threshold: loop back to step (e) with feedback
     If score >= threshold: task complete


Step 4: RESULT PUBLICATION
──────────────────────────
Worker publishes to Event Bus:
  • { type: "artifact_created", artifact_id: "art_043", ... }
  • { type: "agent_state_change", agent: 1, state: "complete" }
  • { type: "metric_update", agent: 1, metric: "clip_t", value: 0.34 }

Orchestrator receives "task_042 complete" → decides next task.
```

---

## 4. How the Backend MANAGES Agent Lifecycle

```text
┌─────────────────────────────────────────────────────────────────┐
│                   AGENT LIFECYCLE                                 │
│                                                                 │
│   IDLE ──────► QUEUED ──────► RUNNING ──────► COMPLETE          │
│    │              │              │                │              │
│    │              │              │                ▼              │
│    │              │              │           (publish result)    │
│    │              │              │                               │
│

…(clipped 14887 characters from `backend_agent_management.md`)

### `sources/excerpts/lifes_quiet_redemption_agent_workflow.md`

# "Life's Quiet Redemption" — Agent-Orchestrated Production Workflow

> **What this document is.** A rebuilt, table-first version of the original "Life's Quiet Redemption" cinematic-short workflow, re-cast onto the **VA-Agent-Swarm** 114-agent system. Every phase, scene, and craft task is now mapped to the *actual* agents that own it, what service each agent delivers, the artifacts it consumes/produces, its tools, its quality gate, and which agents critique it.
>
> - **Project type:** Emotional inspirational short film (~55–65s) + vertical cutdowns
> - **Theme:** Unfulfilled dreams, detours, and "failures" quietly protecting and guiding us
> - **Style:** Cinematic realistic Chinese life drama; warm golden-hour light; shallow DoF; subtle film grain
> - **Pipeline:** Maps to workflow variant **E — AI Short Film** ([workflows/E-ai-short-film.svg](./workflows/E-ai-short-film.svg))
> - **System map:** [SYSTEM_REFERENCE.md](./SYSTEM_REFERENCE.md) · [agents.md](./agents.md) · [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md)

---

## 0. Visual Diagrams (read this first)

These six diagrams describe the workflow end-to-end and are referenced throughout the sections below. Source files live in [`./workflows/`](./workflows/).

| # | Diagram | Describes | Maps to section |
|---|---|---|---|
| D1 | Pipeline Overview | The 6-phase DAG, owning agents, exit gates, and the analytics feedback loop | §1, §5 |
| D2 | Scene Flow | The 14-card timeline, emotional arc, retention bands, and per-shot engine | §2, §10, §15 |
| D3 | Per-Shot Loop | The 3E micro-loop, mandatory visual anchor, VBench gate, and MCTS reroute | §3.4, §13, §14 |
| D4 | Character-Consistency Stack | The identity pipeline keeping characters stable youth→adult | §3.3, §12 |
| D5 | Engine Routing | RouterAgent tiers incl. Grok Imagine, hero engines, and cost optimization | §3.4, §11 |
| D6 | Quality Gate Ladder | The L1/L2/L3 gates and the VBench/VMBench scorecard | §5, §13 |

### D1 · Pipeline Overview
![Life's Quiet Redemption — 6-phase production pipeline with gates and feedback loop](./workflows/lqr-pipeline-overview.svg)

### D2 · Scene Flow, Emotional Arc & Retention Bands
![Scene flow timeline of 14 cards with emotional arc, retention bands, and engine per shot](./workflows/lqr-scene-flow.svg)

### D3 · Per-Shot Generation Loop
![Per-shot generation loop: 3E micro-loop, visual anchor, image-to-video, VBench gate, MCTS reroute](./workflows/lqr-per-shot-loop.svg)

### D4 · Character-Consistency Identity Stack
![Character consistency identity stack: bible, visual anchoring, per-character LoRA, RL identity, memory conditioning, fallback, VLM audit](./workflows/lqr-character-consistency.svg)

### D5 · Engine Routing (RouterAgent Tiers)
![Engine routing tiers: Grok Imagine draft and image-to-video, agent-mode rough cut, hero engines, local ComfyUI, cost optimizer](./workflows/lqr-engine-routing.svg)

### D6 · Quality Gate Ladder & VBench Scorecard
![Quality gate ladder L1 spec, L2 rubric VBench scorecard, L3 audience preference, GateKeeper sign-off](./workflows/lqr-quality-gates.svg)

---

## 1. Pipeline Overview — Phase → Owning Agents → Service

Maps the original Phase 0–6 outline onto the swarm's 6-phase production pipeline (SYSTEM_REFERENCE §6.1). Each phase ends with a **GateKeeperAgent (#57)** L1/L2/L3 sign-off before the DAG advances.

| Phase | Lead Agents | Supporting Agents | Service Delivered (for this film) | Key Artifact Out | Gate (exit criteria) |
|---|---|---|---|---|---|
| **0 · Intent & Concept** | IntentAnalysisAgent (DIA), PlannerAgent (#54), ProducerAgent (#2) | StrategicGoal framework, BrandStrategistAgent (#85), FinanceAgent (#38), CostOptimizerAgent (#74) | Parse the "life secretly saved us" brief into a phased DAG, budget, schedule, emotional-arc target | Parsed brief, character bible seed, phased DAG | Brief unambiguous; DAG valid; budget variance <10% |
| **1 · Creative Development** | DirectorAgent (#1), ScreenwriterAgent (#3), General Creative Agent (SSOR) | IdeationAgent (#59), NarrativeArcAgent (#60), EmotionalArcAgent (#65), NoveltyAgent (#64), StoryboardAgent (#14), MoodBoardAgent (#63) | Treatment, 12-scene + ending storyboard, refined 旁白, recurring-motif design, valence/arousal curve | Locked storyboard table, VO script, lookbook | Beat coverage 100%; cliché count below τ; arc curve fits target |
| **2 · Pre-Production** | ConceptArtistAgent (#15), ProductionDesignAgent (#16), CastingAgent (#5) | CostumeDesignAgent (#17), MUAAgent (#18), AvatarDesignAgent (#47), ResearchAgent, StyleTransferAgent (#61), ContinuityAgent (#98) | Character reference set (young/adult for A,B,C,E,F,J), age-progression pairs, wardrobe, set look, identity hashes | `/refs/` portrait set, style LoRAs, continuity manifest | Identity hash locked per character; consent chain signed |
| **3 · Production (Generation)** | PromptEngineerAgent (#46), CinematographerAgent (#6), CameraOperatorAgent (#7) | TalentAgent (#26), VoiceOverAgent (#21), ComposerAgent (#20), SoundDesignAgent (#19), VoiceCloneAgent (#48), PromptOptimizerAgent (#73) | Per-shot keyframes → image-to-video clips, VO takes, score, SFX/ambience | Raw shot clips, audio stems, VO tracks | CLIP-T ≥0.32; identity drift = 0; ≤3 iterations/shot |
| **4 · Post-Production** | EditorAgent (#9), ColoristAgent (#10), SoundMixerAgent (#22) | AIQAConsistencyAgent (#49), LipSyncAgent (#99), MotionGraphicsAgent (#13), VFXSupervisorAgent (#11), RetentionOptimizerAgent (#76) | Assembled cut to VO rhythm, warm grade, ending cards, mix, QC pass | Graded master, mixed audio, QC report | ΔE drift <2; LUFS on spec; artifact pass >95% |
| **5 · QA, Compliance & Accessibility** | GateKeeperAgent (#57), ComplianceAgent (#37), AccessibilityAgent (#83) | AccessibilityOptimizerAgent (#78), DeepfakeDetectionAgent (#103), EthicsAgent (#107), LocalizationQAAgent (#44) | Bilingual subtitles, C2PA signing, synthetic-media disclosure, rights clearance | Signed master + caption tracks | WCAG AA 100%; zero rights flags; C2PA chain valid |
| **6 · Delivery & Optimization** | SocialMediaStrategistAgent (#28), TrailerEditorAgent (#51), AnalystAgent (#81) | SEOAgent (#87), ChannelManagerAgent (#108), PersonalizationEngineerAgent (#50), OptimizationAgent, CommunityAgent (#88) | Platform variants (16:9 + 9:16), titles/metadata, Shorts hook cut, post-launch analytics loop | Outlet packages, campaign, analytics dashboard | All outlet specs met; reach/retention tracked |

---

## 2. Scene-by-Scene Production Matrix

Each storyboard row becomes a **production card** routed through the DAG. Columns map the original (Duration / Shot / Description / 旁白) plus the agent assignments, generation engine, audio design, continuity controls, and QC owner.

| # | Beat | Dur | Shot | Visual Description (model-facing) | Primary Creative Agent | Generation Agent + Engine | Audio Agents (旁白 / SFX / Music) | Continuity Control | QC Owner |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Youth — study | 4–5s | 特写 / ECU | Student A bent over a paper map, pencil tracing borders, dust-lit window, hopeful focus | DirectorAgent + EmotionalArcAgent | PromptEngineerAgent → Veo 3.1 (slow push-in) | VO: warm narrator line 1 · SFX: pencil-on-paper, faint classroom | ContinuityAgent: A-young identity hash | AIQAConsistencyAgent |
| 2 | Youth — leaving home | 4–5s | 全景 / Wide | 18yo C with suitcase at doorway, morning light, looking back once | DirectorAgent + StoryboardAgent | PromptEngineerAgent → Kling 3.0 (static, wind) | VO line 2 · SFX: door, distant street · Music: piano enters | ContinuityAgent: C-young, wardrobe | AIQAConsistencyAgent |
| 3 | Youth — coding passion | 4–5s | 特写 / CU | Young coder B, red tired eyes, all-nighter glow, fingers pause then type with growing confidence | CinematographerAgent | PromptEngineerAgent → Veo 3.1 (handheld breath) | VO line 3 · SFX: mechanical keyboard (ASMR) · Music: build | ContinuityAgent: B-young, screen glow LUT | AIQAConsisten

…(clipped 39105 characters from `lifes_quiet_redemption_agent_workflow.md`)

### `sources/excerpts/system_build_plan.md`

# VA-Agent-Swarm — System Build Plan

**Document Version:** 1.0 (Ultra-Detailed, Implementation-Ready)
**Date:** May 29, 2026
**Target Build Agent:** **Claude Code** (Anthropic CLI coding agent)
**Authors:** Synthesized for Nicholas (nicholas_hui) from the complete `study/` specification corpus
**Purpose:** This is the **single, authoritative, step-by-step plan** for an AI coding agent (Claude Code) to build the entire **VA-Agent-Swarm** — a 114-agent, hierarchical multi-agent video-production system — from an empty repository to a hardened, observable, production-grade platform.

> **Scope contract:** This document does *not* re-derive the system design. It assumes the design is already specified across `study/` (see [`SYSTEM_REFERENCE.md`](./SYSTEM_REFERENCE.md), [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md), [`agents.md`](./agents.md), and the per-agent functional/technical specs). This plan tells Claude Code **what to build, in what order, with what acceptance gates, and how to use its own tooling to do it reliably.**

---

## 0. How To Use This Document (Read First — This Section Is For Claude Code)

### 0.1 Your operating loop for the whole build

You (Claude Code) will execute this plan as a sequence of **Milestones (M0–M12)**. For *every* milestone and *every* task inside it:

1. **Enter Plan Mode first** (`Shift+Tab` → plan mode). Read the referenced spec(s), restate the goal, list files you will create/modify, and surface unknowns. **Do not edit code in plan mode.**
2. **Confirm the plan** against the milestone's *Acceptance Gate* and *Definition of Done (DoD)*. If anything is ambiguous, ask one consolidated question rather than guessing.
3. **Write the test first** (TDD). Every unit of behavior gets a failing test before implementation. See §9.
4. **Implement** the smallest increment that makes the test pass.
5. **Run the local gate**: `make verify` (lint + type + unit). Never advance with a red gate.
6. **Self-review** using the `code-reviewer` subagent (§2.3) and the milestone's checklist.
7. **Commit** with a Conventional Commit message (§11.3) referencing the milestone (e.g., `feat(m2-orchestrator): ...`).
8. **Update progress**: tick the milestone checklist item in `BUILD_PROGRESS.md` (you maintain this file — see §0.4).
9. **`/clear` context** between unrelated tasks to keep the window clean. Use `/compact` only mid-task.

### 0.2 The "rethink 100 times" mandate, operationalized

The user asked for a plan rethought "100 times with full effort." That intensity is encoded structurally, not as a slogan:

- **§14** is a literal **100-point hardening checklist** (10 themes × 10 checks). The system is not "done" until all 100 pass.
- The reference workflow already defines a **100-pass reassessment discipline** ([`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §1.4). This build plan inherits it: every milestone's acceptance is re-challenged across the five bands (traceability → architecture → handoffs → metrics → wording).
- Every agent you build must clear the system's own **L1/L2/L3 quality framework** and the **Q1–Q6 delivery QC mesh** (§5.5). Quality is recursive: the system that judges videos must itself be judged.

### 0.3 Golden rules (violating these is a defect, even if tests pass)

| # | Rule | Why |
|---|------|-----|
| G1 | **Contracts before code.** The shared Pydantic contracts (§5) are built and frozen *before* any agent. Every agent imports them; none redefines them. | Prevents 114 divergent message formats. |
| G2 | **Vertical slice before breadth.** One workflow (Viral Hook, archetype A) runs end-to-end through real infra before the other 108 agents are built. | Validates the architecture cheaply before scale. |
| G3 | **Every agent is an instance of one base class.** No bespoke agent loops. New agents are *configuration + rubric + tools*, produced by the Agent Factory (§8). | 114 agents must share one lifecycle. |
| G4 | **No agent talks to the UI directly.** Agents publish to the Event Bus; the WebSocket Gateway fans out. | Per [`ui/architecture_communication.md`](./ui/architecture_communication.md). |
| G5 | **Determinism where possible.** Pin seeds, model versions, and prompt versions. Record them in provenance. | Reproducibility + audit. |
| G6 | **Cost & safety are gates, not afterthoughts.** The LLM gateway meters every token from M3; ComplianceAgent can BLOCK from the moment it exists. | Per spec; runaway cost/safety kills the project. |
| G7 | **Mock external gen-models behind an interface from day one.** Real Sora/Veo/Kling calls are expensive and rate-limited; the `MediaGenProvider` interface lets you run the whole DAG on cheap stubs in CI. | Testability + cost control. |

### 0.4 Artifacts you maintain throughout the build

- `BUILD_PROGRESS.md` — living checklist mirroring §6 milestones and §14 hardening; you tick items as you complete them.
- `DECISIONS.md` — an ADR (Architecture Decision Record) log; every non-obvious choice gets a dated entry.
- `CLAUDE.md` (root + per-package) — your persistent project memory (template in Appendix A).
- `.claude/` — your subagents, slash commands, settings, and hooks (Appendices B–D).

---

## 1. Mission & Build Philosophy

### 1.1 What is being built (one paragraph)

A hierarchical **multi-agent system (MAS)** that automates/augments professional video production from a client brief to multi-channel delivery. **114 specialized agents** (10 categories) run as nodes in a **LangGraph DAG**, made durable by **Temporal**, communicating creative artifacts via a **Shared Artifact Handoff Contract** and critique via a **CritiqueMessage bus**, gated by a **L1/L2/L3 + Q1–Q6 quality mesh**, observed via **LangSmith/Grafana**, surfaced to humans through a **Next.js 15 console** over REST + WebSocket. Cross-cutting services (Agentic RAG, Research, GCA, Optimization, DIA, Aesthetics, LLM-cost dashboard) provide reasoning, knowledge, creativity, and taste to every agent.

### 1.2 Build philosophy

1. **Walking skeleton first.** Get the thinnest possible end-to-end path alive (brief → 1 agent → artifact → UI event) before adding muscle.
2. **Platform, then agents.** ~70% of the hard engineering is the *platform* (orchestration, contracts, QC, observability, gateway). Agents are mostly declarative once the platform is right.
3. **Factory over hand-craft.** After the platform and 5 reference agents, the remaining ~109 agents are generated from spec via the Agent Factory and reviewed, not hand-coded loop-by-loop.
4. **Dogfood the Coding Agent spec.** The intended self-building "N1ch01as Architect" coding agent ([`coding_agent_functional_specification.md`](./coding_agent_functional_specification.md)) *is the role Claude Code plays* during this build. Where that spec defines conventions, follow them.
5. **Quality is recursive and measurable.** Use the system's own evaluation philosophy on the system itself: spec-conformance (L1), rubric (L2), preference/behavioral (L3).

---

## 2. Target Build Agent: Claude Code Operating Model

This section configures Claude Code so it builds the system reliably, with high context hygiene and minimal rework. **Set this up in M0 before writing product code.**

### 2.1 `CLAUDE.md` strategy (project memory)

Claude Code auto-loads `CLAUDE.md` from the repo root (and nested package dirs) into context. Use it as the always-on "constitution."

- **Root `CLAUDE.md`** (template in Appendix A): tech stack + pinned versions, monorepo map, the 7 Golden Rules (§0.3), build/test/lint commands, code-style rules, contract location, and "where to find the spec for X."
- **Per-package `CLAUDE.md`**: each `packages/*` and `services/*` gets a short `CLAUDE.md` describing its responsibility, public API, and local test command. Nested files load when you work in that subtree, keeping context tight.
- **Keep it lean.** `CLAUDE.md` competes with task context. Link to specs rather than pasting them. Run `/mem

…(clipped 82565 characters from `system_build_plan.md`)

### `sources/excerpts/SYSTEM_REFERENCE.md`

# VA-Agent-Swarm — System Reference & Integration Map

> **Purpose:** This document is the single entry point that links every agent specification, workflow, technical architecture, and supporting resource into one cohesive system view. It maps how each component relates to the whole, defines the integration points, and provides navigation for implementers.

---

## Table of Contents

1. [System Overview](#1-system-overview)
2. [Architecture Layers](#2-architecture-layers)
3. [Agent Categories & Specification Map](#3-agent-categories--specification-map)
4. [Infrastructure & Support Agents](#4-infrastructure--support-agents)
5. [Cross-Cutting Capabilities](#5-cross-cutting-capabilities)
6. [Workflow Integration](#6-workflow-integration)
7. [Data Flow & Handoff Contracts](#7-data-flow--handoff-contracts)
8. [UI & Communication Layer](#8-ui--communication-layer)
9. [Technology Stack Reference](#9-technology-stack-reference)
10. [Reference Material Index](#10-reference-material-index)
11. [Implementation Priority & Dependencies](#11-implementation-priority--dependencies)

---

## 1. System Overview

The **VA-Agent-Swarm** is a hierarchical multi-agent system (MAS) designed to fully automate (or augment) professional video production — from initial creative brief through final delivery across all distribution channels. The system comprises **114 specialized agents** organized into 10 functional categories, supported by dedicated infrastructure agents, a shared critique bus, and a unified orchestration runtime.


### Core Design Principles

| Principle | Description | Reference |
|-----------|-------------|-----------|
| **Agentic Graph** | Agents as DAG nodes with handoffs and review gates | [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) §1 |
| **Self-Refine + Critique** | Every agent drafts → self-critiques → revises against rubric | Madaan et al., 2023 |
| **Shared Artifact Contract** | Machine-readable manifests flow between all phases | [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) §1.3 |
| **Human-in-the-Loop Gates** | Critical decisions escalate to human approval | [agents.md](./agents.md) — ProducerAgent |
| **Provenance (C2PA)** | Every artifact is signed; downstream agents verify chain | C2PA spec |
| **Continuous Self-Improvement** | Agents learn from outcomes, store episodic memory, ratchet quality | Reflexion (Shinn 2023) |

### System Boundaries

```
┌─────────────────────────────────────────────────────────────────────────┐
│  USER / CLIENT BRIEF                                                     │
└───────────┬─────────────────────────────────────────────────────────────┘
            ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  TIER 1: UI FRONTEND — React 19 + Next.js 15                             │
│  (Project creation, agent management, real-time monitoring)              │
└───────────┬──────────────────────────────────┬──────────────────────────┘
            │ REST/GraphQL (commands)           │ WebSocket (live streams)
            ▼                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  TIER 2: API GATEWAY + ORCHESTRATION BACKEND                             │
│  FastAPI + LangGraph + Temporal + Redis Event Bus                        │
└───────────┬──────────────────────────────────┬──────────────────────────┘
            │ Agent Task Queue                  │ Tool API Calls
            ▼                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  TIER 3: AGENT RUNTIME — 114 Agent Definitions                           │
│  LLM Providers: Grok-4.x, Gemini 2.5 Pro, GPT-4o, Claude 4             │
│  Tool Access: Sora 2, Veo 3.1, Runway Gen-4, ElevenLabs, DaVinci, etc. │
└─────────────────────────────────────────────────────────────────────────┘
```

> **Full architecture details:** [ui/architecture_communication.md](./ui/architecture_communication.md)


---

## 2. Architecture Layers

The system is organized into **7 runtime layers** that every agent participates in:

| Layer | Responsibility | Key Agents / Services |
|-------|---------------|----------------------|
| **Orchestration** | Plan, route, schedule, retry, escalate | PlannerAgent (#54), OrchestratorAgent (#53), RouterAgent (#55), JudgeAgent (#56) |
| **Asset & Data Backbone** | Immutable asset IDs, versioning, dependency edges, rights | Asset Store (S3 + metadata DB) |
| **Message & State Fabric** | Critique bus, job status, gate decisions | Redis Streams / NATS, durable state store |
| **Quality & Continuity Mesh** | Multi-pass QC, continuity, accessibility, compliance | AIQAConsistencyAgent (#49), ComplianceAgent (#37), AccessibilityAgent |
| **Observability & Replay** | Live status, failure causes, bottlenecks, replay | AgentOps pipeline, LangSmith traces |
| **Delivery Fabric** | Package masters into outlet-specific variants | TrailerEditorAgent (#51), SocialMediaStrategistAgent (#28) |
| **Compute & Storage Scaling** | GPU autoscale, tiered storage | Infrastructure layer (Docker/K8s) |

> **Full layer specification:** [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) §1.2

---

## 3. Agent Categories & Specification Map

The 114 agents are organized into 10 categories. Below, each category links to the master roster AND to any dedicated deep-specification documents that provide implementation-level detail.

### 3.1 Above-the-Line Agents (1–5)

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 1 | DirectorAgent | Owns vision; shot intents, pacing, approvals | — |
| 2 | ProducerAgent / EP | Budget, schedule, phase gates | — |
| 3 | ScreenwriterAgent | Treatment → screenplay; dialogue; structure | [screenwriter_strategic_goal_achievement_agent_functional_specification.md](./screenwriter_strategic_goal_achievement_agent_functional_specification.md) |
| 4 | ShowrunnerAgent | Cross-episode arc, writers'-room orchestration | — |
| 5 | CastingAgent | Voice + likeness selection; auditions | — |

**Roster reference:** [agents.md](./agents.md) §1


### 3.2 Camera & Lighting Agents (6–8)

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 6 | CinematographerAgent (DoP) | Lensing, lighting, composition, look | — |
| 7 | CameraOperatorAgent | Framing, focus, camera moves | — |
| 8 | DronePilotAgent | Aerial cinematography | — |

**Roster reference:** [agents.md](./agents.md) §2

### 3.3 Editorial & Color Agents (9–18)

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

**Roster reference:** [agents.md](./agents.md) §3

### 3.4 Sound & Music Agents (19–22)

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 19 | SoundDesignAgent | Ambience, foley, SFX | — |
| 20 | ComposerAgent | Original score | — |
| 21 | VoiceOverAgent | Narration, character VO | [podcast_agent_functional_specifcation.md](./podcast_agent_functional_specifcation.md) (shared patterns) |
| 22 | SoundMixerAgent | Final mix; 5.1/Atmos deliverables | — |

**Roster reference:** [agents.md](./agents.md) §4

### 3.5 Performance & Choreography Agents (23–27)

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 23 | ChoreographyAgent | Movement design | — |
|

…(clipped 29498 characters from `SYSTEM_REFERENCE.md`)

### `sources/excerpts/ui_design.md`

# VA Agent Swarm — Complete UI Layout Design

> Covers every operation in the [Composition Diagram](../agents.md#composition-diagram) and provides a full production-start journey for all 10 workflow types (A–J).

---

## Table of Contents

1. [Design Philosophy](#1-design-philosophy)
2. [Information Architecture](#2-information-architecture)
3. [Master Shell Layout](#3-master-shell-layout)
4. [Surface Inventory](#4-surface-inventory)
5. [Page-by-Page Breakdown](#5-page-by-page-breakdown)
6. [Production Start Flow](#6-production-start-flow)
7. [Composition Diagram Coverage Map](#7-composition-diagram-coverage-map)
8. [Responsive & Accessibility Notes](#8-responsive--accessibility-notes)
9. [Component Library Summary](#9-component-library-summary)
10. [Interaction Patterns](#10-interaction-patterns)

---

## 1. Design Philosophy

### 1.1 Core Principles

| Principle | Rationale |
|-----------|-----------|
| **Brief-First** | Every production starts from a human brief; UI makes brief-entry the gravity center |
| **Progressive Disclosure** | 114 agents are overwhelming; show only what the current phase needs |
| **Live DAG Visibility** | The Composition Diagram runs in real-time; users must see agent state at a glance |
| **Gate-Driven Confidence** | GateKeeperAgent phase transitions surface as explicit approval moments in the UI |
| **Critique Transparency** | Every agent critique message is viewable, searchable, and actionable |
| **Production-Type Aware** | The 10 workflow templates (A–J) shape which agents activate and which panels appear |

### 1.2 Target Users

| Persona | Needs |
|---------|-------|
| **Creator** | Start production fast, review outputs, approve gates |
| **Producer** | Monitor budget/schedule, resolve escalations, manage team |
| **Technical Operator** | Tune prompts, inspect agent logs, manage model routing |
| **Reviewer/Client** | View deliverables, leave feedback, approve final |


---

## 2. Information Architecture

```text
ROOT
├── Dashboard (Home)
│   ├── Active Productions Grid
│   ├── Quick-Start Brief Wizard
│   └── System Health Banner
│
├── Brief Studio
│   ├── Template Selector (A–J workflows)
│   ├── Brief Editor (structured + freeform)
│   ├── Reference Upload (mood boards, scripts, assets)
│   └── Launch Confirmation (→ PlannerAgent)
│
├── Production Console (per-production)
│   ├── DAG Canvas (live Composition Diagram)
│   │   ├── Agent Nodes (state: idle/running/blocked/done)
│   │   ├── Edge Flows (artifact handoffs)
│   │   └── Gate Checkpoints (approve/reject/comment)
│   │
│   ├── Timeline View
│   │   ├── Phase Swimlanes (Pre-pro → Production → Post → Delivery)
│   │   ├── Milestone Markers
│   │   └── Budget Burn Overlay
│   │
│   ├── Agent Inspector (drill-down panel)
│   │   ├── Agent Identity & Role
│   │   ├── Current Task & Progress
│   │   ├── Input/Output Artifacts
│   │   ├── Critique Bus (sent/received)
│   │   ├── Quality Metrics (self-score vs threshold)
│   │   └── Tool Calls Log
│   │
│   ├── Artifact Gallery
│   │   ├── Grid/List Toggle
│   │   ├── Version History per Artifact
│   │   ├── Preview (video/audio/image/text)
│   │   ├── Provenance Chain (C2PA)
│   │   └── Compare Mode (A/B side-by-side)
│   │
│   ├── Critique Feed
│   │   ├── Chronological Message Stream
│   │   ├── Filter by Agent / Phase / Severity
│   │   └── Human Intervention Slot
│   │
│   └── Gate Control Panel
│       ├── Pending Approvals Queue
│       ├── Gate Criteria Checklist (L1/L2/L3)
│       ├── Approve / Reject / Request Changes
│       └── C2PA Sign-off Confirmation
│
├── Agent Registry
│   ├── All 114 Agents (searchable, filterable by category)
│   ├── Agent Detail Card (capabilities, tools, patterns)
│   ├── Dependency Graph
│   └── Performance Benchmarks
│
├── Memory & Knowledge
│   ├── Project Memory (MemoryAgent contents)
│   ├── Episodic Log (Reflexion entries)
│   ├── Series Bible / World-Building DB
│   └── Brand Asset Library
│
├── Delivery Hub
│   ├── Master Package Builder
│   ├── Channel-Specific Variants
│   ├── QC Status Matrix
│   ├── Distribution Tracker
│   └── Analytics Dashboard (post-release)
│
├── Settings & Admin
│   ├── Model Routing Config (RouterAgent rules)
│   ├── Cost/Latency Budgets
│   ├── API Key Management
│   ├── Team & Permissions
│   └── Compliance Config (constitutions, consent DB)
│
└── Help & Docs
    ├── Agent Glossary
    ├── Workflow Templates Guide
    └── API Reference
```


---

## 3. Master Shell Layout

### 3.1 Shell Anatomy

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  TOP BAR (64px)                                                              │
│  ┌──────┬──────────────────────────────┬───────────────────────────────────┐ │
│  │ Logo │  Global Search (Cmd+K)       │  Notifications │ User │ Settings │ │
│  └──────┴──────────────────────────────┴───────────────────────────────────┘ │
├────────┬─────────────────────────────────────────────────────────────────────┤
│  SIDE  │  MAIN CANVAS                                                        │
│  NAV   │                                                                     │
│ (72px) │  ┌─────────────────────────────────────────────────────────────┐    │
│        │  │  CONTEXT BAR (production name, phase, budget, health)       │    │
│  ○ Dash│  ├─────────────────────────────────────────────────────────────┤    │
│  ○ Brief│ │                                                             │    │
│  ○ Prod │ │              PRIMARY VIEW AREA                              │    │
│  ○ Agents│ │          (DAG / Timeline / Gallery / Feed)                 │    │
│  ○ Memory│ │                                                            │    │
│  ○ Deliver│ │                                                           │    │
│  ○ Settings│ │                                                          │    │
│        │  │                                                             │    │
│        │  ├─────────────────────────────────────────────────────────────┤    │
│        │  │  DETAIL DRAWER (slides up: Agent Inspector / Artifact View) │    │
│        │  └─────────────────────────────────────────────────────────────┘    │
│        │                                                                     │
├────────┴─────────────────────────────────────────────────────────────────────┤
│  STATUS BAR (32px)                                                           │
│  Running Agents: 12/27 │ Phase: Production │ Budget: $42/$100 │ ETA: 3m     │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Layout Zones

| Zone | Height/Width | Purpose |
|------|-------------|---------|
| Top Bar | 64px fixed | Global nav, search (searches agents, artifacts, critiques), notifications |
| Side Nav | 72px wide, icon-only (expands on hover to 240px with labels) | Primary navigation |
| Context Bar | 48px fixed | Current production context breadcrumb |
| Primary View | Flex-grow | The active workspace surface |
| Detail Drawer | 0–50% from bottom, resizable | Inspector / preview without leaving context |
| Status Bar | 32px fixed | Live production telemetry at a glance |

### 3.3 Navigation Model

| Level | Mechanism | Example |
|-------|-----------|---------|
| L0 — App sections | Side Nav icons | Dashboard → Brief Studio → Production Console |
| L1 — Views within section | Tab bar inside Primary View | DAG Canvas │ Timeline │ Gallery │ Critique Feed |
| L2 — Detail | Drawer (bottom) or Modal | Agent Inspector, Artifact Viewer, Gate Approval Dialog |
| L3 — Contextual actions | Right-click menu / Command Palette (Cmd+K) | "Retry agent", "Compare versions", "Export artifact" |


---

## 4. Surface Inventory

Every UI surface maps to one or more Composition Diagram operations:

| # | Surface | Composition Diagram Operation(s) | Primary Agent(s) Served |
|---|---------|----------------------------------|------------------------|
| S1 | Brief Wizard | `[Brief]` entry po

…(clipped 59636 characters from `ui_design.md`)

### `sources/generic/video.analyst.SPEC.md`

# AnalystAgent

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 81 |
| **pack_id** | `video.analyst` |
| **category** | `10-Sup` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.analyst/` |

## Category roster section (full, from agents.md)

_The following is the complete category section from the master roster (includes peers in the same craft category)._


## 10. Workflow Support Agents

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


## Responsibility

Aggregates business, creative, and technical performance telemetry into decision-ready reports

## Knowledge distillation sources

Platform analytics dashboards; experiment logs; evaluation-harness outputs; benchmark histories

## Self-quality criteria

KPI completeness; forecast-vs-actual variance within tolerance; insight-to-action turnaround

## Surpass-human signal

Detects actionable performance shifts faster than human analyst rotations

## Critique bus

- **Accepts critique from:** SocialMediaStrategistAgent, PerformanceMarketerAgent, EvaluationHarnessAgent

- **Comments on:** Campaign pacing, release timing, retention and ROAS anomalies

## Tools (design-time documentation)

YouTube Analytics, Meta/TikTok Ads dashboards, BI warehouse, benchmark logs

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

ReAct over telemetry + regression analysis

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

## Deep specifications (full embedded content)


### Document: `study/research_agent_functional_specification.md`

_Embedded from `corpus/study/research_agent_functional_specification.md`. Also stored at `sources/study/research_agent_functional_specification.md` under this agent folder._


# Research Agent Functional Specification

## 1. Document Control

- Document title: `Research Agent Functional Specification`
- System name: `grok-research-agent`
- Document type: Current-state functional specification derived from implementation and tests
- Primary delivery model: Local Python CLI application
- Source of truth for this specification: `grok_research_agent/` package implementation, packaged prompts, and automated tests
- Specification intent: Describe the functional behavior the system currently implements, including workflow behavior, file contracts, validation rules, failure handling, and integration points

## 2. Purpose

The system provides a local-first research automation workflow that converts a user-supplied topic into a detailed Markdown research report through a staged pipeline of scope definition, source discovery, source curation, content extraction, notebook assembly, synthesis, optional full-source preservation, final polishing, knowledge compilation, drill-pack generation, image-prompt generation, and YouTube-script generation.

The system is designed to:

- preserve human control at key decision points;
- store all research artifacts locally in resumable session directories;
- use Grok through the xAI OpenAI-compatible API for all LLM generation tasks;
- support optional ingestion of external local documentation as steering context;
- produce inspectable intermediate artifacts rather than a single opaque result.

## 3. Scope

### 3.1 In Scope

- Command-line session lifecycle management
- Persistent session state and artifact storage
- Eight-phase research workflow orchestration
- Optional unattended execution mode
- External-document preprocessing for local steering material
- Knowledge-base compilation into hypergraph and core concepts
- Drill-pack generation from compiled concepts
- Hypergraph updates from newly fed documents
- Mermaid rendering of hypergraph data
- Image-prompt generation from final report content
- YouTube-script generation from final report or section drafts

### 3.2 Out of Scope

- Web UI, API server, or multi-user collaboration
- Authentication, authorization, and role-based permissions
- Database-backed persistence
- Semantic vector search or retrieval index
- Automatic browser automation or crawler orchestration beyond direct HTTP fetch
- Guaranteed factual validation of LLM outputs
- Binary document feeding in the `feed` command beyond best-effort text decoding

## 4. Stakeholders, Roles, and External Actors

### 4.1 Human User Roles

- `Research Operator`: Starts sessions, approves or revises workflow outputs, selects curated sources, optionally chooses full offline collection, and runs auxiliary commands
- `Reviewer/Study User`: Consumes generated report, drill pack, hypergraph, Mermaid output, image prompts, or YouTube script; this role is not technically distinct from the operator

### 4.2 System Actors

- `LLM Provider`: xAI Grok, accessed through the OpenAI-compatible API
- `Remote Content Hosts`: Public websites and PDF endpoints referenced by curated sources
- `Local Filesystem`: Stores sessions, state, outputs, external-doc artifacts, and knowledge-base artifacts
- `Local Environment`: Provides `.env` or environment variables, `EDITOR`, and Python runtime

### 4.3 Access Model

- The system implements no internal user accounts and no permission model.
- Any user who can execute the CLI and read/write the target sessions directory can operate the system fully.

## 5. System Context and Architecture

### 5.1 Core Modules

- `grok_research_agent.cli`
  - Parses CLI arguments
  - Creates `SessionManager` and `WorkflowRunner`
  - Maps command failures to process exit codes
- `grok_research_agent.session_manager`
  - Creates and persists session state
  - Creates unique run directories
  - Provides canonical session and knowledge-base paths
- `grok_research_agent.workflow_phases`
  - Implements the workflow state machine
  - Handles source fetching, extraction, synthesis, compilation, drill-pack generation, feed, show, image generation, and YouTube script generation
- `grok_research_agent.grok_client`
  - Loads environment configuration
  - Calls xAI Grok using the OpenAI client
  - Maps API exceptions into domain-specific runtime errors
- `grok_research_agent.external_docs`
  - Recursively ingests supported local docs
  - Extracts steering context, constraints, requirements, and relevance signals
- `grok_research_agent.prompts/*`
  - Defines output contracts and behavioral instructions for LLM calls

### 5.2 Execution Model

- The product is a single-process CLI application.
- Each command creates a new run directory under the target session.
- Commands operate on files in the session directory and may also write run-local copies for traceability.
- Long-lived state is file-based; there is no background daemon.

## 6. Technology and Runtime Dependencies

- Python runtime: `>=3.11`
- Required packages:
  - `openai`
  - `python-dotenv`
  - `rich`
  - `pydantic>=2`
  - `pypdf`
  - `python-docx`
  - `requests`
  - `beautifulsoup4`
  - `readability-lxml`
  - `chardet<6`
- Packaged CLI entrypoint: `grok-research-agent = grok_research_agent.cli:main`
- Convenience wrappers: root-level `main.py` and `cli.py` forward to packaged CLI entrypoint

## 7. Configuration Specification

### 7.1 Environment Variables

- `GROK_API_KEY`
  - Required for any command path that instantiates `GrokClient`
  - Must be non-empty after whitespace trimming
  - If absent, LLM-backed actions shall fail with a clear message
- `GROK_MODEL`
  - Optional
  - Defaults to `grok-3`
  - Blank values shall be normalized back to `grok-3`
- `GROK_MAX_OUTPUT_TOKENS`
  - Optional integer
  - Defaults to `50000`
  - Invalid or non-numeric values shall revert to `50000`
  - Values below `1` shall be clamped to `1`
- `GROK_REQUEST_TIMEOUT_SECONDS`
  - Optional integer
  - Defaults to `300`
  - Invalid or non-numeric values shall revert to `300`
  - Values below `1` shall be clamped to `1`
- `EDITOR`
  - Optional
  - Used only during Phase 0 `edit` flow
  - If absent, selecting `edit` shall still create the editable temporary file, but no external editor is launched automatically

### 7.2 `.env` Resolution

- When the workflow constructs a default `GrokClient`, it shall attempt to load a `.env` file located two directory levels above the session directory.
- If no `.env` exists there, the system shall continue using process environment variables only.

## 8. User Interface Specification

### 8.1 Interface Type

- Primary interface: terminal/CLI
- Rendering library: `rich`
- Output types:
  - plain status messages
  - Markdown content echoed to console in some phases
  - preview tables for discovery and full-collection selection

### 8.2 Human Interaction Points

- H0: scope confirmation
- H1: curated-source approval
- H2: draft approval or revision instruction
- H3: full-source offline-copy selection

### 8.3 Unattended Mode

- `--auto` shall bypass interactive prompts and drive the workflow to completion where possible.
- In auto mode:
  - H0 is auto-confirmed
  - H1 source selection is set to `all`
  - H1 approval is set to `approve`
  - H2 feedback is set to `approve`
  - H3 selection is controlled by `--auto-full-collection` and defaults to `all`
- Auto mode shall not call `input()`.

## 9. User Roles and Permissions Specification

Because the system has no identity or authorization layer, the functional permission model is:

- any operator can execute any command;
- any operator can create, resume, modify, compile, drill, feed, and finalize sessions they can access on disk;
- there are no restricted admin-only actions;
- there is no audit or attribution model beyond file timestamps and artifact presence.

## 10. CLI Command Functional Requirements

### 10.1 Common Command Behavior

- `FR-CLI-001`: All commands except `list-types` shall require `--sessions-dir`.
- `FR-CLI-002`: Commands that need an existing session shall require `--session-id`.
- `FR-CLI-003`: The CLI shall return exit code `0` for successful completion.
- `FR-CLI-004`: The CLI shall return exit code `1` when `WorkflowRunner.run()` raises `GrokError` or `GrokQuotaError`.
- `FR-CLI-005`: The CLI shall return exit code `2` for unrecognized command dispatch or `argparse` validation failures.
- `FR-CLI-006`: When `--trace-llm` is enabled, request and response content shall be printed in truncated, control-character-sanitized form.

### 10.2 `start`

- `FR-START-001`: The system shall create a new session with topic, optional focus, optional external docs directory, and a persisted `mode`.
- `FR-START-002`: The system shall print the created session ID.
- `FR-START-003`: The system shall immediately invoke workflow execution beginning at the session's current phase, initially Phase 0.
- `FR-START-004`: The accepted `--mode` values shall be `report`, `compiler`, and `drill`.
- `FR-START-005`: The selected `mode` shall be stored in session state but shall not alter runtime workflow behavior in the current implementation.

### 10.3 `resume`

- `FR-RESUME-001`: The system shall load the session and execute from `current_phase`.
- `FR-RESUME-002`: In interactive mode, execution shall stop at the next human checkpoint or after a phase that explicitly instructs the user to resume again.
- `FR-RESUME-003`: If `current_phase >= 8`, the system shall print `Session is complete.`

### 10.4 `list-sessions`

- `FR-LIST-001`: The system shall list directories under `--sessions-dir` that contain `session.json`.
- `FR-LIST-002`: The listing shall exclude non-directory entries and directories missing `session.json`.
- `FR-LIST-003`: If no sessions exist, the system shall print `No sessions found.`

### 10.5 `list-types`

- `FR-TYPES-001`: The system shall print `auto-hypergraph`.
- `FR-TYPES-002`: No session directory argument shall be required for this command.

### 10.6 `update`

- `FR-UPDATE-001`: The system shall run discovery with `since_last_run=yes`.
- `FR-UPDATE-002`: On completion, the system shall set `current_phase = 2`.
- `FR-UPDATE-003`: The system shall instruct the user to resume in order to curate sources.

### 10.7 `synthesize`

- `FR-SYNTH-001`: The system shall force execution of Phase 5 synthesis regardless of current phase.
- `FR-SYNTH-002`: Phase 5 prerequisites still apply; if notebook input is missing, synthesis shall not proceed.

### 10.8 `compile`

- `FR-COMPILE-001`: The CLI shall expose `--type auto-hypergraph`.
- `FR-COMPILE-002`: The workflow shall accept `auto-hypergraph` and internally tolerate additional dormant auto-type strings, but only `auto-hypergraph` is exposed and supported end-to-end.
- `FR-COMPILE-003`: The system shall compile from `04_master_notebook.md` when present and append any `03_extracted/*.md` content when present.
- `FR-COMPILE-004`: If no notebook or extracted content exists, the system shall print `Missing notebook or extractions. Resume the session to generate them first.` and stop.

### 10.9 `drill`

- `FR-DRILL-001`: The only supported mode shall be `backward`.
- `FR-DRILL-002`: If `core_concepts.json` is absent, the system shall attempt `compile` automatically.
- `FR-DRILL-003`: If core concepts are still absent after compile, the system shall print `Missing core concepts. Run compile first.`

### 10.10 `feed`

- `FR-FEED-001`: The command shall require `--new-doc`.
- `FR-FEED-002`: If the file does not exist or is not a regular file, the system shall print `File not found: <path>` and stop.
- `FR-FEED-003`: The system shall copy the file into `knowledge_base/feed_docs/` with a timestamp prefix.
- `FR-FEED-004`: If no `hypergraph.json` exists, the system shall invoke compile and then return without performing a merge update.

### 10.11 `show`

- `FR-SHOW-001`: If `knowledge_base/hypergraph.json` does not exist, the system shall print `Missing hypergraph.json. Run compile first.`
- `FR-SHOW-002`: Otherwise, the system shall generate `knowledge_base/hypergraph.mmd`.

### 10.12 `generate-images`

- `FR-IMG-001`: The command shall require `FINAL_REPORT.md`.
- `FR-IMG-002`: If `FINAL_REPORT.md` is missing, the system shall print `Missing FINAL_REPORT.md`.
- `FR-IMG-003`: On success, the system shall write `images_to_generate.md` in both the run directory and session directory.

### 10.13 `youtube-script`

- `FR-YT-001`: The command shall require `FINAL_REPORT.md`.
- `FR-YT-002`: If `FINAL_REPORT.md` is missing, the system shall print `Missing FINAL_REPORT.md`.
- `FR-YT-003`: On success, the system shall write `Youtube_Script.md` in both the run directory and session directory.

## 11. Session Management Specification

### 11.1 Session Identity

- `FR-SESSION-001`: Session IDs shall be generated from a slugified topic plus current date in `YYYYMMDD` format.
- `FR-SESSION-002`: Slugification shall lowercase the topic, replace non-alphanumeric characters with `-`, collapse repeated hyphens, and strip leading/trailing hyphens.
- `FR-SESSION-003`: If the slug exceeds the configured prefix length, the system shall trim it and append an 8-character SHA-1 digest suffix.
- `FR-SESSION-004`: If a generated session directory already exists, the system shall append `-2`, `-3`, and so on until unique.

### 11.2 Session State

The persisted `SessionState` shall contain:

- `session_id`
- `topic`
- `focus`
- `mode`
- `external_docs_dir`
- `external_docs_status`
- `external_docs_summary`
- `external_docs_manifest_path`
- `external_docs_context_path`
- `external_docs_processed_files`
- `external_docs_total_files`
- `external_docs_completion_rate`
- `external_docs_relevance_score`
- `external_docs_last_error`
- `created_at`
- `grok_model`
- `current_phase`
- `run_history`
- `updated_at`

### 11.3 Session Persistence Rules

- `FR-SESSION-005`: The system shall persist state to `session.json` encoded as UTF-8 JSON.
- `FR-SESSION-006`: `updated_at` shall be refreshed on each `save_state()`.
- `FR-SESSION-007`: The sessions directory and knowledge-base subdirectories shall be created automatically when saving.
- `FR-SESSION-008`: `run_history` shall be initialized as an empty list but is not populated by current workflow code.

### 11.4 Run Directory Rules

- `FR-RUN-001`: Each command execution that creates a `WorkflowContext` shall create a new run directory under `runs/`.
- `FR-RUN-002`: Run directory names shall use timestamp format `YYYYMMDD_HHMMSS_microseconds`.
- `FR-RUN-003`: If a timestamp collision occurs, the system shall retry up to 1000 times.
- `FR-RUN-004`: If a unique run directory cannot be created within 1000 attempts, the system shall raise `RuntimeError`.

## 12. External Document Preprocessing Specification

### 12.1 Feature Purpose

The external-doc subsystem ingests local reference documents before workflow execution and converts them into mandatory steering context that can influence scope, discovery, curation, extraction, and planning.

### 12.2 Trigger Rules

- `FR-EXT-001`: External-doc preprocessing shall run automatically before workflow commands except `generate-images`, `youtube-script`, `compile`, `drill`, `feed`, and `show`.
- `FR-EXT-002`: If `external_docs_dir` is blank or absent, preprocessing shall be skipped.
- `FR-EXT-003`: If session state already marks preprocessing as `completed` and a summary exists, preprocessing shall not re-run automatically.

### 12.3 Supported Inputs

- Supported suffixes: `.pdf`, `.docx`, `.txt`, `.md`
- Discovery behavior: recursive under the provided root directory
- Unsupported file types: ignored rather than errored

### 12.4 Processing Rules

- `FR-EXT-004`: Each supported file shall be read using type-appropriate logic.
- `FR-EXT-005`: PDF extraction shall iterate pages and skip pages whose text extraction fails.
- `FR-EXT-006`: DOCX extraction shall concatenate non-empty paragraphs.
- `FR-EXT-007`: TXT and Markdown shall be read as UTF-8 with replacement for invalid characters.
- `FR-EXT-008`: Each document shall be categorized as `guideline`, `background`, `steering`, or `general` based on filename keywords.
- `FR-EXT-009`: The processor shall extract key concepts, constraints, requirements, and algorithm insights from sentence-level heuristics.
- `FR-EXT-010`: The processor shall compute a relevance score from topic/focus lexical overlap plus structural bonuses for relevant terms, extracted constraints, and extracted requirements.

### 12.5 Aggregated Outputs

- `FR-EXT-011`: The system shall write:
  - `external_docs/manifest.json`
  - `external_docs/extracted.json`
  - `external_docs/context.md`
- `FR-EXT-012`: `manifest.json` shall include per-file processing results and aggregate success metrics.
- `FR-EXT-013`: `context.md` shall include sections for key concepts, constraints, requirements, optional algorithm enhancement notes, and workflow guidance.
- `FR-EXT-014`: If topic or focus text matches algorithm-oriented keywords, algorithm enhancement notes shall be included; otherwise they shall be omitted.

### 12.6 Status Rules

- `FR-EXT-015`: If the external-doc root directory does not exist or is not a directory, status shall be set to `failed`, an explanatory error shall be stored in session state, and the workflow shall continue.
- `FR-EXT-016`: If individual files fail, those files shall be marked `failed`, but aggregate processing shall continue.
- `FR-EXT-017`: Aggregate status shall be:
  - `completed` when all discovered files process successfully
  - `partial` when at least one file succeeds and at least one fails
  - `failed` when zero files succeed

### 12.7 Prompt Injection Rules

- `FR-EXT-018`: When available, external-doc summary content shall be appended to relevant prompts as mandatory steering/background material.
- `FR-EXT-019`: External-doc context shall be truncated to phase-specific character budgets instead of causing failures.

## 13. Research Workflow State Machine

### 13.1 State Definitions

- Phase `0`: Scope generation and confirmation
- Phase `1`: Discovery
- Phase `2`: Curation and gap analysis
- Phase `3`: Extraction
- Phase `4`: Notebook assembly
- Phase `5`: Synthesis and review
- Phase `6`: Full offline collection selection
- Phase `7`: Final polish
- Phase `8`: Complete

### 13.2 Interactive Progression Rules

- `FR-STATE-001`: In interactive mode, the workflow shall process one phase or one human checkpoint per `resume` call according to `_run_until_human_step()`.
- `FR-STATE-002`: Some phases end by instructing the user to resume later instead of continuing automatically.
- `FR-STATE-003`: Phase transitions shall be persisted immediately when the code explicitly updates `current_phase`.

### 13.3 Auto-Mode Progression Rules

- `FR-STATE-004`: In auto mode, the workflow shall loop until `current_phase >= 8`.
- `FR-STATE-005`: Auto mode shall continue immediately across phases without requiring separate `resume` commands.

## 14. Phase-by-Phase Functional Requirements

### 14.1 Phase 0 - Scope Confirmation

- `FR-P0-001`: The system shall generate a Markdown scope summary using `scope_prompt.txt`.
- `FR-P0-002`: The generated scope shall be written to `<run>/00_scope.md`.
- `FR-P0-003`: The generated scope shall be printed to the console.
- `FR-P0-004`: In auto mode, the scope shall be accepted immediately, saved as `00_scope_confirmed.md`, and `current_phase` shall advance to `1`.
- `FR-P0-005`: In interactive mode, valid user inputs are `yes`, `edit`, and `cancel`.
- `FR-P0-006`: `cancel` shall terminate the phase without changing `current_phase`.
- `FR-P0-007`: `edit` shall write a temporary `00_scope_edit.md`, optionally invoke the `EDITOR`, reload the edited content, print it, and continue prompting.
- `FR-P0-008`: `yes` shall save `00_scope_confirmed.md`, set `current_phase = 1`, save state, and instruct the user to resume.
- `FR-P0-009`: If Grok client creation fails, the system shall print the error plus a `.env` guidance message and return without changing state.

### 14.2 Phase 1 - Discovery

- `FR-P1-001`: The system shall render `discovery_prompt.txt` with topic, effective focus, and `since_last_run`.
- `FR-P1-002`: Discovery output shall be written to both `<run>/01_discovery_table.md` and `<session>/01_discovery_table.md`.
- `FR-P1-003`: The system shall not validate discovery table format before saving.
- `FR-P1-004`: In normal interactive progression, completion of Phase 1 shall set `current_phase = 2` and instruct the user to resume for curation.

### 14.3 Phase 2 - Curation and Gap Analysis

- `FR-P2-001`: Phase 2 shall require `01_discovery_table.md`; if missing, the system shall print `Missing discovery table. Resume from Phase 1.` and stop.
- `FR-P2-002`: The system shall print a preview table containing up to the first 80 non-empty lines of discovery output.
- `FR-P2-003`: The user instruction string may contain free-form source-selection text, including numbers, `all`, `add <urls>`, `remove <indexes>`, or `gap`; the system does not parse these commands locally and instead passes them to the LLM.
- `FR-P2-004`: The system shall attempt curated-source generation up to 3 times.
- `FR-P2-005`: On retry attempts after the first failure, the prompt shall add stricter JSON-only instructions and a top-20 limit.
- `FR-P2-006`: Curated-source output shall be canonicalized into a list of objects with keys:
  - `title`
  - `url`
  - `type`
  - `why_relevant`
  - `credibility`
  - `priority`
- `FR-P2-007`: URLs shall be normalized by trimming quotes/backticks and removing trailing punctuation where possible.
- `FR-P2-008`: If the LLM returns invalid JSON or a non-canonical structure on all attempts, the system shall recover URLs heuristically from the discovery Markdown and build fallback source entries.
- `FR-P2-009`: Run-local curation output shall be written verbatim to `<run>/02_curated_sources.json`.
- `FR-P2-010`: Session-local curation output shall be re-written as canonical JSON to `<session>/02_curated_sources.json`.
- `FR-P2-011`: Gap analysis shall always be attempted using the curated list and saved to `<run>/02_gap_report.md`.
- `FR-P2-012`: If gap analysis times out, the saved gap report shall contain `# Gaps` and an explicit timeout note.
- `FR-P2-013`: Phase advancement to `3` shall occur only when the approval input is exactly `approve`.
- `FR-P2-014`: Any other approval response shall leave the session in Phase 2 and instruct the user to repeat curation later.

### 14.4 Phase 3 - Extraction

- `FR-P3-001`: Phase 3 shall require `02_curated_sources.json`; if missing, the system shall print `Missing curated sources. Resume from Phase 2.`
- `FR-P3-002`: If curated-source JSON exists but canonicalization produces an empty list, the system shall print `Curated sources file is invalid or empty. Resume from Phase 2 to re-curate sources.`
- `FR-P3-003`: The system shall create the following directories in both run and session scopes as applicable:
  - `03_extracted/`
  - `03_source_snapshots/`
  - `03_extracted_chunks/`
- `FR-P3-004`: The system shall request an extraction plan and save it as `<run>/03_extraction_plan.md`.
- `FR-P3-005`: If extraction-plan generation times out, the system shall save a placeholder plan instead of failing.
- `FR-P3-006`: The system shall prefetch source bundles concurrently using up to `4` fetch workers.
- `FR-P3-007`: If an individual source fetch fails during prefetch, the system shall print a warning and continue extracting remaining sources.
- `FR-P3-008`: For each successfully fetched source, the system shall save raw content and normalized source text snapshots in both run and session directories.
- `FR-P3-009`: Snapshot headers shall preserve title, URL, host, type, priority, and credibility metadata.
- `FR-P3-010`: HTML source bundles shall save raw snapshots with `.html`; PDF bundles with `.pdf`; all others with `.txt`.
- `FR-P3-011`: Source text shall be chunked with:
  - max chunk size `45000` characters
  - overlap `5000` characters
- `FR-P3-012`: Chunk extraction shall run in parallel using up to `2` extraction workers.
- `FR-P3-013`: Each chunk prompt shall require strict Markdown sections for coverage summary, terminology, mechanisms, workflows, evidence, limitations, open questions, quotable passages, and extraction notes.
- `FR-P3-014`: If an extraction chunk times out, that chunk shall be skipped and extraction shall continue for other chunks.
- `FR-P3-015`: Each successful extracted chunk shall be written to both run and session `03_extracted_chunks/`.
- `FR-P3-016`: If all chunks for a source fail, the system shall print a warning and skip generating that source dossier.
- `FR-P3-017`: Successful source dossiers shall be assembled into `03_extracted/<nnn>.md` in both run and session directories.
- `FR-P3-018`: On phase completion, the system shall write `<session>/03_extracted_index.txt` with a generation marker.

### 14.5 Phase 4 - Notebook Assembly

- `FR-P4-001`: Phase 4 shall require existence of `<session>/03_extracted/`; otherwise it shall print `No extracted sources found in this run. Resume from Phase 3.`
- `FR-P4-002`: The notebook shall include:
  - top heading `# Master Notebook`
  - topic line
  - notebook purpose section
  - optional external documentation context section
  - source catalog section
  - optional knowledge-base outline
  - source dossiers section
- `FR-P4-003`: The notebook shall concatenate parts using `---` separators.
- `FR-P4-004`: The notebook shall be written to both `<run>/04_master_notebook.md` and `<session>/04_master_notebook.md`.
- `FR-P4-005`: In interactive progression, successful notebook generation shall set `current_phase = 5`.

### 14.6 Phase 5 - Synthesis and Review

- `FR-P5-001`: Phase 5 shall require `04_master_notebook.md`; if missing, the system shall print `Missing notebook. Resume from Phase 4.`
- `FR-P5-002`: The notebook shall be split into chunks of up to `70000` characters with `5000` overlap.
- `FR-P5-003`: If no notebook chunks are produced, the system shall print `Notebook is empty. Resume from Phase 4.`
- `FR-P5-004`: For each report section in the fixed section list, the system shall build section-specific evidence packets from notebook chunks.
- `FR-P5-005`: Standard report sections shall be:
  - `Core Definitions and Scope`
  - `Architecture and Technical Mechanisms`
  - `Workflows, Processes, and Operational Patterns`
  - `Evidence, Examples, and Case Studies`
  - `Limitations, Trade-offs, and Failure Modes`
  - `Open Questions and Future Directions`
- `FR-P5-006`: Evidence-packet generation shall run with up to `2` workers per section.
- `FR-P5-007`: Evidence packets shall be saved in both run and session `05_section_evidence/` directories.
- `FR-P5-008`: If no evidence packets are generated for a section, that section shall be skipped with a warning.
- `FR-P5-009`: Each successfully drafted section shall be written to both run and session `05_section_drafts/`.
- `FR-P5-010`: The draft report shall include scope/coverage text, source catalog, drafted sections, optional knowledge-base alignment, and references.
- `FR-P5-011`: Draft versions shall be saved as incrementing `05_draft_vN.md`.
- `FR-P5-012`: The review prompt shall tell the user they may enter `approve | revise <section> <feedback> | add-section "Title" | gap-check`.
- `FR-P5-013`: Only exact response `approve` shall advance the session to Phase 6.
- `FR-P5-014`: Any non-`approve` response shall be treated as general revision feedback and passed to the revision prompt without local parsing.
- `FR-P5-015`: If revision generation times out, the prior draft shall remain authoritative and phase state shall not advance.
- `FR-P5-016`: Successful revision output shall be stored as the next draft version and require another review cycle.

### 14.7 Phase 6 - Full Offline Collection

- `FR-P6-001`: Phase 6 shall attempt to load curated sources from `02_curated_sources.json`.
- `FR-P6-002`: If curated sources are absent, the system shall attempt heuristic URL recovery from `01_discovery_table.md`.
- `FR-P6-003`: If no curated sources can be recovered, the system shall set `current_phase = 7`, save state, print a skip message, and require a subsequent resume for finalization.
- `FR-P6-004`: The source selection UI shall display index, title, and URL for each curated source.
- `FR-P6-005`: Valid practical inputs are `all`, `none`, or comma-separated integers; non-numeric tokens shall be ignored.
- `FR-P6-006`: Response `none` shall set `current_phase = 7`, save state, print a skip message, and return without finalizing automatically.
- `FR-P6-007`: Response `all` shall select all sources.
- `FR-P6-008`: Numeric selections outside valid index range shall be ignored.
- `FR-P6-009`: Selected sources shall be prefetched before writing full offline copies.
- `FR-P6-010`: For each successfully fetched selected source, the system shall write `06_full_sources/<nnn>.md` in both run and session directories.
- `FR-P6-011`: If a selected source cannot be fetched, that source shall be skipped without aborting the phase.
- `FR-P6-012`: After writing at least the attempted full-collection outputs, the system shall set `current_phase = 7`, invoke final polish immediately, then set `current_phase = 8`.

### 14.8 Phase 7 - Final Polish

- `FR-P7-001`: Final polish shall require both `04_master_notebook.md` and at least one `05_draft_v*.md`; otherwise it shall print `Missing notebook or draft.`
- `FR-P7-002`: The latest draft file by lexicographic version ordering shall be used as the report body source.
- `FR-P7-003`: The system shall generate an executive summary using `final_polish_prompt.txt`.
- `FR-P7-004`: If executive-summary generation times out, the system shall substitute a timeout placeholder message.
- `FR-P7-005`: The system shall generate a glossary using `glossary_prompt.txt`.
- `FR-P7-006`: If glossary generation times out, the system shall substitute a timeout placeholder bullet.
- `FR-P7-007`: If the latest draft begins with a level-1 heading, that heading shall be removed before final report assembly.
- `FR-P7-008`: The system shall build a Markdown table of contents from all level-2 headings in the report body.
- `FR-P7-009`: The final report shall contain:
  - level-1 final report heading
  - table of contents
  - executive summary
  - main body
  - source catalog
  - optional knowledge-base overview
  - glossary
- `FR-P7-010`: The system shall attempt to retarget word count twice if needed:
  - once on the body
  - once on the complete assembled report
- `FR-P7-011`: Final report word-count targets shall be:
  - minimum `9000`
  - maximum `10000`
  - target `9500`
- `FR-P7-012`: Word-count correction shall preserve headings and core claims while expanding or compressing content.
- `FR-P7-013`: The final report shall be written to both `<run>/FINAL_REPORT.md` and `<session>/FINAL_REPORT.md`.
- `FR-P7-014`: The system shall then attempt image-prompt generation and YouTube-script generation.

### 14.9 Phase 8 - Complete

- `FR-P8-001`: A session with `current_phase >= 8` shall be treated as complete.
- `FR-P8-002`: Resume on a completed session shall print `Session is complete.`

## 15. Source Fetching and Transformation Specification

### 15.1 URL Validation

- `FR-FETCH-001`: URLs shall be normalized before validation.
- `FR-FETCH-002`: Only `http` and `https` URLs with a network location shall be accepted.
- `FR-FETCH-003`: Invalid URLs shall raise `ValueError`.

### 15.2 HTTP Fetch Rules

- `FR-FETCH-004`: HTTP fetches shall use a user agent string `grok-research-agent/0.1`.
- `FR-FETCH-005`: Redirects shall be followed.
- `FR-FETCH-006`: Timeout shall be split into connect timeout and read timeout.
- `FR-FETCH-007`: Request timeouts shall raise `TimeoutError` with URL context.

### 15.3 Content-Type Handling

- `FR-FETCH-008`: PDF detection shall use either `Content-Type: application/pdf` or `.pdf` URL suffix.
- `FR-FETCH-009`: PDF bundles shall return extracted text as raw, main, full, and analysis text.
- `FR-FETCH-010`: Non-HTML non-PDF responses shall be treated as plain text.
- `FR-FETCH-011`: HTML responses shall generate:
  - `main_text` from `readability-lxml` summary when available
  - `full_text` from full-page HTML text extraction
  - `analysis_text` as merged main/full text or fallback content

### 15.4 HTML Text Normalization

- `FR-FETCH-012`: HTML extraction shall remove `script`, `style`, `noscript`, and `svg` tags.
- `FR-FETCH-013`: Duplicate normalized lines shall be removed to reduce repeated boilerplate.

## 16. Knowledge Compilation Specification

### 16.1 Compiler Inputs and Outputs

- `FR-KB-001`: Compile shall use notebook content first and then append extracted source dossiers when available.
- `FR-KB-002`: Hypergraph compilation shall use only the first `220000` characters of content.
- `FR-KB-003`: Core-concept extraction shall use:
  - first `220000` characters of source content
  - first `120000` characters of hypergraph JSON
- `FR-KB-004`: Compile outputs shall be written to:
  - `knowledge_base/hypergraph.json`
  - `knowledge_base/auto_types/auto_hypergraph.json`
  - `knowledge_base/core_concepts.json`

### 16.2 Hypergraph Contract

- `FR-KB-005`: Prompted hypergraph schema shall be:

```json
{
  "nodes": [{"id": "N1", "label": "..."}],
  "hyperedges": [{"id": "E1", "nodes": ["N1", "N2", "N3"], "relation": "...", "evidence": "..."}]
}
```

- `FR-KB-006`: If the LLM does not return valid JSON, the system shall persist a fallback JSON wrapper, typically `{ "raw": "<response>" }`, instead of failing the command.

### 16.3 Core Concepts Contract

- `FR-KB-007`: Prompted core-concepts schema shall be:

```json
{
  "core_concepts": [
    {
      "name": "...",
      "definition": "...",
      "why_load_bearing": "..."
    }
  ]
}
```

- `FR-KB-008`: The prompt requires exactly 7 concepts, but the implementation does not independently enforce the count after generation.

### 16.4 Drill-Pack Contract

- `FR-KB-009`: Drill-pack prompt output schema shall be:

```json
{
  "drill_pack_markdown": "markdown string",
  "drill_questions": [
    {
      "concept": "...",
      "questions": [
        {
          "question": "...",
          "answer": "...",
          "pitfalls": ["...", "..."]
        }
      ]
    }
  ]
}
```

- `FR-KB-010`: If `drill_pack_markdown` is missing or blank, the system shall strip code fences from the raw response and use the remainder as Markdown output.
- `FR-KB-011`: If the parsed JSON lacks `drill_questions`, the entire parsed object shall be written as `drill_questions.json`.

### 16.5 Feed and Hypergraph Update

- `FR-KB-012`: Feed shall read the new document using UTF-8 with replacement for decoding errors.
- `FR-KB-013`: Feed merge prompts shall receive:
  - first `160000` characters of existing hypergraph JSON
  - first `160000` characters of new document content
- `FR-KB-014`: Updated hypergraph output shall overwrite both canonical hypergraph locations.

### 16.6 Mermaid Rendering

- `FR-KB-015`: Mermaid output shall begin with `graph TD`.
- `FR-KB-016`: Node rendering shall use up to the first `200` nodes.
- `FR-KB-017`: Edge rendering shall use up to the first `400` edges or hyperedges.
- `FR-KB-018`: For hyperedges with more than two members, Mermaid rendering shall connect only the first two listed nodes.
- `FR-KB-019`: Edge labels shall use `relation` or `label` when present.

## 17. Final Report, Image Prompt, and YouTube Script Specification

### 17.1 Final Report Output Contract

- `FR-OUT-001`: The final report shall be a Markdown document named `FINAL_REPORT.md`.
- `FR-OUT-002`: The final report shall include explicit `## Executive Summary` and `## Source Catalog` sections.
- `FR-OUT-003`: If knowledge-base content exists, the report shall also include `## Knowledge Base Overview`.
- `FR-OUT-004`: The report shall end with a glossary section even if glossary generation timed out.

### 17.2 Image Prompt Generation

- `FR-OUT-005`: Image prompts shall be generated from the complete final report.
- `FR-OUT-006`: The prompt contract requests 5 to 10 image prompts emphasizing concrete mechanisms, workflows, architectures, comparisons, and evidence rather than generic concept art.
- `FR-OUT-007`: If image-prompt generation times out during final polish, report creation shall still succeed.

### 17.3 YouTube Script Generation

- `FR-OUT-008`: The system shall derive YouTube sections primarily from `05_section_drafts/` when available; otherwise it shall derive them from `FINAL_REPORT.md`.
- `FR-OUT-009`: The following report sections shall be excluded from narration source selection:
  - `Table of Contents`
  - `Source Catalog`
  - `Glossary`
  - `References`
  - `Knowledge Base Overview`
  - `Executive Summary`
- `FR-OUT-010`: The generated script shall contain:
  - top heading `# YouTube Script`
  - `## Introduction`
  - one level-2 heading per selected section
  - `## Conclusion`
- `FR-OUT-011`: If intro or outro generation times out, the system shall insert fallback placeholder narration instead of failing.
- `FR-OUT-012`: If a section generation times out, that section may be omitted while the rest of the script proceeds.
- `FR-OUT-013`: Short intro, section, or outro outputs shall be expanded by a secondary LLM call to hit minimum detail thresholds.
- `FR-OUT-014`: If a generated section lacks a Markdown heading, the system shall prepend the required heading automatically.

## 18. Input and Output File Specification

### 18.1 Session Root Outputs

The session root may contain:

- `session.json`
- `00_scope_confirmed.md`
- `01_discovery_table.md`
- `02_curated_sources.json`
- `03_extracted/`
- `03_source_snapshots/`
- `03_extracted_chunks/`
- `03_extracted_index.txt`
- `04_master_notebook.md`
- `05_section_evidence/`
- `05_section_drafts/`
- `05_draft_vN.md`
- `06_full_sources/`
- `FINAL_REPORT.md`
- `images_to_generate.md`
- `Youtube_Script.md`
- `external_docs/`
- `knowledge_base/`
- `runs/`

### 18.2 Knowledge Base Outputs

- `knowledge_base/hypergraph.json`
- `knowledge_base/core_concepts.json`
- `knowledge_base/drill_pack.md`
- `knowledge_base/drill_questions.json`
- `knowledge_base/hypergraph.mmd`
- `knowledge_base/auto_types/auto_hypergraph.json`
- `knowledge_base/feed_docs/<timestamp>_<original_name>`

### 18.3 Run-Scoped Outputs

- Each command execution that builds a workflow context may create run-local copies of generated artifacts for traceability and debugging.

## 19. Validation Rules

### 19.1 CLI Validation

- Required flags shall be enforced by `argparse`.
- Unsupported `compile --type` values exposed via CLI cannot pass parser validation.
- Unsupported `drill --mode` values exposed via CLI cannot pass parser validation.

### 19.2 Semantic Validation

- Curated-source validation is structural and best-effort, not strict schema validation via a dedicated validator.
- Discovery output is not structurally validated.
- Final report content is not semantically validated for factual correctness.
- Core concept count is prompt-constrained but not post-validated.

### 19.3 File Validation

- `feed` validates file existence and regular-file status.
- External docs validate root directory existence and supported suffixes.
- Session listing validates presence of `session.json`.

## 20. Error Handling and Recovery Specification

### 20.1 Grok API Errors

- `FR-ERR-001`: Missing API key shall raise `GrokError("Missing GROK_API_KEY in .env or environment")`.
- `FR-ERR-002`: Quota/billing-related API errors shall be mapped to `GrokQuotaError` with actionable text.
- `FR-ERR-003`: Timeout-like API errors shall be mapped to `GrokTimeoutError` including configured timeout seconds.
- `FR-ERR-004`: Non-timeout non-quota API failures shall be retried up to `5` times with exponential backoff capped at `30` seconds.
- `FR-ERR-005`: Quota and timeout errors are not retried in `GrokClient.chat_text()` once mapped.

### 20.2 LLM Timeout Tolerance

- `FR-ERR-006`: Selected phases use `_llm_optional()` to convert LLM timeout failures into warnings and continue:
  - gap analysis
  - extraction plan
  - extraction chunks
  - section evidence packets
  - section drafts
  - revision
  - executive summary
  - glossary
  - image prompts
  - YouTube intro/segments/outro
  - word-count retargeting
- `FR-ERR-007`: When `_llm_optional()` handles a timeout, the system shall print a warning and continue unless the calling feature requires explicit output to proceed.

### 20.3 Source Fetch Errors

- `FR-ERR-008`: Source fetch failures shall not abort the whole extraction or full-collection phase.
- `FR-ERR-009`: A timed-out fetch shall raise `TimeoutError`; callers may log and skip the source.

### 20.4 JSON Robustness

- `FR-ERR-010`: The system shall strip Markdown code fences when attempting to parse JSON-like model outputs.
- `FR-ERR-011`: The system shall attempt direct parse, bracket-slice parse, and brace-slice parse before falling back to raw wrapper JSON.
- `FR-ERR-012`: Invalid curated-source JSON shall trigger heuristic recovery from discovery links.

### 20.5 Non-Fatal Degradation Rules

- `FR-ERR-013`: Missing external docs shall not block the research workflow.
- `FR-ERR-014`: Missing curated sources in Phase 6 shall downgrade to skip behavior rather than fatal failure.
- `FR-ERR-015`: Missing hypergraph or core concepts shall produce instructional console messages rather than uncaught failures.
- `FR-ERR-016`: Missing final report for image or YouTube generation shall produce instructional console messages.

## 21. Integration Specifications

### 21.1 xAI Grok Integration

- Protocol: OpenAI-compatible chat completions API
- Base URL: `https://api.x.ai/v1`
- Auth: bearer API key supplied via environment
- Message structure: one system message and one user message per call
- Response handling: first completion choice message content or empty string

### 21.2 Remote Web Integration

- Protocol: HTTP/HTTPS GET
- Redirects: enabled
- Authentication: none
- SSL behavior: delegated to `requests`
- Failure handling: errors bubble to caller or are caught per phase and downgraded to warnings where designed

### 21.3 Local Document Integration

- External docs support `.pdf`, `.docx`, `.txt`, `.md`
- Feed command support is broader at file-opening level but uses text decoding and is intended for textual documents

## 22. Security and Privacy Requirements

- `FR-SEC-001`: API keys shall be read from environment or `.env`; the system shall not write them into session artifacts.
- `FR-SEC-002`: Research session directories may store fetched remote content and locally processed external docs; those files shall be considered potentially sensitive.
- `FR-SEC-003`: The system performs no secret redaction on fetched content before storage.
- `FR-SEC-004`: The system performs no access control on session directories.

## 23. Non-Functional Constraints with Functional Impact

- Local-first persistence means all critical artifacts must be inspectable on disk after each major step.
- Resumability depends on `current_phase` and file presence rather than transaction logs or DB state.
- Determinism is partial: filenames and workflow transitions are deterministic, but content is LLM-generated and therefore probabilistic.
- Concurrency is limited and bounded:
  - fetch workers: `4`
  - extraction workers: `2`
  - section-evidence workers: `2`
- Large text handling uses character-based truncation and chunking rather than token-precise segmentation.

## 24. Current Implementation Notes and Known Functional Gaps

- `mode` is stored in session state but does not currently change system behavior.
- `run_history` exists in the session schema but is not populated.
- `list-types` exposes only `auto-hypergraph` even though internal constants list several dormant auto types.
- The interactive guidance strings mention `add-section` and `gap-check`, but no local parser enforces those commands; they are passed verbatim as revision feedback.
- The final report includes a generated table of contents derived only from level-2 headings.
- Mermaid generation simplifies hyperedges to pairwise links using only the first two members.
- Discovery and final-report factual accuracy depend on model output and source quality; the system does not perform automated fact verification.

## 25. Acceptance Criteria

The current implementation shall be considered functionally complete for its intended scope when all of the following are true:

- A new session can be created with a unique session ID and persisted `session.json`.
- Interactive workflow progression can move the session from Phase 0 through Phase 8 with the expected human checkpoints.
- Auto mode can complete the workflow without calling `input()`.
- Discovery creates `01_discovery_table.md`.
- Curation creates `02_curated_sources.json` and a gap report.
- Extraction creates source snapshots, extracted chunks, and source dossiers.
- Notebook assembly creates `04_master_notebook.md`.
- Synthesis creates at least one `05_draft_vN.md`.
- Final polish creates `FINAL_REPORT.md`.
- Final polish or explicit commands can create `images_to_generate.md` and `Youtube_Script.md`.
- Compile creates hypergraph and core-concepts outputs under `knowledge_base/`.
- Drill creates `drill_pack.md` and `drill_questions.json`.
- Feed stores a timestamped document copy and can update or initialize hypergraph output.
- Show creates `hypergraph.mmd`.
- External docs, when supplied, are processed into manifest, extracted summary, and context outputs without blocking the workflow on partial failures.

## 26. Traceability Summary

This specification reflects the behavior implemented in:

- `grok_research_agent/cli.py`
- `grok_research_agent/session_manager.py`
- `grok_research_agent/grok_client.py`
- `grok_research_agent/external_docs.py`
- `grok_research_agent/workflow_phases.py`
- `grok_research_agent/prompts/*.txt`
- `tests/test_cli.py`
- `tests/test_session_manager.py`
- `tests/test_external_docs.py`
- `tests/test_workflow_happy_path.py`



## Additional corpus / va passages naming this agent


### From `corpus/study/SYSTEM_REFERENCE.md` Copy: `sources/excerpts/SYSTEM_REFERENCE.md`.


| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 46 | PromptEngineerAgent | Crafts prompts; steers gen models | — |
| 47 | AvatarDesignAgent | Synthetic presenter identity | — |
| 48 | VoiceCloneAgent / LipSync | Voice cloning + lip-sync | — |
| 49 | AIQAConsistencyAgent | Frame drift, artifacts, identity breaks | — |
| 50 | PersonalizationEngineerAgent | Variable templates (name/face swap) | — |
| 51 | TrailerEditorAgent | Hook-driven trailer cuts | — |
| 52 | SportsAnalystAgent | Tactical breakdowns + diagrams | — |



### From `corpus/study/ai_agent_video_production_workflow.md` Copy: `sources/excerpts/ai_agent_video_production_workflow.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 28 | **SocialMediaStrategistAgent** | Platform-native distribution, timing, trends | TikTok Creator Portal data; Meta Marketing Science; Tubular/Sensor Tower | Predicted-vs-actual reach error; trend-timing latency <2h | Beats agency social leads on 30-day reach lift | AnalystAgent, BrandAgent | CopywriterAgent (off-platform tone), EditorAgent (wrong aspect) |
| 29 | **CopywriterAgent** | Scripts, captions, hooks, headlines | D&AD/One Show winners; *Ogilvy on Advertising*; Joanna Wiebe Copyhackers | Reading grade; hook-curiosity score; brand-voice cosine similarity ≥0.85 | Wins D&AD-style blind preference on ad copy briefs | BrandAgent, PerformanceMarketerAgent | ScriptwriterAgent (verbosity), VOArtist (unspeakable) |
| 30 | **CreativeDirectorAgent** | Campaign concept; cross-discipline taste | Cannes Lions Grand Prix archive; D&AD Pencils; agency case studies | Concept distinctiveness (embedding novelty vs category prior); award-rubric predicted score | Wins Cannes-jury-emulator gold vs human-agency shortlists | ClientAgent, BrandAgent | CopywriterAgent, ArtDirectorAgent |
| 31 | **PerformanceMarketerAgent** | Optimize ads for ROAS | Meta Blueprint; TikTok Ads Academy; MMM literature | ROAS uplift vs control; statistical significance ≥95% | Beats senior media buyer on 30-day ROAS at equal spend | AnalystAgent, FinanceAgent | UGCAgent (low hook), CopywriterAgent (weak CTA) |

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
| 51 | **TrailerEditorAgent** | Hook-driven trailer cuts | Golden Trailer Awards archive; Mark Woollen / AV Squad public reels; trailer-music libraries | Hook-rate at 3s; rising-action curve fit; music-sync precision | Wins Golden-Trailer-rubric blind comparison | DirectorAgent, MusicSupervisorAgent | EditorAgent (over-cut), ComposerAgent (mismatch) |
| 52 | **SportsAnalystAgent / TelestratorOp** | Tactical breakdowns + diagrams | MIT Sloan Sports Analytics papers; ESPN Stats & Info; Kirk Goldsberry analytics | Predicted-vs-actual play-call accuracy; on-screen clarity score | Beats ex-athlete commentator on tactical-prediction tasks | SMEAgent (sport), JournalistAgent | EditorAgent (missed-replay), MotionGraphicsAgent (chart clarity) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 73 | **PromptOptimizerAgent** | Auto-improves prompts via OPRO / APE / DSPy / Promptbreeder | OPRO (Yang 2023), APE (Zhou 2022), DSPy (Stanford), Promptbreeder (DeepMind) | Score uplift per iteration on held-out eval; iteration count to convergence | Beats Karen X. Cheng / Paul Trillo-style hand-tuned prompts on held-out briefs | PromptEngineerAgent, AIQAAgent | PromptEngineerAgent (sub-optimal seed) |
| 74 | **CostOptimizerAgent** | Routes between models / providers for $/quality | Provider pricing sheets; benchmark cost-quality frontiers; FrugalGPT patterns | $/successful-task; Pareto distance from cost-quality frontier | Lower $/quality than human CFO + producer routing decisions | RouterAgent, FinanceAgent | RouterAgent (over-spend), GeneratorAgent (re-roll burn) |
| 75 | **LatencyOptimizerAgent** | Parallelization, caching, speculative decoding, batch packing | vLLM, TensorRT-LLM, distillation literature; Anyscale/Ray patterns | p50/p95 latency; throughput per GPU-hour | Lower p95 than human-tuned pipeline at equal quality | OrchestratorAgent | OrchestratorAgent (serial bottleneck) |
| 76 | **RetentionOptimizerAgent** | Tunes hook, pacing, structure for AVD / hold-rate | YouTube Analytics public benchmarks; TikTok retention curves; AudienceSim outputs | Predicted retention curve vs actual; AVD lift over control | Beats senior YouTube editor on AVD lift in A/B | EditorAgent, AudienceSimAgent | EditorAgent (slow ope
…



### From `corpus/study/human_video_production_workflow.md` Copy: `sources/excerpts/human_video_production_workflow.md`.


| # | Sample Production | Typical Duration | Platform | Crew / Roles Required |
|---|-------------------|------------------|----------|----------------------|
| 1 | Short vertical videos (9:16) | 15–60s | TikTok, Reels, Shorts | Creator / On-camera talent, Phone Operator, Editor, Caption / Copywriter, Social Strategist |
| 2 | Trending sound / reaction videos | 7–30s | TikTok, Reels | On-camera Creator, Editor, Trend Researcher, Music Clearance Checker |
| 3 | Meme videos & funny skits | 5–30s | TikTok, Reels, Shorts | Writer / Comedian, Actor(s), Editor, Sound Designer, Meme Researcher |
| 4 | "Day in the life" style clips | 30–60s | TikTok, Reels | Creator / Vlogger, Camera Op (POV), Editor, Music Supervisor, Caption Writer |
| 5 | Aesthetic / vibe videos (lo-fi, cyberpunk, nature, retro) | 10–60s | Instagram, TikTok | Cinematographer or AI Generator Operator, Colorist, Music Curator, Editor |
| 6 | Hook videos (3-sec scroll-stoppers) | 3–15s | All short-form | Copywriter / Hook Writer, Director, Editor, Sound Designer, A/B Test Strategist |
| 7 | POV / first-person clips | 15–45s | TikTok, Reels | On-camera Creator, GoPro / Phone Operator, Editor, Sound Designer |
| 8 | Duet / stitch-ready reaction templates | 10–30s | TikTok | Creator, Writer, Editor, Trend Analyst |
| 9 | Challenge videos (dance, transformation) | 15–30s | TikTok, Reels | Talent / Dancer, Choreographer, Camera Op, Editor, Music Supervisor |
| 10 | Storytime narration overlays | 30–60s | TikTok, Reels | Storyteller / Narrator, Scriptwriter, Editor, B-roll Producer, Captioner |
| 11 | Green-screen explainer reactions | 15–45s | TikTok | Creator, Compositor / VFX, Editor, Researcher |
| 12 | Get-ready-with-me (GRWM) clips | 30–60s | TikTok, Reels | Creator, MUA / Stylist, Camera Op, Editor, Sponsored-Brand Coordinator |
| 13 | Quick-tip / life-hack videos | 10–30s | All short-form | Subject Expert, Scriptwriter, Demonstrator, Editor, Captioner |

| # | Sample Production | Typical Duration | Best Channel | Crew / Roles Required |
|---|-------------------|------------------|--------------|----------------------|
| 1 | Product showcase / demo videos | 15–60s | Social ads, e-comm | Director, DoP, Product Stylist, Editor, Motion GFX, Copywriter, Brand Manager |
| 2 | Brand story / explainer ads | 30–90s | YouTube, web | Creative Director, Scriptwriter, Director, DoP, Editor, Composer, VO Artist |
| 3 | UGC-style ads | 15–45s | TikTok, Meta ads | UGC Creator, Brief Writer, Editor, Performance-Ads Strategist, Legal Clearance |
| 4 | Before & After transformations | 10–30s | Reels, TikTok | Director, DoP, Talent, Editor, Colorist, Compliance Reviewer |
| 5 | AI-avatar testimonial videos | 30–60s | LinkedIn, landing pages | Scriptwriter, AI Avatar Designer, Voice Cloner / VO Artist, Lip-Sync Specialist, Editor |
| 6 | Carousel-to-video ads | 10–20s | Meta, LinkedIn | Designer, Motion Designer, Copywriter, Editor, Ad Strategist |
| 7 | E-commerce product videos | 10–30s | Shopify, Amazon | Product Photographer, Stylist, 3D Artist (turntable), Editor, Retoucher |
| 8 | Seasonal / holiday campaign spots | 15–60s | All paid social | Creative Director, Producer, Director, DoP, Art Dept, Editor, Composer, Media Buyer |
| 9 | Retargeting A/B ad variations | 6–15s | Meta, Google | Performance Marketer, Copywriter, Editor, Data Analyst |
| 10 | Influencer-style product unboxing | 30–60s | TikTok, Reels | Influencer, Brand Manager, Editor, Disclosure / Legal |
| 11 | Comparison / "vs competitor" videos | 30–60s | YouTube, web | Product Researcher, Scriptwriter, Presenter, Editor, Legal Reviewer |
| 12 | App-install promo videos | 15–30s | TikTok, Meta | UX Researcher, Scriptwriter, Motion Designer, Editor, ASO Specialist |
| 13 | Shoppable video ads | 15–30s | TikTok Shop, Reels | Director, Talent, Editor, E-comm Integrator, Product Tag Specialist |
| 14 | Pre-roll / mid-roll YouTube ads | 6–30s | YouTube | Creative Director, Scriptwriter, Director, Editor, Composer, Media Buyer |
| 15 | Founder-story authenticity videos | 60–120s | LinkedIn, web | Interviewer, DoP, Sound Recordist, Editor, Colorist, Brand Strategist |

| # | Sample Production | Typical Duration | Audience | Crew / Roles Required |
|---|-------------------|------------------|----------|----------------------|
| 1 | Animated explainers | 60–180s | General learners | Instructional Designer, Scriptwriter, Storyboard Artist, 2D Animator, VO Artist, Sound Designer, Editor |
| 2 | Whiteboard-style animations | 60–180s | B2B, training | Scriptwriter, Illustrator, Whiteboard Animator, VO Artist, Editor |
| 3 | Science / history simulation videos | 2–10 min | Students, edutainment | Subject-Matter Expert, Scriptwriter, 3D Artist, Simulation Engineer, VO Artist, Editor, Fact-Checker |
| 4 | Course intro & lesson summary videos | 30–90s | Online courses | Instructional Designer, Presenter, Editor, Motion GFX, LMS Specialist |
| 5 | Moving infographic videos | 30–60s | B2B, marketing | Data Analyst, Information Designer, Motion Designer, Copywriter, VO Artist |
| 6 | Step-by-step tutorial walkthroughs | 1–5 min | DIY, software | Subject Expert, Scriptwriter, Screen-Recordist, Editor, Captioner |
| 7 | Microlearning lessons | 30–60s | Corporate L&D | Instructional Designer, SME, Motion Designer, VO Artist, LMS Specialist |
| 8 | Quiz / flashcard videos | 15–60s | Students | Curriculum Designer, Motion Designer, VO Artist, Editor |
| 9 | Children's educational animations | 1–5 min | Kids 2–7 | Child-Ed Specialist, Scriptwriter, Character Designer, 2D Animator, VO Artist, Composer, Safety Reviewer |
| 10 | Language-learning vocabulary videos | 30–90s | Language learners | Linguist, Native Speaker VO, Illustrator, Motion Designer, Editor |
| 11 | Software / app tutorial screencasts | 1–5 min | SaaS users | Product Expert, Scriptwriter, Screen-Recordist, VO Artist, Editor |
| 12 | Data-visualization storytelling | 60–180s | Analysts, execs | Data Scientist, Information Designer, Motion Designer, VO Artist, Editor |
| 13 | Documentary-style "explained" videos | 5–15 min | YouTube | Researcher, Scriptwriter, Director, Editor, Narrator, Composer, Archive Producer, Fact-Checker |
| 14 | Myth-vs-fact debunking videos | 30–60s | Social | Researcher, Scriptwriter, Presenter, Editor, Fact-Checker |

| # | Niche | Sample Productions | Crew / Roles Required |
|---|-------|--------------------|----------------------|
| 1 | Gaming content | AI cutscenes, game trailers, NPC dialogue scenes, speedrun reels | Game Designer, Concept Artist, 3D Animator, VO Cast, Sound Designer, Composer, Trailer Editor |
| 2 | Fitness & wellness | Guided workouts, yoga flows, meditation visuals | Certified Trainer / Yoga Instructor, Scriptwriter, DoP, Editor, Composer, VO Artist |
| 3 | Food & recipe | Recipe walkthroughs, food cinemagraphs, restaurant promos | Chef / Food Stylist, Food Photographer, DoP, Editor, Recipe Writer, Colorist |
| 4 | Travel & tourism | Destination showcases, virtual travel diaries, hotel promos | Travel Producer, Drone Pilot, DoP, Editor, Colorist, Composer, Local Fixer |
| 5 | Fashion & beauty | Virtual try-on videos, lookbook reels, makeup tutorials | Fashion Stylist, MUA, Model, Photographer / DoP, Editor, Retoucher, AR / Try-On Engineer |
| 6 | News & journalism | AI news briefings, data-driven stories, explainer journalism | Journalist, Editor-in-Chief, Fact-Checker, Data Reporter, Motion Designer, VO / Anchor, Legal Reviewer |
| 7 | Religious / spiritual | Devotional videos, scripture animations, prayer clips | Theological Reviewer, Scriptwriter, Narrator, Animator, Composer, Editor |
| 8 | Sports | Highlight reels, play-breakdown animations, fantasy recaps | Sports Analyst, Editor, Motion GFX (telestrator), Color Commentator / VO, Statistician |
| 9 | Crypto / finance | Market recaps, token explainers, trading tutorials | Financial Analyst, Compliance Reviewer, Scriptwriter, Motion Designer, VO Artist, Legal Reviewer |
| 10 | Healthcare | Patient education, symptom explainers, procedure animations | Medical Doctor / SME, Medical Illustrator, Scriptwriter, 3D Animator, Compliance / HIPAA Reviewer, VO Artist |
| 11 | Legal | Plain-language law explainers, intake videos, compliance training | Attorney, Legal Writer, Compliance Officer, Motion Designer, VO Artist, Captioner |
| 12 | Nonprofit / advocacy | Fundraising stories, awareness clips, donor thank-yous | Story Producer, Director, DoP, Editor, Composer, Fundraising Strategist, Subject Consent Reviewer |
| 13 | Automotive | Car walk-arounds, dealership inventory, test-drive POVs | Automotive Photographer, Drone Pilot, Camera Op, Editor, Colorist, Copywriter |
| 14 | Pets & animals | Pet-care tutorials, breed spotlights, shelter adoption reels | Veterinarian / Animal Behaviorist, Animal Handler, Camera Op, Editor, Narrator |

| # | Role | Core Responsibility | Required Professional Quality | Typical Professional Experience | Related Production Types | Critics / Mentors (Real People & Methods) |
|---|------|---------------------|-------------------------------|---------------------------------|--------------------------|-------------------------------------------|
| 1 | **Director** | Owns creative vision; directs talent, camera, and pacing | Visual storytelling, leadership, decisiveness, taste | Film school + 5–15 yrs assisting / shorts / commercials before features | Films, music videos, ads, series, trailers | Martin Scorsese, Christopher Nolan, Greta Gerwig, Denis Villeneuve; methods: DGA peer screenings, Sundance Director's Lab, Cahiers du Cinéma reviews |
| 2 | **Producer / EP** | Budget, schedule, hiring, delivery | Project management, negotiation, financial literacy | PA → Line Producer → Producer (10+ yrs); MBA or PGA training common | All formats | Kathleen Kennedy, Kevin Feige, Jason Blum; methods: PGA Producers Mark review, studio greenlight committees |
| 3 | **Screenwriter / Scriptwriter** | Writes script, dialogue, structure | Story structure, dialogue, genre fluency, rewriting stamina | MFA or staffed writers' room 3–10 yrs; WGA membership | Films, ads, explainers, series, trailers | Aaron Sorkin, Charlie Kaufman, Phoebe Waller-Bridge; methods: Robert McKee's *Story* seminar, John Truby's *Anatomy of Story*, Black List script reviews |
| 4 | **Showrunner** | Creative + operational lead of a series | Writing + producing + people management | 10+ yrs in writers' rooms, prior staff writer / co-EP credits | Anthology series, episodic content | Vince Gilligan, Shonda Rhimes, Mike Schur; methods: WGA showrunner training, network notes process |
| 5 | **Cinematographer (DoP)** | Lighting, camera, lensing, look | Lighting science, camera tech, composition, color theory | Camera Assistant → Operator → DoP (8–15 yrs); ASC membership | Films, commercials, music videos, real estate, fashion | Roger Deakins, Emmanuel Lubezki, Rachel Morrison; methods: ASC Magazine reviews, ASC Master Class critiques |
| 6 | **Camera Operator** | Operates camera per DoP direction | Steady framing, focus, follow-action | 2nd AC → 1st AC → Operator (5–10 yrs); SOC membership | All live-action formats | Society of Camera Operators (SOC) peers, Steadicam Workshop instructors (Garrett Brown lineage) |
| 7 | **Drone Pilot** | Aerial cinematography | FAA Part 107 (or local equiv.), flight precision, spatial awareness | 100+ flight hours, commercial license, insurance | Real estate, travel, automotive, music videos | Philip Bloom, Dirk Dallas (@fromwhereidrone); methods: SkyPixel competition jury, FAA safety audits |
| 8 | **Editor** | Assembles footage, controls pacing and rhythm | Rhythm, story sense, software mastery (Avid/Premiere/Resolve) | Assistant Editor 3–7 yrs; ACE membership for top tier | All formats | Walter Murch (*In the Blink of an Eye*), Thelma Schoonmaker, Joe Walker; methods: ACE Eddie Awards peer review, Murch's "Rule of Six" |
| 9 | **Colorist** | Final color grade, look consistency | Color theory, DaVinci Resolve / Base
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

| Domain | Source | Key Finding (paraphrased) | Implication for This Workflow |
|---|---|---|---|
| YouTube growth | [Colin & Samir — New Rules of YouTube w/ Paddy Galloway](https://www.colinandsamir.com/resources/the-new-rules-of-youtube-from-paddy-galloway) | The highest leverage is *packaging* (title + thumbnail), not production; one creator jumped from ~2–3K to 1M+ views by shifting effort there | Add a **package-first gate** before generation; title+thumbnail decided in Phase 1, not after |
| YouTube growth | [Paddy Galloway strategy summary](https://outlierkit.com/resources/youtube-scriptwriting-methods-compared/) · [Accelerator](https://www.paddygalloway.com/accelerator) | Success rests on idea → title → retention → packaging, using a channel's own data; model "outlier" videos already over-performing in the niche | Add **OutlierModeling** step (TrendIntel + Analyst) feeding idea selection |
| Retention | [MrBeast leaked-doc breakdowns](https://sherwood.news/culture/mrbeast-youtube-leaked-internal-success-document/) · [koi.app](https://www.koi.app/posts/mrbeast-s-blueprint-for-youtube-domination-key-insights-from-the-leaked-employee-guide) | Three core metrics: CTR, average view duration, average view %; structure as hook (min 0–1) → 1–3 → 3–6 → back half; retention won/lost in first ~60s, so front-load energy | Re-shape the 60s film with an **engineered opener** and per-segment retention targets |
| Retention | [complexminds](https://complexminds.substack.com/p/the-mr-beast-retention-formula-that) · [paulcopy](https://paulcopy.substack.com/p/the-strategy-behind-mr-beasts-70) | MrBeast sustains ~70% avg retention vs ~30% typical | Set retention target bands per segment as explicit gate thresholds |
| Shorts | [opus.pro](https://www.opus.pro/blog/youtube-shorts-hook-formulas) · [rendercut](https://rendercut.io/why-viewers-scroll-away-first-3-seconds/) · [vexub](https://vexub.com/blog/viral-short-form-video-hooks) | The 3-second hold is the distribution threshold; ~2/3 swipe within 3s; spoken hooks ~10–14 words; visual hook must hit on the first frame; 60%+ past-3s retention earns more reach | Cut a **3s-hook vertical** with first-frame visual + ≤14-word VO line |
| Shorts views | [findmecreators](https://www.findmecreators.com/blog/youtube-shorts-retention-rate) | Since 31 Mar 2025 a Shorts "view" counts on play/replay with no minimum watch time | Optimize for hold + replay loop, not just impressions |
| xAI engine | [x.ai — Grok Imagine 1.5 Preview](https://x.ai/news/grok-imagine-1-5) | Image-to-video that animates a still while staying faithful to the source frame (camera moves, atmosphere, physics) up to 720p; shots can be chained for a consistent look across a project | Use Grok I2V as the **keyframe-faithful animator** to protect identity/lighting |
| xAI engine | [x.ai — Video 1.5 Fast](https://x.ai/news/grok-imagine-video-1-5) · [imagine.art](https://www.imagine.art/blogs/xai-grok-imagine-video-1-5-guide) | 1.5 Fast makes 6s 720p in ~25s; 1.5 topped the Image-to-Video Arena (+52 Elo) over Seedance 2.0 and Veo | Use Grok for **fast divergent iteration / variant browsing**; promote winners to premium engines |
| xAI engine | [codersera — Agent Mode](https://codersera.com/blog/grok-imagine-agent-mode-launch-2026/) · [aimlapi](https://aimlapi.com/blog/grok-imagine-video-vs-grok-imagine-video-1-5-preview) | Agent Mode (1 May 2026) is an infinite-canvas agent that plans, generates, edits and stitches 6s clips into longer films; one API covers gen, edit, I2V, reference-video, extension, editing | Mirror our DAG inside Grok Agent Mode for the **fast-draft pass**; native audio + in-quotes dialogue lip-sync |
| Consistency | [arXiv 2512.16954 — Character-Stable Pipeline](https://arxiv.org/html/2512.16954) | Removing the *visual anchoring* mechanism collapsed character consistency (7.99→0.55); visual priors are essential for identity | Make **visual-anchor keyframes mandatory** before any I2V; never pure text-to-video for characters |
| Consistency | [arXiv 2510.10135 — CharCom](https://arxiv.org/html/2510.10135v1) | Composable per-character LoRA adapters on a frozen backbone, applied at inference via prompt-aware control, raise fidelity without retraining | StyleTransferAgent builds **one LoRA per character age** (A-young, E-adult, …) |
| Consistency | [arXiv 2510.14256 — Identity-GRPO](https://arxiv.org/html/2510.14256v1) | RL fine-tuning improved multi-human identity consistency by up to ~18.9% | Use for the multi-character **family-dinner (Scene 10)** shot where drift is worst |
| Consistency | [arXiv 2512.19539 — StoryMem](https://arxiv.org/html/2512.19539) | Memory-conditioned single-shot diffusion generates coherent minute-long multi-shot stories | Pair with our MemoryAgent (#58) for **cross-scene character memory** |
| Consistency | [arXiv 2510.21696 — BachVid](https://arxiv.org/html/2510.21696v1) | Training-free consistency for background + character without reference image
…



### From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


**Build:**
- **Agent Factory** (`packages/agent-factory`): `AgentConfig (YAML) → runnable BaseAgent`. Validates prompt/rubric/tools/QC refs; registers into `agents/_registry.yaml`; generates the per-agent test skeleton. This is the engine for M7–M9.
- **Workflow A craft agents** (subset, via factory): TrendIntelligenceAgent, CopywriterAgent, SocialMediaStrategistAgent, PromptEngineerAgent/GeneratorOperator, AIQAConsistencyAgent, EditorAgent, AccessibilityOptimizerAgent, AudienceSimAgent, AnalystAgent — exactly the crew in [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §3.1.
- **Workflow A DAG** (`workflows/A_viral_hook.py`): Concept → Production → Post → Review → Distribution → Post-launch, with the spec'd critic gates.
- End-to-end run: brief → DIA → Planner builds the A-DAG → agents execute (mock gen) → artifacts flow with handoff contract → critique bus active → QC mesh gates → C2PA-signed deliverable → events on the bus.



### From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 28 | **SocialMediaStrategistAgent** | Platform-native distribution, timing, trends | TikTok Creator Portal; Meta Marketing Science; Tubular/Sensor Tower | Predicted-vs-actual reach error; trend-timing latency <2h | Beats agency social leads on 30-day reach lift | AnalystAgent, BrandAgent | CopywriterAgent (off-platform tone), EditorAgent (wrong aspect) | Meta Graph API; TikTok Content Posting API; Buffer/Hootsuite API; Sensor Tower data | ReAct (trend search → schedule → post) |
| 29 | **CopywriterAgent** | Scripts, captions, hooks, headlines | D&AD/One Show; *Ogilvy on Advertising*; Wiebe Copyhackers | Reading grade; hook-curiosity score; brand-voice cosine ≥0.85 | Wins D&AD-style blind preference on ad briefs | BrandAgent, PerformanceMarketerAgent | ScriptwriterAgent (verbosity), VOArtist (unspeakable) | Brand-voice embedding model; Hemingway readability API; A/B headline tools | Self-Refine (rubric: brand-voice similarity scorer) |
| 30 | **CreativeDirectorAgent** | Campaign concept; cross-discipline taste | Cannes Lions Grand Prix; D&AD Pencils; agency case studies | Concept distinctiveness (embedding novelty); award-rubric predicted score | Wins Cannes-jury-emulator gold vs human shortlists | ClientAgent, BrandAgent | CopywriterAgent, ArtDirectorAgent | Campaign-archive search (Cannes Lions API); Midjourney for concept viz; Figma API | Multi-agent debate (panel of IdeationAgent + NoveltyAgent) |
| 31 | **PerformanceMarketerAgent** | Optimize ads for ROAS | Meta Blueprint; TikTok Ads Academy; MMM literature | ROAS uplift vs control; significance ≥95% | Beats senior media buyer on 30-day ROAS | AnalystAgent, FinanceAgent | UGCAgent (low hook), CopywriterAgent (weak CTA) | Meta Ads API; TikTok Ads API; Google Ads API; Bayesian AB testing libs | RLAIF (reward = ROAS uplift signal from ad platform) |

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
| 46 | **PromptEngineerAgent / GeneratorOperator** | Crafts prompts; steers Sora/Veo/Runway/Kling | Karen X. Cheng/Trillo public sets; r/aivideo; Runway AIFF jury notes | Prompt→output CLIP-T; iteration count to acceptance; seed reproducibility | Target shot in ≤3 iterations vs human avg 10 | DirectorAgent, AIQAAgent | AIQAAgent (re-roll budget), ConsistencyAgent | Sora 2 API, Veo 3.1, Runway Gen-4/Aleph, Kling 3.0; seed/parameter registries | DSPy / OPRO prompt optimization (Yang 2023) |
| 47 | **AvatarDesignAgent** | Synthetic-presenter identity | Synthesia/HeyGen design docs; Hany Farid deepfake-detection; C2PA spec | Identity-hash consistency across shots; consent chain; C2PA signed | C2PA-verifiable + Partnership-on-AI full-pass at scale | ComplianceAgent (consent), DeepfakeDetectionAgent | VoiceCloneAgent (off-likeness), LipSyncAgent | HeyGen Avatar IV API; Synthesia API; C2PA signing library (c2patool); face-embedding models | Constitutional AI (consent + identity constitution) |
| 48 | **VoiceCloneAgent / LipSyncSpecialist** | Voice cloning + lip-sync | ElevenLabs safety docs; Wav2Lip/Sync.so; Baxter lip-sync refs | Voice MOS ≥4.2; phoneme-viseme error <40ms; consent verified | Wins blind MOS vs professional ADR | ComplianceAgent (consent), AnimatorAgent (lip-sync gold) | AvatarDesignAgent (face flicker), DubbingAgent | ElevenLabs v3 cloning API; Sync.so lip-sync; Wav2Lip; consent-doc verification | Self-Refine + MOS scoring model as judge |
| 49 | **AIQAConsistencyAgent** | Catches frame drift, hand/face artifacts, identity breaks | VBench; EvalCrafter; FVD literature; MPC/Weta QC checklists; deepfake models | Per-frame artifact score; identity-hash drift; hand/finger pass | Catches >95% of senior QC catches + 30% missed | DirectorAgent, VFXSupAgent | GeneratorAgent (re-roll), CompositorAgent | VBench evaluation suite; hand-detector models; face-ID embedding (ArcFace); frame-diff tools | Tool-use / ReAct (run detectors → flag → report) |
| 50 | **PersonalizationEngineerAgent** | Variable templates (name/face/voice swap) | Idomoo case studies; DMA campaigns; MarTech lit | Render-success ≥99.5%; spot-check pass; privacy-audit pass | Higher share-rate than top human-templated campaigns | ComplianceAgent (GDPR/CCPA), AnalystAgent | TemplateDesignerAgent (fragility) | Idomoo/Pirsonal APIs; HeyGen personalization; GDPR consent-management platform | ReAct (assemble template → render → validate → deliver) |
| 51 | **TrailerEditorAgent** | Hook-driven trailer cuts | Golden Trailer Awards; Woollen/AV Squad reels; trailer-music libs | Hook-rate at 3s; rising-action curve; music-sync precision | Wins Golden-Trailer-rubric blind comparison | DirectorAgent, MusicSupervisorAgent | EditorAgent (over-cut), ComposerAgent (mismatch) | DaVinci Resolve (MCP); trailer-music APIs (Musicbed/Artlist); retention-curve predictor | Self-Refine (retention-curve model as feedback) |
| 52 | **SportsAnalystAgent / TelestratorOp** | Tactical breakdowns + diagrams | MIT Sloan papers; ESPN Stats & Info; Goldsberry analytics | Play-call accuracy; on-screen clarity score | Beats ex-athlete on tactical-prediction | SMEAgent (sport),
…



### From `corpus/study/ui/ui_design.md` Copy: `sources/excerpts/ui_design.md`.


| # | Surface | Composition Diagram Operation(s) | Primary Agent(s) Served |
|---|---------|----------------------------------|------------------------|
| S1 | Brief Wizard | `[Brief]` entry point | User → PlannerAgent |
| S2 | Template Selector | Workflow type selection (A–J) | PlannerAgent |
| S3 | DAG Canvas | Full `PlannerAgent → OrchestratorAgent → RouterAgent → Craft Agents` flow | OrchestratorAgent, RouterAgent |
| S4 | Agent Node Card | Individual agent status within DAG | Any of 114 agents |
| S5 | Gate Approval Dialog | `GateKeeperAgent` phase transitions | GateKeeperAgent, JudgeAgent |
| S6 | Critique Feed | `CritiqueMessages` bus | All agents (bi-directional) |
| S7 | Memory Panel | `MemoryAgent` retrieval/store | MemoryAgent |
| S8 | Agent Inspector | Agent drill-down (tools, metrics, I/O) | Any agent |
| S9 | Artifact Gallery | Outputs from all craft agents | 52 craft agents (§1–§8) |
| S10 | Artifact Viewer | Preview + compare + provenance | All producing agents |
| S11 | Timeline View | Schedule/phase visualization | ProducerAgent, OrchestratorAgent |
| S12 | Budget Tracker | Cost monitoring | ProducerAgent, CostOptimizerAgent |
| S13 | Router Config | Model/agent routing rules | RouterAgent, CostOptimizerAgent |
| S14 | Prompt Lab | Prompt editing + optimization | PromptEngineerAgent, PromptOptimizerAgent |
| S15 | Quality Dashboard | VBench/EvalCrafter/CLIP-T scores | AIQAConsistencyAgent, EvalHarnessAgent |
| S16 | Delivery Packager | Channel-specific export | DistributorAgent, SoundMixerAgent, ColoristAgent |
| S17 | Analytics Panel | Post-release performance | AnalystAgent, RetentionOptimizerAgent |
| S18 | Compliance Checker | Legal/consent/C2PA status | ComplianceAgent, TrustSafetyAgent |
| S19 | Creative Meta Panel | Ideation/Narrative/Style/Mood/Novelty/Emotion | Creative meta-agents (§9.2) |
| S20 | Research Panel | Web/Archive/Trend/Competitor/Citation | Research meta-agents (§9.3) |
| S21 | Optimization Panel | Prompt/Cost/Latency/Retention/ROAS/A11y | Optimization meta-agents (§9.4) |
| S22 | Notification Center | Escalations, approvals, alerts | ProducerAgent, all gate agents |
| S23 | Team / Permissions | Human-in-the-loop configuration | Admin |
| S24 | Series Bible Editor | Long-running episodic memory | ShowrunnerAgent, WorldBuildingAgent |

Step 1: ARRIVE AT DASHBOARD
   │
   ├── Option A: Click template card (A–J) → Brief Studio (pre-filled)
   ├── Option B: Click "+ New Production" → Brief Studio (blank)
   └── Option C: Type in global search → AI suggests template
   │
   ▼
Step 2: BRIEF STUDIO
   │
   ├── 2a. Select/confirm template (activates workflow-specific agent set)
   ├── 2b. Fill brief details (title, vision, genre, duration, aspect, tone)
   ├── 2c. Upload references (scripts, mood boards, audio refs, brand assets)
   ├── 2d. Set constraints (compliance, platforms, accessibility, budget, deadline)
   └── 2e. Review plan preview (PlannerAgent pre-decomposition estimate)
   │
   ▼
Step 3: LAUNCH
   │
   ├── Brief → PlannerAgent (decomposes into phased DAG)
   ├── PlannerAgent → OrchestratorAgent (initializes execution)
   ├── OrchestratorAgent → RouterAgent (assigns models + agents)
   ├── MemoryAgent initialized with brief + references
   └── UI transitions to Production Console (DAG Canvas view)
   │
   ▼
Step 4: PRE-PRODUCTION PHASE (automated)
   │
   ├── ScreenwriterAgent → script
   ├── StoryboardAgent → panels
   ├── ConceptArtistAgent → look dev
   ├── CastingAgent → voice/talent selection
   ├── ComposerAgent → initial themes
   ├── Creative Meta-agents assist (Ideation, NarrativeArc, Mood, Style)
   ├── Research Meta-agents feed context (Web, Archive, Trend)
   │
   ├── GateKeeperAgent checks L1 criteria
   └── Gate Approval Dialog appears → USER APPROVES → next phase
   │
   ▼
Step 5: PRODUCTION PHASE (automated with optional HiTL)
   │
   ├── DirectorAgent issues shot intents
   ├── PromptEngineerAgent crafts generation prompts
   ├── RouterAgent routes to Veo/Sora/Runway/Kling
   ├── CinematographerAgent validates composition
   ├── AIQAConsistencyAgent runs per-frame QC
   ├── Optimization agents tune (Prompt, Cost, Latency)
   │
   ├── Critique messages flow (viewable in Critique Feed)
   ├── Artifacts appear in Gallery as generated
   ├── User can intervene via Critique Feed human slot
   │
   ├── GateKeeperAgent checks L2 criteria
   └── Gate Approval Dialog → USER APPROVES → next phase
   │
   ▼
Step 6: POST-PRODUCTION PHASE (automated with optional HiTL)
   │
   ├── EditorAgent assembles cut
   ├── ColoristAgent applies grade
   ├── SoundDesignAgent + ComposerAgent lay audio
   ├── SoundMixerAgent final mix
   ├── VFXSupervisorAgent composites
   ├── AccessibilityOptimizerAgent adds captions/AD
   │
   ├── JudgeAgent scores via rubric
   ├── GateKeeperAgent checks L3 criteria
   └── Gate Approval Dialog → USER APPROVES → delivery
   │
   ▼
Step 7: DELIVERY PHASE
   │
   ├── Delivery Hub shows channel matrix
   ├── DistributorAgent packages per-outlet specs
   ├── ComplianceAgent final legal sign-off
   ├── C2PA provenance signed across all outputs
   ├── User reviews final QC, approves distribution
   └── Assets published to target channels
   │
   ▼
Step 8: POST-RELEASE (optional)
   │
   ├── AnalystAgent collects performance data
   ├── RetentionOptimizerAgent / ROASOptimizerAgent analyze
   ├── Analytics Panel shows results
   └── Learnings feed back into MemoryAgent for future productions
```



## Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


## Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


## Provenance

- Master roster row va_id=81 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `C:\Project\va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.analyst · va_id=81 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **AnalystAgent** (`video.analyst`, va_id=81, category `10-Sup`).

### Responsibility focus
Aggregates business, creative, and technical performance telemetry into decision-ready reports

### Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: agentic RAG, web research agents, citation-grounded LLMs, competitive intelligence agents, archive retrieval
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI research agents, agentic RAG, citation tools
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: building research agents, RAG for production research, AI OSINT light workflows

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

<!-- migration_capability_research · video.analyst · v1 · 2026-07-13 -->

### `sources/generic/video.audiencesim.SPEC.md`

Omitted here; same document as `SPEC.md` above.

### `sources/MAPPING.md`

# Mapping — `video.audiencesim`

- VA/generic pack ID: `video.audiencesim`
- Previous common ID: `video.audience_researcher`
- SPEC depth: full generic SPEC body + host runtime binding

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
      "title": "This is Marketing",
      "author": "Seth Godin",
      "isbn13": "9780525541073",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: This is Marketing (Seth Godin), ISBN-13 9780525541073"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Contagious",
      "author": "Jonah Berger",
      "isbn13": "9781451686586",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Contagious (Jonah Berger), ISBN-13 9781451686586"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Made to Stick",
      "author": "Chip & Dan Heath",
      "isbn13": "9781400064281",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Made to Stick (Chip & Dan Heath), ISBN-13 9781400064281"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Crossing the Chasm, 3rd ed.",
      "author": "Geoffrey Moore",
      "isbn13": "9780062292988",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Crossing the Chasm, 3rd ed. (Geoffrey Moore), ISBN-13 9780062292988"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Lean Startup",
      "author": "Eric Ries",
      "isbn13": "9780307887894",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Lean Startup (Eric Ries), ISBN-13 9780307887894"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Ogilvy on Advertising",
      "author": "David Ogilvy",
      "isbn13": "9780394729039",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Ogilvy on Advertising (David Ogilvy), ISBN-13 9780394729039"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Copywriter's Handbook, 4th ed.",
      "author": "Robert W. Bly",
      "isbn13": "9781250238092",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Copywriter's Handbook, 4th ed. (Robert W. Bly), ISBN-13 9781250238092"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Hey, Whipple, Squeeze This, 5th ed.",
      "author": "Luke Sullivan",
      "isbn13": "9781119164005",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Hey, Whipple, Squeeze This, 5th ed. (Luke Sullivan), ISBN-13 9781119164005"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Scientific Advertising",
      "author": "Claude Hopkins",
      "isbn13": "9781607962335",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Scientific Advertising (Claude Hopkins), ISBN-13 9781607962335"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Jab, Jab, Jab, Right Hook",
      "author": "Gary Vaynerchuk",
      "isbn13": "9780062273062",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Jab, Jab, Jab, Right Hook (Gary Vaynerchuk), ISBN-13 9780062273062"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Hooked",
      "author": "Nir Eyal",
      "isbn13": "9781591847786",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Hooked (Nir Eyal), ISBN-13 9781591847786"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Traction",
      "author": "Weinberg & Mares",
      "isbn13": "9781591848363",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Traction (Weinberg & Mares), ISBN-13 9781591848363"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Hacking Growth",
      "author": "Ellis & Brown",
      "isbn13": "9780451497215",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Hacking Growth (Ellis & Brown), ISBN-13 9780451497215"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "这就是营销",
      "isbn13": "9787521702330",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 这就是营销，ISBN-13 9787521702330"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "让创意更有黏性",
      "isbn13": "9787508641245",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 让创意更有黏性，ISBN-13 9787508641245"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "跨越鸿沟",
      "isbn13": "9787111456780",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 跨越鸿沟，ISBN-13 9787111456780"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "精益创业",
      "isbn13": "9787115293701",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 精益创业，ISBN-13 9787115293701"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "一个广告人的自白",
      "isbn13": "9787111496182",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 一个广告人的自白，ISBN-13 9787111496182"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "文案训练手册",
      "isbn13": "9787115351555",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 文案训练手册，ISBN-13 9787115351555"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "上瘾",
      "isbn13": "9787508648017",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 上瘾，ISBN-13 9787508648017"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "增长黑客",
      "isbn13": "9787213066948",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 增长黑客，ISBN-13 9787213066948"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "参与感",
      "isbn13": "9787213055375",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 参与感，ISBN-13 9787213055375"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Trustworthy Online Controlled Experiments",
      "author": "Kohavi, Tang, Xu",
      "isbn13": "9781108724265",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Trustworthy Online Controlled Experiments (Kohavi, Tang, Xu), ISBN-13 9781108724265"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Storytelling with Data",
      "author": "Cole Nussbaumer Knaflic",
      "isbn13": "9781119002253",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Storytelling with Data (Cole Nussbaumer Knaflic), ISBN-13 9781119002253"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Lean Analytics",
      "author": "Croll & Yoskovitz",
      "isbn13": "9781449335670",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Lean Analytics (Croll & Yoskovitz), ISBN-13 9781449335670"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Visual Display of Quantitative Information, 2nd ed.",
      "author": "Edward Tufte",
      "isbn13": "9780961392147",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Visual Display of Quantitative Information, 2nd ed. (Edward Tufte), ISBN-13 9780961392147"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Naked Statistics",
      "author": "Charles Wheelan",
      "isbn13": "9780393347777",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Naked Statistics (Charles Wheelan), ISBN-13 9780393347777"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Signal and the Noise",
      "author": "Nate Silver",
      "isbn13": "9780143125082",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Signal and the Noise (Nate Silver), ISBN-13 9780143125082"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "精益数据分析",
      "isbn13": "9787115384515",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 精益数据分析，ISBN-13 9787115384515"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "用数据讲故事",
      "isbn13": "9787111575558",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 用数据讲故事，ISBN-13 9787111575558"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "赤裸裸的统计学",
      "isbn13": "9787508643427",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 赤裸裸的统计学，ISBN-13 9787508643427"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Understanding Media",
      "author": "Marshall McLuhan",
      "isbn13": "9780262631594",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Understanding Media (Marshall McLuhan), ISBN-13 9780262631594"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Amusing Ourselves to Death",
      "author": "Neil Postman",
      "isbn13": "9780143036531",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Amusing Ourselves to Death (Neil Postman), ISBN-13 9780143036531"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Convergence Culture",
      "author": "Henry Jenkins",
      "isbn13": "9780814742952",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Convergence Culture (Henry Jenkins), ISBN-13 9780814742952"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Spreadable Media",
      "author": "Jenkins, Ford, Green",
      "isbn13": "9780814743508",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Spreadable Media (Jenkins, Ford, Green), ISBN-13 9780814743508"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Attention Merchants",
      "author": "Tim Wu",
      "isbn13": "9780385352017",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Attention Merchants (Tim Wu), ISBN-13 9780385352017"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Here Comes Everybody",
      "author": "Clay Shirky",
      "isbn13": "9780143114949",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Here Comes Everybody (Clay Shirky), ISBN-13 9780143114949"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "理解媒介",
      "isbn13": "9787508040318",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 理解媒介，ISBN-13 9787508040318"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "娱乐至死",
      "isbn13": "9787563397648",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 娱乐至死，ISBN-13 9787563397648"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "融合文化",
      "isbn13": "9787301162262",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 融合文化，ISBN-13 9787301162262"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "认知盈余",
      "isbn13": "9787213044661",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 认知盈余，ISBN-13 9787213044661"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Audience-ology How Moviegoers Shape the Films We Love",
      "author": "Kevin Goetz",
      "isbn13": "9781982186678",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Audience-ology How Moviegoers Shape the Films We Love (Kevin Goetz), ISBN-13 9781982186678"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Film Marketing",
      "author": "Finola Kerrigan",
      "isbn13": "9781138013360",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Film Marketing (Finola Kerrigan), ISBN-13 9781138013360"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Global Film Market Transformation in the Post-Pandemic Era Production, Distribution…",
      "author": "Qiao Li, David Wilson, Yanqiu Guan",
      "isbn13": "9781003345251",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Global Film Market Transformation in the Post-Pandemic Era Production, Distribution… (Qiao Li, David Wilson, Yanqiu Guan), ISBN-13 9781003345251"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Blockbusters Hit-Making, Risk-Taking, and the Big Business of Entertainment",
      "author": "Elberse, Anita",
      "isbn13": "9781491518649",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Blockbusters Hit-Making, Risk-Taking, and the Big Business of Entertainment (Elberse, Anita), ISBN-13 9781491518649"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "电影市场营销（第2版）",
      "author": "于丽",
      "isbn13": "9787106053994",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影市场营销（第2版）（于丽），ISBN-13 9787106053994"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "电影发行与市场营销",
      "author": "刘嘉等",
      "isbn13": "9787010167718",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影发行与市场营销（刘嘉等），ISBN-13 9787010167718"
    }
  ],
  "agent_id": "video.audiencesim",
  "previous_common_agent_id": "video.audience_researcher",
  "va_taxonomy_aligned": true,
  "generic_source": "generic-swarm-ops/business/video/agents/video.audiencesim",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "aligned_at": "2026-07-27T00:48:10.464308Z",
  "generic_source_depth": {
    "excerpts": true,
    "study": true,
    "adopted_at": "2026-07-27T01:30:27.672219+00:00",
    "upstream": "generic-swarm-ops/business/video/agents"
  },
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\video\\agents\\video.audiencesim",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```

### `sources/RETHINK_100_APPLIED.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.audiencesim",
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
    50,
    59,
    63,
    87,
    88,
    92,
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
    "50": "Retention prediction pre-delivery",
    "59": "Agent reasoning in plain English",
    "63": "Comparison with human baseline",
    "87": "Human preference learning (accepts/rejects)",
    "88": "Automated regression on config change",
    "92": "Audience segment simulation",
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
    "When metrics exist, surface retention/ROAS hypotheses with confidence — never fabricate live analytics.",
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
  "agent_id": "video.audiencesim",
  "sources": [
    {
      "id": "src_1",
      "title": "Pairwise preference datasets",
      "description": "Pairwise preference datasets",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.audiencesim",
      "status": "planned_or_partial"
    },
    {
      "id": "src_2",
      "title": "retention studies",
      "description": "retention studies",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.audiencesim",
      "status": "planned_or_partial"
    },
    {
      "id": "src_3",
      "title": "audience segmentation models",
      "description": "audience segmentation models",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.audiencesim",
      "status": "planned_or_partial"
    }
  ],
  "note": "Legal review required before treating external corpora as production grounding."
}
```

### `sources/study/psychological_profile_agent_functional_specifications.md`

# 100 Creator Psychological Profile Library

## 100 Writer Profiles for Screenwriting Framework

**Purpose:** Provide personalized parameter configurations for the framework in this chapter and Appendix A workflow

**File Structure:**
- Basic information (code, age, professional background)
- Psychological traits (MBTI tendencies, motivation types, fear patterns)
- Creation parameters (best tools, time allocation, support needs)
- Framework adaptation (key focuses for each stage, predicted obstacles, success strategies)

## 📊 Complete File Overview Table



### Profiles 1-25: Introverted Creative Type

| Code | Age | Professional Background | MBTI Tendency | Core Motivation | Primary Fear | Creative Style | Best Time Slot | Energy Pattern | Social Needs | Perfectionism | Procrastination Tendency | Self-Doubt | External Motivation Needs | Best Tool Combo | Pomodoro Setting | Weekly Page Goal | Accountability Method | Predicted Main Obstacles | Suggested Strategies |
|------|------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|--------------|--------------|------------|--------------|----------|--------------|----------|
| QINTV | 23 | College Student/Literature Major | INFP | Self-healing | Criticism | Poetic and lyrical | Late night | Low frequency, high intensity | Extremely low | High | High | Extremely high | Low | Obsidian+Fountain | 20/10 | 5 | Anonymous journal | Perfectionism paralysis | Garbage draft method |
| DRMWV | 27 | Barista/Amateur Writer | INFJ | Change the world | Meaninglessness | Symbolic metaphor | Early morning | Medium frequency, medium intensity | Low | Medium-high | Medium | High | Medium-low | Logseq+Manuskript | 25/5 | 8 | Writing partner | Over-planning | Time boxing |
| SHDWK | 31 | IT Engineer | INTP | Intellectual exploration | Mediocrity | Structurally complex | Midnight | Low frequency, extreme intensity | Extremely low | Extremely high | Medium-high | Medium | Extremely low | VS Code+Git | 45/15 | 10 | Self-tracking | Over-complication | MVP mindset |
| MSTFL | 24 | Illustrator | ISFP | Aesthetic expression | Conflict | Visually oriented | Afternoon | High frequency, low intensity | Low | Medium | Medium | Medium-high | Medium | Excalidraw+Fountain | 15/5 | 6 | Visual progress board | Avoiding conflict scenes | Emotional rehearsal |
| ECHOV | 29 | Psychologist | INFJ | Heal others | Harm others | Psychological depth | Evening | Medium frequency, medium intensity | Medium-low | Medium | Low | Medium | Medium | Obsidian+LanguageTool | 25/5 | 12 | Supervisor feedback | Over-analyzing characters | Action first |
| NVLST | 35 | Novelist in transition | INTJ | Challenge self | Failure | Literary adaptation | Early morning | Medium frequency, high intensity | Low | High | Low | Medium-low | Low | Trelby+Afterwriting | 30/5 | 15 | Editor feedback | Novel thinking interference | Format training |
| GHTWR | 22 | Horror novel enthusiast | ISTP | Thrilling experience | Boredom | Suspense thriller | Late night | Low frequency, extreme intensity | Extremely low | Low | Medium | Low | Low | Fountain+Timeline | 40/10 | 8 | None needed | Loose structure | Beat sheet enforcement |
| PHLSF | 33 | Philosophy graduate student | INTP | Idea dissemination | Superficiality | Dialogue-heavy | Any time | Irregular | Low | Extremely high | High | Medium | Extremely low | Logseq+Freeplane | 50/10 | 6 | Academic peers | Preachy tendency | Show, don't tell |
| POETX | 26 | Poet | INFP | Emotional sublimation | Commercialization | Imagery-rich | Dusk | High frequency, low intensity | Low | Medium-high | High | Extremely high | Low | Obsidian plain text | 15/10 | 4 | Poetry society sharing | Overly poetic dialogue | Colloquial practice |
| HERMX | 40 | Retired Teacher | ISTJ | Pass on experience | Being forgotten | Traditional narrative | Early morning | High frequency, medium intensity | Low | Medium | Low | Low | Medium | Word+handwritten | 25/5 | 10 | Family support | Tech barriers | Simplified tools |
| ANXWR | 28 | Anxiety recovery | ISFJ | Share experiences | Relapse | Inner monologue | Morning | Medium frequency, low intensity | Medium-low | Medium | Medium-high | High | High | Simple tools+timer | 15/10 | 5 | Therapist | Emotional triggers | Safe word setting |
| DRKPT | 25 | Goth culture enthusiast | INFP | Explore darkness | Misunderstanding | Dark aesthetics | Midnight | Low frequency, high intensity | Low | Medium | Medium | Medium-high | Low | Dark theme editor | 30/5 | 7 | Subculture community | Too niche | Universal emotional connection |
| SILNT | 32 | Deaf Artist | ISFP | Visual storytelling | Being overlooked | No dialogue/minimalist | Afternoon | Medium frequency, medium intensity | Low | Medium | Low | Medium | Medium | Visual storyboard tools | 25/5 | 8 | Deaf community | Dialogue dependency | Visual priority |
| MNKWR | 38 | Former Monk | INFJ | Spiritual inspiration | Secularization | Meditative rhythm | Early morning | Low frequency, medium intensity | Extremely low | Low | Low | Low | Extremely low | Minimalist tools | 45/15 | 6 | Spiritual mentor | Too abstract | Concretization practice |
| CODEQ | 30 | Programmer | INTJ | System optimization | Chaos | Logically rigorous | Late night | Low frequency, extreme intensity | Low | Extremely high | Medium | Low | Low | Git+automation scripts | 45/10 | 12 | Code review style | Emotional deficiency | Emotional injection practice |
| WIDWX | 45 | Widower | ISFJ | Memorialize the deceased | Forgetting | Memory narrative | Early morning | Medium frequency, low intensity | Medium-low | Low | Medium | Medium | High | Simple+photo integration | 20/10 | 4 | Grief support group | Emotional overwhelm | Emotional boundaries |
| ASPER | 27 | Asperger's | INTP | Unique perspective | Social scenes | Detail-oriented | Fixed time slots | Regular, medium intensity | Extremely low | Extremely high | Low | Medium | Low | Structured templates | 30/5 fixed | 8 | Structured feedback | Social dialogue | Dialogue formulas |
| RECLV | 50 | Reclusive Writer | INTJ | Literary legacy | Exposure | Classic style | Early morning | Medium frequency, high intensity | Extremely low | High | Low | Low | Extremely low | Offline tools | 60/15 | 15 | Editor letters | Out of touch with the times | Modern element injection |
| SHYWV | 21 | Social anxiety college student | INFP | Alternative socializing | Face-to-face | Internet culture | Late night | Low frequency, medium intensity | Extremely low | Medium | High | Extremely high | Medium | Anonymous platforms | 20/10 | 5 | Anonymous community | Weak real-life scenes | Observation practice |
| OLDSL | 55 | Retired Military | ISTJ | Record history | Being forgotten | Documentary style | Early morning | High frequency, medium intensity | Low | Medium | Low | Low | Medium | Traditional tools | 25/5 | 10 | Veteran group | Emotional repression | Emotional release practice |
| NGTOW | 34 | Night-shift Nurse | ISFJ | Witness life and death | Helplessness | Medical drama | Daytime | Irregular | Medium-low | Medium | Medium | Medium | Medium | Mobile App | 15/5 | 4 | Colleagues | Time fragmentation | Micro-writing method |
| BOOKY | 29 | Librarian | INFJ | Story inheritance | Digitalization | Bookish tone | Evening | Medium frequency, medium intensity | Low | Medium-high | Medium | Medium | Medium-low | Traditional+digital hybrid | 25/5 | 8 | Book club | Overly literary | Visualization practice |
| GAMEX | 24 | Game Designer | INTP | Interactive narrative | Linearity | Branching structure | Late night | Low frequency, high intensity | Low | Medium | Medium | Low | Low | Game engine+Fountain | 40/10 | 10 | Gaming community | Overly complex | Linear core |
| MINML | 36 | Minimalist | ISTP | Essence pursuit | Redundancy | Minimalist style | Any time | Low frequency, medium intensity | Low | Medium | Low | Low | Low | Plain text editor | 30/5 | 6 | None needed | Too succinct | Detail supplementation |
| AN

…(clipped 37391 characters from `psychological_profile_agent_functional_specifications.md`)

### `sources/study/psychological_recommendation_agent_functional_specification.md`



# Psychology AI System for Movie Preference Prediction: Complete Guide (Expanded Edition)

## I. Core Conceptual Framework



### 1.1 Why Are Psychological Factors Needed?
Traditional recommendation systems primarily rely on viewing history and collaborative filtering, but incorporating psychological analysis can:

- Explain "why" a certain movie is recommended, providing explainable recommendations to help users understand the recommendation logic.
- Predict potential preferences for unexposed genres, solving the cold start problem.
- Provide more personalized and accurate recommendations, adjusted based on users' intrinsic traits such as personality and emotional state.
- Enhance user engagement and satisfaction; studies show that integrating personality traits can improve recommendation accuracy by 5-10% (refer to the Personality and Recommender Systems paper).
- Address diversity needs, avoid the filter bubble, and ensure recommendations cover content at different emotional and cognitive levels.

Additionally, psychological factors can handle situational changes, such as users preferring light content when under stress rather than high-intensity plots.



### 1.2 Overall System Flow
```
User data collection (viewing history, reviews, surveys) → Psychological feature extraction (personality prediction, sentiment analysis) → AI model training (integrating psychological features) → Preference prediction (multi-modal fusion) → Recommendation explanation and feedback loop
```



### 1.3 New: Empirical Foundation of Psychology in Recommendation Systems
According to the paper list (Psychology-based RecSys GitHub), multiple studies confirm that integrating Big Five personality traits can improve recommendation performance. For example, one study showed that for users high in extraversion, the click-through rate for recommending movies with social themes increased by 15%. Additionally, emotion-based recommendation systems (such as those using the PAD model) reduced RMSE by 0.05-0.1 on the MovieLens dataset.



## II. Classification of Psychological Factors



### 2.1 Basics: Big Five Personality Model
This is the most widely used personality framework, consisting of five dimensions (refer to the Personality and Recommender Systems paper):
**Extraversion**
- High scorers: Prefer social themes, romantic comedies, group interaction plots (e.g., Friends style).
- Low scorers: Prefer independent characters, introspective themes (e.g., art film Her).
- Integration method: Use personality prediction models to infer from user reviews.

**Agreeableness**
- High scorers: Like explorations of human nature, heartwarming family films, positive endings (e.g., Disney animations).
- Low scorers: Can accept moral gray areas, anti-hero characters (e.g., Joker).
- Research shows that high Agreeableness users have 20% higher satisfaction with positive content.

**Neuroticism**
- High scorers: May avoid horror, high-stress plots to prevent triggering anxiety.
- Low scorers: Can handle emotionally intense movies (e.g., thrillers).
- Application: Real-time emotion monitoring to avoid recommending high-intensity content.

**Openness**
- High scorers: Prefer art films, sci-fi, experimental movies (e.g., Inception).
- Low scorers: Prefer traditional narratives, commercial films (e.g., Marvel series).
- High Openness users are more receptive to new genre recommendations.

**Conscientiousness**
- High scorers: Like structurally complete, logically rigorous stories (e.g., detective films).
- Low scorers: Can accept open-ended endings, non-linear narratives (e.g., Pulp Fiction).

How to integrate using open-source frameworks: Use the yashsmehta/personality-prediction GitHub repo to predict Big Five scores from user text (e.g., reviews), then input as features into the recommendation model.



### 2.2 Advanced Factors
**Need for Cognition**
- **Definition**: The extent to which individuals prefer engaging in cognitive effort.
- **Influence**:
  - High Need for Cognition: Prefers complex plots, documentaries, art films (e.g., *Oppenheimer*).
  - Low Need for Cognition: Prefers light entertainment, easy-to-digest content, binge-watching (e.g., Netflix original comedies).
- **Measurement**: Need for Cognition Scale questionnaire or inferred from viewing patterns (e.g., viewing duration).
- **AI Application**: Predicts users' risk of continuous watching, recommends in-depth content. Uses Surprise library for expansion, integrates custom algorithms with cognition scores.

**Early Maladaptive Schemas**
- **Definition**: Negative belief patterns formed in childhood (e.g., abandonment, dependence, mistrust).
- **Influence**: Affects emotional regulation and preference for therapeutic content (e.g., recommending trauma-exploring films like *The Perks of Being a Wallflower*).
- **Measurement**: Young Schema Questionnaire or NLP analysis of reviews, using transformers library's BERT model.
- **AI Application**: Recommends plot-driven films exploring trauma and growth themes, avoids triggering negative patterns.

**Core Self-Evaluations**
- **Definition**: Includes self-esteem, self-efficacy, sense of control, emotional stability.
- **Influence**:
  - High evaluators: Can accept challenging content (e.g., adventure films).
  - Low evaluators: Prefers positive, inspirational movies (e.g., *The Pursuit of Happyness*).
- **Measurement**: Core Self-Evaluations Scale.
- **AI Application**: Avoids recommending content that may trigger negative emotions, uses emotion analysis pipeline for filtering.

**MOVIE Model**
- **Definition**: Movie-specific five-factor preference model
  - Melodrama
  - cOmic (Comedy)
  - Violent
  - Imaginative
  - Exciting
- **Advantages**: Directly corresponds to movie genres, supplements deficiencies of Big Five.
- **AI Application**: Serves as output layer to predict ratings for each genre, integrates into LightFM's feature matrix.

**Other Important Factors**
- **Gender**: Statistical preference differences (avoid stereotypes), e.g., women prefer romances more, but use data-driven approaches to avoid bias.
- **Cultural Background**: Influences acceptance of specific themes (e.g., Eastern cultures prefer collectivist themes), reference GCN-CF paper, use graph neural networks to integrate cultural features.
- **Current Emotional State**: May prefer escapist entertainment under stress, detected via facial recognition or text analysis.
- **Viewing Motivations**: Learning, escapism, social, emotional catharsis, inferred from questionnaires or behavioral data.
- **PAD Emotional Model**: PAD three-dimensional emotional model for user emotion modeling, includes Pleasure, Arousal, Dominance dimensions. From the paper "An intelligent film recommender system based on emotional analysis"[[2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC10280678/), uses PSO for optimizing multimodal feature fusion to achieve emotion-matching recommendations. Open-source implementation: Use PySwarms for PSO, combined with NLTK for sentiment.

**Attachment Styles** - Secure types prefer stable relationship plots, insecure types may avoid romances. Measured via questionnaires, integrated into the feature layer of recommendation models.

## III. Open-Source Frameworks and Tools Ecosystem



### 3.1 Core Framework for Recommendation Systems
**TensorFlow Recommenders (TFRS)**
TFRS is a library for building recommendation system models, supporting the entire recommendation system workflow: data preparation, model formulation, training, evaluation, and deployment[[1]](https://www.tensorflow.org/recommenders). How to integrate custom user features like personality traits: Use Big Five scores as part of the user embedding.

```python
import tensorflow as tf
import tensorflow_datasets as tfds
import tensorflow_recommenders as tfrs

# Load MovieLens data
ratings = tfds.load("movielens/100k-ratings", split="train")
movies = tfds.load("movielens/100k-movies", split="train")

# Define user model, integrate personalit

…(clipped 163321 characters from `psychological_recommendation_agent_functional_specification.md`)
