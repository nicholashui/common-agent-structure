import { describe, expect, it } from "vitest";
import { GRAPH_KIND, LIGHT_SVG_OVERRIDE, graphEdgeStyle, socketColor } from "../src/lib/graphStyle";
import videoWorkflowSvg from "../public/svg/video.workflow.svg?raw";

describe("ComfyUI-like graph tokens", () => {
  it("keeps socket colors stable for a named bus", () => {
    expect(socketColor("video.director")).toBe(socketColor("video.director"));
    expect(socketColor("next")).not.toBe(socketColor("video.critic"));
  });

  it("uses bezier edges and a loop stroke", () => {
    const next = graphEdgeStyle({ handle: "next" });
    const loop = graphEdgeStyle({ loop: true, handle: "video.critic" });
    expect(next.type).toBe("default");
    expect(loop.animated).toBe(true);
    expect(loop.style.stroke).toBe("#e65100");
    expect(loop.style.strokeDasharray).toBe("6 4");
  });

  it("assigns a title color for every node kind", () => {
    expect(GRAPH_KIND.start.title).toMatch(/^#/);
    expect(GRAPH_KIND.agent.title).not.toBe(GRAPH_KIND.human.title);
    expect(GRAPH_KIND.output.mini).toMatch(/^#/);
  });

  it("marks the main workflow SVG as the dark graph visual system", () => {
    expect(videoWorkflowSvg).toContain('data-visual-system="casops-workflow-v3"');
    expect(videoWorkflowSvg).toContain(".canvas{fill:url(#graph-grid)}");
    expect(videoWorkflowSvg).toContain('class="socket socket-in"');
    expect(videoWorkflowSvg).toContain('class="comfy-node"');
    expect(videoWorkflowSvg).toContain(">AGENT</text>");
    expect(videoWorkflowSvg).toContain(">START</text>");
  });

  it("ships a light-theme SVG override that follows the header toggle", () => {
    expect(LIGHT_SVG_OVERRIDE).toContain(".canvas{fill:#f4f7fb!important}");
    expect(LIGHT_SVG_OVERRIDE).toContain(".section-title{fill:#0f172a!important}");
  });
});
