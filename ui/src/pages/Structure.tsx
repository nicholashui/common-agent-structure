import { CommonBadge } from "../components/CommonBadge";
import { ErrorBanner } from "../components/RecoveryBanner";
import { IoPanel } from "../components/IoPanel";
import { Card, JsonWell, PageHeader } from "../components/ui";
import { useAgentId, useAsync } from "../lib/hooks";
import { asRecord, pretty } from "../lib/json";
import { parseAgentIo } from "../lib/io";
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
  const resolved = data ? asRecord(data.resolved) : {};
  const hash = typeof resolved.compose_hash === "string" ? resolved.compose_hash : undefined;
  const folderIo = data ? parseAgentIo(data.structure.io) : undefined;
  const mergedIo = data ? parseAgentIo(resolved.io) : undefined;

  return (
    <div>
      <PageHeader title="Structure" asOf={asOf} />
      <p className="mb-4 text-sm text-stone-500">
        Expected inputs and outputs come from the folder <span className="font-mono">critique_edges</span>{" "}
        contract (union-merged at compose). The structure endpoint used to return only metadata, so this
        page could not show them.
      </p>
      <ErrorBanner error={error} />
      {data ? (
        <div className="grid grid-cols-1 gap-5 lg:grid-cols-2">
          <IoPanel io={folderIo} title="Folder inputs and outputs" />
          <IoPanel io={mergedIo} title="Merged inputs and outputs" />
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
            <JsonWell value={pretty({ mro: resolved.mro, compose_hash: hash, lock: resolved.lock, io: resolved.io })} />
          </Card>
        </div>
      ) : null}
    </div>
  );
}
