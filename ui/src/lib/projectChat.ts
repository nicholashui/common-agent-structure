/** Chat timeline: collab hops, then assembled instruction, then generated clips. */

import { parseVideoAgentIds } from "./projects";
import { formatHktDateTime } from "./time";

export type ChatTimeItem = {
  id: string;
  kind: string;
  created_at?: string;
};

export type ChatHop = ChatTimeItem & {
  from?: string;
  to?: string;
  input_tags?: { comm_id?: string }[];
};

const PARTY_NAMES: Record<string, string> = {
  human_operator: "Human",
  "create-project": "Create Project",
  "output-prompt": "Output",
  "human-ask": "Human",
};

export function displayPartyName(id: string): string {
  const key = String(id || "").trim();
  if (!key) {
    return "";
  }
  return PARTY_NAMES[key] || key;
}

export function sourceCommId<T extends ChatHop>(item: T, items: T[]): string {
  const tagged = (item.input_tags || [])
    .map((row) => String(row.comm_id || ""))
    .find((id) => id && id !== "comm-pending" && id !== item.id);
  if (tagged) {
    return tagged;
  }
  const ordered = sortProjectComms(items);
  const index = ordered.findIndex((row) => row.id === item.id);
  const from = String(item.from || "");
  if (!from || index <= 0) {
    return "";
  }
  for (let i = index - 1; i >= 0; i -= 1) {
    if (String(ordered[i].to || "") === from) {
      return ordered[i].id;
    }
  }
  return "";
}

export function hopKindLabel(kind: string, optionCount = 0): string {
  if (kind === "return" && optionCount) {
    return "suggestions";
  }
  if (kind === "choice") {
    return "selection";
  }
  if (kind === "human_ask") {
    return "ASK_HUMAN";
  }
  if (kind === "generated_media") {
    return "generated clip";
  }
  if (kind === "output" || kind === "assembled") {
    return "generated instruction";
  }
  if (kind === "next_instruction") {
    return "next instruction";
  }
  return kind || "instruction";
}

export function hopExtra(
  item: {
    id: string;
    kind?: string;
    pass_id?: string;
    created_at?: string;
    live?: boolean;
    provider?: string;
    error?: string;
  },
  optionCount = 0,
): string {
  const bits = [
    hopKindLabel(item.kind || "", optionCount),
    item.pass_id || "",
    `#${commSeq(item.id)}`,
    formatHktDateTime(item.created_at),
    item.live ? `live ${item.provider || ""}`.trim() : "not a live hop",
    item.error || "",
  ].filter(Boolean);
  return bits.join(" · ");
}

export function hopHeaderText(
  item: {
    id: string;
    from?: string;
    to?: string;
    kind?: string;
    pass_id?: string;
    created_at?: string;
    live?: boolean;
    provider?: string;
    error?: string;
  },
  optionCount = 0,
): string {
  return `${displayPartyName(item.from || "")} → ${displayPartyName(item.to || "")} | ${hopExtra(item, optionCount)}`;
}

export function optionAgentIds(owner: string, text: string): string[] {
  const names: string[] = [];
  const seen = new Set<string>();
  for (const id of [owner, ...parseVideoAgentIds(text || "")]) {
    const key = String(id || "").trim();
    if (!key || seen.has(key)) {
      continue;
    }
    seen.add(key);
    names.push(key);
  }
  return names;
}

const OUTPUT_KINDS = new Set(["output", "assembled"]);
const CLIP_KINDS = new Set(["generated_media"]);

export function commSeq(id: string): number {
  const match = /^comm-(\d+)$/i.exec(String(id || ""));
  return match ? Number(match[1]) : Number.MAX_SAFE_INTEGER;
}

export function sortProjectComms<T extends ChatTimeItem>(items: T[]): T[] {
  return [...items].sort((left, right) => {
    const leftTime = left.created_at || "";
    const rightTime = right.created_at || "";
    if (leftTime && rightTime && leftTime !== rightTime) {
      return leftTime.localeCompare(rightTime);
    }
    const leftSeq = commSeq(left.id);
    const rightSeq = commSeq(right.id);
    if (leftSeq !== rightSeq) {
      return leftSeq - rightSeq;
    }
    return String(left.id).localeCompare(String(right.id));
  });
}

export function splitProjectChat<T extends ChatTimeItem>(items: T[]): {
  conversation: T[];
  instruction: T[];
  clips: T[];
} {
  const ordered = sortProjectComms(items);
  return {
    conversation: ordered.filter((item) => !OUTPUT_KINDS.has(item.kind) && !CLIP_KINDS.has(item.kind)),
    instruction: ordered.filter((item) => OUTPUT_KINDS.has(item.kind)),
    clips: ordered.filter((item) => CLIP_KINDS.has(item.kind)),
  };
}

const FILE_NAME = /^[A-Za-z0-9._-]+$/;
const FILE_ROUTE = /^\/api\/v3\/projects\/([^/?#]+)\/output\/file\/?$/;

export function mediaHref(url: string, projectId?: string): string {
  if (!url || url.includes("..")) {
    return "";
  }
  const trimmed = url.trim();
  if (/^[a-zA-Z][a-zA-Z0-9+.-]*:/.test(trimmed) && !trimmed.startsWith("/")) {
    return "";
  }
  const qIndex = trimmed.indexOf("?");
  const path = qIndex >= 0 ? trimmed.slice(0, qIndex) : trimmed;
  const query = qIndex >= 0 ? trimmed.slice(qIndex + 1) : "";
  const name = new URLSearchParams(query).get("name") || "";
  const match = FILE_ROUTE.exec(path);
  if (!match || !FILE_NAME.test(name) || name.includes("..")) {
    return "";
  }
  if (projectId && match[1] !== projectId) {
    return "";
  }
  return `${path}?name=${encodeURIComponent(name)}`;
}
