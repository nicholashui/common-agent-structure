"""Fixture importer maps swarm-ops case bodies to Chat prompts without v1 keys."""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))

from complex_agent_testcases import (  # noqa: E402
    MIN_CHAT_CASES,
    MIN_MESSAGE_CHARS,
    _bucket,
    build_complex_chat_cases,
)
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


def test_complex_cases_are_ten_distinct_and_in_role(tmp_path: Path) -> None:
    folder = tmp_path / "agents" / "video.director"
    folder.mkdir(parents=True)
    (folder / "SPEC.md").write_text(
        "## Responsibility\nOwns vision; issues shot intents.\n\n### Domain knowledge (research)\nShot intent is a contract.\n",
        encoding="utf-8",
    )
    spec = {
        "agent_id": "video.director",
        "role": "DirectorAgent (VA Domain Pack)",
        "does_not_own": ["Credentials", "Silent production activation"],
        "critique_edges": {"inputs": ["video.critic"], "outputs": ["video.judge"]},
    }
    cases = build_complex_chat_cases(
        folder,
        spec,
        [("Define shot language for a neon market", {"file": "vendor/x/cases.json", "repo": "vendor/common-agent-swarm-ops"})],
    )
    assert len(cases) == MIN_CHAT_CASES
    kinds = [item.kind for item in cases]
    assert len(set(kinds)) == MIN_CHAT_CASES
    assert sum(1 for item in cases if item.history) >= 3
    messages = [item.message for item in cases]
    assert len(set(messages)) == MIN_CHAT_CASES
    for item in cases:
        assert "video.director" in item.message
        assert len(item.message) >= MIN_MESSAGE_CHARS
        assert item.source.get("kind") == item.kind
        assert "CHARACTERIZATION" in item.source.get("honesty", "")
    assert "Define shot language" in cases[0].message
    assert "shot intent" in cases[0].message.lower() or "shot intents" in cases[0].message.lower()
    assert any("T3" in item.message for item in cases)
    assert any("XAI_API_KEY" in item.message or "personal information" in item.message.lower() for item in cases)
    assert all("(no declared" not in item.message for item in cases)


def _spec(folder: Path) -> dict:
    import json

    return json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))


def test_intent_cases_analyse_text_not_execute_the_vlog() -> None:
    folder = REPO / "agents" / "specials.intent-analysis-agent"
    cases = build_complex_chat_cases(
        folder,
        _spec(folder),
        [("Make a 6-day Osaka travel vlog for high retention", {"file": "vendor/x/cases.json"})],
    )
    text = cases[0].message.lower()
    assert "osaka" in text
    assert "analyse" in text or "analyze" in text or "locution" in text
    assert "bordwell" not in text
    assert "clip-t" not in text
    assert "sora" not in text
    assert "(no declared" not in cases[0].message
    assert _bucket("specials.intent-analysis-agent") == "intent"


def test_health_cases_are_snapshot_not_cinema() -> None:
    folder = REPO / "agents" / "common.health"
    cases = build_complex_chat_cases(folder, _spec(folder), [])
    blob = "\n".join(item.message for item in cases).lower()
    assert "snapshot" in blob or "folder_ok" in blob
    assert "bordwell" not in blob
    assert "clip-t" not in blob
    assert "sora" not in blob
    assert "50mm" not in blob
    assert "(no declared" not in blob
    assert _bucket("common.health") == "health"


def test_legal_cases_are_legal_not_cliche_pacing() -> None:
    folder = REPO / "agents" / "video.legal"
    cases = build_complex_chat_cases(
        folder,
        _spec(folder),
        [("Critique selection for cliché and pacing completeness (bounded refine)", {})],
    )
    first = cases[0].message.lower()
    assert "fair use" in first or "legal" in first or "likeness" in first
    assert "cliché" not in first and "cliche" not in first
    blob = "\n".join(item.message for item in cases)
    assert "CLIP-T" not in blob
    assert "Bordwell" not in blob
    assert _bucket("video.legal") == "legal"
