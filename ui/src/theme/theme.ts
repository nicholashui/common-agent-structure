export type ThemeName = "light" | "dark";

export const THEME_KEY = "casops.control-ui.theme.v1";

export function parseTheme(raw: string | null | undefined): ThemeName {
  return raw === "dark" ? "dark" : "light";
}

export function loadTheme(): ThemeName {
  try {
    return parseTheme(localStorage.getItem(THEME_KEY));
  } catch {
    return "light";
  }
}

export function applyTheme(theme: ThemeName): void {
  const root = document.documentElement;
  root.classList.toggle("dark", theme === "dark");
  root.style.colorScheme = theme;
  try {
    localStorage.setItem(THEME_KEY, theme);
  } catch {
    // ignore quota / private-mode failures
  }
}

export function nextTheme(theme: ThemeName): ThemeName {
  return theme === "dark" ? "light" : "dark";
}
