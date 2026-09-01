import { useState } from "react";
import { ConfirmDialog } from "../components/ConfirmDialog";
import { ErrorBanner } from "../components/RecoveryBanner";
import { Card, Field, GhostButton, JsonWell, PageHeader, PrimaryButton, inputClass } from "../components/ui";
import type { ImprovementCandidate } from "../api/types";
import { useAgentId, useAsync } from "../lib/hooks";
import { canApprove } from "../lib/honesty";
import { pretty } from "../lib/json";
import { useSession } from "../state/session";

const COLUMNS = [
  { id: "PROPOSED", label: "Proposed", match: (state?: string) => !state || state === "PROPOSED" },
  { id: "EVALUATED", label: "Evaluated", match: (state?: string) => state === "EVALUATED" },
  { id: "HUMAN_APPROVED", label: "Approved", match: (state?: string) => state === "HUMAN_APPROVED" },
  { id: "ROLLED_BACK", label: "Rolled back", match: (state?: string) => state === "ROLLED_BACK" },
];

export function ImprovementPage() {
  const agentId = useAgentId();
  const session = useSession();
  const panel = useAsync(async () => {
    const [candidates, ledger] = await Promise.all([
      session.client.listCandidates(agentId),
      session.client.getLedger(agentId),
    ]);
    return { candidates: candidates.candidates, ledger: ledger.ledger };
  }, [session.client, agentId]);
  const [cid, setCid] = useState("");
  const [version, setVersion] = useState("");
  const [approveId, setApproveId] = useState<string | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const approveAllowed = canApprove(session.actor);

  async function evaluate(id: string) {
    try {
      await session.client.evaluateCandidate(agentId, id);
      panel.reload();
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  async function approve(id: string) {
    setApproveId(null);
    try {
      await session.client.approveCandidate(agentId, id);
      panel.reload();
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  async function rollback() {
    try {
      await session.client.rollback(agentId, version);
      panel.reload();
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  const candidates = panel.data?.candidates ?? [];

  return (
    <div>
      <PageHeader title="Improvement" asOf={panel.asOf} />
      <p className="mb-4 text-sm text-stone-500">No promote-to-production control. Agent identities cannot approve.</p>
      {session.actor === "agent_runtime" ? (
        <p className="mb-4 text-sm text-red-700">Agent identities cannot approve.</p>
      ) : null}
      <ErrorBanner error={error ?? panel.error} />
      <div className="mb-5 flex flex-wrap gap-3">
        <Field label="candidate id">
          <input className={`${inputClass} font-mono`} value={cid} onChange={(event) => setCid(event.target.value)} />
        </Field>
        <PrimaryButton type="button" disabled={!session.mutationReady || !cid} onClick={() => void evaluate(cid)}>
          Evaluate
        </PrimaryButton>
        <Field label="rollback version">
          <input className={`${inputClass} font-mono`} value={version} onChange={(event) => setVersion(event.target.value)} />
        </Field>
        <GhostButton type="button" disabled={!session.mutationReady || !version} onClick={() => void rollback()}>
          Rollback
        </GhostButton>
      </div>
      <div className="grid grid-cols-1 gap-4 md:grid-cols-2 xl:grid-cols-4">
        {COLUMNS.map((column) => (
          <div key={column.id} className="rounded-2xl border border-stone-200 bg-stone-50 p-3">
            <h2 className="mb-3 text-xs font-semibold uppercase tracking-wide text-stone-500">{column.label}</h2>
            <div className="space-y-2">
              {candidates.filter((item) => column.match(item.state)).map((item: ImprovementCandidate) => (
                <article key={item.id} className="rounded-xl border border-stone-200 bg-white p-3">
                  <p className="font-mono text-xs">{item.id}</p>
                  <p className="text-xs text-stone-500">{item.state ?? "PROPOSED"}</p>
                  <div className="mt-2 flex flex-wrap gap-1">
                    <GhostButton type="button" disabled={!session.mutationReady} onClick={() => void evaluate(item.id)}>
                      Evaluate
                    </GhostButton>
                    <PrimaryButton
                      type="button"
                      disabled={!session.mutationReady || !approveAllowed}
                      title={approveAllowed ? undefined : "Host allow-list: only independent_approver may approve"}
                      onClick={() => setApproveId(item.id)}
                    >
                      Approve
                    </PrimaryButton>
                  </div>
                </article>
              ))}
            </div>
          </div>
        ))}
      </div>
      <Card className="mt-5 hover:shadow-none">
        <h2 className="mb-3 text-sm font-semibold">Ledger</h2>
        <JsonWell value={pretty(panel.data?.ledger ?? [])} />
      </Card>
      <ConfirmDialog
        open={Boolean(approveId)}
        title="Approve candidate?"
        body={
          <div>
            <p>Actor must remain {session.actor}.</p>
            <p className="mt-2 font-mono text-xs">reason: {session.reason || "(empty)"}</p>
            <p className="mt-2 text-xs text-stone-500">host_service and agent_runtime cannot approve on this host.</p>
          </div>
        }
        confirmLabel="Approve"
        onCancel={() => setApproveId(null)}
        onConfirm={() => approveId && void approve(approveId)}
      />
    </div>
  );
}
