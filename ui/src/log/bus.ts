export type LogChannel = "api" | "ui";
export type LogLevel = "debug" | "info" | "warn" | "error";

export interface LogEntry {
  id: string;
  ts: string;
  channel: LogChannel;
  level: LogLevel;
  message: string;
  detail?: string;
}

const MAX_ENTRIES = 500;
const store: Record<LogChannel, LogEntry[]> = { api: [], ui: [] };
const listeners = new Set<(channel: LogChannel, entries: LogEntry[]) => void>();
let seq = 0;

export const LOG_SESSION_ID = makeSessionId();

function makeSessionId(): string {
  const stamp = new Date().toISOString().replace(/[:.]/g, "-").replace("T", "-").replace("Z", "");
  const rand = Math.random().toString(36).slice(2, 8);
  return `${stamp}-${rand}`;
}

export function snapshot(channel: LogChannel): LogEntry[] {
  return store[channel].slice();
}

export function subscribe(listener: (channel: LogChannel, entries: LogEntry[]) => void): () => void {
  listeners.add(listener);
  return () => {
    listeners.delete(listener);
  };
}

export function appendLog(input: {
  channel: LogChannel;
  level?: LogLevel;
  message: string;
  detail?: string;
}): LogEntry {
  const entry: LogEntry = {
    id: `${Date.now()}-${++seq}`,
    ts: new Date().toISOString(),
    channel: input.channel,
    level: input.level ?? "info",
    message: input.message,
    detail: input.detail,
  };
  const list = store[entry.channel];
  list.push(entry);
  if (list.length > MAX_ENTRIES) {
    store[entry.channel] = list.slice(-MAX_ENTRIES);
  }
  const published = store[entry.channel].slice();
  for (const listener of listeners) {
    listener(entry.channel, published);
  }
  return entry;
}

export function logApi(message: string, detail?: string, level: LogLevel = "info"): void {
  appendLog({ channel: "api", level, message, detail });
}

export function logUi(message: string, detail?: string, level: LogLevel = "info"): void {
  appendLog({ channel: "ui", level, message, detail });
}

export function shouldSkipApiLog(url: string): boolean {
  try {
    const path = url.startsWith("http") ? new URL(url).pathname : url.split("?")[0];
    return path === "/health" || path.startsWith("/debug/");
  } catch {
    return url.includes("/health") || url.includes("/debug/");
  }
}

export function clipLogText(value: unknown, max = 2000): string {
  const text = typeof value === "string" ? value : JSON.stringify(value);
  if (!text) {
    return "";
  }
  if (text.length <= max) {
    return text;
  }
  return `${text.slice(0, max)}…(+${text.length - max}b)`;
}

export function resetLogsForTests(): void {
  store.api = [];
  store.ui = [];
  seq = 0;
}
