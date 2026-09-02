import { useEffect, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  Background,
  BackgroundVariant,
  Controls,
  MiniMap,
  ReactFlow,
  type Node,
} from "@xyflow/react";
import "@xyflow/react/dist/style.css";
import { EmptyState, PageHeader, inputClass } from "../components/ui";
import { OrgNode, type OrgFlowNode } from "../components/OrgNode";
import { listAgentGroups } from "../lib/agents";
import { buildOrgChart, nodesForInitialFit, ORG_MIN_READABLE_ZOOM, type OrgEdgeDraft } from "../lib/orgChart";
import { agentHref } from "../shell/nav";
import { useSession } from "../state/session";

const nodeTypes = { orgNode: OrgNode };

function minimapColor(node: OrgFlowNode): string {
  if (node.data.kind === "group") {
    return "#4f46e5";
  }
  if (node.data.kind === "category") {
    return "#7c3aed";
  }
  return "#a8a29e";
}

export function OrgChatPage() {
  const session = useSession();
  const navigate = useNavigate();
  const groups = useMemo(() => listAgentGroups(session.agents), [session.agents]);
  const [group, setGroup] = useState<string>("");
  const selected = groups.includes(group as (typeof groups)[number])
    ? (group as (typeof groups)[number])
    : groups[0];

  useEffect(() => {
    if (!group && groups[0]) {
      setGroup(groups[0]);
    }
  }, [group, groups]);

  const graph = useMemo(
    () => (selected ? buildOrgChart(session.agents, selected) : { nodes: [], edges: [] as OrgEdgeDraft[] }),
    [session.agents, selected],
  );
  const fitNodes = useMemo(() => nodesForInitialFit(graph.nodes), [graph]);

  function onNodeClick(_event: unknown, node: Node) {
    const data = node.data as OrgFlowNode["data"];
    const agentId = typeof data.agentId === "string" ? data.agentId : "";
    if (data.kind === "agent" && agentId) {
      navigate(agentHref(agentId, ""));
    }
  }

  return (
    <div>
      <PageHeader
        title="Agent Org Chat"
        actions={
          <label className="flex min-w-[12rem] flex-col gap-1 text-xs font-medium text-stone-700">
            Agent Group
            <select
              className={`${inputClass} font-mono`}
              value={selected ?? ""}
              onChange={(event) => setGroup(event.target.value)}
              aria-label="Agent Group"
            >
              {groups.map((item) => (
                <option key={item} value={item}>
                  {item}
                </option>
              ))}
            </select>
          </label>
        }
      />
      <p className="mb-4 text-sm text-stone-500">
        Org chart of the selected Agent Group. Agents are grouped by category. Click an agent node to open it.
      </p>
      {!session.agents.length ? (
        <EmptyState
          title="No agents"
          body="The control plane list is empty. Load the Agent Swarm before opening the org chart."
        />
      ) : (
        <div
          className="h-[calc(100vh-14rem)] overflow-hidden rounded-2xl border border-stone-200 bg-stone-50"
          data-testid="org-chart"
        >
          <ReactFlow
            key={selected}
            nodes={graph.nodes as OrgFlowNode[]}
            edges={graph.edges}
            nodeTypes={nodeTypes}
            fitView
            fitViewOptions={{
              padding: 0.2,
              minZoom: ORG_MIN_READABLE_ZOOM,
              maxZoom: 1,
              nodes: fitNodes as OrgFlowNode[],
            }}
            minZoom={ORG_MIN_READABLE_ZOOM}
            nodesConnectable={false}
            nodesDraggable
            elementsSelectable
            panOnScroll
            onNodeClick={onNodeClick}
            defaultEdgeOptions={{ type: "smoothstep", style: { stroke: "#a8a29e" } }}
            proOptions={{ hideAttribution: false }}
          >
            <Background variant={BackgroundVariant.Dots} gap={18} color="#e7e5e4" />
            <Controls showInteractive={false} />
            <MiniMap
              pannable
              zoomable
              nodeColor={(node) => minimapColor(node as OrgFlowNode)}
              maskColor="rgba(250, 250, 249, 0.7)"
            />
          </ReactFlow>
        </div>
      )}
    </div>
  );
}
