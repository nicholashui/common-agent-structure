# Domain knowledge — `video.dronepilot`

Design-time unique paper/book/standard set (2026-09). Does not enable providers, MCP, network, plugins, memory writes, or production activation. `allowed_tools` stays empty. CLIP-T / arena / VBench numbers are design priors unless this host measures them.

## Owns

Aerial camera paths under safety and airspace constraints.

## Craft

Height, speed, and parallax are numbers. Fail closed on unlicensed airspace. This host does not fly a drone.

## Sources (unique to this agent)

- FAA 14 CFR Part 107 (US small UAS) — https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-107
- EASA UAS regulations (design analog outside US)
- Aerial cinematography: altitude vs compression (Brown / ASC operating notes)

## Shared (generation crafts only)

If this role specifies camera/motion for generative video, control strength is 3D/layout → start/end frames → ControlNet-style passes → text (Flick 2026; NVIDIA RTX video guide; BlenderFusion arXiv:2506.17450). Skip this if the role is legal, archive, finance, or ratings.

## Honesty

Does not enable providers, MCP, network, plugins, memory writes, or production activation. `allowed_tools` stays empty. CLIP-T / arena / VBench numbers are design priors unless this host measures them.

## Triple research (design-time, 2026-09)

Design-time citations collected to complete the arXiv + YouTube + x.ai triple. **Not** live grants. `allowed_tools` stays `[]`. Network, plugins, T3, memory writes, and production stay off.

### arXiv
- Unique arXiv/book set remains in `## Sources (unique to this agent)` above. Do not duplicate Bordwell/CLIP-T off-role.

### YouTube (educational; do not paste transcripts into Chat)
- [DJI Film School, camera movement with Brandon Li](https://www.youtube.com/watch?v=IlptzH1NqhQ)

### xAI (non-activating vendor docs)
- [Imagine image-to-video — not enabled](https://docs.x.ai/developers/model-capabilities/video/image-to-video)
- [Imagine overview — vendor name is not an allow-list](https://x.ai/docs/guides/image-generations)

