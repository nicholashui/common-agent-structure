import { MarkdownBody } from "../components/MarkdownBody";
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
  return <MarkdownBody text={state.text} basePath={state.path || "/docs/"} />;
}
