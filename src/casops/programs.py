"""Named programs under repo `program/<code>/`. Companion, not a live grant.

ISSUE-0013: a Program is the film. Child Projects are segments. Host orchestrates.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

CODE_RE = re.compile(r"^[a-z](?:[a-z0-9-]{0,46}[a-z0-9])?$")
TOKEN_RE = re.compile(r"^[a-z][a-z0-9-]{0,46}$")

PHASES: tuple[str, ...] = ("w0", "w1", "w2", "w3", "w4", "w5", "w6")
LOCK_KEYS: tuple[str, ...] = (
    "logline",
    "pages",
    "generation_list",
    "visual_bible",
    "storyboard",
    "picture",
    "delivery",
)
SPAWN_LOCKS: tuple[str, ...] = ("generation_list", "visual_bible")
FINISH_KINDS: frozenset[str] = frozenset({"color", "mix", "graphics", "sound", "vfx", "titles"})
CUT_STATES: tuple[str, ...] = ("assembly", "rough", "fine", "picture_lock")
LIVE_STILL_TAGS: frozenset[str] = frozenset({"grok-image", "grok-imagine"})
STILL_SHEET_SLOTS: tuple[str, ...] = (
    "character-front.placeholder.txt",
    "character-side.placeholder.txt",
    "character-face.placeholder.txt",
    "location.placeholder.txt",
    "prop.placeholder.txt",
)
BIBLE_FILES: tuple[str, ...] = ("cast.md", "locations.md", "look.md", "world.md")
FIRST_CALLED = "video.showrunner"
FIRST_AGENT_HOP = "specials.intent-analysis-agent"
CREATIVE_AGENT = "specials.general-creative-agent"
PLACEHOLDER_NOTE = "CHARACTERIZATION placeholder. Not a live sheet. Do not copy sample/.\n"


def programs_root_for(agents_root: Path, override: Path | None = None) -> Path:
    if override is not None:
        return override.resolve()
    return (Path(agents_root).resolve().parent / "program").resolve()


def normalize_code(value: str) -> str:
    original = value or ""
    if ".." in original or "/" in original.replace("\\", "/") or "\\" in original:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="invalid program code")
    raw = original.strip().lower().replace(" ", "-")
    raw = re.sub(r"[^a-z0-9-]+", "", raw)
    raw = re.sub(r"-{2,}", "-", raw).strip("-")
    if not raw or not CODE_RE.match(raw):
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="invalid program code")
    return raw


def _safe_dir(root: Path, code: str) -> Path:
    folder = (root / code).resolve()
    try:
        folder.relative_to(root.resolve())
    except ValueError as exc:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="program path escapes root") from exc
    return folder


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _forbid_sample(path: Path) -> None:
    if "sample" in Path(path).parts:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="sample/ is read-only")


def _token(value: str, prefix: str) -> str:
    raw = re.sub(r"[^a-z0-9]+", "-", str(value or "").strip().lower()).strip("-")
    if not raw:
        raw = prefix
    if raw[0].isdigit():
        raw = f"{prefix}-{raw}"
    if not TOKEN_RE.match(raw):
        raw = (prefix + raw)[:47]
        raw = re.sub(r"[^a-z0-9-]", "", raw)
    if not TOKEN_RE.match(raw):
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="invalid segment id")
    return raw


def default_locks() -> dict[str, bool]:
    return {key: False for key in LOCK_KEYS}


def normalize_locks(raw: Any) -> dict[str, bool]:
    locks = default_locks()
    if isinstance(raw, dict):
        for key in LOCK_KEYS:
            if key in raw:
                value = raw[key]
                locks[key] = value is True or value in ("true", "1", 1)
    return locks


def spawn_missing_locks(locks: dict[str, Any] | None) -> list[str]:
    current = normalize_locks(locks or {})
    return [key for key in SPAWN_LOCKS if not current.get(key)]


def generation_list_lock_blockers(generation_list: Any) -> list[str]:
    payload = normalize_generation_list(generation_list)
    scenes = payload.get("scenes") or []
    if not scenes:
        return ["(no scenes)"]
    return [str(scene["id"]) for scene in scenes if not scene.get("segments")]


def assert_generation_list_lockable(generation_list: Any) -> None:
    blockers = generation_list_lock_blockers(generation_list)
    if blockers:
        raise CasopsError(
            ErrorCode.INH_STRUCTURE_MISMATCH,
            detail="cannot lock generation_list: empty scenes: " + ",".join(blockers),
        )


def _assert_no_gold(text: str) -> None:
    from casops.project_comms import GOLD_BODY_PROBES

    lower = str(text or "").lower()
    for probe in GOLD_BODY_PROBES:
        if probe.lower() in lower:
            raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="gold-body probe forbidden")


def request_still_sheet(tag: str) -> dict[str, Any]:
    normalized = str(tag or "").strip().lower()
    if normalized in LIVE_STILL_TAGS:
        return {
            "status": "ok",
            "tag": normalized,
            "success": False,
            "live": False,
            "dry_run_default": True,
            "sheet": None,
            "note": "Grok still is Dry-run gated. Not a successful sheet until Dry-run is off.",
        }
    return {
        "status": "blocked",
        "tag": normalized,
        "success": False,
        "request": {},
        "sheet": None,
        "note": "Fail-closed still tag. Not a successful sheet.",
    }


def inspect_chain_frame(*, end_frame_ok: bool, artifacts: str = "") -> dict[str, Any]:
    if not end_frame_ok or str(artifacts or "").strip():
        return {
            "status": "rejected",
            "inherit_end_frame": False,
            "refresh_from": "program_bible_still",
            "reason": str(artifacts or "end frame failed inspection"),
        }
    return {"status": "ok", "inherit_end_frame": True}


def bible_and_storyboard_plan(code: str, generation_list: Any) -> dict[str, list[str]]:
    sheets = [f"program/{code}/assets/approved/{name}" for name in STILL_SHEET_SLOTS]
    bible = [f"program/{code}/bible/{name}" for name in BIBLE_FILES]
    panels = [
        f"program/{code}/storyboard/{segment['id']}.md"
        for _scene, segment in iter_segments(generation_list or {})
    ]
    return {"sheets": sheets, "bible": bible, "panels": panels}


def write_bible_and_storyboard(folder: Path, record: dict[str, Any], *, dry_run: bool) -> dict[str, Any]:
    code = str(record.get("code") or "")
    plan = bible_and_storyboard_plan(code, record.get("generation_list"))
    if dry_run:
        return {**plan, "written": False, "dry_run": True, "files": []}
    _forbid_sample(folder)
    written: list[str] = []
    bible_dir = folder / "bible"
    sheets_dir = folder / "assets" / "approved"
    boards_dir = folder / "storyboard"
    ledger_dir = folder / "continuity"
    bible_dir.mkdir(parents=True, exist_ok=True)
    sheets_dir.mkdir(parents=True, exist_ok=True)
    boards_dir.mkdir(parents=True, exist_ok=True)
    ledger_dir.mkdir(parents=True, exist_ok=True)
    for name in BIBLE_FILES:
        path = bible_dir / name
        path.write_text(f"# {name}\n\n{PLACEHOLDER_NOTE}", encoding="utf-8")
        written.append(f"program/{code}/bible/{name}")
    for name in STILL_SHEET_SLOTS:
        path = sheets_dir / name
        path.write_text(PLACEHOLDER_NOTE, encoding="utf-8")
        written.append(f"program/{code}/assets/approved/{name}")
    (ledger_dir / "ledger.csv").write_text(
        "scene_id,clip_id,approved_take_id,character_id,wardrobe\n",
        encoding="utf-8",
    )
    written.append(f"program/{code}/continuity/ledger.csv")
    for _scene, segment in iter_segments(record.get("generation_list") or {}):
        panel = boards_dir / f"{segment['id']}.md"
        body = (
            f"# Panel {segment['id']}\n\n"
            f"Scene: {segment.get('scene_id')}\n"
            f"Purpose: {segment.get('purpose') or 'beat'}\n"
            "Still before motion. One panel per segment.\n"
            f"{PLACEHOLDER_NOTE}"
        )
        _assert_no_gold(body)
        panel.write_text(body, encoding="utf-8")
        written.append(f"program/{code}/storyboard/{segment['id']}.md")
    return {**plan, "written": True, "dry_run": False, "files": written}


def delivery_plan(code: str) -> list[str]:
    return [
        f"program/{code}/delivery/specifications.yaml",
        f"program/{code}/delivery/a11y.md",
        f"program/{code}/delivery/captions/.keep",
        f"program/{code}/delivery/archive-plan.md",
    ]


def write_delivery_tree(folder: Path, record: dict[str, Any], *, dry_run: bool) -> dict[str, Any]:
    code = str(record.get("code") or "")
    files = delivery_plan(code)
    if dry_run:
        return {"files": files, "written": False, "dry_run": True, "live_upload": False}
    _forbid_sample(folder)
    dest = folder / "delivery"
    captions = dest / "captions"
    dest.mkdir(parents=True, exist_ok=True)
    captions.mkdir(parents=True, exist_ok=True)
    spec = {
        "honesty": "CHARACTERIZATION",
        "live_upload": False,
        "production_activation": False,
        "captions": f"program/{code}/delivery/captions/",
        "a11y": f"program/{code}/delivery/a11y.md",
        "archive": f"program/{code}/delivery/archive-plan.md",
        "aspect_ratio": (record.get("delivery") or {}).get("aspect_ratio"),
        "frame_rate_fps": (record.get("delivery") or {}).get("frame_rate_fps") or 24,
    }
    (dest / "specifications.yaml").write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (dest / "a11y.md").write_text("# Accessibility\n\nCHARACTERIZATION slot. Captions / AD / contrast. No live upload.\n", encoding="utf-8")
    (captions / ".keep").write_text("", encoding="utf-8")
    (dest / "archive-plan.md").write_text("# Archive plan\n\nCHARACTERIZATION. No live vault write.\n", encoding="utf-8")
    return {"files": files, "written": True, "dry_run": False, "live_upload": False}


def child_inherit_payload(record: dict[str, Any], scene: dict[str, Any], segment: dict[str, Any]) -> dict[str, Any]:
    code = str(record.get("code") or "")
    payload = {
        "program_id": code,
        "scene_id": scene["id"],
        "segment_id": segment["id"],
        "bible_ref": f"program/{code}/bible/",
        "storyboard_ref": f"program/{code}/storyboard/{segment['id']}.md",
        "identity": {"path": "creative.shots.subjects", "source": "program_bible"},
        "constraints": {"path": "constraints", "source": "program_bible"},
    }
    _assert_no_gold(json.dumps(payload))
    return payload


def concat_program(record: dict[str, Any], *, tool_available: bool | None = None) -> dict[str, Any]:
    import shutil

    available = shutil.which("ffmpeg") is not None if tool_available is None else bool(tool_available)
    sequence = program_sequence(record)
    if not available:
        return {
            "status": "blocked",
            "fused_request": None,
            "concat": "post",
            "error": "concat tool missing",
            "mp4": None,
            "clips": sequence.get("clips") or [],
            "honesty": "CHARACTERIZATION",
        }
    return {
        "status": "ok",
        "fused_request": None,
        "concat": "post",
        "mp4": None,
        "clips": sequence.get("clips") or [],
        "honesty": "CHARACTERIZATION",
        "note": "Tool present. CHARACTERIZATION does not auto-write a fused mp4.",
    }


def normalize_generation_list(raw: Any) -> dict[str, Any]:
    scenes_in: list[Any] = []
    if isinstance(raw, dict):
        maybe = raw.get("scenes")
        scenes_in = maybe if isinstance(maybe, list) else []
    elif isinstance(raw, list):
        scenes_in = raw
    scenes: list[dict[str, Any]] = []
    seen_segments: set[str] = set()
    for scene in scenes_in:
        if not isinstance(scene, dict):
            continue
        scene_id = _token(str(scene.get("id") or scene.get("scene_id") or f"sc{len(scenes) + 1}"), "sc")
        segments: list[dict[str, Any]] = []
        for item in scene.get("segments") or []:
            if not isinstance(item, dict):
                continue
            segment_id = _token(str(item.get("id") or item.get("segment_id") or f"seg{len(segments) + 1}"), "seg")
            if segment_id in seen_segments:
                raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail=f"duplicate segment id: {segment_id}")
            seen_segments.add(segment_id)
            try:
                duration = float(item.get("duration_s") or 6)
            except (TypeError, ValueError):
                duration = 6.0
            segments.append(
                {
                    "id": segment_id,
                    "scene_id": scene_id,
                    "purpose": str(item.get("purpose") or ""),
                    "duration_s": duration,
                    "status": str(item.get("status") or "planned"),
                    "project_slug": str(item.get("project_slug") or ""),
                    "still_required": bool(item.get("still_required", True)),
                    "chain_from": str(item.get("chain_from") or ""),
                }
            )
        scenes.append({"id": scene_id, "title": str(scene.get("title") or scene_id), "segments": segments})
    return {"scenes": scenes}


def iter_segments(generation_list: dict[str, Any]) -> list[tuple[dict[str, Any], dict[str, Any]]]:
    rows: list[tuple[dict[str, Any], dict[str, Any]]] = []
    payload = normalize_generation_list(generation_list)
    for scene in payload["scenes"]:
        for segment in scene["segments"]:
            rows.append((scene, segment))
    return rows


def segment_project_slug(program_code: str, segment_id: str) -> str:
    from casops.projects import normalize_slug

    return normalize_slug(f"{program_code}-{segment_id}")


def preview_spawn(code: str, generation_list: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for scene, segment in iter_segments(generation_list):
        rows.append(
            {
                "scene_id": str(scene["id"]),
                "segment_id": str(segment["id"]),
                "slug": segment_project_slug(code, str(segment["id"])),
                "purpose": str(segment.get("purpose") or ""),
            }
        )
    return rows


def normalize_phase(value: Any) -> str:
    text = str(value or "w0").strip().lower()
    return text if text in PHASES else "w0"


def empty_program(code: str, name: str, *, now: str | None = None) -> dict[str, Any]:
    stamp = now or _now()
    return {
        "schema_version": "casops.program.v1",
        "id": code,
        "code": code,
        "name": name,
        "honesty": "CHARACTERIZATION",
        "first_called": FIRST_CALLED,
        "first_agent_hop": FIRST_AGENT_HOP,
        "phase": "w0",
        "locks": default_locks(),
        "generation_list": {"scenes": []},
        "project_ids": [],
        "cut_state": "assembly",
        "generation_list_ref": f"program/{code}/generation-list.yaml",
        "sequence_ref": f"program/{code}/sequence.yaml",
        "bible_ref": f"program/{code}/bible/",
        "storyboard_ref": f"program/{code}/storyboard/",
        "delivery_ref": f"program/{code}/delivery/",
        "delivery": {"runtime_target_s": None, "aspect_ratio": None, "frame_rate_fps": 24},
        "created_at": stamp,
        "updated_at": stamp,
        "folder": f"program/{code}",
        "production_activation": False,
        "allowed_tools": [],
    }


def _merge_program(existing: dict[str, Any] | None, payload: dict[str, Any], code: str, title: str) -> dict[str, Any]:
    now = _now()
    base = empty_program(code, title, now=now)
    if existing:
        for key, value in existing.items():
            if key in {"saved", "dry_run"}:
                continue
            base[key] = value
    if payload.get("phase"):
        base["phase"] = normalize_phase(payload.get("phase"))
    if payload.get("cut_state"):
        cut = str(payload.get("cut_state") or "").strip().lower()
        if cut in CUT_STATES:
            base["cut_state"] = cut
    if "locks" in payload:
        merged = normalize_locks(base.get("locks"))
        incoming = payload.get("locks") if isinstance(payload.get("locks"), dict) else {}
        for key in LOCK_KEYS:
            if key in incoming:
                merged[key] = incoming[key] is True or incoming[key] in ("true", "1", 1)
        base["locks"] = merged
    else:
        base["locks"] = normalize_locks(base.get("locks"))
    if "generation_list" in payload:
        base["generation_list"] = normalize_generation_list(payload.get("generation_list"))
    else:
        base["generation_list"] = normalize_generation_list(base.get("generation_list"))
    if "project_ids" in payload and isinstance(payload.get("project_ids"), list):
        base["project_ids"] = [str(item) for item in payload["project_ids"] if str(item).strip()]
    elif not isinstance(base.get("project_ids"), list):
        base["project_ids"] = []
    if isinstance(payload.get("delivery"), dict):
        delivery = dict(base.get("delivery") or {})
        delivery.update(payload["delivery"])
        base["delivery"] = delivery
    if isinstance(payload.get("graph"), dict):
        base["graph"] = payload["graph"]
    elif existing and isinstance(existing.get("graph"), dict):
        base["graph"] = existing["graph"]
    base["id"] = code
    base["code"] = code
    base["name"] = title
    base["first_called"] = FIRST_CALLED
    base["first_agent_hop"] = FIRST_AGENT_HOP
    base["honesty"] = "CHARACTERIZATION"
    base["folder"] = f"program/{code}"
    base["generation_list_ref"] = f"program/{code}/generation-list.yaml"
    base["sequence_ref"] = f"program/{code}/sequence.yaml"
    base["bible_ref"] = f"program/{code}/bible/"
    base["storyboard_ref"] = f"program/{code}/storyboard/"
    base["delivery_ref"] = f"program/{code}/delivery/"
    if not base.get("cut_state"):
        base["cut_state"] = "assembly"
    base["production_activation"] = False
    base["allowed_tools"] = []
    if existing and existing.get("created_at"):
        base["created_at"] = existing["created_at"]
    elif payload.get("created_at"):
        base["created_at"] = payload["created_at"]
    else:
        base["created_at"] = now
    base["updated_at"] = now
    return base


def list_programs(root: Path) -> list[dict[str, Any]]:
    root.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    for child in sorted(root.iterdir()):
        payload_path = child / "program.json"
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
                "code": payload.get("code") or child.name,
                "name": payload.get("name") or child.name,
                "phase": payload.get("phase") or "w0",
                "project_ids": payload.get("project_ids") if isinstance(payload.get("project_ids"), list) else [],
                "updated_at": payload.get("updated_at"),
            }
        )
    return rows


def read_program(root: Path, code: str) -> dict[str, Any]:
    code = normalize_code(code)
    folder = _safe_dir(root, code)
    path = folder / "program.json"
    if not path.is_file():
        raise CasopsError(ErrorCode.INH_PARENT_MISSING, detail="unknown program")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH)
    record = _merge_program(payload, {}, code, str(payload.get("name") or code))
    record["updated_at"] = payload.get("updated_at") or record["updated_at"]
    record["created_at"] = payload.get("created_at") or record["created_at"]
    return record


def _write_sidecars(folder: Path, record: dict[str, Any]) -> None:
    _forbid_sample(folder)
    (folder / "generation-list.yaml").write_text(
        json.dumps(record.get("generation_list") or {"scenes": []}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    sequence = program_sequence(record)
    (folder / "sequence.yaml").write_text(json.dumps(sequence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_bible_and_storyboard(folder, record, dry_run=False)
    write_delivery_tree(folder, record, dry_run=False)


def write_program(root: Path, payload: dict[str, Any], *, dry_run: bool, create: bool) -> dict[str, Any]:
    code = normalize_code(str(payload.get("code") or payload.get("id") or payload.get("name") or ""))
    title = str(payload.get("name") or "").strip()
    if not title:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="program name required")
    folder = _safe_dir(root, code)
    _forbid_sample(folder)
    existing_path = folder / "program.json"
    existing = None
    if existing_path.is_file():
        loaded = json.loads(existing_path.read_text(encoding="utf-8"))
        existing = loaded if isinstance(loaded, dict) else None
    if create and existing is not None:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="program already exists")
    if not create and existing is None:
        raise CasopsError(ErrorCode.INH_PARENT_MISSING, detail="unknown program")
    record = _merge_program(existing, payload, code, title)
    if record["locks"].get("generation_list"):
        assert_generation_list_lockable(record.get("generation_list"))
    if dry_run:
        record["saved"] = False
        record["dry_run"] = True
        return record
    folder.mkdir(parents=True, exist_ok=True)
    persist = {key: value for key, value in record.items() if key not in {"saved", "dry_run"}}
    (folder / "program.json").write_text(json.dumps(persist, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    _write_sidecars(folder, persist)
    if create:
        from casops.program_comms import stamp_program_comms

        stamp_program_comms(root, code, dry_run=False)
    record["saved"] = True
    record["dry_run"] = False
    return record


def program_sequence(record: dict[str, Any]) -> dict[str, Any]:
    code = str(record.get("code") or record.get("id") or "")
    clips: list[dict[str, Any]] = []
    for index, (scene, segment) in enumerate(iter_segments(record.get("generation_list") or {}), start=1):
        slug = str(segment.get("project_slug") or segment_project_slug(code, str(segment["id"])))
        clips.append(
            {
                "clip_id": slug,
                "order": index,
                "path": f"project/{slug}/output/{slug}-canonical.yaml",
                "role": "clip",
                "logline": str(segment.get("purpose") or scene.get("title") or ""),
                "scene_id": scene["id"],
                "segment_id": segment["id"],
            }
        )
    return {
        "kind": "sequence",
        "schema_version": "casops.program.sequence.v1",
        "program_id": code,
        "generation_unit": "clip",
        "one_pass_one_clip": True,
        "concat": "post",
        "fused_request": None,
        "clips": clips,
        "honesty": "CHARACTERIZATION",
        "note": "Each clip compiles alone. Concatenation is post. Not one Imagine request.",
    }


def compile_program_sequence(record: dict[str, Any]) -> dict[str, Any]:
    from casops.video_prompt.sequence import assemble_sequence, compile_sequence

    sequence = program_sequence(record)
    clips = list(sequence.get("clips") or [])
    if not clips:
        return {
            "status": "ok",
            "sequence_id": None,
            "policy": {"generation_unit": "clip", "one_pass_one_clip": True, "concat": "post"},
            "fused_request": None,
            "concat": "post",
            "clips": [],
            "honesty": "CHARACTERIZATION",
            "note": "No segments yet. Each clip compiles alone. Concatenation is post.",
        }
    assembled = assemble_sequence(
        project_id=str(record.get("code") or "program"),
        logline=str(record.get("name") or ""),
        clips=clips,
    )
    compiled = compile_sequence(assembled, {})
    compiled["fused_request"] = None
    compiled["concat"] = "post"
    compiled["honesty"] = "CHARACTERIZATION"
    return compiled


def spawn_child_projects(
    programs_root: Path,
    projects_root: Path,
    code: str,
    *,
    dry_run: bool,
) -> dict[str, Any]:
    record = read_program(programs_root, code)
    missing = spawn_missing_locks(record.get("locks"))
    if missing:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="missing locks: " + ",".join(missing))
    preview = preview_spawn(record["code"], record.get("generation_list") or {})
    if not preview:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="generation list has no segments")
    if dry_run:
        return {
            **record,
            "dry_run": True,
            "saved": False,
            "preview": preview,
            "project_ids": [],
            "spawned": 0,
        }
    from casops.projects import write_project

    _forbid_sample(projects_root)
    ids: list[str] = []
    generation = normalize_generation_list(record.get("generation_list"))
    for scene in generation["scenes"]:
        for segment in scene["segments"]:
            slug = segment_project_slug(record["code"], str(segment["id"]))
            existing = (Path(projects_root) / slug / "project.json").is_file()
            if not existing:
                inherit = child_inherit_payload(record, scene, segment)
                brief = (
                    f"Program {record['code']} scene {scene['id']} segment {segment['id']}. "
                    f"Inherit bible {inherit['bible_ref']} board {inherit['storyboard_ref']}."
                )
                _assert_no_gold(brief)
                write_project(
                    projects_root,
                    {
                        "name": slug,
                        "title": str(segment.get("purpose") or slug),
                        "brief": brief,
                        "duration": f"{int(segment.get('duration_s') or 6)}s",
                        "notes": json.dumps(inherit, ensure_ascii=False),
                        "inherit": inherit,
                        "sub_workflow_id": "video.template.e",
                    },
                    dry_run=False,
                    create=True,
                )
            segment["project_slug"] = slug
            segment["status"] = "spawned"
            ids.append(slug)
    record["generation_list"] = generation
    record["project_ids"] = ids
    record["phase"] = "w3"
    saved = write_program(programs_root, record, dry_run=False, create=False)
    saved["preview"] = preview
    saved["spawned"] = len(ids)
    saved["dry_run"] = False
    saved["saved"] = True
    return saved


def apply_cut_state(root: Path, code: str, state: str, *, dry_run: bool) -> dict[str, Any]:
    record = read_program(root, code)
    action = str(state or "").strip().lower().replace("-", "_")
    if action not in CUT_STATES:
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="unknown cut state")
    record["cut_state"] = action
    record["phase"] = "w5"
    if action == "picture_lock":
        locks = normalize_locks(record.get("locks"))
        locks["picture"] = True
        record["locks"] = locks
    return write_program(root, record, dry_run=dry_run, create=False)


def apply_finish(root: Path, code: str, kind: str, *, dry_run: bool) -> dict[str, Any]:
    record = read_program(root, code)
    action = str(kind or "").strip().lower().replace("-", "_")
    if action == "trailer":
        raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="trailer is not a silent spawn")
    if action in {"picture", "picture_lock"} or action in CUT_STATES:
        return apply_cut_state(root, code, "picture_lock" if action in {"picture", "picture_lock"} else action, dry_run=dry_run)
    if action in FINISH_KINDS:
        if not normalize_locks(record.get("locks")).get("picture"):
            raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="missing locks: picture")
        result = dict(record)
        result["finish"] = action
        result["status"] = "ok"
        result["fused_request"] = None
        result["dry_run"] = dry_run
        result["saved"] = not dry_run
        result["honesty"] = "CHARACTERIZATION"
        tree = write_delivery_tree(_safe_dir(root, record["code"]), record, dry_run=dry_run)
        result["delivery_files"] = tree.get("files")
        result["live_upload"] = False
        return result
    raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH, detail="unknown finish kind")
