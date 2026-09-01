import { ErrorBanner } from "../components/RecoveryBanner";
import { JsonWell, PageHeader } from "../components/ui";
import { useAgentId, useAsync } from "../lib/hooks";
import { asRecord, parseMaybeJson, pretty } from "../lib/json";
import { useSession } from "../state/session";

export function ProtocolsPage() {
  const agentId = useAgentId();
  const session = useSession();
  const { data, error, asOf } = useAsync(() => session.client.getProtocols(agentId), [session.client, agentId]);
  const body = data ? parseMaybeJson(asRecord(data).protocols ?? data) : null;
  return (
    <div>
      <PageHeader title="Protocols" asOf={asOf} />
      <p className="mb-4 text-sm text-stone-500">Read-only. There is no PATCH on the v3 public plane.</p>
      <ErrorBanner error={error} />
      <JsonWell value={pretty(body)} />
    </div>
  );
}
