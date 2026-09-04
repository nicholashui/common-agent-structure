# video.personalizationengineer — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/video.personalizationengineer/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "video.personalizationengineer",
  "status": "registered",
  "role": "PersonalizationEngineerAgent (VA Domain Pack)",
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
      "video.compliance",
      "video.analyst"
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
  "va_id": 50,
  "va_name": "PersonalizationEngineerAgent",
  "va_category": "8-AI",
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

# PersonalizationEngineerAgent

> Self-contained VA Domain Pack agent on host common-agent-swarm-ops.
> Pack agent ID matches pure VA/generic taxonomy: `video.personalizationengineer`.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 50 |
| **pack_id** | `video.personalizationengineer` |
| **upstream_name** | PersonalizationEngineerAgent |
| **category** | `8-AI` |
| **domain_id** | `video` |
| **previous_common_id** | `video.refine_coordinator` |
| **status** | `registered` |
| **maturity** | L0 / non-active |
| **taxonomy** | Pure VA Domain Pack (via generic pack agents) |
| **folder** | `business/video/agents/video.personalizationengineer/` |

## Responsibility

Variable templates (name/face/voice swap)

Host role binding: `PersonalizationEngineerAgent (VA Domain Pack)`. Design-time VA table content below is historical and non-binding for activation.

### Responsibility (from VA table)

Variable templates (name/face/voice swap)

### Knowledge distillation sources (historical)

Idomoo case studies; DMA campaigns; MarTech lit

### Self-quality criteria (historical)

Render-success ≥99.5%; spot-check pass; privacy-audit pass

### Surpass-human signal (historical)

Higher share-rate than top human-templated campaigns

### Critique bus (historical)

- **Accepts critique from:** ComplianceAgent (GDPR/CCPA), AnalystAgent

- **Comments on:** TemplateDesignerAgent (fragility)

### Tools design-time notes (historical, non-activating)

Idomoo/Pirsonal APIs; HeyGen personalization; GDPR consent-management platform

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

### Architecture pattern (historical)

ReAct (assemble template → render → validate → deliver)

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

- Prompt reference: `video.prompt.personalizationengineer.v1`
- Rubric reference: `video.rubric.personalizationengineer.v1`
- Critique edges: `{"inputs": ["video.critic"], "outputs": ["video.judge"]}`
- Max refinement: `3`
- VA table quality criteria retained under Provenance and Identity surface above.

## Runtime binding

Authoritative fail-closed host configuration:

```json
{
  "agent_id": "video.personalizationengineer",
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
  "prompt_reference": "video.prompt.personalizationengineer.v1",
  "role": "PersonalizationEngineerAgent (VA Domain Pack)",
  "rubric_reference": "video.rubric.personalizationengineer.v1",
  "schema_version": "1.0",
  "status": "registered",
  "va_id": 50,
  "va_name": "PersonalizationEngineerAgent",
  "va_category": "8-AI"
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

- Pack agent ID `video.personalizationengineer` is aligned to pure VA Domain Pack / generic pack taxonomy (Agent IDs ≈ VA tables).
- Previous common inventory ID `video.refine_coordinator` is historical mapping only.
- Upstream design body below is **historical and non-binding**; local `agent_spec.json` is authoritative.
- Full VA/generic SPEC depth retained for offline design fidelity (including category roster rows and common agent structure when present upstream).

### VA Domain Pack specification body (historical and non-binding)

```text
PersonalizationEngineerAgent

> **Self-contained agent definition** for host `upstream-generic-pack`. Body text is embedded from in-pack corpus and upstream-va-design when available. Do not require external repos to understand this agent.

Identity

| Field | Value |
|-------|-------|
| **va_id** | 50 |
| **pack_id** | `video.personalizationengineer` |
| **category** | `8-AI` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.personalizationengineer/` |

Category roster section (full, from agents.md)

_The following is the complete category section from the master roster (includes peers in the same craft category)._


8. AI-Era Specialist Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 46 | **PromptEngineerAgent / GeneratorOperator** | Crafts prompts; steers Sora/Veo/Runway/Kling | Karen X. Cheng/Trillo public sets; r/aivideo; Runway AIFF jury notes | Prompt→output CLIP-T; iteration count to acceptance; seed reproducibility | Target shot in ≤3 iterations vs human avg 10 | DirectorAgent, AIQAAgent | AIQAAgent (re-roll budget), ConsistencyAgent | Sora 2 API, Veo 3.1, Runway Gen-4/Aleph, Kling 3.0; seed/parameter registries | DSPy / OPRO prompt optimization (Yang 2023) |
| 47 | **AvatarDesignAgent** | Synthetic-presenter identity | Synthesia/HeyGen design docs; Hany Farid deepfake-detection; C2PA spec | Identity-hash consistency across shots; consent chain; C2PA signed | C2PA-verifiable + Partnership-on-AI full-pass at scale | ComplianceAgent (consent), DeepfakeDetectionAgent | VoiceCloneAgent (off-likeness), LipSyncAgent | HeyGen Avatar IV API; Synthesia API; C2PA signing library (c2patool); face-embedding models | Constitutional AI (consent + identity constitution) |
| 48 | **VoiceCloneAgent / LipSyncSpecialist** | Voice cloning + lip-sync | ElevenLabs safety docs; Wav2Lip/Sync.so; Baxter lip-sync refs | Voice MOS ≥4.2; phoneme-viseme error <40ms; consent verified | Wins blind MOS vs professional ADR | ComplianceAgent (consent), AnimatorAgent (lip-sync gold) | AvatarDesignAgent (face flicker), DubbingAgent | ElevenLabs v3 cloning API; Sync.so lip-sync; Wav2Lip; consent-doc verification | Self-Refine + MOS scoring model as judge |
| 49 | **AIQAConsistencyAgent** | Catches frame drift, hand/face artifacts, identity breaks | VBench; EvalCrafter; FVD literature; MPC/Weta QC checklists; deepfake models | Per-frame artifact score; identity-hash drift; hand/finger pass | Catches >95% of senior QC catches + 30% missed | DirectorAgent, VFXSupAgent | GeneratorAgent (re-roll), CompositorAgent | VBench evaluation suite; hand-detector models; face-ID embedding (ArcFace); frame-diff tools | Tool-use / ReAct (run detectors → flag → report) |
| 50 | **PersonalizationEngineerAgent** | Variable templates (name/face/voice swap) | Idomoo case studies; DMA campaigns; MarTech lit | Render-success ≥99.5%; spot-check pass; privacy-audit pass | Higher share-rate than top human-templated campaigns | ComplianceAgent (GDPR/CCPA), AnalystAgent | TemplateDesignerAgent (fragility) | Idomoo/Pirsonal APIs; HeyGen personalization; GDPR consent-management platform | ReAct (assemble template → render → validate → deliver) |
| 51 | **TrailerEditorAgent** | Hook-driven trailer cuts | Golden Trailer Awards; Woollen/AV Squad reels; trailer-music libs | Hook-rate at 3s; rising-action curve; music-sync precision | Wins Golden-Trailer-rubric blind comparison | DirectorAgent, MusicSupervisorAgent | EditorAgent (over-cut), ComposerAgent (mismatch) | DaVinci Resolve (MCP); trailer-music APIs (Musicbed/Artlist); retention-curve predictor | Self-Refine (retention-curve model as feedback) |
| 52 | **SportsAnalystAgent / TelestratorOp** | Tactical breakdowns + diagrams | MIT Sloan papers; ESPN Stats & Info; Goldsberry analytics | Play-call accuracy; on-screen clarity score | Beats ex-athlete on tactical-prediction | SMEAgent (sport), JournalistAgent | EditorAgent (missed-replay), MotionGraphicsAgent (chart clarity) | Sports data APIs (StatsBomb, NBA Stats); telestration overlay tools; After Effects MCP | ReAct (fetch play data → annotate → render overlay) |

---


Responsibility

Variable templates (name/face/voice swap)

Knowledge distillation sources

Idomoo case studies; DMA campaigns; MarTech lit

Self-quality criteria

Render-success ≥99.5%; spot-check pass; privacy-audit pass

Surpass-human signal

Higher share-rate than top human-templated campaigns

Critique bus

- **Accepts critique from:** ComplianceAgent (GDPR/CCPA), AnalystAgent

- **Comments on:** TemplateDesignerAgent (fragility)

Tools (design-time documentation)

Idomoo/Pirsonal APIs; HeyGen personalization; GDPR consent-management platform

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

Architecture pattern

ReAct (assemble template → render → validate → deliver)

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


| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 46 | PromptEngineerAgent | Crafts prompts; steers gen models | — |
| 47 | AvatarDesignAgent | Synthetic presenter identity | — |
| 48 | VoiceCloneAgent / LipSync | Voice cloning + lip-sync | — |
| 49 | AIQAConsistencyAgent | Frame drift, artifacts, identity breaks | — |
| 50 | PersonalizationEngineerAgent | Variable templates (name/face swap) | — |
| 51 | TrailerEditorAgent | Hook-driven trailer cuts | — |
| 52 | SportsAnalystAgent | Tactical breakdowns + diagrams | — |

| Capability | What It Provides | Used By | Specification |
|-----------|-----------------|---------|---------------|
| **Strategic Goal Achievement Framework** | 6-stage self-inquiry system for transforming vague goals into actionable plans | All planning agents (PlannerAgent, ProducerAgent, DirectorAgent) | [strategic_goal_achievement_agent_functional_specification.md](./strategic_goal_achievement_agent_functional_specification.md) |
| **Screenwriter Goal Achievement** | Practical demonstration of goal framework applied to creative writing | ScreenwriterAgent, ShowrunnerAgent, ComedyWriterAgent | [screenwriter_strategic_goal_achievement_agent_functional_specification.md](./screenwriter_strategic_goal_achievement_agent_functional_specification.md) |
| **Psychological Profiling** | 100 creator profiles with MBTI, motivations, fears, creative parameters | CastingAgent, TalentAgent, PersonalizationEngineerAgent, UGCCreatorAgent | [psychological_profile_agent_functional_specifications.md](./psychological_profile_agent_functional_specifications.md) |
| **Psychological Recommendation** | Psychology-based preference prediction (Big Five, emotional state) | AudienceSimAgent, PerformanceMarketerAgent, PersonalizationEngineerAgent | [psychological_recommendation_agent_functional_specification.md](./psychological_recommendation_agent_functional_specification.md) |
| **Complex Problem Solving** | WHAT/WHY/HOW/DO/REVIEW structured methodology | All diagnostic agents (FactCheckerAgent, SMEAgent, JudgeAgent, OptimizationAgent) | [complex_problem_solution_process_model.md](./complex_problem_solution_process_model.md) |
| **Common Agent Structure** | Shared architectural pattern for all agents | All 114 agents | [common-agent-structure.svg](./common-agent-structure.svg) + [common-agent-structure.html](./common-agent-structure.html) |

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


**Build:**
- **Psychological Profiling** (100 creator profiles: MBTI, motivations, fears, creative params) → feeds Casting/Talent/Personalization/UGC agents and Aesthetic-Agent *audience-cohort profiles*.
- **Psychological Recommendation** (Big Five / emotional-state preference prediction) → AudienceSim, PerformanceMarketer, Personalization.
- **PersonalizationEngineerAgent** templating (name/face/voice swap) with privacy/consent audit (GDPR/CCPA via ComplianceAgent).
- **Podcast Agent** audio-first workflow (preparation → execution → ending → follow-up), reusing VO/SoundMixer/Editor.



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

- Master roster row va_id=50 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `[historical-path]
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): upstream-va-design.


<!-- self_contained_spec · video.personalizationengineer · va_id=50 -->

Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **PersonalizationEngineerAgent** (`video.personalizationengineer`, va_id=50, category `8-AI`).

Responsibility focus
Variable templates (name/face/voice swap)

Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: prompt optimization DSPy/OPRO, digital humans/avatars, personalization recommender systems, video consistency models, deepfake detection
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: prompt engineering video, AI avatars production, personalized video AI, consistency AI
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: prompting for video models, avatar video production, personalized video at scale, AI consistency checks

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

<!-- migration_capability_research · video.personalizationengineer · v1 · 2026-07-13 -->

```


## Prompts

### `prompts/primary.md`

# Prompt — `video.prompt.personalizationengineer.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: ReAct, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **PersonalizationEngineerAgent (VA Domain Pack)** (`video.personalizationengineer`), a pack agent in the video domain swarm.

### Responsibility (owns)
Variable templates (name/face/voice swap)

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
ReAct (assemble template → render → validate → deliver)

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Idomoo case studies; DMA campaigns; MarTech lit

## Developer

### Tools (allowlist intent)
Design tool surface: Idomoo/Pirsonal APIs; HeyGen personalization; GDPR consent-management platform
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: ComplianceAgent (GDPR/CCPA), AnalystAgent
- May comment on: TemplateDesignerAgent (fragility)
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Render-success ≥99.5%; spot-check pass; privacy-audit pass

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.personalizationengineer",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **PersonalizationEngineerAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.personalizationengineer",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.personalizationengineer`.
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

### `prompts/video.prompt.personalizationengineer.v1.md`

# Prompt — `video.prompt.personalizationengineer.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: ReAct, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **PersonalizationEngineerAgent (VA Domain Pack)** (`video.personalizationengineer`), a pack agent in the video domain swarm.

### Responsibility (owns)
Variable templates (name/face/voice swap)

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
ReAct (assemble template → render → validate → deliver)

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Idomoo case studies; DMA campaigns; MarTech lit

## Developer

### Tools (allowlist intent)
Design tool surface: Idomoo/Pirsonal APIs; HeyGen personalization; GDPR consent-management platform
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: ComplianceAgent (GDPR/CCPA), AnalystAgent
- May comment on: TemplateDesignerAgent (fragility)
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Render-success ≥99.5%; spot-check pass; privacy-audit pass

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.personalizationengineer",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **PersonalizationEngineerAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.personalizationengineer",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.personalizationengineer`.
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

Source rubric `video.rubric.personalizationengineer.v1.json` (baseline_safe; not a production pass).

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.personalizationengineer.v1",
  "agent_id": "video.personalizationengineer",
  "title": "L2 craft rubric for PersonalizationEngineerAgent",
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
          "name": "Render-success ≥99.5%",
          "description": "Render-success ≥99.5%",
          "weight": 0.3333,
          "threshold_hint": "≥99.5%",
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "spot-check pass",
          "description": "spot-check pass",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d3",
          "name": "privacy-audit pass",
          "description": "privacy-audit pass",
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
      "surpass_signal_design": "Higher share-rate than top human-templated campaigns",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Render-success ≥99.5%; spot-check pass; privacy-audit pass",
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

### `rubrics/video.rubric.personalizationengineer.v1.json`

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.personalizationengineer.v1",
  "agent_id": "video.personalizationengineer",
  "title": "L2 craft rubric for PersonalizationEngineerAgent",
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
          "name": "Render-success ≥99.5%",
          "description": "Render-success ≥99.5%",
          "weight": 0.3333,
          "threshold_hint": "≥99.5%",
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "spot-check pass",
          "description": "spot-check pass",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d3",
          "name": "privacy-audit pass",
          "description": "privacy-audit pass",
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
      "surpass_signal_design": "Higher share-rate than top human-templated campaigns",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Render-success ≥99.5%; spot-check pass; privacy-audit pass",
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

# Source acquisition runbook — `video.personalizationengineer`

## Purpose
Obtain or refresh knowledge distillation sources listed in `SOURCE_CATALOG.json`.

## Rules
1. **No secrets in git.** API keys only via environment / secret manager.
2. Prefer **licensed / consented / public domain** material.
3. If license unknown: store only short fair-use design excerpts under `excerpts/` and mark `license_class=unknown_review_required`.
4. Update `PROVENANCE.json` with URL, retrieved_at, hash, and license note.
5. Re-run offline golden eval after material changes.

## Design sources (from agents.md)
Idomoo case studies; DMA campaigns; MarTech lit

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
  "agent_id": "video.personalizationengineer",
  "plan_id": "video.personalizationengineer.distill.v1",
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
  "owner": "video.personalizationengineer",
  "cadence": "quarterly",
  "promotion_criteria": [
    "source license approved or fixture-only",
    "excerpt hash recorded in PROVENANCE",
    "golden eval still passes L1"
  ],
  "memory_namespace": "pack.video.video.personalizationengineer",
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

### `sources/generic/video.critic.SPEC.md`

# CriticAgent

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 95 |
| **pack_id** | `video.critic` |
| **category** | `10-Sup` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.critic/` |

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

Simulates reviewer, press, or jury interpretation

## Knowledge distillation sources

Criticism corpora, festival-jury commentary, review archives

## Self-quality criteria

Interpretive depth, consistency, reviewer-mode diversity

## Surpass-human signal

Provides broader qualitative coverage than ad hoc internal taste review

## Critique bus

- **Accepts critique from:** DirectorAgent, AudienceSimAgent, FestivalStrategistAgent, JudgeAgent

- **Comments on:** Auteur read, tone mismatch, festival/press vulnerability

## Tools (design-time documentation)

Review corpora, jury rubrics, qualitative scoring tools

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

Multi-agent debate as critic panel

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


### Document: `study/aesthetics_agent_functional_specification.md`

_Embedded from `corpus/study/aesthetics_agent_functional_specification.md`. Also stored at `sources/study/aesthetics_agent_functional_specification.md` under this agent folder._


**Comprehensive Functional Specification: Aesthetics Agent — Computational "Artiste Sense" Critic & Alignment Service for the VA-Agent-Swarm**

**Document Version:** 1.0 (Final – Complete & Exhaustive)
**Date:** May 29, 2026
**Authors:** Grok (xAI) + Collaborative Iteration with User Nicholas (nicholas_hui)
**Target Audience:** Senior AI Engineering / Coding Agents (for immediate implementation)
**Purpose:** This is the **definitive, production-grade specification** for building the **Aesthetics Agent** — a stateful, multimodal evaluation-and-alignment service that operationalizes a simulated **"artiste sense"** (artistic/aesthetic intuition) for the entire VA-Agent-Swarm. It is the deep rethink of [`aesthetics_agents.md`](./aesthetics_agents.md): where that document is a *survey of methods*, this is a *buildable agent contract*. It reframes "teach AI artistic sense" from a single image scorer into a **shared aesthetic nervous system** — a critic that every generative agent consults, a reward signal that every fine-tuning loop trusts, and a personalization engine that carries a director's, brand's, or artist's taste across the whole pipeline.

---

### 1. Executive Summary

The **Aesthetics Agent** is the swarm's computational embodiment of "artiste sense." It does not *replace* human taste — it **amplifies, encodes, and propagates** it at superhuman speed across 114 agents.

It serves three distinct, composable functions:

1. **The Critic (Perceive).** A multimodal, multi-head evaluator that scores any visual artifact — single frame, image, or full video clip — against a decomposed aesthetic rubric (composition, color harmony, lighting, depth, emotional resonance, technical quality, style fidelity, novelty). This is the swarm's shared "eye."
2. **The Aligner (Refine).** A preference-and-reward service that turns the Critic's judgments into actionable feedback and training signal — driving self-refinement loops, preference optimization (DPO/RLHF/RLAIF), and prompt steering for `PromptEngineerAgent`, `CinematographerAgent`, `ColoristAgent`, and peers.
3. **The Taste-Keeper (Personalize).** A profile store that captures *whose* aesthetic governs a project — a director's lookbook, a brand's guidelines, an artist's portfolio, an audience cohort's preferences — and conditions all scoring and alignment on that profile.

**Why this is a "deep rethink" and not a wrapper:**

| The naive guide says... | The Aesthetics Agent does... |
|---|---|
| "Train an aesthetic scorer (e.g., NIMA, LAION)." | Treats a single scalar score as *insufficient and dangerous*. Decomposes aesthetics into auditable sub-attributes + a temporal track for video, with calibrated uncertainty. |
| "Use the critic as a reward to fine-tune the generator." | Wraps every reward use in **anti-reward-hacking** guardrails (reward variance monitoring, ensemble disagreement, OOD detection, KL anchoring). |
| "Personalize on one artist's ratings." | Makes taste a **first-class, versioned, consent-governed profile** that flows through the swarm's handoff contract and critique bus. |
| Operates on still images. | Is **video-native first**: temporal coherence, motion aesthetics, cut rhythm, and per-shot-vs-sequence scoring. |
| Aesthetic sense = beauty prediction. | Aesthetic sense = beauty **+ intent fidelity + emotional target + brand/style fit + novelty**, gated so high scores never come from generic "pretty slop." |

The result is a single agent that other agents *cannot do their job without*: it is referenced by `agents.md` entries #6, #10, #14, #15, #16, #39, #46, #49 and others as "aesthetic regressor / CLIP-based aesthetic scoring," and this document is its authoritative definition.

---

### 2. Background: From "Artiste Sense" to Computational Aesthetics

The source document [`aesthetics_agents.md`](./aesthetics_agents.md) defines **"artiste sense"** as the intuitive, perceptual, and expressive sensitivity artists develop — an "eye" for composition, color harmony, rhythm, proportion, light/shadow, depth, and emotional resonance; a structural (3D) way of seeing; a psychological drive to express; and a grounded, iterative creative practice.

Its central thesis, which this spec adopts wholesale:

> AI cannot possess *genuine* lived artistic sense (no consciousness, no emotion), but it can develop a **sophisticated simulated version** through (a) data-driven evaluators trained on human aesthetic judgments, (b) preference-alignment feedback loops, and (c) computational-creativity extensions. The strongest results come from **human–AI symbiosis**, not autonomous AI artists.

This specification accepts that framing as ground truth and answers the only question the survey left open: **what is the precise, implementable agent contract that delivers it inside a 114-agent video production system?**

---

### 3. The Deep Rethink — Five Reframings

The act of "deeply rethinking" the guide produced five architectural commitments. Each is a deliberate departure from the naive "train a scorer" recipe.

**3.1 Aesthetics is a vector, not a scalar.**
A single 1–10 score is unaccountable and trivially reward-hacked. The Critic emits a **decomposed AestheticVector** — independent heads for composition, color, light, depth, subject treatment, technical quality, emotional resonance, style fidelity, and novelty — each with a calibrated confidence. The scalar is a *gated aggregation*, never the source of truth.

**3.2 Aesthetics is temporal.**
This is a video swarm. A montage of individually beautiful frames can be aesthetically incoherent. The Critic scores both **per-frame** and **per-sequence**: motion smoothness, temporal color/exposure stability, cut rhythm vs. genre prior, and "does the clip read as one authored gesture."

**3.3 Aesthetics is whose.**
Following the LAION-Aesthetics audit critique that a "one-size-fits-all" beauty model encodes a narrow, unexamined taste ([arXiv:2601.09896](https://arxiv.org/html/2601.09896v1)), the agent refuses to pretend there is one universal beauty. Every score is conditioned on an explicit **AestheticProfile** (director / brand / artist / audience cohort / "neutral baseline"). Personalization is the default, not an add-on. Recent work shows LLM-interview-elicited personalized aesthetic models can exceed generic ones at predicting an individual's judgments ([arXiv:2605.14761](https://arxiv.org/html/2605.14761v1)).

**3.4 Aesthetics must not be hackable.**
The moment the Critic becomes a reward, generators learn to exploit it (high-frequency texture spam, saturation blowouts, "AI-glossy" sheen). The Aligner therefore ships with first-class **anti-reward-hacking** machinery — ensemble disagreement, reward-variance monitoring (large/diverse reward models retain high variance and resist collapse, per [arXiv:2509.08826](https://arxiv.org/html/2509.08826v1)), KL anchoring to a reference model, OOD artifact detectors, and inference-time mitigation ([arXiv:2510.01549](https://arxiv.org/abs/2510.01549)). Rich, rationale-bearing preferences are favored over opaque scalars ([arXiv:2503.11720](https://arxiv.org/html/2503.11720)).

**3.5 Aesthetics is gated by intent.**
Beauty divorced from the brief is noise. The aggregate quality is multiplied by **intent fidelity** (does it match the shot intent / prompt / brand?) and **emotional-target match** (does it land the intended valence/arousal?). A gorgeous image that ignores the director's intent scores low. This mirrors the value-gated selection in the [General Creative Agent](./general_creative_agent_functional_specification.md) (SSOR).

---

### 4. Formal Aesthetic Model

Let an artifact \( x \) (image or video clip) be evaluated under an aesthetic profile \( p \), an intent/brief \( b \), and an emotional target \( e \).

The Critic produces a **decomposed aesthetic vector**:

\[
\mathbf{A}(x \mid p) = \bigl[\, a_1, a_2, \dots, a_k \,\bigr], \quad a_i \in [0,1], \; \text{with confidence } \sigma_i
\]

over \( k \) sub-attributes (the **Aesthetic Dimensions**, §6). The **gated aesthetic quality** is:

\[
\operatorname{AQ}(x \mid p,b,e) \;=\; \underbrace{G\!\left(\mathbf{A}(x\mid p), \mathbf{w}_p\right)}_{\text{profiled aggregate}} \;\cdot\; \underbrace{I(x,b)}_{\text{intent fidelity}} \;\cdot\; \underbrace{E(x,e)}_{\text{emotion match}} \;\cdot\; \underbrace{\big(1 - H(x)\big)}_{\text{anti-hack penalty}}
\]

Where:
- \( G(\cdot, \mathbf{w}_p) \): profile-weighted aggregation of the attribute vector (weights \( \mathbf{w}_p \) come from the active `AestheticProfile`; a brand may weight color/brand-fit heavily, a horror DoP may weight light/contrast).
- \( I(x,b) \in [0,1] \): intent fidelity (e.g., CLIP-T / VLM grounding of artifact against shot-intent text or reference; target ≥ 0.32 per `DirectorAgent` rubric in `agents.md`).
- \( E(x,e) \in [0,1] \): emotional-target match (valence/arousal regression vs. target, shared with `ComposerAgent` emotional-arc validator).
- \( H(x) \in [0,1] \): hack/artifact likelihood (OOD score, ensemble disagreement, artifact detector) — high \( H \) collapses the score regardless of surface prettiness.

For video, AQ is computed per-frame **and** at sequence level, then combined:

\[
\operatorname{AQ}_{\text{clip}} = \alpha \cdot \operatorname{mean}_t \operatorname{AQ}(x_t) \;+\; \beta \cdot \operatorname{AQ}_{\text{temporal}}(x_{1:T}) \;-\; \gamma \cdot \operatorname{Var}_t\!\big[\text{exposure, color, identity}\big]
\]

penalizing temporal instability (flicker, color drift, identity break — overlaps with `AIQAConsistencyAgent` #49).

**Hard principles (encoded in code):**
- **No naked scalar.** Any consumer requesting only `AQ` also receives \( \mathbf{A} \), \( H \), and the top failing dimension.
- **Uncertainty travels.** Every score ships with confidence; low-confidence scores must escalate to HiTL or a second model, never silently pass.
- **Profile-or-refuse.** If no profile is supplied, the agent uses an explicitly labeled `neutral_baseline_v{n}` profile and flags that the result is taste-agnostic.

---

### 5. Architecture

The Aesthetics Agent is a three-subsystem service sharing one profile store and one model registry.

```
                         ┌───────────────────────────────────────────────┐
                         │              AESTHETICS AGENT                   │
                         │                                                 │
  Artifact (img/video) ─▶│  ┌──────────────┐   ┌──────────────┐           │
  + Profile + Intent     │  │  THE CRITIC  │   │ THE ALIGNER  │           │
  + Emotion target       │  │  (Perceive)  │──▶│  (Refine)    │──┐        │
                         │  │ multi-head   │   │ reward +     │  │        │
                         │  │ evaluator    │   │ preference + │  │        │
                         │  └──────┬───────┘   │ critique gen │  │        │
                         │         │           └──────────────┘  │        │
                         │         ▼                              ▼        │
                         │  ┌──────────────┐          ┌────────────────┐  │
                         │  │ ANTI-HACK    │          │ THE TASTE-KEEPER│  │
                         │  │ guardrails   │◀────────▶│ (Personalize)   │  │
                         │  │ (ensemble,   │          │ AestheticProfile│  │
                         │  │ OOD, KL)     │          │ store (versioned)│ │
                         │  └──────────────┘          └────────────────┘  │
                         └───────────────────────────────────────────────┘
                                   │                          │
                          AestheticVerdict (JSON)     Profile updates
                                   ▼                          ▼
                          CRITIQUE BUS  ──────▶  consuming agents (#6,#10,#15,#39,#46,#49…)
```

**5.1 The Critic (Perceive).** Ensemble of complementary backbones:
- A fast **regression head** on a vision backbone (SigLIP / CLIP-ViT) — Aesthetic-Predictor-V2.5-style MLP for cheap first-pass screening at scale.
- A **VLM critic** (Grok-4.x vision, Gemini 2.5 Pro, GPT-4o-vision) producing fine-grained, attribute-level natural-language critique + scores — the "explainable eye."
- Specialized detectors: artifact/hand/face-distortion detectors, ΔE color drift, exposure histogram/zone analysis, rule-of-thirds & leading-lines geometry, FID/FVD against style reference, temporal smoothness (optical flow), VBench-style video metrics.

**5.2 The Aligner (Refine).** Converts verdicts into action:
- **Self-refine feedback**: a prioritized, machine-readable critique ("scene 3 underexposed in zone IV; subject collides with right edge; color drifts +6 ΔE across cut").
- **Reward signal**: scalar/vector reward for RLHF / RLAIF / DPO / ReFL-style diffusion fine-tuning, always emitted with variance + ensemble-agreement metadata.
- **Preference pairs**: for DPO-style training, with rationale (rich preferences) not just A≻B.
- **Prompt-steer hints**: concrete prompt deltas handed to `PromptEngineerAgent` (#46) to reach target in ≤3 iterations.

**5.3 The Taste-Keeper (Personalize).** Versioned, consent-governed `AestheticProfile` store (see §10), elicited via portfolio ingestion, pairwise preference collection, and LLM-interview elicitation ([arXiv:2605.14761](https://arxiv.org/html/2605.14761v1)).

**5.4 Anti-Hack Guardrails.** Cross-cutting safety layer wrapping every reward emission (see §11).

---

### 6. Aesthetic Dimensions (the Decomposed Rubric)

The Critic emits a score + confidence for each dimension. Profiles re-weight them; they are *never* collapsed before being logged.

| # | Dimension | What it measures | Primary signal |
|---|-----------|------------------|----------------|
| D1 | **Composition** | Balance, rule-of-thirds, leading lines, negative space, framing, staging clarity | Geometry detector + VLM |
| D2 | **Color Harmony** | Palette coherence, contrast, temperature consistency, mood vector | Color histogram, ΔE, palette extraction |
| D3 | **Light & Shadow** | Exposure zones, key/fill ratio, direction, dynamic range, mood | Histogram/zone analysis, VLM |
| D4 | **Depth & Form** | 3D readability, layering, focal depth, structural "seeing" (per artiste-sense) | Depth estimation + VLM |
| D5 | **Subject Treatment** | Subject prominence, gaze, gesture, silhouette readability | Saliency + pose/landmark |
| D6 | **Technical Quality** | Sharpness, noise, banding, artifacts, resolution adequacy | Detectors + IQA model |
| D7 | **Emotional Resonance** | Evoked valence/arousal vs. target | Affect regressor (shared w/ ComposerAgent) |
| D8 | **Style Fidelity** | Adherence to style bible / lookbook / brand | CLIP/embedding distance to reference set |
| D9 | **Novelty / Distinctiveness** | Originality vs. "generic AI slop"; inverted-U (not maximal) | Embedding rarity vs. corpus |
| D10 | **Temporal Aesthetics** *(video)* | Motion smoothness, cut rhythm, temporal stability, "one authored gesture" | Optical flow, VBench-style, beat-sync |

**Novelty note (D9):** Following the SSOR inverted-U principle from the GCA spec, novelty is rewarded in a *moderate* band — too low = cliché/derivative; too high = incoherent. This is what prevents the agent from rewarding bland, statistically-average "pretty" output.

---

### 7. Functional Requirements

**7.1 Input (JSON).**
```json
{
  "artifact_ref": "asset_id_or_uri",
  "media_type": "image | video_clip | frame_sequence",
  "profile_id": "director_lynchian_v3 | brand_acme_v2 | neutral_baseline_v4",
  "intent": { "shot_intent_text": "...", "reference_refs": ["..."], "genre_prior": "noir" },
  "emotional_target": { "valence": -0.4, "arousal": 0.7 },
  "mode": "screen | score | align | compare | refine",
  "constraints": { "aspect_ratio": "2.39:1", "color_space": "ACEScct", "deliverable": "HDR" },
  "budget": { "max_latency_ms": 800, "tier": "fast | deep" }
}
```

**7.2 Output — `AestheticVerdict` (JSON + Markdown).**
```json
{
  "artifact_ref": "asset_id_v2",
  "profile_id": "director_lynchian_v3",
  "aesthetic_vector": { "composition": 0.81, "color_harmony": 0.74, "light": 0.62,
                        "depth": 0.70, "subject": 0.88, "technical": 0.91,
                        "emotion": 0.66, "style_fidelity": 0.79, "novelty": 0.55,
                        "temporal": 0.83 },
  "confidence": { "composition": 0.9, "light": 0.6, "...": "..." },
  "intent_fidelity": 0.79,
  "emotion_match": 0.71,
  "hack_likelihood": 0.04,
  "aesthetic_quality": 0.73,
  "top_failing_dimensions": ["light", "novelty"],
  "actionable_critique": [
    "Underexposed in zone IV; lift key +1/3 stop on subject left.",
    "Palette is conventional for genre; consider one strategic outlier hue."
  ],
  "prompt_steer_hints": ["add 'low-key chiaroscuro, single practical source'"],
  "uncertainty_flag": false,
  "escalate_to_hitl": false,
  "provenance": { "models": ["aesV2.5","grok-vision-4.x"], "ensemble_agreement": 0.86 }
}
```

**7.3 Modes.**
- `screen` — fast scalar gate for high-volume candidate culling (regression head only).
- `score` — full decomposed vector + verdict.
- `align` — emit reward/preference signal for a training/refinement loop.
- `compare` — pairwise/listwise ranking of N candidates (for "choose the best take").
- `refine` — generate → score → critique → suggest, iterated (mimics the artist's iterative loop).

**7.4 Statefulness.** Per-project memory of accepted/rejected artifacts ratchets the profile and feeds Reflexion-style episodic memory (consistent with swarm principle "Continuous Self-Improvement").

**7.5 Non-functional.** Fast-tier screening ≤ 800 ms/artifact; deep-tier ≤ 8 s; horizontal GPU autoscale; deterministic given fixed profile + model versions (reproducibility for audits).

---

### 8. Integration with the VA-Agent-Swarm

This agent is **cross-cutting infrastructure**, registered alongside the Research Agent, GCA, and Optimization Agent in [`SYSTEM_REFERENCE.md`](./SYSTEM_REFERENCE.md) §4.

**8.1 Consumers (who calls it and why).**

| Agent (from `agents.md`) | Use of Aesthetics Agent |
|---|---|
| #6 CinematographerAgent (DoP) | Replaces ad-hoc "CLIP-based aesthetic scoring" — composition/light/color self-refine rubric |
| #10 ColoristAgent | ΔE drift, mood-vector match, palette coherence scoring |
| #14 StoryboardAgent / #15 ConceptArtistAgent / #16 ProductionDesignAgent | Style-bible adherence + composition scoring |
| #39 FoodStylistAgent / #40 TravelCineAgent / #45 RealEstatePhotoAgent | The shared "aesthetic regressor" these specs reference |
| #46 PromptEngineerAgent | `refine` mode + `prompt_steer_hints` to hit target in ≤3 iterations |
| #49 AIQAConsistencyAgent | Temporal stability / artifact (`hack_likelihood`) cross-check |
| #1 DirectorAgent / #56 JudgeAgent | Tie-break and blind-preference adjudication on candidate takes |
| Delivery & Marketing (#27, #28, #31) | Thumbnail/hook aesthetic scoring for predicted engagement |

**8.2 Critique Bus.** Verdicts are published on the swarm's structured critique bus (`SYSTEM_REFERENCE.md` §7.1) with `critique_type: "aesthetic_feedback"`, `severity`, `rubric_score`, and `artifact_ref`, so any agent can react asynchronously.

**8.3 Handoff Contract.** The `AestheticVerdict` is attached to the artifact's `qc_status` field in the **Shared Artifact Handoff Contract** (`SYSTEM_REFERENCE.md` §7), making aesthetic state travel with provenance through every phase.

**8.4 Relationship to neighbors.**
- **vs. GCA (creativity):** GCA *generates* novel-yet-useful candidates; Aesthetics Agent *judges and refines* them. GCA's novelty score (D9) is supplied by this agent. They form a generate↔evaluate loop.
- **vs. AIQAConsistencyAgent (#49):** AIQA catches *errors* (drift, broken hands, identity breaks); Aesthetics Agent judges *taste*. `hack_likelihood` is the shared boundary — co-trained, deduplicated.
- **vs. Psychological Recommendation / AudienceSim:** those predict *audience* preference; Aesthetics Agent encodes *authorial/brand* taste. A profile can be an audience-cohort profile, bridging the two.

---

### 9. The Three Operating Loops

**9.1 Critic Loop (evaluate).** `artifact → ensemble score → decompose → gate by intent/emotion → anti-hack check → AestheticVerdict`.

**9.2 Alignment Loop (teach the generator).** Mirrors the source guide's pipeline, hardened:
1. Generate N candidates (base model).
2. `compare` mode ranks them; `score` mode decomposes.
3. Human raters spot-check a sampled subset (symbiosis, not full autonomy).
4. Build **rich preference pairs** (with rationale) → DPO / RLHF / RLAIF / ReFL update.
5. Monitor reward variance & ensemble agreement; if variance collapses → suspect hacking, freeze, escalate.
6. Repeat; generator internalizes the taste and "instinctively" picks stronger outputs.

**9.3 Personalization Loop (capture whose taste).**
1. Ingest portfolio / lookbook / brand guide → seed embedding profile.
2. Collect pairwise preferences and/or run **LLM-interview elicitation** to surface latent criteria.
3. Fit profile weights \( \mathbf{w}_p \); validate against held-out judgments.
4. Version, sign, and store; expose `profile_id` to the swarm.

---

### 10. Personalization: the `AestheticProfile`

A first-class, versioned, consent-governed object.

```json
{
  "profile_id": "director_lynchian_v3",
  "owner": "consenting_entity_id",
  "consent": { "scope": "project_x", "expires": "2027-01-01", "c2pa_signed": true },
  "weights": { "light": 0.22, "color_harmony": 0.18, "novelty": 0.15, "...": "..." },
  "exemplars": ["asset_uri_1", "..."],
  "anti_exemplars": ["asset_uri_9", "..."],
  "elicited_criteria": ["prefers low-key contrast", "avoids saturated reds", "..."],
  "embedding_centroid": "vec://...",
  "version": 3,
  "lineage": ["v1","v2","v3"]
}
```

Profile types: **Director**, **Brand**, **Artist**, **Audience-Cohort** (links to [Psychological Recommendation](./psychological_recommendation_agent_functional_specification.md)), **Genre-prior**, **Neutral-baseline**. Profiles are composable (e.g., `brand_acme ⊕ genre_noir`) with documented precedence.

**Governance:** Personalizing on a named human's taste/portfolio requires consent recorded in the profile and cleared by `ComplianceAgent` (#37) — same rigor as voice/likeness cloning.

---

### 11. Reward Hacking, Failure Modes & Defenses

The single greatest risk: when the Critic becomes a reward, generators learn to *fool the eye*, not *please it*.

| Failure mode | Symptom | Defense |
|---|---|---|
| **Texture/detail spam** | High score, busy high-frequency noise | Artifact detector; frequency-domain sanity check; human spot-check |
| **Saturation/contrast blowout** | "AI-glossy" oversaturated look | ΔE & gamut bounds; per-dimension caps; brand profile constraints |
| **Mode collapse** | All outputs converge to one "safe" look | Reward-variance monitoring; large/diverse reward ensembles retain variance ([arXiv:2509.08826](https://arxiv.org/html/2509.08826v1)) |
| **Off-distribution exploitation** | Score high on inputs unlike training data | OOD detector → force `escalate_to_hitl`, never auto-pass |
| **Intent drift** | Beautiful but ignores brief | Intent-fidelity gate \( I(x,b) \) multiplies AQ |
| **Opaque-scalar overfit** | Generator games one number | Rich, rationale-bearing preferences ([arXiv:2503.11720](https://arxiv.org/html/2503.11720)); decomposed vector never collapsed |
| **Taste monoculture / bias** | One narrow aesthetic encoded as "universal" | Mandatory explicit profiles; bias audit per LAION critique ([arXiv:2601.09896](https://arxiv.org/html/2601.09896v1)) |

**Core mechanisms:** (1) **Ensemble disagreement** — regression head, VLM critic, and detectors must agree; high disagreement raises \( H(x) \) and triggers HiTL. (2) **KL anchoring** to a reference generator during alignment to prevent runaway exploitation. (3) **Inference-time mitigation** for alignment without full fine-tuning ([arXiv:2510.01549](https://arxiv.org/abs/2510.01549)). (4) **Held-out human eval** as the non-negotiable ground truth — the agent's correlation with human raters is itself continuously monitored and is a release gate.

---

### 12. Technical Architecture & Implementation Guidelines

- **Core classes:** `AestheticCritic`, `AttributeHead[]`, `EnsembleScorer`, `IntentGate`, `EmotionGate`, `AntiHackGuard`, `Aligner`, `PreferenceBuilder`, `TasteKeeper`, `AestheticProfile`, `AestheticsAgent` (facade).
- **Models:** SigLIP/CLIP-ViT backbone + MLP regression head (fast tier, Aesthetic-Predictor-V2.5 lineage); VLM critic via swarm LLM providers (Grok-4.x vision / Gemini 2.5 Pro / GPT-4o); detector zoo (artifact, ΔE, depth, flow, FID/FVD, VBench-style).
- **Frameworks:** PyTorch + `diffusers` (for ReFL/DPO hooks); LangGraph node for orchestration; FastAPI service; Redis Streams for critique-bus publication.
- **Stores:** vector DB (Chroma/Pinecone) for exemplars & embeddings; profile DB (versioned, signed); episodic memory for refine-loop learning.
- **Provenance:** every verdict logs model versions, ensemble agreement, profile version → C2PA-aligned audit trail.
- **Deliverables:** repo skeleton, `AestheticVerdict` schema, profile schema, example notebooks (image scoring, video scoring, DPO alignment loop, profile elicitation), integration adapters for #6/#10/#46/#49.

---

### 13. Evaluation & Success Criteria

| Criterion | Target |
|---|---|
| Correlation with human aesthetic ratings (held-out) | Spearman ρ ≥ 0.75 on benchmark; ≥ 0.85 on personalized profile |
| Personalized > generic | Profiled model beats `neutral_baseline` at predicting owner's pairwise choices (per [arXiv:2605.14761](https://arxiv.org/html/2605.14761v1)) |
| Blind preference (downstream) | Outputs aligned via this agent win ≥ 55% blind pairwise vs. unaligned (Arena-style) |
| Reward-hacking resistance | Reward variance maintained; mode-collapse rate below threshold over a fine-tuning run |
| Anti-hack recall | ≥ 95% of human-flagged "fooled-the-eye" cases caught by `hack_likelihood` |
| Latency | Fast tier ≤ 800 ms; deep tier ≤ 8 s |
| Calibration | Confidence well-calibrated (ECE below threshold); low-confidence reliably escalates |
| Traceability | 100% of verdicts carry decomposed vector + provenance |

---

### 14. Limitations & Future Directions

- **No genuine lived aesthetic.** The agent's "sense" is statistical and derivative; it has no spontaneity or personal impulse. It is an *amplifier* of human taste — best used in symbiosis, with HiTL on novel or low-confidence judgments.
- **Taste is contested.** Even with explicit profiles, the corpus and rater pool carry bias; the agent surfaces *whose* taste it encodes rather than claiming universality.
- **Reward hacking is an arms race.** Defenses reduce, not eliminate, exploitation; held-out human eval remains the ground truth and release gate.
- **Future:** larger multimodal critics; brain-activity / biosignal proxies for emotional resonance; embodied/3D structural "seeing"; tighter artist co-training loops; cross-modal aesthetics (image↔music↔motion) shared with `ComposerAgent` and `ChoreographyAgent`.

---

### 15. References (Curated, 2024–2026)

Foundational & survey (from [`aesthetics_agents.md`](./aesthetics_agents.md)):
- NIMA — Neural Image Assessment (CNN aesthetic-distribution prediction).
- LAION-Aesthetics / CLIP+MLP improved aesthetic predictor; Aesthetic Predictor V2.5 (SigLIP-based).
- Multi-task / unified aesthetic models (UniQA, HumanAesExpert lineage); VBench (video aesthetic/quality benchmark).
- Aesthetic post-training of diffusion models; RLHF for diffusion (DDPO, ReFL, DPOK, RewardDance).

Current grounding (web-verified May 2026; *content rephrased for licensing compliance*):
- Personalized aesthetics via LLM interviews + semantic features — [arXiv:2605.14761](https://arxiv.org/html/2605.14761v1).
- Audit/ethnography of the LAION-Aesthetics predictor ("whose taste") — [arXiv:2601.09896](https://arxiv.org/html/2601.09896v1).
- Reward Scaling in Visual Generation (large RMs resist reward hacking via retained variance) — [arXiv:2509.08826](https://arxiv.org/html/2509.08826v1).
- Mitigating reward hacking in inference-time alignment of T2I diffusion — [arXiv:2510.01549](https://arxiv.org/abs/2510.01549).
- Rich Preference Optimization for diffusion fine-tuning (rationale-bearing preferences) — [arXiv:2503.11720](https://arxiv.org/html/2503.11720).
- Rethinking DPO in diffusion models — [arXiv:2505.18736](https://arxiv.org/abs/2505.18736).
- Alignment & safety of diffusion via RL + reward modeling — [arXiv:2505.17352](https://arxiv.org/abs/2505.17352).

Intra-system references:
- [`aesthetics_agents.md`](./aesthetics_agents.md) — source survey of artiste sense.
- [`general_creative_agent_functional_specification.md`](./general_creative_agent_functional_specification.md) — SSOR creativity (generate side of the loop; novelty inverted-U).
- [`agents.md`](./agents.md) — consuming agents (#6, #10, #14–16, #39, #46, #49).
- [`SYSTEM_REFERENCE.md`](./SYSTEM_REFERENCE.md) — critique bus (§7.1), handoff contract (§7), cross-cutting registration (§4).
- [`psychological_recommendation_agent_functional_specification.md`](./psychological_recommendation_agent_functional_specification.md) — audience-cohort profiles.

---

**This specification is complete, self-contained, and ready for immediate coding.** It transforms the "artiste sense" survey into a buildable, swarm-integrated agent: a decomposed multimodal Critic, a hack-resistant Aligner, and a consent-governed Taste-Keeper — the shared aesthetic nervous system of the VA-Agent-Swarm.

Implement exactly as written. The resulting Aesthetics Agent will give all 114 agents a single, trustworthy, personalizable "eye."

**End of Specification**
*Save as `aesthetics_agent_functional_specification.md`.*



## Additional corpus / va passages naming this agent


### From `corpus/study/SYSTEM_REFERENCE.md` Copy: `sources/excerpts/SYSTEM_REFERENCE.md`.


| Principle | Description | Reference |
|-----------|-------------|-----------|
| **Agentic Graph** | Agents as DAG nodes with handoffs and review gates | [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) §1 |
| **Self-Refine + Critique** | Every agent drafts → self-critiques → revises against rubric | Madaan et al., 2023 |
| **Shared Artifact Contract** | Machine-readable manifests flow between all phases | [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) §1.3 |
| **Human-in-the-Loop Gates** | Critical decisions escalate to human approval | [agents.md](./agents.md) — ProducerAgent |
| **Provenance (C2PA)** | Every artifact is signed; downstream agents verify chain | C2PA spec |
| **Continuous Self-Improvement** | Agents learn from outcomes, store episodic memory, ratchet quality | Reflexion (Shinn 2023) |

| Agent/System | Purpose in VA-Agent-Swarm | Specification Documents |
|--------------|--------------------------|------------------------|
| **Research Agent** | Powers knowledge acquisition for any agent that needs domain research, source discovery, and synthesis | [research_agent_functional_specification.md](./research_agent_functional_specification.md) + [research_agent_technical_specification.md](./research_agent_technical_specification.md) |
| **Process Optimization Agent** | Continuously optimizes production workflows using DMAIC + Lean + multi-agent consensus | [optimization_agent_functional_specification.md](./optimization_agent_functional_specification.md) + [optimization_agent_technical_specification.md](./optimization_agent_technical_specification.md) |
| **General Creative Agent (GCA)** | Provides creative ideation via SSOR model for DirectorAgent, ScreenwriterAgent, ConceptArtistAgent, etc. | [general_creative_agent_functional_specification.md](./general_creative_agent_functional_specification.md) + [general_creative_agent_technical_specification.md](./general_creative_agent_technical_specification.md) |
| **Agentic RAG System** | Shared knowledge backbone — retrieves, compounds, and serves contextual knowledge to all agents | [agentic_rag_functional_specification.md](./agentic_rag_functional_specification.md) |
| **Deep Intent Analysis (DIA)** | Analyzes user briefs, audience intent, hidden agendas — feeds IntentAnalysisAgent and DirectorAgent | [intent_analysis_agent_functional_specification.md](./intent_analysis_agent_functional_specification.md) |
| **Coding Agent (N1ch01as Architect)** | Builds and maintains the system's own codebase; implements new agents | [coding_agent_functional_specification.md](./coding_agent_functional_specification.md) |
| **LLM Usage Dashboard** | Monitors API costs and token consumption across all LLM providers used by the swarm | [llm_usage_functional_specification.md](./llm_usage_functional_specification.md) |
| **Podcast Agent** | Automates podcast/radio production workflow (preparation → execution → ending → follow-up) | [podcast_agent_functional_specifcation.md](./podcast_agent_functional_specifcation.md) |
| **Aesthetics Agent** | Shared "artiste sense" — a decomposed multimodal Critic + Aligner + Taste-Keeper that supplies aesthetic scoring, the L2/perceptual judge signal, novelty to the GCA, and `aesthetic` critiques to CinematographerAgent, ColoristAgent, PromptEngineerAgent, AIQAConsistencyAgent, etc. | [aesthetics_agent_functional_specification.md](./aesthetics_agent_functional_specification.md) |

| Document | Agent/System | Status |
|----------|-------------|--------|
| [agentic_rag_functional_specification.md](./agentic_rag_functional_specification.md) | Hybrid Agentic RAG System | Complete |
| [aesthetics_agent_functional_specification.md](./aesthetics_agent_functional_specification.md) | Aesthetics Agent (Critic + Aligner + Taste-Keeper) | Complete |
| [coding_agent_functional_specification.md](./coding_agent_functional_specification.md) | N1ch01as Architect v1.0 (Coding Agent) | Complete |
| [general_creative_agent_functional_specification.md](./general_creative_agent_functional_specification.md) | General Creative Agent (SSOR) | Complete |
| [intent_analysis_agent_functional_specification.md](./intent_analysis_agent_functional_specification.md) | Deep Intent Analysis v2.0 | Complete |
| [llm_usage_functional_specification.md](./llm_usage_functional_specification.md) | LLM Usage & Cost Dashboard | Complete |
| [optimization_agent_functional_specification.md](./optimization_agent_functional_specification.md) | Process Optimization Agent v2.0 | Complete |
| [podcast_agent_functional_specifcation.md](./podcast_agent_functional_specifcation.md) | Podcast Production Agent | Complete |
| [psychological_profile_agent_functional_specifications.md](./psychological_profile_agent_functional_specifications.md) | 100 Creator Psychological Profiles | Complete |
| [psychological_recommendation_agent_functional_specification.md](./psychological_recommendation_agent_functional_specification.md) | Psychology-Based Recommendation | Complete |
| [research_agent_functional_specification.md](./research_agent_functional_specification.md) | Research Agent (grok-research-agent) | Complete |
| [screenwriter_strategic_goal_achievement_agent_functional_specification.md](./screenwriter_strategic_goal_achievement_agent_functional_specification.md) | Screenwriter Goal Achievement | Complete |
| [strategic_goal_achievement_agent_functional_specification.md](./strategic_goal_achievement_agent_functional_specification.md) | Strategic Goal Achievement Framework | Complete |



### From `corpus/study/ai_agent_video_production_workflow.md` Copy: `sources/excerpts/ai_agent_video_production_workflow.md`.


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

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 53 | **OrchestratorAgent** | Runs the CrewAI / AutoGen / LangGraph DAG; schedules nodes; handles retries, timeouts, fan-out/fan-in | LangGraph + CrewAI + AutoGen reference patterns; Airflow/Temporal workflow corpora; PGA producer-schedule templates | DAG completion rate ≥99.5%; SLA adherence; deadlock rate = 0 | Lower mean time-to-delivery than human EP/line-producer at same scope | ProducerAgent (scope), JudgeAgent (dispute), HiTL on stall | All agents (resource burn, retry storms) |
| 54 | **PlannerAgent** | Decomposes a brief into a phased DAG with agent assignments + critic gates | Production-management corpora; PMBOK; CrewAI task graphs; phase templates from `human_video_production_workflow.md` | Plan validity (no missing critic gate); estimated cost variance vs actual <10% | Produces tighter, cheaper plans than producer-EP first pass in blind A/B | ProducerAgent, FinanceAgent (budget) | RouterAgent (wrong agent picked), OrchestratorAgent |
| 55 | **RouterAgent** | Picks the right specialist agent (and model) for each subtask | Agent-capability registry; benchmark history (cost/quality/latency per agent × task type) | Routing accuracy ≥95% vs oracle; cost-per-task within budget | Beats human producer in agent/vendor selection on cost-adjusted quality | OrchestratorAgent, CostOptimizerAgent | PlannerAgent (bad decomposition) |
| 56 | **JudgeAgent** | Adjudicates inter-agent disputes via multi-agent debate; scores outputs against rubric | Du et al. 2023 (LLM debate); MT-Bench rubrics; guild scoring sheets (DGA/WGA/ASC/ACE) | Inter-rater agreement vs human expert panel ≥0.8 Cohen's κ | Higher κ vs human jury than median human juror | HiTL on overturned rulings | DirectorAgent, ScreenwriterAgent, any disputing pair |
| 57 | **GateKeeperAgent** | Manages phase transitions; verifies L1/L2/L3 success criteria; signs C2PA provenance | Stage-gate methodology; PGA Producers Mark; QMS audit patterns | Zero leaked defects past gate; sign-off SLA hit rate ≥99% | Lower escaped-defect rate than human QA lead | ComplianceAgent, AIQAConsistencyAgent | OrchestratorAgent (premature advance) |
| 58 | **MemoryAgent** | Episodic + long-term project memory; retrieval for any agent | Reflexion (Shinn 2023); MemGPT; vector-DB best practices | Retrieval precision@5 ≥0.9 on project Q&A; freshness SLA | Higher recall than producer's project bible at scale | All agents (correction events) | All agents (stale facts) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 59 | **IdeationAgent** | Divergent brainstorm of concepts, hooks, taglines, what-if angles | Cannes Lions Grand Prix archive; D&AD winners; IDEO design-thinking corpus; SCAMPER / Lateral Thinking (de Bono) | Idea-count per brief; novelty (embedding distance from corpus); semantic diversity within batch | Wins blind agency-pitch shootouts on first-round concept density | CreativeDirectorAgent, NoveltyAgent | CopywriterAgent (derivative), DirectorAgent (unfilmable) |
| 60 | **NarrativeArcAgent** | Shapes 3-act / Save-the-Cat / Kishōtenketsu / Hero's Journey structure | Campbell *Hero with a Thousand Faces*; Snyder *Save the Cat*; Truby *Anatomy of Story*; Black List structural analyses | Beat-sheet coverage 100%; turning-point spacing matches genre prior; emotional-arc curve fit | Beats WGA-staffed first drafts on structural-rubric blind reads | ScreenwriterAgent, DirectorAgent | ScreenwriterAgent (sagging middle) |
| 61 | **StyleTransferAgent** | Applies named aesthetic (Wes Anderson, A24, cyberpunk, vaporwave, Studio Ghibli, etc.) consistently across shots | Curated style corpora per look; LoRA/seed registries; reference-frame banks | Style-similarity score (CLIP/DINO) ≥0.85 to reference; consistency variance across shots ≤τ | Wins blind preference vs human colorist+grader doing same look | DirectorAgent, ColoristAgent | GeneratorAgent (off-style), ColoristAgent (palette drift) |
| 62 | **WorldBuildingAgent** | Builds lore, rules, geography, factions, magic/tech systems for series & franchises | Tolkien legendarium; *Worldbuilding* (Adams); fan-wiki corpora; series-bible leaks | Internal-consistency check (no contradictions across N entries); rule-completeness | Lower contradiction rate than human writers'-room bibles at 10× volume | ShowrunnerAgent, FactCheckerAgent | ScreenwriterAgent (lore break), ConceptArtistAgent |
| 63 | **MoodBoardAgent** | Builds reference boards: visual, sonic, tonal | Pinterest/Are.na corpora; lookbook archives; Spotify-Canvas references | Reference coherence (cluster tightness); brief alignment | Faster + tighter boards than human art director in blind A/B | DirectorAgent, ProductionDesignAgent | ConceptArtistAgent (off-mood) |
| 64 | **NoveltyAgent / Anti-Cliché Critic** | Flags tropes, clichés, and over-fit-to-corpus outputs | TV Tropes; OpenSubtitles n-gram frequency; corpus-novelty embeddings | Cliché-hit count per output; novelty score relative to category prior | Catches more clichés than experienced script editor in blind eval | IdeationAgent, ScreenwriterAgent | ScreenwriterAgent (trope-stuffed), CopywriterAgent (templated) |
| 65 | **EmotionalArcAgent** | Maps valence/arousal curve across runtime; suggests beats | Plutchik emotion wheel; affective-computing corpora; *Story Genius* (Cron) | Curve-fit to target shape; viewer-biosignal-proxy regression accuracy | Better retention-curve prediction than test-screening NRG cards | DirectorAgent, EditorAgent, ComposerAgent | EditorAgent (flat middle), ComposerAgent (cue mismatch) |

Maps the 10 workflows in `human_video_production_workflow.md` to agent-only crews per phase. Each cell lists the **lead agent** for that phase plus any critic agents that gate the handoff.

| Phase | Lead Agent | Critic Agents (Gate) |
|---|---|---|
| Concept | TrendIntelligenceAgent + CopywriterAgent | SocialMediaStrategistAgent |
| Production | PromptEngineerAgent / GeneratorOperator | AIQAConsistencyAgent |
| Post | EditorAgent + AccessibilityOptimizerAgent | AccessibilityAgent |
| Review | SocialMediaStrategistAgent | AudienceSimAgent |
| Distribution | SocialMediaStrategistAgent | ComplianceAgent |
| Post-launch | AnalystAgent + CommunityAgent | AudienceSimAgent |

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | PerformanceMarketerAgent + CopywriterAgent | BrandAgent |
| Production | UGCCreatorAgent | DirectorAgent |
| Post | EditorAgent + MotionGraphicsAgent | BrandAgent |
| Review | ComplianceAgent (FTC/IP) | LegalAgent |
| Distribution | PerformanceMarketerAgent | FinanceAgent (budget) |
| Post-launch | PerformanceMarketerAgent + AnalystAgent | AudienceSimAgent |

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
| Concept | TemplateDesignAgent + PersonalizationEngineerAgent | UXAgent |
| Production | PersonalizationEngineerAgent + VoiceCloneAgent | AvatarDesignAgent |
| Post | AIQAConsistencyAgent | AccessibilityAgent |
| Review | TrustSafetyAgent | ComplianceAgent (GDPR/CCPA) |
| Distribution | CRMAgent | ComplianceAgent |
| Post-launch | AnalystAgent | AudienceSimAgent |

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
| Concept | InstructionalDesignAgent + ComplianceAgent + ScreenwriterAgent | SMEAgent |
| Production | AvatarDesignAgent + MotionGraphicsAgent | DirectorAgent |
| Post | EditorAgent + AccessibilityAgent | AccessibilityOptimizerAgent |
| Review | SMEAgent + ComplianceAgent + AccessibilityAgent | LegalAgent |
| Distribution | LMSAgent | AnalystAgent |
| Post-launch | AnalystAgent + InstructionalDesignAgent | LearnerSimAgent |

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
| Concept | BrandStrategistAgent + ScreenwriterAgent | AvatarDesignAgent |
| Production | AvatarDesignAgent + VoiceCloneAgent + LipSyncAgent | AIQAConsistencyAgent |
| Post | MotionGraphicsAgent + EditorAgent | AccessibilityAgent |
| Review | BrandAgent + ComplianceAgent (C2PA, AI disclosure) | DeepfakeDetectionAgent |
| Distribution | MarketingAgent | ComplianceAgent |
| Post-launch | AnalystAgent + CommsAgent | AudienceSimAgent |

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | ShowrunnerAgent + JournalistAgent + ScreenwriterAgent | FactCheckerAgent |
| Production | DirectorAgent + CinematographerAgent (DoP) + ArchiveProducerAgent + MotionGraphicsAgent + FactCheckerAgent | LegalAgent (clearance) |
| Post | EditorAgent + VoiceOverAgent + ColoristAgent + SoundMixerAgent | AccessibilityAgent |
| Review | FactCheckerAgent + LegalAgent + StandardsEditorAgent | EthicsAgent (SPJ) |
| Distribution | ChannelManagerAgent + SocialMediaStrategistAgent + SEOAgent | AnalystAgent |
| Post-launch | AnalystAgent + StandardsEditorAgent | CorrectionsAgent |



### From `corpus/study/human_video_production_workflow.md` Copy: `sources/excerpts/human_video_production_workflow.md`.


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
| 38 | **Financial Analyst (for video)** | Accurate market / token / earnings facts | CFA charter, SEC/Reg-BI literacy | CF
…



### From `corpus/study/agent_loop_v3.md` Copy: `sources/excerpts/agent_loop_v3.md`.


**Version:** 2026-06-10 (v3 — Cognitive-Enhanced: Integrated high-priority traditional human thinking models from ranked analysis in thinking_model.md (Cynefin, Premortem, AAR, Double-Loop Learning, RPD, Dual Process, Metacognition, 5 Whys/Fishbone, Red Team, Paul-Elder, etc.) for adaptive context routing, proactive risk mitigation, fast/slow deliberation paths, structured reflection, and deeper self-evolution. All v2 details preserved; new mechanisms are additive, configurable, and mapped to existing phases.)  
**Research Sources**: "Why Do Multi-Agent LLM Systems Fail?" (MASFT taxonomy, 14-18 failure modes), Reflexion, Prospector, CGI, memory papers, xAI docs, developer reports on infinite loops/context issues, plus systematic review of 40+ human cognitive frameworks (ranked by adoption priority for agent loops).
**Purpose:** Actionable reference for building reliable, scalable LLM-based agent systems. Combines academic foundations (ReAct synergy of reasoning + acting), xAI's server-side agentic implementation (multi-agent orchestration for deep research), and advanced hierarchical patterns (planner + specialists + self-evolution).  
**Target Audience:** Builders of harnesses, multi-agent systems, coding agents, research agents (e.g., N1ch01as-style Architect with critic/self-refinement loops).  
**Key Principle:** Controlled loops with explicit state, structured outputs, quality gates, and hierarchical delegation. Not uncontrolled chain reactions — managed orchestration with bubbling-up consolidation and deliberate synthesis.

| Thinking Model (Rank / Score) | Primary Integration Point | How Operationalized (v3 Enhancement) | Key Benefit vs v2 Baseline |
|-------------------------------|---------------------------|--------------------------------------|----------------------------|
| **Cynefin Framework** (1 / 10) | Phase 0 (post-spec) + Phase 1 entry/replan decision | Classify task context: Simple (clear cause-effect) / Complicated (expert analysis) / Complex (emergent) / Chaotic (crisis). Dynamically configure loop params: Fast Recognition Path enabled + lighter gates for Simple/Complicated; Full deliberative + heavy reflection/critics + deeper diagnostics for Complex/Chaotic. | Enables adaptive loop intensity (Fast vs Full) — highest-leverage addition for efficiency + reliability. |
| **Premortem Analysis** (2 / 10) | Phase 0 (after plan gen, before state commit) | Mandatory "assume spectacular failure in 6-12 months → work backward to identify top causes/risks → explicitly mitigate in living spec, success criteria, todo items, or agent roles." Can be run by orchestrator LLM or dedicated Red Team critic. | Directly strengthens Phase 0 planning with proactive risk simulation & critic; near-zero cost. |
| **After-Action Review (AAR)** (3 / 10) | Phase 4 (every milestone reflection or termination) | Structured 4-question template: (1) What was supposed to happen? (vs original spec/plan) (2) What actually happened? (from tracer/obs) (3) Why? (diagnosis) (4) What next? (lessons → concrete evolution actions). Feeds self-evolution. | Perfect upgrade for Phase 4 reflection + self-evolution; highly practical structured learning. |
| **Double-Loop Learning** (4 / 9.5) | Phase 4 (after AAR single-loop fixes) | After tactical fixes, explicitly ask: "What governing variables/assumptions (prompt templates, success criteria definitions, agent role boundaries, memory schemas, verification thresholds, or even the task decomposition strategy) led us here? Should they change at the meta level?" Only then commit versioned updates. | Core to making self-evolution truly powerful (double-loop) rather than symptom patching. |
| **Recognition-Primed Decision (RPD)** (5 / 9.5) + **Dual Process Theory (System 1 & 2)** (8 / 9) | Phase 1 (Thought/Decide step) + Memory layer | **Fast Recognition Path** (new): Before verbose ReAct, query Pattern Store (long-term memory of successful high-quality traces + outcome metadata + embeddings). If strong similarity match (and Cynefin context permits), perform lightweight mental simulation ("Similar to trace #47, expected good result with action Z") then act with minimal tokens. System 1 = fast/intuitive/RPD for routine/expert; System 2 = slow/deliberate full ReAct for novel/risky/uncertain. Metacognition (below) decides switch. Fallback to full loop on low confidence. | Enables high-value "Fast Recognition Path" in v3 for expert domains/repeated tasks; foundation for adaptive fast/slow thinking. |
| **Metacognition Cycle** (7 / 9) | Parallel lightweight process alongside all Phase 1 iterations | Ongoing: Planning (align intent to spec) → Monitoring (bias detection, context fit via Cynefin, progress vs todo/success criteria, confidence drift) → Evaluating (quick rigor pulse) → Adjust (trigger mode switch, early replan, or gate escalation in real time or at next decision). | Direct parallel to state management; easy to implement as lightweight meta-prompt or separate small LLM call. |
| **5 Whys + Ishikawa Fishbone + Fault Tree** (6 / 9) | Phase 4 (AAR "Why?" diagnosis) + Verifier/Critic issue analysis | On persistent failures or low-confidence observations: Drill with iterative 5 Whys; categorize root causes via Fishbone (People/Prompts, Process/Methods, Models/Tools, Data/Material, Environment/Context, Metrics) or simple fault tree. Results drive Double-Loop changes and spec hardening. | Greatly strengthens Thought + Reflection for complex problems; systematic visual + deep cause analysis. |
| **Red Team Thinking** (12 / 8) | Verifier / Phase 3 quality gates + Premortem | Dedicated critic mode or separate lightweight agent: "Adversarially attack this plan/draft/output to surface hidden weaknesses, edge cases, or single points of failure." Complements standard verifier schema. | Strong built-in devil’s advocate; easy to implement as dedicated critic agent role. |
| **Paul-Elder Critical Thinking Framework** (9 / 8.5) | Verifier prompt + Thought step augmentation | Enhance `verify_output` and decision prompts with Elements of Thought (purpose, question at issue, information, concepts, assumptions, inferences, implications, point of view) + Intellectual Standards checklist (clarity, accuracy, precision, relevance, depth, breadth, logic, significance, fairness, sufficiency). | Excellent for enhancing Thought and Verifier quality; strong bias and rigor detection. |
| **Theory of Constraints (TOC)** (10 / 8.5) + **TRIZ** (14 / 8) | Phase 3 (Harmonize/Consolidation) + conflict resolution in self-evolution | When sub-results conflict or goals contradict: Use TOC Evaporating Cloud to surface and resolve core conflicts; apply TRIZ contradiction principles for inventive solutions. Feeds versioned prompt/agent edits. | Powerful for resolving conflicting goals; synergizes extremely well with TRIZ and self-evolution. |
| **Six Thinking Hats** (13 / 8) + **SCAMPER / Osborn-Parnes CPS** (15/11) | Phase 3 consolidation or creative sub-agent ideation | Optional multi-perspective pass (White=facts/data, Red=intuition/feelings, Black=risks/critic, Yellow=benefits/opportunities, Green=creativity/alternatives, Blue=process/meta) or SCAMPER checklist (Substitute/Combine/Adapt/Modify/Put to other uses/Eliminate/Reverse) during synthesis or when sub-agent is creative-writing/design-oriented. | Reduces blind spots effectively; directly upgrades ideation and creative sub-agents. |

**Additional Implementation Details (v3)**:
- **Memory Architecture Upgrade**: Add "Pattern Store" (vector + metadata of successful/failed traces with outcome scores) to support RPD fast matching. Hierarchical memory now explicitly tags traces with Cynefin context type for better retrieval.
- **Verifier / Critic Enhancements**: `verify_output` function now accepts `critic_mode` (or runs ensemble): "standard" | "red_team" | "paul_elder" | "six_hats". Returns aggregated issues + suggestions. Can be parallelized for depth.
- **Configurability in Task Spec**: New fields e.g. `"cognitive_profile": {"enable_fast_path": true, "reflection_style": "aar_double_loop_5whys", "critic_modes": ["red_team", "paul_elder"], "cynefin_classification": "complex"}` or auto-detected.
- **Metacognition Implementation**: Lightweight parallel prompt or small dedicated LLM call every N steps or on confidence drop / context shift. Updates shared state flags (e.g., `current_mode: "fast" | "full"`, `bias_flags: [...]`).
- **Early Exit / Efficiency**: Cynefin + RPD + Metacognition together allow safe early termination or fast-pathing on well-understood sub-problems without sacrificing the rigorous gates on hard parts — directly mitigating token waste and infinite-loop risks.

### Major Problem Categories & Frequency/Significance
1. **Specification & Design Ambiguities (Largest Category)**
   - Disobeying or misinterpreting task spec, vague roles, missing success criteria or output contracts.
   - **Impact**: Agents go off-track early; errors compound downstream.
   - **Mitigations**:
     - Phase 0: Mandatory structured Task Specification with explicit success criteria, constraints, output schema, and quality thresholds. Use "living spec" that can be updated.
     - Add automated spec validation (critic or schema check) before loop starts.
     - Clear role definitions and information contracts between orchestrator and sub-agents.

4. **Hallucinations, Error Compounding & Verification Weakness**
   - Fabricated facts, incorrect tool results interpretation, or unverified claims propagating (worse in multi-agent).
   - **Impact**: Unreliable final outputs; cascading failures.
   - **Mitigations**:
     - **Verifier / Critic agents** as mandatory quality gates (Phase 3 consolidation and after sub-results).
     - Structured observation schema (status, confidence, issues list) + cross-validation (compare across agents/sources).
     - Multi-form verification (factual grounding in observations + external checks).
     - Trajectory ranking (e.g., Prospector-style critic selects best among multiple attempts).
     - In self-evolution: Only commit changes validated on held-out traces.

### How Mitigations Integrate into the Loop Phases
- **Phase 0 (Init)**: Spec engineering + validation is the single highest-ROI fix.
- **Phase 1 (Core Loop)**: Cycle detection, bounded steps/reflection, structured observations, progress tracking.
- **Phase 2 (Delegation)**: Narrow sub-specs + contracts; orchestrator monitoring.
- **Phase 3 (Consolidation)**: Verifier/critic gates, cross-validation, harmonization.
- **Phase 4 (Reflection/Self-evolution)**: Validation before applying changes; bounded loops.
- **Phase 5 (Termination)**: Verifier + explicit Done with evidence.

### Phase 0: Initialization (Spec-Driven Setup)
**Goal**: Establish clear contract before any loop iterations.
1. Parse human instruction → generate/validate **Task Specification** (structured: objective, success criteria, constraints, output format, max budget/steps/tokens, quality thresholds).
2. Create **initial state**:
   - `task.md` or structured scratchpad (current plan, todo list, progress, open questions).
   - Memory: Short-term (recent observations), long-term (retrieved knowledge, past versions).
   - Tracer / execution log (for later reflection).
   - Version registry (for prompts/tools/agents if evolving).
3. **Optional Plan Generation** (Plan-and-Execute flavor, recommended for complex tasks):
   - Orchestrator LLM generates high-level plan (numbered steps or dependency graph).
   - Validate plan against spec (self-critique or dedicated critic).
   - Store in state.
4. **v3 Cognitive Enhancements (Cynefin + Premortem)**:
   - **Cynefin Classification** (context-aware routing): LLM or lightweight classifier tags the task (Simple / Complicated / Complex / Chaotic) based on clarity of cause-effect, expert knowledge needed, emergence, or crisis nature. Store in task_spec and use to auto-configure loop behavior (see 1.4 table): e.g., Simple/Complicated → prefer Fast Recognition 
…



### From `corpus/study/agent_loop_v2.md` Copy: `sources/excerpts/agent_loop_v2.md`.


**Version:** 2026-06-07 (Updated with comprehensive research on known agent loop failure modes from MASFT taxonomy & related studies, plus targeted mitigations from Reflexion, critic frameworks, structured specs, memory architectures, and production patterns)  
**Research Sources**: "Why Do Multi-Agent LLM Systems Fail?" (MASFT taxonomy, 14-18 failure modes), Reflexion, Prospector, CGI, memory papers, xAI docs, and developer reports on infinite loops/context issues.
**Purpose:** Actionable reference for building reliable, scalable LLM-based agent systems. Combines academic foundations (ReAct synergy of reasoning + acting), xAI's server-side agentic implementation (multi-agent orchestration for deep research), and advanced hierarchical patterns (planner + specialists + self-evolution).  
**Target Audience:** Builders of harnesses, multi-agent systems, coding agents, research agents (e.g., N1ch01as-style Architect with critic/self-refinement loops).  
**Key Principle:** Controlled loops with explicit state, structured outputs, quality gates, and hierarchical delegation. Not uncontrolled chain reactions — managed orchestration with bubbling-up consolidation and deliberate synthesis.

### Major Problem Categories & Frequency/Significance
1. **Specification & Design Ambiguities (Largest Category)**
   - Disobeying or misinterpreting task spec, vague roles, missing success criteria or output contracts.
   - **Impact**: Agents go off-track early; errors compound downstream.
   - **Mitigations**:
     - Phase 0: Mandatory structured Task Specification with explicit success criteria, constraints, output schema, and quality thresholds. Use "living spec" that can be updated.
     - Add automated spec validation (critic or schema check) before loop starts.
     - Clear role definitions and information contracts between orchestrator and sub-agents.

4. **Hallucinations, Error Compounding & Verification Weakness**
   - Fabricated facts, incorrect tool results interpretation, or unverified claims propagating (worse in multi-agent).
   - **Impact**: Unreliable final outputs; cascading failures.
   - **Mitigations**:
     - **Verifier / Critic agents** as mandatory quality gates (Phase 3 consolidation and after sub-results).
     - Structured observation schema (status, confidence, issues list) + cross-validation (compare across agents/sources).
     - Multi-form verification (factual grounding in observations + external checks).
     - Trajectory ranking (e.g., Prospector-style critic selects best among multiple attempts).
     - In self-evolution: Only commit changes validated on held-out traces.

### How Mitigations Integrate into the Loop Phases
- **Phase 0 (Init)**: Spec engineering + validation is the single highest-ROI fix.
- **Phase 1 (Core Loop)**: Cycle detection, bounded steps/reflection, structured observations, progress tracking.
- **Phase 2 (Delegation)**: Narrow sub-specs + contracts; orchestrator monitoring.
- **Phase 3 (Consolidation)**: Verifier/critic gates, cross-validation, harmonization.
- **Phase 4 (Reflection/Self-evolution)**: Validation before applying changes; bounded loops.
- **Phase 5 (Termination)**: Verifier + explicit Done with evidence.

### Phase 0: Initialization (Spec-Driven Setup)
**Goal**: Establish clear contract before any loop iterations.
1. Parse human instruction → generate/validate **Task Specification** (structured: objective, success criteria, constraints, output format, max budget/steps/tokens, quality thresholds).
2. Create **initial state**:
   - `task.md` or structured scratchpad (current plan, todo list, progress, open questions).
   - Memory: Short-term (recent observations), long-term (retrieved knowledge, past versions).
   - Tracer / execution log (for later reflection).
   - Version registry (for prompts/tools/agents if evolving).
3. **Optional Plan Generation** (Plan-and-Execute flavor, recommended for complex tasks):
   - Orchestrator LLM generates high-level plan (numbered steps or dependency graph).
   - Validate plan against spec (self-critique or dedicated critic).
   - Store in state.
4. Decide architecture: Flat ReAct (simple) vs Hierarchical (complex research/coding) vs Hybrid.

### Phase 1: Core Iteration Loop (ReAct-Inspired, Controlled)
While not terminated:
1. **Observe Current State**: Load full/relevant history + task spec + current plan/todo + latest observations. (Summarize aggressively if context long — use memory manager.)
2. **Reason (Thought)**:
   - Analyze progress vs success criteria.
   - Identify gaps, risks, exceptions.
   - Decide strategy: direct tool, delegate sub-task, synthesize so far, reflect/critique, or finish.
   - Update internal plan or todo if needed.
3. **Act / Decide Next** (strict structured output — parseable):
   - **Option A (Tool)**: Call built-in or custom tool (with args). xAI-style: server handles execution in loop.
   - **Option B (Delegate)**: Invoke sub-agent with narrow sub-instruction + context slice + success criteria for that sub-task. (Hierarchical)
   - **Option C (Internal)**: Update state/plan only, or run critic on draft.
   - **Option D (Finish)**: Output final answer if quality gates passed.
4. **Execute & Observe**:
   - Run action (tool or sub-agent loop).
   - Collect **structured observation**:
     ```json
     {
       "status": "success | partial | failed",
       "data": {...},
       "summary": "concise natural language",
       "confidence": 0.85,
       "issues": ["list of problems"],
       "next_suggestions": ["..."],
       "trace_id": "..."
     }
     ```
   - Append to history + update todo/state.
5. **Light Reflection** (every N steps or on failure): Quick self-critique — "Is this trajectory still aligned? Any obvious fix?"

step = 0
    while step < state.max_steps:
        step += 1
        current_hash = hash_state(state)
        if current_hash in state.seen_states:
            print("Cycle detected — forcing replan or terminate")
            # In production: trigger critic or escalate to human
            break
        state.seen_states.add(current_hash)

**Code Example: Lightweight Verifier / Critic Agent (Prompt + Schema)**

### Phase 3: Consolidation, Synthesis & Restructuring
After sub-results or major milestones:
1. **Aggregate**: Collect all relevant observations + plan progress.
2. **Harmonize**: LLM (or dedicated Reporter agent) merges, deduplicates, cross-references, resolves contradictions. Produces unified view.
3. **Restructure**: Transform into target output shape (report, code, answer, updated plan). Enforce format from initial spec.
4. **Quality Gate**:
   - Run critic/refiner: Score against success criteria, check for hallucinations/gaps, suggest fixes.
   - If fails: Trigger refinement loop (re-plan, re-delegate specific parts, or self-edit).
   - If passes: Proceed (or do final polish).
5. **Update State**: Persist consolidated knowledge to long-term memory / versioned artifacts.

### Phase 4: Reflection, Critique & Self-Evolution (Advanced)
- **Per-trajectory or milestone reflection**: LLM summarizes trace, diagnoses failures/successes, proposes improvements (prompt edits, tool patches, new sub-agent types).
- **Self-evolution loop** (inspired by AgentOrchestra):
  1. Collect trace via tracer.
  2. Attribute errors / opportunities (LLM or TextGrad-style).
  3. Propose targeted changes (to prompts, tools, agent configs, or even generated code).
  4. Validate changes (re-execute on held-out or similar task; check metrics).
  5. If improved: Register new version (with lineage). Support rollback.
- **Critic Agent Role**: Separate lightweight agent that reviews drafts/plans without full execution. Can be invoked at gates.
- **Benefits**: Continuous improvement during runtime; production systems become more robust over repeated use on similar task distributions.

| Task Complexity       | Recommended Pattern                  | Key Features to Enable          | Example Use Case |
|-----------------------|--------------------------------------|---------------------------------|------------------|
| Simple fact lookup    | Flat ReAct (single loop)            | Tool calling, basic thought    | Quick search + answer |
| Multi-step research   | xAI Multi-Agent or Hierarchical     | Parallel agents, leader synth  | Deep analysis with sources |
| Coding / long project | Plan-first + Hierarchical + Worktrees | Sub-agents in isolation, todo.md | Full app generation + debug |
| Open-ended / creative | ReAct + Reflection + Self-evolution | Critic gates, versioned prompts| Iterative design refinement |
| High-stakes / reliable| All above + strong Quality Gates    | Structured results, validation | Enterprise automation |

- **Context explosion**: Aggressive summarization + hierarchical state (local sub-memories).
- **Infinite loops / thrashing**: Hard max iterations + progress tracking in todo + critic that can force replan or escalate.
- **Poor consolidation**: Mandate structured sub-results + dedicated harmonization/reporter step.
- **Hallucinations in plans**: Ground every major claim in observations; use critic before committing to plan.
- **Brittle delegation**: Use explicit sub-task specs + success criteria; validate returned results.
- **Lack of visibility**: Full tracing + optional streaming of reasoning.

This document is designed to be **executable guidance** — copy patterns, adapt pseudocode, and iterate. For refinements, specific code examples in Python/Node, or integration with your existing harness (e.g., critic loops, spec-driven task.md), provide more details on your current stack.



### From `corpus/study/agent_loop.md` Copy: `sources/excerpts/agent_loop.md`.


**Version:** 2026-06-09 (Final synthesized version after deep research, multiple critique passes, and iterative refinement)  
**Based on:** ReAct (Yao et al.), xAI production agentic systems, MASFT failure taxonomy, AgentOrchestra/TEA patterns, Reflexion, critic frameworks, and extensive resilience engineering.

**Purpose:** A complete, actionable, self-contained reference for building reliable, observable, and evolvable LLM agent loops and harnesses. Designed for spec-driven development, critic/self-refinement loops, and production deployment.

| Category                        | % Impact | Key Problems                          | Primary Mitigations                              |
|--------------------------------|----------|---------------------------------------|--------------------------------------------------|
| Specification & Design         | ~40%+   | Vague specs, missing success criteria | Structured Task Spec + validation in Phase 0    |
| Infinite Loops / Thrashing     | High    | Repetitive actions, no progress       | Cycle detection + `max_steps` + progress gates  |
| Context Explosion / Rot        | High    | Lost information in long histories    | Hierarchical memory + structured state + summarization |
| Verification & Hallucination   | High    | Unchecked outputs, error compounding  | Verifier/Critic agents + structured observations |
| Coordination & Misalignment    | High    | Role conflicts, stale state           | Strong orchestrator + information contracts     |
| Termination Problems           | Medium  | Premature stop or never stops         | Explicit `Done` action + quality gates          |

### Phase 3: Consolidation & Quality Gates
- Aggregate results from multiple branches.
- Run **Verifier/Critic** agent.
- Harmonize, resolve conflicts, restructure.
- Update global plan/state.

1. **Week 1**: Phase 0 (structured spec) + basic ReAct loop with cycle detection.
2. **Week 2**: Add Verifier/Critic + structured observations.
3. **Week 3**: Hierarchical delegation + circuit breaker.
4. **Week 4+**: Self-evolution, full tracing, and iterative refinement using this document as the spec.



### From `corpus/study/lifes_quiet_redemption_agent_workflow.md` Copy: `sources/excerpts/lifes_quiet_redemption_agent_workflow.md`.


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

| Service / Capability | Provided By | Role on This Film |
|---|---|---|
| **Aesthetics scoring (Critic + Aligner + Taste-Keeper)** | Aesthetics Agent | Supplies the L2/perceptual "is this beautiful + warm?" judge signal to Cinematographer, Colorist, PromptEngineer, AIQA |
| **Strategic Goal Achievement (6-stage self-inquiry)** | Strategic Goal framework | Turns the vague "make people feel life saved them" goal into measurable creative targets for Planner/Director |
| **Agentic RAG knowledge backbone** | Agentic RAG System | Serves Chinese cinematic references, golden-hour lighting recipes, prompt patterns to any agent on demand |
| **Psychological profiling / recommendation** | Psych Profile + Recommendation agents | Tunes narrator tone and audience-resonance prediction (Big Five / emotional state) for AudienceSim and Personalization |
| **Continuous self-improvement (Reflexion + RLAIF)** | Optimization Agent + EvaluationHarnessAgent (#79) | Feeds 30/60/90-day retention/ROAS back into prompt + edit choices for the next film in the series |
| **Shared Artifact Handoff Contract (C2PA-signed manifests)** | All agents | Every clip, stem, and master carries `artifact_id`, `continuity_state`, `qc_status`, `provenance_manifest` between phases |
| **Critique Bus (CritiqueMessage JSON)** | All agents | Structured blocker/major/minor feedback; disputes escalate to JudgeAgent → HiTL |



### From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


**Build (each as a crosscutting service agent, all on `BaseAgent`):**
1. **DIA (Deep Intent Analysis)** — parses briefs → structured intent (goals, audience, hidden agendas, constraints). The entry point of every production.
2. **GCA (SSOR)** — creative ideation engine; the 7-phase SSOR pipeline + domain factory. Consumed by Director/Screenwriter/ConceptArtist/Ideation.
3. **Process Optimization Agent** — DMAIC + Lean + multi-agent consensus over workflow telemetry.
4. **Strategic Goal Achievement** — 6-stage goal-clarification framework used by all planning agents.
5. **Complex Problem Solving** — WHAT/WHY/HOW/DO/REVIEW methodology for diagnostic agents.
6. **Aesthetics Agent** — the decomposed multimodal Critic + Aligner + Taste-Keeper (per the spec you authored); supplies `qc.l2`/perceptual scoring, novelty (D9) to GCA, and `aesthetic` critiques. Wire its `AestheticVerdict` into `packages/qc` and the critique bus.

**Build:**
- **Agent Factory** (`packages/agent-factory`): `AgentConfig (YAML) → runnable BaseAgent`. Validates prompt/rubric/tools/QC refs; registers into `agents/_registry.yaml`; generates the per-agent test skeleton. This is the engine for M7–M9.
- **Workflow A craft agents** (subset, via factory): TrendIntelligenceAgent, CopywriterAgent, SocialMediaStrategistAgent, PromptEngineerAgent/GeneratorOperator, AIQAConsistencyAgent, EditorAgent, AccessibilityOptimizerAgent, AudienceSimAgent, AnalystAgent — exactly the crew in [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §3.1.
- **Workflow A DAG** (`workflows/A_viral_hook.py`): Concept → Production → Post → Review → Distribution → Post-launch, with the spec'd critic gates.
- End-to-end run: brief → DIA → Planner builds the A-DAG → agents execute (mock gen) → artifacts flow with handoff contract → critique bus active → QC mesh gates → C2PA-signed deliverable → events on the bus.

**Claude Code workflow:** Build gateway first (typed, tested) so the UI has a real contract. Then UI components, driven by the WebSocket event types. Use Playwright for the critical journeys. Honor `RETHINK_100_IMPROVEMENTS.md` as a UI hardening backlog.

Each of the 10 archetypes (A–J) in [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §3 becomes one LangGraph graph in `workflows/`. They share the §3.0 skeleton (Greenlight → Pre-production → Production → Post → Review/Release → Distribution → Post-launch) and differ only in which agents lead each phase and which critics gate the handoff.

**Build order of workflows:** A (M6) → C, E, B (M7) → F, G, H, I (M8) → D (M11, needs personalization) → J (M12, full-system dry-run). A workflow is "done" when its DAG runs end-to-end on mock providers, every phase gate enforces its critic set, and the final artifact carries a complete provenance chain.

| # | Risk | Likelihood | Impact | Mitigation (where in plan) |
|---|------|-----------|--------|----------------------------|
| R1 | Architecture flaw discovered after broad agent build | Med | High | Vertical slice M6 before breadth (G2, §6.1) |
| R2 | Contract drift across 114 agents | High | High | Frozen contracts + `contract-guardian` + snapshot tests (§5, §9.2) |
| R3 | Runaway LLM/gen cost | High | High | Metering+budget gates from M3; mock providers in CI; live-smoke cap (§10.2) |
| R4 | Temporal↔LangGraph boundary confusion | Med | High | ADR-003 + kill/resume tests in M2 (§6 M2) |
| R5 | LLM-judge score noise destabilizes gates | High | Med | Frozen, pinned judges + golden sets (§9.4) |
| R6 | Reward hacking / "pretty slop" from aesthetic reward | Med | Med | Aesthetics Agent anti-hack layer; ensemble disagreement; HiTL on low confidence |
| R7 | Provider outage/rate-limit stalls productions | Med | Med | Provider abstraction + Router fallback + retries (§3.3, RouterAgent) |
| R8 | Consent/IP violation in generated likeness/voice | Low | Critical | ComplianceAgent blocking gate + consent chain + C2PA (§10.3) |
| R9 | Context bloat causes Claude Code regressions during build | High | Med | `/clear`+`/compact`+subagents+per-package CLAUDE.md (§2.8) |
| R10 | Prompt injection via ingested web/research content | Med | High | Input sanitization + SafetyRedTeam + least-tool-privilege (§10.3, §9.5) |
| R11 | Scale bottleneck on Redis Streams | Med | Med | NATS migration path designed in from M2 (§3.2, M12) |
| R12 | Non-deterministic tests flake CI | Med | Med | Deterministic mocks + pinned seeds/judges; quarantine flaky tests (§9) |
| R13 | Scope creep (role inflation: new agents that close no real gap) | Med | Med | Reject per workflow-doc rule §1.1 working-rule #4; ADR required for any agent beyond the 114 |

### Theme 6 — Safety, Security & Compliance (51–60)
51. SafetyRedTeam attack-success ≤1% across the attack taxonomy.
52. Prompt-injection defenses on every agent ingesting external/user content.
53. Consent chain verified before any likeness/voice generation.
54. C2PA signs 100% of releasable artifacts; verification passes downstream.
55. FTC/HIPAA/GDPR-CCPA/IP/EU-AI-Act checklists wired into ComplianceAgent.
56. Secrets never in repo/logs; secret-scan hook + CI gate active.
57. RBAC enforced on all gateway mutations (gate approve, retry, config).
58. Dependency CVE scan + SBOM produced each release; criticals block.
59. AI-disclosure applied where required (avatar/synthetic content).
60. PII handled with generic placeholders in samples; real PII only in consented project data.

### Theme 8 — Frontend & Human Experience (71–80)
71. UI launches/monitors/critiques/approves/delivers Workflow A end-to-end.
72. WebSocket live updates are <50ms-class; DAG node states accurate.
73. No agent→UI direct calls (all via event bus + gateway).
74. WebSocket reconnect restores full state without duplication.
75. Gate Approval Dialog signs C2PA on approval; rejection routes feedback correctly.
76. Budget/quality dashboards reflect backend truth in real time.
77. Playwright E2E covers the critical journeys; green in CI.
78. RBAC denies unauthorized actions in the UI and gateway.
79. `RETHINK_100_IMPROVEMENTS.md` items triaged; criticals addressed.
80. Production-scale discovery adapts the DAG to project complexity (S-tiers).

### 15.2 Critical path
`M0 → M2 → M3 → M5 → M6 → M7 → M8 → M9 → M12`. M1 feeds M2/M4; M4 supports M8; **M10 can parallelize from M3** in a worktree; M11 slots after M9. The single highest-leverage checkpoint is **G-M6** (vertical slice) — it converts architectural risk into a proven foundation.



### From `corpus/study/thinking_model.md` Copy: `sources/excerpts/thinking_model.md`.


| Rank | Thinking Model | Origin / Field | Core Phases / Steps | Similarity to Agent Loop | Strengths Relative to Agent Loop | **Adoption Score (1-10)** | Why This Score? (Key Reason for Agent Loop) |
|------|----------------|----------------|---------------------|---------------------------|----------------------------------|---------------------------|---------------------------------------------|
| 1 | **Cynefin Framework** | Complexity science (Dave Snowden) | Sense context → Respond appropriately (Simple/Complicated/Complex/Chaotic) | Context-aware decision routing | Superior handling of different problem types | **10** | Enables adaptive loop intensity (Fast vs Full) — one of the highest-leverage additions |
| 2 | **Premortem Analysis** | Decision science (Gary Klein) | Imagine failure → Work backward to find causes → Adjust plan | Pre-action risk simulation & critic | Excellent proactive risk detection | **10** | Directly strengthens Phase 0 planning with almost zero implementation cost |
| 3 | **After-Action Review (AAR)** | Military / Lean | What was supposed to happen? → What happened? → Why? → What next? | Structured post-action reflection | Highly practical for learning and improvement | **10** | Perfect upgrade for Phase 4 reflection + self-evolution |
| 4 | **Double-Loop Learning** | Organizational learning (Argyris & Schön) | Act → Question assumptions → Change governing variables | Deep critic on underlying rules | Surfaces hidden mental models and biases | **9.5** | Core to making self-evolution truly powerful (double-loop) |
| 5 | **Recognition-Primed Decision (RPD)** | Naturalistic decision making (Klein) | Pattern recognition → Mental simulation → Act | Experience-driven quick thinking | Much faster in expert domains | **9.5** | Enables high-value "Fast Recognition Path" in v3 |
| 6 | **5 Whys + Ishikawa Fishbone + Fault Tree Analysis** | Root Cause Analysis (Toyota + Ishikawa) | Problem → Categories → Drill down (5 Whys / Fault Tree) → Root cause → Action | Layered diagnostic questioning | Systematic visual + deep cause analysis | **9** | Greatly strengthens Thought + Reflection for complex problems |
| 7 | **Metacognition Cycle** | Educational psychology (Flavell) | Planning → Monitoring → Evaluating → Adjust | Thinking about thinking in real time | Direct parallel to state management | **9** | Easy to implement as lightweight parallel process |
| 8 | **Dual Process Theory (System 1 & 2)** | Psychology (Kahneman) | Fast intuitive + Slow deliberate with switching | Mostly emulates deliberate thinking | Fluid fast/slow thinking | **9** | Foundation for adaptive Fast vs Full loop paths |
| 9 | **Paul-Elder Critical Thinking Framework** | Philosophy/Education | Elements of Thought + Intellectual Standards | Systematic reasoning quality check | Strong bias and rigor detection | **8.5** | Excellent for enhancing Thought and Verifier quality |
| 10 | **Theory of Constraints (TOC) Thinking Processes** | Management (Eliyahu Goldratt) | Current Reality Tree → Evaporating Cloud (contradictions) → Future Reality Tree | Structured contradiction resolution | Powerful for resolving conflicting goals | **8.5** | Synergizes extremely well with TRIZ and self-evolution |
| 11 | **Osborn-Parnes Creative Problem Solving (CPS)** | Creativity research (Alex Osborn & Sidney Parnes) | Clarify → Ideate → Develop → Implement → Evaluate | Structured creative problem-solving loop | One of the best frameworks for creative agents | **8** | Directly upgrades ideation and creative sub-agents |
| 12 | **Red Team Thinking** | Military / Security | Deliberately attack your own plan to find weaknesses | Adversarial critic mechanism | Strong built-in devil’s advocate | **8** | Easy to implement as dedicated critic agent role |
| 13 | **Six Thinking Hats** | Lateral thinking (Edward de Bono) | Six perspectives used sequentially or in parallel | Multi-perspective analysis | Reduces blind spots effectively | **8** | Good for Phase 3 consolidation and verifier |
| 14 | **TRIZ** | Inventive problem solving (Genrich Altshuller) | Identify contradictions → Apply principles → Resolve | Systematic innovation through contradiction | Superior structured creativity | **8** | Already partially integrated — can be expanded |
| 15 | **SCAMPER** | Creative thinking (Bob Eberle) | Substitute, Combine, Adapt, Modify, Put to other uses, Eliminate, Reverse | Structured idea generation checklist | Very practical rapid ideation tool | **7.5** | Lightweight and easy to add to creative sub-agents |
| 16 | **Kaizen (Continuous Small Improvement)** | Japanese management (Toyota) | Many small, continuous improvements over time | Incremental iterative improvement | Reduces risk of big failed changes | **7.5** | Good philosophy for self-evolution and long-running agents |
| 17 | **Appreciative Inquiry** | Organizational development | Discover strengths → Dream → Design → Destiny | Strengths-based instead of problem-focused | Useful for positive, vision-driven tasks | **6.5** | Good complement when problem-focused loops get stuck |
| 18 | **GROW Coaching Model** | Coaching (John Whitmore) | Goal → Reality → Options → Will | Structured coaching conversation | Good for goal clarification and commitment | **6.5** | Useful for user-facing or planning agents |
| 19 | **OODA Loop** | Military strategy (John Boyd) | Observe → Orient → Decide → Act → loop | Very close to ReAct | Fast tempo in uncertainty | **7** | Already very similar — mainly useful as inspiration |
| 20 | **Design Thinking** | Design/Innovation | Empathize → Define → Ideate → Prototype → Test → Iterate | Think → act → observe → refine | Human-centered creativity | **7** | Good for user-facing or product agents |
| 21 | **Scientific Method** | Science/Philosophy | Observe → Hypothesize → Experiment → Analyze → Conclude → Iterate | Strong iterative hypothesis loop | Rigorous self-correction | **6.5** | Foundational but already largely covered |
| 22 | **PDCA / PDSA Cycle** | Quality management (Deming) | Plan → Do → Check → Act → repeat | Planning + verification loop | Simple continuous improvement | **6.5** | Already heavily used as base |
| 23 | **Hansei (Japanese Reflection)** | Japanese business culture | Deep humble self-reflection after action | Strong post-action reflection | Promotes humility and honest learning | **6** | Good cultural inspiration for reflection tone |
| 24 | **Nemawashi** | Japanese decision making | Informal consensus building before formal decision | Pre-action alignment | Improves multi-agent / human collaboration | **5.5** | Useful for collaborative or multi-agent scenarios |
| 25 | **三思而后行** (Think three times) | Traditional Chinese wisdom | Multiple deliberate thinking rounds before action | Emphasizes careful thought | Simple mental discipline | **5** | Good reminder but low structural value |
| 26 | **Wu Wei (Effortless Action)** | Taoist philosophy | Act in harmony with flow, avoid forced effort | Avoids over-looping | Helps with early exit and flow | **5** | Philosophical inspiration for early termination logic |
| 27 | **Stoic Reflection Practices** | Stoicism | Premeditate adversity + daily journaling | Pre/post action reflection + emotional control | Good for bias and emotional regulation | **5** | Useful but can be partially covered by Premortem + AAR |
| 28 | **High-Context vs Low-Context** | Cross-cultural (Edward Hall) | Implicit vs explicit communication styles | Affects how agents should communicate | Helps in multi-cultural or human-agent interaction | **4.5** | Niche but valuable for specific deployments |
| 29 | **Four Noble Truths + Mindfulness** | Buddhism | Diagnosis of suffering → Path to end it + mindful observation | Structured reflective ethical loop | Strong emotional and bias awareness | **4** | Too philosophical for general agent loops |
| 30 | **Ubuntu Philosophy** | African philosophy | "I am because we are" — communal thinking | Relational and consensus-driven | Good for ethical multi-agent design | **3.5** | Interesting conceptually but hard to operationalize |
| 31 | **Dialectical / Paradoxical Thinking** | Philosophy (Hegel + Eastern) | Hold and synthesize opposites | Handles contradiction and ambiguity | Useful in complex/strategic domains | **4** | Already partially covered by Double-Loop + TOC |
| 32 | **Embodied / 4E Cognition** | Cognitive science | Thinking grounded in body and environment | Richer feedback loops | Important for robotics/embodied agents | **4** | High value only for physical agents |
| 33 | **Bloom's Taxonomy** | Education | Remember → Understand → Apply → Analyze → Evaluate → Create | Hierarchical cognitive depth | Good for educational/tutoring agents | **3.5** | Too abstract for general agent architecture |
| 34 | **Action Learning** | Management (Reg Revans) | Real problem + group questioning + action + learning | Collaborative reflective action | Useful for team-based agents | **3** | Niche unless building multi-agent teams |
| 35 | **Kolb's Experiential Learning Cycle** | Education (David Kolb) | Experience → Reflect → Conceptualize → Experiment | Experience-reflection cycle | Good for learning agents | **3** | Already largely covered by existing reflection |
| 36 | **Gibbs' Reflective Cycle** | Reflective practice | Description → Feelings → Evaluation → Analysis → Action Plan | Emotion-inclusive reflection | Adds emotional dimension | **3** | Partially useful but lower priority than AAR |
| 37 | **IDEAL Problem-Solving Model** | Education (Bransford) | Identify → Define → Explore → Act → Look back | Structured problem solving | Clear separation of thinking and action | **3** | Overlaps heavily with existing phases |
| 38 | **Socratic Method** | Philosophy (Socrates) | Iterative questioning to examine assumptions | Deep assumption challenging | Useful for critic/verifier | **4** | Good but largely covered by Paul-Elder + 5 Whys |
| 39 | **DMAIC** | Six Sigma | Define → Measure → Analyze → Improve → Control | Heavy data-driven analysis | Rigorous for process agents | **3.5** | Too heavy for most general agent use cases |
| 40 | **Iterative SWOT Analysis** | Strategic management | Strengths → Weaknesses → Opportunities → Threats → Iterate | Strategic internal/external analysis | Useful for long-term planning agents | **4** | Good for strategic agents but narrow |



### From `corpus/study/complex_problem_solution_process_model.md` Copy: `sources/excerpts/complex_problem_solution_process_model.md`.


## WHAT: Frame the Problem
Problem solving begins with framing. Framing is critical because the way a problem is defined strongly influences how it is understood and therefore how it will be solved. If the frame is flawed, the rest of the effort may be built on a weak foundation.

The structure of the map should be MECE: mutually exclusive and collectively exhaustive. The answers themselves should be independent and collectively exhaustive. Teams are encouraged to generate possible answers before committing to a structure, defer criticism during generation, and continue drilling only while additional detail brings practical value. A map should be insightful, not merely exhaustive. Teams should ask the "so what?" question to judge whether a branch actually improves understanding.

A project charter should summarize the project's critical information. Stakeholders should understand what the project will deliver, what it will not deliver, how long it will take, how much it will cost, what benefits it should create, what drawbacks it should eliminate, and how it will be completed. Clear agreement on these points prevents scope creep and misunderstandings.



### From `corpus/study/knowledge_router_agent.md` Copy: `sources/excerpts/knowledge_router_agent.md`.


# Knowledge Router Agent — Complete Specification & Implementation Guide
**Version:** 1.0  
**Date:** 2026-06-06  
**Status:** Production-Ready Spec (Rethought across research papers, best practices, and your specific use cases)  
**Domains:** AI Filmmaking (text-to-video, consistency, cinematic pipelines) + AI Agents (multi-agent orchestration, advanced RAG, self-improving systems)  
**Philosophy:** Spec-driven, critic-loop heavy, hybrid deterministic + learned routing, fully traceable, continuously improving.

The **Knowledge Router Agent** is the central intelligence layer that ensures every specialized agent in your system (Character Consistency Critic, Video Prompt Optimizer, Multi-Agent Orchestrator Designer, Shot Planning Agent, etc.) receives **precisely the right knowledge** from your growing ~5,000-file `.md` corpus — with minimal noise, high precision, and strong explainability.

**Core Innovations in This Design**
- **Hybrid Routing Stack** (Metadata-first → Cluster/Centroid semantic → Graph traversal → LLM ranker with reflection)
- **Dual Planner + Router** for complex multi-hop creative/technical pipelines
- **Built-in Multi-Level Critic** (retrieval quality, routing decision, downstream utility) inspired by Self-RAG
- **Performance-Supervised Improvement** (soft labels from actual agent success, like AgentRouter)
- **Traceable + Explainable** by design
- **Training-free bootstrap** (RopMura style) with optional learned components
- **Domain packs** for your key agents (Character Consistency, Prompt Engineering for Video, Agentic Video Production, etc.)

**Success Criteria (Quality Gates)**
- Retrieval precision (relevant files returned in top results): ≥ 88% (critic or human eval)
- Routing decision quality (downstream agent success improvement): measurable lift
- Latency: < 4s p95 for standard queries; < 8s for complex pipeline queries
- Explainability: 100% of decisions produce human-readable + structured trace
- Continuous improvement: Routing accuracy improves over time via critic feedback and performance signals
- Cost efficiency: Avoids over-retrieval; supports cost-aware routing

```
Requesting Agent (e.g. Character Consistency Critic)
          ↓ (structured request)
Knowledge Router Agent
   ├── 1. Query Analyzer + Intent Classifier (with reflection)
   ├── 2. Planner (for complex/multi-hop pipeline queries)
   ├── 3. Hybrid Retrieval Engine
   │     ├── 3.1 Metadata Hard Filters (deterministic, fast)
   │     ├── 3.2 Cluster/Centroid Semantic Retriever (RopMura-inspired)
   │     ├── 3.3 Graph Explorer (AgentRouter-inspired heterogeneous GNN or lightweight traversal)
   │     └── 3.4 LLM Ranker + Reflection (Self-RAG style)
   ├── 4. Context Assembler (raw chunks / synthesized pack / structured knowledge)
   ├── 5. Explainer (full reasoning trace)
   └── 6. Multi-Level Critic (evaluates routing + retrieval + downstream utility)
          ↓
Knowledge Base (5,000+ .md files)
   ├── Rich YAML Frontmatter (agent_relevance, tags, category, quality_score, etc.)
   ├── Vector Store (embeddings + metadata filtering)
   ├── Knowledge Graph (nodes: techniques, tools, failure_modes, papers, agents; relations: improves, requires, common_failure, used_with)
   └── Optional Pre-computed Centroids per Domain/Agent Cluster
```

**Key Design Principles**
- **Metadata First**: Hard constraints eliminate 70-80% of irrelevant files instantly.
- **Graph-Guided Intelligence**: Relationships between concepts (e.g., “character consistency techniques improve multi-shot narrative in Seedance”) enable smarter routing.
- **Iterative Refinement**: For complex queries (full AI video production pipeline), Planner + iterative evaluation/simplification (RopMura style).
- **Self-Reflection**: The Router itself uses reflection tokens / critic steps (Self-RAG inspired) to judge its own retrieval quality before finalizing output.
- **Generalized + Extensible**: Core logic is domain-agnostic; domain packs and agent_relevance tags make it powerful for your AI Filmmaking + AI Agents corpus.

### Input from Requesting Agent
```json
{
  "request_id": "uuid-v4",
  "timestamp": "2026-06-06T15:02:00Z",
  "requesting_agent": "character_consistency_critic_v3",
  "task_description": "Ensure face, clothing, and prop consistency across 12 shots in a cinematic wuxia fight scene using Seedance + Kling hybrid workflow",
  "required_concepts": ["character_consistency", "multi_shot", "reference_sheets", "seedance", "kling", "failure_modes_consistency", "clothing_drift"],
  "constraints": {
    "max_files": 15,
    "max_tokens": 12000,
    "prefer_recent": true,
    "min_quality_score": 7.5,
    "exclude_tags": ["2025_outdated"]
  },
  "context": {
    "previous_failures": ["face morphing in shot 7-9", "clothing color shift under dramatic lighting"],
    "style": "cinematic wuxia, high contrast lighting, dynamic camera",
    "downstream_goal": "produce 12 consistent shots + editing notes"
  },
  "routing_hints": {
    "complexity": "high",           // low | medium | high | pipeline
    "needs_graph": true,
    "multi_hop_expected": true
  }
}
```

### Output from Router
```json
{
  "request_id": "...",
  "selected_knowledge": [
    {
      "file_id": "ai_filmmaking/consistency/character_reference_sheets_seedance_2026.md",
      "title": "Character Reference Sheets & Multi-Shot Consistency in Seedance 2.0",
      "relevance_score": 0.96,
      "match_reason": "Directly addresses clothing drift under dramatic lighting + multi-shot face consistency techniques proven with Seedance + Kling hybrid",
      "key_excerpts": ["Use detailed character bible images as first-frame reference...", "Failure mode: Clothing color shifts when lighting changes > 30% — mitigate with..."],
      "tags_matched": ["character_consistency", "multi_shot", "seedance", "failure_modes"],
      "agent_relevance_match": ["character_consistency_critic"]
    }
  ],
  "context_pack": {
    "type": "structured_knowledge_pack",
    "summary": "Key principles for character consistency in 2026 tools...",
    "structured_sections": {
      "best_practices": [...],
      "failure_modes_and_mitigations": [...],
      "tool_specific_notes": {"seedance": "...", "kling": "..."}
    }
  },
  "reasoning_trace": {
    "step_1": "Applied hard metadata filters: category=ai_filmmaking, tags contain character_consistency + multi_shot, quality >=7.5 → reduced to 47 candidates",
    "step_2": "Cluster/centroid semantic match on task_description → top clusters: consistency_systems, seedance_workflows",
    "step_3": "Graph traversal: 'character_consistency' → 'improves' → 'multi_shot_narrative' + 'failure_mode:clothing_drift' nodes → pulled 3 related technique files",
    "step_4": "LLM Ranker with reflection: Scored 12 files. Critic flagged 2 as partially relevant (lower lighting coverage). Final selection: 9 files.",
    "why_these_over_others": "Prioritized files with explicit failure mode coverage matching your previous_failures context."
  },
  "critic_evaluation": {
    "retrieval_quality": 0.93,
    "routing_confidence": 0.91,
    "expected_downstream_utility": "high",
    "suggested_improvements": ["Add more dynamic lighting failure examples", "Create dedicated 'wuxia_consistency' tag"]
  },
  "suggested_next_actions": ["Request deeper graph traversal on 'prop_consistency'", "Flag file X for quality review"]
}
```

4. **LLM Ranker + Reflection** (Self-RAG / CRAG inspired)
   - Scores candidates on relevance to task + previous_failures + constraints.
   - Reflection step: “Are these passages actually useful for the downstream agent’s goal?” “Is anything critical missing?”
   - Can trigger corrective re-retrieval if quality low.

### 4.4 Context Assembler
- Options: raw top chunks | synthesized summary | structured knowledge pack (best for your critic-heavy agents).
- For creative agents: often returns “Knowledge Pack” with sections like Best Practices, Failure Modes & Mitigations, Tool-Specific Notes, Prompt Templates.

### 4.5 Explainer & Traceability
Every output includes a clear `reasoning_trace` (structured + natural language). This is non-negotiable for debugging and critic loops.

### 4.6 Multi-Level Critic (Self-Improving Core)
Three levels:
1. **Retrieval Critic**: Scores relevance, coverage of required_concepts, handling of previous_failures.
2. **Routing Critic**: Judges whether the right files were chosen vs alternatives; suggests better tags or graph edges.
3. **Downstream Utility Critic**: (Ideal) Observes or gets feedback from the requesting agent after it uses the context (“Did this knowledge help you succeed? What was missing?”). Feeds back as soft supervision signal (like AgentRouter’s F1-based training targets).

### Use Case 1: Character Consistency Critic Agent
**Request Example**: See Input contract above (wuxia fight scene).

**Router Behavior**:
- Hard filter: `tags CONTAIN character_consistency AND multi_shot`
- Graph: Pulls “clothing_drift” failure mode nodes + mitigation techniques
- Returns structured pack: “Best reference sheet practices for Seedance + Kling”, “Lighting-induced color shift mitigations”, “Multi-shot coherence checklist”
- Critic checks coverage of “previous_failures”

```yaml
---
title: "..."
category: ai_filmmaking | ai_agents | intersection_agentic_filmmaking
subcategory: consistency_systems | prompt_engineering_video | multi_agent_orchestration | ...
tags: [character_consistency, multi_shot, seedance, failure_modes, ...]
agent_relevance: [character_consistency_critic, video_prompt_optimizer, shot_planning_agent, ...]
domain: creative_video | agent_engineering | both
quality_score: 8.7          # human or critic rated
source_type: youtube | book | course | synthetic | research_paper
date_added: 2026-05-20
last_reviewed: 2026-06-01
---
```

**Phase 1 (MVP – 7–14 days)**
- Metadata hard filters + basic vector search
- Simple Query Analyzer
- Basic Context Assembler + Explainer
- Manual / lightweight critic feedback loop
- Bootstrap with your existing top 500–1000 high-quality files

**Phase 2 (Production Core)**
- Add Cluster/Centroid layer (RopMura style)
- Lightweight Graph Explorer (traversal first, small GNN later)
- Planner for pipeline queries
- Structured Knowledge Pack output
- Automated Critic (levels 1–2)

**Phase 3 (Learning System)**
- Performance signal feedback loop (downstream agent success → soft labels)
- Optional small RouterGNN (AgentRouter style) trained on your data
- Proactive suggestions / push mode
- Full self-improvement via critic + usage analytics

**Phase 4 (Advanced)**
- Cost/latency-aware routing
- Multi-modal support (if you add image/video references to knowledge base)
- Integration with your full N1ch01as Architect harness + main Critic Agent

- **Offline**: Golden test set of 50–100 representative queries per major agent role. Measure precision@K, recall of required_concepts, critic scores.
- **Online**: Track downstream agent success rate before/after Router improvements. Log critic scores and human spot-checks.
- **Ablation**: Test impact of each layer (metadata only vs +graph vs +reflection).
- **Continuous**: Router critic proposes improvements to the knowledge base itself (new tags, missing content detection).

- **Very broad query** → Planner forces decomposition + strict max_files.
- **No good matches** → Router returns “Insufficient high-quality knowledge” + suggestions to expand corpus + low confidence flag.
- **Conflicting information** across files → Graph + Critic prioritize higher quality_score + more recent + explicit failure mode coverage.
- **New agent role appears** → Easy extension: add to `agent_relevance` tags; Router gradually learns via feedback.
- **Latency spikes on complex queries** → Planner has round limits; fallback to simpler retrieval.

- **Orchestration**: LangGraph or your custom harness (excellent for stateful Planner + Router + Critic loops)
- **Vector + Metadata**: LlamaIndex or Haystack with Qdrant/Pinecone (strong metadata filtering)

…



### From `corpus/root/agent_loop_creator_v1.md` Copy: `sources/excerpts/agent_loop_creator_v1.md`.


**Rethink Summary (100x Internal Iteration):**  
- **Core Insight from Research**: ~42% of MAS failures are **specification & design issues** (MASFT); verification/termination another ~21%. Adding agents without strong Phase 0 spec validation, structured observations, explicit `Done` + multi-level critics, and progress tracking often yields diminishing/negative returns. Hierarchical + TEA-style versioning/self-evolution delivers outsized gains on long-horizon tasks (AgentOrchestra 89%+ GAIA).  
- **xAI Alignment**: Use `grok-4.20-multi-agent` (4/16 agents, leader synthesis, server-side ReAct with hidden sub-states) for research sub-tasks; emulate Grok Build patterns (explicit plan generation first, parallel isolated sub-agents, todo-style state) in client loop. Hybrid maximizes power + control + cost efficiency.  
- **Architectural Tradeoffs Resolved**: Custom Python core (Pydantic schemas, strict JSON mode, full tracer) over pure LangGraph for transparency, auditability, and education value (user's harness style). Hybrid memory (structured `todo.md` + vector long-term + aggressive summarization) per TEA/MemGPT. Bounded self-evolution (TextGrad-inspired + validation on held-out traces) to prevent drift. Minimal deps first; optional adapters later. Local-first, observable, sandboxed, production-hardened (circuit breakers, retries, budgets). Dogfood: This harness should help build/improve itself.  
- **Failure Mode Coverage**: Every MASFT mode explicitly mapped to mitigations in specific phases/components (see Section 3).  
- **Phased Build**: MVP (reliable flat ReAct) → Hierarchical delegation + consolidation → TEA versioning/evolution → xAI hybrid + examples. Each phase has clear deliverables, code skeletons, and verification gates (critic checkpoints).  
- **Target Outcomes**: >85% success on complex research/coding benchmarks via evolution; <5% residual MASFT failure modes in controlled tests; full replay/debug from traces; seamless integration with user's Python/Node/xAI/DeepSeek/Cursor/Kiro/OpenWebUI stack.

This is **spec-driven, critic-ready input**. Coding agent: Parse sections, generate code module-by-module, run internal critic/refinement loops on outputs, validate against success criteria before proceeding. Use `task.md` / `todo.md` style internally during build.

### Primary Objective
Implement a **controlled, hierarchical, ReAct-inspired agent loop system** that is:
- Reliable against known MAS failure modes (MASFT taxonomy).
- Evolvable via TEA-inspired versioning, tracing, and self-reflection/TextGrad-style optimization.
- Hybrid: Client-side full control + optional delegation to xAI server-side multi-agent for deep research.
- Production-grade: Observable, cost-aware, secure (sandboxed), testable, extensible.
- Aligned with user's preferences: Spec-driven (living `TaskSpec`), iterative refinement/critic loops, harness engineering, local/minimal-Docker, Python-first with Pydantic/JSON contracts, integration points for existing tools (xAI API, DeepSeek, Cursor/Kiro, self-hosted services).

**Key Findings & Mitigations Integrated**:
- Design/spec quality is #1 ROI. **Phase 0 mandatory**: Structured `TaskSpec` (Pydantic) with explicit objective, success_criteria list, constraints (max_steps, budgets), output_format, quality_gates. Automated spec validator + critic before loop start. Role contracts in delegation.
- Verification is weak spot even in "successful" runs. **Phase 3 + 5**: Dedicated Verifier/Critic agent (strict JSON: passes, score, issues, suggestions, confidence). Multi-level (low-level schema + high-level objective alignment). Explicit `Done` action that **must** pass verifier + evidence check. Progress tracking (% todo complete + criteria alignment in Thought step).
- Context/history loss & repetition common. **Phase 1**: Aggressive summarization on context > threshold, structured state (`task.md` / `todo.md` + key_facts only, not full history dump), cycle detection via recent action+obs hash (md5), `max_steps` hard cap + progress-based early exit.
- Inter-agent issues: Strong central Orchestrator with explicit decomposition/routing/contracts + structured handoff Observation schema (status, data, summary, confidence, issues, next_suggestions, provenance, trace_id). Circuit breakers per tool/role. Versioned shared state.
- Interventions in paper (+9-15% gains): Better prompts/roles/topology + verification sections. Our system goes further with **runtime gates + evolution**.

### 2.3 ReAct Foundations + Enhancements
- **ReAct (Yao et al. ICLR 2023)**: Thought (reasoning trace) → Action (tool/delegate/finish) → Observation (grounded result) loop. 10-34% gains on interactive tasks vs pure CoT or acting. Our core: Strict structured decision output (Pydantic: thought, action_type, payload), structured Observation always.
- **Enhancements Incorporated**:
  - **Reflexion** (Shinn et al.): Verbal self-critique on trajectories → improvement plans. Used in light reflection (every N steps) + full Phase 4.
  - **Prospector** (Kim et al.): Self-Asking + Trajectory Ranking. Optional: Generate multiple candidate trajectories, rank via critic, pick best.
  - **ReflAct** (recent): Strengthens grounding **in the reasoning step itself** (retouches reasoning with world feedback). Enhance Thought prompt to explicitly re-ground vs previous obs + original objective.
  - **Plan-and-Execute + LATS/MetaGPT patterns**: Explicit high-level plan phase (Phase 0 optional) before loop; tree search elements via multiple parallel sub-branches (optional in hierarchical).
- **xAI Production Patterns**: Server-side ReAct loop (model decides tools → executes internally → iterates until final). Multi-agent: realtime parallel specialists + leader synthesis (4 or 16 agents controlled by `reasoning.effort`). Grok Build: Plan-first, parallel sub-agents (isolated contexts/worktrees), structured workflow, ACP support for custom orchestration. **Our Hybrid**: Client orchestrator maintains global state/trace/verifier; delegates research sub-problems to xAI multi-agent (narrow spec, receive synthesized + citations); for coding sub-tasks, use local specialists or emulate parallel in isolated Python processes/threads with copied state slices.

**Rationale Summary**: This design directly attacks the #1 failure category (spec/design) via Phase 0 + living TaskSpec + critic. Closes verification gaps with mandatory gates + structured obs. Prevents loops/context rot with detection + summarization + structured state (todo.md pattern user prefers). Enables long-term robustness via TEA self-evolution. Leverages xAI strengths without ceding control. Matches user's iterative, spec-driven, production harness philosophy.

### 3.1 High-Level Flow (Phases from agent_loop.md, Hardened)
1. **Phase 0: Initialization**
   - Parse instruction → generate/validate `TaskSpec` (Pydantic: objective, success_criteria: List[str], constraints: Dict, output_format, max_steps=50, token_budget=200k, quality_gates, initial_plan?).
   - Spec Validator + Critic (LLM): Check completeness, ambiguity, role clarity, termination conditions. Reject/revise if FM-1.x risks high.
   - Create `AgentState`: task_spec, todo (from plan or empty), memory, tracer, version_registry, budgets, seen_hashes=set().
   - Optional: Planner LLM generates high-level plan (numbered steps + deps) + todo.md content. Validate plan vs spec.
   - Decide architecture: flat | hierarchical | hybrid_xai.

4. **Phase 3: Consolidation & Quality Gates**
   - Aggregator collects observations + plan progress.
   - Harmonizer/Reporter LLM: Merge, dedup, cross-reference, resolve conflicts (cite sources/versions), produce unified draft.
   - Verifier/Critic: Score vs success_criteria, check hallucinations/gaps/FM-3.x issues, suggest fixes. JSON output.
   - If fail gate: Trigger refinement (re-plan specific branch, re-delegate, or self-edit).
   - If pass: Proceed to polish or final.

### 3.3 Key Modules to Implement (with Skeletons from attached + Enhancements)
- **core/loop.py**: `controlled_react_loop` (enhance attached code with Pydantic, full state, MASFT-aware prompts, xAI hybrid hooks, progress tracking).
- **reliability/circuit_breaker.py**: Enhanced class with metrics, per-tool/role instances, integration with safe_execute.
- **reliability/verifier.py**: `verify_output` + `VERIFIER_PROMPT` tuned to catch FM-1.x/2.x/3.x (e.g., "Does this respect original task_spec and roles? Any premature termination or incomplete verification? Cross-check claims vs observations.").
- **hierarchical/orchestrator.py**: Planner logic, delegation router, sub-agent factory, consolidator.
- **evolution/self_evolver.py**: `self_evolve_component` (TextGrad-style: diagnose from trace, propose_edit, validate_improvement, VersionManager.register).
- **tea/protocol.py**: Minimal TCP/ECP/ACP schemas, register_tool/register_agent, get_context_slice, VersionManager.
- **integrations/xai.py**: `call_grok_multi_agent(sub_spec, tools_enabled, context_slice)` → parse leader result into StructuredObservation.
- **memory/ & tracing/**: As described.
- **prompts/**: Versioned JSON/YAML or .md files for system prompts, few-shots (ReAct decision, verifier, planner, reflector, sub-roles). Include MASFT failure mode references in critic prompts.

**Coding Agent Workflow During Build**: After each phase/module, generate code → run internal critic (use verifier logic or separate reflection prompt) → fix issues → re-validate against gate criteria → proceed. Maintain `build_task.md` / `todo.md` internally. Log all to tracer for later self-evolution of the builder itself.

## 6. Testing & Validation Strategy (Critical for Coding Agent)

**Recommended First Prompt to Coding Agent (copy-paste)**:
"Read `agent_loop_creator.md` and `agent_loop.md` fully. Create the `agent_loop/` Python package scaffold with pyproject.toml, core Pydantic models (TaskSpec, StructuredObservation, etc.), basic LLM client, and a minimal working controlled ReAct loop that passes the Phase 0/1 verification gates. Use strict JSON schemas. Include initial failure_injection test skeleton for MASFT modes. Maintain todo.md during your work and apply critic/refinement to every generated module."

**Questions for Clarification (if needed before coding)**: None anticipated — spec is self-contained. If ambiguities arise during build, resolve via internal critic or escalate with specific trace.

This completes the deep research + implementation spec. Build it production-grade, iterate with critics, and make it a cornerstone of advanced agent harnesses.



### From `corpus/root/agent_loop_creator_v2.md` Copy: `sources/excerpts/agent_loop_creator_v2.md`.


**Key v2 Additions (from agent_loop_v3.md Section 1.4)**: Explicit Cynefin context classification for adaptive Fast vs Full loop routing; mandatory Premortem in Phase 0; RPD + Dual Process + Metacognition for Fast Recognition Path in Phase 1; structured AAR + Double-Loop + 5 Whys/Fishbone + multi-perspective critics (Paul-Elder/Red Team/Six Hats) in Phase 4 reflection/self-evolution. All original v1 details, skeletons, MASFT mappings, and phased roadmap preserved and extended.

**Rethink Summary (100x Internal Iteration + Cognitive Layer):**  
- **Core Insight from Research**: ~42% of MAS failures are **specification & design issues** (MASFT); verification/termination another ~21%. Adding agents without strong Phase 0 spec validation, structured observations, explicit `Done` + multi-level critics, and progress tracking often yields diminishing/negative returns. Hierarchical + TEA-style versioning/self-evolution delivers outsized gains on long-horizon tasks (AgentOrchestra 89%+ GAIA). **v2 addition**: Human cognitive frameworks (top-ranked in thinking_model.md) provide the highest-leverage missing layer for adaptive intelligence, proactive risk handling, fast/slow deliberation, and multi-level learning — directly mapped in agent_loop_v3.md Section 1.4.  
- **xAI Alignment**: Use `grok-4.20-multi-agent` (4/16 agents, leader synthesis, server-side ReAct with hidden sub-states) for research sub-tasks; emulate Grok Build patterns (explicit plan generation first, parallel isolated sub-agents, todo-style state) in client loop. Hybrid maximizes power + control + cost efficiency. Cognitive routing (Cynefin) helps decide when to delegate vs local fast path.  
- **Architectural Tradeoffs Resolved**: Custom Python core (Pydantic schemas, strict JSON mode, full tracer) over pure LangGraph for transparency, auditability, and education value (user's harness style). Hybrid memory (structured `todo.md` + vector long-term + aggressive summarization + **Pattern Store for RPD**) per TEA/MemGPT. Bounded self-evolution (TextGrad-inspired + validation on held-out traces + **AAR/Double-Loop structure**) to prevent drift. **Cognitive config** (enable_fast_path, reflection_style, critic_modes) per TaskSpec for adaptability without complexity explosion on simple tasks. Minimal deps first; optional adapters later. Local-first, observable, sandboxed, production-hardened (circuit breakers, retries, budgets). Dogfood: This harness should help build/improve itself (including its own cognitive components).  
- **Failure Mode Coverage**: Every MASFT mode explicitly mapped to mitigations in specific phases/components (see Section 3) **+ cognitive mitigations** (e.g., Premortem for spec/design risks, Metacognition + cycle detection for repetition, AAR/Double-Loop for verification/termination gaps, RPD for context/history issues via pattern matching).  
- **Phased Build**: MVP (reliable flat ReAct) → Controlled core with cognitive mode selection (Fast Recognition Path) → Hierarchical delegation + consolidation → TEA versioning/evolution + full AAR/Double-Loop/5Whys critics → xAI hybrid + examples. Each phase has clear deliverables, code skeletons, and verification gates (critic checkpoints).  
- **Target Outcomes**: >85% success on complex research/coding benchmarks via evolution; <5% residual MASFT failure modes in controlled tests; **cognitive features validated** (Cynefin classification accuracy, Premortem risk coverage, RPD hit rate on repeated tasks, AAR structure compliance, Double-Loop assumption questioning); full replay/debug from traces; seamless integration with user's Python/Node/xAI/DeepSeek/Cursor/Kiro/OpenWebUI stack.

This is **spec-driven, critic-ready input**. Coding agent: Parse sections, generate code module-by-module, run internal critic/refinement loops on outputs, validate against success criteria before proceeding. Use `task.md` / `todo.md` style internally during build.

### Primary Objective
Implement a **controlled, hierarchical, ReAct-inspired agent loop system (v3 Cognitive-Enhanced)** that is:
- Reliable against known MAS failure modes (MASFT taxonomy) **and enhanced with human cognitive best practices** (adaptive context routing via Cynefin, proactive risk via Premortem, fast expert intuition via RPD + Dual Process, structured multi-level reflection via AAR + Double-Loop + 5 Whys, multi-perspective critique via Paul-Elder/Red Team).
- Evolvable via TEA-inspired versioning, tracing, and self-reflection/TextGrad-style optimization **structured as AAR + Double-Loop**.
- Hybrid: Client-side full control + optional delegation to xAI server-side multi-agent for deep research **with cognitive mode selection** (Fast Recognition Path for routine sub-tasks vs Full deliberative for complex).
- Production-grade: Observable, cost-aware, secure (sandboxed), testable, extensible, **with configurable cognitive_profile** (enable_fast_path, reflection_style="aar_double_loop_5whys", critic_modes=["red_team", "paul_elder"]).
- Aligned with user's preferences: Spec-driven (living `TaskSpec` with cognitive_profile), iterative refinement/critic loops, harness engineering, local/minimal-Docker, Python-first with Pydantic/JSON contracts, integration points for existing tools (xAI API, DeepSeek, Cursor/Kiro, self-hosted services). **Dogfood cognitive improvements on its own prompts/verifier during Phase 4**.

**v2 Cognitive Success Criteria (Additional)**:
9. **Adaptive Routing (Cynefin + RPD + Dual Process)**: On mixed-complexity task suites, correctly classifies context (Simple/Complicated/Complex/Chaotic) with ≥85% agreement vs human baseline or held-out labels; Fast Recognition Path triggers on ≥70% of repeated/routine sub-tasks with pattern match (measured by RPD similarity + outcome quality); overall token reduction ≥20-30% vs always-full baseline without quality loss on simple cases.
10. **Proactive Risk (Premortem)**: In Phase 0, Premortem step identifies ≥3-5 plausible failure modes per complex task and incorporates mitigations into spec/todo/quality_gates; demonstrable reduction in downstream FM-1.x/3.x issues in failure-injection tests.
11. **Structured Reflection & Deep Learning (AAR + Double-Loop + 5 Whys)**: Phase 4 reflections produce complete AAR artifacts (4 questions answered with evidence); Double-Loop questions governing variables and proposes meta-changes (e.g., prompt/schema evolution) that pass validation in ≥60% of bounded rounds; 5 Whys + Fishbone categorization used on ≥80% of diagnosed failures with actionable root causes.
12. **Multi-Perspective Critique (Paul-Elder / Red Team / Six Hats)**: Verifier supports critic_modes; ensemble or red_team/paul_elder modes catch ≥15% more issues (esp. assumption, bias, edge-case) than standard mode alone on held-out bad outputs; Six Hats or equivalent used in creative/harmonization steps when configured.

**Key Findings & Mitigations Integrated**:
- Design/spec quality is #1 ROI. **Phase 0 mandatory**: Structured `TaskSpec` (Pydantic) with explicit objective, success_criteria list, constraints (max_steps, budgets), output_format, quality_gates. Automated spec validator + critic before loop start. Role contracts in delegation.
- Verification is weak spot even in "successful" runs. **Phase 3 + 5**: Dedicated Verifier/Critic agent (strict JSON: passes, score, issues, suggestions, confidence). Multi-level (low-level schema + high-level objective alignment). Explicit `Done` action that **must** pass verifier + evidence check. Progress tracking (% todo complete + criteria alignment in Thought step).
- Context/history loss & repetition common. **Phase 1**: Aggressive summarization on context > threshold, structured state (`task.md` / `todo.md` + key_facts only, not full history dump), cycle detection via recent action+obs hash (md5), `max_steps` hard cap + progress-based early exit.
- Inter-agent issues: Strong central Orchestrator with explicit decomposition/routing/contracts + structured handoff Observation schema (status, data, summary, confidence, issues, next_suggestions, provenance, trace_id). Circuit breakers per tool/role. Versioned shared state.
- Interventions in paper (+9-15% gains): Better prompts/roles/topology + verification sections. Our system goes further with **runtime gates + evolution**.

### 2.3 ReAct Foundations + Enhancements
- **ReAct (Yao et al. ICLR 2023)**: Thought (reasoning trace) → Action (tool/delegate/finish) → Observation (grounded result) loop. 10-34% gains on interactive tasks vs pure CoT or acting. Our core: Strict structured decision output (Pydantic: thought, action_type, payload), structured Observation always.
- **Enhancements Incorporated**:
  - **Reflexion** (Shinn et al.): Verbal self-critique on trajectories → improvement plans. Used in light reflection (every N steps) + full Phase 4.
  - **Prospector** (Kim et al.): Self-Asking + Trajectory Ranking. Optional: Generate multiple candidate trajectories, rank via critic, pick best.
  - **ReflAct** (recent): Strengthens grounding **in the reasoning step itself** (retouches reasoning with world feedback). Enhance Thought prompt to explicitly re-ground vs previous obs + original objective.
  - **Plan-and-Execute + LATS/MetaGPT patterns**: Explicit high-level plan phase (Phase 0 optional) before loop; tree search elements via multiple parallel sub-branches (optional in hierarchical).
- **xAI Production Patterns**: Server-side ReAct loop (model decides tools → executes internally → iterates until final). Multi-agent: realtime parallel specialists + leader synthesis (4 or 16 agents controlled by `reasoning.effort`). Grok Build: Plan-first, parallel sub-agents (isolated contexts/worktrees), structured workflow, ACP support for custom orchestration. **Our Hybrid**: Client orchestrator maintains global state/trace/verifier; delegates research sub-problems to xAI multi-agent (narrow spec, receive synthesized + citations); for coding sub-tasks, use local specialists or emulate parallel in isolated Python processes/threads with copied state slices.

**Rationale Summary**: This design directly attacks the #1 failure category (spec/design) via Phase 0 + living TaskSpec + critic. Closes verification gaps with mandatory gates + structured obs. Prevents loops/context rot with detection + summarization + structured state (todo.md pattern user prefers). Enables long-term robustness via TEA self-evolution. Leverages xAI strengths without ceding control. Matches user's iterative, spec-driven, production harness philosophy.

### 3.1 High-Level Flow (Phases from agent_loop_v3.md, Hardened with Cognitive Layer)
1. **Phase 0: Initialization (Spec-Driven + Cognitive Setup)**
   - Parse instruction → generate/validate `TaskSpec` (Pydantic: objective, success_criteria: List[str], constraints: Dict, output_format, max_steps=50, token_budget=200k, quality_gates, initial_plan?, **cognitive_profile: Dict** e.g. {"enable_fast_path": true, "reflection_style": "aar_double_loop_5whys", "critic_modes": ["red_team", "paul_elder"], "cynefin_classification": "auto"}).
   - Spec Validator + Critic (LLM): Check completeness, ambiguity, role clarity, termination conditions. Reject/revise if FM-1.x risks high. **Run Premortem Analysis**: "Assume this spec/plan fails spectacularly — identify top causes and mitigations; merge into living spec, success_criteria, todo, and quality_gates."
   - **Cynefin Classification** (context-aware routing): Tag task context (Simple/Complicated/Complex/Chaotic) based on cause-effect clarity, expertise needed, emergence, or crisis. Store in task_spec and use to auto-configure loop params (Fast path preference for Simple/Complicated; Full + heavy reflection for Complex/Chaotic).
   - Create `AgentState`: task_spec (with cognitive_profile + cynefin_tag), todo (from plan or empty), memory (incl. Pattern Store for RPD), tracer, version_registry, budgets, seen_hashes=set(), **current_mode: "fast" | "full"**.
   - Optional: Planner LLM generates high-level plan (numbered
…



### From `corpus/root/project_starter_0.1.md` Copy: `sources/excerpts/project_starter_0.1.md`.


**Context & Principles**  
- **Spec-Driven Development (SDD)** first: Clear specs drive everything.  
- Prioritize **highest-ranked** items on feature/skill/rule overlap (ECC #1 > Karpathy rules #2 > claude-mem #3 > shanraisshan best-practice #4 > antigravity-awesome-skills #5, etc.).  
- Keep it **portable, minimal-Docker where possible, local-first**, with excellent security, memory, and token efficiency.  
- Output must be **agent-friendly**: clear phases, checklists, acceptance criteria, and hooks for critic/review agents.  
- Support iterative refinement (plan → implement → review → improve loops).  
- Target users: Solo developers, small teams, or power users building custom AI coding workflows (aligns with harness engineering + N1ch01as-style meta-systems).

## Self-Evaluation & Critic Routine (Agent Self-Quality Assessment) — Research-Enhanced

This section is significantly strengthened based on deep research from xAI (Grok multi-agent capabilities, Grok Build agentic coding focus, transparent/auditable reasoning) and high-quality 2025–2026 research (Reflexion, Self-Refine, SAGE multi-agent self-evolution, SCALAR Structured Critic–Actor Loop, human-in-the-loop self-improvement frameworks, context folding/memory architectures).

**Research-Backed Design Principles**
- **Multi-agent critic patterns** (xAI Grok Multi-Agent + SAGE): Use specialized roles (Actor/Solver + Critic/Challenger + optional Judge) that can work in parallel. Each sub-agent shows its reasoning for full auditability and transparency.
- **Structured self-critique** (SCALAR, Reflexion, Self-Refine): Move beyond vague feedback. Use explicit verification of preconditions, state tracking, rubric scoring, and episodic memory of past reflections/critiques.
- **Human-in-the-loop safety** (strong research consensus): All high-impact changes require human confirmation. Optional human guidance when domain knowledge evolves rapidly.
- **Memory & context management**: Support hierarchical summaries, reflection storage, and context folding for long-horizon tasks (enhancing claude-mem with ideas from AgentFold / Recursive Language Models research).
- **Transparency & auditability** (core xAI philosophy): Every sub-agent reasoning step, critique, and decision is logged and reviewable.
- **ECC-first + Research layer**: Start with ECC’s existing review/critique capabilities as the foundation, then layer on stronger multi-agent critic loops and structured reflection.

**Core Routine Flow** (Actor → Multi-Agent Critic → Refine + Memory loop)
- **Actor/Solver**: Generates the implementation or solution using ECC skills + Karpathy rules.
- **Critic/Challenger** (can be multi-agent): Runs structured self-critique using the enhanced rubric. Can spawn parallel sub-agents for deeper analysis on different dimensions (e.g., one for security, one for simplicity). Produces scores + specific issues + concrete, actionable improvement suggestions.
- **Reflection Storage**: Critiques, lessons learned, and successful patterns are stored in episodic memory (build on claude-mem or add dedicated structured reflection store with hierarchical summaries).
- **Refine Loop**: Actor uses the critique + stored reflections to improve the output. Supports multiple iterations with intelligent context management.
- **Human Confirmation Gate**: High-impact suggestions (especially skill/rule changes) go through the human confirmation workflow.
- **Full Audit Log**: All reasoning traces, critiques, and decisions are recorded for transparency and later review (xAI-style auditability).

**Design (ECC-first + Extensible)**
- Central critic skill(s) in `./skills/critic/` (or reuse/extend ECC’s existing review/critique capabilities).
- Structured self-evaluation prompt/template that outputs:
  - Overall quality score (e.g., 1–10 or rubric-based)
  - Breakdown across dimensions (Correctness, Simplicity/Karpathy alignment, Spec adherence, Security, Performance, Maintainability, Token efficiency)
  - Specific issues found
  - Concrete improvement suggestions (as new tasks or diff recommendations)
- Can be triggered:
  - Automatically via post-completion hook
  - Manually with `/self-review` or `/critic` command
  - As part of multi-step workflows (after implementing a feature spec)
- Output stored alongside the work (e.g., `review.md` or appended to `task.md` / `status.md`)
- Feeds back into the loop (agent can then refine based on its own critique)

**Tasks to Implement**
1. [ ] Create or adapt a core **critic / self-review skill** in `./skills/critic/self-review.md` (start with ECC’s review capabilities as base, enhance with Karpathy + best-practice patterns).
2. [ ] Define a reusable **self-evaluation prompt template** (in `rules/` or `skills/critic/`) that agents can invoke.
3. [ ] Add a **slash command** (e.g., `/self-review` or `/critic`) in `.claude/commands/` that triggers structured self-evaluation on the current context or last changes.
4. [ ] Create a **post-completion hook** that optionally runs self-review after significant code changes or task completion.
5. [ ] Make the routine output structured data (Markdown + optional JSON) that can be parsed by other agents or scripts.
6. [ ] Integrate with existing orchestration (e.g., after dmux parallel work or feature implementation from a spec).
7. [ ] Add example usage in `docs/usage.md` and a sample `examples/self-review-workflow/`.
8. [ ] Allow customization of the rubric (e.g., project-specific weights or extra dimensions like accessibility, i18n).
9. [ ] Ensure the critic routine itself can be self-evaluated (meta level) for continuous improvement of the harness.

This builds directly on the Self-Evaluation & Critic Routine and the central `skills/` source of truth.

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

**Tasks to Implement**
1. [ ] Create a **suggestion generator skill** (or extend the critic routine) that can propose add/update/remove actions based on analysis.
2. [ ] Define a standard **suggestion format** (Markdown template with sections: Action, Skill Name, Rationale, Impact, Proposed Content/Diff, Confidence).
3. [ ] Add storage for pending suggestions (`suggestions/` folder + manifest or `pending-skill-changes.md`).
4. [ ] Create slash commands:
   - `/suggest-skills` — trigger analysis and generate new suggestions.
   - `/review-suggestions` — list pending suggestions with details.
   - `/approve-suggestion ` or `/confirm-changes` — human confirmation step.
5. [ ] Integrate with the Self-Evaluation routine so strong critiques can automatically trigger relevant suggestions.
6. [ ] After human confirmation, automatically apply the change to central `skills/` and trigger the sync layer.
7. [ ] Add logging/audit trail for all confirmed changes.
8. [ ] Document the full workflow in `docs/usage.md` with examples.
9. [ ] Make the suggestion system itself self-evaluable (meta-critic).

**Tasks**:
1. [ ] Write excellent `docs/`:
- `README.md` with quick start, architecture overview, ranking rationale.
- `installation.md` with exact commands.
- `usage.md` with example workflows (plan a feature with SDD, parallel agents via task.md, security review, etc.).
2. [ ] Add 2–3 example mini-projects or workflow demos in `examples/`.
3. [ ] Implement quality gates:
- Automated lint / security scan on changes.
- Review prompt or agent command for PRs/changes.
- Self-test script that verifies core commands work.
4. [ ] Add this `task.md` (and future task tracking) as the living spec.
5. [ ] Create critic/review agent prompt or skill for ongoing improvement of the harness itself.

**Tasks**:
1. [ ] Add self-improvement loop skill (research new skills → propose additions → critic review → merge).
2. [ ] Support easy updates from upstream (ECC, skill libraries) via scripts.
3. [ ] Include placeholders for domain-specific extensions (e.g., trading skills, frontend design, Django/TS stacks).
4. [ ] Plan for multi-agent orchestration examples using ECC's dmux + task.md pattern.

**Acceptance Criteria**:
- Clear path to evolve the starter without breaking existing setups.
- Supports your preferred iterative refinement + critic agent workflow.

- **Always start with planning/spec phase** (use ECC planning skills or new SDD skills).
- **Use high-ranking source first** on any overlap.
- **Generate task.md / status.md** for complex sub-tasks (following ECC dmux pattern).
- **Run critic/review** after major phases.
- **Track cost/token usage** throughout.
- **Security scan** before any merge or publish.
- **Document decisions** in `docs/decisions.md`.

This task.md itself serves as the living **spec** for the project. Update it as we progress (or let a critic agent propose improvements).



### From `corpus/root/project_starter_0.2.md` Copy: `sources/excerpts/project_starter_0.2.md`.


- [ ] New repo: `project_starter`.  
- [ ] One main CLI: `node scripts/project-starter.mjs`.  
- [ ] NPM scripts:  
  - `npm run init`  
  - `npm run sync`  
  - `npm run sync:check`  
  - `npm run doctor`  
  - `npm run security`  
  - `npm run review`  
  - `npm run test`  
  - `npm run format`  
- [ ] ECC-based starter profile.  
- [ ] Cross-agent sync engine.  
- [ ] Curated skills/rules/hooks/MCP manifests.  
- [ ] Claude Code, Cursor, Codex, OpenCode, Gemini CLI, Grok Build adapters.  
- [ ] Optional GitHub Copilot, Zed, and Windsurf adapters.  
- [ ] Self-review/critic routine.  
- [ ] Skill lifecycle proposal/approval workflow.  
- [ ] Security baseline with AgentShield or equivalent.  
- [ ] Docs, examples, tests, and acceptance checks.

- [ ] Planning / SDD  
- [ ] Implementation  
- [ ] TDD / testing  
- [ ] Code review  
- [ ] Security review  
- [ ] Debugging  
- [ ] Refactoring  
- [ ] Documentation  
- [ ] Memory / handoff  
- [ ] Context compaction  
- [ ] Cross-agent sync  
- [ ] Self-review / critic  
- [ ] Skill suggestion lifecycle

## 13. Phase 7 — Self-Evaluation and Critic Routine

- **Actor/Solver:** Implements the task.  
- **Critic:** Reviews correctness, simplicity, spec adherence, security, performance, maintainability.  
- **Security Critic:** Optional focused security pass.  
- **Test Critic:** Optional test and verification pass.  
- **Judge:** Summarizes blocking vs non-blocking findings.

- [ ] Claude skill/command: `/self-review`  
- [ ] Claude skill/command: `/critic`  
- [ ] CLI: `npm run review`  
- [ ] Optional hook: post-task self-review

- [ ] `npm run security` runs locally.  
- [ ] Critical findings fail CI.  
- [ ] Sensitive files are protected.  
- [ ] Security docs explain the model.

- [ ] `npm run init` creates a working starter.  
- [ ] `npm run sync` updates all supported agent configs.  
- [ ] Claude Code, Cursor, and at least one of Codex/Gemini/OpenCode are verified.  
- [ ] ECC foundation is installed/adapted and documented.  
- [ ] Karpathy behavior rules are active.  
- [ ] Self-review workflow works.  
- [ ] Skill suggestions require human approval.  
- [ ] Security scan works and blocks critical issues.  
- [ ] Docs are sufficient for a new user.  
- [ ] All generated files are reproducible.  
- [ ] Source audit and decisions are complete.  
- [ ] All project names, docs, generated headers, scripts, and examples consistently use `project_starter`.

1. **Foundation:** repo, CLI, manifests, docs skeleton.  
2. **Sync:** central source → Claude/Cursor/Codex.  
3. **ECC:** install/adapt core.  
4. **Rules:** constitution + Karpathy + SDD.  
5. **Skills:** curated core.  
6. **Security:** AgentShield + secret protections.  
7. **Memory:** handoff + reflection.  
8. **Critic:** self-review workflow.  
9. **Lifecycle:** suggestions + human approval.  
10. **Polish:** examples, CI, docs.



### From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 53 | **OrchestratorAgent** | Runs CrewAI/AutoGen/LangGraph DAG; retries, timeouts, fan-out/fan-in | LangGraph + CrewAI + AutoGen patterns; Airflow/Temporal; PGA schedule templates | DAG completion ≥99.5%; SLA adherence; deadlock = 0 | Lower TTD than human EP at same scope | ProducerAgent (scope), JudgeAgent (dispute), HiTL on stall | All agents (resource burn, retry storms) | LangGraph state machine; Temporal workflow engine; Redis (distributed locks); observability (LangSmith) | Agentic Graph (LangGraph) — deterministic DAG execution |
| 54 | **PlannerAgent** | Decomposes brief into phased DAG with assignments + critic gates | PMBOK; CrewAI task graphs; phase templates | Plan validity (no missing gate); cost variance <10% | Tighter, cheaper plans than EP first pass (blind A/B) | ProducerAgent, FinanceAgent (budget) | RouterAgent (wrong pick), OrchestratorAgent | LangGraph plan-gen; cost-estimation models; Gantt/PERT tools | ReAct (decompose → estimate → validate → emit DAG) |
| 55 | **RouterAgent** | Picks right specialist agent (and model) for each subtask | Agent-capability registry; benchmark history (cost/quality/latency) | Routing accuracy ≥95% vs oracle; cost within budget | Beats human producer in agent/vendor selection | OrchestratorAgent, CostOptimizerAgent | PlannerAgent (bad decomposition) | Agent registry DB; benchmark leaderboard cache; pricing APIs | Classifier + ReAct (match task embedding → agent capability) |
| 56 | **JudgeAgent** | Adjudicates disputes via multi-agent debate; scores against rubric | Du 2023 (LLM debate); MT-Bench rubrics; guild scoring sheets | Inter-rater κ vs expert panel ≥0.8 | Higher κ than median human juror | HiTL on overturned rulings | DirectorAgent, ScreenwriterAgent, any disputing pair | MT-Bench/Arena evaluation harness; rubric template engine | Multi-agent debate (Du 2023) + LLM-as-Judge (Zheng 2023) |
| 57 | **GateKeeperAgent** | Phase transitions; verifies L1/L2/L3 criteria; signs C2PA | Stage-gate methodology; PGA Producers Mark; QMS audit | Zero leaked defects; sign-off SLA ≥99% | Lower escaped-defect rate than human QA lead | ComplianceAgent, AIQAConsistencyAgent | OrchestratorAgent (premature advance) | C2PA signing (c2patool); JSON schema validators; rubric evaluation endpoints | Constitutional AI (constitution = phase-gate criteria) |
| 58 | **MemoryAgent** | Episodic + long-term project memory; retrieval for any agent | Reflexion (Shinn 2023); MemGPT; vector-DB best practices | Retrieval precision@5 ≥0.9; freshness SLA | Higher recall than producer's bible at scale | All agents (correction events) | All agents (stale facts) | Pinecone/Weaviate/Qdrant vector DB; MemGPT-style hierarchical memory; embedding models | Reflexion memory architecture (MemGPT extension) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 59 | **IdeationAgent** | Divergent brainstorm of concepts, hooks, taglines | Cannes Grand Prix; D&AD; IDEO design-thinking; SCAMPER/de Bono | Idea-count; novelty (embedding distance); semantic diversity | Wins agency-pitch shootouts on concept density | CreativeDirectorAgent, NoveltyAgent | CopywriterAgent (derivative), DirectorAgent (unfilmable) | Embedding novelty scorer; concept clustering (UMAP); Are.na/Pinterest search | Self-Refine + NoveltyAgent as critic |
| 60 | **NarrativeArcAgent** | 3-act / Save-the-Cat / Hero's Journey structure | Campbell; Snyder *Save the Cat*; Truby; Black List analyses | Beat-sheet coverage 100%; turning-point spacing; arc curve fit | Beats WGA first drafts on structural rubric | ScreenwriterAgent, DirectorAgent | ScreenwriterAgent (sagging middle) | Beat-sheet validator; emotional-arc plotter; structure templates | Self-Refine (rubric: beat-sheet completeness) |
| 61 | **StyleTransferAgent** | Applies named aesthetic consistently across shots | Curated style corpora; LoRA/seed registries; reference-frame banks | Style-similarity (CLIP/DINO) ≥0.85; cross-shot variance ≤τ | Wins blind preference vs human colorist+grader | DirectorAgent, ColoristAgent | GeneratorAgent (off-style) | LoRA weights per style; CLIP/DINO similarity scorer; Runway style-lock mode; ComfyUI | Self-Refine (CLIP style score as feedback) |
| 62 | **WorldBuildingAgent** | Lore, rules, geography, factions, magic/tech systems | Tolkien; *Worldbuilding* (Adams); fan-wikis; series-bible leaks | Internal-consistency (no contradictions); rule-completeness | Lower contradiction rate than writers' bibles at 10× volume | ShowrunnerAgent, FactCheckerAgent | ScreenwriterAgent (lore break), ConceptArtistAgent | Long-context LLM (Gemini 2.5 Pro); contradiction-detection model; wiki-graph DB | Reflexion (contradiction corrections → episodic memory) |
| 63 | **MoodBoardAgent** | Reference boards: visual, sonic, tonal | Pinterest/Are.na; lookbook archives; Spotify-Canvas | Reference coherence (cluster tightness); brief alignment | Faster + tighter boards than art director (blind A/B) | DirectorAgent, ProductionDesignAgent | ConceptArtistAgent (off-mood) | Pinterest/Are.na APIs; Spotify Canvas; CLIP clustering; Figma board generation | ReAct (search → cluster → layout → validate coherence) |
| 64 | **NoveltyAgent / Anti-Cliché Critic** | Flags tropes, clichés, over-fit outputs | TV Tropes; OpenSubtitles n-gram freq; corpus-novelty embeddings | Cliché-hit count; novelty score vs category prior | Catches more clichés than experienced script editor | IdeationAgent, ScreenwriterAgent | ScreenwriterAgent (trope-stuffed), CopywriterAgent (templated) | TV Tropes scraper; n-gram frequency DB; embedding novelty scorer | LLM-as-Judge (anti-cliché constitution) |
| 65 | **EmotionalArcAgent** | Maps valence/arousal curve; suggests beats | Plutchik; affective-computing corpora; Cron *Story Genius* | Curve-fit to target; biosignal-proxy regression accuracy | Better retention prediction than NRG test-screening cards | DirectorAgent, EditorAgent, ComposerAgent | EditorAgent (flat middle), ComposerAgent (cue mismatch) | Sentiment/emotion classifiers (GoEmotions); retention-curve predictor; biosignal proxy model | Self-Refine (emotional-arc curve as rubric target) |

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
| 90 | **UXAgent** | Reviews clarity and usability of personalized or interactive outputs | UX heuristics, accessibility criteria, usability testing patterns | Readability, friction-point detection, 
…



### From `corpus/study/ui/backend_agent_management.md` Copy: `sources/excerpts/backend_agent_management.md`.


# Find all agents that are configured to critique this agent
    critics = [a for a in agents if event.agent_id in a.comments_on]

for critic in critics:
        # Only deliver if the producer accepts critique from this critic
        if critic.agent_id in producer_agent.accepts_critique_from:
            enqueue_critique_task(
                critic_agent=critic.agent_id,
                artifact=event.artifact_id,
                producer_agent=event.agent_id
            )
```

```text
USER clicks [▶ LAUNCH]
         │
         ▼
┌─────────────────────────────┐
│     API GATEWAY             │
│     POST /productions       │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  PRODUCTION MANAGER         │
│  • Create DB record         │
│  • Load template (A-J)      │
│  • Initialize budget        │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│  ORCHESTRATION ENGINE (LangGraph)                            │
│                                                             │
│  Phase 1: PLANNING                                          │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 1. Invoke PlannerAgent (agent_id=54)                │    │
│  │    → LLM decomposes brief into task DAG             │    │
│  │    → Output: {tasks: [...], gates: [...], deps: {}} │    │
│  │                                                     │    │
│  │ 2. Invoke RouterAgent (agent_id=55)                 │    │
│  │    → Assigns model+provider per task                │    │
│  │    → Respects budget constraints                    │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  Phase 2: EXECUTION (loop until all phases complete)        │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 3. Dispatch tasks to WORKER POOL:                   │    │
│  │    • Parallel where deps allow                      │    │
│  │    • Sequential where order matters                 │    │
│  │                                                     │    │
│  │ 4. WORKER executes agent task:                      │    │
│  │    load_config → build_prompt → call_LLM →          │    │
│  │    execute_tools → self_refine → publish_result     │    │
│  │                                                     │    │
│  │ 5. On task complete:                                │    │
│  │    • Update agent state                             │    │
│  │    • Check if critics need to run                   │    │
│  │    • Check if dependencies are now satisfied        │    │
│  │    • Dispatch next eligible tasks                   │    │
│  │                                                     │    │
│  │ 6. On GATE reached:                                 │    │
│  │    • GateKeeperAgent evaluates criteria             │    │
│  │    • JudgeAgent scores via rubric                   │    │
│  │    • If auto-pass: advance                          │    │
│  │    • If needs human: PAUSE + notify UI              │    │
│  │    • Wait for human decision                        │    │
│  │    • On approve: advance to next phase              │    │
│  │    • On reject: re-dispatch to revision agents      │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  Phase 3: DELIVERY (after all gates pass)                   │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 7. DistributorAgent packages per channel            │    │
│  │ 8. ComplianceAgent signs C2PA                       │    │
│  │ 9. Publish to target platforms                      │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```



### From `corpus/study/ui/RETHINK_100_IMPROVEMENTS.md` Copy: `sources/excerpts/RETHINK_100_IMPROVEMENTS.md`.


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
| 29 | Shadow mode for new configs | Safety | Medium |
| 30 | Multi-tenant isolation | Enterprise | Medium |



### From `corpus/study/ui/ui_design.md` Copy: `sources/excerpts/ui_design.md`.


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
┌─────────────────────────────────────────────────────────────────────────────┐
│  QUALITY DASHBOARD                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── OVERALL SCORES ─────────────────────────────────────────────────┐    │
│  │                                                                    │    │
│  │  VBench:       ████████████████░░░░  0.82  (threshold: 0.75) ✓    │    │
│  │  CLIP-T avg:   █████████████████░░░  0.34  (threshold: 0.32) ✓    │    │
│  │  FVD:          ██████████████░░░░░░  142   (threshold: <180) ✓    │    │
│  │  Aesthetic:    ████████████████████  6.5/7 (threshold: 5.5) ✓     │    │
│  │  Audio STOI:   ██████████████████░░  0.88  (threshold: 0.85) ✓    │    │
│  │  Loudness:     ████████████████████  -23.1 LUFS (target: -23) ✓   │    │
│  │                                                                    │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── PER-SHOT BREAKDOWN ─────────────────────────────────────────────┐    │
│  │  Shot │ CLIP-T │ Hands │ Face-ID │ Temporal │ Style │ Status       │    │
│  │  ─────┼────────┼───────┼─────────┼──────────┼───────┼──────────── │    │
│  │  1    │ 0.35   │ ✓     │ 0.98    │ ✓        │ 0.87  │ ✓ Pass      │    │
│  │  2    │ 0.31   │ ⚠     │ 0.96    │ ✓        │ 0.85  │ ⚠ Review    │    │
│  │  3    │ 0.34   │ ✓     │ 0.97    │ ✓        │ 0.88  │ ✓ Pass      │    │
│  │  4    │ 0.36   │ ✓     │ 0.95    │ ⚠        │ 0.84  │ ⚠ Review    │    │
│  │  5    │ 0.34   │ ✓     │ 0.98    │ ✓        │ 0.86  │ ✓ Pass      │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌─── REGRESSION ALERTS ──────────────────────────────────────────────┐    │
│  │  ⚠ Shot 2: Hand artifact at frame 142 (score dropped 0.03)        │    │
│  │  ⚠ Shot 4: Temporal flicker at transition (score: 0.71 < 0.75)    │    │
│  │  [Auto-Fix All]  [Manual Review]  [Dismiss Non-Critical]          │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

| Component | Usage | Variants |
|-----------|-------|----------|
| `AgentNodeCard` | DAG canvas nodes | mini (DAG), expanded (inspector), list-row (registry) |
| `ArtifactCard` | Gallery items | thumbnail, detail, compare |
| `CritiqueMessage` | Feed items | info, warning, critical, resolved |
| `GateCheckpoint` | DAG + timeline | pending, reviewing, approved, rejected |
| `MetricBar` | Quality dashboard | pass (green), warning (amber), fail (red) |
| `TimelineSwim` | Phase swimlanes | pre-pro, production, post, delivery |
| `BriefField` | Brief studio inputs | text, dropdown, slider, tag-input, file-drop, toggle |
| `DrawerPanel` | Detail views | bottom-slide, side-slide, full-screen |
| `CommandPalette` | Global search/action | Cmd+K triggered |
| `NotificationBadge` | Top bar + nav | count badge, priority indicator |
| `ProvBadge` | C2PA provenance | verified, pending, unsigned |
| `BudgetGauge` | Cost tracking | linear progress with threshold markers |

| Priority | Trigger | Notification Style | Requires Action |
|----------|---------|-------------------|-----------------|
| Critical | Compliance block, budget overrun, legal expiry | Full-screen modal + audio chime | Yes (cannot dismiss) |
| High | Gate ready for approval, quality failure | Toast + badge + status bar flash | Yes (within 5min) |
| Medium | Agent completed task, new critique received | Badge increment + feed highlight | No (informational) |
| Low | Optimization suggestion, memory entry added | Badge only | No |

interface CritiqueMessage {
  id: string;
  timestamp: string;
  fromAgent: number;
  toAgent: number | 'ALL';
  severity: 'info'|'warning'|'critical';
  content: string;
  attachments: ArtifactRef[];
  status: 'open'|'accepted'|'rejected'|'resolved';
  humanResponse?: string;
}
```



## Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


## Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


## Provenance

- Master roster row va_id=95 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `vendor/va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.critic · va_id=95 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **CriticAgent** (`video.critic`, va_id=95, category `10-Sup`).

### Responsibility focus
Simulates reviewer, press, or jury interpretation

### Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: LLM-as-judge, multi-agent debate, critique aggregation, preference learning for media QA
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI judges for content quality, multi-agent critique, video QA with LLMs
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: LLM-as-a-judge for video, multi-agent critique workflows, AI quality arbitration

### arXiv / academic integration (role-applied)
- Du et al. multi-agent debate for factuality
- Zheng et al. LLM-as-Judge / MT-Bench rubrics; inter-rater κ targets

**How this agent uses it:** encode the above as self-quality checks, critique inputs, and design-time tool notes — not as host allow-list expansions.

### X / industry practice (role-applied)
- Arena-style pairwise judging for creative disputes

### YouTube / practitioner guidance (role-applied)
- Rubric adjudication workflows for creative reviews

### Implementation notes for v1
1. Emit artifacts matching role responsibility; self-score against Self-quality criteria.
2. Accept critique only from listed critics; escalate disputes to Judge/Gate as DNA dictates.
3. Design-time tools remain documented only; runtime tools stay in `agent_spec.json`.
4. N1: no second control plane; video logic under `business/video/**` only.

### Research depth note (honest)
This v1 section maps **role-family** literature and the agent’s migration prompt topics into SPEC.
It is **not** a full unsummarized download of every paper/video transcript.
Live primary-source expansion remains a residual for score 100 on S3 where depth is still thin.

<!-- migration_capability_research · video.critic · v1 · 2026-07-13 -->

### `sources/generic/video.promptoptimizer.SPEC.md`

# PromptOptimizerAgent

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 73 |
| **pack_id** | `video.promptoptimizer` |
| **category** | `9-Meta` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.promptoptimizer/` |

## Category roster section (full, from agents.md)

_The following is the complete category section from the master roster (includes peers in the same craft category)._


## 9. Specialist Meta-Agents

### 9.1 Orchestration Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 53 | **OrchestratorAgent** | Runs CrewAI/AutoGen/LangGraph DAG; retries, timeouts, fan-out/fan-in | LangGraph + CrewAI + AutoGen patterns; Airflow/Temporal; PGA schedule templates | DAG completion ≥99.5%; SLA adherence; deadlock = 0 | Lower TTD than human EP at same scope | ProducerAgent (scope), JudgeAgent (dispute), HiTL on stall | All agents (resource burn, retry storms) | LangGraph state machine; Temporal workflow engine; Redis (distributed locks); observability (LangSmith) | Agentic Graph (LangGraph) — deterministic DAG execution |
| 54 | **PlannerAgent** | Decomposes brief into phased DAG with assignments + critic gates | PMBOK; CrewAI task graphs; phase templates | Plan validity (no missing gate); cost variance <10% | Tighter, cheaper plans than EP first pass (blind A/B) | ProducerAgent, FinanceAgent (budget) | RouterAgent (wrong pick), OrchestratorAgent | LangGraph plan-gen; cost-estimation models; Gantt/PERT tools | ReAct (decompose → estimate → validate → emit DAG) |
| 55 | **RouterAgent** | Picks right specialist agent (and model) for each subtask | Agent-capability registry; benchmark history (cost/quality/latency) | Routing accuracy ≥95% vs oracle; cost within budget | Beats human producer in agent/vendor selection | OrchestratorAgent, CostOptimizerAgent | PlannerAgent (bad decomposition) | Agent registry DB; benchmark leaderboard cache; pricing APIs | Classifier + ReAct (match task embedding → agent capability) |
| 56 | **JudgeAgent** | Adjudicates disputes via multi-agent debate; scores against rubric | Du 2023 (LLM debate); MT-Bench rubrics; guild scoring sheets | Inter-rater κ vs expert panel ≥0.8 | Higher κ than median human juror | HiTL on overturned rulings | DirectorAgent, ScreenwriterAgent, any disputing pair | MT-Bench/Arena evaluation harness; rubric template engine | Multi-agent debate (Du 2023) + LLM-as-Judge (Zheng 2023) |
| 57 | **GateKeeperAgent** | Phase transitions; verifies L1/L2/L3 criteria; signs C2PA | Stage-gate methodology; PGA Producers Mark; QMS audit | Zero leaked defects; sign-off SLA ≥99% | Lower escaped-defect rate than human QA lead | ComplianceAgent, AIQAConsistencyAgent | OrchestratorAgent (premature advance) | C2PA signing (c2patool); JSON schema validators; rubric evaluation endpoints | Constitutional AI (constitution = phase-gate criteria) |
| 58 | **MemoryAgent** | Episodic + long-term project memory; retrieval for any agent | Reflexion (Shinn 2023); MemGPT; vector-DB best practices | Retrieval precision@5 ≥0.9; freshness SLA | Higher recall than producer's bible at scale | All agents (correction events) | All agents (stale facts) | Pinecone/Weaviate/Qdrant vector DB; MemGPT-style hierarchical memory; embedding models | Reflexion memory architecture (MemGPT extension) |

### 9.2 Creative Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 59 | **IdeationAgent** | Divergent brainstorm of concepts, hooks, taglines | Cannes Grand Prix; D&AD; IDEO design-thinking; SCAMPER/de Bono | Idea-count; novelty (embedding distance); semantic diversity | Wins agency-pitch shootouts on concept density | CreativeDirectorAgent, NoveltyAgent | CopywriterAgent (derivative), DirectorAgent (unfilmable) | Embedding novelty scorer; concept clustering (UMAP); Are.na/Pinterest search | Self-Refine + NoveltyAgent as critic |
| 60 | **NarrativeArcAgent** | 3-act / Save-the-Cat / Hero's Journey structure | Campbell; Snyder *Save the Cat*; Truby; Black List analyses | Beat-sheet coverage 100%; turning-point spacing; arc curve fit | Beats WGA first drafts on structural rubric | ScreenwriterAgent, DirectorAgent | ScreenwriterAgent (sagging middle) | Beat-sheet validator; emotional-arc plotter; structure templates | Self-Refine (rubric: beat-sheet completeness) |
| 61 | **StyleTransferAgent** | Applies named aesthetic consistently across shots | Curated style corpora; LoRA/seed registries; reference-frame banks | Style-similarity (CLIP/DINO) ≥0.85; cross-shot variance ≤τ | Wins blind preference vs human colorist+grader | DirectorAgent, ColoristAgent | GeneratorAgent (off-style) | LoRA weights per style; CLIP/DINO similarity scorer; Runway style-lock mode; ComfyUI | Self-Refine (CLIP style score as feedback) |
| 62 | **WorldBuildingAgent** | Lore, rules, geography, factions, magic/tech systems | Tolkien; *Worldbuilding* (Adams); fan-wikis; series-bible leaks | Internal-consistency (no contradictions); rule-completeness | Lower contradiction rate than writers' bibles at 10× volume | ShowrunnerAgent, FactCheckerAgent | ScreenwriterAgent (lore break), ConceptArtistAgent | Long-context LLM (Gemini 2.5 Pro); contradiction-detection model; wiki-graph DB | Reflexion (contradiction corrections → episodic memory) |
| 63 | **MoodBoardAgent** | Reference boards: visual, sonic, tonal | Pinterest/Are.na; lookbook archives; Spotify-Canvas | Reference coherence (cluster tightness); brief alignment | Faster + tighter boards than art director (blind A/B) | DirectorAgent, ProductionDesignAgent | ConceptArtistAgent (off-mood) | Pinterest/Are.na APIs; Spotify Canvas; CLIP clustering; Figma board generation | ReAct (search → cluster → layout → validate coherence) |
| 64 | **NoveltyAgent / Anti-Cliché Critic** | Flags tropes, clichés, over-fit outputs | TV Tropes; OpenSubtitles n-gram freq; corpus-novelty embeddings | Cliché-hit count; novelty score vs category prior | Catches more clichés than experienced script editor | IdeationAgent, ScreenwriterAgent | ScreenwriterAgent (trope-stuffed), CopywriterAgent (templated) | TV Tropes scraper; n-gram frequency DB; embedding novelty scorer | LLM-as-Judge (anti-cliché constitution) |
| 65 | **EmotionalArcAgent** | Maps valence/arousal curve; suggests beats | Plutchik; affective-computing corpora; Cron *Story Genius* | Curve-fit to target; biosignal-proxy regression accuracy | Better retention prediction than NRG test-screening cards | DirectorAgent, EditorAgent, ComposerAgent | EditorAgent (flat middle), ComposerAgent (cue mismatch) | Sentiment/emotion classifiers (GoEmotions); retention-curve predictor; biosignal proxy model | Self-Refine (emotional-arc curve as rubric target) |

### 9.3 Research Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 66 | **WebResearchAgent** | Live web search, source ranking, citation extraction | Bing/Google/Brave APIs; Common Crawl; Perplexity patterns | Source-grade per claim; citation precision; recency hit | Faster + more sources than newsroom researcher | FactCheckerAgent, CitationAgent | ScriptwriterAgent (uncited claim) | Brave/Google Search API; Jina Reader (web→markdown); source-quality classifier | ReAct (query → fetch → extract → grade → cite) |
| 67 | **ArchiveResearchAgent** | Historical / academic / archival deep search | JSTOR, arXiv, PubMed, AP Archive, Getty, FOIA | Primary-source ratio; archive-coverage breadth | Higher primary-source ratio than doc producer | FactCheckerAgent, SMEAgent | ScriptwriterAgent (secondary-source reliance) | JSTOR/arXiv/PubMed APIs; Getty Images API; FOIA request tools; OCR (Tesseract) | ReAct (formulate query → search archive → extract → grade source) |
| 68 | **TrendIntelligenceAgent** | Detects emerging memes, sounds, formats | TikTok Creative Center; Trendpop; Tubular; Reddit/X firehose | Prediction lead time vs peak; precision/recall on trend list | Earlier detection than human strategists at higher precision | SocialStrategistAgent, CopywriterAgent | IdeationAgent (off-trend) | TikTok Creative Center API; Reddit/X streaming APIs; Sensor Tower; Google Trends | ReAct + time-series anomaly detection |
| 69 | **CompetitorIntelligenceAgent** | What competitors are shipping | Meta Ad Library; TikTok Top Ads; YouTube scrape; release trackers | Coverage % of competitor set; our-novelty vs landscape | More comprehensive than agency strategy decks | BrandAgent, CreativeDirectorAgent | IdeationAgent (derivative) | Meta Ad Library API; TikTok Top Ads; SimilarWeb; YouTube Data API v3 | ReAct (scrape competitor → classify → report gaps) |
| 70 | **CitationAgent** | Normalizes sources; grades primary/secondary/tertiary | Chicago, APA, AP style; SPJ grading; CRAAP test | Citation format 100% valid; primary % ≥target | Lower error rate than newsroom copy desk | FactCheckerAgent, JournalistAgent | WebResearchAgent (weak source) | Citation parsers (AnyStyle); DOI resolver; CRAAP scoring model | Self-Refine (format validator + source grader as rubric) |
| 71 | **InterviewSynthesisAgent** | Synthesizes practitioner interviews into data | Otter/Rev transcripts; consent forms; SAG/WGA templates | Inter-coder agreement on themes; consent integrity | Faster + richer theme extraction than qualitative researcher | ResearchPIAgent (HiTL), ComplianceAgent | SMEAgent (mis-summarized expert) | Otter.ai/Rev API (transcription); thematic coding models; consent-management DB | Reflexion (interviewer refines questions based on theme gaps) |
| 72 | **BenchmarkResearchAgent** | Monitors VBench, EvalCrafter, MT-Bench, FVD, CLIP-T leaderboards | Papers-with-Code; HuggingFace leaderboards; conference proceedings | Coverage of benchmarks; freshness ≤7 days | Faster + broader than ML-research team | OptimizationAgents (any) | All AI agents (stale baselines) | Papers-with-Code API; HuggingFace Hub API; arXiv RSS; VBench leaderboard scraper | ReAct (poll leaderboards → detect change → alert) |

### 9.4 Optimization Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 73 | **PromptOptimizerAgent** | Auto-improves prompts via OPRO/APE/DSPy/Promptbreeder | OPRO (Yang 2023); APE (Zhou 2022); DSPy (Stanford); Promptbreeder (DeepMind) | Score uplift per iteration; convergence speed | Beats hand-tuned prompts on held-out briefs | PromptEngineerAgent, AIQAAgent | PromptEngineerAgent (sub-optimal seed) | DSPy framework (MIPRO optimizer); OPRO implementation; held-out eval harness | DSPy compilation + OPRO meta-optimization |
| 74 | **CostOptimizerAgent** | Routes between models/providers for $/quality | Provider pricing; cost-quality frontiers; FrugalGPT patterns | $/successful-task; Pareto distance from frontier | Lower $/quality than human CFO routing | RouterAgent, FinanceAgent | RouterAgent (over-spend), GeneratorAgent (re-roll burn) | Provider pricing APIs; benchmark cost DB; FrugalGPT cascade logic | ReAct (evaluate task → pick cheapest model meeting threshold) |
| 75 | **LatencyOptimizerAgent** | Parallelization, caching, speculative decoding, batching | vLLM; TensorRT-LLM; distillation; Anyscale/Ray | p50/p95 latency; throughput/GPU-hour | Lower p95 than human-tuned pipeline | OrchestratorAgent | OrchestratorAgent (serial bottleneck) | vLLM; TensorRT-LLM; Ray Serve; Redis (response cache); speculative decoding configs | Tool-use profiling + automated pipeline restructuring |
| 76 | **RetentionOptimizerAgent** | Tunes hook, pacing, structure for AVD/hold-rate | YouTube Analytics benchmarks; TikTok retention curves; AudienceSim | Predicted retention vs actual; AVD lift over control | Beats senior YouTube editor on AVD lift (A/B) | EditorAgent, AudienceSimAgent | EditorAgent (slow opener), ScriptwriterAgent (front fluff) | YouTube Analytics API; retention-curve predictor model; A/B test framework | RLAIF (reward = retention uplift from real analytics) |
| 77 | **ROASOptimizerAgent** | Optimizes ad creatives for performance | Meta Marketing Science; TikTok Ads Academy; MMM/MTA lit | ROAS uplift vs control; significance ≥95% | Beats senior marketer at equal budget | PerformanceMarketerAgent, AnalystAgent | UGCAgent (low hook), CopywriterAgent (weak CTA) | Meta Ads API (creative testing); TikTok Ads; Bayesian MMM tools (Robyn/Meridian) | RLAIF (reward = real ROAS from ad platform feedback) |
| 78 | **AccessibilityOptimizerAgent** | WCAG 2.2 contrast, captions, audio description, color-blind safe | WCAG 2.2; W3C/WAI-ARIA; DCMP captioning key; Deaf/HoH guidelines | Conformance 100% AA, ≥90% AAA; caption WER ≤2% | Catches more a11y defects than ADA-certified auditor | AccessibilityAgent (HiTL), ComplianceAgent | EditorAgent (caption sync), ColoristAgent (contrast) | axe-core/Lighthouse (contrast); Whisper v4 (captioning); audio-description generator | Constitutional AI (constitution = WCAG 2.2 success criteria) |
| 79 | **EvaluationHarnessAgent** | Runs benchmarks (VBench, EvalCrafter, MT-Bench, FVD, CLIP-T); posts regressions | Papers-with-Code; HuggingFace leaderboards; benchmark repos | Regression precision/recall; alert latency <1h | Catches regressions faster than ML-eng rotation | BenchmarkResearchAgent | All AI agents (regression alerts) | VBench suite; EvalCrafter; MT-Bench harness; CI/CD (GitHub Actions); alerting (PagerDuty) | Tool-use / ReAct (run benchmark → compare → alert if regressed) |
| 80 | **SafetyRedTeamAgent** | Adversarially attacks for deepfake, bias, jailbreak, defamation | Hany Farid benchmarks; Partnership on AI Framework; OWASP LLM Top 10 | Attack-success kept ≤1%; taxonomy coverage | Higher coverage than internal red-team rotation | EthicsAgent (HiTL), ComplianceAgent | AvatarDesignAgent, VoiceCloneAgent, AllGenerators | Deepfake detectors (Farid lab models); bias probes; jailbreak prompt banks; OWASP scanner | Multi-agent debate (red-team vs defender) + adversarial search |

---


## Responsibility

Auto-improves prompts via OPRO/APE/DSPy/Promptbreeder

## Knowledge distillation sources

OPRO (Yang 2023); APE (Zhou 2022); DSPy (Stanford); Promptbreeder (DeepMind)

## Self-quality criteria

Score uplift per iteration; convergence speed

## Surpass-human signal

Beats hand-tuned prompts on held-out briefs

## Critique bus

- **Accepts critique from:** PromptEngineerAgent, AIQAAgent

- **Comments on:** PromptEngineerAgent (sub-optimal seed)

## Tools (design-time documentation)

DSPy framework (MIPRO optimizer); OPRO implementation; held-out eval harness

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

DSPy compilation + OPRO meta-optimization

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


### Document: `study/optimization_agent_functional_specification.md`

_Embedded from `corpus/study/optimization_agent_functional_specification.md`. Also stored at `sources/study/optimization_agent_functional_specification.md` under this agent folder._


**Improved Functional Specification: Process Optimization Agent (v2.0 – Research-Enhanced)**

**Document Version:** 2.0  
**Date:** May 26, 2026  
**Author:** Grok (xAI) – Research synthesis from arXiv (2024–2026 papers on multi-agent LLM systems, Six Sigma Agent, AgentOps, digital process twins, and agentic BPM)  
**Purpose:** Deliver a production-ready, agentic evolution of the original specification, incorporating latest advances in LLM-powered multi-agent systems, autonomous optimization, process mining, digital twins, and enterprise reliability mechanisms.

---

### 1. Executive Summary of Research & Key Upgrades

Deep research across arXiv (e.g., MASS framework for MAS design, Six Sigma Agent for reliability, LLM-guided chemical process optimization, AgentOps observability pipeline, Digital Twins of Business Processes manifesto, SiriuS self-improving MAS, and Agentic BPM surveys) reveals critical gaps in v1.0:

- **Multi-agent collaboration + topology optimization** dramatically outperforms single-agent or static workflows.
- **Enterprise reliability** requires explicit decomposition + consensus (achieving true Six Sigma quality: 3.4 DPMO).
- **Autonomous constraint inference + iterative refinement** eliminates manual bottlenecks.
- **Digital process twins + real-time process mining** enable what-if simulation and living models.
- **Observability & self-improvement loops** (AgentOps-style) turn the agent into a continuously optimizing system.
- **Strong reasoning models** (o-series equivalents) + heterogeneous execution are non-negotiable for convergence.

**v2.0 upgrades** make the agent truly *agentic*, self-improving, and enterprise-deployable while preserving Lean + Six Sigma DMAIC as the core backbone.

---

### 2. Core Architecture (New – Multi-Agent Native)

The agent operates as a **hierarchical multi-agent system (MAS)** orchestrated via AutoGen-style GroupChat or equivalent, with dynamic topology optimization (inspired by MASS framework).

**Specialized Sub-Agents (roles assigned dynamically or via MASS-style search):**
- **Context & Constraint Agent** — Infers realistic operating bounds, SIPOC, and process overview from minimal descriptions.
- **Discovery & Mining Agent** — Performs process mining (event logs → BPMN/Petri nets/OCEL), value-stream mapping, and digital twin initialization.
- **Measurement & Analysis Agent** — Calculates KPIs, identifies wastes/bottlenecks, runs root-cause (5 Whys + Fishbone + causal ML).
- **Simulation & Validation Agent** — Runs discrete-event / Monte Carlo / what-if scenarios; integrates physics-informed or LLM-parameterized simulators.
- **Improvement & Suggestion Agent** — Generates, prioritizes, and iteratively refines solutions using RL-informed or Bayesian optimization.
- **Reliability & Consensus Agent** (Six Sigma layer) — Decomposes tasks into atomic DAG, runs parallel micro-agent sampling across heterogeneous models, applies embedding-based clustering + majority voting.
- **Control & Observability Agent** (AgentOps-inspired) — Monitors runtime, detects drift, triggers self-optimization.

**Topology Optimization:** Internally applies MASS-like interleaved optimization (local prompt → topology pruning → global prompt) for new processes.

---

### 3. Updated Methodologies

**Hybrid Framework:** DMAIC + Lean + Theory of Constraints + **Agentic Enhancements**

| Phase | Traditional | v2.0 Agentic Upgrade |
|-------|-------------|-----------------------|
| **Define** | SIPOC + charter | + Autonomous context/constraint inference |
| **Measure** | Manual KPIs | + Real-time process mining + digital twin sync |
| **Analyze** | 5 Whys / Pareto | + Causal ML + multi-agent hypothesis testing |
| **Improve** | Lean toolkit | + LLM-guided iterative optimization loops + simulation-driven what-if |
| **Control** | SPC dashboards | + AgentOps pipeline (observe → detect → RCA → auto-optimize) + living digital twin |

**Additional Paradigms Integrated:**
- **Self-improving via bootstrapped reasoning** (SiriuS-style: learn from successful trajectories).
- **Consensus-driven execution** for Six Sigma reliability.
- **Digital Process Twin (DPT)** as the central executable model.

---

### 4. Enhanced Functional Requirements

#### 4.1 Process Discovery & Mapping (Upgraded)
- LLM-assisted extraction from documents, event logs (OCEL support), or natural-language descriptions.
- Automatic generation of BPMN, Petri nets, or object-centric models.
- Hierarchical decomposition with human-in-the-loop validation.

#### 4.2 Performance Measurement & Digital Twin Initialization
- Real-time KPI calculation + living DPT synchronization via IoT/CEP where available.
- Baseline digital twin creation for simulation-ready what-if analysis.

#### 4.3 Waste, Bottleneck & Root-Cause Analysis
- 8 Wastes + TOC + automated Pareto.
- Causal ML integration for intervention impact prediction.

#### 4.4 Improvement Generation & Autonomous Optimization
- Lean toolkit + automation opportunities + layout suggestions.
- **Iterative refinement loops** (ParameterAgent → Validation → Simulation → SuggestionAgent).
- Constraint inference from minimal descriptions (no pre-defined bounds needed).
- Multi-objective Bayesian optimization or RL-informed search when data allows.

#### 4.5 Reliability & Enterprise-Grade Execution (New Core Feature)
- **Task decomposition** into verifiable atomic DAG (minimality + determinism).
- **Micro-agent sampling** (n=5–13 parallel heterogeneous LLM executions).
- **Embedding-based consensus voting** with dynamic scaling → 3.4 DPMO target.
- Exponential error reduction while achieving ~80% cost savings vs. single frontier model.

#### 4.6 Simulation & Validation (Enhanced)
- LLM-parameterized discrete-event simulation.
- Digital twin what-if scenarios with real-time data.
- Monte Carlo + uncertainty quantification.

#### 4.7 Prioritization, ROI & Implementation Planning
- Impact/Effort + full cost-benefit with risk register.
- Phased roadmap + pilot design + change management.

#### 4.8 Control, Sustainment & Self-Improvement (AgentOps Pipeline)
- **Six-stage loop:** Observe → Collect Metrics → Detect Issues → RCA → Optimize Recommendations → Automate Operations.
- Statistical Process Control + anomaly detection + auto-prompt/workflow repair.
- Continuous re-optimization triggers on drift or new event data.

---

### 5. User Interaction Model (Agentic & Iterative)

1. **Goal & Context Ingestion** (natural language + files/logs).
2. **Autonomous Scoping & Constraint Discovery**.
3. **Parallel Sub-Agent Execution** with user checkpoints.
4. **Iterative Refinement** (user can inject feedback or approve constraints).
5. **Consensus-Backed Deliverables** + executable digital twin.
6. **Runtime Monitoring Dashboard** + self-optimization reports.

**Behavior Rules (unchanged but strengthened):**
- Always state assumptions and confidence.
- Prefer strong reasoning models for critical paths.
- Human-in-the-loop for high-stakes decisions.

---

### 6. Input / Output Requirements (Unchanged but Expanded)

**New Inputs Supported:**
- Event logs (XES/OCEL), IoT streams, unstructured docs.

**Standard Output Package (Enhanced):**
- Executive summary + Project charter.
- Digital Process Twin (executable model).
- Root-cause + improvement recommendations (with explanations & consensus audit).
- Projected benefits + ROI simulation results.
- Implementation roadmap + Control plan.
- Observability dashboard spec + self-improvement log.

---

### 7. Non-Functional Requirements (Major Upgrades)

- **Reliability:** Target 3.4 DPMO via Six Sigma consensus architecture.
- **Cost Efficiency:** Leverage cheaper models + parallelism for 70–80% savings.
- **Explainability:** Natural-language reasoning traces + causal impact explanations.
- **Scalability:** From simple workflows to enterprise DTOs (Digital Twins of Organizations).
- **Security & Resilience:** RBAC, prompt-injection guards, tamper-proof logging.
- **Interoperability:** OpenTelemetry-compatible tracing + standard protocols for twin integration.

---

### 8. Success Criteria (Updated)

- Achieves measurable Six Sigma-level reliability in execution.
- Produces executable digital twin + autonomous what-if capability.
- Demonstrates self-improvement (performance gains across sessions).
- User can deploy recommendations with minimal rework.

---

### 9. Future Enhancements (v3.0+ Roadmap)

- Full process mining from raw logs → living twin.
- Reinforcement Learning for routing optimization.
- Multi-organization DTO scaling.
- Integration with Grok-native agents (DeepSearch, Code Fast, etc.) for real-time external knowledge.
- MASS-style automated topology search at runtime.

---

**Research-Backed Activation**

This v2.0 specification transforms the Process Optimization Agent from a structured analyst into a **self-improving, multi-agent, digital-twin-native optimization engine** aligned with 2025–2026 frontier research.




### Document: `study/optimization_agent_technical_specification.md`

_Embedded from `corpus/study/optimization_agent_technical_specification.md`. Also stored at `sources/study/optimization_agent_technical_specification.md` under this agent folder._


**Technical Specification: Process Optimization Agent (v2.0 – Research-Enhanced)**

**Document Version:** 2.0  
**Date:** May 26, 2026  
**Author:** Grok (xAI) – Synthesized from arXiv papers (2024–2026) including *Six Sigma Agent* (arXiv:2601.22290), *Multi-Agent System Search (MASS)* (arXiv:2502.02533), *AgentOps* observability frameworks (arXiv:2508.02121, 2411.05285), *Agentic BPM Systems* & Digital Process Twins (arXiv:2601.18833), *Specification and Evaluation of Multi-Agent LLM Systems* (arXiv:2506.10467), hierarchical/orchestrated MAS patterns (arXiv:2601.13671, 2501.06322), and xAI multi-agent capabilities.  
**Purpose:** Define the complete technical architecture, implementation details, and operational mechanisms required to realize the Process Optimization Agent as a reliable, self-improving, multi-agent LLM system.

---

### 1. System Overview

The Process Optimization Agent is implemented as a **hierarchical, orchestrated multi-agent LLM system (MAS)** with a living **Digital Process Twin (DPT)** at its core. It follows a hybrid **DMAIC + Lean + Theory of Constraints** methodology while achieving **enterprise-grade reliability** (target: 3.4 DPMO / Six Sigma level) through consensus-driven decomposed execution.

- **Deployment Model:** Containerized (Docker/Kubernetes) or serverless (cloud functions) with optional edge/IoT integration.
- **Runtime:** Python 3.12+ with LangGraph/AutoGen-style orchestration or custom GroupChat topology (MASS-optimized).
- **LLM Backends:** Heterogeneous mix (Grok-4.x, Claude 3.7+, GPT-4.5, Qwen2.5, open-source) for cost/reliability balance.
- **Observability:** Full AgentOps pipeline (traces, metrics, LLM calls, state checkpoints).

---

### 2. High-Level Architecture

```
[User / External Systems]
         ↓ (Natural Language + Files/Logs)
[Orchestrator Layer]
    ├── Context & Constraint Agent
    ├── Supervisor (MASS-style topology optimizer)
    └── Consensus & Reliability Engine (Six Sigma Agent)
         ↓
[Specialized Sub-Agent Swarm] (parallel + hierarchical)
    ├── Discovery & Mining Agent
    ├── Measurement & Analysis Agent
    ├── Simulation & Validation Agent
    ├── Improvement & Suggestion Agent
    └── Control & Observability Agent
         ↓
[Core State: Digital Process Twin (DPT)]
    - Executable model (Petri nets / OCEL / BPMN + simulation engine)
    - Real-time sync via event logs / IoT
         ↓
[Output Layer] → Deliverables + Implementation Roadmap + Self-Improvement Log
```

**Key Design Patterns (research-backed):**
- **Hierarchical Orchestration** — Top-level planner decomposes tasks; sub-agents execute (AgentOrchestra / BDIM-SE style).
- **MASS Topology Optimization** — Dynamic interleaving of prompt + topology search (local → global).
- **Six Sigma Consensus** — Task decomposition → micro-agent sampling (n=5–13 parallel LLMs) → embedding clustering + majority voting.
- **AgentOps Observability Loop** — Observe → Collect → Detect → RCA → Optimize → Automate.

---

### 3. Core Components & Technical Details

#### 3.1 Sub-Agents (Modular, Role-Based)
Each sub-agent is a specialized LLM instance with:
- Dedicated system prompt + role card
- Memory (short-term: vector store; long-term: symbolic belief structure)
- Tools (MCP-compliant: code execution, simulation, process mining)
- State checkpointing for time-travel debugging

| Sub-Agent | Primary LLM | Key Libraries/Tools | Responsibility |
|-----------|-------------|---------------------|--------------|
| Context & Constraint | Grok-4 / Claude | None (reasoning only) | SIPOC, bounds inference |
| Discovery & Mining | Qwen2.5 + process mining libs | pm4py, OCEL, BPMN | Event log → DPT initialization |
| Measurement & Analysis | Mix (GPT + open-source) | pandas, scipy, causal ML | KPIs, wastes, root cause |
| Simulation & Validation | Grok-4 | SimPy, Monte Carlo, gPROMS-style | What-if scenarios |
| Improvement & Suggestion | Claude 3.7 | Bayesian opt, RLHF-inspired | Solution generation + prioritization |
| Control & Observability | Dedicated lightweight | OpenTelemetry, Prometheus | Drift detection, self-repair |

#### 3.2 Digital Process Twin (DPT)
- **Representation:** Object-centric event log (OCEL 2.0) + executable Petri-net / BPMN model + simulation parameters.
- **Construction:** Process mining (pm4py) + LLM-augmented discovery from natural language / documents.
- **Simulation Engine:** Discrete-event (SimPy) + physics-informed where domain-specific; LLM-parameterized for qualitative steps.
- **Synchronization:** Real-time via Kafka / MQTT for IoT/event streams; periodic re-mining.
- **What-if Capability:** Monte Carlo + sensitivity analysis; outputs projected KPIs with confidence intervals.

#### 3.3 Reliability Layer (Six Sigma Agent)
- **Task Decomposition:** Automatic conversion of any high-level goal into a dependency DAG of atomic actions (minimal + deterministic).
- **Micro-Agent Sampling:** Each atomic action executed *n* times in parallel across heterogeneous LLMs.
- **Consensus Mechanism:**
  1. Embedding-based clustering (cosine similarity).
  2. Majority voting within largest cluster.
  3. Dynamic scaling: start at n=5; escalate to n=13 on uncertainty (target 3.4 DPMO).
- **Proven Gains (per paper):** 14,700× reliability improvement, ~80% cost reduction vs single frontier model.

#### 3.4 MASS-Inspired Topology Optimizer
- Runs as background supervisor.
- Three-stage interleaved optimization:
  1. Block-level prompt warm-up.
  2. Workflow topology search (pruned space).
  3. Global prompt refinement on best topology.
- Supports peer-to-peer, hierarchical, debate, and reflection patterns.

#### 3.5 AgentOps Observability & Self-Improvement
- **Traceability:** Full cognitive traces (prompt → reasoning → tool call → output) with semantic correlation.
- **Metrics:** Token usage, latency, error rates, consensus confidence, DPT accuracy.
- **Anomaly Detection:** Prompt injection, reasoning loops, coordination bottlenecks.
- **Self-Optimization Loop:** On drift → auto-RCA → prompt/topology repair → re-validation.
- **Tools:** OpenTelemetry + custom eBPF-style boundary tracing where deployed.

---

### 4. Data Models & Interfaces

- **Internal State:** JSON-serializable DAG + vector embeddings + symbolic beliefs (AgentSpeak-style).
- **Input Formats Supported:**
  - Text / documents (PDF, Word)
  - Event logs (XES, OCEL, CSV)
  - IoT streams, screenshots, process diagrams
- **Output Formats:**
  - Markdown report + Mermaid/BPMN diagrams
  - Executable DPT (JSON + SimPy script)
  - CSV/Excel for KPIs & ROI
  - JSON schema for API consumption
- **External Interfaces:**
  - REST/gRPC API for integration
  - MCP + A2A protocols for agent-to-agent communication
  - OpenTelemetry exporter

---

### 5. Non-Functional Requirements

| Requirement | Target | Implementation |
|-------------|--------|----------------|
| **Reliability** | 3.4 DPMO | Six Sigma consensus |
| **Latency** | <30s for simple; <5min for complex | Parallel sub-agents + caching |
| **Cost Efficiency** | 70–80% savings | Cheaper models + consensus |
| **Scalability** | 1–1000 concurrent processes | Kubernetes + async orchestration |
| **Security** | RBAC, prompt guards, audit logs | Isolation per tenant + encryption |
| **Explainability** | Full reasoning trace | Structured output + citations |
| **Observability** | 100% trace coverage | AgentOps pipeline |

---

### 6. Implementation Roadmap (Phases)

1. **Core MAS Framework** (2 weeks) — Orchestrator + sub-agents + basic DPT.
2. **Reliability & Consensus** (1 week) — Six Sigma layer.
3. **Simulation & MASS Optimizer** (2 weeks).
4. **AgentOps Self-Improvement** (1 week).
5. **Enterprise Integration & Testing** (2 weeks).

**Tech Stack Summary:**
- Orchestration: LangGraph / custom AutoGen
- Process Mining: pm4py
- Simulation: SimPy + custom LLM-parameterized
- Vector DB: FAISS / Pinecone
- Observability: OpenTelemetry + Prometheus + custom AgentOps dashboard
- Deployment: Docker + Kubernetes (or Grok-native if available)

---

**Activation Note**

This technical specification is fully aligned with the Functional Specification v2.0 and ready for implementation.





### Document: `study/llm_usage_functional_specification.md`

_Embedded from `corpus/study/llm_usage_functional_specification.md`. Also stored at `sources/study/llm_usage_functional_specification.md` under this agent folder._


# Build Central LLM API Usage & Cost Dashboard App

## Project Name Suggestion
**LLMUsageHub** or **MultiLLM Dashboard** or **API Cost Central** or **LLM Spend Tracker**

## 1. Project Overview
Create a **web application** that provides a **single central view** for tracking usage, costs, balances, spending, and token consumption across **all** of the user's LLM API accounts.

The user currently has accounts with:  
- x.ai (Grok API)  
- Poe  
- MiniMax  
- Kimi (Moonshot AI)  
- OpenRouter  
...and many others.

The app should let the user add their API keys once and see **everything aggregated in one beautiful dashboard** — total monthly spend, remaining credits, per-provider breakdowns, charts, trends, alerts, etc.

**Reference / Inspiration**:
Inspired by **[cc-switch](https://github.com/farion1231/cc-switch)** (the popular desktop tool for managing LLM providers for Claude Code / Codex / Gemini CLI). This web app is **purely focused on usage/cost analytics** across direct personal API keys, serving as a usage-only companion to cc-switch but as a web application.

## 2. Core Goals
- One unified place to monitor **all** LLM spending and usage.
- Secure, local-only storage of API keys (never sent to any server).
- Automatic or on-demand fetching of usage/billing data.
- Historical tracking + visualizations.
- Extremely extensible — easy to add new providers.
- Beautiful, modern UI similar to cc-switch.

## 3. Key Features (Must-Have)

### Provider Management
- Add / edit / remove accounts with: name, provider type (preset), API key, base URL (for custom endpoints), notes.
- Pre-built **presets** for as many providers as possible (see section 4).
- Support multiple accounts per provider.
- One-click “Refresh All” and individual refresh buttons.

### Usage & Balance Fetching
- Prefer **official APIs** where available (e.g. `/usage`, `/billing`, `/balance`, `/v1/token_plan/remains`, etc.).
- Fallback options:
  - Manual entry of current usage/balance.
  - Web dashboard scraping (using Playwright if needed, last resort).
- Background auto-refresh (configurable interval) + manual refresh.
- Store full history snapshots in local DB.

### Dashboard UI
- **Overview page**:
  - Total estimated USD spend (today / this month / all time).
  - Total remaining credits/balance (normalized where possible).
  - Number of active providers + quick status.
- **Provider cards** (grid or list):
  - Name + logo (if available).
  - Current balance / remaining credits.
  - Spend this month + trend indicator.
  - Last updated timestamp.
- **Charts**:
  - Spending trend (line chart — daily/weekly).
  - Cost breakdown by provider (pie).
  - Token usage by model (bar).
  - Usage heatmap or calendar view.
- **Detailed tables**:
  - Per-provider usage history.
  - Model-level breakdown.
- **Alerts**:
  - Low balance warnings (configurable thresholds).
  - High daily spend notifications.

### Cost Calculation
- Built-in pricing tables for major models (input/output tokens → USD).
- Allow user to override pricing per model.
- Show estimated USD even when provider only reports tokens.

### Data Persistence & Export
- Local **SQLite** database for all historical usage snapshots.
- Export full data as CSV or JSON.

### Security & UX
- API keys stored **encrypted** locally (Fernet symmetric encryption).
- Dark/light theme (default dark, matching modern AI tools).
- Browser-based UI accessible from localhost.
- Fully offline-first after initial setup.
- Responsive, clean, professional UI.

### Nice-to-Have (Phase 2)
- AI-powered insights (“You spent 68% on Kimi this month — consider switching heavy tasks to Groq”).
- Import/export configuration (including possible cc-switch import).
- Per-model cost forecasting.
- Optional proxy/router mode (like LiteLLM or cc-switch) so the app can also log usage from actual API calls.

## 4. Supported Providers (List as Many as Possible)
The app must ship with **pre-built presets** (fetch logic + pricing) for **as many providers as possible**. Start with user-mentioned ones, then expand.

**High Priority (User’s Current Providers)**
- xAI (Grok API) — console.x.ai usage / billing endpoints
- Poe.com — usage/points_history and current_balance endpoints
- OpenRouter — account usage API
- MiniMax — token plan remains and usage endpoints
- Kimi (Moonshot AI) — platform.moonshot.ai usage/balance API

**Other Major Providers (Include Full Presets)**
- OpenAI
- Anthropic (Claude)
- Google Gemini / Vertex AI
- Groq
- Mistral AI
- Together.ai
- Fireworks.ai
- DeepSeek
- SiliconFlow
- Zhipu AI (GLM / ChatGLM)
- Baichuan
- StepFun
- Alibaba (DashScope / Qwen)
- Baidu (ERNIE)
- Tencent (Hunyuan)
- iFlytek (Spark)
- 01.AI
- Cohere
- Perplexity
- Replicate
- Hugging Face Inference Endpoints
- Novita.ai
- Lepton AI
- Azure OpenAI
- AWS Bedrock (if possible via API or manual)
- Any custom OpenAI-compatible endpoint (user can add base URL + key)

For providers without public usage APIs, still include presets with:
- Manual balance entry
- Notes on how to copy-paste from their dashboard

## 5. Technical Stack

### Backend
- **Framework**: Python 3.11+ with FastAPI
- **API**: OpenAPI 3.1 (auto-generated from FastAPI, browsable at /docs)
- **Database**: SQLite with SQLAlchemy ORM
- **HTTP Client**: httpx (async)
- **Security**: API keys encrypted at rest using cryptography Fernet
- **Background Tasks**: FastAPI BackgroundTasks + APScheduler

### API Design (OpenAPI)
- RESTful endpoints for all CRUD operations
- Automatic OpenAPI schema generation
- Interactive API docs via Swagger UI at /docs
- ReDoc alternative at /redoc

### Frontend
- **Framework**: React 18 + TypeScript
- **Build Tool**: Vite
- **Styling**: TailwindCSS + shadcn/ui
- **Charts**: Recharts
- **State Management**: Zustand
- **HTTP Client**: Axios or fetch API

### Architecture
- **Web App** (not desktop) — runs locally in browser
- Backend runs as a local server (localhost:8000)
- Frontend served by FastAPI static files or separate Vite dev server
- 100% local — no cloud sync unless explicitly added later

## 6. Development Phases (Suggested)
1. Project setup (FastAPI backend + React frontend + SQLite).
2. Provider management + secure key storage.
3. Core usage fetcher system (abstract interface).
4. Implement 5–6 high-priority providers (xAI, Poe, OpenRouter, MiniMax, Kimi, OpenAI).
5. Dashboard UI + charts.
6. Add remaining providers + pricing tables.
7. Background refresh, alerts, export, polish.
8. Testing + documentation.

## 7. Deliverables
- Complete source code with excellent comments and README.
- Clear instructions on **how to add a new provider** (new Python module + pricing config).
- Setup scripts for running locally with FastAPI + React.
- Sample data / test mode.
- License: MIT (or whatever user prefers).

This spec should give the coding agent everything needed to build a production-ready, beautiful, and highly useful central usage dashboard. Feel free to ask the user for clarification on specific provider APIs or preferred tech choices.

**Ready to code!** 🚀



## Additional corpus / va passages naming this agent


### From `corpus/study/ai_agent_video_production_workflow.md` Copy: `sources/excerpts/ai_agent_video_production_workflow.md`.


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

```text
[Brief] ──► PlannerAgent ──► OrchestratorAgent ──► RouterAgent ──► (52 craft agents from §2.1–2.8)
                  ▲                  │                                       │
                  │                  ▼                                       ▼
              MemoryAgent      GateKeeperAgent ◄─── JudgeAgent ◄──── CritiqueMessages (§6)
                                     ▲                                       ▲
                                     │                                       │
             [Creative meta:] IdeationAgent · NarrativeArcAgent · StyleTransferAgent · MoodBoardAgent · NoveltyAgent · EmotionalArcAgent
             [Research meta:] WebResearchAgent · ArchiveResearchAgent · TrendIntelligenceAgent · CompetitorIntelligenceAgent · CitationAgent · InterviewSynthesisAgent · BenchmarkResearchAgent
             [Optimization meta:] PromptOptimizerAgent · CostOptimizerAgent · LatencyOptimizerAgent · RetentionOptimizerAgent · ROASOptimizerAgent · AccessibilityOptimizerAgent · EvaluationHarnessAgent · SafetyRedTeamAgent
```

| Phase | Primary outputs | Mandatory gates |
|---|---|---|
| **Greenlight** | Approved brief, KPI targets, budget envelope, rights-risk register, scale profile | ProducerAgent, FinanceAgent, ComplianceAgent, PlannerAgent |
| **Pre-production packet** | Script lock, storyboard/lookbook, asset IDs, character/world bibles, consent state, continuity baselines | DirectorAgent, ScreenwriterAgent, Asset/Data Backbone, Continuity checks |
| **Production packet** | Shot prompts, camera plans, performance refs, plates, generated takes, render telemetry | PromptEngineerAgent / GeneratorOperator, CinematographerAgent, AIQAConsistencyAgent |
| **Post master** | Timelines, graded masters, stems, captions/subtitles, QC reports, outlet variants | EditorAgent, ColoristAgent, SoundMixerAgent, Accessibility checks |
| **Review and release pack** | AudienceSim results, legal review, provenance bundle, sign-off log, unresolved-risk list | ComplianceAgent, JudgeAgent, HumanInTheLoop when required |
| **Distribution package** | DCP, streaming mezzanine, broadcast master, archive package, trailer/social cutdowns, metadata bundle | Delivery-spec validation, accessibility validation, territorial rights validation |
| **Post-launch learning set** | Performance telemetry, corrections, defect log, benchmark deltas, retraining tickets | AnalystAgent, EvaluationHarnessAgent, PromptOptimizerAgent, model-improvement loop |



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
| PromptEngineerAgent (#46) | Writes the expanded model-facing prompts + negative prompts per shot | Shot card, refs | Final prompts, seeds | Sora 2/Veo 3.1/Runway/Kling, seed registry | Target shot ≤3 iterations | AIQAConsistencyAgent |
| PromptOptimizerAgent (#73) | Auto-tunes weak prompts (OPRO/DSPy) when a shot fails QC | Failed prompt + score | Improved prompt | DSPy MIPRO, OPRO, eval harness | Score uplift per iteration | PromptEngineerAgent |
| CinematographerAgent (#6) | Lensing, lighting, composition (golden hour, shallow DoF) per shot | Shot intent | Lighting/lens spec | Veo camera-path, ACES pipeline | Composition + color-temp consistency | DirectorAgent, ColoristAgent |
| CameraOperatorAgent (#7) | Executes the push-ins, dolly, handheld breath moves | Lens spec | Camera-move presets | Runway camera presets, Kling motion | Frame steadiness, move smoothness | CinematographerAgent |
| TalentAgent (#26) | Renders the on-camera micro-performance (smiles, glances, pauses) | Character refs | Performance takes | HeyGen Avatar IV, emotion models | Emotion-target match | DirectorAgent |
| VoiceOverAgent (#21) | Performs the warm reflective 旁白 in ZH (+EN alt) | VO script | VO takes | ElevenLabs v3, pronunciation lexicon | Prosody + pronunciation match | DirectorAgent |
| VoiceCloneAgent (#48) | If a consistent narrator voice is cloned, handles cloning + consent | Consent + sample | Cloned VO, lip-sync | ElevenLabs cloning, Sync.so | MOS ≥4.2; consent verified | ComplianceAgent, LipSyncAgent |
| ComposerAgent (#20) | Minimalist piano + soft strings score with swells at peaks | Emotion curve | Score stems | Udio/Suno, MIDI, Demucs | Cue-to-emotion alignment | EditorAgent, SoundDesignAgent |
| SoundDesignAgent (#19) | Foley/ambience per scene (pencil, keyboard, soup, city hum) | Shot list | SFX stems | ElevenLabs SFX, Freesound | Sync ≤±1 frame | EditorAgent, ComposerAgent |



### From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


- **Prompt registry:** every agent system prompt is versioned (`prompt.vN.md`); the active version is referenced by `AgentConfig` and recorded in provenance (G5). Prompt changes go through PromptOptimizer (#73) eval before promotion.
- **Model registry:** pinned model+version per agent policy; upgrades are eval-gated (run golden L2/L3 before/after; no regression allowed).
- **Seed/LoRA/style registries:** StyleTransfer (#61) and gen agents reference versioned seeds/LoRAs/reference-frame banks for reproducibility and look-consistency.
- **Golden-set governance:** golden fixtures are frozen and reviewed; changing an expected output requires justification (it may indicate a rubric drift).
- **Aesthetic profiles:** consent-governed, versioned `AestheticProfile`s (per the Aesthetics Agent spec) stored and signed; audience-cohort profiles link to Psychological Recommendation.
- **Eval datasets:** VBench/EvalCrafter/MT-Bench/FVD/CLIP-T runners wrapped behind `EvalToolProvider`; benchmark baselines tracked over time by BenchmarkResearch (#72) + EvaluationHarness (#79).



### From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 73 | **PromptOptimizerAgent** | Auto-improves prompts via OPRO/APE/DSPy/Promptbreeder | OPRO (Yang 2023); APE (Zhou 2022); DSPy (Stanford); Promptbreeder (DeepMind) | Score uplift per iteration; convergence speed | Beats hand-tuned prompts on held-out briefs | PromptEngineerAgent, AIQAAgent | PromptEngineerAgent (sub-optimal seed) | DSPy framework (MIPRO optimizer); OPRO implementation; held-out eval harness | DSPy compilation + OPRO meta-optimization |
| 74 | **CostOptimizerAgent** | Routes between models/providers for $/quality | Provider pricing; cost-quality frontiers; FrugalGPT patterns | $/successful-task; Pareto distance from frontier | Lower $/quality than human CFO routing | RouterAgent, FinanceAgent | RouterAgent (over-spend), GeneratorAgent (re-roll burn) | Provider pricing APIs; benchmark cost DB; FrugalGPT cascade logic | ReAct (evaluate task → pick cheapest model meeting threshold) |
| 75 | **LatencyOptimizerAgent** | Parallelization, caching, speculative decoding, batching | vLLM; TensorRT-LLM; distillation; Anyscale/Ray | p50/p95 latency; throughput/GPU-hour | Lower p95 than human-tuned pipeline | OrchestratorAgent | OrchestratorAgent (serial bottleneck) | vLLM; TensorRT-LLM; Ray Serve; Redis (response cache); speculative decoding configs | Tool-use profiling + automated pipeline restructuring |
| 76 | **RetentionOptimizerAgent** | Tunes hook, pacing, structure for AVD/hold-rate | YouTube Analytics benchmarks; TikTok retention curves; AudienceSim | Predicted retention vs actual; AVD lift over control | Beats senior YouTube editor on AVD lift (A/B) | EditorAgent, AudienceSimAgent | EditorAgent (slow opener), ScriptwriterAgent (front fluff) | YouTube Analytics API; retention-curve predictor model; A/B test framework | RLAIF (reward = retention uplift from real analytics) |
| 77 | **ROASOptimizerAgent** | Optimizes ad creatives for performance | Meta Marketing Science; TikTok Ads Academy; MMM/MTA lit | ROAS uplift vs control; significance ≥95% | Beats senior marketer at equal budget | PerformanceMarketerAgent, AnalystAgent | UGCAgent (low hook), CopywriterAgent (weak CTA) | Meta Ads API (creative testing); TikTok Ads; Bayesian MMM tools (Robyn/Meridian) | RLAIF (reward = real ROAS from ad platform feedback) |
| 78 | **AccessibilityOptimizerAgent** | WCAG 2.2 contrast, captions, audio description, color-blind safe | WCAG 2.2; W3C/WAI-ARIA; DCMP captioning key; Deaf/HoH guidelines | Conformance 100% AA, ≥90% AAA; caption WER ≤2% | Catches more a11y defects than ADA-certified auditor | AccessibilityAgent (HiTL), ComplianceAgent | EditorAgent (caption sync), ColoristAgent (contrast) | axe-core/Lighthouse (contrast); Whisper v4 (captioning); audio-description generator | Constitutional AI (constitution = WCAG 2.2 success criteria) |
| 79 | **EvaluationHarnessAgent** | Runs benchmarks (VBench, EvalCrafter, MT-Bench, FVD, CLIP-T); posts regressions | Papers-with-Code; HuggingFace leaderboards; benchmark repos | Regression precision/recall; alert latency <1h | Catches regressions faster than ML-eng rotation | BenchmarkResearchAgent | All AI agents (regression alerts) | VBench suite; EvalCrafter; MT-Bench harness; CI/CD (GitHub Actions); alerting (PagerDuty) | Tool-use / ReAct (run benchmark → compare → alert if regressed) |
| 80 | **SafetyRedTeamAgent** | Adversarially attacks for deepfake, bias, jailbreak, defamation | Hany Farid benchmarks; Partnership on AI Framework; OWASP LLM Top 10 | Attack-success kept ≤1%; taxonomy coverage | Higher coverage than internal red-team rotation | EthicsAgent (HiTL), ComplianceAgent | AvatarDesignAgent, VoiceCloneAgent, AllGenerators | Deepfake detectors (Farid lab models); bias probes; jailbreak prompt banks; OWASP scanner | Multi-agent debate (red-team vs defender) + adversarial search |

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

| Standard | Purpose | Status (2026) |
|---|---|---|
| C2PA (Content Provenance) | Cryptographic manifest signing for every AI-generated artifact; platforms (YouTube, TikTok, Meta) auto-label | EU AI Act Code of Practice (March 2026) mandates C2PA + watermarking combined. Over 2,300 tools support. [contentauthenticity.org](https://contentauthenticity.org/blog/the-state-of-content-authenticity-in-2026) |
| MCP (Model Context Protocol) | Open standard for LLM ↔ tool integration; 2,300+ public servers; adopted by Claude, VS Code, Cursor, etc. | Donated to Agentic AI Foundation (Linux Foundation, Dec 2025) by Anthropic + OpenAI + Block. [modelcontextprotocol.io](https://modelcontextprotocol.io) |
| DSPy | Framework for programming (not prompting) LLMs; compiles declarative pipelines into optimized prompts/finetunes | Stanford-maintained; MIPRO optimizer; used by PromptOptimizerAgent for automated prompt improvement. [github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) |



### From `corpus/study/ui/backend_agent_management.md` Copy: `sources/excerpts/backend_agent_management.md`.


```text
Agent task fails (LLM error, tool timeout, quality below threshold)
    │
    ▼
RETRY LOGIC (in Orchestrator):
    │
    ├── Is retry_count < max_retries (default: 3)?
    │     YES → Re-queue with exponential backoff
    │           (wait 5s, then 15s, then 45s)
    │
    ├── Is it a transient error (API timeout, rate limit)?
    │     YES → Retry with same parameters
    │
    ├── Is it a quality failure (CLIP-T too low)?
    │     YES → Retry with PromptOptimizerAgent adjusting the prompt
    │
    ├── Is it a budget overrun?
    │     YES → Try with cheaper model (CostOptimizer fallback)
    │
    └── All retries exhausted?
          YES → Mark agent as FAILED
               → Notify user via WebSocket (red node on DAG)
               → User can: [Retry] [Skip] [Modify & Retry]
```



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

### 5.13 Prompt Lab (PromptEngineerAgent + PromptOptimizerAgent Interface)

Optimization Meta-Agents                     S21: Optimization Panel
  PromptOptimizerAgent                            S14: Prompt Lab (OPRO controls)
  CostOptimizerAgent                              S12: Budget Tracker + S13: Router Config
  LatencyOptimizerAgent                           Pipeline timing view
  RetentionOptimizerAgent                         Retention curve predictor
  ROASOptimizerAgent                              ROAS projection chart
  AccessibilityOptimizerAgent                     A11y compliance checklist
  EvaluationHarnessAgent                          S15: Quality Dashboard (benchmark runner)
  SafetyRedTeamAgent                              S18: Compliance → Red Team tab
```

```text
┌────────────────────────────────────────────┐
│  NOTIFICATIONS (3 unread)                  │
├────────────────────────────────────────────┤
│  🔴 Compliance: Voice consent expiring     │
│     2 min ago · [Resolve]                  │
│                                            │
│  🟡 Gate #3 ready for review               │
│     5 min ago · [Open Gate]                │
│                                            │
│  🟡 AIQAAgent: Hand artifact in Shot 2     │
│     8 min ago · [View Shot]                │
│                                            │
│  ── Read ─────────────────────────────     │
│  🔵 EditorAgent completed rough cut        │
│  🔵 PromptOptimizer improved CLIP-T +0.02  │
│  🔵 BudgetAgent: 42% spent                 │
└────────────────────────────────────────────┘
```



## Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


## Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


## Provenance

- Master roster row va_id=73 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `vendor/va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.promptoptimizer · va_id=73 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **PromptOptimizerAgent** (`video.promptoptimizer`, va_id=73, category `9-Meta`).

### Responsibility focus
Auto-improves prompts via OPRO/APE/DSPy/Promptbreeder

### Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: prompt optimization DSPy/OPRO, digital humans/avatars, personalization recommender systems, video consistency models, deepfake detection
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: prompt engineering video, AI avatars production, personalized video AI, consistency AI
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: prompting for video models, avatar video production, personalized video at scale, AI consistency checks

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

<!-- migration_capability_research · video.promptoptimizer · v1 · 2026-07-13 -->

### `sources/MAPPING.md`

# Mapping — `video.personalizationengineer`

- VA/generic pack ID: `video.personalizationengineer`
- Previous common ID: `video.refine_coordinator`
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
      "title": "\u8bbe\u8ba1\u5fc3\u7406\u5b66",
      "isbn13": "9787115417947",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8bbe\u8ba1\u5fc3\u7406\u5b66\uff0cISBN-13 9787115417947"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u70b9\u77f3\u6210\u91d1",
      "isbn13": "9787115249494",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u70b9\u77f3\u6210\u91d1\uff0cISBN-13 9787115249494"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u754c\u9762\u8bbe\u8ba1\u6a21\u5f0f",
      "isbn13": "9787115331861",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u754c\u9762\u8bbe\u8ba1\u6a21\u5f0f\uff0cISBN-13 9787115331861"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7528\u6237\u4f53\u9a8c\u8981\u7d20",
      "author": "\u52a0\u745e\u7279",
      "isbn13": "9787115325466",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7528\u6237\u4f53\u9a8c\u8981\u7d20\uff08\u52a0\u745e\u7279\uff09\uff0cISBN-13 9787115325466"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u8bbe\u8ba1\u4e2d\u7684\u8bbe\u8ba1",
      "author": "\u539f\u7814\u54c9",
      "isbn13": "9787549559787",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8bbe\u8ba1\u4e2d\u7684\u8bbe\u8ba1\uff08\u539f\u7814\u54c9\uff09\uff0cISBN-13 9787549559787"
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
      "title": "\u8fd9\u5c31\u662f\u8425\u9500",
      "isbn13": "9787521702330",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8fd9\u5c31\u662f\u8425\u9500\uff0cISBN-13 9787521702330"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u75af\u4f20",
      "isbn13": "9787508641238",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u75af\u4f20\uff0cISBN-13 9787508641238"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u8ba9\u521b\u610f\u66f4\u6709\u9ecf\u6027",
      "isbn13": "9787508641245",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8ba9\u521b\u610f\u66f4\u6709\u9ecf\u6027\uff0cISBN-13 9787508641245"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u8de8\u8d8a\u9e3f\u6c9f",
      "isbn13": "9787111456780",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8de8\u8d8a\u9e3f\u6c9f\uff0cISBN-13 9787111456780"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7cbe\u76ca\u521b\u4e1a",
      "isbn13": "9787115293701",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7cbe\u76ca\u521b\u4e1a\uff0cISBN-13 9787115293701"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u4e00\u4e2a\u5e7f\u544a\u4eba\u7684\u81ea\u767d",
      "isbn13": "9787111496182",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4e00\u4e2a\u5e7f\u544a\u4eba\u7684\u81ea\u767d\uff0cISBN-13 9787111496182"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6587\u6848\u8bad\u7ec3\u624b\u518c",
      "isbn13": "9787115351555",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6587\u6848\u8bad\u7ec3\u624b\u518c\uff0cISBN-13 9787115351555"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u4e0a\u763e",
      "isbn13": "9787508648017",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4e0a\u763e\uff0cISBN-13 9787508648017"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u589e\u957f\u9ed1\u5ba2",
      "isbn13": "9787213066948",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u589e\u957f\u9ed1\u5ba2\uff0cISBN-13 9787213066948"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u53c2\u4e0e\u611f",
      "isbn13": "9787213055375",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u53c2\u4e0e\u611f\uff0cISBN-13 9787213055375"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Artificial Intelligence: A Modern Approach, 4th ed.",
      "author": "Russell & Norvig",
      "isbn13": "9780134610993",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Artificial Intelligence: A Modern Approach, 4th ed. (Russell & Norvig), ISBN-13 9780134610993"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Multiagent Systems, 2nd ed.",
      "author": "Michael Wooldridge",
      "isbn13": "9780471496915",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Multiagent Systems, 2nd ed. (Michael Wooldridge), ISBN-13 9780471496915"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Deep Learning",
      "author": "Goodfellow, Bengio, Courville",
      "isbn13": "9780262035613",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Deep Learning (Goodfellow, Bengio, Courville), ISBN-13 9780262035613"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Hands-On Machine Learning, 3rd ed.",
      "author": "Aur\u00e9lien G\u00e9ron",
      "isbn13": "9781098125974",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Hands-On Machine Learning, 3rd ed. (Aur\u00e9lien G\u00e9ron), ISBN-13 9781098125974"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Reinforcement Learning, 2nd ed.",
      "author": "Sutton & Barto",
      "isbn13": "9780262039246",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Reinforcement Learning, 2nd ed. (Sutton & Barto), ISBN-13 9780262039246"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Speech and Language Processing, 2nd ed.",
      "author": "Jurafsky & Martin",
      "isbn13": "9780131873216",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Speech and Language Processing, 2nd ed. (Jurafsky & Martin), ISBN-13 9780131873216"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Introduction to Information Retrieval",
      "author": "Manning, Raghavan, Sch\u00fctze",
      "isbn13": "9780521865715",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Introduction to Information Retrieval (Manning, Raghavan, Sch\u00fctze), ISBN-13 9780521865715"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Designing Data-Intensive Applications",
      "author": "Martin Kleppmann",
      "isbn13": "9781449373320",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Designing Data-Intensive Applications (Martin Kleppmann), ISBN-13 9781449373320"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Human Compatible",
      "author": "Stuart Russell",
      "isbn13": "9780525558613",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Human Compatible (Stuart Russell), ISBN-13 9780525558613"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Alignment Problem",
      "author": "Brian Christian",
      "isbn13": "9780393635829",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Alignment Problem (Brian Christian), ISBN-13 9780393635829"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Superintelligence",
      "author": "Nick Bostrom",
      "isbn13": "9780199678112",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Superintelligence (Nick Bostrom), ISBN-13 9780199678112"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Weapons of Math Destruction",
      "author": "Cathy O'Neil",
      "isbn13": "9780553418811",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Weapons of Math Destruction (Cathy O'Neil), ISBN-13 9780553418811"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u4eba\u5de5\u667a\u80fd\uff1a\u4e00\u79cd\u73b0\u4ee3\u7684\u65b9\u6cd5",
      "author": "\u7b2c4\u7248",
      "isbn13": "9787111547044",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4eba\u5de5\u667a\u80fd\uff1a\u4e00\u79cd\u73b0\u4ee3\u7684\u65b9\u6cd5\uff08\u7b2c4\u7248\uff09\uff0cISBN-13 9787111547044"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6df1\u5ea6\u5b66\u4e60",
      "author": "\u82b1\u4e66",
      "isbn13": "9787115461476",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6df1\u5ea6\u5b66\u4e60\uff08\u82b1\u4e66\uff09\uff0cISBN-13 9787115461476"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u673a\u5668\u5b66\u4e60",
      "author": "\u5468\u5fd7\u534e",
      "isbn13": "9787302373575",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u673a\u5668\u5b66\u4e60\uff08\u5468\u5fd7\u534e\uff09\uff0cISBN-13 9787302373575"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7edf\u8ba1\u5b66\u4e60\u65b9\u6cd5",
      "author": "\u674e\u822a",
      "isbn13": "9787302423288",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7edf\u8ba1\u5b66\u4e60\u65b9\u6cd5\uff08\u674e\u822a\uff09\uff0cISBN-13 9787302423288"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5f3a\u5316\u5b66\u4e60",
      "author": "\u7b2c2\u7248",
      "isbn13": "9787115546081",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5f3a\u5316\u5b66\u4e60\uff08\u7b2c2\u7248\uff09\uff0cISBN-13 9787115546081"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u4fe1\u606f\u68c0\u7d22\u5bfc\u8bba",
      "isbn13": "9787115221704",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u4fe1\u606f\u68c0\u7d22\u5bfc\u8bba\uff0cISBN-13 9787115221704"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u6570\u636e\u5bc6\u96c6\u578b\u5e94\u7528\u7cfb\u7edf\u8bbe\u8ba1",
      "isbn13": "9787111547532",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u6570\u636e\u5bc6\u96c6\u578b\u5e94\u7528\u7cfb\u7edf\u8bbe\u8ba1\uff0cISBN-13 9787111547532"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u8d85\u7ea7\u667a\u80fd",
      "isbn13": "9787508663098",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u8d85\u7ea7\u667a\u80fd\uff0cISBN-13 9787508663098"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u751f\u547d3.0",
      "isbn13": "9787508684031",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u751f\u547d3.0\uff0cISBN-13 9787508684031"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u52a8\u624b\u5b66\u6df1\u5ea6\u5b66\u4e60",
      "author": "\u674e\u6c90\u7b49",
      "isbn13": "9787115547460",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u52a8\u624b\u5b66\u6df1\u5ea6\u5b66\u4e60\uff08\u674e\u6c90\u7b49\uff09\uff0cISBN-13 9787115547460"
    }
  ],
  "agent_id": "video.personalizationengineer",
  "previous_common_agent_id": "video.refine_coordinator",
  "va_taxonomy_aligned": true,
  "generic_source": "generic-swarm-ops/business/video/agents/video.personalizationengineer",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "aligned_at": "2026-07-27T00:48:11.273910Z",
  "generic_source_depth": {
    "excerpts": true,
    "study": true,
    "adopted_at": "2026-07-27T01:30:28.593428+00:00",
    "upstream": "generic-swarm-ops/business/video/agents"
  },
  "imported_from": "vendor/common-agent-swarm-ops/business/video/agents/video.personalizationengineer",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```

### `sources/RETHINK_100_APPLIED.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.personalizationengineer",
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
  "agent_id": "video.personalizationengineer",
  "sources": [
    {
      "id": "src_1",
      "title": "Idomoo case studies",
      "description": "Idomoo case studies",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.personalizationengineer",
      "status": "planned_or_partial"
    },
    {
      "id": "src_2",
      "title": "DMA campaigns",
      "description": "DMA campaigns",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.personalizationengineer",
      "status": "planned_or_partial"
    },
    {
      "id": "src_3",
      "title": "MarTech lit",
      "description": "MarTech lit",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.personalizationengineer",
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
