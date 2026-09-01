export type AgentPack = "all" | "specials" | "video" | "other";

export interface AgentFilterFields {
  agent_id: string;
  role?: string;
  folder?: string;
}

export function collectAgentIds(agents: { agent_id: string }[], extra: string[]): string[] {
  const ids = agents.map((agent) => agent.agent_id);
  const seen = new Set(ids);
  for (const id of extra) {
    if (!seen.has(id)) {
      ids.push(id);
      seen.add(id);
    }
  }
  return ids;
}

export function filterAgentIds(ids: string[], query: string): string[] {
  const needle = query.trim().toLowerCase();
  if (!needle) {
    return ids;
  }
  return ids.filter((id) => id.toLowerCase().includes(needle));
}

export function agentPack(agentId: string): Exclude<AgentPack, "all"> {
  if (agentId.startsWith("specials.")) {
    return "specials";
  }
  if (agentId.startsWith("video.")) {
    return "video";
  }
  return "other";
}

export const AGENT_GROUP_ORDER: Exclude<AgentPack, "all">[] = ["video", "specials", "other"];

export function listAgentGroups(agents: { agent_id: string }[]): Exclude<AgentPack, "all">[] {
  const present = new Set(agents.map((agent) => agentPack(agent.agent_id)));
  return AGENT_GROUP_ORDER.filter((pack) => present.has(pack));
}

export function filterAgentCards<T extends AgentFilterFields>(
  items: T[],
  query: string,
  pack: AgentPack = "all",
): T[] {
  const needle = query.trim().toLowerCase();
  return items.filter((item) => {
    if (pack !== "all" && agentPack(item.agent_id) !== pack) {
      return false;
    }
    if (!needle) {
      return true;
    }
    return [item.agent_id, item.role, item.folder].some((value) =>
      (value || "").toLowerCase().includes(needle),
    );
  });
}
