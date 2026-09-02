import { FormEvent, useEffect, useRef, useState } from "react";
import { ErrorBanner } from "../components/RecoveryBanner";
import { IoPanel } from "../components/IoPanel";
import { GhostButton, PageHeader, PrimaryButton } from "../components/ui";
import { clearThread, loadThread, normalizeChatHistory, saveThread, type ChatTurn } from "../lib/chat";
import { useAgentId, useAsync } from "../lib/hooks";
import { parseAgentIo } from "../lib/io";
import { clipLogText, logUi } from "../log/bus";
import { useSession } from "../state/session";

export function ChatPage() {
  const agentId = useAgentId();
  const session = useSession();
  const panel = useAsync(async () => {
    const [structure, llm] = await Promise.all([
      session.client.getStructure(agentId),
      session.client.getAgentLlm(agentId),
    ]);
    return { structure, llm };
  }, [session.client, agentId]);
  const [turns, setTurns] = useState<ChatTurn[]>(() => loadThread(agentId));
  const [draft, setDraft] = useState("");
  const [error, setError] = useState<Error | null>(null);
  const [pending, setPending] = useState(false);
  const logRef = useRef<HTMLDivElement>(null);
  const io = parseAgentIo(panel.data?.structure.io);
  const chatReady = session.healthOk && !session.stale && !session.containment;

  useEffect(() => {
    setTurns(loadThread(agentId));
    setDraft("");
    setError(null);
  }, [agentId]);

  useEffect(() => {
    saveThread(agentId, turns);
  }, [agentId, turns]);

  useEffect(() => {
    logRef.current?.scrollTo({ top: logRef.current.scrollHeight });
  }, [turns, pending]);

  async function send(event?: FormEvent) {
    event?.preventDefault();
    const message = draft.trim();
    if (!message || pending) {
      return;
    }
    const nextTurns: ChatTurn[] = [...turns, { role: "user", content: message }];
    setTurns(nextTurns);
    setDraft("");
    setError(null);
    setPending(true);
    session.setRunning(true);
    logUi(`chat send ${agentId}`, clipLogText(message));
    try {
      const result = await session.client.chatAgent(agentId, {
        message,
        history: normalizeChatHistory(turns),
      });
      setTurns([
        ...nextTurns,
        {
          role: "assistant",
          content: result.reply || "(empty reply)",
          provider: result.provider,
        },
      ]);
      logUi(`chat reply ${agentId} ${result.provider ?? ""}`, clipLogText(result.reply));
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
      setTurns(nextTurns);
    } finally {
      setPending(false);
      session.setRunning(false);
    }
  }

  return (
    <div data-testid="agent-chat">
      <PageHeader
        title="Chat"
        asOf={panel.asOf}
        actions={
          <GhostButton type="button" onClick={() => { clearThread(agentId); setTurns([]); }}>
            Clear
          </GhostButton>
        }
      />
      <p className="mb-4 text-sm text-stone-500">
        Type a text message to talk to <span className="font-mono">{agentId}</span>. Host LLM{" "}
        <span className="font-mono">{panel.data?.llm.provider ?? "local_deterministic"}</span> is used by default.
        Does not write memory, run plugins, enable T3, or grant network.
      </p>
      <ErrorBanner error={error ?? panel.error} />
      <div className="grid grid-cols-1 gap-5 lg:grid-cols-[18rem_minmax(0,1fr)]">
        <IoPanel io={io} />
        <section className="flex h-[min(70vh,40rem)] flex-col overflow-hidden rounded-2xl border border-stone-200 bg-white">
          <div ref={logRef} className="flex-1 space-y-3 overflow-y-auto p-4" data-testid="chat-log" aria-live="polite">
            {turns.length === 0 && !pending ? (
              <p className="text-sm text-stone-500">Send a message to talk to this agent.</p>
            ) : null}
            {turns.map((turn, index) => (
              <div
                key={`${turn.role}-${index}`}
                className={turn.role === "user" ? "flex justify-end" : "flex justify-start"}
              >
                <div
                  className={[
                    "max-w-[85%] rounded-2xl px-3 py-2 text-sm whitespace-pre-wrap",
                    turn.role === "user" ? "bg-indigo-600 text-white" : "bg-stone-100 text-stone-900",
                  ].join(" ")}
                  data-testid={turn.role === "user" ? "chat-user" : "chat-assistant"}
                >
                  {turn.content}
                  {turn.role === "assistant" && turn.provider ? (
                    <p className="mt-1 font-mono text-[10px] text-stone-500">{turn.provider}</p>
                  ) : null}
                </div>
              </div>
            ))}
            {pending ? <p className="text-xs text-stone-400">Waiting for the host router…</p> : null}
          </div>
          <form className="flex gap-2 border-t border-stone-200 p-3" onSubmit={(event) => void send(event)}>
            <label className="sr-only" htmlFor="agent-chat-input">
              Message
            </label>
            <textarea
              id="agent-chat-input"
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
            <PrimaryButton type="submit" disabled={!chatReady || pending || !draft.trim()}>
              {session.stale ? "Stale — Refresh First" : "Send"}
            </PrimaryButton>
          </form>
        </section>
      </div>
    </div>
  );
}
