from pathlib import Path

from casops.projects import (
    heuristic_rank,
    initial_graph,
    merge_suggestions,
    migrate_graph,
    normalize_slug,
    parse_llm_ids,
    suggest_next,
)

try:
    from casops.errors.exceptions import CasopsError
except ImportError:
    from casops.errors.exceptions import CasopsError  # type: ignore


def test_slug_rejects_path_escape() -> None:
    try:
        normalize_slug("../etc")
        raise AssertionError("expected error")
    except CasopsError:
        pass
    assert normalize_slug("Safety Recap") == "safety-recap"


def test_heuristic_training_picks_template_f() -> None:
    ranked = heuristic_rank({"brief": "factory-floor safety recap training", "duration": "3min", "outlets": "web", "risk": "medium"})
    assert ranked[0]["id"] == "video.template.f"


def test_heuristic_short_social_picks_hook() -> None:
    ranked = heuristic_rank({"brief": "tiktok spike", "duration": "15s", "outlets": "social", "risk": "low"})
    assert ranked[0]["id"] == "video.template.a"
    assert any(row["id"] == "video.scale.s1" for row in ranked)


def test_llm_ids_promoted() -> None:
    merged = merge_suggestions(
        {"brief": "tiktok spike", "duration": "15s", "outlets": "social"},
        "Use video.template.g and video.scale.s3",
        True,
    )
    assert merged["honesty"] == "CHARACTERIZATION"
    assert merged["suggestions"][0]["id"] == "video.template.g"
    assert merged["suggestions"][1]["id"] == "video.scale.s3"
    assert parse_llm_ids("no ids here") == []


def test_initial_graph_is_create_project_only() -> None:
    graph = initial_graph({"title": "Safety recap", "brief": "training"}, "video.template.f")
    assert [node["id"] for node in graph["nodes"]] == ["create-project"]
    assert graph["edges"] == []
    assert graph["nodes"][0]["data"]["io"]["outputs"][0] == "video.instructionaldesign"


def test_migrate_drops_catalog_subworkflow() -> None:
    graph = migrate_graph(
        {
            "nodes": [
                {"id": "create-project", "type": "start", "data": {"kind": "start", "label": "Create Project"}},
                {"id": "sub-workflow", "type": "workflow", "data": {"kind": "workflow", "sub_workflow_id": "video.template.f"}},
            ],
            "edges": [{"id": "e-create-sub", "source": "create-project", "target": "sub-workflow"}],
        },
        {"title": "x"},
        "video.template.f",
    )
    assert [node["id"] for node in graph["nodes"]] == ["create-project"]
    assert graph["edges"] == []


def test_suggest_next_start_and_parent_io() -> None:
    root = Path(__file__).resolve().parents[2] / "agents"
    start = suggest_next(
        root,
        template_id="video.template.f",
        from_id="create-project",
        from_agent_id=None,
        occupied=[],
    )
    ids = [row["id"] for row in start["suggestions"]]
    assert "video.instructionaldesign" in ids
    assert start["honesty"] == "CHARACTERIZATION"
    nxt = suggest_next(
        root,
        template_id="video.template.f",
        from_id="n-instructionaldesign",
        from_agent_id="video.instructionaldesign",
        occupied=["video.instructionaldesign"],
    )
    child_ids = [row["id"] for row in nxt["suggestions"]]
    assert "video.screenwriter" in child_ids
    assert nxt["parent_chat_id"] == "video.instructionaldesign"
    one_out = suggest_next(
        root,
        template_id="video.template.f",
        from_id="n-instructionaldesign",
        from_agent_id="video.instructionaldesign",
        occupied=["video.instructionaldesign"],
        out_bus="video.screenwriter",
    )
    assert one_out["out_bus"] == "video.screenwriter"
    assert one_out["suggestions"][0]["id"] == "video.screenwriter"
    assert len(one_out["outs"]) >= 2
    looped = suggest_next(
        root,
        template_id="video.template.f",
        from_id="n-screenwriter",
        from_agent_id="video.screenwriter",
        occupied=["video.instructionaldesign", "video.screenwriter"],
        out_bus="video.instructionaldesign",
    )
    back = next(row for row in looped["suggestions"] if row["id"] == "video.instructionaldesign")
    assert back.get("loopback") is True
    assert back["kind"] == "loop"
