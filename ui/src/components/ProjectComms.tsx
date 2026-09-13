import { useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import type { ProjectCommItem, ProjectCommTag } from "../api/types";
import { parseOptionBlock } from "../lib/chatOptions";
import { displayPartyName, hopExtra, sourceCommId } from "../lib/projectChat";
import { OptionTags } from "./OptionTags";
import { GhostButton, PrimaryButton, inputClass } from "./ui";

export function ProjectCommsPanel({
  projectId,
  items,
  focusId,
  instruction,
  onInstruction,
  onLaunch,
  launching,
}: {
  projectId: string;
  items: ProjectCommItem[];
  focusId: string;
  instruction: string;
  onInstruction: (value: string) => void;
  onLaunch: () => void;
  launching: boolean;
}) {
  const navigate = useNavigate();
  const focusRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    if (!focusId) {
      return;
    }
    const node = document.querySelector(`[data-comm-id="${CSS.escape(focusId)}"]`);
    if (node instanceof HTMLElement) {
      focusRef.current = node;
      node.scrollIntoView({ block: "center", behavior: "smooth" });
    }
  }, [focusId, items]);

  function openTag(tag: ProjectCommTag) {
    const href = `/projects/${encodeURIComponent(tag.project_id)}/chat?comm=${encodeURIComponent(tag.comm_id)}`;
    if (tag.project_id !== projectId) {
      navigate(href);
      return;
    }
    navigate(href, { replace: true });
  }

  return (
    <aside
      className="flex min-h-0 max-h-72 flex-1 flex-col overflow-hidden rounded-2xl border border-stone-200 bg-white lg:max-h-none"
      data-testid="project-comms"
    >
      <div className="border-b border-stone-100 p-3">
        <h3 className="text-sm font-semibold text-stone-900">Node communications</h3>
        <p className="mt-1 text-[11px] text-stone-500">
          Create Project is high-level intent only. Experts on each node suggest options; you or a parent agent pick.
        </p>
        <textarea
          className={`${inputClass} mt-2 h-20 py-2 text-xs`}
          data-testid="project-first-instruction"
          placeholder="High-level intent only (details are decided on expert nodes)"
          value={instruction}
          onChange={(event) => onInstruction(event.target.value)}
        />
        <div className="mt-2">
          <PrimaryButton type="button" data-testid="project-run" disabled={launching} onClick={onLaunch}>
            {launching ? "Running…" : "Launch workflow"}
          </PrimaryButton>
        </div>
      </div>
      <ul className="flex-1 space-y-2 overflow-y-auto p-3">
        {items.length === 0 ? (
          <li className="text-xs text-stone-400">No communications yet.</li>
        ) : (
          items.map((item) => {
            const parsed = parseOptionBlock(item.text);
            const sourceId = sourceCommId(item, items);
            const fromName = displayPartyName(item.from);
            const toName = displayPartyName(item.to);
            const extra = hopExtra(item, parsed.options.length);
            const body = parsed.body || (parsed.options.length ? "" : item.text);
            return (
            <li key={item.id}>
              <article
                data-comm-id={item.id}
                data-testid={`project-comm-${item.id}`}
                className={[
                  "rounded-xl border px-3 py-2 text-xs",
                  focusId === item.id ? "border-amber-400 bg-amber-50 ring-2 ring-amber-300" : "border-stone-200 bg-stone-50",
                ].join(" ")}
              >
                <p className="text-[11px] text-stone-600" data-testid={`project-comm-header-${item.id}`}>
                  {sourceId ? (
                    <button
                      type="button"
                      className="font-semibold text-indigo-700 underline decoration-indigo-300 underline-offset-2 hover:text-indigo-900"
                      data-testid={`project-comm-output-agent-${item.id}`}
                      onClick={() =>
                        navigate(
                          `/projects/${encodeURIComponent(projectId)}/chat?comm=${encodeURIComponent(sourceId)}`,
                        )
                      }
                    >
                      {fromName}
                    </button>
                  ) : (
                    <span className="font-semibold text-stone-800">{fromName}</span>
                  )}
                  <span className="text-stone-400"> → </span>
                  <span className="font-semibold text-stone-800">{toName}</span>
                  <span className="text-stone-400"> | {extra}</span>
                </p>
                {body ? (
                  <p className="mt-1 max-h-24 overflow-auto whitespace-pre-wrap text-stone-800">{body.slice(0, 800)}</p>
                ) : null}
                <OptionTags
                  options={parsed.options}
                  selected={parsed.selected || parsed.recommend}
                  recommend={parsed.recommend}
                  commId={item.id}
                  owner={item.from}
                  onPick={() =>
                    navigate(
                      `/projects/${encodeURIComponent(projectId)}/chat?comm=${encodeURIComponent(item.id)}`,
                    )
                  }
                />
                <TagRow label="in" tags={item.input_tags} onOpen={openTag} />
                <TagRow label="out" tags={item.output_tags} onOpen={openTag} />
              </article>
            </li>
            );
          })
        )}
      </ul>
      <div className="border-t border-stone-100 p-2">
        <GhostButton
          type="button"
          onClick={() => navigate(`/projects/${encodeURIComponent(projectId)}/workflow`)}
        >
          Clear highlight
        </GhostButton>
      </div>
    </aside>
  );
}

function TagRow({
  label,
  tags,
  onOpen,
}: {
  label: string;
  tags: ProjectCommTag[];
  onOpen: (tag: ProjectCommTag) => void;
}) {
  if (!tags.length) {
    return null;
  }
  return (
    <p className="mt-1 flex flex-wrap items-center gap-1">
      <span className="text-[10px] uppercase text-stone-400">{label}</span>
      {tags.map((tag) => (
        <button
          key={`${tag.comm_id}-${tag.label}`}
          type="button"
          className="nodrag rounded-full border border-indigo-200 bg-white px-2 py-0.5 font-mono text-[10px] text-indigo-700 hover:bg-indigo-50"
          data-testid={`project-tag-${tag.comm_id}-${tag.label}`}
          onClick={() => onOpen(tag)}
        >
          {tag.label}
        </button>
      ))}
    </p>
  );
}
