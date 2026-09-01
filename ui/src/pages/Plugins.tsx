import { useState } from "react";
import { ErrorBanner } from "../components/RecoveryBanner";
import { Card, PageHeader, PrimaryButton } from "../components/ui";
import { useAgentId, useAsync } from "../lib/hooks";
import { isolationTooltip } from "../lib/honesty";
import { useSession } from "../state/session";

const TIER_CLASS: Record<string, string> = {
  I0: "bg-stone-100 text-stone-600 border-stone-200",
  I1: "bg-indigo-50 text-indigo-700 border-indigo-200",
  I2: "bg-violet-50 text-violet-700 border-violet-200",
  I3: "bg-amber-50 text-amber-800 border-amber-200",
};

export function PluginsPage() {
  const agentId = useAgentId();
  const session = useSession();
  const panel = useAsync(() => session.client.getPlugins(agentId), [session.client, agentId]);
  const [error, setError] = useState<Error | null>(null);
  const plugins = panel.data?.plugins ?? [];
  const executed = plugins.some((plugin) => plugin.executed === true);

  async function validate() {
    try {
      await session.client.validatePlugins(agentId);
      panel.reload();
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  return (
    <div>
      <PageHeader
        title="Plugins"
        asOf={panel.asOf}
        actions={
          <PrimaryButton type="button" disabled={!session.mutationReady} onClick={() => void validate()}>
            Validate without exec
          </PrimaryButton>
        }
      />
      <ErrorBanner error={error ?? panel.error} />
      {executed ? (
        <div className="mb-4 rounded-2xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-800">
          executed: true appeared — host contract break. Validate-without-exec must stay false.
        </div>
      ) : null}
      <Card>
        <table className="w-full text-left text-sm">
          <thead>
            <tr className="border-b border-stone-200 text-stone-500">
              <th className="py-2 font-medium">id</th>
              <th className="py-2 font-medium">isolation</th>
              <th className="py-2 font-medium">validated</th>
              <th className="py-2 font-medium">executed</th>
            </tr>
          </thead>
          <tbody>
            {plugins.length ? (
              plugins.map((plugin) => (
                <tr key={plugin.id} className="border-b border-stone-100">
                  <td className="py-2 font-mono text-xs">{plugin.id}</td>
                  <td className="py-2">
                    <span title={isolationTooltip(plugin.isolation)} className={`rounded-md border px-2 py-0.5 text-xs ${TIER_CLASS[plugin.isolation] ?? TIER_CLASS.I0}`}>
                      {plugin.isolation}
                    </span>
                  </td>
                  <td className="py-2">{String(plugin.validated)}</td>
                  <td className="py-2 font-mono">{String(plugin.executed ?? false)}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td className="py-3 text-stone-500" colSpan={4}>
                  No plugins in the registry.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </Card>
    </div>
  );
}
