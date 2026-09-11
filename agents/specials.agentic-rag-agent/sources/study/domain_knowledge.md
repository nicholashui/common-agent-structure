# Domain knowledge — `specials.agentic-rag-agent`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation. **Empty live index.**

## RAG is parametric + non-parametric memory

Lewis et al. (arXiv:2005.11401, NeurIPS 2020) define RAG as a seq2seq *parametric* model plus a dense index *non-parametric* memory. Always-on retrieve-then-generate still hallucinates when the index is wrong or ignored.

## When retrieval should happen

**Self-RAG** (Asai et al., arXiv:2310.11511) trains reflection tokens: Retrieve / IsRel / IsSup / IsUse. Retrieval is a *decision*.

**CRAG** (Yan et al., arXiv:2401.15884) classifies retrieved knowledge Correct / Incorrect / Ambiguous and triggers correct / rewrite / fallback. Fallback on this host is **abstain**, not web search.

**Agentic RAG survey** (Singh et al., arXiv:2501.09136) names the pattern: the model decides *when, what, how* to retrieve.

**Agent-Orchestrated Adaptive RAG** (arXiv:2606.05658): query decomposition and reflection are **not universally beneficial** — extra hops can hurt ranking; apply selectively.

## Findings that change this folder

| Finding | Change |
|---|---|
| Self-RAG Retrieve token | Explicit retrieve vs no-retrieve |
| Empty index | **no-knowledge**; do not invent passages |
| CRAG Incorrect/Ambiguous | Abstain or ask for a source; no live rewrite-fetch |
| Adaptive RAG not always better (2606.05658) | Simple queries stay one-shot |
| Multi-intent (2509.10010) | List retrieve vs web vs write; only grounded Q&A in-role |
| OOS (2507.22289) | Non-knowledge asks labelled OOS |
| Wait (2506.01881) | Missing evidence → wait, not a fake citation |

## Skip as live enablement

| Source | Why skipped |
|---|---|
| A-RAG hierarchical retrieval tools (arXiv:2602.03442) | Would grant search tools |
| Q2D-Web 190M corpus (arXiv:2609.08887) | Live web index |
| xAI Collections / Web Search | Vendor; `allowed_tools: []` |
| SPEC Chroma/Wikipedia | Untrusted distillation |
| Skill live ON | Declared `casops.skill.rag.retrieve-decision`; register empty |

## Honesty

Citations must point at operator-provided or local `sources/` text named in the thread. Unsourced fluent answers are a RAG failure.

## Sources

- Lewis et al., RAG, arXiv:2005.11401 — https://arxiv.org/abs/2005.11401
- Asai et al., Self-RAG, arXiv:2310.11511 — https://arxiv.org/abs/2310.11511
- Yan et al., CRAG, arXiv:2401.15884 — https://arxiv.org/abs/2401.15884
- Singh et al., Agentic RAG survey, arXiv:2501.09136 — https://arxiv.org/abs/2501.09136
- Maharjan et al., Agent-Orchestrated Adaptive RAG, arXiv:2606.05658 — https://arxiv.org/abs/2606.05658
- Mishra et al., SoK Agentic RAG, arXiv:2603.07379 — https://arxiv.org/abs/2603.07379
- NLU: arXiv:2509.10010, 2507.22289, 2506.01881
- xAI tools — https://docs.x.ai/developers/tools/overview
- YouTube: search “Self-RAG Asai ICLR 2024” — do not paste transcripts

## Triple research (design-time, 2026-09)

Design-time citations collected to complete the arXiv + YouTube + x.ai triple. **Not** live grants. `allowed_tools` stays `[]`. Network, plugins, T3, memory writes, and production stay off.

### arXiv
- [2310.11511](https://arxiv.org/abs/2310.11511) — Self-RAG (already in study)

### YouTube (educational; do not paste transcripts into Chat)
- [Akari Asai, Self-reflective LMs with retrieval](https://www.youtube.com/watch?v=bVz8Ua1VVsE)

### xAI (non-activating vendor docs)
- [Already cited; still non-activating](https://docs.x.ai/developers/tools/overview)

