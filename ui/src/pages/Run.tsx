import { useState } from "react";
import { Link } from "react-router-dom";
import { ErrorBanner } from "../components/RecoveryBanner";
import { StatusPill } from "../components/StatusPill";
import { Card, GhostButton, JsonWell, PageHeader, PrimaryButton } from "../components/ui";
import type { CacheStats, RunResult } from "../api/types";
import { useAgentId, useAsync } from "../lib/hooks";
import { asRecord, parseMaybeJson, pretty } from "../lib/json";
import { useSession } from "../state/session";

export function RunPage() {
  const agentId = useAgentId();
  const session = useSession();
  const panel = useAsync(async () => {
    const [plan, budget, cache, llm] = await Promise.all([
      session.client.getRuntimePlan(agentId),
      session.client.getContextBudget(agentId),
      session.client.getCacheStats(agentId),
      session.client.getAgentLlm(agentId),
    ]);
    return { plan, budget, cache, llm };
  }, [session.client, agentId]);
  const [run, setRun] = useState<RunResult | null>(session.lastRuns[agentId] ?? null);
  const [error, setError] = useState<Error | null>(null);
  const [openBudget, setOpenBudget] = useState(false);
  const plan = panel.data ? parseMaybeJson(asRecord(panel.data.plan).plan ?? panel.data.plan) : null;
  const nodes = asRecord(plan).nodes;
  const cache: CacheStats | undefined = panel.data?.cache;

  async function execute() {
    session.setRunning(true);
    setError(null);
    try {
      const result = await session.client.runAgent(agentId);
      setRun(result);
      session.rememberRun(result);
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      session.setRunning(false);
    }
  }

  async function invalidate() {
    try {
      await session.client.invalidateCache(agentId);
      panel.reload();
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  return (
    <div>
      <PageHeader
        title="Run"
        asOf={panel.asOf}
        actions={
          <>
            <GhostButton type="button" disabled={!session.mutationReady} onClick={() => void invalidate()}>
              Invalidate cache
            </GhostButton>
            <PrimaryButton type="button" disabled={!session.mutationReady || session.running} onClick={() => void execute()}>
              {session.stale ? "Stale — Refresh First" : session.mutationLabel("Run", "Run (dry-run)")}
            </PrimaryButton>
          </>
        }
      />
      <p className="mb-4 text-sm text-stone-500">
        No streaming chat API. Model node uses host LLM{" "}
        <span className="font-mono">{panel.data?.llm.provider ?? "local_deterministic"}</span>
        {panel.data?.llm.override ? " (agent override)" : " (DEFAULT_LLM)"}. Dry-run still executes the run — this is
        not “no side effects”.
      </p>
      <ErrorBanner error={error ?? panel.error} />
      <div className="grid grid-cols-1 gap-5 lg:grid-cols-2">
        <Card>
          <h2 className="mb-3 text-sm font-semibold">DAG</h2>
          <div className="flex flex-wrap gap-2">
            {Array.isArray(nodes)
              ? nodes.map((node) => {
                  const record = asRecord(node);
                  const kind = String(record.kind ?? "node");
                  return (
                    <span
                      key={String(record.node_id ?? kind)}
                      className={`rounded-lg px-3 py-2 text-xs text-white ${kind === "model" ? "bg-indigo-600" : "bg-violet-600"}`}
                    >
                      {String(record.node_id ?? kind)}
                    </span>
                  );
                })
              : null}
          </div>
          <div className="mt-4">
            <JsonWell value={pretty(plan)} />
          </div>
        </Card>
        <Card>
          <div className="mb-3 flex items-center justify-between">
            <h2 className="text-sm font-semibold">Cache</h2>
            {cache?.t3_enabled ? <StatusPill status="live" /> : <span className="rounded-full border border-stone-200 px-2.5 py-1 text-xs text-stone-500">T3 off</span>}
          </div>
          <JsonWell value={pretty(cache)} />
          <button type="button" className="mt-4 text-xs text-indigo-600" onClick={() => setOpenBudget((value) => !value)}>
            {openBudget ? "Hide" : "Show"} context budget
          </button>
          {openBudget && panel.data ? <div className="mt-2"><JsonWell value={pretty(parseMaybeJson(asRecord(panel.data.budget).budget ?? panel.data.budget))} /></div> : null}
        </Card>
      </div>
      {run ? (
        <Card className="mt-5">
          <div className="mb-3 flex items-center gap-2">
            <h2 className="text-sm font-semibold">Sealed result</h2>
            <StatusPill status={run.cancelled ? "cancelled" : run.containment_stop ? "failed" : "complete"} />
          </div>
          <dl className="grid grid-cols-1 gap-3 text-sm sm:grid-cols-2">
            <div>
              <dt className="text-stone-500">root_trace_id</dt>
              <dd className="font-mono text-xs">{run.root_trace_id}</dd>
            </div>
            <div>
              <dt className="text-stone-500">artifact.id</dt>
              <dd className="font-mono text-xs">{run.artifact?.id}</dd>
            </div>
            <div>
              <dt className="text-stone-500">containment_stop</dt>
              <dd className="font-mono text-xs">{run.containment_stop ?? "null"}</dd>
            </div>
            <div>
              <dt className="text-stone-500">adapter</dt>
              <dd className="font-mono text-xs">{run.adapter}</dd>
            </div>
          </dl>
          <JsonWell value={pretty(run)} />
          <Link
            className="mt-3 inline-block text-sm text-indigo-600"
            to={`/agents/${encodeURIComponent(agentId)}/traces/${encodeURIComponent(run.root_trace_id)}`}
          >
            Open trace
          </Link>
        </Card>
      ) : null}
    </div>
  );
}
