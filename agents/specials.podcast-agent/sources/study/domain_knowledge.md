# Domain knowledge — `specials.podcast-agent`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation.

## Craft vs measurement

Host craft is prep → record → close → follow-up, balancing script and live conversation. That is not the same as **audience numbers**.

IAB Tech Lab Podcast Technical Measurement Guidelines (v2.2 certified; v2.3 public comment 2026) count **downloads from server logs**, not listeners. A valid download typically requires ID3 plus ~1 minute of audio (or 100% of a tiny file), with pre-load filtering. Apple / Spotify / YouTube first-party numbers are **not** IAB-comparable ([Podnews](https://podnews.net/article/understanding-podcast-statistics); [TV Tech on v2.3](https://www.tvtechnology.com/platform/streaming/iab-tech-lab-updates-podcast-technical-measurement-guidelines)).

Do not invent download graphs. This folder has no RSS fetcher.

## Sources

- IAB Tech Lab Podcast Measurement Guidelines v2.2 / v2.3
- Podnews, “How to understand podcast stats”

## Triple research (design-time, 2026-09)

Design-time citations collected to complete the arXiv + YouTube + x.ai triple. **Not** live grants. `allowed_tools` stays `[]`. Network, plugins, T3, memory writes, and production stay off.

### arXiv
- [2106.06605](https://arxiv.org/abs/2106.06605) — Modeling language usage and listener engagement in podcasts — stream rate ≠ download count
- [2411.07892](https://arxiv.org/abs/2411.07892) — Structured Podcast Research Corpus — RSS ecosystem, not a live fetcher here
- [2412.05516](https://arxiv.org/abs/2412.05516) — Pandora audio-ad load field experiment — listening hours ≠ IAB downloads

### YouTube (educational; do not paste transcripts into Chat)
- [IAB Tech Lab Audio Initiatives — podcast measurement working group (downloads vs listeners)](https://www.youtube.com/watch?v=_cygjTdeits)
- [Podcast Stats Explained (downloads vs retention)](https://www.youtube.com/watch?v=kz7wIhQP6gM)

### xAI (non-activating vendor docs)
- [Voice/TTS prices are vendor; this pack has no RSS fetcher](https://docs.x.ai/developers/pricing)

