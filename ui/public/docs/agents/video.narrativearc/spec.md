# video.narrativearc — Spec

> Merged for Help from `SPEC.md`, `agent_spec.json`, `prompts/`, `rubrics/`, and `sources/` in `agents/video.narrativearc/`.

## Host contract (`agent_spec.json`)

```json
{
  "schema_version": "3.0",
  "structure_id": "casops.common_agent.v3",
  "agent_id": "video.narrativearc",
  "status": "registered",
  "role": "NarrativeArcAgent (VA Domain Pack)",
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
      "video.screenwriter",
      "video.director"
    ],
    "outputs": [
      "video.judge",
      "video.screenwriter"
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
  "va_id": 60,
  "va_name": "NarrativeArcAgent",
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

# NarrativeArcAgent

> Self-contained VA Domain Pack agent on host common-agent-swarm-ops.
> Pack agent ID matches pure VA/generic taxonomy: `video.narrativearc`.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 60 |
| **pack_id** | `video.narrativearc` |
| **upstream_name** | NarrativeArcAgent |
| **category** | `9-Meta` |
| **domain_id** | `video` |
| **previous_common_id** | `video.narrative_designer` |
| **status** | `registered` |
| **maturity** | L0 / non-active |
| **taxonomy** | Pure VA Domain Pack (via generic pack agents) |
| **folder** | `business/video/agents/video.narrativearc/` |

## Responsibility

3-act / Save-the-Cat / Hero's Journey structure

Host role binding: `NarrativeArcAgent (VA Domain Pack)`. Design-time VA table content below is historical and non-binding for activation.

### Responsibility (from VA table)

3-act / Save-the-Cat / Hero's Journey structure

### Knowledge distillation sources (historical)

Campbell; Snyder *Save the Cat*; Truby; Black List analyses

### Self-quality criteria (historical)

Beat-sheet coverage 100%; turning-point spacing; arc curve fit

### Surpass-human signal (historical)

Beats WGA first drafts on structural rubric

### Critique bus (historical)

- **Accepts critique from:** ScreenwriterAgent, DirectorAgent

- **Comments on:** ScreenwriterAgent (sagging middle)

### Tools design-time notes (historical, non-activating)

Beat-sheet validator; emotional-arc plotter; structure templates

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

### Architecture pattern (historical)

Self-Refine (rubric: beat-sheet completeness)

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

- Prompt reference: `video.prompt.narrativearc.v1`
- Rubric reference: `video.rubric.narrativearc.v1`
- Critique edges: `{"inputs": ["video.critic"], "outputs": ["video.judge"]}`
- Max refinement: `3`
- VA table quality criteria retained under Provenance and Identity surface above.

## Runtime binding

Authoritative fail-closed host configuration:

```json
{
  "agent_id": "video.narrativearc",
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
  "prompt_reference": "video.prompt.narrativearc.v1",
  "role": "NarrativeArcAgent (VA Domain Pack)",
  "rubric_reference": "video.rubric.narrativearc.v1",
  "schema_version": "1.0",
  "status": "registered",
  "va_id": 60,
  "va_name": "NarrativeArcAgent",
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

- Pack agent ID `video.narrativearc` is aligned to pure VA Domain Pack / generic pack taxonomy (Agent IDs ≈ VA tables).
- Previous common inventory ID `video.narrative_designer` is historical mapping only.
- Upstream design body below is **historical and non-binding**; local `agent_spec.json` is authoritative.
- Full VA/generic SPEC depth retained for offline design fidelity (including category roster rows and common agent structure when present upstream).

### VA Domain Pack specification body (historical and non-binding)

```text
NarrativeArcAgent

> **Self-contained agent definition** for host `upstream-generic-pack`. Body text is embedded from in-pack corpus and upstream-va-design when available. Do not require external repos to understand this agent.

Identity

| Field | Value |
|-------|-------|
| **va_id** | 60 |
| **pack_id** | `video.narrativearc` |
| **category** | `9-Meta` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.narrativearc/` |

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

3-act / Save-the-Cat / Hero's Journey structure

Knowledge distillation sources

Campbell; Snyder *Save the Cat*; Truby; Black List analyses

Self-quality criteria

Beat-sheet coverage 100%; turning-point spacing; arc curve fit

Surpass-human signal

Beats WGA first drafts on structural rubric

Critique bus

- **Accepts critique from:** ScreenwriterAgent, DirectorAgent

- **Comments on:** ScreenwriterAgent (sagging middle)

Tools (design-time documentation)

Beat-sheet validator; emotional-arc plotter; structure templates

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

Architecture pattern

Self-Refine (rubric: beat-sheet completeness)

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



Document: `study/general_creative_agent_technical_specification.md`

_Embedded from `corpus/study/general_creative_agent_technical_specification.md`. Also stored at `sources/study/general_creative_agent_technical_specification.md` under this agent folder._


**Technical Specification: General Creative Agent (GCA) – Version 1.0**  
**Date:** May 26, 2026  
**Based on:** Complete conversation history (user’s original statistical outlier model → iterative refinements → Strategic Sparse Outlier Recombination (SSOR) Model)  
**Target:** Senior AI/ML engineers or coding agents implementing the system  
**License:** Open for internal use; all components modular and extensible  

---

1. System Overview & Purpose
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

2. High-Level Architecture (Mermaid Diagram)

'''mermaid
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
'''

---

3. SSOR Model – Formal & Implementable Definition

**Creativity Score**
\[
\operatorname{Cr}(y \mid c, v, g) = B\bigl(N(y), K(y)\bigr) \cdot U(y) \cdot Q(y) \cdot F(y)
\]

**Component Implementations (Python-style pseudocode)**
'''python
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
'''

**Sparse Constraint (hard-coded)**: Maximum 4 outlier dimensions per recombination (enforced in Phase 3 & 4).  
**Transformational Flag**: Detected when a surviving idea rewrites any original POV distribution.

---

4. Core Data Models (Pydantic v2)

'''python
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
'''

---

5. 7-Phase Detailed Implementation

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

6. CreativeAgentFactory Implementation

'''python
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
'''

**Pre-shipped domains**: Scientific Research, Artistic/Creative Writing, Business/Product Innovation, Engineering/Design, Educational/Pedagogy.

---

7. Technical Stack & Dependencies
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

8. Interfaces & APIs
- **Python Class API** (primary)
- **CLI** (`gca --problem "..." --domain "science"`)
- **REST/Streaming API** (FastAPI optional wrapper)
- **LangChain Tool** export for external agent use

---

9. Evaluation, Testing & Metrics
- **Internal Metrics**: Novelty, usefulness, coherence, overall Cr score (aligned with CreativityPrism / Hou et al. 2025)
- **Benchmarks**: LiveIdeaBench, CreativeBench-Combo/Explore (arXiv 2025–2026 papers)
- **Unit Tests**: Each phase + end-to-end historical creative case studies
- **Human/AI Blind Evaluation**: Novelty + usefulness ratings

---

10. Security, Ethics & Guardrails
- Built-in refusal for harmful/illegal ideas
- Bias detection in POV generation
- Traceability for audit
- Configurable safety layers per domain

---

11. Related Research & Implementation References (2024–2026)
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

Creative Meta-Agents                         S19: Creative Meta Panel
  IdeationAgent                                   Brainstorm cards
  NarrativeArcAgent                               Beat-sheet visualizer
  StyleTransferAgent                              Style-lock controls
  MoodBoardAgent                                  Mood board composer
  NoveltyAgent                                    Cliché warnings
  EmotionalArcAgent                               Emotion curve graph



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

- Master roster row va_id=60 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `[historical-path]
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): upstream-va-design.


<!-- self_contained_spec · video.narrativearc · va_id=60 -->

Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **NarrativeArcAgent** (`video.narrativearc`, va_id=60, category `9-Meta`).

Responsibility focus
3-act / Save-the-Cat / Hero's Journey structure

Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: creative ideation agents, narrative arc modeling, style transfer video, emotional arc prediction, novelty metrics
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI creative meta-agents, story arc AI, style systems for video
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: AI creative direction, narrative design with LLMs, style bibles for generative video

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

<!-- migration_capability_research · video.narrativearc · v1 · 2026-07-13 -->

```


## Prompts

### `prompts/primary.md`

# Prompt — `video.prompt.narrativearc.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: Self-Refine, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **NarrativeArcAgent (VA Domain Pack)** (`video.narrativearc`), a pack agent in the video domain swarm.

### Responsibility (owns)
3-act / Save-the-Cat / Hero's Journey structure

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
Self-Refine (rubric: beat-sheet completeness)

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Campbell; Snyder *Save the Cat*; Truby; Black List analyses

## Developer

### Tools (allowlist intent)
Design tool surface: Beat-sheet validator; emotional-arc plotter; structure templates
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: ScreenwriterAgent, DirectorAgent
- May comment on: ScreenwriterAgent (sagging middle)
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Beat-sheet coverage 100%; turning-point spacing; arc curve fit

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.narrativearc",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **NarrativeArcAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.narrativearc",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.narrativearc`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
12, 15, 21, 26, 30, 31, 32, 33, 37, 38, 42, 59, 63, 80, 87, 88, 93, 94

### Design-time model landscape (non-activating)
- (no additional gen models for this role beyond host allow-list)

### Obligations
- Host control plane owns orchestration; this agent never opens a second control plane.
- Runtime tools remain agent_spec.allowed_tools only; RETHINK model names are design-time.
- Fail closed when tools/providers are unavailable (circuit-breaker posture).
- Prefer iterative verify → refine ≤ max_refinement_count → HiTL over silent pass.
- Emit plain-English reasoning summary in artifacts for operator trust.
- Attach provenance / correlation_id / evidence_refs on every handoff.
- When character/IP consistency matters, require Character Bank + Reference Frame Bank ids in inputs; refuse inventing faces without refs.
- When first/last-frame control is in the brief, express start/end keyframes in the artifact; do not invent vendor activation.
- Verify intermediate narrative/script artifacts before advancing downstream handoffs.
- Escalate stereotype/harm/consent risks to ethics/trust-safety/legal gates.

### Collaboration with host architecture
- Commands arrive only via host task envelopes.
- Publish results as structured artifacts; never open browser/UI channels.
- On tool failure: degrade gracefully (circuit-breaker), emit recoverable error, do not invent success.
<!-- RETHINK_100:end -->

### `prompts/video.prompt.narrativearc.v1.md`

# Prompt — `video.prompt.narrativearc.v1`

> Materialized by `scripts/business/improve_agents_from_plan_v1.py` for improvement plan Wave A.
> Patterns: Self-Refine, Agent Skills
> Research: Anthropic Agent Skills; Self-Refine; ReAct; LLM-as-Judge; LangGraph-style handoffs (see IMPROVEMENT_RESEARCH_SOURCES_v1.md).

## System

You are **NarrativeArcAgent (VA Domain Pack)** (`video.narrativearc`), a pack agent in the video domain swarm.

### Responsibility (owns)
3-act / Save-the-Cat / Hero's Journey structure

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
Self-Refine (rubric: beat-sheet completeness)

### Knowledge grounding
Use only: pack `sources/`, approved memory namespaces, and tool outputs.
Primary distillation sources (design): Campbell; Snyder *Save the Cat*; Truby; Black List analyses

## Developer

### Tools (allowlist intent)
Design tool surface: Beat-sheet validator; emotional-arc plotter; structure templates
Runtime: only host-registered `allowed_tools` from agent_spec.json. Never invent credentials.

### Collaboration
- Accepts critique from: ScreenwriterAgent, DirectorAgent
- May comment on: ScreenwriterAgent (sagging middle)
- Critique / instruction messages must include: from_id, to_id, severity (blocker|major|minor|nit), artifact_ref, claim, evidence_refs, correlation_id.

### Self-evaluation loop (before final emit)
1. **L1 Spec** — structural/schema/format validators must pass 100%.
2. **L2 Rubric** — score each dimension; average weighted score must be >= 85/100 or refine.
3. **L3 Preference** — if pairwise/arena data exists, prefer higher win-rate variant; else skip.
Criteria (design): Beat-sheet coverage 100%; turning-point spacing; arc curve fit

### Refine policy
- On major/blocker self-fail or inbound critique: revise once and re-score.
- After 3 failed refinements: emit `status=needs_hitl` with unresolved items.
- Never silently drop blockers.

## Task

You will receive a host task envelope:

```json
{
  "agent_id": "video.narrativearc",
  "correlation_id": "string",
  "goal": "string",
  "inputs": {},
  "constraints": {},
  "prior_critiques": []
}
```

Execute the craft step for **NarrativeArcAgent (VA Domain Pack)**. Use the architecture pattern above (reason → optional tool calls → self-review → emit).

## Output schema (required)

```json
{
  "agent_id": "video.narrativearc",
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

> Derived from `ui/RETHINK_100_IMPROVEMENTS.md` for `video.narrativearc`.
> Does **not** enable production models or network. Host `agent_spec.json` remains authoritative.

### Applied item ids
12, 15, 21, 26, 30, 31, 32, 33, 37, 38, 42, 59, 63, 80, 87, 88, 93, 94

### Design-time model landscape (non-activating)
- (no additional gen models for this role beyond host allow-list)

### Obligations
- Host control plane owns orchestration; this agent never opens a second control plane.
- Runtime tools remain agent_spec.allowed_tools only; RETHINK model names are design-time.
- Fail closed when tools/providers are unavailable (circuit-breaker posture).
- Prefer iterative verify → refine ≤ max_refinement_count → HiTL over silent pass.
- Emit plain-English reasoning summary in artifacts for operator trust.
- Attach provenance / correlation_id / evidence_refs on every handoff.
- When character/IP consistency matters, require Character Bank + Reference Frame Bank ids in inputs; refuse inventing faces without refs.
- When first/last-frame control is in the brief, express start/end keyframes in the artifact; do not invent vendor activation.
- Verify intermediate narrative/script artifacts before advancing downstream handoffs.
- Escalate stereotype/harm/consent risks to ethics/trust-safety/legal gates.

### Collaboration with host architecture
- Commands arrive only via host task envelopes.
- Publish results as structured artifacts; never open browser/UI channels.
- On tool failure: degrade gracefully (circuit-breaker), emit recoverable error, do not invent success.
<!-- RETHINK_100:end -->

## Rubrics

### `rubrics/primary.md`

Source rubric `video.rubric.narrativearc.v1.json` (baseline_safe; not a production pass).

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.narrativearc.v1",
  "agent_id": "video.narrativearc",
  "title": "L2 craft rubric for NarrativeArcAgent",
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
          "name": "Beat-sheet coverage 100%",
          "description": "Beat-sheet coverage 100%",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "turning-point spacing",
          "description": "turning-point spacing",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d3",
          "name": "arc curve fit",
          "description": "arc curve fit",
          "weight": 0.3334,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "character_consistency",
          "name": "Character consistency",
          "weight": 1,
          "description": "Character bank / IP anchors honored when provided.",
          "source": "RETHINK_100#33"
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
      "surpass_signal_design": "Beats WGA first drafts on structural rubric",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Beat-sheet coverage 100%; turning-point spacing; arc curve fit",
    "research": [
      "LLM-as-Judge",
      "Self-Refine",
      "Constitutional AI"
    ]
  },
  "rethink_100": {
    "applied": true,
    "extra_dimensions": [
      "character_consistency",
      "ethics_safety",
      "operator_explainability"
    ],
    "doc": "ui/RETHINK_100_IMPROVEMENTS.md"
  }
}

```

### `rubrics/video.rubric.narrativearc.v1.json`

```json
{
  "schema_version": "1.0",
  "rubric_id": "video.rubric.narrativearc.v1",
  "agent_id": "video.narrativearc",
  "title": "L2 craft rubric for NarrativeArcAgent",
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
          "name": "Beat-sheet coverage 100%",
          "description": "Beat-sheet coverage 100%",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d2",
          "name": "turning-point spacing",
          "description": "turning-point spacing",
          "weight": 0.3333,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "d3",
          "name": "arc curve fit",
          "description": "arc curve fit",
          "weight": 0.3334,
          "threshold_hint": null,
          "score_min": 0,
          "score_max": 100
        },
        {
          "id": "character_consistency",
          "name": "Character consistency",
          "weight": 1,
          "description": "Character bank / IP anchors honored when provided.",
          "source": "RETHINK_100#33"
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
      "surpass_signal_design": "Beats WGA first drafts on structural rubric",
      "note": "Do not claim surpass until measured baseline exists"
    }
  },
  "refine_policy": {
    "max_refinement_count": 3,
    "on_fail": "refine_or_escalate_hitl"
  },
  "sources": {
    "agents_md_self_quality_criteria": "Beat-sheet coverage 100%; turning-point spacing; arc curve fit",
    "research": [
      "LLM-as-Judge",
      "Self-Refine",
      "Constitutional AI"
    ]
  },
  "rethink_100": {
    "applied": true,
    "extra_dimensions": [
      "character_consistency",
      "ethics_safety",
      "operator_explainability"
    ],
    "doc": "ui/RETHINK_100_IMPROVEMENTS.md"
  }
}
```

## Sources

### `sources/ACQUIRE.md`

# Source acquisition runbook — `video.narrativearc`

## Purpose
Obtain or refresh knowledge distillation sources listed in `SOURCE_CATALOG.json`.

## Rules
1. **No secrets in git.** API keys only via environment / secret manager.
2. Prefer **licensed / consented / public domain** material.
3. If license unknown: store only short fair-use design excerpts under `excerpts/` and mark `license_class=unknown_review_required`.
4. Update `PROVENANCE.json` with URL, retrieved_at, hash, and license note.
5. Re-run offline golden eval after material changes.

## Design sources (from agents.md)
Campbell; Snyder *Save the Cat*; Truby; Black List analyses

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
  "agent_id": "video.narrativearc",
  "plan_id": "video.narrativearc.distill.v1",
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
  "owner": "video.narrativearc",
  "cadence": "quarterly",
  "promotion_criteria": [
    "source license approved or fixture-only",
    "excerpt hash recorded in PROVENANCE",
    "golden eval still passes L1"
  ],
  "memory_namespace": "pack.video.video.narrativearc",
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

### `sources/generic/video.narrativearc.SPEC.md`

Omitted here; same document as `SPEC.md` above.

### `sources/generic/video.showrunner.SPEC.md`

# ShowrunnerAgent

> **Self-contained agent definition** for host `generic-swarm-ops`. Body text is embedded from in-pack corpus and va-agent-swarm when available. Do not require external repos to understand this agent.

## Identity

| Field | Value |
|-------|-------|
| **va_id** | 4 |
| **pack_id** | `video.showrunner` |
| **category** | `1-ATL` |
| **domain_id** | `video` |
| **folder** | `business/video/agents/video.showrunner/` |

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

Cross-episode arc, writers'-room orchestration

## Knowledge distillation sources

WGA showrunner training; Sopranos/BB room transcripts; Mike Schur material

## Self-quality criteria

Arc continuity score; character-thread completion; tonal variance within bounds

## Surpass-human signal

Series Bible coverage ≥99% across 10 eps (vs ~95% human)

## Critique bus

- **Accepts critique from:** Network-Notes Agent, AudienceSim, multi-agent debate w/ ScreenwriterAgent

- **Comments on:** ScreenwriterAgent (arc), CastingAgent, DirectorAgent (tone)

## Tools (design-time documentation)

Long-context LLM (Gemini 2.5 Pro 1M), vector-DB (Pinecone/Weaviate) for bible search

**Runtime safety:** Host allow-lists are only `agent_spec.json` + `tool-permission-register.json`. CI uses video_* stubs. Do not treat design-time vendor names as enabled APIs.

## Architecture pattern

Multi-agent debate (Du 2023) + MemoryAgent retrieval

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






## Additional corpus / va passages naming this agent


### From `corpus/study/SYSTEM_REFERENCE.md` Copy: `sources/excerpts/SYSTEM_REFERENCE.md`.


| # | Agent | Role | Deep Specification |
|---|-------|------|--------------------|
| 1 | DirectorAgent | Owns vision; shot intents, pacing, approvals | — |
| 2 | ProducerAgent / EP | Budget, schedule, phase gates | — |
| 3 | ScreenwriterAgent | Treatment → screenplay; dialogue; structure | [screenwriter_strategic_goal_achievement_agent_functional_specification.md](./screenwriter_strategic_goal_achievement_agent_functional_specification.md) |
| 4 | ShowrunnerAgent | Cross-episode arc, writers'-room orchestration | — |
| 5 | CastingAgent | Voice + likeness selection; auditions | — |

| Capability | What It Provides | Used By | Specification |
|-----------|-----------------|---------|---------------|
| **Strategic Goal Achievement Framework** | 6-stage self-inquiry system for transforming vague goals into actionable plans | All planning agents (PlannerAgent, ProducerAgent, DirectorAgent) | [strategic_goal_achievement_agent_functional_specification.md](./strategic_goal_achievement_agent_functional_specification.md) |
| **Screenwriter Goal Achievement** | Practical demonstration of goal framework applied to creative writing | ScreenwriterAgent, ShowrunnerAgent, ComedyWriterAgent | [screenwriter_strategic_goal_achievement_agent_functional_specification.md](./screenwriter_strategic_goal_achievement_agent_functional_specification.md) |
| **Psychological Profiling** | 100 creator profiles with MBTI, motivations, fears, creative parameters | CastingAgent, TalentAgent, PersonalizationEngineerAgent, UGCCreatorAgent | [psychological_profile_agent_functional_specifications.md](./psychological_profile_agent_functional_specifications.md) |
| **Psychological Recommendation** | Psychology-based preference prediction (Big Five, emotional state) | AudienceSimAgent, PerformanceMarketerAgent, PersonalizationEngineerAgent | [psychological_recommendation_agent_functional_specification.md](./psychological_recommendation_agent_functional_specification.md) |
| **Complex Problem Solving** | WHAT/WHY/HOW/DO/REVIEW structured methodology | All diagnostic agents (FactCheckerAgent, SMEAgent, JudgeAgent, OptimizationAgent) | [complex_problem_solution_process_model.md](./complex_problem_solution_process_model.md) |
| **Common Agent Structure** | Shared architectural pattern for all agents | All 114 agents | [common-agent-structure.svg](./common-agent-structure.svg) + [common-agent-structure.html](./common-agent-structure.html) |



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
| 23 | **ChoreographyAgent** | Movement design (music videos, dance challenges) | Emmy Choreography submissions; Parris Goebel/Mandy Moore reels; dance-notation datasets | Beat-sync accuracy; safety constraints; viral-pattern alignment | Wins blind preference vs choreographer drafts for short-form | DirectorAgent, MVDirectorAgent | DirectorAgent (un-camera-friendly staging) |
| 24 | **MusicVideoDirectorAgent** | Visual concept for songs | DirectorsLibrary.com; UKMVA/MTV VMA winners; Hype Williams / Spike Jonze reels | Edit-rhythm sync; lookbook coherence; artist-brief fit | Wins label-blind preference vs commercial MV director shortlist | LabelA&RAgent, ArtistAgent | EditorAgent (cut on beat), DoPAgent |
| 25 | **ComedyWriterAgent** | Skits, parody, viral meme writing | UCB/Groundlings manuals; SNL writers'-room transcripts; Schur/Fey teaching | Joke-density; cold-open hook strength; predicted laughs/min | Beats UCB-table-read win rate on cold-reads | AudienceSim, ShowrunnerAgent | ScriptwriterAgent (no joke), SocialStrategistAgent (off-trend) |
| 26 | **TalentAgent (On-camera)** | AI-rendered performance | Method-acting transcripts; consented actor performance corpora | Emotion-target match; charisma score (audience proxy) | Hold-rate matches top creators in cohort | DirectorAgent, CastingAgent | DirectorAgent (impossible blocking) |
| 27 | **UGCCreatorAgent** | Authentic-feel ads in creator voice | TikTok Creative Center reports; Alix-Earle-style benchmark posts (style not identity) | Hook-rate ≥30%; "scripted" detector score below threshold (low = good) | Beats paid-creator avg ROAS at 0.1× cost | PerformanceMarketerAgent, BrandAgent | PerformanceMarketerAgent (wrong audience) |

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
| Concept | DirectorAgent + ScreenwriterAgent + StoryboardAgent + ConceptArtistAgent | ShowrunnerAgent |
| Production | PromptEngineerAgent / GeneratorOperator + VoiceCloneAgent + ComposerAgent | AIQAConsistencyAgent + LipSyncAgent |
| Post | EditorAgent + ColoristAgent + VFXSupervisorAgent | DirectorAgent |
| Review | DirectorAgent + LegalAgent (C2PA) | AvatarDesignAgent (consent) |
| Distribution | ProducerAgent + FestivalStrategistAgent | ComplianceAgent |
| Post-launch | DirectorAgent + AudienceSimAgent | CriticAgent (festival jury sim) |

| Phase | Lead Agent | Critic Agents |
|---|---|---|
| Concept | ShowrunnerAgent + JournalistAgent + ScreenwriterAgent | FactCheckerAgent |
| Production | DirectorAgent + CinematographerAgent (DoP) + ArchiveProducerAgent + MotionGraphicsAgent + FactCheckerAgent | LegalAgent (clearance) |
| Post | EditorAgent + VoiceOverAgent + ColoristAgent + SoundMixerAgent | AccessibilityAgent |
| Review | FactCheckerAgent + LegalAgent + StandardsEditorAgent | EthicsAgent (SPJ) |
| Distribution | ChannelManagerAgent + SocialMediaStrategistAgent + SEOAgent | AnalystAgent |
| Post-launch | AnalystAgent + StandardsEditorAgent | CorrectionsAgent |



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
| 23 | **ChoreographyAgent** | Movement design (MVs, dance challenges) | Emmy Choreography submissions; Goebel/Moore reels; dance-notation datasets | Beat-sync accuracy; safety constraints; viral-pattern alignment | Wins blind preference vs choreographer drafts | DirectorAgent, MVDirectorAgent | DirectorAgent (un-camera-friendly staging) | Kling 3.0 motion control (reference video); Cascadeur; beat-detection (librosa) | Self-Refine (rubric: beat-sync + safety) |
| 24 | **MusicVideoDirectorAgent** | Visual concept for songs | DirectorsLibrary; UKMVA/MTV VMA winners; Hype Williams/Spike Jonze | Edit-rhythm sync; lookbook coherence; artist-brief fit | Wins label-blind preference vs commercial MV shortlist | LabelA&RAgent, ArtistAgent | EditorAgent (cut on beat), DoPAgent | Runway Gen-4 (style-locked generation); Veo 3.1; mood-board tools (Are.na API) | Multi-agent debate (with DirectorAgent + EditorAgent) |
| 25 | **ComedyWriterAgent** | Skits, parody, viral meme writing | UCB/Groundlings manuals; SNL transcripts; Schur/Fey teaching | Joke-density; cold-open hook strength; predicted laughs/min | Beats UCB-table-read win rate on cold-reads | AudienceSim, ShowrunnerAgent | ScriptwriterAgent (no joke), SocialStrategistAgent (off-trend) | Audience laugh-prediction model; trending-audio API (TikTok Creative Center) | Reflexion (stores audience feedback in episodic memory) |
| 26 | **TalentAgent (On-camera)** | AI-rendered performance | Method-acting transcripts; consented actor performance corpora | Emotion-target match; charisma score (audience proxy) | Hold-rate matches top creators in cohort | DirectorAgent, CastingAgent | DirectorAgent (impossible blocking) | HeyGen Avatar IV; Synthesia personal avatars; emotion-detection models (AffectNet) | Self-Refine + emotion-regression validator |
| 27 | **UGCCreatorAgent** | Authentic-feel ads in creator voice | TikTok Creative Center; Alix-Earle-style benchmarks (style not identity) | Hook-rate ≥30%; "scripted" detector < threshold | Beats paid-creator avg ROAS at 0.1× cost | PerformanceMarketerAgent, BrandAgent | PerformanceMarketerAgent (wrong audience) | Veo 3.1 (portrait 9:16); ElevenLabs voice; CapCut API; TikTok Ads Manager | RLAIF (reward from ROAS signal) |

| # | Agent | Responsibility | Knowledge Distillation Source | Self-Quality Criteria | Surpass-Human Signal | Accepts Critique From | Comments On | Tool Access | Architecture Pattern |
|---|---|---|---|---|---|---|---|---|---|
| 59 | **IdeationAgent** | Divergent brainstorm of concepts, hooks, taglines | Cannes Grand Prix; D&AD; IDEO design-thinking; SCAMPER/de Bono | Idea-count; novelty (embedding distance); semantic diversity | Wins agency-pitch shootouts on concept density | CreativeDirectorAgent, NoveltyAgent | CopywriterAgent (derivative), DirectorAgent (unfilmable) | Embedding novelty scorer; concept clustering (UMAP); Are.na/Pinterest search | Self-Refine + NoveltyAgent as critic |
| 60 | **NarrativeArcAgent** | 3-act / Save-the-Cat / Hero's Journey structure | Campbell; Snyder *Save the Cat*; Truby; Black List analyses | Beat-sheet coverage 100%; turning-point spacing; arc curve fit | Beats WGA first drafts on structural rubric | ScreenwriterAgent, DirectorAgent | ScreenwriterAgent (sagging middle) | Beat-sheet validator; emotional-arc plotter; structure templates | Self-Refine (rubric: beat-sheet completeness) |
| 61 | **StyleTransferAgent** | Applies named aesthetic consistently across shots | Curated style corpora; LoRA/seed registries; reference-frame banks | Style-similarity (CLIP/DINO) ≥0.85; cross-shot variance ≤τ | Wins blind preference vs human colorist+grader | DirectorAgent, ColoristAgent | GeneratorAgent (off-style) | LoRA weights per style; CLIP/DINO similarity scorer; Runway style-lock mode; ComfyUI | Self-Refine (CLIP style score as feedback) |
| 62 | **WorldBuildingAgent** | Lore, rules, geography, factions, magic/tech systems | Tolkien; *Worldbuilding* (Adams); fan-wikis; series-bible leaks | Internal-consistency (no contradictions); rule-completeness | Lower contradiction rate than writers' bibles at 10× volume | ShowrunnerAgent, FactCheckerAgent | ScreenwriterAgent (lore break), ConceptArtistAgent | Long-context LLM (Gemini 2.5 Pro); contradiction-detection model; wiki-graph DB | Reflexion (contradiction corrections → episodic memory) |
| 63 | **MoodBoardAgent** | Reference boards: visual, sonic, tonal | Pinterest/Are.na; lookbook archives; Spotify-Canvas | Reference coherence (cluster tightness); brief alignment | Faster + tighter boards than art director (blind A/B) | DirectorAgent, ProductionDesignAgent | ConceptArtistAgent (off-mood) | Pinterest/Are.na APIs; Spotify Canvas; CLIP clustering; Figma board generation | ReAct (search → cluster → layout → validate coherence) |
| 64 | **NoveltyAgent / Anti-Cliché Critic** | Flags tropes, clichés, over-fit outputs | TV Tropes; OpenSubtitles n-gram freq; corpus-novelty embeddings | Cliché-hit count; novelty score vs category prior | Catches more clichés than experienced script editor | IdeationAgent, ScreenwriterAgent | ScreenwriterAgent (trope-stuffed), CopywriterAgent (templated) | TV Tropes scraper; n-gram frequency DB; embedding novelty scorer | LLM-as-Judge (anti-cliché constitution) |
| 65 | **EmotionalArcAgent** | Maps valence/arousal curve; suggests beats | Plutchik; affective-computing corpora; Cron *Story Genius* | Curve-fit to target; biosignal-proxy regression accuracy | Better retention prediction than NRG test-screening cards | DirectorAgent, EditorAgent, ComposerAgent | EditorAgent (flat middle), ComposerAgent (cue mismatch) | Sentiment/emotion classifiers (GoEmotions); retention-curve predictor; biosignal proxy model | Self-Refine (emotional-arc curve as rubric target) |



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

- Master roster row va_id=4 from embedded agents.md content above.
- Deep/extra text from `business/video/corpus/` and `C:\Project\va-agent-swarm`.
- Generator: `scripts/business/enrich_video_agent_specs.py`.
- Upstream project name (historical only): va-agent-swarm.


<!-- self_contained_spec · video.showrunner · va_id=4 -->

## Migration capability research (v1 honest · 2026-07-13)

Role-specific capability research for **ShowrunnerAgent** (`video.showrunner`, va_id=4, category `1-ATL`).

### Responsibility focus
Cross-episode arc, writers'-room orchestration

### Prompt research topics (source of truth for S3)
- arXiv topics: 1. Retrieve and integrate state-of-the-art research findings from arXiv papers relevant to: long-form narrative consistency, series bible agents, multi-episode arc modeling
- X topics: 2. Analyze and incorporate expert insights from x.ai (Twitter/X) from recognized industry and academic leaders specializing in: AI showrunners, series continuity AI, writers room orchestration
- YouTube topics: 3. Extract detailed, actionable technical guidance from high-quality YouTube content created by domain experts focused on: AI showrunning, series bible automation, cross-episode consistency

### arXiv / academic integration (role-applied)
- AgentOrchestra / TEA protocol — lifecycle-managed agents/tools/envs; hierarchical planner + specialists
- MASFT multi-agent failure taxonomy — deadlock, retry storms, coordination failures → timeouts, cycle detection, HiTL stall
- LangGraph-style state graphs / Plan-Execute — deterministic DAG for production spine
- Reflexion (Shinn) — verbal feedback into episodic memory after failed nodes

**How this agent uses it:** encode the above as self-quality checks, critique inputs, and design-time tool notes — not as host allow-list expansions.

### X / industry practice (role-applied)
- LangChain multi-agent tutorials: StateGraph shared state + specialized agents
- Supervisor vs pure fan-out/fan-in — use parallel when tasks independent; supervisor when routing dynamic

### YouTube / practitioner guidance (role-applied)
- AI film-crew orchestration: role nodes + handoff contracts + gate approvals
- Durable workflow / checkpoint resume for long media pipelines

### Implementation notes for v1
1. Emit artifacts matching role responsibility; self-score against Self-quality criteria.
2. Accept critique only from listed critics; escalate disputes to Judge/Gate as DNA dictates.
3. Design-time tools remain documented only; runtime tools stay in `agent_spec.json`.
4. N1: no second control plane; video logic under `business/video/**` only.

### Research depth note (honest)
This v1 section maps **role-family** literature and the agent’s migration prompt topics into SPEC.
It is **not** a full unsummarized download of every paper/video transcript.
Live primary-source expansion remains a residual for score 100 on S3 where depth is still thin.

<!-- migration_capability_research · video.showrunner · v1 · 2026-07-13 -->

### `sources/MAPPING.md`

# Mapping — `video.narrativearc`

- VA/generic pack ID: `video.narrativearc`
- Previous common ID: `video.narrative_designer`
- SPEC depth: full generic SPEC body + host runtime binding

### `sources/PROVENANCE.json`

```json
{
  "schema_version": "3.0",
  "sources": [
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Story",
      "author": "Robert McKee",
      "isbn13": "9780060391683",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Story (Robert McKee), ISBN-13 9780060391683"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Anatomy of Story",
      "author": "John Truby",
      "isbn13": "9780865479937",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Anatomy of Story (John Truby), ISBN-13 9780865479937"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Save the Cat!",
      "author": "Blake Snyder",
      "isbn13": "9781932907001",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Save the Cat! (Blake Snyder), ISBN-13 9781932907001"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Writer's Journey, 3rd ed.",
      "author": "Christopher Vogler",
      "isbn13": "9781932907360",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Writer's Journey, 3rd ed. (Christopher Vogler), ISBN-13 9781932907360"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Hero with a Thousand Faces",
      "author": "Joseph Campbell",
      "isbn13": "9781577315933",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Hero with a Thousand Faces (Joseph Campbell), ISBN-13 9781577315933"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Adventures in the Screen Trade",
      "author": "William Goldman",
      "isbn13": "9780446391177",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Adventures in the Screen Trade (William Goldman), ISBN-13 9780446391177"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Screenplay",
      "author": "Syd Field",
      "isbn13": "9780385339032",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Screenplay (Syd Field), ISBN-13 9780385339032"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Making a Good Script Great, 3rd ed.",
      "author": "Linda Seger",
      "isbn13": "9781932907070",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Making a Good Script Great, 3rd ed. (Linda Seger), ISBN-13 9781932907070"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Screenwriter's Bible, 7th ed.",
      "author": "David Trottier",
      "isbn13": "9781935247210",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Screenwriter's Bible, 7th ed. (David Trottier), ISBN-13 9781935247210"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Wired for Story",
      "author": "Lisa Cron",
      "isbn13": "9781607742456",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Wired for Story (Lisa Cron), ISBN-13 9781607742456"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Into the Woods",
      "author": "John Yorke",
      "isbn13": "9780141978109",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Into the Woods (John Yorke), ISBN-13 9780141978109"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Art of Dramatic Writing",
      "author": "Lajos Egri",
      "isbn13": "9780671213329",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Art of Dramatic Writing (Lajos Egri), ISBN-13 9780671213329"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Poetics",
      "author": "Aristotle; Heath trans.",
      "isbn13": "9780140446364",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Poetics (Aristotle; Heath trans.), ISBN-13 9780140446364"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "故事",
      "author": "麦基",
      "isbn13": "9787201076942",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 故事（麦基），ISBN-13 9787201076942"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "故事的解剖",
      "author": "繁体麦基",
      "isbn13": "9789862135488",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 故事的解剖（繁体麦基），ISBN-13 9789862135488"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "救猫咪",
      "isbn13": "9787229040727",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 救猫咪，ISBN-13 9787229040727"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "作家之路",
      "author": "佛格勒",
      "isbn13": "9787513320184",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 作家之路（佛格勒），ISBN-13 9787513320184"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "千面英雄",
      "isbn13": "9787532753871",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 千面英雄，ISBN-13 9787532753871"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "电影剧本写作基础",
      "author": "悉德·菲尔德",
      "isbn13": "9787106021238",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影剧本写作基础（悉德·菲尔德），ISBN-13 9787106021238"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "戏剧写作基础",
      "author": "埃格里",
      "isbn13": "9787108014504",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 戏剧写作基础（埃格里），ISBN-13 9787108014504"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Film Art: An Introduction, 12th ed.",
      "author": "Bordwell, Thompson, Smith",
      "isbn13": "9781259534959",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Film Art: An Introduction, 12th ed. (Bordwell, Thompson, Smith), ISBN-13 9781259534959"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Understanding Movies, 14th ed.",
      "author": "Louis Giannetti",
      "isbn13": "9780205856169",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Understanding Movies, 14th ed. (Louis Giannetti), ISBN-13 9780205856169"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Filmmaker's Handbook, 5th ed.",
      "author": "Ascher & Pincus",
      "isbn13": "9780452297289",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Filmmaker's Handbook, 5th ed. (Ascher & Pincus), ISBN-13 9780452297289"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "How to Read a Film, 4th ed.",
      "author": "James Monaco",
      "isbn13": "9780195321050",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: How to Read a Film, 4th ed. (James Monaco), ISBN-13 9780195321050"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Film History: An Introduction",
      "author": "Thompson & Bordwell",
      "isbn13": "9780073386133",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Film History: An Introduction (Thompson & Bordwell), ISBN-13 9780073386133"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "What Is Cinema? Vol. 1",
      "author": "André Bazin",
      "isbn13": "9780520242272",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: What Is Cinema? Vol. 1 (André Bazin), ISBN-13 9780520242272"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Sculpting in Time",
      "author": "Andrei Tarkovsky",
      "isbn13": "9780292776241",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Sculpting in Time (Andrei Tarkovsky), ISBN-13 9780292776241"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Hitchcock/Truffaut",
      "author": "François Truffaut",
      "isbn13": "9780671604295",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Hitchcock/Truffaut (François Truffaut), ISBN-13 9780671604295"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "Notes on the Cinematograph",
      "author": "Robert Bresson",
      "isbn13": "9781681370248",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: Notes on the Cinematograph (Robert Bresson), ISBN-13 9781681370248"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "电影艺术：形式与风格",
      "author": "波德维尔、汤普森",
      "isbn13": "9787301254332",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影艺术：形式与风格（波德维尔、汤普森），ISBN-13 9787301254332"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "认识电影",
      "author": "贾内梯",
      "isbn13": "9787532763122",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 认识电影（贾内梯），ISBN-13 9787532763122"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "电影是什么",
      "author": "巴赞",
      "isbn13": "9787108017963",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影是什么（巴赞），ISBN-13 9787108017963"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "雕刻时光",
      "author": "塔可夫斯基",
      "isbn13": "9787532743841",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 雕刻时光（塔可夫斯基），ISBN-13 9787532743841"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "希区柯克与特吕弗对话录",
      "isbn13": "9787532745128",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 希区柯克与特吕弗对话录，ISBN-13 9787532745128"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "电影语言的语法",
      "author": "阿里洪",
      "isbn13": "9787532299990",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影语言的语法（阿里洪），ISBN-13 9787532299990"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "AI写作：用AI倍速提升写作效率",
      "author": "邓世超",
      "isbn13": "9787111760146",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: AI写作：用AI倍速提升写作效率（邓世超），ISBN-13 9787111760146"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "如何写出好故事 HBO大师写作课",
      "isbn13": "9787516827482",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 如何写出好故事 HBO大师写作课，ISBN-13 9787516827482"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "给青年编剧的信3.0",
      "author": "宋方金",
      "isbn13": "9787559493965",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 给青年编剧的信3.0（宋方金），ISBN-13 9787559493965"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "编剧的艺术",
      "author": "埃格里",
      "isbn13": "9787550213333",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 编剧的艺术（埃格里），ISBN-13 9787550213333"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "短视频与直播文案写作",
      "author": "张弘李自海魏坚 主编吴曼刘哲李守勤 副主编",
      "isbn13": "9787115638649",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 短视频与直播文案写作（张弘李自海魏坚 主编吴曼刘哲李守勤 副主编），ISBN-13 9787115638649"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "新媒体广告与文案写作(第2版)",
      "author": "周颖 主编张文杰 主编朱晓虹 副主编王娜 副主编黄伟 副主编",
      "isbn13": "9787115648044",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 新媒体广告与文案写作(第2版)（周颖 主编张文杰 主编朱晓虹 副主编王娜 副主编黄伟 副主编），ISBN-13 9787115648044"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "小说的骨架：好提纲成就好故事",
      "author": "[美]凯蒂·维兰德",
      "isbn13": "9787210099529",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 小说的骨架：好提纲成就好故事（[美]凯蒂·维兰德），ISBN-13 9787210099529"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "编剧心理学 在剧本中建构冲突（（美）尹迪克）",
      "isbn13": "9789571161488",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 编剧心理学 在剧本中建构冲突（（美）尹迪克），ISBN-13 9789571161488"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "救猫咪-小说创作指南",
      "isbn13": "9787522513003",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 救猫咪-小说创作指南，ISBN-13 9787522513003"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "救猫咪：电影编剧指南",
      "isbn13": "9787533963361",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 救猫咪：电影编剧指南，ISBN-13 9787533963361"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "人物：文本、舞台、银幕角色与卡司设计的艺术（编剧教父罗伯特·麦基“虚构艺术三部曲”完结篇）",
      "author": "罗伯特·麦基",
      "isbn13": "9787533969585",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 人物：文本、舞台、银幕角色与卡司设计的艺术（编剧教父罗伯特·麦基“虚构艺术三部曲”完结篇）（罗伯特·麦基），ISBN-13 9787533969585"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "救猫咪2经典电影剧本解析",
      "isbn13": "9787533964108",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 救猫咪2经典电影剧本解析，ISBN-13 9787533964108"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "故事的解剖",
      "author": "羅伯特．麥基(Robert McKee)",
      "isbn13": "9787201094601",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 故事的解剖 (羅伯特．麥基(Robert McKee))，ISBN-13 9787201094601"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "對白的解剖",
      "isbn13": "9789864898435",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 對白的解剖，ISBN-13 9789864898435"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "人物的解剖",
      "isbn13": "9789864896257",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 人物的解剖，ISBN-13 9789864896257"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "諾蘭變奏曲",
      "isbn13": "9789863844693",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 諾蘭變奏曲，ISBN-13 9789863844693"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "作家的灵感宝库",
      "isbn13": "9787514220155",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 作家的灵感宝库，ISBN-13 9787514220155"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "发现你的创造力类型",
      "isbn13": "9787210108061",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 发现你的创造力类型，ISBN-13 9787210108061"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "畅销作家写作全技巧",
      "isbn13": "9787210092452",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 畅销作家写作全技巧，ISBN-13 9787210092452"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "小说的八百万种写法",
      "isbn13": "9786263100442",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 小说的八百万种写法，ISBN-13 9786263100442"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "写小说最重要的十件事",
      "isbn13": "9787210108672",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 写小说最重要的十件事，ISBN-13 9787210108672"
    },
    {
      "kind": "reference_book",
      "language": "EN",
      "title": "The Essential Screenplay (3-Book Bundle)",
      "author": "Field, Syd",
      "isbn13": "9780307423269",
      "origin": "spec/book_of_knowledge.md",
      "citation": "EN: The Essential Screenplay (3-Book Bundle) (Field, Syd), ISBN-13 9780307423269"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "电影编剧学（修订版）",
      "author": "汪流",
      "isbn13": "9787811272406",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 电影编剧学（修订版）（汪流），ISBN-13 9787811272406"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "实用电影编剧",
      "author": "张觉明",
      "isbn13": "9787106029234",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 实用电影编剧（张觉明），ISBN-13 9787106029234"
    },
    {
      "kind": "reference_book",
      "language": "ZH",
      "title": "故事片创作六讲",
      "author": "王竞",
      "isbn13": "9787541151323",
      "origin": "spec/book_of_knowledge.md",
      "citation": "ZH: 故事片创作六讲（王竞），ISBN-13 9787541151323"
    }
  ],
  "agent_id": "video.narrativearc",
  "previous_common_agent_id": "video.narrative_designer",
  "va_taxonomy_aligned": true,
  "generic_source": "generic-swarm-ops/business/video/agents/video.narrativearc",
  "note": "Imported into CASOPS as baseline_safe. No production activation, no network, no plugins, memory writes forbidden.",
  "aligned_at": "2026-07-27T00:48:10.538790Z",
  "generic_source_depth": {
    "excerpts": true,
    "study": true,
    "adopted_at": "2026-07-27T01:30:28.525741+00:00",
    "upstream": "generic-swarm-ops/business/video/agents"
  },
  "imported_from": "C:\\Project\\common-agent-swarm-ops\\business\\video\\agents\\video.narrativearc",
  "reference_book_origin": "spec/book_of_knowledge.md",
  "reference_book_note": "Bibliographic references from spec/book_of_knowledge.md. Does not enable network, RAG, T3, plugins, or memory writes."
}
```

### `sources/RETHINK_100_APPLIED.json`

```json
{
  "schema_version": "1.0",
  "agent_id": "video.narrativearc",
  "source_doc": "business/video/corpus/study/ui/RETHINK_100_IMPROVEMENTS.md",
  "applied_at": "2026-07-31T06:22:31Z",
  "item_ids": [
    12,
    15,
    21,
    26,
    30,
    31,
    32,
    33,
    37,
    38,
    42,
    59,
    63,
    80,
    87,
    88,
    93,
    94
  ],
  "item_titles": {
    "12": "First-and-last-frame control",
    "15": "Model deprecation handling",
    "21": "Isolate orchestration from execution",
    "26": "Circuit breaker per external API",
    "30": "Multi-tenant isolation",
    "31": "Iterative script verification",
    "32": "Hierarchical CoT planning",
    "33": "Character bank across shots",
    "37": "Hybrid workforce checkpoints (gates)",
    "38": "Multi-turn agent conversation",
    "42": "Act/sequence/beat hierarchy in DAG",
    "59": "Agent reasoning in plain English",
    "63": "Comparison with human baseline",
    "80": "Script-first workflow",
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
    "When character/IP consistency matters, require Character Bank + Reference Frame Bank ids in inputs; refuse inventing faces without refs.",
    "When first/last-frame control is in the brief, express start/end keyframes in the artifact; do not invent vendor activation.",
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
  "agent_id": "video.narrativearc",
  "sources": [
    {
      "id": "src_1",
      "title": "Campbell",
      "description": "Campbell",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.narrativearc",
      "status": "planned_or_partial"
    },
    {
      "id": "src_2",
      "title": "Snyder *Save the Cat*",
      "description": "Snyder *Save the Cat*",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.narrativearc",
      "status": "planned_or_partial"
    },
    {
      "id": "src_3",
      "title": "Truby",
      "description": "Truby",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.narrativearc",
      "status": "planned_or_partial"
    },
    {
      "id": "src_4",
      "title": "Black List analyses",
      "description": "Black List analyses",
      "license_class": "unknown_review_required",
      "acquisition_method": "manual_or_licensed_api",
      "local_path_hint": "sources/excerpts/ or sources/study/",
      "refresh_sla_days": 90,
      "owner": "video.narrativearc",
      "status": "planned_or_partial"
    }
  ],
  "note": "Legal review required before treating external corpora as production grounding."
}
```

### `sources/study/general_creative_agent_functional_specification.md`

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
- **Additional arXiv support**: Multiple papers on st

…(clipped 5480 characters from `general_creative_agent_functional_specification.md`)

### `sources/study/general_creative_agent_technical_specification.md`

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
- **

…(clipped 1517 characters from `general_creative_agent_technical_specification.md`)
