# ContinuityAgent

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 98 |
| **pack_id** | `video.continuity` |
| **category** | `10-Sup` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.continuity/` |

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

Maintains continuity across character, prop, wardrobe, environment, and time-state

## Knowledge distillation sources

Continuity logs, script supervisor practices, asset manifest state tracking

## Self-quality criteria

State-drift detection, scene-to-scene consistency, manifest update correctness

## Surpass-human signal

Catches continuity breaks earlier than end-of-post review

## Critique bus

- **Accepts critique from:** CostumeDesignAgent, MUAAgent, AIQAConsistencyAgent, CinematographerAgent (DoP), GateKeeperAgent

- **Comments on:** Character-state drift, wardrobe and prop mismatch, time logic errors

## Tools (design-time documentation)

State manifests, shot comparison tools, continuity DB

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

Tool-use / ReAct with continuity manifest enforcement

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


### Document: `study/lifes_quiet_redemption_agent_workflow.md`

_Embedded from `corpus/study/lifes_quiet_redemption_agent_workflow.md`. Also stored at `sources/study/lifes_quiet_redemption_agent_workflow.md` under this agent folder._


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

---

## 3. Agent Service Catalogue (What Each Agent Actually Does on This Film)

Full description of every agent's contribution, the input it consumes, the output it produces, its tools, its self-quality bar, and who reviews it. Grouped by pipeline role.

### 3.1 Orchestration & Planning

| Agent (#) | Service on This Film | Consumes | Produces | Tools | Self-Quality Bar | Critiqued By |
|---|---|---|---|---|---|---|
| IntentAnalysisAgent (DIA) | Decodes the poetic brief into explicit emotional goals, audience, and hidden intent | Client brief, theme statement | Parsed intent + audience model | DIA framework, embedding intent classifier | Intent coverage, ambiguity flags resolved | DirectorAgent, PlannerAgent |
| PlannerAgent (#54) | Breaks film into a 6-phase DAG with shot nodes + critic gates | Parsed intent | Phased DAG, assignments, gate map | LangGraph plan-gen, Gantt/PERT | No missing gate; cost variance <10% | ProducerAgent, RouterAgent |
| OrchestratorAgent (#53) | Executes the DAG; fan-out per shot, retries, escalations | DAG | Scheduled jobs, run state | LangGraph + Temporal, Redis locks | DAG completion ≥99.5%; deadlock = 0 | ProducerAgent, JudgeAgent |
| RouterAgent (#55) | Picks the best agent + model for each shot (Veo vs Kling vs Runway) | Task embeddings | Agent/model routing table | Capability registry, benchmark cache | Routing accuracy ≥95% | CostOptimizerAgent |
| ProducerAgent (#2) | Budget, schedule, phase greenlights | DAG, cost model | Greenlit phase gates | Sheets/Airtable, Temporal, Stripe | On-time; budget ±5% | DirectorAgent |
| CostOptimizerAgent (#74) | Routes re-rolls to cheapest engine meeting quality | Render telemetry | $/quality routing | Pricing APIs, FrugalGPT cascade | Lowest $/successful shot | RouterAgent, FinanceAgent |
| GateKeeperAgent (#57) | Verifies L1/L2/L3 at every phase; signs C2PA | Phase artifacts | Signed pass/fail | c2patool, JSON validators | Zero leaked defects | ComplianceAgent, AIQAConsistencyAgent |
| MemoryAgent (#58) | Stores character bible, prior takes, corrections for recall | All artifacts | Retrievable project memory | Pinecone/Weaviate, MemGPT | Retrieval precision@5 ≥0.9 | All agents |
| JudgeAgent (#56) | Settles disputes (e.g., Editor vs Director on pacing) via debate | Conflicting critiques | Adjudicated ruling | Debate + LLM-as-Judge harness | Inter-rater κ ≥0.8 vs panel | HiTL on overturn |

### 3.2 Above-the-Line & Story

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

### 3.3 Look, Character & Continuity

| Agent (#) | Service on This Film | Consumes | Produces | Tools | Self-Quality Bar | Critiqued By |
|---|---|---|---|---|---|---|
| ConceptArtistAgent (#15) | Designs each character's look across ages (A,B,C,E,F,J young+adult) | Lookbook | Character design sheets | Midjourney v7, SD ControlNet | Style-bible adherence | DirectorAgent |
| CastingAgent (#5) | Selects consented likeness + voice fit per character | Design sheets | Cast/likeness + consent chain | Likeness catalog, voice library | Fit + consent 100% | DirectorAgent, ComplianceAgent |
| AvatarDesignAgent (#47) | Locks synthetic-presenter identity, C2PA-signs each face | Cast refs | Identity hashes, signed refs | HeyGen/Synthesia, c2patool | Identity-hash consistency | ComplianceAgent, DeepfakeDetectionAgent |
| ProductionDesignAgent (#16) | Defines sets (classroom, shop, home, night street) and palette | Lookbook | Set/world look spec | Unreal scouting, Veo location gen | Palette coherence, period accuracy | DirectorAgent |
| CostumeDesignAgent (#17) | Wardrobe per age/role (student, carpenter, mother, office worker) | Design sheets | Wardrobe spec | Fashion-history DB, image-gen | Silhouette read, palette fit | MUAAgent |
| MUAAgent (#18) | Hair/makeup continuity incl. the lipstick beat (Scene 11) | Wardrobe | Continuity hashes per take | Face landmark, perceptual hash | Continuity break <0.5% | ContinuityAgent |
| StyleTransferAgent (#61) | Applies one consistent grade-able aesthetic across all shots | Refs, shots | Per-style LoRA, CLIP score | LoRA, CLIP/DINO, Runway style-lock | Style similarity ≥0.85 | DirectorAgent, ColoristAgent |
| ContinuityAgent (#98) | Tracks identity, wardrobe, props (cat motif), time-state across scenes | All shots | Continuity manifest | State manifests, shot-compare | State-drift detection | AIQAConsistencyAgent, GateKeeperAgent |

### 3.4 Generation, Camera & Audio

| Agent (#) | Service on This Film | Consumes | Produces | Tools | Self-Quality Bar | Critiqued By |
|---|---|---|---|---|---|---|
| PromptEngineerAgent (#46) | Writes the expanded model-facing prompts + negative prompts per shot | Shot card, refs | Final prompts, seeds | Sora 2/Veo 3.1/Runway/Kling, seed registry | Target shot ≤3 iterations | AIQAConsistencyAgent |
| PromptOptimizerAgent (#73) | Auto-tunes weak prompts (OPRO/DSPy) when a shot fails QC | Failed prompt + score | Improved prompt | DSPy MIPRO, OPRO, eval harness | Score uplift per iteration | PromptEngineerAgent |
| CinematographerAgent (#6) | Lensing, lighting, composition (golden hour, shallow DoF) per shot | Shot intent | Lighting/lens spec | Veo camera-path, ACES pipeline | Composition + color-temp consistency | DirectorAgent, ColoristAgent |
| CameraOperatorAgent (#7) | Executes the push-ins, dolly, handheld breath moves | Lens spec | Camera-move presets | Runway camera presets, Kling motion | Frame steadiness, move smoothness | CinematographerAgent |
| TalentAgent (#26) | Renders the on-camera micro-performance (smiles, glances, pauses) | Character refs | Performance takes | HeyGen Avatar IV, emotion models | Emotion-target match | DirectorAgent |
| VoiceOverAgent (#21) | Performs the warm reflective 旁白 in ZH (+EN alt) | VO script | VO takes | ElevenLabs v3, pronunciation lexicon | Prosody + pronunciation match | DirectorAgent |
| VoiceCloneAgent (#48) | If a consistent narrator voice is cloned, handles cloning + consent | Consent + sample | Cloned VO, lip-sync | ElevenLabs cloning, Sync.so | MOS ≥4.2; consent verified | ComplianceAgent, LipSyncAgent |
| ComposerAgent (#20) | Minimalist piano + soft strings score with swells at peaks | Emotion curve | Score stems | Udio/Suno, MIDI, Demucs | Cue-to-emotion alignment | EditorAgent, SoundDesignAgent |
| SoundDesignAgent (#19) | Foley/ambience per scene (pencil, keyboard, soup, city hum) | Shot list | SFX stems | ElevenLabs SFX, Freesound | Sync ≤±1 frame | EditorAgent, ComposerAgent |

### 3.5 Post, QA, Compliance & Delivery

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

---

## 4. Cross-Cutting Services Applied Throughout

These shared capabilities (SYSTEM_REFERENCE §4–§5) operate across every phase, not at a single node.

| Service / Capability | Provided By | Role on This Film |
|---|---|---|
| **Aesthetics scoring (Critic + Aligner + Taste-Keeper)** | Aesthetics Agent | Supplies the L2/perceptual "is this beautiful + warm?" judge signal to Cinematographer, Colorist, PromptEngineer, AIQA |
| **Strategic Goal Achievement (6-stage self-inquiry)** | Strategic Goal framework | Turns the vague "make people feel life saved them" goal into measurable creative targets for Planner/Director |
| **Agentic RAG knowledge backbone** | Agentic RAG System | Serves Chinese cinematic references, golden-hour lighting recipes, prompt patterns to any agent on demand |
| **Psychological profiling / recommendation** | Psych Profile + Recommendation agents | Tunes narrator tone and audience-resonance prediction (Big Five / emotional state) for AudienceSim and Personalization |
| **Continuous self-improvement (Reflexion + RLAIF)** | Optimization Agent + EvaluationHarnessAgent (#79) | Feeds 30/60/90-day retention/ROAS back into prompt + edit choices for the next film in the series |
| **Shared Artifact Handoff Contract (C2PA-signed manifests)** | All agents | Every clip, stem, and master carries `artifact_id`, `continuity_state`, `qc_status`, `provenance_manifest` between phases |
| **Critique Bus (CritiqueMessage JSON)** | All agents | Structured blocker/major/minor feedback; disputes escalate to JudgeAgent → HiTL |

---

## 5. Quality Gate Ladder (Per Shot & Per Phase)

Every artifact clears three layers before GateKeeperAgent advances it (agents.md §11.2).

| Layer | Question | Owner / Mechanism | Threshold |
|---|---|---|---|
| **L1 — Spec** | Did it meet the structured brief (codec, aspect, duration, frame count)? | JSON schema + tool validators | 100% pass |
| **L2 — Rubric** | Does it meet the craft rubric (composition, grade, prosody, beat fit)? | LLM-as-Judge + Aesthetics Agent | ≥85/100 (≤3 Self-Refine iters) |
| **L3 — Preference** | Would the target audience pick this over a human-made baseline? | AudienceSimAgent (#82) pairwise panel + HiTL sample | Win ≥50% (parity) / ≥55% (surpass) |

---

## 6. Delivery Variants & Outlet Specs

| Outlet | Aspect / Spec | Owning Agents | Notes |
|---|---|---|---|
| YouTube (main) | 16:9, 1080p/4K, 24–30fps, burned + soft subs | DistributorAgent (#112), ChannelManagerAgent (#108), SEOAgent (#87) | Full ~60s cut |
| YouTube Shorts | 9:16, face-reframed, burned subs | TrailerEditorAgent (#51), RetentionOptimizerAgent (#76) | 3s hook front-loaded |
| Xiaohongshu (RED) | 9:16 / 3:4, ZH subs | SocialMediaStrategistAgent (#28), LocalizationQAAgent (#44) | Culturally-tuned caption + tags |
| Douyin / TikTok | 9:16, trending-audio aware | SocialMediaStrategistAgent (#28), TrendIntelligenceAgent (#68) | Hook-rate ≥30% target |
| Instagram Reels | 9:16, EN + ZH subs | MarketingAgent (#86), SEOAgent (#87) | Bilingual variant |
| Archive master | ProRes + C2PA, checksum | ArchiveMasterAgent (#114), GateKeeperAgent (#57) | Series-reuse preservation package |

---

## 7. Recommended Tool / Model Stack (June 2026)

| Layer | Models / Tools | Driving Agent(s) |
|---|---|---|
| Agent reasoning | Grok-4.x, Gemini 2.5 Pro (1M), GPT-4o, Claude 4 | Orchestration + all |
| Keyframes / refs | Flux.1 Pro/Kontext, Midjourney v7, Ideogram 3.0 | ConceptArtistAgent, PromptEngineerAgent |
| Video generation | Veo 3.1 (cinematic, character), Kling 3.0 (motion/face), Runway Gen-4 (control), Sora 2 (narrative) | PromptEngineerAgent, RouterAgent |
| Local / self-hosted | ComfyUI + AnimateDiff + ControlNet + IP-Adapter/InstantID | StyleTransferAgent, PromptEngineerAgent |
| Voice / TTS | ElevenLabs v3, GPT-SoVITS / CosyVoice (local, Cantonese) | VoiceOverAgent, VoiceCloneAgent |
| Music | Suno v4 / Udio | ComposerAgent |
| SFX | ElevenLabs SFX, Freesound | SoundDesignAgent |
| Editing / grade | DaVinci Resolve 19+ / CapCut Pro (MCP) | EditorAgent, ColoristAgent |
| Upscale | Topaz Video AI | VFXSupervisorAgent |
| Provenance | c2patool (C2PA) | GateKeeperAgent, AvatarDesignAgent |

---

## 8. Series & Scalability (Reusing the Swarm)

Because the swarm persists character bibles (MemoryAgent #58), identity hashes (AvatarDesignAgent #47), and style LoRAs (StyleTransferAgent #61), a follow-up short reuses ~70% of pre-production. New entries in the 「生活偷偷救赎了我们」 series only re-run Phases 1–4 for new beats, while ContinuityAgent guarantees the recurring "map girl" and "shop cat" stay consistent across episodes.

| Reuse Asset | Stored By | Enables |
|---|---|---|
| Character bible + identity hashes | MemoryAgent, AvatarDesignAgent | Same faces across episodes |
| Style LoRAs + grade LUT | StyleTransferAgent, ColoristAgent | Consistent "warm memory" look |
| 旁白 voice clone | VoiceCloneAgent | Recognizable narrator across series |
| Prompt + seed registry | PromptEngineerAgent | Fast, reproducible re-renders |
| Recurring motifs (cat, paper map) | ContinuityAgent | Audience recognition / brand |

---

*Generated as an enhanced, agent-mapped rebuild of the original "Life's Quiet Redemption" workflow, aligned to the VA-Agent-Swarm 114-agent system. See [SYSTEM_REFERENCE.md](./SYSTEM_REFERENCE.md) for the full architecture.*



---
---

# PART B — Research-Informed Quality Upgrades (June 2026)

> This part hardens Part A with findings from (1) top YouTube growth strategists, (2) xAI's current Grok Imagine video stack, and (3) recent arXiv research on consistent, long-form, multi-shot AI video. Every external claim is cited inline. *Content from all external sources was paraphrased/summarized for compliance with licensing restrictions; no source is quoted beyond fair-use limits.*

## 9. Research Sources → Findings → Workflow Implication

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
| Consistency | [arXiv 2510.21696 — BachVid](https://arxiv.org/html/2510.21696v1) | Training-free consistency for background + character without reference images | Fallback when a clean reference portrait is unavailable |
| Evaluation | [VBench](https://arxiv.org/abs/2311.17982) · [VBench appendix](https://arxiv.org/html/2507.07202) | 16 disentangled dimensions incl. subject consistency, motion smoothness, temporal flicker, spatial relationship, imaging + aesthetic quality, text–video relevance | Replace coarse QC with **VBench 16-dim scorecard** per shot |
| Evaluation | [arXiv 2503.10076 — VMBench](https://arxiv.org/html/2503.10076) | Motion quality evaluated for human-perception alignment | Adds a **motion-naturalness** gate (hands typing, wind, head turns) |
| Evaluation | [arXiv 2504.04907 — Video-Bench](https://arxiv.org/html/2504.04907v1) | MLLM-as-evaluator with few-shot scoring + chain-of-query across all dimensions | Powers the AIQA/Aesthetics judge with structured chain-of-query |
| Orchestration | [arXiv 2508.08487 — MAViS](https://arxiv.org/html/2508.08487v2) | Multi-agent stages (script→shot design→character modeling→keyframe→animation→audio), each under the **3E principle: Explore, Examine, Enhance** | Wrap every swarm node in an explicit Explore→Examine→Enhance micro-loop |
| Orchestration | [arXiv 2506.10540 — MCTS Storytelling](https://arxiv.org/html/2506.10540) | Director / Photography / Reviewer / Post-Production agents with MCTS-driven clip search | Use **MCTS search over candidate clips** instead of fixed 3-reroll cap |
| Orchestration | [arXiv 2605.27891 — SmartDirector](https://arxiv.org/html/2605.27891v1) | Keyframe-conditioned generation with explicit narrative-pacing control | Gives EditorAgent **per-shot pacing knobs** tied to the emotion curve |

## 10. YouTube Marketing Upgrades (mapped to agents)

| Upgrade | What Changes | Owning Agents | Gate / Metric |
|---|---|---|---|
| **Package-first** | Title (≤50 chars, simple words) + thumbnail concept are locked in Phase 1, *before* any generation; the film is made to deliver that promise | BrandStrategistAgent (#85), SEOAgent (#87), Thumbnail=ConceptArtistAgent (#15), DirectorAgent (#1) | CTR predicted ≥ niche median (AudienceSimAgent panel) |
| **Outlier modeling** | Idea is chosen by modeling over-performing videos in the 治愈/reflective-life niche | TrendIntelligenceAgent (#68), AnalystAgent (#81), IdeationAgent (#59) | Idea maps to ≥3 proven outliers |
| **Engineered opener** | First 3–5s re-cut as a hook: strongest image (Scene 1 ECU or Scene 10 warmth) + a curiosity-gap 旁白 line, instead of a slow fade-in | RetentionOptimizerAgent (#76), EditorAgent (#9), ScreenwriterAgent (#3) | First-60s retention ≥ target band |
| **Segment retention bands** | Map the 60s into hook / build / payoff with explicit retention floors per segment, modeled on MrBeast's segmentation | RetentionOptimizerAgent (#76), EmotionalArcAgent (#65) | Per-segment predicted retention ≥ floor |
| **Shorts 3s-hold cut** | Dedicated 9:16 cut: visual hook on **frame 1**, spoken hook ≤14 words, designed to loop | TrailerEditorAgent (#51), MotionGraphicsAgent (#13) | Predicted 3s-hold ≥60%; clean loop seam |
| **Metric instrumentation** | Track CTR + AVD + AVP as first-class KPIs feeding the next episode | AnalystAgent (#81), EvaluationHarnessAgent (#79) | Dashboard live within 24h of launch |

## 11. Generation Engine Upgrade — Add Grok Imagine to the Stack

The routing in §3.4 (RouterAgent #55) gains a Grok tier. Net effect: cheaper, faster iteration up front; premium engines reserved for hero shots.

| Stage | Engine Choice | Why (cited) | Agent |
|---|---|---|---|
| Divergent draft / variant browse | **Grok Imagine 1.5 Fast** (6s, 720p, ~25s/clip) | Fast enough to try many framings and discard quickly ([x.ai](https://x.ai/news/grok-imagine-video-1-5), [imagine.art](https://www.imagine.art/blogs/xai-grok-imagine-video-1-5-guide)) | PromptEngineerAgent (#46), RouterAgent (#55) |
| Keyframe → motion (identity-safe) | **Grok Imagine 1.5 I2V** (animates the locked keyframe, faithful to source) | Continues the still rather than reinterpreting it, protecting face + lighting ([x.ai](https://x.ai/news/grok-imagine-1-5)) | PromptEngineerAgent (#46), ContinuityAgent (#98) |
| Fast full-film rough cut | **Grok Imagine Agent Mode** (plans/stitches 6s clips, native audio, in-quotes lip-sync) | Produces a stitched draft of the whole arc for early editorial review ([codersera](https://codersera.com/blog/grok-imagine-agent-mode-launch-2026/)) | OrchestratorAgent (#53), EditorAgent (#9) |
| Hero / emotional-peak shots | **Veo 3.1 / Kling 3.0 / Runway Gen-4** | Higher fidelity + camera control for Scenes 1, 5, 10, 12 | CinematographerAgent (#6) |
| Local / privacy-sensitive | **ComfyUI + CharCom LoRAs + IP-Adapter** | Full control, per-character LoRA identity ([arXiv CharCom](https://arxiv.org/html/2510.10135v1)) | StyleTransferAgent (#61) |

## 12. Character-Consistency Upgrade (the film's hardest problem)

Replaces "attach a reference image, strength 70–90%" with a research-grade identity stack.

| Technique | Applied To | Mechanism (cited) | Owning Agent | Metric |
|---|---|---|---|---|
| **Mandatory visual anchoring** | Every character shot | Generate a locked keyframe first; never pure T2V — visual priors are essential or consistency collapses ([arXiv 2512.16954](https://arxiv.org/html/2512.16954)) | PromptEngineerAgent (#46) | ID score does not collapse vs anchor |
| **Per-character LoRA (per age)** | A,B,C,E,F,J × young/adult | Composable adapters on a frozen backbone, prompt-aware ([CharCom](https://arxiv.org/html/2510.10135v1)) | StyleTransferAgent (#61) | Face similarity ≥0.85 (ArcFace) |
| **RL identity reinforcement** | Multi-person shots (Scene 10 dinner) | Identity-GRPO improved multi-human consistency ~18.9% ([arXiv 2510.14256](https://arxiv.org/html/2510.14256v1)) | AIQAConsistencyAgent (#49) | Per-person drift = 0 across frames |
| **Memory-conditioned generation** | Across all 14 cards | Shot-by-shot diffusion conditioned on prior-shot memory ([StoryMem](https://arxiv.org/html/2512.19539)) | MemoryAgent (#58) + PromptEngineerAgent | Cross-scene coherence pass |
| **Training-free fallback** | Shots lacking a clean portrait | Background+character consistency without references ([BachVid](https://arxiv.org/html/2510.21696v1)) | ContinuityAgent (#98) | Consistency ≥ threshold |
| **Fine-grained ID audit** | QC gate | VLM-based identity-preservation eval beyond global embeddings ([arXiv 2511.08087](https://arxiv.org/html/2511.08087v1)) | AIQAConsistencyAgent (#49) | Fine-grained ID delta below τ |

## 13. Evaluation Upgrade — VBench-Grade QC Scorecard

The §5 gate ladder's L2 is replaced by a multi-dimensional scorecard scored by an MLLM judge (Video-Bench style, chain-of-query) plus motion-perception checks.

| Dimension (VBench/VMBench) | What It Catches on This Film | Threshold | Judge |
|---|---|---|---|
| Subject (identity) consistency | Face/age drift A→E across scenes | ≥0.90 | AIQAConsistencyAgent (#49) |
| Temporal flicker | Shimmer on shop interior / night bokeh | below τ | AIQAConsistencyAgent |
| Motion smoothness | Hands typing (S3), dolly-in (S10) | ≥ rubric | VMBench check ([arXiv 2503.10076](https://arxiv.org/html/2503.10076)) |
| Imaging quality | Grain/sharpness of close-ups | ≥ rubric | Aesthetics Agent |
| Aesthetic quality | "warm memory" look, composition | ≥85/100 | Aesthetics Agent |
| Spatial relationship | Eyeline match S4 monitor reflection | pass | AIQAConsistencyAgent |
| Text–video relevance | Prompt adherence per shot | CLIP-T ≥0.32 | AIQAConsistencyAgent |
| Motion (human-perception) | Natural breath/wind, no jitter | ≥ VMBench band | VMBench ([2503.10076](https://arxiv.org/html/2503.10076)) |

Scoring method: MLLM evaluator with few-shot scoring + chain-of-query ([Video-Bench, arXiv 2504.04907](https://arxiv.org/html/2504.04907v1)), giving diagnostic, per-dimension feedback rather than a single number.

## 14. Orchestration Upgrade — 3E Loop + MCTS Search

| Pattern | Replaces | How It Works (cited) | Where Applied |
|---|---|---|---|
| **3E micro-loop (Explore→Examine→Enhance)** | Single-pass node execution | Each agent first explores options, examines against the rubric, then enhances before handing off ([MAViS, arXiv 2508.08487](https://arxiv.org/html/2508.08487v2)) | Every DAG node (esp. PromptEngineer, Editor, Composer) |
| **MCTS clip search** | Fixed ≤3 re-roll cap | Reviewer agent runs Monte-Carlo tree search over candidate clips to pick the best path ([arXiv 2506.10540](https://arxiv.org/html/2506.10540)) | Hero shots (S1, S5, S10, S12) |
| **Narrative-pacing control** | Manual trims | Keyframe-conditioned pacing knobs tied to the emotion curve ([SmartDirector, arXiv 2605.27891](https://arxiv.org/html/2605.27891v1)) | EditorAgent (#9) ↔ EmotionalArcAgent (#65) |
| **Unified director front-end** | Hand-written shot prompts only | A director model converts the brief into structured multi-shot scripts for non-experts ([UniMAGE, arXiv 2512.23222](https://arxiv.org/html/2512.23222)) | DirectorAgent (#1) + ScreenwriterAgent (#3) |

## 15. Revised Opening & Shorts Cards (concrete deltas)

| Card | Original | Research-Informed Revision |
|---|---|---|
| **Hook (new 0–3s)** | Slow fade into Scene 1 study ECU | Open on the *strongest* warm frame (S10 dinner steam or S1 eyes), with a ≤14-word curiosity-gap 旁白 ("有些愿望没有实现，后来我才懂为什么"), so the first 3s earns the watch ([opus.pro](https://www.opus.pro/blog/youtube-shorts-hook-formulas), [MrBeast breakdown](https://sherwood.news/culture/mrbeast-youtube-leaked-internal-success-document/)) |
| **Title (package-first)** | (none) | ≤50 chars, simple words, locked before generation ([Galloway summary](https://outlierkit.com/resources/youtube-scriptwriting-methods-compared/)) |
| **Shorts cut** | 9:16 smart-crop of main film | Purpose-built: visual hook on frame 1, ≤14-word VO, clean loop seam, optimized for 3s-hold + replay ([rendercut](https://rendercut.io/why-viewers-scroll-away-first-3-seconds/), [findmecreators](https://www.findmecreators.com/blog/youtube-shorts-retention-rate)) |
| **Ending cards** | Static black/white text | Keep — but A/B the *thumbnail+title* pair, not the poem, since packaging drives the click ([Colin & Samir](https://www.colinandsamir.com/resources/the-new-rules-of-youtube-from-paddy-galloway)) |

---

### Sources

YouTube strategy: [Colin & Samir / Paddy Galloway](https://www.colinandsamir.com/resources/the-new-rules-of-youtube-from-paddy-galloway), [OutlierKit](https://outlierkit.com/resources/youtube-scriptwriting-methods-compared/), [Paddy Galloway Accelerator](https://www.paddygalloway.com/accelerator), [Sherwood/MrBeast doc](https://sherwood.news/culture/mrbeast-youtube-leaked-internal-success-document/), [koi.app](https://www.koi.app/posts/mrbeast-s-blueprint-for-youtube-domination-key-insights-from-the-leaked-employee-guide), [complexminds](https://complexminds.substack.com/p/the-mr-beast-retention-formula-that), [opus.pro](https://www.opus.pro/blog/youtube-shorts-hook-formulas), [rendercut](https://rendercut.io/why-viewers-scroll-away-first-3-seconds/), [vexub](https://vexub.com/blog/viral-short-form-video-hooks), [findmecreators](https://www.findmecreators.com/blog/youtube-shorts-retention-rate).
xAI Grok Imagine: [x.ai 1.5 Preview](https://x.ai/news/grok-imagine-1-5), [x.ai Video 1.5 Fast](https://x.ai/news/grok-imagine-video-1-5), [codersera Agent Mode](https://codersera.com/blog/grok-imagine-agent-mode-launch-2026/), [imagine.art](https://www.imagine.art/blogs/xai-grok-imagine-video-1-5-guide), [aimlapi](https://aimlapi.com/blog/grok-imagine-video-vs-grok-imagine-video-1-5-preview).
arXiv: [2512.16954](https://arxiv.org/html/2512.16954), [2510.10135 CharCom](https://arxiv.org/html/2510.10135v1), [2510.14256 Identity-GRPO](https://arxiv.org/html/2510.14256v1), [2512.19539 StoryMem](https://arxiv.org/html/2512.19539), [2510.21696 BachVid](https://arxiv.org/html/2510.21696v1), [2511.08087 VLM ID eval](https://arxiv.org/html/2511.08087v1), [2311.17982 VBench](https://arxiv.org/abs/2311.17982), [2503.10076 VMBench](https://arxiv.org/html/2503.10076), [2504.04907 Video-Bench](https://arxiv.org/html/2504.04907v1), [2508.08487 MAViS](https://arxiv.org/html/2508.08487v2), [2506.10540 MCTS Storytelling](https://arxiv.org/html/2506.10540), [2605.27891 SmartDirector](https://arxiv.org/html/2605.27891v1), [2512.23222 UniMAGE](https://arxiv.org/html/2512.23222).

*All external content above was paraphrased/summarized for compliance with licensing restrictions.*



## Additional corpus / va passages naming this agent


### From `corpus/study/SYSTEM_REFERENCE.md` Copy: `sources/excerpts/SYSTEM_REFERENCE.md`.


| Layer | Responsibility | Key Agents / Services |
|-------|---------------|----------------------|
| **Orchestration** | Plan, route, schedule, retry, escalate | PlannerAgent (#54), OrchestratorAgent (#53), RouterAgent (#55), JudgeAgent (#56) |
| **Asset & Data Backbone** | Immutable asset IDs, versioning, dependency edges, rights | Asset Store (S3 + metadata DB) |
| **Message & State Fabric** | Critique bus, job status, gate decisions | Redis Streams / NATS, durable state store |
| **Quality & Continuity Mesh** | Multi-pass QC, continuity, accessibility, compliance | AIQAConsistencyAgent (#49), ComplianceAgent (#37), AccessibilityAgent |
| **Observability & Replay** | Live status, failure causes, bottlenecks, replay | AgentOps pipeline, LangSmith traces |
| **Delivery Fabric** | Package masters into outlet-specific variants | TrailerEditorAgent (#51), SocialMediaStrategistAgent (#28) |
| **Compute & Storage Scaling** | GPU autoscale, tiered storage | Infrastructure layer (Docker/K8s) |

These agents manage orchestration, quality, continuity, and system-level concerns:

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 53 | OrchestratorAgent | DAG execution, retries, fan-out/fan-in | — |
| 54 | PlannerAgent | Decomposes brief into phased DAG | — |
| 55 | RouterAgent | Picks right agent + model for subtask | — |
| 56 | JudgeAgent | Adjudicates disputes via debate | — |
| 57–80 | (Various meta-agents) | Memory, continuity, safety, escalation, etc. | — |

| Field | Purpose |
|-------|---------|
| `artifact_id` / `version` | Unique identity for every output and revision |
| `parent_assets` | Provenance links to scripts, prompts, plates, stems |
| `brief_scope` | Subtask, acceptance criteria, target audience |
| `technical_spec` | Codec, aspect ratio, duration, frame rate, color space, loudness |
| `rights_and_consent` | License state, likeness/voice consent, territorial limits |
| `continuity_state` | Character look, props, wardrobe, environment, identity hash |
| `qc_status` | Latest L1/L2/L3 QC result |
| `target_channels` | Theatrical, streaming, broadcast, social, CRM, LMS |
| `provenance_manifest` | C2PA reference, critique log pointer, sign-off chain |



### From `corpus/study/ai_agent_video_production_workflow.md` Copy: `sources/excerpts/ai_agent_video_production_workflow.md`.


**Working rules:**
1. Extract concepts under four lenses: **technical architecture**, **implementation sequence**, **quality/compliance**, and **continuous learning**.
2. Prefer workflow-relevant facts over market commentary unless the market fact changes routing, cost, or scale decisions.
3. Record handoff artifacts explicitly: prompts, scene packets, stems, graded masters, manifests, provenance bundles, and telemetry.
4. Reject role inflation unless a new role closes a real gap in orchestration, validation, continuity, delivery, or retraining.
5. Treat delivery packaging, observability, and asset management as system architecture, not postscript operations.

| Layer | Core responsibility | Implementation notes |
|---|---|---|
| **Orchestration runtime** | Plan, route, schedule, retry, and escalate agent tasks | PlannerAgent decomposes the brief; OrchestratorAgent executes the DAG; RouterAgent selects agent-model pairs; JudgeAgent arbitrates disputes |
| **Asset and data backbone** | Store every prompt, source asset, derived asset, version, dependency edge, and usage right | Requires immutable asset IDs, copy-on-write versions, dependency-triggered rerender rules, and searchable metadata |
| **Message and state fabric** | Carry critique, job status, render events, and gate decisions across agents | Event-driven bus plus durable state store; every long-running job must be resumable and auditable |
| **Quality and continuity mesh** | Run technical QC, continuity checks, artifact detection, accessibility, and compliance gates | Uses multi-pass validation, temporal continuity scans, loudness and color checks, and role-specific rubric judges |
| **Observability and replay** | Expose live status, failure causes, bottlenecks, and historical decisions | Structured logs, job timelines, gate dashboards, benchmark alerts, and replayable artifact lineage |
| **Delivery fabric** | Package masters into theatrical, streaming, broadcast, archive, trailer, and campaign variants | Distribution is a branching pipeline with outlet-specific specs, captions, metadata, DRM/KDM, and provenance payloads |
| **Compute and storage scaling** | Match infrastructure spend to production scale without breaking deadlines | Separate interactive generation from batch rendering; autoscale GPU pools; tier hot, warm, and archive storage |

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

| Passes | Primary question |
|---|---|
| **1-20** | Are all extracted claims traceable to the reference set and aligned with the document's structure? |
| **21-40** | Does the architecture describe the real control plane: orchestration, memory, assets, delivery, and observability? |
| **41-60** | Are workflow handoffs explicit enough for implementation, QA, continuity, and compliance automation? |
| **61-80** | Are metrics, thresholds, and evaluation layers technically coherent across creative, technical, and business gates? |
| **81-100** | Is the wording unambiguous, internally consistent, and suitable for professional technical documentation? |

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

| Phase | Primary outputs | Mandatory gates |
|---|---|---|
| **Greenlight** | Approved brief, KPI targets, budget envelope, rights-risk register, scale profile | ProducerAgent, FinanceAgent, ComplianceAgent, PlannerAgent |
| **Pre-production packet** | Script lock, storyboard/lookbook, asset IDs, character/world bibles, consent state, continuity baselines | DirectorAgent, ScreenwriterAgent, Asset/Data Backbone, Continuity checks |
| **Production packet** | Shot prompts, camera plans, performance refs, plates, generated takes, render telemetry | PromptEngineerAgent / GeneratorOperator, CinematographerAgent, AIQAConsistencyAgent |
| **Post master** | Timelines, graded masters, stems, captions/subtitles, QC reports, outlet variants | EditorAgent, ColoristAgent, SoundMixerAgent, Accessibility checks |
| **Review and release pack** | AudienceSim results, legal review, provenance bundle, sign-off log, unresolved-risk list | ComplianceAgent, JudgeAgent, HumanInTheLoop when required |
| **Distribution package** | DCP, streaming mezzanine, broadcast master, archive package, trailer/social cutdowns, 
…



### From `corpus/study/human_video_production_workflow.md` Copy: `sources/excerpts/human_video_production_workflow.md`.


| Phase | Step | Crew | Tools / Method | Deliverable | Typical Time |
|-------|------|------|----------------|-------------|--------------|
| 1. Development | Logline → treatment → screenplay | Screenwriter, Script Editor, Producer | Final Draft, Black List feedback | Approved screenplay | 3–6 months |
| 1. Development | Financing + IP / rights | Producer, EP, Legal | Pitch deck, LLC, chain of title | Greenlit budget | 2–6 months |
| 1. Pre-production | Visual development (concept art, style bible) | Director, Production Designer, Concept Artists, AI Avatar Designer | Midjourney, Flux, character LoRAs | Locked visual bible | 2–3 months |
| 1. Pre-production | Storyboard / animatic | Storyboard Artists, Editor | Storyboarder + temp VO | Full animatic | 1–2 months |
| 1. Pre-production | Cast voice + likeness (with consent docs) | Casting Director, Legal | SAG-AFTRA AI rider, consent forms | Signed talent + voice models | 1–2 months |
| 2. Production | Scene-by-scene AI generation + traditional plates where needed | AI Generator Ops (pool), VFX Sup, DoP (for hybrid) | Sora, Veo, Runway, Kling, Unreal Engine, virtual production | Rough scene library | 3–6 months |
| 2. Production | Consistency / continuity QC | AI QA Reviewer team, Script Supervisor | Frame-by-frame audit, character-seed registry | Approved scene takes | Parallel |
| 2. Production | Voice performance + lip-sync | Voice Cast, Lip-Sync Specialists | ElevenLabs, Sync.so, Hedra | Synced dialogue tracks | 1–2 months |
| 2. Production | Original score (orchestral + electronic) | Composer, Orchestrator, Musicians | DAW + scoring stage | Final score | 2–3 months |
| 3. Post | Editorial (cut down to feature length) | Editor + Assistant Editors | Avid, Premiere | Picture lock | 2–3 months |
| 3. Post | VFX cleanup, upscale to 4K, color grade | VFX Comp, Colorist | Nuke, Topaz, Resolve | DCP-ready picture | 1–2 months |
| 3. Post | Sound design + 5.1 / Atmos mix | Sound Designer, Re-recording Mixer | Pro Tools + dub stage | Final Atmos mix | 1 month |
| 4. Review | Test screenings + director's cut adjustments | Director, Editor, Test Audience | NRG-style test screening, scorecards | Final cut | 1–2 months |
| 4. Review | MPA rating, AI provenance, legal QC | Legal Reviewer, Compliance, MPA submission | C2PA credentials, MPA classification | Rated + cleared deliverables | 1–2 months |
| 5. Distribution | Festival premiere (Sundance / Cannes / Venice) → sales agent → streamer/theatrical | Sales Agent, Festival Strategist, Distributor | FilmFreeway, AFM, Cannes Marché | Distribution deal | 6–12 months |
| 5. Distribution | Marketing campaign (trailer, posters, press tour) | Marketing Lead, Trailer House, PR Firm | Mark Woollen-style trailer, Rotten Tomatoes press screenings | Launch live | 3–6 months pre-release |
| 6. Post-launch | Box office / streaming metrics, reviews, awards campaign | Distributor, Awards Strategist | Variety / Deadline tracking, Gold Derby | Awards run, sequel/IP plan | 12+ months |



### From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


class ContinuityState(BaseModel):
    character_look: dict = {}
    props: list[str] = []
    wardrobe: dict = {}
    environment: dict = {}
    identity_hash: str | None = None     # for AIQA / Avatar identity drift

class Artifact(BaseModel):
    artifact_id: str
    version: int = 1
    media_type: str                        # video|audio|image|script|manifest|...
    uri: str | None = None
    parent_assets: list[str] = []
    brief_scope: dict                       # subtask, acceptance criteria, audience
    technical_spec: TechnicalSpec | None = None
    rights_and_consent: RightsAndConsent
    continuity_state: ContinuityState = ContinuityState()
    qc_status: QCStatus = QCStatus()
    target_channels: list[str] = []
    provenance_manifest: ProvenanceManifest = ProvenanceManifest()
```

class Category(str, Enum):
    pacing="pacing"; continuity="continuity"; accuracy="accuracy"
    compliance="compliance"; accessibility="accessibility"; brand="brand"
    craft="craft"; aesthetic="aesthetic"   # aesthetic added per aesthetics_agent spec

| API | Layer | Mechanism | Pass |
|-----|-------|-----------|------|
| `qc.l1_spec(artifact)` | Spec | JSON-schema + tool validators (codec/LUFS/aspect/length) | 100% |
| `qc.l2_rubric(artifact, rubric)` | Rubric | LLM-as-judge w/ role constitution | ≥85/100 |
| `qc.l3_preference(artifact, baseline)` | Preference | Pairwise vs human ref + AudienceSim ≥200 personas + ≥20 HiTL | ≥0.50 parity / ≥0.55 surpass |
| `qc.delivery(artifact)` | Q1–Q6 | spec / artifact / audio-sync / continuity / perceptual / outlet-readiness | all 6 pass |

**Tests:** every agent: L1 schema conformance; L2 rubric ≥85 on its golden inputs; emits/accepts critique per the matrix; respects its tool allowlist; metered. Category-level integration tests (e.g., DoP→Colorist→Editor handoff preserves continuity_state).

### Theme 4 — Quality Mesh (31–40)
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



### From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


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
| 81 | **AnalystAgent** | Aggregates business, creative, and technical performance telemetry into decision-ready reports | Platform analytics dashboards; experiment logs; evaluation-harness outputs; benchmark histories | KPI completeness; forecast-vs-actual variance within tolerance; insight-to-action turnaround | Detects actionable performance shifts faster than human analyst rotations | SocialMediaStrategistAgent, PerformanceMarketerAgent, EvaluationHarnessAgent | Campaign pacing, release timing, retention and ROAS anomalies | YouTube Analytics, Meta/TikTok Ads dashboards, BI warehouse, benchmark logs | ReAct over telemetry + regression analysis |
| 82 | **AudienceSimAgent** | Simulates audience preference, engagement, and drop-off | Pairwise preference datasets; retention studies; audience segmentation models | Preference stability across cohorts; retention-prediction accuracy; disagreement logging | Predicts audience reaction earlier than conventional test-screen cycles | DirectorAgent, EditorAgent, AnalystAgent, JudgeAgent | Hooks, pacing, clarity, emotional fit, trailer strength | Persona simulators, pairwise evaluation harness, retention models | LLM-as-Judge + pairwise preference panel |
| 83 | **AccessibilityAgent** | Owns final accessibility acceptance before release | WCAG 2.2, captioning and AD guidelines, Deaf/HoH review frameworks | Caption accuracy, AD completeness, contrast compliance, release-readiness | Finds release-blocking accessibility issues before human audits do | AccessibilityOptimizerAgent, EditorAgent, ColoristAgent, SoundMixerAgent | Caption sync, contrast issues, missing AD or sign-language layers | Caption validators, contrast analyzers, AD review tools | Constitutional AI with accessibility constitution |
| 84 | **BrandAgent** | Enforces brand voice, claims boundaries, and visual consistency | Brand books, approved campaigns, legal claim guardrails, tone guides | Brand-voice similarity, policy adherence, low deviation across assets | Holds cross-channel brand consistency better than fragmented human review | CopywriterAgent, MotionGraphicsAgent, MarketingAgent, BrandStrategistAgent | Voice drift, visual inconsistency, claim creep | Brand asset library, embedding similarity, style guides | Self-Refine against brand constitution |
| 85 | **BrandStrategistAgent** | Defines audience-value framing and positioning before script and campaign execution | Positioning frameworks, campaign strategy decks, market research, brand architecture docs | Strategy coherence, differentiation strength, audience-message clarity | Produces clearer brand-to-script translation than ad hoc human handoffs | BrandAgent, ScreenwriterAgent, MarketingAgent | Positioning gaps, weak value proposition, misaligned audience framing | Research decks, messaging frameworks, strategy templates | Multi-agent debate with BrandAgent and CreativeDirectorAgent |
| 86 | **MarketingAgent** | Packages content for launch, promotions, and release sequencing | Campaign playbooks, launch calendars, media plans, asset packaging requirements | Metadata completeness, asset readiness, launch sequencing accuracy | Ships multi-channel launch packages faster than manual campaign ops | SocialMediaStrategistAgent, SEOAgent, CopywriterAgent, TrailerEditorAgent | Missing formats, weak rollout timing, incomplete promotion sets | Campaign management suites, metadata tools, release planners | ReAct over launch checklists and channel requirements |
| 87 | **SEOAgent** | Optimizes discoverability through titles, descriptions, metadata, and search intent | Search ranking studies, video metadata best practices, keyword taxonomies | Keyword fit, metadata completeness, search-intent match | Lifts discoverability faster than manual metadata tuning | MarketingAgent, CopywriterAgent, AnalystAgent | Weak keywords, poor title-description fit, metadata omissions | Keyword tools,
…



### From `corpus/study/ui/backend_agent_management.md` Copy: `sources/excerpts/backend_agent_management.md`.


```text
┌─────────────────────────────────────────────────────────────────┐
│                    MEMORY SYSTEM                                  │
│                                                                 │
│  ┌─────────────────┐          ┌─────────────────────────────┐  │
│  │  Vector DB       │          │  Structured Store            │  │
│  │  (Pinecone)      │          │  (PostgreSQL)                │  │
│  │                  │          │                             │  │
│  │  Stores:         │          │  Stores:                    │  │
│  │  • Style locks   │          │  • Series bible entries     │  │
│  │  • Tone notes    │          │  • Character state          │  │
│  │  • Past decisions│          │  • Continuity log           │  │
│  │  • Critique hist │          │  • Budget decisions         │  │
│  └────────┬─────────┘          └──────────────┬──────────────┘  │
│           │                                    │                 │
│           └──────────────┬─────────────────────┘                 │
│                          │                                       │
│                          ▼                                       │
│              ┌───────────────────────┐                           │
│              │   Memory API          │                           │
│              │                       │                           │
│              │   recall(query) →     │   Any agent can call      │
│              │     relevant entries  │   this as a TOOL during   │
│              │                       │   its LLM execution       │
│              │   store(entry) →      │                           │
│              │     persists fact     │                           │
│              └───────────────────────┘                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘



## Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


## Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


## Provenance

- Master roster row va_id=98 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `C:\Project\va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.continuity · va_id=98 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **ContinuityAgent** (`video.continuity`, va_id=98, category `10-Sup`).

### Responsibility focus
Maintains continuity across character, prop, wardrobe, environment, and time-state

### Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: AI compliance agents, media law automation, content moderation, continuity checking, template systems, finance ops agents
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI compliance media, content safety agents, continuity AI
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: compliance automation for media, AI content safety, continuity supervision AI

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

<!-- migration_capability_research · video.continuity · v1 · 2026-07-13 -->
