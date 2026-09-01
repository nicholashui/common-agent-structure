import { describe, expect, it } from "vitest";
import {
  canApprove,
  capabilityTone,
  memoryWritesDisabled,
  pillForValidation,
  validationIsPass,
  wroteLocksTone,
} from "../src/lib/honesty";

describe("eval honesty", () => {
  it("does not style NOT_RUN as a pass", () => {
    const report = { verdict: "NOT_RUN", pass: false, reason: "unqualified_instruments" };
    expect(validationIsPass(report)).toBe(false);
    expect(["complete", "live", "running"]).not.toContain(pillForValidation(report));
  });

  it("does not style INDICATIVE screening as a release pass", () => {
    const report = { verdict: "INDICATIVE", pass: false, honesty: "INDICATIVE" };
    expect(validationIsPass(report)).toBe(false);
    expect(pillForValidation(report)).toBe("queued");
  });

  it("uses complete only for measured pass", () => {
    expect(pillForValidation({ verdict: "MEASURED_LOCAL", pass: true })).toBe("complete");
    expect(validationIsPass({ verdict: "MEASURED_LOCAL", pass: true })).toBe(true);
  });
});

describe("contract honesty", () => {
  it("marks wrote_locks false as preview only", () => {
    expect(wroteLocksTone(false)).toEqual({ label: "Preview only", warning: false });
    expect(wroteLocksTone(true).warning).toBe(true);
  });

  it("keeps unverified capabilities off green", () => {
    expect(capabilityTone("VERIFIED")).toBe("verified");
    expect(capabilityTone("ASSERTED_UNVERIFIED")).toBe("unverified");
    expect(capabilityTone("REFUTED")).toBe("refuted");
  });

  it("disables memory writes when policy mode is none", () => {
    expect(memoryWritesDisabled("none")).toBe(true);
    expect(memoryWritesDisabled("working")).toBe(false);
  });

  it("only independent_approver may approve", () => {
    expect(canApprove("independent_approver")).toBe(true);
    expect(canApprove("host_service")).toBe(false);
    expect(canApprove("agent_runtime")).toBe(false);
    expect(canApprove("human_operator")).toBe(false);
  });
});
