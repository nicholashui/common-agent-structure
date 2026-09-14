/** Layered DAG auto-layout for React Flow workflow diagrams. No elk/dagre. */

export type LayoutSize = {
  id: string;
  width: number;
  height: number;
  rankHint?: number;
};

export type LayoutEdge = {
  source: string;
  target: string;
};

export type LayoutOptions = {
  direction?: "LR" | "TB";
  rankGap?: number;
  packGap?: number;
};

export function autoLayoutPositions(
  nodes: LayoutSize[],
  edges: LayoutEdge[],
  options: LayoutOptions = {},
): Record<string, { x: number; y: number }> {
  const direction = options.direction ?? "LR";
  const rankGap = options.rankGap ?? 88;
  const packGap = options.packGap ?? 32;
  const byId = new Map(nodes.map((node) => [node.id, node]));
  const ids = nodes.map((node) => node.id);
  const outgoing = new Map<string, string[]>();
  const incoming = new Map<string, string[]>();
  for (const id of ids) {
    outgoing.set(id, []);
    incoming.set(id, []);
  }
  const pairs: { source: string; target: string }[] = [];
  for (const edge of edges) {
    if (!edge.source || !edge.target || edge.source === edge.target) {
      continue;
    }
    if (!byId.has(edge.source) || !byId.has(edge.target)) {
      continue;
    }
    pairs.push({ source: edge.source, target: edge.target });
    outgoing.get(edge.source)?.push(edge.target);
    incoming.get(edge.target)?.push(edge.source);
  }

  const seen = new Set<string>();
  const stack = new Set<string>();
  const back = new Set<string>();
  function dfs(id: string) {
    seen.add(id);
    stack.add(id);
    for (const next of outgoing.get(id) ?? []) {
      if (!seen.has(next)) {
        dfs(next);
      } else if (stack.has(next)) {
        back.add(`${id}>${next}`);
      }
    }
    stack.delete(id);
  }
  for (const id of ids) {
    if (!seen.has(id)) {
      dfs(id);
    }
  }

  const fwdIn = new Map<string, string[]>();
  const fwdOut = new Map<string, string[]>();
  for (const id of ids) {
    fwdIn.set(id, []);
    fwdOut.set(id, []);
  }
  for (const pair of pairs) {
    if (back.has(`${pair.source}>${pair.target}`)) {
      continue;
    }
    fwdOut.get(pair.source)?.push(pair.target);
    fwdIn.get(pair.target)?.push(pair.source);
  }

  const rank = new Map<string, number>();
  function getRank(id: string, walking: Set<string>): number {
    const cached = rank.get(id);
    if (cached !== undefined) {
      return cached;
    }
    if (walking.has(id)) {
      return 0;
    }
    walking.add(id);
    const preds = fwdIn.get(id) ?? [];
    const value = preds.length ? Math.max(...preds.map((pred) => getRank(pred, walking))) + 1 : 0;
    walking.delete(id);
    rank.set(id, value);
    return value;
  }
  for (const id of ids) {
    getRank(id, new Set());
  }
  for (const node of nodes) {
    if (node.rankHint === 0) {
      rank.set(node.id, 0);
    }
  }
  let maxRank = Math.max(0, ...[...rank.values()]);
  for (const node of nodes) {
    if (node.rankHint !== undefined && node.rankHint >= 999) {
      rank.set(node.id, maxRank + 1);
    }
  }
  maxRank = Math.max(0, ...[...rank.values()]);

  const layers = new Map<number, string[]>();
  for (const id of ids) {
    const layer = rank.get(id) ?? 0;
    const list = layers.get(layer) ?? [];
    list.push(id);
    layers.set(layer, list);
  }
  const order = new Map<string, number>();
  const ranked = [...layers.keys()].sort((left, right) => left - right);
  for (const layer of ranked) {
    const list = layers.get(layer) ?? [];
    list.sort((left, right) => {
      const leftParents = fwdIn.get(left) ?? [];
      const rightParents = fwdIn.get(right) ?? [];
      const leftBar = leftParents.length
        ? leftParents.reduce((sum, id) => sum + (order.get(id) ?? 0), 0) / leftParents.length
        : 0;
      const rightBar = rightParents.length
        ? rightParents.reduce((sum, id) => sum + (order.get(id) ?? 0), 0) / rightParents.length
        : 0;
      return leftBar - rightBar || left.localeCompare(right);
    });
    list.forEach((id, index) => order.set(id, index));
  }

  const positions: Record<string, { x: number; y: number }> = {};
  if (direction === "TB") {
    let y = 0;
    for (const layer of ranked) {
      const list = layers.get(layer) ?? [];
      const rowHeight = Math.max(...list.map((id) => byId.get(id)?.height ?? 0), 0);
      let x = 0;
      for (const id of list) {
        positions[id] = { x, y };
        x += (byId.get(id)?.width ?? 0) + packGap;
      }
      y += rowHeight + rankGap;
    }
  } else {
    let x = 0;
    for (const layer of ranked) {
      const list = layers.get(layer) ?? [];
      const colWidth = Math.max(...list.map((id) => byId.get(id)?.width ?? 0), 0);
      let y = 0;
      for (const id of list) {
        positions[id] = { x, y };
        y += (byId.get(id)?.height ?? 0) + packGap;
      }
      x += colWidth + rankGap;
    }
  }
  return positions;
}

export function rankHintForKind(kind?: string): number | undefined {
  if (kind === "start" || kind === "group") {
    return 0;
  }
  if (kind === "output") {
    return 999;
  }
  return undefined;
}

export function applyAutoLayout<
  T extends {
    id: string;
    position: { x: number; y: number };
    measured?: { width?: number; height?: number };
    width?: number;
    height?: number;
    data?: { kind?: string };
  },
>(
  nodes: T[],
  edges: LayoutEdge[],
  options: LayoutOptions & { defaultWidth?: number; defaultHeight?: number } = {},
): T[] {
  if (!nodes.length) {
    return nodes;
  }
  const defaultWidth = options.defaultWidth ?? 320;
  const defaultHeight = options.defaultHeight ?? 220;
  const sizes: LayoutSize[] = nodes.map((node) => ({
    id: node.id,
    width: node.measured?.width || node.width || defaultWidth,
    height: node.measured?.height || node.height || defaultHeight,
    rankHint: rankHintForKind(node.data?.kind),
  }));
  const positions = autoLayoutPositions(sizes, edges, options);
  return nodes.map((node) => {
    const next = positions[node.id];
    return next ? { ...node, position: next } : node;
  });
}
