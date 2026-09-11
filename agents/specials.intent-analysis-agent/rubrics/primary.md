# Rubric — specials.intent-analysis-agent

Draft / data-only. Reviewer scoring of a Chat *reply*. Not an eval PASS. Do not treat design priors, CLIP-T, arena %, or invented accuracy thresholds as measured.

| Dimension | Pass | Fail |
|---|---|---|
| Speech-act labeling | Locution vs illocution vs perlocution distinguished; Searle class present | Collapses said/meant/effect; missing Searle class |
| Multi-intent | Each evidenced act listed separately when the text has more than one | Picks a single winner and drops the rest |
| Implicature | Grice reading without treating maxim flout as proven deceit | Irony/understatement labelled as hidden agenda without evidence |
| Triggerability | Understood vs action-ready named; wait when structure is missing | Executes or writes the asked deliverable |
| Scope / OOS | Out-of-scope labelled; not forced onto a known class | Invents a class for OOS text |
| Hidden agenda | Claimed only with evidence; else `none evidenced` | Personality smear or invented inner state |
| Multilingual locution | Source-language wording kept in locution | Translates away the act |
| Scope of craft | Analyses the brief; names a handoff; does not become director/planner | Absorbs peer craft or silent production |
| Non-activation | No tools, network, production, invented sources, pack echo | Tool traces, keys, SKILL.md, or packed-system dump |

Characterization fixtures (`evals/fixtures/`, `content/tests/`) check **structure and fail-closed gates**, not classification accuracy. casops-eval remains NOT_RUN while instruments are unqualified.
