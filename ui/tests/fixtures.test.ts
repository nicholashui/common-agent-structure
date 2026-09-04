import { describe, expect, it } from "vitest";
import type { EvalFixturesResponse } from "../src/api/types";
import {
  chatFixtureHref,
  chatFixtures,
  clipPreview,
  findFixture,
  fixtureMessage,
  fixtureTitle,
  runTabHref,
} from "../src/lib/fixtures";
import { validationIsPass } from "../src/lib/honesty";

const suite: EvalFixturesResponse = {
  agent_id: "specials.intent-analysis-agent",
  honesty: "CHARACTERIZATION",
  note: "Not an eval pass. casops-eval stays NOT_RUN.",
  fixtures: [
    {
      id: "chat-tc1",
      path: "chat",
      honesty: "CHARACTERIZATION",
      input: { message: "Make a 6-day Osaka travel vlog for high retention" },
      source: { case_name: "Travel vlog brief" },
    },
    {
      id: "run-tc1",
      path: "run",
      honesty: "CHARACTERIZATION",
      input: {},
      source: { note: "Sealed Runtime.execute" },
    },
  ],
};

describe("characterization fixtures", () => {
  it("extracts chat messages and titles without claiming a pass", () => {
    expect(suite.honesty).toBe("CHARACTERIZATION");
    expect(validationIsPass({ verdict: "NOT_RUN", pass: false })).toBe(false);
    const chats = chatFixtures(suite);
    expect(chats).toHaveLength(1);
    expect(fixtureMessage(chats[0])).toBe("Make a 6-day Osaka travel vlog for high retention");
    expect(fixtureTitle(chats[0])).toBe("Travel vlog brief");
    expect(findFixture(suite, "run-tc1")?.path).toBe("run");
  });

  it("builds Chat load and Run tab hrefs", () => {
    expect(chatFixtureHref("video.director", "chat-tc1")).toBe(
      "/agents/video.director/chat?fixture=chat-tc1",
    );
    expect(runTabHref("video.director")).toBe("/agents/video.director/run");
  });

  it("clips long previews", () => {
    expect(clipPreview("short")).toBe("short");
    expect(clipPreview("abcdefghij", 8)).toBe("abcdefg…");
  });
});
