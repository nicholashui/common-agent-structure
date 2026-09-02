import { rememberChatFiles, type ChatFile, type ChatTurn } from "./chat";

type GetBaseUrl = () => string;

let getBaseUrl: GetBaseUrl = () => "";
let queue: { agentId: string; session: string; turn: ChatTurn }[] = [];
let timer: ReturnType<typeof setTimeout> | null = null;
let flushing = false;
const listeners = new Set<(agentId: string, files: ChatFile[]) => void>();

export function startChatSink(baseUrl: GetBaseUrl): void {
  getBaseUrl = baseUrl;
}

export function subscribeChatFiles(listener: (agentId: string, files: ChatFile[]) => void): () => void {
  listeners.add(listener);
  return () => {
    listeners.delete(listener);
  };
}

export function enqueueChatPersist(agentId: string, session: string, turn: ChatTurn): void {
  queue.push({ agentId, session, turn });
  if (queue.length > 200) {
    queue = queue.slice(-200);
  }
}

export async function flushChatNow(): Promise<void> {
  if (timer !== null) {
    clearTimeout(timer);
    timer = null;
  }
  await flushChat();
  while (queue.length && !flushing) {
    await flushChat();
  }
}

export function resetChatPersistForTests(): void {
  queue = [];
  flushing = false;
  if (timer !== null) {
    clearTimeout(timer);
    timer = null;
  }
}

export async function refreshChatFiles(agentId: string): Promise<ChatFile[]> {
  const base = getBaseUrl().replace(/\/$/, "");
  const response = await fetch(`${base}/debug/chat?agent_id=${encodeURIComponent(agentId)}`, {
    headers: { Accept: "application/json" },
  });
  if (!response.ok) {
    return rememberChatFiles(agentId, []);
  }
  const body = (await response.json()) as { files?: ChatFile[] };
  const files = rememberChatFiles(agentId, body.files ?? []);
  for (const listener of listeners) {
    listener(agentId, files);
  }
  return files;
}

async function flushChat(): Promise<void> {
  if (flushing || !queue.length) {
    return;
  }
  flushing = true;
  const first = queue[0];
  const batch: typeof queue = [];
  const rest: typeof queue = [];
  for (const item of queue) {
    if (item.agentId === first.agentId && item.session === first.session && batch.length < 50) {
      batch.push(item);
    } else {
      rest.push(item);
    }
  }
  queue = rest;
  try {
    const base = getBaseUrl().replace(/\/$/, "");
    const response = await fetch(`${base}/debug/chat`, {
      method: "POST",
      headers: { Accept: "application/json", "Content-Type": "application/json" },
      body: JSON.stringify({
        agent_id: first.agentId,
        session: first.session,
        entries: batch.map((item) => ({
          ts: item.turn.ts ?? "",
          role: item.turn.role,
          content: item.turn.content,
          provider: item.turn.provider ?? "",
        })),
      }),
    });
    if (!response.ok) {
      queue = batch.concat(queue);
      return;
    }
    const body = (await response.json()) as { files?: { transcript?: string } };
    const path = body.files?.transcript;
    if (path) {
      const files = rememberChatFiles(first.agentId, [
        {
          path,
          name: path.replace(/\\/g, "/").split("/").slice(-1)[0] ?? path,
          ts: first.turn.ts || new Date().toISOString(),
        },
      ]);
      for (const listener of listeners) {
        listener(first.agentId, files);
      }
    }
  } catch {
    queue = batch.concat(queue);
  } finally {
    flushing = false;
    if (queue.length && timer === null) {
      timer = setTimeout(() => {
        timer = null;
        void flushChat();
      }, 250);
    }
  }
}
