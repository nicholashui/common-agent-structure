import { FormEvent, useEffect, useRef, useState, type PointerEvent as ReactPointerEvent, type ReactNode } from "react";
import { ArrowUp, ChevronRight, Copy, Download, Plus, RefreshCw, Square } from "lucide-react";
import { useSearchParams } from "react-router-dom";
import { AdapterStatus } from "../components/AdapterStatus";
import { ChatMarkdown } from "../components/ChatMarkdown";
import { ConfirmDialog } from "../components/ConfirmDialog";
import { CharacterizationBadge, ChatFixtureList } from "../components/EvalFixtures";
import { ErrorBanner } from "../components/RecoveryBanner";
import { ChatProofPanel } from "../components/ChatProof";
import { IoPanel } from "../components/IoPanel";
import { GhostButton } from "../components/ui";
import { RequestAbortedError, type ChatContextPack, type ChatProof, type EvalFixture, type RuntimeAdapter } from "../api/types";
import {
  canRegenerate,
  clearThread,
  copyText,
  downloadText,
  exportThreadJson,
  exportThreadMarkdown,
  lastUserIndex,
  loadThread,
  chatHitOutputCap,
  buildChatBody,
  makeChatSessionId,
  replaceThread,
  saveThread,
  sessionFromFileName,
  loadChatSideWidth,
  saveChatSideWidth,
  clampChatSideWidth,
  CHAT_SIDE_WIDTH_MIN,
  CHAT_SIDE_WIDTH_MAX,
  CHAT_SIDE_WIDTH_STEP,
  type ChatFile,
  type ChatTurn,
} from "../lib/chat";
import { enqueueChatPersist, flushChatNow, loadChatTranscript, refreshChatFiles, subscribeChatFiles } from "../lib/chatPersist";
import { isPinnedToBottom } from "../lib/chatScroll";
import { chatFixtures, findFixture, fixtureHistory, fixtureMessage } from "../lib/fixtures";
import { followUpChips } from "../lib/followUps";
import { useAgentId, useAsync } from "../lib/hooks";
import { parseAgentIo } from "../lib/io";
import { clipLogText, logUi } from "../log/bus";
import { formatHktClock, formatHktDateTime, formatHktIso, nowHktIso } from "../lib/time";
import { displayRelativePath } from "../lib/paths";
import { useSession } from "../state/session";

function fileLabel(path: string): string {
  const rel = displayRelativePath(path);
  const parts = rel.split("/").filter(Boolean);
  return parts.slice(-2).join("/") || rel;
}

function ContextPack({ pack }: { pack: ChatContextPack }) {
  const segments = pack.segments ?? [];
  const skills = pack.skills ?? [];
  return (
    <section className="rounded-2xl border border-stone-200 bg-white p-5" data-testid="chat-context">
      <h2 className="mb-1 text-sm font-semibold text-stone-900">Context pack</h2>
      <p className="mb-3 text-xs text-stone-500">
        Adapter {pack.adapter ?? "host_llm"}. Host packed this turn from folder segments. Compaction{" "}
        {pack.compaction ?? "disabled"}. Not an eval pass. Memory, plugins, and T3 stay off.
      </p>
      <ul className="space-y-1 font-mono text-[11px] text-stone-700">
        {segments.map((row) => (
          <li key={row.name}>
            {row.name} {row.tokens}/{row.budget}
            {row.included ? "" : " omitted"}
            {row.clipped ? " clipped" : ""}
          </li>
        ))}
      </ul>
      <p className="mt-3 text-[11px] text-stone-500">
        prompt {pack.prompt_reference ?? "—"} · system {pack.system_tokens ?? 0} tok · history {pack.history_turns ?? 0}
        {pack.history_clipped ? " clipped" : ""}
        {pack.session_id ? ` · session ${pack.session_id}` : ""}
      </p>
      <p className="mt-1 text-[11px] text-stone-500">
        skills {skills.length ? skills.map((item) => item.skill_id).join(", ") : "(none enabled)"}
      </p>
      {pack.omitted?.length ? (
        <p className="mt-1 break-all text-[11px] text-stone-400">omitted {pack.omitted.join(", ")}</p>
      ) : null}
    </section>
  );
}

function turnTime(ts?: string): string {
  return formatHktClock(ts);
}

function IconBtn({
  label,
  testId,
  onClick,
  disabled,
  children,
}: {
  label: string;
  testId?: string;
  onClick?: () => void;
  disabled?: boolean;
  children: ReactNode;
}) {
  return (
    <button
      type="button"
      title={label}
      aria-label={label}
      data-testid={testId}
      disabled={disabled}
      onClick={onClick}
      className="inline-flex h-8 w-8 items-center justify-center rounded-full text-stone-500 hover:bg-stone-100 hover:text-stone-800 disabled:cursor-not-allowed disabled:opacity-40 dark:hover:bg-stone-800 dark:hover:text-stone-100"
    >
      {children}
    </button>
  );
}

function resizeComposer(el: HTMLTextAreaElement | null) {
  if (!el) {
    return;
  }
  el.style.height = "auto";
  el.style.height = `${Math.min(Math.max(el.scrollHeight, 28), 160)}px`;
}

function AccordionItem({
  title,
  subtitle,
  open,
  onToggle,
  testId,
  children,
}: {
  title: string;
  subtitle?: string;
  open: boolean;
  onToggle: () => void;
  testId?: string;
  children: ReactNode;
}) {
  return (
    <div
      className="rounded-xl border border-stone-200 bg-white dark:border-stone-700 dark:bg-stone-900"
      data-testid={testId}
    >
      <button
        type="button"
        aria-expanded={open}
        onClick={onToggle}
        className="flex w-full items-start gap-2 px-3 py-2 text-left text-sm text-stone-800 hover:bg-stone-50 dark:text-stone-100 dark:hover:bg-stone-800"
      >
        <ChevronRight
          className={`mt-0.5 h-4 w-4 shrink-0 text-stone-400 transition-transform ${open ? "rotate-90" : ""}`}
        />
        <span className="min-w-0 flex-1">
          <span className="block truncate font-medium">{title}</span>
          {subtitle ? <span className="mt-0.5 block truncate font-mono text-[10px] text-stone-400">{subtitle}</span> : null}
        </span>
      </button>
      {open ? <div className="border-t border-stone-100 px-3 py-3 dark:border-stone-800">{children}</div> : null}
    </div>
  );
}

export function ChatPage() {
  const agentId = useAgentId();
  const session = useSession();
  const [searchParams, setSearchParams] = useSearchParams();
  const panel = useAsync(async () => {
    const [structure, llm, adapter] = await Promise.all([
      session.client.getStructure(agentId),
      session.client.getAgentLlm(agentId),
      session.client.getRuntimeAdapter(agentId),
    ]);
    return { structure, llm, adapter };
  }, [session.client, agentId]);
  const fixtures = useAsync(() => session.client.getEvalFixtures(agentId), [session.client, agentId]);
  const [turns, setTurns] = useState<ChatTurn[]>(() => loadThread(agentId).turns);
  const [files, setFiles] = useState<ChatFile[]>(() => loadThread(agentId).files);
  const [draft, setDraft] = useState("");
  const [error, setError] = useState<Error | null>(null);
  const [pending, setPending] = useState(false);
  const [stopped, setStopped] = useState(false);
  const [pinned, setPinned] = useState(true);
  const [copiedKey, setCopiedKey] = useState<string>("");
  const [loadTarget, setLoadTarget] = useState<ChatFile | null>(null);
  const [contextPack, setContextPack] = useState<ChatContextPack | null>(null);
  const [chatProof, setChatProof] = useState<ChatProof | null>(null);
  const [adapterLive, setAdapterLive] = useState<RuntimeAdapter | null>(null);
  const logRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLTextAreaElement>(null);
  const abortRef = useRef<AbortController | null>(null);
  const sideDrag = useRef<{ startX: number; startWidth: number } | null>(null);
  const [sideWidth, setSideWidth] = useState(loadChatSideWidth);
  const [sideDragging, setSideDragging] = useState(false);
  const [openItems, setOpenItems] = useState<Record<string, boolean>>({});
  const sideWidthRef = useRef(sideWidth);
  sideWidthRef.current = sideWidth;
  const io = parseAgentIo(panel.data?.structure.io);
  const adapter = adapterLive ?? panel.data?.adapter ?? null;
  const adapterKind = adapter?.kind ?? "host_llm";
  const chatReady = session.healthOk && !session.stale && !session.containment;
  const cases = chatFixtures(fixtures.data);
  const fixtureId = searchParams.get("fixture") || "";
  const lastAssistant = [...turns].reverse().find((turn) => turn.role === "assistant");
  const chips = !pending && lastAssistant ? followUpChips(lastAssistant.content) : [];

  useEffect(() => {
    const thread = loadThread(agentId);
    setTurns(thread.turns);
    setFiles(thread.files);
    setDraft("");
    setError(null);
    setStopped(false);
    setContextPack(null);
    setAdapterLive(null);
    setPinned(true);
    setOpenItems({});
    abortRef.current?.abort();
    abortRef.current = null;
    void refreshChatFiles(agentId)
      .then(setFiles)
      .catch(() => undefined);
  }, [agentId]);

  useEffect(() => {
    return subscribeChatFiles((id, next) => {
      if (id === agentId) {
        setFiles(next);
      }
    });
  }, [agentId]);

  useEffect(() => {
    const el = logRef.current;
    if (pinned && el) {
      el.scrollTo({ top: el.scrollHeight });
    }
  }, [turns, pending, pinned, stopped]);

  useEffect(() => {
    if (panel.data?.adapter) {
      setAdapterLive(panel.data.adapter);
    }
  }, [panel.data?.adapter]);

  useEffect(() => {
    if (!pending) {
      return;
    }
    const tick = () => {
      void session.client.getRuntimeAdapter(agentId).then(setAdapterLive).catch(() => undefined);
    };
    tick();
    const timer = window.setInterval(tick, 1500);
    return () => window.clearInterval(timer);
  }, [pending, agentId, session.client]);

  useEffect(() => {
    function onKey(event: KeyboardEvent) {
      if (event.key === "Escape") {
        abortRef.current?.abort();
      }
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  useEffect(() => {
    resizeComposer(inputRef.current);
  }, [draft]);

  useEffect(() => {
    function onMove(event: PointerEvent) {
      const session = sideDrag.current;
      if (!session) {
        return;
      }
      setSideWidth(clampChatSideWidth(session.startWidth + (event.clientX - session.startX)));
    }
    function onUp() {
      if (!sideDrag.current) {
        return;
      }
      sideDrag.current = null;
      setSideDragging(false);
      document.body.style.cursor = "";
      document.body.style.userSelect = "";
      saveChatSideWidth(sideWidthRef.current);
    }
    window.addEventListener("pointermove", onMove);
    window.addEventListener("pointerup", onUp);
    window.addEventListener("pointercancel", onUp);
    return () => {
      window.removeEventListener("pointermove", onMove);
      window.removeEventListener("pointerup", onUp);
      window.removeEventListener("pointercancel", onUp);
    };
  }, []);

  function beginSideDrag(event: ReactPointerEvent<HTMLDivElement>) {
    event.preventDefault();
    sideDrag.current = { startX: event.clientX, startWidth: sideWidth };
    setSideDragging(true);
    document.body.style.cursor = "col-resize";
    document.body.style.userSelect = "none";
  }

  function onSideKey(event: React.KeyboardEvent<HTMLDivElement>) {
    const step = event.shiftKey ? CHAT_SIDE_WIDTH_STEP * 4 : CHAT_SIDE_WIDTH_STEP;
    if (event.key === "ArrowLeft") {
      event.preventDefault();
      const next = clampChatSideWidth(sideWidth - step);
      setSideWidth(next);
      saveChatSideWidth(next);
    } else if (event.key === "ArrowRight") {
      event.preventDefault();
      const next = clampChatSideWidth(sideWidth + step);
      setSideWidth(next);
      saveChatSideWidth(next);
    } else if (event.key === "Home") {
      event.preventDefault();
      setSideWidth(CHAT_SIDE_WIDTH_MIN);
      saveChatSideWidth(CHAT_SIDE_WIDTH_MIN);
    } else if (event.key === "End") {
      event.preventDefault();
      setSideWidth(CHAT_SIDE_WIDTH_MAX);
      saveChatSideWidth(CHAT_SIDE_WIDTH_MAX);
    }
  }

  function toggleItem(id: string) {
    setOpenItems((current) => ({ ...current, [id]: !current[id] }));
  }

  useEffect(() => {
    if (!fixtureId || !fixtures.data) {
      return;
    }
    const item = findFixture(fixtures.data, fixtureId);
    if (item) {
      applyFixture(item);
    }
    const next = new URLSearchParams(searchParams);
    if (next.has("fixture")) {
      next.delete("fixture");
      setSearchParams(next, { replace: true });
    }
  }, [agentId, fixtureId, fixtures.data, searchParams, setSearchParams]);

  function applyFixture(item: EvalFixture) {
    const message = fixtureMessage(item);
    if (!message) {
      return;
    }
    const prior = fixtureHistory(item).map((turn) => ({ ...turn, ts: nowHktIso() }));
    replaceThread(agentId, prior, makeChatSessionId());
    setTurns(prior);
    setDraft(message);
    inputRef.current?.focus();
  }

  function loadCase(item: EvalFixture) {
    applyFixture(item);
  }

  function markCopied(key: string) {
    setCopiedKey(key);
    window.setTimeout(() => setCopiedKey((current) => (current === key ? "" : current)), 1200);
  }

  async function completeAssistant(message: string, historyTurns: ChatTurn[], baseTurns: ChatTurn[]) {
    const controller = new AbortController();
    abortRef.current = controller;
    setPending(true);
    setStopped(false);
    setError(null);
    setPinned(true);
    session.setRunning(true);
    try {
      const result = await session.client.chatAgent(
        agentId,
        buildChatBody(message, historyTurns, loadThread(agentId).session),
        { signal: controller.signal },
      );
      const assistantTurn: ChatTurn = {
        role: "assistant",
        content: result.reply || "(empty reply)",
        provider: result.provider,
        truncated: chatHitOutputCap(result.llm),
        ts: nowHktIso(),
      };
      const withReply = [...baseTurns, assistantTurn];
      setTurns(withReply);
      saveThread(agentId, withReply);
      enqueueChatPersist(agentId, loadThread(agentId).session, assistantTurn);
      void flushChatNow();
      setContextPack(result.context ?? null);
      setChatProof(result.proof ?? null);
      if (result.context?.pid != null || result.context?.session_id) {
        setAdapterLive((current) => ({
          agent_id: agentId,
          kind: result.context?.adapter ?? current?.kind ?? "grok_acp",
          grok_available: current?.grok_available,
          profile_ready: current?.profile_ready,
          pid: result.context?.pid ?? current?.pid ?? null,
          session_id: result.context?.session_id ?? current?.session_id ?? null,
          healthy: true,
          home: current?.home,
        }));
      }
      void session.client.getRuntimeAdapter(agentId).then(setAdapterLive).catch(() => undefined);
      logUi(`chat reply ${agentId} ${result.provider ?? ""}`, clipLogText(result.reply));
    } catch (err) {
      if (err instanceof RequestAbortedError) {
        setStopped(true);
        logUi(`chat stopped ${agentId}`);
        return;
      }
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      abortRef.current = null;
      setPending(false);
      session.setRunning(false);
    }
  }

  async function sendMessage(message: string, historyTurns: ChatTurn[] = turns) {
    const trimmed = message.trim();
    if (!trimmed || pending) {
      return;
    }
    const chatSession = loadThread(agentId).session;
    const userTurn: ChatTurn = { role: "user", content: trimmed, ts: nowHktIso() };
    const nextTurns: ChatTurn[] = [...historyTurns, userTurn];
    setTurns(nextTurns);
    saveThread(agentId, nextTurns);
    setDraft("");
    enqueueChatPersist(agentId, chatSession, userTurn);
    void flushChatNow();
    logUi(`chat send ${agentId}`, clipLogText(trimmed));
    await completeAssistant(trimmed, historyTurns, nextTurns);
  }

  async function send(event?: FormEvent) {
    event?.preventDefault();
    await sendMessage(draft);
  }

  async function regenerate() {
    if (pending || !canRegenerate(turns)) {
      return;
    }
    const userIdx = lastUserIndex(turns);
    const user = turns[userIdx];
    const historyTurns = turns.slice(0, userIdx);
    const baseTurns = turns.slice(0, userIdx + 1);
    setTurns(baseTurns);
    saveThread(agentId, baseTurns);
    await completeAssistant(user.content, historyTurns, baseTurns);
  }

  async function applyLoad(file: ChatFile) {
    setLoadTarget(null);
    try {
      const loaded = await loadChatTranscript(agentId, file.name);
      const next = replaceThread(agentId, loaded, sessionFromFileName(file.name));
      setTurns(next.turns);
      setFiles(next.files);
      setPinned(true);
      setStopped(false);
      setError(null);
      logUi(`chat load ${agentId} ${file.name}`);
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    }
  }

  function exportMd() {
    downloadText(`${agentId}-chat.md`, exportThreadMarkdown(agentId, turns), "text/markdown;charset=utf-8");
  }

  function exportJson() {
    downloadText(
      `${agentId}-chat.json`,
      exportThreadJson(agentId, loadThread(agentId).session, turns),
      "application/json;charset=utf-8",
    );
  }

  const liveSession = loadThread(agentId).session;

  function startNewChat() {
    abortRef.current?.abort();
    const next = clearThread(agentId);
    setTurns(next.turns);
    setFiles(next.files);
    setStopped(false);
    setChatProof(null);
    setContextPack(null);
    setDraft("");
    inputRef.current?.focus();
  }

  return (
    <div data-testid="agent-chat" className="flex h-[calc(100dvh-12rem)] flex-col overflow-hidden">
      <div className="mb-3 flex shrink-0 flex-wrap items-center justify-between gap-2">
        <div>
          <h2 className="text-lg font-semibold text-stone-800">Chat</h2>
          <p className="text-xs text-stone-500" data-testid="agent-chat-not-autopilot">
            Single-agent packed Chat. Not the project Auto Pilot transcript.
          </p>
          <p className="text-xs text-stone-400">as_of {panel.asOf ? formatHktIso(panel.asOf) : "—"}</p>
        </div>
        <div className="flex flex-wrap gap-2">
          <GhostButton type="button" data-testid="chat-export-md" disabled={!turns.length} onClick={exportMd}>
            Export MD
          </GhostButton>
          <GhostButton type="button" data-testid="chat-export-json" disabled={!turns.length} onClick={exportJson}>
            Export JSON
          </GhostButton>
          <GhostButton type="button" onClick={startNewChat}>
            Clear
          </GhostButton>
        </div>
      </div>
      <p className="sr-only">
        Type a text message to talk to {agentId}. The host packs identity plus the operational prompt. It does not dump
        SKILL.md, memory, or tools. Adapter {adapterKind}. Export is a Chat transcript, not a sealed Run.
      </p>
      <ErrorBanner error={error ?? panel.error} />
      <div className="flex min-h-0 flex-1 flex-col overflow-hidden md:flex-row">
        <aside
          data-testid="chat-subarea"
          style={{ ["--chat-side-width" as string]: `${sideWidth}px` }}
          className={[
            "flex min-h-0 w-full shrink-0 flex-col overflow-hidden max-md:max-h-[38vh] md:w-[var(--chat-side-width)]",
            sideDragging ? "select-none" : "",
          ].join(" ")}
        >
          <p className="mb-2 shrink-0 text-[11px] font-medium uppercase tracking-wide text-stone-400">Chats</p>
          <div className="min-h-0 flex-1 space-y-2 overflow-y-auto pr-1" data-testid="chat-subarea-scroll">
            {files.length ? (
              <section data-testid="chat-files">
                <ul className="space-y-2">
                  {files.map((file) => {
                    const id = `file:${file.name}`;
                    const open = Boolean(openItems[id]);
                    const active = sessionFromFileName(file.name) === liveSession;
                    return (
                      <li key={file.path} data-testid="chat-file">
                        <AccordionItem
                          title={formatHktDateTime(file.ts)}
                          subtitle={fileLabel(file.path)}
                          open={open}
                          onToggle={() => toggleItem(id)}
                        >
                          <p className="break-all font-mono text-[11px] text-stone-500">{displayRelativePath(file.path)}</p>
                          {file.bytes != null ? (
                            <p className="mt-1 text-[11px] text-stone-400">{file.bytes} bytes</p>
                          ) : null}
                          {active ? <p className="mt-1 text-[11px] text-stone-500">Current thread</p> : null}
                          <GhostButton
                            type="button"
                            data-testid="chat-load-history"
                            className="mt-3"
                            onClick={() => {
                              if (turns.length) {
                                setLoadTarget(file);
                              } else {
                                void applyLoad(file);
                              }
                            }}
                          >
                            Load
                          </GhostButton>
                        </AccordionItem>
                      </li>
                    );
                  })}
                </ul>
              </section>
            ) : (
              <p className="text-xs text-stone-400" data-testid="chat-files-empty">
                Transcripts save under logs/chat/{agentId}/.
              </p>
            )}
            <AccordionItem
              title="Adapter"
              open={Boolean(openItems.adapter)}
              onToggle={() => toggleItem("adapter")}
            >
              <AdapterStatus adapter={adapter} testId="chat-adapter-detail" />
            </AccordionItem>
            <AccordionItem
              title="Inputs and outputs"
              open={Boolean(openItems.io)}
              onToggle={() => toggleItem("io")}
            >
              <IoPanel io={io} mode="chat" />
            </AccordionItem>
            {chatProof ? (
              <AccordionItem
                title="Chat proof"
                open={Boolean(openItems.proof)}
                onToggle={() => toggleItem("proof")}
              >
                <ChatProofPanel proof={chatProof} />
              </AccordionItem>
            ) : null}
            {contextPack ? (
              <AccordionItem
                title="Context pack"
                open={Boolean(openItems.context)}
                onToggle={() => toggleItem("context")}
              >
                <ContextPack pack={contextPack} />
              </AccordionItem>
            ) : null}
            {cases.length ? (
              <AccordionItem
                title="Characterization cases"
                subtitle={`${cases.length} cases`}
                open={Boolean(openItems.cases)}
                onToggle={() => toggleItem("cases")}
              >
                <div className="mb-2">
                  <CharacterizationBadge />
                </div>
                <ChatFixtureList items={cases} onLoad={loadCase} compact />
              </AccordionItem>
            ) : null}
          </div>
        </aside>
        <div
          role="separator"
          aria-orientation="vertical"
          aria-label="Resize chats panel"
          aria-valuemin={CHAT_SIDE_WIDTH_MIN}
          aria-valuemax={CHAT_SIDE_WIDTH_MAX}
          aria-valuenow={sideWidth}
          tabIndex={0}
          data-testid="chat-subarea-resize"
          className="relative hidden w-2 shrink-0 cursor-col-resize md:block after:absolute after:inset-y-3 after:left-1/2 after:w-px after:-translate-x-1/2 after:bg-stone-200 hover:after:bg-stone-400 dark:after:bg-stone-700"
          onPointerDown={beginSideDrag}
          onKeyDown={onSideKey}
        />
        <section className="relative flex min-h-0 min-w-0 flex-1 flex-col overflow-hidden">
          <div
            ref={logRef}
            className="flex-1 space-y-8 overflow-y-auto px-1 pb-4 pt-2 lg:px-8"
            data-testid="chat-log"
            aria-live="polite"
            onScroll={(event) => setPinned(isPinnedToBottom(event.currentTarget))}
          >
            {turns.length === 0 && !pending ? (
              <p className="pt-16 text-center text-sm text-stone-400">No messages yet. Type below to start.</p>
            ) : null}
            {turns.map((turn, index) => {
              const key = `${turn.role}-${index}`;
              const lastAssistantTurn = turn.role === "assistant" && index === turns.length - 1;
              if (turn.role === "user") {
                return (
                  <div key={key} className="flex justify-end">
                    <div
                      className="max-w-[min(36rem,90%)] whitespace-pre-wrap rounded-2xl bg-stone-100 px-4 py-2.5 text-sm text-stone-900 dark:bg-stone-800 dark:text-stone-50"
                      data-testid="chat-user"
                    >
                      {turn.content}
                      <div className="mt-1 flex items-center gap-2">
                        <p className="font-mono text-[10px] text-stone-400" data-testid="chat-turn-time">
                          {turnTime(turn.ts)}
                        </p>
                        <button
                          type="button"
                          className="text-[10px] text-stone-400 underline-offset-2 hover:underline"
                          data-testid="chat-copy"
                          onClick={() => {
                            void copyText(turn.content).then((ok) => {
                              if (ok) {
                                markCopied(key);
                              }
                            });
                          }}
                        >
                          {copiedKey === key ? "Copied" : "Copy"}
                        </button>
                      </div>
                    </div>
                  </div>
                );
              }
              return (
                <div key={key} className="mx-auto w-full max-w-[46rem]" data-testid="chat-assistant">
                  <ChatMarkdown text={turn.content} />
                  {turn.truncated ? (
                    <p className="mt-2 text-[11px] text-amber-800" data-testid="chat-output-cap">
                      Reply hit the output token cap.
                    </p>
                  ) : null}
                  <div className="mt-3 flex flex-wrap items-center gap-1 text-stone-400">
                    <p className="mr-2 font-mono text-[10px] text-stone-400" data-testid="chat-turn-time">
                      {turnTime(turn.ts)}
                      {turn.provider ? ` · ${turn.provider}` : ""}
                    </p>
                    <IconBtn
                      label={copiedKey === key ? "Copied" : "Copy"}
                      testId="chat-copy"
                      onClick={() => {
                        void copyText(turn.content).then((ok) => {
                          if (ok) {
                            markCopied(key);
                          }
                        });
                      }}
                    >
                      <Copy className="h-4 w-4" />
                    </IconBtn>
                    {lastAssistantTurn && !pending ? (
                      <IconBtn
                        label="Regenerate"
                        testId="chat-regenerate"
                        disabled={!chatReady || !canRegenerate(turns)}
                        onClick={() => void regenerate()}
                      >
                        <RefreshCw className="h-4 w-4" />
                      </IconBtn>
                    ) : null}
                    <IconBtn label="Export markdown" onClick={exportMd}>
                      <Download className="h-4 w-4" />
                    </IconBtn>
                  </div>
                </div>
              );
            })}
            {pending ? <p className="text-xs text-stone-400">Waiting for {adapterKind}…</p> : null}
            {stopped && !pending ? (
              <p className="text-xs text-amber-800" data-testid="chat-stopped">
                Generation stopped. The last user message is kept.
              </p>
            ) : null}
          </div>
          {!pinned ? (
            <button
              type="button"
              data-testid="chat-jump-latest"
              className="absolute bottom-36 right-6 rounded-full border border-stone-200 bg-white px-3 py-1 text-xs text-stone-700 shadow-sm dark:border-stone-700 dark:bg-stone-900 dark:text-stone-200"
              onClick={() => {
                setPinned(true);
                logRef.current?.scrollTo({ top: logRef.current.scrollHeight });
              }}
            >
              Jump to latest
            </button>
          ) : null}

          <div className="mx-auto w-full max-w-[46rem] px-1 pb-3 lg:px-0">
            {!pending && chips.length > 0 ? (
              <div className="mb-3 flex flex-wrap gap-2" data-testid="chat-follow-ups">
                {chips.map((chip) => (
                  <button
                    key={chip}
                    type="button"
                    data-testid="chat-follow-up"
                    className="rounded-full border border-stone-200 bg-white px-3 py-1.5 text-left text-xs text-stone-700 hover:border-stone-300 hover:bg-stone-50 dark:border-stone-700 dark:bg-stone-900 dark:text-stone-200"
                    disabled={!chatReady}
                    onClick={() => void sendMessage(chip)}
                  >
                    {chip}
                  </button>
                ))}
              </div>
            ) : null}
            <p className="sr-only" data-testid="chat-adapter">
              Adapter {adapterKind}
              {adapter?.profile_ready ? " · profile ready" : " · profile missing"}
              {adapter?.grok_available ? " · grok yes" : " · grok no"}
              {adapter?.pid != null ? ` · pid ${adapter.pid}` : ""}
              {adapter?.session_id ? ` · session ${adapter.session_id}` : ""}
              . Memory, plugins, T3 stay off.
            </p>
            <form
              className="rounded-[1.75rem] border border-stone-200 bg-white px-4 py-3 shadow-sm dark:border-stone-700 dark:bg-stone-900"
              onSubmit={(event) => void send(event)}
            >
              <label className="sr-only" htmlFor="agent-chat-input">
                Message
              </label>
              <textarea
                id="agent-chat-input"
                ref={inputRef}
                data-testid="chat-input"
                className="min-h-[1.75rem] w-full resize-none border-0 bg-transparent px-1 py-1 text-sm text-stone-900 outline-none placeholder:text-stone-400 dark:text-stone-50"
                rows={1}
                value={draft}
                placeholder="Ask anything"
                onChange={(event) => setDraft(event.target.value)}
                onKeyDown={(event) => {
                  if (event.key === "Enter" && !event.shiftKey) {
                    event.preventDefault();
                    void send();
                  }
                }}
              />
              <div className="mt-2 flex items-center justify-between">
                <IconBtn label="New chat" onClick={startNewChat}>
                  <Plus className="h-4 w-4" />
                </IconBtn>
                {pending ? (
                  <button
                    type="button"
                    data-testid="chat-stop"
                    className="inline-flex h-9 w-9 items-center justify-center rounded-full bg-red-600 text-white hover:bg-red-500"
                    onClick={() => abortRef.current?.abort()}
                    aria-label="Stop"
                  >
                    <Square className="h-3.5 w-3.5 fill-current" />
                  </button>
                ) : (
                  <button
                    type="submit"
                    disabled={!chatReady || !draft.trim()}
                    aria-label={session.stale ? "Stale — Refresh First" : "Send"}
                    className="inline-flex h-9 w-9 items-center justify-center rounded-full bg-stone-900 text-white hover:bg-stone-700 disabled:cursor-not-allowed disabled:bg-stone-200 disabled:text-stone-400 dark:bg-stone-100 dark:text-stone-900 dark:hover:bg-white dark:disabled:bg-stone-700"
                  >
                    <ArrowUp className="h-4 w-4" />
                  </button>
                )}
              </div>
            </form>
          </div>
        </section>
      </div>
      <ConfirmDialog
        open={Boolean(loadTarget)}
        title="Load this transcript?"
        body="This replaces the live thread with the saved Chat file. The file stays on disk. This is Chat history, not a sealed Run or eval pass."
        confirmLabel="Load history"
        onCancel={() => setLoadTarget(null)}
        onConfirm={() => {
          if (loadTarget) {
            void applyLoad(loadTarget);
          }
        }}
      />
    </div>
  );
}
