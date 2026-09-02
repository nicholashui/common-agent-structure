export type ChatRole = "user" | "assistant";

export interface ChatTurn {
  role: ChatRole;
  content: string;
  provider?: string;
  ts?: string;
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
const memory = new Map<string, ChatThread>();

export function makeChatSessionId(): string {
  const stamp = new Date().toISOString().replace(/[:.]/g, "-").replace("T", "-").replace("Z", "");
  const rand = Math.random().toString(36).slice(2, 8);
  return `${stamp}-${rand}`;
}

export function normalizeChatHistory(turns: ChatTurn[]): { role: ChatRole; content: string }[] {
  return turns
    .filter((turn) => (turn.role === "user" || turn.role === "assistant") && turn.content.trim())
    .slice(-MAX_HISTORY)
    .map((turn) => ({ role: turn.role, content: turn.content.trim() }));
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
