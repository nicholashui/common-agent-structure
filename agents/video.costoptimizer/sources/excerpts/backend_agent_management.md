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
│    │              │              ├──► SELF-REFINE (loop)         │
│    │              │              │         │                     │
│    │              │              │         ▼                     │
│    │              │              │    (re-run with feedback)     │
│    │              │              │                               │
│    │              │              ├──► WAITING_FOR_CRITIQUE       │
│    │              │              │         │                     │
│    │              │              │         ▼                     │
│    │              │              │    (receives critique,        │
│    │              │              │     resumes execution)        │
│    │              │              │                               │
│    │              │              └──► FAILED                     │
│    │              │                       │                      │
│    │              │                       ▼                      │
│    │              │                  (retry logic)               │
│    │              │                       │                      │
│    │              ◄───────────────────────┘ (re-queue)           │
│    │                                                            │
│    ◄─────────── BLOCKED (waiting for gate approval or input)    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

The backend tracks state for every agent in every production:

```python
# Per-production agent state (stored in PostgreSQL)
class AgentState:
    production_id: str
    agent_id: int
    state: "idle" | "queued" | "running" | "complete" | "failed" | "blocked"
    current_task_id: str | None
    iteration: int              # Which self-refine iteration
    last_metrics: dict          # { "clip_t": 0.34, "beat_coverage": 1.0 }
    critiques_pending: list     # Unprocessed critiques from other agents
    retry_count: int
    total_cost: float           # $ spent by this agent so far
    started_at: datetime
    completed_at: datetime | None
```

---

## 5. How Agents Communicate WITH EACH OTHER (via Backend)

Agents **never** talk directly to each other. The backend mediates ALL communication:

```text
DirectorAgent                    Backend                      EditorAgent
     │                              │                              │
     │  (completes shot intent)     │                              │
     │──publish: artifact_created──►│                              │
     │                              │                              │
     │                              │──(checks: who comments on    │
     │                              │   DirectorAgent's output?)   │
     │                              │                              │
     │                              │──deliver critique task──────►│
     │                              │                              │
     │                              │                              │
     │                              │◄──critique: "pacing too fast"│
     │                              │                              │
     │                              │──(checks: DirectorAgent      │
     │                              │   accepts critique from       │
     │                              │   EditorAgent? YES)           │
     │                              │                              │
     │◄──deliver critique──────────│                              │
     │                              │                              │
     │  (on next iteration,         │                              │
     │   incorporates feedback)     │                              │
```

The critique routing logic:

```python
# When an agent publishes an artifact:
def on_artifact_created(event):
    producer_agent = agents[event.agent_id]
    
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

---

## 6. How the Backend Handles PARALLEL Agents

During the Production phase, multiple agents can run simultaneously:

```text
TIME ──────────────────────────────────────────────────►

Worker 1: ████ DirectorAgent (Shot 5) ████
Worker 2:       ████ PromptEngineerAgent (optimizing) ████
Worker 3:            ████ AIQAAgent (checking Shot 4) ████
Worker 4:                 ████ MoodBoardAgent (reference) ████
Worker 5: ████████ ComposerAgent (theme for Act 2) ████████

                         │
                         ▼
              All publish events to Event Bus
              Orchestrator coordinates dependencies:
              "EditorAgent can't start until DirectorAgent
               completes ALL shots for this scene"
```

The Orchestrator uses a **dependency graph** to know when to dispatch:

```python
# Dependency rules (encoded in the DAG)
dependencies = {
    "editor_assemble": {
        "requires": ["director_all_shots_complete", "composer_score_ready"],
        "gate": "production_gate_passed"
    },
    "colorist_grade": {
        "requires": ["editor_rough_cut_complete"],
    },
    "sound_mix": {
        "requires": ["sound_design_complete", "composer_final_mix"],
    }
}

# Orchestrator checks after every task completion:
def on_task_complete(task):
    for pending_task, deps in dependencies.items():
        if all(is_satisfied(dep) for dep in deps["requires"]):
            dispatch(pending_task)  # Now it can run!
```

---

## 7. How the Backend Handles FAILURES

```text
Agent task fails (LLM error, tool timeout, quality below threshold)
    │
    ▼
RETRY LOGIC (in Orchestrator):
    │
    ├── Is retry_count < max_retries (default: 3)?
    │     YES → Re-queue with exponential backoff
    │           (wait 5s, then 15s, then 45s)
    │
    ├── Is it a transient error (API timeout, rate limit)?
    │     YES → Retry with same parameters
    │
    ├── Is it a quality failure (CLIP-T too low)?
    │     YES → Retry with PromptOptimizerAgent adjusting the prompt
    │
    ├── Is it a budget overrun?
    │     YES → Try with cheaper model (CostOptimizer fallback)
    │
    └── All retries exhausted?
          YES → Mark agent as FAILED
               → Notify user via WebSocket (red node on DAG)
               → User can: [Retry] [Skip] [Modify & Retry]
```

---

## 8. How the Backend Manages MEMORY

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

Example: DirectorAgent working on Shot 5
─────────────────────────────────────────
LLM decides: "I need to check what visual style we locked for Act 2"

→ tool_call: memory.recall("Act 2 visual style lock")
→ Returns: "Style lock: Veo 3.1 seed #4412, melancholic neo-noir"

LLM uses this to generate consistent prompt.
```

---

## 9. Complete Backend Control Flow Diagram

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

---

## 10. Summary: The Backend's Role

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

---

## Key Insight: Agents Are NOT Separate Services

```text
WRONG mental model:
  "Each agent is a separate microservice running 24/7"
  
  DirectorAgent-service ──┐
  EditorAgent-service ────┤── all running simultaneously
  ComposerAgent-service ──┤
  ... 114 services ───────┘

CORRECT mental model:
  "Agents are CONFIGURATIONS that workers INSTANTIATE on demand"

  ┌─────────────────────────────┐
  │     WORKER POOL             │
  │     (10-50 processes)       │
  │                             │
  │  Worker 1: currently executing DirectorAgent task
  │  Worker 2: currently executing PromptEngineerAgent task
  │  Worker 3: idle (waiting for next task)
  │  Worker 4: currently executing AIQAAgent task
  │  ...                        │
  └─────────────────────────────┘

  Each worker can execute ANY agent.
  It loads the agent's config, runs the LLM, then moves on.
  Like an actor playing different roles — same person, different script.
```

This is why 114 agents don't need 114 servers. A pool of 10-50 workers handles all of them, picking up tasks from the queue as they become available.
