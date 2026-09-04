import { afterEach, describe, expect, it, vi } from "vitest";
import { createClient } from "../src/api/v3";
import {
  appendLog,
  clipLogText,
  logApi,
  logUi,
  resetLogsForTests,
  shouldSkipApiLog,
  snapshot,
} from "../src/log/bus";
import { enqueueLogPersist, flushLogsNow, resetLogPersistForTests, startLogSink } from "../src/log/persist";

const mutation = {
  actor: "human_operator" as const,
  reason: "log test",
  expectedParent: "none",
  dryRun: true,
};

afterEach(() => {
  resetLogsForTests();
  resetLogPersistForTests();
  vi.unstubAllGlobals();
});

describe("runtime log bus", () => {
  it("keeps api and ui channels separate", () => {
    logApi("GET /api/v3/agents 200 4ms", '{"agents":[]}');
    logUi("chat send video.director", "hello");
    expect(snapshot("api").map((entry) => entry.message)).toEqual(["GET /api/v3/agents 200 4ms"]);
    expect(snapshot("ui").map((entry) => entry.message)).toEqual(["chat send video.director"]);
    expect(snapshot("api")[0].ts).toMatch(/^\d{4}-\d{2}-\d{2}T/);
    expect(snapshot("ui")[0].detail).toBe("hello");
  });

  it("skips health and debug sink traffic", () => {
    expect(shouldSkipApiLog("/health")).toBe(true);
    expect(shouldSkipApiLog("http://127.0.0.1:18080/health")).toBe(true);
    expect(shouldSkipApiLog("/debug/logs")).toBe(true);
    expect(shouldSkipApiLog("http://127.0.0.1:18080/debug/logs")).toBe(true);
    expect(shouldSkipApiLog("/api/v3/agents")).toBe(false);
  });

  it("clips oversized payloads", () => {
    expect(clipLogText("abcd", 3)).toBe("abc…(+1b)");
  });
});

describe("api client log capture", () => {
  it("records method, path, status, and skips /health", async () => {
    const client = createClient({
      getBaseUrl: () => "http://127.0.0.1:18080",
      getMutation: () => mutation,
      fetchImpl: async () => {
        return new Response(JSON.stringify({ status: "ok", agents: [] }), {
          status: 200,
          headers: { "Content-Type": "application/json" },
        });
      },
    });
    await client.getHealth();
    await client.listAgents();
    expect(snapshot("api").some((entry) => entry.message.includes("/health"))).toBe(false);
    expect(snapshot("api").some((entry) => entry.message.includes("GET /api/v3/agents 200"))).toBe(true);
  });
});

describe("debug log file sink", () => {
  it("posts timestamped entries to /debug/logs", async () => {
    const bodies: unknown[] = [];
    vi.stubGlobal(
      "fetch",
      async (input: string, init?: RequestInit) => {
        expect(input).toBe("http://127.0.0.1:18080/debug/logs");
        bodies.push(JSON.parse(String(init?.body)));
        return new Response(
          JSON.stringify({
            ok: true,
            files: {
              api: "./logs/debug/session-api.log",
              ui: "./logs/debug/session-ui.log",
            },
          }),
          { status: 200, headers: { "Content-Type": "application/json" } },
        );
      },
    );
    startLogSink(() => "http://127.0.0.1:18080");
    const entry = appendLog({
      channel: "ui",
      message: "run common.health",
      detail: "trace-1",
    });
    enqueueLogPersist(entry);
    await flushLogsNow();
    expect(bodies).toHaveLength(1);
    const body = bodies[0] as { session: string; entries: { ts: string; message: string; channel: string }[] };
    expect(body.session.length).toBeGreaterThan(8);
    expect(body.entries[0].channel).toBe("ui");
    expect(body.entries[0].message).toBe("run common.health");
    expect(body.entries[0].ts).toMatch(/^\d{4}-\d{2}-\d{2}T/);
  });
});
