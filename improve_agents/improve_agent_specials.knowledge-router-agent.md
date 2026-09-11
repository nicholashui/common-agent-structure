# Improve `specials.knowledge-router-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Routing is not “give the agent the whole corpus”
Notes: Routing is not “give the agent the whole corpus”. Lewis RAG (arXiv:2005.11401) already showed parametric vs non-parametric memory. Routing adds *which specialist* and *which slice* of the corpus. A practical stack (named in this folder’s design text, grounded here): 1. **Metadata first** — agent_id, domain, license, recency. Cheap and explainable. 2. **Centroid / cluster** — RopMura-style training

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.knowledge-router-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: route explained; no graph DB; empty index → no-knowledge. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.knowledge-router-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2005.11401](https://arxiv.org/abs/2005.11401) |
| arXiv | [2310.11511](https://arxiv.org/abs/2310.11511) |
| YouTube | [Akari Asai, Self-reflective LMs with retrieval (UMass ML lunch)](https://www.youtube.com/watch?v=bVz8Ua1VVsE) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/tools/overview) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

