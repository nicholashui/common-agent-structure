import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { htmlImgsToMarkdown, resolveAssetUrl } from "./markdown";
import type { MarkdownState } from "./useMarkdown";

export function MarkdownView({ state }: { state: MarkdownState }) {
  if (state.status === "idle") {
    return null;
  }
  if (state.status === "loading") {
    return <p className="text-sm text-stone-500">Loading document…</p>;
  }
  if (state.status === "empty") {
    return <p className="text-sm text-stone-500">No document for this screen yet.</p>;
  }
  if (state.status === "error") {
    return (
      <div className="rounded-xl border border-red-200 bg-red-50 p-3 text-sm text-red-800">
        <p className="font-medium">Could not load document.</p>
        {state.path ? <p className="mt-1 font-mono text-xs">{state.path}</p> : null}
        {state.error ? <p className="mt-1 text-xs">{state.error}</p> : null}
      </div>
    );
  }
  const basePath = state.path || "/docs/";
  const source = htmlImgsToMarkdown(state.text);
  return (
    <div className="help-md text-sm text-stone-800">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        urlTransform={(url) => resolveAssetUrl(url, basePath)}
        components={{
          a: ({ href, children }) => (
            <a href={href} className="text-indigo-700 underline decoration-indigo-200 hover:text-indigo-900">
              {children}
            </a>
          ),
          img: ({ src, alt }) => (
            <img src={src} alt={alt ?? ""} className="my-3 max-w-full rounded-lg border border-stone-200" />
          ),
        }}
      >
        {source}
      </ReactMarkdown>
    </div>
  );
}
