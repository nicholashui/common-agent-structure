# Domain knowledge — `specials.controller-agent`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation.

## Why Blender (or any 3D blockout) exists in an AI video loop

Text-only camera prompts (“slow dolly in, slight handheld”) are under-specified. A 3D blockout makes **focal length, path, and timing** executable. 2026 production practice (Flick, NVIDIA RTX video guide) uses three control strengths:

1. **Motion reference** — export a blockout clip; the video model copies camera/action.
2. **Start/end frames** — render viewport stills; image-to-video interpolates.
3. **Render passes** — depth, Canny, OpenPose into ControlNet/ComfyUI for frame-exact structure.

BlenderFusion (arXiv:2506.17450) and CamTrol (arXiv:2406.10126) formalize 3D-grounded camera control: edit camera/object in a scene graph, then let a generative compositor fuse. Seedance-style “clay render → video” is the same idea at product level.

## Honesty on this host

- Naming Veo, Sora, Runway, Kling, or Blender MCP in design text is **not** an allow-list. `allowed_tools` stays `[]`; `network_access` stays false.
- Controllability claims need a stated control map (camera path, pose, depth). A fluent prompt is not control.
- Escalate rights, likeness, and commercial model licenses; do not activate providers.

## Sources

- Flick, *Blender for AI Filmmaking: The 2026 Guide*
- NVIDIA, RTX AI video generation guide (Blender layout → keyframes)
- BlenderFusion, arXiv:2506.17450
- CamTrol, arXiv:2406.10126

## Triple research (design-time, 2026-09)

Design-time citations collected to complete the arXiv + YouTube + x.ai triple. **Not** live grants. `allowed_tools` stays `[]`. Network, plugins, T3, memory writes, and production stay off.

### arXiv
- [2506.17450](https://arxiv.org/abs/2506.17450) — BlenderFusion (already in study)
- [2406.10126](https://arxiv.org/abs/2406.10126) — CamTrol (already in study)

### YouTube (educational; do not paste transcripts into Chat)
- [Camera Movements for Beginners — pan/tilt/dolly vs text-only prompts](https://www.youtube.com/watch?v=KupEY5CAwe4)
- [The Art of Camera Movement (House of Tabula)](https://www.youtube.com/watch?v=ptQwvGcLZIw)

### xAI (non-activating vendor docs)
- [Imagine image-to-video — design-time; not enabled here](https://docs.x.ai/developers/model-capabilities/video/image-to-video)
- [Imagine overview (image/video) — vendor names are not allow-lists](https://x.ai/docs/guides/image-generations)

