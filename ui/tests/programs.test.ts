import { describe, expect, it } from "vitest";
import { PROGRAM_MENU_LABEL, locationLabel } from "../src/shell/nav";
import { normalizeProgramCode, programCodeValid } from "../src/lib/programs";

describe("program code", () => {
  it("keeps lowercase english with no spaces", () => {
    expect(normalizeProgramCode("Spring Launch")).toBe("springlaunch");
    expect(normalizeProgramCode("ABC_def")).toBe("abcdef");
    expect(programCodeValid("springlaunch")).toBe(true);
    expect(programCodeValid("1bad")).toBe(false);
    expect(programCodeValid("")).toBe(false);
  });
});

describe("program nav", () => {
  it("places New program under Program", () => {
    expect(PROGRAM_MENU_LABEL).toBe("Program");
    expect(locationLabel("/programs/new")).toBe("Program / New program");
    expect(locationLabel("/programs/springlaunch")).toBe("Program / springlaunch");
  });
});
