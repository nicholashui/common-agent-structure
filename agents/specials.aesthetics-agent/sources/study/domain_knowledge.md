# Domain knowledge — `specials.aesthetics-agent`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation.

This agent **owns critique of visual taste vs technical quality**. It does not own filming, planning, retrieval, or live vision. xAI image/tool APIs are vendor docs, not a grant.

## Separate technical quality from taste

Image **quality** (blur, noise, compression) is not **aesthetics** (composition, style, cultural preference). NIMA (Talebi & Milanfar, arXiv:1709.05424) predicts the *distribution* of human opinion scores, not a single scalar, because raters disagree. A naked 0–10 score without a vector and a confidence is a hack surface.

## CLIP-linear predictors are not “artiste sense”

LAION-Aesthetics Predictor is a linear head on CLIP embeddings trained to answer “how much do you like this image 1–10?” ([LAION blog](https://laion.ai/blog/laion-aesthetics/)). An audit (Taylor et al., arXiv:2601.09896) finds it over-represents Western/Japanese landscape and portrait conventions and filters captions unevenly by gender and LGBTQ+ mention. Treat LAP as a **dataset-curation prior**, not a universal critic.

Hentschel, Wiradarma, and Sack, “CLIP knows image aesthetics” (Frontiers in AI, 2022) show CLIP linear probes transfer to AVA better than ImageNet backbones, but still need an explicit taste profile.

## Findings that change this folder (implement)

| Finding | Change in this pack |
|---|---|
| NIMA: predict a distribution, not MOS (arXiv:1709.05424) | Dimension vector + confidence; never a naked scalar |
| LAP encodes a narrow gaze (arXiv:2601.09896) | Named `AestheticProfile` or declared baseline; do not cite LAP as measured |
| MLLM aesthetic scores can be demographically biased (AesBiasBench, arXiv:2509.11620, EMNLP 2025) | `hack_likelihood` up if the ask wants a universal “human taste” number |
| Absolute MOS is brittle; relative/attribute critique generalizes better (arXiv:2606.05778) | Prefer attribute critique and pairwise “what to change”; do not invent PLCC/SRCC |
| VLMs encode aesthetic attributes that can personalize without fine-tuning (arXiv:2604.11374) | **Skip live vision.** Use the verbal description if one is given; do not call a VLM |
| Charm (CVPR 2025, arXiv:2504.02522): keep aspect ratio / high-res for IAA | If a still is described as cropped or stretched, flag **technical** not taste |
| Multi-intent operator text (NLU, arXiv:2509.10010) | List score vs restyle vs train; only critic is in-role |
| OOS (arXiv:2507.22289) | Non-aesthetic asks get Scope=OOS, not a fake vector |
| Semantically complete ≠ action-ready (arXiv:2506.01881) | “Make it nicer” without pixels/profile → wait; do not invent a look |

## Skip as live enablement

| Source | Why skipped on this host |
|---|---|
| Charm / NIMA / VLM PIAA inference | Would require vision tools and network. `allowed_tools: []` |
| xAI function calling / image understanding ([tools overview](https://docs.x.ai/developers/tools/overview)) | Vendor Grok capability, not a grant |
| SPEC “production-grade artiste sense / reward signal every fine-tune trusts” | Untrusted `### Domain distillation` |
| Skill live ON | Declared `casops.skill.aesthetics.dimension-vector`; host register skills/tools empty |

## Operating rules

- Always emit the ten-dimension vector plus `hack_likelihood`.
- Score only under a named `AestheticProfile` or a declared neutral baseline.
- Low confidence or high hack likelihood → escalate; do not average away disagreement.
- Live vision and reward-model training stay fail-closed.

## Sources

### Craft (unique to this agent)

- Talebi & Milanfar, NIMA, arXiv:1709.05424 — https://arxiv.org/abs/1709.05424
- LAION-Aesthetics — https://laion.ai/blog/laion-aesthetics/
- Taylor et al., algorithmic gaze of LAP, arXiv:2601.09896 — https://arxiv.org/abs/2601.09896
- Hentschel et al., CLIP knows image aesthetics, doi:10.3389/frai.2022.976235
- Li et al., AesBiasBench, arXiv:2509.11620 (EMNLP 2025) — https://arxiv.org/abs/2509.11620
- Behrad et al., Charm, arXiv:2504.02522 (CVPR 2025) — https://arxiv.org/abs/2504.02522
- *Beyond Absolute Scores*, arXiv:2606.05778 — https://arxiv.org/abs/2606.05778
- Ryu & Yanaka, VLM PIAA internals, arXiv:2604.11374 — https://arxiv.org/abs/2604.11374

### NLU (how briefs are read; this agent still scores aesthetics)

- arXiv:2509.10010 multi-intent list
- arXiv:2507.22289 OOS label
- arXiv:2506.01881 wait when not triggerable

### xAI (non-activating)

- https://docs.x.ai/developers/tools/overview

### YouTube (educational; do not paste transcripts)

- NIMA talk, Peyman Milanfar — https://www.youtube.com/watch?v=xMD3RXUCWtg
- EI 2025 plenary (Milanfar; NIMA as a score histogram) — https://www.youtube.com/watch?v=s59UTnEwBL4
