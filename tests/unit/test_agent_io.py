"""Folder I/O contract: critique_edges, plugin schemas, protocols."""

from __future__ import annotations

import json
from pathlib import Path

from casops.compose.io import folder_io, io_from_spec
from casops.runtime.chat import build_chat_prompt, build_chat_system, normalize_history

REPO = Path(__file__).resolve().parents[2]


def test_io_from_spec_reads_critique_edges() -> None:
    spec = {
        "agent_id": "child",
        "role": "Editor",
        "prompt_reference": "prompts/primary.md",
        "critique_edges": {"inputs": ["video.critic", ""], "outputs": ["video.judge"]},
    }
    io = io_from_spec(spec)
    assert io["defined"] is True
    assert io["merged"] is False
    assert io["source"] == "critique_edges"
    assert io["inputs"] == ["video.critic"]
    assert io["outputs"] == ["video.judge"]
    assert io["role"] == "Editor"
    assert io["prompt_reference"] == "prompts/primary.md"


def test_io_from_spec_empty_edges_are_declared_but_undefined() -> None:
    io = io_from_spec({"agent_id": "t", "critique_edges": {"inputs": [], "outputs": []}})
    assert io["source"] == "critique_edges"
    assert io["defined"] is False
    assert io["inputs"] == []
    assert io["outputs"] == []


def test_io_from_spec_missing_edges() -> None:
    io = io_from_spec({"agent_id": "t", "role": "x"})
    assert io["source"] == "none"
    assert io["defined"] is False


def test_folder_io_includes_plugin_and_protocol_surfaces(tmp_path: Path) -> None:
    (tmp_path / "plugins").mkdir()
    (tmp_path / "plugins" / "registry.json").write_text(
        json.dumps(
            {
                "plugins": [
                    {
                        "id": "frame",
                        "input_schema": "schemas/frame-request.json",
                        "output_schema": "schemas/frame-result.json",
                    },
                    {"id": "no-schema"},
                ]
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "protocols").mkdir()
    (tmp_path / "protocols" / "compatibility.json").write_text(
        json.dumps({"schema_version": "3.0", "protocols": ["handoff.v1", {"id": "score.v1"}]}),
        encoding="utf-8",
    )
    (tmp_path / "agent_spec.json").write_text(
        json.dumps({"agent_id": "pack.frame", "critique_edges": {"inputs": ["a"], "outputs": ["b"]}}),
        encoding="utf-8",
    )
    io = folder_io(tmp_path)
    assert io["plugin_interfaces"] == [
        {
            "id": "frame",
            "input_schema": "schemas/frame-request.json",
            "output_schema": "schemas/frame-result.json",
        }
    ]
    assert io["protocols"] == ["handoff.v1", "score.v1"]
    assert io["defined"] is True


def test_video_director_folder_declares_peer_io() -> None:
    io = folder_io(REPO / "agents" / "video.director")
    assert io["defined"] is True
    assert "video.critic" in io["inputs"]
    assert "video.judge" in io["outputs"]


def test_template_folder_declares_empty_io_bus() -> None:
    io = folder_io(REPO / "agents" / "_template_v3")
    assert io["source"] == "critique_edges"
    assert io["defined"] is False
    assert io["inputs"] == []
    assert io["outputs"] == []


def test_build_chat_prompt_includes_system_io_history_and_message() -> None:
    prompt = build_chat_prompt(
        system="You are director.",
        io={"inputs": ["video.critic"], "outputs": ["video.judge"]},
        history=[{"role": "user", "content": "hi"}, {"role": "assistant", "content": "hello"}],
        message="continue",
    )
    assert "You are director." in prompt
    assert "video.critic" in prompt
    assert "video.judge" in prompt
    assert "hi" in prompt
    assert "hello" in prompt
    assert "continue" in prompt
    assert "free-text" in prompt


def test_build_chat_system_allows_human_text_input() -> None:
    system = build_chat_system(
        prompt="You are director.",
        io={"inputs": ["video.critic"], "outputs": ["video.judge"]},
    )
    assert "You are director." in system
    assert "video.critic" in system
    assert "free-text" in system


def test_normalize_history_keeps_last_user_assistant_turns() -> None:
    turns = normalize_history(
        [
            {"role": "system", "content": "nope"},
            {"role": "user", "content": "a"},
            {"role": "assistant", "content": "b"},
            {"role": "user", "content": "   "},
            "bad",
        ]
    )
    assert turns == [{"role": "user", "content": "a"}, {"role": "assistant", "content": "b"}]
