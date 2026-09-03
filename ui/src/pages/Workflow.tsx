import { useEffect, useMemo, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { EmptyState, PageHeader, inputClass } from "../components/ui";
import { listAgentGroups } from "../lib/agents";
import { listSubWorkflows, subWorkflowSvgSrc, workflowSvgSrc } from "../lib/workflow";
import { useSession } from "../state/session";

const MIN_ZOOM = 1;
const MAX_ZOOM = 2.5;
const ZOOM_STEP = 0.25;
const zoomButtonClass =
  "inline-flex h-8 min-w-8 items-center justify-center rounded-lg border border-stone-200 bg-white px-2 text-xs font-semibold text-stone-700 shadow-sm transition hover:border-indigo-300 hover:bg-indigo-50 hover:text-indigo-700 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-indigo-500 disabled:cursor-not-allowed disabled:opacity-40";

function isAgentChatHref(href: string | null): href is string {
  return Boolean(href && href.startsWith("/agents/") && href.endsWith("/chat"));
}

function clampZoom(value: number): number {
  return Math.min(MAX_ZOOM, Math.max(MIN_ZOOM, value));
}

export function WorkflowPage({ kind = "main" }: { kind?: "main" | "sub" }) {
  const session = useSession();
  const navigate = useNavigate();
  const objectRef = useRef<HTMLObjectElement>(null);
  const groups = useMemo(() => listAgentGroups(session.agents), [session.agents]);
  const [group, setGroup] = useState<string>("");
  const [subId, setSubId] = useState<string>("");
  const [zoom, setZoom] = useState(MIN_ZOOM);
  const selected = groups.includes(group as (typeof groups)[number])
    ? (group as (typeof groups)[number])
    : groups.includes("video")
      ? "video"
      : groups[0];
  const subOptions = selected ? listSubWorkflows(selected) : [];
  const selectedSub = subOptions.find((item) => item.id === subId) ?? subOptions[0];
  const src =
    kind === "sub"
      ? selected
        ? subWorkflowSvgSrc(selected, selectedSub?.id)
        : null
      : selected
        ? workflowSvgSrc(selected)
        : null;
  const title = kind === "sub" ? "Sub Workflow" : "Main Workflow";
  const diagramLabel = kind === "sub" ? `${selectedSub?.label ?? selected} workflow` : `${selected} workflow`;

  useEffect(() => {
    if (!group && selected) {
      setGroup(selected);
    }
  }, [group, selected]);

  useEffect(() => {
    if (kind !== "sub") {
      return;
    }
    const options = selected ? listSubWorkflows(selected) : [];
    if (!options.length) {
      if (subId) {
        setSubId("");
      }
      return;
    }
    if (!options.some((item) => item.id === subId)) {
      setSubId(options[0].id);
    }
  }, [kind, selected, subId]);

  useEffect(() => {
    setZoom(MIN_ZOOM);
  }, [src]);

  useEffect(() => {
    const diagram = objectRef.current;
    if (!diagram || !src) {
      return;
    }
    const host: HTMLObjectElement = diagram;
    function bind(doc: Document) {
      const tagged = doc as Document & { __casopsAgentLinks?: boolean };
      if (tagged.__casopsAgentLinks) {
        return;
      }
      tagged.__casopsAgentLinks = true;
      doc.addEventListener("click", (event) => {
        const target = event.target as Element | null;
        const link = target?.closest("a.agent-link");
        const href = link?.getAttribute("href") ?? null;
        if (!isAgentChatHref(href)) {
          return;
        }
        event.preventDefault();
        navigate(href);
      });
    }
    function onLoad() {
      const doc = host.contentDocument;
      if (doc) {
        bind(doc);
      }
    }
    host.addEventListener("load", onLoad);
    if (host.contentDocument?.documentElement) {
      onLoad();
    }
    return () => host.removeEventListener("load", onLoad);
  }, [src, navigate]);

  function changeZoom(delta: number) {
    setZoom((current) => clampZoom(current + delta));
  }

  return (
    <div>
      <PageHeader
        title={title}
        actions={
          <>
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
            {kind === "sub" ? (
              <label className="flex min-w-[12rem] flex-col gap-1 text-xs font-medium text-stone-700">
                Sub Workflow
                <select
                  className={inputClass}
                  value={selectedSub?.id ?? ""}
                  onChange={(event) => setSubId(event.target.value)}
                  aria-label="Sub Workflow"
                  data-testid="sub-workflow-select"
                  disabled={!subOptions.length}
                >
                  {subOptions.length ? (
                    subOptions.map((item) => (
                      <option key={item.id} value={item.id}>
                        {item.label}
                      </option>
                    ))
                  ) : (
                    <option value="">No sub workflows</option>
                  )}
                </select>
              </label>
            ) : null}
          </>
        }
      />
      <p className="mb-4 text-sm text-stone-500">
        {kind === "sub"
          ? "Sub workflow diagram for the selected Agent Group. Click an agent id to open Agent Profile / Chat."
          : "Workflow diagram for the selected Agent Group. Click an agent id to open Agent Profile / Chat."}
      </p>
      {!session.agents.length ? (
        <EmptyState
          title="No agents"
          body="The control plane list is empty. Load the Agent Swarm before opening a workflow."
        />
      ) : src ? (
        <div
          className="flex h-[calc(100dvh-14rem)] min-h-[28rem] flex-col overflow-hidden rounded-2xl border border-stone-200 bg-[#f4f7fb] shadow-sm"
          data-testid={kind === "sub" ? "agent-sub-workflow" : "agent-workflow"}
        >
          <div className="z-10 flex min-h-11 shrink-0 flex-wrap items-center justify-between gap-2 border-b border-stone-200 bg-white/95 px-3 py-1.5 shadow-sm backdrop-blur">
            <div>
              <p className="text-xs font-semibold text-stone-800">Diagram view</p>
              <p className="hidden text-[11px] text-stone-500 sm:block">Fit for overview; zoom for readable detail.</p>
            </div>
            <div className="flex items-center gap-1.5" role="group" aria-label="Diagram zoom controls">
              <button
                type="button"
                className={zoomButtonClass}
                onClick={() => changeZoom(-ZOOM_STEP)}
                disabled={zoom <= MIN_ZOOM}
                aria-label="Zoom out diagram"
              >
                −
              </button>
              <button
                type="button"
                className={zoomButtonClass}
                onClick={() => setZoom(MIN_ZOOM)}
                aria-pressed={zoom === MIN_ZOOM}
              >
                Fit
              </button>
              <output className="min-w-12 text-center font-mono text-xs font-semibold text-stone-600" aria-live="polite">
                {Math.round(zoom * 100)}%
              </output>
              <button
                type="button"
                className={zoomButtonClass}
                onClick={() => changeZoom(ZOOM_STEP)}
                disabled={zoom >= MAX_ZOOM}
                aria-label="Zoom in diagram"
              >
                +
              </button>
            </div>
          </div>
          <div className="min-h-0 flex-1 overflow-auto overscroll-contain">
            <div className="min-w-full">
              <object
                key={src}
                ref={objectRef}
                data={src}
                type="image/svg+xml"
                className="block max-w-none"
                style={{ width: `${zoom * 100}%` }}
                aria-label={diagramLabel}
              >
                <img src={src} alt={diagramLabel} className="block h-auto w-full max-w-none" />
              </object>
            </div>
          </div>
        </div>
      ) : (
        <div data-testid={kind === "sub" ? "agent-sub-workflow" : "agent-workflow"}>
          <EmptyState
            title="No workflow diagram"
            body={`There is no ${kind === "sub" ? "sub workflow" : "workflow"} SVG for Agent Group “${selected ?? ""}”.`}
          />
        </div>
      )}
    </div>
  );
}
