import type { RuntimeAdapter } from "../api/types";

export function AdapterStatus({
  adapter,
  testId = "adapter-status",
}: {
  adapter?: RuntimeAdapter | null;
  testId?: string;
}) {
  const kind = adapter?.kind ?? "host_llm";
  const grok = adapter?.grok_available ? "yes" : "no";
  const profile = adapter?.profile_ready ? "ready" : "missing";
  const pid = adapter?.pid ?? null;
  const healthy = adapter?.healthy ? "yes" : "no";
  return (
    <section className="rounded-2xl border border-stone-200 bg-white p-5" data-testid={testId}>
      <h2 className="mb-1 text-sm font-semibold text-stone-900">Adapter</h2>
      <p className="mb-3 text-xs text-stone-500">
        Selected before send. {kind === "grok_acp" ? "UI → API → one Grok process per agent." : "In-process host LLM."}{" "}
        Memory, plugins, and T3 stay off.
      </p>
      <dl className="grid grid-cols-2 gap-2 font-mono text-[11px] text-stone-700">
        <div>
          <dt className="text-stone-500">kind</dt>
          <dd data-testid="adapter-kind">{kind}</dd>
        </div>
        <div>
          <dt className="text-stone-500">grok</dt>
          <dd>{grok}</dd>
        </div>
        <div>
          <dt className="text-stone-500">profile</dt>
          <dd>{profile}</dd>
        </div>
        <div>
          <dt className="text-stone-500">pid</dt>
          <dd>{pid ?? "—"}</dd>
        </div>
        <div>
          <dt className="text-stone-500">healthy</dt>
          <dd>{healthy}</dd>
        </div>
      </dl>
    </section>
  );
}
