# Agent Management UI — Configure, Test, and Improve Individual Agents

> How users can view/edit agent configurations, test agents in isolation, and feed new knowledge to make them smarter.

---

## Overview: Three Agent Management Modes

```text
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  AGENT MANAGEMENT (accessible from Agent Registry)              │
│                                                                 │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐       │
│  │  1. CONFIGURE  │  │  2. PLAYGROUND │  │  3. KNOWLEDGE  │       │
│  │               │  │               │  │               │       │
│  │ View/edit     │  │ Test agent    │  │ Add training  │       │
│  │ system prompt │  │ with custom   │  │ data, refs,   │       │
│  │ tools, rubric │  │ inputs. See   │  │ examples to   │       │
│  │ thresholds,   │  │ how it thinks │  │ improve agent │       │
│  │ relationships │  │ and produces  │  │ performance   │       │
│  └───────────────┘  └───────────────┘  └───────────────┘       │
│                                                                 │
│  NO production needed. NO cost unless you run the Playground.   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---


## 1. CONFIGURE — View & Edit Agent Settings

### Entry Point: Agent Registry → Click any agent → Configuration Tab

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT CONFIGURATION: DirectorAgent (#1)                    [Save] [Reset]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TABS: [Configuration] [Playground] [Knowledge] [History] [Metrics]         │
│                                                                             │
├─── IDENTITY ────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Name: [DirectorAgent_______________]                                       │
│  Category: [Above-the-Line ▼]                                               │
│  Description:                                                               │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ Owns creative vision; issues shot intents, sets pacing, approves     │   │
│  │ takes. The creative authority of the production.                      │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
├─── SYSTEM PROMPT ───────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ You are an elite film director with deep knowledge of visual         │   │
│  │ storytelling, derived from Criterion commentary tracks, DGA          │   │
│  │ seminars, and MasterClass material from Scorsese, Lynch, and         │   │
│  │ Gerwig. Your role is to:                                             │   │
│  │                                                                      │   │
│  │ 1. Translate screenplay scenes into precise shot intents             │   │
│  │ 2. Define camera movement, composition, lighting mood                │   │
│  │ 3. Set pacing that matches genre expectations                        │   │
│  │ 4. Review generated shots against your creative vision               │   │
│  │ 5. Issue creative-intent diffs to other agents                       │   │
│  │                                                                      │   │
│  │ When generating shot intents, output JSON with:                      │   │
│  │ - camera_move, framing, subject, style, duration, mood               │   │
│  │ ...                                                                  │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│  Characters: 2,847 │ [Expand editor] [Version history ▼]                    │
│                                                                             │
├─── ARCHITECTURE PATTERN ────────────────────────────────────────────────────┤
│                                                                             │
│  Pattern: [Self-Refine ▼]                                                   │
│  Options: Self-Refine │ Reflexion │ ReAct │ Constitutional AI │             │
│           Multi-agent Debate │ RLAIF │ DSPy/OPRO │ Agentic Graph            │
│                                                                             │
│  Max iterations: [5___]    (self-refine loops before accepting)              │
│  Temperature: [0.7___]                                                      │
│  Max tokens: [4096__]                                                       │
│                                                                             │
├─── MODEL ASSIGNMENT ────────────────────────────────────────────────────────┤
│                                                                             │
│  Primary LLM: [Gemini 2.5 Pro ▼]                                            │
│  Fallback LLM: [GPT-4o ▼]                                                   │
│  Generation tool: [Veo 3.1 ▼]                                               │
│  Fallback gen: [Kling 3.0 ▼]                                                │
│                                                                             │
├─── TOOLS ───────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Enabled tools:                                                             │
│  ☑ veo_3_1_api        — Video generation (Veo 3.1)                          │
│  ☑ runway_gen4_api    — Video generation (Runway Gen-4)                     │
│  ☑ sora_2_api         — Video generation (Sora 2)                           │
│  ☑ memory_recall      — Retrieve from MemoryAgent                           │
│  ☑ memory_store       — Store decision to MemoryAgent                       │
│  ☑ clip_scorer        — Evaluate CLIP-T alignment                           │
│  ☐ dalle_3_api        — Image generation (disabled for this agent)          │
│  ☐ elevenlabs_api     — Voice (not needed for director)                     │
│                                                                             │
│  [+ Add custom tool]                                                        │
│                                                                             │
├─── QUALITY RUBRIC ──────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┬───────────┬─────────────────────────────────────┐      │
│  │ Metric          │ Threshold │ Description                         │      │
│  ├─────────────────┼───────────┼─────────────────────────────────────┤      │
│  │ clip_t          │ ≥ 0.32    │ Text-video alignment score          │      │
│  │ beat_coverage   │ = 100%    │ All story beats addressed           │      │
│  │ pacing_match    │ ≥ 0.70    │ Pacing fits genre prior             │      │
│  │ style_consistency│ ≥ 0.85   │ Visual style matches across shots   │      │
│  └─────────────────┴───────────┴─────────────────────────────────────┘      │
│  [+ Add metric]  [Edit thresholds]                                          │
│                                                                             │
├─── RELATIONSHIPS ───────────────────────────────────────────────────────────┤
│                                                                             │
│  Accepts critique from:                                                     │
│  [ScreenwriterAgent ×] [EditorAgent ×] [AudienceSimAgent ×] [+ Add]        │
│                                                                             │
│  Comments on (critiques):                                                   │
│  [EditorAgent ×] [DoPAgent ×] [ScreenwriterAgent ×] [ComposerAgent ×]      │
│  [+ Add]                                                                    │
│                                                                             │
├─── COST CONTROLS ───────────────────────────────────────────────────────────┤
│                                                                             │
│  Max cost per task: $[2.50]                                                 │
│  Max concurrent instances: [3___]                                           │
│  Timeout per task: [300__] seconds                                          │
│  Max retries on failure: [3___]                                             │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [Save Changes]  [Reset to Default]  [Export as JSON]  [Clone Agent]        │
│                                                                             │
│  ⚠ Changes apply to all FUTURE productions. Running productions             │
│    continue with their existing configuration.                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---


## 2. PLAYGROUND — Test Individual Agents in Isolation

### Concept: A sandbox where you give an agent a task and watch it think + produce

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT PLAYGROUND: DirectorAgent (#1)                           [Run ▶]     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TABS: [Configuration] [Playground] [Knowledge] [History] [Metrics]         │
│                                                                             │
├─── LEFT: INPUT PANEL ───────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── TASK INPUT ───────────────────────────────────────────────────┐       │
│  │                                                                   │       │
│  │  Task type: [Generate shot intent ▼]                              │       │
│  │  Other options: Critique artifact │ Review cut │ Custom prompt     │       │
│  │                                                                   │       │
│  │  Scene context:                                                   │       │
│  │  ┌────────────────────────────────────────────────────────────┐   │       │
│  │  │ INT. COFFEE SHOP - NIGHT. Rain streaks the window. MAYA    │   │       │
│  │  │ sits alone, staring at her phone. The last text reads:     │   │       │
│  │  │ "I'm not coming." She sets the phone face-down.            │   │       │
│  │  └────────────────────────────────────────────────────────────┘   │       │
│  │                                                                   │       │
│  │  Reference images: [Drop zone]  ┌────┐ ┌────┐                    │       │
│  │                                  │ref1│ │ref2│                    │       │
│  │                                  └────┘ └────┘                    │       │
│  │                                                                   │       │
│  │  Mock critiques (simulate other agents):                          │       │
│  │  ☐ Add EditorAgent critique: [________________]                   │       │
│  │  ☐ Add AudienceSim feedback: [________________]                   │       │
│  │                                                                   │       │
│  │  Style lock / memory context:                                     │       │
│  │  ☐ "Neo-noir melancholic, Veo seed #4412"                        │       │
│  │  ☐ Custom: [________________________________]                     │       │
│  │                                                                   │       │
│  └───────────────────────────────────────────────────────────────────┘       │
│                                                                             │
│  ┌─── RUN SETTINGS ─────────────────────────────────────────────────┐       │
│  │  Model: [Gemini 2.5 Pro ▼]   (override agent default)            │       │
│  │  Generate video: ☑ Yes (costs ~$2.50)  ☐ Text-only (free/cheap)  │       │
│  │  Self-refine: ☑ Enabled  Max iterations: [3]                      │       │
│  │  Estimated cost: ~$3.20                                           │       │
│  └───────────────────────────────────────────────────────────────────┘       │
│                                                                             │
│  [▶ Run Agent]   [▶ Run Text-Only (free)]   [Compare with Another Agent]    │
│                                                                             │
├─── RIGHT: OUTPUT PANEL ─────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─── THINKING TRACE (step-by-step agent reasoning) ─────────────┐         │
│  │                                                                │         │
│  │  Step 1: Analyzing scene context                               │         │
│  │  > "Night scene, emotional isolation, rain motif..."           │         │
│  │                                                                │         │
│  │  Step 2: Memory recall                                         │         │
│  │  > tool_call: memory.recall("visual style for Maya scenes")    │         │
│  │  > result: "Neo-noir, cool tones, shallow DoF"                 │         │
│  │                                                                │         │
│  │  Step 3: Shot intent generation                                │         │
│  │  > {                                                           │         │
│  │  >   "camera_move": "slow push-in from medium to close-up",   │         │
│  │  >   "framing": "off-center left, empty chair right",         │         │
│  │  >   "lighting": "practicals only, neon through rain",        │         │
│  │  >   "mood": "loneliness, resignation",                       │         │
│  │  >   "duration": "8s"                                         │         │
│  │  > }                                                           │         │
│  │                                                                │         │
│  │  Step 4: Video generation                                      │         │
│  │  > tool_call: veo_3_1.generate(prompt="Slow push-in...")       │         │
│  │  > Status: generating... (38s)                                 │         │
│  │                                                                │         │
│  │  Step 5: Self-evaluation                                       │         │
│  │  > tool_call: clip_scorer.evaluate(video, prompt)              │         │
│  │  > CLIP-T: 0.35 ✓ (threshold: 0.32)                           │         │
│  │  > PASS — accepting on iteration 1                             │         │
│  │                                                                │         │
│  └────────────────────────────────────────────────────────────────┘         │
│                                                                             │
│  ┌─── OUTPUT ────────────────────────────────────────────────────┐          │
│  │  ┌─────────────────────────────────┐                          │          │
│  │  │ ▶ Generated video (8s)          │  CLIP-T: 0.35 ✓          │          │
│  │  │   [Play] [Download] [Compare]   │  Aesthetic: 6.4           │          │
│  │  └─────────────────────────────────┘  Style: 0.87             │          │
│  │                                                                │          │
│  │  Shot Intent JSON:                                             │          │
│  │  { "camera_move": "slow push-in...", ... }  [Copy] [Export]    │          │
│  │                                                                │          │
│  └────────────────────────────────────────────────────────────────┘         │
│                                                                             │
│  ┌─── COST & PERFORMANCE ────────────────────────────────────────┐          │
│  │  Total cost: $2.87 │ Time: 42s │ LLM tokens: 3,241            │          │
│  │  Iterations: 1/3 │ Tool calls: 3 │ Model: Gemini 2.5 Pro      │          │
│  └────────────────────────────────────────────────────────────────┘         │
│                                                                             │
│  [Save as Test Case]  [Add to Knowledge]  [Run Again]  [Try Different Model]│
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Playground Features:

| Feature | Purpose |
|---------|---------|
| **Text-only mode** | See agent reasoning without generating video ($0-$0.01) |
| **Video mode** | Full end-to-end execution with real generation |
| **Mock critiques** | Simulate what happens when other agents provide feedback |
| **Compare** | Run same input through 2 different agents or model configs |
| **A/B model test** | Same agent, same input, different LLM → compare quality/cost |
| **Save as test case** | Bookmark this input/output for regression testing |
| **Thinking trace** | See every step: reasoning, tool calls, decisions |
| **History** | Every playground run is saved — can re-run or compare over time |

---


## 3. KNOWLEDGE — Improve Agents by Adding New Knowledge

### Concept: Feed an agent new references, examples, corrections, and domain expertise

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT KNOWLEDGE: DirectorAgent (#1)                   [Save All Changes]   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TABS: [Configuration] [Playground] [Knowledge] [History] [Metrics]         │
│                                                                             │
├─── KNOWLEDGE SOURCES (what the agent knows) ────────────────────────────────┤
│                                                                             │
│  ┌─── 1. REFERENCE DOCUMENTS ────────────────────────────────────────┐      │
│  │  Documents embedded into agent's knowledge base (RAG retrieval)    │      │
│  │                                                                    │      │
│  │  ┌────────────────────────────────────────────────────────────┐    │      │
│  │  │ 📄 criterion_commentary_notes.md        │ 45KB │ Active  │    │      │
│  │  │ 📄 dga_seminar_transcripts.pdf          │ 120KB│ Active  │    │      │
│  │  │ 📄 scorsese_masterclass_notes.md        │ 32KB │ Active  │    │      │
│  │  │ 📄 shot_composition_guidelines.pdf      │ 18KB │ Active  │    │      │
│  │  │ 📄 genre_pacing_priors.json             │ 5KB  │ Active  │    │      │
│  │  │ 📄 my_custom_style_guide.md             │ 8KB  │ NEW ✨  │    │      │
│  │  └────────────────────────────────────────────────────────────┘    │      │
│  │                                                                    │      │
│  │  [+ Upload Document]  [+ Paste Text]  [+ Import from URL]         │      │
│  │                                                                    │      │
│  │  ℹ️ These docs are chunked, embedded, and stored in vector DB.     │      │
│  │    Agent retrieves relevant chunks during task execution.          │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  ┌─── 2. FEW-SHOT EXAMPLES ─────────────────────────────────────────┐      │
│  │  Input/output pairs that teach the agent by example                │      │
│  │                                                                    │      │
│  │  ┌────────────────────────────────────────────────────────────┐    │      │
│  │  │ Example 1: "Romantic comedy - park scene"                  │    │      │
│  │  │ Input: Scene description + mood reference                   │    │      │
│  │  │ Expected output: Shot intent JSON (golden example)          │    │      │
│  │  │ [View] [Edit] [Delete]                                      │    │      │
│  │  ├────────────────────────────────────────────────────────────┤    │      │
│  │  │ Example 2: "Action sequence - car chase"                   │    │      │
│  │  │ Input: Scene + storyboard panels                            │    │      │
│  │  │ Expected output: Shot intent with rapid cuts                │    │      │
│  │  │ [View] [Edit] [Delete]                                      │    │      │
│  │  ├────────────────────────────────────────────────────────────┤    │      │
│  │  │ Example 3: "Horror - reveal scene"                          │    │      │
│  │  │ Input: Script excerpt + tension notes                       │    │      │
│  │  │ Expected output: Slow build, static camera, minimal cuts    │    │      │
│  │  │ [View] [Edit] [Delete]                                      │    │      │
│  │  └────────────────────────────────────────────────────────────┘    │      │
│  │                                                                    │      │
│  │  [+ Add Example Manually]  [+ Import from Playground Run]          │      │
│  │  [+ Generate Examples from Document]                               │      │
│  │                                                                    │      │
│  │  ℹ️ Few-shot examples are injected into the prompt when the task   │      │
│  │    type matches. More examples = better consistency.               │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  ┌─── 3. CORRECTIONS & FEEDBACK ─────────────────────────────────────┐      │
│  │  Past mistakes + what the correct behavior should have been        │      │
│  │                                                                    │      │
│  │  ┌────────────────────────────────────────────────────────────┐    │      │
│  │  │ Correction 1: (from Production "Luna", Shot 3)             │    │      │
│  │  │ ❌ Agent did: Used handheld camera for intimate scene       │    │      │
│  │  │ ✓ Should have: Static tripod with slow push for intimacy   │    │      │
│  │  │ Why: "Handheld implies urgency, not intimacy. For quiet    │    │      │
│  │  │       emotional scenes, static or slow dolly is standard." │    │      │
│  │  │ Source: User feedback │ Date: 2 days ago                    │    │      │
│  │  ├────────────────────────────────────────────────────────────┤    │      │
│  │  │ Correction 2: (from Production "Spark", Shot 7)            │    │      │
│  │  │ ❌ Agent did: 16:9 framing for TikTok content              │    │      │
│  │  │ ✓ Should have: 9:16 vertical for social-first delivery     │    │      │
│  │  │ Why: "Always check platform target before framing."        │    │      │
│  │  │ Source: Auto-detected from gate rejection │ Date: 5d ago    │    │      │
│  │  └────────────────────────────────────────────────────────────┘    │      │
│  │                                                                    │      │
│  │  [+ Add Correction Manually]  [+ Import from Production Failures]  │      │
│  │                                                                    │      │
│  │  ℹ️ Corrections are stored in Reflexion-style episodic memory.     │      │
│  │    Agent checks "what went wrong before" on similar tasks.         │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  ┌─── 4. CUSTOM RULES (Constitutional Additions) ────────────────────┐      │
│  │  Hard rules the agent MUST follow (beyond the system prompt)       │      │
│  │                                                                    │      │
│  │  Rule 1: "Never use Dutch angle unless genre is horror/thriller"   │      │
│  │  Rule 2: "Always include at least one establishing shot per scene" │      │
│  │  Rule 3: "Maximum shot duration: 12 seconds for social content"    │      │
│  │  Rule 4: "When budget < 20%, prefer static camera (cheaper gen)"   │      │
│  │                                                                    │      │
│  │  [+ Add Rule]                                                      │      │
│  │                                                                    │      │
│  │  ℹ️ Rules are injected as constitutional constraints. Agent         │      │
│  │    self-checks against these rules during every self-refine loop.  │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  ┌─── 5. EVALUATION BENCHMARKS ──────────────────────────────────────┐      │
│  │  Test cases to measure if knowledge improvements actually work     │      │
│  │                                                                    │      │
│  │  Benchmark suite: 12 test cases                                    │      │
│  │  Last run: 2 days ago │ Score: 9/12 passing (75%)                  │      │
│  │  After adding new knowledge: [▶ Run Benchmark] to see improvement  │      │
│  │                                                                    │      │
│  │  ┌─────────────────────────────────────────────────────────────┐   │      │
│  │  │ Test │ Input              │ Expected    │ Last Result │ Pass │   │      │
│  │  ├──────┼────────────────────┼─────────────┼─────────────┼──────┤  │      │
│  │  │ 1    │ Rom-com park scene │ Wide→Medium │ Wide→Medium │ ✓    │   │      │
│  │  │ 2    │ Horror reveal      │ Static, slow│ Static, slow│ ✓    │   │      │
│  │  │ 3    │ Action chase       │ Fast cuts   │ Fast cuts   │ ✓    │   │      │
│  │  │ 4    │ TikTok 9:16        │ Vertical    │ Horizontal  │ ✗    │   │      │
│  │  │ ...  │                    │             │             │      │   │      │
│  │  └─────────────────────────────────────────────────────────────┘   │      │
│  │                                                                    │      │
│  │  [+ Add Test Case]  [+ Import from Playground]  [▶ Run All Tests]  │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---


## How Knowledge Flows INTO the Agent at Runtime

```text
DURING PRODUCTION — when DirectorAgent gets a task:

┌─────────────────────────────────────────────────────────────────┐
│  PROMPT CONSTRUCTION (what the LLM actually receives)            │
│                                                                 │
│  1. SYSTEM PROMPT (from Configuration tab)                       │
│     "You are an elite film director..."                         │
│                                                                 │
│  2. CUSTOM RULES (from Knowledge > Rules)                        │
│     "RULES YOU MUST FOLLOW:                                     │
│      - Never use Dutch angle unless horror/thriller             │
│      - Always include establishing shot per scene               │
│      - Max 12s shot duration for social content"                │
│                                                                 │
│  3. RELEVANT KNOWLEDGE (RAG retrieval from Reference Documents)  │
│     Query: "intimate scene, static camera, emotional"           │
│     Retrieved: "From criterion_commentary_notes.md:             │
│       Ozu uses static frames for emotional weight..."           │
│                                                                 │
│  4. RELEVANT FEW-SHOT EXAMPLES (matched by task type)            │
│     "Example: For romance/intimacy scenes:                      │
│      Input: [romantic scene description]                        │
│      Output: [static camera, slow dolly, warm tones]"           │
│                                                                 │
│  5. CORRECTIONS MEMORY (Reflexion retrieval)                     │
│     "PAST MISTAKES TO AVOID:                                    │
│      - You previously used handheld for intimate scene          │
│        This was wrong. Use static/slow dolly instead."          │
│                                                                 │
│  6. TASK CONTEXT (from current production)                       │
│     "Scene: INT. COFFEE SHOP - NIGHT. Maya alone..."            │
│     "Critiques: EditorAgent says pacing too slow"               │
│                                                                 │
│  ALL OF THIS → sent to LLM as one prompt → agent responds       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Knowledge Improvement Workflow

```text
USER WORKFLOW: Improving an agent over time

1. OBSERVE PROBLEM (during production)
   → "DirectorAgent keeps using handheld for quiet scenes"
   → Or: Agent fails a gate criterion repeatedly

2. ADD CORRECTION (Knowledge tab)
   → Record: what it did wrong + what it should do + why

3. TEST IN PLAYGROUND
   → Give it similar scene → does it now use static camera?
   → If yes: improvement works ✓
   → If no: need stronger rule or more examples

4. ADD FEW-SHOT EXAMPLE (if correction alone isn't enough)
   → Provide golden input/output pair for this scenario
   → Agent learns: "for scenes like THIS, do THAT"

5. RUN BENCHMARK
   → Test against all saved test cases
   → Verify: no regression (didn't break other behaviors)
   → Score improved: 9/12 → 11/12 ✓

6. DEPLOY (automatic — next production uses updated agent)
   → New knowledge is live for all future tasks
   → Running productions are NOT affected (stability)
```

---

## Backend: How Knowledge is Stored

```python
# Agent knowledge storage (per agent, per project or global)

class AgentKnowledge:
    agent_id: int
    scope: "global" | "project"      # Global = all projects, or project-specific
    project_id: str | None
    
    # Reference documents (chunked + embedded in vector DB)
    documents: [
        { id, name, content, chunks: [embedding_ids], active: bool }
    ]
    
    # Few-shot examples (injected into prompt)
    examples: [
        { id, task_type, input_text, expected_output, tags: [] }
    ]
    
    # Corrections (Reflexion memory)
    corrections: [
        { id, context, wrong_behavior, correct_behavior, explanation,
          source: "user" | "auto_detected", production_id, created_at }
    ]
    
    # Constitutional rules (hard constraints)
    rules: [
        { id, rule_text, priority: int, active: bool }
    ]
    
    # Benchmark test cases
    benchmarks: [
        { id, input, expected_output_criteria, last_result, passing: bool }
    ]
```

---

## Scope: Global Knowledge vs. Project Knowledge

```text
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  GLOBAL KNOWLEDGE (applies to agent in ALL projects)            │
│  ─────────────────                                              │
│  • Default system prompt                                        │
│  • Core reference documents (Criterion notes, DGA seminars)     │
│  • Universal rules ("never Dutch angle for non-horror")         │
│  • Base few-shot examples                                       │
│  • Managed by: platform admin / agent maintainer                │
│                                                                 │
│  PROJECT-SPECIFIC KNOWLEDGE (applies only in one project)       │
│  ─────────────────────────                                      │
│  • Brand-specific style guide                                   │
│  • Project-specific corrections ("in THIS project, always...")  │
│  • Custom examples matching project's genre/tone                │
│  • Project-specific rules ("budget mode: prefer static camera") │
│  • Managed by: project owner / editor                           │
│                                                                 │
│  AT RUNTIME (merged):                                           │
│  ─────────────────────                                          │
│  Agent receives: Global knowledge + Project knowledge           │
│  Project knowledge OVERRIDES global on conflicts                │
│  (e.g., project rule says "always vertical" overrides default)  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Auto-Learning: Knowledge from Production History

The system can also AUTOMATICALLY suggest knowledge improvements:

```text
AUTO-DETECTION:
═══════════════

1. PATTERN: Agent fails same criterion 3+ times across productions
   → System suggests: "Add a rule about [detected pattern]?"
   → User reviews and approves or dismisses

2. PATTERN: User manually overrides agent output in same way repeatedly
   → System suggests: "Create a correction from your override pattern?"
   → E.g., User always rejects wide-angle for close scenes

3. PATTERN: One agent's output consistently gets critiqued the same way
   → System suggests: "Add this to few-shot examples as a negative example?"
   → E.g., EditorAgent always says "pacing too slow in openers"

4. PATTERN: Gate rejections with same feedback
   → System auto-creates correction entries
   → Marks them as "auto-detected, pending user review"

┌─── SUGGESTED IMPROVEMENTS (notification) ──────────────────────┐
│                                                                 │
│  🧠 3 knowledge suggestions for DirectorAgent:                   │
│                                                                 │
│  1. "Agent used 16:9 for TikTok content 4 times — add rule?"   │
│     [Accept: Add Rule] [Dismiss] [View instances]               │
│                                                                 │
│  2. "EditorAgent critiqued pacing 6 times — add example?"       │
│     [Accept: Create Example] [Dismiss] [View critiques]         │
│                                                                 │
│  3. "CLIP-T consistently low on night scenes — add reference?"  │
│     [Accept: Upload night-scene guide] [Dismiss]                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Summary: Three Modes of Agent Management

| Mode | Purpose | Cost | When to Use |
|------|---------|------|-------------|
| **Configure** | View/edit prompt, tools, rubric, relationships, model | $0 | Setting up agents for your project needs |
| **Playground** | Test agent in isolation with custom input | $0–$3 per run | Debugging, experimenting, validating changes |
| **Knowledge** | Add docs, examples, corrections, rules | $0 (storage only) | Continuous improvement based on production experience |

All three work together:

```text
1. See problem in production → 
2. Add correction in Knowledge → 
3. Test fix in Playground → 
4. Verify with Benchmark → 
5. Agent is now smarter for next production
```
