export function parseMaybeJson(value: unknown): unknown {
  if (typeof value !== "string") {
    return value;
  }
  try {
    return JSON.parse(value) as unknown;
  } catch {
    return value;
  }
}

export function pretty(value: unknown): string {
  const parsed = parseMaybeJson(value);
  if (typeof parsed === "string") {
    return parsed;
  }
  try {
    return JSON.stringify(parsed, null, 2);
  } catch {
    return String(value);
  }
}

export function asRecord(value: unknown): Record<string, unknown> {
  return value && typeof value === "object" && !Array.isArray(value) ? (value as Record<string, unknown>) : {};
}

export function asString(value: unknown, fallback = ""): string {
  return typeof value === "string" ? value : fallback;
}
