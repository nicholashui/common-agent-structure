import { useState } from "react";
import { ErrorBanner } from "../components/RecoveryBanner";
import { Card, GhostButton, JsonWell, PageHeader } from "../components/ui";
import { useAgentId, useAsync } from "../lib/hooks";
import { pretty } from "../lib/json";
import { useSession } from "../state/session";

export function CachePage() {
  const agentId = useAgentId();
  const session = useSession();
  const panel = useAsync(() => session.client.getCacheStats(agentId), [session.client, agentId]);
  const [error, setError] = useState<Error | null>(null);

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
        title="Cache"
        asOf={panel.asOf}
        actions={
          <GhostButton type="button" disabled={!session.mutationReady} onClick={() => void invalidate()}>
            Invalidate
          </GhostButton>
        }
      />
      <ErrorBanner error={error ?? panel.error} />
      <Card>
        {panel.data?.t3_enabled === false ? (
          <p className="mb-3 rounded-full border border-stone-200 px-3 py-1 text-xs text-stone-500 inline-block">T3 off</p>
        ) : null}
        <p className="mb-3 text-sm text-stone-500">There is no Enable T3 control. T3 stays off until a host route exists.</p>
        <JsonWell value={pretty(panel.data)} />
      </Card>
    </div>
  );
}
