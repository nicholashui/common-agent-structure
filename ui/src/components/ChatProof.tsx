import type { ChatProof } from "../api/types";
import { Card } from "./ui";

function Flag({ ok, label }: { ok: boolean; label: string }) {
  return (
    <li className="font-mono text-[11px] text-stone-700">
      {label}: {ok ? "yes" : "no"}
    </li>
  );
}

export function ChatProofPanel({ proof }: { proof: ChatProof }) {
  const binding = proof.io_binding;
  const inputs = binding?.declared_inputs ?? [];
  const evalPass = proof.eval?.pass === true;
  return (
    <Card>
      <div data-testid="chat-proof">
        <h2 className="mb-1 text-sm font-semibold text-stone-900">Chat proof</h2>
        <p className="mb-3 text-xs text-stone-500">
          Path <span className="font-mono">{proof.path_id ?? "chat"}</span>
          {proof.not_a_dag_run ? " · not a DAG run" : ""}. Packed folder spec was applied. This is not an eval pass.
        </p>
        <ul className="space-y-1">
          <li className="font-mono text-[11px] text-stone-700" data-testid="chat-proof-eval">
            eval {proof.eval?.verdict ?? "NOT_RUN"}
            {evalPass ? " · PASS (unexpected)" : " · not a pass"}
          </li>
          <li className="font-mono text-[11px] text-stone-700" data-testid="chat-proof-model">
            adapter {proof.model?.adapter ?? "—"} · provider {proof.model?.provider ?? "—"} · folder policy{" "}
            {proof.model?.folder_model_policy_provider || "—"}
            {proof.model?.folder_model_policy_used_for_routing ? "" : " (not used for routing)"}
          </li>
          <li className="font-mono text-[11px] text-stone-700">
            operator message {binding?.operator_message?.status ?? "—"}
            {binding?.operator_message?.chars != null ? ` · ${binding.operator_message.chars} chars` : ""} · history{" "}
            {binding?.chat_history?.status ?? "empty"}
            {binding?.chat_history?.turns != null ? ` · ${binding.chat_history.turns} turns` : ""}
          </li>
          <li className="font-mono text-[11px] text-stone-700" data-testid="chat-proof-io">
            declared inputs fetched: {binding?.declared_inputs_fetched ? "yes" : "no"}
            {inputs.length ? ` · ${inputs.map((row) => `${row.id} name-only`).join(", ")}` : " · none declared"}
          </li>
          <li className="font-mono text-[11px] text-stone-700">
            output {proof.output?.kind ?? "reply"} · {proof.output?.content_chars ?? 0} chars · declared buses produced:{" "}
            {proof.output?.declared_outputs_produced ? "yes" : "no"}
          </li>
          <Flag ok={Boolean(proof.spec_applied?.packed_system)} label="packed system" />
          <Flag ok={Boolean(proof.negative?.plugins_executed)} label="plugins" />
          <Flag ok={Boolean(proof.negative?.t3_enabled)} label="T3" />
          <Flag ok={Boolean(proof.negative?.network_granted)} label="network grant" />
          <li className="font-mono text-[11px] text-stone-700" data-testid="chat-proof-obs">
            observability {proof.observability?.status ?? "NOT_APPLIED"}
            {proof.observability?.exporter_declared ? ` · declared ${proof.observability.exporter_declared}` : ""}
            {proof.observability?.exporter_wired ? "" : " · not wired"}
          </li>
        </ul>
      </div>
    </Card>
  );
}
