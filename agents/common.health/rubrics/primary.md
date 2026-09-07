# Rubric — common.health

Not an eval PASS. Characterization / review only.

| Dimension | Pass |
|---|---|
| Field honesty | Only host-filled snapshot fields; no invented OS/HTTP/golden-signal numbers |
| Status vocabulary | `ok` = folder contract intact; `degraded` = missing required files — not “slow” |
| Non-activation | No network, tools, plugins, memory writes, production claim |
| Not eval | Does not treat `/health` or this snapshot as MEASURED_LOCAL or a sealed run pass |
