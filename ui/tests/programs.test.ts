import { describe, expect, it } from "vitest";
import { PROGRAM_INSTANCE_TABS, PROGRAM_MENU_LABEL, locationLabel, programIdFromPath } from "../src/shell/nav";
import {
  PROGRAM_CHILD_FIRST_CALLED,
  PROGRAM_CHILD_HUMAN_LOCKS,
  PROGRAM_FIRST_AGENT_HOP,
  PROGRAM_FIRST_CALLED,
  PROGRAM_LOCKS,
  PROGRAM_LOCK_LABELS,
  PROGRAM_PHASES,
  CUT_STATES,
  OVERVIEW_PANELS,
  finishReady,
  generationListLockable,
  normalizeProgramCode,
  programCodeValid,
  programNavLabel,
  resolveOverviewPanel,
  spawnMissingLocks,
  spawnReady,
} from "../src/lib/programs";
import { displayRelativePath } from "../src/lib/paths";
import { displayPartyName, hopKindLabel } from "../src/lib/projectChat";

describe("program chat matches project chat hop design", () => {
  it("names Create Program like Create Project and hop kinds", () => {
    expect(displayPartyName("create-program")).toBe("Create Program");
    expect(displayPartyName("create-project")).toBe("Create Project");
    expect(displayPartyName("human_operator")).toBe("Human");
    expect(hopKindLabel("instruction")).toBe("instruction");
    expect(hopKindLabel("induce")).toBe("induce");
    expect(hopKindLabel("return")).toBe("return");
  });
});

describe("program code", () => {
  it("keeps lowercase english with no spaces", () => {
    expect(normalizeProgramCode("Spring Launch")).toBe("spring-launch");
    expect(normalizeProgramCode("night-letter")).toBe("night-letter");
    expect(normalizeProgramCode("ABC_def")).toBe("abcdef");
    expect(programCodeValid("springlaunch")).toBe(true);
    expect(programCodeValid("night-letter")).toBe(true);
    expect(programCodeValid("1bad")).toBe(false);
    expect(programCodeValid("")).toBe(false);
  });
});

describe("program nav", () => {
  it("places New program under Program", () => {
    expect(PROGRAM_MENU_LABEL).toBe("Program");
    expect(locationLabel("/programs/new")).toBe("Program / New program");
    expect(locationLabel("/programs/springlaunch")).toBe("Program / springlaunch / Start");
    expect(locationLabel("/programs/springlaunch/start")).toBe("Program / springlaunch / Start");
    expect(locationLabel("/programs/springlaunch/chat")).toBe("Program / springlaunch / Chat");
    expect(locationLabel("/programs/springlaunch/workflow")).toBe("Program / springlaunch / Workflow");
    expect(locationLabel("/programs/springlaunch/overview")).toBe("Program / springlaunch / Overflow");
    expect(locationLabel("/programs/night-letter/overflow")).toBe("Program / night-letter / Overflow");
    expect(programIdFromPath("/programs/night-letter/chat")).toBe("night-letter");
    expect(programIdFromPath("/programs/new")).toBe("");
    expect(programNavLabel({ name: "Night Letter", code: "night-letter", id: "night-letter" })).toBe(
      "Night Letter",
    );
    expect(programNavLabel({ name: "Spring Launch", id: "spring-launch" })).toBe("Spring Launch");
  });

  it("exposes Start Workflow Chat Overflow tabs (U1–U4)", () => {
    expect(PROGRAM_INSTANCE_TABS.map((item) => item.id)).toEqual(["start", "workflow", "chat", "overflow"]);
    expect(PROGRAM_INSTANCE_TABS.map((item) => item.label)).toEqual(["Start", "Workflow", "Chat", "Overflow"]);
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
    expect(PROGRAM_LOCK_LABELS.generation_list).toBe("Generation list");
    expect(PROGRAM_LOCK_LABELS.visual_bible).toBe("Visual bible");
    expect(spawnReady({ generation_list: true })).toBe(false);
    expect(finishReady({ picture: false })).toBe(false);
  });
});

describe("overview one function one UI", () => {
  it("lists seven functions and defaults to generation list", () => {
    expect(OVERVIEW_PANELS.map((item) => item.id)).toEqual([
      "phase",
      "locks",
      "list",
      "spawn",
      "bible",
      "cut",
      "delivery",
    ]);
    expect(resolveOverviewPanel(null)).toBe("list");
    expect(resolveOverviewPanel("")).toBe("list");
    expect(resolveOverviewPanel("nope")).toBe("list");
    expect(resolveOverviewPanel("phase")).toBe("phase");
    expect(resolveOverviewPanel("locks")).toBe("locks");
    expect(resolveOverviewPanel("spawn")).toBe("spawn");
    expect(resolveOverviewPanel("bible")).toBe("bible");
    expect(resolveOverviewPanel("cut")).toBe("cut");
    expect(resolveOverviewPanel("delivery")).toBe("delivery");
    expect(new Set(OVERVIEW_PANELS.map((item) => item.id)).size).toBe(OVERVIEW_PANELS.length);
  });
});
