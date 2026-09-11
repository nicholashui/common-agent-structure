# Improve `specials.agentic-rag-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: RAG is parametric + non-parametric memory
Notes: RAG is parametric + non-parametric memory. Lewis et al. (arXiv:2005.11401, NeurIPS 2020) define RAG as a seq2seq *parametric* model plus a dense index *non-parametric* memory. Always-on retrieve-then-generate still hallucinates when the index is wrong or ignored.

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.agentic-rag-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: retrieve vs no-retrieve is explicit, and answers are either **no-knowledge** or cited from in-thread text. No qualified recall@k. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.agentic-rag-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2005.11401](https://arxiv.org/abs/2005.11401) |
| arXiv | [2310.11511](https://arxiv.org/abs/2310.11511) |
| arXiv | [2401.15884](https://arxiv.org/abs/2401.15884) |
| arXiv | [2501.09136](https://arxiv.org/abs/2501.09136) |
| YouTube | [Akari Asai, Self-reflective LMs with retrieval](https://www.youtube.com/watch?v=bVz8Ua1VVsE) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/tools/overview) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

