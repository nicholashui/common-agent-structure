import { useState } from "react";
import { Link } from "react-router-dom";
import { OperatorContractFields } from "../components/ActorStrip";
import { CommonBadge } from "../components/CommonBadge";
import { ErrorBanner } from "../components/RecoveryBanner";
import { IoPanel } from "../components/IoPanel";
import { StatusPill } from "../components/StatusPill";
import { Card, Field, GhostButton, PageHeader, PrimaryButton, inputClass } from "../components/ui";
import { useAgentId, useAsync } from "../lib/hooks";
import { pillForValidation, validationIsPass } from "../lib/honesty";
import { parseAgentIo } from "../lib/io";
import { useSession } from "../state/session";

export function AgentOverviewPage() {
  const agentId = useAgentId();
  const session = useSession();
  const { data, error, asOf, reload } = useAsync(async () => {
    const [structure, attestation, report, llm] = await Promise.all([
      session.client.getStructure(agentId),
      session.client.getAttestation(agentId),
      session.client.getValidationReport(agentId),
      session.client.getAgentLlm(agentId),
    ]);
    return { structure, attestation, report, llm };
  }, [session.client, agentId]);
  const [llmChoice, setLlmChoice] = useState<string>("");
  const [llmNotice, setLlmNotice] = useState<string | null>(null);
  const [llmError, setLlmError] = useState<Error | null>(null);
  const run = session.lastRuns[agentId];
  const llmSelected = llmChoice || (data?.llm.override ? data.llm.provider : "__default__");
  const ok = data?.attestation.status === "host_reference";
  const pass = validationIsPass(data?.report ?? null);

  return (
    <div>
      <PageHeader
        title={agentId || "Agent"}
        asOf={asOf}
        actions={
          <>
            <Link to={`/agents/${encodeURIComponent(agentId)}/compose`}>
              <GhostButton type="button">Compose preview</GhostButton>
            </Link>
            <Link to={`/agents/${encodeURIComponent(agentId)}/run`}>
              <GhostButton type="button">Run</GhostButton>
            </Link>
            <Link to={`/agents/${encodeURIComponent(agentId)}/chat`}>
              <PrimaryButton type="button">Chat</PrimaryButton>
            </Link>
          </>
        }
      />
      <ErrorBanner error={error} />
      <div className="mb-5">
        <OperatorContractFields />
      </div>
      {data ? (
        <div className="grid grid-cols-1 gap-5 lg:grid-cols-2">
          <Card className={ok ? "border-indigo-200" : "border-red-200"}>
            <div className="mb-3 flex items-center justify-between gap-2">
              <h2 className="text-sm font-semibold text-stone-900">Attestation</h2>
              <StatusPill status={ok ? "live" : "failed"} />
            </div>
            <p className="font-mono text-xs text-stone-500">{data.attestation.status}</p>
            <p className="mt-2 break-all font-mono text-xs text-stone-700">digest {data.attestation.digest}</p>
            <p className="mt-2 text-xs text-stone-500">Host-owned. The agent folder cannot rewrite this.</p>
            <GhostButton type="button" className="mt-3" onClick={() => reload()}>
              Reload attestation
            </GhostButton>
          </Card>
          <Card>
            <h2 className="mb-3 text-sm font-semibold text-stone-900">Structure</h2>
            <CommonBadge version={data.structure.schema_version} />
            <dl className="mt-3 space-y-2 text-sm">
              <div>
                <dt className="text-stone-500">structure_id</dt>
                <dd className="font-mono text-stone-900">{data.structure.structure_id}</dd>
              </div>
              <div>
                <dt className="text-stone-500">folder</dt>
                <dd className="font-mono text-xs text-stone-700">{data.structure.folder}</dd>
              </div>
              <div>
                <dt className="text-stone-500">spec_bytes</dt>
                <dd className="font-mono">{data.structure.spec_bytes}</dd>
              </div>
            </dl>
          </Card>
          <IoPanel io={parseAgentIo(data.structure.io)} />
          <Card>
            <h2 className="mb-3 text-sm font-semibold text-stone-900">LLM</h2>
            <p className="mb-3 text-sm text-stone-500">
              Resolved <span className="font-mono">{data.llm.provider}</span>. Inherit fleet DEFAULT_LLM or pick a
              configured host backend. Keys stay in .env.
            </p>
            <ErrorBanner error={llmError} />
            {llmNotice ? <p className="mb-2 font-mono text-xs text-stone-600">{llmNotice}</p> : null}
            <Field label="Provider">
              <select className={inputClass} value={llmSelected} onChange={(event) => setLlmChoice(event.target.value)}>
                <option value="__default__">Use default ({data.llm.default_llm})</option>
                {(data.llm.providers ?? []).map((provider) => (
                  <option key={provider.id} value={provider.id} disabled={!provider.configured}>
                    {provider.label}
                    {provider.configured ? "" : " — not configured"}
                  </option>
                ))}
              </select>
            </Field>
            <PrimaryButton
              type="button"
              className="mt-3"
              disabled={!session.mutationReady}
              onClick={() => {
                setLlmError(null);
                const provider = llmSelected === "__default__" ? null : llmSelected;
                void session.client
                  .setAgentLlm(agentId, provider)
                  .then((view) => {
                    setLlmNotice(view.dry_run ? "dry-run: not persisted" : `saved provider=${view.provider}`);
                    reload();
                  })
                  .catch((err: unknown) => setLlmError(err instanceof Error ? err : new Error(String(err))));
              }}
            >
              {session.dryRun ? "Preview agent LLM" : "Save agent LLM"}
            </PrimaryButton>
          </Card>
          <Card>
            <h2 className="mb-3 text-sm font-semibold text-stone-900">Last run (this session)</h2>
            {run ? (
              <div className="space-y-2 text-sm">
                <StatusPill status={run.cancelled ? "cancelled" : run.containment_stop ? "failed" : "complete"} />
                <p className="font-mono text-xs">{run.root_trace_id}</p>
                <Link className="text-indigo-600 text-xs" to={`/agents/${encodeURIComponent(agentId)}/traces/${encodeURIComponent(run.root_trace_id)}`}>
                  Open trace
                </Link>
              </div>
            ) : (
              <p className="text-sm text-stone-500">No run in this browser session.</p>
            )}
          </Card>
          <Card className={pass ? "border-emerald-200" : "border-amber-200 bg-amber-50 hover:shadow-none"}>
            <div className="mb-3 flex items-center gap-2">
              <h2 className="text-sm font-semibold text-stone-900">Validation honesty</h2>
              <StatusPill status={pillForValidation(data.report)} />
            </div>
            <p className="font-mono text-xs text-stone-700">{data.report.verdict}</p>
            <p className="mt-2 text-sm text-stone-700">{data.report.reason}</p>
            <p className="mt-2 text-xs text-stone-500">NOT_RUN / screening is not a production pass.</p>
          </Card>
        </div>
      ) : null}
    </div>
  );
}
