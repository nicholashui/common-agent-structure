import { useEffect, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import { AgentCard, type AgentCardModel } from "../components/AgentCard";
import { EmptyState, PageHeader, inputClass } from "../components/ui";
import { ErrorBanner } from "../components/RecoveryBanner";
import { CasopsHttpError, type AgentSummary } from "../api/types";
import { type AgentPack, filterAgentCards } from "../lib/agents";
import { loadFleetFallback, loadFleetList, runStatusFor, summariesToCards } from "../lib/fleet";
import { useSession } from "../state/session";

const PACKS: { id: AgentPack; label: string }[] = [
  { id: "all", label: "All" },
  { id: "specials", label: "specials" },
  { id: "video", label: "video" },
  { id: "other", label: "other" },
];

export function FleetPage() {
  const session = useSession();
  const navigate = useNavigate();
  const [cards, setCards] = useState<AgentCardModel[]>([]);
  const [query, setQuery] = useState("");
  const [pack, setPack] = useState<AgentPack>("all");
  const [error, setError] = useState<Error | null>(null);
  const [asOf, setAsOf] = useState<Date | null>(null);

  async function load() {
    try {
      let summaries: AgentSummary[] = [];
      try {
        summaries = await loadFleetList(session.client);
        session.setDiscovery(summaries.length ? "list" : "empty");
      } catch (err) {
        summaries = await loadFleetFallback(session.client, session.settings.knownIds);
        session.setDiscovery(summaries.length ? "known" : "empty");
        if (!summaries.length && err instanceof Error) {
          setError(err);
        }
      }
      session.setAgents(summaries);
      setCards(summariesToCards(summaries, session.lastRuns));
      setError(null);
      setAsOf(new Date());
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  useEffect(() => {
    void load();
    const tick = window.setInterval(() => {
      if (document.visibilityState === "visible" && !session.stale) {
        void load();
      }
    }, session.settings.pollMs);
    return () => window.clearInterval(tick);
  }, [session.client, session.settings.pollMs, session.settings.knownIds.join("|")]);

  const listed = cards.length ? cards : summariesToCards(session.agents, session.lastRuns);
  const visible = useMemo(() => {
    const withRuns = listed.map((card) => ({
      ...card,
      runStatus: runStatusFor(session.lastRuns[card.agent_id]),
    }));
    return filterAgentCards(withRuns, query, pack);
  }, [listed, query, pack, session.lastRuns]);

  return (
    <div>
      <PageHeader
        title="Fleet"
        asOf={asOf}
        actions={
          <p className="text-sm text-stone-500" data-testid="fleet-count">
            {visible.length} of {listed.length} agents
          </p>
        }
      />
      {!session.healthOk ? (
        <EmptyState
          title="Control plane unavailable"
          body="Start uvicorn on :8080, then confirm the base URL in Settings."
        />
      ) : null}
      <ErrorBanner error={error instanceof CasopsHttpError || error instanceof Error ? error : null} />
      {listed.length ? (
        <div className="mb-5 flex flex-col gap-3 sm:flex-row sm:items-center">
          <input
            className={`${inputClass} w-full max-w-md font-mono`}
            placeholder="Filter by agent_id, role, or folder"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            aria-label="Filter agents"
          />
          <div className="flex flex-wrap gap-1">
            {PACKS.map((item) => (
              <button
                key={item.id}
                type="button"
                className={[
                  "rounded-full px-3 py-1 text-xs font-medium",
                  pack === item.id
                    ? "bg-indigo-600 text-white"
                    : "bg-stone-100 text-stone-600 hover:bg-stone-200",
                ].join(" ")}
                onClick={() => setPack(item.id)}
              >
                {item.label}
              </button>
            ))}
          </div>
        </div>
      ) : null}
      {session.discovery === "empty" && !listed.length ? (
        <EmptyState
          title="No agents"
          body="Add a known agent_id in Settings or implement GET /api/v3/agents. The UI does not scan disk from the browser."
        />
      ) : visible.length ? (
        <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {visible.map((agent) => (
            <AgentCard
              key={agent.agent_id}
              agent={agent}
              onCompose={() => navigate(`/agents/${encodeURIComponent(agent.agent_id)}/compose`)}
            />
          ))}
        </div>
      ) : (
        <EmptyState title="No matching agents" body="Clear the filter or choose All to see the full fleet." />
      )}
    </div>
  );
}
