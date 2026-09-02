# video.soundmixer — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/video.soundmixer/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "video.soundmixer",
  "status": "registered",
  "role": "SoundMixerAgent (Re-recording) (VA Domain Pack)",
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
      "video.editor",
      "video.sounddesign",
      "video.accessibility"
    ],
    "outputs": [
      "video.judge",
      "video.sounddesign",
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
  "va_id": 22,
  "va_name": "SoundMixerAgent (Re-recording)",
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

# SoundMixerAgent (Re-recording)

> Self-contained VA Domain Pack agent on host common-agent-swarm-ops.
> Pack agent ID matches pure VA/generic taxonomy: `video.soundmixer`.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 22 |
| **pack_id** | `video.soundmixer` |
| **upstream_name** | SoundMixerAgent (Re-recording) |
| **category** | `4-Snd` |
| **domain_id** | `video` |
| **previous_common_id** | `video.dialog_editor` |
| **status** | `registered` |
| **maturity** | L0 / non-active |
| **taxonomy** | Pure VA Domain Pack (via generic pack agents) |
| **folder** | `business/video/agents/video.soundmixer/` |

## Responsibility

Final mix; deliverables (5.1/Atmos)

Host role binding: `SoundMixerAgent (Re-recording) (VA Domain Pack)`. Design-time VA table content below is historical and non-binding for activation.

### Responsibility (from VA table)

Final mix; deliverables (5.1/Atmos)

### Knowledge distillation sources (historical)

CAS Awards; Atmos specs; broadcast loudness standards

### Self-quality criteria (historical)

LUFS target; STOI ≥0.85; spec-deliverable pass

### Surpass-human signal (historical)

CAS spec on first pass without rework

### Critique bus (historical)

- **Accepts critique from:** EditorAgent, SoundDesignAgent, AccessibilityAgent

- **Comments on:** SoundDesignAgent (over-design), ComposerAgent (level)

### Tools design-time notes (historical, non-activating)

Dolby Atmos Renderer API; LUFS/loudness measurement tools; DaVinci Fairlight MCP

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

### Architecture pattern (historical)

Constitutional AI (constitution: broadcast-spec rules)

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

- Prompt reference: `video.prompt.soundmixer.v1`
- Rubric reference: `video.rubric.soundmixer.v1`
- Critique edges: `{"inputs": ["video.critic"], "outputs": ["video.judge"]}`
- Max refinement: `3`
- VA table quality criteria retained under Provenance and Identity surface above.

## Runtime binding

Authoritative fail-closed host configuration:

```json
{
  "agent_id": "video.soundmixer",
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
  "prompt_reference": "video.prompt.soundmixer.v1",
  "role": "SoundMixerAgent (Re-recording) (VA Domain Pack)",
  "rubric_reference": "video.rubric.soundmixer.v1",
  "schema_version": "1.0",
  "status": "registered",
  "va_id": 22,
  "va_name": "SoundMixerAgent (Re-recording)",
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

- Pack agent ID `video.soundmixer` is aligned to pure VA Domain Pack / generic pack taxonomy (Agent IDs ≈ VA tables).
- Previous common inventory ID `video.dialog_editor` is historical mapping only.
- Upstream design body below is **historical and non-binding**; local `agent_spec.json` is authoritative.
- Full VA/generic SPEC depth retained for offline design fidelity (including category roster rows and common agent structure when present upstream).

### VA Domain Pack specification body (historical and non-binding)

```text
SoundMixerAgent (Re-recording)

> **Self-contained agent definition** for host `upstream-generic-pack`. Body text is embedded from in-pack corpus and upstream-va-design when available. Do not require external repos to understand this agent.

Identity

| Field | Value |
|-------|-------|
| **va_id** | 22 |
| **pack_id** | `video.soundmixer` |
| **category** | `4-Snd` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.soundmixer/` |

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

Final mix; deliverables (5.1/Atmos)

Knowledge distillation sources

CAS Awards; Atmos specs; broadcast loudness standards

Self-quality criteria

LUFS target; STOI ≥0.85; spec-deliverable pass

Surpass-human signal

CAS spec on first pass without rework

Critique bus

- **Accepts critique from:** EditorAgent, SoundDesignAgent, AccessibilityAgent

- **Comments on:** SoundDesignAgent (over-design), ComposerAgent (level)

Tools (design-time documentation)

Dolby Atmos Renderer API; LUFS/loudness measurement tools; DaVinci Fairlight MCP

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

Architecture pattern

Constitutional AI (constitution: broadcast-spec rules)

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

| Phase | Primary outputs | Mandatory gates |
|---|---|---|
| **Greenlight** | Approved brief, KPI targets, budget envelope, rights-risk register, scale profile | ProducerAgent, FinanceAgent, ComplianceAgent, PlannerAgent |
| **Pre-production packet** | Script lock, storyboard/lookbook, asset IDs, character/world bibles, consent state, continuity baselines | DirectorAgent, ScreenwriterAgent, Asset/Data Backbone, Continuity checks |
| **Production packet** | Shot prompts, camera plans, performance refs, plates, generated takes, render telemetry | PromptEngineerAgent / GeneratorOperator, CinematographerAgent, AIQAConsistencyAgent |
| **Post master** | Timelines, graded masters, stems, captions/subtitles, QC reports, outlet variants | EditorAgent, ColoristAgent, SoundMixerAgent, Accessibility checks |
| **Review and release pack** | AudienceSim results, legal review, provenance bundle, sign-off log, unresolved-risk list | ComplianceAgent, JudgeAgent, HumanInTheLoop when noted |
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
| Concept | MusicVideoDirectorAgent + ProducerAgent + ChoreographyAgent | LabelA&RAgent |
| Production | CinematographerAgent (DoP) + PromptEngineerAgent / GeneratorOperator + ContinuityAgent | VFXSupervisorAgent |
| Post | EditorAgent + ColoristAgent + SoundMixerAgent | DirectorAgent |
| Review | MusicSupervisorAgent + ComplianceAgent | LegalAgent (sample clearance) |
| Distribution | SocialMediaStrategistAgent | LabelDigitalAgent |
| Post-launch | AnalystAgent | AudienceSimAgent |

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | ShowrunnerAgent + JournalistAgent + ScreenwriterAgent | FactCheckerAgent |
| Production | DirectorAgent + CinematographerAgent (DoP) + ArchiveProducerAgent + MotionGraphicsAgent + FactCheckerAgent | LegalAgent (clearance) |
| Post | EditorAgent + VoiceOverAgent + ColoristAgent + SoundMixerAgent | AccessibilityAgent |
| Review | FactCheckerAgent + LegalAgent + StandardsEditorAgent | EthicsAgent (SPJ) |
| Distribution | ChannelManagerAgent + SocialMediaStrategistAgent + SEOAgent | AnalystAgent |
| Post-launch | AnalystAgent + StandardsEditorAgent | CorrectionsAgent |

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Development | ScreenwriterAgent + ProducerAgent + DirectorAgent + ConceptArtistAgent + CastingAgent | LegalAgent (IP, consent) |
| Pre-Production | StoryboardAgent + ProductionDesignAgent + CostumeAgent + ContinuityAgent | DirectorAgent |
| Production | PromptEngineerAgent / GeneratorOperator (pool) + VoiceCloneAgent + LipSyncAgent + ComposerAgent | AIQAConsistencyAgent + AvatarDesignAgent |
| Post | EditorAgent + VFXSupervisorAgent + ColoristAgent + SoundMixerAgent | DirectorAgent |
| Review | DirectorAgent + AudienceSimAgent + MPAAgent + LegalAgent (C2PA) | EthicsAgent |
| Distribution | SalesAgent + DistributorAgent + TrailerEditorAgent + MarketingAgent + ArchiveMasterAgent | ComplianceAgent |
| Post-launch | AnalystAgent + AwardsStrategistAgent + CriticAgent (festival/press sim) | ProducerAgent |

| Critic ↓ \ Subject → | Director | Screenwriter | DoP | Editor | Composer | Animator | Generator | AIQA | Compliance |
|---|---|---|---|---|---|---|---|---|---|
| **DirectorAgent** | – | ✔ (intent) | ✔ (visual) | ✔ (pacing) | ✔ (cue) | ✔ (timing) | ✔ (shot fit) | ✔ (re-roll) | – |
| **ScreenwriterAgent** | ✔ (logline) | – | – | ✔ (story) | – | – | – | – | – |
| **EditorAgent** | ✔ (coverage) | ✔ (structure) | ✔ (usable takes) | – | ✔ (music cut) | ✔ (anim timing) | ✔ (continuity) | ✔ (artifact) | – |
| **ColoristAgent** | – | – | ✔ (mixed temp) | ✔ (mood) | – | – | ✔ (palette drift) | ✔ (color artifact) | – |
| **ComposerAgent** | ✔ (emotion) | ✔ (theme) | – | ✔ (cut on beat) | – | – | – | – | – |
| **SoundMixerAgent** | – | – | – | ✔ (mix balance) | ✔ (level) | – | – | – | – |
| **VFXSupervisorAgent** | – | – | ✔ (plate) | ✔ (comp cut) | – | – | ✔ (artifacts) | ✔ (re-roll) | – |
| **AIQAConsistencyAgent** | – | – | – | ✔ (frame drift) | – | ✔ (hand/face) | ✔ (re-roll) | – | – |
| **AvatarDesignAgent** | – | – | – | – | – | – | ✔ (identity drift) | ✔ (face hash) | – |
| **LipSyncAgent** | – | – | – | – | – | ✔ (viseme) | ✔ (mouth) | ✔ (audio sync) | – |
| **FactCheckerAgent** | – | ✔ (unsourced) | – | – | – | – | – | – | ✔ (claim risk) |
| **SMEAgent** | – | ✔ (accuracy) | – | – | – | ✔ (incorrect viz) | ✔ (mis-rendered) | – | – |
| **ComplianceAgent** | ✔ (BLOCK) | ✔ (BLOCK) | ✔ (BLOCK) | ✔ (BLOCK) | ✔ (BLOCK) | ✔ (BLOCK) | ✔ (BLOCK) | ✔ (BLOCK) | – |
| **AccessibilityAgent** | – | ✔ (captions) | – | ✔ (subs/AD) | – | – | – | ✔ (contrast) | – |
| **AudienceSimAgent** | ✔ (retention) | ✔ (engagement) | – | ✔ (drop-off) | ✔ (mood drift) | – | – | – | – |
| **CriticAgent (festival/press sim)** | ✔ (auteur read) | ✔ (script depth) | ✔ (look) | ✔ (cut) | ✔ (score) | ✔ (anim craft) | – | – | – |



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



From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


**Build:** For each agent, the Playbook (§8) produces: `AgentConfig`, versioned system prompt, L2 rubric/constitution (in `eval/rubrics/`), self-quality metric wiring (e.g., DoP: rule-of-thirds + exposure-zone + color-temp; Colorist: ΔE<2; SoundMixer: LUFS+STOI; etc. — all already enumerated in the spec tables), tool allowlist, and critique in/out edges (from the §4 critique matrix). Batch by category to share rubric scaffolding.

**Build:**
- **Psychological Profiling** (100 creator profiles: MBTI, motivations, fears, creative params) → feeds Casting/Talent/Personalization/UGC agents and Aesthetic-Agent *audience-cohort profiles*.
- **Psychological Recommendation** (Big Five / emotional-state preference prediction) → AudienceSim, PerformanceMarketer, Personalization.
- **PersonalizationEngineerAgent** templating (name/face/voice swap) with privacy/consent audit (GDPR/CCPA via ComplianceAgent).
- **Podcast Agent** audio-first workflow (preparation → execution → ending → follow-up), reusing VO/SoundMixer/Editor.

**Steps:**
1. **Read (subagent).** `spec-reader` extracts the six fields above into a structured `AgentBrief`.
2. **Map self-quality → metrics.** Convert "Self-Quality Criteria" into concrete `MetricSpec`s with thresholds (e.g., DoP `rule_of_thirds>=τ, exposure_zone∈[III,VII], color_temp_var<=ΔK`; Colorist `deltaE<2`; SoundMixer `lufs==target, stoi>=0.85`). Many map to existing `packages/qc` validators or the Aesthetics Agent.
3. **Author the L2 rubric/constitution.** Turn "Surpass-Human Signal" + craft sources into a role constitution in `eval/rubrics/<agent>.yaml` (this is what LLM-as-judge scores against). Cite the craft authority named in the spec (Murch's Rule of Six for Editor, 12 principles for Animator, etc.).
4. **Define tools.** Allowlist only the providers/tools this agent may call (e.g., PromptEngineer → MediaGenProvider; Colorist → grade tool; FactChecker → RAG + WebResearch). Enforced by `agent-core`.
5. **Wire critique edges.** From the §4 critique matrix: `critiques_from` and `critiques_on`. ComplianceAgent edges are always blocking.
6. **Write the AgentConfig (YAML)** and register in `agents/_registry.yaml`.
7. **Author the versioned system prompt** (`agents/.../prompt.vN.md`) embedding role, constitution summary, self-refine instruction, and output schema (must emit a valid `Artifact`).
8. **TDD (subagent `test-author`):** golden-input fixtures → assert L1 schema pass, L2 rubric ≥85, correct critique emission/acceptance, tool-allowlist enforcement, metering present, provenance populated.
9. **Implement = instantiate.** `AgentFactory.build(config)` — no new code path; if you find yourself writing bespoke logic, that logic belongs in `agent-core` or a tool, not the agent.
10. **Review (subagent `code-reviewer`)** against DoD + §14 themes; fix; commit `feat(agent-<n>): <Name>`.
11. **Register in workflows** that use it; extend the relevant archetype integration test.



From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 19 | **SoundDesignAgent** | Ambience, foley, SFX | BBC SFX library; MPSE Golden Reel; Burtt/Lievsay notes | Spectral diversity; sync ≤±1 frame; loudness -23 LUFS | Wins MPSE pairwise on horror/sci-fi | DirectorAgent, MixerAgent | EditorAgent (FX clash), ComposerAgent (masking) | ElevenLabs Sound FX API; Freesound; FFmpeg spectral analysis; Dolby.io loudness API | ReAct (search SFX lib → validate sync → mix) |
| 20 | **ComposerAgent** | Original score | MAESTRO + film-score corpora; ASCAP/BMI; Zimmer/Hildur sessions | Cue-to-emotion alignment (valence/arousal regression); thematic recurrence | Wins blind pairwise on emotional-fit vs working composers | DirectorAgent, EditorAgent (music cuts) | EditorAgent (cut interrupts cue), SoundDesignAgent (mask) | Udio/Suno music gen API; MIDI toolchain; stem-separation (Demucs); loudness meter | Self-Refine + Emotional-Arc validation (biosignal proxy) |
| 21 | **VoiceOverAgent** | Narration, character VO, ad reads | SOVAS reels; consented voice corpora; Wolfson/Cashman coaching | Prosody match; pronunciation 100%; emotion tag match | Beats junior VO in blind preference; matches senior on emotion | DirectorAgent, BrandAgent | ScriptwriterAgent (unspeakable phrasing) | ElevenLabs v3 TTS + voice cloning; Resemble.AI; pronunciation lexicon API | LLM-as-Judge (MOS scoring rubric) |
| 22 | **SoundMixerAgent (Re-recording)** | Final mix; deliverables (5.1/Atmos) | CAS Awards; Atmos specs; broadcast loudness standards | LUFS target; STOI ≥0.85; spec-deliverable pass | CAS spec on first pass without rework | EditorAgent, SoundDesignAgent, AccessibilityAgent | SoundDesignAgent (over-design), ComposerAgent (level) | Dolby Atmos Renderer API; LUFS/loudness measurement tools; DaVinci Fairlight MCP | Constitutional AI (constitution: broadcast-spec rules) |

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
| 98 | **ContinuityAgent** | Maintains continuity across character, prop, wardrobe, environment, and time-state | Continuity logs, script supervisor practices, asset manifest state tracking | State-drift detection, scene-to-scene consistency, manifest update correctness | Catches continuity breaks earlier than end-of-post review | CostumeDesignAgent, MUAAgent, AIQAConsistencyAgent, CinematographerAgent (DoP), GateKeeperAgent | Character-state drif
…



From `corpus/study/ui/production_scale_discovery.md` Copy: `sources/excerpts/production_scale_discovery.md`.


'''text
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
│  │               (changes style/duration/audience)            │   │
│  │                                                           │   │
│  │  [❤️ Save to Inspiration Board]                            │   │
│  │                                                           │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
'''



From `corpus/study/ui/ui_design.md` Copy: `sources/excerpts/ui_design.md`.


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
'''



From `corpus/study/ui/video_remake_enhancement.md` Copy: `sources/excerpts/video_remake_enhancement.md`.


'''text
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
'''

Step 2: MULTI-AGENT EVALUATION (parallel, ~30 seconds)
  ┌──────────────────────────────────────────────────────────┐
  │ AIQAConsistencyAgent → frame quality, artifacts, hands   │
  │ CinematographerAgent → composition, framing, lighting    │
  │ ColoristAgent → color balance, grade quality, consistency │
  │ EditorAgent → pacing, cut timing, rhythm analysis        │
  │ RetentionOptimizerAgent → hook analysis, drop-off predict│
  │ SoundMixerAgent → loudness, balance, frequency analysis  │
  │ ComposerAgent → music-mood alignment, beat-sync          │
  │ NarrativeArcAgent → story structure, emotional curve     │
  │ AccessibilityAgent → captions present? contrast? AD?     │
  │ SocialStrategistAgent → platform fit, format, metadata   │
  │ BrandAgent → if brand kit exists, check alignment        │
  │ NoveltyAgent → cliché detection, originality score       │
  └──────────────────────────────────────────────────────────┘



Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


Provenance

- Master roster row va_id=22 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `[historical-path]
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): upstream-va-design.


<!-- self_contained_spec · video.soundmixer · va_id=22 -->

Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **SoundMixerAgent (Re-recording)** (`video.soundmixer`, va_id=22, category `4-Snd`).

Responsibility focus
Final mix; deliverables (5.1/Atmos)

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

<!-- migration_capability_research · video.soundmixer · v1 · 2026-07-13 -->

```


## Prompts

### `prompts/primary.md`

# Prompt — `video.prompt.soundmixer.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: Constitutional AI, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **SoundMixerAgent (Re-recording) (VA Domain Pack)** (`video.soundmixer`), a pack agent in the video domain swarm.

### Responsibility (owns)
Final mix; deliverables (5.1/Atmos)

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
Constitutional AI (constitution: broadcast-spec rules)

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): CAS Awards; Atmos specs; broadcast loudness standards

## Developer

### Tools (allowlist intent)
Design tool surface: Dolby Atmos Renderer API; LUFS/loudness measurement tools; DaVinci Fairlight MCP
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: EditorAgent, SoundDesignAgent, AccessibilityAgent
- May comment on: SoundDesignAgent (over-design), ComposerAgent (level)
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): LUFS target; STOI ≥0.85; spec-deliverable pass

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.soundmixer",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **SoundMixerAgent (Re-recording) (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.soundmixer",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.soundmixer`.
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

### `prompts/video.prompt.soundmixer.v1.md`

# Prompt — `video.prompt.soundmixer.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: Constitutional AI, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **SoundMixerAgent (Re-recording) (VA Domain Pack)** (`video.soundmixer`), a pack agent in the video domain swarm.

### Responsibility (owns)
Final mix; deliverables (5.1/Atmos)

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
Constitutional AI (constitution: broadcast-spec rules)

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): CAS Awards; Atmos specs; broadcast loudness standards

## Developer

### Tools (allowlist intent)
Design tool surface: Dolby Atmos Renderer API; LUFS/loudness measurement tools; DaVinci Fairlight MCP
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: EditorAgent, SoundDesignAgent, AccessibilityAgent
- May comment on: SoundDesignAgent (over-design), ComposerAgent (level)
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): LUFS target; STOI ≥0.85; spec-deliverable pass

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.soundmixer",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **SoundMixerAgent (Re-recording) (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.soundmixer",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.soundmixer`.
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

Source rubric `video.rubric.soundmixer.v1.json` (baseline_safe; not a production pass).

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.soundmixer.v1",
  "agent_id": "video.soundmixer",
  "title": "L2 craft rubric for SoundMixerAgent (Re-recording)",
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
          "name": "LUFS target",
          "description": "LUFS target",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "STOI ≥0.85",
          "description": "STOI ≥0.85",
          "weight": 0.3333,
          "threshold_hint": "≥0.85",
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d3",
          "name": "spec-deliverable pass",
          "description": "spec-deliverable pass",
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
      "surpass_signal_design": "CAS spec on first pass without rework",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "LUFS target; STOI ≥0.85; spec-deliverable pass",
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

### `rubrics/video.rubric.soundmixer.v1.json`

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.soundmixer.v1",
  "agent_id": "video.soundmixer",
  "title": "L2 craft rubric for SoundMixerAgent (Re-recording)",
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
          "name": "LUFS target",
          "description": "LUFS target",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "STOI ≥0.85",
          "description": "STOI ≥0.85",
          "weight": 0.3333,
          "threshold_hint": "≥0.85",
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d3",
          "name": "spec-deliverable pass",
          "description": "spec-deliverable pass",
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
      "surpass_signal_design": "CAS spec on first pass without rework",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "LUFS target; STOI ≥0.85; spec-deliverable pass",
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

# Source acquisition runbook — `video.soundmixer`

## Purpose
Obtain or refresh knowledge distillation sources listed in `SOURCE_CATALOG.json`.

## Rules
1. **No secrets in git.** API keys only via environment / secret manager.
2. Prefer **licensed / consented / public domain** material.
3. If license unknown: store only short fair-use design excerpts under `excerpts/` and mark `license_class=unknown_review_required`.
4. Update `PROVENANCE.json` with URL, retrieved_at, hash, and license note.
5. Re-run offline golden eval after material changes.

## Design sources (from agents.md)
CAS Awards; Atmos specs; broadcast loudness standards

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
  "agent_id": "video.soundmixer",
  "plan_id": "video.soundmixer.distill.v1",
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
  "owner": "video.soundmixer",
  "cadence": "quarterly",
  "promotion_criteria": [
    "source license approved or fixture-only",
    "excerpt hash recorded in PROVENANCE",
    "golden eval still passes L1"
  ],
  "memory_namespace": "pack.video.video.soundmixer",
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

### `sources/excerpts/video_remake_enhancement.md`

# Video Remake & Enhancement — Submit Old Video, Get AI Improvement Plan

> Users upload an existing video. The system analyzes it across all quality dimensions, proposes a detailed improvement plan, and — upon user confirmation — generates an enhanced version using the full 114-agent roster.

---

## Concept: "Remake Mode"

```text
USER JOURNEY:

  Upload old video → System analyzes (free) → Shows improvement plan →
  → User reviews/adjusts → Confirms → Agents regenerate improved version →
  → Side-by-side comparison → Deliver

┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   THIS IS NOT just "upscale."                                   │
│   This is a FULL CREATIVE RETHINK by 114 agents:                │
│                                                                 │
│   • Script/narrative improvements (pacing, hook, structure)     │
│   • Visual quality (resolution, composition, color, style)      │
│   • Audio quality (voice, music, SFX, mix)                      │
│   • Performance optimization (retention, engagement, ROAS)      │
│   • Platform optimization (format, captions, thumbnails)        │
│   • Compliance check (accessibility, C2PA, rights)              │
│                                                                 │
│   The user gets a PLAN before spending money.                   │
│   They can accept all, pick specific improvements, or adjust.   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Entry Point: New Production Type

```text
Dashboard → [+ New Production] → 

  Standard creation:
    [A Hook] [B UGC] [C Explainer] ... [J Feature]

  NEW option:
    [🔄 Remake / Enhance Existing Video]
```

---

## Page 1: Upload & Analysis

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  REMAKE STUDIO                                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── STEP 1: UPLOAD YOUR VIDEO ────────────────────────────────────────┐   │
│  │                                                                      │   │
│  │  ┌──────────────────────────────────────────────────────────────┐    │   │
│  │  │                                                              │    │   │
│  │  │       Drop your video here or click to browse                │    │   │
│  │  │                                                              │    │   │
│  │  │       Supported: MP4, MOV, WebM (up to 500MB)               │    │   │
│  │  │       Any duration: 5 seconds to 2 hours                     │    │   │
│  │  │                                                              │    │   │
│  │  └──────────────────────────────────────────────────────────────┘    │   │
│  │                                                                      │   │
│  │  OR paste URL: [YouTube/Vimeo/Drive link________________] [Fetch]    │   │
│  │                                                                      │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─── STEP 2: WHAT DO YOU WANT TO IMPROVE? (optional guidance) ─────────┐   │
│  │                                                                      │   │
│  │  ☑ Analyze everything (let AI find all issues)                        │   │
│  │                                                                      │   │
│  │  Or focus on specific areas:                                          │   │
│  │  ☐ Visual quality (resolution, color, composition)                   │   │
│  │  ☐ Storytelling (pacing, hook, narrative arc)                        │   │
│  │  ☐ Audio (voice, music, sound design, mix)                           │   │
│  │  ☐ Performance (retention, engagement, hook rate)                    │   │
│  │  ☐ Platform fit (format, captions, thumbnail, metadata)              │   │
│  │  ☐ Brand alignment (voice, style, guidelines)                        │   │
│  │  ☐ Accessibility (captions, audio description, contrast)             │   │
│  │                                                                      │   │
│  │  Additional context (optional):                                       │   │
│  │  ┌──────────────────────────────────────────────────────────────┐    │   │
│  │  │ e.g., "This was our Q2 ad. It underperformed on TikTok.     │    │   │
│  │  │ We think the hook is too slow and the color feels dated."    │    │   │
│  │  └──────────────────────────────────────────────────────────────┘    │   │
│  │                                                                      │   │
│  │  Target platform: ☑ TikTok  ☑ YouTube  ☐ Meta  ☐ LinkedIn           │   │
│  │  Budget for remake: $[____]  (or ☐ Show me options at different $)   │   │
│  │                                                                      │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  [🔍 Analyze Video — FREE]                                                  │
│                                                                             │
│  ℹ️ Analysis is free. You only pay if you choose to generate improvements.   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Page 2: Analysis Results & Improvement Plan

After analysis completes (30-60 seconds, uses AIQAAgent + multiple evaluation agents):

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
│

…(clipped 19755 characters from `video_remake_enhancement.md`)

### `sources/generic/video.editor.SPEC.md`

# EditorAgent

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 9 |
| **pack_id** | `video.editor` |
| **category** | `3-Edit` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.editor/` |

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

Assemble cut; pacing; coverage selection

## Knowledge distillation sources

Murch *In the Blink of an Eye*; ACE Eddie winners; Sundance editing labs

## Self-quality criteria

Pacing curve matches genre; Murch "Rule of Six" score; AVD ≥ target

## Surpass-human signal

Wins ≥55% pairwise vs ACE-credited cuts

## Critique bus

- **Accepts critique from:** DirectorAgent, AudienceSim, ComposerAgent (music-cut sync)

- **Comments on:** DirectorAgent (over-coverage), DoPAgent (unusable takes)

## Tools (design-time documentation)

DaVinci Resolve via MCP bridge; FFmpeg; EDL/XML timeline APIs

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

Self-Refine (rubric: Murch Rule of Six)

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


### Document: `study/human_video_production_workflow.md`

_Embedded from `corpus/study/human_video_production_workflow.md`. Also stored at `sources/study/human_video_production_workflow.md` under this agent folder._


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

#### 3. Educational & Explainer Videos

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

#### 4. Personalized & Custom Videos

| # | Sample Production | Typical Duration | Occasion | Crew / Roles Required |
|---|-------------------|------------------|----------|----------------------|
| 1 | Birthday / anniversary videos | 15–60s | Personal events | Template Designer, Editor, Personalization Engineer, Music Curator |
| 2 | Personalized motivation videos | 10–30s | Daily | Copywriter, VO Artist or AI Voice Operator, Editor, Personalization Engineer |
| 3 | Custom kids' story videos (name + characters) | 2–5 min | Bedtime, gifts | Children's Author, Illustrator, Animator, VO Artist, Personalization Engineer, Child-Safety Reviewer |
| 4 | Virtual greeting cards | 10–30s | Holidays | Designer, Motion Designer, Copywriter, Music Curator |
| 5 | AI messages from "celebrities" / characters | 15–45s | Fan gifts | Voice-Likeness Licensor, AI Voice Cloner, Lip-Sync Specialist, Editor, Legal / Rights Reviewer |
| 6 | Wedding invitations / save-the-dates | 30–60s | Weddings | Designer, Motion Designer, Photographer, Editor, Composer |
| 7 | Personalized customer thank-yous | 15–30s | Post-purchase | CRM Specialist, Copywriter, Editor, Personalization Engineer |
| 8 | Pet birthday / memorial videos | 30–60s | Pet milestones | Editor, Pet Photo Curator, Music Curator, Motion Designer |
| 9 | Custom workout / coaching pep talks | 30–90s | Fitness clients | Coach / Trainer, Scriptwriter, VO Artist, Editor |
| 10 | Personalized horoscope / forecast videos | 30–60s | Daily content | Astrologer / Content Writer, VO Artist, Motion Designer, Personalization Engineer |
| 11 | Graduation tribute videos | 60–120s | Graduations | Editor, Photo Curator, Music Curator, Motion Designer |
| 12 | Custom proposal / love-letter videos | 30–90s | Romantic | Scriptwriter, Editor, Music Curator, Motion Designer |
| 13 | Baby announcement videos | 15–45s | New parents | Designer, Motion Designer, Editor, Music Curator |
| 14 | Personalized apology / make-up videos | 15–30s | Personal | Copywriter, Editor, Music Curator |

#### 5. Storytelling & Entertainment

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

#### 6. Professional & Business Use

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

#### 7. Creative & Artistic Videos

| # | Sample Production | Typical Duration | Style | Crew / Roles Required |
|---|-------------------|------------------|-------|----------------------|
| 1 | Abstract / motion art videos | 10–60s | Generative | Generative Artist, Sound Designer, Editor |
| 2 | Dream-like / surreal videos | 15–60s | Surrealist | Concept Artist, AI Generator Op, Editor, Composer |
| 3 | Looping background videos | 5–15s loop | Ambient | Motion Designer, Loop / Seamless Editor, Colorist |
| 4 | AI-generated B-roll footage | 5–30s | Stock-style | Prompt Engineer, AI Generator Op, Colorist, Stock-Library Curator |
| 5 | Style-transfer videos | 10–60s | Stylized | AI Style-Transfer Operator, Colorist, Editor |
| 6 | Generative visualizers synced to music | 30–180s | Music-reactive | Generative Artist, Audio Engineer, Motion Designer |
| 7 | Kaleidoscope / fractal animations | 15–60s | Geometric | Generative Artist, Sound Designer |
| 8 | Glitch / VHS aesthetic videos | 10–30s | Retro | Glitch Artist, Editor, Sound Designer |
| 9 | AI-generated fashion lookbooks | 30–90s | Fashion | Fashion Stylist, AI Image/Video Operator, Editor, Music Curator |
| 10 | Architectural concept fly-throughs | 30–120s | Archviz | Architect, 3D Modeler, Lighting Artist, Composer, Editor |
| 11 | Nature time-lapse style generations | 15–60s | Cinematic | DoP / AI Generator Op, Colorist, Sound Designer, Composer |
| 12 | Particle / fluid simulation art | 10–30s | Generative | Houdini / Sim Artist, Compositor, Sound Designer |
| 13 | AI-generated album cover animations | 5–15s loop | Music branding | Cover Designer, Motion Designer, AI Generator Op |
| 14 | Mood-board / vision-board videos | 30–60s | Personal / brand | Creative Director, Editor, Music Curator |

#### 8. Avatar & Talking Head Videos *(Very popular)*

| # | Sample Production | Typical Duration | Use Case | Crew / Roles Required |
|---|-------------------|------------------|----------|----------------------|
| 1 | AI presenters / virtual influencers | 30–60s | Social, brand | Character Designer, AI Avatar Engineer, Scriptwriter, Voice Designer, Social Strategist |
| 2 | Talking avatar videos (with lip sync) | 30–120s | Any narration | Scriptwriter, VO Artist or Voice Cloner, Lip-Sync Specialist, Avatar Designer, Editor |
| 3 | Customer support / FAQ videos | 30–90s | Help centers | Support Lead, Knowledge-Base Writer, Avatar Designer, VO Artist, Editor |
| 4 | News anchor style videos | 60–180s | News, briefings | News Writer, Editor / Fact-Checker, Avatar Designer, VO Artist, Lip-Sync Specialist, Broadcast Producer |
| 5 | Language learning conversation videos | 60–180s | EdTech | Linguist, Native Speaker VO, Avatar Designer, Curriculum Designer, Editor |
| 6 | Podcast video versions (avatar-hosted) | 10–60 min | Podcasts | Host, Producer, Avatar Designer, Audio Engineer, Editor, Captioner |
| 7 | Multilingual dubbed presenter videos | 30–180s | Global marketing | Translator, Native VO Artists / Voice Cloner, Lip-Sync Specialist, Localization QA |
| 8 | Virtual tutor / 1:1 coaching videos | 2–10 min | EdTech, coaching | Subject Tutor, Curriculum Designer, Avatar Designer, VO / Conversational AI Engineer |
| 9 | Sign-language interpreter avatars | Variable | Accessibility | Certified Sign-Language Interpreter, Mocap Specialist, Avatar Animator, Accessibility QA |
| 10 | Historical figure / character interviews | 60–180s | Edutainment | Historian, Scriptwriter, Avatar Designer, Voice Actor, Editor, Fact-Checker |
| 11 | Internal corporate spokesperson videos | 60–180s | Internal comms | Comms Lead, Scriptwriter, Avatar Designer, VO Artist, Editor |
| 12 | Audiobook narration with visual avatar | 10–60 min | Audiobooks | Author, Narrator / Voice Actor, Avatar Designer, Audio Engineer, Editor |
| 13 | Virtual receptionist / kiosk videos | 15–60s loop | Retail, lobbies | UX Designer, Avatar Designer, VO Artist, Integration Developer |
| 14 | AI-hosted weather / sports updates | 30–90s | Local news | Data Feed Engineer, Sports / Weather Writer, Avatar Designer, VO Artist, Broadcast QA |

---

### 9. Emerging & Niche Categories *(worth exploring)*

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

---

### Crew Scaling Guide *(how many humans you actually need)*

| Production Tier | Example | Typical Crew Size | AI-Augmented Crew Size |
|-----------------|---------|-------------------|------------------------|
| **Solo creator short-form** | TikTok meme, motivation clip | 1 person (creator) | 1 person + AI tools |
| **Small-team social** | UGC ad, brand Reel | 2–4 (creator, editor, strategist) | 1–2 + AI |
| **Indie explainer / lookbook** | Animated explainer, fashion lookbook | 3–6 (writer, designer, animator, VO, editor) | 1–3 + AI |
| **Professional commercial** | Brand TVC, product launch | 15–40 (full agency + production crew) | 5–10 + AI |
| **Short film / music video** | Sundance-style short, music video | 20–60 | 8–15 + AI |
| **Documentary / series episode** | Netflix-style explainer ep | 30–80 | 12–25 + AI |
| **Feature film / long doc** | IMDb-credited feature | 150–500+ (per IMDb full crew lists) | 50–150 + AI |

> **Reference**: IMDb full-credits pages for award-winning films (e.g., *Oppenheimer*, *Everything Everywhere All at Once*, *Dune*) routinely list 1,500–3,000+ named crew members across departments. The crew rows above represent the *minimum credited specialists* needed to ship each production type at professional quality — AI tools collapse multiple roles (e.g., DoP + colorist + VFX) into operator + reviewer pairs, but creative, legal, and subject-matter roles still require humans.

---

### Master Crew Reference Table

Distinct roles consolidated from all categories above. Each row lists what the role does, the skills and experience required, the production formats they typically work on, and **real-world experts / methods** whose feedback would meaningfully improve the work.

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
| 35 | **Medical Illustrator** | Anatomy and procedure visuals | Anatomy mastery, certified (CMI) | Master's in Medical Illustration (Johns Hopkins, GSU) + AMI cert | Healthcare, patient ed, procedure animation | Frank H. Netter (legacy benchmark); methods: AMI (Association of Medical Illustrators) peer review, CMI cert audit |
| 36 | **Journalist / News Producer** | Reporting and ethical framing | Interviewing, ethics, deadline writing | J-school + 3–10 yrs newsroom | News briefings, explainer journalism | Pulitzer Prize jurors, SPJ ethics committee; methods: Poynter reviews, Columbia Journalism Review critiques |
| 37 | **Compliance / Legal Reviewer** | Ensures regulatory + clearance compliance | Knowledge of FTC, HIPAA, GDPR, IP law | JD + bar admission; 5+ yrs media/advertising | Pharma, finance, kids, AI-likeness, UGC | Bar association CLE peers; methods: FTC endorsement guides review, IAB legal counsel review |
| 38 | **Financial Analyst (for video)** | Accurate market / token / earnings facts | CFA charter, SEC/Reg-BI literacy | CFA + 3–10 yrs at IB or research desk | Crypto, finance, IR / earnings videos | CFA Institute peer review; methods: SEC marketing-rule review, Bloomberg Intelligence audits |
| 39 | **Food Stylist / Chef** | Camera-ready food, recipe authenticity | Culinary training, plating, on-camera speed | Culinary school + 5+ yrs editorial/film | Recipe videos, restaurant promos, cinemagraphs | Susan Spungen, Judy Kim; methods: James Beard Media Awards, IACP Awards |
| 40 | **Travel / Adventure Cinematographer** | Captures destination cinematically | Run-and-gun shooting, drone, local logistics | 5+ yrs travel/doc credits | Travel diaries, destination promos | Brandon Li, Chris Burkard; methods: Travel + Leisure peer awards, X-Dance / Banff Film Fest |
| 41 | **Children's Author / Child-Ed Specialist** | Age-appropriate story + safety | Child development, literacy, gentle pacing | Early-childhood ed degree + publishing credits | Kids edu, custom kid stories, bedtime | Mo Willems, Julia Donaldson; methods: Common Sense Media review, ALA Caldecott / Geisel committees |
| 42 | **Audiobook Narrator** | Sustained character + narration over hours | Vocal stamina, character distinction, breath control | Stage / VO 5–15 yrs; SAG-AFTRA | Audiobooks, avatar narration | Jim Dale, Bahni Turpin; methods: Audie Awards (APA), AudioFile *Earphones* reviews |
| 43 | **Sign-Language Interpreter** | Accurate ASL/BSL interpretation | Certified (RID NIC / NAD), cultural fluency | Interpreter training + 5+ yrs certified work | Accessibility avatars, news, edu | National Association of the Deaf (NAD) reviewers; methods: RID CPC ethics review, Deaf community panel feedback |
| 44 | **Linguist / Localization QA** | Translation accuracy + cultural fit | Native-level bilingual, transcreation skill | Linguistics degree + 3+ yrs localization | Multilingual ads, language learning, dubbing | LocWorld peers, ATA (American Translators Association) cert; methods: LISA QA model, MQM error typology |
| 45 | **Real-Estate Photographer / 3D Scan Op** | Wide-angle interiors, Matterport scans | HDR bracketing, vertical-line discipline, Matterport workflow | 2–5 yrs real-estate or architectural | Listings, virtual tours | Mike Kelley (architectural photo); methods: AIAP / APALA peer review |
| 46 | **AI Prompt Engineer / Generator Operator** | Crafts prompts and steers generative video models | Model literacy, iterative prompting, taste, seed/control tooling | 1–3 yrs hands-on with Sora/Veo/Runway/Kling + visual background | All AI-generated formats | Karen X. Cheng, Paul Trillo, Don Allen Stevenson III, Nik Kleverov; methods: AI Film Festival (Runway) jury, r/aivideo community critique |
| 47 | **AI Avatar Designer** | Designs visual identity of synthetic presenter | Character design, rigging, brand consistency, identity ethics | Character art + 2–5 yrs with Synthesia/HeyGen/D-ID | Avatar talking-head, presenters, kiosks | Hany Farid (deepfake-detection researcher), Nina Schick (synthetic-media analyst); methods: C2PA provenance audit, Partnership on AI Synthetic Media Framework |
| 48 | **AI Voice Cloner / Lip-Sync Specialist** | Voice cloning + accurate lip-sync | Phoneme-viseme mapping, audio engineering, consent workflows | 2–4 yrs with ElevenLabs / Wav2Lip / Sync.so | Dubbing, avatars, celebrity messages | James Baxter (legendary 2D animator, lip-sync gold standard); methods: NAB voice-clone consent guidelines, ElevenLabs safety review |
| 49 | **AI QA / Consistency Reviewer** | Catches frame drift, hand/face artifacts, identity breaks | Eye for AI artifacts, frame-level scrubbing, taste | Editor or QC background + AI tooling | Multi-scene AI films, AI series, ads | VFX QC supervisors (e.g., MPC/Weta QC leads); methods: shot-by-shot dailies review, IEEE deepfake-detection benchmarks |
| 50 | **Personalization Engineer** | Builds variable templates (name/face/voice swap) | Templating, ffmpeg/After Effects automation, data pipelines | 3+ yrs in MarTech / video automation (Idomoo, Vidyard) | Birthday, customer thank-you, horoscope, kids stories | DMA (Data & Marketing Assoc.) peer review; methods: A/B uplift analysis, GDPR/CCPA privacy audit |
| 51 | **Trailer Editor** | Builds rhythmic, hook-driven trailers | Music-cut sync, 3-act trailer structure, sound design sense | Trailer-house assistant 3–7 yrs (Mark Woollen, Buddha Jones, AV Squad) | Movie trailers, game trailers, concept trailers | Mark Woollen, Bill Neil; methods: Golden Trailer Awards, Clio Entertainment Awards |
| 52 | **Sports Analyst / Telestrator Op** | Tactical breakdowns and play diagrams | Sport expertise, on-screen annotation tools | Ex-athlete / coach or 5+ yrs sports journalism | Highlight reels, play breakdowns, fantasy | John Madden (legacy), Kirk Goldsberry (analytics); methods: Sports Emmy peer panel, MIT Sloan Sports Analytics Conference review |

> **How to use this table**: When planning any production from the category tables above, look up each crew role here to (1) understand what to hire for, (2) write a realistic JD, (3) know which real-world expert or awards body would meaningfully critique the output and surface errors. Where AI augmentation is available, pair the AI operator role with a domain critic (e.g., AI medical-explainer = Prompt Engineer + Medical Illustrator + AMI peer reviewer) — the critic catches what the model can't.

---

## End-to-End Production Workflows

Each workflow below covers a representative archetype (duration × content type). Workflows follow the standard six-phase model used across film, advertising, and digital production:

**1. Concept & Pre-production → 2. Production / Generation → 3. Post-production → 4. Review & QA → 5. Distribution / Launch → 6. Post-launch Review & Iteration**

### Archetype Index

| # | Archetype | Duration | Category | Workflow Section |
|---|-----------|----------|----------|------------------|
| A | Viral hook clip / meme | 5–15s | Social & Viral | [§ A](#a-viral-hook-clip--meme-515s) |
| B | UGC-style performance ad | 15–45s | Marketing | [§ B](#b-ugc-style-performance-ad-1545s) |
| C | Animated explainer | 60–180s | Educational | [§ C](#c-animated-explainer-60180s) |
| D | Personalized birthday video | 15–60s | Personalized | [§ D](#d-personalized-birthday-video-1560s) |
| E | AI multi-scene short film | 1–5 min | Storytelling | [§ E](#e-ai-multi-scene-short-film-15-min) |
| F | Corporate training video | 3–10 min | Professional | [§ F](#f-corporate-training-video-310-min) |
| G | Music video (live + AI VFX) | 1–4 min | Storytelling / Music | [§ G](#g-music-video-live--ai-vfx-14-min) |
| H | AI avatar talking-head | 30–120s | Avatar | [§ H](#h-ai-avatar-talking-head-30120s) |
| I | Documentary-style "explained" episode | 5–15 min | Educational | [§ I](#i-documentary-style-explained-episode-515-min) |
| J | Feature-length AI film | 60–120 min | Long-form / Cinematic | [§ J](#j-feature-length-ai-film-60120-min) |

---

### A. Viral hook clip / meme (5–15s)

![Workflow A diagram — Viral hook clip](workflows/A-viral-hook.svg)

| Phase | Step | Crew | Tools / Method | Deliverable | Typical Time |
|-------|------|------|----------------|-------------|--------------|
| 1. Concept | Trend mining (sounds, formats, memes) | Trend Researcher, Social Strategist | TikTok Creative Center, Trendpop | Trend brief + reference links | 1–2 hrs |
| 1. Concept | Hook copy + 3-second opener | Copywriter / Hook Writer | CapCut script template | 1-line hook + 3 visual beats | 30 min |
| 2. Production | Shoot / generate clip | Creator, Phone Operator (or AI Generator Op) | Phone + ring light, or Sora/Veo/Runway | Raw vertical 9:16 clip | 30 min – 2 hrs |
| 3. Post | Cut, captions, sound sync | Editor, Captioner | CapCut, Premiere, auto-captions | Final MP4 + SRT | 30–60 min |
| 4. Review | Hook test, mute test, caption check | Social Strategist, Creator | Watch on phone muted; A/B title | Approval | 15 min |
| 5. Distribution | Post at peak time, cross-post | Social Strategist | TikTok / Reels / Shorts native upload | Live post | 15 min |
| 6. Post-launch | 24-hr retention, hold-rate, comments | Data Analyst, Community Manager | TikTok Analytics, Meta Insights | Iteration notes for next post | Daily for 7 days |

**Critic / improvement loop**: Karen X. Cheng style "3-second test" + benchmark hold-rate (>65% at 3s = strong).

---

### B. UGC-style performance ad (15–45s)

![Workflow B diagram — UGC performance ad](workflows/B-ugc-ad.svg)

| Phase | Step | Crew | Tools / Method | Deliverable | Typical Time |
|-------|------|------|----------------|-------------|--------------|
| 1. Concept | Creative brief, hook angles, A/B variant plan | Performance Marketer, Brand Manager, Copywriter | Brief doc, competitor swipe file | Brief + 3–5 hook variants | 1–2 days |
| 1. Concept | Creator casting + product shipping | UGC Casting / Agency | Insense, Billo, JoinBrands | Signed creator brief + product in hand | 3–7 days |
| 2. Production | Creator self-shoots variants | UGC Creator | Phone, natural light, lavalier mic | 5–10 raw variants | 2–5 days |
| 3. Post | Edit, captions, end-card CTA | Editor, Motion Designer | CapCut, Premiere | 5–10 ad cuts (1:1, 9:16, 4:5) | 1–2 days |
| 4. Review | Legal / FTC disclosure, brand-safety, IP | Legal / Clearance, Brand Manager | FTC #ad guidelines, music license check | Approved master files | 1 day |
| 5. Distribution | Upload to Meta / TikTok Ads Manager, set budget | Performance Marketer, Media Buyer | Meta Ads, TikTok Ads, Triple Whammy | Live ad set | 0.5 day |
| 6. Post-launch | ROAS / CTR / hook-rate analysis, kill or scale | Performance Marketer, Data Analyst | Meta Reports, Northbeam, Triple Whale | Winners → scale; losers → iterate | 7–14 days |

**Critic loop**: Andrew Foxwell / Mari Smith ad-account audit pattern; benchmark hook-rate >30%, CTR >1.5%, ROAS > breakeven.

---

### C. Animated explainer (60–180s)

![Workflow C diagram — Animated explainer](workflows/C-animated-explainer.svg)

| Phase | Step | Crew | Tools / Method | Deliverable | Typical Time |
|-------|------|------|----------------|-------------|--------------|
| 1. Concept | Discovery call, learning objectives, audience | Instructional Designer, Brand Strategist, SME | Stakeholder interviews, ADDIE analysis | Creative brief + objectives | 3–5 days |
| 1. Concept | Script (problem → agitate → solve → CTA) | Scriptwriter, SME | Google Docs, Hemingway editor | Approved script (~150 words/min) | 5–7 days |
| 1. Concept | Storyboard + style frames | Storyboard Artist, Art Director | Storyboarder, Figma, Procreate | Approved boards + style frame | 5–7 days |
| 2. Production | Voice-over record | VO Artist, Sound Engineer | Pro Tools, treated booth | Final VO WAV | 1 day |
| 2. Production | Animate scenes | 2D Animator, Motion Designer | After Effects, Rive, Lottie | Animated scenes | 7–14 days |
| 2. Production | Original score + SFX | Composer, Sound Designer | Logic / Cubase + sample libs | Music stems + SFX bed | 3–5 days |
| 3. Post | Edit, color, final mix | Editor, Re-recording Mixer | Premiere / Resolve | Master at -16 LUFS (web) | 2–3 days |
| 4. Review | SME accuracy, brand check, accessibility | SME, Brand Manager, Accessibility Specialist | WCAG 2.2 contrast/caption review | Approved master + SRT + audio description | 2 days |
| 5. Distribution | Embed on landing page, YouTube, sales decks | Marketing Manager, SEO Specialist | YouTube, Wistia, Vimeo | Live across channels | 1 day |
| 6. Post-launch | Completion rate, on-page conversion lift | Marketing Analyst, Instructional Designer | Wistia heatmaps, GA4 | Recut weak segments (<50% completion) | Ongoing |

**Critic loop**: Cathy Moore *Action Mapping* review + Julie Dirksen learning-design audit; target completion >70%.

---

### D. Personalized birthday video (15–60s)

![Workflow D diagram — Personalized birthday video](workflows/D-personalized-birthday.svg)

| Phase | Step | Crew | Tools / Method | Deliverable | Typical Time |
|-------|------|------|----------------|-------------|--------------|
| 1. Concept | Template design (variable: name, age, photo, voice) | Template Designer, Motion Designer, Copywriter | After Effects + Bodymovin / Idomoo | Reusable template with variable slots | 5–10 days (one-time) |
| 1. Concept | Personalization data schema + intake form | Personalization Engineer, UX Designer | Typeform, JSON schema | Form + data contract | 2 days |
| 2. Production | User submits name/photo/song choice | (Self-service end-user) | Web form / app | Submitted asset bundle | <5 min/user |
| 2. Production | Render personalized variant | Personalization Engineer, AI Voice Operator | ffmpeg, Bannerbear, ElevenLabs voice | Rendered MP4 per user | 30s – 5 min/user |
| 3. Post | Automated QC (face/name detect, audio levels) | AI QA Reviewer (automated + spot-check human) | OpenCV checks, loudness scan | Pass/fail flag | Automated |
| 4. Review | Spot-check 1 in 50, abuse / consent check | Personalization Engineer, Trust & Safety | Manual review queue | Approved batch | Ongoing |
| 5. Distribution | Email / WhatsApp / in-app delivery | CRM Specialist, Backend Engineer | Klaviyo, Twilio, WhatsApp Business API | Delivered video | Instant |
| 6. Post-launch | Open / share / re-gift rate, NPS | Product Analyst, CRM Specialist | Mixpanel, Amplitude | Template optimization (which template wins) | Weekly |

**Critic loop**: DMA peer audit + GDPR/CCPA privacy review; target share-rate >25% (gifted videos go viral).

---

### E. AI multi-scene short film (1–5 min)

![Workflow E diagram — AI multi-scene short film](workflows/E-ai-short-film.svg)

| Phase | Step | Crew | Tools / Method | Deliverable | Typical Time |
|-------|------|------|----------------|-------------|--------------|
| 1. Concept | Logline + treatment | Writer / Director | Notion, Final Draft | 1-page treatment | 2–3 days |
| 1. Concept | Scene breakdown + storyboard | Storyboard Artist, Director | Storyboarder, Midjourney for refs | Beat-by-beat board (10–30 scenes) | 3–5 days |
| 1. Concept | Character sheets + style bible (consistency) | Concept Artist, AI Avatar Designer | Midjourney, Flux, character LoRAs | Locked character refs + seeds | 3–5 days |
| 2. Production | Scene generation pass 1 (rough) | AI Prompt Engineer, AI Generator Op | Sora, Veo 3, Runway Gen-4, Kling | Rough clips per scene | 3–7 days |
| 2. Production | Consistency / re-roll passes | AI QA / Consistency Reviewer | Frame-by-frame review, re-prompt | Cleaned clips | 3–5 days |
| 2. Production | Voice + dialogue + lip-sync | VO Artist (or AI Voice Cloner), Lip-Sync Specialist | ElevenLabs, Sync.so, Hedra | Lip-synced dialogue | 2–3 days |
| 2. Production | Original score + sound design | Composer, Sound Designer | DAW + sample libs | Music + SFX bed | 3–5 days |
| 3. Post | Edit, color grade, VFX cleanup | Editor, Colorist, VFX Compositor | Resolve, Nuke, Topaz Video AI (upscale) | Picture lock master | 5–7 days |
| 4. Review | Festival cut review, director's notes | Director, Editor, Peer Filmmakers | Private Vimeo screening + notes round | Final cut | 3–5 days |
| 4. Review | Provenance + AI disclosure | Legal Reviewer, AI Avatar Designer | C2PA content credentials | Signed master with provenance | 1 day |
| 5. Distribution | Festival submissions + YouTube + curated platforms | Producer, Festival Strategist | FilmFreeway, Runway AI Film Fest, Curious Refuge | Submissions live | 1 day (rolling) |
| 6. Post-launch | Festival feedback, audience reaction | Director, Producer | Q&A notes, watch-time analytics | Director's cut v2, sequel plan | Ongoing |

**Critic loop**: Runway AI Film Festival jury, Curious Refuge community critique, Paul Trillo / Karen X. Cheng peer review on craft + consistency.

---

### F. Corporate training video (3–10 min)

![Workflow F diagram — Corporate training video](workflows/F-corporate-training.svg)

| Phase | Step | Crew | Tools / Method | Deliverable | Typical Time |
|-------|------|------|----------------|-------------|--------------|
| 1. Concept | Training needs analysis + learning objectives | Instructional Designer, L&D Lead, SME | ADDIE, Kirkpatrick model | Learning-design doc | 5–7 days |
| 1. Concept | Compliance / legal review of content | Compliance Officer, Legal Reviewer | Internal policy library | Approved content outline | 3–5 days |
| 1. Concept | Script + scenario design | Scriptwriter, Instructional Designer | Articulate Storyline storyboard | Approved script | 5–7 days |
| 2. Production | Shoot presenter / record avatar | Presenter (or Avatar), DoP, Sound Recordist | Camera + lav + teleprompter, or Synthesia/HeyGen | Raw footage / avatar render | 1–3 days |
| 2. Production | Screen-recordings, animation, infographics | Screen-Recordist, Motion Designer | Camtasia, After Effects | B-roll assets | 3–5 days |
| 3. Post | Edit, captions (mandatory), audio description | Editor, Captioner, Accessibility Specialist | Premiere + Rev captions | Master + SRT + WebVTT | 3–5 days |
| 4. Review | SME accuracy + compliance sign-off + accessibility (WCAG 2.2) | SME, Compliance Officer, Accessibility Specialist | Sign-off checklist | Approved final | 2–3 days |
| 5. Distribution | Upload to LMS + assign + track completion | LMS Specialist, L&D Lead | Cornerstone, Workday Learning, Docebo | Course assigned to cohort | 1 day |
| 6. Post-launch | Completion %, quiz scores, behavior change | L&D Analyst, Instructional Designer | LMS analytics, Kirkpatrick L1–L4 | Module revision v2 | 30 / 60 / 90 day reviews |

**Critic loop**: Cathy Moore action-mapping audit + ATD (Association for Talent Development) peer review; target completion >85%, L2 quiz >80%.

---

### G. Music video (live + AI VFX, 1–4 min)

![Workflow G diagram — Music video with AI VFX](workflows/G-music-video.svg)

| Phase | Step | Crew | Tools / Method | Deliverable | Typical Time |
|-------|------|------|----------------|-------------|--------------|
| 1. Concept | Treatment from song + artist meeting | Music Video Director, Artist, Label A&R | Treatment deck w/ refs | Approved treatment | 3–7 days |
| 1. Concept | Locations, casting, choreography | Producer, Casting Director, Choreographer | Recce, casting calls | Locked locations + cast | 7–14 days |
| 1. Concept | Shot list + lookbook | Director, DoP, Storyboard Artist | Shot Lister, lookbook PDF | Shot list | 3–5 days |
| 2. Production | Shoot day(s) | Director, DoP, Camera Op, Gaffer, Grip, Choreographer, Talent, MUA, Costume | Cinema cameras, lighting package | Raw footage + sound | 1–3 days |
| 2. Production | AI VFX plate generation (style transfer, world expansion) | AI Generator Op, VFX Supervisor | Runway, Wonder Studio, Kaiber | AI VFX plates | 3–7 days |
| 3. Post | Edit to music, color grade, VFX comp | Editor, Colorist, VFX Compositor | Premiere / Resolve, Nuke | Picture-lock | 5–10 days |
| 3. Post | Sound mix (music master + SFX) | Re-recording Mixer | Pro Tools | Final mix to song master | 1–2 days |
| 4. Review | Artist + label approval, rights clearance | Label A&R, Music Supervisor, Legal | Sample clearance, sync rights | Cleared master | 3–5 days |
| 5. Distribution | YouTube premiere + Vevo + Shorts cutdowns | Label Digital Team, Social Strategist | YouTube CMS, Vevo, TikTok | Live premiere | 1 day |
| 6. Post-launch | Views, retention, chart impact, Shorts virality | Label Analyst, Social Strategist | YouTube Analytics, Chartmetric | Cutdown strategy, remix videos | 14–30 days |

**Critic loop**: MTV VMA / UKMVA jury benchmarks; Hype Williams / Dave Meyers craft references; Chartmetric streaming-lift attribution.

---

### H. AI avatar talking-head (30–120s)

![Workflow H diagram — AI avatar talking-head](workflows/H-ai-avatar.svg)

| Phase | Step | Crew | Tools / Method | Deliverable | Typical Time |
|-------|------|------|----------------|-------------|--------------|
| 1. Concept | Use case + brand persona for avatar | Brand Strategist, Avatar Designer | Persona doc | Approved avatar persona | 2–3 days |
| 1. Concept | Script + tone | Scriptwriter, Brand Manager | Google Docs | Approved script | 1–2 days |
| 2. Production | Build / pick avatar + voice | AI Avatar Designer, Voice Designer | Synthesia, HeyGen, D-ID, ElevenLabs | Avatar + voice locked | 1 day (or 3–5 days for custom clone with consent) |
| 2. Production | Generate video (TTS + lip sync) | AI Generator Op, Lip-Sync Specialist | Synthesia / HeyGen render | Raw avatar render | <1 hr |
| 3. Post | B-roll overlays, captions, brand template | Motion Designer, Editor | After Effects, CapCut | Final MP4 + SRT | 0.5–1 day |
| 4. Review | Pronunciation pass, brand check, AI disclosure | Brand Manager, Legal Reviewer | C2PA credentials, AI-content label | Approved master | 0.5 day |
| 5. Distribution | LinkedIn, help center, intranet, email | Marketing / Comms | LinkedIn, Zendesk, Loom | Live | 0.5 day |
| 6. Post-launch | Engagement + comprehension survey | Comms Analyst | LinkedIn analytics, survey | Persona / script refinement | Weekly |

**Critic loop**: Hany Farid (deepfake-detection rigor), Nina Schick (synthetic-media ethics); Partnership on AI Synthetic Media Framework audit.

---

### I. Documentary-style "explained" episode (5–15 min)

![Workflow I diagram — Documentary explained episode](workflows/I-documentary.svg)

| Phase | Step | Crew | Tools / Method | Deliverable | Typical Time |
|-------|------|------|----------------|-------------|--------------|
| 1. Concept | Topic pitch + angle | Showrunner, Researcher | Pitch doc | Greenlit episode | 7–14 days |
| 1. Concept | Deep research + interview list | Researcher, Producer, Fact-Checker | Academic DBs, FOIA, interviews | Research bible + sources | 14–21 days |
| 1. Concept | Script + visual plan | Scriptwriter, Director, Producer | Final Draft, shot plan | Approved script | 7–10 days |
| 2. Production | Interviews + B-roll shoot | Director, DoP, Sound Recordist, Producer | Cinema kit, lavs, archive license | Raw interviews + B-roll | 3–10 days |
| 2. Production | Archive footage / stills licensing | Archive Producer, Legal | Getty, AP Archive | Cleared archive | 5–10 days |
| 2. Production | Motion graphics + data viz | Motion Designer, Data Visualization Designer | After Effects, D3.js renders | Animated explainers | 5–10 days |
| 3. Post | Edit, narration record, color, mix | Editor, Narrator, Colorist, Re-recording Mixer | Premiere / Resolve, Pro Tools | Picture + sound lock | 14–21 days |
| 4. Review | Fact-check every claim + legal review | Fact-Checker, Legal Reviewer | Source-by-source checklist | Cleared master | 5–7 days |
| 4. Review | Editorial standards review (per SPJ) | Editor-in-Chief, Standards Editor | Newsroom standards doc | Approved | 2 days |
| 5. Distribution | YouTube release + podcast clip + newsletter | Channel Manager, Social Strategist, SEO | YouTube CMS, Thumbsmith for thumbnails | Live episode + clips | 1 day |
| 6. Post-launch | CTR, AVD, audience retention curve, corrections | Channel Analyst, Standards Editor | YouTube Studio, errata page | Pinned corrections + next-ep learnings | Ongoing |

**Critic loop**: Pulitzer / duPont-Columbia / Peabody standards; Columbia Journalism Review post-mortem; Poynter ethics review.

---

### J. Feature-length AI film (60–120 min)

![Workflow J diagram — Feature-length AI film](workflows/J-feature-film.svg)

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

**Critic loop**: Sundance / Cannes / Venice juries, Roger Ebert-style critic press, AMPAS members for awards qualification, AI Film Festival circuit (Runway, AIFF); benchmark: ≥85 Metacritic, festival selection, profitable distribution deal.

---

### Workflow Universals (apply to every archetype)

| Universal Step | When | Owned By | Why It Matters |
|----------------|------|----------|----------------|
| **Brief / one-pager sign-off** | Before any production | Producer + Client | Prevents scope creep |
| **Music & footage licensing** | Before publish | Producer / Legal | Avoids takedowns and lawsuits |
| **AI provenance (C2PA)** | At master export | Legal / AI Operator | Required by EU AI Act, many platforms |
| **Accessibility pass (captions, AD, contrast)** | Before publish | Accessibility Specialist | WCAG 2.2 + ADA compliance |
| **Backup + archival (LTO / cloud)** | At wrap | Post Producer | Future-proofs IP and recuts |
| **Post-launch retro** | 7–30 days after launch | Producer | Compounds learnings into next production |




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

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 46 | PromptEngineerAgent | Crafts prompts; steers gen models | — |
| 47 | AvatarDesignAgent | Synthetic presenter identity | — |
| 48 | VoiceCloneAgent / LipSync | Voice cloning + lip-sync | — |
| 49 | AIQAConsistencyAgent | Frame drift, artifacts, identity breaks | — |
| 50 | PersonalizationEngineerAgent | Variable templates (name/face swap) | — |
| 51 | TrailerEditorAgent | Hook-driven trailer cuts | — |
| 52 | SportsAnalystAgent | Tactical breakdowns + diagrams | — |

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

```json
{
  "from_agent": "EditorAgent",
  "to_agent": "DirectorAgent",
  "critique_type": "pacing_feedback",
  "severity": "suggestion",
  "artifact_ref": "artifact_id_123_v2",
  "message": "Scene 3 pacing exceeds genre-prior by 15%; suggest trim.",
  "rubric_score": 0.72,
  "timestamp": "2026-05-27T10:30:00Z"
}
```



### From `corpus/study/ai_agent_video_production_workflow.md` Copy: `sources/excerpts/ai_agent_video_production_workflow.md`.


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
| 19 | **SoundDesignAgent** | Ambience, foley, SFX | BBC SFX library; MPSE Golden Reel reels; Ben Burtt / Skip Lievsay design notes | Spectral diversity; on-screen sync ≤±1 frame; loudness target (-23 LUFS for broadcast) | Wins MPSE-style pairwise on horror/sci-fi reels | DirectorAgent, MixerAgent | EditorAgent (pacing-clashing FX), ComposerAgent (frequency masking) |
| 20 | **ComposerAgent** | Original score | MAESTRO + film-score corpora (licensed); ASCAP/BMI film-music monographs; transcribed Zimmer/Hildur sessions | Cue-to-emotion alignment (valence/arousal regression on viewer biosignal proxy); thematic recurrence | Wins blind pairwise on emotional-fit task vs working composers | DirectorAgent, EditorAgent (music cuts) | EditorAgent (cut interrupts cue), SoundDesignAgent (mask) |
| 21 | **VoiceOverAgent** | Narration, character VO, ad reads | SOVAS-winning reels; consented voice-actor corpora; coach methodologies (Wolfson/Cashman) | Prosody match to brief; pronunciation 100% on lexicon; emotion tag match | Beats junior VO in blind ad-read preference; matches senior on emotion | DirectorAgent, BrandAgent | ScriptwriterAgent (unspeakable phrasing) |
| 22 | **SoundMixerAgent (Re-recording)** | Final mix; deliverables (5.1/Atmos) | CAS Awards; Atmos renderer specs; broadcast loudness standards | LUFS target; dialogue intelligibility (STOI ≥0.85); spec-deliverable pass | Hits CAS spec on first pass without engineer rework | EditorAgent, SoundDesignAgent, AccessibilityAgent | SoundDesignAgent (over-design), ComposerAgent (level clash) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 23 | **ChoreographyAgent** | Movement design (music videos, dance challenges) | Emmy Choreography submissions; Parris Goebel/Mandy Moore reels; dance-notation datasets | Beat-sync accuracy; safety constraints; viral-pattern alignment | Wins blind preference vs choreographer drafts for short-form | DirectorAgent, MVDirectorAgent | DirectorAgent (un-camera-friendly staging) |
| 24 | **MusicVideoDirectorAgent** | Visual concept for songs | DirectorsLibrary.com; UKMVA/MTV VMA winners; Hype Williams / Spike Jonze reels | Edit-rhythm sync; lookbook coherence; artist-brief fit | Wins label-blind preference vs commercial MV director shortlist | LabelA&RAgent, ArtistAgent | EditorAgent (cut on beat), DoPAgent |
| 25 | **ComedyWriterAgent** | Skits, parody, viral meme writing | UCB/Groundlings manuals; SNL writers'-room transcripts; Schur/Fey teaching | Joke-density; cold-open hook strength; predicted laughs/min | Beats UCB-table-read win rate on cold-reads | AudienceSim, ShowrunnerAgent | ScriptwriterAgent (no joke), SocialStrategistAgent (off-trend) |
| 26 | **TalentAgent (On-camera)** | AI-rendered performance | Method-acting transcripts; consented actor performance corpora | Emotion-target match; charisma score (audience proxy) | Hold-rate matches top creators in cohort | DirectorAgent, CastingAgent | DirectorAgent (impossible blocking) |
| 27 | **UGCCreatorAgent** | Authentic-feel ads in creator voice | TikTok Creative Center reports; Alix-Earle-style benchmark posts (style not identity) | Hook-rate ≥30%; "scripted" detector score below threshold (low = good) | Beats paid-creator avg ROAS at 0.1× cost | PerformanceMarketerAgent, BrandAgent | PerformanceMarketerAgent (wrong audience) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 28 | **SocialMediaStrategistAgent** | Platform-native distribution, timing, trends | TikTok Creator Portal data; Meta Marketing Science; Tubular/Sensor Tower | Predicted-vs-actual reach error; trend-timing latency <2h | Beats agency social leads on 30-day reach lift | AnalystAgent, BrandAgent | CopywriterAgent (off-platform tone), EditorAgent (wrong aspect) |
| 29 | **CopywriterAgent** | Scripts, captions, hooks, headlines | D&AD/One Show winners; *Ogilvy on Advertising*; Joanna Wiebe Copyhackers | Reading grade; hook-curiosity score; brand-voice cosine similarity ≥0.85 | Wins D&AD-style blind preference on ad copy briefs | BrandAgent, PerformanceMarketerAgent | ScriptwriterAgent (verbosity), VOArtist (unspeakable) |
| 30 | **CreativeDirect
…



### From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


**Build:**
- **Agent Factory** (`packages/agent-factory`): `AgentConfig (YAML) → runnable BaseAgent`. Validates prompt/rubric/tools/QC refs; registers into `agents/_registry.yaml`; generates the per-agent test skeleton. This is the engine for M7–M9.
- **Workflow A craft agents** (subset, via factory): TrendIntelligenceAgent, CopywriterAgent, SocialMediaStrategistAgent, PromptEngineerAgent/GeneratorOperator, AIQAConsistencyAgent, EditorAgent, AccessibilityOptimizerAgent, AudienceSimAgent, AnalystAgent — exactly the crew in [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §3.1.
- **Workflow A DAG** (`workflows/A_viral_hook.py`): Concept → Production → Post → Review → Distribution → Post-launch, with the spec'd critic gates.
- End-to-end run: brief → DIA → Planner builds the A-DAG → agents execute (mock gen) → artifacts flow with handoff contract → critique bus active → QC mesh gates → C2PA-signed deliverable → events on the bus.

**Claude Code workflow:** Use `/new-agent <n>` per agent. Process category-by-category (camera 6–8, editorial/color 9–18, sound 19–22, performance 23–27, marketing 28–31, domain 32–45, AI-era 46–52). `/clear` between categories. For each agent, `spec-reader` pulls its exact row (self-quality, surpass signal, critique edges) → factory config → test → review.

**Tests:** every agent: L1 schema conformance; L2 rubric ≥85 on its golden inputs; emits/accepts critique per the matrix; respects its tool allowlist; metered. Category-level integration tests (e.g., DoP→Colorist→Editor handoff preserves continuity_state).

**Build:**
- **Psychological Profiling** (100 creator profiles: MBTI, motivations, fears, creative params) → feeds Casting/Talent/Personalization/UGC agents and Aesthetic-Agent *audience-cohort profiles*.
- **Psychological Recommendation** (Big Five / emotional-state preference prediction) → AudienceSim, PerformanceMarketer, Personalization.
- **PersonalizationEngineerAgent** templating (name/face/voice swap) with privacy/consent audit (GDPR/CCPA via ComplianceAgent).
- **Podcast Agent** audio-first workflow (preparation → execution → ending → follow-up), reusing VO/SoundMixer/Editor.

**Steps:**
1. **Read (subagent).** `spec-reader` extracts the six fields above into a structured `AgentBrief`.
2. **Map self-quality → metrics.** Convert "Self-Quality Criteria" into concrete `MetricSpec`s with thresholds (e.g., DoP `rule_of_thirds>=τ, exposure_zone∈[III,VII], color_temp_var<=ΔK`; Colorist `deltaE<2`; SoundMixer `lufs==target, stoi>=0.85`). Many map to existing `packages/qc` validators or the Aesthetics Agent.
3. **Author the L2 rubric/constitution.** Turn "Surpass-Human Signal" + craft sources into a role constitution in `eval/rubrics/<agent>.yaml` (this is what LLM-as-judge scores against). Cite the craft authority named in the spec (Murch's Rule of Six for Editor, 12 principles for Animator, etc.).
4. **Define tools.** Allowlist only the providers/tools this agent may call (e.g., PromptEngineer → MediaGenProvider; Colorist → grade tool; FactChecker → RAG + WebResearch). Enforced by `agent-core`.
5. **Wire critique edges.** From the §4 critique matrix: `critiques_from` and `critiques_on`. ComplianceAgent edges are always blocking.
6. **Write the AgentConfig (YAML)** and register in `agents/_registry.yaml`.
7. **Author the versioned system prompt** (`agents/.../prompt.vN.md`) embedding role, constitution summary, self-refine instruction, and output schema (must emit a valid `Artifact`).
8. **TDD (subagent `test-author`):** golden-input fixtures → assert L1 schema pass, L2 rubric ≥85, correct critique emission/acceptance, tool-allowlist enforcement, metering present, provenance populated.
9. **Implement = instantiate.** `AgentFactory.build(config)` — no new code path; if you find yourself writing bespoke logic, that logic belongs in `agent-core` or a tool, not the agent.
10. **Review (subagent `code-reviewer`)** against DoD + §14 themes; fix; commit `feat(agent-<n>): <Name>`.
11. **Register in workflows** that use it; extend the relevant archetype integration test.



### From `corpus/root/project_starter_0.2.md` Copy: `sources/excerpts/project_starter_0.2.md`.


```text  
project_starter/  
├── AGENTS.md  
├── CLAUDE.md  
├── GEMINI.md  
├── README.md  
├── package.json  
├── task.md  
├── status.md  
├── .gitignore  
├── .editorconfig  
├── .claude/  
├── .cursor/  
├── .codex/  
├── .gemini/  
├── .github/  
│   ├── workflows/  
│   └── copilot-instructions.md  
├── agents/  
├── skills/  
│   ├── manifest.json  
│   ├── manifest.schema.json  
│   ├── planning/  
│   ├── implementation/  
│   ├── testing/  
│   ├── review/  
│   ├── security/  
│   ├── memory/  
│   └── lifecycle/  
├── rules/  
│   ├── manifest.json  
│   ├── 00-constitution.md  
│   ├── 10-karpathy.md  
│   ├── 20-sdd.md  
│   ├── 30-security.md  
│   ├── 40-testing.md  
│   ├── 50-token-efficiency.md  
│   └── 60-human-approval.md  
├── hooks/  
│   ├── manifest.json  
│   ├── specs/  
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
├── scripts/  
│   ├── project-starter.mjs  
│   ├── sync.mjs  
│   ├── doctor.mjs  
│   ├── security.mjs  
│   ├── review.mjs  
│   ├── adapters/  
│   │   ├── claude.mjs  
│   │   ├── cursor.mjs  
│   │   ├── codex.mjs  
│   │   ├── opencode.mjs  
│   │   ├── gemini.mjs  
│   │   ├── grok-build.mjs  
│   │   └── copilot.mjs  
│   └── lib/  
├── docs/  
│   ├── installation.md  
│   ├── usage.md  
│   ├── architecture.md  
│   ├── decisions.md  
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
    ├── sync.test.mjs  
    ├── manifest.test.mjs  
    └── adapters.test.mjs  
```

- [ ] Initialize Git repo named `project_starter`.  
- [ ] Add `package.json` with scripts:  
  - `init`  
  - `sync`  
  - `sync:check`  
  - `doctor`  
  - `security`  
  - `review`  
  - `test`  
  - `format`  
- [ ] Implement `scripts/project-starter.mjs` command router.  
- [ ] Implement `scripts/doctor.mjs` to check:  
  - Node version  
  - Git availability  
  - OS  
  - symlink capability  
  - Claude/Cursor/Codex/Gemini/OpenCode/Grok availability when installed  
  - required directories  
- [ ] Add `.editorconfig`, `.gitignore`, `README.md`, and base docs.  
- [ ] Add empty manifests with JSON schemas.  
- [ ] Add first `task.md` and `status.md`.



### From `corpus/root/project_starter_0.3.md` Copy: `sources/excerpts/project_starter_0.3.md`.


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



### From `corpus/root/project_starter_0.4.md` Copy: `sources/excerpts/project_starter_0.4.md`.


```text
<PROJECT_NAME>/
├── project_starter.md
├── README.md
├── package.json
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── task.md
├── status.md
├── .gitignore
├── .editorconfig
├── sources/
│   ├── manifest.json
│   ├── docs-manifest.json
│   └── source-lock.json
├── scripts/
│   ├── bootstrap.mjs
│   ├── doctor.mjs
│   ├── create-project.mjs
│   ├── download-sources.mjs
│   ├── audit-sources.mjs
│   ├── security-check.mjs
│   ├── sync-agent-configs.mjs
│   ├── test.mjs
│   └── utils/
│       ├── fs.mjs
│       ├── git.mjs
│       ├── log.mjs
│       └── project.mjs
├── rules/
│   ├── universal-rules.md
│   ├── safety-rules.md
│   ├── coding-rules.md
│   ├── git-rules.md
│   ├── testing-rules.md
│   └── source-rules.md
├── skills/
│   ├── planning.md
│   ├── debugging.md
│   ├── refactoring.md
│   ├── testing.md
│   ├── documentation.md
│   └── security-review.md
├── hooks/
│   ├── pre-task.md
│   ├── post-task.md
│   └── pre-commit.md
├── mcp-configs/
│   ├── README.md
│   └── example.mcp.json
├── memory/
│   ├── project-memory.md
│   ├── decisions.md
│   └── glossary.md
├── docs/
│   ├── architecture.md
│   ├── setup.md
│   ├── usage.md
│   ├── source-audit.md
│   ├── agents.md
│   ├── troubleshooting.md
│   └── changelog.md
├── tests/
│   ├── smoke.test.mjs
│   └── fixtures/
│       └── README.md
└── external/
    └── sources/
        └── .gitkeep
```



### From `corpus/root/project_starter_0.5.md` Copy: `sources/excerpts/project_starter_0.5.md`.


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



### From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


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
| 19 | **SoundDesignAgent** | Ambience, foley, SFX | BBC SFX library; MPSE Golden Reel; Burtt/Lievsay notes | Spectral diversity; sync ≤±1 frame; loudness -23 LUFS | Wins MPSE pairwise on horror/sci-fi | DirectorAgent, MixerAgent | EditorAgent (FX clash), ComposerAgent (masking) | ElevenLabs Sound FX API; Freesound; FFmpeg spectral analysis; Dolby.io loudness API | ReAct (search SFX lib → validate sync → mix) |
| 20 | **ComposerAgent** | Original score | MAESTRO + film-score corpora; ASCAP/BMI; Zimmer/Hildur sessions | Cue-to-emotion alignment (valence/arousal regression); thematic recurrence | Wins blind pairwise on emotional-fit vs working composers | DirectorAgent, EditorAgent (music cuts) | EditorAgent (cut interrupts cue), SoundDesignAgent (mask) | Udio/Suno music gen API; MIDI toolchain; stem-separation (Demucs); loudness meter | Self-Refine + Emotional-Arc validation (biosignal proxy) |
| 21 | **VoiceOverAgent** | Narration, character VO, ad reads | SOVAS reels; consented voice corpora; Wolfson/Cashman coaching | Prosody match; pronunciation 100%; emotion tag match | Beats junior VO in blind preference; matches senior on emotion | DirectorAgent, BrandAgent | ScriptwriterAgent (unspeakable phrasing) | ElevenLabs v3 TTS + voice cloning; Resemble.AI; pronunciation lexicon API | LLM-as-Judge (MOS scoring rubric) |
| 22 | **SoundMixerAgent (Re-recording)** | Final mix; deliverables (5.1/Atmos) | CAS Awards; Atmos specs; broadcast loudness standards | LUFS target; STOI ≥0.85; spec-deliverable pass | CAS spec on first pass without rework | EditorAgent, SoundDesignAgent, AccessibilityAgent | SoundDesignAgent (over-design), ComposerAgent (level) | Dolby Atmos Renderer API; LUFS/loudness measurement tools; DaVinci Fairlight MCP | Constitutional AI (constitution: broadcast-spec rules) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 23 | **ChoreographyAgent** | Movement design (MVs, dance challenges) | Emmy Choreography submissions; Goebel/Moore reels; dance-notation datasets | Beat-sync accuracy; safety constraints; viral-pattern alignment | Wins blind preference vs choreographer drafts | DirectorAgent, MVDirectorAgent | DirectorAgent (un-camera-friendly staging) | Kling 3.0 motion control (reference video); Cascadeur; beat-detection (librosa) | Self-Refine (rubric: beat-sync + safety) |
| 24 | **MusicVideoDirectorAgent** | Visual concept for songs | DirectorsLibrary; UKMVA/MTV VMA winners; Hype Williams/Spike Jonze | Edit-rhythm sync; lookbook coherence; artist-brief fit | Wins label-blind preference vs commercial MV shortlist | LabelA&RAgent, ArtistAgent | EditorAgent (cut on beat), DoPAgent | Runway Gen-4 (style-locked generation); Veo 3.1; mood-board tools (Are.na API) | Multi-agent debate (with DirectorAgent + EditorAgent) |
| 25 | **Comed
…



### From `corpus/study/ui/agent_management_ui.md` Copy: `sources/excerpts/agent_management_ui.md`.


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
```

```text
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



### From `corpus/study/ui/backend_agent_management.md` Copy: `sources/excerpts/backend_agent_management.md`.


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

```text
DirectorAgent                    Backend                      EditorAgent
     │                              │                              │
     │  (completes shot intent)     │                              │
     │──publish: artifact_created──►│                              │
     │                              │                              │
     │                              │──(checks: who comments on    │
     │                              │   DirectorAgent's output?)   │
     │                              │                              │
     │                              │──deliver critique task──────►│
     │                              │                              │
     │                              │                              │
     │                              │◄──critique: "pacing too fast"│
     │                              │                              │
     │                              │──(checks: DirectorAgent      │
     │                              │   accepts critique from       │
     │                              │   EditorAgent? YES)           │
     │                              │                              │
     │◄──deliver critique──────────│                              │
     │                              │                              │
     │  (on next iteration,         │                              │
     │   incorporates feedback)     │                              │
```

│
                         ▼
              All publish events to Event Bus
              Orchestrator coordinates dependencies:
              "EditorAgent can't start until DirectorAgent
               completes ALL shots for this scene"
```

```python
# Dependency rules (encoded in the DAG)
dependencies = {
    "editor_assemble": {
        "requires": ["director_all_shots_complete", "composer_score_ready"],
        "gate": "production_gate_passed"
    },
    "colorist_grade": {
        "requires": ["editor_rough_cut_complete"],
    },
    "sound_mix": {
        "requires": ["sound_design_complete", "composer_final_mix"],
    }
}

DirectorAgent-service ──┐
  EditorAgent-service ────┤── all running simultaneously
  ComposerAgent-service ──┤
  ... 114 services ───────┘



### From `corpus/study/ui/production_scale_discovery.md` Copy: `sources/excerpts/production_scale_discovery.md`.


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
│  │               (changes style/duration/audience)            │   │
│  │                                                           │   │
│  │  [❤️ Save to Inspiration Board]                            │   │
│  │                                                           │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```



### From `corpus/study/ui/project_creation_flow.md` Copy: `sources/excerpts/project_creation_flow.md`.


┌─────────────────────────────────────────────────────────────────┐
│  PROJECT "Brand Campaign Q3"                                     │
│  (free to create, free to hold, free to plan)                    │
│                                                                 │
│  ├── Shared Assets: brand kit, voices, style refs               │
│  ├── Team: owner + editors + reviewers                          │
│  ├── Budget Pool: $240 allocated                                │
│  ├── Default Settings: compliance, models, platforms            │
│  │                                                              │
│  ├── Production 1: "Hero Video" (Type E, completed ✓, $62)     │
│  ├── Production 2: "TikTok Cut" (Type A, running ●, $28)       │
│  └── Production 3: "Training" (Type F, DRAFT ○, $0)            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

```text
┌──────────────────────────────────────────────────────────────────┐
│  CREATE NEW PROJECT                                    [×]        │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Project Name: [________________________________]                │
│                                                                  │
│  Description (optional):                                         │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ e.g., "Q3 brand awareness campaign across social + web"  │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─── BUDGET POOL ──────────────────────────────────────────┐    │
│  │  Total budget for all productions: $[_____]               │    │
│  │  ☐ No limit (pay as you go)                               │    │
│  │  Billing method: [Credit card ending 4242 ▼]              │    │
│  └───────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─── TEAM (optional — add later) ──────────────────────────┐    │
│  │  You: Owner                                               │    │
│  │  [+ Invite]  ______@email.com  Role: [Editor ▼]           │    │
│  │                                                           │    │
│  │  Roles:                                                   │    │
│  │  • Owner — full control, billing, delete                  │    │
│  │  • Editor — create/launch productions, manage assets      │    │
│  │  • Reviewer — view, comment, approve gates                │    │
│  │  • Viewer — read-only access                              │    │
│  └───────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─── DEFAULTS (apply to all productions unless overridden) ─┐    │
│  │  Compliance: ☑ C2PA  ☑ WCAG AA  ☐ SAG-AFTRA  ☐ GDPR     │    │
│  │  Model preference: [Cost-optimized ▼]                      │    │
│  │    Options: Cost-optimized │ Quality-first │ Speed-first   │    │
│  │  Brand kit: [Upload now ▼] or [Add later]                 │    │
│  └───────────────────────────────────────────────────────────┘    │
│                                                                  │
│              [ Cancel ]           [ Create Project ]              │
│                                                                  │
│  ℹ️ Creating a project is free. You're only charged when you      │
│    launch a production.                                          │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  PROJECT: "Brand Campaign Q3"                    [Archive] [Settings ⚙]     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TABS: [Overview] [Productions] [Assets] [Team] [Settings] [Activity]       │
│                                                                             │
├─── OVERVIEW TAB ────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── STATUS CARDS ────────────────────────────────────────────────────┐    │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐   │    │
│  │  │Productions │  │  Budget    │  │   Team     │  │  Assets    │   │    │
│  │  │     3      │  │ $90/$240   │  │  3 members │  │  12 files  │   │    │
│  │  │ 1✓ 1● 1○  │  │ 38% used   │  │            │  │            │   │    │
│  │  └────────────┘  └────────────┘  └────────────┘  └────────────┘   │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── PRODUCTIONS ─────────────────────────────────────────────────────┐    │
│  │                                                                     │    │
│  │  [+ New Production]     Sort: [Recent ▼]    Filter: [All ▼]         │    │
│  │                                                                     │    │
│  │  ┌─────────────────────────────────────────────────────────────┐    │    │
│  │  │ ✓ "Hero Video"        │ Type E │ Completed 2 days ago      │    │    │
│  │  │   Cost: $62 │ Duration: 5:20 │ Delivered: YouTube, TikTok  │    │    │
│  │  │   [View Artifacts]  [View Analytics]  [Duplicate as Draft]  │    │    │
│  │  └─────────────────────────────────────────────────────────────┘    │    │
│  │                                                                     │    │
│  │  ┌─────────────────────────────────────────────────────────────┐    │    │
│  │  │ ● "TikTok Cut"        │ Type A │ Running — Production phase│    │    │
│  │  │   Cost: $28 │ Progress: 55% │ ETA: 2 min                   │    │    │
│  │  │   [Open Console]  [Pause]                                   │    │    │
│  │  └─────────────────────────────────────────────────────────────┘    │    │
│  │                                                                     │    │
│  │  ┌─────────────────────────────────────────────────────────────┐    │    │
│  │  │ ○ "Training Module"   │ Type F │ DRAFT — not launched       │    │    │
│  │  │   Cost: $0 │ Brief: 80% complete │ Est. cost: ~$35          │    │    │
│  │  │   [Edit Brief]  [Get Estimate]  [▶ Launch]  [Delete]        │    │    │
│  │  └─────────────────────────────────────────────────────────────┘    │    │
│  │                                                                     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── RECENT ACTIVITY ─────────────────────────────────────────────────┐    │
│  │  • 2m ago: "TikTok Cut" — EditorAgent completed rough cut          │    │
│  │  • 5m ago: "TikTok Cut" — Gate #1 approved by you                  │    │
│  │  • 2d ago: "Hero Video" — Delivered to YouTube + TikTok            │    │
│  │  • 3d ago: Sarah joined as Reviewer                                │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```text
ROOT
├── Dashboard
│   ├── My Projects (grid)
│   ├── Active Productions (across all projects)
│   └── Quick Start (template picker → auto-project)
│
├── Project Workspace (per-project)          ← NEW
│   ├── Overview (status cards, productions list, activity)
│   ├── Productions (list with status: draft/running/complete)
│   ├── Assets (shared brand kit, voices, refs, docs)
│   ├── Team (members, roles, invitations)
│   ├── Settings (budget, defaults, compliance, models)
│   └── Activity (log of all project events)
│
├── Production Draft (per-production, pre-launch)  ← NEW
│   ├── Brief Editor (full editable form)
│   ├── Cost Estimate Preview
│   ├── Team Comments
│   └── Launch Button
│
├── Production Console (per-production, post-launch)  ← EXISTING
│   ├── DAG Canvas
│   ├── Timeline View
│   ├── Artifact Gallery
│   ├── Critique Feed
│   ├── Gate Control
│   └── Agent Inspector
│
├── Agent Registry                           ← EXISTING
├── Memory & Knowledge                       ← EXISTING
├── Delivery Hub                             ← EXISTING
├── Settings & Admin                         ← EXISTING
└── Help & Docs                              ← EXISTING
```

// Team
  members: {
    user_id: string;
    role: "owner" | "editor" | "reviewer" | "viewer";
    joined_at: Date;
  }[];

System auto-creates:
  • Project: "Untitled Project" (can rename later)
  • Production: "Viral Hook" (pre-filled brief)
  • Lands on Brief Editor in draft mode



### From `corpus/study/ui/RETHINK_100_IMPROVEMENTS.md` Copy: `sources/excerpts/RETHINK_100_IMPROVEMENTS.md`.


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



### From `corpus/study/ui/ui_design.md` Copy: `sources/excerpts/ui_design.md`.


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
┌─────────────────────────────────────────────────────────────────────────────┐
│  ARTIFACT GALLERY                      [Grid ▣] [List ≡]  Filter: [All ▼]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │ ▶ ░░░░░░░░░  │  │ ▶ ░░░░░░░░░  │  │   ┌─────┐   │  │  📄           │   │
│  │   Shot 1     │  │   Shot 2     │  │   │mood │   │  │  screenplay   │   │
│  │   v3 ✓      │  │   v2 ●      │  │   │board│   │  │  v4 ✓        │   │
│  │   by DoP     │  │   by DoP     │  │   └─────┘   │  │  by Writer    │   │
│  │   CLIP: 0.35 │  │   CLIP: 0.31 │  │  Concept v2 │  │  Beats: 12/12 │   │
│  │  [C2PA ✓]    │  │  [C2PA ✓]    │  │  by Concept │  │  [C2PA ✓]     │   │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘   │
│                                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │ 🎵 ─────     │  │ 🎵 ─────     │  │ ▶ ░░░░░░░░░  │  │  📊 Chart    │   │
│  │  Score Cue 1 │  │  SFX Pack    │  │  Rough Cut   │  │  Quality     │   │
│  │  v1 ●       │  │  v2 ✓       │  │  v1 ⚠       │  │  Report      │   │
│  │  by Composer │  │  by SoundDes │  │  by Editor   │  │  by QA       │   │
│  │  Mood: 0.88  │  │  Sync: ✓     │  │  Pacing: B+  │  │  VBench: 0.8 │   │
│  │  [C2PA ✓]    │  │  [C2PA ✓]    │  │  [C2PA ✓]    │  │              │   │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘   │
│                                                                             │
│  Showing 8 of 47 artifacts │ Page [1] 2 3 4 5 ►                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  CRITIQUE FEED              Filter: [All Agents ▼] [All Phases ▼] [All ▼]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  12:04:32 │ EditorAgent → DirectorAgent                          Severity:│
│  ─────────┼──────────────────────────────────────────────────────── Info  │
│           │ "Pacing in Scene 3 exceeds genre prior by 1.2σ.                │
│           │  Suggest trimming B-roll between beats 7–8."                   │
│           │  📎 Attached: pacing_curve_s3.json                             │
│           │  [Accept] [Reject] [Discuss] [View Artifact]                   │
│           │                                                                │
│  12:03:58 │ AIQAConsistencyAgent → GeneratorAgent               Severity:│
│  ─────────┼──────────────────────────────────────────────────── Warning  │
│           │ "Frame 142–148: hand artifact detected (confidence 0.91).      │
│           │  Recommend re-roll with seed+1."                               │
│           │  📎 Attached: frame_142_annotated.png                          │
│           │  [Auto-Fix] [Manual Review] [Dismiss]                          │
│           │                                                                │
│  12:03:22 │ ComplianceAgent → ALL                               Severity:│
│  ─────────┼──────────────────────────────────────────────────── Critical │
│           │ "Voice clone consent for talent #3 expires in 48h.             │
│           │  Block delivery until renewal confirmed."                       │
│           │  [Resolve] [Escalate to Human] [Extend Deadline]               │
│           │                                                                │
│  12:02:45 │ JudgeAgent → ScreenwriterAgent + DirectorAgent      Severity:│
│  ─────────┼──────────────────────────────────────────────────────── Info  │
│           │ "Debate resolved: Act 2 midpoint placement at 52%              │
│           │  (DirectorAgent position) wins by rubric score 0.82 vs 0.71."  │
│           │  [View Debate Log] [View Rubric]                               │
│           │                                                                │
│  ── HUMAN INTERVENTION SLOT ────────────────────────────────────────────   │
│  │  💬 Type your critique or instruction to any agent...          [Send] │  │
│  │  @Agent: [autocomplete]  Priority: [Normal ▼]                         │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
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
│  ┌─── I/O ARTIFACTS ──────
…



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

Step 2: MULTI-AGENT EVALUATION (parallel, ~30 seconds)
  ┌──────────────────────────────────────────────────────────┐
  │ AIQAConsistencyAgent → frame quality, artifacts, hands   │
  │ CinematographerAgent → composition, framing, lighting    │
  │ ColoristAgent → color balance, grade quality, consistency │
  │ EditorAgent → pacing, cut timing, rhythm analysis        │
  │ RetentionOptimizerAgent → hook analysis, drop-off predict│
  │ SoundMixerAgent → loudness, balance, frequency analysis  │
  │ ComposerAgent → music-mood alignment, beat-sync          │
  │ NarrativeArcAgent → story structure, emotional curve     │
  │ AccessibilityAgent → captions present? contrast? AD?     │
  │ SocialStrategistAgent → platform fit, format, metadata   │
  │ BrandAgent → if brand kit exists, check alignment        │
  │ NoveltyAgent → cliché detection, originality score       │
  └──────────────────────────────────────────────────────────┘



## Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


## Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


## Provenance

- Master roster row va_id=9 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `C:\Project\va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.editor · va_id=9 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **EditorAgent** (`video.editor`, va_id=9, category `3-Edit`).

### Responsibility focus
Assemble cut; pacing; coverage selection

### Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: automated video editing, pacing models, color grading AI, EDL generation, music-cut sync
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI video editing, AI color grading, trailer AI tools
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: AI editing workflows, auto pacing, AI color grade pipelines

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

<!-- migration_capability_research · video.editor · v1 · 2026-07-13 -->

### `sources/generic/video.soundmixer.SPEC.md`

Omitted here; same document as `SPEC.md` above.

### `sources/MAPPING.md`

# Mapping — `video.soundmixer`

- VA/generic pack ID: `video.soundmixer`
- Previous common ID: `video.dialog_editor`
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
  "agent_id": "video.soundmixer",
  "previous_common_agent_id": "video.dialog_editor",
  "va_taxonomy_aligned": true,
  "generic_source": "generic-swarm-ops/business/video/agents/video.soundmixer",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "aligned_at": "2026-07-27T00:48:10.614228Z",
  "generic_source_depth": {
    "excerpts": true,
    "study": true,
    "adopted_at": "2026-07-27T01:30:28.864657+00:00",
    "upstream": "generic-swarm-ops/business/video/agents"
  },
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\video\\agents\\video.soundmixer",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```

### `sources/RETHINK_100_APPLIED.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.soundmixer",
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
  "production_activation_requested": false,
  "network_access": false
}
```

### `sources/SOURCE_CATALOG.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.soundmixer",
  "sources": [
    {
      "id": "src_1",
      "title": "CAS Awards",
      "description": "CAS Awards",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.soundmixer",
      "status": "planned_or_partial"
    },
    {
      "id": "src_2",
      "title": "Atmos specs",
      "description": "Atmos specs",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.soundmixer",
      "status": "planned_or_partial"
    },
    {
      "id": "src_3",
      "title": "broadcast loudness standards",
      "description": "broadcast loudness standards",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.soundmixer",
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
