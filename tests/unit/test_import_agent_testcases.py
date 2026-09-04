"""Fixture importer maps swarm-ops case bodies to Chat prompts without v1 keys."""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))

from import_agent_testcases import (  # noqa: E402
    CASOPS_TO_SWARM_FOLDER,
    fallback_prompts,
    prompt_from_case,
    swarm_case_path,
)


def test_prompt_from_video_goal() -> None:
    text = prompt_from_case(
        {
            "id": "tc1",
            "name": "video.director offline case 1",
            "body": {"goal": "Define shot language", "allow_network": False},
        }
    )
    assert text == "Define shot language"


def test_prompt_from_specials_text_not_v1_keys() -> None:
    text = prompt_from_case(
        {
            "id": "tc1",
            "body": {"text": "Make a 6-day Osaka travel vlog", "channel": "video_brief"},
        }
    )
    assert text == "Make a 6-day Osaka travel vlog"
    assert "primary_intent" not in text


def test_prompt_from_artifact_ref() -> None:
    text = prompt_from_case({"body": {"artifact_ref": "look_bible_stub", "mode": "score"}})
    assert "look_bible_stub" in text
    assert "network" in text.lower() or "vision" in text.lower()


def test_intent_agent_maps_to_underscore_folder() -> None:
    assert (
        CASOPS_TO_SWARM_FOLDER["specials.intent-analysis-agent"]
        == "specials.intent_analysis_agent"
    )


def test_swarm_case_path_none_when_missing(tmp_path: Path) -> None:
    assert swarm_case_path(tmp_path, "specials.planner-agent") is None


def test_fallback_prompts_use_live_role() -> None:
    rows = fallback_prompts("specials.planner-agent", "Special_Agent data-only configuration", "Owns planner")
    assert len(rows) == 3
    assert all("specials.planner-agent" in row for row in rows)
    assert "production" in rows[2].lower()
