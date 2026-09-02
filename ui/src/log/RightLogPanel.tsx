import { useEffect, useRef, useState } from "react";
import { X } from "lucide-react";
import {
  HELP_WIDTH_MAX,
  HELP_WIDTH_MIN,
  HELP_WIDTH_STEP,
  HELP_WIDTH_STEP_LARGE,
  clampHelpWidth,
} from "../help/paths";
import { LOG_SESSION_ID, snapshot, subscribe, type LogChannel, type LogEntry } from "./bus";
import { logFilesSnapshot, subscribeLogFiles, type LogFiles } from "./persist";

const TABS: { id: LogChannel; label: string }[] = [
  { id: "api", label: "API log" },
  { id: "ui", label: "UI log" },
];

function fileLabel(path: string | undefined): string {
  if (!path) {
    return "pending";
  }
  return path.replace(/\\/g, "/").split("/").slice(-2).join("/");
}

export function RightLogPanel({
  width,
  dragging,
  onClose,
  onWidthChange,
  onDraggingChange,
}: {
  width: number;
  dragging: boolean;
  onClose: () => void;
  onWidthChange: (width: number, persist?: boolean) => void;
  onDraggingChange: (dragging: boolean) => void;
}) {
  const [tab, setTab] = useState<LogChannel>("api");
  const [entries, setEntries] = useState<LogEntry[]>(() => snapshot("api"));
  const [files, setFiles] = useState<LogFiles>(logFilesSnapshot);
  const scroller = useRef<HTMLPreElement>(null);
  const stick = useRef(true);
  const drag = useRef<{ startX: number; startWidth: number } | null>(null);
  const widthRef = useRef(width);
  widthRef.current = width;

  useEffect(() => {
    setEntries(snapshot(tab));
    return subscribe((channel, next) => {
      if (channel === tab) {
        setEntries(next);
      }
    });
  }, [tab]);

  useEffect(() => subscribeLogFiles(setFiles), []);

  useEffect(() => {
    const node = scroller.current;
    if (node && stick.current) {
      node.scrollTop = node.scrollHeight;
    }
  }, [entries]);

  useEffect(() => {
    function onMove(event: PointerEvent) {
      const session = drag.current;
      if (!session) {
        return;
      }
      onWidthChange(session.startWidth + (session.startX - event.clientX));
    }
    function onUp() {
      if (!drag.current) {
        return;
      }
      drag.current = null;
      onDraggingChange(false);
      document.body.style.cursor = "";
      document.body.style.userSelect = "";
      onWidthChange(widthRef.current, true);
    }
    window.addEventListener("pointermove", onMove);
    window.addEventListener("pointerup", onUp);
    window.addEventListener("pointercancel", onUp);
    return () => {
      window.removeEventListener("pointermove", onMove);
      window.removeEventListener("pointerup", onUp);
      window.removeEventListener("pointercancel", onUp);
    };
  }, [onDraggingChange, onWidthChange]);

  function beginDrag(event: React.PointerEvent<HTMLDivElement>) {
    event.preventDefault();
    drag.current = { startX: event.clientX, startWidth: width };
    onDraggingChange(true);
    document.body.style.cursor = "col-resize";
    document.body.style.userSelect = "none";
  }

  function onKeyResize(event: React.KeyboardEvent<HTMLDivElement>) {
    const step = event.shiftKey ? HELP_WIDTH_STEP_LARGE : HELP_WIDTH_STEP;
    if (event.key === "ArrowLeft") {
      event.preventDefault();
      onWidthChange(width + step, true);
    } else if (event.key === "ArrowRight") {
      event.preventDefault();
      onWidthChange(width - step, true);
    } else if (event.key === "Home") {
      event.preventDefault();
      onWidthChange(HELP_WIDTH_MAX, true);
    } else if (event.key === "End") {
      event.preventDefault();
      onWidthChange(HELP_WIDTH_MIN, true);
    }
  }

  const clamped = clampHelpWidth(width);

  return (
    <aside
      className={`sticky top-14 z-20 flex h-[calc(100dvh-8rem)] min-h-0 shrink-0 flex-col self-start overflow-hidden border-l border-stone-200 bg-white md:h-[calc(100vh-3.5rem)] ${dragging ? "" : "transition-[width] duration-150"}`}
      style={{ width: clamped }}
      data-testid="log-drawer"
    >
      <div
        role="separator"
        aria-orientation="vertical"
        aria-label="Resize log panel"
        aria-valuemin={HELP_WIDTH_MIN}
        aria-valuemax={HELP_WIDTH_MAX}
        aria-valuenow={clamped}
        tabIndex={0}
        data-testid="log-resize"
        className="absolute inset-y-0 left-0 z-10 w-1.5 cursor-col-resize hover:bg-indigo-200"
        onPointerDown={beginDrag}
        onKeyDown={onKeyResize}
      />
      <div className="flex items-center justify-between gap-2 border-b border-stone-200 px-3 py-2">
        <h2 className="text-sm font-semibold text-stone-800">Logs</h2>
        <button
          type="button"
          className="rounded-lg p-1.5 text-stone-500 hover:bg-stone-100 hover:text-stone-900"
          aria-label="Close log panel"
          data-testid="log-drawer-close"
          onClick={onClose}
        >
          <X size={16} />
        </button>
      </div>
      <div className="flex flex-wrap gap-1 border-b border-stone-200 px-3 py-2" role="tablist" aria-label="Log channel">
        {TABS.map((item) => {
          const selected = item.id === tab;
          return (
            <button
              key={item.id}
              type="button"
              role="tab"
              aria-selected={selected}
              className={`rounded-full px-3 py-1 text-xs font-medium ${
                selected
                  ? "bg-stone-900 text-white dark:bg-stone-100 dark:text-stone-900"
                  : "bg-stone-100 text-stone-600 hover:bg-stone-200"
              }`}
              data-testid={`log-tab-${item.id}`}
              onClick={() => setTab(item.id)}
            >
              {item.label}
            </button>
          );
        })}
      </div>
      <pre
        ref={scroller}
        data-testid="log-stream"
        className="min-h-0 flex-1 overflow-auto px-3 py-2 font-mono text-[11px] leading-5 text-stone-800"
        onScroll={(event) => {
          const node = event.currentTarget;
          stick.current = node.scrollHeight - node.scrollTop - node.clientHeight < 32;
        }}
      >
        {entries.length ? (
          entries.map((entry) => (
            <LogLine key={entry.id} entry={entry} />
          ))
        ) : (
          <span className="text-stone-400">No {tab === "api" ? "API" : "UI"} log lines yet.</span>
        )}
      </pre>
      <p className="border-t border-stone-200 px-3 py-2 font-mono text-[10px] text-stone-500">
        session {LOG_SESSION_ID}
        <br />
        {tab === "api" ? fileLabel(files.api) : fileLabel(files.ui)}
      </p>
    </aside>
  );
}

function LogLine({ entry }: { entry: LogEntry }) {
  const color =
    entry.level === "error" ? "text-red-700" : entry.level === "warn" ? "text-amber-700" : "text-stone-700";
  const time = entry.ts.slice(11, 23);
  return (
    <div className={`whitespace-pre-wrap break-all ${color}`}>
      <span className="text-stone-400">{time}</span> {entry.message}
      {entry.detail ? <span className="block pl-3 text-stone-500">{entry.detail}</span> : null}
    </div>
  );
}
