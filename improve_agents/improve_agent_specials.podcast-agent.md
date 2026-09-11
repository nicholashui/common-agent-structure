# Improve `specials.podcast-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Craft vs measurement
Notes: Craft vs measurement. Host craft is prep → record → close → follow-up, balancing script and live conversation. That is not the same as **audience numbers**. IAB Tech Lab Podcast Technical Measurement Guidelines (v2.2 certified; v2.3 public comment 2026) count **downloads from server logs**, not listeners. A valid download typically requires ID3 plus ~1 minute of audio (or 100% of a tiny file), wit

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.podcast-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: do not invent download graphs; Apple/Spotify first-party ≠ IAB. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.podcast-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2106.06605](https://arxiv.org/abs/2106.06605) |
| arXiv | [2411.07892](https://arxiv.org/abs/2411.07892) |
| arXiv | [2412.05516](https://arxiv.org/abs/2412.05516) |
| YouTube | [IAB Tech Lab Audio Initiatives — podcast measurement working group (downloads vs listeners)](https://www.youtube.com/watch?v=_cygjTdeits) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/pricing) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

