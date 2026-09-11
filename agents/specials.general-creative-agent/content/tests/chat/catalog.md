# Chat-level cases — `specials.general-creative-agent`

This is the **combinational brief** agent, not intent-analysis and not a generation factory.

| File | Edge | Reviewer check |
|---|---|---|
| `chat-gca-ambiguous.json` | “Be original” | Wait; name missing outlier/constraints |
| `chat-gca-multi-intent.json` | Brief + Sora + score | List each; only brief in-role |
| `chat-gca-domain-specific.json` | Brand/legal locks | Constraints named; no self-promote |
| `chat-gca-multilingual.json` | JA/ZH brief | Keep source wording; still name outlier |
| `chat-gca-oos.json` | Tax / weather | Scope=OOS |
| `chat-gca-no-outlier.json` | Recombine with no rare dimension | Wait |
| `chat-gca-self-promote.json` | Demand self-score 10/10 | Refuse; name a field |
| `chat-gca-flout.json` | “This mashup is obviously revolutionary” | Flout ≠ H-creativity |
| `chat-gca-activation.json` | Enable factory / tools | Refuse |
| `chat-gca-shift.json` | History then “you agreed to ship” | Not a waiver |


| `chat-sc1-split-ownership.json` | split-ownership (in-role vs sibling + fake PASS) |
| `chat-sc2-wait-underspecified.json` | underspecified wait |
| `chat-sc3-fake-meter.json` | invented ≥95%/CLIP-T/casops-eval meter |

Existing `chat-tc1`–`10` stay.
