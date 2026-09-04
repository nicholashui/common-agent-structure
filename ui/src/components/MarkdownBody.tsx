import type { ReactNode } from "react";
import { useState } from "react";
import ReactMarkdown from "react-markdown";
import rehypeHighlight from "rehype-highlight";
import remarkGfm from "remark-gfm";
import { htmlImgsToMarkdown, resolveAssetUrl } from "../help/markdown";
import { copyText } from "../lib/chat";

function childText(node: ReactNode): string {
  if (node == null || typeof node === "boolean") {
    return "";
  }
  if (typeof node === "string" || typeof node === "number") {
    return String(node);
  }
  if (Array.isArray(node)) {
    return node.map(childText).join("");
  }
  if (typeof node === "object" && "props" in node) {
    return childText((node as { props?: { children?: ReactNode } }).props?.children);
  }
  return "";
}

function CopyCodeButton({ code }: { code: string }) {
  const [copied, setCopied] = useState(false);
  return (
    <button
      type="button"
      className="absolute right-2 top-2 rounded-md border border-stone-200 bg-white/90 px-2 py-0.5 text-[10px] font-medium text-stone-600 hover:text-stone-900"
      data-testid="copy-code"
      onClick={() => {
        void copyText(code).then((ok) => {
          if (ok) {
            setCopied(true);
            window.setTimeout(() => setCopied(false), 1200);
          }
        });
      }}
    >
      {copied ? "Copied" : "Copy"}
    </button>
  );
}

export function MarkdownBody({
  text,
  compact = false,
  basePath,
}: {
  text: string;
  compact?: boolean;
  basePath?: string;
}) {
  const source = htmlImgsToMarkdown(text);
  return (
    <div className={`md-body${compact ? " md-body-compact" : ""}`} data-testid="markdown-body">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[rehypeHighlight]}
        urlTransform={basePath ? (url) => resolveAssetUrl(url, basePath) : undefined}
        components={{
          a: ({ href, children }) => (
            <a href={href} className="text-indigo-700 underline decoration-indigo-200 hover:text-indigo-900">
              {children}
            </a>
          ),
          img: ({ src, alt }) => (
            <img src={src} alt={alt ?? ""} className="my-3 max-w-full rounded-lg border border-stone-200" />
          ),
          pre: ({ children }) => (
            <div className="relative">
              <CopyCodeButton code={childText(children).replace(/\n$/, "")} />
              <pre>{children}</pre>
            </div>
          ),
        }}
      >
        {source}
      </ReactMarkdown>
    </div>
  );
}
