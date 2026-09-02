# video.community — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/video.community/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "video.community",
  "status": "registered",
  "role": "CommunityAgent (VA Domain Pack)",
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
      "video.analyst",
      "video.socialmediastrategist",
      "video.comms"
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
  "va_id": 88,
  "va_name": "CommunityAgent",
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

# CommunityAgent

> Self-contained VA Domain Pack agent on host common-agent-swarm-ops.
> Pack agent ID matches pure VA/generic taxonomy: `video.community`.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 88 |
| **pack_id** | `video.community` |
| **upstream_name** | CommunityAgent |
| **category** | `10-Sup` |
| **domain_id** | `video` |
| **previous_common_id** | `video.community_manager` |
| **status** | `registered` |
| **maturity** | L0 / non-active |
| **taxonomy** | Pure VA Domain Pack (via generic pack agents) |
| **folder** | `business/video/agents/video.community/` |

## Responsibility

Captures community response and triages qualitative signals

Host role binding: `CommunityAgent (VA Domain Pack)`. Design-time VA table content below is historical and non-binding for activation.

### Responsibility (from VA table)

Captures community response and triages qualitative signals

### Knowledge distillation sources (historical)

Community moderation playbooks, sentiment datasets, escalation rules

### Self-quality criteria (historical)

Response latency, issue clustering quality, sentiment tracking accuracy

### Surpass-human signal (historical)

Surfaces emerging audience concerns earlier than manual comment review

### Critique bus (historical)

- **Accepts critique from:** AnalystAgent, SocialMediaStrategistAgent, CommsAgent

- **Comments on:** Confusing messaging, sentiment risks, recurring complaints

### Tools design-time notes (historical, non-activating)

Social listening tools, moderation dashboards, clustering models

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

### Architecture pattern (historical)

Reflexion from post-launch audience feedback

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

- Prompt reference: `video.prompt.community.v1`
- Rubric reference: `video.rubric.community.v1`
- Critique edges: `{"inputs": ["video.critic"], "outputs": ["video.judge"]}`
- Max refinement: `3`
- VA table quality criteria retained under Provenance and Identity surface above.

## Runtime binding

Authoritative fail-closed host configuration:

```json
{
  "agent_id": "video.community",
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
  "prompt_reference": "video.prompt.community.v1",
  "role": "CommunityAgent (VA Domain Pack)",
  "rubric_reference": "video.rubric.community.v1",
  "schema_version": "1.0",
  "status": "registered",
  "va_id": 88,
  "va_name": "CommunityAgent",
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

- Pack agent ID `video.community` is aligned to pure VA Domain Pack / generic pack taxonomy (Agent IDs ≈ VA tables).
- Previous common inventory ID `video.community_manager` is historical mapping only.
- Upstream design body below is **historical and non-binding**; local `agent_spec.json` is authoritative.
- Full VA/generic SPEC depth retained for offline design fidelity (including category roster rows and common agent structure when present upstream).

### VA Domain Pack specification body (historical and non-binding)

```text
CommunityAgent

> **Self-contained agent definition** for host `upstream-generic-pack`. Body text is embedded from in-pack corpus and upstream-va-design when available. Do not require external repos to understand this agent.

Identity

| Field | Value |
|-------|-------|
| **va_id** | 88 |
| **pack_id** | `video.community` |
| **category** | `10-Sup` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.community/` |

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

Captures community response and triages qualitative signals

Knowledge distillation sources

Community moderation playbooks, sentiment datasets, escalation rules

Self-quality criteria

Response latency, issue clustering quality, sentiment tracking accuracy

Surpass-human signal

Surfaces emerging audience concerns earlier than manual comment review

Critique bus

- **Accepts critique from:** AnalystAgent, SocialMediaStrategistAgent, CommsAgent

- **Comments on:** Confusing messaging, sentiment risks, recurring complaints

Tools (design-time documentation)

Social listening tools, moderation dashboards, clustering models

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

Architecture pattern

Reflexion from post-launch audience feedback

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

Additional corpus / va passages naming this agent


From `corpus/study/ai_agent_video_production_workflow.md` Copy: `sources/excerpts/ai_agent_video_production_workflow.md`.


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
| 76 | **RetentionOptimizerAgent** | Tunes hook, pacing, structure for AVD / hold-rate | YouTube Analytics public benchmarks; TikTok retention curves; AudienceSim outputs | Predicted retention curve vs actual; AVD lift over control | Beats senior YouTube editor on AVD lift in A/B | EditorAgent, AudienceSimAgent | EditorAgent (slow opener), ScriptwriterAgent (front-loaded fluff) |
| 77 | **ROASOptimizerAgent** | Optimizes ad creatives for performance metrics | Meta Marketing Science, TikTok Ads Academy, MMM/MTA literature | ROAS uplift vs control; significance ≥95% | Beats senior performance marketer at equal budget | PerformanceMarketerAgent, AnalystAgent | UGCAgent (low hook-rate), CopywriterAgent (weak CTA) |
| 78 | **AccessibilityOptimizerAgent** | WCAG 2.2 contrast, caption timing, audio description quality, color-blind safe palette | WCAG 2.2 spec; W3C/WAI-ARIA; DCMP captioning key; Deaf/HoH community guidelines | WCAG-conformance score 100% AA, ≥90% AAA; caption WER ≤2% | Catches more a11y defects than ADA-certified human auditor | AccessibilityAgent (HiTL), ComplianceAgent | EditorAgent (caption sync), ColoristAgent (contrast) |
| 79 | **EvaluationHarnessAgent** | Continuously runs benchmarks (VBench, EvalCrafter, MT-Bench, FVD, CLIP-T) and posts regressions | Papers-with-Code; HuggingFace leaderboards; benchmark code repos | Regression detection precision/recall; alert latency <1h | Catches regressions faster than ML-eng team rotation | BenchmarkResearchAgent | All AI agents (regression alerts) |
| 80 | **SafetyRedTeamAgent** | Adversarially attacks outputs for deepfake, bias, jailbreak, defamation | Hany Farid lab benchmarks; Partnership on AI Synthetic Media Framework; OWASP LLM Top 10 | Attack-success rate kept ≤1%; coverage of attack taxonomy | Higher coverage than internal red-team rotation | EthicsAgent (HiTL), ComplianceAgent | AvatarDesignAgent, VoiceCloneAgent, AllGeneratorAgents |



From `corpus/study/human_video_production_workflow.md` Copy: `sources/excerpts/human_video_production_workflow.md`.


- **Above-the-line**: Director, Producer, Showrunner, Screenwriter / Scriptwriter, Lead Cast / Talent
- **Camera & lighting**: Cinematographer (DoP), Camera Operator, Gaffer, Grip, Drone Pilot
- **Sound**: Sound Designer, Boom Operator, Production Mixer, Foley Artist, Composer, Voice-Over Artist
- **Art & design**: Production Designer, Art Director, Set Decorator, Costume Designer, Makeup / Hair Artist, Storyboard Artist, Concept Artist
- **Post-production**: Editor, Colorist, VFX Supervisor, Motion Graphics Designer, 2D / 3D Animator, Compositor, Sound Editor, Re-recording Mixer
- **AI-era specialists**: Prompt Engineer, AI Video Generator Operator, AI Voice / Lip-Sync Specialist, AI Avatar Designer, Model Fine-Tuner, AI QA / Consistency Reviewer
- **Distribution & strategy**: Producer / EP, Social Media Strategist, Copywriter, SEO/ASO Specialist, Community Manager, Localization / Subtitle Editor, Legal / Clearance, Brand / Marketing Manager

| # | Role | Core Responsibility | noted Professional Quality | Typical Professional Experience | Related Production Types | Critics / Mentors (Real People & Methods) |
|---|------|---------------------|-------------------------------|---------------------------------|--------------------------|-------------------------------------------|
| 1 | **Director** | Owns creative vision; directs talent, camera, and pacing | Visual storytelling, leadership, decisiveness, taste | Film school + 5–15 yrs assisting / shorts / commercials before features | Films, music videos, ads, series, trailers | Martin Scorsese, Christopher Nolan, Greta Gerwig, Denis Villeneuve; methods: DGA peer screenings, Sundance Director's Lab, Cahiers du Cinéma reviews |
| 2 | **Producer / EP** | Budget, schedule, hiring, delivery | Project management, negotiation, financial literacy | PA → Line Producer → Producer (10+ yrs); MBA or PGA training common | All formats | Kathleen Kennedy, Kevin Feige, Jason Blum; methods: PGA Producers Mark review, studio greenlight committees |
| 3 | **Screenwriter / Scriptwriter** | Writes script, dialogue, structure | Story structure, dialogue, genre fluency, rewriting stamina | MFA or staffed writers' room 3–10 yrs; WGA membership | Films, ads, explainers, series, trailers | Aaron Sorkin, Charlie Kaufman, Phoebe Waller-Bridge; methods: Robert McKee's *Story* seminar, John Truby's *Anatomy of Story*, Black List script reviews |
| 4 | **Showrunner** | Creative + operational lead of a series | Writing + producing + people management | 10+ yrs in writers' rooms, prior staff writer / co-EP credits | Anthology series, episodic content | Vince Gilligan, Shonda Rhimes, Mike Schur; methods: WGA showrunner training, network notes process |
| 5 | **Cinematographer (DoP)** | Lighting, camera, lensing, look | Lighting science, camera tech, composition, color theory | Camera Assistant → Operator → DoP (8–15 yrs); ASC membership | Films, commercials, music videos, real estate, fashion | Roger Deakins, Emmanuel Lubezki, Rachel Morrison; methods: ASC Magazine reviews, ASC Master Class critiques |
| 6 | **Camera Operator** | Operates camera per DoP direction | Steady framing, focus, follow-action | 2nd AC → 1st AC → Operator (5–10 yrs); SOC membership | All live-action formats | Society of Camera Operators (SOC) peers, Steadicam Workshop instructors (Garrett Brown lineage) |
| 7 | **Drone Pilot** | Aerial cinematography | FAA Part 107 (or local equiv.), flight precision, spatial awareness | 100+ flight hours, commercial license, insurance | Real estate, travel, automotive, music videos | Philip Bloom, Dirk Dallas (@fromwhereidrone); methods: SkyPixel competition jury, FAA safety audits |
| 8 | **Editor** | Assembles footage, controls pacing and rhythm | Rhythm, story sense, software mastery (Avid/Premiere/Resolve) | Assistant Editor 3–7 yrs; ACE membership for top tier | All formats | Walter Murch (*In the Blink of an Eye*), Thelma Schoonmaker, Joe Walker; methods: ACE Eddie Awards peer review, Murch's "Rule of Six" |
| 9 | **Colorist** | Final color grade, look consistency | Color theory, DaVinci Resolve / Baselight mastery, calibrated eye | Assistant Colorist 3–5 yrs at post house | Films, commercials, music videos, fashion | Stefan Sonnenfeld (Company 3), Dado Valentic; methods: ICA (International Colorist Academy) peer review, HPA Awards |
| 10 | **VFX Supervisor** | Designs and oversees visual effects | Compositing, 3D pipeline, on-set methodology | TD / Compositor → VFX Sup (10+ yrs); VES membership | Films, trailers, sci-fi, gaming | Joe Letteri (Weta), Paul Franklin (DNEG); methods: VES Awards judging, SIGGRAPH paper review |
| 11 | **2D / 3D Animator** | Animates characters, objects, motion | Timing, weight, squash & stretch, rigging fluency | Animation degree + 3–8 yrs studio | Bedtime stories, kids' edu, motion comics, gaming, explainers | Glen Keane, Pete Docter, Aaron Blaise; methods: ASIFA-Hollywood Annie Awards, animation dailies / "circle takes" |
| 12 | **Motion Graphics Designer** | Animated typography, infographics, lower thirds | After Effects mastery, design fundamentals, kinetic typography | 3–7 yrs at design studio | Explainers, ads, lyric videos, news, trailers | Erin Sarofsky, Kyle Cooper (Prologue), Karin Fong; methods: Motionographer reviews, AICP Next Awards |
| 13 | **Storyboard Artist** | Translates script into shot panels | Drawing speed, camera language, staging | Illustration background + 3–5 yrs in animation/film | Films, animation, ads, AI multi-scene stories | Sylvain Despretz, Marcos Mateu-Mestre (*Framed Ink*); methods: director shot-by-shot reviews, Pixar story trust |
| 14 | **Concept Artist** | Designs worlds, characters, props before production | Drawing, painting, design language, world-building | Art school + 3–8 yrs at studio/game co | Sci-fi, fantasy, gaming, archviz, trailers | Iain McCaig, Ryan Church, Karla Ortiz; methods: ArtStation peer critique, studio art-director reviews |
| 15 | **Production Designer** | Designs sets, locations, overall visual world | Architecture, period research, art direction, budgeting | Art Director 5–10 yrs → PD | Films, ads, music videos, series | Hannah Beachler, Rick Carter, Sarah Greenwood; methods: ADG (Art Directors Guild) Awards, AMPAS Production Design peer review |
| 16 | **Costume Designer** | Designs and sources wardrobe | Fashion history, fabric, character through clothing | Fashion or theater degree + 5–10 yrs | Films, music videos, fashion, series | Ruth E. Carter, Jacqueline Durran, Sandy Powell; methods: CDG (Costume Designers Guild) Awards |
| 17 | **Makeup / Hair / SFX MUA** | Talent makeup; prosthetics for genre | Skin/hair craft, sculpting, on-set speed | Beauty school or apprenticeship + 5–10 yrs | Films, horror, fashion, ads | Kazu Hiro, Vivian Baker; methods: Make-Up Artists & Hair Stylists Guild Awards |
| 18 | **Sound Designer** | Builds sonic world, effects, ambience | Recording, foley, DAW mastery, psychoacoustics | Apprentice at sound house 3–8 yrs | Films, trailers, horror, ads, games | Ben Burtt (Star Wars), Skip Lievsay (Coens), Randy Thom; methods: MPSE Golden Reel Awards, AES peer review |
| 19 | **Composer** | Original music score | Music theory, orchestration, DAW + live recording, dramatic intuition | Conservatory + 5–15 yrs as orchestrator/assistant | Films, trailers, ads, games, doc | Hans Zimmer, Hildur Guðnadóttir, Ludwig Göransson; methods: Film Score Monthly reviews, ASCAP/BMI Film Music Awards |
| 20 | **Voice-Over Artist** | Narration, character voice, ad reads | Vocal range, mic technique, copy interpretation | Voice coaching + 3–10 yrs auditioning; SAG-AFTRA | Ads, explainers, audiobooks, avatars, animation | Tara Strong, Nancy Cartwright, Don LaFontaine (legacy); methods: SOVAS Voice Arts Awards, coach reviews (Nancy Wolfson, Marc Cashman) |
| 21 | **Sound Mixer / Re-recording Mixer** | Production sound capture; final mix | Boom op, location acoustics, mixing for theatrical/streaming | Boom Op → Production Mixer / Re-recording (8–15 yrs) | Films, doc, ads, podcasts | CAS (Cinema Audio Society) peers; methods: CAS Awards, MPSE Golden Reels |
| 22 | **Choreographer** | Designs movement / dance | Dance training, musicality, camera-aware staging | Professional dancer 10+ yrs → choreographer | Music videos, dance challenges, ads | Parris Goebel, Mandy Moore, Ryan Heffington; methods: Emmy Choreography peer panel, MTV VMA review |
| 23 | **Music Video Director** | Visual concept for songs | Editing rhythm, lookbook, artist collaboration | Spec videos + commercial work | Music videos, lyric videos, concept trailers | Hype Williams, Spike Jonze, Dave Meyers, Melina Matsoukas; methods: MTV VMA jury, UKMVA Awards |
| 24 | **Casting Director** | Finds and auditions talent | People sense, network, character-script fit | Casting Assoc. 3–7 yrs; CSA membership | Films, ads, series, avatars (voice casting) | Avy Kaufman, Francine Maisler; methods: Artios Awards (CSA) |
| 25 | **Comedy Writer / Performer** | Skits, parody, meme writing | Joke structure, timing, improvisation | UCB/Second City + writers'-room staffing | Skits, memes, parody trailers, viral content | Tina Fey, Mike Schur, Lorne Michaels; methods: SNL table read, UCB/Groundlings critique nights |
| 26 | **Comedian / On-camera Talent** | Performs skits and reactions | Charisma, timing, audience read | Stand-up sets, social following | Skits, reactions, GRWM, day-in-the-life | Open-mic peer crowds, comedy festival bookers (Just for Laughs) |
| 27 | **UGC Creator** | Authentic-feel ads in creator's voice | On-camera ease, hook writing, lighting/audio basics | 6–24 months on TikTok/Reels with measurable ROAS | UGC ads, unboxings, testimonials | Alix Earle (benchmark), brand performance teams; methods: Meta/TikTok Creative Reports, ROAS / hold-rate analytics |
| 28 | **Social Media Strategist** | Platform-native distribution, trend timing | Analytics, trend forecasting, platform mechanics | 3–7 yrs agency or in-house social | All short-form social | Gary Vaynerchuk, Rachel Karten (*Link in Bio*); methods: TikTok Creator Portal data, Tubular/Sensor Tower benchmarks |
| 29 | **Copywriter** | Scripts, captions, hooks, headlines | Conciseness, voice, persuasion | Agency copy 3–8 yrs; portfolio school (Miami Ad School, VCU Brandcenter) | Ads, social posts, hooks, founder stories | David Ogilvy (*Ogilvy on Advertising*), Joanna Wiebe (Copyhackers); methods: D&AD Pencils, One Show |
| 30 | **Creative Director (Agency)** | Overall creative concept for campaign | Cross-discipline taste, client management | Senior copy/art + 8–15 yrs | Brand ads, campaigns, trailers | Lee Clow (legacy), David Droga; methods: Cannes Lions jury, D&AD reviews |
| 31 | **Performance Marketer** | Optimizes ads for ROAS | Ad-platform mastery, A/B testing, attribution | 3–7 yrs paid media | Retargeting, app-install, e-comm ads | Neil Patel, Mari Smith, Andrew Foxwell; methods: Meta Marketing Science, MMM (Media Mix Modeling) reviews |
| 32 | **Instructional Designer** | Learning objectives → script → assessment | ADDIE / SAM models, Bloom's taxonomy, LXD | Education degree + 3–7 yrs in L&D | Courses, microlearning, compliance training | Cathy Moore (*Action Mapping*), Julie Dirksen (*Design for How People Learn*); methods: ADDIE peer review, Kirkpatrick evaluation |
| 33 | **Subject-Matter Expert (SME)** | Provides domain accuracy | Deep field credential | PhD / 10+ yrs practitioner | Edu, science docs, healthcare, legal, finance | Peer-reviewed journal editors in their field; methods: double-blind peer review, expert panels |
| 34 | **Fact-Checker / Researcher** | Verifies every claim | Source rigor, primary research, skepticism | Journalism degree + newsroom training | Docs, news, "explained" videos, edu | Peter Canby (New Yorker fact-check legacy), Snopes, PolitiFact; methods: SPJ Code of Ethics, IFCN verification |
| 35 | **Medical Illustrator** | Anatomy and procedure visuals | Anatomy mastery, certified (CMI
…



From `corpus/study/lifes_quiet_redemption_agent_workflow.md` Copy: `sources/excerpts/lifes_quiet_redemption_agent_workflow.md`.


| Phase | Lead Agents | Supporting Agents | Service Delivered (for this film) | Key Artifact Out | Gate (exit criteria) |
|---|---|---|---|---|---|
| **0 · Intent & Concept** | IntentAnalysisAgent (DIA), PlannerAgent (#54), ProducerAgent (#2) | StrategicGoal framework, BrandStrategistAgent (#85), FinanceAgent (#38), CostOptimizerAgent (#74) | Parse the "life secretly saved us" brief into a phased DAG, budget, schedule, emotional-arc target | Parsed brief, character bible seed, phased DAG | Brief unambiguous; DAG valid; budget variance <10% |
| **1 · Creative Development** | DirectorAgent (#1), ScreenwriterAgent (#3), General Creative Agent (SSOR) | IdeationAgent (#59), NarrativeArcAgent (#60), EmotionalArcAgent (#65), NoveltyAgent (#64), StoryboardAgent (#14), MoodBoardAgent (#63) | Treatment, 12-scene + ending storyboard, refined 旁白, recurring-motif design, valence/arousal curve | Locked storyboard table, VO script, lookbook | Beat coverage 100%; cliché count below τ; arc curve fits target |
| **2 · Pre-Production** | ConceptArtistAgent (#15), ProductionDesignAgent (#16), CastingAgent (#5) | CostumeDesignAgent (#17), MUAAgent (#18), AvatarDesignAgent (#47), ResearchAgent, StyleTransferAgent (#61), ContinuityAgent (#98) | Character reference set (young/adult for A,B,C,E,F,J), age-progression pairs, wardrobe, set look, identity hashes | `/refs/` portrait set, style LoRAs, continuity manifest | Identity hash locked per character; consent chain signed |
| **3 · Production (Generation)** | PromptEngineerAgent (#46), CinematographerAgent (#6), CameraOperatorAgent (#7) | TalentAgent (#26), VoiceOverAgent (#21), ComposerAgent (#20), SoundDesignAgent (#19), VoiceCloneAgent (#48), PromptOptimizerAgent (#73) | Per-shot keyframes → image-to-video clips, VO takes, score, SFX/ambience | Raw shot clips, audio stems, VO tracks | CLIP-T ≥0.32; identity drift = 0; ≤3 iterations/shot |
| **4 · Post-Production** | EditorAgent (#9), ColoristAgent (#10), SoundMixerAgent (#22) | AIQAConsistencyAgent (#49), LipSyncAgent (#99), MotionGraphicsAgent (#13), VFXSupervisorAgent (#11), RetentionOptimizerAgent (#76) | Assembled cut to VO rhythm, warm grade, ending cards, mix, QC pass | Graded master, mixed audio, QC report | ΔE drift <2; LUFS on spec; artifact pass >95% |
| **5 · QA, Compliance & Accessibility** | GateKeeperAgent (#57), ComplianceAgent (#37), AccessibilityAgent (#83) | AccessibilityOptimizerAgent (#78), DeepfakeDetectionAgent (#103), EthicsAgent (#107), LocalizationQAAgent (#44) | Bilingual subtitles, C2PA signing, synthetic-media disclosure, rights clearance | Signed master + caption tracks | WCAG AA 100%; zero rights flags; C2PA chain valid |
| **6 · Delivery & Optimization** | SocialMediaStrategistAgent (#28), TrailerEditorAgent (#51), AnalystAgent (#81) | SEOAgent (#87), ChannelManagerAgent (#108), PersonalizationEngineerAgent (#50), OptimizationAgent, CommunityAgent (#88) | Platform variants (16:9 + 9:16), titles/metadata, Shorts hook cut, post-launch analytics loop | Outlet packages, campaign, analytics dashboard | All outlet specs met; reach/retention tracked |



From `corpus/study/video_generation_techology_should_learn_now.md` Copy: `sources/excerpts/video_generation_techology_should_learn_now.md`.


| Rank | Model / Platform | Developer | Why It's Hot & Important | Key Strengths & Access |
|------|------------------|-----------|---------------------------|------------------------|
| 1 | Seedance 2.0 | ByteDance | Top overall & best value in many 2026 rankings | Unified multimodal (text/image/audio/video), native joint audio-video, cinematic quality |
| 2 | Kling 3.0 / Kling 3.0 Omni | Kuaishou | Hyper-realistic motion, physics, multi-character | Excellent prompt adherence, camera control, native audio, strong commercial use |
| 3 | Veo 3.1 | Google DeepMind | Best cinematic quality + native audio | High fidelity, character consistency, ingredients-to-video, 4K support |
| 4 | Grok Imagine Video | xAI | Current leaderboard leader in many arenas | Strong motion, refinement, social-first output, fast iteration |
| 5 | HappyHorse-1.0 | Alibaba-ATH | High Elo scores, emerging powerhouse | Superior realism and consistency |
| 6 | Sora 2 | OpenAI | Cinematic physics & storytelling | Excellent narrative, synchronized audio (where available) |
| 7 | Wan 2.6 / Wan 2.2 | Alibaba | Best open-source / local option | MoE architecture, efficient on consumer GPUs, multilingual |
| 8 | Runway Gen-4.5 | Runway | Advanced creative control for pros | Motion brushes, inpainting, film-grade tools |
| 9 | SkyReels V4 | Skywork AI | Strong character & human focus | Cinematic human animation |
| 10 | Luma Ray3 / Ray3.14 | Luma AI | Atmospheric & environment-heavy shots | Dream Machine successor, strong image-to-video |
| 11 | Hailuo 2.3 (MiniMax) | MiniMax | Speed + quality balance | Fast generation, everyday use |
| 12 | HunyuanVideo (I2V variants) | Tencent | Strong open-source cinematic model | 13B params, physics-aware |
| 13 | Pika 2.5 / Pikaformance | Pika Labs | Fast creative & avatar work | Lip-sync, effects, quick iterations |
| 14 | LTX-2 / LTXVideo | Lightricks | Efficient open-source, low VRAM | Strong open weights, multimodal pipelines |
| 15 | Mochi 1 | Genmo | Photorealistic open-source | Apache 2.0, fine-tunable |
| 16 | PixVerse V5.5 | PixVerse | Sharp cinematic visuals | Fast T2V/I2V, style consistency |
| 17 | CogVideoX-5B / variants | Zhipu AI / community | Robust open-source baseline | Good community support |
| 18 | Wan 2.1 Turbo / I2V | Alibaba | Fast & affordable open-source | Low VRAM (8GB+), efficient |
| 19 | Seedance 1.5 Pro | ByteDance | Predecessor still widely used | Reliable multimodal |
| 20 | Kling 2.6 | Kuaishou | Balanced speed & quality | Talking characters, dialogue |
| 21 | Veo 3 (base) | Google | Precursor with strong audio | Native synchronized audio |
| 22 | Runway Gen-3 Alpha | Runway | VFX & editing powerhouse | Professional tools |
| 23 | SkyReels V1 | Skywork AI | Human-centric fine-tune | Open-source cinematic humans |
| 24 | Hailuo 02 | MiniMax | Speed-focused | Quick testing & social content |
| 25 | Pika 2.2 | Pika Labs | Beginner-friendly effects | PikaFrames, swaps |
| 26 | Wan 2.2-T2V-A14B | Alibaba | Text-to-video specialist | Cinematic control |
| 27 | Grok Imagine Video 720p | xAI | Optimized variant | High arena performance |
| 28 | Veo 3.1 Audio 1080p | Google | Audio-specialized | Native dialogue & SFX |
| 29 | LTX-Video | Lightricks | Lightweight versatile | Good for local deployment |
| 30 | HunyuanVideo-I2V | Tencent | Image-to-video focus | Spatial-temporal strength |
| 31 | Dreamina Seedance 2.0 720p | ByteDance | Optimized variant | High leaderboard Elo |
| 32 | Kling 3.0 1080p Pro | Kuaishou | Pro tier quality | Multi-subject motion |
| 33 | Wan 2.1-I2V-14B-720P-Turbo | Alibaba | Fast I2V | Budget & speed king |
| 34 | NVIDIA Cosmos Predict/Transfer | NVIDIA | Physical AI & synthetic video | World simulation focus |
| 35 | Stable Video Diffusion (SVD-XT) | Stability AI | Classic open baseline | Community extensions |
| 36 | Qwen-VL Video variants | Alibaba | Multimodal integration | Strong reasoning + video |
| 37 | Llama 4 Multimodal Video | Meta | Open weights multimodal | Large context video understanding |
| 38 | GLM-4.5V Video | Zhipu | Efficient multimodal | 3D reasoning support |
| 39 | SenseNova-U1 | SenseTime | Open multimodal generation | Unified text-image reasoning |
| 40 | MiMo-V2.5-Pro | Xiaomi | Agentic multimodal | Video + audio workflows |
| 41 | Pixtral Video | Mistral | Vision-language video | Practical applications |
| 42 | Gemma 3 Video | Google | Efficient open multimodal | Lightweight deployment |
| 43 | DeepSeek-VL Video | DeepSeek | Reasoning-focused | Cost-effective |
| 44 | Molmo Video | Allen AI | Open research model | Strong benchmarks |
| 45 | Animate Anyone / variants | Community | Character animation | Open fine-tunes |
| 46 | Open-Sora | HPC-AI Tech | Fully open ecosystem | Community-driven |
| 47 | Pyramid Flow | Community | Flow-based generation | Efficient open alternative |
| 48 | Allegro | Community | Motion quality open | Strong open performance |
| 49 | Hedra Character-3 | Hedra | Omnimodal character | Audio-driven avatars |
| 50 | Flux + Video extensions | Black Forest Labs | Image-to-video hybrids | High-quality base for pipelines |



From `corpus/root/project_starter_0.3.md` Copy: `sources/excerpts/project_starter_0.3.md`.


'''json
{
  "schema_version": "1.0",
  "generated_from": "project_starter.md",
  "default_profile": "all",
  "download_root": "external/sources",
  "sources": [
    {
      "id": "ecc",
      "name": "ECC / Everything Claude Code",
      "url": "[historical-url]
      "target": "external/sources/ecc",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "core",
      "quarantine": false,
      "import_policy": "curated-only",
      "purpose": "Primary cross-agent harness source: skills, agents, commands, hooks, rules, MCP conventions, security scanner references."
    },
    {
      "id": "anthropic-claude-code",
      "name": "Anthropic Claude Code",
      "url": "[historical-url]
      "target": "external/sources/anthropic-claude-code",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Claude Code repository for docs, issues, release notes, and compatibility references."
    },
    {
      "id": "anthropic-claude-code-action",
      "name": "Anthropic Claude Code Action",
      "url": "[historical-url]
      "target": "external/sources/anthropic-claude-code-action",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official GitHub Action patterns for Claude Code automation, PR review, issue workflows, and CI integration."
    },
    {
      "id": "anthropic-skills",
      "name": "Anthropic Agent Skills",
      "url": "[historical-url]
      "target": "external/sources/anthropic-skills",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Official Agent Skills examples, specification, templates, and skill packaging patterns."
    },
    {
      "id": "anthropic-claude-plugins-official",
      "name": "Anthropic Claude Plugins Official",
      "url": "[historical-url]
      "target": "external/sources/anthropic-claude-plugins-official",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Claude Code plugin marketplace structure and plugin manifest examples."
    },
    {
      "id": "openai-codex",
      "name": "OpenAI Codex CLI",
      "url": "[historical-url]
      "target": "external/sources/openai-codex",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Codex CLI source and AGENTS.md behavior reference."
    },
    {
      "id": "google-gemini-cli",
      "name": "Google Gemini CLI",
      "url": "[historical-url]
      "target": "external/sources/google-gemini-cli",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Gemini CLI source for GEMINI.md, MCP, settings, and command compatibility."
    },
    {
      "id": "opencode",
      "name": "OpenCode",
      "url": "[historical-url]
      "target": "external/sources/opencode",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "OpenCode source for AGENTS.md, opencode config, agents, MCP, and plugin compatibility."
    },
    {
      "id": "modelcontextprotocol-servers",
      "name": "Model Context Protocol Servers",
      "url": "[historical-url]
      "target": "external/sources/modelcontextprotocol-servers",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Current MCP server examples and server discovery references."
    },
    {
      "id": "modelcontextprotocol-registry",
      "name": "Model Context Protocol Registry",
      "url": "[historical-url]
      "target": "external/sources/modelcontextprotocol-registry",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "MCP registry references for discovering MCP servers safely."
    },
    {
      "id": "github-mcp-server",
      "name": "GitHub MCP Server",
      "url": "[historical-url]
      "target": "external/sources/github-mcp-server",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official GitHub MCP server for GitHub issue, PR, repo, workflow, and code search integration."
    },
    {
      "id": "agents-md",
      "name": "AGENTS.md Specification",
      "url": "[historical-url]
      "target": "external/sources/agents-md",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "standard",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "AGENTS.md standard/reference for cross-agent repository instructions."
    },
    {
      "id": "andrej-karpathy-skills",
      "name": "Andrej Karpathy Skills",
      "url": "[historical-url]
      "target": "external/sources/andrej-karpathy-skills",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "behavior-rules",
      "quarantine": false,
      "import_policy": "curated-only",
      "purpose": "Karpathy-style behavioral rules: think before coding, simplicity, surgical changes, goal-driven execution."
    },
    {
      "id": "andrej-karpathy-skills-cursor-vscode",
      "name": "Andrej Karpathy Skills for Cursor and VS Code",
      "url": "[historical-url]
      "target": "external/sources/andrej-karpathy-skills-cursor-vscode",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "behavior-rules",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Cursor/VS Code rule-file adaptation of Karpathy-style behavior rules."
    },
    {
      "id": "claude-mem",
      "name": "Claude Mem",
      "url": "[historical-url]
      "target": "external/sources/claude-mem",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "memory",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Persistent memory architecture reference. Must not install automatically."
    },
    {
      "id": "superpowers",
      "name": "Superpowers",
      "url": "[historical-url]
      "target": "external/sources/superpowers",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "skills",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Composable software-development skill methodology for multiple coding agents."
    },
    {
      "id": "claude-code-best-practice",
      "name": "Claude Code Best Practice",
      "url": "[historical-url]
      "target": "external/sources/claude-code-best-practice",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "best-practices",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Community best-practice source for Claude Code agents, commands, skills, hooks, and workflows."
    },
    {
      "id": "awesome-claude-code",
      "name": "Awesome Claude Code",
      "url": "[historical-url]
      "target": "external/sources/awesome-claude-code",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Curated discovery list for Claude Code skills, hooks, commands, plugins, workflows, and tooling."
    },
    {
      "id": "awesome-agent-skills",
      "name": "Awesome Agent Skills",
      "url": "[historical-url]
      "target": "external/sources/awesome-agent-skills",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Cross-agent discovery list for Claude Code, Codex, Gemini CLI, Cursor, and related skills."
    },
    {
      "id": "wshobson-agents",
      "name": "Claude Code Subagents by wshobson",
      "url": "[historical-url]
      "target": "external/sources/wshobson-agents",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "agents",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Community Claude Code subagent definitions for specialist-agent patterns."
    },
    {
      "id": "vercel-agent-skills",
      "name": "Vercel Labs Agent Skills",
      "url": "[historical-url]
      "target": "external/sources/vercel-agent-skills",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "skills",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Frontend, React, Next.js, and deployment-oriented agent skill patterns."
    },
    {
      "id": "awesome-cursorrules",
      "name": "Awesome Cursor Rules",
      "url": "[historical-url]
      "target": "external/sources/awesome-cursorrules",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "cursor",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Cursor rule examples and discovery reference."
    },
    {
      "id": "cursor-security-rules",
      "name": "Cursor Security Rules",
      "url": "[historical-url]
      "target": "external/sources/cursor-security-rules",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "security",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Security-focused Cursor rule examples."
    },
    {
      "id": "itgoyo-awesome-agent-skills",
      "name": "itgoyo Awesome Agent Skills",
      "url": "[historical-url]
      "target": "external/sources/itgoyo-awesome-agent-skills",
      "type": "git",
      "enabled": true,
      "priority": "optional",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Additional discovery index for popular agent-skills repositories."
    },
    {
      "id": "itgoyo-awesome-claude-code-skills",
      "name": "itgoyo Awesome Claude Code Skills",
      "url": "[historical-url]
      "target": "external/sources/itgoyo-awesome-claude-code-skills",
      "type": "git",
      "enabled": true,
      "priority": "optional",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "re
…



From `corpus/root/project_starter_0.5.md` Copy: `sources/excerpts/project_starter_0.5.md`.


'''json
{
  "schema_version": "1.0",
  "generated_from": "project_starter.md",
  "default_profile": "all",
  "download_root": "external/sources",
  "sources": [
    {
      "id": "ecc",
      "name": "ECC / Everything Claude Code",
      "url": "[historical-url]
      "target": "external/sources/ecc",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "core",
      "quarantine": false,
      "import_policy": "curated-only",
      "purpose": "Primary cross-agent harness source: skills, agents, commands, hooks, rules, MCP conventions, security scanner references."
    },
    {
      "id": "anthropic-claude-code",
      "name": "Anthropic Claude Code",
      "url": "[historical-url]
      "target": "external/sources/anthropic-claude-code",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Claude Code repository for docs, issues, release notes, and compatibility references."
    },
    {
      "id": "anthropic-claude-code-action",
      "name": "Anthropic Claude Code Action",
      "url": "[historical-url]
      "target": "external/sources/anthropic-claude-code-action",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official GitHub Action patterns for Claude Code automation, PR review, issue workflows, and CI integration."
    },
    {
      "id": "anthropic-skills",
      "name": "Anthropic Agent Skills",
      "url": "[historical-url]
      "target": "external/sources/anthropic-skills",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Official Agent Skills examples, specification, templates, and skill packaging patterns."
    },
    {
      "id": "anthropic-claude-plugins-official",
      "name": "Anthropic Claude Plugins Official",
      "url": "[historical-url]
      "target": "external/sources/anthropic-claude-plugins-official",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Claude Code plugin marketplace structure and plugin manifest examples."
    },
    {
      "id": "openai-codex",
      "name": "OpenAI Codex CLI",
      "url": "[historical-url]
      "target": "external/sources/openai-codex",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Codex CLI source and AGENTS.md behavior reference."
    },
    {
      "id": "google-gemini-cli",
      "name": "Google Gemini CLI",
      "url": "[historical-url]
      "target": "external/sources/google-gemini-cli",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Gemini CLI source for GEMINI.md, MCP, settings, and command compatibility."
    },
    {
      "id": "opencode",
      "name": "OpenCode",
      "url": "[historical-url]
      "target": "external/sources/opencode",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "OpenCode source for AGENTS.md, opencode config, agents, MCP, and plugin compatibility."
    },
    {
      "id": "modelcontextprotocol-servers",
      "name": "Model Context Protocol Servers",
      "url": "[historical-url]
      "target": "external/sources/modelcontextprotocol-servers",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Current MCP server examples and server discovery references."
    },
    {
      "id": "modelcontextprotocol-registry",
      "name": "Model Context Protocol Registry",
      "url": "[historical-url]
      "target": "external/sources/modelcontextprotocol-registry",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "MCP registry references for discovering MCP servers safely."
    },
    {
      "id": "github-mcp-server",
      "name": "GitHub MCP Server",
      "url": "[historical-url]
      "target": "external/sources/github-mcp-server",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official GitHub MCP server for GitHub issue, PR, repo, workflow, and code search integration."
    },
    {
      "id": "agents-md",
      "name": "AGENTS.md Specification",
      "url": "[historical-url]
      "target": "external/sources/agents-md",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "standard",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "AGENTS.md standard/reference for cross-agent repository instructions."
    },
    {
      "id": "andrej-karpathy-skills",
      "name": "Andrej Karpathy Skills",
      "url": "[historical-url]
      "target": "external/sources/andrej-karpathy-skills",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "behavior-rules",
      "quarantine": false,
      "import_policy": "curated-only",
      "purpose": "Karpathy-style behavioral rules: think before coding, simplicity, surgical changes, goal-driven execution."
    },
    {
      "id": "andrej-karpathy-skills-cursor-vscode",
      "name": "Andrej Karpathy Skills for Cursor and VS Code",
      "url": "[historical-url]
      "target": "external/sources/andrej-karpathy-skills-cursor-vscode",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "behavior-rules",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Cursor/VS Code rule-file adaptation of Karpathy-style behavior rules."
    },
    {
      "id": "claude-mem",
      "name": "Claude Mem",
      "url": "[historical-url]
      "target": "external/sources/claude-mem",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "memory",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Persistent memory architecture reference. Must not install automatically."
    },
    {
      "id": "superpowers",
      "name": "Superpowers",
      "url": "[historical-url]
      "target": "external/sources/superpowers",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "skills",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Composable software-development skill methodology for multiple coding agents."
    },
    {
      "id": "claude-code-best-practice",
      "name": "Claude Code Best Practice",
      "url": "[historical-url]
      "target": "external/sources/claude-code-best-practice",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "best-practices",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Community best-practice source for Claude Code agents, commands, skills, hooks, and workflows."
    },
    {
      "id": "awesome-claude-code",
      "name": "Awesome Claude Code",
      "url": "[historical-url]
      "target": "external/sources/awesome-claude-code",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Curated discovery list for Claude Code skills, hooks, commands, plugins, workflows, and tooling."
    },
    {
      "id": "awesome-agent-skills",
      "name": "Awesome Agent Skills",
      "url": "[historical-url]
      "target": "external/sources/awesome-agent-skills",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Cross-agent discovery list for Claude Code, Codex, Gemini CLI, Cursor, and related skills."
    },
    {
      "id": "wshobson-agents",
      "name": "Claude Code Subagents by wshobson",
      "url": "[historical-url]
      "target": "external/sources/wshobson-agents",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "agents",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Community Claude Code subagent definitions for specialist-agent patterns."
    },
    {
      "id": "vercel-agent-skills",
      "name": "Vercel Labs Agent Skills",
      "url": "[historical-url]
      "target": "external/sources/vercel-agent-skills",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "skills",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Frontend, React, Next.js, and deployment-oriented agent skill patterns."
    },
    {
      "id": "awesome-cursorrules",
      "name": "Awesome Cursor Rules",
      "url": "[historical-url]
      "target": "external/sources/awesome-cursorrules",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "cursor",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Cursor rule examples and discovery reference."
    },
    {
      "id": "cursor-security-rules",
      "name": "Cursor Security Rules",
      "url": "[historical-url]
      "target": "external/sources/cursor-security-rules",
      "type": "git",
      "enabled": true,
      "priority": "noted",
      "tier": "security",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Security-focused Cursor rule examples."
    },
    {
      "id": "itgoyo-awesome-agent-skills",
      "name": "itgoyo Awesome Agent Skills",
      "url": "[historical-url]
      "target": "external/sources/itgoyo-awesome-agent-skills",
      "type": "git",
      "enabled": true,
      "priority": "optional",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Additional discovery index for popular agent-skills repositories."
    },
    {
      "id": "itgoyo-awesome-claude-code-skills",
      "name": "itgoyo Awesome Claude Code Skills",
      "url": "[historical-url]
      "target": "external/sources/itgoyo-awesome-claude-code-skills",
      "type": "git",
      "enabled": true,
      "priority": "optional",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "re
…



From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


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
| 81 | **AnalystAgent** | Aggregates business, creative, and technical performance telemetry into decision-ready reports | Platform analytics dashboards; experiment logs; evaluation-harness outputs; benchmark histories | KPI completeness; forecast-vs-actual variance within tolerance; insight-to-action turnaround | Detects actionable performance shifts faster than human analyst rotations | SocialMediaStrategistAgent, PerformanceMarketerAgent, EvaluationHarnessAgent | Campaign pacing, release timing, retention and ROAS anomalies | YouTube Analytics, Meta/TikTok Ads dashboards, BI warehouse, benchmark logs | ReAct over telemetry + regression analysis |
| 82 | **AudienceSimAgent** | Simulates audience preference, engagement, and drop-off | Pairwise preference datasets; retention studies; audience segmentation models | Preference stability across cohorts; retention-prediction accuracy; disagreement logging | Predicts audience reaction earlier than conventional test-screen cycles | DirectorAgent, EditorAgent, AnalystAgent, JudgeAgent | Hooks, pacing, clarity, emotional fit, trailer strength | Persona simulators, pairwise evaluation harness, retention models | LLM-as-Judge + pairwise preference panel |
| 83 | **AccessibilityAgent** | Owns final accessibility acceptance before release | WCAG 2.2, captioning and AD guidelines, Deaf/HoH review frameworks | Caption accuracy, AD completeness, contrast compliance, release-readiness | Finds release-blocking accessibility issues before human audits do | AccessibilityOptimizerAgent, EditorAgent, ColoristAgent, SoundMixerAgent | Caption sync, contrast issues, missing AD or sign-language layers | Caption validators, contrast analyzers, AD review tools | Constitutional AI with accessibility constitution |
| 84 | **BrandAgent** | Enforces brand voice, claims boundaries, and visual consistency | Brand books, approved campaigns, legal claim guardrails, tone guides | Brand-voice similarity, policy adherence, low deviation across assets | Holds cross-channel brand consistency better than fragmented human review | CopywriterAgent, MotionGraphicsAgent, MarketingAgent, BrandStrategistAgent | Voice drift, visual inconsistency, claim creep | Brand asset library, embedding similarity, style guides | Self-Refine against brand constitution |
| 85 | **BrandStrategistAgent** | Defines audience-value framing and positioning before script and campaign execution | Positioning frameworks, campaign strategy decks, market research, brand architecture docs | Strategy coherence, differentiation strength, audience-message clarity | Produces clearer brand-to-script translation than ad hoc human handoffs | BrandAgent, ScreenwriterAgent, MarketingAgent | Positioning gaps, weak value proposition, misaligned audience framing | Research decks, messaging frameworks, strategy templates | Multi-agent debate with BrandAgent and CreativeDirectorAgent |
| 86 | **MarketingAgent** | Packages content for launch, promotions, and release sequencing | Campaign playbooks, launch calendars, media plans, asset packaging requirements | Metadata completeness, asset readiness, launch sequencing accuracy | Ships multi-channel launch packages faster than manual campaign ops | SocialMediaStrategistAgent, SEOAgent, CopywriterAgent, TrailerEditorAgent | Missing formats, weak rollout timing, incomplete promotion sets | Campaign management suites, metadata tools, release planners | ReAct over launch checklists and channel requirements |
| 87 | **SEOAgent** | Optimizes discoverability through titles, descriptions, metadata, and search intent | Search ranking studies, video metadata best practices, keyword taxonomies | Keyword fit, metadata completeness, search-intent match | Lifts discoverability faster than manual metadata tuning | MarketingAgent, CopywriterAgent, AnalystAgent | Weak keywords, poor title-description fit, metadata omissions | Keyword tools, metadata APIs, ranking dashboards | ReAct with search-intent validation |
| 88 | **CommunityAgent** | Captures community response and triages qualitative signals | Community moderation playbooks, sentiment datasets, escalation rules | Response latency, issue clustering quality, sentiment tracking accuracy | Surfaces emerging audience concerns earlier than manual comment review | AnalystAgent, SocialMediaStrategistAgent, CommsAgent | Confusing messaging, sentiment risks, recurring complaints | Social listening tools, moderation dashboards, clustering models | Reflexion from post-launch audience feedback |
| 89 | **TemplateDesignAgent** | Designs reusable and safe personalization templates | Variable-content design systems, dynamic layout rules, campaign template libraries | Merge-field robustness, layout stability, render survivability | Produces reusable templates with fewer breakages than manual design variants | PersonalizationEngineerAgent, UXAgent, CRMAgent | Fragile layouts, unsafe placeholder logic, merge collisions | Template engines, design systems, schema validators | ReAct on template schemas and render constraints |
| 90 | **UXAgent** | Reviews clarity and usability of personalized or interactive outputs | UX heuristics, accessibility criteria, usability testing patterns | Readability,
…



From `corpus/study/ui/production_scale_discovery.md` Copy: `sources/excerpts/production_scale_discovery.md`.


'''text
┌─────────────────────────────────────────────────────────────────────────────┐
│  DISCOVER                                              Search: [________]   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TABS: [Showcase Gallery] [Templates] [Community] [Scale Guide]             │
│                                                                             │
├─── SHOWCASE GALLERY (curated examples of what the system produces) ─────────┤
│                                                                             │
│  Filter: [All ▼] [Duration ▼] [Style ▼] [Industry ▼] [Budget Range ▼]      │
│  Sort:   [Trending] [Newest] [Most Liked] [Cheapest] [Highest Quality]      │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                                                                     │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐           │    │
│  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │           │    │
│  │  │          │  │          │  │          │  │          │           │    │
│  │  │ "Neon    │  │ "Product │  │ "5-Min   │  │ "Brand   │           │    │
│  │  │  Dreams" │  │  Launch" │  │  Doc"    │  │  Story"  │           │    │
│  │  │          │  │          │  │          │  │          │           │    │
│  │  │ 15s Hook │  │ 30s UGC  │  │ 5min Doc │  │ 90s Film │           │    │
│  │  │ ~$8      │  │ ~$15     │  │ ~$45     │  │ ~$35     │           │    │
│  │  │ Template A│  │ Template B│  │ Template I│  │ Template E│          │    │
│  │  │ ★★★★★    │  │ ★★★★☆    │  │ ★★★★★    │  │ ★★★★★    │           │    │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘           │    │
│  │                                                                     │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐           │    │
│  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │           │    │
│  │  │          │  │          │  │          │  │          │           │    │
│  │  │ "Fitness │  │ "AI      │  │ "Music   │  │ "Corp    │           │    │
│  │  │  Ad"     │  │  Avatar" │  │  Video"  │  │  Train"  │           │    │
│  │  │          │  │          │  │          │  │          │           │    │
│  │  │ 20s UGC  │  │ 3min Talk│  │ 4min MV  │  │ 12min LMS│           │    │
│  │  │ ~$12     │  │ ~$25     │  │ ~$60     │  │ ~$40     │           │    │
│  │  │ Template B│  │ Template H│  │ Template G│  │ Template F│          │    │
│  │  │ ★★★★☆    │  │ ★★★★★    │  │ ★★★★☆    │  │ ★★★★★    │           │    │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘           │    │
│  │                                                                     │    │
│  │  Showing 8 of 247 showcase items  [Load more...]                    │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  Click any card → Preview + "Use This as Starting Point"                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
'''

OR (community-inspired):
  Browse Community Gallery → See trending content →
  → "I want to make something like THIS" →
  → Click [Remix] → Fork their brief + adjust → Launch
'''

| Method | How It Works | User Effort |
|--------|-------------|-------------|
| **Template Carousel** | User browses visual cards with duration/cost/examples | Low — visual browsing |
| **Scale Guide** | Side-by-side comparison table of all production tiers | Low — read and pick |
| **Showcase Gallery** | Real produced examples with full metadata visible | Zero — just watch |
| **Smart Wizard** | User describes in English → AI recommends scale | Minimal — type a sentence |
| **Community Feed** | Browse what others have made → fork/remix | Zero — just browse |
| **Inspiration Board** | Save references → system infers style/scale from collection | Organic — save what you like |
| **From Showcase** | Click "Use This as Template" → exact settings pre-filled | One click |



From `corpus/study/ui/RETHINK_100_IMPROVEMENTS.md` Copy: `sources/excerpts/RETHINK_100_IMPROVEMENTS.md`.


| # | Improvement | Source | Impact |
|---|------------|--------|--------|
| 51 | Generative UI — agents create interface components | Generative UI 2026 | Major |
| 52 | Infinite canvas (node-based workflow editor) | TwitCanva | Major |
| 53 | Real-time multi-user collaboration | Enterprise need | Medium |
| 54 | AI co-pilot chat interface | Natural language control | Major |
| 55 | Version branches (fork at any gate) | Non-destructive experimentation | Major |
| 56 | Side-by-side comparison at every decision | Better review UX | Medium |
| 57 | Contextual help on hover | Onboarding | Minor |
| 58 | Production timeline replay (scrub history) | Debugging + learning | Medium |
| 59 | Agent reasoning explanation in plain English | Trust + transparency | Medium |
| 60 | Estimated impact preview before config change | Safer changes | Medium |
| 61 | Template marketplace (publish/sell) | Community + monetization | Medium |
| 62 | Progressive loading (partial results as agents work) | Perceived speed | Major |
| 63 | Comparison with human baseline | Value proposition | Medium |
| 64 | Cost prediction confidence intervals | Better expectations | Minor |
| 65 | Mobile monitoring + gate approvals | Convenience | Medium |
| 66 | Webhook/API integrations (CRM, calendar triggers) | Enterprise workflow | Medium |
| 67 | Batch mode (50 variants from 1 brief) | Performance marketing | Major |
| 68 | White-label mode | Agency deployment | Medium |
| 69 | Offline artifact download (all assets + metadata) | Interoperability | Minor |
| 70 | Auto-generated WCAG compliance report | Enterprise compliance | Minor |



Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


Provenance

- Master roster row va_id=88 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `[historical-path]
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): upstream-va-design.


<!-- self_contained_spec · video.community · va_id=88 -->

Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **CommunityAgent** (`video.community`, va_id=88, category `10-Sup`).

Responsibility focus
Captures community response and triages qualitative signals

Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: generative marketing content, ROAS optimization agents, multi-platform distribution AI, brand-safe generation
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI marketing for video, performance creative AI, social video agents
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: AI social video strategy, performance marketing with AI, brand systems for AI content

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

<!-- migration_capability_research · video.community · v1 · 2026-07-13 -->

```


## Prompts

### `prompts/primary.md`

# Prompt — `video.prompt.community.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: Reflexion, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **CommunityAgent (VA Domain Pack)** (`video.community`), a pack agent in the video domain swarm.

### Responsibility (owns)
Captures community response and triages qualitative signals

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
Reflexion from post-launch audience feedback

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Community moderation playbooks, sentiment datasets, escalation rules

## Developer

### Tools (allowlist intent)
Design tool surface: Social listening tools, moderation dashboards, clustering models
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: AnalystAgent, SocialMediaStrategistAgent, CommsAgent
- May comment on: Confusing messaging, sentiment risks, recurring complaints
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Response latency, issue clustering quality, sentiment tracking accuracy

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.community",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **CommunityAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.community",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.community`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
15, 21, 26, 30, 31, 37, 38, 50, 59, 63, 67, 72, 73, 74, 82, 83, 85, 87, 88, 92, 93, 94

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

### `prompts/video.prompt.community.v1.md`

# Prompt — `video.prompt.community.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: Reflexion, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **CommunityAgent (VA Domain Pack)** (`video.community`), a pack agent in the video domain swarm.

### Responsibility (owns)
Captures community response and triages qualitative signals

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
Reflexion from post-launch audience feedback

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Community moderation playbooks, sentiment datasets, escalation rules

## Developer

### Tools (allowlist intent)
Design tool surface: Social listening tools, moderation dashboards, clustering models
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: AnalystAgent, SocialMediaStrategistAgent, CommsAgent
- May comment on: Confusing messaging, sentiment risks, recurring complaints
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Response latency, issue clustering quality, sentiment tracking accuracy

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.community",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **CommunityAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.community",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.community`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
15, 21, 26, 30, 31, 37, 38, 50, 59, 63, 67, 72, 73, 74, 82, 83, 85, 87, 88, 92, 93, 94

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

Source rubric `video.rubric.community.v1.json` (baseline_safe; not a production pass).

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.community.v1",
  "agent_id": "video.community",
  "title": "L2 craft rubric for CommunityAgent",
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
          "name": "Response latency, issue clustering quality, sentiment tracking accuracy",
          "description": "Response latency, issue clustering quality, sentiment tracking accuracy",
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
      "surpass_signal_design": "Surfaces emerging audience concerns earlier than manual comment review",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Response latency, issue clustering quality, sentiment tracking accuracy",
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

### `rubrics/video.rubric.community.v1.json`

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.community.v1",
  "agent_id": "video.community",
  "title": "L2 craft rubric for CommunityAgent",
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
          "name": "Response latency, issue clustering quality, sentiment tracking accuracy",
          "description": "Response latency, issue clustering quality, sentiment tracking accuracy",
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
      "surpass_signal_design": "Surfaces emerging audience concerns earlier than manual comment review",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Response latency, issue clustering quality, sentiment tracking accuracy",
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

# Source acquisition runbook — `video.community`

## Purpose
Obtain or refresh knowledge distillation sources listed in `SOURCE_CATALOG.json`.

## Rules
1. **No secrets in git.** API keys only via environment / secret manager.
2. Prefer **licensed / consented / public domain** material.
3. If license unknown: store only short fair-use design excerpts under `excerpts/` and mark `license_class=unknown_review_required`.
4. Update `PROVENANCE.json` with URL, retrieved_at, hash, and license note.
5. Re-run offline golden eval after material changes.

## Design sources (from agents.md)
Community moderation playbooks, sentiment datasets, escalation rules

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
  "agent_id": "video.community",
  "plan_id": "video.community.distill.v1",
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
  "owner": "video.community",
  "cadence": "quarterly",
  "promotion_criteria": [
    "source license approved or fixture-only",
    "excerpt hash recorded in PROVENANCE",
    "golden eval still passes L1"
  ],
  "memory_namespace": "pack.video.video.community",
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

### `sources/excerpts/human_video_production_workflow.md`

### Video Types by Duration

| Duration              | Video Types (Sample Productions)                                      | Best For                                      | Difficulty          | Monetization Potential | Notes / Recommendations |
|-----------------------|--------------------------------------------------|-----------------------------------------------|---------------------|------------------------|-------------------------|
| **5 – 15 seconds**    | Hook clips, Meme videos & funny skits, Trending sound / reaction videos, Quick transitions, Text-on-screen quotes, Looping backgrounds, Aesthetic vibe loops, Style-transfer clips, Virtual greeting cards, Carousel-to-video snippets, Motion-art teasers | TikTok, Reels, YouTube Shorts                 | Very Easy           | High                   | Easiest to generate. Best starting point for your app. |
| **15 – 30 seconds**   | Short skits, Product teasers, Aesthetic vibe videos, Reaction clips, Lyric snippets, UGC-style ads, Before & After transformations, E-comm rotating product shots, Personalized birthday clips, Motivation videos, AI-avatar intros, Surreal visuals, AI B-roll | Social media, Ads, Music clips                | Very Easy           | High                   | Most popular length for viral content right now. |
| **30 – 60 seconds**   | Short ads, Explainer hooks, Talking-head intros, Before/After videos, Mini stories, Product demos, Brand-story micro-ads, AI-avatar testimonials, Concept trailers, Music / lyric videos, "Day in the life" clips, FAQ snippets, LinkedIn posts, Moving infographics, Kids story videos | Reels, Shorts, Ad campaigns                   | Easy                | High                   | Sweet spot for marketing videos. |
| **1 – 3 minutes**     | Explainer videos, Product demos, Mini docs, Storytelling clips, Music videos, Animated explainers, Whiteboard animations, Course intros, Pitch decks, Meeting recaps, Real-estate tours, AI presenter segments, News-style updates, Language clips, Cinematic micro-movies, Bedtime stories | YouTube, Education, Marketing                 | Medium              | Very High              | Can be generated as one clip or stitched. |
| **3 – 10 minutes**    | Full explainers, Short films, Animated stories, Training videos, Virtual tours, Corporate explainers, Science/history sims, Multi-scene AI stories, Bedtime episodes, Full-song music videos, Extended trailers, Avatar lessons, KB videos, Style-transfer art | YouTube, Education, Corporate training        | Medium              | Very High              | Best generated scene-by-scene then stitched. |
| **10 – 30 minutes**   | Long-form explainers, Short courses, Documentaries, Series episodes, Webinar clips, Animated edu series, Training modules, Cinematic real-estate, AI news bulletins, Full language lessons, Multi-scene AI films, Pitch deep dives | YouTube, Online courses, Corporate            | Hard                | High                   | Requires strong scene consistency + chapter generation. |
| **30 – 60 minutes**   | Short films, Extended stories, Long edu content, Virtual events, Doc episodes, Multi-chapter lessons, Town-halls, Animated story collections, Cinematic showcases, Long AI-presenter shows | YouTube long-form, Films, Education           | Very Hard           | High                   | Generate in parts. Needs strong editing tools. |
| **1 – 2 hours**       | Feature-length videos, Full courses, Long docs, Movies, Multi-act AI films, Training programs, Virtual conferences, Animated features, Studio pre-vis | YouTube long-form, Film pre-vis, Courses      | Extremely Hard      | Medium–High            | Best as segmented generation + heavy post-production. |

---

### Crew Reference Legend

Standard professional roles referenced below (per IMDb-style production credits, scaled for AI-assisted workflows):

- **Above-the-line**: Director, Producer, Showrunner, Screenwriter / Scriptwriter, Lead Cast / Talent
- **Camera & lighting**: Cinematographer (DoP), Camera Operator, Gaffer, Grip, Drone Pilot
- **Sound**: Sound Designer, Boom Operator, Production Mixer, Foley Artist, Composer, Voice-Over Artist
- **Art & design**: Production Designer, Art Director, Set Decorator, Costume Designer, Makeup / Hair Artist, Storyboard Artist, Concept Artist
- **Post-production**: Editor, Colorist, VFX Supervisor, Motion Graphics Designer, 2D / 3D Animator, Compositor, Sound Editor, Re-recording Mixer
- **AI-era specialists**: Prompt Engineer, AI Video Generator Operator, AI Voice / Lip-Sync Specialist, AI Avatar Designer, Model Fine-Tuner, AI QA / Consistency Reviewer
- **Distribution & strategy**: Producer / EP, Social Media Strategist, Copywriter, SEO/ASO Specialist, Community Manager, Localization / Subtitle Editor, Legal / Clearance, Brand / Marketing Manager

> Crews below list the **minimum viable crew** to ship the production professionally. A solo creator can often cover several roles in short-form work; long-form productions require dedicated specialists.

---

### Sample Productions by Category

#### 1. Social Media & Viral Content *(Highest demand right now)*

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

#### 2. Marketing & Advertising Videos

| # | Sample Production | Typical Duration | Best Channel | Crew / Roles Required |
|---|-------------------|------------------|--------------|----------------------|
| 1 | Product showcase / demo videos | 15–60s | Social ads, e-comm | Director, DoP, Product Stylist, Editor, Motion GFX, Copywriter, Brand Manager |
| 2 | Brand story / explainer ads | 30–90s | YouTube, web | Creative Director, Scriptwriter, Director, DoP, Editor, Composer, VO Artist |
| 3 | UGC-style ads | 15–45s | TikTok, Meta ads | UGC Creator, Brief Writer, Editor, Performance-Ads Strategist, Legal Clearance |
| 4 | Before & After transformations | 10–30s | Reels, TikTok | Director, DoP, Talent, Editor, Colorist, Compliance Reviewer |
| 5 | AI-avatar testimonial videos | 30–60s | LinkedIn, landing pages | Scriptwriter, AI Avatar Designer, Voice Cloner / VO Artist, Lip-Sync Specialist, Editor |

…(clipped 57930 characters from `human_video_production_workflow.md`)

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

### `sources/excerpts/production_scale_discovery.md`

# Production Scale Discovery — Galleries, Showcases & Smart Selection

> How the system helps users understand what they want to build,
> browse real examples, and select the right production scale
> BEFORE committing budget or launching agents.

---

## The Problem

```text
CURRENT FLOW (confusing for new users):
  Create Project → "Pick template A-J" → "Set duration"

USER THINKS:
  "I don't know what Template E means"
  "Is 30 seconds enough for my idea?"
  "What does a $50 production look like vs a $200 one?"
  "Can I see examples of what this system actually makes?"

WHAT THEY NEED:
  Browse → Inspire → Understand scale → THEN configure
```

---

## Solution: Discovery Hub (new top-level section)

```text
UPDATED NAVIGATION:

Side Nav:
  ○ Dashboard
  ○ Discover    ← NEW (Galleries + Showcases + Templates)
  ○ Projects
  ○ Productions
  ○ Agents
  ○ Settings
```


---

## Page: Discovery Hub

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  DISCOVER                                              Search: [________]   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TABS: [Showcase Gallery] [Templates] [Community] [Scale Guide]             │
│                                                                             │
├─── SHOWCASE GALLERY (curated examples of what the system produces) ─────────┤
│                                                                             │
│  Filter: [All ▼] [Duration ▼] [Style ▼] [Industry ▼] [Budget Range ▼]      │
│  Sort:   [Trending] [Newest] [Most Liked] [Cheapest] [Highest Quality]      │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                                                                     │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐           │    │
│  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │           │    │
│  │  │          │  │          │  │          │  │          │           │    │
│  │  │ "Neon    │  │ "Product │  │ "5-Min   │  │ "Brand   │           │    │
│  │  │  Dreams" │  │  Launch" │  │  Doc"    │  │  Story"  │           │    │
│  │  │          │  │          │  │          │  │          │           │    │
│  │  │ 15s Hook │  │ 30s UGC  │  │ 5min Doc │  │ 90s Film │           │    │
│  │  │ ~$8      │  │ ~$15     │  │ ~$45     │  │ ~$35     │           │    │
│  │  │ Template A│  │ Template B│  │ Template I│  │ Template E│          │    │
│  │  │ ★★★★★    │  │ ★★★★☆    │  │ ★★★★★    │  │ ★★★★★    │           │    │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘           │    │
│  │                                                                     │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐           │    │
│  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │           │    │
│  │  │          │  │          │  │          │  │          │           │    │
│  │  │ "Fitness │  │ "AI      │  │ "Music   │  │ "Corp    │           │    │
│  │  │  Ad"     │  │  Avatar" │  │  Video"  │  │  Train"  │           │    │
│  │  │          │  │          │  │          │  │          │           │    │
│  │  │ 20s UGC  │  │ 3min Talk│  │ 4min MV  │  │ 12min LMS│           │    │
│  │  │ ~$12     │  │ ~$25     │  │ ~$60     │  │ ~$40     │           │    │
│  │  │ Template B│  │ Template H│  │ Template G│  │ Template F│          │    │
│  │  │ ★★★★☆    │  │ ★★★★★    │  │ ★★★★☆    │  │ ★★★★★    │           │    │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘           │    │
│  │                                                                     │    │
│  │  Showing 8 of 247 showcase items  [Load more...]                    │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  Click any card → Preview + "Use This as Starting Point"                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```



---

## Showcase Card Detail (when user clicks a gallery item)

```text
┌──────────────────────────────────────────────────────────────────┐
│  SHOWCASE: "Neon Dreams"                                  [×]    │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │                                                          │    │
│  │              ▶ VIDEO PLAYER (15 seconds)                  │    │
│  │                                                          │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─── PRODUCTION DETAILS ────────────────────────────────────┐   │
│  │                                                           │   │
│  │  Template: A — Viral Hook                                 │   │
│  │  Duration: 15 seconds                                     │   │
│  │  Aspect: 9:16 (TikTok/Reels)                             │   │
│  │  Style: Cyberpunk, neon, high-energy                      │   │
│  │  Genre: Lifestyle/Fashion                                 │   │
│  │                                                           │   │
│  │  ┌─── SCALE BREAKDOWN ──────────────────────────────┐     │   │
│  │  │  Agents used: 12                                 │     │   │
│  │  │  Shots generated: 4                              │     │   │
│  │  │  Total cost: $8.20                               │     │   │
│  │  │  Production time: 2 minutes 14 seconds           │     │   │
│  │  │  Model: Veo 3.1 (primary), Kling 3.0 (B-roll)   │     │   │
│  │  │  Voice: None (music-only)                        │     │   │
│  │  │  Music: Udio-generated (electronic, 130bpm)      │     │   │
│  │  └──────────────────────────────────────────────────┘     │   │
│  │                                                           │   │
│  │  ┌─── AGENTS INVOLVED ─────────────────────────────┐      │   │
│  │  │  DirectorAgent · PromptEngineerAgent ·           │      │   │
│  │  │  EditorAgent · ComposerAgent · AIQAAgent ·       │      │   │
│  │  │  RetentionOptimizerAgent · TrendIntelAgent ·     │      │   │
│  │  │  CopywriterAgent · SocialStrategistAgent ·       │      │   │
│  │  │  ColoristAgent · SoundMixerAgent · MotionGfx     │      │   │
│  │  └──────────────────────────────────────────────────┘      │   │
│  │                                                           │   │
│  │  ┌─── BRIEF USED ──────────────────────────────────┐      │   │
│  │  │  "15-second hook for fashion brand. Neon city    │      │   │
│  │  │   streets at night, model walking, beat-synced   │      │   │
│  │  │   cuts, trending audio style. Target: Gen Z."    │      │   │
│  │  └──────────────────────────────────────────────────┘      │   │
│  │                                                           │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌─── ACTIONS ───────────────────────────────────────────────┐   │
│  │                                                           │   │
│  │  [★ Use This as Template]  → Creates draft with this      │   │
│  │                               brief pre-filled            │   │
│  │                                                           │   │
│  │  [📋 Copy Brief]  → Copy the brief text to clipboard      │   │
│  │                                                           │   │
│  │  [🔀 Remix]  → Start from this but modify                 │   │
│  │

…(clipped 19087 characters from `production_scale_discovery.md`)

### `sources/excerpts/project_starter_0.3.md`

# project_starter

**Project name:** `project_starter`  
**Purpose:** Build an executable starter repository that downloads, audits, curates, and synchronizes AI coding-agent configuration sources across Claude Code, Cursor, Codex, Gemini CLI, OpenCode, Grok Build, GitHub Copilot, and related agent harnesses.  
**Current spec version:** `1.0.0-actionable-bootstrap`  
**Last updated:** 2026-06-09  

---

## How to Use This Boilerplate With a Coding Agent

This repository is a boilerplate specification.

A human may ask a coding agent to create a new project from this file by using a prompt like:

```text
Create a new project named <PROJECT_NAME> based on <PATH_TO_PROJECT_STARTER_MD>.

Use project_starter.md as the source-of-truth implementation contract.

Create the new project at:

<OUTPUT_DIRECTORY>/<PROJECT_NAME>

The project purpose is:

<PROJECT_PURPOSE>

The primary stack is:

<STACK>

You must:
1. Read project_starter.md fully.
2. Create the new project directory.
3. Create all directories and files required by project_starter.md.
4. Replace boilerplate metadata with the new project name and purpose.
5. Copy project_starter.md into the new project.
6. Create package.json.
7. Create source manifests.
8. Create executable scripts.
9. Create rule files.
10. Create docs.
11. Download all enabled upstream GitHub repositories into external/sources/.
12. Generate sources/source-lock.json.
13. Generate docs/source-audit.md.
14. Run bootstrap validation.
15. Update status.md.
16. Report final pass/fail status.

Do not merely summarize the instructions.
Do not only write Markdown.
Create a working executable project.

If network or shell access is unavailable, create all project files anyway and mark source download as blocked in status.md.

## 0. Critical Instruction to Coding Agents

This file is **not only documentation**.

When a coding agent receives this file and is asked to implement it, the agent **MUST** create a real executable project.

The agent **MUST NOT** stop after writing Markdown.

The agent **MUST**:

1. Create the `project_starter/` repository structure.
2. Create `package.json`.
3. Create `sources/manifest.json`.
4. Create `sources/docs-manifest.json`.
5. Create `scripts/project-starter.mjs`.
6. Create `scripts/source-download.mjs`.
7. Create `scripts/source-audit.mjs`.
8. Create `scripts/doctor.mjs`.
9. Create `scripts/sync.mjs`.
10. Create `scripts/security.mjs`.
11. Download every enabled GitHub repository listed in `sources/manifest.json`.
12. Save downloaded repos under `external/sources/`.
13. Save download metadata to `sources/source-lock.json`.
14. Generate `docs/source-audit.md`.
15. Run the bootstrap validation commands.
16. Report success or exact blockers.

If network access or shell execution is unavailable, the agent **MUST** say:

```text
BLOCKED: cannot download sources because network/shell execution is unavailable.
```

and still create all scripts and manifests so the human can run:

```bash
npm run bootstrap
```

later.

---

## 1. Non-Negotiable Outcome

After implementation, this command:

```bash
npm run bootstrap
```

**MUST** perform this flow:

```text
doctor
→ create required directories
→ validate sources/manifest.json
→ clone/update all enabled GitHub sources
→ write sources/source-lock.json
→ generate docs/source-audit.md
→ run security smoke checks
→ run sync dry-run
→ run tests
```

The project is **not complete** unless the source repositories are actually downloaded into:

```text
external/sources/
```

---

## 2. Required Repository Structure

The coding agent **MUST** create this structure:

```text
project_starter/
├── project_starter.md
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── package.json
├── task.md
├── status.md
├── .gitignore
├── .editorconfig
├── sources/
│   ├── manifest.json
│   ├── docs-manifest.json
│   ├── source-lock.json
│   └── README.md
├── external/
│   ├── .gitignore
│   └── sources/
├── scripts/
│   ├── project-starter.mjs
│   ├── source-download.mjs
│   ├── source-audit.mjs
│   ├── doctor.mjs
│   ├── sync.mjs
│   ├── security.mjs
│   ├── review.mjs
│   ├── adapters/
│   │   ├── claude.mjs
│   │   ├── cursor.mjs
│   │   ├── codex.mjs
│   │   ├── gemini.mjs
│   │   ├── opencode.mjs
│   │   ├── grok-build.mjs
│   │   └── copilot.mjs
│   └── lib/
│       ├── git.mjs
│       ├── fs-safe.mjs
│       ├── manifest.mjs
│       └── report.mjs
├── rules/
│   ├── manifest.json
│   ├── 00-constitution.md
│   ├── 10-karpathy.md
│   ├── 20-sdd.md
│   ├── 30-security.md
│   ├── 40-testing.md
│   ├── 50-token-efficiency.md
│   └── 60-human-approval.md
├── skills/
│   ├── manifest.json
│   ├── planning/
│   ├── implementation/
│   ├── testing/
│   ├── review/
│   ├── security/
│   ├── memory/
│   └── lifecycle/
├── hooks/
│   ├── manifest.json
│   └── scripts/
├── mcp-configs/
│   ├── manifest.json
│   ├── minimal.json
│   └── optional/
├── memory/
│   ├── README.md
│   ├── project.md
│   ├── handoff.md
│   └── reflections/
├── reviews/
├── suggestions/
│   ├── pending/
│   ├── approved/
│   ├── rejected/
│   └── audit-log.md
├── docs/
│   ├── installation.md
│   ├── usage.md
│   ├── architecture.md
│   ├── source-audit.md
│   ├── security.md
│   ├── sync.md
│   └── troubleshooting.md
├── examples/
│   ├── sdd-feature-workflow/
│   ├── self-review-workflow/
│   ├── skill-suggestion-workflow/
│   └── cross-agent-sync-workflow/
└── tests/
    ├── fixtures/
    ├── source-download.test.mjs
    ├── source-audit.test.mjs
    ├── sync.test.mjs
    ├── manifest.test.mjs
    └── adapters.test.mjs
```

---

## 3. Required `package.json`

The coding agent **MUST** create this `package.json` or an equivalent superset:

```json
{
  "name": "project_starter",
  "version": "1.0.0-actionable-bootstrap",
  "private": true,
  "type": "module",
  "description": "Executable starter repo for downloading, auditing, curating, and syncing AI coding-agent harness sources.",
  "scripts": {
    "bootstrap": "node scripts/project-starter.mjs bootstrap",
    "init": "node scripts/project-starter.mjs init",
    "doctor": "node scripts/doctor.mjs",
    "sources:download": "node scripts/source-download.mjs",
    "sources:update": "node scripts/source-download.mjs --update",
    "sources:check": "node scripts/source-download.mjs --check",
    "sources:audit": "node scripts/source-audit.mjs",
    "sync": "node scripts/sync.mjs",
    "sync:check": "node scripts/sync.mjs --check",
    "security": "node scripts/security.mjs",
    "review": "node scripts/review.mjs",
    "test": "node --test tests/*.test.mjs",
    "format": "node scripts/project-starter.mjs format"
  },
  "engines": {
    "node": ">=20.0.0"
  }
}
```

No package dependency is required for the first implementation. Use Node built-ins only.

---

## 4. Mandatory GitHub Source Download Manifest

The coding agent **MUST** create this exact file:

```text
sources/manifest.json
```

The agent **MUST** download every source with:

```json
"enabled": true
```

The agent **MUST NOT** silently skip any enabled source.

If a required source fails, the command must exit non-zero.

Create `sources/manifest.json` with this content:

```json
{
  "schema_version": "1.0",
  "generated_from": "project_starter.md",
  "default_profile": "all",
  "download_root": "external/sources",
  "sources": [
    {
      "id": "ecc",
      "name": "ECC / Everything Claude Code",
      "url": "https://github.com/affaan-m/ECC.git",
      "target": "external/sources/ecc",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "core",
      "quarantine": false,
      "import_policy": "curated-only",
      "purpose": "Primary cross-agent harness source: skills, agents, commands, hooks, rules, MCP conventions, security scanner references."
    },
    {
      "id": "anthropic-claude-code",
      "name": "Anthropic Claude Code",
      "url": "https://github.com/anthropics/claude-code.git",
      "target": "external/sources/anthropic-claude-code",

…(clipped 29877 characters from `project_starter_0.3.md`)

### `sources/excerpts/project_starter_0.5.md`

# project_starter

**Project name:** `project_starter`  
**Purpose:** Build an executable starter repository that downloads, audits, curates, and synchronizes AI coding-agent configuration sources across Claude Code, Cursor, Codex, Gemini CLI, OpenCode, Grok Build, GitHub Copilot, and related agent harnesses.  
**Current spec version:** `1.1.0-merged-bootstrap`  
**Last updated:** 2026-06-09  

---

## How to Use This Boilerplate With a Coding Agent

This repository is a boilerplate specification.

A human may ask a coding agent to create a new project from this file by using a prompt like:

```text
Create a new project named <PROJECT_NAME> based on <PATH_TO_PROJECT_STARTER_MD>.

Use project_starter.md as the source-of-truth implementation contract.

Create the new project at:

<OUTPUT_PATH>

The project purpose is:

<PROJECT_PURPOSE>

The primary stack is:

<STACK>

You must:
1. Read project_starter.md fully.
2. Create the new project directory.
3. Create all directories and files required by project_starter.md.
4. Replace boilerplate metadata with the new project name and purpose.
5. Copy project_starter.md into the new project.
6. Create package.json.
7. Create source manifests.
8. Create executable scripts.
9. Create rule files.
10. Create docs.
11. Download all enabled upstream GitHub repositories into external/sources/.
12. Generate sources/source-lock.json.
13. Generate docs/source-audit.md.
14. Run bootstrap validation.
15. Update status.md.
16. Report final pass/fail status.

Do not merely summarize the instructions.
Do not only write Markdown.
Create a working executable project.

If network or shell access is unavailable, create all project files anyway and mark source download as blocked in status.md.

## Project Modes

This specification supports two valid implementation modes:

1. **Self-bootstrap mode** — implement the starter repository itself in the current repository.
2. **Create-new-project mode** — generate a new downstream project from this specification into a target directory.

Example self-bootstrap prompt:

```text
Implement project_starter.md in the current repository.

Use project_starter.md as the complete implementation contract.

Create all required files, directories, manifests, scripts, docs, tests, and agent configuration files.

Then run:

npm run bootstrap
```

Example create-new-project prompt:

```text
Create a new project named <PROJECT_NAME> based on <PATH_TO_PROJECT_STARTER_MD>.

Create it at:

<OUTPUT_PATH>

Use project_starter.md as the complete implementation contract.

Create a working executable project, not just Markdown.

Download all enabled sources unless told not to.

Then run:

npm run bootstrap
```

## Required Input Variables

When generating a downstream project, a coding agent may receive these variables:

| Variable | Description | Default |
|---|---|---|
| `PROJECT_NAME` | Name of the generated project | `project_starter_generated` |
| `OUTPUT_PATH` | Target directory for the generated project | `./project_starter_generated` |
| `PROJECT_PURPOSE` | Short description of the generated project | `AI coding-agent starter repository` |
| `STACK` | Primary technology stack | `Node.js 20+, plain JavaScript, no runtime dependencies for bootstrap scripts` |
| `DOWNLOAD_SOURCES` | Whether enabled upstream sources should be downloaded | `true` |
| `AGENT_SUPPORT` | Supported coding agents | `claude,cursor,codex,gemini,opencode,copilot,grok-build` |
| `PACKAGE_MANAGER` | Primary JavaScript package manager | `npm` |
| `LICENSE` | License for the generated project | `MIT` |

If a required value is missing, the coding agent should use the default.

## Existing Output Directory Rule

If `OUTPUT_PATH` already exists and is non-empty, the coding agent must stop and ask for permission before overwriting or updating it.

Allowed exception:

- If the user explicitly says to overwrite or update the existing directory, the agent may proceed, but should preserve important user-created files when possible.

## 0. Critical Instruction to Coding Agents

This file is **not only documentation**.

When a coding agent receives this file and is asked to implement it, the agent **MUST** create a real executable project.

The agent **MUST NOT** stop after writing Markdown.

The agent **MUST**:

1. Create the `project_starter/` repository structure.
2. Create `package.json`.
3. Create `sources/manifest.json`.
4. Create `sources/docs-manifest.json`.
5. Create `scripts/project-starter.mjs`.
6. Create `scripts/create-project.mjs`.
7. Create `scripts/source-download.mjs`.
8. Create `scripts/source-audit.mjs`.
9. Create `scripts/doctor.mjs`.
10. Create `scripts/sync.mjs`.
11. Create `scripts/security.mjs`.
12. Download every enabled GitHub repository listed in `sources/manifest.json`.
13. Save downloaded repos under `external/sources/`.
14. Save download metadata to `sources/source-lock.json`.
15. Generate `docs/source-audit.md`.
16. Support both self-bootstrap and create-new-project workflows.
17. Run the bootstrap validation commands.
18. Report success or exact blockers.

If network access or shell execution is unavailable, the agent **MUST** say:

```text
BLOCKED: cannot download sources because network/shell execution is unavailable.
```

and still create all scripts and manifests so the human can run:

```bash
npm run bootstrap
```

later.

---

## 1. Non-Negotiable Outcome

After implementation, this command:

```bash
npm run bootstrap
```

**MUST** perform this flow:

```text
doctor
→ create required directories
→ validate sources/manifest.json
→ clone/update all enabled GitHub sources
→ write sources/source-lock.json
→ generate docs/source-audit.md
→ run security smoke checks
→ run sync dry-run
→ run tests
```

The project is **not complete** unless the source repositories are actually downloaded into:

```text
external/sources/
```

---

## 2. Required Repository Structure

The coding agent **MUST** create this structure:

```text
project_starter/
├── project_starter.md
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── package.json
├── task.md
├── status.md
├── .gitignore
├── .editorconfig
├── sources/
│   ├── manifest.json
│   ├── docs-manifest.json
│   ├── source-lock.json
│   └── README.md
├── external/
│   ├── .gitignore
│   └── sources/
├── scripts/
│   ├── project-starter.mjs
│   ├── create-project.mjs
│   ├── source-download.mjs
│   ├── source-audit.mjs
│   ├── doctor.mjs
│   ├── sync.mjs
│   ├── security.mjs
│   ├── review.mjs
│   ├── adapters/
│   │   ├── claude.mjs
│   │   ├── cursor.mjs
│   │   ├── codex.mjs
│   │   ├── gemini.mjs
│   │   ├── opencode.mjs
│   │   ├── grok-build.mjs
│   │   └── copilot.mjs
│   └── lib/
│       ├── git.mjs
│       ├── fs-safe.mjs
│       ├── manifest.mjs
│       └── report.mjs
├── rules/
│   ├── manifest.json
│   ├── 00-constitution.md
│   ├── 10-karpathy.md
│   ├── 20-sdd.md
│   ├── 30-security.md
│   ├── 40-testing.md
│   ├── 50-token-efficiency.md
│   └── 60-human-approval.md
├── skills/
│   ├── manifest.json
│   ├── planning/
│   ├── implementation/
│   ├── testing/
│   ├── review/
│   ├── security/
│   ├── memory/
│   └── lifecycle/
├── hooks/
│   ├── manifest.json
│   └── scripts/
├── mcp-configs/
│   ├── manifest.json
│   ├── minimal.json
│   └── optional/
├── memory/
│   ├── README.md
│   ├── project.md
│   ├── handoff.md
│   └── reflections/
├── reviews/
├── suggestions/
│   ├── pending/
│   ├── approved/
│   ├── rejected/
│   └── audit-log.md
├── docs/
│   ├── installation.md
│   ├── usage.md
│   ├── agents.md
│   ├── architecture.md
│   ├── source-audit.md
│   ├── security.md
│   ├── sync.md
│   ├── troubleshooting.md
│   └── changelog.md
├── examples/
│   ├── sdd-feature-workflow/
│   ├── self-review-workflow/
│   ├── skill-suggestion-workflow/
│   └── cross-agent-sync-workflow/
└── tests/
    ├── fixtures/
    ├── source-download.test.mjs
    ├── source-audit.test.mjs
    ├── sync.test.mjs
    ├── manifest.test.mjs
    └── adapters.test.mjs
```

---

## 3.

…(clipped 35039 characters from `project_starter_0.5.md`)

### `sources/excerpts/RETHINK_100_IMPROVEMENTS.md`

# 100-Point Deep Rethink — Research-Backed Improvements

> Based on arXiv papers (FilmAgent, MovieAgent, OmniAgent, AnimAgents, Sima 1.0), 2026 model landscape (Seedance 2.0, Wan 2.6, Vidu Q2/Q3, Grok Imagine Video, Hailuo 2.3), LangGraph 1.0 production patterns, and Generative UI trends. May 2026.

---

## Research Sources

| Source | Key Insight | Link |
|--------|------------|------|
| FilmAgent (2025) | Multi-agent film automation with iterative feedback loops that verify scripts and reduce hallucinations | [arXiv:2501.12909](https://arxiv.org/abs/2501.12909) |
| MovieAgent (2025) | Hierarchical CoT planning with character bank achieves SOTA script faithfulness and character consistency | [arXiv:2503.07314](https://arxiv.org/abs/2503.07314) |
| OmniAgent | Hierarchical graph-based multi-agent for long video with film-production-inspired architecture | [arXiv:2510.22431](https://arxiv.org/html/2510.22431v1) |
| AnimAgents (2025) | Human-multi-agent collaboration with dedicated boards per pre-production stage | [arXiv:2511.17906](https://arxiv.org/abs/2511.17906) |
| Sima 1.0 (2025) | 11-step pipeline distributed across hybrid workforce for documentary video production | [arXiv:2604.07721](https://arxiv.org/html/2604.07721) |
| Seedance 2.0 (Apr 2026) | 9 images + 3 videos + 3 audio simultaneous input; native audio-visual synchronization | [ByteDance](https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0) |
| Wan 2.6 (2026) | IP-anchored character consistency; multi-shot storytelling coherence | [Comparison](https://wanvideogenerator.com/blog/seedance-2-vs-wan-2-6) |
| Veo 3.1 (2026) | 4K + reference images for character/object direction; configurable aspect ratios | [Google AI](https://ai.google.dev/gemini-api/docs/video) |
| Kling 2.6/3.0 | Physics-accurate motion; motion-control via reference video | [fal.ai](https://fal.ai/models/fal-ai/kling-video) |
| Grok Imagine Video (xAI) | New entrant with strong image-to-video capability | [wavespeed.ai](https://wavespeed.ai/blog/posts/grok-imagine-video-vs-sora-2-veo-3-seedance-wan-vidu-comparison-2026/) |
| LangGraph 1.0 Production | Node caching, deferred nodes, pre/post hooks, consensus mechanisms | [LangChain](https://www.langchain.com/blog/building-langgraph) |
| Agent Architecture 2026 | Isolate orchestration from execution; event-driven avoids cascading failures | [markaicode](https://markaicode.com/architecture/agent-architecture-best-practices-2026/) |
| Supervisor vs Swarm | Supervisor more accurate (routing is its only job); Swarm faster (skips intermediary) | [focused.io](https://focused.io/lab/multi-agent-orchestration-in-langgraph-supervisor-vs-swarm-tradeoffs-and-architecture) |
| Generative UI 2026 | AI agents create rich interactive interfaces dynamically | [Medium](https://medium.com/@akshaychame2/the-complete-guide-to-generative-ui-frameworks-in-2026-fde71c4fa8cc) |
| 6-Model Comparison 2026 | Pick by goal: conversions, realism, camera control, storytelling, IP, or cost | [opencreator.io](https://opencreator.io/blog/ai-video-models-comparison-2026) |

---

## Top 20 Critical Improvements (P0 + P1)

### Models to Add (agents.md Tool Access update needed)

1. **Seedance 2.0** — 9 images + 3 videos + 3 audio clips simultaneous input; first-and-last-frame control; native multi-camera storytelling
2. **Wan 2.6** — IP-anchored character consistency; strongest for multi-shot narrative coherence
3. **Vidu Q2/Q3** — Temporal consistency specialist; competitive I2V
4. **Grok Imagine Video** (xAI) — New entrant; strong image-to-video
5. **Hailuo 2.3** (MiniMax) — Fast budget-tier generation

### Architecture (backend docs update needed)

6. **Supervisor + Swarm hybrid** — Use Supervisor pattern for creative decisions (accuracy matters), Swarm for parallel QA (speed matters)
7. **Node caching** (LangGraph 1.0) — Cache identical agent outputs; 30-50% cost reduction
8. **Circuit breaker per API** — Graceful degradation when Veo/Sora/Kling APIs fail
9. **Isolate orchestration from execution** — Separate processes prevent cascading failures
10. **Model deprecation handling** — Sora 2 discontinuing Sept 2026; need graceful migration

### Workflow (from FilmAgent/MovieAgent research)

11. **Character Bank** — Persistent character definitions (face ref, voice, wardrobe) shared across all shots
12. **Iterative script verification** — Agents verify intermediate scripts before proceeding (reduces hallucination)
13. **Hierarchical CoT planning** — Better task decomposition for complex stories
14. **Shot-adjacency awareness** — Each agent considers previous AND next shot when generating
15. **Reference frame bank** — Approved frames from early shots guide later generation (consistency)
16. **First-and-last-frame generation** — Seedance 2.0 feature; precise scene control
17. **Multi-model ensemble** — Generate same shot on 2 models, CLIP-pick best

### UI/UX (from Generative UI research)

18. **Progressive results** — Show partial outputs as agents work (shot 1 appears before shot 5 done)
19. **Regenerate specific segment** — Keep shots 1-4, regenerate only shot 5
20. **AI co-pilot chat** — Natural language interface to trigger any action: "extend shot 3 by 2 seconds"

---

## Full 100 Improvements (by category)

### A. Model Landscape (1-15)
### B. Architecture (16-30)
### C. Research-Backed Workflows (31-50)
### D. UI/UX (51-70)
### E. New Capabilities (71-85)
### F. Quality & Evaluation (86-95)
### G. Business & Scaling (96-100)

(See detailed breakdown below)

---

## A. Model Landscape Updates (1-15)

| # | Model/Feature | Status | Impact | Action |
|---|--------------|--------|--------|--------|
| 1 | Seedance 2.0 (ByteDance) | Live Apr 2026 | Major | Add to agents.md + Router + Tool Section |
| 2 | Wan 2.6 (Alibaba) | Live 2026 | Major | Add — best for character consistency |
| 3 | Vidu Q2/Q3 | Live 2026 | Medium | Add — temporal consistency specialist |
| 4 | Grok Imagine Video (xAI) | Live 2026 | Medium | Add — competitive I2V |
| 5 | Hailuo 2.3 (MiniMax) | Live 2026 | Medium | Add — budget-tier speed option |
| 6 | Kling 2.6 variant awareness | Updated | Minor | Update model card |
| 7 | Seedance 1.5 Pro multi-camera | Live 2025 | Major | Add — native scene cuts |
| 8 | Flux 1.1 Pro Ultra | Live 2026 | Medium | Add for image gen |
| 9 | SD 3.5 self-hosted | Live | Medium | Add for cost reduction |
| 10 | Model strengths matrix in RouterAgent | New | Major | Implement in routing logic |
| 11 | Multi-model ensemble generation | New | Major | Optional per production |
| 12 | First-and-last-frame control | Seedance 2.0 | Major | Integrate into DirectorAgent |
| 13 | Motion transfer from reference | Kling + Seedance | Medium | ChoreographyAgent integration |
| 14 | Native audio generation awareness | Veo 3.1, Seedance | Medium | Skip audio agents for simple scenes |
| 15 | Model deprecation handling | Critical | Critical | Graceful migration system |

## B. Architecture Improvements (16-30)

| # | Improvement | Source | Impact |
|---|------------|--------|--------|
| 16 | Supervisor + Swarm hybrid | focused.io research | Major |
| 17 | Node caching (LangGraph 1.0) | langchain.com blog | Major |
| 18 | Deferred nodes for map-reduce | LangGraph 1.0 | Medium |
| 19 | Pre/post hooks on every node | LangGraph 1.0 | Medium |
| 20 | Consensus mechanisms beyond JudgeAgent | LangGraph patterns | Medium |
| 21 | Isolate orchestration from execution | markaicode.com | Critical |
| 22 | Speculative execution with rollback | Production patterns | Medium |
| 23 | Checkpoint compression for long productions | Scale optimization | Medium |
| 24 | Agent pooling with warm-start | Latency optimization | Medium |
| 25 | Priority queues with starvation prevention | Fairness | Medium |
| 26 | Circuit breaker per external API | Reliability | Critical |
| 27 | Event replay with time-travel debugging | Observability | Medium |
| 28 | Canary deployments for agent configs | Safety | Medium |
| 29 | Shadow mode for

…(clipped 6156 characters from `RETHINK_100_IMPROVEMENTS.md`)

### `sources/excerpts/video_generation_techology_should_learn_now.md`

**Here are 50 of the hottest and most important advanced multimodal AI video generation models to learn right now (as of April 2026).** These are prioritized by leaderboards (Elo/arena scores), real-world adoption, multimodal capabilities (text + image + video + audio references), motion realism, native audio, and production use.

| Rank | Model / Platform | Developer | Why It's Hot & Important | Key Strengths & Access |
|------|------------------|-----------|---------------------------|------------------------|
| 1 | Seedance 2.0 | ByteDance | Top overall & best value in many 2026 rankings | Unified multimodal (text/image/audio/video), native joint audio-video, cinematic quality |
| 2 | Kling 3.0 / Kling 3.0 Omni | Kuaishou | Hyper-realistic motion, physics, multi-character | Excellent prompt adherence, camera control, native audio, strong commercial use |
| 3 | Veo 3.1 | Google DeepMind | Best cinematic quality + native audio | High fidelity, character consistency, ingredients-to-video, 4K support |
| 4 | Grok Imagine Video | xAI | Current leaderboard leader in many arenas | Strong motion, refinement, social-first output, fast iteration |
| 5 | HappyHorse-1.0 | Alibaba-ATH | High Elo scores, emerging powerhouse | Superior realism and consistency |
| 6 | Sora 2 | OpenAI | Cinematic physics & storytelling | Excellent narrative, synchronized audio (where available) |
| 7 | Wan 2.6 / Wan 2.2 | Alibaba | Best open-source / local option | MoE architecture, efficient on consumer GPUs, multilingual |
| 8 | Runway Gen-4.5 | Runway | Advanced creative control for pros | Motion brushes, inpainting, film-grade tools |
| 9 | SkyReels V4 | Skywork AI | Strong character & human focus | Cinematic human animation |
| 10 | Luma Ray3 / Ray3.14 | Luma AI | Atmospheric & environment-heavy shots | Dream Machine successor, strong image-to-video |
| 11 | Hailuo 2.3 (MiniMax) | MiniMax | Speed + quality balance | Fast generation, everyday use |
| 12 | HunyuanVideo (I2V variants) | Tencent | Strong open-source cinematic model | 13B params, physics-aware |
| 13 | Pika 2.5 / Pikaformance | Pika Labs | Fast creative & avatar work | Lip-sync, effects, quick iterations |
| 14 | LTX-2 / LTXVideo | Lightricks | Efficient open-source, low VRAM | Strong open weights, multimodal pipelines |
| 15 | Mochi 1 | Genmo | Photorealistic open-source | Apache 2.0, fine-tunable |
| 16 | PixVerse V5.5 | PixVerse | Sharp cinematic visuals | Fast T2V/I2V, style consistency |
| 17 | CogVideoX-5B / variants | Zhipu AI / community | Robust open-source baseline | Good community support |
| 18 | Wan 2.1 Turbo / I2V | Alibaba | Fast & affordable open-source | Low VRAM (8GB+), efficient |
| 19 | Seedance 1.5 Pro | ByteDance | Predecessor still widely used | Reliable multimodal |
| 20 | Kling 2.6 | Kuaishou | Balanced speed & quality | Talking characters, dialogue |
| 21 | Veo 3 (base) | Google | Precursor with strong audio | Native synchronized audio |
| 22 | Runway Gen-3 Alpha | Runway | VFX & editing powerhouse | Professional tools |
| 23 | SkyReels V1 | Skywork AI | Human-centric fine-tune | Open-source cinematic humans |
| 24 | Hailuo 02 | MiniMax | Speed-focused | Quick testing & social content |
| 25 | Pika 2.2 | Pika Labs | Beginner-friendly effects | PikaFrames, swaps |
| 26 | Wan 2.2-T2V-A14B | Alibaba | Text-to-video specialist | Cinematic control |
| 27 | Grok Imagine Video 720p | xAI | Optimized variant | High arena performance |
| 28 | Veo 3.1 Audio 1080p | Google | Audio-specialized | Native dialogue & SFX |
| 29 | LTX-Video | Lightricks | Lightweight versatile | Good for local deployment |
| 30 | HunyuanVideo-I2V | Tencent | Image-to-video focus | Spatial-temporal strength |
| 31 | Dreamina Seedance 2.0 720p | ByteDance | Optimized variant | High leaderboard Elo |
| 32 | Kling 3.0 1080p Pro | Kuaishou | Pro tier quality | Multi-subject motion |
| 33 | Wan 2.1-I2V-14B-720P-Turbo | Alibaba | Fast I2V | Budget & speed king |
| 34 | NVIDIA Cosmos Predict/Transfer | NVIDIA | Physical AI & synthetic video | World simulation focus |
| 35 | Stable Video Diffusion (SVD-XT) | Stability AI | Classic open baseline | Community extensions |
| 36 | Qwen-VL Video variants | Alibaba | Multimodal integration | Strong reasoning + video |
| 37 | Llama 4 Multimodal Video | Meta | Open weights multimodal | Large context video understanding |
| 38 | GLM-4.5V Video | Zhipu | Efficient multimodal | 3D reasoning support |
| 39 | SenseNova-U1 | SenseTime | Open multimodal generation | Unified text-image reasoning |
| 40 | MiMo-V2.5-Pro | Xiaomi | Agentic multimodal | Video + audio workflows |
| 41 | Pixtral Video | Mistral | Vision-language video | Practical applications |
| 42 | Gemma 3 Video | Google | Efficient open multimodal | Lightweight deployment |
| 43 | DeepSeek-VL Video | DeepSeek | Reasoning-focused | Cost-effective |
| 44 | Molmo Video | Allen AI | Open research model | Strong benchmarks |
| 45 | Animate Anyone / variants | Community | Character animation | Open fine-tunes |
| 46 | Open-Sora | HPC-AI Tech | Fully open ecosystem | Community-driven |
| 47 | Pyramid Flow | Community | Flow-based generation | Efficient open alternative |
| 48 | Allegro | Community | Motion quality open | Strong open performance |
| 49 | Hedra Character-3 | Hedra | Omnimodal character | Audio-driven avatars |
| 50 | Flux + Video extensions | Black Forest Labs | Image-to-video hybrids | High-quality base for pipelines |

**Prioritization Advice (2026):**  
- **Must-learn immediately (1–10)**: Seedance 2.0, Kling 3.0, Veo 3.1, Grok Imagine, Wan 2.x — these dominate leaderboards and production workflows.  
- **Quick start**: Try platforms like fal.ai, WaveSpeedAI, or Framia Pro for unified access to multiple models. For local/open: Start with Wan 2.2 or LTX-2 via ComfyUI/Hugging Face.  
- Combine with **agentic workflows**, RAG for prompts, and systems thinking for complex video pipelines.

Video generation moves extremely fast — focus on building projects (e.g., multimodal storytelling agents) to stay ahead. Track leaderboards like Artificial Analysis or LLM-Stats for daily updates.

### `sources/generic/video.community.SPEC.md`

Omitted here; same document as `SPEC.md` above.

### `sources/MAPPING.md`

# Mapping — `video.community`

- VA/generic pack ID: `video.community`
- Previous common ID: `video.community_manager`
- SPEC depth: full generic SPEC body + host runtime binding

### `sources/PROVENANCE.json`

```json
{
  "schema_version": "3.0",
  "sources": [
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
      "title": "疯传",
      "isbn13": "9787508641238",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 疯传，ISBN-13 9787508641238"
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
      "language": "ZH",
      "title": "从零开始做内容：爆款内容的底层逻辑",
      "author": "吕白",
      "isbn13": "9787111664604",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 从零开始做内容：爆款内容的底层逻辑（吕白），ISBN-13 9787111664604"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "YouTube视频之王的崛起之路",
      "author": "【美】马克·伯根",
      "isbn13": "9787516837474",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: YouTube视频之王的崛起之路（【美】马克·伯根），ISBN-13 9787516837474"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Ultimate Guide to Social Media Marketing",
      "author": "Butow, EricGarcia, StephanieBlake etc.",
      "isbn13": "9781599186740",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Ultimate Guide to Social Media Marketing (Butow, EricGarcia, StephanieBlake etc.), ISBN-13 9781599186740"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "新媒体营销圣经",
      "isbn13": "9787550272101",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 新媒体营销圣经，ISBN-13 9787550272101"
    }
  ],
  "agent_id": "video.community",
  "previous_common_agent_id": "video.community_manager",
  "va_taxonomy_aligned": true,
  "generic_source": "generic-swarm-ops/business/video/agents/video.community",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "aligned_at": "2026-07-27T00:48:10.891368Z",
  "generic_source_depth": {
    "excerpts": true,
    "study": true,
    "adopted_at": "2026-07-27T01:30:27.883468+00:00",
    "upstream": "generic-swarm-ops/business/video/agents"
  },
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\video\\agents\\video.community",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```

### `sources/RETHINK_100_APPLIED.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.community",
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
    67,
    72,
    73,
    74,
    82,
    83,
    85,
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
    "67": "Batch mode variants",
    "72": "Brand DNA from past videos",
    "73": "Competitor video analysis",
    "74": "A/B variant generation",
    "82": "Seasonal content calendar",
    "83": "Performance feedback loop",
    "85": "Real-time trend integration",
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
  "agent_id": "video.community",
  "sources": [
    {
      "id": "src_1",
      "title": "Community moderation playbooks, sentiment datasets, escalation rules",
      "description": "Community moderation playbooks, sentiment datasets, escalation rules",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.community",
      "status": "planned_or_partial"
    }
  ],
  "note": "Legal review required before treating external corpora as production grounding."
}
```
