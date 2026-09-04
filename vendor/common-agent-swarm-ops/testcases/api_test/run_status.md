# API test run status

Source: `testcases/api_test/reports/latest.json`

## Summary

| Field | Value |
|-------|-------|
| **Started** | 2026-08-11T06:42:10.350306+00:00 |
| **Finished** | 2026-08-11T06:45:35.801965+00:00 |
| **Host** | `http://127.0.0.1:8000` |
| **Auth** | bearer |
| **Minted key id** | `tok_f6b6e816dbf448a1` |
| **Agents** | 133 |
| **Cases total** | 399 |
| **Cases passed** | 399 |
| **Cases failed (product)** | 0 |
| **Cases skipped (429)** | 0 |
| **Pass rate (all cases)** | 100.0% |
| **Pass rate (excl. 429 skip)** | 100.0% |

## Runner settings (if present)

| Setting | Value |
|---------|-------|
| sleep | 0.35 |
| max_429_retries | 5 |
| batch_size / batch_pause | 80 / 5.0 |
| rate_limit_as_skip | True |

## Agent rollup

| Status | Meaning | Count |
|--------|---------|------:|
| **PASS** | No product fails (skips OK) | 133 |
| **PARTIAL** | Mix of pass/fail/skip | 0 |
| **FAIL** | Only product fails | 0 |
| **SKIP_429** | Only rate-limit skips | 0 |
| **Total agents** | | 133 |

## By kind

| Kind | Agents | Full PASS | Full FAIL | PARTIAL |
|------|-------:|----------:|----------:|--------:|
| Pack (`video.*`) | 114 | 114 | 0 | 0 |
| Specials (`specials.*`) | 19 | 19 | 0 | 0 |

## Failure HTTP status breakdown (product FAIL only)

| HTTP status | Failed cases |
|------------:|-------------:|

## Failure reason buckets (product FAIL only)

| Reason | Count |
|--------|------:|

## All agents (pass / fail / skip counts)

| Agent id | Kind | Passed | Failed | Skip 429 | Status |
|----------|------|-------:|-------:|---------:|--------|
| `specials.aesthetics_agent` | special | 3 | 0 | 0 | **PASS** |
| `specials.agent_loop_v3` | special | 3 | 0 | 0 | **PASS** |
| `specials.agentic_rag` | special | 3 | 0 | 0 | **PASS** |
| `specials.coding_agent` | special | 3 | 0 | 0 | **PASS** |
| `specials.complex_problem_solution_process_model` | special | 3 | 0 | 0 | **PASS** |
| `specials.general_creative_agent` | special | 3 | 0 | 0 | **PASS** |
| `specials.intent_analysis_agent` | special | 3 | 0 | 0 | **PASS** |
| `specials.knowledge_router_agent` | special | 3 | 0 | 0 | **PASS** |
| `specials.lifes_quiet_redemption_agent_workflow` | special | 3 | 0 | 0 | **PASS** |
| `specials.llm_usage` | special | 3 | 0 | 0 | **PASS** |
| `specials.optimization_agent` | special | 3 | 0 | 0 | **PASS** |
| `specials.podcast_agent` | special | 3 | 0 | 0 | **PASS** |
| `specials.psychological_profile_agent` | special | 3 | 0 | 0 | **PASS** |
| `specials.psychological_recommendation_agent` | special | 3 | 0 | 0 | **PASS** |
| `specials.research_agent` | special | 3 | 0 | 0 | **PASS** |
| `specials.screenwriter_strategic_goal_achievement_agent` | special | 3 | 0 | 0 | **PASS** |
| `specials.strategic_goal_achievement_agent` | special | 3 | 0 | 0 | **PASS** |
| `specials.thinking_model` | special | 3 | 0 | 0 | **PASS** |
| `specials.video_generation_techology_should_learn_now` | special | 3 | 0 | 0 | **PASS** |
| `video.accessibility` | pack | 3 | 0 | 0 | **PASS** |
| `video.accessibilityoptimizer` | pack | 3 | 0 | 0 | **PASS** |
| `video.aiqaconsistency` | pack | 3 | 0 | 0 | **PASS** |
| `video.analyst` | pack | 3 | 0 | 0 | **PASS** |
| `video.animator_2d` | pack | 3 | 0 | 0 | **PASS** |
| `video.archivemaster` | pack | 3 | 0 | 0 | **PASS** |
| `video.archiveproducer` | pack | 3 | 0 | 0 | **PASS** |
| `video.archiveresearch` | pack | 3 | 0 | 0 | **PASS** |
| `video.audiencesim` | pack | 3 | 0 | 0 | **PASS** |
| `video.audiobooknarrator` | pack | 3 | 0 | 0 | **PASS** |
| `video.avatardesign` | pack | 3 | 0 | 0 | **PASS** |
| `video.awardsstrategist` | pack | 3 | 0 | 0 | **PASS** |
| `video.benchmarkresearch` | pack | 3 | 0 | 0 | **PASS** |
| `video.brand` | pack | 3 | 0 | 0 | **PASS** |
| `video.brandstrategist` | pack | 3 | 0 | 0 | **PASS** |
| `video.cameraoperator` | pack | 3 | 0 | 0 | **PASS** |
| `video.casting` | pack | 3 | 0 | 0 | **PASS** |
| `video.channelmanager` | pack | 3 | 0 | 0 | **PASS** |
| `video.childrensauthor` | pack | 3 | 0 | 0 | **PASS** |
| `video.choreography` | pack | 3 | 0 | 0 | **PASS** |
| `video.cinematographer` | pack | 3 | 0 | 0 | **PASS** |
| `video.citation` | pack | 3 | 0 | 0 | **PASS** |
| `video.colorist` | pack | 3 | 0 | 0 | **PASS** |
| `video.comedywriter` | pack | 3 | 0 | 0 | **PASS** |
| `video.comms` | pack | 3 | 0 | 0 | **PASS** |
| `video.community` | pack | 3 | 0 | 0 | **PASS** |
| `video.competitorintelligence` | pack | 3 | 0 | 0 | **PASS** |
| `video.compliance` | pack | 3 | 0 | 0 | **PASS** |
| `video.composer` | pack | 3 | 0 | 0 | **PASS** |
| `video.conceptartist` | pack | 3 | 0 | 0 | **PASS** |
| `video.continuity` | pack | 3 | 0 | 0 | **PASS** |
| `video.copywriter` | pack | 3 | 0 | 0 | **PASS** |
| `video.corrections` | pack | 3 | 0 | 0 | **PASS** |
| `video.costoptimizer` | pack | 3 | 0 | 0 | **PASS** |
| `video.costumedesign` | pack | 3 | 0 | 0 | **PASS** |
| `video.creativedirector` | pack | 3 | 0 | 0 | **PASS** |
| `video.critic` | pack | 3 | 0 | 0 | **PASS** |
| `video.crm` | pack | 3 | 0 | 0 | **PASS** |
| `video.deepfakedetection` | pack | 3 | 0 | 0 | **PASS** |
| `video.director` | pack | 3 | 0 | 0 | **PASS** |
| `video.distributor` | pack | 3 | 0 | 0 | **PASS** |
| `video.dronepilot` | pack | 3 | 0 | 0 | **PASS** |
| `video.editor` | pack | 3 | 0 | 0 | **PASS** |
| `video.emotionalarc` | pack | 3 | 0 | 0 | **PASS** |
| `video.ethics` | pack | 3 | 0 | 0 | **PASS** |
| `video.evaluationharness` | pack | 3 | 0 | 0 | **PASS** |
| `video.factchecker` | pack | 3 | 0 | 0 | **PASS** |
| `video.festivalstrategist` | pack | 3 | 0 | 0 | **PASS** |
| `video.finance` | pack | 3 | 0 | 0 | **PASS** |
| `video.foodstylist` | pack | 3 | 0 | 0 | **PASS** |
| `video.gatekeeper` | pack | 3 | 0 | 0 | **PASS** |
| `video.ideation` | pack | 3 | 0 | 0 | **PASS** |
| `video.instructionaldesign` | pack | 3 | 0 | 0 | **PASS** |
| `video.interviewsynthesis` | pack | 3 | 0 | 0 | **PASS** |
| `video.journalist` | pack | 3 | 0 | 0 | **PASS** |
| `video.judge` | pack | 3 | 0 | 0 | **PASS** |
| `video.labela_r` | pack | 3 | 0 | 0 | **PASS** |
| `video.labeldigital` | pack | 3 | 0 | 0 | **PASS** |
| `video.latencyoptimizer` | pack | 3 | 0 | 0 | **PASS** |
| `video.learnersim` | pack | 3 | 0 | 0 | **PASS** |
| `video.legal` | pack | 3 | 0 | 0 | **PASS** |
| `video.lipsync` | pack | 3 | 0 | 0 | **PASS** |
| `video.lms` | pack | 3 | 0 | 0 | **PASS** |
| `video.localizationqa` | pack | 3 | 0 | 0 | **PASS** |
| `video.marketing` | pack | 3 | 0 | 0 | **PASS** |
| `video.medicalillustrator` | pack | 3 | 0 | 0 | **PASS** |
| `video.memory` | pack | 3 | 0 | 0 | **PASS** |
| `video.moodboard` | pack | 3 | 0 | 0 | **PASS** |
| `video.motiongraphics` | pack | 3 | 0 | 0 | **PASS** |
| `video.mpa` | pack | 3 | 0 | 0 | **PASS** |
| `video.mua_makeup` | pack | 3 | 0 | 0 | **PASS** |
| `video.musicsupervisor` | pack | 3 | 0 | 0 | **PASS** |
| `video.musicvideodirector` | pack | 3 | 0 | 0 | **PASS** |
| `video.narrativearc` | pack | 3 | 0 | 0 | **PASS** |
| `video.novelty` | pack | 3 | 0 | 0 | **PASS** |
| `video.orchestrator` | pack | 3 | 0 | 0 | **PASS** |
| `video.performancemarketer` | pack | 3 | 0 | 0 | **PASS** |
| `video.personalizationengineer` | pack | 3 | 0 | 0 | **PASS** |
| `video.planner` | pack | 3 | 0 | 0 | **PASS** |
| `video.producer` | pack | 3 | 0 | 0 | **PASS** |
| `video.productiondesign` | pack | 3 | 0 | 0 | **PASS** |
| `video.promptengineer` | pack | 3 | 0 | 0 | **PASS** |
| `video.promptoptimizer` | pack | 3 | 0 | 0 | **PASS** |
| `video.realestatephoto` | pack | 3 | 0 | 0 | **PASS** |
| `video.retentionoptimizer` | pack | 3 | 0 | 0 | **PASS** |
| `video.roasoptimizer` | pack | 3 | 0 | 0 | **PASS** |
| `video.router` | pack | 3 | 0 | 0 | **PASS** |
| `video.safetyredteam` | pack | 3 | 0 | 0 | **PASS** |
| `video.sales` | pack | 3 | 0 | 0 | **PASS** |
| `video.screenwriter` | pack | 3 | 0 | 0 | **PASS** |
| `video.seo` | pack | 3 | 0 | 0 | **PASS** |
| `video.showrunner` | pack | 3 | 0 | 0 | **PASS** |
| `video.signlanguageinterpreter` | pack | 3 | 0 | 0 | **PASS** |
| `video.sme` | pack | 3 | 0 | 0 | **PASS** |
| `video.socialmediastrategist` | pack | 3 | 0 | 0 | **PASS** |
| `video.sounddesign` | pack | 3 | 0 | 0 | **PASS** |
| `video.soundmixer` | pack | 3 | 0 | 0 | **PASS** |
| `video.sportsanalyst` | pack | 3 | 0 | 0 | **PASS** |
| `video.standardseditor` | pack | 3 | 0 | 0 | **PASS** |
| `video.storyboard` | pack | 3 | 0 | 0 | **PASS** |
| `video.styletransfer` | pack | 3 | 0 | 0 | **PASS** |
| `video.talent` | pack | 3 | 0 | 0 | **PASS** |
| `video.templatedesign` | pack | 3 | 0 | 0 | **PASS** |
| `video.trailereditor` | pack | 3 | 0 | 0 | **PASS** |
| `video.travelcine` | pack | 3 | 0 | 0 | **PASS** |
| `video.trendintelligence` | pack | 3 | 0 | 0 | **PASS** |
| `video.trustsafety` | pack | 3 | 0 | 0 | **PASS** |
| `video.ugccreator` | pack | 3 | 0 | 0 | **PASS** |
| `video.ux` | pack | 3 | 0 | 0 | **PASS** |
| `video.vfxsupervisor` | pack | 3 | 0 | 0 | **PASS** |
| `video.voiceclone` | pack | 3 | 0 | 0 | **PASS** |
| `video.voiceover` | pack | 3 | 0 | 0 | **PASS** |
| `video.webresearch` | pack | 3 | 0 | 0 | **PASS** |
| `video.worldbuilding` | pack | 3 | 0 | 0 | **PASS** |

## Specials — case detail

| Agent | Case | Name | HTTP | Result | Duration (ms) |
|-------|------|------|-----:|--------|--------------:|
| `specials.aesthetics_agent` | tc1 | Look bible score | 200 | **PASS** | 24.4 |
| `specials.aesthetics_agent` | tc2 | Moodboard score | 200 | **PASS** | 16.0 |
| `specials.aesthetics_agent` | tc3 | Grade ref score | 200 | **PASS** | 15.5 |
| `specials.agent_loop_v3` | tc1 | v3 policy read A | 200 | **PASS** | 14.9 |
| `specials.agent_loop_v3` | tc2 | v3 policy read B | 200 | **PASS** | 14.9 |
| `specials.agent_loop_v3` | tc3 | v3 policy read C | 200 | **PASS** | 23.5 |
| `specials.agentic_rag` | tc1 | Travel logistics RAG | 200 | **PASS** | 20.7 |
| `specials.agentic_rag` | tc2 | Package HITL RAG | 200 | **PASS** | 30.7 |
| `specials.agentic_rag` | tc3 | Agent-loop RAG | 200 | **PASS** | 16.1 |
| `specials.coding_agent` | tc1 | Agent-loop smoke plan | 200 | **PASS** | 15.4 |
| `specials.coding_agent` | tc2 | Token harness plan | 200 | **PASS** | 21.6 |
| `specials.coding_agent` | tc3 | Bearer auth regression plan | 200 | **PASS** | 10.5 |
| `specials.complex_problem_solution_process_model` | tc1 | Multi-agent sim | 200 | **PASS** | 8.0 |
| `specials.complex_problem_solution_process_model` | tc2 | Retention vs directing | 200 | **PASS** | 18.6 |
| `specials.complex_problem_solution_process_model` | tc3 | HITL package | 200 | **PASS** | 16.6 |
| `specials.general_creative_agent` | tc1 | Night market hooks | 200 | **PASS** | 29.3 |
| `specials.general_creative_agent` | tc2 | Cold-open motifs | 200 | **PASS** | 29.1 |
| `specials.general_creative_agent` | tc3 | Food B-roll ideation | 200 | **PASS** | 20.1 |
| `specials.intent_analysis_agent` | tc1 | Travel vlog brief | 200 | **PASS** | 16.6 |
| `specials.intent_analysis_agent` | tc2 | B2B marketing brief | 200 | **PASS** | 17.9 |
| `specials.intent_analysis_agent` | tc3 | Explicit offline classify | 200 | **PASS** | 19.4 |
| `specials.knowledge_router_agent` | tc1 | Logistics route | 200 | **PASS** | 17.3 |
| `specials.knowledge_router_agent` | tc2 | Memory vs pack route | 200 | **PASS** | 7.5 |
| `specials.knowledge_router_agent` | tc3 | Handoff storage route | 200 | **PASS** | 18.1 |
| `specials.lifes_quiet_redemption_agent_workflow` | tc1 | Six-day redemption | 200 | **PASS** | 16.4 |
| `specials.lifes_quiet_redemption_agent_workflow` | tc2 | Food rituals belonging | 200 | **PASS** | 14.9 |
| `specials.lifes_quiet_redemption_agent_workflow` | tc3 | Soft hope VO | 200 | **PASS** | 14.7 |
| `specials.llm_usage` | tc1 | Record pack loop usage | 200 | **PASS** | 15.3 |
| `specials.llm_usage` | tc2 | Record special usage | 200 | **PASS** | 16.1 |
| `specials.llm_usage` | tc3 | Record budget gate usage | 200 | **PASS** | 15.2 |
| `specials.optimization_agent` | tc1 | Mid-hold retention | 200 | **PASS** | 7.2 |
| `specials.optimization_agent` | tc2 | Cold-open drop-off | 200 | **PASS** | 27.3 |
| `specials.optimization_agent` | tc3 | DMAIC selection | 200 | **PASS** | 9.6 |
| `specials.podcast_agent` | tc1 | Behind the sim episode | 200 | **PASS** | 11.2 |
| `specials.podcast_agent` | tc2 | Retention science episode | 200 | **PASS** | 21.2 |
| `specials.podcast_agent` | tc3 | Host tools episode | 200 | **PASS** | 14.4 |
| `specials.psychological_profile_agent` | tc1 | YouTube cohort | 200 | **PASS** | 18.9 |
| `specials.psychological_profile_agent` | tc2 | Documentary VO tone | 200 | **PASS** | 7.6 |
| `specials.psychological_profile_agent` | tc3 | Shorts hooks profile | 200 | **PASS** | 24.2 |
| `specials.psychological_recommendation_agent` | tc1 | Food-travel hooks | 200 | **PASS** | 18.7 |
| `specials.psychological_recommendation_agent` | tc2 | Mid-video re-engage | 200 | **PASS** | 14.5 |
| `specials.psychological_recommendation_agent` | tc3 | Soft CTA framing | 200 | **PASS** | 15.3 |
| `specials.research_agent` | tc1 | Osaka research offline | 200 | **PASS** | 25.8 |
| `specials.research_agent` | tc2 | Transit themes | 200 | **PASS** | 19.3 |
| `specials.research_agent` | tc3 | Documentary themes | 200 | **PASS** | 19.6 |
| `specials.screenwriter_strategic_goal_achievement_agent` | tc1 | Curiosity VO | 200 | **PASS** | 16.3 |
| `specials.screenwriter_strategic_goal_achievement_agent` | tc2 | Six-day narration spine | 200 | **PASS** | 50.8 |
| `specials.screenwriter_strategic_goal_achievement_agent` | tc3 | VO motivation stages | 200 | **PASS** | 15.7 |
| `specials.strategic_goal_achievement_agent` | tc1 | Ship vlog goal | 200 | **PASS** | 15.6 |
| `specials.strategic_goal_achievement_agent` | tc2 | Package HITL KRs | 200 | **PASS** | 15.8 |
| `specials.strategic_goal_achievement_agent` | tc3 | Stages-lite multi-agent | 200 | **PASS** | 17.3 |
| `specials.thinking_model` | tc1 | Multi-hop plan | 200 | **PASS** | 15.5 |
| `specials.thinking_model` | tc2 | Retention pipeline profile | 200 | **PASS** | 40.3 |
| `specials.thinking_model` | tc3 | Cynefin crew planning | 200 | **PASS** | 28.6 |
| `specials.video_generation_techology_should_learn_now` | tc1 | media_stub prefer | 200 | **PASS** | 21.4 |
| `specials.video_generation_techology_should_learn_now` | tc2 | Stub timeline providers | 200 | **PASS** | 16.7 |
| `specials.video_generation_techology_should_learn_now` | tc3 | Learn-later radar | 200 | **PASS** | 17.8 |

## Failed cases (all)

| Agent | Case | Name | HTTP | Failures |
|-------|------|------|-----:|----------|

## How to re-run

```powershell
cd C:\Project\common-agent-swarm-ops\testcases\api_test
python run_all_api_tests.py --host http://127.0.0.1:8000 --mint
python render_run_status.py
```

---

*Generated from `reports/latest.json` by `render_run_status.py`.*
