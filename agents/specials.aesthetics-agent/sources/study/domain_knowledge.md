# Domain knowledge — `specials.aesthetics-agent`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation.

## Separate technical quality from taste

Image **quality** (blur, noise, compression) is not **aesthetics** (composition, style, cultural preference). NIMA (Talebi & Milanfar, arXiv:1709.05424) predicts the *distribution* of human opinion scores, not a single scalar, because raters disagree. A naked 0–10 score without a vector and a confidence is a hack surface.

## CLIP-linear predictors are not “artiste sense”

LAION-Aesthetics Predictor is a linear head on CLIP embeddings trained to answer “how much do you like this image 1–10?” ([LAION blog](https://laion.ai/blog/laion-aesthetics/), GitHub `LAION-AI/aesthetic-predictor`). It is widely used to curate training data. An audit (Taylor et al., arXiv:2601.09896) finds the predictor over-represents Western/Japanese landscape and portrait conventions and filters captions unevenly by gender and LGBTQ+ mention. Treat LAP as a **dataset-curation prior**, not a universal critic.

Hentschel, Wiradarma, and Sack, “CLIP knows image aesthetics” (Frontiers in AI, 2022) show CLIP linear probes transfer to AVA better than ImageNet backbones, but still need an explicit taste profile.

## Operating rules for this folder

- Always emit a dimension vector (composition, color, light, depth, subject, technical, emotion, style fidelity, novelty, temporal) plus `hack_likelihood`.
- Score only under a named `AestheticProfile` or a declared neutral baseline.
- Low confidence or high hack likelihood → escalate; do not average away disagreement.
- Live vision and reward-model training stay fail-closed on this host.

## Sources

- Talebi & Milanfar, NIMA, arXiv:1709.05424
- LAION-Aesthetics, https://laion.ai/blog/laion-aesthetics/
- Taylor et al., algorithmic gaze of LAP, arXiv:2601.09896
- Hentschel et al., CLIP knows image aesthetics, doi:10.3389/frai.2022.976235
