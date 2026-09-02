import { StatusPill } from "./StatusPill";
import { CasopsHttpError } from "../api/types";

export function RecoveryBanner({
  error,
  onReload,
}: {
  error: CasopsHttpError | null;
  onReload?: () => void;
}) {
  if (!error?.containment_required) {
    return null;
  }
  return (
    <div className="mb-4 flex flex-col gap-3 rounded-2xl border border-amber-200 bg-amber-50 px-4 py-3 sm:flex-row sm:items-center sm:justify-between">
      <div>
        <div className="mb-1 flex items-center gap-2">
          <StatusPill status="recovery" />
          <span className="font-mono text-xs text-amber-800">{error.code}</span>
        </div>
        <p className="text-sm text-amber-900">{error.message}</p>
        <p className="mt-1 text-xs text-amber-700">Mutations other than Reload attestation are disabled until the host recovers.</p>
      </div>
      {onReload ? (
        <button
          type="button"
          onClick={onReload}
          className="rounded-full bg-stone-900 px-4 py-2 text-xs font-medium text-white dark:bg-stone-100 dark:text-stone-900"
        >
          Reload attestation
        </button>
      ) : null}
    </div>
  );
}

export function ErrorBanner({ error }: { error: CasopsHttpError | Error | null }) {
  if (!error) {
    return null;
  }
  const code = error instanceof CasopsHttpError ? error.code : "ERROR";
  return (
    <div className="mb-4 rounded-2xl border border-red-200 bg-red-50 px-4 py-3">
      <p className="font-mono text-xs text-red-700">{code}</p>
      <p className="mt-1 text-sm text-red-900">{error.message}</p>
    </div>
  );
}
