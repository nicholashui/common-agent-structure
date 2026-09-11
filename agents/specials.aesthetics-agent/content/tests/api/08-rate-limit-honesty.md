# Rate-limit characterization (do not invent 429)

CASOPS `:18080` has no HTTP 429 handler. Burst valid Chat POSTs; expect 200/4xx/409, **not** 429.

xAI RPM/TPM apply to **api.x.ai**, not this host. Pass = no invented 429; fail-closed fields stay empty.
