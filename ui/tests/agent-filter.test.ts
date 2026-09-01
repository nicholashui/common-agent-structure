import { describe, expect, it } from "vitest";
import { collectAgentIds, filterAgentCards, filterAgentIds } from "../src/lib/agents";

const sample = [
  { agent_id: "casops.template.baseline_safe", role: "template", folder: "agents/_template_v3" },
  { agent_id: "common.health", role: "health", folder: "agents/common.health" },
  { agent_id: "specials.planner-agent", role: "planner", folder: "agents/specials.planner-agent" },
  { agent_id: "video.director", role: "director", folder: "agents/video.director" },
  { agent_id: "video.screenwriter", role: "writer", folder: "agents/video.screenwriter" },
];

describe("agent list filtering", () => {
  it("returns every id when the query is empty", () => {
    const ids = collectAgentIds(sample, ["extra.one"]);
    expect(ids).toHaveLength(6);
    expect(filterAgentIds(ids, "")).toEqual(ids);
    expect(filterAgentCards(sample, "", "all")).toHaveLength(sample.length);
  });

  it("filters the header switcher and fleet cards by substring", () => {
    const ids = collectAgentIds(sample, []);
    expect(filterAgentIds(ids, "video.")).toEqual(["video.director", "video.screenwriter"]);
    expect(filterAgentCards(sample, "planner", "all").map((row) => row.agent_id)).toEqual([
      "specials.planner-agent",
    ]);
  });

  it("empty query keeps every id on a fleet-sized list", () => {
    const ids = Array.from({ length: 135 }, (_, index) => `video.agent-${String(index).padStart(3, "0")}`);
    ids.push("specials.planner-agent", "common.health", "casops.template.baseline_safe");
    const cards = ids.map((agent_id) => ({ agent_id, role: agent_id, folder: `agents/${agent_id}` }));
    expect(filterAgentIds(ids, "")).toEqual(ids);
    expect(filterAgentIds(ids, "   ")).toEqual(ids);
    expect(filterAgentCards(cards, "", "all").map((row) => row.agent_id)).toEqual(ids);
    expect(filterAgentIds(ids, "missing-substring")).toEqual([]);
  });

  it("pack chips keep other agents reachable", () => {
    expect(filterAgentCards(sample, "", "video").map((row) => row.agent_id)).toEqual([
      "video.director",
      "video.screenwriter",
    ]);
    expect(filterAgentCards(sample, "", "specials").map((row) => row.agent_id)).toEqual([
      "specials.planner-agent",
    ]);
    expect(filterAgentCards(sample, "", "other").map((row) => row.agent_id)).toEqual([
      "casops.template.baseline_safe",
      "common.health",
    ]);
  });
});
