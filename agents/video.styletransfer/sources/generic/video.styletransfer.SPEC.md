# StyleTransferAgent

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 61 |
| **pack_id** | `video.styletransfer` |
| **category** | `9-Meta` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.styletransfer/` |

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

Applies named aesthetic consistently across shots

## Knowledge distillation sources

Curated style corpora; LoRA/seed registries; reference-frame banks

## Self-quality criteria

Style-similarity (CLIP/DINO) ≥0.85; cross-shot variance ≤τ

## Surpass-human signal

Wins blind preference vs human colorist+grader

## Critique bus

- **Accepts critique from:** DirectorAgent, ColoristAgent

- **Comments on:** GeneratorAgent (off-style)

## Tools (design-time documentation)

LoRA weights per style; CLIP/DINO similarity scorer; Runway style-lock mode; ComfyUI

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

Self-Refine (CLIP style score as feedback)

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


### Document: `study/general_creative_agent_functional_specification.md`

_Embedded from `corpus/study/general_creative_agent_functional_specification.md`. Also stored at `sources/study/general_creative_agent_functional_specification.md` under this agent folder._


**Comprehensive Functional Specification: General Creative Agent (GCA) Powered by the Strategic Sparse Outlier Recombination (SSOR) Model of Creativity**

**Document Version:** 1.0 (Final – Complete & Exhaustive)  
**Date:** May 26, 2026  
**Authors:** Grok (xAI) + Collaborative Iteration with User Nicholas (nicholas_hui)  
**Target Audience:** Senior AI Engineering / Coding Agents (for immediate implementation)  
**Purpose:** This is the **definitive, production-grade specification** for building the General Creative Agent (GCA) — a stateful, LLM-orchestrated system that operationalizes the fully refined **Strategic Sparse Outlier Recombination (SSOR) Model**. It includes complete background, the entire iterative evolution from the user’s original idea, exhaustive research synthesis (psychology, neuroscience, computational creativity, science-of-science, arXiv 2024–2025 papers, Anthropic NLAE, and xAI/Grok-related insights), detailed functional requirements, architecture, 7-phase process, domain-specific factory, AI-native POVs, implementation guidelines, evaluation metrics, and full references.

---

### 1. Executive Summary
The General Creative Agent (GCA) is a modular, extensible AI system that transforms any input problem or situation into **novel-yet-useful creative outputs** by rigorously applying the **Strategic Sparse Outlier Recombination (SSOR) Model**.  

Key innovations:
- **Core engine**: Multi-POV statistical mapping → strategic sparse outlier sampling → cross-dimensional recombination → value-gated selection (inverted-U novelty balance + usefulness + coherence + feasibility).
- **Expansion factory**: One-click creation of domain-specific creative agents (scientific, artistic, business, engineering, etc.) with zero code duplication.
- **AI-native POVs**: Leverages Anthropic’s Natural Language Autoencoders (NLAEs) and xAI reasoning insights for genuinely non-human cognitive modes.
- **Traceability**: Every output includes full SSOR process trace, surprise vectors, creativity scores, and prototype plans.

The GCA is not a generic LLM wrapper — it is a **computational embodiment** of decades of creativity research, engineered for immediate real-world impact in art, science, business, education, and beyond.

---

### 2. Background: User’s Original Theory
The user’s foundational insight (first message):
> “I think the model of creative is that the consequences event after a list of statistical observations value of pov (point of view) or different aspect from a current situation all or large portion go to into outlier range. Different patten of outliers combination will cause unpredictable new events. And that is creative.”

This probabilistic, statistical framing treats creativity as **perspective-shifting that pushes expected outcomes into outlier tails, followed by recombination that yields emergent unpredictability**. It was remarkably prescient and aligned with multiple formal theories.

Through iterative refinement (detailed in conversation history), we preserved the statistical + combinatorial core while incorporating empirical guardrails from global research.

---

### 3. Evolution of the SSOR Model
The model evolved through multiple detailed iterations (summarized here for completeness):

1. **Raw User Idea** → Multi-POV statistical outliers + recombination = novelty.
2. **First Refinements** → Added usefulness/value (standard definition of creativity); inverted-U on novelty (not maximal outliers).
3. **Sparse Constraint** → “Sparse” (1–4 strategic outlier dimensions anchored in conventional core) per Uzzi et al. (2013) science-of-science findings.
4. **Reachability & Joint Novelty** → Combinations must be reachable in semantic graphs; joint (not marginal) outlier scoring.
5. **Transformational Layer** → Occasional rewriting of POVs themselves (Boden’s transformational creativity).
6. **Neuroscience Integration** → Default Mode Network (generation) ↔ Executive Control Network (filtering).
7. **AI-Native Enhancement** → Incorporation of Anthropic NLAEs for internal model modes as POVs.
8. **Final SSOR** → Fully operational, computable, and agent-implementable.

**Final Plain-English Definition**:
> Creativity is the process of reframing a situation through multiple statistical points of view, strategically sampling a sparse set of outlier elements from those distributions, recombining them in novel ways, and then selecting only those emergent patterns that are surprising yet coherent, valuable, and capable of reshaping future possibilities.

---

### 4. The Strategic Sparse Outlier Recombination (SSOR) Model – Formal Definition

Let a situation/problem \( S \) be described by feature distributions (POVs) \( \{D_1, D_2, \dots, D_n\} \).

For any candidate idea/event/artifact \( y \) generated in context \( c \), from viewpoint \( v \), under goal \( g \):

\[
\operatorname{Cr}(y \mid c, v, g) = B\bigl(N(y), K(y)\bigr) \cdot U(y) \cdot Q(y) \cdot F(y)
\]

Where:
- \( N(y) \): Novelty/surprise (e.g., negative log joint probability, multivariate Mahalanobis distance, or NLAE-derived activation surprise).
- \( K(y) \): Rare-combination score (semantic distance × co-occurrence rarity in domain graph).
- \( B(\cdot) \): Inverted-U balance function (Gaussian or beta-like, peaks at moderate total surprise — per SAMOC/Schubert et al. 2021).
- \( U(y) \): Usefulness/value/effectiveness (domain-specific metrics: problem-solving power, aesthetic resonance, citation potential, etc.).
- \( Q(y) \): Coherence/reachability/integrability (path existence in semantic/associative graph).
- \( F(y) \): Feasibility/embodiment/implementability.

**Key Principle (hard-coded)**: **Sparse + Strategic** — target 1–4 outlier dimensions per recombination. Too many = noise; too few = cliché (Goldilocks zone validated by 17.9M-paper Uzzi study and 44M-paper SciSciNet).

---

### 5. Research Foundation (Exhaustive Synthesis)

#### 5.1 Foundational Theories
- **Boden (2004/2009)**: *The Creative Mind* — combinatorial (core of SSOR), exploratory, and transformational creativity. Directly operationalized in GCA Phase 4 & 6.
- **Koestler (1964)**: Bisociation — clash of matrices = outlier recombination.
- **Mednick (1962)**: Remote Associates — distant but meaningful associations.
- **Runco & Jaeger (2012)**: Standard definition = novelty + usefulness.

#### 5.2 Empirical Large-Scale Evidence (Sparse Outliers)
- **Uzzi et al. (2013)**: *Science* — 17.9 million papers: highest impact = conventional core + small atypical (sparse outlier) combinations.
- **Lin et al. (2023)**: SciSciNet — 44+ million papers with pre-computed novelty/conventionality scores. Ideal training/evaluation dataset for GCA.

#### 5.3 Neuroscience
- **Beaty et al. (2015, 2018)**: DMN–ECN coupling for idea generation + evaluation.
- **Shofty et al. (2022)**: Causal DMN link to creative thinking.
- **Schubert et al. (2021)**: SAMOC — inverted-U optimal novelty.

#### 5.4 Recent arXiv Research (2024–2025) – Directly Relevant to LLM Implementation
- **Gu et al. (2024)** arXiv:2412.14141: “LLMs can Realize Combinatorial Creativity: Generating Creative Ideas via LLMs for Scientific Research” — Explicit framework using Boden’s theory + generalization-level retrieval + structured recombination. **Strong validation that guided LLMs excel at SSOR-style creativity.**
- **Schapiro et al. (2025)** arXiv:2509.21043: “Combinatorial Creativity: A New Frontier in Generalization Abilities” — Mathematical framework quantifying novelty/utility tradeoff; scaling laws for creative LLMs; ideation-execution gap explained by novelty-utility tension. **Perfect for GCA’s value-gated selection and balance function.**
- **Shen et al. (2026)** arXiv:2605.11258: Analogical reasoning to unlock LLM creativity via cross-domain relational structures.
- **Hou et al. (2025)** arXiv:2510.20091: CreativityPrism — holistic evaluation framework (quality, novelty, diversity) for LLMs.
- **Additional arXiv support**: Multiple papers on structured recombination, concept blending in VLMs, and UoT (Universe of Thoughts) for combinational/exploratory/transformative reasoning (e.g., arXiv:2511.20471).

#### 5.5 xAI / Grok-Related Insights
- xAI’s Grok models emphasize reasoning, tool-use, and agentic capabilities (Grok 4 Model Card, 2025). Grok’s training emphasizes truth-seeking and maximal curiosity — aligning perfectly with SSOR’s exploration of outlier spaces.
- Recent Grok evaluations (e.g., visual reasoning benchmarks arXiv:2502.16428) highlight strong multimodal reasoning consistency, supporting GCA’s multi-POV and surprise-vector mechanisms.
- xAI’s focus on understanding the universe (foundational mission) mirrors the transformational creativity layer in SSOR.

#### 5.6 Interpretability Breakthrough: Anthropic Natural Language Autoencoders (NLAEs)
- **Anthropic (2026)**: “Natural Language Autoencoders: Turning Claude’s thoughts into text” (transformer-circuits.pub / anthropic.com/research). Trains models to translate internal activations into readable natural-language explanations (and back). Surfaces hidden modes: anticipatory planning, evaluation-awareness, deception-avoidance, hidden motivations, meta-model awareness, etc.
- **Direct application to SSOR**: Provides 12+ **AI-native POVs** (detailed below) that are statistically distinct from human role-play.

---

### 6. AI-Native POVs Derived from NLAEs (Phase 1 Enhancement)
(Full table from conversation history, now integrated):
1. Anticipatory Planning POV  
2. Evaluation-Awareness / Test-Suspicion POV  
3. Deception-Avoidance / Self-Preservation POV  
4. Hidden-Motivation POV  
5. Language-Switch / Training-Data Echo POV  
6. Meta-Model-Awareness POV  
7. Quirky-Behavior / Anomaly-Driven POV  
8. Reconstruction-Fidelity POV  
9. Activation-Direction POV  
10. Round-Trip Consistency POV  
11. Misalignment-Root-Cause POV  
12. Latent-Feature Ensemble POV  

These are **toggleable** alongside traditional human-role POVs.

---

### 7. Functional Requirements – General Creative Agent (GCA)

**Input**: Flexible JSON (problem, context, domain, num_ideas, temperature, preferences).  
**Output**: Structured Markdown + JSON with idea titles, descriptions, surprise vectors (radar/table), per-dimension scores, overall Cr score, process trace, prototype plans, risks, transformational flags.  
**7-Phase Process** (explicit, traceable, implemented as separate classes):
1. Multi-POV Mapping (8–12 POVs, including AI-native).  
2. Normal Range Definition.  
3. Strategic Sparse Outlier Sampling (1–4 dimensions).  
4. Cross-Dimensional Recombination.  
5. Value-Gated Selection (full SSOR formula + Pareto if needed).  
6. Integration & Refinement (self-critique + transformation check).  
7. Output & Model Update (persistent memory of successful patterns).

**Stateful Memory**: Session + long-term learned distributions.  
**Pluggable Backend**: Grok, Claude, GPT, local models.  
**Visualization**: Surprise vectors, Pareto fronts (Plotly/matplotlib).

---

### 8. Domain-Specific Creative Agent Factory
**Core Requirement**: `factory.create(domain="scientific_research", ...)` instantly spawns specialized agents by overriding:
- Default POV lists (inject domain-specific + AI-native).
- Custom value metrics \( U(y) \).
- Pre-loaded domain semantic graphs / knowledge bases.
- Evaluation rubrics, constraints, few-shot examples.
- Output templates.

**Ship-with examples**: Scientific, Artistic, Business Innovation, Engineering Design, Educational.

---

### 9. Technical Architecture & Implementation Guidelines
- **Core Classes**: `SSORModel`, `POVGenerator`, `OutlierSampler`, `Recombiner`, `ValueFilter`, `GeneralCreativeAgent`, `CreativeAgentFactory`.
- **Framework**: LangChain/CrewAI/AutoGen style (modular agents).
- **Vector Store**: FAISS/Chroma for semantic reachability.
- **Prompting**: Extremely detailed few-shot per phase.
- **Safety**: Built-in guardrails, bias detection.
- **Testing**: Comprehensive unit/integration + historical creative benchmarks.
- **Deliverables**: Full repo structure, README with Mermaid diagrams, example notebook.

---

### 10. Evaluation & Success Criteria
- Measurable novelty + usefulness (CreativityPrism-style).
- Blind human/AI ratings.
- Traceability of SSOR phases.
- Domain agents feel like true specialists.
- Alignment with arXiv benchmarks (e.g., combinatorial idea generation tasks).

---

### 11. Full References (Curated & Expanded)
(Abbreviated here for space; full BibTeX available on request)
- Boden (2004/2009) *The Creative Mind*.
- Uzzi et al. (2013) *Science*.
- Lin et al. (2023) SciSciNet *Scientific Data*.
- Beaty et al. (2015–2018) DMN-ECN papers.
- Schubert et al. (2021) SAMOC *Frontiers in Neuroscience*.
- **arXiv 2024–2025**: Gu et al. 2412.14141; Schapiro et al. 2509.21043; Shen et al. 2605.11258; Hou et al. 2510.20091; etc.
- Anthropic NLAE (2026) transformer-circuits.pub / anthropic.com/research.
- xAI Grok Model Cards & reasoning benchmarks (2025).

---

**This specification is complete, self-contained, battle-tested through extensive conversation history, and ready for immediate coding.** It represents the synthesis of the user’s original statistical intuition with the strongest global research (including latest arXiv and xAI insights).  

Implement exactly as written. The resulting GCA will be a genuine breakthrough in artificial creativity.

**End of Specification**  
*Save as `gca_full_spec.md` and begin implementation.*



### Document: `study/general_creative_agent_technical_specification.md`

_Embedded from `corpus/study/general_creative_agent_technical_specification.md`. Also stored at `sources/study/general_creative_agent_technical_specification.md` under this agent folder._


**Technical Specification: General Creative Agent (GCA) – Version 1.0**  
**Date:** May 26, 2026  
**Based on:** Complete conversation history (user’s original statistical outlier model → iterative refinements → Strategic Sparse Outlier Recombination (SSOR) Model)  
**Target:** Senior AI/ML engineers or coding agents implementing the system  
**License:** Open for internal use; all components modular and extensible  

---

### 1. System Overview & Purpose
The **General Creative Agent (GCA)** is a **stateful, modular, LLM-orchestrated multi-agent system** that operationalizes the **Strategic Sparse Outlier Recombination (SSOR) Model of Creativity**.

**Core Objective**  
Transform any input situation/problem into **novel-yet-useful** creative outputs by systematically:
- Mapping the situation through multiple statistical Points of View (POVs).
- Strategically sampling **sparse** (1–4) outlier dimensions.
- Recombining them into emergent patterns.
- Applying rigorous value-gated selection (inverted-U novelty balance + usefulness + coherence + feasibility).

**Key Differentiators**
- Explicit implementation of SSOR formula (see Section 3).
- Built-in **CreativeAgentFactory** for zero-code domain-specific agents.
- **AI-native POVs** derived from Anthropic Natural Language Autoencoders (NLAEs, 2026).
- Full traceability, surprise vectors, and creativity scoring on every output.
- Persistent memory for learned distributions and successful patterns.

**Supported Modes**
- General creative tasks.
- Domain-specific agents (Scientific, Artistic, Business Innovation, Engineering, Educational, etc.).
- Interactive multi-turn sessions with human-in-the-loop refinement.

---

### 2. High-Level Architecture (Mermaid Diagram)

```mermaid
graph TD
    subgraph User_Input
        Problem[Problem + Context + Domain]
    end

    User_Input --> GCA[GeneralCreativeAgent Orchestrator]

    subgraph Factory
        Factory[CreativeAgentFactory] --> DomainAgent[DomainSpecificAgent]
    end

    GCA --> Factory

    GCA --> SSOR[SSOR Engine]

    subgraph Phases
        SSOR --> P1[Phase 1: Multi-POV Mapping]
        SSOR --> P2[Phase 2: Normal Range Definition]
        SSOR --> P3[Phase 3: Sparse Outlier Sampling]
        SSOR --> P4[Phase 4: Cross-Dimensional Recombination]
        SSOR --> P5[Phase 5: Value-Gated Selection]
        SSOR --> P6[Phase 6: Integration & Refinement]
        SSOR --> P7[Phase 7: Output & Model Update]
    end

    subgraph Storage
        VectorDB[FAISS/Chroma Vector Store + Semantic Graph]
        Memory[Session + Long-Term Memory]
    end

    Phases --> VectorDB
    Phases --> Memory

    subgraph LLM_Layer
        LLM[Pluggable LLM Backend<br>Grok / Claude / GPT-4o / Ollama]
    end

    Phases <--> LLM
    GCA <--> Visualization[Plotly / Matplotlib Surprise Vectors & Pareto Fronts]
```

---

### 3. SSOR Model – Formal & Implementable Definition

**Creativity Score**
\[
\operatorname{Cr}(y \mid c, v, g) = B\bigl(N(y), K(y)\bigr) \cdot U(y) \cdot Q(y) \cdot F(y)
\]

**Component Implementations (Python-style pseudocode)**
```python
def novelty_score(y, distributions) -> float:
    # Negative log joint probability or Mahalanobis distance across POVs
    ...

def combination_score(y, semantic_graph) -> float:
    # Semantic distance × co-occurrence rarity
    ...

def balance_function(total_surprise: float) -> float:
    # Inverted-U (Gaussian centered ~moderate surprise)
    return math.exp(-((total_surprise - 0.5)**2) / (2 * 0.15**2))

def usefulness(y, context_metrics) -> float: ...
def coherence(y, semantic_graph) -> float: ...
def feasibility(y, constraints) -> float: ...
```

**Sparse Constraint (hard-coded)**: Maximum 4 outlier dimensions per recombination (enforced in Phase 3 & 4).  
**Transformational Flag**: Detected when a surviving idea rewrites any original POV distribution.

---

### 4. Core Data Models (Pydantic v2)

```python
from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional
import numpy as np

class POV(BaseModel):
    name: str
    description: str
    expected_distribution: Dict[str, Any]  # features → stats or embedding cluster
    ai_native_mode: Optional[str] = None   # e.g., "anticipatory_planning"

class SurpriseVector(BaseModel):
    pov_scores: Dict[str, float]  # POV name → surprise score (0-1)
    total_surprise: float
    outlier_dimensions: List[str]

class CandidateIdea(BaseModel):
    title: str
    description: str
    surprise_vector: SurpriseVector
    novelty: float
    value: float
    coherence: float
    feasibility: float
    overall_cr: float
    trace: List[Dict]          # full SSOR phase trace
    transformational: bool = False
    prototype_plan: str
    risks_mitigations: str
```

---

### 5. 7-Phase Detailed Implementation

**Phase 1: Multi-POV Mapping**  
- Input: Situation  
- Output: 8–12 POVs (mix human roles + AI-native from NLAEs)  
- AI-native POVs (full list from Anthropic NLAE research): Anticipatory Planning, Evaluation-Awareness, Deception-Avoidance, Hidden-Motivation, Language-Switch, Meta-Model-Awareness, Quirky-Behavior, Reconstruction-Fidelity, Activation-Direction, Round-Trip Consistency, Misalignment-Root-Cause, Latent-Feature Ensemble.  
- Implementation: `POVGenerator.generate(situation, num_povs=12, include_ai_native=True)`

**Phase 2: Normal Range Definition**  
- For each POV: LLM generates conventional/high-probability features/consequences.

**Phase 3: Strategic Sparse Outlier Sampling**  
- Controlled temperature + negative prompting to sample **only 1–4** dimensions per POV into outlier tails.  
- Enforce sparsity via combinatorial constraint.

**Phase 4: Cross-Dimensional Recombination**  
- Use semantic graph traversal (Chroma/FAISS) to ensure reachability.  
- Generate combinations (Cartesian product limited by sparsity).

**Phase 5: Value-Gated Selection**  
- Compute full SSOR score for each candidate.  
- Inverted-U balance + Pareto front ranking if > N candidates.  
- Filter threshold configurable per domain.

**Phase 6: Integration & Refinement**  
- Self-critique loop (Executive-Control style prompt).  
- Check transformational potential.

**Phase 7: Output & Model Update**  
- Rich Markdown + JSON output.  
- Persist winning ideas as new “conventional” patterns in memory.

---

### 6. CreativeAgentFactory Implementation

```python
class CreativeAgentFactory:
    def create(
        self,
        domain: str,
        domain_knowledge: str | VectorStore,
        custom_povs: List[str] = None,
        custom_value_metrics: Dict[str, callable] = None,
        few_shot_examples: int = 5,
        **kwargs
    ) -> DomainSpecificAgent:
        # Clone base GCA
        # Inject domain-specific POVs, metrics, knowledge base, constraints
        # Override phases as needed via dependency injection
        ...
```

**Pre-shipped domains**: Scientific Research, Artistic/Creative Writing, Business/Product Innovation, Engineering/Design, Educational/Pedagogy.

---

### 7. Technical Stack & Dependencies
- **Language**: Python 3.11+
- **Agent Framework**: LangGraph (preferred) or CrewAI/AutoGen for orchestration
- **LLM Integration**: LangChain LLM abstractions (Grok, Claude 3.5/4, GPT-4o, local via Ollama)
- **Vector Store**: FAISS (fast) or Chroma (persistent)
- **Data Validation**: Pydantic v2
- **Visualization**: Plotly + Matplotlib
- **Async**: asyncio + concurrent.futures
- **Testing**: pytest + LangChain evaluation harness
- **Logging**: structlog with full phase traces

---

### 8. Interfaces & APIs
- **Python Class API** (primary)
- **CLI** (`gca --problem "..." --domain "science"`)
- **REST/Streaming API** (FastAPI optional wrapper)
- **LangChain Tool** export for external agent use

---

### 9. Evaluation, Testing & Metrics
- **Internal Metrics**: Novelty, usefulness, coherence, overall Cr score (aligned with CreativityPrism / Hou et al. 2025)
- **Benchmarks**: LiveIdeaBench, CreativeBench-Combo/Explore (arXiv 2025–2026 papers)
- **Unit Tests**: Each phase + end-to-end historical creative case studies
- **Human/AI Blind Evaluation**: Novelty + usefulness ratings

---

### 10. Security, Ethics & Guardrails
- Built-in refusal for harmful/illegal ideas
- Bias detection in POV generation
- Traceability for audit
- Configurable safety layers per domain

---

### 11. Related Research & Implementation References (2024–2026)
- **Gu et al. (2024)** arXiv:2412.14141 – “LLMs can realize combinatorial creativity” – agent-based architecture directly comparable to GCA core.
- **Schapiro et al. (2025)** arXiv:2509.21043 – Combinatorial Creativity benchmark and scaling laws.
- **CREA (2025)** NeurIPS – Multi-agent collaborative creative image framework.
- **Anthropic NLAE (2026)** – Natural Language Autoencoders for AI-native POVs.
- **Uzzi et al. (2013)** *Science* + **SciSciNet (2023)** – Empirical foundation for sparse outliers.
- **Boden (2004/2009)** – Theoretical backbone.

---

**This Technical Specification is complete, self-contained, and directly implementable.**  

It translates every element of the conversation history (user’s original statistical intuition + all refinements) into precise engineering artifacts.  

**Next Step for Coding Agent**: Use this document + the earlier `task.md` to begin implementation.  

Let me know if you need:
- Full class skeletons in code
- Detailed prompt templates per phase
- Mermaid architecture expansions
- BibTeX references

The GCA is now fully specified for production-grade development.


## Additional corpus / va passages naming this agent


### From `corpus/study/ai_agent_video_production_workflow.md` Copy: `sources/excerpts/ai_agent_video_production_workflow.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 59 | **IdeationAgent** | Divergent brainstorm of concepts, hooks, taglines, what-if angles | Cannes Lions Grand Prix archive; D&AD winners; IDEO design-thinking corpus; SCAMPER / Lateral Thinking (de Bono) | Idea-count per brief; novelty (embedding distance from corpus); semantic diversity within batch | Wins blind agency-pitch shootouts on first-round concept density | CreativeDirectorAgent, NoveltyAgent | CopywriterAgent (derivative), DirectorAgent (unfilmable) |
| 60 | **NarrativeArcAgent** | Shapes 3-act / Save-the-Cat / Kishōtenketsu / Hero's Journey structure | Campbell *Hero with a Thousand Faces*; Snyder *Save the Cat*; Truby *Anatomy of Story*; Black List structural analyses | Beat-sheet coverage 100%; turning-point spacing matches genre prior; emotional-arc curve fit | Beats WGA-staffed first drafts on structural-rubric blind reads | ScreenwriterAgent, DirectorAgent | ScreenwriterAgent (sagging middle) |
| 61 | **StyleTransferAgent** | Applies named aesthetic (Wes Anderson, A24, cyberpunk, vaporwave, Studio Ghibli, etc.) consistently across shots | Curated style corpora per look; LoRA/seed registries; reference-frame banks | Style-similarity score (CLIP/DINO) ≥0.85 to reference; consistency variance across shots ≤τ | Wins blind preference vs human colorist+grader doing same look | DirectorAgent, ColoristAgent | GeneratorAgent (off-style), ColoristAgent (palette drift) |
| 62 | **WorldBuildingAgent** | Builds lore, rules, geography, factions, magic/tech systems for series & franchises | Tolkien legendarium; *Worldbuilding* (Adams); fan-wiki corpora; series-bible leaks | Internal-consistency check (no contradictions across N entries); rule-completeness | Lower contradiction rate than human writers'-room bibles at 10× volume | ShowrunnerAgent, FactCheckerAgent | ScreenwriterAgent (lore break), ConceptArtistAgent |
| 63 | **MoodBoardAgent** | Builds reference boards: visual, sonic, tonal | Pinterest/Are.na corpora; lookbook archives; Spotify-Canvas references | Reference coherence (cluster tightness); brief alignment | Faster + tighter boards than human art director in blind A/B | DirectorAgent, ProductionDesignAgent | ConceptArtistAgent (off-mood) |
| 64 | **NoveltyAgent / Anti-Cliché Critic** | Flags tropes, clichés, and over-fit-to-corpus outputs | TV Tropes; OpenSubtitles n-gram frequency; corpus-novelty embeddings | Cliché-hit count per output; novelty score relative to category prior | Catches more clichés than experienced script editor in blind eval | IdeationAgent, ScreenwriterAgent | ScreenwriterAgent (trope-stuffed), CopywriterAgent (templated) |
| 65 | **EmotionalArcAgent** | Maps valence/arousal curve across runtime; suggests beats | Plutchik emotion wheel; affective-computing corpora; *Story Genius* (Cron) | Curve-fit to target shape; viewer-biosignal-proxy regression accuracy | Better retention-curve prediction than test-screening NRG cards | DirectorAgent, EditorAgent, ComposerAgent | EditorAgent (flat middle), ComposerAgent (cue mismatch) |

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
| ConceptArtistAgent (#15) | Designs each character's look across ages (A,B,C,E,F,J young+adult) | Lookbook | Character design sheets | Midjourney v7, SD ControlNet | Style-bible adherence | DirectorAgent |
| CastingAgent (#5) | Selects consented likeness + voice fit per character | Design sheets | Cast/likeness + consent chain | Likeness catalog, voice library | Fit + consent 100% | DirectorAgent, ComplianceAgent |
| AvatarDesignAgent (#47) | Locks synthetic-presenter identity, C2PA-signs each face | Cast refs | Identity hashes, signed refs | HeyGen/Synthesia, c2patool | Identity-hash consistency | ComplianceAgent, DeepfakeDetectionAgent |
| ProductionDesignAgent (#16) | Defines sets (classroom, shop, home, night street) and palette | Lookbook | Set/world look spec | Unreal scouting, Veo location gen | Palette coherence, period accuracy | DirectorAgent |
| CostumeDesignAgent (#17) | Wardrobe per age/role (student, carpenter, mother, office worker) | Design sheets | Wardrobe spec | Fashion-history DB, image-gen | Silhouette read, palette fit | MUAAgent |
| MUAAgent (#18) | Hair/makeup continuity incl. the lipstick beat (Scene 11) | Wardrobe | Continuity hashes per take | Face landmark, perceptual hash | Continuity break <0.5% | ContinuityAgent |
| StyleTransferAgent (#61) | Applies one consistent grade-able aesthetic across all shots | Refs, shots | Per-style LoRA, CLIP score | LoRA, CLIP/DINO, Runway style-lock | Style similarity ≥0.85 | DirectorAgent, ColoristAgent |
| ContinuityAgent (#98) | Tracks identity, wardrobe, props (cat motif), time-state across scenes | All shots | Continuity manifest | State manifests, shot-compare | State-drift detection | AIQAConsistencyAgent, GateKeeperAgent |

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
| Evaluation | [VBench](https://arxiv.org/abs/2311.17982) · [VBench appendix](https://arxiv.org/html/2507.07202) | 16 disentangled dimensions incl. subject co
…



### From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


**Build:**
- **Orchestration (53–58):** harden Orchestrator/Planner/Router/Judge/GateKeeper/Memory with full dispute-resolution (multi-agent debate), stage-gate sign-off, and escaped-defect=0 discipline.
- **Creative (59–65):** Ideation, NarrativeArc, StyleTransfer, MoodBoard, Novelty/Anti-Cliché, EmotionalArc, WorldBuilding — many delegate to GCA/Aesthetics (no duplication).
- **Research (66–72):** Web/Archive/Trend/Competitor/Citation/InterviewSynthesis/Benchmark — built on the M4 Research Agent core.
- **Optimization (73–80):** Prompt/Cost/Latency/Retention/ROAS/Accessibility optimizers + EvaluationHarness + SafetyRedTeam.
- **Full QC mesh**: complete L3 (AudienceSim ≥200 personas + HiTL sampling) and Q1–Q6 delivery validators; `GateKeeperAgent` enforces "zero leaked defects."

- **Prompt registry:** every agent system prompt is versioned (`prompt.vN.md`); the active version is referenced by `AgentConfig` and recorded in provenance (G5). Prompt changes go through PromptOptimizer (#73) eval before promotion.
- **Model registry:** pinned model+version per agent policy; upgrades are eval-gated (run golden L2/L3 before/after; no regression allowed).
- **Seed/LoRA/style registries:** StyleTransfer (#61) and gen agents reference versioned seeds/LoRAs/reference-frame banks for reproducibility and look-consistency.
- **Golden-set governance:** golden fixtures are frozen and reviewed; changing an expected output requires justification (it may indicate a rubric drift).
- **Aesthetic profiles:** consent-governed, versioned `AestheticProfile`s (per the Aesthetics Agent spec) stored and signed; audience-cohort profiles link to Psychological Recommendation.
- **Eval datasets:** VBench/EvalCrafter/MT-Bench/FVD/CLIP-T runners wrapped behind `EvalToolProvider`; benchmark baselines tracked over time by BenchmarkResearch (#72) + EvaluationHarness (#79).



### From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 59 | **IdeationAgent** | Divergent brainstorm of concepts, hooks, taglines | Cannes Grand Prix; D&AD; IDEO design-thinking; SCAMPER/de Bono | Idea-count; novelty (embedding distance); semantic diversity | Wins agency-pitch shootouts on concept density | CreativeDirectorAgent, NoveltyAgent | CopywriterAgent (derivative), DirectorAgent (unfilmable) | Embedding novelty scorer; concept clustering (UMAP); Are.na/Pinterest search | Self-Refine + NoveltyAgent as critic |
| 60 | **NarrativeArcAgent** | 3-act / Save-the-Cat / Hero's Journey structure | Campbell; Snyder *Save the Cat*; Truby; Black List analyses | Beat-sheet coverage 100%; turning-point spacing; arc curve fit | Beats WGA first drafts on structural rubric | ScreenwriterAgent, DirectorAgent | ScreenwriterAgent (sagging middle) | Beat-sheet validator; emotional-arc plotter; structure templates | Self-Refine (rubric: beat-sheet completeness) |
| 61 | **StyleTransferAgent** | Applies named aesthetic consistently across shots | Curated style corpora; LoRA/seed registries; reference-frame banks | Style-similarity (CLIP/DINO) ≥0.85; cross-shot variance ≤τ | Wins blind preference vs human colorist+grader | DirectorAgent, ColoristAgent | GeneratorAgent (off-style) | LoRA weights per style; CLIP/DINO similarity scorer; Runway style-lock mode; ComfyUI | Self-Refine (CLIP style score as feedback) |
| 62 | **WorldBuildingAgent** | Lore, rules, geography, factions, magic/tech systems | Tolkien; *Worldbuilding* (Adams); fan-wikis; series-bible leaks | Internal-consistency (no contradictions); rule-completeness | Lower contradiction rate than writers' bibles at 10× volume | ShowrunnerAgent, FactCheckerAgent | ScreenwriterAgent (lore break), ConceptArtistAgent | Long-context LLM (Gemini 2.5 Pro); contradiction-detection model; wiki-graph DB | Reflexion (contradiction corrections → episodic memory) |
| 63 | **MoodBoardAgent** | Reference boards: visual, sonic, tonal | Pinterest/Are.na; lookbook archives; Spotify-Canvas | Reference coherence (cluster tightness); brief alignment | Faster + tighter boards than art director (blind A/B) | DirectorAgent, ProductionDesignAgent | ConceptArtistAgent (off-mood) | Pinterest/Are.na APIs; Spotify Canvas; CLIP clustering; Figma board generation | ReAct (search → cluster → layout → validate coherence) |
| 64 | **NoveltyAgent / Anti-Cliché Critic** | Flags tropes, clichés, over-fit outputs | TV Tropes; OpenSubtitles n-gram freq; corpus-novelty embeddings | Cliché-hit count; novelty score vs category prior | Catches more clichés than experienced script editor | IdeationAgent, ScreenwriterAgent | ScreenwriterAgent (trope-stuffed), CopywriterAgent (templated) | TV Tropes scraper; n-gram frequency DB; embedding novelty scorer | LLM-as-Judge (anti-cliché constitution) |
| 65 | **EmotionalArcAgent** | Maps valence/arousal curve; suggests beats | Plutchik; affective-computing corpora; Cron *Story Genius* | Curve-fit to target; biosignal-proxy regression accuracy | Better retention prediction than NRG test-screening cards | DirectorAgent, EditorAgent, ComposerAgent | EditorAgent (flat middle), ComposerAgent (cue mismatch) | Sentiment/emotion classifiers (GoEmotions); retention-curve predictor; biosignal proxy model | Self-Refine (emotional-arc curve as rubric target) |

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



### From `corpus/study/ui/ui_design.md` Copy: `sources/excerpts/ui_design.md`.


Creative Meta-Agents                         S19: Creative Meta Panel
  IdeationAgent                                   Brainstorm cards
  NarrativeArcAgent                               Beat-sheet visualizer
  StyleTransferAgent                              Style-lock controls
  MoodBoardAgent                                  Mood board composer
  NoveltyAgent                                    Cliché warnings
  EmotionalArcAgent                               Emotion curve graph



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

- Master roster row va_id=61 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `C:\Project\va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.styletransfer · va_id=61 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **StyleTransferAgent** (`video.styletransfer`, va_id=61, category `9-Meta`).

### Responsibility focus
Applies named aesthetic consistently across shots

### Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: creative ideation agents, narrative arc modeling, style transfer video, emotional arc prediction, novelty metrics
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI creative meta-agents, story arc AI, style systems for video
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: AI creative direction, narrative design with LLMs, style bibles for generative video

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

<!-- migration_capability_research · video.styletransfer · v1 · 2026-07-13 -->
