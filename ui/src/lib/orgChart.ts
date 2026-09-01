import { agentPack, type AgentPack } from "./agents";

export const ORG_NODE_WIDTH = 184;
export const ORG_NODE_HEIGHT = 68;
export const ORG_MIN_READABLE_ZOOM = 0.5;
const COL_GAP = 24;
const ROW_GAP = 28;
const LEVEL_GAP = 96;
const LEAF_COLS = 2;
const CATEGORY_COLS = 3;

export type OrgKind = "group" | "category" | "agent";

export interface OrgAgent {
  agent_id: string;
  role?: string;
  va_category?: string;
}

export interface OrgNodeData {
  kind: OrgKind;
  label: string;
  subtitle?: string;
  agentId?: string;
  count?: number;
  [key: string]: unknown;
}

export interface OrgNodeDraft {
  id: string;
  type: "orgNode";
  position: { x: number; y: number };
  data: OrgNodeData;
}

export interface OrgEdgeDraft {
  id: string;
  source: string;
  target: string;
  type: "smoothstep";
}

export function agentCategory(agent: OrgAgent): string {
  const raw = (agent.va_category || "").trim();
  return raw || "uncategorized";
}

export function agentsInGroup(agents: OrgAgent[], group: Exclude<AgentPack, "all">): OrgAgent[] {
  return agents.filter((agent) => agentPack(agent.agent_id) === group);
}

export function buildOrgChart(
  agents: OrgAgent[],
  group: Exclude<AgentPack, "all">,
): { nodes: OrgNodeDraft[]; edges: OrgEdgeDraft[] } {
  const members = agentsInGroup(agents, group).slice().sort((a, b) => a.agent_id.localeCompare(b.agent_id));
  const nodes: OrgNodeDraft[] = [];
  const edges: OrgEdgeDraft[] = [];

  const buckets = new Map<string, OrgAgent[]>();
  for (const agent of members) {
    const category = agentCategory(agent);
    const list = buckets.get(category) ?? [];
    list.push(agent);
    buckets.set(category, list);
  }
  const categories = [...buckets.keys()].sort((a, b) => a.localeCompare(b));
  const useCategories = categories.length > 1;

  const slotWidth = LEAF_COLS * (ORG_NODE_WIDTH + COL_GAP);
  const catCols = Math.min(CATEGORY_COLS, Math.max(categories.length, 1));
  const treeWidth = Math.max(ORG_NODE_WIDTH, (useCategories ? catCols : 1) * slotWidth);
  const rootX = (treeWidth - ORG_NODE_WIDTH) / 2;

  nodes.push({
    id: `group:${group}`,
    type: "orgNode",
    position: { x: rootX, y: 0 },
    data: { kind: "group", label: group, subtitle: "Agent Group", count: members.length },
  });

  if (!members.length) {
    return { nodes, edges };
  }

  if (!useCategories) {
    layoutLeaves(nodes, edges, members, `group:${group}`, Math.max(0, rootX - ((LEAF_COLS - 1) * (ORG_NODE_WIDTH + COL_GAP)) / 2), LEVEL_GAP);
    return { nodes, edges };
  }

  const rowMaxHeight = new Map<number, number>();
  categories.forEach((category, index) => {
    const row = Math.floor(index / catCols);
    const height = leafBlockHeight(buckets.get(category)?.length ?? 0);
    rowMaxHeight.set(row, Math.max(rowMaxHeight.get(row) ?? 0, height));
  });

  function categoryRowTop(row: number): number {
    let top = LEVEL_GAP;
    for (let prior = 0; prior < row; prior += 1) {
      top += ORG_NODE_HEIGHT + LEVEL_GAP + (rowMaxHeight.get(prior) ?? 0);
    }
    return top;
  }

  categories.forEach((category, index) => {
    const catId = `category:${group}:${category}`;
    const col = index % catCols;
    const row = Math.floor(index / catCols);
    const slotX = col * slotWidth;
    const top = categoryRowTop(row);
    nodes.push({
      id: catId,
      type: "orgNode",
      position: { x: slotX + (slotWidth - ORG_NODE_WIDTH) / 2, y: top },
      data: {
        kind: "category",
        label: category,
        subtitle: "category",
        count: buckets.get(category)?.length ?? 0,
      },
    });
    edges.push({
      id: `e:${group}->${category}`,
      source: `group:${group}`,
      target: catId,
      type: "smoothstep",
    });
    layoutLeaves(nodes, edges, buckets.get(category) ?? [], catId, slotX, top + LEVEL_GAP);
  });

  return { nodes, edges };
}

function leafBlockHeight(count: number): number {
  const rows = Math.max(1, Math.ceil(count / LEAF_COLS));
  return rows * (ORG_NODE_HEIGHT + ROW_GAP);
}

export function layoutExtent(nodes: OrgNodeDraft[]): {
  minX: number;
  minY: number;
  maxX: number;
  maxY: number;
  width: number;
  height: number;
} {
  if (!nodes.length) {
    return { minX: 0, minY: 0, maxX: 0, maxY: 0, width: 0, height: 0 };
  }
  let minX = Infinity;
  let minY = Infinity;
  let maxX = -Infinity;
  let maxY = -Infinity;
  for (const node of nodes) {
    minX = Math.min(minX, node.position.x);
    minY = Math.min(minY, node.position.y);
    maxX = Math.max(maxX, node.position.x + ORG_NODE_WIDTH);
    maxY = Math.max(maxY, node.position.y + ORG_NODE_HEIGHT);
  }
  return { minX, minY, maxX, maxY, width: maxX - minX, height: maxY - minY };
}

export function nodesForInitialFit(nodes: OrgNodeDraft[]): OrgNodeDraft[] {
  const group = nodes.filter((node) => node.data.kind === "group");
  const categories = nodes.filter((node) => node.data.kind === "category");
  if (categories.length) {
    const firstRowY = Math.min(...categories.map((node) => node.position.y));
    return [...group, ...categories.filter((node) => node.position.y === firstRowY)];
  }
  const leaves = nodes.filter((node) => node.data.kind === "agent");
  return [...group, ...leaves.slice(0, LEAF_COLS * 3)];
}

function layoutLeaves(
  nodes: OrgNodeDraft[],
  edges: OrgEdgeDraft[],
  members: OrgAgent[],
  parentId: string,
  originX: number,
  originY: number,
): void {
  members.forEach((agent, index) => {
    const col = index % LEAF_COLS;
    const row = Math.floor(index / LEAF_COLS);
    const id = `agent:${agent.agent_id}`;
    nodes.push({
      id,
      type: "orgNode",
      position: {
        x: originX + col * (ORG_NODE_WIDTH + COL_GAP),
        y: originY + row * (ORG_NODE_HEIGHT + ROW_GAP),
      },
      data: {
        kind: "agent",
        label: agent.agent_id,
        subtitle: agent.role || "agent",
        agentId: agent.agent_id,
      },
    });
    edges.push({
      id: `e:${parentId}->${agent.agent_id}`,
      source: parentId,
      target: id,
      type: "smoothstep",
    });
  });
}
