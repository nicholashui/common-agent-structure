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
  detail?: string;
  containment_required?: boolean;
}

export class CasopsHttpError extends Error {
  readonly status: number;
  readonly code: string;
  readonly containment_required: boolean;
  readonly body: unknown;
  readonly detail?: string;

  constructor(status: number, body: unknown) {
    const error =
      body && typeof body === "object" && "error" in body
        ? (body as { error: CasopsErrorBody }).error
        : undefined;
    const code = error?.code || `HTTP_${status}`;
    const detail = error?.detail;
    const message =
      (detail && detail !== error?.message ? `${error?.message || "Request rejected"} (${detail})` : error?.message) ||
      (typeof body === "string" ? body : "Request rejected");
    super(message);
    this.name = "CasopsHttpError";
    this.status = status;
    this.code = code;
    this.containment_required = Boolean(error?.containment_required);
    this.body = body;
    this.detail = detail;
  }
}

export class RequestAbortedError extends Error {
  constructor(message = "Request stopped") {
    super(message);
    this.name = "RequestAbortedError";
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

export interface AgentIo {
  defined?: boolean;
  merged?: boolean;
  source?: string;
  inputs?: string[];
  outputs?: string[];
  role?: string;
  prompt_reference?: string;
  rubric_reference?: string;
  protocols?: string[];
  plugin_interfaces?: { id: string; input_schema?: string; output_schema?: string }[];
}

export interface StructureResponse {
  agent_id: string;
  structure_id: string;
  schema_version: string;
  folder: string;
  spec_bytes: number;
  io?: AgentIo;
  spec?: {
    role?: string;
    prompt_reference?: string;
    rubric_reference?: string;
    critique_edges?: { inputs?: string[]; outputs?: string[] };
  };
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

export interface EvalFixtureSource {
  repo?: string;
  file?: string;
  case_id?: string;
  case_name?: string;
  note?: string;
}

export interface EvalFixture {
  id: string;
  filename?: string;
  agent_id?: string;
  path: string;
  honesty?: string;
  schema_version?: string;
  input?: { message?: string; history?: unknown[] };
  expect?: Record<string, unknown>;
  source?: EvalFixtureSource;
}

export interface EvalFixturesResponse {
  agent_id: string;
  honesty: string;
  note?: string;
  fixtures: EvalFixture[];
  provenance?: Record<string, unknown> | null;
}

export interface AgentFileRow {
  path: string;
  bytes: number;
  kind: string;
  writable: boolean;
}

export interface AgentFileFolder {
  name: string;
  present: boolean;
  files: AgentFileRow[];
}

export interface AgentFilesResponse {
  agent_id: string;
  folders: AgentFileFolder[];
  max_bytes?: number;
}

export interface AgentFileItem {
  agent_id: string;
  path: string;
  bytes: number;
  kind: string;
  writable: boolean;
  host_owned?: boolean;
  encoding?: string | null;
  content?: string | null;
  sha256?: string | null;
  saved?: boolean;
  dry_run?: boolean;
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
  chat_adapter?: string;
  chat_adapter_saved?: string | null;
  grok_available?: boolean;
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

export interface RuntimeAdapter {
  agent_id: string;
  kind: string;
  grok_available?: boolean;
  profile_ready?: boolean;
  pid?: number | null;
  session_id?: string | null;
  healthy?: boolean;
  home?: string;
}

export interface ChatLlmView {
  max_tokens?: number;
  max_tokens_source?: string;
  declared_max_output_tokens?: number | null;
  finish_reason?: string;
  content_chars?: number;
  model?: string;
  truncated?: boolean;
  usage?: Record<string, number>;
}

export interface ChatContextSegment {
  name: string;
  budget: number;
  tokens: number;
  clipped: boolean;
  included: boolean;
}

export interface ChatContextPack {
  tokenizer?: string;
  compaction?: string;
  max_input_tokens?: number;
  prompt_reference?: string;
  skills?: { skill_id: string; description?: string }[];
  omitted?: string[];
  segments?: ChatContextSegment[];
  history_turns?: number;
  history_clipped?: boolean;
  system_tokens?: number;
  adapter?: string;
  session_id?: string;
  pid?: number;
}

export interface ChatIoBinding {
  operator_message?: { status?: string; chars?: number };
  chat_history?: { status?: string; turns?: number };
  declared_inputs?: { id: string; status?: string; fetched?: boolean }[];
  declared_inputs_fetched?: boolean;
  declared_outputs?: { id: string; status?: string; applicable?: boolean; reason?: string }[];
  prompt_file?: { reference?: string; digest?: string | null; packed?: boolean };
  system_tokens?: number;
}

export interface ChatProof {
  path_id?: string;
  not_a_dag_run?: boolean;
  agent_id?: string;
  eval?: { verdict?: string; pass?: boolean; reason?: string };
  io_binding?: ChatIoBinding;
  spec_applied?: {
    packed_system?: boolean;
    prompt_reference?: string;
    profile_projected?: boolean;
    dag_executed?: boolean;
  };
  model?: {
    adapter?: string;
    provider?: string;
    folder_model_policy_provider?: string;
    folder_model_policy_used_for_routing?: boolean;
    max_tokens?: number;
    max_tokens_source?: string;
  };
  output?: {
    kind?: string;
    digest?: string;
    finish_reason?: string;
    truncated?: boolean;
    content_chars?: number;
    declared_outputs_produced?: boolean;
  };
  negative?: {
    memory_writes?: unknown[];
    plugins_executed?: boolean;
    t3_enabled?: boolean;
    network_granted?: boolean;
    folder_network_access?: boolean;
  };
  observability?: {
    status?: string;
    reason?: string;
    exporter_declared?: string;
    exporter_wired?: boolean;
    content_capture?: string;
  };
  decision_record?: {
    inputs?: unknown;
    actions?: string[];
    constraints?: string[];
    codes?: unknown[];
    outcomes?: unknown[];
  };
  digest?: string;
  record?: string;
}

export interface ChatResponse {
  agent_id: string;
  reply: string;
  provider: string;
  digest?: string;
  io?: AgentIo;
  memory_writes: unknown[];
  plugins_executed: boolean;
  t3_enabled: boolean;
  used_prompt_reference?: string;
  context?: ChatContextPack;
  llm?: ChatLlmView;
  proof?: ChatProof;
}

export interface CacheStats {
  agent_id?: string;
  entries?: number;
  tiers?: string[];
  t3_enabled?: boolean;
  telemetry?: Record<string, number>;
  false_reuse_rate?: number | null;
}

export interface ProgramSummary {
  id: string;
  code: string;
  name: string;
  phase?: string;
  project_ids?: string[];
  updated_at?: string;
}

export interface ProgramSegment {
  id: string;
  scene_id?: string;
  purpose?: string;
  duration_s?: number;
  status?: string;
  project_slug?: string;
}

export interface ProgramScene {
  id: string;
  title?: string;
  segments?: ProgramSegment[];
}

export interface ProgramRecord {
  id: string;
  code: string;
  name: string;
  folder?: string;
  honesty?: string;
  saved?: boolean;
  dry_run?: boolean;
  created_at?: string;
  updated_at?: string;
  first_called?: string;
  first_agent_hop?: string;
  phase?: string;
  locks?: Record<string, boolean>;
  generation_list?: { scenes?: ProgramScene[] };
  project_ids?: string[];
  generation_list_ref?: string;
  sequence_ref?: string;
  bible_ref?: string;
  storyboard_ref?: string;
  delivery_ref?: string;
  cut_state?: string;
  graph?: { nodes?: unknown[]; edges?: unknown[] };
  preview?: { slug: string; scene_id: string; segment_id: string; purpose?: string }[];
  spawned?: number;
  finish?: string;
  fused_request?: null;
}

export interface ProgramCommItem {
  id: string;
  from: string;
  to: string;
  kind: string;
  text?: string;
  pass_id?: string;
  live?: boolean;
  created_at?: string;
}

export interface ProgramComms {
  program_id?: string;
  first_called?: string;
  first_agent_hop?: string;
  child_first_called?: string;
  child_human_locks?: string[];
  honesty?: string;
  items?: ProgramCommItem[];
  graph?: { nodes?: unknown[]; edges?: unknown[] };
}

export interface ProgramSequencePayload {
  sequence?: {
    kind?: string;
    concat?: string;
    fused_request?: null;
    clips?: { clip_id?: string; path?: string }[];
  };
  compile?: { fused_request?: null; concat?: string };
}

export interface ProjectSummary {
  id: string;
  name?: string;
  title?: string;
  sub_workflow_id?: string | null;
  updated_at?: string;
}

export interface ProjectCatalogItem {
  id: string;
  kind: string;
  code: string;
  label: string;
  use: string;
}

export interface ProjectSuggestionRow {
  id: string;
  label: string;
  kind: string;
  reason: string;
  rank: number;
  source: string;
}

export interface ProjectSuggestion {
  honesty: string;
  llm_used: boolean;
  primary: string;
  suggestions: ProjectSuggestionRow[];
  llm_excerpt?: string;
  note?: string;
  prompt?: string;
  adapter?: string;
  catalog?: ProjectCatalogItem[];
}

export interface ProjectNextRow {
  id: string;
  label: string;
  kind: string;
  role?: string;
  inputs: string[];
  outputs: string[];
  contract: string[];
  reason: string;
  rank: number;
  source: string;
  loopback?: boolean;
}

export interface ProjectNextSuggestion {
  honesty: string;
  llm_used: boolean;
  from_id: string;
  from_agent_id?: string | null;
  out_bus?: string | null;
  outs?: string[];
  parent_chat_id?: string;
  primary: string;
  suggestions: ProjectNextRow[];
  note?: string;
  prompt?: string;
  adapter?: string;
  llm_excerpt?: string;
}

export interface ProjectCommTag {
  project_id: string;
  node_id: string;
  comm_id: string;
  label: string;
}

export interface ProjectDecisionOption {
  id: string;
  label: string;
  why?: string;
}

export interface ProjectDecision {
  id: string;
  agent_id: string;
  node_id?: string;
  point: string;
  thinking?: string;
  options: ProjectDecisionOption[];
  recommend?: string;
  chosen?: string;
  decide_by?: string;
  selected_by?: string;
  select_reason?: string;
}

export interface ProjectMedia {
  name?: string;
  kind: string;
  path?: string;
  url: string;
  poster?: string;
}

export interface ProjectGeneratorTag {
  id: string;
  label: string;
  engine: string;
  live: boolean;
  configured?: boolean;
  why?: string;
}

export interface ProjectVideoConfig {
  engine?: string;
  mode?: string;
  aspect_ratio?: string;
  duration?: number;
  resolution?: string;
  image_model?: string;
  video_model?: string;
  image_resolution?: string;
}

export interface ProjectCommItem {
  id: string;
  node_id: string;
  from: string;
  to: string;
  kind: string;
  text: string;
  input_tags: ProjectCommTag[];
  output_tags: ProjectCommTag[];
  pass_id?: string;
  created_at?: string;
  live?: boolean;
  provider?: string;
  error?: string;
  agents?: string[];
  media?: ProjectMedia | null;
}

export interface ProjectCommsPayload {
  schema_version?: string;
  project_id?: string;
  items: ProjectCommItem[];
  decisions?: ProjectDecision[];
  walkthrough?: string;
  honesty?: string;
  note?: string;
  saved?: boolean;
  dry_run?: boolean;
  locks?: Record<string, string>;
  autopilot?: {
    status?: string;
    human_roles?: string[];
    locks_selected?: number;
    intent_agent?: string;
    creative_agent?: string;
    cycle?: string;
    cycles?: number;
    cycle_locks?: Record<string, string>;
  };
}

export interface CompileCoverageRow {
  requirement?: string;
  disposition?: string;
  path?: string;
  implementation?: string;
}

export interface CompileDiagnostic {
  code?: string;
  agent_id?: string;
  path?: string;
  severity?: string;
  message?: string;
}

export interface CompileSnapshot {
  status?: string;
  compiler_version?: string;
  profile_id?: string;
  generator_tag?: string;
  live?: boolean;
  mode?: string;
  prompt?: { still?: string; motion?: string };
  request?: Record<string, unknown>;
  coverage?: CompileCoverageRow[];
  diagnostics?: CompileDiagnostic[];
  proposal?: { live?: boolean; message?: string } | null;
  guide?: string | null;
}

export interface OutputSection {
  heading: string;
  owner?: string;
  path?: string;
  body?: string;
}

export interface SequenceClipRow {
  clip_id: string;
  order: number;
  start_s?: number;
  end_s?: number;
  path?: string;
  role?: string;
  logline?: string;
}

export interface SequenceManifest {
  kind?: string;
  sequence_id?: string;
  project_id?: string;
  intent?: { logline?: string };
  clips: SequenceClipRow[];
  delivery?: { timeline_duration_s?: number; in_s?: number; out_s?: number };
  policy?: { generation_unit?: string; one_pass_one_clip?: boolean; concat?: string };
}

export interface ProjectOutputPayload {
  path: string;
  exists: boolean;
  text: string;
  honesty?: string;
  media?: ProjectMedia[];
  generators?: ProjectGeneratorTag[];
  video_config?: ProjectVideoConfig;
  canonical_exists?: boolean;
  clip_source?: string;
  compile_note?: string;
  compiled?: CompileSnapshot | null;
  critic_warnings?: CompileDiagnostic[];
  sections?: OutputSection[];
  sequence?: SequenceManifest | null;
  sequence_compile?: {
    status?: string;
    sequence_id?: string;
    fused_request?: null;
    clips?: { clip_id?: string; status?: string; compiled?: CompileSnapshot | null }[];
    note?: string;
  } | null;
  clip_id?: string;
}

export interface ProjectGenerateResult {
  honesty?: string;
  engine?: string;
  live?: boolean;
  error?: string;
  config?: ProjectVideoConfig;
  media?: ProjectMedia[];
  comms?: ProjectCommsPayload;
  compiled?: CompileSnapshot | null;
  clip_source?: string;
  clip_id?: string;
  note?: string;
}

export interface ProjectRunResult {
  honesty: string;
  dry_run?: boolean;
  saved?: boolean;
  first_called?: string;
  comms?: ProjectCommsPayload;
  graph?: { nodes: unknown[]; edges: unknown[] };
  output_path?: string;
  validation?: {
    matched?: boolean;
    exact?: boolean;
    copied_sample?: boolean;
    missing_markers?: string[];
    missing_sections?: string[];
  };
  live_hops?: number;
  live?: boolean;
  section_sources?: Record<string, string>;
  conflicts?: string[];
  human_asks?: string[];
  dispatch_ids?: string[];
  creative_why?: string;
  status?: string;
  note?: string;
}

export interface ProjectStartSnapshot {
  name?: string;
  title?: string;
  brief?: string;
  audience?: string;
  duration?: string;
  outlets?: string;
  risk?: string;
  notes?: string;
  sub_workflow_id?: string;
  suggestion?: ProjectSuggestion | null;
  saved_at?: string;
  source?: string;
  inherit?: Record<string, unknown>;
}

export interface ProjectRecord {
  id: string;
  name: string;
  title: string;
  brief: string;
  audience?: string;
  duration?: string;
  outlets?: string;
  risk?: string;
  notes?: string;
  group?: string;
  sub_workflow_id?: string;
  suggestion?: ProjectSuggestion | null;
  start?: ProjectStartSnapshot | null;
  start_persisted?: boolean;
  graph?: { nodes: unknown[]; edges: unknown[] };
  honesty?: string;
  saved?: boolean;
  dry_run?: boolean;
  folder?: string;
  inherit?: Record<string, unknown>;
}
