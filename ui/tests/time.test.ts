import { describe, expect, it } from "vitest";
import { formatHktClock, formatHktIso, formatHktStamp } from "../src/lib/time";

describe("Hong Kong timestamps", () => {
  it("converts UTC midnight to +08:00", () => {
    expect(formatHktIso("2026-09-07T00:00:00.000Z")).toBe("2026-09-07T08:00:00.000+08:00");
  });

  it("shows HKT clock from a Z timestamp", () => {
    expect(formatHktClock("2026-09-07T03:55:15.563Z")).toBe("11:55:15");
    expect(formatHktClock("2026-09-07T03:55:15.563Z", true)).toBe("11:55:15.563");
  });

  it("stamps filenames in HKT", () => {
    expect(formatHktStamp("2026-09-07T16:05:09.000Z")).toBe("2026-09-08-00-05-09");
  });

  it("keeps an already-HKT ISO string on +08:00", () => {
    expect(formatHktIso("2026-09-07T08:00:00.000+08:00")).toBe("2026-09-07T08:00:00.000+08:00");
  });
});
