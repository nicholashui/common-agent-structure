import { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { ErrorBanner } from "../components/RecoveryBanner";
import { StatusPill } from "../components/StatusPill";
import { Card, Field, GhostButton, JsonWell, PageHeader, PrimaryButton, inputClass } from "../components/ui";
import { useAgentId } from "../lib/hooks";
import { asRecord, pretty } from "../lib/json";
import { useSession } from "../state/session";

export function TracePage() {
  const agentId = useAgentId();
  const params = useParams();
  const navigate = useNavigate();
  const session = useSession();
  const initial = params.tid ? decodeURIComponent(params.tid) : session.lastRuns[agentId]?.root_trace_id ?? "";
  const [traceId, setTraceId] = useState(initial);
  const [counterfactual, setCounterfactual] = useState("");
  const [trace, setTrace] = useState<unknown>(null);
  const [rootCause, setRootCause] = useState<unknown>(null);
  const [evidence, setEvidence] = useState<unknown>(null);
  const [replay, setReplay] = useState<unknown>(null);
  const [error, setError] = useState<Error | null>(null);
  const [asOf, setAsOf] = useState<Date | null>(null);

  async function load(id: string) {
    setError(null);
    try {
      const body = await session.client.getTrace(id);
      setTrace(body);
      setAsOf(new Date());
      try {
        setRootCause(await session.client.getRootCause(id));
      } catch {
        setRootCause(null);
      }
      const artifactId = String(asRecord(asRecord(body).artifact).id ?? session.lastRuns[agentId]?.artifact?.id ?? "");
      if (artifactId) {
        try {
          setEvidence(await session.client.getEvidenceGraph(artifactId));
        } catch {
          setEvidence(null);
        }
      }
      if (agentId) {
        navigate(`/agents/${encodeURIComponent(agentId)}/traces/${encodeURIComponent(id)}`, { replace: true });
      }
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  async function doReplay(withCounterfactual: boolean) {
    try {
      const body = await session.client.replayTrace(traceId, withCounterfactual ? counterfactual : undefined);
      setReplay(body);
      setAsOf(new Date());
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  const spans = Array.isArray(asRecord(asRecord(trace).trace).spans)
    ? (asRecord(trace).trace as { spans: { span_id: string; name: string; parent_id?: string | null }[] }).spans
    : [];
  const failed = Boolean(asRecord(trace).containment_stop);

  return (
    <div>
      <PageHeader
        title="Trace"
        asOf={asOf}
        actions={
          <>
            <GhostButton type="button" disabled={!traceId} onClick={() => void load(traceId)}>
              Load
            </GhostButton>
            <GhostButton type="button" disabled={!session.mutationReady || !traceId} onClick={() => void doReplay(false)}>
              Replay
            </GhostButton>
            <PrimaryButton
              type="button"
              disabled={!session.mutationReady || !traceId || !counterfactual}
              onClick={() => void doReplay(true)}
            >
              Counterfactual
            </PrimaryButton>
          </>
        }
      />
      <ErrorBanner error={error} />
      <div className="mb-5 grid grid-cols-1 gap-3 md:grid-cols-2">
        <Field label="root_trace_id">
          <input className={`${inputClass} font-mono`} value={traceId} onChange={(event) => setTraceId(event.target.value)} />
        </Field>
        <Field label="counterfactual query">
          <input
            className={inputClass}
            placeholder="counterfactual="
            value={counterfactual}
            onChange={(event) => setCounterfactual(event.target.value)}
          />
        </Field>
      </div>
      <div className="grid grid-cols-1 gap-5 lg:grid-cols-2">
        <Card>
          <div className="mb-3 flex items-center gap-2">
            <h2 className="text-sm font-semibold">Span tree</h2>
            {trace ? <StatusPill status={failed ? "failed" : "complete"} /> : null}
          </div>
          <ul className="space-y-2 font-mono text-xs">
            {spans.map((span) => (
              <li key={span.span_id} className={span.parent_id ? "ml-4 text-stone-600" : "text-stone-900"}>
                {span.name} · {span.span_id}
              </li>
            ))}
          </ul>
          {trace ? <div className="mt-4"><JsonWell value={pretty(trace)} /></div> : <p className="text-sm text-stone-500">Load a trace from a run result.</p>}
        </Card>
        <div className="space-y-5">
          <Card>
            <h2 className="mb-2 text-sm font-semibold">Root cause</h2>
            <JsonWell value={pretty(rootCause)} />
          </Card>
          <Card>
            <h2 className="mb-2 text-sm font-semibold">Evidence</h2>
            <JsonWell value={pretty(evidence)} />
          </Card>
          <Card>
            <h2 className="mb-2 text-sm font-semibold">Replay</h2>
            <p className="mb-2 text-xs text-stone-500">Counterfactual replay does not write memory.</p>
            <JsonWell value={pretty(replay)} />
          </Card>
        </div>
      </div>
    </div>
  );
}
