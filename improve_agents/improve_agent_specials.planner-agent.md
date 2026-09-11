# Improve `specials.planner-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Different artifacts need different plans
Notes: Different artifacts need different plans. A strategic architecture note, a UI screen, a schema migration, and a test plan do not share retrieval scope or output schema. Hierarchical planning: 1. Classify the component type. 2. Scope evidence (only the files that type needs). 3. Synthesize with citations to those files. 4. Critic: missing requirement, untraceable task, security-sensitive step. 5. E

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.planner-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: every task cites a span; ReAct is not this planner; no coding-agent spawn. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.planner-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2210.03629](https://arxiv.org/abs/2210.03629) |
| YouTube | [Yao, LLM Agents history & overview (UC Berkeley CS294-196) — ReAct is execution](https://www.youtube.com/watch?v=RM6ZArd2nVc) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/tools/overview) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

