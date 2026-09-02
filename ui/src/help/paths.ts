import { HELP_FULL_PAGE_PATH } from "./tabs";

export const HELP_WIDTH_KEY = "casops.control-ui.help-width.v1";
export const HELP_WIDTH_MIN = 280;
export const HELP_WIDTH_MAX = 720;
export const HELP_WIDTH_DEFAULT = 380;
export const HELP_WIDTH_STEP = 16;
export const HELP_WIDTH_STEP_LARGE = 64;

export function normalizePath(pathname: string): string {
  if (!pathname || pathname === "/") {
    return "/";
  }
  const trimmed = pathname.replace(/\/+$/, "");
  return trimmed || "/";
}

export function paramsFromPathname(pathname: string): Record<string, string | undefined> {
  const path = normalizePath(pathname);
  const params: Record<string, string | undefined> = {};
  const agent = /^\/agents\/([^/]+)(?:\/(.*))?$/.exec(path);
  if (agent?.[1]) {
    params.agentId = decodeURIComponent(agent[1]);
    const rest = agent[2] || "";
    const nestedTrace = /^traces\/([^/]+)/.exec(rest);
    if (nestedTrace?.[1]) {
      params.tid = decodeURIComponent(nestedTrace[1]);
    }
  }
  const topTrace = /^\/traces\/([^/]+)$/.exec(path);
  if (topTrace?.[1]) {
    params.tid = decodeURIComponent(topTrace[1]);
  }
  return params;
}

export function stripParamValues(pathname: string, params: Record<string, string | undefined>): string {
  let path = normalizePath(pathname);
  const values = Object.values(params)
    .filter((value): value is string => Boolean(value))
    .sort((left, right) => right.length - left.length);
  for (const value of values) {
    for (const token of [encodeURIComponent(value), value]) {
      path = path.split(`/${token}`).join("");
    }
  }
  return normalizePath(path);
}

export function docCandidates(
  pathname: string,
  params: Record<string, string | undefined>,
  tabId: string,
): string[] {
  const exact = normalizePath(pathname);
  const stripped = stripParamValues(pathname, params);
  const folders = [exact, stripped].filter((folder, index, all) => all.indexOf(folder) === index);
  const files: string[] = [];
  for (const folder of folders) {
    files.push(folder === "/" ? `/docs/${tabId}.md` : `/docs${folder}/${tabId}.md`);
  }
  if (exact === "/") {
    files.push(`/docs/index/${tabId}.md`);
  }
  return [...new Set(files)];
}

export function helpPageFrom(search: string, fallbackPathname: string): string {
  const from = new URLSearchParams(search).get("from");
  if (!from || from === HELP_FULL_PAGE_PATH) {
    return normalizePath(fallbackPathname === HELP_FULL_PAGE_PATH ? "/" : fallbackPathname);
  }
  return normalizePath(from);
}

export function helpPageHref(fromPathname: string, search = ""): string {
  const from = normalizePath(fromPathname);
  if (from === HELP_FULL_PAGE_PATH) {
    return `${HELP_FULL_PAGE_PATH}${search || ""}`;
  }
  return `${HELP_FULL_PAGE_PATH}?from=${encodeURIComponent(from)}`;
}

export function clampHelpWidth(width: number, max = HELP_WIDTH_MAX): number {
  const ceiling = Math.max(HELP_WIDTH_MIN, max);
  if (!Number.isFinite(width)) {
    return HELP_WIDTH_DEFAULT;
  }
  return Math.min(ceiling, Math.max(HELP_WIDTH_MIN, Math.round(width)));
}

export function loadHelpWidth(): number {
  try {
    const raw = localStorage.getItem(HELP_WIDTH_KEY);
    if (!raw) {
      return HELP_WIDTH_DEFAULT;
    }
    return clampHelpWidth(Number(raw));
  } catch {
    return HELP_WIDTH_DEFAULT;
  }
}

export function saveHelpWidth(width: number): void {
  try {
    localStorage.setItem(HELP_WIDTH_KEY, String(clampHelpWidth(width)));
  } catch {
    // ignore quota / private-mode failures
  }
}
