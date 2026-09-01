import { useState } from "react";
import { CommonBadge } from "../components/CommonBadge";
import { ErrorBanner } from "../components/RecoveryBanner";
import { Card, JsonWell, PageHeader, PrimaryButton } from "../components/ui";
import type { ComposePreviewResponse } from "../api/types";
import { useAgentId } from "../lib/hooks";
import { wroteLocksTone } from "../lib/honesty";
import { pretty } from "../lib/json";
import { useSession } from "../state/session";

function asList(value: unknown): string[] {
  if (Array.isArray(value)) {
    return value.map((item) => (typeof item === "string" ? item : JSON.stringify(item)));
  }
  if (value && typeof value === "object") {
    return Object.entries(value as Record<string, unknown>).map(([key, item]) => `${key}: ${String(item)}`);
  }
  return [];
}

export function ComposePage() {
  const agentId = useAgentId();
  const session = useSession();
  const [result, setResult] = useState<ComposePreviewResponse | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const [asOf, setAsOf] = useState<Date | null>(null);
  const [busy, setBusy] = useState(false);
  const locks = result ? wroteLocksTone(Boolean(result.wrote_locks)) : null;

  async function run() {
    setBusy(true);
    setError(null);
    try {
      const body = await session.client.composePreview(agentId);
      setResult(body);
      setAsOf(new Date());
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setBusy(false);
    }
  }

  return (
    <div>
      <PageHeader
        title="Compose"
        asOf={asOf}
        actions={
          <PrimaryButton type="button" disabled={!session.mutationReady || busy} onClick={() => void run()}>
            {session.stale ? "Stale — Refresh First" : session.mutationLabel("Compose preview", "Preview")}
          </PrimaryButton>
        }
      />
      <p className="mb-4 text-sm text-stone-500">Prospective lock only. This never implies files were written.</p>
      <ErrorBanner error={error} />
      {result ? (
        <div className="grid grid-cols-1 gap-5 lg:grid-cols-2">
          <Card>
            <div className="mb-3 flex flex-wrap items-center gap-2">
              <CommonBadge hash={result.compose_hash} />
              <span
                className={`rounded-full border px-2.5 py-1 text-xs ${
                  locks?.warning ? "border-amber-300 bg-amber-50 text-amber-800" : "border-stone-200 bg-white text-stone-600"
                }`}
              >
                {locks?.label}
              </span>
            </div>
            <h2 className="mb-2 text-sm font-semibold">Findings</h2>
            <ul className="space-y-1 text-sm">
              {asList(result.findings).length ? (
                asList(result.findings).map((item) => (
                  <li key={item} className="text-emerald-700">
                    ✓ {item}
                  </li>
                ))
              ) : (
                <li className="text-stone-500">No findings list in response.</li>
              )}
            </ul>
            {asList(result.errors).length ? (
              <div className="mt-4 rounded-xl border border-red-200 bg-red-50 p-3 text-sm text-red-800">
                {asList(result.errors).map((item) => (
                  <p key={item}>{item}</p>
                ))}
              </div>
            ) : null}
          </Card>
          <Card>
            <h2 className="mb-2 text-sm font-semibold text-violet-700">MRO</h2>
            <div className="mb-4 flex flex-wrap gap-2">
              {(Array.isArray(result.mro) ? result.mro : []).map((node) => (
                <span key={String(node)} className="rounded-lg bg-indigo-600 px-2 py-1 text-xs text-white">
                  {String(node)}
                </span>
              ))}
            </div>
            <JsonWell value={pretty({ compose_hash: result.compose_hash, lock: result.lock, wrote_locks: result.wrote_locks })} />
          </Card>
        </div>
      ) : null}
    </div>
  );
}
