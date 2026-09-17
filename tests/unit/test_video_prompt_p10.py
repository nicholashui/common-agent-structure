from casops.project_comms import walkthrough_module
from casops.project_generate import GENERATOR_TAGS
from casops.video_prompt.assemble import clip_from_walkthrough
from casops.video_prompt.compile import compile_clip
from casops.video_prompt.dialects import dialect_prompts, strip_param_leaks
from casops.video_prompt.profiles import profile_for_tag


def test_strip_param_leaks_keeps_beat_windows() -> None:
    text = strip_param_leaks("15-second, 9:16 vertical. 0–3s | smash. No 8k masterpiece.")
    assert "9:16" not in text
    assert "15-second" not in text.lower() and "15 second" not in text.lower()
    assert "0–3s" in text or "smash" in text
    assert "8k" not in text.lower()
    assert "masterpiece" not in text.lower()


def test_grok_still_front_loads_subject() -> None:
    clip = clip_from_walkthrough(walkthrough_module("european-handsome"))
    compiled = compile_clip(clip, "xai.grok-imagine-video-1.5.i2v")
    still = compiled["prompt"]["still"]
    motion = compiled["prompt"]["motion"]
    lead = clip["creative"]["shots"][0]["subjects"][0]["identity"].split(".")[0]
    assert still.find(lead) < still.lower().find("photoreal")
    assert "9:16" not in still
    assert compiled["request"]["still"]["aspect_ratio"] == "9:16"
    assert "Hold the composition" in motion
    assert "opening smash" in motion.lower()
    assert compiled["guide"] == "spec/grok_imagine_operation_guide.md"


def test_fail_closed_dialect_preview_has_no_request() -> None:
    clip = clip_from_walkthrough(walkthrough_module("asain-beauty"))
    for tag in ("seedance", "ltx", "hailuo", "gpt-image", "wan"):
        profile = profile_for_tag(tag)
        compiled = compile_clip(clip, profile["profile_id"])
        assert compiled["status"] == "blocked"
        assert compiled["request"] == {}
        assert compiled["prompt"]["still"] or compiled["prompt"]["motion"]
        assert compiled.get("guide")


def test_gpt_image_tag_is_declared_fail_closed() -> None:
    row = next(item for item in GENERATOR_TAGS if item["id"] == "gpt-image")
    assert row["live"] is False
    profile = profile_for_tag("gpt-image")
    assert profile["live"] is False
    assert profile["identity"]["mode"] == "still"


def test_dialect_prompts_seedance_is_structured() -> None:
    clip = clip_from_walkthrough(walkthrough_module("asain-beauty"))
    dialect = dialect_prompts(clip, "seedance")
    assert "[Subject]" in dialect["motion"]
    assert "[Camera]" in dialect["motion"]


def test_wan_dialect_is_fail_closed_i2v_lock() -> None:
    clip = clip_from_walkthrough(walkthrough_module("asain-beauty"))
    dialect = dialect_prompts(clip, "wan")
    assert dialect["still"]
    assert "Keep the first-frame" in dialect["motion"]
    assert "9:16" not in dialect["still"]
    compiled = compile_clip(clip, "alibaba.wan-2.2.stub")
    assert compiled["status"] == "blocked"
    assert compiled["live"] is False
    assert compiled["request"] == {}
    assert compiled["guide"] == "spec/wan_operation_guide.md"
    assert compiled["generator_tag"] == "wan"
    profile = profile_for_tag("wan")
    assert profile["live"] is False
    assert "wan_operation_guide.md" in str(profile.get("notes") or "")
