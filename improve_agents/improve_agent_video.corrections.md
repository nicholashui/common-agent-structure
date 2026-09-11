# Improve `video.corrections`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Coordinates post-publication fixes and correction disclosures.
Notes: A correction is a public record: what was wrong, what is true now, where it ran. This is journalism/QC disclosure, not Murch cutting.

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/video.corrections/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: in-role corrections artifacts or wait; no invented CLIP-T/WCAG/arena numbers. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `video.corrections`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | Unique study set in `agents/video.corrections/sources/study/domain_knowledge.md` |
| YouTube | [Fair use / educational uses](https://www.youtube.com/watch?v=ruV2qn7xyU0) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/tools/overview) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

