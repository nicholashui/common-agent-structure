import type { ButtonHTMLAttributes } from "react";
import { Panel } from "@xyflow/react";
import { DEFAULT_LAYOUT_ALGORITHM, LAYOUT_ALGORITHMS, type LayoutAlgorithm } from "../lib/autoLayout";

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

export function AutoLayoutMenu({
  onLayout,
  disabled,
  testId = "graph-auto-layout",
}: {
  onLayout: (algorithm: LayoutAlgorithm) => void;
  disabled?: boolean;
  testId?: string;
}) {
  if (disabled) {
    return (
      <button type="button" data-testid={testId} className={buttonClass} disabled>
        Auto layout
      </button>
    );
  }
  return (
    <details className="relative" data-testid={testId}>
      <summary
        className={`${buttonClass} cursor-pointer list-none [&::-webkit-details-marker]:hidden`}
        data-testid={`${testId}-toggle`}
        aria-label="Auto layout options"
      >
        Auto layout
      </summary>
      <ul
        role="menu"
        className="absolute right-0 z-30 mt-1 min-w-[13.5rem] rounded-md border border-stone-200 bg-white py-1 shadow-lg dark:border-[#111] dark:bg-[#2b2b2b]"
        data-testid={`${testId}-menu`}
      >
        {LAYOUT_ALGORITHMS.map((row) => (
          <li key={row.id} role="none">
            <button
              type="button"
              role="menuitem"
              data-testid={`${testId}-${row.id}`}
              data-default={row.id === DEFAULT_LAYOUT_ALGORITHM ? "true" : undefined}
              aria-label={`${row.label}. ${row.hint}`}
              className="flex w-full flex-col items-start px-3 py-1.5 text-left hover:bg-indigo-50 dark:hover:bg-[#3a3a3a]"
              onClick={(event) => {
                const root = (event.currentTarget.closest("details") as HTMLDetailsElement | null);
                if (root) {
                  root.open = false;
                }
                onLayout(row.id);
              }}
            >
              <span className="text-[11px] font-medium text-stone-800 dark:text-[#eee]">{row.label}</span>
              <span className="text-[10px] text-stone-500 dark:text-[#999]">{row.hint}</span>
            </button>
          </li>
        ))}
      </ul>
    </details>
  );
}

export function AutoLayoutPanel({
  onLayout,
  disabled,
  testId,
}: {
  onLayout: (algorithm: LayoutAlgorithm) => void;
  disabled?: boolean;
  testId?: string;
}) {
  return (
    <Panel position="top-right" className="m-2">
      <AutoLayoutMenu testId={testId} disabled={disabled} onLayout={onLayout} />
    </Panel>
  );
}
