import { Check } from "lucide-react";
import type { ChatOption } from "../lib/chatOptions";
import { displayPartyName, optionAgentIds } from "../lib/projectChat";

export function OptionTags({
  options,
  selected,
  recommend,
  commId,
  owner,
  onPick,
}: {
  options: ChatOption[];
  selected?: string;
  recommend?: string;
  commId?: string;
  owner?: string;
  onPick?: (optionId: string) => void;
}) {
  if (!options.length) {
    return null;
  }
  return (
    <div className="mt-2" data-testid={commId ? `project-chat-options-${commId}` : "project-chat-options"}>
      <p className="mb-1 text-[10px] font-semibold uppercase tracking-wide text-stone-400">Options</p>
      <div className="flex flex-col gap-1.5">
        {options.map((option) => {
          const active = selected === option.id;
          const rec = !active && recommend === option.id;
          const agents = optionAgentIds(owner || "", `${option.label} ${option.why}`);
          return (
            <button
              key={option.id}
              type="button"
              className={[
                "flex w-full items-start gap-1.5 rounded-xl border px-2 py-1.5 text-left text-[11px]",
                active
                  ? "border-indigo-500 bg-indigo-600 text-white"
                  : rec
                    ? "border-indigo-300 bg-indigo-50 text-indigo-800 dark:border-indigo-700 dark:bg-indigo-950 dark:text-indigo-100"
                    : "border-indigo-200 bg-white text-indigo-900 hover:bg-indigo-50 dark:border-indigo-800 dark:bg-stone-900 dark:text-indigo-100",
              ].join(" ")}
              data-testid={`project-option-tag-${option.id}`}
              data-option-id={option.id}
              data-selected={active ? "true" : "false"}
              onClick={() => onPick?.(option.id)}
            >
              {active ? (
                <Check size={12} className="mt-0.5 shrink-0" aria-hidden="true" data-testid={`project-option-check-${option.id}`} />
              ) : (
                <span className="mt-0.5 inline-block h-3 w-3 shrink-0" aria-hidden="true" />
              )}
              <span className="min-w-0 flex-1">
                <span className="font-mono text-[10px] uppercase tracking-wide">
                  tag {option.id}
                  {active ? " · selected" : rec ? " · rec" : ""}
                </span>
                {agents.length ? (
                  <span className="mt-0.5 flex flex-wrap gap-1">
                    {agents.map((agent) => (
                      <span
                        key={agent}
                        className={[
                          "rounded-full border px-1.5 py-0 font-mono text-[10px]",
                          active ? "border-white/40 text-white" : "border-indigo-200 text-indigo-700 dark:border-indigo-700 dark:text-indigo-200",
                        ].join(" ")}
                      >
                        {displayPartyName(agent)}
                      </span>
                    ))}
                  </span>
                ) : null}
                <span className="mt-0.5 block font-medium leading-snug">{option.label}</span>
                {option.why ? (
                  <span className={["mt-0.5 block leading-snug", active ? "text-indigo-100" : "text-stone-600 dark:text-stone-300"].join(" ")}>
                    {option.why}
                  </span>
                ) : null}
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
}
