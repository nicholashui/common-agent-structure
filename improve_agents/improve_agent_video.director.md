# Improve `video.director`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Owns vision, shot intent, pacing, take approval.
Notes: Shot intent is a contract: size, angle, move, duration, whose look, what changes on the cut. Text-only “cinematic dolly” is not intent. Control strength: 3D camera blockout → start/end frames → depth/pose passes → text last.

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/video.director/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: in-role director artifacts or wait; no invented CLIP-T/WCAG/arena numbers. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `video.director`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | Unique study set in `agents/video.director/sources/study/domain_knowledge.md` |
| YouTube | [The Art of Camera Movement](https://www.youtube.com/watch?v=ptQwvGcLZIw) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/model-capabilities/video/image-to-video) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

