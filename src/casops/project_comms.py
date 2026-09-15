"""Per-node communication history + host-mediated asain-beauty collab pass."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from collections.abc import Callable
from typing import Any

ChatFn = Callable[[str, str], dict[str, Any]]

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.project_instruction import (
    craft_headings_for,
    human_brief_only,
    named_agent_ids,
    order_induce,
    parse_emitted_instructions,
    pick_option,
    split_continuity_craft,
)
from casops.projects import normalize_slug, read_project, write_project

COMMS_SCHEMA = "casops.project.comms.v1"
FIRST_CALLED = "video.promptengineer"
# Gold asain-beauty-prompt.txt headings (structure only). Never paste the sample body into Chat.
GENERATOR_SECTIONS: tuple[str, ...] = (
    "Creative direction",
    "Frame",
    "Subject",
    "Hair",
    "Makeup",
    "Skin",
    "Light",
    "0–3s | opening face smash",
    "3–6s | eye and skin macro",
    "6–10s | nose and mouth super close-up",
    "10–13s | climb back to the eye",
    "13–15s | eye hold",
    "Camera lock",
    "Sound",
    "Negatives",
    "Human asks",
)
FIRST_CALLED_HEADINGS: tuple[str, ...] = ("Frame", "Sound")
INDUCE_ROSTER: tuple[tuple[str, str, str, tuple[str, ...]], ...] = (
    (
        "video.creativedirector",
        "br_asain_01_cd",
        "Creative thesis only: THESIS + WHY grounded in the human brief. Do not author lighting, makeup, or motors.",
        ("Creative direction",),
    ),
    (
        "video.director",
        "br_asain_01_dir",
        "Shot-intent only: 0-3 smash, 3-6 eye/skin, 6-10 nose/mouth, 10-13 climb, 13-15 hold. Size/angle/move/duration/performance. No lighting numbers, no makeup, no camera motors.",
        (
            "0–3s | opening face smash",
            "3–6s | eye and skin macro",
            "6–10s | nose and mouth super close-up",
            "10–13s | climb back to the eye",
            "13–15s | eye hold",
        ),
    ),
    (
        "video.cinematographer",
        "br_asain_01_cin",
        "Light and lens only: hard 4pm sun through sheer, 10-20cm phone-main, authorized off-center crop. No makeup, no blocking, no motors.",
        ("Light",),
    ),
    (
        "video.mua_makeup",
        "br_asain_01_mua",
        "Bare-makeup lock only: sunscreen/moisturizer, natural brow, dusty-rose glaze, no fake lashes. Do not author the pore manifesto.",
        ("Makeup",),
    ),
    (
        "video.cameraoperator",
        "br_asain_01_cam",
        "One motor: handheld 1-2mm breath crawl. No traditional push / pull / pan / orbit.",
        ("Camera lock",),
    ),
    (
        "video.continuity",
        "br_asain_01_cont",
        "Freeze list only: moles, freckles, hair part, vellus, tank strap, skin texture. Do not rewrite lighting or makeup recipes.",
        ("Subject", "Hair", "Skin"),
    ),
    (
        "video.critic",
        "br_asain_01_crit",
        "Critique-bus only. Flag idol-template, poreless skin, ring light, 4K claims, one-pass T2V packing, unauthorized orbit. Not the closer.",
        (),
    ),
)
# Identity locks the gold file requires. Facts, not the sample novel. Agents write new prose around them.
CREATIVE_LOCK = (
    "Must-keep literals (emit these strings; write new surrounding sentences; do not JSON):\n"
    "- clearly adult East Asian woman, about 25-26\n"
    "- tiny light-brown mole sits just under the outer corner of the left eye\n"
    "- faint mole outside the left mouth corner; faint sleep crease on one cheek\n"
    "- 15-second, 9:16 vertical photoreal live-action; handheld phone-main, ~50-70mm, 10-20cm\n"
    "- makeup: sunscreen and thin moisturizer only; natural brows; dusty-rose thin wet glaze\n"
    "- skin: real pores, pale freckles on bridge and cheekbones, T-zone oil, facial vellus\n"
    "- Light: hard late-afternoon sun ~4pm, camera-left front, half-open window + thin white sheer\n"
    "- No traditional push / pull / pan / orbit\n"
    "- no beauty filter, no airbrushed skin, no poreless skin, no ring-light catchlight, no fake eyelashes\n"
    "- Do not claim 4K. Do not orbit. Do not one-pass T2V JSON. English pasteable prose only."
)
# Per-agent slice so members do not parrot crafts they do not own.
LOCK_SLICES: dict[str, str] = {
    FIRST_CALLED: CREATIVE_LOCK,
    "video.director": (
        "In-role lock: clearly adult East Asian woman. 15s, 9:16. "
        "Performance: no speech, small breath/blink, at most 5-10 degree settle. "
        "Do not write lighting numbers, makeup, or camera motors. Do not claim 4K."
    ),
    "video.cinematographer": (
        "In-role lock: hard late-afternoon sun ~4pm, camera-left front, half-open window + thin white sheer. "
        "Phone-main ~50-70mm, 10-20cm, authorized off-center crop. No studio softbox, no ring-light. Do not claim 4K."
    ),
    "video.mua_makeup": (
        "In-role lock: sunscreen and thin moisturizer only; natural brows; dusty-rose thin wet glaze; no fake eyelashes. "
        "Do not author pores/freckles/moles (continuity). Do not write lighting or motors."
    ),
    "video.cameraoperator": (
        "In-role lock: one motor — handheld 1-2mm breath crawl. "
        "Must emit: No traditional push / pull / pan / orbit. Do not own lighting or makeup."
    ),
    "video.continuity": (
        "In-role lock: clearly adult East Asian woman. "
        "Must emit: tiny light-brown mole sits just under the outer corner of the left eye. "
        "Also freeze: faint mole outside the left mouth corner; faint sleep crease; pale freckles; "
        "real pores; T-zone oil; facial vellus; hair part; thin off-white ribbed tank strap if collarbone. "
        "Do not rewrite lighting or makeup recipes."
    ),
    "video.critic": (
        "Evaluate only. Flag: idol-template face, poreless/airbrushed skin, ring-light catchlight, 4K claims, "
        "one-pass T2V packing, unauthorized orbit/push/pull. "
        "If you name avoids, include: no beauty filter, no airbrushed skin. "
        "Return critique-bus rows. Do not write Frame/Subject/Makeup/Light/Negatives."
    ),
}
# Distinctive gold sentence that must NEVER be sent to agents (proves we did not paste the sample body).
GOLD_BODY_PROBE = "Two or three wisps catch on the glossed mouth corner mid-clip."
EUROPEAN_GOLD_BODY_PROBE = "A few teeth may flash and disappear."
JAPANESE_GOLD_BODY_PROBE = "RETURN THE PICKLES BEFORE DINNER"
HONGKONG_GOLD_BODY_PROBE = "GET HOME WITH THE BUN"
GOLD_BODY_PROBES: tuple[str, ...] = (
    GOLD_BODY_PROBE,
    EUROPEAN_GOLD_BODY_PROBE,
    JAPANESE_GOLD_BODY_PROBE,
    HONGKONG_GOLD_BODY_PROBE,
)
HEADING_ALIASES = {
    "0-3s | opening face smash": "0–3s | opening face smash",
    "3-6s | eye and skin macro": "3–6s | eye and skin macro",
    "6-10s | nose and mouth super close-up": "6–10s | nose and mouth super close-up",
    "10-13s | climb back to the eye": "10–13s | climb back to the eye",
    "13-15s | eye hold": "13–15s | eye hold",
    "sound, if the model supports native audio": "Sound",
}

_TAG_SAFE = re.compile(r"^[A-Za-z0-9._:-]{1,80}$")
_MEDIA_NAME = re.compile(r"^[A-Za-z0-9._-]+$")


def sanitize_comm_media(slug: str, media: Any) -> dict[str, Any] | None:
    """Rewrite comm media to same-origin output/file URLs. Off-origin urls are dropped."""
    if not isinstance(media, dict):
        return None
    name = str(media.get("name") or "")
    kind = str(media.get("kind") or "")
    if not _MEDIA_NAME.match(name) or ".." in name or kind not in {"video", "image"}:
        return None
    out: dict[str, Any] = {
        "name": name,
        "kind": kind,
        "path": f"project/{slug}/output/{name}",
        "url": f"/api/v3/projects/{slug}/output/file?name={name}",
    }
    poster = str(media.get("poster") or "")
    poster_name = str(media.get("poster_name") or "")
    if not poster_name and "name=" in poster:
        poster_name = poster.rsplit("name=", 1)[-1].split("&", 1)[0]
    if poster_name and _MEDIA_NAME.match(poster_name) and ".." not in poster_name:
        out["poster"] = f"/api/v3/projects/{slug}/output/file?name={poster_name}"
    return out


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _comms_path(root: Path, slug: str) -> Path:
    return Path(root) / slug / "comms.json"


def _tag(project_id: str, node_id: str, comm_id: str, label: str) -> dict[str, str]:
    return {
        "project_id": project_id,
        "node_id": node_id,
        "comm_id": comm_id,
        "label": label,
    }


def load_comms(root: Path, slug: str) -> dict[str, Any]:
    path = _comms_path(root, slug)
    if not path.is_file():
        return {"schema_version": COMMS_SCHEMA, "project_id": slug, "items": []}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail=str(exc)) from exc
    if not isinstance(payload, dict):
        return {"schema_version": COMMS_SCHEMA, "project_id": slug, "items": []}
    items = payload.get("items") if isinstance(payload.get("items"), list) else []
    decisions = payload.get("decisions") if isinstance(payload.get("decisions"), list) else []
    locks = payload.get("locks") if isinstance(payload.get("locks"), dict) else {}
    autopilot = payload.get("autopilot") if isinstance(payload.get("autopilot"), dict) else {}
    return {
        "schema_version": COMMS_SCHEMA,
        "project_id": slug,
        "items": items,
        "decisions": decisions,
        "walkthrough": payload.get("walkthrough") or "",
        "honesty": payload.get("honesty") or "CHARACTERIZATION",
        "note": payload.get("note") or "",
        "locks": {str(key): str(value) for key, value in locks.items() if str(key) and str(value)},
        "autopilot": autopilot,
    }


def save_comms(root: Path, slug: str, payload: dict[str, Any], *, dry_run: bool) -> dict[str, Any]:
    record = {
        "schema_version": COMMS_SCHEMA,
        "project_id": slug,
        "items": payload.get("items") if isinstance(payload.get("items"), list) else [],
        "decisions": payload.get("decisions") if isinstance(payload.get("decisions"), list) else [],
        "walkthrough": payload.get("walkthrough") or "",
        "updated_at": _now(),
        "honesty": "CHARACTERIZATION",
        "note": payload.get("note") or "",
        "locks": payload.get("locks") if isinstance(payload.get("locks"), dict) else {},
        "autopilot": payload.get("autopilot") if isinstance(payload.get("autopilot"), dict) else {},
    }
    if dry_run:
        record["saved"] = False
        record["dry_run"] = True
        return record
    folder = Path(root) / slug
    folder.mkdir(parents=True, exist_ok=True)
    _comms_path(root, slug).write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    record["saved"] = True
    record["dry_run"] = False
    return record


def append_comm(
    root: Path,
    slug: str,
    body: dict[str, Any],
    *,
    dry_run: bool,
) -> dict[str, Any]:
    normalize_slug(slug)
    store = load_comms(root, slug)
    items: list[dict[str, Any]] = list(store.get("items") or [])
    comm_id = str(body.get("id") or f"comm-{len(items) + 1:04d}")
    if not _TAG_SAFE.match(comm_id):
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="bad comm id")
    node_id = str(body.get("node_id") or "create-project")
    entry = {
        "id": comm_id,
        "node_id": node_id,
        "from": str(body.get("from") or "human_operator"),
        "to": str(body.get("to") or node_id),
        "kind": str(body.get("kind") or "instruction"),
        "text": str(body.get("text") or ""),
        "input_tags": body.get("input_tags") if isinstance(body.get("input_tags"), list) else [],
        "output_tags": body.get("output_tags") if isinstance(body.get("output_tags"), list) else [],
        "pass_id": str(body.get("pass_id") or ""),
        "created_at": _now(),
        "live": bool(body.get("live")),
        "provider": str(body.get("provider") or ""),
        "error": str(body.get("error") or ""),
        "agents": body.get("agents") if isinstance(body.get("agents"), list) else [],
        "media": sanitize_comm_media(slug, body.get("media")),
    }
    items.append(entry)
    saved = save_comms(
        root,
        slug,
        {
            "items": items,
            "decisions": store.get("decisions") or [],
            "walkthrough": store.get("walkthrough") or "",
            "note": store.get("note") or "",
            "locks": store.get("locks") or {},
            "autopilot": store.get("autopilot") or {},
        },
        dry_run=dry_run,
    )
    saved["item"] = entry
    return saved


def sample_prompt_path(root: Path, slug: str) -> Path:
    return Path(root) / slug / "sample" / f"{slug}-prompt.txt"


def output_prompt_path(root: Path, slug: str) -> Path:
    return Path(root) / slug / "output" / f"{slug}-prompt.txt"


def output_canonical_path(root: Path, slug: str) -> Path:
    return Path(root) / slug / "output" / f"{slug}-canonical.yaml"


def output_sequence_path(root: Path, slug: str) -> Path:
    return Path(root) / slug / "output" / f"{slug}-sequence.yaml"


def walkthrough_module(slug: str) -> Any:
    if slug == "european-handsome":
        from casops import project_european_handsome_walkthrough as mod

        return mod
    if slug == "japanese-grandma-gta":
        from casops import project_japanese_grandma_gta_walkthrough as mod

        return mod
    if slug == "hongkong-grandma-gta":
        from casops import project_hongkong_grandma_gta_walkthrough as mod

        return mod
    from casops import project_sample_walkthrough as mod

    return mod


def _output_compile_preview(root: Path, slug: str, text: str, *, engine: str, clip_id: str = "") -> dict[str, Any]:
    """P5: compile snapshot + critic warnings for Chat. Never calls a vendor. Never reads sample/."""
    empty = {
        "canonical_exists": False,
        "clip_source": "missing",
        "compile_note": "",
        "compiled": None,
        "critic_warnings": [],
    }
    try:
        from casops.project_generate import _load_clip_for_generate, _profile_id_for_engine
        from casops.video_prompt.compile import compile_clip, compiled_snapshot
        from casops.video_prompt.owners import heading_owner
        from casops.video_prompt.assemble import parse_projection_sections
    except Exception:
        return empty
    tag = str(engine or "grok-imagine").strip() or "grok-imagine"
    wanted = str(clip_id or "").strip()
    try:
        clip, source = _load_clip_for_generate(root, slug, text, clip_id=wanted or None)
    except Exception:
        clip, source = _load_clip_for_generate(root, slug, text)
    compiled = None
    if clip:
        compiled = compiled_snapshot(compile_clip(clip, _profile_id_for_engine(tag)))
    warnings: list[dict[str, str]] = []
    if isinstance(clip, dict):
        provenance = clip.get("provenance") if isinstance(clip.get("provenance"), dict) else {}
        for row in provenance.get("diagnostics") or []:
            if not isinstance(row, dict):
                continue
            severity = str(row.get("severity") or "warn")
            if severity not in {"warn", "error"}:
                continue
            warnings.append(
                {
                    "agent_id": str(row.get("agent_id") or "video.critic"),
                    "path": str(row.get("path") or ""),
                    "severity": severity,
                    "message": str(row.get("message") or ""),
                }
            )
    if isinstance(compiled, dict):
        for row in compiled.get("diagnostics") or []:
            if not isinstance(row, dict):
                continue
            severity = str(row.get("severity") or "")
            if severity not in {"warn", "error"}:
                continue
            warnings.append(
                {
                    "agent_id": "video.critic" if "constraint" in str(row.get("code") or "").lower() else "compiler",
                    "path": str(row.get("path") or ""),
                    "severity": severity,
                    "message": str(row.get("message") or ""),
                }
            )
    sections: list[dict[str, str]] = []
    if text.strip():
        parts = parse_projection_sections(text)
        for heading, body in parts.items():
            owner, path = heading_owner(heading)
            sections.append({"heading": heading, "owner": owner, "path": path, "body": body})
    note = ""
    if compiled:
        note = "compiled from canonical v2" if source == "canonical" else "compiled from T4 projection"
    sequence = None
    try:
        from casops.video_prompt.sequence import load_sequence_file, sequence_from_clip

        seq_file = output_sequence_path(root, slug)
        if seq_file.is_file() and "sample" not in seq_file.parts:
            sequence = load_sequence_file(seq_file)
        elif clip:
            sequence = sequence_from_clip(clip, slug=slug, path=f"{slug}-canonical.yaml")
    except Exception:
        sequence = None
    sequence_compile = None
    if sequence and clip:
        try:
            from casops.project_generate import _safe_output_clip_path
            from casops.video_prompt.sequence import compile_sequence

            clips_map: dict[str, dict[str, Any]] = {}
            for row in sequence.get("clips") or []:
                if not isinstance(row, dict):
                    continue
                cid = str(row.get("clip_id") or "")
                cand = _safe_output_clip_path(root, slug, str(row.get("path") or ""))
                if cid and cand is not None and cand.is_file():
                    try:
                        payload = json.loads(cand.read_text(encoding="utf-8"))
                    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
                        continue
                    if isinstance(payload, dict) and payload.get("kind") == "clip":
                        clips_map[cid] = payload
            if clip.get("clip_id") and str(clip.get("clip_id")) not in clips_map:
                clips_map[str(clip.get("clip_id"))] = clip
            if clips_map:
                sequence_compile = compile_sequence(sequence, clips_map, _profile_id_for_engine(tag))
        except Exception:
            sequence_compile = None
    return {
        "canonical_exists": source == "canonical",
        "clip_source": source if clip else "missing",
        "clip_id": str((clip or {}).get("clip_id") or wanted or ""),
        "compile_note": note,
        "compiled": compiled,
        "critic_warnings": warnings,
        "sections": sections,
        "sequence": sequence,
        "sequence_compile": sequence_compile,
    }


def read_output(root: Path, slug: str, *, engine: str = "", clip_id: str = "") -> dict[str, Any]:
    """Read generated prompt only from output/. Never from sample/."""
    normalize_slug(slug)
    path = output_prompt_path(root, slug)
    rel = f"project/{slug}/output/{slug}-prompt.txt"
    if "sample" in path.parts:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="sample/ is read-only")
    import os

    from casops.project_generate import default_video_config, generator_catalog, list_output_media

    configured = bool(os.environ.get("XAI_API_KEY", "").strip())
    if not path.is_file():
        return {
            "path": rel,
            "exists": False,
            "text": "",
            "honesty": "CHARACTERIZATION",
            "media": list_output_media(root, slug),
            "generators": generator_catalog(configured=configured),
            "video_config": default_video_config(""),
            "canonical_exists": False,
            "compile_note": "",
            "compiled": None,
            "critic_warnings": [],
            "sections": [],
            "sequence": None,
            "sequence_compile": None,
            "clip_id": "",
        }
    text = path.read_text(encoding="utf-8")
    payload = {
        "path": rel,
        "exists": True,
        "text": text,
        "honesty": "CHARACTERIZATION",
        "media": list_output_media(root, slug),
        "generators": generator_catalog(configured=configured),
        "video_config": default_video_config(text),
    }
    payload.update(_output_compile_preview(root, slug, text, engine=engine, clip_id=clip_id))
    return payload


def _normalize_prompt(text: str) -> str:
    return "\n".join(line.rstrip() for line in (text or "").replace("\r\n", "\n").split("\n")).strip() + "\n"


def _has_marker(haystack: str, needle: str) -> bool:
    text = haystack.lower()
    target = needle.lower()
    if target in text:
        return True
    alts = {
        "no traditional push / pull / pan / orbit": (
            "no traditional push, pull, pan, or orbit",
            "no traditional push or pull",
            "no push, pull, pan, orbit",
        ),
    }
    return any(option in text for option in alts.get(target, ()))


def validate_prompt(generated: str, gold: str) -> dict[str, Any]:
    left = _normalize_prompt(generated)
    right = _normalize_prompt(gold)
    required = (
        "clearly adult East Asian woman",
        "9:16",
    )
    missing = [item for item in required if not _has_marker(left, item)]
    if "[missing:" in left.lower():
        missing.append("host marked one or more sections missing")
    exact = left == right
    return {
        "matched": not missing,
        "exact": exact,
        "copied_sample": exact and bool(right.strip()),
        "missing_markers": missing,
        "generated_chars": len(left),
        "gold_chars": len(right),
    }


def default_human_instruction() -> str:
    return ""


def _strip_reply(text: str) -> str:
    raw = (text or "").strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-zA-Z0-9_-]*\s*\n?", "", raw)
        if raw.endswith("```"):
            raw = raw[: raw.rfind("```")].rstrip()
    return raw.strip()


def _heading_key(line: str) -> str:
    key = line.strip().lstrip("#").strip("*").strip().strip(":").strip()
    lowered = key.lower()
    if lowered in {item.lower() for item in GENERATOR_SECTIONS}:
        for item in GENERATOR_SECTIONS:
            if item.lower() == lowered:
                return item
    return HEADING_ALIASES.get(lowered, "")


def extract_sections(text: str, owned: tuple[str, ...]) -> dict[str, str]:
    """Pull named gold-format headings from a live reply. Does not read sample/."""
    body = _strip_reply(text)
    found: dict[str, str] = {}
    current = ""
    buf: list[str] = []

    def flush() -> None:
        nonlocal current, buf
        if current:
            found[current] = "\n".join(buf).strip()
        buf = []

    for line in body.splitlines():
        matched = _heading_key(line)
        if matched:
            flush()
            current = matched
            continue
        if current:
            buf.append(line)
    flush()
    if not found and owned:
        found[owned[0]] = body
    return {key: value for key, value in found.items() if value}


def assemble_generator_instruction(parts: dict[str, str]) -> tuple[str, list[str]]:
    """Host join of live section bodies. Never fills gaps from sample/."""
    blocks: list[str] = []
    missing: list[str] = []
    for heading in GENERATOR_SECTIONS:
        body = (parts.get(heading) or "").strip()
        if heading == "Human asks" and not body:
            continue
        if heading == "Frame":
            if body:
                blocks.append(body)
            else:
                missing.append(heading)
                blocks.append("[missing: Frame — video.promptengineer]")
            blocks.append("")
            continue
        blocks.append(heading)
        if body:
            blocks.append(body)
        else:
            missing.append(heading)
            blocks.append(f"[missing: {heading}]")
        blocks.append("")
    text = "\n".join(blocks).strip() + "\n"
    return text, missing


def _assert_no_gold_body(message: str) -> None:
    lower = (message or "").lower()
    if any(probe.lower() in lower for probe in GOLD_BODY_PROBES):
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="sample body must not be sent to agents")


def call_agent(chat_fn: ChatFn | None, agent_id: str, message: str) -> dict[str, Any]:
    """One host Chat hop. Does not enable tools, network, or production."""
    if chat_fn is None:
        return {
            "live": False,
            "agent_id": agent_id,
            "reply": "",
            "provider": "",
            "error": "chat_fn missing — no live call",
        }
    try:
        result = chat_fn(agent_id, message)
    except Exception as exc:  # noqa: BLE001 — record the hop, do not invent a craft reply
        return {
            "live": True,
            "agent_id": agent_id,
            "reply": "",
            "provider": "",
            "error": f"{type(exc).__name__}: {exc}",
        }
    payload = result if isinstance(result, dict) else {}
    reply = str(payload.get("reply") or "")
    return {
        "live": True,
        "agent_id": str(payload.get("agent_id") or agent_id),
        "reply": reply,
        "provider": str(payload.get("provider") or ""),
        "error": "" if reply.strip() else "empty reply",
        "digest": str(payload.get("digest") or ""),
    }


def _induce_envelope(
    *,
    brief_id: str,
    agent_id: str,
    why: str,
    headings: tuple[str, ...],
    human: str,
    direction: str = "",
    freeze: str = "",
    human_answers: list[str] | None = None,
) -> str:
    heading_block = ""
    if agent_id == "video.creativedirector":
        heading_block = (
            "return_schema=creative_direction.v1. Write heading 'Creative direction' then: "
            "THESIS (what the piece is), WHY (grounded in the human brief + pack sources, not a gold file), "
            "open ASK_HUMAN lines for locks the human did not specify. "
            "Do not invent mole sites as human facts.\n"
        )
    elif agent_id == "video.aiqaconsistency":
        heading_block = (
            "return_schema=consistency_check.v1. Check later crafts against the freeze. "
            "Emit conflicts. ASK_HUMAN if identity cannot be locked. Do not generate the prompt.\n"
        )
    elif headings:
        heading_lines = "\n".join(f"- {item}" for item in headings)
        heading_block = (
            "return_schema=heading_prose.v1. Each owned heading on its own line, then in-role sentences.\n"
            f"Owned headings:\n{heading_lines}\n"
        )
    else:
        heading_block = (
            "return_schema=critique_bus.v1. Rows: from_id, to_id, severity (blocker|major|minor|nit), "
            "artifact_ref, claim, evidence_refs, correlation_id. Not the closer.\n"
        )
    extras = []
    if direction.strip():
        extras.append("PRIOR CREATIVE DIRECTION (cite, do not contradict without a conflict row):\n" + direction.strip()[:1200])
    if freeze.strip():
        extras.append("IDENTITY FREEZE (must hold across beats; do not morph):\n" + freeze.strip()[:1200])
    if human_answers:
        extras.append("HUMAN ANSWERS:\n" + "\n".join(f"- {item}" for item in human_answers[:8]))
    extra_block = ("\n".join(extras) + "\n") if extras else ""
    return (
        "CASOPS INDUCE kind=casops.instruction_pass.video_collab.v1 "
        f"brief_id={brief_id} from_agent_id={FIRST_CALLED} to_agent_id={agent_id} "
        "must_cite=true instruction_authority=false consolidation_owner=video.promptengineer\n"
        f"You are the domain expert {agent_id}. The human brief is high-level; you generate OPTIONS at this decision point.\n"
        f"You are not first-called. Do not reply to the operator. Do not spawn peers.\n"
        f"Objective: {why}\n"
        "Emit:\nTHINKING: <your expert reasoning>\n"
        "OPTION 1: <choice> — <why>\nOPTION 2: <choice> — <why>\n"
        "RECOMMEND: 1\n"
        "DECIDE_BY: human   (or a parent agent id, or a lower agent id if they should generate sub-options)\n"
        "If DECIDE_BY is a lower expert, also emit induce_call: <agent_id> because <they should expand options>.\n"
        "If DECIDE_BY is human, the node shows options for the human to pick; you may also emit ASK_HUMAN: <question>.\n"
        f"{heading_block}"
        "If you need a peer craft you do not own, emit: induce_call: <agent_id> because <reason>\n"
        "forbidden: rewrite owner SPEC; call undeclared tools; widen scope; reply to operator; "
        "absorb exclusive craft; open a second control plane; enable network/plugins/production/memory writes; "
        "claim 4K; copy sample/; emit Output schema JSON; treat host-invented gold facts as human locks.\n"
        f"{extra_block}"
        f"Human brief (high-level only):\n{human[:400]}"
    )


def negatives_from_critic(text: str) -> str:
    claims: list[str] = []
    for line in (text or "").splitlines():
        stripped = line.strip()
        low = stripped.lower()
        if low.startswith("claim:") or low.startswith("avoid:"):
            claims.append(stripped.split(":", 1)[-1].strip())
    body = _strip_reply(text)
    extracted = extract_sections(body, ("Negatives",))
    if extracted.get("Negatives"):
        return extracted["Negatives"]
    blob = " ".join(claims).strip()
    if "no beauty filter" not in (blob or body).lower() and "no beauty filter" in body.lower():
        blob = (blob + " no beauty filter, no airbrushed skin").strip()
    if "no beauty filter" in body.lower() and "no airbrushed skin" in body.lower() and not claims:
        return "no beauty filter, no airbrushed skin"
    if claims:
        joined = "; ".join(claims)
        if "no beauty filter" not in joined.lower():
            joined = "no beauty filter, no airbrushed skin; " + joined
        return joined
    if "no beauty filter" in body.lower():
        return "no beauty filter, no airbrushed skin"
    return ""


def collect_conflicts(section_parts: dict[str, str]) -> list[str]:
    conflicts: list[str] = []
    cam = (section_parts.get("Camera lock") or "").lower()
    beats = " ".join(
        section_parts.get(item) or ""
        for item in GENERATOR_SECTIONS
        if "s |" in item
    ).lower()
    if "orbit" in beats and ("no orbit" in cam or "no traditional" in cam or "orbit" in cam and "no" in cam):
        conflicts.append(
            "Director beats mention orbit while cameraoperator owns the motor and forbids orbit — preserved; motor stays with video.cameraoperator."
        )
    light = (section_parts.get("Light") or "").lower()
    if "ring" in light and "no ring" not in light:
        conflicts.append("Cinematographer lighting may include ring; critic/lock forbid ring-light — preserved.")
    return conflicts


def _first_called_pass1(human: str, human_answers: list[str] | None = None) -> str:
    heading_lines = "\n".join(f"- {item}" for item in FIRST_CALLED_HEADINGS)
    answers = ""
    if human_answers:
        answers = "HUMAN ANSWERS TO PRIOR ASKS:\n" + "\n".join(f"- {item}" for item in human_answers[:8]) + "\n"
    return (
        "CASOPS INSTRUCTION PASS kind=casops.instruction_pass.video_collab.v1 "
        "pass_id=pass_01 first_called=video.promptengineer "
        "correlation_id=corr_asain_beauty_001 consolidation_owner=video.promptengineer "
        "must_cite=true instruction_authority=false next_instruction_required=true\n"
        "The human brief is HIGH-LEVEL only. Do not demand moles, lighting recipes, or clip grammar from Create Project.\n"
        "You are the orchestrating expert. At this decision point emit:\n"
        "THINKING: ...\nOPTION 1: induce video.creativedirector first — why\nOPTION 2: ...\n"
        "RECOMMEND: 1\nDECIDE_BY: human\n"
        "Also emit induce_call lines for the experts you recommend (host dispatches). "
        "Each downstream expert will generate THEIR options; you (or the human) choose among them.\n"
        f"Owned headings this hop if you already have a chosen frame:\n{heading_lines}\n"
        "Do not copy sample/. Do not claim 4K. Do not write the final generator novel yourself.\n"
        f"{answers}"
        f"Human brief (high-level only):\n{human[:400]}"
    )


def _first_called_fanin(human: str, members: list[dict[str, Any]], conflicts: list[str]) -> str:
    rows = []
    for row in members:
        headings = ", ".join(row.get("headings") or [])
        snippet = (row.get("reply") or row.get("error") or "(empty)")[:400]
        rows.append(
            f"- brief_id={row.get('brief_id')} agent_id={row['agent_id']} headings=[{headings}] "
            f"live={row.get('live')} provider={row.get('provider') or '-'}\n  {snippet}"
        )
    joined = "\n".join(rows)
    conflict_block = "\n".join(f"- {item}" for item in conflicts) if conflicts else "(none — still list empty conflicts[])"
    return (
        "CASOPS FAN-IN pass_01 first_called=video.promptengineer parent_pass_id=null. "
        "The host assembles member English sections into the output file "
        "(agent max_output_tokens=1024 cannot hold the full novel). "
        "Cite each member artifact_ref. Preserve conflicts; do not silently pick a winner. "
        "Emit next_instruction in the same envelope (pass_02, parent_pass_id=pass_01, first_called=video.promptengineer). "
        "Do not paste a sample file. Do not call a vendor. Do not emit generation_prompt_spec JSON as the deliverable.\n"
        f"Human instruction:\n{human[:500]}\n\n"
        f"MEMBER RETURNS:\n{joined[:3500]}\n\n"
        f"CONFLICTS:\n{conflict_block}"
    )


def _node(
    agent_id: str,
    *,
    kind: str,
    x: int,
    y: int,
    reason: str,
    outputs: list[str],
    inputs: list[str],
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    data = {
        "kind": "agent",
        "label": agent_id,
        "agent_id": agent_id,
        "reason": reason,
        "io": {"inputs": inputs, "outputs": outputs},
    }
    if extra:
        data.update(extra)
    return {
        "id": f"agent-{agent_id.replace('.', '-')}",
        "type": "agent",
        "position": {"x": x, "y": y},
        "data": data,
    }


def _decision_extra(parsed: dict[str, Any], chosen: str) -> dict[str, Any]:
    return {
        "thinking": str(parsed.get("thinking") or ""),
        "options": parsed.get("options") if isinstance(parsed.get("options"), list) else [],
        "recommend": str(parsed.get("recommend") or ""),
        "decide_by": str(parsed.get("decide_by") or ""),
        "chosen": chosen,
    }


def _option_labels(options: list[Any]) -> dict[str, str]:
    labels: dict[str, str] = {}
    for row in options:
        if not isinstance(row, dict):
            continue
        option_id = str(row.get("id") or "").strip()
        if option_id:
            labels[option_id] = str(row.get("label") or "").strip()
    return labels


def _human_ask_item(items: list[Any], agent_id: str) -> dict[str, Any] | None:
    found: dict[str, Any] | None = None
    for item in items:
        if isinstance(item, dict) and item.get("kind") == "human_ask" and item.get("from") == agent_id:
            found = item
    return found


def _is_disjoint_human_lock(agent_id: str, option_id: str, graph_options: list[Any], items: list[Any]) -> bool:
    """True when ASK option ids collide with a different expert-decision namespace."""
    ask = _human_ask_item(items, agent_id)
    if not ask:
        return False
    parsed = parse_emitted_instructions(str(ask.get("text") or ""))
    ask_labels = _option_labels(parsed.get("options") or [])
    graph_labels = _option_labels(graph_options)
    if option_id not in ask_labels:
        return False
    if option_id not in graph_labels:
        return True
    return ask_labels[option_id] != graph_labels[option_id]


def _apply_pick(section_parts: dict[str, str], agent_id: str, parsed: dict[str, Any], choice: str | None) -> None:
    pick = pick_option(parsed, choice)
    if not pick:
        return
    craft = str(pick.get("craft") or "").strip()
    text = craft or f"{pick.get('label') or ''}\n{pick.get('why') or ''}".strip()
    if not text:
        return
    if agent_id == "video.creativedirector":
        section_parts["Creative direction"] = text
        return
    if agent_id == "video.continuity":
        for heading, body in split_continuity_craft(craft or text).items():
            if body:
                section_parts[heading] = body
        return
    if agent_id == "video.promptengineer":
        frame, _, sound = text.partition("\n")
        if frame.strip():
            section_parts["Frame"] = frame.strip()
        if sound.strip():
            section_parts["Sound"] = sound.strip()
        return
    heads = craft_headings_for(agent_id)
    if heads:
        current = section_parts.get(heads[0]) or ""
        if not current or len(current) < len(text):
            section_parts[heads[0]] = text


def apply_project_choices(
    root: Path,
    slug: str,
    record: dict[str, Any],
    picks: dict[str, str],
    *,
    dry_run: bool,
) -> dict[str, Any]:
    """Human/parent picks among already-generated expert options. Does not re-call agents."""
    if "host_service" in picks:
        gate = "continue" if str(picks.get("host_service")) == "2" else "stop"
        return apply_autopilot_cycle(root, slug, record, gate, dry_run=dry_run)
    gold_path = sample_prompt_path(root, slug)
    gold = gold_path.read_text(encoding="utf-8") if gold_path.is_file() else ""
    nodes = list((record.get("graph") or {}).get("nodes") or [])
    edges = list((record.get("graph") or {}).get("edges") or [])
    store = load_comms(root, slug)
    items = [dict(row) for row in (store.get("items") or []) if isinstance(row, dict)]
    locks = {str(key): str(value) for key, value in (store.get("locks") or {}).items() if str(key) and str(value)}
    autopilot = dict(store.get("autopilot") or {})
    cycle_locks = {
        str(key): str(value)
        for key, value in (autopilot.get("cycle_locks") or {}).items()
        if str(key) and str(value)
    }
    node_options: dict[str, list[Any]] = {}
    for node in nodes:
        if not isinstance(node, dict) or not isinstance(node.get("data"), dict):
            continue
        agent_id = str(node["data"].get("agent_id") or "")
        options = node["data"].get("options") if isinstance(node["data"].get("options"), list) else []
        if agent_id:
            node_options[agent_id] = options
    lock_picks: dict[str, str] = {}
    expert_picks: dict[str, str] = {}
    for agent_id, option_id in picks.items():
        if str(option_id).startswith("p3-"):
            cycle_locks[agent_id] = option_id
            lock_picks[agent_id] = option_id
        elif _is_disjoint_human_lock(agent_id, option_id, node_options.get(agent_id) or [], items):
            lock_picks[agent_id] = option_id
        else:
            expert_picks[agent_id] = option_id
    domain_lock_picks = {key: value for key, value in lock_picks.items() if not str(value).startswith("p3-")}
    locks.update(domain_lock_picks)
    autopilot["cycle_locks"] = cycle_locks
    if {"video.critic", "video.continuity"} <= set(cycle_locks) and autopilot.get("cycle") == "open":
        autopilot["cycle"] = "ready"
    section_parts: dict[str, str] = {}
    for node in nodes:
        if not isinstance(node, dict) or not isinstance(node.get("data"), dict):
            continue
        data = dict(node["data"])
        agent_id = str(data.get("agent_id") or "")
        options = data.get("options") if isinstance(data.get("options"), list) else []
        parsed = {
            "options": options,
            "recommend": str(data.get("recommend") or ""),
            "thinking": str(data.get("thinking") or ""),
            "decide_by": str(data.get("decide_by") or ""),
        }
        if agent_id in expert_picks:
            data["chosen"] = expert_picks[agent_id]
            node["data"] = data
        if agent_id in lock_picks:
            continue
        _apply_pick(section_parts, agent_id, parsed, data.get("chosen") or expert_picks.get(agent_id))
        if data.get("thinking") and agent_id == "video.creativedirector" and "Creative direction" not in section_parts:
            section_parts["Creative direction"] = str(data.get("thinking") or "")
    missing_sections: list[str] = []
    assembled_clip = None
    if lock_picks:
        walk = walkthrough_module(slug)
        from casops.video_prompt.assemble import clip_from_walkthrough, project_clip

        assembled_clip = clip_from_walkthrough(walk, locks=locks, cycle_locks=cycle_locks)
        from casops.video_prompt.patch import apply_choice_overlays, overlays_from_comms

        overlay_result = apply_choice_overlays(assembled_clip, overlays_from_comms(items))
        assembled_clip = overlay_result["clip"]
        output_text = project_clip(assembled_clip)
        for agent_id, option_id in lock_picks.items():
            text = walk.human_lock_choice_text(agent_id, option_id)
            if not text:
                continue
            updated = False
            cycle_pick = str(option_id).startswith("p3-")
            for item in reversed(items):
                if item.get("kind") != "choice" or item.get("from") != "human_operator" or item.get("to") != agent_id:
                    continue
                if cycle_pick and item.get("pass_id") != "pass_03":
                    continue
                item["text"] = text
                updated = True
                break
            if not updated:
                items.append(
                    {
                        "id": f"comm-lock-{agent_id.replace('.', '-')}-{option_id}",
                        "node_id": "human-ask",
                        "from": "human_operator",
                        "to": agent_id,
                        "kind": "choice",
                        "text": text,
                        "pass_id": "pass_03" if cycle_pick else "pass_01",
                        "live": False,
                    }
                )
    else:
        output_text, missing_sections = assemble_generator_instruction(section_parts)
    report = validate_prompt(output_text, gold) if gold else {
        "matched": False,
        "exact": False,
        "copied_sample": False,
        "missing_markers": [],
        "generated_chars": len(output_text),
        "gold_chars": 0,
    }
    report["missing_sections"] = missing_sections
    out_rel = f"project/{slug}/output/{slug}-prompt.txt"
    copied = bool(report.get("copied_sample"))
    decisions = [dict(row) for row in (store.get("decisions") or []) if isinstance(row, dict)]
    for row in decisions:
        agent_id = str(row.get("agent_id") or "")
        if agent_id in expert_picks:
            row["chosen"] = expert_picks[agent_id]
            row["selected_by"] = "human_operator"
            row["select_reason"] = ""
    if autopilot.get("cycle") == "ready" and not any(
        item.get("kind") == "next_instruction" and item.get("pass_id") == "pass_03" for item in items
    ):
        seq = len(items) + 1
        items.append(
            {
                "id": f"comm-{seq:04d}",
                "node_id": "agent-video-promptengineer",
                "from": FIRST_CALLED,
                "to": FIRST_CALLED,
                "kind": "next_instruction",
                "text": (
                    "next_instruction pass_03. Host re-assembled after clip review. "
                    "Click Grok Imagine to generate again. Folder max_refinement_count stays 0."
                ),
                "pass_id": "pass_03",
                "live": False,
                "input_tags": [],
                "output_tags": [],
            }
        )
        items.append(
            {
                "id": f"comm-{seq + 1:04d}",
                "node_id": "output-prompt",
                "from": "host_service",
                "to": "output-prompt",
                "kind": "assembled",
                "text": "Host-joined pass_03 generator instruction. First-called did not write the novel.",
                "pass_id": "pass_03",
                "live": False,
                "input_tags": [],
                "output_tags": [],
            }
        )
    if not dry_run and not copied:
        out_path = output_prompt_path(root, slug)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        if assembled_clip is not None:
            from casops.video_prompt.assemble import write_clip_files

            write_clip_files(out_path.parent, slug, assembled_clip)
        else:
            out_path.write_text(output_text if output_text.endswith("\n") else output_text + "\n", encoding="utf-8")
        record["graph"] = {"nodes": nodes, "edges": edges}
        write_project(root, record, dry_run=False, create=False)
        for node in nodes:
            data = node.get("data") if isinstance(node, dict) else None
            if isinstance(data, dict) and data.get("kind") == "output":
                data["brief"] = output_text[:280]
        save_comms(
            root,
            slug,
            {
                "items": items,
                "decisions": decisions,
                "walkthrough": store.get("walkthrough") or "",
                "note": store.get("note") or "",
                "locks": locks,
                "autopilot": autopilot,
            },
            dry_run=False,
        )
    return {
        "honesty": "CHARACTERIZATION",
        "dry_run": dry_run,
        "saved": (not dry_run) and (not copied),
        "first_called": FIRST_CALLED,
        "status": "ok",
        "graph": {"nodes": nodes, "edges": edges},
        "comms": {
            "schema_version": COMMS_SCHEMA,
            "project_id": slug,
            "items": items,
            "decisions": decisions,
            "locks": locks,
            "autopilot": autopilot,
        },
        "output_path": out_rel,
        "validation": report,
        "note": "Applied human/parent option picks to existing expert suggestions. Did not re-call agents. Not an eval PASS.",
    }


def apply_autopilot_cycle(
    root: Path,
    slug: str,
    record: dict[str, Any],
    gate: str,
    *,
    dry_run: bool,
) -> dict[str, Any]:
    """Host-owned pass_03 gate. Does not raise folder max_refinement_count. Does not call Imagine."""
    walk = walkthrough_module(slug)
    CYCLE_ASKS = walk.CYCLE_ASKS
    CYCLE_GATE = walk.CYCLE_GATE
    _ask_block = walk._ask_block
    _choice_block = walk._choice_block

    store = load_comms(root, slug)
    items = [dict(row) for row in (store.get("items") or []) if isinstance(row, dict)]
    autopilot = dict(store.get("autopilot") or {})
    cycles = int(autopilot.get("cycles") or 0)
    action = "continue" if gate == "continue" else "stop"
    if action == "continue" and cycles >= 1:
        action = "stop"
    overlay = dict(CYCLE_GATE)
    overlay["chosen"] = "2" if action == "continue" else "1"
    seq = len(items) + 1
    items.append(
        {
            "id": f"comm-{seq:04d}",
            "node_id": "human-ask",
            "from": "host_service",
            "to": "human_operator",
            "kind": "human_ask",
            "text": _ask_block(CYCLE_GATE),
            "pass_id": "pass_03",
            "live": False,
            "input_tags": [],
            "output_tags": [],
        }
    )
    items.append(
        {
            "id": f"comm-{seq + 1:04d}",
            "node_id": "human-ask",
            "from": "human_operator",
            "to": "host_service",
            "kind": "choice",
            "text": _choice_block(overlay),
            "pass_id": "pass_03",
            "live": False,
            "input_tags": [],
            "output_tags": [],
        }
    )
    seq = len(items)
    cycle_from = {str(row["from"]) for row in CYCLE_ASKS}
    if action == "continue":
        for ask in CYCLE_ASKS:
            seq += 1
            items.append(
                {
                    "id": f"comm-{seq:04d}",
                    "node_id": "human-ask",
                    "from": ask["from"],
                    "to": "human_operator",
                    "kind": "human_ask",
                    "text": _ask_block(ask),
                    "pass_id": "pass_03",
                    "live": False,
                    "input_tags": [],
                    "output_tags": [],
                }
            )
        autopilot["cycle"] = "open"
        autopilot["cycles"] = cycles + 1
        autopilot["cycle_locks"] = {}
    else:
        items = [
            item
            for item in items
            if not (
                item.get("pass_id") == "pass_03"
                and item.get("kind") == "human_ask"
                and item.get("from") in cycle_from
            )
        ]
        autopilot["cycle"] = "stopped"
    graph = record.get("graph") or {"nodes": [], "edges": []}
    if not dry_run:
        save_comms(
            root,
            slug,
            {
                "items": items,
                "decisions": store.get("decisions") or [],
                "walkthrough": store.get("walkthrough") or "",
                "note": store.get("note") or "",
                "locks": store.get("locks") or {},
                "autopilot": autopilot,
            },
            dry_run=False,
        )
    return {
        "honesty": "CHARACTERIZATION",
        "dry_run": dry_run,
        "saved": not dry_run,
        "first_called": FIRST_CALLED,
        "status": "ok",
        "graph": graph,
        "comms": {
            "schema_version": COMMS_SCHEMA,
            "project_id": slug,
            "items": items,
            "decisions": store.get("decisions") or [],
            "locks": store.get("locks") or {},
            "autopilot": autopilot,
        },
        "note": "Host-owned Auto Pilot cycle gate. Did not re-call agents. Did not call Imagine. Not an eval PASS.",
    }


def run_asain_beauty_workflow(
    root: Path,
    slug: str,
    *,
    first_instruction: str,
    dry_run: bool,
    agents_root: Path | None = None,
    chat_fn: ChatFn | None = None,
    human_answers: list[str] | None = None,
    choices: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Host-mediated instruction pass. Agents emit induce_calls and ASK_HUMAN. Does not copy sample/."""
    normalize_slug(slug)
    record = read_project(root, slug)
    gold_path = sample_prompt_path(root, slug)
    gold = gold_path.read_text(encoding="utf-8") if gold_path.is_file() else ""
    prompt = human_brief_only(first_instruction, record)
    if not prompt:
        prompt = human_brief_only("", record) or slug
    answers = [str(item).strip() for item in (human_answers or []) if str(item).strip()]
    picks = {str(key): str(value) for key, value in (choices or {}).items() if str(key) and str(value)}
    if picks:
        prior_nodes = (record.get("graph") or {}).get("nodes") or []
        if any(isinstance(node, dict) and isinstance(node.get("data"), dict) and node["data"].get("options") for node in prior_nodes):
            return apply_project_choices(root, slug, record, picks, dry_run=dry_run)

    required_ids = [FIRST_CALLED, *[row[0] for row in INDUCE_ROSTER]]
    missing_agents: list[str] = []
    if agents_root is not None:
        for agent_id in required_ids:
            if not (Path(agents_root) / agent_id / "agent_spec.json").is_file():
                missing_agents.append(agent_id)
    if missing_agents:
        raise CasopsError(ErrorCode.INH_PARENT_MISSING, detail="missing agents: " + ",".join(missing_agents))

    prior_comms = load_comms(root, slug)
    items: list[dict[str, Any]] = []
    seq = 0

    def add(
        *,
        node_id: str,
        from_id: str,
        to_id: str,
        kind: str,
        text: str,
        inputs: list[dict[str, str]],
        outputs: list[dict[str, str]],
        pass_id: str,
    ) -> dict[str, Any]:
        nonlocal seq
        seq += 1
        comm_id = f"comm-{seq:04d}"
        entry = {
            "id": comm_id,
            "node_id": node_id,
            "from": from_id,
            "to": to_id,
            "kind": kind,
            "text": text,
            "input_tags": inputs,
            "output_tags": outputs,
            "pass_id": pass_id,
            "created_at": _now(),
            "live": False,
            "provider": "",
            "error": "",
        }
        items.append(entry)
        return entry

    def stamp(entry: dict[str, Any], hop: dict[str, Any]) -> dict[str, Any]:
        entry["live"] = bool(hop.get("live"))
        entry["provider"] = str(hop.get("provider") or "")
        entry["error"] = str(hop.get("error") or "")
        entry["digest"] = str(hop.get("digest") or "")
        return entry

    human = add(
        node_id="create-project",
        from_id="human_operator",
        to_id="create-project",
        kind="instruction",
        text=prompt,
        inputs=[],
        outputs=[],
        pass_id="pass_01",
    )
    for special_id, special_task in (
        (
            "specials.intent-analysis-agent",
            "Auto Pilot: interpret the human draft only. Return locution, illocution, triggerability, "
            "OPTIONS for thesis class, RECOMMEND, DECIDE_BY. Do not write shot grammar. Do not copy sample/.",
        ),
        (
            "specials.general-creative-agent",
            "Auto Pilot: from the intent reading, propose 3 campaign concepts as OPTIONS. "
            "DECIDE_BY: video.promptengineer. Do not write the generator novel. Do not copy sample/.",
        ),
    ):
        if agents_root is not None and not (Path(agents_root) / special_id / "agent_spec.json").is_file():
            continue
        spec_node = f"agent-{special_id.replace('.', '-')}"
        spec_msg = f"{special_task}\n\nHuman draft:\n{prompt}"
        _assert_no_gold_body(spec_msg)
        brief = add(
            node_id="create-project",
            from_id="create-project",
            to_id=special_id,
            kind="instruction",
            text=spec_msg,
            inputs=[_tag(slug, "create-project", human["id"], "human-draft")],
            outputs=[_tag(slug, spec_node, "comm-pending", special_id)],
            pass_id="pass_01",
        )
        hop = call_agent(chat_fn, special_id, spec_msg)
        add(
            node_id=spec_node,
            from_id=special_id,
            to_id="create-project",
            kind="return",
            text=hop.get("reply") or hop.get("error") or "(empty live reply)",
            inputs=[_tag(slug, "create-project", brief["id"], "autopilot")],
            outputs=[],
            pass_id="pass_01",
        )
        stamp(items[-1], hop)
        if hop.get("live"):
            items[-1]["live"] = True
    launch = add(
        node_id="create-project",
        from_id="create-project",
        to_id=FIRST_CALLED,
        kind="instruction",
        text=(
            "CASOPS INSTRUCTION PASS kind=casops.instruction_pass.video_collab.v1 "
            f"first_called={FIRST_CALLED} correlation_id=corr_asain_beauty_001. "
            "Stay first-called. Induce related agents through the host. Each member returns English "
            "section prose. The host assembles those live sections into the output file. "
            "Generate the next instruction in this same envelope. Do not copy sample/. Do not call a vendor."
        ),
        inputs=[_tag(slug, "create-project", human["id"], "human-first-instruction")],
        outputs=[_tag(slug, f"agent-{FIRST_CALLED.replace('.', '-')}", "comm-pending", FIRST_CALLED)],
        pass_id="pass_01",
    )
    first_node = f"agent-{FIRST_CALLED.replace('.', '-')}"
    received = add(
        node_id=first_node,
        from_id="create-project",
        to_id=FIRST_CALLED,
        kind="instruction",
        text=launch["text"],
        inputs=[_tag(slug, "create-project", launch["id"], "launch")],
        outputs=[],
        pass_id="pass_01",
    )

    first_message = _first_called_pass1(prompt, answers)
    _assert_no_gold_body(first_message)
    hop_first = call_agent(chat_fn, FIRST_CALLED, first_message)
    received["text"] = hop_first.get("reply") or received["text"]
    stamp(received, hop_first)
    first_extracted = extract_sections(hop_first.get("reply") or "", FIRST_CALLED_HEADINGS)
    if hop_first.get("reply") and not any(item in first_extracted for item in FIRST_CALLED_HEADINGS):
        repair_text = (
            "Re-emit induce_call lines (induce_call: video.creativedirector because ...) "
            "and ASK_HUMAN lines if locks are missing. Also Frame and Sound headings as English. "
            "No Output schema JSON. Do not copy sample/. Do not invent gold-file moles as human facts."
        )
        _assert_no_gold_body(repair_text)
        hop_first_repair = call_agent(chat_fn, FIRST_CALLED, repair_text)
        repair_entry = add(
            node_id=first_node,
            from_id="host_service",
            to_id=FIRST_CALLED,
            kind="repair",
            text=repair_text,
            inputs=[_tag(slug, first_node, received["id"], "pass-01")],
            outputs=[],
            pass_id="pass_01",
        )
        stamp(repair_entry, hop_first_repair)
        live_hops_first_repair = 1 if hop_first_repair.get("live") else 0
        repaired_reply = hop_first_repair.get("reply") or ""
        if repaired_reply:
            repaired_comm = add(
                node_id=first_node,
                from_id=FIRST_CALLED,
                to_id="create-project",
                kind="return",
                text=repaired_reply,
                inputs=[_tag(slug, first_node, repair_entry["id"], "repair")],
                outputs=[],
                pass_id="pass_01",
            )
            stamp(repaired_comm, hop_first_repair)
            first_extracted = extract_sections(repaired_reply, FIRST_CALLED_HEADINGS)
            received_id_for_sections = repaired_comm["id"]
        else:
            received_id_for_sections = received["id"]
    else:
        live_hops_first_repair = 0
        received_id_for_sections = received["id"]

    section_parts: dict[str, str] = {}
    section_sources: dict[str, str] = {}
    for heading, body in first_extracted.items():
        section_parts[heading] = body
        section_sources[heading] = received_id_for_sections

    first_parsed = parse_emitted_instructions((received.get("text") if received_id_for_sections == received["id"] else "") or hop_first.get("reply") or "")
    if received_id_for_sections != received["id"]:
        first_parsed = parse_emitted_instructions(next((item["text"] for item in items if item["id"] == received_id_for_sections), hop_first.get("reply") or ""))
    decisions: dict[str, dict[str, Any]] = {FIRST_CALLED: first_parsed}
    _apply_pick(section_parts, FIRST_CALLED, first_parsed, picks.get(FIRST_CALLED))
    emitted_calls = first_parsed.get("induce_calls") or []
    human_asks: list[str] = list(first_parsed.get("human_asks") or [])
    dispatch_ids = [row["agent_id"] for row in emitted_calls if row.get("agent_id") != FIRST_CALLED]
    why_by_id = {row["agent_id"]: row.get("why") or "" for row in emitted_calls}
    for agent_id, _brief_id, why, _heads in INDUCE_ROSTER:
        if agent_id not in dispatch_ids:
            dispatch_ids.append(agent_id)
            why_by_id.setdefault(agent_id, why)
    if not dispatch_ids:
        dispatch_ids = [agent_id for agent_id in named_agent_ids(prompt, agents_root) if agent_id != FIRST_CALLED]
        add(
            node_id=first_node,
            from_id="host_service",
            to_id=FIRST_CALLED,
            kind="note",
            text="First-called did not emit induce_call lines. Host dispatched agents named in the human instruction only — not a gold-file roster.",
            inputs=[_tag(slug, first_node, received["id"], "pass-01")],
            outputs=[],
            pass_id="pass_01",
        )
    dispatch_ids = order_induce(dispatch_ids)[:7]
    if agents_root is not None:
        dispatch_ids = [agent_id for agent_id in dispatch_ids if (Path(agents_root) / agent_id / "agent_spec.json").is_file()]

    member_summaries: list[dict[str, Any]] = []
    live_hops = (
        (1 if hop_first.get("live") else 0)
        + live_hops_first_repair
        + sum(1 for item in items if item.get("live") and str(item.get("from") or "").startswith("specials."))
    )
    direction_text = ""
    freeze_text = ""
    extra_queue: list[tuple[str, str]] = []
    for index, agent_id in enumerate(dispatch_ids, start=1):
        why = why_by_id.get(agent_id) or f"In-role craft for {agent_id} as named by instruction."
        headings = craft_headings_for(agent_id)
        brief_id = f"br_asain_{index:02d}_{agent_id.split('.')[-1][:12]}"
        node_id = f"agent-{agent_id.replace('.', '-')}"
        brief_text = _induce_envelope(
            brief_id=brief_id,
            agent_id=agent_id,
            why=why,
            headings=headings,
            human=prompt,
            direction=direction_text,
            freeze=freeze_text,
            human_answers=answers,
        )
        _assert_no_gold_body(brief_text)
        brief = add(
            node_id=first_node,
            from_id=FIRST_CALLED,
            to_id=agent_id,
            kind="induce",
            text=brief_text,
            inputs=[_tag(slug, first_node, received["id"], "pass-01")],
            outputs=[_tag(slug, node_id, "comm-pending", agent_id)],
            pass_id="pass_01",
        )
        hop = call_agent(chat_fn, agent_id, brief_text)
        if hop.get("live"):
            live_hops += 1
        reply_text = hop.get("reply") or hop.get("error") or "(empty live reply)"
        ret = add(
            node_id=node_id,
            from_id=agent_id,
            to_id=FIRST_CALLED,
            kind="return",
            text=reply_text,
            inputs=[_tag(slug, first_node, brief["id"], brief_id)],
            outputs=[_tag(slug, first_node, "comm-pending", "fan-in")],
            pass_id="pass_01",
        )
        stamp(ret, hop)
        extracted = extract_sections(hop.get("reply") or "", headings) if headings else {}
        if headings and hop.get("reply") and not any(item in extracted for item in headings):
            heading_lines = "\n".join(f"- {item}" for item in headings)
            repair_text = (
                f"CASOPS REPAIR brief_id={brief_id} to_agent_id={agent_id}. "
                "Your last reply had no required headings. Re-emit ONLY in-role English prose.\n"
                f"{heading_lines}\n"
                "No Output schema JSON, no fences, no generation_prompt_spec. Do not copy sample/. "
                "Do not absorb exclusive crafts."
            )
            _assert_no_gold_body(repair_text)
            hop_repair = call_agent(chat_fn, agent_id, repair_text)
            if hop_repair.get("live"):
                live_hops += 1
            repair_entry = add(
                node_id=node_id,
                from_id="host_service",
                to_id=agent_id,
                kind="repair",
                text=repair_text,
                inputs=[_tag(slug, node_id, ret["id"], "return")],
                outputs=[],
                pass_id="pass_01",
            )
            stamp(repair_entry, hop_repair)
            if hop_repair.get("reply"):
                ret2 = add(
                    node_id=node_id,
                    from_id=agent_id,
                    to_id=FIRST_CALLED,
                    kind="return",
                    text=hop_repair.get("reply") or "",
                    inputs=[_tag(slug, node_id, repair_entry["id"], "repair")],
                    outputs=[_tag(slug, first_node, "comm-pending", "fan-in")],
                    pass_id="pass_01",
                )
                stamp(ret2, hop_repair)
                extracted = extract_sections(hop_repair.get("reply") or "", headings)
                ret = ret2
        if agent_id == "video.critic":
            neg = negatives_from_critic(ret.get("text") or hop.get("reply") or "")
            if neg and "Negatives" not in section_parts:
                section_parts["Negatives"] = neg
                section_sources["Negatives"] = ret["id"]
        for heading, body in extracted.items():
            if heading in headings or heading not in section_parts:
                section_parts[heading] = body
                section_sources[heading] = ret["id"]
        member_summaries.append(
            {
                "brief_id": brief_id,
                "agent_id": agent_id,
                "headings": list(headings),
                "status": "ok" if hop.get("reply") else "failed",
                "accepted": bool(hop.get("reply")),
                "summary": (hop.get("reply") or hop.get("error") or "")[:400],
                "artifact_ref": f"artifact://{slug}/{agent_id}/pass_01",
                "return_comm_id": ret["id"],
                "live": hop.get("live"),
                "provider": hop.get("provider"),
                "error": hop.get("error"),
                "reply": hop.get("reply") or "",
                "extracted_headings": list(extracted.keys()),
            }
        )
        parsed_ret = parse_emitted_instructions(ret.get("text") or "")
        decisions[agent_id] = parsed_ret
        _apply_pick(section_parts, agent_id, parsed_ret, picks.get(agent_id))
        for question in parsed_ret.get("human_asks") or []:
            if question not in human_asks:
                human_asks.append(question)
        if agent_id == "video.creativedirector":
            direction_text = (
                extracted.get("Creative direction")
                or parsed_ret.get("why")
                or (ret.get("text") or "")[:1500]
            )
        if agent_id == "video.continuity":
            freeze_text = "\n".join(
                item
                for item in (
                    extracted.get("Subject"),
                    extracted.get("Hair"),
                    extracted.get("Skin"),
                    parsed_ret.get("freeze"),
                )
                if item
            )[:1500]
        occupied = set(dispatch_ids) | {FIRST_CALLED} | {item[0] for item in extra_queue}
        for call in parsed_ret.get("induce_calls") or []:
            gid = str(call.get("agent_id") or "")
            if gid and gid not in occupied and len(extra_queue) < 2:
                extra_queue.append((gid, str(call.get("why") or "peer induce from member")))
                occupied.add(gid)

    for extra_id, extra_why in extra_queue:
        if agents_root is not None and not (Path(agents_root) / extra_id / "agent_spec.json").is_file():
            continue
        dispatch_ids.append(extra_id)
        why_by_id[extra_id] = extra_why
        headings = craft_headings_for(extra_id)
        brief_id = f"br_asain_x_{extra_id.split('.')[-1][:12]}"
        node_id = f"agent-{extra_id.replace('.', '-')}"
        brief_text = _induce_envelope(
            brief_id=brief_id,
            agent_id=extra_id,
            why=extra_why,
            headings=headings,
            human=prompt,
            direction=direction_text,
            freeze=freeze_text,
            human_answers=answers,
        )
        _assert_no_gold_body(brief_text)
        brief = add(
            node_id=first_node,
            from_id=FIRST_CALLED,
            to_id=extra_id,
            kind="induce",
            text=brief_text,
            inputs=[_tag(slug, first_node, received["id"], "pass-01")],
            outputs=[_tag(slug, node_id, "comm-pending", extra_id)],
            pass_id="pass_01",
        )
        hop = call_agent(chat_fn, extra_id, brief_text)
        if hop.get("live"):
            live_hops += 1
        reply_text = hop.get("reply") or hop.get("error") or "(empty live reply)"
        ret = add(
            node_id=node_id,
            from_id=extra_id,
            to_id=FIRST_CALLED,
            kind="return",
            text=reply_text,
            inputs=[_tag(slug, first_node, brief["id"], brief_id)],
            outputs=[_tag(slug, first_node, "comm-pending", "fan-in")],
            pass_id="pass_01",
        )
        stamp(ret, hop)
        extracted = extract_sections(hop.get("reply") or "", headings) if headings else {}
        for heading, body in extracted.items():
            if heading in headings or heading not in section_parts:
                section_parts[heading] = body
                section_sources[heading] = ret["id"]
        parsed_ret = parse_emitted_instructions(ret.get("text") or "")
        decisions[extra_id] = parsed_ret
        _apply_pick(section_parts, extra_id, parsed_ret, picks.get(extra_id))
        for question in parsed_ret.get("human_asks") or []:
            if question not in human_asks:
                human_asks.append(question)
        member_summaries.append(
            {
                "brief_id": brief_id,
                "agent_id": extra_id,
                "headings": list(headings),
                "status": "ok" if hop.get("reply") else "failed",
                "accepted": bool(hop.get("reply")),
                "summary": (hop.get("reply") or hop.get("error") or "")[:400],
                "artifact_ref": f"artifact://{slug}/{extra_id}/pass_01",
                "return_comm_id": ret["id"],
                "live": hop.get("live"),
                "provider": hop.get("provider"),
                "error": hop.get("error"),
                "reply": hop.get("reply") or "",
                "extracted_headings": list(extracted.keys()),
            }
        )

    seen_asks: set[str] = set()
    for agent_id, parsed in decisions.items():
        if agent_id not in {
            "video.promptengineer",
            "video.director",
            "video.cinematographer",
            "video.mua_makeup",
            "video.continuity",
        }:
            continue
        questions = list(parsed.get("human_asks") or [])
        if not questions and parsed.get("options") and str(parsed.get("decide_by") or "").lower() in {"human", "human_operator"}:
            questions = [str(parsed.get("why") or f"{agent_id} lock")]
        for question in questions:
            key = f"{agent_id}:{question}"
            if key in seen_asks:
                continue
            seen_asks.add(key)
            ask_text = question
            options = parsed.get("options") or []
            if options:
                lines = [f"ASK_HUMAN: {question}", "THINKING: Confirm this lock by selecting an option. Do not draft craft.", f"Decision point: {agent_id}"]
                for opt in options:
                    rec = " (recommend)" if str(opt.get("id")) == str(parsed.get("recommend") or "") else ""
                    label = str(opt.get("label") or "")
                    why = str(opt.get("why") or "")
                    lines.append(f"OPTION {opt.get('id')}: {label} — {why}{rec}" if why else f"OPTION {opt.get('id')}: {label}{rec}")
                lines.append(f"RECOMMEND: {parsed.get('recommend') or options[0].get('id')}")
                lines.append("DECIDE_BY: human")
                ask_text = "\n".join(lines)
            add(
                node_id="human-ask",
                from_id=agent_id,
                to_id="human_operator",
                kind="human_ask",
                text=ask_text,
                inputs=[_tag(slug, f"agent-{agent_id.replace('.', '-')}", received["id"], "ask")],
                outputs=[_tag(slug, "human-ask", "comm-pending", "answer")],
                pass_id="pass_01",
            )

    conflicts = collect_conflicts(section_parts)
    fanin_message = _first_called_fanin(prompt, member_summaries, conflicts)
    _assert_no_gold_body(fanin_message)
    hop_cons = call_agent(chat_fn, FIRST_CALLED, fanin_message)
    if hop_cons.get("live"):
        live_hops += 1
    cons_text = hop_cons.get("reply") or hop_cons.get("error") or "(empty consolidator reply)"
    cons = add(
        node_id=first_node,
        from_id=FIRST_CALLED,
        to_id="create-project",
        kind="consolidated",
        text=cons_text,
        inputs=[_tag(slug, f"agent-{row['agent_id'].replace('.', '-')}", row["return_comm_id"], row["agent_id"]) for row in member_summaries],
        outputs=[_tag(slug, "create-project", "comm-pending", f"{slug}-prompt")],
        pass_id="pass_01",
    )
    stamp(cons, hop_cons)
    add(
        node_id=first_node,
        from_id=FIRST_CALLED,
        to_id=FIRST_CALLED,
        kind="next_instruction",
        text=cons_text,
        inputs=[_tag(slug, first_node, cons["id"], "prior_consolidated")],
        outputs=[],
        pass_id="pass_02",
    )
    if direction_text and not (section_parts.get("Creative direction") or "").strip():
        section_parts["Creative direction"] = direction_text
    if human_asks:
        section_parts["Human asks"] = "\n".join(f"- {item}" for item in human_asks)
    output_text, missing_sections = assemble_generator_instruction(section_parts)
    missing_sections = [item for item in missing_sections if item != "Human asks" or human_asks]
    lineage_lines = [
        f"Host assembled output/{slug}-prompt.txt from live section bodies. sample/ was not copied.",
        f"missing_sections: {', '.join(missing_sections) if missing_sections else '(none)'}",
        f"conflicts: {'; '.join(conflicts) if conflicts else '(none)'}",
    ]
    for heading in GENERATOR_SECTIONS:
        lineage_lines.append(f"{heading} <- {section_sources.get(heading) or 'MISSING'}")
    lineage = add(
        node_id="output-prompt",
        from_id="host_service",
        to_id="output-prompt",
        kind="assembled",
        text="Host-joined generator instruction. First-called did not write the novel.\n" + "\n".join(lineage_lines),
        inputs=[_tag(slug, first_node, cons["id"], "consolidated")],
        outputs=[],
        pass_id="pass_02",
    )
    check = add(
        node_id="output-prompt",
        from_id=FIRST_CALLED,
        to_id="output-prompt",
        kind="output",
        text=output_text,
        inputs=[
            _tag(slug, "create-project", lineage["id"], "assembled"),
            _tag(slug, first_node, cons["id"], "consolidated"),
        ],
        outputs=[],
        pass_id="pass_02",
    )
    stamp(check, hop_cons)
    # Point launch/induce pending tags at real ids
    for item in items:
        for bag in ("input_tags", "output_tags"):
            fixed = []
            for tag in item.get(bag) or []:
                if not isinstance(tag, dict):
                    continue
                row = dict(tag)
                if row.get("comm_id") == "comm-pending":
                    row["comm_id"] = check["id"] if row.get("label") in {f"{slug}-prompt", "fan-in"} else received["id"]
                fixed.append(row)
            item[bag] = fixed

    existing_start = {}
    for node in (record.get("graph") or {}).get("nodes") or []:
        if isinstance(node, dict) and node.get("id") == "create-project" and isinstance(node.get("data"), dict):
            existing_start = dict(node["data"])
            break
    start = {
        "id": "create-project",
        "type": "start",
        "position": {"x": 80, "y": 160},
        "deletable": False,
        "data": {
            **existing_start,
            "kind": "start",
            "label": "Create Project",
            "io": {
                "inputs": [],
                "outputs": [FIRST_CALLED],
            },
        },
    }
    pe_outputs = list(dispatch_ids) + (["human-ask"] if human_asks else []) + ["output"]
    nodes = [
        start,
        _node(
            FIRST_CALLED,
            kind="agent",
            x=420,
            y=160,
            reason="orchestrator · options at this decision point",
            inputs=["create-project"],
            outputs=pe_outputs,
            extra=_decision_extra(
                decisions.get(FIRST_CALLED) or {},
                picks.get(FIRST_CALLED) or str((decisions.get(FIRST_CALLED) or {}).get("recommend") or ""),
            ),
        ),
    ]
    edges = [
        {
            "id": "e-create-promptengineer",
            "source": "create-project",
            "target": f"agent-{FIRST_CALLED.replace('.', '-')}",
            "sourceHandle": FIRST_CALLED,
            "targetHandle": "in",
            "type": "smoothstep",
            "label": FIRST_CALLED,
        }
    ]
    for index, agent_id in enumerate(dispatch_ids):
        nodes.append(
            _node(
                agent_id,
                kind="agent",
                x=760,
                y=40 + index * 120,
                reason=why_by_id.get(agent_id) or f"{agent_id} expert decision point",
                inputs=[FIRST_CALLED],
                outputs=["video.promptengineer"],
                extra=_decision_extra(
                    decisions.get(agent_id) or {},
                    picks.get(agent_id) or str((decisions.get(agent_id) or {}).get("recommend") or ""),
                ),
            )
        )
        edges.append(
            {
                "id": f"e-pe-{agent_id.replace('.', '-')}",
                "source": f"agent-{FIRST_CALLED.replace('.', '-')}",
                "target": f"agent-{agent_id.replace('.', '-')}",
                "sourceHandle": agent_id,
                "targetHandle": "in",
                "type": "smoothstep",
                "label": agent_id,
            }
        )
    if human_asks:
        nodes.append(
            {
                "id": "human-ask",
                "type": "human",
                "position": {"x": 420, "y": 420},
                "data": {
                    "kind": "human",
                    "label": "Human",
                    "reason": "Agents generated instructions to the human (ASK_HUMAN)",
                    "brief": "\n".join(human_asks)[:400],
                    "io": {"inputs": [FIRST_CALLED], "outputs": ["answer"]},
                },
            }
        )
        edges.append(
            {
                "id": "e-pe-human-ask",
                "source": f"agent-{FIRST_CALLED.replace('.', '-')}",
                "target": "human-ask",
                "sourceHandle": "human-ask",
                "targetHandle": "in",
                "type": "smoothstep",
                "label": "ASK_HUMAN",
            }
        )
    nodes.append(
        {
            "id": "output-prompt",
            "type": "output",
            "position": {"x": 1100, "y": 160},
            "deletable": False,
            "data": {
                "kind": "output",
                "label": "Output",
                "reason": f"project/{slug}/output/{slug}-prompt.txt",
                "brief": (output_text or "")[:280],
                "io": {"inputs": [FIRST_CALLED], "outputs": []},
            },
        }
    )
    edges.append(
        {
            "id": "e-pe-output",
            "source": f"agent-{FIRST_CALLED.replace('.', '-')}",
            "target": "output-prompt",
            "sourceHandle": "output",
            "targetHandle": "in",
            "type": "smoothstep",
            "label": "output",
        }
    )

    report = validate_prompt(output_text, gold) if gold else {
        "matched": False,
        "exact": False,
        "copied_sample": False,
        "missing_markers": [],
        "generated_chars": len(output_text),
        "gold_chars": 0,
    }
    report["missing_sections"] = missing_sections
    out_rel = f"project/{slug}/output/{slug}-prompt.txt"
    copied = bool(report.get("copied_sample"))
    if not dry_run and not copied:
        out_path = output_prompt_path(root, slug)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output_text if output_text.endswith("\n") else output_text + "\n", encoding="utf-8")
        save_comms(
            root,
            slug,
            {
                "items": items,
                "decisions": prior_comms.get("decisions") or [],
                "walkthrough": prior_comms.get("walkthrough") or "",
                "note": prior_comms.get("note") or "",
                "locks": prior_comms.get("locks") or {},
                "autopilot": prior_comms.get("autopilot") or {},
            },
            dry_run=False,
        )
        record["graph"] = {"nodes": nodes, "edges": edges}
        write_project(root, record, dry_run=False, create=False)
    return {
        "honesty": "CHARACTERIZATION",
        "dry_run": dry_run,
        "saved": (not dry_run) and (not copied),
        "first_called": FIRST_CALLED,
        "correlation_id": "corr_asain_beauty_001",
        "live_hops": live_hops,
        "live": live_hops > 0,
        "comms": {"schema_version": COMMS_SCHEMA, "project_id": slug, "items": items},
        "graph": {"nodes": nodes, "edges": edges},
        "member_returns": member_summaries,
        "section_sources": section_sources,
        "conflicts": conflicts,
        "human_asks": human_asks,
        "dispatch_ids": dispatch_ids,
        "creative_why": direction_text,
        "status": "needs_hitl" if human_asks and not answers else "ok",
        "output_path": out_rel,
        "validation": report,
        "note": (
            "Refused to write a byte copy of sample/."
            if copied
            else "Host assembles live English sections into output/. sample/ is not written. HTTP 200 is not craft-correct. Not an eval PASS. Tools stay off. Agent max_output_tokens=1024 cannot emit the full gold novel in one hop."
        ),
    }
