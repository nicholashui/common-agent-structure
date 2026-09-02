import { useEffect, useMemo, useRef, useState } from "react";
import { inputClass } from "../components/ui";
import { collectAgentIds, filterAgentIds } from "../lib/agents";

export function AgentSwitcher({
  agents,
  extraIds,
  currentId,
  onSelect,
}: {
  agents: { agent_id: string }[];
  extraIds: string[];
  currentId?: string;
  onSelect: (agentId: string) => void;
}) {
  const [query, setQuery] = useState("");
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState(0);
  const root = useRef<HTMLDivElement>(null);
  const listRef = useRef<HTMLUListElement>(null);
  const ids = useMemo(() => collectAgentIds(agents, extraIds), [agents, extraIds]);
  const filtered = useMemo(() => filterAgentIds(ids, query, agents), [ids, query, agents]);

  useEffect(() => {
    setActive(0);
  }, [query, open]);

  useEffect(() => {
    function onPointer(event: MouseEvent) {
      if (!root.current?.contains(event.target as Node)) {
        setOpen(false);
      }
    }
    document.addEventListener("mousedown", onPointer);
    return () => document.removeEventListener("mousedown", onPointer);
  }, []);

  useEffect(() => {
    const node = listRef.current?.querySelector("[data-active='true']");
    if (node instanceof HTMLElement) {
      node.scrollIntoView({ block: "nearest" });
    }
  }, [active, filtered]);

  function choose(id: string) {
    onSelect(id);
    setQuery("");
    setOpen(false);
  }

  return (
    <div ref={root} className="relative w-[min(50%,28rem)] min-w-[16rem]">
      <label className="sr-only" htmlFor="agent-switcher">
        Search agents
      </label>
      <input
        id="agent-switcher"
        role="combobox"
        aria-expanded={open}
        aria-controls="agent-switcher-list"
        aria-autocomplete="list"
        autoComplete="off"
        className={`${inputClass} w-full font-mono`}
        placeholder={currentId || "search agent_id"}
        value={query}
        onFocus={() => setOpen(true)}
        onClick={() => setOpen(true)}
        onChange={(event) => {
          setQuery(event.target.value);
          setOpen(true);
        }}
        onKeyDown={(event) => {
          if (event.key === "Escape") {
            setOpen(false);
            return;
          }
          if (event.key === "ArrowDown") {
            event.preventDefault();
            setOpen(true);
            setActive((index) => Math.min(index + 1, Math.max(filtered.length - 1, 0)));
            return;
          }
          if (event.key === "ArrowUp") {
            event.preventDefault();
            setActive((index) => Math.max(index - 1, 0));
            return;
          }
          if (event.key === "Enter") {
            event.preventDefault();
            const match = filtered[active] || filtered[0] || query || currentId || "";
            if (match) {
              choose(match);
            }
          }
        }}
      />
      {open ? (
        <div className="absolute left-0 right-0 top-full z-50 mt-1 overflow-hidden rounded-lg border border-stone-200 bg-white shadow-md">
          <p className="border-b border-stone-100 px-3 py-1.5 text-[11px] text-stone-500">
            {filtered.length} of {ids.length} agents
          </p>
          {filtered.length ? (
            <ul
              id="agent-switcher-list"
              role="listbox"
              ref={listRef}
              className="max-h-80 overflow-y-auto py-1"
            >
              {filtered.map((id, index) => {
                const selected = id === currentId;
                const highlighted = index === active;
                return (
                  <li key={id} role="option" aria-selected={selected}>
                    <button
                      type="button"
                      data-active={highlighted ? "true" : "false"}
                      className={[
                        "flex w-full px-3 py-1.5 text-left font-mono text-xs",
                        highlighted ? "bg-indigo-50 text-indigo-800" : "text-stone-800 hover:bg-stone-50",
                        selected ? "font-semibold" : "",
                      ].join(" ")}
                      onMouseEnter={() => setActive(index)}
                      onClick={() => choose(id)}
                    >
                      {id}
                    </button>
                  </li>
                );
              })}
            </ul>
          ) : (
            <p className="px-3 py-2 text-xs text-stone-500">No matching agent_id</p>
          )}
        </div>
      ) : null}
    </div>
  );
}
