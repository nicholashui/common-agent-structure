export type ChatRole = "user" | "assistant";

export interface ChatTurn {
  role: ChatRole;
  content: string;
  provider?: string;
}

const MAX_HISTORY = 20;
const threads = new Map<string, ChatTurn[]>();

export function normalizeChatHistory(turns: ChatTurn[]): { role: ChatRole; content: string }[] {
  return turns
    .filter((turn) => (turn.role === "user" || turn.role === "assistant") && turn.content.trim())
    .slice(-MAX_HISTORY)
    .map((turn) => ({ role: turn.role, content: turn.content.trim() }));
}

export function loadThread(agentId: string): ChatTurn[] {
  return threads.get(agentId) ?? [];
}

export function saveThread(agentId: string, turns: ChatTurn[]): void {
  threads.set(agentId, turns);
}

export function clearThread(agentId: string): void {
  threads.delete(agentId);
}
