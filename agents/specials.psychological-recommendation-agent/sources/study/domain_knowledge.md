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
