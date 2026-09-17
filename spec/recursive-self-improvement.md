# Recursive Self-Improvement (RSI)

A research map for implementing Dream-RSI-style loops: frozen models, evolving search/harness/memory, and related algorithms.

**Anchor paper:** Tong Zheng et al., *Dream-RSI: Recursive Self-Improvement through Evolving Worlds*, arXiv:2609.14858 (14 Sep 2026). Google + Google DeepMind + UMD + UVA.  
**Project:** https://www.dream-rsi.com/ · **Repo (code pending):** https://github.com/zhengkid/Dream-RSI · **PDF:** https://dream-rsi.com/assets/dream-rsi.pdf

This note is an implementation-oriented survey, not a claim that any current system is “true / unbounded RSI.” Every public system below is **bounded**: a frozen LLM plus one or more writable artifacts (exploration policy, harness, skills, memory, evaluator, or training recipe).

---

## 1. What “RSI” means in 2026 practice

Classic RSI (I.J. Good 1965; Schmidhuber’s Gödel Machine 2003) is a system that **improves the process that produces the next system**, including its own improvement machinery.

In current agent work the loop is almost always:

```
act → evaluate → persist an artifact → act again with that artifact
```

The artifact is the thing that recurses. Useful split:

| Layer | What changes | What stays frozen | Dream-RSI analogue |
|---|---|---|---|
| **Weights / training recipe** | Parameters, data mix, RL objective | Evaluator sometimes | Not Dream-RSI |
| **Harness / agent code** | Tools, prompts, routers, scaffold | Base LLM | DGM, SICA, Gödel Agent |
| **Exploration policy** | Branch / refine / stop / parallelize | Coding agent + evaluator | **Dream-RSI** |
| **Skills / procedures** | Reusable how-to files | Model | Voyager, MetaSkill-Evolve, WikiSkill |
| **Memory / context** | Playbooks, traces, working memory | Model | Reflexion, ACE, Recuris, RSIAgent |
| **Evaluator** | The score used to accept changes | Agent sometimes | Red Queen Gödel Machine |
| **Target program** | The algorithm being discovered | Agent | AlphaEvolve, FunSearch, SimpleTES |

Dream-RSI’s distinctive claim: **do not rewrite the coding agent**. Rewrite only the **orchestration policy** that decides *where to search next*, and score candidate policies by replaying them on **already-paid-for discovery trees**.

That is model-based RL with an *exact* world, not a learned world model. History is the world. Dreaming is off-policy evaluation of alternative search policies at zero extra executions.

---

## 2. Dream-RSI internals (the thing to clone conceptually)

### 2.1 Loop

1. **Online explore.** Current policy \(\pi\) drives a frozen coding agent. Policy picks a batch of leaves from the discovery tree (width \(W\)), agent writes children, evaluator scores them. Log the tree.
2. **Build replay simulator.** Each completed tree \(\mathcal{T}_i\) is an exact simulator of the realized search space: children and scores are already known.
3. **Dream.** An LLM policy-writer proposes \(M\) new policy programs \(\pi^0 \ldots \pi^{M-1}\). Each is rolled through historical trees without running the coding agent again. Score and keep the winner. Redeploy online. The pool of worlds grows.

### 2.2 What is rewritten vs frozen

- **Rewritten:** exploration-policy code. Must implement something like `solve(question, budget)` and a grid plan (`branch_count`, `refine_count`). Controls branching, refinement, stopping, parallelism.
- **Frozen:** coding agent, evaluator, execution environment, base models (paper used Gemini 3.1 Pro and Gemini 3.7 Flash via Gemini CLI).

### 2.3 Replay score (conceptual)

For policy version \(m\) on historical tree \(i\):

\[
V_i^m = \max_{v \in \mathcal{T}} s_v \;-\; \beta_1 N_i^m \;+\; \beta_2 \frac{N_i^m}{\max(1, k_{i,m}^\star)}
\]

- \(\max s_v\): best quality found in the *revealed* subtree
- \(N\): simulated attempts (cost)
- last term: parallelism bonus (attempts per decision round)
- \(V^m\): average of \(V_i^m\) over the history pool
- winner: \(\pi^\star = \arg\max_m V^m\)

Current policy is always a candidate, so offline revision is designed not to regress on the replay metric.

### 2.4 Reported numbers

Against **SimpleTES** (arXiv:2604.19341), the prior discovery loop they compare to:

| Domain | Result |
|---|---|
| Lasso-path solver | ~**162× fewer agent calls** (317 vs 51,200). Beat sklearn / glmnet on 6 held-out datasets |
| Math opt (Sum-Difference, Circle Packing, Autocorrelation) | Match or beat SimpleTES with **&lt;1,000** generations vs 51,200 |
| KernelBench | VGG16 **2.43×** fewer generations; LayerNorm **1.79×**; ConvDiv **2.09×** higher score at same budget |

Baseline “Recursive Fixed” (same loop, frozen exploration policy) still costs ~1.7× more calls than the dreaming policy.

### 2.5 Limits that matter for a reimplementation

- Replay cannot invent **unseen** branches. Early rounds have thin worlds.
- Recorded outcomes are treated as deterministic; a stochastic agent is only approximately replayed.
- Policy writer is itself an LLM and can overfit history or leak outcomes into `solve()` if you are sloppy. The paper’s own policy contract forbids reading scores/cell IDs inside `solve()`.
- Code release was still “being prepared” as of mid-Sep 2026. Reimplement from the paper + `dream-rsi.com` walkthrough until the official repo drops artifacts.

### 2.6 Immediate parent system

**SimpleTES** — *Structured Scaling of AI Discovery…*, arXiv:2604.19341.  
Budget \(N = C \times L \times K\): width of independent lines × refinement depth × local sample size, plus reuse of evaluated history. Open code: https://github.com/Wizard-Intelligence-Learning-Lab/SimpleTES  

Dream-RSI’s move: **the allocation policy itself becomes the object of RSI**, evaluated offline on trees SimpleTES-style search already paid for.

---

## 3. Taxonomy of similar projects (what to steal)

### 3.1 Closest to Dream-RSI: search-layer / history-as-simulator

| Project | Year | Mechanism | Steal this |
|---|---|---|---|
| **Dream-RSI** | 2026 | Replay trees → rewrite exploration policy | Exact-history world + off-policy policy search |
| **SimpleTES** | 2026 | Structured \(C,L,K\) discovery + history reuse | Discovery-tree logging, evaluators, KernelBench / Lasso tasks |
| **Dreamer / World Models / Dream to Control** | 2018– | Learn a world model, plan inside it | Metaphor only. Dream-RSI does **not** learn a model |
| **MuZero / MCTS agents** | 2019+ | Search + learned value | Tree policy + value over incomplete trees |
| **Tree of Thoughts / LLM-First Search** | 2023 / 2025 | LLM-controlled search | Policy that chooses expand vs stop |
| **LiTS** | 2026 | Modular Policy / Transition / Reward for LLM tree search | Plug-in search components. arXiv:2603.00631 |
| **SkyDiscover, Parallel-R1** | cited by Dream-RSI | Exploration optimization | Parallel search schedules |

### 3.2 Harness / agent-code RSI (frozen weights, rewrite the agent)

These are the practical cousins if the goal is “agent gets better at getting better” rather than “search policy gets cheaper.”

| Project | Paper | Code | What evolves | Headline |
|---|---|---|---|---|
| **Darwin Gödel Machine (DGM)** | arXiv:2505.22954 (Sakana / UBC / Vector; ICLR 2026) | https://github.com/jennyzzt/dgm | Agent scaffold (tools, prompts, editors). Open-ended **archive** of agents. Empirical accept, not Gödel proofs | SWE-bench **20% → 50%**, Polyglot **14.2% → 30.7%** |
| **HyperAgents / DGM-H** | arXiv:2603.19461 | — | Meta-process that chooses *how* agents are modified is itself editable | DGM + metacognitive self-modification |
| **ADAS / Meta Agent Search** | arXiv:2408.08435, ICLR 2025 | https://github.com/ShengranHu/ADAS | Fixed meta-agent writes new agent functions into an archive | First strong “search the agent design space in code” result |
| **ModularRSI** | arXiv:2609.14857 (same day as Dream-RSI) | — | Split harness into modules (loop / tools / observation / context / completion), evolve each from fail/success contrast, then integrate | Complementary to Dream-RSI: harness modules vs exploration policy |
| **STOP** | Zelikman et al., COLM 2024, arXiv:2310.02304 | https://github.com/microsoft/stop | Improver recursively improves its own scaffolding | Target is the improver, not the solution |
| **Gödel Agent** | arXiv:2410.04444, ACL 2025 | https://github.com/Arvid-pku/Godel_Agent | Runtime monkey-patch of own logic from a high-level objective | Fully self-referential; no fixed optimizer |
| **SICA** | arXiv:2504.15228 | https://github.com/MaximeRobeyns/self_improving_coding_agent | Agent **is** the meta-agent; edits own Python repo; Docker sandbox | SWE-Bench Verified subset **17% → 53%** |
| **Mendel Gödel Machine** | arXiv:2608.07645 | — | Comparative evolution across failures/successes and agent versions | More targeted self-edits than blind mutation |
| **Red Queen Gödel Machine** | arXiv:2606.26294 | — | Co-evolve **agent and evaluator** | Stops Goodhart if you can keep the eval honest |
| **Meta-Harness** | arXiv:2603.28052 | — | Agent searches over harness *files* | “A harness for optimizing harnesses” |
| **Proteus** | project | https://github.com/proteus-evolve/Proteus | Harness-agnostic self-evolution | Drop-in wrapper |
| **Reef** | project | https://github.com/Human-Agent-Society/reef | Continual-learning infra for self-improving agents | Persistence layer |
| **Ouroboros** | 2026 | search title | Reviewed core commits become the next runtime | Git-native RSI |
| **Cline RSI** | 2026 blog | Cline harness | One-shot RSI brief → 17h self-tune of prompts/tools | Terminal-Bench 2.1 **88.8%** at $49.8 |
| **Weco AIDE2** | Jul 2026 | commercial/research | Outer agent rewrites inner research agent | 7 successively better inner agents over 8 days |

### 3.3 Evolve the *solution*, not the agent (AlphaEvolve family)

Use these when the artifact is an algorithm / kernel / math object, which is also Dream-RSI’s evaluation domain.

| Project | Notes |
|---|---|
| **FunSearch** (DeepMind, 2023) | LLM + evaluator; function-level evolution |
| **AlphaEvolve** (DeepMind, 2025) | Ensemble LLMs + evaluators over EVOLVE-BLOCK regions. 4×4 complex matmul in **48** multiplies (beats Strassen 49). ~0.7% Google fleet compute recovered; FlashAttention kernel speedups |
| **OpenEvolve** | Open reimplementation. Best-known: https://github.com/algorithmicsuperintelligence/openevolve (`pip install openevolve`) and origin fork https://github.com/codelion/openevolve |
| **FunSearch** | DeepMind, Nature 2023. Island-model evolution of functions + evaluator. https://github.com/google-deepmind/funsearch |
| **AIDE / AIDE2** | Weco tree-search ML agent; AIDE2 is an outer loop that rewrites the inner harness (reported 7 better inner versions over ~8 days). https://github.com/WecoAI/aideml · `pip install weco` |
| **CodeEvolve / ShinkaEvolve / ThetaEvolve / EvoX / TTS-Discovery** | Cited next to Dream-RSI on math-opt tasks |
| **Karpathy Autoresearch / nanochat** | https://github.com/karpathy/autoresearch · https://github.com/karpathy/nanochat |

### 3.4 Skills, memory, environment RSI (no weight update)

| Project | Paper | Idea |
|---|---|---|
| **Voyager** | 2023 | Minecraft skill library that grows and is reused |
| **RSIAgent** | arXiv:2609.15364 | Training-free. Curriculum + actor + verifier. Broad-then-deep exploration. Freeze memory for downstream. OSWorld-v2 / Agent’s Last Exam. Code: https://github.com/AetherLabsAI/RSIAgent |
| **MetaSkill-Evolve** | arXiv:2607.05297 | Fast loop: task skill \(s\). Slow loop: meta-skill \(m=(\psi,\sigma,\alpha,\pi,\varepsilon)\) that *is* the improvement pipeline. Same frozen backbone |
| **Recuris** | arXiv:2608.24876 | Working memory tracks progress; experiential memory holds skills; meta-agent patches skills from localized failures. Large gains on long-horizon benches |
| **SkillGLoW / SkillAdam / WikiSkill** | 2026 | Skill consolidation and wiki-style persistent procedures |
| **ScienceBuddy** | arXiv:2609.17523 | Recursive-in-recursive: inner harness evolution, outer model RL |
| **Reflexion** | NeurIPS 2023 | Verbal RL → episodic memory |
| **ACE** | ICLR 2026, arXiv:2510.04618 | Context as evolving playbook (Generator / Reflector / Curator) |
| **ExpeL, ReasoningBank, AWM, Memp** | 2024–2026 | Experience → reusable insights / workflows |

### 3.5 Prompt / pipeline optimizers (cheap first RSI)

APE, OPRO, **EvoPrompt**, **Promptbreeder** (self-referential mutation prompts), ProTeGi, **DSPy / MIPROv2**, **TextGrad**, **GEPA** (arXiv:2507.19457, ICLR 2026 Oral; https://github.com/gepa-ai/gepa — reflective prompt evolution, reported up to 35× fewer rollouts than GRPO). Cheap first layer: evolve the policy *prompt* before evolving policy *code*.

Promptbreeder is the cleanest “the mutator mutates the mutator” toy. DSPy is the cleanest engineering surface if the improvable object is a typed pipeline rather than a free-form agent.

### 3.6 Weight-update / meta-training RSI (harder, not Dream-RSI-shaped)

- SEAL / self-adapting LMs (arXiv:2506.10943)
- Self-Rewarding LMs, SCoRe, Absolute-Zero
- AI4AI-Bench (arXiv:2608.20318): agent rewrites a **training algorithm**, retrains from scratch. Mean score 0.166 / 1.0 — most agents never change how the model learns
- TREX (arXiv:2604.14116): tree of fine-tuning experiments
- ScienceBuddy outer loop, MetaRSI Model-RSI slot (arXiv:2609.06396)
- Frontis OpenMLE / Frontis-MA1: post-train a model on Draft / Improve / Debug / Crossover operators that the harness also uses

Skip this layer until a frozen-model harness loop is stable. Weight RSI needs a sealed evaluator and a lot of compute.

### 3.7 Surveys, taxonomies, workshops

- Chen, Wang, Qu. *Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops.* arXiv:2607.07663. 1,250-paper corpus. Repo: https://github.com/deepgrounding/recursive-self-improvement
- Duan Yi et al. *The Last AI Built by Humans.* arXiv:2609.11873. Roadmap: improvement-execution → strategy → experience-acquisition → environment-adaptation → recursive meta-improvement. Headroom-Closed Index
- Tang et al. *Generalized Agent Iteration.* arXiv:2609.13406. One formal frame for GPI vs RSI (is the improver *inside* the agent?) and polarity (anchored / goal-drift / self-referential)
- ICLR 2026 Workshop on AI with Recursive Self-Improvement (Schmidhuber on the org list)
- Awesome lists:
  - https://github.com/Prism-Shadow/awesome-rsi
  - https://github.com/leezythu/Awesome-Harness-Self-Improvement
  - https://github.com/Shiyao-Huang/awesome-agent-evolution
- Turing Post, Sep 2026: “9 RSI systems, 7 loop stages, zero full RSI”

---

## 4. xAI / Grok (public signal, not a paper)

There is **no public xAI RSI paper** comparable to Dream-RSI as of 17 Sep 2026. What exists is product + staff commentary:

- Boyuan Zheng (@boyuan__zheng, Agents at xAI), Jul 2026, after Grok 4.5: Grok “analyzing its own weaknesses, discussing and implementing new recipes. It’s an early, primitive form of recursive self-improvement, but it’s real and already in my daily workflow.”
- Shen Zhuoran (@CMS_Flash, coding agents / self-improvement at xAI): self-improvement between **browser use** and **web-app development** — exploit the gap between using an app and building it.
- Secondary writeups claim Grok-class models help write training / inference / client-server code and some of their own data. Treat as anecdotal until a methods paper exists.
- Product pattern that *is* implementable without Colossus: observe a job → correct until it needs zero fixes → freeze as a **skill** → only then schedule as a routine. Specialists stay narrow; an ops agent writes postmortems into playbooks.

That is harness + memory RSI, same family as ACE / Reef / Cline, not Dream-RSI dreaming.

---

## 5. YouTube / talks worth watching

| Video | Why |
|---|---|
| Emergent Garden, *Recursive Self-Improvement* (Jun 2026, ~31 min) https://www.youtube.com/watch?v=t7_ZXgfJVG8 | Best public intuition pump. Autoresearch demo, DGM as “shallow RSI,” strong vs weak RSI. Repos in description: fractalsearch, mandelbrotnn |
| Super Data Science Ep. 1004, Jon Krohn, *Recursive Self-Improvement* (Jun 2026) https://www.youtube.com/watch?v=M7esJPTwBbQ | AlphaEvolve, Karpathy overnight tuner, METR time-horizon, Jack Clark 2028 bet |
| Crash Course Futures of AI #3 https://www.youtube.com/watch?v=KwHS2t2ML9g | FunSearch → AlphaEvolve evolutionary loop in plain language |
| Sakana / AI Papers Academy DGM explainers | Architecture walkthrough of archive + self-modify + benchmark gate |
| Karpathy channel + Autoresearch README | Minimal research-loop template |

Anthropic Institute essay on RSI is the lab-safety counterpart, not an implementation guide.

---

## 6. Algorithms to implement (ranked for a first system)

Build in this order. Each layer is useful alone.

### A. Logging substrate (required for everything)

Store every attempt as a **discovery tree**, not a chat log.

```
node:
  id, parent_id
  action: {branch | refine | stop | parallel_batch}
  artifact_ref: path or hash of code
  score: float | null
  cost: tokens, seconds, agent_calls
  children: [id]
  status: pending | ok | fail | pruned
```

Persist trees as JSONL + a small SQLite index. This *is* the Dream-RSI world.

### B. Fixed discovery policy (SimpleTES clone)

Implement \(C \times L \times K\):

- \(C\) independent roots (width)
- \(L\) refine steps on winners (depth)
- \(K\) local samples before commit

Selectors already in SimpleTES you can copy: `balance`, `puct`, `rpucg`, `llm_elite`.

This alone is a working algorithm-discovery loop.

### C. Dreaming / off-policy policy search (Dream-RSI clone)

1. Represent the exploration policy as a **small Python module** with a stable interface (`plan_grid`, `solve`).
2. After each online lap, sample \(M\) candidate modules (LLM rewrite + keep current policy).
3. For each candidate, walk historical trees: at each node, ask the policy which batch it *would* have opened; reveal only recorded children; accumulate the replay score \(V\).
4. Deploy \(\arg\max V\). Never require a weight update.

Optional: MAP-Elites / archive over policy behaviors (high-width vs high-depth vs cheap-stop) so you do not collapse to one style.

### D. Harness evolution (DGM / SICA clone)

Separate repo or package: tools, prompts, router. Mutation = LLM patch. Acceptance = frozen benchmark + cost. Keep an **archive**, not only the latest winner (open-endedness is the DGM lesson). Sandbox with Docker. Human or red-team gate before promotion.

### E. Skill / memory evolution (Voyager / RSIAgent / Recuris clone)

After failures, write a skill file. Working memory selects skills. Verifier is a different prompt or model. Freeze the skill library for production runs.

### F. Evaluator hygiene (do this before recursion gets long)

- Hidden test split (RSI-Exam / AI4AI-Bench pattern)
- Failed attempts are first-class artifacts
- Builder ≠ reviewer
- Explicit promotion ledger (see https://github.com/lihouwenbin/ai-redteam-recursive-self-improvement)

Without this, RSI Goodharts the judge.

---

## 7. Algorithms for a software agent swarm

Software only: routing, scheduling, search, memory, skills, harness code, evaluators. No GPU kernels, no robots, no chip placement. These are the algorithms *behind* Dream-RSI and its cousins that you can drop into a swarm ops platform (orchestrator, worker pool, history store, skill library, promotion gate).

Wire each one to a **surface**:

| Surface | What it is in a swarm |
|---|---|
| **Router / orchestrator** | Who runs next, width \(W\), stop, handoff |
| **Worker policy** | How a specialist expands a node |
| **Workflow graph** | Edges between agents (pipeline vs debate vs fan-out) |
| **Archive** | Population of harnesses / policies / skills |
| **Memory / skills** | What later runs retrieve |
| **Evaluator / gate** | What is allowed to go live |

### 7.1 Search and selection (the Dream-RSI core)

**PUCT / UCB / UCT (MCTS family)**  
Pick the next leaf to expand:

\[
\text{score}(v) = Q(v) + c \cdot P(v) \frac{\sqrt{N(\text{parent})}}{1+N(v)}
\]

- *From:* AlphaZero, SimpleTES `puct` / `rpucg`, AFlow MCTS, Tree Search for LM Agents.  
- *Swarm use:* router chooses which specialist or which open task to spend the next worker on. \(Q\) = mean task score, \(P\) = LLM prior or skill match, \(N\) = visits.  
- *Cost:* O(frontier) per decision. No extra model calls if \(P\) is a cached embedding.

**SimpleTES allocation \(N = C \times L \times K\)**  
Budget split into independent lines \(C\), refine depth \(L\), local best-of-\(K\).  
- *Swarm use:* spawn \(C\) parallel specialist lineages; each lineage gets \(L\) critic-refine hops; at each hop sample \(K\) workers and keep one. This is the default online policy before you invent dreaming.

**Best-first / beam / successive rejects**  
Keep a priority queue of open nodes by score−cost.  
- *Swarm use:* cheaper than MCTS when you do not need visit counts. Beam width = worker pool size \(W\).

**Bandits (UCB1, Thompson sampling, EXP3)**  
Treat each *agent type*, *model*, *prompt*, or *skill* as an arm.  
- *Swarm use:* model router and specialist picker when outcomes are noisy and the arm set is small (<50). EXP3 if the world is adversarial (eval drift).  
- Start here before PUCT if you only have a flat pool, not a tree.

**Island model / island EA**  
Several populations evolve with rare migration.  
- *From:* FunSearch.  
- *Swarm use:* one island per domain (coding, research, ops). Migration = copy a winning skill or harness across islands. Stops one noisy task from wrecking the whole swarm.

**MAP-Elites / quality-diversity**  
Archive cells indexed by *behavior* (width vs depth, cheap vs thorough, debate vs pipeline), not only fitness.  
- *From:* AlphaEvolve, OpenEvolve, DGM archive, POET.  
- *Swarm use:* do not keep only the current best harness. Keep one champion per cell so the swarm can switch style when the task distribution shifts.

**Pareto selection (quality, cost, latency, parallelism)**  
Dream-RSI’s \(V\) is already a linear scalarization of that front:

\[
V = \underbrace{\max s}_{\text{quality}} - \beta_1 N_{\text{calls}} + \beta_2 \frac{N_{\text{calls}}}{\text{rounds}}
\]

- *Swarm use:* never rank policies on quality alone. Store \((\text{score}, \$, \text{seconds}, \text{tokens})\) and pick with \(\beta\) sliders the user can change per workflow.

### 7.2 Dreaming / off-policy evaluation (the cheap RSI trick)

**Exact-history replay**  
A completed run is a tree of (decision → artifact → score). A candidate orchestrator is scored by walking *recorded* children only.  
- *From:* Dream-RSI. Conceptual parents: off-policy eval, Experience Replay, Dreamer (analogy only — do **not** train a world model first).  
- *Swarm use:* every workflow run writes a tree. At night, generate \(M\) new `policy.py` / router graphs and score them on last week’s trees with **zero worker LLM calls**. Promote if \(V(\pi') \ge V(\pi)\).  
- *Constraint:* replay cannot invent branches nobody tried. Mix 10–20% live exploration so the world pool grows.

**Keep-incumbent / conservative update**  
Incumbent is always in the candidate set.  
- *Swarm use:* production router never changes unless replay + a held-out live canary both win.

**Off-policy correction (optional)**  
If the logged policy and the candidate differ a lot, down-weight nodes the old policy would never have opened (simple importance ratio clipped to \([0.1, 10]\)).  
- Skip until you see replay over-claiming.

### 7.3 Workflow-graph algorithms (how the swarm is wired)

**Supervisor vs peer swarm vs pipeline vs debate**  
- Supervisor: one router LLM every hop — higher route accuracy, more calls.  
- Peer swarm / handoff: specialist passes `Command` to the next specialist — fewer calls, slightly more misroutes.  
- Pipeline: fixed A→B→C. Use when the DAG is known.  
- Debate / committee: \(k\) workers, critic or majority vote. Use when the evaluator is cheap and variance is high.  
- *Swarm use:* these are *graphs*, not vibes. Store the graph as code (AFlow / GPTSwarm style) so an optimizer can mutate edges.

**AFlow — MCTS over workflow code**  
Nodes = operators (`Generate`, `Review`, `Revise`, `Ensemble`, `Test`). Edges = Python. Search = select → LLM-expand → eval → backprop.  
- *Repo:* https://github.com/FoundationAgents/AFlow  
- *Swarm use:* the thing that invents new n8n-style graphs for your dashboard, scored on a frozen eval set.

**GPTSwarm — graph + REINFORCE on edges**  
Intra-agent edges fixed; inter-agent edges are probabilities trained with REINFORCE toward a benchmark score.  
- *Repo:* https://github.com/metauto-ai/GPTSwarm  
- *Swarm use:* learn which specialists should talk to which others. Start with edge probs = 0.5, train offline on logged trajectories if you do not want live RL.

**ScoreFlow / Score-DPO**  
Generate a workflow per query; optimize the generator with score-aware preference (not only pairwise win/lose).  
- *Paper:* arXiv:2502.04306.  
- *Swarm use:* only after you have a numeric workflow score. Heavier than AFlow; skip for v1.

**ADAS Meta Agent Search**  
A frozen meta-agent writes new agent functions into an archive.  
- *Repo:* https://github.com/ShengranHu/ADAS  
- *Swarm use:* nightly job that proposes a new specialist class, evals it, archives it. Does not need weight updates.

### 7.4 Population / harness evolution

**Darwin archive (DGM)**  
Sample parent from archive (fitness + novelty) → mutate harness source → eval → insert.  
- *Swarm use:* version every specialist’s tool file and system prompt. Rollback is `git checkout` of a losing generation.

**STOP loop**  
The improver’s own code is the search object.  
- *Swarm use:* a meta-worker whose only job is editing `orchestrator/` . Gated harder than worker edits.

**Genetic operators on artifacts (not weights)**  
Mutation = LLM patch or prompt crossover. Selection = tournament on held-out score. Crossover = splice two skill files or two graphs.  
- *From:* EvoPrompt, Promptbreeder, GEPA, Voyager skill merge.  
- *Swarm use:* GEPA first (evolve prompts, few rollouts), then code-level mutation once prompts plateau.

**Contrastive fail/success localization (ModularRSI / Mendel GM)**  
Diff a failing trace against a successful sibling; patch only the blamed module (router vs tool-use vs memory).  
- *Swarm use:* do not rewrite the whole agent after one bad run. Attribute, then patch one file.

### 7.5 Memory and skills

**Voyager skill library**  
Verified executable snippets + embedding retrieve + curriculum that proposes the next skill to learn.  
- *Swarm use:* `skills/` in the knowledge tab. A skill is promoted only if a verifier agent reproduces the result.

**ACE / Reflexion playbook**  
Generator / Reflector / Curator. Delta-updates to a playbook, not full rewrite (avoids context collapse).  
- *Swarm use:* ops bot writes *one bullet* into `playbook.md` after a postmortem. Never dump the raw trace into the next system prompt.

**Two-timescale skills (MetaSkill-Evolve)**  
Fast: task skill \(s\). Slow: meta-skill \(m\) that *is* the analyzer / retriever / proposer. Same frozen backbone.  
- *Swarm use:* workers may edit task skills daily; only the orchestrator may edit meta-skills weekly.

**Recuris split memory**  
Working memory = current task state + which skill to call. Experiential memory = durable skills. Failures localize to one of the two.  
- *Swarm use:* stop stuffing the full history into every worker. A 1–2k token working-memory object is the state; skills are files.

**RSIAgent broad-then-deep**  
Phase 1: many cheap parallel probes of an environment. Phase 2: deep dives on hard cases. Freeze memory after construction.  
- *Swarm use:* onboarding a new tool/API: explore first, then write the skill pack, then freeze it for production.

### 7.6 Routing extras (software, not radio)

**Pheromone / ACO-style path memory**  
Successful (task-type → specialist path) trails get a decaying bonus.  
- *From:* AMRO-S and classic ACO.  
- *Swarm use:* a Redis counter per `(intent, agent_id)` incremented on verified wins, decayed nightly. Router adds \(\alpha \log(1+\text{pheromone})\) to PUCT. No learned model required.

**Semantic intent → specialist**  
Small classifier or embedding nearest-neighbor onto a SKOS-like capability ontology. Soft / warn / strict modes.  
- *Swarm use:* cheaper than an LLM supervisor for the common 80% of jobs.

### 7.7 Ensemble and critics

**Self-consistency / majority vote**  
\(k\) independent workers, vote or pick median score.  
- *Swarm use:* only on high-stakes nodes. Cost × \(k\).

**Generator–critic / debate**  
One agent proposes, another attacks, optional third judges.  
- *Swarm use:* promotion gate and code review. Builder ≠ reviewer (same rule as the red-team RSI ledger).

**Best-of-N + verifier filter**  
Sample N, drop those that fail unit tests / schema, then rank.  
- *Swarm use:* default inner step of SimpleTES \(K\).

### 7.8 Scheduling and budgets (the \(\beta\) terms)

**Token / dollar / wall-clock budgets as first-class constraints**  
The policy must stop. Dream-RSI’s \(\beta_1,\beta_2\) are how you teach it that.  
- *Swarm use:* each workflow has `{max_calls, max_usd, max_seconds, max_parallel}`. Router that exceeds them is a failed candidate on replay.

**Work-stealing / DAG ready-queue**  
When a node’s parents are done, it becomes runnable. Idle workers pull.  
- *Swarm use:* this is your parallel bonus term in \(V\). Without a real DAG queue, “parallelism” is fake.

**Speculative cheap-then-escalate**  
Run a small/fast worker first. Escalate to a strong model only if score or verifier confidence \(< \tau\).  
- *Swarm use:* the dual-process router. Bandit or threshold on \(\tau\). Software budget policy, not hardware speculation.

**Population-Based Training (hyperparams only)**  
Periodically copy winner’s \(W\), \(\beta\), temperature, beam width onto losers.  
- *From:* Jaderberg 2017.  
- *Swarm use:* tune orchestrator knobs. Do not copy weights.

**Response-threshold / division of labor**  
Worker \(i\) claims a job only if stimulus \(s_i > \theta_i\); idle workers lower \(\theta\).  
- *Swarm use:* stops every specialist piling onto one hot job.

### 7.9 More algorithms worth wiring

| Algorithm | Origin | Swarm surface | Note |
|---|---|---|---|
| Thompson sampling | Bayesian bandits | Router / archive parent pick | Better than UCB when LLM-as-judge is noisy |
| Novelty search | Lehman & Stanley | Archive | Keep unusual successful traces, not only high score |
| DPP skill rerank | quality-diversity retrieval | Skill picker | Avoid 5 near-duplicate skills on one job |
| Prioritized experience replay | DQN / Schaul | Dream / skill distillation | Sample hard traces more often |
| Mixture-of-Agents | synthesis aggregator | Coordination | Parallel specialists + writer; expensive |
| TextGrad / verbal gradients | Yuksekgonul 2024 | Prompts | Critic writes “increase X, decrease Y” |
| DSPy MIPROv2 | Khattab / Opsahl-Ong | Prompt compile | Compile router instructions from traces |
| Condorcet / diverse jury | council judges | Gate | Heterogeneous models as judges beat one cloned judge |
| Prefix-observable constraint | Dream-RSI | Replay | Policy must not peek at unrevealed child scores |
| rPUCG | SimpleTES | Router on DAGs | γ-decay credit when traces share prefixes |

### 7.10 What to implement first in swarm-ops

Order that compounds and stays software-only:

1. **Trace every run as a discovery tree** (JSONL + SQLite). Without this, nothing else is RSI.  
2. **UCB or PUCT router** over specialists + open nodes.  
3. **\(C \times L \times K\) default policy** + hard budgets.  
4. **Critic + held-out gate + incumbent veto.**  
5. **Skill library with verifier promotion** (Voyager / ACE). GEPA on `SKILL.md` / dispatcher prompt before mutating code.  
6. **Nightly dream job:** rewrite orchestrator policy, score on trees, canary, promote.  
7. **MAP-Elites archive** of harness versions and workflow graphs (DGM + AFlow).  
8. Optional: GPTSwarm edge probs, pheromone table, Thompson parent sampling.  
9. Do **not** start with Score-DPO, weight RL, evaluator self-edits, kernel search, or robots.

Anti-patterns for a swarm: evolving the evaluator and the workers in the same loop; dumping full traces into every prompt; keeping only the latest harness; treating n8n graphs as unversioned UI state instead of scored code.

---

## 8. Recommended implementation path

A system that is Dream-RSI-shaped and shippable on a coding-agent stack:

```
┌─────────────────────────────────────────────┐
│  Orchestrator (writable policy.py)          │
│  plan_grid / branch / refine / stop / W     │
└──────────────────┬──────────────────────────┘
                   │ online
┌──────────────────▼──────────────────────────┐
│  Frozen coding agent (Claude/Grok/Gemini/   │
│  local Qwen) + tools + sandbox              │
└──────────────────┬──────────────────────────┘
                   │ scores
┌──────────────────▼──────────────────────────┐
│  Frozen evaluator (unit tests, KernelBench  │
│  style timing, math checker, SWE tests)     │
└──────────────────┬──────────────────────────┘
                   │ trees
┌──────────────────▼──────────────────────────┐
│  History pool = replay simulator            │
│  dream: rewrite policy.py, score offline    │
└─────────────────────────────────────────────┘
```

**Week-scale build order**

1. Pick one evaluable domain with a cheap, deterministic score: Lasso-path microbench, circle packing, a KernelBench-like kernel, or a 20-task SWE subset.
2. Clone SimpleTES *or* OpenEvolve just to get propose → evaluate → tree logging working.
3. Extract the search decisions into `policy.py`. Freeze the agent.
4. Add replay: given a tree + a policy, compute \(V\) without new LLM-codegen calls (you may still use a tiny LLM if the policy is natural language; prefer code policies so replay is free).
5. Add a policy-writer prompt that only sees prefix features of traces (width used, stop timing, duplicate directions), never raw winning code or scores inside `solve()`.
6. Only then consider DGM-style edits to the **agent** itself, behind a promotion gate.

**Do not start with weight updates.** Dream-RSI’s whole point is that the expensive model can stay still.

**Safety defaults:** Docker/gVisor sandbox, no network in eval, file allowlist, max agent-calls per lap, keep every losing policy in the archive, human approve any change that touches the evaluator.

---

## 8. Open-source starting points (clone first)

| Intent | Repo |
|---|---|
| Dream-RSI official (code pending) | https://github.com/zhengkid/Dream-RSI |
| SimpleTES discovery loop | https://github.com/Wizard-Intelligence-Learning-Lab/SimpleTES · https://github.com/wq-will/SimpleTES |
| AlphaEvolve-style program evolution | https://github.com/algorithmicsuperintelligence/openevolve · https://github.com/codelion/openevolve |
| FunSearch | https://github.com/google-deepmind/funsearch |
| AIDE | https://github.com/WecoAI/aideml |
| ADAS / Meta Agent Search | https://github.com/ShengranHu/ADAS |
| Self-modifying coding agent (SICA) | https://github.com/MaximeRobeyns/self_improving_coding_agent |
| DGM | https://github.com/jennyzzt/dgm · Sakana writeup https://sakana.ai/dgm/ |
| Gödel Agent | https://github.com/Arvid-pku/Godel_Agent |
| STOP | https://github.com/microsoft/stop |
| Voyager skill library | https://github.com/MineDojo/Voyager |
| Env-memory RSI (RSIAgent) | https://github.com/AetherLabsAI/RSIAgent |
| GEPA prompt evolution | https://github.com/gepa-ai/gepa |
| SEAL (weight-update; later) | https://github.com/Continual-Intelligence/SEAL |
| Autoresearch loop | https://github.com/karpathy/autoresearch |
| Harness RSI reproduction | https://github.com/alphaXiv/recursive-harness-self-improvement |
| Promotion-gated RSI protocol | https://github.com/lihouwenbin/ai-redteam-recursive-self-improvement |
| Continual infra (Reef) | https://github.com/Human-Agent-Society/reef |
| Harness-agnostic evolution (Proteus) | https://github.com/proteus-evolve/Proteus |
| RSI paper corpus | https://github.com/deepgrounding/recursive-self-improvement |
| Reading lists | https://github.com/Prism-Shadow/awesome-rsi · https://github.com/leezythu/Awesome-Harness-Self-Improvement · https://github.com/D2I-ai/awesome-recursive-self-improving-agents |

---

## 9. Mapping “similar” onto Dream-RSI components

If the goal is to **implement Dream-RSI**, steal pieces like this:

| Dream-RSI part | Best donor |
|---|---|
| Discovery tree + \(C,L,K\) online search | SimpleTES |
| Exact-history replay as world | Dream-RSI paper itself; Dreamer only for intuition |
| Policy as code with stable `solve` API | SICA / DGM (code-shaped artifacts) + Dream-RSI policy contract |
| Policy mutation | Promptbreeder / EvoPrompt / LLM rewrite with archive (ADAS, DGM) |
| Parallel workers + cost term | SimpleTES + Dream-RSI \(V\) with \(\beta_1,\beta_2\) |
| Domains / evaluators | SimpleTES task suite, KernelBench, OpenEvolve circle-packing, SWE-bench |
| Not leaking outcomes into policy | Dream-RSI `solve()` isolation rule |
| Open-endedness so you do not lock onto one policy | DGM archive / MAP-Elites |
| Promotion / safety | SICA Docker + red-team ledger |

If the goal is broader RSI for an agent platform (swarm ops, skills, routines), stack **ACE or Recuris memory** under the orchestrator, and optionally a **DGM archive** of harness versions. That is complementary, not a substitute for dreaming.

---

## 10. Honest status line

As of 17 Sep 2026:

- **Weak / bounded RSI is real** and reproducible: harness edits, skill files, prompt evolution, exploration-policy rewrite, experiment loops.
- **Strong RSI** (the system autonomously improves the full stack that produces the next, more capable model, including weights and the evaluator, without a human-set outer loop) is **not** demonstrated. Surveys and the ICLR 2026 workshop treat it as an open research program.
- Dream-RSI is the cleanest published design for the **search-policy** slice of that program, and it is the right one to copy if the scarce resource is **agent calls**, not GPU training.

---

## 11. Core citations

```
Zheng et al. Dream-RSI: Recursive Self-Improvement through Evolving Worlds. arXiv:2609.14858, 2026.
WILL Team. Structured Scaling of AI Discovery… (SimpleTES). arXiv:2604.19341, 2026.
Zhang, Hu, Lu, Lange, Clune. Darwin Gödel Machine. arXiv:2505.22954, 2025.
Novikov et al. AlphaEvolve. 2025.
Hu, Lu, Clune. Automated Design of Agentic Systems. arXiv:2408.08435, ICLR 2025.
Yin et al. Gödel Agent. arXiv:2410.04444, ACL 2025.
Robeyns, Szummer, Aitchison. SICA. arXiv:2504.15228, 2025.
Zelikman et al. Self-Taught Optimizer (STOP). COLM 2024.
Wang et al. MetaSkill-Evolve. arXiv:2607.05297, 2026.
Zhu et al. RSIAgent. arXiv:2609.15364, 2026.
Recuris. arXiv:2608.24876, 2026.
Chen, Wang, Qu. RSI survey. arXiv:2607.07663, 2026.
Duan et al. The Last AI Built by Humans. arXiv:2609.11873, 2026.
Schmidhuber. Gödel Machines. 2003.
Hafner et al. Dreamer. 2019.
Shinn et al. Reflexion. 2023.
Fernando et al. Promptbreeder. 2023.
```

---

*Compiled 2026-09-17. Sources: arXiv HTML/abstracts, dream-rsi.com, GitHub READMEs, Awesome-RSI lists, public xAI staff posts, and the YouTube talks listed above.*
