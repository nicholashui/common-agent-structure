import { describe, expect, it } from "vitest";
import {
  applyAutoLayout,
  autoLayoutPositions,
  LAYOUT_ALGORITHMS,
  layoutHasOverlap,
} from "../src/lib/autoLayout";

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

  it("detects stacked project nodes that would hide edges", () => {
    expect(
      layoutHasOverlap(
        [
          { id: "a", position: { x: 720, y: 40 }, width: 320, height: 280 },
          { id: "b", position: { x: 720, y: 160 }, width: 320, height: 280 },
        ],
        24,
      ),
    ).toBe(true);
    const laid = applyAutoLayout(
      [
        { id: "a", position: { x: 720, y: 40 }, width: 320, height: 280 },
        { id: "b", position: { x: 720, y: 160 }, width: 320, height: 280 },
      ],
      [{ source: "a", target: "b" }],
      { direction: "LR", packGap: 48, rankGap: 112 },
    );
    expect(layoutHasOverlap(laid, 24)).toBe(false);
  });

  it("exposes distinct algorithms that place the same graph differently", () => {
    expect(LAYOUT_ALGORITHMS.map((row) => row.id)).toEqual([
      "layered-lr",
      "layered-tb",
      "grid",
      "radial",
      "force",
    ]);
    const nodes = [
      { id: "create-project", position: { x: 0, y: 0 }, width: 320, height: 160, data: { kind: "start" } },
      { id: "agent-1", position: { x: 10, y: 10 }, width: 320, height: 200, data: { kind: "agent" } },
      { id: "agent-2", position: { x: 20, y: 20 }, width: 320, height: 200, data: { kind: "agent" } },
      { id: "output-prompt", position: { x: 30, y: 30 }, width: 320, height: 160, data: { kind: "output" } },
    ];
    const edges = [
      { source: "create-project", target: "agent-1" },
      { source: "agent-1", target: "agent-2" },
      { source: "agent-2", target: "output-prompt" },
    ];
    const lr = applyAutoLayout(nodes, edges, { algorithm: "layered-lr" });
    const tb = applyAutoLayout(nodes, edges, { algorithm: "layered-tb" });
    const grid = applyAutoLayout(nodes, edges, { algorithm: "grid" });
    const radial = applyAutoLayout(nodes, edges, { algorithm: "radial" });
    const force = applyAutoLayout(nodes, edges, { algorithm: "force" });
    const lrBy = Object.fromEntries(lr.map((node) => [node.id, node.position]));
    const tbBy = Object.fromEntries(tb.map((node) => [node.id, node.position]));
    const gridBy = Object.fromEntries(grid.map((node) => [node.id, node.position]));
    expect(lrBy["agent-1"].x).toBeGreaterThan(lrBy["create-project"].x);
    expect(tbBy["agent-1"].y).toBeGreaterThan(tbBy["create-project"].y);
    expect(new Set(grid.map((node) => `${node.position.x},${node.position.y}`)).size).toBe(4);
    expect(radial.map((node) => node.position.x + node.position.y).some((sum) => sum !== 0)).toBe(true);
    expect(force.every((node) => Number.isFinite(node.position.x) && Number.isFinite(node.position.y))).toBe(true);
    expect(`${lrBy["agent-2"].x},${lrBy["agent-2"].y}`).not.toBe(`${tbBy["agent-2"].x},${tbBy["agent-2"].y}`);
    expect(`${lrBy["agent-1"].x},${lrBy["agent-1"].y}`).not.toBe(`${gridBy["agent-1"].x},${gridBy["agent-1"].y}`);
  });
});
