# AI Generator Comparison (Sept 2026)

Snapshot date: **2026-09-15**. Scores are **Artificial Analysis Elo** unless noted. Video is sorted by **image-to-video (with audio)** first; text-to-video Elo is shown beside it. Image is sorted by **text-to-image** Elo.

Elo is blind human preference, not “correctness.” Boards move every few weeks. Prices are official or common list rates; aggregators (fal, WaveSpeed, OpenRouter, BytePlus) can undercut or mark up. Region notes are **first-party** access, not VPN workarounds.

Primary sources for this snapshot: Artificial Analysis / BenchmarkList arena mirrors (updated ~2026-09-02 to 2026-09-14), vendor rate cards (MiniMax, Google Gemini, BytePlus, xAI, Lightricks), and public availability write-ups for Seedance / Veo / OpenAI Sora sunset.

---

## How to read the tables

| Column | Meaning |
|---|---|
| Score | AA Elo. Video: `I2V / T2V`. Image: T2I. |
| License | Proprietary API vs open weights (and which license family). |
| Public | Can a normal user or dev reach it today without a private beta. |
| Region | First-party geo. HK ≠ Mainland. |
| Pricing | Typical hosted rate. Local/open models: GPU cost only if self-hosted. |

**Hong Kong note:** Grok, Gemini/Veo/Nano Banana, Kling international, MiniMax, LTX, Runway, Luma, Suno generally work first-party from HK. OpenAI consumer (ChatGPT Images / Sora) is often blocked first-party in HK and Mainland; Azure Singapore or a gateway is the usual path. Seedance / Seedream / Jimeng / Doubao are CN-first; HK IP is a common official path; BytePlus + resellers are the global API path.

---

## 1. Video models (sorted by I2V Elo)

| Rank | I2V / T2V | Model | Lab | License | Public | Region | Pricing (typical) | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | **1206** / 1235 | MiniMax H3 Max (fal post-train) | MiniMax + fal | Closed API (fine-tune of open H3) | Yes (fal, MiniMax) | Global API. CN lab. | **$0.05/s** 480p, **$0.08/s** 768p. Turbo ~half on fal. | Often #1 I2V-with-audio. 4–15s. Native stereo audio. |
| 2 | **1190** / 1221 | Seedance 2.0 | ByteDance | Proprietary | Official Jimeng / Dreamina / Doubao. Global via BytePlus + resellers. | Official flagship often CN/HK-facing. Global API lagged after studio pressure. | Token-billed. ~**$0.10–0.23/s** by resolution. 720p commonly ~$0.15–0.30/s. | Strong I2V + multi-ref. Dual-channel audio on many SKUs. Up to ~15s. |
| 3 | **1186** / 1227 | MiniMax H3 (base) | MiniMax | **Open weights** + API | Yes. Weights on HF; API MiniMax / fal. | Global API. Open-weight dumps may be geo-restricted. HK-listed company; first-party works from HK. | **$0.08/s** 768p, **$0.13/s** 2K. Audio refs free. Extra images after 5: $0.04. | 4–15s. Up to ~9 image / 3 video / 3 audio refs. First/last frame. |
| 4 | **1180** / **1238** | Gemini Omni Flash / 1.1 | Google | Proprietary | Yes (Gemini, Flow, API) | **HK yes. Mainland no** first-party. Vertex often SG for enterprise. | ~**$0.10/s** Flash. Some edit jobs flat ~$2.40–3.60/clip. | Wins a lot of **T2V**. Any-to-any: text/image/audio/video in → edited video out. |
| 5 | **1174** / **1242** | Wan 3.0 | Alibaba | 3.0 API closed. Older Wan 2.x often **Apache-2.0**. | Yes (Bailian, fal, self-host 2.x) | Strong in CN + global cloud. Open 2.x runs anywhere. | ~**$0.10/s**. 2.6/2.7 often cheaper on WaveSpeed. | **#1 T2V** and **#1 video-edit** on AA as of 14 Sep 2026 (~1196 edit Elo). |
| 6 | ~1105 / 1145 | HappyHorse 1.1 | Alibaba ATH | Proprietary | Yes (Alibaba Cloud + some aggregators) | One of the CN models with a real international API. | ~**¥0.9–1.6/s** (~$0.13–0.22) 720p/1080p. | High silent/visual Elo. 1.1 adds audio + ~7-lang lip-sync. Up to ~15s. |
| 7 | **1109** / ~1062–1113 | Grok Imagine Video 1.5 | xAI | Proprietary | Yes (Grok, X, xAI API) | **Works in HK.** Not Mainland-first. | ~**$0.07–0.14/s** 720p; 1.5 often **$0.08/s**. SuperGrok quotas apply. | Fast short clips, native audio, 6–15s. Strong consistency for faceless / social. |
| 8 | **1086** / 1092 | Veo 3.1 (Quality / Fast / Lite) | Google DeepMind | Proprietary | Yes (Gemini, Flow, Vertex, Google Vids) | **HK yes. Mainland no.** | Quality **$0.40/s** 1080p; Fast **$0.10–0.15/s**; Lite **$0.05–0.08/s**; 4K Quality **$0.60/s**. Audio included. | Mid Elo, high “looks like a camera” hit rate. ~8s native; extendable. Up to 4K. |
| 9 | **1071** / 1108 | Kling 3.0 Pro | Kuaishou | Proprietary | Yes (klingai.com, CN app, APIs) | CN + international site. Feature set can differ by account region. | ~**$0.08–0.17/s**. Turbo ~¥0.8/s (~$0.11) at 720p. | Motion, multi-shot, 4K/60 on some SKUs, motion-path control. 3–15s. |
| 10 | ~1068 / 1074 | PixVerse V6 | PixVerse | Proprietary | Yes, global | Global | From ~**$0.03–0.07/s** at 720p. | Cheap social / effects. |
| 11 | ~1059–1060 / same | LTX 2.5 Fast / Pro | Lightricks | **Open weights** (OpenRAIL-class) | Yes: Hugging Face, ComfyUI, LTX API | **No geo lock** if self-hosted. Hosted API global. | Hosted ~**$0.06–0.32/s** (Fast cheaper). Local = GPU only. | Best open 4K + synced audio path. ~10s. Fast ComfyUI iteration. |
| 12 | unranked-new / mid | Seedance 2.5 | ByteDance | Proprietary | Rolling: Jimeng Pro / Doubao + BytePlus | Same CN-first pattern as 2.0; aggregators lag the CN apps. | ~**$0.10/s** 480p, **$0.23/s** 720p, **~$0.41–0.57/s** 1080p. | Claimed ~30s single pass, many refs (up to ~50 on some SKUs), native audio. |
| 13 | mid / mid | Runway Gen-4.5 | Runway | Proprietary | Yes | Global (US). Works in HK. | Subscription + credits. API often ~**$0.05–0.12/s**. | Control suite (motion brush, camera, Act-style). Not an Elo king. |
| 14 | mid | Luma Ray 3.x | Luma | Proprietary | Yes | Global | ~**$0.15–0.22/s**. | Fast I2V drafts. HDR on some SKUs. |
| 15 | mid | Vidu Q3 | Shengshu | Proprietary | Yes | CN + intl site | ~**$0.04–0.10/s**. | Budget 1080p. |
| 16 | mid | Hailuo 2.3 (older MiniMax) | MiniMax | Proprietary | Yes | Global | ~**$0.03–0.05/s**. | Physics / body motion. Many SKUs lack native dialogue. |
| 17 | — | Sora 2 / Pro | OpenAI | Proprietary | **Dying** | Consumer app shut 26 Apr 2026. **API sunset 24 Sep 2026.** First-party often blocked in HK/CN. | Was $0.10–0.50/s. | Do not start new pipelines. Closest replacements: Veo 3.1 (photoreal+audio), Seedance (long multi-ref), Kling (motion). |
| — | edit **#1** | Wan 3.0 (edit) | Alibaba | See row 5 | Yes | — | See row 5 | Best **video-edit** Elo (~1196 AA / ~1414 Arena video-edit). |

### Video pick by job

| Job | First pick | Fallback |
|---|---|---|
| Image-to-video quality / value | MiniMax H3 / H3 Max | Seedance 2.0 |
| Long multi-ref story (15–30s) | Seedance 2.5 (if reachable) | Seedance 2.0, Kling 3.0 |
| Photoreal + native audio, easy from HK | Veo 3.1 Fast | Grok Imagine Video 1.5 |
| Text-to-video arena | Wan 3.0 or Gemini Omni Flash | H3 Max |
| Open 4K + audio on your GPU | LTX 2.5 | Wan 2.x, Hunyuan Video 1.5 |
| Motion / 4K / multi-shot value | Kling 3.0 | H3 |
| Director control (brush, camera, edit suite) | Runway Gen-4.5 | Gemini Omni (conversational edit) |
| Cheap social clips | PixVerse V6, Hailuo 2.3, LTX Fast | Grok Imagine Video |

---

## 2. Image models (sorted by T2I Elo)

| Rank | T2I Elo | Model | Lab | License | Public | Region | Pricing | Notes |
|---|---|---|---|---|---|---|---|
| 1 | **1187–1188** | GPT Image 2.5 Flare | OpenAI | Proprietary | ChatGPT + API (shipped 8 Sep 2026) | First-party often **blocked in HK & Mainland**. Azure SG / gateway. | ~**$0.21/img** max (~$211 / 1k). | Fast default of Images 2.5. Also strong at edit. |
| 2 | **1180–1182** | GPT Image 2.5 Sunburst | OpenAI | Proprietary | Same | Same | Same price; slower. | **#1 image-edit** (~1165–1167). Precision edits. |
| 3 | **1171–1172** | GPT Image 2 (high) | OpenAI | Proprietary | Same | Same | ~$0.21/img. | Previous T2I leader (Apr–Sep 2026). |
| 4 | **1144–1147** | MAI-Image-2.6 | Microsoft | Proprietary | Playground / Azure Foundry | Azure works; HK via SG region. | ~**$0.04/img** ($39 / 1k). | Best value near the top. |
| 5 | **1127** | Reve 2.1 | Reve | Proprietary | Yes | Global | ~$0.20/img. | Native 4K layouts / UI. |
| 6 | **1122** | Nano Banana 2 (Gemini 3.1 Flash Image) | Google | Proprietary | Gemini app + API | **HK yes. Mainland no.** | ~**$0.067/img**. Free-ish in Gemini app. | Best high-volume stills from HK. Multi-subject consistency. |
| 7 | **1108–1110** | Muse Image | Meta | Proprietary | Meta AI | Global consumer | ~**$0.01/img** API; free in app. | Cheap / free consumer. |
| 8 | **1098** | Nano Banana Pro (Gemini 3 Pro Image) | Google | Proprietary | Gemini paid | HK yes | ~$0.13/img. | Hero stills, identity lock, 4K. |
| 9 | **1085** | Qwen-Image-3.0-Pro | Alibaba | API closed; older Qwen Image often open | Yes | CN + global | ~$0.03–0.04/img. | Text-in-image. |
| 10 | **1081** | Seedream 5.0 Pro | ByteDance | Proprietary | Jimeng / APIs | CN-first, same pattern as Seedance | ~$0.09/img. | |
| 11 | **1041** | Grok Imagine Image Quality | xAI | Proprietary | Grok / X | **HK yes** | ~**$0.05/img** quality ($50 / 1k). | Fast everyday gen in this chat / X. |
| 12 | ~1025 | FLUX.2 [max] | Black Forest Labs | API closed; **[dev] open** | Yes | Global | Max ~$0.07; **dev** hosted ~$0.005–0.012 or local. | Photoreal commercial. |
| — | ~1017 open | Ideogram 4.0 (open weights) | Ideogram | **Open weights** + API | Yes | Global | API higher; local = GPU. | Best **open** T2I on AA. Text-heavy graphics. |
| — | 1000 open | FLUX.2 [dev] | BFL | **Open weights** | HF / Comfy | Anywhere | GPU or cheap hosted. | Photoreal open default. |
| — | not on AA T2I | Midjourney v8 | Midjourney | Proprietary | Discord / web | Global (card billing) | Sub ~$10–120/mo. | Aesthetic leader for many artists. Not on AA board. |

Image-edit board (same week): **Sunburst > Flare > MAI-2.6**.

---

## 3. Music / speech (separate score)

| Rank | Model | Lab | License | Public / region | Pricing | Notes |
|---|---|---|---|---|---|---|
| 1 | Suno v6 / v6-wild / v6-mini | Suno | Proprietary, label-backed (Warner, BMG, Believe) | Global web/app. Works from HK. | Subscription. v6-mini is the free tier. | v6 launched **2026-09-09** and replaces v5.x. AA music arenas still listed **Suno V5.5** as leader just before the swap. Section edit, mashups, multimodal in. |
| 2 | Udio | Udio | Proprietary | Global | Sub | More walled on export after label deals. |
| 3 | Stable Audio 3 | Stability AI | Mixed open + API | Anywhere if self-hosting Small/Medium | API Large; local otherwise | Longer instrumentals. Licensed-data pitch. |
| — | ElevenLabs Music v2 + TTS | ElevenLabs | Proprietary | Works in HK | Per-char / per-min | Speech + music. |
| — | MiniMax Music / speech | MiniMax | Proprietary | CN + global | API | Useful if already on H3. |
| — | Lyria | Google | Proprietary | Gemini / API; HK yes | API | App-embedded music. |
| — | Local Cantonese TTS | GPT-SoVITS-class, CosyVoice, etc. | Open / mixed | Anywhere | GPU | Separate from song models. |

---

## 4. Open weights worth self-hosting

| Modality | Model | License family | Why |
|---|---|---|---|
| Video | LTX 2.5 | OpenRAIL-class | 4K + synced audio, ComfyUI, lowest VRAM among frontier-adjacent. |
| Video | Wan 2.x | Apache-2.0 (check exact tag) | Open realism / faces. 2.7 still widely used locally. |
| Video | MiniMax H3 | Open weights (confirm current license + export) | Frontier I2V with stereo audio. Heavier than LTX. |
| Video | Hunyuan Video 1.5 | Custom OSS | Natural motion. High VRAM. |
| Image | FLUX.2 [dev] | Open weights | Photoreal default. |
| Image | Ideogram 4.0 OW | Open weights | Text-in-image. |
| Image | Qwen Image / HunyuanImage / HiDream / Cosmos3 | Mixed OSS | Open T2I pack below the closed GPT/Gemini/MAI tier. |
| Music | Stable Audio 3 Small/Medium | Open weights | Local instrumentals. |

Local video usually wants **12–24GB+ VRAM** (LTX on the low end, Hunyuan/H3 on the high end). Hosted vs local break-even is often hundreds to a couple thousand clips.

---

## 5. HK access cheat sheet

| Works first-party from HK | Awkward first-party | CN-native, usable from HK | Truly local / no region |
|---|---|---|---|
| Grok Imagine (image + video) | ChatGPT Images / Sora (OpenAI consumer often blocked) | Seedance / Seedream / Jimeng / Doubao if product detects HK | LTX 2.5 |
| Gemini / Veo / Omni / Nano Banana | Anthropic (not a gen-media lab; separately blocked in HK) | BytePlus for Seedance API | Wan 2.x open |
| Kling international | Some Google SKUs in Mainland only | MiniMax CN console + intl API | FLUX.2 dev, Ideogram 4 OW |
| MiniMax H3 API, LTX API, Wan via Alibaba/fal | — | HappyHorse on Aliyun | Hunyuan, MiniMax H3 weights (license permitting) |
| Suno, Runway, Luma | — | Vidu, some Kling CN-only features | — |

---

## 6. Keep-five stack

1. **I2V quality/value:** MiniMax H3 / H3 Max
2. **Long multi-ref story:** Seedance 2.5 (BytePlus or Jimeng) else Seedance 2.0
3. **Photoreal + audio, HK-easy:** Veo 3.1 Fast
4. **Open 4K + audio on your box:** LTX 2.5
5. **Stills in-chat / X:** Grok Imagine; **stills for text/layout:** GPT Image 2.5 (if gateway) or Nano Banana 2

---

## 7. Caveats

- I2V Elo ≠ T2V Elo ≠ photoreal stills ≠ “usable in a finished YouTube cut.”
- Seedance official global availability has been politically and commercially messy in 2026; always check Jimeng vs BytePlus vs reseller this week.
- Sora 2 API sunset: **2026-09-24**.
- Suno v6 just replaced v5.x; music Elo will lag the product swap.
- Prices are per output second unless noted as token billing (Seedance) or per image.
- This file is a snapshot, not a live feed.

---

*Generated 2026-09-15 for local reference. Re-check Artificial Analysis and vendor rate cards before budgeting a production run.*
