import { describe, expect, it } from "vitest";
import { relativeAgentFolder } from "../src/lib/agents";
import { displayRelativePath } from "../src/lib/paths";

describe("displayRelativePath", () => {
  it("strips drive letters and repo prefixes", () => {
    expect(displayRelativePath("C:\\Project\\common-agent-structure\\agents\\video.director")).toBe(
      "agents/video.director",
    );
    expect(displayRelativePath("C:/Project/common-agent-structure/logs/chat/video.director/a.jsonl")).toBe(
      "logs/chat/video.director/a.jsonl",
    );
    expect(displayRelativePath("/Users/me/common-agent-structure/project/asain-beauty")).toBe(
      "project/asain-beauty",
    );
    expect(displayRelativePath("/docs/userguide.md")).toBe("docs/userguide.md");
    expect(displayRelativePath("spec/grok_imagine_operation_guide.md")).toBe(
      "spec/grok_imagine_operation_guide.md",
    );
    expect(displayRelativePath("prompts/primary.md")).toBe("prompts/primary.md");
    expect(displayRelativePath("creative.shots.subjects")).toBe("creative.shots.subjects");
    expect(displayRelativePath("")).toBe("");
  });

  it("keeps agent folders as agents/<id>", () => {
    expect(relativeAgentFolder("C:\\tmp\\agents\\video.director", "video.director")).toBe("agents/video.director");
  });
});
