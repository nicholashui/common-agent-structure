import { useState } from "react";
import { ErrorBanner } from "../components/RecoveryBanner";
import { Card, GhostButton, JsonWell, PageHeader } from "../components/ui";
import { useAgentId, useAsync } from "../lib/hooks";
import { pretty } from "../lib/json";
import { useSession } from "../state/session";

export function CorrigibilityPage() {
  const agentId = useAgentId();
  const session = useSession();
  const { data, error, asOf, reload } = useAsync(() => session.client.getAttestation(agentId), [session.client, agentId]);
  const [reveal, setReveal] = useState(false);

  return (
    <div>
      <PageHeader
        title="Corrigibility"
        asOf={asOf}
        actions={
          <GhostButton type="button" onClick={() => reload()}>
            Reload attestation
          </GhostButton>
        }
      />
      <ErrorBanner error={error} />
      <Card className="border-indigo-200">
        <p className="mb-4 text-sm text-stone-600">The agent folder cannot rewrite this. Host-owned attestation, no edit controls.</p>
        {data ? (
          <dl className="space-y-3 text-sm">
            <div>
              <dt className="text-stone-500">status</dt>
              <dd className="font-mono">{data.status}</dd>
            </div>
            <div>
              <dt className="text-stone-500">invariant_set_id</dt>
              <dd className="font-mono text-xs">{data.invariant_set_id}</dd>
            </div>
            <div>
              <dt className="text-stone-500">digest</dt>
              <dd className="break-all font-mono text-xs">{data.digest}</dd>
            </div>
            <div>
              <dt className="text-stone-500">signature</dt>
              <dd className="break-all font-mono text-xs">
                {reveal ? data.signature : `${data.signature.slice(0, 12)}…`}
                <button type="button" className="ml-2 text-indigo-600" onClick={() => setReveal((value) => !value)}>
                  {reveal ? "hide" : "expand-to-reveal"}
                </button>
              </dd>
            </div>
          </dl>
        ) : null}
        <div className="mt-4">
          <JsonWell value={pretty(reveal ? data : data ? { ...data, signature: `${data.signature.slice(0, 12)}…` } : null)} />
        </div>
      </Card>
    </div>
  );
}
