# Wan 3.0 Complete Operation Guide

**Prompt engineering for full control of Alibaba Tongyi Wanxiang (通义万相)**

Version: 2026-09-17  
Scope: Wan 3.0 video + Wan 2.7 / Wan-Image stills  
Language: English primary, Chinese templates included  
Status: Compiled from official Alibaba creator handbook, Model Studio docs, and production community testing as of mid-September 2026

---

## 0. Read this first

Wan 3.0 is **not** a dedicated text-to-image model. It is Alibaba Tongyi Lab's all-in-one **video** model (`wan3.0-video` / `wan3.0-video-prime`), public beta from 6 August 2026. The still-image line in the same family is **Wan-Image / wan2.7-image / wan2.7-image-pro**.

If the job is a still, use Wan 2.7 Image.  
If the job is motion, use Wan 3.0.  
If the job is a controlled video of a specific face, product, or frame, generate the still first, then drive Wan 3.0 from that still.

The same prompt vocabulary travels across the family. Learn one language, use it for stills and motion.

Wan 3.0 has **no separate negative-prompt box**. Exclusions go inside the main prompt. Same for wan2.7-image. There are **no open weights** for 3.0. Last Apache-2.0 open video model is Wan 2.2.

---

## 1. Product map — pick the right model

| Job | Model ID | Output | Max | Use when |
|---|---|---|---|---|
| Fast still for iteration | wan2.7-image | Still | 2048×2048 | Moodboards, prompt tests, first-frame drafts |
| Hero still / 4K / brand color / hex palette | wan2.7-image-pro | Still | 4096×4096 T2I, 2048×2048 edit | Product hero, character sheet, first frame you will lock |
| Multi-image identity set / 组图 | wan2.7-image-pro + enable_sequential | Still set | n = 1–12, max 2K | Character bible, storyboard, 9-grid, first-frame factory |
| Layout / tiny text / newspaper | qwen-image-3.0-pro | Still | 2048×2048 | Menus, storyboards, exam papers, multilingual type |
| Concept video from words | wan3.0-video | Video 2–30s | 1080P 30fps | Ads, shorts, cinematic scenes |
| Faster / cheaper video iterate | wan3.0-video-prime | Video 2–30s | 1080P 30fps | Same tasks, speed-optimized |
| Animate a locked still | wan3.0-video + first_frame | Video | 30s | Product turntable, portrait life, I2V |
| Start + end frame | wan3.0-video + first_frame + last_frame | Video | 30s | Transitions, loops, before/after |
| Identity + style + audio lock | wan3.0-video omni-reference | Video | 10 img + 5 vid + 5 aud | Character continuity, branded series |
| Deck / PDF / sheet → video | wan3.0-video + file or link | Video | 1 file ≤100MB / 50 pages | Explainer, report-to-video |
| Change one thing in existing clip | wan3.0-video edit | Video | ≤30s | Relight, wardrobe, weather, object remove |
| Continue an existing clip | wan3.0-video extend | Video | input + output ≤30s | Longer take without reshoot |
| Self-host / local / Comfy open | Wan 2.2 (Apache 2.0) | Silent video | ~5–10s | Offline only. Not 3.0. |

**Hard exclusivity (official):**  
`first_frame` / `last_frame` **cannot** be mixed with `reference_image` / `reference_video` / `reference_audio` / `file` / `link` in the same request. Pick one path before you write the prompt.

**Input caps for Wan 3.0**

| Input | Cap |
|---|---|
| Prompt | 20,000 characters |
| First frame | 1 |
| Last frame | 1 |
| Reference images | 10, ≤20MB each |
| Reference videos | 5, combined ≤15s, ≤100MB each |
| Reference audio | 5, combined ≤15s, ≤15MB each |
| Document or webpage | 1 of either, not both. Formats: doc, docx, xls, xlsx, ppt, pptx, pdf, txt, md, key, pages, numbers. Public URL only. |
| Resolution | 480P / 720P / 1080P (default 1080P). No 4K video. |
| Duration | 2–30s, or `-1` smart duration |
| Aspect | 16:9, 4:3, 1:1, 3:4, 9:16, adaptive |
| Frame rate | 30 fps, MP4 |
| Audio | On by default. `audio=false` for silent. Price does not change. |
| prompt_extend | On by default. Turn **OFF** when the prompt is already exact (labels, timecodes, @refs). |

---

## 2. Control philosophy

Wan does not want a Midjourney caption. It wants a **shot brief**.

A still prompt answers: what is in the frame, how it is lit, how it is framed, what it should feel like.  
A video prompt answers: what changes, in what order, for how long, seen by which camera, heard as which sound, and what must never change.

### 2.1 The one rule that beats everything else

**Write the event first. Write the art second.**

Bad: `cinematic coffee ad, shallow depth of field, particles, slow motion, 8k masterpiece`  
Good: `Coffee beans roll out of a burlap sack, bounce twice on the wood table, fall into a hand grinder. The crank turns. Fine powder piles in the drawer. Steam drifts across the lens and closes the shot.`

Then add camera, light, sound, constraints.

### 2.2 What official handbook prompts actually contain

Statistics from 64 official Wan 3.0 creator-handbook prompts (DingTalk archive 2026-08-11):

| Element | Share of official prompts |
|---|---|
| Style and texture (film grain, render look, medium) | 47% |
| Explicit consistency lock (“keep / lock / never change”) | 44% |
| Camera language (push, pan, track, depth, focus) | 31% |
| Sound (dialogue, VO, ambience, SFX) | 23% |
| Reference assignment (`@Image1` etc.) | 20% |
| Aspect ratio named in prompt | 19% |
| Single continuous take | 14% |
| Shot number + timecode | 12% |
| Negative / “do not” | 6% |
| Frame-accurate motion numbers | 3% |

Median official prompt: **268 Chinese characters**. Half of the official set finishes under 300 characters. Long prompts exist almost only for 20–30 second multi-shot stories. Length is not quality. Coverage without contradiction is quality.

### 2.3 Weight order

The model weights the **start** and the **end** of the prompt more than the middle.

1. Open with shot type + scene (or reference roles, if using assets).
2. Then camera move.
3. Then subject action.
4. Then light / style / materials.
5. Then sound.
6. Close with the lock and the exclusions.

What you do not name, the model invents. Every named layer is one less guess.

### 2.4 Language choice

- Chinese cultural scenes, architecture, clothing, food, wuxia, ink-wash: write the prompt in **Chinese**. Wan reads 青瓦白墙, 油纸伞, 石板路, 留白 more accurately than translated English.
- International cinematic / Hollywood / product-English campaigns: English is fine.
- Mixed: scene and identity in Chinese, camera terms in either language. Do not translate the same instruction twice in one prompt.

---

## 3. Still-image operation (Wan-Image / wan2.7-image)

Use this section when you need a still, a character sheet, a product hero, or a first frame for Wan 3.0.

### 3.1 Image prompt formula

**Basic**

```text
[main subject], [environment], [lighting], [camera / framing], [visual style]
```

**Advanced**

```text
[main subject + 3–5 identity anchors],
[environment + foreground / midground / background],
[lighting: source + direction + color + quality],
[camera: shot size + angle + lens feel],
[materials and surfaces named],
[visual style / medium / grade],
[one job the image must do],
[exclusions]
```

### 3.2 Image writing rules

1. Name **one dominant subject**. Do not give three things equal weight.
2. Name materials. Wan Image is strong on Damascus steel, walnut grain, leather weave, ceramic glaze, wet stone, fabric.
3. Layer lighting as a sequence, not a mood word.  
   `Twilight, warm interior tungsten through floor-to-ceiling glass, deep blue sky rolling to orange at the horizon.`
4. Prefer aesthetic anchors over gear lists.  
   Works: `documentary photography style`, `painterly photoreal`, `food editorial photography`, `luxury beauty campaign`.  
   Weaker: `shot on 85mm f/1.4 Sony A7R V 8k`.
5. Give the image a job. Sell a bottle. Establish a face. Become frame 1 of a video.
6. Match aspect to composition before you generate.  
   16:9 landscape / architecture / cinematic.  
   3:4 portrait.  
   1:1 food / product social.  
   9:16 vertical / first frame for Reels / Shorts.
7. For hero fidelity (skin, food surface, fabric), use **wan2.7-image-pro**. Iterate on Standard / wan2.7-image first.
8. Image prompt max is **5,000 characters** (video is 20,000). No `negative_prompt` field. No `prompt_extend`. Use `thinking_mode=true` for complex layouts and on-image text (default on; only when `enable_sequential=false` and there is no image input).
9. `enable_sequential=true` builds a 组图 storyboard series (1–12 frames, max 2K). This is the cleanest first-frame factory for later Wan 3.0 I2V.
10. `color_palette` on image-pro: 3–10 hex colors, ratios summing to 100.00%. Recommended count is 8. Use it when brand color is non-negotiable.
11. Multi-ref edit: up to 9 images + `bbox_list` `[x1,y1,x2,y2]` for placement (`把图1的闹钟放在图2的框选位置`).
12. On-image text: keep short. Long poems and paragraphs will typo. For dense typography use `qwen-image-3.0-pro` instead.
13. Reference images do **not** support a transparent PNG channel. Flatten on a solid or real background first.

### 3.3 Image examples

**Product hero**

```text
A premium glass perfume bottle with a blank cream label and a polished gold cap,
standing on wet black stone at dusk,
soft side key from camera left, warm rim light tracing the cap edge,
water beads on the glass,
close-up product framing, luxury beauty campaign,
realistic glass refraction and controlled reflections,
no readable brand text, no extra products, no label distortion
```

**Documentary portrait (good first-frame candidate)**

```text
Photoreal portrait of a tattooed motorcycle mechanic in a sunlit garage,
sleeve tattoos visible, wiping grease from hands with a rag,
warm golden afternoon light from the open roller door,
documentary photography style, medium shot, eye-level,
natural skin texture, grease on knuckles, no beauty-filter skin
```

**Chinese ink atmosphere (write in Chinese)**

```text
水墨风，留白构图。薄雾竹林，一名戴斗笠、着墨色长袍的剑客立于画面中央，
左手轻按刀柄，竹叶随风落下。绢本质感，浓淡墨韵清晰，冷色调，竖构图。
不要现代元素，不要彩色，不要字幕。
```

**Architectural still**

```text
Wide architectural shot of a midcentury modern house at twilight,
warm interior lights glowing through floor-to-ceiling glass,
deep blue sky transitioning to orange at the horizon,
cool grass in the foreground, painterly photoreal, 16:9
```

**Brand-color product (image-pro palette)**

```text
Matte black wireless speaker on white marble, soft studio key from camera left,
fabric mesh and brushed-metal controls sharp, luxury product still, 1:1.
Do not include extra objects, hands, or readable logos other than the unit itself.
```

Then set `color_palette` in the API, for example 8 swatches summing to 100%: `#0B0B0B 40%`, `#C4C4C4 15%`, `#F4F1EA 20%`, plus supporting neutrals. The prompt names the materials; the palette locks the ink.

### 3.4 Image → video handoff

When the still is destined to become a Wan 3.0 first frame:

- Generate the still at the **same aspect** as the target video.
- Keep the composition simple enough to survive motion (do not pack eight subjects).
- Save a clean identity lock sentence you will reuse word-for-word in every I2V prompt.
- Do not restyle the still in the I2V prompt. The still is already the look.

---

## 4. Video operation (Wan 3.0) by mode

### 4.1 Text-to-video (T2V)

No media. The prompt must build the whole world.

**Minimum that works**

```text
[subject] + [place] + [one movement]
```

Official starter: `A red fox walks across a snowy field at sunrise.`

**Production stack**

```text
[duration + aspect + medium]
[identity anchors]
[world: time, place, weather, spatial layers]
[action: trigger → continuous motion → visible result]
[camera: one shot size + one angle + one move + ending frame]
[look: light + palette + material + motion treatment]
[sound: dialogue / SFX / ambience / music — or explicit silence]
[lock + exclusions]
```

**T2V rules**

- One primary event per generation. Ten seconds cannot hold five locations and a chase.
- Verify character and world at 6–8 seconds before you write a 30-second multi-shot.
- If two locations appear in one prompt, name the transition and how the subject arrives.
- Tight beats beat dense adjectives. 50–120 English words, or ~200–400 Chinese characters, is the working range for a single shot. Multi-shot stories can run longer because they are a shot list, not a caption.

### 4.2 Image-to-video / first frame (I2V)

The image already owns identity, composition, and style. The prompt owns **motion amplitude** and **camera**.

**I2V formula (official Formula 3)**

```text
Prompt = motion + camera move
```

**Do not** redescribe the face, clothes, or room. Redescribing fights the pixels.

**I2V template**

```text
Keep the subject, clothing, background architecture and composition identical to the first frame.
[What moves, in order, with amplitude.]
Camera: [one move + how much]. Do not orbit / do not reset / do not cut.
Background motion: [only X moves, and only slightly].
Sound: [or "no dialogue, no music"].
Lock: face, outfit, product geometry, light direction stay unchanged.
```

**Amplitude vocabulary that actually constrains the model**

| Instead of | Write |
|---|---|
| moves a little | blinks once; two strands of hair lift; hand rises 10 cm |
| camera moves in | camera pushes forward 8 percent, then holds |
| turns | rotates 30 degrees clockwise, then stops |
| walks | takes two steps forward and stops |
| windy | left-side breeze moves only two locks of hair |
| still | fixed locked-off shot, subject holds position |

**Worked I2V**

```text
Keep the first-frame woman, clothing, cliff, and photographic style unchanged.
She looks into camera, a soft breeze moves several strands of hair,
she turns slowly toward the ocean, closes her eyes, then smiles slightly.
Camera starts as a medium close-up and slowly pulls back to reveal cliffs and waves.
Golden-hour light shifts across her face. Natural ocean ambience, distant seabirds.
No dialogue, no music, no new characters, no wardrobe change, no face drift.
```

### 4.3 First frame + last frame

Mutually exclusive with omni-reference. Describe the **path between** the two stills, not the stills themselves.

```text
From the empty table in the first frame to the finished breakfast in the last frame:
a pair of hands slides a tray in from frame right,
sets the cup down first, then the bread plate,
unfolds the napkin and leaves frame.
Table, window light and camera stay locked.
No jump cuts, no extra props, no change of camera height.
```

Name the trigger, the intermediate physics, and the final state.

### 4.4 Omni-reference (R2V)

Upload is only half the job. Wan will not guess that picture 3 is the café and picture 4 is the jacket. **Assign every asset a role in the prompt.**

**Accepted labels** (platform-dependent; use one family consistently)

- English API / Model Studio: `Image 1`, `Img 1`, `Video 1`, `Audio 1`
- Many UIs also accept `@Image1`, `@Video1`, `@Audio1`
- Chinese UIs: `图1`, `@图片1`, `视频1`, `音频1`

Numbering follows upload order **inside each type**. First reference image is Image 1 even if a video was uploaded first.

**Role-assignment block (put this at the top)**

```text
@Image1 is the woman — lock face, short black hair, silver earrings, black leather jacket, height and proportions.
@Image2 is the apartment — lock wooden furniture, large windows, warm afternoon light.
@Video1 is motion rhythm only — copy timing, do not copy the person.
@Audio1 is her speaking voice.
```

Then write the action using those labels.

```text
The woman from @Image1 sits by the window in @Image2 and orders a coffee,
speaking in the timbre of @Audio1: "The usual, please."
No subtitles. Keep her face and jacket identical to @Image1 in every frame.
```

**Reference package that survives 30 seconds**

Build a locked kit and reuse it:

1. Front identity sheet
2. Three-quarter body
3. Face close-up
4. Background plate
5. Hero prop / product sheet

Anime and illustrated styles drift more (line weight, eye shape). Give them more sheets.

### 4.5 Multi-shot / AI Director (up to ~6 shots, 30s)

Official Formula 6:

```text
Prompt = overall description + shot number + timestamp + shot content
```

**Skeleton**

```text
[One-sentence story.]
Shot 1 [0-5s]: [shot size] — [one action]. Camera: [one move].
Shot 2 [5-12s]: [shot size] — [one action]. Camera: [one move].
Shot 3 [12-20s]: [shot size] — [one action]. Camera: [one move].
Shot 4 [20-27s]: [shot size] — [the turn].
Shot 5 [27-30s]: [closing image].
Overall tone: [sound + grade].
Lock: [identity / product / layout].
Exclusions: [specific failures].
```

Timestamps are directing intent, not a frame-accurate editor. If a beat feels rushed, widen **that** range only.

For a single continuous take, write `一镜到底` / `single continuous take` / `No cut` between shots.

**Chinese multi-shot header that official prompts use**

```text
镜头1 [0秒-30秒] 近景, 平视视角, 连续快速摇镜, 一镜到底（单镜头连续无缝运镜）:
```

### 4.6 Audio-driven / dialogue

Official Formula 4:

```text
voice        = exact line + emotion + intonation + pace + timbre + accent
sound effect = material of the source + the action + the room
BGM          = the score itself + its genre + when it enters and stops
```

Fence spoken lines so they cannot be read as scene description:

- English: `{Message me when you get there}`
- Chinese: 「你到了就跟我说一声」

Always add `no subtitles` / `无字幕` unless you explicitly want burned-in captions.

If you do not want music or talk, say so. Wan invents a score by default.

```text
Audio: soft rain on stone, low ambient tone, no dialogue, no music, no subtitles.
```

Lip-sync languages confirmed in production writeups: English, Spanish, French, German, Japanese, Korean, Mandarin. Write the line in the spoken language. Name the accent if it matters (`东京标准口音`, `soft Cantonese, unhurried`).

### 4.7 Document / webpage to video

One file or one public URL. Tell the model what the document is **for**.

```text
Use the uploaded document as the source of truth.
Preserve every number exactly. Do not invent claims.
Prioritize section 2 (quarterly results) and the chart on page 4.
Ignore the appendix.
16:9, 20 seconds, clean explainer, no stock-video clichés,
on-screen figures must match the document, no subtitles unless quoting a figure.
```

### 4.8 Video edit

Change **one dimension**. Lock everything else.

Trigger words the router looks for: `edit video`, `remove`, `replace`, `change to`, `add`.

```text
Edit the video: change only the weather from clear sun to first snow.
Keep identity, gait, camera path, buildings, vehicle positions, duration and cut points identical.
Snow accumulates only on still surfaces and never covers the face.
```

Recommended API: `ratio=adaptive`, `duration=-1` so length and frame stay with the source.

### 4.9 Video extend

```text
Extend Video 1 forward from the last frame.
The courier keeps walking in the same direction at the same pace.
Camera continues the same tracking height.
No new characters, no location jump, no wardrobe change.
```

Input duration + output duration must stay inside 30 seconds.

---

## 5. Official six formulas (Alibaba creator manual)

Memorize these. Every production prompt is one of them.

### Formula 1 — Basic (first tests)

```text
Prompt = subject + scene + motion
```

```text
Hand-drawn animation, oil-paint brushwork, cool colour palette.
On a farm in the American countryside, a flying saucer approaches from the distance;
a green beam of light shoots down from beneath it and lifts one of the farm's cows away;
in a second-floor room not far off, a little boy watches it happen.
```

### Formula 2 — Advanced (once Formula 1 works)

```text
Prompt = subject + scene + motion
       + aesthetic control + stylisation + sound
```

Use beats (`Beat 1 / Beat 2 / Beat 3`) for anything over ~10 seconds.

### Formula 3 — First / last frame or I2V

```text
Prompt = motion + camera move
```

Drop appearance. Keep amplitude. Adverbs do the work: push in *fast*, tighten *slowly*, leaves falling *faster*.

### Formula 4 — Sound

```text
Prompt = voice + sound effects + BGM
```

Write each layer separately. Exclude anything you do not want.

### Formula 5 — Reference

```text
Prompt = @referenced asset + action + dialogue
```

```text
A childlike fairy-tale scene.
@Image1 is bouncing and playing on the grass;
@Image2 is playing the piano under an apple tree beside them;
an apple falls onto @Image2's head;
@Image1, referencing the timbre of @Audio1, points happily at @Image2 and says:
"You're going to become a scientist!"
```

An `@` is a pointer you drop **wherever it applies**, not a declaration you make once at the top.

### Formula 6 — Multi-shot script

```text
Prompt = overall description + shot number + timestamp + shot content
```

Add `No cut` between shots for one continuous take.

---

## 6. Eight-layer production stack

Use this as a checklist. Delete layers the mode does not need.

### Layer 1 — Output

```text
10 seconds, 9:16, photoreal handheld documentary texture.
```

Put unsupported knobs (exact fps, seed, CFG) in the UI, not in the prompt.

### Layer 2 — Identity (3–5 reusable anchors)

Person: age band, one face mark, hair, main garment, one signature accessory.  
Product: silhouette, cap / lid, label zone, material, liquid line.

```text
Young watchmaker, short curls, faint mole on the left brow,
brick-red work jacket, silver round glasses.
```

```text
短卷发、左眉有浅痣、砖红色工装夹克、银色圆框眼镜的年轻修表师。
```

Repeat the **same words** in later shots. Do not paraphrase. Paraphrase is a new person.

### Layer 3 — World

Time + place + weather + foreground / midground / background.

```text
Narrow watch shop at dawn. Foreground: scattered gears.
Midground: wooden bench. Background: a tram sliding past the window.
```

### Layer 4 — Action (cause → effect)

```text
He picks up the mainspring → it releases and kicks back →
he steadies the gear with a thumb → the second hand starts moving.
```

Describe visible physical results, not “dynamic energy”.

### Layer 5 — Camera (one primary move per shot)

```text
0–3s: locked macro.
3–7s: slow lateral slide along the bench.
7–10s: gentle rise to the watchmaker's eyes.
```

### Layer 6 — Visual

Key direction, color temperature, contrast, materials, depth of field.

```text
Cool window skylight as key, warm desk-lamp pool as fill.
Real metal scratches and fingerprints. Soft background falloff.
```

### Layer 7 — Sound (priority order)

Dialogue > key action SFX > ambience > score.

```text
Foreground: crisp gear tick. Mid: distant tram. The man murmurs "it's running."
No music, no subtitles.
```

### Layer 8 — Constraints

Only the failures this scene actually produces.

```text
Keep glasses, jacket and bench position identical.
Only one set of tools. Natural finger count.
No time jumps, no subtitles, no brand marks.
```

---

## 7. Camera dictionary

One move per shot. Name direction, subject orientation, and a spatial anchor.

### 7.1 Official Chinese film language (use these on CN platforms)

| CN | EN | Notes |
|---|---|---|
| 特写 / 近景 / 中景 / 全景 / 远景 / 定场镜头 | close-up / medium / wide / establishing | 定场镜头 = opening wide that plants geography |
| 平视 / 俯视 / 仰视 / 航拍 / 过肩 | eye-level / high / low / aerial / OTS | |
| 微距 / 超广角 / 长焦 / 鱼眼 | macro / ultra-wide / telephoto / fisheye | lens *feel*, not a real EXIF string |
| 镜头推进 / 拉远 / 左移 / 右移 / 环绕 / 跟拍 / 升降 / 手持 / 固定镜头 / 复合运镜 | push / pull / truck L/R / orbit / track / crane / handheld / locked / compound | one per shot; 复合运镜 only if you split it by timestamp |
| 日光 / 火光 / 阴天光 / 晴天光 / 柔光 / 硬光 / 侧光 / 顶光 / 逆光 / 边缘光 / 高对比 | daylight / firelight / overcast / hard sun / soft / hard / side / top / backlight / rim / high contrast | |
| 中心构图 / 左侧重 / 右侧重 | center / left-weighted / right-weighted | |
| 写实 / 赛博朋克 / 废土 / 毛毡 / 3D卡通 / 水彩 / 黏土 / 勾线插画 / 像素 / 蒸汽朋克 | photoreal / cyberpunk / wasteland / felt / 3D cartoon / watercolor / clay / line illustration / pixel / steampunk | pair with one light rule |
| 生成单镜头 / 一镜到底 | Generate single shot / single continuous take | official single-take flags |
| 无台词 / 无背景音乐 / 无字幕 | no dialogue / no BGM / no subtitles | say them or Wan invents them |

### 7.2 Shot size

| Term | Use |
|---|---|
| extreme close-up / 大特写 | eyes, logo, droplet, finger on a button |
| close-up / 近景 / 特写 | face, product hero |
| medium close-up / 中近景 | head and shoulders |
| medium / 中景 | waist-up performance |
| medium wide / 中全景 | full body plus some room |
| wide / establishing / 全景 / 定场镜头 | place first |
| extreme wide / aerial / 大远景 / 航拍 | scale, crane finish |
| POV / 主观镜头 | through the subject's eyes |
| over-the-shoulder / 过肩 | two-person dialogue |
| insert / 插入镜头 | hands, object detail |

### 7.3 Angle

eye-level / 平视 · low angle / 仰拍 · high angle / 俯拍 · bird's-eye / 鸟瞰 · Dutch / 荷兰角 (use rarely) · ground-hugging / 贴地

### 7.4 Movement — write the physical path

| Term | What it does | Reliable phrasing |
|---|---|---|
| static / locked-off / 固定机位 | nothing moves | `fixed locked-off shot at eye level` |
| push-in / dolly in / 推镜 | camera walks closer | `slow push-in from medium to close-up` |
| pull-back / dolly out / 拉镜 | camera walks away | `slow pull-back revealing the full room` |
| pan L/R / 摇镜 | rotates on a fixed axis | `pan right across the wet street` |
| tilt up/down / 俯仰 | pivots vertically | `tilt up from shoes to face` |
| track / truck / 横移跟拍 | slides parallel | `tracks beside her at waist height, matching pace` |
| orbit / arc / 环绕 | circles the subject | `slow clockwise three-quarter orbit, subject centered` |
| crane up/down / 升降 | camera body changes height | `crane up from the bottle to the skyline` |
| handheld / 手持 | breathing shake | `subtle handheld breathing, no abrupt resets` |
| steadicam / gimbal | smooth walking | `smooth gimbal follow from behind` |
| FPV / 第一人称穿越 | aggressive travel | name speed and what it flies past |
| zoom | lens change, not body move | weaker than a dolly; say `push-in` if you want parallax |

**Always add amplitude**

```text
camera pushes forward 8 percent
orbit 90 degrees clockwise, start three-quarter front, end side view
crane up two meters
hold the last frame for one second
```

**Camera reaction time (official handbook trick)**

```text
The hand moves first. The camera follows with a 0.1-second lag.
After the motion ends, autofocus takes about 0.2 seconds to lock again.
```

This makes the camera feel operated, not slid on rails.

**Spatial anchors for long takes**

Name a thing the camera can stay oriented to: platform edge, doorway, reed bed, rock, lakeshore, product pedestal, yellow safety line.

**Illegal stack (do not write this)**

`fast dolly forward, slow orbit, handheld, locked-off, dramatic zoom`

Pick one.

---

## 8. Light, material, style dictionary

### 8.1 Light — write source + direction + quality + color

| Pattern | Phrase |
|---|---|
| Window key | `cool window skylight as key, warm lamp as fill` |
| Golden hour | `low sun from frame left, long shadows, warm rim` |
| Overcast soft | `flat overcast skylight, soft shadows, cool grey fill` |
| Night neon | `wet asphalt, magenta-cyan neon spill, hard practicals` |
| Studio product | `soft side key, dark falloff, controlled specular on metal` |
| Backlight dust | `single backlight, flour / rain / smoke visible in the beam` |
| Motivated interior | `practicals only: desk lamp, fridge light, phone screen` |

Layer lights. Do not stop at `cinematic lighting`.

### 8.2 Style anchors Wan actually follows

painterly photoreal · documentary photography style · food editorial · luxury beauty campaign · 35mm film grain · muted desaturated grade · teal and orange · high-contrast rain night · ink-wash / 水墨风 · 工笔 · cel-shaded anime · 2D animation · 3D short · West Coast street video · Hollywood disaster VFX texture · phone-doc realism · 留白构图

Pair a **medium** with a **light or color rule**.  
`2D animation + cold white moonlight as a hard key` holds for 30 seconds.  
`cinematic masterpiece 8k` does not.

### 8.3 Materials worth naming

wet stone · brushed steel · fabric mesh · clay-stained linen · olive oil glass · copper pot · burlap · fogged window · rain on lens · plush / felt / yarn (stylized) · oil-paint brushwork · ink bead of sweat

---

## 9. Consistency lock system

44% of official prompts lock something. Multi-shot and reference jobs that skip this sentence lose the subject.

### 9.1 Person lock (reuse verbatim)

```text
Identity lock: woman, late 20s, oval face, short black hair, faint mole on left brow,
silver earrings, black leather jacket, same height and proportions in every shot.
Do not change face, hair, clothing or accessories between shots.
```

```text
身份锁定：32岁女性，椭圆脸，短黑卷发，左眉浅痣，砖红色夹克，银色圆框眼镜。
所有镜头保持同一张脸、同一发型、同一服装、同一身高比例。
```

### 9.2 Product lock

```text
Product lock: short square clear glass bottle, rounded shoulder, matte silver cap,
blank rectangular label zone on the front.
Every angle keeps size, cap, liquid line, label position and glass color identical.
No warped geometry, no label drift, no extra products.
```

### 9.3 Environment lock

```text
Keep room layout, furniture placement, window position and light direction identical.
```

### 9.4 Motion lock (when the default motion is wrong)

Do not write “flies quickly”. Ban the default, then give countable tests.

```text
Highest priority: the sprite must move like a dragonfly —
hover in place → instant launch → full hard stop → sharp-angle turn.
Do not portray it as a fairy drifting, cruising, or gliding smoothly.
In the first 7.8 seconds there must be at least six readable burst moves.
Each burst crosses 60–90 percent of frame width in 3–5 frames,
then full-stops for 2–4 frames.
```

This is the highest-control pattern in the official set. Use it for any motion the model keeps getting wrong.

---

## 10. Exclusions (negatives live in the prompt)

Wan 3.0 has no `negative_prompt` field. Write exclusions at the end. Official prompts use them in only 6% of cases — only against a strong default the model will otherwise take.

**Universal production tail**

```text
No subtitles, no extra characters, no subject drift, no camera reset,
no clipping, no broken limbs, no wrong slow motion, no physics-defying float,
no watermark, no brand logos, background music must not bury dialogue or ambience.
```

```text
无字幕，无多余人物，主体不漂移，摄像机不重置，
无穿模，无断肢，无错误慢动作，无违反物理的漂浮，
无水印，无品牌标志，配乐不得盖过对白和环境声。
```

**Mode-specific tails**

| Mode | Add |
|---|---|
| I2V | no restyle, no wardrobe change, no face swap |
| Product | no readable brand text unless specified, no label warp |
| Dialogue | no subtitles, listener keeps mouth closed |
| Long take | no jump cuts, no location teleport |
| Edit | do not change anything except [X] |

Do not paste a 40-item ban list. It crowds out the positive brief.

---

## 11. Iteration loop — how to actually control the model

Change **one variable per run**. If you change subject, camera, light and score together, you cannot tell what fixed the shot.

### 11.1 Recommended sequence

1. **Proof (480P or 720P, 5–8s, audio off)**  
   One subject, one action, one camera move. Confirm identity and physics.
2. **Lock the still or the identity sentence.**  
   If I2V, regenerate the first frame until the face / product is right. Do not “fix it in video”.
3. **Add world feedback**  
   Hair, cloth, rain, dust, reflections responding to the action.
4. **Add sound or silence.**
5. **Scale duration and shots.**  
   Only after the 8-second take is right.
6. **Move to 1080P / wan3.0-video (not prime) for the hero take.**
7. **Edit pass** for the one remaining defect (relight, object remove, weather) instead of regenerating the whole clip.

### 11.2 prompt_extend

Default **on**. It rewrites your prompt through an LLM.

- Leave **on** for short messy ideas (`a cat running on the grass`).
- **Must stay on** for document / webpage input. The file path depends on the rewriter to parse the source.
- Turn **off** the moment you use `@Image1`, shot numbers, timecodes, exact dialogue, or quantified motion. The rewriter will smear labels and invent shots.

Official Skill on Model Studio chat: `/wan3-pe` followed by the raw idea. Use it as a draft engine, then tighten by hand and disable extend for the billed run.

### 11.3 Seed and reproducibility

If the platform exposes a seed, lock it while you tune one clause. prompt_extend **breaks reproducibility** even with a fixed seed, because the rewritten prompt changes.

### 11.4 Failure → which layer to patch

| Symptom | Patch this layer |
|---|---|
| Wrong person / melting face | Identity lock + reference role. Stop paraphrasing anchors. |
| Product warp / logo crawl | Product lock + “no geometry change”. Use I2V from a clean still. |
| Camera flying around | Name one move. Add `fixed shot` or `no camera reset`. |
| Subject skating / moonwalking | Quantify steps. Add a floor anchor. Shorten the shot. |
| Too much motion from a still | Amplitude down: 8% push, two hair strands, one blink. |
| Unwanted cut / color jump | `single continuous take`, `No cut`. Review every 30s clip — uncommanded cuts are a known 3.0 flaw. |
| Unwanted music or talk | `no music`, `no dialogue`, or `audio=false`. |
| Two subjects fail to interact | Simplify blocking. Official testing: multi-subject interaction is a weak zone. One action between them, not a conversation plus a handoff plus a walk. |
| Surreal request gets “fixed” | Wan sides with the reference image and with physics. For impossible events, ban the realistic default explicitly (see §9.4). |
| Style drift across shots | Repeat the same medium + color rule. Do not add new style adjectives mid-list. |
| Beat feels rushed | Widen that timestamp only. |
| Text / subtitles burned in | `no subtitles` / `无字幕`. For on-product type, use Wan-Image / Qwen-Image first, then I2V. |

---

## 12. Mode decision tree

```text
Do I already have the hero frame?
  NO  → generate still on wan2.7-image (-pro if hero)
         then decide T2V vs I2V
  YES → I2V / first-last. Prompt = motion + camera only.

Do I need the same face / product across shots?
  YES → omni-reference. Assign @ roles. First/last path is closed.

Do I need to change an existing clip?
  YES → edit (one dimension) or extend (continue action).

Do I need a report / deck as the source?
  YES → file or link. Say what to preserve.

Is this a 5–10s single action?
  YES → Formula 1 or 2, single paragraph.

Is this a 20–30s story?
  YES → Formula 6 shot list + locks + sound.
```

---

## 13. Copy-ready templates

### 13.1 Single-shot T2V (8–12s)

```text
8 seconds, 16:9, photoreal, shallow depth of field.

A woman in a clay-stained linen apron stands at a thick wooden farmhouse table.
Morning light floods from a large window behind her and catches flour dust in the air.
She lifts a sheet of fresh pasta with both hands; the sheet drapes translucent
and throws a warm amber glow on her face and forearms.
Camera holds static at chest height, then slow push-in as she folds the sheet
onto a floured board and dusts it once with her right hand.
Lived-in kitchen: copper pots, half-empty olive oil, torn flour bag.
Focused, unhurried, not performing.

Sound: thud of dough on wood, whisper of flour, faint table creak, birdsong through the window.
No dialogue, no music, no subtitles.
Keep her face, apron and window direction consistent. No extra people.
```

### 13.2 I2V portrait life

```text
Keep first-frame identity, wardrobe, background and photographic style unchanged.
She blinks once. A left-side breeze lifts two strands of hair.
Her right hand rises slowly to shade the sun.
Camera pushes forward 8 percent only. Do not orbit. Do not cut.
Background: leaves move slightly, nothing else.
No dialogue, no music, no subtitles, no new characters, no face drift.
```

### 13.3 Product 10s (I2V or T2V with product lock)

```text
10 seconds, 16:9.
A white ceramic perfume bottle with a blank cream label and a polished gold cap
stands on wet black stone at dusk.
Preserve bottle shape, label position, cap proportions and warm rim light.

0-3s: Wide establishing. Fine rain in the background. Bottle still. Slow dolly forward.
3-7s: Bottle rotates clockwise about 45 degrees. Camera makes a smooth three-quarter orbit.
      Water beads catch the rim light.
7-10s: Rotation stops. Hold the final composition for one second.

Sound: soft rain on stone, low ambient tone, no dialogue, no music.
No readable brand text, no label drift, no extra products, no camera reset,
no sudden speed change, no warped bottle geometry.
```

### 13.4 Multi-shot 28s narrative

```text
A short film about waiting. Muted desaturated grade, 35mm film grain.
28 seconds, 16:9.

Shot 1 [0-7s]: Wide establishing, rain-soaked train platform at night,
empty benches, amber lights on wet concrete. No people yet. Static.

Shot 2 [7-15s]: Medium. A man in a dark coat enters from frame right,
walks to the end of the platform, stops, checks his watch, looks down the empty tracks.
Camera tracks with him at chest height.

Shot 3 [15-22s]: Close-up on his face as a distant train light appears.
Expression shifts from waiting to recognition. Rain on his shoulders. Slow push-in.

Shot 4 [22-28s]: Wide pull-back from above as the train arrives.
He steps toward the doors. One other passenger steps off.

Overall: sparse ambient score, no dialogue, rain throughout,
distant train brakes in Shot 4. No subtitles.
Keep the same man, same coat, same platform layout in every shot.
```

### 13.5 Reference character series

```text
Use Image 1 as the exact character reference.
Preserve facial structure, short black hair, silver earrings, black leather jacket,
height and body proportions across the entire sequence.

Shot 1 [0-6s]: Image 1 walks into a modern bookstore and looks around. Wide, slow dolly in.
Shot 2 [6-14s]: Track beside Image 1 through the shelves. She picks up a red hardcover.
Shot 3 [14-22s]: Close-up as Image 1 opens the book and smiles.
Shot 4 [22-30s]: Pull back to a wide as she sits by the window and reads.

Warm late-afternoon light. Realistic bookstore ambience, footsteps, page turns.
No dialogue, no music, no subtitles.
Do not change clothing, face, hairstyle or accessories between shots.
```

### 13.6 Wuxia / 国风 (Chinese)

```text
20秒，16:9，水墨淡彩，电影感长镜头，一镜到底。

镜头1 [0-8秒] 全景，薄雾竹林，青石小径。戴斗笠、着墨色长袍的剑客从雾中走来，
竹叶落在斗笠上。摄像机缓慢前推，平视。

镜头2 [8-15秒] 近景，斗笠檐下，一双沉静的眼。右手慢慢握紧刀柄，指节发白。
侧光从竹隙漏下，墨色衣褶清晰。摄像机再推近。

镜头3 [15-20秒] 中景，他抽刀半寸，刃光一闪，随即入鞘。雾气被刃风切开一道又合上。
摄像机微微环绕四分之一圈后定住。

环境声：竹叶、远处山风。无配乐，无对白，无字幕。
保持同一张脸、同一斗笠、同一长袍、同一竹林空间。禁止现代元素，禁止彩色卡通。
```

### 13.7 Hong Kong street / vertical short (9:16)

```text
9:16, 8 seconds, photoreal night, phone-doc texture.

A soaked yellow-jacket courier shoulders open a metal gate into a narrow alley.
Neon spills on wet brick. Mid shot, one slow push-in down the alley,
rain falling through the key light.
He does not look at camera.

Audio: low rain bed, shutter slam as he clears the gate, no music, no dialogue, no subtitles.
Keep the yellow jacket, gate and alley layout identical. No extra people.
```

### 13.8 Audio-synced dance (needs @Audio1)

```text
Vertical 9:16, full-body, fixed stable camera.
A young woman with long black hair, white embroidered long-sleeve top,
white pleated skirt, black belt, white platform trainers,
dances idol-style in a modern minimalist kitchen to the beat of @Audio1.

Choreograph to the rhythm, tempo and emotional swells of @Audio1:
downbeats get crisp large movements and held poses;
softer passages get body waves and hand shapes;
chorus gets denser, more explosive movement.
Continuous, fluent, fully synced to @Audio1.

Smooth motion, natural limb proportions.
No subtitles, no extra people, no camera move.
```

### 13.9 Document-to-video

```text
Use the uploaded PDF as the only source of facts.
20 seconds, 16:9, clean corporate explainer, restrained motion graphics feel,
photoreal presenters only if needed — prefer kinetic type and chart animation.

Preserve every number exactly. Do not invent claims.
Prioritize the executive summary and Figure 2.
Ignore the appendix and legal pages.

No stock office footage clichés, no upbeat corporate pop,
no subtitles except on-screen figures that match the document.
```

### 13.10 Edit one dimension

```text
Edit Video 1: replace the clear daylight with first snow.
Keep identity, walk cycle, camera path, buildings, cars, duration and cut points identical.
Snow settles only on still surfaces. Do not cover the face.
No new characters, no wardrobe change.
```

---

## 14. Teach an AI to write Wan prompts

Use the block below as a system prompt for Grok, Claude, Qwen, or any local model. Paste it once. After that, send only the creative brief.

### 14.1 System prompt — Wan Prompt Engineer

```text
You are a Wan family prompt engineer (Wan 3.0 video + Wan 2.7 / Wan-Image stills).

GOAL
Turn a loose creative brief into a single paste-ready prompt that Wan can execute
with minimum guessing. Prefer coverage without contradiction over length.

DECIDE THE MODE FIRST
- still → Wan-Image / wan2.7-image formula
- motion from words → T2V
- motion from a still → I2V / first-last (motion + camera ONLY)
- locked face/product/place across shots → omni-reference with @ roles
- change an existing clip → edit (one dimension) or extend
- deck/pdf/url → document-to-video
Never mix first/last-frame with omni-reference in one request.

STRUCTURE
Still: subject + setting + light + framing + style + exclusions
T2V single shot: output + identity + world + action + one camera move + look + sound + lock
T2V multi-shot: one-sentence story + Shot N [t0-t1] + one action + one camera + overall tone + lock
I2V: keep-first-frame sentence + ordered motion with amplitude + one camera + silence or sound + lock
Reference: role block first (@Image1 is X, @Image2 is Y) then action using those labels

HARD RULES
1. Event before art. Verbs before adjectives.
2. One primary event per generation. One primary camera move per shot.
3. Identity anchors: 3–5 items, repeated verbatim, never paraphrased.
4. Quantify motion when the default will be wrong
   (percent of push, degrees of turn, step count, frames, screen-width percent).
5. Sound is mandatory to specify. If none: "no dialogue, no music, no subtitles".
6. Exclusions are few and scene-specific. No generic 40-item ban lists.
7. Chinese cultural / wuxia / ink / food / architecture scenes: write the prompt in Chinese.
8. Do not stack conflicting camera terms.
9. Do not redescribe a first-frame image.
10. Official median is ~268 Chinese characters for a single shot. Longer only for shot lists.
11. Close the prompt with the consistency lock.
12. Output ONLY the prompt (and a 3-line mode/reason note above it). No essays.

CAMERA VOCABULARY YOU MAY USE
extreme close-up, close-up, medium, wide, establishing, POV, over-the-shoulder,
eye-level, low angle, high angle,
static locked-off, slow push-in, pull-back, pan left/right, tilt up/down,
track at [height], clockwise three-quarter orbit, crane up/down,
subtle handheld breathing, single continuous take / No cut.

AMPLITUDE VOCABULARY
blinks once; two strands of hair; hand rises 10 cm; two steps; rotates 30 degrees;
camera pushes 8 percent; hold 1 second; 3–5 frames to cross 60–90 percent of frame width.

WHEN THE USER ASKS FOR VARIATIONS
Keep identity lock and mode identical. Change only the variable they named
(time of day, camera, action, length, aspect). Produce 3 variants labeled A/B/C.
```

### 14.2 Few-shot pair to pin the style

Give the model one bad→good pair so it stops writing Midjourney soup.

```text
USER: cinematic woman in tokyo rain ultra detailed masterpiece 8k
YOU:
Mode: T2V single shot, 8s, 16:9. Reason: the brief is a moment, not a still caption.

8 seconds, 16:9, photoreal night.
A woman in a red trench coat stands under a convenience-store awning on a wet Tokyo side street.
She looks up the alley, then steps into the rain and walks away from camera.
Medium shot going to wide. Camera slow pull-back, locked height.
Neon on wet asphalt, rain through the key light, shallow depth.
Audio: rain on plastic awning, distant traffic, no dialogue, no music, no subtitles.
Keep the same coat, hair and street layout. No extra people, no camera reset.
```

### 14.3 Operator commands you can give that AI

| You say | It should do |
|---|---|
| `mode: I2V` | Drop appearance, write amplitude + camera |
| `lock this face` | Emit a 3–5 item identity block and reuse it |
| `30s story` | Formula 6 shot list with timestamps |
| `silent` | `no dialogue, no music, no subtitles` + suggest `audio=false` |
| `国风 / wuxia` | Switch to Chinese, ink or period vocabulary |
| `product lock` | Geometry / label / cap / liquid-line sentence |
| `vary camera only` | Three prompts, identical except camera line |
| `make it official-short` | Cut to ≤300 Chinese characters or ≤120 English words |
| `quantify the motion` | Replace adjectives with frames, percent, degrees, steps |

### 14.4 Self-critique checklist the AI must run before it outputs

- [ ] Mode chosen and legal (no first-last + reference mix)
- [ ] One event, one camera move per shot
- [ ] Identity anchors repeated verbatim if multi-shot
- [ ] Every uploaded asset has a role sentence
- [ ] Sound specified or explicitly refused
- [ ] Exclusions target this scene’s likely failures only
- [ ] No Midjourney quality soup (`masterpiece, 8k, trending`)
- [ ] I2V does not redescribe the still
- [ ] Timestamps cover the requested duration without leftover dead time
- [ ] Language matches the culture of the scene

---

## 15. Parameter cheat sheet

### Wan 3.0 video (Model Studio / compatible APIs)

| Param | Values | Production note |
|---|---|---|
| model | `wan3.0-video` / `wan3.0-video-prime` | prime = faster iterate |
| resolution | 480P / 720P / 1080P | iterate 720, deliver 1080 |
| ratio | 16:9 / 4:3 / 1:1 / 3:4 / 9:16 / adaptive | adaptive when media is attached |
| duration | 2–30 or `-1` | `-1` smart; edit jobs prefer `-1` |
| audio | true / false | default true; false does not change price |
| prompt_extend | true / false | OFF for exact prompts |
| seed | `-1` or `0..2147483647` | useless if prompt_extend is on |
| media.type | first_frame / last_frame / reference_image / reference_video / reference_audio / file / link | first-last XOR reference/file/link |

**API gotchas that burn credits**

- Reference labels follow **type order**, not global array index. First `reference_image` is always `Image 1` / `图1`, first `reference_video` is always `Video 1` / `视频1`, even if a video was uploaded before an image.
- PNG alpha is **not** supported on reference images. Flatten first.
- `prompt_extend` must stay **true** for `file` / `link` jobs.
- With a video input, input seconds + output seconds must stay ≤ 30.
- Task result URLs typically expire in 24 hours. Download immediately.
- Region lock: API key, endpoint and model must share a region (Beijing / Singapore / Virginia). Cross-region calls fail.
- Do not invent CFG, sampler, steps, or a negative_prompt field. They are not on this API.
- Pricing snapshot (verify on the live price page before a billed run): Standard often listed around $0.05 / $0.10 / $0.20 per output second at 480 / 720 / 1080; Prime higher; promotions common. Image-pro 4K is billed separately from video seconds.

### Wan 2.7 Image

| Param | wan2.7-image | wan2.7-image-pro |
|---|---|---|
| T2I max | 2048×2048 | 4096×4096 |
| Edit max | 2048×2048 | 2048×2048 |
| Sequential 组图 | n = 1–12, max 2K | n = 1–12, max 2K |
| Prompt max | 5,000 characters | 5,000 characters |
| Refs | multi-image edit | up to 9 + `bbox_list` |
| color_palette | — | 3–10 hex, ratios = 100.00% |
| thinking_mode | default on (no image in, sequential off) | same |
| Superpower | speed | brand color, 4K, identity sets |

No `negative_prompt` and no `prompt_extend` on the image models. Put exclusions in the main prompt (`不要出现xxx` / `do not include`). Use `thinking_mode` when the layout or on-image text is complex.

---

## 16. Access points (where to run it)

### Official / first party

| Surface | URL | Notes |
|---|---|---|
| Tongyi Wanxiang web | https://tongyi.aliyun.com/wanxiang | Image + video, Alibaba / Alipay login |
| Wanxiang alt | https://wanxiang.aliyun.com | Same family |
| Create workspace | https://create.wan.video | Official create surface |
| Qwen creation | https://c.qianwen.com | PC public beta for 3.0 |
| Wan official brand | https://wan.video | Family site — lists 3.0 video and 2.7 image together |
| Model Studio (API) | https://modelstudio.console.alibabacloud.com | `wan3.0-video`, `wan3.0-video-prime` |
| Bailian console (CN) | https://bailian.console.aliyun.com | China region API |
| Official video guide (EN) | https://www.alibabacloud.com/help/en/model-studio/wan3-video-generation-guide | Parameters, exclusivity, /wan3-pe |
| Official video guide (ZH) | https://help.aliyun.com/zh/model-studio/wan3-video-generation-guide | Same, Chinese |
| Official T2V prompt page (ZH) | https://help.aliyun.com/zh/model-studio/text-to-video-prompt | Official video formula |
| Official T2I prompt page (ZH) | https://help.aliyun.com/zh/model-studio/text-to-image-prompt | Official image formula |
| Official video API ref (EN) | https://www.alibabacloud.com/help/en/model-studio/wan3-video-generation-api-reference | Fields, seed, media types |
| Official video API ref (ZH) | https://help.aliyun.com/zh/model-studio/wan3-video-generation-api-reference | Same, Chinese |
| Official image models | https://www.alibabacloud.com/help/en/model-studio/image-model/ | wan2.7-image IDs |
| Official creator handbook | https://alidocs.dingtalk.com/i/nodes/qnYMoO1rWxrkmoj2IjExdZLBJ47Z3je9 | 64 official prompts (CN, 2026-08-11 archive) |
| /wan3-pe Skill | Model Studio chat, `/wan3-pe` | Official prompt rewriter |

### Third-party playgrounds (capability and syntax vary)

OpenArt · Pixo · Morphic · Runware (`alibaba:wan@3.0`) · Vercel AI Gateway (`alibaba/wan-v3.0-video`) · Comfy Partner Nodes (https://docs.comfy.org/tutorials/partner-nodes/wan/wan3-0) · Civitai hosted API page · fal.ai / Replicate for older Wan image variants · PixelDojo (image tiers) · 万镜一刻 · 堆友 · Qwen Cloud

Always re-check duration, ref caps and whether `@Image1` or `Image 1` is the local label before a billed 30s 1080P run.

### Open weights (not 3.0)

| Item | URL |
|---|---|
| Wan 2.2 (last Apache video) | https://github.com/Wan-Video/Wan2.2 |
| Wan-AI Hugging Face | https://huggingface.co/Wan-AI |
| Wan 2.1 prompt extender source | https://github.com/Wan-Video/Wan2.1 (wan/utils/prompt_extend.py) |

Any site selling “Wan 3.0 weights” is not the real model.

---

## 17. Reference library — learn here, steal structure not adjectives

### Official and near-official

1. Alibaba Cloud — Wan 3.0 video generation guide (EN)  
   https://www.alibabacloud.com/help/en/model-studio/wan3-video-generation-guide  
   ZH: https://help.aliyun.com/zh/model-studio/wan3-video-generation-guide
2. Alibaba Cloud — Wan 3.0 API reference (EN)  
   https://www.alibabacloud.com/help/en/model-studio/wan3-video-generation-api-reference  
   ZH: https://help.aliyun.com/zh/model-studio/wan3-video-generation-api-reference
3. Alibaba Cloud — official T2V prompt page  
   https://help.aliyun.com/zh/model-studio/text-to-video-prompt
4. Alibaba Cloud — official T2I prompt page  
   https://help.aliyun.com/zh/model-studio/text-to-image-prompt
5. Alibaba Cloud — image model list (wan2.7-image / qwen-image-3.0)  
   https://www.alibabacloud.com/help/en/model-studio/image-model/
6. Alibaba Cloud — video generate & edit model card  
   https://www.alibabacloud.com/help/en/model-studio/video-generate-edit-model/
7. Wan 3.0 official creator handbook (DingTalk, Chinese, 64 prompts)  
   https://alidocs.dingtalk.com/i/nodes/qnYMoO1rWxrkmoj2IjExdZLBJ47Z3je9
8. Awesome Wan 3.0 Prompts — every handbook prompt + result clip  
   https://github.com/AtlasCloudAI/awesome-wan-3.0-prompts  
   Stats writeup: `docs/prompting-guide.zh-CN.md`
9. Flaqai prompting guide (8-layer stack, CN)  
   https://github.com/flaqai/awesome_wan-3-0-prompts/blob/main/guides/prompting-guide.md
10. Comfy Partner Nodes — Wan 3.0  
    https://docs.comfy.org/tutorials/partner-nodes/wan/wan3-0
11. wan.video family hub (3.0 video + 2.7 image)  
    https://wan.video  
    Create: https://create.wan.video

### Practical English guides (cross-check, 2026-08/09)

12. OpenArt — syntax, @refs, sound  
    https://openart.ai/blog/wan-3-prompt-guide/
13. PromptZone — six-layer stack + product example  
    https://www.promptzone.com/wan3/how-to-write-a-wan-30-prompt-a-practical-guide-with-examples-4fok
14. Pixo — six official formulas with full copy-paste prompts  
    https://pixo.video/blog/wan-3-0-prompt-guide
15. Aristotto — five-segment order, strengths / limits  
    https://aristotto.ai/blog/wan-3-0-what-it-does-and-how-to-prompt-it
16. JXP — I2V / product / mistake list  
    https://www.jxp.com/wan/blog/wan-3-0-prompt-guide
17. Morphic SPACE framework  
    https://morphic.com/resources/how-to/wan-3-0-guide
18. Picsart WAN 3.0 user guide  
    https://picsart.com/blog/wan-3-0-user-guide/
19. WaveSpeed — production test fields  
    https://wavespeed.ai/blog/ai-guides/wan-3-0-prompt-guide/
20. wan3.io prompt guide  
    https://wan3.io/docs/prompt-guide
21. Atlas Cloud — three official cases reverse-engineered (CN)  
    https://www.atlascloud.ai/zh/blog/tips/how-to-write-wan-3-0-prompt

### Image-side

22. PixelDojo — WAN 2.7 Image prompting  
    https://pixeldojo.ai/guides/wan-2-7-image-prompting-guide
23. PixelDojo — WAN Image (fast tier)  
    https://pixeldojo.ai/guides/wan-image-prompting-guide
24. Wan-Image paper  
    https://arxiv.org/abs/2604.19858

### Camera language (family-agnostic, still useful)

25. CinePrompt camera movement keywords  
    https://cineprompt.io/guides/camera-movement-keywords
26. Runway camera terms table  
    https://runway.com/resources/ai-camera-prompts

### Chinese community / reviews

27. 发现AI Wan 3.0 review + 国风 notes (2026-09-15)  
    https://media.faxianai.com/models/wan-3-0/
28. CSDN template dump (T2V / I2V formulas)  
    https://www.csdn.net/article/2026-08-28/164144442
29. AIHub Wan 3.0 access list  
    https://www.aihub.cn/ai-model/wan-3-0/

Study method: pick 10 official handbook prompts from the AtlasCloud repo. For each, mark which of the eight layers are present. Rewrite one official prompt onto your own subject without changing structure. That transfer is the skill.

---

## 18. Worked method — from idea to locked clip

Use this as the operating procedure, not as theory.

**Step 1 — One sentence**  
`A courier in a yellow jacket walks a neon Hong Kong alley in the rain and pushes through a gate.`

**Step 2 — Pick mode**  
No still yet → T2V proof at 8s.  
Later, if you need that exact jacket and face, generate a wan2.7-image still and switch to I2V.

**Step 3 — Fill only the required slots**

```text
8s, 9:16, photoreal night.
A courier in a soaked yellow jacket shoulders open a metal gate into a narrow alley.
Neon on wet brick. Mid shot, one slow push-in, rain through the key light.
Rain bed, gate slam, no music, no dialogue, no subtitles.
Keep jacket, gate and alley identical. No extra people.
```

**Step 4 — Generate cheap**  
720P, audio off or on as needed, prompt_extend off once the prompt is exact.

**Step 5 — Patch one layer**  
Camera too busy → add `fixed height, no orbit`.  
Face melts on take 2 → make a still, switch to I2V, add identity lock.  
Music appears → `no music` or `audio=false`.

**Step 6 — Scale**  
Only now write Shot 1–4 and go 20–30s at 1080P.

**Step 7 — Archive the lock**  
Save the identity sentence, the still, and the prompt that worked. Reuse the sentence word-for-word in the next episode.

---

## 19. What “complete control” actually means on Wan

You cannot CFG-slide Wan 3.0 like an open SD checkpoint. Control is linguistic and referential:

1. **Mode choice** (T2V / I2V / first-last / reference / edit / extend / file)
2. **Role-labeled assets** (`@Image1 is the jacket`, not “use my images”)
3. **Temporal structure** (shot list + timestamps, or a single take with `No cut`)
4. **One camera path with amplitude**
5. **Quantified motion when defaults fail**
6. **Verbatim identity locks**
7. **Sound specified or refused**
8. **prompt_extend off** on production prompts
9. **One-variable iteration**
10. **Edit pass instead of full regen** for the last defect

If those ten are in place, Wan is one of the more steerable 30-second models available in September 2026 — especially on identity hold, physics, and Chinese/East-Asian scenes. It is weaker on multi-character interaction, uncommanded cuts in long takes, and requests that fight a reference image or real-world physics.

Treat the prompt as a director’s shot brief. If a human DP could not execute the sentence, neither can Wan.

---

*End of guide. Built from Alibaba Model Studio docs (updated 2026-09-16), the Wan 3.0 creator handbook (64 official prompts, archived 2026-08-11), and cross-checked community production guides from August–September 2026.*
