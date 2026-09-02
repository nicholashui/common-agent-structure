import { afterEach, describe, expect, it, vi } from "vitest";
import {
  clearThread,
  loadThread,
  rememberChatFiles,
  resetChatForTests,
  saveThread,
} from "../src/lib/chat";
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
            files: { transcript: "C:/Project/common-agent-structure/logs/chat/common.health/session.jsonl" },
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
