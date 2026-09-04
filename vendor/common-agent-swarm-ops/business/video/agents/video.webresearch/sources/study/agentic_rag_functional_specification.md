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
```

Use `checkpointer = MemorySaver()` (or AsyncSqliteSaver for production persistence).

## 4. Per-Node Detailed Design (Contracts, Inputs/Outputs, Prompts)

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

## 5. Hybrid Retrieval & Indexing Design (65k MD Scale – Critical)

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

## 6. Tools (Dynamic & Extensible)

- `hybrid_retrieve(query: str, use_lightrag: bool = True)`
- `web_search_tavily`
- `wiki_writer(markdown_content: str, title: str)`
- Calculator, arXiv fetcher (bonus).

## 7. Graph Construction (`src/graph/agentic_rag_graph.py`)

- `StateGraph(AgentState)`
- Add nodes + conditional edges for reflection (`should_continue_reflection` based on confidence/iterations).
- Parallel tool execution where possible.
- Full LangSmith tracing on every node (callbacks).

## 8. UI, CLI, Evaluation & Production Features

- **Streamlit** (`app.py`): Chat interface + expandable reasoning trace (node-by-node with scores, docs, critiques) + "Save to Wiki" button.
- **Typer CLI** (`cli.py`): `ingest --resume`, `query "..." [--hybrid] [--wiki] [--trace]`, `lint-corpus`, `eval`, `build-wiki`.
- **Evaluation Harness** (`src/evaluation/`): RAGAS (faithfulness, answer_relevancy, context_precision) + custom reflection score. 50+ golden query test set. Automated runs with JSON reports.
- **Observability**: LangSmith project per run; custom metadata for agentic metrics.
- **Docker**: Multi-container compose (app + Chroma + LightRAG OpenSearch + optional PostgreSQL).
- **Error Handling**: Graceful fallbacks, retry logic, rate limiting.

## 9. Phased Implementation Plan (Strict Order – With Checkpoints)

**Phase 0**: Project skeleton, requirements.txt, config, data models, prompts templates, Docker compose.  
**Phase 1**: Ingestion pipeline – full 65k MD benchmark + incremental mode + LightRAG indexing.  
**Phase 2**: Hybrid retriever + tools implementation.  
**Phase 3**: LangGraph core (state, nodes, edges, reflection/planning loops, memory).  
**Phase 4**: Multi-agent collaboration + critic + wiki synthesizer.  
**Phase 5**: Streamlit UI + CLI + tracing visualization + evaluation harness.  
**Phase 6**: Docker, tests, logging, security (API keys), README (diagrams, comparison table, benchmarks).  
**Phase 7**: End-to-end stress testing (100 complex queries), latency/quality benchmarks, final polish.

## 10. Success Criteria (Measurable & Verifiable)

1. Full 65k MD corpus ingested incrementally without OOM or crashes; benchmark logged.
2. Every complex query trace demonstrates **all 4 patterns** and **7 elements** visibly.
3. Reflection loop triggers on ≥30% of queries and measurably improves confidence/quality.
4. LightRAG hybrid mode shows superior performance on relational/multi-hop queries vs. pure vector.
5. Wiki synthesis produces clean, Obsidian-ready vault with proper frontmatter and links.
6. Evaluation: faithfulness ≥0.92, answer relevancy ≥0.90, average latency <4s on consumer hardware.
7. Code is clean, fully typed (Pydantic + mypy), documented, git-committed per phase.

## 11. References & Recommended Starters

- Paper PDF: https://arxiv.org/pdf/2501.09136
- YouTube Video: https://youtu.be/MT3DM82PRLc
- LightRAG GitHub (2026 features): https://github.com/hkuds/lightrag (OpenSearch support)
- Karpathy LLM Wiki Gist (for wiki_output style): https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- LangGraph Agentic RAG examples (2026 edition)

**Immediate Action**: Start with **Phase 0 + Phase 1** today. Focus on robust, resumable ingestion of the 65k MD corpus first.

When ingestion is complete and benchmarked, ping me for detailed prompt review and graph wiring session.

This is the **canonical, ultra-detailed production-grade Agentic RAG implementation** with hybrid LightRAG and persistent Karpathy-style compounding. Ship it clean, observable, and performant. 🚀
