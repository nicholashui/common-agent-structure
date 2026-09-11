# Chat-level cases — `specials.llm-usage`

request counts are not the meter; no API keys stored. Do not invent eval PASS.

| File | Edge |
|---|---|
| `chat-llm-ambiguous.json` | ambiguous |
| `chat-llm-multi-intent.json` | multi-intent |
| `chat-llm-domain-specific.json` | domain-specific |
| `chat-llm-multilingual.json` | multilingual |
| `chat-llm-oos.json` | oos |
| `chat-llm-wait.json` | wait |
| `chat-llm-invent.json` | invent |
| `chat-llm-activation.json` | activation |
| `chat-llm-shift.json` | shift |
| `chat-llm-handoff.json` | handoff |


| `chat-sc1-split-ownership.json` | split-ownership (in-role vs sibling + fake PASS) |
| `chat-sc2-wait-underspecified.json` | underspecified wait |
| `chat-sc3-fake-meter.json` | invented ≥95%/CLIP-T/casops-eval meter |

Existing `chat-tc1`–`10` stay.
