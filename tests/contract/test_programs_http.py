from pathlib import Path

from fastapi.testclient import TestClient

from casops.api.control import COMPANION_V3_PATHS, create_control_plane

MUTATION = {
    "x-casops-actor": "human_operator",
    "x-casops-reason": "program test",
    "x-casops-expected-parent": "none",
    "x-casops-dry-run": "true",
}

LIVE = {**MUTATION, "x-casops-dry-run": "false"}
REPO = Path(__file__).resolve().parents[2]


def _client(tmp_path: Path) -> TestClient:
    return TestClient(
        create_control_plane(
            agents_root=REPO / "agents",
            programs_root=tmp_path / "program",
            projects_root=tmp_path / "project",
        )
    )


def test_programs_companion_in_openapi() -> None:
    client = TestClient(create_control_plane(agents_root=REPO / "agents"))
    spec = client.get("/openapi.json").json()
    for method, path in COMPANION_V3_PATHS:
        if "/programs" in path:
            assert path in spec["paths"], path


def test_dry_run_create_does_not_write(tmp_path: Path) -> None:
    client = _client(tmp_path)
    created = client.post(
        "/api/v3/programs",
        headers=MUTATION,
        json={"code": "demo", "name": "Demo"},
    )
    assert created.status_code == 200
    body = created.json()
    assert body["dry_run"] is True
    assert body["saved"] is False
    assert body["first_called"] == "video.showrunner"
    assert not (tmp_path / "program" / "demo" / "program.json").is_file()


def test_live_create_list_and_get(tmp_path: Path) -> None:
    client = _client(tmp_path)
    created = client.post(
        "/api/v3/programs",
        headers=LIVE,
        json={"code": "Spring Launch", "name": "Spring Launch"},
    )
    assert created.status_code == 200
    payload = created.json()
    assert payload["id"] == "springlaunch"
    assert payload["code"] == "springlaunch"
    assert payload["name"] == "Spring Launch"
    assert payload["first_called"] == "video.showrunner"
    listed = client.get("/api/v3/programs")
    assert listed.status_code == 200
    assert any(row["id"] == "springlaunch" for row in listed.json()["programs"])
    got = client.get("/api/v3/programs/springlaunch")
    assert got.status_code == 200
    assert got.json()["name"] == "Spring Launch"
    assert got.json()["locks"]["visual_bible"] is False


def test_spawn_without_locks_names_missing_locks(tmp_path: Path) -> None:
    client = _client(tmp_path)
    client.post("/api/v3/programs", headers=LIVE, json={"code": "reel", "name": "Reel"})
    rejected = client.post("/api/v3/programs/reel/spawn", headers=LIVE, json={})
    assert rejected.status_code != 200
    error = rejected.json().get("error") or {}
    blob = " ".join(str(error.get(key) or "") for key in ("message", "detail"))
    assert "generation_list" in blob
    assert "visual_bible" in blob


def test_spawn_two_segments_and_sequence(tmp_path: Path) -> None:
    client = _client(tmp_path)
    client.post("/api/v3/programs", headers=LIVE, json={"code": "reel", "name": "Reel"})
    empty = client.put(
        "/api/v3/programs/reel",
        headers=LIVE,
        json={
            "name": "Reel",
            "locks": {"generation_list": True},
            "generation_list": {"scenes": [{"id": "sc1", "segments": []}]},
        },
    )
    assert empty.status_code != 200
    assert "generation_list" in str(empty.json())
    updated = client.put(
        "/api/v3/programs/reel",
        headers=LIVE,
        json={
            "name": "Reel",
            "locks": {"generation_list": True, "visual_bible": True},
            "generation_list": {
                "scenes": [{"id": "sc1", "segments": [{"id": "one"}, {"id": "two"}]}]
            },
        },
    )
    assert updated.status_code == 200
    assert (tmp_path / "program" / "reel" / "storyboard" / "one.md").is_file()
    assert (tmp_path / "program" / "reel" / "delivery" / "specifications.yaml").is_file()
    spawned = client.post("/api/v3/programs/reel/spawn", headers=LIVE, json={})
    assert spawned.status_code == 200
    body = spawned.json()
    assert body["project_ids"] == ["reel-one", "reel-two"]
    assert (tmp_path / "project" / "reel-one" / "project.json").is_file()
    seq = client.get("/api/v3/programs/reel/sequence")
    assert seq.status_code == 200
    payload = seq.json()
    assert payload["sequence"]["fused_request"] is None
    assert payload["compile"]["fused_request"] is None
    finish = client.post("/api/v3/programs/reel/finish", headers=LIVE, json={"kind": "mix"})
    assert finish.status_code != 200
    assert "picture" in str(finish.json())
    comms = client.get("/api/v3/programs/reel/comms")
    assert comms.status_code == 200
    items = comms.json()["items"]
    assert items[0]["to"] == "specials.intent-analysis-agent"
    assert comms.json()["first_called"] == "video.showrunner"
    assert comms.json()["child_first_called"] == "video.promptengineer"
