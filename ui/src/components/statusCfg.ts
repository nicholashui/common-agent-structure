export type StatusKind =
  | "live"
  | "running"
  | "queued"
  | "self_refine"
  | "delayed"
  | "reconnecting"
  | "degraded"
  | "failed"
  | "recovery"
  | "complete"
  | "unavailable"
  | "stale"
  | "cancelled";

export const STATUS_CFG: Record<
  StatusKind,
  { bg: string; border: string; text: string; dot: string; pulse: boolean; label: string }
> = {
  live: { bg: "bg-emerald-50 dark:bg-emerald-950", border: "border-emerald-200 dark:border-emerald-800", text: "text-emerald-700 dark:text-emerald-300", dot: "bg-emerald-500", pulse: true, label: "Live" },
  running: { bg: "bg-blue-50 dark:bg-blue-950", border: "border-blue-200 dark:border-blue-800", text: "text-blue-700 dark:text-blue-300", dot: "bg-blue-500", pulse: true, label: "Running" },
  queued: { bg: "bg-violet-50 dark:bg-violet-950", border: "border-violet-200 dark:border-violet-800", text: "text-violet-700 dark:text-violet-300", dot: "bg-violet-500", pulse: false, label: "Queued" },
  self_refine: { bg: "bg-purple-50 dark:bg-purple-950", border: "border-purple-200 dark:border-purple-800", text: "text-purple-700 dark:text-purple-300", dot: "bg-purple-500", pulse: true, label: "Self-Refining" },
  delayed: { bg: "bg-yellow-50 dark:bg-yellow-950", border: "border-yellow-200 dark:border-yellow-800", text: "text-yellow-700 dark:text-yellow-300", dot: "bg-yellow-500", pulse: false, label: "Delayed" },
  reconnecting: { bg: "bg-orange-50 dark:bg-orange-950", border: "border-orange-200 dark:border-orange-800", text: "text-orange-700 dark:text-orange-300", dot: "bg-orange-500", pulse: true, label: "Reconnecting" },
  degraded: { bg: "bg-red-50 dark:bg-red-950", border: "border-red-200 dark:border-red-800", text: "text-red-700 dark:text-red-300", dot: "bg-red-500", pulse: false, label: "Degraded" },
  failed: { bg: "bg-red-50 dark:bg-red-950", border: "border-red-200 dark:border-red-800", text: "text-red-700 dark:text-red-300", dot: "bg-red-600", pulse: false, label: "Failed" },
  recovery: { bg: "bg-amber-50 dark:bg-amber-950", border: "border-amber-200 dark:border-amber-800", text: "text-amber-700 dark:text-amber-300", dot: "bg-amber-500", pulse: true, label: "Recovery" },
  complete: { bg: "bg-emerald-50 dark:bg-emerald-950", border: "border-emerald-200 dark:border-emerald-800", text: "text-emerald-700 dark:text-emerald-300", dot: "bg-emerald-500", pulse: false, label: "Complete" },
  unavailable: { bg: "bg-stone-100 dark:bg-stone-800", border: "border-stone-200 dark:border-stone-600", text: "text-stone-500 dark:text-stone-400", dot: "bg-stone-400", pulse: false, label: "Unavailable" },
  stale: { bg: "bg-stone-100 dark:bg-stone-800", border: "border-stone-200 dark:border-stone-600", text: "text-stone-400 dark:text-stone-500", dot: "bg-stone-300 dark:bg-stone-500", pulse: false, label: "Stale" },
  cancelled: { bg: "bg-stone-100 dark:bg-stone-800", border: "border-stone-200 dark:border-stone-600", text: "text-stone-500 dark:text-stone-400", dot: "bg-stone-400", pulse: false, label: "Cancelled" },
};
