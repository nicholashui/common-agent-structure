import { createContext, useCallback, useContext, useEffect, useMemo, useState, type ReactNode } from "react";
import { applyTheme, loadTheme, nextTheme, type ThemeName } from "./theme";

interface ThemeValue {
  theme: ThemeName;
  setTheme: (theme: ThemeName) => void;
  toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeValue | null>(null);

export function ThemeProvider({ children }: { children: ReactNode }) {
  const [theme, setThemeState] = useState<ThemeName>(loadTheme);

  const setTheme = useCallback((next: ThemeName) => {
    setThemeState(next);
    applyTheme(next);
  }, []);

  const toggleTheme = useCallback(() => {
    setThemeState((current) => {
      const next = nextTheme(current);
      applyTheme(next);
      return next;
    });
  }, []);

  useEffect(() => {
    applyTheme(theme);
  }, [theme]);

  const value = useMemo(() => ({ theme, setTheme, toggleTheme }), [theme, setTheme, toggleTheme]);
  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
}

export function useTheme(): ThemeValue {
  const value = useContext(ThemeContext);
  if (!value) {
    throw new Error("useTheme requires ThemeProvider");
  }
  return value;
}
