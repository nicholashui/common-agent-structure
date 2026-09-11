# Domain knowledge — `specials.general-creative-agent`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation.

This agent **owns combinational briefs with named constraints**. It does not own filming, aesthetic scoring, vendor generation, or self-promotion.

## Combinatorial creativity vs sparse recombination

Boden’s split: **combinational**, **exploratory**, and **transformational**. “Strategic Sparse Outlier Recombination” here is a combinational claim: hold most of the distribution, recombine a rare part. That only works if:

- Outliers are *specified* (which dimension is rare).
- Recombination is *constrained* (audience, medium, brand, legal) and the link is *intelligible* (not shaking marbles).
- Evaluation is *separate* from generation.

Csikszentmihalyi’s domain–field–individual: novelty without a field is private play (P-creativity, not H-creativity).

## Findings that change this folder (implement)

| Finding | Change in this pack |
|---|---|
| Boden three types; combinational = unfamiliar combinations of familiar ideas | Packed **Boden type** line; default combinational |
| Combinatorial creativity is open-ended; novelty–utility tradeoff; ideation ≠ execution (Schapiro et al., arXiv:2509.21043) | Name novelty vs utility; do not claim a shoot/train/ship |
| IEI: identify input spaces, shared attributes, implication (arXiv:2504.13120) | Held-constant + outlier + recombination rule |
| Structured recombination, not token-level paraphrase (Mizrahi et al., DishCOVER, arXiv:2504.20643) | Recombination rule must be named |
| Idea-generation surveys: Boden + novelty vs soundness (arXiv:2511.07448; arXiv:2412.14141) | Constraints + separate evaluator |
| Multi-intent briefs (arXiv:2509.10010) | List brief vs generate vs score; only brief in-role |
| OOS (arXiv:2507.22289) | Non-creative asks get Scope=OOS |
| Wait when not triggerable (arXiv:2506.01881) | Missing outlier/constraints → wait, not a factory |

## Skip as live enablement

| Source | Why skipped |
|---|---|
| SPEC “production-grade SSOR factory / 7-phase process” | Untrusted `### Domain distillation` |
| VLM mashup generation (arXiv:2504.13120 generation pipeline) | Would need vision/tools |
| xAI function calling / image gen ([tools overview](https://docs.x.ai/developers/tools/overview)) | Vendor, not a grant |
| Skill live ON | Declared `casops.skill.creative.sparse-recombination`; register empty |

## Honesty

- Do not treat the long SSOR dump as an enabled factory.
- Do not invent arXiv IDs. Do not self-promote artifacts.

## Sources

- Boden, *The Creative Mind* — combinational / exploratory / transformational; P- vs H-creativity
- Csikszentmihalyi, flow and domain–field–individual
- Schapiro et al., Combinatorial Creativity, arXiv:2509.21043 — https://arxiv.org/abs/2509.21043
- IEI / CreativeMashup, arXiv:2504.13120 — https://arxiv.org/abs/2504.13120
- Mizrahi et al., Cooking Up Creativity / DishCOVER, arXiv:2504.20643 — https://arxiv.org/abs/2504.20643
- LLMs combinatorial scientific ideas, arXiv:2412.14141 — https://arxiv.org/abs/2412.14141
- LLM scientific ideation survey, arXiv:2511.07448 — https://arxiv.org/abs/2511.07448
- NLU (briefs only): arXiv:2509.10010, 2507.22289, 2506.01881
- YouTube: Boden AGI-12 — https://www.youtube.com/watch?v=_zp6KOo9ZHQ ; Boden *The Creative Mind* — https://www.youtube.com/watch?v=WblRBrgYOBU
- xAI tools — https://docs.x.ai/developers/tools/overview
