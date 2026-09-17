import json
from pathlib import Path

import pytest

from casops.errors.exceptions import CasopsError
from casops.program_comms import CHILD_FIRST_CALLED, CHILD_HUMAN_LOCKS, FIRST_AGENT_HOP, characterization_hops
from casops.project_comms import GOLD_BODY_PROBES
from casops.programs import (
    FIRST_CALLED,
    apply_cut_state,
    apply_finish,
    compile_program_sequence,
    concat_program,
    inspect_chain_frame,
    list_programs,
    normalize_code,
    program_sequence,
    read_program,
    request_still_sheet,
    spawn_child_projects,
    spawn_missing_locks,
    write_bible_and_storyboard,
    write_delivery_tree,
    write_program,
)
from casops.projects import read_project
from casops.project_sample_walkthrough import FIRST_CALLED as CLIP_FIRST_CALLED


def test_normalize_code_lowercase_no_spaces() -> None:
    assert normalize_code("SpringLaunch") == "springlaunch"
    assert normalize_code("spring launch") == "spring-launch"
    assert normalize_code("night-letter") == "night-letter"
    with pytest.raises(CasopsError):
        normalize_code("")
    with pytest.raises(CasopsError):
        normalize_code("1bad")
    with pytest.raises(CasopsError):
        normalize_code("../escape")


def test_write_and_list_program(tmp_path: Path) -> None:
    root = tmp_path / "program"
    dry = write_program(root, {"code": "alpha", "name": "Alpha"}, dry_run=True, create=True)
    assert dry["dry_run"] is True
    assert dry["saved"] is False
    assert dry["first_called"] == FIRST_CALLED
    assert dry["first_agent_hop"] == FIRST_AGENT_HOP
    assert dry["phase"] == "w0"
    assert dry["locks"]["generation_list"] is False
    assert not (root / "alpha" / "program.json").is_file()
    saved = write_program(root, {"code": "Alpha One", "name": "Alpha One"}, dry_run=False, create=True)
    assert saved["id"] == "alpha-one"
    assert saved["code"] == "alpha-one"
    assert saved["name"] == "Alpha One"
    assert saved["folder"] == "program/alpha-one"
    assert saved["first_called"] == "video.showrunner"
    assert (root / "alpha-one" / "program.json").is_file()
    assert (root / "alpha-one" / "generation-list.yaml").is_file()
    rows = list_programs(root)
    assert rows[0]["id"] == "alpha-one"
    loaded = read_program(root, "alpha-one")
    assert loaded["name"] == "Alpha One"
    assert loaded["locks"]["picture"] is False
    assert loaded["generation_list"]["scenes"] == []


def test_duplicate_program_rejected(tmp_path: Path) -> None:
    root = tmp_path / "program"
    write_program(root, {"code": "beta", "name": "Beta"}, dry_run=False, create=True)
    with pytest.raises(CasopsError):
        write_program(root, {"code": "beta", "name": "Beta 2"}, dry_run=False, create=True)


def _film(root: Path) -> dict:
    return write_program(root, {"code": "film", "name": "Film"}, dry_run=False, create=True)


def test_spawn_refused_without_dual_locks(tmp_path: Path) -> None:
    programs = tmp_path / "program"
    projects = tmp_path / "project"
    _film(programs)
    with pytest.raises(CasopsError) as exc:
        spawn_child_projects(programs, projects, "film", dry_run=False)
    assert "missing locks: generation_list,visual_bible" in exc.value.operator_message
    assert spawn_missing_locks(read_program(programs, "film")["locks"]) == ["generation_list", "visual_bible"]


def test_one_scene_two_segments_spawns_two_projects(tmp_path: Path) -> None:
    programs = tmp_path / "program"
    projects = tmp_path / "project"
    _film(programs)
    write_program(
        programs,
        {
            "code": "film",
            "name": "Film",
            "locks": {"generation_list": True, "visual_bible": True},
            "generation_list": {
                "scenes": [
                    {
                        "id": "sc1",
                        "title": "Opening",
                        "segments": [
                            {"id": "seg-a", "purpose": "Wide"},
                            {"id": "seg-b", "purpose": "Close"},
                        ],
                    }
                ]
            },
        },
        dry_run=False,
        create=False,
    )
    preview = spawn_child_projects(programs, projects, "film", dry_run=True)
    assert preview["dry_run"] is True
    assert preview["saved"] is False
    assert [row["slug"] for row in preview["preview"]] == ["film-seg-a", "film-seg-b"]
    assert not (projects / "film-seg-a" / "project.json").is_file()
    spawned = spawn_child_projects(programs, projects, "film", dry_run=False)
    assert spawned["project_ids"] == ["film-seg-a", "film-seg-b"]
    assert (projects / "film-seg-a" / "project.json").is_file()
    assert (projects / "film-seg-b" / "project.json").is_file()
    assert "sample" not in str(projects / "film-seg-a")


def test_finish_before_picture_lock_refused(tmp_path: Path) -> None:
    programs = tmp_path / "program"
    _film(programs)
    with pytest.raises(CasopsError) as exc:
        apply_finish(programs, "film", "color", dry_run=False)
    assert "missing locks: picture" in exc.value.operator_message
    locked = apply_finish(programs, "film", "picture_lock", dry_run=False)
    assert locked["locks"]["picture"] is True
    color = apply_finish(programs, "film", "color", dry_run=False)
    assert color["finish"] == "color"
    assert color["fused_request"] is None


def test_empty_program_sequence_fused_request_null(tmp_path: Path) -> None:
    programs = tmp_path / "program"
    _film(programs)
    compiled = compile_program_sequence(read_program(programs, "film"))
    assert compiled["fused_request"] is None
    assert program_sequence(read_program(programs, "film"))["fused_request"] is None


def test_program_sequence_fused_request_null(tmp_path: Path) -> None:
    programs = tmp_path / "program"
    _film(programs)
    write_program(
        programs,
        {
            "code": "film",
            "name": "Film",
            "generation_list": {"scenes": [{"id": "sc1", "segments": [{"id": "sega"}, {"id": "segb"}]}]},
        },
        dry_run=False,
        create=False,
    )
    record = read_program(programs, "film")
    sequence = program_sequence(record)
    assert sequence["fused_request"] is None
    assert sequence["concat"] == "post"
    assert len(sequence["clips"]) == 2
    compiled = compile_program_sequence(record)
    assert compiled["fused_request"] is None


def test_program_graph_from_hops_has_create_program_and_showrunner() -> None:
    from casops.program_comms import graph_from_hops

    graph = graph_from_hops()
    ids = [node["id"] for node in graph["nodes"]]
    assert "create-program" in ids
    assert "video.showrunner" in ids
    assert "specials.intent-analysis-agent" in ids
    assert graph["edges"]


def test_program_hops_showrunner_not_screenwriter() -> None:
    hops = characterization_hops()
    assert hops[0]["to"] == FIRST_AGENT_HOP
    assert hops[0]["from"] == "create-program"
    assert any(item["to"] == FIRST_CALLED and item["kind"] == "instruction" for item in hops)
    assert FIRST_CALLED == "video.showrunner"
    assert CLIP_FIRST_CALLED == "video.promptengineer"
    assert CLIP_FIRST_CALLED != FIRST_CALLED
    assert list(CHILD_HUMAN_LOCKS) == [
        "video.promptengineer",
        "video.director",
        "video.cinematographer",
        "video.mua_makeup",
        "video.continuity",
    ]
    assert CHILD_FIRST_CALLED == CLIP_FIRST_CALLED


def test_repo_has_no_night_letter_or_start_program() -> None:
    root = Path(__file__).resolve().parents[2] / "program"
    assert not (root / "night-letter" / "program.json").is_file()
    assert not (root / "nightletter" / "program.json").is_file()
    assert not (root / "start" / "program.json").is_file()


def test_create_stamps_chat_hops(tmp_path: Path) -> None:
    root = tmp_path / "program"
    write_program(root, {"code": "gamma", "name": "Gamma"}, dry_run=False, create=True)
    from casops.program_comms import load_program_comms

    hops = load_program_comms(root, "gamma")["items"]
    assert hops[0]["to"] == FIRST_AGENT_HOP
    assert (root / "gamma" / "comms.json").is_file()


def test_sample_never_written(tmp_path: Path) -> None:
    nested = tmp_path / "sample" / "program"
    with pytest.raises(CasopsError):
        write_program(nested, {"code": "nope", "name": "Nope"}, dry_run=False, create=True)


def test_generation_list_lock_refuses_empty_scene(tmp_path: Path) -> None:
    programs = tmp_path / "program"
    _film(programs)
    with pytest.raises(CasopsError) as exc:
        write_program(
            programs,
            {
                "code": "film",
                "name": "Film",
                "locks": {"generation_list": True},
                "generation_list": {"scenes": [{"id": "sc1", "segments": []}]},
            },
            dry_run=False,
            create=False,
        )
    assert "cannot lock generation_list" in exc.value.operator_message
    assert "sc1" in exc.value.operator_message
    locked = write_program(
        programs,
        {
            "code": "film",
            "name": "Film",
            "locks": {"generation_list": True},
            "generation_list": {
                "scenes": [{"id": "sc1", "segments": [{"id": "sega", "purpose": "Wide"}, {"id": "segb", "purpose": "Close"}]}]
            },
        },
        dry_run=False,
        create=False,
    )
    assert locked["locks"]["generation_list"] is True
    assert len(locked["generation_list"]["scenes"][0]["segments"]) == 2


def test_bible_storyboard_dry_run_writes_nothing(tmp_path: Path) -> None:
    programs = tmp_path / "program"
    record = _film(programs)
    record["generation_list"] = {
        "scenes": [{"id": "sc1", "segments": [{"id": "sega"}, {"id": "segb"}]}]
    }
    folder = programs / "film"
    dry = write_bible_and_storyboard(folder, record, dry_run=True)
    assert dry["written"] is False
    assert not (folder / "storyboard" / "sega.md").is_file()
    live = write_bible_and_storyboard(folder, record, dry_run=False)
    assert live["written"] is True
    assert (folder / "assets" / "approved" / "character-front.placeholder.txt").is_file()
    assert (folder / "storyboard" / "sega.md").is_file()
    assert (folder / "storyboard" / "segb.md").is_file()
    assert (folder / "bible" / "cast.md").is_file()


def test_fail_closed_still_tag_is_not_success() -> None:
    blocked = request_still_sheet("seedance")
    assert blocked["success"] is False
    assert blocked["status"] == "blocked"
    assert blocked.get("sheet") is None
    grok = request_still_sheet("grok-image")
    assert grok["success"] is False
    assert grok["dry_run_default"] is True


def test_spawn_inherit_bible_no_gold(tmp_path: Path) -> None:
    programs = tmp_path / "program"
    projects = tmp_path / "project"
    _film(programs)
    write_program(
        programs,
        {
            "code": "film",
            "name": "Film",
            "locks": {"generation_list": True, "visual_bible": True},
            "generation_list": {
                "scenes": [{"id": "sc1", "segments": [{"id": "seg-a", "purpose": "Wide"}, {"id": "seg-b", "purpose": "Close"}]}]
            },
        },
        dry_run=False,
        create=False,
    )
    spawned = spawn_child_projects(programs, projects, "film", dry_run=False)
    child = read_project(projects, "film-seg-a")
    inherit = child.get("inherit") or child.get("start", {}).get("inherit")
    assert inherit["program_id"] == "film"
    assert inherit["bible_ref"] == "program/film/bible/"
    assert inherit["storyboard_ref"] == "program/film/storyboard/seg-a.md"
    assert inherit["identity"]["path"] == "creative.shots.subjects"
    blob = json.dumps(child)
    assert "sample/" not in blob.replace("\\", "/")
    for probe in GOLD_BODY_PROBES:
        assert probe not in blob
    assert CLIP_FIRST_CALLED == "video.promptengineer"
    rejected = inspect_chain_frame(end_frame_ok=False, artifacts="identity drift")
    assert rejected["inherit_end_frame"] is False
    assert inspect_chain_frame(end_frame_ok=True)["inherit_end_frame"] is True
    assert spawned["project_ids"] == ["film-seg-a", "film-seg-b"]


def test_cut_states_and_delivery_tree(tmp_path: Path) -> None:
    programs = tmp_path / "program"
    _film(programs)
    folder = programs / "film"
    assert (folder / "delivery" / "specifications.yaml").is_file()
    assert (folder / "delivery" / "a11y.md").is_file()
    assert (folder / "delivery" / "captions" / ".keep").is_file()
    assert (folder / "delivery" / "archive-plan.md").is_file()
    assembly = apply_cut_state(programs, "film", "assembly", dry_run=False)
    assert assembly["cut_state"] == "assembly"
    assert assembly["locks"]["picture"] is False
    locked = apply_cut_state(programs, "film", "picture_lock", dry_run=False)
    assert locked["locks"]["picture"] is True
    blocked = concat_program(read_program(programs, "film"), tool_available=False)
    assert blocked["status"] == "blocked"
    assert blocked["fused_request"] is None
    assert "missing" in blocked["error"]
    with pytest.raises(CasopsError) as trailer:
        apply_finish(programs, "film", "trailer", dry_run=False)
    assert "silent spawn" in trailer.value.operator_message
    dry_delivery = write_delivery_tree(folder, read_program(programs, "film"), dry_run=True)
    assert dry_delivery["written"] is False
    assert dry_delivery["live_upload"] is False
