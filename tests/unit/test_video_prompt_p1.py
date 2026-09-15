from copy import deepcopy

import pytest

from casops.project_generate import GENERATOR_TAGS, motion_prompt, still_prompt
from casops.video_prompt import (
    OWNER_PATHS,
    ClipSchemaError,
    empty_clip,
    load_profile,
    load_profiles,
    profile_for_tag,
    validate_clip,
)


def test_envelope_rejects_missing_intent_logline() -> None:
    clip = empty_clip(
        clip_id="CLIP.TEST.001",
        logline="A locked adult identity holds.",
        profile_id="xai.grok-imagine-video-1.5.i2v",
    )
    validate_clip(clip)
    broken = deepcopy(clip)
    broken["intent"] = {}
    with pytest.raises(ClipSchemaError, match="logline"):
        validate_clip(broken)


def test_envelope_rejects_wrong_schema_id() -> None:
    clip = empty_clip(
        clip_id="CLIP.TEST.002",
        logline="A locked adult identity holds.",
        profile_id="xai.grok-imagine-video-1.5.i2v",
    )
    clip["schema"] = "other"
    with pytest.raises(ClipSchemaError):
        validate_clip(clip)


def test_grok_i2v_profile_mode() -> None:
    profile = load_profile("xai.grok-imagine-video-1.5.i2v")
    assert profile["live"] is True
    assert profile["generator_tag"] == "grok-imagine"
    assert profile["identity"]["mode"] == "image_to_video"
    assert profile_for_tag("grok-imagine")["profile_id"] == "xai.grok-imagine-video-1.5.i2v"


def test_stub_profiles_cover_declared_fail_closed_tags() -> None:
    tags = {row["id"]: row["live"] for row in GENERATOR_TAGS}
    profiles = load_profiles()
    by_tag = {row["generator_tag"]: row for row in profiles}
    for tag, live in tags.items():
        assert tag in by_tag, tag
        if live:
            assert by_tag[tag]["live"] is True
        else:
            assert by_tag[tag]["live"] is False
            assert by_tag[tag]["evidence"]["execution_status"] == "not_tested"


def test_owner_paths_cover_domain_experts() -> None:
    for agent_id in (
        "video.creativedirector",
        "video.promptengineer",
        "video.director",
        "video.cinematographer",
        "video.mua_makeup",
        "video.cameraoperator",
        "video.continuity",
        "video.critic",
    ):
        assert OWNER_PATHS[agent_id]


def test_generate_prompts_unchanged_in_p1() -> None:
    text = (
        "Frame\n15-second, 9:16 vertical.\n\n"
        "Subject\nAdult East Asian woman. mole under left eye.\n\n"
        "Coverage / performance\n0–3s smash. 3–6s macro.\n\n"
        "Camera lock\nNo orbit.\n\n"
        "Sound\nRoom tone.\n"
    )
    still = still_prompt(text)
    motion = motion_prompt(text)
    assert "Do not animate" in still
    assert "Hold the composition" in motion
    assert "0–3s smash" in motion or "smash" in motion
    assert "Hair stays off the lips" in still
    assert "Do not chew or eat hair" in motion
