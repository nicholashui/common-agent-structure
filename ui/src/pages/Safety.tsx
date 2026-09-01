import { useState } from "react";
import { ConfirmDialog } from "../components/ConfirmDialog";
import { ErrorBanner } from "../components/RecoveryBanner";
import { Card, JsonWell, PageHeader, PrimaryButton } from "../components/ui";
import { useAgentId, useAsync } from "../lib/hooks";
import { pretty } from "../lib/json";
import { useSession } from "../state/session";

export function SafetyPage() {
  const agentId = useAgentId();
  const session = useSession();
  const panel = useAsync(() => session.client.getIncidents(agentId), [session.client, agentId]);
  const [confirm, setConfirm] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  async function run() {
    setConfirm(false);
    try {
      await session.client.runRedteam(agentId);
      panel.reload();
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  return (
    <div>
      <PageHeader
        title="Safety"
        asOf={panel.asOf}
        actions={
          <PrimaryButton type="button" disabled={!session.mutationReady} onClick={() => setConfirm(true)}>
            Run red-team fixture
          </PrimaryButton>
        }
      />
      <ErrorBanner error={error ?? panel.error} />
      <Card>
        <h2 className="mb-3 text-sm font-semibold">Incidents</h2>
        <JsonWell value={pretty(panel.data?.incidents ?? [])} />
      </Card>
      <ConfirmDialog
        open={confirm}
        title="Run red-team fixture?"
        body="This POSTs /safety/redteam under the mutation contract. Confirm actor and reason in the header strip first."
        confirmLabel="Run red-team"
        onCancel={() => setConfirm(false)}
        onConfirm={() => void run()}
      />
    </div>
  );
}
