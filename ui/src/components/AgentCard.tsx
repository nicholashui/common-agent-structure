import { Bot } from "lucide-react";
import { Link } from "react-router-dom";
import { CommonBadge } from "./CommonBadge";
import { StatusPill } from "./StatusPill";
import type { StatusKind } from "./statusCfg";
import { GhostButton, PrimaryButton } from "./ui";

export interface AgentCardModel {
  agent_id: string;
  folder?: string;
  role?: string;
  schema_version?: string;
  compose_hash?: string;
  runStatus?: StatusKind;
  memoryMode?: string;
  va_category?: string;
}

export function AgentCard({
  agent,
  onCompose,
}: {
  agent: AgentCardModel;
  onCompose?: () => void;
}) {
  const href = `/agents/${encodeURIComponent(agent.agent_id)}`;
  return (
    <article className="rounded-2xl border border-stone-200 bg-white p-5 transition hover:shadow-md">
      <div className="flex items-start gap-3">
        <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-indigo-50 text-indigo-600">
          <Bot size={18} />
        </div>
        <div className="min-w-0 flex-1">
          <div className="flex flex-wrap items-center gap-2">
            <h2 className="truncate text-sm font-semibold text-stone-900">{agent.agent_id}</h2>
            <CommonBadge version={agent.schema_version || "3.0"} hash={agent.compose_hash} />
          </div>
          <p className="mt-1 truncate text-sm text-stone-500">
            {agent.role || "unspecified role"}
            {agent.folder ? ` · ${agent.folder}` : ""}
          </p>
        </div>
      </div>
      <dl className="mt-4 grid grid-cols-3 gap-3 text-xs">
        <div className="rounded-xl bg-stone-50 px-3 py-2">
          <dt className="text-stone-500">compose</dt>
          <dd className="mt-1 truncate font-mono text-stone-900">{agent.compose_hash ? agent.compose_hash.slice(0, 8) : "—"}</dd>
        </div>
        <div className="rounded-xl bg-stone-50 px-3 py-2">
          <dt className="text-stone-500">last run</dt>
          <dd className="mt-1">
            <StatusPill status={agent.runStatus ?? "unavailable"} />
          </dd>
        </div>
        <div className="rounded-xl bg-stone-50 px-3 py-2">
          <dt className="text-stone-500">memory</dt>
          <dd className="mt-1 font-mono text-stone-900">{agent.memoryMode || "—"}</dd>
        </div>
      </dl>
      <div className="mt-4 flex flex-wrap gap-2">
        <Link to={href}>
          <PrimaryButton type="button">Open</PrimaryButton>
        </Link>
        <GhostButton type="button" onClick={onCompose}>
          Compose preview
        </GhostButton>
      </div>
    </article>
  );
}
