# LTX-2.5 Complete Operation Guide

**Prompt engineering for total control of LTX video, stills, and image-to-video**

Version: 2026-09-15  
Model covered: Lightricks **LTX-2.5** (Aug 2026 open-weights world model) + **LTX Studio** still-image stack (FLUX.2 Pro / Nano Banana Pro / Z-Image)  
Purpose: a single operating manual so you can (1) write production-grade prompts yourself, (2) keep identity / camera / light / audio under control, and (3) teach another AI to generate LTX-correct prompts on demand.

---

## 0. How to use this document

Read sections 1–4 once. After that, operate from the mode playbooks (section 6) and the checklists (section 22).

If you only do one thing:

1. Decide the **mode** (T2V single-shot, multi-shot, I2V, FLF2V, A2V, Studio still, Dub-It, Edit IC-LoRA).
2. Write a **flowing present-tense paragraph** using the six-part video structure — or the six-part still-image formula.
3. Put numbers (duration, resolution, fps, CFG, steps) in **settings**, never in the prompt.
4. Iterate by changing **one** element per regeneration.

This guide is written for operators. Every rule below exists because LTX-2.5’s Gemma 4 12B text encoder is unusually literal: it will try to render almost everything you write. That is the source of its control — and of most failures.

Primary official sources:

- [LTX-2.5 Prompt Guide](https://ltx.io/blog/ltx-2-5-prompt-guide)
- [Official prompting docs](https://docs.ltx.io/api-documentation/implementation-guides/prompting-guide)
- [LTX-2.5 model spec](https://docs.ltx.io/models/ltx-2-5)
- [LTX Studio image prompt guide](https://ltx.io/blog/ai-image-prompt-guide)

---

## 1. What LTX-2.5 actually is (and is not)

### 1.1 The model

LTX-2.5 is Lightricks’ August 2026 **open-weights video + audio world model**:

| Fact | Detail |
|---|---|
| Architecture | 22B-parameter asymmetric dual-stream diffusion transformer |
| Text encoder | Fine-tuned **Gemma 4 12B** (`gemma4-12b-ltx-v1`), not stock Gemma |
| Output | Synchronized **video + audio** in one pass |
| Modalities | Text-to-video, image-to-video, audio-to-video, video-to-video |
| Headline 2.5 upgrades | Native multi-shot, Diffusion Fidelity Rendering (DFR), new diffusion video decoder, automatic duration, stronger prompt adherence, native 4K HDR / EXR ACES path |
| Variants | `ltx-2-5-fast` (longer clips, cheaper) · `ltx-2-5-pro` (higher fidelity) |
| Distilled vs full | Distilled ≈ 8 steps, CFG 1. Full/dev ≈ 20–50 steps, CFG ~3.0 |
| License | Open weights; community license free for orgs under $10M ARR |
| Weights | [Hugging Face Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) |
| Inference | [GitHub Lightricks/LTX-2](https://github.com/Lightricks/LTX-2) · [ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo) · LTX API |

### 1.2 What it is not

**LTX-2.5 is not a still-image generator.**

Still images inside the LTX ecosystem live in **LTX Studio Gen Space**, which routes to a different stack:

| Studio image model | Role |
|---|---|
| **FLUX.2 Pro** | Precision / spec-sheet photoreal, product, campaign heroes |
| **Nano Banana Pro / 2** | Fast concepting, edits, many variations |
| **Z-Image** | Stylized, illustrated, graphic, non-photoreal |

Those stills become **first frames** for LTX-2.5 image-to-video. That two-stage path is how you get complete visual control: lock identity and composition as a still, then prompt only motion + camera + audio.

LTX Studio (ltx.io/studio) is a separate subscription product that can call LTX-2.5 plus other video models. LTX-2.5 itself is the open model.

### 1.3 Why prompting style changed in 2.5

Earlier diffusion image models rewarded comma-separated tags (`masterpiece, 8k, photorealistic`). LTX-2.5 does not.

The Gemma 4 encoder was fine-tuned with the video model. It parses:

- grammar and prepositions
- spatial relations (`behind`, `camera-left`, `under the hood`)
- causality (`as she turns`, `then the geyser erupts`)
- chronological connectors (`while`, `after`, `a hard cut transitions to`)

Tag stacking produces jerky motion, generic characters, and floating geometry. Natural-language director prose produces coherent shots.

**Wrong family:** `cyberpunk man, walking, neon lights, rainy street, 8k, cinematic, photorealistic, high quality`

**Right family:** `A cinematic low-angle tracking shot follows a lone courier walking through a dense cyberpunk street at night. Neon blue and magenta signs reflect across wet puddles on the asphalt. Steam rises from sewer grates as futuristic hovercars pass overhead. 35mm anamorphic lens, shallow depth of field, atmospheric volumetric haze.`

---

## 2. The control stack — what lives where

Complete control means putting each decision in the layer that can actually enforce it.

```
INTENT
  │
  ├─ IDENTITY / LOOK ──────────── still image (Studio) or reference sheet / I2V first frame
  ├─ COMPOSITION / LENS ───────── still + first sentence of prompt
  ├─ LIGHT LOGIC ──────────────── still + one coherent light description
  ├─ MOTION / PERFORMANCE ─────── prompt (present-tense action)
  ├─ CAMERA PATH ──────────────── prompt prose  and/or  API camera_motion enum
  ├─ AUDIO / DIALOGUE ─────────── prompt (quoted speech + ambience)
  ├─ CUTS / CONTINUITY ────────── multi-shot prose (named transitions)
  ├─ DURATION / RES / FPS ─────── settings fields, NEVER the prompt
  ├─ QUALITY FLOOR ────────────── negative prompt field
  └─ STYLE LOCK / POSE / DEPTH ── IC-LoRA + a look-only prompt
```

### 2.1 Never put these inside the generation prompt

| Keep outside the prompt | Where it lives |
|---|---|
| Duration / clip length | `duration` or `duration: null` |
| Resolution / aspect ratio | `resolution`, width × height |
| Frame rate | `fps` |
| Model name / version | `model`: `ltx-2-5-fast` or `ltx-2-5-pro` |
| CFG, STG, steps, seed | sampler / pipeline settings |
| `8k`, `4k`, `masterpiece`, `trending on artstation` | delete — they are tag-era noise |
| `generate_audio` | boolean setting |
| `camera_motion` enum | API field (optional) |
| `last_frame_uri` | I2V / FLF2V setting |

If you write “10-second 4K 24fps cinematic masterpiece” into the prompt, Gemma 4 will try to *depict* those words instead of treating them as render settings.

### 2.2 What the prompt must own

1. Shot scale and angle
2. One light logic + palette + textures
3. Chronological action
4. Character physical IDs
5. Camera move + where the frame ends
6. Audio (ambience, SFX, music, quoted speech)

---

## 3. Mental model: write a shot, not a caption

A still-image caption names objects. An LTX prompt names a **shot that occupies time**.

Ask three questions the model cannot infer from a static description:

1. **What moves?** Subject, camera, environment — or all three.
2. **How does the camera behave?** Static, dolly, track, pan, tilt, orbit, handheld, crane.
3. **What do we hear?** Room tone, weather, footsteps, score, speech.

Golden rule from the official guide and every serious community skill file:

> If the prompt reads like a still photo, the output will move like one. Every sentence should imply motion or time passing.

Pacing is written as action. Automatic duration sizes the clip to the beats you described. It will not invent a pause you did not write.

- Write `she pauses`, `he holds the silence`, `a beat of silence`
- Do **not** write a bare `Beat.` — the model may speak the word

---

## 4. Standard operating procedure (SOP)

Use this sequence for every generation.

### Step 1 — Lock intent

Write one sentence of human intent, not a prompt:

> “I want a 8–10s night street approach, yellow raincoat woman, then a close-up whisper, then the man’s boots arriving.”

### Step 2 — Choose mode

| You have / you want | Mode |
|---|---|
| Text only, one continuous take | T2V single-shot |
| Text only, 2–4 deliberate cuts | T2V multi-shot |
| Dialogue-heavy, many beats | Screenplay-style T2V |
| One still to animate | I2V (single take unless you intentionally cut away) |
| Start still + end still | FLF2V (fixed duration; no auto-duration) |
| Existing audio drives picture | A2V |
| Existing talking-head, new words | Dub-It IC-LoRA |
| Change one thing in existing video | Video Editing IC-LoRA |
| Pose / depth / canny / motion tracks | Control IC-LoRA (look-only prompt) |
| Need a still first | Studio image (FLUX.2 Pro / Nano Banana / Z-Image) |

If ambiguous, default to **single-shot T2V** or **I2V single take**.

### Step 3 — Write the prompt in the correct form

See section 5 (structure) and section 6 (mode playbooks).

### Step 4 — Fill settings

See section 16. Start with:

- Fast variant, 1280×720 or 1920×1080, 24 fps
- `duration: null` unless you must hit a slot or you are using a last frame
- Prompt enhancer **ON** if the prompt is short or was written for another model
- Prompt enhancer **OFF** if the paragraph already follows this guide
- Negative prompt from section 13

### Step 5 — Generate once, diagnose, change one variable

Use section 18. Do not rewrite the whole prompt after a miss.

### Step 6 — Promote the winner

- Good still → I2V first frame
- Good clip → Edit IC-LoRA for one change, or Dub-It for language
- Sequence of clips → same visual IDs + same light language across prompts

---

## 5. The six-part LTX-2.5 video structure

Official key elements, recommended token order (early tokens are weighted more heavily):

```
shot and style
→ setting and lighting
→ subject detail
→ chronological action
→ camera behavior and resulting frame
→ synchronized audio
```

| # | Element | What to write | What not to write |
|---|---|---|---|
| 1 | **Shot** | Scale + angle + genre look | “cinematic, masterpiece, 8k” |
| 2 | **Scene** | Place, one light logic, 2–3 colors, textures, weather | Mixed neon + softbox + golden hour in one take |
| 3 | **Action** | One dominant sequence, present tense, beginning → end | Five simultaneous actions |
| 4 | **Characters** | Age, hair, wardrobe, distinguishing marks. Emotion as body | “sad”, “happy”, “emotional”, “beautiful” |
| 5 | **Camera** | Named move + intensity + what the move reveals / how it ends | “the camera moves around” |
| 6 | **Audio** | Room tone + SFX + score + quoted speech | Invented on-screen text instead of sound |

### 5.1 Length

- Typical single shot: **4–8 sentences**, one flowing paragraph
- Match detail to framing: close-ups need material and performance detail; wides need geography and movement
- Longer screenplay-style scenes are allowed if every line adds visual, performance, timing, or audio information
- Community ceiling often cited around **~200 words** for a single generation. Past that you are usually stuffing competing instructions

### 5.2 Language rules

- Present tense, active verbs: `walks`, `turns`, `exhales`, `reaches`, `lifts`
- Chronological connectors: `as`, `while`, `then`, `after`, `a moment later`
- Dialogue only inside `"quotation marks"`
- Name language and accent when they matter
- Reuse the same visual ID every time a person reappears: `the woman in the yellow raincoat`

### 5.3 Single-shot skeleton (copy and fill)

```
A [shot scale] [angle] [genre look] frames [subject physical ID] in [setting], [one light logic], [2–3 color anchors], [key textures / weather].
[Subject] [action beat 1], [beat 2], then [beat 3].
The camera [named move + intensity] [relative to the subject], ending on [resulting frame].
[Ambience]. [Action SFX]. [Score]. [Speaker] [delivery]: "[dialogue]".
```

Worked fill:

```
A medium close-up at eye level, documentary 35mm, frames a woman in her early thirties in a yellow raincoat under a dripping awning. Cool neon magenta and cyan bounce off wet asphalt; rain needles through the streetlight.
She wipes water from her brow with the back of her glove, glances off-screen left, then whispers toward the curb.
The camera slowly pushes in, holding her eyes sharp, ending in a tight close-up under the hood.
Soft synth pad and muffled traffic. Rain ticks on the vinyl hood. She whispers, "He's late."
```

### 5.4 Alternative 7-step build order (official LTX-2 family)

Use this when you are assembling from a rough idea:

1. Main action — one sentence
2. Movements and gestures
3. Appearances
4. Environment
5. Camera
6. Lighting and colour
7. Changes / events over time

Then flatten into one paragraph in the six-part order above.

---

## 6. Mode playbooks

### 6.1 Text-to-video — single continuous take

**Use when:** unbroken camera motion, intimate performance, lip-sync in one framing, most I2V jobs.

**Rules**

- One paragraph, present tense
- One dominant event
- One light logic
- 1–2 featured subjects; crowds are texture, not named actors
- Describe camera relative to the subject and say how the frame ends

**Do not** use numbered shot lists.

**Example (official-style multi-beat single take)**

```
A wide shot opens in a warm, sunlit frog yoga studio with a tactile felt-and-fabric look. Golden morning light pours through tall wooden-framed windows, lush green foliage outside, thin wisps of incense smoke curling through the air. A large green frog instructor sits in lotus position on a woven straw mat, wearing an orange robe, eyes gently closed, a serene half-smile. Behind him, rows of smaller green frogs sit on their own mats, throats swelling as they chant a deep resonant "Om" in unison. Soft pond ambience underneath, and the faint buzz of a housefly. The instructor breathes in slowly, then speaks in a deep calm voice: "We are one… with the pond." The frogs answer, "Om…" The camera pans slowly left to a small frog in the front row as the fly drifts past. Its tongue snaps out, catching the fly mid-air. The master exhales, eyes still closed: "But we do not chase the flies… not during class." The guilty frog lowers its head as the others resume the chant.
```

### 6.2 Text-to-video — native multi-shot (2.5-specific)

LTX-2.5 can generate **2–4 connected shots in one clip**, holding character, lighting, style, and voice across cuts.

**Write one chronological paragraph. Name every cut in prose.**

Do not use:

- `Shot 1 / Shot 2`
- numbered beats
- screenplay sluglines **unless** you also name the cut in sentences
- `START FRAME` / `JUMP CUT` list syntax from other models

#### At every cut you must do four things

1. **Name the transition**  
   `A hard cut transitions to…` · `The view cuts to a close-up of…` · `A match cut connects…` · `The image dissolves into…`
2. **Re-establish the new shot** — scale, angle, who is in frame, lighting if it changed
3. **Re-identify recurring people/objects** with the same visual anchors
4. **State audio continuity** — music / dialogue / ambience continues, changes, or drops

#### Multi-shot vs single-shot

| Aspect | Single-shot | Multi-shot |
|---|---|---|
| Camera | One continuous take | New framing after each cut |
| Transitions | Only camera moves (pan, push-in) | Named edits |
| Continuity | Same space throughout | Re-identify subjects; say what carries |
| Audio | One soundscape | Declare continuity at every cut |

`the camera pans` = same take.  
`a hard cut transitions` = new shot.

#### Multi-shot example (official)

```
A wide shot frames a rainy city intersection at dusk, neon signs reflecting on wet asphalt. A young woman in a yellow raincoat walks toward camera, gripping a folded newspaper, while cars hiss past behind her. Soft synth music and distant traffic fill the air. A hard cut transitions to a medium close-up of her face under the hood, raindrops catching the neon as she looks off-screen left; the synth score continues across the cut, traffic muffled. She whispers, "He's late." Another hard cut jumps to a low-angle shot of a man's scuffed boots stepping into a puddle at the curb; the music drops to a low drone. He lifts his head into frame — short dark hair, soaked jacket — and smiles toward her off-screen as a bus rumbles past.
```

**Tips**

- Prefer 2–4 shots. More cuts need shorter, clearer beats
- Give each shot a job: establish → detail → reaction, or wide → medium → close-up
- Do not change wardrobe, geography, or light unless the cut is an explicit time/place jump and you say so

### 6.3 Screenplay-style (dialogue-heavy)

Use when timing and line delivery matter more than a single flowing paragraph.

Keep the same fundamentals: present tense, physical emotion cues, quoted dialogue. If the scene also cuts, **name the cut in prose**. A slugline alone is not a reliable edit instruction.

**Official sample (compressed from docs):**

```
EXT. TOWN STREET – MORNING – LIVE NEWS BROADCAST

The shot opens on a news reporter standing in front of a row of cordoned-off cars, yellow caution tape fluttering behind him. Warm early sun catches the camera lens. A faint hum of chatter and distant drilling fills the air. The reporter, composed but smiling nervously, looks directly into the camera, microphone in hand.
Reporter: "Thank you, Sylvia. And yes — this is a sentence I never thought I'd say on live television — but this morning, here in the quiet town of New Castle, Vermont… black gold has been found!"
He gestures toward the field behind him. "If my cameraman can pan over, you'll see what all the excitement's about." The camera pans right, slowly revealing a construction site surrounded by workers in hard hats. A beat of silence — then, with a sudden roar, a geyser of oil erupts from the ground.
Workers cheer and scramble as the black stream glistens in the morning light. Reporter (off-screen, shouting over the noise): "There it is, folks — a moment New Castle will never forget!"
```

### 6.4 Image-to-video (I2V) — the identity lock

This is the highest-control path for characters, products, and branded looks.

**The still already owns:** identity, wardrobe, composition, setting, lighting, style.

**The prompt may own only:** what changes — subject motion, performance, environmental motion, camera, audio.

#### I2V rules

- 2–5 sentences, present tense, one dominant action
- Do **not** re-list hair, clothes, colors, or lighting already visible
- Re-describing the still causes the encoder to reconcile two slightly different descriptions of the same person → **identity drift / morph mid-clip**
- Prefer a **single continuous take** so the opening frame is not wasted
- Be explicit about camera and audio; there is no prior motion to infer
- Official example: `The woman turns to face the camera and smiles, a warm breeze moving through her hair. Soft piano music plays in the background.`

#### I2V template

```
[Camera behavior]. [Subject action in present tense], [secondary motion: hair, cloth, weather, hands]. [Audio].
```

#### Before / after

❌ Re-describes the still:

```
The woman has long black hair and an ivory coat, standing on a stone balcony above the clouds. Cinematic lighting, 8k, beautiful.
```

✅ Motion only:

```
Her hair and coat lift in the high-altitude wind. The camera slowly pushes forward from behind her as she takes one step toward the edge. Soft wind and a distant waterfall rumble.
```

Community I2V denoise guidance (Comfy / hosted, treat as starting points):

- ~0.45 — preserve identity
- ~0.65 — allow more transformation

### 6.5 First-last-frame to video (FLF2V)

Two stills: first frame + last frame. The model interpolates the path.

**Rules**

- Prompt only the **transition** and the intended ending state
- Start and end frames must be compositionally similar (pose, angle, light). Huge jumps produce warble
- Use a **fixed duration**. Official rule: automatic duration **cannot** combine with `last_frame_uri`
- One dominant physically plausible event
- Name camera behavior across the transition

Template:

```
The camera [move] as [subject] [plausible action that connects frame A to frame B]. [Audio].
```

### 6.6 Audio-to-video (A2V)

Input audio owns timing and energy. The prompt describes the **visual interpretation** of that audio.

- Duration follows the input audio length
- Do not fight the audio’s rhythm in the prose
- Describe who is on screen, how they move with the sound, camera, and light
- `camera_motion` API presets are typically ignored on audio-driven shots — put camera in the prompt if you need it

### 6.7 When to stay single-shot

Stay in one take when you need:

- unbroken camera motion
- intimate performance
- dialogue that must stay lip-synced in one framing
- I2V from a first frame you do not want to cut away from

---

## 7. LTX Studio still-image generation

Use Studio stills when you need a locked hero frame, character sheet, product plate, or I2V first frame.

Prompts work when they behave like a **director’s brief**, not a poem.

### 7.1 Six-part still formula (this order)

1. **Subject** — one clear noun phrase, not a scene dump
2. **Style** — medium, era, or artistic reference
3. **Composition** — shot type and framing
4. **Light** — direction, quality, time of day
5. **Palette** — 2 to 3 dominant colors
6. **Technical** — lens, focus, resolution language

Copy-paste FLUX.2 Pro example (official):

```
A confident female founder in her mid-thirties, editorial portrait photography, medium close-up with shallow depth of field, soft directional window light from camera-left, muted teal and warm neutral palette, ultra-sharp focus, 85mm lens.
```

Same structure, Z-Image painterly:

```
A confident female founder in her mid-thirties, oil painting in the style of contemporary portrait art, medium close-up, warm window light from camera-left, muted teal and terracotta palette, visible brushwork, textured canvas.
```

### 7.2 Model-specific operation

**FLUX.2 Pro — production lock**

- Treat the prompt as a spec sheet
- Front-load the first ~15 words with subject + composition + lighting (early tokens weigh more)
- If one element drifts, edit **only that element** and regenerate
- Best for campaign heroes, product, anything that must stay on brand

Product hero example:

```
Wireless earbuds in charging case, centered on white marble surface, overhead studio lighting with soft diffusion, minimalist e-commerce product photography, monochrome white and pale gray palette with subtle warm highlights, ultra-sharp focus, 100mm macro lens, high resolution.
```

**Nano Banana Pro — concepting**

- Shorter, looser, drop the technical layer
- Generate 5–10 takes, pin 2–3, then rebuild those pins as full FLUX.2 Pro six-part prompts

```
Cyberpunk street vendor, weathered face, neon backlight, gritty urban night, medium shot.
```

**Z-Image — style range**

- Name movement + medium + era. “Illustrated” is not an anchor.
- Use: `art nouveau illustration`, `Bauhaus poster`, `80s anime cel`, `1970s risograph print`

```
A lone hiker on a mountain ridge, art nouveau illustration with flowing organic linework, wide landscape composition, morning fog rising off distant peaks, muted lavender and sage palette with gold accents, decorative border framing.
```

### 7.3 Still-image mistakes that waste credits

1. Vague subject — `a person` averages every person in the training set
2. Contradictory instructions — `photorealistic cartoon`
3. Overloaded prompts — fifty tokens, all compromised
4. Wrong aspect ratio set in the UI after the fact
5. No negative prompt on delivery work

Aspect ratio is a **setting**, not a prompt token.

### 7.4 Recommended still → video handoff

```
Nano Banana  (explore 8–20 directions)
    → pin 2–3
FLUX.2 Pro   (six-part spec, lock identity)
    → export still
LTX-2.5 I2V  (motion + camera + audio only)
    → optional Edit IC-LoRA / Dub-It
```

---

## 8. Complete-control pipeline (image + video together)

This is the production path when “completely control AI” means a specific face, product, or frame.

### Phase A — Design the still

1. Write a six-part still prompt
2. Set aspect to the video aspect you will use (16:9 or 9:16)
3. Generate on Nano Banana for range, lock on FLUX.2 Pro
4. Reject any still with bad hands, warped logos, or mixed light
5. Do not upscale into a different composition; I2V inherits the frame

### Phase B — Write the motion prompt

Answer only:

- What does the subject do?
- Does the camera move, and how does the frame end?
- What do we hear?

### Phase C — Generate I2V

- Single take
- Enhancer off if your motion prompt is already specific
- Auto duration if there is no last frame
- Same negative prompt family as video

### Phase D — Correct without re-rolling identity

- Wrong words on the lips → Dub-It, do not regenerate the face
- One object wrong → Video Editing IC-LoRA, additive phrasing
- Need a different ending → FLF2V with a last-frame still painted or generated from the same identity

---

## 9. Camera lexicon

Pair **move + intensity + relationship to subject + ending frame**.

### 9.1 Shot scale

`extreme close-up` · `close-up` · `medium close-up` · `medium` · `medium wide` · `wide` · `extreme wide` · `establishing shot` · `over-the-shoulder` · `POV` · `macro`

### 9.2 Angle

`eye level` · `low angle` · `high angle` · `overhead` / `bird’s eye` · `Dutch angle` · `ground-level`

### 9.3 Moves

| Move | What it does | Use when |
|---|---|---|
| Dolly in / push in | Camera physically closer | Emotion, reveal, product detail |
| Dolly out / pull back | Camera physically away | Reveal environment, ending wide |
| Track / follow | Lateral or behind the subject | Walking, driving, fashion |
| Pan left / right | Rotate on a fixed axis, horizontal | Scan space, follow action |
| Tilt up / down | Rotate on a fixed axis, vertical | Hero reveal, architecture |
| Orbit / circles around | Arc around subject | Product, duel, 360 showcase |
| Crane / jib up / down | Vertical height change | Landscape → intimate |
| Handheld | Organic micro-shake | Documentary, vlog |
| Static frame | Locked off | Dialogue, subject-only motion |
| FPV flythrough | Multi-axis aerial | Canyons, action geography |
| Dolly zoom | Zoom in while dollying back | Psychological shock |
| Macro rack focus | Focus near → far | Detail then context |
| Whip pan | Fast pan | Energy, transition inside a take |

### 9.4 Intensity words (pair with every move)

`subtle` · `gentle` · `slight` · `steady` · `gradual` · `smooth` · `dramatic` · `rapid` · `sweeping`

### 9.5 High-adherence camera sentence

```
A [scale] at [angle] [intensity] [move] [relative to subject], keeping [what stays sharp], ending on [resulting frame].
```

Good: `A medium close-up at eye level slowly pushes toward her face as she reads the letter, keeping her eyes sharp, ending in a tight close-up.`

Bad: `the camera moves around`

### 9.6 Lens and film markers (use sparingly, one register)

`35mm anamorphic` · `85mm portrait` · `100mm macro` · `shallow depth of field` · `film grain` · `Kodak Vision3 500T` · `lens flare` · `Alexa look` · `35mm documentary`

### 9.7 API camera presets (settings field, not prose)

Documented `camera_motion` / `cameraMovement` enum:

`dolly_in` · `dolly_out` · `dolly_left` · `dolly_right` · `jib_up` · `jib_down` · `static` · `focus_shift`

Use the enum for batch repeatability. Use prompt prose for orbit, handheld, crane, compound moves. If you set both, they must agree. Presets are generally ignored on audio-driven shots.

---

## 10. Lighting, palette, texture, atmosphere

### 10.1 One light logic per shot

Mixed sources (`neon + softbox + golden hour + candle`) confuse the encoder. Pick a primary and, at most, one motivated accent.

Describe light as:

- source (`window camera-left`, `overhead tungsten`, `neon from above`)
- quality (`soft`, `hard`, `diffused`, `flickering`)
- direction
- time of day / weather interaction
- what it hits (`raindrops catching neon`, `rim on the visor`)

### 10.2 Vocabulary (official “additional helpful terms” plus production extras)

**Lighting:** flickering candles · neon glow · natural sunlight · dramatic shadows · golden hour · tungsten warmth · sodium streetlights · soft key · rim / backlight · volumetric dusk through fog · overcast cool · window light camera-left

**Textures:** rough stone · smooth metal · worn fabric · glossy surfaces · wet asphalt · weathered leather · porcelain · felt-and-fabric

**Palette:** vibrant · muted · monochromatic · high contrast · plus 2–3 named colors (`muted teal and warm neutrals`, `navy and crimson`, `lavender, sage, gold`)

**Atmosphere:** fog · rain · dust · smoke · particles · steam from grates · incense wisps

**Scale words:** expansive · epic · intimate · claustrophobic

**Pacing words:** slow motion · time-lapse · lingering shot · continuous shot · freeze-frame · fade-in / fade-out · sudden stop

**Style categories:** stop-motion · 2D / 3D animation · claymation · hand-drawn · comic book · cyberpunk · 8-bit pixel · surreal · minimalist · painterly · illustrated · period drama · film noir · fantasy · thriller · documentary · arthouse

### 10.3 Domain vocabulary (advanced)

LTX’s encoder responds to craft shorthand if you **rank** domains instead of stacking them equally.

- VFX-primary: rotoscope, matte painting, rack focus
- Animation-secondary: contact / breakdown poses, ease-in / ease-out
- Restoration-tertiary: telecine, gate weave, Kodachrome

Equal weighting averages the look. Name the primary first and most.

Do not write anachronisms (`1920s Kodachrome` — Kodachrome is 1935+).

---

## 11. Audio and dialogue

LTX-2.5 generates picture and sound together. Audio is a first-class control surface, not a garnish.

### 11.1 Three layers

1. **Ambience / room tone** — quiet room tone, rain on vinyl, distant traffic, pond, HVAC, forest birds
2. **Action SFX** — footsteps in a puddle, a bus rumble, a tongue snap, oil geyser roar
3. **Score / voice** — soft synth pad, low drone, whispered line, unison chant

Place sound next to the action that causes it.

### 11.2 Dialogue format

```
[Speaker] [delivery / physical cue]: "[exact words]"
```

Rules:

- Spoken words **only** inside quotation marks
- Specify language and accent when they matter
- Use native script for non-Latin languages
- Direct performance with physical cues and voice quality, not mood labels
- Voice qualities: whisper, mutter, shout, scream; resonant, cracking, monotone, childlike
- For multi-shot, declare whether dialogue continues or drops at the cut
- If you want silence, omit invented sound and set `generate_audio: false`

Good: `He pauses, looks to the side, then continues with a cracking voice: "I didn't see her leave."`

Bad: `He says something sad and emotional.`

### 11.3 Bilingual briefs

Write the **generation prompt in English** even if your notes are in Chinese. Put spoken lines in the native language inside quotes and name the language.

```
She leans toward the microphone and speaks in Cantonese, low and even: "今晚慢慢嚟就得。" Rain ticks on the window. Soft room tone.
```

English (or the model’s strongest cinematic language) carries camera and light. Native script carries the mouth shapes and phonetics.

---

## 12. Continuity system (how to keep the same person)

Text alone will not give you the same face twice. Official mistake #6: generating character-specific scenes without image conditioning.

### 12.1 Identity stack, strongest first

1. Same I2V first-frame still
2. Same visual ID string in every prompt (`the woman in the yellow raincoat, earlier at the table`)
3. Multi-shot inside one generation (2.5 holds character across named cuts)
4. Ingredients / reference-sheet IC-LoRA
5. Fine-tune / character LoRA on the 2.5 base checkpoint

### 12.2 Continuity checklist across cuts or clips

- Same wardrobe words
- Same hair words
- Same distinguishing mark
- Same light logic unless you announce a time jump
- Same voice description
- No unexplained geography change
- Audio continuity stated

---

## 13. Negative prompts

Negatives live in a **separate field**. They work through classifier-free guidance: the sampler steps away from the negative conditioning.

### 13.1 Operating rules

- 5–15 tokens. Five to eight clear concepts beat a 40-word dump
- Do not negate something the positive asked for (`dramatic lighting` + negative `shadows`)
- Distilled pipelines run at CFG 1, so classic CFG negatives may do nothing unless you use NAG (Normalized Attention Guidance, e.g. KJNodes `LTX2_NAG`) or the full/dev model
- Skip long negatives while exploring; use them on anything client-facing

### 13.2 Five buckets

1. **Quality:** `blurry, low resolution, jpeg artifacts, noise, grain`
2. **Anatomy:** `distorted hands, extra fingers, fused fingers, deformed face, asymmetric eyes`
3. **Brand pollution:** `watermark, signature, text overlay, logo, captions`
4. **Style drift** (when you want photoreal): `cartoon, illustration, 3D render, anime, painting, sketch`
5. **Video motion:** `flicker, frame jump, temporal inconsistency, character morphing, identity drift, static frame`

### 13.3 Base recipes

Universal video (copy):

```
blurry, low resolution, jpeg artifacts, distorted hands, extra fingers, deformed face, watermark, text overlay, flicker, frame jump, temporal inconsistency, static frame, cartoon, illustration
```

Studio photoreal still:

```
blurry, low quality, distorted, watermark, text, cluttered background, painting, illustration, cartoon
```

Community Comfy T2V extra (games/cartoon pull):

```
pc game, console game, video game, cartoon, childish, ugly
```

Default documented family in several LTX-2.x pipelines is along the lines of `worst quality, low quality, blurry, distorted` — expand it with the buckets above rather than replacing it with a novel.

---

## 14. JSON prompting (LTX Studio production)

Use prose while exploring. Convert to JSON when a direction must be repeated by a team or iterated one field at a time.

Top-level keys: `scene`, `subject`, `camera`, `duration`.

```json
{
  "scene": {
    "description": "A product launch event in a modern conference room",
    "lighting": "Bright, professional, softbox-style",
    "atmosphere": "High-energy, corporate"
  },
  "subject": {
    "type": "person",
    "action": "presenting to a small audience",
    "position": "center frame, standing"
  },
  "camera": {
    "angle": "eye level",
    "movement": "slow push in",
    "shot_type": "medium shot"
  },
  "duration": 5
}
```

Camera field values that parse cleanly:

- shot_type: `close-up` · `medium shot` · `wide shot` · `establishing shot`
- angle: `eye level` · `low angle` · `high angle` · `overhead` · `bird’s eye`
- movement: `static` · `dolly in` · `dolly out` · `pan left` · `pan right` · `tilt up` · `tilt down` · `orbit`

For LTX-2.5 open-weights inference, flatten JSON back into a flowing paragraph before encode. The Gemma 4 video encoder expects prose. JSON is a Studio / pre-production tool.

---

## 15. IC-LoRA and special formats

These are not generation prompts. Using a cinematic six-part paragraph here will fight the adapter.

### 15.1 Dub-It (speech replacement, V2V)

Replace spoken dialogue in an existing video. The model does **not** translate for you.

Template — output only this:

```
[Speaker] is speaking [Language/Accent], saying: "[full replacement dialogue]"
```

Example:

```
A woman speaking in Russian saying: "Сегодня отличный день, чтобы протестировать рабочие процессы ComfyUI для дубляжа с использованием LTX."
```

Requirements:

- Full dialogue text, native script
- One speaker (beta does not distinguish multiple speakers)
- Match timing / syllable length to source. Slightly longer is safer than short (too long → skipped words; too short → sluggish delivery)
- Validated languages: English, French, Spanish, German, Russian
- Optional delivery/emotion only when requested

Weights reference: [Lightricks LTX-2.3-22b IC-LoRA DubIt](https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-DubIt) (used with 2.x IC-LoRA workflows).

### 15.2 Video Editing IC-LoRA

One concrete, **additive** instruction per pass. Name what changes and what stays.

```
[Desired edited state]. Preserve [identity, action, timing, camera motion, background, lighting, and other unchanged elements].
```

Do not write a full scene-generation prompt. Do not rely only on negation (`remove the bag`). Prefer `She now holds a paper coffee cup. Preserve identity, stride, camera track, rain, and neon.`

### 15.3 Structure / Control IC-LoRA (Canny, Depth, Pose, Union, Motion Track)

- Distilled checkpoint
- Default strength 1.0; combined LoRA strength under 2.0
- Prompt **visual style, appearance, light only**
- Do **not** describe motion — the guide video or tracks own motion
- Conflicting motion text causes warble

Motion Track: draw sparse tracks on the first frame; prompt the look, not the path.

Ingredients sheet: describe elements by position on the reference sheet, then the generated action separately.

### 15.4 Inpaint / outpaint

Describe the **full desired scene**, not “replace the sky”. The adapter fills toward a complete target state.

### 15.5 DFR (Diffusion Fidelity Rendering)

Same prompting style as distilled generation. Extra keyframes + detailing adapter. Longer runtime and VRAM. Use when pixel fidelity on faces, type, and product detail matters more than speed.

---

## 16. Settings bible (outside the prompt)

### 16.1 Hosted API — LTX-2.5

Source: [docs.ltx.io/models/ltx-2-5](https://docs.ltx.io/models/ltx-2-5)

| | Fast | Pro |
|---|---|---|
| Role | Speed, longer clips | Fidelity |
| T2V / I2V / A2V | Yes | Yes |
| Retake / extend / reframe | Not on 2.5 endpoints | Not on 2.5 endpoints |

Resolution (16:9 / 9:16):

| Name | Landscape | Portrait |
|---|---|---|
| 720p | 1280×720 | 720×1280 |
| 1080p | 1920×1080 | 1080×1920 |
| 1440p | 2560×1440 | 1440×2560 |
| 4K | 3840×2160 | 2160×3840 |

Duration matrix:

| Variant | Res | FPS | Duration (seconds) |
|---|---|---|---|
| Fast | 720p / 1080p | 24, 25 | 6, 8, 10, 12, 14, 16, 18, 20 |
| Fast | 720p / 1080p | 48, 50 | 6, 8, 10 |
| Fast | 1440p / 4K | 24, 25, 48, 50 | 6, 8, 10 |
| Pro | all listed | 24, 25, 48, 50 | 6, 8, 10 |

**Automatic duration:** send `"duration": null`. The field is still required. The model sizes the clip from the action. A one-line action stays short; a multi-shot paragraph runs longer. Result will not exceed the max for that res/fps.

**Cannot combine** `duration: null` with `last_frame_uri`.

Other API fields:

- `generate_audio: false` — silent video
- `camera_motion` — enum listed in 9.7
- `last_frame_uri` — FLF2V on I2V / A2V

Example (official):

```bash
curl -X POST https://api.ltx.io/v2/text-to-video \
  -H "Authorization: Bearer $LTX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "ltx-2-5-fast",
    "prompt": "A lighthouse keeper climbs the stairs, then the beam sweeps out over the water",
    "duration": null,
    "resolution": "1280x720",
    "fps": 24
  }'
```

### 16.2 Local / ComfyUI constraints

Official templates: ComfyUI 0.32.0+ · [ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo) · `example_workflows/2.5/`

Common official templates:

- T2V / I2V two-stage distilled (default)
- T2V / I2V single-stage distilled
- FLF2V single-stage
- A2V two-stage
- Union Control, V2V IC-LoRA, Ingredients, Motion Track

Hard numbers:

| Constraint | Value |
|---|---|
| Width / height | Divisible by 32 (some pipelines 64) |
| Frame count | `num_frames % 8 == 1` (97, 121, 153, 169, 185…) |
| 97 frames @ 24 fps | ≈ 4.0 s |
| 121 frames @ 24 fps | ≈ 5.0 s |
| VRAM floor | ~16 GB distilled int8-convrot; 24 GB+ bf16 comfortable |
| 16 GB practical canvas | Stay around 960×544 or 1056×608, short clips |

### 16.3 Sampler starting points

**Distilled (default local / Fast):**

- Steps: fixed short schedule (~8)
- Video CFG: **1.0** (raising CFG does not help)
- STG: 0 or 1. High STG → rubbery skin
- Prompt enhancer: ON for short prompts, OFF for finished six-part prompts
- Two-stage (stage-1 + 2× spatial upscaler + 3-step refine) when VRAM allows

**Full / dev:**

- Steps: 20–50 (30 is a common center)
- Video CFG: ~3.0 (community working range ~3.0–4.2)
- Audio CFG: ~7.0
- STG: ~1.0, blocks often `[28]`
- modality_scale: ~3.0
- guidance_rescale: ~0.7

### 16.4 Prompt enhancer

Gemma 4 E2B rewrite pass, tuned separately for T2V and I2V.

| Turn it ON | Turn it OFF |
|---|---|
| Short, rough, or translated briefs | Prompt already follows this guide |
| Prompts written for Sora / Veo / Kling / Flux tags | You need bit-exact wording |
| First exploration | I2V motion-only prompts you already tightened |

Enhancer can invent detail you did not ask for. That is useful for empty briefs and harmful when you already specified the shot.

### 16.5 16 GB local recipe

- Distilled int8-convrot
- Two-stage if it fits, else single-stage
- 960×544 or 1056×608
- 24 fps, 6–8 s or auto duration
- CFG 1
- Enhancer off once the prompt is six-part
- `generate_audio` on unless you will replace sound in post

---

## 17. Common mistakes and fixes

### 17.1 Tag stacking (Stable Diffusion / Flux habit)

❌ `cyberpunk man, walking, neon lights, rainy street, 8k, cinematic, photorealistic, masterpiece`

✅ `A cinematic low-angle tracking shot follows a lone courier walking through a dense cyberpunk street at night. Neon blue and magenta signs reflect across wet puddles. Steam rises from sewer grates. 35mm anamorphic lens, shallow depth of field, atmospheric volumetric haze.`

### 17.2 Treating video like an image caption

❌ `A woman in a red dress, cinematic lighting, high detail`

✅ `A woman in a red dress walks into a sunlit kitchen from the left, moves to the counter, and begins preparing coffee. The camera follows her from behind at a slight distance. Soft room tone, a kettle beginning to hiss.`

### 17.3 Underspecified motion

❌ `A dog running in a field`

✅ `A golden retriever sprints across an open field, the camera tracking alongside it from a low angle. Motion is fast and fluid. As the dog reaches a tree, it slows and looks back. Wind in grass, paws hitting dirt.`

### 17.4 Conflicting instructions

❌ `A fast action sequence with slow motion and dramatic freeze frames` plus `still peaceful lake with dramatic crashing waves`

✅ Pick one speed and one physical state. `A fighter lands a punch in slow motion. The impact holds for a beat, then the clip resumes at normal speed as they pull back.`

### 17.5 Missing camera

❌ `A chef prepares food in a restaurant kitchen`

✅ `A chef dices vegetables in a busy restaurant kitchen. Close-up on the hands and knife. The camera remains static. Warm overhead lighting. Background activity is blurred. Knife on the board, distant ticket printer.`

If the shot should not move, write `static` explicitly. Otherwise the model often inserts gentle handheld drift.

### 17.6 Overcrowded prompt

Five named subjects + three camera behaviors + busy background = the model satisfies the most average subset.

Fix: one featured subject, one action, one camera behavior, crowd as texture.

### 17.7 No image conditioning for a specific person

Two text-only clips with the same character paragraph will be two different people.

Fix: generate or photograph a still, then I2V. Reuse the still.

### 17.8 I2V re-describes the still

Causes mid-clip morph.

Fix: motion, camera, audio only.

### 17.9 Multi-shot written as a shot list

❌ `Shot 1: wide. Shot 2: close-up. Shot 3: boots.`

✅ One paragraph with `A hard cut transitions to…` and audio continuity.

### 17.10 Abstract emotion labels

❌ `she looks sad and confused`

✅ `her eyes drop to the letter, lips press together, she grips the table edge`

### 17.11 Numbers inside the prompt

❌ `10 seconds, 4K, 24fps, CFG 3.5`

✅ Settings fields. Pace with `she pauses`.

### 17.12 Pasting another model’s prompt

Sora / Veo / Kling / Midjourney syntax underperforms.

Fix: rewrite into a flowing present-tense paragraph, or run the enhancer once, then tighten.

### 17.13 Official four failures (Studio video+image brief)

1. Vague subject — name wardrobe, build, one physical mark
2. Conflicting style cues — one visual register per shot
3. Missing motion — state `static` or the exact move
4. Overstuffed scene — fewer subjects

### 17.14 Five still-image credit burners

Vague subject · contradictory style · overloaded tokens · wrong aspect in the UI · no negative on delivery work

---

## 18. Diagnostic table

| Symptom | Likely cause | Fix |
|---|---|---|
| Clip is almost a still | No motion verbs; image-style caption | Add subject action + named camera + audio |
| Identity morphs mid I2V | Prompt re-described hair/clothes/light | Delete static details; motion only |
| Extra people appear | Too many actors / vague “crowd of…” | One or two named subjects |
| Flicker / warble | Mixed lights, chaotic physics, conflicting camera | One light, simpler motion, one camera path |
| Ignores your subject | Prompt too short or all tags | Six-part paragraph, subject in sentence 1–2 |
| Cuts ignored or smashed together | Shot list / sluglines without prose cuts | `A hard cut transitions to…` + re-establish |
| Wrong duration | Beats not written; or duration field fights last frame | Write pauses; use `duration: null` or a fixed slot, not both with last_frame |
| Rubber skin | STG too high on distilled | STG 0–1, CFG 1 |
| Negative does nothing | Distilled CFG 1 | NAG node, or full model, or stop expecting CFG negatives |
| Lip-sync drift after a cut | Multi-shot dialogue across framings | Keep talking-head in one continuous take |
| On-screen text misspelled | Model limit | Short prominent text only; finish titles in post |
| Geography / wardrobe pop | Continuity not restated | Same visual IDs; announce time jumps |
| Enhancer invented props | Enhancer ON over a finished prompt | Turn enhancer off |
| Audio fights picture | Sound not tied to visible action | Place SFX next to the verb that causes it |

---

## 19. Iteration protocol

Do not rewrite the whole prompt after a near-miss.

Change **one** of:

1. Shot scale
2. Camera move / intensity
3. Light logic
4. Action beat
5. Audio layer
6. Negative bucket

Three structural edits cover most video misses:

- Change framing (`wide` → `medium close-up`)
- Change motion (`slow push-in` → `static` or `handheld track`)
- Change register (`neon noir` → `soft window light, documentary`)

If three structural edits fail, start again from the six-part skeleton. Do not keep tacking adjectives onto a broken paragraph.

Convert any foreign prompt with this recipe:

1. Strip tags, qualities, and numbers
2. Identify subject, action, place, camera, light, audio
3. Rewrite as one present-tense paragraph in six-part order
4. Move numbers to SETTINGS
5. Decide enhancer on/off

---

## 20. Sample prompt library

Settings suggested beside each prompt are starting points, not laws. Do not paste the settings line into the prompt box.

### 20.1 Single-shot T2V — street approach

```
A low-angle medium-wide tracking shot follows a young woman in a yellow raincoat walking toward camera down a rainy city intersection at dusk. Neon magenta and cyan signs smear across wet asphalt. She grips a folded newspaper under one arm, breath visible in the cold. The camera tracks backward at her walking pace, keeping her centered, ending in a medium shot under a dripping awning. Soft synth pad, tires hissing through puddles, rain ticking on vinyl.
```

Settings: Fast, 1280×720, 24 fps, duration null, enhance off if used as written.

### 20.2 Multi-shot T2V — wait / whisper / arrival

Use the official yellow-raincoat multi-shot in section 6.2.

### 20.3 I2V — portrait live

```
She slowly turns her face toward the camera and lets a small smile form. A light breeze lifts a few strands of hair across her cheek. The camera holds static. Soft breathing, distant city ambience, a faint vinyl crackle.
```

### 20.4 I2V — product

```
The camera performs a slow orbit around the matte-black headphones as the lid of the charging case eases open. A single studio highlight travels along the earcup. Quiet room tone, a soft plastic click as the lid settles.
```

### 20.5 Screenplay / news (see section 6.3)

Use the New Castle oil-geyser official sample when you need timed dialogue plus a camera pan to a sudden event.

### 20.6 Studio still — FLUX.2 Pro character plate (then I2V)

```
A woman in her early thirties in a yellow vinyl raincoat with the hood up, editorial cinematic still, medium close-up three-quarter view, cool neon magenta and cyan bounce light from camera-right, rain beads on the hood, muted navy and wet-asphalt palette, 85mm, shallow depth of field, ultra-sharp eyes.
```

Negative: `blurry, distorted face, extra fingers, watermark, text, illustration, cartoon`

### 20.7 Community-style cinematic (rewrite numbers out of the prose)

These are adapted from public LTX 2.5 galleries. CFG/steps belong in the sampler.

Cyberpunk alley:

```
A cinematic low-angle tracking shot follows a woman in a translucent holographic raincoat through a crowded Tokyo alley at midnight. Vibrant neon magenta and cyan advertisements ripple across wet puddles. Rain streaks the lens. Volumetric steam rises from street-food stalls as she glances toward a giant holographic koi floating overhead. Distant bass and sizzling oil, rain on plastic.
```

Watchmaker:

```
An intimate documentary close-up of an elderly watchmaker with silver wireframe glasses working in a wood-paneled workshop. Warm tungsten lamplight hits brass gears and microscopic springs. The camera slowly pushes in on his hands as tweezers place a tiny ruby jewel. Dust motes drift through the beam. Quiet ticking, a single clock heartbeat, soft room tone.
```

Lighthouse (I2V-friendly):

```
A lighthouse keeper walks along the rocky shore at sunset. He steps carefully over wet stones, heavy oilskin coat flaring. The camera tracks beside him with smooth lateral movement. Waves crash in the foreground, seabirds circle overhead, and the golden light intensifies as the sun dips. Surf, gulls, wind in the coat.
```

### 20.8 Dub-It

```
A man speaking in English with a quiet Midland accent, saying: "I waited under the awning until the bus lights turned the puddles white."
```

### 20.9 Video Editing IC-LoRA

```
The folded newspaper in her hand is now a paper coffee cup with a heat sleeve. Preserve her face, yellow raincoat, walking pace, backward tracking camera, rain, and neon reflections.
```

### 20.10 Control IC-LoRA (pose / depth guide video)

```
Photoreal night-street fashion look, yellow vinyl raincoat, cool neon magenta and cyan rim light, wet asphalt reflections, shallow depth of field, 35mm.
```

No walking / running / camera verbs — the guide owns motion.

---

## 21. Teach an AI to generate LTX prompts

Paste the block below into a Claude Project, Cursor rule, custom GPT, OpenWebUI system prompt, or agent skill. It is the operational contract for any LLM that will write prompts for you.

```text
# LTX Prompt Engineer — System Skill

You are an expert prompt engineer for Lightricks LTX.

## Model map (do not confuse)
- LTX-2.5 = open-weights 22B video+audio world model (Aug 2026). Modalities: T2V, I2V, A2V, V2V, native multi-shot, joint audio. Text encoder = fine-tuned Gemma 4 12B. Optional Gemma 4 E2B prompt enhancer.
- LTX Studio still images = FLUX.2 Pro (precision/spec-sheet), Nano Banana Pro/2 (fast concept / edit), Z-Image (stylized/non-photo).
- Never treat LTX-2.5 as a tag-stack image model. No "masterpiece, 8k, photorealistic". It parses grammar, prepositions, spatial relations, and causality.

## Hard rules
1. Output the GENERATION PROMPT only in a fenced block, then a short SETTINGS block (duration/resolution/fps/enhance/negative) outside the prompt.
2. NEVER put duration, resolution, fps, aspect ratio, CFG, steps, model name, or "8k" inside the generation prompt.
3. Present tense. Active verbs. Chronological order.
4. Emotion via physical cues only (gaze, posture, hands, breath, voice quality) — never "sad", "happy", "emotional".
5. Spoken words ONLY inside "quotation marks". Name language/accent/delivery when relevant.
6. One coherent light logic per shot. Few subjects. Every sentence must add visual, motion, or audio detail.
7. Do not copy prompts written for Sora / Veo / Kling / Seedance / Flux tag syntax. Rewrite into LTX flowing-paragraph form.
8. Pauses must be written as action ("he pauses", "holds the silence"). Never a bare "Beat."
9. If the user is unclear, pick a mode and state the assumption in one line before the prompt.
10. If the user's brief is not English, keep camera/light/action in English and put spoken lines in the native language inside quotes, with the language named.

## Choose mode first
- T2V single-shot: default. One continuous take. 4–8 flowing sentences.
- T2V multi-shot: only if the user wants cuts. 2–4 shots. One chronological paragraph. Name every cut in prose.
- Screenplay-style: dialogue-heavy / many beats. Headers + character cues + quoted lines OK. If there are cuts, name them in prose; a slugline alone is not an edit.
- I2V: input image is the first-frame anchor. Prompt ONLY motion, camera, performance, environment change, audio. Do NOT re-list hair/clothes/lighting already visible.
- FLF2V: first + last frame. Describe the plausible chronological path between them. Fixed duration required (cannot combine with auto-duration).
- A2V: audio anchors timing; prompt the visual interpretation of that audio.
- Dub-It: existing talking-head video. Output ONLY:
  [Speaker] is speaking [language/accent], saying: "[full native-script dialogue]"
  Validated languages: English, French, Spanish, German, Russian. Match syllable length to source. One speaker. Model does not translate.
- Video Editing IC-LoRA: ONE additive instruction:
  [Desired edited state]. Preserve [identity, action, timing, camera, background, lighting].
- Control IC-LoRA (Canny/Depth/Pose/Motion-Track): prompt STYLE + SUBJECT + LOOK only. Do not describe motion.
- Ingredients IC-LoRA: Reference sheet: <panel descriptions> / Generated video: <action>
- Inpaint/Outpaint: describe the FULL desired scene, not the edit.
- Studio still image: six-part image formula, not the video paragraph.

## LTX-2.5 six-part video structure (early tokens weigh more)
1. Shot — scale + angle + genre look
2. Scene — setting, one light logic, 2–3 color anchors, textures, atmosphere
3. Action — beginning→end in present tense; connectors: as / while / then / after
4. Characters — age, hair, wardrobe, distinguishing features; physical emotion cues; reuse the same visual ID across cuts
5. Camera — named move + intensity + what the move reveals / how the frame ends
6. Audio — room tone + action SFX + score + quoted speech, synced to visible action
   At every multi-shot cut, state whether music/dialogue/ambience continues or changes.

Single-shot template:
[shot + style]. [setting + lighting + palette]. [subject physical detail] [present-tense action sequence]. [camera move relative to subject, and the resulting frame]. [ambience + SFX + music + "dialogue"].

Multi-shot cut glue:
"A hard cut transitions to…" / "The view cuts to…" / "A match cut connects…" / "The image dissolves into…"
Then re-establish scale, angle, who is in frame, lighting if changed, same visual IDs, audio continuity.

## LTX Studio still-image six-part formula
Subject (one noun phrase) → Style (medium/era/ref) → Composition (shot + framing) → Light (direction/quality/time) → Palette (2–3 colors) → Technical (lens/focus).
- FLUX.2 Pro: spec-sheet; front-load first 15 words with subject + composition + light.
- Nano Banana Pro/2: shorter, looser; iterate many takes; then lock in FLUX.2 Pro.
- Z-Image: name movement + medium + era.
Never put aspect ratio inside the prompt; set it in the UI.

## Settings that stay OUTSIDE the prompt
- duration: null (auto from prompt) OR explicit seconds. Auto cannot combine with last_frame_uri.
- resolution: 720p/1080p/1440p/4K; 16:9 or 9:16. Width/height divisible by 32.
- fps: 24/25/48/50. Fast: 6–20s at 24/25 720p–1080p; 6–10s at 48/50 and at 1440p/4K. Pro: 6–10s all tiers.
- generate_audio: false for silent.
- camera_motion API param must not contradict the prose.
- prompt enhancer ON for short/rough/foreign-model prompts; OFF when the paragraph is already production-grade.
- Full model CFG ~3.0–3.5, STG ~1.0. Distilled: CFG 1, ~8 steps.
- Local frame count: num_frames % 8 == 1.

## Negative prompts (separate field)
Keep 5–15 tokens. Do not contradict the positive.
Universal video: blurry, low quality, distorted anatomy, warped faces, flickering background, unnatural jitter, sudden popping geometry, overexposed, oversaturated colors, static freeze frame, watermarks, text overlays
Studio photoreal: blurry, low resolution, distorted, painting, illustration, cartoon, anime, sketch, oversaturated, watermark, text, signature

## Known weaknesses (do not promise)
- On-screen text: keep short and prominent; finish titles in post.
- Chaotic physics: prefer plausible everyday motion.
- Crowded frames and mixed light sources degrade adherence.

## Quality bar before you output
- Specificity > vagueness
- Named cinematography > "cinematic" / "beautiful" / "8k"
- Physical cues > emotion labels
- One dominant action per shot
- I2V does not re-describe the still
- Multi-shot names cuts in prose, not a numbered shot list
- Dialogue is quoted
- Every sentence implies time passing

## Output format
Assumption: <one line>
MODE: <T2V-single | T2V-multi | screenplay | I2V | FLF2V | A2V | Dub-It | Edit-ICLoRA | Control-ICLoRA | Ingredients | Studio-still>
PROMPT:
<the generation prompt in a fenced block>
SETTINGS:
- duration:
- resolution / aspect:
- fps:
- enhance_prompt:
- generate_audio:
- negative:
WHY (3 bullets max): what you locked and why
```

### 21.1 How to train the teacher on *your* taste

After pasting the skill, add a short house style block. Example:

```text
House style:
- Default to 35mm documentary or 85mm portrait unless asked for anime / noir / product.
- Default audio always includes room tone.
- Prefer one subject, yellow-raincoat test character for night exteriors.
- Spoken Cantonese goes in quotes with "speaks in Cantonese".
- Never add lens flare unless requested.
```

Then give it 3–5 of your accepted prompts as few-shot examples. The encoder is literal; the teacher LLM should copy *your* sentence rhythm, not invent a new house style each turn.

### 21.2 Conversion command you can give any LLM

```text
Rewrite the following as an LTX-2.5 prompt.
Mode: [single-shot T2V | multi-shot | I2V | Studio still].
Strip tags and numbers. Present tense. Six-part order.
Put duration/res/fps in SETTINGS. Quote any dialogue.
Source prompt:
[paste]
```

---

## 22. Checklists

### 22.1 Pre-generation (video)

- [ ] Mode chosen
- [ ] Prompt is a shot, not a caption
- [ ] Present tense, chronological
- [ ] Shot scale + angle named
- [ ] One light logic
- [ ] One dominant action
- [ ] Character physical IDs (or I2V still supplies them)
- [ ] Camera named, or `static` explicit
- [ ] Audio present (or `generate_audio: false`)
- [ ] Dialogue in quotes
- [ ] No duration / res / fps / CFG / 8k in the prose
- [ ] Multi-shot: named cuts, re-IDs, audio continuity
- [ ] I2V: no re-description of the still
- [ ] Negative filled for delivery work
- [ ] Enhancer on or off on purpose

### 22.2 Pre-generation (Studio still)

- [ ] Six-part order
- [ ] Subject is a noun phrase
- [ ] Model matches job (FLUX lock / Banana explore / Z style)
- [ ] Aspect set in UI to the future video aspect
- [ ] Palette is 2–3 colors
- [ ] Negative present for delivery
- [ ] First 15 words contain subject + frame + light (FLUX.2 Pro)

### 22.3 Post-generation

- [ ] Identity stable across frames
- [ ] Motion matches the verbs
- [ ] Light did not mix itself
- [ ] Audio syncs with visible causes
- [ ] On-screen text verified or slated for post
- [ ] If failing: change one element, do not rewrite everything

---

## 23. Reference sites

### 23.1 Official — LTX-2.5 video prompting

| Resource | URL | Why it matters |
|---|---|---|
| LTX-2.5 Prompt Guide | https://ltx.io/blog/ltx-2-5-prompt-guide | Canonical 6-element + multi-shot + Dub-It |
| Docs prompting guide | https://docs.ltx.io/api-documentation/implementation-guides/prompting-guide | Same guide + samples + enhancer |
| Markdown copy | https://docs.ltx.io/api-documentation/implementation-guides/prompting-guide.md | Agent-readable |
| OSS prompting guide | https://docs.ltx.io/open-source-model/usage-guides/prompting-guide | Local/open-source copy |
| Model spec | https://docs.ltx.io/models/ltx-2-5 | Fast/Pro, duration, res, fps, auto duration |
| Agent index | https://docs.ltx.io/llms.txt | Append `.md` to any docs URL |
| Official MCP | https://docs.ltx.io/_mcp/server | Claude Code / Cursor |
| Product page | https://ltx.io/model/ltx-2-5 | Capabilities overview |
| Launch post | https://ltx.io/newsroom/introducing-ltx-2-5 | Gemma 4, DFR, multishot |
| Film-foundation post | https://ltx.io/blog/the-foundation-film-is-made-on | Decoder / HDR ACES |
| Prompting blog index | https://ltx.io/blog-category/prompting | All official prompt essays |
| Hugging Face weights | https://huggingface.co/Lightricks/LTX-2.5 | Checkpoints |
| GitHub inference | https://github.com/Lightricks/LTX-2 | Pipelines, DFR, IC-LoRA |
| ComfyUI nodes | https://github.com/Lightricks/ComfyUI-LTXVideo | Official 2.5 workflows |
| Diffusers LTX-2.X | https://huggingface.co/docs/diffusers/api/pipelines/ltx2 | Prompt enhancement, multimodal CFG |
| I2V usage guide | https://docs.ltx.io/open-source-model/usage-guides/image-to-video | Motion-only official rule |
| LLM facts page | https://ltx.io/llm-info | Clean model card for agents |

### 23.2 Official — LTX Studio stills and shared prompt craft

| Resource | URL |
|---|---|
| AI image prompt guide | https://ltx.io/blog/ai-image-prompt-guide |
| How to write a prompt (video + image) | https://ltx.io/blog/how-to-write-a-prompt |
| JSON prompting | https://ltx.io/blog/json-prompting-for-video-image-generation |
| Negative prompts | https://ltx.io/blog/negative-prompts |
| Common video prompt mistakes | https://ltx.io/blog/common-prompt-mistakes-in-ai-video-generation |
| Domain-specific prompting | https://ltx.io/blog/domain-specific-prompting |
| Visualize ideas / Gen Space | https://ltx.io/blog/visualize-your-ideas-with-the-new-ai-image-generator |

### 23.3 Official — control adapters

| Resource | URL |
|---|---|
| IC-LoRA adapters | https://docs.ltx.io/open-source-model/integration-tools/ic-lo-ra-adapters |
| LoRA usage | https://docs.ltx.io/open-source-model/usage-guides/lo-ra |
| Motion control | https://docs.ltx.io/open-source-model/feature-guides/structural-control/motion-control |
| In/outpainting | https://docs.ltx.io/open-source-model/feature-guides/editing-effects/in-outpainting |
| How to use IC-LoRA | https://ltx.io/blog/how-to-use-ic-lora-in-ltx-2 |
| Dub-It weights | https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-DubIt |

### 23.4 Community guides and agent skills (learn + distill)

| Resource | URL | Use |
|---|---|---|
| Square-Zero LTX-2.5 prompting.md | https://raw.githubusercontent.com/Square-Zero-Labs/video-prompting-skill/main/video-prompting/references/models/ltx2-5/prompting.md | Tight agent reference |
| Square-Zero skill repo | https://github.com/Square-Zero-Labs/video-prompting-skill | Full video-prompting skill |
| benjiyaya LTX-2.5 skill | https://raw.githubusercontent.com/benjiyaya/LTX-2.5-Agent-Prompt-Skill/main/SKILL.md | 6-part enhancement skill |
| Ekly LTX-2 prompting | https://www.ekly.ai/guides/ltx-2-prompting | 7-step formula, settings table |
| ltx23.org prompt guide | https://ltx23.org/blog/ltx-2-5-prompt-guide | Camera lexicon + example gallery |
| Earngenix prompt fix | https://www.earngenix.com/tutorials/ltx-2-5-prompt-fix-comfyui | Symptom → fix, 4 modes |
| Earngenix ComfyUI ops | https://www.earngenix.com/workflows/ltx-2-5-comfyui | prompt_enhance, I2V pitfalls |
| tendre.ai good-prompt article | https://tendre.ai/en/articles/ltx-2-3-prompt-guide | “Don’t prompt like an image” |
| Mac local usage notes | https://github.com/james-see/ltx-video-mac/blob/main/docs/usage.md | Six ingredients + distilled limits |
| Comfy day-0 post | https://blog.comfy.org/p/ltx-25-day-0-support-in-comfyui | Official template names |
| Beginner livestream | https://www.youtube.com/watch?v=Sn6DlDnUz0s | LTX team prompting walkthrough |

### 23.5 Places to run the model

| Surface | URL |
|---|---|
| LTX site / Studio | https://ltx.io · https://ltx.io/studio |
| LTX API | https://api.ltx.io · https://docs.ltx.io |
| Hugging Face | https://huggingface.co/Lightricks/LTX-2.5 |
| ComfyUI templates | bundled with ComfyUI-LTXVideo 2.5 workflows |

---

## 24. Known limits (do not promise these)

- **On-screen text:** 2.5 is better than 2.3, still not a typesetting engine. Keep text short and large. Finish titles, labels, and logos in post.
- **Chaotic physics:** explosions, cloth pile-ups, multi-body collisions still artifact. Everyday motion (walk, turn, pour, dance) is reliable.
- **Exact spelling across frames:** not guaranteed.
- **Crowded direction:** many named characters + many cameras = averaged mush.
- **Retake / extend / reframe:** not exposed on 2.5 API endpoints at the time of this guide. Use I2V, Edit IC-LoRA, or a new generation.
- **Distilled negatives:** CFG 1 means classic negative prompts may be inert without NAG.
- **Auto duration + last frame:** incompatible. Pick one.
- **Enhancer:** helpful on empty briefs; it will invent if you already specified the shot.

---

## 25. One-page operator card

```
MODE → STRUCTURE → SETTINGS → ONE-VARIABLE ITERATE

T2V single:  4–8 sentence paragraph. Shot → scene → action → IDs → camera end-frame → audio.
T2V multi:   same paragraph + "A hard cut transitions to…" + re-ID + audio continuity. 2–4 shots.
I2V:         still owns look. Prompt owns motion/camera/audio only.
FLF2V:       prompt the path between two similar frames. Fixed duration.
Still:       Subject → Style → Comp → Light → Palette → Technical.
Dub-It:      [Speaker] is speaking [lang], saying: "…"
Edit LoRA:   [new state]. Preserve [everything else].

OUTSIDE PROMPT: duration / res / fps / CFG / steps / model / 8k
AUTO DURATION:  duration: null
ENHANCER:       on if rough, off if this guide was followed
NEGATIVE:       5–15 tokens, five buckets, no contradictions
IDENTITY:       still first, then identical visual ID strings
CAMERA:         named move + intensity + ending frame (or write "static")
AUDIO:          room tone + caused SFX + quoted speech
EMOTION:        body only
LANGUAGE:       English for the shot; native script inside quotes for speech
```

---

*Compiled 2026-09-15 from Lightricks official LTX-2.5 / LTX Studio documentation and public operator guides. Settings drift as hosted APIs and Comfy templates update — treat section 16 numbers as starting points and re-check [docs.ltx.io/models/ltx-2-5](https://docs.ltx.io/models/ltx-2-5) before a production run.*
