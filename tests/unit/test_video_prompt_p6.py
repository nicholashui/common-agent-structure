import json
from pathlib import Path

import pytest

from casops.project_comms import GOLD_BODY_PROBES, read_output, walkthrough_module
from casops.project_generate import generate_project_media
from casops.projects import write_project
from casops.video_prompt.assemble import clip_from_walkthrough, write_clip_files
from casops.video_prompt.schema import SequenceSchemaError, empty_clip, validate_sequence
from casops.video_prompt.sequence import assemble_sequence, compile_sequence, sequence_from_clip


REPO = Path(__file__).resolve().parents[2]


def test_sequence_from_one_clip_is_one_generation_unit() -> None:
    clip = clip_from_walkthrough(walkthrough_module("european-handsome"))
    seq = sequence_from_clip(clip, slug="european-handsome", path="european-handsome-canonical.yaml")
    validate_sequence(seq)
    assert seq["kind"] == "sequence"
    assert seq["policy"]["generation_unit"] == "clip"
    assert seq["policy"]["concat"] == "post"
    assert len(seq["clips"]) == 1
    assert seq["clips"][0]["clip_id"] == clip["clip_id"]
    assert seq["clips"][0]["end_s"] == clip["generation"]["duration_s"]
    blob = json.dumps(seq)
    for probe in GOLD_BODY_PROBES:
        assert probe not in blob


def test_overlapping_clips_are_rejected() -> None:
    with pytest.raises(SequenceSchemaError, match="overlap"):
        assemble_sequence(
            project_id="demo",
            logline="Two beats.",
            clips=[
                {
                    "clip_id": "CLIP.demo.001",
                    "order": 1,
                    "start_s": 0,
                    "end_s": 8,
                    "path": "demo-a-canonical.yaml",
                },
                {
                    "clip_id": "CLIP.demo.002",
                    "order": 2,
                    "start_s": 6,
                    "end_s": 14,
                    "path": "demo-b-canonical.yaml",
                },
            ],
        )


def test_sample_path_is_rejected() -> None:
    with pytest.raises(SequenceSchemaError, match="sample"):
        assemble_sequence(
            project_id="demo",
            logline="No sample.",
            clips=[
                {
                    "clip_id": "CLIP.demo.001",
                    "order": 1,
                    "start_s": 0,
                    "end_s": 6,
                    "path": "sample/demo-prompt.txt",
                }
            ],
        )


def test_compile_sequence_does_not_fuse_requests() -> None:
    first = empty_clip(
        clip_id="CLIP.demo.001",
        logline="First locked beat.",
        profile_id="xai.grok-imagine-video-1.5.i2v",
        duration_s=6,
    )
    second = empty_clip(
        clip_id="CLIP.demo.002",
        logline="Second locked beat.",
        profile_id="xai.grok-imagine-video-1.5.i2v",
        duration_s=6,
    )
    first["creative"]["shots"][0]["subjects"] = [{"subject_id": "CHAR.A", "identity": "Adult A face lock."}]
    second["creative"]["shots"][0]["subjects"] = [{"subject_id": "CHAR.B", "identity": "Adult B face lock."}]
    seq = assemble_sequence(
        project_id="demo",
        logline="Two clips, two generations.",
        clips=[
            {"clip_id": "CLIP.demo.001", "order": 1, "start_s": 0, "end_s": 6, "path": "a.yaml"},
            {"clip_id": "CLIP.demo.002", "order": 2, "start_s": 6, "end_s": 12, "path": "b.yaml"},
        ],
    )
    compiled = compile_sequence(
        seq,
        {"CLIP.demo.001": first, "CLIP.demo.002": second},
        "xai.grok-imagine-video-1.5.i2v",
    )
    assert compiled["fused_request"] is None
    assert compiled["policy"]["generation_unit"] == "clip"
    assert len(compiled["clips"]) == 2
    still_a = compiled["clips"][0]["compiled"]["prompt"]["still"]
    still_b = compiled["clips"][1]["compiled"]["prompt"]["still"]
    assert still_a != still_b
    assert "Adult A face lock." in still_a
    assert "Adult B face lock." in still_b
    assert compiled["clips"][0]["compiled"]["request"] is not compiled["clips"][1]["compiled"]["request"]


def test_write_clip_files_emits_sequence(tmp_path: Path) -> None:
    clip = clip_from_walkthrough(walkthrough_module("asain-beauty"))
    write_clip_files(tmp_path, "asain-beauty", clip)
    seq_path = tmp_path / "asain-beauty-sequence.yaml"
    assert seq_path.is_file()
    payload = json.loads(seq_path.read_text(encoding="utf-8"))
    assert payload["kind"] == "sequence"
    assert payload["clips"][0]["path"].endswith("-canonical.yaml")
    assert "sample" not in payload["clips"][0]["path"]
    clip_file = tmp_path / payload["clips"][0]["path"]
    assert clip_file.is_file()


def test_read_output_includes_sequence() -> None:
    payload = read_output(REPO / "project", "european-handsome")
    seq = payload.get("sequence") or {}
    assert seq.get("kind") == "sequence"
    assert seq["policy"]["generation_unit"] == "clip"
    assert seq["clips"][0]["clip_id"].startswith("CLIP.european-handsome")
    assert payload.get("sequence_compile") is None or payload["sequence_compile"].get("fused_request") is None
    clip_id = seq["clips"][0]["clip_id"]
    by_clip = read_output(REPO / "project", "european-handsome", clip_id=clip_id)
    assert by_clip.get("clip_id") == clip_id
    assert by_clip.get("compiled")


def test_generate_clip_id_does_not_fuse(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("XAI_API_KEY", "xai-test")
    write_project(
        tmp_path,
        {
            "schema_version": "casops.project.v1",
            "id": "asain-beauty",
            "name": "asain-beauty",
            "title": "Asain Beauty",
            "brief": "Short vertical beauty clip.",
            "graph": {"nodes": [], "edges": []},
        },
        dry_run=False,
        create=True,
    )
    clip = clip_from_walkthrough(walkthrough_module("asain-beauty"))
    write_clip_files(tmp_path / "asain-beauty" / "output", "asain-beauty", clip)
    result = generate_project_media(
        tmp_path,
        "asain-beauty",
        engine="grok-imagine",
        clip_id=str(clip["clip_id"]),
        dry_run=True,
        post_json=lambda *_a, **_k: (_ for _ in ()).throw(AssertionError("network")),
        get_json=lambda *_a, **_k: (_ for _ in ()).throw(AssertionError("network")),
        get_bytes=lambda *_a, **_k: (_ for _ in ()).throw(AssertionError("network")),
    )
    assert result["error"] == "dry_run"
    assert result["clip_id"] == clip["clip_id"]
    assert result["compiled"]["request"].get("video")
    assert "fused" not in json.dumps(result["compiled"]["request"])
