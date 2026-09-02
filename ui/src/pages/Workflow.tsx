import { useEffect, useMemo, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { EmptyState, PageHeader, inputClass } from "../components/ui";
import { listAgentGroups } from "../lib/agents";
import { listSubWorkflows, subWorkflowSvgSrc, workflowSvgSrc } from "../lib/workflow";
import { useSession } from "../state/session";

function isAgentChatHref(href: string | null): href is string {
  return Boolean(href && href.startsWith("/agents/") && href.endsWith("/chat"));
}

export function WorkflowPage({ kind = "main" }: { kind?: "main" | "sub" }) {
  const session = useSession();
  const navigate = useNavigate();
  const objectRef = useRef<HTMLObjectElement>(null);
  const groups = useMemo(() => listAgentGroups(session.agents), [session.agents]);
  const [group, setGroup] = useState<string>("");
  const [subId, setSubId] = useState<string>("");
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
          className="h-[calc(100vh-14rem)] overflow-auto rounded-2xl border border-stone-200 bg-white"
          data-testid={kind === "sub" ? "agent-sub-workflow" : "agent-workflow"}
        >
          <object
            key={src}
            ref={objectRef}
            data={src}
            type="image/svg+xml"
            className="min-h-full w-full"
            aria-label={kind === "sub" ? `${selectedSub?.label ?? selected} workflow` : `${selected} workflow`}
          >
            <img src={src} alt={kind === "sub" ? `${selectedSub?.label ?? selected} workflow` : `${selected} workflow`} className="w-full" />
          </object>
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
