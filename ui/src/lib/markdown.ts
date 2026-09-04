export function isMarkdownPath(path: string): boolean {
  return path.replace(/\\/g, "/").toLowerCase().endsWith(".md");
}

export function isJsonPath(path: string): boolean {
  return path.replace(/\\/g, "/").toLowerCase().endsWith(".json");
}
