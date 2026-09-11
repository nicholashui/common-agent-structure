# Improve `specials.aesthetics-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Owns critique of visual taste vs technical quality
Notes: Separate technical quality from taste. Image **quality** (blur, noise, compression) is not **aesthetics** (composition, style, cultural preference). NIMA (Talebi & Milanfar, arXiv:1709.05424) predicts the *distribution* of human opinion scores, not a single scalar, because raters disagree. A naked 0–10 score without a vector and a confidence is a hack surface.

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.aesthetics-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: the reply is a scorable **dimension vector** (or an explicit cannot-score), under a named profile, with no invented pixels. There is **no** qualified MOS/LAP/CLIP-T instrument — do not close with “≥95% accuracy”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.aesthetics-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [1709.05424](https://arxiv.org/abs/1709.05424) |
| arXiv | [2601.09896](https://arxiv.org/abs/2601.09896) |
| arXiv | [2509.11620](https://arxiv.org/abs/2509.11620) |
| arXiv | [2504.02522](https://arxiv.org/abs/2504.02522) |
| YouTube | [NIMA talk, Peyman Milanfar](https://www.youtube.com/watch?v=xMD3RXUCWtg) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/tools/overview) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

