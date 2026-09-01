import { STATUS_CFG, type StatusKind } from "./statusCfg";

export function StatusPill({ status }: { status: StatusKind }) {
  const cfg = STATUS_CFG[status] ?? STATUS_CFG.stale;
  return (
    <span
      className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium border ${cfg.bg} ${cfg.border} ${cfg.text}`}
    >
      <span className={`w-1.5 h-1.5 rounded-full ${cfg.dot} ${cfg.pulse ? "animate-pulse" : ""}`} />
      {cfg.label}
    </span>
  );
}
