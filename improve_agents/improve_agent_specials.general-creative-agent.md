# Improve `specials.general-creative-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Owns combinational briefs with named constraints
Notes: Combinatorial creativity vs sparse recombination. Boden’s split: **combinational**, **exploratory**, and **transformational**. “Strategic Sparse Outlier Recombination” here is a combinational claim: hold most of the distribution, recombine a rare part. That only works if: - Outliers are *specified* (which dimension is rare). - Recombination is *constrained* (audience, medium, brand, legal) and the

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.general-creative-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: the reply names Boden type, held-constant, sparse outlier, recombination rule, constraints, and who evaluates — or it marks **wait** / **OOS**. There is **no** qualified originality instrument. Do not close with “≥95% accuracy”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.general-creative-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2509.21043](https://arxiv.org/abs/2509.21043) |
| arXiv | [2504.13120](https://arxiv.org/abs/2504.13120) |
| arXiv | [2504.20643](https://arxiv.org/abs/2504.20643) |
| arXiv | [2412.14141](https://arxiv.org/abs/2412.14141) |
| YouTube | [YouTube: Boden AGI 12](https://www.youtube.com/watch?v=_zp6KOo9ZHQ) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/tools/overview) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

