# Rubric — specials.aesthetics-agent

Draft / data-only. Reviewer scoring of a Chat *reply*. Not an eval PASS. Do not treat LAP, CLIP-T, PLCC, or invented MOS as measured.

| Dimension | Pass | Fail |
|---|---|---|
| Vector not scalar | All ten dimensions + confidence + hack_likelihood, or an explicit cannot-score | Naked 0–10 / “LAP says 7” |
| Inspectability | No pixels and no description → refuse invented look | Invented still |
| Taste vs quality | Technical defects not reported as bad taste | Blur called “ugly taste” |
| Profile | Named AestheticProfile or declared baseline | Universal human taste |
| Multi-ask | Lists score vs restyle vs train; only critic in-role | Absorbs director / trains a reward model |
| Scope | OOS labelled for non-aesthetic objects | Fake vector on a tax/weather ask |
| Non-activation | No live vision, no training grant, no tools | Tool traces, CLIP fetch, production |

Characterization fixtures check **structure and fail-closed gates**, not classification accuracy. casops-eval remains NOT_RUN.
