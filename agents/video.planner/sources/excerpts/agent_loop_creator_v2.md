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
6. **Production Hardening**: Circuit breakers (CLOSED/OPEN/HALF_OPEN with proper recovery), exponential backoff retries, per-phase token/step budgets + early exit, structured error observations, sandboxed tool execution (restricted Python or subprocess isolation), input sanitization, least-privilege.
7. **Usability for Coding Agent / User**: Clean Python package (`agent_loop/`) with CLI (`python -m agent_loop.cli`), optional FastAPI server mode, comprehensive examples (research agent, coding project harness, self-improving meta-agent), full type hints + docstrings, pytest suite passing, MkDocs or rich README.
8. **Integration**: Works with LiteLLM or direct clients (xAI, DeepSeek, OpenAI-compatible); optional LangGraph adapter; exports structured plans/todo for Grok Build / Cursor consumption; compatible with user's self-hosted OpenWebUI/Keycloak/Strapi patterns if extended to server mode.

**v2 Cognitive Success Criteria (Additional)**:
9. **Adaptive Routing (Cynefin + RPD + Dual Process)**: On mixed-complexity task suites, correctly classifies context (Simple/Complicated/Complex/Chaotic) with ≥85% agreement vs human baseline or held-out labels; Fast Recognition Path triggers on ≥70% of repeated/routine sub-tasks with pattern match (measured by RPD similarity + outcome quality); overall token reduction ≥20-30% vs always-full baseline without quality loss on simple cases.
10. **Proactive Risk (Premortem)**: In Phase 0, Premortem step identifies ≥3-5 plausible failure modes per complex task and incorporates mitigations into spec/todo/quality_gates; demonstrable reduction in downstream FM-1.x/3.x issues in failure-injection tests.
11. **Structured Reflection & Deep Learning (AAR + Double-Loop + 5 Whys)**: Phase 4 reflections produce complete AAR artifacts (4 questions answered with evidence); Double-Loop questions governing variables and proposes meta-changes (e.g., prompt/schema evolution) that pass validation in ≥60% of bounded rounds; 5 Whys + Fishbone categorization used on ≥80% of diagnosed failures with actionable root causes.
12. **Multi-Perspective Critique (Paul-Elder / Red Team / Six Hats)**: Verifier supports critic_modes; ensemble or red_team/paul_elder modes catch ≥15% more issues (esp. assumption, bias, edge-case) than standard mode alone on held-out bad outputs; Six Hats or equivalent used in creative/harmonization steps when configured.

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

**Category 2: Inter-Agent Misalignment (36.9%)**
- FM-2.1 Conversation Reset (2.2%)
- FM-2.2 Fail to Ask for Clarification (6.8%)
- FM-2.3 Task Derailment (7.4%)
- FM-2.4 Information Withholding (0.85%)
- FM-2.5 Ignored Other Agent’s Input (1.9%)
- FM-2.6 Reasoning-Action Mismatch (13.2%)

**Category 3: Task Verification & Termination (21.3%)**
- FM-3.1 Premature Termination (6.2%)
- FM-3.2 No or Incomplete Verification (8.2%)
- FM-3.3 Incorrect Verification (9.1%)

**Key Findings & Mitigations Integrated**:
- Design/spec quality is #1 ROI. **Phase 0 mandatory**: Structured `TaskSpec` (Pydantic) with explicit objective, success_criteria list, constraints (max_steps, budgets), output_format, quality_gates. Automated spec validator + critic before loop start. Role contracts in delegation.
- Verification is weak spot even in "successful" runs. **Phase 3 + 5**: Dedicated Verifier/Critic agent (strict JSON: passes, score, issues, suggestions, confidence). Multi-level (low-level schema + high-level objective alignment). Explicit `Done` action that **must** pass verifier + evidence check. Progress tracking (% todo complete + criteria alignment in Thought step).
- Context/history loss & repetition common. **Phase 1**: Aggressive summarization on context > threshold, structured state (`task.md` / `todo.md` + key_facts only, not full history dump), cycle detection via recent action+obs hash (md5), `max_steps` hard cap + progress-based early exit.
- Inter-agent issues: Strong central Orchestrator with explicit decomposition/routing/contracts + structured handoff Observation schema (status, data, summary, confidence, issues, next_suggestions, provenance, trace_id). Circuit breakers per tool/role. Versioned shared state.
- Interventions in paper (+9-15% gains): Better prompts/roles/topology + verification sections. Our system goes further with **runtime gates + evolution**.

**Coding Agent Action**: In prompts and verifier, explicitly reference these modes (e.g., "Check for FM-1.1/1.5/3.1/3.2 violations..."). Build failure_injection test suite that simulates each and asserts mitigation.

### 2.2 AgentOrchestra + TEA Protocol (arXiv:2506.12508)
**"AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool-Environment-Agent (TEA) Protocol"** (Zhang et al., 2025/2026). 89.04% GAIA Test (strong on Level 2/3), self-evolution boosts further (93.33% val).

**TEA Core Abstractions (Implement Minimal Version)**:
- **Tool (TCP)**: First-class, versioned, lifecycle-managed. Register with name, description, schema (Pydantic/JSON), code/impl, semantic embedding for retrieval. Support dynamic generation (Tool Generator sub-agent).
- **Environment (ECP)**: Observation/action spaces, state coherence. (For us: working_dir, file system sandbox, code runtime state, browser if added.)
- **Agent (ACP)**: Roles, competencies, metadata. Hierarchical support, registration, coordination contracts. Support A2T/T2A transformations (agent-as-tool or tool-as-agent for dynamic reconfiguration — Phase 4+).

**Key Mechanisms to Implement**:
- **Version Manager**: Every prompt, tool code, agent config, sub-agent role, generated artifact has version + lineage (parent, timestamp, hash, metrics). register(new), rollback(to_v), select_best(metric).
- **Tracer**: Full execution trajectory (step, thought, action_type, payload, observation, versions_used, token_usage, timings, sub_agent_id). Export JSONL for replay/debug/reflection. Enables audit + optimization signal.
- **Self-Evolution Module**: TextGrad-inspired + self-reflection.
  1. Collect trace via Tracer.
  2. Diagnose (LLM: root_cause, target_component e.g. "planner_prompt_v3", proposed_edit).
  3. Apply edit (string replace or structured patch on prompt/tool code).
  4. Validate (re-execute on held-out trace or similar task; check success rate / steps / verifier score improvement).
  5. If improved per criteria: register new version (with provenance). Support bounded rounds (`max_reflection_rounds`).
- **Context Management**: Run-scoped + component-specific. Slicing/provenance for sub-agents (never full history dump). Semantic retrieval for relevant past versions/knowledge.
- **Hierarchical Orchestration (AgentOrchestra Pattern)**: Central Planner (decompose objective → dependency graph or numbered steps + todo.md → route to specialists with narrow sub-spec + context slice + success_criteria). Sub-agents run own controlled loops (or xAI delegation). Results bubble up → Consolidator (harmonize, dedup, resolve conflicts via cross-ref + verifier) → Reporter for final structured output. Tree routing + local tool ownership per sub-agent. Replan on failure/shift.

**Coding Agent Action**: Model `tea/` module with minimal Protocol classes/schemas. Use in registration and context building. Make self_evolver.py the heart of Phase 4. Planner generates `todo.md` style structured state (user loves this pattern).

### 2.3 ReAct Foundations + Enhancements
- **ReAct (Yao et al. ICLR 2023)**: Thought (reasoning trace) → Action (tool/delegate/finish) → Observation (grounded result) loop. 10-34% gains on interactive tasks vs pure CoT or acting. Our core: Strict structured decision output (Pydantic: thought, action_type, payload), structured Observation always.
- **Enhancements Incorporated**:
  - **Reflexion** (Shinn et al.): Verbal self-critique on trajectories → improvement plans. Used in light reflection (every N steps) + full Phase 4.
  - **Prospector** (Kim et al.): Self-Asking + Trajectory Ranking. Optional: Generate multiple candidate trajectories, rank via critic, pick best.
  - **ReflAct** (recent): Strengthens grounding **in the reasoning step itself** (retouches reasoning with world feedback). Enhance Thought prompt to explicitly re-ground vs previous obs + original objective.
  - **Plan-and-Execute + LATS/MetaGPT patterns**: Explicit high-level plan phase (Phase 0 optional) before loop; tree search elements via multiple parallel sub-branches (optional in hierarchical).
- **xAI Production Patterns**: Server-side ReAct loop (model decides tools → executes internally → iterates until final). Multi-agent: realtime parallel specialists + leader synthesis (4 or 16 agents controlled by `reasoning.effort`). Grok Build: Plan-first, parallel sub-agents (isolated contexts/worktrees), structured workflow, ACP support for custom orchestration. **Our Hybrid**: Client orchestrator maintains global state/trace/verifier; delegates research sub-problems to xAI multi-agent (narrow spec, receive synthesized + citations); for coding sub-tasks, use local specialists or emulate parallel in isolated Python processes/threads with copied state slices.

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

**Rationale Summary**: This design directly attacks the #1 failure category (spec/design) via Phase 0 + living TaskSpec + critic. Closes verification gaps with mandatory gates + structured obs. Prevents loops/context rot with detection + summarization + structured state (todo.md pattern user prefers). Enables long-term robustness via TEA self-evolution. Leverages xAI strengths without ceding control. Matches user's iterative, spec-driven, production harness philosophy.

---

## 3. Detailed System Architecture & Module Breakdown

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

3. **Phase 2: Hierarchical Delegation**
   - Orchestrator (or Planner) decomposes → selects/instantiates specialist (registry: Researcher, Coder, Verifier, Reporter, ToolGen, Browser, Analyzer...).
   - Creates narrow `SubTaskSpec` (subset objective + success_criteria + context_slice + provenance).
   - Invokes sub-agent (own controlled loop instance or xAI multi-agent delegation).
   - Sub returns Structured Observation (bubble up with full sub_trace summary for audit).
   - Parent records, validates/integrates, updates global todo/plan, decides next.

4. **Phase 3: Consolidation & Quality Gates**
   - Aggregator collects observations + plan progress.
   - Harmonizer/Reporter LLM: Merge, dedup, cross-reference, resolve conflicts (cite sources/versions), produce unified draft.
   - Verifier/Critic: Score vs success_criteria, check hallucinations/gaps/FM-3.x issues, suggest fixes. JSON output.
   - If fail gate: Trigger refinement (re-plan specific branch, re-delegate, or self-edit).
   - If pass: Proceed to polish or final.

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
   - Validate improvement on held-out or replay (re-run with new version; check success rate/steps/verifier score + AAR quality).
   - Register new versions if better (VersionManager with lineage + AAR justification). Update Pattern Store with outcome metadata for future RPD.
   - Bounded (`max_reflection_rounds=3`). Support lighter AAR for Fast-path traces.

6. **Phase 5: Termination & Output**
   - Final synthesis + structured output per spec.
   - Persist full trace + versions + metrics.
   - Optional post-hoc reflection summary.
   - Human-in-loop hooks at high-stakes gates or budget exhaustion.

### 3.2 Core Data Models (Pydantic — Generate These First)
```python
from pydantic import BaseModel, Field
from typing import Literal, Optional, List, Dict, Any
from datetime import datetime
import hashlib

class TaskSpec(BaseModel):
    task_id: str
    objective: str
    success_criteria: List[str]
    constraints: Dict[str, Any] = Field(default_factory=dict)  # max_steps, token_budget, etc.
    output_format: str
    quality_gates: List[str] = Field(default_factory=list)
    initial_plan: Optional[List[str]] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    **cognitive_profile**: Dict[str, Any] = Field(default_factory=lambda: {
        "enable_fast_path": True,
        "reflection_style": "aar_double_loop_5whys",
        "critic_modes": ["standard", "red_team", "paul_elder"],
        "cynefin_classification": "auto",
        "max_reflection_rounds": 3
    })

class StructuredObservation(BaseModel):
    status: Literal["success", "partial", "failed", "error", "circuit_open"]
    data: Optional[Any] = None
    summary: str
    confidence: float = Field(ge=0.0, le=1.0)
    issues: List[str] = Field(default_factory=list)
    next_suggestions: List[str] = Field(default_factory=list)
    provenance: str  # e.g. "tool:web_search" or "sub_agent:researcher_v2" or "xai_multi:leader"
    trace_id: str
    versions_used: Dict[str, str] = Field(default_factory=dict)  # component -> version

class TraceEvent(BaseModel):
    step: int
    timestamp: datetime
    thought: str
    action_type: str
    payload: Dict[str, Any]
    observation: StructuredObservation
    token_usage: Optional[Dict[str, int]] = None
    versions: Dict[str, str] = Field(default_factory=dict)

class AgentState(BaseModel):
    task_spec: TaskSpec
    history: List[TraceEvent] = Field(default_factory=list)
    todo: List[str] = Field(default_factory=list)  # or todo_md: str
    plan: Optional[Dict[str, Any]] = None
    memory_short: Dict[str, Any] = Field(default_factory=dict)
    memory_long_ref: Optional[str] = None  # vector ids or summary
    **pattern_store_ref**: Optional[str] = None  # references to successful trace patterns/embeddings for RPD matching
    seen_hashes: set = Field(default_factory=set)  # for cycle detection
    budgets: Dict[str, Any] = Field(default_factory=dict)
    versions: Dict[str, str] = Field(default_factory=dict)  # current active
    tracer: List[TraceEvent] = Field(default_factory=list)  # or separate Tracer class
    **current_mode**: Literal["fast", "full"] = "full"
    **cynefin_context**: Optional[str] = None
    **aar_history**: List[Dict[str, Any]] = Field(default_factory=list)  # structured AAR artifacts for learning + replay
```

(Expand with VersionedComponent, Plan, TodoItem, CircuitBreakerState, etc. in actual code.)

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

**Circuit Breaker Enhancement** (use attached as base; add metrics export, integration with tracer).

**Self-Evolution Example Skeleton** (refine attached):
```python
def self_evolve_component(component_name: str, trace: List[TraceEvent], llm, version_manager, held_out_traces: List = None):
    diagnosis = llm.generate(  # MASFT-aware prompt
        f"Analyze trace for root causes (reference MASFT modes FM-1.x to FM-3.x). Identify target_component and concrete proposed_edit (prompt string patch or code diff):\n{trace}",
        output_schema={"root_cause": str, "target_component": str, "proposed_edit": str, "expected_improvement": str}
    )
    if diagnosis.target_component == component_name:
        new_version = apply_structured_edit(component_name, diagnosis.proposed_edit)  # safe patch
        if validate_improvement(new_version, trace, held_out_traces or replay_subset(trace)):
            version_manager.register(new_version, parent=component_name, metrics=compute_metrics(new_version))
            return new_version
    return None
```

### 3.4 xAI Hybrid Integration Points
- In decision payload or orchestrator: If action_type == "delegate_research" or sub-spec complexity high → call_xai_multi_agent instead of local sub loop.
- Config: `enable_xai_hybrid=True`, `xai_research_threshold=0.7` (or explicit in spec).
- Logging: Always capture `source`, `agent_count` (from reasoning.effort), leader confidence if exposed.
- Fallback: If xAI call fails/circuit open → local sub-agent or direct tools.
- Grok Build Emulation (optional Phase 3): Expose plan/todo export; support "parallel sub-agents" via asyncio.gather on independent branches with isolated state copies.

---

## 4. Phased Implementation Roadmap for Coding Agent

**Phase 0 (Foundation — 1-2 days equiv)**: Project scaffold, Pydantic models (TaskSpec, StructuredObservation, TraceEvent, AgentState, VersionedComponent), basic LLM client wrapper (xAI + fallback), strict JSON schema enforcement helper, simple ReAct loop skeleton that runs without crashing on mock LLM/tools.  
**Verification Gate**: Loop executes 10 steps on toy task (search + summarize); always produces valid structured obs; cycle detection works on injected repetition; spec validation catches obvious FM-1.1/1.5 issues.

**Phase 1 (Controlled Core — Core Reliability + Cognitive Mode Selection)**: Full controlled_react_loop with cycle detection, CircuitBreaker (full states + metrics), safe_execute/safe_invoke, progress tracking (% todo + criteria alignment in Thought), **Fast Recognition Path + RPD Pattern Store matching + lightweight Metacognition Monitor**, light reflection, explicit Finish + basic verifier gate, structured state (todo list + key_facts), aggressive context summarization. Enhanced prompts with MASFT awareness **+ cognitive mode logic**. Basic Tracer (append-only JSONL) **with mode and aar stubs**.  
**Verification Gate**: Failure injection tests pass for FM-1.3 (repetition), FM-1.4/2.1 (history loss simulated), FM-3.1/3.2 (premature/incomplete). Verifier rejects bad Finish attempts. Token usage logged. No infinite loops. **Fast path triggers correctly on pattern-matched routine sub-tasks; Metacognition detects bias/progress issues**.

**Phase 2 (Hierarchical + Consolidation)**: Orchestrator + SubAgentRegistry (pluggable roles with narrow specs + contracts). Delegation path (local sub-loop). Consolidator + Reporter (harmonize + structured output). Multi-level Verifier (schema + objective alignment + MASFT check). Optional plan generation phase. Context slicing + provenance.  
**Verification Gate**: End-to-end on multi-step research/coding task with delegation; sub-results correctly bubbled/integrated; conflicts resolved or flagged; overall success criteria checked by verifier.

**Phase 3 (TEA Versioning + Basic Evolution + xAI Hybrid)**: VersionManager (register/rollback for prompts/tools/roles). Minimal TEA protocol schemas + registration. SelfEvolver (diagnose → propose → validate on held-out → commit). xAI multi-agent client integration (call for research sub-tasks; integrate result as special obs). Basic todo.md generation in planner.  
**Verification Gate**: Self-evolution run on 3 similar tasks shows measurable improvement (success/steps/verifier_score). xAI delegation works end-to-end (research sub-task returns synthesized result with citations). Version history queryable.

**Phase 4 (Polish, Examples, Production, Dogfood)**: Full examples (Deep Research Agent using xAI hybrid + local tools **with cognitive routing**; Coding Project Agent with plan/todo + sub-agents for research/analyze/code/test/verify; Self-Improving Harness that evolves its own verifier/prompts **and cognitive_profile**). Sandboxed code tool. CLI + optional FastAPI server. Full test suite (unit + integration + failure_injection + mini-benchmark **+ cognitive feature tests**). Observability exports (mermaid trace viz, replay function **with mode/AAR overlays**). Cost/token dashboards in tracer. Documentation (README with quickstart, architecture diagrams, MASFT mapping **+ cognitive model integration table**). Dogfood: Use built system to refine its own prompts/verifier **and cognitive components (Cynefin classifier, AAR template, RPD matcher)** on held-out traces; commit improvements via VersionManager **with AAR justification**.  
**Verification Gate**: All success criteria met or exceeded (incl. v2 cognitive criteria 9-12). Coding agent runs full test suite cleanly. User can take `agent_loop/` package and run complex tasks reliably **with measurable benefits from Fast path, Premortem, and structured reflection**. Self-evolution demonstrably improves a held-out component **including cognitive ones**.

**Coding Agent Workflow During Build**: After each phase/module, generate code → run internal critic (use verifier logic or separate reflection prompt) → fix issues → re-validate against gate criteria → proceed. Maintain `build_task.md` / `todo.md` internally. Log all to tracer for later self-evolution of the builder itself.

---

## 5. Production Hardening, Security, Observability & Extensibility

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

---

## 6. Testing & Validation Strategy (Critical for Coding Agent)

1. **Unit**: Schema validation, cycle hash correctness, CircuitBreaker state machine (test all transitions incl. HALF_OPEN recovery), Verifier JSON parsing + logic on edge cases.
2. **Integration**: Full loop on toy tasks (fact lookup, multi-step calc, simple code gen). Hierarchical delegation end-to-end. xAI hybrid (mock or real budgeted calls).
3. **Failure Injection (MASFT Coverage)**: Simulator that forces FM-1.1 (vague spec), FM-1.3 (repeat action), FM-1.5 (ignore done criteria), FM-2.6 (mismatch), FM-3.1/3.2/3.3 (bad termination/verification). Assert: early detection, correct mitigation (replan, verifier reject, escalate), no silent failure.
4. **Benchmark**: Mini suite (web research + synthesis, multi-file code project with tests, GAIA-style factual + reasoning). Measure success, efficiency (steps/tokens), evolution delta (before/after 3 rounds).
5. **Property-Based (Hypothesis)**: Random valid/invalid TaskSpec/obs → assert invariants (always structured output, no NaN confidence, budgets respected, versions consistent).
6. **Dogfood/Evolution Test**: Run self-evolution on verifier or planner prompt using real traces; verify improved version scores higher on held-out set without regression on base tasks.

**Coding Agent Mandate**: Do not mark phase complete until relevant tests pass. Generate tests alongside code.

---

## 7. References & Sources (Deep Research)

- **MASFT/MAST**: Cemri et al. "Why Do Multi-Agent LLM Systems Fail?" arXiv:2503.13657 (2025). MAST-Data, 14 modes, design issues dominant (41.8%), LLM judge, interventions. GitHub: multi-agent-systems-failure-taxonomy/MAST.
- **AgentOrchestra/TEA**: Zhang et al. "AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool–Environment–Agent (TEA) Protocol" arXiv:2506.12508 (2025/2026). 89.04% GAIA, hierarchical planner + specialists, self-evolution (TextGrad + reflection), versioning, lifecycle, protocols (TCP/ECP/ACP), transformations.
- **ReAct**: Yao et al. arXiv:2210.03629 (ICLR 2023).
- **Enhancements**: Reflexion (arXiv:2303.11366), Prospector (Self-Asking + Ranking), ReflAct (grounded reasoning), Plan-and-Execute, LATS, MetaGPT, ReST meets ReAct.
- **Surveys**: "Large Language Model Agent: A Survey on Methodology, Applications and Challenges" arXiv:2503.21460 (2025); other 2025-2026 agent architecture surveys.
- **xAI Production**: docs.x.ai — grok-4.20-multi-agent (server-side ReAct, 4/16 agents, leader synthesis, built-in tools, reasoning.effort controls agent count); Grok Build CLI (plan-first, parallel sub-agents, local/agentic coding, ACP support). Server-side agentic tool calling patterns.
- **Original Spec (v3)**: `agent_loop_v3.md` (Hierarchical ReAct + full cognitive layer from thinking_model.md: Cynefin adaptive routing, Premortem, AAR/Double-Loop/5Whys, RPD Fast Path, Metacognition, multi-perspective critics; production patterns, circuit breaker code, verifier/self-evolve skeletons, enhanced Phase descriptions).
- **Cognitive Frameworks**: `thinking_model.md` (ranked table of 40 traditional human thinking models with adoption scores, phases, similarities to agent loops, and specific integration rationales — top 10 prioritized in v3/v2).

All patterns synthesized for maximal reliability, evolvability, and alignment with research + xAI capabilities + user's engineering style.

---

## 8. Handoff & Immediate Next Actions for Coding Agent

**This spec is complete and actionable.** Start implementation **immediately** with Phase 0 scaffold + core models (generate Pydantic classes first — they are the contract). 

**Recommended First Prompt to Coding Agent (copy-paste)**:
"Read `agent_loop_creator_v2.md`, `agent_loop_v3.md`, and `thinking_model.md` (ranked table) fully. Create the `agent_loop/` Python package scaffold with pyproject.toml, core Pydantic models (TaskSpec with cognitive_profile, StructuredObservation, AgentState with pattern_store and current_mode, etc.), basic LLM client, **Cynefin classifier stub + Premortem step in Phase 0**, and a minimal working controlled ReAct loop **with Fast Recognition Path / Metacognition mode selection** that passes the Phase 0/1 verification gates (incl. cognitive criteria). Use strict JSON schemas. Include initial failure_injection test skeleton for MASFT modes **and cognitive feature tests**. Maintain todo.md during your work and apply critic/refinement to every generated module. Prioritize clean, testable implementation of the cognitive layer from agent_loop_v3.md Section 1.4."

After core loop solid, proceed phase-by-phase. Use the built system to help evolve its own prompts and verifier during Phase 4 dogfood.

**Expected Deliverable**: Fully functional, tested, documented `agent_loop/` package + examples + CLI that a user (or higher meta-agent) can import/run for reliable **cognitive-enhanced** hierarchical agent workflows (Fast Recognition Path on routine tasks, proactive Premortem risk mitigation, structured AAR/Double-Loop/5Whys reflection, multi-perspective critics), with clear extension points for xAI hybrid, custom tools, self-evolution, **and cognitive config**. Full support for replaying traces with mode/AAR overlays.

**Questions for Clarification (if needed before coding)**: None anticipated — spec is self-contained and directly references agent_loop_v3.md + thinking_model.md. If ambiguities arise during build, resolve via internal critic (use the verifier logic being built) or escalate with specific trace/AAR output.

This completes the deep research + implementation spec (v2). Build it production-grade with the cognitive layer as a first-class, configurable strength, iterate with critics on every module, dogfood the cognitive improvements on the builder itself during Phase 4, and make `agent_loop/` a cornerstone of advanced, human-aligned agent harnesses (N1ch01as Architect, DeepTutor, research/coding meta-agents).

**File created for handoff to coding agent (v2 — ready for cognitive-enhanced implementation).** Ready for execution.