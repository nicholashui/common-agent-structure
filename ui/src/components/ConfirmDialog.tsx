import type { ReactNode } from "react";
import { GhostButton, PrimaryButton } from "./ui";

export function ConfirmDialog({
  open,
  title,
  body,
  confirmLabel = "Confirm",
  onCancel,
  onConfirm,
}: {
  open: boolean;
  title: string;
  body: ReactNode;
  confirmLabel?: string;
  onCancel: () => void;
  onConfirm: () => void;
}) {
  if (!open) {
    return null;
  }
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-stone-900/30 p-4">
      <div role="dialog" aria-modal="true" className="w-full max-w-md rounded-2xl border border-stone-200 bg-white p-5 shadow-lg">
        <h2 className="text-lg font-semibold text-stone-900">{title}</h2>
        <div className="mt-3 text-sm text-stone-600">{body}</div>
        <div className="mt-5 flex justify-end gap-2">
          <GhostButton type="button" onClick={onCancel}>
            Cancel
          </GhostButton>
          <PrimaryButton type="button" onClick={onConfirm}>
            {confirmLabel}
          </PrimaryButton>
        </div>
      </div>
    </div>
  );
}
