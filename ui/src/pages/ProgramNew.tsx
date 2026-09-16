import { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Card, Field, PrimaryButton, inputClass } from "../components/ui";
import { DryRunControl } from "../components/ActorStrip";
import { ErrorBanner } from "../components/RecoveryBanner";
import { normalizeProgramCode, programCodeValid } from "../lib/programs";
import { useSession } from "../state/session";

export function ProgramNewPage() {
  const session = useSession();
  const navigate = useNavigate();
  const [code, setCode] = useState("");
  const [name, setName] = useState("");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const ready = programCodeValid(code) && Boolean(name.trim());

  async function onSave(event: FormEvent) {
    event.preventDefault();
    if (!ready) {
      return;
    }
    setError(null);
    setSaving(true);
    try {
      const created = await session.client.createProgram({ code, name: name.trim() });
      if (created.dry_run) {
        setError(new Error("Dry-run is on. Uncheck Dry-run in the header to write program/<code>."));
        return;
      }
      navigate(`/programs/${encodeURIComponent(created.id)}`);
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setSaving(false);
    }
  }

  return (
    <div data-testid="program-new">
      <div className="mb-2 flex flex-wrap items-center justify-between gap-2">
        <h2 className="text-lg font-semibold text-stone-800">New program</h2>
        <DryRunControl />
      </div>
      <p className="mb-4 text-sm text-stone-500">
        Program Code is lowercase English with no spaces. Save writes{" "}
        <span className="font-mono">program/&lt;code&gt;</span>.
      </p>
      <ErrorBanner error={error} />
      <form className="grid max-w-xl gap-4" onSubmit={(event) => void onSave(event)}>
        <Card>
          <div className="grid gap-3">
            <Field label="Program Code" hint="lowercase letters and digits, no spaces">
              <input
                className={`${inputClass} font-mono`}
                value={code}
                required
                autoComplete="off"
                spellCheck={false}
                data-testid="program-code"
                placeholder="e.g. springlaunch"
                onChange={(event) => setCode(normalizeProgramCode(event.target.value))}
              />
            </Field>
            <Field label="Program Name">
              <input
                className={inputClass}
                value={name}
                required
                data-testid="program-name"
                placeholder="e.g. Spring Launch"
                onChange={(event) => setName(event.target.value)}
              />
            </Field>
          </div>
          <div className="mt-4">
            <PrimaryButton type="submit" data-testid="program-save" disabled={saving || !ready}>
              {saving ? "Saving…" : "Save"}
            </PrimaryButton>
          </div>
        </Card>
      </form>
    </div>
  );
}
