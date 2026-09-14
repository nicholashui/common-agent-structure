import { useEffect, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  Background,
  BackgroundVariant,
  Controls,
  ConnectionLineType,
  MiniMap,
  ReactFlow,
  type Node,
} from "@xyflow/react";
import "@xyflow/react/dist/style.css";
import { EmptyState, PageHeader, inputClass } from "../components/ui";
import { OrgNode, type OrgFlowNode } from "../components/OrgNode";
import { listAgentGroups } from "../lib/agents";
import { GRAPH_KIND, socketColor } from "../lib/graphStyle";
import { buildOrgChart, nodesForInitialFit, ORG_MIN_READABLE_ZOOM, type OrgEdgeDraft } from "../lib/orgChart";
import { lastProjectId, projectChatHref } from "../lib/projectContext";
import { filterByRoster, useSwarmRoster } from "../lib/swarmFilter";
import { agentHref } from "../shell/nav";
import { useSession } from "../state/session";
import { useTheme } from "../theme/ThemeProvider";

const nodeTypes = { orgNode: OrgNode };

function minimapColor(node: OrgFlowNode): string {
  return GRAPH_KIND[node.data.kind].mini;
}

export function OrgChatPage() {
  const session = useSession();
  const { theme } = useTheme();
  const dark = theme === "dark";
  const navigate = useNavigate();
  const { swarmId, roster } = useSwarmRoster();
  const agents = useMemo(() => filterByRoster(session.agents, roster), [session.agents, roster]);
  const groups = useMemo(() => listAgentGroups(agents), [agents]);
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
    () => (selected ? buildOrgChart(agents, selected) : { nodes: [], edges: [] as OrgEdgeDraft[] }),
    [agents, selected],
  );
  const fitNodes = useMemo(() => nodesForInitialFit(graph.nodes), [graph]);

  function onNodeClick(_event: unknown, node: Node) {
    const data = node.data as OrgFlowNode["data"];
    const agentId = typeof data.agentId === "string" ? data.agentId : "";
    if (data.kind !== "agent" || !agentId) {
      return;
    }
    const projectId = lastProjectId();
    if (projectId) {
      navigate(projectChatHref(projectId, { agent: agentId }));
      return;
    }
    navigate(agentHref(agentId, ""));
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
        Org chart of the selected Agent Group (pack browser, not a swarm runner
        {swarmId ? ` · roster ${swarmId}` : ""}). Click an agent: Project Chat hop if a project is in context, otherwise
        Agent Profile.
      </p>
      {!session.agents.length ? (
        <EmptyState
          title="No agents"
          body="The control plane list is empty. Load the Agent Swarm before opening the org chart."
        />
      ) : (
        <div
          className="casops-graph h-[calc(100vh-14rem)] overflow-hidden rounded-md border border-stone-200 dark:border-black"
          data-testid="org-chart"
          data-graph-theme={theme}
        >
          <ReactFlow
            key={`${selected}-${theme}`}
            className="casops-graph"
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
            colorMode={theme}
            connectionLineType={ConnectionLineType.Bezier}
            onNodeClick={onNodeClick}
            defaultEdgeOptions={{ type: "default", style: { stroke: socketColor("org"), strokeWidth: 2.4 } }}
            proOptions={{ hideAttribution: true }}
          >
            <Background variant={BackgroundVariant.Dots} gap={20} size={1.2} color={dark ? "#3a3a3a" : "#d6d3d1"} />
            <Controls showInteractive={false} />
            <MiniMap
              pannable
              zoomable
              nodeColor={(node) => minimapColor(node as OrgFlowNode)}
              maskColor={dark ? "rgba(12, 12, 12, 0.55)" : "rgba(250, 250, 249, 0.7)"}
              bgColor={dark ? "#252525" : "#f5f5f4"}
            />
          </ReactFlow>
        </div>
      )}
    </div>
  );
}
