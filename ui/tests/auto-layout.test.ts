import { describe, expect, it } from "vitest";
import { applyAutoLayout, autoLayoutPositions } from "../src/lib/autoLayout";

describe("workflow auto layout", () => {
  it("places a successor to the right on LR layout", () => {
    const pos = autoLayoutPositions(
      [
        { id: "a", width: 320, height: 200 },
        { id: "b", width: 320, height: 200 },
      ],
      [{ source: "a", target: "b" }],
      { direction: "LR", rankGap: 80, packGap: 20 },
    );
    expect(pos.a.x).toBe(0);
    expect(pos.b.x).toBeGreaterThan(pos.a.x);
    expect(pos.b.x).toBe(400);
  });

  it("keeps Create Project left and Output right", () => {
    const laid = applyAutoLayout(
      [
        { id: "create-project", position: { x: 900, y: 40 }, data: { kind: "start" } },
        { id: "agent-1", position: { x: 10, y: 10 }, data: { kind: "agent" } },
        { id: "output-prompt", position: { x: 20, y: 800 }, data: { kind: "output" } },
      ],
      [
        { source: "create-project", target: "agent-1" },
        { source: "agent-1", target: "output-prompt" },
      ],
      { direction: "LR", defaultWidth: 320, defaultHeight: 200 },
    );
    const byId = Object.fromEntries(laid.map((node) => [node.id, node.position]));
    expect(byId["create-project"].x).toBeLessThan(byId["agent-1"].x);
    expect(byId["agent-1"].x).toBeLessThan(byId["output-prompt"].x);
  });

  it("does not throw on a loop edge and still assigns coordinates", () => {
    const pos = autoLayoutPositions(
      [
        { id: "a", width: 100, height: 80 },
        { id: "b", width: 100, height: 80 },
      ],
      [
        { source: "a", target: "b" },
        { source: "b", target: "a" },
      ],
    );
    expect(pos.a).toEqual({ x: expect.any(Number), y: expect.any(Number) });
    expect(pos.b).toEqual({ x: expect.any(Number), y: expect.any(Number) });
  });

  it("places a successor below on TB layout", () => {
    const pos = autoLayoutPositions(
      [
        { id: "root", width: 184, height: 68 },
        { id: "leaf", width: 184, height: 68 },
      ],
      [{ source: "root", target: "leaf" }],
      { direction: "TB", rankGap: 96, packGap: 24 },
    );
    expect(pos.leaf.y).toBeGreaterThan(pos.root.y);
  });
});
