import { FormEvent, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Card, GhostButton, PrimaryButton } from "../components/ui";
import { DryRunControl } from "../components/ActorStrip";
import { ErrorBanner } from "../components/RecoveryBanner";
import { ProjectStartFields, ProjectStartSuggestion, type ProjectStartValues } from "../components/ProjectStartFields";
import type { ProjectCatalogItem, ProjectSuggestion } from "../api/types";
import { applyLlmSuggestion } from "../lib/projects";
import { useSession } from "../state/session";

export function ProjectNewPage() {
  const session = useSession();
  const navigate = useNavigate();
  const [values, setValues] = useState<ProjectStartValues>({
    name: "",
    title: "",
    brief: "",
    audience: "",
    duration: "15s",
    outlets: "social",
    risk: "low",
    notes: "",
  });
  const [pending, setPending] = useState(false);
  const [consulting, setConsulting] = useState(false);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const [catalog, setCatalog] = useState<ProjectCatalogItem[]>([]);
  const [suggestion, setSuggestion] = useState<ProjectSuggestion | null>(null);
  const [selected, setSelected] = useState("");
  const [picked, setPicked] = useState(false);

  const form = {
    ...values,
    title: values.title || values.name,
  };

  useEffect(() => {
    session.client
      .getProjectCatalog()
      .then((payload) => setCatalog(payload.items ?? []))
      .catch(() => undefined);
  }, [session.client]);

  useEffect(() => {
    if (suggestion && !picked) {
      setSelected(suggestion.primary);
    }
  }, [suggestion, picked]);

  async function onSuggest(event: FormEvent) {
    event.preventDefault();
    setError(null);
    setPending(true);
    try {
      const next = await session.client.suggestProject(form);
      setPicked(false);
      setSuggestion(next);
      setSelected(next.primary);
      const prompt = next.prompt;
      if (!prompt) {
        return;
      }
      setConsulting(true);
      const abort = typeof AbortSignal.timeout === "function" ? AbortSignal.timeout(12000) : undefined;
      void session.client
        .chatAgent("video.planner", { message: prompt }, abort ? { signal: abort } : undefined)
        .then((chat) => {
          const reply = chat.reply || "";
          setSuggestion((current) => {
            if (!current) {
              return current;
            }
            return applyLlmSuggestion(current, reply, current.catalog ?? catalog);
          });
        })
        .catch(() => undefined)
        .finally(() => setConsulting(false));
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setPending(false);
    }
  }

  async function onSave() {
    if (!selected) {
      return;
    }
    setError(null);
    setSaving(true);
    try {
      const created = await session.client.createProject({
        ...form,
        sub_workflow_id: selected,
        suggestion,
      });
      if (created.dry_run) {
        setError(new Error("Dry-run is on. Uncheck Dry-run in the header to write project/<name>/ and the Start record."));
        return;
      }
      navigate(`/projects/${encodeURIComponent(created.id)}/start`);
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setSaving(false);
    }
  }

  return (
    <div data-testid="project-new">
      <div className="mb-2 flex flex-wrap items-center justify-between gap-2">
        <h2 className="text-lg font-semibold text-stone-800">New project</h2>
        <DryRunControl />
      </div>
      <p className="mb-4 text-sm text-stone-500">
        Draft intent only: clip type and an adult subject, no SKU, no shot list. Rank a sub-workflow, then click{" "}
        <span className="font-medium text-stone-700">Save</span> to write the Start record. CHARACTERIZATION only — not
        an eval PASS. Tools stay off.
      </p>
      {error ? (
        <div data-testid="project-error">
          <ErrorBanner error={error} />
        </div>
      ) : (
        <ErrorBanner error={error} />
      )}
      <form className="grid max-w-3xl gap-4" onSubmit={(event) => void onSuggest(event)}>
        <Card>
          <ProjectStartFields value={values} onChange={setValues} />
          <p className="mt-3 text-[11px] text-stone-500">
            Save is below the ranked sub-workflow. It writes <span className="font-mono">project/&lt;name&gt;</span> and
            the read-only Start page. Ranking does not save.
          </p>
          <div className="mt-4">
            <PrimaryButton type="submit" data-testid="project-suggest" disabled={pending || !values.name.trim() || !values.brief.trim()}>
              {pending ? "Ranking…" : "Suggest sub-workflow"}
            </PrimaryButton>
          </div>
        </Card>
      </form>
      {suggestion ? (
        <div className="mt-4 max-w-3xl">
          <Card>
            <ProjectStartSuggestion
              suggestion={suggestion}
              selected={selected}
              consulting={consulting}
              onSelect={(id) => {
                setPicked(true);
                setSelected(id);
              }}
            />
            <div className="mt-4 flex gap-2">
              <PrimaryButton type="button" data-testid="project-save" disabled={saving || !selected} onClick={() => void onSave()}>
                {saving ? "Saving…" : session.dryRun ? "Save (dry-run)" : "Save"}
              </PrimaryButton>
              <GhostButton type="button" onClick={() => setSuggestion(null)}>
                Back
              </GhostButton>
            </div>
          </Card>
        </div>
      ) : null}
    </div>
  );
}
