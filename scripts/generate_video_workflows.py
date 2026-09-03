"""Generate scale- and template-specific video BPM workflow SVGs.

Source of truth: spec/production_scale_framework.md
Visual reference: ui/public/svg/video.workflow.svg
"""

from __future__ import annotations

import html
import json
import textwrap
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "ui" / "public" / "svg"
AGENTS_DIR = ROOT / "agents"
WIDTH = 3200
HEIGHT = 5700
PHASE_Y = (1040, 1630, 2220, 2810, 3400, 3990, 4580)
PHASE_HEIGHT = 560


def phase(name, work, agents, control, gate, output, feedback, *, parallel=False, feedback_kind="feedback"):
    return {
        "name": name,
        "work": work,
        "agents": agents,
        "control": control,
        "gate": gate,
        "output": output,
        "feedback": feedback,
        "parallel": parallel,
        "feedback_kind": feedback_kind,
    }


def diagram(kind, code, title, primary, purpose, use_when, dna, basis, quality, stats, phases):
    slug = f"video-{kind}-{code.lower()}-workflow"
    return {
        "kind": kind,
        "code": code.upper(),
        "slug": slug,
        "filename": f"video.{kind}.{code.lower()}.workflow.svg",
        "title": title,
        "primary": primary,
        "purpose": purpose,
        "use_when": use_when,
        "dna": dna,
        "basis": basis,
        "quality": quality,
        "stats": stats,
        "phases": phases,
    }


TEMPLATES = [
    diagram(
        "template", "a", "Viral Hook", "Primary scales S1–S2",
        "Turn a trend, KPI and CTA into a rapid short-form social hook with minimal branching.",
        "Social spike, meme, viral hook, single-SKU promo, proof of concept or DNA UAT.",
        "wf_video_arch_a_viral_hook_v1.dna.json",
        "Explicit S1 flow with the shared seven-phase skeleton; S2 adds a second delivery branch.",
        "L1 required; light L2 at S1; brand/compliance review and L2 ≥90 when promoted to S2.",
        ["Template A", "S1–S2", "1–2 outlets", "fast / low risk"],
        [
            phase("Greenlight", ["Capture KPI, audience, hook and CTA.", "Select S1 or S2 before the archetype.", "Confirm light budget and rights envelope."], ["video.planner", "video.producer", "video.finance", "video.compliance"], ["Freeze brief scope and scale profile.", "Reject budget, rights or feasibility drift."], "G0 · GREENLIGHT", "Approved brief · KPI · budget · rights-risk · scale", "Revise scope, rights or hook before planning."),
            phase("Pre-production", ["Trend scan and divergent hook concepts.", "Write optional short VO/script and CTA.", "Set aspect, duration, caption and outlet specs."], ["video.trendintelligence", "video.copywriter", "video.screenwriter", "video.socialmediastrategist"], ["L1 validates brief, duration and platform spec.", "Keep a single primary creative path at S1."], "G1 · L1 SPEC", "HookConcept · short script · platform specification", "Return failed concept or script only."),
            phase("Production", ["Convert approved hook into generation intents.", "Director checks intent and visual emphasis.", "AIQA inspects identity, artifacts and framing."], ["video.promptengineer", "video.director", "video.aiqaconsistency", "video.router"], ["Host allow-list controls any media adapter.", "Targeted rerender preserves accepted work."], "G2 · CRAFT QC", "Approved takes · prompt evidence · render telemetry", "Rerender only failed take or prompt."),
            phase("Post-production", ["Assemble one concise timeline.", "Add captions and accessibility treatment.", "Prepare platform-safe crop and metadata."], ["video.editor", "video.accessibilityoptimizer", "video.motiongraphics", "video.colorist"], ["Check hook timing, legibility and technical spec.", "No theatrical or broadcast packaging at S1."], "G3 · POST MASTER", "Short master · captions · platform crop", "Trim, recaption or reframe the failed element."),
            phase("Review & release", ["Judge hook clarity and craft quality.", "Run brand and light compliance review.", "Escalate only legal or material brand risk."], ["video.judge", "video.gatekeeper", "video.brand", "video.compliance"], ["S1: hard L1 + light L2.", "S2: L2 ≥90 + brand/compliance gate."], "G4 · RELEASE", "Sign-off log · provenance · unresolved-risk list", "Route notes to the owning phase."),
            phase("Distribution", ["Package one social branch at S1.", "At S2, add a second web/stream branch.", "Publish only channel-ready variants."], ["video.socialmediastrategist", "video.channelmanager", "video.marketing", "video.distributor"], ["Each outlet is Ready, Pending or Blocked.", "A failed outlet does not block accepted outlets."], "G5 · CHANNEL", "1–2 platform packages · metadata · provenance", "Repackage the failed outlet only.", parallel=True),
            phase("Post-launch learning", ["Collect views, CTR, hold rate and defects.", "Compare predicted and observed response.", "Create prompt/routing tickets for future runs."], ["video.analyst", "video.audiencesim", "video.retentionoptimizer", "video.memory"], ["Learning is regression-tested before reuse.", "Never silently mutate the published asset."], "OBSERVE", "Telemetry · learning tickets · memory update", "Feed validated learning into the next brief.", feedback_kind="learning"),
        ],
    ),
    diagram(
        "template", "b", "UGC Ad", "Primary scales S1–S3",
        "Create creator-style performance advertising from a KPI, audience and brand-safe CTA.",
        "Paid social tests, creator-style product ads, unboxing, direct response and variant campaigns.",
        "wf_video_arch_b_ugc_ad_v1.dna.json",
        "Shared skeleton plus the S1 flow; the source maps B to S1–S3 but does not define a bespoke B graph.",
        "L1 always; brand/compliance gate; scale-selected L2 and HiTL depth; privacy/consent remains fail-closed.",
        ["Template B", "S1–S3", "UGC variants", "ROAS feedback"],
        [
            phase("Greenlight", ["Set audience, offer, KPI, CTA and spend cap.", "Choose S1–S3 from risk and campaign depth.", "Confirm claims, creator voice and rights."], ["video.performancemarketer", "video.producer", "video.finance", "video.brand"], ["Reject unsupported claims or unclear consent.", "Freeze archetype, scale and success metric."], "G0 · GREENLIGHT", "Campaign brief · KPI · budget · claims boundary", "Revise offer, claim or audience definition."),
            phase("Pre-production", ["Develop hooks and creator-voice script variants.", "Define product proof, shot list and CTA.", "Set consent, brand and platform constraints."], ["video.ugccreator", "video.copywriter", "video.screenwriter", "video.brandstrategist"], ["L1 checks variant schema and brand boundary.", "Higher scales may retain multiple variants."], "G1 · L1 SPEC", "UGC script set · shot plan · consent state", "Return weak hook or noncompliant claim."),
            phase("Production", ["Perform or generate creator-style takes.", "Capture product demonstration and CTA.", "Run per-take identity and artifact QA."], ["video.ugccreator", "video.talent", "video.promptengineer", "video.aiqaconsistency"], ["Host policy gates generation and voice tools.", "Keep authentic tone without impersonation."], "G2 · CRAFT QC", "UGC takes · prompt evidence · QA report", "Rerecord or rerender only failed variant.", parallel=True),
            phase("Post-production", ["Build fast-paced ad cuts and hook variants.", "Add motion graphics, captions and safe crops.", "Normalize sound and platform formatting."], ["video.editor", "video.motiongraphics", "video.accessibilityoptimizer", "video.soundmixer"], ["Check first-frame hook, CTA and readability.", "Preserve variant IDs for performance analysis."], "G3 · POST MASTER", "Ad masters · captions · variant manifest", "Fix only the affected cut or overlay."),
            phase("Review & release", ["Score brand fit, claim accuracy and trust risk.", "Run compliance and privacy review.", "Escalate novel claims or identity concerns."], ["video.brand", "video.compliance", "video.trustsafety", "video.judge"], ["Scale controls L2 strictness and HiTL depth.", "Blocked claims cannot be published."], "G4 · RELEASE", "Approved ad set · sign-off · provenance", "Route claim, brand or safety notes to owner."),
            phase("Distribution", ["Fan variants into paid and organic social.", "Optionally trigger CRM or web placements.", "Track channel, audience and spend identity."], ["video.socialmediastrategist", "video.performancemarketer", "video.crm", "video.channelmanager"], ["Channel readiness is evaluated independently.", "Budget limits remain host-controlled."], "G5 · CHANNEL", "Paid/organic variants · metadata · campaign IDs", "Repackage the failed channel only.", parallel=True),
            phase("Post-launch learning", ["Measure ROAS, CTR, hook and hold rate.", "Compare variants with audience segments.", "Create evidence-backed optimization tickets."], ["video.analyst", "video.roasoptimizer", "video.audiencesim", "video.memory"], ["Require significance appropriate to the run.", "Validated learning informs future ads."], "OBSERVE", "Performance report · winning signals · tickets", "Feed tested learning into the next campaign.", feedback_kind="learning"),
        ],
    ),
    diagram(
        "template", "c", "Animated Explainer", "Primary scales S2–S4",
        "Explain a concept through coherent multi-scene animation, narration and accessible visual design.",
        "Product explainers, educational shorts, branded explainers and premium animated programmes.",
        "wf_video_arch_c_animated_explainer_v1.dna.json",
        "S2 detailed flow plus S3 premium mapping; S4 depth is a scale overlay rather than a bespoke C graph.",
        "L1 required; standard L2 ≥90 at S2; SME, brand, compliance and accessibility depth rises with scale.",
        ["Template C", "S2–S4", "multi-scene", "SME + a11y"],
        [
            phase("Greenlight", ["Set audience, learning goal and key takeaway.", "Choose S2–S4 from depth and outlet needs.", "Confirm budget, facts, brand and rights."], ["video.instructionaldesign", "video.producer", "video.sme", "video.brand"], ["Reject an unmeasurable objective or weak source base.", "Freeze outcome, scale and delivery plan."], "G0 · GREENLIGHT", "Approved objective · KPI · budget · source plan", "Revise objective, scope or evidence."),
            phase("Pre-production", ["Write one or more concise script variants.", "Build storyboard, look pack and visual grammar.", "Map every claim to an evidence source."], ["video.screenwriter", "video.storyboard", "video.conceptartist", "video.factchecker"], ["L1 validates script, claims and scene coverage.", "Lock narration, boards and terminology."], "G1 · L1 SPEC", "Script lock · storyboard · look pack · citations", "Return failed claim, panel or scene."),
            phase("Production", ["Generate or animate scene assets.", "Record voice and build explanatory graphics.", "Run per-shot consistency and anatomy/domain QA."], ["video.animator_2d", "video.voiceover", "video.motiongraphics", "video.aiqaconsistency"], ["Multi-shot identity and diagram accuracy are gated.", "Targeted rerender keeps accepted scenes."], "G2 · CRAFT QC", "Animated scenes · VO · graphics · QA evidence", "Rerender or revise only failed scene.", parallel=True),
            phase("Post-production", ["Assemble the explanatory sequence.", "Apply grade, score, sound design and mix.", "Add captions, audio description and variants."], ["video.editor", "video.colorist", "video.composer", "video.sounddesign", "video.accessibilityoptimizer"], ["Check pacing, intelligibility and contrast.", "Maintain claim-to-visual alignment."], "G3 · POST MASTER", "Explainer master · stems · captions · variants", "Fix pacing, audio or accessibility defect."),
            phase("Review & release", ["SME and FactChecker validate every claim.", "Brand and Compliance review final framing.", "Audience/Learner simulation tests clarity."], ["video.sme", "video.factchecker", "video.compliance", "video.audiencesim", "video.learnersim"], ["L2 and evidence thresholds follow selected scale.", "HiTL covers material domain or legal risk."], "G4 · RELEASE", "Review pack · provenance · sign-off log", "Route factual or clarity notes to owner."),
            phase("Distribution", ["Create social and streaming/mezzanine packages.", "Add LMS or channel package when required.", "Preserve captions, metadata and source links."], ["video.marketing", "video.seo", "video.channelmanager", "video.lms", "video.distributor"], ["S2 requires at least two relevant branches.", "Each branch passes independent readiness."], "G5 · CHANNEL", "Social · mezzanine · optional LMS/archive package", "Repackage only the failed endpoint.", parallel=True),
            phase("Post-launch learning", ["Measure completion, clarity and drop-off.", "Capture learner/audience confusion points.", "Turn defects into prompt and rubric tickets."], ["video.analyst", "video.audiencesim", "video.learnersim", "video.promptoptimizer"], ["Benchmark changes before promotion.", "Memory stores accepted corrections."], "OBSERVE", "Outcome report · confusion map · learning tickets", "Use validated insights in the next explainer.", feedback_kind="learning"),
        ],
    ),
    diagram(
        "template", "d", "Personalized Birthday", "Primary scales S1–S2",
        "Produce a privacy-aware personalized celebration video from reusable variables, voice and visual templates.",
        "Single-recipient or small-batch personalized greetings with lightweight social/direct delivery.",
        "wf_video_arch_d_personalized_birthday_v1.dna.json",
        "Shared skeleton plus S1/S2 overlays; the source maps D but does not define a bespoke ordered graph.",
        "L1 required; privacy, consent, template robustness and trust checks; S2 adds multi-format depth.",
        ["Template D", "S1–S2", "personalized", "privacy gated"],
        [
            phase("Greenlight", ["Capture recipient variables and creative intent.", "Choose S1 or S2 from batch and format needs.", "Confirm privacy, consent and expiry rules."], ["video.producer", "video.personalizationengineer", "video.compliance", "video.trustsafety"], ["Block missing consent or unsafe personal data.", "Freeze allowed merge fields and outlets."], "G0 · GREENLIGHT", "Personalization brief · consent · variable schema", "Revise data scope, consent or delivery plan."),
            phase("Pre-production", ["Design robust variable-content template.", "Write greeting script and pronunciation guide.", "Select approved avatar/voice treatment."], ["video.templatedesign", "video.copywriter", "video.screenwriter", "video.avatardesign"], ["L1 checks merge fields, layout and fallback values.", "Lock identity and voice consent state."], "G1 · L1 SPEC", "Template · script · variable map · consent state", "Fix unsafe field or fragile layout."),
            phase("Production", ["Merge recipient variables into the template.", "Render avatar/voice or visual variants.", "Run identity, pronunciation and sync QA."], ["video.personalizationengineer", "video.voiceclone", "video.lipsync", "video.aiqaconsistency"], ["No unapproved face or voice substitution.", "Each render retains a correlation ID."], "G2 · CRAFT QC", "Personalized renders · QA result · audit evidence", "Rerender only failed recipient variant.", parallel=True),
            phase("Post-production", ["Assemble greeting and optional music bed.", "Add captions, graphics and safe fallback copy.", "Create direct and share-ready formats."], ["video.editor", "video.motiongraphics", "video.accessibilityoptimizer", "video.composer"], ["Check variable overflow and readability.", "Prevent personal data leaking into metadata."], "G3 · POST MASTER", "Personalized master · captions · safe metadata", "Fix the failed variant or fallback."),
            phase("Review & release", ["Review impersonation and privacy risk.", "Test clarity and usability of personalized output.", "Escalate uncertain identity or consent."], ["video.trustsafety", "video.compliance", "video.ux", "video.deepfakedetection"], ["Scale-selected L2; consent gate is hard.", "Blocked identity cannot advance."], "G4 · RELEASE", "Approval record · provenance · expiry policy", "Return identity, privacy or UX issue."),
            phase("Distribution", ["Deliver through direct or CRM channel.", "Optionally create a share-safe social copy.", "Track delivery without exposing private fields."], ["video.crm", "video.channelmanager", "video.marketing", "video.socialmediastrategist"], ["Recipient and channel scopes stay isolated.", "Failed delivery does not republish content."], "G5 · CHANNEL", "Direct delivery · optional social-safe package", "Retry or repackage the failed delivery only.", parallel=True),
            phase("Post-launch learning", ["Measure render success and delivery completion.", "Collect opt-in audience response.", "Improve template robustness from defect patterns."], ["video.analyst", "video.audiencesim", "video.templatedesign", "video.memory"], ["Do not learn from private content without policy.", "Regression-test every template change."], "OBSERVE", "Delivery report · defect log · template tickets", "Apply validated fixes to future templates.", feedback_kind="learning"),
        ],
    ),
    diagram(
        "template", "e", "AI Short Film", "Primary scales S2–S5",
        "Create a coherent multi-scene short film with governed visual generation, continuity, post and release packaging.",
        "Branded shorts, narrative AI films, premium short-form and scale-expanded multi-unit docu-drama.",
        "wf_video_arch_e_ai_short_film_v1.dna.json",
        "S2 baseline flow; S4/S5 overlays add picture/sound/marketing parallelism and multi-unit depth.",
        "L1 required; multi-shot AIQA and continuity; strict legal, identity and release gates at higher scales.",
        ["Template E", "S2–S5", "multi-scene", "continuity mesh"],
        [
            phase("Greenlight", ["Approve treatment, audience, runtime and tone.", "Select S2–S5 from ambition and risk.", "Confirm budget, IP, likeness and outlets."], ["video.producer", "video.director", "video.finance", "video.legal"], ["Reject unclear rights or infeasible scope.", "Freeze treatment, scale and success criteria."], "G0 · GREENLIGHT", "Treatment · KPI · budget · rights register", "Revise treatment, budget or rights."),
            phase("Pre-production", ["Lock screenplay and scene/beat structure.", "Build boards, lookbook and character references.", "Cast voices/talent and set continuity baselines."], ["video.screenwriter", "video.storyboard", "video.conceptartist", "video.casting", "video.continuity"], ["L1 checks story, coverage, assets and consent.", "Higher scales add production design depth."], "G1 · L1 SPEC", "Script lock · boards · lookbook · continuity bible", "Return only failed story or design artifact."),
            phase("Production", ["Issue shot intents and camera plans.", "Generate/capture scenes and performances.", "Run per-shot AIQA, identity and continuity loops."], ["video.director", "video.cinematographer", "video.promptengineer", "video.aiqaconsistency", "video.continuity"], ["S4+ may run picture, sound and marketing lanes.", "Targeted rerender preserves accepted shots."], "G2 · CRAFT QC", "Takes/plates · prompt evidence · render telemetry", "Rerender the failed shot or performance.", parallel=True),
            phase("Post-production", ["Assemble rough cut and picture lock.", "Run VFX, grade, score, sound and mix.", "Prepare captions, trailer and social cutdowns."], ["video.editor", "video.vfxsupervisor", "video.colorist", "video.composer", "video.soundmixer", "video.trailereditor"], ["Check narrative pacing, continuity and technical QC.", "Branches converge on a reviewable master."], "G3 · POST MASTER", "Picture lock · grade · stems · captions · cutdowns", "Return the failed picture, VFX or sound element.", parallel=True),
            phase("Review & release", ["AudienceSim and Critic test story response.", "Run legal, compliance and synthetic-media review.", "Gate unresolved risks through HiTL."], ["video.audiencesim", "video.critic", "video.compliance", "video.deepfakedetection", "video.judge"], ["L2 strictness follows scale; all releases pass L1.", "Consent and novel legal risk are hard gates."], "G4 · RELEASE", "Audience/legal/provenance pack · sign-off", "Route notes to script, production or post."),
            phase("Distribution", ["Package streaming/mezzanine and social versions.", "Add festival, archive or broadcast by scale.", "Deliver only branches that pass outlet QC."], ["video.distributor", "video.marketing", "video.festivalstrategist", "video.archivemaster", "video.channelmanager"], ["S2 starts with two branches; S5 is multi-branch.", "Preserve territorial rights and provenance."], "G5 · CHANNEL", "Streaming · social · festival/archive packages", "Repackage the failed outlet only.", parallel=True),
            phase("Post-launch learning", ["Measure audience response, retention and defects.", "Capture critic/festival and campaign outcomes.", "Create prompt, routing and rubric tickets."], ["video.analyst", "video.retentionoptimizer", "video.evaluationharness", "video.memory"], ["Run regressions before changing production defaults.", "Corrections update affected versions only."], "OBSERVE", "Performance report · defect log · learning tickets", "Feed tested learning into the next film plan.", feedback_kind="learning"),
        ],
    ),
    diagram(
        "template", "f", "Corporate Training", "Primary scales S2–S5",
        "Build accurate, accessible and measurable training content from objectives through LMS-ready delivery.",
        "Corporate learning modules, recurring training series, compliance education and multilingual programmes.",
        "wf_video_arch_f_corporate_training_v1.dna.json",
        "Detailed S3 flow with the shared skeleton; S2/S4/S5 are scale-depth overlays.",
        "L1 required; SME/fact/legal gates; accessibility and learner outcome review; corrections feed project memory.",
        ["Template F", "S2–S5", "LMS ready", "SME + legal"],
        [
            phase("Greenlight", ["Define learning objectives and target roles.", "Select scale from module/series complexity.", "Confirm SME, compliance, accessibility and budget."], ["video.instructionaldesign", "video.producer", "video.sme", "video.compliance"], ["Reject unmeasurable objectives or missing owner.", "Freeze assessment and distribution strategy."], "G0 · GREENLIGHT", "Learning brief · objectives · budget · policy scope", "Revise objective, scope or governance."),
            phase("Pre-production", ["Build series bible or module structure.", "Write script, assessment and visual plan.", "Fact-check terminology and legal requirements."], ["video.showrunner", "video.screenwriter", "video.instructionaldesign", "video.factchecker", "video.storyboard"], ["L1 validates objectives, script and assessment map.", "SME and Compliance pre-clear factual content."], "G1 · L1 SPEC", "Script lock · assessment · boards · source evidence", "Return failed fact, objective or sequence."),
            phase("Production", ["Direct presenter/avatar and supporting visuals.", "Generate graphics, demonstrations and narration.", "Run consistency and domain QA."], ["video.director", "video.avatardesign", "video.motiongraphics", "video.voiceover", "video.aiqaconsistency"], ["Claims remain tied to approved evidence.", "Targeted rerender preserves accepted lessons."], "G2 · CRAFT QC", "Lesson scenes · narration · graphics · QA report", "Rerender or rewrite the failed lesson element.", parallel=True),
            phase("Post-production", ["Assemble lesson and assessment cues.", "Grade, mix, caption and localize.", "Create SCORM/xAPI and channel variants."], ["video.editor", "video.soundmixer", "video.accessibility", "video.localizationqa", "video.signlanguageinterpreter"], ["Check intelligibility, caption accuracy and contrast.", "Preserve learning-objective traceability."], "G3 · POST MASTER", "Training master · captions · localized assets", "Fix accessibility, localization or pacing defect.", parallel=True),
            phase("Review & release", ["SME and FactChecker verify instruction.", "StandardsEditor and Legal review policy framing.", "LearnerSim tests confusion and assessment fit."], ["video.sme", "video.factchecker", "video.standardseditor", "video.legal", "video.learnersim"], ["L3/HiTL includes SME and legal acceptance.", "No module ships with unresolved factual risk."], "G4 · RELEASE", "SME/legal report · learner simulation · sign-off", "Route issue to script, visual or assessment owner."),
            phase("Distribution", ["Package and deploy to LMS.", "Schedule portal/channel and archive copies.", "Carry metadata, accessibility and tracking schema."], ["video.lms", "video.channelmanager", "video.distributor", "video.archivemaster", "video.seo"], ["Validate SCORM/xAPI and completion tracking.", "Each language/package is independently ready."], "G5 · CHANNEL", "LMS package · portal media · archive master", "Repackage failed LMS or language endpoint.", parallel=True),
            phase("Post-launch learning", ["Measure completion, quiz outcomes and confusion.", "Log corrections and support signals.", "Update project bible and improvement tickets."], ["video.analyst", "video.learnersim", "video.corrections", "video.memory"], ["Corrections preserve version and notice history.", "Regression-test revised prompts and rubrics."], "OBSERVE", "Learning analytics · corrections · improvement tickets", "Feed validated outcomes into the next module.", feedback_kind="learning"),
        ],
    ),
    diagram(
        "template", "g", "Music Video", "Primary scales S3–S5",
        "Coordinate song-led visual concept, performance, picture/audio pipelines, rights and label distribution.",
        "Live + AI VFX music videos, premium performance films and label/digital campaigns.",
        "wf_video_arch_g_music_video_v1.dna.json",
        "Detailed S4 flow; an explicit S2-light exception exists below the primary S3–S5 range.",
        "Strict craft QC; sample/rights clearance; deepfake and consent review; parallel picture, sound and marketing.",
        ["Template G", "S3–S5", "3 parallel lanes", "rights heavy"],
        [
            phase("Greenlight", ["Align artist brief, song, audience and visual ambition.", "Choose S3–S5 and lock budget/schedule.", "Create rights, sample and likeness register."], ["video.musicvideodirector", "video.producer", "video.labela_r", "video.legal"], ["Sample and identity rights must be traceable.", "Freeze creative and campaign success criteria."], "G0 · GREENLIGHT", "Artist brief · concept target · budget · rights register", "Revise concept, rights or production scope."),
            phase("Pre-production", ["Build concept pack, boards and lookbook.", "Plan choreography, casting and production design.", "Define picture, sound and marketing lanes."], ["video.musicvideodirector", "video.choreography", "video.casting", "video.productiondesign", "video.moodboard"], ["L1 checks concept, performance and coverage.", "Consent and sample state must be known."], "G1 · L1 SPEC", "Concept pack · performance plan · boards · clearances", "Return failed design, casting or rights item.", parallel=True),
            phase("Production", ["Picture: DoP, camera/prompt pool, continuity, VFX.", "Audio: score/stems, mix and music supervision.", "Marketing: capture trailer/social moments early."], ["video.cinematographer", "video.promptengineer", "video.continuity", "video.composer", "video.musicsupervisor", "video.aiqaconsistency"], ["Run per-shot QA and performance review.", "Picture, sound and marketing execute in parallel."], "G2 · CRAFT QC", "Picture takes · audio assets · render telemetry", "Rerender, rerecord or restage failed element.", parallel=True),
            phase("Post-production", ["Edit performance and VFX to music structure.", "Grade picture and complete final mix.", "Develop trailer and social cutdowns before lock."], ["video.editor", "video.vfxsupervisor", "video.colorist", "video.soundmixer", "video.trailereditor", "video.socialmediastrategist"], ["Picture lock and music rights precede master.", "Check beat sync, identity and continuity."], "G3 · POST MASTER", "Picture lock · grade · final mix · cutdowns", "Return failed picture, sound or campaign cut.", parallel=True),
            phase("Review & release", ["Run Legal, Compliance and consent checks.", "DeepfakeDetection verifies synthetic identity.", "Judge and GateKeeper consolidate release evidence."], ["video.legal", "video.compliance", "video.deepfakedetection", "video.judge", "video.gatekeeper"], ["S4 quality: strict L2 + rights/deepfake HiTL.", "Blocked sample or identity halts release."], "G4 · RELEASE", "Rights clearance · provenance · sign-off log", "Route legal, identity or craft notes to owner."),
            phase("Distribution", ["LabelDigital packages channel-ready assets.", "Distributor handles relevant outlet branches.", "Marketing/social execute campaign schedule."], ["video.labeldigital", "video.distributor", "video.marketing", "video.socialmediastrategist", "video.channelmanager"], ["Each branch validates metadata and rights.", "Territory and embargo constraints are preserved."], "G5 · CHANNEL", "Label package · platform masters · campaign assets", "Repackage only failed outlet or territory.", parallel=True),
            phase("Post-launch learning", ["Measure audience, community, ROAS and retention.", "Compare song moments and cutdown performance.", "Create next-plan optimization tickets."], ["video.analyst", "video.community", "video.roasoptimizer", "video.retentionoptimizer", "video.memory"], ["Do not rewrite released masters silently.", "Regression-test new prompts and routing."], "OBSERVE", "Campaign report · audience signals · next-plan tickets", "Feed tested learning into the next release plan.", feedback_kind="learning"),
        ],
    ),
    diagram(
        "template", "h", "AI Avatar", "Primary scales S1–S4",
        "Create a consented synthetic presenter workflow with governed identity, voice, lip-sync and disclosure.",
        "Avatar explainers, talking-head campaigns, personalized presenters and multilingual brand content.",
        "wf_video_arch_h_ai_avatar_v1.dna.json",
        "Shared skeleton plus S1–S4 scale overlays; the source maps H but does not define a bespoke ordered graph.",
        "L1 required; consent and disclosure hard gates; identity, voice, lip-sync and deepfake review scale with risk.",
        ["Template H", "S1–S4", "identity gated", "multilingual"],
        [
            phase("Greenlight", ["Define presenter purpose, audience and channels.", "Choose scale from duration, languages and risk.", "Confirm voice/likeness consent and disclosure."], ["video.producer", "video.brandstrategist", "video.compliance", "video.legal"], ["Block missing consent or deceptive use.", "Freeze allowed identity and language scope."], "G0 · GREENLIGHT", "Presenter brief · consent · disclosure · scale", "Revise use case, identity or consent."),
            phase("Pre-production", ["Design synthetic identity and visual rules.", "Write script, pronunciation and localization plan.", "Select approved voice and template treatment."], ["video.avatardesign", "video.screenwriter", "video.voiceclone", "video.templatedesign", "video.localizationqa"], ["L1 validates script, identity bank and consent.", "Lock reference frames and voice profile."], "G1 · L1 SPEC", "Avatar bank · script · voice profile · consent chain", "Fix identity, script or language defect."),
            phase("Production", ["Render avatar performance and voice.", "Align phoneme/viseme timing and gestures.", "Run identity consistency and artifact QA."], ["video.avatardesign", "video.voiceclone", "video.lipsync", "video.aiqaconsistency", "video.promptengineer"], ["No unapproved identity or voice substitution.", "Targeted rerender keeps accepted segments."], "G2 · CRAFT QC", "Avatar takes · voice · sync report · telemetry", "Rerender failed face, voice or sync segment.", parallel=True),
            phase("Post-production", ["Assemble presenter timeline and graphics.", "Add captions, sign language or localization.", "Create channel-specific aspect and duration variants."], ["video.editor", "video.motiongraphics", "video.accessibility", "video.signlanguageinterpreter", "video.localizationqa"], ["Check disclosure, readability and language quality.", "Preserve identity provenance in every variant."], "G3 · POST MASTER", "Presenter master · captions · localized variants", "Fix accessibility, language or graphics issue.", parallel=True),
            phase("Review & release", ["Verify brand, privacy and disclosure.", "Run deepfake and trust/safety screening.", "Escalate identity or high-risk claims to HiTL."], ["video.brand", "video.compliance", "video.deepfakedetection", "video.trustsafety", "video.judge"], ["Consent is a hard gate at every scale.", "Higher scales add strict L2 and rights review."], "G4 · RELEASE", "Identity verification · provenance · sign-off", "Return identity, disclosure or claim issue."),
            phase("Distribution", ["Package marketing, social, CRM or LMS variants.", "Keep language and identity metadata aligned.", "Publish only approved identity/channel pairs."], ["video.marketing", "video.socialmediastrategist", "video.crm", "video.lms", "video.channelmanager"], ["Each outlet and language is independently ready.", "Personalized scopes remain isolated."], "G5 · CHANNEL", "Channel packages · disclosure metadata · archive copy", "Repackage failed language or channel only.", parallel=True),
            phase("Post-launch learning", ["Measure clarity, completion and trust signals.", "Track identity/sync defects and corrections.", "Improve reference banks through tested tickets."], ["video.analyst", "video.audiencesim", "video.corrections", "video.memory"], ["Private or biometric data is not reused silently.", "Regression-test all identity changes."], "OBSERVE", "Quality report · correction log · improvement tickets", "Feed validated improvements into future avatars.", feedback_kind="learning"),
        ],
    ),
    diagram(
        "template", "i", "Documentary", "Primary scales S4–S6",
        "Build a source-grounded documentary through archive research, continuous fact checking, ethical review and corrections.",
        "Explained episodes, historical/scientific series, docuseries and multilingual archive-heavy releases.",
        "wf_video_arch_i_documentary_v1.dna.json",
        "Detailed S6 flow; S3-light and S4/S5 variants are explicit scale exceptions/overlays.",
        "Strict factual L2; dual legal/ethics clearance; continuous fact mesh; mandatory post-launch corrections at S6.",
        ["Template I", "S4–S6", "fact mesh", "archive + ethics"],
        [
            phase("Greenlight", ["Start research track before full greenlight.", "Define thesis, subjects, territories and sources.", "Approve budget, rights and portrayal ethics."], ["video.producer", "video.finance", "video.legal", "video.ethics", "video.planner"], ["Dual clearance: rights plus ethical portrayal.", "Unresolved source/subject risk blocks production."], "G0 · GREENLIGHT", "Research brief · budget · rights · ethics record", "Revise thesis, rights or portrayal plan."),
            phase("Pre-production", ["Web and archive research build SourceCatalog.", "Journalist and Screenwriter form treatment.", "FactChecker establishes continuous claim mesh."], ["video.webresearch", "video.archiveresearch", "video.journalist", "video.screenwriter", "video.factchecker", "video.citation"], ["L1 requires source traceability and treatment scope.", "Archive assets carry rights and provenance."], "G1 · L1 SPEC", "SourceCatalog · treatment · citations · archive plan", "Return unsupported claim or unclear source."),
            phase("Production", ["Capture interviews, scenes and contextual visuals.", "Integrate ArchiveProducer source inserts.", "Continuously verify claims and continuity."], ["video.director", "video.cinematographer", "video.archiveproducer", "video.interviewsynthesis", "video.factchecker"], ["Evidence follows each artifact handoff.", "Targeted pickup replaces only failed material."], "G2 · CRAFT QC", "Interviews · footage · archive inserts · evidence", "Pickup, reclear or correct failed evidence."),
            phase("Post-production", ["Assemble narrative and voiceover.", "Complete color, sound, captions and localization.", "Keep citations and archive lineage attached."], ["video.editor", "video.voiceover", "video.colorist", "video.soundmixer", "video.localizationqa", "video.accessibility"], ["Check source-context fidelity and accessibility.", "No edit may detach a claim from evidence."], "G3 · POST MASTER", "Documentary master · stems · captions · source map", "Fix edit, context, audio or localization defect."),
            phase("Review & release", ["FactChecker validates final claim set.", "Legal, StandardsEditor and Ethics review.", "Judge/GateKeeper resolve remaining disputes."], ["video.factchecker", "video.legal", "video.standardseditor", "video.ethics", "video.gatekeeper"], ["S6: strict L2 + ethics/corrections HiTL.", "Unresolved factual or portrayal risk blocks."], "G4 · RELEASE", "Fact/legal/ethics pack · provenance · sign-off", "Route factual, legal or ethical note to owner.", parallel=True),
            phase("Distribution", ["Package channel, SEO and multilingual assets.", "Create preservation master and source archive.", "Carry territorial rights to each endpoint."], ["video.channelmanager", "video.seo", "video.archivemaster", "video.distributor", "video.localizationqa"], ["Every outlet validates rights and metadata.", "Archive integrity is mandatory for S6."], "G5 · CHANNEL", "Channel packages · metadata · archive master", "Repackage or reclear only failed endpoint.", parallel=True),
            phase("Post-launch learning", ["Monitor audience response and factual challenges.", "Issue transparent corrections/version notices.", "Create distillation and benchmark tickets."], ["video.corrections", "video.analyst", "video.evaluationharness", "video.memory"], ["Corrections are mandatory in the S6 overlay.", "Learning remains evidence-backed and tested."], "OBSERVE", "Corrections · telemetry · distillation tickets", "Feed validated findings into future research.", feedback_kind="learning"),
        ],
    ),
    diagram(
        "template", "j", "Feature Film", "Primary scales S6–S7",
        "Run a formally governed feature workflow from IP intake through phased full-crew production and long-tail learning.",
        "Feature-length, animated feature, epic or high-risk multi-territory cinematic production.",
        "wf_video_arch_j_feature_film_v1.dna.json",
        "Detailed S7 flow; the matrix also permits S6, but this source contains no separate J-at-S6 graph.",
        "Full L1/L2/L3; hard human phase gates; consent, ethics, MPA, C2PA and final release board.",
        ["Template J", "S6–S7", "phased 114 pool", "formal board"],
        [
            phase("Greenlight", ["Perform IP, rights, likeness and ethics intake.", "Develop screenplay, narrative arc and concept art.", "Formal board approves budget, scope and slate."], ["video.screenwriter", "video.producer", "video.director", "video.legal", "video.ethics", "video.finance"], ["GateKeeper + HiTL hard gate every phase.", "No production before formal GreenlightPacket."], "G0 · FORMAL BOARD", "Rights intake · development pack · GreenlightPacket", "Return screenplay, budget, consent or IP issue."),
            phase("Pre-production", ["Build boards, production design and costume bible.", "Lock cast reference/character banks.", "Write continuity, world and sequence plans to Memory."], ["video.storyboard", "video.productiondesign", "video.costumedesign", "video.mua_makeup", "video.casting", "video.continuity"], ["L1 checks complete sequence coverage and consent.", "Principal cast reference banks are required."], "G1 · L1 SPEC", "Pre-production bible · reference banks · schedule", "Return failed sequence, design or consent item.", parallel=True),
            phase("Production", ["Run per-sequence picture DAGs.", "Execute voice/music/sync track in parallel.", "Apply AIQA, continuity and VFX supervision."], ["video.promptengineer", "video.cinematographer", "video.cameraoperator", "video.voiceclone", "video.lipsync", "video.aiqaconsistency"], ["Full telemetry and provenance per sequence.", "Accepted sequences survive targeted rework."], "G2 · CRAFT QC", "Sequence plates/takes · audio · QA · telemetry", "Rerender or rerecord failed sequence element.", parallel=True),
            phase("Post-production", ["Assemble edit and complex VFX pipeline.", "Complete grade, sound design and final mix.", "Develop trailer/marketing assets in parallel."], ["video.editor", "video.vfxsupervisor", "video.colorist", "video.sounddesign", "video.soundmixer", "video.trailereditor"], ["Strict craft and six-pass delivery QC.", "Picture, sound and campaign lanes converge."], "G3 · POST MASTER", "Picture master · stems · VFX · trailers · QC", "Return failed picture, VFX, sound or campaign asset.", parallel=True),
            phase("Review & release", ["AudienceSim/Critic test preference and interpretation.", "MPA, Legal/C2PA, Ethics and Compliance review.", "Human release board resolves final risks."], ["video.audiencesim", "video.critic", "video.mpa", "video.legal", "video.compliance", "video.gatekeeper"], ["Full L1/L2/L3 plus formal final HiTL.", "Consent, ethics, rating and legal gates are hard."], "G4 · RELEASE BOARD", "C2PA release pack · rating · sign-off · risks", "Route notes to the exact owning sequence/phase.", parallel=True),
            phase("Distribution", ["Build multi-territory sales/distributor packages.", "Fan out theatrical, stream, broadcast and archive.", "Run trailer, marketing, festival and awards tracks."], ["video.sales", "video.distributor", "video.marketing", "video.archivemaster", "video.festivalstrategist", "video.awardsstrategist"], ["Every territory/outlet has independent readiness.", "Awards/festival planning starts early."], "G5 · CHANNEL MATRIX", "DCP · stream · broadcast · archive · campaigns", "Repackage only failed outlet or territory.", parallel=True),
            phase("Post-launch learning", ["Track years-long audience, awards and defects.", "Run evaluation and prompt/routing regressions.", "Issue corrections and dependency-targeted updates."], ["video.analyst", "video.evaluationharness", "video.promptoptimizer", "video.corrections", "video.memory"], ["Canary all high-risk model/policy changes.", "Never silently replace released masters."], "OBSERVE", "Long-tail telemetry · corrections · learning tickets", "Feed tested findings into future development.", feedback_kind="learning"),
        ],
    ),
]


SCALES = [
    diagram(
        "scale", "s1", "Micro Production", "$100–$50K · ~15–25 active agents · hours to days",
        "Optimize speed and cost for short-form content with a small crew, minimal branching and one primary outlet.",
        "Social spike, single-SKU promo, fail-closed proof of concept, or A/B/H DNA UAT.",
        "A/B/H defaults; D-light · one DNA graph",
        "Explicit S1 data flow and crew capability map from the production scale framework.",
        "L1 required; light L2; rare legal-only HiTL; sparse critique; one delivery branch.",
        ["Scale S1", "~15–25 agents", "1 outlet", "hours → days"],
        [
            phase("Greenlight", ["Human brief enters through host command/UI.", "Planner emits a 4–6-node S1 plan.", "Producer checks light budget and rights."], ["video.planner", "video.producer", "video.finance", "video.compliance"], ["Set scale_profile=S1 before archetype.", "GateKeeper/HiTL only on material failure."], "G0 · GREENLIGHT", "Brief · KPI · light budget/rights · S1 plan", "Reduce scope or clear rights before launch."),
            phase("Pre-production", ["TrendIntelligence and Copywriter form HookConcept.", "Optional Screenwriter creates short VO/script.", "Freeze single-outlet technical specification."], ["video.trendintelligence", "video.copywriter", "video.screenwriter", "video.director"], ["L1 is hard; low-risk L2 may be light.", "Keep minimal nodes and no unnecessary branches."], "G1 · L1 SPEC", "HookConcept · optional script · outlet spec", "Return failed concept or script only."),
            phase("Production", ["PromptEngineer creates generation intents.", "Host-gated adapter produces takes.", "AIQAConsistency accepts or targets rerender."], ["video.promptengineer", "video.aiqaconsistency", "video.router", "video.orchestrator"], ["Tools remain fail-closed without activation.", "Record evidence_refs and render telemetry."], "G2 · CRAFT QC", "Approved takes · prompts · QA · telemetry", "Rerender only failed take."),
            phase("Post-production", ["Editor assembles a single timeline.", "AccessibilityOptimizer adds captions.", "Create 1–2 platform variants."], ["video.editor", "video.accessibilityoptimizer", "video.motiongraphics", "video.socialmediastrategist"], ["No theatrical/broadcast branch.", "Validate aspect, duration and readability."], "G3 · POST MASTER", "Single master · captions · platform variants", "Trim or reformat failed variant."),
            phase("Review & release", ["Judge/GateKeeper consolidate L1 and light L2.", "Compliance performs a light legal check.", "Human reviews only material legal risk."], ["video.judge", "video.gatekeeper", "video.compliance", "video.critic"], ["Critique density is sparse.", "Unresolved legal risk blocks release."], "G4 · RELEASE", "Light review pack · sign-off · provenance", "Return the exact failed artifact."),
            phase("Distribution", ["Publish one primary social branch.", "Optionally emit a second platform crop.", "Project status to console through host events."], ["video.socialmediastrategist", "video.channelmanager", "video.marketing", "video.distributor"], ["One branch is the S1 operating rule.", "Each variant retains correlation/provenance."], "G5 · CHANNEL", "Social package · metadata · event projection", "Repackage failed platform crop only."),
            phase("Post-launch learning", ["Analyst collects views and CTR.", "Optional AudienceSim compares expected response.", "Memory stores approved learning tickets."], ["video.analyst", "video.audiencesim", "video.memory", "video.promptoptimizer"], ["No automatic autoscaling to S2.", "Regression-test any prompt/routing update."], "OBSERVE", "Views/CTR · defect log · learning tickets", "Use validated signals in the next S1 brief.", feedback_kind="learning"),
        ],
    ),
    diagram(
        "scale", "s2", "Small Production", "$1K–$100K · ~25–40 agents · days to weeks",
        "Add multi-scene coherence, cinematography/VFX, richer audio, continuity-lite and multi-format delivery.",
        "Animated explainer, multi-scene short, interview package, or social plus web/streaming mezzanine.",
        "C/D/E-short/G-light DNA",
        "Explicit S2 data flow and additive crew from the production scale framework.",
        "L1 required; L2 standard ≥90; brand/compliance HiTL; moderate critique; at least two delivery branches.",
        ["Scale S2", "~25–40 agents", "≥2 outlets", "L2 ≥90"],
        [
            phase("Greenlight", ["Brief becomes a multi-phase Planner DAG.", "Producer and Finance approve scope/budget.", "Select C/D/E-short/G-light archetype."], ["video.planner", "video.producer", "video.finance", "video.compliance"], ["Set scale_profile=S2 first.", "Require at least two relevant outlets."], "G0 · GREENLIGHT", "Multi-phase plan · budget · rights · distribution map", "Reduce scope, budget or branch count."),
            phase("Pre-production", ["Optionally develop A/B script variants.", "Build storyboard and ConceptArtist look pack.", "Define shot adjacency and continuity-lite."], ["video.screenwriter", "video.storyboard", "video.conceptartist", "video.director"], ["L1 checks scenes, boards and identity references.", "Brand constraints enter before generation."], "G1 · L1 SPEC", "Scripts · storyboard · look pack · shot plan", "Return failed script, board or look asset."),
            phase("Production", ["Director emits shot intents.", "PromptEngineer and AIQA loop per shot.", "Cinematographer validates framing and look."], ["video.director", "video.promptengineer", "video.aiqaconsistency", "video.cinematographer", "video.vfxsupervisor"], ["Multi-shot identity QA is required.", "Router design does not auto-enable live tools."], "G2 · CRAFT QC", "Shot takes · QA reports · render telemetry", "Rerender only failed shot."),
            phase("Post-production", ["Editor creates rough cut.", "Colorist, Composer and SoundDesign finish.", "Accessibility and variants complete package."], ["video.editor", "video.colorist", "video.composer", "video.sounddesign", "video.accessibilityoptimizer"], ["Check coherence, audio and technical specs.", "Preserve versioned scene dependencies."], "G3 · POST MASTER", "Rough/final cut · grade · score · captions", "Fix failed post lane only.", parallel=True),
            phase("Review & release", ["Brand and Compliance review final work.", "Judge enforces L2 ≥90.", "AudienceSim provides post-launch/pre-release signal."], ["video.brand", "video.compliance", "video.judge", "video.critic", "video.audiencesim"], ["Brand/compliance HiTL applies.", "Moderate critique remains bounded."], "G4 · RELEASE", "Brand/compliance report · L2 score · sign-off", "Return notes to owning scene or post lane."),
            phase("Distribution", ["Package social branch.", "Package streaming/mezzanine or archive branch.", "Validate metadata and accessibility per outlet."], ["video.socialmediastrategist", "video.distributor", "video.channelmanager", "video.archivemaster"], ["At least two distribution branches.", "Each branch may be Ready/Pending/Blocked."], "G5 · CHANNEL", "Social · mezzanine/archive · metadata", "Repackage failed branch only.", parallel=True),
            phase("Post-launch learning", ["Analyst measures performance.", "AudienceSim compares audience cohorts.", "PromptOptimizer creates held-out improvement tests."], ["video.analyst", "video.audiencesim", "video.promptoptimizer", "video.memory"], ["No automatic scale promotion.", "Only tested learning enters future plans."], "OBSERVE", "Performance report · benchmark delta · tickets", "Feed validated learning into next plan.", feedback_kind="learning"),
        ],
    ),
    diagram(
        "scale", "s3", "Medium Production", "$20K–$1M · ~40–55 agents · recurring days/weeks",
        "Run a broadcast-like recurring cadence with specialized craft, project memory, scheduled publishing and fact/legal gates.",
        "Recurring shows, corporate training series, documentary explainers and multilingual programmes.",
        "F/I-segment/C-premium DNA",
        "Explicit S3 series-bible-to-corrections flow from the production scale framework.",
        "L1 required; standard L2; SME + legal HiTL; dense factual critique; social/stream/archive delivery.",
        ["Scale S3", "~40–55 agents", "series memory", "fact + legal"],
        [
            phase("Greenlight", ["Initialize series bible in Memory.", "Showrunner and Planner create seasonal plan.", "Producer/Compliance confirm cadence and scope."], ["video.showrunner", "video.planner", "video.producer", "video.memory", "video.compliance"], ["Set scale_profile=S3 and recurring identity.", "Legal and compliance are required before release."], "G0 · GREENLIGHT", "Series bible · seasonal plan · budget · rights", "Revise cadence, scope or governance."),
            phase("Pre-production", ["Episode brief drives Screenwriter and SME.", "FactChecker/Citation pre-clear claims.", "Craft teams plan sets, wardrobe and boards."], ["video.screenwriter", "video.sme", "video.factchecker", "video.citation", "video.productiondesign", "video.storyboard"], ["L1 checks episode, facts and continuity.", "Memory stores approved bible updates."], "G1 · L1 SPEC", "Episode brief · script · evidence · craft plan", "Return unsupported fact or continuity conflict."),
            phase("Production", ["Director/DoP/prompt pool run production unit.", "Costume, makeup and choreography support craft.", "AIQA and continuity verify recurring identity."], ["video.director", "video.cinematographer", "video.promptengineer", "video.costumedesign", "video.mua_makeup", "video.aiqaconsistency"], ["Specialized crew follows episode plan.", "Targeted pickups preserve approved segments."], "G2 · CRAFT QC", "Episode takes · craft assets · telemetry", "Pickup or rerender failed segment."),
            phase("Post-production", ["Post unit completes edit, color, sound and A11y.", "Localize and add sign-language layer as needed.", "Trailer/marketing assets begin early."], ["video.editor", "video.colorist", "video.soundmixer", "video.accessibility", "video.localizationqa", "video.trailereditor"], ["Check recurring look, loudness and access.", "Maintain episode/series version lineage."], "G3 · POST MASTER", "Episode master · localized/access assets · trailer", "Fix failed post or localization lane.", parallel=True),
            phase("Review & release", ["StandardsEditor and Legal gate release.", "SME/FactChecker close factual issues.", "Judge consolidates dense critique."], ["video.standardseditor", "video.legal", "video.sme", "video.factchecker", "video.judge"], ["L3/HiTL includes SME and legal acceptance.", "No factual show advances with open blocker."], "G4 · RELEASE", "Standards/legal/fact pack · sign-off", "Route issue to script, evidence or edit."),
            phase("Distribution", ["ChannelManager schedules multi-platform release.", "Fan out social, streaming and archive.", "Add broadcast package where needed."], ["video.channelmanager", "video.socialmediastrategist", "video.distributor", "video.archivemaster", "video.marketing"], ["Every platform validates metadata and access.", "Publishing cadence is tracked."], "G5 · CHANNEL", "Social · streaming · archive · optional broadcast", "Repackage failed channel only.", parallel=True),
            phase("Post-launch learning", ["Analyst tracks episode and series performance.", "Corrections closes factual/version issues.", "Memory updates the series bible."], ["video.analyst", "video.corrections", "video.memory", "video.evaluationharness"], ["Correction notices remain auditable.", "Regression-test prompt/rubric changes."], "OBSERVE", "Analytics · corrections · bible updates", "Feed validated feedback into next episode.", feedback_kind="learning"),
        ],
    ),
    diagram(
        "scale", "s4", "Medium-Large Production", "$50K–$5M · ~55–75 agents · 1–6 months",
        "Run premium picture, sound and marketing lanes with rights-heavy clearance, optimization and multi-outlet packaging.",
        "Music video, premium brand film, comedy/talk package or label/digital release coordination.",
        "G Music Video / E premium DNA",
        "Explicit S4 parallel picture/audio/marketing data flow from the production scale framework.",
        "L1 required; strict L2; rights + deepfake HiTL; full QC mesh; multi-outlet delivery.",
        ["Scale S4", "~55–75 agents", "3 parallel lanes", "full QC mesh"],
        [
            phase("Greenlight", ["Approve budget and detailed rights register.", "Select premium concept and outlet matrix.", "Align label/series, producer and counsel."], ["video.producer", "video.finance", "video.legal", "video.musicvideodirector", "video.showrunner"], ["Set scale_profile=S4.", "Sample, likeness and outlet rights are explicit."], "G0 · GREENLIGHT", "Budget · rights register · concept mandate", "Revise budget, rights or outlet ambition."),
            phase("Pre-production", ["Build concept pack and lookbook.", "Plan choreography, casting and production design.", "Define parallel picture/sound/marketing work."], ["video.choreography", "video.casting", "video.productiondesign", "video.moodboard", "video.labela_r"], ["L1 validates coverage and performance plan.", "Trailer/social work is planned before lock."], "G1 · L1 SPEC", "Concept pack · boards · performance/marketing plan", "Return failed concept, casting or clearance."),
            phase("Production", ["Picture: DoP + prompt pool + continuity + VFX.", "Sound: composer + mixer + supervisor.", "Marketing: social moments and campaign capture."], ["video.cinematographer", "video.promptengineer", "video.continuity", "video.vfxsupervisor", "video.composer", "video.musicsupervisor"], ["Cost/latency routing is policy-only until enabled.", "Per-shot QA and provenance are mandatory."], "G2 · CRAFT QC", "Picture · audio · campaign assets · telemetry", "Rerender, rerecord or restage failed lane.", parallel=True),
            phase("Post-production", ["Editor builds picture-lock candidate.", "Grade, VFX and final sound converge.", "TrailerEditor/social cutdowns run in parallel."], ["video.editor", "video.colorist", "video.soundmixer", "video.trailereditor", "video.socialmediastrategist"], ["Sample clearance precedes master.", "Full QC mesh spans picture and sound."], "G3 · POST MASTER", "Picture lock · final mix · trailer/social assets", "Return only failed post/campaign asset.", parallel=True),
            phase("Review & release", ["Legal/Compliance clear rights and claims.", "DeepfakeDetection screens synthetic identity.", "Judge/GateKeeper consolidate strict L2."], ["video.legal", "video.compliance", "video.deepfakedetection", "video.judge", "video.gatekeeper"], ["Rights + deepfake HiTL is required.", "Blocked sample or identity halts release."], "G4 · RELEASE", "Clearance · strict L2 · provenance · sign-off", "Route rights, identity or craft issue."),
            phase("Distribution", ["LabelDigital and Distributor fan out packages.", "Marketing/social schedule campaign assets.", "Validate every outlet and territory."], ["video.labeldigital", "video.distributor", "video.marketing", "video.channelmanager", "video.socialmediastrategist"], ["Multi-outlet packaging is parallel.", "Failed branch does not invalidate ready branches."], "G5 · CHANNEL", "Label · platform · campaign · archive packages", "Repackage failed outlet only.", parallel=True),
            phase("Post-launch learning", ["Analyst measures outcome and cost.", "ROAS/Retention optimizers evaluate campaign.", "Community signals feed the next plan."], ["video.analyst", "video.roasoptimizer", "video.retentionoptimizer", "video.community", "video.memory"], ["EvaluationHarness checks regressions.", "No automatic live policy promotion."], "OBSERVE", "Performance · cost · community · optimization tickets", "Feed tested results into next premium plan.", feedback_kind="learning"),
        ],
    ),
    diagram(
        "scale", "s5", "Large Production", "$200K–$50M · ~75–95 agents · 2–12 months",
        "Coordinate multiple concurrent production units, merge gates, live analytics and heavy multi-branch delivery.",
        "Live or live-to-tape, sports/concert highlight factory, awards show or multi-region campaign.",
        "E/I/G composition on E2E/spine DNA",
        "Explicit S5 Unit A ∥ Unit B ∥ Unit C flow from the production scale framework.",
        "L1 required; strict L2; live-safety HiTL; multi-unit merge gates; broadcast/stream/social/archive.",
        ["Scale S5", "~75–95 agents", "3+ units", "live safety"],
        [
            phase("Greenlight", ["Planner builds integrated production calendar.", "Producer approves unit scope, budget and rights.", "Define production ID and segment merge rules."], ["video.planner", "video.producer", "video.finance", "video.orchestrator", "video.legal"], ["Set scale_profile=S5.", "Formal HiTL covers safety/rights segments."], "G0 · GREENLIGHT", "Calendar · unit plan · budget · rights · merge rules", "Reduce unit scope or clear blocked segment."),
            phase("Pre-production", ["Design stage, field and social-desk units.", "Prepare segment briefs and shared continuity.", "Plan live comms, safety and fallback assets."], ["video.showrunner", "video.director", "video.continuity", "video.comms", "video.trustsafety"], ["L1 validates every segment and handoff.", "Memory shares facts across unit DAGs."], "G1 · L1 SPEC", "Unit briefs · segment map · continuity · fallbacks", "Return failed unit or segment plan."),
            phase("Production", ["Unit A runs stage production.", "Unit B runs field/live capture.", "Unit C runs social/highlight desk."], ["video.cameraoperator", "video.dronepilot", "video.sportsanalyst", "video.promptengineer", "video.aiqaconsistency", "video.socialmediastrategist"], ["Orchestrator runs concurrent unit DAGs.", "Merge gates occur at segment boundaries."], "G2 · UNIT MERGE", "Stage · field · social unit outputs · telemetry", "Retry failed unit; preserve accepted segments.", parallel=True),
            phase("Post-production", ["Editor assembles multiple timelines.", "Picture, sound and graphics finish segments.", "AudienceSim tests every major segment."], ["video.editor", "video.colorist", "video.soundmixer", "video.motiongraphics", "video.audiencesim"], ["Segment IDs preserve unit provenance.", "Live deadlines use prepared fallbacks."], "G3 · POST MERGE", "Multi-timeline master · segment QC · fallbacks", "Fix failed segment or merge only.", parallel=True),
            phase("Review & release", ["Standards, Legal and TrustSafety review.", "AudienceSim/Analyst check major segments.", "HiTL resolves live safety and rights."], ["video.standardseditor", "video.legal", "video.trustsafety", "video.audiencesim", "video.judge"], ["Strict L2 and multi-unit merge gates.", "Blocker halts affected segment/branch."], "G4 · RELEASE", "Segment sign-offs · safety/rights · provenance", "Route issue to exact unit/segment."),
            phase("Distribution", ["Fan out broadcast package.", "Fan out streaming/social packages.", "Create archive and campaign/sales assets."], ["video.distributor", "video.channelmanager", "video.archivemaster", "video.sales", "video.crm", "video.awardsstrategist"], ["Broadcast, stream, social and archive are explicit.", "Branches advance independently."], "G5 · CHANNEL", "Broadcast · stream · social · archive packages", "Repackage failed branch or territory.", parallel=True),
            phase("Post-launch learning", ["Live analytics scores produced segments.", "Planner reprioritizes remaining segments.", "Comms/Community track reputation signals."], ["video.analyst", "video.planner", "video.community", "video.comms", "video.memory"], ["Reprioritization affects unproduced work only.", "Systemic changes require regression evidence."], "OBSERVE", "Live analytics · reprioritized plan · tickets", "Feed validated data into remaining/future segments.", feedback_kind="learning"),
        ],
    ),
    diagram(
        "scale", "s6", "Very Large Production", "$300K–$30M · ~90–110 agents · 3–24 months",
        "Run a research/archive-heavy production with continuous facts, dual rights/ethics clearance and mandatory corrections.",
        "Documentary, docuseries, historical/scientific limited series and multilingual global launch.",
        "I Documentary / E docu-drama DNA",
        "Explicit S6 research-before-greenlight and corrections flow from the production scale framework.",
        "L1 required; strict L2; ethics + corrections HiTL; continuous fact mesh; archive/rights heavy.",
        ["Scale S6", "~90–110 agents", "fact mesh", "3–24 months"],
        [
            phase("Greenlight", ["Research track starts before full approval.", "Define thesis, archive scope and territories.", "Producer/Finance/Legal/Ethics approve."], ["video.planner", "video.producer", "video.finance", "video.legal", "video.ethics"], ["Dual clearance: rights and portrayal ethics.", "Set scale_profile=S6 after research framing."], "G0 · DUAL CLEARANCE", "Research brief · budget · rights · ethics record", "Revise thesis, rights or portrayal plan."),
            phase("Pre-production", ["WebResearch and ArchiveResearch build catalog.", "Journalist/Screenwriter create treatment.", "FactChecker/Citation establish continuous mesh."], ["video.webresearch", "video.archiveresearch", "video.journalist", "video.screenwriter", "video.factchecker", "video.citation"], ["L1 requires source and archive traceability.", "Memory stores SourceCatalog and consent."], "G1 · L1 SPEC", "SourceCatalog · treatment · evidence · archive plan", "Return unsupported claim or unclear source."),
            phase("Production", ["Director/DoP capture programme material.", "ArchiveProducer integrates cleared sources.", "InterviewSynthesis and facts follow every handoff."], ["video.director", "video.cinematographer", "video.archiveproducer", "video.interviewsynthesis", "video.factchecker"], ["Continuous fact mesh remains active.", "Targeted pickups preserve evidence lineage."], "G2 · FACT + CRAFT", "Footage · interviews · archive inserts · evidence", "Pickup, reclear or correct failed material."),
            phase("Post-production", ["Editor and VO build final narrative.", "Color/sound/accessibility/localization finish.", "Source map remains attached to timeline."], ["video.editor", "video.voiceover", "video.colorist", "video.soundmixer", "video.accessibility", "video.localizationqa"], ["Long post preserves claim/source alignment.", "Check multilingual and cultural authenticity."], "G3 · POST MASTER", "Programme master · stems · captions · source map", "Fix context, edit, audio or localization defect.", parallel=True),
            phase("Review & release", ["FactChecker closes final claim set.", "Legal, StandardsEditor and Ethics gate.", "Judge/GateKeeper resolve evidence disputes."], ["video.factchecker", "video.legal", "video.standardseditor", "video.ethics", "video.gatekeeper"], ["Strict L2 + ethics/corrections HiTL.", "Open factual or portrayal blocker halts."], "G4 · RELEASE", "Fact/legal/ethics pack · provenance · sign-off", "Route issue to exact evidence or edit."),
            phase("Distribution", ["Package channel and SEO releases.", "Build multilingual/territorial variants.", "ArchiveMaster creates preservation package."], ["video.channelmanager", "video.seo", "video.distributor", "video.localizationqa", "video.archivemaster"], ["Rights follow every territory and source asset.", "Archive integrity is mandatory."], "G5 · CHANNEL", "Channel · multilingual · archive packages", "Repackage or reclear failed endpoint.", parallel=True),
            phase("Post-launch learning", ["Corrections pipeline is mandatory.", "Analyst tracks response and defects.", "Create benchmark and distillation tickets."], ["video.corrections", "video.analyst", "video.evaluationharness", "video.benchmarkresearch", "video.memory"], ["Correction notices preserve version history.", "Learning is evidence-backed and tested."], "OBSERVE", "Corrections · telemetry · distillation tickets", "Feed validated research into future work.", feedback_kind="learning"),
        ],
    ),
    diagram(
        "scale", "s7", "Premium / Cinematic Production", "$5M–$500M · phased full 114-agent pool · 6–60 months",
        "Operate a feature-scale programme with formal human governance, parallel VFX, multi-territory release and long-tail learning.",
        "Feature, animated feature, epic or sci-fi with high-risk IP/likeness and theatrical+stream+broadcast+archive.",
        "J Feature + Delivery + E2E DNA",
        "Explicit S7 feature workflow and phase crew lists from the production scale framework.",
        "Full L1/L2/L3; hard phase gates; consent, ethics, MPA and final human board; full QC and festival simulation.",
        ["Scale S7", "phased 114 pool", "formal board", "6–60 months"],
        [
            phase("Greenlight", ["Run IP, rights, likeness and ethics intake.", "Develop writers-room and concept package.", "Formal board approves budget and slate."], ["video.screenwriter", "video.producer", "video.director", "video.legal", "video.ethics", "video.finance"], ["GateKeeper + human hard-gate every phase.", "Tools require separate production activation."], "G0 · FORMAL BOARD", "IP intake · development pack · GreenlightPacket", "Return IP, consent, budget or story issue."),
            phase("Pre-production", ["Build boards, design, costume and world bible.", "Create character/reference banks for principals.", "Store schedule and continuity state in Memory."], ["video.storyboard", "video.productiondesign", "video.costumedesign", "video.mua_makeup", "video.worldbuilding", "video.continuity"], ["L1 requires full sequence and reference coverage.", "Principal cast consent is mandatory."], "G1 · L1 SPEC", "Pre-production bible · banks · sequence schedule", "Return failed design, sequence or consent item.", parallel=True),
            phase("Production", ["Run phased per-sequence picture DAGs.", "Run voice/music/lip-sync audio in parallel.", "AIQA/Continuity/VFX gate every sequence."], ["video.promptengineer", "video.cinematographer", "video.cameraoperator", "video.voiceclone", "video.lipsync", "video.aiqaconsistency"], ["Nearly full roster is phased, not simultaneous.", "Every sequence emits telemetry/provenance."], "G2 · SEQUENCE QC", "Sequence takes · audio · QA · telemetry", "Rerender/rerecord failed dependency only.", parallel=True),
            phase("Post-production", ["Assemble feature edit and parallel VFX.", "Complete grade, sound design and final mix.", "Develop trailers and campaign assets."], ["video.editor", "video.vfxsupervisor", "video.colorist", "video.sounddesign", "video.soundmixer", "video.trailereditor"], ["Strict L2 and full delivery QC mesh.", "Picture/sound/campaign converge on master."], "G3 · POST MASTER", "Feature master · stems · VFX · trailers · QC", "Return failed picture, sound or campaign asset.", parallel=True),
            phase("Review & release", ["AudienceSim/Critic run preference and jury tests.", "MPA, Legal/C2PA, Ethics and Compliance gate.", "Final human release board resolves risks."], ["video.audiencesim", "video.critic", "video.mpa", "video.legal", "video.ethics", "video.gatekeeper"], ["Full L1/L2/L3 and formal HiTL.", "Consent, rating, ethics and legal are hard."], "G4 · RELEASE BOARD", "C2PA pack · rating · sign-off · risk log", "Route notes to the exact sequence/phase.", parallel=True),
            phase("Distribution", ["Sales/Distributor build multi-territory packages.", "Fan theatrical, stream, broadcast and archive.", "Run trailer/marketing/festival/awards in parallel."], ["video.sales", "video.distributor", "video.marketing", "video.archivemaster", "video.festivalstrategist", "video.awardsstrategist"], ["Every territory/outlet has independent readiness.", "Awards/festival strategy begins early."], "G5 · CHANNEL MATRIX", "DCP · stream · broadcast · archive · campaigns", "Repackage failed territory or outlet only.", parallel=True),
            phase("Post-launch learning", ["Track years-long audience, awards and defects.", "Run evaluation/prompt/routing regressions.", "Issue corrections and canary improvements."], ["video.analyst", "video.evaluationharness", "video.promptoptimizer", "video.corrections", "video.memory"], ["High-risk changes require canary rollout.", "Never silently replace released masters."], "OBSERVE", "Long-tail telemetry · corrections · learning tickets", "Feed tested findings into future development.", feedback_kind="learning"),
        ],
    ),
]

ALL_DIAGRAMS = TEMPLATES + SCALES


def esc(value):
    return html.escape(str(value), quote=True)


def wrap(value, width=72, limit=None):
    """Wrap visible copy without ever dropping source information."""
    lines = textwrap.wrap(str(value), width=width, break_long_words=False, break_on_hyphens=False) or [""]
    if limit is not None and len(lines) > limit:
        raise ValueError(f"Text needs {len(lines)} lines but only {limit} are available: {value}")
    return lines


def text_lines(parts, css_class, x, y, lines, dy=30, prefix=""):
    for index, line in enumerate(lines):
        parts.append(f'<text class="{css_class}" x="{x}" y="{y + index * dy}">{esc(prefix + line)}</text>')


def agent_link(parts, agent_id, x, y, width=650):
    safe = esc(agent_id)
    parts.append(
        f'<a class="agent-link" href="/agents/{safe}/chat" target="_top" aria-label="Open {safe} Chat">'
        f'<rect class="agent-hit" x="{x - 12}" y="{y - 21}" width="{width}" height="27" rx="8"/>'
        f'<text class="agent-text" data-agent-id="{safe}" x="{x}" y="{y}">• {safe}  ↗</text></a>'
    )


def render_card(parts, css_class, x, y, width, height, title, lines, *, line_class="small"):
    accent_class = {
        "card-blue": "accent-blue",
        "card-purple": "accent-purple",
        "card-green": "accent-green",
        "card-amber": "accent-amber",
        "card-rose": "accent-rose",
    }.get(css_class, "accent-neutral")
    parts.append('<g class="content-card">')
    parts.append(f'<rect class="{css_class}" x="{x}" y="{y}" width="{width}" height="{height}" rx="18"/>')
    parts.append(f'<rect class="card-accent {accent_class}" x="{x + 1}" y="{y + 1}" width="{width - 2}" height="8" rx="4"/>')
    parts.append(f'<text class="card-title" x="{x + 28}" y="{y + 45}">{esc(title)}</text>')
    text_lines(parts, line_class, x + 28, y + 82, lines, 31)
    parts.append("</g>")


def render_phase(parts, item, index, y):
    phase_data = item["phases"][index]
    slug = item["slug"]
    label_id = f"{slug}-phase-{index}-label"
    bg = "phase-bg" if index % 2 == 0 else "phase-bg-alt"
    chip = (
        "phase-chip",
        "phase-chip-purple",
        "phase-chip-green",
        "phase-chip-amber",
        "phase-chip-rose",
        "phase-chip-green",
        "phase-chip",
    )[index]
    gate_center_y = y + 482
    card_y = y + 170
    parts.append(
        f'<g id="{slug}-phase-{index}" role="group" aria-labelledby="{label_id}" '
        f'data-phase-index="{index}" data-phase-name="{esc(phase_data["name"].lower().replace(" ", "-"))}">'
    )
    parts.append(f'<rect class="{bg}" x="40" y="{y}" width="3120" height="{PHASE_HEIGHT}" rx="24"/>')
    parts.append(f'<rect class="{chip}" x="40" y="{y + 22}" width="8" height="516" rx="4"/>')
    parts.append(f'<rect class="{chip}" x="70" y="{y + 28}" width="64" height="64" rx="18"/>')
    parts.append(f'<text class="phase-num" x="91" y="{y + 73}">{index}</text>')
    parts.append(f'<text id="{label_id}" class="phase-name" x="158" y="{y + 59}">{esc(phase_data["name"])}</text>')
    mode_label = "PARALLEL FAN-OUT / FAN-IN" if phase_data["parallel"] else "GOVERNED SEQUENCE"
    parts.append(
        f'<text class="phase-count" x="158" y="{y + 89}">{mode_label} · TYPED ARTIFACT HANDOFF · BOUNDED REWORK</text>'
    )

    if phase_data["parallel"]:
        parts.append(f'<polygon class="parallel" points="1600,{y + 90} 1646,{y + 136} 1600,{y + 182} 1554,{y + 136}"/>')
        parts.append(f'<text class="parallel-symbol" x="1600" y="{y + 146}">+</text>')
        for center in (540, 1540, 2540):
            parts.append(f'<path class="branch" data-flow-kind="branch" d="M1600 {y + 182} L{center} {card_y - 14}"/>')
    else:
        parts.append(f'<circle class="phase-start" cx="1600" cy="{y + 132}" r="20"/>')
        parts.append(f'<path class="flow" data-flow-kind="sequence" d="M1600 {y + 152} V{y + 158} H540 V{card_y - 14}"/>')

    card_x = (80, 1080, 2080)
    card_w = 920
    card_h = 240
    card_classes = ("card-blue", "card-purple", "card-green")

    render_card(
        parts,
        card_classes[0],
        card_x[0],
        card_y,
        card_w,
        card_h,
        "Work package",
        [f"• {line}" for line in phase_data["work"]],
        line_class="small",
    )

    parts.append('<g class="content-card">')
    parts.append(
        f'<rect class="{card_classes[1]}" x="{card_x[1]}" y="{card_y}" width="{card_w}" height="{card_h}" rx="18"/>'
    )
    parts.append(
        f'<rect class="card-accent accent-purple" x="{card_x[1] + 1}" y="{card_y + 1}" width="{card_w - 2}" height="8" rx="4"/>'
    )
    parts.append(f'<text class="card-title" x="{card_x[1] + 28}" y="{card_y + 45}">Principal crew</text>')
    for agent_index, agent_id in enumerate(phase_data["agents"]):
        agent_link(parts, agent_id, card_x[1] + 28, card_y + 83 + agent_index * 28, card_w - 56)
    parts.append("</g>")

    render_card(
        parts,
        card_classes[2],
        card_x[2],
        card_y,
        card_w,
        card_h,
        "Control and acceptance",
        [f"• {line}" for line in phase_data["control"]],
        line_class="small",
    )

    if phase_data["parallel"]:
        for center in (540, 1540, 2540):
            parts.append(
                f'<path class="branch" data-flow-kind="branch" d="M{center} {card_y + card_h} V{y + 427} H1600"/>'
            )
    else:
        parts.append(f'<path class="flow" data-flow-kind="sequence" d="M1000 {card_y + 120} H1065"/>')
        parts.append(f'<path class="flow" data-flow-kind="sequence" d="M2000 {card_y + 120} H2065"/>')
        parts.append(f'<path class="flow" data-flow-kind="sequence" d="M2540 {card_y + card_h} V{y + 427} H1600"/>')

    parts.append(
        f'<polygon class="gateway" data-gate="{esc(phase_data["gate"])}" '
        f'points="1600,{gate_center_y - 55} 1655,{gate_center_y} 1600,{gate_center_y + 55} 1545,{gate_center_y}"/>'
    )
    gate_lines = wrap(phase_data["gate"], 18, 2)
    if len(gate_lines) == 1:
        parts.append(f'<text class="gateway-text" x="1600" y="{gate_center_y + 6}">{esc(gate_lines[0])}</text>')
    else:
        parts.append(f'<text class="gateway-text" x="1600" y="{gate_center_y - 3}">{esc(gate_lines[0])}</text>')
        parts.append(f'<text class="gateway-sub" x="1600" y="{gate_center_y + 19}">{esc(gate_lines[1])}</text>')

    parts.append(f'<path class="association" data-flow-kind="artifact" d="M1655 {gate_center_y} H1875"/>')
    parts.append(f'<rect class="artifact" x="1900" y="{y + 426}" width="1130" height="108" rx="14"/>')
    parts.append(f'<text class="label" x="1928" y="{y + 458}">HANDOFF / OUTPUT</text>')
    text_lines(parts, "small", 1928, y + 492, wrap(phase_data["output"], 70, 2), 27)

    feedback_class = phase_data["feedback_kind"]
    parts.append(
        f'<path class="{feedback_class}" data-flow-kind="{feedback_class}" '
        f'd="M1545 {gate_center_y} C1050 {y + 551} 65 {y + 551} 65 {card_y + 120} H80"/>'
    )
    parts.append(f'<text class="feedback-label" x="120" y="{y + 544}">{esc(phase_data["feedback"])}</text>')
    parts.append("</g>")


def render_svg(item):
    slug = item["slug"]
    title_id = f"{slug}-title"
    desc_id = f"{slug}-desc"
    unique_agents = sorted({agent for p in item["phases"] for agent in p["agents"]} | {
        "video.planner", "video.producer", "video.orchestrator", "video.router", "video.memory", "video.judge", "video.gatekeeper", "video.evaluationharness"
    })
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}" preserveAspectRatio="xMinYMin meet" lang="en" role="img" aria-labelledby="{title_id} {desc_id}" data-diagram-id="{slug}" data-diagram-kind="{item["kind"]}" data-code="{item["code"]}" data-agent-count="{len(unique_agents)}" data-schema-version="1" data-visual-system="casops-workflow-v2">',
        f'<title id="{title_id}">Video {esc(item["kind"].title())} {esc(item["code"])} BPM workflow — {esc(item["title"])}</title>',
        f'<desc id="{desc_id}">Seven-phase governed video production BPM workflow for {esc(item["title"])}. It shows greenlight, pre-production, production, post, release review, distribution, post-launch learning, quality gates, typed artifacts, principal agents, targeted rework, and fail-closed runtime status.</desc>',
        f'<metadata>Generated from spec/production_scale_framework.md. Visual system follows ui/public/svg/video.workflow.svg. Evidence basis: {esc(item["basis"])} Runtime remains fail-closed; capability maps do not activate tools, network, or production.</metadata>',
        '<defs>',
        '<style><![CDATA[',
        f'''
          svg{{background:#f4f7fb;text-rendering:optimizeLegibility}}
          .canvas{{fill:#f4f7fb}}
          .header-title{{font:750 52px 'Segoe UI',Arial,sans-serif;fill:#ffffff;letter-spacing:-.7px}}
          .header-sub{{font:450 22px 'Segoe UI',Arial,sans-serif;fill:#cbd5e1}}
          .header-note{{font:650 18px 'Segoe UI',Arial,sans-serif;fill:#78350f}}
          .stat{{font:700 17px 'Segoe UI',Arial,sans-serif;fill:#ffffff;letter-spacing:.15px}}
          .section-title{{font:750 31px 'Segoe UI',Arial,sans-serif;fill:#0f172a;letter-spacing:-.25px}}
          .section-sub{{font:450 18px 'Segoe UI',Arial,sans-serif;fill:#475569}}
          .phase-num{{font:800 36px 'Segoe UI',Arial,sans-serif;fill:#ffffff}}
          .phase-name{{font:750 30px 'Segoe UI',Arial,sans-serif;fill:#0f172a;letter-spacing:-.2px}}
          .phase-count{{font:700 16px 'Segoe UI',Arial,sans-serif;fill:#526176;letter-spacing:.8px}}
          .card-title{{font:700 21px 'Segoe UI',Arial,sans-serif;fill:#172033}}
          .small{{font:500 18px 'Segoe UI',Arial,sans-serif;fill:#405066}}
          .tiny{{font:450 15px 'Segoe UI',Arial,sans-serif;fill:#64748b}}
          .label{{font:750 16px 'Segoe UI',Arial,sans-serif;fill:#334155;letter-spacing:.65px}}
          .agent-text{{font:650 18px 'Segoe UI',Arial,sans-serif;fill:#1d4ed8;text-decoration:underline;text-decoration-color:#bfdbfe}}
          .agent-link{{cursor:pointer;text-decoration:none;outline:none}}
          .agent-hit{{fill:#eff6ff;stroke:#dbeafe;stroke-width:1;opacity:.9;vector-effect:non-scaling-stroke}}
          .agent-link:hover .agent-hit,.agent-link:focus .agent-hit{{fill:#dbeafe;stroke:#60a5fa;stroke-width:2}}
          .agent-link:hover .agent-text,.agent-link:focus .agent-text{{fill:#1e40af;text-decoration-color:#60a5fa}}
          .gateway-text{{font:800 15px 'Segoe UI',Arial,sans-serif;fill:#78350f;text-anchor:middle}}
          .gateway-sub{{font:750 13px 'Segoe UI',Arial,sans-serif;fill:#78350f;text-anchor:middle}}
          .parallel-symbol{{font:800 30px 'Segoe UI',Arial,sans-serif;fill:#3730a3;text-anchor:middle}}
          .feedback-label{{font:700 16px 'Segoe UI',Arial,sans-serif;fill:#b42318}}
          .phase-bg{{fill:#ffffff;stroke:#d8e1ec;stroke-width:2;filter:url(#{slug}-panel-shadow)}}
          .phase-bg-alt{{fill:#f8fafc;stroke:#d8e1ec;stroke-width:2;filter:url(#{slug}-panel-shadow)}}
          .control-bg{{fill:url(#{slug}-control-surface);stroke:#c7d2fe;stroke-width:2;filter:url(#{slug}-panel-shadow)}}
          .card,.card-blue,.card-purple,.card-green,.card-amber,.card-rose{{stroke-width:2;filter:url(#{slug}-shadow);vector-effect:non-scaling-stroke}}
          .card{{fill:#ffffff;stroke:#cbd5e1}}
          .card-blue{{fill:#f8fbff;stroke:#bfdbfe}}
          .card-purple{{fill:#faf9ff;stroke:#ddd6fe}}
          .card-green{{fill:#f7fcfa;stroke:#bbf7d0}}
          .card-amber{{fill:#fffdf7;stroke:#fde68a}}
          .card-rose{{fill:#fff9fa;stroke:#fecdd3}}
          .card-accent{{stroke:none}}
          .accent-blue{{fill:#2563eb}} .accent-purple{{fill:#7c3aed}} .accent-green{{fill:#059669}}
          .accent-amber{{fill:#b45309}} .accent-rose{{fill:#be123c}} .accent-neutral{{fill:#64748b}}
          .artifact{{fill:#ffffff;stroke:#64748b;stroke-width:2;stroke-dasharray:9 7;filter:url(#{slug}-shadow);vector-effect:non-scaling-stroke}}
          .gateway{{fill:#fff7ed;stroke:#d97706;stroke-width:3;filter:url(#{slug}-shadow);vector-effect:non-scaling-stroke}}
          .parallel{{fill:#eef2ff;stroke:#4f46e5;stroke-width:3;filter:url(#{slug}-shadow);vector-effect:non-scaling-stroke}}
          .phase-start{{fill:#ffffff;stroke:#2563eb;stroke-width:4;vector-effect:non-scaling-stroke}}
          .event{{fill:#ffffff;stroke:#2563eb;stroke-width:5;vector-effect:non-scaling-stroke}}
          .end-event-outer{{fill:#ffffff;stroke:#047857;stroke-width:5;vector-effect:non-scaling-stroke}}
          .end-event-inner{{fill:none;stroke:#047857;stroke-width:3;vector-effect:non-scaling-stroke}}
          .flow{{fill:none;stroke:#334155;stroke-width:4;stroke-linecap:round;stroke-linejoin:round;marker-end:url(#{slug}-arrow);vector-effect:non-scaling-stroke}}
          .branch{{fill:none;stroke:#526176;stroke-width:3;stroke-linecap:round;stroke-linejoin:round;marker-end:url(#{slug}-arrow);vector-effect:non-scaling-stroke}}
          .feedback{{fill:none;stroke:#c2413b;stroke-width:3;stroke-linecap:round;stroke-dasharray:12 8;marker-end:url(#{slug}-feedback-arrow);vector-effect:non-scaling-stroke}}
          .learning{{fill:none;stroke:#6d28d9;stroke-width:3;stroke-linecap:round;stroke-dasharray:12 8;marker-end:url(#{slug}-learning-arrow);vector-effect:non-scaling-stroke}}
          .association{{fill:none;stroke:#64748b;stroke-width:2;stroke-linecap:round;stroke-dasharray:5 7;vector-effect:non-scaling-stroke}}
          .phase-chip{{fill:#1d4ed8}} .phase-chip-purple{{fill:#6d28d9}} .phase-chip-green{{fill:#047857}}
          .phase-chip-amber{{fill:#92400e}} .phase-chip-rose{{fill:#9f1239}}
          .runtime-banner{{fill:#fffbeb;stroke:#f59e0b;stroke-width:2;vector-effect:non-scaling-stroke}}
          .legend-line{{stroke:#334155;stroke-width:4;stroke-linecap:round;vector-effect:non-scaling-stroke}}
        ''',
        ']]></style>',
        f'<linearGradient id="{slug}-header-gradient" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0f172a"/><stop offset="0.56" stop-color="#172554"/><stop offset="1" stop-color="#312e81"/></linearGradient>',
        f'<linearGradient id="{slug}-control-surface" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f8fbff"/><stop offset="1" stop-color="#eef2ff"/></linearGradient>',
        f'<filter id="{slug}-panel-shadow" x="-8%" y="-8%" width="116%" height="120%"><feDropShadow dx="0" dy="7" stdDeviation="12" flood-color="#0f172a" flood-opacity="0.07"/></filter>',
        f'<filter id="{slug}-shadow" x="-15%" y="-15%" width="130%" height="140%"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.09"/></filter>',
        f'<marker id="{slug}-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="1.6" markerHeight="1.6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#334155"/></marker>',
        f'<marker id="{slug}-feedback-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="1.6" markerHeight="1.6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#c2413b"/></marker>',
        f'<marker id="{slug}-learning-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="1.6" markerHeight="1.6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#6d28d9"/></marker>',
        '</defs>',
        f'<rect class="canvas" width="{WIDTH}" height="{HEIGHT}"/>',
    ]

    # Header
    parts.extend([
        '<g id="header" role="group" aria-label="Workflow title, profile and runtime status">',
        f'<rect x="0" y="0" width="3200" height="290" fill="url(#{slug}-header-gradient)"/>',
        '<circle cx="2940" cy="-35" r="280" fill="#a5b4fc" opacity="0.10"/>',
        '<circle cx="3120" cy="210" r="190" fill="#38bdf8" opacity="0.07"/>',
        f'<text class="header-title" x="70" y="78">Video {esc(item["kind"].title())} {esc(item["code"])} · {esc(item["title"])} BPM Workflow</text>',
        '<text class="header-sub" x="70" y="120">Shared seven-phase production skeleton · specialized tasks, crew, gates, handoffs and feedback</text>',
    ])
    pill_x = (70, 330, 650, 970)
    pill_w = (230, 290, 290, 390)
    pill_colors = ("#1d4ed8", "#6d28d9", "#047857", "#92400e")
    for idx, stat in enumerate(item["stats"]):
        parts.append(f'<rect x="{pill_x[idx]}" y="143" width="{pill_w[idx]}" height="40" rx="20" fill="{pill_colors[idx]}"/>')
        parts.append(f'<text class="stat" x="{pill_x[idx] + 28}" y="169">{esc(stat)}</text>')
    parts.extend([
        '<rect class="runtime-banner" x="70" y="205" width="3060" height="60" rx="12"/>',
        '<text class="header-note" x="96" y="242">FAIL-CLOSED — This workflow is a capability/scheduling design. It does not activate network, tools, providers or production without separate host and human gates.</text>',
        '</g>',
    ])

    # Summary band
    parts.extend([
        '<g id="workflow-summary" role="group" aria-labelledby="workflow-summary-title">',
        '<rect class="control-bg" x="40" y="320" width="3120" height="380" rx="24"/>',
        '<text id="workflow-summary-title" class="section-title" x="70" y="365">Workflow profile and evidence basis</text>',
        '<text class="section-sub" x="70" y="393">Scale is selected before archetype. Typed handoffs carry correlation, evidence, quality, rights and HiTL state.</text>',
    ])
    summaries = [
        ("card-blue", "Purpose", item["purpose"] + " " + item["use_when"]),
        ("card-purple", "Operating envelope", item["primary"]),
        ("card-green", "DNA / source basis", item["dna"] + ". " + item["basis"]),
        ("card-amber", "Quality posture", item["quality"]),
    ]
    xs = (70, 850, 1630, 2410)
    widths = (730, 730, 730, 720)
    for idx, (cls, title, body) in enumerate(summaries):
        render_card(parts, cls, xs[idx], 420, widths[idx], 230, title, wrap(body, 64, 5), line_class="small")
    parts.append('</g>')

    # Control spine
    parts.extend([
        '<g id="governed-control-spine" role="group" aria-labelledby="governed-control-spine-title">',
        '<rect class="phase-bg" x="40" y="730" width="3120" height="280" rx="24"/>',
        '<text id="governed-control-spine-title" class="section-title" x="70" y="775">Governed control spine</text>',
        '<text class="section-sub" x="70" y="803">Host-owned orchestration, evidence, memory and approvals span all seven phases.</text>',
    ])
    control_cards = [
        ("card-blue", "Plan and greenlight", ["video.planner", "video.producer"]),
        ("card-purple", "Execute and route", ["video.orchestrator", "video.router"]),
        ("card-green", "Memory and evidence", ["video.memory", "video.evaluationharness"]),
        ("card-amber", "Critique and gate", ["video.judge", "video.gatekeeper"]),
    ]
    control_accents = ("accent-blue", "accent-purple", "accent-green", "accent-amber")
    for idx, (cls, title, agents) in enumerate(control_cards):
        x = xs[idx]
        w = widths[idx]
        parts.append(f'<rect class="{cls}" x="{x}" y="835" width="{w}" height="130" rx="18"/>')
        parts.append(f'<rect class="card-accent {control_accents[idx]}" x="{x + 1}" y="836" width="{w - 2}" height="8" rx="4"/>')
        parts.append(f'<text class="card-title" x="{x + 28}" y="878">{esc(title)}</text>')
        for a_idx, agent_id in enumerate(agents):
            agent_link(parts, agent_id, x + 28, 912 + a_idx * 28, w - 56)
    parts.extend(['<path class="association" d="M1600 965 V1020"/>', '</g>'])

    # Phases and inter-phase sequence
    for index, y in enumerate(PHASE_Y):
        render_phase(parts, item, index, y)
        if index < len(PHASE_Y) - 1:
            next_y = PHASE_Y[index + 1]
            parts.append(f'<path class="flow" data-flow-kind="sequence" d="M1600 {y + 537} V{next_y + 74}"/>')

    # Systemic learning loop
    parts.append(f'<path class="learning" data-flow-kind="learning" d="M1545 {PHASE_Y[-1] + 482} C900 5160 25 5160 25 865 H70"/>')
    parts.append('<text class="label" x="90" y="5172" fill="#6d28d9">REGRESSION-TESTED LEARNING → FUTURE PLAN / BRIEF</text>')

    # Footer
    parts.extend([
        '<g id="legend-and-source" role="group" aria-labelledby="legend-and-source-title">',
        f'<rect x="40" y="5220" width="3120" height="410" rx="24" fill="#ffffff" stroke="#d8e1ec" stroke-width="2" filter="url(#{slug}-panel-shadow)"/>',
        '<text id="legend-and-source-title" class="section-title" x="70" y="5265">BPM legend and operating notes</text>',
        '<circle class="event" cx="110" cy="5325" r="18"/><text class="small" x="145" y="5331">event / phase start</text>',
        '<rect class="card" x="430" y="5305" width="80" height="40" rx="9"/><text class="small" x="530" y="5331">task group</text>',
        '<polygon class="gateway" points="760,5305 780,5325 760,5345 740,5325"/><text class="small" x="800" y="5331">quality / decision gate</text>',
        '<polygon class="parallel" points="1130,5305 1150,5325 1130,5345 1110,5325"/><text class="small" x="1170" y="5331">parallel fan-out / fan-in</text>',
        '<line x1="1510" y1="5325" x2="1600" y2="5325" class="legend-line"/><text class="small" x="1620" y="5331">sequence / branch</text>',
        '<line x1="1900" y1="5325" x2="1990" y2="5325" stroke="#c2413b" stroke-width="3" stroke-dasharray="10 7"/><text class="small" x="2010" y="5331">targeted rework</text>',
        '<line x1="2280" y1="5325" x2="2370" y2="5325" stroke="#6d28d9" stroke-width="3" stroke-dasharray="10 7"/><text class="small" x="2390" y="5331">systemic learning</text>',
        '<rect class="artifact" x="2700" y="5305" width="90" height="40" rx="8"/><text class="small" x="2810" y="5331">typed artifact</text>',
        '<rect class="runtime-banner" x="70" y="5370" width="3060" height="92" rx="12"/>',
        '<text class="header-note" x="96" y="5404">HANDOFF CONTRACT — correlation_id · from/to agent · artifact_ref/type · scale · archetype · evidence_refs · L1/L2 · rights_state · needs_hitl</text>',
        '<text class="tiny" x="96" y="5434">Offline/UAT runs also emit knowledge_usage. Crew lists are capability maps; host policy remains authoritative.</text>',
        f'<text class="label" x="70" y="5505">OUTPUT: {esc(item["filename"])}</text>',
        f'<text class="small" x="70" y="5538">Evidence basis: {esc(item["basis"])}</text>',
        '<text class="small" x="70" y="5570">Source: spec/production_scale_framework.md · Style reference: ui/public/svg/video.workflow.svg</text>',
        f'<text class="tiny" x="70" y="5602">Principal unique agents linked in this diagram: {len(unique_agents)} · Seven phases · fail-closed runtime · no automatic scale promotion.</text>',
        '</g>',
    ])

    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def declared_agent_ids():
    ids = set()
    for folder in AGENTS_DIR.glob("video.*"):
        spec = folder / "agent_spec.json"
        if not spec.is_file():
            continue
        ids.add(json.loads(spec.read_text(encoding="utf-8"))["agent_id"])
    return ids


def validate_matrix():
    if len(TEMPLATES) != 10 or len(SCALES) != 7 or len(ALL_DIAGRAMS) != 17:
        raise ValueError("Expected 10 templates, 7 scales, and 17 total diagrams")
    expected_files = {f"video.template.{letter}.workflow.svg" for letter in "abcdefghij"}
    expected_files |= {f"video.scale.s{number}.workflow.svg" for number in range(1, 8)}
    actual_files = {item["filename"] for item in ALL_DIAGRAMS}
    if actual_files != expected_files:
        raise ValueError(f"Filename matrix mismatch: {sorted(actual_files ^ expected_files)}")
    declared = declared_agent_ids()
    used = {agent for item in ALL_DIAGRAMS for p in item["phases"] for agent in p["agents"]}
    used |= {"video.planner", "video.producer", "video.orchestrator", "video.router", "video.memory", "video.judge", "video.gatekeeper", "video.evaluationharness"}
    unknown = sorted(used - declared)
    if unknown:
        raise ValueError(f"Unknown video agents in workflow matrix: {unknown}")
    for item in ALL_DIAGRAMS:
        if len(item["phases"]) != 7:
            raise ValueError(f'{item["filename"]} does not have seven phases')
        for phase_data in item["phases"]:
            if not 1 <= len(phase_data["agents"]) <= 6:
                raise ValueError(
                    f'{item["filename"]} phase {phase_data["name"]} needs 1–6 visible principal agents'
                )


def validate_svg_output(item, target, declared_agents):
    """Validate one rendered SVG against semantics, accessibility, and visual-system contracts."""
    import re

    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    def local_name(node):
        return node.tag.rsplit("}", 1)[-1]

    def normalized(value):
        return " ".join(str(value).split())

    tree = ElementTree.parse(target)
    root = tree.getroot()
    nodes = list(root.iter())
    raw = target.read_text(encoding="utf-8")
    visible_text = normalized("".join(root.itertext()))

    require(local_name(root) == "svg", "root element is not svg")
    require(root.get("viewBox") == f"0 0 {WIDTH} {HEIGHT}", "unexpected viewBox")
    require(root.get("width") == str(WIDTH) and root.get("height") == str(HEIGHT), "unexpected dimensions")
    require(root.get("preserveAspectRatio") == "xMinYMin meet", "unexpected aspect-ratio behavior")
    require(root.get("role") == "img" and root.get("lang") == "en", "missing image role or language")
    require(root.get("data-diagram-id") == item["slug"], "diagram id does not match filename matrix")
    require(root.get("data-diagram-kind") == item["kind"], "diagram kind mismatch")
    require(root.get("data-code") == item["code"], "diagram code mismatch")
    require(root.get("data-schema-version") == "1", "schema version mismatch")
    require(root.get("data-visual-system") == "casops-workflow-v2", "visual-system version mismatch")

    ids = [node.get("id") for node in nodes if node.get("id")]
    duplicate_ids = sorted({node_id for node_id in ids if ids.count(node_id) > 1})
    require(not duplicate_ids, f"duplicate ids: {duplicate_ids}")
    id_map = {node.get("id"): node for node in nodes if node.get("id")}
    labelled_by = root.get("aria-labelledby", "").split()
    require(labelled_by == [f'{item["slug"]}-title', f'{item["slug"]}-desc'], "aria-labelledby mismatch")
    require(all(label in id_map for label in labelled_by), "aria-labelledby contains unresolved ids")
    if labelled_by and all(label in id_map for label in labelled_by):
        require(local_name(id_map[labelled_by[0]]) == "title", "accessible title id is not on title")
        require(local_name(id_map[labelled_by[1]]) == "desc", "accessible description id is not on desc")

    referenced_ids = set(re.findall(r"url\(#([^)]+)\)", raw))
    require(not (referenced_ids - set(ids)), f"unresolved url references: {sorted(referenced_ids - set(ids))}")

    phases = [node for node in nodes if node.get("data-phase-index") is not None]
    expected_phase_indexes = [str(index) for index in range(7)]
    expected_phase_names = [phase_data["name"].lower().replace(" ", "-") for phase_data in item["phases"]]
    require(len(phases) == 7, f"expected 7 phases, found {len(phases)}")
    require([node.get("data-phase-index") for node in phases] == expected_phase_indexes, "phase indexes are not 0 through 6")
    require([node.get("data-phase-name") for node in phases] == expected_phase_names, "phase names do not match the matrix")
    for phase_node in phases:
        descendants = list(phase_node.iter())
        phase_index = phase_node.get("data-phase-index")
        phase_label = phase_node.get("aria-labelledby")
        require(phase_node.get("role") == "group", f"phase {phase_index} is not an accessible group")
        require(bool(phase_label) and phase_label in id_map, f"phase {phase_index} label is unresolved")
        require(
            sum(node.get("data-gate") is not None for node in descendants) == 1,
            f"phase {phase_index} does not have exactly one gate",
        )
        require(
            sum(node.get("data-flow-kind") == "artifact" for node in descendants) == 1,
            f"phase {phase_index} does not have exactly one typed artifact handoff",
        )
        require(any(node.get("data-agent-id") for node in descendants), f"phase {phase_index} has no linked principal crew")
        require(
            any(node.get("data-flow-kind") in {"feedback", "learning"} for node in descendants),
            f"phase {phase_index} has no bounded feedback path",
        )

    flow_kinds = {node.get("data-flow-kind") for node in nodes if node.get("data-flow-kind")}
    required_flow_kinds = {"sequence", "artifact", "feedback", "learning"}
    if any(phase_data["parallel"] for phase_data in item["phases"]):
        required_flow_kinds.add("branch")
    require(required_flow_kinds <= flow_kinds, f"missing BPM flow kinds: {sorted(required_flow_kinds - flow_kinds)}")
    require(sum(node.get("data-gate") is not None for node in nodes) == 7, "expected seven phase gates")
    require(sum(node.get("data-flow-kind") == "artifact" for node in nodes) == 7, "expected seven artifact associations")

    links = [node for node in nodes if local_name(node) == "a"]
    linked_agents = {node.get("data-agent-id") for node in nodes if node.get("data-agent-id")}
    required_controls = {
        "video.planner",
        "video.producer",
        "video.orchestrator",
        "video.router",
        "video.memory",
        "video.judge",
        "video.gatekeeper",
    }
    require(required_controls <= linked_agents, f"missing governed control agents: {sorted(required_controls - linked_agents)}")
    require(linked_agents <= declared_agents, f"unknown linked agents: {sorted(linked_agents - declared_agents)}")
    require(root.get("data-agent-count") == str(len(linked_agents)), "data-agent-count does not match unique linked agents")
    for link in links:
        link_agents = [node.get("data-agent-id") for node in link.iter() if node.get("data-agent-id")]
        hit_targets = [node for node in link.iter() if "agent-hit" in node.get("class", "").split()]
        require(link.get("class") == "agent-link", "interactive link is missing the agent-link class")
        require(link.get("target") == "_top", "interactive link does not preserve standalone navigation")
        require(len(link_agents) == 1, "agent link does not contain exactly one agent id")
        require(len(hit_targets) == 1, "agent link does not contain exactly one enlarged hit target")
        if len(link_agents) == 1:
            agent_id = link_agents[0]
            require(link.get("href") == f"/agents/{agent_id}/chat", f"incorrect chat href for {agent_id}")
            require(bool(link.get("aria-label")), f"missing accessible label for {agent_id}")

    required_text = [
        "FAIL-CLOSED",
        "HANDOFF CONTRACT",
        "Evidence basis:",
        "Source: spec/production_scale_framework.md",
        "Style reference: ui/public/svg/video.workflow.svg",
        "typed artifact",
        "bounded rework",
        "systemic learning",
        "rights_state",
        "needs_hitl",
        item["filename"],
        item["primary"],
        item["purpose"],
        item["use_when"],
        item["dna"],
        item["basis"],
        item["quality"],
        *item["stats"],
    ]
    for phase_data in item["phases"]:
        required_text.extend(
            [
                phase_data["name"],
                *phase_data["work"],
                *phase_data["agents"],
                *phase_data["control"],
                phase_data["gate"],
                phase_data["output"],
                phase_data["feedback"],
            ]
        )
    lower_visible_text = visible_text.lower()
    for text in required_text:
        require(normalized(text).lower() in lower_visible_text, f"missing source information: {text}")

    style_nodes = [node for node in nodes if local_name(node) == "style"]
    css = "\n".join(node.text or "" for node in style_nodes)
    required_style_tokens = [
        "Segoe UI",
        "text-rendering:optimizeLegibility",
        ".canvas{fill:#f4f7fb}",
        ".header-title{font:750 52px",
        ".phase-bg{fill:#ffffff",
        ".card-blue{fill:#f8fbff",
        ".agent-hit{fill:#eff6ff",
        ".gateway{fill:#fff7ed;stroke:#d97706",
        ".parallel{fill:#eef2ff;stroke:#4f46e5",
        ".feedback{fill:none;stroke:#c2413b",
        ".learning{fill:none;stroke:#6d28d9",
        ".artifact{fill:#ffffff;stroke:#64748b",
        "vector-effect:non-scaling-stroke",
        "stroke-dasharray",
    ]
    for token in required_style_tokens:
        require(token in css, f"missing professional visual-system token: {token}")

    if errors:
        raise ValueError(f"{target.name}: " + "; ".join(errors))


def validate_main_svg(target, declared_agents):
    """Validate the hand-maintained 114-agent master workflow."""
    import re

    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    def local_name(node):
        return node.tag.rsplit("}", 1)[-1]

    root = ElementTree.parse(target).getroot()
    nodes = list(root.iter())
    raw = target.read_text(encoding="utf-8")
    visible_text = " ".join("".join(root.itertext()).split())
    ids = [node.get("id") for node in nodes if node.get("id")]
    id_map = {node.get("id"): node for node in nodes if node.get("id")}

    require(local_name(root) == "svg", "root element is not svg")
    require(root.get("viewBox") == f"0 0 {WIDTH} {HEIGHT}", "unexpected viewBox")
    require(root.get("preserveAspectRatio") == "xMinYMin meet", "unexpected aspect-ratio behavior")
    require(root.get("role") == "img" and root.get("lang") == "en", "missing image role or language")
    require(root.get("data-diagram-id") == "video-main-workflow", "main diagram id mismatch")
    require(root.get("data-diagram-kind") == "main", "main diagram kind mismatch")
    require(root.get("data-agent-count") == "114" and root.get("data-video-agent-count") == "114", "main agent count metadata mismatch")
    require(root.get("data-visual-system") == "casops-workflow-v2", "visual-system version mismatch")
    require(len(ids) == len(set(ids)), "duplicate ids are present")
    labelled_by = root.get("aria-labelledby", "").split()
    require(labelled_by == ["workflow-title", "workflow-desc"], "aria-labelledby mismatch")
    require(all(label in id_map for label in labelled_by), "aria-labelledby contains unresolved ids")
    referenced_ids = set(re.findall(r"url\(#([^)]+)\)", raw))
    require(not (referenced_ids - set(ids)), f"unresolved url references: {sorted(referenced_ids - set(ids))}")

    links = [node for node in nodes if local_name(node) == "a"]
    link_agents = []
    for link in links:
        nested_agents = [node.get("data-agent-id") for node in link.iter() if node.get("data-agent-id")]
        require(link.get("class") == "agent-link", "interactive link is missing the agent-link class")
        require(link.get("target") == "_top", "interactive link does not preserve standalone navigation")
        require(len(nested_agents) == 1, "agent link does not contain exactly one agent id")
        if len(nested_agents) == 1:
            agent_id = nested_agents[0]
            link_agents.append(agent_id)
            require(link.get("href") == f"/agents/{agent_id}/chat", f"incorrect chat href for {agent_id}")
            require(bool(link.get("aria-label")), f"missing accessible label for {agent_id}")
    require(len(link_agents) == 114, f"expected 114 linked agents, found {len(link_agents)}")
    require(len(set(link_agents)) == 114, "main workflow contains duplicate agent links")
    require(set(link_agents) <= declared_agents, f"unknown linked agents: {sorted(set(link_agents) - declared_agents)}")

    for text in [
        "All 114 CASOPS video agents",
        "STATUS NOTE",
        "Principal placement avoids duplicate roster entries",
        "cross-cutting 28 + development 16 + pre-production 12 + production 17 + post 11 + review 13 + distribution 14 + post-release 3 = 114",
        "Sources: video agent SPECs",
    ]:
        require(text.lower() in visible_text.lower(), f"missing main workflow information: {text}")

    style_nodes = [node for node in nodes if local_name(node) == "style"]
    css = "\n".join(node.text or "" for node in style_nodes)
    for token in [
        "text-rendering:optimizeLegibility",
        ".canvas{fill:#f4f7fb}",
        ".header-title{font:750 52px",
        ".agent-list .agentline{fill:#1d4ed8",
        ".phase-bg{fill:#ffffff",
        ".card-blue{fill:#f8fbff",
        "vector-effect:non-scaling-stroke",
    ]:
        require(token in css, f"missing main visual-system token: {token}")

    if errors:
        raise ValueError(f"{target.name}: " + "; ".join(errors))


def validate_generated_set(expected_files):
    generated = {
        path.name
        for pattern in ("video.template.*.workflow.svg", "video.scale.*.workflow.svg")
        for path in OUT_DIR.glob(pattern)
    }
    if generated != expected_files:
        raise ValueError(f"Generated output set mismatch: {sorted(generated ^ expected_files)}")
    expected_all = expected_files | {"video.workflow.svg"}
    actual_all = {path.name for path in OUT_DIR.glob("*.svg")}
    if actual_all != expected_all:
        raise ValueError(f"SVG directory inventory mismatch: {sorted(actual_all ^ expected_all)}")


def main():
    validate_matrix()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    declared_agents = declared_agent_ids()
    expected_files = {item["filename"] for item in ALL_DIAGRAMS}
    for item in ALL_DIAGRAMS:
        target = OUT_DIR / item["filename"]
        target.write_text(render_svg(item), encoding="utf-8")
        validate_svg_output(item, target, declared_agents)
        print(target.relative_to(ROOT))
    main_svg = OUT_DIR / "video.workflow.svg"
    validate_main_svg(main_svg, declared_agents)
    print(main_svg.relative_to(ROOT))
    validate_generated_set(expected_files)
    print(f"Validated all {len(ALL_DIAGRAMS) + 1} workflow SVGs against the output contract.")


if __name__ == "__main__":
    main()
