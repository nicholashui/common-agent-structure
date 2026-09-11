#!/usr/bin/env python3
"""Land verified arXiv + YouTube + x.ai citations on listed agents missing any leg.

Citations are design-time only. Does not enable tools, network, or production.
Does not rewrite unique video source blocks (keeps unique-papers test).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "tools"))

from casops.runtime.chat import estimate_tokens, operational_prompt  # noqa: E402
from complex_agent_testcases import _bucket  # noqa: E402

MARKER = "## Triple research (design-time, 2026-09)"
IMPROVE_MARK = "## Research landed (verified, 2026-09)"

# Remaining specials: verified on 2026-09-11. Not clones of intent-analysis.
SPECIALS: dict[str, dict[str, list[tuple[str, str]]]] = {
    "specials.autotelic-agent": {
        "arxiv": [
            ("2012.09830", "Colas et al., Autotelic Agents / IMGEP (already in study)"),
        ],
        "youtube": [
            ("https://www.youtube.com/watch?v=7bJ0fnvPLaA", "Oudeyer, Developmental Machine Learning, ICLR 2019 keynote (IMGEP)"),
            ("https://www.youtube.com/watch?v=Jx6-DKXgAKU", "Oudeyer, MIT Embodied Intelligence seminar (curiosity / IMGEP)"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/tools/overview", "Tools overview — naming tools is not a live-training grant"),
        ],
    },
    "specials.complex-problem-solution-process-model": {
        "arxiv": [
            ("2204.10358", "Gizzi et al., Creative Problem Solving in AI agents — survey and framework"),
            ("2505.00018", "Wu & Or, open complex Human–AI collaboration for problem solving"),
        ],
        "youtube": [
            ("https://www.youtube.com/watch?v=ogtpxA6brGo", "The Cynefin Company, The Cynefin Framework (official)"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/tools/overview", "Non-activating: Cynefin diagnosis does not call tools"),
        ],
    },
    "specials.controller-agent": {
        "arxiv": [
            ("2506.17450", "BlenderFusion (already in study)"),
            ("2406.10126", "CamTrol (already in study)"),
        ],
        "youtube": [
            ("https://www.youtube.com/watch?v=KupEY5CAwe4", "Camera Movements for Beginners — pan/tilt/dolly vs text-only prompts"),
            ("https://www.youtube.com/watch?v=ptQwvGcLZIw", "The Art of Camera Movement (House of Tabula)"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/model-capabilities/video/image-to-video", "Imagine image-to-video — design-time; not enabled here"),
            ("https://x.ai/docs/guides/image-generations", "Imagine overview (image/video) — vendor names are not allow-lists"),
        ],
    },
    "specials.knowledge-router-agent": {
        "arxiv": [
            ("2005.11401", "Lewis RAG (already in study)"),
            ("2310.11511", "Self-RAG (already in study)"),
        ],
        "youtube": [
            ("https://www.youtube.com/watch?v=bVz8Ua1VVsE", "Akari Asai, Self-reflective LMs with retrieval (UMass ML lunch)"),
        ],
        "xai": [
            ("https://x.ai/docs/developers/quickstart", "Files & Collections mentioned as RAG pipelines — this host has no live index"),
            ("https://docs.x.ai/developers/tools/overview", "Collections/Web Search are vendor tools; allowed_tools stays empty"),
        ],
    },
    "specials.llm-usage": {
        "arxiv": [
            ("2606.24616", "Zhu, AI Tokenomics — tokens as the accounting unit (names xAI among billers)"),
            ("2605.30040", "Hoque et al., Token Inflation — per-token bills are hard to audit"),
            ("2504.13359", "Cost-of-Pass — expected cost of a correct solution, not request counts"),
        ],
        "youtube": [
            ("https://www.youtube.com/watch?v=zduSFxRajkE", "Karpathy, Let's build the GPT Tokenizer — meter tokens, not 'API calls'"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/pricing", "Dated xAI token / Imagine / Voice / tools prices — stale unless dated; do not store keys"),
        ],
    },
    "specials.optimization-agent": {
        "arxiv": [
            ("2503.12434", "Survey on optimization of LLM-based agents"),
            ("2605.27630", "OptiLoop — verify constraints in the loop; missing contract is not a convex program"),
            ("2605.27375", "LCO — LLM constraint optimization; missing safety constraints"),
        ],
        "youtube": [
            ("https://www.youtube.com/watch?v=bO3GpAjVvD8", "EPM, PDCA Cycle Explained (Deming / Shewhart)"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/pricing", "Cost is a constraint, not a live dashboard"),
        ],
    },
    "specials.planner-agent": {
        "arxiv": [
            ("2210.03629", "Yao et al., ReAct — execution loops, not this planner's job (already in study)"),
        ],
        "youtube": [
            ("https://www.youtube.com/watch?v=RM6ZArd2nVc", "Yao, LLM Agents history & overview (UC Berkeley CS294-196) — ReAct is execution"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/tools/overview", "Planner emits file+acceptance; it does not spawn tools"),
        ],
    },
    "specials.podcast-agent": {
        "arxiv": [
            ("2106.06605", "Modeling language usage and listener engagement in podcasts — stream rate ≠ download count"),
            ("2411.07892", "Structured Podcast Research Corpus — RSS ecosystem, not a live fetcher here"),
            ("2412.05516", "Pandora audio-ad load field experiment — listening hours ≠ IAB downloads"),
        ],
        "youtube": [
            ("https://www.youtube.com/watch?v=_cygjTdeits", "IAB Tech Lab Audio Initiatives — podcast measurement working group (downloads vs listeners)"),
            ("https://www.youtube.com/watch?v=kz7wIhQP6gM", "Podcast Stats Explained (downloads vs retention)"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/pricing", "Voice/TTS prices are vendor; this pack has no RSS fetcher"),
        ],
    },
    "specials.psychological-profile-agent": {
        "arxiv": [
            ("2510.14203", "Joint modeling of Big Five and HEXACO for apparent personality"),
            ("2511.23101", "Mind Reading or Misreading? LLMs on the Big Five — not a diagnosis"),
            ("2607.02325", "Personality Without Persons? Psychometric critique of Big Five testing in LLMs"),
        ],
        "youtube": [
            ("https://www.youtube.com/watch?v=oWpRKJPCI7M", "Seeker, The Big 5 Personality Traits (Costa & McCrae)"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/tools/overview", "No patient record, no memory writes of inferred personality"),
        ],
    },
    "specials.psychological-recommendation-agent": {
        "arxiv": [
            ("2101.12153", "Survey on personality-aware recommendation systems"),
            ("2106.03060", "Big-Five vs HEXACO vs MBTI for personality-aware recs; cold start"),
            ("2501.01945", "Cold-start recommendation in the LLM era — no fake history"),
        ],
        "youtube": [
            ("https://www.youtube.com/watch?v=D33VOyGGib8", "Trait theories lecture (Eysenck, Costa, McCrae, Cattell) — traits as rec side-features"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/tools/overview", "No live catalog, no tracking pixels"),
        ],
    },
    "specials.research-agent": {
        "arxiv": [
            ("2508.12752", "Deep Research survey — planning/retrieval/synthesis; this host does not fetch the web"),
            ("2609.01432", "Citing Less Critically — LLMs reshape citation rhetoric; do not invent arXiv IDs"),
            ("2605.07723", "LLM hallucinations in the wild — non-existent citations"),
        ],
        "youtube": [
            ("https://www.youtube.com/watch?v=fkpZfpNWjWY", "Claim–Evidence–Reasoning (Booth-style argument spine)"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/tools/overview", "Web Search exists at xAI; CASOPS Chat does not enable it"),
        ],
    },
    "specials.screenwriter-strategic-goal-achievement-agent": {
        "arxiv": [
            ("2311.16542", "Agents meet OKR — hierarchical objects and key results; do not write the screenplay"),
            ("1708.09040", "Modelling protagonist goals and desires — want vs need as KR inputs"),
            ("2107.13189", "Goal-Oriented Script Construction — steps to a goal, not the finished script"),
        ],
        "youtube": [
            ("https://www.youtube.com/watch?v=pMlBMBTtJEw", "John Doerr, Intel Operation Crush OKR example — KRs must be yes/no"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/tools/overview", "No video.screenwriter tool grant"),
        ],
    },
    "specials.strategic-goal-achievement-agent": {
        "arxiv": [
            ("2311.16542", "Agents meet OKR — Objective + Key Results; do not execute the plan"),
            ("2311.00236", "OKRs in software teams — measuring progress is hard work"),
            ("2511.08242", "Outcome-oriented agent metrics — Goal Completion Rate is not Chat 200"),
        ],
        "youtube": [
            ("https://www.youtube.com/watch?v=MV4UViKjJ34", "John Doerr, OKRs Explained (Measure What Matters)"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/tools/overview", "Advice is not a live OKR dashboard"),
        ],
    },
    "specials.techology-advisor-agent": {
        "arxiv": [
            ("2510.02453", "How to Train Your Advisor — steering black-box LLMs; vendor names are not enabled APIs"),
            ("2609.05385", "Necessary or Sufficient? Evaluating LLM explanations with behavioural evidence"),
        ],
        "youtube": [
            ("https://www.youtube.com/watch?v=zduSFxRajkE", "Karpathy tokenizer lecture — dated vendor internals vs 'latest model' memory"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/pricing", "Prefer dated xAI pricing/docs over undated 'latest model'"),
            ("https://x.ai/docs/developers/quickstart", "Quickstart is not a live key or MCP grant"),
        ],
    },
    "specials.agent-loop-creator": {
        "arxiv": [("2210.03629", "ReAct (already in study)")],
        "youtube": [
            ("https://www.youtube.com/watch?v=RM6ZArd2nVc", "Yao, LLM Agents / ReAct (Berkeley LLM Agents MOOC)"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/tools/overview", "Loop design is not a tool grant (already noted)"),
        ],
    },
    "specials.agentic-rag-agent": {
        "arxiv": [("2310.11511", "Self-RAG (already in study)")],
        "youtube": [
            ("https://www.youtube.com/watch?v=bVz8Ua1VVsE", "Akari Asai, Self-reflective LMs with retrieval"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/tools/overview", "Already cited; still non-activating"),
        ],
    },
}

# Video packs already have unique arXiv/book sets. Add taught + vendor legs by craft bucket.
VIDEO_BUCKET: dict[str, dict[str, list[tuple[str, str]]]] = {
    "camera": {
        "youtube": [
            ("https://www.youtube.com/watch?v=KupEY5CAwe4", "Camera Movements for Beginners"),
            ("https://www.youtube.com/watch?v=ptQwvGcLZIw", "The Art of Camera Movement"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/model-capabilities/video/image-to-video", "Imagine image-to-video — not enabled"),
            ("https://x.ai/docs/guides/image-generations", "Imagine overview — vendor name is not an allow-list"),
        ],
    },
    "edit": {
        "youtube": [
            ("https://www.youtube.com/watch?v=9-6-7bCBlLU", "Walter Murch, Rule of Six (Web of Stories)"),
            ("https://www.youtube.com/watch?v=PKYeClvvlTw", "StudioBinder, In the Blink of an Eye / Rule of Six"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/model-capabilities/video/image-to-video", "Imagine video is generation, not an edit DAG"),
        ],
    },
    "picture": {
        "youtube": [
            ("https://www.youtube.com/watch?v=wfns4DuEB5M", "Think like a Cinematographer: Camera Movement"),
            ("https://www.youtube.com/watch?v=s8VMCbEioFM", "Adding camera movement to cinematography"),
        ],
        "xai": [
            ("https://x.ai/docs/guides/image-generations", "Imagine image/video — design-time only"),
        ],
    },
    "audio": {
        "youtube": [
            ("https://www.youtube.com/watch?v=_cygjTdeits", "IAB Tech Lab audio / podcast measurement initiatives"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/pricing", "Voice / TTS / STT prices — not a live mixer"),
        ],
    },
    "story": {
        "youtube": [
            ("https://www.youtube.com/watch?v=DXSIHm115gk", "Measure What Matters core message — goals vs fuzzy 'more cinematic'"),
        ],
        "xai": [
            ("https://x.ai/docs/developers/quickstart", "Text generation quickstart — this pack does not write via Imagine"),
        ],
    },
    "legal": {
        "youtube": [
            ("https://www.youtube.com/watch?v=IFhF_tHrj4s", "Fair Use four factors (educational)"),
            ("https://www.youtube.com/watch?v=ruV2qn7xyU0", "Educational uses and fair use"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/tools/overview", "Vendor docs are not a bar card; no live generation"),
        ],
    },
    "a11y": {
        "youtube": [
            ("https://www.youtube.com/watch?v=iWO5N3n1DXU", "W3C WAI Perspectives: Video Captions"),
            ("https://www.youtube.com/watch?v=-LILWDvEuxw", "Checking YouTube captions for accuracy (WCAG)"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/tools/overview", "Captions/AD requirements are WCAG, not Imagine"),
        ],
    },
    "audience": {
        "youtube": [
            ("https://www.youtube.com/watch?v=kz7wIhQP6gM", "Podcast/audience stats: downloads vs retention"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/pricing", "Vendor RPM is not a host SLO or CLIP-T"),
        ],
    },
    "research_video": {
        "youtube": [
            ("https://www.youtube.com/watch?v=bVz8Ua1VVsE", "Asai, retrieval + self-reflection (cite, don't invent)"),
        ],
        "xai": [
            ("https://x.ai/docs/developers/quickstart", "Files & Collections / web search — not enabled"),
            ("https://docs.x.ai/developers/tools/overview", "Web Search is a Grok API tool, not this pack"),
        ],
    },
    "sports": {
        "youtube": [
            ("https://www.youtube.com/watch?v=14tfyWcYfEc", "Motivated vs unmotivated camera movement (storytelling purpose)"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/model-capabilities/video/image-to-video", "Imagine is not a live sports feed"),
        ],
    },
    "archive": {
        "youtube": [
            ("https://www.youtube.com/watch?v=fkpZfpNWjWY", "Claim–evidence–reasoning — archive notes need sources"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/tools/overview", "No live archive crawl"),
        ],
    },
    "biz": {
        "youtube": [
            ("https://www.youtube.com/watch?v=MV4UViKjJ34", "John Doerr, OKRs Explained"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/pricing", "Dated vendor prices; not a ROAS oracle"),
        ],
    },
    "systems": {
        "youtube": [
            ("https://www.youtube.com/watch?v=RM6ZArd2nVc", "Yao, LLM agents / ReAct overview"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/tools/overview", "Function calling is xAI, not CASOPS Chat"),
        ],
    },
    "talent": {
        "youtube": [
            ("https://www.youtube.com/watch?v=oWpRKJPCI7M", "Big Five traits — not a casting diagnosis"),
        ],
        "xai": [
            ("https://x.ai/docs/guides/image-generations", "Imagine likeness risks; no live generation"),
        ],
    },
    "video_generic": {
        "youtube": [
            ("https://www.youtube.com/watch?v=ptQwvGcLZIw", "The Art of Camera Movement — craft, not CLIP-T"),
        ],
        "xai": [
            ("https://docs.x.ai/developers/tools/overview", "xAI tools overview — non-activating"),
        ],
    },
}


def listed_ids() -> list[str]:
    return [
        ln.strip()
        for ln in (REPO / "improve_agents" / "agent_list.txt").read_text(encoding="utf-8").splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]


def triple_for(agent_id: str) -> dict[str, list[tuple[str, str]]]:
    if agent_id in SPECIALS:
        return SPECIALS[agent_id]
    bucket = _bucket(agent_id)
    row = VIDEO_BUCKET.get(bucket) or VIDEO_BUCKET["video_generic"]
    return {"arxiv": [], "youtube": row["youtube"], "xai": row["xai"]}


def render_study_block(agent_id: str, spec: dict[str, list[tuple[str, str]]]) -> str:
    lines = [
        MARKER,
        "",
        "Design-time citations collected to complete the arXiv + YouTube + x.ai triple. "
        "**Not** live grants. `allowed_tools` stays `[]`. Network, plugins, T3, memory writes, and production stay off.",
        "",
        "### arXiv",
    ]
    if spec.get("arxiv"):
        for aid, title in spec["arxiv"]:
            lines.append(f"- [{aid}](https://arxiv.org/abs/{aid}) — {title}")
    else:
        lines.append("- Unique arXiv/book set remains in `## Sources (unique to this agent)` above. Do not duplicate Bordwell/CLIP-T off-role.")
    lines += ["", "### YouTube (educational; do not paste transcripts into Chat)"]
    for url, title in spec.get("youtube") or []:
        lines.append(f"- [{title}]({url})")
    lines += ["", "### xAI (non-activating vendor docs)"]
    for url, title in spec.get("xai") or []:
        lines.append(f"- [{title}]({url})")
    lines.append("")
    return "\n".join(lines) + "\n"


def upsert_marked(text: str, marker: str, block: str) -> str:
    if marker in text:
        pre, rest = text.split(marker, 1)
        # drop old marked tail if it runs to EOF or next top-level that we don't use
        return pre.rstrip() + "\n\n" + block
    return text.rstrip() + "\n\n" + block


def patch_sources_md(path: Path, spec: dict[str, list[tuple[str, str]]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = path.read_text(encoding="utf-8") if path.is_file() else "# Research map\n"
    extra = ["", "## arXiv / YouTube / xAI (verified 2026-09)", ""]
    if spec.get("arxiv"):
        extra.append("### arXiv")
        extra.append("")
        extra.append("| ID | Why here |")
        extra.append("|---|---|")
        for aid, title in spec["arxiv"]:
            extra.append(f"| [{aid}](https://arxiv.org/abs/{aid}) | {title} |")
        extra.append("")
    extra.append("### YouTube")
    extra.append("")
    for url, title in spec.get("youtube") or []:
        extra.append(f"- [{title}]({url})")
    extra.append("")
    extra.append("### xAI (non-activating)")
    extra.append("")
    for url, title in spec.get("xai") or []:
        extra.append(f"- [{title}]({url})")
    extra.append("")
    extra.append("Do not enable tools/network from these citations.")
    extra.append("")
    blob = "\n".join(extra)
    if "YouTube (verified 2026-09)" in existing or "## arXiv / YouTube / xAI (verified 2026-09)" in existing:
        pre = existing.split("## arXiv / YouTube / xAI (verified 2026-09)", 1)[0].rstrip()
        path.write_text(pre + blob, encoding="utf-8")
    else:
        path.write_text(existing.rstrip() + blob, encoding="utf-8")


def patch_improve_md(agent_id: str, spec: dict[str, list[tuple[str, str]]]) -> None:
    path = REPO / "improve_agents" / f"improve_agent_{agent_id}.md"
    if not path.is_file():
        return
    lines = [
        "",
        IMPROVE_MARK,
        "",
        f"In-role citations for `{agent_id}`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.",
        "",
        "| Leg | Citation |",
        "|---|---|",
    ]
    if spec.get("arxiv"):
        for aid, title in spec["arxiv"]:
            lines.append(f"| arXiv | [{aid}](https://arxiv.org/abs/{aid}) — {title} |")
    else:
        lines.append("| arXiv | Unique study set already in `agents/" + agent_id + "/sources/study/domain_knowledge.md` |")
    for url, title in spec.get("youtube") or []:
        lines.append(f"| YouTube | [{title}]({url}) |")
    for url, title in spec.get("xai") or []:
        lines.append(f"| x.ai | [{title}]({url}) |")
    lines += [
        "",
        "Apply these into `content/research/sources.md` and `sources/study/domain_knowledge.md`. Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.",
        "",
    ]
    block = "\n".join(lines)
    text = path.read_text(encoding="utf-8")
    if IMPROVE_MARK in text:
        text = text.split(IMPROVE_MARK, 1)[0].rstrip() + "\n" + block
    else:
        text = text.rstrip() + "\n" + block
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8")


def maybe_pack_line(folder: Path, agent_id: str, spec: dict[str, list[tuple[str, str]]]) -> None:
    """Add one compact triple line to packed Domain knowledge for specials with budget."""
    if not agent_id.startswith("specials."):
        return
    path = folder / "prompts" / "primary.md"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    if "YouTube:" in text.split("## Developer", 1)[0] and "docs.x.ai" in text.split("## Developer", 1)[0]:
        return
    yt = (spec.get("youtube") or [("https://www.youtube.com/watch?v=7bJ0fnvPLaA", "")])[0][0]
    xai = (spec.get("xai") or [("https://docs.x.ai/developers/tools/overview", "")])[0][0]
    arx = spec.get("arxiv") or []
    arx_s = arx[0][0] if arx else "see study"
    line = (
        f"Triple (design-time, non-activating): arXiv {arx_s}; YouTube {yt}; xAI {xai}. "
        "Do not paste transcripts. Do not enable tools."
    )
    if "### Domain knowledge (research)" not in text:
        return
    updated = text.replace(
        "See `sources/study/domain_knowledge.md`.",
        f"{line} See `sources/study/domain_knowledge.md`.",
        1,
    )
    if updated == text:
        updated = text.replace(
            "### Domain knowledge (research)",
            "### Domain knowledge (research)\n" + line + "\n",
            1,
        )
    packed = operational_prompt(updated)
    if estimate_tokens(packed) > 740:
        return
    if "Sora 2 API" in packed or "## Developer" in packed:
        return
    path.write_text(updated.replace("\r\n", "\n"), encoding="utf-8")


def apply_one(agent_id: str) -> str:
    folder = REPO / "agents" / agent_id
    study = folder / "sources" / "study" / "domain_knowledge.md"
    spec = triple_for(agent_id)
    if study.is_file():
        text = study.read_text(encoding="utf-8")
        text = upsert_marked(text, MARKER, render_study_block(agent_id, spec))
        study.write_text(text.replace("\r\n", "\n"), encoding="utf-8")
    patch_sources_md(folder / "content" / "research" / "sources.md", spec)
    patch_improve_md(agent_id, spec)
    maybe_pack_line(folder, agent_id, spec)
    return agent_id


def main() -> int:
    skip_full = {
        "specials.intent-analysis-agent",
        "specials.aesthetics-agent",
        "specials.general-creative-agent",
    }
    done = []
    for agent_id in listed_ids():
        if agent_id in skip_full:
            # still ensure improve md notes existing triple if missing marker
            folder = REPO / "agents" / agent_id
            blob = ""
            for rel in ("content/research/sources.md", "sources/study/domain_knowledge.md"):
                p = folder / rel
                if p.is_file():
                    blob += p.read_text(encoding="utf-8")
            if "youtube.com/watch" in blob and ("docs.x.ai" in blob or "x.ai/" in blob) and re.search(r"arxiv", blob, re.I):
                continue
        apply_one(agent_id)
        done.append(agent_id)
    print(f"updated={len(done)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
