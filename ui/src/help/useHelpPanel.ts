import { useCallback, useState } from "react";
import { clampHelpWidth, loadHelpWidth, saveHelpWidth } from "./paths";

export function useHelpPanel() {
  const [rightPanelOpen, setRightPanelOpen] = useState(false);
  const [rightPanelWidth, setRightPanelWidth] = useState(loadHelpWidth);
  const [rightPanelDragging, setRightPanelDragging] = useState(false);

  const toggleRightPanel = useCallback(() => {
    setRightPanelOpen((open) => !open);
  }, []);

  const closeRightPanel = useCallback(() => {
    setRightPanelOpen(false);
  }, []);

  const updateWidth = useCallback((width: number, persist = false) => {
    const next = clampHelpWidth(width);
    setRightPanelWidth(next);
    if (persist) {
      saveHelpWidth(next);
    }
  }, []);

  return {
    rightPanelOpen,
    rightPanelWidth,
    rightPanelDragging,
    setRightPanelDragging,
    toggleRightPanel,
    closeRightPanel,
    updateWidth,
  };
}
