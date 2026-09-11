# Domain knowledge — `video.cinematographer`

Design-time unique paper/book/standard set (2026-09). Does not enable providers, MCP, network, plugins, memory writes, or production activation. `allowed_tools` stays empty. CLIP-T / arena / VBench numbers are design priors unless this host measures them.

## Owns

Owns lensing, lighting, composition, look.

## Craft

Exposure and movement are numbers (focal length, T-stop, path), not adjectives. ACES is a color-management intent, not an enabled pipeline on this host.

## Sources (unique to this agent)

- Blain Brown, *Cinematography: Theory and Practice*
- ASC, *American Cinematographer Manual*
- Academy Color Encoding System (ACES) documentation — https://www.oscars.org/science-technology/aces
- CamTrol, arXiv:2406.10126 — camera path as data, not prompt poetry

## Shared (generation crafts only)

If this role specifies camera/motion for generative video, control strength is 3D/layout → start/end frames → ControlNet-style passes → text (Flick 2026; NVIDIA RTX video guide; BlenderFusion arXiv:2506.17450). Skip this if the role is legal, archive, finance, or ratings.

## Honesty

Does not enable providers, MCP, network, plugins, memory writes, or production activation. `allowed_tools` stays empty. CLIP-T / arena / VBench numbers are design priors unless this host measures them.

## Triple research (design-time, 2026-09)

Design-time citations collected to complete the arXiv + YouTube + x.ai triple. **Not** live grants. `allowed_tools` stays `[]`. Network, plugins, T3, memory writes, and production stay off.

### arXiv
- Unique arXiv/book set remains in `## Sources (unique to this agent)` above. Do not duplicate Bordwell/CLIP-T off-role.

### YouTube (educational; do not paste transcripts into Chat)
- [Camera movements for beginners](https://www.youtube.com/watch?v=KupEY5CAwe4)

### xAI (non-activating vendor docs)
- [Imagine image-to-video — not enabled](https://docs.x.ai/developers/model-capabilities/video/image-to-video)
- [Imagine overview — vendor name is not an allow-list](https://x.ai/docs/guides/image-generations)

