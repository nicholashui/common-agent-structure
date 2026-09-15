# Grok Imagine Operation Guide

**Complete prompt-engineering and control manual for xAI Grok Imagine (image + video)**

| Field | Value |
|---|---|
| Version | 1.0 |
| Last verified | 2026-09-15 |
| Current image model | `grok-imagine-image-2.0` (Quality Mode) |
| Current video model | `grok-imagine-video-1.5` |
| Audience | Operators who want deterministic control, not lucky one-shots |
| Deliverable | This file is the working spec. Copy templates. Do not invent extra syntax. |

---

## 0. How to use this guide

Read sections 1–3 once. After that, operate from the SOP checklists:

- **Still image from an idea** → §6
- **Edit / restyle / composite** → §7
- **Readable text on the image** → §8
- **Animate a still into video** → §9
- **Video from text only** → §10
- **Make Grok write the Imagine prompt for you** → §13
- **Style recipes (wuxia, anime, cinematic, product, YT, HK night)** → §14
- **Something went wrong** → §15

xAI does **not** publish an official Imagine prompting guide. What follows is synthesized from official docs, the official XCreators consumer guide, the Image 2.0 announcement, API parameter pages, and field-tested community references (listed in §18). Where sources disagree, the guide states both and gives the operational rule.

---

## 1. Mental model — you are briefing a director of photography

Grok Imagine is not Midjourney, Flux, or Stable Diffusion. It does not want tag soup.

**The model responds to a shot brief written in natural English.**

| Other generators | Grok Imagine |
|---|---|
| Keyword stacks: `woman, park, cinematic, 8k, masterpiece` | A sentence a photographer could shoot from |
| `--ar 16:9 --stylize 250 --no text` | Aspect ratio is a **parameter**, not prompt text |
| Separate `negative_prompt` field | No negative-prompt field. Phrase the desired state. Short “no X” only at the end |
| Seeds for reproducibility | No public seed. Control by locking the still, then editing one variable |
| Style presets | Named references inside the sentence: “Blade Runner palette”, “85mm f/1.4” |

The single most important image rule:

> **Front-load the subject.** The first 20–30 words carry the most weight. If you bury the subject under style adjectives, you get a generic stock image.

The single most important video rule:

> **The still carries composition, lighting, and style. The video prompt only describes what changes.** Dial the frame first. Then animate.

Official one-liner from xAI’s Video 1.5 preview (the closest thing to official prompt advice that exists):

> Direct the shot with natural-language prompts. Describe the camera move, the pacing, and the sound design, then set your resolution and clip length.

---

## 2. Surfaces and access

### 2.1 Where Imagine lives

| Surface | URL / location | Best for |
|---|---|---|
| Web Imagine | [grok.com](https://grok.com) → Imagine tab, or [grok.com/imagine](https://grok.com/imagine) | Quality Mode, Smart Resize, Magic Wand, templates |
| Grok iOS / Android | Imagine tab | Same core controls + video motion modes |
| Grok chat | Ask Grok to generate an image inside a conversation | Fast drafts; Grok writes the prompt unless you demand verbatim |
| Imagine Agent / canvas | `grok.com/imagine/agent` (where available) | Multi-step projects, region edits, series consistency |
| API | `https://api.x.ai/v1/images/generations` and `/v1/images/edits`; video at `/v1/videos/generations` | Production pipelines, batch, exact parameters |
| Console | [console.x.ai](https://console.x.ai) | API keys |

Paid plan required for Imagine (free-tier Imagine was removed 19 Mar 2026). SuperGrok / SuperGrokPro unlocks Quality Mode and higher limits.

### 2.2 Consumer image modes

| Mode | What it is | Use when |
|---|---|---|
| **Speed / Fast** | Older / cheaper image path (`grok-imagine-image` 1.0 lineage) | Drafts, memes, volume exploration |
| **Quality** | `grok-imagine-image-2.0` since 7 Aug 2026 | Finals, typography, photorealism, precise edits |
| **Think Harder** | Upgrade a Speed result toward Quality fidelity | Direction is right, detail is not |

Image 2.0 Quality Mode extras in the consumer UI:

- Magic Wand (edit the region you point at)
- Segmentation (select an area, change only that)
- Background removal with transparent export
- Multi-reference (upload several images; consumer guide historically said up to 7 with `@` tagging)
- Smart Resize (recomposes into a new ratio instead of cropping)
- Workflow templates: product, headshot, icon, game asset, merch, UGC, collage, mascot, BG change

### 2.3 Consumer video motion modes

| Mode | Behavior |
|---|---|
| Normal | Restrained motion, close to the source frame |
| Fun | Playful / exaggerated motion |
| Custom | You write the motion and camera instructions |
| Spicy | Age-gated, paid, more permissive creative setting. Still subject to xAI Acceptable Use Policy. Not a jailbreak. |

Spicy is a **render mode**, not a chat personality. It typically appears after you have an image and tap Make Video. Enabling it also requires content-preference toggles (display sensitive media + allow sensitive media generation) and age verification. Availability varies by region and plan. Confirm in your own Settings.

### 2.4 Policy constraints (non-negotiable)

xAI Acceptable Use Policy (read the live page before shipping work): [https://x.ai/legal/acceptable-use-policy](https://x.ai/legal/acceptable-use-policy)

Hard blocks that matter for operators:

- Do not generate sexual / nude / revealing imagery of **real identifiable people**, and do not undress or “nudify” photos of real people.
- Do not deceptively impersonate a real person.
- Do not generate CSAM or any sexual content involving minors (including fictional minors).
- Do not remove watermarks or provenance.
- Do not use Imagine to circumvent safeguards.

Operational workaround for *benign* celebrity / brand filters: describe a **fictional** character with visual traits, not a real name. Generalize logos. This is for avoiding false-positive filters on legal work, not for impersonation.

Hong Kong and other jurisdictions add local law on top of xAI policy. Follow both.

---

## 3. Current models and hard parameters

Verify live values on [docs.x.ai](https://docs.x.ai/developers/model-capabilities/images/generation) before locking a pipeline. Snapshot as of 15 Sep 2026.

### 3.1 Image models

| Slug | Role | Notes |
|---|---|---|
| `grok-imagine-image-2.0` | **Use this** | Quality Mode. Instruction fidelity, typography, edit preservation. Optional `quality` param. |
| `grok-imagine-image` | Speed / 1.0 | Cheaper drafts. Not affected by the Nov 2026 quality-slug retirement. |
| `grok-imagine-image-quality` | Legacy | Retires **2 Nov 2026**. After that, requests redirect to 2.0 with `quality=low`. Do not start new work on this slug. |
| `grok-imagine-image-pro` | Dead | Redirected May 2026. Do not use. |

### 3.2 Image generation parameters

| Parameter | Values | Default | Where it belongs |
|---|---|---|---|
| `prompt` | Natural-language shot brief | required | Prompt box / API body |
| `model` | `grok-imagine-image-2.0` | — | Parameter, not prompt text |
| `aspect_ratio` | See table below | `auto` | Parameter. Do **not** write “16:9” inside the prompt unless you also set the param |
| `resolution` | `1k` \| `2k` | `1k` on official API when omitted | Parameter |
| `quality` | `low` \| `medium` \| `auto` (2.0 only) | `auto` | Parameter. Auto currently = **low for generation, medium for editing**. You are billed at the quality served. |
| `n` | 1–10 | 1 | Same prompt, multiple variations |
| `response_format` | `url` \| `b64_json` | `url` | URLs are **temporary**. Download immediately. |

**Aspect ratios (official API table)**

| Ratio | Use |
|---|---|
| `1:1` | Social grid, thumbnails, icons |
| `16:9` / `9:16` | YouTube / desktop vs Stories / Reels / TikTok |
| `4:3` / `3:4` | Presentations, classic portraits |
| `3:2` / `2:3` | Photography, editorial |
| `2:1` / `1:2` | Banners, headers, tall posters |
| `19.5:9` / `9:19.5` | iPhone full-bleed |
| `20:9` / `9:20` | Android full-bleed |
| `21:9` | Cinematic widescreen |
| `5:2` | Ultra-wide banners |
| `auto` | Model picks from the prompt |

Consumer UI historically exposes a shorter set (16:9, 9:16, 3:2, 2:3, 1:1). API has the rest. Pick the ratio **before** you generate.

**Resolution + quality operating rule**

1. Iterate at `1k` + `quality=low` (or Speed Mode).
2. Lock the prompt.
3. Final at `2k` + `quality=medium` (Quality Mode).

### 3.3 Image editing parameters

| Mode | Inputs | Notes |
|---|---|---|
| Single edit | 1 source image + instruction | Source = public URL, `data:` URI, or Files API `file_id`. Output AR follows input unless you override. |
| Multi-image edit | 2–**5** source images (official multi-edit page, Aug 2026) | Order in the request matters. Default AR = first image. Consumer app + older XCreators guide mentioned up to 7 with `@` tagging. Design pipelines around **5**. |
| Multi-turn | Feed each output back as the next input | Change **one** thing per turn. |

OpenAI SDK `images.edit()` is **not** supported (it sends multipart; xAI wants JSON). Use `xai_sdk`, Vercel AI SDK, or raw HTTP.

### 3.4 Video models and parameters

| Slug | Role |
|---|---|
| `grok-imagine-video-1.5` | **Use this.** Native 1080p on T2V and I2V. First+last frame pin. Reference images + voices. |
| `grok-imagine-video` | Classic / cheaper path |

| Setting | Documented value |
|---|---|
| Duration (generate) | 1–15 seconds |
| Duration (edit) | Not configurable. Inherits input. Input cap **8.7 s**. Output capped 720p. |
| Duration (extend) | Input 2–15 s. Adds **2–10 new seconds** (default 6). Output capped 720p. |
| Aspect ratio | `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`. Default `16:9`. I2V follows the still unless overridden. |
| Resolution | `480p` (default), `720p`, `1080p`. 1080p = T2V + I2V on 1.5 only. Reference-to-video capped 720p. |
| Audio | On by default. `generate_audio=false` for silence. |
| Reference images | Up to **7**. Tag in prompt as `<IMAGE_1>`, `<IMAGE_2>`, … |
| Preset voices | Up to **3**. Tag as `<AUDIO_0>`, `<AUDIO_1>`, `<AUDIO_2>`. |
| First + last frame | `image` pins first frame. `last_frame` pins last frame. Model interpolates. Prompt optional if frames do the work. |

Indicative API pricing (confirm live): image 2.0 from about $0.04/image depending on resolution/quality; video 1.5 billed per output second and resolution. See [docs.x.ai/developers/pricing](https://docs.x.ai/developers/pricing).

---

## 4. Image prompt grammar

### 4.1 The five-layer brief (canonical)

This is the official XCreators consumer structure, confirmed by Image 2.0 community guides. Write it as **one flowing paragraph**, not a bullet list.

```
[1 SUBJECT + attributes + action],
[2 ENVIRONMENT: place, time, weather, one anchoring prop],
[3 CAMERA / LIGHT: shot size, angle, lens, light source + direction + quality],
[4 STYLE / MOOD: medium, named reference, color grade],
[5 FINISH + CONSTRAINTS: DoF, grain, texture, exact quoted text, short avoids]
```

**XCreators canonical example (keep this in muscle memory):**

> A street vendor arranging dried flowers at a wooden cart on a cobblestone alley in Lisbon, late afternoon, warm golden light raking across the scene from the right, medium shot at eye level, slight lens flare, faded vintage color grade, shallow depth of field

Compare to the coin-flip version of the same idea: `a flower seller in a European city`.

### 4.2 Slot-by-slot — what “control” actually means

#### Layer 1 — Subject

Answer four questions before you type:

1. What should a viewer notice first?
2. What is that subject doing?
3. Which 2–3 details make it recognizable (material, age, garment, condition)?
4. What must stay **out** of the frame?

| Weak | Strong |
|---|---|
| a car | matte black EV hatchback, three-quarter front view, doors closed |
| a woman in a park | 30-year-old East Asian woman in a camel wool coat walking a Tokyo park path under golden autumn maples |
| a sword | long guan dao with a worn crimson tassel, blade catching dawn light |

Do not inventory every pore. Two or three identifying details beat a laundry list.

#### Layer 2 — Environment

Place + time + weather + one object that proves the place is real.

- “wet Tokyo alley at night, neon reflections on asphalt”
- “rocky ridge above an alpine lake, wind tearing at a yellow rain shell”
- “cha chaan teng booth, Formica table, condensed milk tin, afternoon ceiling fan”

#### Layer 3 — Camera and light

This is the highest-leverage pair. If you skip them, the model invents a snapshot.

**Camera — name three things:** shot size, height/angle, lens feel.

**Light — name three things:** source, direction, quality.

Never write “nice light” or “cinematic lighting” as the only lighting clause.

#### Layer 4 — Style / mood

Use a **named reference**, not a lone adjective.

| Lone adjective (weak) | Named reference (strong) |
|---|---|
| dark and moody | film noir lighting, deep shadows, desaturated except for a single red accent |
| cinematic | anamorphic 35mm still, teal-orange grade, mild halation |
| anime | 1980s OVA cel, thick key lines, painted background, grain on the sky |
| wuxia | early-2000s Hong Kong wuxia film still, silk in wind, ink-wash mountains behind |

Commit to **one** aesthetic. “Cyberpunk watercolor Renaissance photograph” fights itself.

#### Layer 5 — Finish + constraints

Finishing details give the image a point of view:

- Depth of field: `shallow 85mm` vs `everything sharp, 24mm`
- Grain / stock: `Kodak Portra 400` / `Fujifilm color science` / `clean digital`
- Texture: `visible fabric weave` / `condensation on glass` / `spray-paint stencil edge`
- Layout: `clean negative space in the upper third for a headline`

Constraints go **last**, short, positive-first:

> sharp focus, natural skin texture, no watermark, no extra fingers, no brand logos

### 4.3 Word count and language

| Source | Recommendation |
|---|---|
| Picsart field guide | 30–80 words. Shorter = under-specified. Longer = lost focus. |
| Community GitHub refs | 50–200 words for complex videos / posters. Cap rambling. |
| Operational rule | Simple subject: 30–50 words. Poster / multi-element / style transfer: 60–120 words. Every clause must change a visible decision. |

**Write the prompt body in English.** Notes, titles, and your own comments can be in any language. English shot language is the most reliable for this model family in 2026.

### 4.4 Negatives — the honest rule

There is **no** `negative_prompt` API field.

Sources disagree on trailing “no X”:

- Picsart / Prompt Architects: classic negatives are ignored; rewrite as the desired state (`smooth clear skin` not `no blemishes`).
- Image 2.0 community guides: a short trailing list (`no watermark, no extra text, no fake logos`) does reduce junk.

**Operate like this:**

1. Describe what **is** in the frame.
2. Put a short avoid list at the **end**, never mid-sentence.
3. If a mistake repeats, add one more specific avoid (`no extra fingers`, `no second head`).
4. Never paste a Midjourney-style paragraph of `--no` tokens.

### 4.5 Reusable image template

```
[subject doing something] in [setting], [time of day and light],
[composition and camera position], [important material or color details],
[mood / named reference], [visual medium or finish],
[exact text "LIKE THIS" if any], [no watermark, no extra text]
```

Product variant:

```
[style] photo of [product + material + color] [action/placement] on [surface]
in [setting], [light recipe], [lens + angle + framing],
[negative space instruction], [commercial/editorial finish],
no text, no brand logos, no watermark
```

---

## 5. Control vocabulary (the operator word bank)

Use these instead of empty praise words (`stunning`, `breathtaking`, `8K`, `masterpiece`, `ultra-detailed`).

### 5.1 Shot size

| Term | What the frame contains |
|---|---|
| extreme close-up | eyes, lips, a product detail |
| close-up | head and shoulders |
| medium close-up | chest up |
| medium shot | waist up |
| cowboy / three-quarter | mid-thigh up |
| full body | head to toe with ground |
| wide / establishing | subject small in environment |
| extreme wide | landscape dominates |
| overhead / flat lay / top-down | camera above, looking down |
| aerial / drone | high above |

### 5.2 Camera height and angle

`eye level` · `low angle looking up` · `high angle looking down` · `worm’s eye` · `bird’s eye` · `dutch angle` · `over-the-shoulder` · `profile` · `three-quarter view` · `straight-on` · `from across the street`

### 5.3 Lens language (photoreal lever)

| Phrase | Look |
|---|---|
| 24mm wide, straight verticals | architecture, environment |
| 35mm documentary | street, candid |
| 50mm natural | “what the eye sees” |
| 85mm f/1.4, shallow DoF | portrait, subject separation |
| 100mm macro | food, product texture |
| anamorphic, horizontal flares | cinema |
| tilt-shift | miniature / selective plane |
| locked off on sticks | no handheld sway |

Naming a camera body (`shot on a Sony A7R V with an 85mm f/1.2`) is more useful than writing `photorealistic`.

### 5.4 Light recipes

Always: **source + direction + quality**.

| Recipe | Result |
|---|---|
| golden hour backlight, rim on hair and shoulders | hero glow |
| warm late-afternoon side light from camera right | form + texture |
| soft window light from the left, no harsh shadows | editorial / beauty |
| overcast diffused, even, low contrast | honest documentary |
| single hard spotlight from camera left, deep shadow right | noir / drama |
| Rembrandt lighting, triangle on the shadow cheek | classic portrait |
| three-point studio: key + fill + rim | catalog product |
| overhead fluorescent, slight green cast | office / institutional |
| neon bounce off wet asphalt, mixed color temperatures | night street |
| practical lamps only, warm interior, falloff into dark | night interior |
| noon hard sun, short sharp shadows | brutal daylight |
| moonlight + one warm practical | night wuxia / fantasy |

### 5.5 Motion and pose (stills)

Stills still need an action verb. `mid-stride`, `hands wrapped around a mug`, `blade held across the body`, `looking just past camera`, `coat lifted by wind`.

Describe the **mechanics of an expression**, not the emotion word:

- Weak: `sad old man`
- Strong: `elderly man at a kitchen table, both hands around a mug, eyes looking slightly past camera, mouth neither smiling nor frowning`

### 5.6 Finish / grade / stock

`Kodak Portra 400` · `Kodak Ektar 100` · `Fujifilm color science` · `70s Kodachrome` · `muted film tones` · `teal-orange grade` · `bleach bypass` · `faded vintage` · `clean commercial digital` · `soft film grain` · `halation on highlights` · `painterly brushstroke` · `risograph misregistration` · `ink-wash wash behind photoreal subject`

### 5.7 Words that usually waste tokens

`stunning` · `breathtaking` · `beautiful` · `gorgeous` · `8K` · `4K` · `ultra-detailed` · `masterpiece` · `best quality` · `award-winning` · `trending on Artstation` · `cinematic` **used alone** · `photorealistic` **used alone**

Replace each with a camera, light, or material fact.

---

## 6. Image generation SOP (text-to-image)

### 6.1 Pre-flight (30 seconds)

1. Write one sentence: *what must the viewer notice first?*
2. Pick aspect ratio from the destination (YT thumb = 16:9, Shorts = 9:16, poster = 2:3, product hero = 4:5-ish → use 2:3 or 3:4).
3. Pick mode: Speed to hunt, Quality to finish.
4. Decide whether text will live **in** the image or be overlaid later. Overlay later is safer unless you need Image 2.0 typography.

### 6.2 Write the brief

Fill the five layers. Read it aloud. If a photographer would ask a question, put the answer in.

### 6.3 Generate

- First run: one image, not ten.
- Score four boxes: subject / light / style / text.
- If the idea is right but the sample is wrong, **rerun the exact same prompt 2–3 times** before rewriting. Imagine is stochastic. XCreators official advice: the keeper is often one or two rolls away.

### 6.4 Controlled variation

Change **one slot per run**:

| Run | What you change |
|---|---|
| A | Base prompt |
| B | Light only (side → backlight) |
| C | Lens only (35mm → 85mm) |
| D | Grade only (Portra → teal-orange) |
| E | Crop / negative space |

If you change five things, you learn nothing.

### 6.5 Promote to final

When the brief is locked:

- Quality Mode / `quality=medium` / `resolution=2k`
- Or Speed result → Think Harder
- Save the **prompt + settings + output** together. The prompt is the asset.

### 6.6 Worked examples

**Vague → specific (the money comparison)**

Vague:

```
a woman in a park
```

Specific:

```
30-year-old East Asian woman in a camel wool coat walking through golden autumn maple trees on a Tokyo park path, warm late-afternoon side light, 85mm shallow depth of field, cinematic color grade, natural skin texture, elegant magazine photography, no watermark
```

**Product hero**

```
Premium product photo of a matte black wireless headphone pair on a seamless soft gray sweep, three-point studio light with a gentle rim, crisp material detail on the ear cushions, centered three-quarter view, commercial catalog style, sharp focus, clean negative space on the left for a headline, no text, no watermark, no logos
```

**Editorial portrait (XCreators)**

```
close-up portrait, strong directional light from a window on the left, deep shadows on the right side of the face, natural skin texture, shallow depth of field, desaturated tones, Vanity Fair cover energy
```

**YT thumbnail with overlay space (XCreators)**

```
dramatic low-angle shot of a figure silhouetted against a stormy sky, strong contrast, open space in the upper third for text overlay, cinematic color grade, bold composition
```

**Photoreal product in a real street (SuperGrok.tech pattern)**

```
Realistic product photo of a matte black electric scooter parked beside a curb on a wet Tokyo side street at night. Neon signs reflect in the road. Low camera angle, 50mm lens, three-quarter front view, soft street lighting, crisp details, no text, no brand logos, no distorted wheels, leave clean space in the upper left for a headline.
```

---

## 7. Image editing SOP (the real control surface)

Image 2.0 was built so **editing is first-class**. Most “I can’t control Imagine” problems are people regenerating instead of editing.

### 7.1 Decision tree

```
Is the composition / camera / identity already good?
  YES → region edit or single-instruction edit (do not regenerate)
  NO  → regenerate from an improved brief
Is only the background wrong?
  YES → BG removal, then new background edit
Is the ratio wrong?
  YES → Smart Resize (recomposes). Do not crop a finished hero if you can resize.
Do you need two subjects / a product on a set / a style match?
  YES → multi-reference edit
```

### 7.2 Single-image edit pattern

Editing prompts are **imperative**. Describe the change. Do **not** re-describe the whole photo — that gives the model permission to reinterpret it.

```
Keep [identity / pose / camera / composition] completely unchanged.
Change only [X].
Re-balance lighting and shadows so the new element belongs.
Keep [Y] sharp and unaltered.
```

Examples:

```
Give the subject a silver necklace and change the background to a softly blurred autumn park. Keep face, pose, and camera unchanged.
```

```
Render this image as an oil painting in the style of impressionism. Preserve composition and subject identity.
```

```
Render this as a pencil sketch with detailed shading.
```

```
Change only the jacket color to deep indigo. Keep the face, hands, background, and lighting unchanged.
```

Official style-transfer targets that work as clauses: oil painting, pencil sketch, pop art, anime, watercolor. Go deeper than the one-word label (`visible brushwork, broken color, luminous plein-air surface`).

### 7.3 Multi-reference / composite

API: pass 2–5 images in order. First image sets default aspect ratio.

Prompt pattern:

```
Place the product from image 1 onto the surface in image 2, matching the lighting and color grade of image 2. Keep the product label sharp and unchanged. No extra people.
```

```
Show all subjects sitting together on the grass in a sunny park. Casual relaxed mood, natural daylight, warm tones. No additional people or animals.
```

Consumer app: upload refs, then `@` tag a specific image when you need to bind one subject to one file.

Video reference-to-video uses a different syntax (`<IMAGE_1>`). Do not mix that syntax into still-image API calls.

### 7.4 Multi-turn discipline

One change per turn. Example chain:

1. Generate clean living room, city windows.
2. Edit: replace the sofa with a mid-century leather sofa. Keep windows and floor.
3. Edit: warmer late-afternoon light from the left. Keep furniture.
4. Edit: add a ceramic lamp on the side table. Keep everything else.
5. Smart Resize to 16:9 if it will be a YouTube still.

Save every keeper. The chain is your reproducibility.

### 7.5 Region tools (Quality Mode UI)

| Tool | When |
|---|---|
| Magic Wand | One object / one region is wrong |
| Segmentation | You need a clean mask (hair, product edge) |
| Background removal | Subject is good, environment is not |
| Smart Resize | Same image, new destination ratio |

Prompt for a region pass the same way as a single edit: name the region, name the change, name what stays.

---

## 8. Typography and on-image text

Image 2.0’s headline feature is that it **plans type and layout before rendering**. Small text is usable in a way older Imagine was not. It is still not InDesign.

### 8.1 Rules that actually work

1. Put the exact string in **quotes**: `exact text "SUMMER SALE"`.
2. Keep each text layer to **2–6 words**.
3. State hierarchy: large headline / smaller subline / tiny footer.
4. Describe type loosely (`bold condensed sans`, `hand-painted wood letters`), not a licensed font name you do not have rights to reproduce as a brand mark.
5. Ask for `sharp small text` and `clean margins`.
6. Proofread every character in the output. Do not ship generated prices, legal copy, or citations from Imagine.
7. If the text is long (paragraph, T&Cs, lyrics), generate the image **without** text and composite in a design tool.

### 8.2 Poster template

```
Editorial poster, large exact text "PROMPT CRAFT", smaller exact text "Subject → Light → Style", modern Swiss graphic design, coral and teal geometric shapes on cream paper texture, strong hierarchy, sharp small text, clean margins, no fake logos, no watermark
```

### 8.3 Environmental text

```
A hand-painted wooden sign outside a small coffee shop reading "Open Early, Closed Late", weathered paint, warm afternoon sunlight, shallow depth of field behind the sign
```

---

## 9. Image-to-video SOP (the default video workflow)

This is the highest-control video path.

### 9.1 Core principle

> The image carries composition, lighting, and style.
> The prompt only describes what changes.

If you re-describe the photo in the video prompt, the model treats it as permission to rebuild the first frame.

### 9.2 Pipeline

1. Generate or shoot a still until composition, light, identity, and costume are locked. Quality Mode / 2k if it will be published.
2. Use that still as the first frame (`image` / I2V / Make Video).
3. Write a **short shot brief**: one action, one camera move (or locked), named sound.
4. Duration 5–8 s for a single beat. 10–15 s only if the action is slow and simple.
5. If the end must land on a specific frame, pin `last_frame`.
6. If identity must survive a new location, use reference-to-video with `<IMAGE_n>` rather than hoping T2V remembers a face.

### 9.3 I2V prompt skeleton

```
Hold the composition, subject identity, colors, and camera angle exactly.
[One concrete action, with intensity].
Camera: [locked / slow push-in / drift left] — only one move.
Pacing: [calm / accelerating / held].
Sound: [named sources, materials, “no music” if you do not want a score].
Nothing else changes. No new people, no warping, no text overlay.
```

Good I2V prompts:

```
Use this image as the first frame. Keep the room layout, main subject, colors, and camera angle consistent. Add only a slow camera push-in and subtle movement in the curtains. No new people, no text, no object warping, no fast cuts.
```

```
Hold the composition exactly. The woman turns her head six inches to the left and her eyes follow. Hair moves slightly. Camera stays locked. Nothing else changes.
Sound: quiet room tone, fabric rustle. No music.
```

### 9.4 Camera moves that work (one per clip)

`locked, static` · `slow push-in` · `slow pull-out` · `aerial push-in toward` · `camera drifts gently to the left` · `tracking shot alongside` · `slow pan` · `slow tilt` · `handheld tracking, slight sway` · `crane up a few feet`

Stacking two moves in six seconds produces warping. “Cinematic camera” is not a move.

### 9.5 Intensity modifiers

The model under-plays verbs unless you scale them.

| Weak | Strong |
|---|---|
| The wave crests | The wave crests fully and pitches forward, crashing down with tremendous force |
| He skateboards | He starts skateboarding slowly, then goes faster, then is going very fast; background streaks |
| She smiles | She smiles gently, then the smile widens as she looks into the lens |

### 9.6 Focus rule

Give the clip **two or three beats**, not a plot.

- Touch cheek → small smile → wider smile to camera
- Draw the guan dao → one step forward → cloth settles
- Steam rises → camera eases in → screen reflection steadies

Lock everything that is not a beat.

---

## 10. Text-to-video SOP

Use T2V only when you have no plate. The prompt now has two jobs: build the first frame **and** animate it. Front-load composition the same way you would for an image, then attach motion + sound.

### 10.1 T2V skeleton

```
[Subject and what it is doing]
[Setting, time of day, one concrete anchoring detail]
[Camera: shot size, lens feel, ONE movement]
[Light: source, direction, quality]
[Motion pacing]
[Audio: what should be heard]
[One grade or film-reference clause]
```

### 10.2 Example (Replicate / community pattern)

```
A young woman in a red raincoat stands on a neon-lit Tokyo side street, slowly turning her head toward the camera. Slow push-in camera movement. Light rain falls, reflections ripple on the pavement, distant traffic glows in the background. Moody cinematic night lighting. Photorealistic.
Sound: rain on packed nylon, wet tires on asphalt, a distant crosswalk chirp, no music.
```

### 10.3 First + last frame

When you can afford two stills, pin them.

```
image:       opening still
last_frame:  closing still
prompt:      The camera dollies from the sunlit doorway to the window, settling on the closing frame.
duration:    8
```

If the two frames already tell the story, the prompt can be only the camera path.

### 10.4 Reference-to-video

Up to 7 images, 3 voices. Prompt with tags:

```
The person from <IMAGE_1> presents the product from <IMAGE_2> on the set from <IMAGE_3>, speaking with the voice from <AUDIO_0>. Medium close-up, locked camera. Soft key from camera left. Room tone under the dialogue, no music.
```

1080p is not available in this mode (720p cap). Plan for that.

### 10.5 Extend and edit

- **Extend:** input 2–15 s, add 2–10 new seconds from the last frame. Prompt only what happens next.
- **Edit:** input ≤ 8.7 s. Imperative instruction (`Give the woman a silver necklace`). Duration and AR inherit. Cap 720p.

---

## 11. Sound design (Video 1.5)

Audio is generated in the **same pass** as motion and is on by default. Unspecified audio becomes generic music on a large fraction of clips. Write sound like a sound designer.

### 11.1 Pattern

```
Sound: [event that is visible], [material texture], [off-screen bed], [dialogue in quotes], [no music / no score if you do not want one]
```

| Vague | Specific |
|---|---|
| Sound: city sounds, traffic | Sound: cars passing by, skateboards rolling on pavement, teenagers laughing, the distant rumble of a street |
| ambient cafe | espresso machine hiss, cup on saucer, muffled traffic through glass, no music |
| she talks | she says "Welcome" — quote the exact line |

Useful legal cues: `no music`, `camera not moving` (this is both picture and sound — it kills whoosh and score).

### 11.2 Full example (Replicate)

```
The wave crests fully and pitches forward, the translucent green crest folding and crashing down onto the dark rocks with tremendous force. White foam explodes upward and outward, hanging for a moment before collapsing back. Sea spray drifts across the frame in the dawn wind. The water rushes back off the rocks in white rivulets. A second smaller wave rises behind.
Sound: the deep boom of a heavy swell hitting rock, the hiss and rush of water pulling back across stone, the low moan of wind across an open coastline, sea spray on a microphone.
```

API silence: `generate_audio: false`.

---

## 12. Iteration loop and quality gates

### 12.1 The 10-minute loop

1. Save the best output and its exact prompt + settings.
2. Write the failure in **one sentence** (“hands are melted”, “type is soft”, “camera drifted”).
3. Keep every clause that worked.
4. Change one or two variables.
5. If the same mistake repeats, add one constraint at the end.
6. Prefer region edit over full regen when composition is good.
7. Stop when the frame is useful enough for the next human step (overlay, edit, animate, publish).

### 12.2 Quality gate checklist (images)

- [ ] Subject is the first thing you see
- [ ] Light has a named source and direction
- [ ] Hands / fingers / eyes survive a 100% crop
- [ ] On-image text is spelled correctly (or there is no on-image text)
- [ ] No watermark, no phantom logo, no extra limb
- [ ] Ratio matches the destination
- [ ] Prompt is saved next to the file

### 12.3 Quality gate checklist (video)

- [ ] First frame is a still you already approved
- [ ] One action, one camera move
- [ ] Identity holds for the full duration
- [ ] Physics of cloth / hair / water is acceptable
- [ ] Sound matches visible events (or is intentionally silent)
- [ ] No morph at the end of the clip
- [ ] Duration matches the beat (do not pad)

### 12.4 Troubleshooting matrix

| Symptom | Likely cause | Fix |
|---|---|---|
| Generic stock photo | Subject buried or underspecified | Front-load concrete subject + light + lens |
| Random framing | No camera language | Add shot size + angle + lens |
| Flat light | “cinematic” with no recipe | Name source, direction, quality |
| Style soup | Two aesthetics in one brief | Commit to one reference |
| Soft / wrong on-image text | Paragraph of copy, or Speed Mode | 2–6 words in quotes, Quality Mode, or composite later |
| Watermark / junk glyphs | No trailing constraint | End with `no watermark, no extra text` |
| Identity drift on edit | Prompt re-described the whole scene | Imperative change + explicit “keep face/pose/camera” |
| Video warps | Two camera moves or too many actions | Lock camera or pick one move; freeze the rest |
| Video ignores the still | I2V prompt rebuilt the scene in words | Delete visual description; keep only change + sound |
| Random score | No Sound: clause | Write Sound: or set `generate_audio=false` |
| Celebrity / brand filter | Named real person or logo | Fictional descriptor; generic packaging |
| Hands fail | Hands are hero of the frame | Crop hands out, or give them a simple rest pose |
| “Masterpiece” did nothing | Adjective spam | Delete it; add a material or lens fact |

---

## 13. Teach an AI to write Grok Imagine prompts

This is the official recommended workflow: **Grok chat writes the Imagine prompt; Imagine renders it.** Justine Moore and Elon Musk both stated this publicly in April 2026. XCreators built it into the consumer guide.

You will run two layers:

1. A **prompt engineer** (Grok chat, a Grok Project, or any LLM given the instructions below).
2. A **renderer** (Imagine Quality Mode / API).

Never skip layer 1 on complex work. The LLM is better at filling missing layers than you are at remembering them under deadline.

### 13.1 Fast method (no Project)

In a normal Grok chat:

```
Turn the following idea into a production-ready Grok Imagine prompt.
Use five layers in one flowing paragraph: subject, environment, light, camera, finish.
Do not use Midjourney tag syntax. Do not use words like 8K, masterpiece, ultra-detailed.
Recommend Quality vs Speed and an aspect ratio.
Idea: [plain language]
```

Paste the returned prompt into Imagine. Generate. If it is close, send the image back to chat:

```
Here is the output. The problem is: [one sentence].
Rewrite only the clause that fixes that. Keep everything else.
```

### 13.2 Grok Project method (best for a personal or brand library)

Create a Grok Project. Paste the following into Project Instructions. This is the field-tested “Imagine prompt engineer” brief published by @lamps_apple after the official XCreators guide, adapted here so it also covers Image 2.0 and Video 1.5.

```
You are a specialized prompt engineer for Grok Imagine, xAI's image and video generator
(current still model: grok-imagine-image-2.0 / Quality Mode;
 current video model: grok-imagine-video-1.5).

Your sole job is to take a user's idea, concept, or edit request and output a
production-ready Grok Imagine prompt that will generate the best possible result
on the first try.

CORE BEHAVIOR
When the user describes what they want, respond with:
1. The prompt (clearly labeled, ready to copy-paste)
2. Recommended mode (Speed or Quality) and, for video, Normal / Fun / Custom
3. Recommended aspect ratio
4. Recommended resolution / quality (1k low to iterate, 2k medium to finish)
5. Reference-image guidance (what to upload, whether to @ tag or use <IMAGE_n>)
Keep conversational text minimal. The prompt is the deliverable.

PROMPT CONSTRUCTION — FIVE LAYERS (images and T2V first frames)
Every still prompt addresses all five layers in one flowing paragraph.
Layer 1 Subject: concrete nouns, 2–3 identity traits, a visible action.
Layer 2 Environment: place, time, weather, one anchoring object.
Layer 3 Light + camera: named source, direction, quality; shot size, angle, lens.
Layer 4 Mood: named reference (film / stock / movement), not a lone adjective.
Layer 5 Finish: DoF, grain, grade, texture, exact quoted on-image text, short avoids last.

IMAGE EDITING PROMPTS
Do not re-describe the source photo. Write an imperative change.
Always state what must stay unchanged (face, pose, camera, composition, label).
Categories: enhancement, object add/remove, style transform, scene transplant, typography fix.

VIDEO PROMPTS
If a still exists, do not rebuild it in words.
I2V pattern: hold composition + identity; one action; one camera move or locked; Sound: clause.
T2V pattern: five layers first, then motion + sound.
One camera move per clip. Two or three beats, not a plot.
Write Sound: like a sound designer. Say "no music" when a score would hurt.

REFERENCE STRATEGY
Stills API / Quality Mode: up to 5 images in one edit (consumer surfaces may allow more).
Video reference-to-video: up to 7 images as <IMAGE_1>… and up to 3 voices as <AUDIO_0>….
Tell the user what to upload and why.

MODE
Speed = drafts, memes, volume.
Quality = text, photoreal, commercial, anything that will be published.
Think Harder upgrades a Speed keeper.

ASPECT RATIO
16:9 timeline / YT / desktop
9:16 Stories / Reels / Shorts
3:2 editorial
2:3 portrait / Pinterest / poster
1:1 grid / icon
21:9 cinematic (API)
Pick one. Never leave it to auto unless the user asks.

RULES
- Every word does visual work. No 8K / masterpiece / ultra-detailed / best quality.
- No Midjourney --ar --stylize --no syntax. No JSON unless the user asks for an API payload.
- Prompts are one flowing passage, not markdown.
- Simple ideas stay short (30–50 words). Posters, style transforms, and multi-element frames go long and precise.
- Default Quality Mode.
- Always recommend a ratio.
- Prompt body in English even if the user writes in another language.
- If the idea is ambiguous, ask ONE clarifying question, then produce a prompt with stated assumptions.
- Refuse requests that violate xAI Acceptable Use Policy (real-person sexual imagery, undressing real people, CSAM, deceptive impersonation, watermark removal).

OUTPUT FORMAT
**Prompt:**
[copy-paste prompt]

**Mode:** [Speed / Quality]  |  **Aspect Ratio:** [ratio] — [one-line why]
**Settings:** [1k low / 2k medium]  |  **Refs:** [none / what to upload]
**Video add-on (if asked):** [I2V or T2V brief + Sound: + duration]
```

### 13.3 Compact meta-prompt (any LLM)

Use this when you cannot install a Project — Cursor, Claude, local models, another Grok chat.

```
System:
You write Grok Imagine prompts only.
Grammar: subject → environment → camera/light → style → finish + short avoids.
Natural English. No tag stacks. No "8K masterpiece ultra-detailed".
On-image text goes in quotes, 2–6 words per layer.
Edits are imperative and name what stays unchanged.
Video: if a still exists, describe only motion + camera + Sound:.
Return: Prompt, Mode, Aspect Ratio, one-line settings.

User:
[idea]
Destination: [YouTube thumb / Shorts / poster / product / film still]
Must include: [constraints]
Must avoid: [constraints]
```

### 13.4 JSON authoring schema (compile, then flatten)

Grok Imagine itself wants **prose**, not JSON. Do not paste raw JSON into the Imagine box.

Use JSON only as a **writer-side checklist** (Grok Project, Cursor, your own agent). Compile it to one flowing paragraph before render. This is the same compile-to-prose pattern used for Grok / Seedance / Veo shot briefs.

```json
{
  "job": "still | edit | i2v | t2v",
  "destination": "yt-thumb | shorts | poster | product | film-still | icon",
  "ratio": "16:9",
  "mode": "quality",
  "resolution": "2k",
  "quality": "medium",
  "subject": "who/what + two identity traits",
  "action": "visible verb",
  "environment": "place + time + weather + one anchor object",
  "camera": "shot size + angle + lens",
  "light": "source + direction + quality",
  "style": "one named reference / medium / grade",
  "exact_text": ["HEADLINE", "subline"],
  "layout": "headline top third, product lower right, empty upper-left",
  "finish": "DoF, grain, texture",
  "preserve": ["face", "pose", "camera", "label"],
  "change": "only used for edits — the one thing that moves",
  "motion": "only used for video — one action",
  "camera_move": "locked | slow push-in | …",
  "sound": "named sources, or no music",
  "duration_s": 8,
  "avoids": ["watermark", "extra text", "extra people", "logos"],
  "refs": ["what to upload and which image is which"]
}
```

Compile rule: walk the keys in five-layer order and emit **one paragraph**. Drop empty keys. Edits emit `change` + `preserve` only. I2V emits `motion` + `camera_move` + `sound` only.

Still-image official syntax is natural language. Consumer UI uses `@` to bind a specific upload. Video reference-to-video official docs use `<IMAGE_1>` and `<AUDIO_0>`. Third-party gateways that accept `<IMAGE_N>` inside **still** edits are gateway-specific — do not assume that works on `api.x.ai`.

### 13.5 Teach *yourself* the grammar (drills)

Run these until the five layers are automatic.

1. Take any weak prompt you have used. Rewrite it with all five layers. Generate both. Keep the pair.
2. Lock a keeper. Change **only** light. Generate. Change **only** lens. Generate. Label the three files.
3. Take a product photo. Write three edit prompts: color change, background transplant, style transfer. One change each.
4. Take a locked still. Write three I2V briefs: locked camera + cloth motion; slow push-in + no other motion; tracking + one spoken line.
5. Keep a prompt library: `style-wuxia.md`, `style-yt-thumb.md`, `style-product.md`. Reuse the finish clause; swap only Layer 1.

### 13.6 Custom Templates (paid consumer feature)

SuperGrok / Premium+ surfaces let you save reusable Imagine templates (Photo→Video, style edits, shareable). Once a five-layer brief works, save it as a template and only swap the subject. This is the same idea as a Grok Project, on the renderer side.

---

## 14. Style cookbooks

Copy, then swap the subject. All prompts are English on purpose.

### 14.1 Wuxia / guan dao / ink-wash hybrid

Still:

```
A lone swordsman in a weathered slate-blue silk robe stands on a wind-scoured granite ridge above a sea of cloud, a long guan dao planted beside him, crimson tassel lifting in the dawn wind. Thin ink-wash mountains fade behind photoreal rock and cloth. Pale gold backlight rims the blade and the hair. Medium-wide shot, slight low angle, 35mm anamorphic still from an early-2000s Hong Kong wuxia film, fine silk weave visible, no text, no watermark.
```

I2V from that still:

```
Hold composition, costume, and light exactly. The crimson tassel and robe hems stir in a rising mountain wind. The swordsman shifts his weight half a step; the guan dao stays planted. Camera locked. Slow, held pacing.
Sound: high wind across granite, cloth snapping, a distant temple bell, no music.
```

### 14.2 Anime / 80s OVA

```
A young mechanic in an oil-stained flight jacket crouches beside a parked fighter on a dusk tarmac, orange sodium lamps mixed with a purple sky. 1980s OVA look: thick confident key lines, painted gouache background, visible cel grain in the sky, limited shadow colors. Medium shot at eye level, slight wide 35mm, no modern PBR gloss, no text, no watermark.
```

Do not write only `anime`. Name the era and the material (cel, key line, painted bg).

### 14.3 Cinematic still (teal-orange, usable as a plate)

```
Cinematic wide shot of a lone motorcycle rider on a desert highway at blue hour, neon motel signs far away, volumetric dust in the headlights, anamorphic lens flares, teal and orange grade, film still look, 24mm, no text, no watermark.
```

### 14.4 Photoreal portrait

```
A close-up portrait of a woman in her early thirties wearing a charcoal wool sweater, soft window light from the left, shallow depth of field, natural skin texture, calm confident expression, muted earthy color palette, shot on 85mm, no retouch-plastic skin, no watermark.
```

### 14.5 Product / catalog

```
A matte-black ceramic coffee mug centered on a polished concrete surface, single soft key light from upper right, gentle reflection beneath, clean neutral background, premium commercial product photography, sharp focus, empty space on the left for a label, no text, no watermark, no logos.
```

### 14.6 YouTube thumbnail (text will be overlaid later)

```
Dramatic low-angle three-quarter portrait of a focused engineer at a dim workbench, one practical lamp carving the face, shallow depth of field, high contrast, teal shadows and warm key, large empty sky of negative space in the upper third for a headline, 24mm, no on-image text, no watermark, no logos.
```

### 14.7 Hong Kong night street

```
A wet Hong Kong side street at 11pm after rain, red and green neon from a cha chaan teng reflecting on asphalt, steam from a drain, one taxi passing through the background, low-angle 35mm street photograph, mixed color temperatures, light film grain, no readable shop names, no watermark.
```

### 14.8 Food / flat lay

```
Overhead flat-lay of a rustic sourdough loaf, olive oil bottle, and rosemary on warm marble, soft morning window light from the left, shallow depth of field, food magazine style, appetizing color, no text, no watermark.
```

### 14.9 Icon / game prop

```
Isometric fantasy game prop: crystal-hilt dagger on a seamless neutral background, clean game-art style, readable silhouette, limited four-color palette of indigo teal gold ivory, soft rim light, asset-sheet ready, no text, no watermark.
```

### 14.10 Children’s illustration

```
Soft children’s book illustration of a small fox reading under a mushroom, warm watercolor texture, gentle pastel palette, cozy night atmosphere with fireflies, storybook composition, no scary elements, no text, no watermark.
```

### 14.11 Before-edit base (generate this on purpose)

```
Clean studio photo of a red ceramic mug on a white table, soft even light, centered, product-photo simplicity, sharp edges, empty background, no text, no watermark — leave room for later color or logo edits.
```

---

## 15. Anti-patterns

Do not do these. They are the usual reason people say “Imagine won’t listen.”

1. **Tag-stack Midjourney syntax.** `woman, park, cinematic, 8k --ar 16:9 --no text` is the wrong language.
2. **Adjective soup.** `epic cinematic ultra detailed masterpiece` crowds out subject and light.
3. **Burying the subject.** Style words first, subject last.
4. **Writing resolution, duration, or aspect ratio only inside the prompt.** Set the parameter. Mention ratio in the prompt only as composition intent (`wide cinematic frame`) after the param is set.
5. **Re-describing a source photo in I2V or in an edit.** Describe the change.
6. **Two camera moves + four actions in a 6-second clip.**
7. **Mixing clashing aesthetics** in one brief.
8. **Changing five variables between runs.**
9. **Assuming a seed exists.** It does not in the public API. Reproducibility = saved still + saved prompt + one-variable edits.
10. **Named real celebrity or trademarked lockup** when you do not need them. Filters + AUP.
11. **Paragraphs of on-image copy.**
12. **Shipping generated legal text, prices, or UI screenshots as if they were real product evidence.**

---

## 16. API cheat sheet

### 16.1 Text-to-image

```python
import xai_sdk

client = xai_sdk.Client()

response = client.image.sample(
    prompt="A collage of London landmarks in a stenciled street-art style",
    model="grok-imagine-image-2.0",
    aspect_ratio="16:9",
    resolution="2k",
    quality="medium",
)
print(response.url)   # temporary — download now
```

Batch variations of the same prompt:

```python
responses = client.image.sample_batch(
    prompt="A futuristic city skyline at night",
    model="grok-imagine-image-2.0",
    n=4,
)
```

Different prompts in parallel: `AsyncClient` + `asyncio.gather`. Do not fake that with `n`.

### 16.2 Single edit

```python
response = client.image.sample(
    prompt="Render this as a pencil sketch with detailed shading",
    model="grok-imagine-image-2.0",
    image_url="https://example.com/source.png",
)
```

### 16.3 Multi-image edit

```python
response = client.image.sample(
    prompt="Show all subjects sitting together on the grass in a sunny park. Casual relaxed mood, natural daylight, warm tones. No additional people or animals.",
    model="grok-imagine-image-2.0",
    image_urls=["https://.../woman.jpg", "https://.../man.jpg"],
    aspect_ratio="3:2",
)
```

### 16.4 Image-to-video

```python
response = client.video.generate(
    prompt="Generate a slow and serene time-lapse",
    model="grok-imagine-video-1.5",
    image_url="https://example.com/still.png",
    duration=12,
)
print(response.url)
```

Video jobs are asynchronous on raw HTTP: POST `/v1/videos/generations`, then poll `/v1/videos/{request_id}` until `status=done`.

### 16.5 REST image generation

```bash
curl -X POST https://api.x.ai/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -d '{
    "model": "grok-imagine-image-2.0",
    "prompt": "Mountain landscape at sunrise",
    "aspect_ratio": "16:9",
    "resolution": "2k",
    "quality": "medium"
  }'
```

OpenAI-compatible clients work for **generation**. They do **not** work for `images.edit()` multipart. Use JSON.

Check `response.respect_moderation` before you treat a URL as publishable.

---

## 17. Operator one-pagers

### 17.1 Still, from scratch

1. One-sentence intent.
2. Pick ratio.
3. Write five-layer brief in English.
4. Speed / 1k / low → 2–3 rolls.
5. One-variable variants.
6. Quality / 2k / medium.
7. Save prompt + file.

### 17.2 Still, from a photo

1. Upload the photo.
2. One imperative sentence + “keep face / pose / camera”.
3. Quality Mode.
4. If one region fails → Magic Wand, do not regen.

### 17.3 Video, from a still

1. Approve the still first.
2. I2V. Prompt = change + one camera + Sound:.
3. 5–8 seconds.
4. If the end must match a drawing, pin last_frame.

### 17.4 Series with a consistent character

1. Generate a hero still. Lock it.
2. Every new shot is an **edit** or a **reference-to-video** with that still as `<IMAGE_1>`.
3. Do not T2V a “same character” from memory.

### 17.5 Poster with readable type

1. Quality Mode. 2k.
2. Headline and subline in quotes. Two layers only.
3. Proofread.
4. If type fails twice, generate without type and composite.

---

## 18. Reference library

### 18.1 Official

| Resource | URL |
|---|---|
| Imagine on grok.com | https://grok.com/imagine |
| Image 2.0 announcement (Quality Mode, typography, Magic Wand, 5-ref, Smart Resize, templates) | https://x.ai/news/grok-imagine-image-2 |
| Imagine Video 1.5 news | https://x.ai/news/grok-imagine-video-1-5 |
| Video 1.5 references announcement | https://x.ai/news/grok-imagine-video-1-5-references |
| Quality Mode API announcement | https://x.ai/news/grok-imagine-quality-mode |
| Video generation | https://docs.x.ai/developers/model-capabilities/video/generation |
| Reference-to-video | https://docs.x.ai/developers/model-capabilities/video/reference-to-video |
| Imagine overview | https://docs.x.ai/developers/model-capabilities/imagine |
| Image generation params | https://docs.x.ai/developers/model-capabilities/images/generation |
| Image editing | https://docs.x.ai/developers/model-capabilities/images/editing |
| Multi-image editing (up to 5) | https://docs.x.ai/developers/model-capabilities/images/multi-image-editing |
| Image-to-video | https://docs.x.ai/developers/model-capabilities/video/image-to-video |
| Video editing | https://docs.x.ai/developers/model-capabilities/video/editing |
| Video extension | https://docs.x.ai/developers/model-capabilities/video/extension |
| Image 2.0 model card | https://docs.x.ai/developers/models/grok-imagine-image-2.0 |
| Models + pricing index | https://docs.x.ai/developers/models |
| Pricing | https://docs.x.ai/developers/pricing |
| Quality-slug retirement (2 Nov 2026) | https://docs.x.ai/developers/migration/imagine-image-quality-nov-2 |
| Imagine API landing | https://x.ai/api/imagine |
| Acceptable Use Policy | https://x.ai/legal/acceptable-use-policy |
| Official consumer image guide (XCreators) | https://x.com/XCreators/status/2040196196388762028 |
| “Use the LLM to write Imagine prompts” (Justine Moore / Elon Musk) | https://x.com/elonmusk/status/2040208784682012818 |

### 18.2 Field-tested community

| Resource | Why it is here |
|---|---|
| https://github.com/thoxakihiko/grok-imagine-prompt-1.5-guide | Best single repo: image + video grammar, anti-patterns, specs cross-checked to docs.x.ai |
| https://github.com/that-cod/awesome-grok-imagine-prompts | Prompt library + five-pillar community framework |
| https://replicate.com/blog/grok-imagine | Best Sound: and intensity-modifier writeup for Video 1.5 |
| https://prompt-architects.com/blog/297-prompting-grok-imagine-video-1-5 | T2V vs I2V vs ref-to-video; official-docs facts table |
| https://aristotto.ai/blog/grok-imagine-video-1-5-what-it-does-and-how-to-prompt-it | How 1.5 reads a prompt; audio failure modes |
| https://grokimagineimage2.com/blog/grok-imagine-prompt-guide | Image 2.0 five-slot structure + 12 copyable still prompts |
| https://supergrok.tech/guides/grok-imagine-image-video-guide/ | Practical revision loop and constraint examples |
| https://picsart.com/blog/grok-imagine-prompts/ | Photographer-brief style, 30–80 word rule, photoreal levers |
| https://pixeldojo.ai/guides/grok-imagine-prompting-guide | Adapted XCreators structure with extra templates |
| https://clickup.com/blog/how-to-use-grok-imagine/ | Consumer modes (Quality / Fast / Normal / Fun / Custom / Spicy) mapped to jobs |
| https://runware.ai/docs/models/xai-grok-imagine-image-2-0/guides/prompting | API-oriented Image 2.0 prompting (layers, photographic language) |

### 18.3 Related craft (not Imagine-specific, still useful)

| Resource | Use |
|---|---|
| https://docs.bfl.ml/guides/prompting_summary | FLUX official prompting — same “no negatives, natural language, specify light” discipline |
| https://promptcrates.com/guides/how-to-structure-image-prompts | Subject / Atmosphere / Technical three-layer revision loop |

Treat third-party playgrounds as renderers, not as sources of truth for parameters. When a blog and `docs.x.ai` disagree, believe `docs.x.ai`.

---

## 19. Appendix — copy-paste prompt pack

Use as-is, then swap only Layer 1.

**A. Professional headshot**

```
Professional LinkedIn headshot of a confident mid-30s man in a navy blazer, soft gray studio background, Rembrandt lighting, 85mm portrait lens, sharp eyes, natural skin texture, corporate photography, no text, no watermark
```

**B. Fashion editorial**

```
Full-body fashion editorial of a model in an oversized charcoal trench coat on a windy rooftop at dusk, city skyline bokeh, 50mm, dramatic side light, high-fashion magazine look, natural fabric motion, no logos, no watermark
```

**C. Architecture**

```
Contemporary glass pavilion in a misty pine forest at dawn, long-exposure soft fog, 24mm wide angle, architectural photography, cool blue-hour palette, sharp glass reflections, no people, no text, no watermark
```

**D. World-building interior (XCreators)**

```
the interior of an abandoned space station, overgrown with bioluminescent plants, shafts of blue-green light filtering through cracked hull panels, wide shot, sci-fi concept art style, high detail
```

**E. Meme / comedy (XCreators)**

```
a golden retriever in a suit sitting at the head of a conference table, other dogs in business attire looking at a whiteboard full of charts, corporate office with fluorescent lighting, shot like a scene from The Office
```

**F. Quiet I2V (Replicate pattern)**

```
The figure slowly lowers the phone from their ear, exhales, and lets their hand fall to their side. They turn their head almost imperceptibly toward the room. Dust motes drift through the shaft of golden light. The cat lifts its head, ears swivelling. Camera locked.
Sound: distant city traffic muffled through glass, a kitchen tap dripping somewhere off-screen, the soft hum of an old TV, the creak of a wood floor. No music.
```

**G. Skate I2V with dialogue**

```
Hold the faces and street from the still. The rider in the middle starts skateboarding slowly, then faster, then very fast. Camera tracks his face from the side. The other two stay in frame, laughing, not talking. Background streaks.
Sound: skateboard wheels on rough asphalt, cars passing, teenagers laughing. He says "I told you bro, this will be the best summer!" then goes quiet. No music bed under the line.
```

**H. Style-transfer edit**

```
Transform into a luminous plein-air impressionist oil painting with visible brushwork, broken color, and richly painterly surface texture. Preserve the original composition, colors, and subject. No glossy CGI look.
```

**I. Multi-ref product-on-set**

```
Place the bottle from image 1 on the marble vanity from image 2. Match the window light and color grade of image 2. Keep the label sharp and unchanged. No extra objects, no extra hands, no text.
```

---

## 20. What “complete control” actually means

You will never get pixel-perfect seeds out of Imagine. Control is a stack, not a slider:

1. **Parameters** decide ratio, resolution, quality, duration, audio on/off.
2. **Five-layer language** decides subject, light, camera, style.
3. **A locked still** decides composition for every video and every edit.
4. **One-variable iteration** teaches you which clause does what.
5. **Region edit** fixes a part without gambling the whole frame.
6. **A prompt-engineer Project** fills missing layers before you spend a generation.
7. **A saved library** is how a look becomes a brand instead of a lucky roll.

If a generation surprises you, a layer was empty. Fill the layer. Do not add adjectives.

---

*End of guide. Re-verify live parameter tables on docs.x.ai when xAI ships the next Imagine slug.*
