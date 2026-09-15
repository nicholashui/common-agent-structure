import { Field, inputClass } from "./ui";
import type { ProjectSuggestion } from "../api/types";
import { STUDY_PLACEHOLDER } from "../lib/projectDrafts";

export const DURATIONS = ["15s", "30s", "60s", "3min", "10min"];
export const OUTLETS = ["social", "web", "broadcast"];
export const RISKS = ["low", "medium", "high"];

export type ProjectStartValues = {
  name: string;
  title: string;
  brief: string;
  audience: string;
  duration: string;
  outlets: string;
  risk: string;
  notes: string;
};

export function ProjectStartFields({
  value,
  onChange,
  readOnly,
}: {
  value: ProjectStartValues;
  onChange?: (next: ProjectStartValues) => void;
  readOnly?: boolean;
}) {
  function patch(partial: Partial<ProjectStartValues>) {
    onChange?.({ ...value, ...partial });
  }
  const disabled = Boolean(readOnly);
  return (
    <div className="grid gap-3 sm:grid-cols-2">
      <Field label="Project name" hint={readOnly ? "Folder slug under project/." : "New folder slug under project/."}>
        <input
          className={inputClass}
          value={value.name}
          required
          disabled={disabled}
          readOnly={readOnly}
          data-testid="project-name"
          placeholder={STUDY_PLACEHOLDER.name}
          onChange={(event) => patch({ name: event.target.value })}
        />
      </Field>
      <Field label="Title">
        <input
          className={inputClass}
          value={value.title}
          disabled={disabled}
          readOnly={readOnly}
          data-testid="project-title"
          placeholder={STUDY_PLACEHOLDER.title}
          onChange={(event) => patch({ title: event.target.value })}
        />
      </Field>
      <div className="sm:col-span-2">
        <Field label="Brief" hint="First Chat hop only: clip type + adult subject. No product, no coverage, no lighting.">
          <textarea
            className={`${inputClass} h-20 py-2`}
            value={value.brief}
            required
            disabled={disabled}
            readOnly={readOnly}
            data-testid="project-brief"
            placeholder={STUDY_PLACEHOLDER.brief}
            onChange={(event) => patch({ brief: event.target.value })}
          />
        </Field>
      </div>
      <Field label="Audience">
        <input
          className={inputClass}
          value={value.audience}
          disabled={disabled}
          readOnly={readOnly}
          data-testid="project-audience"
          placeholder={STUDY_PLACEHOLDER.audience}
          onChange={(event) => patch({ audience: event.target.value })}
        />
      </Field>
      <Field label="Duration">
        <select
          className={inputClass}
          value={value.duration}
          disabled={disabled}
          data-testid="project-duration"
          onChange={(event) => patch({ duration: event.target.value })}
        >
          {DURATIONS.map((item) => (
            <option key={item} value={item}>
              {item}
            </option>
          ))}
        </select>
      </Field>
      <Field label="Outlets">
        <select
          className={inputClass}
          value={value.outlets}
          disabled={disabled}
          data-testid="project-outlets"
          onChange={(event) => patch({ outlets: event.target.value })}
        >
          {OUTLETS.map((item) => (
            <option key={item} value={item}>
              {item}
            </option>
          ))}
        </select>
      </Field>
      <Field label="Risk">
        <select
          className={inputClass}
          value={value.risk}
          disabled={disabled}
          data-testid="project-risk"
          onChange={(event) => patch({ risk: event.target.value })}
        >
          {RISKS.map((item) => (
            <option key={item} value={item}>
              {item}
            </option>
          ))}
        </select>
      </Field>
      <div className="sm:col-span-2">
        <Field label="Notes" hint="Honesty: sub-workflow SVG is the pack map, not the Chat creative lock.">
          <input
            className={inputClass}
            value={value.notes}
            disabled={disabled}
            readOnly={readOnly}
            data-testid="project-notes"
            placeholder={STUDY_PLACEHOLDER.notes}
            onChange={(event) => patch({ notes: event.target.value })}
          />
        </Field>
      </div>
    </div>
  );
}

export function ProjectStartSuggestion({
  suggestion,
  selected,
  onSelect,
  consulting,
  readOnly,
}: {
  suggestion: ProjectSuggestion;
  selected: string;
  onSelect?: (id: string) => void;
  consulting?: boolean;
  readOnly?: boolean;
}) {
  return (
    <div className="mt-4 max-w-3xl" data-testid="project-suggestions">
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
                disabled={readOnly}
                onChange={() => onSelect?.(row.id)}
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
    </div>
  );
}
