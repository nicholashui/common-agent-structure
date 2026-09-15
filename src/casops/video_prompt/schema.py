"""Load and validate video_generation_prompt_specification.v2 clip envelopes."""

from __future__ import annotations

from pathlib import Path
from typing import Any, TypedDict

import jsonschema

CLIP_SCHEMA_ID = "video_generation_prompt_specification.v2"
CLIP_SPEC_VERSION = "2.0.0"


class ClipSchemaError(ValueError):
    """Envelope failed V1 structure validation."""


class SequenceSchemaError(ValueError):
    """Sequence manifest failed structure or timeline validation."""


class CasopsExtension(TypedDict, total=False):
    project_id: str
    comm_ids: list[str]
    owner_map: dict[str, list[str]]
    frame_prose: str


class ClipObject(TypedDict, total=False):
    schema: str
    spec_version: str
    kind: str
    clip_id: str
    revision: int
    classification: dict[str, Any]
    target: dict[str, Any]
    generation: dict[str, Any]
    delivery: dict[str, Any]
    intent: dict[str, Any]
    assets: list[dict[str, Any]]
    creative: dict[str, Any]
    constraints: dict[str, Any]
    provenance: dict[str, Any]
    extensions: dict[str, Any]


def repo_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "spec" / "video_generation_prompt_specification.v2.md").is_file():
            return parent
    raise FileNotFoundError("CASOPS repo root with video prompt spec not found")


def envelope_schema_path() -> Path:
    return repo_root() / "spec" / "schemas" / "video_generation_prompt.v2.clip.envelope.json"


def sequence_schema_path() -> Path:
    return repo_root() / "spec" / "schemas" / "video_generation_prompt.v2.sequence.json"


def load_envelope_schema() -> dict[str, Any]:
    import json

    path = envelope_schema_path()
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ClipSchemaError("clip envelope schema must be an object")
    return payload


def empty_clip(
    *,
    clip_id: str,
    logline: str,
    profile_id: str,
    mode: str = "image_to_video",
    duration_s: float = 15,
) -> ClipObject:
    """Minimal envelope that satisfies V1 structure. Not an executable request."""
    return {
        "schema": CLIP_SCHEMA_ID,
        "spec_version": CLIP_SPEC_VERSION,
        "kind": "clip",
        "clip_id": clip_id,
        "revision": 1,
        "target": {"profile_id": profile_id, "mode": mode},
        "generation": {"duration_s": duration_s},
        "delivery": {},
        "intent": {"logline": logline},
        "assets": [],
        "creative": {
            "shots": [
                {
                    "shot_id": f"{clip_id}.A",
                    "start_s": 0,
                    "end_s": duration_s,
                    "camera": {},
                    "action": {},
                }
            ],
            "audio": {},
        },
        "constraints": {},
        "provenance": {},
        "extensions": {"casops": {}},
    }


def validate_clip(payload: Any) -> ClipObject:
    if not isinstance(payload, dict):
        raise ClipSchemaError("clip envelope must be an object")
    try:
        jsonschema.validate(payload, load_envelope_schema())
    except jsonschema.ValidationError as exc:
        raise ClipSchemaError(exc.message) from exc
    return payload  # type: ignore[return-value]


def load_sequence_schema() -> dict[str, Any]:
    import json

    path = sequence_schema_path()
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise SequenceSchemaError("sequence schema must be an object")
    return payload


def empty_sequence(
    *,
    sequence_id: str,
    project_id: str,
    logline: str,
    clips: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "schema": CLIP_SCHEMA_ID,
        "spec_version": CLIP_SPEC_VERSION,
        "kind": "sequence",
        "sequence_id": sequence_id,
        "revision": 1,
        "project_id": project_id,
        "intent": {"logline": logline},
        "clips": clips,
        "delivery": {},
        "policy": {
            "generation_unit": "clip",
            "one_pass_one_clip": True,
            "concat": "post",
        },
        "provenance": {"honesty": "CHARACTERIZATION"},
        "extensions": {"casops": {"project_id": project_id}},
    }


def validate_sequence(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise SequenceSchemaError("sequence manifest must be an object")
    try:
        jsonschema.validate(payload, load_sequence_schema())
    except jsonschema.ValidationError as exc:
        raise SequenceSchemaError(exc.message) from exc
    clips = payload.get("clips") if isinstance(payload.get("clips"), list) else []
    ids: list[str] = []
    orders: list[int] = []
    timed: list[tuple[float, float, str]] = []
    for row in clips:
        if not isinstance(row, dict):
            raise SequenceSchemaError("sequence clip row must be an object")
        clip_id = str(row.get("clip_id") or "")
        path = str(row.get("path") or "")
        if "sample" in Path(path).parts or path.replace("\\", "/").find("sample/") >= 0:
            raise SequenceSchemaError("sample/ is read-only; sequence paths cannot use sample/")
        if clip_id in ids:
            raise SequenceSchemaError(f"duplicate clip_id {clip_id}")
        ids.append(clip_id)
        try:
            order = int(row.get("order"))
        except (TypeError, ValueError) as exc:
            raise SequenceSchemaError("clip order must be an integer") from exc
        if order in orders:
            raise SequenceSchemaError(f"duplicate clip order {order}")
        orders.append(order)
        if row.get("start_s") is None or row.get("end_s") is None:
            continue
        start_s = float(row.get("start_s"))
        end_s = float(row.get("end_s"))
        if start_s >= end_s:
            raise SequenceSchemaError(f"{clip_id} start_s must be < end_s")
        timed.append((start_s, end_s, clip_id))
    timed.sort()
    for index in range(1, len(timed)):
        prev_end = timed[index - 1][1]
        prev_id = timed[index - 1][2]
        start_s, _, clip_id = timed[index]
        if start_s < prev_end:
            raise SequenceSchemaError(f"clips {prev_id} and {clip_id} overlap; sequence is editorial, not one generation")
    policy = payload.get("policy") if isinstance(payload.get("policy"), dict) else {}
    if policy.get("generation_unit") != "clip":
        raise SequenceSchemaError("generation_unit must be clip; do not fuse a sequence into one vendor request")
    return payload
