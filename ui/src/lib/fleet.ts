import type { AgentSummary, RunResult, StructureResponse } from "../api/types";
import type { AgentCardModel } from "../components/AgentCard";

export type FleetListClient = {
  listAgents: () => Promise<{ agents: AgentSummary[] }>;
};

export type FleetFallbackClient = {
  getStructure: (agentId: string) => Promise<StructureResponse>;
};

export function runStatusFor(run: RunResult | undefined): AgentCardModel["runStatus"] {
  if (!run) {
    return "unavailable";
  }
  if (run.cancelled) {
    return "cancelled";
  }
  if (run.containment_stop) {
    return "failed";
  }
  return "complete";
}

export function summariesToCards(
  summaries: AgentSummary[],
  lastRuns: Record<string, RunResult> = {},
): AgentCardModel[] {
  return summaries.map((summary) => ({
    agent_id: summary.agent_id,
    folder: summary.folder,
    role: summary.role,
    schema_version: summary.schema_version,
    memoryMode: summary.memory_mode,
    runStatus: runStatusFor(lastRuns[summary.agent_id]),
  }));
}

export async function loadFleetList(client: FleetListClient): Promise<AgentSummary[]> {
  const listed = await client.listAgents();
  return Array.isArray(listed.agents) ? listed.agents : [];
}

export async function loadFleetFallback(
  client: FleetFallbackClient,
  knownIds: string[],
): Promise<AgentSummary[]> {
  const probed = await Promise.allSettled(knownIds.map((id) => client.getStructure(id)));
  return probed.flatMap((result) => {
    if (result.status !== "fulfilled") {
      return [];
    }
    return [
      {
        agent_id: result.value.agent_id,
        folder: result.value.folder,
        structure_id: result.value.structure_id,
        schema_version: result.value.schema_version,
        role: "",
      },
    ];
  });
}
