import { describe, expect, it } from "vitest";
import { CLIENT_BINDINGS, COMPANION_V3_PATHS, SPEC_V3_PATHS } from "../src/api/paths";
import { createClient } from "../src/api/v3";

const mutation = {
  actor: "human_operator" as const,
  reason: "contract test",
  expectedParent: "none",
  dryRun: true,
};

function mockClient(handler: (url: string, init?: RequestInit) => Promise<Response> | Response) {
  return createClient({
    getBaseUrl: () => "http://127.0.0.1:18080",
    getMutation: () => mutation,
    fetchImpl: async (url, init) => handler(url, init),
  });
}

describe("SPEC_V3 client coverage", () => {
  it("binds a client operation to every spec §19 path", () => {
    const companion = new Set(COMPANION_V3_PATHS.map(([method, path]) => `${method} ${path}`));
    const bound = new Set(
      Object.values(CLIENT_BINDINGS)
        .map((pair) => `${pair[0]} ${pair[1]}`)
        .filter((key) => !companion.has(key)),
    );
    for (const [method, path] of SPEC_V3_PATHS) {
      expect(bound.has(`${method} ${path}`), `missing ${method} ${path}`).toBe(true);
    }
    expect(bound.size).toBe(SPEC_V3_PATHS.length);
  });

  it("binds the companion list path", () => {
    expect(CLIENT_BINDINGS.listAgents).toEqual(COMPANION_V3_PATHS[0]);
  });

  it("invokes each bound path through the client", async () => {
    const seen: string[] = [];
    const client = mockClient((url, init) => {
      const path = url.replace("http://127.0.0.1:18080", "").split("?")[0];
      seen.push(`${init?.method ?? "GET"} ${path}`);
      return new Response(JSON.stringify({ ok: true, agents: [], plugins: [], records: [], candidates: [], incidents: [], ledger: [], fixtures: [], matrix: [] }), {
        status: 200,
        headers: { "Content-Type": "application/json" },
      });
    });

    await client.getStructure("a");
    await client.getResolved("a");
    await client.composePreview("a");
    await client.getRuntimePlan("a");
    await client.getRuntimeCapabilities("a");
    await client.getCapabilitiesMatrix("a");
    await client.verifyCapabilities("a");
    await client.getContextBudget("a");
    await client.getCacheStats("a");
    await client.invalidateCache("a");
    await client.getProtocols("a");
    await client.getPlugins("a");
    await client.validatePlugins("a");
    await client.getMemoryPolicy("a");
    await client.getMemoryHierarchy("a");
    await client.queryMemory("a", { tenant: "t", subject: "s", text: "note" });
    await client.writeMemoryCandidate("a", { tenant: "t", subject: "s", text: "note" });
    await client.consolidateMemory("a");
    await client.deleteMemory("a", "m1", { tenant: "t", subject: "s" });
    await client.verifyMemoryDeletion("a", "m1", { tenant: "t", subject: "s" });
    await client.getTrace("tr");
    await client.replayTrace("tr");
    await client.replayTrace("tr", "what-if");
    await client.getRootCause("tr");
    await client.getEvidenceGraph("art");
    await client.getIncidents("a");
    await client.runRedteam("a");
    await client.listCandidates("a");
    await client.evaluateCandidate("a", "c1");
    await client.approveCandidate("a", "c1");
    await client.rollback("a", "v1");
    await client.getLedger("a");
    await client.getRegressionSuite("a");
    await client.getAttestation("a");
    await client.getValidationReport("a");
    await client.runAgent("a");
    await client.listAgents();
    await client.listLlmProviders();
    await client.getLlmSettings();
    await client.setLlmSettings("local_deterministic");
    await client.getAgentLlm("a");
    await client.setAgentLlm("a", "openai");
    await client.chatAgent("a", { message: "hello" });

    const normalized = seen.map((row) =>
      row
        .replace("/api/v3/agents/a/", "/api/v3/agents/{agent_id}/")
        .replace("/api/v3/agents/a", "/api/v3/agents")
        .replace("/api/v3/traces/tr", "/api/v3/traces/{trace_id}")
        .replace("/api/v3/artifacts/art", "/api/v3/artifacts/{artifact_id}")
        .replace("/memory/m1", "/memory/{memory_id}")
        .replace("/candidates/c1/", "/candidates/{cid}/")
        .replace("/rollback/v1", "/rollback/{version}"),
    );

    for (const [method, path] of SPEC_V3_PATHS) {
      expect(normalized).toContain(`${method} ${path}`);
    }
    expect(normalized).toContain("GET /api/v3/agents");
    expect(normalized).toContain("GET /api/v3/llm/providers");
    expect(normalized).toContain("GET /api/v3/llm/settings");
    expect(normalized).toContain("POST /api/v3/llm/settings");
    expect(normalized).toContain("GET /api/v3/agents/{agent_id}/llm");
    expect(normalized).toContain("POST /api/v3/agents/{agent_id}/llm");
    expect(normalized).toContain("POST /api/v3/agents/{agent_id}/runtime/chat");
  });
});
