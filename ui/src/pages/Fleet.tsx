import { useEffect, useMemo, useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import { AgentCard, type AgentCardModel } from "../components/AgentCard";
import { EmptyState, PageHeader, inputClass } from "../components/ui";
import { ErrorBanner } from "../components/RecoveryBanner";
import { CasopsHttpError, type AgentSummary } from "../api/types";
import { type AgentPack, agentPack, filterAgentCards, groupFleetCards, listAgentCategories } from "../lib/agents";
import { loadFleetFallback, loadFleetList, runStatusFor, summariesToCards } from "../lib/fleet";
import { filterByRoster, useSwarmRoster } from "../lib/swarmFilter";
import { HOME_LABEL } from "../shell/nav";
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
  const [, setSearchParams] = useSearchParams();
  const { swarmId, roster } = useSwarmRoster();
  const [swarms, setSwarms] = useState<{ swarm_id: string }[]>([]);
  const [cards, setCards] = useState<AgentCardModel[]>([]);
  const [query, setQuery] = useState("");
  const [pack, setPack] = useState<AgentPack>("all");
  const [category, setCategory] = useState("");
  const [error, setError] = useState<Error | null>(null);
  const [asOf, setAsOf] = useState<Date | null>(null);
  const [ready, setReady] = useState(false);

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
    } finally {
      setReady(true);
    }
  }

  useEffect(() => {
    session.client
      .listSwarms()
      .then((payload) => setSwarms(payload.swarms || []))
      .catch(() => setSwarms([]));
  }, [session.client]);

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
  const categoryOptions = useMemo(() => {
    const source = pack === "all" ? listed : listed.filter((item) => agentPack(item.agent_id) === pack);
    return listAgentCategories(source);
  }, [listed, pack]);
  const effectiveCategory = categoryOptions.includes(category) ? category : "";
  const visible = useMemo(() => {
    const withRuns = listed.map((card) => ({
      ...card,
      runStatus: runStatusFor(session.lastRuns[card.agent_id]),
    }));
    return filterByRoster(filterAgentCards(withRuns, query, pack, effectiveCategory), roster);
  }, [listed, query, pack, effectiveCategory, session.lastRuns, roster]);
  const groups = useMemo(() => groupFleetCards(visible, pack), [visible, pack]);
  const showPackHeadings = pack === "all" && groups.length > 1;

  return (
    <div>
      <PageHeader
        title={HOME_LABEL}
        subtitle={
          swarmId
            ? `Roster ${swarmId} — not a swarm runner`
            : "Pack browser — not a swarm runner"
        }
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
          body="Start uvicorn on :18080, then confirm the base URL in Settings."
        />
      ) : null}
      <ErrorBanner error={error instanceof CasopsHttpError || error instanceof Error ? error : null} />
      {listed.length ? (
        <div className="mb-5 flex flex-col gap-3 sm:flex-row sm:items-center">
          <input
            className={`${inputClass} w-full max-w-md font-mono`}
            placeholder="Filter by agent_id, role, folder, or category"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            aria-label="Filter agents"
          />
          {swarms.length ? (
            <select
              className={`${inputClass} w-full max-w-[16rem] font-mono`}
              value={swarmId}
              onChange={(event) => {
                const value = event.target.value;
                if (value) {
                  setSearchParams({ swarm: value });
                } else {
                  setSearchParams({});
                }
              }}
              aria-label="Swarm roster"
              data-testid="fleet-swarm-filter"
            >
              <option value="">All pack</option>
              {swarms.map((row) => (
                <option key={row.swarm_id} value={row.swarm_id}>
                  {row.swarm_id}
                </option>
              ))}
            </select>
          ) : null}
          {categoryOptions.length ? (
            <select
              className={`${inputClass} w-full max-w-[12rem] font-mono`}
              value={effectiveCategory}
              onChange={(event) => setCategory(event.target.value)}
              aria-label="Filter by category"
              data-testid="fleet-category-filter"
            >
              <option value="">All categories</option>
              {categoryOptions.map((item) => (
                <option key={item} value={item}>
                  {item}
                </option>
              ))}
            </select>
          ) : null}
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
      {!ready && !listed.length ? (
        <p className="text-sm text-stone-500" data-testid="fleet-loading">
          Loading agents…
        </p>
      ) : session.discovery === "empty" && !listed.length ? (
        <EmptyState
          title="No agents"
          body="Add a known agent_id in Settings or implement GET /api/v3/agents. The UI does not scan disk from the browser."
        />
      ) : visible.length ? (
        <div className="space-y-8">
          {groups.map((group) => (
            <section
              key={group.pack}
              data-testid="fleet-pack"
              data-pack={group.pack}
            >
              {showPackHeadings ? (
                <h2 className="mb-3 text-xs font-semibold uppercase tracking-wide text-stone-400">
                  {group.pack}
                  <span className="ml-2 font-normal normal-case text-stone-400">
                    {group.categories.reduce((sum, item) => sum + item.items.length, 0)}
                  </span>
                </h2>
              ) : null}
              <div className="space-y-6">
                {group.categories.map((bucket) => (
                  <div
                    key={`${group.pack}:${bucket.category}`}
                    data-testid="fleet-category"
                    data-category={bucket.category}
                  >
                    {group.showCategory ? (
                      <div className="mb-3 flex items-baseline gap-2">
                        <h3 className="text-sm font-semibold text-stone-900">{bucket.category}</h3>
                        <span className="text-xs text-stone-400">{bucket.items.length}</span>
                      </div>
                    ) : null}
                    <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
                      {bucket.items.map((agent) => (
                        <AgentCard
                          key={agent.agent_id}
                          agent={agent}
                          onCompose={() => navigate(`/agents/${encodeURIComponent(agent.agent_id)}/compose`)}
                        />
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </section>
          ))}
        </div>
      ) : (
        <EmptyState title="No matching agents" body="Clear the filter or choose All to see the full Agent Swarm." />
      )}
    </div>
  );
}
