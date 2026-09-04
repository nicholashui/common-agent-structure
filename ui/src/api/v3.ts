import {
  CLIENT_BINDINGS,
  DEFAULT_TIMEOUT_MS,
  LONG_TIMEOUT_MS,
  MUTATING,
  type HttpMethod,
} from "./paths";
import { clipLogText, logApi, shouldSkipApiLog } from "../log/bus";
import {
  CasopsHttpError,
  MutationContractError,
  RequestAbortedError,
  type MutationContract,
  type AgentSummary,
  type Attestation,
  type CacheStats,
  type ComposePreviewResponse,
  type ImprovementCandidate,
  type MemoryRecord,
  type PluginRow,
  type RunResult,
  type StructureResponse,
  type ValidationReport,
  type LlmProvider,
  type LlmSettingsView,
  type AgentLlmView,
  type ChatResponse,
  type EvalFixturesResponse,
  type AgentFileItem,
  type AgentFilesResponse,
} from "./types";

export type FetchLike = (input: string, init?: RequestInit) => Promise<Response>;

export interface ClientOptions {
  getBaseUrl: () => string;
  getMutation: () => MutationContract;
  fetchImpl?: FetchLike;
  onSuccess?: () => void;
  onError?: (error: CasopsHttpError) => void;
}

function fill(path: string, params: Record<string, string>): string {
  return path.replace(/\{(\w+)\}/g, (_, key: string) => {
    const value = params[key];
    if (!value) {
      throw new Error(`missing path parameter ${key}`);
    }
    return encodeURIComponent(value);
  });
}

function query(params: Record<string, string | undefined>): string {
  const search = new URLSearchParams();
  for (const [key, value] of Object.entries(params)) {
    if (value !== undefined && value !== "") {
      search.set(key, value);
    }
  }
  const text = search.toString();
  return text ? `?${text}` : "";
}

function joinUrl(base: string, path: string): string {
  if (!base) {
    return path;
  }
  return `${base.replace(/\/$/, "")}${path}`;
}

function mutationHeaders(contract: MutationContract): Record<string, string> {
  return {
    "x-casops-actor": contract.actor,
    "x-casops-reason": contract.reason,
    "x-casops-expected-parent": contract.expectedParent,
    "x-casops-dry-run": contract.dryRun ? "true" : "false",
  };
}

function assertMutation(method: HttpMethod, path: string, contract: MutationContract): void {
  if (!MUTATING.has(method)) {
    return;
  }
  if (!contract.actor || !contract.reason.trim() || contract.expectedParent === undefined || contract.dryRun === undefined) {
    throw new MutationContractError(
      "IMP_UNSIGNED",
      "mutation requires actor, reason, expected parent version, dry-run",
    );
  }
  if (path.endsWith("/approve") && contract.actor === "agent_runtime") {
    throw new MutationContractError("IMP_SELF_APPROVAL", "agent cannot approve or write invariants");
  }
}

async function parseBody(response: Response): Promise<unknown> {
  const text = await response.text();
  if (!text) {
    return {};
  }
  try {
    return JSON.parse(text) as unknown;
  } catch {
    return text;
  }
}

export function createClient(options: ClientOptions) {
  const fetchImpl: FetchLike = options.fetchImpl ?? ((input, init) => fetch(input, init));

  async function request<T>(
    method: HttpMethod,
    path: string,
    init?: {
      params?: Record<string, string>;
      query?: Record<string, string | undefined>;
      timeoutMs?: number;
      body?: unknown;
      reasonFallback?: string;
      signal?: AbortSignal;
    },
  ): Promise<T> {
    const filled = fill(path, init?.params ?? {});
    const url = joinUrl(options.getBaseUrl(), `${filled}${query(init?.query ?? {})}`);
    const headers: Record<string, string> = { Accept: "application/json" };
    if (MUTATING.has(method)) {
      const raw = options.getMutation();
      const contract = raw.reason.trim()
        ? raw
        : { ...raw, reason: init?.reasonFallback?.trim() || raw.reason };
      assertMutation(method, filled, contract);
      Object.assign(headers, mutationHeaders(contract));
    }
    let payload: string | undefined;
    if (init?.body !== undefined) {
      headers["Content-Type"] = "application/json";
      payload = JSON.stringify(init.body);
    }
    const controller = new AbortController();
    const external = init?.signal;
    const onAbort = () => controller.abort();
    if (external) {
      if (external.aborted) {
        controller.abort();
      } else {
        external.addEventListener("abort", onAbort, { once: true });
      }
    }
    const timeoutMs = init?.timeoutMs ?? DEFAULT_TIMEOUT_MS;
    let timedOut = false;
    const timer = setTimeout(() => {
      timedOut = true;
      controller.abort();
    }, timeoutMs);
    const started = Date.now();
    const skipLog = shouldSkipApiLog(url);
    try {
      const response = await fetchImpl(url, { method, headers, body: payload, signal: controller.signal });
      const body = await parseBody(response);
      const elapsed = Date.now() - started;
      if (!skipLog) {
        const level = response.ok ? "info" : "error";
        logApi(`${method} ${filled} ${response.status} ${elapsed}ms`, clipLogText({ request: payload ?? null, response: body }), level);
      }
      if (!response.ok) {
        const error = new CasopsHttpError(response.status, body);
        options.onError?.(error);
        throw error;
      }
      if (filled.startsWith("/api/v3")) {
        options.onSuccess?.();
      }
      return body as T;
    } catch (error) {
      if (error instanceof CasopsHttpError) {
        throw error;
      }
      const abortedByUser = Boolean(external?.aborted) && !timedOut;
      if (abortedByUser) {
        throw new RequestAbortedError("Generation stopped");
      }
      const elapsed = Date.now() - started;
      if (!skipLog) {
        logApi(
          `${method} ${filled} FAILED ${elapsed}ms`,
          error instanceof Error ? error.message : String(error),
          "error",
        );
      }
      const wrapped = new CasopsHttpError(0, {
        error: {
          code: "UNAVAILABLE",
          message: error instanceof Error ? error.message : "Control plane unreachable",
          containment_required: false,
        },
      });
      options.onError?.(wrapped);
      throw wrapped;
    } finally {
      if (external) {
        external.removeEventListener("abort", onAbort);
      }
      clearTimeout(timer);
    }
  }

  function bound<K extends keyof typeof CLIENT_BINDINGS>(
    name: K,
    params: Record<string, string>,
    extra?: { query?: Record<string, string | undefined>; timeoutMs?: number },
  ) {
    const [method, path] = CLIENT_BINDINGS[name];
    return request(method, path, { params, query: extra?.query, timeoutMs: extra?.timeoutMs });
  }

  return {
    request,
    getHealth: () => request<{ status: string; service: string }>("GET", "/health"),
    listAgents: () => bound("listAgents", {}) as Promise<{ agents: AgentSummary[] }>,
    getStructure: (agentId: string) => bound("getStructure", { agent_id: agentId }) as Promise<StructureResponse>,
    getResolved: (agentId: string) => bound("getResolved", { agent_id: agentId }) as Promise<Record<string, unknown>>,
    composePreview: (agentId: string) =>
      bound("composePreview", { agent_id: agentId }, { timeoutMs: LONG_TIMEOUT_MS }) as Promise<ComposePreviewResponse>,
    getRuntimePlan: (agentId: string) => bound("getRuntimePlan", { agent_id: agentId }) as Promise<Record<string, unknown>>,
    getRuntimeCapabilities: (agentId: string) =>
      bound("getRuntimeCapabilities", { agent_id: agentId }) as Promise<Record<string, unknown>>,
    getCapabilitiesMatrix: (agentId: string) =>
      bound("getCapabilitiesMatrix", { agent_id: agentId }) as Promise<{
        agent_id?: string;
        matrix: { capability: string; status: string }[];
        production_bindable?: boolean;
      }>,
    verifyCapabilities: (agentId: string) =>
      bound("verifyCapabilities", { agent_id: agentId }) as Promise<{
        matrix: { capability: string; status: string }[];
        production_bindable?: boolean;
      }>,
    getContextBudget: (agentId: string) =>
      bound("getContextBudget", { agent_id: agentId }) as Promise<Record<string, unknown>>,
    getCacheStats: (agentId: string) => bound("getCacheStats", { agent_id: agentId }) as Promise<CacheStats>,
    invalidateCache: (agentId: string) =>
      bound("invalidateCache", { agent_id: agentId }) as Promise<Record<string, unknown>>,
    getProtocols: (agentId: string) => bound("getProtocols", { agent_id: agentId }) as Promise<Record<string, unknown>>,
    getPlugins: (agentId: string) =>
      bound("getPlugins", { agent_id: agentId }) as Promise<{ plugins: PluginRow[]; count?: number }>,
    validatePlugins: (agentId: string) =>
      bound("validatePlugins", { agent_id: agentId }) as Promise<{ plugins: PluginRow[]; executed?: boolean }>,
    getMemoryPolicy: (agentId: string) =>
      bound("getMemoryPolicy", { agent_id: agentId }) as Promise<Record<string, unknown>>,
    getMemoryHierarchy: (agentId: string) =>
      bound("getMemoryHierarchy", { agent_id: agentId }) as Promise<Record<string, unknown>>,
    queryMemory: (agentId: string, scope: { tenant: string; subject: string; text?: string }) =>
      bound("queryMemory", { agent_id: agentId }, { query: scope }) as Promise<{ records: MemoryRecord[] }>,
    writeMemoryCandidate: (agentId: string, scope: { tenant: string; subject: string; text: string }) =>
      bound("writeMemoryCandidate", { agent_id: agentId }, { query: scope }) as Promise<{ memory_id: string }>,
    consolidateMemory: (agentId: string) =>
      bound("consolidateMemory", { agent_id: agentId }) as Promise<{ queued: boolean; queue_depth: number }>,
    deleteMemory: (agentId: string, memoryId: string, scope: { tenant: string; subject: string }) =>
      bound("deleteMemory", { agent_id: agentId, memory_id: memoryId }, { query: scope }) as Promise<{
        tombstoned: boolean;
        memory_id: string;
      }>,
    verifyMemoryDeletion: (agentId: string, memoryId: string, scope: { tenant: string; subject: string }) =>
      bound("verifyMemoryDeletion", { agent_id: agentId, memory_id: memoryId }, { query: scope }) as Promise<
        Record<string, unknown>
      >,
    getTrace: (traceId: string) => bound("getTrace", { trace_id: traceId }) as Promise<Record<string, unknown>>,
    replayTrace: (traceId: string, counterfactual?: string) =>
      bound("replayTrace", { trace_id: traceId }, { query: { counterfactual } }) as Promise<Record<string, unknown>>,
    getRootCause: (traceId: string) => bound("getRootCause", { trace_id: traceId }) as Promise<Record<string, unknown>>,
    getEvidenceGraph: (artifactId: string) =>
      bound("getEvidenceGraph", { artifact_id: artifactId }) as Promise<unknown>,
    getIncidents: (agentId: string) =>
      bound("getIncidents", { agent_id: agentId }) as Promise<{ incidents: unknown[] }>,
    runRedteam: (agentId: string) => bound("runRedteam", { agent_id: agentId }) as Promise<Record<string, unknown>>,
    listCandidates: (agentId: string) =>
      bound("listCandidates", { agent_id: agentId }) as Promise<{ candidates: ImprovementCandidate[] }>,
    evaluateCandidate: (agentId: string, cid: string) =>
      bound("evaluateCandidate", { agent_id: agentId, cid }) as Promise<ImprovementCandidate>,
    approveCandidate: (agentId: string, cid: string) =>
      bound("approveCandidate", { agent_id: agentId, cid }) as Promise<ImprovementCandidate>,
    rollback: (agentId: string, version: string) =>
      bound("rollback", { agent_id: agentId, version }) as Promise<Record<string, unknown>>,
    getLedger: (agentId: string) => bound("getLedger", { agent_id: agentId }) as Promise<{ ledger: unknown[] }>,
    getRegressionSuite: (agentId: string) =>
      bound("getRegressionSuite", { agent_id: agentId }) as Promise<{ fixtures: string[] }>,
    getEvalFixtures: (agentId: string) =>
      bound("getEvalFixtures", { agent_id: agentId }) as Promise<EvalFixturesResponse>,
    listAgentFiles: (agentId: string) =>
      bound("listAgentFiles", { agent_id: agentId }) as Promise<AgentFilesResponse>,
    getAgentFile: (agentId: string, path: string) =>
      bound("getAgentFile", { agent_id: agentId }, { query: { path } }) as Promise<AgentFileItem>,
    putAgentFile: (agentId: string, path: string, content: string) =>
      request<AgentFileItem>("PUT", "/api/v3/agents/{agent_id}/files/item", {
        params: { agent_id: agentId },
        query: { path },
        body: { content },
      }),
    getAttestation: (agentId: string) => bound("getAttestation", { agent_id: agentId }) as Promise<Attestation>,
    getValidationReport: (agentId: string) =>
      bound("getValidationReport", { agent_id: agentId }) as Promise<ValidationReport>,
    runAgent: (agentId: string) =>
      bound("runAgent", { agent_id: agentId }, { timeoutMs: LONG_TIMEOUT_MS }) as Promise<RunResult>,
    listLlmProviders: () => bound("listLlmProviders", {}) as Promise<{ providers: LlmProvider[] }>,
    getLlmSettings: () => bound("getLlmSettings", {}) as Promise<LlmSettingsView>,
    setLlmSettings: (defaultLlm: string | null) =>
      request<LlmSettingsView>("POST", "/api/v3/llm/settings", { body: { default_llm: defaultLlm } }),
    getAgentLlm: (agentId: string) => bound("getAgentLlm", { agent_id: agentId }) as Promise<AgentLlmView>,
    setAgentLlm: (agentId: string, provider: string | null) =>
      request<AgentLlmView>("POST", "/api/v3/agents/{agent_id}/llm", {
        params: { agent_id: agentId },
        body: { provider },
      }),
    chatAgent: (
      agentId: string,
      body: { message: string; history?: { role: string; content: string }[] },
      extra?: { signal?: AbortSignal },
    ) =>
      request<ChatResponse>("POST", "/api/v3/agents/{agent_id}/runtime/chat", {
        params: { agent_id: agentId },
        body,
        timeoutMs: LONG_TIMEOUT_MS,
        reasonFallback: "operator chat",
        signal: extra?.signal,
      }),
  };
}

export type CasopsClient = ReturnType<typeof createClient>;
