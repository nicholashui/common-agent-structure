import { useEffect, useMemo, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { AutoLayoutButton } from "../components/GraphAutoLayout";
import { EmptyState, PageHeader, inputClass } from "../components/ui";
import { listAgentGroups } from "../lib/agents";
import { applySvgTheme } from "../lib/graphStyle";
import { listSubWorkflows, subWorkflowSvgSrc, workflowSvgSrc } from "../lib/workflow";
import { agentIdFromProfileChatHref, lastProjectId, projectChatHref } from "../lib/projectContext";
import { useSwarmRoster } from "../lib/swarmFilter";
import { useSession } from "../state/session";
import { useTheme } from "../theme/ThemeProvider";

const MIN_ZOOM = 1;
const MAX_ZOOM = 2.5;
const ZOOM_STEP = 0.25;
const zoomButtonClass =
  "inline-flex h-8 min-w-8 items-center justify-center rounded border border-stone-200 bg-white px-2 text-xs font-semibold text-stone-700 shadow-sm transition hover:border-indigo-300 hover:bg-indigo-50 hover:text-indigo-700 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-indigo-500 disabled:cursor-not-allowed disabled:opacity-40 dark:border-[#111] dark:bg-[#353535] dark:text-[#ddd] dark:hover:border-[#64b5f6] dark:hover:bg-[#454545] dark:hover:text-white dark:focus-visible:ring-[#64b5f6]";

function isAgentChatHref(href: string | null): href is string {
  return Boolean(href && href.startsWith("/agents/") && href.endsWith("/chat"));
}

function clampZoom(value: number): number {
  return Math.min(MAX_ZOOM, Math.max(MIN_ZOOM, value));
}

export function WorkflowPage({ kind = "main" }: { kind?: "main" | "sub" }) {
  const session = useSession();
  const { theme } = useTheme();
  const navigate = useNavigate();
  const { swarmId, roster } = useSwarmRoster();
  const objectRef = useRef<HTMLObjectElement>(null);
  const scrollerRef = useRef<HTMLDivElement>(null);
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
      if (!tagged.__casopsAgentLinks) {
        tagged.__casopsAgentLinks = true;
        doc.addEventListener("click", (event) => {
          const target = event.target as Element | null;
          const link = target?.closest("a.agent-link");
          const href = link?.getAttribute("href") ?? null;
          if (!isAgentChatHref(href)) {
            return;
          }
          event.preventDefault();
          const agentId = agentIdFromProfileChatHref(href);
          if (roster && agentId && !roster.includes(agentId)) {
            return;
          }
          const projectId = lastProjectId();
          if (projectId && agentId) {
            navigate(projectChatHref(projectId, { agent: agentId }));
            return;
          }
          navigate(href);
        });
      }
      applySvgTheme(doc, theme);
      doc.querySelectorAll("a.agent-link").forEach((link) => {
        const agentId = link.querySelector("[data-agent-id]")?.getAttribute("data-agent-id") || "";
        const dim = Boolean(roster && agentId && !roster.includes(agentId));
        (link as HTMLElement).style.opacity = dim ? "0.28" : "";
        (link as HTMLElement).style.pointerEvents = dim ? "none" : "";
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
  }, [src, navigate, theme, roster]);

  function changeZoom(delta: number) {
    setZoom((current) => clampZoom(current + delta));
  }

  function onAutoLayout() {
    setZoom(MIN_ZOOM);
    const scroller = scrollerRef.current;
    if (scroller) {
      scroller.scrollTo({ left: 0, top: 0, behavior: "smooth" });
    }
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
          className="casops-graph flex h-[calc(100dvh-14rem)] min-h-[28rem] flex-col overflow-hidden rounded-md border border-stone-200 shadow-sm dark:border-black"
          data-testid={kind === "sub" ? "agent-sub-workflow" : "agent-workflow"}
          data-graph-theme={theme}
        >
          <div className="z-10 flex min-h-11 shrink-0 flex-wrap items-center justify-between gap-2 border-b border-stone-200 bg-white px-3 py-1.5 dark:border-[#111] dark:bg-[#252525]">
            <div>
              <p className="text-xs font-semibold text-stone-800 dark:text-[#eee]">Diagram view</p>
              <p className="hidden text-[11px] text-stone-500 sm:block dark:text-[#888]">Fit for overview; zoom for readable detail.</p>
            </div>
            <div className="flex items-center gap-1.5" role="group" aria-label="Diagram zoom controls">
              <AutoLayoutButton
                testId={kind === "sub" ? "sub-workflow-auto-layout" : "workflow-auto-layout"}
                onClick={onAutoLayout}
              />
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
              <output className="min-w-12 text-center font-mono text-xs font-semibold text-stone-600 dark:text-[#bbb]" aria-live="polite">
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
          <div ref={scrollerRef} className="min-h-0 flex-1 overflow-auto overscroll-contain">
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
