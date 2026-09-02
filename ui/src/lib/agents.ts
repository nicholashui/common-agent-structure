export type AgentPack = "all" | "specials" | "video" | "other";

export interface AgentFilterFields {
  agent_id: string;
  role?: string;
  folder?: string;
  va_category?: string;
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

export function filterAgentIds(
  ids: string[],
  query: string,
  agents: { agent_id: string; va_category?: string }[] = [],
): string[] {
  const needle = query.trim().toLowerCase();
  if (!needle) {
    return ids;
  }
  const categories = new Map(
    agents.map((agent) => [agent.agent_id, (agent.va_category || "").toLowerCase()]),
  );
  return ids.filter((id) => {
    if (id.toLowerCase().includes(needle)) {
      return true;
    }
    const category = categories.get(id) || "";
    return category.includes(needle);
  });
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

export function agentCategory(agent: { va_category?: string }): string {
  const raw = (agent.va_category || "").trim();
  return raw || "uncategorized";
}

export function listAgentCategories(agents: { va_category?: string }[]): string[] {
  const names = new Set<string>();
  for (const agent of agents) {
    const category = agentCategory(agent);
    if (category !== "uncategorized") {
      names.add(category);
    }
  }
  return [...names].sort((left, right) => left.localeCompare(right));
}

export interface FleetCategoryGroup<T> {
  category: string;
  items: T[];
}

export interface FleetPackGroup<T> {
  pack: Exclude<AgentPack, "all">;
  showCategory: boolean;
  categories: FleetCategoryGroup<T>[];
}

function sortCategories(keys: string[]): string[] {
  return keys.slice().sort((left, right) => {
    if (left === "uncategorized") {
      return 1;
    }
    if (right === "uncategorized") {
      return -1;
    }
    return left.localeCompare(right);
  });
}

export function groupFleetCards<T extends { agent_id: string; va_category?: string }>(
  items: T[],
  pack: AgentPack = "all",
): FleetPackGroup<T>[] {
  const packs = pack === "all" ? AGENT_GROUP_ORDER : [pack];
  const groups: FleetPackGroup<T>[] = [];
  for (const current of packs) {
    const members = items.filter((item) => agentPack(item.agent_id) === current);
    if (!members.length) {
      continue;
    }
    const buckets = new Map<string, T[]>();
    for (const item of members) {
      const category = agentCategory(item);
      const list = buckets.get(category) ?? [];
      list.push(item);
      buckets.set(category, list);
    }
    const names = sortCategories([...buckets.keys()]);
    const showCategory = names.some((name) => name !== "uncategorized");
    groups.push({
      pack: current,
      showCategory,
      categories: showCategory
        ? names.map((category) => ({ category, items: buckets.get(category) ?? [] }))
        : [{ category: "uncategorized", items: members }],
    });
  }
  return groups;
}

export function listAgentGroups(agents: { agent_id: string }[]): Exclude<AgentPack, "all">[] {
  const present = new Set(agents.map((agent) => agentPack(agent.agent_id)));
  return AGENT_GROUP_ORDER.filter((pack) => present.has(pack));
}

export function filterAgentCards<T extends AgentFilterFields>(
  items: T[],
  query: string,
  pack: AgentPack = "all",
  category = "",
): T[] {
  const needle = query.trim().toLowerCase();
  const wanted = category.trim();
  return items.filter((item) => {
    if (pack !== "all" && agentPack(item.agent_id) !== pack) {
      return false;
    }
    if (wanted && agentCategory(item) !== wanted) {
      return false;
    }
    if (!needle) {
      return true;
    }
    return [item.agent_id, item.role, item.folder, item.va_category].some((value) =>
      (value || "").toLowerCase().includes(needle),
    );
  });
}
