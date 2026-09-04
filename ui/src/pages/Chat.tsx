import { FormEvent, useEffect, useRef, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { ChatMarkdown } from "../components/ChatMarkdown";
import { ConfirmDialog } from "../components/ConfirmDialog";
import { CharacterizationBadge, ChatFixtureList } from "../components/EvalFixtures";
import { ErrorBanner } from "../components/RecoveryBanner";
import { IoPanel } from "../components/IoPanel";
import { DangerButton, GhostButton, PageHeader, PrimaryButton } from "../components/ui";
import { RequestAbortedError, type ChatContextPack, type EvalFixture } from "../api/types";
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
  normalizeChatHistory,
  replaceThread,
  saveThread,
  sessionFromFileName,
  type ChatFile,
  type ChatTurn,
} from "../lib/chat";
import { enqueueChatPersist, flushChatNow, loadChatTranscript, refreshChatFiles, subscribeChatFiles } from "../lib/chatPersist";
import { isPinnedToBottom } from "../lib/chatScroll";
import { chatFixtures, findFixture, fixtureMessage } from "../lib/fixtures";
import { followUpChips } from "../lib/followUps";
import { useAgentId, useAsync } from "../lib/hooks";
import { parseAgentIo } from "../lib/io";
import { clipLogText, logUi } from "../log/bus";
import { useSession } from "../state/session";

function fileLabel(path: string): string {
  return path.replace(/\\/g, "/").split("/").slice(-2).join("/");
}

function ContextPack({ pack }: { pack: ChatContextPack }) {
  const segments = pack.segments ?? [];
  const skills = pack.skills ?? [];
  return (
    <section className="rounded-2xl border border-stone-200 bg-white p-5" data-testid="chat-context">
      <h2 className="mb-1 text-sm font-semibold text-stone-900">Context pack</h2>
      <p className="mb-3 text-xs text-stone-500">
        Host packed this turn from folder segments. Compaction {pack.compaction ?? "disabled"}. Not an eval pass.
        Memory, plugins, and T3 stay off.
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
  if (!ts) {
    return "";
  }
  return ts.slice(11, 19) || ts.slice(0, 10);
}

export function ChatPage() {
  const agentId = useAgentId();
  const session = useSession();
  const [searchParams, setSearchParams] = useSearchParams();
  const panel = useAsync(async () => {
    const [structure, llm] = await Promise.all([
      session.client.getStructure(agentId),
      session.client.getAgentLlm(agentId),
    ]);
    return { structure, llm };
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
  const logRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLTextAreaElement>(null);
  const abortRef = useRef<AbortController | null>(null);
  const io = parseAgentIo(panel.data?.structure.io);
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
    setPinned(true);
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
    function onKey(event: KeyboardEvent) {
      if (event.key === "Escape") {
        abortRef.current?.abort();
      }
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  useEffect(() => {
    if (!fixtureId || !fixtures.data) {
      return;
    }
    const item = findFixture(fixtures.data, fixtureId);
    const message = fixtureMessage(item);
    if (message) {
      setDraft(message);
      inputRef.current?.focus();
    }
    const next = new URLSearchParams(searchParams);
    if (next.has("fixture")) {
      next.delete("fixture");
      setSearchParams(next, { replace: true });
    }
  }, [agentId, fixtureId, fixtures.data, searchParams, setSearchParams]);

  function loadCase(item: EvalFixture) {
    const message = fixtureMessage(item);
    if (!message) {
      return;
    }
    setDraft(message);
    inputRef.current?.focus();
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
        { message, history: normalizeChatHistory(historyTurns) },
        { signal: controller.signal },
      );
      const assistantTurn: ChatTurn = {
        role: "assistant",
        content: result.reply || "(empty reply)",
        provider: result.provider,
        truncated: chatHitOutputCap(result.llm),
        ts: new Date().toISOString(),
      };
      const withReply = [...baseTurns, assistantTurn];
      setTurns(withReply);
      saveThread(agentId, withReply);
      enqueueChatPersist(agentId, loadThread(agentId).session, assistantTurn);
      void flushChatNow();
      setContextPack(result.context ?? null);
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
    const userTurn: ChatTurn = { role: "user", content: trimmed, ts: new Date().toISOString() };
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

  return (
    <div data-testid="agent-chat">
      <PageHeader
        title="Chat"
        asOf={panel.asOf}
        actions={
          <>
            <GhostButton type="button" data-testid="chat-export-md" disabled={!turns.length} onClick={exportMd}>
              Export MD
            </GhostButton>
            <GhostButton type="button" data-testid="chat-export-json" disabled={!turns.length} onClick={exportJson}>
              Export JSON
            </GhostButton>
            <GhostButton
              type="button"
              onClick={() => {
                abortRef.current?.abort();
                const next = clearThread(agentId);
                setTurns(next.turns);
                setFiles(next.files);
                setStopped(false);
              }}
            >
              Clear
            </GhostButton>
          </>
        }
      />
      <p className="mb-4 text-sm text-stone-500">
        Type a text message to talk to <span className="font-mono">{agentId}</span>. The host packs identity plus the
        operational prompt under <span className="font-mono">runtime/context.json</span> budgets. It does not dump
        SKILL.md, memory, or tools. Host LLM{" "}
        <span className="font-mono">{panel.data?.llm.provider ?? "local_deterministic"}</span>. Export is a Chat
        transcript, not a sealed Run.
      </p>
      <ErrorBanner error={error ?? panel.error} />
      <div className="grid grid-cols-1 gap-5 lg:grid-cols-[18rem_minmax(0,1fr)]">
        <div className="order-2 space-y-5 lg:order-1">
          <IoPanel io={io} />
          {contextPack ? <ContextPack pack={contextPack} /> : null}
          {files.length ? (
            <section className="rounded-2xl border border-stone-200 bg-white p-5" data-testid="chat-files">
              <h2 className="mb-1 text-sm font-semibold text-stone-900">Saved transcripts</h2>
              <p className="mb-3 text-xs text-stone-500">
                Load replaces the live thread. Files stay on disk. Clear starts a new file and does not delete these.
              </p>
              <ul className="space-y-2">
                {files.slice(0, 8).map((file) => (
                  <li key={file.path} className="flex items-start justify-between gap-2" data-testid="chat-file">
                    <span className="min-w-0 font-mono text-[11px] text-stone-500">
                      {file.ts.slice(0, 19).replace("T", " ")}
                      <span className="mt-0.5 block break-all">{fileLabel(file.path)}</span>
                    </span>
                    <GhostButton
                      type="button"
                      data-testid="chat-load-history"
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
                  </li>
                ))}
              </ul>
            </section>
          ) : (
            <p className="font-mono text-[11px] text-stone-400" data-testid="chat-files-empty">
              Transcripts save under logs/chat/{agentId}/ with a timestamped file per conversation.
            </p>
          )}
        </div>
        <section className="relative order-1 flex h-[min(70vh,40rem)] flex-col overflow-hidden rounded-2xl border border-stone-200 bg-white lg:order-2">
          <div
            ref={logRef}
            className="flex-1 space-y-3 overflow-y-auto p-4"
            data-testid="chat-log"
            aria-live="polite"
            onScroll={(event) => setPinned(isPinnedToBottom(event.currentTarget))}
          >
            {turns.length === 0 && !pending ? (
              <div>
                <p className="text-sm text-stone-500">Send a message to talk to this agent.</p>
                {cases.length ? (
                  <div className="mt-4">
                    <div className="mb-2 flex flex-wrap items-center gap-2">
                      <p className="text-sm font-medium text-stone-800">Characterization cases</p>
                      <CharacterizationBadge />
                    </div>
                    <p className="mb-3 text-xs text-stone-500">
                      Load fills the composer only. Sending is still host Chat, not an eval pass.
                    </p>
                    <ChatFixtureList items={cases} onLoad={loadCase} />
                  </div>
                ) : null}
              </div>
            ) : null}
            {turns.map((turn, index) => {
              const key = `${turn.role}-${index}`;
              const lastAssistantTurn = turn.role === "assistant" && index === turns.length - 1;
              return (
                <div key={key} className={turn.role === "user" ? "flex justify-end" : "flex justify-start"}>
                  <div
                    className={[
                      "max-w-[85%] rounded-2xl px-3 py-2 text-sm",
                      turn.role === "user" ? "bg-indigo-600 text-white whitespace-pre-wrap" : "bg-stone-100 text-stone-900",
                    ].join(" ")}
                    data-testid={turn.role === "user" ? "chat-user" : "chat-assistant"}
                  >
                    {turn.role === "assistant" ? <ChatMarkdown text={turn.content} /> : turn.content}
                    {turn.role === "assistant" && turn.truncated ? (
                      <p className="mt-1 text-[11px] text-amber-800" data-testid="chat-output-cap">
                        Reply hit the output token cap.
                      </p>
                    ) : null}
                    <div className="mt-1 flex flex-wrap items-center gap-2">
                      <p
                        className={`font-mono text-[10px] ${turn.role === "user" ? "text-indigo-100" : "text-stone-500"}`}
                        data-testid="chat-turn-time"
                      >
                        {turnTime(turn.ts)}
                        {turn.role === "assistant" && turn.provider ? ` · ${turn.provider}` : ""}
                      </p>
                      <button
                        type="button"
                        className={`text-[10px] underline-offset-2 hover:underline ${
                          turn.role === "user" ? "text-indigo-100" : "text-stone-500"
                        }`}
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
                      {lastAssistantTurn && !pending ? (
                        <button
                          type="button"
                          className="text-[10px] text-stone-500 underline-offset-2 hover:underline"
                          data-testid="chat-regenerate"
                          disabled={!chatReady || !canRegenerate(turns)}
                          onClick={() => void regenerate()}
                        >
                          Regenerate
                        </button>
                      ) : null}
                    </div>
                  </div>
                </div>
              );
            })}
            {pending ? <p className="text-xs text-stone-400">Waiting for the host router…</p> : null}
            {stopped && !pending ? (
              <p className="text-xs text-amber-800" data-testid="chat-stopped">
                Generation stopped. The last user message is kept.
              </p>
            ) : null}
            {!pending && chips.length > 0 ? (
              <div className="flex flex-wrap gap-2 pt-1" data-testid="chat-follow-ups">
                {chips.map((chip) => (
                  <button
                    key={chip}
                    type="button"
                    data-testid="chat-follow-up"
                    className="rounded-full border border-stone-200 bg-white px-3 py-1 text-left text-xs text-stone-700 hover:border-stone-300 hover:text-stone-900"
                    disabled={!chatReady}
                    onClick={() => void sendMessage(chip)}
                  >
                    {chip}
                  </button>
                ))}
              </div>
            ) : null}
          </div>
          {!pinned ? (
            <button
              type="button"
              data-testid="chat-jump-latest"
              className="absolute bottom-24 right-4 rounded-full border border-stone-200 bg-white px-3 py-1 text-xs text-stone-700 shadow-sm"
              onClick={() => {
                setPinned(true);
                logRef.current?.scrollTo({ top: logRef.current.scrollHeight });
              }}
            >
              Jump to latest
            </button>
          ) : null}
          <div className="border-t border-stone-200">
            {turns.length > 0 && cases.length ? (
              <details className="border-b border-stone-200 px-3 py-2">
                <summary className="cursor-pointer text-xs text-stone-600">Load a characterization case</summary>
                <p className="mt-2 text-[11px] text-stone-500">Fills the composer. Not an eval pass.</p>
                <div className="mt-2">
                  <ChatFixtureList items={cases} onLoad={loadCase} compact />
                </div>
              </details>
            ) : null}
            <form className="flex gap-2 p-3" onSubmit={(event) => void send(event)}>
              <label className="sr-only" htmlFor="agent-chat-input">
                Message
              </label>
              <textarea
                id="agent-chat-input"
                ref={inputRef}
                data-testid="chat-input"
                className="min-h-[2.5rem] flex-1 resize-none rounded-lg border border-stone-200 bg-white px-3 py-2 text-sm text-stone-900"
                rows={2}
                value={draft}
                placeholder="Message this agent"
                onChange={(event) => setDraft(event.target.value)}
                onKeyDown={(event) => {
                  if (event.key === "Enter" && !event.shiftKey) {
                    event.preventDefault();
                    void send();
                  }
                }}
              />
              {pending ? (
                <DangerButton
                  type="button"
                  data-testid="chat-stop"
                  onClick={() => abortRef.current?.abort()}
                >
                  Stop
                </DangerButton>
              ) : (
                <PrimaryButton type="submit" disabled={!chatReady || !draft.trim()}>
                  {session.stale ? "Stale — Refresh First" : "Send"}
                </PrimaryButton>
              )}
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
