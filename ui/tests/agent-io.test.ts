import { describe, expect, it } from "vitest";
import { AGENT_MENU_LABEL, AGENT_TABS, WORKFLOW_MENU_LABEL, WORKFLOW_TABS, locationLabel } from "../src/shell/nav";
import { listSubWorkflows, subWorkflowSvgSrc, workflowAgentChatHrefs, workflowSvgSrc } from "../src/lib/workflow";
import videoWorkflowSvg from "../public/svg/video.workflow.svg?raw";
import { ioHasContract, parseAgentIo } from "../src/lib/io";
import { chatHitOutputCap, normalizeChatHistory } from "../src/lib/chat";

describe("agent I/O contract", () => {
  it("parses critique_edges inputs and outputs", () => {
    const io = parseAgentIo({
      defined: true,
      source: "critique_edges",
      inputs: ["video.critic", ""],
      outputs: ["video.judge"],
      prompt_reference: "prompts/primary.md",
    });
    expect(io.defined).toBe(true);
    expect(io.inputs).toEqual(["video.critic"]);
    expect(io.outputs).toEqual(["video.judge"]);
    expect(ioHasContract(io)).toBe(true);
  });

  it("treats empty buses as undeclared content", () => {
    const io = parseAgentIo({
      defined: false,
      source: "critique_edges",
      inputs: [],
      outputs: [],
    });
    expect(ioHasContract(io)).toBe(false);
    expect(io.source).toBe("critique_edges");
  });
});

describe("page location label", () => {
  it("uses the agent path as the large menu label", () => {
    expect(locationLabel("/agents/common.health/corrigibility")).toBe(
      "Agent Swarm / agents/common.health/corrigibility",
    );
    expect(locationLabel("/agents/video.director")).toBe("Agent Swarm / agents/video.director");
    expect(locationLabel("/")).toBe("Agent Swarm");
    expect(locationLabel("/org-chat")).toBe("Agent Swarm / Agent Org Chat");
    expect(locationLabel("/workflow")).toBe("Agent Swarm / Agent Workflow / Main Workflow");
    expect(locationLabel("/workflow/sub")).toBe("Agent Swarm / Agent Workflow / Main Workflow / Sub Workflow");
    expect(locationLabel("/help")).toBe("Agent Swarm / Help");
  });
});

describe("agent workflow svg", () => {
  it("embeds video.workflow.svg for the video Agent Group", () => {
    expect(workflowSvgSrc("video")).toBe("/svg/video.workflow.svg");
    expect(workflowSvgSrc("specials")).toBeNull();
    expect(workflowSvgSrc("other")).toBeNull();
  });

  it("lists template and scale SVGs for Sub Workflow", () => {
    const video = listSubWorkflows("video");
    expect(video.map((item) => item.label)).toEqual([
      "Template A",
      "Template B",
      "Template C",
      "Template D",
      "Template E",
      "Template F",
      "Template G",
      "Template H",
      "Template I",
      "Template J",
      "Scale S1",
      "Scale S2",
      "Scale S3",
      "Scale S4",
      "Scale S5",
      "Scale S6",
      "Scale S7",
    ]);
    expect(subWorkflowSvgSrc("video")).toBe("/svg/video.template.a.workflow.svg");
    expect(subWorkflowSvgSrc("video", "video.scale.s1")).toBe("/svg/video.scale.s1.workflow.svg");
    expect(subWorkflowSvgSrc("video", "video.template.j")).toBe("/svg/video.template.j.workflow.svg");
    expect(listSubWorkflows("specials")).toEqual([]);
    expect(subWorkflowSvgSrc("specials")).toBeNull();
  });

  it("links every video agent id to Agent Profile Chat", () => {
    const hrefs = workflowAgentChatHrefs(videoWorkflowSvg);
    expect(hrefs).toHaveLength(114);
    expect(new Set(hrefs).size).toBe(114);
    expect(hrefs).toContain("video.director");
    expect(hrefs).toContain("video.orchestrator");
    expect(videoWorkflowSvg).toContain('target="_top"');
  });
});

describe("agent menu label", () => {
  it("names the Agent workspace Agent Profile", () => {
    expect(AGENT_MENU_LABEL).toBe("Agent Profile");
  });

  it("nests Main Workflow under Agent Workflow", () => {
    expect(WORKFLOW_MENU_LABEL).toBe("Agent Workflow");
    expect(WORKFLOW_TABS.some((tab) => tab.id === "main" && tab.path === "/workflow" && tab.label === "Main Workflow")).toBe(true);
    expect(WORKFLOW_TABS.some((tab) => tab.id === "sub" && tab.path === "/workflow/sub" && tab.label === "Sub Workflow" && tab.depth === 2)).toBe(true);
  });
});

describe("agent chat helpers", () => {
  it("keeps a Chat tab under the Agent menu", () => {
    expect(AGENT_TABS.some((tab) => tab.id === "chat" && tab.path === "chat" && tab.label === "Chat")).toBe(true);
  });

  it("keeps a Files tab under the Agent menu", () => {
    expect(AGENT_TABS.some((tab) => tab.id === "files" && tab.path === "files" && tab.label === "Files")).toBe(true);
  });

  it("sends only user/assistant turns as history", () => {
    const history = normalizeChatHistory([
      { role: "user", content: "hi" },
      { role: "assistant", content: "hello" },
      { role: "user", content: "   " },
    ]);
    expect(history).toEqual([
      { role: "user", content: "hi" },
      { role: "assistant", content: "hello" },
    ]);
  });

  it("treats length finish as an output-cap hit", () => {
    expect(chatHitOutputCap({ truncated: true })).toBe(true);
    expect(chatHitOutputCap({ finish_reason: "length" })).toBe(true);
    expect(chatHitOutputCap({ finish_reason: "stop" })).toBe(false);
  });
});
