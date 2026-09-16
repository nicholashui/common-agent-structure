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
    assert created.json()["dry_run"] is True
    assert created.json()["saved"] is False
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
    listed = client.get("/api/v3/programs")
    assert listed.status_code == 200
    assert any(row["id"] == "springlaunch" for row in listed.json()["programs"])
    got = client.get("/api/v3/programs/springlaunch")
    assert got.status_code == 200
    assert got.json()["name"] == "Spring Launch"
