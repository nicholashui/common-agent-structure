"""Instruction-pass parsing: agents accept a pass and emit induce_calls / ASK_HUMAN / next_instruction."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

AGENT_ID_RE = re.compile(r"\b((?:video|specials)\.[a-z0-9_-]+)\b", re.I)
INDUCE_LINE_RE = re.compile(
    r"induce_call:\s*((?:video|specials)\.[a-z0-9_-]+)\s*(?:because|why|[-—:])?\s*(.*)$",
    re.I,
)
ASK_LINE_RE = re.compile(r"(?:ASK_HUMAN|human_ask)\s*:\s*(.+)$", re.I)
OPTION_RE = re.compile(r"^OPTION\s*([A-Za-z0-9][A-Za-z0-9_-]*)[\.:)\]]\s*(.+)$", re.I)
RECOMMEND_RE = re.compile(r"^RECOMMEND:\s*(\S+)", re.I)
DECIDE_BY_RE = re.compile(r"^DECIDE_BY:\s*(\S+)", re.I)
DISPATCH_ORDER = (
    "video.creativedirector",
    "video.director",
    "video.continuity",
    "video.cinematographer",
    "video.mua_makeup",
    "video.cameraoperator",
    "video.critic",
    "video.aiqaconsistency",
)
CRAFT_HEADINGS: dict[str, tuple[str, ...]] = {
    "video.creativedirector": ("Creative direction",),
    "video.director": (
        "0–3s | opening face smash",
        "3–6s | eye and skin macro",
        "6–10s | nose and mouth super close-up",
        "10–13s | climb back to the eye",
        "13–15s | eye hold",
    ),
    "video.cinematographer": ("Light",),
    "video.mua_makeup": ("Makeup",),
    "video.cameraoperator": ("Camera lock",),
    "video.continuity": ("Subject", "Hair", "Skin"),
    "video.critic": (),
    "video.aiqaconsistency": (),
    "video.promptengineer": ("Frame", "Sound"),
}


def default_human_instruction() -> str:
    """Unused as a protocol dump. Create Project stays a short human brief."""
    return ""


def human_brief_only(text: str, record: dict[str, Any] | None = None) -> str:
    """Create Project is high-level intent only. Protocol and craft detail are not the human's job."""
    raw = (text or "").strip()
    record = record if isinstance(record, dict) else {}
    title = str(record.get("title") or record.get("name") or "").strip()
    brief = str(record.get("brief") or "").strip()
    protocol = (
        "CASOPS INSTRUCTION" in raw
        or "must induce related crafts" in raw
        or "induce_call:" in raw.lower()
        or "next_instruction_required" in raw
    )
    if not raw or protocol:
        return ". ".join(part for part in (title, brief) if part).strip() or title
    if len(raw) > 280:
        return raw[:280].rsplit(" ", 1)[0]
    return raw


def _json_blob(text: str) -> dict[str, Any]:
    raw = (text or "").strip()
    if "```" in raw:
        start = raw.find("```")
        chunk = raw[start + 3 :]
        if chunk.lower().startswith("json"):
            chunk = chunk[4:]
        end = chunk.find("```")
        if end >= 0:
            raw = chunk[:end].strip()
    try:
        payload = json.loads(raw)
        return payload if isinstance(payload, dict) else {}
    except json.JSONDecodeError:
        left = (text or "").find("{")
        right = (text or "").rfind("}")
        if left >= 0 and right > left:
            try:
                payload = json.loads((text or "")[left : right + 1])
                return payload if isinstance(payload, dict) else {}
            except json.JSONDecodeError:
                return {}
    return {}


def parse_emitted_instructions(text: str) -> dict[str, Any]:
    """Read induce_calls, ASK_HUMAN, why, freeze, next_instruction from an agent reply."""
    induce: list[dict[str, str]] = []
    asks: list[str] = []
    seen_ids: set[str] = set()
    blob = _json_blob(text)
    for item in blob.get("induce_calls") or []:
        if isinstance(item, str):
            agent_id = item.strip()
            why = ""
        elif isinstance(item, dict):
            agent_id = str(item.get("to_agent_id") or item.get("agent_id") or "").strip()
            why = str(item.get("objective") or item.get("why") or item.get("because") or "").strip()
        else:
            continue
        if agent_id and agent_id not in seen_ids:
            seen_ids.add(agent_id)
            induce.append({"agent_id": agent_id, "why": why})
    raw_asks = blob.get("human_asks") or blob.get("ask_human") or blob.get("ASK_HUMAN") or []
    if isinstance(raw_asks, str) and raw_asks.strip():
        asks.append(raw_asks.strip())
    elif isinstance(raw_asks, list):
        for item in raw_asks:
            if isinstance(item, str) and item.strip():
                asks.append(item.strip())
            elif isinstance(item, dict):
                q = str(item.get("question") or item.get("text") or "").strip()
                if q:
                    asks.append(q)
    why = str(blob.get("why") or blob.get("creative_direction") or blob.get("thesis") or "").strip()
    freeze = str(blob.get("freeze") or blob.get("freeze_list") or "").strip()
    thinking = str(blob.get("thinking") or "").strip()
    recommend = str(blob.get("recommend") or blob.get("recommended") or "").strip()
    decide_by = str(blob.get("decide_by") or blob.get("DECIDE_BY") or "").strip()
    options: list[dict[str, str]] = []
    for item in blob.get("options") or []:
        if isinstance(item, str) and item.strip():
            options.append({"id": str(len(options) + 1), "label": item.strip(), "why": ""})
        elif isinstance(item, dict):
            options.append(
                {
                    "id": str(item.get("id") or len(options) + 1),
                    "label": str(item.get("label") or item.get("text") or "").strip(),
                    "why": str(item.get("why") or item.get("because") or "").strip(),
                }
            )
    nxt = blob.get("next_instruction")
    next_instruction = ""
    if isinstance(nxt, dict):
        next_instruction = json.dumps(nxt, ensure_ascii=False)
    elif isinstance(nxt, str):
        next_instruction = nxt.strip()
    for line in (text or "").splitlines():
        match = INDUCE_LINE_RE.match(line.strip())
        if match:
            agent_id = match.group(1)
            reason = (match.group(2) or "").strip()
            if agent_id not in seen_ids:
                seen_ids.add(agent_id)
                induce.append({"agent_id": agent_id, "why": reason})
        ask = ASK_LINE_RE.match(line.strip())
        if ask:
            question = ask.group(1).strip()
            if question and question not in asks:
                asks.append(question)
        low = line.strip().lower()
        if low.startswith("why:") or low.startswith("creative direction"):
            extra = line.split(":", 1)[-1].strip()
            if extra:
                why = (why + "\n" + extra).strip() if why else extra
        if low.startswith("freeze:") or low.startswith("freeze list"):
            extra = line.split(":", 1)[-1].strip()
            if extra:
                freeze = (freeze + "\n" + extra).strip() if freeze else extra
        if low.startswith("thinking:"):
            extra = line.split(":", 1)[-1].strip()
            if extra:
                thinking = (thinking + "\n" + extra).strip() if thinking else extra
        opt = OPTION_RE.match(line.strip())
        if opt:
            options.append({"id": opt.group(1), "label": opt.group(2).strip(), "why": ""})
        rec = RECOMMEND_RE.match(line.strip())
        if rec:
            recommend = rec.group(1).strip()
        dec = DECIDE_BY_RE.match(line.strip())
        if dec:
            decide_by = dec.group(1).strip()
    if options and not recommend:
        recommend = options[0]["id"]
    if not decide_by:
        decide_by = "human" if options else "self"
    return {
        "induce_calls": induce,
        "human_asks": asks,
        "why": why,
        "freeze": freeze,
        "next_instruction": next_instruction,
        "thinking": thinking,
        "options": [row for row in options if row.get("label")],
        "recommend": recommend,
        "decide_by": decide_by,
    }


def pick_option(parsed: dict[str, Any], choice: str | None) -> dict[str, str] | None:
    options = parsed.get("options") if isinstance(parsed.get("options"), list) else []
    if not options:
        return None
    pick = str(choice or parsed.get("recommend") or options[0].get("id") or "")
    for row in options:
        if str(row.get("id")) == pick:
            return row
    return options[0]


def named_agent_ids(text: str, agents_root: Path | None) -> list[str]:
    found: list[str] = []
    for match in AGENT_ID_RE.finditer(text or ""):
        agent_id = match.group(1)
        if agent_id in found:
            continue
        if agents_root is not None and not (Path(agents_root) / agent_id / "agent_spec.json").is_file():
            continue
        found.append(agent_id)
    return found


def order_induce(agent_ids: list[str]) -> list[str]:
    seen: list[str] = []
    for item in DISPATCH_ORDER:
        if item in agent_ids and item not in seen:
            seen.append(item)
    for item in agent_ids:
        if item not in seen:
            seen.append(item)
    return seen


def craft_headings_for(agent_id: str) -> tuple[str, ...]:
    return CRAFT_HEADINGS.get(agent_id, ())


def split_continuity_craft(craft: str) -> dict[str, str]:
    """Map one continuity lock craft into Subject / Hair / Skin. Wardrobe stays on Subject."""
    parts = [item.strip() for item in (craft or "").split("\n") if item.strip()]
    identity = parts[0] if parts else ""
    hair = parts[1] if len(parts) > 1 else ""
    skin = parts[2] if len(parts) > 2 else ""
    wardrobe = "\n".join(parts[3:]) if len(parts) > 3 else ""
    subject = "\n".join(item for item in (identity, wardrobe) if item)
    return {"Subject": subject, "Hair": hair, "Skin": skin}
