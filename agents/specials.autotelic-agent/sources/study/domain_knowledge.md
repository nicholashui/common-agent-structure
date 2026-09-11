# Domain knowledge — `specials.autotelic-agent`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation.

## Autotelic ≠ random curiosity

From Greek *auto* (self) + *telos* (goal): an autotelic agent **represents, generates, selects, and masters its own goals** (Colas, Karch, Sigaud, Oudeyer, JAIR 2022, arXiv:2012.09830). It is a special case of intrinsic motivation, which is a special case of autonomy.

**IMGEP** (Intrinsically Motivated Goal Exploration Processes) is the developmental-robotics family: self-generate parameterized goals, pick them by learning progress, reuse trajectories across goals (Baranes & Oudeyer; Forestier et al.). **RL-IMGEP** ports that to goal-conditioned deep RL. **EMGEP** is the externally motivated counterpart (goals supplied by a teacher).

## Safety-oriented reading for this folder

Open-ended self-goal generation without a budget is a runaway loop. On this host:

- Goals must be representable as structured artifacts with a stop condition.
- Intrinsic reward may not grant tools, network, or memory writes.
- A human gate remains on production activation; “autotelic” does not mean unsupervised live training.
- Prefer competence-based intrinsic motivation (progress on self-goals) over novelty-only noise.

## Sources

- Colas et al., Autotelic Agents with IMGEP / goal-conditioned RL, arXiv:2012.09830 / JAIR 74 (2022)
- Colas, *Towards Vygotskian Autotelic Agents* (PhD, Bordeaux, 2021)

## Triple research (design-time, 2026-09)

Design-time citations collected to complete the arXiv + YouTube + x.ai triple. **Not** live grants. `allowed_tools` stays `[]`. Network, plugins, T3, memory writes, and production stay off.

### arXiv
- [2012.09830](https://arxiv.org/abs/2012.09830) — Colas et al., Autotelic Agents / IMGEP (already in study)

### YouTube (educational; do not paste transcripts into Chat)
- [Oudeyer, Developmental Machine Learning, ICLR 2019 keynote (IMGEP)](https://www.youtube.com/watch?v=7bJ0fnvPLaA)
- [Oudeyer, MIT Embodied Intelligence seminar (curiosity / IMGEP)](https://www.youtube.com/watch?v=Jx6-DKXgAKU)

### xAI (non-activating vendor docs)
- [Tools overview — naming tools is not a live-training grant](https://docs.x.ai/developers/tools/overview)

