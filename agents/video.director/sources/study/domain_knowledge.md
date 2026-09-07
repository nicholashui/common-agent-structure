# Domain knowledge — `video.director`

Design-time unique paper/book/standard set (2026-09). Does not enable providers, MCP, network, plugins, memory writes, or production activation. `allowed_tools` stays empty. CLIP-T / arena / VBench numbers are design priors unless this host measures them.

## Owns

Owns vision, shot intent, pacing, take approval.

## Craft

Shot intent is a contract: size, angle, move, duration, whose look, what changes on the cut. Text-only “cinematic dolly” is not intent. Control strength: 3D camera blockout → start/end frames → depth/pose passes → text last.

## Sources (unique to this agent)

- Bordwell, Thompson, Staiger, *The Classical Hollywood Cinema* (1985) — coverage and continuity as a system
- BlenderFusion, arXiv:2506.17450 — 3D-grounded camera/object edit then generative composite
- CamTrol, arXiv:2406.10126 — training-free camera control for video diffusion
- DGA creative-rights practice (design) — director vs editor/DoP handoff

## Shared (generation crafts only)

If this role specifies camera/motion for generative video, control strength is 3D/layout → start/end frames → ControlNet-style passes → text (Flick 2026; NVIDIA RTX video guide; BlenderFusion arXiv:2506.17450). Skip this if the role is legal, archive, finance, or ratings.

## Honesty

Does not enable providers, MCP, network, plugins, memory writes, or production activation. `allowed_tools` stays empty. CLIP-T / arena / VBench numbers are design priors unless this host measures them.
