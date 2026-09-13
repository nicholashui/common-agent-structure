import { Handle, Position, type Node, type NodeProps } from "@xyflow/react";
import { Check } from "lucide-react";
import { GRAPH_KIND, socketColor } from "../lib/graphStyle";
import { displayPartyName, optionAgentIds } from "../lib/projectChat";

export type ProjectIo = {
  inputs?: string[];
  outputs?: string[];
};

export type ProjectNodeData = {
  kind: "start" | "agent" | "workflow" | "output" | "human";
  label: string;
  title?: string;
  brief?: string;
  audience?: string;
  duration?: string;
  outlets?: string;
  risk?: string;
  agent_id?: string | null;
  role?: string;
  io?: ProjectIo;
  contract?: string[];
  reason?: string;
  linkedOuts?: string[];
  onNext?: (id: string, outBus?: string) => void;
  thinking?: string;
  options?: { id: string; label: string; why?: string }[];
  recommend?: string;
  decide_by?: string;
  chosen?: string;
  selected_by?: string;
  select_reason?: string;
  onChoose?: (id: string, optionId: string) => void;
};

export type ProjectFlowNode = Node<ProjectNodeData>;

function kindOf(data: ProjectNodeData): keyof typeof GRAPH_KIND {
  if (data.kind === "start") {
    return "start";
  }
  if (data.kind === "output") {
    return "output";
  }
  if (data.kind === "human") {
    return "human";
  }
  if (data.kind === "workflow") {
    return "workflow";
  }
  return "agent";
}

export function ProjectNode({ id, data, selected }: NodeProps<ProjectFlowNode>) {
  const start = data.kind === "start";
  const output = data.kind === "output";
  const human = data.kind === "human";
  const inputs = data.io?.inputs ?? [];
  const outputs = data.io?.outputs ?? [];
  const linked = new Set(data.linkedOuts ?? []);
  const kind = kindOf(data);
  const chrome = GRAPH_KIND[kind];
  const extraInputs = inputs.slice(1);
  return (
    <div
      data-testid={
        start ? "project-start-node" : output ? "project-output-node" : human ? "project-human-node" : "project-agent-node"
      }
      data-node-id={id}
      className={[
        "casops-node w-80 overflow-hidden rounded-md border",
        selected ? "ring-1 ring-stone-900 dark:ring-white" : "",
      ].join(" ")}
    >
      <div
        className="flex h-7 items-center justify-between gap-2 px-2 text-[11px] font-semibold text-white"
        style={{ background: chrome.title }}
      >
        <span className="uppercase tracking-wide">{chrome.label}</span>
        <span className="truncate font-mono text-[10px] opacity-90">{data.label}</span>
      </div>
      {start ? null : (
        <div className="relative flex items-center px-2 py-1">
          <Handle
            type="target"
            id="in"
            position={Position.Left}
            className="!left-[-6px]"
            style={{ background: socketColor(inputs[0] || "in") }}
          />
          <span className="socket-label truncate">{inputs[0] || "in"}</span>
        </div>
      )}
      {extraInputs.map((bus) => (
        <div key={bus} className="relative flex items-center px-2 py-0.5">
          <Handle type="target" id={bus} position={Position.Left} className="!left-[-6px]" style={{ background: socketColor(bus) }} />
          <span className="socket-label truncate">{bus}</span>
        </div>
      ))}
      {start ? (
        <dl className="space-y-0.5 px-2 pb-1 text-[11px] text-stone-500 dark:text-[#bbb]">
          {data.title ? (
            <div>
              <dt className="inline text-stone-400 dark:text-[#888]">Title </dt>
              <dd className="inline text-stone-800 dark:text-[#eee]">{data.title}</dd>
            </div>
          ) : null}
          {data.brief ? <div className="line-clamp-3 text-stone-600 dark:text-[#ccc]">{data.brief}</div> : null}
          {data.audience ? <div>Audience {data.audience}</div> : null}
          {data.duration || data.outlets || data.risk ? (
            <div>{[data.duration, data.outlets, data.risk].filter(Boolean).join(" · ")}</div>
          ) : null}
        </dl>
      ) : (
        <p className="px-2 font-mono text-[11px] text-indigo-700 dark:text-[#9cdcfe]">{data.agent_id || (output ? "generated prompt" : "")}</p>
      )}
      {output || human ? (
        <p className="line-clamp-4 whitespace-pre-wrap px-2 text-[11px] text-stone-500 dark:text-[#bbb]">{data.brief || data.reason}</p>
      ) : null}
      {data.reason && !output && !human ? <p className="px-2 text-[11px] text-stone-500 dark:text-[#aaa]">{data.reason}</p> : null}
      {data.thinking ? (
        <p className="line-clamp-3 px-2 text-[11px] text-stone-600 dark:text-[#ccc]" data-testid={`project-think-${id}`}>
          <span className="font-semibold text-stone-400 dark:text-[#888]">Think </span>
          {data.thinking}
        </p>
      ) : null}
      {data.decide_by ? (
        <p className="px-2 text-[10px] text-stone-500 dark:text-[#aaa]">
          Decide by {data.decide_by}
          {data.recommend ? ` · expert recommends ${data.recommend}` : ""}
        </p>
      ) : null}
      {data.chosen ? (
        <p className="px-2 text-[10px] text-emerald-800 dark:text-[#a5d6a7]" data-testid={`project-chosen-${id}`}>
          Selected {data.chosen}
          {data.selected_by ? ` by ${data.selected_by}` : ""}
        </p>
      ) : null}
      {data.select_reason ? (
        <p className="line-clamp-4 px-2 text-[10px] text-stone-500 dark:text-[#bbb]" data-testid={`project-select-reason-${id}`}>
          Reason {data.select_reason}
        </p>
      ) : null}
      {data.options?.length ? (
        <div className="space-y-1 px-2 py-1" data-testid={`project-options-${id}`}>
          {data.options.map((option) => {
            const active = data.chosen === option.id;
            const rec = !active && data.recommend === option.id;
            const agents = optionAgentIds(data.agent_id || "", `${option.label} ${option.why || ""}`);
            return (
              <button
                key={option.id}
                type="button"
                className={[
                  "nodrag nopan flex w-full items-start gap-1.5 rounded-xl border px-2 py-1.5 text-left text-[11px]",
                  active
                    ? "border-indigo-500 bg-indigo-600 text-white"
                    : rec
                      ? "border-indigo-300 bg-indigo-50 text-indigo-800 dark:border-indigo-700 dark:bg-indigo-950 dark:text-indigo-100"
                      : "border-stone-200 bg-white text-stone-700 hover:border-indigo-300 dark:border-[#4a4a4a] dark:bg-[#2b2b2b] dark:text-[#ccc] dark:hover:border-[#64b5f6]",
                ].join(" ")}
                data-testid={`project-option-${id}-${option.id}`}
                data-selected={active ? "true" : "false"}
                onClick={(event) => {
                  event.stopPropagation();
                  data.onChoose?.(id, option.id);
                }}
              >
                {active ? (
                  <Check size={12} className="mt-0.5 shrink-0" aria-hidden="true" />
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
                            "rounded-full border px-1.5 font-mono text-[10px]",
                            active ? "border-white/40 text-white" : "border-indigo-200 text-indigo-700 dark:border-indigo-700",
                          ].join(" ")}
                        >
                          {displayPartyName(agent)}
                        </span>
                      ))}
                    </span>
                  ) : null}
                  <span className="mt-0.5 block font-medium leading-snug">{option.label}</span>
                  {option.why ? (
                    <span className={["mt-0.5 block leading-snug", active ? "text-indigo-100" : "text-stone-500 dark:text-[#bbb]"].join(" ")}>
                      {option.why}
                    </span>
                  ) : null}
                </span>
              </button>
            );
          })}
        </div>
      ) : null}
      {output ? (
        <p className="px-2 py-1 text-[10px] font-semibold uppercase tracking-wide text-amber-700 dark:text-[#ffcc80]">No Out · end node</p>
      ) : (
        <div className="space-y-0.5 pb-1 pt-1">
          {(outputs.length ? outputs : ["next"]).map((bus) => {
            const named = bus !== "next";
            const used = linked.has(bus);
            return (
              <div key={bus} className="relative flex items-center justify-end px-2 py-0.5">
                <button
                  type="button"
                  className={[
                    "nodrag nopan flex min-w-0 items-center gap-1 rounded px-1.5 py-0.5 text-right text-[11px]",
                    used ? "text-emerald-800 dark:text-[#c8e6c9]" : "text-stone-600 hover:text-stone-900 dark:text-[#ccc] dark:hover:text-white",
                  ].join(" ")}
                  data-testid={named ? `project-out-${id}-${bus}` : `project-next-${id}`}
                  title={named ? `Out ${bus} — suggest next agents` : "Suggest next agents"}
                  onClick={(event) => {
                    event.stopPropagation();
                    data.onNext?.(id, named ? bus : undefined);
                  }}
                >
                  {used ? <span className="text-[9px] font-semibold uppercase text-[#81c784]">linked</span> : null}
                  <span className="socket-label truncate">{named ? bus : "Next"}</span>
                </button>
                <Handle
                  type="source"
                  id={named ? bus : "next"}
                  position={Position.Right}
                  className="!right-[-6px]"
                  style={{ background: socketColor(named ? bus : "next") }}
                />
              </div>
            );
          })}
          {outputs.length ? (
            <button
              type="button"
              className="nodrag nopan mx-2 mb-1 inline-flex items-center rounded border border-stone-200 bg-white px-2 py-0.5 text-[10px] font-medium text-stone-600 hover:border-indigo-300 dark:border-[#4a4a4a] dark:bg-[#2b2b2b] dark:text-[#bbb] dark:hover:border-[#64b5f6] dark:hover:text-white"
              data-testid={`project-next-${id}`}
              title="Suggest next agents for every Out"
              onClick={(event) => {
                event.stopPropagation();
                data.onNext?.(id);
              }}
            >
              Next all
            </button>
          ) : null}
        </div>
      )}
    </div>
  );
}
