from pathlib import Path
import json
import shutil

from casops.project_comms import (
    GOLD_BODY_PROBE,
    append_comm,
    apply_autopilot_cycle,
    apply_project_choices,
    assemble_generator_instruction,
    extract_sections,
    load_comms,
    run_asain_beauty_workflow,
    sample_prompt_path,
    _induce_envelope,
)
from casops.projects import read_project
from casops.project_instruction import human_brief_only, parse_emitted_instructions, pick_option


REPO = Path(__file__).resolve().parents[2]


def test_walkthrough_chat_matches_workflow() -> None:
    from casops.project_sample_walkthrough import DECISIONS, assembled_output, comms_payload, graph_bundle
    from casops.project_comms import GOLD_BODY_PROBE

    comms = comms_payload()
    graph = graph_bundle()
    assert comms["decisions"] == DECISIONS
    by_agent = {node["data"]["agent_id"]: node["data"] for node in graph["nodes"] if node["data"].get("agent_id")}
    for dec in DECISIONS:
        data = by_agent[dec["agent_id"]]
        assert data["options"] == dec["options"]
        assert data["chosen"] == dec["chosen"]
        assert data["selected_by"] == dec["selected_by"]
        if dec["selected_by"] != "human_operator":
            assert dec["select_reason"]
            assert data["select_reason"] == dec["select_reason"]
    assert "output-prompt" in [node["id"] for node in graph["nodes"]]
    out = assembled_output()
    gold = (REPO / "project" / "asain-beauty" / "sample" / "asain-beauty-prompt.txt").read_text(encoding="utf-8")
    assert GOLD_BODY_PROBE not in out
    assert out.strip() != gold.strip()
    assert "tiny light-brown mole sits just under the outer corner of the left eye" in out
    assert "faint blue vessels" in out
    assert "warm amber ring" in out
    assert "5–8°" in out
    assert "ribbed tank strap" in out
    assert "window grid" in out
    assert "Human asks" not in out
    from casops.project_sample_walkthrough import HUMAN_ASKS, HUMAN_DOMAIN_ROLES, CREATIVE_AGENT, INTENT_AGENT

    human_domain = [
        item
        for item in comms["items"]
        if item["from"] == "human_operator" and item["to"] in HUMAN_DOMAIN_ROLES
    ]
    assert {item["to"] for item in human_domain} == set(HUMAN_DOMAIN_ROLES)
    assert all(item["kind"] == "choice" for item in human_domain)
    assert not any(
        item["from"] == "human_operator"
        and item["to"] in {"video.cameraoperator", "video.critic"}
        for item in comms["items"]
    )
    assert not any(
        item["from"] == "human_operator"
        and item["kind"] == "instruction"
        and item["to"] != "create-project"
        for item in comms["items"]
    )
    for ask in HUMAN_ASKS:
        assert any(
            item["kind"] == "human_ask" and item["from"] == ask["from"] and ask["question"] in item["text"]
            for item in comms["items"]
        )
    parties = {(item["from"], item["to"]) for item in comms["items"]}
    assert ("create-project", INTENT_AGENT) in parties
    assert (INTENT_AGENT, CREATIVE_AGENT) in parties or (CREATIVE_AGENT, INTENT_AGENT) in parties
    kinds = {item["kind"] for item in comms["items"]}
    assert "choice" in kinds
    assert "human_ask" in kinds
    choosers = [item for item in comms["items"] if item["kind"] == "choice"]
    assert any("REASON:" in item["text"] and item["from"] != "human_operator" for item in choosers)


def test_output_prompt_path_uses_slug() -> None:
    from casops.project_comms import output_prompt_path, read_output, sample_prompt_path

    root = REPO / "project"
    assert output_prompt_path(root, "asain-beauty").name == "asain-beauty-prompt.txt"
    assert output_prompt_path(root, "european-handsome").name == "european-handsome-prompt.txt"
    assert sample_prompt_path(root, "european-handsome").name == "european-handsome-prompt.txt"
    payload = read_output(root, "european-handsome")
    assert payload["path"] == "project/european-handsome/output/european-handsome-prompt.txt"
    assert payload["exists"] is True
    assert "Rooftop phone-macro" in payload["text"]
    assert "asain-beauty-prompt.txt" not in payload["path"]
    assert output_prompt_path(root, "japanese-grandma-gta").name == "japanese-grandma-gta-prompt.txt"
    assert sample_prompt_path(root, "japanese-grandma-gta").name == "japanese-grandma-gta-prompt.txt"
    assert output_prompt_path(root, "hongkong-grandma-gta").name == "hongkong-grandma-gta-prompt.txt"
    assert sample_prompt_path(root, "hongkong-grandma-gta").name == "hongkong-grandma-gta-prompt.txt"


def test_european_handsome_walkthrough_chat_matches_workflow() -> None:
    from casops.project_european_handsome_walkthrough import (
        CREATIVE_AGENT,
        DECISIONS,
        GOLD_BODY_PROBE,
        HUMAN_ASKS,
        HUMAN_DOMAIN_ROLES,
        INTENT_AGENT,
        assembled_output,
        comms_payload,
        expected_autopilot_hops,
        graph_bundle,
        pack_map_suggestion,
    )
    from casops.project_comms import extract_sections

    comms = comms_payload()
    graph = graph_bundle()
    assert comms["decisions"] == DECISIONS
    by_agent = {node["data"]["agent_id"]: node["data"] for node in graph["nodes"] if node["data"].get("agent_id")}
    for dec in DECISIONS:
        data = by_agent[dec["agent_id"]]
        assert data["options"] == dec["options"]
        assert data["chosen"] == dec["chosen"]
        assert data["selected_by"] == dec["selected_by"]
    assert "output-prompt" in [node["id"] for node in graph["nodes"]]
    out = assembled_output()
    gold = (REPO / "project" / "european-handsome" / "sample" / "european-handsome-prompt.txt").read_text(
        encoding="utf-8"
    )
    assert GOLD_BODY_PROBE not in out
    assert out.strip() != gold.strip()
    assert "tiny pale scar cuts the left eyebrow" in out
    assert "flat brown mole sits on the right side of the neck" in out
    assert "broken capillary near the inner right eye" in out
    assert "7:20am" in out
    assert "6–10°" in out
    assert "faded black cotton tank" in out
    assert "thin silver chain" in out
    assert "grey-green" in out
    assert "hooks it away with his lower lip" not in out
    assert "no hair in the mouth" in out
    assert "never crosses the mouth" in out or "never into the mouth" in out
    assert "salt-damp tips" in out
    assert "sleep-swelling" in out
    assert "concrete roof" in out
    assert "tank strap" in out
    parts = extract_sections(out, ("Subject", "Hair", "Skin"))
    assert "tiny pale scar" in parts["Subject"]
    assert "tiny pale scar" not in parts["Hair"]
    assert "slightly wavy" in parts["Hair"]
    assert "broken capillary" in parts["Skin"]
    hops = expected_autopilot_hops()
    assert hops[0] == ("human_operator", "create-project", "instruction")
    assert hops[1] == ("create-project", INTENT_AGENT, "instruction")
    assert hops[-1] == ("video.promptengineer", "output-prompt", "output")
    human_domain = [
        item
        for item in comms["items"]
        if item["from"] == "human_operator" and item["to"] in HUMAN_DOMAIN_ROLES
    ]
    assert {item["to"] for item in human_domain} == set(HUMAN_DOMAIN_ROLES)
    assert not any(
        item["from"] == "human_operator" and item["to"] in {"video.cameraoperator", "video.critic"}
        for item in comms["items"]
    )
    for ask in HUMAN_ASKS:
        assert any(
            item["kind"] == "human_ask" and item["from"] == ask["from"] and ask["question"] in item["text"]
            for item in comms["items"]
        )
    parties = {(item["from"], item["to"]) for item in comms["items"]}
    assert ("create-project", INTENT_AGENT) in parties
    assert (INTENT_AGENT, CREATIVE_AGENT) in parties or (CREATIVE_AGENT, INTENT_AGENT) in parties
    suggestion = pack_map_suggestion(
        {
            "name": "european-handsome",
            "title": "European Handsome",
            "brief": "Short vertical beauty clip. Adult European man.",
            "audience": "18-34 on social",
            "duration": "15s",
            "outlets": "social",
            "risk": "low",
        }
    )
    assert suggestion["primary"] == "video.template.b"
    assert suggestion["suggestions"][0]["id"] == "video.template.b"
    assert "pack map" in suggestion["suggestions"][0]["label"]
    assert len(suggestion["suggestions"]) >= 2
    assert suggestion["catalog"]


def test_japanese_grandma_gta_walkthrough_chat_matches_workflow() -> None:
    from casops.project_japanese_grandma_gta_walkthrough import (
        CREATIVE_AGENT,
        DECISIONS,
        GOLD_BODY_PROBE,
        HUMAN_ASKS,
        HUMAN_DOMAIN_ROLES,
        INTENT_AGENT,
        assembled_output,
        comms_payload,
        expected_autopilot_hops,
        graph_bundle,
        pack_map_suggestion,
    )
    from casops.project_comms import extract_sections

    comms = comms_payload()
    graph = graph_bundle()
    assert comms["decisions"] == DECISIONS
    by_agent = {node["data"]["agent_id"]: node["data"] for node in graph["nodes"] if node["data"].get("agent_id")}
    for dec in DECISIONS:
        data = by_agent[dec["agent_id"]]
        assert data["options"] == dec["options"]
        assert data["chosen"] == dec["chosen"]
        assert data["selected_by"] == dec["selected_by"]
    assert "output-prompt" in [node["id"] for node in graph["nodes"]]
    out = assembled_output()
    gold = (REPO / "project" / "japanese-grandma-gta" / "sample" / "japanese-grandma-gta-prompt.txt").read_text(
        encoding="utf-8"
    )
    assert GOLD_BODY_PROBE not in out
    assert out.strip() != gold.strip()
    assert "silver four-wheel senior mobility scooter" in out
    assert "short permed silver" in out
    assert "Floral blouse" in out
    assert "beige cardigan" in out
    assert "rice paddies" in out
    assert "3 meters behind" in out
    assert "get the pickles home before supper" in out
    assert "wanted stars" in out
    assert "not Miami" in out or "No neon Vice City" in out
    parts = extract_sections(out, ("Subject", "Hair", "Skin"))
    assert "75–82" in parts["Subject"]
    assert "75–82" not in parts["Hair"]
    assert "permed silver" in parts["Hair"]
    assert "age spots" in parts["Skin"]
    hops = expected_autopilot_hops()
    assert hops[0] == ("human_operator", "create-project", "instruction")
    assert hops[1] == ("create-project", INTENT_AGENT, "instruction")
    assert hops[-1] == ("video.promptengineer", "output-prompt", "output")
    human_domain = [
        item
        for item in comms["items"]
        if item["from"] == "human_operator" and item["to"] in HUMAN_DOMAIN_ROLES
    ]
    assert {item["to"] for item in human_domain} == set(HUMAN_DOMAIN_ROLES)
    assert not any(
        item["from"] == "human_operator" and item["to"] in {"video.cameraoperator", "video.critic"}
        for item in comms["items"]
    )
    for ask in HUMAN_ASKS:
        assert any(
            item["kind"] == "human_ask" and item["from"] == ask["from"] and ask["question"] in item["text"]
            for item in comms["items"]
        )
    parties = {(item["from"], item["to"]) for item in comms["items"]}
    assert ("create-project", INTENT_AGENT) in parties
    assert (INTENT_AGENT, CREATIVE_AGENT) in parties or (CREATIVE_AGENT, INTENT_AGENT) in parties
    suggestion = pack_map_suggestion(
        {
            "name": "japanese-grandma-gta",
            "title": "Japanese Grandma GTA",
            "brief": "Short 16:9 chase clip. Adult Japanese grandma on a senior scooter.",
            "audience": "18-34 on social",
            "duration": "15s",
            "outlets": "social",
            "risk": "low",
        }
    )
    assert suggestion["primary"] == "video.template.b"
    assert suggestion["suggestions"][0]["id"] == "video.template.b"
    assert "pack map" in suggestion["suggestions"][0]["label"]
    assert len(suggestion["suggestions"]) >= 2
    assert suggestion["catalog"]


def test_hongkong_grandma_gta_walkthrough_chat_matches_workflow() -> None:
    from casops.project_hongkong_grandma_gta_walkthrough import (
        CREATIVE_AGENT,
        DECISIONS,
        GOLD_BODY_PROBE,
        HUMAN_ASKS,
        HUMAN_DOMAIN_ROLES,
        INTENT_AGENT,
        assembled_output,
        comms_payload,
        expected_autopilot_hops,
        graph_bundle,
        pack_map_suggestion,
    )
    from casops.project_comms import extract_sections

    comms = comms_payload()
    graph = graph_bundle()
    assert comms["decisions"] == DECISIONS
    by_agent = {node["data"]["agent_id"]: node["data"] for node in graph["nodes"] if node["data"].get("agent_id")}
    for dec in DECISIONS:
        data = by_agent[dec["agent_id"]]
        assert data["options"] == dec["options"]
        assert data["chosen"] == dec["chosen"]
        assert data["selected_by"] == dec["selected_by"]
    assert "output-prompt" in [node["id"] for node in graph["nodes"]]
    out = assembled_output()
    gold = (REPO / "project" / "hongkong-grandma-gta" / "sample" / "hongkong-grandma-gta-prompt.txt").read_text(
        encoding="utf-8"
    )
    assert GOLD_BODY_PROBE not in out
    assert out.strip() != gold.strip()
    assert "pineapple bun" in out
    assert "Mong Kok" in out
    assert "2–3 meters behind" in out
    assert "bring the pineapple bun home" in out
    assert "grey-white perm" in out or "grey-white permed" in out
    assert "Floral short-sleeve blouse" in out or "floral short-sleeve blouse" in out
    assert "wanted stars" in out
    parts = extract_sections(out, ("Subject", "Hair", "Skin"))
    assert "70–78" in parts["Subject"]
    assert "70–78" not in parts["Hair"]
    assert "grey-white perm" in parts["Hair"] or "grey-white permed" in parts["Hair"]
    assert "age spots" in parts["Skin"]
    hops = expected_autopilot_hops()
    assert hops[0] == ("human_operator", "create-project", "instruction")
    assert hops[1] == ("create-project", INTENT_AGENT, "instruction")
    assert hops[-1] == ("video.promptengineer", "output-prompt", "output")
    human_domain = [
        item
        for item in comms["items"]
        if item["from"] == "human_operator" and item["to"] in HUMAN_DOMAIN_ROLES
    ]
    assert {item["to"] for item in human_domain} == set(HUMAN_DOMAIN_ROLES)
    assert not any(
        item["from"] == "human_operator" and item["to"] in {"video.cameraoperator", "video.critic"}
        for item in comms["items"]
    )
    for ask in HUMAN_ASKS:
        assert any(
            item["kind"] == "human_ask" and item["from"] == ask["from"] and ask["question"] in item["text"]
            for item in comms["items"]
        )
    parties = {(item["from"], item["to"]) for item in comms["items"]}
    assert ("create-project", INTENT_AGENT) in parties
    assert (INTENT_AGENT, CREATIVE_AGENT) in parties or (CREATIVE_AGENT, INTENT_AGENT) in parties
    suggestion = pack_map_suggestion(
        {
            "name": "hongkong-grandma-gta",
            "title": "Hong Kong Grandma GTA",
            "brief": "Short 16:9 chase clip. Adult Hong Kong grandma walking home at night.",
            "audience": "18-34 on social",
            "duration": "15s",
            "outlets": "social",
            "risk": "low",
        }
    )
    assert suggestion["primary"] == "video.template.b"
    assert suggestion["suggestions"][0]["id"] == "video.template.b"
    assert "pack map" in suggestion["suggestions"][0]["label"]
    assert len(suggestion["suggestions"]) >= 2
    assert suggestion["catalog"]


def test_expected_autopilot_hops_match_chat_spine() -> None:
    from casops.project_comms import INDUCE_ROSTER
    from casops.project_sample_walkthrough import expected_autopilot_hops

    hops = expected_autopilot_hops()
    assert hops[0] == ("human_operator", "create-project", "instruction")
    assert hops[1] == ("create-project", "specials.intent-analysis-agent", "instruction")
    assert ("host_service", "output-prompt", "assembled") in hops
    assert hops[-1] == ("video.promptengineer", "output-prompt", "output")
    assert hops[hops.index(("host_service", "output-prompt", "assembled")) + 1] == (
        "video.promptengineer",
        "output-prompt",
        "output",
    )
    assert [row[0] for row in INDUCE_ROSTER][0] == "video.creativedirector"
    human_tos = [to for frm, to, kind in hops if frm == "human_operator" and kind == "choice"]
    assert "video.cameraoperator" not in human_tos
    assert "video.critic" not in human_tos
    assert "video.promptengineer" in human_tos


def test_assembled_output_splits_continuity_into_distinct_sections() -> None:
    from casops.project_sample_walkthrough import assembled_output

    out = assembled_output()
    parts = extract_sections(out, ("Subject", "Hair", "Skin"))
    subject, hair, skin = parts["Subject"], parts["Hair"], parts["Skin"]
    assert subject != hair
    assert hair != skin
    assert "tiny light-brown mole sits just under the outer corner of the left eye" in subject
    assert "tiny light-brown mole" not in hair
    assert "slight wave" in hair
    assert "slight wave" not in subject
    assert "faint blue vessels" in skin
    assert "faint blue vessels" not in subject
    assert "ribbed tank strap" in subject
    assert "ribbed tank strap" not in hair
    assert "ribbed tank strap" not in skin
    assert GOLD_BODY_PROBE not in out


def test_append_comm_and_tags(tmp_path: Path) -> None:
    root = tmp_path / "project"
    (root / "demo").mkdir(parents=True)
    (root / "demo" / "project.json").write_text(
        '{"schema_version":"casops.project.v1","id":"demo","name":"demo","title":"Demo","brief":"x","graph":{"nodes":[{"id":"create-project","type":"start","data":{"kind":"start","label":"Create Project"}}],"edges":[]}}',
        encoding="utf-8",
    )
    saved = append_comm(
        root,
        "demo",
        {
            "node_id": "create-project",
            "from": "human_operator",
            "to": "create-project",
            "kind": "instruction",
            "text": "hello",
            "output_tags": [{"project_id": "demo", "node_id": "create-project", "comm_id": "comm-0001", "label": "first"}],
        },
        dry_run=False,
    )
    assert saved["saved"] is True
    store = load_comms(root, "demo")
    assert store["items"][0]["text"] == "hello"
    assert store["items"][0]["output_tags"][0]["label"] == "first"


def test_append_comm_rewrites_off_origin_media(tmp_path: Path) -> None:
    root = tmp_path / "project"
    (root / "demo").mkdir(parents=True)
    (root / "demo" / "project.json").write_text(
        '{"schema_version":"casops.project.v1","id":"demo","name":"demo","title":"Demo","brief":"x","graph":{"nodes":[],"edges":[]}}',
        encoding="utf-8",
    )
    saved = append_comm(
        root,
        "demo",
        {
            "kind": "generated_media",
            "text": "clip",
            "media": {
                "name": "demo.mp4",
                "kind": "video",
                "url": "https://evil.example/steal.mp4",
                "poster": "https://evil.example/x.jpg",
                "poster_name": "demo-still.jpg",
            },
        },
        dry_run=False,
    )
    media = saved["item"]["media"]
    assert media["url"] == "/api/v3/projects/demo/output/file?name=demo.mp4"
    assert "evil" not in media["url"]
    assert media["poster"] == "/api/v3/projects/demo/output/file?name=demo-still.jpg"
    dropped = append_comm(
        root,
        "demo",
        {"kind": "generated_media", "text": "bad", "media": {"name": "../x", "kind": "video", "url": "/etc/passwd"}},
        dry_run=False,
    )
    assert dropped["item"]["media"] is None


def test_run_asain_beauty_uses_chat_fn_not_sample_copy(tmp_path: Path) -> None:
    root = tmp_path / "project"
    src = REPO / "project" / "asain-beauty"
    shutil.copytree(src, root / "asain-beauty")
    gold = (src / "sample" / "asain-beauty-prompt.txt").read_bytes()

    def fake_chat(agent_id: str, message: str) -> dict:
        if agent_id == "video.promptengineer" and "FAN-IN" in message:
            return {"reply": "next_instruction", "provider": "test_adapter", "agent_id": agent_id}
        if agent_id == "video.promptengineer":
            return {
                "reply": (
                    "THINKING: human brief is high-level; experts must propose options\n"
                    "OPTION 1: induce creativedirector first — owns thesis\n"
                    "RECOMMEND: 1\nDECIDE_BY: human\n"
                    "induce_call: video.creativedirector because thesis\n"
                    "induce_call: video.director because beats\n"
                    "induce_call: video.cinematographer because light\n"
                    "induce_call: video.mua_makeup because makeup\n"
                    "induce_call: video.cameraoperator because motor\n"
                    "induce_call: video.continuity because freeze\n"
                    "induce_call: video.critic because critique\n"
                    "Frame\nLIVE-video.promptengineer\nSound\nroom"
                ),
                "provider": "test_adapter",
                "agent_id": agent_id,
            }
        return {
            "reply": (
                f"THINKING: {agent_id} expert decision\n"
                f"OPTION 1: path A for {agent_id}\nOPTION 2: path B\n"
                "RECOMMEND: 1\nDECIDE_BY: human\n"
                f"LIVE-{agent_id}::{message[:40]}"
            ),
            "provider": "test_adapter",
            "agent_id": agent_id,
        }

    result = run_asain_beauty_workflow(
        root,
        "asain-beauty",
        first_instruction="",
        dry_run=False,
        agents_root=REPO / "agents",
        chat_fn=fake_chat,
    )
    human = next(item for item in result["comms"]["items"] if item["from"] == "human_operator")
    assert "CASOPS INSTRUCTION" not in human["text"]
    assert "induce_call:" not in human["text"]
    pe = next(node for node in result["graph"]["nodes"] if node["data"].get("agent_id") == "video.promptengineer")
    assert pe["data"]["options"]
    assert pe["data"]["thinking"]
    assert result["first_called"] == "video.promptengineer"
    assert result["live"] is True
    assert result["live_hops"] >= 7
    returns = [item for item in result["comms"]["items"] if item["kind"] == "return"]
    assert returns
    assert all(row["live"] for row in returns)
    assert all("LIVE-" in str(row["text"]) or "OPTION" in str(row["text"]) for row in returns)
    out = (root / "asain-beauty" / "output" / "asain-beauty-prompt.txt").read_text(encoding="utf-8")
    assert "video.director" in out or "LIVE-video.director" in out
    assert "path A" in out or "LIVE-" in out
    assert gold != out.encode("utf-8")
    assert GOLD_BODY_PROBE not in out
    sample_after = (root / "asain-beauty" / "sample" / "asain-beauty-prompt.txt").read_bytes()
    assert sample_after == gold
    from casops.project_comms import read_output

    payload = read_output(root, "asain-beauty")
    assert payload["path"] == "project/asain-beauty/output/asain-beauty-prompt.txt"
    assert "sample" not in Path(payload["path"]).parts
    assembled = [item for item in result["comms"]["items"] if item["kind"] == "assembled"]
    assert assembled
    assert "sample/ was not copied" in assembled[0]["text"]


def test_validate_accepts_comma_camera_lock_and_rejects_copy() -> None:
    from casops.project_comms import validate_prompt

    gold = (REPO / "project" / "asain-beauty" / "sample" / "asain-beauty-prompt.txt").read_text(encoding="utf-8")
    generated = (
        "clearly adult East Asian woman\n"
        "9:16 vertical phone-macro\n"
        "No traditional push, pull, pan, or orbit.\n"
    )
    report = validate_prompt(generated, gold)
    assert report["copied_sample"] is False
    assert report["exact"] is False
    assert report["missing_markers"] == []
    assert report["matched"] is True
    clone = validate_prompt(gold, gold)
    assert clone["copied_sample"] is True


def test_extract_and_assemble_uses_member_prose_not_gold() -> None:
    parts = extract_sections(
        "Subject\nclearly adult East Asian woman with a live mole lock.\nHair\nlong black, one side tucked.",
        ("Subject", "Hair"),
    )
    assert parts["Subject"].startswith("clearly adult")
    text, missing = assemble_generator_instruction(parts)
    assert "Subject" in text
    assert "live mole lock" in text
    assert "Hair" in text
    assert "[missing: Light]" in text
    assert "Light" in missing
    assert GOLD_BODY_PROBE not in text


def test_run_never_sends_gold_body_to_agents(tmp_path: Path) -> None:
    root = tmp_path / "project"
    src = REPO / "project" / "asain-beauty"
    shutil.copytree(src, root / "asain-beauty")
    gold = (src / "sample" / "asain-beauty-prompt.txt").read_text(encoding="utf-8")
    sent: list[str] = []

    def fake_chat(agent_id: str, message: str) -> dict:
        sent.append(message)
        if agent_id == "video.promptengineer" and "FAN-IN" in message:
            return {"reply": "next_instruction pass_02 cite members", "provider": "test_adapter", "agent_id": agent_id}
        if agent_id == "video.promptengineer":
            return {
                "reply": (
                    "induce_call: video.creativedirector because thesis and WHY\n"
                    "induce_call: video.director because beats\n"
                    "induce_call: video.cinematographer because light\n"
                    "induce_call: video.mua_makeup because makeup\n"
                    "induce_call: video.cameraoperator because motor\n"
                    "induce_call: video.continuity because freeze\n"
                    "induce_call: video.critic because critique\n"
                    "ASK_HUMAN: Confirm adult lock and whether a left-eye mole should be specified.\n"
                    "Frame\nGenerate a 15-second, 9:16 vertical phone-macro study of a clearly adult East Asian woman.\n"
                    "Sound\nLeaves outside, breath, no score."
                ),
                "provider": "test_adapter",
                "agent_id": agent_id,
            }
        if agent_id == "video.creativedirector":
            return {
                "reply": (
                    "Creative direction\nTHESIS: phone-macro skin study, not a UGC glass-skin ad.\n"
                    "WHY: the human brief asked for an adult East Asian woman phone-macro; hard sun and pores follow from that, not from a gold file.\n"
                    "ASK_HUMAN: Specify mole sites if identity must freeze them."
                ),
                "provider": "test_adapter",
                "agent_id": agent_id,
            }
        if agent_id == "video.continuity":
            return {
                "reply": (
                    "Subject\nThe subject is a clearly adult East Asian woman. A tiny light-brown mole sits just under the outer corner of the left eye.\n"
                    "Hair\nNatural long black, one side tucked.\n"
                    "Skin\nReal pores, pale freckles, T-zone oil, facial vellus."
                ),
                "provider": "test_adapter",
                "agent_id": agent_id,
            }
        if agent_id == "video.director":
            return {
                "reply": (
                    "0–3s | opening face smash\nStart already in extreme close-up.\n"
                    "3–6s | eye and skin macro\nTrue macro, slow crawl.\n"
                    "6–10s | nose and mouth super close-up\nNose and mouth fill the frame.\n"
                    "10–13s | climb back to the eye\nClimb, no orbit.\n"
                    "13–15s | eye hold\nHold one eye."
                ),
                "provider": "test_adapter",
                "agent_id": agent_id,
            }
        if agent_id == "video.cameraoperator":
            return {
                "reply": "Camera lock\nNo traditional push / pull / pan / orbit. Handheld 1-2mm breath crawl.",
                "provider": "test_adapter",
                "agent_id": agent_id,
            }
        if agent_id == "video.critic":
            return {
                "reply": (
                    "from_id: video.critic\nto_id: video.promptengineer\nseverity: major\n"
                    "artifact_ref: artifact://asain-beauty/critic/pass_01\n"
                    "claim: no beauty filter, no airbrushed skin; reject 4K and ring-light\n"
                    "evidence_refs: Bordwell Poetics of Cinema\ncorrelation_id: corr_asain_beauty_001"
                ),
                "provider": "test_adapter",
                "agent_id": agent_id,
            }
        if agent_id == "video.cinematographer":
            return {"reply": "Light\nHard 4pm sun through a thin white sheer.", "provider": "test_adapter", "agent_id": agent_id}
        if agent_id == "video.mua_makeup":
            return {
                "reply": "Makeup\nSunscreen and thin moisturizer, dusty-rose thin wet glaze, no fake eyelashes.",
                "provider": "test_adapter",
                "agent_id": agent_id,
            }
        return {"reply": f"LIVE-{agent_id}", "provider": "test_adapter", "agent_id": agent_id}

    result = run_asain_beauty_workflow(
        root,
        "asain-beauty",
        first_instruction="",
        dry_run=False,
        agents_root=REPO / "agents",
        chat_fn=fake_chat,
    )
    assert sent
    for message in sent:
        assert GOLD_BODY_PROBE not in message
        assert gold not in message
    mua_msgs = [message for message in sent if "to_agent_id=video.mua_makeup" in message]
    assert mua_msgs
    assert "4pm" not in mua_msgs[0]
    assert "ASK_HUMAN" in mua_msgs[0]
    critic_msgs = [message for message in sent if "to_agent_id=video.critic" in message]
    assert critic_msgs
    assert "critique_bus" in critic_msgs[0]
    assert "You are not first-called" in critic_msgs[0]
    out = (root / "asain-beauty" / "output" / "asain-beauty-prompt.txt").read_text(encoding="utf-8")
    assert out != gold
    assert GOLD_BODY_PROBE not in out
    assert "tiny light-brown mole sits just under the outer corner of the left eye" in out
    assert "0–3s | opening face smash" in out
    assert "No traditional push / pull / pan / orbit" in out
    assert "no beauty filter, no airbrushed skin" in out
    assert result["validation"]["copied_sample"] is False
    assert result["validation"]["exact"] is False
    assert sample_prompt_path(root, "asain-beauty").read_text(encoding="utf-8") == gold


def test_induce_briefs_stay_in_role() -> None:
    mua = _induce_envelope(
        brief_id="br_asain_01_mua",
        agent_id="video.mua_makeup",
        why="bare makeup",
        headings=("Makeup",),
        human="compile asain-beauty",
    )
    assert "must_cite=true" in mua
    assert "instruction_authority=false" in mua
    assert "ASK_HUMAN" in mua
    assert "induce_call:" in mua
    assert "4pm" not in mua
    assert "No traditional push" not in mua
    cin = _induce_envelope(
        brief_id="br_asain_01_cin",
        agent_id="video.cinematographer",
        why="light only",
        headings=("Light",),
        human="compile asain-beauty",
    )
    assert "dusty-rose" not in cin
    critic = _induce_envelope(
        brief_id="br_asain_01_crit",
        agent_id="video.critic",
        why="critique bus",
        headings=(),
        human="compile asain-beauty",
    )
    assert "return_schema=critique_bus.v1" in critic
    assert "closer" in critic.lower()
    assert GOLD_BODY_PROBE not in mua + cin + critic
    assert "tiny light-brown mole" not in mua
    assert "tiny light-brown mole" not in cin


def test_packed_howto_includes_host_collab() -> None:
    from casops.runtime.chat import operational_prompt

    agents = (
        "video.promptengineer",
        "video.director",
        "video.cinematographer",
        "video.mua_makeup",
        "video.cameraoperator",
        "video.continuity",
        "video.critic",
    )
    for agent_id in agents:
        raw = (REPO / "agents" / agent_id / "prompts" / "primary.md").read_text(encoding="utf-8")
        packed = operational_prompt(raw)
        assert "Host collab" in packed, agent_id
        assert "## Developer" not in packed, agent_id
        spec = json.loads((REPO / "agents" / agent_id / "agent_spec.json").read_text(encoding="utf-8"))
        outputs = spec["critique_edges"]["outputs"]
        assert "video.promptengineer" in outputs or agent_id == "video.promptengineer", agent_id
    pe = json.loads((REPO / "agents" / "video.promptengineer" / "agent_spec.json").read_text(encoding="utf-8"))
    for needed in (
        "video.director",
        "video.cinematographer",
        "video.mua_makeup",
        "video.cameraoperator",
        "video.continuity",
        "video.critic",
        "video.creativedirector",
        "video.aiqaconsistency",
    ):
        assert needed in pe["critique_edges"]["outputs"]
    cd = (REPO / "agents" / "video.creativedirector" / "prompts" / "primary.md").read_text(encoding="utf-8")
    from casops.runtime.chat import operational_prompt

    assert "ASK_HUMAN" in operational_prompt(cd)


def test_human_brief_stays_high_level() -> None:
    brief = human_brief_only(
        "CASOPS INSTRUCTION PASS first_called=video.promptengineer induce_call: video.director",
        {"title": "Asain Beauty", "brief": "Short vertical beauty clip."},
    )
    assert brief == "Asain Beauty. Short vertical beauty clip."
    assert "induce_call" not in brief
    parsed = parse_emitted_instructions(
        "THINKING: raking sun shows pores\nOPTION 1: hard 4pm sheer — phone-macro\nOPTION 2: overcast window — softer\nRECOMMEND: 1\nDECIDE_BY: human\n"
    )
    assert parsed["thinking"].startswith("raking")
    assert len(parsed["options"]) == 2
    assert parsed["recommend"] == "1"
    assert parsed["decide_by"] == "human"
    pick = pick_option(parsed, "2")
    assert pick and "overcast" in pick["label"]


def test_parse_induce_and_ask_human() -> None:
    parsed = parse_emitted_instructions(
        "induce_call: video.creativedirector because thesis + why\n"
        "ASK_HUMAN: Where should the mole sit?\n"
        "WHY: phone-macro because the brief asked for skin, not a shop CTA.\n"
    )
    assert parsed["induce_calls"][0]["agent_id"] == "video.creativedirector"
    assert parsed["human_asks"][0].startswith("Where should")
    assert "phone-macro" in parsed["why"]


def test_graph_has_output_end_node(tmp_path: Path) -> None:
    root = tmp_path / "project"
    src = REPO / "project" / "asain-beauty"
    shutil.copytree(src, root / "asain-beauty")

    def fake_chat(agent_id: str, message: str) -> dict:
        if agent_id == "video.promptengineer" and "FAN-IN" in message:
            return {"reply": "next_instruction pass_02", "provider": "test_adapter", "agent_id": agent_id}
        if agent_id == "video.promptengineer":
            return {
                "reply": "induce_call: video.director because beats\nASK_HUMAN: Confirm duration.\nFrame\n9:16 adult study\nSound\nroom tone",
                "provider": "test_adapter",
                "agent_id": agent_id,
            }
        return {
            "reply": f"0–3s | opening face smash\nlive {agent_id}",
            "provider": "test_adapter",
            "agent_id": agent_id,
        }

    result = run_asain_beauty_workflow(
        root,
        "asain-beauty",
        first_instruction="",
        dry_run=False,
        agents_root=REPO / "agents",
        chat_fn=fake_chat,
    )
    ids = [node["id"] for node in result["graph"]["nodes"]]
    kinds = {node["id"]: node["data"]["kind"] for node in result["graph"]["nodes"]}
    assert "output-prompt" in ids
    assert kinds["output-prompt"] == "output"
    assert result["graph"]["nodes"][next(i for i, n in enumerate(result["graph"]["nodes"]) if n["id"] == "output-prompt")]["data"]["io"]["outputs"] == []
    assert "human-ask" in ids
    assert result["status"] == "needs_hitl"
    assert result["human_asks"]
    assert GOLD_BODY_PROBE not in (root / "asain-beauty" / "output" / "asain-beauty-prompt.txt").read_text(encoding="utf-8")


def test_apply_choices_does_not_recall_agents(tmp_path: Path) -> None:
    root = tmp_path / "project"
    src = REPO / "project" / "asain-beauty"
    shutil.copytree(src, root / "asain-beauty")
    calls = {"n": 0}

    def fake_chat(agent_id: str, message: str) -> dict:
        calls["n"] += 1
        if agent_id == "video.promptengineer" and "FAN-IN" in message:
            return {"reply": "next", "provider": "test_adapter", "agent_id": agent_id}
        if agent_id == "video.promptengineer":
            return {
                "reply": "THINKING: t\nOPTION 1: a\ninduce_call: video.cinematographer because light\nFrame\nx",
                "provider": "test_adapter",
                "agent_id": agent_id,
            }
        return {
            "reply": "THINKING: light\nOPTION 1: hard sun\nOPTION 2: softbox\nRECOMMEND: 1\nDECIDE_BY: human\nLight\nhard sun",
            "provider": "test_adapter",
            "agent_id": agent_id,
        }

    first = run_asain_beauty_workflow(
        root,
        "asain-beauty",
        first_instruction="Short beauty clip",
        dry_run=False,
        agents_root=REPO / "agents",
        chat_fn=fake_chat,
    )
    hops = calls["n"]
    saved = load_comms(root, "asain-beauty")
    assert saved.get("autopilot", {}).get("status") == "aligned"
    assert saved.get("locks")
    assert any(item.get("kind") == "assembled" and item.get("from") == "host_service" for item in first["comms"]["items"])
    second = run_asain_beauty_workflow(
        root,
        "asain-beauty",
        first_instruction="Short beauty clip",
        dry_run=False,
        agents_root=REPO / "agents",
        chat_fn=fake_chat,
        choices={"video.cinematographer": "2"},
    )
    assert calls["n"] == hops
    cin = next(node for node in second["graph"]["nodes"] if node["data"].get("agent_id") == "video.cinematographer")
    assert cin["data"]["chosen"] == "2"
    assert "output-prompt" in [node["id"] for node in first["graph"]["nodes"]]


def test_human_lock_pick_does_not_clobber_expert_who_leads(tmp_path: Path) -> None:
    root = tmp_path / "project"
    src = REPO / "project" / "asain-beauty"
    shutil.copytree(src, root / "asain-beauty")
    record = read_project(root, "asain-beauty")
    result = apply_project_choices(
        root,
        "asain-beauty",
        record,
        {"video.promptengineer": "2"},
        dry_run=False,
    )
    pe = next(row for row in result["comms"]["decisions"] if row["agent_id"] == "video.promptengineer")
    assert pe["chosen"] == "1"
    assert pe["selected_by"] == "specials.general-creative-agent"
    assert pe["select_reason"]
    node = next(row for row in result["graph"]["nodes"] if row.get("data", {}).get("agent_id") == "video.promptengineer")
    assert node["data"]["chosen"] == "1"
    out = (root / "asain-beauty" / "output" / "asain-beauty-prompt.txt").read_text(encoding="utf-8")
    assert "Induce video.director first" not in out
    assert "6-second square talking-head" in out
    assert result["comms"].get("autopilot", {}).get("status") == "aligned"
    assert result["comms"].get("locks", {}).get("video.promptengineer") == "2"
    saved = load_comms(root, "asain-beauty")
    assert saved.get("autopilot", {}).get("status") == "aligned"
    assert saved.get("locks", {}).get("video.promptengineer") == "2"
    choice = next(
        item
        for item in reversed(result["comms"]["items"])
        if item.get("kind") == "choice" and item.get("to") == "video.promptengineer"
    )
    assert "OPTION 2" in choice["text"]


def test_autopilot_cycle_is_host_owned_and_capped(tmp_path: Path) -> None:
    root = tmp_path / "project"
    shutil.copytree(REPO / "project" / "asain-beauty", root / "asain-beauty")
    record = read_project(root, "asain-beauty")
    first = apply_autopilot_cycle(root, "asain-beauty", record, "continue", dry_run=False)
    assert first["comms"]["autopilot"]["cycle"] == "open"
    assert first["comms"]["autopilot"]["cycles"] == 1
    asks = [item for item in first["comms"]["items"] if item.get("kind") == "human_ask" and item.get("pass_id") == "pass_03"]
    assert any(item["from"] == "host_service" for item in asks)
    assert any(item["from"] == "video.critic" for item in asks)
    assert any(item["from"] == "video.continuity" for item in asks)
    again = apply_autopilot_cycle(root, "asain-beauty", record, "continue", dry_run=False)
    assert again["comms"]["autopilot"]["cycle"] == "stopped"
    picked = apply_project_choices(
        root,
        "asain-beauty",
        record,
        {"video.critic": "p3-2", "video.continuity": "p3-1"},
        dry_run=False,
    )
    # continue was capped to stop on second gate; p3 picks still record cycle_locks
    assert picked["comms"]["autopilot"].get("cycle_locks", {}).get("video.critic") == "p3-2"


def test_cycle_ready_appends_pass03_next_instruction(tmp_path: Path) -> None:
    root = tmp_path / "project"
    shutil.copytree(REPO / "project" / "asain-beauty", root / "asain-beauty")
    record = read_project(root, "asain-beauty")
    apply_autopilot_cycle(root, "asain-beauty", record, "continue", dry_run=False)
    picked = apply_project_choices(
        root,
        "asain-beauty",
        record,
        {"video.critic": "p3-2", "video.continuity": "p3-1"},
        dry_run=False,
    )
    assert picked["comms"]["autopilot"]["cycle"] == "ready"
    assert any(
        item.get("kind") == "next_instruction" and item.get("pass_id") == "pass_03"
        for item in picked["comms"]["items"]
    )
    assert any(
        item.get("kind") == "assembled" and item.get("pass_id") == "pass_03"
        for item in picked["comms"]["items"]
    )
    out = (root / "asain-beauty" / "output" / "asain-beauty-prompt.txt").read_text(encoding="utf-8")
    assert "no extra jewelry" in out or "no identity morph" in out


def test_cycle_stop_retracts_open_pass03_asks(tmp_path: Path) -> None:
    root = tmp_path / "project"
    shutil.copytree(REPO / "project" / "asain-beauty", root / "asain-beauty")
    record = read_project(root, "asain-beauty")
    apply_autopilot_cycle(root, "asain-beauty", record, "continue", dry_run=False)
    stopped = apply_autopilot_cycle(root, "asain-beauty", record, "stop", dry_run=False)
    assert stopped["comms"]["autopilot"]["cycle"] == "stopped"
    open_from = {
        item["from"]
        for item in stopped["comms"]["items"]
        if item.get("kind") == "human_ask"
        and item.get("pass_id") == "pass_03"
        and item.get("from") in {"video.critic", "video.continuity"}
    }
    answered = {
        item["to"]
        for item in stopped["comms"]["items"]
        if item.get("kind") == "choice"
        and item.get("from") == "human_operator"
        and item.get("to") in {"video.critic", "video.continuity"}
        and item.get("pass_id") == "pass_03"
    }
    assert not (open_from - answered)


def test_cycle_dry_run_does_not_write_comms(tmp_path: Path) -> None:
    root = tmp_path / "project"
    shutil.copytree(REPO / "project" / "asain-beauty", root / "asain-beauty")
    record = read_project(root, "asain-beauty")
    before = load_comms(root, "asain-beauty")
    result = apply_autopilot_cycle(root, "asain-beauty", record, "continue", dry_run=True)
    after = load_comms(root, "asain-beauty")
    assert result["dry_run"] is True
    assert result["saved"] is False
    assert after.get("autopilot", {}).get("cycle") == before.get("autopilot", {}).get("cycle")


def test_cycle_ask_option_ids_parse_on_real_hop() -> None:
    from casops.project_instruction import parse_emitted_instructions
    from casops.project_sample_walkthrough import CYCLE_ASKS, _ask_block

    fixture = REPO / "ui" / "tests" / "fixtures" / "cycle-ask-critic.txt"
    text = _ask_block(CYCLE_ASKS[0])
    assert text.strip() == fixture.read_text(encoding="utf-8").strip()
    parsed = parse_emitted_instructions(text)
    assert [row["id"] for row in parsed["options"]] == ["p3-1", "p3-2"]
    assert parsed["recommend"] == "p3-1"


def test_swarm_roster_is_read_only() -> None:
    from casops.swarms import compose_preview, list_swarms, read_swarm

    listed = list_swarms(REPO / "agents")
    ids = [row["swarm_id"] for row in listed["swarms"]]
    assert "video.asain-beauty" in ids
    payload = read_swarm(REPO / "agents", "video.asain-beauty")
    assert payload["runner"] is False
    assert "video.promptengineer" in payload["member_ids"]
    assert "specials.intent-analysis-agent" in payload["member_ids"]
    preview = compose_preview(REPO / "agents", "video.asain-beauty")
    assert preview["wrote_locks"] is False
