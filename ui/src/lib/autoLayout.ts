/** DAG auto-layout for React Flow workflow diagrams. No elk/dagre. */

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

export type LayoutAlgorithm = "layered-lr" | "layered-tb" | "grid" | "radial" | "force";

export const DEFAULT_LAYOUT_ALGORITHM: LayoutAlgorithm = "force";

export const LAYOUT_ALGORITHMS: { id: LayoutAlgorithm; label: string; hint: string }[] = [
  { id: "force", label: "Force", hint: "Spring-embedder organic layout (default)" },
  { id: "layered-lr", label: "Layered →", hint: "Sugiyama, left to right" },
  { id: "layered-tb", label: "Layered ↓", hint: "Sugiyama, top to bottom" },
  { id: "grid", label: "Grid", hint: "Regular rows and columns" },
  { id: "radial", label: "Radial", hint: "Rings around the start node" },
];

export type LayoutOptions = {
  algorithm?: LayoutAlgorithm;
  direction?: "LR" | "TB";
  rankGap?: number;
  packGap?: number;
};

export function resolveLayoutAlgorithm(options: LayoutOptions = {}): LayoutAlgorithm {
  if (options.algorithm) {
    return options.algorithm;
  }
  if (options.direction === "TB") {
    return "layered-tb";
  }
  if (options.direction === "LR") {
    return "layered-lr";
  }
  return DEFAULT_LAYOUT_ALGORITHM;
}

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

function gridLayoutPositions(
  nodes: LayoutSize[],
  edges: LayoutEdge[],
  options: LayoutOptions = {},
): Record<string, { x: number; y: number }> {
  const packGap = options.packGap ?? 48;
  const layered = autoLayoutPositions(nodes, edges, { ...options, direction: "LR" });
  const ranked = nodes
    .slice()
    .sort((left, right) => {
      const leftPos = layered[left.id] || { x: 0, y: 0 };
      const rightPos = layered[right.id] || { x: 0, y: 0 };
      return leftPos.x - rightPos.x || leftPos.y - rightPos.y || left.id.localeCompare(right.id);
    });
  const cols = Math.max(1, Math.ceil(Math.sqrt(ranked.length)));
  const colWidth: number[] = Array.from({ length: cols }, () => 0);
  const rowHeight: number[] = [];
  ranked.forEach((node, index) => {
    const col = index % cols;
    const row = Math.floor(index / cols);
    colWidth[col] = Math.max(colWidth[col], node.width);
    rowHeight[row] = Math.max(rowHeight[row] ?? 0, node.height);
  });
  const colX: number[] = [];
  let x = 0;
  for (let col = 0; col < cols; col += 1) {
    colX[col] = x;
    x += colWidth[col] + packGap;
  }
  const rowY: number[] = [];
  let y = 0;
  for (let row = 0; row < rowHeight.length; row += 1) {
    rowY[row] = y;
    y += rowHeight[row] + packGap;
  }
  const positions: Record<string, { x: number; y: number }> = {};
  ranked.forEach((node, index) => {
    const col = index % cols;
    const row = Math.floor(index / cols);
    positions[node.id] = { x: colX[col], y: rowY[row] };
  });
  return positions;
}

function radialLayoutPositions(
  nodes: LayoutSize[],
  edges: LayoutEdge[],
  options: LayoutOptions = {},
): Record<string, { x: number; y: number }> {
  const rankGap = options.rankGap ?? 120;
  const layered = autoLayoutPositions(nodes, edges, { ...options, direction: "LR" });
  const root =
    nodes.find((node) => node.rankHint === 0)?.id ||
    nodes.slice().sort((left, right) => (layered[left.id]?.x ?? 0) - (layered[right.id]?.x ?? 0))[0]?.id;
  const outgoing = new Map<string, string[]>();
  for (const node of nodes) {
    outgoing.set(node.id, []);
  }
  for (const edge of edges) {
    if (edge.source && edge.target && edge.source !== edge.target && outgoing.has(edge.source) && outgoing.has(edge.target)) {
      outgoing.get(edge.source)?.push(edge.target);
    }
  }
  const ring = new Map<string, number>();
  const queue: string[] = [];
  if (root) {
    ring.set(root, 0);
    queue.push(root);
  }
  while (queue.length) {
    const id = queue.shift() as string;
    const depth = ring.get(id) ?? 0;
    for (const next of outgoing.get(id) ?? []) {
      if (!ring.has(next)) {
        ring.set(next, depth + 1);
        queue.push(next);
      }
    }
  }
  let extra = Math.max(0, ...[...ring.values()], 0) + 1;
  for (const node of nodes) {
    if (!ring.has(node.id)) {
      ring.set(node.id, extra);
      extra += 1;
    }
  }
  const byRing = new Map<number, LayoutSize[]>();
  for (const node of nodes) {
    const depth = ring.get(node.id) ?? 0;
    const list = byRing.get(depth) ?? [];
    list.push(node);
    byRing.set(depth, list);
  }
  const maxSize = Math.max(...nodes.map((node) => Math.max(node.width, node.height)), 160);
  const positions: Record<string, { x: number; y: number }> = {};
  const rings = [...byRing.keys()].sort((left, right) => left - right);
  for (const depth of rings) {
    const list = byRing.get(depth) ?? [];
    if (depth === 0 && list.length === 1) {
      positions[list[0].id] = { x: 0, y: 0 };
      continue;
    }
    const radius = Math.max(depth, 1) * (maxSize + rankGap);
    list.forEach((node, index) => {
      const angle = -Math.PI / 2 + (2 * Math.PI * index) / Math.max(list.length, 1);
      positions[node.id] = {
        x: Math.round(Math.cos(angle) * radius),
        y: Math.round(Math.sin(angle) * radius),
      };
    });
  }
  const minX = Math.min(...Object.values(positions).map((item) => item.x));
  const minY = Math.min(...Object.values(positions).map((item) => item.y));
  for (const id of Object.keys(positions)) {
    positions[id] = { x: positions[id].x - minX, y: positions[id].y - minY };
  }
  return positions;
}

function forceLayoutPositions(
  nodes: LayoutSize[],
  edges: LayoutEdge[],
  options: LayoutOptions = {},
): Record<string, { x: number; y: number }> {
  const packGap = options.packGap ?? 48;
  const seed = autoLayoutPositions(nodes, edges, { ...options, direction: "LR" });
  const items = nodes.map((node) => ({
    id: node.id,
    x: seed[node.id]?.x ?? 0,
    y: seed[node.id]?.y ?? 0,
    w: node.width,
    h: node.height,
  }));
  const index = new Map(items.map((item, i) => [item.id, i]));
  const springs: { a: number; b: number }[] = [];
  for (const edge of edges) {
    const a = index.get(edge.source);
    const b = index.get(edge.target);
    if (a === undefined || b === undefined || a === b) {
      continue;
    }
    springs.push({ a, b });
  }
  const rest = 280 + packGap;
  for (let iter = 0; iter < 80; iter += 1) {
    const disp = items.map(() => ({ x: 0, y: 0 }));
    for (let i = 0; i < items.length; i += 1) {
      for (let j = i + 1; j < items.length; j += 1) {
        let dx = items[i].x - items[j].x;
        let dy = items[i].y - items[j].y;
        let dist2 = dx * dx + dy * dy;
        if (dist2 < 16) {
          dx = ((i + 1) * 13) % 11;
          dy = ((j + 1) * 17) % 11;
          dist2 = dx * dx + dy * dy;
        }
        const force = 180000 / dist2;
        const dist = Math.sqrt(dist2);
        disp[i].x += (dx / dist) * force;
        disp[i].y += (dy / dist) * force;
        disp[j].x -= (dx / dist) * force;
        disp[j].y -= (dy / dist) * force;
      }
    }
    for (const spring of springs) {
      const a = items[spring.a];
      const b = items[spring.b];
      const dx = b.x - a.x;
      const dy = b.y - a.y;
      const dist = Math.max(Math.sqrt(dx * dx + dy * dy), 1);
      const pull = (dist - rest) * 0.06;
      disp[spring.a].x += (dx / dist) * pull;
      disp[spring.a].y += (dy / dist) * pull;
      disp[spring.b].x -= (dx / dist) * pull;
      disp[spring.b].y -= (dy / dist) * pull;
    }
    const cool = 0.92 ** (iter / 12);
    for (let i = 0; i < items.length; i += 1) {
      items[i].x += Math.max(-48, Math.min(48, disp[i].x * cool));
      items[i].y += Math.max(-48, Math.min(48, disp[i].y * cool));
    }
  }
  for (let pass = 0; pass < 10; pass += 1) {
    for (let i = 0; i < items.length; i += 1) {
      for (let j = i + 1; j < items.length; j += 1) {
        const dx = items[j].x - items[i].x;
        const dy = items[j].y - items[i].y;
        const minX = (items[i].w + items[j].w) / 2 + packGap;
        const minY = (items[i].h + items[j].h) / 2 + packGap;
        if (Math.abs(dx) >= minX || Math.abs(dy) >= minY) {
          continue;
        }
        const overlapX = minX - Math.abs(dx);
        const overlapY = minY - Math.abs(dy);
        if (overlapX < overlapY) {
          const push = (overlapX / 2) * (dx === 0 ? 1 : Math.sign(dx) || 1);
          items[i].x -= push;
          items[j].x += push;
        } else {
          const push = (overlapY / 2) * (dy === 0 ? 1 : Math.sign(dy) || 1);
          items[i].y -= push;
          items[j].y += push;
        }
      }
    }
  }
  const minX = Math.min(...items.map((item) => item.x));
  const minY = Math.min(...items.map((item) => item.y));
  const positions: Record<string, { x: number; y: number }> = {};
  for (const item of items) {
    positions[item.id] = { x: Math.round(item.x - minX), y: Math.round(item.y - minY) };
  }
  return positions;
}

export function layoutPositions(
  nodes: LayoutSize[],
  edges: LayoutEdge[],
  options: LayoutOptions = {},
): Record<string, { x: number; y: number }> {
  const algorithm = resolveLayoutAlgorithm(options);
  if (algorithm === "layered-tb") {
    return autoLayoutPositions(nodes, edges, { ...options, direction: "TB" });
  }
  if (algorithm === "grid") {
    return gridLayoutPositions(nodes, edges, options);
  }
  if (algorithm === "radial") {
    return radialLayoutPositions(nodes, edges, options);
  }
  if (algorithm === "force") {
    return forceLayoutPositions(nodes, edges, options);
  }
  return autoLayoutPositions(nodes, edges, { ...options, direction: "LR" });
}

export function layoutHasOverlap(
  nodes: {
    id: string;
    position: { x: number; y: number };
    measured?: { width?: number; height?: number };
    width?: number;
    height?: number;
  }[],
  gap = 8,
  defaults = { width: 320, height: 220 },
): boolean {
  const boxes = nodes.map((node) => ({
    x: node.position.x,
    y: node.position.y,
    w: node.measured?.width || node.width || defaults.width,
    h: node.measured?.height || node.height || defaults.height,
  }));
  for (let i = 0; i < boxes.length; i += 1) {
    for (let j = i + 1; j < boxes.length; j += 1) {
      const left = boxes[i];
      const right = boxes[j];
      if (
        left.x < right.x + right.w + gap &&
        left.x + left.w + gap > right.x &&
        left.y < right.y + right.h + gap &&
        left.y + left.h + gap > right.y
      ) {
        return true;
      }
    }
  }
  return false;
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
  const positions = layoutPositions(sizes, edges, options);
  return nodes.map((node) => {
    const next = positions[node.id];
    return next ? { ...node, position: next } : node;
  });
}
