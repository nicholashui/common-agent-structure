export const ACTORS = [
  "human_operator",
  "independent_approver",
  "host_service",
  "agent_runtime",
] as const;

export type ActorClass = (typeof ACTORS)[number];

export interface MutationContract {
  actor: ActorClass;
  reason: string;
  expectedParent: string;
  dryRun: boolean;
}

export interface CasopsErrorBody {
  code: string;
  message: string;
  containment_required?: boolean;
}

export class CasopsHttpError extends Error {
  readonly status: number;
  readonly code: string;
  readonly containment_required: boolean;
  readonly body: unknown;

  constructor(status: number, body: unknown) {
    const error =
      body && typeof body === "object" && "error" in body
        ? (body as { error: CasopsErrorBody }).error
        : undefined;
    const code = error?.code || `HTTP_${status}`;
    const message = error?.message || (typeof body === "string" ? body : "Request rejected");
    super(message);
    this.name = "CasopsHttpError";
    this.status = status;
    this.code = code;
    this.containment_required = Boolean(error?.containment_required);
    this.body = body;
  }
}

export class MutationContractError extends CasopsHttpError {
  constructor(code: "IMP_UNSIGNED" | "IMP_SELF_APPROVAL", message: string) {
    super(409, { error: { code, message, containment_required: false } });
    this.name = "MutationContractError";
  }
}

export interface AgentSummary {
  agent_id: string;
  folder: string;
  structure_id: string;
  schema_version: string;
  role: string;
  memory_mode?: string;
  va_category?: string;
}

export interface StructureResponse {
  agent_id: string;
  structure_id: string;
  schema_version: string;
  folder: string;
  spec_bytes: number;
}

export interface ComposePreviewResponse {
  agent_id?: string;
  compose_hash: string;
  mro: unknown;
  findings: unknown;
  errors: unknown;
  lock: unknown;
  wrote_locks: boolean;
}

export interface CapabilityRow {
  capability: string;
  status: string;
  assertion?: unknown;
}

export interface PluginRow {
  id: string;
  isolation: string;
  validated?: boolean;
  executed?: boolean;
}

export interface MemoryRecord {
  memory_id: string;
  text: string;
}

export interface ValidationReport {
  agent_id?: string;
  verdict?: string;
  reason?: string;
  pass?: boolean;
  instruments?: string[];
  honesty?: string;
  tier?: string;
}

export interface RunResult {
  agent_id: string;
  root_trace_id: string;
  trace?: unknown;
  artifact?: { id?: string; text?: string; digest?: string };
  containment_stop: string | null;
  memory_writes: unknown[];
  safety?: unknown;
  cancelled: boolean;
  adapter: string;
}

export interface ImprovementCandidate {
  id: string;
  agent_id?: string;
  state?: string;
}

export interface Attestation {
  agent_id: string;
  digest: string;
  signature: string;
  status: string;
  invariant_set_id: string;
}

export interface LlmProvider {
  id: string;
  label: string;
  kind: string;
  configured: boolean;
  model?: string;
}

export interface LlmSettingsView {
  env_default: string;
  default_llm: string;
  default_source: string;
  agents: Record<string, string>;
  providers: LlmProvider[];
  saved?: boolean;
  dry_run?: boolean;
}

export interface AgentLlmView {
  agent_id: string;
  provider: string;
  override?: string | null;
  default_llm?: string;
  providers?: LlmProvider[];
  saved?: boolean;
  dry_run?: boolean;
}

export interface CacheStats {
  agent_id?: string;
  entries?: number;
  tiers?: string[];
  t3_enabled?: boolean;
  telemetry?: Record<string, number>;
  false_reuse_rate?: number | null;
}
