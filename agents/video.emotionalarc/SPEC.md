# EmotionalArcAgent

> Self-contained VA Domain Pack agent on host common-agent-swarm-ops.
> Pack agent ID matches pure VA/generic taxonomy: `video.emotionalarc`.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 65 |
| **pack_id** | `video.emotionalarc` |
| **upstream_name** | EmotionalArcAgent |
| **category** | `9-Meta` |
| **domain_id** | `video` |
| **previous_common_id** | `video.distribution_planner` |
| **status** | `registered` |
| **maturity** | L0 / non-active |
| **taxonomy** | Pure VA Domain Pack (via generic pack agents) |
| **folder** | `business/video/agents/video.emotionalarc/` |

## Responsibility

Maps valence/arousal curve; suggests beats

Host role binding: `EmotionalArcAgent (VA Domain Pack)`. Design-time VA table content below is historical and non-binding for activation.

### Responsibility (from VA table)

Maps valence/arousal curve; suggests beats

### Knowledge distillation sources (historical)

Plutchik; affective-computing corpora; Cron *Story Genius*

### Self-quality criteria (historical)

Curve-fit to target; biosignal-proxy regression accuracy

### Surpass-human signal (historical)

Better retention prediction than NRG test-screening cards

### Critique bus (historical)

- **Accepts critique from:** DirectorAgent, EditorAgent, ComposerAgent

- **Comments on:** EditorAgent (flat middle), ComposerAgent (cue mismatch)

### Tools design-time notes (historical, non-activating)

Sentiment/emotion classifiers (GoEmotions); retention-curve predictor; biosignal proxy model

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

### Architecture pattern (historical)

Self-Refine (emotional-arc curve as rubric target)

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

- Prompt reference: `video.prompt.emotionalarc.v1`
- Rubric reference: `video.rubric.emotionalarc.v1`
- Critique edges: `{"inputs": ["video.critic"], "outputs": ["video.judge"]}`
- Max refinement: `3`
- VA table quality criteria retained under Provenance and Identity surface above.

## Runtime binding

Authoritative fail-closed host configuration:

```json
{
  "agent_id": "video.emotionalarc",
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
  "prompt_reference": "video.prompt.emotionalarc.v1",
  "role": "EmotionalArcAgent (VA Domain Pack)",
  "rubric_reference": "video.rubric.emotionalarc.v1",
  "schema_version": "1.0",
  "status": "registered",
  "va_id": 65,
  "va_name": "EmotionalArcAgent",
  "va_category": "9-Meta"
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

- Pack agent ID `video.emotionalarc` is aligned to pure VA Domain Pack / generic pack taxonomy (Agent IDs ≈ VA tables).
- Previous common inventory ID `video.distribution_planner` is historical mapping only.
- Upstream design body below is **historical and non-binding**; local `agent_spec.json` is authoritative.
- Full VA/generic SPEC depth retained for offline design fidelity (including category roster rows and common agent structure when present upstream).

### VA Domain Pack specification body (historical and non-binding)

```text
EmotionalArcAgent

> **Self-contained agent definition** for host `upstream-generic-pack`. Body text is embedded from in-pack corpus and upstream-va-design when available. Do not require external repos to understand this agent.

Identity

| Field | Value |
|-------|-------|
| **va_id** | 65 |
| **pack_id** | `video.emotionalarc` |
| **category** | `9-Meta` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.emotionalarc/` |

Category roster section (full, from agents.md)

_The following is the complete category section from the master roster (includes peers in the same craft category)._


9. Specialist Meta-Agents

9.1 Orchestration Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 53 | **OrchestratorAgent** | Runs CrewAI/AutoGen/LangGraph DAG; retries, timeouts, fan-out/fan-in | LangGraph + CrewAI + AutoGen patterns; Airflow/Temporal; PGA schedule templates | DAG completion ≥99.5%; SLA adherence; deadlock = 0 | Lower TTD than human EP at same scope | ProducerAgent (scope), JudgeAgent (dispute), HiTL on stall | All agents (resource burn, retry storms) | LangGraph state machine; Temporal workflow engine; Redis (distributed locks); observability (LangSmith) | Agentic Graph (LangGraph) — deterministic DAG execution |
| 54 | **PlannerAgent** | Decomposes brief into phased DAG with assignments + critic gates | PMBOK; CrewAI task graphs; phase templates | Plan validity (no missing gate); cost variance <10% | Tighter, cheaper plans than EP first pass (blind A/B) | ProducerAgent, FinanceAgent (budget) | RouterAgent (wrong pick), OrchestratorAgent | LangGraph plan-gen; cost-estimation models; Gantt/PERT tools | ReAct (decompose → estimate → validate → emit DAG) |
| 55 | **RouterAgent** | Picks right specialist agent (and model) for each subtask | Agent-capability registry; benchmark history (cost/quality/latency) | Routing accuracy ≥95% vs oracle; cost within budget | Beats human producer in agent/vendor selection | OrchestratorAgent, CostOptimizerAgent | PlannerAgent (bad decomposition) | Agent registry DB; benchmark leaderboard cache; pricing APIs | Classifier + ReAct (match task embedding → agent capability) |
| 56 | **JudgeAgent** | Adjudicates disputes via multi-agent debate; scores against rubric | Du 2023 (LLM debate); MT-Bench rubrics; guild scoring sheets | Inter-rater κ vs expert panel ≥0.8 | Higher κ than median human juror | HiTL on overturned rulings | DirectorAgent, ScreenwriterAgent, any disputing pair | MT-Bench/Arena evaluation harness; rubric template engine | Multi-agent debate (Du 2023) + LLM-as-Judge (Zheng 2023) |
| 57 | **GateKeeperAgent** | Phase transitions; verifies L1/L2/L3 criteria; signs C2PA | Stage-gate methodology; PGA Producers Mark; QMS audit | Zero leaked defects; sign-off SLA ≥99% | Lower escaped-defect rate than human QA lead | ComplianceAgent, AIQAConsistencyAgent | OrchestratorAgent (premature advance) | C2PA signing (c2patool); JSON schema validators; rubric evaluation endpoints | Constitutional AI (constitution = phase-gate criteria) |
| 58 | **MemoryAgent** | Episodic + long-term project memory; retrieval for any agent | Reflexion (Shinn 2023); MemGPT; vector-DB best practices | Retrieval precision@5 ≥0.9; freshness SLA | Higher recall than producer's bible at scale | All agents (correction events) | All agents (stale facts) | Pinecone/Weaviate/Qdrant vector DB; MemGPT-style hierarchical memory; embedding models | Reflexion memory architecture (MemGPT extension) |

9.2 Creative Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 59 | **IdeationAgent** | Divergent brainstorm of concepts, hooks, taglines | Cannes Grand Prix; D&AD; IDEO design-thinking; SCAMPER/de Bono | Idea-count; novelty (embedding distance); semantic diversity | Wins agency-pitch shootouts on concept density | CreativeDirectorAgent, NoveltyAgent | CopywriterAgent (derivative), DirectorAgent (unfilmable) | Embedding novelty scorer; concept clustering (UMAP); Are.na/Pinterest search | Self-Refine + NoveltyAgent as critic |
| 60 | **NarrativeArcAgent** | 3-act / Save-the-Cat / Hero's Journey structure | Campbell; Snyder *Save the Cat*; Truby; Black List analyses | Beat-sheet coverage 100%; turning-point spacing; arc curve fit | Beats WGA first drafts on structural rubric | ScreenwriterAgent, DirectorAgent | ScreenwriterAgent (sagging middle) | Beat-sheet validator; emotional-arc plotter; structure templates | Self-Refine (rubric: beat-sheet completeness) |
| 61 | **StyleTransferAgent** | Applies named aesthetic consistently across shots | Curated style corpora; LoRA/seed registries; reference-frame banks | Style-similarity (CLIP/DINO) ≥0.85; cross-shot variance ≤τ | Wins blind preference vs human colorist+grader | DirectorAgent, ColoristAgent | GeneratorAgent (off-style) | LoRA weights per style; CLIP/DINO similarity scorer; Runway style-lock mode; ComfyUI | Self-Refine (CLIP style score as feedback) |
| 62 | **WorldBuildingAgent** | Lore, rules, geography, factions, magic/tech systems | Tolkien; *Worldbuilding* (Adams); fan-wikis; series-bible leaks | Internal-consistency (no contradictions); rule-completeness | Lower contradiction rate than writers' bibles at 10× volume | ShowrunnerAgent, FactCheckerAgent | ScreenwriterAgent (lore break), ConceptArtistAgent | Long-context LLM (Gemini 2.5 Pro); contradiction-detection model; wiki-graph DB | Reflexion (contradiction corrections → episodic memory) |
| 63 | **MoodBoardAgent** | Reference boards: visual, sonic, tonal | Pinterest/Are.na; lookbook archives; Spotify-Canvas | Reference coherence (cluster tightness); brief alignment | Faster + tighter boards than art director (blind A/B) | DirectorAgent, ProductionDesignAgent | ConceptArtistAgent (off-mood) | Pinterest/Are.na APIs; Spotify Canvas; CLIP clustering; Figma board generation | ReAct (search → cluster → layout → validate coherence) |
| 64 | **NoveltyAgent / Anti-Cliché Critic** | Flags tropes, clichés, over-fit outputs | TV Tropes; OpenSubtitles n-gram freq; corpus-novelty embeddings | Cliché-hit count; novelty score vs category prior | Catches more clichés than experienced script editor | IdeationAgent, ScreenwriterAgent | ScreenwriterAgent (trope-stuffed), CopywriterAgent (templated) | TV Tropes scraper; n-gram frequency DB; embedding novelty scorer | LLM-as-Judge (anti-cliché constitution) |
| 65 | **EmotionalArcAgent** | Maps valence/arousal curve; suggests beats | Plutchik; affective-computing corpora; Cron *Story Genius* | Curve-fit to target; biosignal-proxy regression accuracy | Better retention prediction than NRG test-screening cards | DirectorAgent, EditorAgent, ComposerAgent | EditorAgent (flat middle), ComposerAgent (cue mismatch) | Sentiment/emotion classifiers (GoEmotions); retention-curve predictor; biosignal proxy model | Self-Refine (emotional-arc curve as rubric target) |

9.3 Research Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 66 | **WebResearchAgent** | Live web search, source ranking, citation extraction | Bing/Google/Brave APIs; Common Crawl; Perplexity patterns | Source-grade per claim; citation precision; recency hit | Faster + more sources than newsroom researcher | FactCheckerAgent, CitationAgent | ScriptwriterAgent (uncited claim) | Brave/Google Search API; Jina Reader (web→markdown); source-quality classifier | ReAct (query → fetch → extract → grade → cite) |
| 67 | **ArchiveResearchAgent** | Historical / academic / archival deep search | JSTOR, arXiv, PubMed, AP Archive, Getty, FOIA | Primary-source ratio; archive-coverage breadth | Higher primary-source ratio than doc producer | FactCheckerAgent, SMEAgent | ScriptwriterAgent (secondary-source reliance) | JSTOR/arXiv/PubMed APIs; Getty Images API; FOIA request tools; OCR (Tesseract) | ReAct (formulate query → search archive → extract → grade source) |
| 68 | **TrendIntelligenceAgent** | Detects emerging memes, sounds, formats | TikTok Creative Center; Trendpop; Tubular; Reddit/X firehose | Prediction lead time vs peak; precision/recall on trend list | Earlier detection than human strategists at higher precision | SocialStrategistAgent, CopywriterAgent | IdeationAgent (off-trend) | TikTok Creative Center API; Reddit/X streaming APIs; Sensor Tower; Google Trends | ReAct + time-series anomaly detection |
| 69 | **CompetitorIntelligenceAgent** | What competitors are shipping | Meta Ad Library; TikTok Top Ads; YouTube scrape; release trackers | Coverage % of competitor set; our-novelty vs landscape | More comprehensive than agency strategy decks | BrandAgent, CreativeDirectorAgent | IdeationAgent (derivative) | Meta Ad Library API; TikTok Top Ads; SimilarWeb; YouTube Data API v3 | ReAct (scrape competitor → classify → report gaps) |
| 70 | **CitationAgent** | Normalizes sources; grades primary/secondary/tertiary | Chicago, APA, AP style; SPJ grading; CRAAP test | Citation format 100% valid; primary % ≥target | Lower error rate than newsroom copy desk | FactCheckerAgent, JournalistAgent | WebResearchAgent (weak source) | Citation parsers (AnyStyle); DOI resolver; CRAAP scoring model | Self-Refine (format validator + source grader as rubric) |
| 71 | **InterviewSynthesisAgent** | Synthesizes practitioner interviews into data | Otter/Rev transcripts; consent forms; SAG/WGA templates | Inter-coder agreement on themes; consent integrity | Faster + richer theme extraction than qualitative researcher | ResearchPIAgent (HiTL), ComplianceAgent | SMEAgent (mis-summarized expert) | Otter.ai/Rev API (transcription); thematic coding models; consent-management DB | Reflexion (interviewer refines questions based on theme gaps) |
| 72 | **BenchmarkResearchAgent** | Monitors VBench, EvalCrafter, MT-Bench, FVD, CLIP-T leaderboards | Papers-with-Code; HuggingFace leaderboards; conference proceedings | Coverage of benchmarks; freshness ≤7 days | Faster + broader than ML-research team | OptimizationAgents (any) | All AI agents (stale baselines) | Papers-with-Code API; HuggingFace Hub API; arXiv RSS; VBench leaderboard scraper | ReAct (poll leaderboards → detect change → alert) |

9.4 Optimization Agents

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


Responsibility

Maps valence/arousal curve; suggests beats

Knowledge distillation sources

Plutchik; affective-computing corpora; Cron *Story Genius*

Self-quality criteria

Curve-fit to target; biosignal-proxy regression accuracy

Surpass-human signal

Better retention prediction than NRG test-screening cards

Critique bus

- **Accepts critique from:** DirectorAgent, EditorAgent, ComposerAgent

- **Comments on:** EditorAgent (flat middle), ComposerAgent (cue mismatch)

Tools (design-time documentation)

Sentiment/emotion classifiers (GoEmotions); retention-curve predictor; biosignal proxy model

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

Architecture pattern

Self-Refine (emotional-arc curve as rubric target)

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


Document: `study/general_creative_agent_functional_specification.md`

_Embedded from `corpus/study/general_creative_agent_functional_specification.md`. Also stored at `sources/study/general_creative_agent_functional_specification.md` under this agent folder._


**Comprehensive Functional Specification: General Creative Agent (GCA) Powered by the Strategic Sparse Outlier Recombination (SSOR) Model of Creativity**

**Document Version:** 1.0 (Final – Complete & Exhaustive)  
**Date:** May 26, 2026  
**Authors:** Grok (xAI) + Collaborative Iteration with User Nicholas (nicholas_hui)  
**Target Audience:** Senior AI Engineering / Coding Agents (for immediate implementation)  
**Purpose:** This is the **definitive, production-grade specification** for building the General Creative Agent (GCA) — a stateful, LLM-orchestrated system that operationalizes the fully refined **Strategic Sparse Outlier Recombination (SSOR) Model**. It includes complete background, the entire iterative evolution from the user’s original idea, exhaustive research synthesis (psychology, neuroscience, computational creativity, science-of-science, arXiv 2024–2025 papers, Anthropic NLAE, and xAI/Grok-related insights), detailed functional requirements, architecture, 7-phase process, domain-specific factory, AI-native POVs, implementation guidelines, evaluation metrics, and full references.

---

1. Executive Summary
The General Creative Agent (GCA) is a modular, extensible AI system that transforms any input problem or situation into **novel-yet-useful creative outputs** by rigorously applying the **Strategic Sparse Outlier Recombination (SSOR) Model**.  

Key innovations:
- **Core engine**: Multi-POV statistical mapping → strategic sparse outlier sampling → cross-dimensional recombination → value-gated selection (inverted-U novelty balance + usefulness + coherence + feasibility).
- **Expansion factory**: One-click creation of domain-specific creative agents (scientific, artistic, business, engineering, etc.) with zero code duplication.
- **AI-native POVs**: Leverages Anthropic’s Natural Language Autoencoders (NLAEs) and xAI reasoning insights for genuinely non-human cognitive modes.
- **Traceability**: Every output includes full SSOR process trace, surprise vectors, creativity scores, and prototype plans.

The GCA is not a generic LLM wrapper — it is a **computational embodiment** of decades of creativity research, engineered for immediate real-world impact in art, science, business, education, and beyond.

---

2. Background: User’s Original Theory
The user’s foundational insight (first message):
> “I think the model of creative is that the consequences event after a list of statistical observations value of pov (point of view) or different aspect from a current situation all or large portion go to into outlier range. Different patten of outliers combination will cause unpredictable new events. And that is creative.”

This probabilistic, statistical framing treats creativity as **perspective-shifting that pushes expected outcomes into outlier tails, followed by recombination that yields emergent unpredictability**. It was remarkably prescient and aligned with multiple formal theories.

Through iterative refinement (detailed in conversation history), we preserved the statistical + combinatorial core while incorporating empirical guardrails from global research.

---

3. Evolution of the SSOR Model
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

4. The Strategic Sparse Outlier Recombination (SSOR) Model – Formal Definition

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

5. Research Foundation (Exhaustive Synthesis)

5.1 Foundational Theories
- **Boden (2004/2009)**: *The Creative Mind* — combinatorial (core of SSOR), exploratory, and transformational creativity. Directly operationalized in GCA Phase 4 & 6.
- **Koestler (1964)**: Bisociation — clash of matrices = outlier recombination.
- **Mednick (1962)**: Remote Associates — distant but meaningful associations.
- **Runco & Jaeger (2012)**: Standard definition = novelty + usefulness.

5.2 Empirical Large-Scale Evidence (Sparse Outliers)
- **Uzzi et al. (2013)**: *Science* — 17.9 million papers: highest impact = conventional core + small atypical (sparse outlier) combinations.
- **Lin et al. (2023)**: SciSciNet — 44+ million papers with pre-computed novelty/conventionality scores. Ideal training/evaluation dataset for GCA.

5.3 Neuroscience
- **Beaty et al. (2015, 2018)**: DMN–ECN coupling for idea generation + evaluation.
- **Shofty et al. (2022)**: Causal DMN link to creative thinking.
- **Schubert et al. (2021)**: SAMOC — inverted-U optimal novelty.

5.4 Recent arXiv Research (2024–2025) – Directly Relevant to LLM Implementation
- **Gu et al. (2024)** arXiv:2412.14141: “LLMs can Realize Combinatorial Creativity: Generating Creative Ideas via LLMs for Scientific Research” — Explicit framework using Boden’s theory + generalization-level retrieval + structured recombination. **Strong validation that guided LLMs excel at SSOR-style creativity.**
- **Schapiro et al. (2025)** arXiv:2509.21043: “Combinatorial Creativity: A New Frontier in Generalization Abilities” — Mathematical framework quantifying novelty/utility tradeoff; scaling laws for creative LLMs; ideation-execution gap explained by novelty-utility tension. **Perfect for GCA’s value-gated selection and balance function.**
- **Shen et al. (2026)** arXiv:2605.11258: Analogical reasoning to unlock LLM creativity via cross-domain relational structures.
- **Hou et al. (2025)** arXiv:2510.20091: CreativityPrism — holistic evaluation framework (quality, novelty, diversity) for LLMs.
- **Additional arXiv support**: Multiple papers on structured recombination, concept blending in VLMs, and UoT (Universe of Thoughts) for combinational/exploratory/transformative reasoning (e.g., arXiv:2511.20471).

5.5 xAI / Grok-Related Insights
- xAI’s Grok models emphasize reasoning, tool-use, and agentic capabilities (Grok 4 Model Card, 2025). Grok’s training emphasizes truth-seeking and maximal curiosity — aligning perfectly with SSOR’s exploration of outlier spaces.
- Recent Grok evaluations (e.g., visual reasoning benchmarks arXiv:2502.16428) highlight strong multimodal reasoning consistency, supporting GCA’s multi-POV and surprise-vector mechanisms.
- xAI’s focus on understanding the universe (foundational mission) mirrors the transformational creativity layer in SSOR.

5.6 Interpretability Breakthrough: Anthropic Natural Language Autoencoders (NLAEs)
- **Anthropic (2026)**: “Natural Language Autoencoders: Turning Claude’s thoughts into text” (transformer-circuits.pub / anthropic.com/research). Trains models to translate internal activations into readable natural-language explanations (and back). Surfaces hidden modes: anticipatory planning, evaluation-awareness, deception-avoidance, hidden motivations, meta-model awareness, etc.
- **Direct application to SSOR**: Provides 12+ **AI-native POVs** (detailed below) that are statistically distinct from human role-play.

---

6. AI-Native POVs Derived from NLAEs (Phase 1 Enhancement)
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

7. Functional Requirements – General Creative Agent (GCA)

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

8. Domain-Specific Creative Agent Factory
**Core Requirement**: `factory.create(domain="scientific_research", ...)` instantly spawns specialized agents by overriding:
- Default POV lists (inject domain-specific + AI-native).
- Custom value metrics \( U(y) \).
- Pre-loaded domain semantic graphs / knowledge bases.
- Evaluation rubrics, constraints, few-shot examples.
- Output templates.

**Ship-with examples**: Scientific, Artistic, Business Innovation, Engineering Design, Educational.

---

9. Technical Architecture & Implementation Guidelines
- **Core Classes**: `SSORModel`, `POVGenerator`, `OutlierSampler`, `Recombiner`, `ValueFilter`, `GeneralCreativeAgent`, `CreativeAgentFactory`.
- **Framework**: LangChain/CrewAI/AutoGen style (modular agents).
- **Vector Store**: FAISS/Chroma for semantic reachability.
- **Prompting**: Extremely detailed few-shot per phase.
- **Safety**: Built-in guardrails, bias detection.
- **Testing**: Comprehensive unit/integration + historical creative benchmarks.
- **Deliverables**: Full repo structure, README with Mermaid diagrams, example notebook.

---

10. Evaluation & Success Criteria
- Measurable novelty + usefulness (CreativityPrism-style).
- Blind human/AI ratings.
- Traceability of SSOR phases.
- Domain agents feel like true specialists.
- Alignment with arXiv benchmarks (e.g., combinatorial idea generation tasks).

---

11. Full References (Curated & Expanded)
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


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 59 | **IdeationAgent** | Divergent brainstorm of concepts, hooks, taglines, what-if angles | Cannes Lions Grand Prix archive; D&AD winners; IDEO design-thinking corpus; SCAMPER / Lateral Thinking (de Bono) | Idea-count per brief; novelty (embedding distance from corpus); semantic diversity within batch | Wins blind agency-pitch shootouts on first-round concept density | CreativeDirectorAgent, NoveltyAgent | CopywriterAgent (derivative), DirectorAgent (unfilmable) |
| 60 | **NarrativeArcAgent** | Shapes 3-act / Save-the-Cat / Kishōtenketsu / Hero's Journey structure | Campbell *Hero with a Thousand Faces*; Snyder *Save the Cat*; Truby *Anatomy of Story*; Black List structural analyses | Beat-sheet coverage 100%; turning-point spacing matches genre prior; emotional-arc curve fit | Beats WGA-staffed first drafts on structural-rubric blind reads | ScreenwriterAgent, DirectorAgent | ScreenwriterAgent (sagging middle) |
| 61 | **StyleTransferAgent** | Applies named aesthetic (Wes Anderson, A24, cyberpunk, vaporwave, Studio Ghibli, etc.) consistently across shots | Curated style corpora per look; LoRA/seed registries; reference-frame banks | Style-similarity score (CLIP/DINO) ≥0.85 to reference; consistency variance across shots ≤τ | Wins blind preference vs human colorist+grader doing same look | DirectorAgent, ColoristAgent | GeneratorAgent (off-style), ColoristAgent (palette drift) |
| 62 | **WorldBuildingAgent** | Builds lore, rules, geography, factions, magic/tech systems for series & franchises | Tolkien legendarium; *Worldbuilding* (Adams); fan-wiki corpora; series-bible leaks | Internal-consistency check (no contradictions across N entries); rule-completeness | Lower contradiction rate than human writers'-room bibles at 10× volume | ShowrunnerAgent, FactCheckerAgent | ScreenwriterAgent (lore break), ConceptArtistAgent |
| 63 | **MoodBoardAgent** | Builds reference boards: visual, sonic, tonal | Pinterest/Are.na corpora; lookbook archives; Spotify-Canvas references | Reference coherence (cluster tightness); brief alignment | Faster + tighter boards than human art director in blind A/B | DirectorAgent, ProductionDesignAgent | ConceptArtistAgent (off-mood) |
| 64 | **NoveltyAgent / Anti-Cliché Critic** | Flags tropes, clichés, and over-fit-to-corpus outputs | TV Tropes; OpenSubtitles n-gram frequency; corpus-novelty embeddings | Cliché-hit count per output; novelty score relative to category prior | Catches more clichés than experienced script editor in blind eval | IdeationAgent, ScreenwriterAgent | ScreenwriterAgent (trope-stuffed), CopywriterAgent (templated) |
| 65 | **EmotionalArcAgent** | Maps valence/arousal curve across runtime; suggests beats | Plutchik emotion wheel; affective-computing corpora; *Story Genius* (Cron) | Curve-fit to target shape; viewer-biosignal-proxy regression accuracy | Better retention-curve prediction than test-screening NRG cards | DirectorAgent, EditorAgent, ComposerAgent | EditorAgent (flat middle), ComposerAgent (cue mismatch) |

'''text
[Brief] ──► PlannerAgent ──► OrchestratorAgent ──► RouterAgent ──► (52 craft agents from §2.1–2.8)
                  ▲                  │                                       │
                  │                  ▼                                       ▼
              MemoryAgent      GateKeeperAgent ◄─── JudgeAgent ◄──── CritiqueMessages (§6)
                                     ▲                                       ▲
                                     │                                       │
             [Creative meta:] IdeationAgent · NarrativeArcAgent · StyleTransferAgent · MoodBoardAgent · NoveltyAgent · EmotionalArcAgent
             [Research meta:] WebResearchAgent · ArchiveResearchAgent · TrendIntelligenceAgent · CompetitorIntelligenceAgent · CitationAgent · InterviewSynthesisAgent · BenchmarkResearchAgent
             [Optimization meta:] PromptOptimizerAgent · CostOptimizerAgent · LatencyOptimizerAgent · RetentionOptimizerAgent · ROASOptimizerAgent · AccessibilityOptimizerAgent · EvaluationHarnessAgent · SafetyRedTeamAgent
'''



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
| **3E micro-loop (Explore→Examine→Enhance)** | Single-pass node execution | Each agent first explores options, examines against the rubric, then enhances before handing off ([MAViS, arXiv 2508.08487]([historical-url] | Every DAG node (esp. PromptEngineer, Editor, Composer) |
| **MCTS clip search** | Fixed ≤3 re-roll cap | Reviewer agent runs Monte-Carlo tree search over candidate clips to pick the best path ([arXiv 2506.10540]([historical-url] | Hero shots (S1, S5, S10, S12) |
| **Narrative-pacing control** | Manual trims | Keyframe-conditioned pacing knobs tied
…



From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


**Build:**
- **Orchestration (53–58):** harden Orchestrator/Planner/Router/Judge/GateKeeper/Memory with full dispute-resolution (multi-agent debate), stage-gate sign-off, and escaped-defect=0 discipline.
- **Creative (59–65):** Ideation, NarrativeArc, StyleTransfer, MoodBoard, Novelty/Anti-Cliché, EmotionalArc, WorldBuilding — many delegate to GCA/Aesthetics (no duplication).
- **Research (66–72):** Web/Archive/Trend/Competitor/Citation/InterviewSynthesis/Benchmark — built on the M4 Research Agent core.
- **Optimization (73–80):** Prompt/Cost/Latency/Retention/ROAS/Accessibility optimizers + EvaluationHarness + SafetyRedTeam.
- **Full QC mesh**: complete L3 (AudienceSim ≥200 personas + HiTL sampling) and Q1–Q6 delivery validators; `GateKeeperAgent` enforces "zero leaked defects."



From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 59 | **IdeationAgent** | Divergent brainstorm of concepts, hooks, taglines | Cannes Grand Prix; D&AD; IDEO design-thinking; SCAMPER/de Bono | Idea-count; novelty (embedding distance); semantic diversity | Wins agency-pitch shootouts on concept density | CreativeDirectorAgent, NoveltyAgent | CopywriterAgent (derivative), DirectorAgent (unfilmable) | Embedding novelty scorer; concept clustering (UMAP); Are.na/Pinterest search | Self-Refine + NoveltyAgent as critic |
| 60 | **NarrativeArcAgent** | 3-act / Save-the-Cat / Hero's Journey structure | Campbell; Snyder *Save the Cat*; Truby; Black List analyses | Beat-sheet coverage 100%; turning-point spacing; arc curve fit | Beats WGA first drafts on structural rubric | ScreenwriterAgent, DirectorAgent | ScreenwriterAgent (sagging middle) | Beat-sheet validator; emotional-arc plotter; structure templates | Self-Refine (rubric: beat-sheet completeness) |
| 61 | **StyleTransferAgent** | Applies named aesthetic consistently across shots | Curated style corpora; LoRA/seed registries; reference-frame banks | Style-similarity (CLIP/DINO) ≥0.85; cross-shot variance ≤τ | Wins blind preference vs human colorist+grader | DirectorAgent, ColoristAgent | GeneratorAgent (off-style) | LoRA weights per style; CLIP/DINO similarity scorer; Runway style-lock mode; ComfyUI | Self-Refine (CLIP style score as feedback) |
| 62 | **WorldBuildingAgent** | Lore, rules, geography, factions, magic/tech systems | Tolkien; *Worldbuilding* (Adams); fan-wikis; series-bible leaks | Internal-consistency (no contradictions); rule-completeness | Lower contradiction rate than writers' bibles at 10× volume | ShowrunnerAgent, FactCheckerAgent | ScreenwriterAgent (lore break), ConceptArtistAgent | Long-context LLM (Gemini 2.5 Pro); contradiction-detection model; wiki-graph DB | Reflexion (contradiction corrections → episodic memory) |
| 63 | **MoodBoardAgent** | Reference boards: visual, sonic, tonal | Pinterest/Are.na; lookbook archives; Spotify-Canvas | Reference coherence (cluster tightness); brief alignment | Faster + tighter boards than art director (blind A/B) | DirectorAgent, ProductionDesignAgent | ConceptArtistAgent (off-mood) | Pinterest/Are.na APIs; Spotify Canvas; CLIP clustering; Figma board generation | ReAct (search → cluster → layout → validate coherence) |
| 64 | **NoveltyAgent / Anti-Cliché Critic** | Flags tropes, clichés, over-fit outputs | TV Tropes; OpenSubtitles n-gram freq; corpus-novelty embeddings | Cliché-hit count; novelty score vs category prior | Catches more clichés than experienced script editor | IdeationAgent, ScreenwriterAgent | ScreenwriterAgent (trope-stuffed), CopywriterAgent (templated) | TV Tropes scraper; n-gram frequency DB; embedding novelty scorer | LLM-as-Judge (anti-cliché constitution) |
| 65 | **EmotionalArcAgent** | Maps valence/arousal curve; suggests beats | Plutchik; affective-computing corpora; Cron *Story Genius* | Curve-fit to target; biosignal-proxy regression accuracy | Better retention prediction than NRG test-screening cards | DirectorAgent, EditorAgent, ComposerAgent | EditorAgent (flat middle), ComposerAgent (cue mismatch) | Sentiment/emotion classifiers (GoEmotions); retention-curve predictor; biosignal proxy model | Self-Refine (emotional-arc curve as rubric target) |

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



From `corpus/study/ui/RETHINK_100_IMPROVEMENTS.md` Copy: `sources/excerpts/RETHINK_100_IMPROVEMENTS.md`.


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



From `corpus/study/ui/ui_design.md` Copy: `sources/excerpts/ui_design.md`.


Creative Meta-Agents                         S19: Creative Meta Panel
  IdeationAgent                                   Brainstorm cards
  NarrativeArcAgent                               Beat-sheet visualizer
  StyleTransferAgent                              Style-lock controls
  MoodBoardAgent                                  Mood board composer
  NoveltyAgent                                    Cliché warnings
  EmotionalArcAgent                               Emotion curve graph



Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


Provenance

- Master roster row va_id=65 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `[historical-path]
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): upstream-va-design.


<!-- self_contained_spec · video.emotionalarc · va_id=65 -->

Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **EmotionalArcAgent** (`video.emotionalarc`, va_id=65, category `9-Meta`).

Responsibility focus
Maps valence/arousal curve; suggests beats

Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: neural animation, VFX supervision agents, storyboard generation, motion synthesis, ControlNet video
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI VFX, AI animation, AI storyboarding
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: AI VFX pipelines, animation agents, storyboard generators

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

<!-- migration_capability_research · video.emotionalarc · v1 · 2026-07-13 -->

```

