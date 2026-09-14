"""Characterization walkthrough for european-handsome: Chat decisions aligned with Workflow nodes."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from casops.project_instruction import split_continuity_craft
from casops.project_sample_walkthrough import (
    CREATIVE_AGENT,
    FIRST_CALLED,
    HUMAN_DOMAIN_ROLES,
    INTENT_AGENT,
    _ask_block,
    _choice_block,
    _chosen_option,
    _option_block,
    _stamp,
)

SLUG = "european-handsome"
HUMAN_BRIEF = "Short vertical beauty clip. Adult European man."
GOLD_BODY_PROBE = "A few teeth may flash and disappear."

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
        "decide_by": "specials.general-creative-agent",
        "selected_by": "specials.general-creative-agent",
        "select_reason": "Creative-agent confirmed the intent-analysis reading: a person-led clip, so thesis (creativedirector) precedes coverage.",
    },
    {
        "id": "dec-02",
        "agent_id": "video.creativedirector",
        "node_id": "agent-video-creativedirector",
        "point": "Creative thesis",
        "thinking": "The draft names an adult European man, not a product. Thesis must survive 15s vertical without influencer tan or studio beauty.",
        "options": [
            {
                "id": "1",
                "label": "Rooftop phone-macro: lived-in handsome, hard morning sun, anti-influencer skin",
                "why": "Matches 'adult man' + beauty without inventing a shop CTA.",
            },
            {
                "id": "2",
                "label": "Grooming UGC demo with product and CTA",
                "why": "Fits template heuristics; the human did not name a product.",
            },
            {
                "id": "3",
                "label": "Studio still then I2V",
                "why": "More control, but softbox fights a rooftop phone-macro look.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "video.promptengineer",
        "selected_by": "video.promptengineer",
        "select_reason": "Parent orchestrator picked option 1 because the brief is a person on a roof, not a product. Option 2 invents a CTA. Option 3 implies studio gear nobody authorized.",
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
                "label": "Five face-stuck beats: smash, skin rake, mouth/chin, climb to shaded eye, one-eye hold",
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
        "select_reason": "Creative director selected option 1 so the rooftop thesis is one continuous face crawl. Option 2 is packing, not coverage. Option 3 contradicts the no-product thesis.",
    },
    {
        "id": "dec-04",
        "agent_id": "video.cinematographer",
        "node_id": "agent-video-cinematographer",
        "point": "Light / lens",
        "thinking": "Macro skin needs raking cold morning sun so pores and stubble read. Softbox would flatten the thesis.",
        "options": [
            {
                "id": "1",
                "label": "Hard 7:20am sun camera-right slightly behind, 10–20cm phone-main, rooftop rake",
                "why": "Cold split so pores, freckles, and stubble shadows read; no ring-light.",
            },
            {
                "id": "2",
                "label": "Overcast even fill",
                "why": "Safer exposure, weaker pore contrast.",
            },
            {
                "id": "3",
                "label": "Beauty ring + large softbox",
                "why": "Influencer catchlight; critic will reject.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "video.director",
        "selected_by": "video.director",
        "select_reason": "Director selected option 1 because the beats stay 10-20cm on skin; a ring light would fight every smash/macro beat.",
    },
    {
        "id": "dec-05",
        "agent_id": "video.mua_makeup",
        "node_id": "agent-video-mua_makeup",
        "point": "Makeup lock",
        "thinking": "No makeup. Pore manifesto is continuity, not MUA.",
        "options": [
            {
                "id": "1",
                "label": "No makeup; muted rose mouth; grey-green iris; raw brows; no liner or lashes",
                "why": "Supports hard-sun pores; face stays a lock, not a filter.",
            },
            {
                "id": "2",
                "label": "Grooming base, brow gel, lip balm shine",
                "why": "Reads as influencer template under hard sun.",
            },
            {
                "id": "3",
                "label": "Styled beard oil and contour",
                "why": "Contradicts overnight stubble.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "video.creativedirector",
        "selected_by": "video.creativedirector",
        "select_reason": "Creative director selected option 1: no product on skin. Option 2 becomes a male-model template. Option 3 fights the overnight-growth lock.",
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
                "craft": (
                    "No dolly, no orbit, no beauty push-in. A macro crawl stuck to the face. "
                    "Same adult European man the whole time. Mole, brow scar, stubble pattern, hair color, and skin do not morph. "
                    "Handheld breath, not gimbal glass. No jump cuts. No warped mouth. No extra teeth. "
                    "Hair stays off the lips for the whole clip."
                ),
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
        "select_reason": "Cinematographer selected option 1 so the motor does not add a second move on top of hard-sun crop. Option 3 is rejected: orbit was never granted.",
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
                "label": "Freeze named marks: left-brow scar, right-neck mole, overnight stubble, grey-green iris",
                "why": "Matches the rooftop man the draft implied.",
            },
            {
                "id": "3",
                "label": "Allow identity drift across beats",
                "why": "Breaks the thesis; AIQA would fail.",
            },
        ],
        "recommend": "2",
        "chosen": "2",
        "decide_by": FIRST_CALLED,
        "selected_by": FIRST_CALLED,
        "select_reason": "Human already froze named marks on the ASK_HUMAN lock; orchestrator confirms option 2.",
    },
    {
        "id": "dec-08",
        "agent_id": "video.critic",
        "node_id": "agent-video-critic",
        "point": "Critique / negatives",
        "thinking": "Check chosen locks against poreless skin, tanned influencer, ring light, orbit, styled beard.",
        "options": [
            {
                "id": "1",
                "label": "Pass with Avoid: no beauty filter, no poreless skin, no ring-light, no orbit, no styled beard, no morph",
                "why": "Chosen path already avoids those; write them as Avoid.",
                "craft": (
                    "no beauty filter, no airbrushed skin, no poreless skin, no plastic CGI face, no doll skin, "
                    "no male-model template face, no overly tanned European influencer skin, no studio softbox, "
                    "no ring light catchlight, no styled beard, no fake lashes, no over-symmetrical face, "
                    "no golden-hour grade, no talking, no posed smile to camera, no dolly zoom, no orbit shot, "
                    "no extra fingers, no warped nose, no morphing identity, "
                    "no hair in the mouth, no chewing or eating hair, no lip-hooking a strand, no hair between the teeth."
                ),
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
        "select_reason": "Orchestrator selected option 1 so negatives document the already-chosen path.",
    },
]

INTENT_DECISION: dict[str, Any] = {
    "id": "dec-intent",
    "agent_id": INTENT_AGENT,
    "node_id": "agent-specials-intent-analysis-agent",
    "point": "What the draft is asking for",
    "thinking": (
        "Locution: a short vertical beauty clip of an adult European man. "
        "Illocution: directive to produce a clip. Triggerable as a container, not as shot grammar. "
        "No product, speech, or studio is evidenced."
    ),
    "options": [
        {"id": "1", "label": "Person-led rooftop skin study (no product named)", "why": "Draft names a man, not a SKU or CTA."},
        {"id": "2", "label": "Paid grooming UGC ad", "why": "Would invent a shop CTA the draft omitted."},
        {"id": "3", "label": "Talking-head explainer", "why": "Draft did not ask for speech."},
    ],
    "recommend": "1",
    "chosen": "1",
    "decide_by": CREATIVE_AGENT,
    "selected_by": CREATIVE_AGENT,
    "select_reason": "Creative-agent takes the person-led reading; a UGC ad or explainer would exceed the draft.",
}

CREATIVE_DECISION: dict[str, Any] = {
    "id": "dec-creative",
    "agent_id": CREATIVE_AGENT,
    "node_id": "agent-specials-general-creative-agent",
    "point": "Campaign concept / execution framework",
    "thinking": (
        "Intent is a person, not a product. The framework must survive a short vertical without becoming a tanned-influencer ad. "
        "Domain experts lock craft via ASK_HUMAN options."
    ),
    "options": [
        {"id": "1", "label": "Phone-macro lived-in handsome, five face-stuck beats on a roof", "why": "Aligns with intent-analysis option 1; no SKU."},
        {"id": "2", "label": "Grooming UGC demo with product insert", "why": "Contradicts the draft: no product was named."},
        {"id": "3", "label": "Studio beauty still then I2V", "why": "Implies gear the draft did not authorize."},
    ],
    "recommend": "1",
    "chosen": "1",
    "decide_by": FIRST_CALLED,
    "selected_by": FIRST_CALLED,
    "select_reason": "Promptengineer accepts the rooftop phone-macro framework and will induce creativedirector to lock WHY.",
}

HUMAN_ASKS: list[dict[str, Any]] = [
    {
        "from": "video.promptengineer",
        "question": "Duration, aspect, look, and room tone?",
        "point": "Frame / sound lock",
        "thinking": "Human confirms the container. Experts write the novel.",
        "options": [
            {
                "id": "1",
                "label": "15s 9:16 phone-macro, roof wind only",
                "why": "Matches a short vertical beauty clip; no score or VO.",
                "craft": (
                    "15-second, 9:16 vertical, ultra-photoreal live-action. Handheld phone-main close-up, "
                    "about 50–70mm equivalent with a slight tele crop. Optical shallow depth of field: only the nearest "
                    "skin plane is sharp; the far cheek, ear, and rear hair go soft. No studio. No cinematic grade. "
                    "No AI-smoothed face.\n"
                    "Roof wind, a distant truck, one swallow, fabric tick from the tank strap. No music. No VO."
                ),
            },
            {
                "id": "2",
                "label": "6s 1:1 talking-head with VO",
                "why": "Different container; the draft did not ask for speech.",
                "craft": "6-second square talking-head with voiceover. Not the draft.",
            },
            {
                "id": "3",
                "label": "30s 16:9 product UGC",
                "why": "Needs a product the draft did not name.",
                "craft": "30-second widescreen product UGC. Not the draft.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "human",
        "selected_by": "human_operator",
    },
    {
        "from": "video.director",
        "question": "Beat map and performance?",
        "point": "Coverage / performance lock",
        "thinking": "Human picks the coverage shape. The selected option carries the beat grammar.",
        "options": [
            {
                "id": "1",
                "label": "Five face-stuck beats: smash → skin rake → mouth/chin → climb → shaded-eye hold",
                "why": "Keeps identity on one plane; no speech; features may clip the frame.",
                "craft": (
                    "0–3s | opening smash. Already in an extreme close-up, 10–20cm from the face. "
                    "9:16 packed with: right eye, bridge, nose tip, mouth, a slab of right cheek and dark-blond stubble. "
                    "He is not looking at the lens at first. Gaze is a few degrees off, toward the harbor. "
                    "Lips closed, then part a millimeter. No speech. One visible breath that moves the philtrum. "
                    "Handheld drift of 1–2mm. Focus breathes on the nearest pore field.\n"
                    "3–6s | skin rake. Camera creeps closer and slides from the right eye across the bridge onto the freckled right cheek. "
                    "Very slow. No whip. Morning sun rakes the cheek; freckle scatter, pore pits, and stubble shadows become the subject. "
                    "Around 4.5s he squints against a gust, then the lid lifts again. "
                    "The eye reflects railing + pale sky + phone, not a circle of studio light.\n"
                    "6–10s | mouth and chin. Lens drops. Frame becomes: nose tip + philtrum + both lips + chin + a corner of the jaw. "
                    "The eyes are gone. Features may clip the frame. Do not recenter a full face. "
                    "Show the tight T-zone, dry-to-damp lip texture, mixed-length stubble on the chin, "
                    "and the firmer chin skin between hairs. "
                    "Around 7s a thin rooftop gust lifts dry ends at the temple and cheek only; they stay off the lips. "
                    "Mouth stays nearly closed. He does not hook hair with his lip. He does not chew or eat hair. "
                    "Around 9s a small swallow. The chain at the neck ticks if it is in frame.\n"
                    "10–13s | climb to the shaded eye. Camera crawls back up the left side of the face, into the open shade. "
                    "Head turns toward the lens about 6–10°, then stops short of a pose. "
                    "Gaze finally meets the camera, holds, then flicks away once to the sun and back. "
                    "Light flips as he turns: the hot right cheek loses sun, the left eye picks up a thin rim. The brow scar catches a brief highlight. "
                    "A few dry ends blow through the top of the frame, never down into the mouth.\n"
                    "13–15s | shaded-eye hold. End on the left eye and the nearby bridge, now half in shade. "
                    "One eye is the center. Grey-green iris. Pupil holds a sharp reflection of sky and railing. "
                    "A damp strand at the hairline ticks in the wind above the eye, never into the mouth. "
                    "He blinks once, slower than a posed blink. "
                    "Almost no expression change — only the mouth softens half a millimeter. Hold about one second. End."
                ),
            },
            {
                "id": "2",
                "label": "Three I2V clips 6/4/5 from a locked still",
                "why": "Packing strategy, not coverage intent.",
                "craft": "Three I2V clips from a locked still. Not the face-stuck thesis.",
            },
            {
                "id": "3",
                "label": "Wide-to-close hero plus product insert",
                "why": "Needs a product the brief never named.",
                "craft": "Wide-to-close hero with product insert. Not the draft.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "human",
        "selected_by": "human_operator",
    },
    {
        "from": "video.cinematographer",
        "question": "Light, working distance, and eye catch?",
        "point": "Light / lens lock",
        "thinking": "Human confirms the key. DoP already proposed raking morning sun vs ring light.",
        "options": [
            {
                "id": "1",
                "label": "Hard 7:20am sun camera-right slightly behind, 10–20cm, sky/railing catch in the eye",
                "why": "Cold raking key so pores and stubble read; no ring-light.",
                "craft": (
                    "Early morning, about 7:20am. Hard, cold sunlight from camera-right and slightly behind, "
                    "the kind you get on a concrete roof before the day warms up. "
                    "Clear split of light and shade down the face. The right cheek and the side of the nose are hot; the left eye sits in open shade. "
                    "Specular hits on the damp hairline, the irregular bump on the nose, a wet point on the lower lip, and one lash line. "
                    "Tiny blowout allowed only on the nose ridge and a single wet hair crossing the cheek. "
                    "Wind keeps moving hair across the sun, so the shadows on the face — and the micro-shadows inside the stubble — tick and change. "
                    "No softbox. No even beauty light. No warm golden-hour filter. No ring-light catchlight.\n"
                    "Real reflections in the eye: pale sky, a metal railing, the dark rectangle of a phone. No ring-light catchlight."
                ),
            },
            {
                "id": "2",
                "label": "Overcast even fill",
                "why": "Safer exposure, weaker pore contrast.",
                "craft": "Overcast even fill. Weaker for the anti-influencer thesis.",
            },
            {
                "id": "3",
                "label": "Beauty ring + large softbox",
                "why": "Influencer catchlight; critic will reject.",
                "craft": "Beauty ring and large softbox. Rejected for this thesis.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "human",
        "selected_by": "human_operator",
    },
    {
        "from": "video.mua_makeup",
        "question": "Makeup lock?",
        "point": "Makeup lock",
        "thinking": "No makeup. Pore manifesto is continuity, not MUA.",
        "options": [
            {
                "id": "1",
                "label": "No makeup; muted rose mouth; grey-green iris; raw brows; no liner",
                "why": "Supports hard-sun pores; face stays a lock, not a filter.",
                "craft": (
                    "No makeup. Mouth is a natural muted rose, a little dry and chapped at the inner edge, "
                    "with a faint sheen only where saliva sits. Brows are raw dark brown; you can see the grain "
                    "and a few hairs that grow the wrong way across the scar. Eyes are grey-green with a brown ring around the pupil. "
                    "Wet surface. Natural lashes, darker than the hair. No liner. "
                    "A little sleep-swelling still left on the upper lid."
                ),
            },
            {
                "id": "2",
                "label": "Grooming base and brow gel",
                "why": "Reads as influencer template.",
                "craft": "Grooming base and brow gel. Not the draft.",
            },
            {
                "id": "3",
                "label": "Styled beard oil",
                "why": "Fights overnight stubble.",
                "craft": "Styled beard oil. Rejected.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "human",
        "selected_by": "human_operator",
    },
    {
        "from": "video.continuity",
        "question": "Identity freeze — named marks?",
        "point": "Identity freeze",
        "thinking": "Human names the marks. Continuity freezes them. Do not paste sample/.",
        "options": [
            {
                "id": "1",
                "label": "Unmarked adult freeze only",
                "why": "If no moles or scars are named.",
                "craft": "Adult European man, late twenties. No named marks.",
            },
            {
                "id": "2",
                "label": "Named marks: left-brow scar, right-neck mole, overnight stubble, grey-green iris, tank + chain",
                "why": "Keeps the same man across beats.",
                "craft": (
                    "Clearly adult European man, late twenties. Handsome in a lived-in way: long-ish oval, high cheekbones that are not razor-cut, "
                    "a straight nose with a small irregular bump on the bridge, a firm jaw that still has a little morning softness under it. "
                    "Brow bone a bit heavy. Mouth slightly full for a man. Real proportions, a little asymmetrical — the left eye sits a hair lower. "
                    "Short, uneven dark-blond stubble on the upper lip, jaw, and chin; not a styled beard, just overnight growth with mixed lengths and a few bare patches. "
                    "A tiny pale scar cuts the left eyebrow. A flat brown mole sits on the right side of the neck just under the jaw, only visible if the frame drops.\n"
                    "Hair is medium-brown with dull gold in the sun, slightly wavy, still damp at the roots as if he washed it an hour ago and let it air-dry on a roof. "
                    "Medium length, falling forward off a rough side part. Damp pieces cling to the temple and the side of the neck. "
                    "Dry ends lift in a thin rooftop wind at the temple and nape only. Hair never crosses the mouth or enters the lips. "
                    "Every strand must read as real: mixed thickness, a few bent hairs, baby hairs at the hairline, salt-damp tips that catch the sun.\n"
                    "Skin is the point. Do not generate poreless AI skin or a tanned Instagram-European face. "
                    "On the cheeks, nostrils, and bridge you must clearly see: real pores, denser and slightly larger on the nose and inner cheek; "
                    "fine texture and a slight orange-peel on the chin between stubble; a scatter of light freckles across the bridge and the upper cheeks, denser on the right; "
                    "tiny pigment dots; one broken capillary near the inner right eye; mild wind-redness on the ears and around the nostrils; "
                    "under-eye thin skin with a cool violet undertone, not a stamped dark circle; T-zone still a bit tight from the wash, with a small fresh oil point only on the nose tip; "
                    "cheekbone highlight as real specular skin, with pore pits right beside it; fine blond vellus hair in front of the ear; "
                    "stubble that casts tiny hard shadows when the sun rakes sideways; a faint pillow crease still dying out on the left cheek; "
                    "fair-to-light adult male skin, a little weather on it, not spa-perfect.\n"
                    "If the frame drops, a faded black cotton tank and a thin silver chain."
                ),
            },
            {
                "id": "3",
                "label": "Allow identity drift across beats",
                "why": "Breaks the thesis; AIQA would fail.",
                "craft": "Identity drift. Rejected.",
            },
        ],
        "recommend": "2",
        "chosen": "2",
        "decide_by": "human",
        "selected_by": "human_operator",
    },
]

CYCLE_GATE: dict[str, Any] = {
    "from": "host_service",
    "question": "After this clip, run another Auto Pilot cycle?",
    "point": "pass_03 host gate",
    "thinking": "Host-owned loop. Folder max_refinement_count stays 0. Do not auto-call Imagine.",
    "options": [
        {"id": "1", "label": "stop", "why": "Keep this clip. No further critic or continuity ASK.", "craft": "stop"},
        {
            "id": "2",
            "label": "another Auto Pilot cycle",
            "why": "Critic and continuity review the clip; host re-assembles; click Grok Imagine again.",
            "craft": "continue",
        },
    ],
    "recommend": "1",
    "chosen": "1",
    "decide_by": "human",
    "selected_by": "human_operator",
}

CYCLE_ASKS: list[dict[str, Any]] = [
    {
        "from": "video.critic",
        "question": "After the clip, keep Negatives as-is or tighten?",
        "point": "pass_03-cycle critic",
        "thinking": "Host-owned pass_03. Do not write the generator novel.",
        "options": [
            {"id": "p3-1", "label": "keep Negatives", "why": "Clip matches the lock.", "craft": ""},
            {
                "id": "p3-2",
                "label": "tighten Negatives",
                "why": "Add no morph and no styled beard after seeing the clip.",
                "craft": "After the clip: no identity morph, no styled beard, no ring-light catchlight, no hair in the mouth.",
            },
        ],
        "recommend": "p3-1",
        "chosen": "p3-1",
        "decide_by": "human",
        "selected_by": "human_operator",
    },
    {
        "from": "video.continuity",
        "question": "After the clip, hold the identity freeze?",
        "point": "pass_03-cycle continuity",
        "thinking": "Host-owned pass_03. Scar, mole, stubble must not drift.",
        "options": [
            {"id": "p3-1", "label": "hold freeze", "why": "Clip already matches the named marks.", "craft": ""},
            {
                "id": "p3-2",
                "label": "restate freeze",
                "why": "Re-assert brow scar, neck mole, and tank chain for pass_03.",
                "craft": (
                    "Pass_03 freeze: tiny pale scar on the left eyebrow; flat brown mole on the right neck under the jaw; "
                    "overnight dark-blond stubble; faded black cotton tank and a thin silver chain if the frame drops."
                ),
            },
        ],
        "recommend": "p3-1",
        "chosen": "p3-1",
        "decide_by": "human",
        "selected_by": "human_operator",
    },
]


def _ask_for(agent_id: str, option_id: str | None = None) -> dict[str, Any] | None:
    chosen = str(option_id or "")
    if chosen:
        for row in list(CYCLE_ASKS) + [CYCLE_GATE] + list(HUMAN_ASKS):
            if row["from"] == agent_id and any(str(opt.get("id")) == chosen for opt in row["options"]):
                return row
    for row in HUMAN_ASKS:
        if row["from"] == agent_id:
            return row
    return None


def human_lock_choice_text(agent_id: str, option_id: str) -> str:
    ask = _ask_for(agent_id, option_id)
    if not ask:
        return ""
    overlay = dict(ask)
    overlay["chosen"] = option_id
    return _choice_block(overlay)


def _cycle_craft(agent_id: str, cycle_locks: dict[str, str] | None = None) -> str:
    if not cycle_locks or agent_id not in cycle_locks:
        return ""
    ask = _ask_for(agent_id, cycle_locks[agent_id])
    if not ask:
        return ""
    opt = next((row for row in ask["options"] if str(row.get("id")) == str(cycle_locks[agent_id])), None)
    return str((opt or {}).get("craft") or "").strip()


def _chosen_craft(agent_id: str, locks: dict[str, str] | None = None) -> str:
    ask = _ask_for(agent_id)
    if ask:
        chosen_id = str((locks or {}).get(agent_id) or ask["chosen"])
        opt = next((row for row in ask["options"] if str(row.get("id")) == chosen_id), None)
        if opt is None:
            opt = _chosen_option(ask)
        return str(opt.get("craft") or opt.get("label") or "")
    dec = next((row for row in DECISIONS if row["agent_id"] == agent_id), None)
    if not dec:
        return ""
    overlay = dict(dec)
    if locks and agent_id in locks:
        overlay["chosen"] = locks[agent_id]
    opt = _chosen_option(overlay)
    return str(opt.get("craft") or opt.get("label") or "")


def _append_human_lock(items: list[dict[str, Any]], seq: int, agent_id: str) -> int:
    ask = _ask_for(agent_id)
    if not ask:
        return seq
    seq += 1
    items.append(
        _stamp(
            seq,
            node_id="human-ask",
            **{"from": agent_id, "to": "human_operator", "kind": "human_ask", "text": _ask_block(ask)},
        )
    )
    seq += 1
    items.append(
        _stamp(
            seq,
            node_id="human-ask",
            **{"from": "human_operator", "to": agent_id, "kind": "choice", "text": _choice_block(ask)},
        )
    )
    return seq


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
                "to": INTENT_AGENT,
                "kind": "instruction",
                "text": (
                    "Auto Pilot preamble (not human detail): interpret the draft. "
                    "Return locution, illocution, triggerability, OPTIONS, RECOMMEND, DECIDE_BY. "
                    "Do not write shot grammar."
                ),
            },
        )
    )
    seq += 1
    items.append(
        _stamp(
            seq,
            node_id=INTENT_DECISION["node_id"],
            **{"from": INTENT_AGENT, "to": "create-project", "kind": "return", "text": _option_block(INTENT_DECISION)},
        )
    )
    seq += 1
    items.append(
        _stamp(
            seq,
            node_id=INTENT_DECISION["node_id"],
            **{"from": CREATIVE_AGENT, "to": INTENT_AGENT, "kind": "choice", "text": _choice_block(INTENT_DECISION)},
        )
    )
    seq += 1
    items.append(
        _stamp(
            seq,
            node_id=INTENT_DECISION["node_id"],
            **{
                "from": INTENT_AGENT,
                "to": CREATIVE_AGENT,
                "kind": "induce",
                "text": (
                    f"induce_call: {CREATIVE_AGENT} because campaign concept. "
                    "Propose OPTIONS for an execution framework. Do not write the generator novel."
                ),
            },
        )
    )
    seq += 1
    items.append(
        _stamp(
            seq,
            node_id=CREATIVE_DECISION["node_id"],
            **{"from": CREATIVE_AGENT, "to": FIRST_CALLED, "kind": "return", "text": _option_block(CREATIVE_DECISION)},
        )
    )
    seq += 1
    items.append(
        _stamp(
            seq,
            node_id=CREATIVE_DECISION["node_id"],
            **{"from": FIRST_CALLED, "to": CREATIVE_AGENT, "kind": "choice", "text": _choice_block(CREATIVE_DECISION)},
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
                    "Human brief stays high-level. Intent-analysis and creative-agent already ran. "
                    "Emit THINKING, OPTIONS, RECOMMEND, DECIDE_BY, induce_call."
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
            **{"from": CREATIVE_AGENT, "to": FIRST_CALLED, "kind": "choice", "text": _choice_block(pe)},
        )
    )
    seq = _append_human_lock(items, seq, FIRST_CALLED)
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
        seq = _append_human_lock(items, seq, dec["agent_id"])
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
                    "next_instruction pass_02 parent_pass_id=pass_01. Auto Pilot aligned. "
                    "Compile the generator instruction from SELECTED options and the five human locks. "
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
                "from": "host_service",
                "to": "output-prompt",
                "kind": "assembled",
                "text": (
                    "Host-joined generator instruction. First-called did not write the novel. "
                    "sample/ was not copied."
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


def expected_autopilot_hops() -> list[tuple[str, str, str]]:
    return [(str(item["from"]), str(item["to"]), str(item["kind"])) for item in comms_items()]


def assembled_output(
    locks: dict[str, str] | None = None,
    cycle_locks: dict[str, str] | None = None,
) -> str:
    picked = {dec["agent_id"]: _chosen_option(dec) for dec in DECISIONS}
    thesis = picked["video.creativedirector"]["label"]
    pe_craft = _chosen_craft("video.promptengineer", locks)
    frame, _, sound = pe_craft.partition("\n")
    if not sound.strip():
        frame, sound = pe_craft, pe_craft
    cont = split_continuity_craft(_chosen_craft("video.continuity", locks))
    makeup = _chosen_craft("video.mua_makeup", locks)
    light = _chosen_craft("video.cinematographer", locks)
    beats = _chosen_craft("video.director", locks)
    motor = _chosen_craft("video.cameraoperator", locks)
    negatives = _chosen_craft("video.critic", locks)
    extra_neg = _cycle_craft("video.critic", cycle_locks)
    extra_cont = _cycle_craft("video.continuity", cycle_locks)
    if extra_neg:
        negatives = "\n".join(part for part in (negatives, extra_neg) if part)
    if extra_cont:
        cont["Subject"] = "\n".join(part for part in (cont["Subject"], extra_cont) if part)
    return "\n".join(
        [
            "Generate from the locked decisions below. Host-assembled from Chat selections and ASK_HUMAN locks. sample/ is not a source.",
            "",
            "Creative direction",
            thesis + ".",
            "WHY: Auto Pilot — intent-analysis read a person, not a product; creative-agent set the rooftop phone-macro framework.",
            "",
            "Frame",
            frame.strip(),
            "",
            "Subject",
            cont["Subject"],
            "",
            "Hair",
            cont["Hair"],
            "",
            "Makeup",
            makeup,
            "",
            "Skin",
            cont["Skin"],
            "",
            "Light",
            light,
            "",
            "Coverage / performance",
            beats,
            "",
            "Camera lock",
            motor,
            "",
            "Sound, if the model supports native audio",
            sound.strip() or frame.strip(),
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
            "position": {"x": 40, "y": 160},
            "deletable": False,
            "data": {
                "kind": "start",
                "label": "Create Project",
                "title": "European Handsome",
                "brief": HUMAN_BRIEF,
                "audience": "18-34 on social",
                "duration": "15s",
                "outlets": "social",
                "risk": "low",
                "agent_id": None,
                "io": {"inputs": [], "outputs": [INTENT_AGENT]},
            },
        },
        {
            "id": INTENT_DECISION["node_id"],
            "type": "agent",
            "position": {"x": 380, "y": 40},
            "data": {
                "kind": "agent",
                "label": "intent-analysis-agent",
                "agent_id": INTENT_AGENT,
                "reason": INTENT_DECISION["point"],
                "thinking": INTENT_DECISION["thinking"],
                "options": INTENT_DECISION["options"],
                "recommend": INTENT_DECISION["recommend"],
                "decide_by": INTENT_DECISION["decide_by"],
                "chosen": INTENT_DECISION["chosen"],
                "selected_by": INTENT_DECISION["selected_by"],
                "select_reason": INTENT_DECISION["select_reason"],
                "io": {"inputs": ["create-project"], "outputs": [CREATIVE_AGENT]},
            },
        },
        {
            "id": CREATIVE_DECISION["node_id"],
            "type": "agent",
            "position": {"x": 380, "y": 280},
            "data": {
                "kind": "agent",
                "label": "creative-agent",
                "agent_id": CREATIVE_AGENT,
                "reason": CREATIVE_DECISION["point"],
                "thinking": CREATIVE_DECISION["thinking"],
                "options": CREATIVE_DECISION["options"],
                "recommend": CREATIVE_DECISION["recommend"],
                "decide_by": CREATIVE_DECISION["decide_by"],
                "chosen": CREATIVE_DECISION["chosen"],
                "selected_by": CREATIVE_DECISION["selected_by"],
                "select_reason": CREATIVE_DECISION["select_reason"],
                "io": {"inputs": [INTENT_AGENT], "outputs": [FIRST_CALLED]},
            },
        },
        {
            "id": "agent-video-promptengineer",
            "type": "agent",
            "position": {"x": 720, "y": 160},
            "data": {
                "kind": "agent",
                "label": FIRST_CALLED,
                "agent_id": FIRST_CALLED,
                "reason": DECISIONS[0]["point"],
                "thinking": DECISIONS[0]["thinking"],
                "options": DECISIONS[0]["options"],
                "recommend": DECISIONS[0]["recommend"],
                "decide_by": DECISIONS[0]["decide_by"],
                "chosen": DECISIONS[0]["chosen"],
                "selected_by": DECISIONS[0]["selected_by"],
                "select_reason": DECISIONS[0]["select_reason"] or "Human confirmed the expert recommend.",
                "io": {"inputs": [CREATIVE_AGENT], "outputs": pe_outs},
            },
        },
    ]
    edges: list[dict[str, Any]] = [
        {
            "id": "e-create-intent",
            "source": "create-project",
            "target": INTENT_DECISION["node_id"],
            "sourceHandle": INTENT_AGENT,
            "targetHandle": "in",
            "type": "smoothstep",
            "label": INTENT_AGENT,
        },
        {
            "id": "e-intent-creative",
            "source": INTENT_DECISION["node_id"],
            "target": CREATIVE_DECISION["node_id"],
            "sourceHandle": CREATIVE_AGENT,
            "targetHandle": "in",
            "type": "smoothstep",
            "label": CREATIVE_AGENT,
        },
        {
            "id": "e-creative-promptengineer",
            "source": CREATIVE_DECISION["node_id"],
            "target": "agent-video-promptengineer",
            "sourceHandle": FIRST_CALLED,
            "targetHandle": "in",
            "type": "smoothstep",
            "label": FIRST_CALLED,
        },
    ]
    for index, dec in enumerate(DECISIONS[1:]):
        nodes.append(
            {
                "id": dec["node_id"],
                "type": "agent",
                "position": {"x": 1060, "y": 20 + index * 130},
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
                        + (["human-ask"] if dec["agent_id"] in HUMAN_DOMAIN_ROLES else []),
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
            "position": {"x": 720, "y": 480},
            "data": {
                "kind": "human",
                "label": "Human",
                "reason": "Five domain ASK_HUMAN locks — human selects options only",
                "brief": "\n".join(
                    f"Human → {row['from']}: {row['question']} (option {row['chosen']})" for row in HUMAN_ASKS
                ),
                "io": {"inputs": list(HUMAN_DOMAIN_ROLES), "outputs": ["answer"]},
            },
        }
    )
    for role in HUMAN_DOMAIN_ROLES:
        node_id = "agent-video-promptengineer" if role == FIRST_CALLED else f"agent-{role.replace('.', '-')}"
        edges.append(
            {
                "id": f"e-{role.replace('.', '-')}-human",
                "source": node_id,
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
            "position": {"x": 1480, "y": 160},
            "deletable": False,
            "data": {
                "kind": "output",
                "label": "Output",
                "reason": f"project/{SLUG}/output/{SLUG}-prompt.txt",
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
        "walkthrough": "auto-pilot-v1",
        "note": "Auto Pilot characterization. Not live Grok hops. Human draft plus five option locks. Workflow nodes copy these decisions.",
        "autopilot": {
            "status": "aligned",
            "human_roles": list(HUMAN_DOMAIN_ROLES),
            "locks_selected": len(HUMAN_DOMAIN_ROLES),
            "intent_agent": INTENT_AGENT,
            "creative_agent": CREATIVE_AGENT,
        },
        "decisions": DECISIONS,
        "locks": {row["from"]: row["chosen"] for row in HUMAN_ASKS},
        "items": comms_items(),
    }


def pack_map_suggestion(brief: dict[str, Any]) -> dict[str, Any]:
    """Template B is the pack-map SVG only. Rank it first with an honesty label, like asain-beauty."""
    from casops.projects import CATALOG_BY_ID, catalog_public, merge_suggestions, suggest_prompt

    merged = merge_suggestions(brief, "", False)
    rows = [dict(row) for row in (merged.get("suggestions") or []) if isinstance(row, dict)]
    by_id = {str(row.get("id")): row for row in rows}
    catalog_b = CATALOG_BY_ID["video.template.b"]
    pack = dict(
        by_id.get("video.template.b")
        or {
            "id": "video.template.b",
            "label": f"{catalog_b['code']} · {catalog_b['label']}",
            "kind": catalog_b["kind"],
            "reason": catalog_b["use"],
            "source": "heuristic",
        }
    )
    pack["label"] = "B · pack map (not this project's creative lock)"
    pack["reason"] = "Sub-workflow SVG template B is the pack picture only. Chat lock is no-SKU rooftop phone-macro."
    pack["rank"] = 1
    ordered = [pack]
    seen = {"video.template.b"}
    for row in rows:
        rid = str(row.get("id") or "")
        if rid in seen:
            continue
        next_row = dict(row)
        next_row["rank"] = len(ordered) + 1
        ordered.append(next_row)
        seen.add(rid)
        if len(ordered) >= 5:
            break
    merged["suggestions"] = ordered
    merged["primary"] = "video.template.b"
    merged["honesty"] = "CHARACTERIZATION"
    merged["honesty_note"] = "Pack map only — not this project's creative lock."
    merged["llm_used"] = False
    merged["adapter"] = "host_llm"
    merged["prompt"] = suggest_prompt(brief)
    merged["catalog"] = catalog_public()
    return merged


def write_european_handsome_walkthrough(root: Path) -> dict[str, Any]:
    from casops.projects import read_project, write_project

    folder = Path(root) / SLUG
    folder.mkdir(parents=True, exist_ok=True)
    if not (folder / "project.json").is_file():
        write_project(
            root,
            {
                "id": SLUG,
                "name": SLUG,
                "title": "European Handsome",
                "brief": HUMAN_BRIEF,
                "audience": "18-34 on social",
                "duration": "15s",
                "outlets": "social",
                "risk": "low",
                "sub_workflow_id": "video.template.b",
            },
            dry_run=False,
            create=True,
        )
    prior_media: list[dict[str, Any]] = []
    comms_path = folder / "comms.json"
    if comms_path.is_file():
        try:
            prior = json.loads(comms_path.read_text(encoding="utf-8"))
            prior_media = [
                item
                for item in (prior.get("items") or [])
                if isinstance(item, dict) and item.get("kind") == "generated_media"
            ]
        except (OSError, json.JSONDecodeError):
            prior_media = []
    comms = comms_payload()
    if prior_media:
        comms["items"] = list(comms["items"]) + prior_media
    (folder / "comms.json").write_text(json.dumps(comms, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    out = assembled_output()
    out_dir = folder / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{SLUG}-prompt.txt").write_text(out if out.endswith("\n") else out + "\n", encoding="utf-8")
    record = read_project(root, SLUG)
    record["brief"] = HUMAN_BRIEF
    record["title"] = "European Handsome"
    record["notes"] = (
        "sub_workflow_id is the pack-map SVG only. Chat creative lock is a rooftop phone-macro of an adult European man, not a UGC ad."
    )
    brief = {
        "name": SLUG,
        "title": "European Handsome",
        "brief": HUMAN_BRIEF,
        "audience": "18-34 on social",
        "duration": "15s",
        "outlets": "social",
        "risk": "low",
        "notes": record["notes"],
    }
    record["suggestion"] = pack_map_suggestion(brief)
    record["io_overlay"] = {
        "note": "Auto Pilot Chat edges. Pack critique_edges on video.* stay for Main/Sub SVG. Host dispatch does not count against folder max_peer_hops (agent-initiated tools only; allowlist empty).",
        "peer_hops": "host_mediated",
        "edges": {
            "specials.intent-analysis-agent": {
                "inputs": ["create-project"],
                "outputs": ["specials.general-creative-agent"],
            },
            "specials.general-creative-agent": {
                "inputs": ["specials.intent-analysis-agent"],
                "outputs": ["video.promptengineer"],
            },
            "video.promptengineer": {
                "inputs": ["specials.general-creative-agent", "create-project"],
                "outputs": [
                    "video.creativedirector",
                    "video.director",
                    "video.cinematographer",
                    "video.mua_makeup",
                    "video.cameraoperator",
                    "video.continuity",
                    "video.critic",
                ],
            },
        },
    }
    record["graph"] = graph_bundle()
    write_project(root, record, dry_run=False, create=False)
    return {"comms": comms, "graph": record["graph"], "output": out}
