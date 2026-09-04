import { afterEach, describe, expect, it, vi } from "vitest";
import {
  canRegenerate,
  clearThread,
  exportThreadJson,
  exportThreadMarkdown,
  loadThread,
  rememberChatFiles,
  replaceThread,
  resetChatForTests,
  saveThread,
  sessionFromFileName,
} from "../src/lib/chat";
import { followUpChips } from "../src/lib/followUps";
import { isPinnedToBottom } from "../src/lib/chatScroll";
import { enqueueChatPersist, flushChatNow, resetChatPersistForTests, startChatSink } from "../src/lib/chatPersist";

afterEach(() => {
  resetChatForTests();
  resetChatPersistForTests();
  vi.unstubAllGlobals();
});

describe("per-agent chat history", () => {
  it("keeps separate timestamped threads and remembers files after clear", () => {
    saveThread("common.health", [{ role: "user", content: "ping", ts: "2026-09-02T12:00:00.000Z" }]);
    saveThread("video.director", [{ role: "assistant", content: "ready", ts: "2026-09-02T12:01:00.000Z" }]);
    expect(loadThread("common.health").turns[0].content).toBe("ping");
    expect(loadThread("video.director").turns[0].content).toBe("ready");
    rememberChatFiles("common.health", [
      {
        path: "logs/chat/common.health/2026-09-02-12-00-00.jsonl",
        name: "2026-09-02-12-00-00.jsonl",
        ts: "2026-09-02T12:00:00.000Z",
      },
    ]);
    const cleared = clearThread("common.health");
    expect(cleared.turns).toEqual([]);
    expect(cleared.files[0].name).toBe("2026-09-02-12-00-00.jsonl");
    expect(loadThread("video.director").turns).toHaveLength(1);
  });
});

describe("chat transcript sink", () => {
  it("posts timestamped turns to /debug/chat", async () => {
    const bodies: unknown[] = [];
    vi.stubGlobal(
      "fetch",
      async (input: string, init?: RequestInit) => {
        expect(String(input)).toBe("http://127.0.0.1:18080/debug/chat");
        bodies.push(JSON.parse(String(init?.body)));
        return new Response(
          JSON.stringify({
            ok: true,
            files: { transcript: "./logs/chat/common.health/session.jsonl" },
          }),
          { status: 200, headers: { "Content-Type": "application/json" } },
        );
      },
    );
    startChatSink(() => "http://127.0.0.1:18080");
    enqueueChatPersist("common.health", "2026-09-02-12-00-00-sess", {
      role: "user",
      content: "ping",
      ts: "2026-09-02T12:00:00.000Z",
    });
    await flushChatNow();
    expect(bodies).toHaveLength(1);
    const body = bodies[0] as { agent_id: string; session: string; entries: { ts: string; role: string }[] };
    expect(body.agent_id).toBe("common.health");
    expect(body.session).toBe("2026-09-02-12-00-00-sess");
    expect(body.entries[0].ts).toBe("2026-09-02T12:00:00.000Z");
    expect(body.entries[0].role).toBe("user");
    expect(loadThread("common.health").files[0].name).toBe("session.jsonl");
  });
});

describe("chat transcript helpers", () => {
  it("exports markdown and json without claiming a run pass", () => {
    const turns = [
      { role: "user" as const, content: "hello", ts: "2026-09-04T12:00:00.000Z" },
      { role: "assistant" as const, content: "hi", provider: "xai", ts: "2026-09-04T12:00:01.000Z" },
    ];
    const md = exportThreadMarkdown("video.director", turns);
    expect(md).toContain("# Chat with video.director");
    expect(md).toContain("Not a sealed Run");
    expect(md).toContain("## user");
    expect(md).toContain("hello");
    const json = JSON.parse(exportThreadJson("video.director", "sess-1", turns));
    expect(json.agent_id).toBe("video.director");
    expect(json.honesty).toBe("CHARACTERIZATION");
    expect(json.turns).toHaveLength(2);
  });

  it("regenerates only after an assistant reply", () => {
    expect(canRegenerate([{ role: "user", content: "hi" }])).toBe(false);
    expect(
      canRegenerate([
        { role: "user", content: "hi" },
        { role: "assistant", content: "hello" },
      ]),
    ).toBe(true);
  });

  it("loads a transcript into a named session", () => {
    expect(sessionFromFileName("2026-09-04-00-58-35-810-jzswag.jsonl")).toBe(
      "2026-09-04-00-58-35-810-jzswag",
    );
    const next = replaceThread(
      "common.health",
      [{ role: "user", content: "loaded" }],
      "2026-09-04-00-58-35-810-jzswag",
    );
    expect(next.session).toBe("2026-09-04-00-58-35-810-jzswag");
    expect(loadThread("common.health").turns[0].content).toBe("loaded");
  });

  it("builds follow-up chips from questions or fallbacks", () => {
    const fromQuestion = followUpChips("You could try X.\nWhat should we do next?");
    expect(fromQuestion[0]).toBe("What should we do next?");
    expect(fromQuestion).toHaveLength(3);
    const fallback = followUpChips("No questions here.");
    expect(fallback[0]).toMatch(/Summarize/i);
  });

  it("treats near-bottom as pinned", () => {
    expect(isPinnedToBottom({ scrollHeight: 400, scrollTop: 320, clientHeight: 80 } as HTMLElement)).toBe(true);
    expect(isPinnedToBottom({ scrollHeight: 400, scrollTop: 10, clientHeight: 80 } as HTMLElement)).toBe(false);
  });
});
