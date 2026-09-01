# Aesthetics Agent L2 rubric (offline Host foundation)

Pass when offline evaluate produces:

| Check | Gate |
|-------|------|
| AestheticVector complete | All D1–D10 present in [0,1] |
| Confidence present | Per-dimension confidence |
| No naked scalar | `aesthetic_quality` accompanied by vector + hack |
| Profile resolved | Explicit profile_id or neutral_baseline flag |
| Anti-hack field | `hack_likelihood` in [0,1] |
| Critique usable | ≥1 actionable_critique line on score/align/refine |

Fail / escalate:

- `hack_likelihood` ≥ 0.55
- any confidence < 0.65 (uncertainty_flag)
- `aesthetic_quality` < 0.25

Live SigLIP/VLM correlation targets (ρ ≥ 0.75) are **not** enforced in offline stub mode.
