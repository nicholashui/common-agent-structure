export const AGENT_TABS = [
  { id: "overview", label: "Overview", path: "" },
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

const NAV_KEY = "casops.control-ui.nav.v1";

export interface NavChrome {
  collapsed: boolean;
  agentOpen: boolean;
}

export function loadNavChrome(): NavChrome {
  try {
    const raw = localStorage.getItem(NAV_KEY);
    if (!raw) {
      return { collapsed: false, agentOpen: true };
    }
    const parsed = JSON.parse(raw) as Partial<NavChrome>;
    return {
      collapsed: Boolean(parsed.collapsed),
      agentOpen: parsed.agentOpen !== false,
    };
  } catch {
    return { collapsed: false, agentOpen: true };
  }
}

export function saveNavChrome(next: NavChrome): void {
  localStorage.setItem(NAV_KEY, JSON.stringify(next));
}
