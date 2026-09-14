import type { ButtonHTMLAttributes } from "react";
import { Panel } from "@xyflow/react";

const buttonClass =
  "inline-flex items-center justify-center rounded-md border border-stone-200 bg-white px-2.5 py-1 text-[11px] font-medium text-stone-700 shadow-sm hover:border-indigo-300 hover:bg-indigo-50 hover:text-indigo-800 disabled:cursor-not-allowed disabled:opacity-40 dark:border-[#111] dark:bg-[#353535] dark:text-[#ddd] dark:hover:border-[#64b5f6] dark:hover:bg-[#454545]";

export function AutoLayoutButton({
  testId = "graph-auto-layout",
  children,
  className,
  ...props
}: ButtonHTMLAttributes<HTMLButtonElement> & { testId?: string }) {
  return (
    <button type="button" data-testid={testId} className={`${buttonClass} ${className ?? ""}`} {...props}>
      {children ?? "Auto layout"}
    </button>
  );
}

export function AutoLayoutPanel({
  onLayout,
  disabled,
  testId,
}: {
  onLayout: () => void;
  disabled?: boolean;
  testId?: string;
}) {
  return (
    <Panel position="top-right" className="m-2">
      <AutoLayoutButton testId={testId} disabled={disabled} onClick={onLayout}>
        Auto layout
      </AutoLayoutButton>
    </Panel>
  );
}
