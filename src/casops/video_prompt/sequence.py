"""ISSUE-0009 P6: kind=sequence manifest. One collab pass = one clip; longer pieces are lists."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

from casops.video_prompt.compile import compile_clip, compiled_snapshot
from casops.video_prompt.schema import (
    CLIP_SCHEMA_ID,
    SequenceSchemaError,
    empty_sequence,
    validate_clip,
    validate_sequence,
)

COMPILER_POLICY = {
    "generation_unit": "clip",
    "one_pass_one_clip": True,
    "concat": "post",
}


def dump_sequence(sequence: dict[str, Any]) -> str:
    return json.dumps(sequence, indent=2, ensure_ascii=False) + "\n"


def sequence_from_clip(clip: dict[str, Any], *, slug: str, path: str | None = None) -> dict[str, Any]:
    """Wrap one canonical clip as a one-row sequence. Does not invent extra coverage."""
    generation = clip.get("generation") if isinstance(clip.get("generation"), dict) else {}
    intent = clip.get("intent") if isinstance(clip.get("intent"), dict) else {}
    try:
        duration = float(generation.get("duration_s") or 15)
    except (TypeError, ValueError):
        duration = 15.0
    clip_id = str(clip.get("clip_id") or f"CLIP.{slug}.001")
    logline = str(intent.get("logline") or "")
    rel = path or f"{slug}-canonical.yaml"
    payload = empty_sequence(
        sequence_id=f"SEQ.{slug}.001",
        project_id=slug,
        logline=logline,
        clips=[
            {
                "clip_id": clip_id,
                "order": 1,
                "start_s": 0,
                "end_s": duration,
                "path": rel,
                "role": "primary",
                "logline": logline,
            }
        ],
    )
    payload["delivery"] = {
        "timeline_duration_s": duration,
        "in_s": 0,
        "out_s": duration,
    }
    payload["policy"] = dict(COMPILER_POLICY)
    payload["provenance"] = {
        "honesty": "CHARACTERIZATION",
        "source_clip_id": clip_id,
        "schema": CLIP_SCHEMA_ID,
    }
    return validate_sequence(payload)


def assemble_sequence(
    *,
    project_id: str,
    logline: str,
    clips: list[dict[str, Any]],
    sequence_id: str | None = None,
) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for index, raw in enumerate(clips, start=1):
        if not isinstance(raw, dict):
            raise SequenceSchemaError("sequence clip row must be an object")
        row = {
            "clip_id": str(raw.get("clip_id") or f"CLIP.{project_id}.{index:03d}"),
            "order": int(raw.get("order") or index),
            "path": str(raw.get("path") or ""),
            "role": str(raw.get("role") or "clip"),
            "logline": str(raw.get("logline") or logline),
        }
        if raw.get("start_s") is not None:
            row["start_s"] = float(raw["start_s"])
        if raw.get("end_s") is not None:
            row["end_s"] = float(raw["end_s"])
        rows.append(row)
    timed = [row for row in rows if row.get("start_s") is not None and row.get("end_s") is not None]
    duration = 0.0
    if timed:
        duration = max(float(row["end_s"]) for row in timed) - min(float(row["start_s"]) for row in timed)
    payload = empty_sequence(
        sequence_id=sequence_id or f"SEQ.{project_id}.001",
        project_id=project_id,
        logline=logline,
        clips=rows,
    )
    payload["delivery"] = {"timeline_duration_s": duration}
    payload["policy"] = dict(COMPILER_POLICY)
    return validate_sequence(payload)


def write_sequence_file(output_dir: Path, slug: str, sequence: dict[str, Any]) -> Path:
    folder = Path(output_dir)
    if "sample" in folder.parts:
        raise SequenceSchemaError("sample/ is read-only")
    folder.mkdir(parents=True, exist_ok=True)
    dest = folder / f"{slug}-sequence.yaml"
    dest.write_text(dump_sequence(validate_sequence(sequence)), encoding="utf-8")
    return dest


def load_sequence_file(path: Path) -> dict[str, Any]:
    if "sample" in Path(path).parts:
        raise SequenceSchemaError("sample/ is read-only")
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return validate_sequence(payload)


def compile_sequence(
    sequence: dict[str, Any],
    clips: dict[str, dict[str, Any]],
    profile_id: str | None = None,
) -> dict[str, Any]:
    """Compile each clip independently. Never fuse into one vendor request."""
    manifest = validate_sequence(deepcopy(sequence))
    rows: list[dict[str, Any]] = []
    blocked = False
    for item in manifest.get("clips") or []:
        clip_id = str(item.get("clip_id") or "")
        clip = clips.get(clip_id)
        if clip is None:
            rows.append(
                {
                    "clip_id": clip_id,
                    "status": "blocked",
                    "compiled": None,
                    "error": "clip object missing",
                }
            )
            blocked = True
            continue
        validate_clip(clip)
        compiled = compile_clip(clip, profile_id)
        snapshot = compiled_snapshot(compiled)
        if snapshot.get("status") != "ok":
            blocked = True
        rows.append({"clip_id": clip_id, "status": snapshot.get("status"), "compiled": snapshot})
    return {
        "status": "blocked" if blocked else "ok",
        "sequence_id": manifest.get("sequence_id"),
        "policy": manifest.get("policy"),
        "fused_request": None,
        "clips": rows,
        "honesty": "CHARACTERIZATION",
        "note": "Each clip compiles alone. Concatenation is post. Not one Imagine request.",
    }
