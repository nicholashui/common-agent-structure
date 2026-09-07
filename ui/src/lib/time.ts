/** Hong Kong civil time (UTC+8, no DST) for operator-facing timestamps. */

export const HKT_TZ = "Asia/Hong_Kong";
export const HKT_OFFSET = "+08:00";

type TimeParts = {
  year: string;
  month: string;
  day: string;
  hour: string;
  minute: string;
  second: string;
  ms: string;
};

function hktParts(date: Date): TimeParts | null {
  if (Number.isNaN(date.getTime())) {
    return null;
  }
  const fmt = new Intl.DateTimeFormat("en-GB", {
    timeZone: HKT_TZ,
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hourCycle: "h23",
    fractionalSecondDigits: 3,
  });
  const bag: Record<string, string> = {};
  for (const part of fmt.formatToParts(date)) {
    if (part.type !== "literal") {
      bag[part.type] = part.value;
    }
  }
  return {
    year: bag.year,
    month: bag.month,
    day: bag.day,
    hour: bag.hour,
    minute: bag.minute,
    second: bag.second,
    ms: (bag.fractionalSecond || "000").padEnd(3, "0").slice(0, 3),
  };
}

function toDate(input?: Date | string | number | null): Date | null {
  if (input == null || input === "") {
    return null;
  }
  const date = input instanceof Date ? input : new Date(input);
  return Number.isNaN(date.getTime()) ? null : date;
}

export function formatHktIso(input?: Date | string | number | null): string {
  const parts = toDate(input ?? new Date());
  const bag = parts ? hktParts(parts) : null;
  if (!bag) {
    return "";
  }
  return `${bag.year}-${bag.month}-${bag.day}T${bag.hour}:${bag.minute}:${bag.second}.${bag.ms}${HKT_OFFSET}`;
}

export function formatHktClock(input?: Date | string | number | null, withMs = false): string {
  const date = toDate(input ?? null);
  const bag = date ? hktParts(date) : null;
  if (!bag) {
    return "";
  }
  return withMs
    ? `${bag.hour}:${bag.minute}:${bag.second}.${bag.ms}`
    : `${bag.hour}:${bag.minute}:${bag.second}`;
}

export function formatHktDateTime(input?: Date | string | number | null): string {
  const date = toDate(input ?? null);
  const bag = date ? hktParts(date) : null;
  if (!bag) {
    return "";
  }
  return `${bag.year}-${bag.month}-${bag.day} ${bag.hour}:${bag.minute}:${bag.second}`;
}

export function formatHktStamp(input?: Date | string | number | null): string {
  const date = toDate(input ?? new Date());
  const bag = date ? hktParts(date) : null;
  if (!bag) {
    return "";
  }
  return `${bag.year}-${bag.month}-${bag.day}-${bag.hour}-${bag.minute}-${bag.second}`;
}

export function nowHktIso(): string {
  return formatHktIso(new Date());
}
