import json
from pathlib import Path

from casops.project_comms import GOLD_BODY_PROBES, walkthrough_module
from casops.project_european_handsome_walkthrough import GOLD_BODY_PROBE as EU_PROBE
from casops.project_hongkong_grandma_gta_walkthrough import GOLD_BODY_PROBE as HK_PROBE
from casops.project_japanese_grandma_gta_walkthrough import GOLD_BODY_PROBE as JP_PROBE
from casops.video_prompt.assemble import clip_from_walkthrough, parse_beats, project_clip, write_clip_files
from casops.video_prompt.schema import validate_clip

REPO = Path(__file__).resolve().parents[2]
SLUGS = ("asain-beauty", "european-handsome", "japanese-grandma-gta", "hongkong-grandma-gta")


def test_beats_parse_numeric_windows() -> None:
    rows = parse_beats(
        "0–3s | smash. Already close.\n3–6.5s | rake across the cheek.\nHold.",
        15,
    )
    assert rows[0]["start_s"] == 0
    assert rows[0]["end_s"] == 3
    assert "smash" in rows[0]["action"]
    assert rows[1]["end_s"] == 6.5


def test_four_walkthroughs_emit_valid_canonical_and_t4() -> None:
    probes = set(GOLD_BODY_PROBES) | {EU_PROBE, JP_PROBE, HK_PROBE}
    for slug in SLUGS:
        mod = walkthrough_module(slug)
        clip = clip_from_walkthrough(mod)
        validate_clip(clip)
        assert clip["target"]["profile_id"] == "xai.grok-imagine-video-1.5.i2v"
        assert clip["target"]["mode"] == "image_to_video"
        assert clip["generation"]["duration_s"] == 15
        shot = clip["creative"]["shots"][0]
        assert shot["action"]["beats"]
        assert clip["extensions"]["casops"]["project_id"] == slug
        text = project_clip(clip)
        assert "Creative direction" in text
        assert "Coverage / performance" in text
        assert "sample/ is not a source" in text
        for probe in probes:
            assert probe not in text
            blob = json.dumps(clip)
            assert probe not in blob
        sample = REPO / "project" / slug / "sample" / f"{slug}-prompt.txt"
        if sample.is_file():
            gold = sample.read_text(encoding="utf-8")
            assert text.strip() != gold.strip()


def test_write_clip_files_next_to_prompt(tmp_path: Path) -> None:
    mod = walkthrough_module("european-handsome")
    clip = clip_from_walkthrough(mod)
    text = write_clip_files(tmp_path, "european-handsome", clip)
    prompt = tmp_path / "european-handsome-prompt.txt"
    canon = tmp_path / "european-handsome-canonical.yaml"
    assert prompt.is_file()
    assert canon.is_file()
    assert "tiny pale scar" in text
    payload = json.loads(canon.read_text(encoding="utf-8"))
    assert payload["intent"]["logline"]
    assert payload["creative"]["shots"][0]["lighting"]["key"]
    assert payload["creative"]["shots"][0]["subjects"][0]["anchors"]["hair"]
    assert "forbid" in payload["constraints"]
    assert "hard" in payload["constraints"]
    compiled = tmp_path / "compiled" / "grok-imagine" / "compiled.request.json"
    assert compiled.is_file()
    request = json.loads(compiled.read_text(encoding="utf-8"))
    assert request["still"]["prompt"]
