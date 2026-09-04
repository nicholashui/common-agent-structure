import { describe, expect, it } from "vitest";
import { COMPANION_V3_PATHS } from "../src/api/paths";
import { isJsonPath, isMarkdownPath } from "../src/lib/markdown";

describe("agent files companion", () => {
  it("registers list and item GET/PUT as companion v3 paths", () => {
    const keys = COMPANION_V3_PATHS.map(([method, path]) => `${method} ${path}`);
    expect(keys).toContain("GET /api/v3/agents/{agent_id}/files");
    expect(keys).toContain("GET /api/v3/agents/{agent_id}/files/item");
    expect(keys).toContain("PUT /api/v3/agents/{agent_id}/files/item");
  });

  it("treats markdown and json paths as preview kinds", () => {
    expect(isMarkdownPath("prompts/primary.md")).toBe(true);
    expect(isMarkdownPath("docs/user_guide.MD")).toBe(true);
    expect(isMarkdownPath("identity/persona.json")).toBe(false);
    expect(isJsonPath("identity/persona.json")).toBe(true);
    expect(isJsonPath("prompts/primary.md")).toBe(false);
  });
});
