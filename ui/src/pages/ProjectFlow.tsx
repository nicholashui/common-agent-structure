import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import {
  Background,
  BackgroundVariant,
  Controls,
  MiniMap,
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
import { ProjectNode, type ProjectFlowNode, type ProjectNodeData } from "../components/ProjectNode";
import type { ProjectNextRow, ProjectNextSuggestion, ProjectRecord } from "../api/types";
import { applyLlmNext } from "../lib/projects";
import { useSession } from "../state/session";

const nodeTypes = { start: ProjectNode, agent: ProjectNode, workflow: ProjectNode };

function FitOnResize({
  nodeCount,
  width,
  height,
}: {
  nodeCount: number;
  width: number;
  height: number;
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
  }, [fitView, nodeCount, ready, width, height]);
  return null;
}

function asNodes(graph: ProjectRecord["graph"]): Node<ProjectNodeData>[] {
  const raw = (graph?.nodes ?? []) as ProjectFlowNode[];
  return raw.map((node) => ({
    ...node,
    type: node.id === "create-project" || node.data?.kind === "start" ? "start" : "agent",
    deletable: node.id === "create-project" ? false : node.deletable,
    data: {
      ...node.data,
      kind: node.id === "create-project" || node.data?.kind === "start" ? "start" : "agent",
      label: node.data?.label ?? (node.id === "create-project" ? "Create Project" : node.data?.agent_id ?? "Agent"),
    },
  }));
}

function asEdges(graph: ProjectRecord["graph"]): Edge[] {
  return (graph?.edges ?? []) as Edge[];
}

function persistable(nodes: Node<ProjectNodeData>[], edges: Edge[]) {
  return {
    nodes: nodes.map((node) => {
      const { onNext: _onNext, linkedOuts: _linked, ...data } = node.data;
      return { ...node, data };
    }),
    edges,
  };
}

export function ProjectFlowPage() {
  const session = useSession();
  const navigate = useNavigate();
  const params = useParams();
  const projectId = params.projectId ? decodeURIComponent(params.projectId) : "";
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

  useEffect(() => {
    const el = canvasRef.current;
    if (!el) {
      return;
    }
    const update = () => {
      const width = el.clientWidth;
      const height = el.clientHeight;
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
    session.client
      .getProject(projectId)
      .then((payload) => {
        setRecord(payload);
        setNodes(asNodes(payload.graph));
        setEdges(asEdges(payload.graph));
      })
      .catch((err) => setError(err instanceof Error ? err : new Error(String(err))));
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
        { ...connection, type: "smoothstep", targetHandle: connection.targetHandle || "in" },
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
              .filter((row) => (next.outs ?? []).includes(row.id))
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

  const displayNodes = useMemo(
    () =>
      nodes.map((node) => ({
        ...node,
        data: {
          ...node.data,
          linkedOuts: linkedBySource.get(node.id) ?? [],
          onNext: (id: string, bus?: string) => void handleNext(id, bus),
        },
      })),
    [nodes, handleNext, linkedBySource],
  );

  function addNext(rows: ProjectNextRow[]) {
    const parent = nodes.find((node) => node.id === fromId);
    const origin = parent?.position ?? { x: 80, y: 180 };
    const already = new Set(nodes.map((node) => node.data.agent_id).filter(Boolean));
    const unique = rows.filter((row) => !already.has(row.id));
    if (!unique.length) {
      setSuggestion(null);
      setFromId("");
      setOutBus("");
      return;
    }
    setNodes((current) => {
      const nextNodes = [...current];
      unique.forEach((row, index) => {
        nextNodes.push({
          id: `agent-${row.id.replace(/\./g, "-")}-${current.length + index + 1}`,
          type: "agent",
          position: { x: origin.x + 320, y: origin.y + (edges.filter((edge) => edge.source === fromId).length + index) * 210 },
          data: {
            kind: "agent",
            label: row.label,
            agent_id: row.id,
            role: row.role,
            io: { inputs: row.inputs, outputs: row.outputs },
            contract: row.contract,
            reason: row.reason,
          },
        });
      });
      return nextNodes;
    });
    setEdges((current) => {
      let nextEdges = current;
      unique.forEach((row, index) => {
        const id = `agent-${row.id.replace(/\./g, "-")}-${nodes.length + index + 1}`;
        const handle = row.contract?.[0] || row.id;
        nextEdges = addEdge(
          {
            id: `e-${fromId}-${id}`,
            source: fromId,
            target: id,
            sourceHandle: handle,
            targetHandle: "in",
            type: "smoothstep",
            label: handle,
          },
          nextEdges,
        );
      });
      return nextEdges;
    });
    setSuggestion(null);
    setFromId("");
    setOutBus("");
    setSelected([]);
  }

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
            {record?.folder ?? `project/${projectId}`} · one workflow · {record?.sub_workflow_id ?? "—"} · CHARACTERIZATION
          </p>
        </div>
        <div className="flex gap-2">
          <DryRunControl />
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
      {suggestion ? (
        <aside
          className="max-h-64 overflow-y-auto rounded-2xl border border-stone-200 bg-white p-4 lg:max-h-none lg:h-[calc(100vh-14rem)] lg:w-80 lg:shrink-0"
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
      <div
        ref={canvasRef}
        className="h-72 min-w-0 w-full flex-1 overflow-hidden rounded-2xl border border-stone-200 bg-stone-50 lg:h-[calc(100vh-14rem)] lg:min-h-0"
        data-testid="project-canvas"
      >
        {flowSize.width > 0 && flowSize.height > 0 && displayNodes.length ? (
          <ReactFlow
            key={`${flowSize.width}x${flowSize.height}`}
            nodes={displayNodes}
            edges={edges}
            nodeTypes={nodeTypes}
            onNodesChange={onNodesChange}
            onEdgesChange={onEdgesChange}
            onConnect={onConnect}
            fitView
            panOnScroll
            width={flowSize.width}
            height={flowSize.height}
            deleteKeyCode={["Backspace", "Delete"]}
            defaultEdgeOptions={{ type: "smoothstep", style: { stroke: "#a8a29e" } }}
          >
            <FitOnResize nodeCount={displayNodes.length} width={flowSize.width} height={flowSize.height} />
            <Background variant={BackgroundVariant.Dots} gap={18} color="#e7e5e4" />
            <Controls />
            {flowSize.width >= 640 ? (
              <MiniMap
                pannable
                zoomable
                nodeColor={(node) => ((node.data as ProjectNodeData | undefined)?.kind === "start" ? "#6366f1" : "#a8a29e")}
                maskColor="rgba(250, 250, 249, 0.7)"
              />
            ) : null}
          </ReactFlow>
        ) : (
          <div className="flex h-full items-center justify-center text-xs text-stone-400">Loading graph…</div>
        )}
      </div>
      </div>
    </div>
  );
}
