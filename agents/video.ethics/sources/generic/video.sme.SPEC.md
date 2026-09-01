# SMEAgent (Subject-Matter Expert)

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 33 |
| **pack_id** | `video.sme` |
| **category** | `7-Edu` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.sme/` |

## Category roster section (full, from agents.md)

_The following is the complete category section from the master roster (includes peers in the same craft category)._


## 7. Education & Domain-Expert Agents

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

---


## Responsibility

Domain accuracy in target field

## Knowledge distillation sources

Peer-reviewed journals; certified curricula (CFA, USMLE, AWS); expert interviews

## Self-quality criteria

Citation density; benchmark exam pass; hallucination ≤0.5%

## Surpass-human signal

Passes same certification as human pro

## Critique bus

- **Accepts critique from:** FactCheckerAgent, peer SMEAgents (debate)

- **Comments on:** ScriptwriterAgent (inaccuracy), MotionGraphicsAgent (mis-labels)

## Tools (design-time documentation)

PubMed/arXiv/JSTOR search APIs; exam-question banks; RAG over certified corpora

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

Multi-agent debate + RAG retrieval

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
| 32 | InstructionalDesignAgent | Learning objectives → content | — |
| 33 | SMEAgent | Domain accuracy | — |
| 34 | FactCheckerAgent | Source-grade every claim | — |
| 35 | MedicalIllustratorAgent | Anatomy & procedure visuals | — |
| 36 | JournalistAgent | Reporting + ethics | — |
| 37 | ComplianceAgent (Legal) | FTC, HIPAA, GDPR, IP clearance | — |
| 38 | FinanceAgent | Market/earnings accuracy | — |
| 39 | FoodStylistAgent | Camera-ready food | — |
| 40 | TravelCineAgent | Destination cinematography | — |
| 41 | ChildrensAuthorAgent | Age-appropriate content | — |
| 42 | AudiobookNarratorAgent | Sustained narration | — |
| 43 | SignLanguageInterpreterAgent | ASL/BSL interpretation | — |
| 44 | LocalizationQAAgent | Translation + cultural fit | — |
| 45 | RealEstatePhotoAgent | Interiors, 3D scans | — |

| Capability | What It Provides | Used By | Specification |
|-----------|-----------------|---------|---------------|
| **Strategic Goal Achievement Framework** | 6-stage self-inquiry system for transforming vague goals into actionable plans | All planning agents (PlannerAgent, ProducerAgent, DirectorAgent) | [strategic_goal_achievement_agent_functional_specification.md](./strategic_goal_achievement_agent_functional_specification.md) |
| **Screenwriter Goal Achievement** | Practical demonstration of goal framework applied to creative writing | ScreenwriterAgent, ShowrunnerAgent, ComedyWriterAgent | [screenwriter_strategic_goal_achievement_agent_functional_specification.md](./screenwriter_strategic_goal_achievement_agent_functional_specification.md) |
| **Psychological Profiling** | 100 creator profiles with MBTI, motivations, fears, creative parameters | CastingAgent, TalentAgent, PersonalizationEngineerAgent, UGCCreatorAgent | [psychological_profile_agent_functional_specifications.md](./psychological_profile_agent_functional_specifications.md) |
| **Psychological Recommendation** | Psychology-based preference prediction (Big Five, emotional state) | AudienceSimAgent, PerformanceMarketerAgent, PersonalizationEngineerAgent | [psychological_recommendation_agent_functional_specification.md](./psychological_recommendation_agent_functional_specification.md) |
| **Complex Problem Solving** | WHAT/WHY/HOW/DO/REVIEW structured methodology | All diagnostic agents (FactCheckerAgent, SMEAgent, JudgeAgent, OptimizationAgent) | [complex_problem_solution_process_model.md](./complex_problem_solution_process_model.md) |
| **Common Agent Structure** | Shared architectural pattern for all agents | All 114 agents | [common-agent-structure.svg](./common-agent-structure.svg) + [common-agent-structure.html](./common-agent-structure.html) |

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


Documentation changes for this system are reviewed as a repeated challenge cycle rather than a single proofread. A 100-pass reassessment can be grouped into the following bands:

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
| 66 | **WebResearchAgent** | Live web search, source ranking, citation extraction | Bing/Google/Brave search APIs; Common Crawl; Perplexity / GPTSearcher patterns | Source-grade per claim; citation precision; recency window hit | Faster + more sources than newsroom researcher at same precision | FactCheckerAgent, CitationAgent | ScriptwriterAgent (uncited claim) |
| 67 | **ArchiveResearchAgent** | Historical / academic / archival deep search | JSTOR, arXiv, PubMed, AP Archive, Getty, FOIA datasets | Primary-source ratio; archive-coverage breadth | Higher primary-source ratio than doc producer's research deck | FactCheckerAgent, SMEAgent | ScriptwriterAgent (secondary-source over-reliance) |
| 68 | **TrendIntelligenceAgent** | Detects emerging memes, sounds, formats with lead time | TikTok Creative Center, Trendpop, Tubular, Sensor Tower, Reddit/X firehose | Trend-prediction lead time vs viral peak; precision/recall on trend list | Earlier detection than social-strategist humans at higher precision | SocialStrategistAgent, CopywriterAgent | IdeationAgent (off-trend) |
| 69 | **CompetitorIntelligenceAgent** | What competing brands, creators, studios are shipping | Public ad libraries (Meta Ad Library, TikTok Top Ads); YouTube channel scrape; theatrical/streaming release trackers | Coverage % of named competitor set; novelty-of-our-output vs landscape | More comprehensive than agency strategy decks in blind comparison | BrandAgent, CreativeDirectorAgent | IdeationAgent (derivative) |
| 70 | **CitationAgent** | Normalizes sources; grades primary/secondary/tertiary | Chicago, APA, AP style guides; SPJ source-grading; CRAAP test | Citation format 100% valid; primary-source % ≥target | Lower formatting/grading error rate than newsroom copy desk | FactCheckerAgent, JournalistAgent | WebResearchAgent (weak source) |
| 71 | **InterviewSynthesisAgent** | Conducts/synthesizes practitioner interviews into instruction-tuning data | Otter/Rev transcripts; consent forms; SAG-AFTRA/WGA interview consent templates | Inter-coder agreement on theme extraction; consent-chain integrity | Faster + richer theme extraction than qualitative researcher | ResearchPIAgent (HiTL), ComplianceAgent | SMEAgent (mis-summarized expert) |
| 72 | **BenchmarkResearchAgent** | Monitors VBench, EvalCrafter, MT-Bench, FVD, CLIP-T leaderboards + new benchmarks | Papers-with-Code; HuggingFace leaderboards; AI conference proceedings | Coverage of active benchmarks; freshness ≤7 days | Faster + broader than human ML-research team | OptimizationAgents (any) | All AI-era agents (stale baselines) |

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | InstructionalDesignAgent + ScreenwriterAgent + StoryboardAgent | SMEAgent |
| Production | VoiceOverAgent + AnimatorAgent + ComposerAgent | DirectorAgent |
| Post | EditorAgent + SoundMixerAgent | AccessibilityAgent |
| Review | SMEAgent + BrandAgent | ComplianceAgent |
| Distribution | MarketingAgent + SEOAgent | AnalystAgent |
| 
…



### From `corpus/study/human_video_production_workflow.md` Copy: `sources/excerpts/human_video_production_workflow.md`.


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

| # | Sample Production | Typical Duration | Use Case | Crew / Roles Required |
|---|-------------------|------------------|----------|----------------------|
| 1 | Corporate explainer videos | 60–120s | Web, sales | Brand Strategist, Scriptwriter, Storyboard Artist, Motion Designer, VO Artist, Editor |
| 2 | Real estate virtual tours | 1–5 min | Listings | Real-Estate Photographer, 3D Scan Operator (Matterport), Drone Pilot, Editor, Colorist |
| 3 | Training & onboarding videos | 2–10 min | HR, L&D | Instructional Designer, SME, Scriptwriter, Presenter / Avatar, Editor, LMS Specialist |
| 4 | Meeting summary / recap videos | 1–3 min | Internal comms | Note-Taker / AI Transcriber, Editor, Motion Designer, Copywriter |
| 5 | LinkedIn thought leadership videos | 30–90s | Personal branding | Ghostwriter, Personal Brand Coach, Camera Op, Editor, Captioner |
| 6 | Pitch deck videos | 2–5 min | Fundraising | Founder / Presenter, Pitch Coach, Designer, Motion GFX, Editor, VO Artist |
| 7 | Investor update videos | 2–5 min | Quarterly | CFO / IR Lead, Scriptwriter, Designer, Editor, Compliance Reviewer |
| 8 | Annual report / earnings highlight videos | 1–3 min | IR / shareholders | IR Manager, Data Designer, Motion Designer, VO Artist, Legal Reviewer |
| 9 | HR policy & compliance training | 3–10 min | Mandatory training | Compliance Officer, Legal Reviewer, Instructional Designer, Presenter, Editor, Accessibility Specialist |
| 10 | Sales enablement walkthroughs | 2–5 min | Sales teams | Product Marketer, SME, Screen-Recordist, Editor, VO Artist |
| 11 | Internal CEO announcement videos | 1–3 min | All-hands | CEO / Talent, Speech Writer, Teleprompter Op, DoP, Editor, Comms Manager |
| 12 | Conference / event recap reels | 60–120s | Marketing | Event Videographer, Editor, Music Curator, Copywriter |
| 13 | Case study videos | 90–180s | Sales, marketing | Customer-Story Producer, Interviewer, DoP, Editor, Colorist, Copywriter |
| 14 | Recruitment / employer-branding | 60–120s | Hiring | Employer Brand Lead, Director, DoP, Editor, Composer, Cast (employees) |
| 15 | Quarterly all-hands recap videos | 2–5 min | Internal | Internal Comms Lead, Editor, Motion Designer, Captioner |

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
| 9 | **Colorist** | Final color grade, look consistency | Color theory, DaVinci Resolve / Baselight mastery, calibrated eye | Assistant Colorist 3–5 yrs at post house | Films, commercials, music videos, fashion | Stefan Sonnenfeld (Company 3), Dado Valentic; methods: ICA (International Colorist Academy) peer review, HPA Awards |
| 10 | **VFX Supervisor** | Designs and oversees visual effects | Compositing, 3D pipeline, on-set methodology | TD / Compositor → VFX Sup (10+ yrs); VES membership | Films, trailers, sci-fi, gaming | Joe Letteri (Weta), Paul Franklin (DNEG); methods: VES Awards judging, SIGGRAPH paper review |
| 11 | **2D / 3D Animator** | Animates characters, objects, motion | Timing, weight, squash & stretch, rigging fluency | Animation degree + 3–8 yrs studio | Bedtime stories, kids' edu, motion comics, gaming, explainers | Glen Keane, Pete Docter, Aaron Blaise; methods: ASIFA-Hollywood Annie Awards, animation dailies / "circle takes" |
| 12 | **Motion Graphics Designer** | Animated typography, infographics, lower thirds | After Effects mastery, design fundamentals, kinetic typography | 3–7 yrs at design studio | Explainers, ads, lyric videos, news, trailers | Erin Sarofsky, Kyle Cooper (Prologue), Karin Fong; methods: Motionographer reviews, AICP Next Awards |
| 13 | **Storyboard Artist** | Translates script into shot panels | Drawing speed, camera language, staging | Illustration background + 3–5 yrs in animation/film | Films, animation, ads, AI multi-scene stories | Sylvain Despretz, Marcos Mateu-Mestre (*Framed Ink*); methods: director shot-by-shot reviews, Pixar story trust |
| 14 | **Concept Artist** | Designs worlds, characters, props before production | Drawing, painting, design language, world-building | Art school + 3–8 yrs at studio/game co | Sci-fi, fantasy, gaming, archviz, trailers | Iain McCaig, Ryan Church, Karla Ortiz; methods: ArtStation peer critique, studio art-director reviews |
| 15 | **Production Designer** | Designs sets, locations, overall visual world | Archi
…



### From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


- **§14** is a literal **100-point hardening checklist** (10 themes × 10 checks). The system is not "done" until all 100 pass.
- The reference workflow already defines a **100-pass reassessment discipline** ([`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §1.4). This build plan inherits it: every milestone's acceptance is re-challenged across the five bands (traceability → architecture → handoffs → metrics → wording).
- Every agent you build must clear the system's own **L1/L2/L3 quality framework** and the **Q1–Q6 delivery QC mesh** (§5.5). Quality is recursive: the system that judges videos must itself be judged.



### From `corpus/root/project_starter_0.1.md` Copy: `sources/excerpts/project_starter_0.1.md`.


## Self-Evaluation & Critic Routine (Agent Self-Quality Assessment) — Research-Enhanced

**Core Workflow (Human-in-the-Loop)**
1. **Analysis Phase** (triggered by critic, periodic review, or after completing significant work):
   - Agent analyzes current skill usage, quality scores from self-reviews, relevance to recent tasks, duplication, or gaps.
   - Uses high-ranking sources (ECC patterns first, then best-practice insights).
2. **Suggestion Generation**:
   - Produces clear, structured suggestions:
     - **Add**: New skill proposal (name, purpose, source or draft content, why it's valuable).
     - **Update**: Specific improvements to an existing skill (with diff or before/after summary).
     - **Remove**: Reason for removal (low usage, superseded, quality issues) + impact assessment.
   - Suggestions are saved to a `suggestions/` folder or `pending-skill-changes.md` with unique IDs.
3. **Human Review & Confirmation**:
   - Human reviews the suggestions (via file, dashboard, or agent command like `/review-suggestions`).
   - Human confirms, rejects, or modifies (e.g., edits the suggestion file or replies with approval).
   - Only confirmed items proceed.
4. **Safe Application**:
   - After confirmation, the change is applied to the central `skills/` (and `rules/` if relevant).
   - The Cross-Agent Sync Layer then propagates the update to all agents' folders (`.claude/`, `.cursor/`, etc.).
5. **Audit & Rollback**:
   - All changes are logged with timestamp, reason, and human approver.
   - Easy rollback via git or a dedicated undo mechanism.



### From `corpus/root/project_starter_0.2.md` Copy: `sources/excerpts/project_starter_0.2.md`.


- ID  
- Action: add/update/remove  
- Target skill/rule/hook  
- Rationale  
- Evidence  
- Proposed diff/content  
- Risk assessment  
- Rollback plan  
- Confidence  
- Human approval field



### From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


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
| 52 | **SportsAnalystAgent / TelestratorOp** | Tactical breakdowns + diagrams | MIT Sloan papers; ESPN Stats & Info; Goldsberry analytics | Play-call accuracy; on-screen clarity score | Beats ex-athlete on tactical-prediction | SMEAgent (sport), JournalistAgent | EditorAgent (missed-replay), MotionGraphicsAgent (chart clarity) | Sports data APIs (StatsBomb, NBA Stats); telestration overlay tools; After Effects MCP | ReAct (fetch play data → annotate → render overlay) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 66 | **WebResearchAgent** | Live web search, source ranking, citation extraction | Bing/Google/Brave APIs; Common Crawl; Perplexity patterns | Source-grade per claim; citation precision; recency hit | Faster + more sources than newsroom researcher | FactCheckerAgent, CitationAgent | ScriptwriterAgent (uncited claim) | Brave/Google Search API; Jina Reader (web→markdown); source-quality classifier | ReAct (query → fetch → extract → grade → cite) |
| 67 | **ArchiveResearchAgent** | Historical / academic / archival deep search | JSTOR, arXiv, PubMed, AP Archive, Getty, FOIA | Primary-source ratio; archive-coverage breadth | Higher primary-source ratio than doc producer | FactCheckerAgent, SMEAgent | ScriptwriterAgent (secondary-source reliance) | JSTOR/arXiv/PubMed APIs; Getty Images API; FOIA request tools; OCR (Tesseract) | ReAct (formulate query → search archive → extract → grade source) |
| 68 | **TrendIntelligenceAgent** | Detects emerging memes, sounds, formats | TikTok Creative Center; Trendpop; Tubular; Reddit/X firehose | Prediction lead time vs peak; precision/recall on trend list | Earlier detection than human strategists at higher precision | SocialStrategistAgent, CopywriterAgent | IdeationAgent (off-trend) | TikTok Creative Center API; Reddit/X streaming APIs; Sensor Tower; Google Trends | ReAct + time-series anomaly detection |
| 69 | **CompetitorIntelligenceAgent** | What competitors are shipping | Meta Ad Library; TikTok Top Ads; YouTube scrape; release trackers | Coverage % of competitor set; our-novelty vs landscape | More comprehensive than agency strategy deck
…



### From `corpus/study/ui/project_creation_flow.md` Copy: `sources/excerpts/project_creation_flow.md`.


```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  PRODUCTION DRAFT: "Training Module"              Status: DRAFT (not launched)│
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── BRIEF EDITOR ──────────────────────────────────────────────────┐     │
│  │                                                                    │     │
│  │  Template: [F] Corporate Training    [Change]                      │     │
│  │                                                                    │     │
│  │  Title: [Training Module: Product Onboarding___]                   │     │
│  │                                                                    │     │
│  │  Vision:                                                           │     │
│  │  ┌──────────────────────────────────────────────────────────────┐  │     │
│  │  │ A 10-minute interactive training video that teaches new      │  │     │
│  │  │ employees how to use our product dashboard. Should feel      │  │     │
│  │  │ modern, friendly, and include knowledge checks.              │  │     │
│  │  └──────────────────────────────────────────────────────────────┘  │     │
│  │                                                                    │     │
│  │  Duration: [10 min]  Format: [16:9]  Tone: [friendly, professional]│     │
│  │  Learning objectives: [Tag: navigate dashboard, create report, ...]│     │
│  │  Assessment type: [Quiz after each section ▼]                      │     │
│  │  Delivery: ☑ SCORM  ☑ xAPI  ☐ Standalone video                    │     │
│  │                                                                    │     │
│  │  References from project: ☑ Brand Kit ☑ Voice "Brand Voice A"     │     │
│  │  Additional: [product_screenshots.zip] uploaded                    │     │
│  │                                                                    │     │
│  │  Budget for this production: $[35___]                              │     │
│  │  (Project pool remaining: $150 of $240)                            │     │
│  │                                                                    │     │
│  │  Last saved: 2 minutes ago (auto-save)                             │     │
│  │                                                                    │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌─── COST ESTIMATE PREVIEW ─────────────────────────────────────────┐     │
│  │                                                                    │     │
│  │  [🔄 Refresh Estimate]    Last estimated: 10 min ago               │     │
│  │                                                                    │     │
│  │  Estimated breakdown:                                              │     │
│  │  • Script + Instructional Design: ~$3                              │     │
│  │  • Avatar rendering (10 min): ~$12                                 │     │
│  │  • Voice synthesis: ~$4                                            │     │
│  │  • Motion graphics: ~$6                                            │     │
│  │  • Assessment generation: ~$2                                      │     │
│  │  • QC + Compliance: ~$3                                            │     │
│  │  • LMS packaging: ~$1                                              │     │
│  │  ─────────────────────────────                                     │     │
│  │  TOTAL ESTIMATE: ~$31 (±15%)                                       │     │
│  │                                                                    │     │
│  │  Agents needed: 18 │ Estimated duration: ~8 min                    │     │
│  │                                                                    │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌─── TEAM COMMENTS ON THIS DRAFT ───────────────────────────────────┐     │
│  │  Sarah (Reviewer): "Can we add a section on report exports?"      │     │
│  │  You: "Good idea, added to learning objectives"                    │     │
│  │  [+ Add comment]                                                   │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  ┌─── ACTIONS ───────────────────────────────────────────────────────┐     │
│  │                                                                    │     │
│  │  [ Save Draft ]    [ Share for Review ]    [ ▶ Launch Production ] │     │
│  │                                                                    │     │
│  │  ▶ Launch will:                                                    │     │
│  │    • Charge up to $35 from project budget pool                     │     │
│  │    • Activate 18 agents (Instructional, Avatar, Voice, LMS, ...)   │     │
│  │    • Begin production — you'll monitor in Production Console       │     │
│  │    • Estimated completion: ~8 minutes                              │     │
│  │                                                                    │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
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

```text
┌──────────────────────────────────────────────────────────┐
│  GATE APPROVAL — Phase: Pre-Production → Production       │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Gate: #2 (Script Lock + Storyboard Approval)            │
│  GateKeeperAgent Assessment: READY FOR REVIEW            │
│  JudgeAgent Score: 0.87/1.00                             │
│                                                          │
│  ┌─── CRITERIA CHECKLIST ──────────────────────────────┐ │
│  │  ✓ Script beat-sheet coverage: 12/12 (100%)         │ │
│  │  ✓ Dialogue distinctiveness: 0.42 (≥0.35)          │ │
│  │  ✓ Storyboard shot coverage: 24/24 (100%)          │ │
│  │  ✓ Budget estimate within cap: $85 ≤ $100          │ │
│  │  ⚠ Style consistency: 0.83 (target ≥0.85)          │ │
│  │  ✓ Compliance pre-check: PASS                       │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                          │
│  ┌─── ARTIFACTS FOR REVIEW ────────────────────────────┐ │
│  │  📄 screenplay_v4.fdx    [Preview]                  │ │
│  │  🖼  storyboard_panels/  [Preview Gallery]          │ │
│  │  📊 budget_estimate.json [View]                     │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                          │
│  Comments: ________________________________________      │
│                                                          │
│  [ ✓ APPROVE ]  [ ✗ REJECT ]  [ ↩ REQUEST CHANGES ]    │
│                                                          │
│  C2PA: Signing as [user@org]  ☑ Attach provenance       │
└──────────────────────────────────────────────────────────┘
```

| Template | Notable UI Differences |
|----------|----------------------|
| A — Viral Hook | Compressed timeline (all phases in 2–5 min); TrendIntel panel prominent; retention curve preview |
| B — UGC Ad | Performance targets panel; A/B variant grid; ROAS predictions visible |
| C — Animated Explainer | Learning objectives editor in brief; assessment builder; Bloom-level tagger |
| D — Personalized Birthday | Variable template editor; merge-field preview; batch render queue |
| E — AI Short Film | Full DAG visible; all 52 craft agents active; multiple gate approvals |
| F — Corporate Training | LMS packaging panel; SCORM preview; learner simulation results |
| G — Music Video | Beat-grid timeline; audio waveform overlay; choreography reference |
| H — AI Avatar | Avatar design studio; voice clone consent flow; lip-sync validation |
| I — Documentary | Archive research panel; source-grade tracker; interview synthesis |
| J — Feature Film | Episode/act navigation; series bible; full 114-agent roster; festival strategy |



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

| Principle | Implementation |
|-----------|---------------|
| **Free analysis** | Never charge for the assessment — only for generation |
| **Transparent scoring** | Show exactly what's wrong and how much better it can get |
| **User control** | Checkboxes — user picks which improvements to apply |
| **Budget tiers** | Quick fix / Recommended / Full — don't force all-or-nothing |
| **Before/after proof** | Side-by-side comparison with synced playback |
| **Non-destructive** | Original video is NEVER modified or deleted |
| **Iterative** | After first remake, user can click "Iterate Further" to refine more |
| **Shareable plan** | Export plan as PDF for team/client approval before spending |



## Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


## Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


## Provenance

- Master roster row va_id=33 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `C:\Project\va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.sme · va_id=33 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **SMEAgent (Subject-Matter Expert)** (`video.sme`, va_id=33, category `7-Edu`).

### Responsibility focus
Domain accuracy in target field

### Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: educational video AI, fact verification agents, multimodal accessibility (WCAG), domain-expert RAG, localization QA
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI edtech video, fact-checking AI, accessible media AI
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: AI for educational video, accessibility in media, domain expert AI agents

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

<!-- migration_capability_research · video.sme · v1 · 2026-07-13 -->
