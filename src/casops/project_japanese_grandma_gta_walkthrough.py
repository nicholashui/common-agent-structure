"""Characterization walkthrough for japanese-grandma-gta: Chat decisions aligned with Workflow nodes."""

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

SLUG = "japanese-grandma-gta"
HUMAN_BRIEF = "Short 16:9 chase clip. Adult Japanese grandma on a senior scooter."
GOLD_BODY_PROBE = "RETURN THE PICKLES BEFORE DINNER"

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
        "thinking": "The draft names an adult Japanese grandma on a scooter, not a SKU. Thesis must survive 15s as a rural-Japan gameplay chase, not Miami vice or a beauty spot.",
        "options": [
            {
                "id": "1",
                "label": "Rural-Japan third-person chase: grandma on a senior scooter, invented HUD, anti-Miami",
                "why": "Matches 'adult grandma' + chase without inventing a shop CTA or copying Rockstar assets.",
            },
            {
                "id": "2",
                "label": "Grooming UGC demo with product and CTA",
                "why": "Fits template heuristics; the human did not name a product.",
            },
            {
                "id": "3",
                "label": "Vice City neon homage then I2V",
                "why": "Fights the rural-Japan lock the draft implied.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "video.promptengineer",
        "selected_by": "video.promptengineer",
        "select_reason": "Parent orchestrator picked option 1 because the brief is a grandma chase in the countryside, not a product. Option 2 invents a CTA. Option 3 implies Miami nobody authorized.",
    },
    {
        "id": "dec-03",
        "agent_id": "video.director",
        "node_id": "agent-video-director",
        "point": "Coverage / beat map",
        "thinking": "Thesis is a 15s already-in-motion chase. Coverage should stay on grandma + scooter as the player vehicle, not a portrait pullback.",
        "options": [
            {
                "id": "1",
                "label": "Five chase beats: farm-road smash, paddy cut, village drift, drainage hop, levee escape",
                "why": "Keeps identity on the scooter; slapstick only; HUD stays on.",
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
        "select_reason": "Creative director selected option 1 so the countryside chase is one continuous gameplay take. Option 2 is packing, not coverage. Option 3 contradicts the no-product thesis.",
    },
    {
        "id": "dec-04",
        "agent_id": "video.cinematographer",
        "node_id": "agent-video-cinematographer",
        "point": "Light / lens",
        "thinking": "Gameplay cam needs late-afternoon countryside sun so paddies, dust, and the scooter chrome read. Neon Miami would flatten the thesis.",
        "options": [
            {
                "id": "1",
                "label": "Sunny late-afternoon rural Japan, third-person chase key, dust and paddy glare",
                "why": "Warm split on farm roads and mountains; no Vice City neon.",
            },
            {
                "id": "2",
                "label": "Overcast even fill",
                "why": "Safer exposure, weaker dust and water spray.",
            },
            {
                "id": "3",
                "label": "Night neon Miami key",
                "why": "Contradicts the countryside lock; critic will reject.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "video.director",
        "selected_by": "video.director",
        "select_reason": "Director selected option 1 because the beats stay on a farm-road chase; Miami neon would fight every countryside beat.",
    },
    {
        "id": "dec-05",
        "agent_id": "video.mua_makeup",
        "node_id": "agent-video-mua_makeup",
        "point": "Makeup lock",
        "thinking": "No makeup. Age is continuity, not MUA. Do not de-age.",
        "options": [
            {
                "id": "1",
                "label": "No makeup; un-beautified 75–82 face; age spots; no liner or lashes",
                "why": "Supports lived-in grandma identity; face stays a lock, not a filter.",
            },
            {
                "id": "2",
                "label": "Soft-focus beauty base and brow gel",
                "why": "Reads as de-aged influencer grandma.",
            },
            {
                "id": "3",
                "label": "Contour and false lashes",
                "why": "Contradicts the age freeze.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "video.creativedirector",
        "selected_by": "video.creativedirector",
        "select_reason": "Creative director selected option 1: no product on skin. Option 2 becomes a de-aged template. Option 3 fights the 75–82 lock.",
    },
    {
        "id": "dec-06",
        "agent_id": "video.cameraoperator",
        "node_id": "agent-video-cameraoperator",
        "point": "Camera motor",
        "thinking": "One motor. Director beats are a chase; a beauty orbit would steal the gameplay cam.",
        "options": [
            {
                "id": "1",
                "label": "Third-person chase cam ~3m behind and slightly above. Brief wheel-level and drone peeks only",
                "why": "Matches GTA-like driving camera; grandma + scooter stay readable lower-center.",
                "craft": (
                    "Persistent third-person chase camera about 3 meters behind and slightly above the scooter. "
                    "Same adult Japanese grandma and the same silver four-wheel senior scooter the whole time. "
                    "Occasional low wheel-level cut and one brief high drone peek, then back to gameplay cam. "
                    "Subtle handheld game-cam. No beauty orbit. No extra wheels. No melted face."
                ),
            },
            {
                "id": "2",
                "label": "Locked hood-mount on the tiller",
                "why": "Loses the GTA chase read.",
            },
            {
                "id": "3",
                "label": "Gentle orbit around the head",
                "why": "Breaks the chase motor and recenters as a portrait.",
            },
        ],
        "recommend": "1",
        "chosen": "1",
        "decide_by": "video.cinematographer",
        "selected_by": "video.cinematographer",
        "select_reason": "Cinematographer selected option 1 so the motor stays a gameplay chase cam. Option 3 is rejected: orbit was never granted.",
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
                "why": "If the human names no vehicle or wardrobe.",
            },
            {
                "id": "2",
                "label": "Freeze named lock: 75–82 grandma, silver perm, floral blouse, silver four-wheel scooter",
                "why": "Matches the countryside rider the draft implied.",
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
        "thinking": "Check chosen locks against Rockstar replica UI, Miami, de-aged grandma, motorcycle swap, gore.",
        "options": [
            {
                "id": "1",
                "label": "Pass with Avoid: no official GTA UI, no Miami, no young grandma, no extra wheels, no gore",
                "why": "Chosen path already avoids those; write them as Avoid.",
                "craft": (
                    "no official Rockstar or GTA replica UI, no copied logos, cars, fonts, or characters, "
                    "no Miami neon, no palm-lined vice strip, no art-deco hotels, "
                    "no young pretty grandma, no de-aging, no motorcycle swap, "
                    "no melted face, no extra limbs, no extra wheels, no disappearing basket, "
                    "no explosions, no guns, no gore, no realistic grievous harm, "
                    "not documentary footage, not a how-to."
                ),
            },
            {
                "id": "2",
                "label": "Blocker: send back for Miami neon",
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
        "Locution: a short 16:9 chase clip of an adult Japanese grandma on a senior scooter. "
        "Illocution: directive to produce a clip. Triggerable as a container, not as shot grammar. "
        "No product SKU is evidenced. Gameplay parody is implied, not a shop CTA."
    ),
    "options": [
        {"id": "1", "label": "Person-led countryside chase (no product named)", "why": "Draft names a grandma and a scooter, not a SKU or CTA."},
        {"id": "2", "label": "Paid grooming UGC ad", "why": "Would invent a shop CTA the draft omitted."},
        {"id": "3", "label": "Talking-head explainer", "why": "Draft did not ask for speech."},
    ],
    "recommend": "1",
    "chosen": "1",
    "decide_by": CREATIVE_AGENT,
    "selected_by": CREATIVE_AGENT,
    "select_reason": "Creative-agent takes the person-led chase reading; a UGC ad or explainer would exceed the draft.",
}

CREATIVE_DECISION: dict[str, Any] = {
    "id": "dec-creative",
    "agent_id": CREATIVE_AGENT,
    "node_id": "agent-specials-general-creative-agent",
    "point": "Campaign concept / execution framework",
    "thinking": (
        "Intent is a person on a scooter, not a product. The framework must survive 15s as rural-Japan gameplay without becoming Miami vice or a UGC ad. "
        "Domain experts lock craft via ASK_HUMAN options."
    ),
    "options": [
        {"id": "1", "label": "Rural-Japan third-person chase, five scooter beats, invented HUD", "why": "Aligns with intent-analysis option 1; no SKU."},
        {"id": "2", "label": "Grooming UGC demo with product insert", "why": "Contradicts the draft: no product was named."},
        {"id": "3", "label": "Studio beauty still then I2V", "why": "Implies gear the draft did not authorize."},
    ],
    "recommend": "1",
    "chosen": "1",
    "decide_by": FIRST_CALLED,
    "selected_by": FIRST_CALLED,
    "select_reason": "Promptengineer accepts the countryside chase framework and will induce creativedirector to lock WHY.",
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
                "label": "15s 16:9 gameplay capture, invented HUD, village ambience",
                "why": "Matches a short chase clip; no licensed score or VO.",
                "craft": (
                    "15-second, 16:9, photoreal next-gen AAA gameplay capture inspired by modern open-world crime games. "
                    "Rural Japan, not Miami. Invented HUD only, visible the whole time: circular mini-map bottom-left "
                    "with farm roads and a yellow destination blip; health and armor bars; wanted stars starting at 1 "
                    "and rising to 2–3; a cash counter; tiny mission line that reads get the pickles home before supper. "
                    "No watermark, no real brand marks, no burned-in subtitles. "
                    "No official Rockstar logos, cars, fonts, or characters. "
                    "Parody billing may read as a senior-scooter heist, not a licensed title.\n"
                    "Diegetic: high-pitched scooter motor, rattling basket, chickens, kei-truck horn, delayed siren, "
                    "Japanese village ambience, a short muffled police yell. No licensed music. No narrator."
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
                "label": "30s 9:16 beauty UGC",
                "why": "Wrong aspect and genre for a chase clip.",
                "craft": "30-second vertical beauty UGC. Not the draft.",
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
                "label": "Five chase beats: farm smash → paddy cut → village drift → drainage hop → levee hold",
                "why": "Keeps identity on the scooter; start mid-action; slapstick only.",
                "craft": (
                    "0–3s | farm-road smash. Already speeding down a narrow farm road on the scooter. "
                    "Basket rattling. Cardigan flapping. Chickens scatter. Invented HUD is on. A distant siren. "
                    "She does not look at the lens. Calm, slightly mischievous stone face. No speech.\n"
                    "3–6.5s | paddy cut. She cuts a corner onto a rice-paddy path, kicking up water and mud, "
                    "overtaking a slow kei truck. A white-and-black Japanese patrol car appears behind, lights flashing, arriving late.\n"
                    "6.5–10s | village drift. Chase on the village main street past vending machines and a konbini. "
                    "She drifts the scooter around a mailbox. Wanted stars tick up. Officers shout in Japanese in the distance. She is not scared.\n"
                    "10–13s | drainage hop. She bumps a low irrigation lip; the scooter lands heavy but stays upright. "
                    "A second patrol car slides and misses. Slapstick only: no blood, no crash that reads as real injury.\n"
                    "13–15s | levee escape. Camera lifts slightly behind her as she pulls onto an empty levee road in late sun, "
                    "scooter still screaming forward, jars of pickles still in the basket. Freeze on a readable gameplay pose: "
                    "grandma, scooter, HUD, paddies stretching ahead. End."
                ),
            },
            {
                "id": "2",
                "label": "Three I2V clips 6/4/5 from a locked still",
                "why": "Packing strategy, not coverage intent.",
                "craft": "Three I2V clips from a locked still. Not the chase thesis.",
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
        "thinking": "Human confirms the key. DoP already proposed late-afternoon countryside vs Miami neon.",
        "options": [
            {
                "id": "1",
                "label": "Sunny late-afternoon rural Japan, dust and paddy glare, mountains in the back",
                "why": "Warm countryside key so chrome, water spray, and tiled roofs read; no Vice City.",
                "craft": (
                    "Sunny late afternoon in the Japanese countryside. Narrow farm roads, rice paddies, irrigation ditches, "
                    "utility poles, vending machines, tiled-roof houses, a convenience store, a small shrine gate, "
                    "aging kei trucks, bicycles, scarecrows. Dust on asphalt. Green mountains in the distance. "
                    "No neon Vice City, no palm trees, no art-deco hotels.\n"
                    "Specular on the scooter chrome and wet paddy water. Motion blur on the background only. "
                    "Ray-traced puddles if a wet patch exists. No studio softbox. No ring-light catchlight."
                ),
            },
            {
                "id": "2",
                "label": "Overcast even fill",
                "why": "Safer exposure, weaker dust and spray.",
                "craft": "Overcast even fill. Weaker for the countryside chase thesis.",
            },
            {
                "id": "3",
                "label": "Night neon Miami key",
                "why": "Contradicts the rural-Japan lock; critic will reject.",
                "craft": "Night neon Miami key. Rejected for this thesis.",
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
        "thinking": "No makeup. Age freeze is continuity, not MUA.",
        "options": [
            {
                "id": "1",
                "label": "No makeup; un-beautified 75–82 face; age spots; no liner",
                "why": "Supports the lived-in grandma lock; face stays a lock, not a filter.",
                "craft": (
                    "No makeup. Do not de-age. Mouth is a natural muted rose, a little dry. "
                    "Brows are sparse silver-grey with a few darker hairs. Eyes are dark brown, slightly watery in the wind. "
                    "Natural lashes, no liner, no false lashes, no contour."
                ),
            },
            {
                "id": "2",
                "label": "Soft-focus beauty base",
                "why": "Reads as de-aged influencer grandma.",
                "craft": "Soft-focus beauty base. Not the draft.",
            },
            {
                "id": "3",
                "label": "Contour and false lashes",
                "why": "Fights the age freeze.",
                "craft": "Contour and false lashes. Rejected.",
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
                "why": "If no vehicle or wardrobe is named.",
                "craft": "Adult Japanese woman. No named vehicle.",
            },
            {
                "id": "2",
                "label": "Named lock: 75–82 grandma, silver perm, floral blouse, silver four-wheel scooter + basket",
                "why": "Keeps the same rider and vehicle across beats.",
                "craft": (
                    "Clearly adult Japanese grandma, about 75–82. Short round face, deep wrinkles, age spots, not beautified. "
                    "Calm, slightly mischievous stone face. She never becomes young. No extra limbs. "
                    "Floral blouse, beige cardigan, dark cropped trousers, white socks, plastic sandals or walking shoes, "
                    "a small cloth shopping bag in the front basket.\n"
                    "Hair is short permed silver, not dyed, not flowing anime hair. Tight curls sit close to the scalp. "
                    "A few flyaways at the nape lift in the scooter wind.\n"
                    "Skin is the age lock. Do not generate poreless AI skin or a de-aged idol grandma. "
                    "You must clearly see: deep nasolabial folds; crow's feet; age spots on the cheeks and hands; "
                    "thin under-eye skin; weather on the neck; knuckles on the tiller.\n"
                    "She rides a silver four-wheel senior mobility scooter: two front wheels, two rear, high backrest, "
                    "tiller steering, grocery basket. Scooter color, shape, and basket contents stay consistent. "
                    "Jars of pickles bounce but do not vanish. The scooter looks like a real Japanese shinia-ka "
                    "but moves with exaggerated game-physics speed, drifts, and jumps while remaining a mobility scooter."
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
                "why": "Add no morph and no extra wheels after seeing the clip.",
                "craft": "After the clip: no identity morph, no extra wheels, no official replica UI.",
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
        "thinking": "Host-owned pass_03. Grandma, scooter, and basket must not drift.",
        "options": [
            {"id": "p3-1", "label": "hold freeze", "why": "Clip already matches the named marks.", "craft": ""},
            {
                "id": "p3-2",
                "label": "restate freeze",
                "why": "Re-assert silver perm, four-wheel scooter, and pickle basket for pass_03.",
                "craft": (
                    "Pass_03 freeze: adult Japanese grandma about 75–82; short permed silver hair; floral blouse and beige cardigan; "
                    "silver four-wheel senior scooter with tiller and grocery basket; pickles stay in the basket."
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
            "WHY: Auto Pilot — intent-analysis read a person, not a product; creative-agent set the rural-Japan scooter-chase framework.",
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
                "title": "Japanese Grandma GTA",
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
    pack["reason"] = "Sub-workflow SVG template B is the pack picture only. Chat lock is a rural-Japan scooter chase, not a UGC ad."
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


def write_japanese_grandma_gta_walkthrough(root: Path) -> dict[str, Any]:
    from casops.projects import read_project, write_project

    folder = Path(root) / SLUG
    folder.mkdir(parents=True, exist_ok=True)
    if not (folder / "project.json").is_file():
        write_project(
            root,
            {
                "id": SLUG,
                "name": SLUG,
                "title": "Japanese Grandma GTA",
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
    record["title"] = "Japanese Grandma GTA"
    record["notes"] = (
        "sub_workflow_id is the pack-map SVG only. Chat creative lock is a rural-Japan third-person scooter chase, not a UGC ad."
    )
    brief = {
        "name": SLUG,
        "title": "Japanese Grandma GTA",
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
