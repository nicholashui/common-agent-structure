import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { Card, Field, GhostButton, inputClass } from "../components/ui";
import { ErrorBanner } from "../components/RecoveryBanner";
import type { ProgramRecord } from "../api/types";
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
        <h2 className="text-lg font-semibold text-stone-800">{record?.name || programId || "Program"}</h2>
        <GhostButton type="button" onClick={() => navigate("/programs/new")}>
          New program
        </GhostButton>
      </div>
      <ErrorBanner error={error} />
      {!record && !error ? (
        <p className="text-sm text-stone-500">Loading program…</p>
      ) : record ? (
        <Card className="max-w-xl">
          <div className="grid gap-3">
            <Field label="Program Code">
              <input className={`${inputClass} font-mono`} value={record.code} readOnly disabled data-testid="program-code" />
            </Field>
            <Field label="Program Name">
              <input className={inputClass} value={record.name} readOnly disabled data-testid="program-name" />
            </Field>
          </div>
        </Card>
      ) : null}
    </div>
  );
}
