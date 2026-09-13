import { describe, expect, it } from "vitest";
import {
  commSeq,
  displayPartyName,
  hopHeaderText,
  mediaHref,
  optionAgentIds,
  sortProjectComms,
  sourceCommId,
  splitProjectChat,
} from "../src/lib/projectChat";

describe("project chat time sequence", () => {
  it("reads padded and unpadded comm ids as sequence numbers", () => {
    expect(commSeq("comm-0009")).toBe(9);
    expect(commSeq("comm-10")).toBe(10);
  });

  it("orders equal timestamps by comm sequence, not string localeCompare", () => {
    const rows = sortProjectComms([
      { id: "comm-10", kind: "induce", created_at: "2026-09-13T08:00:00Z" },
      { id: "comm-9", kind: "return", created_at: "2026-09-13T08:00:00Z" },
      { id: "comm-2", kind: "instruction", created_at: "2026-09-13T08:00:00Z" },
    ]);
    expect(rows.map((row) => row.id)).toEqual(["comm-2", "comm-9", "comm-10"]);
  });

  it("orders later created_at after earlier hops, even with a later id already assigned", () => {
    const rows = sortProjectComms([
      { id: "comm-0054", kind: "generated_media", created_at: "2026-09-13T11:29:56Z" },
      { id: "comm-0001", kind: "instruction", created_at: "2026-09-13T08:00:00Z" },
      { id: "comm-0051", kind: "output", created_at: "2026-09-13T08:00:00Z" },
    ]);
    expect(rows.map((row) => row.id)).toEqual(["comm-0001", "comm-0051", "comm-0054"]);
  });

  it("keeps collab hops, then assembled instruction, then generated clips", () => {
    const split = splitProjectChat([
      { id: "comm-0054", kind: "generated_media", created_at: "2026-09-13T11:29:56Z" },
      { id: "comm-0001", kind: "instruction", created_at: "2026-09-13T08:00:00Z" },
      { id: "comm-0050", kind: "next_instruction", created_at: "2026-09-13T08:00:00Z" },
      { id: "comm-0052", kind: "generated_media", created_at: "2026-09-13T11:27:35Z" },
      { id: "comm-0051", kind: "output", created_at: "2026-09-13T08:00:00Z" },
    ]);
    expect(split.conversation.map((row) => row.kind)).toEqual(["instruction", "next_instruction"]);
    expect(split.instruction.map((row) => row.id)).toEqual(["comm-0051"]);
    expect(split.clips.map((row) => row.id)).toEqual(["comm-0052", "comm-0054"]);
  });

  it("embeds only same-origin output file names", () => {
    const ok = "/api/v3/projects/asain-beauty/output/file?name=asain-beauty.mp4";
    expect(mediaHref(ok, "asain-beauty")).toBe(ok);
    expect(mediaHref("https://evil.example/x.mp4", "asain-beauty")).toBe("");
    expect(mediaHref("javascript:alert(1)", "asain-beauty")).toBe("");
    expect(mediaHref("/api/v3/projects/asain-beauty/output/file?name=../sample/x.txt", "asain-beauty")).toBe("");
    expect(mediaHref(ok, "other-project")).toBe("");
  });

  it("names hop parties Human -> Create Project on the first box", () => {
    expect(displayPartyName("human_operator")).toBe("Human");
    expect(displayPartyName("create-project")).toBe("Create Project");
    expect(displayPartyName("output-prompt")).toBe("Output");
    expect(displayPartyName("video.promptengineer")).toBe("video.promptengineer");
    expect(
      hopHeaderText({
        id: "comm-0001",
        from: "human_operator",
        to: "create-project",
        kind: "instruction",
        pass_id: "pass_01",
        created_at: "2026-09-13T08:00:00Z",
        live: false,
      }),
    ).toBe("Human → Create Project | instruction · pass_01 · #1 · 2026-09-13 16:00:00 · not a live hop");
  });

  it("links an output agent to the prior box that wrote into it", () => {
    const hops = [
      { id: "comm-0001", kind: "instruction", from: "human_operator", to: "create-project" },
      { id: "comm-0002", kind: "instruction", from: "create-project", to: "video.promptengineer" },
      { id: "comm-0003", kind: "return", from: "video.promptengineer", to: "create-project" },
    ];
    expect(sourceCommId(hops[0], hops)).toBe("");
    expect(sourceCommId(hops[1], hops)).toBe("comm-0001");
    expect(sourceCommId(hops[2], hops)).toBe("comm-0002");
  });

  it("lists the proposing agent and agents named in an option", () => {
    expect(optionAgentIds("video.promptengineer", "Induce video.creativedirector first")).toEqual([
      "video.promptengineer",
      "video.creativedirector",
    ]);
  });
});
