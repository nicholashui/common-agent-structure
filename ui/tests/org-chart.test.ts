import { describe, expect, it } from "vitest";
import { listAgentGroups } from "../src/lib/agents";
import {
  agentsInGroup,
  agentCategory,
  buildOrgChart,
  layoutExtent,
  nodesForInitialFit,
  ORG_MIN_READABLE_ZOOM,
} from "../src/lib/orgChart";

const sample = [
  { agent_id: "video.director", role: "Director", va_category: "1-ATL" },
  { agent_id: "video.cinematographer", role: "Camera", va_category: "2-Cam" },
  { agent_id: "video.producer", role: "Producer", va_category: "1-ATL" },
  { agent_id: "specials.planner-agent", role: "Planner", va_category: "" },
  { agent_id: "common.health", role: "Health" },
];

describe("agent org chart", () => {
  it("lists packs present in the fleet as Agent Groups", () => {
    expect(listAgentGroups(sample)).toEqual(["video", "specials", "other"]);
    expect(listAgentGroups(sample.filter((row) => row.agent_id.startsWith("video.")))).toEqual(["video"]);
  });

  it("groups the selected pack by category and keeps every agent as a leaf", () => {
    const video = agentsInGroup(sample, "video");
    expect(video.map((row) => row.agent_id)).toEqual([
      "video.director",
      "video.cinematographer",
      "video.producer",
    ]);
    const graph = buildOrgChart(sample, "video");
    const agentNodes = graph.nodes.filter((node) => node.data.kind === "agent");
    expect(agentNodes.map((node) => node.data.agentId).sort()).toEqual(
      video.map((row) => row.agent_id).sort(),
    );
    expect(graph.nodes.some((node) => node.id === "group:video" && node.data.kind === "group")).toBe(true);
    expect(graph.nodes.filter((node) => node.data.kind === "category").map((node) => node.data.label).sort()).toEqual(
      ["1-ATL", "2-Cam"],
    );
    const agentIds = new Set(agentNodes.map((node) => node.id));
    for (const agent of video) {
      expect(graph.edges.some((edge) => edge.target === `agent:${agent.agent_id}`)).toBe(true);
    }
    expect(agentIds.has("agent:specials.planner-agent")).toBe(false);
  });

  it("skips the category layer when every agent is uncategorized", () => {
    const graph = buildOrgChart(sample, "specials");
    expect(graph.nodes.filter((node) => node.data.kind === "category")).toEqual([]);
    expect(graph.nodes.filter((node) => node.data.kind === "agent")).toHaveLength(1);
    expect(graph.edges).toEqual([
      {
        id: "e:group:specials->specials.planner-agent",
        source: "group:specials",
        target: "agent:specials.planner-agent",
        type: "smoothstep",
      },
    ]);
  });

  it("treats empty va_category as uncategorized", () => {
    expect(agentCategory({})).toBe("uncategorized");
    expect(agentCategory({ va_category: "1-ATL" })).toBe("1-ATL");
  });

  it("keeps every member as a distinctly placed leaf on a video-scale pack", () => {
    const pack = videoScalePack(120, 8);
    const members = agentsInGroup(pack, "video");
    expect(members).toHaveLength(120);
    const graph = buildOrgChart(pack, "video");
    const leaves = graph.nodes.filter((node) => node.data.kind === "agent");
    expect(leaves.map((node) => node.data.agentId).sort()).toEqual(members.map((row) => row.agent_id).sort());
    const keys = new Set(leaves.map((node) => `${node.position.x},${node.position.y}`));
    expect(keys.size).toBe(leaves.length);
    const categories = graph.nodes.filter((node) => node.data.kind === "category");
    expect(categories).toHaveLength(8);
    const fit = nodesForInitialFit(graph.nodes);
    expect(fit.some((node) => node.data.kind === "group")).toBe(true);
    expect(fit.every((node) => node.data.kind !== "agent")).toBe(true);
    expect(fit.length).toBeLessThan(graph.nodes.length);
    expect(ORG_MIN_READABLE_ZOOM).toBeGreaterThanOrEqual(0.5);
  });

  it("grows the layout bounding box when categories or leaves increase", () => {
    const compact = buildOrgChart(videoScalePack(24, 2), "video");
    const wider = buildOrgChart(videoScalePack(24, 6), "video");
    const taller = buildOrgChart(videoScalePack(96, 2), "video");
    const compactBox = layoutExtent(compact.nodes);
    const widerBox = layoutExtent(wider.nodes);
    const tallerBox = layoutExtent(taller.nodes);
    expect(widerBox.width).toBeGreaterThan(compactBox.width);
    expect(tallerBox.height).toBeGreaterThan(compactBox.height);
    expect(compactBox.width).toBeGreaterThan(0);
    expect(compactBox.height).toBeGreaterThan(0);
  });
});

function videoScalePack(count: number, categoryCount: number) {
  return Array.from({ length: count }, (_, index) => ({
    agent_id: `video.agent-${String(index).padStart(3, "0")}`,
    role: "role",
    va_category: `${(index % categoryCount) + 1}-Cat`,
  }));
}
