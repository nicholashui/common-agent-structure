# Domain knowledge — `specials.psychological-recommendation-agent`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation.

## Explainable recs, cold start, filter bubbles

A recommendation is incomplete without **why** (features used, trait used, what was not chosen). Cold start: no history → use stated traits and situational context (stress → lower intensity), not a fake viewing history.

Diversity: optimizing only predicted rating collapses to a filter bubble. Personality-aware recsys literature reports modest accuracy lifts when traits are used as side information — treat “5–10%” design claims as **unverified in this folder** unless a local eval says otherwise.

No live catalog, no tracking pixels, no memory writes of inferred personality.

## Sources

- Tkalčič, M. et al., personality-aware recommender systems (survey chapters; treat numeric lift as unverified here)
- Pariser, E. *The Filter Bubble* (2011) — diversity as a constraint
- HEXACO: https://hexaco.org — side features, not a live catalog
- Sibling: `agents/specials.psychological-profile-agent/sources/study/domain_knowledge.md`

## Triple research (design-time, 2026-09)

Design-time citations collected to complete the arXiv + YouTube + x.ai triple. **Not** live grants. `allowed_tools` stays `[]`. Network, plugins, T3, memory writes, and production stay off.

### arXiv
- [2101.12153](https://arxiv.org/abs/2101.12153) — Survey on personality-aware recommendation systems
- [2106.03060](https://arxiv.org/abs/2106.03060) — Big-Five vs HEXACO vs MBTI for personality-aware recs; cold start
- [2501.01945](https://arxiv.org/abs/2501.01945) — Cold-start recommendation in the LLM era — no fake history

### YouTube (educational; do not paste transcripts into Chat)
- [Trait theories lecture (Eysenck, Costa, McCrae, Cattell) — traits as rec side-features](https://www.youtube.com/watch?v=D33VOyGGib8)

### xAI (non-activating vendor docs)
- [No live catalog, no tracking pixels](https://docs.x.ai/developers/tools/overview)

