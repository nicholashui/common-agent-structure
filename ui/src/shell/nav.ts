export const AGENT_TABS = [
  { id: "overview", label: "Overview", path: "" },
  { id: "chat", label: "Chat", path: "chat" },
  { id: "structure", label: "Structure", path: "structure" },
  { id: "files", label: "Files", path: "files" },
  { id: "compose", label: "Compose", path: "compose" },
  { id: "run", label: "Run", path: "run" },
  { id: "trace", label: "Trace", path: "traces" },
  { id: "capabilities", label: "Capabilities", path: "capabilities" },
  { id: "protocols", label: "Protocols", path: "protocols" },
  { id: "memory", label: "Memory", path: "memory" },
  { id: "plugins", label: "Plugins", path: "plugins" },
  { id: "cache", label: "Cache", path: "cache" },
  { id: "safety", label: "Safety", path: "safety" },
  { id: "improvement", label: "Improvement", path: "improvement" },
  { id: "validation", label: "Validation", path: "validation" },
  { id: "corrigibility", label: "Corrigibility", path: "corrigibility" },
] as const;

export function agentHref(agentId: string, tabPath: string): string {
  const base = `/agents/${encodeURIComponent(agentId)}`;
  return tabPath ? `${base}/${tabPath}` : base;
}

/** Current Agent Profile tab path (chat, files, traces, …). Empty on Overview. */
export function agentTabPath(pathname: string): string {
  const trimmed = pathname.replace(/\/+$/, "") || "/";
  const match = /^\/agents\/[^/]+(?:\/(.*))?$/.exec(trimmed);
  if (!match) {
    return "";
  }
  const rest = match[1] || "";
  if (!rest) {
    return "";
  }
  if (rest === "traces" || rest.startsWith("traces/")) {
    return "traces";
  }
  return rest.split("/")[0] || "";
}

export const HOME_LABEL = "Agent Swarm";
export const APP_NAME = "Common Agents Swarm System (CASS)";
export const PROGRAM_MENU_LABEL = "Program";
export const PROJECT_MENU_LABEL = "Project";
export const AGENT_MENU_LABEL = "Agent Profile";
export const WORKFLOW_MENU_LABEL = "Agent Workflow";
export const WORKFLOW_TABS = [
  { id: "main", label: "Main Workflow", path: "/workflow", depth: 1 },
  { id: "sub", label: "Sub Workflow", path: "/workflow/sub", depth: 2 },
] as const;

export const PROJECT_INSTANCE_TABS = [
  { id: "start", label: "Start", path: "start" },
  { id: "workflow", label: "Workflow", path: "workflow" },
  { id: "chat", label: "Chat", path: "chat" },
] as const;

export const PROGRAM_INSTANCE_TABS = [
  { id: "start", label: "Start", path: "" },
  { id: "workflow", label: "Workflow", path: "workflow" },
  { id: "chat", label: "Chat", path: "chat" },
  { id: "overflow", label: "Overflow", path: "overview" },
] as const;

export function locationLabel(pathname: string): string {
  const trimmed = pathname.replace(/\/+$/, "") || "/";
  if (trimmed === "/") {
    return HOME_LABEL;
  }
  if (trimmed === "/programs/new") {
    return `${PROGRAM_MENU_LABEL} / New program`;
  }
  if (trimmed.startsWith("/programs/")) {
    const rest = decodeURIComponent(trimmed.slice("/programs/".length));
    const [id, tab] = rest.split("/");
    if (tab === "chat") {
      return `${PROGRAM_MENU_LABEL} / ${id} / Chat`;
    }
    if (tab === "workflow") {
      return `${PROGRAM_MENU_LABEL} / ${id} / Workflow`;
    }
    if (tab === "overview" || tab === "overflow") {
      return `${PROGRAM_MENU_LABEL} / ${id} / Overflow`;
    }
    if (tab === "start") {
      return `${PROGRAM_MENU_LABEL} / ${id} / Start`;
    }
    return id ? `${PROGRAM_MENU_LABEL} / ${id} / Start` : PROGRAM_MENU_LABEL;
  }
  if (trimmed === "/programs") {
    return PROGRAM_MENU_LABEL;
  }
  if (trimmed === "/projects/new") {
    return `${PROJECT_MENU_LABEL} / New project`;
  }
  if (trimmed.startsWith("/projects/")) {
    const rest = decodeURIComponent(trimmed.slice("/projects/".length));
    const [id, tab] = rest.split("/");
    if (tab === "chat") {
      return `${PROJECT_MENU_LABEL} / ${id} / Chat`;
    }
    if (tab === "workflow") {
      return `${PROJECT_MENU_LABEL} / ${id} / Workflow`;
    }
    if (tab === "start") {
      return `${PROJECT_MENU_LABEL} / ${id} / Start`;
    }
    return `${PROJECT_MENU_LABEL} / ${id}`;
  }
  if (trimmed === "/projects") {
    return PROJECT_MENU_LABEL;
  }
  if (trimmed === "/org-chat") {
    return `${HOME_LABEL} / Agent Org Chat`;
  }
  if (trimmed === "/workflow" || trimmed.startsWith("/workflow/")) {
    const tab = WORKFLOW_TABS.find((item) => item.path === trimmed);
    if (tab?.id === "sub") {
      return `${HOME_LABEL} / ${WORKFLOW_MENU_LABEL} / Main Workflow / Sub Workflow`;
    }
    return `${HOME_LABEL} / ${WORKFLOW_MENU_LABEL} / ${tab?.label ?? "Main Workflow"}`;
  }
  if (trimmed === "/settings") {
    return `${HOME_LABEL} / Settings`;
  }
  if (trimmed === "/help") {
    return `${HOME_LABEL} / Help`;
  }
  if (trimmed.startsWith("/agents/")) {
    const rest = trimmed.slice("/agents/".length);
    let decoded = rest;
    try {
      decoded = decodeURIComponent(rest);
    } catch {
      decoded = rest;
    }
    const slash = decoded.indexOf("/");
    const id = slash >= 0 ? decoded.slice(0, slash) : decoded;
    const tabPath = slash >= 0 ? decoded.slice(slash + 1) : "";
    if (!id) {
      return `${HOME_LABEL} / ${AGENT_MENU_LABEL}`;
    }
    const tab = AGENT_TABS.find(
      (item) => item.path === tabPath || (item.id === "trace" && tabPath.startsWith("traces")),
    );
    if (tab && tab.path) {
      return `${HOME_LABEL} / ${id} / ${tab.label}`;
    }
    return `${HOME_LABEL} / ${id}`;
  }
  let path = trimmed.replace(/^\//, "");
  try {
    path = decodeURIComponent(path);
  } catch {
    // keep the raw path if it is not valid percent-encoding
  }
  return `${HOME_LABEL} / ${path}`;
}

export const NAV_KEY = "casops.control-ui.nav.v2";

export interface NavChrome {
  collapsed: boolean;
  agentOpen: boolean;
  workflowOpen: boolean;
  programOpen: boolean;
  projectOpen: boolean;
  openProjects: string[];
  openPrograms: string[];
}

export function defaultNavChrome(): NavChrome {
  return {
    collapsed: false,
    agentOpen: false,
    workflowOpen: false,
    programOpen: false,
    projectOpen: false,
    openProjects: [],
    openPrograms: [],
  };
}

export function parseOpenProjects(value: unknown): string[] {
  if (!Array.isArray(value)) {
    return [];
  }
  const out: string[] = [];
  for (const item of value) {
    if (typeof item === "string" && item && !out.includes(item)) {
      out.push(item);
    }
  }
  return out;
}

export function toggleOpenProject(ids: string[], id: string): string[] {
  if (!id) {
    return ids;
  }
  return ids.includes(id) ? ids.filter((item) => item !== id) : [...ids, id];
}

export function ensureOpenProject(ids: string[], id: string): string[] {
  if (!id || ids.includes(id)) {
    return ids;
  }
  return [...ids, id];
}

export function programIdFromPath(pathname: string): string {
  const trimmed = pathname.replace(/\/+$/, "") || "/";
  const match = /^\/programs\/([^/]+)/.exec(trimmed);
  if (!match) {
    return "";
  }
  let id = match[1];
  try {
    id = decodeURIComponent(id);
  } catch {
    // keep the raw segment
  }
  return id === "new" ? "" : id;
}

export function projectIdFromPath(pathname: string): string {
  const trimmed = pathname.replace(/\/+$/, "") || "/";
  const match = /^\/projects\/([^/]+)/.exec(trimmed);
  if (!match) {
    return "";
  }
  let id = match[1];
  try {
    id = decodeURIComponent(id);
  } catch {
    // keep the raw segment
  }
  return id === "new" ? "" : id;
}

export function loadNavChrome(): NavChrome {
  const fallback = defaultNavChrome();
  try {
    const raw = localStorage.getItem(NAV_KEY);
    if (!raw) {
      return fallback;
    }
    const parsed = JSON.parse(raw) as Partial<NavChrome>;
    return {
      collapsed: Boolean(parsed.collapsed),
      agentOpen: Boolean(parsed.agentOpen),
      workflowOpen: Boolean(parsed.workflowOpen),
      programOpen: Boolean(parsed.programOpen),
      projectOpen: Boolean(parsed.projectOpen),
      openProjects: parseOpenProjects(parsed.openProjects),
      openPrograms: parseOpenProjects(parsed.openPrograms),
    };
  } catch {
    return fallback;
  }
}

export function saveNavChrome(next: NavChrome): void {
  localStorage.setItem(NAV_KEY, JSON.stringify(next));
}
