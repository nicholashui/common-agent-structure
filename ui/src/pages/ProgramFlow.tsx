import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { useNavigate, useParams, useSearchParams } from "react-router-dom";
import {
  Background,
  BackgroundVariant,
  Controls,
  ConnectionLineType,
  MiniMap,
  Panel,
  ReactFlow,
  addEdge,
  applyEdgeChanges,
  applyNodeChanges,
  useNodesInitialized,
  useReactFlow,
  type Connection,
  type Edge,
  type EdgeChange,
  type Node,
  type NodeChange,
} from "@xyflow/react";
import "@xyflow/react/dist/style.css";
import { GhostButton, PrimaryButton } from "../components/ui";
import { DryRunControl } from "../components/ActorStrip";
import { ErrorBanner } from "../components/RecoveryBanner";
import { ProjectCommsPanel } from "../components/ProjectComms";
import { ProjectNode, type ProjectNodeData } from "../components/ProjectNode";
import type { ProgramCommItem, ProgramRecord, ProjectCommItem } from "../api/types";
import { AutoLayoutMenu } from "../components/GraphAutoLayout";
import { applyAutoLayout, DEFAULT_LAYOUT_ALGORITHM, type LayoutAlgorithm } from "../lib/autoLayout";
import { GRAPH_KIND, graphEdgeStyle, socketColor } from "../lib/graphStyle";
import { commIdForAgent, sortProjectComms } from "../lib/projectChat";
import { displayRelativePath } from "../lib/paths";
import { useSession } from "../state/session";
import { useTheme } from "../theme/ThemeProvider";

const nodeTypes = { start: ProjectNode, agent: ProjectNode, workflow: ProjectNode, output: ProjectNode, human: ProjectNode };

function LayoutDefault({
  onLayout,
}: {
  onLayout: (measured: Node<ProjectNodeData>[]) => void;
}) {
  const ready = useNodesInitialized();
  const { getNodes } = useReactFlow();
  const ran = useRef(false);
  useEffect(() => {
    if (!ready || ran.current) {
      return;
    }
    const measured = getNodes() as Node<ProjectNodeData>[];
    if (!measured.length) {
      return;
    }
    ran.current = true;
    onLayout(measured);
  }, [ready, getNodes, onLayout]);
  return null;
}

function FitOnResize({
  nodeCount,
  width,
  height,
  nonce,
}: {
  nodeCount: number;
  width: number;
  height: number;
  nonce: number;
}) {
  const { fitView } = useReactFlow();
  const ready = useNodesInitialized();
  useEffect(() => {
    if (!nodeCount || !ready || width <= 0 || height <= 0) {
      return;
    }
    const frame = window.requestAnimationFrame(() => fitView({ padding: 0.2 }));
    const later = window.setTimeout(() => fitView({ padding: 0.2 }), 50);
    return () => {
      window.cancelAnimationFrame(frame);
      window.clearTimeout(later);
    };
  }, [fitView, nodeCount, ready, width, height, nonce]);
  return null;
}

function asNodes(graph: ProgramRecord["graph"]): Node<ProjectNodeData>[] {
  const raw = (graph?.nodes ?? []) as Node<ProjectNodeData>[];
  return raw.map((node) => {
    const kind =
      node.data?.kind ||
      (node.id === "create-program"
        ? "start"
        : node.id === "output-prompt"
          ? "output"
          : node.id === "human-ask" || node.id === "human_operator"
            ? "human"
            : "agent");
    return {
      ...node,
      type: kind === "start" || kind === "output" || kind === "human" ? kind : "agent",
      deletable: node.id === "create-program" || kind === "output" ? false : node.deletable,
      data: {
        ...node.data,
        kind,
        label:
          node.data?.label ??
          (kind === "start" ? "Create Program" : kind === "output" ? "Output" : kind === "human" ? "Human" : node.data?.agent_id ?? node.id),
      },
    };
  });
}

function asEdges(graph: ProgramRecord["graph"]): Edge[] {
  return ((graph?.edges ?? []) as Edge[]).map((edge) => {
    const loop = Boolean((edge.data as { loop?: boolean } | undefined)?.loop);
    return {
      ...edge,
      ...graphEdgeStyle({ loop, handle: String(edge.sourceHandle || "next") }),
      label: edge.label,
      data: edge.data,
    };
  });
}

function persistable(nodes: Node<ProjectNodeData>[], edges: Edge[]) {
  return {
    nodes: nodes.map((node) => {
      const { onNext: _onNext, onChoose: _onChoose, onOpenChat: _onOpen, linkedOuts: _linked, ...data } = node.data;
      return { ...node, data };
    }),
    edges,
  };
}

function asProjectComms(items: ProgramCommItem[]): ProjectCommItem[] {
  return items.map((item) => ({
    id: item.id,
    node_id: item.from,
    from: item.from,
    to: item.to,
    kind: item.kind,
    text: item.text || "",
    input_tags: [],
    output_tags: [],
    pass_id: item.pass_id,
    created_at: item.created_at,
    live: item.live,
  }));
}

export function ProgramFlowPage() {
  const session = useSession();
  const { theme } = useTheme();
  const dark = theme === "dark";
  const navigate = useNavigate();
  const params = useParams();
  const [searchParams] = useSearchParams();
  const programId = params.programId ? decodeURIComponent(params.programId) : "";
  const focusComm = searchParams.get("comm") || "";
  const [record, setRecord] = useState<ProgramRecord | null>(null);
  const [nodes, setNodes] = useState<Node<ProjectNodeData>[]>([]);
  const [edges, setEdges] = useState<Edge[]>([]);
  const [error, setError] = useState<Error | null>(null);
  const [saving, setSaving] = useState(false);
  const [comms, setComms] = useState<ProjectCommItem[]>([]);
  const [instruction, setInstruction] = useState("");
  const [launching, setLaunching] = useState(false);
  const [layoutNonce, setLayoutNonce] = useState(0);
  const canvasRef = useRef<HTMLDivElement>(null);
  const [canvasSize, setCanvasSize] = useState({ width: 0, height: 0 });
  const [flowSize, setFlowSize] = useState({ width: 0, height: 0 });
  const orderedComms = useMemo(() => sortProjectComms(comms), [comms]);

  useEffect(() => {
    const el = canvasRef.current;
    if (!el) {
      return;
    }
    const update = () => {
      const width = el.clientWidth;
      const height = el.clientHeight || 288;
      setCanvasSize((current) =>
        current.width === width && current.height === height ? current : { width, height },
      );
    };
    update();
    const observer = new ResizeObserver(update);
    observer.observe(el);
    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    const timer = window.setTimeout(() => setFlowSize(canvasSize), 80);
    return () => window.clearTimeout(timer);
  }, [canvasSize]);

  useEffect(() => {
    if (!programId) {
      return;
    }
    session.client
      .getProgram(programId)
      .then((payload) => {
        setRecord(payload);
        setNodes(asNodes(payload.graph));
        setEdges(asEdges(payload.graph));
        if (!instruction) {
          setInstruction(payload.name || "");
        }
      })
      .catch((err) => setError(err instanceof Error ? err : new Error(String(err))));
    session.client
      .listProgramComms(programId)
      .then((payload) => {
        setComms(asProjectComms(payload.items ?? []));
        if (payload.graph?.nodes?.length && !nodes.length) {
          setNodes(asNodes(payload.graph));
          setEdges(asEdges(payload.graph));
        }
      })
      .catch(() => undefined);
  }, [programId, session.client]);

  const onNodesChange = useCallback((changes: NodeChange[]) => {
    setNodes((current) =>
      applyNodeChanges(
        changes.filter((change) => !(change.type === "remove" && "id" in change && change.id === "create-program")),
        current,
      ) as Node<ProjectNodeData>[],
    );
  }, []);
  const onEdgesChange = useCallback((changes: EdgeChange[]) => {
    setEdges((current) => applyEdgeChanges(changes, current));
  }, []);
  const onConnect = useCallback((connection: Connection) => {
    setEdges((current) =>
      addEdge(
        {
          ...connection,
          ...graphEdgeStyle({ handle: String(connection.sourceHandle || "next") }),
          targetHandle: connection.targetHandle || "in",
        },
        current,
      ),
    );
  }, []);

  const linkedBySource = useMemo(() => {
    const map = new Map<string, string[]>();
    for (const edge of edges) {
      const handle = String(edge.sourceHandle || "");
      if (!handle) {
        continue;
      }
      const current = map.get(edge.source) ?? [];
      if (!current.includes(handle)) {
        current.push(handle);
      }
      map.set(edge.source, current);
    }
    return map;
  }, [edges]);

  function onNodeClick(_event: unknown, node: Node<ProjectNodeData>) {
    if (!programId) {
      return;
    }
    const kind = node.data?.kind;
    const agentId = String(node.data?.agent_id || node.id || "");
    const chat = `/programs/${encodeURIComponent(programId)}/chat`;
    if (kind === "start") {
      const first = orderedComms.find((item) => item.kind === "instruction" && item.from === "create-program");
      navigate(`${chat}?comm=${encodeURIComponent(first?.id || "comm-0001")}`);
      return;
    }
    if (kind === "output") {
      const output = [...orderedComms].reverse().find((item) => item.kind === "output" || item.kind === "assembled");
      navigate(output?.id ? `${chat}?comm=${encodeURIComponent(output.id)}` : chat);
      return;
    }
    if (kind === "human") {
      const ask = [...orderedComms].reverse().find((item) => item.kind === "human_ask");
      navigate(ask?.id ? `${chat}?comm=${encodeURIComponent(ask.id)}` : chat);
      return;
    }
    if (agentId) {
      const comm = commIdForAgent(orderedComms, agentId);
      navigate(comm ? `${chat}?comm=${encodeURIComponent(comm)}` : `${chat}?agent=${encodeURIComponent(agentId)}`);
    }
  }

  function openChatForNode(nodeId: string) {
    const node = nodes.find((item) => item.id === nodeId);
    if (node) {
      onNodeClick(undefined, node);
    }
  }

  const displayNodes = useMemo(
    () =>
      nodes.map((node) => ({
        ...node,
        data: {
          ...node.data,
          linkedOuts: linkedBySource.get(node.id) ?? [],
          onOpenChat: (id: string) => openChatForNode(id),
        },
      })),
    [nodes, linkedBySource],
  );

  async function onLaunch() {
    if (!programId) {
      return;
    }
    setLaunching(true);
    setError(null);
    try {
      const stamped = await session.client.stampProgramComms(programId);
      const hops = asProjectComms(stamped.items ?? []);
      setComms(hops);
      if (stamped.graph) {
        setNodes(asNodes(stamped.graph));
        setEdges(asEdges(stamped.graph));
      }
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setLaunching(false);
    }
  }

  async function onSave() {
    if (!record) {
      return;
    }
    setSaving(true);
    setError(null);
    try {
      const saved = await session.client.saveProgram(record.id, {
        name: record.name,
        graph: persistable(nodes, edges),
      });
      setRecord(saved);
      if (saved.dry_run) {
        setError(new Error("Dry-run is on. Uncheck Dry-run in the header to write the graph."));
      }
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setSaving(false);
    }
  }

  function onAutoLayout(algorithm: LayoutAlgorithm = DEFAULT_LAYOUT_ALGORITHM) {
    setNodes((current) =>
      applyAutoLayout(current, edges, {
        algorithm,
        rankGap: 112,
        packGap: 48,
        defaultWidth: 320,
        defaultHeight: 280,
      }),
    );
    setLayoutNonce((current) => current + 1);
  }

  const onLayoutDefault = useCallback((measured: Node<ProjectNodeData>[]) => {
    setNodes((current) =>
      applyAutoLayout(
        current.map((node) => {
          const hit = measured.find((item) => item.id === node.id);
          return hit?.measured ? { ...node, measured: hit.measured } : node;
        }),
        edges,
        { algorithm: DEFAULT_LAYOUT_ALGORITHM, rankGap: 112, packGap: 48, defaultWidth: 320, defaultHeight: 280 },
      ),
    );
    setLayoutNonce((current) => current + 1);
  }, [edges]);

  const chatBase = `/programs/${encodeURIComponent(programId)}/chat`;
  const workflowHref = `/programs/${encodeURIComponent(programId)}/workflow`;

  return (
    <div data-testid="program-flow">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <div>
          <h2 className="text-lg font-semibold text-stone-800">{record?.name ?? programId}</h2>
          <p className="text-xs text-stone-500">
            {displayRelativePath(record?.folder) || `program/${programId}`} · Create Program → intent-analysis →
            showrunner · CHARACTERIZATION
          </p>
        </div>
        <div className="flex gap-2">
          <DryRunControl />
          <AutoLayoutMenu testId="program-auto-layout" disabled={!nodes.length} onLayout={onAutoLayout} />
          <GhostButton type="button" onClick={() => navigate("/programs/new")}>
            New program
          </GhostButton>
          <PrimaryButton type="button" data-testid="program-save-graph" disabled={saving || !record} onClick={() => void onSave()}>
            {saving ? "Saving…" : "Save graph"}
          </PrimaryButton>
        </div>
      </div>
      <ErrorBanner error={error} />
      <div className="flex flex-col gap-3 lg:flex-row lg:items-stretch">
        <div className="flex min-h-0 flex-col gap-3 lg:h-[calc(100vh-14rem)] lg:w-80 lg:shrink-0">
          <ProjectCommsPanel
            projectId={programId}
            items={orderedComms}
            focusId={focusComm}
            instruction={instruction}
            onInstruction={setInstruction}
            onLaunch={() => void onLaunch()}
            launching={launching}
            chatBase={chatBase}
            workflowHref={workflowHref}
            launchLabel="Launch workflow"
            hint="Auto Pilot: Create Program is the draft only. intent-analysis-agent then showrunner. Same canvas logic as Project Workflow."
          />
        </div>
        <div
          ref={canvasRef}
          className="casops-graph h-[28rem] min-h-[28rem] min-w-0 w-full overflow-hidden rounded-md border border-stone-200 dark:border-black lg:h-[calc(100vh-14rem)] lg:min-h-0 lg:flex-1"
          data-testid="program-canvas"
          data-graph-theme={theme}
        >
          {flowSize.width > 0 && flowSize.height > 0 && displayNodes.length ? (
            <ReactFlow
              key={`${programId}-${flowSize.width}x${flowSize.height}-${theme}`}
              className="casops-graph"
              nodes={displayNodes}
              edges={edges}
              nodeTypes={nodeTypes}
              onNodesChange={onNodesChange}
              onEdgesChange={onEdgesChange}
              onConnect={onConnect}
              onNodeClick={onNodeClick}
              fitView
              panOnScroll
              colorMode={theme}
              connectionLineType={ConnectionLineType.Bezier}
              width={flowSize.width}
              height={flowSize.height}
              deleteKeyCode={["Backspace", "Delete"]}
              defaultEdgeOptions={{ type: "default", style: { stroke: socketColor("next"), strokeWidth: 2.4 } }}
              proOptions={{ hideAttribution: true }}
            >
              <LayoutDefault onLayout={onLayoutDefault} />
              <FitOnResize
                nodeCount={displayNodes.length}
                width={flowSize.width}
                height={flowSize.height}
                nonce={layoutNonce}
              />
              <Background variant={BackgroundVariant.Dots} gap={20} size={1.2} color={dark ? "#3a3a3a" : "#d6d3d1"} />
              <Controls />
              <Panel position="top-right" className="m-2 hidden md:block">
                <AutoLayoutMenu testId="program-canvas-auto-layout" disabled={!nodes.length} onLayout={onAutoLayout} />
              </Panel>
              {flowSize.width >= 640 ? (
                <MiniMap
                  pannable
                  zoomable
                  nodeColor={(node) => {
                    const kind = (node.data as ProjectNodeData | undefined)?.kind;
                    if (kind === "start") {
                      return GRAPH_KIND.start.mini;
                    }
                    if (kind === "output") {
                      return GRAPH_KIND.output.mini;
                    }
                    if (kind === "human") {
                      return GRAPH_KIND.human.mini;
                    }
                    return GRAPH_KIND.agent.mini;
                  }}
                  maskColor={dark ? "rgba(12, 12, 12, 0.55)" : "rgba(250, 250, 249, 0.7)"}
                  bgColor={dark ? "#252525" : "#f5f5f4"}
                />
              ) : null}
            </ReactFlow>
          ) : (
            <div className="flex h-full items-center justify-center text-xs text-[#777]">Loading graph…</div>
          )}
        </div>
      </div>
    </div>
  );
}
