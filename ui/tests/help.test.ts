import { describe, expect, it } from "vitest";
import { htmlImgsToMarkdown, isHtmlFallback, resolveAssetUrl } from "../src/help/markdown";
import {
  clampHelpWidth,
  docCandidates,
  helpPageFrom,
  helpPageHref,
  HELP_WIDTH_MAX,
  HELP_WIDTH_MIN,
  paramsFromPathname,
  stripParamValues,
} from "../src/help/paths";
import { HELP_FULL_PAGE_PATH, HELP_TABS } from "../src/help/tabs";
import { locationLabel } from "../src/shell/nav";

describe("help route resolution", () => {
  it("builds exact then parameter-stripped markdown candidates", () => {
    expect(docCandidates("/agents/video.director/chat", { agentId: "video.director" }, "spec")).toEqual([
      "/docs/agents/video.director/chat/spec.md",
      "/docs/agents/video.director/spec.md",
      "/docs/agents/chat/spec.md",
    ]);
    expect(docCandidates("/agents/specials.aesthetics-agent", { agentId: "specials.aesthetics-agent" }, "userguide")).toEqual([
      "/docs/agents/specials.aesthetics-agent/userguide.md",
      "/docs/agents/userguide.md",
    ]);
    expect(docCandidates("/", {}, "userguide")).toEqual(["/docs/userguide.md", "/docs/index/userguide.md"]);
    expect(docCandidates("/workflow/sub", {}, "spec")).toEqual(["/docs/workflow/sub/spec.md"]);
  });

  it("strips encoded and raw param values", () => {
    expect(stripParamValues("/agents/video.director/structure", { agentId: "video.director" })).toBe("/agents/structure");
    expect(paramsFromPathname("/agents/video.director/chat")).toEqual({ agentId: "video.director" });
  });

  it("keeps the full-page help route configurable", () => {
    expect(HELP_FULL_PAGE_PATH).toBe("/help");
    expect(helpPageHref("/workflow/sub")).toBe("/help?from=%2Fworkflow%2Fsub");
    expect(helpPageFrom("?from=/settings", "/")).toBe("/settings");
    expect(locationLabel("/help")).toBe("Agent Swarm / Help");
  });
});

describe("help markdown guards", () => {
  it("treats HTML fallbacks as missing documents", () => {
    expect(isHtmlFallback("text/html", "<html>index</html>")).toBe(true);
    expect(isHtmlFallback("text/markdown", "# Hello")).toBe(false);
    expect(isHtmlFallback("text/plain", "<!DOCTYPE html><html></html>")).toBe(true);
  });

  it("converts raw HTML images and resolves relative assets", () => {
    expect(htmlImgsToMarkdown('before <img src="./shot.png" alt="Shot"> after')).toBe("before ![Shot](./shot.png) after");
    expect(resolveAssetUrl("./shot.png", "/docs/workflow/spec.md")).toBe("/docs/workflow/shot.png");
    expect(resolveAssetUrl("/img/logo.svg", "/docs/workflow/spec.md")).toBe("/img/logo.svg");
    expect(resolveAssetUrl("https://example.com/a.png", "/docs/workflow/spec.md")).toBe("https://example.com/a.png");
  });
});

describe("help drawer width", () => {
  it("clamps persisted width", () => {
    expect(clampHelpWidth(12)).toBe(HELP_WIDTH_MIN);
    expect(clampHelpWidth(9000)).toBe(HELP_WIDTH_MAX);
    expect(clampHelpWidth(400)).toBe(400);
  });
});

describe("help tabs", () => {
  it("exposes generic spec and userguide types", () => {
    expect(HELP_TABS.map((tab) => tab.id)).toEqual(["spec", "userguide"]);
  });
});
