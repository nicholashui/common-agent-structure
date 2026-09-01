import { describe, expect, it } from "vitest";
import type { AgentSummary } from "../src/api/types";
import { loadFleetList, summariesToCards } from "../src/lib/fleet";

function summaries(count: number): AgentSummary[] {
  return Array.from({ length: count }, (_, index) => ({
    agent_id: `video.agent-${String(index).padStart(3, "0")}`,
    folder: `agents/video.agent-${String(index).padStart(3, "0")}`,
    structure_id: "casops.common_agent.v3",
    schema_version: "3.0",
    role: "role",
    memory_mode: "none",
  }));
}

describe("fleet list load", () => {
  it("maps a large list with a constant number of list fetches", async () => {
    const agents = summaries(80);
    const calls: string[] = [];
    const client = {
      listAgents: async () => {
        calls.push("GET /api/v3/agents");
        return { agents };
      },
      getAttestation: async () => {
        calls.push("GET attestation");
        return { status: "host_reference" };
      },
      getResolved: async () => {
        calls.push("GET resolved");
        return {};
      },
      getMemoryPolicy: async () => {
        calls.push("GET memory-policy");
        return { mode: "none" };
      },
    };
    const listed = await loadFleetList(client);
    const cards = summariesToCards(listed, {});
    expect(listed.map((row) => row.agent_id)).toEqual(agents.map((row) => row.agent_id));
    expect(cards).toHaveLength(80);
    expect(cards.map((card) => card.agent_id)).toEqual(agents.map((row) => row.agent_id));
    expect(calls).toEqual(["GET /api/v3/agents"]);
  });
});
