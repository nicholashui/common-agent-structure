# Production Scale Discovery — Galleries, Showcases & Smart Selection

> How the system helps users understand what they want to build,
> browse real examples, and select the right production scale
> BEFORE committing budget or launching agents.

---

## The Problem

```text
CURRENT FLOW (confusing for new users):
  Create Project → "Pick template A-J" → "Set duration"

USER THINKS:
  "I don't know what Template E means"
  "Is 30 seconds enough for my idea?"
  "What does a $50 production look like vs a $200 one?"
  "Can I see examples of what this system actually makes?"

WHAT THEY NEED:
  Browse → Inspire → Understand scale → THEN configure
```

---

## Solution: Discovery Hub (new top-level section)

```text
UPDATED NAVIGATION:

Side Nav:
  ○ Dashboard
  ○ Discover    ← NEW (Galleries + Showcases + Templates)
  ○ Projects
  ○ Productions
  ○ Agents
  ○ Settings
```


---

## Page: Discovery Hub

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  DISCOVER                                              Search: [________]   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TABS: [Showcase Gallery] [Templates] [Community] [Scale Guide]             │
│                                                                             │
├─── SHOWCASE GALLERY (curated examples of what the system produces) ─────────┤
│                                                                             │
│  Filter: [All ▼] [Duration ▼] [Style ▼] [Industry ▼] [Budget Range ▼]      │
│  Sort:   [Trending] [Newest] [Most Liked] [Cheapest] [Highest Quality]      │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                                                                     │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐           │    │
│  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │           │    │
│  │  │          │  │          │  │          │  │          │           │    │
│  │  │ "Neon    │  │ "Product │  │ "5-Min   │  │ "Brand   │           │    │
│  │  │  Dreams" │  │  Launch" │  │  Doc"    │  │  Story"  │           │    │
│  │  │          │  │          │  │          │  │          │           │    │
│  │  │ 15s Hook │  │ 30s UGC  │  │ 5min Doc │  │ 90s Film │           │    │
│  │  │ ~$8      │  │ ~$15     │  │ ~$45     │  │ ~$35     │           │    │
│  │  │ Template A│  │ Template B│  │ Template I│  │ Template E│          │    │
│  │  │ ★★★★★    │  │ ★★★★☆    │  │ ★★★★★    │  │ ★★★★★    │           │    │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘           │    │
│  │                                                                     │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐           │    │
│  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │  │ ▶ ░░░░░  │           │    │
│  │  │          │  │          │  │          │  │          │           │    │
│  │  │ "Fitness │  │ "AI      │  │ "Music   │  │ "Corp    │           │    │
│  │  │  Ad"     │  │  Avatar" │  │  Video"  │  │  Train"  │           │    │
│  │  │          │  │          │  │          │  │          │           │    │
│  │  │ 20s UGC  │  │ 3min Talk│  │ 4min MV  │  │ 12min LMS│           │    │
│  │  │ ~$12     │  │ ~$25     │  │ ~$60     │  │ ~$40     │           │    │
│  │  │ Template B│  │ Template H│  │ Template G│  │ Template F│          │    │
│  │  │ ★★★★☆    │  │ ★★★★★    │  │ ★★★★☆    │  │ ★★★★★    │           │    │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘           │    │
│  │                                                                     │    │
│  │  Showing 8 of 247 showcase items  [Load more...]                    │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  Click any card → Preview + "Use This as Starting Point"                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```



---

## Showcase Card Detail (when user clicks a gallery item)

```text
┌──────────────────────────────────────────────────────────────────┐
│  SHOWCASE: "Neon Dreams"                                  [×]    │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │                                                          │    │
│  │              ▶ VIDEO PLAYER (15 seconds)                  │    │
│  │                                                          │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─── PRODUCTION DETAILS ────────────────────────────────────┐   │
│  │                                                           │   │
│  │  Template: A — Viral Hook                                 │   │
│  │  Duration: 15 seconds                                     │   │
│  │  Aspect: 9:16 (TikTok/Reels)                             │   │
│  │  Style: Cyberpunk, neon, high-energy                      │   │
│  │  Genre: Lifestyle/Fashion                                 │   │
│  │                                                           │   │
│  │  ┌─── SCALE BREAKDOWN ──────────────────────────────┐     │   │
│  │  │  Agents used: 12                                 │     │   │
│  │  │  Shots generated: 4                              │     │   │
│  │  │  Total cost: $8.20                               │     │   │
│  │  │  Production time: 2 minutes 14 seconds           │     │   │
│  │  │  Model: Veo 3.1 (primary), Kling 3.0 (B-roll)   │     │   │
│  │  │  Voice: None (music-only)                        │     │   │
│  │  │  Music: Udio-generated (electronic, 130bpm)      │     │   │
│  │  └──────────────────────────────────────────────────┘     │   │
│  │                                                           │   │
│  │  ┌─── AGENTS INVOLVED ─────────────────────────────┐      │   │
│  │  │  DirectorAgent · PromptEngineerAgent ·           │      │   │
│  │  │  EditorAgent · ComposerAgent · AIQAAgent ·       │      │   │
│  │  │  RetentionOptimizerAgent · TrendIntelAgent ·     │      │   │
│  │  │  CopywriterAgent · SocialStrategistAgent ·       │      │   │
│  │  │  ColoristAgent · SoundMixerAgent · MotionGfx     │      │   │
│  │  └──────────────────────────────────────────────────┘      │   │
│  │                                                           │   │
│  │  ┌─── BRIEF USED ──────────────────────────────────┐      │   │
│  │  │  "15-second hook for fashion brand. Neon city    │      │   │
│  │  │   streets at night, model walking, beat-synced   │      │   │
│  │  │   cuts, trending audio style. Target: Gen Z."    │      │   │
│  │  └──────────────────────────────────────────────────┘      │   │
│  │                                                           │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌─── ACTIONS ───────────────────────────────────────────────┐   │
│  │                                                           │   │
│  │  [★ Use This as Template]  → Creates draft with this      │   │
│  │                               brief pre-filled            │   │
│  │                                                           │   │
│  │  [📋 Copy Brief]  → Copy the brief text to clipboard      │   │
│  │                                                           │   │
│  │  [🔀 Remix]  → Start from this but modify                 │   │
│  │               (changes style/duration/audience)            │   │
│  │                                                           │   │
│  │  [❤️ Save to Inspiration Board]                            │   │
│  │                                                           │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```



---

## Scale Guide Tab (visual comparison of production scales)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  SCALE GUIDE — "What should I build?"                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── PRODUCTION SCALE SPECTRUM ────────────────────────────────────────┐   │
│  │                                                                     │   │
│  │  5s        15s       30s      60s      3min     10min    30min  2hr │   │
│  │  │─────────│─────────│────────│────────│────────│────────│──────│  │   │
│  │                                                                     │   │
│  │  ┌─────┐  ┌─────┐  ┌──────┐  ┌──────┐  ┌──────┐ ┌──────┐ ┌─────┐ │   │
│  │  │MICRO│  │HOOK │  │SHORT │  │MEDIUM│  │LONG  │ │EPISOD│ │FEAT.│ │   │
│  │  │     │  │     │  │      │  │      │  │      │ │      │ │     │ │   │
│  │  │ $2-5│  │$5-15│  │$10-30│  │$20-50│  │$40-80│ │$60+  │ │$150+│ │   │
│  │  │ 1min│  │ 2min│  │ 3min │  │ 5min │  │10min │ │20min │ │ 1hr+│ │   │
│  │  │ 4   │  │ 8-12│  │12-18 │  │18-30 │  │30-50 │ │50-80 │ │ 114 │ │   │
│  │  │agents│  │agents│ │agents│  │agents│  │agents│ │agents│ │agent│ │   │
│  │  └─────┘  └─────┘  └──────┘  └──────┘  └──────┘ └──────┘ └─────┘ │   │
│  │                                                                     │   │
│  │  Click any tier → see examples at that scale                        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─── SCALE COMPARISON TABLE ───────────────────────────────────────────┐   │
│  │                                                                      │   │
│  │  Scale      │Duration│Cost  │Time │Agents│Best For         │Template │   │
│  │  ───────────┼────────┼──────┼─────┼──────┼─────────────────┼─────────│   │
│  │  Micro Clip │ 3-5s   │$2-5  │<1min│ 4-6  │GIF replacement, │ —       │   │
│  │             │        │      │     │      │loop animations  │         │   │
│  │  ───────────┼────────┼──────┼─────┼──────┼─────────────────┼─────────│   │
│  │  Viral Hook │ 7-15s  │$5-15 │1-3m │ 8-12 │TikTok, Reels,   │ A       │   │
│  │             │        │      │     │      │YouTube Shorts   │         │   │
│  │  ───────────┼────────┼──────┼─────┼──────┼─────────────────┼─────────│   │
│  │  Short Ad   │ 15-45s │$10-30│2-5m │12-18 │UGC ads, product │ B       │   │
│  │             │        │      │     │      │demos, testimonial│        │   │
│  │  ───────────┼────────┼──────┼─────┼──────┼─────────────────┼─────────│   │
│  │  Explainer  │ 60-180s│$20-50│3-8m │18-25 │Product explainer,│ C       │   │
│  │             │        │      │     │      │animated tutorial │         │   │
│  │  ───────────┼────────┼──────┼─────┼──────┼─────────────────┼─────────│   │
│  │  Music Video│ 3-5min │$40-80│8-15m│25-35 │Full MV, visual  │ G       │   │
│  │             │        │      │     │      │album, lyric vid │         │   │
│  │  ───────────┼────────┼──────┼─────┼──────┼─────────────────┼─────────│   │
│  │  Short Film │ 3-15min│$50-95│10-25│30-50 │Narrative, brand  │ E       │   │
│  │             │        │      │     │      │film, short doc  │         │   │
│  │  ───────────┼────────┼──────┼─────┼──────┼─────────────────┼─────────│   │
│  │  Training   │ 5-30min│$30-60│8-20m│18-30 │Corporate, LMS,  │ F       │   │
│  │             │        │      │     │      │onboarding       │         │   │
│  │  ───────────┼────────┼──────┼─────┼──────┼─────────────────┼─────────│   │
│  │  Documentary│10-90min│$80+  │30m+ │40-60 │Interview-based, │ I       │   │
│  │             │        │      │     │      │archival, invest.│         │   │
│  │  ───────────┼────────┼──────┼─────┼──────┼─────────────────┼─────────│   │
│  │  Feature    │90min+  │$150+ │1hr+ │ 114  │Full narrative   │ J       │   │
│  │             │        │      │     │      │film, series     │         │   │
│  │  ───────────┴────────┴──────┴─────┴──────┴─────────────────┴─────────│   │
│  │                                                                      │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```



---

## Smart Selection Wizard (AI-guided "What should I build?")

```text
┌──────────────────────────────────────────────────────────────────┐
│  WHAT DO YOU WANT TO MAKE?                                        │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Just describe your idea — we'll recommend the right scale:      │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ "I want a promotional video for my coffee shop's new      │    │
│  │  seasonal drink. It should feel cozy and trendy, for      │    │
│  │  Instagram and TikTok."                                   │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  [Suggest →]                                                     │
│                                                                  │
│  ┌─── AI RECOMMENDATION ────────────────────────────────────┐    │
│  │                                                           │    │
│  │  Based on your description, here are our suggestions:     │    │
│  │                                                           │    │
│  │  ★ RECOMMENDED: Viral Hook (Template A)                    │    │
│  │  ┌────────────────────────────────────────────────────┐   │    │
│  │  │  Duration: 15-30 seconds                           │   │    │
│  │  │  Aspect: 9:16 (vertical, social-first)            │   │    │
│  │  │  Estimated cost: ~$12                              │   │    │
│  │  │  Production time: ~3 minutes                       │   │    │
│  │  │  Why: Short-form social content with trending      │   │    │
│  │  │       hooks gets maximum reach on IG/TikTok.       │   │    │
│  │  │  Example: ▶ [Preview similar showcase]             │   │    │
│  │  │  [★ Use This →]                                    │   │    │
│  │  └────────────────────────────────────────────────────┘   │    │
│  │                                                           │    │
│  │  ALSO CONSIDER:                                            │    │
│  │  ┌────────────────────────────────────────────────────┐   │    │
│  │  │  UGC-Style Ad (Template B) — 30s, ~$18             │   │    │
│  │  │  More authentic feel, testimonial-style.           │   │    │
│  │  │  Good if you want "real person talking" vibe.      │   │    │
│  │  │  [Use This →]                                      │   │    │
│  │  └────────────────────────────────────────────────────┘   │    │
│  │  ┌────────────────────────────────────────────────────┐   │    │
│  │  │  Multi-format Pack — Hook + Ad + Story (3 videos)  │   │    │
│  │  │  15s + 30s + 60s versions from same brief.         │   │    │
│  │  │  ~$35 total. Covers all placements.                │   │    │
│  │  │  [Use This →]                                      │   │    │
│  │  └────────────────────────────────────────────────────┘   │    │
│  │                                                           │    │
│  └───────────────────────────────────────────────────────────┘    │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Community Tab (user-generated showcase feed)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  COMMUNITY GALLERY                              [Submit Yours] [Following]   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Sort: [Trending] [New] [Top This Week] [Staff Picks]                       │
│  Filter: [All Types ▼] [All Durations ▼] [All Styles ▼]                    │
│                                                                             │
│  ┌─── MASONRY GRID (Pinterest-style) ──────────────────────────────────┐   │
│  │                                                                     │   │
│  │  ┌──────────┐  ┌────────────────┐  ┌──────────┐                    │   │
│  │  │ ▶        │  │ ▶              │  │ ▶        │                    │   │
│  │  │          │  │                │  │          │                    │   │
│  │  │          │  │   (tall 9:16)  │  │          │                    │   │
│  │  │ 16:9     │  │                │  │ 1:1      │                    │   │
│  │  │          │  │                │  │          │                    │   │
│  │  │"Midnight │  │                │  │"Product  │                    │   │
│  │  │ Cafe"    │  │ "Dance        │  │ Launch"  │                    │   │
│  │  │ by @luca │  │  Challenge"   │  │ by @brand│                    │   │
│  │  │ 45s Film │  │  by @maya     │  │ 20s UGC  │                    │   │
│  │  │ ❤️ 342   │  │  15s Hook     │  │ ❤️ 128   │                    │   │
│  │  │ 💬 28    │  │  ❤️ 1.2k      │  │ 💬 15    │                    │   │
│  │  └──────────┘  │  💬 89        │  └──────────┘                    │   │
│  │                 └────────────────┘                                  │   │
│  │  ┌────────────────┐  ┌──────────┐  ┌──────────────┐               │   │
│  │  │ ▶              │  │ ▶        │  │ ▶            │               │   │
│  │  │                │  │          │  │              │               │   │
│  │  │  "Training:    │  │          │  │ "Music Video │               │   │
│  │  │   Safety"      │  │ "AI      │  │  Remix"      │               │   │
│  │  │  by @corp_co   │  │  Avatar" │  │  by @beats   │               │   │
│  │  │  8min Training │  │  by @sam │  │  3min MV     │               │   │
│  │  │  ❤️ 56         │  │  2min    │  │  ❤️ 567      │               │   │
│  │  └────────────────┘  │  ❤️ 234  │  └──────────────┘               │   │
│  │                      └──────────┘                                   │   │
│  │                                                                     │   │
│  │  [Load more...]                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Click any → Preview + "Remix This" / "Use Same Settings"                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Template Carousel (visual template browser)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  TEMPLATES                                                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── CAROUSEL: PRODUCTION TYPES ──────────────────── [← →] ──────────┐   │
│  │                                                                     │   │
│  │  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐           │   │
│  │  │               │  │               │  │               │           │   │
│  │  │   ▶ Preview   │  │   ▶ Preview   │  │   ▶ Preview   │           │   │
│  │  │               │  │               │  │               │           │   │
│  │  │  ┌─────────┐  │  │  ┌─────────┐  │  │  ┌─────────┐  │           │   │
│  │  │  │ A       │  │  │  │ B       │  │  │  │ C       │  │           │   │
│  │  │  │ VIRAL   │  │  │  │ UGC     │  │  │  │ ANIMATED│  │           │   │
│  │  │  │ HOOK    │  │  │  │ AD      │  │  │  │ EXPLAIN │  │           │   │
│  │  │  └─────────┘  │  │  └─────────┘  │  │  └─────────┘  │           │   │
│  │  │               │  │               │  │               │           │   │
│  │  │  7-60s        │  │  15-45s       │  │  60-180s      │           │   │
│  │  │  9:16 vertical│  │  9:16 vertical│  │  16:9 wide    │           │   │
│  │  │  $5-15        │  │  $10-30       │  │  $20-50       │           │   │
│  │  │  ~2 min       │  │  ~4 min       │  │  ~7 min       │           │   │
│  │  │               │  │               │  │               │           │   │
│  │  │  Best for:    │  │  Best for:    │  │  Best for:    │           │   │
│  │  │  TikTok,Reels │  │  Paid social  │  │  Website,     │           │   │
│  │  │  YouTube Short│  │  Meta/TikTok  │  │  YouTube      │           │   │
│  │  │               │  │  ads          │  │  SaaS demos   │           │   │
│  │  │  [Use This]   │  │  [Use This]   │  │  [Use This]   │           │   │
│  │  │  [See 5 examples]│ │  [See 8 examples]│ │  [See 4 examples]│    │   │
│  │  └───────────────┘  └───────────────┘  └───────────────┘           │   │
│  │                                                                     │   │
│  │  ... [D Birthday] [E Film] [F Training] [G Music Video] [H Avatar] │   │
│  │      [I Documentary] [J Feature Film]                               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## How Scale Detection Works (Backend Logic)

When user describes their idea (or selects a showcase), the system infers scale:

```python
# Scale inference from user input (runs as cheap LLM call)

async def infer_production_scale(user_input: str) -> ScaleRecommendation:
    """Called when user types a description in Smart Selection Wizard."""
    
    response = await llm.classify(
        system="""You are a video production consultant. 
        Given a user's description of what they want to create,
        recommend the best production scale and template.
        
        Consider: platform (social=short, web=medium, cinema=long),
        content type (ad=15-60s, explainer=1-3min, narrative=3min+),
        complexity (talking head=simple, VFX=complex, multi-scene=long),
        audience expectations, and budget sensitivity.""",
        
        user_input=user_input,
        
        output_schema={
            "recommended_template": "A-J",
            "duration_range": {"min_seconds": int, "max_seconds": int},
            "estimated_cost": {"low": float, "mid": float, "high": float},
            "estimated_time_minutes": int,
            "agents_needed": int,
            "aspect_ratio": "16:9 | 9:16 | 1:1",
            "reasoning": str,
            "alternatives": [{
                "template": str,
                "why": str,
                "tradeoff": str
            }]
        }
    )
    
    return ScaleRecommendation(**response)
```

---

## Inspiration Board (per-project)

Users can save showcase items for reference before building:

```text
┌──────────────────────────────────────────────────────────────────┐
│  PROJECT: "Coffee Shop Campaign" > INSPIRATION BOARD              │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Saved from Discover:                                            │
│                                                                  │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────────────┐    │
│  │ ▶ "Neon │  │ ▶ "Cozy │  │ ▶ "Latte│  │  + Browse More  │    │
│  │  Dreams" │  │  Vibes" │  │  Art"   │  │  from Discover  │    │
│  │  15s     │  │  30s    │  │  20s    │  │                 │    │
│  │  Style ★ │  │  Tone ★ │  │  Edit ★ │  │                 │    │
│  └─────────┘  └─────────┘  └─────────┘  └─────────────────┘    │
│                                                                  │
│  Notes: "I like the warm tones from 'Cozy Vibes' but the        │
│         fast pacing from 'Neon Dreams'. Latte Art has the        │
│         right product-focus framing."                            │
│                                                                  │
│  [Create Production from These References →]                     │
│  (Auto-fills brief with style cues from saved items)             │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Updated User Journey (with Discovery)

```text
BEFORE (confusing):
  Create Project → "Pick template A-J" → confusion → abandon

AFTER (guided):
  Create Project → Browse Discover Hub → See real examples →
  → "That one! I want something like THAT" →
  → Click [Use as Template] → Brief pre-filled with right scale →
  → Adjust details → Launch

OR (AI-guided):
  Create Project → Describe idea in plain English →
  → AI recommends: "You need a 15s Hook, here's why" →
  → Shows 3 examples at that scale →
  → User picks → Brief pre-filled → Launch

OR (community-inspired):
  Browse Community Gallery → See trending content →
  → "I want to make something like THIS" →
  → Click [Remix] → Fork their brief + adjust → Launch
```

---

## Summary: How System Knows Production Scale

| Method | How It Works | User Effort |
|--------|-------------|-------------|
| **Template Carousel** | User browses visual cards with duration/cost/examples | Low — visual browsing |
| **Scale Guide** | Side-by-side comparison table of all production tiers | Low — read and pick |
| **Showcase Gallery** | Real produced examples with full metadata visible | Zero — just watch |
| **Smart Wizard** | User describes in English → AI recommends scale | Minimal — type a sentence |
| **Community Feed** | Browse what others have made → fork/remix | Zero — just browse |
| **Inspiration Board** | Save references → system infers style/scale from collection | Organic — save what you like |
| **From Showcase** | Click "Use This as Template" → exact settings pre-filled | One click |

All methods lead to the same destination: **a Draft Production with the correct template, duration, aspect ratio, and budget pre-filled** — ready for the user to customize and launch.
