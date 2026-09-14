export type ChatOption = {
  id: string;
  label: string;
  why: string;
};

export type ParsedOptionBlock = {
  body: string;
  options: ChatOption[];
  recommend: string;
  selected: string;
  selectedBy: string;
  reason: string;
  decideBy: string;
};

const OPTION_RE = /^OPTION\s+([A-Za-z0-9][A-Za-z0-9_-]*)[:.)]\s*(.+)$/i;
const RECOMMEND_RE = /^RECOMMEND:\s*(\S+)/i;
const DECIDE_BY_RE = /^DECIDE_BY:\s*(\S+)/i;
const SELECTED_RE = /^SELECTED:\s*(?:OPTION\s*)?([A-Za-z0-9][A-Za-z0-9_-]*)\b/i;
const SELECTED_BY_RE = /^SELECTED_BY:\s*(.+)$/i;
const REASON_RE = /^REASON:\s*(.+)$/i;

function splitLabelWhy(rest: string): { label: string; why: string } {
  const cut = rest.split(/\s+[—–-]\s+|\s+\((recommend)\)\s*$/i);
  const label = (cut[0] || rest).replace(/\s+\(recommend\)\s*$/i, "").trim();
  const why = rest.includes("—") ? rest.split("—").slice(1).join("—").replace(/\s+\(recommend\)\s*$/i, "").trim() : "";
  return { label, why };
}

export function parseOptionBlock(text: string): ParsedOptionBlock {
  const options: ChatOption[] = [];
  const kept: string[] = [];
  let recommend = "";
  let selected = "";
  let selectedBy = "";
  let reason = "";
  let decideBy = "";
  for (const line of (text || "").split(/\r?\n/)) {
    const option = OPTION_RE.exec(line.trim());
    if (option) {
      const { label, why } = splitLabelWhy(option[2].trim());
      options.push({ id: option[1], label, why });
      continue;
    }
    const rec = RECOMMEND_RE.exec(line.trim());
    if (rec) {
      recommend = rec[1];
      continue;
    }
    const dec = DECIDE_BY_RE.exec(line.trim());
    if (dec) {
      decideBy = dec[1];
      continue;
    }
    const sel = SELECTED_RE.exec(line.trim());
    if (sel) {
      selected = sel[1];
      const dash = line.indexOf("—");
      if (dash >= 0 && !options.some((row) => row.id === selected)) {
        options.push({ id: selected, label: line.slice(dash + 1).trim(), why: "" });
      }
      continue;
    }
    const by = SELECTED_BY_RE.exec(line.trim());
    if (by) {
      selectedBy = by[1].trim();
      continue;
    }
    const whyLine = REASON_RE.exec(line.trim());
    if (whyLine) {
      reason = whyLine[1].trim();
      continue;
    }
    kept.push(line);
  }
  return {
    body: kept.join("\n").replace(/\n{3,}/g, "\n\n").trim(),
    options,
    recommend,
    selected,
    selectedBy,
    reason,
    decideBy,
  };
}

export function choiceIdFromAsk(askText: string, typed: string): string {
  const parsed = parseOptionBlock(askText);
  const want = (typed || "").trim();
  const hit = parsed.options.find((row) => row.id === want || row.label === want);
  return hit?.id || want;
}
