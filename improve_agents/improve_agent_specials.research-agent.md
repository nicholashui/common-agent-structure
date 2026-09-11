# Improve `specials.research-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Claims need sources
Notes: Claims need sources. Booth et al., *The Craft of Research*: a claim is a sentence that needs a reason and evidence. Unsourced fluent reports are not research. On this host: - Prefer operator-supplied URLs and local `sources/`. - Do not invent arXiv IDs, quotes, or page numbers. - If a required section (Source Catalog, glossary) cannot be filled, say so; do not pad. - Network search is off. “I woul

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.research-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: no invented arXiv IDs or quotes; missing section → say so. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.research-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2508.12752](https://arxiv.org/abs/2508.12752) |
| arXiv | [2609.01432](https://arxiv.org/abs/2609.01432) |
| arXiv | [2605.07723](https://arxiv.org/abs/2605.07723) |
| YouTube | [Claim–Evidence–Reasoning (Booth-style argument spine)](https://www.youtube.com/watch?v=fkpZfpNWjWY) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/tools/overview) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

