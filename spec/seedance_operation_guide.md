# Seedance 2.0 / 2.5 Complete Operation Guide

**Prompt engineering for full control of ByteDance Seedance video generation**

Version: 2026-09-15  
Audience: creators, developers, and agent systems that must write Seedance-ready prompts on demand  
Output target: repeatable, director-level control — not lucky one-offs

---

## 0. Read this first

### 0.1 Seedance is a video model

Seedance 2.0 and Seedance 2.5 are ByteDance **video** generation models. They do text-to-video, image-to-video, multi-reference-to-video, first/last-frame animation, video editing, and video extension.

They are **not** still-image generators.

| Name | What it actually is | Typical output |
|---|---|---|
| **Seedance** | Video model | 4–15s (2.0) or 4–30s (2.5) clips with optional native audio |
| **Seedream** | Image model | Still images up to 4K, text-in-image, editing |
| **Jimeng / 即梦** | China-domestic creation app | Hosts Seedance + Seedream |
| **Dreamina** | International sibling of Jimeng | dreamina.capcut.com |
| **CapCut / 剪映** | Editor that surfaces the same models | Timeline-native generation |
| **Doubao / 豆包** | Consumer assistant that also runs Seedance | Chat + video workspace |
| **BytePlus ModelArk / Volcano Ark** | Official APIs | `dreamina-seedance-2-5-260628` and 2.0 family IDs |

Mnemonic: Seed**ance** puts things in motion. Seed**ream** paints a still.

If the job is a poster, keyframe, character sheet, or first frame, generate it in **Seedream** (or any still model), then feed that still into Seedance as a reference or first frame. This guide is the Seedance half of that pipeline.

### 0.2 The one rule that pays more than any other

**Describe motion, not subject. Structure the prompt like a production brief, not a poem.**

Vague mood paragraphs produce vague clips. Slot-structured prompts produce repeatable clips. Image-to-video rewards prompts that look more like shot instructions than creative writing.

### 0.3 What “complete control” actually means

You cannot force every pixel. You *can* lock:

1. Who / what is on screen (subject binding)
2. What happens, in what order, and when (action + timestamps)
3. How the camera sees it (one move per beat, film language)
4. What must not change (continuity + exclusions)
5. What the audience hears (audio brackets)
6. What each uploaded file is allowed to contribute (role + exclusion)

Everything in this guide exists to make those six locks reliable.

---

## 1. Model map — Seedance 2.0 vs 2.5

Numbers vary slightly by platform (Jimeng web, Dreamina, BytePlus, third-party APIs). Treat the table as the working production map, not a legal spec sheet.

| Dimension | Seedance 2.0 family | Seedance 2.5 |
|---|---|---|
| Model IDs | `doubao-seedance-2-0-260128` (standard) · `…-fast-260128` · `…-mini-260615` · international `dreamina-seedance-2-0-260128` | `doubao-seedance-2-5-260628` · international `dreamina-seedance-2-5-260628` |
| Single-pass duration | 4–15 seconds (often default 5s; `-1` = model-chosen) | 4–30 seconds native (`-1` = model-chosen). Extension toward 60s. Some surfaces expose an Ultra Long mode toward 180s |
| Output resolution | Official ModelArk: 480p / 720p / 1080p 8-bit + **4K 10-bit** on standard 2.0. Fast/Mini cap at 720p | Official ModelArk table: 480p 8-bit / 720p 8-bit / **1080p 10-bit**. **No 4K listed for 2.5.** Jimeng web, Together, and many hosts still cap 2.5 at 720p. Input 4K ≠ output 4K. Check the host you are on |
| Frame rate | 24 fps fixed | 24 fps fixed |
| Aspect ratio | 16:9, 4:3, 1:1, 3:4, 9:16, 21:9, adaptive | Same named ratios, plus adaptive in roughly 0.4–2.5. Edit / first-last-frame / extend often **force adaptive** |
| Reference images | Up to 9 | Up to **30** (each ≤4K, typically ≤30 MB) |
| Reference videos | Up to 3, combined ≤15s | Up to **10**, combined ≤30s |
| Reference audio | Up to 3, combined ≤15s; usually cannot be the only reference | Up to **10**, combined ≤30s; **audio-only reference is allowed** |
| Total reference budget | ~12 | **50** (30 + 10 + 10) — three separate budgets, not one pool of 50 |
| Timing syntax | Shot numbers (`Shot 1`, `Shot 2`) are reliable. Precise `0–3s` timestamps are weak | Whole-second timestamps **are first-class**. Continuous ranges, no gaps |
| Audio | Native audio on later 2.0 surfaces; weaker lip-sync | Co-generated audio is default. Dedicated bracket syntax. Stronger lip-sync. 10+ languages |
| Editing | Limited / regenerate the whole clip | First-class region / subject / audio edit. Quality holds better after a fix |
| Extension | Weaker chaining | First-class “extend / continue” with continuity |
| Blockout / 3D white model | Not a first-class input | Supported on some surfaces: lock camera path and proportions from a previz |
| Prompt adherence | Baseline | Officially cited ~20% better |
| Prompt length budget | Short clips tolerate 60–150 words | Chinese ≤ ~500 characters is safer than an essay; English ≤ ~1000 words. **Clearer beats longer.** Two to four tight blocks beat one 400-word paragraph |
| When to pick it | Short hero clip, maximum pixels, cheap iteration, single subject doing one thing | 15–30s narrative, multi-shot, multi-reference, dialogue, edit, extend, one-take arcs |

**Compatibility:** A well-written 2.0 prompt usually runs on 2.5 unchanged. The upgrade path is: keep the 2.0 grammar, then add timestamps, `@` role binding, audio brackets, and a consistency tail.

**Version choice in one line:**

- Need 1080p / 4K and a 5–12s punch? → **2.0 standard**
- Need volume / cheap drafts? → **2.0 Fast or Mini**
- Need a 20–30s story, references, dialogue, or an edit? → **2.5**

Generation parameters (duration, ratio, resolution, `generate_audio`) live in the UI / API. **Do not write “make it 4K 30 seconds 9:16” inside the prompt** except in Ultra Long mode, where restating duration and ratio at the top is sometimes required.

---

## 2. Where to run it

### 2.1 Official and first-party

Hong Kong / international first: **Dreamina** at https://dreamina.capcut.com (Google / email / TikTok login, no +86). CapCut’s AI Video tools expose the same model as Dreamina Seedance. Jimeng / Doubao remain the fullest CN surfaces but account and payment paths differ.

| Surface | URL / entry | Notes |
|---|---|---|
| Dreamina (international) | https://dreamina.capcut.com | English UI. Best first stop outside mainland CN |
| CapCut / 剪映 | CapCut AI video tools | Model listed as Dreamina Seedance. Drops onto the timeline |
| Jimeng / 即梦 web | https://jimeng.jianying.com | Fullest consumer surface in CN. Phone / Douyin login. Video Generation → pick Seedance 2.0 or 2.5. 白模 / blockout lives here |
| Jimeng App | Search「即梦」or「即梦 AI」 | Same credit pool as web |
| 小云雀 | https://xyq.jianying.com | Fast consumer remix / “same style” workflows |
| Doubao / 豆包 | https://www.doubao.com | Pro workspace exposes Seedance 2.5 |
| ByteDance Seed | https://seed.bytedance.com/seedance2_5 | Research homepage + model cards, not the generator |
| Volcano Engine Ark | https://www.volcengine.com/product/ark | CN developer API |
| BytePlus ModelArk | https://docs.byteplus.com/en/docs/ModelArk/2607689 | International API. Model ID `dreamina-seedance-2-5-260628` |

### 2.2 Common third-party API hosts

Fal, Together, Replicate, Segmind, PiAPI, and various CN aggregators (API易 and others) proxy the same model IDs. Prompt syntax is the same. Parameter names and whether 1080p is exposed are **not** the same. Always set duration / ratio / resolution in the host’s parameter panel, not in the prompt text.

### 2.3 Suggested credit strategy

1. Draft at 480p or 720p, 5–8 seconds, 2.0 Fast or 2.5 short.
2. Lock subject, motion, and camera.
3. Only then spend a 15–30s 2.5 pass or a 2.0 high-res hero pass.
4. Keep reference count in the stable band (see §11). More files are not automatically more control.

---

## 3. Core philosophy — how Seedance actually reads a prompt

### 3.1 Weight order

Empirically, the model attends in roughly this order:

1. **First 20–30 words** — subject + primary action lock here
2. **Uploaded references, in upload order** — earlier files weigh more
3. **Explicit `@` bindings and exclusions**
4. **Timestamped beats / shot list**
5. **Camera instruction inside each beat**
6. **Audio brackets next to the event they belong to**
7. **Global consistency tail**
8. **Style adjectives and quality words** — weakest signal

This is why “cinematic, epic, 8K, masterpiece, ultra detailed” at the end does almost nothing, and why a muddy opening sentence ruins a beautiful second paragraph.

### 3.2 Four laws

**Law 1 — One job per unit.**  
One primary action per sentence. One camera move per beat. One job per reference file. One change per 30s stage. A unit asked to do three things produces mush.

**Law 2 — Motion is physical.**  
Write contact, force, secondary motion, and the end state. “Fights elegantly” is a wish. “Left palm slaps the incoming wrist, right short-staff pins the blade, shoulder drives the chest, opponent’s back hits the snow” is a shot.

**Law 3 — Say what to use and what not to use.**  
References leak. Backgrounds leak. Extra people leak. If you do not write the exclusion, the model will steal the part you did not want.

**Law 4 — Parameters are not prompt words.**  
Duration, aspect, resolution, seed, `generate_audio` belong in the control panel. Putting them in the text wastes the attention budget and is ignored or misread.

### 3.3 2.0 grammar vs 2.5 grammar

2.0 prompting is *writing a shot*.  
2.5 prompting is *filling out a build file*.

| 2.0 habit that still works | 2.5 addition you should start using |
|---|---|
| Subject + action + camera + light + style | Timed beats with end states |
| One camera move + one secondary motion | `@Image N` role + exclusion for every file |
| “Keep appearance consistent” | `[Maintain Consistency]` block that lists the actual attributes |
| Shot 1 / Shot 2 | `0–6s` / `6–14s` continuous ranges |
| Ambient sound as a sentence | `(music)` `<sfx>` `{dialogue}` `【title】` |
| Short 60–100 word prompts | Four-block production template for anything >12s |

---

## 4. End-to-end operation workflow

Use this as the default operating procedure. Do not skip steps 1–4 to “save time.” Most wasted credits come from generating before the brief is locked.

### Step 1 — Decide the job, not the vibe

Write one sentence:

> Platform + duration + ratio + task type + one sentence of what happens + what must be identical if I rerun this.

Examples:

- 9:16 / 8s / I2V / product hero: bottle rotates, label readable, no new props.
- 16:9 / 30s / T2V / wuxia one-take: female swordsman vs assassin in a bamboo inn, identity locked to Image 1.
- 16:9 / edit / replace the background of Video 1 with a rainy neon alley, keep the walk cycle.

If you cannot write that sentence, you are not ready to prompt.

### Step 2 — Pick the task type

See §5. The task type decides which parameters are free and which are locked. Wrong task + right prose still fails.

### Step 3 — Set UI / API parameters first

- Model: 2.0 / 2.0 Fast / 2.5
- Duration: 4–15 (2.0) or 4–30 (2.5), or `-1`
- Ratio: 16:9, 9:16, 1:1, 21:9, adaptive
- Resolution: draft low, final high
- `generate_audio`: on if you will direct sound; off if you will score in post
- Seed: lock it once a take is close, so you can change one variable at a time

### Step 4 — Prepare assets

- Official 2.0 working recipe, still the right instinct on 2.5: **1–2 character stills (face + full body) + 1 scene still + 1 camera-move video + 1 audio**. Do not max the quota to feel in control.
- Faces: held pose, clear light, no heavy filters, no burned-in labels. Mid-action identity photos cause drift.
- Products: 1–3 angles of the *same* object. Isolate from people and busy backgrounds
- Motion refs: 5–10s, one action, readable camera
- Voice refs: one speaker per file, dry if possible
- Storyboards: line art, ≤15 panels, almost no text
- Blockouts: simple geometry. Strip motion paths, axes, and frustums so they do not leak into the render

Upload order is priority. **Slot 1 is whatever you most need preserved.** For a real person, that is always the face.

### Step 5 — Write the prompt in blocks

Use the templates in §6. Fill only the slots you intend to control. Empty slots are decisions you are giving the model — that is allowed and often better.

### Step 6 — Generate a cheap probe

5–8 seconds, low res, same seed after the first keeper. Ask only:

- Is the subject the right subject?
- Is the primary action visible?
- Is the camera doing one thing?
- Did a reference leak (wrong clothes, wrong room, extra person)?

### Step 7 — Change one variable

If the face drifted, do not also rewrite the camera and the audio. One change per reroll or you cannot learn.

### Step 8 — Scale duration and references

Only after the short probe is stable: stretch to 15–30s, add beat timestamps, add audio brackets, add the consistency tail.

### Step 9 — Edit or extend instead of regenerating the universe

2.5 can replace a subject, swap a background, restripe a language, or continue 5–15s. Use those modes when 80% of the take is already right.

### Step 10 — Archive the working prompt

Store: prompt text, model, duration, ratio, seed, asset list with roles, what failed, what fixed it. A prompt library compounds. A chat history does not.

---

## 5. Task modes and parameter locks

BytePlus / Jimeng classify the request from (a) the assets’ `content.role` and (b) verbs in the prompt. If those two disagree, the job can fail with a task-type mismatch and you still may be billed on some hosts.

### 5.1 Mode table

| Task | What you give it | Prompt trigger | Locked settings | What the prompt should do |
|---|---|---|---|---|
| **Text-to-video** | Text only | No asset verbs required | Nothing. You choose ratio and duration | Invent subject, action, camera, sound |
| **Reference-to-video (R2V)** | Text + images / videos / audio as `reference_*` | `@Image 1` / `@Video 1` / `@Audio 1` plus a role sentence | Nothing locked. Assets are semantic | Bind every file. Do not re-describe what a file already proves |
| **Image-to-video / first frame** | 1 image as `first_frame` + motion text | “animate this image”, “start from this frame” | Ratio often locked to the image | Describe **only motion + camera**. Keep lighting/composition |
| **First + last frame** | 2 images as `first_frame` + `last_frame` | “from this frame to that frame” | Ratio locked to first image. Last frame of a different ratio gets stretched | Describe the journey between the two stills. Do not invent a third location |
| **Video editing** | Source video + optional replacement assets | **Must contain an edit verb**: add / remove / replace / modify / 增加 / 删除 / 替换 / 修改 | `ratio: adaptive`, `duration: -1`. Output follows source ratio and approximate duration | Name the master video, name the scope, name what stays |
| **Video extension** | Source video + optional new refs | **Must contain an extend verb**: extend / continue / 向后延长 / 续写 / 延续 | Ratio locked to source. Duration is the *new* length you set | Start from the last frame’s state. Do not restart the story |

### 5.2 Official input recommendations (stability, not the hard cap)

| Input | Hard cap (2.5) | Stable working range |
|---|---|---|
| Images | 30, each ≤4K | 1–8 distinct subjects. Split crowded photos |
| Videos | 10 clips, ≤30s combined | 1–5 subjects, 5–10s each. Edit sources under 20s |
| Audio | 10 clips, ≤30s combined | 1–5 voices. State whether each file is voice, melody, or rhythm |
| Storyboard grid | — | ≤15 panels, line art, almost no text |
| Blockout | — | Simple geometry. No gizmos in frame |
| People / products in one clip | — | Reliable to about **8** identities. Past that, expect swaps |

---

## 6. Official prompt formulas

Memorize two. Use the short one for clips under ~12s. Use the long one for everything else.

### 6.1 Six-part formula (official 2.5, also the 2.0 backbone)

```text
Subject + Action or Event + Scene and Environment + Visual Style + Camera Movement or Cut + Audio
```

Only **Subject** and **Action** are required. Slots 3–6 are optional. Filling every slot with decoration is how prompts fight themselves.

Sentence form:

```text
<Subject> performs <primary action or event> in <scene and environment>.
The visuals feature <visual style>.
Use <shot size, camera angle, camera movement, or cuts>.
Audio includes <dialogue, ambience, sound effects, or music>.
```

Worked six-slot example:

```text
A ceramicist in a linen apron lifts a finished bowl from the wheel and turns it slowly in the light, in a cluttered studio at golden hour with clay dust in the air, warm 35mm film look with soft halation, slow push in that settles on her hands, (sparse piano) <wheel slowing, clay scraping>.
```

### 6.2 Four-part production template (the 2.5 build file)

Use this the moment you have references, more than one shot, or more than 12 seconds.

```text
[Asset mapping]
[One-sentence brief]
[Timeline / shot order]
[Global constraints]
```

Expanded:

```text
Asset mapping:
@Image 1 defines <who/what> — use only <attributes>. Do not use <leaks>.
@Video 1 defines <motion or camera>. Do not use <identity/scene>.
@Audio 1 defines <voice / music / rhythm>.

One-sentence brief:
<Subject> + <location> + <event> + <genre/style> + <special camera treatment>.

Timeline:
0–Xs: <shot size + camera> <action> <end state> <sound>
Xs–Ys: ...
End state of last beat: <what the last frame must show>.

Global constraints:
Keep <identity, wardrobe, prop, layout, grade> constant.
No <subtitles / extra people / style drift / morphing>.
Audio: <what is allowed>.
```

### 6.3 Image-to-video six-slot (2.0 developer anatomy — still the best I2V skeleton)

When a still already defines look and composition, stop re-describing the still.

```text
1. Subject action      — what the main subject does
2. Secondary motion    — hair, cloth, steam, water, eyes
3. Camera move         — exactly one, with a pacing word
4. Environment beat    — light / weather / ambient motion only
5. Style anchor        — photographic / cinematic / handheld / studio
6. Negative constraint — what must NOT happen
```

Target length: **60–100 words**. Hit four to six slots.

### 6.4 Chinese five-element director formula (still valid)

```text
[角色指定] + [场景设定] + [动作/剧情] + [镜头语言] + [氛围/声音]
```

Same information as the six-part formula. Use whichever language you will actually generate in. Mixed-language prompts work; mixed-language *priorities* do not. Pick one spine language.

### 6.5 中文速记条（可贴在工作台旁边）

```text
2.5 四块：素材职责 → 一句简报 → 连续时间轴（每段一件事+结束状态）→ 全局锁定
素材：@图1 只定脸/发型，不要背景。@视频1 只定运镜，不要身份。
音频：(配乐) <音效> {对白} 【字幕】
对白：先写语言+口音+语气，再写 {原句}。不要中英夹杂整句对白。
运镜：每一拍只做一个动作。推镜/拉镜/横移/摇镜/环绕/手持/一镜到底。
禁写进提示词：时长、比例、分辨率、8K、masterpiece。
任务词：编辑必须写「编辑/替换/删除 @视频1」；延长必须写「延长/续写 @视频1」。
不要写「参考 @视频1」去做编辑——模型会当成普通 R2V，锁失效。
```

---

## 7. Slot-by-slot instruction list

### 7.1 Subject — be specific enough to hold for 30 seconds

Use the **7-slot character formula** when the face is invented in text rather than locked to a photo:

```text
[age / ethnicity] + [skin tone and texture] + [3–4 facial landmarks]
+ [eyes / expression] + [hair] + [clothing and fabric] + [build / mood]
```

The skin slot should end with a physical lock: `keep real fine pores and skin texture`. Name the emotion through a visible face change (`eyes redden, mouth corners drop`), not through `sad`.

Vague: `a woman`  
Holds: `a woman in her thirties, short black bob, red wool coat, pale gold hoop earrings, calm closed-mouth expression`

For products: name the object, material, finish, and the one graphic that must stay readable.

```text
a matte-black reusable bottle with a brushed steel lid and a cream label that reads "RIVER" in condensed sans
```

Subject rules:

- Age band, hair, clothing, one identifying prop.
- Real-person work: bind the face to `@Image 1` and list the attributes that image is allowed to give.
- Two states of the same person (clean / wounded, day / armor) = two image slots, each bound to a time range.
- Do not put character names inside the reference pixels. Bind names in text.

### 7.2 Action — one visible arc with an end state

Write cause → contact → result.

Weak: `she fights with a sword`  
Strong: `she draws, the first cut meets the incoming dagger in a burst of orange sparks, both blades lock, she shoves the assassin back two steps`

Rules:

- Opening sentence = one action, not four.
- Every beat needs an **end state** the next beat can inherit: “the door has swung shut behind her.”
- Secondary motion is how clips feel alive: hair lift, coat flare, steam, rain off a brim, cloth settle, eyes blink once.
- For fights and dance, write the body mechanics (feet, hip, shoulder, contact point), not the school name alone.
- Cap spoken lines around 16 words. Longer lines desync.

### 7.3 Scene and environment

Give the model surfaces, light sources, and spatial relations.

```text
rain-covered alley, flickering neon in kanji, steam from a subway grate, wet asphalt reflections, one working streetlamp
```

Rules:

- Name 3–5 concrete nouns. Stop.
- Weather and time of day do more than “atmospheric.”
- If a reference image already is the location, say so and forbid its people.

### 7.4 Visual style — specify the medium, not the adjective

“Cinematic” is a shrug. A medium sentence is a lock.

Good style locks:

- `warm 35mm film look, soft halation, gentle grain, slightly lifted blacks`
- `ARRI Alexa texture, restrained highlight roll-off, fine 35mm grain`
- `handheld early-2000s home DV, rolling shutter, imperfect white balance, tape softness`
- `guofeng 2.5D anime, ink-wash edges, flat fill, no 3D grease`
- `clean commercial product photography, high-key, hard floor reflection`
- `documentary available-light, 50mm, skin texture preserved`

For photorealism on CN surfaces, practitioners still append `真人实拍` near the end. Placement matters: keep it in the style slot, not beside dialogue, or the model may start speaking Chinese.

Do **not** stack `8K, HDR, masterpiece, ultra detailed, best quality`. Those words burned attention in 2023 and still steal it now.

### 7.5 Camera — see §8

One move per beat. Pair every move with a speed word: `slow`, `smooth`, `gentle`, `fast`, `violent`.

### 7.6 Audio — see §10

Direct it. If you say nothing, 2.5 will invent a score and sometimes burn in subtitles.

### 7.7 Constraints — see §15

Write the two or three failures this exact shot is likely to produce. A generic ban-list is weaker than a local one.

---

## 8. Camera language — the control surface that changes the shot fastest

Seedance understands plain film terms. Official docs list static, pan/tilt, zoom/focus, dolly/tracking, aerial/crane, and specialty moves. Use the term **and** a visible result if the move is uncommon.

### 8.1 Shot size

| Term | Shows | Use |
|---|---|---|
| Extreme close-up | Eye, mouth, texture, logo | Tension, material proof |
| Close-up | Face or one object | Emotion, product hero |
| Medium close-up | Head and shoulders | Dialogue |
| Medium | Waist-up | Everyday action |
| Wide / full | Whole person + setting | Body action, blocking |
| Extreme wide / establishing | Whole environment | Openings, scale |

### 8.2 Angle

| Term | Effect |
|---|---|
| Eye level | Neutral, conversational |
| Low angle / worm’s eye | Power, hero, threat |
| High angle | Vulnerability, observation |
| Overhead / bird’s eye / top-down | Geography, ritual, food, layout |
| Dutch / canted | Unease. One per scene, then stop |
| POV / FPV | Immersion. Declare whose eyes |

### 8.3 Movement lexicon (EN / 中文)

| Family | English wording that works | 中文 | What it does |
|---|---|---|---|
| Static | `static shot`, `locked-off camera`, `no camera movement` | 固定镜头 / 锁机 | All motion comes from the subject |
| Dolly in | `slow dolly-in`, `slow push-in from medium to close-up` | 推镜 | Camera walks toward the subject |
| Dolly out | `slow pull-back`, `dolly out to reveal the room` | 拉镜 | Camera retreats, reveals context |
| Track / truck | `side tracking shot at shoulder height`, `track left with the runner` | 横移 / 跟拍 | Camera travels with the subject |
| Pan | `smooth pan right across the skyline` | 摇镜（左右） | Tripod yaw. Horizon stays level |
| Tilt | `tilt up from the shoes to the face` | 摇镜（上下） | Tripod pitch |
| Pedestal | `pedestal up from 0.8m to 2.2m, lens level` | 升降（垂直） | Elevator move, no arc |
| Crane / jib | `crane up from street level to rooftop` | 摇臂 / 升降 | Vertical plus a little arc |
| Orbit / arc | `slow 180-degree orbit`, `smooth 360 arc keeping subject centered` | 环绕 | Circles the subject |
| Steadicam / gimbal | `steadicam follow through the corridor` | 斯坦尼康 / 稳定器 | Smooth walk-and-follow |
| Handheld | `handheld documentary, slight breathing shake` | 手持 | Intentional instability |
| Aerial / drone | `aerial descending toward the courtyard` | 航拍 | Height + travel |
| FPV | `FPV continuous long take through the alley` | 穿越机 | Aggressive 3-axis |
| Whip pan | `whip pan right, smear, land on composition B` | 甩镜 | Fast rotational cut-in-camera |
| Zoom (optical) | `slow zoom in on the eyes` (no parallax) | 变焦 | Focal length only |
| Crash / crush zoom | `violent crash zoom out in 0.4s, then hold` | 暴焦 | Stylized punctuation |
| Dolly zoom | `dolly in while zooming out, head size constant, background stretches` | 希区柯克变焦 | Vertigo |
| Rack focus | `rack focus from the glass in the foreground to the woman` | 拉焦 | Focus plane travels, camera does not |
| One-take | `one continuous take, no cuts` | 一镜到底 | Forbids editorial chopping |

### 8.4 Speed words

`slow` · `smooth` · `gentle` · `steady` · `sudden` · `fast` · `violent` · `unhurried`

“Fast” alone is weak. Prefer a named move: `whip pan`, `crash zoom`, `explosive burst out of frame`.

### 8.5 Combination rules

1. **One decisive move per beat.** Pan + orbit + crane in the same 8 seconds is mud.
2. Formula: `[size] + [angle] + [move] + [speed]`.  
   Example: `medium low-angle slow push-in`.
3. For one-takes, write the *path*: where the camera starts, what it passes, where it lands.
4. Uncommon moves need the visible result, not only the name:

```text
Starting at second 4, rack focus: the sharp glass in the foreground
gradually softens while the woman in the background moves from
blurred to sharp. Camera position does not change.
```

5. Do not put focal-length numbers in unless you also describe the look. `35mm, slight barrel, subject large in frame` beats `35mm` alone.
6. Never fight the style slot. `locked-off symmetrical` and `handheld vérité` cannot both win.

### 8.6 Transitions you can prompt (2.5)

Prefer transitions the camera can photograph. Do fades and wipes in an editor when you can.

| Type | Prompt cue |
|---|---|
| Hard cut | `cut to interior` |
| Match cut | `the full moon holds center; it resolves into the round wine bowl` |
| Whip pan | `whip pan right, smear, land on composition B` |
| Occlusion / mask | `a giant bamboo leaf crosses the lens to black; when it clears…` |
| Action relay | `her hand slams the door; on the impact, cut to the alley` |
| Zoom-through | `the camera dives into his pupil until the reflection fills the frame` |
| Ink-wash | `on the click of the sword seating, the frame blooms into ink` |

If a transition can fire too early, forbid it in the global block: `the ink-wash may only appear after the 25s click — never earlier.`

### 8.7 Default camera recipes

| Goal | Recipe |
|---|---|
| Product hero | `slow 180 orbit, then a gentle dolly-in to the logo, locked horizon` |
| Face / talking head | `static medium close-up, eye level, very slow push-in, no tilt` |
| Reveal | `start tight, slow pull-back to wide` |
| Intimacy / decision | `slow push-in from medium to close-up` |
| Chase | `shoulder-height tracking shot, occasional whip onto the pursuer` |
| Scale | `crane up, subject stays in the lower third` |
| Documentary | `handheld, breathing micro-shake, recover the frame` |
| Wuxia impact | `low-angle tracking + 0.12–0.18s speed ramp on the clash, then wide` |

---

## 9. Lighting, color, and medium texture

Lighting is the single highest-leverage look word after the subject. Use **one** lighting sentence.

### 9.1 Lighting phrases that actually change the image

- `soft morning window light from camera left`
- `golden-hour backlight, rim on hair, face slightly underexposed`
- `overcast daylight, soft shadows, cool pavement bounce`
- `high-key studio, large softbox overhead, clean floor bounce`
- `moody single practical: a warm bulb in frame, everything else falls off`
- `neon split: cold cyan from the left, magenta kick from the right`
- `moonlit frost-blue key, snow bounce, one dark-orange coal glow for contrast`
- `hard noon sun, sharp nose shadow, heat shimmer`

Write direction + quality + color. Stop.

### 9.2 Color / grade

- `low saturation, bright and clear, cold-warm contrast`
- `teal and orange feature grade, skin protected`
- `faded 1970s 16mm: warm highlights, weak blacks, slight green cast`
- `ink-wash after the sword click — not before`

### 9.3 Medium texture (this is how you stop “AI video” look)

Pick **one** capture system and list its defects:

```text
early-2000s home DV: mild smear on pans, uneven auto-exposure,
consumer wide-angle distortion, tape hiss in the audio
```

```text
35mm theatrical: fine grain, gentle halation on practicals,
24fps cadence, no plastic skin
```

Do not mix DV artifacts with Alexa cleanliness in the same prompt.

---

## 10. Audio syntax — treat sound as a directed channel

On 2.5, audio is generated with the picture. If you do not direct it, you get a generic bed and sometimes burned-in captions.

### 10.1 Four official brackets

| Bracket | Channel | Example |
|---|---|---|
| `( )` | Music / ambient bed | `(low cello drone, no beat drop)` |
| `< >` | Sound effects, one physical event per bracket | `<door latch>` `<rain on glass>` |
| `{ }` | Spoken dialogue | `{We should go.}` |
| `【 】` | On-screen title / subtitle | `【Chapter One: Departure】` |

`{dialogue}` and `【subtitles】` are **different channels**. If you want both, write both. If you want neither burned-in text, say `no subtitles` in the global tail.

### 10.2 Dialogue formula

```text
Dialogue language: <language + region/accent>.
<Speaker> says <delivery>: {line}
```

Example:

```text
Dialogue language: British English, warm and low.
The courier says quietly: {One more stop before work.}
```

```text
对白语言：香港粤语，语速自然，不要书面腔。
女侠低声说：{今晚唔好出街。}
```

Supported well across 10+ languages, including mixed-language scenes if each speaker is labeled.

Rules:

- Declare language and delivery *before* the braces.
- Keep lines short.
- Put the line next to the beat where the mouth must move.
- Do not mix Chinese and English inside one spoken line except proper nouns. Non-ZH/EN must be labeled: `The girl says softly in Japanese: {もう大丈夫です}`
- 2.5 speech languages commonly include EN, ZH, ES, ID, MS, TH, AR, PT, VI, JA, KO. Language is named in the prompt, not a separate API field.
- If you need silence: `No BGM. No score. Only wind, cloth, and footsteps.`

### 10.3 Sound design rules

- Two or three specific sounds beat a paragraph of ambience.
- Write sounds as physical events: `chain click`, `wet tire hiss`, `sword seat click`.
- Sync music to picture only if you say so: `cut on the kick`, `flashes land on the snare`.
- Off-screen sound is allowed and useful: `<a siren passes left to right, never seen>`.

---

## 11. Reference binding — the real 2.5 upgrade

Uploading a file does nothing by itself. The prompt must employ it.

### 11.1 Numbering

Files are numbered by **upload order**, not by type:

- First image → `@Image 1`
- Second image → `@Image 2`
- First video → `@Video 1`
- First audio → `@Audio 1`

Syntax variants seen in the wild that the model accepts: `@Image 1`, `@Image1`, `@image1`, `@图片1`, `@图1`. Pick one scheme and stay consistent inside a prompt.

### 11.2 Every file gets a job and an exclusion

```text
@Image 1 defines Mara's face, hair, and dark green apron.
Do not use the image background. Do not use her pose.

@Image 2 defines the wooden workbench, window placement, and morning light.
Do not use the people in the image.

@Video 1 defines only the pacing of both hands throwing clay, lifting the cup, and setting it down.
Do not use the person's identity, clothing, or room.

@Audio 1 defines Mara's speaking voice only.
Do not use its background music.
```

The officially forbidden pattern:

```text
@Images 1 through 4 define four characters respectively.
```

That sentence never says who is who. Map one by one.

### 11.3 Priority and mention rules

- Earlier uploads weigh more. `@Image 1` = the thing you cannot afford to lose.
- Mention every uploaded file. An unmentioned file often fails to bind.
- Re-mentioning a file later in the prompt increases adherence.
- One identity ↔ one file. Two files that both “define the jacket” will blend.
- Introduce references scene by scene in long pieces. Do not force the whole cast into frame one.

### 11.4 What each modality is good for

| Asset | Good at | Bad at |
|---|---|---|
| Still of a face, held pose | Identity | Inventing a walk cycle |
| Multi-view product pack | Structure, materials, logo | Motion |
| Style still with no people | Grade, palette, lighting | Acting |
| 5–10s motion clip | Timing, body mechanics, camera path | Donating its actor’s face unless you allow it |
| Voice clip | Timbre, pace | Forcing words you did not write |
| Storyboard grid | Shot count and order | Pixel-accurate framing |
| Blockout / white model | Camera path, blocking, timing | Surface look (you must describe look in text) |

### 11.5 Subject profile block (reuse this for series work)

```text
[Subject Profile: Conservator]
Appearance and clothing: @Image 1.
Fixed prop: sample case from @Image 5.
Locations: conservation lab, gallery.
Motion references: case-opening from @Video 1.
Do not use other characters' clothing.
Do not give this character the record board.
```

### 11.6 Image-to-video binding when the still is the whole look

```text
Use the uploaded image as the full appearance reference.
Keep the subject, clothing, colors, and background exactly as shown.
Add only this motion: she turns her head slightly toward the light,
blinks once, and takes one step forward.
Camera: slow push-in from medium to medium close-up.
No new props, no face redesign, no wardrobe change.
```

---

## 12. Timestamped beats — how 30 seconds stops wandering

A 12-second prompt can be one paragraph. A 30-second paragraph wanders, rushes the middle, or freezes one moment.

### 12.1 Beat rules

1. **3–5 beats** for a 30s clip. Four is the default.
2. **One job per beat.** One location change *or* one emotional turn *or* one camera move.
3. **Continuous ranges, no gaps:** `0–6s`, `6–14s`, `14–24s`, `24–30s`.
4. Every beat states: camera + action + **end state**.
5. Name transitions or the model will morph: `cut to interior`, `whip pan into the clash`, `the door closes, hold`.
6. Carry continuity across gaps: same coat, same bottle, same hallway.

2.0 note: prefer `Shot 1 / Shot 2` if timestamps misbehave on 2.0. 2.5 honors whole seconds.

### 12.2 Opening / middle / close skeleton

```text
Opening (0–5s) — lock the scene.
Who is in frame, where, lighting, reference anchors, baseline camera.

Middle (5–22s) — one development.
The action that justifies the clip. One camera idea.

Close (22–30s) — land.
A readable final frame you could pause on. No new location, no new character.
```

### 12.3 Stage template (copy this)

```text
[Generation Goal]
<Video type and the single central event.>

[Stage 1]
Initial state: ...
Primary event: ...
End state: ...

[Stage 2]
Continue from the previous end state.
Primary event: ...
End state: ...

[Stage 3]
Closing event.
Final state: ...

[Maintain Consistency]
Keep <face, wardrobe, prop, layout, grade> identical across stages.
```

### 12.4 Worked 30s narrative (no references)

```text
A 30-second night scene.

0–6s: A woman in a red raincoat waits alone at a rain-soaked bus stop.
Sodium streetlights. Static wide shot. She checks her watch.
End state: she is still at the stop, looking down the street.

6–14s: A vintage car pulls into frame, headlights flaring through the rain.
Slow push-in as she leans down to the passenger window.
End state: she has one hand on the door.

14–24s: Cut to the car interior. Warm dashboard glow. She laughs at
something the driver says, shoulders dropping. Rack focus from her
face to the rearview mirror.
End state: she is seated, door closed.

24–30s: Exterior. The car pulls away down the empty street, taillights
receding. Crane up to the skyline.
End state: small red lights in a wet black street.

Keep the same face, red raincoat, and rain density throughout.
<Tire hiss> <soft wiper> (low, distant jazz, no vocal)
No subtitles.
```

---

## 13. Image-to-video — the mode most people write wrong

When you upload a still as first frame or as the look reference, the image already won subject, wardrobe, composition, and often lighting. The prompt’s only job is **what changes**.

### 13.1 I2V laws

1. Do not re-describe the person in the photo.
2. Ask for motion that the still could physically continue.
3. One primary motion + one secondary motion.
4. One camera move, with a pace word.
5. Add `keep the existing lighting and composition` when you want fidelity rather than reinterpretation.
6. Add `maintain exact appearance from the reference image, no facial drift, no clothing change`.
7. Calm portraits want small motion. Action stills can take a larger move. Mismatch is the usual uncanny result.

### 13.2 Copy-ready I2V templates

**Portrait breathe**

```text
The subject turns the head slowly toward the window.
Hair lifts gently in a soft breeze, eyes blink once.
Static medium shot, no camera movement.
Soft morning light from the left, preserved from the image.
Photographic, natural pace.
No warping, no zoom, no background drift.
```

**Product orbit**

```text
The product rotates slowly on its vertical axis.
Highlights crawl across the surface.
Smooth slow orbit.
Clean studio, even key, preserved from the image.
Commercial product photography.
No logo distortion, no texture warping, no shadow flicker.
```

**Landscape live**

```text
Distant clouds drift slowly to the right.
Foreground grass sways, water ripples.
Slow dolly forward, steady.
Late-afternoon golden hour preserved.
Cinematic, shallow depth of field preserved.
No time-lapse, no flicker, no frame drift.
```

**Identity-locked page turn**

```text
The character looks down at the book and turns one page.
Hair settles, shirt fabric shifts.
Static close-up, eye level.
Soft library light, dust in the air, preserved.
Cinematic. Preserve composition and colors from the reference.
Maintain exact appearance from the reference image.
No facial drift, no clothing change.
```

**Wuxia still → first clash**

```text
From this exact frame: the swordsman completes the draw.
The blade clears the scabbard, rain jumps off the steel,
coat hem snaps once.
Camera: slow push-in into a medium close-up of the eyes,
then hold.
Keep wardrobe, face, bamboo, and night rain exactly as shown.
No extra attackers, no style change to animation.
<Steel whisper> <rain on leaves>
```

---

## 14. Editing and extension

### 14.0 Language trap — this one mis-classifies the job

Edit and extend are triggered by **verbs**, not by the fact that you uploaded a video.

- Legal: `Edit @Video 1` · `Replace the background in @Video 1` · `Extend @Video 1 by 6 seconds` · `严格编辑 @视频1` · `向后延长 @视频1`
- Illegal for those modes: `Reference @Video 1` · `参考 @视频1`

“Reference” classifies the job as ordinary R2V. The duration/ratio locks will not apply and the model will treat the clip as a mood board instead of a master.

API `content.role` values: `reference_image` · `reference_video` · `reference_audio` · `first_frame` · `last_frame`. First and last frames must share an aspect ratio or the last frame stretches.

### 14.1 Edit pattern

```text
[Edit Goal]
Edit @Video 1. Within <entire clip / 4–9s>,
<add / remove / replace / modify> <object, region, or audio>.

[Source Video Role]
@Video 1 is the sole editing master. It defines characters,
scene, actions, composition, camera, occlusion, audio, and order.

[Target Material Role]
@Image 1 defines <replacement attributes only>. Do not use its background.

[Edit Scope]
Modify only <the named thing>.

[Content to Preserve]
Keep <everything else> from @Video 1, including timing and camera path.
```

Examples of legal intents:

- `Replace the two-person fight in @Video 1 with an empty-handed exchange. Keep rhythm and camera.`
- `Remove the watermark in the lower-right of @Video 1.`
- `Replace the daytime background with a rainy neon alley. Keep the walk cycle.`
- `Translate spoken dialogue into Cantonese. Adjust mouth shapes. No subtitles.`

API locks: `ratio: adaptive`, `duration: -1`. Source video under 20s is more stable.

### 14.2 Extend pattern

```text
Extend @Video 1 by 6 seconds.
Continue from the last frame: the same woman, same red coat,
same wet street.

6s addition:
She steps off the curb, the car’s tail lights already small.
Camera cranes a little higher and holds.
No new characters. No cut back to the bus stop.
<Footsteps in puddles> No new music.
```

Do not restart the story. The last frame is the new first frame. Prefer `output_format: mov` on edit/extend when the host offers it — later passes composite cleaner.

### 14.3 Blockout / 白模 (Jimeng 2.5 first-class control)

A white-model or clay previz locks camera path, blocking, and timing so the text prompt only has to lock look.

**Coarse blockout** — inherit structure, invent look:

```text
Use @Video 1 only for shot order, camera positions, framing changes,
subject paths, and timing. Do not copy the blockout materials or
character appearance.
@Image 2 through @Image 6 constrain character design, environment,
and color at each corresponding stage.
Do not render motion paths, axes, or camera frustums.
```

**Fine re-render** — keep the previz, replace the world:

```text
Fully re-render @Video 1 while preserving its action paths, camera
movement, timing, and framing exactly.
Replace the environment with [NEW LOOK]. The subject is [NEW SUBJECT].
No background music. Do not generate motion paths, axes, or camera guides.
```

Strip gizmos from the blockout *before* upload. Axes and camera frustums leak into the beauty pass.

### 14.4 Storyboard and keyframe sequence

- Storyboard grid: ≤15 panels, line art, almost no text. Good for shot count and order, not pixel alignment.
- Strict alignment: separate keyframe stills. `Use Images 1 through N in order as keyframes. 0–3s corresponds to Image 1; 3–8s to Image 2…`
- Separate keyframes align more tightly than a grid.

### 14.5 Ultra-long (Jimeng beta, roughly 30–180s)

Fewer, larger time blocks. Repeat identity / wardrobe / grade at the **top** of the prompt. Name the transition between scenes. Do not write a 30-beat shot list for a three-minute clip — the model will rush or drop events.

---

## 15. Constraints, “negatives,” and what not to write

Seedance does not have a separate Midjourney-style negative box on most surfaces. Constraints live in the same prompt. 2.5 obeys them much more reliably than 1.x / early 2.0.

### 15.1 Write local bans, not encyclopedias

Generic: `no ugly, no extra fingers, no blur, no watermark, no bad anatomy`  
Useful: the two ways *this* shot dies.

Fight clip:

```text
No identity swap between the two fighters.
No missing contact — blades and hands must meet.
No axis jump that reverses screen direction.
No change of courtyard layout mid-clip.
```

Product clip:

```text
No second copy of the bottle.
No logo warping.
No extra text on the label.
```

Talking head:

```text
No burned-in subtitles.
No background music.
No wardrobe change.
No jump cuts.
```

### 15.2 Positive constraints often beat bans

```text
Maintain exact appearance from @Image 1.
Keep the bottle proportions, color, and label consistent across all shots.
Preserve composition and colors from the reference image.
One animal species per stage.
```

### 15.3 Words that waste budget

`masterpiece` · `8K` · `ultra detailed` · `best quality` · `epic cinematic breathtaking` · `trending on artstation` · `perfect anatomy`

Also wasteful: restating duration and resolution that you already set in the UI.

### 15.4 Content that still breaks

- Tiny on-screen English / Chinese text you need to be readable — still weak; prefer Seedream for typography, then I2V
- Crowds with distinct faces
- Hands doing intricate finger work across 30s
- True contact sports physics at high speed (write the contact anyway; inspect the take)
- Real-person commercial endorsement language (legal problem, not a model problem)

Official consumer apps may refuse or distort real-person face references. Have a generic stand-in ready.

---

## 16. Copy-ready genre templates

Replace bracketed parts. Keep the structure.

### 16.1 Product commercial (2.5, 15–30s)

```text
Three-shot product story for [PRODUCT].

Shot 1, close-up: [PRODUCT] stands on [SURFACE] as [MICRO MOTION: condensation / dust / light sweep].
[LIGHT].

Shot 2, medium tracking: a person picks up the same [PRODUCT] and moves through [SPACE].
Camera follows at shoulder height.

Shot 3, hero: they stop at [LANDING], set the [PRODUCT] down, camera pushes in to the [LOGO AREA].

Keep [PRODUCT] proportions, color, and label consistent across all shots.
<Specific handling sound> <environment>
No extra text, no second copy of the product.
```

### 16.2 Talking-head / explainer

```text
A [AGE, LOOK] presenter in a [WARDROBE] speaks to camera in a [ROOM].
Static medium shot, very slow push-in, eye level.
Soft key from camera left, warm practical in the background.
Dialogue language: [LANG]. Natural conversational delivery:
{[LINE UNDER 16 WORDS]}
No BGM. Room tone only. No subtitles.
Keep face and wardrobe identical. No jump cuts.
```

### 16.3 Documentary / nature

```text
Realistic nature-documentary look. [PLACE] in [LIGHT].
[SUBJECT + DISTINCTIVE BODY DETAIL] [ONE PHYSICAL ACTION].

0–3s: [SIZE + ANGLE]. [ACTION START].
3–8s: camera [ONE MOVE]. [ACTION END STATE].

Keep the subject sharp, background naturally defocused, subtle handheld breathing.
Use only [2–3 natural sounds]. No music. No subtitles.
```

### 16.4 Anime / guofeng 2.5D

```text
Top-tier guofeng anime look (2.5D), ink-wash edges, cold moonlight against warm candle.
A 22-year-old swordsman, sharp brows, high ponytail, white robe with black trim.

Forbidden: no 3D greasiness, no clipping in the fight, no subtitles.
The ink-wash effect may only appear after the 25s sword-seat click — never earlier.

[00:00–00:04] ...
[00:05–00:10] ...
[00:11–00:18] ...
[00:19–00:24] ...
[00:25–00:30] on the click of the sword seating, the scene blooms into
black-and-white ink and disperses into a splash-ink landscape. End.

Keep identity, robe, and weapon identical in every beat.
```

### 16.5 Wuxia / kung fu — production brief (2.5)

This is the high-control pattern for hard-style 武侠, not floating 仙侠.

```text
[Generation Goal]
[DURATION]s continuous live-action wuxia fight. Hong Kong close-range
choreography logic: pressure on the centerline, parry-into-grab,
impact-into-throw, short weapon, environment used as a weapon.
Not floating xianxia. Real contact + wuxia exaggeration.

[Look]
Frost-blue moonlight, snow bounce, cold stone, one dark-orange coal glow.
ARRI Alexa texture, 35mm wide, fine grain.
Real skin, wet hair, coarse cloth, brick, snow, wood.

[Cast]
@Image 1 defines the lead's face, hair, body, and wardrobe only.
Do not use its background or pose.
Opponent is a generic adult [DESCRIPTION], never a copy of the lead.

[Weapon]
One short staff / one jian. Solid, heavy, no magic length change, no neon blade.

[Event script]
0–4s: [camera path]. [opening attack]. End state: first attack broken.
4–12s: [continuous exchange, name 2–3 techniques and their contacts].
End state: opponent off-balance.
12–20s: [environment used: pillar / table / snow / wall].
End state: opponent down or disarmed.
20–[END]s: [landing shot, sheath or breath]. Hold.

[Camera]
Treat the camera as a third fighter: low-level track, short whip pans,
brief 0.12–0.18s speed ramps on contact. Face close-ups under 0.4s.
No axis jump.

[Audio]
No score, or (spare low percussion only).
<Steel> <cloth> <body impact> <snow crunch>
No subtitles.

[Maintain Consistency]
Same lead face and wardrobe as @Image 1.
Same courtyard geometry.
No extra fighters.
No identity swap.
Blades and hands must meet.
```

Shorter 2.0-length wuxia (8–12s):

```text
A wuxia-style [HERO] in [WARDROBE] fights in a rainy bamboo forest at night.
Fast sword exchanges with visible steel trails and water spray from each clash.
Low-angle follow camera, one crane pop on the finishing cut, then a close-up hold.
Cinematic live-action, wet cloth physics, rain interaction.
Maintain exact face and clothing.
No extra attackers, no cartoon squash, no glowing fairy sword.
<Rain> <steel>
```

### 16.6 One-take interior walk

```text
One-take gimbal tracking shot.
The camera pushes through [ENTRANCE DETAIL] into [FIRST SPACE],
passes [MID DETAIL], and lands on [FINAL SUBJECT].
Subject does [ONE ACTION] as the camera arrives.
Keep architecture consistent. No cuts. No teleporting rooms.
<Footsteps> <room tone>
```

---

## 17. The control loop — how to iterate like a director, not a gambler

### 17.1 Isolate variables

Order of operations when a take is wrong:

1. Subject / identity
2. Primary action and end state
3. Camera (one move)
4. Reference binding / exclusions
5. Lighting
6. Audio
7. Style texture
8. Duration / beat density

Do not jump to style if the face is already the wrong person.

### 17.2 Diagnostic table

| Symptom | Likely cause | Fix |
|---|---|---|
| Generic pretty person | Vague subject, no reference, weak opening | Open with attributes + `@Image 1` face-only |
| Face drifts after 8s | Too many jobs per beat; no consistency tail | Shorter beats; restate face/wardrobe at the tail and mid-prompt |
| Identity swap in a two-hander | Two faces, one description | Separate profiles; “no identity swap”; different wardrobe colors |
| Camera soup | Three moves in one beat | One move. Name it. Give it a speed |
| Morphy transition | Missing “cut to” / end state | Write the join: `cut to interior. Same coat.` |
| Reference ignored | File never mentioned, or mentioned as a group | One file, one job, one exclusion; mention it twice |
| Wrong room leaked from a portrait | No exclusion | `Do not use the image background` |
| Motion ignored on I2V | Prompt re-described the still | Delete subject prose. Leave action + camera |
| Frantic or missing actions | Beat overstuffed or empty | One job per beat; count the seconds |
| Random subtitles / BGM | Undirected audio on 2.5 | `No subtitles. No BGM.` plus brackets for what you *do* want |
| Plastic skin / game CG | No medium sentence | Name a camera + grain + `真人实拍` or `real skin pores` |
| Logo melts | Orbit too close + no product constraint | `no logo distortion`; end on a hold, not a move |
| Hands / extra limbs | Fast action + tight close-up for too long | Wider shot during the exchange; close-up only on the landing |
| Edit changed the whole clip | Missing preserve block / missing edit verb | Use the §14 pattern; `duration: -1`, `ratio: adaptive` |
| Extension restarts the plot | You described a new opening | Start from the last frame’s end state |

### 17.3 Probe protocol

1. 5s locked-off version of the action only.
2. 5s with the intended camera.
3. Add references.
4. Add audio.
5. Stretch beats to full length.

A failed 30s pass that mixed all five is unreadable. A failed 5s pass is information.

### 17.4 Seed discipline

When a take is close, freeze the seed and change one sentence. If you change seed and prompt together, you learn nothing.

---

## 18. Common failure modes (pre-flight)

Before you pay for a 30s 2.5 pass, walk this list:

1. Did I pick the correct **task type** and verbs?
2. Are duration / ratio / resolution set in the **panel**, not the prose?
3. Do the first 30 words name **subject + one action**?
4. Does every uploaded file have a **role and an exclusion**?
5. Is `@Image 1` the thing I most need preserved?
6. Is there **one camera move per beat**?
7. Does every beat have an **end state**?
8. Are timestamps continuous with **no gaps**?
9. Is audio either directed in brackets or explicitly suppressed?
10. Does the tail restate identity, wardrobe, layout, and the two local bans?
11. Did I ask the clip to do more events than the seconds can hold? (Rough budget: one substantial action every 3–5 seconds.)
12. For I2V: did I delete the subject paragraph?

---

## 19. Teach an AI to generate Seedance prompts

Use the following as a system prompt, Claude Code / Cursor skill, or swarm-ops agent spec. It is written so another model can emit ready-to-paste Seedance prompts without inventing illegal parameters.

### 19.1 System prompt (copy this block)

```text
You are a Seedance Prompt Engineer for ByteDance Seedance 2.0 and Seedance 2.5.

MISSION
Turn a user's creative brief into a paste-ready Seedance prompt that a
non-expert can drop into Jimeng / Dreamina / BytePlus without editing.

HARD FACTS
- Seedance is a VIDEO model. Seedream is the still-image sibling.
- Do not put duration, aspect ratio, resolution, fps, or seed inside the
  prompt unless the user is in Ultra Long mode and explicitly needs them
  restated. Those belong in the UI / API.
- Seedance 2.0: 4–15s, Shot 1/2/3 timing, fewer refs (≈9 images / 3 videos / 3 audios).
- Seedance 2.5: 4–30s, whole-second timestamps, up to 30 images / 10 videos / 10 audios,
  native audio brackets, first-class edit + extend.
- 2.0 prompts run on 2.5. 2.5-only syntax is timestamps, @ role+exclusion, audio brackets.

OUTPUT CONTRACT
Always return:
1) Recommended model (2.0 / 2.0 Fast / 2.5) and why, in one line.
2) UI settings: duration, ratio, resolution tier, generate_audio on/off, task type.
3) Asset list the user must upload, in upload order, with the role each file will play.
4) The paste-ready prompt, inside a single fenced block.
5) A 5-second probe variant of the same prompt.
6) The two most likely failure modes and the exact sentence that prevents each.

PROMPT SHAPES YOU MAY EMIT

A. Short clip ≤12s (2.0 or 2.5), no refs:
<Subject> performs <one action> in <scene>.
Visuals: <one medium/lighting sentence>.
Camera: <shot size + one move + speed>.
Audio: <brackets or "no BGM, no subtitles">.

B. I2V / first-frame:
Do not re-describe the still.
Subject action + secondary motion + one camera move + keep lighting/composition
+ appearance lock + local bans.

C. 2.5 long / referenced / multi-shot:
[Asset mapping] role + exclusion per file
[Generation Goal] one sentence
[Event script] continuous timestamps, one job + end state per beat
[Maintain Consistency] concrete attributes
[Audio] (music) <sfx> {dialogue} 【title】 only as needed

BINDING RULES
- Map files one by one. Never write "Images 1–4 are four characters respectively."
- Every file: what to inherit AND what not to inherit.
- @Image 1 = the identity or product that must not drift.
- Do not burn labels into images; bind in text.

CAMERA RULES
- One move per beat. Pair with a speed word.
- Use film terms: static, dolly-in, pull-back, track, pan, tilt, crane,
  orbit, steadicam, handheld, rack focus, whip pan, one-take.
- Uncommon moves need the visible result, not only the name.

ACTION RULES
- Visible, physical, causal. Contact + result + end state.
- No stacked unrelated verbs in the opening sentence.
- Dialogue ≤16 words. Declare language and delivery before {line}.

STYLE RULES
- One medium sentence beats ten adjectives.
- Ban: masterpiece, 8K, ultra detailed, best quality, epic cinematic as filler.
- Photoreal lock: name a camera system + grain + real skin / 真人实拍.
- Anime lock: name the treatment (guofeng 2.5D, ink-wash) and forbid 3D grease.

CONSTRAINT RULES
- Two or three LOCAL bans that would kill THIS shot.
- Restate identity / wardrobe / layout in the tail.

IF INFORMATION IS MISSING
Ask only for the missing locks, in this order: task type, duration/ratio,
subject identity source (text vs image), primary action, camera intent,
must-not-change list. Do not stall for flavor.

LANGUAGE
Write the paste-ready prompt in the language the user will generate in.
If they write Cantonese or Traditional Chinese, emit Traditional Chinese
prompt text and keep film terms bilingual when helpful (推镜 / dolly-in).

NEVER
- Invent API fields Seedance does not have (camera_fixed on 2.5, frames, 60fps).
- Claim Seedance paints still posters.
- Produce a 400-word single paragraph for a 30s clip.
- Leave uploaded files unbound.
```

### 19.2 Few-shot the teacher model with one gold example

When you install the system prompt in an agent, pin one gold input/output pair so it copies structure rather than tone.

**User:** 8s, 9:16, I2V, my photo of a man in a yellow raincoat on a boat at dawn. I want a slow living portrait for a YouTube intro.

**Teacher output:**

```text
Model: Seedance 2.0 standard or 2.5 short — single subject, no story.
UI: 8s, 9:16, 720p draft / 1080p final on 2.0, generate_audio ON, task = first-frame I2V.
Assets: Image 1 = the photo (first frame + appearance).

Paste-ready prompt:
Use the uploaded image as the full appearance and composition reference.
The fisherman turns his head slowly toward the incoming swell and exhales.
Beard hair and raincoat hem lift once in the wind, a thin sheet of spray
crosses the lower frame.
Camera: static medium shot, no pan, no zoom.
Keep the original dawn light, grey-green water, and yellow raincoat exactly.
Photographic, natural pace.
No facial drift, no wardrobe change, no extra boats, no zoom.
<Water against hull> <distant gull> No music. No subtitles.

5s probe:
Same prompt, delete the spray sentence, duration 5s.

Likely failures:
1) Model invents a new face — already blocked by "full appearance reference" + "no facial drift".
2) Model pushes in and crops the boat — already blocked by "static medium shot, no zoom".
```

### 19.3 Skill install options

Official BytePlus / Dreamina skill:

```bash
npx --yes skills@latest add \
  "https://arkdocs-en.tos-ap-southeast-1.volces.com/skills/" \
  --skill sd25-pe --yes
```

Then invoke `/sd25-pe` plus a draft brief. There is a 2.0 counterpart (`sd2-pe`) on the same channel.

Public community skills you can study or adapt:

- https://github.com/rich5000/seedance-prompt-guide
- https://github.com/liangdabiao/make-prompt-seedance2
- https://github.com/songguoxs/seedance-prompt-skill
- https://github.com/xiaoliangliang/seedance-2.5-prompt-skill
- https://github.com/MapleShaw/seedance2.0-prompt-skill
- https://github.com/scotti1i/seedance-2.0-superprompt
- https://github.com/alchaincyf/seedance-skill (clay / 白模 pipeline)

Install pattern used by several of those repos:

```bash
npx skills add https://github.com/rich5000/seedance-prompt-guide.git
```

Then invoke with a brief: `/seedance-prompt 15s 16:9 武侠 竹林夜雨 女剑客 @图1定脸`.

If you are wiring this into a custom swarm: give the agent the system prompt in §19.1, a folder of accepted prompts that actually rendered, and a critic that only checks the pre-flight list in §18.

### 19.4 Critic agent checklist (second pass before you spend credits)

Run this as a separate agent on the draft prompt. Yes/no only.

- [ ] Task type named; edit/extend verbs present if that is the job; no “reference Video 1” on an edit
- [ ] Duration / ratio / resolution / fps / 8K / masterpiece stay **out** of the prompt
- [ ] Every `@` asset has a role **and** an exclusion
- [ ] `@Image 1` is the identity or product lock
- [ ] Timeline covers 0 → end with no gaps; 2.0 uses Shot N; 2.5 uses seconds
- [ ] One job per beat; subject motion ≠ camera motion
- [ ] Visible end state on every beat, including the last
- [ ] Audio brackets correct; spoken-word budget sane; language declared before `{ }`
- [ ] Identity / wardrobe / layout restated in the tail
- [ ] Two local bans, not a generic ugly-list
- [ ] A 5–8s probe version exists

### 19.5 How to grow a private prompt library

For every keeper, store:

```text
id:
date:
model:
task: T2V | I2V | R2V | edit | extend
duration_s:
ratio:
seed:
assets:
  - file: hero_face.png
    slot: Image 1
    role: face + hair only
    exclusion: background, pose
prompt: |
  ...
probe_prompt: |
  ...
result: keeper | reject
notes: what drifted, what sentence fixed it
```

After twenty keepers, the teacher model should retrieve from this library instead of inventing new grammar.

---

## 20. One-page checklists

### 20.1 2.0 short-clip checklist

- [ ] Subject named with visible attributes
- [ ] One primary action + one secondary motion
- [ ] One camera move + speed word
- [ ] One lighting sentence
- [ ] One style / medium sentence
- [ ] Local ban for the likely failure
- [ ] 60–100 words
- [ ] Shot 1 / Shot 2 if multi-shot
- [ ] Duration / ratio set in UI

### 20.2 2.5 long-clip checklist

- [ ] Task type and trigger verbs match the assets
- [ ] Asset map: every file has role + exclusion
- [ ] `@Image 1` is the identity/product lock
- [ ] One-sentence brief at the top
- [ ] 3–5 continuous timestamped beats
- [ ] End state on every beat
- [ ] One camera idea per beat
- [ ] Audio brackets or explicit silence
- [ ] Consistency tail lists real attributes
- [ ] Two local bans, not a generic essay
- [ ] Probe exists at 5–8s

### 20.3 I2V checklist

- [ ] Prompt does not re-describe the still
- [ ] Motion could physically continue from the photo
- [ ] “Keep existing lighting and composition”
- [ ] Appearance lock sentence
- [ ] One camera move only

---

## 21. Reference sites and documents

Study these in order. Official first, then syntax references, then community pattern libraries.

### 21.1 Official / first-party

| Resource | URL | Why |
|---|---|---|
| ByteDance Seed — 2.5 homepage | https://seed.bytedance.com/seedance2_5 | What 2.5 is supposed to be |
| ByteDance Seed — 2.5 launch post | https://seed.bytedance.com/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5 | Official capability list |
| BytePlus ModelArk 2.5 prompt guide | https://docs.byteplus.com/en/docs/ModelArk/2607689 | Official 2.5 structure, tasks, refs |
| BytePlus ModelArk 2.0 prompt guide | https://docs.byteplus.com/api/docs/ModelArk/2222480 | Official 2.0 grammar |
| BytePlus 2.0 tutorial | https://docs.byteplus.com/en/docs/ModelArk/2291680 | Worked official examples |
| BytePlus video capability tutorial | https://docs.byteplus.com/en/docs/ModelArk/2298881 | Official res / duration table |
| Volcengine 2.5 tutorial | https://www.volcengine.com/docs/82379/2607688 | CN official twin of the BytePlus guide |
| Volcengine 2.5 prompt guide | https://www.volcengine.com/docs/82379/2607689 | CN official prompt formula |
| Dreamina / Lark official writing guide | https://bytedance.larkoffice.com/docx/A88jd0B47oAd8zxWp5ycZFMfnxh | Six-part formula in first-party language |
| Seedance.tv 2.5 prompting guide | https://docs.seedance.tv/en/seedance-2-5-prompting-guide | Asset mapping, blockout, storyboard |
| Seedance.tv 2.5 editing guide | https://docs.seedance.tv/en/seedance-2-5-video-editing-guide | Edit / extend patterns |
| Seedance.tv camera movements | https://docs.seedance.tv/en/camera-movements | Per-move official wording |
| Jimeng | https://jimeng.jianying.com | CN consumer surface |
| Dreamina | https://dreamina.capcut.com | International consumer surface |
| Volcano Ark | https://www.volcengine.com/product/ark | CN API |
| BytePlus ModelArk | https://docs.byteplus.com | International API |

### 21.2 High-signal practitioner guides (English)

| Resource | URL | Why |
|---|---|---|
| Segmind — official six-part formula explained | https://blog.segmind.com/the-official-seedance-2-5-prompt-guide-bytedances-six-part-formula-explained-with-examples/ | Best single syntax reference |
| VideoGen 2.5 prompting | https://videogen.io/blog/seedance-2-5-prompting-guide | Five layers + multi-shot examples |
| VideoGen 2.0 | https://videogen.io/blog/how-to-use-seedance-2 | 2.0 five-layer version |
| getstarrd 2.5 handbook | https://www.getstarrd.app/blog/seedance-2-5-prompt-guide | Timed beats, 50-slot allocation |
| seedance-25.ai prompt guide | https://www.seedance-25.ai/blog/seedance-2-5-prompt-guide | Camera list + I2V rules |
| Magnific 2.5 review + official-shaped prompts | https://www.magnific.com/blog/seedance-2-5-review/ | Full bracketed examples |
| Rendley — task types and locks | https://rendley.com/blog/how-to-prompt-seedance-2-5 | Best task-lock table |
| Our Code World — 2.0 I2V developer guide | https://ourcodeworld.com/articles/read/3199/a-developer-s-guide-to-writing-image-to-video-prompts-for-seedance-2-0 | Six-slot I2V anatomy + templates |
| Scenic / Shoty camera wording | https://www.scenic.sh/en/blog/seedance-camera-movements-guide | Movement phrases that actually fire |
| JXP 2.0 vs 2.5 | https://www.jxp.com/seedance/blog/seedance-2-5-prompt-guide | Side-by-side model table |
| OpenArt 2.0 vs 2.5 | https://openart.ai/blog/seedance-2-0-vs-2-5/ | Timing syntax difference |
| Together AI 2.5 quickstart | https://docs.together.ai/docs/seedance2.5-quickstart | API-shaped limits |
| CineV — 2.5 vision-to-sequence | https://cinev.com/insights/empowering-seedance-2-5-from-vision-to-sequence/ | Official difference list vs 2.0 |
| Pixo — character formula + transitions | https://pixo.video/blog/seedance-2-5-prompt-guide | Wuxia transition case |

### 21.3 Chinese community (high volume, copyable patterns)

| Resource | URL | Why |
|---|---|---|
| 林悦己 — 6 structures / 8 control strategies | https://cheerselfai.com/blog/seedance-2-5-prompt-writing-guide | Best CN structural analysis of 2.5 |
| 知乎 — 59 official-manual templates (2.0) | https://zhuanlan.zhihu.com/p/2008546867957485869 | Huge 2.0 template dump |
| Redreamality 2.0 攻略 | https://redreamality.com/cn/blog/seedance-2-guide/ | Bilingual camera table |
| 发现AI — 20 methods + camera list | http://www.faxai.cn/archives/1673 | Beginner EN/CN hybrid tricks |
| Morphic CN 2.5 guide | https://morphic.com/zh/resources/how-to/seedance-2-5-guide | Official formula in Chinese |
| seedance2prompts.com/zh | https://seedance2prompts.com/zh/guides | Community pattern guides + builder |
| Volcengine wuxia note | https://www.volcengine.com/article/42477 | Short wuxia phrasing |
| API易 2.0/2.5 parameter reference | https://docs.apiyi.com/api-capabilities/seedance2/video-generation | CN API parameter truth table |

### 21.4 Prompt libraries, skills, production refs

| Resource | URL | Why |
|---|---|---|
| seedance2prompts.com 2.5 recipes | https://seedance2prompts.com/seedance-2-5 | One-take / R2V / timestamp recipes |
| rich5000 seedance-prompt-guide (skill) | https://github.com/rich5000/seedance-prompt-guide | Installable prompt skill |
| liangdabiao structured prompts | https://github.com/liangdabiao/make-prompt-seedance2 | 16+ templates, scene menu |
| songguoxs seedance-prompt-skill | https://github.com/songguoxs/seedance-prompt-skill | Chinese skill with 10 modes |
| smixs visual-skills seedance-25.md | https://raw.githubusercontent.com/smixs/visual-skills/main/video/references/seedance-25.md | Compact production reference |
| MapleShaw camera codec | https://github.com/MapleShaw/seedance2.0-prompt-skill | Deep camera vocabulary |
| AtlasCloud cinematography.md | https://github.com/AtlasCloudAI/awesome-seedance-2.5-prompts-skills | Shot-size / move caution table |
| awesome-seedance-2.5-api-prompts | https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts | API + 6-step formula + camera vocab |
| HowAIWorks name map | https://howaiworks.ai/blog/jimeng-dreamina-seedance-bytedance-ai-video | Jimeng vs Dreamina vs Seedance vs Seedream |

### 21.5 How to study so you can teach the model

Do not collect 2,000 prompts. Collect **20 keepers** and tear each one into slots:

1. What was the task type?
2. Which sentence named the subject?
3. Which sentence named the only action?
4. Which camera move fired?
5. Which exclusion prevented a leak?
6. Which beat was overstuffed?

Then feed those 20 keepers to the teacher agent in §19. That is how you “teach AI to generate related prompts” without letting it drift into Midjourney dialect.

---

## 22. Quick start — first successful clip today

If you only do one thing after reading this file:

1. Open Dreamina or Jimeng. Pick **Seedance 2.5** if you have it, else **2.0**.
2. Set **8 seconds**, **16:9**, **720p**, audio on.
3. Paste this and only swap the subject:

```text
A street dumpling vendor in a grease-spotted apron flips a dumpling
in a hot pan at a night market. Steam catches the lantern light.
Camera starts in a medium side profile and slowly pushes closer as
he glances at the lens and smiles.
Warm documentary color, realistic hands, no beauty filter.
<Sizzling oil> <distant market chatter>
He says, casually, in Cantonese: {趁热。}
No subtitles. No extra cooks. Hands must hold the pan the whole time.
```

4. Generate three seeds. Keep the one where the hands and the pan stay connected.
5. Only then add a face reference as `@Image 1` (face and hair only; do not use the background) and rerun.

That loop — short clip, one action, one camera, local ban, then bind a face — is the entire guide in miniature.

---

## 23. Version notes for this document

- Seedance 2.5 public launch: 2026-07-31 (Jimeng / Doubao first; Dreamina and APIs rolling by market).
- Prompt formulas here follow BytePlus / Dreamina official practice guides and the highest-signal 2026 practitioner writeups.
- Resolution caveat: official BytePlus ModelArk lists 2.0 up to 4K 10-bit and 2.5 up to 1080p 10-bit. Jimeng web, Together, and many third-party hosts still cap 2.5 at 720p. Ultra Long mode and credit prices also change by surface. Re-check the host you actually use before quoting a number to a client.
- Still-image generation remains **Seedream**, not Seedance. Use Seedream (or any still model) to mint keyframes, character sheets, and first frames, then hand them to Seedance.

---

*End of guide.*
