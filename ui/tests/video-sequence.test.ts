import { describe, expect, it } from "vitest";
import type { SequenceManifest } from "../src/api/types";

function sequenceNote(seq: SequenceManifest): string {
  const count = seq.clips.length;
  const unit = seq.policy?.generation_unit || "clip";
  return `Sequence · ${count} clip${count === 1 ? "" : "s"} · generation unit: ${unit}`;
}

describe("sequence manifest (Chat strip)", () => {
  it("states clip as the generation unit and does not imply one fused take", () => {
    const seq: SequenceManifest = {
      kind: "sequence",
      sequence_id: "SEQ.demo.001",
      clips: [
        { clip_id: "CLIP.demo.001", order: 1, start_s: 0, end_s: 6 },
        { clip_id: "CLIP.demo.002", order: 2, start_s: 6, end_s: 12 },
      ],
      policy: { generation_unit: "clip", concat: "post" },
    };
    const note = sequenceNote(seq);
    expect(note).toContain("2 clips");
    expect(note).toContain("generation unit: clip");
    expect(seq.policy?.concat).toBe("post");
  });
});
