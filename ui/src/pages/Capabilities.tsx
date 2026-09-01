import { useState } from "react";
import { ErrorBanner } from "../components/RecoveryBanner";
import { Card, JsonWell, PageHeader, PrimaryButton } from "../components/ui";
import { useAgentId, useAsync } from "../lib/hooks";
import { capabilityTone } from "../lib/honesty";
import { pretty } from "../lib/json";
import { useSession } from "../state/session";

export function CapabilitiesPage() {
  const agentId = useAgentId();
  const session = useSession();
  const [openRuntime, setOpenRuntime] = useState(false);
  const panel = useAsync(async () => {
    const [matrix, runtime] = await Promise.all([
      session.client.getCapabilitiesMatrix(agentId),
      session.client.getRuntimeCapabilities(agentId),
    ]);
    return { matrix, runtime };
  }, [session.client, agentId]);
  const [error, setError] = useState<Error | null>(null);

  async function verify() {
    try {
      await session.client.verifyCapabilities(agentId);
      panel.reload();
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  const rows = panel.data?.matrix.matrix ?? [];

  return (
    <div>
      <PageHeader
        title="Capabilities"
        asOf={panel.asOf}
        actions={
          <PrimaryButton type="button" disabled={!session.mutationReady} onClick={() => void verify()}>
            Verify
          </PrimaryButton>
        }
      />
      <ErrorBanner error={error ?? panel.error} />
      <Card>
        <p className="mb-3 text-sm text-stone-500">
          production_bindable {String(panel.data?.matrix.production_bindable ?? false)}. Unverified claims stay amber, never green.
        </p>
        <table className="w-full text-left text-sm">
          <thead>
            <tr className="border-b border-stone-200 text-stone-500">
              <th className="py-2 font-medium">capability</th>
              <th className="py-2 font-medium">status</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((row) => {
              const tone = capabilityTone(row.status);
              const cls =
                tone === "verified"
                  ? "bg-emerald-50 text-emerald-700 border-emerald-200"
                  : tone === "refuted"
                    ? "bg-red-50 text-red-700 border-red-200"
                    : "bg-amber-50 text-amber-800 border-amber-200";
              return (
                <tr key={row.capability} className="border-b border-stone-100">
                  <td className="py-2 font-mono text-xs">{row.capability}</td>
                  <td className="py-2">
                    <span className={`rounded-md border px-2 py-0.5 text-xs ${cls}`}>{row.status}</span>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </Card>
      <button type="button" className="mt-4 text-xs text-indigo-600" onClick={() => setOpenRuntime((value) => !value)}>
        {openRuntime ? "Hide" : "Show"} runtime capabilities
      </button>
      {openRuntime && panel.data ? <div className="mt-3"><JsonWell value={pretty(panel.data.runtime)} /></div> : null}
    </div>
  );
}
