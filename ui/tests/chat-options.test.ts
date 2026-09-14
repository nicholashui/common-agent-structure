import { describe, expect, it } from "vitest";
import { choiceIdFromAsk, parseOptionBlock } from "../src/lib/chatOptions";
import { HUMAN_DOMAIN_ROLES, humanReplyAgent } from "../src/lib/projectChat";

/** Same hop as casops.project_sample_walkthrough._ask_block(CYCLE_ASKS[0]); pytest pins the file. */
const cycleAskHop = `ASK_HUMAN: After the clip, keep Negatives as-is or tighten?
THINKING: Host-owned pass_03. Do not write the generator novel.
Decision point: pass_03-cycle critic
OPTION p3-1: keep Negatives — Clip matches the lock. (recommend)
OPTION p3-2: tighten Negatives — Add no morph and no extra jewelry after seeing the clip.
RECOMMEND: p3-1
DECIDE_BY: human
`;

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

  it("parses CYCLE_ASK OPTION p3-1 / p3-2 so onPick sends those ids", () => {
    const parsed = parseOptionBlock(cycleAskHop);
    expect(parsed.options.map((row) => row.id)).toEqual(["p3-1", "p3-2"]);
    expect(parsed.recommend).toBe("p3-1");
    expect(choiceIdFromAsk(cycleAskHop, "p3-2")).toBe("p3-2");
    expect(choiceIdFromAsk(cycleAskHop, "tighten Negatives")).toBe("p3-2");
    expect(humanReplyAgent("video.critic")).toBe("video.critic");
    expect(HUMAN_DOMAIN_ROLES.includes("video.critic" as (typeof HUMAN_DOMAIN_ROLES)[number])).toBe(false);
  });
});
