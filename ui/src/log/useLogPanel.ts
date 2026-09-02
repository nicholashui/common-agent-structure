import { useCallback, useState } from "react";
import { HELP_WIDTH_DEFAULT, clampHelpWidth, loadHelpWidth } from "../help/paths";

const LOG_WIDTH_KEY = "casops.control-ui.log-width.v1";

function loadLogWidth(): number {
  try {
    const raw = localStorage.getItem(LOG_WIDTH_KEY);
    if (!raw) {
      return loadHelpWidth();
    }
    return clampHelpWidth(Number(raw));
  } catch {
    return HELP_WIDTH_DEFAULT;
  }
}

export function useLogPanel() {
  const [logPanelOpen, setLogPanelOpen] = useState(false);
  const [logPanelWidth, setLogPanelWidth] = useState(loadLogWidth);
  const [logPanelDragging, setLogPanelDragging] = useState(false);

  const toggleLogPanel = useCallback(() => {
    setLogPanelOpen((open) => !open);
  }, []);

  const closeLogPanel = useCallback(() => {
    setLogPanelOpen(false);
  }, []);

  const updateLogWidth = useCallback((width: number, persist = false) => {
    const next = clampHelpWidth(width);
    setLogPanelWidth(next);
    if (persist) {
      try {
        localStorage.setItem(LOG_WIDTH_KEY, String(next));
      } catch {
        // ignore quota / private-mode failures
      }
    }
  }, []);

  return {
    logPanelOpen,
    logPanelWidth,
    logPanelDragging,
    setLogPanelDragging,
    toggleLogPanel,
    closeLogPanel,
    updateLogWidth,
  };
}
