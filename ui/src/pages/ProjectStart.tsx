import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { Card, GhostButton } from "../components/ui";
import { ErrorBanner } from "../components/RecoveryBanner";
import { ProjectStartFields, ProjectStartSuggestion } from "../components/ProjectStartFields";
import type { ProjectRecord, ProjectStartSnapshot } from "../api/types";
import { rememberProject } from "../lib/projectContext";
import { useSession } from "../state/session";

function valuesFromStart(start: ProjectStartSnapshot, fallback: ProjectRecord) {
  return {
    name: start.name || fallback.name || fallback.id,
    title: start.title || fallback.title || "",
    brief: start.brief || fallback.brief || "",
    audience: start.audience || fallback.audience || "",
    duration: start.duration || fallback.duration || "15s",
    outlets: start.outlets || fallback.outlets || "social",
    risk: start.risk || fallback.risk || "low",
    notes: start.notes || fallback.notes || "",
  };
}

export function ProjectStartPage() {
  const params = useParams();
  const projectId = params.projectId ? decodeURIComponent(params.projectId) : "";
  const session = useSession();
  const navigate = useNavigate();
  const [record, setRecord] = useState<ProjectRecord | null>(null);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    if (!projectId) {
      return;
    }
    rememberProject(projectId);
    session.client
      .getProject(projectId)
      .then(setRecord)
      .catch((err) => setError(err instanceof Error ? err : new Error(String(err))));
  }, [projectId, session.client]);

  const start = record?.start;
  const values = start && record ? valuesFromStart(start, record) : null;
  const selected = start?.sub_workflow_id || record?.sub_workflow_id || "";
  const suggestion = start?.suggestion || record?.suggestion || null;

  return (
    <div data-testid="project-start">
      <div className="mb-2 flex flex-wrap items-center justify-between gap-2">
        <h2 className="text-lg font-semibold text-stone-800">Start</h2>
        <GhostButton type="button" onClick={() => navigate(`/projects/${encodeURIComponent(projectId)}/workflow`)}>
          Workflow
        </GhostButton>
      </div>
      <p className="mb-4 text-sm text-stone-500">
        Read-only record of Project / New project. Written only when you click Save there.
        {record && record.start_persisted === false
          ? " This project has no saved Start yet — fields below are reconstructed from the current project.json."
          : null}
      </p>
      <ErrorBanner error={error} />
      {values ? (
        <div className="grid max-w-3xl gap-4">
          <Card>
            <ProjectStartFields value={values} readOnly />
            {suggestion ? (
              <ProjectStartSuggestion suggestion={suggestion} selected={selected} readOnly />
            ) : selected ? (
              <p className="mt-4 font-mono text-[11px] text-stone-500" data-testid="project-start-workflow-id">
                {selected}
              </p>
            ) : null}
          </Card>
        </div>
      ) : !error ? (
        <p className="text-sm text-stone-500">Loading Start record…</p>
      ) : null}
    </div>
  );
}
