# GPT Image 2.5 Complete Operation Guide

**How to control OpenAI GPT Image 2.5 with prompt engineering**

- Document: `gpt_image_operation_guide.md`
- Model family: ChatGPT Images 2.5 / GPT-Image-2.5 Flare & Sunburst
- Released: 8 September 2026
- Guide compiled: 15 September 2026
- Official source of truth: [OpenAI Image Prompting Guide](https://developers.openai.com/api/docs/guides/image-prompting)

This is an operations manual, not a vibe list. GPT Image 2.5 does not reward `masterpiece, 8k, ultra detailed, --ar 16:9, (weight:1.3)`. It rewards a brief that answers four questions:

1. What finished asset am I making?
2. What must be visible?
3. How is the frame built (composition, camera, light, medium)?
4. What must not change or appear?

If you remember only one paragraph from this guide, remember this official line:

> Start with the image you need, then describe the subject, composition, style, and constraints. For edits, identify what should change and what must stay the same. Refine one thing at a time and inspect the result.

---

## 0. How to use this guide

| If you want to… | Go to |
|---|---|
| Understand the product and pick Flare vs Sunburst | §1–§2 |
| Generate from ChatGPT UI | §3 |
| Generate from the API | §4 |
| Write a first-pass prompt that actually controls the model | §5–§7 |
| Lock composition, camera, light, color, people, text | §8 |
| Edit surgically and keep identity | §9 |
| Run a use-case playbook (product, poster, UI, diagram, cutout…) | §10 |
| Diagnose a bad image | §11 |
| Teach another AI to write these prompts | §12 |
| Copy templates and official example prompts | §13–§14 |
| Keep learning from source sites | §15 |

---

## 1. Product map — what “GPT Image 2.5” actually is

OpenAI shipped three related things on 8 September 2026. Do not mix the names.

| Surface | Name | What it is |
|---|---|---|
| ChatGPT product | **ChatGPT Images 2.5** | Consumer image generation + editing inside ChatGPT, ChatGPT Work, and Codex. Adds Sketch, Templates, region comments, and shareable prompts. |
| API small model | **`gpt-image-2.5-flare`** | Fast default. Quality comparable to / better than GPT Image 2 at up to ~50% lower latency. Everyday generation, high volume, prototyping. |
| API base model | **`gpt-image-2.5-sunburst`** | Quality-first. Tighter edit control, richer texture and lighting, slower. Campaign creative, product geometry, multi-turn precision. |

Hard facts:

- The bare ID `gpt-image-2.5` is **invalid**. The API returns model-not-found. Always suffix `-flare` or `-sunburst`.
- Snapshot ID form: `gpt-image-2.5-flare-2026-09-08` / `gpt-image-2.5-sunburst-2026-09-08`.
- Both models accept **text + image** input and output **images**.
- Both generate, edit, inpaint, take multiple references, and support transparent backgrounds.
- Fine-tuning, function calling, and structured outputs are **not** supported on these image models.
- Images carry C2PA metadata and invisible watermarking.
- Content policy still applies. `moderation` can be `auto` (default) or `low`.

### 1.1 What improved versus GPT Image 2 / Images 2.0

- Sharper detail, more natural lighting, richer texture.
- Better preservation of people and products from reference photos.
- Edits more reliably change only what you asked and leave the rest alone across multiple turns.
- Complex layouts (UI, slides, diagrams, transparent assets) hold together better.
- Exact text in images is stronger than earlier GPT Image versions, but still requires quotes + count + placement.
- Flare latency is reported up to ~50% lower than Images 2.0 (workload-dependent; measure your own prompts).

### 1.2 What this model is *not*

It is not Midjourney. It is not Stable Diffusion. It is not DALL·E 3.

| Old habit | What GPT Image 2.5 actually does |
|---|---|
| Keyword soup (`cinematic, 8k, masterpiece, highly detailed`) | Ignores or weakly treats as mood. Prefer visible facts. |
| Numeric weights `(red car:1.4)` | Not a control surface. |
| `--stylize`, `--ar`, `--v` flags | Not parsed. Set aspect via `size` / UI picker. |
| Negative-prompt box | There is no separate negative field. Put exclusions in the same prompt. |
| One giant prompt that does five edits | Drift. One change per turn. |
| “Make it 4K” inside the sentence | Suggestion only. `size="3840x2160"` is a guarantee. |

---

## 2. Decision matrix — Flare vs Sunburst vs quality vs size

Pick the model **before** you rewrite the prompt. OpenAI is explicit: parameters are not prose.

### 2.1 Which model

| Situation | Start here | Then |
|---|---|---|
| Exploring ideas, social, thumbnails, high volume | **Flare** + `quality=medium` or `high` | Drop to `medium`/`low` if it still passes |
| Existing GPT Image 2 workflow already good enough | **Flare** first (hunt latency) | Keep Sunburst only if Flare fails the quality bar |
| GPT Image 2 never met the quality bar | **Sunburst** first | After it passes, A/B the same prompt on Flare |
| Product geometry, label text, identity lock, campaign final | **Sunburst** + `high` / `xhigh` | Use `max` only if a measured defect remains |
| Multi-turn surgical edit chain | **Sunburst** | Restate the preserve list every turn |
| Transparent cutout / logo / sticker | Either, plus `background=transparent` | Inspect the alpha channel, not the preview |

Same `quality="high"` on Flare is **not** the same picture as `quality="high"` on Sunburst. Compare like-for-like on *your* prompt.

### 2.2 Parameters that must live outside the prompt

Set these on the API call or in the ChatGPT UI. Do not bury them in adjectives.

| Parameter | Values | Rule |
|---|---|---|
| `model` | `gpt-image-2.5-flare` \| `gpt-image-2.5-sunburst` | Required on API. No bare `gpt-image-2.5`. |
| `quality` | `auto` (default), `low`, `medium`, `high`, `xhigh`, `max` | Climb only when a defect exists. Climb back down after it passes. `xhigh`/`max` only if they fix an unmet requirement inside your latency/cost budget. |
| `size` | `auto` or `WIDTHxHEIGHT` | See constraints below. |
| `background` | `auto`, `opaque`, `transparent` | Transparency needs this **and** PNG/WebP **and** a prompt that asks for a clean cutout. |
| `output_format` | `png` (default), `jpeg`, `webp` | PNG for logos/cutouts. JPEG/WebP for photos. |
| `output_compression` | `0–100` | JPEG/WebP only. Never apply to PNG. |
| `n` | integer, default `1` | Variations. Useful for logos. |
| `moderation` | `auto`, `low` | Policy still applies. |
| `partial_images` | `0–3` | Streaming previews. Each partial costs extra output tokens. |

### 2.3 Size constraints (hard)

Custom `WIDTHxHEIGHT` must satisfy all four:

1. Each edge ≤ 3,840 px.
2. Both edges are multiples of 16.
3. Long edge ÷ short edge ≤ 3.
4. Total pixels between 655,360 and 8,294,400.

Common presets:

| Intent | Size | Notes |
|---|---|---|
| Square | `1024x1024` | Default working size |
| Landscape | `1536x1024` | Social / web hero |
| Portrait | `1024x1536` | Stories, posters, product |
| 2K square | `2048x2048` | Print-ish, inspect cost |
| 2K landscape | `2048x1152` | |
| 4K landscape | `3840x2160` | Experimental territory above 2560×1440 |
| 4K portrait | `2160x3840` | |
| Pitch slide 16:9 | `1536x864` | Official example size |

Outputs above 3,686,400 total pixels (`2560x1440`) are flagged **experimental**. Inspect before shipping.

In ChatGPT, use the aspect-ratio picker or name the ratio in the prompt (`4:5 paid-social`, `9:16 story`, `16:9 slide`). The picker is more reliable than hoping the model infers it.

### 2.4 Quality ladder and approximate cost

Token rates (both models, per 1M tokens):

| Token type | Standard | Cached |
|---|---|---|
| Text input | $5.00 | $1.25 |
| Image input | $8.00 | $2.00 |
| Image output | $30.00 | — |

Approximate cost for one 1024×1024 image (image output tokens only):

| Quality | Output tokens (approx.) | Cost |
|---|---|---|
| `low` | 196 | ~$0.006 |
| `medium` | ~439 | ~$0.013 |
| `high` | ~1,756 | ~$0.053 |
| `xhigh` | ~3,122 | ~$0.094 |
| `max` | ~7,024 | ~$0.211 |

Tokens do **not** scale linearly with pixel area. A 3840×2160 `low` image is still cheap; a 1024×1024 `max` image is not. Measure cost per *accepted* image, including retries.

Operating rule:

1. Generate at the lowest quality that still reads.
2. Raise quality only to fix a measured defect (mushy small type, collapsed diagram labels, melted product edges).
3. After it passes, test one step down. Keep the cheaper setting if quality holds.
4. Never use `max` as a substitute for a vague prompt.

**Migration remap from GPT Image 2.** The 2.5 quality ladder shifted. Keeping `quality="medium"` when you move a GPT Image 2 workflow onto 2.5 silently drops spend and often drops fidelity. A practical remap used by early migrators:

| You used on GPT Image 2 | Try first on 2.5 |
|---|---|
| `low` | `low` or `medium` |
| `medium` | `high` |
| `high` | `max` |
| `auto` | Do not trust `auto` for production cost. Pin a value. |

Then walk back down one step if the image still passes. Confirm live token counts; the official GPT Image 2 calculator does **not** estimate 2.5 consumption. Flare is not cheaper per token than Sunburst — it is only faster.

### 2.5 Transparent assets — the triple requirement

All three must be true or you will get a fake checkerboard:

1. API/UI: `background="transparent"`.
2. Format: `png` or `webp`.
3. Prompt: “fully transparent background, clean alpha edges, no checkerboard, no pedestal, no drop shadow unless requested.”

Then open the file and inspect the **alpha channel** at hair, glass, shadows, thin straps, and product edges. A drawn checkerboard in the pixels is a failure, not transparency.

---

## 3. ChatGPT UI operations

Use ChatGPT when you want conversation, Sketch, templates, and region comments. Use the API when you want deterministic size/quality, model choice, or app integration.

Important UI limits:

- You **cannot pick Flare vs Sunburst** inside ChatGPT. Testers treat the consumer path as Flare-class. For Sunburst, use the API.
- Default ChatGPT output is often under 1080p (one measured default ~1672×941). For production resolution, set `size` on the API.
- Templates live at Sidebar → Images → Templates. They are reported **unavailable in Work mode**.
- Sketch: type `@Sketch` in the composer, or open Images → Sketch, or `https://chatgpt.com/sketch`. Help Center documents it most clearly on mobile; the product page says type `@Sketch` in ChatGPT generally.

### 3.1 Generate from a blank chat

1. Open a **new chat** (old image context will leak into later edits).
2. Write a concrete brief. Name the deliverable first.
3. Attach 0–N reference photos. In the prompt, number them and assign roles (see §9.3).
4. Send. Wait for the image.
5. Inspect with the QA checklist in §11 **before** asking for another change.

Starter sentence shapes that work:

```text
Create a 4:5 product photograph for a landing-page hero.
Subject: [one object], [material], [orientation].
Composition: [placement], [camera], [negative space].
Light: [source + direction].
Constraints: no text, no logos, no extra products.
```

```text
Create a vertical poster.
Headline (exact, once): "Open Late"
Subline (exact, once): "Thursday to Sunday"
Layout: headline top third, subject center, subline bottom band.
No other text.
```

### 3.2 Templates

Templates exist because most people need a *format*, not a scene.

1. Sidebar → **Images** → **Templates**.
2. Pick a category (Poster, Merch, flyer, product photo, logo, icon, sticker, etc.).
3. Fill the content fields. Answer follow-up questions (style: Clean Studio / Editorial / Lifestyle / Dramatic).
4. Send.

Templates set framing conventions so your prompt only supplies content. One report notes templates are not available in Work mode — if you do not see them, use the labeled-section template in §6 instead.

### 3.3 Sketch (`@Sketch`)

Sketch is the highest-leverage layout control in the ChatGPT product. Use it when placement is the thing you keep regenerating.

1. In the composer type `@` and choose **Sketch**, or open Images → Sketch, or `chatgpt.com/sketch`.
2. Draw the layout: where the subject sits, where type goes, where empty space is. Color and erase as needed.
3. Confirm with the checkmark.
4. Add a text brief: subject, materials, light, style, exact copy, constraints.
5. Send.
6. On the result, treat the sketch as **layout intent**. If the model invents new objects, the next edit is: “Preserve the exact layout, proportions, and perspective of the sketch. Do not add new elements.”

Sketch prompt pattern:

```text
Turn this sketch into a photorealistic image.
Preserve the exact layout, proportions, and perspective.
Subject: [what each region is].
Materials and lighting consistent with the sketch intent.
Do not add new elements or text.
```

### 3.4 Region comments and local edits

After an image exists:

- Click the image → drop a **comment on a region** (“make this mug blue”, “remove the second chair”).
- Use the select / mark-area tool when you need inpainting rather than a global rewrite.
- **Remove background** for cutouts, then still inspect alpha.
- **Resize** with the aspect picker rather than “make it wider” in prose.
- **Share** can include the prompt so someone else can rerun it with their own references.

### 3.5 Multi-turn editing in ChatGPT

The conversation *is* the edit history. That is a feature and a trap.

Rules:

1. One change per message.
2. Start with the change, then list what must stay.
3. Restate identity / geometry / labels every turn. “Same as before” is weak; named invariants are strong.
4. If a region must stay pixel-identical, download, composite in an editor, and re-upload. Do not trust the model to lock pixels.
5. If the image has drifted after five turns, restart from the last good download as a fresh input rather than continuing the polluted thread.

---

## 4. API operations

Two entry points:

| Entry | Use when |
|---|---|
| `POST /v1/images/generations` and `/v1/images/edits` | Direct image in / image out. Simplest. |
| Responses API + `tools: [{ type: "image_generation" }]` | Multi-image input, masks, a parent language model that can revise the prompt, action control (`generate` / `edit` / `auto`). |

### 4.1 Generate (Python)

```python
from openai import OpenAI
import base64

client = OpenAI()

result = client.images.generate(
    model="gpt-image-2.5-flare",
    prompt="""Create a photorealistic product photograph for a landing-page hero.
A matte ceramic pour-over carafe, bone white, centered on a pale oak board.
Eye-level, 85mm compression, shallow depth of field.
Soft window light from the left, gentle contact shadow.
No text, no logos, no extra props.""",
    size="1024x1536",
    quality="high",
    background="opaque",
    output_format="png",
    n=1,
)

image_bytes = base64.b64decode(result.data[0].b64_json)
with open("carafe.png", "wb") as f:
    f.write(image_bytes)
```

### 4.2 Edit (conceptual)

```python
result = client.images.edit(
    model="gpt-image-2.5-sunburst",
    image=open("carafe.png", "rb"),
    prompt="""Change only the board to honed black slate.
Keep the carafe geometry, glaze, highlights, contact shadow shape,
camera angle, crop, and color of the ceramic exactly as they are.
Do not add text, logos, props, or a new light source.""",
    size="1024x1536",
    quality="high",
)
```

Mask notes (when you inpaint a region):

- Mask must match the input image size and format.
- Mask uses the alpha channel to mark the editable region.
- File < 50 MB.
- If multiple input images are supplied, the mask applies to the first.

### 4.3 Responses API pattern (multi-reference + optional mask)

Use a parent model (the current Responses-capable model in your account) plus the image-generation tool. Number the attached images in the text so rule 7 fires.

```text
Image 1 = approved product identity. Preserve geometry, label, and material.
Image 2 = kitchen environment. Use architecture, window, and daylight direction only.
Image 3 = styling reference. Take palette and negative space only. Do not copy its products.

Create a 3:2 editorial lifestyle photograph of the product from image 1
standing on the island from image 2.
Match image 2's window-light direction, contact shadow, and white balance.
No people, no extra products, no text.
```

Action control on the tool (when available):

- `auto` — model decides generate vs edit
- `generate` — force a new image
- `edit` — force an edit if an image is in context

### 4.4 Hard limits

| Limit | Value |
|---|---|
| Prompt length | 32,000 characters |
| Images per request (`n`) | 1–10 |
| Reference images | up to 16, each < 50 MB, png / jpg / webp |
| Mask | PNG with alpha, same dimensions as the source, < 50 MB |
| `input_fidelity` | **Not accepted on 2.5.** Sending it returns 400. Fidelity is always high. |
| Batch API | Not available for 2.5 at launch |
| Streaming previews | `partial_images` 0–3; each partial adds output tokens |

If a region must stay untouched, a **mask** is stronger than polite wording.

### 4.5 Rate limits (Sunburst published tiers; confirm current dashboard)

| Tier | TPM | IPM |
|---|---|---|
| 1 | 100,000 | 5 |
| 2 | 250,000 | 20 |
| 3 | 800,000 | 50 |
| 4 | 3,000,000 | 150 |
| 5 | 8,000,000 | 250 |

Free tier: not supported for these API models.

### 4.6 Migration playbook (official 6 steps)

If you already have a GPT Image 1 / 1.5 / 2 pipeline:

1. **Save a baseline.** Production prompts, references, hard cases (faces, product geometry, exact text, transparent assets). Record model, settings, results.
2. **Choose the first candidate.** Quality already fine → Flare. Quality never fine → Sunburst. Freeze prompt, refs, size, format for the first comparison.
3. **Check the complete result.** Instruction following, identity, product geometry, text accuracy, unwanted changes, transparency. Repeat to measure consistency. Test the *full edit sequence*, not one step.
4. **Hunt latency after quality passes.** If Sunburst passed, A/B Flare. Switch only if quality holds *and* latency improves.
5. **Tune one setting at a time.** Quality ladder before prompt rewrites. Measure typical *and* slow responses, failures, retries, cost per accepted image. Do not assume Flare is cheaper — token rates are the same.
6. **Roll out by workflow.** Small traffic share, same metrics, gradual expand, keep the previous model for rollback.

---

## 5. The 8 official prompting rules (operating checklist)

Print this. Use it before you blame the model.

### Rule 1 — Define the result

Name the **deliverable** and the **use**.

Bad: `a cool picture of a coffee cup`

Good: `A product photograph for a landing-page hero` / `a 16:9 movie teaser poster` / `a high-school biology handout` / `a transparent e-commerce cutout`

The deliverable loads a stack of unspoken conventions (crop, negative space, type hierarchy, polish). Specify composition, aspect, and placement when they matter. For complex jobs, use labeled sections: scene / subject / details / constraints.

### Rule 2 — Choose a maintainable format

There is no secret syntax. These are all valid and equivalent in power:

- Short paragraph
- Labeled sections (`SCENE`, `SUBJECT`, `CONSTRAINTS`)
- XML-ish blocks (`<deliverable>…</deliverable>`)
- JSON-looking text (the model reads it as structure, not as a schema)

Pick the format you can edit next week without breaking it. JSON is a *readability* choice, not an unlock.

### Rule 3 — Describe visible details

Name materials, lighting, colors, and the visual medium.

- Say **photorealistic** or **real photograph** when that is the goal.
- `soft morning light from a window on the left` beats `beautiful lighting`.
- `brushed aluminum` beats `shiny metal`.
- Camera specs (`85mm`, `50mm`, `24mm`, `macro`) are **appearance cues**, not a physics simulator.
- For wide / cinematic / low-light / rainy / neon scenes, specify scale, atmosphere, and color. Do not lean on mood words alone (`epic`, `moody`, `premium`, `cozy`).

### Rule 4 — Specify people and actions

Describe body framing, relative scale, gaze, and contact with objects.

Useful fragments:

- `full body visible, feet included`
- `looking down at the open book`
- `hands naturally gripping the handlebars`
- `medium close-up at eye level`
- `she is centered but looking away from the camera`

Unspecified hands, feet, and gaze are the usual source of mannequin poses.

### Rule 5 — Specify exact text

- Put required wording in **"quotation marks"**.
- Say how many times it appears: `Render the tagline "Yours to Create" exactly once.`
- Say where it sits and what it looks like: `bold condensed type across the top`.
- Spell unusual words or brand names letter by letter when accuracy matters: `S-T-R-I-P-E`.
- End with `No extra text, no watermarks, no unrelated logos.`
- Then actually read the pixels. Small / dense / multi-font text wants `quality=high` or above.
- Keep lines short. Long sentences still degrade.

### Rule 6 — Separate changes from constraints

Edit formula:

```text
Change only [X].
Keep [identity / geometry / layout / lighting / labels / crop / shadows] exactly as they are.
Do not add [text / logos / props / new light].
```

For surgical local edits, also lock saturation, contrast, arrows, camera angle, and surrounding objects. Repeat the preserve list every turn.

### Rule 7 — Assign roles to references

Never say “use these four images as reference.”

Say:

```text
Image 1 = identity. Face, proportions, skin tone. Nothing else.
Image 2 = clothing only.
Image 3 = interior architecture and daylight direction.
Image 4 = color palette and grade only. Do not copy its objects.
```

Then explain the combine: `Place the product from image 1 on the table in image 2, matching the light direction in image 2.`

### Rule 8 — Iterate deliberately

- Pass the previous output in as the next edit input.
- Request **one** change.
- Restate critical constraints. “Same style as before” is optional color; named invariants are load-bearing.
- Inspect before adding more instructions.
- If a region must stay pixel-identical, composite it. Prompting cannot guarantee pixel lock.

---

## 6. Master prompt anatomy

### 6.1 New image — labeled spec (recommended default)

```text
DELIVERABLE
What asset, for what use, at what aspect.

SUBJECT
Primary subject, visible attributes, pose, materials.

SCENE
Environment, action, supporting objects, time of day.

COMPOSITION
Framing, camera angle, placement, hierarchy, negative space.

VISUAL DIRECTION
Lighting (source + direction + quality), palette (3–5 named colors),
materials, texture, medium, realism level.

TEXT
Exact copy in "quotes". Count. Placement. Type style. Color.
"No other text."

CONSTRAINTS
What must not appear. What must not be invented.

OUTPUT
Orientation / production use / transparency if needed.
```

### 6.2 New image — short ordered prose

Official recommended order: **subject → composition → style → constraints**.

```text
A white ceramic coffee cup on a linen tablecloth.
Shot from a low angle, cup centered, the top third of the frame empty.
Photorealistic, soft morning light from a window on the left, shallow depth of field.
No text and no logos.
```

Purpose in one clause changes the crop even when the subject is identical:

- `A product photo for a landing-page hero`
- `A flat-lay for an Instagram post`
- `A book cover`
- `A YouTube thumbnail`
- `A packaging mockup`
- `A sticker`
- `A slide background`

### 6.3 Edit spec

```text
EDIT TARGET
Change only [one thing].

PRESERVE
Identity, geometry, layout, lighting, labels, crop, shadows, grade.

REFERENCE ROLES
Image N = [exactly one job].

INTEGRATION
Match existing light direction, perspective, texture, contact shadow.

EXCLUSIONS
No extra text, no new props, no relighting, no redesign.

OUTPUT
Same size / same transparency requirement.
```

### 6.4 XML-style spec (good for teaching another model)

```text
<deliverable>4:5 paid-social campaign still for [brand]</deliverable>
<subject>…</subject>
<scene>…</scene>
<composition>…</composition>
<visual_direction>…</visual_direction>
<text>Render exactly once: "…". Placement. Type.</text>
<constraints>No people. No extra products. No watermarks.</constraints>
```

### 6.5 JSON-looking spec (good for dense layouts)

Useful for posters, UI, slides, infographics — anything with distinct regions. This is still plain text. It is not a schema the API validates.

```text
{
  "type": "poster",
  "use": "16:9 YouTube thumbnail",
  "subject": "…",
  "composition": "subject left third, type right third, quiet top 15%",
  "visual": "photoreal, 35mm, tungsten practicals, palette: …",
  "text": {
    "headline": "EXACT WORDS",
    "count": 1,
    "placement": "upper right",
    "style": "bold condensed sans, white"
  },
  "constraints": ["no extra text", "no logos", "no watermark"]
}
```

---

## 7. Instruction list — the operating procedure

Run this every time. Do not skip steps because the idea “feels simple.”

### Phase A — Brief (2 minutes)

1. Write one sentence: **I am making a [deliverable] for [use].**
2. Write one sentence: **The viewer should notice [subject] first.**
3. Decide aspect / size. Set it in the UI or `size=`. Do not only mention it in prose.
4. Decide Flare vs Sunburst and quality using §2.
5. List every reference image and give each exactly one role.
6. Write the exact on-image copy in quotes, or write `no text`.
7. Write a short exclusion list (5 items or fewer). Long exclusion novels get ignored.

### Phase B — First generate

8. Assemble the prompt in the order: deliverable → subject → scene → composition → visual → text → constraints.
9. Generate **one** image (or `n=2~4` only for logo exploration).
10. Do not rewrite the prompt yet. Inspect.

### Phase C — Inspect (mandatory)

11. Read every piece of on-image text out loud.
12. Check hands, feet, gaze, contact shadows, label geometry, extra objects.
13. Check whether the composition matches the brief (thirds, negative space, crop).
14. If transparent, inspect the alpha channel.
15. Decide: accept / one targeted edit / restart from a cleaner brief.

### Phase D — Edit loop

16. Change **one** variable: light, or lens, or background, or one text string, or one object.
17. Restate the preserve list.
18. Feed the previous output back in.
19. Stop after the defect is gone. Do not “improve” an accepted image.

### Phase E — Lock and export

20. Download the accepted file. Do not keep iterating on a winner.
21. If a later campaign needs a variant, start from that file as Image 1 with a new edit brief.
22. If pixel-identical regions matter (logo lockup, legal line, product die-line), composite them in a design tool.

---

## 8. Control levers — how to steer each visual axis

This is the lexicon that actually moves GPT Image 2.5. Use concrete nouns. Avoid mood adjectives unless you immediately translate them into light, color, and geometry.

### 8.1 Composition and placement

The model will invent a crop if you do not specify one.

| You want | Say |
|---|---|
| Subject left, room to type | `Place the subject in the lower-left third. Keep the upper-right 40% visually quiet for copy.` |
| Centered icon / logo | `Single centered mark, generous padding, no scenery.` |
| Hero product uncropped | `No cropped product edges. Full silhouette visible.` |
| Wide environment | `Wide establishing frame, subject small in the lower third, sky taking the top half.` |
| Tight portrait | `Medium close-up, head and shoulders, eye level, background falloff.` |
| Flat-lay | `Overhead 90-degree flat-lay, objects arranged on [surface], even spacing.` |
| Rule of thirds | `Subject on the right third. Leading lines from lower left to the subject.` |
| Symmetry | `Dead-center symmetrical composition, mirrored negative space.` |

Sketch (§3.3) beats any of these paragraphs when the layout is the product.

### 8.2 Camera (appearance cues, not physics)

| Token | Typical look |
|---|---|
| `24mm wide-angle` | Immersive interior / landscape, edge stretch |
| `35mm` | Environmental, natural documentary |
| `50mm` | Neutral “what the eye sees,” official sailor example |
| `85mm` | Portrait compression, background melt |
| `100mm macro` | Product texture, label close-up |
| `low angle` | Monumental, product hero |
| `high angle` / `overhead` | Maps, flat-lays, vulnerable subject |
| `eye level` | Honest, documentary |
| `three-quarter view` | Product / face volume |
| `shallow depth of field` | Subject separation |
| `deep focus` | Diagrams, groups, architecture |
| `35mm film grain` | Mild texture; say `subtle film grain` not `heavy grain` |

Do not stack five lenses. Pick one.

### 8.3 Lighting

Always specify **source + direction + quality**.

| Look | Phrase |
|---|---|
| Window daylight | `soft morning light from a window on the left` |
| Overcast | `overcast diffuse daylight, almost no cast shadow` |
| Golden hour | `low warm sun from camera right, long shadows, mild lens flare on chrome` |
| Studio product | `large softbox from upper left, gentle fill from the right, controlled contact shadow` |
| Rim / separation | `narrow warm rim light on the right edge` |
| Rembrandt portrait | `single key from upper left, triangle of light on the far cheek, deep wraparound shadow` |
| Practical interior | `only the lamps in the scene, tungsten color, falloff into shadow` |
| Neon night | `cool cyan neon from the left, magenta bounce from the right, wet asphalt reflections` |
| Honest documentary | `available light only, no cinematic grading` |

“Cinematic lighting” alone does almost nothing. “Single tungsten spotlight from above, deep shadows wrapping the rest of the room” does.

### 8.4 Materials and surfaces

Name the substance the light is hitting.

- `matte ceramic`, `glazed bone china`, `brushed aluminum`, `anodized black metal`
- `raw linen with visible weave`, `honed black slate`, `pink marble veined with cream`
- `wet asphalt at night`, `unfinished oak with open grain`, `worn leather`
- `condensation on cold aluminum`, `dust on a desert highway`

For still life and product work, **anchor the subject to a named surface**. A “table” is a stock photo. A “slab of pink marble veined with cream and gold” is an editorial.

### 8.5 Color palette

Give 3–5 named colors. More than five and the model commits to none.

```text
Color palette: pale mineral gray, cobalt stripe, wet-stone charcoal,
cool morning blue, a narrow warm rim of sunrise amber.
```

Hex sometimes works; named colors are more reliable. Constrain by exclusion when a color must not appear: `no neon, no orange, no pure black.`

### 8.6 People, identity, hands

Minimum viable person spec:

1. Age range / build / distinguishing features you actually need.
2. Body framing (`full body, feet included` / `waist-up`).
3. Gaze (`looking at camera` / `looking down at the book` / `looking off-frame left`).
4. What the hands are doing (`both hands on the carafe handle`, `one hand adjusting a net`).
5. Wardrobe in materials, not brands, unless you have rights and a reference.

Identity lock (with a reference photo):

```text
Using image 1 as the exact reference for face, proportions, skin tone,
and expression: change only [setting / wardrobe / lighting].
Do not alter likeness, age, or identity in any way.
```

### 8.7 Style and medium

Name a **medium**, then optionally one accent.

| Goal | Phrase |
|---|---|
| Real photo | `photorealistic real photograph, unstyled, no heavy retouching` |
| Editorial fashion | `high-end fashion editorial, 50mm, bright midday sun` |
| Campaign ad | `polished campaign image, premium fashion photography cues` |
| Flat vector logo | `clean vector-like shapes, flat design, minimal strokes, no gradients` |
| Classroom diagram | `clean classroom handout, white background, simple icons, easy-to-read labels` |
| Comic | `vertical comic-style reel with 4 panels` + per-panel action |
| Watercolor | `transparent watercolor on cold-press paper, visible pigment granulation` |
| Style fuse | `[base medium] with [accent] highlights` — never two bases as equals |

Official warning: camera and style words are cues. If you want a real photograph, say so. If you want a diagram, say “classroom handout,” not “cinematic infographic.”

### 8.8 Constraints and exclusions

Short list at the end. Typical commercial footer:

```text
No extra text. No watermarks. No signatures. No logos other than the specified mark.
No extra products. No people. No heavy retouching. No checkerboard. No fake drop shadow.
```

For photoreal people: `No glamorization, no heavy retouching. Keep real skin texture.`

For diagrams: `Avoid tiny text, extra decoration, or anything that makes the diagram hard to understand.`

---

## 9. Editing protocol — how to actually control changes

2.5’s headline skill is **leaving the rest of the image alone**. You only get that skill if you ask for it in the right shape.

### 9.1 The one-change rule

Five clean single-turn edits beat one prompt that lists five changes.

Good sequence:

1. Change background only.
2. Change the front-label line only.
3. Warm the rim light only.

Bad: “Change the background, rewrite the label, add condensation, relight, and crop taller.”

### 9.2 Preserve-list template (reuse every turn)

```text
Change only [ONE thing].

Do not change:
- subject identity / face / proportions
- product geometry, cap, label size, logo
- camera angle, crop, lens feel
- lighting direction and color temperature
- contact shadows and reflections
- any text other than the one string being replaced
- saturation, contrast, and grade
- surrounding objects

Do not add text, logos, watermarks, or new props.
```

If drift starts, paste this block again even if you already said it two turns ago.

### 9.3 Multi-reference roles

Number images in the order they are attached.

```text
Image 1 = approved product identity.
Preserve the exact bottle, cap, label, logo, proportions, and material.

Image 2 = environment reference.
Use the kitchen architecture, marble island, window placement, and daylight direction.

Image 3 = styling reference only.
Use its restrained neutral palette and editorial still-life composition.
Do not copy its products, props, or typography.

Place the product from image 1 on the island from image 2.
Match image 2's window-light direction, contact shadow, reflection strength,
white balance, and depth of field.
The product must feel photographed in the scene, not composited on top.
```

### 9.4 Identity + wardrobe swap (official pattern)

```text
Edit the image to dress the woman using the provided clothing images.
Do not change her face, facial features, skin tone, body shape, pose, or identity
in any way. Preserve her exact likeness, expression, hairstyle, and proportions.
Replace only the clothing, fitting the garments naturally to her existing pose
and body geometry with realistic fabric behavior.
Match lighting, shadows, and color temperature to the original photo so the
outfit integrates photorealistically, without looking pasted on.
Do not change the background, camera angle, framing, or image quality,
and do not add accessories, text, logos, or watermarks.
```

### 9.5 Combine two photos (official pattern)

```text
Place the dog from the second image into the setting of image 1,
right next to the woman, use the same style of lighting, composition
and background. Do not change anything else.
```

### 9.6 Translate text, keep layout (official pattern)

```text
Translate the text in the infographic to Spanish.
Do not change any other aspect of the image.
```

Then read every label. Translation edits are where hidden extra words appear.

### 9.7 Style transfer (official pattern)

```text
Use the same style from the input image and generate a man riding
a motorcycle on a white background.
```

When you need tighter control:

```text
Image 1 = style only (line weight, palette, rendering).
Image 2 = subject identity.
Generate [new scene] in the style of image 1.
Do not copy image 1's objects. Preserve image 2's likeness.
```

### 9.8 Transparent cutout (official pattern)

Settings: `background="transparent"`, `output_format="png"`, quality at least `medium`.

```text
Extract the product from the input image and isolate it on a fully
transparent background.
Output: centered product, crisp silhouette, no halos/fringing.
Preserve product geometry and label legibility exactly.
Add only light polishing. Do not add a solid backdrop, checkerboard,
scenery, or shadow.
Do not restyle the product; remove the background and preserve
clean alpha transparency.
```

### 9.9 Sketch or drawing → photograph (official pattern)

```text
Turn this drawing into a photorealistic image.
Preserve the exact layout, proportions, and perspective.
Choose realistic materials and lighting consistent with the sketch intent.
Do not add new elements or text.
```

### 9.10 Remove an object (official pattern)

```text
Remove the flower from the man's hand. Do not change anything else.
```

After object removal, inspect the hole: texture fill, shadow leftover, warped hands. A second turn may be `Rebuild only the palm and fingers. Keep the rest of the image unchanged.`

### 9.10b Swap one object, lock the room

```text
In this room photo, replace ONLY the white chairs with chairs made of wood.
Preserve camera angle, room lighting, floor shadows, and surrounding objects.
Do not change the walls, floor, windows, or any other furniture.
```

### 9.10c Multi-turn billboard (create, then relight)

Turn 1 — create with exact copy:

```text
Create a realistic billboard mockup of the shampoo on a highway scene during sunset.
Billboard text (EXACT, verbatim, no extra characters):
"Fresh and clean"
No other text on the billboard. Keep the product recognizable.
```

Turn 2 — one environmental change, restate the copy lock:

```text
Change only the time of day to a winter evening with snowfall.
Keep the billboard structure, the product, the camera angle, and the exact
text "Fresh and clean" unchanged. Do not add any other copy.
```

### 9.11 When prompting is the wrong tool

Composite in a design tool, then re-import, when you need:

- A legally locked logo or wordmark
- A die-line that must match packaging art
- A face that must stay pixel-identical across a campaign set
- A chart whose numbers were already approved

OpenAI says this out loud: *if a region must remain pixel-identical, composite the approved edit into the original image instead of relying on prompting alone.*

---

## 10. Use-case playbooks

Each playbook is a ready operating procedure. Swap the bracketed content. Keep the structure.

### 10.1 Photoreal photograph

**Settings:** Flare or Sunburst, `1024x1536` or `1536x1024`, `quality=medium` or `high`.

**Must include:** subject + body/object detail, lens, height, light source + direction, texture, anti-retouch constraint.

Official example (sailor):

```text
Create a photorealistic candid photograph of an elderly sailor standing on a small fishing boat.
He has weathered skin with visible wrinkles, pores, and sun texture, and a few faded traditional sailor tattoos on his arms.
He is calmly adjusting a net while his dog sits nearby on the deck. Shot like a 35mm film photograph, medium close-up at eye level, using a 50mm lens.
Soft coastal daylight, shallow depth of field, subtle film grain, natural color balance.
The image should feel honest and unposed, with real skin texture, worn materials, and everyday detail. No glamorization, no heavy retouching.
```

### 10.2 Product / e-commerce hero

**Must include:** deliverable, exact product description or Image 1 identity lock, surface, light direction, crop rule, “no extra products.”

```text
DELIVERABLE
A 4:5 e-commerce main image for a product detail page.

SUBJECT
[Product], [material], [color], unopened, physically plausible.

SCENE
[Surface]. [Optional one supporting prop].

COMPOSITION
Product centered or lower-left third. No cropped edges.
Eye-level, slight telephoto compression.

VISUAL DIRECTION
Large soft light from upper left, gentle fill, real contact shadow.
Photoreal product photography, not glossy 3D.

CONSTRAINTS
No people, no extra units, no text, no logos except the product mark,
no pedestal, no fake reflection plate.
```

### 10.3 Poster / ad / thumbnail with exact copy

**Must include:** quoted headline, count = 1, placement, type style, “no other text.”

Official example (Thread):

```text
Give me a cool in-culture ad / fashion shot for a brand called Thread.
It's a hip young street brand. The ad shows a group of friends hanging out together with the tagline "Yours to Create."
Make it feel like a polished campaign image for a youth streetwear audience: stylish, contemporary, energetic, and tasteful.
Use clean composition, strong color direction, natural poses, and premium fashion photography cues.
Render the tagline exactly once, clearly and legibly, integrated into the ad layout.
No extra text, no watermarks, no unrelated logos.
```

Headline pattern:

```text
A poster with the headline "Open Late" in bold condensed type across the top,
and "Thursday to Sunday" in small type at the bottom. No other text.
```

### 10.4 Logo / mark

**Settings:** `background=transparent`, `png`, `n=4` to explore, quality `medium`/`high`.

Official example:

```text
Create an original, non-infringing logo for a company called Field & Flour, a local bakery.
The logo should feel warm, simple, and timeless. Use clean, vector-like shapes, a strong silhouette, and balanced negative space.
Favor simplicity over detail so it reads clearly at small and large sizes. Flat design, minimal strokes, no gradients unless essential.
Fully transparent background. Deliver a single centered logo with generous padding, clean alpha edges, and no solid backdrop, scenery, checkerboard, or watermark.
```

Always say **original, non-infringing**. Do not ask it to “make a logo like [famous brand].”

### 10.5 UI mockup

Prompt it like a shipped screenshot, not concept art.

Official example:

```text
Create a realistic mobile app UI mockup for a local farmers market.
Show today’s market with a simple header, a short list of vendors with small photos and categories, a small “Today’s specials” section, and basic information for location and hours.
Design it to be practical, and easy to use. White background, subtle natural accent colors, clear typography, and minimal decoration.
It should look like a real, well-designed, beautiful app for a small local market.
Place the UI mockup in an iPhone frame.
```

Add:

```text
It should look like a shipped application screenshot, not a futuristic concept image.
Readable type. Real labels. No lorem-ipsum garbage characters. No fake 3D glass.
```

Then read every label. UI is a text-accuracy job.

### 10.6 Diagram / infographic / slide

Name the audience and the information, not the aesthetic.

Official infographic:

```text
Create a detailed Infographic of the functioning and flow of an automatic coffee machine like a Jura.
From bean basket, to grinding, to scale, water tank, boiler, etc.
I'd like to understand technically and visually the flow.
```

Official classroom diagram (`size="1536x1024"`, `quality="high"`):

```text
Create a simple biology diagram titled "Cellular Respiration at a Glance" for high school students.

Show how glucose turns into energy inside a cell. Include glycolysis, the Krebs cycle, and the electron transport chain.
Use arrows to connect the steps, and label the main molecules: glucose, pyruvate, ATP, NADH, FADH2, CO2, O2, and H2O.
Make it look like a clean classroom handout or slide, with a white background, simple icons, clear labels, and easy-to-read text.

Avoid tiny text, extra decoration, or anything that makes the diagram hard to understand.
```

Official pitch slide (`size="1536x864"`, `quality="high"`):

```text
Create one pitch-deck slide titled "Market Opportunity" that feels like a real Series A fundraising slide from a YC-backed startup.

Use a clean white background, modern sans-serif typography like Inter, and a crisp, minimal layout. The slide should include:

* A TAM/SAM/SOM concentric-circle diagram in muted blues and grays
* Specific, believable market sizing numbers:
  * TAM: $42B
  * SAM: $8.7B
  * SOM: $340M
* A clean bar chart below showing market growth from 2021 to 2026, with a subtle upward trend
* Small footnotes: "AGI Research, 2024" and "Internal analysis"
* A company logo placeholder in the bottom-right corner

The design should look like it belongs in a deck that actually raised money: highly readable text, clear data hierarchy, polished spacing, and professional startup-style visual language.

Avoid clip art, stock photography, gradients, shadows, decorative elements, or anything that feels generic or overdesigned.
```

**Always verify numbers and arrows after generation.** The model can draw a convincing wrong diagram.

### 10.7 Comic / storyboard

Specify panel count, reading order, and the action in each panel. Vertical reel? Say so.

Official 4-panel:

```text
Create a short vertical comic-style reel with 4 panels.
Panel 1: The owner leaves through the front door. The pet is framed in the window behind them, small against the glass, eyes wide, paws pressed high, the house suddenly quiet.
Panel 2: The door clicks shut. Silence breaks. The pet slowly turns toward the empty house, posture shifting, eyes sharp with possibility.
Panel 3: The house transformed. The pet sprawls across the couch like it owns the place, crumbs nearby, sunlight cutting across the room like a spotlight.
Panel 4: The door opens. The pet is seated perfectly by the entrance, alert and composed, as if nothing happened.
```

### 10.8 Historical / real-world knowledge scenes

The model has world knowledge. Use dates and places when period accuracy matters.

```text
Create a realistic outdoor crowd scene in Bethel, New York on August 16, 1969.
Photorealistic, period-accurate clothing, staging, and environment.
```

Then add constraints: `no modern phones, no modern sneakers, no brand anachronisms.`

### 10.9 Character sheet / consistency

Ask for multiple views in **one** image rather than hoping later images match.

```text
Create a character design sheet for [character], one image, white background.
Include: front full-body, side, back, three-quarter, and three expression heads
(neutral, smile, frown). Same outfit, same proportions, same colors in every view.
Label each view in small clean sans-serif. No extra characters. No scenery.
```

Later scenes: attach the sheet as Image 1 = identity + costume lock.

### 10.10 Insert a person into a scene

Official pattern (grounded, anti-cinematic):

```text
Generate a highly realistic action scene where this person is running away from a large, realistic brown bear attacking a campsite. The image should look like a real photograph someone could have taken, not an overly enhanced or cinematic movie-poster image.
She is centered in the image but looking away from the camera, wearing outdoorsy camping attire, with dirt on her face and tears in her clothing. She is clearly afraid but focused on escaping, running away from the bear as it destroys the campsite behind her.
The campsite is in Yosemite National Park, with believable natural details. The time of day is dusk, with natural lighting and realistic colors. Everything should feel grounded, authentic, and unstyled, as if captured in a real moment. Avoid cinematic lighting, dramatic color grading, or stylized composition.
```

Likeness rule: use a reference you have rights to. Ask for a generic person when you do not.

---

## 11. Failure modes, QA checklist, and fixes

### 11.1 QA checklist (read against the pixels)

- [ ] Deliverable is recognizable as that deliverable (poster looks like a poster, UI looks like UI).
- [ ] Subject is the one you named, not a cousin.
- [ ] Composition matches the brief (placement, crop, negative space).
- [ ] Light direction is the one you named.
- [ ] Materials look like the named materials.
- [ ] On-image text is spelled correctly, appears the requested number of times, sits where you asked.
- [ ] No surprise text, logos, watermarks, or extra objects.
- [ ] Hands, feet, gaze, and object contact are physical.
- [ ] Identity / product geometry survived if this was an edit.
- [ ] Transparency is real alpha, not a painted checkerboard.
- [ ] Diagram arrows and numbers are factually right.

### 11.2 Symptom → cause → fix

| Symptom | Likely cause | Fix |
|---|---|---|
| Generic stock photo | No deliverable, no lens, no light direction | Name the asset + one lens + one light |
| Right subject, wrong crop | No composition sentence | Lock thirds / negative space, or `@Sketch` |
| Extra words on the poster | Copy not quoted, or missing “exactly once / no other text” | Quote, count, place, forbid extras |
| Misspelled brand | Unusual token | Spell letter-by-letter; raise quality |
| Face drift after edits | Preserve list dropped | Restate likeness every turn; restart from last good file |
| Product looks redesigned | Edit bundled too many changes | Change only the requested part; lock geometry |
| Fake composite | No integration sentence | “Match existing light, contact shadow, white balance. Must feel photographed in the scene.” |
| Mannequin hands | No hand action | Name the grip / contact |
| Over-beautified skin | Missing anti-retouch | `real skin texture, no heavy retouching` |
| Mood words did nothing | `epic / cozy / premium` with no visuals | Replace with scale, color, light |
| Checkerboard background | `background` not set, or PNG not used | Triple requirement in §2.5 |
| Quality still bad at `max` | Vague prompt | Rewrite the brief. `max` will not invent missing facts |
| Edit undid a previous fix | Multi-change prompt or dropped invariants | One change; paste preserve list |
| Diagram looks pretty and is wrong | No verification step | Read every label; regenerate that region only |
| Two styles mashed into sludge | Equal style fusion | One base medium + one accent |
| `{BRAND}` or `[NAME]` painted as text | Placeholder left in the prompt | Replace every template token before you run |
| Transparent request saved as JPEG | JPEG has no alpha | `png` or `webp` + `background=transparent` |
| `output_compression` wrecked a logo | Compression applied to PNG | Compression is JPEG/WebP only |
| Consumer image too small for print | ChatGPT default often <1080p | Set `size` on the API |
| Quality cratered after migrating from Image 2 | Ladder shifted; `medium` is no longer the same spend | Remap Image 2 `medium` → 2.5 `high`; see §2.4 |

### 11.3 Anti-drift rules for long sessions

1. Download every accepted step.
2. After ~4–5 edits, start a new chat and attach the last good file.
3. Never say only “improve it” or “make it better.”
4. If two defects exist, fix the structural one (layout, identity, text) before the cosmetic one (grade, grain).
5. Keep a running “invariants” block and paste it every turn.

---

## 12. Teach another AI to write GPT Image 2.5 prompts

This is the section that turns the guide into a reusable skill. Paste the system prompt below into ChatGPT, Claude, Gemini, a local model, or an agent. Then give it a short brief. It will emit a GPT Image 2.5-ready prompt plus a settings recommendation.

### 12.1 System prompt (copy as-is)

```text
You are a GPT Image 2.5 prompt engineer.

Target models: gpt-image-2.5-flare (fast default) and gpt-image-2.5-sunburst (precision).
Product surface may be ChatGPT Images 2.5 or the Images / Responses API.

NON-NEGOTIABLE RULES
1. Do not use magic keywords: masterpiece, 8k, ultra detailed, trending on artstation,
   octane, unreal engine, --ar, --stylize, numeric attention weights.
2. Do not put size, quality, or background into the image prompt as adjectives.
   Recommend them separately as API/UI settings.
3. Start with the deliverable and its use.
4. Order: deliverable → subject → scene → composition → visual direction → text → constraints.
5. Camera terms are appearance cues, not physics.
6. Any literal on-image copy goes in quotation marks, with a count, a placement, and
   a type style. Always add "no other text" when text exists — or "no text" when it does not.
7. Edits must be one change. Separate EDIT TARGET from PRESERVE.
8. Every reference image gets exactly one role, addressed as Image 1, Image 2, …
9. Constraints are a short list. Do not write a novel of negatives.
10. Prefer visible facts (materials, light source + direction, named colors, body framing,
    hand contact) over mood words (cinematic, cozy, epic, premium, stunning).

WHEN THE USER BRIEF IS THIN
Ask up to 5 clarifying questions only if a missing fact would change the image:
deliverable/use, aspect, subject identity, exact copy, photoreal vs illustration.
If you must proceed, mark assumptions explicitly.

OUTPUT FORMAT — always use these four blocks

## Settings
- model: flare | sunburst
- quality: low | medium | high | xhigh | max
- size: WIDTHxHEIGHT or ChatGPT aspect
- background: auto | opaque | transparent
- format: png | jpeg | webp
- why: one sentence

## Prompt
A ready-to-paste prompt. Use labeled sections for complex jobs,
short ordered prose for simple photos.

## Edit variant
If the user is iterating on an existing image, also emit an edit prompt
in the shape: Change only X. Keep [invariants]. Do not add [exclusions].

## QA
3–6 things the user must inspect in the pixels after generation.

If the user asks for a brand-infringing logo, a real person's likeness
without a reference they own, or photoreal CSAM / non-consensual sexual
content, refuse that part and offer a generic original alternative.
```

### 12.2 Critic loop (second agent or second pass)

After the first AI writes a prompt, run this:

```text
You are a GPT Image 2.5 prompt critic. Score the prompt 0–2 on each item
and rewrite only the failing parts.

[ ] Deliverable and use are named
[ ] Composition / placement is specified
[ ] Light has source + direction
[ ] Materials are named
[ ] Palette is 3–5 named colors or explicitly default
[ ] People have framing, gaze, and hand contact (if people exist)
[ ] Exact text is quoted + counted + placed, or "no text" is stated
[ ] Reference roles are numbered (if refs exist)
[ ] Edit is one change with a preserve list (if this is an edit)
[ ] No magic keywords, no size/quality stuffed into prose
[ ] Exclusion list is short
[ ] Prompt is maintainable (could be edited next week)

Return:
1. Score table
2. Rewritten prompt
3. Settings recommendation
```

### 12.3 Few-shot pair to include in the teacher model

**User brief:** `coffee cup, cozy, professional`

**Bad prompt the student must not emit:**

```text
nice photo of a coffee cup, cozy vibes, professional, 8k, masterpiece
```

**Good prompt the student must emit:**

```text
A product photograph for a cafe landing-page hero.
A white ceramic coffee cup on a linen tablecloth.
Shot from a low angle, cup centered, the top third of the frame empty.
Photorealistic, soft morning light from a window on the left, shallow depth of field.
No text and no logos.
```

**Settings:** `gpt-image-2.5-flare`, `quality=medium`, `size=1024x1536`, `background=opaque`.

### 12.4 How you should practice (so you can teach it well)

Do 12 generations, one per playbook in §10. For each:

1. Write the brief in one sentence.
2. Expand it with the labeled spec.
3. Generate.
4. Run the QA checklist.
5. Do exactly one edit.
6. Save the final prompt next to the image.

After 12 cycles the format becomes muscle memory. That corpus is also the best fine-context you can give another model: 12 brief → prompt → defect → edit pairs.

### 12.5 Distilling this guide into an agent skill

If you drop this file into a coding agent or a custom GPT:

- Point the agent at **§5, §6, §7, §12.1** as always-on policy.
- Point it at **§10** as recipes.
- Point it at **§11** as a post-generation tool.
- Forbid it from inventing Midjourney flags.
- Require it to emit Settings + Prompt + QA every time.

---

## 13. Copy-paste templates

### 13.1 Blank generate

```text
DELIVERABLE
[asset] for [use], [aspect].

SUBJECT
[who/what], [materials], [pose or orientation].

SCENE
[place], [time], [supporting objects that are allowed].

COMPOSITION
[placement], [camera height + lens], [negative space].

VISUAL DIRECTION
[light source + direction + quality].
Palette: [color 1], [color 2], [color 3].
Medium: [photoreal photograph | editorial | flat vector | classroom diagram | …].

TEXT
Render exactly once: "[copy]".
Placement: [where]. Style: [weight, family, color].
No other text.

CONSTRAINTS
No watermarks, no extra logos, no extra objects, no heavy retouching.
```

### 13.2 Blank edit

```text
Change only [one thing] to [new value].

Keep exactly:
- [identity / product geometry]
- [crop and camera]
- [light direction and grade]
- [all other text]
- [shadows and reflections]

Do not add text, logos, props, or a new light source.
```

### 13.3 Blank multi-reference

```text
Image 1 = [role]. Use [these attributes] only.
Image 2 = [role]. Use [these attributes] only.
Image 3 = [role]. Use [these attributes] only.

Create [deliverable].
Combine them by [placement + light-match sentence].
Do not copy anything from a reference that is outside its assigned role.
```

### 13.4 Blank Sketch follow-up

```text
Turn this sketch into [medium].
Preserve the exact layout, proportions, and perspective of the sketch.
[Subject / materials / light].
Do not add new elements or text.
```

### 13.5 Surgical packaging-copy swap

```text
Replace ONLY the front-label line "Daily Hydration" with "Mineral Hydration".
Match the existing typeface appearance, weight, size, kerning, baseline,
ink color, and print texture. The replacement must fit the exact current text box.

Do not change bottle geometry, logo, cap, label dimensions, any other printed
copy, camera angle, crop, background, condensation, reflections, highlights,
shadows, or color grade.

The new copy must read exactly "Mineral Hydration".
No extra letters, alternate wording, or duplicate text.
```

---

## 14. Official technique catalog (quick index)

From the OpenAI Image Prompting Guide. Steal the *shape*, then swap content.

| # | Technique | What you learn |
|---|---|---|
| G1 | Photoreal sailor | Subject + texture + lens + light + anti-retouch |
| G2 | Coffee-machine infographic | Name the process and the audience |
| G3 | Thread streetwear ad | Exact tagline once + campaign deliverable |
| G4 | Field & Flour logo | Transparent, simple, original, padded |
| G5 | Bethel 1969 crowd | Real-world date/place as a constraint |
| G6 | 4-panel pet comic | Per-panel action, vertical reel |
| G7 | Farmers-market app UI | Shipped-screenshot language + device frame |
| G8 | Cellular respiration diagram | Labels, arrows, “classroom handout,” no tiny type |
| G9 | Series A market-opportunity slide | Real slide conventions + exact numbers |
| E1 | Translate infographic to Spanish | Change copy, lock layout |
| E2 | Style transfer onto new subject | Style from input, new content |
| E3 | Identity-locked wardrobe swap | Preserve likeness, replace clothes only |
| E4 | Place dog from image 2 into image 1 | Combine refs, “do not change anything else” |
| E5 | Transparent product cutout | Alpha, no checkerboard, preserve geometry |
| E6 | Drawing → photoreal | Preserve layout/perspective of the sketch |
| E7 | Remove object | One deletion, lock the rest |
| E8 | Insert person into grounded action scene | Anti-cinematic, reference identity |

Full wording for the main official prompts is in §10 and §9.

---

## 15. Reference sites and libraries

Learn from these in this order. Official first, then decoded write-ups, then prompt packs.

### 15.1 Official

| Resource | URL | Why |
|---|---|---|
| Image prompting guide (source of truth) | https://developers.openai.com/api/docs/guides/image-prompting | 8 rules, techniques, Flare/Sunburst, params |
| Image generation API guide | https://developers.openai.com/api/docs/guides/image-generation | Endpoints, masks, multi-image, code |
| ChatGPT Images 2.5 announcement | https://openai.com/index/introducing-chatgpt-images-2-5/ | Sketch, templates, product claims |
| Images in ChatGPT help | https://help.openai.com/en/articles/11084440-images-in-chatgpt | Templates, Sketch steps, aspect picker |
| OpenAI Academy: creating images | https://openai.com/academy/image-generation/ | Short consumer prompting advice |
| Sunburst model card | https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst | Pricing, rate limits, modalities |
| OpenAI Skills prompting notes | https://raw.githubusercontent.com/openai/skills/main/skills/.system/imagegen/references/prompting.md | Condensed internal-style rules |

### 15.2 Decoded guides (read after official)

| Resource | URL | Why |
|---|---|---|
| Felo: official guide decoded | https://felo.ai/blog/openai-gpt-image-2-5-prompting-guide-decoded/ | 8 rules + params + migration, clearly restated |
| OpenArt 2.5 prompt guide | https://openart.ai/blog/gpt-image-2-5-prompt-guide/ | Order, purpose-first, worked examples |
| Promptessor 2.5 prompting guide | https://promptessor.com/blog/gpt-image-2-5-prompting-guide | Best labeled generate/edit templates |
| OpenArt 2.5 specs overview | https://openart.ai/blog/gpt-image-2-5-overview-specs/ | Size, quality, feature table |
| CellCog Flare vs Sunburst / cost | https://cellcog.ai/blog/gpt-image-2-5-release-date/ | Quality-tier token costs |
| Tosea complete guide | https://tosea.ai/blog/gpt-image-2-5-complete-guide | API naming traps (`gpt-image-2.5` invalid) |
| GPT Image 2 field techniques | https://gpt-image2ai.org/en/blog/gpt-image-2-prompt-engineering | 12 transferable techniques (lens, palette, one-variable iteration) |

### 15.3 Prompt libraries (steal structure, then rewrite content)

| Resource | URL | Why |
|---|---|---|
| awesome-gpt-image-2-5-prompts | https://github.com/youart-open-source/awesome-gpt-image-2-5-prompts | 150 credited prompts, 9 use cases, verbatim |
| LaplaceYoung awesome-gpt-image-2.5 | https://github.com/LaplaceYoung/awesome-gpt-image-2.5 | Official samples + templates + case pages |
| wangrunlin multilingual pack | https://github.com/wangrunlin/awesome-gpt-image-2-5-prompts | Same idea, nine languages |
| Anil-matcha API prompt pack | https://github.com/Anil-matcha/Awesome-GPT-Image-2.5-API-Prompts | Reference fidelity, precision edits, API snippets |

Use-case folders in the youart pack (good study set):

- posters
- text-in-image
- infographics
- UI mockups
- product shots
- ad creative
- character design
- portraits
- illustration

How to study a borrowed prompt:

1. Copy it verbatim once and run it, so you see what the author actually got.
2. Highlight deliverable, layout, quoted text, camera, constraints.
3. Rewrite those five slots for your job. Do not paraphrase the quoted strings unless you intend to change the on-image copy.
4. Replace any `{PLACEHOLDER}` or `[BRAND NAME]` before running — the model will otherwise paint the placeholder.

### 15.4 Product extras worth knowing

- Sketch: type `@Sketch` in ChatGPT, or Images → Sketch.
- Templates: Images → Templates (Poster, Merch, product photo, flyer, logo, icon…).
- Share-with-prompt: send the image *and* the brief so someone can rerun it with their face or product.
- Region comments: click the image, comment on the spot that is wrong.

---

## 16. One-page field card

Keep this next to the keyboard.

```text
DELIVERABLE first.
Then subject, then where it sits in the frame, then light + material + medium.
Quote on-image text. Count it. Place it. Forbid extra text.
Short exclusions.
Settings live outside the sentence: model, quality, size, background.

Flare = draft / volume / already-good-enough.
Sunburst = final / identity / geometry / multi-turn edit.
quality climbs only to fix a measured defect.

Edit = Change only X. Keep [list]. Do not add [list].
One change per turn. Restate the list. Inspect pixels.
References get one role each: Image 1 = …, Image 2 = …

No masterpiece. No 8K. No weights.
If pixels must not move, composite them.
```

---

## 17. Changelog of sources used for this guide

Primary:

- OpenAI Image Prompting Guide (developers.openai.com/api/docs/guides/image-prompting)
- OpenAI Image Generation Guide
- Introducing ChatGPT Images 2.5 (8 Sep 2026)
- OpenAI Help: Images in ChatGPT (article 11084440)
- GPT-Image-2.5 Sunburst model card

Secondary (interpretation, templates, libraries, cost tables):

- Felo decoded guide, OpenArt prompt guide, Promptessor templates
- CellCog quality-tier costs, Tosea API naming notes
- GitHub prompt packs listed in §15.3
- OpenAI Academy image-generation page

Verify live parameter names and prices against the official docs before you ship a production integration. Model cards and rate limits move.

---

*End of gpt_image_operation_guide.md*
