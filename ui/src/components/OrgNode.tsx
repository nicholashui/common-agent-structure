import { Handle, Position, type Node, type NodeProps } from "@xyflow/react";
import { ORG_NODE_WIDTH, type OrgNodeData } from "../lib/orgChart";

export type OrgFlowNode = Node<OrgNodeData, "orgNode">;

const KIND_CLASS: Record<OrgNodeData["kind"], string> = {
  group:
    "border-indigo-200 bg-indigo-50 text-indigo-900",
  category:
    "border-violet-200 bg-white text-stone-900",
  agent:
    "border-stone-200 bg-white text-stone-900 hover:border-indigo-300 hover:shadow-md",
};

export function OrgNode({ data, selected }: NodeProps<OrgFlowNode>) {
  const clickable = data.kind === "agent" && Boolean(data.agentId);
  return (
    <div
      style={{ width: ORG_NODE_WIDTH }}
      className={[
        "rounded-2xl border px-3 py-2 shadow-sm",
        KIND_CLASS[data.kind],
        selected ? "ring-2 ring-indigo-600" : "",
        clickable ? "cursor-pointer" : "",
      ].join(" ")}
    >
      {data.kind !== "group" ? (
        <Handle type="target" position={Position.Top} isConnectable={false} className="!bg-indigo-500" />
      ) : null}
      <p className="truncate text-[10px] font-medium uppercase tracking-wide text-stone-500">
        {data.kind === "group" ? "Agent Group" : data.kind}
        {typeof data.count === "number" ? ` · ${data.count}` : ""}
      </p>
      <p className={`mt-0.5 truncate text-sm font-semibold ${data.kind === "agent" ? "font-mono" : ""}`}>
        {data.label}
      </p>
      {data.subtitle ? <p className="mt-0.5 truncate text-xs text-stone-500">{data.subtitle}</p> : null}
      {data.kind !== "agent" ? (
        <Handle type="source" position={Position.Bottom} isConnectable={false} className="!bg-indigo-500" />
      ) : null}
    </div>
  );
}
