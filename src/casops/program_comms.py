"""ISSUE-0013 Program collab hops. Characterization only. Host-mediated."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.programs import CREATIVE_AGENT, FIRST_AGENT_HOP, FIRST_CALLED, _forbid_sample, read_program

CHILD_FIRST_CALLED = "video.promptengineer"
CHILD_HUMAN_LOCKS: tuple[str, ...] = (
    "video.promptengineer",
    "video.director",
    "video.cinematographer",
    "video.mua_makeup",
    "video.continuity",
)

PROGRAM_HOPS: tuple[dict[str, str], ...] = (
    {
        "from": "create-program",
        "to": FIRST_AGENT_HOP,
        "kind": "instruction",
        "text": "Decode the Program brief. OPTIONS only. Do not write pages or shot grammar.",
        "pass_id": "w0",
    },
    {
        "from": FIRST_AGENT_HOP,
        "to": "create-program",
        "kind": "return",
        "text": "Locution read. Next agent is specials.general-creative-agent, then video.showrunner.",
        "pass_id": "w0",
    },
    {
        "from": FIRST_AGENT_HOP,
        "to": CREATIVE_AGENT,
        "kind": "induce",
        "text": "induce_call: specials.general-creative-agent because campaign framework. DECIDE_BY: video.showrunner.",
        "pass_id": "w0",
    },
    {
        "from": CREATIVE_AGENT,
        "to": FIRST_CALLED,
        "kind": "return",
        "text": "Three OPTIONS for the film framework. Do not write the generator novel. DECIDE_BY: video.showrunner.",
        "pass_id": "w0",
    },
    {
        "from": FIRST_CALLED,
        "to": CREATIVE_AGENT,
        "kind": "choice",
        "text": "Showrunner is Program first-called. Screenwriter is W1 after logline lock.",
        "pass_id": "w0",
    },
    {
        "from": "create-program",
        "to": FIRST_CALLED,
        "kind": "instruction",
        "text": "You are first-called for this Program. Own bible/arc. Induce video.screenwriter only after logline lock.",
        "pass_id": "w0",
    },
    {
        "from": FIRST_CALLED,
        "to": "video.screenwriter",
        "kind": "induce",
        "text": "induce_call: video.screenwriter because W1 treatment then screenplay. Not first-called.",
        "pass_id": "w1",
    },
    {
        "from": "video.director",
        "to": "video.planner",
        "kind": "induce",
        "text": "W2 generation list: scene → segments. One segment = one Project. Do not spawn yet.",
        "pass_id": "w2",
    },
    {
        "from": "video.storyboard",
        "to": FIRST_CALLED,
        "kind": "return",
        "text": "Boards before motion. Visual bible lock required with generation_list before spawn.",
        "pass_id": "w2",
    },
    {
        "from": "host_service",
        "to": "video.editor",
        "kind": "instruction",
        "text": "Cut pass only after takes exist. Order: assembly → rough → fine → picture lock. Then color/mix/VFX/titles. fused_request stays null.",
        "pass_id": "w5",
    },
    {
        "from": "video.editor",
        "to": "host_service",
        "kind": "return",
        "text": "cut_state: assembly",
        "pass_id": "w5",
    },
    {
        "from": "video.editor",
        "to": "host_service",
        "kind": "return",
        "text": "cut_state: rough",
        "pass_id": "w5",
    },
    {
        "from": "video.editor",
        "to": "host_service",
        "kind": "return",
        "text": "cut_state: fine",
        "pass_id": "w5",
    },
    {
        "from": "video.editor",
        "to": "host_service",
        "kind": "return",
        "text": "cut_state: picture_lock. Finish refused before this lock.",
        "pass_id": "w5",
    },
)


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def graph_from_hops(items: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    hops = list(items or characterization_hops())
    nodes: dict[str, dict[str, Any]] = {
        "create-program": {
            "id": "create-program",
            "type": "start",
            "position": {"x": 40, "y": 80},
            "deletable": False,
            "data": {"kind": "start", "label": "Create Program"},
        }
    }
    edges: list[dict[str, Any]] = []
    seen_edges: set[tuple[str, str]] = set()
    for hop in hops:
        src = str(hop.get("from") or "")
        dst = str(hop.get("to") or "")
        if not src or not dst:
            continue
        for party in (src, dst):
            if party in nodes:
                continue
            if party in {"human_operator", "human-ask"}:
                kind = "human"
                label = "Human"
                agent_id = None
            elif party == "create-program":
                continue
            elif party in {"output-prompt", "host_service"}:
                kind = "output" if party == "output-prompt" else "agent"
                label = "Output" if party == "output-prompt" else "Host"
                agent_id = None if party == "output-prompt" else party
            else:
                kind = "agent"
                label = party.split(".")[-1]
                agent_id = party
            nodes[party] = {
                "id": party,
                "type": kind if kind in {"start", "output", "human"} else "agent",
                "position": {"x": 80, "y": 80},
                "data": {"kind": kind, "label": label, "agent_id": agent_id},
            }
        key = (src, dst)
        if key in seen_edges or src == dst:
            continue
        seen_edges.add(key)
        edges.append(
            {
                "id": f"e-{src}-{dst}-{len(edges)}",
                "source": src,
                "target": dst,
                "sourceHandle": "next",
                "targetHandle": "in",
                "label": str(hop.get("kind") or ""),
            }
        )
    return {"nodes": list(nodes.values()), "edges": edges}


def characterization_hops() -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for index, hop in enumerate(PROGRAM_HOPS, start=1):
        items.append(
            {
                "id": f"comm-{index:04d}",
                "from": hop["from"],
                "to": hop["to"],
                "kind": hop["kind"],
                "text": hop["text"],
                "pass_id": hop["pass_id"],
                "live": False,
                "honesty": "CHARACTERIZATION",
                "created_at": _now(),
            }
        )
    return items


def load_program_comms(root: Path, code: str) -> dict[str, Any]:
    record = read_program(root, code)
    folder = Path(root) / record["code"]
    path = folder / "comms.json"
    if path.is_file():
        payload = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(payload, dict) and isinstance(payload.get("items"), list):
            payload["first_called"] = FIRST_CALLED
            payload["first_agent_hop"] = FIRST_AGENT_HOP
            payload["child_first_called"] = CHILD_FIRST_CALLED
            payload["child_human_locks"] = list(CHILD_HUMAN_LOCKS)
            payload["honesty"] = "CHARACTERIZATION"
            payload["graph"] = graph_from_hops(payload.get("items") if isinstance(payload.get("items"), list) else None)
            return payload
    items = characterization_hops()
    return {
        "program_id": record["code"],
        "first_called": FIRST_CALLED,
        "first_agent_hop": FIRST_AGENT_HOP,
        "child_first_called": CHILD_FIRST_CALLED,
        "child_human_locks": list(CHILD_HUMAN_LOCKS),
        "honesty": "CHARACTERIZATION",
        "live": False,
        "items": items,
        "graph": graph_from_hops(items),
    }


def stamp_program_comms(root: Path, code: str, *, dry_run: bool) -> dict[str, Any]:
    record = read_program(root, code)
    payload = load_program_comms(root, code)
    if not payload.get("items"):
        payload["items"] = characterization_hops()
    payload["first_called"] = FIRST_CALLED
    payload["first_agent_hop"] = FIRST_AGENT_HOP
    payload["child_first_called"] = CHILD_FIRST_CALLED
    payload["child_human_locks"] = list(CHILD_HUMAN_LOCKS)
    payload["honesty"] = "CHARACTERIZATION"
    payload["program_id"] = record["code"]
    payload["graph"] = graph_from_hops(payload.get("items") if isinstance(payload.get("items"), list) else None)
    if dry_run:
        payload["dry_run"] = True
        payload["saved"] = False
        return payload
    folder = Path(root) / record["code"]
    _forbid_sample(folder)
    if not folder.is_dir():
        raise CasopsError(ErrorCode.INH_PARENT_MISSING, detail="unknown program")
    persist = {key: value for key, value in payload.items() if key not in {"saved", "dry_run"}}
    (folder / "comms.json").write_text(json.dumps(persist, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    payload["dry_run"] = False
    payload["saved"] = True
    return payload
