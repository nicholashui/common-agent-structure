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
import { ProjectNode, type ProjectFlowNode, type ProjectNodeData } from "../components/ProjectNode";
import type { ProjectCommItem, ProjectNextRow, ProjectNextSuggestion, ProjectRecord } from "../api/types";
import { AutoLayoutMenu } from "../components/GraphAutoLayout";
import {
  applyAutoLayout,
  DEFAULT_LAYOUT_ALGORITHM,
  type LayoutAlgorithm,
} from "../lib/autoLayout";
import { GRAPH_KIND, graphEdgeStyle, socketColor } from "../lib/graphStyle";
import { commIdForAgent, sortProjectComms } from "../lib/projectChat";
import { displayRelativePath } from "../lib/paths";
import { projectChatHref, rememberProject } from "../lib/projectContext";
import { applyLlmNext, createsCycle } from "../lib/projects";
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

function asNodes(graph: ProjectRecord["graph"]): Node<ProjectNodeData>[] {
  const raw = (graph?.nodes ?? []) as ProjectFlowNode[];
  return raw.map((node) => {
    const kind =
      node.data?.kind ||
      (node.id === "create-project"
        ? "start"
        : node.id === "output-prompt"
          ? "output"
          : node.id === "human-ask"
            ? "human"
            : "agent");
    return {
      ...node,
      type: kind === "start" || kind === "output" || kind === "human" ? kind : "agent",
      deletable: node.id === "create-project" || kind === "output" ? false : node.deletable,
      data: {
        ...node.data,
        kind,
        label:
          node.data?.label ??
          (kind === "start" ? "Create Project" : kind === "output" ? "Output" : kind === "human" ? "Human" : node.data?.agent_id ?? "Agent"),
      },
    };
  });
}

function asEdges(graph: ProjectRecord["graph"]): Edge[] {
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

export function ProjectFlowPage() {
  const session = useSession();
  const { theme } = useTheme();
  const dark = theme === "dark";
  const navigate = useNavigate();
  const params = useParams();
  const [searchParams] = useSearchParams();
  const projectId = params.projectId ? decodeURIComponent(params.projectId) : "";
  const focusComm = searchParams.get("comm") || "";
  const [record, setRecord] = useState<ProjectRecord | null>(null);
  const [nodes, setNodes] = useState<Node<ProjectNodeData>[]>([]);
  const [edges, setEdges] = useState<Edge[]>([]);
  const [error, setError] = useState<Error | null>(null);
  const [saving, setSaving] = useState(false);
  const [pending, setPending] = useState(false);
  const [consulting, setConsulting] = useState(false);
  const [fromId, setFromId] = useState("");
  const [outBus, setOutBus] = useState("");
  const [selected, setSelected] = useState<string[]>([]);
  const [suggestion, setSuggestion] = useState<ProjectNextSuggestion | null>(null);
  const canvasRef = useRef<HTMLDivElement>(null);
  const [canvasSize, setCanvasSize] = useState({ width: 0, height: 0 });
  const [flowSize, setFlowSize] = useState({ width: 0, height: 0 });
  const [comms, setComms] = useState<ProjectCommItem[]>([]);
  const [autoPilot, setAutoPilot] = useState(false);
  const orderedComms = useMemo(() => sortProjectComms(comms), [comms]);
  const [instruction, setInstruction] = useState("");
  const [launching, setLaunching] = useState(false);
  const [layoutNonce, setLayoutNonce] = useState(0);

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
    if (!projectId) {
      return;
    }
    rememberProject(projectId);
    session.client
      .getProject(projectId)
      .then((payload) => {
        setRecord(payload);
        setNodes(asNodes(payload.graph));
        setEdges(asEdges(payload.graph));
        if (!instruction) {
          setInstruction(payload.brief || payload.title || "");
        }
      })
      .catch((err) => setError(err instanceof Error ? err : new Error(String(err))));
    session.client
      .listProjectComms(projectId)
      .then((payload) => {
        setComms(payload.items ?? []);
        setAutoPilot(Boolean(payload.autopilot?.status || payload.walkthrough === "auto-pilot-v1"));
      })
      .catch(() => undefined);
  }, [projectId, session.client]);

  const onNodesChange = useCallback((changes: NodeChange[]) => {
    setNodes((current) =>
      applyNodeChanges(
        changes.filter((change) => !(change.type === "remove" && "id" in change && change.id === "create-project")),
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

  const handleNext = useCallback(
    async (nodeId: string, bus?: string) => {
      if (!projectId) {
        return;
      }
      const parent = nodes.find((node) => node.id === nodeId);
      setFromId(nodeId);
      setOutBus(bus || "");
      setSuggestion(null);
      setSelected([]);
      setError(null);
      setPending(true);
      try {
        const occupied = nodes.map((node) => node.data.agent_id).filter((id): id is string => Boolean(id));
        const next = await session.client.suggestProjectNext(projectId, {
          from_id: nodeId,
          from_agent_id: parent?.data.agent_id || undefined,
          occupied,
          out_bus: bus,
        });
        setSuggestion(next);
        const preselect = bus
          ? [next.primary].filter(Boolean)
          : next.suggestions
              .filter((row) => (next.outs ?? []).includes(row.id) && !row.loopback)
              .map((row) => row.id);
        setSelected(preselect.length ? preselect : next.primary ? [next.primary] : []);
        const prompt = next.prompt;
        const chatId = next.parent_chat_id || "video.planner";
        if (!prompt) {
          return;
        }
        setConsulting(true);
        const abort = typeof AbortSignal.timeout === "function" ? AbortSignal.timeout(12000) : undefined;
        void session.client
          .chatAgent(chatId, { message: prompt }, abort ? { signal: abort } : undefined)
          .then((chat) => {
            setSuggestion((current) => (current ? applyLlmNext(current, chat.reply || "") : current));
          })
          .catch(() => undefined)
          .finally(() => setConsulting(false));
      } catch (err) {
        setError(err instanceof Error ? err : new Error(String(err)));
      } finally {
        setPending(false);
      }
    },
    [nodes, projectId, session.client],
  );

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

  async function handleChoose(nodeId: string, optionId: string) {
    if (!projectId) {
      return;
    }
    const agentId = nodes.find((node) => node.id === nodeId)?.data.agent_id;
    if (!agentId) {
      return;
    }
    setLaunching(true);
    setError(null);
    try {
      const result = await session.client.runProject(projectId, { instruction, choices: { [agentId]: optionId } });
      if (result.graph) {
        setNodes(asNodes(result.graph));
        setEdges(asEdges(result.graph));
      }
      if (result.comms?.items) {
        setComms(result.comms.items);
      }
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setLaunching(false);
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
          onNext: autoPilot ? undefined : (id: string, bus?: string) => void handleNext(id, bus),
          onChoose: (id: string, optionId: string) => void handleChoose(id, optionId),
        },
      })),
    [nodes, handleNext, linkedBySource, autoPilot],
  );

  function openChatForNode(nodeId: string) {
    const node = nodes.find((item) => item.id === nodeId);
    if (!node) {
      return;
    }
    onNodeClick(undefined, node);
  }

  function onNodeClick(_event: unknown, node: Node<ProjectNodeData>) {
    if (!projectId) {
      return;
    }
    const kind = node.data?.kind;
    const agentId = String(node.data?.agent_id || "");
    if (kind === "start") {
      const first = orderedComms.find((item) => item.kind === "instruction" && item.from === "human_operator");
      navigate(projectChatHref(projectId, { comm: first?.id || "comm-0001" }));
      return;
    }
    if (kind === "output") {
      const output = [...orderedComms].reverse().find((item) => item.kind === "output" || item.kind === "assembled");
      navigate(projectChatHref(projectId, { comm: output?.id, agent: undefined }));
      return;
    }
    if (kind === "human") {
      const ask = [...orderedComms].reverse().find((item) => item.kind === "human_ask");
      navigate(projectChatHref(projectId, { comm: ask?.id }));
      return;
    }
    if (agentId) {
      const comm = commIdForAgent(orderedComms, agentId);
      navigate(projectChatHref(projectId, comm ? { comm } : { agent: agentId }));
    }
  }

  function addNext(rows: ProjectNextRow[]) {
    const parent = nodes.find((node) => node.id === fromId);
    const origin = parent?.position ?? { x: 80, y: 180 };
    const byAgent = new Map(
      nodes.filter((node) => node.data.agent_id).map((node) => [node.data.agent_id as string, node.id]),
    );
    let nextNodes = [...nodes];
    let nextEdges = [...edges];
    let created = 0;
    for (const row of rows) {
      const handle = row.contract?.[0] || row.id;
      const existingId = byAgent.get(row.id);
      if (existingId === fromId) {
        continue;
      }
      let targetId = existingId;
      if (!targetId) {
        targetId = `agent-${row.id.replace(/\./g, "-")}-${nextNodes.length + 1}`;
        nextNodes = [
          ...nextNodes,
          {
            id: targetId,
            type: "agent",
            position: {
              x: origin.x + 320,
              y: origin.y + (nextEdges.filter((edge) => edge.source === fromId).length + created) * 210,
            },
            data: {
              kind: "agent",
              label: row.label,
              agent_id: row.id,
              role: row.role,
              io: { inputs: row.inputs, outputs: row.outputs },
              contract: row.contract,
              reason: row.reason,
            },
          },
        ];
        byAgent.set(row.id, targetId);
        created += 1;
      }
      if (
        nextEdges.some(
          (edge) => edge.source === fromId && edge.target === targetId && String(edge.sourceHandle || "") === handle,
        )
      ) {
        continue;
      }
      const loop = createsCycle(nextEdges, fromId, targetId);
      nextEdges = addEdge(
        {
          id: `e-${fromId}-${targetId}-${handle}`,
          source: fromId,
          target: targetId,
          sourceHandle: handle,
          targetHandle: "in",
          ...graphEdgeStyle({ loop, handle }),
          label: loop ? `loop · ${handle}` : handle,
          data: { loop },
        },
        nextEdges,
      );
    }
    setNodes(nextNodes);
    setEdges(nextEdges);
    setSuggestion(null);
    setFromId("");
    setOutBus("");
    setSelected([]);
  }

  async function onLaunch() {
    if (!projectId) {
      return;
    }
    setLaunching(true);
    setError(null);
    try {
      const result = await session.client.runProject(projectId, { instruction });
      if (result.dry_run) {
        setError(
          new Error(
            `Dry-run is on. Uncheck Dry-run to write comms, graph, and output/${projectId}-prompt.txt.`,
          ),
        );
      }
      if (result.graph) {
        setNodes(asNodes(result.graph));
        setEdges(asEdges(result.graph));
      }
      if (result.comms?.items) {
        setComms(result.comms.items);
      }
      if (result.status === "needs_hitl") {
        setError(new Error("Agents generated ASK_HUMAN instructions. Open Chat and answer, then Launch again."));
      } else if (result.validation?.copied_sample) {
        setError(
          new Error(`Output matched sample/${projectId}-prompt.txt byte-for-byte — refused as a copy.`),
        );
      } else if (result.validation?.missing_markers?.length) {
        setError(
          new Error(
            "Generated prompt is live-assembled but missing: " + result.validation.missing_markers.join("; ") + ".",
          ),
        );
      }
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setLaunching(false);
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

  const onLayoutDefault = useCallback(
    (measured: Node<ProjectNodeData>[]) => {
      setNodes((current) =>
        applyAutoLayout(
          current.map((node) => {
            const hit = measured.find((item) => item.id === node.id);
            return hit?.measured ? { ...node, measured: hit.measured } : node;
          }),
          edges,
          {
            algorithm: DEFAULT_LAYOUT_ALGORITHM,
            rankGap: 112,
            packGap: 48,
            defaultWidth: 320,
            defaultHeight: 280,
          },
        ),
      );
      setLayoutNonce((current) => current + 1);
    },
    [edges],
  );

  async function onSave() {
    if (!record) {
      return;
    }
    setSaving(true);
    setError(null);
    try {
      const saved = await session.client.saveProject(record.id, {
        ...record,
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

  return (
    <div data-testid="project-flow">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <div>
          <h2 className="text-lg font-semibold text-stone-800">{record?.title ?? projectId}</h2>
          <p className="text-xs text-stone-500">
            {displayRelativePath(record?.folder) || `project/${projectId}`} · pack map {record?.sub_workflow_id ?? "—"} (not this
            project&apos;s creative lock) · CHARACTERIZATION
          </p>
        </div>
        <div className="flex gap-2">
          <DryRunControl />
          <AutoLayoutMenu testId="project-auto-layout" disabled={!nodes.length} onLayout={onAutoLayout} />
          <GhostButton type="button" onClick={() => navigate("/projects/new")}>
            New project
          </GhostButton>
          <PrimaryButton type="button" data-testid="project-save-graph" disabled={saving || !record} onClick={() => void onSave()}>
            {saving ? "Saving…" : "Save graph"}
          </PrimaryButton>
        </div>
      </div>
      <ErrorBanner error={error} />
      <div className="flex flex-col gap-3 lg:flex-row lg:items-stretch">
      <div className="flex min-h-0 flex-col gap-3 lg:h-[calc(100vh-14rem)] lg:w-80 lg:shrink-0">
      <ProjectCommsPanel
        projectId={projectId}
        items={orderedComms}
        focusId={focusComm}
        instruction={instruction}
        onInstruction={setInstruction}
        onLaunch={() => void onLaunch()}
        launching={launching}
      />
      {suggestion ? (
        <aside
          className="max-h-56 overflow-y-auto rounded-2xl border border-stone-200 bg-white p-4 lg:max-h-none lg:min-h-0 lg:flex-1"
          data-testid="project-next-suggestions"
        >
          <h3 className="text-sm font-semibold text-stone-900">
            Next from{" "}
            {fromId === "create-project"
              ? "Create Project"
              : nodes.find((node) => node.id === fromId)?.data.agent_id || fromId}
            {outBus ? ` · Out ${outBus}` : ""}
          </h3>
          <p className="mt-1 text-xs text-stone-500">
            {suggestion.note}{" "}
            {consulting
              ? `Consulting ${suggestion.parent_chat_id ?? "parent"}…`
              : suggestion.llm_used
                ? "Parent agent consulted."
                : pending
                  ? "Ranking…"
                  : "Declared I/O ranking — parent not consulted yet."}
          </p>
          <ul className="mt-3 space-y-2">
            {suggestion.suggestions.map((row) => (
              <li key={row.id}>
                <label className="flex cursor-pointer items-start gap-2 rounded-xl border border-stone-200 px-3 py-2 hover:bg-stone-50">
                  <input
                    type="checkbox"
                    name="project-next"
                    data-testid={`project-next-pick-${row.id}`}
                    checked={selected.includes(row.id)}
                    onChange={() => {
                      setSelected((current) =>
                        current.includes(row.id) ? current.filter((id) => id !== row.id) : [...current, row.id],
                      );
                    }}
                  />
                  <span>
                    <span className="block font-mono text-sm font-medium text-stone-800">{row.id}</span>
                    <span className="block text-[11px] text-stone-500">
                      in {row.inputs.join(" · ") || "—"} → out {row.outputs.join(" · ") || "—"}
                    </span>
                    <span className="block text-xs text-stone-500">{row.reason}</span>
                    {row.loopback ? (
                      <span className="mt-0.5 inline-block rounded-full bg-amber-100 px-1.5 py-0.5 text-[10px] font-semibold uppercase tracking-wide text-amber-800">
                        link back · loop
                      </span>
                    ) : null}
                  </span>
                </label>
              </li>
            ))}
          </ul>
          <div className="mt-3 flex gap-2">
            <PrimaryButton
              type="button"
              data-testid="project-next-add"
              disabled={!selected.length}
              onClick={() => {
                const rows = suggestion.suggestions.filter((item) => selected.includes(item.id));
                if (rows.length) {
                  addNext(rows);
                }
              }}
            >
              {selected.length > 1 ? `Add ${selected.length} next` : "Add next"}
            </PrimaryButton>
            <GhostButton type="button" onClick={() => setSuggestion(null)}>
              Cancel
            </GhostButton>
          </div>
        </aside>
      ) : null}
      </div>
      <div
        ref={canvasRef}
        className="casops-graph h-[28rem] min-h-[28rem] min-w-0 w-full overflow-hidden rounded-md border border-stone-200 dark:border-black lg:h-[calc(100vh-14rem)] lg:min-h-0 lg:flex-1"
        data-testid="project-canvas"
        data-graph-theme={theme}
      >
        {flowSize.width > 0 && flowSize.height > 0 && displayNodes.length ? (
          <ReactFlow
            key={`${projectId}-${flowSize.width}x${flowSize.height}-${theme}`}
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
              <AutoLayoutMenu testId="project-canvas-auto-layout" disabled={!nodes.length} onLayout={onAutoLayout} />
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
