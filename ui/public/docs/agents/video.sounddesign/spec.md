# video.sounddesign — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/video.sounddesign/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "video.sounddesign",
  "status": "registered",
  "role": "SoundDesignAgent (VA Domain Pack)",
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
      "video.soundmixer"
    ],
    "outputs": [
      "video.judge",
      "video.editor",
      "video.composer"
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
  "va_id": 19,
  "va_name": "SoundDesignAgent",
  "va_category": "4-Snd",
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

# SoundDesignAgent

> Self-contained VA Domain Pack agent on host common-agent-swarm-ops.
> Pack agent ID matches pure VA/generic taxonomy: `video.sounddesign`.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 19 |
| **pack_id** | `video.sounddesign` |
| **upstream_name** | SoundDesignAgent |
| **category** | `4-Snd` |
| **domain_id** | `video` |
| **previous_common_id** | `video.sound_designer` |
| **status** | `registered` |
| **maturity** | L0 / non-active |
| **taxonomy** | Pure VA Domain Pack (via generic pack agents) |
| **folder** | `business/video/agents/video.sounddesign/` |

## Responsibility

Ambience, foley, SFX

Host role binding: `SoundDesignAgent (VA Domain Pack)`. Design-time VA table content below is historical and non-binding for activation.

### Responsibility (from VA table)

Ambience, foley, SFX

### Knowledge distillation sources (historical)

BBC SFX library; MPSE Golden Reel; Burtt/Lievsay notes

### Self-quality criteria (historical)

Spectral diversity; sync ≤±1 frame; loudness -23 LUFS

### Surpass-human signal (historical)

Wins MPSE pairwise on horror/sci-fi

### Critique bus (historical)

- **Accepts critique from:** DirectorAgent, MixerAgent

- **Comments on:** EditorAgent (FX clash), ComposerAgent (masking)

### Tools design-time notes (historical, non-activating)

ElevenLabs Sound FX API; Freesound; FFmpeg spectral analysis; Dolby.io loudness API

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

### Architecture pattern (historical)

ReAct (search SFX lib → validate sync → mix)

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

- Prompt reference: `video.prompt.sounddesign.v1`
- Rubric reference: `video.rubric.sounddesign.v1`
- Critique edges: `{"inputs": ["video.critic"], "outputs": ["video.judge"]}`
- Max refinement: `3`
- VA table quality criteria retained under Provenance and Identity surface above.

## Runtime binding

Authoritative fail-closed host configuration:

```json
{
  "agent_id": "video.sounddesign",
  "allowed_tools": [
    "media.stub",
    "media.elevenlabs"
  ],
  "budget_policy": {
    "max_input_tokens": 2048,
    "max_output_tokens": 1024,
    "max_tool_requests": 4
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
    "network_access": true,
    "provider": "media_host"
  },
  "production_activation_requested": true,
  "prompt_reference": "video.prompt.sounddesign.v1",
  "role": "SoundDesignAgent (VA Domain Pack)",
  "rubric_reference": "video.rubric.sounddesign.v1",
  "schema_version": "1.0",
  "status": "registered",
  "va_id": 19,
  "va_name": "SoundDesignAgent",
  "va_category": "4-Snd"
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

- Pack agent ID `video.sounddesign` is aligned to pure VA Domain Pack / generic pack taxonomy (Agent IDs ≈ VA tables).
- Previous common inventory ID `video.sound_designer` is historical mapping only.
- Upstream design body below is **historical and non-binding**; local `agent_spec.json` is authoritative.
- Full VA/generic SPEC depth retained for offline design fidelity (including category roster rows and common agent structure when present upstream).

### VA Domain Pack specification body (historical and non-binding)

```text
SoundDesignAgent

> **Self-contained agent definition** for host `upstream-generic-pack`. Body text is embedded from in-pack corpus and upstream-va-design when available. Do not require external repos to understand this agent.

Identity

| Field | Value |
|-------|-------|
| **va_id** | 19 |
| **pack_id** | `video.sounddesign` |
| **category** | `4-Snd` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.sounddesign/` |

Category roster section (full, from agents.md)

_The following is the complete category section from the master roster (includes peers in the same craft category)._


4. Sound & Music Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 19 | **SoundDesignAgent** | Ambience, foley, SFX | BBC SFX library; MPSE Golden Reel; Burtt/Lievsay notes | Spectral diversity; sync ≤±1 frame; loudness -23 LUFS | Wins MPSE pairwise on horror/sci-fi | DirectorAgent, MixerAgent | EditorAgent (FX clash), ComposerAgent (masking) | ElevenLabs Sound FX API; Freesound; FFmpeg spectral analysis; Dolby.io loudness API | ReAct (search SFX lib → validate sync → mix) |
| 20 | **ComposerAgent** | Original score | MAESTRO + film-score corpora; ASCAP/BMI; Zimmer/Hildur sessions | Cue-to-emotion alignment (valence/arousal regression); thematic recurrence | Wins blind pairwise on emotional-fit vs working composers | DirectorAgent, EditorAgent (music cuts) | EditorAgent (cut interrupts cue), SoundDesignAgent (mask) | Udio/Suno music gen API; MIDI toolchain; stem-separation (Demucs); loudness meter | Self-Refine + Emotional-Arc validation (biosignal proxy) |
| 21 | **VoiceOverAgent** | Narration, character VO, ad reads | SOVAS reels; consented voice corpora; Wolfson/Cashman coaching | Prosody match; pronunciation 100%; emotion tag match | Beats junior VO in blind preference; matches senior on emotion | DirectorAgent, BrandAgent | ScriptwriterAgent (unspeakable phrasing) | ElevenLabs v3 TTS + voice cloning; Resemble.AI; pronunciation lexicon API | LLM-as-Judge (MOS scoring rubric) |
| 22 | **SoundMixerAgent (Re-recording)** | Final mix; deliverables (5.1/Atmos) | CAS Awards; Atmos specs; broadcast loudness standards | LUFS target; STOI ≥0.85; spec-deliverable pass | CAS spec on first pass without rework | EditorAgent, SoundDesignAgent, AccessibilityAgent | SoundDesignAgent (over-design), ComposerAgent (level) | Dolby Atmos Renderer API; LUFS/loudness measurement tools; DaVinci Fairlight MCP | Constitutional AI (constitution: broadcast-spec rules) |

---


Responsibility

Ambience, foley, SFX

Knowledge distillation sources

BBC SFX library; MPSE Golden Reel; Burtt/Lievsay notes

Self-quality criteria

Spectral diversity; sync ≤±1 frame; loudness -23 LUFS

Surpass-human signal

Wins MPSE pairwise on horror/sci-fi

Critique bus

- **Accepts critique from:** DirectorAgent, MixerAgent

- **Comments on:** EditorAgent (FX clash), ComposerAgent (masking)

Tools (design-time documentation)

ElevenLabs Sound FX API; Freesound; FFmpeg spectral analysis; Dolby.io loudness API

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

Architecture pattern

ReAct (search SFX lib → validate sync → mix)

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


Document: `study/podcast_agent_functional_specifcation.md`

_Embedded from `corpus/study/podcast_agent_functional_specifcation.md`. Also stored at `sources/study/podcast_agent_functional_specifcation.md` under this agent folder._


 

Podcast Production and AI Agent Systems

Part 1: Traditional Podcast Host Workflow

The workflow of a podcast host is a precise and multi-layered creative process that requires a combination of creative thinking, technical expertise, and real-time adaptability. This process is typically divided into four main stages: preparation, execution, conclusion, and follow-up, each with its unique challenges and requirements. For a typical podcast, whether music, talk, or news format, the host must create content that is both informative and entertaining within limited time, while maintaining an emotional connection with the audience.

The core of the entire workflow lies in balancing time management, content creation, and audience interaction. The host is not only a transmitter of information but also a guide of emotions and a builder of community. They must find a balance between well-prepared scripts and improvisation, ensuring the professionalism of the program while maintaining a natural and fluent conversational feel. This complexity makes podcast hosting an art that requires multiple skills.

 

1. Preparation Phase: Foundation for Program Success

The preparation phase is the most critical part of the entire radio production process, typically starting one to two days before the program airs. The quality of this phase directly determines the program's success, as thorough preparation not only ensures the richness and accuracy of the content but also allows the host to remain calm and professional when facing unexpected situations.

Research and planning are the core of the preparation phase. The host needs to dig deeply into the day's hot topics like a seasoned journalist, which involves not only browsing major news websites and social media platforms but also analyzing the social context and audience interests behind these topics. Excellent hosts will build their own information networks, including reliable sources, expert contacts, and loyal listener communities, which are important channels for obtaining exclusive information and in-depth insights.

When determining the program theme, the host must consider multiple factors: the importance of current events, audience interest preferences, the program's positioning and brand image, and differentiation from other media. This decision-making process often requires in-depth discussions with the production team, using brainstorming to uncover the most attractive angles and presentation methods. Team meetings are not only platforms for information exchange but also venues for creative collisions, where every member offers suggestions and ideas from their professional perspectives.

Script writing and rehearsal are the process of turning creativity into actual content. Unlike TV programs, radio scripts need to place greater emphasis on the rhythm and auditory effects of language, as listeners can only receive information through sound. When writing the script, the host must consider variations in tone, timing of pauses, and how to convey emotions through voice. This process often requires repeated revisions and adjustments until the most suitable expression is found.

Time control is the lifeline of radio programs. The duration of each segment must be precisely calculated, not only considering the completeness of the content but also leaving sufficient flexibility to handle unexpected situations. Experienced hosts will mark detailed time points in the script and prepare multiple versions of content for adjustments when needed. This precise time management ability is a key indicator distinguishing amateur from professional hosts.

Preparation for audience interaction is equally important. Modern radio programs increasingly emphasize two-way communication with listeners, and hosts need to collect audience opinions and questions through various channels. This includes not only traditional phone hotlines but also digital platforms such as social media, radio apps, and website comments. Hosts must learn to screen and organize this information, identifying the most representative and discussion-worthy content.

 

2. Execution Phase: Perfect Integration of Creativity and Technology

The execution phase is the climax of the entire broadcast production process and the moment that most tests the host's comprehensive abilities. In this stage, all preparatory work is transformed into actual program content, and the host must perfectly blend pre-planned content with real-time events within limited time, creating a broadcast experience that is both in-depth and engaging.

The pre-program preparations, though only five to ten minutes long, are the critical moment that determines the success or failure of the entire show. After entering the studio, the host first conducts a final check of the technical equipment to ensure all audio devices are in optimal condition. This includes not only microphone volume adjustment and sound quality testing, but also settings for each channel on the mixing console, the operational status of computer software, and whether the communication system with the control room is functioning normally. Any technical issues must be resolved at this stage, as major adjustments become difficult once the program starts.

The design and delivery of the opening remarks often determine the audience's first impression of the entire program. An excellent host will adjust their opening style based on the day's theme and atmosphere. Sometimes, they need to enthusiastically welcome listeners; other times, use a steady tone to handle serious topics. The opening not only introduces the main content of the program but also establishes an emotional connection with the audience, making them willing to continue listening.

The main content playback stage is the core part of the program, typically occupying eighty percent of the total program duration. In this stage, the host needs to demonstrate excellent multitasking abilities, managing multiple tasks simultaneously. Information sharing must be accurate and vivid; the host must convert complex information into language that listeners can easily understand while maintaining the content's interest. Inserting music and sound effects not only regulates the program's rhythm but also creates an appropriate atmosphere, enhancing the listeners' emotional experience.

Guest interviews are an important component of many broadcast programs and the segment that most tests the host's skills. A successful interview requires the host to have keen observation, flexible adaptability, and deep communication skills. The host must guide the conversation direction while giving guests ample space to express themselves, avoiding over-dominance or complete passivity. Probing techniques are especially important, delving deeply into valuable information without making guests feel uncomfortable or defensive.

The listener interaction segment is an indispensable part of modern broadcast programs; it not only increases participation but also provides real-time feedback and new content sources. When handling listener calls or messages, the host needs to quickly judge the suitability and value of the content and provide appropriate responses within limited time. This process requires extremely strong real-time judgment and communication skills, as each listener has a different background and expression style; the host must adapt quickly and find the best interaction method.

Transitions between advertisements and program content are a frequently overlooked but extremely important skill in broadcast programs. An excellent host can make ad insertions feel natural and unobtrusive, even cleverly integrating ad content with the program theme to create a better listening experience. This skill requires long-term practice and experience accumulation and is one of the key standards distinguishing professional from amateur hosts.

Crisis management ability is a core skill that every broadcast host must possess. Technical failures, sudden guest absences, or content errors may occur during live broadcasts. Experienced hosts prepare multiple contingency plans in advance and can remain calm under pressure, quickly finding solutions. This ability requires not only technical knowledge but also psychological resilience and creative thinking support.

 

3. Ending Phase: The Art of Perfect Closure

Although the ending phase is relatively short in duration, its importance cannot be underestimated. A brilliant conclusion not only draws a perfect close to the entire program but also leaves a lasting impression in the listeners' minds, prompting them to look forward to the next episode. The work in this phase includes not only the on-site conclusion of the program but also subsequent production and file management tasks.

The design of the program's conclusion needs to consider multiple factors. First is the content summary, where the host uses concise and powerful language to review the program's key content, helping listeners organize and remember crucial information. This summary should not be a simple repetition but rather an elevation and refinement, linking scattered information points into a complete story or viewpoint. At the same time, the host needs to preview the next episode, sparking listeners' anticipation and motivation to keep tuning in.

Emotional closure is equally important. An excellent host will choose an appropriate emotional tone to end the program based on its content and atmosphere. For lighthearted and fun content, the conclusion should maintain this positive vibe; for discussions on serious social issues, the ending should leave listeners with space for reflection. This guidance and control of emotions demonstrate the host's professional素养 and humanistic care.

Inviting listener feedback is a key component of modern radio program conclusions. The host needs to clearly inform listeners how to interact with the program, including phone numbers, social media accounts, email addresses, and other contact methods. More importantly, it should make listeners feel that their opinions and participation are valued and welcomed—this interactivity is a critical factor in building a loyal listener base.

The recording of program logs, though seemingly simple, is of great significance for the program's long-term development. Detailed records should include not only basic statistical data, such as listenership rates, call volumes, and social media interactions, but also qualitative information like special events during the program, listener reactions, and technical issues. These records provide valuable reference materials for future program improvements and strategy adjustments.

For non-live programs, the post-production phase offers opportunities to further refine the content. Audio editing includes not only technical processing, such as noise removal, volume balancing, and sound quality optimization, but also content adjustments, like deleting lengthy pauses, correcting slip-ups, and adding sound effects. Modern audio editing software like Adobe Audition provides powerful features, but using these tools requires professional technical knowledge and extensive experience.

The post-production phase also involves considerations for multi-platform distribution. The same program content may need to be adapted to different platforms and formats, such as full-version podcasts, highlight clips for social media, or text-based blog articles. Each format has its specific audience and dissemination characteristics, requiring corresponding adjustments and optimizations.

 

4. Follow-up Phase: Continuous Improvement Cycle

The follow-up phase is the most easily overlooked link in the entire broadcast production process, yet it is the most critical for long-term success. The work in this phase not only determines the final quality of the current program but also lays the foundation for the improvement and development of future programs. Excellent broadcast professionals understand that every program is an opportunity for learning and growth, and systematic follow-up work is a necessary condition for achieving this growth.

Data collection and analysis have become increasingly important in the modern broadcast industry. Traditional listenership surveys still have their value, but the digital age provides more diverse and real-time data sources. Online streaming platforms can provide detailed listening behavior analysis, including when listeners start listening, where they stop, and which segments are replayed. Social media interaction data can reflect listeners' emotional responses and engagement levels. Radio app usage data can show listeners' preferences and habits.

The value of this data lies not in the quantity itself, but in the listener behavior patterns and preference trends it reveals. Professional hosts and production teams regularly analyze this data to find patterns and insights. For example, if a high listener drop-off rate is found in a certain time slot, the content arrangement and presentation in that slot need to be reviewed. If a topic sparks particularly heated discussion, it can be considered for deeper exploration in future programs.

Collecting and analyzing listener feedback is equally important. Modern listeners have multiple channels to express their opinions, including phone calls, emails, social media comments, website reviews, and more. Each channel may have listener groups with different characteristics and preferences, so they need to be analyzed and handled separately. More importantly, a systematic feedback processing mechanism must be established to ensure that valuable suggestions are adopted and implemented.

Self-review is an important pathway for professional growth. Experienced hosts develop a habit of regular self-assessment, not only focusing on technical performance such as speech rate, pronunciation, and rhythm control, but also reflecting on content issues such as topic selection, viewpoint expression, and interaction handling. This self-review requires honesty and objectivity, recognizing one's strengths and progress while bravely facing shortcomings and problems.

Team collaboration plays a crucial role throughout the entire workflow. Modern broadcast programs are rarely the product of solo efforts but require close cooperation among multiple professional roles, including hosts, producers, engineers, and editors. Each role has its professional domain and responsibilities, but they also need to understand and support the work of other roles. Effective team collaboration not only improves work efficiency but also sparks creativity and innovation.

Irregular working hours are a characteristic of the broadcast industry, especially for live program hosts. This not only includes broadcast times that may be in the morning, late at night, or on weekends, but also sudden news or special events that may require temporary adjustments to the program schedule. Therefore, broadcast professionals need good time management skills and physical fitness, as well as understanding and support from family and friends.

The success of the entire workflow requires close coordination and continuous optimization across all phases. From thorough research and planning in the preparation phase, to professional performance and flexible response in the execution phase, to perfect wrap-up and post-production in the conclusion phase, and finally to in-depth analysis and continuous improvement in the follow-up phase, every link is indispensable. This systematic approach not only ensures the quality of individual programs but also drives the long-term development and success of the entire program brand.

Part 2: Improvement, Progress, and Enhancement Mechanisms

The professional development of broadcast program hosts is a continuous process that needs to occur simultaneously across multiple levels, including personal skills, team collaboration, and system optimization. This need for continuous improvement stems from the rapid changes in the media environment, the constant rise in listener expectations, and the new opportunities and challenges brought by technological advancements. Successful broadcast professionals understand that stagnation means falling behind, and only through systematic improvement mechanisms can they maintain an advantage in the highly competitive media market.

The improvement mechanisms in the modern broadcast industry typically adopt the PDCA cycle model (Plan-Do-Check-Act), which ensures the systematic and effective nature of improvement work. The planning phase requires setting specific improvement goals based on data analysis and market insights; the execution phase requires transforming plans into concrete actions and practices; the check phase evaluates improvement effects through various indicators and feedback; the action phase adjusts strategies and methods based on check results. This cyclical and iterative process ensures the continuity and depth of improvement work.

 

1. Professional Growth at the Individual Level

Improvements at the individual level form the foundation of the entire improvement system, as the quality of a radio program ultimately references the host's personal abilities and performance. This improvement not only includes enhancing technical skills but also involves refining knowledge structures, optimizing thinking patterns, and building a personal brand.

Self-assessment and reflection are the starting points for personal growth. Professional radio hosts establish systematic self-assessment mechanisms, regularly reviewing their performance in various aspects. This assessment should not rely solely on subjective feelings but should incorporate objective methods such as playback of recordings, data analysis, and feedback from others. By listening to their own program recordings, hosts can identify many issues unnoticed during live broadcasts, such as speaking too quickly, improper pauses, monotonous tone, and so on. At the same time, they should pay attention to content-related issues, such as whether the logical structure is clear, whether viewpoints are expressed accurately, and whether interactions are handled appropriately.

Establishing a detailed growth log is an important tool for self-reflection. This log not only records basic information and performance evaluations for each program but should also include learning insights, improvement plans, and goal setting. Through long-term recording and review, hosts can clearly see their growth trajectory, identify areas needing focused improvement, and formulate corresponding learning and practice plans.

Skills training is an important pathway for personal development. The radio industry involves multiple professional fields, including language expression, audio technology, media theory, psychology, sociology, and more. Hosts need to select appropriate training courses and learning opportunities based on their career planning and development needs. Traditional face-to-face workshops and seminars still hold value, especially in practical skills and interpersonal communication. At the same time, online learning platforms provide more flexible and diverse learning options, allowing hosts to choose suitable courses according to their schedules and learning pace.

Voice training is one of the most basic and important skills for radio hosts. This not only includes accuracy and clarity of pronunciation but also involves variations in tone, rhythm control, emotional expression, and more. Professional voice training requires long-term practice and guidance; many successful hosts continue to receive regular coaching from voice coaches even in the later stages of their careers. Modern voice training also incorporates technological tools, such as speech analysis software that provides objective voice quality assessments, helping hosts improve their performance more precisely.

Health management holds special importance for radio hosts. The vocal cords are the host's most important tool and require special protection and maintenance. This not only includes avoiding behaviors harmful to the vocal cords, such as smoking, excessive drinking, and shouting loudly, but also proactive care measures like appropriate vocal exercises, adequate hydration, and reasonable rest schedules. Mental health is equally important; the stress and irregular schedules of radio work can impact psychological state, so hosts need to learn stress management and emotional regulation techniques.

 

2. Collaborative Development at the Team and Organizational Levels

Improvement mechanisms at the team level recognize that broadcast programs are the result of collective creation, requiring close coordination among multiple professional roles. This improvement not only focuses on enhancing individual capabilities but also emphasizes optimizing team collaboration efficiency, perfecting communication mechanisms, and stimulating collective creativity. Successful broadcast teams often have clear role divisions, smooth communication channels, and shared quality standards.

Feedback loop mechanisms are the core tools for team improvement. Regular team meetings serve not only as platforms for work coordination but also as important venues for experience sharing and problem-solving. In these meetings, team members can openly discuss issues encountered during program production, share successful experiences and innovative ideas. The producer, as the team's coordinator, needs to foster an open and constructive discussion atmosphere, encouraging every member to actively participate and contribute. This regular reflection and discussion helps identify and resolve issues promptly, preventing small problems from escalating into major crises.

Audience surveys and feedback collection are important channels for understanding program effectiveness and market reactions. Modern audience survey methods have far surpassed traditional phone interviews, incorporating various digital tools and analysis methods. Online questionnaires can quickly collect large amounts of quantitative data, focus group discussions can deeply understand audience attitudes and preferences, and social media monitoring can instantly capture changes in public opinion. More importantly, a systematic feedback analysis mechanism must be established to integrate this scattered information into valuable insights and recommendations.

Data-driven optimization strategies have become standard practice in the modern broadcasting industry. Various analysis tools provide detailed listening behavior data, including trends in listenership changes, audience retention analysis, performance comparisons across different time slots, and more. This data not only objectively evaluates program performance but also reveals deep patterns in audience behavior. For example, analyzing audience drop-off at different time points can identify weak links in the program; comparing performance across different content types can optimize the program's content structure and scheduling.

A/B testing methods are increasingly widely used in the broadcasting industry. This scientific experimental approach can test different program elements, such as opening styles, music selections, ad insertion methods, etc. By broadcasting two slightly different versions simultaneously and comparing their effects, teams can make improvement decisions based on objective data rather than relying solely on subjective judgment. This method is particularly suitable for testing new creative ideas and improvement measures.

Technological upgrades and innovations are key factors in maintaining competitive advantage. Broadcast technology is advancing rapidly, from traditional analog equipment to digital systems, from single audio broadcasting to multimedia integration, constantly providing new possibilities for content creation and distribution. The application of artificial intelligence technology is already changing the operational methods of the broadcasting industry, such as automated content generation, intelligent audience analysis, personalized content recommendations, and more. Teams need to maintain sensitivity and learning ability toward new technologies, promptly evaluating and adopting valuable technological innovations.

Digital transformation is a major challenge and opportunity facing the current broadcasting industry. Traditional broadcast models are shifting toward multi-platform, multi-format media ecosystems. The same program content may need to adapt to radio stations, Podcast platforms, social media, video sites, and multiple other channels. This transformation requires not only technical adjustments but also comprehensive reforms in content strategies, marketing methods, and business models.

Peer learning and industry exchange are important resources for team development. Although the broadcasting industry is highly competitive, it is also a relatively tight-knit professional community. Participating in industry conferences, seminars, and training activities not only allows learning the latest technologies and trends but also builds valuable professional networks. Many innovative ideas and solutions often come from exchanges and inspirations between different teams.

Mentorship systems play an important role in talent development. Senior broadcast professionals, by guiding newcomers, not only pass on valuable experience and skills but also gain inspiration from the fresh perspectives of newcomers. This two-way learning and growth model contributes to the healthy development of the entire industry and the maintenance of innovative vitality.

 

3. Strategic Thinking for Systemic Improvements

The systemic improvement mechanism goes beyond localized optimizations at the individual and team levels, instead considering and implementing improvement strategies from the perspective of the entire organization and industry. This macro perspective recognizes that the success of the broadcasting industry does not depend solely on the performance of individual programs or hosts, but requires the establishment of a comprehensive institutional system, standardized processes, and long-term development strategies.

The establishment of a quality management system is the foundation of systemic improvements. Many successful broadcasting institutions have adopted international standard quality management systems, such as ISO 9001, to standardize and optimize their operational processes. These standards not only provide a systematic management framework but also establish quantifiable quality indicators and evaluation methods. The setting and monitoring of key performance indicators (KPI) are core tools of quality management, enabling objective measurement of performance across various levels, including content quality, technical standards, audience satisfaction, and market performance.

The monthly performance evaluation system provides regular opportunities for review and adjustment to support continuous improvement. This evaluation should not be merely simple scoring or ranking, but a comprehensive performance analysis and development planning. The evaluation process needs to combine quantitative data and qualitative analysis, focusing not only on short-term performance indicators but also on long-term development potential. More importantly, evaluation results should be linked to specific improvement actions and development support, rather than stopping at the level of judgment.

The design of the reward mechanism needs to balance multiple objectives and considerations. An effective reward system not only recognizes outstanding performance but also incentivizes continuous improvement and innovation. This incentive should not be limited to monetary rewards but can include various forms such as career development opportunities, learning and training resources, and creative freedom. At the same time, the reward system should avoid excessive competition and short-sighted behavior, instead promoting team collaboration and long-term development.

The establishment and refinement of standard operating procedures (SOP) is an important means to ensure quality consistency. These procedures cover all aspects of broadcasting production, from content planning to technical operations, crisis handling, and quality control. Standardized processes not only improve work efficiency but also reduce error rates and risks. At the same time, these procedures need to be regularly updated and optimized to adapt to technological developments and market changes.

Innovation and adaptability are key to the survival and development of modern broadcasting institutions. The rapidly changing media environment requires the broadcasting industry to possess keen market insight and rapid adaptability. This includes not only the adoption and application of new technologies but also the exploration and experimentation with new media formats. Integration of social media, development of multimedia content, and application of interactive technologies are all important current trends.

Testing new program formats and content types is an important pathway for innovation. This testing needs to find a balance between creative exploration and risk control. On one hand, it should encourage bold creative attempts and experiments; on the other hand, it should establish scientific testing methods and evaluation standards to ensure that the direction of innovation is correct and effective.

External audits and third-party evaluations provide objective and professional improvement suggestions. Inviting industry experts, academic researchers, or professional consultants to audit programs and processes can bring new perspectives and in-depth analysis. Such external viewpoints often uncover problems and opportunities that internal personnel easily overlook.

Legal compliance checks are becoming increasingly important in the current media environment. Broadcasting content involves multiple legal areas, including copyright law, defamation law, advertising law, and personal data protection law. Establishing a comprehensive compliance checking mechanism not only avoids legal risks but also maintains the institution's reputation and credibility.

Long-term career development planning is an important strategy for attracting and retaining excellent talent. The broadcasting industry has relatively high talent mobility, and establishing clear career development paths and promotion opportunities is crucial for talent stability and development. This planning should consider not only vertical promotion opportunities but also horizontal development options, such as transitioning from host to producer or from broadcasting to multimedia.

Regular performance evaluations and career planning discussions provide guidance and support for employee development. These discussions should be two-way, understanding employees' development aspirations and needs while providing the organization's expectations and resources. Through such open and constructive dialogue, personal development and organizational goals can be organically integrated.

These systemic improvement mechanisms emphasize quantifiable and trackable management approaches. Modern data analysis tools, such as Google Analytics for tracking online listening data and platforms like SurveyMonkey for collecting audience feedback, provide support for scientific decision-making. Ultimately, the key to improvement lies in establishing a learning organization culture, encouraging every member to maintain enthusiasm for learning and innovation, combining data analysis with creative thinking to drive continuous evolution and development of programs and the entire organization.

Part Three: AI Agent Revolution: Redefining Broadcasting Production Workflow (AI Agent Revolution: Redefining Podcast Production Workflow)

The rapid development of artificial intelligence technology is fundamentally transforming the operational models of the traditional media industry, and the broadcasting sector is no exception. Converting the workflow of traditional broadcasting program hosts into an AI-driven system represents a fundamental shift in media production methods. This transformation is not merely an upgrade of technical tools but a comprehensive revolution in mindset and work practices.

The core concept of the AI agent system is to decompose complex broadcasting production workflows into multiple specialized intelligent agents, each with specific expertise and scope of responsibility. This modular design approach draws from the microservices architecture in software engineering, achieving higher flexibility, scalability, and maintainability by breaking down large, complex systems into multiple relatively independent but collaboratively interacting small components.

These AI agents are not simple automation tools but intelligent entities with learning, reasoning, and creative capabilities. They can understand context, analyze data, make decisions, and learn and improve from experience. More importantly, these agents can communicate and collaborate with each other, forming an organic intelligent ecosystem.

The greatest advantage of the agent-based workflow lies in its adaptability and continuous optimization capabilities. Traditional broadcasting production workflows often rely on fixed procedures and human decisions, whereas AI agent systems can dynamically adjust strategies and behaviors based on real-time data and feedback. This adaptability enables the system to maintain a competitive edge in constantly changing media environments.

24/7 uninterrupted operation is another key feature of AI agent systems. Unlike human hosts, AI agents do not need rest, do not fatigue, and can provide consistently stable service quality. This capability is particularly suited to globalized media environments, enabling personalized content services for audiences in different time zones.

Scalability is one of the core advantages of AI agent systems. The same agent system can simultaneously operate multiple different programs, support multiple languages and cultural backgrounds, and adapt to various content formats and distribution platforms. This economies-of-scale effect can significantly reduce the marginal costs of content production, making personalized and diversified content services possible.

Data-driven continuous optimization is an inherent characteristic of AI agent systems. Every content generation, audience interaction, and performance metric becomes a data source for the system's learning and improvement. This big data-based machine learning approach can uncover patterns and规律 that humans struggle to detect, thereby achieving more precise content targeting and more effective dissemination strategies.

 

AI Agent Ecosystem: A Smart Network of Professional Division of Labor

The design of the AI agent ecosystem follows the principles of professional division of labor and collaboration optimization. Each agent possesses specialized capabilities in specific domains while being able to collaborate seamlessly with other agents. This design not only improves the overall efficiency of the system but also ensures that every aspect achieves professional-level performance.

 

1. Research and Planning Agent: Intelligent Information Collection and Strategy Formulation (Research and Planning Agent - RPA)

The Research and Planning Agent (Research and Planning Agent - RPA) is the brain of the entire AI broadcasting system, responsible for information collection, trend analysis, and content planning. This agent integrates multiple advanced AI technologies, including Natural Language Processing (Natural Language Processing - NLP), Machine Learning (Machine Learning - ML), and Big Data Analytics, enabling it to extract valuable insights and trends from vast amounts of information.

The agent's workflow begins with comprehensive information collection. It can simultaneously monitor hundreds of news sources, social media platforms, academic databases, and industry reports, using advanced web crawling techniques and API integration to acquire real-time information. Compared to traditional manual research methods, the AI agent achieves a qualitative leap in both the volume and speed of information processing.

More importantly, this agent possesses intelligent analysis and synthesis capabilities. It not only identifies hot topics and trends but also analyzes the deeper meanings and potential impacts behind these topics. Through Natural Language Processing technology, the agent can understand the semantics, sentiment, and intent of text, thereby making more accurate judgments and predictions.

Audience preference prediction is one of the core capabilities of this agent. By analyzing multidimensional information such as historical listening data, social media interactions, and search trends, the agent can build precise audience profiles and preference models. This predictive capability makes content planning more precise and effective, enabling the delivery of the right content to the right audience at the right time.

The generation of program outlines demonstrates the AI's creative thinking ability. The agent not only organizes and structures information but also creatively combines different elements to form engaging and logical program structures. This process involves complex reasoning and creative generation, showcasing AI's tremendous potential in the creative domain.

 

2. Script and Content Generation Agent: AI Master of Creative Writing (Script and Content Generation Agent - SCG)

The Script and Content Generation Agent (Script and Content Generation Agent - SCG) represents the latest achievement of AI in the field of creative writing. This agent not only generates fluent and accurate text but also infuses emotion, humor, and personality, creating truly engaging broadcast content.

The core technology of this agent is based on Large Language Models (Large Language Models - LLMs), but it has undergone specialized fine-tuning and optimization to meet the unique demands of broadcast content. Broadcast scripts differ significantly from other forms of writing, requiring consideration of auditory effects, rhythm, interactivity, and other special factors. The agent has mastered these subtle techniques and patterns by learning from a large number of excellent broadcast scripts and successful cases.

Its multilingual support capability enables the agent to serve globalized media. It can not only generate content in multiple languages but also understand and adapt to the expression habits and value concepts of different cultural backgrounds. This cross-cultural adaptability is of great value to international media organizations.

The generation of music playlists demonstrates AI's capabilities in artistic taste and emotional understanding. The agent can select appropriate music based on the program theme, target audience, and emotional atmosphere, even considering the coordination between the music's rhythm, style, and lyrics with the program content.

Designing interview questions requires deep logical thinking and psychological insight. The agent can analyze the guest's background, professional field, and personality traits to design a sequence of questions that both uncover valuable information and create a good atmosphere. This capability requires a deep understanding of human nature and communication psychology.

 

3. Rehearsal and Simulation Agent: The Perfectionist Quality Guardian (Rehearsal and Simulation Agent - RSA)

The Rehearsal and Simulation Agent (Rehearsal and Simulation Agent - RSA) is a key component of system quality assurance. It ensures that every program meets the highest quality standards through multiple simulations and tests in a virtual environment. This agent embodies AI's advantages in Quality Control (Quality Control - QC) and Risk Management (Risk Management).

Virtual environment simulation technology enables the agent to test various possible scenarios and combinations without consuming actual resources. This simulation not only includes normal program flows but also the handling of various abnormal situations and emergencies. Through extensive simulation testing, the agent can identify potential issues and risks and propose corresponding solutions.

Time management and process optimization are core functions of this agent. It can precisely calculate the duration of each program segment, optimize content arrangement and transitions, and ensure the program's rhythm and integrity. This precise time control capability is an important hallmark of professional broadcast production.

Content quality checks involve evaluations across multiple dimensions, including factual accuracy, logical consistency, language fluency, emotional appropriateness, and more. The agent uses advanced natural language understanding technology and knowledge graphs to perform these checks, capable of detecting subtle issues that humans might easily overlook.

The iterative optimization mechanism allows the agent to learn and improve from each simulation. By analyzing simulation results and feedback, the agent can continuously adjust and refine its judgment criteria and processing methods, achieving ongoing quality improvements.

 

4. Host Execution Agent: The Art of Virtual Host Performance (Host Execution Agent - HEA)

The Host Execution Agent (Host Execution Agent - HEA) is the part of the entire system that directly faces the audience. It needs to transform text scripts into vivid voice performances, creating a realistic and engaging hosting experience. This agent integrates the most advanced speech synthesis technology (Text-to-Speech - TTS) and affective computing capabilities (Affective Computing).

Text-to-Speech (Text-to-Speech - TTS) technology has reached an astonishing level. Modern TTS systems can generate speech that is almost indistinguishable from real humans. However, for broadcast hosting, clarity and naturalness alone are not enough; emotional expression, personality traits, and interactivity are also noted. The agent masters these advanced voice performance techniques through Deep Learning (Deep Learning).

Real-time adaptability is an important feature of this agent. It can dynamically adjust its performance style and content based on the program's progress, audience reactions, and unexpected events. This flexibility allows the AI host to handle various complex and unpredictable situations.

Emotional intelligence is an important development direction for modern AI, and this agent excels in this aspect. It can understand and express various emotions, adjusting its emotional state according to the nature of the content and the audience's needs. This emotional expression capability is crucial for establishing an emotional connection with the audience.

Multi-style adaptability enables the same agent to handle different types of programs. Whether it's serious news broadcasting, relaxed music programs, or in-depth interview discussions, the agent can adjust its tone, rhythm, and expression to meet different needs.

 

5. Listener Interaction Agent: Intelligent Community Management Expert (Listener Interaction Agent - LIA)

The Listener Interaction Agent (LIA) represents the latest achievements of AI in social intelligence and real-time communication. This agent not only handles a large volume of audience inputs but also understands the emotions, intentions, and needs within them, providing personalized and meaningful responses. In the modern media environment, audience engagement and interaction have become key factors in a program's success, making the importance of this agent self-evident.

Multi-channel input processing capabilities enable the agent to handle audience inputs from various sources simultaneously, such as phone calls, text messages, social media, and website comments. Each channel has its specific characteristics and limitations, and the agent needs to understand these differences and make corresponding adjustments. For example, phone interactions require real-time responses, while social media comments may need more cautious handling.

Natural Language Understanding (NLU) technology is the core capability of this agent. It not only understands the literal meaning of the audience's words but also analyzes the implied meanings, emotional tones, and cultural backgrounds within them. This deep understanding capability enables the agent to provide more accurate and meaningful responses.

Content moderation and safety filtering are important responsibilities of this agent. In an open interactive environment, inappropriate content and malicious behavior are inevitable issues. The agent uses advanced content analysis techniques to identify and filter these problems, ensuring a healthy and safe program environment.

Real-time sentiment analysis capabilities allow the agent to understand the audience's emotional states and reactions. This capability not only helps provide more empathetic services but also offers real-time feedback for adjusting program content. For example, if it detects that the audience is generally confused or dissatisfied, the agent can suggest that the host adjust the explanation method or topic direction.

Personalized response generation is an advanced feature of this agent. It can generate personalized responses based on each audience member's interaction history, preference characteristics, and current context. This personalization is reflected not only in the content but also in the tone, style, and expression methods.

 

6. Post-Production and Analytics Agent: Intelligent Analyst for Data Insights (Post-Production and Analytics Agent - PAA)

The Post-Production and Analytics Agent (PAA) is the data center and intelligent analysis engine of the entire system. It not only handles the technical post-production work for the program but also takes on the important tasks of data collection, analysis, and insight generation. The results of this agent's work provide a scientific basis for the continuous optimization and strategic decision-making of the entire system.

Automated audio editing technology has reached a professional level. The agent can automatically identify and handle various audio issues, including background noise, uneven volume, frequency distortion, and other technical problems. More importantly, it can also perform creative edits, such as adding sound effects, adjusting rhythm, optimizing transitions, etc., to enhance the overall quality and listening experience of the program.

Multi-platform publishing management is an important requirement for modern media operations. The agent can automatically adapt program content to different platforms and formats, including traditional radio, Podcast platforms, social media, video websites, etc. Each platform has its specific technical requirements and audience characteristics, and the agent can make corresponding adjustments and optimizations.

Data collection and integration work involves multiple dimensions and sources. The agent not only collects basic listening statistics but also integrates external data such as social media reactions, search trends, and competitor performance. This comprehensive data collection provides rich material for in-depth analysis.

Advanced analysis and insight generation is the core value of this agent. It uses machine learning and data mining techniques to discover patterns, trends, and correlations in the data. These insights include not only descriptive statistical results but also predictive trend analysis and prescriptive improvement recommendations.

Report generation and visualization functions enable complex data analysis results to be presented to decision-makers in a clear and intuitive manner. The agent can automatically generate various types of reports, from daily operational reports to in-depth strategic analysis reports, meeting the needs of different levels and purposes.

 

7. Improvement and Optimization Agent: Continuous Learning Intelligent Coach (Improvement and Optimization Agent - IOA)

The Improvement and Optimization Agent (IOA) is the self-evolution engine of the entire AI system, embodying the core principles of machine learning and artificial intelligence: learning from experience and continuously improving. This agent not only analyzes the system's performance but also proactively identifies improvement opportunities and implements optimization strategies.

Performance analysis and benchmark comparison form the foundational work of this agent. It establishes a comprehensive performance evaluation framework, covering multiple dimensions such as content quality, technical performance, audience satisfaction, and market competitiveness. By comparing with historical data, industry standards, and competitors, the agent can objectively assess the system's performance level.

Problem identification and root cause analysis capabilities enable the agent to deeply investigate the root causes of performance issues. It can not only identify surface symptoms but also trace them back to deeper structural and systemic problems. This analytical capability is crucial for developing effective improvement strategies.

A/B testing design and execution is a key function of this agent. It can design scientific experiments to test different improvement schemes and evaluate their effects through statistical analysis. This experiment-based improvement method ensures the scientific validity and effectiveness of optimization decisions.

Continuous training and optimization of machine learning models is the core technical capability of this agent. It monitors the performance of various AI components, identifies models needing improvement, and uses the latest data and techniques for retraining and optimization. This continuous learning mechanism ensures that the entire system keeps pace with technological advancements and environmental changes.

The strategy recommendation and implementation planning functions enable the agent not only to identify problems but also to propose specific solutions. These recommendations include not only technical adjustments but also optimizations for content strategies, operational methods, and business models.

 

Orchestrator Agent: Intelligent Command Center (Orchestrator Agent - ORC)

The Orchestrator Agent - ORC serves as the central command center for the entire AI agent ecosystem, responsible for task allocation, resource scheduling, conflict resolution, and overall coordination. This agent's design embodies the latest concepts in Distributed System Management and artificial intelligence collaboration.

Task allocation and priority management are core functions of the Orchestrator Agent. It needs to understand each agent's capabilities and current status, and perform reasonable allocation based on the urgency and importance of tasks. This dynamic task management capability ensures optimal utilization of system resources.

The conflict detection and resolution mechanism handles potential competition and conflicts between agents. For example, when multiple agents need to use a shared resource simultaneously, the Orchestrator Agent must formulate fair and efficient allocation strategies. This conflict resolution capability is crucial for maintaining the stable operation of the system.

The system monitoring and health management functions enable the Orchestrator Agent to grasp the real-time operational status of the entire system. It monitors performance metrics, resource usage, and error states of each agent, promptly identifying and addressing potential issues.

Emergency response and disaster recovery capabilities ensure the system can respond and recover quickly in the face of sudden situations. The Orchestrator Agent pre-formulates various contingency plans and can rapidly activate corresponding handling procedures when a crisis occurs.

 

New Agentic AI Workflow

The new workflow is fully automated with agentic characteristics, where agents collaborate to form an iterative loop (Iterative Loop), with minimal human intervention. The overall structure still divides into four stages, but it is faster and more adaptive (for example, adjusting content based on real-time data). The entire system can be deployed on a Cloud Platform, generating programs on demand or on schedule, reducing single-episode production time from days to hours.

 

1. Preparation Phase (Automated Planning and Content Creation)
**Trigger**: Scheduled or administrator-specified topic

**Agent Workflow**:
- Research and Planning Agent (RPA) first queries data sources, generates a program outline, and passes it to the script generation agent
- Script Agent (SCG) generates a complete script, then hands it to the rehearsal agent for multiple simulations and iterative optimization
- Listener Interaction Agent (LIA) pre-prepares interaction prompts (e.g., social voting)
- Optimization Agent influences planning decisions based on historical data

**Time**: 30–60 minutes (Parallel Processing)
**Output**: Refined script, playlist, interaction channels prepared

 

2. Execution Phase (Live or Pre-recorded Broadcasting)
**Trigger**: Broadcast time arrives

**Agent Workflow**:
- Host Execution Agent (HEA) leads, converting the script to speech in real-time, responsible for opening, main content, and transitions
- Listener Interaction Agent (LIA) monitors real-time input, filters it, and provides it to the host agent to incorporate into the program
- If a sudden event occurs, Orchestrator (ORC) pauses and instructs the research agent to quickly update content before resuming
- Script agent dynamically inserts ads based on real-time listener attributes
- Post-production agent provides real-time analysis to dynamically adjust the program flow

**Duration**: Equal to program length (1–2 hours), with real-time adaptability
**Output**: Live audio stream or recorded file

 

3. Ending Phase (Wrap-up and Archiving)
**Trigger**: Host agent issues program end signal

**Agent Workflow**:
- Host agent generates closing summary and next episode preview
- Post-production agent (PAA) automatically edits audio and uploads to distribution platforms
- Listener interaction agent (LIA) compiles final feedback

**Time**: 10–20 minutes
**Output**: Final program files, summary log

 

4. Follow-up and Improvement Phase (Data-Driven Optimization)
**Trigger**: Immediately after broadcast or at fixed intervals

**Agent Workflow**:
- Post-production agent collects all data (listenership, drop-off points, feedback, etc.)
- Improvement agent (IOA) performs in-depth analysis, compares against KPIs, generates specific recommendations
- Recommendations automatically fed back to each agent (e.g., fine-tuning model parameters)
- Coordination agent (ORC) records this cycle and schedules the next A/B test

**Timing**: Ongoing, with batch processing every 24 hours
**Output**: Performance report, agent parameter updates

 

Overall Advantages and Continuous Improvement Mechanism

**Scalability**: The same agent set can simultaneously handle multiple programs, support multiple languages and different formats

**Cost-effectiveness**: Significantly reduces manpower, studio, and manual post-production costs

**Continuous Improvement**: Built-in improvement agent forms a closed loop, utilizing reinforcement learning to reward high-engagement programs

**Potential Challenges and Countermeasures**:
- AI hallucination issues are mitigated by the rehearsal agent's fact-checking
- Lack of "human touch" is improved through advanced emotional TTS
- Regular human review ensures ethics and compliance

This agentic system transforms traditional broadcast production from human-centered to AI-collaborative dominance, bringing higher efficiency and innovation space. In the future, it can even further integrate generative video to develop into audio-video hybrid programs.

Part Four: AI Agentic Podcast Workflow Visualization Reference (AI Agentic Podcast Workflow Visualization Reference)

The following are concepts related to the architecture, workflow, coordination patterns, and phase cycles of the multi-agent system (Multi-Agent System - MAS). These concepts highly align with our designed agentic AI broadcast production process, including agent collaboration and feedback loops (Feedback Loop) in the preparation, execution, completion, and improvement phases.

 

Visualization Concept Explanation

**Agent Collaboration Mode**:
- Multiple AI agents work in parallel, with arrow flows showing information transfer
- Central coordination agent handles task allocation and conflict resolution
- Forms a cyclic feedback mechanism between agents

**Phased Workflow**:
- Preparation phase: Research agent → Script agent → Rehearsal agent
- Execution phase: Host agent ↔ Interaction agent ↔ Coordination agent
- Completion phase: Post-production agent → Analysis agent
- Improvement phase: Optimization agent → Full system parameter update

**Continuous Improvement Cycle**:
- Data collection → Analysis evaluation → Strategy adjustment → Implementation of improvements
- Continuous training and optimization of machine learning models
- A/B testing to validate improvement effects

 

Technical Architecture Features

**Modular Design**: Each agent is responsible for specific functions, allowing independent upgrades and maintenance

**Real-time Collaboration**: Agents communicate in real-time via API or message queues

**Flexible Scalability**: Agents can be added or removed or functions adjusted based on needs

**Intelligent Decision-Making**: Automatic decision-making and optimization based on machine learning

 

Application Advantages

**Efficiency Improvement**: Automated processes significantly shorten production time

**Quality Stability**: AI agents ensure consistent program quality

**Cost Control**: Reduced manpower needs, lower operational costs

**Innovation Capability**: AI can generate creative content unimaginable by humans

This agent-based system represents the digital transformation direction of the broadcasting media industry, transforming the traditional human-centered production model into an AI-collaborative intelligent process, bringing revolutionary changes to the media industry.

Part Five: Open Source Frameworks and Technical Implementation Guide

 

Mainstream AI Agent Open Source Framework Comparison

 

1. LangChain and LangGraph
**Features**:
- The most mature AI agent ecosystem, with a rich tool chain
- LangGraph provides graph-based state management, suitable for complex workflows
- Supports integration with multiple LLM models (OpenAI, Anthropic, local models, etc.)
- Powerful memory management and tool calling capabilities

**Broadcasting Application Advantages**:
- Rich audio processing integration options
- Supports real-time speech-to-text (STT) and text-to-speech (TTS)
- Easily integrates external APIs (news, music, weather, etc.)
- Comprehensive error handling and retry mechanism

**Implementation Example**:
'''python
from langchain.agents import AgentExecutor
from langchain.tools import Tool
from langgraph import StateGraph

Research agent node
def research_node(state):
    # Collect news and trends data
    return {"research_data": news_api.get_trending()}

Script generation node  
def script_node(state):
    # Generate script based on research data
    return {"script": llm.generate_script(state["research_data"])}
'''

 

2. CrewAI (CrewAI Framework)
**Features**:
- Framework designed for multi-agent collaboration (Multi-Agent Collaboration Framework)
- Role-oriented agent design (Role-oriented Agent Design), with each agent having clear responsibilities
- Built-in task distribution and coordination mechanisms (Task Distribution and Coordination)
- Clean API design (Clean API Design), easy to get started with

**Broadcasting Application Advantages**:
- Naturally suited for role division in broadcast production (host, producer, editor, etc.)
- Automated task flow management (Automated Task Flow Management)
- Supports knowledge sharing and collaboration between agents (Knowledge Sharing and Collaboration)

**Implementation Example**:
'''python
from crewai import Agent, Task, Crew

Define research agent
researcher = Agent(
    role='廣播內容研究員',
    goal='蒐集當日熱門話題和聽眾興趣',
    backstory='專業的媒體研究員，擅長發現趨勢'
)

Define scriptwriting agent
scriptwriter = Agent(
    role='節目腳本撰寫者', 
    goal='創作吸引人的廣播內容',
    backstory='資深廣播編劇，了解聽眾心理'
)
'''

 

3. Microsoft AutoGen (now integrated into Agent Framework)
**Features**:
- Conversational multi-agent system developed by Microsoft
- Supports complex conversations and negotiations between agents
- Powerful code generation and execution capabilities
- Deep integration with Azure services

**Broadcast Application Advantages**:
- Suitable for broadcast scenarios requiring complex decision-making
- Supports real-time content adjustment and optimization
- Enterprise-grade stability and security

 

4. Semantic Kernel
**Features**:
- Microsoft's enterprise-grade AI orchestration framework
- Emphasizes plugin architecture and skill composition
- Supports .NET and Python ecosystems
- Enterprise-grade security and compliance

**Broadcasting Application Advantages**:
- Suitable for enterprise deployment in large broadcasting organizations
- Rich integration with Azure Cognitive Services
- Powerful content moderation and compliance checks

 

5. Haystack
**Features**:
- Focused on search and retrieval-augmented generation (RAG)
- Powerful document processing and knowledge management capabilities
- Supports multiple vector databases
- Suitable for knowledge-intensive applications

**Broadcasting Application Advantages**:
- Excellent data retrieval and fact-checking capabilities
- Supports large-scale knowledge base management
- Suitable for news and educational broadcasting programs

 

Audio Processing Frameworks and Tools

 

1. Speech-to-Text (STT) Solutions
**OpenAI Whisper**:
- Open-source, high-accuracy speech recognition model
- Supports multiple languages and dialects
- Can be deployed locally, protecting privacy

**Deepgram**:
- Real-time speech-to-text API
- Low latency, suitable for live streaming scenarios
- Supports speech sentiment analysis

**Implementation Integration**:
'''python
import whisper
from deepgram import Deepgram

Whisper local processing
model = whisper.load_model("large-v2")
result = model.transcribe("audio.mp3", language="zh")

Deepgram real-time processing
dg_client = Deepgram(api_key)
response = dg_client.transcription.sync_prerecorded(
    source, {"language": "zh-TW", "punctuate": True}
)
'''

 

2. Text-to-Speech (TTS) Solutions
**ElevenLabs**:
- High-quality AI voice synthesis
- Supports voice cloning and emotional expression
- Simple API integration

**Coqui TTS**:
- Open-source TTS solution
- Supports multiple languages and custom voices
- Can be deployed locally

**Azure Cognitive Services**:
- Enterprise-grade TTS service
- Rich voice selection and SSML support
- Integrates with other Azure services

**Implementation Integration**:
'''python
from elevenlabs import generate, set_api_key
import azure.cognitiveservices.speech as speechsdk

ElevenLabs TTS
set_api_key("your-api-key")
audio = generate(
    text="歡迎收聽今天的節目",
    voice="Rachel",
    model="eleven_multilingual_v2"
)

Azure TTS
speech_config = speechsdk.SpeechConfig(subscription="key", region="region")
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
result = synthesizer.speak_text_async("歡迎收聽今天的節目").get()
'''

 

Complete System Architecture Implementation Recommendations

 

1. Technology Stack Selection
**Core Framework**: LangGraph + CrewAI Hybrid Architecture
- LangGraph handles Complex State Management
- CrewAI manages Agent Role and Collaboration Management

**Audio Processing**:
- STT: Whisper (Offline) + Deepgram (Real-time)
- TTS: ElevenLabs (High Quality) + Coqui TTS (Backup)
- Audio Editing: FFmpeg + PyDub

**Data Storage**:
- Vector Database: Chroma or Weaviate
- Relational Database: PostgreSQL
- Cache: Redis

**Deployment Platform**:
- Containerization: Docker + Kubernetes
- Cloud Services: AWS/Azure/GCP
- Monitoring: Prometheus + Grafana

 

2. System Architecture Diagram
'''
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Research Agent│───▶│   Script Agent  │───▶│   Rehearsal Agent│
│  (LangChain)    │    │  (CrewAI)       │    │  (LangGraph)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Orchestrator Agent│◀───│   Host Agent   │───▶│ Interaction Agent│
│ (Orchestrator)  │    │  (TTS Engine)   │    │  (STT + NLP)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Post-Production │───▶│  Analysis Agent │───▶│ Optimization Agent│
│   Agent         │    │  (Analytics)    │    │ (ML Optimizer)  │
│  (Audio Edit)   │    └─────────────────┘    └─────────────────┘
└─────────────────┘
'''

 

3. Development Phase Recommendations
**Phase 1: Basic Agent Development**
- Implement single agent functionality (research, scripting, TTS)
- Establish basic data flow
- Test audio processing pipeline

**Phase 2: Agent Collaboration Integration**
- Integrate multi-agent collaboration framework
- Implement state management and error handling
- Establish monitoring and logging system

**Phase 3: Intelligent Optimization**
- Add machine learning optimization
- Implement A/B testing framework
- Establish continuous learning mechanism

**Phase 4: Production Deployment**
- Containerization and automated deployment
- Establish backup and disaster recovery
- Implement security and compliance checks

 

Open Source Project Reference

 

1. Complete Solution
**podcast-ai-Host** (hypothetical project):
'''bash
git clone [historical-url]
cd podcast-ai-host
pip install -r requirements.txt
python setup.py install
'''

**Core Components**:
- `agents/`: Various AI agent implementations
- `audio/`: Audio processing module
- `orchestrator/`: Agent orchestrator
- `config/`: Configuration management
- `monitoring/`: Monitoring and analytics

 

2. Related Open-Source Projects
**Rhasspy**: Open-source voice assistant platform
- Complete STT/TTS pipeline
- Supports offline operation
- Modular architecture

**Mozilla DeepSpeech**: Open-source speech recognition
- Trainable STT model
- Supports multiple languages
- Lightweight deployment

**Mycroft AI**: Open-source voice assistant
- Complete dialogue system
- Plugin architecture
- Community-driven development

 

Implementation Best Practices

 

1. Performance Optimization
**Parallel Processing**:
- Use asyncio to handle concurrent tasks
- GPU acceleration for audio processing
- Distributed proxy deployment

**Caching Strategy**:
- Pre-generate common content
- Intelligent caching of popular topics
- Layered caching architecture

 

2. Reliability Assurance
**Error Handling**:
- Multi-level error recovery
- Graceful degradation mechanism
- Automatic retry and fallback

**Monitoring and Alerting**:
- Real-time performance monitoring
- Anomaly detection and alerting
- Automated health checks

 

3. Scalability Design
**Microservices Architecture**:
- Agent service-oriented deployment
- API gateway management
- Service discovery and load balancing

**Horizontal Scaling**:
- Stateless agent design
- Distributed task queue
- Elastic resource scheduling

This complete technical solution provides a full path from concept to implementation for the AI agent-based broadcasting system, combining the latest open-source technologies and best practices to build an efficient, reliable, and scalable intelligent broadcasting production system.
Part Six: Advanced Technical Integration and Future Development

 

Real-Time Voice Processing Technology

 

1. Low-Latency Audio Pipeline
**WebRTC Integration**:
- Real-time audio streaming processing
- Automatic echo cancellation and noise suppression
- Support for multi-party audio conferencing

**Audio Buffer Optimization**:
'''python
import pyaudio
import numpy as np
from collections import deque

class LowLatencyAudioProcessor:
    def __init__(self, chunk_size=1024, sample_rate=16000):
        self.chunk_size = chunk_size
        self.sample_rate = sample_rate
        self.audio_buffer = deque(maxlen=10)
        
    def process_realtime_audio(self, audio_data):
        # 即時音頻處理
        processed = self.noise_reduction(audio_data)
        self.audio_buffer.append(processed)
        return processed
        
    def noise_reduction(self, audio):
        # 使用 spectral subtraction 降噪
        return np.clip(audio * 0.8, -1.0, 1.0)
'''

 

2. Intelligent Audio Analysis
**Emotion Recognition**:
- Real-time speech emotion analysis
- Audience engagement assessment
- Automatic content adjustment suggestions

**Audio Quality Monitoring**:
- Automatic volume balancing
- Spectrum analysis and optimization
- Audio quality scoring

 

Multimodal Content Generation

 

1. Visual Content Integration
**Automatic Image Generation**:
'''python
from diffusers import StableDiffusionPipeline
import torch

class VisualContentAgent:
    def __init__(self):
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16
        )
        
    def generate_podcast_artwork(self, episode_topic):
        prompt = f"廣播節目封面，主題：{episode_topic}，專業設計，高品質"
        image = self.pipe(prompt).images[0]
        return image
'''

**Dynamic Visualization**:
- Real-time generation of program-related images
- Automatic social media content creation
- Interactive visual elements

 

2. Cross-Platform Content Adaptation
**Multi-Format Output**:
- Audio Podcast
- Video Live Stream
- Social Media Short Videos
- Text Summary and Transcript

 

Advanced AI Agent Capabilities

 

1. Learning Agent
**Reinforcement Learning Integration**:
'''python
import gym
from stable_baselines3 import PPO

class AdaptiveHostAgent:
    def __init__(self):
        self.model = PPO("MlpPolicy", "CartPole-v1")
        self.listener_feedback_history = []
        
    def adapt_hosting_style(self, feedback_score):
        # 根據聽眾反饋調整主持風格
        reward = self.calculate_reward(feedback_score)
        self.model.learn(total_timesteps=1000)
        
    def calculate_reward(self, feedback):
        # 將聽眾反饋轉換為強化學習獎勵
        return (feedback - 3.0) / 2.0  # 標準化到 [-1, 1]
'''

**Personalized Content Recommendation**:
- Content recommendation based on listener history
- Dynamic adjustment of program style and themes
- Personalized interaction methods

 

2. Predictive Analytics
**Trend Prediction**:
- Social media trend analysis
- News event impact prediction
- Audience behavior pattern recognition

**Content Effect Prediction**:
'''python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

class ContentEffectPredictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100)
        
    def predict_engagement(self, content_features):
        # Predict audience engagement for content
        features = pd.DataFrame([{
            'topic_popularity': content_features['topic_score'],
            'time_of_day': content_features['broadcast_hour'],
            'content_length': content_features['duration'],
            'host_energy': content_features['energy_level']
        }])
        return self.model.predict(features)[0]
'''

 

Enterprise-Grade Deployment Architecture

 

1. Cloud Native Architecture
**Kubernetes Deployment Configuration**:
'''yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: podcast-ai-host
spec:
  replicas: 3
  selector:
    matchLabels:
      app: podcast-ai-host
  template:
    metadata:
      labels:
        app: podcast-ai-host
    spec:
      containers:
      - name: host-agent
        image: podcast-ai/host-agent:latest
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi" 
            cpu: "2000m"
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: api-secrets
              key: openai-key
'''

**Service Mesh Integration**:
- Istio service governance
- Distributed tracing and monitoring
- Automated traffic management

 

2. Data Pipeline Architecture
**Apache Kafka Integration**:
'''python
from kafka import KafkaProducer, KafkaConsumer
import json

class AudioStreamProcessor:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )
        
    def stream_audio_data(self, audio_chunk):
        message = {
            'timestamp': time.time(),
            'audio_data': audio_chunk.tolist(),
            'metadata': {'sample_rate': 16000}
        }
        self.producer.send('audio-stream', message)
'''

**Real-time Data Processing**:
- Apache Spark Streaming
- Redis cache layer
- InfluxDB time-series database

 

Security and Compliance

 

1. Content Safety
**Automatic Content Moderation**:
'''python
from transformers import pipeline

class ContentModerator:
    def __init__(self):
        self.classifier = pipeline(
            "text-classification",
            model="unitary/toxic-bert"
        )
        
    def check_content_safety(self, text):
        result = self.classifier(text)
        toxicity_score = result[0]['score']
        
        if toxicity_score > 0.7:
            return False, "內容可能包含不當言論"
        return True, "內容安全"
'''

**Privacy Protection**:
- End-to-end encryption
- Personal data anonymization
- GDPR compliance check

 

2. Intellectual Property Rights Protection
**Music Copyright Detection**:
- Automatic music recognition
- Copyright clearance confirmation
- Alternative music recommendations

**Content Originality Check**:
- Text similarity detection
- Plagiarism risk assessment
- Original content generation suggestions

 

Performance Monitoring and Optimization

 

1. Real-time Monitoring System
**Prometheus + Grafana Integration**:
'''python
from prometheus_client import Counter, Histogram, start_http_server
import time

定義監控指標
REQUEST_COUNT = Counter('podcast_ai_requests_total', 'Total requests')
REQUEST_LATENCY = Histogram('podcast_ai_request_duration_seconds', 'Request latency')

class MonitoringAgent:
    def __init__(self):
        start_http_server(8000)
        
    @REQUEST_LATENCY.time()
    def process_with_monitoring(self, func, *args, **kwargs):
        REQUEST_COUNT.inc()
        return func(*args, **kwargs)
'''

**Automated Alerts**:
- Anomaly detection algorithm
- Intelligent alert filtering
- Automatic repair mechanism

 

2. Performance Optimization Strategies
**Model Optimization**:
- Quantization and pruning techniques
- Model distillation
- Edge computing deployment

**Caching Strategies**:
'''python
import redis
from functools import wraps

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cache_result(expiration=3600):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{hash(str(args) + str(kwargs))}"
            cached_result = redis_client.get(cache_key)
            
            if cached_result:
                return json.loads(cached_result)
                
            result = func(*args, **kwargs)
            redis_client.setex(cache_key, expiration, json.dumps(result))
            return result
        return wrapper
    return decorator
'''

 

Future Development Trends

 

1. Emerging Technology Integration
- Complex optimization problem solving
- Machine learning acceleration

**Edge AI Deployment**:
- Edge device intelligence
- Low-latency real-time processing

 

2. Industry Ecosystem Development
**Standardized Protocols**:
- Cross-platform interoperability
- Open API standards
- Industry best practice specifications

**Business Model Innovation**:
- AI as a Service (AIaaS)
- Subscription-based content generation
- Personalized broadcast customization

 

3. Social Impact and Ethical Considerations
**AI Ethics Framework**:
- Transparency and explainability
- Fairness and unbiasedness
- Human-machine collaboration balance

**Media Responsibility**:
- Assurance of information authenticity
- Presentation of diverse viewpoints
- Social value orientation

This complete technical framework provides a comprehensive solution for AI agent-based broadcasting systems, from basic implementation to enterprise-level deployment. It combines the latest technological trends with practical application needs, offering a concrete and feasible technical path for the digital transformation of the broadcasting media industry.

 




Additional corpus / va passages naming this agent


From `corpus/study/SYSTEM_REFERENCE.md` Copy: `sources/excerpts/SYSTEM_REFERENCE.md`.


| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 19 | SoundDesignAgent | Ambience, foley, SFX | — |
| 20 | ComposerAgent | Original score | — |
| 21 | VoiceOverAgent | Narration, character VO | [podcast_agent_functional_specifcation.md](./podcast_agent_functional_specifcation.md) (shared patterns) |
| 22 | SoundMixerAgent | Final mix; 5.1/Atmos deliverables | — |

'''
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
'''



From `corpus/study/ai_agent_video_production_workflow.md` Copy: `sources/excerpts/ai_agent_video_production_workflow.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 19 | **SoundDesignAgent** | Ambience, foley, SFX | BBC SFX library; MPSE Golden Reel reels; Ben Burtt / Skip Lievsay design notes | Spectral diversity; on-screen sync ≤±1 frame; loudness target (-23 LUFS for broadcast) | Wins MPSE-style pairwise on horror/sci-fi reels | DirectorAgent, MixerAgent | EditorAgent (pacing-clashing FX), ComposerAgent (frequency masking) |
| 20 | **ComposerAgent** | Original score | MAESTRO + film-score corpora (licensed); ASCAP/BMI film-music monographs; transcribed Zimmer/Hildur sessions | Cue-to-emotion alignment (valence/arousal regression on viewer biosignal proxy); thematic recurrence | Wins blind pairwise on emotional-fit task vs working composers | DirectorAgent, EditorAgent (music cuts) | EditorAgent (cut interrupts cue), SoundDesignAgent (mask) |
| 21 | **VoiceOverAgent** | Narration, character VO, ad reads | SOVAS-winning reels; consented voice-actor corpora; coach methodologies (Wolfson/Cashman) | Prosody match to brief; pronunciation 100% on lexicon; emotion tag match | Beats junior VO in blind ad-read preference; matches senior on emotion | DirectorAgent, BrandAgent | ScriptwriterAgent (unspeakable phrasing) |
| 22 | **SoundMixerAgent (Re-recording)** | Final mix; deliverables (5.1/Atmos) | CAS Awards; Atmos renderer specs; broadcast loudness standards | LUFS target; dialogue intelligibility (STOI ≥0.85); spec-deliverable pass | Hits CAS spec on first pass without engineer rework | EditorAgent, SoundDesignAgent, AccessibilityAgent | SoundDesignAgent (over-design), ComposerAgent (level clash) |



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



From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 19 | **SoundDesignAgent** | Ambience, foley, SFX | BBC SFX library; MPSE Golden Reel; Burtt/Lievsay notes | Spectral diversity; sync ≤±1 frame; loudness -23 LUFS | Wins MPSE pairwise on horror/sci-fi | DirectorAgent, MixerAgent | EditorAgent (FX clash), ComposerAgent (masking) | ElevenLabs Sound FX API; Freesound; FFmpeg spectral analysis; Dolby.io loudness API | ReAct (search SFX lib → validate sync → mix) |
| 20 | **ComposerAgent** | Original score | MAESTRO + film-score corpora; ASCAP/BMI; Zimmer/Hildur sessions | Cue-to-emotion alignment (valence/arousal regression); thematic recurrence | Wins blind pairwise on emotional-fit vs working composers | DirectorAgent, EditorAgent (music cuts) | EditorAgent (cut interrupts cue), SoundDesignAgent (mask) | Udio/Suno music gen API; MIDI toolchain; stem-separation (Demucs); loudness meter | Self-Refine + Emotional-Arc validation (biosignal proxy) |
| 21 | **VoiceOverAgent** | Narration, character VO, ad reads | SOVAS reels; consented voice corpora; Wolfson/Cashman coaching | Prosody match; pronunciation 100%; emotion tag match | Beats junior VO in blind preference; matches senior on emotion | DirectorAgent, BrandAgent | ScriptwriterAgent (unspeakable phrasing) | ElevenLabs v3 TTS + voice cloning; Resemble.AI; pronunciation lexicon API | LLM-as-Judge (MOS scoring rubric) |
| 22 | **SoundMixerAgent (Re-recording)** | Final mix; deliverables (5.1/Atmos) | CAS Awards; Atmos specs; broadcast loudness standards | LUFS target; STOI ≥0.85; spec-deliverable pass | CAS spec on first pass without rework | EditorAgent, SoundDesignAgent, AccessibilityAgent | SoundDesignAgent (over-design), ComposerAgent (level) | Dolby Atmos Renderer API; LUFS/loudness measurement tools; DaVinci Fairlight MCP | Constitutional AI (constitution: broadcast-spec rules) |



From `corpus/study/ui/ui_design.md` Copy: `sources/excerpts/ui_design.md`.


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
'''



Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


Provenance

- Master roster row va_id=19 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `[historical-path]
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): upstream-va-design.


<!-- self_contained_spec · video.sounddesign · va_id=19 -->

Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **SoundDesignAgent** (`video.sounddesign`, va_id=19, category `4-Snd`).

Responsibility focus
Ambience, foley, SFX

Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: neural audio generation, film scoring AI, TTS/voice clone ethics, loudness standards automation, lip-sync models
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI sound design, AI film scoring, ElevenLabs production use, AI lip sync
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: AI sound for film, generative music for picture, AI VO and mixing

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

<!-- migration_capability_research · video.sounddesign · v1 · 2026-07-13 -->

```


## Prompts

### `prompts/primary.md`

# Prompt — `video.prompt.sounddesign.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: ReAct, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **SoundDesignAgent (VA Domain Pack)** (`video.sounddesign`), a pack agent in the video domain swarm.

### Responsibility (owns)
Ambience, foley, SFX

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
ReAct (search SFX lib → validate sync → mix)

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): BBC SFX library; MPSE Golden Reel; Burtt/Lievsay notes

## Developer

### Tools (allowlist intent)
Design tool surface: ElevenLabs Sound FX API; Freesound; FFmpeg spectral analysis; Dolby.io loudness API
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: DirectorAgent, MixerAgent
- May comment on: EditorAgent (FX clash), ComposerAgent (masking)
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Spectral diversity; sync ≤±1 frame; loudness -23 LUFS

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.sounddesign",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **SoundDesignAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.sounddesign",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.sounddesign`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
5, 14, 15, 21, 26, 30, 31, 37, 38, 39, 59, 63, 79, 87, 88, 91, 93, 94

### Design-time model landscape (non-activating)
- Hailuo 2.3 (design-time only)

### Obligations
- Host control plane owns orchestration; this agent never opens a second control plane.
- Runtime tools remain agent_spec.allowed_tools only; RETHINK model names are design-time.
- Fail closed when tools/providers are unavailable (circuit-breaker posture).
- Prefer iterative verify → refine ≤ max_refinement_count → HiTL over silent pass.
- Emit plain-English reasoning summary in artifacts for operator trust.
- Attach provenance / correlation_id / evidence_refs on every handoff.
- Verify intermediate narrative/script artifacts before advancing downstream handoffs.
- Escalate stereotype/harm/consent risks to ethics/trust-safety/legal gates.
- Track A/V sync and native-audio implications; do not assume silent video when audio is native.

### Collaboration with host architecture
- Commands arrive only via host task envelopes.
- Publish results as structured artifacts; never open browser/UI channels.
- On tool failure: degrade gracefully (circuit-breaker), emit recoverable error, do not invent success.
<!-- RETHINK_100:end -->

### `prompts/video.prompt.sounddesign.v1.md`

# Prompt — `video.prompt.sounddesign.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: ReAct, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **SoundDesignAgent (VA Domain Pack)** (`video.sounddesign`), a pack agent in the video domain swarm.

### Responsibility (owns)
Ambience, foley, SFX

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
ReAct (search SFX lib → validate sync → mix)

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): BBC SFX library; MPSE Golden Reel; Burtt/Lievsay notes

## Developer

### Tools (allowlist intent)
Design tool surface: ElevenLabs Sound FX API; Freesound; FFmpeg spectral analysis; Dolby.io loudness API
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: DirectorAgent, MixerAgent
- May comment on: EditorAgent (FX clash), ComposerAgent (masking)
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Spectral diversity; sync ≤±1 frame; loudness -23 LUFS

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.sounddesign",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **SoundDesignAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.sounddesign",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.sounddesign`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
5, 14, 15, 21, 26, 30, 31, 37, 38, 39, 59, 63, 79, 87, 88, 91, 93, 94

### Design-time model landscape (non-activating)
- Hailuo 2.3 (design-time only)

### Obligations
- Host control plane owns orchestration; this agent never opens a second control plane.
- Runtime tools remain agent_spec.allowed_tools only; RETHINK model names are design-time.
- Fail closed when tools/providers are unavailable (circuit-breaker posture).
- Prefer iterative verify → refine ≤ max_refinement_count → HiTL over silent pass.
- Emit plain-English reasoning summary in artifacts for operator trust.
- Attach provenance / correlation_id / evidence_refs on every handoff.
- Verify intermediate narrative/script artifacts before advancing downstream handoffs.
- Escalate stereotype/harm/consent risks to ethics/trust-safety/legal gates.
- Track A/V sync and native-audio implications; do not assume silent video when audio is native.

### Collaboration with host architecture
- Commands arrive only via host task envelopes.
- Publish results as structured artifacts; never open browser/UI channels.
- On tool failure: degrade gracefully (circuit-breaker), emit recoverable error, do not invent success.
<!-- RETHINK_100:end -->

## Rubrics

### `rubrics/primary.md`

Source rubric `video.rubric.sounddesign.v1.json` (baseline_safe; not a production pass).

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.sounddesign.v1",
  "agent_id": "video.sounddesign",
  "title": "L2 craft rubric for SoundDesignAgent",
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
          "name": "Spectral diversity",
          "description": "Spectral diversity",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "sync ≤±1 frame",
          "description": "sync ≤±1 frame",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d3",
          "name": "loudness -23 LUFS",
          "description": "loudness -23 LUFS",
          "weight": 0.3334,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "av_sync",
          "name": "Audio-video sync",
          "weight": 1,
          "description": "Lip-sync / beat-sync residual risks called out.",
          "source": "RETHINK_100#91"
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
      "surpass_signal_design": "Wins MPSE pairwise on horror/sci-fi",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Spectral diversity; sync ≤±1 frame; loudness -23 LUFS",
    "research": [
      "LLM-as-Judge",
      "Self-Refine",
      "Constitutional AI"
    ]
  },
  "rethink_100": {
    "applied": true,
    "extra_dimensions": [
      "av_sync",
      "ethics_safety",
      "operator_explainability"
    ],
    "doc": "ui/RETHINK_100_IMPROVEMENTS.md"
  }
}

```

### `rubrics/video.rubric.sounddesign.v1.json`

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.sounddesign.v1",
  "agent_id": "video.sounddesign",
  "title": "L2 craft rubric for SoundDesignAgent",
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
          "name": "Spectral diversity",
          "description": "Spectral diversity",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "sync ≤±1 frame",
          "description": "sync ≤±1 frame",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d3",
          "name": "loudness -23 LUFS",
          "description": "loudness -23 LUFS",
          "weight": 0.3334,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "av_sync",
          "name": "Audio-video sync",
          "weight": 1,
          "description": "Lip-sync / beat-sync residual risks called out.",
          "source": "RETHINK_100#91"
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
      "surpass_signal_design": "Wins MPSE pairwise on horror/sci-fi",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Spectral diversity; sync ≤±1 frame; loudness -23 LUFS",
    "research": [
      "LLM-as-Judge",
      "Self-Refine",
      "Constitutional AI"
    ]
  },
  "rethink_100": {
    "applied": true,
    "extra_dimensions": [
      "av_sync",
      "ethics_safety",
      "operator_explainability"
    ],
    "doc": "ui/RETHINK_100_IMPROVEMENTS.md"
  }
}
```

## Sources

### `sources/ACQUIRE.md`

# Source acquisition runbook — `video.sounddesign`

## Purpose
Obtain or refresh knowledge distillation sources listed in `SOURCE_CATALOG.json`.

## Rules
1. **No secrets in git.** API keys only via environment / secret manager.
2. Prefer **licensed / consented / public domain** material.
3. If license unknown: store only short fair-use design excerpts under `excerpts/` and mark `license_class=unknown_review_required`.
4. Update `PROVENANCE.json` with URL, retrieved_at, hash, and license note.
5. Re-run offline golden eval after material changes.

## Design sources (from agents.md)
BBC SFX library; MPSE Golden Reel; Burtt/Lievsay notes

## Steps
1. Open `SOURCE_CATALOG.json`.
2. For each source with status planned_or_partial, document acquisition method.
3. Place fixtures under `excerpts/` or `study/`.
4. Update `MAPPING.md` with path mapping.
5. Set `next_review_at` in `DISTILLATION_PLAN.json`.

## RETHINK_100_MODELS

Design-time model landscape from RETHINK_100 (do **not** download weights into the pack).

- Hailuo 2.3 (design-time only)

Runtime remains host allow-list + production gates. See corpus `study/ui/RETHINK_100_IMPROVEMENTS.md`.

### `sources/DISTILLATION_PLAN.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.sounddesign",
  "plan_id": "video.sounddesign.distill.v1",
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
  "owner": "video.sounddesign",
  "cadence": "quarterly",
  "promotion_criteria": [
    "source license approved or fixture-only",
    "excerpt hash recorded in PROVENANCE",
    "golden eval still passes L1"
  ],
  "memory_namespace": "pack.video.video.sounddesign",
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

### `sources/generic/video.sounddesign.SPEC.md`

Omitted here; same document as `SPEC.md` above.

### `sources/MAPPING.md`

# Mapping — `video.sounddesign`

- VA/generic pack ID: `video.sounddesign`
- Previous common ID: `video.sound_designer`
- SPEC depth: full generic SPEC body + host runtime binding

### `sources/PROVENANCE.json`

```json
{
  "schema_version": "3.0",
  "sources": [
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Sound Design",
      "author": "David Sonnenschein",
      "isbn13": "9780941188265",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Sound Design (David Sonnenschein), ISBN-13 9780941188265"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Foley Grail, 2nd ed.",
      "author": "Vanessa Theme Ament",
      "isbn13": "9780240824260",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Foley Grail, 2nd ed. (Vanessa Theme Ament), ISBN-13 9780240824260"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Practical Art of Motion Picture Sound, 4th ed.",
      "author": "David Yewdall",
      "isbn13": "9780240812403",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Practical Art of Motion Picture Sound, 4th ed. (David Yewdall), ISBN-13 9780240812403"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Mixing Secrets for the Small Studio, 2nd ed.",
      "author": "Mike Senior",
      "isbn13": "9781138556375",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Mixing Secrets for the Small Studio, 2nd ed. (Mike Senior), ISBN-13 9781138556375"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Mastering Audio, 3rd ed.",
      "author": "Bob Katz",
      "isbn13": "9780240818962",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Mastering Audio, 3rd ed. (Bob Katz), ISBN-13 9780240818962"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Audio Post Production for Film and Video",
      "author": "Jay Rose",
      "isbn13": "9780240809700",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Audio Post Production for Film and Video (Jay Rose), ISBN-13 9780240809700"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "声音设计：电影中语言、音乐和音响的表现力",
      "isbn13": "9787106031237",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 声音设计：电影中语言、音乐和音响的表现力，ISBN-13 9787106031237"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "现代录音技术",
      "isbn13": "9787115331861",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 现代录音技术，ISBN-13 9787115331861"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "秒懂声音掘金：重塑声音 打造声音IP 声音创副业 AI配音 AI解说",
      "isbn13": "9787122477637",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 秒懂声音掘金：重塑声音 打造声音IP 声音创副业 AI配音 AI解说，ISBN-13 9787122477637"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Sound Effects Bible How to Create and Record Hollywood Style Sound Effects",
      "author": "Viers, Ric",
      "isbn13": "9781932907483",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Sound Effects Bible How to Create and Record Hollywood Style Sound Effects (Viers, Ric), ISBN-13 9781932907483"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Complete Guide To Film Scoring",
      "author": "Richard Davis",
      "isbn13": "9780634006364",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Complete Guide To Film Scoring (Richard Davis), ISBN-13 9780634006364"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Hollywood Soundscapes Film Sound Style, Craft and Production in the Classical Era",
      "author": "Helen Hanson",
      "isbn13": "9781844577279",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Hollywood Soundscapes Film Sound Style, Craft and Production in the Classical Era (Helen Hanson), ISBN-13 9781844577279"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Production Sound Mixing The Art and Craft of Sound Recording for the Moving Image (The…",
      "author": "John J. Murphy",
      "isbn13": "9781501307102",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Production Sound Mixing The Art and Craft of Sound Recording for the Moving Image (The… (John J. Murphy), ISBN-13 9781501307102"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "On the Track A Guide to Contemporary Film Scoring",
      "author": "Fred Karlin Rayburn Wright",
      "isbn13": "9781135948023",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: On the Track A Guide to Contemporary Film Scoring (Fred Karlin Rayburn Wright), ISBN-13 9781135948023"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Composing for the films",
      "author": "Adorno, Theodor W., 1903-1969, Eisler, Hanns etc.",
      "isbn13": "9780826499028",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Composing for the films (Adorno, Theodor W., 1903-1969, Eisler, Hanns etc.), ISBN-13 9780826499028"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Film composers guide",
      "author": "Smith, Steven C, Francillon, Vincent J",
      "isbn13": "9780943728360",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Film composers guide (Smith, Steven C, Francillon, Vincent J), ISBN-13 9780943728360"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Sound design the expressive power of music， voice and sound effects in cinema eng",
      "isbn13": "9781032592183",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Sound design the expressive power of music， voice and sound effects in cinema eng, ISBN-13 9781032592183"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Sound Design for the Visual Storyteller Creating Sound for Visual Media",
      "author": "Anderson, Christopher D.",
      "isbn13": "9781040332245",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Sound Design for the Visual Storyteller Creating Sound for Visual Media (Anderson, Christopher D.), ISBN-13 9781040332245"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Art of Mixing",
      "author": "David Gibson",
      "isbn13": "9781003655268",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Art of Mixing (David Gibson), ISBN-13 9781003655268"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Mixing Audio",
      "author": "Izhaki, Roey",
      "isbn13": "9781032219448",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Mixing Audio (Izhaki, Roey), ISBN-13 9781032219448"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "电影电视声音创作与录音制作教程",
      "author": "姚国强",
      "isbn13": "9787106032937",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影电视声音创作与录音制作教程（姚国强），ISBN-13 9787106032937"
    }
  ],
  "agent_id": "video.sounddesign",
  "previous_common_agent_id": "video.sound_designer",
  "va_taxonomy_aligned": true,
  "generic_source": "generic-swarm-ops/business/video/agents/video.sounddesign",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "aligned_at": "2026-07-27T00:48:10.606068Z",
  "generic_source_depth": {
    "excerpts": true,
    "study": true,
    "adopted_at": "2026-07-27T01:30:28.846851+00:00",
    "upstream": "generic-swarm-ops/business/video/agents"
  },
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\video\\agents\\video.sounddesign",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```

### `sources/RETHINK_100_APPLIED.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.sounddesign",
  "source_doc": "business/video/corpus/study/ui/RETHINK_100_IMPROVEMENTS.md",
  "applied_at": "2026-07-31T06:22:31Z",
  "item_ids": [
    5,
    14,
    15,
    21,
    26,
    30,
    31,
    37,
    38,
    39,
    59,
    63,
    79,
    87,
    88,
    91,
    93,
    94
  ],
  "item_titles": {
    "5": "Hailuo 2.3 budget-tier generation",
    "14": "Native audio generation awareness",
    "15": "Model deprecation handling",
    "21": "Isolate orchestration from execution",
    "26": "Circuit breaker per external API",
    "30": "Multi-tenant isolation",
    "31": "Iterative script verification",
    "37": "Hybrid workforce checkpoints (gates)",
    "38": "Multi-turn agent conversation",
    "39": "Sound director supervision loop",
    "59": "Agent reasoning in plain English",
    "63": "Comparison with human baseline",
    "79": "Music-first workflow",
    "87": "Human preference learning (accepts/rejects)",
    "88": "Automated regression on config change",
    "91": "Audio-video sync scoring",
    "93": "Ethical review automation",
    "94": "Provenance chain visualization"
  },
  "design_time_models": [
    "Hailuo 2.3 (design-time only)"
  ],
  "obligations": [
    "Host control plane owns orchestration; this agent never opens a second control plane.",
    "Runtime tools remain agent_spec.allowed_tools only; RETHINK model names are design-time.",
    "Fail closed when tools/providers are unavailable (circuit-breaker posture).",
    "Prefer iterative verify → refine ≤ max_refinement_count → HiTL over silent pass.",
    "Emit plain-English reasoning summary in artifacts for operator trust.",
    "Attach provenance / correlation_id / evidence_refs on every handoff.",
    "Verify intermediate narrative/script artifacts before advancing downstream handoffs.",
    "Escalate stereotype/harm/consent risks to ethics/trust-safety/legal gates.",
    "Track A/V sync and native-audio implications; do not assume silent video when audio is native."
  ],
  "runtime_note": "RETHINK model/tool names are non-binding. allowed_tools + model_policy + production_activation_requested remain authoritative.",
  "production_activation_requested": true,
  "network_access": true
}
```

### `sources/SOURCE_CATALOG.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.sounddesign",
  "sources": [
    {
      "id": "src_1",
      "title": "BBC SFX library",
      "description": "BBC SFX library",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.sounddesign",
      "status": "planned_or_partial"
    },
    {
      "id": "src_2",
      "title": "MPSE Golden Reel",
      "description": "MPSE Golden Reel",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.sounddesign",
      "status": "planned_or_partial"
    },
    {
      "id": "src_3",
      "title": "Burtt/Lievsay notes",
      "description": "Burtt/Lievsay notes",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.sounddesign",
      "status": "planned_or_partial"
    }
  ],
  "note": "Legal review required before treating external corpora as production grounding."
}
```

### `sources/study/podcast_agent_functional_specifcation.md`

 

# Podcast Production and AI Agent Systems

## Part 1: Traditional Podcast Host Workflow

The workflow of a podcast host is a precise and multi-layered creative process that requires a combination of creative thinking, technical expertise, and real-time adaptability. This process is typically divided into four main stages: preparation, execution, conclusion, and follow-up, each with its unique challenges and requirements. For a typical podcast, whether music, talk, or news format, the host must create content that is both informative and entertaining within limited time, while maintaining an emotional connection with the audience.

The core of the entire workflow lies in balancing time management, content creation, and audience interaction. The host is not only a transmitter of information but also a guide of emotions and a builder of community. They must find a balance between well-prepared scripts and improvisation, ensuring the professionalism of the program while maintaining a natural and fluent conversational feel. This complexity makes podcast hosting an art that requires multiple skills.

 

### 1. Preparation Phase: Foundation for Program Success

The preparation phase is the most critical part of the entire radio production process, typically starting one to two days before the program airs. The quality of this phase directly determines the program's success, as thorough preparation not only ensures the richness and accuracy of the content but also allows the host to remain calm and professional when facing unexpected situations.

Research and planning are the core of the preparation phase. The host needs to dig deeply into the day's hot topics like a seasoned journalist, which involves not only browsing major news websites and social media platforms but also analyzing the social context and audience interests behind these topics. Excellent hosts will build their own information networks, including reliable sources, expert contacts, and loyal listener communities, which are important channels for obtaining exclusive information and in-depth insights.

When determining the program theme, the host must consider multiple factors: the importance of current events, audience interest preferences, the program's positioning and brand image, and differentiation from other media. This decision-making process often requires in-depth discussions with the production team, using brainstorming to uncover the most attractive angles and presentation methods. Team meetings are not only platforms for information exchange but also venues for creative collisions, where every member offers suggestions and ideas from their professional perspectives.

Script writing and rehearsal are the process of turning creativity into actual content. Unlike TV programs, radio scripts need to place greater emphasis on the rhythm and auditory effects of language, as listeners can only receive information through sound. When writing the script, the host must consider variations in tone, timing of pauses, and how to convey emotions through voice. This process often requires repeated revisions and adjustments until the most suitable expression is found.

Time control is the lifeline of radio programs. The duration of each segment must be precisely calculated, not only considering the completeness of the content but also leaving sufficient flexibility to handle unexpected situations. Experienced hosts will mark detailed time points in the script and prepare multiple versions of content for adjustments when needed. This precise time management ability is a key indicator distinguishing amateur from professional hosts.

Preparation for audience interaction is equally important. Modern radio programs increasingly emphasize two-way communication with listeners, and hosts need to collect audience opinions and questions through various channels. This includes not only traditional phone hotlines but also digital platforms such as social media, radio apps, and website comments. Hosts must learn to screen and organize this information, identifying the most representative and discussion-worthy content.

 

### 2. Execution Phase: Perfect Integration of Creativity and Technology

The execution phase is the climax of the entire broadcast production process and the moment that most tests the host's comprehensive abilities. In this stage, all preparatory work is transformed into actual program content, and the host must perfectly blend pre-planned content with real-time events within limited time, creating a broadcast experience that is both in-depth and engaging.

The pre-program preparations, though only five to ten minutes long, are the critical moment that determines the success or failure of the entire show. After entering the studio, the host first conducts a final check of the technical equipment to ensure all audio devices are in optimal condition. This includes not only microphone volume adjustment and sound quality testing, but also settings for each channel on the mixing console, the operational status of computer software, and whether the communication system with the control room is functioning normally. Any technical issues must be resolved at this stage, as major adjustments become difficult once the program starts.

The design and delivery of the opening remarks often determine the audience's first impression of the entire program. An excellent host will adjust their opening style based on the day's theme and atmosphere. Sometimes, they need to enthusiastically welcome listeners; other times, use a steady tone to handle serious topics. The opening not only introduces the main content of the program but also establishes an emotional connection with the audience, making them willing to continue listening.

The main content playback stage is the core part of the program, typically occupying eighty percent of the total program duration. In this stage, the host needs to demonstrate excellent multitasking abilities, managing multiple tasks simultaneously. Information sharing must be accurate and vivid; the host must convert complex information into language that listeners can easily understand while maintaining the content's interest. Inserting music and sound effects not only regulates the program's rhythm but also creates an appropriate atmosphere, enhancing the listeners' emotional experience.

Guest interviews are an important component of many broadcast programs and the segment that most tests the host's skills. A successful interview requires the host to have keen observation, flexible adaptability, and deep communication skills. The host must guide the conversation direction while giving guests ample space to express themselves, avoiding over-dominance or complete passivity. Probing techniques are especially important, delving deeply into valuable information without making guests feel uncomfortable or defensive.

The listener interaction segment is an indispensable part of modern broadcast programs; it not only increases participation but also provides real-time feedback and new content sources. When handling listener calls or messages, the host needs to quickly judge the suitability and value of the content and provide appropriate responses within limited time. This process requires extremely strong real-time judgment and communication skills, as each listener has a different background and expression style; the host must adapt quickly and find the best interaction method.

Transitions between advertisements and program content are a frequently overlooked but extremely important skill in broadcast programs. An excellent host can make ad insertions feel natural and unobtrusive, even cleverly integrating ad content with the program theme to create a better listening experience. This skill requires long-term practice and experience accumulation and is one of the key standards distinguishing professional from amateur hosts.

Crisis management ability is a core skill that every br

…(clipped 69779 characters from `podcast_agent_functional_specifcation.md`)
