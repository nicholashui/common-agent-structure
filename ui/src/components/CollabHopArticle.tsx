import { OptionTags } from "./OptionTags";
import { parseOptionBlock } from "../lib/chatOptions";
import {
  commSeq,
  displayPartyName,
  hopExtra,
  shownOptionId,
  sourceCommId,
} from "../lib/projectChat";
import { mediaHref } from "../lib/projectChat";
import type { ProjectDecision, ProjectMedia } from "../api/types";

export type CollabHop = {
  id: string;
  from: string;
  to: string;
  kind: string;
  text?: string;
  pass_id?: string;
  created_at?: string;
  live?: boolean;
  provider?: string;
  error?: string;
  agents?: string[];
  media?: ProjectMedia | null;
  input_tags?: { comm_id: string; label: string; project_id?: string }[];
  output_tags?: { comm_id: string; label: string; project_id?: string }[];
};

export function kindTone(kind: string, from: string): string {
  if (from === "human_operator" || (kind === "instruction" && from === "human_operator")) {
    return "border-indigo-200 bg-indigo-50 dark:border-indigo-800 dark:bg-indigo-950";
  }
  if (kind === "output" || kind === "consolidated" || kind === "assembled" || kind === "generated_media") {
    return "border-amber-200 bg-amber-50 dark:border-amber-800 dark:bg-amber-950";
  }
  if (kind === "repair") {
    return "border-orange-200 bg-orange-50 dark:border-orange-800 dark:bg-orange-950";
  }
  if (kind === "human_ask") {
    return "border-rose-200 bg-rose-50 dark:border-rose-800 dark:bg-rose-950";
  }
  if (kind === "choice") {
    return "border-indigo-200 bg-indigo-50 dark:border-indigo-800 dark:bg-indigo-950";
  }
  if (kind === "induce") {
    return "border-stone-200 bg-white dark:border-stone-700 dark:bg-stone-900";
  }
  if (kind === "return") {
    return "border-stone-200 bg-stone-50 dark:border-stone-700 dark:bg-stone-900";
  }
  return "border-stone-200 bg-white dark:border-stone-700 dark:bg-stone-900";
}

function ChatMedia({ media, scopeId }: { media: ProjectMedia; scopeId: string }) {
  const src = mediaHref(media.url, scopeId);
  const poster = media.poster ? mediaHref(media.poster, scopeId) : undefined;
  if (!src) {
    return null;
  }
  if (media.kind === "video") {
    return (
      <div className="mt-3" data-testid="project-chat-video-wrap">
        <video
          className="mx-auto block w-full max-w-[22rem] max-h-[36rem] rounded-xl bg-black"
          src={src}
          controls
          playsInline
          preload="metadata"
          poster={poster}
          data-testid="project-chat-video"
        >
          <source src={src} type="video/mp4" />
          <a href={src}>Open video</a>
        </video>
        <p className="mt-1 text-[10px] text-stone-500">
          Click play in this bubble. Saved as {media.name || "clip.mp4"} in output/.
        </p>
      </div>
    );
  }
  if (media.kind === "image") {
    return (
      <img
        className="mt-3 w-full rounded-xl"
        src={src}
        alt={media.name || "generated still"}
        data-testid="project-chat-still"
      />
    );
  }
  return null;
}

export function CollabHopArticle({
  item,
  hops,
  focusComm,
  focusOpt,
  listedDecisions,
  scopeId,
  testIdPrefix = "project-chat",
  onPickOption,
  onOpenTag,
}: {
  item: CollabHop;
  hops: CollabHop[];
  focusComm: string;
  focusOpt: string;
  listedDecisions: ProjectDecision[];
  scopeId: string;
  testIdPrefix?: string;
  onPickOption: (agentId: string, optionId: string, commId?: string) => void;
  onOpenTag: (scopeId: string, commId: string) => void;
}) {
  const parsed = parseOptionBlock(item.text || "");
  const fromDecision = listedDecisions.find((dec) => dec.agent_id === item.from || dec.agent_id === item.to);
  const followChoice =
    item.kind === "human_ask"
      ? hops.find(
          (row) =>
            row.kind === "choice" &&
            row.from === "human_operator" &&
            row.to === item.from &&
            commSeq(row.id) > commSeq(item.id),
        )
      : undefined;
  const followParsed = followChoice ? parseOptionBlock(followChoice.text || "") : null;
  const shown = shownOptionId({
    kind: item.kind,
    optionIds: parsed.options.map((row) => row.id),
    parsedSelected: parsed.selected,
    followSelected: followParsed?.selected,
    expertChosen: fromDecision?.chosen,
    recommend: parsed.recommend,
    focusOpt,
    focusMatchesComm: focusComm === item.id,
  });
  const agentId =
    item.kind === "human_ask"
      ? item.from
      : item.kind === "return"
        ? item.from
        : item.kind === "choice"
          ? item.to
          : fromDecision?.agent_id || item.from;
  const sourceId = sourceCommId(item, hops);
  const fromName = displayPartyName(item.from);
  const toName = displayPartyName(item.to);
  const extra = hopExtra(item, parsed.options.length);
  return (
    <article
      data-comm-id={item.id}
      data-testid={`${testIdPrefix}-${item.id}`}
      className={[
        "rounded-2xl border px-4 py-3",
        kindTone(item.kind, item.from),
        focusComm === item.id ? "ring-2 ring-amber-400" : "",
      ].join(" ")}
    >
      <p className="text-[11px] text-stone-600" data-testid={`${testIdPrefix}-header-${item.id}`}>
        {sourceId ? (
          <button
            type="button"
            className="font-semibold text-indigo-700 underline decoration-indigo-300 underline-offset-2 hover:text-indigo-900"
            data-testid={`${testIdPrefix}-output-agent-${item.id}`}
            onClick={() => onOpenTag(scopeId, sourceId)}
          >
            {fromName}
          </button>
        ) : (
          <span className="font-semibold text-stone-800" data-testid={`${testIdPrefix}-output-agent-${item.id}`}>
            {fromName}
          </span>
        )}
        <span className="text-stone-400"> → </span>
        <span className="font-semibold text-stone-800">{toName}</span>
        <span className="text-stone-400"> | {extra}</span>
      </p>
      {parsed.body ? (
        <pre className="mt-2 max-h-[28rem] overflow-auto whitespace-pre-wrap font-sans text-sm text-stone-800">
          {parsed.body}
        </pre>
      ) : item.kind === "choice" || parsed.options.length ? null : (
        <pre className="mt-2 max-h-[28rem] overflow-auto whitespace-pre-wrap font-sans text-sm text-stone-800">
          {item.text}
        </pre>
      )}
      {item.agents?.length ? (
        <p className="mt-2 text-[10px] text-stone-500">Agents {item.agents.join(" · ")}</p>
      ) : null}
      {item.media ? <ChatMedia media={item.media} scopeId={scopeId} /> : null}
      <OptionTags
        options={parsed.options}
        selected={shown}
        recommend={item.kind === "human_ask" ? parsed.recommend : parsed.recommend || fromDecision?.recommend}
        commId={item.id}
        owner={item.from}
        onPick={(optionId) => onPickOption(agentId, optionId, item.id)}
      />
      {parsed.reason ? <p className="mt-1 text-[11px] text-indigo-900">Reason: {parsed.reason}</p> : null}
      {parsed.selectedBy ? (
        <p className="mt-1 text-[11px] text-stone-500">Selected by {displayPartyName(parsed.selectedBy)}</p>
      ) : null}
      {item.input_tags?.length ? (
        <p className="mt-2 flex flex-wrap gap-1 text-[10px] text-stone-500">
          in
          {item.input_tags.map((tag) => (
            <button
              key={`${tag.comm_id}-${tag.label}`}
              type="button"
              className="rounded-full border border-indigo-200 bg-white px-2 py-0.5 font-mono text-indigo-700"
              data-testid={`${testIdPrefix}-tag-${tag.comm_id}-${tag.label}`}
              onClick={() => onOpenTag(tag.project_id || scopeId, tag.comm_id)}
            >
              {tag.label}
            </button>
          ))}
        </p>
      ) : null}
      {item.output_tags?.length ? (
        <p className="mt-1 flex flex-wrap gap-1 text-[10px] text-stone-500">
          out
          {item.output_tags.map((tag) => (
            <button
              key={`${tag.comm_id}-${tag.label}-out`}
              type="button"
              className="rounded-full border border-indigo-200 bg-white px-2 py-0.5 font-mono text-indigo-700"
              onClick={() => onOpenTag(tag.project_id || scopeId, tag.comm_id)}
            >
              {tag.label}
            </button>
          ))}
        </p>
      ) : null}
    </article>
  );
}
