import { describe, expect, it } from "vitest";
import { createClient } from "../src/api/v3";
import { MutationContractError } from "../src/api/types";
import type { MutationContract } from "../src/api/types";

function capture(contract: MutationContract) {
  const calls: { url: string; init: RequestInit }[] = [];
  const client = createClient({
    getBaseUrl: () => "http://127.0.0.1:18080",
    getMutation: () => contract,
    fetchImpl: async (url, init) => {
      calls.push({ url, init: init ?? {} });
      return new Response(JSON.stringify({ ok: true }), {
        status: 200,
        headers: { "Content-Type": "application/json" },
      });
    },
  });
  return { client, calls };
}

function header(init: RequestInit, name: string): string | null {
  const headers = new Headers(init.headers);
  return headers.get(name);
}

describe("mutation headers", () => {
  it("injects the four contract headers on POST", async () => {
    const { client, calls } = capture({
      actor: "human_operator",
      reason: "compose check",
      expectedParent: "none",
      dryRun: true,
    });
    await client.composePreview("casops.template.baseline_safe");
    expect(calls).toHaveLength(1);
    expect(header(calls[0].init, "x-casops-actor")).toBe("human_operator");
    expect(header(calls[0].init, "x-casops-reason")).toBe("compose check");
    expect(header(calls[0].init, "x-casops-expected-parent")).toBe("none");
    expect(header(calls[0].init, "x-casops-dry-run")).toBe("true");
  });

  it("injects headers on DELETE", async () => {
    const { client, calls } = capture({
      actor: "human_operator",
      reason: "forget note",
      expectedParent: "none",
      dryRun: false,
    });
    await client.deleteMemory("agent", "mid", { tenant: "t", subject: "s" });
    expect(header(calls[0].init, "x-casops-dry-run")).toBe("false");
    expect(calls[0].init.method).toBe("DELETE");
  });

  it("does not send mutation headers on GET", async () => {
    const { client, calls } = capture({
      actor: "human_operator",
      reason: "unused",
      expectedParent: "none",
      dryRun: true,
    });
    await client.getStructure("agent");
    expect(header(calls[0].init, "x-casops-actor")).toBeNull();
    expect(header(calls[0].init, "x-casops-reason")).toBeNull();
    expect(header(calls[0].init, "x-casops-expected-parent")).toBeNull();
    expect(header(calls[0].init, "x-casops-dry-run")).toBeNull();
  });

  it("refuses approve when actor is agent_runtime before fetch", async () => {
    const { client, calls } = capture({
      actor: "agent_runtime",
      reason: "self approve",
      expectedParent: "none",
      dryRun: false,
    });
    await expect(client.approveCandidate("agent", "c1")).rejects.toBeInstanceOf(MutationContractError);
    await expect(client.approveCandidate("agent", "c1")).rejects.toMatchObject({ code: "IMP_SELF_APPROVAL" });
    expect(calls).toHaveLength(0);
  });

  it("fails closed when reason is empty", async () => {
    const { client, calls } = capture({
      actor: "human_operator",
      reason: "   ",
      expectedParent: "none",
      dryRun: true,
    });
    await expect(client.composePreview("agent")).rejects.toMatchObject({ code: "IMP_UNSIGNED" });
    expect(calls).toHaveLength(0);
  });

  it("sends a chat fallback reason so text messages work without Overview reason", async () => {
    const { client, calls } = capture({
      actor: "human_operator",
      reason: "",
      expectedParent: "none",
      dryRun: true,
    });
    await client.chatAgent("video.director", { message: "hello" });
    expect(header(calls[0].init, "x-casops-reason")).toBe("operator chat");
    expect(JSON.parse(String(calls[0].init.body))).toEqual({ message: "hello" });
  });
});
