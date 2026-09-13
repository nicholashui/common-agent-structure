import { Handle, Position, type Node, type NodeProps } from "@xyflow/react";
import { GRAPH_KIND, socketColor } from "../lib/graphStyle";
import { ORG_NODE_WIDTH, type OrgNodeData } from "../lib/orgChart";

export type OrgFlowNode = Node<OrgNodeData, "orgNode">;

export function OrgNode({ data, selected }: NodeProps<OrgFlowNode>) {
  const clickable = data.kind === "agent" && Boolean(data.agentId);
  const chrome = GRAPH_KIND[data.kind];
  return (
    <div
      style={{ width: ORG_NODE_WIDTH }}
      className={[
        "casops-node overflow-hidden rounded-md border",
        selected ? "ring-1 ring-stone-900 dark:ring-white" : "",
        clickable ? "cursor-pointer" : "",
      ].join(" ")}
    >
      {data.kind !== "group" ? (
        <Handle
          type="target"
          position={Position.Top}
          isConnectable={false}
          className="!top-[-6px]"
          style={{ background: socketColor(data.kind) }}
        />
      ) : null}
      <div
        className="flex h-6 items-center justify-between gap-1 px-2 text-[10px] font-semibold uppercase tracking-wide text-white"
        style={{ background: chrome.title }}
      >
        <span className="truncate">{chrome.label}</span>
        {typeof data.count === "number" ? <span className="opacity-80">{data.count}</span> : null}
      </div>
      <div className="px-2 py-1">
        <p className={`truncate text-xs font-semibold text-stone-800 dark:text-[#eee] ${data.kind === "agent" ? "font-mono" : ""}`}>
          {data.label}
        </p>
        {data.subtitle ? <p className="mt-0.5 truncate text-[11px] text-stone-500 dark:text-[#aaa]">{data.subtitle}</p> : null}
      </div>
      {data.kind !== "agent" ? (
        <Handle
          type="source"
          position={Position.Bottom}
          isConnectable={false}
          className="!bottom-[-6px]"
          style={{ background: socketColor(`${data.kind}-out`) }}
        />
      ) : null}
    </div>
  );
}
