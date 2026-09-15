"""Characterization walkthrough for asain-beauty: Chat decisions aligned with Workflow nodes."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from casops.project_instruction import split_continuity_craft

FIRST_CALLED = "video.promptengineer"
SLUG = "asain-beauty"
HUMAN_BRIEF = "Short vertical beauty clip. Adult East Asian woman."
ASSEMBLE_WHY = "Auto Pilot — intent-analysis read a person, not a product; creative-agent set the phone-macro framework."

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
        "decide_by": "specials.general-creative-agent",
        "selected_by": "specials.general-creative-agent",
        "select_reason": "Creative-agent confirmed the intent-analysis reading: a person-led clip, so thesis (creativedirector) precedes coverage.",
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
                "craft": (
                    "No traditional push / pull / pan / orbit. This is a macro crawl stuck to the face. "
                    "Same adult East Asian woman the whole time. Features, moles, hair color, and skin do not morph. "
                    "Stable but with real handheld breath, about 1–2mm. Features may clip the frame edge. "
                    "No jump cuts. No warped face. No melted teeth. No drifting eyes."
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
        "decide_by": FIRST_CALLED,
        "selected_by": FIRST_CALLED,
        "select_reason": "Human already froze named marks on the ASK_HUMAN lock; orchestrator confirms option 2.",
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
                "craft": (
                    "no beauty filter, no airbrushed skin, no poreless skin, no plastic CGI face, no doll skin, "
                    "no influencer template face, no studio softbox, no ring light catchlight, no fake eyelashes, "
                    "no over-symmetrical face, no cinematic color grade, no talking, no posed smile to camera, "
                    "no dolly zoom, no orbit shot, no extra fingers, no warped nose, no morphing identity."
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
        "select_reason": "Orchestrator selected option 1 so negatives document the already-chosen path. Options 2 and 3 reopen decisions that parent experts already closed.",
    },
]

INTENT_AGENT = "specials.intent-analysis-agent"
CREATIVE_AGENT = "specials.general-creative-agent"
HUMAN_DOMAIN_ROLES: tuple[str, ...] = (
    "video.promptengineer",
    "video.director",
    "video.cinematographer",
    "video.mua_makeup",
    "video.continuity",
)

INTENT_DECISION: dict[str, Any] = {
    "id": "dec-intent",
    "agent_id": INTENT_AGENT,
    "node_id": "agent-specials-intent-analysis-agent",
    "point": "What the draft is asking for",
    "thinking": (
        "Locution: a short vertical beauty clip of an adult East Asian woman. "
        "Illocution: directive to produce a clip. Triggerable as a container, not as shot grammar. "
        "No product, speech, or studio is evidenced."
    ),
    "options": [
        {"id": "1", "label": "Person-led beauty skin study (no product named)", "why": "Draft names a woman, not a SKU or CTA."},
        {"id": "2", "label": "Paid UGC product ad", "why": "Would invent a shop CTA the draft omitted."},
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
        "Intent is a person, not a product. The framework must survive a short vertical without becoming an idol-template ad. "
        "Domain experts (promptengineer, director, cinematographer, mua_makeup, continuity) lock craft via ASK_HUMAN options."
    ),
    "options": [
        {"id": "1", "label": "Phone-macro anti-idol skin study, five face-stuck beats", "why": "Aligns with intent-analysis option 1; no SKU."},
        {"id": "2", "label": "Glass-skin UGC demo with product insert", "why": "Contradicts the draft: no product was named."},
        {"id": "3", "label": "Studio beauty still then I2V", "why": "Implies gear the draft did not authorize."},
    ],
    "recommend": "1",
    "chosen": "1",
    "decide_by": FIRST_CALLED,
    "selected_by": FIRST_CALLED,
    "select_reason": "Promptengineer accepts the phone-macro framework and will induce creativedirector to lock WHY.",
}

# One ASK_HUMAN per domain role. Human selects an option; craft prose is agent-authored (not a human essay).
# Paraphrased from sample/asain-beauty-prompt.txt so the gold body probe is never pasted.
HUMAN_ASKS: list[dict[str, Any]] = [
    {
        "from": "video.promptengineer",
        "question": "Duration, aspect, look, and room tone?",
        "point": "Frame / sound lock",
        "thinking": "Human confirms the container. Experts write the novel.",
        "options": [
            {
                "id": "1",
                "label": "15s 9:16 phone-macro, room tone only",
                "why": "Matches a short vertical beauty clip; no score or VO.",
                "craft": (
                    "15-second, 9:16 vertical, 4K ultra-photoreal live-action. Handheld phone-main close-up, "
                    "roughly 50–70mm equivalent with a slight tele crop. Optical shallow depth of field: only the nearest "
                    "skin plane is sharp; the ear side and rear hair fall off. No studio setup. No cinematic grade. "
                    "No AI-smoothed face.\n"
                    "Extreme close-up room tone only: leaves outside, a very faint distant car, one swallow, breath. "
                    "No score. No VO."
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
                "label": "Five face-stuck beats: smash → eye/skin → nose/mouth → climb → one-eye hold",
                "why": "Keeps identity on one plane; no speech; features may clip the frame.",
                "craft": (
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
        "thinking": "Human confirms the key. DoP already proposed raking sun vs ring light.",
        "options": [
            {
                "id": "1",
                "label": "Hard 4pm sun through sheer, 10–20cm, real window catch in the eye",
                "why": "Raking key so pores read; no ring-light.",
                "craft": (
                    "Hard late-afternoon sun, around 4pm. Sun hits from camera-left front and slightly above, first through a "
                    "half-open window and a thin white sheer curtain, then onto the face. Clear highlight / shadow split. "
                    "Real specular hits on the bridge, nose tip, highest point of the cheekbone, upper-lip glaze, and forehead. "
                    "Tiny blowout allowed only on nose tip, upper-lip glaze, and cheekbone peak. "
                    "As she and the camera drift a few millimeters, curtain, outdoor leaves, and hair keep cutting the sun, "
                    "throwing moving stripe and dapple shadows across the face. Slight overexposure in those tiny hotspots is "
                    "part of the phone-close-up look. Camera 10–20cm from the face. No studio soft light. No perfectly even lighting. "
                    "No beauty filter, no smoothed skin, no plastic highlight. No ring-light catchlight.\n"
                    "Real reflections in pupil and iris: window grid, sheer curtain, a silhouette of the person shooting. "
                    "Hard sunlight specular on the nose tip. No ring-light catchlight."
                ),
            },
            {
                "id": "2",
                "label": "Overcast window, even fill, no sheer",
                "why": "Safer exposure, weaker pore contrast.",
                "craft": "Overcast window, even fill, no sheer. Weaker for the anti-idol thesis.",
            },
            {
                "id": "3",
                "label": "Beauty ring + large softbox",
                "why": "Idol catchlight; critic will reject.",
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
        "thinking": "Bare lock only. Pore manifesto is continuity, not MUA.",
        "options": [
            {
                "id": "1",
                "label": "Sunscreen + thin moisturizer; natural brow; dusty-rose glaze; no fake lashes",
                "why": "Supports hard-sun pores; makeup stays a lock, not a filter.",
                "craft": (
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
                "id": "2",
                "label": "Full base, contour, lash strip",
                "why": "Reads as influencer template under hard sun.",
                "craft": "Full base, contour, lash strip. Not the lock.",
            },
            {
                "id": "3",
                "label": "No product on skin at all",
                "why": "Legal, but dry flake may dominate the macro.",
                "craft": "No product on skin. Continuity texture, not makeup.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "human",
        "selected_by": "human_operator",
    },
    {
        "from": "video.continuity",
        "question": "Identity, hair, skin, and wardrobe freeze?",
        "point": "Identity freeze",
        "thinking": "One human lock for the whole 15s. Do not split into four essays.",
        "options": [
            {
                "id": "1",
                "label": "Unmarked adult freeze only",
                "why": "If the human names no moles.",
                "craft": "Unmarked adult freeze only. No named moles.",
            },
            {
                "id": "2",
                "label": "Named marks: left-eye mole, mouth-corner mole, sleep crease, 25-26 adult, black hair, pale freckles, tank strap",
                "why": "Freeze what a human would have named from the draft, not a gold paste.",
                "craft": (
                    "Clearly adult East Asian woman, about 25–26. Natural cool-toned East Asian face. Slightly long small oval, "
                    "cheekbones gently lifted but not sharp, soft jawline, a visible philtrum groove. Real facial proportions. "
                    "Not an influencer-template face. A tiny light-brown mole sits just under the outer corner of the left eye. "
                    "Another almost unnoticeable mole sits outside the left mouth corner. One cheek still holds a very faint "
                    "sleep crease that sunlight is slowly erasing. Do not morph.\n"
                    "Natural long black with a slight wave, as if she just came inside from outdoors. Wind-tousled. "
                    "One side casually tucked behind the ear, the other side fully down. Individual black strands fall across "
                    "the forehead, lashes, and cheek. A few loose strands snag on the wet mouth corner while the camera is "
                    "down on the lips. Fine vellus at the hairline, plus a little heat-lifted frizz. Every strand must read as "
                    "real: thickness variation, messy flyaways, peach fuzz near the crown, translucent tips when the sun hits them.\n"
                    "Skin is the most important thing. Do not generate a traditional AI-beauty poreless face. "
                    "On the cheeks, nostrils, and bridge you must clearly see: real pores, fine skin texture, slight uneven relief, "
                    "a few pale freckles mostly on both sides of the bridge and the cheekbones, tiny pigment dots, natural moles, "
                    "mild uneven tone, real nostril texture. Under-eyes are not a dark-circle template — thin skin with faint blue "
                    "vessels plus 2–3 shallow micro-lines. T-zone oilier than the cheeks; a small sebum highlight collected at the "
                    "alar crease / nasolabial junction, not an all-over oily face. Cheekbone highlight as actual specular skin, "
                    "with pore shadows immediately beside it. Fine facial vellus. An almost invisible dry flake beside one nostril. "
                    "Adult female skin, still clean, healthy, and clear.\n"
                    "If the frame drops to the collarbone, a thin off-white ribbed tank strap is allowed. Nothing else."
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
        {
            "id": "1",
            "label": "stop",
            "why": "Keep this clip. No further critic or continuity ASK.",
            "craft": "stop",
        },
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
            {
                "id": "p3-1",
                "label": "keep Negatives",
                "why": "Clip matches the lock.",
                "craft": "",
            },
            {
                "id": "p3-2",
                "label": "tighten Negatives",
                "why": "Add no morph and no extra jewelry after seeing the clip.",
                "craft": "After the clip: no identity morph, no extra jewelry, no ring-light catchlight.",
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
        "thinking": "Host-owned pass_03. Mole, hair, strap must not drift.",
        "options": [
            {
                "id": "p3-1",
                "label": "hold freeze",
                "why": "Clip already matches the named marks.",
                "craft": "",
            },
            {
                "id": "p3-2",
                "label": "restate freeze",
                "why": "Re-assert mole, hair part, and tank strap for pass_03.",
                "craft": (
                    "Pass_03 freeze: tiny light-brown mole sits just under the outer corner of the left eye; "
                    "natural long black with a slight wave; thin off-white ribbed tank strap if the frame drops."
                ),
            },
        ],
        "recommend": "p3-1",
        "chosen": "p3-1",
        "decide_by": "human",
        "selected_by": "human_operator",
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


def _ask_block(ask: dict[str, Any]) -> str:
    lines = [
        f"ASK_HUMAN: {ask['question']}",
        f"THINKING: {ask['thinking']}",
        f"Decision point: {ask['point']}",
    ]
    for opt in ask["options"]:
        rec = " (recommend)" if opt["id"] == ask["recommend"] else ""
        lines.append(f"OPTION {opt['id']}: {opt['label']} — {opt['why']}{rec}")
    lines.append(f"RECOMMEND: {ask['recommend']}")
    lines.append("DECIDE_BY: human")
    return "\n".join(lines)


def _chosen_option(block: dict[str, Any]) -> dict[str, Any]:
    return next((opt for opt in block["options"] if opt["id"] == block["chosen"]), block["options"][0])


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
    """Characterization hop table: (from, to, kind) in Chat time order."""
    return [(str(item["from"]), str(item["to"]), str(item["kind"])) for item in comms_items()]


def assembled_output(
    locks: dict[str, str] | None = None,
    cycle_locks: dict[str, str] | None = None,
) -> str:
    """Host-join SELECTED options + ASK_HUMAN crafts. Never paste sample/."""
    from casops.video_prompt.assemble import clip_from_walkthrough, project_clip

    return project_clip(clip_from_walkthrough(__import__("sys").modules[__name__], locks, cycle_locks))


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
                "title": "Asain Beauty",
                "brief": HUMAN_BRIEF,
                "audience": "18-34 beauty shoppers on social",
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


def write_asain_beauty_walkthrough(root: Path) -> dict[str, Any]:
    from casops.projects import read_project, write_project

    folder = Path(root) / SLUG
    folder.mkdir(parents=True, exist_ok=True)
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
    from casops.video_prompt.assemble import clip_from_walkthrough, write_clip_files

    clip = clip_from_walkthrough(__import__("sys").modules[__name__])
    out_dir = folder / "output"
    out = write_clip_files(out_dir, SLUG, clip)
    record = read_project(root, SLUG)
    record["brief"] = HUMAN_BRIEF
    record["notes"] = (
        "sub_workflow_id is the pack-map SVG only. Chat creative lock is a phone-macro skin study, not a UGC ad."
    )
    suggestion = dict(record.get("suggestion") or {})
    suggestion["honesty_note"] = "Pack map only — not this project's creative lock."
    rows = list(suggestion.get("suggestions") or [])
    for row in rows:
        if isinstance(row, dict) and row.get("id") == "video.template.b":
            row["label"] = "B · pack map (not this project's creative lock)"
            row["reason"] = "Sub-workflow SVG template B is the pack picture only. Chat lock is no-SKU phone-macro."
    suggestion["suggestions"] = rows
    record["suggestion"] = suggestion
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
