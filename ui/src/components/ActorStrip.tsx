import { Lock } from "lucide-react";
import { ACTORS } from "../api/types";
import { useSession } from "../state/session";
import { inputClass } from "./ui";

const labelClass = "flex h-4 items-center text-xs font-medium text-stone-700";

export function ActorStrip() {
  const session = useSession();
  const reasonMissing = !session.reason.trim();
  return (
    <div className="flex min-w-0 flex-1 flex-wrap items-end gap-x-3 gap-y-1">
      <label className="flex w-[11.5rem] shrink-0 flex-col gap-1" htmlFor="actor-select">
        <span className={labelClass}>Actor</span>
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
      </label>
      <label className="flex min-w-[8rem] flex-1 flex-col gap-1" htmlFor="actor-reason">
        <span className={labelClass}>Reason</span>
        <input
          id="actor-reason"
          aria-describedby="actor-reason-hint"
          className={`${inputClass} w-full`}
          placeholder="why this change"
          title={reasonMissing ? "required for mutations" : undefined}
          value={session.reason}
          onChange={(event) => session.setReason(event.target.value)}
        />
        <span id="actor-reason-hint" className="sr-only">
          {reasonMissing ? "required for mutations" : ""}
        </span>
      </label>
      <label className="flex w-[9rem] shrink-0 flex-col gap-1" htmlFor="actor-expected-parent">
        <span className={labelClass}>Expected parent</span>
        <input
          id="actor-expected-parent"
          className={`${inputClass} w-full font-mono`}
          value={session.expectedParent}
          onChange={(event) => session.setExpectedParent(event.target.value)}
        />
      </label>
      <div className="flex shrink-0 flex-col gap-1">
        <span className={labelClass} aria-hidden="true" />
        <label className="flex h-9 items-center gap-1.5 text-xs font-medium text-stone-700">
          <input
            type="checkbox"
            checked={session.dryRun}
            onChange={(event) => session.setDryRun(event.target.checked)}
          />
          Dry-run
          {session.dryRun ? <Lock size={12} className="text-indigo-600" aria-hidden="true" /> : null}
        </label>
      </div>
    </div>
  );
}
