# MemoryAgent

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 58 |
| **pack_id** | `video.memory` |
| **category** | `9-Meta` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.memory/` |

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

Episodic + long-term project memory; retrieval for any agent

## Knowledge distillation sources

Reflexion (Shinn 2023); MemGPT; vector-DB best practices

## Self-quality criteria

Retrieval precision@5 ≥0.9; freshness SLA

## Surpass-human signal

Higher recall than producer's bible at scale

## Critique bus

- **Accepts critique from:** All agents (correction events)

- **Comments on:** All agents (stale facts)

## Tools (design-time documentation)

Pinecone/Weaviate/Qdrant vector DB; MemGPT-style hierarchical memory; embedding models

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

Reflexion memory architecture (MemGPT extension)

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


### Document: `study/agentic_rag_functional_specification.md`

_Embedded from `corpus/study/agentic_rag_functional_specification.md`. Also stored at `sources/study/agentic_rag_functional_specification.md` under this agent folder._


# Task: Build Ultra-Production-Grade Hybrid Agentic RAG System – Exhaustive Architectural & Implementation Specification (April 2026)

** Initial Prompt to task.md from Creator **
```
# How to create backend services
FIRST:
Conduct a comprehensive analysis and research of the task.md file to fully understand all requirements, specifications, 
and technical details. Based on this analysis, design and implement a complete backend server architecture that fulfills 
all outlined requirements. The backend server must be created within a dedicated 'backend' folder structure. Ensure the 
implementation includes proper API endpoints, database schema design, authentication mechanisms, error handling, logging 
systems, and follows RESTful principles. Document all API endpoints with clear specifications, implement comprehensive 
unit and integration tests, and verify that the server handles all edge cases and scalability requirements mentioned in 
task.md.
THEN:
Configure the application to integrate with GROK from x.ai by utilizing the environment variables defined in backend/.env  . 
Update all relevant codebase components to establish GROK as the primary Large Language Model (LLM) provider. This includes 
modifying API connection configurations, authentication parameters, model endpoints, and any existing LLM integration code 
to ensure seamless communication with GROK services. Implement proper error handling, rate limiting, and fallback mechanisms.
Verify the integration by testing all LLM-dependent features including text generation, chat completions, and any custom 
model interactions. Document the configuration changes and ensure backward compatibility where applicable.

# How to create frontend services
Conduct comprehensive research and analysis of the task.md requirements document to architect and implement a complete 
frontend application with integrated backend services and knowledge-base functionality. Design and develop the frontend 
solution with the following specifications: analyze all functional requirements from task.md, create responsive UI 
components with modern frameworks, implement state management for complex data flows, establish API integrations with 
backend services, incorporate knowledge-base search and retrieval features, optimize performance for fast load times, 
implement accessibility standards (WCAG 2.1), create intuitive navigation patterns, add comprehensive error handling and 
user feedback mechanisms, ensure cross-browser compatibility, implement proper security measures for data handling, write 
unit and integration tests for all components, document the codebase with clear comments and README files, and save the 
complete frontend project structure to the designated frontend folder. The final deliverable must provide exceptional user 
experience through thoughtful interaction design, consistent visual hierarchy, smooth animations, mobile-first responsive 
design, and intuitive user workflows that minimize cognitive load while maximizing task completion efficiency.

```
**Task Owner:** Coding Agent  
**Priority:** Critical  
**Estimated Effort:** 10–14 days (MVP core in 6 days; full scale, hybrid integration, wiki compounding, observability & benchmarks in remaining days)  
**Goal:** Deliver a **complete, production-ready, observable, evaluable, extensible, and benchmarked Agentic RAG system** that **precisely** implements the **4 Core Agentic Design Patterns** and **7 Architectural Elements** from the survey paper "Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG" (arXiv:2501.09136, v4 as of April 2026) and the YouTube video "Agentic RAG Overview: 4 Core Principles and 7 Architectural Elements!" (https://youtu.be/MT3DM82PRLc).

The system **must**:
- Natively ingest and index your **~65,000 Markdown files (~500 MB corpus)** using **hierarchical chunking** with memory-safe, incremental, resumable processing.
- Support **hybrid knowledge representation**: Chroma vector store + **LightRAG** (latest 2026 version with OpenSearch backend support) for entity-relation graph and dual-level retrieval.
- Include **persistent knowledge compounding** via optional Karpathy-style LLM Wiki output (`wiki_output/` vault with `index.md`, `log.md`, concepts/, frontmatter, [[links]]`).
- Be fully local-first, Dockerized, traceable (LangSmith), and production-hardened.

This specification is the **definitive, deeply-rethought synthesis** of the entire conversation history after 10+ iterations of refinement: original Agentic RAG request → Karpathy Wiki comparison table → LightRAG enhancement → scale for 65k MD → repeated calls for deeper design details.

## 1. Core Concepts from Paper (Exact Mapping – Non-Negotiable)

**4 Core Agentic Design Patterns** (must be visible as explicit graph cycles/conditional edges):
1. **Reflection** — Agents self-evaluate outputs (relevance, faithfulness, hallucination) using rubrics and iterate (Self-RAG style reflection tokens or grader loops).
2. **Planning** — Autonomous decomposition of complex queries into sub-tasks or multi-hop plans.
3. **Tool Use** — Dynamic, interleaved tool calling (ReAct-style: think → act → observe).
4. **Multi-Agent Collaboration** — Specialized agents with shared state, hierarchical supervision, or flat peer coordination.

**7 Architectural Elements** (explicitly realized in design):
1. Single-agent routing + multi-agent delegation.
2. Hierarchical / graph-based control flow (LangGraph Pregel execution).
3. Adaptive retrieval (query complexity → strategy selection).
4. Stateful memory (conversation + long-term index + checkpoints).
5. Hybrid knowledge (vector + lightweight KG + persistent Markdown).
6. Iterative refinement with quality gates and max iterations.
7. Evaluation-aware (built-in metrics, tracing, health checks).

**Key Differentiators** (include updated comparison table in README.md):
- Superior to naive RAG (adds agency).
- Superior to pure Karpathy Wiki (query-time agentic reasoning + optional write-back).
- LightRAG adds fast relational power without heavy GraphRAG rebuild costs.

## 2. Full System Architecture (Mermaid – Include & Render in README)

```mermaid
graph TD
    User[User Query via CLI/Streamlit] --> Router[Query Analyzer Router<br/>Adaptive Strategy Selection]
    Router --> Planner[Planner Agent<br/>Decompose + Multi-Hop Plan]
    Planner --> ToolRouter[Tool Router<br/>Structured Decision: Vector | LightRAG | Web | Wiki]
    ToolRouter --> Vector[Vector Retriever<br/>Chroma MMR + Hierarchical + Rerank]
    ToolRouter --> LightRAGNode[LightRAG Dual-Level Retriever<br/>Entity + Relation Graph]
    ToolRouter --> Web[Tavily Web Search Tool]
    Vector & LightRAGNode & Web --> Researcher[Researcher + Grader Agent<br/>Reflection Loop + Doc Rubric Scoring]
    Researcher -->|grade < 0.85 & iterations < 3| Planner
    Researcher --> Generator[Generator Agent<br/>Synthesize with Citations]
    Generator --> Critic[Critic Agent<br/>Faithfulness + Hallucination Check]
    Critic -->|fail| Researcher
    Critic --> Final[Final Answer + Citations]
    Final --> WikiSynth[Optional Wiki Synthesizer Agent<br/>Karpathy-style Persistent Output]
    subgraph "State & Memory"
        State[AgentState + MemorySaver Checkpoints<br/>Conversation Summary + Long-term Index]
    end
    subgraph "Hybrid Knowledge Layer"
        Chroma[Chroma Vector DB<br/>Parent/Child Hierarchical Chunks]
        LRAG[LightRAG KG<br/>Entities, Relations, OpenSearch Backend]
    end
    WikiSynth --> WikiVault[wiki_output/ Vault<br/>index.md + log.md + concepts/]
```

## 3. Detailed Data Models (Pydantic v2 – Required)

Create `src/graph/state.py`:

```python
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Annotated, Literal
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from langchain_core.documents import Document

class RetrievedDoc(BaseModel):
    doc: Document
    relevance_score: float = Field(..., ge=0.0, le=1.0)
    source: str
    chunk_type: Literal["parent", "child"]
    headers: List[str] = Field(default_factory=list)
    lightrag_entities: List[str] = Field(default_factory=list)
    lightrag_relations: List[Dict] = Field(default_factory=list)

class AgentState(BaseModel):
    messages: Annotated[List[BaseMessage], add_messages]
    query: str
    plan: Optional[List[str]] = None
    retrieved_docs: List[RetrievedDoc] = Field(default_factory=list)
    critique: Optional[str] = None
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)
    iterations: int = Field(default=0, ge=0, le=3)
    final_answer: Optional[str] = None
    citations: List[Dict[str, str]] = Field(default_factory=list)
    wiki_output_path: Optional[str] = None
    lightrag_context: Optional[Dict] = None
    metadata: Dict = Field(default_factory=dict)  # tracing, timestamps, etc.
```

Use `checkpointer = MemorySaver()` (or AsyncSqliteSaver for production persistence).

## 4. Per-Node Detailed Design (Contracts, Inputs/Outputs, Prompts)

All nodes in `src/agents/`; each takes `state: AgentState` and returns `partial dict` for state update.

1. **query_analyzer**: Classify complexity (simple/factual vs. multi-hop/relational). Decide routing. Prompt: `prompts/analyzer.md` (rubric-based classification).

2. **planner**: Output numbered plan or sub-queries. Few-shot examples for multi-hop (e.g., "Compare X and Y" → sub-queries on each + synthesis).

3. **tool_router**: Structured output (Pydantic model) selecting tools + parameters. Support parallel tool calls where safe.

4. **researcher_grader**: 
   - Execute selected retrievers (vector + optional LightRAG).
   - Grade each doc with detailed rubric (relevance, completeness, recency, authority).
   - Filter (threshold 0.75) and reflect if collection is weak.
   - Conditional edge for reflection loop.

5. **generator**: Use filtered docs, plan, and critique to produce grounded answer with inline citations.

6. **critic**: Independent scoring (faithfulness 0–1 using RAGAS-style or custom LLM judge). Trigger loop if low.

7. **wiki_synthesizer**: Generate Obsidian-compatible Markdown (YAML frontmatter: `source`, `date`, `tags`, `confidence`; explicit [[WikiLinks]]; update `index.md` and `log.md`).

**Prompt Library** (`src/prompts/`): One `.md` file per node with:
- Strict system role + task.
- Detailed rubric or output format (JSON mode preferred).
- 2–4 few-shot examples (positive + negative).
- Chain-of-thought encouragement for reflection/planning.

## 5. Hybrid Retrieval & Indexing Design (65k MD Scale – Critical)

**Ingestion Pipeline** (`src/ingestion/pipeline.py` – memory-safe, incremental):

- **Loader**: `DirectoryLoader` with `**/*.md`, multiprocessing.Pool (16–32 workers, batch size 2000–5000 files).
- **Hierarchical Chunking** (2026 best practice for Markdown):
  1. `MarkdownHeaderTextSplitter` (header levels 1–4) → parent chunks (~2000–4000 tokens) with full header path in metadata.
  2. `RecursiveCharacterTextSplitter(chunk_size=400–512, chunk_overlap=50–100)` on parent content → child chunks.
  3. Link via `parent_id` UUID.
- **Vector Indexing**: Chroma.from_documents (separate collections or metadata flag for parent/child). Use MMR retrieval.
- **LightRAG Indexing**: After vector, `lightrag.insert_batch(parent_chunks)` (async, entity/relation extraction). Use OpenSearch backend for scale (Docker compose included). Support incremental via hash/timestamp check.
- **Resumability**: JSON checkpoint with processed file hashes. GC after each batch.
- **Target Performance**: <45 min full ingestion on 32 GB RAM machine; incremental <1 min for small changes.

**Retrieval Logic**:
- Vector: `k=15`, `fetch_k=50`, reranker (optional Cohere or cross-encoder).
- LightRAG: `mode="hybrid"` (low-level entities + high-level relations).
- Adaptive: Router prefers LightRAG for queries with "compare", "how", "relation", "who connected to".

## 6. Tools (Dynamic & Extensible)

- `hybrid_retrieve(query: str, use_lightrag: bool = True)`
- `web_search_tavily`
- `wiki_writer(markdown_content: str, title: str)`
- Calculator, arXiv fetcher (bonus).

## 7. Graph Construction (`src/graph/agentic_rag_graph.py`)

- `StateGraph(AgentState)`
- Add nodes + conditional edges for reflection (`should_continue_reflection` based on confidence/iterations).
- Parallel tool execution where possible.
- Full LangSmith tracing on every node (callbacks).

## 8. UI, CLI, Evaluation & Production Features

- **Streamlit** (`app.py`): Chat interface + expandable reasoning trace (node-by-node with scores, docs, critiques) + "Save to Wiki" button.
- **Typer CLI** (`cli.py`): `ingest --resume`, `query "..." [--hybrid] [--wiki] [--trace]`, `lint-corpus`, `eval`, `build-wiki`.
- **Evaluation Harness** (`src/evaluation/`): RAGAS (faithfulness, answer_relevancy, context_precision) + custom reflection score. 50+ golden query test set. Automated runs with JSON reports.
- **Observability**: LangSmith project per run; custom metadata for agentic metrics.
- **Docker**: Multi-container compose (app + Chroma + LightRAG OpenSearch + optional PostgreSQL).
- **Error Handling**: Graceful fallbacks, retry logic, rate limiting.

## 9. Phased Implementation Plan (Strict Order – With Checkpoints)

**Phase 0**: Project skeleton, requirements.txt, config, data models, prompts templates, Docker compose.  
**Phase 1**: Ingestion pipeline – full 65k MD benchmark + incremental mode + LightRAG indexing.  
**Phase 2**: Hybrid retriever + tools implementation.  
**Phase 3**: LangGraph core (state, nodes, edges, reflection/planning loops, memory).  
**Phase 4**: Multi-agent collaboration + critic + wiki synthesizer.  
**Phase 5**: Streamlit UI + CLI + tracing visualization + evaluation harness.  
**Phase 6**: Docker, tests, logging, security (API keys), README (diagrams, comparison table, benchmarks).  
**Phase 7**: End-to-end stress testing (100 complex queries), latency/quality benchmarks, final polish.

## 10. Success Criteria (Measurable & Verifiable)

1. Full 65k MD corpus ingested incrementally without OOM or crashes; benchmark logged.
2. Every complex query trace demonstrates **all 4 patterns** and **7 elements** visibly.
3. Reflection loop triggers on ≥30% of queries and measurably improves confidence/quality.
4. LightRAG hybrid mode shows superior performance on relational/multi-hop queries vs. pure vector.
5. Wiki synthesis produces clean, Obsidian-ready vault with proper frontmatter and links.
6. Evaluation: faithfulness ≥0.92, answer relevancy ≥0.90, average latency <4s on consumer hardware.
7. Code is clean, fully typed (Pydantic + mypy), documented, git-committed per phase.

## 11. References & Recommended Starters

- Paper PDF: https://arxiv.org/pdf/2501.09136
- YouTube Video: https://youtu.be/MT3DM82PRLc
- LightRAG GitHub (2026 features): https://github.com/hkuds/lightrag (OpenSearch support)
- Karpathy LLM Wiki Gist (for wiki_output style): https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- LangGraph Agentic RAG examples (2026 edition)

**Immediate Action**: Start with **Phase 0 + Phase 1** today. Focus on robust, resumable ingestion of the 65k MD corpus first.

When ingestion is complete and benchmarked, ping me for detailed prompt review and graph wiring session.

This is the **canonical, ultra-detailed production-grade Agentic RAG implementation** with hybrid LightRAG and persistent Karpathy-style compounding. Ship it clean, observable, and performant. 🚀




### Document: `study/agent_loop_v3.md`

_Embedded from `corpus/study/agent_loop_v3.md`. Also stored at `sources/study/agent_loop_v3.md` under this agent folder._


# Refined Agent Loop: Hierarchical, ReAct-Inspired, Production-Grade Design

**Version:** 2026-06-10 (v3 — Cognitive-Enhanced: Integrated high-priority traditional human thinking models from ranked analysis in thinking_model.md (Cynefin, Premortem, AAR, Double-Loop Learning, RPD, Dual Process, Metacognition, 5 Whys/Fishbone, Red Team, Paul-Elder, etc.) for adaptive context routing, proactive risk mitigation, fast/slow deliberation paths, structured reflection, and deeper self-evolution. All v2 details preserved; new mechanisms are additive, configurable, and mapped to existing phases.)  
**Research Sources**: "Why Do Multi-Agent LLM Systems Fail?" (MASFT taxonomy, 14-18 failure modes), Reflexion, Prospector, CGI, memory papers, xAI docs, developer reports on infinite loops/context issues, plus systematic review of 40+ human cognitive frameworks (ranked by adoption priority for agent loops).
**Purpose:** Actionable reference for building reliable, scalable LLM-based agent systems. Combines academic foundations (ReAct synergy of reasoning + acting), xAI's server-side agentic implementation (multi-agent orchestration for deep research), and advanced hierarchical patterns (planner + specialists + self-evolution).  
**Target Audience:** Builders of harnesses, multi-agent systems, coding agents, research agents (e.g., N1ch01as-style Architect with critic/self-refinement loops).  
**Key Principle:** Controlled loops with explicit state, structured outputs, quality gates, and hierarchical delegation. Not uncontrolled chain reactions — managed orchestration with bubbling-up consolidation and deliberate synthesis.

## 1. Core Principles (Refined from Research)

### 1.1 Foundational: ReAct Paradigm (Yao et al., ICLR 2023)
- **Definition**: Interleave **verbal reasoning traces (Thoughts)** with **actions** (tool calls, environment interactions, or delegation). Observations from actions ground and update reasoning.
- **Why it works**:
  - Pure Chain-of-Thought (CoT): Static, prone to hallucinations and error propagation (no external grounding).
  - Pure Acting: No high-level planning, poor exception handling, inefficient trajectories.
  - **ReAct synergy**: Thoughts decompose goals, track progress, handle exceptions, and replan. Actions provide real observations that correct reasoning and enable adaptation. Results in 10-34% gains on interactive tasks and reduced hallucinations on knowledge tasks.
- **Basic Cycle** (one iteration):
  1. **Thought**: LLM reasons about current state, goal, progress, next step, or exception. (Internal, updates context.)
  2. **Action**: Decide and output executable step (tool call with args, sub-agent delegation, or `Finish`/`Done`).
  3. **Observation**: Environment / tool / sub-agent returns structured result (data + metadata: status, confidence, summary, issues).
  4. Append to history/state → repeat.
- **Prompt Structure** (few-shot examples essential): Dense thoughts for reasoning-heavy tasks (QA/research); sparser for embodied/decision tasks. Use explicit tags or JSON schema for parseability.
- **Exception Handling**: Thought step detects failure ("Nothing useful returned") → replans or adjusts action in next iteration.

**xAI Alignment**: Grok's server-side agentic tool calling implements a production ReAct-style loop internally. The model decides tools, executes server-side (web_search, x_search, code_execution, collections_search), iterates until it can produce the final answer. Client sees only final (or streamed) output + optional reasoning tokens.

### 1.2 Production xAI Multi-Agent Orchestration (2026)
- **grok-4.20-multi-agent** (or equivalent): Launches configurable teams (4 agents for quick/focused; 16 for deep/comprehensive).
- **How the loop works**:
  - Server-side **realtime collaboration**: Multiple specialized agents run in parallel.
  - Each contributes reasoning, tool calls, findings.
  - **Leader agent** synthesizes discussion, cross-references, and delivers final structured answer.
  - Parallel tool invocation and iteration based on intermediate findings.
  - Sub-agent internal states encrypted/hidden by default (control + security); only leader outputs + (optionally) encrypted content exposed.
- **Strengths**: Deep multi-step research, structured outputs (tables, comparisons), realtime refinement, automatic tool use without client intervention in the loop.
- **Plan-first elements**: Complementary patterns in xAI tools like Grok Build CLI use explicit plan generation first, then parallel sub-agent execution (e.g., up to 8 sub-agents in isolated Git worktrees).

### 1.3 Hierarchical + Self-Evolving (AgentOrchestra / Surveys 2025-2026)
- **Central Planner / Orchestrator / Supervisor** at top level.
- Decomposes into sub-tasks → delegates to **specialized sub-agents** (Deep Researcher, Analyzer, Browser/Tool agents, Reporter, etc.).
- Each sub-agent runs its **own loop** (ReAct-style or domain-optimized).
- **Tree-structured routing** + results bubble up.
- **TEA Protocol inspiration** (Tool-Environment-Agent): Treat tools, environments, and agents as first-class, versioned, lifecycle-managed entities with standardized protocols for context, invocation, and evolution.
- **Closed feedback / Self-evolution**:
  - Reflection (verbal self-critique on traces).
  - Trace-based optimization (e.g., TextGrad-style: attribute errors → propose edits → validate on held-out → version/register).
  - Version manager: Register improved prompts/tools/agents; support rollback/select best.
  - Tracer for full execution trajectories (auditability + optimization signal).
- **Consolidation**: Planner aggregates sub-results, harmonizes evidence, resolves conflicts, updates global plan/state, or triggers refinement. Dedicated Reporter agent often handles final synthesis with citations/deduplication.
- **Performance evidence**: AgentOrchestra-style systems reach 89%+ on GAIA benchmark; sub-agents + self-evolution add double-digit gains; hierarchical routing improves scalability vs flat multi-agent.

**Overall Refined Model**: Start with ReAct core loop. Layer hierarchical delegation for complexity. Add explicit planning phase + reflection/critique gates + structured state/versioning for production reliability. xAI shows this can run server-side with strong orchestration primitives.

### 1.4 Cognitive Architecture Enhancements from Ranked Human Thinking Models (v3 Addition)

To further strengthen the loop against the failure modes detailed in Section 1.5, v3 explicitly incorporates high-adoption-priority traditional human thinking models (ranked by adoption priority for agent loops in the companion `thinking_model.md` — full table of 40 models with phases, similarities, strengths, and scores). These are mapped as first-class mechanisms rather than afterthoughts, delivering **adaptive intelligence** (context-aware routing), **proactive robustness** (pre-action risk), **efficient cognition** (fast/slow paths), and **deeper organizational learning** (double-loop + structured reflection). Prioritized models (scores 9–10) receive the deepest integration; others enhance specific sub-components (verifier, ideation, harmonization).

**Key Mappings & Operationalization in the v3 Loop**:

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

These additions are **production-aware**: all new steps are bounded, versioned, logged via tracer, and can be toggled or depth-limited per task. They transform the agent from a capable ReAct/hierarchical engine (v2) into a more cognitively complete system that thinks about its own thinking, anticipates failure, learns at multiple levels, and adapts its deliberation style to context — while fully preserving every v2 mechanism, code example, and mitigation.

### 1.5 Known Problems, Failure Modes & Targeted Mitigations (Research-Backed)

Recent systematic studies (especially the **MASFT taxonomy** from analysis of 150+ traces across popular multi-agent frameworks) identify that **most failures stem from design/spec issues (~40%+)**, coordination breakdowns, and weak verification/termination — **not raw model intelligence**. Single-agent ReAct loops suffer overlapping issues plus context bloat and repetitive behavior. Below is a synthesized taxonomy of the most common, well-documented problems, with **actionable mitigations** mapped directly to the phases in this document.

### Major Problem Categories & Frequency/Significance
1. **Specification & Design Ambiguities (Largest Category)**
   - Disobeying or misinterpreting task spec, vague roles, missing success criteria or output contracts.
   - **Impact**: Agents go off-track early; errors compound downstream.
   - **Mitigations**:
     - Phase 0: Mandatory structured Task Specification with explicit success criteria, constraints, output schema, and quality thresholds. Use "living spec" that can be updated.
     - Add automated spec validation (critic or schema check) before loop starts.
     - Clear role definitions and information contracts between orchestrator and sub-agents.

2. **Infinite Loops, Repetitive Actions & Thrashing**
   - Agent repeats the same (or similar) actions without progress; common in ReAct from poor exception handling or missing info; can be induced by prompt injection.
   - **Impact**: Wasted tokens/cost, timeouts, frustration (frequent real-world complaint).
   - **Mitigations**:
     - Phase 1 loop: Add **cycle detection** (state hashing of recent actions + observations; if similarity > threshold, force replan or terminate).
     - Explicit `max_steps`, `max_reflection_rounds`, and progress-based early exit (e.g., todo completion %).
     - Bounded reflection: Limit "improve this" iterations.
     - `Done` / `Finish` tool with mandatory verification before acceptance.
     - In hierarchical: Orchestrator monitors sub-agent progress and can kill/reassign stuck branches.

3. **Context Window Explosion / Context Rot / History Bloat**
   - Long trajectories cause key early info or instructions to be dropped; leads to inconsistency, repetition, goal drift.
   - **Impact**: Degraded performance in long-running or multi-turn tasks.
   - **Mitigations**:
     - Aggressive hierarchical memory: Short-term working memory + long-term persistent store (vector search, semantic caching, MemGPT-style).
     - Summarization at milestones or when context > threshold (signal-aware truncation).
     - Structured state (`task.md`, todo list, key facts only) instead of dumping full history every turn.
     - Sub-agents receive only relevant context slices + provenance.

4. **Hallucinations, Error Compounding & Verification Weakness**
   - Fabricated facts, incorrect tool results interpretation, or unverified claims propagating (worse in multi-agent).
   - **Impact**: Unreliable final outputs; cascading failures.
   - **Mitigations**:
     - **Verifier / Critic agents** as mandatory quality gates (Phase 3 consolidation and after sub-results).
     - Structured observation schema (status, confidence, issues list) + cross-validation (compare across agents/sources).
     - Multi-form verification (factual grounding in observations + external checks).
     - Trajectory ranking (e.g., Prospector-style critic selects best among multiple attempts).
     - In self-evolution: Only commit changes validated on held-out traces.

5. **Inter-Agent Misalignment & Coordination Failures (Multi-Agent Specific)**
   - Role overstepping, conflicting goals, stale state sharing, communication gaps, error propagation between agents.
   - **Impact**: Poor collaboration; sometimes single strong agent outperforms complex MAS.
   - **Mitigations**:
     - Strong central **Orchestrator/Planner** with explicit decomposition and routing (hierarchical control beats flat).
     - Information contracts + structured handoff formats.
     - Versioned shared state + durable coordination primitives (e.g., streams, pub/sub).
     - Circuit breakers: Detect inconsistency → pause, reconcile, or escalate.
     - Clear "Extreme hierarchical differentiation" (well-defined specialist roles).

6. **Termination & Goal Drift Problems**
   - Premature stopping (incomplete work) or failure to recognize completion; agents continue or give up wrongly.
   - **Impact**: Wrong or partial results.
   - **Mitigations**:
     - Explicit success criteria in spec + progress tracking against them.
     - Dedicated termination action (`Done` tool) that must pass verifier.
     - Periodic alignment checks in Thought step vs original objective.
     - Early termination signals when intermediate results satisfy criteria.

7. **Other Notable Issues**
   - **State staleness & memory failures**: Use hybrid memory (fast short-term + persistent long-term with retrieval).
   - **Security (prompt injection → loops or misuse)**: Sandbox tools, input sanitization, least-privilege tool access, monitoring for anomalous loops.
   - **Cost & scalability overhead**: Multi-agent only when benefit > coordination cost; monitor token usage per phase; parallel where safe.
   - **Debuggability**: Full tracer + structured logs are non-negotiable.

### How Mitigations Integrate into the Loop Phases
- **Phase 0 (Init)**: Spec engineering + validation is the single highest-ROI fix.
- **Phase 1 (Core Loop)**: Cycle detection, bounded steps/reflection, structured observations, progress tracking.
- **Phase 2 (Delegation)**: Narrow sub-specs + contracts; orchestrator monitoring.
- **Phase 3 (Consolidation)**: Verifier/critic gates, cross-validation, harmonization.
- **Phase 4 (Reflection/Self-evolution)**: Validation before applying changes; bounded loops.
- **Phase 5 (Termination)**: Verifier + explicit Done with evidence.

**Key Insight from Research**: Fixing **specification quality + verification layers + explicit termination controls** delivers the largest reliability gains. Adding more agents or raw model power without these often yields diminishing or negative returns.

## 2. The Complete Agent Loop Process (Actionable)

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
   - **Cynefin Classification** (context-aware routing): LLM or lightweight classifier tags the task (Simple / Complicated / Complex / Chaotic) based on clarity of cause-effect, expert knowledge needed, emergence, or crisis nature. Store in task_spec and use to auto-configure loop behavior (see 1.4 table): e.g., Simple/Complicated → prefer Fast Recognition Path + reduced reflection depth; Complex/Chaotic → enforce Full mode + AAR/Double-Loop + multi-critic ensemble.
   - **Premortem Analysis** (proactive risk critic): Before finalizing state, run dedicated step (orchestrator or Red Team critic): "Imagine this plan and spec have failed spectacularly after deployment. List the top 5-7 plausible causes. For each, propose concrete mitigations (update success_criteria, add todo risk items, tighten constraints, adjust agent roles, or add verification gates)." Merge mitigations into living spec and initial todo. This is now a recommended mandatory gate for all but the simplest tasks.
5. Decide architecture: Flat ReAct (simple) vs Hierarchical (complex research/coding) vs Hybrid. Also set initial `cognitive_profile` flags from Cynefin + task type (enable_fast_path, reflection_style, etc.).

**Actionable Output Format** (example JSON or Markdown section):
```json
{
  "task_id": "...",
  "objective": "...",
  "success_criteria": ["...", "..."],
  "constraints": ["max_steps: 50", "budget_tokens: 200k"],
  "output_format": "structured report with citations",
  "initial_plan": ["Step 1: ...", "Step 2: ..."],
  "quality_gates": ["completeness > 90%", "no hallucinations", "structured output"]
}
```

### Phase 1: Core Iteration Loop (ReAct-Inspired, Controlled)
While not terminated:
**v3 Mode Selection (Cynefin + RPD + Dual Process + Metacognition)**: At loop start or after major observation, determine operating mode:
- If Cynefin context is Simple/Complicated **and** high-similarity match found in Pattern Store (RPD) **and** metacognition confidence high → enter **Fast Recognition Path**: lightweight Thought (mental simulation only), skip verbose reasoning, proceed to action with minimal tokens. Log as "fast_path" for later AAR review.
- Otherwise (Complex/Chaotic, low pattern match, or explicit config) → **Full Deliberative Mode** (standard detailed ReAct Thought + full gates). Metacognition runs lightweight parallel monitor (bias scan, progress pulse, context drift check) and can force mode switch mid-iteration if uncertainty spikes.

1. **Observe Current State**: Load full/relevant history + task spec + current plan/todo + latest observations. (Summarize aggressively if context long — use memory manager. Also retrieve relevant Pattern Store entries for RPD matching.)
2. **Reason (Thought)**:
   - **Metacognitive overlay** (parallel): "Am I in the right mode? Any detected biases (per Paul-Elder)? Progress vs success criteria and todo? Context still matches Cynefin tag? Any governing assumptions to flag for Double-Loop later?"
   - Analyze progress vs success criteria.
   - Identify gaps, risks, exceptions.
   - Decide strategy: direct tool, delegate sub-task, synthesize so far, reflect/critique, or finish. (In Fast mode: keep this extremely concise.)
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

**Circuit Breaker Pattern (Recommended for Production)**

Circuit breakers prevent cascading failures when a tool, LLM call, or sub-agent is repeatedly failing. They have three states:
- **CLOSED**: Normal operation, requests go through.
- **OPEN**: Too many failures → fast-fail immediately (protects the system).
- **HALF_OPEN**: After timeout, allow limited test requests to check recovery.

Use one circuit breaker per tool type or per sub-agent role. Integrate with the retry wrappers below.

**Code Example: Minimal Controlled ReAct Loop with Cycle Detection (Python)**

```python
import hashlib
from typing import Any, Dict, List
from dataclasses import dataclass, field

@dataclass
class AgentState:
    task_spec: Dict[str, Any]
    history: List[Dict] = field(default_factory=list)
    todo: List[str] = field(default_factory=list)
    max_steps: int = 50
    seen_states: set = field(default_factory=set)  # for cycle detection

def hash_state(state: AgentState) -> str:
    """Simple cycle detection via recent action+obs hash"""
    recent = state.history[-3:] if len(state.history) > 3 else state.history
    return hashlib.md5(str(recent).encode()).hexdigest()

def controlled_react_loop(llm, tools, state: AgentState, max_retries: int = 3):
    import time
    import traceback

    step = 0
    while step < state.max_steps:
        step += 1
        current_hash = hash_state(state)
        if current_hash in state.seen_states:
            print("Cycle detected — forcing replan or terminate")
            # In production: trigger critic or escalate to human
            break
        state.seen_states.add(current_hash)

        try:
            # 1. Observe + build context (summarize if long)
            context = build_context(state)

            # 2. Reason + Decide (strict structured output)
            decision = llm.generate(
                prompt=build_decision_prompt(context, state.task_spec),
                output_schema={"thought": str, "action_type": str, "payload": dict}
            )

            if decision.action_type == "finish":
                if verify_output(decision.payload, state.task_spec):
                    return decision.payload
                else:
                    continue

            # 3. Execute with robust error handling
            obs = None
            if decision.action_type == "tool":
                obs = safe_execute_tool(decision.payload, tools, max_retries=max_retries)
            elif decision.action_type == "delegate":
                obs = safe_invoke_sub_agent(decision.payload, max_retries=max_retries)
            else:
                obs = {"status": "internal", "data": None}

        except Exception as e:
            # Structured error observation
            obs = {
                "status": "error",
                "error_type": type(e).__name__,
                "error_message": str(e),
                "traceback": traceback.format_exc(),
                "step": step
            }
            print(f"Error at step {step}: {e}")  # or send to tracer

        # 4. Structured observation + update state
        state.history.append({
            "thought": getattr(decision, 'thought', 'N/A'),
            "action": getattr(decision, 'action_type', 'error'),
            "observation": obs
        })
        update_todo(state, obs)

        # Optional: exponential backoff on errors
        if obs.get("status") == "error":
            time.sleep(min(2 ** (step % 5), 30))  # simple backoff

    return {"status": "max_steps_reached_or_error", "partial_result": state.history[-1]}


class CircuitBreaker:
    """
    Production-grade circuit breaker with proper Half-Open logic.

    States:
    - CLOSED: Normal operation. All calls go through.
    - OPEN: Too many failures. Fast-fail immediately to protect downstream systems.
    - HALF_OPEN: Recovery testing phase. Allow a limited number of test calls.
      - Success → back to CLOSED.
      - Failure → back to OPEN.
    """
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 30, half_open_max_calls: int = 1):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.half_open_max_calls = half_open_max_calls

        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"
        self.half_open_calls_made = 0  # track test calls in HALF_OPEN

    def _should_allow_request(self) -> bool:
        import time
        now = time.time()

        if self.state == "CLOSED":
            return True

        if self.state == "OPEN":
            if now - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF_OPEN"
                self.half_open_calls_made = 0
                return True
            return False

        if self.state == "HALF_OPEN":
            if self.half_open_calls_made < self.half_open_max_calls:
                self.half_open_calls_made += 1
                return True
            return False

        return False

    def call(self, func, *args, **kwargs):
        import time

        if not self._should_allow_request():
            return {
                "status": "circuit_open",
                "error": f"Circuit breaker is {self.state} - fast failing",
                "circuit_state": self.state
            }

        try:
            result = func(*args, **kwargs)

            # Success path
            if self.state == "HALF_OPEN":
                # Successful test call in recovery → fully recover
                self.state = "CLOSED"
                self.failure_count = 0
                self.half_open_calls_made = 0
            elif self.state == "CLOSED":
                self.failure_count = 0

            return result

        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()

            if self.state == "HALF_OPEN":
                # Test call failed during recovery → go back to OPEN
                self.state = "OPEN"
                self.half_open_calls_made = 0
            elif self.failure_count >= self.failure_threshold:
                self.state = "OPEN"

            raise e

    def should_retry(self) -> bool:
        """
        Returns True if we should attempt (or re-attempt) the operation.
        Useful for explicit "repeat if needed" logic outside the breaker.
        """
        return self.state in ("CLOSED", "HALF_OPEN")

    def reset(self):
        """Manually reset the circuit breaker to CLOSED state."""
        self.state = "CLOSED"
        self.failure_count = 0
        self.half_open_calls_made = 0
        self.last_failure_time = 0


def safe_execute_tool(payload: dict, tools: dict, max_retries: int = 3, circuit_breaker: CircuitBreaker = None) -> dict:
    """Retry wrapper for tool execution with structured error output + circuit breaker"""
    cb = circuit_breaker or CircuitBreaker()

    for attempt in range(max_retries):
        try:
            def _call():
                tool_name = payload.get("tool_name")
                args = payload.get("args", {})
                if tool_name not in tools:
                    return {"status": "error", "error": f"Unknown tool: {tool_name}"}
                result = tools[tool_name](**args)
                return {"status": "success", "data": result}

            result = cb.call(_call)
            return result
        except Exception as e:
            if attempt == max_retries - 1:
                return {
                    "status": "error",
                    "error_type": type(e).__name__,
                    "error_message": str(e),
                    "attempts": attempt + 1,
                    "circuit_state": cb.state
                }
            time.sleep(0.5 * (attempt + 1))
    return {"status": "error", "error": "Max retries exceeded", "circuit_state": cb.state}


def safe_invoke_sub_agent(payload: dict, max_retries: int = 2, circuit_breaker: CircuitBreaker = None) -> dict:
    """Wrapper for sub-agent delegation with retry, structured result + circuit breaker"""
    cb = circuit_breaker or CircuitBreaker(failure_threshold=3, recovery_timeout=60)

    for attempt in range(max_retries):
        try:
            def _call():
                result = invoke_sub_agent(payload)
                if result.get("status") in ["success", "partial"]:
                    return result
                raise RuntimeError(f"Sub-agent returned non-success: {result.get('status')}")

            result = cb.call(_call)
            return result
        except Exception as e:
            if attempt == max_retries - 1:
                return {
                    "status": "error",
                    "error_type": type(e).__name__,
                    "error_message": str(e),
                    "attempts": attempt + 1,
                    "sub_agent_payload": payload,
                    "circuit_state": cb.state
                }
            time.sleep(1)
    return {"status": "error", "error": "Sub-agent max retries exceeded", "circuit_state": cb.state}
```

**Code Example: Lightweight Verifier / Critic Agent (Prompt + Schema) — v3 Enhanced with Critic Modes + Paul-Elder Standards**

```python
VERIFIER_PROMPT = """
You are a strict, skeptical Verifier / Critic Agent operating in {critic_mode} mode.
Given the original task_spec and the candidate_output, 
return ONLY valid JSON with the schema below.

**Mode-specific instructions**:
- standard: Focus on factual grounding, completeness vs success_criteria, hallucination detection, format compliance.
- red_team: Adversarially attack the output — actively hunt for weaknesses, edge cases, hidden assumptions, single points of failure, or ways it could be misinterpreted/misused. Be creative and ruthless but evidence-based.
- paul_elder: Explicitly apply Paul-Elder Critical Thinking: evaluate Elements of Thought (purpose, question, information, concepts, assumptions, inferences, implications, point of view) and Intellectual Standards (clarity, accuracy, precision, relevance, depth, breadth, logic, significance, fairness, sufficiency). Flag violations with specific quotes/references.
- six_hats or ensemble: Incorporate multiple perspectives (or run sub-checks) and aggregate.

{
  "passes": true | false,
  "score": 0.0-1.0,
  "issues": ["list of concrete problems with evidence"],
  "suggestions": ["actionable fixes"],
  "confidence": 0.0-1.0,
  "critic_mode_used": "{critic_mode}",
  "paul_elder_violations": ["optional list if mode includes it"]
}

Task Spec: {task_spec}
Candidate Output: {candidate_output}
"""

def verify_output(candidate: dict, task_spec: dict, llm, critic_mode: str = "standard") -> dict:
    """v3 enhanced: Supports multiple critic modes. 'ensemble' runs 2-3 modes in parallel and merges results."""
    prompt = VERIFIER_PROMPT.format(
        task_spec=task_spec, 
        candidate_output=candidate,
        critic_mode=critic_mode
    )
    result = llm.generate(prompt, output_schema=...)  # force JSON
    # Optional: if critic_mode == "ensemble": run red_team + paul_elder in parallel and aggregate
    return result
```

**Code Example: Simple Self-Evolution / Reflection Step (Trace → Edit → Validate)**

```python
def self_evolve_component(component_name: str, trace: List[dict], llm, version_manager):
    """Minimal TextGrad / reflection-style evolution"""
    diagnosis = llm.generate(
        f"Analyze this execution trace and identify the root cause of any failures or inefficiencies:\n{trace}",
        output_schema={"root_cause": str, "target_component": str, "proposed_edit": str}
    )
    
    if diagnosis.target_component == component_name:
        new_version = apply_edit(component_name, diagnosis.proposed_edit)
        # Validate on held-out or re-execution
        if validate_improvement(new_version, trace):
            version_manager.register(new_version, parent=component_name)
            return new_version
    return None  # no change or rollback
```

**Termination Conditions** (checked every iteration or at gates):
- Success criteria met + quality gate passed.
- Max steps / token budget / time reached.
- Explicit `Done` / `Finish` action with validated output.
- Irrecoverable failure (escalate to human or higher orchestrator).
- Early exit if intermediate result satisfies objective.

### Phase 2: Hierarchical Delegation & Sub-Loops
When orchestrator decides to delegate:
1. **Decompose & Route**:
   - Planner selects or instantiates appropriate sub-agent type (specialist role, toolset, prompt template).
   - Creates narrow sub-task spec (subset of parent objective + relevant context slice).
   - Invokes sub-agent (can be same LLM with different system prompt/role, or different model).
2. **Sub-Agent Runs Independent Loop**:
   - Sub-agent executes its own ReAct-style iterations (or optimized variant) against its sub-spec.
   - Maintains local state/memory.
   - Can further delegate (tree) or call tools.
3. **Return Structured Result** to parent (bubbles up):
   - Same structured observation format above.
   - Includes provenance (which sub-agent, trace summary).
4. **Parent Handles**:
   - Records in global state/tracer.
   - Validates/integrates (merge with other branches, resolve conflicts via harmonization step).
   - Updates global plan/todo.
   - Decides next: more delegation, direct action, consolidate, or critique.

**Parallelism**: Where dependencies allow (e.g., independent research branches), run multiple sub-agents/tools concurrently (xAI multi-agent style or worktree isolation like Grok Build).

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

**Example Consolidator Prompt Snippet**:
"You are a synthesis expert. Given the original task spec, current plan, and these sub-results [structured list], produce: 1) Updated progress summary. 2) Any conflicts resolved. 3) Draft final output section. 4) Remaining gaps and recommended next actions."

### Phase 4: Reflection, Critique & Self-Evolution (Advanced)
**v3 Structured Reflection (AAR + Double-Loop + 5 Whys / Ishikawa + Paul-Elder / Red Team)**: All reflections now follow an explicit, multi-layered protocol (configurable via task_spec.reflection_style). This upgrades the original verbal self-critique into a rigorous, multi-model cognitive process.

- **Mandatory AAR Template** (applied at every milestone, failure, or termination; directly from After-Action Review best practice):
  1. **What was supposed to happen?** — Re-state relevant parts of original task_spec, success criteria, plan, and expected observations.
  2. **What actually happened?** — Summarize from tracer + structured observations (successes, partials, errors, key metrics). Include Fast vs Full mode usage stats if applicable.
  3. **Why? (Diagnosis)** — 
     - First pass: Standard attribution (TextGrad-style or LLM).
     - Deep pass (if issues or Cynefin=Complex): Apply **5 Whys** iteratively on top 2-3 problems. Then categorize using **Ishikawa Fishbone** (or lightweight fault tree): e.g., Prompts/Methods, Models/Tools/Agents, Data/Observations, Context/Environment, State/Memory, Verification Gates, Human Spec.
     - Cross-check with **Paul-Elder** lens: Which elements of thought were weak? Which intellectual standards violated (accuracy? depth? fairness?)?
  4. **What next? (Actionable Lessons)** — Concrete, versionable changes. Prioritize by impact/effort.

- **Double-Loop Learning Layer** (always after AAR single-loop diagnosis, before committing changes):
  - "Beyond fixing the immediate symptoms: What *governing variables* or foundational assumptions created the conditions for this outcome? Examples: Was our definition of 'quality output' too loose? Did agent role boundaries allow drift? Is the memory retrieval strategy misaligned with task type? Should success criteria themselves evolve? Should we add new critic roles or change loop routing logic?"
  - Only changes that survive this meta-question are proposed for validation + registration. This prevents superficial patching and enables genuine architectural self-improvement.

- **Per-trajectory or milestone reflection** (original): LLM summarizes trace, diagnoses failures/successes, proposes improvements (prompt edits, tool patches, new sub-agent types). Now wrapped inside the AAR + Double-Loop structure above.

- **Self-evolution loop** (inspired by AgentOrchestra, enhanced):
  1. Collect trace via tracer + AAR output.
  2. Attribute errors / opportunities (LLM or TextGrad-style) **within AAR/Double-Loop frame**.
  3. Propose targeted changes (to prompts, tools, agent configs, success criteria, or even generated code / memory schemas).
  4. Validate changes (re-execute on held-out or similar task; check metrics; optionally re-run Premortem on proposed new version).
  5. If improved (and Double-Loop approved): Register new version (with lineage + AAR justification). Support rollback. Update Pattern Store with outcome metadata for future RPD use.
  6. Optional: If change is meta (e.g., new critic mode or routing rule), propagate to cognitive_profile defaults.

- **Critic Agent Role** (enhanced): Separate lightweight agent that reviews drafts/plans without full execution. Can be invoked at gates. Now supports multiple modes (standard | red_team | paul_elder | six_hats | ensemble) as defined in Section 1.4. Red Team mode is especially recommended during Premortem and high-stakes consolidation.

- **Benefits**: Continuous improvement during runtime; production systems become more robust over repeated use on similar task distributions. The combination of AAR structure, Double-Loop depth, systematic root-cause (5 Whys/Fishbone), and multi-perspective critics (Paul-Elder/Red Team) makes Phase 4 a true engine for compounding intelligence rather than just incremental fixes. Fast-path traces are still reviewed (lighter AAR) so the system can learn when to trust RPD matches.

**Implementation Tip**: Store AAR outputs as structured artifacts linked to versions in the registry. This creates an auditable "learning history" that future agents (or the same system on similar tasks) can retrieve for RPD-style pattern matching.

### Phase 5: Termination & Output
- When gates passed or termination condition met:
  1. Final synthesis pass.
  2. Structured final output (match spec).
  3. Optional: Post-hoc reflection summary for user or logging.
  4. Persist full trace + versions for audit/replay/debug.
- **Human-in-loop hooks**: At quality gate failures, high-stakes actions, or budget exhaustion.

## 3. State, Memory & Infrastructure Recommendations

- **State Schema**: task_spec + current_plan/todo + history (thought/action/observation tuples) + memory (key-value or vector) + versions + tracer.
- **Memory Management**: Hierarchical (local per sub-agent + global). Summarization on context pressure. Session-isolated for concurrency.
- **Tracing**: Full execution graph (who called what, results, timings, versions). Enables debugging, reflection, and optimization.
- **Versioning** (TEA-inspired): Prompts, tools, agent roles, generated artifacts — all versioned with semantic lineage and rollback.
- **xAI Integration Tips**:
  - Use Grok multi-agent mode for research-heavy top-level tasks.
  - Mix server-side agentic tools with client-side custom tools (hybrid).
  - For coding agents: Adopt plan-first + parallel sub-agents in isolated environments (worktrees).
  - Stream reasoning tokens when possible for transparency.
- **Production Hardening**:
  - Strict output schemas (JSON mode or constrained decoding).
  - Timeouts, retry with backoff, circuit breakers on failing tools/sub-agents.
  - Cost/token budgets + monitoring.
  - Logging + observability (every thought/action/observation).
  - Sandboxed execution for tools/code.

## 4. Decision Framework (When to Use What)

| Task Complexity       | Recommended Pattern                  | Key Features to Enable          | Example Use Case |
|-----------------------|--------------------------------------|---------------------------------|------------------|
| Simple fact lookup    | Flat ReAct (single loop)            | Tool calling, basic thought    | Quick search + answer |
| Multi-step research   | xAI Multi-Agent or Hierarchical     | Parallel agents, leader synth  | Deep analysis with sources |
| Coding / long project | Plan-first + Hierarchical + Worktrees | Sub-agents in isolation, todo.md | Full app generation + debug |
| Open-ended / creative | ReAct + Reflection + Self-evolution | Critic gates, versioned prompts| Iterative design refinement |
| High-stakes / reliable| All above + strong Quality Gates    | Structured results, validation | Enterprise automation |

## 5. Common Pitfalls & Mitigations (from Research)

**Primary reference: See the full MASFT-style taxonomy, failure modes, and phase-specific mitigations in Section 1.5 above.** The points below are retained for quick scanning and now include additional patterns from recent studies.

- **Context explosion**: Aggressive summarization + hierarchical state (local sub-memories).
- **Infinite loops / thrashing**: Hard max iterations + progress tracking in todo + critic that can force replan or escalate.
- **Poor consolidation**: Mandate structured sub-results + dedicated harmonization/reporter step.
- **Hallucinations in plans**: Ground every major claim in observations; use critic before committing to plan.
- **Brittle delegation**: Use explicit sub-task specs + success criteria; validate returned results.
- **Lack of visibility**: Full tracing + optional streaming of reasoning.

## 6. Quick-Start Pseudocode Skeleton (Python-like)

```python
def agent_loop(task_instruction, tools, sub_agent_registry, max_steps=50):
    state = initialize_state(task_instruction)  # spec, plan, todo, memory, tracer
    orchestrator = get_llm(role="orchestrator")
    
    while not should_terminate(state, max_steps):
        # 1. Observe
        context = build_context(state)
        
        # 2. Reason + Decide
        decision = orchestrator.generate(
            prompt=build_decision_prompt(context, state.spec),
            output_schema=DECISION_SCHEMA  # thought, action_type, payload
        )
        
        if decision.action_type == "tool":
            obs = execute_tool(decision.payload, tools)
        elif decision.action_type == "delegate":
            sub_result = invoke_sub_agent(decision.payload, sub_agent_registry)  # runs its own loop
            obs = structured_observation_from(sub_result)
        elif decision.action_type == "synthesize":
            obs = consolidate_and_gate(state)
        elif decision.action_type == "finish":
            return finalize_output(state, decision)
        
        # 3. Update state
        state.history.append(decision.thought, decision, obs)
        state = update_todo_and_plan(state, obs)
        
        # 4. Optional light reflection or full self-evolution pass
        if should_reflect(state):
            state = reflect_and_evolve(state)  # critique + version updates
    
    return handle_termination(state)
```

Sub-agent invoke follows the same pattern recursively (narrower scope).

## 7. References & Sources

- **ReAct Foundational**: Yao et al. "ReAct: Synergizing Reasoning and Acting in Language Models" (arXiv:2210.03629, ICLR 2023).
- **xAI Production**: xAI Developer Docs (Multi-Agent orchestration, server-side agentic tool calling, Grok Build CLI patterns) — realtime multi-agent research with leader synthesis; 4/16 agent teams.
- **Hierarchical & Advanced**:
  - "AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool–Environment–Agent (TEA) Protocol" (arXiv ~2026) — hierarchical planner, TEA protocols, self-evolution via reflection/TextGrad-style, strong GAIA results.
  - Surveys: "The Landscape of Emerging AI Agent Architectures..." (2024); "Large Language Model Agent: A Survey..." (2025); "LLM-based Agentic Reasoning Frameworks: A Survey" (2025).
- Additional patterns: Reflexion (self-reflection), Plan-and-Execute variants, LATS (tree search), MetaGPT / AgentVerse / DyLAN (multi-agent collaboration).

---

**Next Steps for Implementation**:
1. Start with a minimal ReAct harness in your preferred framework (LangGraph, custom loop, or xAI SDK).
2. Add structured observation schema and todo/state management.
3. Layer hierarchical delegation + consolidation.
4. Instrument tracing + quality gates.
5. Experiment with reflection/self-evolution on repeated task types.
6. Integrate xAI multi-agent mode for research sub-tasks.

This document is designed to be **executable guidance** — copy patterns, adapt pseudocode, and iterate. For refinements, specific code examples in Python/Node, or integration with your existing harness (e.g., critic loops, spec-driven task.md), provide more details on your current stack.

**File created at**: `/home/workdir/artifacts/agent_loop_v3.md` (v3 cognitive-enhanced edition with integrations from ranked human thinking models table in thinking_model.md; all original v2 content, code examples, mitigations, and structure preserved and extended)



### Document: `study/knowledge_router_agent.md`

_Embedded from `corpus/study/knowledge_router_agent.md`. Also stored at `sources/study/knowledge_router_agent.md` under this agent folder._


# Knowledge Router Agent — Complete Specification & Implementation Guide
**Version:** 1.0  
**Date:** 2026-06-06  
**Status:** Production-Ready Spec (Rethought across research papers, best practices, and your specific use cases)  
**Domains:** AI Filmmaking (text-to-video, consistency, cinematic pipelines) + AI Agents (multi-agent orchestration, advanced RAG, self-improving systems)  
**Philosophy:** Spec-driven, critic-loop heavy, hybrid deterministic + learned routing, fully traceable, continuously improving.

---

## Executive Summary

The **Knowledge Router Agent** is the central intelligence layer that ensures every specialized agent in your system (Character Consistency Critic, Video Prompt Optimizer, Multi-Agent Orchestrator Designer, Shot Planning Agent, etc.) receives **precisely the right knowledge** from your growing ~5,000-file `.md` corpus — with minimal noise, high precision, and strong explainability.

It draws from 2025–2026 research (AgentRouter’s graph-guided GNN routing with performance supervision, RopMura/RIRS centroid-based + iterative planning, Self-RAG reflection tokens, CRAG corrective retrieval, MasRouter unified routing, and production patterns from xAI Grok multi-agent modes) while being fully generalized for any knowledge-intensive domain.

**Core Innovations in This Design**
- **Hybrid Routing Stack** (Metadata-first → Cluster/Centroid semantic → Graph traversal → LLM ranker with reflection)
- **Dual Planner + Router** for complex multi-hop creative/technical pipelines
- **Built-in Multi-Level Critic** (retrieval quality, routing decision, downstream utility) inspired by Self-RAG
- **Performance-Supervised Improvement** (soft labels from actual agent success, like AgentRouter)
- **Traceable + Explainable** by design
- **Training-free bootstrap** (RopMura style) with optional learned components
- **Domain packs** for your key agents (Character Consistency, Prompt Engineering for Video, Agentic Video Production, etc.)

This spec is ready for direct implementation or feeding into your N1ch01as Architect coding agents.

---

## 1. Purpose & Success Criteria

**Purpose**  
Serve as the single, intelligent gateway between any requesting agent and the curated knowledge base. It must understand *who* is asking, *what* they need, and *why*, then deliver the optimal context pack with full reasoning.

**Success Criteria (Quality Gates)**
- Retrieval precision (relevant files returned in top results): ≥ 88% (critic or human eval)
- Routing decision quality (downstream agent success improvement): measurable lift
- Latency: < 4s p95 for standard queries; < 8s for complex pipeline queries
- Explainability: 100% of decisions produce human-readable + structured trace
- Continuous improvement: Routing accuracy improves over time via critic feedback and performance signals
- Cost efficiency: Avoids over-retrieval; supports cost-aware routing

---

## 2. Architecture Overview

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

---

## 3. Input / Output Contract (Strict & Rich)

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

---

## 4. Core Components (Detailed)

### 4.1 Query Analyzer + Intent Classifier
- Parses task_description + required_concepts + previous_failures.
- Extracts entities (tools: Seedance, Kling; concepts: character_consistency).
- Classifies complexity and whether Planner is needed.
- Uses lightweight reflection: “Is this query about a single technique or a full pipeline?”

### 4.2 Planner (for High-Complexity / Pipeline Queries)
Inspired by RopMura: When `routing_hints.complexity == "pipeline"` or `multi_hop_expected == true`:
- Decomposes into sub-tasks (e.g., 1. Character bible creation, 2. Shot-by-shot consistency rules, 3. Lighting-specific mitigations, 4. Tool-specific prompt patterns).
- Routes sub-tasks iteratively or in parallel.
- Uses Question Simplifier / Response Evaluator loop (max 4–5 rounds).

### 4.3 Hybrid Retrieval Engine (The Heart)
**Layered Approach (in order):**

1. **Metadata Hard Filters** (fast, deterministic, 70-80% reduction)
   - Exact match on `agent_relevance`, `category`, `tags` intersection, `quality_score`, recency, etc.

2. **Cluster / Centroid Semantic Retriever** (RopMura-inspired, efficient)
   - Pre-compute coherent clusters per major subcategory (consistency_systems, prompt_engineering_video, multi_agent_patterns, etc.).
   - Store only centroids + representative files.
   - Query embedding → Top-K centroids → expand to files in those clusters.
   - Great for scaling without broadcasting to entire 5k corpus.

3. **Graph Explorer** (AgentRouter-inspired)
   - Lightweight traversal or small heterogeneous GNN (if you train one later).
   - Nodes: techniques, tools (Seedance, Kling, LangGraph), failure_modes, papers, agent_roles.
   - Relations: improves, requires, common_failure_when, used_together_with, mitigates.
   - Example path: `character_consistency` → `improves` → `multi_shot_narrative` + `failure_mode:clothing_drift_under_dramatic_lighting`.

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

This turns the Router into a learning system over time.

---

## 5. Particular Use Case Implementations

### Use Case 1: Character Consistency Critic Agent
**Request Example**: See Input contract above (wuxia fight scene).

**Router Behavior**:
- Hard filter: `tags CONTAIN character_consistency AND multi_shot`
- Graph: Pulls “clothing_drift” failure mode nodes + mitigation techniques
- Returns structured pack: “Best reference sheet practices for Seedance + Kling”, “Lighting-induced color shift mitigations”, “Multi-shot coherence checklist”
- Critic checks coverage of “previous_failures”

### Use Case 2: Video Prompt Optimizer Agent
- Prioritizes files tagged `prompt_engineering`, `camera_movement_prompts`, `lighting_prompts`, `negative_prompts`, `seedance_prompt_formulas`, `2026_best_practices`
- Graph traversal for “prompt formula that worked with dynamic camera in cinematic scenes”
- Returns prompt templates + before/after examples + common failure prompts to avoid

### Use Case 3: Multi-Agent Orchestrator Designer
- Routes to `multi_agent_patterns`, `langgraph`, `crewai_roles`, `memory_architectures`, `production_ready_patterns`, `agentic_video_production`
- Planner decomposes: “Orchestration for consistency across shots” + “Cost/latency optimization for video gen agents”
- Returns role definitions, graph patterns, and real pipeline examples from your corpus

### Use Case 4: Shot Planning Agent (Script → Shot List → Generation)
- High complexity → activates Planner
- Iterative routing across scriptwriting, cinematography language, tool-specific shot capabilities, consistency constraints
- Final pack: Structured shot list template + per-shot prompting guidance + consistency guardrails

**Generalization Note**: For any new domain, simply:
- Add `agent_relevance` values in frontmatter
- Define new clusters / graph node types
- Optionally create a small “Domain Pack” template

---

## 6. Knowledge Base Integration Requirements

Every `.md` file **must** have rich frontmatter (this is non-negotiable for the Router to work well):

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

**Recommended Additions for Scale**:
- Pre-computed cluster_id or centroid_id per file
- Graph node references (optional but powerful)

---

## 7. Phased Implementation Roadmap

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

---

## 8. Evaluation Framework

- **Offline**: Golden test set of 50–100 representative queries per major agent role. Measure precision@K, recall of required_concepts, critic scores.
- **Online**: Track downstream agent success rate before/after Router improvements. Log critic scores and human spot-checks.
- **Ablation**: Test impact of each layer (metadata only vs +graph vs +reflection).
- **Continuous**: Router critic proposes improvements to the knowledge base itself (new tags, missing content detection).

---

## 9. Edge Cases & Mitigations

- **Very broad query** → Planner forces decomposition + strict max_files.
- **No good matches** → Router returns “Insufficient high-quality knowledge” + suggestions to expand corpus + low confidence flag.
- **Conflicting information** across files → Graph + Critic prioritize higher quality_score + more recent + explicit failure mode coverage.
- **New agent role appears** → Easy extension: add to `agent_relevance` tags; Router gradually learns via feedback.
- **Latency spikes on complex queries** → Planner has round limits; fallback to simpler retrieval.

---

## 10. Tech Recommendations (Aligned with Your Stack)

- **Orchestration**: LangGraph or your custom harness (excellent for stateful Planner + Router + Critic loops)
- **Vector + Metadata**: LlamaIndex or Haystack with Qdrant/Pinecone (strong metadata filtering)
- **Graph**: Lightweight NetworkX/Neo4j for traversal; optional small GNN later (PyG or DGL)
- **Embeddings**: High-quality model (e.g., voyage, Snowflake, or your preferred)
- **LLM for Analyzer/Ranker/Critic**: Mix of strong reasoning model (Grok 4, Claude 4, DeepSeek R1, etc.) + cheaper models for simple steps
- **Storage**: All `.md` files in git + vector DB + optional graph DB

---

## 11. Generalization to Any Domain

This design is deliberately **domain-agnostic at the core**:
- Replace `category` / `subcategory` / `agent_relevance` with your new domain’s taxonomy.
- Define new clusters and graph schemas.
- The Hybrid Retrieval + Planner + Multi-Level Critic pattern transfers directly.

Your AI Filmmaking + AI Agents corpus is actually an **excellent stress test** because it combines creative, technical, and meta-agent knowledge — success here means the Router will generalize extremely well.

---

## Next Steps (Recommended)

1. Review and refine this spec with your main Critic Agent.
2. Start Phase 1 implementation (I can generate the detailed task.md + code skeletons next).
3. Audit/enrich frontmatter on your top 300–500 highest-value files.
4. Build the first version of the Metadata + Vector layer and test with 2–3 of your real agents.

This specification has been deeply researched and rethought for production robustness, your specific creative + agent use cases, and alignment with the latest 2025–2026 research patterns.

**File created at:** `/home/workdir/artifacts/knowledge_router_agent.md`

Ready for the next artifact (task.md for implementation, code skeletons, or graph schema)? Just say the word. We can iterate until it is perfect for your N1ch01as Architect ecosystem.


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

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 53 | OrchestratorAgent | DAG execution, retries, fan-out/fan-in | — |
| 54 | PlannerAgent | Decomposes brief into phased DAG | — |
| 55 | RouterAgent | Picks right agent + model for subtask | — |
| 56 | JudgeAgent | Adjudicates disputes via debate | — |
| 57–80 | (Various meta-agents) | Memory, continuity, safety, escalation, etc. | — |



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

| Passes | Primary question |
|---|---|
| **1-20** | Are all extracted claims traceable to the reference set and aligned with the document's structure? |
| **21-40** | Does the architecture describe the real control plane: orchestration, memory, assets, delivery, and observability? |
| **41-60** | Are workflow handoffs explicit enough for implementation, QA, continuity, and compliance automation? |
| **61-80** | Are metrics, thresholds, and evaluation layers technically coherent across creative, technical, and business gates? |
| **81-100** | Is the wording unambiguous, internally consistent, and suitable for professional technical documentation? |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 53 | **OrchestratorAgent** | Runs the CrewAI / AutoGen / LangGraph DAG; schedules nodes; handles retries, timeouts, fan-out/fan-in | LangGraph + CrewAI + AutoGen reference patterns; Airflow/Temporal workflow corpora; PGA producer-schedule templates | DAG completion rate ≥99.5%; SLA adherence; deadlock rate = 0 | Lower mean time-to-delivery than human EP/line-producer at same scope | ProducerAgent (scope), JudgeAgent (dispute), HiTL on stall | All agents (resource burn, retry storms) |
| 54 | **PlannerAgent** | Decomposes a brief into a phased DAG with agent assignments + critic gates | Production-management corpora; PMBOK; CrewAI task graphs; phase templates from `human_video_production_workflow.md` | Plan validity (no missing critic gate); estimated cost variance vs actual <10% | Produces tighter, cheaper plans than producer-EP first pass in blind A/B | ProducerAgent, FinanceAgent (budget) | RouterAgent (wrong agent picked), OrchestratorAgent |
| 55 | **RouterAgent** | Picks the right specialist agent (and model) for each subtask | Agent-capability registry; benchmark history (cost/quality/latency per agent × task type) | Routing accuracy ≥95% vs oracle; cost-per-task within budget | Beats human producer in agent/vendor selection on cost-adjusted quality | OrchestratorAgent, CostOptimizerAgent | PlannerAgent (bad decomposition) |
| 56 | **JudgeAgent** | Adjudicates inter-agent disputes via multi-agent debate; scores outputs against rubric | Du et al. 2023 (LLM debate); MT-Bench rubrics; guild scoring sheets (DGA/WGA/ASC/ACE) | Inter-rater agreement vs human expert panel ≥0.8 Cohen's κ | Higher κ vs human jury than median human juror | HiTL on overturned rulings | DirectorAgent, ScreenwriterAgent, any disputing pair |
| 57 | **GateKeeperAgent** | Manages phase transitions; verifies L1/L2/L3 success criteria; signs C2PA provenance | Stage-gate methodology; PGA Producers Mark; QMS audit patterns | Zero leaked defects past gate; sign-off SLA hit rate ≥99% | Lower escaped-defect rate than human QA lead | ComplianceAgent, AIQAConsistencyAgent | OrchestratorAgent (premature advance) |
| 58 | **MemoryAgent** | Episodic + long-term project memory; retrieval for any agent | Reflexion (Shinn 2023); MemGPT; vector-DB best practices | Retrieval precision@5 ≥0.9 on project Q&A; freshness SLA | Higher recall than producer's project bible at scale | All agents (correction events) | All agents (stale facts) |

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

**Acceptance rules:**
1. **Blocker** severity halts the DAG until resolved.
2. **Major** triggers a Self-Refine / Reflexion loop (max 3 iterations) on the receiving agent.
3. **Minor / nit** is logged to the agent's memory store and aggregated for the next training cycle (RLAIF reward signal).
4. Disputes between two agents go to a **JudgeAgent** running multi-agent debate (Du et al. 2023) with the relevant rubric as the constitution; if unresolved, escalates to a HumanInTheLoop reviewer.
5. Every accepted critique is appended to the artifact's C2PA provenance chain so downstream agents and humans can audit.



### From `corpus/study/agent_loop_v2.md` Copy: `sources/excerpts/agent_loop_v2.md`.


**Version:** 2026-06-07 (Updated with comprehensive research on known agent loop failure modes from MASFT taxonomy & related studies, plus targeted mitigations from Reflexion, critic frameworks, structured specs, memory architectures, and production patterns)  
**Research Sources**: "Why Do Multi-Agent LLM Systems Fail?" (MASFT taxonomy, 14-18 failure modes), Reflexion, Prospector, CGI, memory papers, xAI docs, and developer reports on infinite loops/context issues.
**Purpose:** Actionable reference for building reliable, scalable LLM-based agent systems. Combines academic foundations (ReAct synergy of reasoning + acting), xAI's server-side agentic implementation (multi-agent orchestration for deep research), and advanced hierarchical patterns (planner + specialists + self-evolution).  
**Target Audience:** Builders of harnesses, multi-agent systems, coding agents, research agents (e.g., N1ch01as-style Architect with critic/self-refinement loops).  
**Key Principle:** Controlled loops with explicit state, structured outputs, quality gates, and hierarchical delegation. Not uncontrolled chain reactions — managed orchestration with bubbling-up consolidation and deliberate synthesis.

3. **Context Window Explosion / Context Rot / History Bloat**
   - Long trajectories cause key early info or instructions to be dropped; leads to inconsistency, repetition, goal drift.
   - **Impact**: Degraded performance in long-running or multi-turn tasks.
   - **Mitigations**:
     - Aggressive hierarchical memory: Short-term working memory + long-term persistent store (vector search, semantic caching, MemGPT-style).
     - Summarization at milestones or when context > threshold (signal-aware truncation).
     - Structured state (`task.md`, todo list, key facts only) instead of dumping full history every turn.
     - Sub-agents receive only relevant context slices + provenance.

7. **Other Notable Issues**
   - **State staleness & memory failures**: Use hybrid memory (fast short-term + persistent long-term with retrieval).
   - **Security (prompt injection → loops or misuse)**: Sandbox tools, input sanitization, least-privilege tool access, monitoring for anomalous loops.
   - **Cost & scalability overhead**: Multi-agent only when benefit > coordination cost; monitor token usage per phase; parallel where safe.
   - **Debuggability**: Full tracer + structured logs are non-negotiable.

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

### Phase 2: Hierarchical Delegation & Sub-Loops
When orchestrator decides to delegate:
1. **Decompose & Route**:
   - Planner selects or instantiates appropriate sub-agent type (specialist role, toolset, prompt template).
   - Creates narrow sub-task spec (subset of parent objective + relevant context slice).
   - Invokes sub-agent (can be same LLM with different system prompt/role, or different model).
2. **Sub-Agent Runs Independent Loop**:
   - Sub-agent executes its own ReAct-style iterations (or optimized variant) against its sub-spec.
   - Maintains local state/memory.
   - Can further delegate (tree) or call tools.
3. **Return Structured Result** to parent (bubbles up):
   - Same structured observation format above.
   - Includes provenance (which sub-agent, trace summary).
4. **Parent Handles**:
   - Records in global state/tracer.
   - Validates/integrates (merge with other branches, resolve conflicts via harmonization step).
   - Updates global plan/todo.
   - Decides next: more delegation, direct action, consolidate, or critique.

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

## 3. State, Memory & Infrastructure Recommendations

- **State Schema**: task_spec + current_plan/todo + history (thought/action/observation tuples) + memory (key-value or vector) + versions + tracer.
- **Memory Management**: Hierarchical (local per sub-agent + global). Summarization on context pressure. Session-isolated for concurrency.
- **Tracing**: Full execution graph (who called what, results, timings, versions). Enables debugging, reflection, and optimization.
- **Versioning** (TEA-inspired): Prompts, tools, agent roles, generated artifacts — all versioned with semantic lineage and rollback.
- **xAI Integration Tips**:
  - Use Grok multi-agent mode for research-heavy top-level tasks.
  - Mix server-side agentic tools with client-side custom tools (hybrid).
  - For coding agents: Adopt plan-first + parallel sub-agents in isolated environments (worktrees).
  - Stream reasoning tokens when possible for transparency.
- **Production Hardening**:
  - Strict output schemas (JSON mode or constrained decoding).
  - Timeouts, retry with backoff, circuit breakers on failing tools/sub-agents.
  - Cost/token budgets + monitoring.
  - Logging + observability (every thought/action/observation).
  - Sandboxed execution for tools/code.

```python
def agent_loop(task_instruction, tools, sub_agent_registry, max_steps=50):
    state = initialize_state(task_instruction)  # spec, plan, todo, memory, tracer
    orchestrator = get_llm(role="orchestrator")



### From `corpus/study/agent_loop.md` Copy: `sources/excerpts/agent_loop.md`.


| Category                        | % Impact | Key Problems                          | Primary Mitigations                              |
|--------------------------------|----------|---------------------------------------|--------------------------------------------------|
| Specification & Design         | ~40%+   | Vague specs, missing success criteria | Structured Task Spec + validation in Phase 0    |
| Infinite Loops / Thrashing     | High    | Repetitive actions, no progress       | Cycle detection + `max_steps` + progress gates  |
| Context Explosion / Rot        | High    | Lost information in long histories    | Hierarchical memory + structured state + summarization |
| Verification & Hallucination   | High    | Unchecked outputs, error compounding  | Verifier/Critic agents + structured observations |
| Coordination & Misalignment    | High    | Role conflicts, stale state           | Strong orchestrator + information contracts     |
| Termination Problems           | Medium  | Premature stop or never stops         | Explicit `Done` action + quality gates          |

### Phase 0: Initialization (Spec-Driven)
1. Parse instruction → create **structured Task Specification** (objective, success criteria, constraints, output format, budgets, quality thresholds).
2. Initialize state: `task.md`, todo list, memory, tracer, version registry.
3. (Optional but recommended) Generate high-level plan and validate it.
4. Decide architecture: Flat ReAct vs Hierarchical.



### From `corpus/study/lifes_quiet_redemption_agent_workflow.md` Copy: `sources/excerpts/lifes_quiet_redemption_agent_workflow.md`.


### D4 · Character-Consistency Identity Stack
![Character consistency identity stack: bible, visual anchoring, per-character LoRA, RL identity, memory conditioning, fallback, VLM audit](./workflows/lqr-character-consistency.svg)

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

Because the swarm persists character bibles (MemoryAgent #58), identity hashes (AvatarDesignAgent #47), and style LoRAs (StyleTransferAgent #61), a follow-up short reuses ~70% of pre-production. New entries in the 「生活偷偷救赎了我们」 series only re-run Phases 1–4 for new beats, while ContinuityAgent guarantees the recurring "map girl" and "shop cat" stay consistent across episodes.

| Reuse Asset | Stored By | Enables |
|---|---|---|
| Character bible + identity hashes | MemoryAgent, AvatarDesignAgent | Same faces across episodes |
| Style LoRAs + grade LUT | StyleTransferAgent, ColoristAgent | Consistent "warm memory" look |
| 旁白 voice clone | VoiceCloneAgent | Recognizable narrator across series |
| Prompt + seed registry | PromptEngineerAgent | Fast, reproducible re-renders |
| Recurring motifs (cat, paper map) | ContinuityAgent | Audience recognition / brand |

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

| Technique | Applied To | Mechanism (cited) | Owning Agent | Metric |
|---|---|---|---|---|
| **Mandatory visual anchoring** | Every character shot | Generate a locked keyframe first; never pure T2V — visual priors are essential or consistency collapses ([arXiv 2512.16954](https://arxiv.org/html/2512.16954)) | PromptEngineerAgent (#46) | ID score does not collapse vs anchor |
| **Per-character LoRA (per age)** | A,B,C,E,F,J × young/adult | Composable adapters on a frozen backbone, prompt-aware ([CharCom](https://arxiv.org/html/2510.10135v1)) | StyleTransferAgent (#61) | Face similarity ≥0.85 (ArcFace) |
| **RL identity reinforcement** | Multi-person shots (Scene 10 dinner) | Identity-GRPO improved multi-human consistency ~18.9% ([arXiv 2510.14256](https://arxiv.org/html/2510.14256v1)) | AIQAConsistencyAgent (#49) | Per-person drift = 0 across frames |
| **Memory-conditioned generation** | Across all 14 cards | Shot-by-shot diffusion conditioned on prior-shot memory ([StoryMem](https://arxiv.org/html/2512.19539)) | MemoryAgent (#58) + PromptEngineerAgent | Cross-scene coherence pass |
| **Training-free fallback** | Shots lacking a clean portrait | Background+character consistency without references ([BachVid](https://arxiv.org/html/2510.21696v1)) | ContinuityAgent (#98) | Consistency ≥ threshold |
| **Fine-grained ID audit** | QC gate | VLM-based identity-preservation eval beyond global embeddings ([arXiv 2511.08087](https://arxiv.org/html/2511.08087v1)) | AIQAConsistencyAgent (#49) | Fine-grained ID delta below τ |

| Dimension (VBench/VMBench) | What It Catches on This Film | Threshold | Judge |
|---|---|---|---|
| Subject (identity) consistency | Face/age drift A→E across scenes | ≥0.90 | AIQAConsistencyAgent (#49) |
| Temporal flicker | Shimmer on shop interior / night bokeh | below τ | AIQAConsistencyAgent |
| Motion smoothness | Hands typing (S3), dolly-in (S10) | ≥ rubric | VMBench check ([arXiv 2503.10076](https://arxiv.org/html/2503.10076)) |
| Imaging quality | Grain/sharpness of close-ups | ≥ rubric | Aesthetics Agent |
| Aesthetic quality | "warm memory" look, composition | ≥85/100 | Aesthetics Agent |
| Spatial r
…



### From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


- `BUILD_PROGRESS.md` — living checklist mirroring §6 milestones and §14 hardening; you tick items as you complete them.
- `DECISIONS.md` — an ADR (Architecture Decision Record) log; every non-obvious choice gets a dated entry.
- `CLAUDE.md` (root + per-package) — your persistent project memory (template in Appendix A).
- `.claude/` — your subagents, slash commands, settings, and hooks (Appendices B–D).

- **Root `CLAUDE.md`** (template in Appendix A): tech stack + pinned versions, monorepo map, the 7 Golden Rules (§0.3), build/test/lint commands, code-style rules, contract location, and "where to find the spec for X."
- **Per-package `CLAUDE.md`**: each `packages/*` and `services/*` gets a short `CLAUDE.md` describing its responsibility, public API, and local test command. Nested files load when you work in that subtree, keeping context tight.
- **Keep it lean.** `CLAUDE.md` competes with task context. Link to specs rather than pasting them. Run `/memory` to review; prune aggressively.
- Bootstrap with `/init`, then hand-edit to match Appendix A.

| Concern | Choice | Rationale (from specs) |
|---------|--------|------------------------|
| Agent orchestration (DAG) | **LangGraph** | DAG + conditional edges + first-class HiTL gates + checkpointing. |
| Durable workflow engine | **Temporal (Python SDK)** | Productions run minutes→hours; guaranteed delivery, retries, replay. |
| Event bus | **Redis Streams** (dev/MVP) → **NATS JetStream** (scale) | Pub/sub + persistence + replay; topic-per-production. |
| Relational store | **PostgreSQL 16** + **SQLModel/SQLAlchemy 2 + Alembic** | Production metadata, gate state, critiques, configs, audit log. (Spec mentions Drizzle; we standardize on Python ORM since the gateway is FastAPI. TS types are generated from Pydantic — see §5.6. ADR-001.) |
| Object storage | **S3 / Cloudflare R2** (via `boto3`/S3 API) | Video/audio/image artifacts; content-addressed keys. |
| Vector DB | **Chroma** (dev) → **Pinecone/Weaviate** (prod) | MemoryAgent + Agentic RAG retrieval. |
| Graph/Hybrid RAG | **LightRAG over OpenSearch** | Per [`agentic_rag_functional_specification.md`](./agentic_rag_functional_specification.md). |
| Cache / sessions / rate-limit | **Redis** | Hot data, locks, token buckets. |
| API gateway | **FastAPI** + **uvicorn/gunicorn** | REST + WebSocket gateway. |
| LLM access | **litellm** unified client | One interface for Grok-4.x, Gemini 2.5 Pro, GPT-4o, Claude 4, OSS. |
| Observability | **LangSmith** (agent traces) + **OpenTelemetry → Grafana/Tempo/Loki** | Traces, metrics, logs, replay. |
| Provenance | **C2PA** (`c2pa-python`) | Sign every artifact; verify chain downstream. |
| Containerization | **Docker** + **docker-compose** (dev) → **Kubernetes + Helm** (prod) | GPU node pool for gen tasks; CPU pool for LLM-only. |
| Secrets | **Doppler/Vault** (prod), `.env` + `direnv` (dev, gitignored) | Never in repo. |

```text
va-agent-swarm/                      # repo root (build target; specs live in study/)
├── CLAUDE.md                        # root project memory (Appendix A)
├── BUILD_PROGRESS.md                # living milestone + hardening checklist (you maintain)
├── DECISIONS.md                     # ADR log
├── Makefile                         # the single command surface: make verify|test|dev|...
├── .claude/                         # Claude Code config
│   ├── settings.json                # permissions + hooks (Appendix D)
│   ├── agents/                      # subagents (Appendix B)
│   └── commands/                    # slash commands (Appendix C)
├── .mcp.json                        # project-scoped MCP servers
├── docker-compose.yml               # postgres, redis, temporal, opensearch, chroma, minio
├── pyproject.toml                   # uv workspace root
├── uv.lock
├── pnpm-workspace.yaml
├── turbo.json
├── infra/                           # IaC: helm charts, k8s manifests, terraform
│
├── packages/                        # SHARED, REUSABLE (build these FIRST)
│   ├── contracts/                   # ⭐ FROZEN shared Pydantic models + generated TS types (§5)
│   ├── agent-core/                  # BaseAgent, lifecycle, Self-Refine/Reflexion loop (§5.3)
│   ├── agent-factory/               # AgentConfig → runnable agent (§8)
│   ├── llm-gateway/                 # litellm wrapper, metering, routing hooks (M3)
│   ├── providers/                   # MediaGen/Voice/LipSync/Music/Eval provider impls + mocks
│   ├── rag/                         # Agentic RAG client + indexers (M1)
│   ├── qc/                          # L1/L2/L3 judges + Q1–Q6 delivery mesh (§5.5)
│   ├── eventbus/                    # Redis Streams/NATS pub-sub + typed topics
│   ├── memory/                      # MemoryAgent store (episodic + vector)
│   ├── provenance/                  # C2PA signing/verification
│   └── observability/              # OTel + LangSmith wiring, structured logging
│
├── services/                        # DEPLOYABLE PROCESSES
│   ├── orchestrator/                # LangGraph graphs + Temporal workflows/activities (M2)
│   ├── agent-runtime/               # worker pool that executes agent nodes (M2/M6)
│   ├── api-gateway/                 # FastAPI REST + WebSocket gateway (M10)
│   └── scheduler/                   # cron/triggers for optimization + retraining loops
│
├── apps/
│   └── web/                         # Next.js 15 console (M10)
│
├── agents/                          # ⭐ 114 agent definitions (config + rubric + prompts)
│   ├── _registry.yaml               # the canonical agent registry (id→config path)
│   ├── production/                  # 1–52 craft agents
│   ├── meta/                        # 53–80 orchestration/creative/research/optimization
│   ├── support/                     # 81–114 workflow-support agents
│   └── crosscutting/               # GCA, Research, Optimization, DIA, Aesthetics, RAG, etc.
│
├── workflows/                       # the 10 archetype DAGs (A–J) as LangGraph graph defs
│
├── eval/                            # golden sets, rubrics, benchmark runners, sim personas
│   ├── golden/                      # frozen input→expected fixtures
│   ├── rubrics/                     # per-role L2 constitutions (JSON/YAML)
│   └── harness/                     # VBench/EvalCrafter/CLIP-T/FVD runners (wrap providers)
│
└── tests/                           # cross-package integration + E2E + contract tests
```

**Acceptance rules (implement in `agent-core`, test exhaustively):**
- `blocker` → halts the DAG node until resolved (Temporal signal / LangGraph interrupt).
- `major` → triggers Self-Refine/Reflexion loop on the receiver, **max 3 iterations**, then escalate to JudgeAgent.
- `minor`/`nit` → logged to MemoryAgent; aggregated as RLAIF reward signal for the next training cycle.
- Two-agent disputes → routed to JudgeAgent (multi-agent debate). ComplianceAgent critiques are always `blocker` (BLOCK gate).

The base class wires in: LLM gateway (metered), RAG client, MemoryAgent, event-bus emit, provenance signing, OTel span. **No agent subclass reimplements these.** Specializations differ only by `AgentConfig`.

Topics (from `ui/architecture_communication.md`): `production.{id}.agent_events`, `.critiques`, `.gates`, `.artifacts`, plus `system.alerts`. Every event is one of the typed WebSocket event models (`agent_state_change`, `artifact_created`, `critique_message`, `gate_ready`, `gate_resolved`, `budget_update`, `metric_update`, `memory_entry`, `tool_call`, `production_phase_change`, `error`). These live in `packages/contracts/events.py` and are the *only* shapes allowed on the bus.

**Build:**
- `packages/eventbus`: typed Redis Streams pub/sub; topic contract (§5.7); replayable; at-least-once + idempotency keys.
- `packages/observability`: OTel tracing + structured logs + LangSmith hookup; every node run is a span.
- `services/orchestrator`:
  - **LangGraph graph runtime**: nodes = agent tasks; conditional edges; **HiTL interrupt** points (gates); checkpointer backed by Postgres.
  - **Temporal workflows/activities**: each agent task is a Temporal activity (retry/backoff/timeout); the production is a Temporal workflow (resumable across restarts).
  - **OrchestratorAgent / PlannerAgent / RouterAgent / JudgeAgent / GateKeeperAgent / MemoryAgent** skeletons (agents #53–58) — these are *platform* agents, built here, refined in M8.
  - DAG primitives: fan-out/fan-in, dependency-triggered rerender, deadlock detection, SLA timers.
- `packages/memory`: episodic + long-term project memory (Reflexion/MemGPT pattern) over the vector DB; `MemoryAgent` retrieval API.
- Asset/Data backbone: immutable `artifact_id`, copy-on-write versions, dependency edges, searchable metadata (Postgres + S3/MinIO), C2PA signing via `packages/provenance`.
- State store: production state machine; gate state; durable, auditable, resumable.

**Build:**
- **Orchestration (53–58):** harden Orchestrator/Planner/Router/Judge/GateKeeper/Memory with full dispute-resolution (multi-agent debate), stage-gate sign-off, and escaped-defect=0 discipline.
- **Creative (59–65):** Ideation, NarrativeArc, StyleTransfer, MoodBoard, Novelty/Anti-Cliché, EmotionalArc, WorldBuilding — many delegate to GCA/Aesthetics (no duplication).
- **Research (66–72):** Web/Archive/Trend/Competitor/Citation/InterviewSynthesis/Benchmark — built on the M4 Research Agent core.
- **Optimization (73–80):** Prompt/Cost/Latency/Retention/ROAS/Accessibility optimizers + EvaluationHarness + SafetyRedTeam.
- **Full QC mesh**: complete L3 (AudienceSim ≥200 personas + HiTL sampling) and Q1–Q6 delivery validators; `GateKeeperAgent` enforces "zero leaked defects."

**Build:**
- `services/api-gateway` (FastAPI): REST endpoints + WebSocket gateway exactly per the API contract tables in [`architecture_communication.md`](./ui/architecture_communication.md) (`POST /api/productions`, gate decisions, critiques, retry/skip, router-config, artifacts, delivery). Auth/RBAC, rate-limit, validation, C2PA signing on gate approval. Subscribes to the Event Bus, filters by `production_id`, fans out over WebSocket.
- `apps/web` (Next.js 15 + React 19): Brief Studio, DAG Canvas (live node states), Artifact Gallery, Critique Feed, Gate Approval Dialog, Budget Tracker, Quality Dashboard, Agent Inspector, Memory Panel, Delivery Hub. State via Zustand + React Query; WebSocket via socket.io-client (auto-reconnect, room-per-production). Types imported from generated `packages/contracts/ts` (§5.6).
- Project-creation flow + production-scale discovery (S0–S? scale profiles) + video-remake/enhancement flow.

### Theme 1 — Contracts & Schema Integrity (1–10)
1. Every inter-agent message is a typed `packages/contracts` model; zero ad-hoc dicts on the bus.
2. Handoff `Artifact` populated at every phase boundary (no empty required fields).
3. Contract snapshot tests guard all models; removal/rename requires version bump + ADR.
4. Generated TS types are in sync with Pydantic (CI diff check green).
5. `parent_assets` always form an acyclic provenance DAG.
6. CritiqueMessage severity semantics enforced (blocker halts, major→3-iter refine, minor/nit→memory).
7. Event-bus payloads validate against `events.py`; invalid events are rejected, not silently dropped.
8. Versioning is copy-on-write; no in-place artifact mutation anywhere.
9. `qc_status` and `provenance_manifest` are never null on a releasable artifact.
10. No package redefines a shared contract locally (grep proves single source).

### Theme 3 — Agent Correctness (21–30)
21. All 114 agents instantiated via the factory (no bespoke loops).
22. Each agent passes L1 schema conformance on its golden inputs.
23. Each agent scores ≥85 on its L2 rubric (frozen judge).
24. Critique edges match the §4 matrix exactly (no missing/extra edges).
25. Tool allowlist enforced; an agent calling a disallowed tool fails closed.
26. Self-Refine caps at `max_refine_iters`; runaway loops impossible.
27. Reflexion memory writes/reads verified; lessons persist across retries.
28. No a
…



### From `corpus/root/agent_loop_creator_v1.md` Copy: `sources/excerpts/agent_loop_creator_v1.md`.


**Rethink Summary (100x Internal Iteration):**  
- **Core Insight from Research**: ~42% of MAS failures are **specification & design issues** (MASFT); verification/termination another ~21%. Adding agents without strong Phase 0 spec validation, structured observations, explicit `Done` + multi-level critics, and progress tracking often yields diminishing/negative returns. Hierarchical + TEA-style versioning/self-evolution delivers outsized gains on long-horizon tasks (AgentOrchestra 89%+ GAIA).  
- **xAI Alignment**: Use `grok-4.20-multi-agent` (4/16 agents, leader synthesis, server-side ReAct with hidden sub-states) for research sub-tasks; emulate Grok Build patterns (explicit plan generation first, parallel isolated sub-agents, todo-style state) in client loop. Hybrid maximizes power + control + cost efficiency.  
- **Architectural Tradeoffs Resolved**: Custom Python core (Pydantic schemas, strict JSON mode, full tracer) over pure LangGraph for transparency, auditability, and education value (user's harness style). Hybrid memory (structured `todo.md` + vector long-term + aggressive summarization) per TEA/MemGPT. Bounded self-evolution (TextGrad-inspired + validation on held-out traces) to prevent drift. Minimal deps first; optional adapters later. Local-first, observable, sandboxed, production-hardened (circuit breakers, retries, budgets). Dogfood: This harness should help build/improve itself.  
- **Failure Mode Coverage**: Every MASFT mode explicitly mapped to mitigations in specific phases/components (see Section 3).  
- **Phased Build**: MVP (reliable flat ReAct) → Hierarchical delegation + consolidation → TEA versioning/evolution → xAI hybrid + examples. Each phase has clear deliverables, code skeletons, and verification gates (critic checkpoints).  
- **Target Outcomes**: >85% success on complex research/coding benchmarks via evolution; <5% residual MASFT failure modes in controlled tests; full replay/debug from traces; seamless integration with user's Python/Node/xAI/DeepSeek/Cursor/Kiro/OpenWebUI stack.

### Constraints & Non-Goals
- **Language/Stack**: Python 3.11+ primary (Pydantic v2, asyncio, httpx, dataclasses). Optional: chromadb/FAISS for vector memory, fastapi/uvicorn for server, langgraph for adapter only. No heavy framework lock-in for core loop.
- **Minimalism First**: Core loop + state + reliability + basic hierarchical in <2k LOC initially. Add evolution/xAI hybrid in later phases.
- **No Uncontrolled Loops**: Hard `max_steps`, cycle detection (state hash), progress-based exit, circuit breakers. All LLM calls use strict output_schema (Pydantic/JSON mode or constrained decoding).
- **Security**: Sandbox code execution tools; never trust LLM-generated tool args blindly (validate + least-privilege); monitor for anomalous patterns (e.g., rapid repetition).
- **Cost Control**: Token budgets, parallel only for independent branches, summarization on context pressure, early termination when criteria met.
- **Non-Goals (Phase 1-2)**: Full distributed execution (Ray/Celery later), GUI dashboard (CLI + JSON export first), multimodal native (text+code focus; vision via xAI or sub-agent), production multi-tenancy.

### 2.4 Final Architectural Decisions (Post-100x Rethink)
- **Loop Style**: Controlled custom ReAct (dataclass/Pydantic State + hash cycle detect + circuit breakers) as foundation. Hierarchical on top (Orchestrator decides delegate vs tool vs synthesize vs finish). Not flat multi-agent (central control beats coordination chaos per research).
- **State**: `AgentState` (task_spec: TaskSpec, history: List[TraceEvent], todo: List[TodoItem] or todo_md_content, plan: Optional[Plan], memory_short: Summary + recent, memory_long: VectorStore + key_facts, versions: VersionRegistry, tracer: Tracer, budgets: Token/StepBudget, seen_hashes: set for cycles).
- **Memory Strategy**: Structured `todo.md` / key_facts (primary, low token) + aggressive summarization (on context pressure or milestone) + optional vector (Chroma/FAISS) for semantic retrieval of past traces/versions/knowledge. Sub-agents get **sliced context + provenance only**.
- **LLM Calling**: Unified client (support xAI direct, DeepSeek, OpenAI compat via LiteLLM or custom). All calls: system + few-shot (dense for research, sparse for embodied) + strict `output_schema` (Pydantic model_dump_json or JSON mode). Enforce parseability.
- **Tools**: Registry with validation. Safe execute wrapper (circuit + retry + structured error obs). Sandbox for code_execution (restricted globals or firejail/subprocess).
- **xAI Hybrid Specific**: `XAIClient` wrapper for `grok-4.20-multi-agent` calls. Payload: narrow sub_objective + success_criteria + enabled_tools list + context_slice. Parse leader final answer + optional reasoning. Log as special Observation with `source: "xai_multi_agent"`, `agent_count`, `synthesis_confidence`.
- **Self-Evolution Scope (Phased)**: Phase 2+: Prompts & verifier prompts. Phase 3+: Tool code (dynamic generation + validate). Phase 4: Agent configs/roles, even sub-spec generation heuristics.
- **Testing Dogfood**: Build failure simulator that replays MASFT examples; assert mitigations. Use the harness to improve its own prompts/verifier on held-out traces during development.
- **Extensibility**: Pluggable LLM backend, Tool types, SubAgent roles (registry + factory), Memory backends, Evolution strategies. CLI for single runs; server mode (FastAPI) for multi-session / integration with OpenWebUI-style frontends.

### 3.1 High-Level Flow (Phases from agent_loop.md, Hardened)
1. **Phase 0: Initialization**
   - Parse instruction → generate/validate `TaskSpec` (Pydantic: objective, success_criteria: List[str], constraints: Dict, output_format, max_steps=50, token_budget=200k, quality_gates, initial_plan?).
   - Spec Validator + Critic (LLM): Check completeness, ambiguity, role clarity, termination conditions. Reject/revise if FM-1.x risks high.
   - Create `AgentState`: task_spec, todo (from plan or empty), memory, tracer, version_registry, budgets, seen_hashes=set().
   - Optional: Planner LLM generates high-level plan (numbered steps + deps) + todo.md content. Validate plan vs spec.
   - Decide architecture: flat | hierarchical | hybrid_xai.

2. **Phase 1: Core Controlled ReAct Loop**
   - While not terminate:
     - Build context (summarize history if long + key_facts + todo + task_spec + latest obs).
     - LLM Decision (strict schema): `thought` (analyze progress vs criteria, gaps, risks, strategy; re-ground vs objective), `action_type` ("tool" | "delegate" | "synthesize" | "finish" | "reflect"), `payload` (args or sub_spec).
     - Cycle check: hash recent (action+obs) ; if seen → force replan or terminate.
     - Execute: safe_tool (circuit + retry + sandbox) or safe_delegate (sub loop or xAI call) or internal.
     - Structured Observation: `{status, data, summary, confidence, issues, next_suggestions, provenance, trace_id, versions_used}`.
     - Append TraceEvent to history + update todo/progress + memory.
     - Light reflection (every N or on error): Quick self-critique alignment.
   - CircuitBreaker per tool_name/role (CLOSED/OPEN/HALF_OPEN logic as in attached code; track metrics).
   - Termination signals: success_criteria met + verifier pass, max_steps/budget, explicit verified Finish, irrecoverable (escalate), early exit on intermediate criteria met.

class AgentState(BaseModel):
    task_spec: TaskSpec
    history: List[TraceEvent] = Field(default_factory=list)
    todo: List[str] = Field(default_factory=list)  # or todo_md: str
    plan: Optional[Dict[str, Any]] = None
    memory_short: Dict[str, Any] = Field(default_factory=dict)
    memory_long_ref: Optional[str] = None  # vector ids or summary
    seen_hashes: set = Field(default_factory=set)  # for cycle detection
    budgets: Dict[str, Any] = Field(default_factory=dict)
    versions: Dict[str, str] = Field(default_factory=dict)  # current active
    tracer: List[TraceEvent] = Field(default_factory=list)  # or separate Tracer class
```

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

- **Reliability**: Circuit breakers + retries + backoff (per attached safe_* wrappers). Structured error obs always. Budget enforcement + graceful degradation. Progress-based early exit.
- **Security**: Tool sandbox (restricted Python exec or isolated subprocess/Docker for code_execution; browser tools via controlled libs). Validate/sanitize all LLM-generated args before execution. Least-privilege tool access. Anomaly detection on loop patterns (e.g., rapid same-action repetition → circuit open + alert).
- **Observability**: Tracer is first-class. Every event: full context snapshot option (configurable), versions, token counts, timings, sub-calls. Export JSONL / Parquet. Replay function: `replay_trace(trace_id, from_step=5)`. Optional OpenTelemetry export or integration with user's Jenkins/OpenWebUI logging.
- **Cost/Scalability**: Per-phase budgets. Parallel only independent branches (asyncio). Summarization signals (context length + semantic importance). Session isolation for concurrency.
- **Extensibility**: 
  - LLM backends via abstract client or LiteLLM.
  - Tools: Simple registry + Pydantic schema validation.
  - Sub-agents: Factory + role prompts in registry.
  - Memory: Pluggable (in-memory dict, vector store, persistent DB).
  - Evolution strategies: Swap TextGrad for other (e.g., Reflexion-only).
  - Adapters: LangGraph state machine wrapper; export to Grok Build ACP/MCP skills; FastAPI endpoints for remote orchestration.
- **Deployment**: `pyproject.toml` with optional deps. Docker minimal (Python + venv). Local-first by default. Server mode for multi-user/integration if needed (Keycloak OIDC ready pattern from user's stack).



### From `corpus/root/agent_loop_creator_v2.md` Copy: `sources/excerpts/agent_loop_creator_v2.md`.


**Rethink Summary (100x Internal Iteration + Cognitive Layer):**  
- **Core Insight from Research**: ~42% of MAS failures are **specification & design issues** (MASFT); verification/termination another ~21%. Adding agents without strong Phase 0 spec validation, structured observations, explicit `Done` + multi-level critics, and progress tracking often yields diminishing/negative returns. Hierarchical + TEA-style versioning/self-evolution delivers outsized gains on long-horizon tasks (AgentOrchestra 89%+ GAIA). **v2 addition**: Human cognitive frameworks (top-ranked in thinking_model.md) provide the highest-leverage missing layer for adaptive intelligence, proactive risk handling, fast/slow deliberation, and multi-level learning — directly mapped in agent_loop_v3.md Section 1.4.  
- **xAI Alignment**: Use `grok-4.20-multi-agent` (4/16 agents, leader synthesis, server-side ReAct with hidden sub-states) for research sub-tasks; emulate Grok Build patterns (explicit plan generation first, parallel isolated sub-agents, todo-style state) in client loop. Hybrid maximizes power + control + cost efficiency. Cognitive routing (Cynefin) helps decide when to delegate vs local fast path.  
- **Architectural Tradeoffs Resolved**: Custom Python core (Pydantic schemas, strict JSON mode, full tracer) over pure LangGraph for transparency, auditability, and education value (user's harness style). Hybrid memory (structured `todo.md` + vector long-term + aggressive summarization + **Pattern Store for RPD**) per TEA/MemGPT. Bounded self-evolution (TextGrad-inspired + validation on held-out traces + **AAR/Double-Loop structure**) to prevent drift. **Cognitive config** (enable_fast_path, reflection_style, critic_modes) per TaskSpec for adaptability without complexity explosion on simple tasks. Minimal deps first; optional adapters later. Local-first, observable, sandboxed, production-hardened (circuit breakers, retries, budgets). Dogfood: This harness should help build/improve itself (including its own cognitive components).  
- **Failure Mode Coverage**: Every MASFT mode explicitly mapped to mitigations in specific phases/components (see Section 3) **+ cognitive mitigations** (e.g., Premortem for spec/design risks, Metacognition + cycle detection for repetition, AAR/Double-Loop for verification/termination gaps, RPD for context/history issues via pattern matching).  
- **Phased Build**: MVP (reliable flat ReAct) → Controlled core with cognitive mode selection (Fast Recognition Path) → Hierarchical delegation + consolidation → TEA versioning/evolution + full AAR/Double-Loop/5Whys critics → xAI hybrid + examples. Each phase has clear deliverables, code skeletons, and verification gates (critic checkpoints).  
- **Target Outcomes**: >85% success on complex research/coding benchmarks via evolution; <5% residual MASFT failure modes in controlled tests; **cognitive features validated** (Cynefin classification accuracy, Premortem risk coverage, RPD hit rate on repeated tasks, AAR structure compliance, Double-Loop assumption questioning); full replay/debug from traces; seamless integration with user's Python/Node/xAI/DeepSeek/Cursor/Kiro/OpenWebUI stack.

### Constraints & Non-Goals
- **Language/Stack**: Python 3.11+ primary (Pydantic v2, asyncio, httpx, dataclasses). Optional: chromadb/FAISS for vector memory, fastapi/uvicorn for server, langgraph for adapter only. No heavy framework lock-in for core loop.
- **Minimalism First**: Core loop + state + reliability + basic hierarchical in <2k LOC initially. Add evolution/xAI hybrid in later phases.
- **No Uncontrolled Loops**: Hard `max_steps`, cycle detection (state hash), progress-based exit, circuit breakers. All LLM calls use strict output_schema (Pydantic/JSON mode or constrained decoding).
- **Security**: Sandbox code execution tools; never trust LLM-generated tool args blindly (validate + least-privilege); monitor for anomalous patterns (e.g., rapid repetition).
- **Cost Control**: Token budgets, parallel only for independent branches, summarization on context pressure, early termination when criteria met.
- **Non-Goals (Phase 1-2)**: Full distributed execution (Ray/Celery later), GUI dashboard (CLI + JSON export first), multimodal native (text+code focus; vision via xAI or sub-agent), production multi-tenancy.

### 2.4 Final Architectural Decisions (Post-100x Rethink)
- **Loop Style**: Controlled custom ReAct (dataclass/Pydantic State + hash cycle detect + circuit breakers) as foundation. Hierarchical on top (Orchestrator decides delegate vs tool vs synthesize vs finish). Not flat multi-agent (central control beats coordination chaos per research).
- **State**: `AgentState` (task_spec: TaskSpec, history: List[TraceEvent], todo: List[TodoItem] or todo_md_content, plan: Optional[Plan], memory_short: Summary + recent, memory_long: VectorStore + key_facts, versions: VersionRegistry, tracer: Tracer, budgets: Token/StepBudget, seen_hashes: set for cycles).
- **Memory Strategy**: Structured `todo.md` / key_facts (primary, low token) + aggressive summarization (on context pressure or milestone) + optional vector (Chroma/FAISS) for semantic retrieval of past traces/versions/knowledge. Sub-agents get **sliced context + provenance only**.
- **LLM Calling**: Unified client (support xAI direct, DeepSeek, OpenAI compat via LiteLLM or custom). All calls: system + few-shot (dense for research, sparse for embodied) + strict `output_schema` (Pydantic model_dump_json or JSON mode). Enforce parseability.
- **Tools**: Registry with validation. Safe execute wrapper (circuit + retry + structured error obs). Sandbox for code_execution (restricted globals or firejail/subprocess).
- **xAI Hybrid Specific**: `XAIClient` wrapper for `grok-4.20-multi-agent` calls. Payload: narrow sub_objective + success_criteria + enabled_tools list + context_slice. Parse leader final answer + optional reasoning. Log as special Observation with `source: "xai_multi_agent"`, `agent_count`, `synthesis_confidence`.
- **Self-Evolution Scope (Phased)**: Phase 2+: Prompts & verifier prompts. Phase 3+: Tool code (dynamic generation + validate). Phase 4: Agent configs/roles, even sub-spec generation heuristics.
- **Testing Dogfood**: Build failure simulator that replays MASFT examples; assert mitigations. Use the harness to improve its own prompts/verifier on held-out traces during development.
- **Extensibility**: Pluggable LLM backend, Tool types, SubAgent roles (registry + factory), Memory backends, Evolution strategies. CLI for single runs; server mode (FastAPI) for multi-session / integration with OpenWebUI-style frontends.

### 3.1 High-Level Flow (Phases from agent_loop_v3.md, Hardened with Cognitive Layer)
1. **Phase 0: Initialization (Spec-Driven + Cognitive Setup)**
   - Parse instruction → generate/validate `TaskSpec` (Pydantic: objective, success_criteria: List[str], constraints: Dict, output_format, max_steps=50, token_budget=200k, quality_gates, initial_plan?, **cognitive_profile: Dict** e.g. {"enable_fast_path": true, "reflection_style": "aar_double_loop_5whys", "critic_modes": ["red_team", "paul_elder"], "cynefin_classification": "auto"}).
   - Spec Validator + Critic (LLM): Check completeness, ambiguity, role clarity, termination conditions. Reject/revise if FM-1.x risks high. **Run Premortem Analysis**: "Assume this spec/plan fails spectacularly — identify top causes and mitigations; merge into living spec, success_criteria, todo, and quality_gates."
   - **Cynefin Classification** (context-aware routing): Tag task context (Simple/Complicated/Complex/Chaotic) based on cause-effect clarity, expertise needed, emergence, or crisis. Store in task_spec and use to auto-configure loop params (Fast path preference for Simple/Complicated; Full + heavy reflection for Complex/Chaotic).
   - Create `AgentState`: task_spec (with cognitive_profile + cynefin_tag), todo (from plan or empty), memory (incl. Pattern Store for RPD), tracer, version_registry, budgets, seen_hashes=set(), **current_mode: "fast" | "full"**.
   - Optional: Planner LLM generates high-level plan (numbered steps + deps) + todo.md content. Validate plan vs spec **+ Premortem risks**.
   - Decide architecture: flat | hierarchical | hybrid_xai. Set initial mode from Cynefin + config.

2. **Phase 1: Core Controlled ReAct Loop (with Cognitive Mode Selection)**
   - While not terminate:
     - **v2 Mode Selection (Cynefin + RPD + Dual Process + Metacognition)**: At start of iteration or after major obs, determine operating mode:
       - If Cynefin allows (Simple/Complicated) **and** high-similarity match in Pattern Store (RPD) **and** metacognition confidence high → **Fast Recognition Path**: lightweight Thought (mental simulation referencing matched trace), minimal tokens, proceed to action. Log mode for AAR review.
       - Else → **Full Deliberative Mode** (detailed ReAct Thought with re-grounding + full gates). Run lightweight parallel **Metacognition Monitor** (bias scan, progress vs criteria, context drift, confidence pulse) that can force mode switch or early replan.
     - Build context (summarize history if long + key_facts + todo + task_spec + latest obs + relevant Pattern Store entries for RPD).
     - LLM Decision (strict schema): `thought` (**Metacognitive overlay** first: "Right mode? Biases per Paul-Elder? Progress vs criteria?"), `action_type` ("tool" | "delegate" | "synthesize" | "finish" | "reflect"), `payload` (args or sub_spec). In Fast mode: keep concise.
     - Cycle check: hash recent (action+obs) ; if seen → force replan or terminate.
     - Execute: safe_tool (circuit + retry + sandbox) or safe_delegate (sub loop or xAI call) or internal.
     - Structured Observation: `{status, data, summary, confidence, issues, next_suggestions, provenance, trace_id, versions_used, mode_used}`.
     - Append TraceEvent to history + update todo/progress + memory (update Pattern Store on high-quality outcomes).
     - Light reflection (every N or on error): Quick self-critique alignment **+ mode effectiveness note**.
   - CircuitBreaker per tool_name/role (CLOSED/OPEN/HALF_OPEN logic as in attached code; track metrics; integrate with mode for cost-aware decisions).
   - Termination signals: success_criteria met + verifier pass, max_steps/budget, explicit verified Finish, irrecoverable (escalate), early exit on intermediate criteria met **or strong Fast-path success on sub-criteria**.

5. **Phase 4: Reflection & Self-Evolution (Advanced — AAR + Double-Loop + 5 Whys + Multi-Perspective Critics)**
   - At milestones or end (or on explicit reflect action): Full trace + mode history to SelfEvolver.
   - **Mandatory Structured AAR** (4-question template from After-Action Review):
     1. What was supposed to happen? (vs original TaskSpec + plan + success_criteria)
     2. What actually happened? (from tracer + StructuredObservations, including Fast vs Full mode stats and RPD matches)
     3. Why? (diagnosis — standard attribution + deep pass with **5 Whys** on top issues + **Ishikawa Fishbone** or fault tree categorization: Prompts/Methods, Models/Tools, Data/Obs, Context/Env, State/Memory, Verification, Human Spec)
     4. What next? (actionable lessons → concrete edits)
   - **Double-Loop Learning Layer** (after AAR single-loop diagnosis): Explicitly question governing variables/assumptions (e.g., "Was our definition of quality too loose? Did role boundaries allow drift? Should success_criteria or cognitive_profile defaults evolve?"). Only meta-approved changes proceed to proposal.
   - Diagnose root causes (MASFT-aware + cognitive lens prompt, referencing FM modes and thinking_model mappings).
   - Propose targeted edits (prompts, tool code, role defs, sub-spec heuristics, **even cognitive_profile defaults or new critic modes**). Use Paul-Elder standards or Red Team attack during diagnosis/proposal where configured.
   - Validate improvement on held-out or replay (re-run with new version; check success rate/steps/verifier scor
…



### From `corpus/root/project_starter_0.1.md` Copy: `sources/excerpts/project_starter_0.1.md`.


**Context & Principles**  
- **Spec-Driven Development (SDD)** first: Clear specs drive everything.  
- Prioritize **highest-ranked** items on feature/skill/rule overlap (ECC #1 > Karpathy rules #2 > claude-mem #3 > shanraisshan best-practice #4 > antigravity-awesome-skills #5, etc.).  
- Keep it **portable, minimal-Docker where possible, local-first**, with excellent security, memory, and token efficiency.  
- Output must be **agent-friendly**: clear phases, checklists, acceptance criteria, and hooks for critic/review agents.  
- Support iterative refinement (plan → implement → review → improve loops).  
- Target users: Solo developers, small teams, or power users building custom AI coding workflows (aligns with harness engineering + N1ch01as-style meta-systems).

**Success Criteria**  
- New project folder initializes in < 5 minutes with one main script.  
- ECC fully installed + configured as core harness.  
- Karpathy behavioral rules active by default.  
- Persistent memory (claude-mem or equivalent) enabled.  
- High-value skills from top libraries selectively merged (no duplication).  
- Best-practice configs, hooks, rules, and example workflows included.  
- Security baseline (AgentShield or equivalent) active.  
- Clear docs + task.md for further extension.  
- Works cross-platform (macOS/Linux/Windows where possible) and with multiple agents.  
- Includes quality gates (lint, tests, review prompts).
- **All supported coding agents share the exact same curated skills, rules, and hooks** via automated or documented synchronization from a single source of truth.

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

**Tasks**:
1. [ ] Verify current top repos (use web search or direct GitHub):
   - ECC (affaan-m/ECC) – primary harness (skills, agents, hooks, rules, security, MCP).
   - Karpathy rules (forrestchang/andrej-karpathy-skills or multica-ai mirror) – behavioral CLAUDE.md.
   - claude-mem (thedotmack/claude-mem) – persistent memory.
   - shanraisshan/claude-code-best-practice – workflows & patterns.
   - sickn33/antigravity-awesome-skills – bulk skill library (selective install only high-value bundles).
2. [ ] Identify overlaps and decide:
   - Core harness/rules/hooks/security/MCP → **ECC first** (highest rank + most comprehensive).
   - Behavioral guidelines → **Karpathy rules** (add as base or merge into ECC rules if compatible).
   - Memory → **claude-mem** (or ECC's built-in memory/instincts if sufficient; prefer dedicated if better persistence).
   - Planning / best-practice workflows → Merge from shanraisshan + ECC's planning skills.
   - Bulk skills → Use antigravity-awesome-skills installer but **curate** only top 20–50 most useful (planning, TDD, review, security, frontend, etc.). Avoid installing everything.
3. [ ] Check for official Anthropic skills or new high-rank additions since last check.
4. [ ] Document decisions in `docs/decisions.md` (use ECC's research-first style).

## Phase 3: Memory, Skills & Selective Library Integration (Priority #3 & #5)

**Objective**: Add persistent memory and curated high-impact skills.

**Acceptance Criteria**:
- Memory persists across sessions and improves context for long tasks.
- Curated skill set is lean yet powerful (document which ones were chosen and why).
- Easy way to add/remove skills later.

**Tasks**:
1. [ ] Enable **AgentShield** (or ECC security) + secret detection, vulnerability scanning.
2. [ ] Configure key **hooks** (pre-commit validation, post-completion review, context compaction, cost tracking).
3. [ ] Set up **MCP configs** for common tools (GitHub, file system, etc.) – start minimal and secure.
4. [ ] Apply ECC token optimization settings (MAX_THINKING_TOKENS, compact thresholds, etc.).
5. [ ] Add `.gitignore`, license (MIT), and contributor guidelines.
6. [ ] Create bootstrap script(s) in `scripts/`:
- `bootstrap.sh` or `install.js` that runs ECC install + memory + curated skills + config copy.
- Support flags for different agents (Claude Code, Cursor, etc.).

**Initial Priority Order for Implementation**:
1. ECC foundation (Phase 1)
2. Karpathy + best practices (Phase 2)
3. Memory + curated skills (Phase 3)
4. Security/hooks/MCP (Phase 4)
5. Docs + validation (Phase 5)



### From `corpus/root/project_starter_0.2.md` Copy: `sources/excerpts/project_starter_0.2.md`.


1. Making **ECC the foundation**, but installing curated profiles first instead of blindly copying everything.  
2. Replacing Bash-first sync with a **cross-platform Node.js CLI**.  
3. Defining **one source of truth** and generated adapters with drift checks.  
4. Treating “same skills/rules everywhere” as **semantic parity**, not identical file format parity.  
5. Adding license, source, checksum, and version manifests.  
6. Separating **instructions**, **skills**, **memory**, **hooks**, **MCP**, and **generated tool configs**.  
7. Adding an explicit **security threat model**.  
8. Replacing “log all reasoning traces” with **auditable summaries, evidence, decisions, diffs, commands, test results, and review outputs**. Do not request or store hidden chain-of-thought.  
9. Making self-improvement **proposal-only until human approval**.  
10. Adding measurable quality gates, sync tests, and install-time budgets.

1. **ECC** — primary cross-agent harness foundation.  
2. **Karpathy-style behavioral rules** — concise behavioral layer.  
3. **claude-mem or equivalent** — persistent memory if compatible and safe.  
4. **Claude Code best-practice repositories** — selected planning/workflow patterns.  
5. **Curated skill libraries** — selective import only; no bulk install by default.  
6. **Official agent docs** — Claude Code, Cursor, Codex, OpenCode, Gemini CLI, Grok Build, GitHub Copilot.

1. **SDD first:** Specs drive implementation.  
2. **ECC-first on overlap:** Prefer ECC components, naming, conventions, security, and cross-harness architecture unless a source audit proves a better fit.  
3. **Karpathy behavior layer:** Think before coding, simplicity first, surgical changes, goal-driven execution.  
4. **Single source of truth:** Central `skills/`, `rules/`, `hooks/`, `mcp-configs/`, and manifests are authoritative.  
5. **Generated adapters:** `.claude/`, `.cursor/`, `.gemini/`, `.codex/`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, etc. are generated or documented from the source of truth.  
6. **Safe by default:** No destructive automation, remote MCP, or skill mutation without explicit human approval.  
7. **Local-first:** Prefer local scripts, local memory, local audit logs, and optional external services.  
8. **Minimal core, optional bundles:** Starter must be lean; large skill libraries are curated, not fully installed.  
9. **Cross-platform:** macOS, Linux, Windows/PowerShell/WSL where possible.  
10. **Auditable, not opaque:** Store concise rationales, evidence, decisions, diffs, commands run, test results, and review summaries. Do **not** require hidden chain-of-thought.

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

- [ ] Verify latest ECC release, installer commands, profiles, and license.  
- [ ] Verify Karpathy-style rules source and Cursor rule variant.  
- [ ] Verify `claude-mem` or equivalent persistent-memory candidate.  
- [ ] Verify best-practice workflow repositories and select only non-duplicative patterns.  
- [ ] Verify curated skill libraries and choose only high-value bundles.  
- [ ] Verify official docs for Claude Code, Cursor, Codex, OpenCode, Gemini CLI, Grok Build, and GitHub Copilot.  
- [ ] Create `docs/source-audit.md` with:  
  - source name  
  - URL  
  - version/commit/tag  
  - license  
  - install command  
  - selected components  
  - rejected components  
  - rationale  
- [ ] Create `docs/decisions.md` with ADR-style decisions.  
- [ ] Define starter profiles:  
  - **Core profile:** minimal, safe, under 5-minute init.  
  - **Power profile:** ECC broader install + memory + curated skills.  
  - **Experimental profile:** Grok Build, extra MCP, multi-agent demos.

- [ ] No source is used without license and version/commit recorded.  
- [ ] No conflicting duplicate skills/rules are accepted.  
- [ ] Clear priority order exists: ECC > Karpathy > memory > best-practice > curated libraries.  
- [ ] Install commands are verified before scripting.

- [ ] Add `scripts/adapters/ecc.mjs` or installer wrapper.  
- [ ] Support profiles:  
  - `--profile core`  
  - `--profile minimal`  
  - `--profile power`  
  - `--profile experimental`  
- [ ] Install/select ECC components:  
  - core rules  
  - planning/review/security skills  
  - AgentShield/security scan  
  - token/context optimization  
  - memory/instinct learning where safe  
  - dmux or parallel orchestration patterns  
  - MCP conventions  
- [ ] Avoid blind full copy by default.  
- [ ] Record ECC source version in `docs/source-audit.md`.  
- [ ] Add attribution to imported/derived files.  
- [ ] Run AgentShield/security scan after ECC setup.

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

**Goal:** Provide persistent, privacy-aware memory without context bloat.

- [ ] `status.md`: current progress.  
- [ ] `task.md`: living spec.  
- [ ] `memory/project.md`: stable project context.  
- [ ] `memory/handoff.md`: compact continuation summary.  
- [ ] `memory/reflections/`: review lessons and repeated patterns.  
- [ ] Optional `claude-mem` or ECC memory/instinct layer.

- [ ] Never store secrets.  
- [ ] Redact credentials and personal data.  
- [ ] Summarize instead of dumping logs.  
- [ ] Load only relevant memory.  
- [ ] Prefer handoff files for session continuation.  
- [ ] Keep auto-injected context small.

- [ ] A new session can resume from `task.md`, `status.md`, and `memory/handoff.md`.  
- [ ] Self-review outputs can generate reflection entries.  
- [ ] Memory can be disabled.

- [ ] Agent can critique its own work.  
- [ ] Critique includes actionable fixes.  
- [ ] Review can block completion if serious issues exist.  
- [ ] Review output feeds memory/reflection safely.

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
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Claude Code repository for docs, issues, release notes, and compatibility references."
    },
    {
      "id": "anthropic-claude-code-action",
      "name": "Anthropic Claude Code Action",
      "url": "https://github.com/anthropics/claude-code-action.git",
      "target": "external/sources/anthropic-claude-code-action",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official GitHub Action patterns for Claude Code automation, PR review, issue workflows, and CI integration."
    },
    {
      "id": "anthropic-skills",
      "name": "Anthropic Agent Skills",
      "url": "https://github.com/anthropics/skills.git",
      "target": "external/sources/anthropic-skills",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Official Agent Skills examples, specification, templates, and skill packaging patterns."
    },
    {
      "id": "anthropic-claude-plugins-official",
      "name": "Anthropic Claude Plugins Official",
      "url": "https://github.com/anthropics/claude-plugins-official.git",
      "target": "external/sources/anthropic-claude-plugins-official",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Claude Code plugin marketplace structure and plugin manifest examples."
    },
    {
      "id": "openai-codex",
      "name": "OpenAI Codex CLI",
      "url": "https://github.com/openai/codex.git",
      "target": "external/sources/openai-codex",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Codex CLI source and AGENTS.md behavior reference."
    },
    {
      "id": "google-gemini-cli",
      "name": "Google Gemini CLI",
      "url": "https://github.com/google-gemini/gemini-cli.git",
      "target": "external/sources/google-gemini-cli",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Gemini CLI source for GEMINI.md, MCP, settings, and command compatibility."
    },
    {
      "id": "opencode",
      "name": "OpenCode",
      "url": "https://github.com/anomalyco/opencode.git",
      "target": "external/sources/opencode",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "OpenCode source for AGENTS.md, opencode config, agents, MCP, and plugin compatibility."
    },
    {
      "id": "modelcontextprotocol-servers",
      "name": "Model Context Protocol Servers",
      "url": "https://github.com/modelcontextprotocol/servers.git",
      "target": "external/sources/modelcontextprotocol-servers",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Current MCP server examples and server discovery references."
    },
    {
      "id": "modelcontextprotocol-registry",
      "name": "Model Context Protocol Registry",
      "url": "https://github.com/modelcontextprotocol/registry.git",
      "target": "external/sources/modelcontextprotocol-registry",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "MCP registry references for discovering MCP servers safely."
    },
    {
      "id": "github-mcp-server",
      "name": "GitHub MCP Server",
      "url": "https://github.com/github/github-mcp-server.git",
      "target": "external/sources/github-mcp-server",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official GitHub MCP server for GitHub issue, PR, repo, workflow, and code search integration."
    },
    {
      "id": "agents-md",
      "name": "AGENTS.md Specification",
      "url": "https://github.com/openai/agents.md.git",
      "target": "external/sources/agents-md",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "standard",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "AGENTS.md standard/reference for cross-agent repository instructions."
    },
    {
      "id": "andrej-karpathy-skills",
      "name": "Andrej Karpathy Skills",
      "url": "https://github.com/forrestchang/andrej-karpathy-skills.git",
      "target": "external/sources/andrej-karpathy-skills",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "behavior-rules",
      "quarantine": false,
      "import_policy": "curated-only",
      "purpose": "Karpathy-style behavioral rules: think before coding, simplicity, surgical changes, goal-driven execution."
    },
    {
      "id": "andrej-karpathy-skills-cursor-vscode",
      "name": "Andrej Karpathy Skills for Cursor and VS Code",
      "url": "https://github.com/mbeijen/andrej-karpathy-skills-cursor-vscode.git",
      "target": "external/sources/andrej-karpathy-skills-cursor-vscode",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "behavior-rules",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Cursor/VS Code rule-file adaptation of Karpathy-style behavior rules."
    },
    {
      "id": "claude-mem",
      "name": "Claude Mem",
      "url": "https://github.com/thedotmack/claude-mem.git",
      "target": "external/sources/claude-mem",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "memory",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Persistent memory architecture reference. Must not install automatically."
    },
    {
      "id": "superpowers",
      "name": "Superpowers",
      "url": "https://github.com/obra/superpowers.git",
      "target": "external/sources/superpowers",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "skills",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Composable software-development skill methodology for multiple coding agents."
    },
    {
      "id": "claude-code-best-practice",
      "name": "Claude Code Best Practice",
      "url": "https://github.com/shanraisshan/claude-code-best-practice.git",
      "target": "external/sources/claude-code-best-practice",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "best-practices",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Community best-practice source for Claude Code agents, commands, skills, hooks, and workflows."
    },
    {
      "id": "awesome-claude-code",
      "name": "Awesome Claude Code",
      "url": "https://github.com/hesreallyhim/awesome-claude-code.git",
      "target": "external/sources/awesome-claude-code",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Curated discovery list for Claude Code skills, hooks, commands, plugins, workflows, and tooling."
    },
    {
      "id": "awesome-agent-skills",
      "name": "Awesome Agent Skills",
      "url": "https://github.com/VoltAgent/awesome-agent-skills.git",
      "target": "external/sources/awesome-agent-skills",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Cross-agent discovery list for Claude Code, Codex, Gemini CLI, Cursor, and related skills."
    },
    {
      "id": "wshobson-agents",
      "name": "Claude Code Subagents by wshobson",
      "url": "https://github.com/wshobson/agents.git",
      "target": "external/sources/wshobson-agents",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "agents",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Community Claude Code subagent definitions for specialist-agent patterns."
    },
    {
      "id": "vercel-agent-skills",
      "name": "Vercel Labs Agent Skills",
      "url": "https://github.com/vercel-labs/agent-skills.git",
      "target": "external/sources/vercel-agent-skills",
      "type": "git",
      "enabled": true,
      "priority": "requir
…



### From `corpus/root/project_starter_0.4.md` Copy: `sources/excerpts/project_starter_0.4.md`.


```text
project_starter/
├── project_starter.md
├── README.md
├── package.json
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── task.md
├── status.md
├── sources/
├── scripts/
├── rules/
├── skills/
├── hooks/
├── mcp-configs/
├── memory/
├── docs/
├── tests/
└── external/
```

```text
abc/
├── project_starter.md
├── README.md
├── package.json
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── task.md
├── status.md
├── sources/
├── scripts/
├── rules/
├── skills/
├── hooks/
├── mcp-configs/
├── memory/
├── docs/
├── tests/
└── external/
```

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

Generated:
- package.json
- scripts/
- sources/
- rules/
- skills/
- hooks/
- mcp-configs/
- memory/
- docs/
- tests/
- agent configs

```text
project_starter.md
README.md
package.json
AGENTS.md
CLAUDE.md
GEMINI.md
task.md
status.md
sources/manifest.json
sources/docs-manifest.json
sources/source-lock.json
scripts/bootstrap.mjs
scripts/doctor.mjs
scripts/create-project.mjs
scripts/download-sources.mjs
scripts/audit-sources.mjs
scripts/security-check.mjs
scripts/sync-agent-configs.mjs
scripts/test.mjs
rules/
skills/
hooks/
mcp-configs/
memory/
docs/
tests/
external/sources/.gitkeep
```

1. Create directories.
2. Create root metadata files.
3. Create manifests.
4. Create rules.
5. Create skills.
6. Create hooks.
7. Create memory files.
8. Create docs.
9. Create package.json.
10. Create utility scripts.
11. Create validation scripts.
12. Create bootstrap script.
13. Create create-project script.
14. Create tests.
15. Run doctor.
16. Run security.
17. Run tests.
18. Run bootstrap.
19. Update status.
20. Report final result.

Create all required files, directories, manifests, scripts, docs, tests, rules, skills, hooks, memory files, and agent configuration files.



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
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Claude Code repository for docs, issues, release notes, and compatibility references."
    },
    {
      "id": "anthropic-claude-code-action",
      "name": "Anthropic Claude Code Action",
      "url": "https://github.com/anthropics/claude-code-action.git",
      "target": "external/sources/anthropic-claude-code-action",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official GitHub Action patterns for Claude Code automation, PR review, issue workflows, and CI integration."
    },
    {
      "id": "anthropic-skills",
      "name": "Anthropic Agent Skills",
      "url": "https://github.com/anthropics/skills.git",
      "target": "external/sources/anthropic-skills",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Official Agent Skills examples, specification, templates, and skill packaging patterns."
    },
    {
      "id": "anthropic-claude-plugins-official",
      "name": "Anthropic Claude Plugins Official",
      "url": "https://github.com/anthropics/claude-plugins-official.git",
      "target": "external/sources/anthropic-claude-plugins-official",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Claude Code plugin marketplace structure and plugin manifest examples."
    },
    {
      "id": "openai-codex",
      "name": "OpenAI Codex CLI",
      "url": "https://github.com/openai/codex.git",
      "target": "external/sources/openai-codex",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Codex CLI source and AGENTS.md behavior reference."
    },
    {
      "id": "google-gemini-cli",
      "name": "Google Gemini CLI",
      "url": "https://github.com/google-gemini/gemini-cli.git",
      "target": "external/sources/google-gemini-cli",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official Gemini CLI source for GEMINI.md, MCP, settings, and command compatibility."
    },
    {
      "id": "opencode",
      "name": "OpenCode",
      "url": "https://github.com/anomalyco/opencode.git",
      "target": "external/sources/opencode",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "OpenCode source for AGENTS.md, opencode config, agents, MCP, and plugin compatibility."
    },
    {
      "id": "modelcontextprotocol-servers",
      "name": "Model Context Protocol Servers",
      "url": "https://github.com/modelcontextprotocol/servers.git",
      "target": "external/sources/modelcontextprotocol-servers",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Current MCP server examples and server discovery references."
    },
    {
      "id": "modelcontextprotocol-registry",
      "name": "Model Context Protocol Registry",
      "url": "https://github.com/modelcontextprotocol/registry.git",
      "target": "external/sources/modelcontextprotocol-registry",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "MCP registry references for discovering MCP servers safely."
    },
    {
      "id": "github-mcp-server",
      "name": "GitHub MCP Server",
      "url": "https://github.com/github/github-mcp-server.git",
      "target": "external/sources/github-mcp-server",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "official",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Official GitHub MCP server for GitHub issue, PR, repo, workflow, and code search integration."
    },
    {
      "id": "agents-md",
      "name": "AGENTS.md Specification",
      "url": "https://github.com/openai/agents.md.git",
      "target": "external/sources/agents-md",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "standard",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "AGENTS.md standard/reference for cross-agent repository instructions."
    },
    {
      "id": "andrej-karpathy-skills",
      "name": "Andrej Karpathy Skills",
      "url": "https://github.com/forrestchang/andrej-karpathy-skills.git",
      "target": "external/sources/andrej-karpathy-skills",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "behavior-rules",
      "quarantine": false,
      "import_policy": "curated-only",
      "purpose": "Karpathy-style behavioral rules: think before coding, simplicity, surgical changes, goal-driven execution."
    },
    {
      "id": "andrej-karpathy-skills-cursor-vscode",
      "name": "Andrej Karpathy Skills for Cursor and VS Code",
      "url": "https://github.com/mbeijen/andrej-karpathy-skills-cursor-vscode.git",
      "target": "external/sources/andrej-karpathy-skills-cursor-vscode",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "behavior-rules",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Cursor/VS Code rule-file adaptation of Karpathy-style behavior rules."
    },
    {
      "id": "claude-mem",
      "name": "Claude Mem",
      "url": "https://github.com/thedotmack/claude-mem.git",
      "target": "external/sources/claude-mem",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "memory",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Persistent memory architecture reference. Must not install automatically."
    },
    {
      "id": "superpowers",
      "name": "Superpowers",
      "url": "https://github.com/obra/superpowers.git",
      "target": "external/sources/superpowers",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "skills",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Composable software-development skill methodology for multiple coding agents."
    },
    {
      "id": "claude-code-best-practice",
      "name": "Claude Code Best Practice",
      "url": "https://github.com/shanraisshan/claude-code-best-practice.git",
      "target": "external/sources/claude-code-best-practice",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "best-practices",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Community best-practice source for Claude Code agents, commands, skills, hooks, and workflows."
    },
    {
      "id": "awesome-claude-code",
      "name": "Awesome Claude Code",
      "url": "https://github.com/hesreallyhim/awesome-claude-code.git",
      "target": "external/sources/awesome-claude-code",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Curated discovery list for Claude Code skills, hooks, commands, plugins, workflows, and tooling."
    },
    {
      "id": "awesome-agent-skills",
      "name": "Awesome Agent Skills",
      "url": "https://github.com/VoltAgent/awesome-agent-skills.git",
      "target": "external/sources/awesome-agent-skills",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "discovery",
      "quarantine": true,
      "import_policy": "reference-only",
      "purpose": "Cross-agent discovery list for Claude Code, Codex, Gemini CLI, Cursor, and related skills."
    },
    {
      "id": "wshobson-agents",
      "name": "Claude Code Subagents by wshobson",
      "url": "https://github.com/wshobson/agents.git",
      "target": "external/sources/wshobson-agents",
      "type": "git",
      "enabled": true,
      "priority": "required",
      "tier": "agents",
      "quarantine": true,
      "import_policy": "curated-only",
      "purpose": "Community Claude Code subagent definitions for specialist-agent patterns."
    },
    {
      "id": "vercel-agent-skills",
      "name": "Vercel Labs Agent Skills",
      "url": "https://github.com/vercel-labs/agent-skills.git",
      "target": "external/sources/vercel-agent-skills",
   
…



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
| 23 | **ChoreographyAgent** | Movement design (MVs, dance challenges) | Emmy Choreography submissions; Goebel/Moore reels; dance-notation datasets | Beat-sync accuracy; safety constraints; viral-pattern alignment | Wins blind preference vs choreographer drafts | DirectorAgent, MVDirectorAgent | DirectorAgent (un-camera-friendly staging) | Kling 3.0 motion control (reference video); Cascadeur; beat-detection (librosa) | Self-Refine (rubric: beat-sync + safety) |
| 24 | **MusicVideoDirectorAgent** | Visual concept for songs | DirectorsLibrary; UKMVA/MTV VMA winners; Hype Williams/Spike Jonze | Edit-rhythm sync; lookbook coherence; artist-brief fit | Wins label-blind preference vs commercial MV shortlist | LabelA&RAgent, ArtistAgent | EditorAgent (cut on beat), DoPAgent | Runway Gen-4 (style-locked generation); Veo 3.1; mood-board tools (Are.na API) | Multi-agent debate (with DirectorAgent + EditorAgent) |
| 25 | **ComedyWriterAgent** | Skits, parody, viral meme writing | UCB/Groundlings manuals; SNL transcripts; Schur/Fey teaching | Joke-density; cold-open hook strength; predicted laughs/min | Beats UCB-table-read win rate on cold-reads | AudienceSim, ShowrunnerAgent | ScriptwriterAgent (no joke), SocialStrategistAgent (off-trend) | Audience laugh-prediction model; trending-audio API (TikTok Creative Center) | Reflexion (stores audience feedback in episodic memory) |
| 26 | **TalentAgent (On-camera)** | AI-rendered performance | Method-acting transcripts; consented actor performance corpora | Emotion-target match; charisma score (audience proxy) | Hold-rate matches top creators in cohort | DirectorAgent, CastingAgent | DirectorAgent (impossible blocking) | HeyGen Avatar IV; Synthesia personal avatars; emotion-detection models (AffectNet) | Self-Refine + emotion-regression validator |
| 27 | **UGCCreatorAgent** | Authentic-feel ads in creator voice | TikTok Creative Center; Alix-Earle-style benchmarks (style not identity) | Hook-rate ≥30%; "scripted" detector < threshold | Beats paid-creator avg ROAS at 0.1× cost | PerformanceMarketerAgent, BrandAgent | PerformanceMarketerAgent (wrong audience) | Veo 3.1 (portrait 9:16); ElevenLabs voice; CapCut API; TikTok Ads Manager | RLAIF (reward from ROAS signal) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 53 | **OrchestratorAgent** | Runs CrewAI/AutoGen/LangGraph DAG; retries, timeouts, fan-out/fan-in | LangGraph + CrewAI + AutoGen patterns; Airflow/Temporal; PGA schedule templates | DAG completion ≥99.5%; SLA adherence; deadlock = 0 | Lower TTD than human EP at same scope | ProducerAgent (scope), JudgeAgent (dispute), HiTL on stall | All agents (resource burn, retry storms) | LangGraph state machine; Temporal workflow engine; Redis (distributed locks); observability (LangSmith) | Agentic Graph (LangGraph) — deterministic DAG execution |
| 54 | **PlannerAgent** | Decomposes brief into phased DAG with assignments + critic gates | PMBOK; CrewAI task graphs; phase templates | Plan validity (no missing gate); cost variance <10% | Tighter, cheaper plans than EP first pass (blind A/B) | ProducerAgent, FinanceAgent (budget) | RouterAgent (wrong pick), OrchestratorAgent | LangGraph plan-gen; cost-estimation models; Gantt/PERT tools | ReAct (decompose → estimate → validate → emit DAG) |
| 55 | **RouterAgent** | Picks right specialist agent (and model) for each subtask | Agent-capability registry; benchmark history (cost/quality/latency) | Routing accuracy ≥95% vs oracle; cost within budget | Beats human producer in agent/vendor selection | OrchestratorAgent, CostOptimizerAgent | PlannerAgent (bad decomposition) | Agent registry DB; benchmark leaderboard cache; pricing APIs | Classifier + ReAct (match task embedding → ag
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



### From `corpus/study/ui/architecture_communication.md` Copy: `sources/excerpts/architecture_communication.md`.


```text
USER types in Critique Feed:
    "@DirectorAgent Use wider lens for Scene 3, it feels too claustrophobic"
    │
    ▼
FRONTEND
    │
    │  POST /api/productions/{id}/critiques
    │  Body: { to_agent: 1, content: "Use wider lens...", priority: "normal" }
    │
    ▼
API GATEWAY
    │
    │  Creates CritiqueMessage record
    │  Publishes to Event Bus with target agent
    │
    ▼
ORCHESTRATION ENGINE
    │
    │  Delivers critique to DirectorAgent's input queue
    │  DirectorAgent processes on next iteration:
    │    - Reads critique via MemoryAgent
    │    - Adjusts shot intent parameters
    │    - Re-generates with updated prompt
    │    - Publishes response critique back
    │
    ▼
EVENT BUS → WebSocket → Frontend
    │
    │  Agent response appears in Critique Feed
    │  Updated artifact appears in Gallery
```

| Event Type | Payload | Updates |
|-----------|---------|---------|
| `agent_state_change` | `{ agent_id, state, task, progress }` | DAG Canvas nodes |
| `artifact_created` | `{ artifact_id, type, version, producer, thumbnail_url }` | Gallery |
| `artifact_updated` | `{ artifact_id, version, quality_scores }` | Gallery + Quality |
| `critique_message` | `{ from, to, content, severity, attachments }` | Critique Feed |
| `gate_ready` | `{ gate_id, criteria, judge_score, artifacts }` | Gate Dialog + Notification |
| `gate_resolved` | `{ gate_id, decision, next_phase }` | DAG Canvas + Timeline |
| `budget_update` | `{ spent, remaining, per_agent_breakdown }` | Budget Tracker + Status Bar |
| `metric_update` | `{ agent_id, metric_name, value, threshold, pass }` | Quality Dashboard |
| `memory_entry` | `{ entry_id, content, accessed_by }` | Memory Panel |
| `tool_call` | `{ agent_id, tool, params, status, duration }` | Agent Inspector |
| `production_phase_change` | `{ production_id, new_phase }` | Context Bar + Timeline |
| `error` | `{ agent_id, error_type, message, recoverable }` | Notification + DAG (red node) |

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                        API GATEWAY LAYER                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                  │
│  │  Auth / RBAC │  │  Rate Limit  │  │  Validation  │                  │
│  └──────────────┘  └──────────────┘  └──────────────┘                  │
├─────────────────────────────────────────────────────────────────────────┤
│                        SERVICE LAYER                                     │
│                                                                         │
│  ┌──────────────────┐     ┌──────────────────┐                          │
│  │ Production       │     │ WebSocket        │                          │
│  │ Manager Service  │     │ Gateway Service  │                          │
│  │                  │     │                  │                          │
│  │ • CRUD           │     │ • Client mgmt   │                          │
│  │ • Brief parsing  │     │ • Event routing  │                          │
│  │ • Permissions    │     │ • Filtering      │                          │
│  └────────┬─────────┘     └────────┬─────────┘                          │
│           │                         │                                    │
│           ▼                         ▼                                    │
│  ┌──────────────────────────────────────────────┐                       │
│  │              EVENT BUS                        │                       │
│  │         (Redis Streams / NATS)                │                       │
│  │                                              │                       │
│  │  Topics:                                     │                       │
│  │  • production.{id}.agent_events              │                       │
│  │  • production.{id}.critiques                 │                       │
│  │  • production.{id}.gates                     │                       │
│  │  • production.{id}.artifacts                 │                       │
│  │  • system.alerts                             │                       │
│  └──────────────────────┬───────────────────────┘                       │
│                         │                                                │
│                         ▼                                                │
│  ┌──────────────────────────────────────────────┐                       │
│  │         ORCHESTRATION ENGINE                  │                       │
│  │         (LangGraph + Temporal)                │                       │
│  │                                              │                       │
│  │  ┌────────────┐  ┌────────────┐             │                       │
│  │  │ DAG State  │  │ Task Queue │             │                       │
│  │  │ Machine    │  │ (per agent)│             │                       │
│  │  └────────────┘  └────────────┘             │                       │
│  │                                              │                       │
│  │  ┌────────────┐  ┌────────────┐             │                       │
│  │  │ Retry /    │  │ Gate       │             │                       │
│  │  │ Timeout    │  │ Evaluator  │             │                       │
│  │  └────────────┘  └────────────┘             │                       │
│  └──────────────────────┬───────────────────────┘                       │
│                         │                                                │
│                         ▼                                                │
│  ┌──────────────────────────────────────────────┐                       │
│  │           AGENT WORKER POOL                   │                       │
│  │                                              │                       │
│  │  Each agent worker:                          │                       │
│  │  1. Pulls task from queue                    │                       │
│  │  2. Loads agent config (prompt, tools, rubric)│                      │
│  │  3. Calls LLM (reason about task)            │                       │
│  │  4. Calls tools (generate video, evaluate)   │                       │
│  │  5. Self-refines if below threshold          │                       │
│  │  6. Publishes result + events to Event Bus   │                       │
│  │                                              │                       │
│  │  Scaling: Horizontal worker pool             │                       │
│  │  GPU workers for generation tasks            │                       │
│  │  CPU workers for LLM-only tasks              │                       │
│  └──────────────────────────────────────────────┘                       │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                        DATA LAYER                                        │
│                                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐               │
│  │PostgreSQL│  │ S3/R2    │  │ Pinecone │  │ Redis    │               │
│  │          │  │          │  │ /Weaviate│  │          │               │
│  │Production│  │ Artifacts│  │ Memory   │  │ Cache +  │               │
│  │metadata  │  │ (video,  │  │ (vector  │  │ Sessions │               │
│  │Gate state│  │  audio,  │  │  DB for  │  │ Event    │               │
│  │Critiques │  │  images) │  │  Memory  │  │ Streams  │               │
│  │Configs   │  │          │  │  Agent)  │  │          │               │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘               │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

| Role | Technology | Why |
|------|-----------|-----|
| Frontend framework | React 19 + Next.js 15 | SSR for dashboard, client for real-time console |
| State management | Zustand + React Query | Lightweight; optimistic updates; WebSocket sync |
| WebSocket client | Socket.io-client | Auto-reconnect, room-based filtering |
| API Gateway | FastAPI (Python) or Express (Node.js) | Fast, typed, middleware ecosystem |
| Orchestration | LangGraph (Python) | DAG execution with state + HiTL gates |
| Workflow durability | Temporal | Long-running workflow guarantees |
| Event Bus | Redis Streams or NATS JetStream | Pub/sub + persistence + replay |
| Agent runtime | LangGraph nodes / CrewAI agents | Tool-calling LLM agents with typed I/O |
| LLM providers | Gemini 2.5 Pro, GPT-4o, Claude 4 | Via litellm for unified interface |
| Gen AI tools | Veo 3.1, Sora 2, Runway, Kling, ElevenLabs | Direct API calls from agent workers |
| Database | PostgreSQL + Drizzle ORM | Production state, configs, audit log |
| Object storage | S3 / Cloudflare R2 | Video, audio, image artifacts |
| Vector DB | Pinecone / Weaviate | MemoryAgent semantic retrieval |
| Cache | Redis | Session state, rate limiting, hot data |
| Observability | LangSmith + Grafana | Agent tracing, performance dashboards |



### From `corpus/study/ui/backend_agent_management.md` Copy: `sources/excerpts/backend_agent_management.md`.


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

a) Load AgentDefinition for agent_id=1 (DirectorAgent)
  b) Fetch input artifacts from Asset Store
  c) Fetch relevant memories from MemoryAgent (vector search)
  d) Construct LLM messages:

e) Call LLM (Gemini 2.5 Pro):
     response = await llm.chat(messages, tools=[veo_api, memory_store])

MemoryAgent isn't just another agent — it's a **shared service** that other agents call:

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

→ tool_call: memory.recall("Act 2 visual style lock")
→ Returns: "Style lock: Veo 3.1 seed #4412, melancholic neo-noir"



### From `corpus/study/ui/project_creation_flow.md` Copy: `sources/excerpts/project_creation_flow.md`.


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

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  PRODUCTION: "Luna" (Type E: AI Short Film)     Phase: Production  ⏱ 12m    │
├──────────────────┬──────────────────────────────────────────────────────────┤
│  VIEW TABS:      │                                                          │
│  [DAG] Timeline  │                                                          │
│  Gallery Critique│            ┌─────────────┐                               │
│                  │            │  [Brief]    │                               │
│  FILTER:         │            └──────┬──────┘                               │
│  ○ All           │                   │                                      │
│  ○ Active        │                   ▼                                      │
│  ○ Blocked       │        ┌──────────────────┐                              │
│  ○ Completed     │        │  PlannerAgent    │                              │
│                  │        │  ✓ Complete      │                              │
│  ZOOM: [─────●]  │        └────────┬─────────┘                              │
│                  │                 │                                         │
│  LAYERS:         │                 ▼                                         │
│  ☑ Orchestration │     ┌─────────────────────┐                              │
│  ☑ Craft         │     │  OrchestratorAgent  │                              │
│  ☑ Meta-Creative │     │  ● Running          │                              │
│  ☑ Meta-Research │     └────┬───────────┬────┘                              │
│  ☑ Meta-Optimize │          │           │                                   │
│  ☑ Critique      │          ▼           ▼                                   │
│                  │   ┌───────────┐  ┌──────────────┐                        │
│                  │   │RouterAgent│  │MemoryAgent   │                        │
│                  │   │ ● Running │  │ ● Listening  │                        │
│                  │   └─────┬─────┘  └──────────────┘                        │
│                  │         │                                                 │
│                  │    ┌────┼────┬────────┬──────────┐                        │
│                  │    ▼    ▼    ▼        ▼          ▼                        │
│                  │ ┌────┐┌────┐┌────┐┌────────┐┌────────┐                   │
│                  │ │Dir ││DoP ││Edit││Composer││VFX Sup │                   │
│                  │ │ ●  ││ ○  ││ ○  ││  ○     ││  ○     │                   │
│                  │ └────┘└────┘└────┘└────────┘└────────┘                   │
│                  │         │         ▲                                       │
│                  │         ▼         │                                       │
│                  │  ┌──────────────────────┐                                │
│                  │  │   GateKeeperAgent    │                                │
│                  │  │   ⚠ Awaiting Approval │                                │
│                  │  └──────────────────────┘                                │
│                  │         ▲                                                 │
│                  │         │                                                 │
│                  │  ┌──────────────┐                                        │
│                  │  │  JudgeAgent  │                                        │
│                  │  │  ● Scoring   │                                        │
│                  │  └──────────────┘                                        │
│                  │                                                          │
├──────────────────┴──────────────────────────────────────────────────────────┤
│  DETAIL DRAWER ▲                                                            │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ DirectorAgent │ Task: Shot Intent #4 │ Score: CLIP-T 0.34 (✓≥0.32)  │   │
│  │ Input: Scene 2 script │ Output: shot_intent_04.json │ Critiques: 2   │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
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
│                                                                   
…



## Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


## Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


## Provenance

- Master roster row va_id=58 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `C:\Project\va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.memory · va_id=58 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **MemoryAgent** (`video.memory`, va_id=58, category `9-Meta`).

### Responsibility focus
Episodic + long-term project memory; retrieval for any agent

### Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: agent memory architectures MemGPT, episodic memory for media projects, hierarchical memory RAG
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI agent memory systems, project memory for film AI
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: building memory for AI agents, long-horizon agent memory

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

<!-- migration_capability_research · video.memory · v1 · 2026-07-13 -->
