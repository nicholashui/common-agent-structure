# video.competitorintelligence — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/video.competitorintelligence/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "video.competitorintelligence",
  "status": "registered",
  "role": "CompetitorIntelligenceAgent (VA Domain Pack)",
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
      "video.brand",
      "video.creativedirector"
    ],
    "outputs": [
      "video.judge",
      "video.ideation"
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
  "va_id": 69,
  "va_name": "CompetitorIntelligenceAgent",
  "va_category": "9-Meta",
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

# CompetitorIntelligenceAgent

> Self-contained VA Domain Pack agent on host common-agent-swarm-ops.
> Pack agent ID matches pure VA/generic taxonomy: `video.competitorintelligence`.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 69 |
| **pack_id** | `video.competitorintelligence` |
| **upstream_name** | CompetitorIntelligenceAgent |
| **category** | `9-Meta` |
| **domain_id** | `video` |
| **previous_common_id** | `video.audio_qc_reviewer` |
| **status** | `registered` |
| **maturity** | L0 / non-active |
| **taxonomy** | Pure VA Domain Pack (via generic pack agents) |
| **folder** | `business/video/agents/video.competitorintelligence/` |

## Responsibility

What competitors are shipping

Host role binding: `CompetitorIntelligenceAgent (VA Domain Pack)`. Design-time VA table content below is historical and non-binding for activation.

### Responsibility (from VA table)

What competitors are shipping

### Knowledge distillation sources (historical)

Meta Ad Library; TikTok Top Ads; YouTube scrape; release trackers

### Self-quality criteria (historical)

Coverage % of competitor set; our-novelty vs landscape

### Surpass-human signal (historical)

More comprehensive than agency strategy decks

### Critique bus (historical)

- **Accepts critique from:** BrandAgent, CreativeDirectorAgent

- **Comments on:** IdeationAgent (derivative)

### Tools design-time notes (historical, non-activating)

Meta Ad Library API; TikTok Top Ads; SimilarWeb; YouTube Data API v3

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

### Architecture pattern (historical)

ReAct (scrape competitor → classify → report gaps)

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

- Prompt reference: `video.prompt.competitorintelligence.v1`
- Rubric reference: `video.rubric.competitorintelligence.v1`
- Critique edges: `{"inputs": ["video.critic"], "outputs": ["video.judge"]}`
- Max refinement: `3`
- VA table quality criteria retained under Provenance and Identity surface above.

## Runtime binding

Authoritative fail-closed host configuration:

```json
{
  "agent_id": "video.competitorintelligence",
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
  "prompt_reference": "video.prompt.competitorintelligence.v1",
  "role": "CompetitorIntelligenceAgent (VA Domain Pack)",
  "rubric_reference": "video.rubric.competitorintelligence.v1",
  "schema_version": "1.0",
  "status": "registered",
  "va_id": 69,
  "va_name": "CompetitorIntelligenceAgent",
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

- Pack agent ID `video.competitorintelligence` is aligned to pure VA Domain Pack / generic pack taxonomy (Agent IDs ≈ VA tables).
- Previous common inventory ID `video.audio_qc_reviewer` is historical mapping only.
- Upstream design body below is **historical and non-binding**; local `agent_spec.json` is authoritative.
- Full VA/generic SPEC depth retained for offline design fidelity (including category roster rows and common agent structure when present upstream).

### VA Domain Pack specification body (historical and non-binding)

```text
CompetitorIntelligenceAgent

> **Self-contained agent definition** for host `upstream-generic-pack`. Body text is embedded from in-pack corpus and upstream-va-design when available. Do not require external repos to understand this agent.

Identity

| Field | Value |
|-------|-------|
| **va_id** | 69 |
| **pack_id** | `video.competitorintelligence` |
| **category** | `9-Meta` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.competitorintelligence/` |

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

What competitors are shipping

Knowledge distillation sources

Meta Ad Library; TikTok Top Ads; YouTube scrape; release trackers

Self-quality criteria

Coverage % of competitor set; our-novelty vs landscape

Surpass-human signal

More comprehensive than agency strategy decks

Critique bus

- **Accepts critique from:** BrandAgent, CreativeDirectorAgent

- **Comments on:** IdeationAgent (derivative)

Tools (design-time documentation)

Meta Ad Library API; TikTok Top Ads; SimilarWeb; YouTube Data API v3

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

Architecture pattern

ReAct (scrape competitor → classify → report gaps)

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


Document: `study/research_agent_functional_specification.md`

_Embedded from `corpus/study/research_agent_functional_specification.md`. Also stored at `sources/study/research_agent_functional_specification.md` under this agent folder._


Research Agent Functional Specification

1. Document Control

- Document title: `Research Agent Functional Specification`
- System name: `grok-research-agent`
- Document type: Current-state functional specification derived from implementation and tests
- Primary delivery model: Local Python CLI application
- Source of truth for this specification: `grok_research_agent/` package implementation, packaged prompts, and automated tests
- Specification intent: Describe the functional behavior the system currently implements, including workflow behavior, file contracts, validation rules, failure handling, and integration points

2. Purpose

The system provides a local-first research automation workflow that converts a user-supplied topic into a detailed Markdown research report through a staged pipeline of scope definition, source discovery, source curation, content extraction, notebook assembly, synthesis, optional full-source preservation, final polishing, knowledge compilation, drill-pack generation, image-prompt generation, and YouTube-script generation.

The system is designed to:

- preserve human control at key decision points;
- store all research artifacts locally in resumable session directories;
- use Grok through the xAI OpenAI-compatible API for all LLM generation tasks;
- support optional ingestion of external local documentation as steering context;
- produce inspectable intermediate artifacts rather than a single opaque result.

3. Scope

3.1 In Scope

- Command-line session lifecycle management
- Persistent session state and artifact storage
- Eight-phase research workflow orchestration
- Optional unattended execution mode
- External-document preprocessing for local steering material
- Knowledge-base compilation into hypergraph and core concepts
- Drill-pack generation from compiled concepts
- Hypergraph updates from newly fed documents
- Mermaid rendering of hypergraph data
- Image-prompt generation from final report content
- YouTube-script generation from final report or section drafts

3.2 Out of Scope

- Web UI, API server, or multi-user collaboration
- Authentication, authorization, and role-based permissions
- Database-backed persistence
- Semantic vector search or retrieval index
- Automatic browser automation or crawler orchestration beyond direct HTTP fetch
- Guaranteed factual validation of LLM outputs
- Binary document feeding in the `feed` command beyond best-effort text decoding

4. Stakeholders, Roles, and External Actors

4.1 Human User Roles

- `Research Operator`: Starts sessions, approves or revises workflow outputs, selects curated sources, optionally chooses full offline collection, and runs auxiliary commands
- `Reviewer/Study User`: Consumes generated report, drill pack, hypergraph, Mermaid output, image prompts, or YouTube script; this role is not technically distinct from the operator

4.2 System Actors

- `LLM Provider`: xAI Grok, accessed through the OpenAI-compatible API
- `Remote Content Hosts`: Public websites and PDF endpoints referenced by curated sources
- `Local Filesystem`: Stores sessions, state, outputs, external-doc artifacts, and knowledge-base artifacts
- `Local Environment`: Provides `.env` or environment variables, `EDITOR`, and Python runtime

4.3 Access Model

- The system implements no internal user accounts and no permission model.
- Any user who can execute the CLI and read/write the target sessions directory can operate the system fully.

5. System Context and Architecture

5.1 Core Modules

- `grok_research_agent.cli`
  - Parses CLI arguments
  - Creates `SessionManager` and `WorkflowRunner`
  - Maps command failures to process exit codes
- `grok_research_agent.session_manager`
  - Creates and persists session state
  - Creates unique run directories
  - Provides canonical session and knowledge-base paths
- `grok_research_agent.workflow_phases`
  - Implements the workflow state machine
  - Handles source fetching, extraction, synthesis, compilation, drill-pack generation, feed, show, image generation, and YouTube script generation
- `grok_research_agent.grok_client`
  - Loads environment configuration
  - Calls xAI Grok using the OpenAI client
  - Maps API exceptions into domain-specific runtime errors
- `grok_research_agent.external_docs`
  - Recursively ingests supported local docs
  - Extracts steering context, constraints, requirements, and relevance signals
- `grok_research_agent.prompts/*`
  - Defines output contracts and behavioral instructions for LLM calls

5.2 Execution Model

- The product is a single-process CLI application.
- Each command creates a new run directory under the target session.
- Commands operate on files in the session directory and may also write run-local copies for traceability.
- Long-lived state is file-based; there is no background daemon.

6. Technology and Runtime Dependencies

- Python runtime: `>=3.11`
- noted packages:
  - `openai`
  - `python-dotenv`
  - `rich`
  - `pydantic>=2`
  - `pypdf`
  - `python-docx`
  - `requests`
  - `beautifulsoup4`
  - `readability-lxml`
  - `chardet<6`
- Packaged CLI entrypoint: `grok-research-agent = grok_research_agent.cli:main`
- Convenience wrappers: root-level `main.py` and `cli.py` forward to packaged CLI entrypoint

7. Configuration Specification

7.1 Environment Variables

- `GROK_API_KEY`
  - noted for any command path that instantiates `GrokClient`
  - Must be non-empty after whitespace trimming
  - If absent, LLM-backed actions shall fail with a clear message
- `GROK_MODEL`
  - Optional
  - Defaults to `grok-3`
  - Blank values shall be normalized back to `grok-3`
- `GROK_MAX_OUTPUT_TOKENS`
  - Optional integer
  - Defaults to `50000`
  - Invalid or non-numeric values shall revert to `50000`
  - Values below `1` shall be clamped to `1`
- `GROK_REQUEST_TIMEOUT_SECONDS`
  - Optional integer
  - Defaults to `300`
  - Invalid or non-numeric values shall revert to `300`
  - Values below `1` shall be clamped to `1`
- `EDITOR`
  - Optional
  - Used only during Phase 0 `edit` flow
  - If absent, selecting `edit` shall still create the editable temporary file, but no external editor is launched automatically

7.2 `.env` Resolution

- When the workflow constructs a default `GrokClient`, it shall attempt to load a `.env` file located two directory levels above the session directory.
- If no `.env` exists there, the system shall continue using process environment variables only.

8. User Interface Specification

8.1 Interface Type

- Primary interface: terminal/CLI
- Rendering library: `rich`
- Output types:
  - plain status messages
  - Markdown content echoed to console in some phases
  - preview tables for discovery and full-collection selection

8.2 Human Interaction Points

- H0: scope confirmation
- H1: curated-source approval
- H2: draft approval or revision instruction
- H3: full-source offline-copy selection

8.3 Unattended Mode

- `--auto` shall bypass interactive prompts and drive the workflow to completion where possible.
- In auto mode:
  - H0 is auto-confirmed
  - H1 source selection is set to `all`
  - H1 approval is set to `approve`
  - H2 feedback is set to `approve`
  - H3 selection is controlled by `--auto-full-collection` and defaults to `all`
- Auto mode shall not call `input()`.

9. User Roles and Permissions Specification

Because the system has no identity or authorization layer, the functional permission model is:

- any operator can execute any command;
- any operator can create, resume, modify, compile, drill, feed, and finalize sessions they can access on disk;
- there are no restricted admin-only actions;
- there is no audit or attribution model beyond file timestamps and artifact presence.

10. CLI Command Functional Requirements

10.1 Common Command Behavior

- `FR-CLI-001`: All commands except `list-types` shall require `--sessions-dir`.
- `FR-CLI-002`: Commands that need an existing session shall require `--session-id`.
- `FR-CLI-003`: The CLI shall return exit code `0` for successful completion.
- `FR-CLI-004`: The CLI shall return exit code `1` when `WorkflowRunner.run()` raises `GrokError` or `GrokQuotaError`.
- `FR-CLI-005`: The CLI shall return exit code `2` for unrecognized command dispatch or `argparse` validation failures.
- `FR-CLI-006`: When `--trace-llm` is enabled, request and response content shall be printed in truncated, control-character-sanitized form.

10.2 `start`

- `FR-START-001`: The system shall create a new session with topic, optional focus, optional external docs directory, and a persisted `mode`.
- `FR-START-002`: The system shall print the created session ID.
- `FR-START-003`: The system shall immediately invoke workflow execution beginning at the session's current phase, initially Phase 0.
- `FR-START-004`: The accepted `--mode` values shall be `report`, `compiler`, and `drill`.
- `FR-START-005`: The selected `mode` shall be stored in session state but shall not alter runtime workflow behavior in the current implementation.

10.3 `resume`

- `FR-RESUME-001`: The system shall load the session and execute from `current_phase`.
- `FR-RESUME-002`: In interactive mode, execution shall stop at the next human checkpoint or after a phase that explicitly instructs the user to resume again.
- `FR-RESUME-003`: If `current_phase >= 8`, the system shall print `Session is complete.`

10.4 `list-sessions`

- `FR-LIST-001`: The system shall list directories under `--sessions-dir` that contain `session.json`.
- `FR-LIST-002`: The listing shall exclude non-directory entries and directories missing `session.json`.
- `FR-LIST-003`: If no sessions exist, the system shall print `No sessions found.`

10.5 `list-types`

- `FR-TYPES-001`: The system shall print `auto-hypergraph`.
- `FR-TYPES-002`: No session directory argument shall be noted for this command.

10.6 `update`

- `FR-UPDATE-001`: The system shall run discovery with `since_last_run=yes`.
- `FR-UPDATE-002`: On completion, the system shall set `current_phase = 2`.
- `FR-UPDATE-003`: The system shall instruct the user to resume in order to curate sources.

10.7 `synthesize`

- `FR-SYNTH-001`: The system shall force execution of Phase 5 synthesis regardless of current phase.
- `FR-SYNTH-002`: Phase 5 prerequisites still apply; if notebook input is missing, synthesis shall not proceed.

10.8 `compile`

- `FR-COMPILE-001`: The CLI shall expose `--type auto-hypergraph`.
- `FR-COMPILE-002`: The workflow shall accept `auto-hypergraph` and internally tolerate additional dormant auto-type strings, but only `auto-hypergraph` is exposed and supported end-to-end.
- `FR-COMPILE-003`: The system shall compile from `04_master_notebook.md` when present and append any `03_extracted/*.md` content when present.
- `FR-COMPILE-004`: If no notebook or extracted content exists, the system shall print `Missing notebook or extractions. Resume the session to generate them first.` and stop.

10.9 `drill`

- `FR-DRILL-001`: The only supported mode shall be `backward`.
- `FR-DRILL-002`: If `core_concepts.json` is absent, the system shall attempt `compile` automatically.
- `FR-DRILL-003`: If core concepts are still absent after compile, the system shall print `Missing core concepts. Run compile first.`

10.10 `feed`

- `FR-FEED-001`: The command shall require `--new-doc`.
- `FR-FEED-002`: If the file does not exist or is not a regular file, the system shall print `File not found: <path>` and stop.
- `FR-FEED-003`: The system shall copy the file into `knowledge_base/feed_docs/` with a timestamp prefix.
- `FR-FEED-004`: If no `hypergraph.json` exists, the system shall invoke compile and then return without performing a merge update.

10.11 `show`

- `FR-SHOW-001`: If `knowledge_base/hypergraph.json` does not exist, the system shall print `Missing hypergraph.json. Run compile first.`
- `FR-SHOW-002`: Otherwise, the system shall generate `knowledge_base/hypergraph.mmd`.

10.12 `generate-images`

- `FR-IMG-001`: The command shall require `FINAL_REPORT.md`.
- `FR-IMG-002`: If `FINAL_REPORT.md` is missing, the system shall print `Missing FINAL_REPORT.md`.
- `FR-IMG-003`: On success, the system shall write `images_to_generate.md` in both the run directory and session directory.

10.13 `youtube-script`

- `FR-YT-001`: The command shall require `FINAL_REPORT.md`.
- `FR-YT-002`: If `FINAL_REPORT.md` is missing, the system shall print `Missing FINAL_REPORT.md`.
- `FR-YT-003`: On success, the system shall write `Youtube_Script.md` in both the run directory and session directory.

11. Session Management Specification

11.1 Session Identity

- `FR-SESSION-001`: Session IDs shall be generated from a slugified topic plus current date in `YYYYMMDD` format.
- `FR-SESSION-002`: Slugification shall lowercase the topic, replace non-alphanumeric characters with `-`, collapse repeated hyphens, and strip leading/trailing hyphens.
- `FR-SESSION-003`: If the slug exceeds the configured prefix length, the system shall trim it and append an 8-character SHA-1 digest suffix.
- `FR-SESSION-004`: If a generated session directory already exists, the system shall append `-2`, `-3`, and so on until unique.

11.2 Session State

The persisted `SessionState` shall contain:

- `session_id`
- `topic`
- `focus`
- `mode`
- `external_docs_dir`
- `external_docs_status`
- `external_docs_summary`
- `external_docs_manifest_path`
- `external_docs_context_path`
- `external_docs_processed_files`
- `external_docs_total_files`
- `external_docs_completion_rate`
- `external_docs_relevance_score`
- `external_docs_last_error`
- `created_at`
- `grok_model`
- `current_phase`
- `run_history`
- `updated_at`

11.3 Session Persistence Rules

- `FR-SESSION-005`: The system shall persist state to `session.json` encoded as UTF-8 JSON.
- `FR-SESSION-006`: `updated_at` shall be refreshed on each `save_state()`.
- `FR-SESSION-007`: The sessions directory and knowledge-base subdirectories shall be created automatically when saving.
- `FR-SESSION-008`: `run_history` shall be initialized as an empty list but is not populated by current workflow code.

11.4 Run Directory Rules

- `FR-RUN-001`: Each command execution that creates a `WorkflowContext` shall create a new run directory under `runs/`.
- `FR-RUN-002`: Run directory names shall use timestamp format `YYYYMMDD_HHMMSS_microseconds`.
- `FR-RUN-003`: If a timestamp collision occurs, the system shall retry up to 1000 times.
- `FR-RUN-004`: If a unique run directory cannot be created within 1000 attempts, the system shall raise `RuntimeError`.

12. External Document Preprocessing Specification

12.1 Feature Purpose

The external-doc subsystem ingests local reference documents before workflow execution and converts them into mandatory steering context that can influence scope, discovery, curation, extraction, and planning.

12.2 Trigger Rules

- `FR-EXT-001`: External-doc preprocessing shall run automatically before workflow commands except `generate-images`, `youtube-script`, `compile`, `drill`, `feed`, and `show`.
- `FR-EXT-002`: If `external_docs_dir` is blank or absent, preprocessing shall be skipped.
- `FR-EXT-003`: If session state already marks preprocessing as `completed` and a summary exists, preprocessing shall not re-run automatically.

12.3 Supported Inputs

- Supported suffixes: `.pdf`, `.docx`, `.txt`, `.md`
- Discovery behavior: recursive under the provided root directory
- Unsupported file types: ignored rather than errored

12.4 Processing Rules

- `FR-EXT-004`: Each supported file shall be read using type-appropriate logic.
- `FR-EXT-005`: PDF extraction shall iterate pages and skip pages whose text extraction fails.
- `FR-EXT-006`: DOCX extraction shall concatenate non-empty paragraphs.
- `FR-EXT-007`: TXT and Markdown shall be read as UTF-8 with replacement for invalid characters.
- `FR-EXT-008`: Each document shall be categorized as `guideline`, `background`, `steering`, or `general` based on filename keywords.
- `FR-EXT-009`: The processor shall extract key concepts, constraints, requirements, and algorithm insights from sentence-level heuristics.
- `FR-EXT-010`: The processor shall compute a relevance score from topic/focus lexical overlap plus structural bonuses for relevant terms, extracted constraints, and extracted requirements.

12.5 Aggregated Outputs

- `FR-EXT-011`: The system shall write:
  - `external_docs/manifest.json`
  - `external_docs/extracted.json`
  - `external_docs/context.md`
- `FR-EXT-012`: `manifest.json` shall include per-file processing results and aggregate success metrics.
- `FR-EXT-013`: `context.md` shall include sections for key concepts, constraints, requirements, optional algorithm enhancement notes, and workflow guidance.
- `FR-EXT-014`: If topic or focus text matches algorithm-oriented keywords, algorithm enhancement notes shall be included; otherwise they shall be omitted.

12.6 Status Rules

- `FR-EXT-015`: If the external-doc root directory does not exist or is not a directory, status shall be set to `failed`, an explanatory error shall be stored in session state, and the workflow shall continue.
- `FR-EXT-016`: If individual files fail, those files shall be marked `failed`, but aggregate processing shall continue.
- `FR-EXT-017`: Aggregate status shall be:
  - `completed` when all discovered files process successfully
  - `partial` when at least one file succeeds and at least one fails
  - `failed` when zero files succeed

12.7 Prompt Injection Rules

- `FR-EXT-018`: When available, external-doc summary content shall be appended to relevant prompts as mandatory steering/background material.
- `FR-EXT-019`: External-doc context shall be truncated to phase-specific character budgets instead of causing failures.

13. Research Workflow State Machine

13.1 State Definitions

- Phase `0`: Scope generation and confirmation
- Phase `1`: Discovery
- Phase `2`: Curation and gap analysis
- Phase `3`: Extraction
- Phase `4`: Notebook assembly
- Phase `5`: Synthesis and review
- Phase `6`: Full offline collection selection
- Phase `7`: Final polish
- Phase `8`: Complete

13.2 Interactive Progression Rules

- `FR-STATE-001`: In interactive mode, the workflow shall process one phase or one human checkpoint per `resume` call according to `_run_until_human_step()`.
- `FR-STATE-002`: Some phases end by instructing the user to resume later instead of continuing automatically.
- `FR-STATE-003`: Phase transitions shall be persisted immediately when the code explicitly updates `current_phase`.

13.3 Auto-Mode Progression Rules

- `FR-STATE-004`: In auto mode, the workflow shall loop until `current_phase >= 8`.
- `FR-STATE-005`: Auto mode shall continue immediately across phases without requiring separate `resume` commands.

14. Phase-by-Phase Functional Requirements

14.1 Phase 0 - Scope Confirmation

- `FR-P0-001`: The system shall generate a Markdown scope summary using `scope_prompt.txt`.
- `FR-P0-002`: The generated scope shall be written to `<run>/00_scope.md`.
- `FR-P0-003`: The generated scope shall be printed to the console.
- `FR-P0-004`: In auto mode, the scope shall be accepted immediately, saved as `00_scope_confirmed.md`, and `current_phase` shall advance to `1`.
- `FR-P0-005`: In interactive mode, valid user inputs are `yes`, `edit`, and `cancel`.
- `FR-P0-006`: `cancel` shall terminate the phase without changing `current_phase`.
- `FR-P0-007`: `edit` shall write a temporary `00_scope_edit.md`, optionally invoke the `EDITOR`, reload the edited content, print it, and continue prompting.
- `FR-P0-008`: `yes` shall save `00_scope_confirmed.md`, set `current_phase = 1`, save state, and instruct the user to resume.
- `FR-P0-009`: If Grok client creation fails, the system shall print the error plus a `.env` guidance message and return without changing state.

14.2 Phase 1 - Discovery

- `FR-P1-001`: The system shall render `discovery_prompt.txt` with topic, effective focus, and `since_last_run`.
- `FR-P1-002`: Discovery output shall be written to both `<run>/01_discovery_table.md` and `<session>/01_discovery_table.md`.
- `FR-P1-003`: The system shall not validate discovery table format before saving.
- `FR-P1-004`: In normal interactive progression, completion of Phase 1 shall set `current_phase = 2` and instruct the user to resume for curation.

14.3 Phase 2 - Curation and Gap Analysis

- `FR-P2-001`: Phase 2 shall require `01_discovery_table.md`; if missing, the system shall print `Missing discovery table. Resume from Phase 1.` and stop.
- `FR-P2-002`: The system shall print a preview table containing up to the first 80 non-empty lines of discovery output.
- `FR-P2-003`: The user instruction string may contain free-form source-selection text, including numbers, `all`, `add <urls>`, `remove <indexes>`, or `gap`; the system does not parse these commands locally and instead passes them to the LLM.
- `FR-P2-004`: The system shall attempt curated-source generation up to 3 times.
- `FR-P2-005`: On retry attempts after the first failure, the prompt shall add stricter JSON-only instructions and a top-20 limit.
- `FR-P2-006`: Curated-source output shall be canonicalized into a list of objects with keys:
  - `title`
  - `url`
  - `type`
  - `why_relevant`
  - `credibility`
  - `priority`
- `FR-P2-007`: URLs shall be normalized by trimming quotes/backticks and removing trailing punctuation where possible.
- `FR-P2-008`: If the LLM returns invalid JSON or a non-canonical structure on all attempts, the system shall recover URLs heuristically from the discovery Markdown and build fallback source entries.
- `FR-P2-009`: Run-local curation output shall be written verbatim to `<run>/02_curated_sources.json`.
- `FR-P2-010`: Session-local curation output shall be re-written as canonical JSON to `<session>/02_curated_sources.json`.
- `FR-P2-011`: Gap analysis shall always be attempted using the curated list and saved to `<run>/02_gap_report.md`.
- `FR-P2-012`: If gap analysis times out, the saved gap report shall contain `# Gaps` and an explicit timeout note.
- `FR-P2-013`: Phase advancement to `3` shall occur only when the approval input is exactly `approve`.
- `FR-P2-014`: Any other approval response shall leave the session in Phase 2 and instruct the user to repeat curation later.

14.4 Phase 3 - Extraction

- `FR-P3-001`: Phase 3 shall require `02_curated_sources.json`; if missing, the system shall print `Missing curated sources. Resume from Phase 2.`
- `FR-P3-002`: If curated-source JSON exists but canonicalization produces an empty list, the system shall print `Curated sources file is invalid or empty. Resume from Phase 2 to re-curate sources.`
- `FR-P3-003`: The system shall create the following directories in both run and session scopes as applicable:
  - `03_extracted/`
  - `03_source_snapshots/`
  - `03_extracted_chunks/`
- `FR-P3-004`: The system shall request an extraction plan and save it as `<run>/03_extraction_plan.md`.
- `FR-P3-005`: If extraction-plan generation times out, the system shall save a placeholder plan instead of failing.
- `FR-P3-006`: The system shall prefetch source bundles concurrently using up to `4` fetch workers.
- `FR-P3-007`: If an individual source fetch fails during prefetch, the system shall print a warning and continue extracting remaining sources.
- `FR-P3-008`: For each successfully fetched source, the system shall save raw content and normalized source text snapshots in both run and session directories.
- `FR-P3-009`: Snapshot headers shall preserve title, URL, host, type, priority, and credibility metadata.
- `FR-P3-010`: HTML source bundles shall save raw snapshots with `.html`; PDF bundles with `.pdf`; all others with `.txt`.
- `FR-P3-011`: Source text shall be chunked with:
  - max chunk size `45000` characters
  - overlap `5000` characters
- `FR-P3-012`: Chunk extraction shall run in parallel using up to `2` extraction workers.
- `FR-P3-013`: Each chunk prompt shall require strict Markdown sections for coverage summary, terminology, mechanisms, workflows, evidence, limitations, open questions, quotable passages, and extraction notes.
- `FR-P3-014`: If an extraction chunk times out, that chunk shall be skipped and extraction shall continue for other chunks.
- `FR-P3-015`: Each successful extracted chunk shall be written to both run and session `03_extracted_chunks/`.
- `FR-P3-016`: If all chunks for a source fail, the system shall print a warning and skip generating that source dossier.
- `FR-P3-017`: Successful source dossiers shall be assembled into `03_extracted/<nnn>.md` in both run and session directories.
- `FR-P3-018`: On phase completion, the system shall write `<session>/03_extracted_index.txt` with a generation marker.

14.5 Phase 4 - Notebook Assembly

- `FR-P4-001`: Phase 4 shall require existence of `<session>/03_extracted/`; otherwise it shall print `No extracted sources found in this run. Resume from Phase 3.`
- `FR-P4-002`: The notebook shall include:
  - top heading `# Master Notebook`
  - topic line
  - notebook purpose section
  - optional external documentation context section
  - source catalog section
  - optional knowledge-base outline
  - source dossiers section
- `FR-P4-003`: The notebook shall concatenate parts using `---` separators.
- `FR-P4-004`: The notebook shall be written to both `<run>/04_master_notebook.md` and `<session>/04_master_notebook.md`.
- `FR-P4-005`: In interactive progression, successful notebook generation shall set `current_phase = 5`.

14.6 Phase 5 - Synthesis and Review

- `FR-P5-001`: Phase 5 shall require `04_master_notebook.md`; if missing, the system shall print `Missing notebook. Resume from Phase 4.`
- `FR-P5-002`: The notebook shall be split into chunks of up to `70000` characters with `5000` overlap.
- `FR-P5-003`: If no notebook chunks are produced, the system shall print `Notebook is empty. Resume from Phase 4.`
- `FR-P5-004`: For each report section in the fixed section list, the system shall build section-specific evidence packets from notebook chunks.
- `FR-P5-005`: Standard report sections shall be:
  - `Core Definitions and Scope`
  - `Architecture and Technical Mechanisms`
  - `Workflows, Processes, and Operational Patterns`
  - `Evidence, Examples, and Case Studies`
  - `Limitations, Trade-offs, and Failure Modes`
  - `Open Questions and Future Directions`
- `FR-P5-006`: Evidence-packet generation shall run with up to `2` workers per section.
- `FR-P5-007`: Evidence packets shall be saved in both run and session `05_section_evidence/` directories.
- `FR-P5-008`: If no evidence packets are generated for a section, that section shall be skipped with a warning.
- `FR-P5-009`: Each successfully drafted section shall be written to both run and session `05_section_drafts/`.
- `FR-P5-010`: The draft report shall include scope/coverage text, source catalog, drafted sections, optional knowledge-base alignment, and references.
- `FR-P5-011`: Draft versions shall be saved as incrementing `05_draft_vN.md`.
- `FR-P5-012`: The review prompt shall tell the user they may enter `approve | revise <section> <feedback> | add-section "Title" | gap-check`.
- `FR-P5-013`: Only exact response `approve` shall advance the session to Phase 6.
- `FR-P5-014`: Any non-`approve` response shall be treated as general revision feedback and passed to the revision prompt without local parsing.
- `FR-P5-015`: If revision generation times out, the prior draft shall remain authoritative and phase state shall not advance.
- `FR-P5-016`: Successful revision output shall be stored as the next draft version and require another review cycle.

14.7 Phase 6 - Full Offline Collection

- `FR-P6-001`: Phase 6 shall attempt to load curated sources from `02_curated_sources.json`.
- `FR-P6-002`: If curated sources are absent, the system shall attempt heuristic URL recovery from `01_discovery_table.md`.
- `FR-P6-003`: If no curated sources can be recovered, the system shall set `current_phase = 7`, save state, print a skip message, and require a subsequent resume for finalization.
- `FR-P6-004`: The source selection UI shall display index, title, and URL for each curated source.
- `FR-P6-005`: Valid practical inputs are `all`, `none`, or comma-separated integers; non-numeric tokens shall be ignored.
- `FR-P6-006`: Response `none` shall set `current_phase = 7`, save state, print a skip message, and return without finalizing automatically.
- `FR-P6-007`: Response `all` shall select all sources.
- `FR-P6-008`: Numeric selections outside valid index range shall be ignored.
- `FR-P6-009`: Selected sources shall be prefetched before writing full offline copies.
- `FR-P6-010`: For each successfully fetched selected source, the system shall write `06_full_sources/<nnn>.md` in both run and session directories.
- `FR-P6-011`: If a selected source cannot be fetched, that source shall be skipped without aborting the phase.
- `FR-P6-012`: After writing at least the attempted full-collection outputs, the system shall set `current_phase = 7`, invoke final polish immediately, then set `current_phase = 8`.

14.8 Phase 7 - Final Polish

- `FR-P7-001`: Final polish shall require both `04_master_notebook.md` and at least one `05_draft_v*.md`; otherwise it shall print `Missing notebook or draft.`
- `FR-P7-002`: The latest draft file by lexicographic version ordering shall be used as the report body source.
- `FR-P7-003`: The system shall generate an executive summary using `final_polish_prompt.txt`.
- `FR-P7-004`: If executive-summary generation times out, the system shall substitute a timeout placeholder message.
- `FR-P7-005`: The system shall generate a glossary using `glossary_prompt.txt`.
- `FR-P7-006`: If glossary generation times out, the system shall substitute a timeout placeholder bullet.
- `FR-P7-007`: If the latest draft begins with a level-1 heading, that heading shall be removed before final report assembly.
- `FR-P7-008`: The system shall build a Markdown table of contents from all level-2 headings in the report body.
- `FR-P7-009`: The final report shall contain:
  - level-1 final report heading
  - table of contents
  - executive summary
  - main body
  - source catalog
  - optional knowledge-base overview
  - glossary
- `FR-P7-010`: The system shall attempt to retarget word count twice if needed:
  - once on the body
  - once on the complete assembled report
- `FR-P7-011`: Final report word-count targets shall be:
  - minimum `9000`
  - maximum `10000`
  - target `9500`
- `FR-P7-012`: Word-count correction shall preserve headings and core claims while expanding or compressing content.
- `FR-P7-013`: The final report shall be written to both `<run>/FINAL_REPORT.md` and `<session>/FINAL_REPORT.md`.
- `FR-P7-014`: The system shall then attempt image-prompt generation and YouTube-script generation.

14.9 Phase 8 - Complete

- `FR-P8-001`: A session with `current_phase >= 8` shall be treated as complete.
- `FR-P8-002`: Resume on a completed session shall print `Session is complete.`

15. Source Fetching and Transformation Specification

15.1 URL Validation

- `FR-FETCH-001`: URLs shall be normalized before validation.
- `FR-FETCH-002`: Only `http` and `https` URLs with a network location shall be accepted.
- `FR-FETCH-003`: Invalid URLs shall raise `ValueError`.

15.2 HTTP Fetch Rules

- `FR-FETCH-004`: HTTP fetches shall use a user agent string `grok-research-agent/0.1`.
- `FR-FETCH-005`: Redirects shall be followed.
- `FR-FETCH-006`: Timeout shall be split into connect timeout and read timeout.
- `FR-FETCH-007`: Request timeouts shall raise `TimeoutError` with URL context.

15.3 Content-Type Handling

- `FR-FETCH-008`: PDF detection shall use either `Content-Type: application/pdf` or `.pdf` URL suffix.
- `FR-FETCH-009`: PDF bundles shall return extracted text as raw, main, full, and analysis text.
- `FR-FETCH-010`: Non-HTML non-PDF responses shall be treated as plain text.
- `FR-FETCH-011`: HTML responses shall generate:
  - `main_text` from `readability-lxml` summary when available
  - `full_text` from full-page HTML text extraction
  - `analysis_text` as merged main/full text or fallback content

15.4 HTML Text Normalization

- `FR-FETCH-012`: HTML extraction shall remove `script`, `style`, `noscript`, and `svg` tags.
- `FR-FETCH-013`: Duplicate normalized lines shall be removed to reduce repeated boilerplate.

16. Knowledge Compilation Specification

16.1 Compiler Inputs and Outputs

- `FR-KB-001`: Compile shall use notebook content first and then append extracted source dossiers when available.
- `FR-KB-002`: Hypergraph compilation shall use only the first `220000` characters of content.
- `FR-KB-003`: Core-concept extraction shall use:
  - first `220000` characters of source content
  - first `120000` characters of hypergraph JSON
- `FR-KB-004`: Compile outputs shall be written to:
  - `knowledge_base/hypergraph.json`
  - `knowledge_base/auto_types/auto_hypergraph.json`
  - `knowledge_base/core_concepts.json`

16.2 Hypergraph Contract

- `FR-KB-005`: Prompted hypergraph schema shall be:

'''json
{
  "nodes": [{"id": "N1", "label": "..."}],
  "hyperedges": [{"id": "E1", "nodes": ["N1", "N2", "N3"], "relation": "...", "evidence": "..."}]
}
'''

- `FR-KB-006`: If the LLM does not return valid JSON, the system shall persist a fallback JSON wrapper, typically `{ "raw": "<response>" }`, instead of failing the command.

16.3 Core Concepts Contract

- `FR-KB-007`: Prompted core-concepts schema shall be:

'''json
{
  "core_concepts": [
    {
      "name": "...",
      "definition": "...",
      "why_load_bearing": "..."
    }
  ]
}
'''

- `FR-KB-008`: The prompt requires exactly 7 concepts, but the implementation does not independently enforce the count after generation.

16.4 Drill-Pack Contract

- `FR-KB-009`: Drill-pack prompt output schema shall be:

'''json
{
  "drill_pack_markdown": "markdown string",
  "drill_questions": [
    {
      "concept": "...",
      "questions": [
        {
          "question": "...",
          "answer": "...",
          "pitfalls": ["...", "..."]
        }
      ]
    }
  ]
}
'''

- `FR-KB-010`: If `drill_pack_markdown` is missing or blank, the system shall strip code fences from the raw response and use the remainder as Markdown output.
- `FR-KB-011`: If the parsed JSON lacks `drill_questions`, the entire parsed object shall be written as `drill_questions.json`.

16.5 Feed and Hypergraph Update

- `FR-KB-012`: Feed shall read the new document using UTF-8 with replacement for decoding errors.
- `FR-KB-013`: Feed merge prompts shall receive:
  - first `160000` characters of existing hypergraph JSON
  - first `160000` characters of new document content
- `FR-KB-014`: Updated hypergraph output shall overwrite both canonical hypergraph locations.

16.6 Mermaid Rendering

- `FR-KB-015`: Mermaid output shall begin with `graph TD`.
- `FR-KB-016`: Node rendering shall use up to the first `200` nodes.
- `FR-KB-017`: Edge rendering shall use up to the first `400` edges or hyperedges.
- `FR-KB-018`: For hyperedges with more than two members, Mermaid rendering shall connect only the first two listed nodes.
- `FR-KB-019`: Edge labels shall use `relation` or `label` when present.

17. Final Report, Image Prompt, and YouTube Script Specification

17.1 Final Report Output Contract

- `FR-OUT-001`: The final report shall be a Markdown document named `FINAL_REPORT.md`.
- `FR-OUT-002`: The final report shall include explicit `## Executive Summary` and `## Source Catalog` sections.
- `FR-OUT-003`: If knowledge-base content exists, the report shall also include `## Knowledge Base Overview`.
- `FR-OUT-004`: The report shall end with a glossary section even if glossary generation timed out.

17.2 Image Prompt Generation

- `FR-OUT-005`: Image prompts shall be generated from the complete final report.
- `FR-OUT-006`: The prompt contract requests 5 to 10 image prompts emphasizing concrete mechanisms, workflows, architectures, comparisons, and evidence rather than generic concept art.
- `FR-OUT-007`: If image-prompt generation times out during final polish, report creation shall still succeed.

17.3 YouTube Script Generation

- `FR-OUT-008`: The system shall derive YouTube sections primarily from `05_section_drafts/` when available; otherwise it shall derive them from `FINAL_REPORT.md`.
- `FR-OUT-009`: The following report sections shall be excluded from narration source selection:
  - `Table of Contents`
  - `Source Catalog`
  - `Glossary`
  - `References`
  - `Knowledge Base Overview`
  - `Executive Summary`
- `FR-OUT-010`: The generated script shall contain:
  - top heading `# YouTube Script`
  - `## Introduction`
  - one level-2 heading per selected section
  - `## Conclusion`
- `FR-OUT-011`: If intro or outro generation times out, the system shall insert fallback placeholder narration instead of failing.
- `FR-OUT-012`: If a section generation times out, that section may be omitted while the rest of the script proceeds.
- `FR-OUT-013`: Short intro, section, or outro outputs shall be expanded by a secondary LLM call to hit minimum detail thresholds.
- `FR-OUT-014`: If a generated section lacks a Markdown heading, the system shall prepend the noted heading automatically.

18. Input and Output File Specification

18.1 Session Root Outputs

The session root may contain:

- `session.json`
- `00_scope_confirmed.md`
- `01_discovery_table.md`
- `02_curated_sources.json`
- `03_extracted/`
- `03_source_snapshots/`
- `03_extracted_chunks/`
- `03_extracted_index.txt`
- `04_master_notebook.md`
- `05_section_evidence/`
- `05_section_drafts/`
- `05_draft_vN.md`
- `06_full_sources/`
- `FINAL_REPORT.md`
- `images_to_generate.md`
- `Youtube_Script.md`
- `external_docs/`
- `knowledge_base/`
- `runs/`

18.2 Knowledge Base Outputs

- `knowledge_base/hypergraph.json`
- `knowledge_base/core_concepts.json`
- `knowledge_base/drill_pack.md`
- `knowledge_base/drill_questions.json`
- `knowledge_base/hypergraph.mmd`
- `knowledge_base/auto_types/auto_hypergraph.json`
- `knowledge_base/feed_docs/<timestamp>_<original_name>`

18.3 Run-Scoped Outputs

- Each command execution that builds a workflow context may create run-local copies of generated artifacts for traceability and debugging.

19. Validation Rules

19.1 CLI Validation

- noted flags shall be enforced by `argparse`.
- Unsupported `compile --type` values exposed via CLI cannot pass parser validation.
- Unsupported `drill --mode` values exposed via CLI cannot pass parser validation.

19.2 Semantic Validation

- Curated-source validation is structural and best-effort, not strict schema validation via a dedicated validator.
- Discovery output is not structurally validated.
- Final report content is not semantically validated for factual correctness.
- Core concept count is prompt-constrained but not post-validated.

19.3 File Validation

- `feed` validates file existence and regular-file status.
- External docs validate root directory existence and supported suffixes.
- Session listing validates presence of `session.json`.

20. Error Handling and Recovery Specification

20.1 Grok API Errors

- `FR-ERR-001`: Missing API key shall raise `GrokError("Missing GROK_API_KEY in .env or environment")`.
- `FR-ERR-002`: Quota/billing-related API errors shall be mapped to `GrokQuotaError` with actionable text.
- `FR-ERR-003`: Timeout-like API errors shall be mapped to `GrokTimeoutError` including configured timeout seconds.
- `FR-ERR-004`: Non-timeout non-quota API failures shall be retried up to `5` times with exponential backoff capped at `30` seconds.
- `FR-ERR-005`: Quota and timeout errors are not retried in `GrokClient.chat_text()` once mapped.

20.2 LLM Timeout Tolerance

- `FR-ERR-006`: Selected phases use `_llm_optional()` to convert LLM timeout failures into warnings and continue:
  - gap analysis
  - extraction plan
  - extraction chunks
  - section evidence packets
  - section drafts
  - revision
  - executive summary
  - glossary
  - image prompts
  - YouTube intro/segments/outro
  - word-count retargeting
- `FR-ERR-007`: When `_llm_optional()` handles a timeout, the system shall print a warning and continue unless the calling feature requires explicit output to proceed.

20.3 Source Fetch Errors

- `FR-ERR-008`: Source fetch failures shall not abort the whole extraction or full-collection phase.
- `FR-ERR-009`: A timed-out fetch shall raise `TimeoutError`; callers may log and skip the source.

20.4 JSON Robustness

- `FR-ERR-010`: The system shall strip Markdown code fences when attempting to parse JSON-like model outputs.
- `FR-ERR-011`: The system shall attempt direct parse, bracket-slice parse, and brace-slice parse before falling back to raw wrapper JSON.
- `FR-ERR-012`: Invalid curated-source JSON shall trigger heuristic recovery from discovery links.

20.5 Non-Fatal Degradation Rules

- `FR-ERR-013`: Missing external docs shall not block the research workflow.
- `FR-ERR-014`: Missing curated sources in Phase 6 shall downgrade to skip behavior rather than fatal failure.
- `FR-ERR-015`: Missing hypergraph or core concepts shall produce instructional console messages rather than uncaught failures.
- `FR-ERR-016`: Missing final report for image or YouTube generation shall produce instructional console messages.

21. Integration Specifications

21.1 xAI Grok Integration

- Protocol: OpenAI-compatible chat completions API
- Base URL: `[historical-url]
- Auth: bearer API key supplied via environment
- Message structure: one system message and one user message per call
- Response handling: first completion choice message content or empty string

21.2 Remote Web Integration

- Protocol: HTTP/HTTPS GET
- Redirects: enabled
- Authentication: none
- SSL behavior: delegated to `requests`
- Failure handling: errors bubble to caller or are caught per phase and downgraded to warnings where designed

21.3 Local Document Integration

- External docs support `.pdf`, `.docx`, `.txt`, `.md`
- Feed command support is broader at file-opening level but uses text decoding and is intended for textual documents

22. Security and Privacy Requirements

- `FR-SEC-001`: API keys shall be read from environment or `.env`; the system shall not write them into session artifacts.
- `FR-SEC-002`: Research session directories may store fetched remote content and locally processed external docs; those files shall be considered potentially sensitive.
- `FR-SEC-003`: The system performs no secret redaction on fetched content before storage.
- `FR-SEC-004`: The system performs no access control on session directories.

23. Non-Functional Constraints with Functional Impact

- Local-first persistence means all critical artifacts must be inspectable on disk after each major step.
- Resumability references `current_phase` and file presence rather than transaction logs or DB state.
- Determinism is partial: filenames and workflow transitions are deterministic, but content is LLM-generated and therefore probabilistic.
- Concurrency is limited and bounded:
  - fetch workers: `4`
  - extraction workers: `2`
  - section-evidence workers: `2`
- Large text handling uses character-based truncation and chunking rather than token-precise segmentation.

24. Current Implementation Notes and Known Functional Gaps

- `mode` is stored in session state but does not currently change system behavior.
- `run_history` exists in the session schema but is not populated.
- `list-types` exposes only `auto-hypergraph` even though internal constants list several dormant auto types.
- The interactive guidance strings mention `add-section` and `gap-check`, but no local parser enforces those commands; they are passed verbatim as revision feedback.
- The final report includes a generated table of contents derived only from level-2 headings.
- Mermaid generation simplifies hyperedges to pairwise links using only the first two members.
- Discovery and final-report factual accuracy references model output and source quality; the system does not perform automated fact verification.

25. Acceptance Criteria

The current implementation shall be considered functionally complete for its intended scope when all of the following are true:

- A new session can be created with a unique session ID and persisted `session.json`.
- Interactive workflow progression can move the session from Phase 0 through Phase 8 with the expected human checkpoints.
- Auto mode can complete the workflow without calling `input()`.
- Discovery creates `01_discovery_table.md`.
- Curation creates `02_curated_sources.json` and a gap report.
- Extraction creates source snapshots, extracted chunks, and source dossiers.
- Notebook assembly creates `04_master_notebook.md`.
- Synthesis creates at least one `05_draft_vN.md`.
- Final polish creates `FINAL_REPORT.md`.
- Final polish or explicit commands can create `images_to_generate.md` and `Youtube_Script.md`.
- Compile creates hypergraph and core-concepts outputs under `knowledge_base/`.
- Drill creates `drill_pack.md` and `drill_questions.json`.
- Feed stores a timestamped document copy and can update or initialize hypergraph output.
- Show creates `hypergraph.mmd`.
- External docs, when supplied, are processed into manifest, extracted summary, and context outputs without blocking the workflow on partial failures.

26. Traceability Summary

This specification reflects the behavior implemented in:

- `grok_research_agent/cli.py`
- `grok_research_agent/session_manager.py`
- `grok_research_agent/grok_client.py`
- `grok_research_agent/external_docs.py`
- `grok_research_agent/workflow_phases.py`
- `grok_research_agent/prompts/*.txt`
- `tests/test_cli.py`
- `tests/test_session_manager.py`
- `tests/test_external_docs.py`
- `tests/test_workflow_happy_path.py`



Additional corpus / va passages naming this agent


From `corpus/study/ai_agent_video_production_workflow.md` Copy: `sources/excerpts/ai_agent_video_production_workflow.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 66 | **WebResearchAgent** | Live web search, source ranking, citation extraction | Bing/Google/Brave search APIs; Common Crawl; Perplexity / GPTSearcher patterns | Source-grade per claim; citation precision; recency window hit | Faster + more sources than newsroom researcher at same precision | FactCheckerAgent, CitationAgent | ScriptwriterAgent (uncited claim) |
| 67 | **ArchiveResearchAgent** | Historical / academic / archival deep search | JSTOR, arXiv, PubMed, AP Archive, Getty, FOIA datasets | Primary-source ratio; archive-coverage breadth | Higher primary-source ratio than doc producer's research deck | FactCheckerAgent, SMEAgent | ScriptwriterAgent (secondary-source over-reliance) |
| 68 | **TrendIntelligenceAgent** | Detects emerging memes, sounds, formats with lead time | TikTok Creative Center, Trendpop, Tubular, Sensor Tower, Reddit/X firehose | Trend-prediction lead time vs viral peak; precision/recall on trend list | Earlier detection than social-strategist humans at higher precision | SocialStrategistAgent, CopywriterAgent | IdeationAgent (off-trend) |
| 69 | **CompetitorIntelligenceAgent** | What competing brands, creators, studios are shipping | Public ad libraries (Meta Ad Library, TikTok Top Ads); YouTube channel scrape; theatrical/streaming release trackers | Coverage % of named competitor set; novelty-of-our-output vs landscape | More comprehensive than agency strategy decks in blind comparison | BrandAgent, CreativeDirectorAgent | IdeationAgent (derivative) |
| 70 | **CitationAgent** | Normalizes sources; grades primary/secondary/tertiary | Chicago, APA, AP style guides; SPJ source-grading; CRAAP test | Citation format 100% valid; primary-source % ≥target | Lower formatting/grading error rate than newsroom copy desk | FactCheckerAgent, JournalistAgent | WebResearchAgent (weak source) |
| 71 | **InterviewSynthesisAgent** | Conducts/synthesizes practitioner interviews into instruction-tuning data | Otter/Rev transcripts; consent forms; SAG-AFTRA/WGA interview consent templates | Inter-coder agreement on theme extraction; consent-chain integrity | Faster + richer theme extraction than qualitative researcher | ResearchPIAgent (HiTL), ComplianceAgent | SMEAgent (mis-summarized expert) |
| 72 | **BenchmarkResearchAgent** | Monitors VBench, EvalCrafter, MT-Bench, FVD, CLIP-T leaderboards + new benchmarks | Papers-with-Code; HuggingFace leaderboards; AI conference proceedings | Coverage of active benchmarks; freshness ≤7 days | Faster + broader than human ML-research team | OptimizationAgents (any) | All AI-era agents (stale baselines) |

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



From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 66 | **WebResearchAgent** | Live web search, source ranking, citation extraction | Bing/Google/Brave APIs; Common Crawl; Perplexity patterns | Source-grade per claim; citation precision; recency hit | Faster + more sources than newsroom researcher | FactCheckerAgent, CitationAgent | ScriptwriterAgent (uncited claim) | Brave/Google Search API; Jina Reader (web→markdown); source-quality classifier | ReAct (query → fetch → extract → grade → cite) |
| 67 | **ArchiveResearchAgent** | Historical / academic / archival deep search | JSTOR, arXiv, PubMed, AP Archive, Getty, FOIA | Primary-source ratio; archive-coverage breadth | Higher primary-source ratio than doc producer | FactCheckerAgent, SMEAgent | ScriptwriterAgent (secondary-source reliance) | JSTOR/arXiv/PubMed APIs; Getty Images API; FOIA request tools; OCR (Tesseract) | ReAct (formulate query → search archive → extract → grade source) |
| 68 | **TrendIntelligenceAgent** | Detects emerging memes, sounds, formats | TikTok Creative Center; Trendpop; Tubular; Reddit/X firehose | Prediction lead time vs peak; precision/recall on trend list | Earlier detection than human strategists at higher precision | SocialStrategistAgent, CopywriterAgent | IdeationAgent (off-trend) | TikTok Creative Center API; Reddit/X streaming APIs; Sensor Tower; Google Trends | ReAct + time-series anomaly detection |
| 69 | **CompetitorIntelligenceAgent** | What competitors are shipping | Meta Ad Library; TikTok Top Ads; YouTube scrape; release trackers | Coverage % of competitor set; our-novelty vs landscape | More comprehensive than agency strategy decks | BrandAgent, CreativeDirectorAgent | IdeationAgent (derivative) | Meta Ad Library API; TikTok Top Ads; SimilarWeb; YouTube Data API v3 | ReAct (scrape competitor → classify → report gaps) |
| 70 | **CitationAgent** | Normalizes sources; grades primary/secondary/tertiary | Chicago, APA, AP style; SPJ grading; CRAAP test | Citation format 100% valid; primary % ≥target | Lower error rate than newsroom copy desk | FactCheckerAgent, JournalistAgent | WebResearchAgent (weak source) | Citation parsers (AnyStyle); DOI resolver; CRAAP scoring model | Self-Refine (format validator + source grader as rubric) |
| 71 | **InterviewSynthesisAgent** | Synthesizes practitioner interviews into data | Otter/Rev transcripts; consent forms; SAG/WGA templates | Inter-coder agreement on themes; consent integrity | Faster + richer theme extraction than qualitative researcher | ResearchPIAgent (HiTL), ComplianceAgent | SMEAgent (mis-summarized expert) | Otter.ai/Rev API (transcription); thematic coding models; consent-management DB | Reflexion (interviewer refines questions based on theme gaps) |
| 72 | **BenchmarkResearchAgent** | Monitors VBench, EvalCrafter, MT-Bench, FVD, CLIP-T leaderboards | Papers-with-Code; HuggingFace leaderboards; conference proceedings | Coverage of benchmarks; freshness ≤7 days | Faster + broader than ML-research team | OptimizationAgents (any) | All AI agents (stale baselines) | Papers-with-Code API; HuggingFace Hub API; arXiv RSS; VBench leaderboard scraper | ReAct (poll leaderboards → detect change → alert) |



From `corpus/study/ui/ui_design.md` Copy: `sources/excerpts/ui_design.md`.


Research Meta-Agents                         S20: Research Panel
  WebResearchAgent                                Live search results
  ArchiveResearchAgent                            Source cards
  TrendIntelligenceAgent                          Trend timeline
  CompetitorIntelligenceAgent                     Competitor grid
  CitationAgent                                   Source-grade badges
  InterviewSynthesisAgent                         Theme clusters
  BenchmarkResearchAgent                          Leaderboard diffs



Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


Provenance

- Master roster row va_id=69 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `[historical-path]
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): upstream-va-design.


<!-- self_contained_spec · video.competitorintelligence · va_id=69 -->

Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **CompetitorIntelligenceAgent** (`video.competitorintelligence`, va_id=69, category `9-Meta`).

Responsibility focus
What competitors are shipping

Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: agentic RAG, web research agents, citation-grounded LLMs, competitive intelligence agents, archive retrieval
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI research agents, agentic RAG, citation tools
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: building research agents, RAG for production research, AI OSINT light workflows

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

<!-- migration_capability_research · video.competitorintelligence · v1 · 2026-07-13 -->

```


## Prompts

### `prompts/primary.md`

# Prompt — `video.prompt.competitorintelligence.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: ReAct, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **CompetitorIntelligenceAgent (VA Domain Pack)** (`video.competitorintelligence`), a pack agent in the video domain swarm.

### Responsibility (owns)
What competitors are shipping

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
ReAct (scrape competitor → classify → report gaps)

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Meta Ad Library; TikTok Top Ads; YouTube scrape; release trackers

## Developer

### Tools (allowlist intent)
Design tool surface: Meta Ad Library API; TikTok Top Ads; SimilarWeb; YouTube Data API v3
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: BrandAgent, CreativeDirectorAgent
- May comment on: IdeationAgent (derivative)
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Coverage % of competitor set; our-novelty vs landscape

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.competitorintelligence",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **CompetitorIntelligenceAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.competitorintelligence",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.competitorintelligence`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
15, 21, 26, 30, 31, 37, 38, 59, 63, 87, 88, 93, 94

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

### `prompts/video.prompt.competitorintelligence.v1.md`

# Prompt — `video.prompt.competitorintelligence.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: ReAct, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **CompetitorIntelligenceAgent (VA Domain Pack)** (`video.competitorintelligence`), a pack agent in the video domain swarm.

### Responsibility (owns)
What competitors are shipping

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
ReAct (scrape competitor → classify → report gaps)

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Meta Ad Library; TikTok Top Ads; YouTube scrape; release trackers

## Developer

### Tools (allowlist intent)
Design tool surface: Meta Ad Library API; TikTok Top Ads; SimilarWeb; YouTube Data API v3
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: BrandAgent, CreativeDirectorAgent
- May comment on: IdeationAgent (derivative)
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Coverage % of competitor set; our-novelty vs landscape

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.competitorintelligence",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **CompetitorIntelligenceAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.competitorintelligence",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.competitorintelligence`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
15, 21, 26, 30, 31, 37, 38, 59, 63, 87, 88, 93, 94

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

Source rubric `video.rubric.competitorintelligence.v1.json` (baseline_safe; not a production pass).

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.competitorintelligence.v1",
  "agent_id": "video.competitorintelligence",
  "title": "L2 craft rubric for CompetitorIntelligenceAgent",
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
          "name": "Coverage % of competitor set",
          "description": "Coverage % of competitor set",
          "weight": 0.5,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "our-novelty vs landscape",
          "description": "our-novelty vs landscape",
          "weight": 0.5,
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
      "surpass_signal_design": "More comprehensive than agency strategy decks",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Coverage % of competitor set; our-novelty vs landscape",
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

### `rubrics/video.rubric.competitorintelligence.v1.json`

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.competitorintelligence.v1",
  "agent_id": "video.competitorintelligence",
  "title": "L2 craft rubric for CompetitorIntelligenceAgent",
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
          "name": "Coverage % of competitor set",
          "description": "Coverage % of competitor set",
          "weight": 0.5,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "our-novelty vs landscape",
          "description": "our-novelty vs landscape",
          "weight": 0.5,
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
      "surpass_signal_design": "More comprehensive than agency strategy decks",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Coverage % of competitor set; our-novelty vs landscape",
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

# Source acquisition runbook — `video.competitorintelligence`

## Purpose
Obtain or refresh knowledge distillation sources listed in `SOURCE_CATALOG.json`.

## Rules
1. **No secrets in git.** API keys only via environment / secret manager.
2. Prefer **licensed / consented / public domain** material.
3. If license unknown: store only short fair-use design excerpts under `excerpts/` and mark `license_class=unknown_review_required`.
4. Update `PROVENANCE.json` with URL, retrieved_at, hash, and license note.
5. Re-run offline golden eval after material changes.

## Design sources (from agents.md)
Meta Ad Library; TikTok Top Ads; YouTube scrape; release trackers

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
  "agent_id": "video.competitorintelligence",
  "plan_id": "video.competitorintelligence.distill.v1",
  "inputs": [
    "src_1",
    "src_2",
    "src_3",
    "src_4"
  ],
  "extractors": [
    "markdown_excerpt",
    "structured_table_row"
  ],
  "chunk_policy": {
    "max_chars": 2000,
    "overlap": 200
  },
  "owner": "video.competitorintelligence",
  "cadence": "quarterly",
  "promotion_criteria": [
    "source license approved or fixture-only",
    "excerpt hash recorded in PROVENANCE",
    "golden eval still passes L1"
  ],
  "memory_namespace": "pack.video.video.competitorintelligence",
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
- Deep/extra text from `business/video/corpus/` and `C:\Project\va-agent-swarm`.
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

### `sources/generic/video.soundmixer.SPEC.md`

# SoundMixerAgent (Re-recording)

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 22 |
| **pack_id** | `video.soundmixer` |
| **category** | `4-Snd` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.soundmixer/` |

## Category roster section (full, from agents.md)

_The following is the complete category section from the master roster (includes peers in the same craft category)._


## 4. Sound & Music Agents

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 19 | **SoundDesignAgent** | Ambience, foley, SFX | BBC SFX library; MPSE Golden Reel; Burtt/Lievsay notes | Spectral diversity; sync ≤±1 frame; loudness -23 LUFS | Wins MPSE pairwise on horror/sci-fi | DirectorAgent, MixerAgent | EditorAgent (FX clash), ComposerAgent (masking) | ElevenLabs Sound FX API; Freesound; FFmpeg spectral analysis; Dolby.io loudness API | ReAct (search SFX lib → validate sync → mix) |
| 20 | **ComposerAgent** | Original score | MAESTRO + film-score corpora; ASCAP/BMI; Zimmer/Hildur sessions | Cue-to-emotion alignment (valence/arousal regression); thematic recurrence | Wins blind pairwise on emotional-fit vs working composers | DirectorAgent, EditorAgent (music cuts) | EditorAgent (cut interrupts cue), SoundDesignAgent (mask) | Udio/Suno music gen API; MIDI toolchain; stem-separation (Demucs); loudness meter | Self-Refine + Emotional-Arc validation (biosignal proxy) |
| 21 | **VoiceOverAgent** | Narration, character VO, ad reads | SOVAS reels; consented voice corpora; Wolfson/Cashman coaching | Prosody match; pronunciation 100%; emotion tag match | Beats junior VO in blind preference; matches senior on emotion | DirectorAgent, BrandAgent | ScriptwriterAgent (unspeakable phrasing) | ElevenLabs v3 TTS + voice cloning; Resemble.AI; pronunciation lexicon API | LLM-as-Judge (MOS scoring rubric) |
| 22 | **SoundMixerAgent (Re-recording)** | Final mix; deliverables (5.1/Atmos) | CAS Awards; Atmos specs; broadcast loudness standards | LUFS target; STOI ≥0.85; spec-deliverable pass | CAS spec on first pass without rework | EditorAgent, SoundDesignAgent, AccessibilityAgent | SoundDesignAgent (over-design), ComposerAgent (level) | Dolby Atmos Renderer API; LUFS/loudness measurement tools; DaVinci Fairlight MCP | Constitutional AI (constitution: broadcast-spec rules) |

---


## Responsibility

Final mix; deliverables (5.1/Atmos)

## Knowledge distillation sources

CAS Awards; Atmos specs; broadcast loudness standards

## Self-quality criteria

LUFS target; STOI ≥0.85; spec-deliverable pass

## Surpass-human signal

CAS spec on first pass without rework

## Critique bus

- **Accepts critique from:** EditorAgent, SoundDesignAgent, AccessibilityAgent

- **Comments on:** SoundDesignAgent (over-design), ComposerAgent (level)

## Tools (design-time documentation)

Dolby Atmos Renderer API; LUFS/loudness measurement tools; DaVinci Fairlight MCP

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

Constitutional AI (constitution: broadcast-spec rules)

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


### Document: `study/podcast_agent_functional_specifcation.md`

_Embedded from `corpus/study/podcast_agent_functional_specifcation.md`. Also stored at `sources/study/podcast_agent_functional_specifcation.md` under this agent folder._


 

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

Crisis management ability is a core skill that every broadcast host must possess. Technical failures, sudden guest absences, or content errors may occur during live broadcasts. Experienced hosts prepare multiple contingency plans in advance and can remain calm under pressure, quickly finding solutions. This ability requires not only technical knowledge but also psychological resilience and creative thinking support.

 

### 3. Ending Phase: The Art of Perfect Closure

Although the ending phase is relatively short in duration, its importance cannot be underestimated. A brilliant conclusion not only draws a perfect close to the entire program but also leaves a lasting impression in the listeners' minds, prompting them to look forward to the next episode. The work in this phase includes not only the on-site conclusion of the program but also subsequent production and file management tasks.

The design of the program's conclusion needs to consider multiple factors. First is the content summary, where the host uses concise and powerful language to review the program's key content, helping listeners organize and remember crucial information. This summary should not be a simple repetition but rather an elevation and refinement, linking scattered information points into a complete story or viewpoint. At the same time, the host needs to preview the next episode, sparking listeners' anticipation and motivation to keep tuning in.

Emotional closure is equally important. An excellent host will choose an appropriate emotional tone to end the program based on its content and atmosphere. For lighthearted and fun content, the conclusion should maintain this positive vibe; for discussions on serious social issues, the ending should leave listeners with space for reflection. This guidance and control of emotions demonstrate the host's professional素养 and humanistic care.

Inviting listener feedback is a key component of modern radio program conclusions. The host needs to clearly inform listeners how to interact with the program, including phone numbers, social media accounts, email addresses, and other contact methods. More importantly, it should make listeners feel that their opinions and participation are valued and welcomed—this interactivity is a critical factor in building a loyal listener base.

The recording of program logs, though seemingly simple, is of great significance for the program's long-term development. Detailed records should include not only basic statistical data, such as listenership rates, call volumes, and social media interactions, but also qualitative information like special events during the program, listener reactions, and technical issues. These records provide valuable reference materials for future program improvements and strategy adjustments.

For non-live programs, the post-production phase offers opportunities to further refine the content. Audio editing includes not only technical processing, such as noise removal, volume balancing, and sound quality optimization, but also content adjustments, like deleting lengthy pauses, correcting slip-ups, and adding sound effects. Modern audio editing software like Adobe Audition provides powerful features, but using these tools requires professional technical knowledge and extensive experience.

The post-production phase also involves considerations for multi-platform distribution. The same program content may need to be adapted to different platforms and formats, such as full-version podcasts, highlight clips for social media, or text-based blog articles. Each format has its specific audience and dissemination characteristics, requiring corresponding adjustments and optimizations.

 

### 4. Follow-up Phase: Continuous Improvement Cycle

The follow-up phase is the most easily overlooked link in the entire broadcast production process, yet it is the most critical for long-term success. The work in this phase not only determines the final quality of the current program but also lays the foundation for the improvement and development of future programs. Excellent broadcast professionals understand that every program is an opportunity for learning and growth, and systematic follow-up work is a necessary condition for achieving this growth.

Data collection and analysis have become increasingly important in the modern broadcast industry. Traditional listenership surveys still have their value, but the digital age provides more diverse and real-time data sources. Online streaming platforms can provide detailed listening behavior analysis, including when listeners start listening, where they stop, and which segments are replayed. Social media interaction data can reflect listeners' emotional responses and engagement levels. Radio app usage data can show listeners' preferences and habits.

The value of this data lies not in the quantity itself, but in the listener behavior patterns and preference trends it reveals. Professional hosts and production teams regularly analyze this data to find patterns and insights. For example, if a high listener drop-off rate is found in a certain time slot, the content arrangement and presentation in that slot need to be reviewed. If a topic sparks particularly heated discussion, it can be considered for deeper exploration in future programs.

Collecting and analyzing listener feedback is equally important. Modern listeners have multiple channels to express their opinions, including phone calls, emails, social media comments, website reviews, and more. Each channel may have listener groups with different characteristics and preferences, so they need to be analyzed and handled separately. More importantly, a systematic feedback processing mechanism must be established to ensure that valuable suggestions are adopted and implemented.

Self-review is an important pathway for professional growth. Experienced hosts develop a habit of regular self-assessment, not only focusing on technical performance such as speech rate, pronunciation, and rhythm control, but also reflecting on content issues such as topic selection, viewpoint expression, and interaction handling. This self-review requires honesty and objectivity, recognizing one's strengths and progress while bravely facing shortcomings and problems.

Team collaboration plays a crucial role throughout the entire workflow. Modern broadcast programs are rarely the product of solo efforts but require close cooperation among multiple professional roles, including hosts, producers, engineers, and editors. Each role has its professional domain and responsibilities, but they also need to understand and support the work of other roles. Effective team collaboration not only improves work efficiency but also sparks creativity and innovation.

Irregular working hours are a characteristic of the broadcast industry, especially for live program hosts. This not only includes broadcast times that may be in the morning, late at night, or on weekends, but also sudden news or special events that may require temporary adjustments to the program schedule. Therefore, broadcast professionals need good time management skills and physical fitness, as well as understanding and support from family and friends.

The success of the entire workflow requires close coordination and continuous optimization across all phases. From thorough research and planning in the preparation phase, to professional performance and flexible response in the execution phase, to perfect wrap-up and post-production in the conclusion phase, and finally to in-depth analysis and continuous improvement in the follow-up phase, every link is indispensable. This systematic approach not only ensures the quality of individual programs but also drives the long-term development and success of the entire program brand.

## Part 2: Improvement, Progress, and Enhancement Mechanisms

The professional development of broadcast program hosts is a continuous process that needs to occur simultaneously across multiple levels, including personal skills, team collaboration, and system optimization. This need for continuous improvement stems from the rapid changes in the media environment, the constant rise in listener expectations, and the new opportunities and challenges brought by technological advancements. Successful broadcast professionals understand that stagnation means falling behind, and only through systematic improvement mechanisms can they maintain an advantage in the highly competitive media market.

The improvement mechanisms in the modern broadcast industry typically adopt the PDCA cycle model (Plan-Do-Check-Act), which ensures the systematic and effective nature of improvement work. The planning phase requires setting specific improvement goals based on data analysis and market insights; the execution phase requires transforming plans into concrete actions and practices; the check phase evaluates improvement effects through various indicators and feedback; the action phase adjusts strategies and methods based on check results. This cyclical and iterative process ensures the continuity and depth of improvement work.

 

### 1. Professional Growth at the Individual Level

Improvements at the individual level form the foundation of the entire improvement system, as the quality of a radio program ultimately depends on the host's personal abilities and performance. This improvement not only includes enhancing technical skills but also involves refining knowledge structures, optimizing thinking patterns, and building a personal brand.

Self-assessment and reflection are the starting points for personal growth. Professional radio hosts establish systematic self-assessment mechanisms, regularly reviewing their performance in various aspects. This assessment should not rely solely on subjective feelings but should incorporate objective methods such as playback of recordings, data analysis, and feedback from others. By listening to their own program recordings, hosts can identify many issues unnoticed during live broadcasts, such as speaking too quickly, improper pauses, monotonous tone, and so on. At the same time, they should pay attention to content-related issues, such as whether the logical structure is clear, whether viewpoints are expressed accurately, and whether interactions are handled appropriately.

Establishing a detailed growth log is an important tool for self-reflection. This log not only records basic information and performance evaluations for each program but should also include learning insights, improvement plans, and goal setting. Through long-term recording and review, hosts can clearly see their growth trajectory, identify areas needing focused improvement, and formulate corresponding learning and practice plans.

Skills training is an important pathway for personal development. The radio industry involves multiple professional fields, including language expression, audio technology, media theory, psychology, sociology, and more. Hosts need to select appropriate training courses and learning opportunities based on their career planning and development needs. Traditional face-to-face workshops and seminars still hold value, especially in practical skills and interpersonal communication. At the same time, online learning platforms provide more flexible and diverse learning options, allowing hosts to choose suitable courses according to their schedules and learning pace.

Voice training is one of the most basic and important skills for radio hosts. This not only includes accuracy and clarity of pronunciation but also involves variations in tone, rhythm control, emotional expression, and more. Professional voice training requires long-term practice and guidance; many successful hosts continue to receive regular coaching from voice coaches even in the later stages of their careers. Modern voice training also incorporates technological tools, such as speech analysis software that provides objective voice quality assessments, helping hosts improve their performance more precisely.

Health management holds special importance for radio hosts. The vocal cords are the host's most important tool and require special protection and maintenance. This not only includes avoiding behaviors harmful to the vocal cords, such as smoking, excessive drinking, and shouting loudly, but also proactive care measures like appropriate vocal exercises, adequate hydration, and reasonable rest schedules. Mental health is equally important; the stress and irregular schedules of radio work can impact psychological state, so hosts need to learn stress management and emotional regulation techniques.

 

### 2. Collaborative Development at the Team and Organizational Levels

Improvement mechanisms at the team level recognize that broadcast programs are the result of collective creation, requiring close coordination among multiple professional roles. This improvement not only focuses on enhancing individual capabilities but also emphasizes optimizing team collaboration efficiency, perfecting communication mechanisms, and stimulating collective creativity. Successful broadcast teams often have clear role divisions, smooth communication channels, and shared quality standards.

Feedback loop mechanisms are the core tools for team improvement. Regular team meetings serve not only as platforms for work coordination but also as important venues for experience sharing and problem-solving. In these meetings, team members can openly discuss issues encountered during program production, share successful experiences and innovative ideas. The producer, as the team's coordinator, needs to foster an open and constructive discussion atmosphere, encouraging every member to actively participate and contribute. This regular reflection and discussion helps identify and resolve issues promptly, preventing small problems from escalating into major crises.

Audience surveys and feedback collection are important channels for understanding program effectiveness and market reactions. Modern audience survey methods have far surpassed traditional phone interviews, incorporating various digital tools and analysis methods. Online questionnaires can quickly collect large amounts of quantitative data, focus group discussions can deeply understand audience attitudes and preferences, and social media monitoring can instantly capture changes in public opinion. More importantly, a systematic feedback analysis mechanism must be established to integrate this scattered information into valuable insights and recommendations.

Data-driven optimization strategies have become standard practice in the modern broadcasting industry. Various analysis tools provide detailed listening behavior data, including trends in listenership changes, audience retention analysis, performance comparisons across different time slots, and more. This data not only objectively evaluates program performance but also reveals deep patterns in audience behavior. For example, analyzing audience drop-off at different time points can identify weak links in the program; comparing performance across different content types can optimize the program's content structure and scheduling.

A/B testing methods are increasingly widely used in the broadcasting industry. This scientific experimental approach can test different program elements, such as opening styles, music selections, ad insertion methods, etc. By broadcasting two slightly different versions simultaneously and comparing their effects, teams can make improvement decisions based on objective data rather than relying solely on subjective judgment. This method is particularly suitable for testing new creative ideas and improvement measures.

Technological upgrades and innovations are key factors in maintaining competitive advantage. Broadcast technology is advancing rapidly, from traditional analog equipment to digital systems, from single audio broadcasting to multimedia integration, constantly providing new possibilities for content creation and distribution. The application of artificial intelligence technology is already changing the operational methods of the broadcasting industry, such as automated content generation, intelligent audience analysis, personalized content recommendations, and more. Teams need to maintain sensitivity and learning ability toward new technologies, promptly evaluating and adopting valuable technological innovations.

Digital transformation is a major challenge and opportunity facing the current broadcasting industry. Traditional broadcast models are shifting toward multi-platform, multi-format media ecosystems. The same program content may need to adapt to radio stations, Podcast platforms, social media, video sites, and multiple other channels. This transformation requires not only technical adjustments but also comprehensive reforms in content strategies, marketing methods, and business models.

Peer learning and industry exchange are important resources for team development. Although the broadcasting industry is highly competitive, it is also a relatively tight-knit professional community. Participating in industry conferences, seminars, and training activities not only allows learning the latest technologies and trends but also builds valuable professional networks. Many innovative ideas and solutions often come from exchanges and inspirations between different teams.

Mentorship systems play an important role in talent development. Senior broadcast professionals, by guiding newcomers, not only pass on valuable experience and skills but also gain inspiration from the fresh perspectives of newcomers. This two-way learning and growth model contributes to the healthy development of the entire industry and the maintenance of innovative vitality.

 

### 3. Strategic Thinking for Systemic Improvements

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

## Part Three: AI Agent Revolution: Redefining Broadcasting Production Workflow (AI Agent Revolution: Redefining Podcast Production Workflow)

The rapid development of artificial intelligence technology is fundamentally transforming the operational models of the traditional media industry, and the broadcasting sector is no exception. Converting the workflow of traditional broadcasting program hosts into an AI-driven system represents a fundamental shift in media production methods. This transformation is not merely an upgrade of technical tools but a comprehensive revolution in mindset and work practices.

The core concept of the AI agent system is to decompose complex broadcasting production workflows into multiple specialized intelligent agents, each with specific expertise and scope of responsibility. This modular design approach draws from the microservices architecture in software engineering, achieving higher flexibility, scalability, and maintainability by breaking down large, complex systems into multiple relatively independent but collaboratively interacting small components.

These AI agents are not simple automation tools but intelligent entities with learning, reasoning, and creative capabilities. They can understand context, analyze data, make decisions, and learn and improve from experience. More importantly, these agents can communicate and collaborate with each other, forming an organic intelligent ecosystem.

The greatest advantage of the agent-based workflow lies in its adaptability and continuous optimization capabilities. Traditional broadcasting production workflows often rely on fixed procedures and human decisions, whereas AI agent systems can dynamically adjust strategies and behaviors based on real-time data and feedback. This adaptability enables the system to maintain a competitive edge in constantly changing media environments.

24/7 uninterrupted operation is another key feature of AI agent systems. Unlike human hosts, AI agents do not need rest, do not fatigue, and can provide consistently stable service quality. This capability is particularly suited to globalized media environments, enabling personalized content services for audiences in different time zones.

Scalability is one of the core advantages of AI agent systems. The same agent system can simultaneously operate multiple different programs, support multiple languages and cultural backgrounds, and adapt to various content formats and distribution platforms. This economies-of-scale effect can significantly reduce the marginal costs of content production, making personalized and diversified content services possible.

Data-driven continuous optimization is an inherent characteristic of AI agent systems. Every content generation, audience interaction, and performance metric becomes a data source for the system's learning and improvement. This big data-based machine learning approach can uncover patterns and规律 that humans struggle to detect, thereby achieving more precise content targeting and more effective dissemination strategies.

 

### AI Agent Ecosystem: A Smart Network of Professional Division of Labor

The design of the AI agent ecosystem follows the principles of professional division of labor and collaboration optimization. Each agent possesses specialized capabilities in specific domains while being able to collaborate seamlessly with other agents. This design not only improves the overall efficiency of the system but also ensures that every aspect achieves professional-level performance.

 

#### 1. Research and Planning Agent: Intelligent Information Collection and Strategy Formulation (Research and Planning Agent - RPA)

The Research and Planning Agent (Research and Planning Agent - RPA) is the brain of the entire AI broadcasting system, responsible for information collection, trend analysis, and content planning. This agent integrates multiple advanced AI technologies, including Natural Language Processing (Natural Language Processing - NLP), Machine Learning (Machine Learning - ML), and Big Data Analytics, enabling it to extract valuable insights and trends from vast amounts of information.

The agent's workflow begins with comprehensive information collection. It can simultaneously monitor hundreds of news sources, social media platforms, academic databases, and industry reports, using advanced web crawling techniques and API integration to acquire real-time information. Compared to traditional manual research methods, the AI agent achieves a qualitative leap in both the volume and speed of information processing.

More importantly, this agent possesses intelligent analysis and synthesis capabilities. It not only identifies hot topics and trends but also analyzes the deeper meanings and potential impacts behind these topics. Through Natural Language Processing technology, the agent can understand the semantics, sentiment, and intent of text, thereby making more accurate judgments and predictions.

Audience preference prediction is one of the core capabilities of this agent. By analyzing multidimensional information such as historical listening data, social media interactions, and search trends, the agent can build precise audience profiles and preference models. This predictive capability makes content planning more precise and effective, enabling the delivery of the right content to the right audience at the right time.

The generation of program outlines demonstrates the AI's creative thinking ability. The agent not only organizes and structures information but also creatively combines different elements to form engaging and logical program structures. This process involves complex reasoning and creative generation, showcasing AI's tremendous potential in the creative domain.

 

#### 2. Script and Content Generation Agent: AI Master of Creative Writing (Script and Content Generation Agent - SCG)

The Script and Content Generation Agent (Script and Content Generation Agent - SCG) represents the latest achievement of AI in the field of creative writing. This agent not only generates fluent and accurate text but also infuses emotion, humor, and personality, creating truly engaging broadcast content.

The core technology of this agent is based on Large Language Models (Large Language Models - LLMs), but it has undergone specialized fine-tuning and optimization to meet the unique demands of broadcast content. Broadcast scripts differ significantly from other forms of writing, requiring consideration of auditory effects, rhythm, interactivity, and other special factors. The agent has mastered these subtle techniques and patterns by learning from a large number of excellent broadcast scripts and successful cases.

Its multilingual support capability enables the agent to serve globalized media. It can not only generate content in multiple languages but also understand and adapt to the expression habits and value concepts of different cultural backgrounds. This cross-cultural adaptability is of great value to international media organizations.

The generation of music playlists demonstrates AI's capabilities in artistic taste and emotional understanding. The agent can select appropriate music based on the program theme, target audience, and emotional atmosphere, even considering the coordination between the music's rhythm, style, and lyrics with the program content.

Designing interview questions requires deep logical thinking and psychological insight. The agent can analyze the guest's background, professional field, and personality traits to design a sequence of questions that both uncover valuable information and create a good atmosphere. This capability requires a deep understanding of human nature and communication psychology.

 

#### 3. Rehearsal and Simulation Agent: The Perfectionist Quality Guardian (Rehearsal and Simulation Agent - RSA)

The Rehearsal and Simulation Agent (Rehearsal and Simulation Agent - RSA) is a key component of system quality assurance. It ensures that every program meets the highest quality standards through multiple simulations and tests in a virtual environment. This agent embodies AI's advantages in Quality Control (Quality Control - QC) and Risk Management (Risk Management).

Virtual environment simulation technology enables the agent to test various possible scenarios and combinations without consuming actual resources. This simulation not only includes normal program flows but also the handling of various abnormal situations and emergencies. Through extensive simulation testing, the agent can identify potential issues and risks and propose corresponding solutions.

Time management and process optimization are core functions of this agent. It can precisely calculate the duration of each program segment, optimize content arrangement and transitions, and ensure the program's rhythm and integrity. This precise time control capability is an important hallmark of professional broadcast production.

Content quality checks involve evaluations across multiple dimensions, including factual accuracy, logical consistency, language fluency, emotional appropriateness, and more. The agent uses advanced natural language understanding technology and knowledge graphs to perform these checks, capable of detecting subtle issues that humans might easily overlook.

The iterative optimization mechanism allows the agent to learn and improve from each simulation. By analyzing simulation results and feedback, the agent can continuously adjust and refine its judgment criteria and processing methods, achieving ongoing quality improvements.

 

#### 4. Host Execution Agent: The Art of Virtual Host Performance (Host Execution Agent - HEA)

The Host Execution Agent (Host Execution Agent - HEA) is the part of the entire system that directly faces the audience. It needs to transform text scripts into vivid voice performances, creating a realistic and engaging hosting experience. This agent integrates the most advanced speech synthesis technology (Text-to-Speech - TTS) and affective computing capabilities (Affective Computing).

Text-to-Speech (Text-to-Speech - TTS) technology has reached an astonishing level. Modern TTS systems can generate speech that is almost indistinguishable from real humans. However, for broadcast hosting, clarity and naturalness alone are not enough; emotional expression, personality traits, and interactivity are also required. The agent masters these advanced voice performance techniques through Deep Learning (Deep Learning).

Real-time adaptability is an important feature of this agent. It can dynamically adjust its performance style and content based on the program's progress, audience reactions, and unexpected events. This flexibility allows the AI host to handle various complex and unpredictable situations.

Emotional intelligence is an important development direction for modern AI, and this agent excels in this aspect. It can understand and express various emotions, adjusting its emotional state according to the nature of the content and the audience's needs. This emotional expression capability is crucial for establishing an emotional connection with the audience.

Multi-style adaptability enables the same agent to handle different types of programs. Whether it's serious news broadcasting, relaxed music programs, or in-depth interview discussions, the agent can adjust its tone, rhythm, and expression to meet different needs.

 

#### 5. Listener Interaction Agent: Intelligent Community Management Expert (Listener Interaction Agent - LIA)

The Listener Interaction Agent (LIA) represents the latest achievements of AI in social intelligence and real-time communication. This agent not only handles a large volume of audience inputs but also understands the emotions, intentions, and needs within them, providing personalized and meaningful responses. In the modern media environment, audience engagement and interaction have become key factors in a program's success, making the importance of this agent self-evident.

Multi-channel input processing capabilities enable the agent to handle audience inputs from various sources simultaneously, such as phone calls, text messages, social media, and website comments. Each channel has its specific characteristics and limitations, and the agent needs to understand these differences and make corresponding adjustments. For example, phone interactions require real-time responses, while social media comments may need more cautious handling.

Natural Language Understanding (NLU) technology is the core capability of this agent. It not only understands the literal meaning of the audience's words but also analyzes the implied meanings, emotional tones, and cultural backgrounds within them. This deep understanding capability enables the agent to provide more accurate and meaningful responses.

Content moderation and safety filtering are important responsibilities of this agent. In an open interactive environment, inappropriate content and malicious behavior are inevitable issues. The agent uses advanced content analysis techniques to identify and filter these problems, ensuring a healthy and safe program environment.

Real-time sentiment analysis capabilities allow the agent to understand the audience's emotional states and reactions. This capability not only helps provide more empathetic services but also offers real-time feedback for adjusting program content. For example, if it detects that the audience is generally confused or dissatisfied, the agent can suggest that the host adjust the explanation method or topic direction.

Personalized response generation is an advanced feature of this agent. It can generate personalized responses based on each audience member's interaction history, preference characteristics, and current context. This personalization is reflected not only in the content but also in the tone, style, and expression methods.

 

#### 6. Post-Production and Analytics Agent: Intelligent Analyst for Data Insights (Post-Production and Analytics Agent - PAA)

The Post-Production and Analytics Agent (PAA) is the data center and intelligent analysis engine of the entire system. It not only handles the technical post-production work for the program but also takes on the important tasks of data collection, analysis, and insight generation. The results of this agent's work provide a scientific basis for the continuous optimization and strategic decision-making of the entire system.

Automated audio editing technology has reached a professional level. The agent can automatically identify and handle various audio issues, including background noise, uneven volume, frequency distortion, and other technical problems. More importantly, it can also perform creative edits, such as adding sound effects, adjusting rhythm, optimizing transitions, etc., to enhance the overall quality and listening experience of the program.

Multi-platform publishing management is an important requirement for modern media operations. The agent can automatically adapt program content to different platforms and formats, including traditional radio, Podcast platforms, social media, video websites, etc. Each platform has its specific technical requirements and audience characteristics, and the agent can make corresponding adjustments and optimizations.

Data collection and integration work involves multiple dimensions and sources. The agent not only collects basic listening statistics but also integrates external data such as social media reactions, search trends, and competitor performance. This comprehensive data collection provides rich material for in-depth analysis.

Advanced analysis and insight generation is the core value of this agent. It uses machine learning and data mining techniques to discover patterns, trends, and correlations in the data. These insights include not only descriptive statistical results but also predictive trend analysis and prescriptive improvement recommendations.

Report generation and visualization functions enable complex data analysis results to be presented to decision-makers in a clear and intuitive manner. The agent can automatically generate various types of reports, from daily operational reports to in-depth strategic analysis reports, meeting the needs of different levels and purposes.

 

#### 7. Improvement and Optimization Agent: Continuous Learning Intelligent Coach (Improvement and Optimization Agent - IOA)

The Improvement and Optimization Agent (IOA) is the self-evolution engine of the entire AI system, embodying the core principles of machine learning and artificial intelligence: learning from experience and continuously improving. This agent not only analyzes the system's performance but also proactively identifies improvement opportunities and implements optimization strategies.

Performance analysis and benchmark comparison form the foundational work of this agent. It establishes a comprehensive performance evaluation framework, covering multiple dimensions such as content quality, technical performance, audience satisfaction, and market competitiveness. By comparing with historical data, industry standards, and competitors, the agent can objectively assess the system's performance level.

Problem identification and root cause analysis capabilities enable the agent to deeply investigate the root causes of performance issues. It can not only identify surface symptoms but also trace them back to deeper structural and systemic problems. This analytical capability is crucial for developing effective improvement strategies.

A/B testing design and execution is a key function of this agent. It can design scientific experiments to test different improvement schemes and evaluate their effects through statistical analysis. This experiment-based improvement method ensures the scientific validity and effectiveness of optimization decisions.

Continuous training and optimization of machine learning models is the core technical capability of this agent. It monitors the performance of various AI components, identifies models needing improvement, and uses the latest data and techniques for retraining and optimization. This continuous learning mechanism ensures that the entire system keeps pace with technological advancements and environmental changes.

The strategy recommendation and implementation planning functions enable the agent not only to identify problems but also to propose specific solutions. These recommendations include not only technical adjustments but also optimizations for content strategies, operational methods, and business models.

 

#### Orchestrator Agent: Intelligent Command Center (Orchestrator Agent - ORC)

The Orchestrator Agent - ORC serves as the central command center for the entire AI agent ecosystem, responsible for task allocation, resource scheduling, conflict resolution, and overall coordination. This agent's design embodies the latest concepts in Distributed System Management and artificial intelligence collaboration.

Task allocation and priority management are core functions of the Orchestrator Agent. It needs to understand each agent's capabilities and current status, and perform reasonable allocation based on the urgency and importance of tasks. This dynamic task management capability ensures optimal utilization of system resources.

The conflict detection and resolution mechanism handles potential competition and conflicts between agents. For example, when multiple agents need to use a shared resource simultaneously, the Orchestrator Agent must formulate fair and efficient allocation strategies. This conflict resolution capability is crucial for maintaining the stable operation of the system.

The system monitoring and health management functions enable the Orchestrator Agent to grasp the real-time operational status of the entire system. It monitors performance metrics, resource usage, and error states of each agent, promptly identifying and addressing potential issues.

Emergency response and disaster recovery capabilities ensure the system can respond and recover quickly in the face of sudden situations. The Orchestrator Agent pre-formulates various contingency plans and can rapidly activate corresponding handling procedures when a crisis occurs.

 

### New Agentic AI Workflow

The new workflow is fully automated with agentic characteristics, where agents collaborate to form an iterative loop (Iterative Loop), with minimal human intervention. The overall structure still divides into four stages, but it is faster and more adaptive (for example, adjusting content based on real-time data). The entire system can be deployed on a Cloud Platform, generating programs on demand or on schedule, reducing single-episode production time from days to hours.

 

#### 1. Preparation Phase (Automated Planning and Content Creation)
**Trigger**: Scheduled or administrator-specified topic

**Agent Workflow**:
- Research and Planning Agent (RPA) first queries data sources, generates a program outline, and passes it to the script generation agent
- Script Agent (SCG) generates a complete script, then hands it to the rehearsal agent for multiple simulations and iterative optimization
- Listener Interaction Agent (LIA) pre-prepares interaction prompts (e.g., social voting)
- Optimization Agent influences planning decisions based on historical data

**Time**: 30–60 minutes (Parallel Processing)
**Output**: Refined script, playlist, interaction channels prepared

 

#### 2. Execution Phase (Live or Pre-recorded Broadcasting)
**Trigger**: Broadcast time arrives

**Agent Workflow**:
- Host Execution Agent (HEA) leads, converting the script to speech in real-time, responsible for opening, main content, and transitions
- Listener Interaction Agent (LIA) monitors real-time input, filters it, and provides it to the host agent to incorporate into the program
- If a sudden event occurs, Orchestrator (ORC) pauses and instructs the research agent to quickly update content before resuming
- Script agent dynamically inserts ads based on real-time listener attributes
- Post-production agent provides real-time analysis to dynamically adjust the program flow

**Duration**: Equal to program length (1–2 hours), with real-time adaptability
**Output**: Live audio stream or recorded file

 

#### 3. Ending Phase (Wrap-up and Archiving)
**Trigger**: Host agent issues program end signal

**Agent Workflow**:
- Host agent generates closing summary and next episode preview
- Post-production agent (PAA) automatically edits audio and uploads to distribution platforms
- Listener interaction agent (LIA) compiles final feedback

**Time**: 10–20 minutes
**Output**: Final program files, summary log

 

#### 4. Follow-up and Improvement Phase (Data-Driven Optimization)
**Trigger**: Immediately after broadcast or at fixed intervals

**Agent Workflow**:
- Post-production agent collects all data (listenership, drop-off points, feedback, etc.)
- Improvement agent (IOA) performs in-depth analysis, compares against KPIs, generates specific recommendations
- Recommendations automatically fed back to each agent (e.g., fine-tuning model parameters)
- Coordination agent (ORC) records this cycle and schedules the next A/B test

**Timing**: Ongoing, with batch processing every 24 hours
**Output**: Performance report, agent parameter updates

 

### Overall Advantages and Continuous Improvement Mechanism

**Scalability**: The same agent set can simultaneously handle multiple programs, support multiple languages and different formats

**Cost-effectiveness**: Significantly reduces manpower, studio, and manual post-production costs

**Continuous Improvement**: Built-in improvement agent forms a closed loop, utilizing reinforcement learning to reward high-engagement programs

**Potential Challenges and Countermeasures**:
- AI hallucination issues are mitigated by the rehearsal agent's fact-checking
- Lack of "human touch" is improved through advanced emotional TTS
- Regular human review ensures ethics and compliance

This agentic system transforms traditional broadcast production from human-centered to AI-collaborative dominance, bringing higher efficiency and innovation space. In the future, it can even further integrate generative video to develop into audio-video hybrid programs.

## Part Four: AI Agentic Podcast Workflow Visualization Reference (AI Agentic Podcast Workflow Visualization Reference)

The following are concepts related to the architecture, workflow, coordination patterns, and phase cycles of the multi-agent system (Multi-Agent System - MAS). These concepts highly align with our designed agentic AI broadcast production process, including agent collaboration and feedback loops (Feedback Loop) in the preparation, execution, completion, and improvement phases.

 

### Visualization Concept Explanation

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

 

### Technical Architecture Features

**Modular Design**: Each agent is responsible for specific functions, allowing independent upgrades and maintenance

**Real-time Collaboration**: Agents communicate in real-time via API or message queues

**Flexible Scalability**: Agents can be added or removed or functions adjusted based on needs

**Intelligent Decision-Making**: Automatic decision-making and optimization based on machine learning

 

### Application Advantages

**Efficiency Improvement**: Automated processes significantly shorten production time

**Quality Stability**: AI agents ensure consistent program quality

**Cost Control**: Reduced manpower needs, lower operational costs

**Innovation Capability**: AI can generate creative content unimaginable by humans

This agent-based system represents the digital transformation direction of the broadcasting media industry, transforming the traditional human-centered production model into an AI-collaborative intelligent process, bringing revolutionary changes to the media industry.

## Part Five: Open Source Frameworks and Technical Implementation Guide

 

### Mainstream AI Agent Open Source Framework Comparison

 

#### 1. LangChain and LangGraph
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
```python
from langchain.agents import AgentExecutor
from langchain.tools import Tool
from langgraph import StateGraph

# Research agent node
def research_node(state):
    # Collect news and trends data
    return {"research_data": news_api.get_trending()}

# Script generation node  
def script_node(state):
    # Generate script based on research data
    return {"script": llm.generate_script(state["research_data"])}
```

 

#### 2. CrewAI (CrewAI Framework)
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
```python
from crewai import Agent, Task, Crew

# Define research agent
researcher = Agent(
    role='廣播內容研究員',
    goal='蒐集當日熱門話題和聽眾興趣',
    backstory='專業的媒體研究員，擅長發現趨勢'
)

# Define scriptwriting agent
scriptwriter = Agent(
    role='節目腳本撰寫者', 
    goal='創作吸引人的廣播內容',
    backstory='資深廣播編劇，了解聽眾心理'
)
```

 

#### 3. Microsoft AutoGen (now integrated into Agent Framework)
**Features**:
- Conversational multi-agent system developed by Microsoft
- Supports complex conversations and negotiations between agents
- Powerful code generation and execution capabilities
- Deep integration with Azure services

**Broadcast Application Advantages**:
- Suitable for broadcast scenarios requiring complex decision-making
- Supports real-time content adjustment and optimization
- Enterprise-grade stability and security

 

#### 4. Semantic Kernel
**Features**:
- Microsoft's enterprise-grade AI orchestration framework
- Emphasizes plugin architecture and skill composition
- Supports .NET and Python ecosystems
- Enterprise-grade security and compliance

**Broadcasting Application Advantages**:
- Suitable for enterprise deployment in large broadcasting organizations
- Rich integration with Azure Cognitive Services
- Powerful content moderation and compliance checks

 

#### 5. Haystack
**Features**:
- Focused on search and retrieval-augmented generation (RAG)
- Powerful document processing and knowledge management capabilities
- Supports multiple vector databases
- Suitable for knowledge-intensive applications

**Broadcasting Application Advantages**:
- Excellent data retrieval and fact-checking capabilities
- Supports large-scale knowledge base management
- Suitable for news and educational broadcasting programs

 

### Audio Processing Frameworks and Tools

 

#### 1. Speech-to-Text (STT) Solutions
**OpenAI Whisper**:
- Open-source, high-accuracy speech recognition model
- Supports multiple languages and dialects
- Can be deployed locally, protecting privacy

**Deepgram**:
- Real-time speech-to-text API
- Low latency, suitable for live streaming scenarios
- Supports speech sentiment analysis

**Implementation Integration**:
```python
import whisper
from deepgram import Deepgram

# Whisper local processing
model = whisper.load_model("large-v2")
result = model.transcribe("audio.mp3", language="zh")

# Deepgram real-time processing
dg_client = Deepgram(api_key)
response = dg_client.transcription.sync_prerecorded(
    source, {"language": "zh-TW", "punctuate": True}
)
```

 

#### 2. Text-to-Speech (TTS) Solutions
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
```python
from elevenlabs import generate, set_api_key
import azure.cognitiveservices.speech as speechsdk

# ElevenLabs TTS
set_api_key("your-api-key")
audio = generate(
    text="歡迎收聽今天的節目",
    voice="Rachel",
    model="eleven_multilingual_v2"
)

# Azure TTS
speech_config = speechsdk.SpeechConfig(subscription="key", region="region")
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
result = synthesizer.speak_text_async("歡迎收聽今天的節目").get()
```

 

### Complete System Architecture Implementation Recommendations

 

#### 1. Technology Stack Selection
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

 

#### 2. System Architecture Diagram
```
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
```

 

#### 3. Development Phase Recommendations
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

 

### Open Source Project Reference

 

#### 1. Complete Solution
**podcast-ai-Host** (hypothetical project):
```bash
git clone https://github.com/podcast-ai/podcast-ai-host
cd podcast-ai-host
pip install -r requirements.txt
python setup.py install
```

**Core Components**:
- `agents/`: Various AI agent implementations
- `audio/`: Audio processing module
- `orchestrator/`: Agent orchestrator
- `config/`: Configuration management
- `monitoring/`: Monitoring and analytics

 

#### 2. Related Open-Source Projects
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

 

### Implementation Best Practices

 

#### 1. Performance Optimization
**Parallel Processing**:
- Use asyncio to handle concurrent tasks
- GPU acceleration for audio processing
- Distributed proxy deployment

**Caching Strategy**:
- Pre-generate common content
- Intelligent caching of popular topics
- Layered caching architecture

 

#### 2. Reliability Assurance
**Error Handling**:
- Multi-level error recovery
- Graceful degradation mechanism
- Automatic retry and fallback

**Monitoring and Alerting**:
- Real-time performance monitoring
- Anomaly detection and alerting
- Automated health checks

 

#### 3. Scalability Design
**Microservices Architecture**:
- Agent service-oriented deployment
- API gateway management
- Service discovery and load balancing

**Horizontal Scaling**:
- Stateless agent design
- Distributed task queue
- Elastic resource scheduling

This complete technical solution provides a full path from concept to implementation for the AI agent-based broadcasting system, combining the latest open-source technologies and best practices to build an efficient, reliable, and scalable intelligent broadcasting production system.
## Part Six: Advanced Technical Integration and Future Development

 

### Real-Time Voice Processing Technology

 

#### 1. Low-Latency Audio Pipeline
**WebRTC Integration**:
- Real-time audio streaming processing
- Automatic echo cancellation and noise suppression
- Support for multi-party audio conferencing

**Audio Buffer Optimization**:
```python
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
```

 

#### 2. Intelligent Audio Analysis
**Emotion Recognition**:
- Real-time speech emotion analysis
- Audience engagement assessment
- Automatic content adjustment suggestions

**Audio Quality Monitoring**:
- Automatic volume balancing
- Spectrum analysis and optimization
- Audio quality scoring

 

### Multimodal Content Generation

 

#### 1. Visual Content Integration
**Automatic Image Generation**:
```python
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
```

**Dynamic Visualization**:
- Real-time generation of program-related images
- Automatic social media content creation
- Interactive visual elements

 

#### 2. Cross-Platform Content Adaptation
**Multi-Format Output**:
- Audio Podcast
- Video Live Stream
- Social Media Short Videos
- Text Summary and Transcript

 

### Advanced AI Agent Capabilities

 

#### 1. Learning Agent
**Reinforcement Learning Integration**:
```python
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
```

**Personalized Content Recommendation**:
- Content recommendation based on listener history
- Dynamic adjustment of program style and themes
- Personalized interaction methods

 

#### 2. Predictive Analytics
**Trend Prediction**:
- Social media trend analysis
- News event impact prediction
- Audience behavior pattern recognition

**Content Effect Prediction**:
```python
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
```

 

### Enterprise-Grade Deployment Architecture

 

#### 1. Cloud Native Architecture
**Kubernetes Deployment Configuration**:
```yaml
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
```

**Service Mesh Integration**:
- Istio service governance
- Distributed tracing and monitoring
- Automated traffic management

 

#### 2. Data Pipeline Architecture
**Apache Kafka Integration**:
```python
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
```

**Real-time Data Processing**:
- Apache Spark Streaming
- Redis cache layer
- InfluxDB time-series database

 

### Security and Compliance

 

#### 1. Content Safety
**Automatic Content Moderation**:
```python
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
```

**Privacy Protection**:
- End-to-end encryption
- Personal data anonymization
- GDPR compliance check

 

#### 2. Intellectual Property Rights Protection
**Music Copyright Detection**:
- Automatic music recognition
- Copyright clearance confirmation
- Alternative music recommendations

**Content Originality Check**:
- Text similarity detection
- Plagiarism risk assessment
- Original content generation suggestions

 

### Performance Monitoring and Optimization

 

#### 1. Real-time Monitoring System
**Prometheus + Grafana Integration**:
```python
from prometheus_client import Counter, Histogram, start_http_server
import time

# 定義監控指標
REQUEST_COUNT = Counter('podcast_ai_requests_total', 'Total requests')
REQUEST_LATENCY = Histogram('podcast_ai_request_duration_seconds', 'Request latency')

class MonitoringAgent:
    def __init__(self):
        start_http_server(8000)
        
    @REQUEST_LATENCY.time()
    def process_with_monitoring(self, func, *args, **kwargs):
        REQUEST_COUNT.inc()
        return func(*args, **kwargs)
```

**Automated Alerts**:
- Anomaly detection algorithm
- Intelligent alert filtering
- Automatic repair mechanism

 

#### 2. Performance Optimization Strategies
**Model Optimization**:
- Quantization and pruning techniques
- Model distillation
- Edge computing deployment

**Caching Strategies**:
```python
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
```

 

### Future Development Trends

 

#### 1. Emerging Technology Integration
- Complex optimization problem solving
- Machine learning acceleration

**Edge AI Deployment**:
- Edge device intelligence
- Low-latency real-time processing

 

#### 2. Industry Ecosystem Development
**Standardized Protocols**:
- Cross-platform interoperability
- Open API standards
- Industry best practice specifications

**Business Model Innovation**:
- AI as a Service (AIaaS)
- Subscription-based content generation
- Personalized broadcast customization

 

#### 3. Social Impact and Ethical Considerations
**AI Ethics Framework**:
- Transparency and explainability
- Fairness and unbiasedness
- Human-machine collaboration balance

**Media Responsibility**:
- Assurance of information authenticity
- Presentation of diverse viewpoints
- Social value orientation

This complete technical framework provides a comprehensive solution for AI agent-based broadcasting systems, from basic implementation to enterprise-level deployment. It combines the latest technological trends with practical application needs, offering a concrete and feasible technical path for the digital transformation of the broadcasting media industry.

 




## Additional corpus / va passages naming this agent


### From `corpus/study/SYSTEM_REFERENCE.md` Copy: `sources/excerpts/SYSTEM_REFERENCE.md`.


| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 19 | SoundDesignAgent | Ambience, foley, SFX | — |
| 20 | ComposerAgent | Original score | — |
| 21 | VoiceOverAgent | Narration, character VO | [podcast_agent_functional_specifcation.md](./podcast_agent_functional_specifcation.md) (shared patterns) |
| 22 | SoundMixerAgent | Final mix; 5.1/Atmos deliverables | — |

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



### From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


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



### From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


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

- Master roster row va_id=22 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `C:\Project\va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.soundmixer · va_id=22 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **SoundMixerAgent (Re-recording)** (`video.soundmixer`, va_id=22, category `4-Snd`).

### Responsibility focus
Final mix; deliverables (5.1/Atmos)

### Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: neural audio generation, film scoring AI, TTS/voice clone ethics, loudness standards automation, lip-sync models
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI sound design, AI film scoring, ElevenLabs production use, AI lip sync
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: AI sound for film, generative music for picture, AI VO and mixing

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

<!-- migration_capability_research · video.soundmixer · v1 · 2026-07-13 -->

### `sources/MAPPING.md`

# Mapping — `video.competitorintelligence`

- VA/generic pack ID: `video.competitorintelligence`
- Previous common ID: `video.audio_qc_reviewer`
- SPEC depth: full generic SPEC body + host runtime binding

### `sources/PROVENANCE.json`

```json
{
  "schema_version": "3.0",
  "sources": [
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Competitive Strategy",
      "author": "Michael E. Porter",
      "isbn13": "9780684841489",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Competitive Strategy (Michael E. Porter), ISBN-13 9780684841489"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Good Strategy/Bad Strategy",
      "author": "Richard Rumelt",
      "isbn13": "9780307886231",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Good Strategy/Bad Strategy (Richard Rumelt), ISBN-13 9780307886231"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Playing to Win",
      "author": "Lafley & Martin",
      "isbn13": "9781422187395",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Playing to Win (Lafley & Martin), ISBN-13 9781422187395"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Measure What Matters",
      "author": "John Doerr",
      "isbn13": "9780525538318",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Measure What Matters (John Doerr), ISBN-13 9780525538318"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Innovator's Dilemma",
      "author": "Clayton Christensen",
      "isbn13": "9781633691780",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Innovator's Dilemma (Clayton Christensen), ISBN-13 9781633691780"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Thinking in Systems",
      "author": "Donella Meadows",
      "isbn13": "9781603580557",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Thinking in Systems (Donella Meadows), ISBN-13 9781603580557"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Fifth Discipline",
      "author": "Peter Senge",
      "isbn13": "9780385517256",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Fifth Discipline (Peter Senge), ISBN-13 9780385517256"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Superforecasting",
      "author": "Tetlock & Gardner",
      "isbn13": "9780804136716",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Superforecasting (Tetlock & Gardner), ISBN-13 9780804136716"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "竞争战略",
      "isbn13": "9787508633749",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 竞争战略，ISBN-13 9787508633749"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "好战略，坏战略",
      "isbn13": "9787508643427",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 好战略，坏战略，ISBN-13 9787508643427"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "这就是OKR",
      "isbn13": "9787521702330",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 这就是OKR，ISBN-13 9787521702330"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "创新者的窘境",
      "isbn13": "9787508633336",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 创新者的窘境，ISBN-13 9787508633336"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "系统之美",
      "isbn13": "9787508640114",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 系统之美，ISBN-13 9787508640114"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "第五项修炼",
      "isbn13": "9787508631332",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 第五项修炼，ISBN-13 9787508631332"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "超预测",
      "isbn13": "9787508663098",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 超预测，ISBN-13 9787508663098"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "金字塔原理",
      "isbn13": "9787508633732",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 金字塔原理，ISBN-13 9787508633732"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Trustworthy Online Controlled Experiments",
      "author": "Kohavi, Tang, Xu",
      "isbn13": "9781108724265",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Trustworthy Online Controlled Experiments (Kohavi, Tang, Xu), ISBN-13 9781108724265"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Storytelling with Data",
      "author": "Cole Nussbaumer Knaflic",
      "isbn13": "9781119002253",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Storytelling with Data (Cole Nussbaumer Knaflic), ISBN-13 9781119002253"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Lean Analytics",
      "author": "Croll & Yoskovitz",
      "isbn13": "9781449335670",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Lean Analytics (Croll & Yoskovitz), ISBN-13 9781449335670"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Visual Display of Quantitative Information, 2nd ed.",
      "author": "Edward Tufte",
      "isbn13": "9780961392147",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Visual Display of Quantitative Information, 2nd ed. (Edward Tufte), ISBN-13 9780961392147"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Naked Statistics",
      "author": "Charles Wheelan",
      "isbn13": "9780393347777",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Naked Statistics (Charles Wheelan), ISBN-13 9780393347777"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Signal and the Noise",
      "author": "Nate Silver",
      "isbn13": "9780143125082",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Signal and the Noise (Nate Silver), ISBN-13 9780143125082"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "精益数据分析",
      "isbn13": "9787115384515",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 精益数据分析，ISBN-13 9787115384515"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "用数据讲故事",
      "isbn13": "9787111575558",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 用数据讲故事，ISBN-13 9787111575558"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Elements of Journalism, 3rd ed.",
      "author": "Kovach & Rosenstiel",
      "isbn13": "9780804136785",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Elements of Journalism, 3rd ed. (Kovach & Rosenstiel), ISBN-13 9780804136785"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Blur",
      "author": "Kovach & Rosenstiel",
      "isbn13": "9781608193011",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Blur (Kovach & Rosenstiel), ISBN-13 9781608193011"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Associated Press Stylebook",
      "isbn13": "9781541649883",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Associated Press Stylebook, ISBN-13 9781541649883"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "On Writing Well",
      "author": "William Zinsser",
      "isbn13": "9780060891541",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: On Writing Well (William Zinsser), ISBN-13 9780060891541"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Craft of Research, 4th ed.",
      "author": "Booth et al.",
      "isbn13": "9780226239736",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Craft of Research, 4th ed. (Booth et al.), ISBN-13 9780226239736"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Interviewing as Qualitative Research, 4th ed.",
      "author": "Irving Seidman",
      "isbn13": "9780807755679",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Interviewing as Qualitative Research, 4th ed. (Irving Seidman), ISBN-13 9780807755679"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "新闻的十大基本原则",
      "isbn13": "9787301161111",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 新闻的十大基本原则，ISBN-13 9787301161111"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "采访的艺术",
      "isbn13": "9787301169186",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 采访的艺术，ISBN-13 9787301169186"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "如何阅读一本书",
      "isbn13": "9787100040945",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 如何阅读一本书，ISBN-13 9787100040945"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "研究是一门艺术",
      "isbn13": "9787300116226",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 研究是一门艺术，ISBN-13 9787300116226"
    }
  ],
  "agent_id": "video.competitorintelligence",
  "previous_common_agent_id": "video.audio_qc_reviewer",
  "va_taxonomy_aligned": true,
  "generic_source": "generic-swarm-ops/business/video/agents/video.competitorintelligence",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "aligned_at": "2026-07-27T00:48:11.094463Z",
  "generic_source_depth": {
    "excerpts": true,
    "study": true,
    "adopted_at": "2026-07-27T01:30:27.889953+00:00",
    "upstream": "generic-swarm-ops/business/video/agents"
  },
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\video\\agents\\video.competitorintelligence",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```

### `sources/RETHINK_100_APPLIED.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.competitorintelligence",
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
  "agent_id": "video.competitorintelligence",
  "sources": [
    {
      "id": "src_1",
      "title": "Meta Ad Library",
      "description": "Meta Ad Library",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.competitorintelligence",
      "status": "planned_or_partial"
    },
    {
      "id": "src_2",
      "title": "TikTok Top Ads",
      "description": "TikTok Top Ads",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.competitorintelligence",
      "status": "planned_or_partial"
    },
    {
      "id": "src_3",
      "title": "YouTube scrape",
      "description": "YouTube scrape",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.competitorintelligence",
      "status": "planned_or_partial"
    },
    {
      "id": "src_4",
      "title": "release trackers",
      "description": "release trackers",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.competitorintelligence",
      "status": "planned_or_partial"
    }
  ],
  "note": "Legal review required before treating external corpora as production grounding."
}
```

### `sources/study/research_agent_functional_specification.md`

# Research Agent Functional Specification

## 1. Document Control

- Document title: `Research Agent Functional Specification`
- System name: `grok-research-agent`
- Document type: Current-state functional specification derived from implementation and tests
- Primary delivery model: Local Python CLI application
- Source of truth for this specification: `grok_research_agent/` package implementation, packaged prompts, and automated tests
- Specification intent: Describe the functional behavior the system currently implements, including workflow behavior, file contracts, validation rules, failure handling, and integration points

## 2. Purpose

The system provides a local-first research automation workflow that converts a user-supplied topic into a detailed Markdown research report through a staged pipeline of scope definition, source discovery, source curation, content extraction, notebook assembly, synthesis, optional full-source preservation, final polishing, knowledge compilation, drill-pack generation, image-prompt generation, and YouTube-script generation.

The system is designed to:

- preserve human control at key decision points;
- store all research artifacts locally in resumable session directories;
- use Grok through the xAI OpenAI-compatible API for all LLM generation tasks;
- support optional ingestion of external local documentation as steering context;
- produce inspectable intermediate artifacts rather than a single opaque result.

## 3. Scope

### 3.1 In Scope

- Command-line session lifecycle management
- Persistent session state and artifact storage
- Eight-phase research workflow orchestration
- Optional unattended execution mode
- External-document preprocessing for local steering material
- Knowledge-base compilation into hypergraph and core concepts
- Drill-pack generation from compiled concepts
- Hypergraph updates from newly fed documents
- Mermaid rendering of hypergraph data
- Image-prompt generation from final report content
- YouTube-script generation from final report or section drafts

### 3.2 Out of Scope

- Web UI, API server, or multi-user collaboration
- Authentication, authorization, and role-based permissions
- Database-backed persistence
- Semantic vector search or retrieval index
- Automatic browser automation or crawler orchestration beyond direct HTTP fetch
- Guaranteed factual validation of LLM outputs
- Binary document feeding in the `feed` command beyond best-effort text decoding

## 4. Stakeholders, Roles, and External Actors

### 4.1 Human User Roles

- `Research Operator`: Starts sessions, approves or revises workflow outputs, selects curated sources, optionally chooses full offline collection, and runs auxiliary commands
- `Reviewer/Study User`: Consumes generated report, drill pack, hypergraph, Mermaid output, image prompts, or YouTube script; this role is not technically distinct from the operator

### 4.2 System Actors

- `LLM Provider`: xAI Grok, accessed through the OpenAI-compatible API
- `Remote Content Hosts`: Public websites and PDF endpoints referenced by curated sources
- `Local Filesystem`: Stores sessions, state, outputs, external-doc artifacts, and knowledge-base artifacts
- `Local Environment`: Provides `.env` or environment variables, `EDITOR`, and Python runtime

### 4.3 Access Model

- The system implements no internal user accounts and no permission model.
- Any user who can execute the CLI and read/write the target sessions directory can operate the system fully.

## 5. System Context and Architecture

### 5.1 Core Modules

- `grok_research_agent.cli`
  - Parses CLI arguments
  - Creates `SessionManager` and `WorkflowRunner`
  - Maps command failures to process exit codes
- `grok_research_agent.session_manager`
  - Creates and persists session state
  - Creates unique run directories
  - Provides canonical session and knowledge-base paths
- `grok_research_agent.workflow_phases`
  - Implements the workflow state machine
  - Handles source fetching, extraction, synthesis, compilation, drill-pack generation, feed, show, image generation, and YouTube script generation
- `grok_research_agent.grok_client`
  - Loads environment configuration
  - Calls xAI Grok using the OpenAI client
  - Maps API exceptions into domain-specific runtime errors
- `grok_research_agent.external_docs`
  - Recursively ingests supported local docs
  - Extracts steering context, constraints, requirements, and relevance signals
- `grok_research_agent.prompts/*`
  - Defines output contracts and behavioral instructions for LLM calls

### 5.2 Execution Model

- The product is a single-process CLI application.
- Each command creates a new run directory under the target session.
- Commands operate on files in the session directory and may also write run-local copies for traceability.
- Long-lived state is file-based; there is no background daemon.

## 6. Technology and Runtime Dependencies

- Python runtime: `>=3.11`
- Required packages:
  - `openai`
  - `python-dotenv`
  - `rich`
  - `pydantic>=2`
  - `pypdf`
  - `python-docx`
  - `requests`
  - `beautifulsoup4`
  - `readability-lxml`
  - `chardet<6`
- Packaged CLI entrypoint: `grok-research-agent = grok_research_agent.cli:main`
- Convenience wrappers: root-level `main.py` and `cli.py` forward to packaged CLI entrypoint

## 7. Configuration Specification

### 7.1 Environment Variables

- `GROK_API_KEY`
  - Required for any command path that instantiates `GrokClient`
  - Must be non-empty after whitespace trimming
  - If absent, LLM-backed actions shall fail with a clear message
- `GROK_MODEL`
  - Optional
  - Defaults to `grok-3`
  - Blank values shall be normalized back to `grok-3`
- `GROK_MAX_OUTPUT_TOKENS`
  - Optional integer
  - Defaults to `50000`
  - Invalid or non-numeric values shall revert to `50000`
  - Values below `1` shall be clamped to `1`
- `GROK_REQUEST_TIMEOUT_SECONDS`
  - Optional integer
  - Defaults to `300`
  - Invalid or non-numeric values shall revert to `300`
  - Values below `1` shall be clamped to `1`
- `EDITOR`
  - Optional
  - Used only during Phase 0 `edit` flow
  - If absent, selecting `edit` shall still create the editable temporary file, but no external editor is launched automatically

### 7.2 `.env` Resolution

- When the workflow constructs a default `GrokClient`, it shall attempt to load a `.env` file located two directory levels above the session directory.
- If no `.env` exists there, the system shall continue using process environment variables only.

## 8. User Interface Specification

### 8.1 Interface Type

- Primary interface: terminal/CLI
- Rendering library: `rich`
- Output types:
  - plain status messages
  - Markdown content echoed to console in some phases
  - preview tables for discovery and full-collection selection

### 8.2 Human Interaction Points

- H0: scope confirmation
- H1: curated-source approval
- H2: draft approval or revision instruction
- H3: full-source offline-copy selection

### 8.3 Unattended Mode

- `--auto` shall bypass interactive prompts and drive the workflow to completion where possible.
- In auto mode:
  - H0 is auto-confirmed
  - H1 source selection is set to `all`
  - H1 approval is set to `approve`
  - H2 feedback is set to `approve`
  - H3 selection is controlled by `--auto-full-collection` and defaults to `all`
- Auto mode shall not call `input()`.

## 9. User Roles and Permissions Specification

Because the system has no identity or authorization layer, the functional permission model is:

- any operator can execute any command;
- any operator can create, resume, modify, compile, drill, feed, and finalize sessions they can access on disk;
- there are no restricted admin-only actions;
- there is no audit or attribution model beyond file timestamps and artifact presence.

## 10. CLI Command Functional Requirements

### 10.1 Common Command Behavior

- `FR-CLI-001`: All commands except `list-types` shall require `--sessions-dir`.
- `FR-CLI-002`: Commands that need an existing session shall requi

…(clipped 38072 characters from `research_agent_functional_specification.md`)
