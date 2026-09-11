# Research log — specials.intent-analysis-agent

Date: 2026-09-11. Craft: intent analysis / NLU / speech-act labelling. Not a generic “agent skills harness”.

The packaged agent does **not** gain network or tools from this search. Citations below were checked against arXiv / xAI docs / YouTube titles. Do not invent IDs.

## A. Host contract (this repo)

- `agent_spec.json`: `status: draft`, `allowed_tools: []`, `network_access: false`, `production_activation_requested: false`, `va_category: null`.
- Chat packs `prompts/primary.md` from `## System` until `## Developer`.
- Fixtures: `casops.testcase.v1`, `honesty: CHARACTERIZATION`. Chat 200 ≠ agent-correct (ISSUE-0002).
- Public plane: `/api/v3` only. Mutation POSTs need `x-casops-actor`, `x-casops-reason`, `x-casops-expected-parent`, `x-casops-dry-run`.

## B. arXiv — implement vs skip

| ID | Title | Takeaway for this folder | Decision |
|---|---|---|---|
| 2509.10010 | Multi-Intent Recognition in Dialogue Understanding | MultiWOZ 2.1; few-shot LLMs vs BERT; multi-label, not single-class | **Implement**: list each intent |
| 2507.22289 | Intent Recognition and OOS Detection (SIGDIAL 2025) | OOS is first-class in multi-party dialogue | **Implement**: Scope field |
| 2506.01881 | WHEN TO ACT, WHEN TO WAIT (STORM) | Semantically complete ≠ triggerable | **Implement**: Triggerability / wait |
| 2411.14252 | Chain-of-Intent / MINT-CL (CIKM 2025) | Multi-turn, multilingual intent shift | **Implement**: history is data |
| 2503.21544 | SWI: Speaking with Intent | Explicit intent-before-sentence improves reviewability | **Implement** as reply *structure*, not `<INTENT>` tags (token budget) |
| 2603.28929 | Known Intents, New Combinations | Compositional pairs/triples; clause-factorized decoding | **Implement**: do not assume co-occurrence |
| 2609.05975 | Intent Drift at SME Scale | Purpose + constrained tools + scope ledger + pre-action check | **Skip live**: would require tools/writes |

## C. xAI

- https://docs.x.ai/developers/tools/overview — built-in tools vs function calling.
- https://docs.x.ai/developers/models/grok-4 — function calling, structured outputs; **xAI** RPM limits (not CASOPS).
- This pack: do not set `tool_choice`, do not add MCP, do not enable Docs MCP.

## D. YouTube (educational)

- https://www.youtube.com/watch?v=FItTy4yizlw — Searle & Magee 1977, illocution vs perlocution.
- https://www.youtube.com/watch?v=kX0Nks4P6fw — SWI paper explainer (Arxiv Papers). Summarize; do not paste transcripts.

## E. Applied to files

Packed How to reply now has multi-intent, triggerability, OOS, multilingual locution, refuse tools. Operator study lives under `content/`. Extra NLU fixtures are CHARACTERIZATION only.
