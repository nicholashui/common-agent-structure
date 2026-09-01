# StoryboardAgent

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 14 |
| **pack_id** | `video.storyboard` |
| **category** | `3-Edit` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.storyboard/` |

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

Script → shot panels

## Knowledge distillation sources

*Framed Ink* (Mateu-Mestre); Pixar story-trust; Despretz boards

## Self-quality criteria

Shot-language fidelity; coverage completeness; staging clarity

## Surpass-human signal

Pixar story-trust pass rate at minutes per page

## Critique bus

- **Accepts critique from:** DirectorAgent, DoPAgent

- **Comments on:** ScriptwriterAgent (unfilmable), DirectorAgent (staging)

## Tools (design-time documentation)

DALL-E 3 / Midjourney API; panel-layout templates; Fountain parser

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

Self-Refine (director feedback loop)

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

```
USER BRIEF
    │
    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 1: INTENT & PLANNING                                           │
│ IntentAnalysisAgent (DIA) → PlannerAgent → ProducerAgent             │
│ Outputs: Parsed brief, phased DAG, budget, schedule                  │
│ Spec: intent_analysis_agent_functional_specification.md               │
└───────────────────────────────────┬─────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 2: CREATIVE DEVELOPMENT                                        │
│ DirectorAgent + ScreenwriterAgent + GCA (SSOR)                       │
│ Outputs: Script, shot list, lookbook, storyboards                    │
│ Specs: general_creative_agent_*, screenwriter_*                      │
└───────────────────────────────────┬─────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 3: PRE-PRODUCTION                                              │
│ CastingAgent + ProductionDesignAgent + ConceptArtistAgent            │
│ + CostumeAgent + ResearchAgent (domain knowledge)                    │
│ Outputs: Cast, sets, costumes, world bible, research dossiers        │
│ Spec: research_agent_functional_specification.md                     │
└───────────────────────────────────┬─────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 4: PRODUCTION (GENERATION)                                     │
│ PromptEngineerAgent + CinematographerAgent + TalentAgent             │
│ + SoundDesignAgent + ComposerAgent + VoiceOverAgent                  │
│ Outputs: Raw footage, audio stems, VO tracks, SFX                    │
│ Tech ref: video_generation_techology_should_learn_now.md             │
└───────────────────────────────────┬─────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 5: POST-PRODUCTION                                             │
│ EditorAgent + ColoristAgent + VFXSupervisorAgent + AnimatorAgent      │
│ + SoundMixerAgent + AIQAConsistencyAgent                             │
│ Outputs: Graded master, mixed audio, QC-passed final                 │
└───────────────────────────────────┬─────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 6: DELIVERY & OPTIMIZATION                                     │
│ SocialMediaStrategistAgent + PerformanceMarketerAgent                 │
│ + TrailerEditorAgent + PersonalizationEngineerAgent                   │
│ + OptimizationAgent (continuous improvement)                         │
│ Outputs: Platform-specific packages, campaigns, analytics            │
│ Spec: optimization_agent_functional_specification.md                 │
└─────────────────────────────────────────────────────────────────────┘
```



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

| Phase | Primary outputs | Mandatory gates |
|---|---|---|
| **Greenlight** | Approved brief, KPI targets, budget envelope, rights-risk register, scale profile | ProducerAgent, FinanceAgent, ComplianceAgent, PlannerAgent |
| **Pre-production packet** | Script lock, storyboard/lookbook, asset IDs, character/world bibles, consent state, continuity baselines | DirectorAgent, ScreenwriterAgent, Asset/Data Backbone, Continuity checks |
| **Production packet** | Shot prompts, camera plans, performance refs, plates, generated takes, render telemetry | PromptEngineerAgent / GeneratorOperator, CinematographerAgent, AIQAConsistencyAgent |
| **Post master** | Timelines, graded masters, stems, captions/subtitles, QC reports, outlet variants | EditorAgent, ColoristAgent, SoundMixerAgent, Accessibility checks |
| **Review and release pack** | AudienceSim results, legal review, provenance bundle, sign-off log, unresolved-risk list | ComplianceAgent, JudgeAgent, HumanInTheLoop when required |
| **Distribution package** | DCP, streaming mezzanine, broadcast master, archive package, trailer/social cutdowns, metadata bundle | Delivery-spec validation, accessibility validation, territorial rights validation |
| **Post-launch learning set** | Performance telemetry, corrections, defect log, benchmark deltas, retraining tickets | AnalystAgent, EvaluationHarnessAgent, PromptOptimizerAgent, model-improvement loop |

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | InstructionalDesignAgent + ScreenwriterAgent + StoryboardAgent | SMEAgent |
| Production | VoiceOverAgent + AnimatorAgent + ComposerAgent | DirectorAgent |
| Post | EditorAgent + SoundMixerAgent | AccessibilityAgent |
| Review | SMEAgent + BrandAgent | ComplianceAgent |
| Distribution | MarketingAgent + SEOAgent | AnalystAgent |
| Post-launch | AnalystAgent + InstructionalDesignAgent | AudienceSimAgent |

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | DirectorAgent + ScreenwriterAgent + StoryboardAgent + ConceptArtistAgent | ShowrunnerAgent |
| Production | PromptEngineerAgent / GeneratorOperator + VoiceCloneAgent + ComposerAgent | AIQAConsistencyAgent + LipSyncAgent |
| Post | EditorAgent + ColoristAgent + VFXSupervisorAgent | DirectorAgent |
| Review | DirectorAgent + LegalAgent (C2PA) | AvatarDesignAgent (consent) |
| Distribution | ProducerAgent + FestivalStrategistAgent | ComplianceAgent |
| Post-launch | DirectorAgent + AudienceSimAgent | CriticAgent (festival jury sim) |

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Development | ScreenwriterAgent + ProducerAgent + DirectorAgent + ConceptArtistAgent + CastingAgent | LegalAgent (IP, consent) |
| Pre-Production | StoryboardAgent + ProductionDesignAgent + CostumeAgent + ContinuityAgent | DirectorAgent |
| Production | PromptEngineerAgent / GeneratorOperator (pool) + VoiceCloneAgent + LipSyncAgent + ComposerAgent | AIQAConsistencyAgent + AvatarDesignAgent |
| Post | EditorAgent + VFXSupervisorAgent + ColoristAgent + SoundMixerAgent | DirectorAgent |
| Review | DirectorAgent + AudienceSimAgent + MPAAgent + LegalAgent (C2PA) | EthicsAgent |
| Distribution | SalesAgent + DistributorAgent + TrailerEditorAgent + MarketingAgent + ArchiveMasterAgent | ComplianceAgent |
| Post-launch | AnalystAgent + AwardsStrategistAgent + CriticAgent (festival/press sim) | ProducerAgent |

| Data family | Examples | Why it matters |
|---|---|---|
| **Narrative text** | Scripts, subtitles, transcripts, treatments, reviews | Trains story structure, dialogue, narrative compression, and claim extraction |
| **Visual material** | Storyboards, frames, plates, concept art, shot libraries | Grounds composition, continuity, lensing, and style transfer |
| **Audio material** | Dialogue, ADR, ambience, SFX libraries, score stems | Supports voice, sync, sound design, mix, and emotion modeling |
| **Structured metadata** | Budgets, schedules, rights records, view-through, CTR, ROAS, corrections | Connects creative output to business and compliance outcomes |
| **Multimodal pairs** | Video + audio + subtitle sets, prompt/output pairs, scene packets | Enables end-to-end generation, QA, and retrieval workflows |
| **Operational telemetry** | Queue depth, render latency, rerender reasons, cache hits, benchmark regressions | Turns production behavior into optimization and retraining signal |



### From `corpus/study/human_video_production_workflow.md` Copy: `sources/excerpts/human_video_production_workflow.md`.


- **Above-the-line**: Director, Producer, Showrunner, Screenwriter / Scriptwriter, Lead Cast / Talent
- **Camera & lighting**: Cinematographer (DoP), Camera Operator, Gaffer, Grip, Drone Pilot
- **Sound**: Sound Designer, Boom Operator, Production Mixer, Foley Artist, Composer, Voice-Over Artist
- **Art & design**: Production Designer, Art Director, Set Decorator, Costume Designer, Makeup / Hair Artist, Storyboard Artist, Concept Artist
- **Post-production**: Editor, Colorist, VFX Supervisor, Motion Graphics Designer, 2D / 3D Animator, Compositor, Sound Editor, Re-recording Mixer
- **AI-era specialists**: Prompt Engineer, AI Video Generator Operator, AI Voice / Lip-Sync Specialist, AI Avatar Designer, Model Fine-Tuner, AI QA / Consistency Reviewer
- **Distribution & strategy**: Producer / EP, Social Media Strategist, Copywriter, SEO/ASO Specialist, Community Manager, Localization / Subtitle Editor, Legal / Clearance, Brand / Marketing Manager

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

| # | Sample Production | Typical Duration | Style | Crew / Roles Required |
|---|-------------------|------------------|-------|----------------------|
| 1 | Short cinematic films / micro-movies | 15–60s | Cinematic | Director, Screenwriter, DoP, Production Designer, Cast, Editor, Colorist, Composer, Sound Designer |
| 2 | AI-generated multi-scene short stories | 1–5 min | Narrative | Story Writer, Storyboard Artist, AI Generator Operator, Consistency Reviewer, Editor, Composer, VO Artist |
| 3 | Animated bedtime stories | 3–10 min | Kids | Author, Illustrator, Animator, Narrator, Composer, Child-Safety Reviewer, Editor |
| 4 | Music videos & lyric videos | 1–4 min | Music | Director, DoP, Choreographer, Editor, Colorist, VFX Artist, Typography / Lyric Designer |
| 5 | Concept trailers (movie-style) | 30–90s | Cinematic | Director, Editor, Composer, Trailer Sound Designer, VO Artist, Colorist, Motion GFX |
| 6 | Fan-fiction visualizations | 1–5 min | Fan content | Writer / Fan-Author, Storyboard Artist, AI Generator Op, Editor, Composer, IP / Legal Reviewer |
| 7 | Mythology / folklore retellings | 2–10 min | Cultural | Cultural Consultant, Scriptwriter, Illustrator, Animator, Narrator, Composer, Editor |
| 8 | Anthology series episodes | 5–15 min | Series | Showrunner, Writers' Room, Director, DoP, Cast, Editor, Colorist, Composer, VFX, Sound Mixer |
| 9 | Animated motion comics | 30–90s | Motion comic | Comic Artist, Letterer, Motion Designer, VO Cast, Sound Designer, Editor |
| 10 | Interactive choose-your-own-adventure clips | 1–3 min | Interactive | Branching Narrative Writer, Game Designer, Director, Editor, Developer (interactive layer), Composer |
| 11 | Horror / suspense short shorts | 30–90s | Genre | Director, DoP, SFX Makeup Artist, Sound Designer, Composer, Editor, Cast |
| 12 | Sci-fi worldbuilding vignettes | 30–120s | Genre | Concept Artist, Production Designer, VFX Supervisor, Director, Composer, Editor |
| 13 | Parody / spoof trailers | 60–120s | Comedy | Comedy Writer, Director, Editor, VO Artist, Composer, Cast |
| 14 | Animated poetry / spoken-word visuals | 60–180s | Artistic | Poet, Narrator, Illustrator / Motion Artist, Composer, Editor |

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
| 13 | **Storyboard Artist** | Translates script into shot panels | Drawing speed, camera language, staging | Il
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



### From `corpus/study/ui/agent_management_ui.md` Copy: `sources/excerpts/agent_management_ui.md`.


```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT KNOWLEDGE: DirectorAgent (#1)                   [Save All Changes]   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TABS: [Configuration] [Playground] [Knowledge] [History] [Metrics]         │
│                                                                             │
├─── KNOWLEDGE SOURCES (what the agent knows) ────────────────────────────────┤
│                                                                             │
│  ┌─── 1. REFERENCE DOCUMENTS ────────────────────────────────────────┐      │
│  │  Documents embedded into agent's knowledge base (RAG retrieval)    │      │
│  │                                                                    │      │
│  │  ┌────────────────────────────────────────────────────────────┐    │      │
│  │  │ 📄 criterion_commentary_notes.md        │ 45KB │ Active  │    │      │
│  │  │ 📄 dga_seminar_transcripts.pdf          │ 120KB│ Active  │    │      │
│  │  │ 📄 scorsese_masterclass_notes.md        │ 32KB │ Active  │    │      │
│  │  │ 📄 shot_composition_guidelines.pdf      │ 18KB │ Active  │    │      │
│  │  │ 📄 genre_pacing_priors.json             │ 5KB  │ Active  │    │      │
│  │  │ 📄 my_custom_style_guide.md             │ 8KB  │ NEW ✨  │    │      │
│  │  └────────────────────────────────────────────────────────────┘    │      │
│  │                                                                    │      │
│  │  [+ Upload Document]  [+ Paste Text]  [+ Import from URL]         │      │
│  │                                                                    │      │
│  │  ℹ️ These docs are chunked, embedded, and stored in vector DB.     │      │
│  │    Agent retrieves relevant chunks during task execution.          │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  ┌─── 2. FEW-SHOT EXAMPLES ─────────────────────────────────────────┐      │
│  │  Input/output pairs that teach the agent by example                │      │
│  │                                                                    │      │
│  │  ┌────────────────────────────────────────────────────────────┐    │      │
│  │  │ Example 1: "Romantic comedy - park scene"                  │    │      │
│  │  │ Input: Scene description + mood reference                   │    │      │
│  │  │ Expected output: Shot intent JSON (golden example)          │    │      │
│  │  │ [View] [Edit] [Delete]                                      │    │      │
│  │  ├────────────────────────────────────────────────────────────┤    │      │
│  │  │ Example 2: "Action sequence - car chase"                   │    │      │
│  │  │ Input: Scene + storyboard panels                            │    │      │
│  │  │ Expected output: Shot intent with rapid cuts                │    │      │
│  │  │ [View] [Edit] [Delete]                                      │    │      │
│  │  ├────────────────────────────────────────────────────────────┤    │      │
│  │  │ Example 3: "Horror - reveal scene"                          │    │      │
│  │  │ Input: Script excerpt + tension notes                       │    │      │
│  │  │ Expected output: Slow build, static camera, minimal cuts    │    │      │
│  │  │ [View] [Edit] [Delete]                                      │    │      │
│  │  └────────────────────────────────────────────────────────────┘    │      │
│  │                                                                    │      │
│  │  [+ Add Example Manually]  [+ Import from Playground Run]          │      │
│  │  [+ Generate Examples from Document]                               │      │
│  │                                                                    │      │
│  │  ℹ️ Few-shot examples are injected into the prompt when the task   │      │
│  │    type matches. More examples = better consistency.               │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  ┌─── 3. CORRECTIONS & FEEDBACK ─────────────────────────────────────┐      │
│  │  Past mistakes + what the correct behavior should have been        │      │
│  │                                                                    │      │
│  │  ┌────────────────────────────────────────────────────────────┐    │      │
│  │  │ Correction 1: (from Production "Luna", Shot 3)             │    │      │
│  │  │ ❌ Agent did: Used handheld camera for intimate scene       │    │      │
│  │  │ ✓ Should have: Static tripod with slow push for intimacy   │    │      │
│  │  │ Why: "Handheld implies urgency, not intimacy. For quiet    │    │      │
│  │  │       emotional scenes, static or slow dolly is standard." │    │      │
│  │  │ Source: User feedback │ Date: 2 days ago                    │    │      │
│  │  ├────────────────────────────────────────────────────────────┤    │      │
│  │  │ Correction 2: (from Production "Spark", Shot 7)            │    │      │
│  │  │ ❌ Agent did: 16:9 framing for TikTok content              │    │      │
│  │  │ ✓ Should have: 9:16 vertical for social-first delivery     │    │      │
│  │  │ Why: "Always check platform target before framing."        │    │      │
│  │  │ Source: Auto-detected from gate rejection │ Date: 5d ago    │    │      │
│  │  └────────────────────────────────────────────────────────────┘    │      │
│  │                                                                    │      │
│  │  [+ Add Correction Manually]  [+ Import from Production Failures]  │      │
│  │                                                                    │      │
│  │  ℹ️ Corrections are stored in Reflexion-style episodic memory.     │      │
│  │    Agent checks "what went wrong before" on similar tasks.         │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  ┌─── 4. CUSTOM RULES (Constitutional Additions) ────────────────────┐      │
│  │  Hard rules the agent MUST follow (beyond the system prompt)       │      │
│  │                                                                    │      │
│  │  Rule 1: "Never use Dutch angle unless genre is horror/thriller"   │      │
│  │  Rule 2: "Always include at least one establishing shot per scene" │      │
│  │  Rule 3: "Maximum shot duration: 12 seconds for social content"    │      │
│  │  Rule 4: "When budget < 20%, prefer static camera (cheaper gen)"   │      │
│  │                                                                    │      │
│  │  [+ Add Rule]                                                      │      │
│  │                                                                    │      │
│  │  ℹ️ Rules are injected as constitutional constraints. Agent         │      │
│  │    self-checks against these rules during every self-refine loop.  │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  ┌─── 5. EVALUATION BENCHMARKS ──────────────────────────────────────┐      │
│  │  Test cases to measure if knowledge improvements actually work     │      │
│  │                                                                    │      │
│  │  Benchmark suite: 12 test cases                                    │      │
│  │  Last run: 2 days ago │ Score: 9/12 passing (75%)                  │      │
│  │  After adding new knowledge: [▶ Run Benchmark] to see improvement  │      │
│  │                                                                    │      │
│  │  ┌─────────────────────────────────────────────────────────────┐   │      │
│  │  │ Test │ Input              │ Expected    │ Last Result │ Pass │   │      │
│  │  ├──────┼────────────────────┼─────────────┼─────────────┼──────┤  │      │
│  │  │ 1    │ Rom-com park scene │ Wide→Medium │ Wide→Medium │ ✓    │   │      │
│  │  │ 2    │ Horror reveal      │ Static, slow│ Static, slow│ ✓    │   │      │
│  │  │ 3    │ Action chase       │ Fast cuts   │ Fast cuts   │ ✓    │   │      │
│  │  │ 4    │ TikTok 9:16        │ Vertical    │ Horizontal  │ ✗    │   │      │
│  │  │ ...  │                    │             │             │      │   │      │
│  │  └─────────────────────────────────────────────────────────────┘   │      │
│  │                                                                    │      │
│  │  [+ Add Test Case]  [+ Import from Playground]  [▶ Run All Tests]  │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```



### From `corpus/study/ui/backend_agent_management.md` Copy: `sources/excerpts/backend_agent_management.md`.


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



### From `corpus/study/ui/RETHINK_100_IMPROVEMENTS.md` Copy: `sources/excerpts/RETHINK_100_IMPROVEMENTS.md`.


| # | Improvement | Source Paper | Impact |
|---|------------|-------------|--------|
| 31 | Iterative script verification | FilmAgent | Major |
| 32 | Hierarchical CoT planning | MovieAgent | Major |
| 33 | Character bank across shots | MovieAgent | Major |
| 34 | Shared world model | ShareVerse | Major |
| 35 | Cinematic language grammar (shot transitions) | arXiv:2604.09195 | Medium |
| 36 | Dedicated boards per stage | AnimAgents | Medium |
| 37 | Hybrid workforce checkpoints | Sima 1.0 | Already have (gates) |
| 38 | Multi-turn agent conversation | FilmAgent revision | Major |
| 39 | Sound Director supervision loop | arXiv:2503.07217 | Medium |
| 40 | Cross-modal temporal state sharing | OmniAgent | Major |
| 41 | Graph-based memory (not just vector) | Knowledge graphs | Medium |
| 42 | Act/sequence/beat hierarchy in DAG | MovieAgent structure | Medium |
| 43 | Shot-adjacency awareness | Cinematic language paper | Major |
| 44 | Location scouting focus | MovieAgent | Already have (ProductionDesign) |
| 45 | Character-aware subtitle generation | MovieAgent | Medium |
| 46 | Distinct pipeline for multi-scene vs 1-shot | OmniAgent | Major |
| 47 | Storyboard panels as control images for gen | AnimAgents + ControlNet | Major |
| 48 | Reference frame bank (approved frames guide later) | Character consistency | Major |
| 49 | Emotion curve verification post-assembly | EmotionalArcAgent loop | Medium |
| 50 | Retention prediction on final cut pre-delivery | RetentionOptimizer timing | Medium |



### From `corpus/study/ui/ui_design.md` Copy: `sources/excerpts/ui_design.md`.


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

```text
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
```

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

- Master roster row va_id=14 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `C:\Project\va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.storyboard · va_id=14 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **StoryboardAgent** (`video.storyboard`, va_id=14, category `3-Edit`).

### Responsibility focus
Script → shot panels

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

<!-- migration_capability_research · video.storyboard · v1 · 2026-07-13 -->
