import { useEffect, useRef } from "react";
import { X } from "lucide-react";
import { HelpDocument } from "./HelpDocument";
import {
  HELP_WIDTH_MAX,
  HELP_WIDTH_MIN,
  HELP_WIDTH_STEP,
  HELP_WIDTH_STEP_LARGE,
  clampHelpWidth,
} from "./paths";

export function RightHelpPanel({
  width,
  dragging,
  pathname,
  params,
  onClose,
  onWidthChange,
  onDraggingChange,
}: {
  width: number;
  dragging: boolean;
  pathname: string;
  params: Record<string, string | undefined>;
  onClose: () => void;
  onWidthChange: (width: number, persist?: boolean) => void;
  onDraggingChange: (dragging: boolean) => void;
}) {
  const drag = useRef<{ startX: number; startWidth: number } | null>(null);
  const widthRef = useRef(width);
  widthRef.current = width;

  useEffect(() => {
    function onMove(event: PointerEvent) {
      const session = drag.current;
      if (!session) {
        return;
      }
      const next = session.startWidth + (session.startX - event.clientX);
      onWidthChange(next);
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
  }, [onDraggingChange, onWidthChange, width]);

  function beginDrag(event: React.PointerEvent<HTMLDivElement>) {
    event.preventDefault();
    drag.current = { startX: event.clientX, startWidth: width };
    onDraggingChange(true);
    document.body.style.cursor = "col-resize";
    document.body.style.userSelect = "none";
  }

  function onKeyResize(event: React.KeyboardEvent<HTMLDivElement>) {
    const large = event.shiftKey;
    const step = large ? HELP_WIDTH_STEP_LARGE : HELP_WIDTH_STEP;
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
      data-testid="help-drawer"
    >
      <div
        role="separator"
        aria-orientation="vertical"
        aria-label="Resize help panel"
        aria-valuemin={HELP_WIDTH_MIN}
        aria-valuemax={HELP_WIDTH_MAX}
        aria-valuenow={clamped}
        tabIndex={0}
        data-testid="help-resize"
        className="absolute inset-y-0 left-0 z-10 w-1.5 cursor-col-resize hover:bg-indigo-200"
        onPointerDown={beginDrag}
        onKeyDown={onKeyResize}
      />
      <div className="flex items-center justify-between gap-2 border-b border-stone-200 px-3 py-2">
        <h2 className="text-sm font-semibold text-stone-800">Help</h2>
        <button
          type="button"
          className="rounded-lg p-1.5 text-stone-500 hover:bg-stone-100 hover:text-stone-900"
          aria-label="Close help panel"
          data-testid="help-drawer-close"
          onClick={onClose}
        >
          <X size={16} />
        </button>
      </div>
      <div className="flex min-h-0 flex-1 flex-col overflow-hidden px-3 py-3">
        <HelpDocument pathname={pathname} params={params} enabled />
      </div>
    </aside>
  );
}
