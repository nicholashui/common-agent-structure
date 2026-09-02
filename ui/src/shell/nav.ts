export const AGENT_TABS = [
  { id: "overview", label: "Overview", path: "" },
  { id: "chat", label: "Chat", path: "chat" },
  { id: "structure", label: "Structure", path: "structure" },
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

export const HOME_LABEL = "Agent Swarm";
export const AGENT_MENU_LABEL = "Agent Profile";
export const WORKFLOW_MENU_LABEL = "Agent Workflow";
export const WORKFLOW_TABS = [
  { id: "main", label: "Main Workflow", path: "/workflow", depth: 1 },
  { id: "sub", label: "Sub Workflow", path: "/workflow/sub", depth: 2 },
] as const;

export function locationLabel(pathname: string): string {
  const trimmed = pathname.replace(/\/+$/, "") || "/";
  if (trimmed === "/") {
    return HOME_LABEL;
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
  let path = trimmed.replace(/^\//, "");
  try {
    path = decodeURIComponent(path);
  } catch {
    // keep the raw path if it is not valid percent-encoding
  }
  return `${HOME_LABEL} / ${path}`;
}

const NAV_KEY = "casops.control-ui.nav.v1";

export interface NavChrome {
  collapsed: boolean;
  agentOpen: boolean;
  workflowOpen: boolean;
}

export function loadNavChrome(): NavChrome {
  try {
    const raw = localStorage.getItem(NAV_KEY);
    if (!raw) {
      return { collapsed: false, agentOpen: true, workflowOpen: true };
    }
    const parsed = JSON.parse(raw) as Partial<NavChrome>;
    return {
      collapsed: Boolean(parsed.collapsed),
      agentOpen: parsed.agentOpen !== false,
      workflowOpen: parsed.workflowOpen !== false,
    };
  } catch {
    return { collapsed: false, agentOpen: true, workflowOpen: true };
  }
}

export function saveNavChrome(next: NavChrome): void {
  localStorage.setItem(NAV_KEY, JSON.stringify(next));
}
