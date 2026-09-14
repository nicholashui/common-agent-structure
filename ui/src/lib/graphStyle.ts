/** Shared ComfyUI-like graph tokens for Project, Org Chat, and SVG workflows. */

export const GRAPH_CANVAS = "#1e1e1e";
export const GRAPH_NODE = "#353535";
export const GRAPH_GRID = "#3a3a3a";

export const GRAPH_KIND = {
  start: { title: "#2a5ea7", mini: "#2a82da", label: "Start" },
  agent: { title: "#2e7d32", mini: "#43a047", label: "Agent" },
  human: { title: "#6a1b9a", mini: "#ab47bc", label: "Human" },
  output: { title: "#e65100", mini: "#fb8c00", label: "Output" },
  workflow: { title: "#37474f", mini: "#78909c", label: "Workflow" },
  group: { title: "#1a237e", mini: "#5c6bc0", label: "Agent Group" },
  category: { title: "#4a148c", mini: "#7e57c2", label: "Category" },
} as const;

const SOCKET_PALETTE = ["#64b5f6", "#81c784", "#ffcc80", "#ce93d8", "#f48fb1", "#80deea", "#aed581", "#ffab91"];

export function socketColor(name: string): string {
  const key = name.trim() || "next";
  let hash = 0;
  for (let index = 0; index < key.length; index += 1) {
    hash = (hash * 31 + key.charCodeAt(index)) >>> 0;
  }
  return SOCKET_PALETTE[hash % SOCKET_PALETTE.length];
}

/** Injected into Main/Sub Workflow SVG documents when the app theme is light. */
export const LIGHT_SVG_OVERRIDE = `
svg{background:#f4f7fb!important}
.canvas{fill:#f4f7fb!important}
.section-title{fill:#0f172a!important}
.section-sub{fill:#475569!important}
.phase-name{fill:#0f172a!important}
.phase-count{fill:#526176!important}
.card-title{fill:#ffffff!important}
.small{fill:#405066!important}
.tiny{fill:#64748b!important}
.label{fill:#334155!important}
.agent-text{fill:#1d4ed8!important;text-decoration-color:#bfdbfe!important}
.agent-list{fill:#334155!important}
.agent-list .agentline{fill:#1d4ed8!important;text-decoration-color:#bfdbfe!important}
.agent-hit{fill:#eff6ff!important;stroke:#dbeafe!important}
.phase-bg{fill:#ffffff!important;stroke:#d8e1ec!important}
.phase-bg-alt{fill:#f8fafc!important;stroke:#d8e1ec!important}
.control-bg{fill:#f8fafc!important;stroke:#c7d2fe!important}
.card,.card-blue,.card-purple,.card-green,.card-amber,.card-rose{fill:#ffffff!important;stroke:#cbd5e1!important}
.gateway{fill:#fff7ed!important;stroke:#d97706!important}
.gateway-text,.gateway-sub{fill:#78350f!important}
.parallel{fill:#eef2ff!important;stroke:#4f46e5!important}
.parallel-symbol{fill:#3730a3!important}
.artifact{fill:transparent!important;stroke:#64748b!important}
.runtime-banner{fill:#fffbeb!important;stroke:#f59e0b!important}
.header-note{fill:#78350f!important}
.feedback-label{fill:#b42318!important}
.flow{stroke:#2563eb!important}
.branch{stroke:#059669!important}
.feedback{stroke:#c2413b!important}
.learning{stroke:#6d28d9!important}
.association{stroke:#64748b!important}
.legend-line{stroke:#334155!important}
.event,.phase-start{fill:#ffffff!important;stroke:#2563eb!important}
.end-event-outer{fill:#ffffff!important;stroke:#047857!important}
`;

export function applySvgTheme(doc: Document, theme: "light" | "dark"): void {
  const existing = doc.getElementById("casops-theme-override");
  if (theme === "dark") {
    existing?.remove();
    return;
  }
  let style = existing as SVGStyleElement | null;
  if (!style) {
    style = doc.createElementNS("http://www.w3.org/2000/svg", "style") as SVGStyleElement;
    style.setAttribute("id", "casops-theme-override");
    doc.documentElement.appendChild(style);
  }
  style.textContent = LIGHT_SVG_OVERRIDE;
}

export function graphEdgeStyle(options?: { loop?: boolean; handle?: string | null }) {
  const loop = Boolean(options?.loop);
  return {
    type: "default" as const,
    animated: loop,
    style: {
      stroke: loop ? "#e65100" : socketColor(String(options?.handle || "next")),
      strokeWidth: 2.4,
      strokeDasharray: loop ? "6 4" : undefined,
    },
  };
}
