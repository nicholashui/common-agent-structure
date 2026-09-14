# ISSUE-0008 — Gap analysis: asain-beauty Chat agent-call flow vs the rest of the app

**Status:** Implemented (P0–P5 in app; P3 is a host-owned gated cycle, folders stay `max_refinement_count: 0`; P4 is a read-only roster + `?swarm=` filter, not `runtime/run`. Not an eval PASS; not a production license)  
**Severity:** High (operator-verified Chat flow is the expected collab spine; most other surfaces still implement a different product)  
**Component:** Project Chat (`/projects/asain-beauty/chat`), Project Workflow, Agent Profile Chat/Run, Agent Org Chat, Main/Sub Workflow SVGs, `casops.project_comms` / `project_sample_walkthrough`, Common Agent Structure v3 folders, Common Swarm Structure v4 spec  
**Observed:** 2026-09-14  
**Operator statement:** Chat at `http://localhost:15173/projects/asain-beauty/chat` is the expected agents-call flow from start to end. Review whether the complete app matches that flow.  
**Related:** ISSUE-0002 (Agent Profile Chat 200 ≠ agent-correct / DAG not executed). ISSUE-0005/0006 (ACP transport). ISSUE-0007 (Auto Pilot Chat characterization).  
**Honesty:** The asain-beauty transcript is `CHARACTERIZATION` (`live: false` on hops 1–43). Hop 44 (`generated_media`) is the live Grok Imagine clip the operator already verified. `sample/` is not a source. Do not claim an eval PASS.

This issue is a **gap analysis**. It does not implement the suggestions. It does not authorize production activation, T3, network grants, plugin execution, L5 promotion, or an LLM as live swarm orchestrator.

---

## 1. Expected flow (operator-verified Chat)

Source of truth for this issue: `project/asain-beauty/comms.json` (44 items, `walkthrough: auto-pilot-v1`, `autopilot.status: aligned`, five human locks).

Human draft is one line. Domain novels are option crafts, not human essays. Host assembles the generator instruction. Grok Imagine is a **host** vendor call after that file exists.

```text
Human → Create Project                         instruction   (draft)
Create Project → specials.intent-analysis-agent instruction
intent-analysis-agent → Create Project         return
creative-agent → intent-analysis-agent         choice
intent-analysis-agent → creative-agent         induce
creative-agent → video.promptengineer          return
video.promptengineer → creative-agent          choice
Create Project → video.promptengineer          instruction   (first-called)
video.promptengineer → Create Project          return        (who-leads OPTIONS)
creative-agent → video.promptengineer          choice        (induce creativedirector)
video.promptengineer → Human                   human_ask     (Frame / sound lock)
Human → video.promptengineer                   choice

then for each domain expert (induce → return → optional ASK_HUMAN → human choice → parent choice):
  PE → video.creativedirector → PE
  PE → video.director → Human lock → creativedirector choice
  PE → video.cinematographer → Human lock → director choice
  PE → video.mua_makeup → Human lock → creativedirector choice
  PE → video.cameraoperator → cinematographer choice          (no human hop)
  PE → video.continuity → Human lock → PE confirm
  PE → video.critic → PE choice                               (no human hop)

video.promptengineer → video.promptengineer    next_instruction  pass_02
video.promptengineer → Output                  output            (host-assembled file)
video.promptengineer → Human                   generated_media   live=true (Grok Imagine I2V)
```

Valid **Human →** roles (ISSUE-0007): `video.promptengineer`, `video.director`, `video.cinematographer`, `video.mua_makeup`, `video.continuity`. Cameraoperator and critic stay agent-to-agent.

Owned headings (host join, not PE solo novel):

| Heading | Owner |
|---|---|
| Creative direction | `video.creativedirector` |
| Frame, Sound | `video.promptengineer` |
| Subject, Hair, Skin | `video.continuity` |
| Makeup | `video.mua_makeup` |
| Light | `video.cinematographer` |
| Coverage / performance | `video.director` |
| Camera lock | `video.cameraoperator` |
| Negatives | `video.critic` |

Chat hop headers use `displayPartyName` (`intent-analysis-agent`, `creative-agent`, `Human → video.*`). Workflow node options are supposed to copy the same `DECISIONS` fields.

---

## 2. Match matrix (Chat flow vs each surface)

| Surface | Route / artifact | Matches Chat collab spine? | Notes |
|---|---|---|---|
| Project Chat | `/projects/:id/chat` | **Yes (reference)** | 42 collab hops + assembled instruction + live clip. Auto Pilot 5/5. |
| Project Workflow | `/projects/:id/workflow` | **Partial** | Same `DECISIONS` / intent+creative nodes / ASK_HUMAN edges. Clicking a node does **not** open the matching Chat hop. `Next` consults `video.planner` Chat, a path the transcript never uses. Comms side panel lists hops but is not the Chat time-sequence layout. |
| Project record | `project/asain-beauty/project.json` | **No (template)** | `sub_workflow_id: video.template.b` labeled **UGC Ad**. Chat thesis is phone-macro **anti-idol / no SKU**. Heuristic template contradicts Auto Pilot creative lock. |
| Grok Imagine tag | Chat output panel | **Yes (live hop 44)** | Operator verified. Dry-run must be off. Other generator tags fail-closed. |
| New project | `/projects/new` | **No** | Creates a graph stub. Does not start intent → creative → PE → five locks. Auto Pilot is asain-beauty walkthrough-only. |
| Agent Profile Chat | `/agents/:id/chat` | **No** | Packed `Runtime.chat` to one folder (ISSUE-0002). Not induce/return/ASK_HUMAN. Org Chat and Main/Sub SVG clicks land **here**, not on Project Chat. |
| Agent Run | `/agents/:id/run` | **No** | Per-agent DAG/model nodes share packed complete with Chat. Not the project collab pass. |
| Agent Swarm home | `/` | **No** | Fleet list of folders. Not a swarm walk of the Chat spine. |
| Agent Org Chat | `/org-chat` | **No** | Org-chart picture (`buildOrgChart`). Read-only except local drag. Click → Agent Profile. No collab hops. |
| Main / Sub Workflow SVG | `/workflow`, `/workflow/sub` | **No** | 114-agent ComfyUI production map (or template A–J / scale S1–S7). Click → `/agents/{id}/chat`. Not the asain-beauty Auto Pilot DAG. |
| Control UI spec | `spec/ui.v1.md` | **Stale** | Still says UI `DRAFT — not implemented`. Does not describe Project Chat Auto Pilot. |
| Backend live Launch | `POST /api/v3/projects/{id}/run` | **Partial** | Can call agents via `chat_fn` and host-join sections. Default asain-beauty **file** is the walkthrough (`live: false`). Launch **replaces** characterization items. Specials preamble only if `agent_spec.json` exists. `INDUCE_ROSTER` omits `video.creativedirector` as a roster row (still required_ids). Fan-in tells PE not to write the novel; host `assemble_generator_instruction` writes the file. |
| Backend generate | `POST .../generate` | **Match for Imagine** | Reads assembled `output/`. Does not re-call the swarm. PE `does_not_own` includes “Live vendor generation” — host owns the vendor call, Chat still attributes the hop `from: video.promptengineer`. |
| Common Agent Structure | `agents/<id>/` v3 folders | **Declared, not executed by Chat** | Folders exist (including both specials). Project Chat does not run compose DAG, critique_edges, observability decision records, or eval. `max_peer_hops: 0` and `max_refinement_count: 0` on PE and specials **contradict** induce/choice hops. Intent `critique_edges` are `spagent.intent-analysis-agent-input/output`, not `create-project` / creative-agent. PE outputs list `video.judge` and a second `video.aiqaconsistency`; Chat never induces them. `model_policy.provider: local_deterministic`; live Chat/Launch uses host xAI when `chat_fn` is Runtime.chat. |
| Common Swarm Structure | `common_swarm_structure.md` / spec v4 | **Specified only** | No `swarms/` tree. No `/api/v3/swarms`. No `/swarms/:id` UI. v4 **forbids** a swarm-wide Chat that bypasses per-agent `runtime/chat`, and **forbids** “auto-orchestrate with LLM”. Project Chat is a **host-mediated collab pass**, not a v4 swarm walk. Citation `CIT-GATE-001` remains BLOCKED; deployment recommendation NO-GO. |

---

## 3. Gaps (what does not match)

### 3.1 UI

**G-UI-1 — Three “chat” products, one operator expectation.**  
Project Chat = collab hops. Agent Profile Chat = single-folder LLM. Org Chat = org picture. The names all say Chat. Clicking an agent on Org Chat or on Main/Sub SVG opens Profile Chat and **leaves** the verified flow.

**G-UI-2 — Project Workflow is a cousin, not the same story.**  
Graph nodes copy `DECISIONS` and show intent/creative. Missing vs Chat: hop time-sequence, ASK option crafts vs expert who-leads on PE (two namespaces), `next_instruction` / assembled output / generated clip as first-class canvas objects. `Next` → `video.planner` is an extra agent the Chat spine does not call. Node click does not `?comm=` into Project Chat.

**G-UI-3 — Main/Sub Workflow SVG is a different DAG.**  
114 unique video agents, seven production phases. Auto Pilot uses ~12 parties. Clicking `video.promptengineer` on the SVG opens `/agents/video.promptengineer/chat`, which cannot replay induce/ASK/locks.

**G-UI-4 — Template chip fights the Chat thesis.**  
`project.json` `sub_workflow_id` = template B UGC Ad. Chat creative lock = phone-macro skin study, no product. Operator can believe Workflow “B” is the same job as Chat.

**G-UI-5 — Auto Pilot is not a productized new-project path.**  
Only asain-beauty has the walkthrough. `/projects/new` does not run intent-analysis or seed five ASK_HUMAN locks.

**G-UI-6 — Iterative loop from ISSUE-0007 is one cycle.**  
Chat is pass_01 collab + pass_02 assemble. There is no second intent→creative→domain→human cycle after the clip, and no UI to “continue Auto Pilot” from generated_media.

**G-UI-7 — `spec/ui.v1.md` does not mention Project Chat / Auto Pilot.**  
Docs drift. Help/user_guide likely still describe Agent Profile Chat as the chat.

### 3.2 Backend

**G-BE-1 — Characterization file vs live Launch are different programs.**  
On-disk Chat the operator verified is `write_asain_beauty_walkthrough` (stamped hops, `live: false`). `run_asain_beauty_workflow` is a second sequencer: specials if present, PE pass_01, induce from PE `induce_call` lines + roster, host extract_sections, fan-in, assemble. Launch **overwrites** `comms.json` items (save_comms with items-only at the end of a live run historically dropped `autopilot`/`locks` until ISSUE-0008-adjacent save keys; live run still does not emit the walkthrough’s exact 43-hop script).

**G-BE-2 — Live induce roster ≠ Chat induce set.**  
Chat always induces creativedirector, director, cinematographer, mua, cameraoperator, continuity, critic. Live `INDUCE_ROSTER` is director…critic; creativedirector is required on disk but dispatched only if PE emits `induce_call`. Specials are a preamble, not the same choice/induce/return triangle as the walkthrough.

**G-BE-3 — Host join, not PE novel — but Chat labels PE as Output author.**  
Correct per protocol (`Do not write the final generator novel yourself`). Easy to misread as “PE generated the prompt.” Backend does not emit a `kind: assembled` hop into the Chat conversation list the operator sees (lineage hop exists on live Launch; walkthrough skips it and puts prose on `kind: output`).

**G-BE-4 — No swarm execution plane.**  
`grep` of `src/casops/api` finds **zero** `/api/v3/swarms` routes. Project collab is not `Runtime.execute` of member DAGs and not a v4 outer walk.

**G-BE-5 — Generate does not close the agent loop.**  
Imagine consumes the text file. It does not notify critic/continuity, does not start pass_03, does not write per-agent decision records.

**G-BE-6 — `max_peer_hops: 0` vs induce.**  
Folder budget says zero peer hops. Host still stamps PE→domain induce. Either the folder contract or the collab host is lying.

### 3.3 Common Agent Structure (v3 folders)

**G-CAS-1 — Project Chat does not execute the folder contract.**  
Same finding class as ISSUE-0002, now at **project** scale: hops are host-stamped (walkthrough) or `Runtime.chat` dumps (live Launch). Compose DAG, skills as live grants, memory writes, plugins, T3, observability `decision_record`, eval harness: **not** this flow. Fixtures on specials/video folders are CHARACTERIZATION, `validation/report` stays `NOT_RUN` / `unqualified_instruments`.

**G-CAS-2 — `critique_edges` ≠ Chat edges.**  
PE folder outputs include `video.judge` (never in Chat) and duplicate `video.aiqaconsistency`. Inputs are critic+director only; Chat also receives creative-agent, continuity confirm, fan-in members. Intent-analysis edges are `spagent.*` placeholders, not `create-project` / `specials.general-creative-agent`.

**G-CAS-3 — Specials status `draft`; video PE `registered`.**  
Chat treats both as first-class Auto Pilot parties. Folder `status` and `model_policy.local_deterministic` do not match host xAI Chat.

**G-CAS-4 — `max_refinement_count: 0` vs ISSUE-0007 iterative loop.**  
Folders forbid refinement. Auto Pilot asks for multiple intent→creative→domain→human cycles. Implementation did one characterization pass.

**G-CAS-5 — Citations / skills declared, not live.**  
Unchanged host rule. Chat option `why` text is not a tool grant.

### 3.4 Common Swarm Structure (v4)

**G-CSS-1 — No swarm identity for asain-beauty.**  
v4: one `swarm_id` folder, roster, topology class, visibility windows, bulletin, authority envelopes, commit governor. asain-beauty is `casops.project.v1` + comms log. There is no `swarms/asain-beauty/`.

**G-CSS-2 — Visualization maps are not the Chat spine.**  
v4 §24 maps Fleet / Org / Workflow to a named swarm. Implemented UI maps them to the **whole loaded pack** (114 video + specials). Chat spine is a **subset** with a different topology (linear host dispatch, not the 114-agent SVG).

**G-CSS-3 — Specified swarm Chat is forbidden; Project Chat exists anyway.**  
v4: “Forbidden: swarm Chat; … a swarm-wide Chat bypassing per-agent `runtime/chat`.” Project Chat is exactly a multi-party transcript. It is honest as **host collab**, dishonest if labeled a v4 swarm runner.

**G-CSS-4 — Coordination/commit/consistency/scheduling planes absent.**  
No bulletin, no isolation windows, no conformal commit, no shared-memory fence, no sub-deadlines. Conflicts in live Launch are **listed** in fan-in text (`collect_conflicts`); they are not a v4 commit decision.

**G-CSS-5 — `/swarms/:id/*` UI routes do not exist.**  
`App.tsx` has `/`, `/org-chat`, `/workflow`, `/projects/:id/*`, `/agents/:id/*`. No swarm profile / bulletin / authority / propagation / schedule.

---

## 4. What already matches (do not “fix” these into something else)

- Human draft only; five Human → domain option locks; cameraoperator/critic not human hops.
- Intent-analysis-agent and creative-agent appear in Chat and on Project Workflow.
- Host-assembled generator instruction; Grok Imagine I2V after Dry-run off; clip below the instruction box.
- Org Chat has no Auto layout (operator request).
- Main/Sub SVG ComfyUI restyle and theme toggle.
- ISSUE-0002 proof panel on **Agent Profile** Chat (adapter/pack) — keep it there; do not pretend Profile Chat is Project Chat.

---

## 5. Change suggestions

Priority is **make every UI that looks like “the swarm” either show this Chat spine or clearly refuse to**. Do not start by implementing v4 `/api/v3/swarms/{id}/runtime/run`.

### P0 — Stop sending the operator to the wrong Chat

1. **Project Workflow node click** → `/projects/asain-beauty/chat?comm=<hop>` (and `?opt=` for that hop only). Do not navigate to `/agents/:id/chat` from a project canvas.
2. **Org Chat / Main / Sub SVG** agent click: if a project is in context, offer **Project Chat hop** vs **Agent Profile** (Profile remains ISSUE-0002 packed Chat). Default for asain-beauty operators: Project Chat.
3. Rename labels where cheap: Agent Profile tab stays “Chat”; Project page stays “Chat” but the hop header already says Human → agent. Add a one-line badge on Profile Chat: “Single-agent packed Chat. Not the project Auto Pilot transcript.”
4. Fix `project.json` `sub_workflow_id` / suggestion primary so it does not say UGC Ad while Chat is a no-SKU skin study — or show the template as “pack map only, not this project’s creative lock.”

**Frontend: keep Project Chat / Imagine / Org-as-picture; change click-through and honesty labels.** Do not merge the three Chat products into one screen. Do not restyle Main/Sub SVG into the Auto Pilot DAG. Do not put Auto layout back on Org Chat.

| Change? | Surface | Action |
|---|---|---|
| No | Project Chat hop list, five Human → domain OptionTags, Auto Pilot banner, `shownOptionId` | Keep. Operator-verified spine |
| No | Grok Imagine / Grok Image tags, Dry-run, clip `<video>` below instruction | Keep. Other generator tags stay fail-closed |
| No | Org Chat as org-chart picture; no Auto layout | Keep read-only except local drag |
| No | Main/Sub SVG ComfyUI restyle + theme toggle | Keep as **pack map**, not this job’s DAG |
| No | Agent Profile Chat packed LLM + ISSUE-0002 proof panel | Keep. Do not make it Project Chat |
| No | `/swarms/:id/*` screens | Do not add to “match Chat” |
| No | Pixel-perfect redesign / new Auto Pilot v2 chrome | Out of scope |
| Yes | Project Workflow node click | Item 1: `/projects/:id/chat?comm=` (+ `opt` only if that hop). Not `/agents/:id/chat` |
| Yes | Org Chat / Main / Sub SVG agent click | Item 2: if a project is in context, default Project Chat hop; Profile is explicit second choice |
| Yes | Profile Chat badge | Item 3: “Single-agent packed Chat. Not the project Auto Pilot transcript.” |
| Yes | Template B UGC Ad vs Chat thesis | Item 4: `project.json` / Workflow chip honesty |
| Yes | Project Workflow `Next` → `video.planner` | Stop calling an agent the Chat spine never uses, or hide Next on Auto Pilot projects |
| Yes | New project | G-UI-5: optional later seed of intent→creative→five locks; not required to “match” asain-beauty Chat |
| Yes | Honesty on Chat banner | P5 item 19: hops 1–43 CHARACTERIZATION; generate `live` |
| Conditional | Continue Auto Pilot after clip | P3 / G-UI-6. UI option only if backend pass_03 ships |

### P1 — One sequencer, two honest modes

5. **Single hop table** shared by walkthrough and live Launch: same `from`/`to`/`kind` order as §1. Walkthrough fills `live: false`. Launch stamps the same rows with `live: true` when `chat_fn` returns. Stop having Launch overwrite the spine with a different shape.
6. Put `video.creativedirector` on `INDUCE_ROSTER` (or always dispatch after PE who-leads), matching Chat.
7. Keep host assembly. Add a visible Chat hop `kind: assembled` (host_service → output) so PE is not mistaken as novelist. Keep `from: video.promptengineer` on `kind: output` only if the protocol still requires first-called attribution — then say “host-joined” in `hopExtra` (already partly true).
8. Preserve `autopilot` + `locks` on every `save_comms` path, including live Launch (items-only save currently wipes them).

**Backend: keep host assembly + Imagine; change Launch hop shape to match Chat.** Do not add `/api/v3/swarms`. Do not execute member compose DAGs from Project Chat. Do not send `GOLD_BODY_PROBE` or write `sample/`.

| Change? | Surface | Action |
|---|---|---|
| No | `assembled_output` / `assemble_generator_instruction` host join | Keep. PE does not write the novel |
| No | `POST /api/v3/projects/{id}/generate` Grok Imagine I2V (still then video) | Keep. Fail-closed for Kling/Veo/Sora/… |
| No | Dry-run short-circuit; `XAI_API_KEY` required for live | Keep |
| No | `Runtime.chat` packed folder for Agent Profile | Keep (ISSUE-0002). Not the project sequencer |
| No | `POST /api/v3/swarms` / outer `runtime/run` | Do not implement to match Chat |
| No | Per-agent `Runtime.execute` DAG from Project Chat | Do not. Host-mediated collab |
| Yes | `run_asain_beauty_workflow` hop table | Item 5: same `from`/`to`/`kind` order as §1. Walkthrough `live: false`; Launch stamps `live` when `chat_fn` returns. Stop overwriting the spine with a different shape |
| Yes | `INDUCE_ROSTER` | Item 6: always include `video.creativedirector` |
| Yes | Specials preamble | Same induce/return/choice triangle as walkthrough, not a bolt-on |
| Yes | `kind: assembled` hop | Item 7: host_service → output so PE is not read as novelist |
| Yes | `save_comms` / live Launch save | Item 8: always persist `autopilot` + `locks` (and decisions). Items-only save wipes them |
| Yes | Human lock pick vs expert who-leads | Already: disjoint ASK namespace must not clobber PE who-leads; keep that |
| Conditional | Generate → critic/continuity → pass_03 | G-BE-5 / P3. Only with a human stop option |
| Doc | `spec/ui.v1.md` still “UI not implemented” | P5. Not a runtime change |

9. Update `critique_edges` on the Auto Pilot parties to the Chat edges (intent↔creative↔PE↔domain). Do **not** invent `va_category`. Leave `video.judge` off this project’s spine or add an explicit “not in asain-beauty pass_01” note on the node — do not silently induce 114 agents.
10. Set `max_peer_hops` on PE to the real host-dispatch bound (count of induce roster), or document that peer hops are **host-mediated** and folder `max_peer_hops` applies only to agent-initiated tools (today `allowed_tools: []`). Pick one and test it.
11. Specials `critique_edges`: replace `spagent.*` placeholders with `create-project` / `specials.general-creative-agent` / `video.promptengineer` as in Chat.
12. Do not claim eval PASS. Add characterization fixtures that **replay the §1 hop list** (from/to/kind only), not gold-body probes.

**CAS model: do not change the v3 schema.** Keep `casops.common_agent.v3` / `schema_version: 3.0`. Do not add Auto Pilot fields, a new plane, or a v4 agent type. Chat hops belong on `casops.project.v1` / comms. Edit **instance** `agent_spec.json` on the Auto Pilot parties only (or a **project overlay** so Main/Sub pack edges stay valid).

| Change? | Field | Action |
|---|---|---|
| No | `structure_id` / schema `3.0` | Keep |
| No | `model_policy.provider: local_deterministic` | Keep. Host Chat/Launch already uses the host LLM adapter; do not flip folders to xAI |
| No | `production_activation_requested: false` | Keep fail-closed |
| No | `allowed_tools` / `allowed_plugins` empty | Skills stay declared, not live grants |
| No | `max_output_tokens: 1024` | Why the host joins the generator file |
| No | PE `does_not_own` “Live vendor generation” | Imagine stays a host call |
| No | `va_category` | Do not invent or rewrite |
| No | Other ~100 video agents | Pack map for Main/Sub SVG, not this spine |
| Yes | `critique_edges` on Auto Pilot set | Match Chat (items 9, 11). Prefer project overlay over deleting pack edges (director still lists screenwriter/editor; CD lists brand; continuity lists costumedesign/gatekeeper) |
| Yes | PE (and specials) `max_peer_hops: 0` | Item 10 — pick host-mediated vs raise to induce-roster size; test it |
| Conditional | Specials `status: draft` | G-CAS-3. Bump to `registered` only if Launch actually runs those folders; else keep `draft` and keep Chat hops CHARACTERIZATION |
| Conditional | `max_refinement_count: 0` | Leave 0 unless P3 pass_03 ships; then raise **host** policy or keep folders at 0 and own the loop on the host |

**Agent folder contents (prompts / skills / identity): overlay, do not rewrite the pack.** Domain knowledge, fail-closed, packed JSON Output schema, and Agent Profile “How to reply” 1–6 stay. Auto Pilot live Launch (`_induce_envelope` / `_first_called_pass1`) asks for **THINKING + OPTION n + RECOMMEND + DECIDE_BY + ASK_HUMAN**. Packed `prompts/primary.md` mostly does **not**. Walkthrough Chat does not read these files (`live: false`). Live Launch + Profile Chat **do** pack `primary.md`. Do not paste `sample/`. Do not grow `video.director` `primary.md` past the 768 packed-task clip. Skills stay declared, not live grants.

| Change? | File | Action |
|---|---|---|
| No | `identity/`, `sources/study/`, L1 JSON output schema, fail-closed, empty tools | Keep. Profile Chat (ISSUE-0002) still uses the packed envelope |
| No | Other ~100 video `prompts/primary.md` | Pack map, not this spine |
| No | `skills/SKILL.md` as a live procedure | Declared only. Do not treat as a grant |
| No | `evals/fixtures/*` as gold | Stay CHARACTERIZATION; not an eval PASS |
| Yes | Auto Pilot set `prompts/primary.md` **Host collab** bullet | Add: emit `THINKING` / `OPTION n: label — why` / `RECOMMEND` / `DECIDE_BY` / optional `ASK_HUMAN`. Human picks options; do not demand a domain essay. Do not copy `sample/` |
| Yes | `specials.intent-analysis-agent/prompts/primary.md` | Locution/illocution stay. **Also** emit thesis-class OPTIONS + RECOMMEND + DECIDE_BY (Launch/walkthrough). Next-agent handoff = `specials.general-creative-agent`, not a generic planner |
| Yes | `specials.general-creative-agent/prompts/primary.md` | Boden/recombination stay. **Also** emit 3 campaign OPTIONS; `DECIDE_BY: video.promptengineer`; do not write the generator novel |
| Yes | `video.promptengineer/prompts/primary.md` | Soften “stay the only operator reply”: first-called among **agents**; five Human → domain ASK locks are in-role. Host collab already has induce_call/ASK_HUMAN — add OPTION block. “Steers Sora/Veo/Runway/Kling” is design-time; runtime vendor call is **host** Grok Imagine. Prompt “refine at most 3 times” vs folder `max_refinement_count: 0` — align to 0 until P3 |
| Yes | Domain collab bullets (director, cinematographer, mua, continuity, cameraoperator, critic, creativedirector) | Already own headings. Add OPTION/DECIDE_BY so they match `_induce_envelope`. Critic prompt says do **not** write a Negatives block; host `negatives_from_critic` still parses one — pick one format |
| No (clip) | `video.director/prompts/primary.md` size | Do not grow past packed-task 768 |

### P3 — Auto Pilot loop (ISSUE-0007 remainder)

13. After `generated_media`, optional pass_03: critic/continuity ASK on the clip, then re-assemble, then Imagine again. Gate with a human option (“another Auto Pilot cycle” / “stop”). Do not spin unbounded. `max_refinement_count: 0` must be raised **or** the loop stays host-owned and folders stay 0.

### P4 — Swarm structure (CSS v4) — do not fake a runner

14. **Do not** implement `POST /api/v3/swarms/{id}/runtime/run` to “match Chat.” Chat is a project collab log, not a v4 outer walk.
15. Optional later: a `swarms/video.asain-beauty/` **roster** that **names** the Chat parties (intent, creative, PE, five locks, camera, critic) as members, with topology = this spine. Fleet/Org/Workflow `?swarm=` filters to that roster so Org Chat and Main SVG stop looking like “the whole pack is this job.”
16. Keep v4 forbids: no swarm-wide Chat that bypasses per-agent runtime; no “auto-orchestrate with LLM” button; Org Chat remains non-mutating except local layout.
17. Until `/api/v3/swarms` exists, the Control UI title “Agent Swarm” should subtitle as **pack browser**, not swarm runner.

**CSS model: do not change the v4 schema.** Keep `casops.common_swarm.v4` / `schema_version: 4.0`. Do not add Auto Pilot fields, a fifth “project collab” plane, or a v5 swarm type so Chat can pretend to be a swarm walk. Project Chat stays `casops.project.v1` + comms. There is **no live swarm folder** to patch today (`swarms/` missing). Optional later work is a **new instance** of the existing roster model, not a spec change. Do not weaken v4 forbids to legalize swarm Chat.

| Change? | Field / rule | Action |
|---|---|---|
| No | `structure_id` `casops.common_swarm.v4` / schema `4.0` | Keep. Independent of member schema `3.0` |
| No | Members remain common-agent v3 folders | Swarm does not own SPEC, tools, keys, or persona |
| No | Forbid swarm-wide Chat / Chat bypassing per-agent `runtime/chat` | Keep. Project Chat is **host collab**, not v4 swarm Chat |
| No | Forbid `POST /api/v3/swarms/{id}/runtime/run` as the first Chat fix | Item 14. Outer walk is specified, `NOT_RUN`, not this spine |
| No | Forbid LLM as live orchestrator; topology search; envelope-mint to non-host; production-activation / plugin-execute / T3 / network via swarm JSON | Keep. v4 delivery note + §23 forbids |
| No | Eight swarm-native planes (topology, coordination, authority, commit, consistency, scheduling, propagation, + membership) | Do not shrink the spec to match asain-beauty. Do not implement them to “complete” Chat |
| No | `CIT-GATE-001` BLOCKED / deployment NO-GO | Unchanged. Chat Imagine 200 is not a swarm release |
| No | `/api/v3` only; no `/api/v1/swarms` | Keep |
| No | Org Chat as write surface / Workflow click as run | Keep read-only except local layout (already) |
| Doc only | §24 Control UI mapping | Optional note: `/projects/:id/chat` is project collab, not `/swarms/:id` Chat. Can live in `spec/ui.v1.md` (P5) instead of a v4 schema bump |
| Optional instance | `swarms/video.asain-beauty/` roster + `graph.json` = §1 hop parties | Item 15. Names the Chat subset so Fleet/Org/Workflow can `?swarm=` filter. Does **not** change v4 schema. Do not copy 114-agent SVG into that roster |
| Optional instance | `swarm_spec.json` on that folder | Standard v4 keys (`roster_ref`, `graph_ref`, …). No Auto Pilot-only keys. `wrote_locks: false` on compose-preview |

### P5 — Docs

18. Update `spec/ui.v1.md` (or a delta) with Project Chat / Workflow / Imagine. Point Help at `/projects/asain-beauty/chat` as the collab example.
19. Record on every Chat banner: `honesty: CHARACTERIZATION` for hops 1–43; `live` only for generate.

---

## 6. Suggested implementation order

1. P0 click-through + template contradiction (UI only; no new agent calls).  
2. P1 single sequencer + creativedirector roster + assembled hop + save_comms keys.  
3. P2 critique_edges / hop-list fixtures (still CHARACTERIZATION).  
4. P3 optional second cycle after clip.  
5. P4 swarm roster filter **after** P0–P1, never a live v4 runner as the first “fix Chat” task.

---

## 7. Out of scope / non-goals

- Production activation, T3, plugins, memory writes, network grants.  
- Claiming Chat 200 or Imagine 200 as agent-correct (ISSUE-0002 remains).  
- Writing `sample/`. Sending `GOLD_BODY_PROBE` to agents.  
- Implementing all 147 v4 swarm requirements to make asain-beauty “complete.”  
- Pixel-perfect redesign of Org Chat or the 114-agent SVG into the Auto Pilot DAG.

---

## 8. Evidence captured this issue

- `project/asain-beauty/comms.json`: 44 items; hops listed in §1; `autopilot.aligned`; locks PE/director/cin/mua=1, continuity=2; hop 44 `generated_media` `live: true`.  
- `project/asain-beauty/project.json`: `sub_workflow_id: video.template.b` (UGC Ad).  
- `ui/src/App.tsx`: no `/swarms/:id`. Org Chat `onNodeClick` → `agentHref`. Workflow SVG → `/agents/.../chat`.  
- `src/casops/api`: no `/api/v3/swarms`.  
- `agents/video.promptengineer/agent_spec.json`: `max_peer_hops: 0`, `max_refinement_count: 0`, critique outputs include `video.judge`.  
- `agents/specials.intent-analysis-agent/agent_spec.json`: `status: draft`, `critique_edges` `spagent.*`.  
- `swarms/` directory: missing.  
- Common Swarm Structure v4: specified, `NOT_RUN` locally, `CIT-GATE-001` BLOCKED, NO-GO for production.
