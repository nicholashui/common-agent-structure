"""Each scanned video.* pack has a unique cited study set in Chat-visible domain knowledge."""

from __future__ import annotations

from pathlib import Path

from casops.compose.folders import list_agent_ids, locate_agent_folder
from casops.runtime.chat import operational_prompt

REPO = Path(__file__).resolve().parents[2]


def test_video_agents_have_unique_cited_paper_sets() -> None:
    agents_root = REPO / "agents"
    ids = [agent_id for agent_id in list_agent_ids(agents_root) if agent_id.startswith("video.")]
    assert ids, "scan found no video.* agents"

    source_blocks: dict[str, str] = {}
    packed_systems: dict[str, str] = {}
    for agent_id in ids:
        folder = locate_agent_folder(agents_root, agent_id)
        assert folder is not None
        study = (folder / "sources" / "study" / "domain_knowledge.md").read_text(encoding="utf-8")
        assert "Craft family:" not in study
        assert "allowed_tools" in study
        assert "Sources (unique to this agent)" in study
        block = study.split("## Sources (unique to this agent)", 1)[1].split("## Shared", 1)[0].strip()
        assert block, agent_id
        assert block not in source_blocks, f"{agent_id} duplicates sources of {source_blocks.get(block)}"
        source_blocks[block] = agent_id

        packed = operational_prompt((folder / "prompts" / "primary.md").read_text(encoding="utf-8"))
        assert "Sora 2 API" not in packed
        assert "## Developer" not in packed
        assert "Unique sources:" in packed
        assert packed not in packed_systems, f"{agent_id} packed system matches {packed_systems.get(packed)}"
        packed_systems[packed] = agent_id

    assert "video.corrections" in ids
    corrections = locate_agent_folder(agents_root, "video.corrections")
    assert corrections is not None
    packed_corrections = operational_prompt((corrections / "prompts" / "primary.md").read_text(encoding="utf-8"))
    assert "IFCN" in packed_corrections
    assert "Rule of Six" not in packed_corrections
