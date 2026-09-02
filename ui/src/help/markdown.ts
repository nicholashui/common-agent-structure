const HTML_START = /^\s*(<!doctype html|<html[\s>])/i;

export function isHtmlFallback(contentType: string | null | undefined, body: string): boolean {
  if ((contentType || "").toLowerCase().includes("text/html")) {
    return true;
  }
  return HTML_START.test(body);
}

export function htmlImgsToMarkdown(source: string): string {
  return source.replace(/<img\b([^>]*)\/?>/gi, (_all, attrs: string) => {
    const src = /(?:^|\s)src\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+))/i.exec(attrs);
    const alt = /(?:^|\s)alt\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+))/i.exec(attrs);
    const href = src?.[1] ?? src?.[2] ?? src?.[3] ?? "";
    const label = alt?.[1] ?? alt?.[2] ?? alt?.[3] ?? "";
    return `![${label}](${href})`;
  });
}

export function resolveAssetUrl(src: string, markdownPath: string): string {
  const value = src.trim();
  if (!value) {
    return value;
  }
  if (/^(https?:|data:|blob:|mailto:|#)/i.test(value)) {
    return value;
  }
  if (value.startsWith("/")) {
    return value;
  }
  const base = markdownPath.replace(/[^/]+$/, "");
  try {
    return new URL(value, `https://help.local${base}`).pathname;
  } catch {
    return value;
  }
}

export function isSoftMissStatus(status: number): boolean {
  return status === 404;
}
