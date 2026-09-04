import { describe, expect, it } from "vitest";
import {
  collectAgentIds,
  filterAgentCards,
  filterAgentIds,
  groupFleetCards,
  listAgentCategories,
  relativeAgentFolder,
} from "../src/lib/agents";

const sample = [
  { agent_id: "casops.template.baseline_safe", role: "template", folder: "agents/_template_v3" },
  { agent_id: "common.health", role: "health", folder: "agents/common.health" },
  { agent_id: "specials.planner-agent", role: "planner", folder: "agents/specials.planner-agent" },
  { agent_id: "video.director", role: "director", folder: "agents/video.director" },
  { agent_id: "video.screenwriter", role: "writer", folder: "agents/video.screenwriter" },
];

describe("relative agent folder", () => {
  it("strips drive-letter roots down to agents/<id>", () => {
    expect(relativeAgentFolder("C:\\Project\\common-agent-structure\\agents\\video.director", "video.director")).toBe(
      "agents/video.director",
    );
    expect(relativeAgentFolder("C:/tmp/agents/_template_v3")).toBe("agents/_template_v3");
    expect(relativeAgentFolder("agents/specials.planner-agent")).toBe("agents/specials.planner-agent");
    expect(relativeAgentFolder("", "common.health")).toBe("agents/common.health");
  });
});

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

  it("filters fleet cards by va_category", () => {
    const cards = [
      { agent_id: "video.director", role: "director", folder: "agents/video.director", va_category: "1-ATL" },
      { agent_id: "video.cinematographer", role: "camera", folder: "agents/video.cinematographer", va_category: "2-Cam" },
    ];
    expect(filterAgentCards(cards, "1-ATL", "all").map((row) => row.agent_id)).toEqual(["video.director"]);
    expect(filterAgentCards(cards, "", "all", "2-Cam").map((row) => row.agent_id)).toEqual([
      "video.cinematographer",
    ]);
  });

  it("lists declared categories for the Agent Swarm filter", () => {
    expect(
      listAgentCategories([
        { va_category: "1-ATL" },
        { va_category: "2-Cam" },
        { va_category: "1-ATL" },
        { va_category: "" },
      ]),
    ).toEqual(["1-ATL", "2-Cam"]);
  });

  it("matches header search by category as well as agent_id", () => {
    const cards = [
      { agent_id: "video.director", va_category: "1-ATL" },
      { agent_id: "video.cinematographer", va_category: "2-Cam" },
    ];
    expect(filterAgentIds(["video.director", "video.cinematographer"], "1-ATL", cards)).toEqual([
      "video.director",
    ]);
  });
});

describe("fleet category grouping", () => {
  const sample = [
    { agent_id: "video.director", va_category: "1-ATL" },
    { agent_id: "video.producer", va_category: "1-ATL" },
    { agent_id: "video.cinematographer", va_category: "2-Cam" },
    { agent_id: "specials.planner-agent", va_category: "" },
    { agent_id: "common.health" },
  ];

  it("groups video agents by va_category and leaves uncategorized packs flat", () => {
    const groups = groupFleetCards(sample, "all");
    expect(groups.map((group) => group.pack)).toEqual(["video", "specials", "other"]);
    expect(groups[0].showCategory).toBe(true);
    expect(groups[0].categories.map((bucket) => [bucket.category, bucket.items.map((item) => item.agent_id)])).toEqual([
      ["1-ATL", ["video.director", "video.producer"]],
      ["2-Cam", ["video.cinematographer"]],
    ]);
    expect(groups[1].showCategory).toBe(false);
    expect(groups[1].categories[0].items.map((item) => item.agent_id)).toEqual(["specials.planner-agent"]);
    expect(groups[2].showCategory).toBe(false);
    expect(groups[2].categories[0].items.map((item) => item.agent_id)).toEqual(["common.health"]);
  });

  it("keeps category groups when a pack chip is selected", () => {
    const groups = groupFleetCards(sample, "video");
    expect(groups).toHaveLength(1);
    expect(groups[0].pack).toBe("video");
    expect(groups[0].categories.map((bucket) => bucket.category)).toEqual(["1-ATL", "2-Cam"]);
  });

  it("does not invent categories when none are declared", () => {
    const groups = groupFleetCards(sample.filter((row) => row.agent_id.startsWith("specials.")), "specials");
    expect(groups[0].showCategory).toBe(false);
    expect(groups[0].categories).toHaveLength(1);
  });
});
