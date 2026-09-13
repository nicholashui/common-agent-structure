import { describe, expect, it } from "vitest";
import { parseOptionBlock } from "../src/lib/chatOptions";

describe("parseOptionBlock", () => {
  it("extracts option tags and selected id", () => {
    const parsed = parseOptionBlock(
      "THINKING: pick a thesis\nOPTION 1: phone-macro — pores\nOPTION 2: UGC CTA — product\nRECOMMEND: 1\nDECIDE_BY: human\n",
    );
    expect(parsed.options.map((row) => row.id)).toEqual(["1", "2"]);
    expect(parsed.options[0].label).toContain("phone-macro");
    expect(parsed.recommend).toBe("1");
    expect(parsed.body).toContain("THINKING");
    expect(parsed.body).not.toContain("OPTION 1");
  });

  it("parses a choice bubble", () => {
    const parsed = parseOptionBlock(
      "SELECTED: OPTION 1 — phone-macro\nSELECTED_BY: video.promptengineer\nREASON: brief is a person\n",
    );
    expect(parsed.selected).toBe("1");
    expect(parsed.selectedBy).toBe("video.promptengineer");
    expect(parsed.reason).toContain("person");
    expect(parsed.body).toBe("");
  });
});
