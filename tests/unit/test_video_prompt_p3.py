from casops.project_comms import walkthrough_module
from casops.video_prompt.assemble import clip_from_walkthrough
from casops.video_prompt.patch import (
    OwnershipError,
    apply_choice_overlays,
    apply_owned_patch,
    overlays_from_comms,
    path_allowed,
)


def _clip():
    return clip_from_walkthrough(walkthrough_module("european-handsome"))


def test_cinematographer_cannot_change_identity() -> None:
    clip = _clip()
    before = clip["creative"]["shots"][0]["subjects"][0]["identity"]
    result = apply_owned_patch(
        clip,
        "video.cinematographer",
        {
            "creative": {
                "shots": [
                    {
                        "subjects": [{"identity": "rewritten face"}],
                        "lighting": {"key": "hard 7:20am sun camera-right"},
                    }
                ]
            }
        },
    )
    assert "creative.shots.0.subjects.0.identity" in result["rejected"]
    assert result["clip"]["creative"]["shots"][0]["subjects"][0]["identity"] == before
    assert "hard 7:20am" in result["clip"]["creative"]["shots"][0]["lighting"]["key"]
    assert any("lighting" in item for item in result["applied"])
    assert len(result["clip"]["creative"]["shots"][0]["subjects"]) == len(clip["creative"]["shots"][0]["subjects"])


def test_cinematographer_identity_strict_raises() -> None:
    clip = _clip()
    try:
        apply_owned_patch(
            clip,
            "video.cinematographer",
            {"creative": {"shots": [{"subjects": [{"identity": "nope"}]}]}},
            strict=True,
        )
    except OwnershipError as exc:
        assert "creative.shots.0.subjects.0.identity" in exc.rejected
    else:
        raise AssertionError("expected OwnershipError")


def test_critic_warn_on_camera_lands_in_diagnostics() -> None:
    clip = _clip()
    result = apply_owned_patch(
        clip,
        "video.critic",
        {
            "diagnostics": [
                {
                    "path": "creative.shots.camera.movement",
                    "severity": "warn",
                    "message": "Orbit was never granted.",
                }
            ]
        },
    )
    assert "provenance.diagnostics" in result["applied"]
    diags = result["clip"]["provenance"]["diagnostics"]
    assert diags[-1]["path"] == "creative.shots.camera.movement"
    assert "Orbit" in diags[-1]["message"]
    assert diags[-1]["agent_id"] == "video.critic"


def test_critic_cannot_replace_lighting_without_grant() -> None:
    clip = _clip()
    before = clip["creative"]["shots"][0]["lighting"]["key"]
    result = apply_owned_patch(
        clip,
        "video.critic",
        {"creative": {"shots": [{"lighting": {"key": "ring light"}}]}},
    )
    assert any("lighting" in item for item in result["rejected"])
    assert result["clip"]["creative"]["shots"][0]["lighting"]["key"] == before
    granted = apply_owned_patch(
        clip,
        "video.critic",
        {"creative": {"shots": [{"lighting": {"key": "approved fill"}}]}},
        granted=["creative.shots.lighting"],
    )
    assert granted["clip"]["creative"]["shots"][0]["lighting"]["key"] == "approved fill"


def test_critic_merges_constraints_forbid() -> None:
    clip = _clip()
    existing = list(clip["constraints"].get("forbid") or [])
    result = apply_owned_patch(
        clip,
        "video.critic",
        {"constraints": {"forbid": ["no hair in the mouth"]}},
    )
    forbid = result["clip"]["constraints"]["forbid"]
    assert "no hair in the mouth" in forbid
    assert len(forbid) >= len(existing)


def test_host_applies_overlays_without_rewriting_choice_text() -> None:
    clip = _clip()
    items = [
        {
            "kind": "choice",
            "from": "human_operator",
            "to": "video.critic",
            "text": "SELECTED: OPTION 1",
            "canonical_patch": {
                "diagnostics": [{"path": "creative.shots.camera.movement", "message": "keep motor still"}]
            },
        }
    ]
    overlays = overlays_from_comms(items)
    assert overlays[0]["agent_id"] == "video.critic"
    result = apply_choice_overlays(clip, overlays)
    assert items[0]["text"] == "SELECTED: OPTION 1"
    assert result["clip"]["provenance"]["diagnostics"][-1]["message"] == "keep motor still"


def test_path_allowed_matches_owner_prefixes() -> None:
    assert path_allowed("video.cinematographer", "creative.shots.0.lighting.key")
    assert not path_allowed("video.cinematographer", "creative.shots.0.subjects.0.identity")
    assert path_allowed("video.continuity", "creative.shots.0.subjects.0.identity")
