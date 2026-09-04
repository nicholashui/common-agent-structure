# LearnerSimAgent

> Self-contained VA Domain Pack agent on host common-agent-swarm-ops.
> Pack agent ID matches pure VA/generic taxonomy: `video.learnersim`.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 97 |
| **pack_id** | `video.learnersim` |
| **upstream_name** | LearnerSimAgent |
| **category** | `10-Sup` |
| **domain_id** | `video` |
| **previous_common_id** | `video.asset_security_officer` |
| **status** | `registered` |
| **maturity** | L0 / non-active |
| **taxonomy** | Pure VA Domain Pack (via generic pack agents) |
| **folder** | `business/video/agents/video.learnersim/` |

## Responsibility

Simulates learner behavior, confusion points, and assessment performance

Host role binding: `LearnerSimAgent (VA Domain Pack)`. Design-time VA table content below is historical and non-binding for activation.

### Responsibility (from VA table)

Simulates learner behavior, confusion points, and assessment performance

### Knowledge distillation sources (historical)

Learner-modeling datasets, completion analytics, quiz outcome patterns

### Self-quality criteria (historical)

Friction-point prediction, completion accuracy, simulated quiz realism

### Surpass-human signal (historical)

Predicts weak spots before live learner complaints emerge

### Critique bus (historical)

- **Accepts critique from:** InstructionalDesignAgent, LMSAgent, AnalystAgent

- **Comments on:** Confusing content, weak assessments, low-completion pathways

### Tools design-time notes (historical, non-activating)

Learner simulation models, assessment predictors, LMS data

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

### Architecture pattern (historical)

Audience-style simulation adapted for learning outcomes

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

- Prompt reference: `video.prompt.learnersim.v1`
- Rubric reference: `video.rubric.learnersim.v1`
- Critique edges: `{"inputs": ["video.critic"], "outputs": ["video.judge"]}`
- Max refinement: `3`
- VA table quality criteria retained under Provenance and Identity surface above.

## Runtime binding

Authoritative fail-closed host configuration:

```json
{
  "agent_id": "video.learnersim",
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
  "prompt_reference": "video.prompt.learnersim.v1",
  "role": "LearnerSimAgent (VA Domain Pack)",
  "rubric_reference": "video.rubric.learnersim.v1",
  "schema_version": "1.0",
  "status": "registered",
  "va_id": 97,
  "va_name": "LearnerSimAgent",
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

- Pack agent ID `video.learnersim` is aligned to pure VA Domain Pack / generic pack taxonomy (Agent IDs ≈ VA tables).
- Previous common inventory ID `video.asset_security_officer` is historical mapping only.
- Upstream design body below is **historical and non-binding**; local `agent_spec.json` is authoritative.
- Full VA/generic SPEC depth retained for offline design fidelity (including category roster rows and common agent structure when present upstream).

### VA Domain Pack specification body (historical and non-binding)

```text
LearnerSimAgent

> **Self-contained agent definition** for host `upstream-generic-pack`. Body text is embedded from in-pack corpus and upstream-va-design when available. Do not require external repos to understand this agent.

Identity

| Field | Value |
|-------|-------|
| **va_id** | 97 |
| **pack_id** | `video.learnersim` |
| **category** | `10-Sup` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.learnersim/` |

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

Simulates learner behavior, confusion points, and assessment performance

Knowledge distillation sources

Learner-modeling datasets, completion analytics, quiz outcome patterns

Self-quality criteria

Friction-point prediction, completion accuracy, simulated quiz realism

Surpass-human signal

Predicts weak spots before live learner complaints emerge

Critique bus

- **Accepts critique from:** InstructionalDesignAgent, LMSAgent, AnalystAgent

- **Comments on:** Confusing content, weak assessments, low-completion pathways

Tools (design-time documentation)

Learner simulation models, assessment predictors, LMS data

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

Architecture pattern

Audience-style simulation adapted for learning outcomes

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






Additional corpus / va passages naming this agent


From `corpus/study/ai_agent_video_production_workflow.md` Copy: `sources/excerpts/ai_agent_video_production_workflow.md`.


| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | InstructionalDesignAgent + ComplianceAgent + ScreenwriterAgent | SMEAgent |
| Production | AvatarDesignAgent + MotionGraphicsAgent | DirectorAgent |
| Post | EditorAgent + AccessibilityAgent | AccessibilityOptimizerAgent |
| Review | SMEAgent + ComplianceAgent + AccessibilityAgent | LegalAgent |
| Distribution | LMSAgent | AnalystAgent |
| Post-launch | AnalystAgent + InstructionalDesignAgent | LearnerSimAgent |



From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


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
| 102 | **LabelDigitalAgent** | Runs label-side digital rollout, metadata, and channel packaging | Digital music release operations, metadata schemas, distribution platform requirements | Metadata completeness, rollout timing, channel readiness |
…



Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


Provenance

- Master roster row va_id=97 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `[historical-path]
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): upstream-va-design.


<!-- self_contained_spec · video.learnersim · va_id=97 -->

Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **LearnerSimAgent** (`video.learnersim`, va_id=97, category `10-Sup`).

Responsibility focus
Simulates learner behavior, confusion points, and assessment performance

Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: educational video AI, fact verification agents, multimodal accessibility (WCAG), domain-expert RAG, localization QA
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI edtech video, fact-checking AI, accessible media AI
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: AI for educational video, accessibility in media, domain expert AI agents

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

<!-- migration_capability_research · video.learnersim · v1 · 2026-07-13 -->

```

