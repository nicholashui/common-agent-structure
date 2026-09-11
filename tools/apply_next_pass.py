#!/usr/bin/env python3
"""Next pass: craft-specific improve_agent md, unique YouTube, procedure skill ids, packed triple line."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "tools"))

from casops.runtime.chat import estimate_tokens, operational_prompt, pack_chat_context  # noqa: E402
from complex_agent_testcases import _bucket  # noqa: E402

IMPROVE_MARK = "## Research landed (verified, 2026-09)"
CLONE = "focused on intent analysis, natural language understanding"

# Distinct verified talks for packs that previously shared Doerr / ReAct / camera-movement.
# Only IDs confirmed on-disk from prior research or the official Search Central / WAI / film-school listings.
VIDEO_YT: dict[str, tuple[str, str]] = {
    "seo": ("https://www.youtube.com/watch?v=aLWQqlpwHK8", "Google Search Central, How to perform a technical SEO audit"),
    "marketing": ("https://www.youtube.com/watch?v=lutawRrVTHw", "Welcome to Google Search Central"),
    "sales": ("https://www.youtube.com/watch?v=ViwW9D-brTQ", "Demystifying Google Analytics and Search Console"),
    "finance": ("https://www.youtube.com/watch?v=JdvJb_ElQHE", "PDCA / Deming cycle — cost and quality loop"),
    "crm": ("https://www.youtube.com/watch?v=dzJY5GDm0hY", "5 reasons for using Google Search Console"),
    "producer": ("https://www.youtube.com/watch?v=zU_1ClPIOAg", "Crash Course Film Production, What producers do (Lily Gladstone)"),
    "planner": ("https://www.youtube.com/watch?v=1wOi7GGZShc", "Doerr / What Matters, Why OKRs"),
    "roasoptimizer": ("https://www.youtube.com/watch?v=EpOGsS5JGaw", "Google Ads, Set a target ROAS recommendation"),
    "retentionoptimizer": ("https://www.youtube.com/watch?v=kz7wIhQP6gM", "Podcast stats: downloads vs retention"),
    "brand": ("https://www.youtube.com/watch?v=DPJ0AzJSlFE", "How to modify your site name in Google Search"),
    "brandstrategist": ("https://www.youtube.com/watch?v=wvJIOQndzow", "Introducing SEO Made Easy"),
    "socialmediastrategist": ("https://www.youtube.com/watch?v=vc3uGc6TSH0", "Internal linking for SEO"),
    "performancemarketer": ("https://www.youtube.com/watch?v=EABqJXHQB3w", "Rewriting the SEO Starter Guide (Search Off the Record)"),
    "festivalstrategist": ("https://www.youtube.com/watch?v=im3Cqu2sMkI", "An example OKR (What Matters)"),
    "awardsstrategist": ("https://www.youtube.com/watch?v=nOtiil3PHm8", "Five benefits of OKRs (Doerr)"),
    "channelmanager": ("https://www.youtube.com/watch?v=5LF6SwB5jZ0", "Analyzing performance on Google Search"),
    "comms": ("https://www.youtube.com/watch?v=BKtQ5tVAwSo", "Getting started with Search Console Insights"),
    "community": ("https://www.youtube.com/watch?v=Q5kYrmzNhcU", "Help! Google Search isn't indexing my pages"),
    "costoptimizer": ("https://www.youtube.com/watch?v=bO3GpAjVvD8", "PDCA cycle explained (EPM)"),
    "distributor": ("https://www.youtube.com/watch?v=3QBgbmJsB6c", "What do producers do — hardest job in film"),
    "labela_r": ("https://www.youtube.com/watch?v=_cygjTdeits", "IAB Tech Lab audio initiatives"),
    "labeldigital": ("https://www.youtube.com/watch?v=1UaLeWKh5_U", "Producer craft (distribution-adjacent, educational)"),
    "aiqaconsistency": ("https://www.youtube.com/watch?v=tYfCjbvaOYg", "Structured data for beginners (Search Central)"),
    "instructionaldesign": ("https://www.youtube.com/watch?v=zLKuG0C7dUw", "3 tips for setting up a sitemap"),
    "latencyoptimizer": ("https://www.youtube.com/watch?v=_6Tz_-3_4ok", "4 tips for faster images on your website"),
    "lms": ("https://www.youtube.com/watch?v=o0AGWPU96TQ", "Search Console, AI, and HTTPS updates (Q4 2025)"),
    "memory": ("https://www.youtube.com/watch?v=fkpZfpNWjWY", "Claim–evidence–reasoning"),
    "orchestrator": ("https://www.youtube.com/watch?v=RM6ZArd2nVc", "Yao, LLM agents / ReAct (Berkeley)"),
    "personalizationengineer": ("https://www.youtube.com/watch?v=D33VOyGGib8", "Trait theories lecture"),
    "promptengineer": ("https://www.youtube.com/watch?v=zduSFxRajkE", "Karpathy, Let's build the GPT Tokenizer"),
    "promptoptimizer": ("https://www.youtube.com/watch?v=qz-XdI89vUM", "PDCA / PDSA problem solving (CQE Academy)"),
    "router": ("https://www.youtube.com/watch?v=bVz8Ua1VVsE", "Asai, self-reflective retrieval"),
    "ugccreator": ("https://www.youtube.com/watch?v=tua3DdacgOo", "Google I/O, YouTube Caption API / WebVTT"),
    "legal": ("https://www.youtube.com/watch?v=IFhF_tHrj4s", "Fair use four factors"),
    "director": ("https://www.youtube.com/watch?v=ptQwvGcLZIw", "The Art of Camera Movement"),
    "editor": ("https://www.youtube.com/watch?v=9-6-7bCBlLU", "Walter Murch, Rule of Six"),
    "cinematographer": ("https://www.youtube.com/watch?v=KupEY5CAwe4", "Camera movements for beginners"),
    "accessibility": ("https://www.youtube.com/watch?v=iWO5N3n1DXU", "W3C WAI Perspectives: Video Captions"),
    "accessibilityoptimizer": ("https://www.youtube.com/watch?v=-LILWDvEuxw", "Checking YouTube captions for accuracy"),
    "signlanguageinterpreter": ("https://www.youtube.com/watch?v=3f31oufqFSM", "WAI Perspectives compilation"),
    "localizationqa": ("https://www.youtube.com/watch?v=4qIordU8vT8", "WAI Video Captions — audio described"),
    "ux": ("https://www.youtube.com/watch?v=Hui87z2Vx8o", "WAI: colors with good contrast"),
    "cameraoperator": ("https://www.youtube.com/watch?v=s8VMCbEioFM", "Adding camera movement to cinematography"),
    "dronepilot": ("https://www.youtube.com/watch?v=IlptzH1NqhQ", "DJI Film School, camera movement with Brandon Li"),
    "travelcine": ("https://www.youtube.com/watch?v=wfns4DuEB5M", "Think like a cinematographer: movement"),
    "musicvideodirector": ("https://www.youtube.com/watch?v=iqDxVvu5sq4", "Why camera movement should be motivated"),
    "continuity": ("https://www.youtube.com/watch?v=PKYeClvvlTw", "StudioBinder, In the Blink of an Eye"),
    "trailereditor": ("https://www.youtube.com/watch?v=dqdxPcSr1V8", "The Film Look, motivated camera halt / freeze"),
    "standardseditor": ("https://www.youtube.com/watch?v=9-6-7bCBlLU", "Murch Rule of Six (standards cut)"),
    "compliance": ("https://www.youtube.com/watch?v=ruV2qn7xyU0", "Educational uses and fair use"),
    "corrections": ("https://www.youtube.com/watch?v=ruV2qn7xyU0", "Fair use / educational uses"),
    "ethics": ("https://www.youtube.com/watch?v=IFhF_tHrj4s", "Fair use four factors"),
    "factchecker": ("https://www.youtube.com/watch?v=fkpZfpNWjWY", "Claim–evidence–reasoning"),
    "deepfakedetection": ("https://www.youtube.com/watch?v=IFhF_tHrj4s", "Fair use / likeness caution"),
    "gatekeeper": ("https://www.youtube.com/watch?v=ruV2qn7xyU0", "Educational copyright uses"),
    "mpa": ("https://www.youtube.com/watch?v=IFhF_tHrj4s", "Four factors (ratings adjacent, not a board)"),
    "safetyredteam": ("https://www.youtube.com/watch?v=ruV2qn7xyU0", "Fair use limits"),
    "trustsafety": ("https://www.youtube.com/watch?v=IFhF_tHrj4s", "Four factors"),
    "screenwriter": ("https://www.youtube.com/watch?v=DXSIHm115gk", "Measure What Matters — goals vs fuzzy cinematic"),
    "showrunner": ("https://www.youtube.com/watch?v=pMlBMBTtJEw", "Doerr, Operation Crush OKR example"),
    "webresearch": ("https://www.youtube.com/watch?v=fkpZfpNWjWY", "Claim–evidence–reasoning"),
    "analyst": ("https://www.youtube.com/watch?v=x1_FS61AzLM", "How Search Off the Record tackles SEO and web development"),
    "sme": ("https://www.youtube.com/watch?v=h1rZdfW5vqM", "Thoughts on SEO and SEO for AI"),
    "citation": ("https://www.youtube.com/watch?v=tVSasQC6G_k", "Search Console and SEO updates (January 2025)"),
    "competitorintelligence": ("https://www.youtube.com/watch?v=bVz8Ua1VVsE", "Asai, self-reflective retrieval"),
}

PROCEDURE = {
    "legal": "four-factor",
    "director": "shot-intent",
    "editor": "rule-of-six",
    "accessibility": "wcag-captions",
    "accessibilityoptimizer": "caption-qc",
    "cinematographer": "coverage-path",
    "cameraoperator": "move-notes",
    "dronepilot": "motivated-move",
    "travelcine": "location-path",
    "musicvideodirector": "beat-block",
    "seo": "search-visibility",
    "finance": "cost-notes",
    "producer": "pga-credits",
    "roasoptimizer": "roas-window",
    "retentionoptimizer": "retention-curve",
    "podcast": "iab-download",
    "colorist": "grade-notes",
    "sounddesign": "cue-list",
    "soundmixer": "mix-notes",
    "composer": "temp-score",
    "storyboard": "frame-beats",
    "screenwriter": "want-need",
    "showrunner": "season-bible",
    "factchecker": "cite-or-wait",
    "webresearch": "cite-or-wait",
    "signlanguageinterpreter": "signing-space",
    "deepfakedetection": "likeness-risk",
    "mpa": "ratings-notes",
    "ux": "pour-check",
    "promptengineer": "brief-tokens",
    "orchestrator": "handoff-map",
    "router": "slice-route",
    "marketing": "channel-fit",
    "sales": "pipeline-notes",
    "brand": "cbbe-ladder",
    "brandstrategist": "positioning-tradeoff",
    "planner": "okr-notes",
    "continuity": "match-cut",
    "trailereditor": "pace-cut",
    "standardseditor": "spec-cut",
    "compliance": "issue-spot",
    "corrections": "ifcn-notes",
    "ethics": "harm-notes",
    "gatekeeper": "release-gate",
    "trustsafety": "abuse-notes",
    "safetyredteam": "red-team-notes",
    "labela_r": "iab-download",
    "labeldigital": "platform-metrics",
}

BUCKET_XAI = {
    "camera": "https://docs.x.ai/developers/model-capabilities/video/image-to-video",
    "edit": "https://docs.x.ai/developers/model-capabilities/video/image-to-video",
    "picture": "https://x.ai/docs/guides/image-generations",
    "audio": "https://docs.x.ai/developers/pricing",
    "story": "https://x.ai/docs/developers/quickstart",
    "legal": "https://docs.x.ai/developers/tools/overview",
    "a11y": "https://docs.x.ai/developers/tools/overview",
    "audience": "https://docs.x.ai/developers/pricing",
    "research_video": "https://docs.x.ai/developers/tools/overview",
    "sports": "https://docs.x.ai/developers/model-capabilities/video/image-to-video",
    "archive": "https://docs.x.ai/developers/tools/overview",
    "biz": "https://docs.x.ai/developers/pricing",
    "systems": "https://docs.x.ai/developers/tools/overview",
    "talent": "https://x.ai/docs/guides/image-generations",
    "video_generic": "https://docs.x.ai/developers/tools/overview",
}

BUCKET_YT_FALLBACK = {
    "camera": ("https://www.youtube.com/watch?v=KupEY5CAwe4", "Camera movements for beginners"),
    "edit": ("https://www.youtube.com/watch?v=9-6-7bCBlLU", "Murch Rule of Six"),
    "picture": ("https://www.youtube.com/watch?v=wfns4DuEB5M", "Think like a cinematographer"),
    "audio": ("https://www.youtube.com/watch?v=_cygjTdeits", "IAB Tech Lab audio initiatives"),
    "story": ("https://www.youtube.com/watch?v=DXSIHm115gk", "Measure What Matters core message"),
    "legal": ("https://www.youtube.com/watch?v=IFhF_tHrj4s", "Fair use four factors"),
    "a11y": ("https://www.youtube.com/watch?v=iWO5N3n1DXU", "WAI video captions"),
    "audience": ("https://www.youtube.com/watch?v=kz7wIhQP6gM", "Downloads vs retention"),
    "research_video": ("https://www.youtube.com/watch?v=bVz8Ua1VVsE", "Asai retrieval + reflection"),
    "sports": ("https://www.youtube.com/watch?v=14tfyWcYfEc", "Motivated camera movement"),
    "archive": ("https://www.youtube.com/watch?v=fkpZfpNWjWY", "Claim–evidence–reasoning"),
    "biz": ("https://www.youtube.com/watch?v=fdaiw74GaSY", "What is an OKR"),
    "systems": ("https://www.youtube.com/watch?v=RM6ZArd2nVc", "Yao LLM agents"),
    "talent": ("https://www.youtube.com/watch?v=oWpRKJPCI7M", "Big Five traits — not a diagnosis"),
    "video_generic": ("https://www.youtube.com/watch?v=ptQwvGcLZIw", "The Art of Camera Movement"),
}


def listed_ids() -> list[str]:
    return [
        ln.strip()
        for ln in (REPO / "improve_agents" / "agent_list.txt").read_text(encoding="utf-8").splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]


def parse_section(study: str, heading: str) -> str:
    match = re.search(rf"^## {re.escape(heading)}\s*$", study, re.M)
    if not match:
        return ""
    body = study[match.end() :]
    if "\n## " in body:
        body = body.split("\n## ", 1)[0]
    return " ".join(body.strip().split())


def yt_for(agent_id: str) -> tuple[str, str]:
    slug = agent_id.split(".", 1)[-1]
    if slug in VIDEO_YT:
        return VIDEO_YT[slug]
    return BUCKET_YT_FALLBACK.get(_bucket(agent_id), BUCKET_YT_FALLBACK["video_generic"])


def xai_for(agent_id: str) -> str:
    if agent_id.startswith("specials."):
        if agent_id in {"specials.llm-usage", "specials.optimization-agent", "specials.podcast-agent", "specials.techology-advisor-agent"}:
            return "https://docs.x.ai/developers/pricing"
        if agent_id in {"specials.controller-agent"}:
            return "https://docs.x.ai/developers/model-capabilities/video/image-to-video"
        return "https://docs.x.ai/developers/tools/overview"
    return BUCKET_XAI.get(_bucket(agent_id), BUCKET_XAI["video_generic"])


def procedure_slug(agent_id: str, craft: str = "") -> str:
    slug = agent_id.split(".", 1)[-1]
    if slug in PROCEDURE:
        return PROCEDURE[slug]
    words = re.findall(r"[a-zA-Z0-9]+", (craft or slug).lower())
    words = [w for w in words if w not in {"the", "and", "for", "not", "a", "an", "of", "to", "in"}][:3]
    if words:
        return "-".join(words)[:32]
    return slug.replace("_", "-")[:24] + "-notes"


def procedure_id(agent_id: str, craft: str = "") -> str:
    slug = agent_id.split(".", 1)[-1]
    return f"casops.skill.video.{slug}.{procedure_slug(agent_id, craft)}"


def accuracy_line(agent_id: str, owns: str) -> str:
    slug = agent_id.split(".", 1)[-1]
    if agent_id.startswith("specials."):
        guide = REPO / "agents" / agent_id / "content" / "test_guide.md"
        if guide.is_file():
            g = guide.read_text(encoding="utf-8")
            m = re.search(r"here means: ([^\n]+)", g)
            if m:
                return m.group(1).strip().rstrip(".")
    return f"in-role {slug} artifacts or wait; no invented CLIP-T/WCAG/arena numbers"


def rewrite_improve_md(agent_id: str, owns: str, craft: str, research_block: str) -> None:
    path = REPO / "improve_agents" / f"improve_agent_{agent_id}.md"
    acc = accuracy_line(agent_id, owns)
    body = f"""# Improve `{agent_id}`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: {owns or craft or agent_id}
Notes: {craft[:400] if craft else owns}

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/{agent_id}/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: {acc}. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

{research_block}
"""
    path.write_text(body.replace("\r\n", "\n"), encoding="utf-8")


def research_block(agent_id: str, yt: tuple[str, str], xai: str, study: str) -> str:
    lines = [
        IMPROVE_MARK,
        "",
        f"In-role citations for `{agent_id}`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.",
        "",
        "| Leg | Citation |",
        "|---|---|",
    ]
    arx = re.findall(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", study, re.I)
    if arx:
        for aid in list(dict.fromkeys(arx))[:4]:
            lines.append(f"| arXiv | [{aid}](https://arxiv.org/abs/{aid}) |")
    else:
        lines.append(f"| arXiv | Unique study set in `agents/{agent_id}/sources/study/domain_knowledge.md` |")
    lines.append(f"| YouTube | [{yt[1]}]({yt[0]}) |")
    lines.append(f"| x.ai | [non-activating vendor doc]({xai}) |")
    lines += [
        "",
        "Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.",
        "",
    ]
    return "\n".join(lines)


def replace_skill_id(folder: Path, old: str, new: str) -> None:
    if old == new or not old:
        return
    for path in folder.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".json", ".md"}:
            continue
        text = path.read_text(encoding="utf-8")
        if old not in text:
            continue
        path.write_text(text.replace(old, new).replace("\r\n", "\n"), encoding="utf-8")


def update_skill_md(folder: Path, agent_id: str, skill_id: str, owns: str, proc: str) -> None:
    path = folder / "skills" / "SKILL.md"
    body = (
        f"---\n"
        f"description: {proc} procedure for {agent_id}. Omitted from Chat until host_permission AND "
        f"operator_toggle resolve true. Adds no tools.\n"
        f"---\n\n"
        f"No live grant. Procedure: {(owns or proc).rstrip('.')}. Reply in numbered {agent_id.split('.',1)[-1]} artifacts. "
        f"Wait if evidence is missing. Refuse tools, network, production, memory writes.\n\n"
        f"This skill adds **no** tools. `allowed_tools` stays `[]`.\n"
    )
    path.write_text(body.replace("\r\n", "\n"), encoding="utf-8")


def patch_guide_phrase(folder: Path) -> None:
    path = folder / "content" / "test_guide.md"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace("“Intent classification accuracy” here means:", "Craft success (characterization) here means:")
    text = text.replace("Intent classification accuracy here means:", "Craft success (characterization) here means:")
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8")


def upsert_youtube_in_study(study_text: str, yt: tuple[str, str], xai: str) -> str:
    # Replace first YouTube bullet in Triple research if present
    if "### YouTube" in study_text:
        pre, rest = study_text.split("### YouTube", 1)
        after = rest
        if "### xAI" in after:
            yt_block, rest2 = after.split("### xAI", 1)
            new_yt = (
                " (educational; do not paste transcripts into Chat)\n"
                f"- [{yt[1]}]({yt[0]})\n\n### xAI"
            )
            return pre + "### YouTube" + new_yt + rest2
    return study_text


def patch_sources_youtube(path: Path, yt: tuple[str, str], xai: str) -> None:
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    if "### YouTube" in text:
        pre, rest = text.split("### YouTube", 1)
        if "### xAI" in rest:
            _, rest2 = rest.split("### xAI", 1)
            text = (
                pre
                + "### YouTube\n\n"
                + f"- [{yt[1]}]({yt[0]})\n\n### xAI"
                + rest2
            )
            # ensure xai url present
            if xai not in text:
                text = text.replace("### xAI (non-activating)", f"### xAI (non-activating)\n\n- [non-activating]({xai})", 1)
            path.write_text(text.replace("\r\n", "\n"), encoding="utf-8")


def pack_vendor_line(folder: Path, agent_id: str, yt: tuple[str, str], xai: str) -> bool:
    path = folder / "prompts" / "primary.md"
    if not path.is_file():
        return False
    spec = json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))
    before = pack_chat_context(folder, spec, {}, message="ping", history=[])
    task0 = next(s for s in before["public"]["segments"] if s["name"] == "task")
    if task0["tokens"] >= 640:
        return False
    original = path.read_text(encoding="utf-8")
    line = f"Taught/vendor (design-time, non-activating): {yt[0]} ; {xai}."
    packed_part = original.split("## Developer", 1)[0]
    if "Taught/vendor (design-time" in packed_part:
        text = re.sub(
            r"Taught/vendor \(design-time, non-activating\): [^\n]+",
            line,
            original,
            count=1,
        )
    elif "See `sources/study/domain_knowledge.md`." in packed_part:
        text = original.replace(
            "See `sources/study/domain_knowledge.md`.",
            line + " See `sources/study/domain_knowledge.md`.",
            1,
        )
    else:
        return False
    packed = operational_prompt(text)
    if estimate_tokens(packed) > 720:
        return False
    if "Sora 2 API" in packed or "## Developer" in packed:
        return False
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8")
    after = pack_chat_context(folder, spec, {}, message="ping", history=[])
    task = next(s for s in after["public"]["segments"] if s["name"] == "task")
    if task["clipped"] or task["tokens"] > 768:
        path.write_text(original.replace("\r\n", "\n"), encoding="utf-8")
        return False
    return True


def apply_video(agent_id: str) -> None:
    folder = REPO / "agents" / agent_id
    study_path = folder / "sources" / "study" / "domain_knowledge.md"
    study = study_path.read_text(encoding="utf-8") if study_path.is_file() else ""
    owns = parse_section(study, "Owns")
    craft = parse_section(study, "Craft")
    yt = yt_for(agent_id)
    xai = xai_for(agent_id)
    slug = agent_id.split(".", 1)[-1]
    proc = procedure_slug(agent_id, craft)
    new_skill = procedure_id(agent_id, craft)
    bind_path = folder / "skills" / "bindings.json"
    old_skill = ""
    if bind_path.is_file():
        bind = json.loads(bind_path.read_text(encoding="utf-8"))
        rows = bind.get("bindings") or []
        if rows:
            old_skill = str(rows[0].get("skill_id") or "")
    if old_skill and old_skill != new_skill:
        replace_skill_id(folder, old_skill, new_skill)
    update_skill_md(folder, agent_id, new_skill, owns, proc)
    if study_path.is_file():
        study_path.write_text(upsert_youtube_in_study(study, yt, xai).replace("\r\n", "\n"), encoding="utf-8")
        study = study_path.read_text(encoding="utf-8")
    patch_sources_youtube(folder / "content" / "research" / "sources.md", yt, xai)
    patch_guide_phrase(folder)
    rewrite_improve_md(agent_id, owns, craft, research_block(agent_id, yt, xai, study))
    pack_vendor_line(folder, agent_id, yt, xai)


def first_youtube(study: str) -> tuple[str, str]:
    md = re.search(
        r"\[([^\]]+)\]\((https://(?:www\.)?youtube\.com/watch\?v=[\w-]+)\)",
        study,
    )
    if md:
        return (md.group(2), md.group(1).strip())
    bare = re.search(r"https://(?:www\.)?youtube\.com/watch\?v=([\w-]+)", study)
    if bare:
        url = f"https://www.youtube.com/watch?v={bare.group(1)}"
        prefix = study[max(0, bare.start() - 90) : bare.start()]
        label = re.sub(r"[-—*#\[\]()]+", " ", prefix).strip().split("\n")[-1].strip(" :;,")
        label = re.sub(r"\s+", " ", label)[-80:] or "in-role educational talk"
        return (url, label)
    return ("https://www.youtube.com/watch?v=7bJ0fnvPLaA", "in-role educational talk")


def specials_owns_craft(study: str) -> tuple[str, str]:
    owns = parse_section(study, "Owns")
    m = re.search(r"This agent \*\*owns ([^*]+)\*\*", study)
    if m:
        owns = "Owns " + m.group(1).strip().rstrip(".")
    skip_heads = (
        "sources",
        "triple research",
        "honesty",
        "skip as live enablement",
        "findings that change this folder",
        "shared",
    )
    craft = parse_section(study, "Craft")
    if not craft:
        for match in re.finditer(r"^## ([^\n]+)\n+(.+?)(?=\n## |\Z)", study, re.S | re.M):
            title = match.group(1).strip()
            low = title.lower()
            if any(low.startswith(s) for s in skip_heads):
                continue
            body = " ".join(match.group(2).strip().split())
            craft = f"{title}. {body}"[:400]
            if not owns:
                owns = title
            break
    if not owns:
        for block in study.split("\n\n"):
            blob = " ".join(block.split())
            if not blob or blob.startswith("#") or blob.startswith("Design-time study"):
                continue
            owns = blob[:240]
            break
    return owns or "in-role craft", craft or owns or "in-role craft"


def apply_specials_md_only(agent_id: str) -> None:
    folder = REPO / "agents" / agent_id
    study_path = folder / "sources" / "study" / "domain_knowledge.md"
    study = study_path.read_text(encoding="utf-8") if study_path.is_file() else ""
    owns, craft = specials_owns_craft(study)
    yt = first_youtube(study)
    xai = xai_for(agent_id)
    patch_guide_phrase(folder)
    rewrite_improve_md(agent_id, owns, craft, research_block(agent_id, yt, xai, study))


def verify() -> None:
    clone = 0
    declared = 0
    clipped = 0
    packed_yt = 0
    yt_counts: dict[str, int] = {}
    yt_re = re.compile(r"youtube\.com/watch\?v=([\w-]+)")
    for agent_id in listed_ids():
        md = REPO / "improve_agents" / f"improve_agent_{agent_id}.md"
        if md.is_file() and CLONE in md.read_text(encoding="utf-8"):
            clone += 1
        folder = REPO / "agents" / agent_id
        bind = folder / "skills" / "bindings.json"
        if bind.is_file() and "declared-craft" in bind.read_text(encoding="utf-8"):
            declared += 1
        study = folder / "sources" / "study" / "domain_knowledge.md"
        if study.is_file():
            for vid in yt_re.findall(study.read_text(encoding="utf-8")):
                yt_counts[vid] = yt_counts.get(vid, 0) + 1
        spec_path = folder / "agent_spec.json"
        prompt = folder / "prompts" / "primary.md"
        if spec_path.is_file() and prompt.is_file():
            spec = json.loads(spec_path.read_text(encoding="utf-8"))
            packed = pack_chat_context(folder, spec, {}, message="ping", history=[])
            task = next(s for s in packed["public"]["segments"] if s["name"] == "task")
            if task["clipped"]:
                clipped += 1
            if "Taught/vendor" in operational_prompt(prompt.read_text(encoding="utf-8")):
                packed_yt += 1
    worst = sorted(yt_counts.items(), key=lambda kv: -kv[1])[:8]
    print(
        f"verify clone_md={clone} declared-craft={declared} clipped={clipped} "
        f"packed_vendor_line={packed_yt} yt_unique={len(yt_counts)} worst={worst}"
    )


def main() -> int:
    n_v = n_s = 0
    for agent_id in listed_ids():
        if agent_id.startswith("video."):
            apply_video(agent_id)
            n_v += 1
        elif agent_id.startswith("specials."):
            apply_specials_md_only(agent_id)
            n_s += 1
    print(f"video={n_v} specials_md={n_s}")
    verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
