import { formatHktStamp } from "./time";

export type ChatRole = "user" | "assistant";

export interface ChatTurn {
  role: ChatRole;
  content: string;
  provider?: string;
  truncated?: boolean;
  ts?: string;
}

export function chatHitOutputCap(llm?: { truncated?: boolean; finish_reason?: string } | null): boolean {
  if (!llm) {
    return false;
  }
  if (llm.truncated) {
    return true;
  }
  const reason = (llm.finish_reason || "").toLowerCase();
  return reason === "length" || reason === "max_tokens" || reason === "max_output_tokens";
}

export interface ChatFile {
  path: string;
  name: string;
  ts: string;
  bytes?: number;
}

export interface ChatThread {
  session: string;
  turns: ChatTurn[];
  files: ChatFile[];
}

const MAX_HISTORY = 20;
const MAX_STORED = 200;
const THREAD_KEY = "casops.control-ui.chat.v1";
export const CHAT_SIDE_WIDTH_KEY = "casops.control-ui.chat-side-width.v1";
export const CHAT_SIDE_WIDTH_MIN = 280;
export const CHAT_SIDE_WIDTH_MAX = 560;
export const CHAT_SIDE_WIDTH_DEFAULT = 360;
export const CHAT_SIDE_WIDTH_STEP = 16;

export function clampChatSideWidth(width: number): number {
  if (!Number.isFinite(width)) {
    return CHAT_SIDE_WIDTH_DEFAULT;
  }
  return Math.min(CHAT_SIDE_WIDTH_MAX, Math.max(CHAT_SIDE_WIDTH_MIN, Math.round(width)));
}

export function loadChatSideWidth(): number {
  try {
    const raw = localStorage.getItem(CHAT_SIDE_WIDTH_KEY);
    if (!raw) {
      return CHAT_SIDE_WIDTH_DEFAULT;
    }
    return clampChatSideWidth(Number(raw));
  } catch {
    return CHAT_SIDE_WIDTH_DEFAULT;
  }
}

export function saveChatSideWidth(width: number): void {
  try {
    localStorage.setItem(CHAT_SIDE_WIDTH_KEY, String(clampChatSideWidth(width)));
  } catch {
    // ignore quota / private-mode
  }
}
const memory = new Map<string, ChatThread>();

export function makeChatSessionId(): string {
  const rand = Math.random().toString(36).slice(2, 8);
  return `${formatHktStamp()}-${rand}`;
}

export function normalizeChatHistory(turns: ChatTurn[]): { role: ChatRole; content: string }[] {
  return turns
    .filter((turn) => (turn.role === "user" || turn.role === "assistant") && turn.content.trim())
    .slice(-MAX_HISTORY)
    .map((turn) => ({ role: turn.role, content: turn.content.trim() }));
}

export function buildChatBody(
  message: string,
  history: ChatTurn[],
  session: string,
): { message: string; history: { role: ChatRole; content: string }[]; session: string } {
  return { message, history: normalizeChatHistory(history), session };
}

export function emptyThread(): ChatThread {
  return { session: makeChatSessionId(), turns: [], files: [] };
}

function readDisk(): Record<string, ChatThread> {
  try {
    const raw = localStorage.getItem(THREAD_KEY);
    if (!raw) {
      return {};
    }
    const parsed = JSON.parse(raw) as Record<string, Partial<ChatThread>>;
    const out: Record<string, ChatThread> = {};
    for (const [agentId, value] of Object.entries(parsed)) {
      if (!agentId || !value || typeof value !== "object") {
        continue;
      }
      out[agentId] = {
        session: typeof value.session === "string" && value.session ? value.session : makeChatSessionId(),
        turns: Array.isArray(value.turns) ? value.turns.filter(isTurn).slice(-MAX_STORED) : [],
        files: Array.isArray(value.files) ? value.files.filter(isFile).slice(0, 50) : [],
      };
    }
    return out;
  } catch {
    return {};
  }
}

function writeDisk(all: Record<string, ChatThread>): void {
  try {
    localStorage.setItem(THREAD_KEY, JSON.stringify(all));
  } catch {
    // ignore quota / private-mode failures
  }
}

function isTurn(value: unknown): value is ChatTurn {
  if (!value || typeof value !== "object") {
    return false;
  }
  const turn = value as ChatTurn;
  return (turn.role === "user" || turn.role === "assistant") && typeof turn.content === "string";
}

function isFile(value: unknown): value is ChatFile {
  if (!value || typeof value !== "object") {
    return false;
  }
  const file = value as ChatFile;
  return Boolean(file.path && file.name && file.ts);
}

function persistAgent(agentId: string, thread: ChatThread): void {
  memory.set(agentId, thread);
  const all = readDisk();
  all[agentId] = thread;
  writeDisk(all);
}

export function loadThread(agentId: string): ChatThread {
  const cached = memory.get(agentId);
  if (cached) {
    return cached;
  }
  const stored = readDisk()[agentId];
  const thread = stored ?? emptyThread();
  memory.set(agentId, thread);
  return thread;
}

export function saveThread(agentId: string, turns: ChatTurn[]): ChatThread {
  const current = loadThread(agentId);
  const next: ChatThread = { ...current, turns: turns.slice(-MAX_STORED) };
  persistAgent(agentId, next);
  return next;
}

export function clearThread(agentId: string): ChatThread {
  const current = loadThread(agentId);
  const next: ChatThread = { session: makeChatSessionId(), turns: [], files: current.files };
  persistAgent(agentId, next);
  return next;
}

export function rememberChatFiles(agentId: string, files: ChatFile[]): ChatFile[] {
  const current = loadThread(agentId);
  const byPath = new Map<string, ChatFile>();
  for (const file of [...current.files, ...files]) {
    if (file.path) {
      byPath.set(file.path, file);
    }
  }
  const merged = [...byPath.values()].sort((a, b) => b.ts.localeCompare(a.ts)).slice(0, 50);
  persistAgent(agentId, { ...current, files: merged });
  return merged;
}

export function resetChatForTests(): void {
  memory.clear();
  try {
    localStorage.removeItem(THREAD_KEY);
  } catch {
    // ignore
  }
}

export function sessionFromFileName(name: string): string {
  return name.replace(/\.jsonl$/i, "");
}

export function replaceThread(agentId: string, turns: ChatTurn[], session: string): ChatThread {
  const current = loadThread(agentId);
  const next: ChatThread = {
    session: session || makeChatSessionId(),
    turns: turns.filter(isTurn).slice(-MAX_STORED),
    files: current.files,
  };
  persistAgent(agentId, next);
  return next;
}

export function lastUserIndex(turns: ChatTurn[]): number {
  for (let index = turns.length - 1; index >= 0; index -= 1) {
    if (turns[index]?.role === "user" && turns[index].content.trim()) {
      return index;
    }
  }
  return -1;
}

export function canRegenerate(turns: ChatTurn[]): boolean {
  if (turns.length < 2) {
    return false;
  }
  const last = turns[turns.length - 1];
  return last.role === "assistant" && lastUserIndex(turns) >= 0;
}

export function exportThreadMarkdown(agentId: string, turns: ChatTurn[]): string {
  const lines = [
    `# Chat with ${agentId}`,
    "",
    "Honesty: host Chat transcript. Not a sealed Run. Not an eval pass.",
    "",
  ];
  for (const turn of turns) {
    lines.push(`## ${turn.role}`);
    if (turn.ts) {
      lines.push(`_${turn.ts}_${turn.provider ? ` · ${turn.provider}` : ""}`);
      lines.push("");
    }
    lines.push(turn.content.trim() || "(empty)");
    lines.push("");
  }
  return lines.join("\n");
}

export function exportThreadJson(agentId: string, session: string, turns: ChatTurn[]): string {
  return `${JSON.stringify(
    {
      agent_id: agentId,
      session,
      honesty: "CHARACTERIZATION",
      note: "Host Chat transcript. Not a sealed Run. Not an eval pass.",
      turns,
    },
    null,
    2,
  )}\n`;
}

export function downloadText(filename: string, text: string, mime: string): void {
  const blob = new Blob([text], { type: mime });
  const href = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = href;
  link.download = filename;
  link.click();
  URL.revokeObjectURL(href);
}

export async function copyText(text: string): Promise<boolean> {
  try {
    if (navigator.clipboard?.writeText) {
      await navigator.clipboard.writeText(text);
      return true;
    }
  } catch {
    // fall through
  }
  try {
    const area = document.createElement("textarea");
    area.value = text;
    area.setAttribute("readonly", "true");
    area.style.position = "fixed";
    area.style.left = "-9999px";
    document.body.appendChild(area);
    area.select();
    const ok = document.execCommand("copy");
    area.remove();
    return ok;
  } catch {
    return false;
  }
}
