# Operator content — `specials.general-creative-agent`

This folder is **operator study**. The host still loads `prompts/primary.md`, `sources/study/domain_knowledge.md`, `evals/fixtures/*.json`, and `agent_spec.json`.

Skill `casops.skill.creative.sparse-recombination` is **declared** and **not host-granted**. Tools, network, plugins, memory writes, production, and vendor generation stay off.

```
content/
  README.md
  research/sources.md
  tests/chat/
  tests/api/
  tests/multi-agent/
  test_guide.md
```

Host-loadable copies of edge chat cases: `evals/fixtures/chat-gca-*.json`.
