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
  live: { bg: "bg-emerald-50", border: "border-emerald-200", text: "text-emerald-700", dot: "bg-emerald-500", pulse: true, label: "Live" },
  running: { bg: "bg-blue-50", border: "border-blue-200", text: "text-blue-700", dot: "bg-blue-500", pulse: true, label: "Running" },
  queued: { bg: "bg-violet-50", border: "border-violet-200", text: "text-violet-700", dot: "bg-violet-500", pulse: false, label: "Queued" },
  self_refine: { bg: "bg-purple-50", border: "border-purple-200", text: "text-purple-700", dot: "bg-purple-500", pulse: true, label: "Self-Refining" },
  delayed: { bg: "bg-yellow-50", border: "border-yellow-200", text: "text-yellow-700", dot: "bg-yellow-500", pulse: false, label: "Delayed" },
  reconnecting: { bg: "bg-orange-50", border: "border-orange-200", text: "text-orange-700", dot: "bg-orange-500", pulse: true, label: "Reconnecting" },
  degraded: { bg: "bg-red-50", border: "border-red-200", text: "text-red-700", dot: "bg-red-500", pulse: false, label: "Degraded" },
  failed: { bg: "bg-red-50", border: "border-red-200", text: "text-red-700", dot: "bg-red-600", pulse: false, label: "Failed" },
  recovery: { bg: "bg-amber-50", border: "border-amber-200", text: "text-amber-700", dot: "bg-amber-500", pulse: true, label: "Recovery" },
  complete: { bg: "bg-emerald-50", border: "border-emerald-200", text: "text-emerald-700", dot: "bg-emerald-500", pulse: false, label: "Complete" },
  unavailable: { bg: "bg-stone-100", border: "border-stone-200", text: "text-stone-500", dot: "bg-stone-400", pulse: false, label: "Unavailable" },
  stale: { bg: "bg-stone-100", border: "border-stone-200", text: "text-stone-400", dot: "bg-stone-300", pulse: false, label: "Stale" },
  cancelled: { bg: "bg-stone-100", border: "border-stone-200", text: "text-stone-500", dot: "bg-stone-400", pulse: false, label: "Cancelled" },
};
