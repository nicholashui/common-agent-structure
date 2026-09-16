/** Program Code: lowercase English letters, digits, hyphens; no spaces. ISSUE-0013 filmmaking fields. */

export const PROGRAM_FIRST_CALLED = "video.showrunner";
export const PROGRAM_FIRST_AGENT_HOP = "specials.intent-analysis-agent";
export const PROGRAM_CHILD_FIRST_CALLED = "video.promptengineer";
export const PROGRAM_CHILD_HUMAN_LOCKS = [
  "video.promptengineer",
  "video.director",
  "video.cinematographer",
  "video.mua_makeup",
  "video.continuity",
] as const;

export const PROGRAM_PHASES = [
  { id: "w0", label: "W0 Development" },
  { id: "w1", label: "W1 Literary" },
  { id: "w2", label: "W2 Pre-production" },
  { id: "w3", label: "W3 Spawn" },
  { id: "w4", label: "W4 Production" },
  { id: "w5", label: "W5 Post / NLE" },
  { id: "w6", label: "W6 Delivery" },
] as const;

export const PROGRAM_LOCKS = [
  "logline",
  "pages",
  "generation_list",
  "visual_bible",
  "storyboard",
  "picture",
  "delivery",
] as const;

export const OVERVIEW_PANELS = [
  { id: "phase", label: "Phase", blurb: "W0–W6 stage. First hop intent-analysis; first-called showrunner." },
  { id: "locks", label: "Locks", blurb: "Human + closer gates. Spawn needs generation list and visual bible." },
  { id: "list", label: "Generation list", blurb: "One segment = one Project. Empty scenes cannot lock." },
  { id: "spawn", label: "Spawn", blurb: "Host mkdir one Project per segment after list + bible locks." },
  { id: "bible", label: "Bible", blurb: "Visual bible and storyboard refs. Stills before motion." },
  { id: "cut", label: "Cut", blurb: "Assembly through picture lock. Color/mix/graphics after picture lock." },
  { id: "delivery", label: "Delivery", blurb: "Delivery tree. No live upload. Trailer is not a silent spawn." },
] as const;

export type OverviewPanelId = (typeof OVERVIEW_PANELS)[number]["id"];

export function resolveOverviewPanel(raw: string | null | undefined): OverviewPanelId {
  const id = String(raw || "list");
  return OVERVIEW_PANELS.some((panel) => panel.id === id) ? (id as OverviewPanelId) : "list";
}

export const PROGRAM_LOCK_LABELS: Record<(typeof PROGRAM_LOCKS)[number], string> = {
  logline: "Logline",
  pages: "Pages",
  generation_list: "Generation list",
  visual_bible: "Visual bible",
  storyboard: "Storyboard",
  picture: "Picture lock",
  delivery: "Delivery",
};

export const SPAWN_LOCKS = ["generation_list", "visual_bible"] as const;

export function normalizeProgramCode(raw: string): string {
  return String(raw || "")
    .toLowerCase()
    .trim()
    .replace(/\s+/g, "-")
    .replace(/[^a-z0-9-]+/g, "")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "");
}

export function programCodeValid(code: string): boolean {
  return /^[a-z](?:[a-z0-9-]{0,46}[a-z0-9])?$/.test(code);
}

/** Left-nav label: Program Name as stored (display name). */
export function programNavLabel(item: { name?: string; code?: string; id?: string }): string {
  return String(item.name || item.code || item.id || "").trim();
}

export function spawnReady(locks: Record<string, boolean> | undefined | null): boolean {
  const current = locks || {};
  return Boolean(current.generation_list) && Boolean(current.visual_bible);
}

export function spawnMissingLocks(locks: Record<string, boolean> | undefined | null): string[] {
  const current = locks || {};
  return SPAWN_LOCKS.filter((key) => !current[key]);
}

export function finishReady(locks: Record<string, boolean> | undefined | null): boolean {
  return Boolean(locks?.picture);
}

export const CUT_STATES = ["assembly", "rough", "fine", "picture_lock"] as const;

export function generationListLockable(
  scenes: { id?: string; segments?: unknown[] }[] | undefined | null,
): boolean {
  if (!scenes || scenes.length === 0) {
    return false;
  }
  return scenes.every((scene) => Array.isArray(scene.segments) && scene.segments.length > 0);
}
