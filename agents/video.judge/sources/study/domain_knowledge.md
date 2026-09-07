# Domain knowledge — `video.judge`

Design-time unique paper/book/standard set (2026-09). Does not enable providers, MCP, network, plugins, memory writes, or production activation. `allowed_tools` stays empty. CLIP-T / arena / VBench numbers are design priors unless this host measures them.

## Owns

Owns accept/refine/escalate against a rubric, not a review essay.

## Craft

LLM-as-judge literature. Do not claim arena win-rate. Max refinements then HiTL.

## Sources (unique to this agent)

- Zheng et al., Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena, arXiv:2306.05685
- Liang et al., HELM, arXiv:2211.09110
- host max_refinement_count in `agent_spec.json`

## Shared (generation crafts only)

If this role specifies camera/motion for generative video, control strength is 3D/layout → start/end frames → ControlNet-style passes → text (Flick 2026; NVIDIA RTX video guide; BlenderFusion arXiv:2506.17450). Skip this if the role is legal, archive, finance, or ratings.

## Honesty

Does not enable providers, MCP, network, plugins, memory writes, or production activation. `allowed_tools` stays empty. CLIP-T / arena / VBench numbers are design priors unless this host measures them.
