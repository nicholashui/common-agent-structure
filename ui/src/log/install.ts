import { appendLog, logUi, snapshot, subscribe } from "./bus";
import { enqueueLogPersist } from "./persist";

let installed = false;

export function installLogCapture(): void {
  if (installed) {
    return;
  }
  installed = true;
  for (const channel of ["api", "ui"] as const) {
    for (const entry of snapshot(channel)) {
      enqueueLogPersist(entry);
    }
  }
  subscribe((_channel, entries) => {
    const latest = entries[entries.length - 1];
    if (latest) {
      enqueueLogPersist(latest);
    }
  });
  const warn = console.warn.bind(console);
  const error = console.error.bind(console);
  let quiet = false;
  function capture(level: "warn" | "error", args: unknown[]): void {
    if (quiet || !shouldCaptureConsole(args)) {
      return;
    }
    quiet = true;
    try {
      logUi(args.map(String).join(" "), undefined, level);
    } finally {
      quiet = false;
    }
  }
  console.warn = (...args: unknown[]) => {
    warn(...args);
    capture("warn", args);
  };
  console.error = (...args: unknown[]) => {
    error(...args);
    capture("error", args);
  };
}

function shouldCaptureConsole(args: unknown[]): boolean {
  const text = args.map(String).join(" ");
  return !text.includes("React Router Future Flag Warning") && !text.includes("/debug/logs");
}

let lastNav = { path: "", at: 0 };

export function recordNavigation(pathname: string): void {
  const now = Date.now();
  if (lastNav.path === pathname && now - lastNav.at < 750) {
    return;
  }
  lastNav = { path: pathname, at: now };
  appendLog({ channel: "ui", message: `navigate ${pathname}` });
}
