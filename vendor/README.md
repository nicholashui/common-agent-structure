# Vendor copies

Self-contained copies of external sources. **Not file links.**

- `common-agent-swarm-ops/` — `testcases/api_test`, pack agent folders, and `docs/special_agents_redesign`. Media (mp3 and similar) is not copied; the importer already skips it.
- `va-agent-swarm/` — design corpus previously cited by agent user guides (untrusted provenance).

Refresh (only if a sibling checkout still exists on this machine):

```powershell
python tools/vendor_external_sources.py
```
