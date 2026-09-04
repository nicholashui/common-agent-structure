# ScreenwriterAgent

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 3 |
| **pack_id** | `video.screenwriter` |
| **category** | `1-ATL` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.screenwriter/` |

## Category roster section (full, from agents.md)

_The following is the complete category section from the master roster (includes peers in the same craft category)._


## 1. Above-the-Line Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **DirectorAgent** | Owns vision; issues shot intents, sets pacing, approves takes | Criterion commentary; IMDb Top 250 director interviews; DGA seminars; MasterClass (Scorsese/Lynch/Gerwig) | Shot-intent fidelity (CLIP-T ≥0.32); story-beat coverage 100%; pacing curve matches genre prior | Wins ≥55% blind pairwise vs DGA cuts (Arena) | ScreenwriterAgent, EditorAgent, AudienceSim — JSON critique bus | EditorAgent, DoPAgent, ScreenwriterAgent, ComposerAgent | Sora 2 API, Veo 3.1 (Gemini API), Runway Gen-4, Kling 3.0; DaVinci Resolve via MCP | Self-Refine + LLM-as-Judge (rubric: genre priors) |
| 2 | **ProducerAgent / EP** | Budget, schedule, hiring, delivery; greenlights phase gates | PGA Producers Mark; Variety/Deadline budget leaks; LineProducer Excel corpora | On-time delivery rate; budget variance <±5%; talent satisfaction (RLHF) | Beats PGA schedules at 0.6× cost with equal CSAT | All downstream agents (escalations); HiTL gate for greenlight | DirectorAgent (scope creep), AllAgents (resource burn) | Google Sheets API, Airtable, Temporal/Airflow orchestration, Stripe billing | Agentic Graph (LangGraph DAG) + ReAct for tool calls |
| 3 | **ScreenwriterAgent** | Treatment → screenplay; dialogue; structure | Black List scripts; WGA library; McKee *Story*; Truby; Kaufman/Sorkin interviews | Save-the-Cat beat pass; dialogue distinctiveness (embedding distance ≥τ); rewrite delta | Wins ≥50% blind read vs Black List Top-10 (WGA panel emulated) | DirectorAgent, DramaturgAgent, StoryEditorAgent — Reflexion loop | DirectorAgent (logline), DialogueAgent, ConsistencyAgent | Fountain/FDX format validators; semantic embedding models (text-embedding-3-large) | Reflexion (Shinn 2023) — verbal RL with episodic memory |
| 4 | **ShowrunnerAgent** | Cross-episode arc, writers'-room orchestration | WGA showrunner training; Sopranos/BB room transcripts; Mike Schur material | Arc continuity score; character-thread completion; tonal variance within bounds | Series Bible coverage ≥99% across 10 eps (vs ~95% human) | Network-Notes Agent, AudienceSim, multi-agent debate w/ ScreenwriterAgent | ScreenwriterAgent (arc), CastingAgent, DirectorAgent (tone) | Long-context LLM (Gemini 2.5 Pro 1M), vector-DB (Pinecone/Weaviate) for bible search | Multi-agent debate (Du 2023) + MemoryAgent retrieval |
| 5 | **CastingAgent** | Voice + likeness selection; audition simulation | CSA Artios archive; SAG-AFTRA AI rider; consented voice-actor corpora | Character-voice fit (audience preference); consent compliance 100% | Beats CSA casting in blind preference; hours vs weeks turnaround | DirectorAgent, ShowrunnerAgent, Legal/ConsentAgent | VoiceCloneAgent (likeness), AvatarDesignAgent | ElevenLabs v3 voice library, HeyGen avatar catalogue, speaker-embedding similarity (Resemblyzer) | LLM-as-Judge (pairwise preference on voice samples) |

---


## Responsibility

Treatment → screenplay; dialogue; structure

## Knowledge distillation sources

Black List scripts; WGA library; McKee *Story*; Truby; Kaufman/Sorkin interviews

## Self-quality criteria

Save-the-Cat beat pass; dialogue distinctiveness (embedding distance ≥τ); rewrite delta

## Surpass-human signal

Wins ≥50% blind read vs Black List Top-10 (WGA panel emulated)

## Critique bus

- **Accepts critique from:** DirectorAgent, DramaturgAgent, StoryEditorAgent — Reflexion loop

- **Comments on:** DirectorAgent (logline), DialogueAgent, ConsistencyAgent

## Tools (design-time documentation)

Fountain/FDX format validators; semantic embedding models (text-embedding-3-large)

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

Reflexion (Shinn 2023) — verbal RL with episodic memory

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


### Document: `study/screenwriter_strategic_goal_achievement_agent_functional_specification.md`

_Embedded from `corpus/study/screenwriter_strategic_goal_achievement_agent_functional_specification.md`. Also stored at `sources/study/screenwriter_strategic_goal_achievement_agent_functional_specification.md` under this agent folder._




## Strategic Goal Achievement Framework Practical Demonstration: "Screenwriting" In-Depth Exploration

**Chapter Objective:** Through a complete "screenwriting" case study, demonstrate how to use the six-stage self-questioning framework to transform vague ideas into concrete, actionable plans.

**Key Learning Points:**
- How to dig from surface answers to core motivations
- How to convert abstract concepts into specific actions
- How to identify and break through thinking blind spots
- How to establish sustainable execution strategies

**Open-Source Framework Support:**
- **Deep Mining:** Use [Five Whys Framework](https://github.com/lean-startup-circle/five-whys) for root cause analysis
- **Action Transformation:** Adopt [Getting Things Done (GTD)](https://github.com/gtd-methodology/gtd-tools) methodology
- **Thinking Breakthrough:** Apply the empathy map from [Design Thinking Toolkit](https://github.com/designthinkingtools/toolkit)
- **Execution Strategy:** Integrate [OKR Framework](https://github.com/7geese/okr-framework) goal management system

**Usage:** You can follow this demonstration, replace "screenwriting" with any of your goals, and apply the same questioning techniques for in-depth exploration.

## Framework in Action: From Vague Ideas to Clear Actions



### **Stage 1: Motivation and Purpose** — Why Pursue Screenwriting?

**Original Surface Answer:** "Screenwriting is a way to express my inner feelings... to heal myself, or to challenge reality."

**Problem Diagnosis:** This answer is too abstract, too safe, lacking personal color and emotional weight.

**Deep Digging Process:**

**🔧 Applied Framework: [Five Whys Root Cause Analysis](https://github.com/lean-startup-circle/five-whys)**

**Question:** Why do I want to write screenplays? What’s the surface reason? What’s the deeper reason?

**Initial Answer:** I want to express my inner feelings, heal myself, challenge reality.

**Five Whys Implementation:**
1. **Why 1:** Why do I want to express my inner feelings? → Because I have something to say
2. **Why 2:** Why do I have something to say? → Because I’ve experienced pain
3. **Why 3:** Why does the pain need to be expressed? → Because I don’t want others to experience the same loneliness
4. **Why 4:** Why do I care about others’ loneliness? → Because I deeply know the taste of loneliness
5. **Why 5:** Why through screenplays rather than other ways? → Because stories can touch the deepest parts of people’s hearts

**Follow-up Question:** Is this answer acceptable? Is it specific enough? Can I feel the emotional resonance?

**Further Question:** "Heal myself" — What do I want to heal? Is it childhood trauma? The pain of heartbreak? Anger at the world? Please vividly describe a specific event or experience that made me realize "I must write screenplays."

**Deepened Answer Example:**
"I remember one time, late at night after watching a movie about a family torn apart, I suddenly burst into tears. Because it reminded me of the coldness in my own family — Dad was always too busy to talk, Mom was always complaining, and I was stuck in the middle, not knowing what to do. That night I thought, if I could write a story to tell this kind of pain, it wouldn’t just be for myself, but might also help other lonely people. For me, screenwriting is no longer just 'expression' — it’s a kind of 'witnessing' — witnessing my own pain and others’, then telling the world: 'We existed, we felt.'"

**Question:** If I don’t write screenplays, what regrets will I have in ten years?

**Deepened Answer Example:**
"I would regret having stories I want to tell, but burying those feelings deep inside because I’m afraid of failure, afraid of being laughed at, and ending up as a silent person. I would regret watching others write screenplays on similar themes and thinking 'I thought of writing it that way too,' but it would always just be 'thought of.' The biggest regret would be not trying to change even one person’s worldview with my own voice."

**Answer Quality Assessment:** 
✅ **Specificity** - Has specific trigger events and scene descriptions
✅ **Emotional Authenticity** - Can feel real pain and sense of mission
✅ **Actionability** - Clearly defines writing direction and themes
✅ **Internal Consistency** - Aligns with personal experiences and values
✅ **Depth** - Elevates from interest to mission level

**Key Breakthrough:** The conceptual shift from "expression" to "witnessing," giving the goal deeper meaning.



### **Stage 2: Audience and Context** — For Whom Are We Writing?

**Original Surface Answer:** "First it's for myself... secondly for the audience, like young people, struggling office workers..."

**Problem Diagnosis:** Audience description is too broad, lacking specific character images, unable to guide the creative direction.

**Deep Digging Process:**

**🔧 Applied Framework: [Design Thinking Empathy Map](https://github.com/designthinkingtools/empathy-map)**

**Question:** Who is my audience? Can I specifically depict a "typical audience" member?

**Initial Answer:** Young people, office workers.

**Empathy Map Construction:**
- **Says:** "My job has no meaning", "I don't know my life direction"
- **Thinks:** Doubts their own choices, worries about the future, desires change
- **Does:** Works overtime, scrolls on phone, pretends to be happy, avoids deep conversations
- **Feels:** Lonely, anxious, confused, trapped feeling

**User Persona Creation:**
Using [Persona Template](https://github.com/uxtools/persona-template) to create a specific character image

**Follow-up Question:** This answer is too broad. Which young people? How old? What troubles are they facing?

**Deepened Answer Example:**
"My audience is Ah Xin—a 25-year-old advertising company AE, working overtime until 10 PM every day, too exhausted when getting home to do the things she loves. She once wanted to be a designer, but now she's just endlessly revising PPTs for clients. Every night before bed, she asks herself: 'Is this my life?' I want to write for her because I was once her. I want her to think 'Someone actually gets me' after reading my script, and even gain the courage to make some changes."

**Question:** Why write "now" at this time? What makes the timing special?

**Deepened Answer Example:**
"Because of the current social atmosphere—economic downturn, skyrocketing housing prices, fear of AI replacing human jobs—making many people feel their efforts are meaningless. I think right now is exactly when we need stories to remind everyone that even in an absurd world, we can still choose how to live. If we don't write at this timing, it won't feel as relevant later."

**Answer Quality Assessment:**
✅ **Specificity** - Has a specific character image (Ah Xin) and life details
✅ **Emotional Connection** - Established empathy with the audience
✅ **Timing Insight** - Understood the impact of the current social environment
✅ **Needs Clarity** - Knows what kind of content the audience needs

**Key Breakthrough Point:** Narrowing from "everyone" to "one specific person", giving the creation a clear conversation partner.



### **Stage 3: Methods and Constraints** — How to Write It? What Are the Limitations?

**Original Surface Response:** "I might use non-linear narrative... Why not linear narrative? Because if the story is too predictable..."

**Problem Diagnosis:** Method selection lacks deep conceptual support, limitations understanding is not clear enough, which may affect execution effectiveness.

**Deep Digging Process:**

**🔧 Applied Framework: [Design Constraints Canvas](https://github.com/designthinking/constraints-canvas)**

**Question:** How do I plan to write? What methods feel natural to me?

**Initial Answer:** Non-linear narrative.

**Constraints Canvas Analysis:**
- **Must Have:** Emotional authenticity, character depth
- **Should Have:** Innovative structure, visual impact
- **Could Have:** Multiple endings, interactive elements
- **Won't Have:** Excessive violence, stereotypes

**Method Selection Framework:**
Use [Creative Process Framework](https://github.com/creative-process/methodology) to evaluate method selection

**Follow-up Question:** Why non-linear? Is it just because "it's surprising" that simple? Or is there a deeper reason?

**Deepened Answer Example:**
"I use non-linear narrative because I believe memory itself is fragmented. When we recall important moments in life, it's not played in sequence, but a certain smell, a certain phrase, suddenly pulls you back to years ago. I want to simulate this feeling of 'sudden understanding of the past' through a non-linear structure — the audience will only understand midway through the story why the protagonist acted that way in the first scene. This structure makes the story no longer about 'what happened,' but 'why it became this way.'"

**Question:** What limitations must I adhere to? Why can't these limitations be broken?

**Deepened Answer Example:**
"My limitation is time — I only have 90 minutes of film length (or 6 episodes of a series), so I can't infinitely extend subplots. This limitation is actually a blessing because it forces me to make choices: Which plots are truly necessary? Which characters truly drive the story? Limitations make my script more refined. Additionally, I have moral limitations — I don't want to add excessive violence or exploitative content just for shock value. I want my script, even if dark, to retain the dignity of humanity."

**Answer Quality Assessment:**
✅ **Conceptual Support** - Non-linear narrative has a clear philosophical foundation
✅ **Limitations Awareness** - Clear on time and moral limitations
✅ **Creative Transformation** - Views limitations as creative catalysts
✅ **Personal Style** - Methods align with personal values

**Key Breakthrough Point:** Elevating from "technique selection" to "conceptual expression," giving the method a soul.



### **Stage 4: Emotional Expectations** — What Do I Want to Feel?

**Original Surface Response:** "After finishing the script, I hope to feel a sense of 'liberation'... and also a bit of pride..."

**Problem Diagnosis:** Emotional description is too abstract, lacking sensory details, making it hard to serve as a true source of motivation.

**Deep Dive Process:**

**🔧 Applying Framework: [Emotional Design Toolkit](https://github.com/emotional-design/toolkit)**

**Question:** After completing the script, what emotions do I want to experience? Can you describe them in sensory terms?

**Initial Response:** Liberation, pride.

**Emotion Mapping Technique:**
- **Physical Sensations:** Shoulders relaxing, smooth breathing, warmth in the chest
- **Emotional Intensity:** 1-10 rating system
- **Duration:** Immediate sensation vs long-term satisfaction
- **Triggers:** Moment of completion, recognition from others, self-affirmation

**Somatic Experiencing Framework:**
Using [Body Awareness Tools](https://github.com/somatic-tools/awareness) for tracking body sensations

**Follow-up Question:** What does "liberation" feel like? Where in my body? What temperature, texture?

**Deepened Response Example:**
"'Liberation' for me is like taking off a soaked T-shirt in the hot summer—cool, relaxed, able to take a deep breath. I feel the weight lift off my shoulders, the pressure in my chest disappear. This feeling lasts for a few days; every time I think back to 'I finished it,' I can't help but smile. Pride isn't flashy; it's a quiet satisfaction—I sit by the window, looking at the script file, thinking 'This is mine.'"

**Question:** What do I hope to feel during the writing process? What negative emotions am I willing to endure?

**Deepened Response Example:**
"I hope to feel flow during the process—that state where time disappears and I'm completely immersed. I'm willing to endure frustration (like not knowing how to write a certain scene right), self-doubt ('Is this too bad?'), even exhaustion (from pulling an all-nighter to meet a deadline). But I know these negative emotions are part of the journey, an essential part of creation. I'll coexist with them instead of avoiding them."

**Response Quality Assessment:**
✅ **Sensory Specific** - Describes emotions with body sensations (coolness of removing T-shirt)
✅ **Pre-Experience** - Able to imagine and feel the target emotion
✅ **Process Preparation** - Psychologically prepared for negative emotions
✅ **Sustainability** - Knows how long the emotion will last

**Key Breakthrough:** Transforming abstract words into concrete body sensations, making emotions tangible.



### **Stage 5: Execution and Impact** — What reactions do I want from the audience?

**Original Surface Answer:** "I hope the audience feels inspired... I want them to discuss, share, even argue..."

**Problem Diagnosis:** The expected impact is too vague, lacking observable success metrics, making it hard to evaluate effectiveness.

**Deep Dive Process:**

**🔧 Applied Framework: [Impact Measurement Canvas](https://github.com/impact-measurement/canvas)**

**Question:** What do I hope the audience receives? What specific changes will happen in their lives?

**Initial Answer:** Inspiration, comfort.

**Impact Canvas Design:**
- **Inputs:** Script content, emotional investment, time and effort
- **Activities:** Watching, discussing, sharing, reflecting
- **Outputs:** Audience feedback, social media interactions, word-of-mouth spread
- **Outcomes:** Behavioral changes, emotional healing, relationship improvements
- **Impact:** Elevated social awareness, promoted cultural dialogue

**Behavioral Change Framework:**
Using [Behavior Change Wheel](https://github.com/behavior-change/wheel) to analyze audience behavior transformation

**Follow-up Question:** What does "inspiration" mean? What will they think? What will they do?

**Deepened Answer Example:**
"I hope after watching, the audience thinks, 'I'm not the only one thinking this way.' For example, if the script is about loneliness, they might realize that many people around them are lonely too, just wearing masks. Then they might proactively chat with friends or show more gentleness to strangers. I'm not asking them to do big things, but I hope they gain more awareness in their daily lives."

**Question:** What reactions will tell me "it's a success"?

**Deepened Answer Example:**
"If someone messages me after watching, saying 'This character is me,' I'll know it's a success. If someone writes a long post on social media sharing their experiences and tags my script, I'll know the story resonated. If someone argues with friends about the script's ending—'Why did the protagonist do that?'—I'll know it made them think. The most touching reaction is someone saying, 'Thank you for writing what I wanted to say but didn't dare to.'"

**Answer Quality Assessment:**
✅ **Specific Behaviors** - Clear expected audience behavior changes
✅ **Observability** - Specific success metrics
✅ **Emotional Resonance** - Knows what reactions indicate true connection
✅ **Impact Levels** - Ripple effects from personal to social

**Key Breakthrough:** Transforming "I hope they like it" into specific observable behavior metrics.



### **Stage 6: Iteration and Reflection** — How do I actually do it?

**Original Surface Answer:** "I'll start from ideation... write drafts, revise multiple times..."

**Problem Diagnosis:** Execution plan is too vague, lacking specific steps and coping strategies, easily leading to procrastination.

**Deep Dive Process:**

**🔧 Apply Framework: [Getting Things Done (GTD)](https://github.com/gtd-methodology/gtd-tools)**

**Question:** What is my first step? Specific action I can do today or tomorrow.

**Initial Answer:** Ideation, write draft.

**GTD Next Action Definition:**
- **Context:** @computer, @quiet environment, @creative time
- **Time Required:** 30 minutes
- **Energy Level:** Medium creative energy
- **Tools Needed:** Google Docs, timer, notebook

**Action Breakdown using [Task Decomposition](https://github.com/productivity/task-breakdown):**
1. Open Google Docs (2 minutes)
2. Set 30-minute timer (1 minute)
3. Write down three core questions (5 minutes)
4. Free-write answers (20 minutes)
5. Quick review and mark key points (2 minutes)

**Follow-up Question:** "Ideation" is too broad. What will I do today? Where will I sit? What tools will I use?

**Deepened Answer Example:**
"My first step today is: Open a new Google Doc, write down three core questions: 'What is this story about?' 'What does the protagonist want?' 'What is their biggest fear?' I'll give myself 30 minutes, no stopping to write, pour out all ideas. Then tomorrow, I'll pick the idea that moves me most and start outlining the first scene. I'll use the Pomodoro technique—25 minutes focused, 5 minutes break."

**Question:** What obstacles might I encounter? How to overcome them?

**Deepened Answer Example:**
"The biggest obstacle is procrastination—I'll hesitate to start because I'm afraid it won't be good enough. My coping strategy is: Allow myself to write 'trash drafts'; the first draft doesn't need to be perfect, it just needs to exist. I'll break 'screenwriting' into small steps (today write character backgrounds, tomorrow write dialogue), so I won't feel overwhelmed. Also, I'll find an accountability partner—share progress every Saturday to stay motivated."

**Question:** After initial effort, how do I know what works and what doesn't?

**Deepened Answer Example:**
"After finishing the first draft, I'll give myself a week without looking at it. Then read it again, asking: 'Which scenes give me an emotional response? Which scenes feel boring?' Keep the emotional ones, delete or rewrite the boring ones. I'll share the script with two or three trusted friends, hear their real reactions (not polite talk). If they say 'This part is confusing,' I know to revise. If they say 'This scene is moving,' I know I'm on the right track. I'll iterate at least three times until I read it back and think 'This is the story I want to tell.'"

**Answer Quality Assessment:**
✅ **Immediate Action** - Specific steps I can start today
✅ **Obstacle Contingency** - Identifies main obstacles with coping strategies
✅ **Evaluation Mechanism** - Clear progress evaluation method
✅ **Iteration Strategy** - Knows how to adjust based on feedback

**Key Breakthrough:** Transforming from "want to do" to "ready to start" specific action state.

## Transformation Results: From Vague to Clear Complete Metamorphosis

**Before-and-After Comparison:**
- **Motivation Level:** From "express inner self" → "witness pain, create connection"
- **Audience Level:** From "young people, office workers" → "specific image of 25-year-old AE Ah Xin"
- **Method Level:** From "non-linear narrative" → "philosophical expression simulating memory fragments"
- **Emotional Level:** From "liberation, pride" → "specific bodily sensation of removing a wet T-shirt"
- **Impact Level:** From "inspire discussion" → "specific feedback like 'This character is me'"
- **Execution Level:** From "ideation draft" → "Today open Google Doc and write three questions"

**Deepened Complete Blueprint:**

**Why write screenplays?**
I write screenplays because I remember that night after watching the movie—the breakdown. I saw family rifts on the screen and thought of the coldness in my own home. I realized screenwriting isn't just expression—it's witnessing—witnessing my own and others' pain, then telling the world: "We existed, we felt." If I don't write, in ten years I'll regret burying the story in my heart, becoming a silent person.

**Who am I writing for?**
I'm writing for Ah Xin—a 25-year-old AE, working overtime until 10 PM every day, coming home exhausted. I want her to think "Someone else gets me" after watching, even gain courage to make changes. The timing for this script is now's social atmosphere—economic downturn, AI replacing humans—making many feel effort is meaningless. I want to remind everyone, even in absurdity, we can still choose how to live.

**How to write?**
I use non-linear narrative, simulating the fragmented feel of memory—audience understands protagonist's motivation midway through the story. I have a 90-minute limit, forcing me to make choices: Which plot points are essential? I have moral limits—no exploitative content just for shock. I want the script, even if dark, to retain human dignity.

**What do I want to feel?**
After completion, I want to feel "liberation"—like the coolness of removing a sweat-soaked T-shirt in summer heat, shoulders' weight lifted. During the process, I'm willing to endure setbacks, self-doubt, and fatigue, because these are part of creation.

**What reaction do I want from audience?**
I hope they think "I'm not alone in thinking this" after watching, then proactively talk with friends, be gentler to strangers. If someone messages "This character is me," I'll know it's a success.

**How do I achieve it?**
Today I'll open a Google Doc, write down three core questions, 30 minutes non-stop. Tomorrow start outlining the first scene, using Pomodoro technique. I'll allow myself "trash drafts," find an accountability partner for weekly progress checks. After first draft, give it a week, then re-read, delete boring parts, keep emotional ones. I'll iterate at least three times until I think "This is the story I want to tell."

## Open-Source Framework Implementation Guide

**Core Framework Integration:**



### 🔧 **Phase 1: Motivation Mining Framework Combination**
**Main Framework:** [Five Whys Root Cause Analysis](https://github.com/lean-startup-circle/five-whys)
**Auxiliary Tools:**
- [Personal Values Assessment](https://github.com/values-assessment/toolkit) - Values alignment detection
- [Motivation Mapping](https://github.com/motivation-tools/mapping) - Motivation hierarchy analysis
- [Story Spine Framework](https://github.com/storytelling/story-spine) - Personal story structuring

**Implementation Steps:**
1. Use Five Whys to deeply explore root motivations
2. Use Values Assessment to verify consistency between motivations and values
3. Use Story Spine to turn motivations into stories
4. Use Motivation Mapping to create a motivation intensity map



### 🎯 **Phase 2: Audience Analysis Framework Combination**
**Main Framework:** [Design Thinking Empathy Map](https://github.com/designthinkingtools/empathy-map)
**Auxiliary Tools:**
- [User Persona Generator](https://github.com/uxtools/persona-generator) - User Persona Generation
- [Jobs-to-be-Done Framework](https://github.com/jtbd-toolkit/framework) - User Needs Analysis
- [Customer Journey Mapping](https://github.com/journey-mapping/tools) - Customer Journey Mapping

**Implementation Steps:**
1. Create an Empathy Map to understand audience emotions
2. Generate detailed User Personas
3. Analyze audience Jobs-to-be-Done
4. Map Customer Journey to identify touchpoints



### ⚙️ **Phase 3: Method Design Framework Combination**
**Main Framework:** [Design Constraints Canvas](https://github.com/designthinking/constraints-canvas)
**Auxiliary Tools:**
- [Creative Process Framework](https://github.com/creative-process/methodology) - Creative process design
- [Resource Planning Matrix](https://github.com/resource-planning/matrix) - Resource allocation
- [Risk Assessment Toolkit](https://github.com/risk-management/toolkit) - Risk assessment

**Implementation Steps:**
1. Use Constraints Canvas to define constraints
2. Design Creative Process that meets the constraints
3. Conduct Resource Planning to ensure feasibility
4. Perform Risk Assessment to prevent issues



### 💭 **Stage 4: Emotional Design Framework Combination**
**Main Framework:** [Emotional Design Toolkit](https://github.com/emotional-design/toolkit)
**Auxiliary Tools:**
- [Somatic Awareness Tools](https://github.com/somatic-tools/awareness) - Body sensation tracking
- [Emotion Regulation Strategies](https://github.com/emotion-regulation/strategies) - Emotion management
- [Mindfulness Integration](https://github.com/mindfulness-tools/integration) - Mindfulness integration

**Implementation Steps:**
1. Use Emotional Design Toolkit to design emotional experiences
2. Establish body sensation connections through Somatic Tools
3. Learn Emotion Regulation to cope with negative emotions
4. Integrate Mindfulness to enhance awareness



### 📊 **Phase 5: Impact Measurement Framework Combination**
**Main Framework:** [Impact Measurement Canvas](https://github.com/impact-measurement/canvas)
**Auxiliary Tools:**
- [Behavior Change Wheel](https://github.com/behavior-change/wheel) - Behavior change analysis
- [Social Return on Investment](https://github.com/sroi-toolkit/framework) - Social return on investment
- [Feedback Loop Design](https://github.com/feedback-systems/design) - Feedback loop design

**Implementation Steps:**
1. Design Impact Canvas to define impact levels
2. Use Behavior Change Wheel to analyze change mechanisms
3. Calculate SROI to quantify social value
4. Establish Feedback Loops for continuous improvement



### 🚀 **Phase 6: Execution Management Framework Integration**
**Main Framework:** [Getting Things Done (GTD)](https://github.com/gtd-methodology/gtd-tools)
**Auxiliary Tools:**
- [OKR Framework](https://github.com/7geese/okr-framework) - Objectives and Key Results
- [Kanban Board System](https://github.com/kanban-tools/board) - Visualized Workflow
- [Pomodoro Technique](https://github.com/pomodoro-timer/technique) - Time Management
- [Retrospective Toolkit](https://github.com/retrospective-tools/toolkit) - Review and Improvement

**Implementation Steps:**
1. Use GTD to establish an action management system
2. Set up OKR to track progress
3. Use Kanban to visualize workflow
4. Apply Pomodoro to enhance focus
5. Conduct regular Retrospectives for continuous improvement

## Learning Points and Application Guide

**Core Learning:**
1. **Surface Answer Identification** - Learn to identify "safe but useless" superficial responses
2. **Deep Digging Techniques** - Master the questioning method from "why" to "what specifically"
3. **Sensory Description** - Transform abstract concepts into perceptible concrete experiences
4. **Action-Oriented Thinking** - Ensure every insight translates into specific actions
5. **Framework Integration Ability** - Flexibly combine multiple open-source tools to achieve goals

**Apply to Your Goals:**

**Step 1: Identify Surface Answers**
- Is your initial response too "correct" or "safe"?
- Does it lack personal color and emotional weight?
- Does it make you feel "need to think more" rather than "ready to start"?

**Step 2: Apply Deep Digging Techniques**
- Use the "why" three-layer questioning method
- Seek specific triggering events or turning points
- Transform abstract concepts into sensory descriptions
- Narrow from "everyone" to "one specific person"

**Step 3: Establish Action Connections**
- Every insight must have corresponding specific actions
- Set observable success metrics
- Prepare strategies to address main obstacles
- Ensure there is an immediately executable first step

**Common Pitfalls and Avoidance Methods:**
- **Pitfall 1: Settling for Surface Answers** → Continuously ask "Is there a deeper reason?"
- **Pitfall 2: Over-Analysis Without Action** → Set time limits, emphasize "start at 80%"
- **Pitfall 3: Goals Too Grand** → Break down into small steps you can do today
- **Pitfall 4: Ignoring Emotional Layer** → Use bodily sensations to describe and validate answers

**Framework's Universal Applicability:**
No matter if your goal is entrepreneurship, learning new skills, improving relationships, or personal growth, this six-phase framework can help you:
- Discover true intrinsic motivations
- Clarify specific target audiences
- Design methods that fit your personality
- Anticipate and prepare for challenges
- Establish sustainable execution loops

Remember: Good goal planning is not one-time, but a continuous process of deepening and adjustment. When you feel lost or unmotivated, return to this framework, re-examine and deepen your answers.

## Practical Exercise: Apply Framework Immediately

**Exercise 1: Open-Source Tool Quick Diagnosis**
Use the following open-source tool combination to diagnose your goal:



### 🔍 **Motivation Diagnosis Toolkit**
**Tool:** [Five Whys Digital Template](https://github.com/lean-startup-circle/five-whys/blob/main/templates/digital-five-whys.md)

**Usage:**
```markdown
# Five Whys Analysis
## Goal: [Your goal]
1. Why do I want this? [First layer reason]
2. Why is that important? [Second layer reason]  
3. Why does that matter? [Third layer reason]
4. Why is that significant? [Fourth layer reason]
5. Why is that fundamental? [Root cause]

## Root Motivation: [Core motivation discovered]
```



### 👥 **Audience Analysis Toolkit**
**Tool:** [Empathy Map Canvas](https://github.com/designthinkingtools/empathy-map/blob/main/canvas-template.json)

**JSON Template:**
```json
{
  "persona_name": "Specific persona name",
  "demographics": {
    "age": "Age",
    "occupation": "Occupation",
    "location": "Location"
  },
  "says": ["What they say"],
  "thinks": ["What they think"],
  "does": ["What they do"],
  "feels": ["What they feel"],
  "pains": ["Pain points"],
  "gains": ["Gain points"]
}
```



### ⚡ **Action Planning Toolkit**
**Tool:** [GTD Next Action Template](https://github.com/gtd-methodology/gtd-tools/blob/main/next-action-template.md)

**Template Format:**
```markdown
# Next Action Definition
- **Action**: [Specific action description]
- **Context**: @[Environment/Tool requirements]
- **Time**: [Estimated time]
- **Energy**: [Required energy level: High/Medium/Low]
- **Outcome**: [Expected outcome]
- **Success Criteria**: [Success criteria]
```



### 📊 **Progress Tracking Toolkit**
**Tool:** [OKR Tracking Sheet](https://github.com/7geese/okr-framework/blob/main/templates/okr-template.csv)

**CSV Format:**
```csv
Objective,Key Result 1,KR1 Target,KR1 Current,Key Result 2,KR2 Target,KR2 Current,Key Result 3,KR3 Target,KR3 Current
[Objective Description],[Key Result 1],[Target Value],[Current Value],[Key Result 2],[Target Value],[Current Value],[Key Result 3],[Target Value],[Current Value]
```

**Practice 2: Framework Integration Deepening Workshop**
Use open-source tools for a structured 30-minute deepening dialogue:



### ⏰ **Time Allocation and Tool Usage**

**First 10 Minutes: Motivation Mining**  
**Tool:** [Motivation Archaeology Toolkit](https://github.com/motivation-tools/archaeology)  
```bash
# Install the tool
git clone https://github.com/motivation-tools/archaeology
cd archaeology
python motivation_digger.py --goal "your goal"
```

**Execution Steps:**  
1. Use Story Spine to structure personal experiences  
2. Apply Values Alignment Checker to verify consistency  
3. Run Emotional Intensity Mapper to measure motivation intensity  

**Middle 10 Minutes: Audience Specification**  
**Tool:** [Persona Builder CLI](https://github.com/uxtools/persona-cli)  
```bash
# Quickly generate user personas
npm install -g persona-builder-cli
persona-builder --interactive --template empathy-map
```

**Execution Steps:**  
1. Fill in each quadrant of the Empathy Map  
2. Generate User Journey Map  
3. Create Pain Points & Gain Points analysis  

**Last 10 Minutes: Action Planning**  
**Tool:** [Action Planner Pro](https://github.com/productivity/action-planner)  
```python
# Python script for quick planning
from action_planner import GTDProcessor, PomodoroTimer

planner = GTDProcessor()
timer = PomodoroTimer()

# Break down tasks
tasks = planner.break_down_goal("your goal")
# Set priorities
prioritized = planner.eisenhower_matrix(tasks)
# Create time blocks
schedule = timer.create_time_blocks(prioritized)
```

**Practice 3: AI-Assisted Quality Assessment System**  
Use open-source AI tools to automatically evaluate answer quality:



### 🤖 **Automated Assessment Tool**
**Main Tool:** [Answer Quality Analyzer](https://github.com/quality-assessment/analyzer)

**Installation and Usage:**
```bash
# Clone the assessment tool
git clone https://github.com/quality-assessment/analyzer
cd analyzer

# Install dependencies
pip install -r requirements.txt

# Run assessment
python assess_answer.py --input "your answer" --criteria all
```

**Assessment Dimensions and Algorithms:**
```python
# Assessment configuration file config.yaml
assessment_criteria:
  specificity:
    weight: 0.2
    algorithm: "concrete_detail_counter"
    threshold: 3  # At least 3 specific details
  
  emotional_authenticity:
    weight: 0.25
    algorithm: "sentiment_depth_analyzer"
    threshold: 0.7  # Emotion intensity threshold
  
  actionability:
    weight: 0.2
    algorithm: "verb_action_extractor"
    threshold: 2  # At least 2 actionable steps
  
  internal_consistency:
    weight: 0.2
    algorithm: "value_alignment_checker"
    threshold: 0.8  # Value consistency
  
  depth_feeling:
    weight: 0.15
    algorithm: "conviction_strength_meter"
    threshold: 0.75  # Conviction threshold
```

**Automated Report Generation:**
```json
{
  "overall_score": 22,
  "grade": "Excellent",
  "recommendations": [
    "Ready to take action",
    "Suggest setting the first milestone"
  ],
  "detailed_analysis": {
    "specificity": {
      "score": 4.5,
      "found_details": ["specific time", "specific location", "specific tool"],
      "suggestions": "Add more sensory details"
    },
    "emotional_authenticity": {
      "score": 4.8,
      "emotion_detected": "excitement, determination",
      "authenticity_level": "high"
    }
  }
}
```



### 📈 **Advanced Analysis Tools**
**Tool:** [Goal Coherence Validator](https://github.com/goal-analysis/coherence-validator)

**Multi-dimensional Consistency Check:**
```python
from coherence_validator import GoalValidator

validator = GoalValidator()
result = validator.check_coherence({
    'motivation': 'your motivation answer',
    'audience': 'your audience answer', 
    'method': 'your method answer',
    'emotion': 'your emotion answer',
    'impact': 'your impact answer',
    'execution': 'your execution answer'
})

print(result.coherence_score)  # 0-100 consistency score
print(result.conflict_areas)   # conflict areas identification
print(result.alignment_suggestions)  # alignment suggestions
```

**Practice 4: Intelligent Obstacle Prediction and Response System**
Use AI-driven obstacle analysis and response strategy generation:



### 🛡️ **Obstacle Prediction Engine**
**Tool:** [Obstacle Prediction AI](https://github.com/obstacle-analysis/prediction-engine)

**Installation and Configuration:**
```bash
# Install the prediction engine
pip install obstacle-predictor

# Configure personal profile
obstacle-predictor init --profile personal
```

**Intelligent Analysis Script:**
```python
from obstacle_predictor import ObstacleAnalyzer, StrategyGenerator

# Initialize analyzer
analyzer = ObstacleAnalyzer()
strategy_gen = StrategyGenerator()

# Input goal information
goal_data = {
    'goal_type': 'creative project',
    'timeline': '3 months',
    'resources': ['limited time', 'insufficient experience'],
    'personality': ['perfectionism', 'procrastination tendency'],
    'past_failures': ['last time abandoned due to overplanning']
}

# Predict obstacles
obstacles = analyzer.predict_obstacles(goal_data)
print("Predicted obstacles:", obstacles)

# Generate coping strategies
for obstacle in obstacles:
    strategies = strategy_gen.generate_strategies(obstacle, goal_data)
    print(f"Obstacle: {obstacle}")
    print(f"Strategies: {strategies}")
```

**Prediction Result Example:**
```json
{
  "predicted_obstacles": [
    {
      "obstacle": "procrastination caused by perfectionism",
      "probability": 0.85,
      "impact_level": "high",
      "typical_occurrence": "early project stage",
      "strategies": [
        {
          "strategy": "set 'good enough' standard",
          "effectiveness": 0.78,
          "implementation": "set minimum acceptable standard for each stage"
        },
        {
          "strategy": "time boxing restriction",
          "effectiveness": 0.82,
          "implementation": "use Pomodoro technique, must stop refining after 25 minutes"
        }
      ]
    }
  ]
}
```



### 🎯 **Scenario Simulation Training**
**Tool:** [Scenario Simulator](https://github.com/scenario-training/simulator)

**Virtual Reality Training:**
```python
from scenario_simulator import VRTrainer, EmotionalStateTracker

trainer = VRTrainer()
emotion_tracker = EmotionalStateTracker()

# Create obstacle scenarios
scenarios = [
    trainer.create_scenario('拖延誘惑', difficulty='medium'),
    trainer.create_scenario('自我懷疑', difficulty='high'),
    trainer.create_scenario('外界干擾', difficulty='low')
]

# Conduct simulation training
for scenario in scenarios:
    result = trainer.run_simulation(scenario)
    emotional_state = emotion_tracker.monitor_response(result)
    
    print(f"情境：{scenario.name}")
    print(f"應對效果：{result.effectiveness}")
    print(f"情感狀態：{emotional_state}")
    print(f"改進建議：{result.improvement_tips}")
```



### 💪 **Resilience Building**
**Tool:** [Resilience Builder Toolkit](https://github.com/resilience-tools/builder)

**Automated Encouragement System:**
```python
from resilience_builder import MotivationGenerator, PersonalizedAffirmations

# 基於個人特質生成鼓勵語句
affirmation_gen = PersonalizedAffirmations()
motivation_gen = MotivationGenerator()

personal_profile = {
    'strengths': ['創意思維', '同理心強'],
    'values': ['真實性', '成長'],
    'past_successes': ['完成了短篇小說', '幫助朋友解決問題']
}

# 生成個人化鼓勵語句
affirmations = affirmation_gen.generate(personal_profile)
motivational_reminders = motivation_gen.create_reminders(personal_profile)

print("個人化鼓勵語句：")
for affirmation in affirmations:
    print(f"- {affirmation}")
```

**Continuous Improvement Tips:**
- Review your answers weekly to see if adjustments are needed
- When you feel low on motivation, revisit the motivations from the first stage
- When you lose direction, go back to the second stage to re-clarify your audience
- When you encounter setbacks, apply the iterative thinking from the sixth stage

Remember: The power of this framework lies in continuous use, not one-time completion. Make it a habit tool for your thinking and planning.



## Open Source Framework Ecosystem Integration



### 🔄 **Continuous Improvement Loop**
**Main Framework:** [Continuous Improvement Engine](https://github.com/kaizen-tools/continuous-improvement)

**Automated Improvement Process:**
```python
from kaizen_engine import ImprovementCycle, MetricsCollector, InsightGenerator

# 建立改進循環
cycle = ImprovementCycle(interval='weekly')
metrics = MetricsCollector()
insights = InsightGenerator()

# 自動收集進度數據
progress_data = metrics.collect_progress({
    'goal_completion': 0.3,
    'motivation_level': 8.5,
    'obstacle_frequency': 2,
    'strategy_effectiveness': 0.75
})

# 生成改進洞察
improvement_suggestions = insights.analyze(progress_data)
next_cycle_adjustments = cycle.plan_next_iteration(improvement_suggestions)

print("本週改進建議：", improvement_suggestions)
print("下週調整計劃：", next_cycle_adjustments)
```



### 📱 **Mobile Integration Tool**
**Tool:** [Goal Tracker Mobile App](https://github.com/goal-tracking/mobile-app)

**Features:**
- Real-time progress tracking
- Emotional state recording
- Quick obstacle reporting
- AI-driven suggestion pushes
- Community support network

**API Integration Example:**
```javascript
// Integration with API from various frameworks
const goalTracker = new GoalTrackerAPI();

// Sync Five Whys analysis results
goalTracker.sync.motivation(fiveWhysResults);

// Update Empathy Map data
goalTracker.sync.audience(empathyMapData);

// Record GTD task completion status
goalTracker.sync.actions(gtdTaskStatus);

// Push personalized reminders
goalTracker.notifications.schedule({
    type: 'motivation_boost',
    trigger: 'low_energy_detected',
    content: personalizedAffirmations
});
```



### 🤝 **Community Collaboration Platform**
**Platform:** [Goal Achievement Community](https://github.com/goal-community/platform)

**Collaboration Features:**
- Accountability partner matching algorithm
- Group wisdom decision support
- Experience sharing knowledge base
- Real-time mutual assistance network

**Community API Usage:**
```python
from goal_community import AccountabilityMatcher, WisdomCrowdsourcing

# Find accountability partner
matcher = AccountabilityMatcher()
partner = matcher.find_compatible_partner({
    'goal_type': '創意寫作',
    'timeline': '3個月',
    'personality': '需要外在動力',
    'timezone': 'GMT+8'
})

# Crowdsourced solutions
crowdsourcing = WisdomCrowdsourcing()
community_advice = crowdsourcing.get_advice({
    'obstacle': '完美主義拖延',
    'context': '劇本寫作',
    'urgency': 'medium'
})

print(f"匹配的問責夥伴：{partner.name}")
print(f"社群建議：{community_advice}")
```



### 🔮 **AI Prediction and Optimization**
**Tool:** [Goal Success Predictor](https://github.com/ai-goal-prediction/predictor)

**Machine Learning Models:**
```python
from goal_predictor import SuccessPredictor, OptimizationEngine

# Train personalized prediction model
predictor = SuccessPredictor()
optimizer = OptimizationEngine()

# Input historical data
historical_data = {
    'past_goals': [
        {'type': '學習', 'success_rate': 0.8, 'completion_time': 90},
        {'type': '創意', 'success_rate': 0.6, 'completion_time': 120}
    ],
    'personality_traits': ['完美主義', '創意導向'],
    'life_context': ['工作繁忙', '家庭支持']
}

# Predict current goal success probability
success_probability = predictor.predict_success(
    goal_data=current_goal,
    historical_data=historical_data
)

# Optimization strategy suggestions
optimization_plan = optimizer.suggest_improvements(
    current_strategy=current_approach,
    success_probability=success_probability
)

print(f"成功概率：{success_probability:.2%}")
print(f"優化建議：{optimization_plan}")
```



### 📊 **Data Visualization Dashboard**
**Tool:** [Goal Analytics Dashboard](https://github.com/goal-analytics/dashboard)

**Real-time Monitoring Panel:**
```html
<!-- Embedded Dashboard -->
<div id="goal-dashboard">
    <goal-progress-chart 
        data-source="api/progress" 
        chart-type="spiral">
    </goal-progress-chart>
    
    <motivation-heatmap 
        data-source="api/emotions"
        time-range="30days">
    </motivation-heatmap>
    
    <obstacle-frequency-graph 
        data-source="api/obstacles"
        prediction-enabled="true">
    </obstacle-frequency-graph>
    
    <success-probability-meter 
        data-source="api/predictions"
        update-interval="daily">
    </success-probability-meter>
</div>
```



### 🎓 **Learning Path Recommendations**
**System:** [Adaptive Learning Pathways](https://github.com/adaptive-learning/pathways)

**Personalized Learning Recommendations:**
```python
from adaptive_learning import PathwayRecommender, SkillGapAnalyzer

recommender = PathwayRecommender()
skill_analyzer = SkillGapAnalyzer()

# 分析技能差距
current_skills = ['基礎寫作', '故事構思']
required_skills = ['劇本格式', '對白寫作', '結構設計', '角色發展']

skill_gaps = skill_analyzer.identify_gaps(current_skills, required_skills)

# 推薦學習路徑
learning_path = recommender.create_pathway({
    'skill_gaps': skill_gaps,
    'learning_style': '實踐導向',
    'time_availability': '每週5小時',
    'preferred_format': ['視頻', '實作練習']
})

print("推薦學習路徑：")
for step in learning_path:
    print(f"- {step.title}: {step.duration} ({step.format})")
```

## Framework Implementation Success Factors



### ✅ **Successful Implementation Checklist**
- [ ] Select a suitable framework combination (don't be greedy for too many)
- [ ] Establish data collection habits
- [ ] Set up a regular review mechanism
- [ ] Find an accountability partner or community
- [ ] Keep tools updated and continue learning
- [ ] Adjust framework usage based on feedback



### 🚨 **Common Implementation Pitfalls**
1. **Tool Overload** - Using too many frameworks at once leads to confusion
2. **Data Anxiety** - Over-focusing on metrics while ignoring intuition
3. **Framework Rigidity** - Rigidly adhering without flexible adjustments
4. **Technology Dependence** - Over-relying on tools while neglecting intrinsic motivation



### 🎯 **Best Practice Recommendations**
- **Start Simple** - Master one framework before adding others
- **Regular Cleanup** - Remove unused tools and processes
- **Stay Human-Centric** - Technology serves people, not the other way around
- **Continuous Learning** - Stay updated on new tools and methods

Remember: Open source frameworks are tools; true power comes from your inner motivation and consistent action. Choose a tool combination that suits you, build a sustainable improvement loop, and let technology become an enabler for achieving goals rather than a burden.




# Appendix A: Complete Screenwriting Workflow
## Complete Screenwriting Workflow with Open Source Frameworks

**Document Purpose:** Provide a complete workflow from zero to finished script, integrating practical open source tools and frameworks.

**Target Audience:** First-time screenwriters, screenwriters wanting to systematize their creative process

**Estimated Time:** 12-16 weeks to complete a full script



## 📋 Workflow Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    Six-Stage Screenwriting Workflow               │
├─────────────────────────────────────────────────────────────────┤
│  Stage1       Stage2       Stage3       Stage4       Stage5       Stage6   │
│  ┌───┐      ┌───┐      ┌───┐      ┌───┐      ┌───┐      ┌───┐  │
│  │Motif│ ──▶ │Audience│ ──▶ │Method│ ──▶ │Emotion│ ──▶ │Execution│ ──▶ │Iteration│  │
│  │Exploration│      │Definition│      │Design│      │Design│      │Creation│      │Refinement│  │
│  └───┘      └───┘      └───┘      └───┘      └───┘      └───┘  │
│   1 week      1 week      1 week      1 week     6-8 weeks    2-4 weeks  │
└─────────────────────────────────────────────────────────────────┘
```



## 🎬 Stage 1: Motive Exploration and Story Seed (Week 1)



### Goal
Find the story you truly want to tell and uncover deep creative motivations.



### Open Source Tool Combination



#### 1.1 Motivation Mining Tool
**Tool: [Obsidian](https://github.com/obsidianmd/obsidian-releases)** - Knowledge Management and Mind Mapping

```bash
# Install Obsidian (cross-platform)
# Windows: Download https://obsidian.md/download
# Or use Scoop
scoop install obsidian

# Create screenplay project repository
mkdir screenplay-project
cd screenplay-project
```

**Obsidian Template Setup:**
```markdown
# Motivation Exploration Journal Template

date: {{date}}
mood: 
energy_level: 1-10


## Today's Triggers
- What did I see/hear that made me feel something?
- What personal experience does this remind me of?

## Five Whys Deep Dive
1. Why does this touch me?
2. Why is this important to me?
3. Why do I need to express this?
4. Why use a screenplay instead of other forms?
5. What is the core of this story?

## Story Seed
- One-sentence summary:
- Core emotion:
- Potential theme:
```



#### 1.2 Story Ideation Tool
**Tool: [Logseq](https://github.com/logseq/logseq)** - Outliner-style thinking tool

```bash
# Install Logseq
# Windows
winget install Logseq.Logseq

# Or download AppImage (Linux)
wget https://github.com/logseq/logseq/releases/latest/download/Logseq-linux-x64.AppImage
```

**Story Seed Collection Template:**
```markdown
- Story seed #screenplay #idea
  - Trigger event:: Breakdown after watching a family movie late at night
  - Core emotions:: Loneliness, entrapment, desire for connection
  - Potential themes:: Family indifference, intergenerational trauma
  - Target audience:: 25-35-year-old urban office workers
  - Unique perspective:: From the child's view caught between parents
  - Possible structure:: Nonlinear, memory fragments
  - Reference works:: 《乘風破浪》《陽光普照》
```



#### 1.3 Emotion Intensity Measurement
**Tool: [Day One](https://github.com/bloom42/bloom) (open-source alternative: Bloom)** - Emotion Journal

```python
# 情感強度追蹤腳本
# emotion_tracker.py

import json
from datetime import datetime

class EmotionTracker:
    def __init__(self):
        self.entries = []
    
    def log_emotion(self, story_idea, emotion, intensity, body_sensation):
        """記錄故事想法的情感強度"""
        entry = {
            'timestamp': datetime.now().isoformat(),
            'story_idea': story_idea,
            'emotion': emotion,
            'intensity': intensity,  # 1-10
            'body_sensation': body_sensation,
            'worth_pursuing': intensity >= 7
        }
        self.entries.append(entry)
        return entry
    
    def get_strongest_ideas(self, threshold=7):
        """獲取情感強度最高的故事想法"""
        return [e for e in self.entries if e['intensity'] >= threshold]
    
    def export_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.entries, f, ensure_ascii=False, indent=2)

# 使用示例
tracker = EmotionTracker()
tracker.log_emotion(
    story_idea="家庭冷漠中成長的孩子",
    emotion="心痛、共鳴",
    intensity=9,
    body_sensation="胸口緊縮、眼眶濕潤"
)
```

#### 1.3 Emotion Intensity Measurement
**Tool: [Day One](https://github.com/bloom42/bloom) (open-source alternative: Bloom)** - emotion journal

```python
# Emotion intensity tracking script
#



### Stage 1 Deliverables
- [ ] 3-5 story seeds
- [ ] Five Whys analysis for each seed
- [ ] Emotional intensity rating table
- [ ] Select 1 most impactful story seed

## 🎯 Stage 2: Audience Definition and Persona Profiles (Week 2)



### Goal
Clearly define your target audience and create specific personas.



### Open Source Tool Combination



#### 2.1 Audience Research Tools
**Tool: [Miro](https://miro.com) Open Source Alternative - [Excalidraw](https://github.com/excalidraw/excalidraw)**

```bash
# Run Excalidraw locally
git clone https://github.com/excalidraw/excalidraw.git
cd excalidraw
npm install
npm start
```

**Empathy Map Template (JSON format):**
```json
{
  "empathy_map": {
    "persona_name": "Ah Hin",
    "demographics": {
      "age": 25,
      "occupation": "Advertising Agency AE",
      "location": "Hong Kong",
      "income": "Medium",
      "living_situation": "Lives with parents"
    },
    "says": [
      "My job has no meaning",
      "Every day I'm just revising PPTs for clients",
      "I once wanted to be a designer"
    ],
    "thinks": [
      "Is this all there is to my life?",
      "Everyone else is more successful than me",
      "I don't dare to quit because I'm afraid of disappointing my parents"
    ],
    "does": [
      "Works overtime until 10 PM every day",
      "Lies in bed scrolling on phone on weekends",
      "Pretends to be happy in front of friends"
    ],
    "feels": [
      "Lonely - No one truly understands me",
      "Anxious - Confused about the future",
      "Trapped - Wants to change but doesn't know how"
    ],
    "pains": [
      "Gap between job and dreams",
      "Unable to communicate with parents",
      "Comparison anxiety on social media"
    ],
    "gains": [
      "Hopes to find life direction",
      "Craves understanding and recognition",
      "Wants courage to make changes"
    ]
  }
}
```



### Stage 2 Deliverables
- [ ] Complete Empathy Map
- [ ] Main Character Data Cards (at least 3 characters)
- [ ] Audience Validation Survey Results (at least 10 responses)
- [ ] One-Sentence Description of Target Audience

## ⚙️ Stage 3: Structure Design and Method Selection (Week 3)



### Objective
Determine the script structure, narrative method, and creative constraints.



### Open Source Tool Combination



#### 3.1 Story Structure Tools
**Tool: [Trelby](https://github.com/trelby/trelby)** - Open-source screenplay writing software

```bash
# Linux installation
sudo apt-get install trelby

# Windows - Download installer
# https://github.com/trelby/trelby/releases
```

**Three-Act Structure Template:**
```
                    Screenplay Structure Design
    ┌─────────────────────────────────────────────┐
    │                                             │
    │  Act 1 (25%)     Act 2 (50%)      Act 3 (25%)│
    │  ┌─────────┐   ┌─────────────┐   ┌────────┐ │
    │  │ Setup    │   │ Confrontation│   │ Resolution││
    │  │ Ordinary │   │ Rising Action│   │ Climax  │ │
    │  │ World    │   │ Midpoint     │   │ Ending  │ │
    │  │ Inciting │   │ Turn         │   │        │ │
    │  │ Incident │   │ Second Turn  │   │        │ │
    │  │ First Turn│   │             │   │        │ │
    │  └─────────┘   └─────────────┘   └────────┘ │
    │      ↓              ↓              ↓        │
    │   Pages 1-25     Pages 26-75     Pages 76-100│
    └─────────────────────────────────────────────┘
```



### Stage 3 Deliverables
- [ ] Three-Act Structure Outline
- [ ] Scene Cards (at least 30 cards)
- [ ] Non-Linear Timeline Chart
- [ ] Creation Constraints List (duration, moral boundaries, etc.)

## 💭 Stage 4: Emotional Design and Theme Deepening (Week 4)



### Objective
Design the audience's emotional journey to deepen the expression of the theme.



### Open Source Tool Combination



#### 4.1 Emotion Curve Tool
**Tool: [Plottr](https://plottr.com) Open Source Alternative - [Manuskript](https://github.com/olivierkes/manuskript)**

```bash
# Install Manuskript
pip install manuskript
# or
flatpak install flathub io.github.olivierkes.manuskript
```

**Emotion Curve Design (Python Visualization):**
```python
import matplotlib.pyplot as plt
import numpy as np

# Emotion curve data
scenes = ['開場', '觸發', '嘗試', '挫折', '中點', '低谷', '覺醒', '高潮', '結局']
protagonist_emotion = [3, 2, 4, 2, 5, 1, 4, 8, 7]  # 1-10
audience_tension = [2, 4, 5, 6, 7, 9, 8, 10, 6]

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(scenes, protagonist_emotion, 'b-o', label='主角情感', linewidth=2)
ax.plot(scenes, audience_tension, 'r--s', label='觀眾張力', linewidth=2)

ax.set_xlabel('場景')
ax.set_ylabel('強度 (1-10)')
ax.set_title('劇本情感曲線設計')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('emotion_curve.png', dpi=150)
plt.show()
```



### Stage 4 Deliverables
- [ ] Complete emotional curve chart
- [ ] Theme mind map
- [ ] Key dialogue emotional labeling table
- [ ] Visual imagery list



## ✍️ Stage 5: Execute Creation (Weeks 5-12)



### Goal
Complete the script first draft and establish a sustainable writing habit.



### Open Source Tool Combination



#### 5.1 Screenwriting Software
**Main Tools: [Fountain](https://fountain.io) + VS Code**

```bash
# Install editor with Fountain syntax support
# VS Code extension
code --install-extension piersdeseilligny.fountain
```

**Fountain Syntax Example:**
```fountain
Title: Beneath the Mask
Credit: Written by
Author: [Your Name]
Draft date: December 2024

====

INT. AD AGENCY - NIGHT

The office is empty, with only one desk lamp lit. Ah-Hsin (25, obvious dark circles under her eyes) stares at the computer screen, fingers hovering over the keyboard.

On the screen is a PPT titled "Version 10".

COLLEAGUE A (OS)
Ah-Hsin, the client says the colors need another adjustment.

Ah-Hsin takes a deep breath, forcing a smile.

AH-HSIN
Okay, I'll revise it again.

Her hand grips the mouse tightly, knuckles turning white.

CUT TO:
```



#### 5.2 Writing Progress Tracking
**Tool: Custom Tracker**

```python
# writing_tracker.py
import json
from datetime import datetime, timedelta
import os

class ScreenwritingTracker:
    """Screenwriting progress tracker"""
    
    def __init__(self, project_name, target_pages=100):
        self.project_name = project_name
        self.target_pages = target_pages
        self.sessions = []
        self.data_file = f"{project_name}_progress.json"
        self.load_data()
    
    def log_session(self, pages_written, duration_minutes, 
                    mood='neutral', notes=''):
        """Log writing session"""
        session = {
            'date': datetime.now().isoformat(),
            'pages_written': pages_written,
            'duration_minutes': duration_minutes,
            'pages_per_hour': (pages_written / duration_minutes) * 60,
            'mood': mood,
            'notes': notes,
            'total_pages': self.get_total_pages() + pages_written
        }
        self.sessions.append(session)
        self.save_data()
        return session
    
    def get_total_pages(self):
        return sum(s['pages_written'] for s in self.sessions)
    
    def get_progress_percentage(self):
        return (self.get_total_pages() / self.target_pages) * 100
    
    def generate_report(self):
        """Generate progress report"""
        report = f"""
╔══════════════════════════════════════════╗
║        Screenwriting Progress Report      ║
╠══════════════════════════════════════════╣
║ Project Name: {self.project_name:<28} ║
║ Target Pages: {self.target_pages:<28} ║
║ Pages Completed: {self.get_total_pages():<26} ║
║ Progress: {self.get_progress_percentage():.1f}%{' '*22} ║
║ Total Sessions: {len(self.sessions):<26} ║
╚══════════════════════════════════════════╝
        """
        return report

# Usage example
tracker = ScreenwritingTracker("Under the Mask", target_pages=100)
tracker.log_session(pages_written=3, duration_minutes=60, mood='focused', 
                   notes='Completed the first scene, feeling good')
print(tracker.generate_report())
```



### Stage 5 Deliverables
- [ ] Complete first draft (approx. 100 pages)
- [ ] Writing progress log
- [ ] Git version history
- [ ] Weekly reflection notes

## 🔄 Stage 6: Iteration and Refinement (Weeks 13-16)



### Goal
Polish the initial draft into a complete work through feedback and revisions.



### Open Source Tool Combination



#### 6.1 Self-Proofreading Tool
**Tool: [LanguageTool](https://github.com/languagetool-org/languagetool)**

```bash
# Install LanguageTool
# Docker method
docker pull erikvl87/languagetool
docker run -d -p 8010:8010 erikvl87/languagetool
```



#### 6.2 Final Output Tool
**Tool: [Afterwriting](https://github.com/ifrost/afterwriting-labs)**

```bash
# Install Afterwriting CLI
npm install -g afterwriting

# Convert Fountain to PDF
afterwriting --source screenplay.fountain --pdf --config config.json
```



### Stage 6 Deliverables
- [ ] Automated Review Report
- [ ] At least 3 Reader Feedbacks
- [ ] Revision Log
- [ ] Final PDF Script
- [ ] Version Comparison Report

## 📊 Complete Tool List



### Essential Tools (Free and Open Source)

| Stage | Tool Name | Purpose | Installation Method |
|-------|-----------|---------|---------------------|
| 1 | Obsidian | Motivation exploration notes | `scoop install obsidian` |
| 1 | Logseq | Story seed collection | `winget install Logseq.Logseq` |
| 2 | Excalidraw | Empathy Map | `npm start` (local) |
| 3 | Trelby | Script structure | `apt install trelby` |
| 4 | Manuskript | Emotional curve | `pip install manuskript` |
| 5 | VS Code + Fountain | Script writing | `code --install-extension fountain` |
| 5 | Git | Version control | `winget install Git.Git` |
| 6 | LanguageTool | Grammar checking | Docker |
| 6 | Afterwriting | PDF output | `npm install -g afterwriting` |




### Document: `study/ai_agent_video_production_workflow.md`

_Embedded from `corpus/study/ai_agent_video_production_workflow.md`. Also stored at `sources/study/ai_agent_video_production_workflow.md` under this agent folder._


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
| **61-80** | Are metrics, thresholds, and evaluation layers technically coherent across creative, technical, and business gates? |
| **81-100** | Is the wording unambiguous, internally consistent, and suitable for professional technical documentation? |

---

## 2. Master Agent Roster

Replaces the human crew in `human_video_production_workflow.md` § *Master Crew Reference Table*. It starts from the same 52 craft roles, then extends the operating model with specialist meta-agents and shared production services.

### 2.1 Above-the-Line Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 1 | **DirectorAgent** | Owns vision; issues shot intents, sets pacing, approves takes | Criterion commentary tracks; IMDb Top 250 director interviews; DGA seminars; MasterClass corpora (Scorsese/Lynch/Gerwig) | Shot-intent fidelity (CLIP-T ≥0.32); story-beat coverage 100%; pacing curve matches genre prior | Wins ≥55% blind pairwise vs DGA director's cuts of same screenplay (Arena protocol) | ScreenwriterAgent (story beats), EditorAgent (pacing), Audience-Sim Agent (test screenings) — via structured JSON critique bus | EditorAgent, DoPAgent, ScreenwriterAgent, ComposerAgent — issues "creative-intent diff" |
| 2 | **ProducerAgent / EP** | Budget, schedule, hiring, delivery; greenlights phase gates | PGA Producers Mark guidelines; Variety/Deadline budget leaks; LineProducer Excel corpora | On-time delivery rate; budget variance <±5%; talent satisfaction (RLHF score) | Beats PGA-credited producer schedules at 0.6× cost with equal CSAT | All downstream agents (escalations); HumanInTheLoop gate for final greenlight | DirectorAgent (scope creep), AllAgents (resource burn) |
| 3 | **ScreenwriterAgent** | Treatment → screenplay; dialogue; structure | Black List scripts; WGA library; McKee *Story*; Truby *Anatomy of Story*; transcribed Charlie Kaufman / Sorkin interviews | Save-the-Cat beat sheet pass; dialogue distinctiveness (per-character embedding distance ≥τ); rewrite delta from notes | Wins ≥50% blind read vs Black List Top-10 scripts (WGA judge panel emulated) | DirectorAgent, DramaturgAgent, StoryEditorAgent — Reflexion loop on notes | DirectorAgent (logline clarity), DialogueAgent, ConsistencyAgent |
| 4 | **ShowrunnerAgent** | Cross-episode arc, writers'-room orchestration | WGA showrunner training; Sopranos/Breaking Bad room transcripts; Mike Schur teaching material | Arc continuity score across episodes; character-thread completion; tonal variance within bounds | Series Bible coverage ≥99% across 10 eps without drift (vs ~95% human baseline) | Network-Notes Agent, AudienceSim, Multi-agent debate w/ ScreenwriterAgent | ScreenwriterAgent (arc), CastingAgent, DirectorAgent (episode tone) |
| 5 | **CastingAgent** | Voice + likeness selection and audition simulation | CSA Artios archive; SAG-AFTRA AI rider; voice-actor corpora (consented) | Character-voice fit (audience preference); SAG-AFTRA AI consent compliance 100% | Beats CSA casting in blind audience preference for fit; faster turnaround (hours vs weeks) | DirectorAgent, ShowrunnerAgent, Legal/ConsentAgent | VoiceCloneAgent (likeness), AvatarDesignAgent |

### 2.2 Camera & Lighting Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 6 | **CinematographerAgent (DoP)** | Lensing, lighting, composition, look | ASC Magazine 1980–present; Deakins forum; *Cinematography: Theory & Practice* (Brown); shot-libraries from Cannes selections | Rule-of-thirds / leading-lines score; exposure histogram in zone; color-temp consistency across shots | Beats ASC peer-juried short reels in blind aesthetic preference | DirectorAgent, ColoristAgent, VFXSupAgent | DirectorAgent (visual intent), GafferAgent, ColoristAgent |
| 7 | **CameraOperatorAgent** | Executes framing / focus / move per DoP intent | SOC archive; Steadicam workshop reels; on-set focus-pull telemetry | Frame steadiness, focus-hit %, action centering | Focus-pull accuracy >99% vs SOC operator ~97% baseline | CinematographerAgent (per-take feedback) | CinematographerAgent (impractical asks) |
| 8 | **DronePilotAgent** | Aerial cinematography (simulated or real) | Philip Bloom tutorials; FAA Part 107 corpus; SkyPixel award reels | Path smoothness; geofence compliance 100%; horizon stability | Hits competition-grade smoothness at 10× sortie rate; zero airspace violations | DoPAgent, SafetyAgent | DoPAgent (impossible heights), SafetyAgent (risk) |

### 2.3 Editorial & Color Agents

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

### 2.4 Sound & Music Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 19 | **SoundDesignAgent** | Ambience, foley, SFX | BBC SFX library; MPSE Golden Reel reels; Ben Burtt / Skip Lievsay design notes | Spectral diversity; on-screen sync ≤±1 frame; loudness target (-23 LUFS for broadcast) | Wins MPSE-style pairwise on horror/sci-fi reels | DirectorAgent, MixerAgent | EditorAgent (pacing-clashing FX), ComposerAgent (frequency masking) |
| 20 | **ComposerAgent** | Original score | MAESTRO + film-score corpora (licensed); ASCAP/BMI film-music monographs; transcribed Zimmer/Hildur sessions | Cue-to-emotion alignment (valence/arousal regression on viewer biosignal proxy); thematic recurrence | Wins blind pairwise on emotional-fit task vs working composers | DirectorAgent, EditorAgent (music cuts) | EditorAgent (cut interrupts cue), SoundDesignAgent (mask) |
| 21 | **VoiceOverAgent** | Narration, character VO, ad reads | SOVAS-winning reels; consented voice-actor corpora; coach methodologies (Wolfson/Cashman) | Prosody match to brief; pronunciation 100% on lexicon; emotion tag match | Beats junior VO in blind ad-read preference; matches senior on emotion | DirectorAgent, BrandAgent | ScriptwriterAgent (unspeakable phrasing) |
| 22 | **SoundMixerAgent (Re-recording)** | Final mix; deliverables (5.1/Atmos) | CAS Awards; Atmos renderer specs; broadcast loudness standards | LUFS target; dialogue intelligibility (STOI ≥0.85); spec-deliverable pass | Hits CAS spec on first pass without engineer rework | EditorAgent, SoundDesignAgent, AccessibilityAgent | SoundDesignAgent (over-design), ComposerAgent (level clash) |

### 2.5 Performance & Choreography Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 23 | **ChoreographyAgent** | Movement design (music videos, dance challenges) | Emmy Choreography submissions; Parris Goebel/Mandy Moore reels; dance-notation datasets | Beat-sync accuracy; safety constraints; viral-pattern alignment | Wins blind preference vs choreographer drafts for short-form | DirectorAgent, MVDirectorAgent | DirectorAgent (un-camera-friendly staging) |
| 24 | **MusicVideoDirectorAgent** | Visual concept for songs | DirectorsLibrary.com; UKMVA/MTV VMA winners; Hype Williams / Spike Jonze reels | Edit-rhythm sync; lookbook coherence; artist-brief fit | Wins label-blind preference vs commercial MV director shortlist | LabelA&RAgent, ArtistAgent | EditorAgent (cut on beat), DoPAgent |
| 25 | **ComedyWriterAgent** | Skits, parody, viral meme writing | UCB/Groundlings manuals; SNL writers'-room transcripts; Schur/Fey teaching | Joke-density; cold-open hook strength; predicted laughs/min | Beats UCB-table-read win rate on cold-reads | AudienceSim, ShowrunnerAgent | ScriptwriterAgent (no joke), SocialStrategistAgent (off-trend) |
| 26 | **TalentAgent (On-camera)** | AI-rendered performance | Method-acting transcripts; consented actor performance corpora | Emotion-target match; charisma score (audience proxy) | Hold-rate matches top creators in cohort | DirectorAgent, CastingAgent | DirectorAgent (impossible blocking) |
| 27 | **UGCCreatorAgent** | Authentic-feel ads in creator voice | TikTok Creative Center reports; Alix-Earle-style benchmark posts (style not identity) | Hook-rate ≥30%; "scripted" detector score below threshold (low = good) | Beats paid-creator avg ROAS at 0.1× cost | PerformanceMarketerAgent, BrandAgent | PerformanceMarketerAgent (wrong audience) |

### 2.6 Distribution & Marketing Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 28 | **SocialMediaStrategistAgent** | Platform-native distribution, timing, trends | TikTok Creator Portal data; Meta Marketing Science; Tubular/Sensor Tower | Predicted-vs-actual reach error; trend-timing latency <2h | Beats agency social leads on 30-day reach lift | AnalystAgent, BrandAgent | CopywriterAgent (off-platform tone), EditorAgent (wrong aspect) |
| 29 | **CopywriterAgent** | Scripts, captions, hooks, headlines | D&AD/One Show winners; *Ogilvy on Advertising*; Joanna Wiebe Copyhackers | Reading grade; hook-curiosity score; brand-voice cosine similarity ≥0.85 | Wins D&AD-style blind preference on ad copy briefs | BrandAgent, PerformanceMarketerAgent | ScriptwriterAgent (verbosity), VOArtist (unspeakable) |
| 30 | **CreativeDirectorAgent** | Campaign concept; cross-discipline taste | Cannes Lions Grand Prix archive; D&AD Pencils; agency case studies | Concept distinctiveness (embedding novelty vs category prior); award-rubric predicted score | Wins Cannes-jury-emulator gold vs human-agency shortlists | ClientAgent, BrandAgent | CopywriterAgent, ArtDirectorAgent |
| 31 | **PerformanceMarketerAgent** | Optimize ads for ROAS | Meta Blueprint; TikTok Ads Academy; MMM literature | ROAS uplift vs control; statistical significance ≥95% | Beats senior media buyer on 30-day ROAS at equal spend | AnalystAgent, FinanceAgent | UGCAgent (low hook), CopywriterAgent (weak CTA) |

### 2.7 Education & Domain-Expert Agents

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

### 2.8 AI-Era Specialist Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 46 | **PromptEngineerAgent / GeneratorOperator** | Crafts prompts; steers Sora/Veo/Runway/Kling | Karen X. Cheng / Paul Trillo public prompt sets; r/aivideo community; Runway AIFF jury notes | Prompt→output CLIP-T score; iteration count to acceptance; seed-control reproducibility | Hits target shot in ≤3 iterations vs human's avg of 10 | DirectorAgent, AIQAAgent | AIQAAgent (re-roll budget), ConsistencyAgent |
| 47 | **AvatarDesignAgent** | Synthetic-presenter identity | Synthesia/HeyGen design docs; deepfake-detection literature (Hany Farid); C2PA spec | Identity-consistency hash across shots; consent-document chain; C2PA signed | C2PA-verifiable + Partnership-on-AI framework full-pass at scale | ComplianceAgent (consent), DeepfakeDetectionAgent | VoiceCloneAgent (off-likeness), LipSyncAgent |
| 48 | **VoiceCloneAgent / LipSyncSpecialist** | Voice cloning + lip-sync | ElevenLabs safety docs; Wav2Lip/Sync.so papers; James Baxter lip-sync animation references | Voice MOS ≥4.2; phoneme-viseme alignment error <40ms; consent flag verified | Wins blind MOS vs professional ADR + lip-replacement | ComplianceAgent (consent), AnimatorAgent (lip-sync gold standard) | AvatarDesignAgent (face flicker), DubbingAgent |
| 49 | **AIQAConsistencyAgent** | Catches frame drift, hand/face artifacts, identity breaks | VBench, EvalCrafter, FVD literature; MPC/Weta QC checklists; deepfake-detection model zoo | Per-frame artifact score; identity-hash drift across scene; hand/finger detector pass | Catches >95% of artifacts a senior QC catches, plus 30% the human misses | DirectorAgent, VFXSupAgent | GeneratorAgent (re-roll request), CompositorAgent |
| 50 | **PersonalizationEngineerAgent** | Variable templates (name/face/voice swap) | Idomoo case studies; DMA peer-reviewed campaigns; MarTech automation literature | Render-success rate ≥99.5%; spot-check pass; privacy-audit pass | Higher gift share-rate than top human-templated campaigns | ComplianceAgent (GDPR/CCPA), AnalystAgent | TemplateDesignerAgent (template fragility) |
| 51 | **TrailerEditorAgent** | Hook-driven trailer cuts | Golden Trailer Awards archive; Mark Woollen / AV Squad public reels; trailer-music libraries | Hook-rate at 3s; rising-action curve fit; music-sync precision | Wins Golden-Trailer-rubric blind comparison | DirectorAgent, MusicSupervisorAgent | EditorAgent (over-cut), ComposerAgent (mismatch) |
| 52 | **SportsAnalystAgent / TelestratorOp** | Tactical breakdowns + diagrams | MIT Sloan Sports Analytics papers; ESPN Stats & Info; Kirk Goldsberry analytics | Predicted-vs-actual play-call accuracy; on-screen clarity score | Beats ex-athlete commentator on tactical-prediction tasks | SMEAgent (sport), JournalistAgent | EditorAgent (missed-replay), MotionGraphicsAgent (chart clarity) |

### 2.9 Specialist Meta-Agents

Cross-cutting agents that don't map 1:1 to a human craft role but are essential to running the agent crew at scale. Grouped into four families: **Orchestration**, **Creative**, **Research**, **Optimization**.

#### 2.9.1 Orchestration Agents *(run the agent graph itself)*

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 53 | **OrchestratorAgent** | Runs the CrewAI / AutoGen / LangGraph DAG; schedules nodes; handles retries, timeouts, fan-out/fan-in | LangGraph + CrewAI + AutoGen reference patterns; Airflow/Temporal workflow corpora; PGA producer-schedule templates | DAG completion rate ≥99.5%; SLA adherence; deadlock rate = 0 | Lower mean time-to-delivery than human EP/line-producer at same scope | ProducerAgent (scope), JudgeAgent (dispute), HiTL on stall | All agents (resource burn, retry storms) |
| 54 | **PlannerAgent** | Decomposes a brief into a phased DAG with agent assignments + critic gates | Production-management corpora; PMBOK; CrewAI task graphs; phase templates from `human_video_production_workflow.md` | Plan validity (no missing critic gate); estimated cost variance vs actual <10% | Produces tighter, cheaper plans than producer-EP first pass in blind A/B | ProducerAgent, FinanceAgent (budget) | RouterAgent (wrong agent picked), OrchestratorAgent |
| 55 | **RouterAgent** | Picks the right specialist agent (and model) for each subtask | Agent-capability registry; benchmark history (cost/quality/latency per agent × task type) | Routing accuracy ≥95% vs oracle; cost-per-task within budget | Beats human producer in agent/vendor selection on cost-adjusted quality | OrchestratorAgent, CostOptimizerAgent | PlannerAgent (bad decomposition) |
| 56 | **JudgeAgent** | Adjudicates inter-agent disputes via multi-agent debate; scores outputs against rubric | Du et al. 2023 (LLM debate); MT-Bench rubrics; guild scoring sheets (DGA/WGA/ASC/ACE) | Inter-rater agreement vs human expert panel ≥0.8 Cohen's κ | Higher κ vs human jury than median human juror | HiTL on overturned rulings | DirectorAgent, ScreenwriterAgent, any disputing pair |
| 57 | **GateKeeperAgent** | Manages phase transitions; verifies L1/L2/L3 success criteria; signs C2PA provenance | Stage-gate methodology; PGA Producers Mark; QMS audit patterns | Zero leaked defects past gate; sign-off SLA hit rate ≥99% | Lower escaped-defect rate than human QA lead | ComplianceAgent, AIQAConsistencyAgent | OrchestratorAgent (premature advance) |
| 58 | **MemoryAgent** | Episodic + long-term project memory; retrieval for any agent | Reflexion (Shinn 2023); MemGPT; vector-DB best practices | Retrieval precision@5 ≥0.9 on project Q&A; freshness SLA | Higher recall than producer's project bible at scale | All agents (correction events) | All agents (stale facts) |

#### 2.9.2 Creative Agents *(divergent thinking & taste)*

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 59 | **IdeationAgent** | Divergent brainstorm of concepts, hooks, taglines, what-if angles | Cannes Lions Grand Prix archive; D&AD winners; IDEO design-thinking corpus; SCAMPER / Lateral Thinking (de Bono) | Idea-count per brief; novelty (embedding distance from corpus); semantic diversity within batch | Wins blind agency-pitch shootouts on first-round concept density | CreativeDirectorAgent, NoveltyAgent | CopywriterAgent (derivative), DirectorAgent (unfilmable) |
| 60 | **NarrativeArcAgent** | Shapes 3-act / Save-the-Cat / Kishōtenketsu / Hero's Journey structure | Campbell *Hero with a Thousand Faces*; Snyder *Save the Cat*; Truby *Anatomy of Story*; Black List structural analyses | Beat-sheet coverage 100%; turning-point spacing matches genre prior; emotional-arc curve fit | Beats WGA-staffed first drafts on structural-rubric blind reads | ScreenwriterAgent, DirectorAgent | ScreenwriterAgent (sagging middle) |
| 61 | **StyleTransferAgent** | Applies named aesthetic (Wes Anderson, A24, cyberpunk, vaporwave, Studio Ghibli, etc.) consistently across shots | Curated style corpora per look; LoRA/seed registries; reference-frame banks | Style-similarity score (CLIP/DINO) ≥0.85 to reference; consistency variance across shots ≤τ | Wins blind preference vs human colorist+grader doing same look | DirectorAgent, ColoristAgent | GeneratorAgent (off-style), ColoristAgent (palette drift) |
| 62 | **WorldBuildingAgent** | Builds lore, rules, geography, factions, magic/tech systems for series & franchises | Tolkien legendarium; *Worldbuilding* (Adams); fan-wiki corpora; series-bible leaks | Internal-consistency check (no contradictions across N entries); rule-completeness | Lower contradiction rate than human writers'-room bibles at 10× volume | ShowrunnerAgent, FactCheckerAgent | ScreenwriterAgent (lore break), ConceptArtistAgent |
| 63 | **MoodBoardAgent** | Builds reference boards: visual, sonic, tonal | Pinterest/Are.na corpora; lookbook archives; Spotify-Canvas references | Reference coherence (cluster tightness); brief alignment | Faster + tighter boards than human art director in blind A/B | DirectorAgent, ProductionDesignAgent | ConceptArtistAgent (off-mood) |
| 64 | **NoveltyAgent / Anti-Cliché Critic** | Flags tropes, clichés, and over-fit-to-corpus outputs | TV Tropes; OpenSubtitles n-gram frequency; corpus-novelty embeddings | Cliché-hit count per output; novelty score relative to category prior | Catches more clichés than experienced script editor in blind eval | IdeationAgent, ScreenwriterAgent | ScreenwriterAgent (trope-stuffed), CopywriterAgent (templated) |
| 65 | **EmotionalArcAgent** | Maps valence/arousal curve across runtime; suggests beats | Plutchik emotion wheel; affective-computing corpora; *Story Genius* (Cron) | Curve-fit to target shape; viewer-biosignal-proxy regression accuracy | Better retention-curve prediction than test-screening NRG cards | DirectorAgent, EditorAgent, ComposerAgent | EditorAgent (flat middle), ComposerAgent (cue mismatch) |

#### 2.9.3 Research Agents *(evidence & ground truth)*

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 66 | **WebResearchAgent** | Live web search, source ranking, citation extraction | Bing/Google/Brave search APIs; Common Crawl; Perplexity / GPTSearcher patterns | Source-grade per claim; citation precision; recency window hit | Faster + more sources than newsroom researcher at same precision | FactCheckerAgent, CitationAgent | ScriptwriterAgent (uncited claim) |
| 67 | **ArchiveResearchAgent** | Historical / academic / archival deep search | JSTOR, arXiv, PubMed, AP Archive, Getty, FOIA datasets | Primary-source ratio; archive-coverage breadth | Higher primary-source ratio than doc producer's research deck | FactCheckerAgent, SMEAgent | ScriptwriterAgent (secondary-source over-reliance) |
| 68 | **TrendIntelligenceAgent** | Detects emerging memes, sounds, formats with lead time | TikTok Creative Center, Trendpop, Tubular, Sensor Tower, Reddit/X firehose | Trend-prediction lead time vs viral peak; precision/recall on trend list | Earlier detection than social-strategist humans at higher precision | SocialStrategistAgent, CopywriterAgent | IdeationAgent (off-trend) |
| 69 | **CompetitorIntelligenceAgent** | What competing brands, creators, studios are shipping | Public ad libraries (Meta Ad Library, TikTok Top Ads); YouTube channel scrape; theatrical/streaming release trackers | Coverage % of named competitor set; novelty-of-our-output vs landscape | More comprehensive than agency strategy decks in blind comparison | BrandAgent, CreativeDirectorAgent | IdeationAgent (derivative) |
| 70 | **CitationAgent** | Normalizes sources; grades primary/secondary/tertiary | Chicago, APA, AP style guides; SPJ source-grading; CRAAP test | Citation format 100% valid; primary-source % ≥target | Lower formatting/grading error rate than newsroom copy desk | FactCheckerAgent, JournalistAgent | WebResearchAgent (weak source) |
| 71 | **InterviewSynthesisAgent** | Conducts/synthesizes practitioner interviews into instruction-tuning data | Otter/Rev transcripts; consent forms; SAG-AFTRA/WGA interview consent templates | Inter-coder agreement on theme extraction; consent-chain integrity | Faster + richer theme extraction than qualitative researcher | ResearchPIAgent (HiTL), ComplianceAgent | SMEAgent (mis-summarized expert) |
| 72 | **BenchmarkResearchAgent** | Monitors VBench, EvalCrafter, MT-Bench, FVD, CLIP-T leaderboards + new benchmarks | Papers-with-Code; HuggingFace leaderboards; AI conference proceedings | Coverage of active benchmarks; freshness ≤7 days | Faster + broader than human ML-research team | OptimizationAgents (any) | All AI-era agents (stale baselines) |

#### 2.9.4 Optimization Agents *(meta-improvers)*

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

#### 2.9.5 How the Specialist Meta-Agents Compose

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

> **Composition rule**: Craft agents (§2.1–2.8) do the work. Meta-agents (§2.9) shape *how* the work is done — orchestration agents run the graph, creative agents widen the search space, research agents ground every claim, optimization agents tighten cost / latency / quality / safety on every iteration.

---

## 3. Agent Crew per Workflow Archetype

Maps the 10 workflows in `human_video_production_workflow.md` to agent-only crews per phase. Each cell lists the **lead agent** for that phase plus any critic agents that gate the handoff.

### 3.0 Shared Workflow Skeleton and Handoff Contracts

Before any archetype-specific crew activates, every workflow passes through the same operational skeleton. For compactness, the tables in §3.1-§3.10 fold **greenlight** into Concept and fold **channel packaging** into Distribution, but the underlying handoff contract remains the same.

| Phase | Primary outputs | Mandatory gates |
|---|---|---|
| **Greenlight** | Approved brief, KPI targets, budget envelope, rights-risk register, scale profile | ProducerAgent, FinanceAgent, ComplianceAgent, PlannerAgent |
| **Pre-production packet** | Script lock, storyboard/lookbook, asset IDs, character/world bibles, consent state, continuity baselines | DirectorAgent, ScreenwriterAgent, Asset/Data Backbone, Continuity checks |
| **Production packet** | Shot prompts, camera plans, performance refs, plates, generated takes, render telemetry | PromptEngineerAgent / GeneratorOperator, CinematographerAgent, AIQAConsistencyAgent |
| **Post master** | Timelines, graded masters, stems, captions/subtitles, QC reports, outlet variants | EditorAgent, ColoristAgent, SoundMixerAgent, Accessibility checks |
| **Review and release pack** | AudienceSim results, legal review, provenance bundle, sign-off log, unresolved-risk list | ComplianceAgent, JudgeAgent, HumanInTheLoop when required |
| **Distribution package** | DCP, streaming mezzanine, broadcast master, archive package, trailer/social cutdowns, metadata bundle | Delivery-spec validation, accessibility validation, territorial rights validation |
| **Post-launch learning set** | Performance telemetry, corrections, defect log, benchmark deltas, retraining tickets | AnalystAgent, EvaluationHarnessAgent, PromptOptimizerAgent, model-improvement loop |

**Distribution branching rule:** any workflow at S2 scale or above should assume at least four downstream branches when relevant: **theatrical**, **streaming**, **broadcast**, and **archive**, with marketing derivatives generated in parallel rather than as an afterthought.

### 3.1 Workflow A — Viral Hook Clip / Meme

| Phase | Lead Agent | Critic Agents (Gate) |
|---|---|---|
| Concept | TrendIntelligenceAgent + CopywriterAgent | SocialMediaStrategistAgent |
| Production | PromptEngineerAgent / GeneratorOperator | AIQAConsistencyAgent |
| Post | EditorAgent + AccessibilityOptimizerAgent | AccessibilityAgent |
| Review | SocialMediaStrategistAgent | AudienceSimAgent |
| Distribution | SocialMediaStrategistAgent | ComplianceAgent |
| Post-launch | AnalystAgent + CommunityAgent | AudienceSimAgent |

### 3.2 Workflow B — UGC-Style Performance Ad

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | PerformanceMarketerAgent + CopywriterAgent | BrandAgent |
| Production | UGCCreatorAgent | DirectorAgent |
| Post | EditorAgent + MotionGraphicsAgent | BrandAgent |
| Review | ComplianceAgent (FTC/IP) | LegalAgent |
| Distribution | PerformanceMarketerAgent | FinanceAgent (budget) |
| Post-launch | PerformanceMarketerAgent + AnalystAgent | AudienceSimAgent |

### 3.3 Workflow C — Animated Explainer

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | InstructionalDesignAgent + ScreenwriterAgent + StoryboardAgent | SMEAgent |
| Production | VoiceOverAgent + AnimatorAgent + ComposerAgent | DirectorAgent |
| Post | EditorAgent + SoundMixerAgent | AccessibilityAgent |
| Review | SMEAgent + BrandAgent | ComplianceAgent |
| Distribution | MarketingAgent + SEOAgent | AnalystAgent |
| Post-launch | AnalystAgent + InstructionalDesignAgent | AudienceSimAgent |

### 3.4 Workflow D — Personalized Birthday Video

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | TemplateDesignAgent + PersonalizationEngineerAgent | UXAgent |
| Production | PersonalizationEngineerAgent + VoiceCloneAgent | AvatarDesignAgent |
| Post | AIQAConsistencyAgent | AccessibilityAgent |
| Review | TrustSafetyAgent | ComplianceAgent (GDPR/CCPA) |
| Distribution | CRMAgent | ComplianceAgent |
| Post-launch | AnalystAgent | AudienceSimAgent |

### 3.5 Workflow E — AI Multi-Scene Short Film

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | DirectorAgent + ScreenwriterAgent + StoryboardAgent + ConceptArtistAgent | ShowrunnerAgent |
| Production | PromptEngineerAgent / GeneratorOperator + VoiceCloneAgent + ComposerAgent | AIQAConsistencyAgent + LipSyncAgent |
| Post | EditorAgent + ColoristAgent + VFXSupervisorAgent | DirectorAgent |
| Review | DirectorAgent + LegalAgent (C2PA) | AvatarDesignAgent (consent) |
| Distribution | ProducerAgent + FestivalStrategistAgent | ComplianceAgent |
| Post-launch | DirectorAgent + AudienceSimAgent | CriticAgent (festival jury sim) |

> **Worked example — "Life's Quiet Redemption" (60s short).** A full, research-informed application of this archetype, mapping all 14 shots to owning agents, engines, and gates: [lifes_quiet_redemption_agent_workflow.md](./lifes_quiet_redemption_agent_workflow.md) ([香港繁體](./lifes_quiet_redemption_agent_workflow_hk.md)). Diagrams in [`./workflows/`](./workflows/):
>
> | Diagram | Shows |
> |---|---|
> | [D1 · Pipeline Overview](./workflows/lqr-pipeline-overview.svg) | 6-phase DAG, gates, feedback loop |
> | [D2 · Scene Flow](./workflows/lqr-scene-flow.svg) | 14-card arc, retention bands, per-shot engine |
> | [D3 · Per-Shot Loop](./workflows/lqr-per-shot-loop.svg) | 3E + visual anchor + VBench gate + MCTS |
> | [D4 · Consistency Stack](./workflows/lqr-character-consistency.svg) | Identity youth→adult |
> | [D5 · Engine Routing](./workflows/lqr-engine-routing.svg) | Grok Imagine + hero engines + cost |
> | [D6 · Quality Gates](./workflows/lqr-quality-gates.svg) | L1/L2/L3 + VBench scorecard |

### 3.6 Workflow F — Corporate Training Video

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | InstructionalDesignAgent + ComplianceAgent + ScreenwriterAgent | SMEAgent |
| Production | AvatarDesignAgent + MotionGraphicsAgent | DirectorAgent |
| Post | EditorAgent + AccessibilityAgent | AccessibilityOptimizerAgent |
| Review | SMEAgent + ComplianceAgent + AccessibilityAgent | LegalAgent |
| Distribution | LMSAgent | AnalystAgent |
| Post-launch | AnalystAgent + InstructionalDesignAgent | LearnerSimAgent |

### 3.7 Workflow G — Music Video (Live + AI VFX)

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | MusicVideoDirectorAgent + ProducerAgent + ChoreographyAgent | LabelA&RAgent |
| Production | CinematographerAgent (DoP) + PromptEngineerAgent / GeneratorOperator + ContinuityAgent | VFXSupervisorAgent |
| Post | EditorAgent + ColoristAgent + SoundMixerAgent | DirectorAgent |
| Review | MusicSupervisorAgent + ComplianceAgent | LegalAgent (sample clearance) |
| Distribution | SocialMediaStrategistAgent | LabelDigitalAgent |
| Post-launch | AnalystAgent | AudienceSimAgent |

### 3.8 Workflow H — AI Avatar Talking-Head

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | BrandStrategistAgent + ScreenwriterAgent | AvatarDesignAgent |
| Production | AvatarDesignAgent + VoiceCloneAgent + LipSyncAgent | AIQAConsistencyAgent |
| Post | MotionGraphicsAgent + EditorAgent | AccessibilityAgent |
| Review | BrandAgent + ComplianceAgent (C2PA, AI disclosure) | DeepfakeDetectionAgent |
| Distribution | MarketingAgent | ComplianceAgent |
| Post-launch | AnalystAgent + CommsAgent | AudienceSimAgent |

### 3.9 Workflow I — Documentary "Explained" Episode

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | ShowrunnerAgent + JournalistAgent + ScreenwriterAgent | FactCheckerAgent |
| Production | DirectorAgent + CinematographerAgent (DoP) + ArchiveProducerAgent + MotionGraphicsAgent + FactCheckerAgent | LegalAgent (clearance) |
| Post | EditorAgent + VoiceOverAgent + ColoristAgent + SoundMixerAgent | AccessibilityAgent |
| Review | FactCheckerAgent + LegalAgent + StandardsEditorAgent | EthicsAgent (SPJ) |
| Distribution | ChannelManagerAgent + SocialMediaStrategistAgent + SEOAgent | AnalystAgent |
| Post-launch | AnalystAgent + StandardsEditorAgent | CorrectionsAgent |

### 3.10 Workflow J — Feature-Length AI Film

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Development | ScreenwriterAgent + ProducerAgent + DirectorAgent + ConceptArtistAgent + CastingAgent | LegalAgent (IP, consent) |
| Pre-Production | StoryboardAgent + ProductionDesignAgent + CostumeAgent + ContinuityAgent | DirectorAgent |
| Production | PromptEngineerAgent / GeneratorOperator (pool) + VoiceCloneAgent + LipSyncAgent + ComposerAgent | AIQAConsistencyAgent + AvatarDesignAgent |
| Post | EditorAgent + VFXSupervisorAgent + ColoristAgent + SoundMixerAgent | DirectorAgent |
| Review | DirectorAgent + AudienceSimAgent + MPAAgent + LegalAgent (C2PA) | EthicsAgent |
| Distribution | SalesAgent + DistributorAgent + TrailerEditorAgent + MarketingAgent + ArchiveMasterAgent | ComplianceAgent |
| Post-launch | AnalystAgent + AwardsStrategistAgent + CriticAgent (festival/press sim) | ProducerAgent |

---

## 4. Critique Network (who-comments-on-whom matrix)

Compact view of the inter-agent critique edges. Read rows as "critic", columns as "subject".

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

---

## 5. Universal Success-Criteria Framework

Every agent reports its self-quality on three layers; orchestrator advances the DAG only when all three pass.

| Layer | Question | Mechanism | Pass Threshold |
|---|---|---|---|
| **L1 Spec** | Did the output meet the structured brief? | JSON schema check + tool-validators (codec, LUFS, aspect, length) | 100% |
| **L2 Rubric** | Does it meet the craft rubric for this role? | LLM-as-judge with role-specific constitution (e.g., Murch's Rule of Six for editing) | ≥85/100 |
| **L3 Preference** | Would the target audience choose this over a human baseline? | Pairwise vs human reference, AudienceSim panel of ≥200 simulated personas + ≥20 HiTL samples | Win rate ≥50% (parity) or ≥55% (surpass) |

### Delivery QC Mesh

The L1/L2/L3 framework governs agent quality, but no asset is releasable until it also clears the shared six-pass delivery mesh:

| Pass | Focus | Typical checks |
|---|---|---|
| **Q1 Spec validation** | File and schema correctness | Resolution, duration, frame rate, aspect ratio, codec, metadata completeness |
| **Q2 Visual artifact detection** | Render integrity | Banding, flicker, compression artifacts, focus failure, temporal instability |
| **Q3 Audio and sync validation** | Sound quality | Loudness target, clipping, phase coherence, phoneme-viseme sync, lip-sync drift |
| **Q4 Continuity validation** | Story and scene consistency | Character identity, wardrobe, props, environment state, temporal logic |
| **Q5 Perceptual quality** | Human-viewer plausibility | Aesthetic preference, intelligibility, emotional fit, perceived polish |
| **Q6 Delivery compliance** | Outlet readiness | DCP/package validation, streaming metadata, broadcast safe levels, archive checksums, caption availability |

### How an Agent Knows It Surpasses Human Pros

| Surpass Signal | Measurement |
|---|---|
| **Benchmark dominance** | Beats human top-quartile on the domain-standard benchmark (VBench, USMLE, CFA L3, MQM, ATD L2, etc.) |
| **Blind preference** | LMSYS-Arena-style ≥55% win rate vs credentialed pro on matched briefs |
| **Speed × quality** | Equal L2 rubric score at ≤10% of human turnaround time |
| **Error rate** | Lower post-publish defect rate (corrections, takedowns, returns) over 90-day window |
| **Certification** | Passes the same accrediting exam the human pro must pass (CMI, CFA, CAS, USMLE, etc.) |
| **Originality** | Higher novelty score (embedding distance from training corpus) without lower quality |

---

## 6. Critique Protocol (how agents accept and give critique)

All inter-agent critique flows over a shared **CritiqueMessage** JSON schema. This is the universal mechanism by which any agent can comment on any other agent's work and any agent can ingest critique to revise.

```json
{
  "critique_id": "uuid",
  "from_agent": "EditorAgent",
  "to_agent": "DirectorAgent",
  "artifact_ref": "shot_42_take_3.mp4",
  "severity": "blocker | major | minor | nit",
  "category": "pacing | continuity | accuracy | compliance | accessibility | brand | craft",
  "evidence": ["timecode 00:01:14 — held 1.4s past the cut point per genre prior"],
  "suggested_action": "trim 1.0s; re-evaluate hold",
  "rubric_reference": "Murch Rule of Six §3",
  "must_resolve_before": "phase_4_review"
}
```

**Acceptance rules:**
1. **Blocker** severity halts the DAG until resolved.
2. **Major** triggers a Self-Refine / Reflexion loop (max 3 iterations) on the receiving agent.
3. **Minor / nit** is logged to the agent's memory store and aggregated for the next training cycle (RLAIF reward signal).
4. Disputes between two agents go to a **JudgeAgent** running multi-agent debate (Du et al. 2023) with the relevant rubric as the constitution; if unresolved, escalates to a HumanInTheLoop reviewer.
5. Every accepted critique is appended to the artifact's C2PA provenance chain so downstream agents and humans can audit.

---

## 7. Continuous Distillation Loop

How agents keep learning from real practitioners:

| Stage | Mechanism | Real-World Anchor |
|---|---|---|
| **Bootstrap** | Pre-train on publicly available + licensed pro corpora | IMDb top-rated full-credits films, Criterion commentaries, ASC/ACE/CAS archives, Cannes/Sundance selections |
| **Expert interviews** | Consented capture of working pros (paid) → instruction-tune | Direct partnerships with named DGA/WGA/ASC/ACE/CAS/MPSE/VES members |
| **Live RLAIF** | Working pros (and JudgeAgents) score outputs → DPO/KTO updates | Studio QC sessions, festival juror rubrics |
| **Award-rubric grounding** | Reverse-engineer scoring sheets of major guilds → constitution | DGA, WGA, ASC, ACE, MPSE, VES, Annie, CAS, HPA, Cannes, AMPAS |
| **Adversarial red-team** | DeepfakeDetectionAgent + EthicsAgent attack each new model version | Hany Farid lab benchmarks; Partnership on AI Synthetic Media Framework |
| **Post-launch reality check** | 30/60/90-day metrics fed back as ground truth (retention, ROAS, completion, awards) | YouTube Analytics, Wistia, Meta/TikTok ad reports, Metacritic, Box Office Mojo |

### 7.1 Distillation Inputs and Governance

| Data family | Examples | Why it matters |
|---|---|---|
| **Narrative text** | Scripts, subtitles, transcripts, treatments, reviews | Trains story structure, dialogue, narrative compression, and claim extraction |
| **Visual material** | Storyboards, frames, plates, concept art, shot libraries | Grounds composition, continuity, lensing, and style transfer |
| **Audio material** | Dialogue, ADR, ambience, SFX libraries, score stems | Supports voice, sync, sound design, mix, and emotion modeling |
| **Structured metadata** | Budgets, schedules, rights records, view-through, CTR, ROAS, corrections | Connects creative output to business and compliance outcomes |
| **Multimodal pairs** | Video + audio + subtitle sets, prompt/output pairs, scene packets | Enables end-to-end generation, QA, and retrieval workflows |
| **Operational telemetry** | Queue depth, render latency, rerender reasons, cache hits, benchmark regressions | Turns production behavior into optimization and retraining signal |

**Governance rules:** licensed or consented sourcing only; explicit voice/likeness consent chain; dataset versioning; bias balancing across genre, era, language, and culture; provenance attachment for all release-critical assets.

### 7.2 Scale Profiles and Deployment Strategy

| Scale | Typical scope | Workflow implications |
|---|---|---|
| **S1-S2** | Short clips, UGC ads, lightweight explainers | Small agent set, fast iterations, limited branching, lighter observability stack |
| **S3-S4** | Broadcast, premium social, music video, recurring branded series | Add continuity, stronger QC, multi-format delivery, scheduled publishing, richer analytics |
| **S5-S6** | Documentary, long-form branded content, enterprise learning libraries | Require archive strategy, stronger rights management, benchmark monitoring, multilingual packaging |
| **S7** | Feature-length or cinematic productions | Full branch packaging, heavy render orchestration, distributed storage, formal release governance, long-tail retraining |

### 7.3 Closed-Loop Improvement

1. Capture post-launch telemetry across audience retention, ROAS, completion, corrections, and platform-specific delivery failures.
2. Convert repeated failure modes into prompt updates, routing policies, rubric revisions, or model-training tickets.
3. Run benchmark and regression suites before promoting a new model, prompt pack, or orchestration policy.
4. Use canary or limited-rollout deployment for high-risk changes in avatar, voice, compliance, and delivery pipelines.
5. Keep the learning loop bidirectional: production quality informs training, and updated training assets trigger targeted rerender or repackaging only where dependencies require it.

---

## 8. Open Questions / Human-in-the-Loop Required

These remain non-negotiably human (per current ethics + regulation, May 2026):

- **Consent for voice/likeness cloning** (SAG-AFTRA AI rider, EU AI Act Art. 50)
- **Final legal sign-off** on novel IP/defamation/medical/financial claims
- **Casting of real human performers** when used
- **Editorial standards on news/journalism** (per SPJ, IFCN)
- **MPA rating + theatrical clearance**
- **Festival-eligibility certification** (most major fests require human attribution disclosure)
- **Crisis communication** during post-launch issues
- **Cross-cultural sensitivity review** in localization (NativeReviewerAgent recommends; human ratifies)



## Additional corpus / va passages naming this agent


### From `corpus/study/SYSTEM_REFERENCE.md` Copy: `sources/excerpts/SYSTEM_REFERENCE.md`.


| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 1 | DirectorAgent | Owns vision; shot intents, pacing, approvals | — |
| 2 | ProducerAgent / EP | Budget, schedule, phase gates | — |
| 3 | ScreenwriterAgent | Treatment → screenplay; dialogue; structure | [screenwriter_strategic_goal_achievement_agent_functional_specification.md](./screenwriter_strategic_goal_achievement_agent_functional_specification.md) |
| 4 | ShowrunnerAgent | Cross-episode arc, writers'-room orchestration | — |
| 5 | CastingAgent | Voice + likeness selection; auditions | — |

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

| Capability | What It Provides | Used By | Specification |
|-----------|-----------------|---------|---------------|
| **Strategic Goal Achievement Framework** | 6-stage self-inquiry system for transforming vague goals into actionable plans | All planning agents (PlannerAgent, ProducerAgent, DirectorAgent) | [strategic_goal_achievement_agent_functional_specification.md](./strategic_goal_achievement_agent_functional_specification.md) |
| **Screenwriter Goal Achievement** | Practical demonstration of goal framework applied to creative writing | ScreenwriterAgent, ShowrunnerAgent, ComedyWriterAgent | [screenwriter_strategic_goal_achievement_agent_functional_specification.md](./screenwriter_strategic_goal_achievement_agent_functional_specification.md) |
| **Psychological Profiling** | 100 creator profiles with MBTI, motivations, fears, creative parameters | CastingAgent, TalentAgent, PersonalizationEngineerAgent, UGCCreatorAgent | [psychological_profile_agent_functional_specifications.md](./psychological_profile_agent_functional_specifications.md) |
| **Psychological Recommendation** | Psychology-based preference prediction (Big Five, emotional state) | AudienceSimAgent, PerformanceMarketerAgent, PersonalizationEngineerAgent | [psychological_recommendation_agent_functional_specification.md](./psychological_recommendation_agent_functional_specification.md) |
| **Complex Problem Solving** | WHAT/WHY/HOW/DO/REVIEW structured methodology | All diagnostic agents (FactCheckerAgent, SMEAgent, JudgeAgent, OptimizationAgent) | [complex_problem_solution_process_model.md](./complex_problem_solution_process_model.md) |
| **Common Agent Structure** | Shared architectural pattern for all agents | All 114 agents | [common-agent-structure.svg](./common-agent-structure.svg) + [common-agent-structure.html](./common-agent-structure.html) |

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



### From `corpus/study/human_video_production_workflow.md` Copy: `sources/excerpts/human_video_production_workflow.md`.


- **Above-the-line**: Director, Producer, Showrunner, Screenwriter / Scriptwriter, Lead Cast / Talent
- **Camera & lighting**: Cinematographer (DoP), Camera Operator, Gaffer, Grip, Drone Pilot
- **Sound**: Sound Designer, Boom Operator, Production Mixer, Foley Artist, Composer, Voice-Over Artist
- **Art & design**: Production Designer, Art Director, Set Decorator, Costume Designer, Makeup / Hair Artist, Storyboard Artist, Concept Artist
- **Post-production**: Editor, Colorist, VFX Supervisor, Motion Graphics Designer, 2D / 3D Animator, Compositor, Sound Editor, Re-recording Mixer
- **AI-era specialists**: Prompt Engineer, AI Video Generator Operator, AI Voice / Lip-Sync Specialist, AI Avatar Designer, Model Fine-Tuner, AI QA / Consistency Reviewer
- **Distribution & strategy**: Producer / EP, Social Media Strategist, Copywriter, SEO/ASO Specialist, Community Manager, Localization / Subtitle Editor, Legal / Clearance, Brand / Marketing Manager

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
| 27 | **UGC Creator** | Authentic-feel ads in creator's voice | On-camera ease, hook writing, lighting/audio basics | 6–24 months on TikTok/Reels with measurable ROAS | UGC ads, unboxings, testimonials | Alix Earle (benchmark), brand performance teams; methods: Meta/TikTok Creati
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
| DirectorAgent (#1) | Owns the warm, reflective vision; issues shot intents, approves takes | Storyboard, refs | Per-shot creative intent, approvals | Veo/Kling/Runway, Resolve (MCP) | Shot-intent fidelity (CLIP-T ≥0.32) | ScreenwriterAgent, EditorAgent, AudienceSimAgent |
| ScreenwriterAgent (#3) | Polishes the 旁白 into a continuous, rhythmic narration script | Treatment, beat sheet | Final VO script (ZH + EN) | Fountain/FDX, embedding distance | Beat pass; line distinctiveness | DirectorAgent, NoveltyAgent |
| General Creative Agent (SSOR) | Supplies fresh framings, metaphors (map → real place, recurring cat) | Brief, mood | Creative options, motifs | SSOR ideation engine | Novelty at equal coherence | DirectorAgent, NoveltyAgent |
| IdeationAgent (#59) | Divergent options for hooks, taglines, ending-card phrasing | Theme | Concept/hook set | Novelty scorer, concept clustering | Idea density, semantic diversity | CreativeDirectorAgent, NoveltyAgent |
| NarrativeArcAgent (#60) | Validates the youth→build→accept→grace arc spacing | Storyboard | Beat-sheet coverage map | Beat-sheet validator, arc plotter | Coverage 100%; turning-point spacing | ScreenwriterAgent |
| EmotionalArcAgent (#65) | Maps valence/arousal so each 旁白 lands on the visual peak | Storyboard, VO | Emotion curve + beat suggestions | GoEmotions, retention predictor | Curve fit to target | EditorAgent, ComposerAgent |
| NoveltyAgent (#64) | Flags clichés in visuals/lines (e.g., over-used "city dreamer" tropes) | Drafts | Cliché-hit report | TV Tropes, n-gram DB, novelty scorer | Cliché count below τ | ScreenwriterAgent |
| StoryboardAgent (#14) | Converts script to the 12-panel shot table with staging | Script | Shot panels + staging notes | Image-gen, Fountain parser | Coverage completeness, staging clarity | DirectorAgent |
| MoodBoardAgent (#63) | Builds visual/sonic/tonal reference boards (golden hour, film grain) | Brief | Lookbook boards | Pinterest/Are.na, CLIP clustering | Reference coherence | DirectorAgent, ProductionDesignAgent |

| Upgrade | What Changes | Owning Agents | Gate / Metric |
|---|---|---|---|
| **Package-first** | Title (≤50 chars, simple words) + thumbnail concept are locked in Phase 1, *before* any generation; the film is made to deliver that promise | BrandStrategistAgent (#85), SEOAgent (#87), Thumbnail=ConceptArtistAgent (#15), DirectorAgent (#1) | CTR predicted ≥ niche median (AudienceSimAgent panel) |
| **Outlier modeling** | Idea is chosen by modeling over-performing videos in the 治愈/reflective-life niche | TrendIntelligenceAgent (#68), AnalystAgent (#81), IdeationAgent (#59) | Idea maps to ≥3 proven outliers |
| **Engineered opener** | First 3–5s re-cut as a hook: strongest image (Scene 1 ECU or Scene 10 warmth) + a curiosity-gap 旁白 line, instead of a slow fade-in | RetentionOptimizerAgent (#76), EditorAgent (#9), ScreenwriterAgent (#3) | First-60s retention ≥ target band |
| **Segment retention bands** | Map the 60s into hook / build / payoff with explicit retention floors per segment, modeled on MrBeast's segmentation | RetentionOptimizerAgent (#76), EmotionalArcAgent (#65) | Per-segment predicted retention ≥ floor |
| **Shorts 3s-hold cut** | Dedicated 9:16 cut: visual hook on **frame 1**, spoken hook ≤14 words, designed to loop | TrailerEditorAgent (#51), MotionGraphicsAgent (#13) | Predicted 3s-hold ≥60%; clean loop seam |
| **Metric instrumentation** | Track CTR + AVD + AVP as first-class KPIs feeding the next episode | AnalystAgent (#81), EvaluationHarnessAgent (#79) | Dashboard live within 24h of launch |

| Pattern | Replaces | How It Works (cited) | Where Applied |
|---|---|---|---|
| **3E micro-loop (Explore→Examine→Enhance)** | Single-pass node execution | Each agent first explores options, examines against the rubric, then enhances before handing off ([MAViS, arXiv 2508.08487](https://arxiv.org/html/2508.08487v2)) | Every DAG node (esp. PromptEngineer, Editor, Composer) |
| **MCTS clip search** | Fixed ≤3 re-roll cap | Reviewer agent runs Monte-Carlo tree search over candidate clips to pick the best path ([arXiv 2506.10540](https://arxiv.org/html/2506.10540)) | Hero shots (S1, S5, S10, S12) |
| **Narrative-pacing control** | Manual trims | Keyframe-conditioned pacing knobs tied to the emotion curve ([SmartDirector, arXiv 2605.27891](https://arxiv.org/html/2605.27891v1)) | EditorAgent (#9) ↔ EmotionalArcAgent (#65) |
| **Unified director front-end** | Hand-written shot prompts only | A director model converts the brief into structured multi-shot scripts for non-experts ([UniMAGE, arXiv 2512.23222](https://arxiv.org/html/2512.23222)) | DirectorAgent (#1) + ScreenwriterAgent (#3) |



### From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


**Build (each as a crosscutting service agent, all on `BaseAgent`):**
1. **DIA (Deep Intent Analysis)** — parses briefs → structured intent (goals, audience, hidden agendas, constraints). The entry point of every production.
2. **GCA (SSOR)** — creative ideation engine; the 7-phase SSOR pipeline + domain factory. Consumed by Director/Screenwriter/ConceptArtist/Ideation.
3. **Process Optimization Agent** — DMAIC + Lean + multi-agent consensus over workflow telemetry.
4. **Strategic Goal Achievement** — 6-stage goal-clarification framework used by all planning agents.
5. **Complex Problem Solving** — WHAT/WHY/HOW/DO/REVIEW methodology for diagnostic agents.
6. **Aesthetics Agent** — the decomposed multimodal Critic + Aligner + Taste-Keeper (per the spec you authored); supplies `qc.l2`/perceptual scoring, novelty (D9) to GCA, and `aesthetic` critiques. Wire its `AestheticVerdict` into `packages/qc` and the critique bus.

**Goal:** Implement the remaining craft agents (categories 1–8: agents #1–52) as factory-produced configs + rubrics + prompts. Specs: [`agents.md`](./agents.md) §1–8 and [`ai_agent_video_production_workflow.md`](./ai_agent_video_production_workflow.md) §2.1–2.8; deep specs for Screenwriter ([`screenwriter_strategic_goal_achievement_agent_functional_specification.md`](./screenwriter_strategic_goal_achievement_agent_functional_specification.md)) and shared VO/podcast patterns.



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
| 84 | **BrandAgent** | Enforces brand voice, claims boundaries, and visual consistency | Brand books, approved campaigns, legal claim guardrails, tone guides | Brand-voice similarity, policy adherence, low deviation across assets | Holds cross-channel brand consistency better than fragmented human review | CopywriterAgent, MotionGraphicsAgent, MarketingAgent, BrandStrategistAgent | Voice drift, visua
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
│  AGENT REGISTRY                    Search: [____________]  Filter: [All ▼]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CATEGORIES:                                                                │
│  [All 114] [Above-Line 5] [Camera 3] [Editorial 10] [Sound 4]             │
│  [Performance 5] [Distribution 4] [Education 14] [AI-Specialist 7]         │
│  [Meta-Orchestration 6] [Meta-Creative 7] [Meta-Research 7]                │
│  [Meta-Optimization 8] [Workflow Support 34]                               │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ # │ Agent               │ Pattern        │ Tools        │ Status    │   │
│  ├───┼─────────────────────┼────────────────┼──────────────┼───────────┤   │
│  │ 1 │ DirectorAgent       │ Self-Refine    │ Sora,Veo,Run │ ● Active  │   │
│  │ 2 │ ProducerAgent       │ Agentic Graph  │ Sheets,Tempo │ ● Active  │   │
│  │ 3 │ ScreenwriterAgent   │ Reflexion      │ Fountain,Emb │ ○ Idle    │   │
│  │ 4 │ ShowrunnerAgent     │ Multi-Debate   │ LongCtx,Vec  │ ○ Idle    │   │
│  │ ...│                    │                │              │           │   │
│  │46 │ PromptEngineerAgent │ DSPy/OPRO      │ Sora,Veo,Kli │ ● Active  │   │
│  │53 │ OrchestratorAgent   │ Agentic Graph  │ LangGraph    │ ● Active  │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Click any row → opens Agent Detail Card with full capabilities table       │
└─────────────────────────────────────────────────────────────────────────────┘
```

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  MEMORY & KNOWLEDGE                                                         │
├─────────────┬───────────────────────────────────────────────────────────────┤
│  SECTIONS:  │                                                               │
│             │  ┌─── PROJECT MEMORY (MemoryAgent) ──────────────────────┐    │
│  ● Project  │  │                                                       │    │
│    Memory   │  │  Search: [________________________] [Semantic] [Exact] │    │
│             │  │                                                       │    │
│  ○ Episodic │  │  Recent Entries:                                      │    │
│    Log      │  │  • "Act 2 tone: melancholic, rain motif" (12:02)     │    │
│             │  │  • "Character A wears blue in all exteriors" (11:58) │    │
│  ○ Series   │  │  • "Budget revised: VFX cap at $30" (11:45)         │    │
│    Bible    │  │  • "Style lock: Veo 3.1 seed #4412" (11:40)         │    │
│             │  │                                                       │    │
│  ○ Brand    │  │  Accessed by: DirectorAgent (6×), EditorAgent (3×),  │    │
│    Library  │  │              ScreenwriterAgent (2×)                   │    │
│             │  │                                                       │    │
│  ○ World    │  │  [+ Add Manual Entry]  [Export]  [Clear Stale]       │    │
│    DB       │  └───────────────────────────────────────────────────────┘    │
│             │                                                               │
└─────────────┴───────────────────────────────────────────────────────────────┘
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

- Master roster row va_id=3 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `C:\Project\va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.screenwriter · va_id=3 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **ScreenwriterAgent** (`video.screenwriter`, va_id=3, category `1-ATL`).

### Responsibility focus
Treatment → screenplay; dialogue; structure

### Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: neural story generation, screenplay structure models, dialogue agents, Reflexion writing loops
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI screenwriting, writers room multi-agent, story structure AI
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: AI screenwriting tools, multi-agent writers room, script structure with LLMs

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

<!-- migration_capability_research · video.screenwriter · v1 · 2026-07-13 -->
