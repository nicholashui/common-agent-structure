import type { StatusKind } from "../components/statusCfg";

export function pillForValidation(report: { verdict?: string; pass?: boolean; honesty?: string } | null): StatusKind {
  if (!report) {
    return "unavailable";
  }
  const verdict = report.verdict || "";
  if (verdict === "NOT_RUN" || verdict === "BLOCKED") {
    return "stale";
  }
  if (verdict === "INDICATIVE" || report.honesty === "INDICATIVE") {
    return "queued";
  }
  if (report.pass === false) {
    return "failed";
  }
  if ((verdict === "MEASURED_LOCAL" || verdict === "MEASURED_EXTERNAL") && report.pass === true) {
    return "complete";
  }
  return "unavailable";
}

export function validationIsPass(report: { verdict?: string; pass?: boolean } | null): boolean {
  if (!report) {
    return false;
  }
  if (report.verdict === "NOT_RUN" || report.verdict === "INDICATIVE" || report.verdict === "BLOCKED") {
    return false;
  }
  return report.pass === true;
}

export function wroteLocksTone(wroteLocks: boolean): { label: string; warning: boolean } {
  if (wroteLocks) {
    return { label: "wrote_locks true — host bug relative to v1 contract", warning: true };
  }
  return { label: "Preview only", warning: false };
}

export function capabilityTone(status: string): "verified" | "refuted" | "unverified" {
  if (status === "VERIFIED") {
    return "verified";
  }
  if (status === "REFUTED") {
    return "refuted";
  }
  return "unverified";
}

export function canApprove(actor: string): boolean {
  return actor === "independent_approver";
}

export function memoryWritesDisabled(mode: string | undefined): boolean {
  return mode === "none" || mode === "disabled";
}

export function isolationTooltip(tier: string): string {
  if (tier === "I3") {
    return "I3 needs sandbox; network requires I3.";
  }
  if (tier === "I0" || tier === "I1") {
    return "Unsigned plugins cannot be I0/I1.";
  }
  return "Isolation tier from the plugin manifest.";
}
