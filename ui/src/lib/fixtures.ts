import type { EvalFixture, EvalFixturesResponse } from "../api/types";
import { agentHref } from "../shell/nav";

export function chatFixtures(suite: EvalFixturesResponse | null | undefined): EvalFixture[] {
  return (suite?.fixtures ?? []).filter((item) => item.path === "chat" && fixtureMessage(item));
}

export function runFixtures(suite: EvalFixturesResponse | null | undefined): EvalFixture[] {
  return (suite?.fixtures ?? []).filter((item) => item.path === "run");
}

export function fixtureMessage(item: EvalFixture | null | undefined): string {
  const message = item?.input?.message;
  return typeof message === "string" ? message.trim() : "";
}

export function fixtureHistory(item: EvalFixture | null | undefined): { role: "user" | "assistant"; content: string }[] {
  const raw = item?.input?.history;
  if (!Array.isArray(raw)) {
    return [];
  }
  const turns: { role: "user" | "assistant"; content: string }[] = [];
  for (const row of raw) {
    if (!row || typeof row !== "object") {
      continue;
    }
    const rec = row as { role?: unknown; content?: unknown };
    const role = String(rec.role || "").trim().toLowerCase();
    const content = typeof rec.content === "string" ? rec.content.trim() : "";
    if ((role === "user" || role === "assistant") && content) {
      turns.push({ role, content });
    }
  }
  return turns;
}

export function fixtureTitle(item: EvalFixture): string {
  const name = item.source?.case_name?.trim();
  return name || item.id;
}

export function findFixture(suite: EvalFixturesResponse | null | undefined, id: string): EvalFixture | undefined {
  return (suite?.fixtures ?? []).find((item) => item.id === id);
}

export function clipPreview(text: string, max = 140): string {
  const trimmed = text.trim();
  if (trimmed.length <= max) {
    return trimmed;
  }
  return `${trimmed.slice(0, Math.max(0, max - 1))}…`;
}

export function chatFixtureHref(agentId: string, fixtureId: string): string {
  return `${agentHref(agentId, "chat")}?fixture=${encodeURIComponent(fixtureId)}`;
}

export function runTabHref(agentId: string): string {
  return agentHref(agentId, "run");
}
