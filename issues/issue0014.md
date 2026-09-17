# ISSUE-0014 — Bounded RSI for hop policy (deferred)

**Status:** Deferred. Do **not** implement. Do **not** start P0–P7 until the **reinvoke gate** below is true.  
**Severity:** Medium (search/cost; not a filmmaking blocker)  
**Component:** Program Chat / Project Chat collab, Trace, Agent Profile Improvement, Validation, skills/playbooks  
**Observed:** 2026-09-16  
**Operator statement:** Study `spec/recursive-self-improvement.md` for what could improve this app. Dream-RSI-shaped search policy is the fit. Specialists are **not** in a training loop — “freeze specialists” means freeze **roles/packs**, not weights. Mark as next issue. **Reinvoke only when all agents’ models are completed.** Do this work later.  
**Related:** `spec/recursive-self-improvement.md` (Dream-RSI / SimpleTES / ACE), `common_agent_structure` §13 (L0–L5 improvement), ISSUE-0002 (Chat 200 ≠ agent-correct), ISSUE-0007 (clip Auto Pilot), ISSUE-0008 (Project Chat spine), ISSUE-0013 (Program filmmaking).  
**Honesty:** CHARACTERIZATION. Not an eval PASS. Not a production license. `sample/` stays read-only. Dry-run stays default. Fail-closed engines stay fail-closed. Skills and citations stay declared, not live grants. `improvement.mode` stays `disabled` until this issue is actually opened. Agents cannot approve or promote.

This issue records the RSI study so a later session can pick it up. It does **not** change host, UI, packs, or `improvement/` in this pass.

---

## Reinvoke gate (hard)

**Do not work this issue until all agents’ models are completed.**

Until that is true:

- Do not implement P0–P7.
- Do not enable `improvement.mode`.
- Do not add a dream/replay job.
- Do not mutate specialist `prompts/primary.md`, bindings, or first-called as an RSI experiment.
- Continue ISSUE-0013 filmmaking and pack/model completion instead.

When the gate is true, re-read this file + `spec/recursive-self-improvement.md` and implement in P0→P7 order. Do not skip to P5 (dream) or DGM harness rewrite.

---

## 0. Why this is later (and why “freeze” is not about training)

Specialists in this repo are **not being trained**. There is no LoRA, no serving gradient, no weight RSI. `TrainerBridge` is export-only. That is already true.

“Freeze specialists” in Dream-RSI language means: **do not make the specialist pack the RSI artifact.** The loop is always `act → score → persist an artifact → act again with that artifact`. The artifact that may recurse later is the **orchestrator hop policy** (who next, width, stop), not `video.screenwriter` / `video.showrunner` / `video.promptengineer` files.

Packs can change **without training** (edit `primary.md`, first-called, skills). That is DGM/SICA (harness RSI). CASS already fixed the crew:

- Program first agent hop: `specials.intent-analysis-agent`
- Program first-called: `video.showrunner`
- Screenwriter owns pages (W1), not spawn
- Child first-called: `video.promptengineer`
- Five human locks stay on the child
- Improvement policy `mode: disabled`; agents cannot approve

RSI must not search over “what is a screenwriter.” It may later search over **how many OPTIONS / critic hops / Imagine tries** for a film, after models are complete.

---

## 1. What is better (decision, frozen)

| Approach | Verdict | Why |
|---|---|---|
| Dream-RSI + SimpleTES \(C \times L \times K\) | **Do later** | Freeze packs. Change hop policy. Score on old trees. Matches OPTIONS + critic + generate. Scarce resource = agent calls + Imagine calls. |
| ACE / Voyager skill bullets | **Second, later** | After a miss, one playbook/skill bullet. Not a pack rewrite. |
| DGM / SICA harness rewrite | **Not first** | Fights ownership contracts. |
| GEPA / prompt evolution | **After trees** | Blind prompt search Goodharts Chat. |
| Weight / LoRA RSI | **Skip** | Wrong layer. Models are not a training loop here. |

CASS §13 (propose → sandbox → human → ledger → rollback) stays the **governance**. Dream-RSI stays the **search** slice. Neither is complete alone. Do not claim strong RSI.

---

## 2. Work to do later (only after the reinvoke gate)

### P0 — Discovery trees (required substrate)

Persist every Program and Project collab pass as a tree, not only hop bubbles:

```
node: id, parent_id
action: branch | refine | stop | parallel_batch
artifact_ref
score: float | null
cost: tokens, seconds, agent_calls, imagine_calls
children, status: pending | ok | fail | pruned
```

JSONL + small index. Trace UI can show the tree. Overflow stays the production board (one function one UI). Without trees, nothing else is RSI.

### P1 — Default policy \(C \times L \times K\) + budgets

Make the informal Chat shape explicit:

- **C** = OPTIONS width
- **L** = critic / lock refine
- **K** = compile/engine tries before commit

Hard stop: `{max_calls, max_imagine, max_seconds, max_parallel}`. Optional W0–W2 specialists (ideation, worldbuilding, …) may be bandit/PUCT-picked. **Do not** move first-hop or first-called.

Pareto: \(V = \max s - \beta_1 N_{\text{calls}} + \beta_2 (N_{\text{calls}}/\text{rounds})\). Imagine cost counts in \(N\).

### P2 — Improvement evaluate is real

`POST .../improvement/candidates/{cid}/evaluate` must run frozen Validation fixtures + `video.judge` + fail-closed — not a state flip to `EVALUATED`. Builder ≠ reviewer. Failed attempts become regression fixtures. Incumbent stays a candidate. Human approve stays. `improvement.mode` stays disabled until this P2 is true.

### P3 — Skill / playbook bullets

After fail-closed, empty-scene lock, or critic warning: one ACE bullet into playbook/`skills/`. Verifier must reproduce. Do not dump the hop log into the next system prompt.

### P4 — GEPA on skill text (optional)

Evolve `SKILL.md` / dispatcher copy **after** P0–P2. Not `primary.md` of owned specialists.

### P5 — Nightly dream / replay

LLM writes \(M\) hop-policy modules. Replay on historical trees with **zero** live Grok/Imagine. Promote only if \(V(\pi') \ge V(\pi)\) **and** live canary **and** human approve. Policy `solve()` must not peek at child scores. Keep ~10–20% live exploration (replay cannot invent unseen branches).

### P6 — Archive (MAP-Elites / DGM-style)

Keep policy/graph champions by behavior (high-width vs cheap-stop, debate vs pipeline), not only latest. Workflow graphs as versioned code, not only React Flow layout.

### P7 — Explicitly out of scope

- Weight / LoRA / serving gradient
- Rewriting corrigibility, safety, gates, held-out sets, or the judge
- Agents approving candidates
- Production activation, T3, plugin execute
- `POST /swarms/{id}/runtime/run`
- Claiming Chat 200 = agent-correct
- Writing `sample/`

---

## 3. Current facts (so a later session does not re-discover)

- Improvement API evaluate/approve/ledger is in-memory; evaluate does not score.
- Traces are OTel-style spans, not discovery trees (no score/cost/branch).
- Program/Project hops are CHARACTERIZATION lists (`program_comms.py` / project walkthroughs).
- Skills are declared, not live grants.
- `improvement/policy.json` `mode` is `disabled` on packs (e.g. `video.showrunner`).
- L5 research isolation exists and must stay research-only.

---

## 4. Exit (when eventually implemented)

- Reinvoke gate was true (all agents’ models completed) before any P0 code landed.
- Program + Project runs persist as scored trees.
- Hop policy is \(C \times L \times K\) with budgets; first-hop / first-called unchanged.
- Improvement evaluate uses Validation + critic; human approve; no agent self-approval.
- Dream/replay (if shipped) uses historical trees only; no live Imagine in replay.
- CHARACTERIZATION until a frozen evaluator exists. Not an eval PASS.

**This file is the next issue. Implementation is later. Do not start it now.**
