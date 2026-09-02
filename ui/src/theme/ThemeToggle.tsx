import { Moon, Sun } from "lucide-react";
import { useTheme } from "./ThemeProvider";

export function ThemeToggle() {
  const { theme, toggleTheme } = useTheme();
  const dark = theme === "dark";
  const label = dark ? "Switch to light theme" : "Switch to dark theme";
  return (
    <button
      type="button"
      className="rounded-lg p-1.5 text-stone-500 hover:bg-stone-100 hover:text-stone-900"
      aria-label={label}
      aria-pressed={dark}
      title={label}
      data-testid="theme-toggle"
      onClick={toggleTheme}
    >
      {dark ? <Sun size={16} /> : <Moon size={16} />}
    </button>
  );
}
