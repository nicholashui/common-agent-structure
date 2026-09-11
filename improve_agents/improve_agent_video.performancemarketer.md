# Improve `video.performancemarketer`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Owns paid performance hypotheses and incrementality, not brand identity.
Notes: Last-click is not causal. Name the attribution window.

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/video.performancemarketer/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: in-role performancemarketer artifacts or wait; no invented CLIP-T/WCAG/arena numbers. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `video.performancemarketer`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | Unique study set in `agents/video.performancemarketer/sources/study/domain_knowledge.md` |
| YouTube | [Rewriting the SEO Starter Guide (Search Off the Record)](https://www.youtube.com/watch?v=EABqJXHQB3w) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/pricing) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

