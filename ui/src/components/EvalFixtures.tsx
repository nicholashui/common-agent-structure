import type { EvalFixture } from "../api/types";
import { clipPreview, fixtureMessage, fixtureTitle } from "../lib/fixtures";
import { GhostButton } from "./ui";

export function CharacterizationBadge() {
  return (
    <span className="rounded-full border border-amber-200 bg-amber-50 px-2.5 py-1 text-xs text-amber-800">
      CHARACTERIZATION
    </span>
  );
}

export function ChatFixtureList({
  items,
  onLoad,
  compact = false,
}: {
  items: EvalFixture[];
  onLoad: (item: EvalFixture) => void;
  compact?: boolean;
}) {
  if (!items.length) {
    return null;
  }
  return (
    <ul className={compact ? "space-y-2" : "space-y-3"} data-testid="chat-fixtures">
      {items.map((item) => (
        <li key={item.id} className="rounded-xl border border-stone-200 bg-stone-50 p-3">
          <div className="flex flex-wrap items-center gap-2">
            <GhostButton type="button" data-testid="chat-load-fixture" onClick={() => onLoad(item)}>
              Load {item.id}
            </GhostButton>
            <span className="font-mono text-[11px] text-stone-500">{item.id}</span>
          </div>
          <p className="mt-2 text-sm font-medium text-stone-800">{fixtureTitle(item)}</p>
          <p className="mt-1 text-sm text-stone-600">{clipPreview(fixtureMessage(item), compact ? 90 : 160)}</p>
        </li>
      ))}
    </ul>
  );
}
