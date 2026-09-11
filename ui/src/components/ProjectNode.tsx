import { ArrowRight } from "lucide-react";
import { Handle, Position, type Node, type NodeProps } from "@xyflow/react";

export type ProjectIo = {
  inputs?: string[];
  outputs?: string[];
};

export type ProjectNodeData = {
  kind: "start" | "agent" | "workflow";
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
};

export type ProjectFlowNode = Node<ProjectNodeData>;

export function ProjectNode({ id, data, selected }: NodeProps<ProjectFlowNode>) {
  const start = data.kind === "start";
  const inputs = data.io?.inputs ?? [];
  const outputs = data.io?.outputs ?? [];
  const linked = new Set(data.linkedOuts ?? []);
  return (
    <div
      data-testid={start ? "project-start-node" : "project-agent-node"}
      data-node-id={id}
      className={[
        "w-72 rounded-2xl border px-3 py-2 shadow-sm",
        start ? "border-indigo-300 bg-indigo-50 text-indigo-950" : "border-stone-200 bg-white text-stone-900",
        selected ? "ring-2 ring-indigo-600" : "",
      ].join(" ")}
    >
      {start ? null : (
        <Handle type="target" id="in" position={Position.Left} className="!bg-indigo-500" />
      )}
      <p className="text-[10px] font-medium uppercase tracking-wide text-stone-500">
        {start ? "Start" : "Agent"}
      </p>
      <p className="mt-0.5 text-sm font-semibold">{data.label}</p>
      {start ? (
        <dl className="mt-2 space-y-0.5 text-[11px] text-stone-600">
          {data.title ? (
            <div>
              <dt className="inline text-stone-400">Title </dt>
              <dd className="inline">{data.title}</dd>
            </div>
          ) : null}
          {data.brief ? <div className="line-clamp-3">{data.brief}</div> : null}
          {data.audience ? <div>Audience {data.audience}</div> : null}
          {data.duration || data.outlets || data.risk ? (
            <div>{[data.duration, data.outlets, data.risk].filter(Boolean).join(" · ")}</div>
          ) : null}
        </dl>
      ) : (
        <p className="mt-1 font-mono text-[11px] text-stone-500">{data.agent_id}</p>
      )}
      {inputs.length ? (
        <p className="mt-1 line-clamp-2 font-mono text-[10px] text-stone-500">in {inputs.join(" · ")}</p>
      ) : null}
      {data.reason ? <p className="mt-1 text-[11px] text-stone-500">{data.reason}</p> : null}
      <div className="mt-2 space-y-1">
        <p className="text-[10px] font-semibold uppercase tracking-wide text-stone-400">Out</p>
        {(outputs.length ? outputs : ["next"]).map((bus) => {
          const named = bus !== "next";
          const used = linked.has(bus);
          return (
            <div key={bus} className="relative flex items-center pr-2">
              <button
                type="button"
                className={[
                  "nodrag nopan flex min-w-0 flex-1 items-center justify-between gap-1 rounded-lg border px-2 py-1 text-left text-[11px]",
                  used
                    ? "border-indigo-400 bg-indigo-100 text-indigo-900"
                    : "border-stone-200 bg-white text-stone-700 hover:border-indigo-300 hover:bg-indigo-50",
                ].join(" ")}
                data-testid={named ? `project-out-${id}-${bus}` : `project-next-${id}`}
                title={named ? `Out ${bus} — suggest next agents` : "Suggest next agents"}
                onClick={(event) => {
                  event.stopPropagation();
                  data.onNext?.(id, named ? bus : undefined);
                }}
              >
                <span className="truncate font-mono">{named ? bus : "Next"}</span>
                <span className="flex shrink-0 items-center gap-1">
                  {used ? <span className="text-[9px] font-semibold uppercase">linked</span> : null}
                  <ArrowRight size={12} className="text-indigo-600" />
                </span>
              </button>
              <Handle
                type="source"
                id={named ? bus : "next"}
                position={Position.Right}
                className="!right-[-5px] !bg-indigo-500"
              />
            </div>
          );
        })}
        {outputs.length ? (
          <button
            type="button"
            className="nodrag nopan mt-1 inline-flex items-center gap-1 rounded-full border border-indigo-200 bg-white px-2 py-0.5 text-[10px] font-medium text-indigo-700 hover:bg-indigo-50"
            data-testid={`project-next-${id}`}
            title="Suggest next agents for every Out"
            onClick={(event) => {
              event.stopPropagation();
              data.onNext?.(id);
            }}
          >
            Next all
            <ArrowRight size={11} />
          </button>
        ) : null}
      </div>
    </div>
  );
}
