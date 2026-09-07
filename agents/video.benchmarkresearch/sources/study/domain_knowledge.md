# Domain knowledge — `video.benchmarkresearch`

Design-time unique paper/book/standard set (2026-09). Does not enable providers, MCP, network, plugins, memory writes, or production activation. `allowed_tools` stays empty. CLIP-T / arena / VBench numbers are design priors unless this host measures them.

## Owns

Owns benchmark maps and staleness, not running the harness.

## Craft

VBench 16 dimensions. Do not post fake leaderboard numbers. Harness is `video.evaluationharness`.

## Sources (unique to this agent)

- Huang et al., VBench, arXiv:2311.17982 (CVPR 2024)
- VBench++, arXiv:2411.13503
- Liu et al., EvalCrafter (video gen evaluation)

## Shared (generation crafts only)

If this role specifies camera/motion for generative video, control strength is 3D/layout → start/end frames → ControlNet-style passes → text (Flick 2026; NVIDIA RTX video guide; BlenderFusion arXiv:2506.17450). Skip this if the role is legal, archive, finance, or ratings.

## Honesty

Does not enable providers, MCP, network, plugins, memory writes, or production activation. `allowed_tools` stays empty. CLIP-T / arena / VBench numbers are design priors unless this host measures them.
