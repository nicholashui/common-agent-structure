import { describe, expect, it } from "vitest";
import { applyLlmNext, applyLlmSuggestion, parseVideoAgentIds, parseVideoWorkflowIds, suggestionRow } from "../src/lib/projects";
import type { ProjectCatalogItem, ProjectSuggestion } from "../src/api/types";

const CATALOG: ProjectCatalogItem[] = [
  { id: "video.template.a", kind: "template", code: "A", label: "Viral Hook", use: "short social spike" },
  { id: "video.template.f", kind: "template", code: "F", label: "Corporate Training", use: "internal training" },
  { id: "video.scale.s3", kind: "scale", code: "S3", label: "Scale S3", use: "variant campaign" },
];

const BASE: ProjectSuggestion = {
  honesty: "CHARACTERIZATION",
  llm_used: false,
  primary: "video.template.a",
  suggestions: [
    suggestionRow(CATALOG[0], 1, "heuristic"),
    suggestionRow(CATALOG[2], 2, "heuristic"),
  ],
};

describe("project suggestion merge", () => {
  it("parses template and scale ids", () => {
    expect(parseVideoWorkflowIds("Use video.template.f and video.scale.s3 please")).toEqual([
      "video.template.f",
      "video.scale.s3",
    ]);
    expect(parseVideoWorkflowIds("no ids")).toEqual([]);
  });

  it("promotes llm ids above heuristic rows", () => {
    const merged = applyLlmSuggestion(BASE, "Pick video.template.f then video.scale.s3", CATALOG);
    expect(merged.llm_used).toBe(true);
    expect(merged.primary).toBe("video.template.f");
    expect(merged.suggestions[0].id).toBe("video.template.f");
    expect(merged.suggestions[0].source).toBe("llm");
    expect(merged.suggestions[1].id).toBe("video.scale.s3");
    expect(merged.suggestions.map((row) => row.id)).toContain("video.template.a");
  });

  it("keeps heuristic order when the planner names nothing", () => {
    const merged = applyLlmSuggestion(BASE, "I am unsure", CATALOG);
    expect(merged.primary).toBe("video.template.a");
    expect(merged.suggestions[0].id).toBe("video.template.a");
    expect(merged.llm_used).toBe(true);
  });
});

describe("project next-node merge", () => {
  it("promotes parent-named agent ids", () => {
    expect(parseVideoAgentIds("next video.screenwriter then video.judge")).toEqual([
      "video.screenwriter",
      "video.judge",
    ]);
    const merged = applyLlmNext(
      {
        honesty: "CHARACTERIZATION",
        llm_used: false,
        from_id: "create-project",
        primary: "video.instructionaldesign",
        suggestions: [
          {
            id: "video.instructionaldesign",
            label: "video.instructionaldesign",
            kind: "agent",
            inputs: [],
            outputs: ["video.screenwriter"],
            contract: ["video.instructionaldesign"],
            reason: "lane",
            rank: 1,
            source: "lane",
          },
          {
            id: "video.screenwriter",
            label: "video.screenwriter",
            kind: "agent",
            inputs: ["video.instructionaldesign"],
            outputs: [],
            contract: ["video.screenwriter"],
            reason: "output bus",
            rank: 2,
            source: "parent_output",
          },
        ],
      },
      "Use video.screenwriter",
    );
    expect(merged.primary).toBe("video.screenwriter");
    expect(merged.suggestions[0].source).toBe("llm");
  });
});
