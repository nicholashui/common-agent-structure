import { CommonBadge } from "../components/CommonBadge";
import { ErrorBanner } from "../components/RecoveryBanner";
import { Card, JsonWell, PageHeader } from "../components/ui";
import { useAgentId, useAsync } from "../lib/hooks";
import { pretty } from "../lib/json";
import { useSession } from "../state/session";

export function StructurePage() {
  const agentId = useAgentId();
  const session = useSession();
  const { data, error, asOf } = useAsync(async () => {
    const [structure, resolved] = await Promise.all([
      session.client.getStructure(agentId),
      session.client.getResolved(agentId),
    ]);
    return { structure, resolved };
  }, [session.client, agentId]);
  const hash = data && typeof data.resolved.compose_hash === "string" ? data.resolved.compose_hash : undefined;

  return (
    <div>
      <PageHeader title="Structure" asOf={asOf} />
      <ErrorBanner error={error} />
      {data ? (
        <div className="grid grid-cols-1 gap-5 lg:grid-cols-2">
          <Card>
            <h2 className="mb-3 text-sm font-semibold">Raw structure</h2>
            <JsonWell value={pretty(data.structure)} />
          </Card>
          <Card>
            <div className="mb-3 flex items-center gap-2">
              <h2 className="text-sm font-semibold">Resolved</h2>
              <CommonBadge hash={hash} />
            </div>
            <p className="mb-2 text-xs text-violet-700">MRO</p>
            <JsonWell value={pretty({ mro: data.resolved.mro, compose_hash: hash, lock: data.resolved.lock })} />
          </Card>
        </div>
      ) : null}
    </div>
  );
}
