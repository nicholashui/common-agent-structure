import { describe, expect, it } from "vitest";
import {
  HUMAN_DOMAIN_ROLES,
  commIdForAgent,
  commSeq,
  cyclePersistError,
  displayPartyName,
  hopHeaderText,
  instructionHopForPanel,
  mediaHref,
  optionAgentIds,
  shownOptionId,
  pairHumanAsks,
  sortProjectComms,
  sourceCommId,
  splitProjectChat,
} from "../src/lib/projectChat";
import { agentIdFromProfileChatHref, projectChatHref } from "../src/lib/projectContext";
import { filterByRoster, rosterAfterFetch } from "../src/lib/swarmFilter";

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

  it("prefers the output hop over assembled host note for the generator panel", () => {
    const hop = instructionHopForPanel([
      { id: "comm-0050", kind: "assembled", text: "Host-joined generator instruction.", created_at: "2026-09-13T08:00:00Z" },
      { id: "comm-0051", kind: "output", text: "Rooftop phone-macro: lived-in handsome.", created_at: "2026-09-13T08:00:00Z" },
    ]);
    expect(hop?.id).toBe("comm-0051");
    expect(hop?.text).toContain("Rooftop phone-macro");
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
    expect(displayPartyName("host_service")).toBe("Host");
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

  it("names Auto Pilot specials and the five human domain locks", () => {
    expect(displayPartyName("specials.intent-analysis-agent")).toBe("intent-analysis-agent");
    expect(displayPartyName("specials.general-creative-agent")).toBe("creative-agent");
    expect([...HUMAN_DOMAIN_ROLES]).toEqual([
      "video.promptengineer",
      "video.director",
      "video.cinematographer",
      "video.mua_makeup",
      "video.continuity",
    ]);
    expect(
      hopHeaderText({
        id: "comm-0012",
        from: "human_operator",
        to: "video.director",
        kind: "choice",
        pass_id: "pass_01",
        created_at: "2026-09-13T08:00:00Z",
        live: false,
      }),
    ).toBe("Human → video.director | selection · pass_01 · #12 · 2026-09-13 16:00:00 · not a live hop");
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

  it("does not treat an expert decision chosen id as the human ASK selection", () => {
    const askIds = ["1", "2", "3"];
    expect(
      shownOptionId({
        kind: "human_ask",
        optionIds: askIds,
        parsedSelected: "",
        followSelected: "",
        expertChosen: "1",
        recommend: "1",
        focusOpt: "",
        focusMatchesComm: false,
      }),
    ).toBe("");
    expect(
      shownOptionId({
        kind: "human_ask",
        optionIds: askIds,
        parsedSelected: "",
        followSelected: "2",
        expertChosen: "1",
        recommend: "1",
        focusOpt: "3",
        focusMatchesComm: false,
      }),
    ).toBe("2");
    expect(
      shownOptionId({
        kind: "human_ask",
        optionIds: askIds,
        parsedSelected: "",
        followSelected: "",
        expertChosen: "1",
        recommend: "1",
        focusOpt: "2",
        focusMatchesComm: true,
      }),
    ).toBe("2");
    expect(
      shownOptionId({
        kind: "return",
        optionIds: askIds,
        parsedSelected: "",
        followSelected: "",
        expertChosen: "1",
        recommend: "2",
        focusOpt: "2",
        focusMatchesComm: false,
      }),
    ).toBe("1");
  });

  it("resolves a Project Chat hop for an agent and prefers ASK_HUMAN", () => {
    const hops = [
      { id: "comm-0008", kind: "instruction", from: "create-project", to: "video.promptengineer" },
      { id: "comm-0009", kind: "return", from: "video.promptengineer", to: "create-project" },
      { id: "comm-0011", kind: "human_ask", from: "video.promptengineer", to: "human_operator" },
    ];
    expect(commIdForAgent(hops, "video.promptengineer")).toBe("comm-0011");
    expect(projectChatHref("asain-beauty", { comm: "comm-0011" })).toBe(
      "/projects/asain-beauty/chat?comm=comm-0011",
    );
    expect(projectChatHref("asain-beauty", { agent: "video.director" })).toBe(
      "/projects/asain-beauty/chat?agent=video.director",
    );
    expect(agentIdFromProfileChatHref("/agents/video.promptengineer/chat")).toBe("video.promptengineer");
  });

  it("filters fleet rows to a swarm roster", () => {
    const rows = [{ agent_id: "video.promptengineer" }, { agent_id: "video.planner" }, { agent_id: "video.director" }];
    expect(filterByRoster(rows, ["video.promptengineer", "video.director"]).map((row) => row.agent_id)).toEqual([
      "video.promptengineer",
      "video.director",
    ]);
    expect(filterByRoster(rows, null)).toEqual(rows);
    expect(rosterAfterFetch(false)).toBeNull();
    expect(filterByRoster(rows, rosterAfterFetch(false))).toEqual(rows);
    expect(rosterAfterFetch(true, ["video.promptengineer"])).toEqual(["video.promptengineer"]);
  });

  it("does not treat a critic p3 choice as the answer to a later continuity ASK", () => {
    const pairs = pairHumanAsks([
      { id: "ask-critic", kind: "human_ask", from: "video.critic", to: "human_operator", node_id: "human-ask" },
      { id: "ask-cont", kind: "human_ask", from: "video.continuity", to: "human_operator", node_id: "human-ask" },
      {
        id: "pick-critic",
        kind: "choice",
        from: "human_operator",
        to: "video.critic",
        node_id: "human-ask",
      },
    ]);
    expect(pairs.find((row) => row.ask.from === "video.critic")?.answer?.id).toBe("pick-critic");
    expect(pairs.find((row) => row.ask.from === "video.continuity")?.answer).toBeUndefined();
  });

  it("warns when an Auto Pilot cycle would not persist under dry-run", () => {
    expect(cyclePersistError(true)).toMatch(/Dry-run is on/i);
    expect(cyclePersistError(false)).toBe("");
  });
});
