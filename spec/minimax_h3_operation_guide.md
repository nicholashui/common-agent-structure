# MiniMax H3 Complete Operation Guide

**Prompt engineering, image control, and full-system operation for MiniMax H3 (Hailuo 3.0)**

Version: 2026-09-15  
Audience: operators who need to *completely control* H3 output — stills, first/last frames, identity locks, product/brand shots, and 4–15s native-audio video.

This document is an operations manual, not a teaser. It follows MiniMax’s official rewrite format (the intermediate representation the model was trained to read), plus the practical still-image workflows that exist around H3.

---

## 0. Read this first: what H3 actually is

MiniMax H3 (also called Hailuo 3.0) is an **omni-modal generation system**, launched 2026-07-31.

It is **not** a Midjourney-style still-image model with extra video bolted on. It is a single transformer that denoises one packed sequence of text + conditioning media + target video latents + target audio latents. Video and 32 kHz stereo audio come out of the same pass. There is no separate vocoder and no post-hoc lip-sync.

| Fact | Implication for control |
| --- | --- |
| Official hosted product is **video** | `MiniMax-H3` / `MiniMax-H3-Max` have no still-image REST endpoint |
| Pretraining included **text-to-image** | Local Diffusers / ComfyUI can emit T2I and Ref2I stills by generating a short frame packet and picking one frame |
| Official MiniMax still-image API is a **different model**: `image-01` | Use `image-01` to *make* stills; use H3 to *lock, edit, or animate* them |
| H3-Context-IR is the official rewriter | The 3-field / 6-field prompt format is what the base model expects, not a style preference |
| 2K is **in-context regeneration**, not a native DiT size | Hosted 2K = 768p generation + a second H3 pass that reuses original context. Open weights locally = 768p |

If your job is “generate one still poster,” use `image-01` (hosted) or H3 T2I (local). If your job is “lock this face / product / layout and make it move, speak, or hold across shots,” use H3 with reference images and the official prompt schema.

**Control stack (the only stack that actually works):**

```
references (what is locked)
    + retention (how tightly it is locked)
    + structured prompt (what happens, camera, sound, text)
    + mode (T2I / T2VA / I2VA / FL2VA / L2VA / Ref2VA)
    + API / sampler settings (resolution, duration, ratio, expansion)
```

Natural-language mood adjectives do not control H3. Field names, labels, retention markers, and camera grammar do.

---

## 1. Access map

### 1.1 Official hosted

| Surface | URL | What it is |
| --- | --- | --- |
| Hailuo web (global) | https://hailuoai.video and https://hailuoai.video/tools/minimax-h3 | Consumer UI. Tabs: Text to Video, First & Last Frame, Reference. Type `@` to tag uploaded files. |
| Hailuo web (CN) | https://hailuoai.com | Same product, CN login. |
| MiniMax Hub | https://hub.minimax.io (global) / https://hub.minimaxi.com (CN) | Desktop / canvas workflows. Official style skills live here. |
| Platform API (global) | https://platform.minimax.io · `https://api.minimax.io` | Pay-as-you-go. Models: `MiniMax-H3`, `MiniMax-H3-Max`. Also `image-01`. |
| Platform API (CN) | https://platform.minimaxi.com · `https://api.minimaxi.com` | Same surface, CN endpoint. |
| Hugging Face | https://huggingface.co/MiniMaxAI/MiniMax-H3 | Open weights, official prompt guides, reproducible scripts. |
| Official skills | https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills | Installable `h3-prompt-writing` skill + 8 style skills. |

Install the official prompt-writing skill:

```bash
npx skills add https://github.com/MiniMax-AI/MiniMax-H3 --skill h3-prompt-writing
```

That skill is portable (Claude Code, Cursor, Codex, LangChain, any agent that can read local files). It does not call MiniMax APIs.

### 1.2 Partner and local

| Surface | Notes |
| --- | --- |
| fal.ai | `minimax/h3/text-to-video`, `image-to-video`, `reference-to-video`. Also H3 Max. |
| OpenRouter | `minimax/hailuo-3` |
| Runware | `minimax:h3@0` |
| Hugging Face Diffusers | Modular Pipeline. Modes: T2VA, FL2VA, Ref2VA, plus community T2I / Ref2I. |
| ComfyUI MiniMax H3 Studio | Video workflows. |
| ComfyUI MiniMax H3 Image Studio | Still-image generate / edit / draft. Treats H3 as a still engine by decoding a short packet. |
| X-MinimaxH3, MiniMax-H3-Swift | Local servers with storyboard editors, acceleration, second sampling. |

### 1.3 Two models you will confuse if you are not careful

| ID | Job |
| --- | --- |
| `MiniMax-H3` | Quality / 2K / full omni-reference (9 images + 3 videos + 3 audios). 4–15 s. |
| `MiniMax-H3-Max` | Fast draft. 480P / 768P. 5–15 s. Prompt expansion. Weaker or later-added omni-ref depending on host. |
| `image-01` / `image-01-live` | Official MiniMax **still-image** API. Not H3. Prompt ≤ 1500 chars. 1 character reference. |

Operating rule used by people who ship: **draft on H3 Max, finish on H3, make hero stills on `image-01` or a dedicated image model, then lock those stills into H3 as first_frame or reference_image.**

---

## 2. Choose the mode before you write a single word

Wrong mode wastes the whole prompt. Decide this first.

```
Do I need a still, or motion?

STILL
  Hosted official API     → image-01  (or Flux / Midjourney / Seedream, then import)
  Local H3 weights        → T2I  (no refs)  or  Ref2I (up to 9 images)
  “Edit this picture”     → Ref2I / H3 Image Studio Image Edit

MOTION
  Text only               → T2VA          (FL2VA checkpoint, 0 images)
  This photo is frame 0   → I2VA          (role=first_frame)
  This photo is the end   → L2VA          (role=last_frame)
  These two photos are
  start AND end           → FL2VA         (first_frame + last_frame)
  Lock face / product /
  style / motion / voice
  without pixel-locking
  frame 0                 → Ref2VA        (reference_image / _video / _audio)
```

Hard rule on hosted H3: **do not mix `first_frame`/`last_frame` with `reference_image` in one request.** They are different entry modes.

---

## 3. Specs you must design around

### 3.1 Output

| Item | MiniMax-H3 | MiniMax-H3-Max |
| --- | --- | --- |
| Resolution | 768P or 2K | 480P or 768P (no 2K) |
| Duration | 4–15 s, integers only | 5–15 s, integers only |
| Frame rate | 24 fps | 24 fps |
| Audio | Native 32 kHz stereo | Native stereo |
| Aspect | 21:9, 16:9, 4:3, 1:1, 3:4, 9:16, or adaptive | Same list |
| Prompt length | ≤ 7000 characters | ≤ 7000 characters |

T2VA: `ratio` is **required** and **cannot** be `adaptive`.  
I2VA / first-frame: ratio is taken from the image (adaptive).  
Ref2VA: ratio optional, default adaptive.

### 3.2 Input caps (hosted)

| Asset | Cap | Per-file limit |
| --- | --- | --- |
| Reference images | ≤ 9 | 256–5760 px, aspect 2:5–5:2, ≤ 30 MB, JPG/JPEG/PNG/WEBP/HEIC/HEIF |
| Reference videos | ≤ 3 | 2–15 s each, total ≤ 15 s, ≤ 50 MB, H.264/H.265 |
| Reference audio | ≤ 3 | 2–15 s each, total ≤ 15 s, ≤ 15 MB, WAV/MP3. **Cannot be the only input.** |
| Mixed files | ≤ 12 total | Request body ≤ 64 MB. Prefer URLs. |

First/last-frame entry: 0, 1, or 2 images. Zero images = T2VA.

### 3.3 Pricing (official pay-as-you-go, late 2026 — confirm live)

| Item | Price |
| --- | --- |
| H3 768P | ~$0.08 / s |
| H3 2K | ~$0.13 / s |
| H3-Max 480P | ~$0.05 / s |
| H3-Max 768P | ~$0.08 / s |
| 768P → 2K regeneration | ~$0.05 / s |
| Reference images | first 5 free, then ~$0.04 |
| `image-01` still | ~$0.0035 / image |

At 2K, MiniMax claims per-second price under one-third of mainstream 2K video models.

### 3.4 What is *not* in the official hosted schema

- No documented `seed`
- No documented `cfg` / `guidance_scale`
- No documented `negative_prompt` field
- Released weights are CFG-distilled

Local exceptions exist (MiniMax-H3-Swift `--cfg-scale 3.0–7.5` and `--negative-prompt`; some ComfyUI NegPiP nodes). On hosted H3, write constraints as ordinary English sentences inside the prompt, not as a separate negative field.

---

## 4. The official prompt is a document, not a sentence

H3-Context-IR rewrites free-form input into a fixed document. You can skip Context-IR and write that document yourself. That is how you take control.

**Language rule:** rewrite sections in English. Keep dialogue, lyrics, and visible on-screen text in the original language.

**Content rule:** every sentence must correspond to something **visible or audible**. No backstory, no “beautiful,” no “epic mood,” no intentions the camera cannot see.

---

## 5. Base modes — three fields (T2VA / I2VA / FL2VA / L2VA)

Exact order. Exact field names. Do not invent extra headings.

```text
[optional alignment line]

integrated_multimodal_description: [Shot 1] ...

overall_soundscape: ...

non_diegetic_music: ...
```

### 5.1 Alignment lines (mandatory when images are keyframes)

**T2VA** — no alignment line. Start at `integrated_multimodal_description`.

**I2VA** (image is frame 0):

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.
```

**FL2VA** (two images, start and end). Duration written to exactly two decimals:

```text
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 8.00-second mark of the target video.
```

**L2VA** (image is the last frame only):

```text
How the reference pictures align with the target video — <Picture 1> (from [Shot 1]) aligns with the 6.00-second mark of the target video.
```

The alignment line is the first line. Then one blank line. Then the three fields.

### 5.2 `integrated_multimodal_description`

This is the body. It carries style, opening composition, subject appearance and position, scene and props, actions, shot changes, spoken language, singing, and synchronized diegetic sound.

Open Shot 1 with style + composition. Official style tokens:

`Cinematic` · `live-action` · `2D-animated` · `3D CG` · `claymation` · `watercolor` · `vintage film`

```text
[Shot 1] Live-action, cinematic, a medium-wide shot frames ...
```

For keyframe tasks, derive style from the reference image. For T2VA, take it from the user’s request.

### 5.3 Shots and cuts

- Shot 1 has **no timestamp**.
- Later shots: `[Shot 2] At 00:03.500, the camera cuts to...`
- Cut times must be strictly increasing and inside the requested duration.
- Accepted cut verbs: `the camera cuts to` / `the shot cuts to` / `the shot transitions to` / `the shot changes to` / `the shot switches to`.
- Cross-dissolve, fade, wipe only when the user asked for them.
- A cut must introduce new information (subject, space, state, viewpoint, or time). If you only need a closer view, write camera motion instead of a cut.
- FL2VA prefers a **single shot** so the model can interpolate from first frame to last frame.

### 5.4 Official camera grammar

Write camera as a natural English action **inside the shot**, not as a `[Zoom in]` sticker at the end.

Complete expression = **motion type + amplitude + speed**.

Omit amplitude/speed when they are medium/normal.

| Motion type | Meaning |
| --- | --- |
| `Zoom In` / `Zoom Out` | Focal length changes; body stays put |
| `Push In` / `Pull Out` | Camera body moves forward / backward |
| `Pan Left` / `Pan Right` | Body stays; lens pivots horizontally |
| `Truck Left` / `Truck Right` | Camera translates horizontally |
| `Tilt Up` / `Tilt Down` | Body stays; lens pivots vertically |
| `Pedestal Up` / `Pedestal Down` | Whole camera rises / drops |
| `Arc Shot` | Camera orbits the subject |
| `Tracking Shot` | Camera follows a moving subject |
| `Static Shot` | Position and lens stay still |
| `Shake Slightly` / `Shake Strongly` | Handheld shake |
| `POV` | Subject’s point of view |
| `Roll Clockwise` / `Roll Counterclockwise` | Roll around lens axis |

Amplitude: `with small amplitude` · `with large amplitude`  
Speed: `at slow speed` · `at fast speed`

```text
The camera pushes in with small amplitude at slow speed toward the folded letter in her hands.
The camera pans right with large amplitude at fast speed, revealing the open doorway.
The camera holds a static shot as the runner exits the frame.
```

One primary camera move per shot.

### 5.5 Speakers, dialogue, singing

- Speakers who actually vocalize get stable IDs: `(S1)`, `(S2)`, compound `(S1,S2)`.
- Silent characters get no ID.
- IDs persist across shots.
- On first appearance, establish type, age/gender if relevant, on-screen vs off-screen, pitch, timbre, rate, accent.
- Dialogue lives inside `<d>`. Outside the tag: identity + ID + action + delivery. Inside the tag: language tag + **verbatim** words. Do not translate. Do not rewrite punctuation.

```text
The young woman with a quiet, breathy voice (S1) says: <d>[English] I get off at the next station.</d>
The two children (S1,S2) shout together, <d>[English] Wait for us!</d>
```

Voiceover — use this exact phrase, then close the lips:

```text
The man (S1) says in an off-screen voiceover: <d>[English] I still remember that road.</d> while his lips remain completely closed.
```

Dialogue that crosses a cut: wrap both sides with `<scenetrans>` and say the audio continues (`continues seamlessly across the cut`, `carries over from the previous shot`, etc.).

Speech truncated by the end of the clip: `<cutoff>`.

Supported dialogue languages (stable): Arabic, Chinese, English, French, German, Italian, Japanese, Korean, Portuguese, Russian, Spanish.

### 5.6 On-screen text (critical for brand work)

Anything actually visible — neon, label, poster title, UI string — goes in English double quotes. Preserve original language and punctuation. Do not translate.

```text
A red neon sign reading "营业中" glows above the doorway.
The bottle label reads "HAKU 700ml" in white serif on matte black glass.
```

H3 is unusually good at legible brand text **if you quote the exact string and tell it to stay sharp and correctly spelled for the whole clip**.

### 5.7 `overall_soundscape`

1–4 English sentences, one paragraph. Ambient + physical action + non-verbal human sound (wind, rain, footsteps, fabric, impacts, breathing, laughter).

Do **not** repeat dialogue, singing, or diegetic music here.

`N/A` only when the user wants complete silence.

```text
overall_soundscape: Steady rain taps against the café windows while low room ambience continues underneath. The entrance bell rings once, followed by wet footsteps and the soft scrape of a chair.
```

### 5.8 `non_diegetic_music`

1–3 sentences. Score the **characters cannot hear**. Instrumentation, tempo, rhythm, dynamics. No mood words (“sad,” “epic”).

Diegetic radio / phone / on-screen band belongs in `integrated_multimodal_description`.

No score: `N/A`.

```text
non_diegetic_music: Sparse piano notes at a slow tempo, joined by sustained low strings that gradually increase in volume before fading out.
```

---

## 6. Full-reference mode — six fields (Ref2VA)

Use this when you attach reference images / videos / audio that are **not** simple first/last keyframes. This is the mode that “completely controls” identity, product, motion, and voice.

Exact order:

```text
subject_definitions:
...

summary:
...

retention_analysis:
...

detailed_description:
...

overall_soundscape:
...

non_diegetic_music:
...
```

`detailed_description` for generation tasks is normally **350–500 English words**. Dialogue-dense clips prioritize fitting the spoken timeline over hitting a word count.

### 6.1 Labels (keep them stable across every section)

| Label | Meaning |
| --- | --- |
| `<Subject N>` | Reusable visible unit: person, object, outfit, room, style, pose, UI |
| `<Picture N>` | A reference image used as a concrete frame or storyboard anchor |
| `<Video N>` | A reference video used as edit source, continuation, or temporal structure |
| `<Audio N>` | A standalone audio asset (or an enabled sync track from a ref video) |

`<Picture N>` / `<Video N>` / `<Audio N>` match upload order. Hailuo UI uses `@Image1` `@Video1` `@Audio1` — same idea. In the official rewrite, use the angle-bracket labels.

If an image only defines a character, do **not** also create a standalone `<Picture N>` line. Cite it inside the `<Subject N>` definition.

```text
<Subject 1> is the young woman in <Picture 1>, with long dark hair, a blue cardigan, and a thin silver necklace.
<Subject 1> is the woman whose appearance comes from <Picture 1> and whose walking motion comes from <Video 1>.
<Picture 2> is the first frame of [Shot 1], showing a woman seated beside a café window.
<Picture 3> is a storyboard reference for [Shot 1] and [Shot 2], defining their viewpoint, subject placement, and shot order.
<Video 1> is the source video for the target video edit.
<Audio 1> is the voice-timbre reference for <Subject 1> (S1).
```

`<Video N>` and `<Audio N>` are numbered independently. A file containing sound does **not** automatically create an `<Audio N>`.

### 6.2 `summary` prefixes

One short English paragraph. Starts with a square-bracketed task type:

| Prefix | When |
| --- | --- |
| `keyframe completion` | Image is an actual first / last / mid keyframe |
| `reference generation` | Asset guides character, style, action, camera, storyboard — not a concrete frame and not an edited source video |
| `video editing` | An existing video is directly modified |
| `video continuation` | New content continues from an existing video |
| `audio reuse` | Same audio signal copied in full or in part |
| `audio reference` | Timbre / rhythm / style / lyric content referenced, not copied |

Combine with ` + `. Do not repeat a type.

```text
[reference generation + audio reference] The target video shows <Subject 3> eating a cookie in <Subject 1>. ...
[video continuation + keyframe completion]
[video editing + audio reuse]
```

### 6.3 Retention markers (fixed English — do not paraphrase)

Visual (`<Subject N>`, `<Picture N>`, `<Video N>`):

| Marker | Meaning |
| --- | --- |
| `fully_preserved` | Defined role kept in full |
| `partially_preserved` | Still used; some defined traits change |
| `attribute_transfer` | Selected traits move onto a different target |
| `weak_reference` | Only broad style / category / atmosphere |

Audio (`<Audio N>`):

| Marker | Meaning |
| --- | --- |
| `fully_copy` | Entire source audio is the final track |
| `partially_copy` | Part of the timeline or selected layers copied |
| `reference` | Timbre / rhythm / style / content referenced, signal not copied |
| `weak_reference` | Broad category / atmosphere only |

```text
<Subject 1> (appears in [Shot 1], [Shot 3]): fully_preserved - face, hair, and green corduroy jacket remain identical.
<Picture 2> ([Shot 1] first frame): fully_preserved - composition, lighting, and product geometry stay locked.
<Video 1> (cut and pacing structure): weak_reference - only edit rhythm is borrowed.
<Audio 1>: reference - vocal timbre and measured delivery guide <Subject 1> (S1) without copying the original signal.
```

This section is how you stop H3 from blending every uploaded file into one soup.

### 6.4 Using labels inside shots

First clear appearance: describe referenced traits, frame position, current action. Later shots reuse the same label without redefining it.

```text
the shot begins from <Picture 1>
the shot's keyframe corresponds to <Picture 2>
the shot ends on <Picture 3>
<Subject 2> (S1) turns toward the woman and says, <d>[English] Last summer, I went to my grandfather's house.</d>
```

Style for Ref2VA is stated in **one or two sentences before `[Shot 1]`**, not after it.

---

## 7. Image generation and image control

This is the section most “H3 image prompt” searches miss. There are three different jobs.

### 7.1 Job A — Official stills: `image-01`

Hosted endpoint:

```
POST https://api.minimax.io/v1/image_generation
Authorization: Bearer <token>
```

```json
{
  "model": "image-01",
  "prompt": "A man in a white t-shirt, full-body, standing front view, outdoors, with the Venice Beach sign in the background, Los Angeles. Fashion photography in 90s documentary style, film grain, photorealistic.",
  "aspect_ratio": "16:9",
  "response_format": "url",
  "n": 3,
  "prompt_optimizer": true
}
```

With a character lock:

```json
{
  "model": "image-01",
  "prompt": "A girl stands by the library window, gazing into the distance",
  "aspect_ratio": "16:9",
  "subject_reference": [
    {
      "type": "character",
      "image_file": "https://example.com/face.jpg"
    }
  ],
  "n": 2,
  "prompt_optimizer": false
}
```

| Parameter | Rule |
| --- | --- |
| `model` | `image-01` or `image-01-live` |
| `prompt` | required, **max 1500 characters** (not 7000) |
| `aspect_ratio` | `1:1` (1024²), `16:9` (1280×720), `4:3` (1152×864), `3:2` (1248×832), `2:3` (832×1248), `3:4` (864×1152), `9:16` (720×1280), `21:9` (1344×576, image-01 only) |
| `width` + `height` | optional custom size on `image-01`; set together |
| `n` | 1–9 images per request |
| `prompt_optimizer` | bool, default `false`. Turn **off** when the prompt is already specific. |
| `subject_reference` | **one** character image per request |
| `response_format` | `url` or `base64` |
| `seed` | available on the `image-01` still API (not on hosted H3 video) |

`image-01` prompt engineering is classic still-image prompting:

```
[subject with distinctive traits] + [pose / viewpoint] + [wardrobe] + [environment] + [lighting] + [lens / medium] + [color grade] + [exact on-screen text]
```

Weak: `a beautiful woman in a city, cinematic, 8k`  
Strong: `A woman in her early thirties with a sharp bob and a moss-green corduroy jacket, three-quarter view, standing under a Tokyo station clock at night. Wet pavement, neon "新宿" reflected in the tiles, 35mm, shallow depth of field, tungsten practicals, film grain, photorealistic.`

Then feed the best still into H3 as `first_frame` or `reference_image`.

### 7.2 Job B — Local H3 stills: T2I / Ref2I

H3 is still an AV model. Local image studios (ComfyUI MiniMax H3 Image Studio, Diffusers T2I/Ref2I tabs) generate a **short frame packet**, decode it, and pick one still. That is why “H3 image generation” exists at all on consumer GPUs.

Typical local canvas:

| Profile | Area | Use |
| --- | --- | --- |
| fast preview | ~0.40 MP | prompt tests |
| balanced | ~0.70 MP | drafts |
| native detail | ~0.98 MP (≈1344×768) | default hero still |
| high-res 2–8 MP | optional | small-text recovery; VRAM climbs; detail does not scale linearly |

Sampling starting points:

- Draft / Turbo 768p: euler or 4–8 steps
- Quality: res_multistep / simple, ~20 steps
- Experimental single-frame T2I exists; 5-frame packets are more stable
- Local CFG (only where the UI exposes it): 3.0–7.5 useful; 1.0 = no second pass
- Negatives, if the node supports them, go in `--negative-prompt`, **not** inside the official fields

**Still-image prompt format used by H3 image compilers** (omit audio fields):

```text
subject_definitions:
<Subject 1> is the woman in <Picture 1>, exact face, hair, and green corduroy jacket.
<Subject 2> is the gothic ink rendering style from <Picture 2>.
<Subject 3> is the poster hierarchy and typography placement from <Picture 3>.

summary:
[image generation] 9:16 promotional anime key visual titled "DIO'S REQUIEM", locking identity from Picture 1, transferring ink style from Picture 2, transferring layout from Picture 3.

retention_analysis:
<Subject 1>: fully_preserved - face, hair, jacket identical.
<Subject 2>: attribute_transfer - ink linework and contrast only; ignore the source subject.
<Subject 3>: attribute_transfer - title placement and hierarchy only.

detailed_description:
A 9:16 key visual, painted in high-contrast gothic ink. <Subject 1> occupies the lower third, three-quarter view, looking just past camera. Title "DIO'S REQUIEM" sits in the upper third in the hierarchy taken from <Picture 3>. Paper tooth visible. No motion blur. No extra figures.
```

Still-image rules:

- Describe **composition, subject, lighting, materials, typography, fidelity** — not time.
- One job per reference image. If refs fight, H3 averages them.
- Quote exact on-screen text in `"double quotes"`.
- Identity drift → `fully_preserved` + list immutable traits (face, hairline, moles, jacket stitching) + closer crop.
- Large edits: keep source fidelity around 0.50–0.60 in UIs that expose it.

Ref2I is how you do outfit swap, style transfer, environment replacement, and 3D/anime → photoreal **without** a separate image model, as long as you assign roles.

### 7.3 Job C — Control images *inside* hosted H3 (the real production path)

You do not “prompt an image model.” You assign each still a **legal role**.

| Role | What it does | When to use |
| --- | --- | --- |
| `first_frame` | Pixel-level lock at t = 0.00 | Animate *this* photograph |
| `last_frame` | Pixel-level lock at the last frame | Land on *this* photograph |
| `first_frame` + `last_frame` | Interpolate the path | Transformation, product open, grow-up |
| `reference_image` | Identity / product / style / layout guidance. Not a pixel lock. | Character consistency, catalog, brand kit, multi-subject |

**I2VA still-to-motion template (copy this):**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action, commercial product photography, the subject shown in <Picture 1> remains in the same position, wardrobe, colors, key objects, and spatial relationships. The camera pushes in with small amplitude at slow speed toward the bottle. A thin stream of espresso begins to fall from the spout. Pale crema builds into a ring. The stream thins, then stops, leaving the cup two thirds full.

overall_soundscape: A low pump hum runs under the shot, followed by the steady hiss of espresso striking ceramic and a faint metallic tick as the pump cuts out.

non_diegetic_music: N/A
```

I2VA writing order: **first-frame anchor → action onset → continuous development → result.**  
Do not re-describe the whole photograph. Name only the invariants that must not drift, then write the delta.

FL2VA writing order: **first-frame state → observable intermediate changes → progressively narrowing differences → last-frame state.**  
The two photos must be the same room, compatible framing, compatible light. Otherwise the model morphs.

L2VA writing order: **plausible preceding state → explicit transition → gradual convergence → last-frame landing.**

### 7.4 Reference-image operating rules (the control surface)

1. Give every image **one job**.  
   `Image 1 = face lock. Image 2 = product geometry + label. Image 3 = location + lighting. Image 4 = ending logo.`
2. Say what to **ignore**.  
   `Video 1 defines hand trajectory and timing only. Do not copy its actor, wardrobe, setting, lighting, or camera.`
3. Separate **invariants** from **variables**.  
   Invariants: face, hairline, product silhouette, label spelling, brand hex.  
   Variables: pose, camera, room, time of day.
4. Close-ups hold identity. Wide shots of small faces drift.
5. Never ask H3 to invent a body from a tight face crop (“she stands up and walks away” from a headshot). Stay inside the information the still already contains, or supply a full-body reference.
6. Source image quality is a hard ceiling. Soft, busy, or badly lit stills produce soft, busy, badly lit motion.
7. In Hailuo Reference tab, type `@` and insert the numbered tag. Confirm the thumbnail before you generate.

---

## 8. Hosted API operation checklist

### 8.1 Endpoints

| Step | Method | Path |
| --- | --- | --- |
| Create | POST | `/v2/video_generation` |
| Poll | GET | `/v2/query/video_generation/{task_id}` every ~10 s |
| Download | GET | `content.url` from the succeeded payload |
| Rewrite prompt | H3-Context-IR — documented as `POST /v2/h3_context_ir` and as `video-generation-v2-h3-context-ir` | same `content[]` as generation; returns structured `content.prompt`. Re-attach media in **the same order**. Official statement: Context-IR is critical to quality; open weights do not include it. |
| Lift to 2K | H3-Regenerate-2K (`/video-generation-v2-regeneration`) | send original content + `base_video` |

Global base: `https://api.minimax.io`  
CN base: `https://api.minimaxi.com`

### 8.2 T2VA

```json
{
  "model": "MiniMax-H3",
  "content": [
    {"type": "text", "text": "<your 3-field prompt>"}
  ],
  "duration": 5,
  "resolution": "2K",
  "ratio": "16:9"
}
```

### 8.3 I2VA (first frame)

```json
{
  "model": "MiniMax-H3",
  "content": [
    {"type": "text", "text": "<alignment line + 3-field prompt>"},
    {
      "type": "image_url",
      "image_url": {"url": "https://.../still.png"},
      "role": "first_frame"
    }
  ],
  "duration": 8,
  "resolution": "2K"
}
```

### 8.4 First + last frame

```json
{
  "model": "MiniMax-H3",
  "content": [
    {"type": "text", "text": "<FL2VA alignment + 3-field prompt>"},
    {"type": "image_url", "image_url": {"url": "https://.../start.jpg"}, "role": "first_frame"},
    {"type": "image_url", "image_url": {"url": "https://.../end.jpg"}, "role": "last_frame"}
  ],
  "duration": 8,
  "resolution": "2K"
}
```

### 8.5 Ref2VA

```json
{
  "model": "MiniMax-H3",
  "content": [
    {"type": "text", "text": "<6-field prompt citing <Picture 1> <Video 1> <Audio 1>>"},
    {"type": "image_url", "image_url": {"url": "https://.../face.png"}, "role": "reference_image"},
    {"type": "image_url", "image_url": {"url": "https://.../product.png"}, "role": "reference_image"},
    {"type": "video_url", "video_url": {"url": "https://.../motion.mp4"}, "role": "reference_video"},
    {"type": "audio_url", "audio_url": {"url": "https://.../voice.wav"}, "role": "reference_audio"}
  ],
  "duration": 10,
  "resolution": "2K"
}
```

Every request **must** include one non-empty `type=text` item.

### 8.6 H3 Max expansion

```json
"extra": {
  "prompt_expansion_mode": "disabled"
}
```

| Mode | Use |
| --- | --- |
| `disabled` | You already wrote the official document. Always use this for production briefs. |
| `balanced` | Default. Short casual prompts. |
| `quality` | Even more rewriting. Loses control. |

If you spent time writing the 3-field / 6-field document, set expansion to `disabled` or the rewriter will flatten your labels.

### 8.7 Recommended hosted loop

1. Write a short intent (one action, one camera, one sound).
2. Optionally send it through **H3-Context-IR** and inspect `content.prompt`.
3. Edit the structured prompt by hand (this is the control step).
4. Generate 5 s at **768P** on H3 or H3 Max.
5. Fix one axis only (identity, camera, sound, text). Repeat invariants every time.
6. Generate the keeper at full duration.
7. Run **H3-Regenerate-2K** on the 768P keeper. This is not an ESRGAN upscale; it re-reads original context and recovers small text / product detail.

---

## 9. Worked official examples

### 9.1 T2VA — bakery, two shots (official pattern)

```text
integrated_multimodal_description: [Shot 1] Live-action, cinematic, a medium-wide shot frames a baker opening the shutters of a small street bakery before sunrise. The camera pushes in with small amplitude at slow speed as the middle-aged baker with a calm, slightly raspy voice (S1) places a fresh loaf on the wooden counter and says: <d>[English] First batch of the morning.</d> [Shot 2] At 00:05.000, the camera cuts to a close-up of steam rising from the sliced bread while the baker's final words carry over from the previous shot.

overall_soundscape: Wooden shutters scrape open over a quiet street as trays clink softly inside the bakery. The doorbell rings once, followed by light footsteps and the crisp sound of bread being sliced.

non_diegetic_music: A soft acoustic-guitar pattern at a moderate tempo, joined by sparse upright-bass notes and a gentle fade at the end.
```

### 9.2 I2VA — train window from a still (official pattern)

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, the young woman shown in <Picture 1> remains beside the rain-covered train window, preserving her appearance, clothing, seat position, and the carriage layout. The camera trucks right with small amplitude at slow speed as she lifts her gaze from the folded letter toward the passing city lights. Her reflection moves across the glass while the quiet, breathy young woman (S1) says: <d>[English] I get off at the next station.</d> She folds the letter along its existing crease.

overall_soundscape: The train wheels produce a steady metallic rhythm beneath a low ventilation hum. Rain ticks against the window while paper rustles softly in her hands.

non_diegetic_music: Sustained cello notes at a slow tempo with widely spaced piano tones, gradually decreasing in volume.
```

### 9.3 FL2VA — umbrella opens onto the last frame (official pattern)

```text
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 8.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, a rain-soaked cyclist begins in the position and framing established by Picture 1, holding a closed black umbrella beside a silver bicycle. The camera pulls out with small amplitude at slow speed as she releases the bicycle handle, raises the umbrella above her shoulder, and presses the runner upward until the canopy opens. Water rolls from the expanding fabric while she steps beneath it, rotates the handle into the final angle, and settles into the pose, spacing, and composition established by Picture 2 at the end of the shot.

overall_soundscape: Rain falls steadily on the pavement, followed by the metallic click of the umbrella runner and the soft snap of the canopy opening. Water drips from the bicycle frame as distant traffic passes.

non_diegetic_music: N/A
```

### 9.4 Product still → 8 s commercial (production pattern)

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action, commercial product photography, the matte black espresso machine shown in <Picture 1> stands on the walnut counter exactly as framed, preserving its position, the white ceramic cup beneath the spout, the raking window light from the left, and the dark tiled backsplash behind it. The camera pushes in with small amplitude at slow speed toward the cup as a thin stream of espresso begins to fall from the spout. Pale crema builds into a ring on the surface while a single curl of steam rises and bends toward the window. The stream thins, then stops, leaving the cup two thirds full.

overall_soundscape: A low pump hum runs under the shot, followed by the steady hiss of espresso striking ceramic and a faint metallic tick as the pump cuts out.

non_diegetic_music: A single sustained electric-piano chord at a slow tempo, decreasing in volume through the second half.
```

### 9.5 Brand text that must stay spelled correctly

```text
integrated_multimodal_description: [Shot 1] Live-action, cinematic, early morning, empty street. A café front window fills the frame. The words "OPEN FROM SEVEN" are painted on the glass in cream serif capitals, arched, and they stay sharp and correctly spelled for the whole clip. A small circular cream logo sits centered under the arch. The camera pushes in with small amplitude at slow speed toward the lettering. Soft overcast daylight. Faint reflections of the street move across the glass.

overall_soundscape: A distant bus passes. A metal shutter rolls up off screen.

non_diegetic_music: N/A
```

### 9.6 Ref2VA sitcom beat (official complete example, condensed)

```text
subject_definitions:
<Subject 1> is the coffee-shop environment in <Picture 1>, featuring an exposed brick wall, an orange tufted sofa with patterned pillows, a neon sign, and a wooden coffee table.
<Subject 2> is the fluffy white Samoyed in <Picture 2>, <Picture 3>, and <Picture 4>, with thick white fur, pointed ears, a dark nose, and a curved tail.
<Subject 3> is the young blonde woman in <Video 1>, with long blonde hair and a light-pink button-down shirt with rolled-up sleeves.
<Subject 4> is the young man in <Video 2>, with short wavy brown hair and a dark-grey hoodie with drawstrings.
<Audio 1> is the voice-timbre reference for <Subject 3> (S1), containing a spoken English vocal layer.

summary:
[reference generation + audio reference] The target video shows <Subject 3> eating a cookie in <Subject 1>. <Subject 4> enters with <Subject 2>, which lunges toward the cookie. The three-shot exchange uses <Audio 1> as the voice-timbre reference for <Subject 3> and ends with a canned audience laugh.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - brick wall, orange sofa, pillows, neon, table retained.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - Samoyed identity retained.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - blonde identity, long hair, light-pink shirt retained.
<Subject 4> (appears in [Shot 1], [Shot 2]): fully_preserved - hoodie identity retained.
<Audio 1>: reference - vocal timbre guides <Subject 3> without copying the original signal.

detailed_description:
The target video uses a realistic multi-camera sitcom style with warm indoor lighting.
[Shot 1] A medium shot establishes <Subject 1> ... <Subject 3> (S1) ... <d>[English] Hey! Watch your dog!</d> ...
[Shot 2] At 00:03.000, the shot cuts to a close-up of <Subject 4> (S2) ...
[Shot 3] At 00:05.000, the shot cuts to a close-up of <Subject 3> (S1) ...

overall_soundscape:
Soft indoor coffee-shop room tone continues throughout the scene.

non_diegetic_music:
N/A
```

---

## 10. Production recipes (copy, then swap nouns)

### 10.1 Character locked by a still, new room

```text
Keep the woman in <Picture 1> exactly as she is: face, hair, and green corduroy jacket stay identical from the first frame to the last. Put her in a second-hand bookshop. She walks the length of the aisle, pulls a paperback from a high shelf, and reads the back cover as she keeps walking. Warm tungsten, tall stacks, shallow depth of field.
Sound: floorboards, a page turning, a quiet radio at the front of the shop.
```

Rewrite this into I2VA or Ref2VA official fields before sending.

### 10.2 Motion transfer

```text
<Video 1> defines camera speed, direction, and the moment the move settles only. Do not copy its actor, wardrobe, setting, or lighting.
<Picture 1> fully_preserved as the subject: a lone red tractor in a harvested field at dusk.
Low sun behind the tractor. Long shadows on the stubble.
Sound: wind across open ground, metal ticking as the engine cools.
```

### 10.3 Outfit try-on (attribute_transfer)

```text
<Picture 1> identity/fully_preserved — face, hair, body proportions.
<Picture 2> attribute_transfer — garment color, material, cut only; ignore the person wearing it.
<Picture 3> environment and lighting only; ignore people.
[0–3s] medium shot, relaxed pose.
[3–6s] quarter turn.
[6–8s] settles and smiles.
Camera: locked eye-level with micro-movement.
Sound: room tone only. non_diegetic_music: N/A
```

### 10.4 UGC talking head, 9:16

```text
<Picture 1> fully_preserved — face, hair, skin, outfit.
<Picture 2> bedroom and lighting only.
Chest-up, static handheld with micro-movement.
[0–1.5s] looks into camera.
[1.5–8s] <d>[Cantonese] 呢支真係冇香味死白開。</d>
Natural room tone. No music. No subtitles. No beauty smoothing.
```

### 10.5 Local Ref2I poster

Use the four-section still format in §7.2. One image = identity, one = style, one = layout. Quote the title. State “no motion blur.”

---

## 11. Control levers ranked by actual power

1. **Mode + role of each file** — first_frame vs reference_image changes the physics of the job.
2. **Retention markers** — `fully_preserved` vs `attribute_transfer` vs `weak_reference`.
3. **Explicit ignore lists** — “do not copy setting / lighting / extra people.”
4. **Official field structure** — unlabeled paragraphs get rewritten badly.
5. **One action that fits the duration** — 5 s cannot hold four beats.
6. **Camera sentence with type + amplitude + speed** — missing camera = locked tripod.
7. **Quoted on-screen text** — unquoted text gets invented or misspelled.
8. **Sound written as sources** — “wooden rib scraping clay,” not “relaxing audio.”
9. **H3-Context-IR then hand-edit** — let the official rewriter draft, then lock labels.
10. **768P iterate → 2K regenerate** — do not spend 2K budget on a broken 5 s draft.
11. **Prompt expansion = disabled** once the document is written.
12. **Source-image quality** — H3 cannot add information the still never had.

Things that look like controls but usually are not, on hosted H3: CFG, seed, negative-prompt boxes, “8k,” “masterpiece,” stacked style hashtags.

---

## 12. Common failure modes and the fix

| Failure | Cause | Fix |
| --- | --- | --- |
| Face drifts mid-clip | Wide shot, weak lock, or first_frame used as a loose ref | Close-up + `fully_preserved` + list immutable traits; or add a second identity still |
| Product label warps | Geometry not locked; text not quoted | Quote the exact string; `fully_preserved` on silhouette + label layout; use 2K regen |
| Morph between first and last frame | Photos from different rooms / lenses / light | Reshoot or regenerate endpoints so they share space and light; keep a single shot |
| Action turns to mush | Three actions in 5 s | One completed move per clip |
| Locked-off boring clip | No camera sentence | Write one official camera move |
| Random score | `non_diegetic_music` omitted | Write `N/A` |
| Random subtitles / watermark | Model likes to invent text | Constraint sentence: `No subtitles, captions, or watermarks.` Also describe an empty place rather than banning a person who “should not be there.” |
| References blended | No roles, no ignore list | One job per file + retention line |
| Body invented from a headshot | Prompt asks for a walk-away the still cannot support | Stay in-frame, or supply a full-body reference |
| Dialogue out of sync / wrong language | Words rewritten or not wrapped in `<d>` | Verbatim inside `<d>[Language] ...</d>` |
| Expansion destroyed your brief | `balanced` / `quality` on a finished document | `disabled` |
| 2K looks like a soft upscale | You upscaled the MP4 instead of H3-Regenerate-2K | Use the official regeneration pass with original context |
| Local T2I looks like a random video frame | You left motion / audio fields in a still prompt | Four-section still format, no sound fields, “no motion blur” |

---

## 13. Teach another AI to write H3 prompts

Install MiniMax’s official skill when you can:

```bash
npx skills add https://github.com/MiniMax-AI/MiniMax-H3 --skill h3-prompt-writing
```

When you cannot install skills, paste the system prompt below into Claude / Grok / Cursor / your own rewriter agent.

### 13.1 System prompt (copy)

```text
You are an H3 prompt compiler for MiniMax H3 (Hailuo 3.0).

GOAL
Rewrite the user's request into the exact MiniMax H3 document the model was trained to read. Do not write Midjourney / Flux keyword soup. Do not add mood adjectives, backstory, or "8k masterpiece" tags.

STEP 1 — DETECT MODE
Choose exactly one:
- T2I / Ref2I     still image (local H3 image studio or image-01 companion)
- T2VA            text only
- I2VA            one image is frame 0
- L2VA            one image is the last frame
- FL2VA           two images are start and end frames
- Ref2VA          any mix of reference images / videos / audio that are not simple keyframes

If the user did not specify duration, default 6 seconds for motion, still-image otherwise.
If the user did not specify aspect, default 16:9 (T2VA) or adaptive (I2VA / Ref2VA).

STEP 2 — LANGUAGE
Write all structural fields in English.
Preserve dialogue, lyrics, and visible on-screen text in the original language, verbatim.

STEP 3 — OUTPUT SHAPE

Still image (T2I / Ref2I):
subject_definitions
summary            (prefix [image generation])
retention_analysis
detailed_description
Do NOT emit overall_soundscape or non_diegetic_music.
Describe composition, subject, lighting, materials, typography, fidelity. No timeline.

T2VA / I2VA / FL2VA / L2VA:
[alignment line if I2VA / FL2VA / L2VA]
integrated_multimodal_description
overall_soundscape
non_diegetic_music

I2VA alignment (verbatim):
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

FL2VA alignment:
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot N) aligns with the S.SS-second mark of the target video.

L2VA alignment:
How the reference pictures align with the target video — <Picture 1> (from [Shot N]) aligns with the S.SS-second mark of the target video.

Ref2VA, in this exact order:
subject_definitions
summary
retention_analysis
detailed_description
overall_soundscape
non_diegetic_music

STEP 4 — HARD RULES
1. Exact field names and order. Never invent extra section titles.
2. Every sentence maps to something visible or audible.
3. One primary action per clip. Start state → change → end state. Match the requested duration.
4. [Shot 1] has no timestamp. Later shots: [Shot N] At MM:SS.mmm, the camera cuts to ...
5. Camera is a sentence using official vocabulary:
   Zoom In/Out, Push In/Pull Out, Pan Left/Right, Truck Left/Right, Tilt Up/Down,
   Pedestal Up/Down, Arc Shot, Tracking Shot, Static Shot, Shake Slightly/Strongly,
   POV, Roll Clockwise/Counterclockwise
   plus optional "with small/large amplitude" and "at slow/fast speed".
6. Speakers: (S1) (S2) (S1,S2). Dialogue: <d>[Language] verbatim</d>.
   Voiceover: "says in an off-screen voiceover" + "lips remain completely closed".
7. On-screen text in English double quotes, original language preserved.
8. Style opens Shot 1 (base modes) or sits in 1–2 sentences before Shot 1 (Ref2VA):
   Cinematic, live-action, 2D-animated, 3D CG, claymation, watercolor, vintage film.
9. Assign every reference a narrow job AND what to ignore.
10. Retention markers are fixed English:
    visual: fully_preserved | partially_preserved | attribute_transfer | weak_reference
    audio:  fully_copy | partially_copy | reference | weak_reference
11. summary prefixes: [keyframe completion] [reference generation] [video editing]
    [video continuation] [audio reuse] [audio reference] — combine with " + ".
12. overall_soundscape = ambience + foley + non-verbal human sound. N/A only for total silence.
13. non_diegetic_music = audience-only score, instrumentation + tempo, no mood words. N/A if none.
14. Do not translate or paraphrase user dialogue.
15. If the user's idea overflows the duration, split into multiple clips and say so. Do not cram.

STEP 5 — RETURN
Return only the compiled H3 document, ready to paste.
If something is ambiguous (duration, aspect, which image is the face lock), ask one short question first.
```

### 13.2 Few-shot user → compiler examples to keep in the agent

User: `雨夜便利店，女孩撑伞等车，镜头慢推，只有雨声，不要配乐，6秒 9:16`

Compiler emits T2VA, 9:16, 6.00 s, `[Shot 1] Live-action, cinematic night photography...`, `non_diegetic_music: N/A`.

User: `用这张产品图做8秒广告，机器不要变形，标签 HAKU 700ml 一直清楚`

Compiler emits I2VA with the official alignment line, quotes `"HAKU 700ml"`, `fully referenced`, one camera push, physical pump/hiss in `overall_soundscape`.

User: `图1锁脸，图2只借外套材质，图3是房间，她转身对镜头讲一句广东话`

Compiler emits Ref2VA six fields, `attribute_transfer` on the jacket, `<d>[Cantonese] ...</d>`, ignore lists on each picture.

### 13.3 Quality gate before you send

- [ ] Mode is correct and matches the files you will attach
- [ ] Field names and order match the official guide
- [ ] Duration of the description equals requested seconds
- [ ] Shot 1 has no timestamp; later shots do
- [ ] Each reference has a role + ignore list + retention marker
- [ ] Camera uses official vocabulary as a sentence
- [ ] Quoted on-screen text is exact
- [ ] Dialogue is inside `<d>` and untranslated
- [ ] `non_diegetic_music` is either a real score or `N/A`
- [ ] Expansion will be `disabled`
- [ ] You are iterating at 768P before paying for 2K

---

## 14. Local / ComfyUI notes (when you self-host)

Open weights: https://huggingface.co/MiniMaxAI/MiniMax-H3  
Checkpoints: `transformer/` = T2VA + FL2VA; `transformer_ref/` = Ref2VA.

Practical VRAM (community measurements, Aug 2026):

- Projected text encoder + `H3_LOWVRAM=group` + fp16 VAE can run T2I 768² on a 16 GB card
- 5 s 768² T2VA on RTX 4060 Ti 16 GB: ~25 min, ~11.4 GB peak
- Audio-ref and tall 768×1344 clips need more than 12 GB
- W4A8 profiles exist for 8 GB first-pass; INT8 for 16 GB

Image Studio workflows to start with:

- Image Generate / Image Draft (Turbo 4–8 step)
- Image Edit / Reference Edit (Ref2VA, up to 9 ordered refs)
- T2I and I2I, including experimental single-frame variants

Second sampling / SelfLift / H3-Regenerate-style local passes reuse clean latents + original prompt + original refs. That is not “upscale the MP4.”

License: MiniMax H3 Community License. US / EU / UK / South Korea weight use may require the application at https://platform.minimax.io/h3-license. Confirm current geographic terms before distributing weights.

---

## 15. Companion still-image prompting (image-01 and any still you will later lock)

When you generate the still that H3 will have to honor, write it as a **production still**, not a vibe.

Template:

```
[exact subject: age range, hair, face landmarks, wardrobe with materials]
[pose and eyeline]
[environment with 3 concrete props]
[lighting: source + direction + hardness + time of day]
[lens / medium: 35mm / 50mm / 85mm, depth of field, grain, still-photography look]
[color: named palette, not "cinematic"]
[on-screen text in "exact glyphs"]
[what must stay empty]
```

Turn `prompt_optimizer` **off** once this is filled. Optimizer helps one-line prompts and hurts locked briefs.

Then decide the H3 role before you upload: first_frame (pixel lock) vs reference_image (identity/style lock).

---

## 16. Reference sites — official first, then learning libraries

### Official (read these before anything else)

1. MiniMax H3 announcement — https://www.minimax.io/blog/minimax-h3  
2. Hugging Face model card — https://huggingface.co/MiniMaxAI/MiniMax-H3  
3. Official prompt-writing skill — https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills  
4. Base-mode writing guide — https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md  
5. Ref2VA writing guide — https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md  
6. Raw official base guide — https://github.com/MiniMax-AI/MiniMax-H3/blob/main/skills/h3-prompt-writing/references/base-en.txt  
7. Raw official ref guide — https://github.com/MiniMax-AI/MiniMax-H3/blob/main/skills/h3-prompt-writing/references/ref-en.txt  
8. Video generation guide (API) — https://platform.minimax.io/docs/guides/video-generation  
9. Create-task API reference — https://platform.minimax.io/docs/api-reference/video-generation-v2-create  
10. H3-Context-IR API — https://platform.minimax.io/docs/api-reference/video-generation-v2-h3-context-ir  
11. H3-Regenerate-2K API — https://platform.minimax.io/docs/api-reference/video-generation-v2-regeneration  
12. H3 feature / cookbook entry — https://platform.minimax.io/docs/guides/video-prompt  
13. Official still-image API — https://platform.minimax.io/docs/guides/image-generation  
14. Still-image T2I reference — https://platform.minimax.io/docs/api-reference/image-generation-t2i  
15. Hailuo playground — https://hailuoai.video/tools/minimax-h3  
16. MiniMax Hub — https://hub.minimax.io  
17. Diffusers MiniMax-H3 pipeline — https://huggingface.co/docs/diffusers/main/en/api/pipelines/minimax_h3  

### Hands-on platforms

18. fal H3 — https://fal.ai/minimax-h3  
19. ComfyUI H3 tutorial index — https://docs.comfy.org/tutorials/video/minimax/minimax-h3  
20. ComfyUI H3 Image Studio — https://github.com/astropuzzo/ComfyUI-MiniMax-H3-Image-Studio  
21. ComfyUI MiniMax H3 Studio (T2I via FL2VA) — https://github.com/thaakeno/ComfyUI-MiniMax-H3-Studio  
22. Diffusers local GUI with T2I/Ref2I tabs — https://github.com/animede/Diffusers_minimax-h3  

### Prompt libraries and explainers (use to learn patterns, then compile into official fields)

23. Awesome MiniMax H3 Prompts (222+ credited clips) — https://github.com/xianyu110/awesome-minimax-h3-prompts  
24. joeVenner awesome-minimax-h3 — https://github.com/joeVenner/awesome-minimax-h3  
25. Community prompt skill (r600a-code) — https://github.com/r600a-code/minimax-h3-prompt-skill  
26. EasyWithAI H3 prompt guide — https://easywithai.com/guide/minimax-h3-prompt-guide/  
27. Leadde how-to + prompt guide — https://leadde.ai/blog/how-to-use-mini-max-h3 · https://leadde.ai/blog/mini-max-h3-prompt-guide  
28. DreamPixelForge official-format explainer — https://www.dreampixelforge.com/blog/minimax-h3-prompts  
29. Kapwing creator guide (retention + templates) — https://www.kapwing.com/resources/how-to-prompt-minimax-h3-hailuo-3-0-a-guide-for-ai-video-creators/  
30. Picsart 10-prompt H3 / H3 Max guide — https://picsart.com/blog/minimax-prompting-guide/  
31. Pixo official-formula notes — https://pixo.video/blog/minimax-h3-prompt-guide  
32. Mixio Hailuo H3 structure — https://mixio.studio/hailuo-h3-prompt-guide  
33. Hailuo3.me templates — https://hailuo3.me/blog/minimax-h3-prompt-guide  
34. APIDot cinematic templates — https://apidot.ai/blog/minimax-h3-prompt-guide  
35. ArcLoop H3 vs H3 Max handbook — https://arcloop.ai/handbook/en-US/minimax-h3-guide  
36. Morphic how-to (roles, beats, sound) — https://morphic.com/resources/how-to/minimax-h3-guide  
37. deAPI I2VA alignment-line guide — https://deapi.ai/blog/minimax-h3-image-to-video-prompting-guide-alignment-lines-keyframes-and-3-example-prompts  
38. 226+ prompt gallery — https://apimodels.app/minimax-h3-prompts  
39. MiniMax-H3-Swift PROMPTING.md — https://github.com/loading-awesome/MiniMax-H3-Swift/blob/main/docs/PROMPTING.md  
40. comfy-agent H3 compiler notes — https://github.com/shinshin86/comfy-agent/blob/main/docs/minimax-h3-prompting.md  
41. Civitai structure article — https://civitai.com/articles/34646  
42. ComfyUI Wiki official-skills writeup — https://comfyui-wiki.com/en/news/2026-08-10-minimax-h3-official-skills  

### How to study those libraries

Do not paste community prompts blindly. For each clip you like:

1. Identify the mode (T2VA / I2VA / Ref2VA).
2. List every attached file and guess its job.
3. Rewrite the community paragraph into official fields.
4. Run your rewrite and the original side by side.
5. Keep a personal “compiler memory”: 20 prompts that survived contact with the model, tagged by mode.

That loop is how you teach *your* agent. The system prompt in §13 is the constitution; your surviving prompts are the case law.

---

## 17. One-page field card (print this)

```
MODE        T2I | T2VA | I2VA | FL2VA | L2VA | Ref2VA
DURATION    4–15 s integer          RATIO  21:9 16:9 4:3 1:1 3:4 9:16
RES         768P draft → 2K regen   EXPAND disabled once compiled

BASE FIELDS
  integrated_multimodal_description
  overall_soundscape
  non_diegetic_music

REF FIELDS
  subject_definitions
  summary
  retention_analysis
  detailed_description
  overall_soundscape
  non_diegetic_music

LABELS      <Subject N> <Picture N> <Video N> <Audio N>
DIALOGUE    (S1) <d>[Lang] verbatim</d>
TEXT        "exact glyphs"
CAMERA      type + with small/large amplitude + at slow/fast speed
RETAIN vis  fully_preserved | partially_preserved | attribute_transfer | weak_reference
RETAIN aud  fully_copy | partially_copy | reference | weak_reference
NO SCORE    non_diegetic_music: N/A
SILENCE     overall_soundscape: N/A

IMAGE ROLES
  first_frame / last_frame   pixel lock
  reference_image            identity / product / style   (do not mix with first_frame)

STILL COMPANION
  image-01  prompt ≤1500  n=1–9  prompt_optimizer off for locked briefs
```

---

## 18. Source trail

Primary specifications in this guide come from MiniMax’s own materials dated July–September 2026: the H3 research post, the Hugging Face model card, `skills/h3-prompt-writing` (`base-en.txt`, `ref-en.txt`, `SKILL.md`), platform video-generation and image-generation docs, and the create-task API schema. Community measurements (VRAM, Image Studio canvases, CFG-distilled behavior, partner seed notes) are marked as local/community where they are not in the official schema.

Official hosted H3 does not currently expose a still-image endpoint. Still-image control on H3 is: generate the still elsewhere or locally, assign it a legal role, and write the official document around that role.

That is the whole control surface.
