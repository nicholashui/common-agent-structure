/** Repo-relative path for UI display. Never a drive letter, UNC, or /Users absolute. */

const REPO_MARKERS = [
  "/agents/",
  "/program/",
  "/project/",
  "/logs/",
  "/spec/",
  "/sample/",
  "/docs/",
  "/src/",
  "/ui/",
  "/issues/",
  "/book/",
  "/tests/",
  "/evals/",
  "/vendor/",
];

export function displayRelativePath(path: string | undefined | null): string {
  const raw = String(path ?? "").trim();
  if (!raw) {
    return "";
  }
  let posix = raw.replace(/\\/g, "/");
  posix = posix.replace(/^file:\/\//i, "");
  posix = posix.replace(/^[A-Za-z]:/, "");
  posix = posix.replace(/^\/\/[^/]+\/[^/]+/, "");
  posix = posix.replace(/\/{2,}/g, "/");
  const lower = posix.toLowerCase();
  let at = -1;
  for (const marker of REPO_MARKERS) {
    const idx = lower.lastIndexOf(marker);
    if (idx > at) {
      at = idx;
    }
  }
  if (at >= 0) {
    return posix.slice(at + 1);
  }
  return posix.replace(/^\/+/, "");
}
