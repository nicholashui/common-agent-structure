# Improve `video.childrensauthor`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Owns age-band language, picture-book or kids’-video pacing.
Notes: Developmental load (vocabulary, fear, runtime) is a constraint. COPPA/child-directed rules escalate to legal. Do not diagnose.

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/video.childrensauthor/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: in-role childrensauthor artifacts or wait; no invented CLIP-T/WCAG/arena numbers. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `video.childrensauthor`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | Unique study set in `agents/video.childrensauthor/sources/study/domain_knowledge.md` |
| YouTube | [Measure What Matters core message](https://www.youtube.com/watch?v=DXSIHm115gk) |
| x.ai | [non-activating vendor doc](https://x.ai/docs/developers/quickstart) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

