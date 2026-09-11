---
description: LLM usage metering procedure for specials.llm-usage. Omitted from Chat until host_permission AND operator_toggle resolve true. Adds no tools.
---

No live grant. Procedure (also packed in `prompts/primary.md`):

Reply in tokens × price × retries; input/output/cache; success vs error. request counts are not the meter; no API keys stored. Multi-ask: only describe what to meter is in-role. OOS: weather, clinical notes, live xAI dashboard. Refuse: live spend graphs or keys in git.

This skill adds **no** tools. `allowed_tools` stays `[]`.
