#!/usr/bin/env python3
"""Generate per-agent API test case folders under testcases/api_test/<agent_id>/."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Video pack agents (114) — offline agent-loop run
# ---------------------------------------------------------------------------
VIDEO_AGENTS = [
    "video.accessibility",
    "video.accessibilityoptimizer",
    "video.aiqaconsistency",
    "video.analyst",
    "video.animator_2d",
    "video.archivemaster",
    "video.archiveproducer",
    "video.archiveresearch",
    "video.audiencesim",
    "video.audiobooknarrator",
    "video.avatardesign",
    "video.awardsstrategist",
    "video.benchmarkresearch",
    "video.brand",
    "video.brandstrategist",
    "video.cameraoperator",
    "video.casting",
    "video.channelmanager",
    "video.childrensauthor",
    "video.choreography",
    "video.cinematographer",
    "video.citation",
    "video.colorist",
    "video.comedywriter",
    "video.comms",
    "video.community",
    "video.competitorintelligence",
    "video.compliance",
    "video.composer",
    "video.conceptartist",
    "video.continuity",
    "video.copywriter",
    "video.corrections",
    "video.costoptimizer",
    "video.costumedesign",
    "video.creativedirector",
    "video.critic",
    "video.crm",
    "video.deepfakedetection",
    "video.director",
    "video.distributor",
    "video.dronepilot",
    "video.editor",
    "video.emotionalarc",
    "video.ethics",
    "video.evaluationharness",
    "video.factchecker",
    "video.festivalstrategist",
    "video.finance",
    "video.foodstylist",
    "video.gatekeeper",
    "video.ideation",
    "video.instructionaldesign",
    "video.interviewsynthesis",
    "video.journalist",
    "video.judge",
    "video.labela_r",
    "video.labeldigital",
    "video.latencyoptimizer",
    "video.learnersim",
    "video.legal",
    "video.lipsync",
    "video.lms",
    "video.localizationqa",
    "video.marketing",
    "video.medicalillustrator",
    "video.memory",
    "video.moodboard",
    "video.motiongraphics",
    "video.mpa",
    "video.mua_makeup",
    "video.musicsupervisor",
    "video.musicvideodirector",
    "video.narrativearc",
    "video.novelty",
    "video.orchestrator",
    "video.performancemarketer",
    "video.personalizationengineer",
    "video.planner",
    "video.producer",
    "video.productiondesign",
    "video.promptengineer",
    "video.promptoptimizer",
    "video.realestatephoto",
    "video.retentionoptimizer",
    "video.roasoptimizer",
    "video.router",
    "video.safetyredteam",
    "video.sales",
    "video.screenwriter",
    "video.seo",
    "video.showrunner",
    "video.signlanguageinterpreter",
    "video.sme",
    "video.socialmediastrategist",
    "video.sounddesign",
    "video.soundmixer",
    "video.sportsanalyst",
    "video.standardseditor",
    "video.storyboard",
    "video.styletransfer",
    "video.talent",
    "video.templatedesign",
    "video.trailereditor",
    "video.travelcine",
    "video.trendintelligence",
    "video.trustsafety",
    "video.ugccreator",
    "video.ux",
    "video.vfxsupervisor",
    "video.voiceclone",
    "video.voiceover",
    "video.webresearch",
    "video.worldbuilding",
]

# Role-flavored goal templates (keyword → 3 goals)
ROLE_GOALS: list[tuple[re.Pattern[str], list[str]]] = [
    (
        re.compile(r"planner|orchestrator|showrunner|producer", re.I),
        [
            "Plan a 90-second offline wuxia short with clear acts and contingencies",
            "Produce a production plan skeleton for a 6-day travel vlog (artifact kinds only)",
            "Coordinate a multi-agent offline run for high-retention YouTube hook",
        ],
    ),
    (
        re.compile(r"director|cinematographer|camera|storyboard|travelcine|drone", re.I),
        [
            "Define shot language and camera moves for a neon night market walk-and-talk",
            "Storyboard three beats for a cold-open trailer style sequence",
            "Direct pacing and composition for a food close-up montage (structure only)",
        ],
    ),
    (
        re.compile(r"editor|trailer|colorist|motion|sound|music|voice|lipsync", re.I),
        [
            "Propose cut list and pacing grammar for a 60s retention-first short",
            "Design trailer cold-open hooks from day-highlight beats (refs only)",
            "Outline VO delivery and mix targets for documentary-style vlog",
        ],
    ),
    (
        re.compile(r"retention|audience|trend|marketing|seo|social|performance|roas", re.I),
        [
            "Rank candidate scenes for max mid-hold retention on a travel vlog",
            "Map platform hooks for YouTube long-form vs Shorts from the same brief",
            "Suggest CTR-worthy moment flags without inventing full itinerary text",
        ],
    ),
    (
        re.compile(r"research|web|archive|benchmark|citation|fact|journalist", re.I),
        [
            "Build an offline research brief skeleton for Osaka transit and season themes",
            "List fact-check claims that a travel VO might make (structure only)",
            "Assemble redacted research bundle refs for multi-day documentary lane",
        ],
    ),
    (
        re.compile(r"critic|judge|ethics|safety|compliance|legal|trust|gatekeeper|qa|aiqa", re.I),
        [
            "Critique selection for cliché and pacing completeness (bounded refine)",
            "Apply offline QC consistency checks across multi-day stub assets",
            "Gate package release with HITL-required decision notes only",
        ],
    ),
    (
        re.compile(r"screen|copy|comedy|narrative|emotional|world|ideation|concept", re.I),
        [
            "Draft beat-level VO structure for three selected travel segments",
            "Map emotional arc open/mid/close for a six-day trip story spine",
            "Ideate distinctive visual hooks without full script body",
        ],
    ),
]


def goals_for_video(agent_id: str) -> list[str]:
    short = agent_id.split(".", 1)[-1]
    for pat, goals in ROLE_GOALS:
        if pat.search(short) or pat.search(agent_id):
            return goals
    role = short.replace("_", " ")
    return [
        f"As {agent_id}, perform offline craft work for: short travel vlog high retention",
        f"Produce structure-only artifacts for role '{role}' on a 6-day Osaka-style brief",
        f"Self-review offline Plan→Act→Self-Review output for {agent_id} quality gates",
    ]


def pack_success(agent_id: str) -> dict:
    return {
        "http_status": [200],
        "required_keys_any": ["agent_id", "ok", "phases", "v3", "status", "run_id"],
        "json_equals": {"agent_id": agent_id},
        "notes": (
            "Offline loop: expect 200 with agent_id match; prefer ok=true or v3/phases present. "
            "allow_production/allow_network must stay false."
        ),
    }


def video_cases(agent_id: str) -> list[dict]:
    goals = goals_for_video(agent_id)
    cases = []
    for i, goal in enumerate(goals, start=1):
        cases.append(
            {
                "id": f"tc{i}",
                "name": f"{agent_id} offline case {i}",
                "method": "POST",
                "path": f"/api/v1/agent-loops/agents/{agent_id}/run",
                "body": {
                    "goal": goal,
                    "enable_v3": True,
                    "max_steps": 2 if i == 3 else 3,
                    "allow_production": False,
                    "allow_network": False,
                },
                "success_criteria": pack_success(agent_id),
            }
        )
    return cases


# ---------------------------------------------------------------------------
# Specials — Host special APIs
# ---------------------------------------------------------------------------
def special_def(
    agent_id: str,
    method: str,
    path: str,
    bodies: list[dict],
    names: list[str],
    success: dict,
) -> dict:
    cases = []
    for i, (body, name) in enumerate(zip(bodies, names, strict=True), start=1):
        cases.append(
            {
                "id": f"tc{i}",
                "name": name,
                "method": method,
                "path": path,
                "body": body,
                "success_criteria": success,
            }
        )
    return {
        "agent_id": agent_id,
        "kind": "special",
        "cases": cases,
    }


SPECIALS: list[dict] = [
    special_def(
        "specials.intent_analysis_agent",
        "POST",
        "/api/v1/intent/analyze",
        [
            {"text": "Make a 6-day Osaka travel vlog for high retention", "channel": "video_brief"},
            {"text": "Explain our SaaS pricing to enterprise buyers", "channel": "marketing"},
            {"text": "Offline only: classify multi-hop production intent", "channel": "video_brief"},
        ],
        ["Travel vlog brief", "B2B marketing brief", "Explicit offline classify"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "primary_intent", "intent", "correlation_id", "result"],
            "notes": "Expect 200 offline intent analysis without live LLM.",
        },
    ),
    special_def(
        "specials.research_agent",
        "POST",
        "/api/v1/research/query",
        [
            {"query": "Osaka travel production research offline", "allow_live_web": False},
            {"query": "Transit themes and seasonal constraints skeleton", "allow_live_web": False},
            {"query": "Documentary fact themes for multi-day vlog", "max_sources": 4, "allow_live_web": False},
        ],
        ["Osaka research offline", "Transit themes", "Documentary themes"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "sources", "brief", "result", "correlation_id"],
            "notes": "allow_live_web must stay false; offline research skeleton OK.",
        },
    ),
    special_def(
        "specials.thinking_model",
        "POST",
        "/api/v1/thinking/recommend",
        [
            {"goal": "Multi-day multi-hop production plan"},
            {"goal": "Choose cognitive profile for retention-first vlog pipeline"},
            {"goal": "Offline Cynefin-aware planning for agent crew"},
        ],
        ["Multi-hop plan", "Retention pipeline profile", "Cynefin crew planning"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "profile", "recommendation", "correlation_id", "result"],
            "notes": "Offline thinking recommend returns profile-like payload.",
        },
    ),
    special_def(
        "specials.strategic_goal_achievement_agent",
        "POST",
        "/api/v1/strategic/plan",
        [
            {"goal": "Ship high-retention Osaka travel vlog", "domain": "video"},
            {"goal": "Define KRs for offline simulated package HITL", "horizon": "project"},
            {"goal": "Stages-lite plan for multi-agent vlog simulation", "domain": "video"},
        ],
        ["Ship vlog goal", "Package HITL KRs", "Stages-lite multi-agent"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "plan", "objectives", "correlation_id", "result"],
            "notes": "Strategic offline plan without live OKR systems.",
        },
    ),
    special_def(
        "specials.knowledge_router_agent",
        "POST",
        "/api/v1/knowledge/route",
        [
            {"query": "Osaka logistics and vlog production", "allow_live_web": False},
            {"query": "Route memory vs pack vs RAG for travel brief", "allow_live_web": False},
            {"query": "Where to store production plan handoffs", "allow_live_web": False},
        ],
        ["Logistics route", "Memory vs pack route", "Handoff storage route"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "primary", "route", "correlation_id", "result"],
            "notes": "Offline knowledge router; no live web.",
        },
    ),
    special_def(
        "specials.aesthetics_agent",
        "POST",
        "/api/v1/aesthetics/evaluate",
        [
            {
                "artifact_ref": "look_bible_stub",
                "media_type": "image",
                "mode": "score",
                "allow_live_vision": False,
            },
            {
                "artifact_ref": "moodboard_stub_01",
                "media_type": "image",
                "mode": "score",
                "allow_live_vision": False,
            },
            {
                "artifact_ref": "grade_ref_stub",
                "media_type": "image",
                "mode": "score",
                "allow_live_vision": False,
            },
        ],
        ["Look bible score", "Moodboard score", "Grade ref score"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "scores", "result", "correlation_id", "evaluation"],
            "notes": "Offline aesthetic scoring; allow_live_vision false.",
        },
    ),
    special_def(
        "specials.optimization_agent",
        "POST",
        "/api/v1/optimization/recommend",
        [
            {"goal": "Improve mid-hold retention on travel vlog cuts", "kind": "retention"},
            {"goal": "Reduce drop-off after cold open", "kind": "retention"},
            {"goal": "DMAIC-lite suggestions for selection set", "kind": "retention"},
        ],
        ["Mid-hold retention", "Cold-open drop-off", "DMAIC selection"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "recommendations", "result", "correlation_id"],
            "notes": "Offline optimization recommend.",
        },
    ),
    special_def(
        "specials.coding_agent",
        "POST",
        "/api/v1/coding/plan",
        [
            {"goal": "Plan Host API smoke tests for agent-loops", "area": "host", "allow_network": False},
            {"goal": "Outline offline test harness for developer tokens", "area": "host"},
            {"goal": "Plan fail-closed Bearer auth regression checks", "area": "host", "allow_shell_exec": False},
        ],
        ["Agent-loop smoke plan", "Token harness plan", "Bearer auth regression plan"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "plan", "steps", "result", "correlation_id"],
            "notes": "Coding plan offline; no network/shell required.",
        },
    ),
    special_def(
        "specials.complex_problem_solution_process_model",
        "POST",
        "/api/v1/complex-problem/solve",
        [
            {"problem": "Coordinate multi-agent Osaka vlog simulation without live media", "max_steps": 5},
            {"problem": "Balance retention scoring vs directing cost", "context": "T3 before T4"},
            {"problem": "Fail-closed package release with HITL", "max_steps": 4},
        ],
        ["Multi-agent sim", "Retention vs directing", "HITL package"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "steps", "solution", "result", "correlation_id"],
            "notes": "Complex-problem offline process model.",
        },
    ),
    special_def(
        "specials.general_creative_agent",
        "POST",
        "/api/v1/creative/ideate",
        [
            {"brief": "Distinctive Osaka night market visual hooks", "n_candidates": 3, "domain": "video"},
            {"brief": "Cold-open motifs for travel documentary vlog", "genre": "documentary"},
            {"brief": "SSOR-lite ideation for food B-roll patterns", "n_candidates": 2},
        ],
        ["Night market hooks", "Cold-open motifs", "Food B-roll ideation"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "candidates", "ideas", "result", "correlation_id"],
            "notes": "Creative ideate offline.",
        },
    ),
    special_def(
        "specials.podcast_agent",
        "POST",
        "/api/v1/podcast/outline",
        [
            {"topic": "Behind the multi-agent Osaka vlog simulation", "duration_min": 20},
            {"topic": "Retention science for travel content", "format": "interview"},
            {"topic": "Offline Host tools for creators", "duration_min": 15, "allow_live_tts": False},
        ],
        ["Behind the sim episode", "Retention science episode", "Host tools episode"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "outline", "segments", "result", "correlation_id"],
            "notes": "Podcast outline offline; TTS live off.",
        },
    ),
    special_def(
        "specials.psychological_profile_agent",
        "POST",
        "/api/v1/psychology/profile",
        [
            {"brief": "Audience cohort for high-retention travel vlog viewers", "platform": "youtube"},
            {"brief": "Tone profile for documentary-style VO", "locale": "en"},
            {"brief": "Lite psych profile for short-form hooks", "mode": "lite"},
        ],
        ["YouTube cohort", "Documentary VO tone", "Shorts hooks profile"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "profile", "result", "correlation_id"],
            "notes": "Psychology profile offline.",
        },
    ),
    special_def(
        "specials.psychological_recommendation_agent",
        "POST",
        "/api/v1/psychology/recommend",
        [
            {"brief": "Recommend hook styles for curious food-travel audience", "n_hooks": 3},
            {"brief": "Suggest mid-video re-engagement beats", "n_hooks": 2},
            {"brief": "CTA framing for subscribe without hard sell", "n_hooks": 3},
        ],
        ["Food-travel hooks", "Mid-video re-engage", "Soft CTA framing"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "recommendations", "hooks", "result", "correlation_id"],
            "notes": "Psychology recommend offline.",
        },
    ),
    special_def(
        "specials.screenwriter_strategic_goal_achievement_agent",
        "POST",
        "/api/v1/screenwriting/plan",
        [
            {"logline_or_goal": "Travel vlog VO that motivates day-to-day curiosity", "form": "vlog"},
            {"logline_or_goal": "Documentary narration spine for six days", "genre": "documentary"},
            {"logline_or_goal": "Stages-lite VO motivation handoff", "form": "voiceover"},
        ],
        ["Curiosity VO", "Six-day narration spine", "VO motivation stages"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "plan", "beats", "result", "correlation_id"],
            "notes": "Screenwriting plan offline.",
        },
    ),
    special_def(
        "specials.llm_usage",
        "POST",
        "/api/v1/llm-usage/record",
        [
            {
                "operation": "api_test_pack_loop",
                "estimated_input_tokens": 1200,
                "estimated_output_tokens": 400,
                "agent_id": "video.planner",
                "offline": True,
            },
            {
                "operation": "api_test_special_intent",
                "estimated_input_tokens": 800,
                "estimated_output_tokens": 200,
                "offline": True,
            },
            {
                "operation": "api_test_budget_gate",
                "estimated_input_tokens": 5000,
                "estimated_output_tokens": 1000,
                "agent_id": "video.orchestrator",
                "offline": True,
            },
        ],
        ["Record pack loop usage", "Record special usage", "Record budget gate usage"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "recorded", "ledger", "result", "correlation_id", "status"],
            "notes": "Offline usage ledger record.",
        },
    ),
    special_def(
        "specials.agentic_rag",
        "POST",
        "/api/v1/rag/query",
        [
            {"query": "Osaka multi-day travel vlog logistics offline", "allow_live_web": False},
            {"query": "How Host package HITL works", "max_iterations": 2, "allow_chroma": False},
            {"query": "Agent-loop Plan Act Self-Review summary", "top_k": 5, "allow_live_web": False},
        ],
        ["Travel logistics RAG", "Package HITL RAG", "Agent-loop RAG"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "answer", "chunks", "result", "correlation_id"],
            "notes": "Agentic RAG offline; no live web/chroma required.",
        },
    ),
    special_def(
        "specials.video_generation_techology_should_learn_now",
        "POST",
        "/api/v1/tech-radar/advise",
        [
            {"goal": "Prefer offline media_stub for package simulation", "prefer_offline": True},
            {"goal": "Advise provider posture for travel vlog stub timeline", "prefer_offline": True},
            {"goal": "List tech to learn later without enabling live media", "prefer_offline": True},
        ],
        ["media_stub prefer", "Stub timeline providers", "Learn-later radar"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "advice", "providers", "result", "correlation_id"],
            "notes": "Tech radar offline advice.",
        },
    ),
    special_def(
        "specials.lifes_quiet_redemption_agent_workflow",
        "POST",
        "/api/v1/lqr/overview",
        [
            {"logline": "Quiet redemption arc across six travel days", "variant": "default"},
            {"logline": "Character finds belonging through local food rituals", "variant": "default"},
            {"logline": "Soft hope without melodrama for documentary VO", "variant": "default"},
        ],
        ["Six-day redemption", "Food rituals belonging", "Soft hope VO"],
        {
            "http_status": [200],
            "required_keys_any": ["ok", "overview", "stages", "result", "correlation_id"],
            "notes": "LQR overview offline.",
        },
    ),
    special_def(
        "specials.agent_loop_v3",
        "GET",
        "/api/v1/agent-loops/v3/policy",
        [
            {},
            {},
            {},
        ],
        ["v3 policy read A", "v3 policy read B", "v3 policy read C"],
        {
            "http_status": [200],
            "required_keys_any": ["patterns", "critic_modes", "note", "correlation_id", "activation_policy"],
            "notes": "agent_loop_v3 Host policy endpoint (GET); three probes for stability.",
        },
    ),
]


def write_agent(folder_name: str, payload: dict) -> None:
    # Windows-safe: keep dots in folder names (allowed)
    d = ROOT / folder_name
    d.mkdir(parents=True, exist_ok=True)
    (d / "cases.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    # One-line summary for humans
    (d / "README.md").write_text(
        f"# {payload['agent_id']}\n\n"
        f"- kind: `{payload.get('kind')}`\n"
        f"- cases: {len(payload.get('cases') or [])}\n"
        f"- run: `python run_all_api_tests.py --only {payload['agent_id']}`\n",
        encoding="utf-8",
    )


def main() -> None:
    count = 0
    for aid in VIDEO_AGENTS:
        payload = {
            "agent_id": aid,
            "kind": "pack",
            "cases": video_cases(aid),
        }
        write_agent(aid, payload)
        count += 1

    for spec in SPECIALS:
        write_agent(spec["agent_id"], spec)
        count += 1

    index = {
        "pack_count": len(VIDEO_AGENTS),
        "special_count": len(SPECIALS),
        "total_agents": count,
        "cases_per_agent": 3,
        "total_cases": count * 3,
        "pack_agents": VIDEO_AGENTS,
        "special_agents": [s["agent_id"] for s in SPECIALS],
    }
    (ROOT / "index.json").write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {count} agent folders ({count * 3} cases) under {ROOT}")


if __name__ == "__main__":
    main()
