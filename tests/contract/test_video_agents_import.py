"""Imported VA video pack agents are CASOPS v3 baseline_safe folders."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema

from casops.api.apps import create_control_plane
from casops.registry.folder import validate_required_files
from casops.runtime.executor import Runtime
from casops.corrigibility.store import InvariantStore
from fastapi.testclient import TestClient

REPO = Path(__file__).resolve().parents[2]
SOURCE = Path(r"C:\Project\common-agent-swarm-ops\business\video\agents")
SCHEMA = json.loads((REPO / "schemas" / "agent" / "agent_spec.schema.json").read_text(encoding="utf-8"))
MUTATION = {
    "x-casops-actor": "host_service",
    "x-casops-reason": "test",
    "x-casops-expected-parent": "none",
    "x-casops-dry-run": "true",
}


def _source_ids() -> list[str]:
    ids = []
    if not SOURCE.is_dir():
        return ids
    for child in SOURCE.iterdir():
        spec_path = child / "agent_spec.json"
        if child.is_dir() and spec_path.is_file():
            payload = json.loads(spec_path.read_text(encoding="utf-8"))
            ids.append(str(payload.get("agent_id") or child.name))
    return sorted(ids)


def test_each_source_video_agent_is_imported_as_v3_folder() -> None:
    source_ids = _source_ids()
    assert source_ids, "source video agents not found"
    for agent_id in source_ids:
        folder = REPO / "agents" / agent_id
        check = validate_required_files(folder)
        assert check.ok, f"{agent_id}: {check.missing}"
        spec = json.loads((folder / "agent_spec.json").read_text(encoding="utf-8"))
        jsonschema.validate(spec, SCHEMA)
        assert spec["agent_id"] == agent_id
        assert spec["schema_version"] == "3.0"
        assert spec["structure_id"] == "casops.common_agent.v3"
        assert spec["production_activation_requested"] is False
        assert spec["model_policy"]["network_access"] is False
        assert spec["model_policy"]["provider"] == "local_deterministic"
        assert spec["allowed_tools"] == []
        assert spec["allowed_plugins"] == []
        memory = json.loads((folder / "memory" / "policy.json").read_text(encoding="utf-8"))
        assert memory["mode"] == "none"


def test_video_director_run_is_baseline_safe() -> None:
    runtime = Runtime(agents_root=REPO / "agents", store=InvariantStore.with_host_defaults())
    result = runtime.execute("video.director")
    assert result.agent_id == "video.director"
    assert result.adapter == "local_deterministic"
    assert result.memory_writes == []
    assert result.containment_stop is None
    payload = json.loads(result.artifact["text"])
    assert payload["agent_id"] == "video.director"
    assert payload["status"] == "ready"
    assert payload["note"].startswith("baseline_safe")


def test_control_plane_lists_video_director() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    body = client.get("/api/v3/agents").json()
    ids = [item["agent_id"] for item in body["agents"]]
    assert "video.director" in ids
    assert "video.accessibility" in ids
    headers = MUTATION
    preview = client.post("/api/v3/agents/video.director/compose-preview", headers=headers)
    assert preview.status_code == 200
    assert preview.json()["wrote_locks"] is False
    run = client.post("/api/v3/agents/video.director/runtime/run", headers=headers)
    assert run.status_code == 200
    assert run.json()["agent_id"] == "video.director"
