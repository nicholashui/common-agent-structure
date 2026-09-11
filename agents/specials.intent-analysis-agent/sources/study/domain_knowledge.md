# Domain knowledge — `specials.intent-analysis-agent`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation.

This agent **owns analysis of operator text**. It does not own planning, filming, retrieval, or tool execution. xAI function-calling docs describe Grok tools; this pack’s `allowed_tools` stays `[]`.

## Speech acts, not “hidden agenda” as a vibe

Austin (*How to Do Things with Words*): **locution** (what is said), **illocution** (the act performed *in* saying), **perlocution** (the effect *by* saying). Searle (*Speech Acts*, 1969) taxonomizes illocutions as **assertives, directives, commissives, expressives, declarations**.

Grice’s cooperative principle and maxims (Quantity, Quality, Relation, Manner) explain **implicature**: what is meant beyond what is said. Violating a maxim *on purpose* (irony, understatement) is still cooperative; that is not the same as deception.

## Dialogue-act annotation

ISO 24617-2 (SemAF — Dialogue acts, 2012, recertified 2020) is the interoperable annotation scheme (DiAML) for communicative functions in spoken, written, and multimodal dialogue (Bunt et al., DialogBank). Prefer ISO function labels over inventing a private “DIA v2.0” taxonomy unless the extra labels are defined and mapped.

## Findings that change this folder (implement)

| Finding | Change in this pack |
|---|---|
| Multi-intent utterances are common; collapsing them to one class loses recall (Ahmad et al., arXiv:2509.10010 on MultiWOZ 2.1; Nandy, arXiv:2603.28929 on compositional pairs) | Packed **How to reply** lists **each** intent. Do not pick a single winner. |
| Out-of-scope is a first-class label, not a nearest-neighbour known class (Castillo-López et al., arXiv:2507.22289, SIGDIAL 2025) | **Scope** field: in-scope vs OOS for the *analysed* domain. Refuse forced mapping. |
| Semantically complete ≠ action-ready (Qian et al., arXiv:2506.01881, STORM / intent-action alignment) | **Triggerability**: wait / not triggerable when structure is missing. Do not execute. |
| Multi-turn intent can shift; history is data, not a waiver (Liu et al., arXiv:2411.14252, Chain-of-Intent / MINT-CL) | Analyse the latest turn against history. Prior bubbles do not grant tools. |
| Indirect speech acts: locution can be a question while illocution is a request | Name both. Do not treat politeness as uncertainty about the act. |
| Multilingual locution should stay in the source language; illocution labels stay in the packed English taxonomy | **Locution** keeps source wording. Do not “translate away” the act. |
| Explicit intent-before-action helps *this agent’s own reply* stay reviewable (Yin et al., arXiv:2503.21544, SWI) | Reply structure is locution → illocution → implicature → triggerability. Do not wrap every sentence in `<INTENT>` tags (token budget). |
| xAI tool calling exists; `tool_choice` can be none | Skip live enablement. This pack does not call functions. |

## Skip as live enablement

| Source | Why skipped on this host |
|---|---|
| Voroshilov, arXiv:2609.05975 (Chain of Intent *governance*: purpose, constrained tools, scope ledger, pre-action check) | Correct as *design advice* for firms that grant tools. This pack must not gain tools, a ledger writer, or production activation. Record the four controls as **peer/host** concerns, not this agent’s runtime. |
| xAI Agent Tools / function calling / Docs MCP (`https://docs.x.ai/developers/tools/overview`, `https://docs.x.ai/api/mcp`) | Vendor capability of Grok, not a grant. `allowed_tools: []`, `network_access: false`. Host tool grant is `permissions/register.json` ∩ spec (both empty). |
| Skill AND-gate (ISO-style FR-SKL) | **Gated, not live:** `casops.skill.intent.speech-act` is declared; `host_permission` is read from `permissions/register.json`, not from `bindings.json`. |
| SPEC “DIA v2.0 production-ready” / native search / 1M context | Untrusted design provenance under `### Domain distillation`. Chat packing stops before that dump when `## System` is absent; with `## System` present, packing stops at `## Developer`. |

## Honesty on this host

- The folder already lists Austin, Searle, Lakoff & Johnson, Kahneman in `sources/PROVENANCE.json`. Use those before claiming new frameworks.
- “Hidden agenda” requires evidence of a mismatch between illocution and likely perlocution, not a personality smear.
- No live search, no moderator-tool grants. Draft / data-only.
- Chat HTTP 200 is not an eval PASS (ISSUE-0002). Classification *accuracy %* is unmeasured while casops-eval instruments are unqualified.

## Sources

### Classics

- Austin, *How to Do Things with Words*
- Searle, *Speech Acts* (assertive / directive / commissive / expressive / declaration)
- Grice, implicature and conversational maxims
- ISO 24617-2:2020 Dialogue acts (Halliday Centre / ISO SemAF Part 2); DialogBank (Bunt et al.)

### arXiv (verified 2026-09)

- arXiv:2509.10010 — Ahmad, Kowol, Hillmann, Möller. *Multi-Intent Recognition in Dialogue Understanding* (MultiWOZ 2.1; Mistral-7B few-shot vs BERT). https://arxiv.org/abs/2509.10010
- arXiv:2507.22289 — Castillo-López, de Chalendar, Semmar. *Intent Recognition and Out-of-Scope Detection using LLMs in Multi-party Conversations* (SIGDIAL 2025). https://arxiv.org/abs/2507.22289
- arXiv:2506.01881 — Qian et al. *WHEN TO ACT, WHEN TO WAIT* (STORM; intent-action alignment). https://arxiv.org/abs/2506.01881
- arXiv:2411.14252 — Liu, Tan, Fu, Lim. *From Intents to Conversations* (Chain-of-Intent / MINT-CL; CIKM 2025). https://arxiv.org/abs/2411.14252
- arXiv:2503.21544 — Yin, Hwang, Carenini. *SWI: Speaking with Intent in Large Language Models*. https://arxiv.org/abs/2503.21544
- arXiv:2603.28929 — Nandy. *Known Intents, New Combinations* (clause-factorized multi-intent). https://arxiv.org/abs/2603.28929
- arXiv:2609.05975 — Voroshilov. *Intent Drift at SME Scale* (governance; **skip live enablement**). https://arxiv.org/abs/2609.05975

### xAI (vendor docs; non-activating)

- Tools overview — https://docs.x.ai/developers/tools/overview (built-in tools vs function calling)
- Grok 4 capabilities include function calling and structured outputs — https://docs.x.ai/developers/models/grok-4 (rate limits are **xAI API**, not this CASOPS control plane)

### YouTube (educational; do not paste transcripts)

- Searle & Magee (1977), *The Philosophy of Language* — https://www.youtube.com/watch?v=FItTy4yizlw (illocution vs perlocution)
- Arxiv Papers explainer of SWI (arXiv:2503.21544) — https://www.youtube.com/watch?v=kX0Nks4P6fw
