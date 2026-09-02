import { useState } from "react";
import { ACTORS, type ActorClass } from "../api/types";
import { Card, Field, PageHeader, PrimaryButton, inputClass } from "../components/ui";
import { ErrorBanner } from "../components/RecoveryBanner";
import { useAsync } from "../lib/hooks";
import { useSession } from "../state/session";

export function SettingsPage() {
  const session = useSession();
  const settings = session.settings;
  const llm = useAsync(() => session.client.getLlmSettings(), [session.client]);
  const [choice, setChoice] = useState<string>("");
  const [notice, setNotice] = useState<string | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const selected = choice || llm.data?.default_llm || "local_deterministic";

  return (
    <div>
      <PageHeader title="Settings" />
      <div className="grid grid-cols-1 gap-5 lg:grid-cols-2">
        <Card>
          <h2 className="mb-4 text-sm font-semibold">Control plane</h2>
          <Field label="Base URL" hint="Leave empty to use the Vite proxy to http://127.0.0.1:18080">
            <input
              className={`${inputClass} font-mono`}
              placeholder="http://127.0.0.1:18080"
              value={settings.baseUrl}
              onChange={(event) => session.setSettings({ ...settings, baseUrl: event.target.value.trim() })}
            />
          </Field>
          <div className="mt-4">
            <Field label="Agent Swarm poll interval (ms)">
              <input
                className={inputClass}
                type="number"
                min={5000}
                value={settings.pollMs}
                onChange={(event) => session.setSettings({ ...settings, pollMs: Number(event.target.value) || 15000 })}
              />
            </Field>
          </div>
        </Card>
        <Card>
          <h2 className="mb-4 text-sm font-semibold">Actor defaults</h2>
          <Field label="Default actor">
            <select
              className={inputClass}
              value={settings.defaultActor}
              onChange={(event) => session.setSettings({ ...settings, defaultActor: event.target.value as ActorClass })}
            >
              {ACTORS.map((actor) => (
                <option key={actor} value={actor}>
                  {actor}
                </option>
              ))}
            </select>
          </Field>
          <label className="mt-4 flex items-center gap-2 text-sm text-stone-700">
            <input
              type="checkbox"
              checked={settings.defaultDryRun}
              onChange={(event) => session.setSettings({ ...settings, defaultDryRun: event.target.checked })}
            />
            Default dry-run ON
          </label>
          <label className="mt-3 flex items-center gap-2 text-sm text-stone-700">
            <input
              type="checkbox"
              checked={settings.persistActor}
              onChange={(event) => session.setSettings({ ...settings, persistActor: event.target.checked })}
            />
            Persist actor on this machine (opt-in)
          </label>
        </Card>
        <Card className="lg:col-span-2">
          <h2 className="mb-2 text-sm font-semibold">Default LLM</h2>
          <p className="mb-3 text-sm text-stone-500">
            Host-owned. Keys stay in <span className="font-mono">.env</span>. Agents inherit{" "}
            <span className="font-mono">DEFAULT_LLM</span> unless overridden on the agent page. This does not grant
            the agent network access.
          </p>
          <ErrorBanner error={error ?? llm.error} />
          {notice ? <p className="mb-3 font-mono text-xs text-stone-600">{notice}</p> : null}
          <Field label="DEFAULT_LLM" hint={`env default ${llm.data?.env_default ?? "local_deterministic"} · source ${llm.data?.default_source ?? "DEFAULT_LLM"}`}>
            <select className={inputClass} value={selected} onChange={(event) => setChoice(event.target.value)}>
              {(llm.data?.providers ?? []).map((provider) => (
                <option key={provider.id} value={provider.id} disabled={!provider.configured}>
                  {provider.label}
                  {provider.model ? ` (${provider.model})` : ""}
                  {provider.configured ? "" : " — not configured in .env"}
                </option>
              ))}
            </select>
          </Field>
          <div className="mt-4">
            <PrimaryButton
              type="button"
              disabled={!session.mutationReady}
              onClick={() => {
                setError(null);
                void session.client
                  .setLlmSettings(selected)
                  .then((view) => {
                    setNotice(view.dry_run ? "dry-run: not persisted" : `saved default_llm=${view.default_llm}`);
                    llm.reload();
                  })
                  .catch((err: unknown) => setError(err instanceof Error ? err : new Error(String(err))));
              }}
            >
              {session.dryRun ? "Preview default LLM" : "Save default LLM"}
            </PrimaryButton>
          </div>
        </Card>
        <Card className="lg:col-span-2">
          <h2 className="mb-2 text-sm font-semibold">Known agent IDs</h2>
          <p className="mb-3 text-sm text-stone-500">
            Used when GET /api/v3/agents is missing. Discovery {session.discovery}. Do not paste host Ed25519 keys here.
          </p>
          <textarea
            className="min-h-[8rem] w-full rounded-xl border border-stone-200 bg-white p-3 font-mono text-sm text-stone-900"
            value={settings.knownIds.join("\n")}
            onChange={(event) =>
              session.setSettings({
                ...settings,
                knownIds: event.target.value
                  .split(/\s+/)
                  .map((item) => item.trim())
                  .filter(Boolean),
              })
            }
          />
        </Card>
        <Card className="lg:col-span-2 bg-stone-50 hover:shadow-none">
          <p className="text-sm text-stone-600">Never store production secrets in this UI. Localhost operator tool. No SSO.</p>
        </Card>
      </div>
    </div>
  );
}
