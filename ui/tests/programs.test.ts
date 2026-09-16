import { describe, expect, it } from "vitest";
import { PROGRAM_INSTANCE_TABS, PROGRAM_MENU_LABEL, locationLabel } from "../src/shell/nav";
import {
  PROGRAM_CHILD_FIRST_CALLED,
  PROGRAM_CHILD_HUMAN_LOCKS,
  PROGRAM_FIRST_AGENT_HOP,
  PROGRAM_FIRST_CALLED,
  PROGRAM_LOCKS,
  PROGRAM_PHASES,
  CUT_STATES,
  finishReady,
  generationListLockable,
  normalizeProgramCode,
  programCodeValid,
  spawnMissingLocks,
  spawnReady,
} from "../src/lib/programs";
import { displayRelativePath } from "../src/lib/paths";

describe("program code", () => {
  it("keeps lowercase english with no spaces", () => {
    expect(normalizeProgramCode("Spring Launch")).toBe("springlaunch");
    expect(normalizeProgramCode("ABC_def")).toBe("abcdef");
    expect(programCodeValid("springlaunch")).toBe(true);
    expect(programCodeValid("1bad")).toBe(false);
    expect(programCodeValid("")).toBe(false);
  });
});

describe("program nav", () => {
  it("places New program under Program", () => {
    expect(PROGRAM_MENU_LABEL).toBe("Program");
    expect(locationLabel("/programs/new")).toBe("Program / New program");
    expect(locationLabel("/programs/springlaunch")).toBe("Program / springlaunch");
    expect(locationLabel("/programs/springlaunch/chat")).toBe("Program / springlaunch / Chat");
    expect(locationLabel("/programs/springlaunch/workflow")).toBe("Program / springlaunch / Workflow");
  });

  it("exposes overview workflow chat tabs", () => {
    expect(PROGRAM_INSTANCE_TABS.map((item) => item.id)).toEqual(["overview", "workflow", "chat"]);
  });
});

describe("ISSUE-0013 program filmmaking state", () => {
  it("lists W0–W6 and lock names", () => {
    expect(PROGRAM_PHASES.map((item) => item.id)).toEqual(["w0", "w1", "w2", "w3", "w4", "w5", "w6"]);
    expect([...PROGRAM_LOCKS]).toEqual([
      "logline",
      "pages",
      "generation_list",
      "visual_bible",
      "storyboard",
      "picture",
      "delivery",
    ]);
  });

  it("gates spawn on generation_list and visual_bible", () => {
    expect(spawnReady({})).toBe(false);
    expect(spawnMissingLocks({ generation_list: true })).toEqual(["visual_bible"]);
    expect(spawnReady({ generation_list: true, visual_bible: true })).toBe(true);
    expect(finishReady({})).toBe(false);
    expect(finishReady({ picture: true })).toBe(true);
  });

  it("keeps Program first-called showrunner and child Auto Pilot PE", () => {
    expect(PROGRAM_FIRST_AGENT_HOP).toBe("specials.intent-analysis-agent");
    expect(PROGRAM_FIRST_CALLED).toBe("video.showrunner");
    expect(PROGRAM_CHILD_FIRST_CALLED).toBe("video.promptengineer");
    expect([...PROGRAM_CHILD_HUMAN_LOCKS]).toEqual([
      "video.promptengineer",
      "video.director",
      "video.cinematographer",
      "video.mua_makeup",
      "video.continuity",
    ]);
  });

  it("shows generation list as scene with many segments and relative paths", () => {
    const scenes = [{ id: "sc1", segments: [{ id: "a" }, { id: "b" }] }];
    expect(scenes[0].segments).toHaveLength(2);
    expect(generationListLockable([])).toBe(false);
    expect(generationListLockable([{ id: "sc1", segments: [] }])).toBe(false);
    expect(generationListLockable(scenes)).toBe(true);
    expect(displayRelativePath("C:/Project/common-agent-structure/program/film/generation-list.yaml")).toBe(
      "program/film/generation-list.yaml",
    );
    expect(displayRelativePath("C:/Project/common-agent-structure/program/film/delivery/specifications.yaml")).toBe(
      "program/film/delivery/specifications.yaml",
    );
    expect(displayRelativePath("C:/Project/common-agent-structure/program/film/bible/cast.md")).toBe(
      "program/film/bible/cast.md",
    );
    expect([...CUT_STATES]).toEqual(["assembly", "rough", "fine", "picture_lock"]);
    expect(PROGRAM_LOCKS).toContain("visual_bible");
    expect(PROGRAM_LOCKS).toContain("storyboard");
    expect(spawnReady({ generation_list: true })).toBe(false);
    expect(finishReady({ picture: false })).toBe(false);
  });
});
