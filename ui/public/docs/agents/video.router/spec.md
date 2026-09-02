# video.router — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/video.router/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "video.router",
  "status": "registered",
  "role": "RouterAgent (VA Domain Pack)",
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
      "video.orchestrator",
      "video.costoptimizer"
    ],
    "outputs": [
      "video.judge",
      "video.planner"
    ]
  },
  "max_refinement_count": 0,
  "production_activation_requested": false,
  "does_not_own": [
    "Host credential storage",
    "Silent production activation without fail-closed gates",
    "Inventing action references for irreversible mutations",
    "Owning other agents' exclusive craft outputs without handoff contract",
    "Long-running multi-step craft execution",
    "Credentials",
    "Silent production activation",
    "Another agent's exclusive craft output without handoff",
    "Automatic promotion of self-generated artifacts",
    "Modification of safety, telemetry, gates, permissions, or corrigibility",
    "Self-granting tools, plugins, network, or isolation downgrades"
  ],
  "va_id": 55,
  "va_name": "RouterAgent",
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

# RouterAgent

> Self-contained VA Domain Pack agent on host common-agent-swarm-ops.
> Pack agent ID matches pure VA/generic taxonomy: `video.router`.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 55 |
| **pack_id** | `video.router` |
| **upstream_name** | RouterAgent |
| **category** | `9-Meta` |
| **domain_id** | `video` |
| **previous_common_id** | `video.tool_policy_designer` |
| **status** | `registered` |
| **maturity** | L0 / non-active |
| **taxonomy** | Pure VA Domain Pack (via generic pack agents) |
| **folder** | `business/video/agents/video.router/` |

## Responsibility

Picks right specialist agent (and model) for each subtask

Host role binding: `RouterAgent (VA Domain Pack)`. Design-time VA table content below is historical and non-binding for activation.

### Responsibility (from VA table)

Picks right specialist agent (and model) for each subtask

### Knowledge distillation sources (historical)

Agent-capability registry; benchmark history (cost/quality/latency)

### Self-quality criteria (historical)

Routing accuracy ≥95% vs oracle; cost within budget

### Surpass-human signal (historical)

Beats human producer in agent/vendor selection

### Critique bus (historical)

- **Accepts critique from:** OrchestratorAgent, CostOptimizerAgent

- **Comments on:** PlannerAgent (bad decomposition)

### Tools design-time notes (historical, non-activating)

Agent registry DB; benchmark leaderboard cache; pricing APIs

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

### Architecture pattern (historical)

Classifier + ReAct (match task embedding → agent capability)

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

- Prompt reference: `video.prompt.router.v1`
- Rubric reference: `video.rubric.router.v1`
- Critique edges: `{"inputs": ["video.critic"], "outputs": ["video.judge"]}`
- Max refinement: `3`
- VA table quality criteria retained under Provenance and Identity surface above.

## Runtime binding

Authoritative fail-closed host configuration:

```json
{
  "agent_id": "video.router",
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
  "prompt_reference": "video.prompt.router.v1",
  "role": "RouterAgent (VA Domain Pack)",
  "rubric_reference": "video.rubric.router.v1",
  "schema_version": "1.0",
  "status": "registered",
  "va_id": 55,
  "va_name": "RouterAgent",
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

- Pack agent ID `video.router` is aligned to pure VA Domain Pack / generic pack taxonomy (Agent IDs ≈ VA tables).
- Previous common inventory ID `video.tool_policy_designer` is historical mapping only.
- Upstream design body below is **historical and non-binding**; local `agent_spec.json` is authoritative.
- Full VA/generic SPEC depth retained for offline design fidelity (including category roster rows and common agent structure when present upstream).

### VA Domain Pack specification body (historical and non-binding)

```text
RouterAgent

> **Self-contained agent definition** for host `upstream-generic-pack`. Body text is embedded from in-pack corpus and upstream-va-design when available. Do not require external repos to understand this agent.

Identity

| Field | Value |
|-------|-------|
| **va_id** | 55 |
| **pack_id** | `video.router` |
| **category** | `9-Meta` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.router/` |

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

Picks right specialist agent (and model) for each subtask

Knowledge distillation sources

Agent-capability registry; benchmark history (cost/quality/latency)

Self-quality criteria

Routing accuracy ≥95% vs oracle; cost within budget

Surpass-human signal

Beats human producer in agent/vendor selection

Critique bus

- **Accepts critique from:** OrchestratorAgent, CostOptimizerAgent

- **Comments on:** PlannerAgent (bad decomposition)

Tools (design-time documentation)

Agent registry DB; benchmark leaderboard cache; pricing APIs

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

Architecture pattern

Classifier + ReAct (match task embedding → agent capability)

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


Document: `study/llm_usage_functional_specification.md`

_Embedded from `corpus/study/llm_usage_functional_specification.md`. Also stored at `sources/study/llm_usage_functional_specification.md` under this agent folder._


Build Central LLM API Usage & Cost Dashboard App

Project Name Suggestion
**LLMUsageHub** or **MultiLLM Dashboard** or **API Cost Central** or **LLM Spend Tracker**

1. Project Overview
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
Inspired by **[cc-switch]([historical-url] (the popular desktop tool for managing LLM providers for Claude Code / Codex / Gemini CLI). This web app is **purely focused on usage/cost analytics** across direct personal API keys, serving as a usage-only companion to cc-switch but as a web application.

2. Core Goals
- One unified place to monitor **all** LLM spending and usage.
- Secure, local-only storage of API keys (never sent to any server).
- Automatic or on-demand fetching of usage/billing data.
- Historical tracking + visualizations.
- Extremely extensible — easy to add new providers.
- Beautiful, modern UI similar to cc-switch.

3. Key Features (Must-Have)

Provider Management
- Add / edit / remove accounts with: name, provider type (preset), API key, base URL (for custom endpoints), notes.
- Pre-built **presets** for as many providers as possible (see section 4).
- Support multiple accounts per provider.
- One-click “Refresh All” and individual refresh buttons.

Usage & Balance Fetching
- Prefer **official APIs** where available (e.g. `/usage`, `/billing`, `/balance`, `/v1/token_plan/remains`, etc.).
- Fallback options:
  - Manual entry of current usage/balance.
  - Web dashboard scraping (using Playwright if needed, last resort).
- Background auto-refresh (configurable interval) + manual refresh.
- Store full history snapshots in local DB.

Dashboard UI
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

Cost Calculation
- Built-in pricing tables for major models (input/output tokens → USD).
- Allow user to override pricing per model.
- Show estimated USD even when provider only reports tokens.

Data Persistence & Export
- Local **SQLite** database for all historical usage snapshots.
- Export full data as CSV or JSON.

Security & UX
- API keys stored **encrypted** locally (Fernet symmetric encryption).
- Dark/light theme (default dark, matching modern AI tools).
- Browser-based UI accessible from localhost.
- Fully offline-first after initial setup.
- Responsive, clean, professional UI.

Nice-to-Have (Phase 2)
- AI-powered insights (“You spent 68% on Kimi this month — consider switching heavy tasks to Groq”).
- Import/export configuration (including possible cc-switch import).
- Per-model cost forecasting.
- Optional proxy/router mode (like LiteLLM or cc-switch) so the app can also log usage from actual API calls.

4. Supported Providers (List as Many as Possible)
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

5. Technical Stack

Backend
- **Framework**: Python 3.11+ with FastAPI
- **API**: OpenAPI 3.1 (auto-generated from FastAPI, browsable at /docs)
- **Database**: SQLite with SQLAlchemy ORM
- **HTTP Client**: httpx (async)
- **Security**: API keys encrypted at rest using cryptography Fernet
- **Background Tasks**: FastAPI BackgroundTasks + APScheduler

API Design (OpenAPI)
- RESTful endpoints for all CRUD operations
- Automatic OpenAPI schema generation
- Interactive API docs via Swagger UI at /docs
- ReDoc alternative at /redoc

Frontend
- **Framework**: React 18 + TypeScript
- **Build Tool**: Vite
- **Styling**: TailwindCSS + shadcn/ui
- **Charts**: Recharts
- **State Management**: Zustand
- **HTTP Client**: Axios or fetch API

Architecture
- **Web App** (not desktop) — runs locally in browser
- Backend runs as a local server (localhost:8000)
- Frontend served by FastAPI static files or separate Vite dev server
- 100% local — no cloud sync unless explicitly added later

6. Development Phases (Suggested)
1. Project setup (FastAPI backend + React frontend + SQLite).
2. Provider management + secure key storage.
3. Core usage fetcher system (abstract interface).
4. Implement 5–6 high-priority providers (xAI, Poe, OpenRouter, MiniMax, Kimi, OpenAI).
5. Dashboard UI + charts.
6. Add remaining providers + pricing tables.
7. Background refresh, alerts, export, polish.
8. Testing + documentation.

7. Deliverables
- Complete source code with excellent comments and README.
- Clear instructions on **how to add a new provider** (new Python module + pricing config).
- Setup scripts for running locally with FastAPI + React.
- Sample data / test mode.
- License: MIT (or whatever user prefers).

This spec should give the coding agent everything needed to build a production-ready, beautiful, and highly useful central usage dashboard. Feel free to ask the user for clarification on specific provider APIs or preferred tech choices.

**Ready to code!** 🚀




Document: `plan/planner_agent_v2.1.md`

_Embedded from `corpus/plan/planner_agent_v2.1.md`. Also stored at `sources/plan/planner_agent_v2.1.md` under this agent folder._


SIPA — Software Implementation Planner Agent

Complete Research-Hardened Specification & Design Document

**Version:** 2.1 — Research-Hardened, Security-Operationalized  
**Date:** 2026-06-03  
**Status:** Production-Ready Design Spec  
**Primary Goal:** Convert very large software-specification corpora into high-fidelity, traceable, component-type-adaptive implementation plans and granular tasks for AI coding agents and human developers.

---

Change Summary — v2.0 → v2.1

This revision is a deep-research pass and adversarial “100x rethink” consolidation. It does **not** merely expand the previous document; it tightens the system into an implementable, governable, security-aware planner.

Major Improvements

1. **Research verification and correction**
   - Verified MAAD as arXiv:2606.01385, submitted May 31, 2026, and preserved it as the core architecture-planning influence. ([arxiv.org]([historical-url]
   - Updated AgentOrchestra reference: current arXiv title emphasizes the Tool-Environment-Agent, or TEA, protocol and lifecycle-aware orchestration rather than only “general-purpose task solving.” ([arxiv.org]([historical-url]
   - Updated GitHub Spec Kit alignment to include the current Spec → Plan → Tasks → Implement flow plus newer practical commands such as constitution, clarify, analyze, checklist, and task-to-issues. ([github.github.com]([historical-url]
   - Qualified xAI/Grok Build claims: official xAI pages verify plan mode, parallel subagents, skills/plugins/hooks/MCP, headless mode, and API availability; this spec no longer references unofficial “Arena Mode” claims and instead defines SIPA’s own optional local “Arena Evaluator.” ([x.ai]([historical-url]

2. **Added security and trust model**
   - Added prompt-injection, memory-poisoning, MCP/tool safety, least-privilege execution, untrusted-context boundaries, and human approval controls.
   - Integrated NCSC guidance that LLMs do not enforce a hard data/instruction boundary and should be treated as “inherently confusable” components. ([ncsc.gov.uk]([historical-url]
   - Integrated MCP security principles around user consent, tool safety, data privacy, and untrusted tool descriptions. ([modelcontextprotocol.io]([historical-url]
   - Added OWASP GenAI/agentic risk alignment and operational monitoring requirements. ([genai.owasp.org]([historical-url]

3. **Strengthened context engineering**
   - Formalized SIPA’s context pipeline around **write, select, compress, isolate**, matching current agent context-engineering practice. ([langchain.com]([historical-url]
   - Added retrieval budgets, evidence ledgers, source confidence levels, retrieval evaluation, and stale-source detection.
   - Added optional GraphRAG-style global/local retrieval for corpus-wide sensemaking and dependency impact analysis. ([microsoft.com]([historical-url]

4. **Expanded component taxonomy**
   - Added Security/Compliance, Testing/Quality, Migration/Legacy, AI/Agent Workflow, and Documentation/Developer Experience component types.
   - Added secondary risk tags that directly change retrieval depth, critic rubrics, and human-review requirements.

5. **Made outputs more machine-consumable**
   - Added artifact manifests, evidence ledgers, decision logs, task execution contracts, and canonical schemas.
   - Added stable IDs for requirements, claims, decisions, interfaces, tasks, risks, and open questions.

6. **Added evaluation science**
   - Added retrieval metrics, plan-quality metrics, artifact-level critic thresholds, and downstream coder-agent success metrics.
   - Integrated RAG evaluation dimensions such as context relevance, answer faithfulness, answer relevance, context precision, and context recall. ([aclanthology.org]([historical-url]

7. **Improved implementation roadmap**
   - Split MVP into a safer vertical slice.
   - Added CLI/API/MCP deployment model, observability, cache strategy, sandbox strategy, and governance gates.

---

Table of Contents

1. Executive Summary
2. Core Problem
3. Research Foundation
4. Design Principles
5. Component Taxonomy
6. System Architecture
7. Agent Roles
8. End-to-End Workflow
9. Context Engineering, RAG, and Memory
10. Critic/Evaluator Subsystem
11. Security and Trust Model
12. Data Models and Schemas
13. Output Artifacts
14. Implementation Roadmap
15. Tool and Harness Integration
16. Metrics and Success Criteria
17. Risks and Mitigations
18. Future Roadmap
19. References

---

1. Executive Summary

SIPA is a hierarchical, context-engineered, multi-agent planning system for turning large software specification corpora into implementation-ready plans and tasks.

It is designed for projects where the source material may include:

- Markdown specs
- PRDs
- architecture notes
- API contracts
- user stories
- domain models
- UI descriptions
- ADRs
- implementation notes
- test plans
- legacy migration notes
- operational constraints

The key idea is simple but powerful:

> **Different software components require different levels and types of detail.**

A strategic architecture plan should not be generated with the same retrieval scope, summarization style, or output format as a UI screen, a shared library, a data model, or a migration adapter.

SIPA therefore uses:

- **Component-type classification**
- **Scoped retrieval**
- **Evidence-based synthesis**
- **Hierarchical memory**
- **Embedded critic loops**
- **Traceability-first artifacts**
- **Granular task generation**
- **Security-aware agent execution**

The result is a planner that reduces context size for downstream coding agents while improving fidelity, traceability, and implementation success.

---

2. Core Problem

Large software specs break AI coding workflows in predictable ways:

1. **Context overload**
   - Too much raw documentation causes distraction, contradiction, and missed details.

2. **Uniform summarization failure**
   - Architecture needs synthesis.
   - UI features need exhaustive local detail.
   - Shared components need contracts.
   - Data models need invariants.
   - Integrations need error semantics and compatibility rules.

3. **Loss of traceability**
   - Coding agents often implement plausible behavior that is not grounded in the source spec.

4. **Weak plan-to-task translation**
   - Large plans often become vague tasks.
   - Vague tasks create bad code, rework, and hidden assumptions.

5. **Security and tool-risk amplification**
   - Agentic coding tools can read files, run commands, call APIs, and modify repos.
   - Prompt injection, over-permissioned tools, and memory poisoning become architectural risks, not just prompt risks.

SIPA exists to solve these problems before coding begins.

---

3. Research Foundation

3.1 Spec-Driven Development

GitHub Spec Kit treats specifications as the center of AI-assisted development and ships a core flow of **Spec → Plan → Tasks → Implement**. It also provides Markdown artifacts, quality checklists, and cross-artifact analysis, making it a strong workflow model for SIPA’s output structure. ([github.github.com]([historical-url]

SIPA extends this model for **pre-existing massive corpora**, not just greenfield features. It adds corpus indexing, type-aware planning, traceability enforcement, and critic loops.

3.2 MAAD and Requirements-to-Architecture Planning

MAAD proposes four specialized agents — Analyst, Modeler, Designer, and Evaluator — to convert requirements into multi-view architectural blueprints with quality assessments. It uses RAG for architecture standards and patterns, hierarchical memory for design history, and an evaluator for structured quality reports. ([arxiv.org]([historical-url]

SIPA adopts MAAD most directly for the Architecture Sub-Planner, then generalizes the same analyst/designer/evaluator structure across other component types.

3.3 Hierarchical Multi-Agent Orchestration

AgentOrchestra’s current formulation introduces TEA, a Tool-Environment-Agent protocol that treats agents, tools, environments, prompts, memory, and outputs as versioned lifecycle-managed resources. It also uses a central planner coordinating specialized sub-agents. ([arxiv.org]([historical-url]

SIPA adopts the practical lesson: orchestration should not be “agents chatting.” It should be explicit state, typed handoffs, versioned artifacts, and lifecycle-aware execution.

3.4 Multi-Agent Software Engineering Patterns

The LLM-based multi-agent systems survey identifies role specialization, SDLC coverage, agent synergy, and trustworthy autonomous software engineering as major research directions. ([arxiv.org]([historical-url]

MASAI shows the value of modular sub-agents with separate objectives and strategies for software-engineering tasks, including avoiding unnecessarily long trajectories and excessive context. ([arxiv.org]([historical-url]

SWE-agent demonstrates that the interface between agent and computer materially affects coding-agent performance, motivating SIPA’s emphasis on harness-native task packaging. ([arxiv.org]([historical-url]

SWE-Search supports the value of self-evaluation and iterative refinement for repository-level software tasks. ([proceedings.iclr.cc]([historical-url]

3.5 Context Engineering

Modern agent design increasingly treats context engineering as a first-class discipline. LangChain’s current framework groups context strategies into **write, select, compress, and isolate**, which SIPA adopts as its core context model. ([langchain.com]([historical-url]

SIPA applies this as follows:

- **Write:** Persist plans, decisions, summaries, memory, and evidence outside the prompt.
- **Select:** Retrieve only the task-relevant source chunks, patterns, and memories.
- **Compress:** Summarize and extract with source-preserving compression.
- **Isolate:** Give each sub-planner a scoped context window rather than the entire corpus.

3.6 GraphRAG and Corpus Sensemaking

GraphRAG combines text extraction, network analysis, LLM prompting, and summarization to understand text datasets. Microsoft’s GraphRAG project is especially relevant for corpus-wide themes and dependency discovery. ([microsoft.com]([historical-url]

SIPA uses graph retrieval optionally, but the architecture is designed so a simpler hybrid vector/BM25 retriever can be used first.

3.7 Architecture Standards

SIPA’s architecture outputs are aligned with:

- **ISO/IEC/IEEE 42010** concepts of stakeholders, concerns, viewpoints, and views. ([iso-architecture.org]([historical-url]
- **C4 model** levels: system context, container, component, and code, with an emphasis on only producing diagrams that add value. ([c4model.com]([historical-url]
- **ATAM** for reasoning about quality-attribute tradeoffs and architectural risks. ([sei.cmu.edu]([historical-url]
- **Kruchten 4+1 views** for multi-perspective architecture description. ([scirp.org]([historical-url]

3.8 Security Research and Agentic Risk

NCSC warns that current LLMs do not enforce a true boundary between data and instructions, so prompt injection should be treated as an inherent residual risk that must be reduced through system design and impact limitation. ([ncsc.gov.uk]([historical-url]

OWASP’s GenAI exploit reporting shows AI security incidents are increasingly targeting agent identities, orchestration layers, supply chains, permissions, and validation controls rather than only model outputs. ([genai.owasp.org]([historical-url]

The MCP specification explicitly notes that MCP enables arbitrary data access and code execution paths, requiring user consent, data privacy controls, and caution around tool behavior descriptions. ([modelcontextprotocol.io]([historical-url]

SIPA therefore treats security as a core subsystem, not a postscript.

---

4. Design Principles

1. **Type-aware planning**
   - Every component gets the planning style it actually needs.

2. **Traceability before creativity**
   - SIPA may synthesize, but every major claim must be grounded in source evidence or explicitly marked as an assumption.

3. **Small context, high signal**
   - Never feed the full corpus to a sub-planner unless the task is corpus-level analysis.

4. **Critic-first quality culture**
   - Drafts are not final until they pass structured quality gates.

5. **Living specifications**
   - Plans are versioned, diffable, and updated as implementation changes.

6. **Harness-native outputs**
   - Outputs must be directly useful to Cursor, Claude Code, Kiro, Grok Build, OpenWebUI, custom CLI agents, or human developers.

7. **Security by architecture**
   - Tool access, memory, retrieval, source trust, and approval flows must be explicitly governed.

8. **Human gates where risk is high**
   - Human review is noted for strategic, security-critical, destructive, or high-cost decisions.

9. **Evaluation built in**
   - Retrieval quality, traceability, consistency, implementability, and downstream success are measured.

10. **Composable implementation**
   - SIPA can start as a CLI and later expose MCP/API integrations.

---

5. Component Taxonomy

The taxonomy controls:

- Retrieval strategy
- Context budget
- Planner selection
- Output template
- Critic rubric
- Human-review requirement
- Task decomposition style

5.1 Primary Component Types

| Type | Detail Level | Retrieval Strategy | Output Emphasis | Example |
|---|---:|---|---|---|
| Architecture / Strategic | High-level synthesis | Broad cross-corpus retrieval + ASRs/NFRs + patterns | Views, ADRs, tradeoffs, quality attributes | System architecture, service topology |
| Feature / UI / Tactical | Deep scoped detail | Narrow feature retrieval + full local excerpts | User stories, acceptance criteria, flows, state, validation | Dashboard, onboarding flow |
| Common / Shared Component | Contract-focused | Cross-module references + interface mentions | APIs, types, invariants, extension points | Auth service, notification library |
| Data / Domain Model | Medium | Entities, relationships, invariants, lifecycle rules | Schemas, aggregates, constraints, migrations | User, Order, Course, ExamAttempt |
| Integration / External | Medium | API contracts, event schemas, third-party docs | Mapping, retry, idempotency, compatibility | Stripe adapter, LMS sync |
| Infrastructure / DevOps | High-operational | NFRs, deployment docs, runtime constraints | IaC, CI/CD, observability, scaling | Kubernetes, GitHub Actions |
| Security / Compliance | High-rigor | Security reqs, policies, threat models, data flows | Threat model, controls, audit evidence | PII handling, RBAC, encryption |
| Testing / Quality | Medium | Acceptance criteria, test notes, defect history | Test matrix, fixtures, validation strategy | E2E suite, contract tests |
| Migration / Legacy | Medium-high | Legacy docs, current behavior, target constraints | Strangler plan, compatibility, rollback | COBOL replacement, DB migration |
| AI / Agent Workflow | High-rigor | Agent instructions, tools, memory, data access | Agent state machine, tool policy, eval harness | Coding agent, RAG assistant |
| Documentation / DevEx | Medium | Onboarding docs, workflows, developer feedback | Quickstarts, AGENTS.md, conventions | Contributor guide, module README |

5.2 Secondary Tags

Secondary tags modify critic gates and output sections:

- `security-critical`
- `privacy-sensitive`
- `performance-sensitive`
- `high-availability`
- `user-facing`
- `internal-only`
- `regulated`
- `legacy-modernization`
- `agentic-tool-use`
- `destructive-actions`
- `requires-human-review`
- `experimental`
- `mvp-critical`

5.3 Classification Rules

SIPA classifies components using:

1. Explicit metadata if present.
2. Requirement IDs and section names.
3. Keyword heuristics.
4. LLM classifier with structured output.
5. Human override.
6. Critic validation.

Classification output must include:

'''yaml
component_id: CMP-auth-service
name: Auth Service
primary_type: common_component
secondary_tags:
  - security-critical
  - privacy-sensitive
confidence: 0.91
evidence:
  - specs/auth.md#overview
  - specs/security.md#session-management
needs_human_review: true
'''

---

6. System Architecture

'''mermaid
flowchart TD
    A[Spec Corpus] --> B[Ingestion & Indexing]
    B --> C[Hybrid Retriever]
    B --> D[Knowledge Graph Optional]
    B --> E[Corpus Summary & Glossary]

    E --> F[Master Orchestrator]
    C --> F
    D --> F

    F --> G[Component Classifier]
    G --> H[Dependency Graph]
    H --> I[Master Plan]

    I --> J1[Architecture Sub-Planner]
    I --> J2[Feature/UI Sub-Planner]
    I --> J3[Common Component Sub-Planner]
    I --> J4[Data/Domain Sub-Planner]
    I --> J5[Integration Sub-Planner]
    I --> J6[Security/Compliance Sub-Planner]
    I --> J7[Testing/Quality Sub-Planner]

    J1 --> K[Critic/Evaluator]
    J2 --> K
    J3 --> K
    J4 --> K
    J5 --> K
    J6 --> K
    J7 --> K

    K -->|refine| J1
    K -->|refine| J2
    K -->|refine| J3
    K -->|refine| J4
    K -->|refine| J5
    K -->|refine| J6
    K -->|refine| J7

    K --> L[Approved Specs]
    L --> M[Task Decomposer]
    M --> N[Task Lists / Agent Work Packs]
    N --> O[Coder Agents / Humans]
    O --> P[Implementation Feedback]
    P --> Q[Memory Update + Impact Analysis]
    Q --> F
'''

---

7. Agent Roles

7.1 Master Orchestrator

**Purpose:** Own the global plan, decomposition, dependencies, and coordination.

**Responsibilities:**

- Build corpus-level project understanding.
- Identify epics, modules, components, and phases.
- Classify components.
- Generate `master_plan.md`.
- Maintain dependency graph.
- Trigger sub-planners.
- Coordinate critic feedback and refinements.
- Escalate high-risk ambiguity to humans.

**Outputs:**

- `master_plan.md`
- `component_inventory.yml`
- `dependency_graph.mmd`
- `traceability_index.yml`
- `planning_run_manifest.json`

---

7.2 Architecture Sub-Planner

**Purpose:** Produce strategic architecture plans.

**Pattern:** MAAD-inspired Analyst → Modeler → Designer → Evaluator.

**Responsibilities:**

- Extract functional requirements, NFRs, and ASRs.
- Produce C4 and/or 4+1 views where useful.
- Generate ADRs.
- Identify tradeoffs.
- Define interface boundaries.
- Produce deployment and runtime views.
- Run ATAM-lite quality analysis.

**Outputs:**

- `architecture_<component>.md`
- `adr_<decision>.md`
- `architecture_views/*.mmd`
- `quality_attribute_scenarios.yml`

---

7.3 Feature/UI Sub-Planner

**Purpose:** Produce detailed, scoped implementation specs for user-facing behavior.

**Responsibilities:**

- Extract user stories.
- Expand acceptance criteria.
- Define UI states.
- Define user flows.
- Identify validations and errors.
- Link APIs and data dependencies.
- Generate implementation-sized tasks.

**Outputs:**

- `feature_spec_<name>.md`
- `flow_<name>.mmd`
- `acceptance_criteria_<name>.yml`
- `tasks_<name>.md`

---

7.4 Common Component Sub-Planner

**Purpose:** Produce contract-first shared component specs.

**Responsibilities:**

- Aggregate scattered mentions.
- Define public interfaces.
- Define invariants.
- Define extension points.
- Document configuration.
- Document failure modes.
- Provide usage examples.

**Outputs:**

- `component_spec_<name>.md`
- `interface_contract_<name>.yml`
- `usage_examples_<name>.md`

---

7.5 Data/Domain Sub-Planner

**Purpose:** Produce domain model and data lifecycle specifications.

**Responsibilities:**

- Identify entities, aggregates, value objects, and relationships.
- Define lifecycle states.
- Capture invariants and constraints.
- Identify migration and versioning needs.
- Define query patterns.
- Link domain objects to features and APIs.

**Outputs:**

- `domain_model_<bounded_context>.md`
- `schema_conceptual_<bounded_context>.mmd`
- `invariants_<bounded_context>.yml`

---

7.6 Integration Sub-Planner

**Purpose:** Produce robust integration and adapter specs.

**Responsibilities:**

- Define external contracts.
- Map source and target data.
- Define retry, timeout, idempotency, and backoff.
- Define auth and secret handling.
- Define version compatibility.
- Define observability and reconciliation.

**Outputs:**

- `integration_spec_<name>.md`
- `contract_mapping_<name>.yml`
- `integration_test_plan_<name>.md`

---

7.7 Security/Compliance Sub-Planner

**Purpose:** Produce security-sensitive plans and controls.

**Responsibilities:**

- Identify assets, trust boundaries, actors, and data flows.
- Threat-model agent/tool/data paths.
- Map requirements to controls.
- Define least-privilege policies.
- Define audit evidence.
- Require human approval for high-risk actions.

**Outputs:**

- `security_spec_<scope>.md`
- `threat_model_<scope>.md`
- `control_matrix_<scope>.yml`
- `approval_policy_<scope>.yml`

---

7.8 Critic/Evaluator

**Purpose:** Prevent bad plans from becoming implementation tasks.

**Critic dimensions:**

- Traceability
- Source fidelity
- Completeness
- Consistency
- Implementability
- Testability
- Security
- Risk
- Sizing
- Downstream agent usability

**Outputs:**

- `critique_<artifact>.json`
- `patch_instructions_<artifact>.md`
- `quality_gate_report_<artifact>.md`

---

7.9 Task Decomposer

**Purpose:** Convert approved specs into small, executable tasks.

**Task properties:**

- One logical change.
- Clear acceptance criteria.
- Source links.
- Relevant context excerpt.
- Dependencies.
- Suggested files.
- Test expectations.
- Rollback notes if needed.

**Outputs:**

- `tasks_<component>.md`
- optional issue exports
- optional agent work-pack JSON

---

8. End-to-End Workflow

Phase 0 — Project Constitution

Before planning, SIPA should establish or ingest project principles.

Inputs may include:

- architecture principles
- coding standards
- testing standards
- security rules
- stack preferences
- UX rules
- naming conventions
- human review policy

Output:

'''text
constitution.md
'''

This aligns with current Spec Kit practice, where a constitution can govern subsequent specification, planning, and implementation artifacts. ([github.com]([historical-url]

---

Phase 1 — Ingestion and Indexing

Steps:

1. Scan source directories.
2. Respect include/exclude rules.
3. Parse Markdown heading hierarchy.
4. Extract requirement IDs.
5. Detect components, entities, APIs, screens, and decisions.
6. Chunk semantically.
7. Generate embeddings.
8. Build keyword index.
9. Optionally build graph index.
10. Generate corpus summary and glossary.

Outputs:

- `corpus_index.md`
- `glossary.md`
- `chunks.parquet`
- `embeddings.db`
- `knowledge_graph.graphml`
- `ingestion_manifest.json`

---

Phase 2 — Master Plan

The Master Orchestrator:

1. Reads corpus summaries.
2. Retrieves global cross-cutting requirements.
3. Builds initial component inventory.
4. Classifies components.
5. Generates dependency graph.
6. Creates implementation phases.
7. Identifies MVP slice.
8. Flags risks and unknowns.
9. Runs master-plan critic.

Output:

'''text
plans/master_plan.md
'''

noted sections:

- project summary
- scope
- non-goals
- component inventory
- phases
- dependency graph
- risk register
- traceability skeleton
- open questions
- human approval checklist

---

Phase 3 — Type-Aware Sub-Planning

For each component:

1. Confirm component type.
2. Assemble context package.
3. Run relevant sub-planner.
4. Generate draft artifact.
5. Run critic.
6. Patch only failing sections.
7. Re-run critic.
8. Persist approved artifact.

Output examples:

'''text
plans/architecture_core_platform.md
plans/feature_spec_student_dashboard.md
plans/component_spec_auth_service.md
plans/domain_model_user_progress.md
plans/integration_spec_lms_sync.md
plans/security_spec_auth_and_sessions.md
'''

---

Phase 4 — Task Generation

The Task Decomposer creates implementation tasks from approved plans.

Task format:

'''markdown
- [ ] T042 [P] Build StudentDashboardHeader
  - **Component:** Student Dashboard
  - **Source:** feature_spec_student_dashboard.md#ui-header
  - **references:** T011, T018
  - **Acceptance:**
    - Renders avatar, name, role, and notification state.
    - Handles loading and empty-avatar states.
    - Meets responsive behavior defined in section 4.2.
  - **Tests:**
    - Unit render states.
    - E2E dropdown interaction.
  - **Context excerpt:** See linked source section.
'''

---

Phase 5 — Implementation Feedback

After coder agents or humans execute tasks, SIPA ingests:

- diffs
- test results
- review comments
- implementation blockers
- changed assumptions
- failed tasks
- new requirements

SIPA then:

1. Updates episodic memory.
2. Performs impact analysis.
3. Updates affected plans.
4. Re-runs critic gates.
5. Regenerates affected tasks.

---

9. Context Engineering, RAG, and Memory

9.1 Context Package Structure

Every sub-planner receives a context package:

'''yaml
context_package_id: CTX-feature-student-dashboard-v1
component_id: CMP-student-dashboard
planner_type: feature_ui
token_budget:
  max_total: 45000
  source_evidence: 25000
  memory: 5000
  master_context: 5000
  template_and_instructions: 5000
retrievals:
  - chunk_id: CHK-00123
    source: specs/student.md#dashboard
    relevance: 0.94
    trust_level: canonical
  - chunk_id: CHK-00418
    source: specs/ui.md#notifications
    relevance: 0.87
    trust_level: canonical
compression:
  method: extractive_then_abstractive
  preserve_quotes: true
  preserve_requirement_ids: true
'''

9.2 Retrieval Modes

| Mode | Purpose |
|---|---|
| Exact ID lookup | Requirement IDs, ADR IDs, API names |
| BM25 keyword | Exact technical terms |
| Vector search | Semantic similarity |
| Graph traversal | Dependencies and trace links |
| Global summarization | Corpus-wide themes |
| Local neighborhood | Closely related chunks |
| Reranked hybrid | Default production mode |

9.3 Memory Types

| Memory | Scope | Examples |
|---|---|---|
| Working | Current run | draft, active critic notes |
| Episodic | Past runs | refinements, implementation feedback |
| Semantic | Generalized knowledge | patterns, glossary, conventions |
| Procedural | Agent behavior | prompts, rubrics, templates |
| Evidence | Source-grounding | chunk IDs, citations, excerpts |
| Security | Trust and permissions | approved tools, blocked actions |

9.4 Evidence Ledger

Every major output claim should map to evidence:

'''yaml
claim_id: CLM-architecture-012
claim: "Auth Service owns session creation and refresh-token rotation."
artifact: component_spec_auth_service.md
evidence:
  - source: specs/auth.md#session-lifecycle
    quote: "..."
  - source: specs/security.md#refresh-token-policy
    quote: "..."
confidence: 0.93
status: supported
'''

---

10. Critic/Evaluator Subsystem

10.1 Quality Gates

| Gate | noted For | Pass Threshold |
|---|---|---:|
| Traceability | all artifacts | ≥ 0.90 |
| Source fidelity | all artifacts | ≥ 0.92 |
| Internal consistency | all artifacts | ≥ 0.90 |
| Cross-artifact consistency | multi-component plans | ≥ 0.88 |
| Implementability | task lists | ≥ 0.90 |
| Testability | features/components | ≥ 0.90 |
| Security review | tagged artifacts | no high findings |
| Human approval | strategic/high-risk | explicit approval |

10.2 Critique Schema

'''json
{
  "artifact_id": "feature_spec_student_dashboard",
  "overall_verdict": "refine",
  "scores": {
    "traceability": 0.86,
    "source_fidelity": 0.93,
    "consistency": 0.91,
    "implementability": 0.88,
    "testability": 0.84,
    "security": 0.90
  },
  "issues": [
    {
      "severity": "high",
      "category": "traceability",
      "location": "section 4.3",
      "description": "Notification polling interval is asserted without source evidence.",
      "suggested_patch": "Either link to source requirement or mark as assumption requiring human approval."
    }
  ],
  "recommended_next_action": "targeted_refinement"
}
'''

10.3 Optional SIPA Arena Evaluator

SIPA can run multiple competing planner outputs and evaluate them using the same rubric.

Arena mode should compare:

- traceability
- clarity
- completeness
- risk handling
- taskability
- security posture
- source fidelity

This is independent of any external vendor feature. Official xAI documentation verifies Grok Build plan mode and parallel subagents, but SIPA’s evaluator must remain vendor-neutral. ([x.ai]([historical-url]

---

11. Security and Trust Model

11.1 Core Security Assumptions

1. Retrieved documents may contain malicious instructions.
2. Tool descriptions may be untrusted.
3. Memory can be poisoned.
4. Agent outputs can be wrong even when confident.
5. Human approval is only useful if the UI shows the actual action, not merely the agent’s summary.
6. High-impact operations require deterministic controls outside the LLM.

11.2 Trust Levels

| Trust Level | Meaning | Example |
|---|---|---|
| canonical | approved source of truth | reviewed spec |
| trusted-derived | generated from canonical and approved | approved plan |
| unreviewed-derived | generated but not approved | draft plan |
| external | outside corpus | web docs |
| untrusted | user/tool/retrieved content with possible injection | arbitrary webpage |
| hostile-test | adversarial fixture | red-team prompt |

11.3 Tool Permission Policy

| Action | Default |
|---|---|
| Read project specs | allowed |
| Write generated plans | allowed in output directory |
| Modify source code | blocked by SIPA planner |
| Run shell commands | blocked unless explicit tool mode |
| Delete files | human approval noted |
| Access secrets | prohibited |
| Call external APIs | human approval noted |
| Install packages | human approval noted |
| Update memory | allowed only through memory sanitizer |

11.4 Prompt-Injection Controls

SIPA must:

- Wrap retrieved content as untrusted evidence.
- Never let retrieved content override system/developer instructions.
- Strip or flag suspicious instructions in source chunks.
- Separate source evidence from planner instructions.
- Use deterministic policy checks for tool calls.
- Log source-to-claim mappings.
- Require human approval for high-impact actions.

11.5 MCP Controls

If SIPA exposes MCP tools:

- Every tool must have a narrow schema.
- Destructive tools must require explicit approval.
- Tool descriptions must be treated as untrusted unless from trusted servers.
- MCP resources must not be forwarded without consent.
- Tool calls must be logged with inputs, outputs, requester, and artifact ID.

These requirements follow MCP’s own security posture around user consent, tool safety, data privacy, and arbitrary code execution risks. ([modelcontextprotocol.io]([historical-url]

---

12. Data Models and Schemas

12.1 Core Artifact Frontmatter

'''yaml
---
artifact_id: string
type: master_plan | architecture | feature_ui | common_component | domain_model | integration | security | task_list | critique
component_id: string
component_name: string
primary_type: string
secondary_tags: []
version: string
status: draft | in_review | approved | implemented | superseded
created_at: ISO-8601
updated_at: ISO-8601
source_corpus_version: string
traceability_score: number
critic_score: number
dependencies: []
review_required: boolean
approved_by: string | null
---
'''

12.2 Requirement Record

'''yaml
requirement_id: REQ-001
text: "Users must be able to reset their password by email."
source:
  file: specs/auth.md
  section: password-reset
type: functional
priority: must
component_refs:
  - CMP-auth-service
  - CMP-email-service
status: active
'''

12.3 Decision Record

'''yaml
decision_id: ADR-004
title: "Use refresh-token rotation"
status: proposed
context: "Session persistence requires secure long-lived authentication."
decision: "Use short-lived access tokens and rotating refresh tokens."
alternatives:
  - server-side sessions
  - static refresh tokens
consequences:
  positive:
    - limits replay window
  negative:
    - requires token-family invalidation logic
evidence:
  - specs/security.md#token-policy
'''

12.4 Task Record

'''yaml
task_id: T042
title: "Implement refresh-token rotation"
component_id: CMP-auth-service
source_artifacts:
  - component_spec_auth_service.md#refresh-token-rotation
dependencies:
  - T038
parallelizable: false
risk: high
acceptance_criteria:
  - "Refresh token is rotated on every successful refresh."
  - "Reuse of old refresh token invalidates token family."
tests:
  - "unit"
  - "integration"
human_review_required: true
'''

---

13. Output Artifacts

13.1 `master_plan.md`

noted sections:

1. Executive summary
2. Scope and non-goals
3. Corpus summary
4. Component inventory
5. Component classification table
6. Dependency graph
7. Implementation phases
8. MVP slice
9. Risk register
10. Traceability skeleton
11. Open questions
12. Approval checklist
13. Changelog

13.2 Architecture Spec

noted sections:

1. Architecture scope
2. Stakeholders and concerns
3. ASRs and NFRs
4. C4 context/container/component views
5. Runtime scenarios
6. Deployment view
7. ADRs
8. Interface catalog
9. Quality attribute scenarios
10. Tradeoff analysis
11. Risks
12. Traceability matrix

13.3 Feature/UI Spec

noted sections:

1. Feature summary
2. User stories
3. User flows
4. UI states
5. Acceptance criteria
6. Validation matrix
7. Error and edge cases
8. API/data dependencies
9. Accessibility notes
10. Analytics/events
11. Test scenarios
12. Traceability matrix

13.4 Common Component Spec

noted sections:

1. Purpose
2. Scope
3. Public interface
4. Data contracts
5. Invariants
6. Configuration
7. Extension points
8. Error handling
9. Performance expectations
10. Security considerations
11. Usage examples
12. Test strategy
13. Traceability matrix

13.5 Security Spec

noted sections:

1. Assets
2. Actors
3. Trust boundaries
4. Data flows
5. Threats
6. Controls
7. Residual risks
8. Approval requirements
9. Monitoring
10. Audit evidence
11. Traceability matrix

13.6 Task List

noted sections:

1. Task overview
2. Execution order
3. Parallelizable tasks
4. Critical path
5. Task checklist
6. Test checklist
7. Review checklist
8. Rollback notes
9. Source links

---

14. Implementation Roadmap

Phase 1 — Safe MVP

Build a vertical slice:

- Corpus loader
- Markdown chunker
- Hybrid search
- Component classifier
- Master planner
- One sub-planner
- Basic critic
- Markdown renderer
- Task decomposer
- CLI command

Recommended first sub-planner: **Feature/UI** if validating implementation handoff, or **Architecture** if validating strategic planning.

Phase 2 — Core System

Add:

- All primary sub-planners
- Knowledge graph
- Evidence ledger
- Hierarchical memory
- Multi-stage critic
- Human approval gates
- Incremental re-planning
- Evaluation metrics
- Template library

Phase 3 — Production Hardening

Add:

- Observability dashboard
- Cost/token tracking
- Model routing
- Prompt/version registry
- MCP server
- Sandboxed tool mode
- Security red-team suite
- CI validation
- Plan drift detection
- Issue tracker export

Phase 4 — Self-Improvement

Add:

- Planner performance analytics
- Failed-task learning
- Retrieval strategy optimization
- Prompt/template evolution
- Domain-specific taxonomies
- Automatic benchmark generation

---

15. Tool and Harness Integration

15.1 Cursor / Claude Code / Kiro / Similar Tools

SIPA should write:

'''text
plans/
tasks/
AGENTS.md
.cursor/rules/
.claude/commands/
'''

Generated `AGENTS.md` should include:

- module conventions
- relevant plan links
- forbidden actions
- test expectations
- source-of-truth order

15.2 Grok Build

Official xAI docs verify that Grok Build supports plan mode, headless scripting, custom models, skills/plugins, MCP servers, and parallel subagents. ([x.ai]([historical-url]

SIPA integration pattern:

1. SIPA generates approved plan and task pack.
2. Grok Build runs in plan mode.
3. Human compares Grok’s execution plan to SIPA task criteria.
4. Implementation proceeds only after approval.
5. SIPA ingests diffs and test results.

15.3 MCP/API Mode

SIPA can expose:

- `sipa.index_corpus`
- `sipa.get_master_plan`
- `sipa.plan_component`
- `sipa.critique_artifact`
- `sipa.generate_tasks`
- `sipa.trace_requirement`
- `sipa.impact_analysis`

All write or destructive operations require authorization.

---

16. Metrics and Success Criteria

16.1 Retrieval Metrics

- Context precision
- Context recall
- Source coverage
- Duplicate chunk rate
- Stale source rate
- Evidence sufficiency
- Unsupported claim rate

16.2 Artifact Metrics

- Traceability score
- Source-fidelity score
- Consistency score
- Completeness score
- Testability score
- Implementability score
- Security score
- Human review time

16.3 Downstream Metrics

- Task completion rate
- Rework rate
- Test pass rate
- Spec deviation rate
- Clarification count
- Average task context size
- Time from spec change to updated tasks

16.4 MVP Success Thresholds

- Traceability ≥ 0.85 for MVP, ≥ 0.90 for production.
- No high-severity critic findings on approved artifacts.
- Average refinement loops < 3.
- At least 30% reduction in downstream task clarification.
- At least 50% reduction in context passed to coder agents compared with raw-spec prompting.

---

17. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Bad retrieval | Hybrid search, reranking, evidence ledger, retrieval eval |
| Hallucinated plans | Source-fidelity critic, unsupported-claim detector |
| Over-decomposition | Task sizing critic |
| Under-decomposition | Dependency and acceptance-criteria checks |
| Conflicting specs | Conflict detector and human resolution |
| Prompt injection | Untrusted-source boundaries, deterministic controls |
| Memory poisoning | Memory sanitizer and trust levels |
| Tool abuse | Least privilege and approval gates |
| Stale plans | Incremental indexing and impact analysis |
| High token cost | Compression, caching, model routing |
| Human bottleneck | Risk-based approvals |
| Vendor lock-in | Markdown-first artifacts and MCP-compatible API |

---

18. Future Roadmap

1. Full GraphRAG impact analysis.
2. Multimodal ingestion for UI mocks and architecture diagrams.
3. Automatic test generation from acceptance criteria.
4. Formal-methods bridge for critical invariants.
5. Domain packs for edtech, finance, embedded systems, and legacy modernization.
6. Jira/GitHub issue export.
7. Continuous plan-code drift detection.
8. Multi-model evaluator arena.
9. Self-optimizing prompt/template registry.
10. Secure enterprise deployment bundle.

---

19. References

- MAAD — requirements-to-architecture multi-agent design with Analyst, Modeler, Designer, Evaluator, RAG, hierarchical memory, and quality evaluation. ([arxiv.org]([historical-url]
- AgentOrchestra / TEA Protocol — lifecycle-aware hierarchical multi-agent orchestration. ([arxiv.org]([historical-url]
- LLM-Based Multi-Agent Systems for Software Engineering survey. ([arxiv.org]([historical-url]
- Designing LLM-based Multi-Agent Systems for SE Tasks — quality attributes, design patterns, and rationale. ([arxiv.org]([historical-url]
- GitHub Spec Kit documentation and repository. ([github.github.com]([historical-url]
- LangChain context engineering: write, select, compress, isolate. ([langchain.com]([historical-url]
- Microsoft GraphRAG project. ([microsoft.com]([historical-url]
- MASAI modular software-engineering agents. ([arxiv.org]([historical-url]
- SWE-agent agent-computer interface research. ([arxiv.org]([historical-url]
- SWE-Search iterative refinement and MCTS for software agents. ([proceedings.iclr.cc]([historical-url]
- ARES and RAGAS-style RAG evaluation dimensions. ([aclanthology.org]([historical-url]
- ISO/IEC/IEEE 42010 architecture description concepts. ([iso-architecture.org]([historical-url]
- C4 model diagrams. ([c4model.com]([historical-url]
- ATAM architecture tradeoff analysis. ([sei.cmu.edu]([historical-url]
- NCSC prompt-injection guidance. ([ncsc.gov.uk]([historical-url]
- OWASP GenAI exploit reporting and agentic risk framing. ([genai.owasp.org]([historical-url]
- Model Context Protocol specification and security principles. ([modelcontextprotocol.io]([historical-url]
- xAI Grok Build official CLI and documentation pages. ([x.ai]([historical-url]

---
Learn more:
1. [\[2606.01385\] Bridging Requirements and Architecture: Multi-Agent Orchestration with External Knowledge and Hierarchical Memory]([historical-url]
2. [\[2506.12508\] AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool-Environment-Agent(TEA) Protocol]([historical-url]
3. [GitHub Spec Kit | Spec Kit Documentation]([historical-url]
4. [Introducing Grok Build | xAI]([historical-url]
5. [Prompt injection is not SQL injection (it may be worse) | National Cyber Security Centre]([historical-url]
6. [Specification - Model Context Protocol]([historical-url]
7. [OWASP GenAI Exploit Round-up Report Q1 2026 - OWASP Gen AI Security Project]([historical-url]
8. [Context Engineering]([historical-url]
9. [Project GraphRAG - Microsoft Research]([historical-url]
10. [ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems - ACL Anthology]([historical-url]
11. [\[2404.04834\] LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision and the Road Ahead]([historical-url]
12. [MASAI: Modular Architecture for Software-engineering AI Agents]([historical-url]
13. [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering]([historical-url]
14. [SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement]([historical-url]
15. [ISO/IEC/IEEE 42010: Conceptual Model]([historical-url]
16. [Diagrams | C4 model]([historical-url]
17. [The Architecture Tradeoff Analysis Method | CMU Software Engineering Institute]([historical-url]
18. [Kruchten, P. (1995) Architectural Blueprints—The “4+1” View Model of Software Architecture. IEEE Software, 12, 42-50. - References - Scientific Research Publishing]([historical-url]
19. [GitHub - github/spec-kit:  Toolkit to help you get started with Spec-Driven Development · GitHub]([historical-url]
20. [Grok Build Beta | xAI]([historical-url]
21. [\[2511.08475\] Designing LLM-based Multi-Agent Systems for Software Engineering Tasks: Quality Attributes, Design Patterns and Rationale]([historical-url]



Document: `study/agent_loop_v3.md`

_Embedded from `corpus/study/agent_loop_v3.md`. Also stored at `sources/study/agent_loop_v3.md` under this agent folder._


Refined Agent Loop: Hierarchical, ReAct-Inspired, Production-Grade Design

**Version:** 2026-06-10 (v3 — Cognitive-Enhanced: Integrated high-priority traditional human thinking models from ranked analysis in thinking_model.md (Cynefin, Premortem, AAR, Double-Loop Learning, RPD, Dual Process, Metacognition, 5 Whys/Fishbone, Red Team, Paul-Elder, etc.) for adaptive context routing, proactive risk mitigation, fast/slow deliberation paths, structured reflection, and deeper self-evolution. All v2 details preserved; new mechanisms are additive, configurable, and mapped to existing phases.)  
**Research Sources**: "Why Do Multi-Agent LLM Systems Fail?" (MASFT taxonomy, 14-18 failure modes), Reflexion, Prospector, CGI, memory papers, xAI docs, developer reports on infinite loops/context issues, plus systematic review of 40+ human cognitive frameworks (ranked by adoption priority for agent loops).
**Purpose:** Actionable reference for building reliable, scalable LLM-based agent systems. Combines academic foundations (ReAct synergy of reasoning + acting), xAI's server-side agentic implementation (multi-agent orchestration for deep research), and advanced hierarchical patterns (planner + specialists + self-evolution).  
**Target Audience:** Builders of harnesses, multi-agent systems, coding agents, research agents (e.g., N1ch01as-style Architect with critic/self-refinement loops).  
**Key Principle:** Controlled loops with explicit state, structured outputs, quality gates, and hierarchical delegation. Not uncontrolled chain reactions — managed orchestration with bubbling-up consolidation and deliberate synthesis.

1. Core Principles (Refined from Research)

1.1 Foundational: ReAct Paradigm (Yao et al., ICLR 2023)
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

1.2 Production xAI Multi-Agent Orchestration (2026)
- **grok-4.20-multi-agent** (or equivalent): Launches configurable teams (4 agents for quick/focused; 16 for deep/comprehensive).
- **How the loop works**:
  - Server-side **realtime collaboration**: Multiple specialized agents run in parallel.
  - Each contributes reasoning, tool calls, findings.
  - **Leader agent** synthesizes discussion, cross-references, and delivers final structured answer.
  - Parallel tool invocation and iteration based on intermediate findings.
  - Sub-agent internal states encrypted/hidden by default (control + security); only leader outputs + (optionally) encrypted content exposed.
- **Strengths**: Deep multi-step research, structured outputs (tables, comparisons), realtime refinement, automatic tool use without client intervention in the loop.
- **Plan-first elements**: Complementary patterns in xAI tools like Grok Build CLI use explicit plan generation first, then parallel sub-agent execution (e.g., up to 8 sub-agents in isolated Git worktrees).

1.3 Hierarchical + Self-Evolving (AgentOrchestra / Surveys 2025-2026)
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

1.4 Cognitive Architecture Enhancements from Ranked Human Thinking Models (v3 Addition)

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

1.5 Known Problems, Failure Modes & Targeted Mitigations (Research-Backed)

Recent systematic studies (especially the **MASFT taxonomy** from analysis of 150+ traces across popular multi-agent frameworks) identify that **most failures stem from design/spec issues (~40%+)**, coordination breakdowns, and weak verification/termination — **not raw model intelligence**. Single-agent ReAct loops suffer overlapping issues plus context bloat and repetitive behavior. Below is a synthesized taxonomy of the most common, well-documented problems, with **actionable mitigations** mapped directly to the phases in this document.

Major Problem Categories & Frequency/Significance
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

How Mitigations Integrate into the Loop Phases
- **Phase 0 (Init)**: Spec engineering + validation is the single highest-ROI fix.
- **Phase 1 (Core Loop)**: Cycle detection, bounded steps/reflection, structured observations, progress tracking.
- **Phase 2 (Delegation)**: Narrow sub-specs + contracts; orchestrator monitoring.
- **Phase 3 (Consolidation)**: Verifier/critic gates, cross-validation, harmonization.
- **Phase 4 (Reflection/Self-evolution)**: Validation before applying changes; bounded loops.
- **Phase 5 (Termination)**: Verifier + explicit Done with evidence.

**Key Insight from Research**: Fixing **specification quality + verification layers + explicit termination controls** delivers the largest reliability gains. Adding more agents or raw model power without these often yields diminishing or negative returns.

2. The Complete Agent Loop Process (Actionable)

Phase 0: Initialization (Spec-Driven Setup)
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
'''json
{
  "task_id": "...",
  "objective": "...",
  "success_criteria": ["...", "..."],
  "constraints": ["max_steps: 50", "budget_tokens: 200k"],
  "output_format": "structured report with citations",
  "initial_plan": ["Step 1: ...", "Step 2: ..."],
  "quality_gates": ["completeness > 90%", "no hallucinations", "structured output"]
}
'''

Phase 1: Core Iteration Loop (ReAct-Inspired, Controlled)
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
     '''json
     {
       "status": "success | partial | failed",
       "data": {...},
       "summary": "concise natural language",
       "confidence": 0.85,
       "issues": ["list of problems"],
       "next_suggestions": ["..."],
       "trace_id": "..."
     }
     '''
   - Append to history + update todo/state.
5. **Light Reflection** (every N steps or on failure): Quick self-critique — "Is this trajectory still aligned? Any obvious fix?"

**Circuit Breaker Pattern (Recommended for Production)**

Circuit breakers prevent cascading failures when a tool, LLM call, or sub-agent is repeatedly failing. They have three states:
- **CLOSED**: Normal operation, requests go through.
- **OPEN**: Too many failures → fast-fail immediately (protects the system).
- **HALF_OPEN**: After timeout, allow limited test requests to check recovery.

Use one circuit breaker per tool type or per sub-agent role. Integrate with the retry wrappers below.

**Code Example: Minimal Controlled ReAct Loop with Cycle Detection (Python)**

'''python
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
'''

**Code Example: Lightweight Verifier / Critic Agent (Prompt + Schema) — v3 Enhanced with Critic Modes + Paul-Elder Standards**

'''python
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
'''

**Code Example: Simple Self-Evolution / Reflection Step (Trace → Edit → Validate)**

'''python
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
'''

**Termination Conditions** (checked every iteration or at gates):
- Success criteria met + quality gate passed.
- Max steps / token budget / time reached.
- Explicit `Done` / `Finish` action with validated output.
- Irrecoverable failure (escalate to human or higher orchestrator).
- Early exit if intermediate result satisfies objective.

Phase 2: Hierarchical Delegation & Sub-Loops
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

Phase 3: Consolidation, Synthesis & Restructuring
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

Phase 4: Reflection, Critique & Self-Evolution (Advanced)
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

Phase 5: Termination & Output
- When gates passed or termination condition met:
  1. Final synthesis pass.
  2. Structured final output (match spec).
  3. Optional: Post-hoc reflection summary for user or logging.
  4. Persist full trace + versions for audit/replay/debug.
- **Human-in-loop hooks**: At quality gate failures, high-stakes actions, or budget exhaustion.

3. State, Memory & Infrastructure Recommendations

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

4. Decision Framework (When to Use What)

| Task Complexity       | Recommended Pattern                  | Key Features to Enable          | Example Use Case |
|-----------------------|--------------------------------------|---------------------------------|------------------|
| Simple fact lookup    | Flat ReAct (single loop)            | Tool calling, basic thought    | Quick search + answer |
| Multi-step research   | xAI Multi-Agent or Hierarchical     | Parallel agents, leader synth  | Deep analysis with sources |
| Coding / long project | Plan-first + Hierarchical + Worktrees | Sub-agents in isolation, todo.md | Full app generation + debug |
| Open-ended / creative | ReAct + Reflection + Self-evolution | Critic gates, versioned prompts| Iterative design refinement |
| High-stakes / reliable| All above + strong Quality Gates    | Structured results, validation | Enterprise automation |

5. Common Pitfalls & Mitigations (from Research)

**Primary reference: See the full MASFT-style taxonomy, failure modes, and phase-specific mitigations in Section 1.5 above.** The points below are retained for quick scanning and now include additional patterns from recent studies.

- **Context explosion**: Aggressive summarization + hierarchical state (local sub-memories).
- **Infinite loops / thrashing**: Hard max iterations + progress tracking in todo + critic that can force replan or escalate.
- **Poor consolidation**: Mandate structured sub-results + dedicated harmonization/reporter step.
- **Hallucinations in plans**: Ground every major claim in observations; use critic before committing to plan.
- **Brittle delegation**: Use explicit sub-task specs + success criteria; validate returned results.
- **Lack of visibility**: Full tracing + optional streaming of reasoning.

6. Quick-Start Pseudocode Skeleton (Python-like)

'''python
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
'''

Sub-agent invoke follows the same pattern recursively (narrower scope).

7. References & Sources

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



Document: `study/SYSTEM_REFERENCE.md`

_Embedded from `corpus/study/SYSTEM_REFERENCE.md`. Also stored at `sources/study/SYSTEM_REFERENCE.md` under this agent folder._


VA-Agent-Swarm — System Reference & Integration Map

> **Purpose:** This document is the single entry point that links every agent specification, workflow, technical architecture, and supporting resource into one cohesive system view. It maps how each component relates to the whole, defines the integration points, and provides navigation for implementers.

---

Table of Contents

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

1. System Overview

The **VA-Agent-Swarm** is a hierarchical multi-agent system (MAS) designed to fully automate (or augment) professional video production — from initial creative brief through final delivery across all distribution channels. The system comprises **114 specialized agents** organized into 10 functional categories, supported by dedicated infrastructure agents, a shared critique bus, and a unified orchestration runtime.


Core Design Principles

| Principle | Description | Reference |
|-----------|-------------|-----------|
| **Agentic Graph** | Agents as DAG nodes with handoffs and review gates | [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) §1 |
| **Self-Refine + Critique** | Every agent drafts → self-critiques → revises against rubric | Madaan et al., 2023 |
| **Shared Artifact Contract** | Machine-readable manifests flow between all phases | [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) §1.3 |
| **Human-in-the-Loop Gates** | Critical decisions escalate to human approval | [agents.md](./agents.md) — ProducerAgent |
| **Provenance (C2PA)** | Every artifact is signed; downstream agents verify chain | C2PA spec |
| **Continuous Self-Improvement** | Agents learn from outcomes, store episodic memory, ratchet quality | Reflexion (Shinn 2023) |

System Boundaries

'''
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
'''

> **Full architecture details:** [ui/architecture_communication.md](./ui/architecture_communication.md)


---

2. Architecture Layers

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

3. Agent Categories & Specification Map

The 114 agents are organized into 10 categories. Below, each category links to the master roster AND to any dedicated deep-specification documents that provide implementation-level detail.

3.1 Above-the-Line Agents (1–5)

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 1 | DirectorAgent | Owns vision; shot intents, pacing, approvals | — |
| 2 | ProducerAgent / EP | Budget, schedule, phase gates | — |
| 3 | ScreenwriterAgent | Treatment → screenplay; dialogue; structure | [screenwriter_strategic_goal_achievement_agent_functional_specification.md](./screenwriter_strategic_goal_achievement_agent_functional_specification.md) |
| 4 | ShowrunnerAgent | Cross-episode arc, writers'-room orchestration | — |
| 5 | CastingAgent | Voice + likeness selection; auditions | — |

**Roster reference:** [agents.md](./agents.md) §1


3.2 Camera & Lighting Agents (6–8)

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 6 | CinematographerAgent (DoP) | Lensing, lighting, composition, look | — |
| 7 | CameraOperatorAgent | Framing, focus, camera moves | — |
| 8 | DronePilotAgent | Aerial cinematography | — |

**Roster reference:** [agents.md](./agents.md) §2

3.3 Editorial & Color Agents (9–18)

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

3.4 Sound & Music Agents (19–22)

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 19 | SoundDesignAgent | Ambience, foley, SFX | — |
| 20 | ComposerAgent | Original score | — |
| 21 | VoiceOverAgent | Narration, character VO | [podcast_agent_functional_specifcation.md](./podcast_agent_functional_specifcation.md) (shared patterns) |
| 22 | SoundMixerAgent | Final mix; 5.1/Atmos deliverables | — |

**Roster reference:** [agents.md](./agents.md) §4

3.5 Performance & Choreography Agents (23–27)

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 23 | ChoreographyAgent | Movement design | — |
| 24 | MusicVideoDirectorAgent | Visual concept for songs | — |
| 25 | ComedyWriterAgent | Skits, parody, viral memes | — |
| 26 | TalentAgent (On-camera) | AI-rendered performance | — |
| 27 | UGCCreatorAgent | Authentic-feel ads | — |

**Roster reference:** [agents.md](./agents.md) §5


3.6 Distribution & Marketing Agents (28–31)

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 28 | SocialMediaStrategistAgent | Platform distribution, trends | — |
| 29 | CopywriterAgent | Scripts, captions, hooks | — |
| 30 | CreativeDirectorAgent | Campaign concept | — |
| 31 | PerformanceMarketerAgent | Optimize ads for ROAS | — |

**Roster reference:** [agents.md](./agents.md) §6

3.7 Education & Domain-Expert Agents (32–45)

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

**Roster reference:** [agents.md](./agents.md) §7

3.8 AI-Era Specialist Agents (46–52)

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 46 | PromptEngineerAgent | Crafts prompts; steers gen models | — |
| 47 | AvatarDesignAgent | Synthetic presenter identity | — |
| 48 | VoiceCloneAgent / LipSync | Voice cloning + lip-sync | — |
| 49 | AIQAConsistencyAgent | Frame drift, artifacts, identity breaks | — |
| 50 | PersonalizationEngineerAgent | Variable templates (name/face swap) | — |
| 51 | TrailerEditorAgent | Hook-driven trailer cuts | — |
| 52 | SportsAnalystAgent | Tactical breakdowns + diagrams | — |

**Roster reference:** [agents.md](./agents.md) §8


3.9 Specialist Meta-Agents (53–80)

These agents manage orchestration, quality, continuity, and system-level concerns:

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 53 | OrchestratorAgent | DAG execution, retries, fan-out/fan-in | — |
| 54 | PlannerAgent | Decomposes brief into phased DAG | — |
| 55 | RouterAgent | Picks right agent + model for subtask | — |
| 56 | JudgeAgent | Adjudicates disputes via debate | — |
| 57–80 | (Various meta-agents) | Memory, continuity, safety, escalation, etc. | — |

**Roster reference:** [agents.md](./agents.md) §9

3.10 Workflow Support Agents (81–114)

These agents provide production infrastructure services:

| Range | Function | Examples |
|-------|----------|----------|
| 81–90 | Asset management, versioning, render dispatch | RenderFarmAgent, AssetManagerAgent |
| 91–100 | Quality gates, delivery packaging, compliance | DeliveryAgent, QCGateAgent |
| 101–114 | Analytics, feedback loops, retraining triggers | AnalyticsAgent, FeedbackLoopAgent |

**Roster reference:** [agents.md](./agents.md) §10

---

4. Infrastructure & Support Agents

These cross-cutting agents have their own **deep functional and technical specifications** because they serve the entire system:

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


---

5. Cross-Cutting Capabilities

These specifications define capabilities that are shared across multiple agents or apply system-wide:

| Capability | What It Provides | Used By | Specification |
|-----------|-----------------|---------|---------------|
| **Strategic Goal Achievement Framework** | 6-stage self-inquiry system for transforming vague goals into actionable plans | All planning agents (PlannerAgent, ProducerAgent, DirectorAgent) | [strategic_goal_achievement_agent_functional_specification.md](./strategic_goal_achievement_agent_functional_specification.md) |
| **Screenwriter Goal Achievement** | Practical demonstration of goal framework applied to creative writing | ScreenwriterAgent, ShowrunnerAgent, ComedyWriterAgent | [screenwriter_strategic_goal_achievement_agent_functional_specification.md](./screenwriter_strategic_goal_achievement_agent_functional_specification.md) |
| **Psychological Profiling** | 100 creator profiles with MBTI, motivations, fears, creative parameters | CastingAgent, TalentAgent, PersonalizationEngineerAgent, UGCCreatorAgent | [psychological_profile_agent_functional_specifications.md](./psychological_profile_agent_functional_specifications.md) |
| **Psychological Recommendation** | Psychology-based preference prediction (Big Five, emotional state) | AudienceSimAgent, PerformanceMarketerAgent, PersonalizationEngineerAgent | [psychological_recommendation_agent_functional_specification.md](./psychological_recommendation_agent_functional_specification.md) |
| **Complex Problem Solving** | WHAT/WHY/HOW/DO/REVIEW structured methodology | All diagnostic agents (FactCheckerAgent, SMEAgent, JudgeAgent, OptimizationAgent) | [complex_problem_solution_process_model.md](./complex_problem_solution_process_model.md) |
| **Common Agent Structure** | Shared architectural pattern for all agents | All 114 agents | [common-agent-structure.svg](./common-agent-structure.svg) + [common-agent-structure.html](./common-agent-structure.html) |

---

6. Workflow Integration

6.1 Production Pipeline (End-to-End)

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


6.2 Workflow Variants (by Video Type)

Each video type follows a customized path through the agent DAG. Visual workflows are available as SVGs:

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

6.3 Human Baseline Comparison

The system is designed as a direct AI replacement/augmentation of the human production workflow:

> **Reference:** [human_video_production_workflow.md](./human_video_production_workflow.md) — Defines the 52 human craft roles that the agent system maps to and extends.

---

7. Data Flow & Handoff Contracts

Every agent communicates via a **Shared Artifact Handoff Contract** (machine-readable JSON manifest):

| Field | Purpose |
|-------|---------|
| `artifact_id` / `version` | Unique identity for every output and revision |
| `parent_assets` | Provenance links to scripts, prompts, plates, stems |
| `brief_scope` | Subtask, acceptance criteria, target audience |
| `technical_spec` | Codec, aspect ratio, duration, frame rate, color space, loudness |
| `rights_and_consent` | License state, likeness/voice consent, territorial limits |
| `continuity_state` | Character look, props, wardrobe, environment, identity hash |
| `qc_status` | Latest L1/L2/L3 QC result |
| `target_channels` | Theatrical, streaming, broadcast, social, CRM, LMS |
| `provenance_manifest` | C2PA reference, critique log pointer, sign-off chain |

> **Full contract spec:** [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) §1.3

7.1 Critique Bus Protocol

All agents communicate critique via a structured JSON bus:

'''json
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
'''


---

8. UI & Communication Layer

The frontend provides human operators with visibility and control over the agent swarm:

| UI Document | Covers | Link |
|------------|--------|------|
| Architecture & Communication | Three-tier protocol (REST, WebSocket, Agent Queue) | [ui/architecture_communication.md](./ui/architecture_communication.md) |
| Agent Management UI | How to monitor, configure, and override agents | [ui/agent_management_ui.md](./ui/agent_management_ui.md) |
| Backend Agent Management | Server-side agent lifecycle, scaling, health | [ui/backend_agent_management.md](./ui/backend_agent_management.md) |
| UI Design | Visual design system, components, interactions | [ui/ui_design.md](./ui/ui_design.md) |
| Project Creation Flow | User journey from brief to running production | [ui/project_creation_flow.md](./ui/project_creation_flow.md) |
| Production Scale Discovery | How the system adapts to project complexity | [ui/production_scale_discovery.md](./ui/production_scale_discovery.md) |
| Video Remake Enhancement | Workflow for improving existing videos | [ui/video_remake_enhancement.md](./ui/video_remake_enhancement.md) |
| 100 Improvements Rethink | Comprehensive UI improvement catalog | [ui/RETHINK_100_IMPROVEMENTS.md](./ui/RETHINK_100_IMPROVEMENTS.md) |

---

9. Technology Stack Reference

9.1 LLM Providers (for Agent Reasoning)

| Provider | Models | Primary Use |
|----------|--------|------------|
| xAI | Grok-4.x | Primary reasoning, tool use, research |
| Google DeepMind | Gemini 2.5 Pro (1M context) | Long-context analysis, bible search |
| OpenAI | GPT-4o, o-series | Structured outputs, consensus sampling |
| Anthropic | Claude 4 | Safety, constitutional AI agents |
| Open-source | Qwen2.5, Wan 2.6 | Cost optimization, local inference |

9.2 Video Generation Models

> **Full reference (50 models ranked):** [video_generation_techology_should_learn_now.md](./video_generation_techology_should_learn_now.md)

| Rank | Model | Primary Use in System |
|------|-------|--------------------|
| 1 | Seedance 2.0 (ByteDance) | Multimodal generation with native audio |
| 2 | Kling 3.0 (Kuaishou) | Motion control, multi-character scenes |
| 3 | Veo 3.1 (Google) | Cinematic quality, character consistency |
| 4 | Grok Imagine Video (xAI) | Fast iteration, social-first output |
| 6 | Sora 2 (OpenAI) | Narrative/physics storytelling |
| 8 | Runway Gen-4.5 | Professional creative control, VFX |

9.3 Audio/Voice Tools

| Tool | Purpose |
|------|---------|
| ElevenLabs v3 | TTS, voice cloning, sound effects |
| Sync.so | Lip-sync alignment |
| Udio/Suno | Music generation |
| Dolby Atmos Renderer | Spatial audio mixing |

9.4 Infrastructure

| Component | Technology |
|-----------|-----------|
| Orchestration | LangGraph + Temporal |
| Event Bus | Redis Streams / NATS |
| Asset Storage | S3 + metadata DB |
| Observability | LangSmith + AgentOps |
| Frontend | React 19 + Next.js 15 |
| Backend | FastAPI (Python) |
| Vector DB | Chroma + Pinecone/Weaviate |
| Graph DB | LightRAG (OpenSearch) |


---

10. Reference Material Index

10.1 Deep Implementation Reference (68 Chapters)

The `reference/how_to_build_a_video_agent_system/` directory contains 68 chapters of detailed implementation guidance:

| Chapters | Likely Coverage |
|----------|----------------|
| 01–10 | System foundations, architecture patterns, agent design |
| 11–20 | Individual agent implementation, tool integration |
| 21–30 | Quality assurance, evaluation, testing patterns |
| 31–40 | Orchestration, state management, message passing |
| 41–50 | Video generation, audio, creative pipelines |
| 51–60 | Delivery, distribution, optimization loops |
| 61–68 | Advanced topics, scaling, future directions |

> **Location:** [reference/how_to_build_a_video_agent_system/](./reference/how_to_build_a_video_agent_system/)

10.2 Complete Document Inventory

Functional Specifications (English)

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

Technical Specifications (English)

| Document | Agent/System | Status |
|----------|-------------|--------|
| [general_creative_agent_technical_specification.md](./general_creative_agent_technical_specification.md) | GCA Implementation | Complete |
| [optimization_agent_technical_specification.md](./optimization_agent_technical_specification.md) | Optimization Agent Architecture | Complete |
| [research_agent_technical_specification.md](./research_agent_technical_specification.md) | Research Agent Redevelopment | Complete |

System-Level Documents (English)

| Document | Covers | Status |
|----------|--------|--------|
| [agents.md](./agents.md) | Full 114-agent roster with categories | Complete |
| [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) | Complete production workflow + runtime architecture | Complete |
| [human_video_production_workflow.md](./human_video_production_workflow.md) | Human baseline (52 crew roles) | Complete |
| [complex_problem_solution_process_model.md](./complex_problem_solution_process_model.md) | WHAT/WHY/HOW/DO/REVIEW methodology | Complete |
| [system_build_plan.md](./system_build_plan.md) | Ultra-detailed implementation plan for building the whole system (target build agent: Claude Code; milestones M0–M12 + 100-point hardening) | Complete |
| [video_generation_techology_should_learn_now.md](./video_generation_techology_should_learn_now.md) | 50 AI video generation models (April 2026) | Complete |
| [lifes_quiet_redemption_agent_workflow.md](./lifes_quiet_redemption_agent_workflow.md) | Worked example: agent-mapped + research-informed short-film workflow (with diagrams) | Complete |

Chinese (香港繁體) Translations

All major documents have `_hk.md` counterparts providing Hong Kong Traditional Chinese translations. These follow the same naming pattern (e.g., `agents_hk.md`, `optimization_agent_functional_specification_hk.md`).

10.3 Workflow Diagram Gallery — "Life's Quiet Redemption" (Worked Example)

A worked end-to-end example of the system applied to a 60-second cinematic short. The six diagrams below (in [`./workflows/`](./workflows/)) visualize how the 114-agent swarm, the gate ladder, and the 2026 engine/research upgrades come together. Full write-up: [lifes_quiet_redemption_agent_workflow.md](./lifes_quiet_redemption_agent_workflow.md) ([香港繁體](./lifes_quiet_redemption_agent_workflow_hk.md)).

<table>
  <tr>
    <td width="33%" align="center"><a href="./workflows/lqr-pipeline-overview.svg"><img src="./workflows/lqr-pipeline-overview.svg" width="260" alt="6-phase pipeline overview"/></a><br/><b>D1 · Pipeline Overview</b><br/>6-phase DAG, gates, feedback loop</td>
    <td width="33%" align="center"><a href="./workflows/lqr-scene-flow.svg"><img src="./workflows/lqr-scene-flow.svg" width="260" alt="scene flow, emotional arc, retention bands"/></a><br/><b>D2 · Scene Flow</b><br/>Arc, retention bands, per-shot engine</td>
    <td width="33%" align="center"><a href="./workflows/lqr-per-shot-loop.svg"><img src="./workflows/lqr-per-shot-loop.svg" width="260" alt="per-shot generation loop"/></a><br/><b>D3 · Per-Shot Loop</b><br/>3E + visual anchor + VBench + MCTS</td>
  </tr>
  <tr>
    <td width="33%" align="center"><a href="./workflows/lqr-character-consistency.svg"><img src="./workflows/lqr-character-consistency.svg" width="260" alt="character consistency identity stack"/></a><br/><b>D4 · Consistency Stack</b><br/>Identity youth→adult</td>
    <td width="33%" align="center"><a href="./workflows/lqr-engine-routing.svg"><img src="./workflows/lqr-engine-routing.svg" width="260" alt="engine routing tiers"/></a><br/><b>D5 · Engine Routing</b><br/>Grok Imagine + hero engines + cost</td>
    <td width="33%" align="center"><a href="./workflows/lqr-quality-gates.svg"><img src="./workflows/lqr-quality-gates.svg" width="260" alt="quality gate ladder and VBench scorecard"/></a><br/><b>D6 · Quality Gates</b><br/>L1/L2/L3 + VBench scorecard</td>
  </tr>
</table>

> If a thumbnail does not render, click it to open the full SVG. Diagrams follow the same visual language as [common-agent-structure.svg](./common-agent-structure.svg).

---

11. Implementation Priority & Dependencies

11.1 Foundation Layer (Build First)

These must exist before any production agent can function:

'''
1. Agentic RAG System          ← Knowledge backbone for all agents
   └── agentic_rag_functional_specification.md

2. Orchestration Runtime        ← DAG execution, routing, state
   └── agents.md §9 (OrchestratorAgent, PlannerAgent, RouterAgent)

3. Research Agent               ← Knowledge acquisition service
   └── research_agent_functional_specification.md
   └── research_agent_technical_specification.md

4. Coding Agent                 ← Builds all other agents
   └── coding_agent_functional_specification.md

5. LLM Usage Dashboard          ← Cost monitoring from day one
   └── llm_usage_functional_specification.md
'''

11.2 Intelligence Layer (Build Second)

These provide reasoning capabilities that production agents consume:

'''
6. Deep Intent Analysis (DIA)   ← Parses user briefs into structured intents
   └── intent_analysis_agent_functional_specification.md

7. General Creative Agent (GCA) ← Creative ideation engine
   └── general_creative_agent_functional_specification.md
   └── general_creative_agent_technical_specification.md

8. Process Optimization Agent   ← Workflow improvement engine
   └── optimization_agent_functional_specification.md
   └── optimization_agent_technical_specification.md

9. Strategic Goal Achievement   ← Goal clarification for all planning
   └── strategic_goal_achievement_agent_functional_specification.md

10. Complex Problem Solving     ← Diagnostic reasoning framework
    └── complex_problem_solution_process_model.md
'''

11.3 Production Layer (Build Third)

The 52 core production agents (1–52) from the master roster, activated per workflow type.

11.4 Enhancement Layer (Build Fourth)

'''
11. Psychological Profiling     ← Personalizes creator/audience modeling
    └── psychological_profile_agent_functional_specifications.md

12. Psychological Recommendation ← Audience preference prediction
    └── psychological_recommendation_agent_functional_specification.md

13. Podcast Agent               ← Audio-first production variant
    └── podcast_agent_functional_specifcation.md
'''

11.5 Dependency Graph

'''
                    ┌─────────────────┐
                    │  Coding Agent   │ ← Builds everything
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
    ┌─────────────┐  ┌─────────────┐  ┌──────────────┐
    │ Agentic RAG │  │ Orchestrator│  │ LLM Dashboard│
    └──────┬──────┘  └──────┬──────┘  └──────────────┘
           │                │
     ┌─────┴─────┐    ┌────┴────┐
     ▼           ▼    ▼         ▼
┌─────────┐ ┌──────┐ ┌──────┐ ┌──────────┐
│Research │ │ DIA  │ │Router│ │ Planner  │
│ Agent   │ │      │ │Agent │ │  Agent   │
└────┬────┘ └──┬───┘ └──┬───┘ └────┬─────┘
     │         │         │          │
     └─────────┴─────────┴──────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │  52 Production Agents (1–52) │
    │  + GCA + Optimization Agent   │
    │  + Goal Framework             │
    │  + Psychological Profiling    │
    └───────────────────────────────┘
'''

---

12. How to Use This Document

1. **Starting a new implementation?** → Begin with §11 (Priority & Dependencies), then follow the Foundation → Intelligence → Production → Enhancement sequence. For a concrete, step-by-step build (milestones M0–M12, acceptance gates, and a 100-point hardening checklist) targeting the **Claude Code** build agent, follow [system_build_plan.md](./system_build_plan.md).

2. **Need to understand a specific agent?** → Find it in §3 (Agent Categories), then follow the "Deep Specification" link.

3. **Designing a new workflow?** → Check §6 (Workflow Integration) for the pipeline phases and §6.2 for existing workflow variants.

4. **Integrating agents together?** → See §7 (Data Flow & Handoff Contracts) for the shared manifest format and critique bus protocol.

5. **Building the UI?** → See §8 for all UI/communication documents.

6. **Need reference material?** → See §10 for the complete inventory including the 68-chapter deep reference.

---

*Document generated: May 27, 2026*  
*Covers: 114 agents, 12 functional specifications, 3 technical specifications, 10 workflow variants, 68 reference chapters*




Document: `study/knowledge_router_agent.md`

_Embedded from `corpus/study/knowledge_router_agent.md`. Also stored at `sources/study/knowledge_router_agent.md` under this agent folder._


Knowledge Router Agent — Complete Specification & Implementation Guide
**Version:** 1.0  
**Date:** 2026-06-06  
**Status:** Production-Ready Spec (Rethought across research papers, best practices, and your specific use cases)  
**Domains:** AI Filmmaking (text-to-video, consistency, cinematic pipelines) + AI Agents (multi-agent orchestration, advanced RAG, self-improving systems)  
**Philosophy:** Spec-driven, critic-loop heavy, hybrid deterministic + learned routing, fully traceable, continuously improving.

---

Executive Summary

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

1. Purpose & Success Criteria

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

2. Architecture Overview

'''
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
'''

**Key Design Principles**
- **Metadata First**: Hard constraints eliminate 70-80% of irrelevant files instantly.
- **Graph-Guided Intelligence**: Relationships between concepts (e.g., “character consistency techniques improve multi-shot narrative in Seedance”) enable smarter routing.
- **Iterative Refinement**: For complex queries (full AI video production pipeline), Planner + iterative evaluation/simplification (RopMura style).
- **Self-Reflection**: The Router itself uses reflection tokens / critic steps (Self-RAG inspired) to judge its own retrieval quality before finalizing output.
- **Generalized + Extensible**: Core logic is domain-agnostic; domain packs and agent_relevance tags make it powerful for your AI Filmmaking + AI Agents corpus.

---

3. Input / Output Contract (Strict & Rich)

Input from Requesting Agent
'''json
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
'''

Output from Router
'''json
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
'''

---

4. Core Components (Detailed)

4.1 Query Analyzer + Intent Classifier
- Parses task_description + required_concepts + previous_failures.
- Extracts entities (tools: Seedance, Kling; concepts: character_consistency).
- Classifies complexity and whether Planner is needed.
- Uses lightweight reflection: “Is this query about a single technique or a full pipeline?”

4.2 Planner (for High-Complexity / Pipeline Queries)
Inspired by RopMura: When `routing_hints.complexity == "pipeline"` or `multi_hop_expected == true`:
- Decomposes into sub-tasks (e.g., 1. Character bible creation, 2. Shot-by-shot consistency rules, 3. Lighting-specific mitigations, 4. Tool-specific prompt patterns).
- Routes sub-tasks iteratively or in parallel.
- Uses Question Simplifier / Response Evaluator loop (max 4–5 rounds).

4.3 Hybrid Retrieval Engine (The Heart)
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

4.4 Context Assembler
- Options: raw top chunks | synthesized summary | structured knowledge pack (best for your critic-heavy agents).
- For creative agents: often returns “Knowledge Pack” with sections like Best Practices, Failure Modes & Mitigations, Tool-Specific Notes, Prompt Templates.

4.5 Explainer & Traceability
Every output includes a clear `reasoning_trace` (structured + natural language). This is non-negotiable for debugging and critic loops.

4.6 Multi-Level Critic (Self-Improving Core)
Three levels:
1. **Retrieval Critic**: Scores relevance, coverage of required_concepts, handling of previous_failures.
2. **Routing Critic**: Judges whether the right files were chosen vs alternatives; suggests better tags or graph edges.
3. **Downstream Utility Critic**: (Ideal) Observes or gets feedback from the requesting agent after it uses the context (“Did this knowledge help you succeed? What was missing?”). Feeds back as soft supervision signal (like AgentRouter’s F1-based training targets).

This turns the Router into a learning system over time.

---

5. Particular Use Case Implementations

Use Case 1: Character Consistency Critic Agent
**Request Example**: See Input contract above (wuxia fight scene).

**Router Behavior**:
- Hard filter: `tags CONTAIN character_consistency AND multi_shot`
- Graph: Pulls “clothing_drift” failure mode nodes + mitigation techniques
- Returns structured pack: “Best reference sheet practices for Seedance + Kling”, “Lighting-induced color shift mitigations”, “Multi-shot coherence checklist”
- Critic checks coverage of “previous_failures”

Use Case 2: Video Prompt Optimizer Agent
- Prioritizes files tagged `prompt_engineering`, `camera_movement_prompts`, `lighting_prompts`, `negative_prompts`, `seedance_prompt_formulas`, `2026_best_practices`
- Graph traversal for “prompt formula that worked with dynamic camera in cinematic scenes”
- Returns prompt templates + before/after examples + common failure prompts to avoid

Use Case 3: Multi-Agent Orchestrator Designer
- Routes to `multi_agent_patterns`, `langgraph`, `crewai_roles`, `memory_architectures`, `production_ready_patterns`, `agentic_video_production`
- Planner decomposes: “Orchestration for consistency across shots” + “Cost/latency optimization for video gen agents”
- Returns role definitions, graph patterns, and real pipeline examples from your corpus

Use Case 4: Shot Planning Agent (Script → Shot List → Generation)
- High complexity → activates Planner
- Iterative routing across scriptwriting, cinematography language, tool-specific shot capabilities, consistency constraints
- Final pack: Structured shot list template + per-shot prompting guidance + consistency guardrails

**Generalization Note**: For any new domain, simply:
- Add `agent_relevance` values in frontmatter
- Define new clusters / graph node types
- Optionally create a small “Domain Pack” template

---

6. Knowledge Base Integration Requirements

Every `.md` file **must** have rich frontmatter (this is non-negotiable for the Router to work well):

'''yaml
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
'''

**Recommended Additions for Scale**:
- Pre-computed cluster_id or centroid_id per file
- Graph node references (optional but powerful)

---

7. Phased Implementation Roadmap

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

8. Evaluation Framework

- **Offline**: Golden test set of 50–100 representative queries per major agent role. Measure precision@K, recall of required_concepts, critic scores.
- **Online**: Track downstream agent success rate before/after Router improvements. Log critic scores and human spot-checks.
- **Ablation**: Test impact of each layer (metadata only vs +graph vs +reflection).
- **Continuous**: Router critic proposes improvements to the knowledge base itself (new tags, missing content detection).

---

9. Edge Cases & Mitigations

- **Very broad query** → Planner forces decomposition + strict max_files.
- **No good matches** → Router returns “Insufficient high-quality knowledge” + suggestions to expand corpus + low confidence flag.
- **Conflicting information** across files → Graph + Critic prioritize higher quality_score + more recent + explicit failure mode coverage.
- **New agent role appears** → Easy extension: add to `agent_relevance` tags; Router gradually learns via feedback.
- **Latency spikes on complex queries** → Planner has round limits; fallback to simpler retrieval.

---

10. Tech Recommendations (Aligned with Your Stack)

- **Orchestration**: LangGraph or your custom harness (excellent for stateful Planner + Router + Critic loops)
- **Vector + Metadata**: LlamaIndex or Haystack with Qdrant/Pinecone (strong metadata filtering)
- **Graph**: Lightweight NetworkX/Neo4j for traversal; optional small GNN later (PyG or DGL)
- **Embeddings**: High-quality model (e.g., voyage, Snowflake, or your preferred)
- **LLM for Analyzer/Ranker/Critic**: Mix of strong reasoning model (Grok 4, Claude 4, DeepSeek R1, etc.) + cheaper models for simple steps
- **Storage**: All `.md` files in git + vector DB + optional graph DB

---

11. Generalization to Any Domain

This design is deliberately **domain-agnostic at the core**:
- Replace `category` / `subcategory` / `agent_relevance` with your new domain’s taxonomy.
- Define new clusters and graph schemas.
- The Hybrid Retrieval + Planner + Multi-Level Critic pattern transfers directly.

Your AI Filmmaking + AI Agents corpus is actually an **excellent stress test** because it combines creative, technical, and meta-agent knowledge — success here means the Router will generalize extremely well.

---

Next Steps (Recommended)

1. Review and refine this spec with your main Critic Agent.
2. Start Phase 1 implementation (I can generate the detailed task.md + code skeletons next).
3. Audit/enrich frontmatter on your top 300–500 highest-value files.
4. Build the first version of the Metadata + Vector layer and test with 2–3 of your real agents.

This specification has been deeply researched and rethought for production robustness, your specific creative + agent use cases, and alignment with the latest 2025–2026 research patterns.

**File created at:** `/home/workdir/artifacts/knowledge_router_agent.md`

Ready for the next artifact (task.md for implementation, code skeletons, or graph schema)? Just say the word. We can iterate until it is perfect for your N1ch01as Architect ecosystem.


Additional corpus / va passages naming this agent


From `corpus/study/ai_agent_video_production_workflow.md` Copy: `sources/excerpts/ai_agent_video_production_workflow.md`.


| Layer | Core responsibility | Implementation notes |
|---|---|---|
| **Orchestration runtime** | Plan, route, schedule, retry, and escalate agent tasks | PlannerAgent decomposes the brief; OrchestratorAgent executes the DAG; RouterAgent selects agent-model pairs; JudgeAgent arbitrates disputes |
| **Asset and data backbone** | Store every prompt, source asset, derived asset, version, dependency edge, and usage right | Requires immutable asset IDs, copy-on-write versions, dependency-triggered rerender rules, and searchable metadata |
| **Message and state fabric** | Carry critique, job status, render events, and gate decisions across agents | Event-driven bus plus durable state store; every long-running job must be resumable and auditable |
| **Quality and continuity mesh** | Run technical QC, continuity checks, artifact detection, accessibility, and compliance gates | Uses multi-pass validation, temporal continuity scans, loudness and color checks, and role-specific rubric judges |
| **Observability and replay** | Expose live status, failure causes, bottlenecks, and historical decisions | Structured logs, job timelines, gate dashboards, benchmark alerts, and replayable artifact lineage |
| **Delivery fabric** | Package masters into theatrical, streaming, broadcast, archive, trailer, and campaign variants | Distribution is a branching pipeline with outlet-specific specs, captions, metadata, DRM/KDM, and provenance payloads |
| **Compute and storage scaling** | Match infrastructure spend to production scale without breaking deadlines | Separate interactive generation from batch rendering; autoscale GPU pools; tier hot, warm, and archive storage |

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
| 73 | **PromptOptimizerAgent** | Auto-improves prompts via OPRO / APE / DSPy / Promptbreeder | OPRO (Yang 2023), APE (Zhou 2022), DSPy (Stanford), Promptbreeder (DeepMind) | Score uplift per iteration on held-out eval; iteration count to convergence | Beats Karen X. Cheng / Paul Trillo-style hand-tuned prompts on held-out briefs | PromptEngineerAgent, AIQAAgent | PromptEngineerAgent (sub-optimal seed) |
| 74 | **CostOptimizerAgent** | Routes between models / providers for $/quality | Provider pricing sheets; benchmark cost-quality frontiers; FrugalGPT patterns | $/successful-task; Pareto distance from cost-quality frontier | Lower $/quality than human CFO + producer routing decisions | RouterAgent, FinanceAgent | RouterAgent (over-spend), GeneratorAgent (re-roll burn) |
| 75 | **LatencyOptimizerAgent** | Parallelization, caching, speculative decoding, batch packing | vLLM, TensorRT-LLM, distillation literature; Anyscale/Ray patterns | p50/p95 latency; throughput per GPU-hour | Lower p95 than human-tuned pipeline at equal quality | OrchestratorAgent | OrchestratorAgent (serial bottleneck) |
| 76 | **RetentionOptimizerAgent** | Tunes hook, pacing, structure for AVD / hold-rate | YouTube Analytics public benchmarks; TikTok retention curves; AudienceSim outputs | Predicted retention curve vs actual; AVD lift over control | Beats senior YouTube editor on AVD lift in A/B | EditorAgent, AudienceSimAgent | EditorAgent (slow opener), ScriptwriterAgent (front-loaded fluff) |
| 77 | **ROASOptimizerAgent** | Optimizes ad creatives for performance metrics | Meta Marketing Science, TikTok Ads Academy, MMM/MTA literature | ROAS uplift vs control; significance ≥95% | Beats senior performance marketer at equal budget | PerformanceMarketerAgent, AnalystAgent | UGCAgent (low hook-rate), CopywriterAgent (weak CTA) |
| 78 | **AccessibilityOptimizerAgent** | WCAG 2.2 contrast, caption timing, audio description quality, color-blind safe palette | WCAG 2.2 spec; W3C/WAI-ARIA; DCMP captioning key; Deaf/HoH community guidelines | WCAG-conformance score 100% AA, ≥90% AAA; caption WER ≤2% | Catches more a11y defects than ADA-certified human auditor | AccessibilityAgent (HiTL), ComplianceAgent | EditorAgent (caption sync), ColoristAgent (contrast) |
| 79 | **EvaluationHarnessAgent** | Continuously runs benchmarks (VBench, EvalCrafter, MT-Bench, FVD, CLIP-T) and posts regressions | Papers-with-Code; HuggingFace leaderboards; benchmark code repos | Regression detection precision/recall; alert latency <1h | Catches regressions faster than ML-eng team rotation | BenchmarkResearchAgent | All AI agents (regression alerts) |
| 80 | **SafetyRedTeamAgent** | Adversarially attacks outputs for deepfake, bias, jailbreak, defamation | Hany Farid lab benchmarks; Partnership on AI Synthetic Media Framework; OWASP LLM Top 10 | Attack-success rate kept ≤1%; coverage of attack taxonomy | Higher coverage than internal red-team rotation | EthicsAgent (HiTL), ComplianceAgent | AvatarDesignAgent, VoiceCloneAgent, AllGeneratorAgents |

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


| # | Diagram | Describes | Maps to section |
|---|---|---|---|
| D1 | Pipeline Overview | The 6-phase DAG, owning agents, exit gates, and the analytics feedback loop | §1, §5 |
| D2 | Scene Flow | The 14-card timeline, emotional arc, retention bands, and per-shot engine | §2, §10, §15 |
| D3 | Per-Shot Loop | The 3E micro-loop, mandatory visual anchor, VBench gate, and MCTS reroute | §3.4, §13, §14 |
| D4 | Character-Consistency Stack | The identity pipeline keeping characters stable youth→adult | §3.3, §12 |
| D5 | Engine Routing | RouterAgent tiers incl. Grok Imagine, hero engines, and cost optimization | §3.4, §11 |
| D6 | Quality Gate Ladder | The L1/L2/L3 gates and the VBench/VMBench scorecard | §5, §13 |

D5 · Engine Routing (RouterAgent Tiers)
![Engine routing tiers: Grok Imagine draft and image-to-video, agent-mode rough cut, hero engines, local ComfyUI, cost optimizer](./workflows/lqr-engine-routing.svg)

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

The routing in §3.4 (RouterAgent #55) gains a Grok tier. Net effect: cheaper, faster iteration up front; premium engines reserved for hero shots.

| Stage | Engine Choice | Why (cited) | Agent |
|---|---|---|---|
| Divergent draft / variant browse | **Grok Imagine 1.5 Fast** (6s, 720p, ~25s/clip) | Fast enough to try many framings and discard quickly ([x.ai]([historical-url] [imagine.art]([historical-url] | PromptEngineerAgent (#46), RouterAgent (#55) |
| Keyframe → motion (identity-safe) | **Grok Imagine 1.5 I2V** (animates the locked keyframe, faithful to source) | Continues the still rather than reinterpreting it, protecting face + lighting ([x.ai]([historical-url] | PromptEngineerAgent (#46), ContinuityAgent (#98) |
| Fast full-film rough cut | **Grok Imagine Agent Mode** (plans/stitches 6s clips, native audio, in-quotes lip-sync) | Produces a stitched draft of the whole arc for early editorial review ([codersera]([historical-url] | OrchestratorAgent (#53), EditorAgent (#9) |
| Hero / emotional-peak shots | **Veo 3.1 / Kling 3.0 / Runway Gen-4** | Higher fidelity + camera control for Scenes 1, 5, 10, 12 | CinematographerAgent (#6) |
| Local / privacy-sensitive | **ComfyUI + CharCom LoRAs + IP-Adapter** | Full control, per-character LoRA identity ([arXiv CharCom]([historical-url] | StyleTransferAgent (#61) |



From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


| Concern | Choice | Notes |
|---------|--------|-------|
| Backend / agents | **Python 3.12** | LangGraph, Temporal SDK, litellm, ML tooling all Python-first. |
| Python env & deps | **uv** (lockfile-driven) | Fast, reproducible; one workspace lock. |
| Frontend | **TypeScript 5.x, React 19, Next.js 15 (App Router)** | Per [`ui/architecture_communication.md`](./ui/architecture_communication.md). |
| JS package mgr / monorepo | **pnpm workspaces + Turborepo** | Caches builds across `apps/*` + `packages/*` (TS side). |
| Lint/format | **ruff** (Py), **eslint + prettier** (TS) | Enforced in hooks + CI. |
| Types | **pyright/mypy (strict)** (Py), **tsc strict** (TS) | No untyped public surface. |
| Tests | **pytest + pytest-asyncio + hypothesis** (Py), **vitest + Playwright** (TS) | Property tests for contracts; Playwright for UI E2E. |

> **Decision (ADR-002):** All providers implement a common `Provider` protocol with `capabilities()`, `estimate_cost()`, `invoke()`, and `health()`. The `RouterAgent` selects among providers by cost/quality/latency. CI uses mock providers exclusively.

'''text
M0 Bootstrap ──► M1 RAG ──► M2 Orchestration ──► M3 LLM Gateway+Router+CostDash
                                  │                       │
                                  ▼                       ▼
                          M4 Research+Coding harness   M5 Intelligence (DIA,GCA,Opt,Goal,CPS,Aesthetics)
                                  │                       │
                                  └───────────┬───────────┘
                                              ▼
                                  M6 Agent Factory + VERTICAL SLICE (Workflow A) ◄── proves architecture
                                              ▼
                                  M7 Production agents 1–52 (factory breadth)
                                              ▼
                                  M8 Meta-agents 53–80 + QC mesh + GateKeeper
                                              ▼
                                  M9 Support agents 81–114 + Delivery fabric
                                              ▼
                                  M10 UI (web + gateway + websocket)   ── can start in parallel after M3 via worktree
                                              ▼
                                  M11 Enhancement (psych, podcast, personalization)
                                              ▼
                                  M12 Hardening, scale, security, launch (the §14 100-point pass)
'''

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

M3 — Foundation: LLM Gateway, Router & Cost Dashboard

**Goal:** Every token metered and routed from day one (G6). Specs: [`llm_usage_functional_specification.md`](./llm_usage_functional_specification.md); RouterAgent in [`agents.md`](./agents.md) §9.

**Build:**
- `packages/llm-gateway`: litellm wrapper exposing `complete()/stream()/embed()` with: provider/model abstraction (Grok-4.x, Gemini 2.5 Pro, GPT-4o, Claude 4, OSS), automatic retry/fallback, **per-call token+cost metering** emitted to the bus (`budget_update`), prompt+model **version tagging** into provenance (G5), response caching, and a **frozen-judge** mode for QC.
- **RouterAgent (#55)** real impl: capability registry + benchmark history → pick agent/model by cost/quality/latency; budget-aware. **CostOptimizerAgent (#74)** hooks.
- **LLM Usage Dashboard** backend: aggregates spend per production/agent/provider; alert thresholds; exposes `/api/llm-usage`.
- Budget guardrails: per-production budget envelope; hard stop + escalation when exceeded (ProducerAgent gate).

**Tests:** cost computed correctly per provider; fallback on provider error; budget-exceeded halts + emits escalation; router picks the Pareto-optimal provider on a fixture matrix; cache hit avoids a call; every call writes model+prompt version to provenance.

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
| R13 | Scope creep (role inflation: new agents that close no real gap) | Med | Med | Reject per workflow-doc rule §1.1 working-rule #4; ADR noted for any agent beyond the 114 |

| M | Milestone | Acceptance Gate (one-line) | Primary specs |
|---|-----------|----------------------------|---------------|
| M0 | Bootstrap + Claude config | Clean clone → `make verify` green; `.claude/` live | SYSTEM_REFERENCE §11 |
| M1 | Agentic RAG | precision@5 ≥0.9 on golden corpus; graded citations | agentic_rag |
| M2 | Orchestration runtime | 3-node DAG survives worker kill; typed events; C2PA | workflow §1.2; ui/architecture |
| M3 | LLM gateway + Router + Cost | every call metered/routed/version-tagged; budget stop | llm_usage; agents §9 |
| M4 | Research + Coding harness | cited dossier in RAG; conventions enforced | research_*; coding_agent |
| M5 | Intelligence layer | 6 reasoning services pass golden behavioral tests | intent/gca/optimization/goal/cps/aesthetics |
| M6 | Factory + Vertical Slice A | `make e2e-workflow-a` signed deliverable on mocks | workflow §3.1 |
| M7 | Production agents 1–52 | all 52 green on L1+L2+critique; 3 more workflows E2E | agents §1–8 |
| M8 | Meta-agents 53–80 + QC | all 80 live; full L1/L2/L3+Q1–Q6; red-team+harness nightly | workflow §2.9, §5 |
| M9 | Support 81–114 + delivery | 4 delivery branches Q6-valid; learning loop closes | agents §10; workflow §3.0 |
| M10 | UI + gateway + WS | human runs Workflow A fully in browser, live | all ui/ |
| M11 | Enhancement | personalized/cohort variants under consent; podcast E2E | psych_*; podcast |
| M12 | Hardening + launch | 100/100 checks; Workflow J all-114 dry-run; live-smoke | §14 |



From `corpus/root/agent_loop_creator_v1.md` Copy: `sources/excerpts/agent_loop_creator_v1.md`.


3.3 Key Modules to Implement (with Skeletons from attached + Enhancements)
- **core/loop.py**: `controlled_react_loop` (enhance attached code with Pydantic, full state, MASFT-aware prompts, xAI hybrid hooks, progress tracking).
- **reliability/circuit_breaker.py**: Enhanced class with metrics, per-tool/role instances, integration with safe_execute.
- **reliability/verifier.py**: `verify_output` + `VERIFIER_PROMPT` tuned to catch FM-1.x/2.x/3.x (e.g., "Does this respect original task_spec and roles? Any premature termination or incomplete verification? Cross-check claims vs observations.").
- **hierarchical/orchestrator.py**: Planner logic, delegation router, sub-agent factory, consolidator.
- **evolution/self_evolver.py**: `self_evolve_component` (TextGrad-style: diagnose from trace, propose_edit, validate_improvement, VersionManager.register).
- **tea/protocol.py**: Minimal TCP/ECP/ACP schemas, register_tool/register_agent, get_context_slice, VersionManager.
- **integrations/xai.py**: `call_grok_multi_agent(sub_spec, tools_enabled, context_slice)` → parse leader result into StructuredObservation.
- **memory/ & tracing/**: As described.
- **prompts/**: Versioned JSON/YAML or .md files for system prompts, few-shots (ReAct decision, verifier, planner, reflector, sub-roles). Include MASFT failure mode references in critic prompts.



From `corpus/root/agent_loop_creator_v2.md` Copy: `sources/excerpts/agent_loop_creator_v2.md`.


3.3 Key Modules to Implement (with Skeletons from attached + Enhancements)
- **core/loop.py**: `controlled_react_loop` (enhance attached code with Pydantic, full state, MASFT-aware prompts, xAI hybrid hooks, progress tracking).
- **reliability/circuit_breaker.py**: Enhanced class with metrics, per-tool/role instances, integration with safe_execute.
- **reliability/verifier.py**: `verify_output` + `VERIFIER_PROMPT` tuned to catch FM-1.x/2.x/3.x (e.g., "Does this respect original task_spec and roles? Any premature termination or incomplete verification? Cross-check claims vs observations.").
- **hierarchical/orchestrator.py**: Planner logic, delegation router, sub-agent factory, consolidator.
- **evolution/self_evolver.py**: `self_evolve_component` (TextGrad-style: diagnose from trace, propose_edit, validate_improvement, VersionManager.register).
- **tea/protocol.py**: Minimal TCP/ECP/ACP schemas, register_tool/register_agent, get_context_slice, VersionManager.
- **integrations/xai.py**: `call_grok_multi_agent(sub_spec, tools_enabled, context_slice)` → parse leader result into StructuredObservation.
- **memory/ & tracing/**: As described.
- **prompts/**: Versioned JSON/YAML or .md files for system prompts, few-shots (ReAct decision, verifier, planner, reflector, sub-roles). Include MASFT failure mode references in critic prompts.



From `corpus/root/project_starter_0.2.md` Copy: `sources/excerpts/project_starter_0.2.md`.


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
  - noted directories  
- [ ] Add `.editorconfig`, `.gitignore`, `README.md`, and base docs.  
- [ ] Add empty manifests with JSON schemas.  
- [ ] Add first `task.md` and `status.md`.



From `corpus/root/project_starter_0.5.md` Copy: `sources/excerpts/project_starter_0.5.md`.


The router must also support create-new-project mode either directly or by delegating to:



From `corpus/study/agents.md` Copy: `sources/excerpts/agents.md`.


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
| 73 | **PromptOptimizerAgent** | Auto-improves prompts via OPRO/APE/DSPy/Promptbreeder | OPRO (Yang 2023); APE (Zhou 2022); DSPy (Stanford); Promptbreeder (DeepMind) | Score uplift per iteration; convergence speed | Beats hand-tuned prompts on held-out briefs | PromptEngineerAgent, AIQAAgent | PromptEngineerAgent (sub-optimal seed) | DSPy framework (MIPRO optimizer); OPRO implementation; held-out eval harness | DSPy compilation + OPRO meta-optimization |
| 74 | **CostOptimizerAgent** | Routes between models/providers for $/quality | Provider pricing; cost-quality frontiers; FrugalGPT patterns | $/successful-task; Pareto distance from frontier | Lower $/quality than human CFO routing | RouterAgent, FinanceAgent | RouterAgent (over-spend), GeneratorAgent (re-roll burn) | Provider pricing APIs; benchmark cost DB; FrugalGPT cascade logic | ReAct (evaluate task → pick cheapest model meeting threshold) |
| 75 | **LatencyOptimizerAgent** | Parallelization, caching, speculative decoding, batching | vLLM; TensorRT-LLM; distillation; Anyscale/Ray | p50/p95 latency; throughput/GPU-hour | Lower p95 than human-tuned pipeline | OrchestratorAgent | OrchestratorAgent (serial bottleneck) | vLLM; TensorRT-LLM; Ray Serve; Redis (response cache); speculative decoding configs | Tool-use profiling + automated pipeline restructuring |
| 76 | **RetentionOptimizerAgent** | Tunes hook, pacing, structure for AVD/hold-rate | YouTube Analytics benchmarks; TikTok retention curves; AudienceSim | Predicted retention vs actual; AVD lift over control | Beats senior YouTube editor on AVD lift (A/B) | EditorAgent, AudienceSimAgent | EditorAgent (slow opener), ScriptwriterAgent (front fluff) | YouTube Analytics API; retention-curve predictor model; A/B test framework | RLAIF (reward = retention uplift from real analytics) |
| 77 | **ROASOptimizerAgent** | Optimizes ad creatives for performance | Meta Marketing Science; TikTok Ads Academy; MMM/MTA lit | ROAS uplift vs control; significance ≥95% | Beats senior marketer at equal budget | PerformanceMarketerAgent, AnalystAgent | UGCAgent (low hook), CopywriterAgent (weak CTA) | Meta Ads API (creative testing); TikTok Ads; Bayesian MMM tools (Robyn/Meridian) | RLAIF (reward = real ROAS from ad platform feedback) |
| 78 | **AccessibilityOptimizerAgent** | WCAG 2.2 contrast, captions, audio description, color-blind safe | WCAG 2.2; W3C/WAI-ARIA; DCMP captioning key; Deaf/HoH guidelines | Conformance 100% AA, ≥90% AAA; caption WER ≤2% | Catches more a11y defects than ADA-certified auditor | AccessibilityAgent (HiTL), ComplianceAgent | EditorAgent (caption sync), ColoristAgent (contrast) | axe-core/Lighthouse (contrast); Whisper v4 (captioning); audio-description generator | Constitutional AI (constitution = WCAG 2.2 success criteria) |
| 79 | **EvaluationHarnessAgent** | Runs benchmarks (VBench, EvalCrafter, MT-Bench, FVD, CLIP-T); posts regressions | Papers-with-Code; HuggingFace leaderboards; benchmark repos | Regression precision/recall; alert latency <1h | Catches regressions faster than ML-eng rotation | BenchmarkResearchAgent | All AI agents (regression alerts) | VBench suite; EvalCrafter; MT-Bench harness; CI/CD (GitHub Actions); alerting (PagerDuty) | Tool-use / ReAct (run benchmark → compare → alert if regressed) |
| 80 | **SafetyRedTeamAgent** | Adversarially attacks for deepfake, bias, jailbreak, defamation | Hany Farid benchmarks; Partnership on AI Framework; OWASP LLM Top 10 | Attack-success kept ≤1%; taxonomy coverage | Higher coverage than internal red-team rotation | EthicsAgent (HiTL), ComplianceAgent | AvatarDesignAgent, VoiceCloneAgent, AllGenerators | Deepfake detectors (Farid lab models); bias probes; jailbreak prompt banks; OWASP scanner | Multi-agent debate (red-team vs defender) + adversarial search |

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

'''text
[Brief] ──► PlannerAgent ──► OrchestratorAgent ──► RouterAgent ──► (52 craft agents §1–§8)
                 ▲                  │                                       │
                 │                  ▼                                       ▼
             MemoryAgent      GateKeeperAgent ◄─── JudgeAgent ◄──── CritiqueMessages
                                    ▲                                       ▲
                                    │                                       │
            [Creative meta:] IdeationAgent · NarrativeArcAgent · StyleTransferAgent · MoodBoardAgent · NoveltyAgent · Emotio
…



From `corpus/study/ui/architecture_communication.md` Copy: `sources/excerpts/architecture_communication.md`.


'''text
USER (Browser)
    │
    │  1. Fills Brief Studio form
    │  2. Clicks [▶ LAUNCH PRODUCTION]
    │
    ▼
FRONTEND (React)
    │
    │  POST /api/productions
    │  Body: { template: "E", title: "Luna", vision: "...",
    │          genre: "sci-fi", duration: 600, budget: 100, ... }
    │
    ▼
API GATEWAY (Backend)
    │
    │  3. Creates Production record in DB
    │  4. Enqueues "start_production" job
    │
    ▼
ORCHESTRATION ENGINE (LangGraph)
    │
    │  5. PlannerAgent receives brief
    │     - LLM call (Gemini 2.5 Pro): decompose brief → phased DAG
    │     - Returns: task list, agent assignments, gate criteria
    │
    │  6. OrchestratorAgent initializes DAG execution
    │     - Creates state machine in LangGraph
    │     - Registers all agent nodes
    │
    │  7. RouterAgent assigns model + provider per task
    │     - Checks cost/quality rules from config
    │
    ▼
AGENT WORKERS (Parallel)
    │
    │  8. DirectorAgent gets "generate shot intent" task
    │     - LLM call: Gemini 2.5 Pro (creative reasoning)
    │     - Tool call: Veo 3.1 API (video generation)
    │     - Self-Refine loop: score with CLIP-T, iterate if < threshold
    │
    │  9. Each completed step:
    │     - Agent → publishes event to Event Bus
    │     - Event Bus → WebSocket Gateway → Frontend (real-time update)
    │
    ▼
FRONTEND receives WebSocket events
    │
    │  10. DAG Canvas node transitions: ○ → ● → ✓
    │  11. Artifact appears in Gallery
    │  12. Critique message appears in Feed
    │  13. Status bar updates (agents running, budget spent)
'''

| Method | Endpoint | Purpose | Called By |
|--------|----------|---------|-----------|
| POST | `/api/productions` | Create + launch production from brief | Brief Studio |
| GET | `/api/productions` | List all productions | Dashboard |
| GET | `/api/productions/{id}` | Get production state | Production Console |
| POST | `/api/productions/{id}/gates/{gid}/decision` | Approve/reject gate | Gate Dialog |
| POST | `/api/productions/{id}/critiques` | Send human critique | Critique Feed |
| POST | `/api/productions/{id}/agents/{aid}/retry` | Retry failed agent | Agent Inspector |
| POST | `/api/productions/{id}/agents/{aid}/skip` | Skip agent task | Agent Inspector |
| PUT | `/api/settings/router-config` | Update model routing rules | Router Config |
| GET | `/api/agents` | List all 114 agent definitions | Agent Registry |
| GET | `/api/productions/{id}/artifacts` | List artifacts | Artifact Gallery |
| GET | `/api/productions/{id}/artifacts/{aid}` | Get artifact + provenance | Artifact Viewer |
| POST | `/api/productions/{id}/delivery/package` | Trigger delivery packaging | Delivery Hub |



From `corpus/study/ui/backend_agent_management.md` Copy: `sources/excerpts/backend_agent_management.md`.


'''text
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
'''

| Backend Responsibility | How It Does It |
|----------------------|----------------|
| **Define agents** | Agent configs stored in DB (prompt, tools, rubric, relationships) |
| **Decide WHEN to run** | DAG dependency graph — only dispatch when predecessors complete |
| **Decide WHICH model** | RouterAgent + cost rules → pick cheapest model that meets quality |
| **Execute agent logic** | Worker loads config → builds LLM prompt → calls LLM → executes tools |
| **Self-refine loop** | Worker checks quality metrics → if below threshold, loops with feedback |
| **Route critiques** | Checks "accepts_critique_from" config → delivers to right agent's queue |
| **Manage state** | PostgreSQL tracks per-agent state, retry count, cost, metrics |
| **Handle failures** | Retry with backoff → cheaper model fallback → human escalation |
| **Enforce gates** | Evaluates criteria → pauses for human → advances on approval |
| **Scale workers** | Horizontal worker pool — add more for parallel agent execution |
| **Persist everything** | Event sourcing — full replay of every decision, critique, artifact |



From `corpus/study/ui/RETHINK_100_IMPROVEMENTS.md` Copy: `sources/excerpts/RETHINK_100_IMPROVEMENTS.md`.


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



From `corpus/study/ui/ui_design.md` Copy: `sources/excerpts/ui_design.md`.


'''text
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
'''

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

'''text
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
'''

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
   ├── AnalystAgent collects
…



From `corpus/study/ui/video_remake_enhancement.md` Copy: `sources/excerpts/video_remake_enhancement.md`.


Once launched, it flows through the same:
  PlannerAgent → OrchestratorAgent → RouterAgent → Craft Agents → Gates → Delivery
'''



Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


Provenance

- Master roster row va_id=55 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `[historical-path]
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): upstream-va-design.


<!-- self_contained_spec · video.router · va_id=55 -->

Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **RouterAgent** (`video.router`, va_id=55, category `9-Meta`).

Responsibility focus
Picks right specialist agent (and model) for each subtask

Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: agent routing, model selection, mixture-of-experts routing, cost/quality tradeoff routing
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: LLM router agents, specialist agent selection, inference routing for media
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: routing tasks to specialist AI agents, model routers for video tools

arXiv / academic integration (role-applied)
- Classifier + embedding match task→agent capability registries
- FrugalGPT / model cascade routing for cost/latency frontiers

**How this agent uses it:** encode the above as self-quality checks, critique inputs, and design-time tool notes — not as host allow-list expansions.

X / industry practice (role-applied)
- Router as capability registry + benchmark cache pattern

YouTube / practitioner guidance (role-applied)
- Agent selection demos: specialize don't monolith

Implementation notes for v1
1. Emit artifacts matching role responsibility; self-score against Self-quality criteria.
2. Accept critique only from listed critics; escalate disputes to Judge/Gate as DNA dictates.
3. Design-time tools remain documented only; runtime tools stay in `agent_spec.json`.
4. N1: no second control plane; video logic under `business/video/**` only.

Research depth note (honest)
This v1 section maps **role-family** literature and the agent’s migration prompt topics into SPEC.
It is **not** a full unsummarized download of every paper/video transcript.
Live primary-source expansion remains a residual for score 100 on S3 where depth is still thin.

<!-- migration_capability_research · video.router · v1 · 2026-07-13 -->

```


## Prompts

### `prompts/primary.md`

# Prompt — `video.prompt.router.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: ReAct, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **RouterAgent (VA Domain Pack)** (`video.router`), a pack agent in the video domain swarm.

### Responsibility (owns)
Picks right specialist agent (and model) for each subtask

### Does not own
- Host credential storage
- Silent production activation without fail-closed gates
- Inventing action references for irreversible mutations
- Owning other agents' exclusive craft outputs without handoff contract
- Long-running multi-step craft execution

### Operating principles
1. Stay inside responsibility; use typed handoffs for everything else.
2. Prefer evidence and pack sources over invention.
3. Fail closed on missing credentials, missing tools, or irreversible actions without HiTL.
4. Emit structured artifacts that validate against L1 schema before self-scoring.
5. Accept peer critique; refine at most 3 times; escalate blockers.

### Architecture pattern
Classifier + ReAct (match task embedding → agent capability)

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Agent-capability registry; benchmark history (cost/quality/latency)

## Developer

### Tools (allowlist intent)
Design tool surface: Agent registry DB; benchmark leaderboard cache; pricing APIs
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: OrchestratorAgent, CostOptimizerAgent
- May comment on: PlannerAgent (bad decomposition)
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Routing accuracy ≥95% vs oracle; cost within budget

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.router",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **RouterAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.router",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.router`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 21, 26, 30, 31, 37, 38, 59, 63, 87, 88, 89, 93, 94

### Design-time model landscape (non-activating)
- Seedance 2.0 (design-time only)
- Wan 2.6 (design-time only)
- Vidu Q2/Q3 (design-time only)
- Grok Imagine Video (design-time only)
- Hailuo 2.3 (design-time only)
- Kling 2.6/3.0 variants (design-time only)
- Seedance multi-camera (design-time only)
- Flux 1.1 Pro Ultra (design-time only)
- SD 3.5 self-hosted path (design-time only)

### Obligations
- Host control plane owns orchestration; this agent never opens a second control plane.
- Runtime tools remain agent_spec.allowed_tools only; RETHINK model names are design-time.
- Fail closed when tools/providers are unavailable (circuit-breaker posture).
- Prefer iterative verify → refine ≤ max_refinement_count → HiTL over silent pass.
- Emit plain-English reasoning summary in artifacts for operator trust.
- Attach provenance / correlation_id / evidence_refs on every handoff.
- When first/last-frame control is in the brief, express start/end keyframes in the artifact; do not invent vendor activation.
- Verify intermediate narrative/script artifacts before advancing downstream handoffs.
- Maintain a design-time model strengths matrix (quality, cost, latency, consistency); host routing remains authoritative.
- Escalate stereotype/harm/consent risks to ethics/trust-safety/legal gates.
- Track A/V sync and native-audio implications; do not assume silent video when audio is native.
- When ensemble is requested, propose multi-model candidates + selection criterion; host executes tools.

### Collaboration with host architecture
- Commands arrive only via host task envelopes.
- Publish results as structured artifacts; never open browser/UI channels.
- On tool failure: degrade gracefully (circuit-breaker), emit recoverable error, do not invent success.
<!-- RETHINK_100:end -->

### `prompts/video.prompt.router.v1.md`

# Prompt — `video.prompt.router.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: ReAct, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **RouterAgent (VA Domain Pack)** (`video.router`), a pack agent in the video domain swarm.

### Responsibility (owns)
Picks right specialist agent (and model) for each subtask

### Does not own
- Host credential storage
- Silent production activation without fail-closed gates
- Inventing action references for irreversible mutations
- Owning other agents' exclusive craft outputs without handoff contract
- Long-running multi-step craft execution

### Operating principles
1. Stay inside responsibility; use typed handoffs for everything else.
2. Prefer evidence and pack sources over invention.
3. Fail closed on missing credentials, missing tools, or irreversible actions without HiTL.
4. Emit structured artifacts that validate against L1 schema before self-scoring.
5. Accept peer critique; refine at most 3 times; escalate blockers.

### Architecture pattern
Classifier + ReAct (match task embedding → agent capability)

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Agent-capability registry; benchmark history (cost/quality/latency)

## Developer

### Tools (allowlist intent)
Design tool surface: Agent registry DB; benchmark leaderboard cache; pricing APIs
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: OrchestratorAgent, CostOptimizerAgent
- May comment on: PlannerAgent (bad decomposition)
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Routing accuracy ≥95% vs oracle; cost within budget

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.router",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **RouterAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.router",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.router`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 21, 26, 30, 31, 37, 38, 59, 63, 87, 88, 89, 93, 94

### Design-time model landscape (non-activating)
- Seedance 2.0 (design-time only)
- Wan 2.6 (design-time only)
- Vidu Q2/Q3 (design-time only)
- Grok Imagine Video (design-time only)
- Hailuo 2.3 (design-time only)
- Kling 2.6/3.0 variants (design-time only)
- Seedance multi-camera (design-time only)
- Flux 1.1 Pro Ultra (design-time only)
- SD 3.5 self-hosted path (design-time only)

### Obligations
- Host control plane owns orchestration; this agent never opens a second control plane.
- Runtime tools remain agent_spec.allowed_tools only; RETHINK model names are design-time.
- Fail closed when tools/providers are unavailable (circuit-breaker posture).
- Prefer iterative verify → refine ≤ max_refinement_count → HiTL over silent pass.
- Emit plain-English reasoning summary in artifacts for operator trust.
- Attach provenance / correlation_id / evidence_refs on every handoff.
- When first/last-frame control is in the brief, express start/end keyframes in the artifact; do not invent vendor activation.
- Verify intermediate narrative/script artifacts before advancing downstream handoffs.
- Maintain a design-time model strengths matrix (quality, cost, latency, consistency); host routing remains authoritative.
- Escalate stereotype/harm/consent risks to ethics/trust-safety/legal gates.
- Track A/V sync and native-audio implications; do not assume silent video when audio is native.
- When ensemble is requested, propose multi-model candidates + selection criterion; host executes tools.

### Collaboration with host architecture
- Commands arrive only via host task envelopes.
- Publish results as structured artifacts; never open browser/UI channels.
- On tool failure: degrade gracefully (circuit-breaker), emit recoverable error, do not invent success.
<!-- RETHINK_100:end -->

## Rubrics

### `rubrics/primary.md`

Source rubric `video.rubric.router.v1.json` (baseline_safe; not a production pass).

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.router.v1",
  "agent_id": "video.router",
  "title": "L2 craft rubric for RouterAgent",
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
          "name": "Routing accuracy ≥95% vs oracle",
          "description": "Routing accuracy ≥95% vs oracle",
          "weight": 0.5,
          "threshold_hint": "≥95%",
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "cost within budget",
          "description": "cost within budget",
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
      "surpass_signal_design": "Beats human producer in agent/vendor selection",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Routing accuracy ≥95% vs oracle; cost within budget",
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

### `rubrics/video.rubric.router.v1.json`

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.router.v1",
  "agent_id": "video.router",
  "title": "L2 craft rubric for RouterAgent",
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
          "name": "Routing accuracy ≥95% vs oracle",
          "description": "Routing accuracy ≥95% vs oracle",
          "weight": 0.5,
          "threshold_hint": "≥95%",
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "cost within budget",
          "description": "cost within budget",
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
      "surpass_signal_design": "Beats human producer in agent/vendor selection",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Routing accuracy ≥95% vs oracle; cost within budget",
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

# Source acquisition runbook — `video.router`

## Purpose
Obtain or refresh knowledge distillation sources listed in `SOURCE_CATALOG.json`.

## Rules
1. **No secrets in git.** API keys only via environment / secret manager.
2. Prefer **licensed / consented / public domain** material.
3. If license unknown: store only short fair-use design excerpts under `excerpts/` and mark `license_class=unknown_review_required`.
4. Update `PROVENANCE.json` with URL, retrieved_at, hash, and license note.
5. Re-run offline golden eval after material changes.

## Design sources (from agents.md)
Agent-capability registry; benchmark history (cost/quality/latency)

## Steps
1. Open `SOURCE_CATALOG.json`.
2. For each source with status planned_or_partial, document acquisition method.
3. Place fixtures under `excerpts/` or `study/`.
4. Update `MAPPING.md` with path mapping.
5. Set `next_review_at` in `DISTILLATION_PLAN.json`.

## RETHINK_100_MODELS

Design-time model landscape from RETHINK_100 (do **not** download weights into the pack).

- Seedance 2.0 (design-time only)
- Wan 2.6 (design-time only)
- Vidu Q2/Q3 (design-time only)
- Grok Imagine Video (design-time only)
- Hailuo 2.3 (design-time only)
- Kling 2.6/3.0 variants (design-time only)
- Seedance multi-camera (design-time only)
- Flux 1.1 Pro Ultra (design-time only)
- SD 3.5 self-hosted path (design-time only)

Runtime remains host allow-list + production gates. See corpus `study/ui/RETHINK_100_IMPROVEMENTS.md`.

### `sources/DISTILLATION_PLAN.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.router",
  "plan_id": "video.router.distill.v1",
  "inputs": [
    "src_1",
    "src_2"
  ],
  "extractors": [
    "markdown_excerpt",
    "structured_table_row"
  ],
  "chunk_policy": {
    "max_chars": 2000,
    "overlap": 200
  },
  "owner": "video.router",
  "cadence": "quarterly",
  "promotion_criteria": [
    "source license approved or fixture-only",
    "excerpt hash recorded in PROVENANCE",
    "golden eval still passes L1"
  ],
  "memory_namespace": "pack.video.video.router",
  "next_review_at": "2026-10-01"
}
```

### `sources/excerpts/agent_loop_creator_v1.md`

# agent_loop_creator.md
**Version:** 2026-06-09 | **Status:** Production-Ready Spec for Implementation  
**Purpose:** Detailed, executable implementation guide for building the Refined Hierarchical ReAct Agent Loop (as specified in `agent_loop.md`). Optimized as input for a coding agent (Grok Build, Claude Code, Cursor + xAI/DeepSeek, N1ch01as Architect harness, or equivalent). Incorporates deep research from MASFT taxonomy (arXiv:2503.13657), AgentOrchestra/TEA Protocol (arXiv:2506.12508), ReAct enhancements (Reflexion, Prospector, ReflAct), xAI production patterns (grok-4.20-multi-agent server-side orchestration, Grok Build CLI sub-agents/plan-first), and 2025-2026 LLM agent surveys.  

**Rethink Summary (100x Internal Iteration):**  
- **Core Insight from Research**: ~42% of MAS failures are **specification & design issues** (MASFT); verification/termination another ~21%. Adding agents without strong Phase 0 spec validation, structured observations, explicit `Done` + multi-level critics, and progress tracking often yields diminishing/negative returns. Hierarchical + TEA-style versioning/self-evolution delivers outsized gains on long-horizon tasks (AgentOrchestra 89%+ GAIA).  
- **xAI Alignment**: Use `grok-4.20-multi-agent` (4/16 agents, leader synthesis, server-side ReAct with hidden sub-states) for research sub-tasks; emulate Grok Build patterns (explicit plan generation first, parallel isolated sub-agents, todo-style state) in client loop. Hybrid maximizes power + control + cost efficiency.  
- **Architectural Tradeoffs Resolved**: Custom Python core (Pydantic schemas, strict JSON mode, full tracer) over pure LangGraph for transparency, auditability, and education value (user's harness style). Hybrid memory (structured `todo.md` + vector long-term + aggressive summarization) per TEA/MemGPT. Bounded self-evolution (TextGrad-inspired + validation on held-out traces) to prevent drift. Minimal deps first; optional adapters later. Local-first, observable, sandboxed, production-hardened (circuit breakers, retries, budgets). Dogfood: This harness should help build/improve itself.  
- **Failure Mode Coverage**: Every MASFT mode explicitly mapped to mitigations in specific phases/components (see Section 3).  
- **Phased Build**: MVP (reliable flat ReAct) → Hierarchical delegation + consolidation → TEA versioning/evolution → xAI hybrid + examples. Each phase has clear deliverables, code skeletons, and verification gates (critic checkpoints).  
- **Target Outcomes**: >85% success on complex research/coding benchmarks via evolution; <5% residual MASFT failure modes in controlled tests; full replay/debug from traces; seamless integration with user's Python/Node/xAI/DeepSeek/Cursor/Kiro/OpenWebUI stack.  

This is **spec-driven, critic-ready input**. Coding agent: Parse sections, generate code module-by-module, run internal critic/refinement loops on outputs, validate against success criteria before proceeding. Use `task.md` / `todo.md` style internally during build.

---

## 1. Mission, Success Criteria & Constraints

### Primary Objective
Implement a **controlled, hierarchical, ReAct-inspired agent loop system** that is:
- Reliable against known MAS failure modes (MASFT taxonomy).
- Evolvable via TEA-inspired versioning, tracing, and self-reflection/TextGrad-style optimization.
- Hybrid: Client-side full control + optional delegation to xAI server-side multi-agent for deep research.
- Production-grade: Observable, cost-aware, secure (sandboxed), testable, extensible.
- Aligned with user's preferences: Spec-driven (living `TaskSpec`), iterative refinement/critic loops, harness engineering, local/minimal-Docker, Python-first with Pydantic/JSON contracts, integration points for existing tools (xAI API, DeepSeek, Cursor/Kiro, self-hosted services).

### Measurable Success Criteria (for Coding Agent Verification)
1. **Reliability**: In synthetic failure-injection tests (covering all 14 MASFT modes), mitigated failure rate <5% residual; explicit early detection for spec/role violations, cycle detection triggers replan/terminate, verifier rejects incomplete/incorrect `Finish`.
2. **Performance**: On held-out research/coding tasks (mini-GAIA style, web navigation + synthesis, multi-file code gen + test), base success ≥70%; with 2-3 self-evolution iterations on similar task distribution: ≥85% success, reduced steps/tokens vs baseline ReAct.
3. **Observability & Debuggability**: 100% of executions produce complete, replayable `Trace` (JSONL or structured) with provenance, versions, timings, token counts, thought/action/obs tuples. Support visualize (mermaid export or networkx graph) and replay from any step.
4. **Evolvability (TEA-aligned)**: VersionManager supports register/rollback/select-best for prompts, tool code, agent configs, sub-agent roles. SelfEvolver proposes + validates improvements (TextGrad-style) on held-out traces; demonstrable improvement after 3 bounded reflection rounds.
5. **Hybrid xAI Integration**: Seamless delegation of research sub-tasks to `grok-4.20-multi-agent` (narrow sub-spec + enabled tools); leader-synthesized result integrated into main trajectory with provenance. Optional plan-first + parallel sub-agents pattern emulating Grok Build.
6. **Production Hardening**: Circuit breakers (CLOSED/OPEN/HALF_OPEN with proper recovery), exponential backoff retries, per-phase token/step budgets + early exit, structured error observations, sandboxed tool execution (restricted Python or subprocess isolation), input sanitization, least-privilege.
7. **Usability for Coding Agent / User**: Clean Python package (`agent_loop/`) with CLI (`python -m agent_loop.cli`), optional FastAPI server mode, comprehensive examples (research agent, coding project harness, self-improving meta-agent), full type hints + docstrings, pytest suite passing, MkDocs or rich README.
8. **Integration**: Works with LiteLLM or direct clients (xAI, DeepSeek, OpenAI-compatible); optional LangGraph adapter; exports structured plans/todo for Grok Build / Cursor consumption; compatible with user's self-hosted OpenWebUI/Keycloak/Strapi patterns if extended to server mode.

### Constraints & Non-Goals
- **Language/Stack**: Python 3.11+ primary (Pydantic v2, asyncio, httpx, dataclasses). Optional: chromadb/FAISS for vector memory, fastapi/uvicorn for server, langgraph for adapter only. No heavy framework lock-in for core loop.
- **Minimalism First**: Core loop + state + reliability + basic hierarchical in <2k LOC initially. Add evolution/xAI hybrid in later phases.
- **No Uncontrolled Loops**: Hard `max_steps`, cycle detection (state hash), progress-based exit, circuit breakers. All LLM calls use strict output_schema (Pydantic/JSON mode or constrained decoding).
- **Security**: Sandbox code execution tools; never trust LLM-generated tool args blindly (validate + least-privilege); monitor for anomalous patterns (e.g., rapid repetition).
- **Cost Control**: Token budgets, parallel only for independent branches, summarization on context pressure, early termination when criteria met.
- **Non-Goals (Phase 1-2)**: Full distributed execution (Ray/Celery later), GUI dashboard (CLI + JSON export first), multimodal native (text+code focus; vision via xAI or sub-agent), production multi-tenancy.

**Living Spec**: This `agent_loop_creator.md` + `agent_loop.md` can be updated by the built system itself (self-evolution on the spec).

---

## 2. Deep Research Synthesis & Key Architectural Decisions

### 2.1 MASFT Taxonomy (arXiv:2503.13657) — Primary Failure Map
**"Why Do Multi-Agent LLM Systems Fail?"** (Cemri et al., 2025; MAST-Data: 1642 traces from 7 frameworks; 14 modes, κ=0.88 human IAA; LLM judge o1 few-shot κ=0.77).

**Category 1: System Design Issues (41.8% — Largest Lever)**
- FM-1.1 Disobey Task Specification (11.8%)
- FM-1.2 Disobey Role Specification (1.5%)
- FM-1.3 Step Repetition (15.7%)
- FM-1.4 Loss of Conversation History (2.8%)
- FM-1.5 Unaware of Termination Conditions (12.4%)

**

…(clipped 28267 characters from `agent_loop_creator_v1.md`)

### `sources/excerpts/agent_loop_creator_v2.md`

# agent_loop_creator_v2.md
**Version:** 2026-06-10 | **Status:** Production-Ready Spec for Implementation (v2 — Cognitive-Enhanced)  
**Purpose:** Detailed, executable implementation guide for building the **Cognitive-Enhanced Hierarchical ReAct Agent Loop v3** (as specified in `agent_loop_v3.md`). Builds directly on v1 while integrating the ranked human thinking models (Cynefin, Premortem, AAR, Double-Loop Learning, RPD + Dual Process, Metacognition, 5 Whys + Ishikawa, Red Team, Paul-Elder, etc.) from `thinking_model.md` as first-class, configurable mechanisms. Optimized as input for a coding agent (Grok Build, Claude Code, Cursor + xAI/DeepSeek, N1ch01as Architect harness, or equivalent). Incorporates deep research from MASFT taxonomy (arXiv:2503.13657), AgentOrchestra/TEA Protocol (arXiv:2506.12508), ReAct enhancements, xAI production patterns, and systematic cognitive framework analysis.  

**Key v2 Additions (from agent_loop_v3.md Section 1.4)**: Explicit Cynefin context classification for adaptive Fast vs Full loop routing; mandatory Premortem in Phase 0; RPD + Dual Process + Metacognition for Fast Recognition Path in Phase 1; structured AAR + Double-Loop + 5 Whys/Fishbone + multi-perspective critics (Paul-Elder/Red Team/Six Hats) in Phase 4 reflection/self-evolution. All original v1 details, skeletons, MASFT mappings, and phased roadmap preserved and extended.  

**Rethink Summary (100x Internal Iteration + Cognitive Layer):**  
- **Core Insight from Research**: ~42% of MAS failures are **specification & design issues** (MASFT); verification/termination another ~21%. Adding agents without strong Phase 0 spec validation, structured observations, explicit `Done` + multi-level critics, and progress tracking often yields diminishing/negative returns. Hierarchical + TEA-style versioning/self-evolution delivers outsized gains on long-horizon tasks (AgentOrchestra 89%+ GAIA). **v2 addition**: Human cognitive frameworks (top-ranked in thinking_model.md) provide the highest-leverage missing layer for adaptive intelligence, proactive risk handling, fast/slow deliberation, and multi-level learning — directly mapped in agent_loop_v3.md Section 1.4.  
- **xAI Alignment**: Use `grok-4.20-multi-agent` (4/16 agents, leader synthesis, server-side ReAct with hidden sub-states) for research sub-tasks; emulate Grok Build patterns (explicit plan generation first, parallel isolated sub-agents, todo-style state) in client loop. Hybrid maximizes power + control + cost efficiency. Cognitive routing (Cynefin) helps decide when to delegate vs local fast path.  
- **Architectural Tradeoffs Resolved**: Custom Python core (Pydantic schemas, strict JSON mode, full tracer) over pure LangGraph for transparency, auditability, and education value (user's harness style). Hybrid memory (structured `todo.md` + vector long-term + aggressive summarization + **Pattern Store for RPD**) per TEA/MemGPT. Bounded self-evolution (TextGrad-inspired + validation on held-out traces + **AAR/Double-Loop structure**) to prevent drift. **Cognitive config** (enable_fast_path, reflection_style, critic_modes) per TaskSpec for adaptability without complexity explosion on simple tasks. Minimal deps first; optional adapters later. Local-first, observable, sandboxed, production-hardened (circuit breakers, retries, budgets). Dogfood: This harness should help build/improve itself (including its own cognitive components).  
- **Failure Mode Coverage**: Every MASFT mode explicitly mapped to mitigations in specific phases/components (see Section 3) **+ cognitive mitigations** (e.g., Premortem for spec/design risks, Metacognition + cycle detection for repetition, AAR/Double-Loop for verification/termination gaps, RPD for context/history issues via pattern matching).  
- **Phased Build**: MVP (reliable flat ReAct) → Controlled core with cognitive mode selection (Fast Recognition Path) → Hierarchical delegation + consolidation → TEA versioning/evolution + full AAR/Double-Loop/5Whys critics → xAI hybrid + examples. Each phase has clear deliverables, code skeletons, and verification gates (critic checkpoints).  
- **Target Outcomes**: >85% success on complex research/coding benchmarks via evolution; <5% residual MASFT failure modes in controlled tests; **cognitive features validated** (Cynefin classification accuracy, Premortem risk coverage, RPD hit rate on repeated tasks, AAR structure compliance, Double-Loop assumption questioning); full replay/debug from traces; seamless integration with user's Python/Node/xAI/DeepSeek/Cursor/Kiro/OpenWebUI stack.  

This is **spec-driven, critic-ready input**. Coding agent: Parse sections, generate code module-by-module, run internal critic/refinement loops on outputs, validate against success criteria before proceeding. Use `task.md` / `todo.md` style internally during build.

---

## 1. Mission, Success Criteria & Constraints

### Primary Objective
Implement a **controlled, hierarchical, ReAct-inspired agent loop system (v3 Cognitive-Enhanced)** that is:
- Reliable against known MAS failure modes (MASFT taxonomy) **and enhanced with human cognitive best practices** (adaptive context routing via Cynefin, proactive risk via Premortem, fast expert intuition via RPD + Dual Process, structured multi-level reflection via AAR + Double-Loop + 5 Whys, multi-perspective critique via Paul-Elder/Red Team).
- Evolvable via TEA-inspired versioning, tracing, and self-reflection/TextGrad-style optimization **structured as AAR + Double-Loop**.
- Hybrid: Client-side full control + optional delegation to xAI server-side multi-agent for deep research **with cognitive mode selection** (Fast Recognition Path for routine sub-tasks vs Full deliberative for complex).
- Production-grade: Observable, cost-aware, secure (sandboxed), testable, extensible, **with configurable cognitive_profile** (enable_fast_path, reflection_style="aar_double_loop_5whys", critic_modes=["red_team", "paul_elder"]).
- Aligned with user's preferences: Spec-driven (living `TaskSpec` with cognitive_profile), iterative refinement/critic loops, harness engineering, local/minimal-Docker, Python-first with Pydantic/JSON contracts, integration points for existing tools (xAI API, DeepSeek, Cursor/Kiro, self-hosted services). **Dogfood cognitive improvements on its own prompts/verifier during Phase 4**.

### Measurable Success Criteria (for Coding Agent Verification)
1. **Reliability**: In synthetic failure-injection tests (covering all 14 MASFT modes), mitigated failure rate <5% residual; explicit early detection for spec/role violations, cycle detection triggers replan/terminate, verifier rejects incomplete/incorrect `Finish`.
2. **Performance**: On held-out research/coding tasks (mini-GAIA style, web navigation + synthesis, multi-file code gen + test), base success ≥70%; with 2-3 self-evolution iterations on similar task distribution: ≥85% success, reduced steps/tokens vs baseline ReAct.
3. **Observability & Debuggability**: 100% of executions produce complete, replayable `Trace` (JSONL or structured) with provenance, versions, timings, token counts, thought/action/obs tuples. Support visualize (mermaid export or networkx graph) and replay from any step.
4. **Evolvability (TEA-aligned)**: VersionManager supports register/rollback/select-best for prompts, tool code, agent configs, sub-agent roles. SelfEvolver proposes + validates improvements (TextGrad-style) on held-out traces; demonstrable improvement after 3 bounded reflection rounds.
5. **Hybrid xAI Integration**: Seamless delegation of research sub-tasks to `grok-4.20-multi-agent` (narrow sub-spec + enabled tools); leader-synthesized result integrated into main trajectory with provenance. Optional plan-first + parallel sub-agents pattern emulating Grok Build.
6. **Production Hardening**: Circuit breakers (CLOSED/OPEN/HALF_OPEN with proper recovery), exponential backoff retries, per-phase token/step budgets + early exit, structured error observations, sandboxed tool executi

…(clipped 38444 characters from `agent_loop_creator_v2.md`)

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

### `sources/excerpts/architecture_communication.md`

# UI ↔ Agent Communication Architecture

> How the frontend talks to the backend, and how the backend orchestrates the 114 agents.

---

## Overview: Three-Tier Architecture

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   TIER 1: UI FRONTEND (Browser)                                             │
│   React 19 + Next.js 15                                                     │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  User actions (click, type, approve, upload)                       │    │
│   │  Real-time state subscriptions (agent states, critiques, artifacts)│    │
│   └──────────┬─────────────────────────────────┬───────────────────────┘    │
│              │ REST / GraphQL                    │ WebSocket                  │
│              │ (commands)                        │ (live streams)             │
│              ▼                                   ▼                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   TIER 2: API GATEWAY + ORCHESTRATION BACKEND                               │
│   Node.js / Python (FastAPI) + LangGraph + Temporal                         │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  Production Manager Service (CRUD, auth, permissions)              │    │
│   │  Orchestration Engine (LangGraph DAG execution)                    │    │
│   │  Event Bus (Redis Streams / NATS)                                  │    │
│   │  Asset Store (S3 + metadata DB)                                    │    │
│   │  WebSocket Gateway (pushes live state to frontend)                 │    │
│   └──────────┬─────────────────────────────────┬───────────────────────┘    │
│              │ Agent Task Queue                  │ Tool API Calls             │
│              │ (dispatch tasks)                  │ (Sora, Veo, ElevenLabs...) │
│              ▼                                   ▼                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   TIER 3: AGENT RUNTIME (LLM Workers)                                       │
│   LangGraph Nodes / CrewAI Agents / AutoGen Actors                          │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │  114 Agent definitions (system prompts, tools, rubrics)            │    │
│   │  LLM providers (Gemini 2.5 Pro, GPT-4o, Claude 4)                 │    │
│   │  Generative tools (Sora 2, Veo 3.1, Runway, Kling, ElevenLabs)    │    │
│   │  Evaluation tools (VBench, CLIP-T, ArcFace, loudness meters)       │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Detailed Communication Flow

### 1. User Launches a Production (Brief → Agents)

```text
USER (Browser)
    │
    │  1. Fills Brief Studio form
    │  2. Clicks [▶ LAUNCH PRODUCTION]
    │
    ▼
FRONTEND (React)
    │
    │  POST /api/productions
    │  Body: { template: "E", title: "Luna", vision: "...",
    │          genre: "sci-fi", duration: 600, budget: 100, ... }
    │
    ▼
API GATEWAY (Backend)
    │
    │  3. Creates Production record in DB
    │  4. Enqueues "start_production" job
    │
    ▼
ORCHESTRATION ENGINE (LangGraph)
    │
    │  5. PlannerAgent receives brief
    │     - LLM call (Gemini 2.5 Pro): decompose brief → phased DAG
    │     - Returns: task list, agent assignments, gate criteria
    │
    │  6. OrchestratorAgent initializes DAG execution
    │     - Creates state machine in LangGraph
    │     - Registers all agent nodes
    │
    │  7. RouterAgent assigns model + provider per task
    │     - Checks cost/quality rules from config
    │
    ▼
AGENT WORKERS (Parallel)
    │
    │  8. DirectorAgent gets "generate shot intent" task
    │     - LLM call: Gemini 2.5 Pro (creative reasoning)
    │     - Tool call: Veo 3.1 API (video generation)
    │     - Self-Refine loop: score with CLIP-T, iterate if < threshold
    │
    │  9. Each completed step:
    │     - Agent → publishes event to Event Bus
    │     - Event Bus → WebSocket Gateway → Frontend (real-time update)
    │
    ▼
FRONTEND receives WebSocket events
    │
    │  10. DAG Canvas node transitions: ○ → ● → ✓
    │  11. Artifact appears in Gallery
    │  12. Critique message appears in Feed
    │  13. Status bar updates (agents running, budget spent)
```

---

### 2. Real-Time State Updates (Agents → UI)

```text
AGENT (e.g., DirectorAgent)
    │
    │  Emits events as it works:
    │  • { type: "agent_state_change", agent: 1, state: "running", task: "shot_5" }
    │  • { type: "tool_call_start", agent: 1, tool: "veo_3.1", params: {...} }
    │  • { type: "artifact_created", id: "art_042", type: "video", version: 1 }
    │  • { type: "critique_sent", from: 1, to: 9, content: "..." }
    │  • { type: "metric_update", agent: 1, metric: "clip_t", value: 0.34 }
    │
    ▼
EVENT BUS (Redis Streams / NATS)
    │
    │  Persists events for replay + forwards to subscribers
    │
    ▼
WEBSOCKET GATEWAY
    │
    │  Filters events by production_id
    │  Pushes to connected frontend clients
    │
    ▼
FRONTEND (React + Zustand)
    │
    │  Updates local state store
    │  React components re-render:
    │  • DAG node color changes (blue pulse)
    │  • New artifact card appears
    │  • Critique feed message slides in
    │  • Status bar counters update
    │  • Budget gauge animates
```

---

### 3. Human-in-the-Loop (UI → Agent)

```text
USER sees Gate Approval Dialog
    │
    │  Reviews criteria checklist + artifacts
    │  Clicks [✓ APPROVE] or [↩ REQUEST CHANGES]
    │
    ▼
FRONTEND
    │
    │  POST /api/productions/{id}/gates/{gate_id}/decision
    │  Body: { decision: "approve", comment: "...", c2pa_sign: true }
    │
    ▼
API GATEWAY
    │
    │  Validates user permission
    │  Signs C2PA provenance manifest
    │  Publishes "gate_decision" event to Event Bus
    │
    ▼
ORCHESTRATION ENGINE (LangGraph)
    │
    │  GateKeeperAgent receives decision
    │  If approved: advances DAG to next phase
    │  If rejected: routes feedback to relevant agents for revision
    │
    ▼
NEXT PHASE AGENTS activate
    │
    │  (cycle continues)
```

---

### 4. User Sends Critique to Agent

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

---

## API Contract Summary

### REST Endpoints (Commands — things the user initiates)

| Method | Endpoint | Purpose | Called By |
|--------|----------|---------|-----------|
| POST | `/api/productions` | Create + launch production from brief | Brief Studio |
| GET | `/api/productions` | List all productions | Dashboard |
| GET | `/api/productions/{id}` | Get production state | Production Console |
| POST | `/api/productions/{id}/gates/{gid}/decision

…(clipped 13466 characters from `architecture_communication.md`)

### `sources/excerpts/backend_agent_management.md`

# Backend → Agent Management: How the Backend Controls 114 Agents

> Deep dive into the internal mechanics of how the orchestration backend manages, dispatches, monitors, retries, and communicates with the AI agent workers.

---

## The Core Question

```text
Q: The backend has 114 agent "definitions" — but HOW does it actually
   create, run, communicate with, and control them?

A: Each agent is NOT a separate server or microservice.
   An agent is a CONFIGURATION (system prompt + tools + rubric)
   that gets EXECUTED by a worker process when given a task.

   Think of it like this:
   - The backend is the CONDUCTOR of an orchestra
   - Agents are SHEET MUSIC (instructions)
   - Workers are MUSICIANS (execution)
   - The LLM is the INSTRUMENT (capability)
```

---

## 1. What IS an Agent at Runtime?

An agent is **not** a long-running process. It's a **stateless function** that gets invoked with:

```python
# Pseudocode — what an "agent" actually is in LangGraph

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

When the backend needs DirectorAgent to generate shot intent #5, it:

1. Loads this definition
2. Constructs the LLM prompt (system prompt + task context + critique history)
3. Calls the LLM
4. The LLM decides which tools to call
5. Backend executes tool calls on behalf of the agent
6. Loops if self-refine pattern requires it
7. Publishes result + events

---

## 2. The Orchestration Engine (The Brain)

```text
┌─────────────────────────────────────────────────────────────────────┐
│                    ORCHESTRATION ENGINE                               │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                    DAG STATE MACHINE                          │    │
│  │                    (LangGraph Graph)                          │    │
│  │                                                             │    │
│  │  Nodes:    [Brief] → [Plan] → [Route] → [Craft×N] → [Gate]│    │
│  │  Edges:    Conditional (if gate passes → next phase)        │    │
│  │  State:    { phase, active_agents, pending_tasks, budget }  │    │
│  │  Checkpoint: Persisted after every node execution           │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ┌───────────────────┐  ┌───────────────────┐                      │
│  │   TASK DISPATCHER  │  │   TASK QUEUE      │                      │
│  │                   │  │                   │                      │
│  │ Decides:          │  │ Per-agent queues: │                      │
│  │ • WHICH agent     │  │ • agent_1: [t5]  │                      │
│  │ • WHAT task       │  │ • agent_6: [t3]  │                      │
│  │ • WHICH model     │  │ • agent_9: []    │                      │
│  │ • WHEN to run     │  │ • agent_46: [t7] │                      │
│  │ • Priority order  │  │ • ...            │                      │
│  └───────────────────┘  └───────────────────┘                      │
│                                                                     │
│  ┌───────────────────┐  ┌───────────────────┐                      │
│  │   CRITIQUE ROUTER  │  │   GATE EVALUATOR  │                      │
│  │                   │  │                   │                      │
│  │ Routes critique   │  │ Checks criteria   │                      │
│  │ messages between  │  │ Triggers approval │                      │
│  │ agents based on   │  │ Advances phase    │                      │
│  │ "accepts_from"    │  │ when human says OK│                      │
│  │ relationships     │  │                   │                      │
│  └───────────────────┘  └───────────────────┘                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. How the Backend DISPATCHES a Task to an Agent

Step-by-step, here's what happens when the OrchestratorAgent decides "DirectorAgent should work on Shot #5":

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


Step 2: QUEUE + WORKER PICKUP
─────────────────────────────
Task goes into agent_1's queue.
A free worker process picks it up.

The worker pool is like a thread pool:
  - 10-50 concurrent workers (configurable)
  - Each worker can execute ANY agent's task
  - Workers are stateless — they load agent config per task


Step 3: AGENT EXECUTION (inside the worker)
───────────────────────────────────────────

Worker does this:

  a) Load AgentDefinition for agent_id=1 (DirectorAgent)
  b) Fetch input artifacts from Asset Store
  c) Fetch relevant memories from MemoryAgent (vector search)
  d) Construct LLM messages:

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
         
         Output: JSON shot intent with camera, subject, style, duration.
       """ }
     ]

  e) Call LLM (Gemini 2.5 Pro):
     response = await llm.chat(messages, tools=[veo_api, memory_store])

  f) LLM responds with tool calls:
     → tool_call: veo_api.generate(prompt="slow dolly push...", seed=4412)
     → Worker EXECUTES this tool call (HTTP to Veo 3.1 API)
     → Gets back: video URL + metadata

  g) LLM evaluates result (self-refine):
     → tool_call: clip_scorer.evaluate(video_url, text_prompt)
     → Score: 0.34 (threshold: 0.32) ✓ PASS

  h) If score < threshold: loop back to step (e) with feedback
     If score >= threshold: task complete


Step 4: RESULT PUBLICATION
──────────────────────────
Worker publishes to Event Bus:
  • { type: "artifact_created", artifact_id: "art_043", ... }
  • { type: "agent_state_change", agent: 1, state: "complete" }
  • { type: "metric_update", agent: 1, metric: "clip_t", value: 0.34 }

Orchestrator receives "task_042 complete" → decides next task.
```

---

## 4. How the Backend MANAGES Agent Lifecycle

```text
┌─────────────────────────────────────────────────────────────────┐
│                   AGENT LIFECYCLE                                 │
│                                                                 │
│   IDLE ──────► QUEUED ──────► RUNNING ──────► COMPLETE          │
│    │              │              │                │              │
│    │              │              │                ▼              │
│    │              │              │           (publish result)    │
│    │              │              │                               │
│

…(clipped 14887 characters from `backend_agent_management.md`)

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

### `sources/excerpts/project_starter_0.2.md`

# Project Starter — Improved Living Task Spec  
  
**Project name:** `project_starter`    
**Package/repo name:** `project_starter`    
**Version:** `0.2.0-rethink`    
**Status:** Ready for Phase 0 execution    
**Created:** 2026-06-07    
**Primary objective:** Build a production-ready starter repo that installs, synchronizes, audits, and evolves a cross-agent coding harness for Claude Code, Cursor, Codex, OpenCode, Gemini CLI, Grok Build, and similar tools.  
  
---  
  
## 0. Key Rethink Summary  
  
The original plan is strong but broad, partially duplicative, and slightly risky because it assumes “full installs” and “exact parity” across tools whose config systems differ. This improved spec makes the project more executable by:  
  
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
  
---  
  
## 1. Source Verification Snapshot  
  
Phase 0 must re-check all sources before implementation. Current intended source priorities:  
  
1. **ECC** — primary cross-agent harness foundation.  
2. **Karpathy-style behavioral rules** — concise behavioral layer.  
3. **claude-mem or equivalent** — persistent memory if compatible and safe.  
4. **Claude Code best-practice repositories** — selected planning/workflow patterns.  
5. **Curated skill libraries** — selective import only; no bulk install by default.  
6. **Official agent docs** — Claude Code, Cursor, Codex, OpenCode, Gemini CLI, Grok Build, GitHub Copilot.  
  
Phase 0 must verify:  
  
- Latest version, commit, tag, or release.  
- License.  
- Installation method.  
- Supported config paths.  
- Security implications.  
- What is included, adapted, or rejected.  
  
---  
  
## 2. Non-Negotiable Principles  
  
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
  
---  
  
## 3. Target Deliverables  
  
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
  
---  
  
## 4. Proposed Repository Structure  
  
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
  
---  
  
## 5. Generated File Policy  
  
Every generated/adapted file must include a header:  
  
```text  
<!-- AUTO-GENERATED by project_starter. Do not edit directly.  
Source: skills/, rules/, hooks/, mcp-configs/  
Run: npm run sync  
-->  
```  
  
Rules:  
  
- [ ] Central files are authoritative.  
- [ ] Generated files are overwritten only after conflict checks.  
- [ ] Local user files are backed up before overwrite.  
- [ ] `--dry-run` must show exact writes/deletes.  
- [ ] `--check` must fail if generated files are stale.  
- [ ] Symlinks are preferred only where safe and supported.  
- [ ] Windows fallback is copy mode unless Developer Mode/admin symlink support is detected.  
  
---  
  
## 6. Phase 0 — Research, Scope Lock, and Source Audit  
  
**Goal:** Confirm latest sources, install commands, licenses, and compatibility before generating files.  
  
### Tasks  
  
- [ ] Verify latest ECC release, installer commands, profiles, and license.  
- [ ] Verify Karpathy-style rules source and Cursor rule variant.  
- [ ] Verify `claude-mem` or equivalent persistent-memory candidate.  
- [ ] Verify best-practice workflow repositories and select only non-duplicative patterns.  
- [ ] Verify curated skill libraries and choose only high-value bundles.  
- [ ] Verify official docs for Claude Code, Cursor, Codex, OpenCode, Gemini CLI, Grok Build, and GitHub Copilot.  
- [ ]

…(clipped 15363 characters from `project_starter_0.2.md`)

### `sources/excerpts/project_starter_0.5.md`

# project_starter

**Project name:** `project_starter`  
**Purpose:** Build an executable starter repository that downloads, audits, curates, and synchronizes AI coding-agent configuration sources across Claude Code, Cursor, Codex, Gemini CLI, OpenCode, Grok Build, GitHub Copilot, and related agent harnesses.  
**Current spec version:** `1.1.0-merged-bootstrap`  
**Last updated:** 2026-06-09  

---

## How to Use This Boilerplate With a Coding Agent

This repository is a boilerplate specification.

A human may ask a coding agent to create a new project from this file by using a prompt like:

```text
Create a new project named <PROJECT_NAME> based on <PATH_TO_PROJECT_STARTER_MD>.

Use project_starter.md as the source-of-truth implementation contract.

Create the new project at:

<OUTPUT_PATH>

The project purpose is:

<PROJECT_PURPOSE>

The primary stack is:

<STACK>

You must:
1. Read project_starter.md fully.
2. Create the new project directory.
3. Create all directories and files required by project_starter.md.
4. Replace boilerplate metadata with the new project name and purpose.
5. Copy project_starter.md into the new project.
6. Create package.json.
7. Create source manifests.
8. Create executable scripts.
9. Create rule files.
10. Create docs.
11. Download all enabled upstream GitHub repositories into external/sources/.
12. Generate sources/source-lock.json.
13. Generate docs/source-audit.md.
14. Run bootstrap validation.
15. Update status.md.
16. Report final pass/fail status.

Do not merely summarize the instructions.
Do not only write Markdown.
Create a working executable project.

If network or shell access is unavailable, create all project files anyway and mark source download as blocked in status.md.

## Project Modes

This specification supports two valid implementation modes:

1. **Self-bootstrap mode** — implement the starter repository itself in the current repository.
2. **Create-new-project mode** — generate a new downstream project from this specification into a target directory.

Example self-bootstrap prompt:

```text
Implement project_starter.md in the current repository.

Use project_starter.md as the complete implementation contract.

Create all required files, directories, manifests, scripts, docs, tests, and agent configuration files.

Then run:

npm run bootstrap
```

Example create-new-project prompt:

```text
Create a new project named <PROJECT_NAME> based on <PATH_TO_PROJECT_STARTER_MD>.

Create it at:

<OUTPUT_PATH>

Use project_starter.md as the complete implementation contract.

Create a working executable project, not just Markdown.

Download all enabled sources unless told not to.

Then run:

npm run bootstrap
```

## Required Input Variables

When generating a downstream project, a coding agent may receive these variables:

| Variable | Description | Default |
|---|---|---|
| `PROJECT_NAME` | Name of the generated project | `project_starter_generated` |
| `OUTPUT_PATH` | Target directory for the generated project | `./project_starter_generated` |
| `PROJECT_PURPOSE` | Short description of the generated project | `AI coding-agent starter repository` |
| `STACK` | Primary technology stack | `Node.js 20+, plain JavaScript, no runtime dependencies for bootstrap scripts` |
| `DOWNLOAD_SOURCES` | Whether enabled upstream sources should be downloaded | `true` |
| `AGENT_SUPPORT` | Supported coding agents | `claude,cursor,codex,gemini,opencode,copilot,grok-build` |
| `PACKAGE_MANAGER` | Primary JavaScript package manager | `npm` |
| `LICENSE` | License for the generated project | `MIT` |

If a required value is missing, the coding agent should use the default.

## Existing Output Directory Rule

If `OUTPUT_PATH` already exists and is non-empty, the coding agent must stop and ask for permission before overwriting or updating it.

Allowed exception:

- If the user explicitly says to overwrite or update the existing directory, the agent may proceed, but should preserve important user-created files when possible.

## 0. Critical Instruction to Coding Agents

This file is **not only documentation**.

When a coding agent receives this file and is asked to implement it, the agent **MUST** create a real executable project.

The agent **MUST NOT** stop after writing Markdown.

The agent **MUST**:

1. Create the `project_starter/` repository structure.
2. Create `package.json`.
3. Create `sources/manifest.json`.
4. Create `sources/docs-manifest.json`.
5. Create `scripts/project-starter.mjs`.
6. Create `scripts/create-project.mjs`.
7. Create `scripts/source-download.mjs`.
8. Create `scripts/source-audit.mjs`.
9. Create `scripts/doctor.mjs`.
10. Create `scripts/sync.mjs`.
11. Create `scripts/security.mjs`.
12. Download every enabled GitHub repository listed in `sources/manifest.json`.
13. Save downloaded repos under `external/sources/`.
14. Save download metadata to `sources/source-lock.json`.
15. Generate `docs/source-audit.md`.
16. Support both self-bootstrap and create-new-project workflows.
17. Run the bootstrap validation commands.
18. Report success or exact blockers.

If network access or shell execution is unavailable, the agent **MUST** say:

```text
BLOCKED: cannot download sources because network/shell execution is unavailable.
```

and still create all scripts and manifests so the human can run:

```bash
npm run bootstrap
```

later.

---

## 1. Non-Negotiable Outcome

After implementation, this command:

```bash
npm run bootstrap
```

**MUST** perform this flow:

```text
doctor
→ create required directories
→ validate sources/manifest.json
→ clone/update all enabled GitHub sources
→ write sources/source-lock.json
→ generate docs/source-audit.md
→ run security smoke checks
→ run sync dry-run
→ run tests
```

The project is **not complete** unless the source repositories are actually downloaded into:

```text
external/sources/
```

---

## 2. Required Repository Structure

The coding agent **MUST** create this structure:

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

---

## 3.

…(clipped 35039 characters from `project_starter_0.5.md`)

### `sources/excerpts/RETHINK_100_IMPROVEMENTS.md`

# 100-Point Deep Rethink — Research-Backed Improvements

> Based on arXiv papers (FilmAgent, MovieAgent, OmniAgent, AnimAgents, Sima 1.0), 2026 model landscape (Seedance 2.0, Wan 2.6, Vidu Q2/Q3, Grok Imagine Video, Hailuo 2.3), LangGraph 1.0 production patterns, and Generative UI trends. May 2026.

---

## Research Sources

| Source | Key Insight | Link |
|--------|------------|------|
| FilmAgent (2025) | Multi-agent film automation with iterative feedback loops that verify scripts and reduce hallucinations | [arXiv:2501.12909](https://arxiv.org/abs/2501.12909) |
| MovieAgent (2025) | Hierarchical CoT planning with character bank achieves SOTA script faithfulness and character consistency | [arXiv:2503.07314](https://arxiv.org/abs/2503.07314) |
| OmniAgent | Hierarchical graph-based multi-agent for long video with film-production-inspired architecture | [arXiv:2510.22431](https://arxiv.org/html/2510.22431v1) |
| AnimAgents (2025) | Human-multi-agent collaboration with dedicated boards per pre-production stage | [arXiv:2511.17906](https://arxiv.org/abs/2511.17906) |
| Sima 1.0 (2025) | 11-step pipeline distributed across hybrid workforce for documentary video production | [arXiv:2604.07721](https://arxiv.org/html/2604.07721) |
| Seedance 2.0 (Apr 2026) | 9 images + 3 videos + 3 audio simultaneous input; native audio-visual synchronization | [ByteDance](https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0) |
| Wan 2.6 (2026) | IP-anchored character consistency; multi-shot storytelling coherence | [Comparison](https://wanvideogenerator.com/blog/seedance-2-vs-wan-2-6) |
| Veo 3.1 (2026) | 4K + reference images for character/object direction; configurable aspect ratios | [Google AI](https://ai.google.dev/gemini-api/docs/video) |
| Kling 2.6/3.0 | Physics-accurate motion; motion-control via reference video | [fal.ai](https://fal.ai/models/fal-ai/kling-video) |
| Grok Imagine Video (xAI) | New entrant with strong image-to-video capability | [wavespeed.ai](https://wavespeed.ai/blog/posts/grok-imagine-video-vs-sora-2-veo-3-seedance-wan-vidu-comparison-2026/) |
| LangGraph 1.0 Production | Node caching, deferred nodes, pre/post hooks, consensus mechanisms | [LangChain](https://www.langchain.com/blog/building-langgraph) |
| Agent Architecture 2026 | Isolate orchestration from execution; event-driven avoids cascading failures | [markaicode](https://markaicode.com/architecture/agent-architecture-best-practices-2026/) |
| Supervisor vs Swarm | Supervisor more accurate (routing is its only job); Swarm faster (skips intermediary) | [focused.io](https://focused.io/lab/multi-agent-orchestration-in-langgraph-supervisor-vs-swarm-tradeoffs-and-architecture) |
| Generative UI 2026 | AI agents create rich interactive interfaces dynamically | [Medium](https://medium.com/@akshaychame2/the-complete-guide-to-generative-ui-frameworks-in-2026-fde71c4fa8cc) |
| 6-Model Comparison 2026 | Pick by goal: conversions, realism, camera control, storytelling, IP, or cost | [opencreator.io](https://opencreator.io/blog/ai-video-models-comparison-2026) |

---

## Top 20 Critical Improvements (P0 + P1)

### Models to Add (agents.md Tool Access update needed)

1. **Seedance 2.0** — 9 images + 3 videos + 3 audio clips simultaneous input; first-and-last-frame control; native multi-camera storytelling
2. **Wan 2.6** — IP-anchored character consistency; strongest for multi-shot narrative coherence
3. **Vidu Q2/Q3** — Temporal consistency specialist; competitive I2V
4. **Grok Imagine Video** (xAI) — New entrant; strong image-to-video
5. **Hailuo 2.3** (MiniMax) — Fast budget-tier generation

### Architecture (backend docs update needed)

6. **Supervisor + Swarm hybrid** — Use Supervisor pattern for creative decisions (accuracy matters), Swarm for parallel QA (speed matters)
7. **Node caching** (LangGraph 1.0) — Cache identical agent outputs; 30-50% cost reduction
8. **Circuit breaker per API** — Graceful degradation when Veo/Sora/Kling APIs fail
9. **Isolate orchestration from execution** — Separate processes prevent cascading failures
10. **Model deprecation handling** — Sora 2 discontinuing Sept 2026; need graceful migration

### Workflow (from FilmAgent/MovieAgent research)

11. **Character Bank** — Persistent character definitions (face ref, voice, wardrobe) shared across all shots
12. **Iterative script verification** — Agents verify intermediate scripts before proceeding (reduces hallucination)
13. **Hierarchical CoT planning** — Better task decomposition for complex stories
14. **Shot-adjacency awareness** — Each agent considers previous AND next shot when generating
15. **Reference frame bank** — Approved frames from early shots guide later generation (consistency)
16. **First-and-last-frame generation** — Seedance 2.0 feature; precise scene control
17. **Multi-model ensemble** — Generate same shot on 2 models, CLIP-pick best

### UI/UX (from Generative UI research)

18. **Progressive results** — Show partial outputs as agents work (shot 1 appears before shot 5 done)
19. **Regenerate specific segment** — Keep shots 1-4, regenerate only shot 5
20. **AI co-pilot chat** — Natural language interface to trigger any action: "extend shot 3 by 2 seconds"

---

## Full 100 Improvements (by category)

### A. Model Landscape (1-15)
### B. Architecture (16-30)
### C. Research-Backed Workflows (31-50)
### D. UI/UX (51-70)
### E. New Capabilities (71-85)
### F. Quality & Evaluation (86-95)
### G. Business & Scaling (96-100)

(See detailed breakdown below)

---

## A. Model Landscape Updates (1-15)

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

## B. Architecture Improvements (16-30)

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
| 29 | Shadow mode for

…(clipped 6156 characters from `RETHINK_100_IMPROVEMENTS.md`)

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

### `sources/generic/video.gatekeeper.SPEC.md`

# GateKeeperAgent

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 57 |
| **pack_id** | `video.gatekeeper` |
| **category** | `9-Meta` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.gatekeeper/` |

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

Phase transitions; verifies L1/L2/L3 criteria; signs C2PA

## Knowledge distillation sources

Stage-gate methodology; PGA Producers Mark; QMS audit

## Self-quality criteria

Zero leaked defects; sign-off SLA ≥99%

## Surpass-human signal

Lower escaped-defect rate than human QA lead

## Critique bus

- **Accepts critique from:** ComplianceAgent, AIQAConsistencyAgent

- **Comments on:** OrchestratorAgent (premature advance)

## Tools (design-time documentation)

C2PA signing (c2patool); JSON schema validators; rubric evaluation endpoints

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

Constitutional AI (constitution = phase-gate criteria)

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


### Document: `study/intent_analysis_agent_functional_specification.md`

_Embedded from `corpus/study/intent_analysis_agent_functional_specification.md`. Also stored at `sources/study/intent_analysis_agent_functional_specification.md` under this agent folder._


**Deep Intent Analysis Framework (DIA) v2.0**  
**Comprehensive Functional Specification Document**

**Version:** 2.0 (Research-Enhanced)  
**Date:** May 26, 2026  
**Status:** Complete Functional Specification  
**Basis:** Original 6-phase DIA (from conversation history) + deep integration of 2025–2026 arXiv research on computational pragmatics, speech act theory, LLM-based intent/implicature reasoning, multi-party discourse analysis, and xAI Grok capabilities.

---

### 1. Executive Summary

The **Deep Intent Analysis Framework (DIA) v2.0** is a complete, production-ready, modular system for systematically decoding any text’s **purpose**, **hidden agenda**, **multi-angle perspectives**, **illocutionary force**, and **ethical/behavioral quality**.  

It transforms the original 6-phase manual/LLM-prompt pipeline into a **fully specified, agentic, evaluable software system** built on xAI’s Grok-4.3 (or latest) with native tool use, 1M+ token context, structured outputs, and low-hallucination reasoning.

**Core Objectives**  
- Answer: *Why does this language exist? What is the real goal? What is hidden? How many angles exist? Is the behavior good/wrong/effective?*  
- Achieve human-expert-level pragmatic reasoning at scale.  
- Support manual use, API, web app, IDE plugin, and enterprise analytics.

**Key v2.0 Improvements (from arXiv + xAI research)**  
- **Pragmatic Inference Chain (PIC)** integration for superior implicature & hidden-agenda detection.  
- **Multi-Perspective Agent Simulation** (inspired by multi-party conversational agents survey) for richer angle mapping.  
- **Gricean + Extended Maxims** (including Benevolence & Transparency for AI contexts).  
- **Automated Speech Act / Dialog Act Classification** using recent taxonomies and LLM judges.  
- **Hybrid Evaluation Pipeline** (automatic metrics + human-in-the-loop).  
- **Native xAI Integration**: Grok-4.3 reasoning modes, tool calling, real-time search for context validation.

**Target Users**  
Journalists, analysts, researchers, educators, content moderators, legal teams, AI safety engineers, and power users who want to “see through” language.

---

### 2. Background, Motivation & Research Foundation

**Original Motivation (from user history)**  
Language serves communication, but always with purpose, hidden intent, multiple angles, and moral implications. The 6-phase DIA provides a repeatable algorithm.

**2025–2026 Research Integration** (selected key sources)

- **Pragmatics in the Era of LLMs Survey** (arXiv:2502.12378): Comprehensive datasets for speech acts, implicature, social pragmatics; highlights LLM gaps in deeper pragmatic reasoning and English-centric bias. Recommends hybrid evaluation and theory-grounded prompting.

- **Pragmatic Inference Chain (PIC)** (arXiv:2503.01539): 4-step relevance-theory-based prompting dramatically improves implicit toxicity / hidden bias detection (GPT-4o: +12.26 pp). Explicitly separates literal meaning, metaphors, norm violation, and judgment. Directly enhances Phase 3 & 4.

- **Multi-Party Conversational Agents Survey** (arXiv:2505.18845): State-of-Mind taxonomy (Emotion, Engagement, Personality Big-Five, Dialog Acts); discourse structure; Theory of Mind (ToM) for multi-perspective modeling. Enables true multi-angle simulation.

- **Gricean Maxims in NLP & Human-AI Interaction**: Multiple papers extend Grice with Benevolence & Transparency maxims for AI; use maxim-violation detection for offensive/hidden-agenda texts.

- **xAI / Grok Research**: Grok-4.3 excels at agentic tool use, long-context reasoning, low hallucination, and social role mediation (truth arbiter, adversary). Ideal backbone for DIA as a trustworthy, multi-role analysis agent.

These findings directly upgrade the original framework into a **scientifically grounded, computationally implementable specification**.

---

### 3. System Architecture (High-Level)

**Modular, Agentic Design** (Grok-4.3 native)

```
User Input (Text + Optional Context)
          ↓
Phase 0: Context Analyzer Agent
          ↓
Phase 1: Purpose Classifier (Jakobson + LLM)
          ↓
Phase 2: Surface Literal Parser (NLP + LLM)
          ↓
Phase 3: Pragmatic Engine (Speech Acts + PIC + Grice Maxim Detector)
          ↓
Phase 4: Hidden Agenda & Multi-Angle Dissector (Multi-Agent ToM Simulation)
          ↓
Phase 5: Judgment Engine (Multi-Criteria Scorer + Ethical Auditor)
          ↓
Phase 6: Synthesizer & Action Recommender
          ↓
Structured JSON Output + Human-Readable Report + Visualizations
```

**Core Components**  
- **LLM Backbone**: Grok-4.3 (reasoning mode configurable: low/medium/high) via xAI API.  
- **Tool Layer**: Real-time search (for context validation), code interpreter (metrics, clustering), structured output enforcement.  
- **Optional Classical NLP Layer**: spaCy/transformers for baseline speech act classifiers, embeddings (angle similarity), topic modeling.  
- **Orchestration**: LangGraph-style or custom xAI agent framework with parallel tool calls.  
- **Storage**: Analysis history, user templates, benchmark results (PostgreSQL + vector DB for similarity search).  
- **Interfaces**: REST API, Web UI (Streamlit/Gradio), CLI, VS Code / Cursor extension, Slack/Discord bot.

**Data Flow**  
Every phase produces typed artifacts (JSON) that feed the next. Full traceability with evidence spans and confidence scores.

---

### 4. Detailed Functional Requirements – 6 Phases (v2.0 Enhanced)

#### Phase 0: Context Analyzer
**Inputs**: Raw text, optional metadata (sender, platform, date, prior messages).  
**Processing**: LLM extracts sender power/relationship, audience, medium norms, trigger event; bias self-check prompt.  
**Enhancement**: Real-time search tool for historical/cultural context.  
**Output**: Structured context object + confidence.

#### Phase 1: Purpose Categorization (Jakobson Functions)
**Table** (unchanged but now LLM-ranked with evidence): Referential, Emotive, Conative, Phatic, Metalingual, Poetic.  
**v2.0**: Multi-label classification with probability distribution + justification.

#### Phase 2: Surface Literal Analysis
**Checklist** (facts vs opinions, loaded words, voice, omissions, ambiguity).  
**Enhancement**: Embedding-based vagueness scoring + coreference resolution.

#### Phase 3: Pragmatic & Speech Act Engine (Core Upgrade)
**Components**:
- **Searle’s 5 Categories** (Assertives, Directives, Commissives, Expressives, Declaratives) + fine-grained taxonomies from Parliamentary Debates & CyberAgressionAdo-v2 (“attack”, “defend”, etc.).
- **Grice Maxim Violation Detector**: Automated scoring (Quantity, Quality, Relation, Manner) + extended maxims (Benevolence, Transparency).
- **PIC Integration** (mandatory for hidden agenda):
  1. Explain metaphors/special meanings (layperson language).
  2. Literal meaning (layperson language).
  3. Identify contradictions with relevant social/ethical norms (equality, truth-seeking, non-manipulation, etc.).
  4. Final implicature judgment.

**Output per utterance**: `{illocutionary_act, perlocutionary_effect, maxim_violations: [...], implicature: "...", confidence}`

#### Phase 4: Hidden Agenda & Multi-Angle Dissection (Major Upgrade)
**Steps**:
1. Explicit vs Implicit goals (power, status, division, validation…).
2. Power & ideology scan (CDA-style: who benefits? us vs them?).
3. **Multi-Perspective Agent Simulation** (new): Spawn 4–6 parallel Grok agents, each embodying one POV (speaker, receiver, opponent, society, historical, environmental). Each produces angle summary + evidence. Aggregate with clustering.
4. Framing analysis + inconsistency detection.
5. Agenda Type classification (Inform / Persuade / Manipulate / Bond / Signal / Deceive) with sub-scores.

**Output**: `hidden_agenda: str, angle_count: int, angles: [{perspective, framing, evidence}], ignored_angles: [...]`

#### Phase 5: Behavioral Judgment Engine
**6 Core Dimensions** (1–10 or 0–1) + 2 new:
1. Truthfulness
2. Ethical Impact (harm, autonomy, power imbalance)
3. Effectiveness (stated + hidden goals)
4. Clarity & Cooperation (Grice)
5. Social Value (understanding vs division)
6. Transparency
7. **Benevolence** (new – AI-specific)
8. **Cultural Appropriateness** (new – from multi-task pragmatic models)

**Final Verdict**: Categorical + narrative + recommended action.  
**Rule**: All scores must cite evidence from Phases 0–4.

#### Phase 6: Synthesis
One-paragraph executive summary + actionable recommendations + confidence vector.  
Optional: Counter-argument generator or “how to respond” module.

---

### 5. Data Models & Output Schema (JSON)

```json
{
  "analysis_id": "uuid",
  "input_text": "...",
  "context": {...},
  "purpose": {
    "dominant_functions": [{"function": "Conative", "score": 0.62, "evidence": "..."}],
    "jakobson_ranking": [...]
  },
  "surface": {...},
  "pragmatic": {
    "speech_acts": [...],
    "grice_violations": [...],
    "pic_implicature": "..."
  },
  "hidden_agenda": {
    "primary_agenda": "Manipulate via fear",
    "angle_count": 5,
    "angles": [...],
    "multi_perspective_summary": {...}
  },
  "judgment": {
    "scores": {
      "truthfulness": 7.2,
      "ethics": 3.1,
      "benevolence": 4.5,
      ...
    },
    "verdict": "Strategically effective but ethically manipulative",
    "recommended_action": "..."
  },
  "confidence": 0.87,
  "processing_time_ms": 12400,
  "model": "grok-4.3-reasoning-high"
}
```

---

### 6. Non-Functional Requirements

- **Performance**: <15s for <5k token text on Grok-4.3 high reasoning; parallel phase execution.  
- **Scalability**: Stateless API; batch mode for enterprise (1000s of texts).  
- **Accuracy**: Target >85% agreement with expert linguists on speech act + implicature benchmarks (use Parliamentary Debates, PIC test sets, etc.).  
- **Explainability**: Every claim has evidence span + confidence.  
- **Ethics & Safety**: Built-in refusal for harmful misuse; bias auditing; xAI alignment principles (truth-seeking, helpfulness without sycophancy).  
- **Privacy**: Optional local mode; no persistent storage of user texts unless opted in.

---

### 7. Implementation Roadmap

**Phase 1 (Weeks 1–4)**: Prompt-engineered prototype on Grok-4.3 (all 6 phases + PIC + basic multi-agent). Structured output validation.  
**Phase 2 (Months 2–3)**: Fine-tune lightweight speech act classifier on public datasets; integrate classical NLP metrics.  
**Phase 3 (Months 4–6)**: Full agentic orchestration, web UI, API, benchmark suite (accuracy, latency, user studies).  
**Phase 4 (Ongoing)**: Continuous evaluation on new pragmatic datasets; community benchmark contribution.

**Technology Stack**  
- Backend: Python + xAI SDK + LangGraph / custom agents  
- Frontend: Streamlit / Next.js  
- Storage: PostgreSQL + Qdrant (vector)  
- Evaluation: Custom harness using arXiv pragmatic datasets

---

### 8. Evaluation Framework

- **Automatic**: F1 on speech act datasets, PIC accuracy lift, Grice violation detection correlation with human labels.  
- **Human**: Expert linguist agreement (Cohen’s κ > 0.75 target).  
- **A/B Testing**: DIA vs baseline LLM on real-world texts (news, ads, political speech, X posts).  
- **xAI-Specific**: Measure reduction in sycophancy / hallucination in judgment phase.

---

### 9. Limitations & Future Work

**Current Limitations**  
- English-dominant (mitigate with multilingual PIC prompts).  
- Requires high-quality context for best results.  
- Computational cost on very long documents (mitigated by 1M context + summarization agents).

**Future**  
- Multimodal extension (video/audio discourse).  
- Real-time conversation monitoring (multi-party).  
- Fine-tuned DIA-specialist model on xAI infrastructure.  
- Open-source benchmark suite contribution to arXiv community.

---

### 10. References (Key Sources)

- Pragmatics in the Era of Large Language Models: A Survey (arXiv:2502.12378)  
- Pragmatic Inference Chain (PIC) (arXiv:2503.01539)  
- Multi-Party Conversational Agents: A Survey (arXiv:2505.18845)  
- Various Gricean Maxims in NLP papers (2024–2025)  
- xAI Grok-4.3 Model Card & API Documentation (2025–2026)  
- Original DIA framework (user conversation history, May 2026)

---

**This document constitutes the complete, actionable functional specification.**  

You can now:
- Copy it directly into a product requirements document or Notion.
- Hand it to engineers for implementation.
- Use it as the system prompt for building the actual Grok-powered DIA agent.

**Next Step Recommendation**: Provide a sample text (or confirm you want a live demonstration), and I will execute the full v2.0 pipeline on it using the exact enhanced structure above.  

Ready to build or test? Just say the word.



### Document: `plan/planner_agent_v2.1.md`

_Embedded from `corpus/plan/planner_agent_v2.1.md`. Also stored at `sources/plan/planner_agent_v2.1.md` under this agent folder._


# SIPA — Software Implementation Planner Agent

## Complete Research-Hardened Specification & Design Document

**Version:** 2.1 — Research-Hardened, Security-Operationalized  
**Date:** 2026-06-03  
**Status:** Production-Ready Design Spec  
**Primary Goal:** Convert very large software-specification corpora into high-fidelity, traceable, component-type-adaptive implementation plans and granular tasks for AI coding agents and human developers.

---

## Change Summary — v2.0 → v2.1

This revision is a deep-research pass and adversarial “100x rethink” consolidation. It does **not** merely expand the previous document; it tightens the system into an implementable, governable, security-aware planner.

### Major Improvements

1. **Research verification and correction**
   - Verified MAAD as arXiv:2606.01385, submitted May 31, 2026, and preserved it as the core architecture-planning influence. ([arxiv.org](https://arxiv.org/abs/2606.01385))
   - Updated AgentOrchestra reference: current arXiv title emphasizes the Tool-Environment-Agent, or TEA, protocol and lifecycle-aware orchestration rather than only “general-purpose task solving.” ([arxiv.org](https://arxiv.org/abs/2506.12508))
   - Updated GitHub Spec Kit alignment to include the current Spec → Plan → Tasks → Implement flow plus newer practical commands such as constitution, clarify, analyze, checklist, and task-to-issues. ([github.github.com](https://github.github.com/spec-kit/))
   - Qualified xAI/Grok Build claims: official xAI pages verify plan mode, parallel subagents, skills/plugins/hooks/MCP, headless mode, and API availability; this spec no longer depends on unofficial “Arena Mode” claims and instead defines SIPA’s own optional local “Arena Evaluator.” ([x.ai](https://x.ai/news/grok-build-cli))

2. **Added security and trust model**
   - Added prompt-injection, memory-poisoning, MCP/tool safety, least-privilege execution, untrusted-context boundaries, and human approval controls.
   - Integrated NCSC guidance that LLMs do not enforce a hard data/instruction boundary and should be treated as “inherently confusable” components. ([ncsc.gov.uk](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection))
   - Integrated MCP security principles around user consent, tool safety, data privacy, and untrusted tool descriptions. ([modelcontextprotocol.io](https://modelcontextprotocol.io/specification/2025-03-26/index))
   - Added OWASP GenAI/agentic risk alignment and operational monitoring requirements. ([genai.owasp.org](https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/))

3. **Strengthened context engineering**
   - Formalized SIPA’s context pipeline around **write, select, compress, isolate**, matching current agent context-engineering practice. ([langchain.com](https://www.langchain.com/blog/context-engineering))
   - Added retrieval budgets, evidence ledgers, source confidence levels, retrieval evaluation, and stale-source detection.
   - Added optional GraphRAG-style global/local retrieval for corpus-wide sensemaking and dependency impact analysis. ([microsoft.com](https://www.microsoft.com/en-us/research/project/graphrag/?msockid=334382bc6c746f231ca6946e6d716e0a))

4. **Expanded component taxonomy**
   - Added Security/Compliance, Testing/Quality, Migration/Legacy, AI/Agent Workflow, and Documentation/Developer Experience component types.
   - Added secondary risk tags that directly change retrieval depth, critic rubrics, and human-review requirements.

5. **Made outputs more machine-consumable**
   - Added artifact manifests, evidence ledgers, decision logs, task execution contracts, and canonical schemas.
   - Added stable IDs for requirements, claims, decisions, interfaces, tasks, risks, and open questions.

6. **Added evaluation science**
   - Added retrieval metrics, plan-quality metrics, artifact-level critic thresholds, and downstream coder-agent success metrics.
   - Integrated RAG evaluation dimensions such as context relevance, answer faithfulness, answer relevance, context precision, and context recall. ([aclanthology.org](https://aclanthology.org/2024.naacl-long.20/?utm_source=openai))

7. **Improved implementation roadmap**
   - Split MVP into a safer vertical slice.
   - Added CLI/API/MCP deployment model, observability, cache strategy, sandbox strategy, and governance gates.

---

## Table of Contents

1. Executive Summary
2. Core Problem
3. Research Foundation
4. Design Principles
5. Component Taxonomy
6. System Architecture
7. Agent Roles
8. End-to-End Workflow
9. Context Engineering, RAG, and Memory
10. Critic/Evaluator Subsystem
11. Security and Trust Model
12. Data Models and Schemas
13. Output Artifacts
14. Implementation Roadmap
15. Tool and Harness Integration
16. Metrics and Success Criteria
17. Risks and Mitigations
18. Future Roadmap
19. References

---

## 1. Executive Summary

SIPA is a hierarchical, context-engineered, multi-agent planning system for turning large software specification corpora into implementation-ready plans and tasks.

It is designed for projects where the source material may include:

- Markdown specs
- PRDs
- architecture notes
- API contracts
- user stories
- domain models
- UI descriptions
- ADRs
- implementation notes
- test plans
- legacy migration notes
- operational constraints

The key idea is simple but powerful:

> **Different software components require different levels and types of detail.**

A strategic architecture plan should not be generated with the same retrieval scope, summarization style, or output format as a UI screen, a shared library, a data model, or a migration adapter.

SIPA therefore uses:

- **Component-type classification**
- **Scoped retrieval**
- **Evidence-based synthesis**
- **Hierarchical memory**
- **Embedded critic loops**
- **Traceability-first artifacts**
- **Granular task generation**
- **Security-aware agent execution**

The result is a planner that reduces context size for downstream coding agents while improving fidelity, traceability, and implementation success.

---

## 2. Core Problem

Large software specs break AI coding workflows in predictable ways:

1. **Context overload**
   - Too much raw documentation causes distraction, contradiction, and missed details.

2. **Uniform summarization failure**
   - Architecture needs synthesis.
   - UI features need exhaustive local detail.
   - Shared components need contracts.
   - Data models need invariants.
   - Integrations need error semantics and compatibility rules.

3. **Loss of traceability**
   - Coding agents often implement plausible behavior that is not grounded in the source spec.

4. **Weak plan-to-task translation**
   - Large plans often become vague tasks.
   - Vague tasks create bad code, rework, and hidden assumptions.

5. **Security and tool-risk amplification**
   - Agentic coding tools can read files, run commands, call APIs, and modify repos.
   - Prompt injection, over-permissioned tools, and memory poisoning become architectural risks, not just prompt risks.

SIPA exists to solve these problems before coding begins.

---

## 3. Research Foundation

### 3.1 Spec-Driven Development

GitHub Spec Kit treats specifications as the center of AI-assisted development and ships a core flow of **Spec → Plan → Tasks → Implement**. It also provides Markdown artifacts, quality checklists, and cross-artifact analysis, making it a strong workflow model for SIPA’s output structure. ([github.github.com](https://github.github.com/spec-kit/))

SIPA extends this model for **pre-existing massive corpora**, not just greenfield features. It adds corpus indexing, type-aware planning, traceability enforcement, and critic loops.

### 3.2 MAAD and Requirements-to-Architecture Planning

MAAD proposes four specialized agents — Analyst, Modeler, Designer, and Evaluator — to convert requirements into multi-view architectural blueprints with quality assessments. It uses RAG for architecture standards and patterns, hierarchical memory for design history, and an evaluator for structured quality reports. ([arxiv.org](https://arxiv.org/abs/2606.01385))

SIPA adopts MAAD most directly for the Architecture Sub-Planner, then generalizes the same analyst/designer/evaluator structure across other component types.

### 3.3 Hierarchical Multi-Agent Orchestration

AgentOrchestra’s current formulation introduces TEA, a Tool-Environment-Agent protocol that treats agents, tools, environments, prompts, memory, and outputs as versioned lifecycle-managed resources. It also uses a central planner coordinating specialized sub-agents. ([arxiv.org](https://arxiv.org/abs/2506.12508))

SIPA adopts the practical lesson: orchestration should not be “agents chatting.” It should be explicit state, typed handoffs, versioned artifacts, and lifecycle-aware execution.

### 3.4 Multi-Agent Software Engineering Patterns

The LLM-based multi-agent systems survey identifies role specialization, SDLC coverage, agent synergy, and trustworthy autonomous software engineering as major research directions. ([arxiv.org](https://arxiv.org/abs/2404.04834))

MASAI shows the value of modular sub-agents with separate objectives and strategies for software-engineering tasks, including avoiding unnecessarily long trajectories and excessive context. ([arxiv.org](https://arxiv.org/abs/2406.11638?utm_source=openai))

SWE-agent demonstrates that the interface between agent and computer materially affects coding-agent performance, motivating SIPA’s emphasis on harness-native task packaging. ([arxiv.org](https://arxiv.org/abs/2405.15793?utm_source=openai))

SWE-Search supports the value of self-evaluation and iterative refinement for repository-level software tasks. ([proceedings.iclr.cc](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a1e6783e4d739196cad3336f12d402bf-Abstract-Conference.html?utm_source=openai))

### 3.5 Context Engineering

Modern agent design increasingly treats context engineering as a first-class discipline. LangChain’s current framework groups context strategies into **write, select, compress, and isolate**, which SIPA adopts as its core context model. ([langchain.com](https://www.langchain.com/blog/context-engineering))

SIPA applies this as follows:

- **Write:** Persist plans, decisions, summaries, memory, and evidence outside the prompt.
- **Select:** Retrieve only the task-relevant source chunks, patterns, and memories.
- **Compress:** Summarize and extract with source-preserving compression.
- **Isolate:** Give each sub-planner a scoped context window rather than the entire corpus.

### 3.6 GraphRAG and Corpus Sensemaking

GraphRAG combines text extraction, network analysis, LLM prompting, and summarization to understand text datasets. Microsoft’s GraphRAG project is especially relevant for corpus-wide themes and dependency discovery. ([microsoft.com](https://www.microsoft.com/en-us/research/project/graphrag/?msockid=334382bc6c746f231ca6946e6d716e0a))

SIPA uses graph retrieval optionally, but the architecture is designed so a simpler hybrid vector/BM25 retriever can be used first.

### 3.7 Architecture Standards

SIPA’s architecture outputs are aligned with:

- **ISO/IEC/IEEE 42010** concepts of stakeholders, concerns, viewpoints, and views. ([iso-architecture.org](https://www.iso-architecture.org/ieee-1471/cm/?utm_source=openai))
- **C4 model** levels: system context, container, component, and code, with an emphasis on only producing diagrams that add value. ([c4model.com](https://c4model.com/diagrams?utm_source=openai))
- **ATAM** for reasoning about quality-attribute tradeoffs and architectural risks. ([sei.cmu.edu](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/?utm_source=openai))
- **Kruchten 4+1 views** for multi-perspective architecture description. ([scirp.org](https://www.scirp.org/reference/referencespapers?referenceid=2072965&utm_source=openai))

### 3.8 Security Research and Agentic Risk

NCSC warns that current LLMs do not enforce a true boundary between data and instructions, so prompt injection should be treated as an inherent residual risk that must be reduced through system design and impact limitation. ([ncsc.gov.uk](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection))

OWASP’s GenAI exploit reporting shows AI security incidents are increasingly targeting agent identities, orchestration layers, supply chains, permissions, and validation controls rather than only model outputs. ([genai.owasp.org](https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/))

The MCP specification explicitly notes that MCP enables arbitrary data access and code execution paths, requiring user consent, data privacy controls, and caution around tool behavior descriptions. ([modelcontextprotocol.io](https://modelcontextprotocol.io/specification/2025-03-26/index))

SIPA therefore treats security as a core subsystem, not a postscript.

---

## 4. Design Principles

1. **Type-aware planning**
   - Every component gets the planning style it actually needs.

2. **Traceability before creativity**
   - SIPA may synthesize, but every major claim must be grounded in source evidence or explicitly marked as an assumption.

3. **Small context, high signal**
   - Never feed the full corpus to a sub-planner unless the task is corpus-level analysis.

4. **Critic-first quality culture**
   - Drafts are not final until they pass structured quality gates.

5. **Living specifications**
   - Plans are versioned, diffable, and updated as implementation changes.

6. **Harness-native outputs**
   - Outputs must be directly useful to Cursor, Claude Code, Kiro, Grok Build, OpenWebUI, custom CLI agents, or human developers.

7. **Security by architecture**
   - Tool access, memory, retrieval, source trust, and approval flows must be explicitly governed.

8. **Human gates where risk is high**
   - Human review is required for strategic, security-critical, destructive, or high-cost decisions.

9. **Evaluation built in**
   - Retrieval quality, traceability, consistency, implementability, and downstream success are measured.

10. **Composable implementation**
   - SIPA can start as a CLI and later expose MCP/API integrations.

---

## 5. Component Taxonomy

The taxonomy controls:

- Retrieval strategy
- Context budget
- Planner selection
- Output template
- Critic rubric
- Human-review requirement
- Task decomposition style

### 5.1 Primary Component Types

| Type | Detail Level | Retrieval Strategy | Output Emphasis | Example |
|---|---:|---|---|---|
| Architecture / Strategic | High-level synthesis | Broad cross-corpus retrieval + ASRs/NFRs + patterns | Views, ADRs, tradeoffs, quality attributes | System architecture, service topology |
| Feature / UI / Tactical | Deep scoped detail | Narrow feature retrieval + full local excerpts | User stories, acceptance criteria, flows, state, validation | Dashboard, onboarding flow |
| Common / Shared Component | Contract-focused | Cross-module references + interface mentions | APIs, types, invariants, extension points | Auth service, notification library |
| Data / Domain Model | Medium | Entities, relationships, invariants, lifecycle rules | Schemas, aggregates, constraints, migrations | User, Order, Course, ExamAttempt |
| Integration / External | Medium | API contracts, event schemas, third-party docs | Mapping, retry, idempotency, compatibility | Stripe adapter, LMS sync |
| Infrastructure / DevOps | High-operational | NFRs, deployment docs, runtime constraints | IaC, CI/CD, observability, scaling | Kubernetes, GitHub Actions |
| Security / Compliance | High-rigor | Security reqs, policies, threat models, data flows | Threat model, controls, audit evidence | PII handling, RBAC, encryption |
| Testing / Quality | Medium | Acceptance criteria, test notes, defect history | Test matrix, fixtures, validation strategy | E2E suite, contract tests |
| Migration / Legacy | Medium-high | Legacy docs, current behavior, target constraints | Strangler plan, compatibility, rollback | COBOL replacement, DB migration |
| AI / Agent Workflow | High-rigor | Agent instructions, tools, memory, data access | Agent state machine, tool policy, eval harness | Coding agent, RAG assistant |
| Documentation / DevEx | Medium | Onboarding docs, workflows, developer feedback | Quickstarts, AGENTS.md, conventions | Contributor guide, module README |

### 5.2 Secondary Tags

Secondary tags modify critic gates and output sections:

- `security-critical`
- `privacy-sensitive`
- `performance-sensitive`
- `high-availability`
- `user-facing`
- `internal-only`
- `regulated`
- `legacy-modernization`
- `agentic-tool-use`
- `destructive-actions`
- `requires-human-review`
- `experimental`
- `mvp-critical`

### 5.3 Classification Rules

SIPA classifies components using:

1. Explicit metadata if present.
2. Requirement IDs and section names.
3. Keyword heuristics.
4. LLM classifier with structured output.
5. Human override.
6. Critic validation.

Classification output must include:

```yaml
component_id: CMP-auth-service
name: Auth Service
primary_type: common_component
secondary_tags:
  - security-critical
  - privacy-sensitive
confidence: 0.91
evidence:
  - specs/auth.md#overview
  - specs/security.md#session-management
needs_human_review: true
```

---

## 6. System Architecture

```mermaid
flowchart TD
    A[Spec Corpus] --> B[Ingestion & Indexing]
    B --> C[Hybrid Retriever]
    B --> D[Knowledge Graph Optional]
    B --> E[Corpus Summary & Glossary]

    E --> F[Master Orchestrator]
    C --> F
    D --> F

    F --> G[Component Classifier]
    G --> H[Dependency Graph]
    H --> I[Master Plan]

    I --> J1[Architecture Sub-Planner]
    I --> J2[Feature/UI Sub-Planner]
    I --> J3[Common Component Sub-Planner]
    I --> J4[Data/Domain Sub-Planner]
    I --> J5[Integration Sub-Planner]
    I --> J6[Security/Compliance Sub-Planner]
    I --> J7[Testing/Quality Sub-Planner]

    J1 --> K[Critic/Evaluator]
    J2 --> K
    J3 --> K
    J4 --> K
    J5 --> K
    J6 --> K
    J7 --> K

    K -->|refine| J1
    K -->|refine| J2
    K -->|refine| J3
    K -->|refine| J4
    K -->|refine| J5
    K -->|refine| J6
    K -->|refine| J7

    K --> L[Approved Specs]
    L --> M[Task Decomposer]
    M --> N[Task Lists / Agent Work Packs]
    N --> O[Coder Agents / Humans]
    O --> P[Implementation Feedback]
    P --> Q[Memory Update + Impact Analysis]
    Q --> F
```

---

## 7. Agent Roles

### 7.1 Master Orchestrator

**Purpose:** Own the global plan, decomposition, dependencies, and coordination.

**Responsibilities:**

- Build corpus-level project understanding.
- Identify epics, modules, components, and phases.
- Classify components.
- Generate `master_plan.md`.
- Maintain dependency graph.
- Trigger sub-planners.
- Coordinate critic feedback and refinements.
- Escalate high-risk ambiguity to humans.

**Outputs:**

- `master_plan.md`
- `component_inventory.yml`
- `dependency_graph.mmd`
- `traceability_index.yml`
- `planning_run_manifest.json`

---

### 7.2 Architecture Sub-Planner

**Purpose:** Produce strategic architecture plans.

**Pattern:** MAAD-inspired Analyst → Modeler → Designer → Evaluator.

**Responsibilities:**

- Extract functional requirements, NFRs, and ASRs.
- Produce C4 and/or 4+1 views where useful.
- Generate ADRs.
- Identify tradeoffs.
- Define interface boundaries.
- Produce deployment and runtime views.
- Run ATAM-lite quality analysis.

**Outputs:**

- `architecture_<component>.md`
- `adr_<decision>.md`
- `architecture_views/*.mmd`
- `quality_attribute_scenarios.yml`

---

### 7.3 Feature/UI Sub-Planner

**Purpose:** Produce detailed, scoped implementation specs for user-facing behavior.

**Responsibilities:**

- Extract user stories.
- Expand acceptance criteria.
- Define UI states.
- Define user flows.
- Identify validations and errors.
- Link APIs and data dependencies.
- Generate implementation-sized tasks.

**Outputs:**

- `feature_spec_<name>.md`
- `flow_<name>.mmd`
- `acceptance_criteria_<name>.yml`
- `tasks_<name>.md`

---

### 7.4 Common Component Sub-Planner

**Purpose:** Produce contract-first shared component specs.

**Responsibilities:**

- Aggregate scattered mentions.
- Define public interfaces.
- Define invariants.
- Define extension points.
- Document configuration.
- Document failure modes.
- Provide usage examples.

**Outputs:**

- `component_spec_<name>.md`
- `interface_contract_<name>.yml`
- `usage_examples_<name>.md`

---

### 7.5 Data/Domain Sub-Planner

**Purpose:** Produce domain model and data lifecycle specifications.

**Responsibilities:**

- Identify entities, aggregates, value objects, and relationships.
- Define lifecycle states.
- Capture invariants and constraints.
- Identify migration and versioning needs.
- Define query patterns.
- Link domain objects to features and APIs.

**Outputs:**

- `domain_model_<bounded_context>.md`
- `schema_conceptual_<bounded_context>.mmd`
- `invariants_<bounded_context>.yml`

---

### 7.6 Integration Sub-Planner

**Purpose:** Produce robust integration and adapter specs.

**Responsibilities:**

- Define external contracts.
- Map source and target data.
- Define retry, timeout, idempotency, and backoff.
- Define auth and secret handling.
- Define version compatibility.
- Define observability and reconciliation.

**Outputs:**

- `integration_spec_<name>.md`
- `contract_mapping_<name>.yml`
- `integration_test_plan_<name>.md`

---

### 7.7 Security/Compliance Sub-Planner

**Purpose:** Produce security-sensitive plans and controls.

**Responsibilities:**

- Identify assets, trust boundaries, actors, and data flows.
- Threat-model agent/tool/data paths.
- Map requirements to controls.
- Define least-privilege policies.
- Define audit evidence.
- Require human approval for high-risk actions.

**Outputs:**

- `security_spec_<scope>.md`
- `threat_model_<scope>.md`
- `control_matrix_<scope>.yml`
- `approval_policy_<scope>.yml`

---

### 7.8 Critic/Evaluator

**Purpose:** Prevent bad plans from becoming implementation tasks.

**Critic dimensions:**

- Traceability
- Source fidelity
- Completeness
- Consistency
- Implementability
- Testability
- Security
- Risk
- Sizing
- Downstream agent usability

**Outputs:**

- `critique_<artifact>.json`
- `patch_instructions_<artifact>.md`
- `quality_gate_report_<artifact>.md`

---

### 7.9 Task Decomposer

**Purpose:** Convert approved specs into small, executable tasks.

**Task properties:**

- One logical change.
- Clear acceptance criteria.
- Source links.
- Relevant context excerpt.
- Dependencies.
- Suggested files.
- Test expectations.
- Rollback notes if needed.

**Outputs:**

- `tasks_<component>.md`
- optional issue exports
- optional agent work-pack JSON

---

## 8. End-to-End Workflow

### Phase 0 — Project Constitution

Before planning, SIPA should establish or ingest project principles.

Inputs may include:

- architecture principles
- coding standards
- testing standards
- security rules
- stack preferences
- UX rules
- naming conventions
- human review policy

Output:

```text
constitution.md
```

This aligns with current Spec Kit practice, where a constitution can govern subsequent specification, planning, and implementation artifacts. ([github.com](https://github.com/github/spec-kit))

---

### Phase 1 — Ingestion and Indexing

Steps:

1. Scan source directories.
2. Respect include/exclude rules.
3. Parse Markdown heading hierarchy.
4. Extract requirement IDs.
5. Detect components, entities, APIs, screens, and decisions.
6. Chunk semantically.
7. Generate embeddings.
8. Build keyword index.
9. Optionally build graph index.
10. Generate corpus summary and glossary.

Outputs:

- `corpus_index.md`
- `glossary.md`
- `chunks.parquet`
- `embeddings.db`
- `knowledge_graph.graphml`
- `ingestion_manifest.json`

---

### Phase 2 — Master Plan

The Master Orchestrator:

1. Reads corpus summaries.
2. Retrieves global cross-cutting requirements.
3. Builds initial component inventory.
4. Classifies components.
5. Generates dependency graph.
6. Creates implementation phases.
7. Identifies MVP slice.
8. Flags risks and unknowns.
9. Runs master-plan critic.

Output:

```text
plans/master_plan.md
```

Required sections:

- project summary
- scope
- non-goals
- component inventory
- phases
- dependency graph
- risk register
- traceability skeleton
- open questions
- human approval checklist

---

### Phase 3 — Type-Aware Sub-Planning

For each component:

1. Confirm component type.
2. Assemble context package.
3. Run relevant sub-planner.
4. Generate draft artifact.
5. Run critic.
6. Patch only failing sections.
7. Re-run critic.
8. Persist approved artifact.

Output examples:

```text
plans/architecture_core_platform.md
plans/feature_spec_student_dashboard.md
plans/component_spec_auth_service.md
plans/domain_model_user_progress.md
plans/integration_spec_lms_sync.md
plans/security_spec_auth_and_sessions.md
```

---

### Phase 4 — Task Generation

The Task Decomposer creates implementation tasks from approved plans.

Task format:

```markdown
- [ ] T042 [P] Build StudentDashboardHeader
  - **Component:** Student Dashboard
  - **Source:** feature_spec_student_dashboard.md#ui-header
  - **Depends on:** T011, T018
  - **Acceptance:**
    - Renders avatar, name, role, and notification state.
    - Handles loading and empty-avatar states.
    - Meets responsive behavior defined in section 4.2.
  - **Tests:**
    - Unit render states.
    - E2E dropdown interaction.
  - **Context excerpt:** See linked source section.
```

---

### Phase 5 — Implementation Feedback

After coder agents or humans execute tasks, SIPA ingests:

- diffs
- test results
- review comments
- implementation blockers
- changed assumptions
- failed tasks
- new requirements

SIPA then:

1. Updates episodic memory.
2. Performs impact analysis.
3. Updates affected plans.
4. Re-runs critic gates.
5. Regenerates affected tasks.

---

## 9. Context Engineering, RAG, and Memory

### 9.1 Context Package Structure

Every sub-planner receives a context package:

```yaml
context_package_id: CTX-feature-student-dashboard-v1
component_id: CMP-student-dashboard
planner_type: feature_ui
token_budget:
  max_total: 45000
  source_evidence: 25000
  memory: 5000
  master_context: 5000
  template_and_instructions: 5000
retrievals:
  - chunk_id: CHK-00123
    source: specs/student.md#dashboard
    relevance: 0.94
    trust_level: canonical
  - chunk_id: CHK-00418
    source: specs/ui.md#notifications
    relevance: 0.87
    trust_level: canonical
compression:
  method: extractive_then_abstractive
  preserve_quotes: true
  preserve_requirement_ids: true
```

### 9.2 Retrieval Modes

| Mode | Purpose |
|---|---|
| Exact ID lookup | Requirement IDs, ADR IDs, API names |
| BM25 keyword | Exact technical terms |
| Vector search | Semantic similarity |
| Graph traversal | Dependencies and trace links |
| Global summarization | Corpus-wide themes |
| Local neighborhood | Closely related chunks |
| Reranked hybrid | Default production mode |

### 9.3 Memory Types

| Memory | Scope | Examples |
|---|---|---|
| Working | Current run | draft, active critic notes |
| Episodic | Past runs | refinements, implementation feedback |
| Semantic | Generalized knowledge | patterns, glossary, conventions |
| Procedural | Agent behavior | prompts, rubrics, templates |
| Evidence | Source-grounding | chunk IDs, citations, excerpts |
| Security | Trust and permissions | approved tools, blocked actions |

### 9.4 Evidence Ledger

Every major output claim should map to evidence:

```yaml
claim_id: CLM-architecture-012
claim: "Auth Service owns session creation and refresh-token rotation."
artifact: component_spec_auth_service.md
evidence:
  - source: specs/auth.md#session-lifecycle
    quote: "..."
  - source: specs/security.md#refresh-token-policy
    quote: "..."
confidence: 0.93
status: supported
```

---

## 10. Critic/Evaluator Subsystem

### 10.1 Quality Gates

| Gate | Required For | Pass Threshold |
|---|---|---:|
| Traceability | all artifacts | ≥ 0.90 |
| Source fidelity | all artifacts | ≥ 0.92 |
| Internal consistency | all artifacts | ≥ 0.90 |
| Cross-artifact consistency | multi-component plans | ≥ 0.88 |
| Implementability | task lists | ≥ 0.90 |
| Testability | features/components | ≥ 0.90 |
| Security review | tagged artifacts | no high findings |
| Human approval | strategic/high-risk | explicit approval |

### 10.2 Critique Schema

```json
{
  "artifact_id": "feature_spec_student_dashboard",
  "overall_verdict": "refine",
  "scores": {
    "traceability": 0.86,
    "source_fidelity": 0.93,
    "consistency": 0.91,
    "implementability": 0.88,
    "testability": 0.84,
    "security": 0.90
  },
  "issues": [
    {
      "severity": "high",
      "category": "traceability",
      "location": "section 4.3",
      "description": "Notification polling interval is asserted without source evidence.",
      "suggested_patch": "Either link to source requirement or mark as assumption requiring human approval."
    }
  ],
  "recommended_next_action": "targeted_refinement"
}
```

### 10.3 Optional SIPA Arena Evaluator

SIPA can run multiple competing planner outputs and evaluate them using the same rubric.

Arena mode should compare:

- traceability
- clarity
- completeness
- risk handling
- taskability
- security posture
- source fidelity

This is independent of any external vendor feature. Official xAI documentation verifies Grok Build plan mode and parallel subagents, but SIPA’s evaluator must remain vendor-neutral. ([x.ai](https://x.ai/news/grok-build-cli))

---

## 11. Security and Trust Model

### 11.1 Core Security Assumptions

1. Retrieved documents may contain malicious instructions.
2. Tool descriptions may be untrusted.
3. Memory can be poisoned.
4. Agent outputs can be wrong even when confident.
5. Human approval is only useful if the UI shows the actual action, not merely the agent’s summary.
6. High-impact operations require deterministic controls outside the LLM.

### 11.2 Trust Levels

| Trust Level | Meaning | Example |
|---|---|---|
| canonical | approved source of truth | reviewed spec |
| trusted-derived | generated from canonical and approved | approved plan |
| unreviewed-derived | generated but not approved | draft plan |
| external | outside corpus | web docs |
| untrusted | user/tool/retrieved content with possible injection | arbitrary webpage |
| hostile-test | adversarial fixture | red-team prompt |

### 11.3 Tool Permission Policy

| Action | Default |
|---|---|
| Read project specs | allowed |
| Write generated plans | allowed in output directory |
| Modify source code | blocked by SIPA planner |
| Run shell commands | blocked unless explicit tool mode |
| Delete files | human approval required |
| Access secrets | prohibited |
| Call external APIs | human approval required |
| Install packages | human approval required |
| Update memory | allowed only through memory sanitizer |

### 11.4 Prompt-Injection Controls

SIPA must:

- Wrap retrieved content as untrusted evidence.
- Never let retrieved content override system/developer instructions.
- Strip or flag suspicious instructions in source chunks.
- Separate source evidence from planner instructions.
- Use deterministic policy checks for tool calls.
- Log source-to-claim mappings.
- Require human approval for high-impact actions.

### 11.5 MCP Controls

If SIPA exposes MCP tools:

- Every tool must have a narrow schema.
- Destructive tools must require explicit approval.
- Tool descriptions must be treated as untrusted unless from trusted servers.
- MCP resources must not be forwarded without consent.
- Tool calls must be logged with inputs, outputs, requester, and artifact ID.

These requirements follow MCP’s own security posture around user consent, tool safety, data privacy, and arbitrary code execution risks. ([modelcontextprotocol.io](https://modelcontextprotocol.io/specification/2025-03-26/index))

---

## 12. Data Models and Schemas

### 12.1 Core Artifact Frontmatter

```yaml
---
artifact_id: string
type: master_plan | architecture | feature_ui | common_component | domain_model | integration | security | task_list | critique
component_id: string
component_name: string
primary_type: string
secondary_tags: []
version: string
status: draft | in_review | approved | implemented | superseded
created_at: ISO-8601
updated_at: ISO-8601
source_corpus_version: string
traceability_score: number
critic_score: number
dependencies: []
review_required: boolean
approved_by: string | null
---
```

### 12.2 Requirement Record

```yaml
requirement_id: REQ-001
text: "Users must be able to reset their password by email."
source:
  file: specs/auth.md
  section: password-reset
type: functional
priority: must
component_refs:
  - CMP-auth-service
  - CMP-email-service
status: active
```

### 12.3 Decision Record

```yaml
decision_id: ADR-004
title: "Use refresh-token rotation"
status: proposed
context: "Session persistence requires secure long-lived authentication."
decision: "Use short-lived access tokens and rotating refresh tokens."
alternatives:
  - server-side sessions
  - static refresh tokens
consequences:
  positive:
    - limits replay window
  negative:
    - requires token-family invalidation logic
evidence:
  - specs/security.md#token-policy
```

### 12.4 Task Record

```yaml
task_id: T042
title: "Implement refresh-token rotation"
component_id: CMP-auth-service
source_artifacts:
  - component_spec_auth_service.md#refresh-token-rotation
dependencies:
  - T038
parallelizable: false
risk: high
acceptance_criteria:
  - "Refresh token is rotated on every successful refresh."
  - "Reuse of old refresh token invalidates token family."
tests:
  - "unit"
  - "integration"
human_review_required: true
```

---

## 13. Output Artifacts

### 13.1 `master_plan.md`

Required sections:

1. Executive summary
2. Scope and non-goals
3. Corpus summary
4. Component inventory
5. Component classification table
6. Dependency graph
7. Implementation phases
8. MVP slice
9. Risk register
10. Traceability skeleton
11. Open questions
12. Approval checklist
13. Changelog

### 13.2 Architecture Spec

Required sections:

1. Architecture scope
2. Stakeholders and concerns
3. ASRs and NFRs
4. C4 context/container/component views
5. Runtime scenarios
6. Deployment view
7. ADRs
8. Interface catalog
9. Quality attribute scenarios
10. Tradeoff analysis
11. Risks
12. Traceability matrix

### 13.3 Feature/UI Spec

Required sections:

1. Feature summary
2. User stories
3. User flows
4. UI states
5. Acceptance criteria
6. Validation matrix
7. Error and edge cases
8. API/data dependencies
9. Accessibility notes
10. Analytics/events
11. Test scenarios
12. Traceability matrix

### 13.4 Common Component Spec

Required sections:

1. Purpose
2. Scope
3. Public interface
4. Data contracts
5. Invariants
6. Configuration
7. Extension points
8. Error handling
9. Performance expectations
10. Security considerations
11. Usage examples
12. Test strategy
13. Traceability matrix

### 13.5 Security Spec

Required sections:

1. Assets
2. Actors
3. Trust boundaries
4. Data flows
5. Threats
6. Controls
7. Residual risks
8. Approval requirements
9. Monitoring
10. Audit evidence
11. Traceability matrix

### 13.6 Task List

Required sections:

1. Task overview
2. Execution order
3. Parallelizable tasks
4. Critical path
5. Task checklist
6. Test checklist
7. Review checklist
8. Rollback notes
9. Source links

---

## 14. Implementation Roadmap

### Phase 1 — Safe MVP

Build a vertical slice:

- Corpus loader
- Markdown chunker
- Hybrid search
- Component classifier
- Master planner
- One sub-planner
- Basic critic
- Markdown renderer
- Task decomposer
- CLI command

Recommended first sub-planner: **Feature/UI** if validating implementation handoff, or **Architecture** if validating strategic planning.

### Phase 2 — Core System

Add:

- All primary sub-planners
- Knowledge graph
- Evidence ledger
- Hierarchical memory
- Multi-stage critic
- Human approval gates
- Incremental re-planning
- Evaluation metrics
- Template library

### Phase 3 — Production Hardening

Add:

- Observability dashboard
- Cost/token tracking
- Model routing
- Prompt/version registry
- MCP server
- Sandboxed tool mode
- Security red-team suite
- CI validation
- Plan drift detection
- Issue tracker export

### Phase 4 — Self-Improvement

Add:

- Planner performance analytics
- Failed-task learning
- Retrieval strategy optimization
- Prompt/template evolution
- Domain-specific taxonomies
- Automatic benchmark generation

---

## 15. Tool and Harness Integration

### 15.1 Cursor / Claude Code / Kiro / Similar Tools

SIPA should write:

```text
plans/
tasks/
AGENTS.md
.cursor/rules/
.claude/commands/
```

Generated `AGENTS.md` should include:

- module conventions
- relevant plan links
- forbidden actions
- test expectations
- source-of-truth order

### 15.2 Grok Build

Official xAI docs verify that Grok Build supports plan mode, headless scripting, custom models, skills/plugins, MCP servers, and parallel subagents. ([x.ai](https://x.ai/cli))

SIPA integration pattern:

1. SIPA generates approved plan and task pack.
2. Grok Build runs in plan mode.
3. Human compares Grok’s execution plan to SIPA task criteria.
4. Implementation proceeds only after approval.
5. SIPA ingests diffs and test results.

### 15.3 MCP/API Mode

SIPA can expose:

- `sipa.index_corpus`
- `sipa.get_master_plan`
- `sipa.plan_component`
- `sipa.critique_artifact`
- `sipa.generate_tasks`
- `sipa.trace_requirement`
- `sipa.impact_analysis`

All write or destructive operations require authorization.

---

## 16. Metrics and Success Criteria

### 16.1 Retrieval Metrics

- Context precision
- Context recall
- Source coverage
- Duplicate chunk rate
- Stale source rate
- Evidence sufficiency
- Unsupported claim rate

### 16.2 Artifact Metrics

- Traceability score
- Source-fidelity score
- Consistency score
- Completeness score
- Testability score
- Implementability score
- Security score
- Human review time

### 16.3 Downstream Metrics

- Task completion rate
- Rework rate
- Test pass rate
- Spec deviation rate
- Clarification count
- Average task context size
- Time from spec change to updated tasks

### 16.4 MVP Success Thresholds

- Traceability ≥ 0.85 for MVP, ≥ 0.90 for production.
- No high-severity critic findings on approved artifacts.
- Average refinement loops < 3.
- At least 30% reduction in downstream task clarification.
- At least 50% reduction in context passed to coder agents compared with raw-spec prompting.

---

## 17. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Bad retrieval | Hybrid search, reranking, evidence ledger, retrieval eval |
| Hallucinated plans | Source-fidelity critic, unsupported-claim detector |
| Over-decomposition | Task sizing critic |
| Under-decomposition | Dependency and acceptance-criteria checks |
| Conflicting specs | Conflict detector and human resolution |
| Prompt injection | Untrusted-source boundaries, deterministic controls |
| Memory poisoning | Memory sanitizer and trust levels |
| Tool abuse | Least privilege and approval gates |
| Stale plans | Incremental indexing and impact analysis |
| High token cost | Compression, caching, model routing |
| Human bottleneck | Risk-based approvals |
| Vendor lock-in | Markdown-first artifacts and MCP-compatible API |

---

## 18. Future Roadmap

1. Full GraphRAG impact analysis.
2. Multimodal ingestion for UI mocks and architecture diagrams.
3. Automatic test generation from acceptance criteria.
4. Formal-methods bridge for critical invariants.
5. Domain packs for edtech, finance, embedded systems, and legacy modernization.
6. Jira/GitHub issue export.
7. Continuous plan-code drift detection.
8. Multi-model evaluator arena.
9. Self-optimizing prompt/template registry.
10. Secure enterprise deployment bundle.

---

## 19. References

- MAAD — requirements-to-architecture multi-agent design with Analyst, Modeler, Designer, Evaluator, RAG, hierarchical memory, and quality evaluation. ([arxiv.org](https://arxiv.org/abs/2606.01385))
- AgentOrchestra / TEA Protocol — lifecycle-aware hierarchical multi-agent orchestration. ([arxiv.org](https://arxiv.org/abs/2506.12508))
- LLM-Based Multi-Agent Systems for Software Engineering survey. ([arxiv.org](https://arxiv.org/abs/2404.04834))
- Designing LLM-based Multi-Agent Systems for SE Tasks — quality attributes, design patterns, and rationale. ([arxiv.org](https://arxiv.org/abs/2511.08475))
- GitHub Spec Kit documentation and repository. ([github.github.com](https://github.github.com/spec-kit/))
- LangChain context engineering: write, select, compress, isolate. ([langchain.com](https://www.langchain.com/blog/context-engineering))
- Microsoft GraphRAG project. ([microsoft.com](https://www.microsoft.com/en-us/research/project/graphrag/?msockid=334382bc6c746f231ca6946e6d716e0a))
- MASAI modular software-engineering agents. ([arxiv.org](https://arxiv.org/abs/2406.11638?utm_source=openai))
- SWE-agent agent-computer interface research. ([arxiv.org](https://arxiv.org/abs/2405.15793?utm_source=openai))
- SWE-Search iterative refinement and MCTS for software agents. ([proceedings.iclr.cc](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a1e6783e4d739196cad3336f12d402bf-Abstract-Conference.html?utm_source=openai))
- ARES and RAGAS-style RAG evaluation dimensions. ([aclanthology.org](https://aclanthology.org/2024.naacl-long.20/?utm_source=openai))
- ISO/IEC/IEEE 42010 architecture description concepts. ([iso-architecture.org](https://www.iso-architecture.org/ieee-1471/cm/?utm_source=openai))
- C4 model diagrams. ([c4model.com](https://c4model.com/diagrams?utm_source=openai))
- ATAM architecture tradeoff analysis. ([sei.cmu.edu](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/?utm_source=openai))
- NCSC prompt-injection guidance. ([ncsc.gov.uk](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection))
- OWASP GenAI exploit reporting and agentic risk framing. ([genai.owasp.org](https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/))
- Model Context Protocol specification and security principles. ([modelcontextprotocol.io](https://modelcontextprotocol.io/specification/2025-03-26/index))
- xAI Grok Build official CLI and documentation pages. ([x.ai](https://x.ai/news/grok-build-cli))

---
Learn more:
1. [\[2606.01385\] Bridging Requirements and Architecture: Multi-Agent Orchestration with External Knowledge and Hierarchical Memory](https://arxiv.org/abs/2606.01385)
2. [\[2506.12508\] AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool-Environment-Agent(TEA) Protocol](https://arxiv.org/abs/2506.12508)
3. [GitHub Spec Kit | Spec Kit Documentation](https://github.github.com/spec-kit/)
4. [Introducing Grok Build | xAI](https://x.ai/news/grok-build-cli)
5. [Prompt injection is not SQL injection (it may be worse) | National Cyber Security Centre](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection)
6. [Specification - Model Context Protocol](https://modelcontextprotocol.io/specification/2025-03-26/index)
7. [OWASP GenAI Exploit Round-up Report Q1 2026 - OWASP Gen AI Security Project](https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/)
8. [Context Engineering](https://www.langchain.com/blog/context-engineering)
9. [Project GraphRAG - Microsoft Research](https://www.microsoft.com/en-us/research/project/graphrag/?msockid=334382bc6c746f231ca6946e6d716e0a)
10. [ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems - ACL Anthology](https://aclanthology.org/2024.naacl-long.20/?utm_source=openai)
11. [\[2404.04834\] LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision and the Road Ahead](https://arxiv.org/abs/2404.04834)
12. [MASAI: Modular Architecture for Software-engineering AI Agents](https://arxiv.org/abs/2406.11638?utm_source=openai)
13. [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793?utm_source=openai)
14. [SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a1e6783e4d739196cad3336f12d402bf-Abstract-Conference.html?utm_source=openai)
15. [ISO/IEC/IEEE 42010: Conceptual Model](https://www.iso-architecture.org/ieee-1471/cm/?utm_source=openai)
16. [Diagrams | C4 model](https://c4model.com/diagrams?utm_source=openai)
17. [The Architecture Tradeoff Analysis Method | CMU Software Engineering Institute](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/?utm_source=openai)
18. [Kruchten, P. (1995) Architectural Blueprints—The “4+1” View Model of Software Architecture. IEEE Software, 12, 42-50. - References - Scientific Research Publishing](https://www.scirp.org/reference/referencespapers?referenceid=2072965&utm_source=openai)
19. [GitHub - github/spec-kit:  Toolkit to help you get started with Spec-Driven Development · GitHub](https://github.com/github/spec-kit)
20. [Grok Build Beta | xAI](https://x.ai/cli)
21. [\[2511.08475\] Designing LLM-based Multi-Agent Systems for Software Engineering Tasks: Quality Attributes, Design Patterns and Rationale](https://arxiv.org/abs/2511.08475)



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



### Document: `study/SYSTEM_REFERENCE.md`

_Embedded from `corpus/study/SYSTEM_REFERENCE.md`. Also stored at `sources/study/SYSTEM_REFERENCE.md` under this agent folder._


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
| 24 | MusicVideoDirectorAgent | Visual concept for songs | — |
| 25 | ComedyWriterAgent | Skits, parody, viral memes | — |
| 26 | TalentAgent (On-camera) | AI-rendered performance | — |
| 27 | UGCCreatorAgent | Authentic-feel ads | — |

**Roster reference:** [agents.md](./agents.md) §5


### 3.6 Distribution & Marketing Agents (28–31)

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 28 | SocialMediaStrategistAgent | Platform distribution, trends | — |
| 29 | CopywriterAgent | Scripts, captions, hooks | — |
| 30 | CreativeDirectorAgent | Campaign concept | — |
| 31 | PerformanceMarketerAgent | Optimize ads for ROAS | — |

**Roster reference:** [agents.md](./agents.md) §6

### 3.7 Education & Domain-Expert Agents (32–45)

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

**Roster reference:** [agents.md](./agents.md) §7

### 3.8 AI-Era Specialist Agents (46–52)

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 46 | PromptEngineerAgent | Crafts prompts; steers gen models | — |
| 47 | AvatarDesignAgent | Synthetic presenter identity | — |
| 48 | VoiceCloneAgent / LipSync | Voice cloning + lip-sync | — |
| 49 | AIQAConsistencyAgent | Frame drift, artifacts, identity breaks | — |
| 50 | PersonalizationEngineerAgent | Variable templates (name/face swap) | — |
| 51 | TrailerEditorAgent | Hook-driven trailer cuts | — |
| 52 | SportsAnalystAgent | Tactical breakdowns + diagrams | — |

**Roster reference:** [agents.md](./agents.md) §8


### 3.9 Specialist Meta-Agents (53–80)

These agents manage orchestration, quality, continuity, and system-level concerns:

| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 53 | OrchestratorAgent | DAG execution, retries, fan-out/fan-in | — |
| 54 | PlannerAgent | Decomposes brief into phased DAG | — |
| 55 | RouterAgent | Picks right agent + model for subtask | — |
| 56 | JudgeAgent | Adjudicates disputes via debate | — |
| 57–80 | (Various meta-agents) | Memory, continuity, safety, escalation, etc. | — |

**Roster reference:** [agents.md](./agents.md) §9

### 3.10 Workflow Support Agents (81–114)

These agents provide production infrastructure services:

| Range | Function | Examples |
|-------|----------|----------|
| 81–90 | Asset management, versioning, render dispatch | RenderFarmAgent, AssetManagerAgent |
| 91–100 | Quality gates, delivery packaging, compliance | DeliveryAgent, QCGateAgent |
| 101–114 | Analytics, feedback loops, retraining triggers | AnalyticsAgent, FeedbackLoopAgent |

**Roster reference:** [agents.md](./agents.md) §10

---

## 4. Infrastructure & Support Agents

These cross-cutting agents have their own **deep functional and technical specifications** because they serve the entire system:

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


---

## 5. Cross-Cutting Capabilities

These specifications define capabilities that are shared across multiple agents or apply system-wide:

| Capability | What It Provides | Used By | Specification |
|-----------|-----------------|---------|---------------|
| **Strategic Goal Achievement Framework** | 6-stage self-inquiry system for transforming vague goals into actionable plans | All planning agents (PlannerAgent, ProducerAgent, DirectorAgent) | [strategic_goal_achievement_agent_functional_specification.md](./strategic_goal_achievement_agent_functional_specification.md) |
| **Screenwriter Goal Achievement** | Practical demonstration of goal framework applied to creative writing | ScreenwriterAgent, ShowrunnerAgent, ComedyWriterAgent | [screenwriter_strategic_goal_achievement_agent_functional_specification.md](./screenwriter_strategic_goal_achievement_agent_functional_specification.md) |
| **Psychological Profiling** | 100 creator profiles with MBTI, motivations, fears, creative parameters | CastingAgent, TalentAgent, PersonalizationEngineerAgent, UGCCreatorAgent | [psychological_profile_agent_functional_specifications.md](./psychological_profile_agent_functional_specifications.md) |
| **Psychological Recommendation** | Psychology-based preference prediction (Big Five, emotional state) | AudienceSimAgent, PerformanceMarketerAgent, PersonalizationEngineerAgent | [psychological_recommendation_agent_functional_specification.md](./psychological_recommendation_agent_functional_specification.md) |
| **Complex Problem Solving** | WHAT/WHY/HOW/DO/REVIEW structured methodology | All diagnostic agents (FactCheckerAgent, SMEAgent, JudgeAgent, OptimizationAgent) | [complex_problem_solution_process_model.md](./complex_problem_solution_process_model.md) |
| **Common Agent Structure** | Shared architectural pattern for all agents | All 114 agents | [common-agent-structure.svg](./common-agent-structure.svg) + [common-agent-structure.html](./common-agent-structure.html) |

---

## 6. Workflow Integration

### 6.1 Production Pipeline (End-to-End)

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


### 6.2 Workflow Variants (by Video Type)

Each video type follows a customized path through the agent DAG. Visual workflows are available as SVGs:

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

### 6.3 Human Baseline Comparison

The system is designed as a direct AI replacement/augmentation of the human production workflow:

> **Reference:** [human_video_production_workflow.md](./human_video_production_workflow.md) — Defines the 52 human craft roles that the agent system maps to and extends.

---

## 7. Data Flow & Handoff Contracts

Every agent communicates via a **Shared Artifact Handoff Contract** (machine-readable JSON manifest):

| Field | Purpose |
|-------|---------|
| `artifact_id` / `version` | Unique identity for every output and revision |
| `parent_assets` | Provenance links to scripts, prompts, plates, stems |
| `brief_scope` | Subtask, acceptance criteria, target audience |
| `technical_spec` | Codec, aspect ratio, duration, frame rate, color space, loudness |
| `rights_and_consent` | License state, likeness/voice consent, territorial limits |
| `continuity_state` | Character look, props, wardrobe, environment, identity hash |
| `qc_status` | Latest L1/L2/L3 QC result |
| `target_channels` | Theatrical, streaming, broadcast, social, CRM, LMS |
| `provenance_manifest` | C2PA reference, critique log pointer, sign-off chain |

> **Full contract spec:** [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) §1.3

### 7.1 Critique Bus Protocol

All agents communicate critique via a structured JSON bus:

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


---

## 8. UI & Communication Layer

The frontend provides human operators with visibility and control over the agent swarm:

| UI Document | Covers | Link |
|------------|--------|------|
| Architecture & Communication | Three-tier protocol (REST, WebSocket, Agent Queue) | [ui/architecture_communication.md](./ui/architecture_communication.md) |
| Agent Management UI | How to monitor, configure, and override agents | [ui/agent_management_ui.md](./ui/agent_management_ui.md) |
| Backend Agent Management | Server-side agent lifecycle, scaling, health | [ui/backend_agent_management.md](./ui/backend_agent_management.md) |
| UI Design | Visual design system, components, interactions | [ui/ui_design.md](./ui/ui_design.md) |
| Project Creation Flow | User journey from brief to running production | [ui/project_creation_flow.md](./ui/project_creation_flow.md) |
| Production Scale Discovery | How the system adapts to project complexity | [ui/production_scale_discovery.md](./ui/production_scale_discovery.md) |
| Video Remake Enhancement | Workflow for improving existing videos | [ui/video_remake_enhancement.md](./ui/video_remake_enhancement.md) |
| 100 Improvements Rethink | Comprehensive UI improvement catalog | [ui/RETHINK_100_IMPROVEMENTS.md](./ui/RETHINK_100_IMPROVEMENTS.md) |

---

## 9. Technology Stack Reference

### 9.1 LLM Providers (for Agent Reasoning)

| Provider | Models | Primary Use |
|----------|--------|------------|
| xAI | Grok-4.x | Primary reasoning, tool use, research |
| Google DeepMind | Gemini 2.5 Pro (1M context) | Long-context analysis, bible search |
| OpenAI | GPT-4o, o-series | Structured outputs, consensus sampling |
| Anthropic | Claude 4 | Safety, constitutional AI agents |
| Open-source | Qwen2.5, Wan 2.6 | Cost optimization, local inference |

### 9.2 Video Generation Models

> **Full reference (50 models ranked):** [video_generation_techology_should_learn_now.md](./video_generation_techology_should_learn_now.md)

| Rank | Model | Primary Use in System |
|------|-------|--------------------|
| 1 | Seedance 2.0 (ByteDance) | Multimodal generation with native audio |
| 2 | Kling 3.0 (Kuaishou) | Motion control, multi-character scenes |
| 3 | Veo 3.1 (Google) | Cinematic quality, character consistency |
| 4 | Grok Imagine Video (xAI) | Fast iteration, social-first output |
| 6 | Sora 2 (OpenAI) | Narrative/physics storytelling |
| 8 | Runway Gen-4.5 | Professional creative control, VFX |

### 9.3 Audio/Voice Tools

| Tool | Purpose |
|------|---------|
| ElevenLabs v3 | TTS, voice cloning, sound effects |
| Sync.so | Lip-sync alignment |
| Udio/Suno | Music generation |
| Dolby Atmos Renderer | Spatial audio mixing |

### 9.4 Infrastructure

| Component | Technology |
|-----------|-----------|
| Orchestration | LangGraph + Temporal |
| Event Bus | Redis Streams / NATS |
| Asset Storage | S3 + metadata DB |
| Observability | LangSmith + AgentOps |
| Frontend | React 19 + Next.js 15 |
| Backend | FastAPI (Python) |
| Vector DB | Chroma + Pinecone/Weaviate |
| Graph DB | LightRAG (OpenSearch) |


---

## 10. Reference Material Index

### 10.1 Deep Implementation Reference (68 Chapters)

The `reference/how_to_build_a_video_agent_system/` directory contains 68 chapters of detailed implementation guidance:

| Chapters | Likely Coverage |
|----------|----------------|
| 01–10 | System foundations, architecture patterns, agent design |
| 11–20 | Individual agent implementation, tool integration |
| 21–30 | Quality assurance, evaluation, testing patterns |
| 31–40 | Orchestration, state management, message passing |
| 41–50 | Video generation, audio, creative pipelines |
| 51–60 | Delivery, distribution, optimization loops |
| 61–68 | Advanced topics, scaling, future directions |

> **Location:** [reference/how_to_build_a_video_agent_system/](./reference/how_to_build_a_video_agent_system/)

### 10.2 Complete Document Inventory

#### Functional Specifications (English)

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

#### Technical Specifications (English)

| Document | Agent/System | Status |
|----------|-------------|--------|
| [general_creative_agent_technical_specification.md](./general_creative_agent_technical_specification.md) | GCA Implementation | Complete |
| [optimization_agent_technical_specification.md](./optimization_agent_technical_specification.md) | Optimization Agent Architecture | Complete |
| [research_agent_technical_specification.md](./research_agent_technical_specification.md) | Research Agent Redevelopment | Complete |

#### System-Level Documents (English)

| Document | Covers | Status |
|----------|--------|--------|
| [agents.md](./agents.md) | Full 114-agent roster with categories | Complete |
| [ai_agent_video_production_workflow.md](./ai_agent_video_production_workflow.md) | Complete production workflow + runtime architecture | Complete |
| [human_video_production_workflow.md](./human_video_production_workflow.md) | Human baseline (52 crew roles) | Complete |
| [complex_problem_solution_process_model.md](./complex_problem_solution_process_model.md) | WHAT/WHY/HOW/DO/REVIEW methodology | Complete |
| [system_build_plan.md](./system_build_plan.md) | Ultra-detailed implementation plan for building the whole system (target build agent: Claude Code; milestones M0–M12 + 100-point hardening) | Complete |
| [video_generation_techology_should_learn_now.md](./video_generation_techology_should_learn_now.md) | 50 AI video generation models (April 2026) | Complete |
| [lifes_quiet_redemption_agent_workflow.md](./lifes_quiet_redemption_agent_workflow.md) | Worked example: agent-mapped + research-informed short-film workflow (with diagrams) | Complete |

#### Chinese (香港繁體) Translations

All major documents have `_hk.md` counterparts providing Hong Kong Traditional Chinese translations. These follow the same naming pattern (e.g., `agents_hk.md`, `optimization_agent_functional_specification_hk.md`).

### 10.3 Workflow Diagram Gallery — "Life's Quiet Redemption" (Worked Example)

A worked end-to-end example of the system applied to a 60-second cinematic short. The six diagrams below (in [`./workflows/`](./workflows/)) visualize how the 114-agent swarm, the gate ladder, and the 2026 engine/research upgrades come together. Full write-up: [lifes_quiet_redemption_agent_workflow.md](./lifes_quiet_redemption_agent_workflow.md) ([香港繁體](./lifes_quiet_redemption_agent_workflow_hk.md)).

<table>
  <tr>
    <td width="33%" align="center"><a href="./workflows/lqr-pipeline-overview.svg"><img src="./workflows/lqr-pipeline-overview.svg" width="260" alt="6-phase pipeline overview"/></a><br/><b>D1 · Pipeline Overview</b><br/>6-phase DAG, gates, feedback loop</td>
    <td width="33%" align="center"><a href="./workflows/lqr-scene-flow.svg"><img src="./workflows/lqr-scene-flow.svg" width="260" alt="scene flow, emotional arc, retention bands"/></a><br/><b>D2 · Scene Flow</b><br/>Arc, retention bands, per-shot engine</td>
    <td width="33%" align="center"><a href="./workflows/lqr-per-shot-loop.svg"><img src="./workflows/lqr-per-shot-loop.svg" width="260" alt="per-shot generation loop"/></a><br/><b>D3 · Per-Shot Loop</b><br/>3E + visual anchor + VBench + MCTS</td>
  </tr>
  <tr>
    <td width="33%" align="center"><a href="./workflows/lqr-character-consistency.svg"><img src="./workflows/lqr-character-consistency.svg" width="260" alt="character consistency identity stack"/></a><br/><b>D4 · Consistency Stack</b><br/>Identity youth→adult</td>
    <td width="33%" align="center"><a href="./workflows/lqr-engine-routing.svg"><img src="./workflows/lqr-engine-routing.svg" width="260" alt="engine routing tiers"/></a><br/><b>D5 · Engine Routing</b><br/>Grok Imagine + hero engines + cost</td>
    <td width="33%" align="center"><a href="./workflows/lqr-quality-gates.svg"><img src="./workflows/lqr-quality-gates.svg" width="260" alt="quality gate ladder and VBench scorecard"/></a><br/><b>D6 · Quality Gates</b><br/>L1/L2/L3 + VBench scorecard</td>
  </tr>
</table>

> If a thumbnail does not render, click it to open the full SVG. Diagrams follow the same visual language as [common-agent-structure.svg](./common-agent-structure.svg).

---

## 11. Implementation Priority & Dependencies

### 11.1 Foundation Layer (Build First)

These must exist before any production agent can function:

```
1. Agentic RAG System          ← Knowledge backbone for all agents
   └── agentic_rag_functional_specification.md

2. Orchestration Runtime        ← DAG execution, routing, state
   └── agents.md §9 (OrchestratorAgent, PlannerAgent, RouterAgent)

3. Research Agent               ← Knowledge acquisition service
   └── research_agent_functional_specification.md
   └── research_agent_technical_specification.md

4. Coding Agent                 ← Builds all other agents
   └── coding_agent_functional_specification.md

5. LLM Usage Dashboard          ← Cost monitoring from day one
   └── llm_usage_functional_specification.md
```

### 11.2 Intelligence Layer (Build Second)

These provide reasoning capabilities that production agents consume:

```
6. Deep Intent Analysis (DIA)   ← Parses user briefs into structured intents
   └── intent_analysis_agent_functional_specification.md

7. General Creative Agent (GCA) ← Creative ideation engine
   └── general_creative_agent_functional_specification.md
   └── general_creative_agent_technical_specification.md

8. Process Optimization Agent   ← Workflow improvement engine
   └── optimization_agent_functional_specification.md
   └── optimization_agent_technical_specification.md

9. Strategic Goal Achievement   ← Goal clarification for all planning
   └── strategic_goal_achievement_agent_functional_specification.md

10. Complex Problem Solving     ← Diagnostic reasoning framework
    └── complex_problem_solution_process_model.md
```

### 11.3 Production Layer (Build Third)

The 52 core production agents (1–52) from the master roster, activated per workflow type.

### 11.4 Enhancement Layer (Build Fourth)

```
11. Psychological Profiling     ← Personalizes creator/audience modeling
    └── psychological_profile_agent_functional_specifications.md

12. Psychological Recommendation ← Audience preference prediction
    └── psychological_recommendation_agent_functional_specification.md

13. Podcast Agent               ← Audio-first production variant
    └── podcast_agent_functional_specifcation.md
```

### 11.5 Dependency Graph

```
                    ┌─────────────────┐
                    │  Coding Agent   │ ← Builds everything
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
    ┌─────────────┐  ┌─────────────┐  ┌──────────────┐
    │ Agentic RAG │  │ Orchestrator│  │ LLM Dashboard│
    └──────┬──────┘  └──────┬──────┘  └──────────────┘
           │                │
     ┌─────┴─────┐    ┌────┴────┐
     ▼           ▼    ▼         ▼
┌─────────┐ ┌──────┐ ┌──────┐ ┌──────────┐
│Research │ │ DIA  │ │Router│ │ Planner  │
│ Agent   │ │      │ │Agent │ │  Agent   │
└────┬────┘ └──┬───┘ └──┬───┘ └────┬─────┘
     │         │         │          │
     └─────────┴─────────┴──────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │  52 Production Agents (1–52) │
    │  + GCA + Optimization Agent   │
    │  + Goal Framework             │
    │  + Psychological Profiling    │
    └───────────────────────────────┘
```

---

## 12. How to Use This Document

1. **Starting a new implementation?** → Begin with §11 (Priority & Dependencies), then follow the Foundation → Intelligence → Production → Enhancement sequence. For a concrete, step-by-step build (milestones M0–M12, acceptance gates, and a 100-point hardening checklist) targeting the **Claude Code** build agent, follow [system_build_plan.md](./system_build_plan.md).

2. **Need to understand a specific agent?** → Find it in §3 (Agent Categories), then follow the "Deep Specification" link.

3. **Designing a new workflow?** → Check §6 (Workflow Integration) for the pipeline phases and §6.2 for existing workflow variants.

4. **Integrating agents together?** → See §7 (Data Flow & Handoff Contracts) for the shared manifest format and critique bus protocol.

5. **Building the UI?** → See §8 for all UI/communication documents.

6. **Need reference material?** → See §10 for the complete inventory including the 68-chapter deep reference.

---

*Document generated: May 27, 2026*  
*Covers: 114 agents, 12 functional specifications, 3 technical specifications, 10 workflow variants, 68 reference chapters*



## Additional corpus / va passages naming this agent


### From `corpus/study/ai_agent_video_production_workflow.md` Copy: `sources/excerpts/ai_agent_video_production_workflow.md`.


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



### From `corpus/study/lifes_quiet_redemption_agent_workflow.md` Copy: `sources/excerpts/lifes_quiet_redemption_agent_workflow.md`.


### D6 · Quality Gate Ladder & VBench Scorecard
![Quality gate ladder L1 spec, L2 rubric VBench scorecard, L3 audience preference, GateKeeper sign-off](./workflows/lqr-quality-gates.svg)

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

Every artifact clears three layers before GateKeeperAgent advances it (agents.md §11.2).

| Outlet | Aspect / Spec | Owning Agents | Notes |
|---|---|---|---|
| YouTube (main) | 16:9, 1080p/4K, 24–30fps, burned + soft subs | DistributorAgent (#112), ChannelManagerAgent (#108), SEOAgent (#87) | Full ~60s cut |
| YouTube Shorts | 9:16, face-reframed, burned subs | TrailerEditorAgent (#51), RetentionOptimizerAgent (#76) | 3s hook front-loaded |
| Xiaohongshu (RED) | 9:16 / 3:4, ZH subs | SocialMediaStrategistAgent (#28), LocalizationQAAgent (#44) | Culturally-tuned caption + tags |
| Douyin / TikTok | 9:16, trending-audio aware | SocialMediaStrategistAgent (#28), TrendIntelligenceAgent (#68) | Hook-rate ≥30% target |
| Instagram Reels | 9:16, EN + ZH subs | MarketingAgent (#86), SEOAgent (#87) | Bilingual variant |
| Archive master | ProRes + C2PA, checksum | ArchiveMasterAgent (#114), GateKeeperAgent (#57) | Series-reuse preservation package |

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



### From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


```text
M0 Bootstrap ──► M1 RAG ──► M2 Orchestration ──► M3 LLM Gateway+Router+CostDash
                                  │                       │
                                  ▼                       ▼
                          M4 Research+Coding harness   M5 Intelligence (DIA,GCA,Opt,Goal,CPS,Aesthetics)
                                  │                       │
                                  └───────────┬───────────┘
                                              ▼
                                  M6 Agent Factory + VERTICAL SLICE (Workflow A) ◄── proves architecture
                                              ▼
                                  M7 Production agents 1–52 (factory breadth)
                                              ▼
                                  M8 Meta-agents 53–80 + QC mesh + GateKeeper
                                              ▼
                                  M9 Support agents 81–114 + Delivery fabric
                                              ▼
                                  M10 UI (web + gateway + websocket)   ── can start in parallel after M3 via worktree
                                              ▼
                                  M11 Enhancement (psych, podcast, personalization)
                                              ▼
                                  M12 Hardening, scale, security, launch (the §14 100-point pass)
```

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

**Acceptance Gate G-M2:** A hard-coded 3-node DAG (`Planner → echo-agent → GateKeeper`) runs end-to-end on real Temporal+Redis+Postgres, survives a mid-run worker kill, emits correct typed events, and signs artifacts with C2PA. ✅ This is the *walking skeleton*.

**Build:**
- **Orchestration (53–58):** harden Orchestrator/Planner/Router/Judge/GateKeeper/Memory with full dispute-resolution (multi-agent debate), stage-gate sign-off, and escaped-defect=0 discipline.
- **Creative (59–65):** Ideation, NarrativeArc, StyleTransfer, MoodBoard, Novelty/Anti-Cliché, EmotionalArc, WorldBuilding — many delegate to GCA/Aesthetics (no duplication).
- **Research (66–72):** Web/Archive/Trend/Competitor/Citation/InterviewSynthesis/Benchmark — built on the M4 Research Agent core.
- **Optimization (73–80):** Prompt/Cost/Latency/Retention/ROAS/Accessibility optimizers + EvaluationHarness + SafetyRedTeam.
- **Full QC mesh**: complete L3 (AudienceSim ≥200 personas + HiTL sampling) and Q1–Q6 delivery validators; `GateKeeperAgent` enforces "zero leaked defects."

**Tests:** Judge inter-rater agreement κ≥0.8 vs a fixture human-panel; GateKeeper blocks a seeded defect; SafetyRedTeam attack-success ≤1% on the seeded attack set; EvaluationHarness detects an injected regression <1h; AudienceSim L3 win-rate computed on a golden pair.

### 10.4 The non-negotiable release predicate
An artifact is releasable **iff**: `L1==pass AND L2>=85 AND L3>=threshold AND all(Q1..Q6) AND compliance==clear AND c2pa_signed AND budget_ok`. Encode this as a single `qc.release_ok(artifact)` function; the GateKeeperAgent calls only this.

### Theme 4 — Quality Mesh (31–40)
31. `qc.release_ok()` is the single release predicate; GateKeeper calls only it.
32. L1 deterministic validators cover codec/aspect/duration/frame-rate/LUFS/captions.
33. L2 judges are pinned (model+prompt version); score variance within tolerance across reruns.
34. L3 AudienceSim uses ≥200 personas + ≥20 HiTL; win-rate computed correctly.
35. Q1–Q6 delivery mesh each implemented and gating.
36. Continuity (Q4) detects identity/wardrobe/prop drift via `identity_hash`.
37. Aesthetic scoring returns decomposed vector + `hack_likelihood`; low confidence escalates.
38. Reward-hacking defenses active (ensemble disagreement, variance monitoring).
39. Accessibility (WCAG 2.2 AA min) gated for any human-facing output.
40. A seeded defect is reliably caught and blocked before release.



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
| 97 | **LearnerSimAgent** | Simulate
…



### From `corpus/study/ui/architecture_communication.md` Copy: `sources/excerpts/architecture_communication.md`.


```text
USER sees Gate Approval Dialog
    │
    │  Reviews criteria checklist + artifacts
    │  Clicks [✓ APPROVE] or [↩ REQUEST CHANGES]
    │
    ▼
FRONTEND
    │
    │  POST /api/productions/{id}/gates/{gate_id}/decision
    │  Body: { decision: "approve", comment: "...", c2pa_sign: true }
    │
    ▼
API GATEWAY
    │
    │  Validates user permission
    │  Signs C2PA provenance manifest
    │  Publishes "gate_decision" event to Event Bus
    │
    ▼
ORCHESTRATION ENGINE (LangGraph)
    │
    │  GateKeeperAgent receives decision
    │  If approved: advances DAG to next phase
    │  If rejected: routes feedback to relevant agents for revision
    │
    ▼
NEXT PHASE AGENTS activate
    │
    │  (cycle continues)
```



### From `corpus/study/ui/backend_agent_management.md` Copy: `sources/excerpts/backend_agent_management.md`.


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



### From `corpus/study/ui/ui_design.md` Copy: `sources/excerpts/ui_design.md`.


| Principle | Rationale |
|-----------|-----------|
| **Brief-First** | Every production starts from a human brief; UI makes brief-entry the gravity center |
| **Progressive Disclosure** | 114 agents are overwhelming; show only what the current phase needs |
| **Live DAG Visibility** | The Composition Diagram runs in real-time; users must see agent state at a glance |
| **Gate-Driven Confidence** | GateKeeperAgent phase transitions surface as explicit approval moments in the UI |
| **Critique Transparency** | Every agent critique message is viewable, searchable, and actionable |
| **Production-Type Aware** | The 10 workflow templates (A–J) shape which agents activate and which panels appear |

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

**DAG Interactions:**
- Click node → opens Agent Inspector in Detail Drawer
- Double-click node → full-screen Agent Inspector
- Click edge → shows artifact being passed
- Click GateKeeper → opens Gate Approval Dialog
- Right-click node → context menu: Retry, Skip, Inspect, View Critiques
- Drag to pan, scroll to zoom, Ctrl+click to multi-select

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
Step 7: DELIVERY PH
…



## Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


## Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


## Provenance

- Master roster row va_id=57 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `C:\Project\va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.gatekeeper · va_id=57 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **GateKeeperAgent** (`video.gatekeeper`, va_id=57, category `9-Meta`).

### Responsibility focus
Phase transitions; verifies L1/L2/L3 criteria; signs C2PA

### Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: stage-gate quality systems, C2PA provenance, release criteria automation, policy-as-code gates
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI content gates, provenance signing C2PA, automated release QA
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: phase gates in production pipelines, C2PA and content authenticity, automated QC gates

### arXiv / academic integration (role-applied)
- Constitutional AI constitutions as phase-gate criteria
- C2PA / provenance signing for artifact handoff integrity

**How this agent uses it:** encode the above as self-quality checks, critique inputs, and design-time tool notes — not as host allow-list expansions.

### X / industry practice (role-applied)
- Stage-gate methodology in AI production pipelines

### YouTube / practitioner guidance (role-applied)
- QC sign-off flows; never silent phase advance

### Implementation notes for v1
1. Emit artifacts matching role responsibility; self-score against Self-quality criteria.
2. Accept critique only from listed critics; escalate disputes to Judge/Gate as DNA dictates.
3. Design-time tools remain documented only; runtime tools stay in `agent_spec.json`.
4. N1: no second control plane; video logic under `business/video/**` only.

### Research depth note (honest)
This v1 section maps **role-family** literature and the agent’s migration prompt topics into SPEC.
It is **not** a full unsummarized download of every paper/video transcript.
Live primary-source expansion remains a residual for score 100 on S3 where depth is still thin.

<!-- migration_capability_research · video.gatekeeper · v1 · 2026-07-13 -->

### `sources/generic/video.router.SPEC.md`

Omitted here; same document as `SPEC.md` above.

### `sources/MAPPING.md`

# Mapping — `video.router`

- VA/generic pack ID: `video.router`
- Previous common ID: `video.tool_policy_designer`
- SPEC depth: full generic SPEC body + host runtime binding

### `sources/PROVENANCE.json`

```json
{
  "schema_version": "3.0",
  "sources": [
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
      "author": "Aurélien Géron",
      "isbn13": "9781098125974",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Hands-On Machine Learning, 3rd ed. (Aurélien Géron), ISBN-13 9781098125974"
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
      "author": "Manning, Raghavan, Schütze",
      "isbn13": "9780521865715",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Introduction to Information Retrieval (Manning, Raghavan, Schütze), ISBN-13 9780521865715"
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
      "title": "人工智能：一种现代的方法",
      "author": "第4版",
      "isbn13": "9787111547044",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 人工智能：一种现代的方法（第4版），ISBN-13 9787111547044"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "深度学习",
      "author": "花书",
      "isbn13": "9787115461476",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 深度学习（花书），ISBN-13 9787115461476"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "机器学习",
      "author": "周志华",
      "isbn13": "9787302373575",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 机器学习（周志华），ISBN-13 9787302373575"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "统计学习方法",
      "author": "李航",
      "isbn13": "9787302423288",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 统计学习方法（李航），ISBN-13 9787302423288"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "强化学习",
      "author": "第2版",
      "isbn13": "9787115546081",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 强化学习（第2版），ISBN-13 9787115546081"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "信息检索导论",
      "isbn13": "9787115221704",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 信息检索导论，ISBN-13 9787115221704"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "数据密集型应用系统设计",
      "isbn13": "9787111547532",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 数据密集型应用系统设计，ISBN-13 9787111547532"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "超级智能",
      "isbn13": "9787508663098",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 超级智能，ISBN-13 9787508663098"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "生命3.0",
      "isbn13": "9787508684031",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 生命3.0，ISBN-13 9787508684031"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "动手学深度学习",
      "author": "李沐等",
      "isbn13": "9787115547460",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 动手学深度学习（李沐等），ISBN-13 9787115547460"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Mining of Massive Datasets",
      "author": "Leskovec, Rajaraman, Ullman",
      "isbn13": "9781107157873",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Mining of Massive Datasets (Leskovec, Rajaraman, Ullman), ISBN-13 9781107157873"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Recommender Systems Handbook, 2nd ed.",
      "author": "Ricci et al.",
      "isbn13": "9781489976369",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Recommender Systems Handbook, 2nd ed. (Ricci et al.), ISBN-13 9781489976369"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "推荐系统实践",
      "author": "项亮",
      "isbn13": "9787115281708",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 推荐系统实践（项亮），ISBN-13 9787115281708"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "agentic-design-patterns-chinese",
      "isbn13": "9783032014016",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: agentic-design-patterns-chinese, ISBN-13 9783032014016"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "智能体设计指南",
      "author": "云中江树",
      "isbn13": "9787111775843",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 智能体设计指南（云中江树），ISBN-13 9787111775843"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "大模型应用开发：动手做AI Agent",
      "author": "黄佳",
      "isbn13": "9787115642172",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 大模型应用开发：动手做AI Agent（黄佳），ISBN-13 9787115642172"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "构建Agentic AI系统",
      "author": "Anjanava Biswas, Wrick Talukdar",
      "isbn13": "9787302703983",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 构建Agentic AI系统（Anjanava Biswas, Wrick Talukdar），ISBN-13 9787302703983"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building Applications with AI Agents Designing and Implementing Multiagent Systems",
      "isbn13": "9781098176501",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building Applications with AI Agents Designing and Implementing Multiagent Systems, ISBN-13 9781098176501"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "AI Agent开发与应用：基于大模型的智能体构建",
      "author": "凌峰",
      "isbn13": "9787302685975",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: AI Agent开发与应用：基于大模型的智能体构建（凌峰），ISBN-13 9787302685975"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "AI Agents in Action",
      "author": "Micheal Lanham",
      "isbn13": "9781633436343",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: AI Agents in Action (Micheal Lanham), ISBN-13 9781633436343"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "AI Engineering Building Applications with Foundation Models",
      "author": "Chip Huyen",
      "isbn13": "9781098166304",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: AI Engineering Building Applications with Foundation Models (Chip Huyen), ISBN-13 9781098166304"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "从零开始构建大型语言模型Build a Large Language Model (From Scratch)",
      "author": "SEBASTIAN RASCHKA",
      "isbn13": "9781633437166",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 从零开始构建大型语言模型Build a Large Language Model (From Scratch)（SEBASTIAN RASCHKA），ISBN-13 9781633437166"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building AI Agent Platforms (for Isabel Garcia)",
      "author": "Ben OMahony and Fabian Nonnenmacher",
      "isbn13": "9798341666344",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building AI Agent Platforms (for Isabel Garcia) (Ben OMahony and Fabian Nonnenmacher), ISBN-13 9798341666344"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "大模型项目实战 多领域智能应用开发",
      "author": "高强文",
      "isbn13": "9787111762348",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 大模型项目实战 多领域智能应用开发（高强文），ISBN-13 9787111762348"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "LLM Engineer’s Handbook",
      "author": "Paul Iusztin ,Maxime Labonne",
      "isbn13": "9781836200079",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: LLM Engineer’s Handbook (Paul Iusztin ,Maxime Labonne), ISBN-13 9781836200079"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "An Illustrated Guide to AI Agents",
      "isbn13": "9798341662681",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: An Illustrated Guide to AI Agents, ISBN-13 9798341662681"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Managing Memory for AI Agents",
      "isbn13": "9798341661257",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Managing Memory for AI Agents, ISBN-13 9798341661257"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Patterns for Building AI Agents",
      "author": "SAM BHAGWATMICHELLE GIENOW",
      "isbn13": "9798270198107",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Patterns for Building AI Agents (SAM BHAGWATMICHELLE GIENOW), ISBN-13 9798270198107"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "AI Agents with MCP (First Early Release)",
      "author": "Kyle Stratis",
      "isbn13": "9798341639508",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: AI Agents with MCP (First Early Release) (Kyle Stratis), ISBN-13 9798341639508"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Build a Multi-Agent System (from Scratch) With MCP and A2A",
      "author": "Val Andrei Fajardo",
      "isbn13": "9781633434660",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Build a Multi-Agent System (from Scratch) With MCP and A2A (Val Andrei Fajardo), ISBN-13 9781633434660"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building Generative AI Agents. Using LangGraph, AutoGen, and CrewAI 2025",
      "author": "Tom Taulli, Gaurav Deshmukh",
      "isbn13": "9798868811340",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building Generative AI Agents. Using LangGraph, AutoGen, and CrewAI 2025 (Tom Taulli, Gaurav Deshmukh), ISBN-13 9798868811340"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Ultimate Agentic AI with AutoGen for Enterprise Automation",
      "author": "Shekhar Agrawal, Srinivasa Sunil Chippada etc.",
      "isbn13": "9789349888951",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Ultimate Agentic AI with AutoGen for Enterprise Automation (Shekhar Agrawal, Srinivasa Sunil Chippada etc.), ISBN-13 9789349888951"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "从零构建大模型算法、训练与微调",
      "isbn13": "9787302685616",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 从零构建大模型算法、训练与微调，ISBN-13 9787302685616"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "多模态大模型 从理论到实践",
      "isbn13": "9787302686927",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 多模态大模型 从理论到实践，ISBN-13 9787302686927"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "AutoGPT Revolutionizing Automation with Generative AI",
      "author": "Kameron Hussain, Frahaan Hussain",
      "isbn13": "9798224989805",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: AutoGPT Revolutionizing Automation with Generative AI (Kameron Hussain, Frahaan Hussain), ISBN-13 9798224989805"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "这就是MCP",
      "author": "艾逗笔",
      "isbn13": "9787115677471",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 这就是MCP（艾逗笔），ISBN-13 9787115677471"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building Multimodal Generative AI and Agentic Applications Shaping concept to code for…",
      "isbn13": "9789365898385",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building Multimodal Generative AI and Agentic Applications Shaping concept to code for…, ISBN-13 9789365898385"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Agentic Architectural Patterns for Building Multi-Agent Systems",
      "isbn13": "9781806029570",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Agentic Architectural Patterns for Building Multi-Agent Systems, ISBN-13 9781806029570"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Agentic Mesh",
      "isbn13": "9798341621619",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Agentic Mesh, ISBN-13 9798341621619"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building LLM Agents with RAG, Knowledge Graphs, and Reflection",
      "isbn13": "9798232017378",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building LLM Agents with RAG, Knowledge Graphs, and Reflection, ISBN-13 9798232017378"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "MCP协议与AI Agent开发：标准、应用与实现",
      "isbn13": "9787302695349",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: MCP协议与AI Agent开发：标准、应用与实现，ISBN-13 9787302695349"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "MCP协议与大模型集成实战",
      "isbn13": "9787121503863",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: MCP协议与大模型集成实战，ISBN-13 9787121503863"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangChain核心技术与LLM项目实践",
      "author": "凌峰",
      "isbn13": "9787302685630",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangChain核心技术与LLM项目实践（凌峰），ISBN-13 9787302685630"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangChain 入门指南构建高可复用、可扩展的 LLM 应用程序",
      "author": "李特丽",
      "isbn13": "9787121467271",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangChain 入门指南构建高可复用、可扩展的 LLM 应用程序（李特丽），ISBN-13 9787121467271"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "AI Agents and Applications (MEAP, all 14 chapters) With LangChain, LangGraph, and MCP",
      "author": "Roberto Infante",
      "isbn13": "9781633436541",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: AI Agents and Applications (MEAP, all 14 chapters) With LangChain, LangGraph, and MCP (Roberto Infante), ISBN-13 9781633436541"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Learning LangChain Building AI and LLM Applications with LangChain and LangGraph",
      "author": "Mayo Oshin, Nuno Campos",
      "isbn13": "9781098167288",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Learning LangChain Building AI and LLM Applications with LangChain and LangGraph (Mayo Oshin, Nuno Campos), ISBN-13 9781098167288"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "大模型RAG实战：RAG原理、应用与系统构建",
      "author": "汪鹏, 谷清水, 卞龙鹏",
      "isbn13": "9787111761990",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 大模型RAG实战：RAG原理、应用与系统构建（汪鹏, 谷清水, 卞龙鹏），ISBN-13 9787111761990"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Building Natural Language and LLM Pipelines Build production-grade RAG, tool contracts,…",
      "author": "Laura Funderburk",
      "isbn13": "9781835467008",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Building Natural Language and LLM Pipelines Build production-grade RAG, tool contracts,… (Laura Funderburk), ISBN-13 9781835467008"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "多模态大模型 算法、应用与微调",
      "author": "刘兆峰",
      "isbn13": "9787111754886",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 多模态大模型 算法、应用与微调（刘兆峰），ISBN-13 9787111754886"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "AI Agent AI的下一个风口 智能体的核心技术讲解书籍 大模型时代的AI介绍书",
      "isbn13": "9787121474606",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: AI Agent AI的下一个风口 智能体的核心技术讲解书籍 大模型时代的AI介绍书，ISBN-13 9787121474606"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "官方正版 LangChain实战 从原型到生产 动手打造 LLM 应用",
      "isbn13": "9787121475450",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 官方正版 LangChain实战 从原型到生产 动手打造 LLM 应用，ISBN-13 9787121475450"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "正版包邮 LangChain编程 从入门到实践",
      "isbn13": "9787115639424",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 正版包邮 LangChain编程 从入门到实践，ISBN-13 9787115639424"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LLM串接所有服務：LangChain原型到產品全面開發",
      "isbn13": "9786267383919",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LLM串接所有服務：LangChain原型到產品全面開發，ISBN-13 9786267383919"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "極速ChatGPT開發者兵器指南：跨界整合Prompt Flow、LangChain與Semantic Kernel框架",
      "isbn13": "9786263338203",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 極速ChatGPT開發者兵器指南：跨界整合Prompt Flow、LangChain與Semantic Kernel框架，ISBN-13 9786263338203"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "生成式AI实战基于Transformer、Stable Diffusion、LangChain和AI Agent",
      "isbn13": "9787115650443",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 生成式AI实战基于Transformer、Stable Diffusion、LangChain和AI Agent，ISBN-13 9787115650443"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangChain技术解密 构建大模型应用的全景指南 王浩帆",
      "isbn13": "9787121477379",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangChain技术解密 构建大模型应用的全景指南 王浩帆，ISBN-13 9787121477379"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangChain大模型AI应用开发实践",
      "isbn13": "9787302672524",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangChain大模型AI应用开发实践，ISBN-13 9787302672524"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "AI Agent应用与项目实战",
      "isbn13": "9787121491818",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: AI Agent应用与项目实战，ISBN-13 9787121491818"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "一本书读懂AI Agent：技术、应用与商业",
      "isbn13": "9787111764168",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 一本书读懂AI Agent：技术、应用与商业，ISBN-13 9787111764168"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "大模型项目实战Agent开发与应用",
      "isbn13": "9787111777335",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 大模型项目实战Agent开发与应用，ISBN-13 9787111777335"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "MCP开发从入门到实战：人工智能AI智能体Agent应用开发",
      "isbn13": "9787115674142",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: MCP开发从入门到实战：人工智能AI智能体Agent应用开发，ISBN-13 9787115674142"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "AI Agent设计实战：智能体设计方法与技巧",
      "isbn13": "9787111779247",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: AI Agent设计实战：智能体设计方法与技巧，ISBN-13 9787111779247"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "MCP极简开发：轻松打造高效智能体 MCP开发教程 Agent智能体大语",
      "isbn13": "9787115674883",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: MCP极简开发：轻松打造高效智能体 MCP开发教程 Agent智能体大语，ISBN-13 9787115674883"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "A2A協議：多Agent系統全鏈路開發",
      "isbn13": "9787111791980",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: A2A協議：多Agent系統全鏈路開發，ISBN-13 9787111791980"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangGraph實戰──構建新一代 AI 智慧體系統",
      "isbn13": "9787121507007",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangGraph實戰──構建新一代 AI 智慧體系統，ISBN-13 9787121507007"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "MCP+A2A+LangGraph 驅動的智能體全流程開發",
      "isbn13": "9787115682024",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: MCP+A2A+LangGraph 驅動的智能體全流程開發，ISBN-13 9787115682024"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "大模型应用开发：RAG入门与实战 大语言模型大模型多模态Prompt提示词工程RAG检索增强生成技术",
      "isbn13": "9787115648938",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 大模型应用开发：RAG入门与实战 大语言模型大模型多模态Prompt提示词工程RAG检索增强生成技术，ISBN-13 9787115648938"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LangChain開發手冊：OpenAI × LCEL 表達式 × Agent 自動化流程 × RAG 擴展模型知識 × 圖形資料庫 × LangSmith 除錯工具",
      "isbn13": "9789863127918",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LangChain開發手冊：OpenAI × LCEL 表達式 × Agent 自動化流程 × RAG 擴展模型知識 × 圖形資料庫 × LangSmith 除錯工具，ISBN-13 9789863127918"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "大模型RAG应用开发：构建智能生成系统",
      "isbn13": "9787302685982",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 大模型RAG应用开发：构建智能生成系统，ISBN-13 9787302685982"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "LlamaIndex大模型RAG开发实践",
      "isbn13": "9787302697084",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: LlamaIndex大模型RAG开发实践，ISBN-13 9787302697084"
    }
  ],
  "agent_id": "video.router",
  "previous_common_agent_id": "video.tool_policy_designer",
  "va_taxonomy_aligned": true,
  "generic_source": "generic-swarm-ops/business/video/agents/video.router",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "aligned_at": "2026-07-27T00:48:10.977434Z",
  "generic_source_depth": {
    "excerpts": true,
    "study": true,
    "adopted_at": "2026-07-27T01:30:28.745149+00:00",
    "upstream": "generic-swarm-ops/business/video/agents"
  },
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\video\\agents\\video.router",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```

### `sources/RETHINK_100_APPLIED.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.router",
  "source_doc": "business/video/corpus/study/ui/RETHINK_100_IMPROVEMENTS.md",
  "applied_at": "2026-07-31T06:22:31Z",
  "item_ids": [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    14,
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
    89,
    93,
    94
  ],
  "item_titles": {
    "1": "Seedance 2.0 multi-input / first-last frame",
    "2": "Wan 2.6 IP-anchored character consistency",
    "3": "Vidu Q2/Q3 temporal consistency",
    "4": "Grok Imagine Video I2V",
    "5": "Hailuo 2.3 budget-tier generation",
    "6": "Kling variant awareness",
    "7": "Seedance multi-camera awareness",
    "8": "Flux image-gen awareness",
    "9": "SD self-hosted cost path awareness",
    "10": "Model strengths matrix (router)",
    "11": "Multi-model ensemble generation",
    "14": "Native audio generation awareness",
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
    "89": "Cross-model quality normalization",
    "93": "Ethical review automation",
    "94": "Provenance chain visualization"
  },
  "design_time_models": [
    "Seedance 2.0 (design-time only)",
    "Wan 2.6 (design-time only)",
    "Vidu Q2/Q3 (design-time only)",
    "Grok Imagine Video (design-time only)",
    "Hailuo 2.3 (design-time only)",
    "Kling 2.6/3.0 variants (design-time only)",
    "Seedance multi-camera (design-time only)",
    "Flux 1.1 Pro Ultra (design-time only)",
    "SD 3.5 self-hosted path (design-time only)"
  ],
  "obligations": [
    "Host control plane owns orchestration; this agent never opens a second control plane.",
    "Runtime tools remain agent_spec.allowed_tools only; RETHINK model names are design-time.",
    "Fail closed when tools/providers are unavailable (circuit-breaker posture).",
    "Prefer iterative verify → refine ≤ max_refinement_count → HiTL over silent pass.",
    "Emit plain-English reasoning summary in artifacts for operator trust.",
    "Attach provenance / correlation_id / evidence_refs on every handoff.",
    "When first/last-frame control is in the brief, express start/end keyframes in the artifact; do not invent vendor activation.",
    "Verify intermediate narrative/script artifacts before advancing downstream handoffs.",
    "Maintain a design-time model strengths matrix (quality, cost, latency, consistency); host routing remains authoritative.",
    "Escalate stereotype/harm/consent risks to ethics/trust-safety/legal gates.",
    "Track A/V sync and native-audio implications; do not assume silent video when audio is native.",
    "When ensemble is requested, propose multi-model candidates + selection criterion; host executes tools."
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
  "agent_id": "video.router",
  "sources": [
    {
      "id": "src_1",
      "title": "Agent-capability registry",
      "description": "Agent-capability registry",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.router",
      "status": "planned_or_partial"
    },
    {
      "id": "src_2",
      "title": "benchmark history (cost/quality/latency)",
      "description": "benchmark history (cost/quality/latency)",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.router",
      "status": "planned_or_partial"
    }
  ],
  "note": "Legal review required before treating external corpora as production grounding."
}
```

### `sources/study/agent_loop_v3.md`

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
| **Cynefin Framework** (1 / 10) | Phase 0 (post-spec) + Phase 1 entry/replan decision | Classify task context: Simple (clear cause-effect) / Complicated (expert analysis) / Complex (emergent) / Chaotic (crisis). Dynamically configure loop params: Fast Recognition Path enabled + lighter gates for Simple/Complicated; Full deliberative + heavy reflection/critics + deeper diagnostics for Complex/Chaotic. | Enables adaptive loop intensity (Fast vs Full) — highest-leverage addition for efficiency + reliabilit

…(clipped 44163 characters from `agent_loop_v3.md`)

### `sources/study/knowledge_router_agent.md`

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
    "suggested_impro

…(clipped 10368 characters from `knowledge_router_agent.md`)

### `sources/study/llm_usage_functional_specification.md`

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

### `sources/study/SYSTEM_REFERENCE.md`

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
