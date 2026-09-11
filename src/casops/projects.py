"""Draft video projects under repo `project/<slug>/`. Companion, not a live grant."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from casops.compose.io import folder_io
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

SLUG_RE = re.compile(r"^[a-z][a-z0-9-]{0,46}[a-z0-9]$|^[a-z]$")
VIDEO_IDS = re.compile(r"video\.(?:template|scale)\.[a-j0-9s]+", re.I)
AGENT_IDS = re.compile(r"video\.[a-z0-9_]+", re.I)

# First agents in each video template/scale (Greenlight). One project = one workflow.
FIRST_AGENTS: dict[str, tuple[str, ...]] = {
    "video.template.a": ("video.planner", "video.producer", "video.finance", "video.compliance"),
    "video.template.b": ("video.performancemarketer", "video.producer", "video.finance", "video.brand"),
    "video.template.c": ("video.instructionaldesign", "video.producer", "video.sme", "video.brand"),
    "video.template.d": ("video.producer", "video.personalizationengineer", "video.compliance", "video.trustsafety"),
    "video.template.e": ("video.producer", "video.director", "video.finance", "video.legal"),
    "video.template.f": ("video.instructionaldesign", "video.producer", "video.sme", "video.compliance"),
    "video.template.g": ("video.musicvideodirector", "video.producer", "video.labela_r", "video.legal"),
    "video.template.h": ("video.producer", "video.brandstrategist", "video.compliance", "video.legal"),
    "video.template.i": ("video.producer", "video.finance", "video.legal", "video.ethics", "video.planner"),
    "video.template.j": ("video.screenwriter", "video.producer", "video.director", "video.legal", "video.ethics", "video.finance"),
    "video.scale.s1": ("video.planner", "video.producer", "video.finance", "video.compliance"),
    "video.scale.s2": ("video.planner", "video.producer", "video.finance", "video.compliance"),
    "video.scale.s3": ("video.showrunner", "video.planner", "video.producer", "video.memory", "video.compliance"),
    "video.scale.s4": ("video.producer", "video.finance", "video.legal", "video.musicvideodirector", "video.showrunner"),
    "video.scale.s5": ("video.planner", "video.producer", "video.finance", "video.orchestrator", "video.legal"),
    "video.scale.s6": ("video.planner", "video.producer", "video.finance", "video.legal", "video.ethics"),
    "video.scale.s7": ("video.screenwriter", "video.producer", "video.director", "video.legal", "video.ethics", "video.finance"),
}

CATALOG: tuple[dict[str, str], ...] = (
    {"id": "video.template.a", "kind": "template", "code": "A", "label": "Viral Hook", "use": "short social spike, meme, CTA"},
    {"id": "video.template.b", "kind": "template", "code": "B", "label": "UGC Ad", "use": "paid social, creator-style product ad"},
    {"id": "video.template.c", "kind": "template", "code": "C", "label": "Animated Explainer", "use": "how-to, product explainer"},
    {"id": "video.template.d", "kind": "template", "code": "D", "label": "Personalized Birthday", "use": "personal greeting, short gift clip"},
    {"id": "video.template.e", "kind": "template", "code": "E", "label": "AI Short Film", "use": "narrative short, cinematic sketch"},
    {"id": "video.template.f", "kind": "template", "code": "F", "label": "Corporate Training", "use": "internal training, safety recap"},
    {"id": "video.template.g", "kind": "template", "code": "G", "label": "Music Video", "use": "performance, beat-led picture"},
    {"id": "video.template.h", "kind": "template", "code": "H", "label": "AI Avatar", "use": "presenter, talking-head, avatar"},
    {"id": "video.template.i", "kind": "template", "code": "I", "label": "Documentary", "use": "interview, archive, long-form report"},
    {"id": "video.template.j", "kind": "template", "code": "J", "label": "Feature Film", "use": "feature-length, high-risk production"},
    {"id": "video.scale.s1", "kind": "scale", "code": "S1", "label": "Scale S1", "use": "one outlet, fast, low risk"},
    {"id": "video.scale.s2", "kind": "scale", "code": "S2", "label": "Scale S2", "use": "two outlets, light brand gate"},
    {"id": "video.scale.s3", "kind": "scale", "code": "S3", "label": "Scale S3", "use": "variant campaign, mid depth"},
    {"id": "video.scale.s4", "kind": "scale", "code": "S4", "label": "Scale S4", "use": "multi-phase, review-heavy"},
    {"id": "video.scale.s5", "kind": "scale", "code": "S5", "label": "Scale S5", "use": "premium short / training series"},
    {"id": "video.scale.s6", "kind": "scale", "code": "S6", "label": "Scale S6", "use": "long-form documentary depth"},
    {"id": "video.scale.s7", "kind": "scale", "code": "S7", "label": "Scale S7", "use": "feature / broadcast, highest risk"},
)

CATALOG_BY_ID = {row["id"]: row for row in CATALOG}


def projects_root_for(agents_root: Path, override: Path | None = None) -> Path:
    if override is not None:
        return override.resolve()
    return (Path(agents_root).resolve().parent / "project").resolve()


def normalize_slug(name: str) -> str:
    original = name or ""
    if ".." in original or "/" in original.replace("\\", "/") or "\\" in original:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="invalid project name")
    raw = original.strip().lower().replace("_", "-")
    raw = re.sub(r"[^a-z0-9-]+", "-", raw)
    raw = re.sub(r"-{2,}", "-", raw).strip("-")
    if not raw or not SLUG_RE.match(raw):
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="invalid project name")
    return raw


def _safe_dir(root: Path, slug: str) -> Path:
    folder = (root / slug).resolve()
    try:
        folder.relative_to(root.resolve())
    except ValueError as exc:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="project path escapes root") from exc
    return folder


def catalog_public() -> list[dict[str, str]]:
    return [dict(row) for row in CATALOG]


def heuristic_rank(brief: dict[str, Any]) -> list[dict[str, Any]]:
    text = " ".join(
        str(brief.get(key) or "")
        for key in ("title", "brief", "audience", "notes", "duration", "outlets", "risk")
    ).lower()
    duration = str(brief.get("duration") or "").lower()
    outlets = str(brief.get("outlets") or "").lower()
    risk = str(brief.get("risk") or "low").lower()

    template = "video.template.a"
    if any(token in text for token in ("ugc", "paid social", "roas", "product ad", "unboxing")):
        template = "video.template.b"
    elif any(token in text for token in ("explainer", "how-to", "howto", "animated")):
        template = "video.template.c"
    elif any(token in text for token in ("birthday", "greeting", "personal gift")):
        template = "video.template.d"
    elif any(token in text for token in ("short film", "narrative", "cinematic")):
        template = "video.template.e"
    elif any(token in text for token in ("training", "safety recap", "corporate", "lms")):
        template = "video.template.f"
    elif any(token in text for token in ("music video", "song", "beat")):
        template = "video.template.g"
    elif any(token in text for token in ("avatar", "talking head", "presenter", "spokesperson")):
        template = "video.template.h"
    elif any(token in text for token in ("documentary", "interview", "archive")):
        template = "video.template.i"
    elif any(token in text for token in ("feature", "theatrical", "broadcast film")):
        template = "video.template.j"

    scale = "video.scale.s1"
    if "10min" in duration or "feature" in duration or risk == "high" or "broadcast" in outlets:
        scale = "video.scale.s6" if template != "video.template.j" else "video.scale.s7"
    elif "3min" in duration or "6min" in duration or risk == "medium" or "web" in outlets:
        scale = "video.scale.s3"
    elif "60s" in duration or "60 s" in duration:
        scale = "video.scale.s2"

    ranked_ids = [template, scale]
    extras = [row["id"] for row in CATALOG if row["id"] not in ranked_ids]
    ordered = ranked_ids + extras
    out: list[dict[str, Any]] = []
    for index, item_id in enumerate(ordered[:5]):
        row = CATALOG_BY_ID[item_id]
        out.append(
            {
                "id": item_id,
                "label": f"{row['code']} · {row['label']}",
                "kind": row["kind"],
                "reason": row["use"],
                "rank": index + 1,
                "source": "heuristic",
            }
        )
    return out


def first_agents(template_id: str) -> list[str]:
    key = (template_id or "video.template.a").lower()
    return list(FIRST_AGENTS.get(key) or FIRST_AGENTS["video.template.a"])


def video_io_index(agents_root: Path) -> dict[str, dict[str, Any]]:
    root = Path(agents_root)
    out: dict[str, dict[str, Any]] = {}
    if not root.is_dir():
        return out
    for folder in root.iterdir():
        if not folder.is_dir() or not folder.name.startswith("video."):
            continue
        spec_path = folder / "agent_spec.json"
        if not spec_path.is_file():
            continue
        try:
            spec = json.loads(spec_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(spec, dict):
            continue
        snapshot = folder_io(folder, spec=spec)
        out[folder.name] = {
            "id": folder.name,
            "role": str(snapshot.get("role") or folder.name),
            "inputs": list(snapshot.get("inputs") or []),
            "outputs": list(snapshot.get("outputs") or []),
        }
    return out


def parse_agent_ids(text: str, known: set[str] | None = None) -> list[str]:
    found: list[str] = []
    allow = known
    for match in AGENT_IDS.findall(text or ""):
        key = match.lower()
        if key in CATALOG_BY_ID:
            continue
        if allow is not None and key not in allow:
            continue
        if key not in found:
            found.append(key)
    return found


def parse_llm_ids(text: str) -> list[str]:
    found: list[str] = []
    for match in VIDEO_IDS.findall(text or ""):
        key = match.lower()
        key = key.replace("video.scale.s0", "video.scale.s")
        if key in CATALOG_BY_ID and key not in found:
            found.append(key)
    return found


def merge_suggestions(brief: dict[str, Any], llm_text: str, llm_used: bool) -> dict[str, Any]:
    ranked = heuristic_rank(brief)
    llm_ids = parse_llm_ids(llm_text)
    if llm_ids:
        promoted: list[dict[str, Any]] = []
        seen: set[str] = set()
        for item_id in llm_ids:
            row = CATALOG_BY_ID[item_id]
            promoted.append(
                {
                    "id": item_id,
                    "label": f"{row['code']} · {row['label']}",
                    "kind": row["kind"],
                    "reason": row["use"],
                    "rank": len(promoted) + 1,
                    "source": "llm",
                }
            )
            seen.add(item_id)
        for row in ranked:
            if row["id"] not in seen:
                row = dict(row)
                row["rank"] = len(promoted) + 1
                promoted.append(row)
                seen.add(row["id"])
        ranked = promoted[:5]
    return {
        "honesty": "CHARACTERIZATION",
        "llm_used": llm_used,
        "primary": ranked[0]["id"] if ranked else "video.template.a",
        "suggestions": ranked,
        "llm_excerpt": (llm_text or "")[:1200],
        "note": "Not an eval PASS. Chat HTTP 200 is not craft-correct. Skills and tools stay ungated.",
    }


def suggest_prompt(brief: dict[str, Any]) -> str:
    lines = ["Pick one video.template.* and one video.scale.* for this draft. Reply with the ids."]
    for row in CATALOG:
        lines.append(f"- {row['id']}: {row['label']} — {row['use']}")
    lines.append("Brief:")
    for key in ("name", "title", "brief", "audience", "duration", "outlets", "risk", "notes"):
        value = str(brief.get(key) or "").strip()
        if value:
            lines.append(f"{key}: {value}")
    lines.append("Do not enable tools, network, production, or memory writes.")
    return "\n".join(lines)


def initial_graph(brief: dict[str, Any], selected_id: str) -> dict[str, Any]:
    title = str(brief.get("title") or brief.get("name") or "Untitled")
    outputs = first_agents(selected_id)
    return {
        "nodes": [
            {
                "id": "create-project",
                "type": "start",
                "position": {"x": 80, "y": 180},
                "data": {
                    "kind": "start",
                    "label": "Create Project",
                    "title": title,
                    "brief": str(brief.get("brief") or ""),
                    "audience": str(brief.get("audience") or ""),
                    "duration": str(brief.get("duration") or ""),
                    "outlets": str(brief.get("outlets") or ""),
                    "risk": str(brief.get("risk") or ""),
                    "agent_id": None,
                    "io": {"inputs": [], "outputs": outputs},
                },
                "deletable": False,
            }
        ],
        "edges": [],
    }


def migrate_graph(graph: Any, brief: dict[str, Any], selected_id: str) -> dict[str, Any]:
    if not isinstance(graph, dict) or not graph.get("nodes"):
        return initial_graph(brief, selected_id)
    nodes = [dict(node) for node in graph.get("nodes") or [] if isinstance(node, dict)]
    edges = [dict(edge) for edge in graph.get("edges") or [] if isinstance(edge, dict)]
    kept_nodes: list[dict[str, Any]] = []
    dropped: set[str] = set()
    for node in nodes:
        data = node.get("data") if isinstance(node.get("data"), dict) else {}
        node_id = str(node.get("id") or "")
        if node_id == "sub-workflow" or (
            str(node.get("type") or data.get("kind") or "") == "workflow" and not data.get("agent_id")
        ):
            dropped.add(node_id)
            continue
        kept_nodes.append(node)
    if not any(str(node.get("id") or "") == "create-project" for node in kept_nodes):
        return initial_graph(brief, selected_id)
    for node in kept_nodes:
        if str(node.get("id") or "") != "create-project":
            continue
        data = node.setdefault("data", {})
        if not isinstance(data, dict):
            data = {}
            node["data"] = data
        io = data.setdefault("io", {})
        if not isinstance(io, dict):
            io = {}
            data["io"] = io
        io.setdefault("inputs", [])
        if not io.get("outputs"):
            io["outputs"] = first_agents(selected_id)
    kept_edges = [
        edge
        for edge in edges
        if str(edge.get("source") or "") not in dropped and str(edge.get("target") or "") not in dropped
    ]
    return {"nodes": kept_nodes, "edges": kept_edges}


def _row_for_agent(agent_id: str, index: dict[str, dict[str, Any]], *, contract: list[str], reason: str, source: str, rank: int) -> dict[str, Any]:
    info = index.get(agent_id) or {"id": agent_id, "role": agent_id, "inputs": [], "outputs": []}
    return {
        "id": agent_id,
        "label": agent_id,
        "kind": "agent",
        "role": info.get("role") or agent_id,
        "inputs": list(info.get("inputs") or []),
        "outputs": list(info.get("outputs") or []),
        "contract": contract,
        "reason": reason,
        "rank": rank,
        "source": source,
    }


def suggest_next(
    agents_root: Path,
    *,
    template_id: str,
    from_id: str,
    from_agent_id: str | None,
    occupied: list[str],
    out_bus: str | None = None,
) -> dict[str, Any]:
    index = video_io_index(agents_root)
    taken = {item.lower() for item in occupied if item}
    taken.add((from_agent_id or "").lower())
    ranked: list[dict[str, Any]] = []
    seen: set[str] = set()
    bus = (out_bus or "").lower().strip()

    def push(agent_id: str, contract: list[str], reason: str, source: str) -> None:
        key = agent_id.lower()
        if not key.startswith("video.") or key in taken or key in seen or key in CATALOG_BY_ID:
            return
        if key not in index and source != "lane":
            return
        seen.add(key)
        ranked.append(_row_for_agent(key, index, contract=contract, reason=reason, source=source, rank=len(ranked) + 1))

    parent = (from_agent_id or "").lower()
    start = from_id == "create-project" or not parent
    outs = first_agents(template_id) if start else [str(item).lower() for item in (index.get(parent) or {}).get("outputs") or []]
    if start:
        lanes = outs
        if bus:
            if bus in lanes:
                push(bus, [bus], f"Create Project Out {bus} (critique_edges bus).", "lane")
            for agent_id in lanes:
                push(agent_id, [agent_id], "Greenlight next from Create Project (critique_edges bus).", "lane")
        else:
            for agent_id in lanes:
                push(agent_id, [agent_id], "Greenlight next from Create Project (critique_edges bus).", "lane")
    else:
        parent_io = index.get(parent) or {"inputs": [], "outputs": []}
        outputs = [str(item).lower() for item in parent_io.get("outputs") or []]
        if bus:
            push(bus, [bus], f"{parent} Out {bus}.", "parent_output")
            for agent_id, info in index.items():
                inputs = [str(item).lower() for item in info.get("inputs") or []]
                if bus in inputs or (parent in inputs and agent_id == bus):
                    push(agent_id, [bus], f"{agent_id} takes Out {bus}.", "parent_input")
            for agent_id in outputs:
                push(agent_id, [agent_id], f"{parent} outputs this bus.", "parent_output")
        else:
            for agent_id in outputs:
                push(agent_id, [agent_id], f"{parent} outputs this bus.", "parent_output")
            for agent_id, info in index.items():
                inputs = [str(item).lower() for item in info.get("inputs") or []]
                if parent in inputs:
                    push(agent_id, [parent], f"{agent_id} lists {parent} as input.", "parent_input")

    return {
        "honesty": "CHARACTERIZATION",
        "llm_used": False,
        "from_id": from_id,
        "from_agent_id": parent or None,
        "out_bus": bus or None,
        "outs": outs,
        "parent_chat_id": parent if parent in index else "video.planner",
        "primary": ranked[0]["id"] if ranked else "",
        "suggestions": ranked[:8],
        "note": "Not an eval PASS. A node may Out to several next agents. Declared I/O handoff, not a live grant. Skills and tools stay ungated.",
        "llm_excerpt": "",
    }


def next_prompt(body: dict[str, Any]) -> str:
    from_id = str(body.get("from_id") or "create-project")
    parent = str(body.get("from_agent_id") or "Create Project")
    lines = [
        f"Parent node {parent} ({from_id}) needs the next workflow agent.",
        "Reply with one video.* agent id from this list. Use the declared critique_edges buses only.",
    ]
    for row in body.get("suggestions") or []:
        if not isinstance(row, dict):
            continue
        lines.append(
            f"- {row.get('id')}: in={','.join(row.get('inputs') or []) or '—'} "
            f"out={','.join(row.get('outputs') or []) or '—'} ({row.get('reason')})"
        )
    lines.append("Do not enable tools, network, production, or memory writes.")
    return "\n".join(lines)


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def list_projects(root: Path) -> list[dict[str, Any]]:
    root.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    for child in sorted(root.iterdir()):
        payload_path = child / "project.json"
        if not child.is_dir() or not payload_path.is_file():
            continue
        try:
            payload = json.loads(payload_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(payload, dict):
            continue
        rows.append(
            {
                "id": child.name,
                "name": payload.get("name") or child.name,
                "title": payload.get("title") or child.name,
                "sub_workflow_id": payload.get("sub_workflow_id"),
                "updated_at": payload.get("updated_at"),
            }
        )
    return rows


def read_project(root: Path, slug: str) -> dict[str, Any]:
    slug = normalize_slug(slug)
    folder = _safe_dir(root, slug)
    path = folder / "project.json"
    if not path.is_file():
        raise CasopsError(ErrorCode.INH_PARENT_MISSING, detail="unknown project")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH)
    payload["id"] = slug
    payload["folder"] = f"project/{slug}"
    brief = {
        "name": slug,
        "title": str(payload.get("title") or slug),
        "brief": str(payload.get("brief") or ""),
        "audience": str(payload.get("audience") or ""),
        "duration": str(payload.get("duration") or ""),
        "outlets": str(payload.get("outlets") or ""),
        "risk": str(payload.get("risk") or ""),
    }
    payload["graph"] = migrate_graph(payload.get("graph"), brief, str(payload.get("sub_workflow_id") or "video.template.a"))
    return payload


def write_project(root: Path, payload: dict[str, Any], *, dry_run: bool, create: bool) -> dict[str, Any]:
    slug = normalize_slug(str(payload.get("name") or payload.get("id") or ""))
    folder = _safe_dir(root, slug)
    existing = (folder / "project.json").is_file()
    if create and existing:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="project already exists")
    if not create and not existing:
        raise CasopsError(ErrorCode.INH_PARENT_MISSING, detail="unknown project")
    selected = str(payload.get("sub_workflow_id") or "video.template.a").lower()
    if selected not in CATALOG_BY_ID:
        selected = "video.template.a"
    brief = {
        "name": slug,
        "title": str(payload.get("title") or slug),
        "brief": str(payload.get("brief") or ""),
        "audience": str(payload.get("audience") or ""),
        "duration": str(payload.get("duration") or "15s"),
        "outlets": str(payload.get("outlets") or "social"),
        "risk": str(payload.get("risk") or "low"),
        "notes": str(payload.get("notes") or ""),
    }
    graph = migrate_graph(payload.get("graph"), brief, selected)
    now = _now()
    record = {
        "schema_version": "casops.project.v1",
        "id": slug,
        "name": slug,
        "title": brief["title"],
        "brief": brief["brief"],
        "audience": brief["audience"],
        "duration": brief["duration"],
        "outlets": brief["outlets"],
        "risk": brief["risk"],
        "notes": brief["notes"],
        "group": "video",
        "sub_workflow_id": selected,
        "suggestion": payload.get("suggestion") if isinstance(payload.get("suggestion"), dict) else None,
        "graph": graph,
        "honesty": "CHARACTERIZATION",
        "created_at": payload.get("created_at") or now,
        "updated_at": now,
        "folder": f"project/{slug}",
        "production_activation": False,
        "allowed_tools": [],
    }
    if dry_run:
        record["saved"] = False
        record["dry_run"] = True
        return record
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "project.json").write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    readme = (
        f"# {record['title']}\n\n"
        f"One project, one workflow (`{selected}`). Start at Create Project; next-link expands agents via critique_edges. CHARACTERIZATION only.\n\n"
        f"{record['brief']}\n"
    )
    (folder / "README.md").write_text(readme, encoding="utf-8")
    record["saved"] = True
    record["dry_run"] = False
    return record
