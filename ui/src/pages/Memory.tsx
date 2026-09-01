import { useMemo, useState } from "react";
import { ErrorBanner } from "../components/RecoveryBanner";
import { StatusPill } from "../components/StatusPill";
import { Card, DangerButton, Field, GhostButton, PageHeader, PrimaryButton, inputClass } from "../components/ui";
import { CasopsHttpError, type MemoryRecord } from "../api/types";
import { useAgentId, useAsync } from "../lib/hooks";
import { memoryWritesDisabled } from "../lib/honesty";
import { asRecord, parseMaybeJson } from "../lib/json";
import { useSession } from "../state/session";

function scopeKey(agentId: string): string {
  return `casops.control-ui.memory-scope.${agentId}`;
}

export function MemoryPage() {
  const agentId = useAgentId();
  const session = useSession();
  const stored = useMemo(() => {
    try {
      return JSON.parse(sessionStorage.getItem(scopeKey(agentId)) || "{}") as { tenant?: string; subject?: string };
    } catch {
      return {};
    }
  }, [agentId]);
  const [tenant, setTenant] = useState(stored.tenant ?? "t");
  const [subject, setSubject] = useState(stored.subject ?? "s");
  const [text, setText] = useState("");
  const [records, setRecords] = useState<MemoryRecord[]>([]);
  const [emptyOk, setEmptyOk] = useState(false);
  const [queue, setQueue] = useState<{ queued?: boolean; queue_depth?: number } | null>(null);
  const [notice, setNotice] = useState<string | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const [asOf, setAsOf] = useState<Date | null>(null);
  const header = useAsync(async () => {
    const [policy, hierarchy] = await Promise.all([
      session.client.getMemoryPolicy(agentId),
      session.client.getMemoryHierarchy(agentId),
    ]);
    return { policy, hierarchy };
  }, [session.client, agentId]);
  const policy = header.data ? asRecord(parseMaybeJson(asRecord(header.data.policy).policy ?? header.data.policy)) : {};
  const mode = String(policy.mode ?? asRecord(header.data?.hierarchy).mode ?? "");
  const writeDisabled = memoryWritesDisabled(mode);

  function persist(nextTenant: string, nextSubject: string) {
    sessionStorage.setItem(scopeKey(agentId), JSON.stringify({ tenant: nextTenant, subject: nextSubject }));
  }

  async function search() {
    setError(null);
    persist(tenant, subject);
    try {
      const body = await session.client.queryMemory(agentId, { tenant, subject, text: text || undefined });
      setRecords(body.records);
      setEmptyOk(body.records.length === 0);
      setAsOf(new Date());
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  async function write() {
    try {
      await session.client.writeMemoryCandidate(agentId, { tenant, subject, text });
      await search();
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  async function remove(id: string) {
    try {
      const body = await session.client.deleteMemory(agentId, id, { tenant, subject });
      setNotice(body.tombstoned ? `tombstoned: true for ${id}` : `delete result for ${id}`);
      await search();
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  async function verify(id: string) {
    try {
      await session.client.verifyMemoryDeletion(agentId, id, { tenant, subject });
      await search();
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  async function consolidate() {
    try {
      setQueue(await session.client.consolidateMemory(agentId));
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  const scopeError = error instanceof CasopsHttpError && error.code === "MEM_SCOPE";

  return (
    <div>
      <PageHeader title="Memory" asOf={asOf ?? header.asOf} />
      <ErrorBanner error={header.error} />
      {scopeError ? (
        <div className="mb-4 rounded-2xl border border-amber-200 bg-amber-50 px-4 py-3">
          <p className="font-mono text-xs text-amber-800">MEM_SCOPE</p>
          <p className="mt-1 text-sm text-amber-900">Wrong tenant/subject for this row — not a missing record.</p>
        </div>
      ) : (
        <ErrorBanner error={error} />
      )}
      <Card className="mb-5">
        <p className="text-sm text-stone-600">
          mode <span className="font-mono">{mode || "unknown"}</span>
          {writeDisabled ? " — Write candidate disabled (MEM_TRUST_TIER)." : ""}
        </p>
        <div className="mt-4 grid grid-cols-1 gap-3 md:grid-cols-3">
          <Field label="tenant">
            <input className={inputClass} value={tenant} onChange={(event) => setTenant(event.target.value)} />
          </Field>
          <Field label="subject">
            <input className={inputClass} value={subject} onChange={(event) => setSubject(event.target.value)} />
          </Field>
          <Field label="text (optional)">
            <input className={inputClass} value={text} onChange={(event) => setText(event.target.value)} />
          </Field>
        </div>
        <div className="mt-4 flex flex-wrap gap-2">
          <PrimaryButton type="button" disabled={!session.mutationReady || !tenant || !subject} onClick={() => void search()}>
            Search
          </PrimaryButton>
          <GhostButton
            type="button"
            disabled={!session.mutationReady || writeDisabled || !text}
            title={writeDisabled ? "MEM_TRUST_TIER" : undefined}
            onClick={() => void write()}
          >
            Write candidate
          </GhostButton>
          <GhostButton type="button" disabled={!session.mutationReady} onClick={() => void consolidate()}>
            Enqueue consolidate
          </GhostButton>
        </div>
        {queue ? (
          <div className="mt-3 flex items-center gap-2 text-sm">
            <StatusPill status="queued" />
            <span>queue_depth {queue.queue_depth}</span>
          </div>
        ) : null}
        <p className="mt-3 text-xs text-stone-500">Serving path enqueues only. The consolidation worker drains offline.</p>
      </Card>
      {notice ? <p className="mb-3 font-mono text-sm text-stone-700">{notice}</p> : null}
      {emptyOk ? <p className="mb-3 text-sm text-stone-500">No rows in this scope</p> : null}
      <div className="overflow-x-auto rounded-2xl border border-stone-200">
        <table className="w-full text-left text-sm">
          <thead className="bg-stone-50 text-stone-500">
            <tr>
              <th className="px-3 py-2 font-medium">memory_id</th>
              <th className="px-3 py-2 font-medium">text</th>
              <th className="px-3 py-2 font-medium">actions</th>
            </tr>
          </thead>
          <tbody>
            {records.map((row) => (
              <tr key={row.memory_id} className="border-t border-stone-100">
                <td className="px-3 py-2 font-mono text-xs">{row.memory_id}</td>
                <td className="px-3 py-2">{row.text}</td>
                <td className="px-3 py-2">
                  <div className="flex gap-2">
                    <DangerButton type="button" disabled={!session.mutationReady} onClick={() => void remove(row.memory_id)}>
                      Delete
                    </DangerButton>
                    <GhostButton type="button" disabled={!session.mutationReady} onClick={() => void verify(row.memory_id)}>
                      Verify deletion
                    </GhostButton>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
