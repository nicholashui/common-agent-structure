import { FormEvent, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Card, Field, GhostButton, PrimaryButton, inputClass } from "../components/ui";
import { DryRunControl } from "../components/ActorStrip";
import { ErrorBanner } from "../components/RecoveryBanner";
import type { ProjectCatalogItem, ProjectSuggestion } from "../api/types";
import { applyLlmSuggestion } from "../lib/projects";
import { useSession } from "../state/session";

const DURATIONS = ["15s", "30s", "60s", "3min", "10min"];
const OUTLETS = ["social", "web", "broadcast"];
const RISKS = ["low", "medium", "high"];

export function ProjectNewPage() {
  const session = useSession();
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [title, setTitle] = useState("");
  const [brief, setBrief] = useState("");
  const [audience, setAudience] = useState("");
  const [duration, setDuration] = useState("15s");
  const [outlets, setOutlets] = useState("social");
  const [risk, setRisk] = useState("low");
  const [notes, setNotes] = useState("");
  const [pending, setPending] = useState(false);
  const [consulting, setConsulting] = useState(false);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const [catalog, setCatalog] = useState<ProjectCatalogItem[]>([]);
  const [suggestion, setSuggestion] = useState<ProjectSuggestion | null>(null);
  const [selected, setSelected] = useState("");
  const [picked, setPicked] = useState(false);

  const form = {
    name,
    title: title || name,
    brief,
    audience,
    duration,
    outlets,
    risk,
    notes,
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

  async function onConfirm() {
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
        setError(new Error("Dry-run is on. Uncheck Dry-run in the header to write project/<name>/."));
        return;
      }
      navigate(`/projects/${encodeURIComponent(created.id)}`);
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
        Draft a video sub-workflow under <span className="font-mono">project/&lt;name&gt;</span>. Ranked against
        templates A–J and scales S1–S7, then the host asks <span className="font-mono">video.planner</span> which to
        use. CHARACTERIZATION only — not an eval PASS. Tools stay off.
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
          <div className="grid gap-3 sm:grid-cols-2">
            <Field label="Project name" hint="Folder slug under project/">
              <input
                className={inputClass}
                value={name}
                required
                data-testid="project-name"
                placeholder="safety-recap"
                onChange={(event) => setName(event.target.value)}
              />
            </Field>
            <Field label="Title">
              <input
                className={inputClass}
                value={title}
                data-testid="project-title"
                placeholder="Factory-floor safety recap"
                onChange={(event) => setTitle(event.target.value)}
              />
            </Field>
            <Field label="Brief">
              <textarea
                className={`${inputClass} h-20 py-2`}
                value={brief}
                required
                data-testid="project-brief"
                placeholder="What should this video do?"
                onChange={(event) => setBrief(event.target.value)}
              />
            </Field>
            <Field label="Audience">
              <input
                className={inputClass}
                value={audience}
                data-testid="project-audience"
                placeholder="shop-floor operators"
                onChange={(event) => setAudience(event.target.value)}
              />
            </Field>
            <Field label="Duration">
              <select
                className={inputClass}
                value={duration}
                data-testid="project-duration"
                onChange={(event) => setDuration(event.target.value)}
              >
                {DURATIONS.map((item) => (
                  <option key={item} value={item}>
                    {item}
                  </option>
                ))}
              </select>
            </Field>
            <Field label="Outlets">
              <select className={inputClass} value={outlets} onChange={(event) => setOutlets(event.target.value)}>
                {OUTLETS.map((item) => (
                  <option key={item} value={item}>
                    {item}
                  </option>
                ))}
              </select>
            </Field>
            <Field label="Risk">
              <select className={inputClass} value={risk} onChange={(event) => setRisk(event.target.value)}>
                {RISKS.map((item) => (
                  <option key={item} value={item}>
                    {item}
                  </option>
                ))}
              </select>
            </Field>
            <Field label="Notes">
              <input className={inputClass} value={notes} onChange={(event) => setNotes(event.target.value)} />
            </Field>
          </div>
          <div className="mt-4">
            <PrimaryButton type="submit" data-testid="project-suggest" disabled={pending || !name.trim() || !brief.trim()}>
              {pending ? "Ranking…" : "Suggest sub-workflow"}
            </PrimaryButton>
          </div>
        </Card>
      </form>
      {suggestion ? (
        <div className="mt-4 max-w-3xl" data-testid="project-suggestions">
        <Card>
          <h3 className="text-sm font-semibold text-stone-900">Suggested video sub-workflow</h3>
          <p className="mt-1 text-xs text-stone-500" data-testid="project-suggest-note">
            {suggestion.note}{" "}
            {consulting
              ? "Consulting video.planner…"
              : suggestion.llm_used
                ? "Planner LLM consulted."
                : "Heuristic ranking — planner not consulted yet."}
          </p>
          <ul className="mt-3 space-y-2">
            {suggestion.suggestions.map((row) => (
              <li key={row.id}>
                <label className="flex cursor-pointer items-start gap-2 rounded-xl border border-stone-200 px-3 py-2 hover:bg-stone-50">
                  <input
                    type="radio"
                    name="sub-workflow"
                    data-testid={`project-pick-${row.id}`}
                    checked={selected === row.id}
                    onChange={() => {
                      setPicked(true);
                      setSelected(row.id);
                    }}
                  />
                  <span>
                    <span className="block text-sm font-medium text-stone-800">{row.label}</span>
                    <span className="block font-mono text-[11px] text-stone-500">
                      {row.id} · {row.source}
                    </span>
                    <span className="block text-xs text-stone-500">{row.reason}</span>
                  </span>
                </label>
              </li>
            ))}
          </ul>
          {suggestion.llm_excerpt ? (
            <pre className="mt-3 max-h-32 overflow-auto rounded-lg bg-stone-50 p-2 font-mono text-[11px] text-stone-600">
              {suggestion.llm_excerpt}
            </pre>
          ) : null}
          <div className="mt-4 flex gap-2">
            <PrimaryButton type="button" data-testid="project-confirm" disabled={saving || !selected} onClick={() => void onConfirm()}>
              {saving ? "Saving…" : session.dryRun ? "Confirm (dry-run)" : "Confirm and open designer"}
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
