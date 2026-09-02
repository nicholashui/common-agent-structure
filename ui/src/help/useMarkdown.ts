import { useEffect, useState } from "react";
import { isHtmlFallback, isSoftMissStatus } from "./markdown";

export type MarkdownStatus = "idle" | "loading" | "ready" | "error" | "empty";

export interface MarkdownState {
  status: MarkdownStatus;
  path: string | null;
  text: string;
  error: string | null;
}

const cache = new Map<string, string>();

export function markdownCacheClear(): void {
  cache.clear();
}

async function fetchMarkdown(path: string): Promise<"soft" | { kind: "ready"; text: string } | { kind: "error"; message: string }> {
  const cached = cache.get(path);
  if (cached !== undefined) {
    return { kind: "ready", text: cached };
  }
  let response: Response;
  try {
    response = await fetch(path, {
      credentials: "same-origin",
      headers: { Accept: "text/markdown, text/plain;q=0.9, */*;q=0.1" },
    });
  } catch (err) {
    return { kind: "error", message: err instanceof Error ? err.message : String(err) };
  }
  const contentType = response.headers.get("content-type");
  const body = await response.text();
  if (isSoftMissStatus(response.status) || isHtmlFallback(contentType, body)) {
    return "soft";
  }
  if (!response.ok) {
    return { kind: "error", message: `${response.status} ${response.statusText || "request failed"}`.trim() };
  }
  cache.set(path, body);
  return { kind: "ready", text: body };
}

export function useMarkdown(candidates: string[], enabled: boolean): MarkdownState {
  const [state, setState] = useState<MarkdownState>({
    status: enabled ? "loading" : "idle",
    path: null,
    text: "",
    error: null,
  });

  useEffect(() => {
    if (!enabled) {
      setState({ status: "idle", path: null, text: "", error: null });
      return;
    }
    const paths = candidates.filter(Boolean);
    if (!paths.length) {
      setState({ status: "empty", path: null, text: "", error: null });
      return;
    }
    let cancelled = false;
    setState({ status: "loading", path: null, text: "", error: null });
    void (async () => {
      let lastError: string | null = null;
      for (const path of paths) {
        const result = await fetchMarkdown(path);
        if (cancelled) {
          return;
        }
        if (result === "soft") {
          continue;
        }
        if (result.kind === "ready") {
          setState({ status: "ready", path, text: result.text, error: null });
          return;
        }
        lastError = `${path}: ${result.message}`;
      }
      if (cancelled) {
        return;
      }
      if (lastError) {
        setState({ status: "error", path: paths[0] ?? null, text: "", error: lastError });
        return;
      }
      setState({ status: "empty", path: paths[0] ?? null, text: "", error: null });
    })();
    return () => {
      cancelled = true;
    };
  }, [enabled, candidates.join("|")]);

  return state;
}
