"""Chat packs identity + operational prompt; it does not dump SKILL.md or tool design notes."""

from __future__ import annotations

from pathlib import Path

from casops.runtime.chat import operational_prompt, pack_chat_context

REPO = Path(__file__).resolve().parents[2]


def _spec(folder: Path) -> dict:
    import json

    return json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))


def test_operational_prompt_drops_developer_tools_and_rethink() -> None:
    raw = (REPO / "agents" / "video.director" / "prompts" / "primary.md").read_text(encoding="utf-8")
    packed = operational_prompt(raw)
    assert "DirectorAgent" in packed
    assert "Owns vision" in packed
    assert "Sora 2 API" not in packed
    assert "RETHINK_100" not in packed
    assert "## Developer" not in packed


def test_pack_clips_to_context_json_and_omits_disabled_surfaces() -> None:
    folder = REPO / "agents" / "video.director"
    spec = _spec(folder)
    packed = pack_chat_context(
        folder,
        spec,
        {"inputs": ["video.critic"], "outputs": ["video.judge"]},
        message="neon night market walk-and-talk",
        history=[],
    )
    public = packed["public"]
    names = {row["name"]: row for row in public["segments"]}
    assert names["memory"]["budget"] == 0
    assert names["memory"]["included"] is False
    assert names["tools"]["included"] is False
    assert names["task"]["tokens"] <= names["task"]["budget"]
    assert names["policy"]["tokens"] <= names["policy"]["budget"]
    assert "skills/SKILL.md" in public["omitted"]
    assert public["skills"] == []
    assert public["compaction"] == "disabled"
    assert "video.director" in packed["system"]
    assert "DirectorAgent" in packed["system"]
    assert "Sora 2 API" not in packed["system"]
    assert "Do not call tools" in packed["system"]


def test_pack_differs_across_agents() -> None:
    director = REPO / "agents" / "video.director"
    intent = REPO / "agents" / "specials.intent-analysis-agent"
    left = pack_chat_context(director, _spec(director), {}, message="hello", history=[])
    right = pack_chat_context(intent, _spec(intent), {}, message="hello", history=[])
    assert left["system"] != right["system"]
    assert "video.director" in left["system"]
    assert "intent-analysis" in right["system"]
