/** Cheap local follow-up chips. Does not call the host LLM. */

const FALLBACKS = [
  "Summarize that in five bullets",
  "What constraints or risks did you assume?",
  "Give one concrete next step I can take",
];

export function followUpChips(assistant: string, limit = 3): string[] {
  const questions: string[] = [];
  for (const raw of assistant.split(/\n+/)) {
    const text = raw.replace(/^[-*]\s+/, "").replace(/^\d+\.\s+/, "").trim();
    if (!text.endsWith("?") || text.length < 12 || text.length > 140) {
      continue;
    }
    if (!questions.includes(text)) {
      questions.push(text);
    }
    if (questions.length >= limit) {
      return questions.slice(0, limit);
    }
  }
  for (const item of FALLBACKS) {
    if (questions.length >= limit) {
      break;
    }
    if (!questions.includes(item)) {
      questions.push(item);
    }
  }
  return questions.slice(0, limit);
}
