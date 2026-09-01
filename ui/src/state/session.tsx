import { createContext, useContext, useEffect, useMemo, useState, type ReactNode } from "react";
import { createClient, type CasopsClient } from "../api/v3";
import { ACTORS, CasopsHttpError, type ActorClass, type AgentSummary, type MutationContract, type RunResult } from "../api/types";
import type { StatusKind } from "../components/statusCfg";

const SETTINGS_KEY = "casops.control-ui.settings.v1";
const ACTOR_KEY = "casops.control-ui.actor.v1";
const TEMPLATE_ID = "casops.template.baseline_safe";
const SAMPLE_HEALTH_ID = "common.health";

export interface Toast {
  id: number;
  code: string;
  message: string;
}

export interface SettingsState {
  baseUrl: string;
  knownIds: string[];
  pollMs: number;
  persistActor: boolean;
  defaultActor: ActorClass;
  defaultDryRun: boolean;
}

interface SessionValue {
  settings: SettingsState;
  setSettings: (next: SettingsState) => void;
  actor: ActorClass;
  setActor: (actor: ActorClass) => void;
  reason: string;
  setReason: (reason: string) => void;
  expectedParent: string;
  setExpectedParent: (value: string) => void;
  dryRun: boolean;
  setDryRun: (value: boolean) => void;
  client: CasopsClient;
  connection: StatusKind;
  healthOk: boolean;
  stale: boolean;
  running: boolean;
  setRunning: (value: boolean) => void;
  lastError: CasopsHttpError | null;
  containment: boolean;
  agents: AgentSummary[];
  setAgents: (agents: AgentSummary[]) => void;
  discovery: "list" | "known" | "empty";
  setDiscovery: (value: "list" | "known" | "empty") => void;
  lastRuns: Record<string, RunResult>;
  rememberRun: (run: RunResult) => void;
  toasts: Toast[];
  dismissToast: (id: number) => void;
  mutationReady: boolean;
  mutationLabel: (live: string, dry: string) => string;
  refreshHealth: () => Promise<void>;
}

const SessionContext = createContext<SessionValue | null>(null);

function loadSettings(): SettingsState {
  const fallback: SettingsState = {
    baseUrl: import.meta.env.VITE_CASOPS_BASE ?? "",
    knownIds: [TEMPLATE_ID, SAMPLE_HEALTH_ID],
    pollMs: 15000,
    persistActor: false,
    defaultActor: "human_operator",
    defaultDryRun: true,
  };
  try {
    const raw = localStorage.getItem(SETTINGS_KEY);
    if (!raw) {
      return fallback;
    }
    const parsed = JSON.parse(raw) as Partial<SettingsState>;
    return {
      ...fallback,
      ...parsed,
      knownIds: parsed.knownIds?.length ? parsed.knownIds : fallback.knownIds,
      defaultActor: ACTORS.includes(parsed.defaultActor as ActorClass)
        ? (parsed.defaultActor as ActorClass)
        : "human_operator",
    };
  } catch {
    return fallback;
  }
}

function loadActor(settings: SettingsState): MutationContract {
  const fallback: MutationContract = {
    actor: settings.defaultActor,
    reason: "",
    expectedParent: "none",
    dryRun: settings.defaultDryRun,
  };
  try {
    const raw = (settings.persistActor ? localStorage : sessionStorage).getItem(ACTOR_KEY);
    if (!raw) {
      return fallback;
    }
    const parsed = JSON.parse(raw) as Partial<MutationContract>;
    return {
      actor: ACTORS.includes(parsed.actor as ActorClass) ? (parsed.actor as ActorClass) : fallback.actor,
      reason: parsed.reason ?? "",
      expectedParent: parsed.expectedParent ?? "none",
      dryRun: parsed.dryRun ?? true,
    };
  } catch {
    return fallback;
  }
}

function deriveConnection(opts: {
  healthOk: boolean;
  lastSuccessAt: number | null;
  reconnecting: boolean;
  running: boolean;
  containment: boolean;
  now: number;
}): StatusKind {
  if (opts.containment) {
    return "recovery";
  }
  if (opts.running) {
    return "running";
  }
  if (opts.reconnecting) {
    return "reconnecting";
  }
  if (!opts.healthOk) {
    return "unavailable";
  }
  if (opts.lastSuccessAt === null) {
    return "live";
  }
  const age = opts.now - opts.lastSuccessAt;
  if (age > 5 * 60_000) {
    return "stale";
  }
  if (age >= 30_000) {
    return "delayed";
  }
  return "live";
}

export function SessionProvider({ children }: { children: ReactNode }) {
  const [settings, setSettingsState] = useState<SettingsState>(() => loadSettings());
  const initial = loadActor(settings);
  const [actor, setActor] = useState<ActorClass>(initial.actor);
  const [reason, setReason] = useState(initial.reason);
  const [expectedParent, setExpectedParent] = useState(initial.expectedParent);
  const [dryRun, setDryRun] = useState(initial.dryRun);
  const [healthOk, setHealthOk] = useState(false);
  const [reconnecting, setReconnecting] = useState(false);
  const [lastSuccessAt, setLastSuccessAt] = useState<number | null>(null);
  const [running, setRunning] = useState(false);
  const [lastError, setLastError] = useState<CasopsHttpError | null>(null);
  const [agents, setAgents] = useState<AgentSummary[]>([]);
  const [discovery, setDiscovery] = useState<"list" | "known" | "empty">("known");
  const [lastRuns, setLastRuns] = useState<Record<string, RunResult>>({});
  const [toasts, setToasts] = useState<Toast[]>([]);
  const [now, setNow] = useState(() => Date.now());

  useEffect(() => {
    localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings));
  }, [settings]);

  useEffect(() => {
    const payload = JSON.stringify({ actor, reason, expectedParent, dryRun });
    sessionStorage.setItem(ACTOR_KEY, payload);
    if (settings.persistActor) {
      localStorage.setItem(ACTOR_KEY, payload);
    }
  }, [actor, reason, expectedParent, dryRun, settings.persistActor]);

  const pushToast = (error: CasopsHttpError) => {
    setToasts((current) => [...current.slice(-4), { id: Date.now(), code: error.code, message: error.message }]);
  };

  const client = useMemo(
    () =>
      createClient({
        getBaseUrl: () => settings.baseUrl,
        getMutation: () => ({ actor, reason, expectedParent, dryRun }),
        onSuccess: () => {
          setLastSuccessAt(Date.now());
          setReconnecting(false);
        },
        onError: (error) => {
          setLastError(error);
          if (error.code === "UNAVAILABLE") {
            setReconnecting(true);
            setHealthOk(false);
          }
          pushToast(error);
        },
      }),
    [settings.baseUrl, actor, reason, expectedParent, dryRun],
  );

  const refreshHealth = async () => {
    try {
      await client.getHealth();
      setHealthOk(true);
      setReconnecting(false);
    } catch {
      setHealthOk(false);
      setReconnecting(true);
    }
  };

  useEffect(() => {
    void refreshHealth();
    const id = window.setInterval(() => {
      setNow(Date.now());
      void refreshHealth();
    }, 5000);
    return () => window.clearInterval(id);
  }, [client]);

  useEffect(() => {
    let cancelled = false;
    void (async () => {
      try {
        const listed = await client.listAgents();
        if (cancelled) {
          return;
        }
        setAgents(listed.agents);
        setDiscovery(listed.agents.length ? "list" : "empty");
      } catch {
        if (!cancelled) {
          setDiscovery("known");
        }
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [client]);

  const containment = Boolean(lastError?.containment_required);
  const connection = deriveConnection({
    healthOk,
    lastSuccessAt,
    reconnecting,
    running,
    containment,
    now,
  });
  const stale = connection === "stale";
  const mutationReady = reason.trim().length > 0 && !stale && !containment && healthOk;

  const value: SessionValue = {
    settings,
    setSettings: setSettingsState,
    actor,
    setActor,
    reason,
    setReason,
    expectedParent,
    setExpectedParent,
    dryRun,
    setDryRun,
    client,
    connection,
    healthOk,
    stale,
    running,
    setRunning,
    lastError,
    containment,
    agents,
    setAgents,
    discovery,
    setDiscovery,
    lastRuns,
    rememberRun: (run) => setLastRuns((current) => ({ ...current, [run.agent_id]: run })),
    toasts,
    dismissToast: (id) => setToasts((current) => current.filter((toast) => toast.id !== id)),
    mutationReady,
    mutationLabel: (live, dry) => (dryRun ? dry : live),
    refreshHealth,
  };

  return <SessionContext.Provider value={value}>{children}</SessionContext.Provider>;
}

export function useSession(): SessionValue {
  const value = useContext(SessionContext);
  if (!value) {
    throw new Error("useSession outside provider");
  }
  return value;
}
