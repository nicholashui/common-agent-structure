import { useEffect, useMemo, useState } from "react";
import { Check } from "lucide-react";
import { useNavigate, useParams, useSearchParams } from "react-router-dom";
import { ErrorBanner } from "../components/RecoveryBanner";
import {
  CasopsHttpError,
  type ProjectCommItem,
  type ProjectDecision,
  type ProjectGeneratorTag,
  type ProjectMedia,
  type ProjectOutputPayload,
  type ProjectRecord,
  type ProjectVideoConfig,
} from "../api/types";
import { DryRunControl } from "../components/ActorStrip";
import { GhostButton } from "../components/ui";
import { OptionTags } from "../components/OptionTags";
import { choiceIdFromAsk, parseOptionBlock } from "../lib/chatOptions";
import {
  HUMAN_DOMAIN_ROLES,
  commIdForAgent,
  commSeq,
  cyclePersistError,
  humanReplyAgent,
  pairHumanAsks,
  displayPartyName,
  hopExtra,
  hopKindLabel,
  mediaHref,
  shownOptionId,
  sourceCommId,
  instructionHopForPanel,
  splitProjectChat,
} from "../lib/projectChat";
import { rememberProject } from "../lib/projectContext";
import { useSession } from "../state/session";

function kindTone(kind: string, from: string): string {
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

function ChatMedia({ media, projectId }: { media: ProjectMedia; projectId: string }) {
  const src = mediaHref(media.url, projectId);
  const poster = media.poster ? mediaHref(media.poster, projectId) : undefined;
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

function CommArticle({
  item,
  hops,
  focusComm,
  focusOpt,
  listedDecisions,
  projectId,
  onPickOption,
  onOpenTag,
}: {
  item: ProjectCommItem;
  hops: ProjectCommItem[];
  focusComm: string;
  focusOpt: string;
  listedDecisions: ProjectDecision[];
  projectId: string;
  onPickOption: (agentId: string, optionId: string, commId?: string) => void;
  onOpenTag: (projectId: string, commId: string) => void;
}) {
  const parsed = parseOptionBlock(item.text);
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
  const followParsed = followChoice ? parseOptionBlock(followChoice.text) : null;
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
      data-testid={`project-chat-${item.id}`}
      className={[
        "rounded-2xl border px-4 py-3",
        kindTone(item.kind, item.from),
        focusComm === item.id ? "ring-2 ring-amber-400" : "",
      ].join(" ")}
    >
      <p className="text-[11px] text-stone-600" data-testid={`project-chat-header-${item.id}`}>
        {sourceId ? (
          <button
            type="button"
            className="font-semibold text-indigo-700 underline decoration-indigo-300 underline-offset-2 hover:text-indigo-900"
            data-testid={`project-chat-output-agent-${item.id}`}
            onClick={() => onOpenTag(projectId, sourceId)}
          >
            {fromName}
          </button>
        ) : (
          <span className="font-semibold text-stone-800" data-testid={`project-chat-output-agent-${item.id}`}>
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
      {item.media ? <ChatMedia media={item.media} projectId={projectId} /> : null}
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
              data-testid={`project-chat-tag-${tag.comm_id}-${tag.label}`}
              onClick={() => onOpenTag(tag.project_id, tag.comm_id)}
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
              onClick={() => onOpenTag(tag.project_id, tag.comm_id)}
            >
              {tag.label}
            </button>
          ))}
        </p>
      ) : null}
    </article>
  );
}

export function ProjectChatPage() {
  const session = useSession();
  const navigate = useNavigate();
  const params = useParams();
  const [search] = useSearchParams();
  const projectId = params.projectId ? decodeURIComponent(params.projectId) : "";
  const focusCommParam = search.get("comm") || "";
  const focusAgent = search.get("agent") || "";
  const [record, setRecord] = useState<ProjectRecord | null>(null);
  const [items, setItems] = useState<ProjectCommItem[]>([]);
  const [decisions, setDecisions] = useState<ProjectDecision[]>([]);
  const [autopilotMeta, setAutopilotMeta] = useState<{ cycle?: string; cycles?: number; status?: string }>({});
  const [output, setOutput] = useState<ProjectOutputPayload | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const [answer, setAnswer] = useState("");
  const [sending, setSending] = useState(false);
  const [generating, setGenerating] = useState(false);
  const [generatingEngine, setGeneratingEngine] = useState("");
  const [videoConfig, setVideoConfig] = useState<ProjectVideoConfig>({
    mode: "i2v",
    aspect_ratio: "9:16",
    duration: 15,
    resolution: "1080p",
  });

  useEffect(() => {
    if (!projectId) {
      return;
    }
    rememberProject(projectId);
    session.client
      .getProject(projectId)
      .then(setRecord)
      .catch((err) => setError(err instanceof Error ? err : new Error(String(err))));
    session.client
      .listProjectComms(projectId)
      .then((payload) => {
        setItems(payload.items ?? []);
        setDecisions(payload.decisions ?? []);
        setAutopilotMeta(payload.autopilot ?? {});
      })
      .catch((err) => setError(err instanceof Error ? err : new Error(String(err))));
    session.client
      .getProjectOutput(projectId)
      .then((payload) => {
        setOutput(payload);
        if (payload.video_config) {
          setVideoConfig((current) => ({ ...current, ...payload.video_config }));
        }
      })
      .catch(() => undefined);
  }, [projectId, session.client]);

  const { conversation, clips } = useMemo(() => splitProjectChat(items), [items]);
  const focusComm =
    focusCommParam || (focusAgent ? commIdForAgent(items, focusAgent) : "");
  const charHops = items.filter((item) => !item.live).length;
  const liveHops = items.filter((item) => item.live).length;

  useEffect(() => {
    if (!focusComm) {
      return;
    }
    const node = document.querySelector(`[data-comm-id="${CSS.escape(focusComm)}"]`);
    if (node instanceof HTMLElement) {
      node.scrollIntoView({ block: "center", behavior: "smooth" });
    }
  }, [focusComm, items]);
  const instructionHop = useMemo(() => instructionHopForPanel(items), [items]);
  const outputText = output?.text || instructionHop?.text || "";
  const outputPath = output?.path || `project/${projectId}/output/${projectId}-prompt.txt`;
  const generators: ProjectGeneratorTag[] = output?.generators?.length
    ? output.generators
    : [
        { id: "grok-imagine", label: "Grok Imagine", engine: "grok-imagine", live: true },
        { id: "grok-image", label: "Grok Image", engine: "grok-image", live: true },
        { id: "kling", label: "Kling 3.0", engine: "kling", live: false },
        { id: "veo", label: "Veo 3.1", engine: "veo", live: false },
        { id: "seedance", label: "Seedance 2.0", engine: "seedance", live: false },
        { id: "sora", label: "Sora 2", engine: "sora", live: false },
        { id: "runway", label: "Runway Gen-4", engine: "runway", live: false },
        { id: "luma", label: "Luma Ray 3", engine: "luma", live: false },
        { id: "pika", label: "Pika 2.2", engine: "pika", live: false },
        { id: "hailuo", label: "Hailuo 02", engine: "hailuo", live: false },
        { id: "wan", label: "Wan 2.2", engine: "wan", live: false },
      ];

  async function onGenerate(engine: string) {
    if (!projectId || generating) {
      return;
    }
    setGenerating(true);
    setGeneratingEngine(engine);
    setError(null);
    try {
      const result = await session.client.generateProject(projectId, { engine, config: videoConfig });
      if (result.error === "dry_run") {
        setError(new Error(result.note || "Dry-run is on. Uncheck Dry-run to submit to Grok Imagine."));
      }
      if (result.comms?.items) {
        setItems(result.comms.items);
      }
      const next = await session.client.getProjectOutput(projectId);
      setOutput(next);
      const last = (result.comms?.items ?? []).at(-1);
      if (last?.id) {
        navigate(`/projects/${encodeURIComponent(projectId)}/chat?comm=${encodeURIComponent(last.id)}`, { replace: true });
      }
    } catch (err) {
      setError(err instanceof CasopsHttpError || err instanceof Error ? err : new Error(String(err)));
    } finally {
      setGenerating(false);
      setGeneratingEngine("");
    }
  }
  const askPairs = useMemo(() => pairHumanAsks(conversation), [conversation]);
  const unanswered = askPairs.filter((row) => !row.answer);
  const humanLocks = HUMAN_DOMAIN_ROLES.filter((role) =>
    conversation.some((item) => item.kind === "choice" && item.from === "human_operator" && item.to === role),
  );
  const autoPilotAligned = humanLocks.length === HUMAN_DOMAIN_ROLES.length;
  const cycleState = String(autopilotMeta.cycle || "");
  const showCycleGate =
    clips.length > 0 && autoPilotAligned && unanswered.length === 0 && !["open", "stopped", "ready"].includes(cycleState);
  const focusOpt = search.get("opt") || "";
  const listedDecisions = useMemo(() => {
    if (decisions.length) {
      return decisions;
    }
    const nodes = (record?.graph?.nodes ?? []) as { data?: Record<string, unknown> }[];
    return nodes
      .filter((node) => Array.isArray(node.data?.options) && (node.data?.options as unknown[]).length)
      .map((node) => ({
        id: String(node.data?.agent_id || ""),
        agent_id: String(node.data?.agent_id || ""),
        point: String(node.data?.reason || node.data?.agent_id || ""),
        thinking: String(node.data?.thinking || ""),
        options: (node.data?.options as ProjectDecision["options"]) || [],
        recommend: String(node.data?.recommend || ""),
        chosen: String(node.data?.chosen || ""),
        decide_by: String(node.data?.decide_by || ""),
        selected_by: String(node.data?.selected_by || ""),
        select_reason: String(node.data?.select_reason || ""),
      }));
  }, [decisions, record]);

  async function onPickOption(agentId: string, optionId: string, commId?: string) {
    if (!projectId || !agentId || !optionId) {
      return;
    }
    setError(null);
    try {
      const result = await session.client.runProject(projectId, {
        instruction: record?.brief || "",
        choices: { [agentId]: optionId },
      });
      if (result.comms?.items) {
        setItems(result.comms.items);
      }
      if (result.comms?.decisions) {
        setDecisions(result.comms.decisions);
      }
      if (result.comms?.autopilot) {
        setAutopilotMeta(result.comms.autopilot);
      }
      if (result.graph) {
        setRecord((current) => (current ? { ...current, graph: result.graph } : current));
      }
      const next = await session.client.getProjectOutput(projectId);
      setOutput(next);
    } catch {
      /* walkthrough still highlights locally via ?opt= */
    }
    navigate(
      `/projects/${encodeURIComponent(projectId)}/chat?comm=${encodeURIComponent(commId || "")}&opt=${encodeURIComponent(optionId)}`,
      { replace: true },
    );
  }

  async function onCycle(gate: "stop" | "continue") {
    if (!projectId) {
      return;
    }
    setError(null);
    try {
      const result = await session.client.runProject(projectId, {
        instruction: record?.brief || "",
        cycle: gate,
      });
      const persist = cyclePersistError(Boolean(result.dry_run) || session.dryRun);
      if (persist) {
        setError(new Error(persist));
        return;
      }
      if (result.comms?.items) {
        setItems(result.comms.items);
      }
      if (result.comms?.autopilot) {
        setAutopilotMeta(result.comms.autopilot);
      }
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  async function onAnswer() {
    if (!projectId || !answer.trim()) {
      return;
    }
    const ask = unanswered[0]?.ask;
    const target = humanReplyAgent(ask?.from || "");
    if (!target) {
      return;
    }
    const optionId = choiceIdFromAsk(ask?.text || "", answer);
    setSending(true);
    setError(null);
    try {
      await onPickOption(target, optionId, ask?.id);
      setAnswer("");
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setSending(false);
    }
  }

  return (
    <div data-testid="project-chat">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <div>
          <h2 className="text-lg font-semibold text-stone-800">{record?.title ?? projectId}</h2>
          <p className="text-xs text-stone-500">
            Auto Pilot · draft only, then intent-analysis-agent → creative-agent → domain locks · Chat
          </p>
          <p className="text-xs text-stone-500" data-testid="project-chat-honesty">
            {charHops} hop{charHops === 1 ? "" : "s"} CHARACTERIZATION (not live Grok). {liveHops} live
            {liveHops ? " (generate / Imagine)" : ""}.
          </p>
        </div>
        <div className="flex gap-2">
          <DryRunControl />
          <GhostButton type="button" onClick={() => navigate(`/projects/${encodeURIComponent(projectId)}/workflow`)}>
            Workflow
          </GhostButton>
        </div>
      </div>
      <ErrorBanner error={error} />
      {conversation.length === 0 && clips.length === 0 && !outputText ? (
        <p className="rounded-2xl border border-stone-200 bg-white p-5 text-sm text-stone-500">
          No communications yet. Open Workflow, enter the first human instruction on Create Project, then Launch
          workflow.
        </p>
      ) : conversation.length ? (
        <ol className="mx-auto max-w-3xl space-y-3" data-testid="project-chat-log">
          {conversation.map((item) => (
            <li key={item.id}>
              <CommArticle
                item={item}
                hops={items}
                focusComm={focusComm}
                focusOpt={focusOpt}
                listedDecisions={listedDecisions}
                projectId={projectId}
                onPickOption={(agentId, optionId, commId) => void onPickOption(agentId, optionId, commId)}
                onOpenTag={(tagProjectId, commId) =>
                  navigate(
                    `/projects/${encodeURIComponent(tagProjectId)}/chat?comm=${encodeURIComponent(commId)}`,
                  )
                }
              />
            </li>
          ))}
        </ol>
      ) : null}
      {conversation.length ? (
        <p
          className="mx-auto mt-3 max-w-3xl rounded-xl border border-stone-200 bg-white px-3 py-2 text-[11px] text-stone-600 dark:border-stone-700 dark:bg-stone-900"
          data-testid="project-autopilot-status"
        >
          Auto Pilot · {humanLocks.length}/{HUMAN_DOMAIN_ROLES.length} human locks
          {autoPilotAligned ? " · aligned" : " · waiting on option picks"}
          {" · "}
          {HUMAN_DOMAIN_ROLES.map((role) => `Human → ${role}`).join(" · ")}
        </p>
      ) : null}
      {unanswered.length ? (
        <section className="mx-auto mt-4 max-w-3xl rounded-2xl border border-rose-200 bg-rose-50 p-4 dark:border-rose-800 dark:bg-rose-950" data-testid="project-human-asks">
          <h3 className="text-sm font-semibold text-rose-900">Open ASK_HUMAN — select an option</h3>
          <p className="mt-1 text-[11px] text-stone-600">
            Auto Pilot: do not draft domain prompts. Pick a pre-vetted option for each lock.
          </p>
          <ul className="mt-2 space-y-3">
            {unanswered.map((row) => {
              const parsedAsk = parseOptionBlock(row.ask.text);
              return (
                <li key={row.ask.id} className="rounded-xl border border-rose-200 bg-white p-3 dark:border-rose-800 dark:bg-rose-950">
                  <p className="text-[11px] font-semibold text-stone-800">
                    Human → {displayPartyName(row.ask.from)} | {row.ask.text.split("\n")[0]}
                  </p>
                  {parsedAsk.options.length ? (
                    <OptionTags
                      options={parsedAsk.options}
                      selected={parsedAsk.selected}
                      recommend={parsedAsk.recommend}
                      commId={row.ask.id}
                      owner={row.ask.from}
                      onPick={(optionId) => void onPickOption(row.ask.from, optionId, row.ask.id)}
                    />
                  ) : (
                    <p className="mt-1 text-sm text-stone-700">{row.ask.text}</p>
                  )}
                </li>
              );
            })}
          </ul>
          {unanswered.some((row) => !parseOptionBlock(row.ask.text).options.length) ? (
            <>
              <textarea
                className="mt-3 w-full rounded-xl border border-rose-200 bg-white p-2 text-sm"
                data-testid="project-human-answer"
                rows={3}
                value={answer}
                onChange={(event) => setAnswer(event.target.value)}
                placeholder="Only if an ASK has no options — otherwise pick a tag above"
              />
              <button
                type="button"
                className="mt-2 rounded-full bg-rose-800 px-3 py-1 text-xs font-semibold text-white disabled:opacity-50"
                data-testid="project-human-answer-send"
                disabled={sending || !answer.trim()}
                onClick={() => void onAnswer()}
              >
                {sending ? "Sending…" : "Answer and continue"}
              </button>
            </>
          ) : null}
        </section>
      ) : null}
      {outputText ? (
        <section className="mx-auto mt-6 max-w-3xl rounded-2xl border border-amber-200 bg-amber-50 p-4 dark:border-amber-800 dark:bg-amber-950" data-testid="project-chat-output">
          <h3 className="text-sm font-semibold text-stone-900">Generated video-generator instruction</h3>
          <p className="mt-1 text-[11px] text-stone-600" data-testid="project-chat-output-header">
            <span className="font-semibold text-stone-800">{displayPartyName(instructionHop?.from || "video.promptengineer")}</span>
            <span className="text-stone-400"> → </span>
            <span className="font-semibold text-stone-800">{displayPartyName(instructionHop?.to || "output-prompt")}</span>
            <span className="text-stone-400"> | {instructionHop ? hopExtra(instructionHop) : hopKindLabel("output")}</span>
          </p>
          <p className="mt-1 font-mono text-[11px] text-stone-500">{outputPath}</p>
          <p className="mt-1 text-[11px] text-stone-500">
            Host-assembled after the hops above. sample/ is never written. Click a generator tag to submit.
            Generated clips appear below this box. Grok Imagine: still (Image 2.0) then I2V (Video 1.5). Uncheck Dry-run first.
          </p>
          <div className="mt-3 flex flex-wrap gap-2" data-testid="project-generator-tags">
            {generators.map((tag) => (
              <button
                key={tag.id}
                type="button"
                disabled={generating}
                data-testid={`project-generator-${tag.id}`}
                className={[
                  "flex max-w-full items-start gap-1.5 rounded-xl border px-2.5 py-1.5 text-left text-[11px]",
                  tag.live
                    ? "border-amber-400 bg-white text-amber-900 hover:bg-amber-100 dark:bg-amber-950 dark:text-amber-100"
                    : "border-stone-300 bg-stone-100 text-stone-500 dark:border-stone-600 dark:bg-stone-800",
                  generatingEngine === tag.id ? "ring-2 ring-amber-500" : "",
                ].join(" ")}
                onClick={() => void onGenerate(tag.id)}
              >
                {generatingEngine === tag.id ? (
                  <Check size={12} className="mt-0.5 shrink-0" aria-hidden="true" />
                ) : (
                  <span className="mt-0.5 inline-block h-3 w-3 shrink-0" aria-hidden="true" />
                )}
                <span>
                  <span className="font-mono">
                    {generatingEngine === tag.id ? "Submitting…" : tag.label}
                    {tag.live ? "" : " · declared"}
                  </span>
                  {tag.why ? <span className="mt-0.5 block text-[10px] leading-snug text-stone-500">{tag.why}</span> : null}
                </span>
              </button>
            ))}
          </div>
          <div className="mt-3 grid gap-2 sm:grid-cols-4" data-testid="project-video-config">
            <label className="text-[10px] font-semibold uppercase tracking-wide text-stone-500">
              Aspect
              <select
                className="mt-1 w-full rounded-lg border border-stone-200 bg-white px-2 py-1 text-xs"
                value={videoConfig.aspect_ratio || "9:16"}
                onChange={(event) => setVideoConfig((current) => ({ ...current, aspect_ratio: event.target.value }))}
              >
                <option value="9:16">9:16</option>
                <option value="16:9">16:9</option>
                <option value="1:1">1:1</option>
              </select>
            </label>
            <label className="text-[10px] font-semibold uppercase tracking-wide text-stone-500">
              Duration
              <select
                className="mt-1 w-full rounded-lg border border-stone-200 bg-white px-2 py-1 text-xs"
                value={String(videoConfig.duration || 15)}
                onChange={(event) =>
                  setVideoConfig((current) => ({ ...current, duration: Number(event.target.value) }))
                }
              >
                <option value="6">6s</option>
                <option value="8">8s</option>
                <option value="10">10s</option>
                <option value="15">15s</option>
              </select>
            </label>
            <label className="text-[10px] font-semibold uppercase tracking-wide text-stone-500">
              Resolution
              <select
                className="mt-1 w-full rounded-lg border border-stone-200 bg-white px-2 py-1 text-xs"
                value={videoConfig.resolution || "1080p"}
                onChange={(event) => setVideoConfig((current) => ({ ...current, resolution: event.target.value }))}
              >
                <option value="480p">480p</option>
                <option value="720p">720p</option>
                <option value="1080p">1080p</option>
              </select>
            </label>
            <label className="text-[10px] font-semibold uppercase tracking-wide text-stone-500">
              Mode
              <select
                className="mt-1 w-full rounded-lg border border-stone-200 bg-white px-2 py-1 text-xs"
                value={videoConfig.mode || "i2v"}
                onChange={(event) => setVideoConfig((current) => ({ ...current, mode: event.target.value }))}
              >
                <option value="i2v">Image then I2V</option>
                <option value="t2v">Text-to-video</option>
              </select>
            </label>
          </div>
          <pre className="mt-3 max-h-[40rem] overflow-auto whitespace-pre-wrap rounded-xl bg-white p-3 text-xs text-stone-800">
            {outputText}
          </pre>
        </section>
      ) : null}
      {clips.length ? (
        <ol className="mx-auto mt-4 max-w-3xl space-y-3" data-testid="project-chat-clips">
          {clips.map((item) => (
            <li key={item.id}>
              <CommArticle
                item={item}
                hops={items}
                focusComm={focusComm}
                focusOpt={focusOpt}
                listedDecisions={listedDecisions}
                projectId={projectId}
                onPickOption={(agentId, optionId, commId) => void onPickOption(agentId, optionId, commId)}
                onOpenTag={(tagProjectId, commId) =>
                  navigate(
                    `/projects/${encodeURIComponent(tagProjectId)}/chat?comm=${encodeURIComponent(commId)}`,
                  )
                }
              />
            </li>
          ))}
        </ol>
      ) : null}
      {showCycleGate ? (
        <section
          className="mx-auto mt-4 max-w-3xl rounded-2xl border border-indigo-200 bg-indigo-50 p-4 dark:border-indigo-800 dark:bg-indigo-950"
          data-testid="project-cycle-gate"
        >
          <h3 className="text-sm font-semibold text-indigo-950 dark:text-indigo-100">After this clip</h3>
          <p className="mt-1 text-[11px] text-stone-600">
            Host-owned Auto Pilot cycle. Folder max_refinement_count stays 0. Imagine is not called automatically.
          </p>
          <div className="mt-3 flex flex-wrap gap-2">
            <button
              type="button"
              className="rounded-full bg-indigo-700 px-3 py-1 text-xs font-semibold text-white"
              data-testid="project-cycle-stop"
              onClick={() => void onCycle("stop")}
            >
              stop
            </button>
            <button
              type="button"
              className="rounded-full border border-indigo-400 bg-white px-3 py-1 text-xs font-semibold text-indigo-800"
              data-testid="project-cycle-continue"
              onClick={() => void onCycle("continue")}
            >
              another Auto Pilot cycle
            </button>
          </div>
        </section>
      ) : null}
      {cycleState === "ready" ? (
        <p className="mx-auto mt-3 max-w-3xl text-[11px] text-amber-800" data-testid="project-cycle-ready">
          pass_03 instruction updated. Click Grok Imagine to generate again.
        </p>
      ) : null}
    </div>
  );
}
