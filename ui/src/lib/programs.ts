/** Program Code: lowercase English letters and digits, no spaces. ISSUE-0013 filmmaking fields. */

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

export const SPAWN_LOCKS = ["generation_list", "visual_bible"] as const;

export function normalizeProgramCode(raw: string): string {
  return String(raw || "")
    .toLowerCase()
    .replace(/[^a-z0-9]/g, "");
}

export function programCodeValid(code: string): boolean {
  return /^[a-z][a-z0-9]{0,47}$/.test(code);
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
