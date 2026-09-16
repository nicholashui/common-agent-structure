import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { Card, Field, GhostButton, inputClass } from "../components/ui";
import { DryRunControl } from "../components/ActorStrip";
import { ErrorBanner } from "../components/RecoveryBanner";
import type { ProgramRecord } from "../api/types";
import { displayRelativePath } from "../lib/paths";
import { useSession } from "../state/session";

export function ProgramViewPage() {
  const params = useParams();
  const programId = params.programId ? decodeURIComponent(params.programId) : "";
  const session = useSession();
  const navigate = useNavigate();
  const [record, setRecord] = useState<ProgramRecord | null>(null);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    if (!programId) {
      return;
    }
    session.client
      .getProgram(programId)
      .then(setRecord)
      .catch((err) => setError(err instanceof Error ? err : new Error(String(err))));
  }, [programId, session.client]);

  return (
    <div data-testid="program-view">
      <div className="mb-2 flex flex-wrap items-center justify-between gap-2">
        <h2 className="text-lg font-semibold text-stone-800 dark:text-stone-100">Start</h2>
        <div className="flex flex-wrap items-center gap-2">
          <DryRunControl />
          <GhostButton type="button" onClick={() => navigate(`/programs/${encodeURIComponent(programId)}/workflow`)}>
            Workflow
          </GhostButton>
        </div>
      </div>
      <p className="mb-4 text-sm text-stone-500">
        Read-only record of Program / New program. Written only when you click Save there. Same idea as Project Start.
      </p>
      <ErrorBanner error={error} />
      {record ? (
        <Card data-testid="program-start">
          <div className="grid max-w-xl gap-3">
            <Field label="Program Code" hint="lowercase letters, digits, hyphens; no spaces">
              <input className={`${inputClass} font-mono`} value={record.code} readOnly disabled data-testid="program-code" />
            </Field>
            <Field label="Program Name">
              <input className={inputClass} value={record.name} readOnly disabled data-testid="program-name" />
            </Field>
            <p className="font-mono text-xs text-stone-500">{displayRelativePath(record.folder)}</p>
          </div>
        </Card>
      ) : !error ? (
        <p className="text-sm text-stone-500">Loading Start record…</p>
      ) : null}
    </div>
  );
}
