# common.health

Sample v3 agent derived from `casops.template.baseline_safe`.

On run, the **host** observes local control-plane and folder facts and seals them as the run artifact. The agent does not own `/health`, does not call the network, and does not write memory.

Profile: `baseline_safe` (local deterministic host observe, T0 cache, memory `none`, no plugins, improvement disabled).
