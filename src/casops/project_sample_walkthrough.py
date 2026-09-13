"""Characterization walkthrough for asain-beauty: Chat decisions aligned with Workflow nodes."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

FIRST_CALLED = "video.promptengineer"
SLUG = "asain-beauty"
HUMAN_BRIEF = "Short vertical beauty clip. Adult East Asian woman."

# Source of truth. Chat lists these; Workflow nodes copy the same fields.
DECISIONS: list[dict[str, Any]] = [
    {
        "id": "dec-01",
        "agent_id": "video.promptengineer",
        "node_id": "agent-video-promptengineer",
        "point": "Who leads the first expert hop",
        "thinking": "The human brief is only intent. A domain expert must propose a thesis before anyone writes clip grammar.",
        "options": [
            {"id": "1", "label": "Induce video.creativedirector first", "why": "Owns campaign thesis and WHY, not shot lists."},
            {"id": "2", "label": "Induce video.director first", "why": "Shot-led path; risks locking coverage before taste."},
            {"id": "3", "label": "Induce video.ugccreator first", "why": "Creator-ad grammar; fits shop CTA, not a skin study."},
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "human",
        "selected_by": "human_operator",
        "select_reason": "",
    },
    {
        "id": "dec-02",
        "agent_id": "video.creativedirector",
        "node_id": "agent-video-creativedirector",
        "point": "Creative thesis",
        "thinking": "Audience is 18-34 beauty shoppers, but the brief is a clip about a woman, not a product demo. Thesis must survive a 15s vertical without becoming an idol-template ad.",
        "options": [
            {
                "id": "1",
                "label": "Phone-macro skin study: hard sun, anti-idol, pores and identity marks readable",
                "why": "Matches 'adult woman' + beauty without inventing a shop CTA the human did not write.",
            },
            {
                "id": "2",
                "label": "Glass-skin UGC demo with product and CTA",
                "why": "Fits template B heuristics; the human did not name a product.",
            },
            {
                "id": "3",
                "label": "Studio beauty still then I2V",
                "why": "More control, but ring/softbox fights a phone-macro look.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "video.promptengineer",
        "selected_by": "video.promptengineer",
        "select_reason": "Parent orchestrator picked option 1 because the human brief is a person, not a product. Option 2 would write a UGC ad the human could have typed themselves if they wanted it. Option 3 implies studio gear nobody authorized.",
    },
    {
        "id": "dec-03",
        "agent_id": "video.director",
        "node_id": "agent-video-director",
        "point": "Coverage / beat map",
        "thinking": "Thesis is a 15s face-stuck macro. Coverage should be one climb on the face, not a portrait pullback.",
        "options": [
            {
                "id": "1",
                "label": "Five face-stuck beats: smash, eye/skin macro, nose/mouth super close-up, climb, one-eye hold",
                "why": "Keeps identity on one plane; no speech; features may clip the frame.",
            },
            {
                "id": "2",
                "label": "Three I2V clips 6/4/5 from a locked still",
                "why": "Imagine-family split; more vendor-shaped, still valid.",
            },
            {
                "id": "3",
                "label": "Wide-to-close hero plus product insert",
                "why": "Needs a product the brief never named.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "video.creativedirector",
        "selected_by": "video.creativedirector",
        "select_reason": "Creative director selected option 1 so the thesis (phone-macro skin study) is one continuous face crawl. Option 2 is a packing strategy, not coverage intent. Option 3 contradicts the no-product thesis already chosen.",
    },
    {
        "id": "dec-04",
        "agent_id": "video.cinematographer",
        "node_id": "agent-video-cinematographer",
        "point": "Light / lens",
        "thinking": "Macro skin needs raking natural sun so pores read. Softbox would flatten the thesis.",
        "options": [
            {
                "id": "1",
                "label": "Hard 4pm sun camera-left through half-open window and thin white sheer, 10–20cm phone-main, moving dapple",
                "why": "Raking key so pores and freckles read; curtain/leaves/hair cut the sun.",
            },
            {
                "id": "2",
                "label": "Overcast window, no sheer, even fill",
                "why": "Safer exposure, weaker pore contrast.",
            },
            {
                "id": "3",
                "label": "Beauty ring + large softbox",
                "why": "Idol catchlight; critic will reject.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "video.director",
        "selected_by": "video.director",
        "select_reason": "Director selected option 1 because the chosen beats stay 10-20cm on skin; a ring light (option 3) would fight every smash/macro beat. Option 2 is acceptable but weaker for the anti-idol thesis.",
    },
    {
        "id": "dec-05",
        "agent_id": "video.mua_makeup",
        "node_id": "agent-video-mua_makeup",
        "point": "Makeup lock",
        "thinking": "Bare lock only. Pore manifesto is continuity, not MUA.",
        "options": [
            {
                "id": "1",
                "label": "Sunscreen + thin moisturizer; natural brow; dusty-rose wet glaze; wet iris with real window catch; no fake lashes",
                "why": "Supports hard-sun pores; makeup stays a lock, not a filter.",
            },
            {
                "id": "2",
                "label": "Full base, contour, lash strip",
                "why": "Reads as influencer template under hard sun.",
            },
            {
                "id": "3",
                "label": "No product on skin at all",
                "why": "Legal, but dry flake may dominate the macro.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "video.creativedirector",
        "selected_by": "video.creativedirector",
        "select_reason": "Creative director selected option 1: enough moisture for sun speculars, not enough coverage to become option 2's idol face. Option 3 is a continuity texture choice, not makeup.",
    },
    {
        "id": "dec-06",
        "agent_id": "video.cameraoperator",
        "node_id": "agent-video-cameraoperator",
        "point": "Camera motor",
        "thinking": "One motor. Director beats are a crawl on the face; orbit would steal DoP's crop.",
        "options": [
            {
                "id": "1",
                "label": "Handheld 1-2mm breath crawl. No push / pull / pan / orbit",
                "why": "Matches face-stuck beats and 10-20cm working distance.",
            },
            {
                "id": "2",
                "label": "Slow planar slider across the cheek",
                "why": "Cleaner, less breath; slightly less 'phone'.",
            },
            {
                "id": "3",
                "label": "Gentle orbit around the head",
                "why": "Breaks the no-orbit motor and recenters the face.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "video.cinematographer",
        "selected_by": "video.cinematographer",
        "select_reason": "Cinematographer selected option 1 so the motor does not add a second move on top of hard-sun crop. Option 3 is rejected: orbit was never granted. Option 2 is fine if the human later wants less shake.",
    },
    {
        "id": "dec-07",
        "agent_id": "video.continuity",
        "node_id": "agent-video-continuity",
        "point": "Identity freeze",
        "thinking": "Identity freeze must come from human fills, not from a host gold paste. ASK_HUMAN, then freeze what they named.",
        "options": [
            {
                "id": "1",
                "label": "Unmarked adult freeze only",
                "why": "If the human names no moles.",
            },
            {
                "id": "2",
                "label": "Freeze human-named marks: left-eye mole, mouth-corner mole, sleep crease, 25-26 adult, black hair part, pale freckles",
                "why": "Matches what the sample human would have filled from asain-beauty-prompt.txt.",
            },
            {
                "id": "3",
                "label": "Allow identity drift across beats",
                "why": "Breaks the thesis; AIQA would fail.",
            },
        ],
        "recommend": "2",
        "chosen": "2",
        "decide_by": "human",
        "selected_by": "human_operator",
        "select_reason": "",
    },
    {
        "id": "dec-08",
        "agent_id": "video.critic",
        "node_id": "agent-video-critic",
        "point": "Critique / negatives",
        "thinking": "Check chosen locks against idol-template, poreless skin, ring light, 4K claims, orbit.",
        "options": [
            {
                "id": "1",
                "label": "Pass with Avoid: no beauty filter, no poreless skin, no ring-light, no orbit, no extra fingers, no morph",
                "why": "Chosen path already avoids those; write them as Avoid, not as a studio redo.",
            },
            {
                "id": "2",
                "label": "Blocker: send back for studio lighting",
                "why": "Would undo cinematographer's pick.",
            },
            {
                "id": "3",
                "label": "Blocker: require a product insert",
                "why": "Contradicts creative thesis.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "video.promptengineer",
        "selected_by": "video.promptengineer",
        "select_reason": "Orchestrator selected option 1 so negatives document the already-chosen path. Options 2 and 3 reopen decisions that parent experts already closed.",
    },
]

# Inferred from sample/asain-beauty-prompt.txt: what the human would have filled at ASK_HUMAN.
# Paraphrased so the gold body probe is never pasted. Create Project stays one-line intent.
HUMAN_FILLS: list[dict[str, str]] = [
    {
        "from": "video.promptengineer",
        "question": "Duration, aspect, and look?",
        "answer": (
            "15-second, 9:16 vertical, 4K ultra-photoreal live-action. Handheld phone-main close-up, "
            "roughly 50–70mm equivalent with a slight tele crop. Optical shallow depth of field: only the nearest "
            "skin plane is sharp; the ear side and rear hair fall off. No studio setup. No cinematic grade. "
            "No AI-smoothed face."
        ),
    },
    {
        "from": "video.promptengineer",
        "question": "If the engine can carry native audio, what room?",
        "answer": (
            "Extreme close-up room tone only: leaves outside, a very faint distant car, one swallow, breath. "
            "No score. No VO."
        ),
    },
    {
        "from": "video.continuity",
        "question": "Which identity marks must freeze for the whole 15s?",
        "answer": (
            "Clearly adult East Asian woman, about 25–26. Natural cool-toned East Asian face. Slightly long small oval, "
            "cheekbones gently lifted but not sharp, soft jawline, a visible philtrum groove. Real facial proportions. "
            "Not an influencer-template face. A tiny light-brown mole sits just under the outer corner of the left eye. "
            "Another almost unnoticeable mole sits outside the left mouth corner. One cheek still holds a very faint "
            "sleep crease that sunlight is slowly erasing. Do not morph."
        ),
    },
    {
        "from": "video.continuity",
        "question": "Hair freeze?",
        "answer": (
            "Natural long black with a slight wave, as if she just came inside from outdoors. Wind-tousled. "
            "One side casually tucked behind the ear, the other side fully down. Individual black strands fall across "
            "the forehead, lashes, and cheek. A few loose strands snag on the wet mouth corner while the camera is "
            "down on the lips. Fine vellus at the hairline, plus a little heat-lifted frizz. Every strand must read as "
            "real: thickness variation, messy flyaways, peach fuzz near the crown, translucent tips when the sun hits them."
        ),
    },
    {
        "from": "video.continuity",
        "question": "What skin texture must stay readable under hard sun?",
        "answer": (
            "Skin is the most important thing. Do not generate a traditional AI-beauty poreless face. "
            "On the cheeks, nostrils, and bridge you must clearly see: real pores, fine skin texture, slight uneven relief, "
            "a few pale freckles mostly on both sides of the bridge and the cheekbones, tiny pigment dots, natural moles, "
            "mild uneven tone, real nostril texture. Under-eyes are not a dark-circle template — thin skin with faint blue "
            "vessels plus 2–3 shallow micro-lines. T-zone oilier than the cheeks; a small sebum highlight collected at the "
            "alar crease / nasolabial junction, not an all-over oily face. Cheekbone highlight as actual specular skin, "
            "with pore shadows immediately beside it. Fine facial vellus. An almost invisible dry flake beside one nostril. "
            "Adult female skin, still clean, healthy, and clear."
        ),
    },
    {
        "from": "video.continuity",
        "question": "If the frame drops below the face, what wardrobe is allowed?",
        "answer": "If the frame drops to the collarbone, a thin off-white ribbed tank strap is allowed. Nothing else.",
    },
    {
        "from": "video.mua_makeup",
        "question": "Makeup lock?",
        "answer": (
            "Extremely light, almost none — sunscreen and a thin layer of moisturizer. "
            "Natural brows; hair direction and sparse spots in the brow are visible. "
            "Dark brown eyes, slightly sleepy narrow almond shape. Wet eyeballs. A very thin warm amber ring on the inner iris. "
            "Fine natural liner and lashes. No fake lashes. Lower lashes sparse and visible. "
            "Slim natural nose bridge. A real break where tip meets nostril. "
            "Lips are naturally full dusty rose, not coral-orange. A thin wet glaze only, pooling in the valleys of the lip lines. "
            "Keep full real lip texture, Cupid’s-bow relief, and corner creases."
        ),
    },
    {
        "from": "video.cinematographer",
        "question": "Light and working distance?",
        "answer": (
            "Hard late-afternoon sun, around 4pm. Sun hits from camera-left front and slightly above, first through a "
            "half-open window and a thin white sheer curtain, then onto the face. Clear highlight / shadow split. "
            "Real specular hits on the bridge, nose tip, highest point of the cheekbone, upper-lip glaze, and forehead. "
            "Tiny blowout allowed only on nose tip, upper-lip glaze, and cheekbone peak. "
            "As she and the camera drift a few millimeters, curtain, outdoor leaves, and hair keep cutting the sun, "
            "throwing moving stripe and dapple shadows across the face. Slight overexposure in those tiny hotspots is "
            "part of the phone-close-up look. Camera 10–20cm from the face. No studio soft light. No perfectly even lighting. "
            "No beauty filter, no smoothed skin, no plastic highlight. No ring-light catchlight."
        ),
    },
    {
        "from": "video.cinematographer",
        "question": "What must the eye catch as a real reflection?",
        "answer": (
            "Real reflections in pupil and iris: window grid, sheer curtain, a silhouette of the person shooting. "
            "Hard sunlight specular on the nose tip. No ring-light catchlight."
        ),
    },
    {
        "from": "video.director",
        "question": "Beat map and performance?",
        "answer": (
            "0–3s | opening face smash. Start already in an extreme facial close-up. Camera 10–20cm from the face. "
            "Her face almost fills the 9:16 frame. Slightly off-axis so you see at once: one eye, the bridge, the tip, "
            "both lips, part of a cheek. She looks quietly at the lens. Lips barely parted. No speech. Only very small "
            "breath; nostrils open and close with it. Eyes drift naturally. An occasional small blink. Breathing-scale "
            "handheld drift, about 1–2mm. Focus crawls on the nearest skin plane. Not electronic-stabilizer dead-still. "
            "Not shake-to-blur.\n"
            "3–6s | eye and skin macro. Camera eases even closer. True macro beauty close-up. Lens creeps sideways very "
            "slowly: eye → bridge → freckled cheek. No fast moves. When sun rakes the cheek, pores, freckles, pigment "
            "dots, and texture light up. Around 5s she does one slightly longer double blink; lids drop, then open slowly. "
            "The eye reflects window grid, sheer curtain, and the camera.\n"
            "6–10s | nose and mouth super close-up. Lens keeps drifting down. Frame becomes: nose tip + nostril + upper "
            "lip + lower lip + one cheek, filling almost the whole shot. Forehead and one eye get cropped off. Features "
            "are allowed to clip the frame edge. Do not keep a full centered face. Camera is extremely close to skin. "
            "Show real pores around the nostril, pale freckles on the cheek, oil on the nose tip, and that tiny dry patch "
            "beside the ala. Lips stay slightly open; a hint of teeth may flash. Around 8s she swallows once; the lower "
            "lip shifts a millimeter. Wet glaze picks up sun. One or two black strands brush the mouth corner and leave.\n"
            "10–13s | climb back to the eye. Camera crawls back up the face: mouth → bridge → eye. Her head turns a "
            "natural 5–8°, sinks about 3°, then settles. Not a posed head turn. A few black flyaways enter frame and "
            "cover near the eye. Gaze goes first to the window beside camera, then back to the lens. Light on the face "
            "changes. Curtain shadow slides from cheekbone onto the bridge. Some areas fall into shade; some get recut by sun.\n"
            "13–15s | eye hold. End on a super-close of one eye and the nearby bridge. One eye is the center. The pupil "
            "holds a sharp real reflection of window frame and leaves. Black strands hang in from the top of the frame. "
            "Sun through hair and curtain throws fine stripe shadows around the eye and cheek. She blinks once, small. "
            "A change at the mouth corner so slight you almost miss it. Hold about one second. End."
        ),
    },
    {
        "from": "video.cameraoperator",
        "question": "Camera motor?",
        "answer": (
            "No traditional push / pull / pan / orbit. This is a macro crawl stuck to the face. "
            "Same adult East Asian woman the whole time. Features, moles, hair color, and skin do not morph. "
            "Stable but with real handheld breath, about 1–2mm. Features may clip the frame edge. "
            "No jump cuts. No warped face. No melted teeth. No drifting eyes."
        ),
    },
    {
        "from": "video.critic",
        "question": "Must-avoid list?",
        "answer": (
            "no beauty filter, no airbrushed skin, no poreless skin, no plastic CGI face, no doll skin, "
            "no influencer template face, no studio softbox, no ring light catchlight, no fake eyelashes, "
            "no over-symmetrical face, no cinematic color grade, no talking, no posed smile to camera, "
            "no dolly zoom, no orbit shot, no extra fingers, no warped nose, no morphing identity."
        ),
    },
]


def _stamp(seq: int, **row: Any) -> dict[str, Any]:
    comm_id = f"comm-{seq:04d}"
    base = {
        "id": comm_id,
        "input_tags": [],
        "output_tags": [],
        "pass_id": "pass_01",
        "created_at": "2026-09-13T08:00:00Z",
        "live": False,
        "provider": "",
        "error": "",
        "honesty": "CHARACTERIZATION",
    }
    base.update(row)
    return base


def _option_block(dec: dict[str, Any]) -> str:
    lines = [
        f"THINKING: {dec['thinking']}",
        f"Decision point: {dec['point']}",
    ]
    for opt in dec["options"]:
        rec = " (recommend)" if opt["id"] == dec["recommend"] else ""
        lines.append(f"OPTION {opt['id']}: {opt['label']} — {opt['why']}{rec}")
    lines.append(f"RECOMMEND: {dec['recommend']}")
    lines.append(f"DECIDE_BY: {dec['decide_by']}")
    return "\n".join(lines)


def _choice_block(dec: dict[str, Any]) -> str:
    chosen = next((opt for opt in dec["options"] if opt["id"] == dec["chosen"]), dec["options"][0])
    who = dec["selected_by"]
    if who == "human_operator":
        reason = "Human selected this option at the decision point."
    else:
        reason = dec.get("select_reason") or f"{who} selected option {dec['chosen']}."
    return (
        f"SELECTED: OPTION {chosen['id']} — {chosen['label']}\n"
        f"SELECTED_BY: {who}\n"
        f"REASON: {reason}"
    )


def _fills_for(agent_id: str) -> list[dict[str, str]]:
    return [row for row in HUMAN_FILLS if row["from"] == agent_id]


def comms_items() -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    seq = 1
    items.append(
        _stamp(
            seq,
            node_id="create-project",
            **{"from": "human_operator", "to": "create-project", "kind": "instruction", "text": HUMAN_BRIEF},
        )
    )
    seq += 1
    items.append(
        _stamp(
            seq,
            node_id="create-project",
            **{
                "from": "create-project",
                "to": FIRST_CALLED,
                "kind": "instruction",
                "text": (
                    "Host pass (not human detail): first-called is the orchestrating expert. "
                    "Human brief stays high-level. Emit THINKING, OPTIONS, RECOMMEND, DECIDE_BY, induce_call."
                ),
            },
        )
    )
    seq += 1
    pe = DECISIONS[0]
    items.append(
        _stamp(
            seq,
            node_id=pe["node_id"],
            **{"from": FIRST_CALLED, "to": "create-project", "kind": "return", "text": _option_block(pe)},
        )
    )
    seq += 1
    items.append(
        _stamp(
            seq,
            node_id=pe["node_id"],
            **{"from": "human_operator", "to": FIRST_CALLED, "kind": "choice", "text": _choice_block(pe)},
        )
    )
    for fill in _fills_for(FIRST_CALLED):
        seq += 1
        items.append(
            _stamp(
                seq,
                node_id="human-ask",
                **{"from": fill["from"], "to": "human_operator", "kind": "human_ask", "text": fill["question"]},
            )
        )
        seq += 1
        items.append(
            _stamp(
                seq,
                node_id="human-ask",
                **{"from": "human_operator", "to": fill["from"], "kind": "instruction", "text": fill["answer"]},
            )
        )
    for dec in DECISIONS[1:]:
        seq += 1
        items.append(
            _stamp(
                seq,
                node_id="agent-video-promptengineer",
                **{
                    "from": FIRST_CALLED,
                    "to": dec["agent_id"],
                    "kind": "induce",
                    "text": (
                        f"induce_call: {dec['agent_id']} because {dec['point']}. "
                        "Return THINKING + OPTIONS + RECOMMEND + DECIDE_BY. Do not write the final novel."
                    ),
                },
            )
        )
        seq += 1
        items.append(
            _stamp(
                seq,
                node_id=dec["node_id"],
                **{"from": dec["agent_id"], "to": FIRST_CALLED, "kind": "return", "text": _option_block(dec)},
            )
        )
        for fill in _fills_for(dec["agent_id"]):
            seq += 1
            items.append(
                _stamp(
                    seq,
                    node_id="human-ask",
                    **{"from": fill["from"], "to": "human_operator", "kind": "human_ask", "text": fill["question"]},
                )
            )
            seq += 1
            items.append(
                _stamp(
                    seq,
                    node_id="human-ask",
                    **{"from": "human_operator", "to": fill["from"], "kind": "instruction", "text": fill["answer"]},
                )
            )
        seq += 1
        chooser = dec["selected_by"]
        items.append(
            _stamp(
                seq,
                node_id=dec["node_id"],
                **{"from": chooser, "to": dec["agent_id"], "kind": "choice", "text": _choice_block(dec)},
            )
        )
    seq += 1
    items.append(
        _stamp(
            seq,
            node_id="agent-video-promptengineer",
            **{
                "from": FIRST_CALLED,
                "to": FIRST_CALLED,
                "kind": "next_instruction",
                "text": (
                    "next_instruction pass_02 parent_pass_id=pass_01. "
                    "Compile the generator instruction from SELECTED options only. "
                    "Cite each decision id. Do not copy sample/."
                ),
                "pass_id": "pass_02",
            },
        )
    )
    seq += 1
    items.append(
        _stamp(
            seq,
            node_id="output-prompt",
            **{
                "from": FIRST_CALLED,
                "to": "output-prompt",
                "kind": "output",
                "text": assembled_output(),
                "pass_id": "pass_02",
            },
        )
    )
    return items


def _fill(agent_id: str) -> str:
    return " ".join(row["answer"] for row in HUMAN_FILLS if row["from"] == agent_id)


def _fill_q(agent_id: str, question_contains: str) -> str:
    for row in HUMAN_FILLS:
        if row["from"] == agent_id and question_contains.lower() in row["question"].lower():
            return row["answer"]
    return ""


def assembled_output() -> str:
    """Host-join SELECTED options + ASK_HUMAN fills. Never paste sample/."""
    picked = {dec["agent_id"]: next(opt for opt in dec["options"] if opt["id"] == dec["chosen"]) for dec in DECISIONS}
    thesis = picked["video.creativedirector"]["label"]
    frame = _fill_q("video.promptengineer", "Duration")
    sound = _fill_q("video.promptengineer", "native audio")
    identity = _fill_q("video.continuity", "identity marks")
    hair = _fill_q("video.continuity", "Hair freeze")
    skin = _fill_q("video.continuity", "skin texture")
    wardrobe = _fill_q("video.continuity", "wardrobe")
    makeup = _fill_q("video.mua_makeup", "Makeup")
    light = _fill_q("video.cinematographer", "Light")
    eye_catch = _fill_q("video.cinematographer", "eye catch")
    beats = _fill_q("video.director", "Beat map")
    motor = _fill_q("video.cameraoperator", "Camera motor")
    negatives = _fill_q("video.critic", "Must-avoid")
    return "\n".join(
        [
            "Generate from the locked decisions below. Host-assembled from Chat selections and ASK_HUMAN fills. sample/ is not a source.",
            "",
            "Creative direction",
            thesis + ".",
            "WHY: video.promptengineer selected this because the human brief is a person, not a product.",
            "",
            "Frame",
            frame,
            "",
            "Subject",
            identity,
            wardrobe,
            "",
            "Hair",
            hair,
            "",
            "Makeup",
            makeup,
            "",
            "Skin",
            skin,
            "",
            "Light",
            light,
            eye_catch,
            "",
            "Coverage / performance",
            beats,
            "",
            "Camera lock",
            motor,
            "",
            "Sound, if the model supports native audio",
            sound,
            "",
            "Negatives",
            negatives,
            "",
        ]
    )


def graph_bundle() -> dict[str, Any]:
    pe_outs = [dec["agent_id"] for dec in DECISIONS[1:]] + ["human-ask", "output"]
    nodes: list[dict[str, Any]] = [
        {
            "id": "create-project",
            "type": "start",
            "position": {"x": 80, "y": 200},
            "deletable": False,
            "data": {
                "kind": "start",
                "label": "Create Project",
                "title": "Asain Beauty",
                "brief": HUMAN_BRIEF,
                "audience": "18-34 beauty shoppers on social",
                "duration": "15s",
                "outlets": "social",
                "risk": "low",
                "agent_id": None,
                "io": {"inputs": [], "outputs": [FIRST_CALLED]},
            },
        },
        {
            "id": "agent-video-promptengineer",
            "type": "agent",
            "position": {"x": 400, "y": 200},
            "data": {
                "kind": "agent",
                "label": "video.promptengineer",
                "agent_id": "video.promptengineer",
                "reason": DECISIONS[0]["point"],
                "thinking": DECISIONS[0]["thinking"],
                "options": DECISIONS[0]["options"],
                "recommend": DECISIONS[0]["recommend"],
                "decide_by": DECISIONS[0]["decide_by"],
                "chosen": DECISIONS[0]["chosen"],
                "selected_by": DECISIONS[0]["selected_by"],
                "select_reason": DECISIONS[0]["select_reason"] or "Human confirmed the expert recommend.",
                "io": {"inputs": ["create-project"], "outputs": pe_outs},
            },
        },
    ]
    edges: list[dict[str, Any]] = [
        {
            "id": "e-create-promptengineer",
            "source": "create-project",
            "target": "agent-video-promptengineer",
            "sourceHandle": FIRST_CALLED,
            "targetHandle": "in",
            "type": "smoothstep",
            "label": FIRST_CALLED,
        }
    ]
    for index, dec in enumerate(DECISIONS[1:]):
        nodes.append(
            {
                "id": dec["node_id"],
                "type": "agent",
                "position": {"x": 760, "y": 20 + index * 130},
                "data": {
                    "kind": "agent",
                    "label": dec["agent_id"],
                    "agent_id": dec["agent_id"],
                    "reason": dec["point"],
                    "thinking": dec["thinking"],
                    "options": dec["options"],
                    "recommend": dec["recommend"],
                    "decide_by": dec["decide_by"],
                    "chosen": dec["chosen"],
                    "selected_by": dec["selected_by"],
                    "select_reason": dec["select_reason"]
                    or ("Human selected this option." if dec["selected_by"] == "human_operator" else ""),
                    "io": {
                        "inputs": [FIRST_CALLED],
                        "outputs": ["video.promptengineer"]
                        + (["human-ask"] if dec["agent_id"] == "video.continuity" else []),
                    },
                },
            }
        )
        edges.append(
            {
                "id": f"e-pe-{dec['agent_id'].replace('.', '-')}",
                "source": "agent-video-promptengineer",
                "target": dec["node_id"],
                "sourceHandle": dec["agent_id"],
                "targetHandle": "in",
                "type": "smoothstep",
                "label": dec["agent_id"],
            }
        )
    nodes.append(
        {
            "id": "human-ask",
            "type": "human",
            "position": {"x": 400, "y": 520},
            "data": {
                "kind": "human",
                "label": "Human",
                "reason": "Identity freeze is a human decision",
                "brief": "\n".join(f"Q ({row['from']}): {row['question']}\nA: {row['answer']}" for row in HUMAN_FILLS)[:900],
                "io": {"inputs": ["video.continuity"], "outputs": ["answer"]},
            },
        }
    )
    edges.append(
        {
            "id": "e-cont-human",
            "source": "agent-video-continuity",
            "target": "human-ask",
            "sourceHandle": "human-ask",
            "targetHandle": "in",
            "type": "smoothstep",
            "label": "ASK_HUMAN",
        }
    )
    out_text = assembled_output()
    nodes.append(
        {
            "id": "output-prompt",
            "type": "output",
            "position": {"x": 1120, "y": 200},
            "deletable": False,
            "data": {
                "kind": "output",
                "label": "Output",
                "reason": "project/asain-beauty/output/asain-beauty-prompt.txt",
                "brief": out_text[:280],
                "io": {"inputs": [FIRST_CALLED], "outputs": []},
            },
        }
    )
    edges.append(
        {
            "id": "e-pe-output",
            "source": "agent-video-promptengineer",
            "target": "output-prompt",
            "sourceHandle": "output",
            "targetHandle": "in",
            "type": "smoothstep",
            "label": "output",
        }
    )
    return {"nodes": nodes, "edges": edges}


def comms_payload() -> dict[str, Any]:
    return {
        "schema_version": "casops.project.comms.v1",
        "project_id": SLUG,
        "honesty": "CHARACTERIZATION",
        "walkthrough": "decision-points-v1",
        "note": "Sample walkthrough. Not live Grok hops. Workflow nodes copy these decisions.",
        "decisions": DECISIONS,
        "items": comms_items(),
    }


def write_asain_beauty_walkthrough(root: Path) -> dict[str, Any]:
    from casops.projects import read_project, write_project

    folder = Path(root) / SLUG
    folder.mkdir(parents=True, exist_ok=True)
    comms = comms_payload()
    (folder / "comms.json").write_text(json.dumps(comms, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    out = assembled_output()
    out_dir = folder / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "asain-beauty-prompt.txt").write_text(out if out.endswith("\n") else out + "\n", encoding="utf-8")
    record = read_project(root, SLUG)
    record["brief"] = HUMAN_BRIEF
    record["graph"] = graph_bundle()
    write_project(root, record, dry_run=False, create=False)
    return {"comms": comms, "graph": record["graph"], "output": out}
