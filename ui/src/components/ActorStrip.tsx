import { Lock } from "lucide-react";
import { ACTORS } from "../api/types";
import { useSession } from "../state/session";
import { Card, Field, inputClass } from "./ui";

export function OperatorContractFields() {
  const session = useSession();
  const reasonMissing = !session.reason.trim();
  return (
    <Card>
      <div data-testid="operator-contract">
        <h2 className="mb-1 text-sm font-semibold text-stone-900">Operator contract</h2>
        <p className="mb-4 text-xs text-stone-500">
          Actor, reason, and expected parent are sent as mutation headers. Set them here on Overview.
        </p>
        <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
          <Field label="Actor">
            <select
              id="actor-select"
              className={`${inputClass} w-full`}
              value={session.actor}
              onChange={(event) => session.setActor(event.target.value as typeof session.actor)}
            >
              {ACTORS.map((actor) => (
                <option key={actor} value={actor}>
                  {actor}
                </option>
              ))}
            </select>
          </Field>
          <Field label="Reason" hint={reasonMissing ? "required for mutations" : undefined}>
            <input
              id="actor-reason"
              className={`${inputClass} w-full`}
              placeholder="why this change"
              title={reasonMissing ? "required for mutations" : undefined}
              value={session.reason}
              onChange={(event) => session.setReason(event.target.value)}
            />
          </Field>
          <Field label="Expected parent">
            <input
              id="actor-expected-parent"
              className={`${inputClass} w-full font-mono`}
              value={session.expectedParent}
              onChange={(event) => session.setExpectedParent(event.target.value)}
            />
          </Field>
        </div>
      </div>
    </Card>
  );
}

export function DryRunControl() {
  const session = useSession();
  return (
    <label
      data-testid="dry-run"
      className="inline-flex h-9 items-center gap-1.5 rounded-full border border-stone-200 bg-white px-3 text-xs font-medium text-stone-700"
      title={
        session.dryRun
          ? "Dry-run still executes the DAG — this is not “no side effects”."
          : "Mutations persist when the host accepts them."
      }
    >
      <input
        id="dry-run-toggle"
        type="checkbox"
        checked={session.dryRun}
        onChange={(event) => session.setDryRun(event.target.checked)}
      />
      Dry-run
      {session.dryRun ? <Lock size={12} className="text-indigo-600" aria-hidden="true" /> : null}
    </label>
  );
}
