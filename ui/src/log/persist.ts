import { LOG_SESSION_ID, type LogChannel, type LogEntry } from "./bus";

export interface LogFiles {
  api?: string;
  ui?: string;
}

type GetBaseUrl = () => string;

let getBaseUrl: GetBaseUrl = () => "";
let queue: LogEntry[] = [];
let timer: ReturnType<typeof setTimeout> | null = null;
let flushing = false;
let files: LogFiles = {};
const fileListeners = new Set<(files: LogFiles) => void>();

export function startLogSink(baseUrl: GetBaseUrl): void {
  getBaseUrl = baseUrl;
}

export function logFilesSnapshot(): LogFiles {
  return { ...files };
}

export function subscribeLogFiles(listener: (next: LogFiles) => void): () => void {
  fileListeners.add(listener);
  return () => {
    fileListeners.delete(listener);
  };
}

export function enqueueLogPersist(entry: LogEntry): void {
  queue.push(entry);
  if (queue.length > 500) {
    queue = queue.slice(-500);
  }
  if (timer !== null) {
    return;
  }
  timer = setTimeout(() => {
    timer = null;
    void flushLogs();
  }, 250);
}

export async function flushLogsNow(): Promise<void> {
  if (timer !== null) {
    clearTimeout(timer);
    timer = null;
  }
  await flushLogs();
}

export function resetLogPersistForTests(): void {
  queue = [];
  files = {};
  flushing = false;
  if (timer !== null) {
    clearTimeout(timer);
    timer = null;
  }
}

async function flushLogs(): Promise<void> {
  if (flushing || !queue.length) {
    return;
  }
  flushing = true;
  const batch = queue.splice(0, 100);
  try {
    const base = getBaseUrl().replace(/\/$/, "");
    const response = await fetch(`${base}/debug/logs`, {
      method: "POST",
      headers: { Accept: "application/json", "Content-Type": "application/json" },
      body: JSON.stringify({
        session: LOG_SESSION_ID,
        entries: batch.map((entry) => ({
          channel: entry.channel,
          ts: entry.ts,
          level: entry.level,
          message: entry.message,
          detail: entry.detail ?? "",
        })),
      }),
    });
    if (!response.ok) {
      queue = batch.concat(queue);
      return;
    }
    const body = (await response.json()) as { files?: Record<LogChannel, string> };
    if (body.files) {
      files = { ...files, ...body.files };
      for (const listener of fileListeners) {
        listener(files);
      }
    }
  } catch {
    queue = batch.concat(queue);
  } finally {
    flushing = false;
    if (queue.length && timer === null) {
      timer = setTimeout(() => {
        timer = null;
        void flushLogs();
      }, 250);
    }
  }
}
