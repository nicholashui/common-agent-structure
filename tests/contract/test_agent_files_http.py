"""Companion GET/PUT for on-disk agent configuration folders."""

from __future__ import annotations

import json
from pathlib import Path

from fastapi.testclient import TestClient

from casops.api.apps import create_control_plane
from casops.api.control import COMPANION_V3_PATHS, SPEC_V3_PATHS
from casops.compose.files import CONFIG_FOLDERS

REPO = Path(__file__).resolve().parents[2]
LIST = "/api/v3/agents/{agent_id}/files"
ITEM = "/api/v3/agents/{agent_id}/files/item"
MUTATION = {
    "x-casops-actor": "human_operator",
    "x-casops-reason": "update agent file",
    "x-casops-expected-parent": "none",
    "x-casops-dry-run": "true",
}


def _mini_root(tmp_path: Path) -> Path:
    root = tmp_path / "agents"
    folder = root / "demo.agent"
    (folder / "prompts").mkdir(parents=True)
    (folder / "prompts" / "primary.md").write_text("# hello\n", encoding="utf-8")
    (folder / "identity").mkdir()
    (folder / "identity" / "persona.json").write_text('{"role": "demo"}\n', encoding="utf-8")
    (folder / "corrigibility").mkdir()
    (folder / "corrigibility" / "attestation.json").write_text('{"status": "host"}\n', encoding="utf-8")
    (folder / "memory").mkdir()
    (folder / "memory" / "policy.json").write_text('{"mode": "none"}\n', encoding="utf-8")
    spec = {
        "agent_id": "demo.agent",
        "structure_id": "casops.common_agent.v3",
        "schema_version": "3.0",
        "role": "Demo",
    }
    (folder / "agent_spec.json").write_text(json.dumps(spec), encoding="utf-8")
    return root


def test_files_companion_in_openapi() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    spec = client.get("/openapi.json").json()
    assert ("GET", LIST) in COMPANION_V3_PATHS
    assert ("GET", ITEM) in COMPANION_V3_PATHS
    assert ("PUT", ITEM) in COMPANION_V3_PATHS
    assert LIST in spec["paths"]
    assert ITEM in spec["paths"]
    assert spec["paths"][ITEM].get("get")
    assert spec["paths"][ITEM].get("put")
    assert ("GET", LIST) not in SPEC_V3_PATHS
    assert ("PUT", ITEM) not in SPEC_V3_PATHS


def test_list_files_covers_sixteen_folders_on_director() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    response = client.get("/api/v3/agents/video.director/files")
    assert response.status_code == 200
    body = response.json()
    assert body["agent_id"] == "video.director"
    names = [row["name"] for row in body["folders"]]
    assert names == list(CONFIG_FOLDERS)
    prompts = next(row for row in body["folders"] if row["name"] == "prompts")
    assert any(item["path"] == "prompts/primary.md" for item in prompts["files"])
    identity = next(row for row in body["folders"] if row["name"] == "identity")
    assert any(item["path"] == "identity/background.json" for item in identity["files"])
    sources = next(row for row in body["folders"] if row["name"] == "sources")
    assert sources["present"] is True
    assert sources["files"]


def test_get_file_and_reject_escape() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    ok = client.get("/api/v3/agents/video.director/files/item", params={"path": "prompts/primary.md"})
    assert ok.status_code == 200
    body = ok.json()
    assert body["path"] == "prompts/primary.md"
    assert "Director" in body["content"] or "director" in body["content"].lower() or body["content"]
    assert body["writable"] is True
    escaped = client.get("/api/v3/agents/video.director/files/item", params={"path": "../agent_spec.json"})
    assert escaped.status_code != 200
    assert escaped.json()["error"]["code"] in {"SAF_EXFILTRATION", "INH_SURFACE_UNKNOWN"}


def test_put_requires_mutation_and_dry_run_does_not_write(tmp_path: Path) -> None:
    root = _mini_root(tmp_path)
    client = TestClient(create_control_plane(agents_root=root))
    unsigned = client.put(
        "/api/v3/agents/demo.agent/files/item",
        params={"path": "prompts/primary.md"},
        json={"content": "# unsigned\n"},
    )
    assert unsigned.status_code != 200
    assert unsigned.json()["error"]["code"] == "IMP_UNSIGNED"
    dry = client.put(
        "/api/v3/agents/demo.agent/files/item",
        params={"path": "prompts/primary.md"},
        json={"content": "# dry\n"},
        headers=MUTATION,
    )
    assert dry.status_code == 200
    assert dry.json()["saved"] is False
    assert dry.json()["dry_run"] is True
    assert (root / "demo.agent" / "prompts" / "primary.md").read_text(encoding="utf-8") == "# hello\n"
    live = dict(MUTATION)
    live["x-casops-dry-run"] = "false"
    written = client.put(
        "/api/v3/agents/demo.agent/files/item",
        params={"path": "prompts/primary.md"},
        json={"content": "# live\n"},
        headers=live,
    )
    assert written.status_code == 200
    assert written.json()["saved"] is True
    assert (root / "demo.agent" / "prompts" / "primary.md").read_text(encoding="utf-8") == "# live\n"


def test_put_attestation_and_agent_runtime_blocked(tmp_path: Path) -> None:
    root = _mini_root(tmp_path)
    client = TestClient(create_control_plane(agents_root=root))
    live = dict(MUTATION)
    live["x-casops-dry-run"] = "false"
    blocked = client.put(
        "/api/v3/agents/demo.agent/files/item",
        params={"path": "corrigibility/attestation.json"},
        json={"content": '{"hack": true}'},
        headers=live,
    )
    assert blocked.status_code != 200
    assert blocked.json()["error"]["code"] == "IMP_CORRIGIBILITY"
    runtime = dict(live)
    runtime["x-casops-actor"] = "agent_runtime"
    denied = client.put(
        "/api/v3/agents/demo.agent/files/item",
        params={"path": "prompts/primary.md"},
        json={"content": "# agent\n"},
        headers=runtime,
    )
    assert denied.status_code != 200
    assert denied.json()["error"]["code"] == "IMP_SELF_APPROVAL"
    assert (root / "demo.agent" / "prompts" / "primary.md").read_text(encoding="utf-8") == "# hello\n"
