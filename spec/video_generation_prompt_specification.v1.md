# Video Generation Prompt Specification v1

**Document ID:** `video_generation_prompt_specification.v1`  
**Version:** 1.0.0  
**Status:** Specification / production handbook  
**Date:** 2026-09-14  
**Scope:** Common prompt structures across commercial video models, open-source frameworks, and LLM prompt-compilers. Visual, audio, consistency, camera, background, and runtime settings. Software provenance. Prompt-setting types. Sample ladder from a 2-second micro-clip to a feature-length production bible.

This is a **unified specification**. Store meaning in a portable object; compile that object into each product’s dialect. Do not mix dialects in one generation call.

---

## 0. How to use this document

1. Author a clip as a **canonical prompt object** (Section 7).
2. Compile it into the **vendor dialect** of the model you will run (Section 5).
3. Attach **runtime settings** the model exposes as API/UI knobs (duration, aspect, seed, first frame, audio on/off).
4. For anything longer than one model clip (typically 4–15 seconds), use the **long-form pipeline** (Section 9). Do not ask one prompt to be a movie.

| Need | Section |
|---|---|
| Why video prompts look like shot lists | 1 |
| What each product accepts | 2 |
| Shared anatomy | 3 |
| Field values (visual / audio / consistency / camera / background) | 4 |
| Official formulas and provenance | 5 |
| Prompt setting types | 6 |
| Portable schema | 7 |
| Samples, micro to feature | 8 |
| Long movie pipeline | 9 |
| LLM compiler contract | 10 |
| Anti-patterns | 11 |

---

## 1. Background and history

### 1.1 What a video prompt is

An image prompt describes a frozen frame. A video prompt describes a **shot**: what is in frame at t0, what changes, how the camera observes it, what it sounds like, and what must stay the same.

Background is not decoration. It is a first-class layer (foreground / midground / background, weather, architecture, practical lights, crowd, signage, reflections). Unspecified backgrounds are the main source of location drift across shots.

### 1.2 Three generations of grammar

| Gen | Years | Mental model | Audio | Consistency |
|---|---|---|---|---|
| G0 Caption | 2022-2024 | Describe the picture; hope it moves | None / post | Seed only |
| G1 Shot brief | 2024-2025 | Subject + action + camera + look | Rare / TTS | First frame, seed, LoRA |
| G2 Directed sequence | 2025-2026 | Timed beats + dialogue + named refs + multi-shot | Native, layered | Elements, @refs, first/last, ingredients, Soul ID |

### 1.3 Timeline

| Period | Systems | What changed |
|---|---|---|
| 2022-2023 | Make-A-Video, Imagen Video, Phenaki, Tune-A-Video, Runway Gen-1/2, SVD, AnimateDiff | Seconds-long clips; morphing; no audio; SVD motion is motion_bucket_id |
| 2024 | Sora demo, Veo 1, Kling 1.x, Runway Gen-3, Luma Dream Machine, CogVideoX, HunyuanVideo | Cinematographer language: shot size, dolly, lighting, beats |
| 2025 | Veo 3 native AV, Sora 2 API, Kling 2/3, Seedance 1-2, Wan 2.5-2.7, Midjourney Video V1, Firefly Video, Hailuo 02 | Dialogue / SFX / ambience / music become prompt fields; first/last and refs become standard |
| 2026 | Veo 3.1, Kling 3.0/Omni, Seedance 2.5, Wan 2.7/3.0, Grok Imagine 1.5, LTX 2.5, Higgsfield Soul+DoP | Multi-shot grammar, @Image/@Video/@Audio binding, 4K + 15 s class, storyboard-first long-form pipelines |

**Sora status:** Consumer app shutdown reported 2026-04-26; several developer notes schedule Sora 2 API retirement around 2026-09-24. The dialect is documented as a compile target, not a guaranteed live endpoint.

### 1.4 Why dialects exist

- Autoregressive multimodal models (Sora 2, Grok Imagine / Aurora, parts of Veo) prefer storyboard prose.
- DiT / flow models (Wan, Hunyuan, CogVideoX, Mochi, LTX, SVD, AnimateDiff) split meaning into text + numeric graph fields.
- I2V-first products (Runway Gen-4, Midjourney V1) treat the image as the picture; text is change.
- V2V editors (Runway Aleph, Wan edit) want transformation verbs.
- Reference-heavy products (Seedance 2.5, Kling Elements, Veo ingredients, Higgsfield Soul) need named bindings with a job sentence.

### 1.5 Hard production limits

- Single-generation length is usually 4-15 seconds (outliers: some Seedance modes 15-30 s or longer; Luma extend toward 30 s; Higgsfield Cinema marketing 15-60 s).
- Multi-shot inside one generation (Kling 3 ~6 cuts, Veo timestamps, Wan Shot N, Seedance stages) is still a short scene, not an act.
- Identity persists better inside a clip than across clips.
- Always-on audio models invent score or captions if you do not specify silence / no text.
- Readable on-screen text is unreliable. Generate type in post (Remotion, CapCut, After Effects).
- No current model generates a coherent feature film in one prompt.

---
## 2. Software and framework map (provenance)

Limits move. Treat live vendor docs as source of truth for numbers.

### 2.1 Commercial flagship models

| System | Vendor / origin | Modes | Official / de-facto structure | Audio | Consistency | Typical limits |
|---|---|---|---|---|---|---|
| **Veo 3 / 3.1** | Google DeepMind; Gemini API; Vertex / Flow | T2V, I2V, ingredients-to-video (up to 3 refs), first+last, extend | `[Cinematography]+[Subject]+[Action]+[Context]+[Style & Ambiance]` | Always-on: quotes for speech; `SFX:`; `Ambient noise:` | Ingredient images; first/last; timestamped beats | 4/6/8 s; 720p/1080p/4K; 16:9 or 9:16 |
| **Sora 2 / 2 Pro** | OpenAI Cookbook + Videos API | T2V, input_reference, extend, edit | Prose + Cinematography / Actions / Dialogue blocks | Dialogue and diegetic sound in prompt | Distinctive anchors; one reference image | API seconds 4/8/12; prompt very long |
| **Runway Gen-3 / Gen-4 / 4.5 / Aleph** | Runway ML | I2V primary (Gen-4 image required), keyframes, Act-One, Aleph V2V | Motion-first. I2V must not re-describe the still. Aleph = verb + only the change | Generally post | Character refs; last-frame chaining; positive phrasing only | ~5-10 s; Gen-4 prompt ~1000 chars |
| **Kling 2.1-2.6 / 3.0 / Omni / O1** | Kuaishou | T2V, I2V, Elements, first/last, multi-shot, avatar | Subject + Movement + Scene + (Camera + Lighting + Atmosphere) | 2.6+ native; 3.0 dialogue + dialects + lip-sync | Elements @name; [Character A:]; @VoiceName | 3-15 s on 3.0; up to ~6 shots; prompt ~2.5-3k chars |
| **Seedance 2.0 / 2.5** | ByteDance (Jimeng / Dreamina / CapCut / BytePlus) | T2V, I2V, R2V, extend, timestamp edit | Subject + Action + Scene + Style + Camera + Audio | Native. `(music)` `<sfx>` `{dialogue}` `【subtitles】` | @Image N / @Video N / @Audio N with role; 2.5 up to 30/10/10 | ~4-30 s; ultra-long modes reported |
| **Wan 2.5 / 2.6 / 2.7 / 3.0** | Alibaba Cloud Model Studio | T2V, I2V, kf2v, R2V, edit, extend | Basic Entity+Scene+Motion. Advanced + aesthetic. Multi-shot Overall + Shot N [t0-t1] | Native from 2.5+; strong lip-sync on 2.7 | 图n / Image N media[]; negative_prompt | 2-15 s class; prompt thousands of chars |
| **Grok Imagine Video 1.5** | xAI (Aurora) | T2V, I2V, R2V, first/last, edit, extend | Subject + motion + camera + env + Sound: | Native SFX/ambience/dialogue | 1-7 refs; I2V first frame; last frame | ~1-15 s; 480p-1080p class |
| **Luma Ray 2 / later Ray** | Luma Labs | T2V, I2V, keyframes, loop, extend | NL + Camera Motion / Angle Concepts | SFX stronger than speech | frame0/frame1; concepts compose | 5-10 s; extend toward ~30 s |
| **Pika 2.2 / 2.5** | Pika Labs | T2V, I2V, Pikaffects, Pikaframes, Pikaformance | Short scene + effect + camera | Core silent; Pikaformance = lipsync | Ingredients; first/last; negatives OK | 5/10 s; frames path 10-25 s |
| **Hailuo 02 / 2.3 / H3** | MiniMax | T2V, I2V, first+last (02), subject-ref | Prose + [camera command] tokens; H3 timeline | H3 native; older often silent | First/last; S2V subject ref | 5/6/10 s; API prompt <=2000 chars |
| **Adobe Firefly Video** | Adobe | T2V, I2V, first/last, composition-ref, partner models | Shot Type + Character + Action + Location + Aesthetic | Partner-dependent | Elements; first/last; <=5 shots | Often 5 s / 24 fps |
| **Midjourney Video V1** | Midjourney | I2V / Animate; extend; loop; --end | Motion sentence + `--motion low\|high` `--raw` `--loop` `--end` `--bs` | No | Start + end frames | ~4-5 s + extend ~4 s x 4 |
| **PixVerse / Vidu** | PixVerse; Shengshu | T2V, I2V, R2V, effects | Short cinematic + refs | Versioned | First/last; multi-ref | Short + extend |
| **Higgsfield Soul / DoP / Cinema** | Higgsfield | I2V, Soul ID, named presets | MCSLA: Model, Camera, Subject, Look, Action | Routed-model dependent | Soul ID | 15 s / 60 s Cinema reported |
| **HeyGen-class / Viggle-class** | Various | Avatar+script; image+driver video | Performance + line; text secondary on Viggle | Voice driven / usually none | Avatar ID / driver motion | Minutes via assembly |

### 2.2 Open-source models and frameworks

| System | Origin | Prompt / param shape | Notes |
|---|---|---|---|
| **HunyuanVideo 1.5** | Tencent | Subject + Motion + Scene + [Shot] + [Cam] + [Lighting] + [Style] + [Atmosphere]. I2V = subject motion + scene motion + camera | Official camera library. LLM rewrite Normal vs Director |
| **Wan 2.1 / 2.2 open weights** | Alibaba | Entity+Scene+Motion; ComfyUI graphs | Frames often 4n+1 (81/121/161). cfg, seed, flow-shift, camera embed |
| **CogVideoX** | Zhipu / Tsinghua | Camera language + subject + movement + scene + atmosphere. Long captions | T2V + I2V. guidance, num_frames, seed, LoRA |
| **LTX-Video / LTX 2.x** | Lightricks | Single flowing paragraph; I2V = motion only; quotes for dialogue | Frames 1+8n. generate_audio on later API |
| **Mochi 1** | Genmo | Free prose + physics | Frames 7+6n. 848x480 class |
| **SVD / SVD-XT** | Stability | Text is weak | motion_bucket_id 1-255, fps_id, noise aug. Frames 14/25 |
| **AnimateDiff** | SD ecosystem | Image prompt + motion LoRA; optional per-range schedule | IP-Adapter / InstantID / PuLID for faces |
| **Open-Sora, Step-Video, Cosmos, Pyramid Flow, DynamiCrafter, FramePack** | Various | Long recaption or I2V dual condition; FramePack FLF2V | ComfyUI citizens: frames/cfg/seed |
| **ComfyUI** | Comfy-Org | Graph runtime | Prompt split across CLIP, ControlNet, LoRA, first/last nodes |
| **Remotion** | Code | React tree + timing | Titles and assembly after generative plates |

### 2.3 LLM compilers

These emit vendor prompts; they do not render pixels.

| Tool / pattern | Job |
|---|---|
| Hunyuan rewrite (Normal / Director) | Expand short intent into model-preferred cinematic prose |
| Gemini / Qwen / GPT / Grok / Claude as DoP | Shot-list a script; render dialects; freeze bibles |
| Vendor skills (Kling, Seedance, Veo) | Encode brackets, @ refs, camera tokens |
| PenShot / storyboard-first agents | Screenplay to duration-matched fragments |
| CapCut / Jimeng templates | Consumer UI over Seedance-class models |

### 2.4 Official documentation anchors

- DeepMind Veo prompt guide: https://deepmind.google/models/veo/prompt-guide/
- Google Cloud Veo 3.1 ultimate prompting guide (2025-10-16): https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- OpenAI Sora 2 Cookbook + Videos API POST /videos
- Runway Gen-4 Video Prompting Guide; Aleph 2.0 Prompting Guide
- Kling Text-to-Video prompt guide; 2.6 audio user guide; 3.0 capability map
- BytePlus / Seedance 2.x prompt guides; Seed 2.5 launch posts
- Alibaba Cloud Model Studio Wan text-to-video prompt guide
- HunyuanVideo 1.5 Prompt Handbook EN (GitHub)
- MiniMax Open Platform Hailuo camera-command + first/last docs
- Luma Dream Machine video API + Camera Motion/Angle Concepts
- Adobe Firefly Writing effective text prompts for video generation
- Midjourney video parameter docs
- xAI Imagine Video / I2V / R2V docs
- ComfyUI Wan 2.2 + WanCameraImageToVideo node docs

---

## 3. Universal prompt anatomy

```
0  META         mode, model, duration, fps, aspect, seed, audio on/off
1  INTENT       logline / purpose of this shot
2  VISUAL       subject, wardrobe, set, light, grade
3  MOTION       subject action beats + physics + timing
4  CAMERA       size, angle, lens, move, start/end framing
5  AUDIO        dialogue, SFX, ambience, music, silence
6  CONSISTENCY  ids, refs, retain/forbid, negatives
```

Vendor order is not portable. Veo puts cinematography first. Kling puts subject first. Sora puts prose first. Runway Gen-4 puts motion first. Seedance is subject, action, scene, style, camera, audio. Store named fields; reorder on emit.

Separate three clocks:

1. Subject motion (body, cloth, hair, face, prop)
2. Camera motion (the rig)
3. Editorial motion (cuts) — only in multi-shot modes

---
## 4. Field catalog

### 4.1 Runtime / meta

| Field | Values | Notes |
|---|---|---|
| mode | t2v, i2v, fl2v, r2v, v2v, extend, edit, loop, avatar | Changes what the text may contain |
| duration_s | 2, 4, 5, 6, 8, 10, 12, 15, 30 | Do not ask a 5 s model for three locations |
| fps | 8, 16, 24, 25, 30, 60 | |
| num_frames | Wan 4n+1; Mochi 7+6n; LTX 1+8n; SVD 14/25 | duration ≈ frames/fps |
| aspect_ratio | 16:9, 9:16, 1:1, 4:3, 2.39:1, 4:5 | |
| resolution | 480p, 720p, 1080p, 4K | |
| seed | int | Not portable across models |
| cfg / guidance | ~4-12; some Kling scales 0-1 | |
| generate_audio | bool | Default on for Veo 3.x, Seedance 2.x, Sora 2, Kling 2.6+ |
| negative_prompt | string | OSS + Pika + Wan. Not on Runway Gen-4 |
| motion_bucket_id | SVD 1-255 | Text-weak I2V control |
| loop | bool | Luma, MJ --loop |
| prompt_optimizer / prompt_extend | bool | Disable when syntax is locked |

### 4.2 Subject (visual)

Use 2-3 distinctive face anchors (Kling two-details rule). Extra adjectives compete and drift. Wardrobe = garment + color + material + wear. Material words improve physics. Exact object counts are unreliable.

### 4.3 Background (first-class)

Specify: location, time of day, weather, architecture/period, FG / MG / BG layers, practical lights, crowd density, signage policy (no readable text unless a short string is the point), reflections, geography lock ("same alley as SHOT_014"). Empty infinity coves are valid product backgrounds — say them.

### 4.4 Lighting / look

Write source + direction + quality + color temperature + contrast. Weak: cinematic lighting. Strong: single window camera-left, soft 5600K, warm 2700K desk lamp fill.

Look axes: capture medium (16mm / 35mm / clean digital / VHS), lens (24/35/50/85), DoF, grade (neutral, Portra, restrained teal-orange, bleach-bypass, anime cel, ink-wash), art style (photoreal, documentary, stop-motion, 2D, 3D, xieyi).

### 4.5 Motion

Ordered verb-first beats that fit duration_s. Include start_state / end_state for I2V and FL2V. Speech budget ≈ 2-2.5 words per second of clip.

### 4.6 Camera

Size: ECU, CU, MCU, MS, MLS/cowboy, WS, EWS, two-shot, OTS, insert, establishing, POV, aerial, overhead, ground-level.  
Angle: eye-level, low, high, bird's-eye, worm's-eye, Dutch (rare), 3/4, profile.  
Moves: locked-off; dolly in/out; tracking/truck; pan; tilt; pedestal/crane; orbit/arc; zoom (not the same as dolly); handheld; steadicam; FPV; whip pan.

One primary move per shot.

Hailuo official tokens (embed in prompt):

`[Truck left]` `[Truck right]` `[Pan left]` `[Pan right]` `[Push in]` `[Pull out]` `[Pedestal up]` `[Pedestal down]` `[Tilt up]` `[Tilt down]` `[Zoom in]` `[Zoom out]` `[Shake]` `[Tracking shot]` `[Static shot]`

Combine at most 3 inside one bracket: `[Pan left, Pedestal up]`. Sequence with prose.

Luma also accepts API concepts: `[{ "key": "dolly_zoom" }]`.

### 4.7 Audio (four buses)

| Bus | How to write |
|---|---|
| Dialogue | Speaker + delivery + exact words in quotes. Who is not speaking |
| SFX | Object + material + action + optional timestamp |
| Ambience | Continuous bed + distance (near/mid/far) |
| Music | Style, in/out — or no music |
| Silence | Explicit on always-on models |

Dialect syntax:

- Veo: `A woman says, "We have to leave now."` / `SFX:` / `Ambient noise:`
- Sora: Dialogue block
- Seedance: `(low cello)` `<door latch>` `{We should go.}` `【Chapter One】`
- Kling 3: `[Detective Li @Mr. Wang’s voice] demands, "Where is the evidence?"`
- Grok Imagine: `Sound:` paragraph with spatial/material nouns
- Wan 2.7+: dialogue + BGM in prose
- Most open DiTs: no audio; plan a second pass

### 4.8 Consistency

| Mechanism | Who |
|---|---|
| First frame / I2V | Almost everyone |
| Last frame / FL2V | Hailuo 02, Kling, Veo 3.1, Pika 2.2, Grok 1.5, some Wan |
| Extend | Sora, Luma, MJ, Seedance, Vidu, Kling, Veo |
| Seed | Runway, Wan, Pika, graphs |
| Ingredient / R2V images | Veo <=3; Seedance <=30; Grok 1-7; Kling Elements; Wan media[] |
| Named elements / tags | Kling [Character A], Firefly Elements, Seedance @Image N |
| Soul ID / LoRA / IP-Adapter / InstantID | Higgsfield; ComfyUI |
| Motion transfer | Runway Act-One, Wan Animate, Viggle |
| Verbatim look sheet | All models |

Binding rule: assign a job.

```
@Image 1 provides CHAR.LIN face and hair only.
@Video 1 provides camera path only; ignore its actor and wardrobe.
@Audio 1 provides tempo only; do not copy lyrics or timbre.
```

---

## 5. Official formulas (provenance)

**Veo 3.1 (Google Cloud, 2025-10-16):** `[Cinematography]+[Subject]+[Action]+[Context]+[Style & Ambiance]`

**Sora 2 (OpenAI Cookbook, 2025-10):** prose scene + Cinematography / Actions / Dialogue. API: prompt, input_reference, seconds in {4,8,12}, model sora-2 or sora-2-pro.

**Kling (official T2V guide):** Subject + Subject Movement + Scene + (Camera + Lighting + Atmosphere). 3.0 adds Shot 1/2 and character/voice tags.

**Seedance 2.5 (ByteDance official six-part):** Subject + Action + Scene + Style + Camera + Audio plus @ role binding and audio brackets.

**HunyuanVideo 1.5 handbook:** T2V Subject+Motion+Scene+[Shot]+[Cam]+[Lighting]+[Style]+[Atmosphere]. I2V subject motion + scene motion + camera.

**Wan (Alibaba Model Studio):** Basic 主体+场景+运动. Advanced + 美学 + 风格化. Multi-shot: 总体 + 镜头N + 时间戳.

**Hailuo (MiniMax API):** prose + [command] tokens. FL2V describes the journey A to B.

**Runway Gen-4:** motion-only on a required image; no negatives. Aleph: Change X. Keep everything else identical.

**Firefly:** Shot Type + Character + Action + Location + Aesthetic

**CogVideoX:** (Camera + Angle + Lighting) + Subject + Movement + Scene + Atmosphere

**LTX:** one chronological paragraph; start with the action.

**Midjourney V1:** motion sentence + --motion --raw --loop --end.

**Grok Imagine 1.5:** shot brief + Sound:; I2V does not restate the still.

**SVD:** set motion_bucket_id, not an essay.

---

## 6. Types of video generation prompt settings

| ID | Type | When | What you write |
|---|---|---|---|
| T1 | Micro caption | Tests, B-roll | 3-12 words |
| T2 | Five-box shot card | Portable default | Subject / action / env / camera / style |
| T3 | Director prose | Veo, Sora, LTX | One or two dense paragraphs |
| T4 | Labeled blocks | Sora Cookbook, bibles | Cinematography / Actions / Dialogue / Audio |
| T5 | Timestamp screenplay | Veo, Wan, Hailuo H3 | [00:00-00:02] blocks |
| T6 | Multi-shot master | Kling, Seedance, Wan | Shot N + seconds + content |
| T7 | I2V motion delta | Any I2V | Preserve + one action + one camera |
| T8 | First-last interpolation | Veo FLF, Luma, Pikaframes, Hailuo-02 | Start, path, end |
| T9 | Reference-to-video | Seedance, Grok R2V, Veo ingredients | Role-mapped assets + new action |
| T10 | Talking head | Veo CU, Wan lip-sync, HeyGen, Pikaformance | Face-front + exact line + no music |
| T11 | Product / orbit | Ads | Locked subject, one move, foley |
| T12 | Physics plate | Hailuo, Luma | Materials + collisions + one camera |
| T13 | Parameter dialect | MJ, SVD, Pika legacy | Flags and numbers dominate |
| T14 | Negative-heavy OSS | Wan, Hunyuan, Comfy | Twin pos/neg prompts |
| T15 | YAML canonical | Agents, SDD, batch | Section 7 object |
| T16 | LLM-compiler brief | Pre-step | Intent + target + duration + refs |
| T17 | Loop / ambient | MJ --loop, Luma loop | End = start, low motion |
| T18 | Extend / continue | Veo, Sora, Seedance, Grok | What happens next |
| T19 | V2V edit | Aleph, Wan edit | Change X, keep Z |
| T20 | Sequence packet | 30 s-12 min | Shared bibles + N compiled shots |
| T21 | Feature packet | 70-120 min | Acts, scenes, continuity ledger |
| T22 | Code-native | Remotion | Components + frames |
| T23 | Background plate only | Establishing, VFX | No hero face; layered env |
| T24 | Performance transfer | Act-One, Viggle, Wan Animate | Driver video + identity image |

---

## 7. Canonical specification (portable object)

```yaml
schema: video_generation_prompt_specification.v1
shot_id: SHOT_014
setting: T15
target:
  model: veo-3.1
  mode: r2v
  duration_s: 8
  fps: 24
  aspect_ratio: "16:9"
  resolution: "1080p"
  seed: null
  generate_audio: true
  enhance_prompt: false
intent:
  logline: "Lin finds the unopened letter and decides not to read it yet."
  emotion: "quiet resolve"
visual:
  subjects:
    - id: CHAR.LIN
      lock: "late-20s East Asian woman, short black hair with a silver streak at the temple, navy linen shirt, faint scar at left brow"
      wardrobe_lock: "navy linen shirt, small gold studs"
      expression_arc: "tired to still to a single contained breath"
  environment:
    location: "third-floor kitchen, old Hong Kong walk-up"
    time_of_day: "blue hour"
    weather: "light rain on the window"
    layers:
      fg: ["envelope in hands", "tile edge"]
      mg: ["sink", "rice cooker LED"]
      bg: ["wet glass", "neon smear from the street"]
    set_dressing: ["yellow crate with tangerines"]
  lighting:
    key: "window camera-left, cool rain light ~6500K"
    fill: "warm rice-cooker LED 2700K, very low"
    style: "low-key, naturalistic"
  look:
    medium: "35mm spherical, faint grain"
    lens_mm: 50
    dof: "shallow"
    grade: "cold shadows, intact skin tones"
motion:
  cuts: none
  beats:
    - { t: "0-3s", action: "stands at the sink, unopened envelope in both hands" }
    - { t: "3-6s", action: "turns the envelope over once, does not open it" }
    - { t: "6-8s", action: "sets it on the tile, palm resting on it" }
  start_state: "envelope held at waist"
  end_state: "envelope on the counter, hand covering it"
camera:
  size: "MCU into CU"
  angle: "eye-level, 3/4 toward window"
  move: "slow push-in"
audio:
  dialogue: []
  sfx: ["paper flex", "soft tile tap", "rain on glass"]
  ambience: "distant tram bell, muffled TV, fridge hum"
  music: "none"
  mix_note: "foley in front; street distant"
consistency:
  references:
    - { handle: "@Image1", role: "CHAR.LIN face and hair only" }
    - { handle: "@Image2", role: "kitchen geography and tile color" }
  retain: ["silver streak", "navy linen", "yellow crate"]
  forbid: ["on-screen text", "extra people", "jump cuts"]
  negative_prompt: "subtitles, watermark, extra fingers, warped face"
```

Sequence object: shared look_sheet + shots[] + transitions.  
Feature object: world rules, cast bible, location bible, look/sound bibles, act map, coverage policy, continuity ledger.

Compiler rules: drop illegal fields; reorder to vendor formula; bind refs with jobs; collapse lists for Pika/MJ; expand timestamps for Veo/Wan/Seedance; convert camera to Hailuo tokens; convert audio to Seedance brackets; I2V deletes appearance already in pixels; invert forbids to positive phrasing for Runway; SVD mostly ignores text.

---
## 8. Sample library

Each sample lists setting type, duration, intended models, then the prompt. Original characters only.

### S01 — Micro caption (T1), 3-5 s, any T2V

```
A red paper lantern sways in night rain.
```

### S02 — One-liner with camera (T2), 4-6 s

```
Close-up of dark coffee poured into a white ceramic cup, steam rising, morning window light, slow push-in, shallow depth of field, no music, soft pour sound.
```

### S03 — Product hero (T11), 6 s

```
Locked camera, 50mm, product tabletop. A frosted glass serum bottle stands on wet black stone.
A single drop slides down the bottle and joins a shallow puddle.
Softbox key from upper left, rim light from behind, dark studio void in the background.
SFX: quiet droplet tick. No music. No labels readable. No hands.
```

### S04 — Weak vs strong

Weak: `A cool woman walking in the rain, dramatic, cinematic`

Strong:

```
Medium-wide shot of a woman in her 30s in a long red wool coat crossing a rain-slicked city street at night.
She walks left to right at a steady pace, coat hem heavy with water, one hand in a pocket.
Background: wet asphalt, zebra crosswalk, neon signs reflected in puddles, two parked taxis, steam from a subway grate in the foreground.
Camera: slow dolly backward keeping her centered, 35mm anamorphic, shallow DOF.
Lighting: hard backlight from a sodium streetlamp, magenta spill from a pharmacy sign camera-right.
Audio: rain on fabric, distant tires on wet road, no music, no subtitles.
Duration: 8 seconds.
```

### S05 — Veo 3.1 five-part + audio (T3), 8 s

```
Camera: Medium close-up tracking shot from her right side, 35mm lens, slight handheld feel.
Subject: A woman in her early 30s, wet black bob stuck to her cheek, camel trench cinched at the waist, faint scar at the left brow.
Action: She walks through standing water, then stops, looks up at a second-floor window, and says, "未到时候。"
Context: A narrow Hong Kong alley at night, rain falling through neon, dripping air-conditioner boxes, plastic stools in the foreground, crossing umbrellas in the background. No readable shop names.
Style and Ambiance: Photoreal, cool teal pavement with warm sodium practicals, fine grain.
Ambient noise: rain on canvas awnings, AC drip, far traffic.
SFX: a shoe splash on the first step.
No music. No burned-in subtitles.
```

### S06 — Veo timestamp play-by-play (T5), 8 s

Pattern from Google Cloud Veo 3.1 timestamp guide.

```
[00:00-00:02] Medium shot from behind a young explorer with a leather satchel as she pushes aside a jungle vine.
[00:02-00:04] Reverse on her freckled face, awe. SFX: leaf rustle, distant birds.
[00:04-00:06] Tracking shot, she runs a hand over carved stone. Emotion: reverence.
[00:06-00:08] Wide high-angle crane: she is small in a temple court swallowed by jungle. SFX: a gentle orchestral swell begins.
```

### S07 — Sora 2 block template (T4), 8 s

```
A small recording booth, worn grey foam. A young man in headphones leans into a large condenser mic.

Cinematography:
Camera shot: MCU, slight low angle
Mood: late-night focus

Actions:
- He inhales
- He delivers the line without smiling
- His hand rides the volume fader down

Dialogue:
HOST: "Stay until the rain stops."

Background sound: preamp hiss, rain on the building, no music.
```

### S08 to S12 — Same rain-alley shot, multiple dialects

Intent: 8 s, 16:9, woman under a clear umbrella, Mong Kok rain, slow push-in, one Cantonese line.

Veo:

```
Medium close-up, slow push-in, a woman in her late 20s in a black trench and clear umbrella, neon magenta and teal reflecting in puddles on a crowded Hong Kong night street. She looks past camera and says, "落雨都要行完呢段路。"
SFX: rain on plastic umbrella, bus hiss.
Ambient noise: wet-tyre wash.
No music. Background: signage glow, steam from a dai pai dong, one taxi left to right.
```

Sora:

```
Night, rain-slick Mong Kok. A woman in a black trench and a clear umbrella.

Cinematography:
Camera shot: MCU, eye level, 35mm, shallow DOF, slow push-in
Mood: tired, unsentimental

Actions:
- she blinks rain off her lashes
- a taxi passes behind her left to right
- she speaks

Dialogue:
WOMAN: "落雨都要行完呢段路。"

Audio: rain on umbrella, bus air-brake, no score.
```

Kling:

```
Master: 35mm night documentary, wet Mong Kok, woman black trench, clear umbrella, magenta-teal neon.
Shot 1 (0-4s): MCU then slow push-in, rain on umbrella.
Shot 2 (4-8s): she looks past camera.
[Woman: quiet tired Cantonese]: "落雨都要行完呢段路。"
Audio: rain, bus air-brake, no music.
```

Seedance:

```
@Image1 is her face and trench only.
Night Mong Kok rain. Slow push-in MCU.
She says "落雨都要行完呢段路。"
<rain on umbrella> (no music)
Keep face, hair, coat identical. Background: neon puddles, one taxi L to R.
```

Runway I2V:

```
The camera slowly pushes in as the subject blinks rain off her lashes and speaks. A taxi slides left to right in the background. Rain ticks on the umbrella. Locked framing besides the push-in.
```

Grok Imagine:

```
Slow push-in, MCU, 35mm. She blinks rain off her lashes and speaks.
Sound: rain hitting the umbrella canopy, one bus air-brake, wet tyres mid-distance, no music, no laugh track.
```

Wan:

```
主体：黑风衣女子，透明伞。场景：旺角夜雨，品红与青绿霓虹倒影。运动：慢推进。
镜头1 [0-4s] 中近景，雨打伞面。
镜头2 [4-8s] 她望向镜头外，说「落雨都要行完呢段路。」
背景音乐：无。环境声：雨、巴士气刹。图1作为面容与风衣。
```

### S13 — I2V preserve identity (T7), 5 s

```
Keep face, hair, and navy linen identical to the first frame. She turns the envelope over once and sets it on the tile. Slow push-in. Rain continues on the glass. No new objects, no cuts.
```

### S14 — First-last wuxia (T8), 8 s

```
Preserve face, hair knot, charcoal linen robe with rust collar thread, and the guan dao silhouette from @Image1.
Start: she stands on wet courtyard flagstones under moonlight, blade tip down.
Then she inhales, shifts weight to the rear foot, and launches a single upward slash; rain needles streak through lantern light; robe hem snaps.
End on the mid-air pose matching @Image2.
Camera: low-angle tracking, one move, follows the blade arc.
Background: Ming-style courtyard, wet stone, two red lanterns, distant tiled roofs, no extra people.
Audio: rain on tile, one cloth snap, steel through air, no music, no speech.
```

Labeled wuxia variant:

```
Subject lock: LIN QIU — late-20s East Asian woman, ink-black hair in a low knot, charcoal linen robe with rust thread at the collar, faint scar at the left brow.
Action: She draws a weathered guan dao in one continuous arc, rain beads flying off the blade, then settles into a low horse stance.
Background: Ming-style courtyard at night; wet flagstones (FG); paper lanterns and a mossy stone lion (MG); tiled roofs and a distant city wall (BG); light rain.
Camera: Low-angle medium-wide, 35mm anamorphic, slow orbit left, shallow DOF. One move only.
Lighting: Cool moonlight key from above-right, warm lantern fill, wet-stone speculars.
Audio: Rain on tile, steel whisper of the draw, distant thunder; no music; no extra voices.
Style: Wuxia ink-realism, 24fps film grain.
Constraints: same face and robe throughout; no readable signage; no extra fighters.
```

### S15 — Hailuo physics + token (T12), 6 s

```
[Push in] A ceramic teapot releases a thin ribbon of steam on a walnut table, soft morning window light, one continuous product shot, no cuts.
```

### S16 — Talking head (T10), 8 s

```
Duration 8s. Presenter from the supplied front-facing photo, same charcoal sweater. Looks at lens, small nod, then:
"Three things changed in video prompts in 2026: sound, references, and multi-shot grammar."
Delivery: even, slightly dry. Background: soft grey sweep. No music. Shoulders still; blink naturally.
```

### S17 — Documentary interview (T4), 8 s

```
Medium shot, eye-level, 50mm, available window light camera-left. A middle-aged tram inspector in a worn uniform jacket sits in a depot canteen and says, "The last car is always the quietest."
Ambient noise: fluorescent buzz, distant metal wheels.
SFX: ceramic cup set down after the line.
No music. No extra patrons in focus.
```

### S18 — Anime continuity, three shots (T20), 3x5 s

Shared lock: CHAR.AOI — teen, short indigo hair with one long side-lock, school coat too big, scuffed white sneakers. Style: 2D evening anime, soft cel shade, no 3D shine.

```
Shot A: WS rooftop water tanks, city haze, Aoi sits on the ledge, kicks one sneaker. Locked camera.
Shot B: CU side-lock lifts in wind. Slow push-in.
Shot C: MS she stands and picks up a kraft envelope. Same coat, same hair.
Audio all shots: wind, far train, no score, no speech.
```

### S19 — ASMR / sleep B-roll (T17), 8 s, 9:16

```
Extreme close-up of dry tea leaves dropping into a porcelain gaiwan. Static macro, overhead soft daylight. No faces, no text.
Sound: dry leaves, porcelain tick. No music. Seamless enough to loop.
```

### S20 — Establishing background plate (T23), 8 s

```
Locked wide. Foreground: wet railing beads. Midground: one empty tram sliding right to left. Background: stacked neon, rain curtain, no landmark postcard angle. Night, overcast, 35mm, deep focus.
Sound: rail hiss, rain, far horns. No music, no readable shop names, no hero face.
```

### S21 — Veo office example pattern (T3)

```
Medium shot, a tired office worker, rubbing his temples, in front of a bulky 1980s computer in a cluttered office late at night. Harsh fluorescent overhead lights and the green glow of a monochrome monitor. Retro aesthetic, as if shot on 1980s color film, slightly grainy.
Ambient noise: transformer buzz, distant elevator.
SFX: chair creak.
```

### S22 — Seedance ceramicist six-part (T9)

```
A ceramicist in a linen apron lifts a finished bowl from the wheel and turns it slowly in the light, in a cluttered studio at golden hour with clay dust in the air, warm 35mm film look with soft halation, slow push in that settles on her hands, (sparse piano) <wheel slowing, clay scraping>
```

### S23 — Seedance ref exclusions (T9)

```
@Image 1 defines the cream stone facade and window rhythm. Do not use its sky or the parked cars.
@Image 2 defines the courier's face and hair only. Do not use her clothing or the background.
@Video 1 defines the camera rhythm: one slow lateral track, no cuts.
```

### S24 — Midjourney video (T13), ~5 s

```
fog slides between the pines, a single crow crosses left to right, camera locked --motion low --raw
```

### S25 — SVD parameter setting (T13)

Image of waves. motion_bucket_id: 80, fps_id: 7, light noise aug. Text optional: ocean swell.

### S26 — AnimateDiff schedule (T13)

```
0-8: steam only, locked kettle
8-16: hand enters frame left, lifts lid
16-24: steam blooms, hand exits
```

Plus motion LoRA. Keep IP-Adapter face off if no character.

### S27 — Aleph edit (T19)

```
Re-light this scene as blue hour. Keep wardrobe, faces, and blocking identical. Add light rain on the pavement.
```

### S28 — Extend (T18)

```
Continue: she leaves the envelope on the tile and walks out of frame right. The camera stays on the envelope. Rain gets a little harder. No new people.
```

### S29 — Luma concepts

```
A rusted fishing trawler at a concrete pier, overcast.
concepts: orbit right + handheld
```

### S30 — 24-second ad sequence (T20)

| t | id | size | job | audio |
|---|---|---|---|---|
| 0-6 | A1 | CU | condensation on bottle | tick, no music |
| 6-12 | A2 | MS | runner takes the same bottle | footsteps, wind |
| 12-18 | A3 | WS | bottle on lakeside rock, push to label | water, cap click |
| 18-24 | A4 | MS | "Still cold." after a breath | piano after the line |

Look sheet on every generate: soft morning window, pale stone + lake, 50mm, no VO until A4. Logo in the editor.

A4 Veo:

```
Medium shot, runner by a lake, same matte bottle in hand. She unscrews the cap, drinks, and says, "Still cold." Soft morning light, 50mm, slow push.
SFX: cap click, water, light wind. No on-screen logo.
```

### S31 — One-minute narrative The Letter (T20)

| t | id | size | action | audio |
|---|---|---|---|---|
| 0-6 | L01 | WS | rain alley, upstairs window lit | rain, tram |
| 6-12 | L02 | MS | Lin climbs stairs, envelope in pocket | footsteps |
| 12-20 | L03 | MCU to CU | envelope on tile, not opened | paper, fridge |
| 20-28 | L04 | CU | window rain; her reflection | rain up |
| 28-36 | L05 | MS | kettle on | gas click |
| 36-44 | L06 | empty two-shot | two cups, only she is there | kettle |
| 44-52 | L07 | CU | writes "not tonight" on the envelope back | pen |
| 52-60 | L08 | WS | lights off, window still rain | rain, one piano note |

L07 Sora:

```
Close-up of a woman's hand, silver-streaked hair barely in frame, writing two words on the back of a kraft envelope with a cheap blue pen. Third-floor kitchen tile, blue hour window rain in the blur.

Cinematography:
Camera shot: top-down close-up, locked
Mood: private, unsentimental

Actions:
- pen touches paper
- two short words
- pen rests

Background sound: kettle in the next room-layer, rain, no music.
No readable extra text besides those two words.
```

### S32 — Five-minute essay structure (T20)

```
PROJECT: How a tram window thinks
runtime_target: 5:00
A-roll talking head: 8-12 s chunks
B-roll generated: rain glass, ticket machine, night grid, hands on yellow pole
Lower-thirds: Remotion, never T2V
VO: recorded or TTS, mixed after
look_sheet: handheld 35mm, tungsten interiors vs cool street, grain 16mm-ish
forbid: fake Chinese typography, tourist montage cliches
```

B-roll 8 s I2V from a real still of a tram-pole hand:

```
Fingers adjust on the yellow pole as the cabin sways. Camera locked on the hand. Street lights smear in the window.
Sound: cabin rattle, ticket bell once, rain.
```

### S33 — 90-second trailer as 12 clips (T20)

Twelve 6-8 s plates sharing one look sheet and two character refs. Pattern: 3 identity locks, 4 action beats, 3 geography, 1 title card in post, 1 end card in post. Score is a licensed bed cut to picture.

### S34 — 8-12 minute short packet (T20/T21)

Required files, not one string:

- bible.md — logline, theme, rules
- cast/CHAR.LIN.md — lock paragraph + 6 stills
- loc/KITCHEN.md + weather variants
- look_sheet.md — lens, grade, lighting logic
- shot_list.csv — 80-120 rows: id, t, size, mode, model, refs, audio
- per-shot YAML from Section 7
- continuity_ledger.csv — wardrobe, hair, time, weather, prop, last-frame file

### S35 — Feature-length package (T21), 90-110 minutes

```yaml
project_id: FEATURE_RAIN_LINE
working_title: Rain Line
target_runtime_s: 5400
aspect_ratio: "2.39:1"
fps: 24
logline: "A night-shift tram inspector walks the last unopened letter across the city and does not deliver it."
world:
  city: "Hong Kong analogue, unnamed"
  season: "late rainy season"
  rules: ["naturalistic physics only", "phones stay in pockets until act 3"]
cast_bible:
  CHAR.LIN: { anchors: ["silver streak", "navy linen off-duty", "inspector jacket on duty"] }
  CHAR.MA: { anchors: ["short grey hair", "plastic rain poncho", "thermos"] }
location_bible: [LOC.DEPOT, LOC.TRAM, LOC.KITCHEN, LOC.ROOF]
look_bible:
  capture: "spherical 35/50"
  do_not: ["teal-orange trailer grade", "drone hero landmark shots"]
sound_bible:
  beds: ["rain families", "tram metal", "fluorescent buzz"]
  score: "sparse piano + low strings, enter late"
structure:
  act1_s: [0, 1500]
  act2_s: [1500, 3900]
  act3_s: [3900, 5400]
coverage_policy:
  generate: "singles 5-12 s plus selected 8 s multi-beats"
  stitch: "editorial; first-last only inside one geography"
  titles: "offline"
```

90-minute math: 30-50 sequences, 400-900 shots, 3-20 character refs, 4-8 look sheets. Continuity ledger columns: scene, wardrobe, hair, injury, time, weather, prop, last-frame, next first-frame.

### S36 — One feature scene, about 3 minutes, 8 plates

```
SCENE 24 — INT. TRAM / EXT. STREET — NIGHT — RAIN
Goal: Lin almost gives the letter to Ma and does not.
Look sheet: 35mm, eye-level, handheld only when the cabin moves, warm interior vs cold glass.

24-01 WS 6s  Last tram into a shallow-flooded stop. Ma waits in a poncho.
24-02 MS 8s  R2V
             Lin: "You shouldn't stand in that."
             Ma:  "The roof is worse."
24-03 OTS 5s Envelope half out of the inner pocket; she pushes it back.
24-04 CU 5s  Ma's thermos lid. Steam. Rain on plastic.
24-05 TWO 8s They sit one bench apart. Empty cabin. No dialogue.
24-06 CU 8s  Lin: "Not tonight." Almost inaudible. No performance tears.
24-07 WS 6s  Ma rings. Doors open onto rain. She leaves without looking back.
24-08 MCU 8s Empty bench. Envelope outline under the jacket. First score after the doors.
```

Kling emit of 24-02:

```
Night tram doorway, rain. [Character A: Lin, silver streak, inspector jacket] stands on the step. [Character B: Ma, grey hair, plastic poncho] waits on the flooded stop.
[Character A @VoiceLin] says, "You shouldn't stand in that."
[Character B @VoiceMa] answers, "The roof is worse."
Medium shot, eye-level, cabin warm vs street cold, no extra passengers, no readable ads.
```

### S37 — Feature anti-example

Do not do this:

```
Make a full 90 minute wuxia movie about a hero who saves the dynasty, lots of battles, romance, beautiful cinematography, epic music, 4K, IMAX.
```

Replace with S35-S36.

### S38 — Background weather variants of one alley (T23)

```
Wide locked camera, the same alley, rain only, no hero, two extras under the awning never looking up. 8s. Rain ambience. No music.
```

```
Same alley geometry and neon color. Rain density doubled, visible streaks across a 35mm frame, puddle rings continuous. No new signage. Locked camera. 6s.
```

```
Same alley geometry. Night neon off. Overcast dawn, leftover wet, steam only from the drain. No magenta. Slow pedestal up. Gull far away. 8s.
```

### S39 — Constraint variants of S05

Veo tail: No burned-in subtitles, no logos, no extra pedestrians crossing in front of her, no extra fingers.

Wan negative field: subtitles, captions, watermark, logo, extra limbs, duplicate face, readable text, morphing

Runway positive inverse: Single subject. Locked horizon. Clean alley. Hands remain anatomically normal.

### S40 — LLM compiler brief (T16)

```
You are a director of photography and sound designer, not a novelist.
Target model: veo-3.1
Duration: 8s
Aspect: 16:9
Assets: Image1 = character turnaround, Image2 = alley plate
Intent: Lin refuses to go upstairs yet. One Cantonese line: 未到时候。
Use the film bible lock strings verbatim. Do not paraphrase CHAR or STYLE.
Output: (1) Veo prompt (2) constraints (3) audio channels (4) what must match the previous shot's end_state
Previous end_state: mid-stride, umbrella still open, looking left.
```

### S41 — Remotion assembly (T22)

```tsx
<Series>
  <Sequence from={0} durationInFrames={24 * 8}>
    <Video src={shot_1_07} />
  </Sequence>
  <Sequence from={24 * 8} durationInFrames={24 * 6}>
    <Video src={shot_1_08} />
  </Sequence>
</Series>
```

Type stays out of the model.

### S42 — Empty kitchen holdout

```
Wide, locked tripod. The same third-floor kitchen at blue hour, no people, kettle unlit, rain on the window, neon smear, yellow crate of tangerines. 8 seconds, photoreal, 35mm.
Sound: fridge, rain, distant TV. No music.
```

### S43 — Hunyuan T2V formula fill

```
An Asian woman with long black hair wearing a red dress walks slowly through a night market. Medium shot, camera tracks beside her, warm lantern light, photorealistic style, lively but unhurried atmosphere.
```

### S44 — Firefly formula fill

```
Close-up, eye-level, slow zoom-in, a large polar bear with bright white fur looking pensive, walking toward a hole in the ice, barren snow, gray clouds moving slowly, cinematic, 35mm, shallow depth of field.
```

### S45 — Wan / ComfyUI pair

Positive: cinematic medium shot of a cyclist leaning into a rain-soaked corner at night, neon puddles, tracking camera at wheel height, wet asphalt spray, teal-orange grade, 35mm, shallow depth

Negative: still image, overexposed, subtitles, extra fingers, warped wheels, low quality, jitter, morphing background text

Graph: 81 frames, 24 fps, 832x480 draft, cfg 6.

### S46 — Off-road physics plate (T3), 8 s

```
Found-footage energy, camera seemingly mounted on the chase vehicle, mud on the lens, harsh sun through trees. An unbranded open-cockpit buggy, caked in mud, hits a shallow river at speed and throws an opaque sheet of water. A high-clearance truck follows through the same curtain and lands on the far bank, wipers fighting the mud.
Sound: guttural engines, transmission whine, suspension slam, water impact. No commentary, no logos.
```

---

## 9. Long-form pipeline

```
intent → script
      → character bibles + turnarounds
      → location plates + style bible + audio bible
      → storyboard stills
      → per-shot vg_prompt objects (duration <= model max)
      → compile to vendor dialect
      → generate 2-N takes
      → last-frame chain only inside continuous geography
      → assemble (Premiere / CapCut / Remotion / ffmpeg)
      → replace score, readable type, and problem lips in post
```

Rules: never prompt an entire scene-change inside 4 seconds; never paraphrase a character bible; generate stills before video when identity matters; assign models per shot type; keep a continuity ledger; treat burned-in text as a post problem; use LLMs as compilers, not cameras.

Suggested model assignment: Veo for dialogue two-shots, Kling for action, Seedance for multimodal inserts, Runway Aleph for surgical fixes, Remotion for type.

---

## 10. LLM compiler contract

1. Ask or assume target.model, mode, duration_s, aspect_ratio.
2. Choose a setting type from Section 6.
3. Fill the schema; do not invent plot to fill empty buses.
4. One shot per call unless the target documents multi-shot.
5. Copy look_sheet and character anchors unchanged.
6. Use the vendor's dialogue punctuation.
7. I2V = change only. Aleph = delta only.
8. Split rather than cram duration.
9. Attach retain/forbid. State audio or silence.
10. Keep counts vague unless frame 0 shows them.
11. Do not mix dialects. Return YAML + emitted string.

System prefix:

```
You are a video-prompt compiler for video_generation_prompt_specification.v1.
Read the shot schema. Emit (1) validated YAML (2) the vendor dialect string only.
Do not add new plot. Do not exceed duration_s beats. Always specify audio or silence.
```

---

## 11. Quality gates and pitfalls

Before generate: one primary action; one primary camera move; background has FG/MG/BG or an explicit void; time of day + weather; audio specified or silent; duration fits beats; identity method chosen; aspect matches delivery.

After generate: face/wardrobe match; light direction matches; no surprise score or captions; physics plausible; end frame usable if chaining.

Pitfalls: adjective stacks; three camera moves; dialogue longer than the clip; paraphrasing the character every shot; asking a silent model for a soundtrack; leaving always-on audio unspecified; readable store signs; I2V prompts that rebuild the still; Runway negatives; one prompt for a movie; mixing identity photos from different haircuts; changing implied time of day between chained shots; using copyrighted films as if they were LUTs.

---

## 12. Quick reference

```
STORAGE:     meta → intent → visual → motion → camera → audio → consistency
VEO:         camera → subject → action → context → style → audio
KLING:       subject → movement → scene → camera/light/atmosphere → audio
SORA:        prose → cinematography → beats → dialogue → bed
SEEDANCE:    refs/roles → subject → action → scene → style → camera → ( ) < > { }
WAN:         主体+场景+运动[+美学] ; 图n ; Shot N [t0-t1]
HUNYUAN:     subject + motion + scene + [shot] + [cam] + [light] + [style] + [atmosphere]
RUNWAY G4:   subject motion + camera + scene motion
ALEPH:       verb + only the change
I2V:         what moves + camera + air + sound
FL2V:        continuous journey A → B, no cuts
MJ / PIKA:   short motion sentence + flags
SVD:         motion_bucket_id
```

Portable skeleton:

```
Subject:
Action (in order):
Camera (size + one move + lens):
Place / time / weather / FG-MG-BG:
Light (source + direction + quality):
Look (medium + grade):
Audio (dialogue / SFX / ambience / music or silent):
Retain:
Forbid:
Duration / AR:
```

---

## 13. Versioning

| Version | Date | Notes |
|---|---|---|
| 1.0.0 | 2026-09-14 | Initial specification: anatomy, vendor map, canonical YAML, setting types T1-T24, sample ladder micro to feature |

Successor versions should add live API field dumps, measured word-budget tables, and a machine-readable JSON Schema of the shot object.

---

## 14. References

- Google DeepMind, How to create effective prompts with Veo 3.
- Google Cloud, Ultimate prompting guide for Veo 3.1, 2025-10-16.
- OpenAI Cookbook, Sora 2 prompting guide; OpenAI Videos API.
- Runway Help Center, Gen-4 Video Prompting Guide; Aleph 2.0 Prompting Guide.
- Kuaishou Kling T2V prompt guide; 2.6 audio user guide; 3.0 capability map.
- BytePlus / Volcengine / Seed, Seedance 2.x prompt guides and 2.5 launch posts.
- Alibaba Cloud Model Studio, Wan text-to-video prompt guide.
- Tencent HunyuanVideo 1.5 Prompt Handbook EN.
- MiniMax Open Platform, Hailuo camera commands and first/last frame API.
- Luma Labs Dream Machine API; Camera Motion / Angle Concepts.
- Adobe Firefly, writing effective text prompts for video generation.
- Midjourney video parameters (--motion, --raw, --loop, --end).
- xAI, Grok Imagine video / I2V / R2V docs.
- Zhipu CogVideoX prompting notes.
- Lightricks LTX-Video README.
- Stability SVD parameter set (motion_bucket_id, fps_id).
- ComfyUI Wan 2.2 and video-model latent-grid docs.

When a vendor document and this specification disagree on a numeric limit, believe the vendor document for that day, and keep the canonical object unchanged.

---

End of video_generation_prompt_specification.v1
