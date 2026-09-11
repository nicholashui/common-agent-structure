# Domain knowledge — `specials.knowledge-router-agent`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation.

## Routing is not “give the agent the whole corpus”

Lewis RAG (arXiv:2005.11401) already showed parametric vs non-parametric memory. Routing adds *which specialist* and *which slice* of the corpus.

A practical stack (named in this folder’s design text, grounded here):

1. **Metadata first** — agent_id, domain, license, recency. Cheap and explainable.
2. **Centroid / cluster** — RopMura-style training-free assignment to a specialist bucket.
3. **Self-RAG reflection** (Asai et al., arXiv:2310.11511) — Retrieve / IsRel / IsSup / IsUse on the candidate slice.
4. **CRAG corrective** (Yan et al., arXiv:2401.15884) — Correct / Incorrect / Ambiguous then rewrite or abstain.
5. **Downstream utility** — a routing decision is wrong if the specialist still fails, even if retrieval looked relevant.

## Honesty on this host

- There is no 5,000-file live index in CASOPS Chat. Route over **this folder’s `sources/`** and operator-supplied text.
- Explain the route (why this slice, why not that agent). Unexplained “I picked the best docs” is not a router.
- Do not grant graph DBs, GNNs, or network search.

## Sources

- Lewis et al., RAG, arXiv:2005.11401
- Asai et al., Self-RAG, arXiv:2310.11511
- Yan et al., CRAG, arXiv:2401.15884

## Triple research (design-time, 2026-09)

Design-time citations collected to complete the arXiv + YouTube + x.ai triple. **Not** live grants. `allowed_tools` stays `[]`. Network, plugins, T3, memory writes, and production stay off.

### arXiv
- [2005.11401](https://arxiv.org/abs/2005.11401) — Lewis RAG (already in study)
- [2310.11511](https://arxiv.org/abs/2310.11511) — Self-RAG (already in study)

### YouTube (educational; do not paste transcripts into Chat)
- [Akari Asai, Self-reflective LMs with retrieval (UMass ML lunch)](https://www.youtube.com/watch?v=bVz8Ua1VVsE)

### xAI (non-activating vendor docs)
- [Files & Collections mentioned as RAG pipelines — this host has no live index](https://x.ai/docs/developers/quickstart)
- [Collections/Web Search are vendor tools; allowed_tools stays empty](https://docs.x.ai/developers/tools/overview)

