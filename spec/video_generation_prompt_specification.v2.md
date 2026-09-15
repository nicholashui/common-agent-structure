# Video Generation Prompt Specification v2

**Document ID:** `video_generation_prompt_specification.v2`  
**Version:** 2.0.1  
**Status:** Specification handbook. CASOPS Video Swarm integration is **planned** (`issues/issue0009.md`); not an eval PASS.  
**Date:** 2026-09-14  
**Supersedes:** `video_generation_prompt_specification.v1`  
**Scope:** Portable creative intent, model-specific prompt compilation, visual and audio direction, reference binding, runtime validation, continuity, software provenance, editorial assembly, and production planning—from a two-second insert to a feature-length package.

> **Core principle:** Store creative meaning independently of the model. Compile it into a verified target profile. Keep prompts, runtime controls, reference assets, and editorial instructions separate.
>
> Portability preserves intent. It does not guarantee identical output or equivalent capabilities across models.

---

## 0. What changes in v2

### 0.1 Major improvements

1. **Separates documented capabilities from production heuristics.**
2. **Replaces broad vendor-version claims with versioned capability profiles.**
3. **Distinguishes generated duration from edited duration.**
4. **Separates native audio instructions from post-production audio requirements.**
5. **Treats references as actual assets—not magic text handles.**
6. **Adds explicit validation, conflict handling, and compilation-loss reporting.**
7. **Preserves canonical requirements instead of silently dropping unsupported fields.**
8. **Distinguishes single-shot clips, multi-shot generations, sequences, and complete projects.**
9. **Adds typed timing, asset provenance, acceptance criteria, and reproducibility records.**
10. **Corrects inconsistent examples, runtime arithmetic, looping assumptions, and assembly code.**

### 0.2 Corrections to v1

| v1 issue | v2 correction |
|---|---|
| Google Cloud article dated October 16, 2025 | The supplied article is dated **October 15, 2025**. |
| Model architecture used to infer preferred prompt grammar | Adapter behavior must follow documentation and tests, not architectural speculation. |
| Product families treated as interchangeable endpoints | Identify provider, surface, exact model, mode, and profile revision. |
| Universal “always-on audio” claims | Record audio capabilities and controls per endpoint. |
| Vendor punctuation presented as universally meaningful syntax | Separate ordinary prose conventions from actual parser/API syntax. |
| Seeds presented as a continuity mechanism | Treat seeds as execution controls, not identity guarantees. |
| “I2V deletes appearance” | Omit redundant description where appropriate; retain necessary disambiguation and approved changes. |
| Unsupported fields silently dropped | Preserve requirements and report unsupported or approximated mappings. |
| Four audio buses implied separately delivered tracks | Audio categories are a planning abstraction unless separate stems are documented. |
| Two-second sample implied universally available generation | Generate a supported duration and trim when necessary. |
| Eight plates described as approximately three minutes | The listed plates total **54 seconds**. |
| Irreversible action described as a seamless loop | Require compatible start/end state and motion, or solve the loop editorially. |
| `Sequence` used as the sequential child of `Series` | Use `Series.Sequence` for the demonstrated sequential assembly pattern. |

The article-date correction follows the supplied Google Cloud text; the sequential component correction follows Remotion’s documentation. ([cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1))

### 0.3 Evidence labels

This document uses four evidence classes:

| Label | Meaning |
|---|---|
| **Documented** | Supported by an identified primary source for a specified product or implementation. |
| **House rule** | A production convention adopted by this specification. |
| **Heuristic** | A starting assumption to test, not a capability guarantee. |
| **Unverified** | Must not be used to authorize an executable request. |

**MUST**, **SHOULD**, and **MAY** express requirements of this specification—not guarantees made by a generation model.

---

## 1. Architecture: five separate layers

A production request consists of five layers.

```text
CREATIVE INTENT
    What should appear, happen, sound, and remain consistent.

ASSET BINDINGS
    Which actual images, videos, audio files, and bibles provide guidance.

TARGET PROFILE
    What this exact endpoint and mode accept.

GENERATION REQUEST
    Compiled prompt + supported runtime fields + uploaded asset bindings.

DELIVERY PLAN
    Trimming, assembly, captions, graphics, audio replacement, finishing.
```

### 1.1 Why this separation matters

“Eight seconds,” “slow push-in,” and “character reference” are not the same type of instruction:

- **Eight seconds** may be an API parameter.
- **Slow push-in** is usually creative direction.
- **Character reference** requires an actual asset and a supported conditioning mechanism.
- **A two-second final insert** may be an editorial trim of a longer generation.
- **Exact dialogue at a particular frame** may require post-production rather than prompt text alone.

OpenAI’s Sora prompting guide explicitly distinguishes prompt content from runtime parameters such as size and duration; its archived status also illustrates why a prompt guide must not be mistaken for a live availability guarantee. ([cookbook.openai.com](https://cookbook.openai.com/examples/sora/sora2_prompting_guide))

### 1.2 Production units

| Unit | Definition |
|---|---|
| **Beat** | A bounded action or change within a shot. |
| **Shot** | A continuous camera view without an editorial cut. |
| **Clip** | One generated output; may contain one shot or several requested shots. |
| **Take** | One candidate generation for the same clip specification. |
| **Sequence** | An edited arrangement of clips, graphics, and sound. |
| **Scene** | A dramatic unit; may span several shots and generation calls. |
| **Project** | A complete production with shared bibles, timelines, and delivery requirements. |

**House rule:** One generation should have one clear dramatic or visual purpose. Multi-shot capability is not permission to overload it.

---

## 2. Capability profiles and software provenance

### 2.1 Do not maintain a universal limits table

Limits belong to a versioned adapter profile, not the portable creative schema.

A profile MUST distinguish:

- Provider.
- Product surface: API, consumer UI, hosted service, or local workflow.
- Exact model identifier.
- Model variant.
- Generation mode.
- Region or deployment, where relevant.
- SDK or workflow version.
- Documentation source and retrieval date.
- Documentation evidence versus an actual execution test.

“Veo,” “Runway,” or “Wan” alone is insufficient for executable compilation.

### 2.2 Capability profile structure

```yaml
profile_id: google.veo31.reference_video.example
profile_revision: 1

identity:
  provider: google
  surface: configured_google_video_endpoint
  model_id: veo-3.1-generate-001
  mode: reference_to_video

evidence:
  documentation_status: verified
  documentation_checked_at: "2026-09-14"
  source_ids:
    - SRC.GOOGLE.VEO31.MODEL_REFERENCE
  execution_status: not_tested
  execution_tested_at: null

capabilities:
  text_prompt: true
  image_references: true
  audio_generation: true
  separate_audio_stems: unknown
  timestamp_prose: best_effort
  exact_frame_timing: unknown

validation:
  duration_rule: reference_video_requires_8_seconds
  asset_roles: endpoint_specific
  combined_feature_constraints: endpoint_specific
  runtime_field_mapping: adapter_owned

availability:
  account_access: unknown
  quota: unknown
  region_access: unknown
```

This is a **profile format example**, not a complete runnable integration.

The consulted Google model reference lists 4-, 6-, and 8-second outputs, with reference-image generation restricted to 8 seconds. It also distinguishes capabilities and output resolutions between standard and Fast variants. Those distinctions belong in profiles rather than a single “Veo 3.1” row. ([docs.cloud.google.com](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate))

### 2.3 Capability dependencies

A profile MUST validate combinations, not only individual fields.

Examples of dependencies to represent:

```text
reference images × duration
resolution × duration
mode × aspect ratio
first/last frames × reference images
extension × source-video requirements
audio generation × model variant
seed × reproducibility expectations
frame count × temporal compression constraints
```

A feature being available somewhere in a product does not establish that it can be combined with every other feature.

### 2.4 Source-backed adapter examples

| Adapter family | What this specification adopts | Boundary |
|---|---|---|
| **Veo 3.1** | Five-part scene structure; explicit sound direction; reference and endpoint-frame workflows; timestamped narrative prompts | Runtime support must be validated separately. |
| **Runway Gen-4 I2V** | Start with simple motion; use the image for visual grounding; prefer positive phrasing | Do not generalize this exact contract to every Runway model. |
| **Sora 2 guide pattern** | Scene prose plus structured camera, action, and dialogue direction | The consulted guide is archived; availability requires separate verification. |
| **Diffusers SVD pipeline** | Image conditioning and motion-related numeric controls | The standard pipeline interface is not an ordinary text-prompt interface. |
| **Remotion assembly** | Frame-based sequencing of approved media | Assembly is separate from generative inference. |

These examples are grounded in the respective primary documentation. ([cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1))

### 2.5 Additional adapter candidates

The following names from v1 remain in the **integration backlog**, not a verified capability matrix:

- Kling.
- Seedance.
- Wan.
- HunyuanVideo.
- CogVideoX.
- LTX.
- Mochi.
- AnimateDiff.
- Luma.
- Pika.
- Hailuo.
- Firefly.
- Midjourney Video.
- Grok Imagine.
- PixVerse.
- Vidu.
- Higgsfield.
- Avatar and performance-transfer systems.

Before enabling an adapter, record its exact endpoint or implementation and validate its controls. Do not carry forward v1’s numeric limits, version chronology, punctuation rules, or retirement dates without supporting evidence.

### 2.6 Local workflow provenance

For local or graph-based inference, archive:

```yaml
software_provenance:
  repository_commit: null
  package_lockfile: null
  model_checkpoint_hash: null
  text_encoder_hash: null
  vae_hash: null
  adapter_and_lora_hashes: []
  workflow_graph_hash: null
  custom_node_versions: {}
  scheduler_configuration: {}
  precision: null
  hardware_summary: null
```

**House rule:** A workflow screenshot is not a reproducibility record.

---

## 3. Universal creative anatomy

```text
INTENT       Why this clip exists.
SUBJECT      Who or what matters.
ACTION       What changes, in chronological order.
CONTEXT      Where, when, and under what environmental conditions.
CAMERA       Framing, position, movement, and focus.
LOOK         Lighting, medium, texture, color, and mood.
AUDIO        Speech, effects, ambience, music, or intended silence.
CONTINUITY   What must match and what may change.
ACCEPTANCE   What an approved take must visibly or audibly demonstrate.
```

Google Cloud’s five-part Veo formula emphasizes cinematography, subject, action, context, and style/ambiance. DeepMind’s guide complements it with character specificity, sensory world-building, explicit audio, and detailed action planning. ([cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1))

### 3.1 Ordering is an adapter concern

Store named fields. Reorder when compiling.

A model-facing prompt is not required to reproduce the canonical object’s storage order.

### 3.2 Separate four timelines

1. **Subject timeline:** movement, gesture, expression, cloth, props.
2. **Camera timeline:** movement, framing, focus.
3. **Audio timeline:** speech, effects, ambience, music.
4. **Editorial timeline:** cuts, trims, transitions, titles.

A camera orbit is not an editorial cut. A sound cue may begin before a cut or continue across it.

### 3.3 Prompt economy

**House rule:** Use the shortest prompt that preserves the required distinctions.

Add detail in this order:

1. Essential subject and action.
2. Starting composition.
3. Necessary environment.
4. Camera behavior.
5. Required sound.
6. Continuity anchors.
7. Stylistic refinements.

Long prompts are appropriate when details resolve ambiguity. Length by itself is not a quality criterion.

DeepMind explicitly demonstrates both short prompts and elaborate action descriptions; Runway’s Gen-4 guidance recommends beginning simply and adding elements incrementally. ([deepmind.google](https://deepmind.google/models/veo/prompt-guide/))

### 3.4 Visible action before abstract intent

Keep emotional intent in the canonical object, but express it through observable behavior.

| Abstract intent | Model-facing behavior |
|---|---|
| She becomes determined | Her gaze steadies; she stops fidgeting and places the envelope flat. |
| He distrusts the visitor | He keeps his hand on the door and answers without stepping aside. |
| The place feels abandoned | Empty chairs, an unlit counter, dust disturbed only by a moving curtain. |

Do not invent additional plot to make an abstract emotion visible.

---

## 4. Field catalog

### 4.1 Runtime and delivery

| Field | Meaning | Validation rule |
|---|---|---|
| `generation.duration_s` | Requested generated duration | Must be supported by the target profile. |
| `generation.frame_rate_fps` | Requested or resolved output frame rate | Do not imply it is configurable if fixed. |
| `generation.num_frames` | Requested frame count for supported implementations | Validate against the exact workflow. |
| `generation.aspect_ratio` | Generation aspect ratio | Must match supported mode combinations. |
| `generation.resolution` | Generation output resolution | Do not confuse with final export or upscaling. |
| `generation.seed` | Optional execution seed | No cross-model identity guarantee. |
| `generation.vendor_parameters` | Namespaced adapter-specific controls | Validate types and allowed values. |
| `delivery.in_s`, `delivery.out_s` | Selected source interval | Must lie within the approved take. |
| `delivery.timeline_duration_s` | Duration used in the edit | Must match trim and any approved retiming. |
| `delivery.aspect_ratio` | Final composition | Any crop, padding, or reframe must be explicit. |
| `delivery.frame_rate_fps` | Final timeline frame rate | Conversion must be planned, not implied. |

**House rule:** Do not publish universal CFG ranges, frame-grid formulas, or seed semantics.

### 4.2 Time representation

- Canonical times are numeric seconds.
- Beat intervals use `[start_s, end_s)`.
- Prompt timestamps are a rendered representation.
- Frame-accurate delivery uses integer timeline frames.
- Actual media timing is checked after generation.

For a constant-frame-rate timeline:

```text
timeline_duration_s = timeline_frame_count / timeline_fps
```

The interval between the first and last frame timestamps is a different quantity from total playback duration.

### 4.3 Subjects and identity

A subject description SHOULD contain only useful distinguishing information:

- Stable identifier.
- Relevant appearance.
- Current wardrobe.
- Position or role within the frame.
- Expression or performance arc.
- Prop interaction.

Separate permanent identity from scene state:

```yaml
identity:
  id: CHAR.LIN
  anchors:
    - short black hair
    - silver streak at left temple

scene_state:
  wardrobe: navy linen shirt
  condition: sleeves damp at the cuffs
  prop: unopened kraft envelope
```

**House rule:** Exact counts may remain hard requirements. Do not silently make them vague; report count-critical shots as requiring inspection or controlled composition.

### 4.4 Environment and background

Describe only layers that matter to the composition:

- Location and geography.
- Time of day.
- Weather.
- Foreground, midground, background.
- Practical light sources.
- Crowd or traffic behavior.
- Reflections and atmospheric motion.
- Signage and graphics policy.

An empty studio background does not require artificial foreground/midground/background detail.

**Continuity rule:** “Same alley” is not sufficient by itself. Resolve it to an approved location description and, where supported, an actual reference asset.

### 4.5 Lighting and look

Separate physical lighting from finish:

```yaml
lighting:
  key: soft cool window light from camera-left
  practical: warm shaded lamp behind the subject
  contrast: low-key with readable shadow detail

look:
  medium: restrained 35mm-film texture
  color: cool exterior tones, natural skin
  depth_of_field: moderately shallow
```

Avoid contradictory combinations unless intentional.

A tiny appliance indicator may be visible set dressing; do not assign it the role of a substantial fill light without a plausible stylized rationale.

### 4.6 Action and physical causality

Actions SHOULD identify:

1. Starting state.
2. Initiating movement.
3. Contact or interaction.
4. Environmental response.
5. Resulting state.

Example:

```text
The cup tilts.
Tea reaches the rim.
A narrow stream lands on the cloth.
The cloth darkens outward from the impact point.
The cup returns upright.
```

**Heuristic:** Prefer one principal event with a small number of dependent beats over unrelated simultaneous events.

### 4.7 Camera

Store camera dimensions separately:

| Dimension | Examples |
|---|---|
| Framing | Close-up, medium shot, wide shot, two-shot |
| Angle | Eye-level, low, high, overhead |
| Position | Profile, three-quarter, over shoulder |
| Movement | Locked, dolly, track, pan, tilt, crane, arc |
| Focus | Deep focus, shallow focus, rack focus |
| Lens intent | Wide environmental view, normal perspective, compressed portrait |
| Start/end composition | Hands visible at start; envelope remains visible at end |

**House rule:** Default to one primary camera move per shot. Compound moves are allowed when necessary and temporally coherent.

Do not pair a face-only close-up with a hand action that must be visible unless the camera reframes.

### 4.8 Audio

Use four **conceptual categories**:

| Category | Required description when used |
|---|---|
| Dialogue | Speaker, exact text, language, delivery, timing window |
| SFX | Source, action, material, proximity, event timing |
| Ambience | Continuous environment and spatial perspective |
| Music | Function, style, entry/exit, or explicit absence |

These categories do not imply independently downloadable stems.

```yaml
audio:
  production: native
  dialogue: []
  sfx:
    - paper flexes near the camera
  ambience:
    - quiet refrigerator hum
    - rain against the window
  music: none
  delivery_policy: retain_if_approved
```

Allowed production policies:

- `native`
- `post`
- `hybrid`
- `silent`

For silence, distinguish:

- No dialogue.
- No music.
- Environmental sound only.
- Completely silent final delivery.

If strict digital silence is required, enforce it in the delivered media rather than relying only on descriptive wording.

### 4.9 Dialogue timing

**Heuristic:** For initial English-language planning, estimate roughly two spoken words per second, then allow time for breathing, reaction, and turn-taking.

This is not a universal language rule or a measured model limit.

```text
available_speech_time
    = speech_window
    − pauses
    − reaction_time
    − transition_margin
```

For production:

- Time a read-through.
- Use the actual language and delivery.
- Separate speaker turns.
- Avoid overlapping speakers unless necessary.
- Do not silently rewrite approved dialogue to fit.

### 4.10 Negative instructions and constraints

Canonical exclusions are model-independent:

```yaml
constraints:
  forbid:
    - burned-in subtitles
    - additional foreground pedestrians
```

The adapter decides whether to express them as:

- A documented negative-prompt field.
- Plain-language constraints.
- Positive composition.
- Post-production requirements.
- Unsupported requirements requiring another approach.

Google’s guide uses concrete exclusions; Runway Gen-4 recommends positive phrasing and discourages negative prompts. These are different adapter behaviors, not a universal rule. ([cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1))

Do not include removal of required provenance marking as a quality requirement. The supplied Veo guide identifies SynthID marking as part of generated output provenance. ([cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1))

---

## 5. Veo reference implementation

This section translates the two supplied Google guides into a production workflow.

### 5.1 Five-part visual structure

```text
[Cinematography]
+ [Subject]
+ [Action]
+ [Context]
+ [Style & Ambiance]
```

Then add explicit audio and any necessary continuity instructions.

The ordering is Google Cloud’s recommended formula, not a formal parser grammar. DeepMind also demonstrates beginning with visual style; the two guides are complementary rather than mutually exclusive. ([cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1))

### 5.2 Practical template

```text
[Shot size, angle, camera movement, focus.]

[Subject identification and relevant appearance.]
[Actions in chronological order.]

[Location, time, weather, important background behavior.]

[Lighting, visual texture, color, emotional tone.]

Dialogue: [Speaker, delivery, exact words.]
SFX: [Specific synchronized effects.]
Ambient noise: [Continuous soundscape.]
Music: [Description or none.]

[Necessary continuity and composition constraints.]
```

`Dialogue:`, `SFX:`, and similar labels organize natural-language instructions. They are not assumed to create separate audio tracks.

### 5.3 Text-to-video example

**Generation request:** 8 seconds; supported aspect and resolution selected separately.

```text
Medium shot at counter height, a very slow push-in that keeps both hands
and the envelope visible.

Lin, a woman in her late twenties with short black hair and a silver streak
at her left temple, wears a navy linen shirt. She holds an unopened kraft
envelope over a tiled kitchen counter. She turns it over once, pauses,
then places it flat and leaves her palm resting on it.

A small walk-up kitchen at blue hour. Rain tracks down the window behind
the sink. A yellow crate of tangerines sits at the rear of the counter.
The room remains empty apart from Lin.

Soft cool window light enters from camera-left; a warm shaded lamp glows
in the background. Restrained film grain, natural skin tones, quiet resolve.

SFX: a close paper flex, then a soft envelope tap on tile.
Ambient noise: rain against glass and a low refrigerator hum.
No dialogue or music. No burned-in captions.

The envelope remains unopened throughout.
```

### 5.4 Workflow A: first and last frame

The Google Cloud guide describes generating two endpoint images and using Veo to create the transition between them. ([cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1))

**Production procedure:**

1. Create or approve the starting frame.
2. Create or approve the ending frame.
3. Check identity, wardrobe, props, lighting, geography, and aspect compatibility.
4. Bind both images through the target’s supported input mechanism.
5. Describe the journey—not merely the two endpoints.
6. Review the intermediate motion and final-frame match.

Example:

```text
One continuous medium shot. Starting from the supplied first frame,
she lowers the unopened envelope from chest height to the counter,
turns it once, and lays it flat beneath her right palm, arriving at the
supplied ending composition. The camera makes a gentle forward move.
Her left hand releases the envelope before her right palm settles.

SFX: paper flex and a soft contact with tile.
Ambient noise: rain against the window.
No speech or music.
```

**House rule:** Do not use incompatible endpoint images and expect the prompt to repair the contradiction invisibly.

### 5.5 Workflow B: reference-guided dialogue coverage

The supplied guide uses character and location reference images to generate complementary dialogue shots. ([cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1))

**Production procedure:**

1. Approve character and location assets.
2. Assign each asset a role.
3. Establish screen positions and eyelines.
4. Generate a master or primary shot.
5. Generate complementary coverage with the same resolved continuity.
6. Inspect voice, identity, eyeline, and audio perspective across cuts.

**Important:** A sentence such as “use Image 1” does not upload an image. Asset binding must occur in the request or UI.

### 5.6 Workflow C: timestamp prompting

The Google Cloud guide demonstrates a complete eight-second sequence divided into timed shot descriptions. ([cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1))

Use timestamps as **requested pacing**, not a substitute for frame-accurate editing:

```text
[00:00–00:02] Locked close-up of a brass key resting beside a wet glove.
A hand enters and lifts the key. SFX: a small metal scrape.

[00:02–00:05] Medium shot of the same courier at a service door.
She inserts the key and turns it once. SFX: lock mechanism clicks.

[00:05–00:08] View from inside the dark room as the door opens.
A narrow strip of cool corridor light widens across the floor.
Ambient noise: distant rain. No dialogue or music.
```

If exact cut placement is mandatory, generate separate plates and assemble them.

### 5.7 Workflow D: prompt enhancement

Both supplied guides describe using Gemini to expand or enrich prompts. ([cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1))

For production, constrain the enhancement step:

```text
May add:
- Concrete spatial relationships.
- Camera terminology.
- Material and lighting specificity.
- Clearer causal ordering.

Must preserve:
- Approved dialogue.
- Character identity.
- Plot outcome.
- Required objects.
- Duration and shot count.
- Intended audio policy.

Must not invent:
- Additional characters.
- New locations.
- New dialogue.
- Unrequested music.
- A different ending.
```

Store the original brief, enhanced prompt, and a change summary.

---

## 6. Prompt types: preserve IDs, separate dimensions

The v1 type IDs remain valid labels, but they are not mutually exclusive settings.

| ID | Type | Dimension |
|---|---|---|
| T1 | Micro caption | Prompt form |
| T2 | Shot card | Prompt form |
| T3 | Director prose | Prompt form |
| T4 | Labeled blocks | Prompt form |
| T5 | Timestamp sequence | Temporal form |
| T6 | Multi-shot generation | Clip structure |
| T7 | Image-to-video motion delta | Input mode |
| T8 | First/last-frame transition | Input mode |
| T9 | Reference-guided video | Input mode |
| T10 | Talking head | Use case |
| T11 | Product shot | Use case |
| T12 | Physical interaction | Use case |
| T13 | Parameter-led workflow | Execution form |
| T14 | Positive/negative prompt pair | Adapter form |
| T15 | Canonical YAML/JSON | Storage form |
| T16 | Compiler brief | Authoring stage |
| T17 | Loop or ambient plate | Delivery/use case |
| T18 | Extension | Input mode |
| T19 | Video edit | Input mode |
| T20 | Sequence packet | Production scope |
| T21 | Feature packet | Production scope |
| T22 | Code-native assembly | Delivery method |
| T23 | Background plate | Use case |
| T24 | Performance transfer | Input mode |

Example:

```yaml
classification:
  prompt_form: labeled_blocks
  input_mode: reference_to_video
  clip_structure: single_shot
  use_case: dialogue
  production_scope: sequence
  legacy_tags: [T4, T9, T20]
```

Do not use a single `setting: T15` field as a substitute for mode, use case, and structure.

---

## 7. Canonical clip object

### 7.1 Serialization rules

- YAML and JSON represent the same object.
- UTF-8 text is required.
- Missing or `null` means unspecified.
- `[]` means explicitly no entries.
- `false` means explicitly disabled.
- Vendor handles are not canonical asset identifiers.
- Unknown vendor fields belong under `vendor_parameters`.
- Project-specific extensions belong under `extensions`.
- Drafts may contain unresolved fields.
- Executable requests may not contain unresolved required fields.

### 7.2 Complete authoring example

```yaml
schema: video_generation_prompt_specification.v2
spec_version: "2.0.0"
kind: clip
clip_id: CLIP.LETTER.014
revision: 1

classification:
  prompt_form: director_prose
  input_mode: reference_to_video
  clip_structure: single_shot
  use_case: narrative
  production_scope: sequence
  legacy_tags: [T3, T9, T15, T20]

target:
  profile_id: google.veo31.reference_video.example
  profile_revision: 1
  model_id: veo-3.1-generate-001
  mode: reference_to_video

generation:
  duration_s: 8
  aspect_ratio: "16:9"
  resolution: "1080p"
  frame_rate_fps: null
  num_frames: null
  seed: null
  prompt_enhancement: preserve_authoring
  vendor_parameters: {}

delivery:
  in_s: 0
  out_s: 8
  timeline_duration_s: 8
  aspect_ratio: "16:9"
  frame_rate_fps: 24
  retime_policy: none
  reframe_policy: none
  audio_policy: retain_if_approved
  graphics_policy: post_only

intent:
  logline: Lin decides not to open the letter.
  emotion: quiet resolve
  required_outcome: envelope remains sealed on the counter

assets:
  - asset_id: ASSET.LIN.PORTRAIT.03
    media_type: image
    path: assets/lin/portrait_03.png
    sha256: null
    binding:
      role: identity_reference
      applies_to: CHAR.LIN
      use_for:
        - face
        - hair
      exclude_from_guidance:
        - background
        - wardrobe
    rights_record_id: RIGHTS.LIN.03

  - asset_id: ASSET.KITCHEN.PLATE.02
    media_type: image
    path: assets/kitchen/plate_02.png
    sha256: null
    binding:
      role: environment_reference
      applies_to: LOC.KITCHEN
      use_for:
        - counter geometry
        - window position
        - tile color
      exclude_from_guidance: []
    rights_record_id: RIGHTS.KITCHEN.02

creative:
  continuity:
    character_bible_id: BIBLE.CHAR.LIN.R3
    location_bible_id: BIBLE.LOC.KITCHEN.R2
    look_bible_id: BIBLE.LOOK.LETTER.R1
    previous_clip_id: CLIP.LETTER.013
    previous_end_state:
      envelope: sealed and held in both hands
      wardrobe: navy linen shirt
      location: beside the kitchen counter

  shots:
    - shot_id: SHOT.LETTER.014A
      start_s: 0
      end_s: 8

      subjects:
        - subject_id: CHAR.LIN
          identity: >-
            Woman in her late twenties, short black hair,
            silver streak at the left temple.
          wardrobe: navy linen shirt and small gold studs
          performance: tired stillness followed by a contained breath

      environment:
        location_id: LOC.KITCHEN
        description: small third-floor walk-up kitchen
        time_of_day: blue hour
        weather: light rain outside
        foreground:
          - tiled counter edge
          - envelope and hands
        midground:
          - Lin
          - sink
        background:
          - rain-streaked window
          - yellow crate of tangerines
          - shaded practical lamp
        population: Lin alone
        text_policy: no generated readable signage

      lighting:
        key: soft cool window light from camera-left
        practical: dim warm shaded lamp in the background
        contrast: low-key with readable skin and hands

      look:
        medium: restrained 35mm-film texture
        color: cool shadows and natural skin
        depth_of_field: moderately shallow

      camera:
        framing: medium shot with face, hands, and counter visible
        angle: eye-level three-quarter view
        movement: very slow push-in
        focus: maintain readable envelope and hand action
        end_framing: envelope remains inside the frame

      action:
        start_state: sealed envelope held just above the counter
        beats:
          - start_s: 0
            end_s: 2
            action: holds still and looks down at the envelope

          - start_s: 2
            end_s: 5
            action: turns the envelope over once without opening it

          - start_s: 5
            end_s: 7
            action: places it flat on the tile and rests her right palm on it

          - start_s: 7
            end_s: 8
            action: holds the final position and releases a small breath

        end_state: sealed envelope flat on tile beneath her right palm

  audio:
    production: native
    dialogue: []

    sfx:
      - start_s: 2
        end_s: 5
        description: close paper flex during the turn

      - start_s: 5
        end_s: 7
        description: soft envelope contact with tile

    ambience:
      - rain against the window
      - quiet refrigerator hum

    music: none
    spatial_note: paper close; rain behind Lin
    exact_timing_required: false

constraints:
  hard:
    - envelope remains unopened
    - navy linen wardrobe remains unchanged
    - no additional people
    - no editorial cuts

  soft:
    - restrained grain
    - very slow camera movement

  forbid:
    - burned-in subtitles
    - unrequested music

  acceptance:
    - the envelope turn is visible
    - the final envelope position is stable
    - face and wardrobe match the approved references
    - no audible dialogue
    - no visible cut

provenance:
  authored_at: "2026-09-14"
  source_brief_id: BRIEF.LETTER.014
  compiler_version: null
  compiled_at: null
  capability_profile_hash: null
  execution_manifest_id: null

extensions: {}
```

This example is an **authoring object**. Asset hashes, upload bindings, capability validation, and account availability must be resolved before execution.

### 7.3 Reference role limitations

`use_for` and `exclude_from_guidance` express intent. They do not guarantee selective disentanglement of an image.

If a reference contains distracting wardrobe, background, or lighting:

- Prefer a cleaner reference.
- Crop or prepare an approved reference where appropriate.
- Use separate assets for separate roles.
- Report reference conflicts before generation.

### 7.4 Minimal machine-readable envelope schema

The following validates the **document envelope**. It is not a complete validator for every creative subtree; semantic rules in Section 8 remain mandatory.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Video Generation Prompt Specification v2 — Clip Envelope",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema",
    "spec_version",
    "kind",
    "clip_id",
    "revision",
    "target",
    "generation",
    "delivery",
    "intent",
    "assets",
    "creative",
    "constraints",
    "provenance"
  ],
  "properties": {
    "schema": {
      "const": "video_generation_prompt_specification.v2"
    },
    "spec_version": {
      "const": "2.0.0"
    },
    "kind": {
      "const": "clip"
    },
    "clip_id": {
      "type": "string",
      "minLength": 1
    },
    "revision": {
      "type": "integer",
      "minimum": 1
    },
    "classification": {
      "type": "object"
    },
    "target": {
      "type": "object",
      "required": ["profile_id", "mode"],
      "properties": {
        "profile_id": {
          "type": "string",
          "minLength": 1
        },
        "mode": {
          "enum": [
            "text_to_video",
            "image_to_video",
            "first_last_frame",
            "reference_to_video",
            "video_to_video",
            "extend",
            "edit",
            "performance_transfer",
            "avatar"
          ]
        }
      }
    },
    "generation": {
      "type": "object",
      "required": ["duration_s"],
      "properties": {
        "duration_s": {
          "type": "number",
          "exclusiveMinimum": 0
        },
        "frame_rate_fps": {
          "type": ["number", "null"],
          "exclusiveMinimum": 0
        },
        "num_frames": {
          "type": ["integer", "null"],
          "minimum": 1
        },
        "vendor_parameters": {
          "type": "object"
        }
      }
    },
    "delivery": {
      "type": "object"
    },
    "intent": {
      "type": "object",
      "required": ["logline"]
    },
    "assets": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["asset_id", "media_type", "binding"]
      }
    },
    "creative": {
      "type": "object",
      "required": ["shots", "audio"],
      "properties": {
        "shots": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "object",
            "required": [
              "shot_id",
              "start_s",
              "end_s",
              "camera",
              "action"
            ]
          }
        },
        "audio": {
          "type": "object"
        }
      }
    },
    "constraints": {
      "type": "object"
    },
    "provenance": {
      "type": "object"
    },
    "extensions": {
      "type": "object"
    }
  }
}
```

A production implementation SHOULD publish additional schemas for assets, shots, audio events, profiles, sequence manifests, and execution records.

---

## 8. Validation and compiler contract

### 8.1 Validation passes

| Pass | Checks |
|---|---|
| **V1 Structure** | Required fields, types, identifiers, serialization. |
| **V2 Timing** | Valid intervals, shot boundaries, beat coverage, delivery duration. |
| **V3 Assets** | Files exist, hashes resolve, roles and subjects match. |
| **V4 Capabilities** | Exact mode and combined runtime settings are supported. |
| **V5 Creative consistency** | No contradictions between action, camera, references, and bibles. |
| **V6 Audio feasibility** | Speaker turns fit; native/post/silent policy is executable. |
| **V7 Compilation fidelity** | Every hard requirement is represented or explicitly blocked. |
| **V8 Execution readiness** | Credentials, access, uploads, quota, and output destination resolve. |

### 8.2 Semantic timing rules

For every shot:

```text
0 ≤ start_s < end_s ≤ generation.duration_s
```

For every beat:

```text
shot.start_s ≤ beat.start_s < beat.end_s ≤ shot.end_s
```

For a single-shot clip:

```text
shots.length = 1
shot.start_s = 0
shot.end_s = generation.duration_s
```

For delivery without retiming:

```text
0 ≤ delivery.in_s < delivery.out_s ≤ generated_media_duration_s

delivery.timeline_duration_s
    = delivery.out_s − delivery.in_s
```

Gaps or overlaps in a requested multi-shot timeline MUST be intentional and documented.

### 8.3 Mode requirements

| Mode | Required input |
|---|---|
| Text-to-video | Creative text or supported structured input. |
| Image-to-video | Actual starting image. |
| First/last-frame | Actual starting and ending images. |
| Reference-to-video | At least one supported reference asset. |
| Video-to-video / edit | Actual source video and transformation intent. |
| Extend | Compatible source clip or vendor generation identifier. |
| Performance transfer | Supported identity and performance inputs. |
| Avatar | Supported avatar identity and performance/script inputs. |

### 8.4 Conflict handling

Do not silently resolve contradictions such as:

- “Locked camera” and “orbit around the subject.”
- “No speech” and a dialogue line.
- Reference wardrobe inconsistent with a hard wardrobe lock.
- A sealed envelope at the end and an action that opens it.
- A two-second generation request on a profile that requires a longer output.
- Native audio required on an endpoint without native audio support.

Return a blocking diagnostic or an explicit adaptation proposal.

### 8.5 Compilation dispositions

Every requirement receives one disposition:

| Disposition | Meaning |
|---|---|
| `exact` | Mapped to a supported runtime field or binding. |
| `prompted` | Expressed as natural-language guidance. |
| `approximated` | Represented by an imperfect alternative. |
| `post` | Assigned to an explicit downstream task. |
| `unsupported` | No approved implementation exists. |
| `not_applicable` | Proven irrelevant to this target or mode. |

`prompted` does not mean guaranteed.

### 8.6 Unsupported-field policy

Default: **strict**.

```yaml
compilation_policy:
  unsupported_hard_requirement: block
  unsupported_soft_requirement: warn
  adaptation_requires_approval: true
  preserve_canonical_object: true
```

Examples:

- Two-second delivery from a four-second source: propose trim.
- Final 2.39:1 frame from 16:9 generation: propose safe-area composition and crop.
- Native speech unavailable: propose post audio only if visible lip-sync is not a hard requirement.
- Exact typography: assign graphics work to post.

### 8.7 Compiler output package

```text
validated.canonical.yaml
compiled.prompt.txt
compiled.request.json
compiled.asset_bindings.json
compiled.delivery_tasks.json
compiled.diagnostics.json
compiled.manifest.json
```

`compiled.request.json` must contain only fields accepted by the selected endpoint. The canonical object remains unchanged.

### 8.8 Example diagnostic

```yaml
status: blocked

diagnostics:
  - code: CAPABILITY_DURATION_UNSUPPORTED
    severity: error
    path: generation.duration_s
    requested: 2
    message: Selected profile does not support a two-second generation.
    proposal:
      generate_duration_s: 4
      delivery_in_s: 1
      delivery_out_s: 3
    approval_required: true

requirement_coverage:
  - requirement: two-second final insert
    disposition: post
    implementation: approved source trim
```

### 8.9 LLM compiler system instruction

```text
You compile video_generation_prompt_specification.v2 objects.

Use only the supplied capability profile and resolved assets.
Do not infer undocumented vendor syntax or runtime fields.
Do not invent plot, dialogue, characters, locations, music, or references.

Preserve approved dialogue and continuity facts.
Keep canonical intent separate from emitted prompt text.
Validate timing, mode prerequisites, reference bindings, and capability combinations.

Use motion-focused wording for image-to-video where the target guide recommends it.
Do not remove necessary subject disambiguation.
Do not treat reference handles in prose as uploaded assets.

Never silently drop a hard requirement.
Report exact, prompted, approximated, post, and unsupported mappings.
If execution is blocked, return diagnostics instead of a pretend-valid request.

Return:
1. Validated canonical object.
2. Model-facing prompt.
3. Runtime request.
4. Asset bindings.
5. Delivery tasks.
6. Diagnostics and requirement coverage.
```

---

## 9. Sample library

All prompts below are illustrative creative briefs. Durations are generated durations unless explicitly labeled **delivery duration**.

### S01 — Two-second micro-insert

**Types:** T1, T20  
**Delivery:** 2 seconds  
**Generation:** A supported source duration.

```text
Locked macro view of a raindrop suspended from the corner of a red paper
lantern. The drop lengthens, detaches, and falls out of frame.
Soft night reflections. A single quiet drip; no music.
```

Select a two-second interval containing the full event. Do not stretch the shot merely to meet a source-duration setting.

### S02 — Four-second sensory object shot

**Types:** T2, T11

```text
Close-up, locked camera. Dark coffee pours into a white ceramic cup,
the stream slowing to a final drip. Soft morning window light from the left.
The cup remains fully visible. Audio: close pouring sound and a quiet ceramic
touch. No speech or music.
```

### S03 — Six-second product shot

**Types:** T3, T11

```text
Medium close-up of an unbranded frosted glass bottle on wet black stone.
A slow lateral camera move reveals its curved edge while a single droplet
slides down the glass. Soft overhead key and narrow rear rim light.
Dark studio background.

SFX: one quiet droplet contact.
No dialogue or music. Leave the label area blank for graphics in post.
```

### S04 — Eight-second restrained dialogue

**Types:** T3, T10

```text
Medium close-up, eye-level, locked camera. A tram inspector in a worn navy
jacket sits beside a rain-streaked depot window. She looks toward someone
just off camera, waits briefly, then says softly, "Not tonight."

She keeps her expression controlled and looks down after the line.
Cool window light, warm room behind her, natural skin tones.

Ambient noise: distant metal wheels and rain.
No music. No other speaker.
```

### S05 — Cantonese dialogue

**Types:** T3, T10

```text
Medium close-up beneath a clear umbrella, slow push-in. Lin looks toward
an upstairs window, then says quietly in Cantonese, "未係時候。"
She remains still afterward.

Rain taps against the umbrella canopy. Distant traffic stays soft.
No music or burned-in subtitles.
```

**Production note:** Language, pronunciation, delivery, and lip-sync require review. Approved dialogue must not be translated automatically by the compiler.

### S06 — Image-to-video motion delta

**Types:** T7

```text
The subject turns the envelope over once, then places it flat on the counter.
Her right palm settles on it while her left hand relaxes beside it.
The camera gently moves closer, keeping both hands visible.
Rain continues down the window.
```

This illustrates motion-focused I2V wording consistent with Runway’s guidance; audio requirements belong in the supported audio path or delivery plan. ([help.runwayml.com](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide?utm_source=openai))

### S07 — First/last-frame controlled movement

**Types:** T8

```text
One continuous low-angle medium-wide shot. From the supplied starting pose,
the performer shifts her weight backward, raises the polearm in a single
controlled arc, and settles into the supplied ending stance.
The camera tracks slightly right to keep the blade inside the frame.

Rain beads scatter from the blade during the movement.
Audio: rain on stone, a brief cloth snap, and the blade moving through air.
No speech or music.
```

Check blade position, body balance, wardrobe, and endpoint compatibility before generation.

### S08 — Reference-guided conversation coverage

**Types:** T9, T20

**Shared assets:** Lin reference, Ma reference, tram doorway reference.

**Shot A:**

```text
Medium shot of Lin standing inside the tram doorway, looking down toward Ma
outside. Warm cabin light behind Lin, cool rain beyond the doorway.
Lin says, "You shouldn't stand in that."
Ma remains off-screen and silent.

Ambient noise: rain and the idling tram.
```

**Shot B:**

```text
Complementary medium shot of Ma outside the tram, looking up toward Lin.
Match the established screen direction and rain density.
Ma answers dryly, "The roof is worse."

Ambient noise: the same rain and idling tram, heard from outside.
```

Two shots are easier to revise independently than a densely packed exchange.

### S09 — Eight-second causal action plate

**Types:** T3, T12

```text
Low tracking view beside a mud-covered buggy approaching a shallow stream.
Its front wheels enter first, pushing a bow wave outward. The rear wheels
follow, throwing muddy spray behind it. The buggy climbs the far bank,
its suspension compressing and recovering once.

Bright broken sunlight through trees; documentary texture.
Audio: engine strain, water impact, and a heavy suspension thump.
No commentary or music.
```

For a pursuing truck, generate a separate complementary plate unless both vehicles are essential to the same event.

### S10 — Eight-second return-to-state loop candidate

**Types:** T17

```text
Locked close-up of a paper lantern moving gently in a light breeze.
It begins near the center, drifts slightly left, passes slowly right,
and returns toward its starting position and direction of motion.
Steady soft illumination, unchanged background.

Continuous quiet wind. No speech, music, or isolated sound event.
```

Loop acceptance requires visual and audio seam inspection. Matching position alone is insufficient.

### S11 — Background plate

**Types:** T23

```text
Locked wide view of an empty kitchen at blue hour.
Foreground: tiled counter edge.
Midground: sink and unlit kettle.
Background: rain-streaked window, a warm shaded lamp, and a yellow crate
of tangerines.

Only rain and faint curtain movement.
Audio: refrigerator hum and rain against glass.
No people, dialogue, or music.
```

### S12 — Video edit delta

**Types:** T19

```text
Change the exterior light visible through the window from afternoon
to blue hour. Preserve the actor, wardrobe, blocking, camera path,
and interior practical-light positions.

Keep the source performance and dialogue timing unchanged.
```

This is a generic edit brief. The selected editor must document the required preservation and audio behavior.

### S13 — Extension brief

**Types:** T18

```text
Continue from the supplied clip. Lin lifts her hand from the unopened
envelope and exits frame right. The camera stays on the envelope.
Rain continues at the same intensity. No new person enters.

Preserve the counter arrangement and blue-hour lighting.
```

Inspect the join for motion, exposure, geometry, and audio discontinuity.

### S14 — Parameter-led SVD workflow

**Types:** T13

```yaml
input_image: assets/ocean_still.png

pipeline_parameters:
  motion_bucket_id: 80
  noise_aug_strength: 0.02

creative_description_for_archive:
  intent: gentle ocean swell
  camera: apparently stationary

delivery:
  audio: post
```

For the standard Diffusers SVD pipeline, archive prose as intent rather than pretending it is a supported text input. The implementation exposes image conditioning and motion-related parameters. ([github.com](https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_video_diffusion/pipeline_stable_video_diffusion.py?utm_source=openai))

### S15 — Twenty-four-second product sequence

**Types:** T20

| Timeline | Clip | Purpose | Audio |
|---|---|---|---|
| 00:00–00:06 | A1 | Droplet on the bottle | Close droplet sound |
| 00:06–00:12 | A2 | Runner picks up the same bottle | Cloth, footsteps |
| 00:12–00:18 | A3 | Bottle on lakeside stone | Water and wind |
| 00:18–00:24 | A4 | Runner lowers bottle after drinking: “Still cold.” | Line, then optional score |

**Shared look:** Cool early-morning daylight; bottle design locked. Studio and lakeside setups receive separate lighting descriptions.

**Graphics:** Logo and end-card typography in post.

Do not require cap removal, drinking, swallowing, dialogue, and a dramatic reaction in the same short clip unless the timed performance fits.

### S16 — Sixty-second narrative: *The Letter*

**Types:** T20

| Timeline | Clip | Action |
|---|---|---|
| 00:00–00:06 | L01 | Rainy alley; upstairs window illuminated |
| 00:06–00:12 | L02 | Lin reaches the kitchen doorway |
| 00:12–00:20 | L03 | Turns the unopened envelope and sets it down |
| 00:20–00:28 | L04 | Watches rain through the window |
| 00:28–00:36 | L05 | Switches on the kettle |
| 00:36–00:44 | L06 | Places a second cup beside the first |
| 00:44–00:52 | L07 | Writes a short note on a separate blank slip |
| 00:52–01:00 | L08 | Turns off the lamp; window remains faintly blue |

**Text requirement:** If the note must read exactly “not tonight,” add it through a controlled insert or tracked graphic. Do not make generated handwriting the only way the narrative communicates its meaning.

### S17 — Ninety-second trailer

**Types:** T20

Exact example allocation:

```text
10 picture clips × 8 seconds = 80 seconds
1 title card × 4 seconds     =  4 seconds
1 end card × 6 seconds       =  6 seconds
TOTAL                       = 90 seconds
```

The music timeline is authored across the complete trailer, not independently improvised in every clip.

### S18 — Fifty-four-second dramatic scene

**Types:** T20

```text
SCENE 24 — TRAM DOORWAY / CABIN — NIGHT

24-01  6s  Wide: tram arrives; Ma waits beneath a leaking shelter.
24-02  8s  Medium: Lin and Ma exchange two short lines.
24-03  5s  Insert: envelope emerges halfway from Lin's pocket, then stops.
24-04  5s  Close-up: steam rises from Ma's thermos lid.
24-05  8s  Two-shot: they sit one bench apart.
24-06  8s  Close-up: Lin says, "Not tonight," then holds.
24-07  6s  Wide: doors open; Ma leaves.
24-08  8s  Medium: Lin remains beside the empty seat.

TOTAL: 54 seconds.
```

These are **editorial plate durations**. Generate longer supported sources and trim where necessary.

To reach three minutes, add 126 seconds of deliberate coverage, performance, or scene development. Do not relabel the same material.

---

## 10. Sequence and feature production

### 10.1 Sequence package

```text
project/
  brief.md
  script.md

  bibles/
    characters/
    locations/
    look.md
    sound.md
    world_rules.md

  assets/
    approved/
    asset_manifest.json

  clips/
    CLIP_001/
      canonical.yaml
      compiled/
      takes/
      review.json

  continuity/
    ledger.csv

  edit/
    timeline.json
    graphics/
    audio/

  delivery/
    specifications.yaml
    qc_reports/
```

### 10.2 Continuity ledger

Recommended fields:

```text
scene_id
clip_id
approved_take_id
story_time
location_id
character_id
wardrobe
hair
wetness_or_dirt
injury_state
prop_state
screen_position
movement_direction
eyeline
key_light_direction
weather
start_state
end_state
approved_reference_ids
```

Track changes intentionally. “Keep everything identical” is incorrect when the story requires a wet coat to dry, an object to move, or a light to switch off.

### 10.3 Feature package example

```yaml
schema: video_generation_prompt_specification.v2
kind: project
project_id: FEATURE.RAIN_LINE
working_title: Rain Line

delivery:
  runtime_target_s: 5400
  aspect_ratio: "2.39:1"
  frame_rate_fps: 24
  graphics: post
  audio_master: post

logline: >-
  A night-shift tram inspector carries an unopened letter across the city
  and decides not to deliver it.

bibles:
  world: BIBLE.WORLD.R1
  cast: BIBLE.CAST.R3
  locations: BIBLE.LOCATIONS.R2
  look: BIBLE.LOOK.R2
  sound: BIBLE.SOUND.R1

structure:
  act_1:
    start_s: 0
    end_s: 1500
  act_2:
    start_s: 1500
    end_s: 3900
  act_3:
    start_s: 3900
    end_s: 5400

coverage_policy:
  planning_unit: scene
  generation_unit: validated_clip
  editorial_unit: approved_trim
  multi_shot_generation: selective
  reference_refresh: at_scene_boundaries
  typography: controlled_graphics

continuity:
  ledger: continuity/ledger.csv
  canonical_refs: assets/approved/

generation_policy:
  choose_target_by: measured_project_tests
  max_attempts_per_clip: 6
  escalation_after_failures: revise_blocking_or_method
  unapproved_model_substitution: forbidden
```

### 10.4 Runtime arithmetic

For planning:

```text
required_picture_segments
    ≈ generated-picture runtime / average approved segment duration
```

Example:

```text
5,400 seconds / 6 seconds = 900 approved segments
```

This is an arithmetic illustration, not a prediction of shot count.

Adjust for:

- Live-action or archival material.
- Longer approved takes.
- Graphics and credits.
- Reused shots.
- Overlapping transitions.
- Editorial holds.
- Trims and handles.

### 10.5 Generation-volume planning

```text
generated_seconds
    = Σ(requested duration of every attempted generation)
```

A simple scenario:

```text
900 required segments
× 3 attempts per segment
× 8 generated seconds per attempt
= 21,600 generated seconds
= 6 hours of source output
```

That is a planning assumption, not a measured acceptance rate. Track actual usable seconds per attempt.

### 10.6 Long-form pipeline

```text
brief
→ script and scene objectives
→ bibles and asset approval
→ storyboard or animatic
→ clip specifications
→ capability validation
→ prompt compilation
→ candidate takes
→ review and selection
→ continuity updates
→ editorial assembly
→ sound and graphics
→ finishing
→ delivery QC
```

**House rule:** Select models through project-specific tests, not unsupported blanket rankings such as “Model A for all dialogue” or “Model B for all action.”

---

## 11. Assembly and post-production

### 11.1 Exact requirements belong in controlled stages

Assign the following explicitly when they are critical:

- Typography and logos.
- Frame-accurate cuts.
- Exact music entries.
- Silence.
- Final aspect ratio.
- Delivery frame rate.
- Loudness and channel layout.
- Color-space conversion.
- Captions.
- Repair of problematic lip-sync or continuity.

Native generation may supply usable material, but acceptance remains a production responsibility.

### 11.2 Corrected Remotion example

The documented sequential pattern uses `Series.Sequence` children. ([remotion.dev](https://www.remotion.dev/docs/series))

```tsx
import {
  OffthreadVideo,
  Series,
  staticFile,
  useVideoConfig,
} from "remotion";

export const LetterSequence = () => {
  const {fps} = useVideoConfig();

  return (
    <Series>
      <Series.Sequence durationInFrames={8 * fps}>
        <OffthreadVideo
          src={staticFile("approved/letter_014.mp4")}
          muted
        />
      </Series.Sequence>

      <Series.Sequence durationInFrames={6 * fps}>
        <OffthreadVideo
          src={staticFile("approved/letter_015.mp4")}
          muted
        />
      </Series.Sequence>
    </Series>
  );
};
```

Assumptions:

- The composition is configured at 24 fps.
- The approved inputs are already prepared for the selected intervals.
- The final audio is assembled separately.
- Total picture duration is 14 seconds.

### 11.3 Chaining policy

Use an approved ending frame as a new starting image only when it serves the shot design.

Before chaining, inspect:

- Identity.
- Geometry.
- Prop state.
- Motion direction.
- Camera position.
- Exposure and color.
- Accumulated artifacts.

**House rule:** Refresh from approved references at suitable scene boundaries instead of indefinitely inheriting errors from generated endpoints.

---

## 12. Quality gates and iteration

### 12.1 Before generation

- [ ] Shot purpose is clear.
- [ ] Mode and target profile are resolved.
- [ ] Runtime combination is supported.
- [ ] Required assets exist and are correctly bound.
- [ ] Actions fit the available time.
- [ ] Camera framing reveals the required action.
- [ ] Audio production policy is explicit.
- [ ] Dialogue is approved and timed.
- [ ] Continuity requirements are resolved.
- [ ] Hard constraints have implementation dispositions.
- [ ] Post tasks are recorded.
- [ ] No unresolved blocking diagnostics remain.

### 12.2 After generation

Evaluate the actual take:

| Dimension | Check |
|---|---|
| Intent | Does the required event occur? |
| Identity | Does the subject match the approved reference? |
| Wardrobe and props | Are required details stable? |
| Motion | Are contacts, trajectories, and transitions acceptable? |
| Camera | Does framing and movement support the action? |
| Environment | Is geography coherent? |
| Audio | Correct speaker, wording, sound sources, and music policy? |
| Timing | Does the usable action fit the edit? |
| Continuity | Does the take connect to adjacent shots? |
| Delivery | Are technical and provenance requirements satisfied? |

### 12.3 Acceptance model

Use hard gates plus optional scoring:

```yaml
review:
  hard_gates:
    required_action: pass
    identity: pass
    approved_dialogue: not_applicable
    continuity: fail
    delivery_integrity: pass

  scores:
    camera: 4
    lighting: 4
    physical_motion: 3
    audio: 4

  decision: reject
  reason: envelope changes from sealed to open
```

A high aesthetic score does not override a failed story requirement.

### 12.4 Iteration procedure

1. Identify one failure category.
2. Determine whether it originates in the prompt, reference, mode, or target.
3. Change the smallest useful variable.
4. Record the change.
5. Compare against the same acceptance criteria.
6. Escalate after the attempt budget is reached.

Possible escalation:

- Simplify blocking.
- Split the clip.
- Replace a conflicting reference.
- Change framing.
- Generate a controlled insert.
- Move the requirement to post.
- Select a different validated target.

Do not respond to every failure by adding more adjectives.

---

## 13. Provenance, permissions, and execution records

### 13.1 Asset governance

**House policy:** Record authorization for assets used as identity, voice, performance, music, or location references.

```yaml
asset_record:
  asset_id: ASSET.LIN.PORTRAIT.03
  origin: commissioned_reference
  creator_record_id: CREATOR.014
  permission_record_id: RIGHTS.LIN.03
  approved_uses:
    - character_reference
  restrictions: []
  sha256: resolved_before_execution
```

Do not place credentials or sensitive permission documents inside model-facing prompts.

### 13.2 Execution manifest

Archive:

```yaml
execution:
  manifest_id: EXEC.LETTER.014.TAKE03
  canonical_revision: 1
  canonical_hash: null
  profile_id: google.veo31.reference_video.example
  profile_revision: 1
  compiler_version: null

  request:
    prompt_hash: null
    runtime_parameters: {}
    uploaded_asset_ids: []
    seed: null

  result:
    provider_request_id: null
    submitted_at: null
    completed_at: null
    output_hash: null
    actual_duration_s: null
    actual_frame_rate_fps: null
    actual_dimensions: null
    audio_present: null

  review:
    status: pending
    reviewer: null
    approved_trim: null
```

### 13.3 Reproducibility wording

Prefer:

> “This manifest records the inputs and configuration used for the take.”

Do not promise:

> “The same seed will reproduce the same character and video forever.”

Record provider-side model changes or unavailable revisions when known.

---

## 14. Quick reference

### 14.1 Portable authoring card

```text
PURPOSE:
What must the viewer understand?

SUBJECT:
Who or what is essential?

START STATE:
What is already true?

ACTION:
What happens, in order?

END STATE:
What must be true at the end?

CAMERA:
Framing, position, primary movement, focus.

CONTEXT:
Location, time, weather, important background behavior.

LOOK:
Lighting, texture, color, mood.

AUDIO:
Dialogue, SFX, ambience, music—or final silence.

CONTINUITY:
What must match? What is allowed to change?

ASSETS:
Actual files and their roles.

GENERATION:
Target profile, mode, supported runtime settings.

DELIVERY:
Trim, timeline duration, aspect, frame rate, post tasks.

ACCEPTANCE:
Observable pass/fail requirements.
```

### 14.2 Compilation rules

```text
STORE:
Meaning, constraints, and provenance.

VERIFY:
Exact endpoint, mode, assets, and combined capabilities.

COMPILE:
One target dialect per request.

PRESERVE:
Canonical requirements and approved dialogue.

REPORT:
Approximations, unsupported fields, and post dependencies.

GENERATE:
Candidate takes, not presumed final shots.

REVIEW:
Story correctness before aesthetic preference.

ASSEMBLE:
Approved intervals, sound, graphics, and continuity.

ARCHIVE:
What was requested, what ran, what was delivered.
```

### 14.3 Core anti-patterns

- Treating a marketing name as an API identifier.
- Treating a prompt guide as a current availability contract.
- Mixing several vendors’ flags or reference tags.
- Writing an asset handle without binding an asset.
- Assuming every capability can be combined.
- Assuming a soundtrack description produces editable stems.
- Promising exact timing from timestamps alone.
- Omitting the action that connects two endpoint images.
- Asking for visible hand action in a face-only composition.
- Making a loop from an irreversible event without a reset strategy.
- Silently removing hard requirements.
- Describing a feature film as one generation request.
- Reusing an unverified numeric limit from a previous specification.

---

## 15. Migration from v1

| v1 field or practice | v2 destination |
|---|---|
| `shot_id` as the entire request identity | `clip_id` plus `creative.shots[].shot_id` |
| `setting: T15` | Orthogonal `classification` fields |
| `target.duration_s` | `generation.duration_s` |
| One `fps` field | Generation and delivery frame rates |
| `@Image1` in canonical storage | Stable asset ID plus compiled binding |
| `generate_audio: true` | Explicit production policy plus target-specific runtime mapping |
| `motion.beats[].t: "0-3s"` | Numeric `start_s` and `end_s` |
| Global “negative prompt” | Canonical constraints compiled per adapter |
| “Drop illegal fields” | Preserve, diagnose, and propose approved adaptations |
| Unqualified vendor capability table | Versioned profile with evidence |
| Single prompt plus YAML output | Full compilation and execution package |
| Approximate runtime labels | Validated timeline arithmetic |

### 15.1 Migration procedure

1. Preserve the original v1 object.
2. Move runtime settings into `generation`.
3. Add an explicit `delivery` plan.
4. Resolve textual reference handles to asset records.
5. Split identity from wardrobe and current state.
6. Convert time strings to numeric intervals.
7. Separate hard requirements from preferences.
8. Add acceptance criteria.
9. Select or build a verified target profile.
10. Compile with a requirement-coverage report.

Migration does not establish that a previously named model or endpoint is available.

---

## 16. Sources and version history

### 16.1 Primary sources used

- **Google Cloud:** *The ultimate prompting guide for Veo 3.1*, October 15, 2025. Source for the five-part formula, sound direction, reference workflows, endpoint-frame workflows, and timestamp examples. ([cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1))
- **Google DeepMind:** *How to create effective prompts with Veo 3*. Source for detailed character direction, sensory world-building, action play-by-play, style, audio, and everyday narratives. ([deepmind.google](https://deepmind.google/models/veo/prompt-guide/))
- **Google model reference:** Veo 3.1 model-specific capabilities and technical specifications. ([docs.cloud.google.com](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate))
- **Runway:** Gen-4 and image-to-video prompting guidance. ([help.runwayml.com](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide))
- **OpenAI:** Archived Sora 2 prompting guide, used for prompting and parameter-separation principles—not as proof of active availability. ([cookbook.openai.com](https://cookbook.openai.com/examples/sora/sora2_prompting_guide))
- **Hugging Face Diffusers:** Stable Video Diffusion documentation and pipeline implementation. ([huggingface.co](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/svd))
- **Remotion:** `Series` documentation. ([remotion.dev](https://www.remotion.dev/docs/series))

The two Google guides supplied with the brief are the primary editorial foundation. The additional sources support specific implementation corrections; they do not constitute a complete market survey.

### 16.2 Version history

| Version | Date | Notes |
|---|---|---|
| 1.0.0 | 2026-09-14 | Initial unified handbook and sample library. |
| 2.0.0 | 2026-09-14 | Capability profiles, evidence labels, typed timing, asset bindings, compilation diagnostics, delivery separation, corrected examples, provenance, and quality gates. |
| 2.0.1 | 2026-09-15 | CASOPS Video Swarm house rules: one canonical clip object, agent-owned fields, compiler adapters, Grok Imagine as the only live endpoint. Implementation plan in `issues/issue0009.md`. |
| 2.0.2 | 2026-09-15 | Sequence manifest (`kind: sequence`): one row per clip, generation unit remains clip, concat is post. |

### 16.3 Governing rule

> When documentation and this specification disagree about an endpoint, update the capability profile.
>
> When a target cannot express the requested intent, preserve the canonical object and report the gap.
>
> When a generated take fails a hard requirement, reject or repair the take—not the requirement.

---

## 17. CASOPS Video Swarm (house rules)

This section binds the portable v2 object to the Common Agent Structure **Video** swarm as it exists in this repository. It does **not** activate production, T3, plugins, or undeclared vendors.

**Evidence:** House rule, except Grok Imagine live generation (operator-verified) and fail-closed declared tags.

**Implementation plan:** `issues/issue0009.md`. Do not treat this section as shipped code.

### 17.1 Product metaphor

A coding agent calls a sub-agent or skill to write one routine. A video agent calls a domain expert to write **one owned field** of one **clip** (a generated video segment). The human supplies CONTROL: the initial brief plus option locks. The host assembles a canonical clip object. An adapter compiles that object into one vendor dialect.

```text
Human CONTROL (brief + ASK_HUMAN option ids)
    → intent-analysis / creative-agent (framework only)
    → video.promptengineer (orchestrates; does not write the novel)
    → domain experts write owned fields only
    → host join → canonical.yaml (storage form T15)
    → adapter compile → compiled.prompt.txt + compiled.request.json
    → Video Generator (Grok Imagine live; Seedance / LTX / … fail-closed until profiled)
```

**House rule:** One collab pass produces one clip. A longer piece is a sequence of clips (`kind: sequence`), not one overloaded generation.

### 17.2 Operator-facing projection (T4 labeled blocks)

Project Chat today shows labeled headings. Those headings remain the **operator projection** of the canonical object, not a second source of truth.

| Operator heading (Chat / output txt) | Canonical path | Owner agent |
|---|---|---|
| Creative direction | `intent` + `creative.continuity` thesis | `video.creativedirector` |
| Frame | `generation.duration_s`, `generation.aspect_ratio`, `classification` | `video.promptengineer` |
| Subject / Hair / Skin | `creative.shots[].subjects` identity + scene_state | `video.continuity` |
| Makeup | `creative.shots[].subjects[].scene_state` (face finish) | `video.mua_makeup` |
| Light | `creative.shots[].lighting` + `look` | `video.cinematographer` |
| Coverage / performance (beats) | `creative.shots[].action.beats` | `video.director` |
| Camera lock | `creative.shots[].camera` | `video.cameraoperator` |
| Sound | `creative.audio` | `video.promptengineer` (container) with director/SFX as needed |
| Negatives / constraints | `constraints.hard` / `soft` / `forbid` / `acceptance` | `video.critic` (may warn any path; may patch only `constraints` unless the human grants a field) |

**House rule:** An agent MUST NOT overwrite another agent's owned path. Critic MAY attach `diagnostics` and `constraints` on any path. Aesthetics / color / style belong under `look` (cinematographer or a declared look owner—not PE).

Beat labels in the current asain-beauty walkthrough (`0–3s | opening face smash`, …) are **clip-specific coverage**, not the universal schema. Store them as `action.beats[].action` with numeric `start_s` / `end_s`. Do not hard-code those five beauty-macro titles into the compiler.

### 17.3 Human CONTROL

Valid human locks stay the ISSUE-0007 set:

`video.promptengineer`, `video.director`, `video.cinematographer`, `video.mua_makeup`, `video.continuity`.

Cameraoperator and critic stay agent-to-agent unless a later issue adds a human lock.

The human brief is locution only (Create Project / Start record). Domain novels are option crafts. `sample/` is never a generation source. Distinctive gold-body probes MUST NOT be sent to agents or vendors.

### 17.4 Compiler and Video Generator

Every generator tag in `casops.project_generate.GENERATOR_TAGS` MUST have a **capability profile** (Section 2) before it may emit a live request.

| Tag | Status in this app today | v2 disposition |
|---|---|---|
| `grok-imagine` | Live Image 2.0 still then Video 1.5 I2V | Profile + compiler required. Mode `image_to_video`. |
| `grok-image` | Live still only | Mode is not video; compile still from identity/look only. |
| `kling`, `veo`, `seedance`, `sora`, `runway`, `luma`, `pika`, `hailuo`, `wan` | Declared, fail-closed | Backlog profiles. Compiler MUST return `unsupported` diagnostics, not a pretend request. |
| `ltx` | Declared, fail-closed | Stub profile `lightricks.ltx-2.stub`. Tag and profile ship together. Not live. |

**House rule:** The operator's CONTROL is the canonical object. Adapters may reorder, shorten, or split still vs motion (T7). They MUST NOT invent plot, wardrobe, or lighting. Dry-run remains the default.

Current `still_prompt` / `motion_prompt` are **heuristic compilers** for Grok Imagine. ISSUE-0009 replaces them with profile-driven compilation and requirement coverage.

### 17.5 Files on disk (target)

Per clip, under `project/<slug>/`:

```text
output/<slug>-canonical.yaml     T15 storage; agent-owned paths
output/<slug>-prompt.txt         Operator T4 projection (Chat panel)
output/<slug>-sequence.yaml      kind: sequence manifest (one row per clip; concat is post)
output/compiled/<engine>/        compiled.prompt.txt, compiled.request.json, diagnostics.json
output/<slug>.jpg / .mp4         takes (existing Imagine path)
```

Host join writes canonical + projection together. A vendor click compiles from canonical, not from `sample/`, and not from a free-text paste.

### 17.6 Honesty

ISSUE-0009 P0–P6 shipped as **CHARACTERIZATION** runtime. It is not an eval PASS. It is not a production license. Grok Imagine remains the only live generation path, and only with Dry-run off. Other declared tags (including LTX) stay fail-closed.

---

**End of `video_generation_prompt_specification.v2`**