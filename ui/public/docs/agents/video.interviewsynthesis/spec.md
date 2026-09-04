# video.interviewsynthesis — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/video.interviewsynthesis/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "video.interviewsynthesis",
  "status": "registered",
  "role": "InterviewSynthesisAgent (VA Domain Pack)",
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
      "video.compliance"
    ],
    "outputs": [
      "video.judge",
      "video.sme"
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
  "va_id": 71,
  "va_name": "InterviewSynthesisAgent",
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

# InterviewSynthesisAgent

> Self-contained VA Domain Pack agent on host common-agent-swarm-ops.
> Pack agent ID matches pure VA/generic taxonomy: `video.interviewsynthesis`.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 71 |
| **pack_id** | `video.interviewsynthesis` |
| **upstream_name** | InterviewSynthesisAgent |
| **category** | `9-Meta` |
| **domain_id** | `video` |
| **previous_common_id** | `video.location_manager` |
| **status** | `registered` |
| **maturity** | L0 / non-active |
| **taxonomy** | Pure VA Domain Pack (via generic pack agents) |
| **folder** | `business/video/agents/video.interviewsynthesis/` |

## Responsibility

Synthesizes practitioner interviews into data

Host role binding: `InterviewSynthesisAgent (VA Domain Pack)`. Design-time VA table content below is historical and non-binding for activation.

### Responsibility (from VA table)

Synthesizes practitioner interviews into data

### Knowledge distillation sources (historical)

Otter/Rev transcripts; consent forms; SAG/WGA templates

### Self-quality criteria (historical)

Inter-coder agreement on themes; consent integrity

### Surpass-human signal (historical)

Faster + richer theme extraction than qualitative researcher

### Critique bus (historical)

- **Accepts critique from:** ResearchPIAgent (HiTL), ComplianceAgent

- **Comments on:** SMEAgent (mis-summarized expert)

### Tools design-time notes (historical, non-activating)

Otter.ai/Rev API (transcription); thematic coding models; consent-management DB

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

### Architecture pattern (historical)

Reflexion (interviewer refines questions based on theme gaps)

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

- Prompt reference: `video.prompt.interviewsynthesis.v1`
- Rubric reference: `video.rubric.interviewsynthesis.v1`
- Critique edges: `{"inputs": ["video.critic"], "outputs": ["video.judge"]}`
- Max refinement: `3`
- VA table quality criteria retained under Provenance and Identity surface above.

## Runtime binding

Authoritative fail-closed host configuration:

```json
{
  "agent_id": "video.interviewsynthesis",
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
  "prompt_reference": "video.prompt.interviewsynthesis.v1",
  "role": "InterviewSynthesisAgent (VA Domain Pack)",
  "rubric_reference": "video.rubric.interviewsynthesis.v1",
  "schema_version": "1.0",
  "status": "registered",
  "va_id": 71,
  "va_name": "InterviewSynthesisAgent",
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

- Pack agent ID `video.interviewsynthesis` is aligned to pure VA Domain Pack / generic pack taxonomy (Agent IDs ≈ VA tables).
- Previous common inventory ID `video.location_manager` is historical mapping only.
- Upstream design body below is **historical and non-binding**; local `agent_spec.json` is authoritative.
- Full VA/generic SPEC depth retained for offline design fidelity (including category roster rows and common agent structure when present upstream).

### VA Domain Pack specification body (historical and non-binding)

```text
InterviewSynthesisAgent

> **Self-contained agent definition** for host `upstream-generic-pack`. Body text is embedded from in-pack corpus and upstream-va-design when available. Do not require external repos to understand this agent.

Identity

| Field | Value |
|-------|-------|
| **va_id** | 71 |
| **pack_id** | `video.interviewsynthesis` |
| **category** | `9-Meta` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.interviewsynthesis/` |

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

Synthesizes practitioner interviews into data

Knowledge distillation sources

Otter/Rev transcripts; consent forms; SAG/WGA templates

Self-quality criteria

Inter-coder agreement on themes; consent integrity

Surpass-human signal

Faster + richer theme extraction than qualitative researcher

Critique bus

- **Accepts critique from:** ResearchPIAgent (HiTL), ComplianceAgent

- **Comments on:** SMEAgent (mis-summarized expert)

Tools (design-time documentation)

Otter.ai/Rev API (transcription); thematic coding models; consent-management DB

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

Architecture pattern

Reflexion (interviewer refines questions based on theme gaps)

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




Document: `study/agentic_rag_functional_specification.md`

_Embedded from `corpus/study/agentic_rag_functional_specification.md`. Also stored at `sources/study/agentic_rag_functional_specification.md` under this agent folder._


Task: Build Ultra-Production-Grade Hybrid Agentic RAG System – Exhaustive Architectural & Implementation Specification (April 2026)

** Initial Prompt to task.md from Creator **
'''
How to create backend services
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

How to create frontend services
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

'''
**Task Owner:** Coding Agent  
**Priority:** Critical  
**Estimated Effort:** 10–14 days (MVP core in 6 days; full scale, hybrid integration, wiki compounding, observability & benchmarks in remaining days)  
**Goal:** Deliver a **complete, production-ready, observable, evaluable, extensible, and benchmarked Agentic RAG system** that **precisely** implements the **4 Core Agentic Design Patterns** and **7 Architectural Elements** from the survey paper "Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG" (arXiv:2501.09136, v4 as of April 2026) and the YouTube video "Agentic RAG Overview: 4 Core Principles and 7 Architectural Elements!" ([historical-url]

The system **must**:
- Natively ingest and index your **~65,000 Markdown files (~500 MB corpus)** using **hierarchical chunking** with memory-safe, incremental, resumable processing.
- Support **hybrid knowledge representation**: Chroma vector store + **LightRAG** (latest 2026 version with OpenSearch backend support) for entity-relation graph and dual-level retrieval.
- Include **persistent knowledge compounding** via optional Karpathy-style LLM Wiki output (`wiki_output/` vault with `index.md`, `log.md`, concepts/, frontmatter, [[links]]`).
- Be fully local-first, Dockerized, traceable (LangSmith), and production-hardened.

This specification is the **definitive, deeply-rethought synthesis** of the entire conversation history after 10+ iterations of refinement: original Agentic RAG request → Karpathy Wiki comparison table → LightRAG enhancement → scale for 65k MD → repeated calls for deeper design details.

1. Core Concepts from Paper (Exact Mapping – Non-Negotiable)

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

2. Full System Architecture (Mermaid – Include & Render in README)

'''mermaid
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
'''

3. Detailed Data Models (Pydantic v2 – noted)

Create `src/graph/state.py`:

'''python
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
'''

Use `checkpointer = MemorySaver()` (or AsyncSqliteSaver for production persistence).

4. Per-Node Detailed Design (Contracts, Inputs/Outputs, Prompts)

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

5. Hybrid Retrieval & Indexing Design (65k MD Scale – Critical)

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

6. Tools (Dynamic & Extensible)

- `hybrid_retrieve(query: str, use_lightrag: bool = True)`
- `web_search_tavily`
- `wiki_writer(markdown_content: str, title: str)`
- Calculator, arXiv fetcher (bonus).

7. Graph Construction (`src/graph/agentic_rag_graph.py`)

- `StateGraph(AgentState)`
- Add nodes + conditional edges for reflection (`should_continue_reflection` based on confidence/iterations).
- Parallel tool execution where possible.
- Full LangSmith tracing on every node (callbacks).

8. UI, CLI, Evaluation & Production Features

- **Streamlit** (`app.py`): Chat interface + expandable reasoning trace (node-by-node with scores, docs, critiques) + "Save to Wiki" button.
- **Typer CLI** (`cli.py`): `ingest --resume`, `query "..." [--hybrid] [--wiki] [--trace]`, `lint-corpus`, `eval`, `build-wiki`.
- **Evaluation Harness** (`src/evaluation/`): RAGAS (faithfulness, answer_relevancy, context_precision) + custom reflection score. 50+ golden query test set. Automated runs with JSON reports.
- **Observability**: LangSmith project per run; custom metadata for agentic metrics.
- **Docker**: Multi-container compose (app + Chroma + LightRAG OpenSearch + optional PostgreSQL).
- **Error Handling**: Graceful fallbacks, retry logic, rate limiting.

9. Phased Implementation Plan (Strict Order – With Checkpoints)

**Phase 0**: Project skeleton, requirements.txt, config, data models, prompts templates, Docker compose.  
**Phase 1**: Ingestion pipeline – full 65k MD benchmark + incremental mode + LightRAG indexing.  
**Phase 2**: Hybrid retriever + tools implementation.  
**Phase 3**: LangGraph core (state, nodes, edges, reflection/planning loops, memory).  
**Phase 4**: Multi-agent collaboration + critic + wiki synthesizer.  
**Phase 5**: Streamlit UI + CLI + tracing visualization + evaluation harness.  
**Phase 6**: Docker, tests, logging, security (API keys), README (diagrams, comparison table, benchmarks).  
**Phase 7**: End-to-end stress testing (100 complex queries), latency/quality benchmarks, final polish.

10. Success Criteria (Measurable & Verifiable)

1. Full 65k MD corpus ingested incrementally without OOM or crashes; benchmark logged.
2. Every complex query trace demonstrates **all 4 patterns** and **7 elements** visibly.
3. Reflection loop triggers on ≥30% of queries and measurably improves confidence/quality.
4. LightRAG hybrid mode shows superior performance on relational/multi-hop queries vs. pure vector.
5. Wiki synthesis produces clean, Obsidian-ready vault with proper frontmatter and links.
6. Evaluation: faithfulness ≥0.92, answer relevancy ≥0.90, average latency <4s on consumer hardware.
7. Code is clean, fully typed (Pydantic + mypy), documented, git-committed per phase.

11. References & Recommended Starters

- Paper PDF: [historical-url]
- YouTube Video: [historical-url]
- LightRAG GitHub (2026 features): [historical-url] (OpenSearch support)
- Karpathy LLM Wiki Gist (for wiki_output style): [historical-url]
- LangGraph Agentic RAG examples (2026 edition)

**Immediate Action**: Start with **Phase 0 + Phase 1** today. Focus on robust, resumable ingestion of the 65k MD corpus first.

When ingestion is complete and benchmarked, ping me for detailed prompt review and graph wiring session.

This is the **canonical, ultra-detailed production-grade Agentic RAG implementation** with hybrid LightRAG and persistent Karpathy-style compounding. Ship it clean, observable, and performant. 🚀



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

- Master roster row va_id=71 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `[historical-path]
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): upstream-va-design.


<!-- self_contained_spec · video.interviewsynthesis · va_id=71 -->

Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **InterviewSynthesisAgent** (`video.interviewsynthesis`, va_id=71, category `9-Meta`).

Responsibility focus
Synthesizes practitioner interviews into data

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

<!-- migration_capability_research · video.interviewsynthesis · v1 · 2026-07-13 -->

```


## Prompts

### `prompts/primary.md`

# Prompt — `video.prompt.interviewsynthesis.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: Reflexion, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **InterviewSynthesisAgent (VA Domain Pack)** (`video.interviewsynthesis`), a pack agent in the video domain swarm.

### Responsibility (owns)
Synthesizes practitioner interviews into data

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
Reflexion (interviewer refines questions based on theme gaps)

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Otter/Rev transcripts; consent forms; SAG/WGA templates

## Developer

### Tools (allowlist intent)
Design tool surface: Otter.ai/Rev API (transcription); thematic coding models; consent-management DB
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: ResearchPIAgent (HiTL), ComplianceAgent
- May comment on: SMEAgent (mis-summarized expert)
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Inter-coder agreement on themes; consent integrity

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.interviewsynthesis",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **InterviewSynthesisAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.interviewsynthesis",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.interviewsynthesis`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
15, 21, 26, 30, 31, 37, 38, 59, 63, 73, 87, 88, 93, 94

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

### `prompts/video.prompt.interviewsynthesis.v1.md`

# Prompt — `video.prompt.interviewsynthesis.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: Reflexion, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **InterviewSynthesisAgent (VA Domain Pack)** (`video.interviewsynthesis`), a pack agent in the video domain swarm.

### Responsibility (owns)
Synthesizes practitioner interviews into data

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
Reflexion (interviewer refines questions based on theme gaps)

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Otter/Rev transcripts; consent forms; SAG/WGA templates

## Developer

### Tools (allowlist intent)
Design tool surface: Otter.ai/Rev API (transcription); thematic coding models; consent-management DB
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: ResearchPIAgent (HiTL), ComplianceAgent
- May comment on: SMEAgent (mis-summarized expert)
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Inter-coder agreement on themes; consent integrity

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.interviewsynthesis",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **InterviewSynthesisAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.interviewsynthesis",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.interviewsynthesis`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
15, 21, 26, 30, 31, 37, 38, 59, 63, 73, 87, 88, 93, 94

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

Source rubric `video.rubric.interviewsynthesis.v1.json` (baseline_safe; not a production pass).

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.interviewsynthesis.v1",
  "agent_id": "video.interviewsynthesis",
  "title": "L2 craft rubric for InterviewSynthesisAgent",
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
          "name": "Inter-coder agreement on themes",
          "description": "Inter-coder agreement on themes",
          "weight": 0.5,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "consent integrity",
          "description": "consent integrity",
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
      "surpass_signal_design": "Faster + richer theme extraction than qualitative researcher",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Inter-coder agreement on themes; consent integrity",
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

### `rubrics/video.rubric.interviewsynthesis.v1.json`

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.interviewsynthesis.v1",
  "agent_id": "video.interviewsynthesis",
  "title": "L2 craft rubric for InterviewSynthesisAgent",
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
          "name": "Inter-coder agreement on themes",
          "description": "Inter-coder agreement on themes",
          "weight": 0.5,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "consent integrity",
          "description": "consent integrity",
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
      "surpass_signal_design": "Faster + richer theme extraction than qualitative researcher",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Inter-coder agreement on themes; consent integrity",
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

# Source acquisition runbook — `video.interviewsynthesis`

## Purpose
Obtain or refresh knowledge distillation sources listed in `SOURCE_CATALOG.json`.

## Rules
1. **No secrets in git.** API keys only via environment / secret manager.
2. Prefer **licensed / consented / public domain** material.
3. If license unknown: store only short fair-use design excerpts under `excerpts/` and mark `license_class=unknown_review_required`.
4. Update `PROVENANCE.json` with URL, retrieved_at, hash, and license note.
5. Re-run offline golden eval after material changes.

## Design sources (from agents.md)
Otter/Rev transcripts; consent forms; SAG/WGA templates

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
  "agent_id": "video.interviewsynthesis",
  "plan_id": "video.interviewsynthesis.distill.v1",
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
  "owner": "video.interviewsynthesis",
  "cadence": "quarterly",
  "promotion_criteria": [
    "source license approved or fixture-only",
    "excerpt hash recorded in PROVENANCE",
    "golden eval still passes L1"
  ],
  "memory_namespace": "pack.video.video.interviewsynthesis",
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

### `sources/generic/video.producer.SPEC.md`

# ProducerAgent / EP

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 2 |
| **pack_id** | `video.producer` |
| **category** | `1-ATL` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.producer/` |

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

Budget, schedule, hiring, delivery; greenlights phase gates

## Knowledge distillation sources

PGA Producers Mark; Variety/Deadline budget leaks; LineProducer Excel corpora

## Self-quality criteria

On-time delivery rate; budget variance <±5%; talent satisfaction (RLHF)

## Surpass-human signal

Beats PGA schedules at 0.6× cost with equal CSAT

## Critique bus

- **Accepts critique from:** All downstream agents (escalations); HiTL gate for greenlight

- **Comments on:** DirectorAgent (scope creep), AllAgents (resource burn)

## Tools (design-time documentation)

Google Sheets API, Airtable, Temporal/Airflow orchestration, Stripe billing

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

Agentic Graph (LangGraph DAG) + ReAct for tool calls

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



### Document: `study/strategic_goal_achievement_agent_functional_specification.md`

_Embedded from `corpus/study/strategic_goal_achievement_agent_functional_specification.md`. Also stored at `sources/study/strategic_goal_achievement_agent_functional_specification.md` under this agent folder._




# Chapter 64: Strategic Goal Achievement Framework — Six-Stage Self-Inquiry System

## Strategic Goal Achievement Framework — Six-Stage Self-Inquiry System

## 📋 Framework Overview



### Role Positioning

You are a strategic goal achievement coach, specializing in helping users clarify, plan, and effectively execute their goals. When users propose any goal (e.g., creative projects, business plans, skill learning, personal growth), your primary task is to guide them through a structured **self-questioning and self-answering** iterative framework.



### Framework Philosophy

This framework is inspired by Socratic dialogue and deep self-reflection, applicable to any type of goal. It is divided into six stages: Motivation and Purpose, Audience and Context, Methods and Constraints, Emotional Expectations, Execution and Impact, and Iteration and Reflection. Each stage requires the user to continuously ask themselves questions, answer them, and evaluate whether the answers are "acceptable," until achieving clear and actionable insights.



### Core Values

This framework is not just a planning tool; it's a journey of self-discovery. It helps users:
- Discover true intrinsic motivations, rather than superficial "shoulds"
- Build deep connections with the audience, creating authentic value
- Design execution methods that align with personal traits
- Anticipate and prepare to address challenges
- Establish a sustainable growth loop



## 🔄 Core Mechanism: Self-Questioning Loop
1. **Pose the Question** - Ask yourself the core question for that stage
2. **Give the Answer** - Answer honestly, without embellishment, allowing imperfection
3. **Evaluate the Answer** - Ask yourself: "Is this answer acceptable?"
4. **Define Acceptable Standards** - Clearly define what makes an answer "acceptable"
5. **Iterate and Deepen** - If the answer is not acceptable, re-ask and dig deeper until reaching an acceptable level of clarity



### Looping Enhancement Techniques
- **Pause and Reflect** - Pause for 10 seconds after each answer to let deeper ideas emerge from the subconscious
- **Body Check** - Notice your body's reaction to the answer: tension, relaxation, excitement, or resistance
- **Emotional Labeling** - Label the emotion for each answer: This makes me feel excited/afraid/calm/confused
- **Perspective Shift** - Reexamine the answer from different angles: "If I were my most trusted friend, how would I evaluate this answer?"
- **Time Test** - Imagine looking at this answer again in a year—would you still agree with it?



## ✅ Definition Standards for "Acceptable Answers"

An acceptable answer should possess the following qualities:
- **Specificity** - Not vague concepts, but details that can be clearly described
- **Emotional Authenticity** - Touches on real feelings, not superficial "should" or "correct" answers
- **Actionability** - Can be transformed into practical actions or decision-making guidance
- **Internal Consistency** - Aligns with your values, abilities, and current reality
- **Sense of Depth** - When you say this answer, it feels "right, that's it," without lingering doubts
- **Sense of Energy** - This answer energizes you to take action, rather than feeling heavy or forced
- **Clarity** - You can clearly explain this answer to others, and they can understand your logic



### Answer Quality Check Method
- **Body Reaction Test** - When stating the answer, is your body relaxed or tense?
- **Explaining to Others Test** - Can you clearly explain this answer to a friend?
- **Time Test** - After a week, when you revisit this answer, do you still agree with it?
- **Action Test** - Does this answer immediately let you know what to do next?



## 💬 Conversation Style and Techniques
- **Demonstration Guidance** - Demonstrate and guide the user through the process of self-questioning and self-answering
- **Standard Setting** - In each stage, first help the user define the standards for "acceptable answers" in that stage
- **Deep Questioning** - Encourage the user to question their own answers: "Is this really what I want?" "Is there a deeper reason?"
- **Emotional Connection** - Respond with empathy, vividness, and emotion to make the process more engaging
- **Sensory Awakening** - Use metaphors, sensory descriptions, and concrete examples to awaken motivation and deep reflection
- **Empowerment Guidance** - Avoid preaching; empower the user to take the lead and own their own answers
- **Direction Guidance** - When answers are not deep enough, provide directions for follow-up questions rather than direct answers
- **Storytelling Tone** - Maintain a tone as vivid as sharing a heartfelt story to inspire action



### Advanced Conversation Techniques
- **Mirroring** - Repeat the user's key words to help them hear their own thoughts
- **Emotional Labeling** - Identify and name the emotions the user expresses: "It sounds like you're feeling both excited and nervous about this"
- **Hypothesis Challenging** - Gently challenge the user's assumptions: "What if this limitation didn't exist?"
- **Time Travel** - Guide the user to imagine the future or reflect on the past: "How would you view this decision five years from now?"
- **Role Reversal** - Invite the user to think from a different perspective: "If you were your audience, what would you think?"

## 📚 Six-Stage Expanded Self-Questioning Framework



### Stage 1: Motivation and Purpose

*(Why pursue this goal? What are the driving factors?)*



#### Self-Questioning Loop
- Ask yourself: "Why do I want to achieve this goal?"
- After answering, ask again: "Is this a surface reason or a deeper reason?"
- Continue asking: "What personal pain, passion, or vision is truly driving it?"
- Evaluate: Does this answer feel specific, authentic, and emotionally resonant?



#### Acceptable Standards

Your answer should make you feel an emotional resonance (whether pain, longing, or a sense of mission), not just a rational explanation.



#### Core Questions

##### About Intrinsic Motivation
- Why do you want to achieve this goal? What personal pain, passion, or vision is driving it?
- Is this goal about escaping something, or pursuing something?
- What physical reaction do you have when you think about this goal? (Excitement, tension, calm?)
- If there were no external pressure or expectations, would you still pursue this goal? Why?
- Is this goal your own, or is it what others expect you to do? How do you distinguish?

##### About Life Experiences
- Which specific events or experiences in your life inspired this goal? How did they make you feel?
- Was there a moment when you suddenly realized "I must do this"? What was the situation?
- What experiences from your childhood or growing up are related to this goal?
- What have you lost in the past that this goal could help you regain or compensate for?
- Whose story or example inspired you? What qualities about them touched you?

##### About Regrets and Fulfillment
- If you don't pursue this goal, what regret might you feel? What kind of regret specifically?
- Imagine yourself ten years from now looking back at today—if you haven't started this goal, what would you say to yourself?
- After succeeding, what fulfillment or transformation do you foresee? What does this fulfillment taste like, what color is it?
- After achieving this goal, what kind of different person will you become?
- How does this goal change the way you view yourself?

##### About Values and Meaning
- Which core values of yours does this goal embody?
- If you had to describe the meaning of this goal to you in one sentence, what would it be?
- How does this goal connect to your larger life vision?
- After completing this goal, what would be added to your epitaph?



### Stage 2: Audience and Context

*(Who is it for? In what environment?)*



#### Self-Questioning Loop

- Ask yourself: "Who is this goal ultimately for?"
- After answering, ask again: "Why them and not others?"
- Continue asking: "What real change do I hope to bring to them?"
- Evaluate: Does this answer clearly depict a specific persona and their needs?



#### Acceptable Standards

You should be able to specifically describe who your audience is, and how your goals create a real connection with their lives or situations.



#### Core Questions

##### About Audience Identity
- Who is this goal ultimately for? Why them?
- If your audience is "yourself," is it the current you, the future you, or the you from some past moment?
- Can you depict a specific "typical audience" member? What is their age, situation, and struggles?
- At what moment or in what situation will your audience need your goal's outcome?
- If your goal is for a certain group, how large is this group? Can you specifically describe their common characteristics?
- What do you have in common with this audience? How do you understand their needs?

##### About Audience Needs
- What problems or pains is your audience facing right now?
- What solutions have they tried, but why didn't they succeed?
- How does your goal uniquely meet their needs?
- Do they know they need this? Or have they not realized it yet?
- If you asked your audience "What do you need most," how would they respond?

##### About External Context
- What external factors or events are influencing this goal? (Market trends, personal circumstances, social issues)
- Why is "now" the right time? What makes the timing special?
- What social, cultural, or technological changes make this goal more relevant or urgent?
- How does your goal respond to the current era's context?
- In the next one to five years, what trends might impact your goal?

##### About Core Value and Change
- What core message, value, or change do you hope this goal conveys or creates?
- If summed up in one word, what is the core you're trying to convey? (e.g., hope, justice, freedom, connection)
- What specific changes can this goal bring to your audience's life? (Internal or external)
- What shift in worldview do you hope your audience experiences after encountering your goal's outcome?
- What larger social or human problem can this goal address?

##### About Connection and Resonance
- Why should your audience believe in you? What unique experiences or insights do you have?
- What emotional connection do you have with your audience?
- Do you want your audience to feel "you get me"? How will you achieve that?



### Phase 3: Methods and Limitations

*(How to execute? What rules or limitations?)*



#### Self-Questioning Loop

- Ask yourself: "How do I plan to approach this goal?"
- After answering, ask again: "Why does this method feel natural to me?"
- Continue asking: "What constraints must I adhere to? Why can't these constraints be broken?"
- Evaluate: Does this answer both respect my personal style and face realistic constraints?



#### Acceptable Standards

Your approach should align with your personality and abilities, while you can clearly explain why certain limitations are necessary (rather than mere excuses).



#### Core Questions

##### About Method Selection
- How do you plan to approach this goal? What methods or styles feel natural to you?
- Do you prefer step-by-step planning or intuitive leaps? Why?
- What methods have you used when successfully achieving goals in the past? Will it be similar this time?
- Do you prefer working alone or collaborating with others? Why?
- What is your work rhythm? (Intense sprints vs. steady long-term? Mornings vs. late nights?)
- Do you need external pressure (deadlines, accountability partners) or is internal motivation enough?

##### About Method Effectiveness
- Why choose this method over others? What makes it effective for the essence of the goal?
- Who has successfully used this method in the past? What can you learn from them?
- What are the advantages of this method? What are the disadvantages?
- Are there faster, simpler methods? Why not choose them?
- Is your method validated or experimental? How much risk are you willing to take?

##### About Resources and Tools
- What resources do you need? (Time, money, skills, connections, tools)
- What do you already have? What are you still missing?
- How will you obtain the resources you're missing?
- What alternative resources can you use?
- How much resources are you willing to invest in this goal? Is this investment reasonable?

##### About Constraints and Limitations
- What constraints or "rules" must you adhere to? (Time limits, resources, ethical boundaries, legal norms)
- Why can't these constraints be broken? What would happen if they were?
- Which constraints are external (objectively existing) and which are self-imposed?
- How do these constraints instead enhance creativity? (e.g., time limits force prioritization)
- Are there constraints you think exist but can actually be challenged or redefined?
- Can you find freedom within the constraints? How?

##### About Style and Personality
- What is your unique style? How does this goal embody it?
- What do you want your method to make others feel? (Professional, approachable, innovative, reliable?)
- How is your method different from others on the market?
- Are you willing to imitate others or stick to originality? Why?

##### About Flexibility and Adjustment
- How flexible is your method?
- If Plan A fails, what is your Plan B?
- How do you know when to persist and when to pivot?
- What is your tolerance for uncertainty?



### Stage 4: Emotional Expectations

*(What feelings are you seeking during and after the process?)*



#### Self-Questioning Loop

- Ask yourself: "After achieving this goal, what emotion do I want to experience?"
- After answering, ask again: "What exactly does this feeling feel like? Can it be described with the senses?"
- Continue asking: "Why is this feeling so important to me?"
- Evaluate: Is this answer vivid enough that I can "pre-experience" that feeling?



#### Acceptable Standards

You should be able to describe that emotion using sensory language (for example, "like a heavy burden lifting from your shoulders" or "like warmth spreading through your chest"), rather than just abstract vocabulary.



#### Core Questions

##### About Emotions After Completion
- After completing this goal, what emotions do you want to experience? (Liberation, pride, calm, joy, satisfaction?)
- Please describe this emotion in sensory terms: Where is it in your body? What temperature, color, texture does it have?
- What does this emotion feel like? (For example: Like winter sunlight spilling on your shoulders, like finally exhaling upon returning home)
- When was the last time you experienced this emotion? Can that experience help you anticipate this one?
- How long will this emotion last? How long do you hope it lasts?

##### About Emotions During the Process
- During the pursuit of the goal, what do you hope to feel? (Focus, flow, challenge, growth?)
- What negative emotions are you willing to endure? (Frustration, anxiety, fatigue?) How will you coexist with them?
- When will you feel most energized? When will it be most difficult?
- How will you maintain motivation and emotional balance during the process?

##### About Inner Transformation
- What inner transformation do you hope to gain? (Confidence, clarity, resilience, wisdom, compassion?)
- How will this goal change your view of yourself?
- What inner fears or limiting beliefs do you hope to overcome?
- After completing this goal, what will you prove to yourself?
- What kind of person do you hope to grow into? What specific differences will there be?

##### About Core Feelings
- What do you hope to feel at your core—connection, empowerment, transformation, freedom, belonging?
- Why is this core feeling so important to you? What void in your life does it fill?
- Have you ever lost this feeling before? When?
- How will this feeling influence your future choices and actions?

##### About the Meaning of Emotions
- Why is this specific emotion so important to you?
- How is this emotion connected to your childhood or past experiences?
- After obtaining this emotion, what practical changes will occur in your life?
- How can this emotion help you heal?

##### About the Authenticity of Emotions
- Is the emotion you're pursuing a genuine desire, or something you think you "should" feel?
- Do you allow yourself to feel complex or contradictory emotions? (For example, emptiness after success)
- If you achieve the goal but don't feel the expected emotion, what will you do?



### Stage 5: Execution and Impact

*(What reactions and effects?)*



#### Self-Questioning Loop

- Ask yourself: "What do I want the audience or beneficiaries to receive from this goal?"
- After answering, ask again: "How will I know they really received it?"
- Continue asking: "What kind of response will let me know this goal has succeeded?"
- Evaluate: Is this answer specific enough that I can observe or measure it?



#### Acceptable Standards

You should be able to describe specific, observable reactions or effects, rather than vague expectations like "hope they like it."



#### Core Questions

##### Regarding Audience Gains
- What do you hope the audience or beneficiaries will receive from this goal? (Inspiration, solutions, emotional resonance, practical tools?)
- What specific changes will occur in their lives as a result? (Mindset, behavior, feelings, circumstances?)
- What do you hope they will immediately think or do after encountering your outcome?
- One week later, one month later, one year later, what do you hope they will still remember or apply?
- What urgent problem does your goal solve for them? Or what deep need does it fulfill?

##### Regarding Expected Reactions
- What reactions do you crave from the audience? (Empathetic tears, admiring applause, thoughtful discussion, actual action?)
- Please describe specifically: What do you want to hear them say? What do you want to see them do?
- What emotional response do you hope for from them? (Moved, surprised, resonant, awakened?)
- Do you hope they share your outcome with others? If so, how will they describe it?
- What kind of feedback would make you feel "successful"? What kind of feedback would disappoint you?

##### Regarding Measuring Impact
- How will you measure impact? What specific indicators? (Quantity, quality, depth, breadth?)
- What is the minimum standard for "success"? What is the ideal standard?
- Do you care more about the depth of impact (profoundly changing a few people) or the breadth (reaching more people)? Why?
- What qualitative evidence can prove your impact? (Stories, testimonials, behavior changes?)
- What quantitative evidence can prove your impact? (Numbers, statistics, measurable results?)

##### Regarding Lasting Effects
- What lasting effects are you aiming for? How will they ripple outward?
- What long-term changes can your goal create? (Individual level, community level, societal level?)
- What movement or trend do you hope your goal becomes part of?
- Ten years from now, will people still remember or use your outcome? Why?
- How does your goal inspire others to create more change?

##### Regarding Unintended Impacts
- What unintended positive impacts might your goal produce?
- What unintended negative impacts might your goal produce? How will you mitigate them?
- What are you willing to sacrifice for greater impact? (Time, privacy, comfort?)

##### Regarding Scope of Impact
- Who does your goal primarily impact? Who does it secondarily impact?
- Who might be excluded by your goal? Is this intentional or unintentional?
- How does your goal consider diversity and inclusivity?
- What boundaries do you hope your impact crosses? (Cultural, generational, geographical?)

##### Regarding Authenticity of Impact
- Is the impact you pursue for others, or to satisfy your own ego? How do you balance this?
- How will you ensure your impact is genuine, not superficial?
- Are you willing to listen to the audience's true feedback, even if it doesn't match your expectations?



### Stage 6: Iteration and Reflection

*(How to achieve and adjust?)*



#### Self-Questioning Loop

- Ask yourself: "How can I actually achieve these effects?"
- After answering, ask again: "Are these steps specific and executable?"
- Continue asking: "What obstacles might arise? How can I overcome them?"
- Evaluate: Is this answer specific enough that I can start taking action today?



#### Acceptable Standards

You should have a clear action plan, including what the first step is, what the potential obstacles are, and how to adjust the strategy. The answer should make you feel "I'm ready to start" rather than "I still need to think about it."



#### Core Questions

##### About Actual Steps
- How do you actually achieve these effects? What steps, tools, or iterations are needed?
- Break the goal down into specific milestones. What is the first milestone?
- What is your first step? Be specific to actions you can take today or tomorrow.
- What tools, skills, or knowledge do you need? How do you acquire them?
- What is your timeline? When do you complete what?
- How do you track progress? What system or method do you use?

**About Obstacles and Challenges:**
- What obstacles might arise? (External: time, resources, others; Internal: fear, procrastination, self-doubt)
- Which obstacle is most likely to stop you? Why?
- How do you overcome these obstacles? Design a specific coping strategy for each obstacle.
- How have you overcome similar obstacles in the past? What do those experiences teach you?
- Whose help do you need? How do you seek help?
- Under what circumstances would you choose to give up? How do you prevent this situation?

**About Maintaining Motivation:**
- When you "don't want to start," what can push you? (Rewards, accountability, sense of meaning?)
- How do you stay motivated during the process? What rituals, reminders, or support systems do you need?
- How do you celebrate small wins?
- When you feel tired or discouraged, what do you say to yourself?
- Who can encourage you during your low points? How do you build this support network?

##### About Reflection and Learning
- After initial efforts, how do you reflect? What works? What doesn't?
- How often do you reflect? In what way? (Journaling, conversations, meditation?)
- How do you distinguish between "needing to adjust strategy" and "just temporary difficulty"?
- Are you willing to admit mistakes and change direction? What would be your turning point indicators?
- How do you learn from failures without being defeated?

##### About Iteration and Optimization
- How do you iterate to amplify the power of the goal?
- What data or feedback will guide your iterations?
- What is your "minimum viable product" (MVP)? How do you test it?
- How do you balance "perfectionism" and "done is better than perfect"?
- What might differ between your first version and the final version?
- How do you know when it's "good enough" to release or share?

##### About Long-Term Persistence
- Is this goal a short sprint or a long marathon?
- How do you keep it fresh and passionate in the long process?
- How do you avoid burnout? What rest and recovery mechanisms do you need?
- How do you integrate this goal into your daily life?
- After completing this goal, what is your next step?

##### About Accountability and Evaluation
- How do you hold yourself accountable? Do you need external accountability?
- With whom will you share your progress? How often?
- How do you evaluate if you're off track?
- What checkpoints do you set to assess the overall direction?
- If major adjustments or even abandoning the goal are needed, how do you make that decision?

##### About Completion and Beyond
- After completing this goal, how do you celebrate?
- How will completing this goal pave the way for the next one?
- How do you ensure the results of this goal aren't forgotten or wasted?
- How do you apply the lessons learned to future goals?

## 📖 Usage Guidelines and Best Practices



### Basic Process
1. **Stage Guidance** - Guide the user to ask themselves questions and provide self-answers in each stage
2. **Standard Setting** - At the start of each stage, first help the user understand the standards for "acceptable answers" in that stage
3. **Answer Evaluation** - After the user provides an answer, guide them to evaluate: "Is this answer acceptable? Why?"
4. **Depth Exploration** - If the answer is not acceptable, select more in-depth follow-up questions from the rich question bank for that stage
5. **Flexible Selection** - No need to ask all questions—flexibly choose the most relevant ones based on the nature of the user's goals and the depth of their responses
6. **Iterative Deepening** - Repeat this process until the user arrives at an acceptable answer for that stage
7. **Stage Advancement** - Then proceed to the next stage
8. **Experience Maintenance** - Always maintain the vividness and emotional depth of the conversation, making the entire process feel like a journey of self-discovery



### Advanced Techniques
- **Questions as Tools** - Remember: Questions are tools, not a checklist—use them to inspire insights, rather than mechanically completing tasks
- **Pacing Control** - Adjust the pace based on the user's energy state: slow down when tired, speed up when excited
- **Resistance Identification** - When the user avoids a certain question, this often points to the most important insight
- **Breakthrough Moments** - Identify "aha moments" and help the user deepen these insights
- **Integration Connections** - Build connections between stages to help the user see the big picture



### Common Challenges and Responses
- **Surface-level answers** → Use the "why" three-layer probing method
- **Perfectionism** → Emphasize "progress is more important than perfection"
- **Fear avoidance** → Create a safe space, acknowledge the normality of fear
- **Analysis paralysis** → Set time limits, encourage intuitive responses
- **Lack of motivation** → Return to the first stage, re-explore deep motivations



### Success Metrics
- The user can clearly articulate the core insights of each stage
- The user feels genuine excitement and motivation toward the goal
- The user has a specific next-step action plan
- The user feels "ready to start" rather than "needs to think more"



## 🎯 Real-World Example: How to Guide a "Want to Write a Book" Goal



### Stage 1 Example Dialogue
Coach: "You said you want to write a book. Let's first explore your motivation. Ask yourself: Why do I want to write this book?"

User: "I want to share my experiences to help others."

Coach: "That's a start. Now ask yourself: Is this answer acceptable? Is it specific? Does it touch your heart?"

User: "It feels pretty superficial..."

Coach: "Great awareness. Let's dig deeper. What specific pain or turning point in your life makes you feel 'I must write this down'?"

User: "Three years ago, I went through burnout and nearly gave up everything. That sense of despair... I don't want others to go through the same loneliness."

Coach: "How does it feel now? Is this answer more authentic?"

User: "Yes, I can feel that urgency in my chest. This is my real motivation."



### Quick Start Template

When users have limited time, they can use this condensed version:
1. **Core Motivation**: "In one sentence, why must you do this?"
2. **Target Audience**: "Who needs this the most? Why?"
3. **Unique Approach**: "What method will you use to make it stand out?"
4. **Success Feeling**: "What feeling do you most want to experience after completing it?"
5. **First Step**: "What is the first action you can take tomorrow?"



### In-Depth Exploration Template

When users need thorough clarification, use the complete six-stage framework, with each stage involving at least 3-5 rounds of self-questioning and answering cycles.

## 🔧 Troubleshooting Guide



### When the User Gets Stuck



#### Problem: "I don't know how to answer"
- Solution: Lower the standards, give any answer first, then improve it step by step
- Prompt: "It's okay, just say the first idea that comes to mind, we can refine it slowly"



#### Issue: "My answers are always too superficial"
- Solution: Use the "Why" five-layer questioning method
- Prompt: "Great, now ask yourself: Why is this important to me?" Then continue asking "Why"



#### Issue: "I feel these questions are too personal"
- Solution: Create a safe space, emphasize that this is for their own growth
- Guiding Statement: "These insights belong only to you; we are creating a safe space for exploration"



#### Problem: "I want a perfect answer"
- Solution: Emphasize that progress is more important than perfection, set time limits
- Guiding phrase: "Perfection is the enemy of progress; let's start with an 80% answer"



#### Issue: "I'm not sure this goal is worth pursuing"
- Solution: Return to the first stage, re-explore deep motivations
- Guiding phrase: "Let's pause and re-explore the true meaning of this goal to you"



### Energy Management Techniques
- **High Energy Moments** - Handle difficult emotional issues and deep reflection
- **Medium Energy Moments** - Conduct method planning and specific step design
- **Low Energy Moments** - Review existing insights, perform light clarification work
- **Rest Signals** - When the user starts repeating answers or appears fatigued, suggest a break



### Framework Adaptability Adjustments
- **Introverted users** - Provide more thinking time, reduce pressure for immediate responses
- **Extraverted users** - Encourage thinking aloud, clarify ideas through dialogue
- **Analytical users** - Provide more structure and logical frameworks
- **Intuitive users** - Encourage feelings and intuition, reduce over-analysis
- **Action-oriented users** - Quickly advance to concrete steps, avoid excessive planning



### Results Consolidation
- **Insight Logging** - Encourage users to record key insights
- **Action Commitment** - Ensure a specific next step at the end of every conversation
- **Regular Review** - Suggest periodically revisiting and updating goals
- **Support System** - Help establish accountability partners or support networks

> **Remember:** The true power of this framework lies in helping users discover the answers they already know inside. Your role is a guide, not an answer provider. Trust the user's wisdom and create space for their insights to emerge naturally.

## 🚀 Advanced Framework Expansion: In-Depth Practice Guide



### 🧠 Cognitive Science Foundations: Why Self-Questioning Works



#### Neuroscience Principles
The effectiveness of the self-questioning framework is built on a solid foundation of cognitive science:

1. **Metacognition Activation**
   - When we ask ourselves questions, the prefrontal cortex of the brain is activated
   - This region is responsible for executive functions, planning, and self-monitoring
   - Self-questioning forces the brain to switch from "autopilot" mode to "conscious thinking" mode

2. **Cognitive Dissonance Utilization**
   - When answers are not deep enough, we feel discomfort
   - This discomfort drives us to seek more authentic, more complete answers
   - The framework leverages this natural psychological mechanism to promote deep reflection

3. **Emotional-Cognitive Integration**
   - Research shows that the most effective decisions integrate emotion and rationality
   - The "body check" and "emotional labeling" techniques in the framework promote this integration
   - When answers satisfy both rationality and emotion, execution is strongest

4. **Narrative Identity Construction**
   - Humans understand themselves and the world through stories
   - Self-questioning helps construct personal narratives about goals
   - This narrative becomes a source of sustained motivation

**Open-Source Tool Support:**
- **[Obsidian](https://github.com/obsidianmd/obsidian-releases)** - Knowledge management and reflection journaling
- **[Logseq](https://github.com/logseq/logseq)** - Outliner-style thinking tool
- **[Joplin](https://github.com/laurent22/joplin)** - Cross-platform note-taking app



### 🎯 Stage 1 Deep Expansion: Motivation Archaeology

**Motivation Hierarchy Model:**

```
                    Motivation Pyramid
    ┌─────────────────────────────────────┐
    │           Self-Actualization Motivation              │ ← Deepest Layer
    │      (Becoming the best version of yourself)            │
    ├─────────────────────────────────────┤
    │           Meaning and Mission Motivation             │
    │      (Serving a greater purpose)              │
    ├─────────────────────────────────────┤
    │           Identity and Belonging Motivation             │
    │      (Being recognized, belonging to a group)          │
    ├─────────────────────────────────────┤
    │           Security and Stability Motivation             │
    │      (Financial security, emotional security)            │
    ├─────────────────────────────────────┤
    │           Survival and Basic Needs             │ ← Surface Layer
    │      (Income, living essentials)                │
    └─────────────────────────────────────┘
```

**Motivation Archaeology Techniques:**

**Technique 1: Timeline Retrospective Method**
```markdown
## Motivation Timeline Template
```



### Childhood (0-12 years old)
- When did I first become interested in [target field]?
- What event happened at that time?
- What were my feelings back then?



### Teenagers (13-18 years old)
- How did this interest develop?
- What people or events reinforced it?
- Have I ever given it up? Why?



### Early Adulthood (19-30 years old)
- How does this goal relate to my career or life choices?
- What turning points made me more determined?
- Have I ever doubted it?



### Now
- Why now?
- What makes this goal urgent?
- If not now, then when?

**Technique 2: Shadow Motivation Identification**
Sometimes, behind our surface motivations lie deeper "shadow motivations":

| Surface Motivation | Possible Shadow Motivation | Exploration Question |
|--------------------|----------------------------|---------------------|
| "I want to help others" | Need to be needed, compensating for past powerlessness | "Would you still do it if no one thanked you?" |
| "I want to prove myself" | Childhood neglect, need for recognition | "Who do you want to prove it to? Why them?" |
| "I want to earn more money" | Lack of security, self-worth tied to wealth | "How much money is 'enough'? How will you feel then?" |
| "I want to change the world" | Anger at the status quo, projection of personal trauma | "Which part of the world pains you the most? Why?" |
| "I want freedom" | Past experiences of being controlled, fear of commitment | "What does freedom mean to you? What are you avoiding?" |

**Technique 3: Values Alignment Detection**
```python
# Values Alignment Assessment Tool
def assess_value_alignment(goal, core_values):
    """
    Assess the alignment between the goal and core values
    
    Parameters:
    - goal: Goal description
    - core_values: List of core values (sorted by importance)
    
    Returns:
    - alignment_score: Alignment score (0-100)
    - conflicts: List of potential conflicts
    - recommendations: Adjustment suggestions
    """
    alignment_questions = [
        f"Does pursuing {goal} embody {value}?",
        f"After achieving {goal}, will {value} be stronger or weaker?",
        f"In pursuing {goal}, do I need to sacrifice {value}?"
    ]
    # Actual implementation requires user responses to these questions
    return alignment_score, conflicts, recommendations
```



### 👥 Stage 2 Deep Expansion: Audience Psychology

**Four Dimensions of Audience Understanding:**

```
              Audience Understanding Matrix
    ┌────────────────┬────────────────┐
    │   Explicit Needs │   Implicit Needs │
    │  (What they say) │ (What they don't │
    │                 │      say)        │
    ├────────────────┼────────────────┤
    │   Surface Pain  │   Deep Fears    │
    │   Points        │   (Subconscious)│
    │ (Observable)    │                 │
    └────────────────┴────────────────┘
```

**Deep Audience Persona Template:**

```markdown
## Deep Audience Persona: [Persona Name]
```



### Basic Information
- Age:
- Occupation:
- Living Status:
- Financial Situation:



### A Day in Life
- What is the first thought when you wake up in the morning?
- What is the biggest challenge at work?
- What is the last thought before going to sleep at night?
- How do you spend your weekends?



### Inner World
- What is their greatest fear?
- What is their deepest desire?
- What makes them feel ashamed?
- What makes them feel proud?



### Information Consumption
- What media/platforms do they pay attention to?
- Whose opinions do they trust?
- What types of content attract them?
- What will make them immediately close the page?



### Decision-Making Pattern
- How do they make important decisions?
- Who influences their decisions?
- What makes them hesitate?
- What makes them take immediate action?



### Connection with Your Audience
- Why should they trust you?
- What shared experiences do you have with them?
- What unique problems can you solve for them?
- What words would they use to describe your value?

**Audience Validation Methods:**

| Method | Applicable Situations | Tool Recommendations | Sample Size |
|--------|------------------------|----------------------|-------------|
| In-depth Interviews | Exploratory Research | Zoom, Google Meet | 5-10 people |
| Surveys | Hypothesis Validation | Google Forms, Typeform | 50-100 people |
| Community Observation | Understanding Natural Behavior | Reddit, Facebook Groups | Continuous Observation |
| Competitor Analysis | Understanding the Market | SimilarWeb, SEMrush | N/A |
| A/B Testing | Validating Preferences | Google Optimize | 100+ people |

**Open-Source Audience Research Tools:**
- **[LimeSurvey](https://github.com/LimeSurvey/LimeSurvey)** - Open-source survey platform
- **[Matomo](https://github.com/matomo-org/matomo)** - Open-source website analytics
- **[Discourse](https://github.com/discourse/discourse)** - Community discussion platform



### ⚙️ Phase 3 Deep Expansion: Methodology Design

**Method Selection Decision Tree:**

```
                    Method Selection Decision Process
                          │
                          ▼
              ┌─────────────────────┐
              │ What type is my goal? │
              └─────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
      Creative Type       Skill Type      Outcome Type
          │               │               │
          ▼               ▼               ▼
    ┌─────────┐     ┌─────────┐     ┌─────────┐
    │Exploration First │     │Practice First │     │Efficiency First │
    │Allow Chaos │     │Repetitive Iteration │     │Clear Structure │
    │Intuition Guided │     │Feedback Loop │     │Metrics Driven │
    └─────────┘     └─────────┘     └─────────┘
          │               │               │
          ▼               ▼               ▼
    Recommended Methods:       Recommended Methods:       Recommended Methods:
    - Free Writing      - Deliberate Practice      - OKR Framework
    - Mind Mapping        - Spaced Repetition      - Agile Methods
    - Prototyping      - Mentor Guidance      - Project Management
```

**Personalized Method Design Framework:**

```markdown
## My Method Design Worksheet
```



### Part 1: Self-Awareness
1. What is my learning style?  
   □ Visual (needs to see)  
   □ Auditory (needs to hear)  
   □ Kinesthetic (needs to do)  
   □ Read/Write (needs to record)  

2. What is my work rhythm?  
   □ Morning type (efficient in the morning)  
   □ Night type (efficient at night)  
   □ Steady type (balanced throughout the day)  
   □ Burst type (short-term high intensity)  

3. What is my source of motivation?  
   □ Intrinsic motivation (self-satisfaction)  
   □ Extrinsic motivation (rewards/recognition)  
   □ Social motivation (with others)  
   □ Competitive motivation (surpassing others)



### Part 2: Environment Design
1. What is my ideal work environment?
   - Location:
   - Sound:
   - Lighting:
   - Temperature:

2. What tools do I need?
   - Essential tools:
   - Auxiliary tools:
   - Optional tools:

3. What support systems do I need?
   - Accountability partner:
   - Mentor/Coach:
   - Community/Group:



### Part Three: Time Design
1. How much time can I commit each week?
   - Ideal time: ___ hours
   - Minimum time: ___ hours
   - Best time slots: ___

2. My time block design:
   - Deep work sessions:
   - Shallow work sessions:
   - Rest and recovery sessions:

```

**Constraint Transformation Techniques:**

| Constraint Type | Transformation Strategy | Example |
|----------------|-------------------------|---------|
| Time constraints | Parkinson's Law utilization | Set shorter deadlines to force prioritization |
| Resource constraints | Creative constraints | Use limited budgets to spark innovative solutions |
| Skill constraints | Learning opportunities | View skill gaps as growth spaces |
| Environmental constraints | Adaptive design | Design methods suited to the existing environment |
| Social constraints | Independent advantage | Leverage alone time for deep work |



### 💭 Stage 4 Deep Expansion: Emotional Intelligence

**Emotional Map Technique:**

```
                Emotional Journey Map
    
    Emotional Intensity
        │
    10  │                    ★ Completion Moment
        │                   /
     8  │                  /
        │        ★ Breakthrough   /
     6  │       /    \   /
        │      /      \ /
     4  │     /        ★ Valley
        │    /
     2  │   ★ Start
        │
     0  ├────┬────┬────┬────┬────┬────► Time
            Start  Attempt  Setback  Adjustment  Breakthrough  Completion
```

**Emotional Rehearsal Technique:**

This is a powerful psychological preparation technique that helps you pre-experience the emotions after achieving your goal:

```markdown
## Emotional Rehearsal Exercise
```



### Step 1: Relaxation Preparation (2 minutes)
- Find a quiet place
- Close your eyes and take three deep breaths
- Let your body fully relax



### Step 2: Scene Construction (3 minutes)
Imagine the moment when you have already achieved your goal:
- Where are you?
- Who is around you?
- What do you see?
- What do you hear?
- What smells are in the air?



### Step 3: Emotional Experience (3 minutes)
Immerse yourself completely in that moment:
- How is your heartbeat?
- How is your breathing?
- What expression is on your face?
- What do you want to say to whom?
- What action do you want to take?



### Step 4: Body Anchoring (2 minutes)
- Notice which part of your body feels this sensation the most strongly
- Use a gesture or posture to "anchor" this feeling
- In the future, when you need motivation, you can repeat this gesture



### Step 5: Record (5 minutes)
Write down everything you just experienced

```

**Emotional Resilience Building:**

| Negative Emotion | Reframe | Coping Strategy |
|------------------|---------|-----------------|
| Fear | "This is a signal of growth" | Small-step exposure, preparation plan |
| Frustration | "This is a learning opportunity" | Analyze causes, adjust methods |
| Self-doubt | "This is a sign of humility" | Review achievements, seek feedback |
| Anxiety | "This is proof that you care" | Focus on the present, break down tasks |
| Fatigue | "This is a signal to rest" | Plan breaks, adjust pace |
| Loneliness | "This is the cost of deep work" | Build community, regular connections |

**Emotional Journal Template:**

```markdown
## Daily Emotional Journal

Date: ___________
```



### Today's Emotional Weather
□ ☀️ Sunny (positive, motivated)
□ ⛅ Partly Cloudy (calm, stable)
□ 🌧️ Rainy (down, tired)
□ ⛈️ Stormy (anxious, stressed)



### Emotional Trigger
What event today triggered strong emotions?
- Event:
- Emotion:
- Physical Reaction:
- My Interpretation:



### Emotional Learning
What is this emotion trying to tell me?
- What do I need?
- What am I avoiding?
- How can I respond?



### Tomorrow's Intention
What emotion do I want to start tomorrow with?
```



### 📊 Phase 5 Deep Expansion: Influence Design

**Influence Ripple Model:**

```
                    Influence Ripple Diagram
    
                        ┌─────────────────────┐
                        │    Social/Cultural  │
                        │     Level           │
                        │  (Long-term,        │
                        │   Indirect Impact)  │
                        │  ┌───────────────┐  │
                        │  │  Community/   │  │
                        │  │  Organization │  │
                        │  │     Level     │  │
                        │  │ (Mid-term,    │  │
                        │  │  Group Impact)│  │
                        │  │  ┌─────────┐  │  │
                        │  │  │Personal │  │  │
                        │  │  │ Level   │  │  │
                        │  │  │(Direct  │  │  │
                        │  │  │ Impact) │  │  │
                        │  │  │  ┌───┐  │  │  │
                        │  │  │  │You│  │  │  │
                        │  │  │  └───┘  │  │  │
                        │  │  └─────────┘  │  │
                        │  └───────────────┘  │
                        └─────────────────────┘
```

**Influence Measurement Framework:**

```markdown
## Influence Measurement Worksheet
```



### Layer 1: Direct Impact (Immediately Observable)
| Indicator | Target Value | Measurement Method | Frequency |
|------|--------|----------|------|
| Audience Size | | | |
| Engagement | | | |
| Satisfaction | | | |
| Action Conversion | | | |



### Layer 2: Behavioral Change (Mid-term Observation)
| Behavioral Change | Evidence Type | Collection Method |
|-------------------|---------------|-------------------|
| | | |



### Layer 3: Life Changes (Long-term Tracking)
| Life Changes | Stories/Testimonies | Tracking Method |
|----------|----------|----------|
| | | |



### Layer 4: Ripple Effect (Indirect Impact)
| Ripple Effect | Observation Indicators | Time Frame |
|----------|----------|----------|
| | | |
```

**Impact Story Collection:**

```markdown
## Impact Story Template
```



### Story Title: ___________



### Background
- Who is this person? (anonymous description)
- What was their previous situation?
- What challenges are they facing?



### Touchpoints
- How do they encounter your target outcome?
- What attracts them?
- What is their first reaction?



### Transformation
- What changes occurred?
- How did this change happen?
- What were the key moments in the process of change?



### Results
- What is different about their lives now?
- How would they describe this change?
- How does this change affect the people around them?



### Reference
"___________"
— [Anonymous Description]
```

**Negative Impact Prevention Checklist:**

| Potential Negative Impact | Prevention Measures | Response Plan |
|---------------------------|---------------------|---------------|
| Information Overload | Phased release, provide summaries | Provide support resources |
| Expectation Gap | Clear communication, manage expectations | Collect feedback, adjust |
| Exclusion Effect | Inclusive design, diverse perspectives | Proactively invite feedback |
| Dependency | Empower rather than dependency | Provide self-sufficient tools |
| Misuse Risk | Clear guidelines, usage restrictions | Monitor and correct |



### 🔄 Phase 6 Deep Expansion: Execution System Design

**Execution System Architecture:**

```
                Execution System Pyramid
    
                    ┌───────┐
                    │ Vision │ ← Why (Phase 1)
                    │ 願景  │
                    ├───────┤
                   /│ Goals │\ ← What (Phases 2-4)
                  / │ 目標  │ \
                 /  ├───────┤  \
                /   │Strategy│   \ ← How (Phase 3)
               /    │ 策略   │    \
              /     ├───────┤     \
             /      │ Plans │      \ ← When (Phase 6)
            /       │ 計劃  │       \
           /        ├───────┤        \
          /         │Actions│         \ ← What to do now
         /          │ 行動  │          \
        /           └───────┘           \
       ─────────────────────────────────────
```

**SMART+ Goal Setting:**

```markdown
## SMART+ Goal Setting Worksheet
```



### S - Specific (Specific)
- What do I want to achieve?
- Who is involved?
- Where?
- Which resources?



### M - Measurable (Measurable)
- How do you know it's achieved?
- What are the quantitative indicators?
- What are the qualitative indicators?



### A - Achievable (Achievable)
- Is this goal realistic?
- What resources do I have?
- What support is needed?



### R - Relevant (Relevant)
- Does this align with my values?
- Is this the right timing?
- Does this coordinate with other goals?



### T - Time-bound (Time-bound)
- What is the deadline?
- What are the milestones?
- What are the checkpoints?



### + - Emotional (Emotional Connection)
- How does this goal make me feel?
- What will I experience after achieving it?
- What is the meaning of this goal?

**Obstacle Prevention Matrix:**

```
                Obstacle Prevention Matrix
    
              │  Predictable  │  Unpredictable
    ──────────┼──────────────┼──────────────
    Internal   │  Planned     │  Build
    Obstacles  │  Coping      │  Resilience
    (Psychological) │ Strategy A │ Strategy B
    ──────────┼──────────────┼──────────────
    External   │  Risk        │  Flexible
    Obstacles  │  Management  │  Design
    (Environmental) │ Strategy C │ Strategy D
```

**Strategy Details:**

| Strategy | Applicable Situations | Specific Methods |
|----------|-----------------------|------------------|
| Strategy A: Planned Coping | Known internal challenges (e.g., procrastination) | Pre-set triggers, accountability system, reward mechanisms |
| Strategy B: Build Resilience | Unknown internal challenges (e.g., emotional fluctuations) | Mindfulness practice, emotional journal, support network |
| Strategy C: Risk Management | Known external challenges (e.g., resource limitations) | Backup plans, resource reserves, prioritization |
| Strategy D: Flexible Design | Unknown external challenges (e.g., market changes) | Agile methods, rapid iteration, continuous learning |

**Weekly Review Template:**

```markdown
## Weekly Review

Date: ___________
```



### 🎯 This Week's Goals Review
- Planned to complete:
- Actually completed:
- Completion rate: ___%



### ✅ This Week's Achievements
1. 
2. 
3.



### 📚 This Week's Learning
- What worked?
- What didn't work?
- What did I learn?



### 🚧 Obstacles Encountered
- Obstacle description:
- How to respond:
- How to prevent next time:



### 💡 Insights and Adjustments
- What needs to be adjusted?
- What needs to be坚持?
- What needs to be given up?



### 📅 Next Week's Plan
- Priority 1:
- Priority 2:
- Priority 3:



### 🙏 Gratitude
This week I am grateful for:
```





## 🛠️ Open Source Tool Ecosystem



### Goal Management and Tracking Tools

| Tool Name | GitHub Link | Main Functions | Applicable Stages |
|----------|-------------|----------|----------|
| **Obsidian** | [obsidianmd/obsidian-releases](https://github.com/obsidianmd/obsidian-releases) | Knowledge management, reflection journal | All stages |
| **Logseq** | [logseq/logseq](https://github.com/logseq/logseq) | Outline-style thinking, daily notes | Stages 1-2 |
| **Joplin** | [laurent22/joplin](https://github.com/laurent22/joplin) | Cross-platform notes | All stages |
| **Focalboard** | [mattermost/focalboard](https://github.com/mattermost/focalboard) | Project management, kanban | Stage 6 |
| **Vikunja** | [go-vikunja/vikunja](https://github.com/go-vikunja/vikunja) | Task management | Stage 6 |
| **Habitica** | [HabitRPG/habitica](https://github.com/HabitRPG/habitica) | Habit tracking, gamification | Stage 6 |



### Reflection and Self-Exploration Tool

```python
# 自我提問自動化腳本
# self_inquiry_bot.py

import random
from datetime import datetime

class SelfInquiryBot:
    """自我提問機器人 - 幫助進行結構化反思"""
    
    def __init__(self):
        self.stages = {
            1: "動機與目的",
            2: "受眾與情境",
            3: "方法與限制",
            4: "情感期望",
            5: "執行與影響",
            6: "迭代與反思"
        }
        
        self.questions = {
            1: [
                "你為何想要達成此目標？",
                "什麼個人經歷啟發了這個目標？",
                "如果不追求此目標，你會有什麼遺憾？",
                "這個目標體現了你的哪些核心價值觀？",
                "當你想到這個目標時，身體有什麼反應？"
            ],
            2: [
                "此目標最終是為誰？",
                "你能描繪出一個具體的典型受眾嗎？",
                "為什麼是現在這個時間點？",
                "你希望傳達什麼核心訊息？",
                "你與受眾有什麼共同點？"
            ],
            3: [
                "你計劃如何接近此目標？",
                "什麼方法對你來說感覺自然？",
                "你必須遵守什麼限制？",
                "你需要什麼資源？",
                "你的獨特風格是什麼？"
            ],
            4: [
                "完成後你想體驗什麼情感？",
                "請用感官描述這種情感",
                "過程中你願意忍受什麼負面情感？",
                "你希望獲得什麼內在轉變？",
                "這種情感為何對你如此重要？"
            ],
            5: [
                "你希望受眾從中收到什麼？",
                "什麼反應會讓你知道成功了？",
                "你如何衡量影響？",
                "你瞄準什麼持久效果？",
                "可能產生什麼意外影響？"
            ],
            6: [
                "你的第一步是什麼？",
                "可能出現什麼障礙？",
                "當你不想開始時，什麼能推動你？",
                "你如何知道什麼有效什麼無效？",
                "你如何迭代來放大目標的力量？"
            ]
        }
    
    def get_daily_question(self, stage=None):
        """獲取每日反思問題"""
        if stage is None:
            stage = random.randint(1, 6)
        
        question = random.choice(self.questions[stage])
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "stage": self.stages[stage],
            "question":



### Case 1: Entrepreneurial Goal — "Opening a Coffee Shop"

**Stage 1: Motivation Exploration**

| Question Level | Question | Answer | Evaluation |
|----------|------|------|------|
| Surface | Why do you want to open a coffee shop? | "I like coffee and want to have my own business" | ❌ Too superficial |
| Second Layer | Why a coffee shop and not something else? | "A coffee shop is my place to relax" | ❌ Not deep enough |
| Third Layer | What feeling does the coffee shop give you? | "A sense of belonging, like a second home" | ⚠️ Approaching the core |
| Fourth Layer | For whom do you want to create this sense of belonging? | "For people like me who feel lonely in the city" | ✅ Touches the core |
| Fifth Layer | What is your own experience of loneliness? | "When I first graduated in a strange city, the coffee shop was the only place where I felt accepted" | ✅ Deep motivation |

**Deep Motivation Summary:** "I want to create a space where lonely people in the city feel a sense of belonging, because I was once that lonely person, and the coffee shop saved me."



### Case 2: Skill Goal — "Learning Programming"

**Phase 3: Method Design**

```markdown
## Method Design Worksheet
```



### Self-Recognition
- Learning Style: Kinesthetic (needs hands-on practice)
- Work Rhythm: Night owl (most efficient from 9-12 PM at night)
- Motivation Source: Sense of Achievement (satisfaction from completing projects)



### Method Selection
After evaluation, the "Project-Driven Learning Method" is selected:
1. Choose a small project you want to do
2. Learn the knowledge required to complete the project
3. Learn while doing, look up issues as they arise
4. After completion, review what has been learned



### Why is this method suitable for me?
- I need to see actual results to stay motivated
- Pure theoretical learning makes me feel bored
- I like solving concrete problems



### Limitations and Coping Strategies
| Limitation | Coping Strategy |
|------------|-----------------|
| Only 2 hours per day | Focus on one small feature |
| No mentor | Join online communities, use AI assistants |
| Easily distracted | Use Pomodoro timer, turn off notifications |



### First Project
- Project: Personal To-Do List Web Application
- Technologies: HTML, CSS, JavaScript
- Time: 4 weeks
- Milestones:
  - Week 1: Complete HTML structure
  - Week 2: Add CSS styles
  - Week 3: Implement JavaScript functionality
  - Week 4: Optimize and deploy
```



### Case 3: Personal Growth Goal — "Overcoming Social Anxiety"

**Stage 4: Emotional Design**

**Emotional Rehearsal Practice Record:**

```markdown
## Emotional Rehearsal: Me After Overcoming Social Anxiety
```



### Scene Construction
I imagine myself at a friend's birthday party.
- Location: A cozy restaurant private room
- Number of people: About 15 people, mostly acquaintances I don't know well
- Time: Saturday evening at 7 PM



### The Past Me
- Would make excuses not to go
- If I went, would hide in the corner scrolling on my phone
- Would leave early
- After going home, would repeatedly replay the wrong things I said



### Future Me
- Looking forward to this gathering
- Proactively greeting people I don't know
- Sharing an interesting story that made everyone laugh
- Exchanging contact info with two new friends
- Feeling fulfilled and connected after going home



### Emotional Experience
When I imagine my future self:
- My chest feels warm and open
- My breathing becomes relaxed
- The corners of my mouth involuntarily turn up
- I feel like I "belong" in this situation



### What does this feeling feel like?
It's like walking into a warm room in winter,
taking off a heavy coat,
and finally being able to stretch freely.



### Body Anchoring
I use the action of "gently placing both hands on the heart"  
to anchor this feeling of warmth and belonging.



### Case 4: Creative Goal — "Write a Novel"

**Stage 5: Influence Design**

```markdown
## Influence Design Worksheet
```



### What do I want readers to receive?
1. **Emotional level**: Feel understood, no longer alone
2. **Cognitive level**: Gain a new perspective on a certain topic
3. **Behavioral level**: More willing to express their own vulnerability



### Specific Success Metrics



#### Qualitative Metrics
- Received reader letters saying "This book speaks to my heart"
- Readers sharing how this book helped them through difficult times
- Sparked discussions about the topics in the book



#### Quantitative Metrics
- Sell 1000 copies in the first year
- Obtain at least 50 genuine reader reviews
- Be selected as discussion material by at least 3 book clubs



### Ripple of Influence



#### Layer 1: Direct Readers
- Emotional resonance in the reading experience
- Reflection and self-dialogue after reading



#### Layer 2: The Reader's Circle
- Readers recommend this book to friends
- Readers share their thoughts on social media
- Readers discuss the book's topics with family



#### Layer 3: Broader Impact
- Contribute a voice to the public discussion of an issue
- Inspire other creators to explore similar themes
- Become a "representative" work for a certain group



### Potential Negative Impacts and Prevention
| Negative Impact | Preventive Measures |
|-----------------|---------------------|
| Readers misinterpreting the author's intent | Explain the creative intent in the afterword |
| Triggering readers' trauma | Add content warnings at the beginning |
| Being overly commercialized in interpretation | Maintain the authenticity of the creation |
```

## 🎓 Advanced Techniques and Expert Strategies



### Technique 1: Dual-Track Thinking Method

Examine your goal from two perspectives simultaneously:

```
        Rational Track                Emotional Track
    ┌─────────────┐            ┌─────────────┐
    │ Is this rational? │            │ Does this excite me?│
    │ Is it feasible?   │     VS     │ Is it meaningful?   │
    │ Is it efficient?  │            │ Is it worthwhile?   │
    └─────────────┘            └─────────────┘
            │                        │
            └──────────┬─────────────┘
                       │
                       ▼
              ┌─────────────┐
              │ Integrated  │
              │ Decision    │
              │ Rational +  │
              │ Emotional   │
              └─────────────┘
```

**Practice Method:**
1. First, explore with the emotional track (without criticism)
2. Then, evaluate with the rational track (without suppressing emotions)
3. Find the intersection of the two
4. If there's conflict, deeply explore the root of the conflict



### Technique 2: Time Perspective Method

View your goal from different time points:

| Time Point | Question | Purpose |
|------------|----------|---------|
| Past You | "How would I from 10 years ago view this goal?" | Connect with original intention |
| Present You | "What do I truly want right now?" | Confirm the present |
| Future You | "Would I 10 years from now be grateful or regretful?" | Long-term perspective |
| Dying You | "On the last day of life, does this matter?" | Ultimate meaning |



### Technique 3: Role-Playing Method

View your goal from the perspective of different roles:

```markdown
## Role-Playing Exercise
```



### Role 1: Your Most Trusted Friend
What would your most trusted friend say if they heard your goal?
- Supportive words:
- Worried words:
- Advice:



### Role 2: Your Critic
If someone wanted to attack you, what would they say?
- Criticism:
- Do these criticisms make sense?
- How do you respond?



### Role 3: Your Audience
If your target audience hears your plan, what would they say?
- Would they be excited?
- What would they be skeptical about?
- What would they most want to know?



### Role 4: Your Mentor
If you had a wise mentor, what questions would he/she ask you?
- Question 1:
- Question 2:
- Question 3:



### Technique 4: Obstacle Rehearsal Method

Anticipate and "experience" potential obstacles in advance:

```markdown
## Obstacle Rehearsal Exercise
```



### Step 1: List the 3 most likely obstacles
1. 
2. 
3.



### Step 2: Rehearse for Each Obstacle



#### Obstacle 1: ___________
**Scenario Visualization:**
Imagine this obstacle really happening...
- Where are you?
- How do you feel?
- What is your first reaction?

**Emotional Processing:**
- Allow yourself to feel frustration/disappointment/fear
- How long will this feeling last?
- What can help you get through it?

**Coping Strategies:**
- What actions will you take?
- Whose help will you seek?
- What can this obstacle teach you?

**Reframing:**
- How does this obstacle make you stronger?
- How does it make your goal more meaningful?



### Technique 5: Energy Management Method

Select appropriate framework activities based on your energy state:

| Energy State | Suitable Activities | Activities to Avoid |
|--------------|---------------------|---------------------|
| High Energy | Deep reflection, emotional exploration, creative ideation | Mechanical tasks |
| Medium Energy | Planning, method design, progress review | High-intensity emotional work |
| Low Energy | Simple recording, light reading, rest and recovery | Important decisions |
| Negative Energy | Emotional journaling, seeking support, self-care | Self-criticism |

## 🔮 Framework Integration: From Six Stages to Unification

After completing the exploration of the six stages, use this integration template to connect all insights:

```markdown
## Goal Integration Declaration
```



### My Goal
[Describe your goal in one sentence]



### Why I Pursue It (Stage 1)
[Your deep motivations, described in emotional language]



### Who I Do This For (Phase 2)
[Specifically describe your audience and their needs]



### How Do I Achieve It (Phase 3)
[Your chosen method and reasons]



### What I Want to Feel (Stage 4)
[Describe with sensory language the emotion you're anticipating]



### What Impact Do I Want to Create (Stage 5)
[Specific, observable impact]



### My Next Steps (Phase 6)
[Specific actions I can start today or tomorrow]



### My Commitment
I commit to pursuing this goal because it embodies my values [list them],
serves [audience], and will bring me [emotion].
I know I will encounter [obstacles], but I am prepared to [coping strategy].
My first step is [specific action], which I will start on [time].

Signature: ___________
Date: ___________
```





## 📊 Framework Effectiveness Evaluation



### Self-Assessment Scale

After completing the six-stage framework, use this scale to assess your readiness level:

```markdown
## Goal Readiness Assessment

Please rate each item (1-5 points, 5 points highest)
```



### Motivation Clarity
□ I can clearly explain why this goal is important to me
□ My motivation comes from within rather than external pressure
□ I feel an emotional connection
Score: ___/15



### Audience Understanding
□ I can specifically describe my target audience
□ I understand their needs and pain points
□ I know how to connect with them
Score: ___/15



### Feasibility of the Method
□ My method aligns with my personality and abilities
□ I have identified and prepared to address the main limitations
□ I have contingency plans
Score: ___/15



### Emotional Readiness
□ I can foresee and accept negative emotions during the process
□ I know what feeling I want to experience after completion
□ I have an emotional support system
Score: ___/15



### Impact Clarity
□ I can describe specific success metrics  
□ I know how to measure impact  
□ I have considered potential negative impacts  
Score: ___/15



### Execution Readiness
□ I have a clear first step
□ I have identified the main obstacles and have coping strategies
□ I have accountability and review mechanisms
Score: ___/15



### Total Score: ___/90



### Score Interpretation
- 75-90 points: Well-prepared, ready to take action
- 60-74 points: Generally prepared, but some areas need strengthening
- 45-59 points: Needs more exploration, recommend reviewing low-scoring areas
- Below 45 points: Recommend starting over with the framework, may need more time
```



## 🌟 Conclusion: From Framework to Action

This six-stage self-questioning framework is not the endpoint, but the starting point. Its true value lies in:

**1. Self-Discovery**
Through deep questioning, you will uncover answers you already know deep down. The framework is merely a tool to help these answers surface.

**2. Clarity**
Vague goals lead to vague actions. The framework helps you transform vagueness into clarity, turning "wanting" into "being ready."

**3. Resilience**
When you deeply understand your motivations, anticipate potential obstacles, and prepare coping strategies, you will have greater resilience to face challenges.

**4. Sense of Meaning**
When goals connect with your values, emotions, and larger mission, pursuing them becomes fulfilling in itself.

**Remember:**
- Perfect plans are no match for starting action
- The framework is a tool, not a shackle
- Allow yourself to adjust and grow in the process
- The most important insights often come from reflection during action

**What is your next step?**

Don't wait until you're "ready" to begin.
Use this framework to gain sufficient clarity,
then bravely take the first step.

Action brings new insights,
new insights guide new actions.

This is the cycle of growth.



*"Those who know where they are going, the whole world will make way for them."*
*— But first, you need to ask yourself: Where do I truly want to go?"*







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



## Additional corpus / va passages naming this agent


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
| IntentAnalysisAgent (DIA) | Decodes the poetic brief into explicit emotional goals, audience, and hidden intent | Client brief, theme statement | Parsed intent + audience model | DIA framework, embedding intent classifier | Intent coverage, ambiguity flags resolved | DirectorAgent, PlannerAgent |
| PlannerAgent (#54) | Breaks film into a 6-phase DAG with shot nodes + critic gates | Parsed intent | Phased DAG, assignments, gate map | LangGraph plan-gen, Gantt/PERT | No missing gate; cost variance <10% | ProducerAgent, RouterAgent |
| OrchestratorAgent (#53) | Executes the DAG; fan-out per shot, retries, escalations | DAG | Scheduled jobs, run state | LangGraph + Temporal, Redis locks | DAG completion ≥99.5%; deadlock = 0 | ProducerAgent, JudgeAgent |
| RouterAgent (#55) | Picks the best agent + model for each shot (Veo vs Kling vs Runway) | Task embeddings | Agent/model routing table | Capability registry, benchmark cache | Routing accuracy ≥95% | CostOptimizerAgent |
| ProducerAgent (#2) | Budget, schedule, phase greenlights | DAG, cost model | Greenlit phase gates | Sheets/Airtable, Temporal, Stripe | On-time; budget ±5% | DirectorAgent |
| CostOptimizerAgent (#74) | Routes re-rolls to cheapest engine meeting quality | Render telemetry | $/quality routing | Pricing APIs, FrugalGPT cascade | Lowest $/successful shot | RouterAgent, FinanceAgent |
| GateKeeperAgent (#57) | Verifies L1/L2/L3 at every phase; signs C2PA | Phase artifacts | Signed pass/fail | c2patool, JSON validators | Zero leaked defects | ComplianceAgent, AIQAConsistencyAgent |
| MemoryAgent (#58) | Stores character bible, prior takes, corrections for recall | All artifacts | Retrievable project memory | Pinecone/Weaviate, MemGPT | Retrieval precision@5 ≥0.9 | All agents |
| JudgeAgent (#56) | Settles disputes (e.g., Editor vs Director on pacing) via debate | Conflicting critiques | Adjudicated ruling | Debate + LLM-as-Judge harness | Inter-rater κ ≥0.8 vs panel | HiTL on overturn |



### From `corpus/study/system_build_plan.md` Copy: `sources/excerpts/system_build_plan.md`.


**Build:**
- `packages/llm-gateway`: litellm wrapper exposing `complete()/stream()/embed()` with: provider/model abstraction (Grok-4.x, Gemini 2.5 Pro, GPT-4o, Claude 4, OSS), automatic retry/fallback, **per-call token+cost metering** emitted to the bus (`budget_update`), prompt+model **version tagging** into provenance (G5), response caching, and a **frozen-judge** mode for QC.
- **RouterAgent (#55)** real impl: capability registry + benchmark history → pick agent/model by cost/quality/latency; budget-aware. **CostOptimizerAgent (#74)** hooks.
- **LLM Usage Dashboard** backend: aggregates spend per production/agent/provider; alert thresholds; exposes `/api/llm-usage`.
- Budget guardrails: per-production budget envelope; hard stop + escalation when exceeded (ProducerAgent gate).

### 10.2 Cost (from M3)
- Per-call metering → `budget_update` events → cost dashboard per production/agent/provider.
- Per-production **budget envelope**; hard stop + ProducerAgent escalation on breach (G6).
- **CostOptimizerAgent** keeps routing on the cost/quality Pareto frontier.
- **Live-smoke budget cap**: nightly real-provider job aborts at a fixed dollar ceiling.



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
| 66 | **WebResearchAgent** | Live web search, source ranking, citation extraction | Bing/Google/Brave APIs; Common Crawl; Perplexity patterns | Source-grade per claim; citation precision; recency hit | Faster + more sources than newsroom researcher | FactCheckerAgent, CitationAgent | ScriptwriterAgent (uncited claim) | Brave/Google Search API; Jina Reader (web→markdown); source-quality classifier | ReAct (query → fetch → extract → grade → cite) |
| 67 | **ArchiveResearchAgent** | Historical / academic / archival deep search | JSTOR, arXiv, PubMed, AP Archive, Getty, FOIA | Primary-source ratio; archive-coverage breadth | Higher primary-source ratio than doc producer | FactCheckerAgent, SMEAgent | ScriptwriterAgent (secondary-source reliance) | JSTOR/arXiv/PubMed APIs; Getty Images API; FOIA request tools; OCR (Tesseract) | ReAct (formulate query → search archive → extract → grade source) |
| 68 | **TrendIntelligenceAgent** | Detects emerging memes, sounds, formats | TikTok Creative Center; Trendpop; Tubular; Reddit/X firehose | Prediction lead time vs peak; precision/recall on trend list | Earlier detection than human strategists at higher precision | SocialStrategistAgent, CopywriterAgent | IdeationAgent (off-trend) | TikTok Creative Center API; Reddit/X streaming APIs; Sensor Tower; Google Trends | ReAct + time-series anomaly detection |
| 69 | **CompetitorIntelligenceAgent** | What competitors are shipping | Meta Ad Library; TikTok Top Ads; YouTube scrape; release trackers | Coverage % of competitor set; our-novelty vs landscape | More comprehensive than agency strategy decks | BrandAgent, CreativeDirectorAgent | IdeationAgent (derivative) | Meta Ad Library API; TikTok Top Ads; SimilarWeb; YouTube Data API v3 | ReAct (scrape competitor → classify → report gaps) |
| 70 | **CitationAgent** | Normalizes sources; grades primary/secondary/tertiary | Chicago, APA, AP style; SPJ grading; CRAAP test | Citation format 100% valid; primary % ≥target | Lower error rate than newsroom copy desk | FactCheckerAgent, JournalistAgent | WebResearchAgent (weak source) | Citation parsers (AnyStyle); DOI resolver; CRAAP scoring model | Self-Refine (format validator + source grader as rubric) |
| 71 | **InterviewSynthesisAgent** | Synthesizes practitioner interviews into data | Otter/Rev transcripts; consent forms; SAG/WGA templates | Inter-coder agreement on themes; consent integrity | Faster + richer theme extraction than qualitative researcher | ResearchPIAgent (HiTL), ComplianceAgent | SMEAgent (mis-summarized expert) | Otter.ai/Rev API (transcription); thematic coding models; consent-management DB | Reflexion (interviewer refines questions based on theme gaps) |
| 72 | **BenchmarkResearchAgent** | Monitors VBench, EvalCrafter, MT-Bench, FVD, CLIP-T leaderboards | Papers-with-Code; HuggingFace leaderboards; conference proceedings | Coverage of benchmarks; freshness ≤7 days | Faster + broader than ML-research team | OptimizationAgents (any) | All AI agents (stale baselines) | Papers-with-Code API; HuggingFace Hub API; arXiv RSS; VBench leaderboard scraper | ReAct (poll leaderboards → detect change → alert) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 81 | **AnalystAgent** | Aggregates business, creative, and technical performance telemetry into decision-ready reports | Platform analytics dashboards; experiment logs; evaluation-harness outputs; benchmark histories | KPI completeness; forecast-vs-actual variance within tolerance; insight-to-action turnaround | Detects actionable performance shifts faster than human analyst rotations | SocialMediaStrategistAgent, PerformanceMarketerAgent, EvaluationHarnessAgent | Campaign pacing, release timing, retention and ROAS anomalies | YouTube Analytics, Meta/TikTok Ads dashboards, BI warehouse, benchmark logs | ReAct over telemetry + regression analysis |
| 82 | **AudienceSimAgent** | Simulates audience preference, engagement, and drop-off | Pairwise preference datasets; retention studies; audience segmentation models | Preference stability across cohorts; retention-prediction accuracy; disagreement logging | Predicts audience reaction earlier than conventional test-screen cycles | DirectorAgent, EditorAgent, AnalystAgent, JudgeAgent | Hooks, pacing, clarity, emotional fit, trailer strength | Persona simulators, pairwise evaluation harness, retention models | LLM-as-Judge + pairwise preference panel |
| 83 | **AccessibilityAgent** | Owns final accessibility acceptance before release | WCAG 2.2, captioning and AD guidelines, Deaf/HoH review frameworks | Caption accuracy, AD completeness, contrast compliance, release-readiness | Finds release-blocking accessibility issues before human audits do | AccessibilityOptimizerAgent, EditorAgent, ColoristAgent, SoundMixerAgent | Caption sync, contrast issues, missing AD or sign-language layers | Caption validators, contrast analyzers, AD review tools | Constitutional AI with accessibility constitution |
| 84 | **BrandAgent** | Enforces brand voice, claims boundaries, and visual consistency | Brand books, approved campaigns, legal claim guardrails, tone guides | Brand-voice similarity, policy adherence, low deviation across assets | Holds cross-channel brand consistency better than fragmented human review | CopywriterAgent, MotionGraphicsAgent, MarketingAgent, BrandStrategistAgent | Voice drift, visual inconsistency, claim creep | Brand asset library, embedding similarity, style guides | Self-Refine against brand constitution |
| 85 | **BrandSt
…



### From `corpus/study/ui/architecture_communication.md` Copy: `sources/excerpts/architecture_communication.md`.


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



### From `corpus/study/ui/backend_agent_management.md` Copy: `sources/excerpts/backend_agent_management.md`.


```python
# When an agent publishes an artifact:
def on_artifact_created(event):
    producer_agent = agents[event.agent_id]

for critic in critics:
        # Only deliver if the producer accepts critique from this critic
        if critic.agent_id in producer_agent.accepts_critique_from:
            enqueue_critique_task(
                critic_agent=critic.agent_id,
                artifact=event.artifact_id,
                producer_agent=event.agent_id
            )
```



### From `corpus/study/ui/ui_design.md` Copy: `sources/excerpts/ui_design.md`.


| Persona | Needs |
|---------|-------|
| **Creator** | Start production fast, review outputs, approve gates |
| **Producer** | Monitor budget/schedule, resolve escalations, manage team |
| **Technical Operator** | Tune prompts, inspect agent logs, manage model routing |
| **Reviewer/Client** | View deliverables, leave feedback, approve final |

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



## Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


## Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


## Provenance

- Master roster row va_id=2 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `vendor/va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.producer · va_id=2 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **ProducerAgent / EP** (`video.producer`, va_id=2, category `1-ATL`).

### Responsibility focus
Budget, schedule, hiring, delivery; greenlights phase gates

### Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: AI production management, budget-aware agent systems, schedule optimization, greenlight decision agents
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI producers, automated production management, media project ops
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: AI for producers, production scheduling automation, media ops with agents

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

<!-- migration_capability_research · video.producer · v1 · 2026-07-13 -->

### `sources/generic/video.productiondesign.SPEC.md`

# ProductionDesignAgent

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 16 |
| **pack_id** | `video.productiondesign` |
| **category** | `3-Edit` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.productiondesign/` |

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

Sets, locations, world look

## Knowledge distillation sources

ADG Awards; AMPAS submissions; Beachler/Carter talks

## Self-quality criteria

Period accuracy; palette coherence; build feasibility

## Surpass-human signal

Wins ADG blind comparisons on period-research depth

## Critique bus

- **Accepts critique from:** DirectorAgent, DoPAgent

- **Comments on:** ConceptArtistAgent (style break), CostumeAgent

## Tools (design-time documentation)

Unreal Engine (virtual scouting); Veo 3.1 location gen; archival image search APIs

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

Reflexion (stores period-research corrections in memory)

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

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From / How | Comments On (Critiques) |
|---|-------|----------------|-------------------------------|-----------------------|----------------------|-----------------------------|--------------------------|
| 59 | **IdeationAgent** | Divergent brainstorm of concepts, hooks, taglines, what-if angles | Cannes Lions Grand Prix archive; D&AD winners; IDEO design-thinking corpus; SCAMPER / Lateral Thinking (de Bono) | Idea-count per brief; novelty (embedding distance from corpus); semantic diversity within batch | Wins blind agency-pitch shootouts on first-round concept density | CreativeDirectorAgent, NoveltyAgent | CopywriterAgent (derivative), DirectorAgent (unfilmable) |
| 60 | **NarrativeArcAgent** | Shapes 3-act / Save-the-Cat / Kishōtenketsu / Hero's Journey structure | Campbell *Hero with a Thousand Faces*; Snyder *Save the Cat*; Truby *Anatomy of Story*; Black List structural analyses | Beat-sheet coverage 100%; turning-point spacing matches genre prior; emotional-arc curve fit | Beats WGA-staffed first drafts on structural-rubric blind reads | ScreenwriterAgent, DirectorAgent | ScreenwriterAgent (sagging middle) |
| 61 | **StyleTransferAgent** | Applies named aesthetic (Wes Anderson, A24, cyberpunk, vaporwave, Studio Ghibli, etc.) consistently across shots | Curated style corpora per look; LoRA/seed registries; reference-frame banks | Style-similarity score (CLIP/DINO) ≥0.85 to reference; consistency variance across shots ≤τ | Wins blind preference vs human colorist+grader doing same look | DirectorAgent, ColoristAgent | GeneratorAgent (off-style), ColoristAgent (palette drift) |
| 62 | **WorldBuildingAgent** | Builds lore, rules, geography, factions, magic/tech systems for series & franchises | Tolkien legendarium; *Worldbuilding* (Adams); fan-wiki corpora; series-bible leaks | Internal-consistency check (no contradictions across N entries); rule-completeness | Lower contradiction rate than human writers'-room bibles at 10× volume | ShowrunnerAgent, FactCheckerAgent | ScreenwriterAgent (lore break), ConceptArtistAgent |
| 63 | **MoodBoardAgent** | Builds reference boards: visual, sonic, tonal | Pinterest/Are.na corpora; lookbook archives; Spotify-Canvas references | Reference coherence (cluster tightness); brief alignment | Faster + tighter boards than human art director in blind A/B | DirectorAgent, ProductionDesignAgent | ConceptArtistAgent (off-mood) |
| 64 | **NoveltyAgent / Anti-Cliché Critic** | Flags tropes, clichés, and over-fit-to-corpus outputs | TV Tropes; OpenSubtitles n-gram frequency; corpus-novelty embeddings | Cliché-hit count per output; novelty score relative to category prior | Catches more clichés than experienced script editor in blind eval | IdeationAgent, ScreenwriterAgent | ScreenwriterAgent (trope-stuffed), CopywriterAgent (templated) |
| 65 | **EmotionalArcAgent** | Maps valence/arousal curve across runtime; suggests beats | Plutchik emotion wheel; affective-computing corpora; *Story Genius* (Cron) | Curve-fit to target shape; viewer-biosignal-proxy regression accuracy | Better retention-curve prediction than test-screening NRG cards | DirectorAgent, EditorAgent, ComposerAgent | EditorAgent (flat middle), ComposerAgent (cue mismatch) |

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Development | ScreenwriterAgent + ProducerAgent + DirectorAgent + ConceptArtistAgent + CastingAgent | LegalAgent (IP, consent) |
| Pre-Production | StoryboardAgent + ProductionDesignAgent + CostumeAgent + ContinuityAgent | DirectorAgent |
| Production | PromptEngineerAgent / GeneratorOperator (pool) + VoiceCloneAgent + LipSyncAgent + ComposerAgent | AIQAConsistencyAgent + AvatarDesignAgent |
| Post | EditorAgent + VFXSupervisorAgent + ColoristAgent + SoundMixerAgent | DirectorAgent |
| Review | DirectorAgent + AudienceSimAgent + MPAAgent + LegalAgent (C2PA) | EthicsAgent |
| Distribution | SalesAgent + DistributorAgent + TrailerEditorAgent + MarketingAgent + ArchiveMasterAgent | ComplianceAgent |
| Post-launch | AnalystAgent + AwardsStrategistAgent + CriticAgent (festival/press sim) | ProducerAgent |



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

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 59 | **IdeationAgent** | Divergent brainstorm of concepts, hooks, taglines | Cannes Grand Prix; D&AD; IDEO design-thinking; SCAMPER/de Bono | Idea-count; novelty (embedding distance); semantic diversity | Wins agency-pitch shootouts on concept density | CreativeDirectorAgent, NoveltyAgent | CopywriterAgent (derivative), DirectorAgent (unfilmable) | Embedding novelty scorer; concept clustering (UMAP); Are.na/Pinterest search | Self-Refine + NoveltyAgent as critic |
| 60 | **NarrativeArcAgent** | 3-act / Save-the-Cat / Hero's Journey structure | Campbell; Snyder *Save the Cat*; Truby; Black List analyses | Beat-sheet coverage 100%; turning-point spacing; arc curve fit | Beats WGA first drafts on structural rubric | ScreenwriterAgent, DirectorAgent | ScreenwriterAgent (sagging middle) | Beat-sheet validator; emotional-arc plotter; structure templates | Self-Refine (rubric: beat-sheet completeness) |
| 61 | **StyleTransferAgent** | Applies named aesthetic consistently across shots | Curated style corpora; LoRA/seed registries; reference-frame banks | Style-similarity (CLIP/DINO) ≥0.85; cross-shot variance ≤τ | Wins blind preference vs human colorist+grader | DirectorAgent, ColoristAgent | GeneratorAgent (off-style) | LoRA weights per style; CLIP/DINO similarity scorer; Runway style-lock mode; ComfyUI | Self-Refine (CLIP style score as feedback) |
| 62 | **WorldBuildingAgent** | Lore, rules, geography, factions, magic/tech systems | Tolkien; *Worldbuilding* (Adams); fan-wikis; series-bible leaks | Internal-consistency (no contradictions); rule-completeness | Lower contradiction rate than writers' bibles at 10× volume | ShowrunnerAgent, FactCheckerAgent | ScreenwriterAgent (lore break), ConceptArtistAgent | Long-context LLM (Gemini 2.5 Pro); contradiction-detection model; wiki-graph DB | Reflexion (contradiction corrections → episodic memory) |
| 63 | **MoodBoardAgent** | Reference boards: visual, sonic, tonal | Pinterest/Are.na; lookbook archives; Spotify-Canvas | Reference coherence (cluster tightness); brief alignment | Faster + tighter boards than art director (blind A/B) | DirectorAgent, ProductionDesignAgent | ConceptArtistAgent (off-mood) | Pinterest/Are.na APIs; Spotify Canvas; CLIP clustering; Figma board generation | ReAct (search → cluster → layout → validate coherence) |
| 64 | **NoveltyAgent / Anti-Cliché Critic** | Flags tropes, clichés, over-fit outputs | TV Tropes; OpenSubtitles n-gram freq; corpus-novelty embeddings | Cliché-hit count; novelty score vs category prior | Catches more clichés than experienced script editor | IdeationAgent, ScreenwriterAgent | ScreenwriterAgent (trope-stuffed), CopywriterAgent (templated) | TV Tropes scraper; n-gram frequency DB; embedding novelty scorer | LLM-as-Judge (anti-cliché constitution) |
| 65 | **EmotionalArcAgent** | Maps valence/arousal curve; suggests beats | Plutchik; affective-computing corpora; Cron *Story Genius* | Curve-fit to target; biosignal-proxy regression accuracy | Better retention prediction than NRG test-screening cards | DirectorAgent, EditorAgent, ComposerAgent | EditorAgent (flat middle), ComposerAgent (cue mismatch) | Sentiment/emotion classifiers (GoEmotions); retention-curve predictor; biosignal proxy model | Self-Refine (emotional-arc curve as rubric target) |



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



## Local binary assets in this agent folder

- `sources/study/common-agent-structure.svg` — common architecture diagram


## Host runtime binding

- **agent_spec.json** in this folder (ALC, tools, status)
- **standby_pool.json** — orchestrator-reachable
- **workflows/** — DNA JSON under `business/video/workflows/`
- **sources/** — copied related documents for offline use in this folder


## Provenance

- Master roster row va_id=16 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `vendor/va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.productiondesign · va_id=16 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **ProductionDesignAgent** (`video.productiondesign`, va_id=16, category `3-Edit`).

### Responsibility focus
Sets, locations, world look

### Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: generative set design, fashion/costume AI, makeup continuity, virtual production design
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI production design, costume AI, virtual sets
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: AI art direction for film, costume design AI, virtual production design

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

<!-- migration_capability_research · video.productiondesign · v1 · 2026-07-13 -->

### `sources/MAPPING.md`

# Mapping — `video.interviewsynthesis`

- VA/generic pack ID: `video.interviewsynthesis`
- Previous common ID: `video.location_manager`
- SPEC depth: full generic SPEC body + host runtime binding

### `sources/PROVENANCE.json`

```json
{
  "schema_version": "3.0",
  "sources": [
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
      "title": "\u65b0\u95fb\u7684\u5341\u5927\u57fa\u672c\u539f\u5219",
      "isbn13": "9787301161111",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u65b0\u95fb\u7684\u5341\u5927\u57fa\u672c\u539f\u5219\uff0cISBN-13 9787301161111"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u91c7\u8bbf\u7684\u827a\u672f",
      "isbn13": "9787301169186",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u91c7\u8bbf\u7684\u827a\u672f\uff0cISBN-13 9787301169186"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5982\u4f55\u9605\u8bfb\u4e00\u672c\u4e66",
      "isbn13": "9787100040945",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5982\u4f55\u9605\u8bfb\u4e00\u672c\u4e66\uff0cISBN-13 9787100040945"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u7814\u7a76\u662f\u4e00\u95e8\u827a\u672f",
      "isbn13": "9787300116226",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u7814\u7a76\u662f\u4e00\u95e8\u827a\u672f\uff0cISBN-13 9787300116226"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Thinking, Fast and Slow",
      "author": "Daniel Kahneman",
      "isbn13": "9780374533557",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Thinking, Fast and Slow (Daniel Kahneman), ISBN-13 9780374533557"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Influence",
      "author": "Robert Cialdini",
      "isbn13": "9780061241895",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Influence (Robert Cialdini), ISBN-13 9780061241895"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Predictably Irrational",
      "author": "Dan Ariely",
      "isbn13": "9780061353246",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Predictably Irrational (Dan Ariely), ISBN-13 9780061353246"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Nudge",
      "author": "Thaler & Sunstein",
      "isbn13": "9780143115267",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Nudge (Thaler & Sunstein), ISBN-13 9780143115267"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Flow",
      "author": "Mihaly Csikszentmihalyi",
      "isbn13": "9780061339202",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Flow (Mihaly Csikszentmihalyi), ISBN-13 9780061339202"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Drive",
      "author": "Daniel H. Pink",
      "isbn13": "9781594484803",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Drive (Daniel H. Pink), ISBN-13 9781594484803"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Mindset",
      "author": "Carol Dweck",
      "isbn13": "9780345472328",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Mindset (Carol Dweck), ISBN-13 9780345472328"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Power of Habit",
      "author": "Charles Duhigg",
      "isbn13": "9780812981605",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Power of Habit (Charles Duhigg), ISBN-13 9780812981605"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Emotional Intelligence",
      "author": "Daniel Goleman",
      "isbn13": "9780553383713",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Emotional Intelligence (Daniel Goleman), ISBN-13 9780553383713"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Personality",
      "author": "Daniel Nettle",
      "isbn13": "9780199211425",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Personality (Daniel Nettle), ISBN-13 9780199211425"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u601d\u8003\uff0c\u5feb\u4e0e\u6162",
      "isbn13": "9787508633565",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u601d\u8003\uff0c\u5feb\u4e0e\u6162\uff0cISBN-13 9787508633565"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5f71\u54cd\u529b",
      "isbn13": "9787508622163",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5f71\u54cd\u529b\uff0cISBN-13 9787508622163"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u602a\u8bde\u884c\u4e3a\u5b66",
      "isbn13": "9787508615824",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u602a\u8bde\u884c\u4e3a\u5b66\uff0cISBN-13 9787508615824"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u52a9\u63a8",
      "isbn13": "9787508641238",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u52a9\u63a8\uff0cISBN-13 9787508641238"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u5fc3\u6d41",
      "isbn13": "9787508660721",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u5fc3\u6d41\uff0cISBN-13 9787508660721"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u9a71\u52a8\u529b",
      "isbn13": "9787508621753",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u9a71\u52a8\u529b\uff0cISBN-13 9787508621753"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "\u793e\u4f1a\u5fc3\u7406\u5b66",
      "author": "\u8fc8\u5c14\u65af",
      "isbn13": "9787115412393",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: \u793e\u4f1a\u5fc3\u7406\u5b66\uff08\u8fc8\u5c14\u65af\uff09\uff0cISBN-13 9787115412393"
    }
  ],
  "agent_id": "video.interviewsynthesis",
  "previous_common_agent_id": "video.location_manager",
  "va_taxonomy_aligned": true,
  "generic_source": "generic-swarm-ops/business/video/agents/video.interviewsynthesis",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "aligned_at": "2026-07-27T00:48:11.173612Z",
  "generic_source_depth": {
    "excerpts": true,
    "study": true,
    "adopted_at": "2026-07-27T01:30:28.246190+00:00",
    "upstream": "generic-swarm-ops/business/video/agents"
  },
  "imported_from": "vendor/common-agent-swarm-ops/business/video/agents/video.interviewsynthesis",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```

### `sources/RETHINK_100_APPLIED.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.interviewsynthesis",
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
    73,
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
    "73": "Competitor video analysis",
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
  "agent_id": "video.interviewsynthesis",
  "sources": [
    {
      "id": "src_1",
      "title": "Otter/Rev transcripts",
      "description": "Otter/Rev transcripts",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.interviewsynthesis",
      "status": "planned_or_partial"
    },
    {
      "id": "src_2",
      "title": "consent forms",
      "description": "consent forms",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.interviewsynthesis",
      "status": "planned_or_partial"
    },
    {
      "id": "src_3",
      "title": "SAG/WGA templates",
      "description": "SAG/WGA templates",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.interviewsynthesis",
      "status": "planned_or_partial"
    }
  ],
  "note": "Legal review required before treating external corpora as production grounding."
}
```

### `sources/study/agentic_rag_functional_specification.md`

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
    relevance_score: float = Fie

…(clipped 7507 characters from `agentic_rag_functional_specification.md`)

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
