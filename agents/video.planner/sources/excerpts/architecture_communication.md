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
| POST | `/api/productions/{id}/gates/{gid}/decision` | Approve/reject gate | Gate Dialog |
| POST | `/api/productions/{id}/critiques` | Send human critique | Critique Feed |
| POST | `/api/productions/{id}/agents/{aid}/retry` | Retry failed agent | Agent Inspector |
| POST | `/api/productions/{id}/agents/{aid}/skip` | Skip agent task | Agent Inspector |
| PUT | `/api/settings/router-config` | Update model routing rules | Router Config |
| GET | `/api/agents` | List all 114 agent definitions | Agent Registry |
| GET | `/api/productions/{id}/artifacts` | List artifacts | Artifact Gallery |
| GET | `/api/productions/{id}/artifacts/{aid}` | Get artifact + provenance | Artifact Viewer |
| POST | `/api/productions/{id}/delivery/package` | Trigger delivery packaging | Delivery Hub |

### WebSocket Events (Streams — things the system pushes to UI)

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

---

## Backend Architecture Detail

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

---

## Key Design Decisions

### Why WebSocket for agent→UI (not polling)?

- 114 agents can produce events every 1–5 seconds during active production
- Polling would require 10+ requests/second → expensive and laggy
- WebSocket gives instant updates (< 50ms latency) for DAG state changes
- Single connection per production, server filters events by relevance

### Why Event Bus between backend services (not direct calls)?

- Agents are asynchronous and parallel — no request/response pattern fits
- Event sourcing enables full replay of any production decision
- Decouples agent execution from UI delivery
- Multiple consumers can listen (UI, analytics, compliance logger, alerting)

### Why LangGraph for orchestration (not custom code)?

- DAG with conditional edges maps directly to the Composition Diagram
- Built-in state management for long-running multi-step workflows
- Human-in-the-loop gates are a first-class LangGraph concept
- Checkpointing: can resume after backend restart

### Why Temporal for durability?

- Productions can run for minutes (Viral Hook) to hours (Feature Film)
- Need guaranteed delivery: no lost tasks even if workers crash
- Automatic retry with backoff for failed agent tasks
- Workflow history for debugging and audit

---

## Sequence Diagram: Complete Request Lifecycle

```text
User          Frontend       API Gateway    Event Bus    Orchestrator    Agent Worker    LLM/Tool
 │               │               │              │             │               │             │
 │─click node──►│               │              │             │               │             │
 │               │─GET /agent───►│              │             │               │             │
 │               │◄──agent data──│              │             │               │             │
 │◄──render─────│               │              │             │               │             │
 │               │               │              │             │               │             │
 │─approve gate─►│              │              │             │               │             │
 │               │─POST /gate───►│              │             │               │             │
 │               │               │─publish──────►│            │               │             │
 │               │               │              │─gate_ok────►│               │             │
 │               │               │              │             │─dispatch──────►│             │
 │               │               │              │             │               │─LLM call───►│
 │               │               │              │             │               │◄──response──│
 │               │               │              │             │               │─tool call──►│
 │               │               │              │             │               │◄──video─────│
 │               │               │              │             │               │             │
 │               │               │              │◄─artifact_created───────────│             │
 │               │               │              │◄─state_change───────────────│             │
 │               │◄─────ws push──│◄─subscribe───│             │               │             │
 │◄──re-render──│               │              │             │               │             │
```

---

## Summary: Answer to "How does UI talk to agents?"

```text
YES — your intuition is exactly right:

   UI Frontend  ──(REST/WebSocket)──►  Backend  ──(Task Queue)──►  Agents

Specifically:

1. COMMANDS flow:  UI → REST API → Backend → Task Queue → Agent
   (user actions: launch, approve, critique, retry, configure)

2. EVENTS flow:    Agent → Event Bus → WebSocket Gateway → UI
   (real-time updates: state changes, artifacts, critiques, metrics)

3. The Backend is NOT a simple pass-through. It provides:
   • Orchestration (DAG execution, scheduling, retry logic)
   • State management (which agents are active, what phase we're in)
   • Asset management (storing artifacts, tracking versions)
   • Gate logic (evaluating criteria, collecting approvals)
   • Security (auth, permissions, C2PA signing)
   • Observability (logging, metrics, replay)

4. Agents NEVER talk directly to the UI.
   They publish events to the Event Bus, and the WebSocket Gateway
   delivers those events to the correct frontend client.
```

---

## Technology Mapping

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
