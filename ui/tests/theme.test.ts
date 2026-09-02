import { afterEach, describe, expect, it } from "vitest";
import { applyTheme, loadTheme, nextTheme, parseTheme, THEME_KEY } from "../src/theme/theme";

describe("theme", () => {
  afterEach(() => {
    try {
      localStorage.removeItem(THEME_KEY);
    } catch {
      // node test env may not have localStorage
    }
  });

  it("parses stored values and defaults to light", () => {
    expect(parseTheme("dark")).toBe("dark");
    expect(parseTheme("light")).toBe("light");
    expect(parseTheme(null)).toBe("light");
    expect(parseTheme("nope")).toBe("light");
  });

  it("toggles light and dark", () => {
    expect(nextTheme("light")).toBe("dark");
    expect(nextTheme("dark")).toBe("light");
  });

  it("keeps an explicit key for the html class and storage", () => {
    expect(THEME_KEY).toBe("casops.control-ui.theme.v1");
    expect(loadTheme()).toBe("light");
    if (typeof document === "undefined" || typeof localStorage === "undefined") {
      return;
    }
    applyTheme("dark");
    expect(document.documentElement.classList.contains("dark")).toBe(true);
    expect(localStorage.getItem(THEME_KEY)).toBe("dark");
    expect(loadTheme()).toBe("dark");
    applyTheme("light");
    expect(document.documentElement.classList.contains("dark")).toBe(false);
    expect(localStorage.getItem(THEME_KEY)).toBe("light");
  });
});
