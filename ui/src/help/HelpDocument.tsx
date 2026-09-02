import { useMemo, useState } from "react";
import { docCandidates, paramsFromPathname } from "./paths";
import { HELP_DEFAULT_TAB, HELP_TABS } from "./tabs";
import { MarkdownView } from "./MarkdownView";
import { useMarkdown } from "./useMarkdown";

export function HelpDocument({
  pathname,
  params,
  enabled,
}: {
  pathname: string;
  params: Record<string, string | undefined>;
  enabled: boolean;
}) {
  const [tabId, setTabId] = useState(HELP_DEFAULT_TAB);
  const active = HELP_TABS.some((tab) => tab.id === tabId) ? tabId : HELP_DEFAULT_TAB;
  const mergedParams = { ...paramsFromPathname(pathname), ...params };
  const paramKey = JSON.stringify(mergedParams);
  const candidates = useMemo(() => {
    const tab = HELP_TABS.find((item) => item.id === active);
    if (tab?.mdPath) {
      return [tab.mdPath];
    }
    return docCandidates(pathname, JSON.parse(paramKey) as Record<string, string | undefined>, active);
  }, [pathname, paramKey, active]);
  const markdown = useMarkdown(candidates, enabled);

  return (
    <div className="flex min-h-0 flex-1 flex-col">
      <div className="flex flex-wrap gap-1 border-b border-stone-200 pb-2" role="tablist" aria-label="Document type">
        {HELP_TABS.map((tab) => {
          const selected = tab.id === active;
          return (
            <button
              key={tab.id}
              type="button"
              role="tab"
              aria-selected={selected}
              className={`rounded-full px-3 py-1 text-xs font-medium ${
                selected
                  ? "bg-stone-900 text-white dark:bg-stone-100 dark:text-stone-900"
                  : "bg-stone-100 text-stone-600 hover:bg-stone-200"
              }`}
              onClick={() => setTabId(tab.id)}
            >
              {tab.label}
            </button>
          );
        })}
      </div>
      <div className="min-h-0 flex-1 overflow-auto pt-3" role="tabpanel">
        <MarkdownView state={markdown} />
      </div>
    </div>
  );
}
