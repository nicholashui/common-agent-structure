import type {
  ProjectCatalogItem,
  ProjectNextSuggestion,
  ProjectSuggestion,
  ProjectSuggestionRow,
} from "../api/types";

const VIDEO_ID_RE = /video\.(?:template|scale)\.[a-j0-9s]+/gi;

export function parseVideoWorkflowIds(text: string): string[] {
  const found: string[] = [];
  const seen = new Set<string>();
  for (const match of text.matchAll(VIDEO_ID_RE)) {
    const key = match[0].toLowerCase();
    if (seen.has(key)) {
      continue;
    }
    seen.add(key);
    found.push(key);
  }
  return found;
}

export function suggestionRow(item: ProjectCatalogItem, rank: number, source: string): ProjectSuggestionRow {
  return {
    id: item.id,
    label: `${item.code} · ${item.label}`,
    kind: item.kind,
    reason: item.use,
    rank,
    source,
  };
}

export function applyLlmSuggestion(
  current: ProjectSuggestion,
  reply: string,
  catalog: ProjectCatalogItem[] = [],
): ProjectSuggestion {
  const excerpt = (reply || "").slice(0, 1200);
  const ids = parseVideoWorkflowIds(reply);
  if (!ids.length) {
    return { ...current, llm_used: true, llm_excerpt: excerpt || current.llm_excerpt };
  }
  const catalogById = new Map(catalog.map((row) => [row.id, row]));
  const existing = new Map(current.suggestions.map((row) => [row.id, row]));
  const promoted: ProjectSuggestionRow[] = [];
  const seen = new Set<string>();
  for (const id of ids) {
    if (seen.has(id)) {
      continue;
    }
    const item = catalogById.get(id);
    const prior = existing.get(id);
    if (!item && !prior) {
      continue;
    }
    seen.add(id);
    const row = prior ?? (item ? suggestionRow(item, 0, "llm") : null);
    if (!row) {
      continue;
    }
    promoted.push({ ...row, source: "llm", rank: promoted.length + 1 });
  }
  for (const row of current.suggestions) {
    if (!seen.has(row.id)) {
      promoted.push({ ...row, rank: promoted.length + 1 });
      seen.add(row.id);
    }
  }
  return {
    ...current,
    llm_used: true,
    llm_excerpt: excerpt,
    primary: promoted[0]?.id ?? current.primary,
    suggestions: promoted.slice(0, 5),
  };
}

export function createsCycle(edges: { source: string; target: string }[], source: string, target: string): boolean {
  if (source === target) {
    return true;
  }
  const adj = new Map<string, string[]>();
  for (const edge of edges) {
    const list = adj.get(edge.source) ?? [];
    list.push(edge.target);
    adj.set(edge.source, list);
  }
  const stack = [target];
  const seen = new Set<string>();
  while (stack.length) {
    const current = stack.pop();
    if (!current) {
      break;
    }
    if (current === source) {
      return true;
    }
    if (seen.has(current)) {
      continue;
    }
    seen.add(current);
    for (const next of adj.get(current) ?? []) {
      stack.push(next);
    }
  }
  return false;
}

const AGENT_ID_RE = /video\.[a-z0-9_]+/gi;

export function parseVideoAgentIds(text: string): string[] {
  const found: string[] = [];
  const seen = new Set<string>();
  for (const match of text.matchAll(AGENT_ID_RE)) {
    const key = match[0].toLowerCase();
    if (key.includes(".template.") || key.includes(".scale.") || seen.has(key)) {
      continue;
    }
    seen.add(key);
    found.push(key);
  }
  return found;
}

export function applyLlmNext(current: ProjectNextSuggestion, reply: string): ProjectNextSuggestion {
  const excerpt = (reply || "").slice(0, 1200);
  const ids = parseVideoAgentIds(reply);
  if (!ids.length) {
    return { ...current, llm_used: true, llm_excerpt: excerpt || current.llm_excerpt };
  }
  const existing = new Map(current.suggestions.map((row) => [row.id, row]));
  const promoted = [];
  const seen = new Set<string>();
  for (const id of ids) {
    const prior = existing.get(id);
    if (!prior || seen.has(id)) {
      continue;
    }
    seen.add(id);
    promoted.push({ ...prior, source: "llm", rank: promoted.length + 1 });
  }
  for (const row of current.suggestions) {
    if (!seen.has(row.id)) {
      promoted.push({ ...row, rank: promoted.length + 1 });
      seen.add(row.id);
    }
  }
  return {
    ...current,
    llm_used: true,
    llm_excerpt: excerpt,
    primary: promoted[0]?.id ?? current.primary,
    suggestions: promoted,
  };
}
