import { describe, expect, it } from "vitest";
import {
  OWNER_PATHS,
  dispositionChips,
  headingOwner,
  ownerPathsFor,
  splitProjection,
} from "../src/lib/videoPrompt";

describe("video prompt owners", () => {
  it("maps T4 headings to canonical owners", () => {
    expect(headingOwner("Subject")).toEqual({
      owner: "video.continuity",
      path: "creative.shots.subjects",
    });
    expect(headingOwner("Light")).toEqual({
      owner: "video.cinematographer",
      path: "creative.shots.lighting",
    });
    expect(headingOwner("Hair")).toEqual({
      owner: "video.continuity",
      path: "creative.shots.subjects.anchors",
    });
    expect(headingOwner("Negatives").owner).toBe("video.critic");
    expect(headingOwner("0–3s | smash").owner).toBe("video.director");
  });

  it("keeps unique projection blocks and owners", () => {
    const split = splitProjection(
      "Generate from locks.\n\nSubject\nAdult face lock.\n\nHair\nHair stays off the lips.\n\nLight\nHard sun.\n",
    );
    expect(split.intro).toContain("Generate from locks");
    expect(split.sections.map((row) => row.heading)).toEqual(["Subject", "Hair", "Light"]);
    expect(split.sections[0].body).toBe("Adult face lock.");
    expect(split.sections[1].body).toBe("Hair stays off the lips.");
    expect(split.sections[0].owner).toBe("video.continuity");
    expect(split.sections[2].owner).toBe("video.cinematographer");
  });

  it("lists owned paths per agent without a live count", () => {
    expect(ownerPathsFor("video.cinematographer")).toEqual(["creative.shots.lighting", "creative.shots.look"]);
    expect(Object.keys(OWNER_PATHS).length).toBeGreaterThan(0);
  });

  it("collapses coverage into disposition chips", () => {
    const chips = dispositionChips([
      { disposition: "prompted" },
      { disposition: "exact" },
      { disposition: "prompted" },
      { disposition: "unsupported" },
    ]);
    expect(chips.map((row) => row.disposition)).toEqual(["exact", "prompted", "unsupported"]);
    expect(chips.find((row) => row.disposition === "prompted")?.count).toBe(2);
  });
});
