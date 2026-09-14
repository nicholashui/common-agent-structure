const LAST_PROJECT_KEY = "casops.control-ui.last-project.v1";

export function rememberProject(projectId: string): void {
  const id = String(projectId || "").trim();
  if (!id) {
    return;
  }
  try {
    localStorage.setItem(LAST_PROJECT_KEY, id);
  } catch {
    // ignore quota / private mode
  }
}

export function lastProjectId(): string {
  try {
    return localStorage.getItem(LAST_PROJECT_KEY) || "";
  } catch {
    return "";
  }
}

export function projectChatHref(
  projectId: string,
  opts?: { comm?: string; opt?: string; agent?: string },
): string {
  const base = `/projects/${encodeURIComponent(projectId)}/chat`;
  const query = new URLSearchParams();
  if (opts?.comm) {
    query.set("comm", opts.comm);
    if (opts.opt) {
      query.set("opt", opts.opt);
    }
  } else if (opts?.agent) {
    query.set("agent", opts.agent);
  }
  const suffix = query.toString();
  return suffix ? `${base}?${suffix}` : base;
}

export { commIdForAgent } from "./projectChat";

export function agentIdFromProfileChatHref(href: string): string {
  const match = /^\/agents\/([^/]+)\/chat\/?$/.exec(href);
  if (!match) {
    return "";
  }
  try {
    return decodeURIComponent(match[1]);
  } catch {
    return match[1];
  }
}

