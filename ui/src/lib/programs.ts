/** Program Code: lowercase English letters and digits, no spaces. */

export function normalizeProgramCode(raw: string): string {
  return String(raw || "")
    .toLowerCase()
    .replace(/[^a-z0-9]/g, "");
}

export function programCodeValid(code: string): boolean {
  return /^[a-z][a-z0-9]{0,47}$/.test(code);
}
