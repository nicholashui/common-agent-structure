import { useEffect, useMemo, useState } from "react";
import { useNavigate, useParams, useSearchParams } from "react-router-dom";
import { ErrorBanner } from "../components/RecoveryBanner";
import type { ProgramCommItem, ProgramRecord, ProjectDecision } from "../api/types";
import { DryRunControl } from "../components/ActorStrip";
import { GhostButton } from "../components/ui";
import { CollabHopArticle, type CollabHop } from "../components/CollabHopArticle";
import { commIdForAgent, displayPartyName, hopKindLabel, splitProjectChat } from "../lib/projectChat";
import { PROGRAM_FIRST_AGENT_HOP, PROGRAM_FIRST_CALLED } from "../lib/programs";
import { useSession } from "../state/session";

function asHop(item: ProgramCommItem): CollabHop {
  return {
    id: item.id,
    from: item.from,
    to: item.to,
    kind: item.kind,
    text: item.text || "",
    pass_id: item.pass_id,
    created_at: item.created_at,
    live: item.live ?? false,
  };
}

export function ProgramChatPage() {
  const session = useSession();
  const navigate = useNavigate();
  const params = useParams();
  const [search] = useSearchParams();
  const programId = params.programId ? decodeURIComponent(params.programId) : "";
  const focusCommParam = search.get("comm") || "";
  const focusAgent = search.get("agent") || "";
  const [record, setRecord] = useState<ProgramRecord | null>(null);
  const [items, setItems] = useState<CollabHop[]>([]);
  const [error, setError] = useState<Error | null>(null);
  const [commsLoaded, setCommsLoaded] = useState(false);
  const [loadingHops, setLoadingHops] = useState(false);

  useEffect(() => {
    if (!programId) {
      return;
    }
    setCommsLoaded(false);
    setItems([]);
    setRecord(null);
    session.client
      .getProgram(programId)
      .then(setRecord)
      .catch((err) => setError(err instanceof Error ? err : new Error(String(err))));
    session.client
      .listProgramComms(programId)
      .then((payload) => {
        setItems((payload.items ?? []).map(asHop));
      })
      .catch((err) => setError(err instanceof Error ? err : new Error(String(err))))
      .finally(() => setCommsLoaded(true));
  }, [programId, session.client]);

  const { conversation } = useMemo(() => splitProjectChat(items), [items]);
  const focusComm = useMemo(() => {
    if (focusCommParam && items.some((item) => item.id === focusCommParam)) {
      return focusCommParam;
    }
    const agent = focusAgent || focusCommParam;
    return agent ? commIdForAgent(items, agent) : "";
  }, [focusCommParam, focusAgent, items]);
  const charHops = items.filter((item) => !item.live).length;
  const liveHops = items.filter((item) => item.live).length;
  const listedDecisions: ProjectDecision[] = [];
  const focusOpt = search.get("opt") || "";

  useEffect(() => {
    if (!focusComm) {
      return;
    }
    const node = document.querySelector(`[data-comm-id="${CSS.escape(focusComm)}"]`);
    if (node instanceof HTMLElement) {
      node.scrollIntoView({ block: "center", behavior: "smooth" });
    }
  }, [focusComm, items]);

  async function loadHops() {
    if (!programId || loadingHops) {
      return;
    }
    setLoadingHops(true);
    setError(null);
    try {
      const stamped = await session.client.stampProgramComms(programId);
      setItems((stamped.items ?? []).map(asHop));
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setLoadingHops(false);
    }
  }

  function onPickOption(_agentId: string, optionId: string, commId?: string) {
    navigate(
      `/programs/${encodeURIComponent(programId)}/chat?comm=${encodeURIComponent(commId || "")}&opt=${encodeURIComponent(optionId)}`,
      { replace: true },
    );
  }

  return (
    <div data-testid="program-chat">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <div>
          <h2 className="text-lg font-semibold text-stone-800">{record?.name ?? programId}</h2>
          <p className="text-xs text-stone-500">
            Auto Pilot · first hop {displayPartyName(record?.first_agent_hop || PROGRAM_FIRST_AGENT_HOP)} →
            first-called {displayPartyName(record?.first_called || PROGRAM_FIRST_CALLED)} · Chat
          </p>
          <p className="text-xs text-stone-500" data-testid="program-chat-honesty">
            {charHops} hop{charHops === 1 ? "" : "s"} CHARACTERIZATION (not live Grok). {liveHops} live
            {liveHops ? " (generate / Imagine)" : ""}.
          </p>
        </div>
        <div className="flex gap-2">
          <DryRunControl />
          <GhostButton type="button" onClick={() => navigate(`/programs/${encodeURIComponent(programId)}/workflow`)}>
            Workflow
          </GhostButton>
        </div>
      </div>
      <ErrorBanner error={error} />
      {!commsLoaded ? (
        <p className="text-sm text-stone-500" data-testid="program-chat-loading">
          Loading Chat…
        </p>
      ) : conversation.length === 0 ? (
        <div className="rounded-2xl border border-stone-200 bg-white p-5 text-sm text-stone-500">
          <p>No communications yet. Load Program hops (intent-analysis then showrunner), same spine as Project Chat.</p>
          <GhostButton type="button" className="mt-3" data-testid="program-chat-load-hops" disabled={loadingHops} onClick={() => void loadHops()}>
            {loadingHops ? "Loading…" : "Load hops"}
          </GhostButton>
        </div>
      ) : (
        <ol className="mx-auto max-w-3xl space-y-3" data-testid="program-chat-log">
          {conversation.map((item) => (
            <li key={item.id}>
              <CollabHopArticle
                item={item}
                hops={items}
                focusComm={focusComm}
                focusOpt={focusOpt}
                listedDecisions={listedDecisions}
                scopeId={programId}
                testIdPrefix="program-chat"
                onPickOption={onPickOption}
                onOpenTag={(_scope, commId) =>
                  navigate(`/programs/${encodeURIComponent(programId)}/chat?comm=${encodeURIComponent(commId)}`)
                }
              />
            </li>
          ))}
        </ol>
      )}
      {conversation.length ? (
        <p
          className="mx-auto mt-3 max-w-3xl rounded-xl border border-stone-200 bg-white px-3 py-2 text-[11px] text-stone-600 dark:border-stone-700 dark:bg-stone-900"
          data-testid="program-autopilot-status"
        >
          Auto Pilot · Program first hop {PROGRAM_FIRST_AGENT_HOP} · first-called {PROGRAM_FIRST_CALLED}
          {" · "}
          Create Program → {hopKindLabel("instruction")}
        </p>
      ) : null}
    </div>
  );
}
