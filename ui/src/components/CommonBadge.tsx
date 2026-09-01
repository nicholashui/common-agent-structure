export function CommonBadge({ version = "3.0", hash }: { version?: string; hash?: string }) {
  const prefix = hash ? hash.slice(0, 8) : undefined;
  return (
    <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-indigo-50 border border-indigo-200 text-indigo-700 text-xs font-mono whitespace-nowrap">
      <span className="font-semibold text-indigo-600">Common</span>
      <span>v{version}</span>
      {prefix ? <span className="text-stone-400 hidden sm:inline">· {prefix}</span> : null}
    </span>
  );
}
