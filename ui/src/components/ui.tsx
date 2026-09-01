import type { ButtonHTMLAttributes, ReactNode } from "react";

const focus = "focus-visible:ring-2 focus-visible:ring-indigo-600 focus-visible:ring-offset-2";

export function PrimaryButton(props: ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button
      {...props}
      className={`inline-flex items-center justify-center gap-1.5 rounded-full bg-stone-900 px-4 py-2 text-xs font-medium text-white hover:bg-stone-700 disabled:cursor-not-allowed disabled:bg-stone-300 disabled:text-stone-500 ${focus} ${props.className ?? ""}`}
    />
  );
}

export function CommonButton(props: ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button
      {...props}
      className={`inline-flex items-center justify-center gap-1.5 rounded-full bg-indigo-600 px-4 py-2 text-xs font-medium text-white hover:bg-indigo-500 disabled:cursor-not-allowed disabled:bg-indigo-200 ${focus} ${props.className ?? ""}`}
    />
  );
}

export function DangerButton(props: ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button
      {...props}
      className={`inline-flex items-center justify-center gap-1.5 rounded-full bg-red-600 px-4 py-2 text-xs font-medium text-white hover:bg-red-500 disabled:cursor-not-allowed disabled:bg-red-200 ${focus} ${props.className ?? ""}`}
    />
  );
}

export function GhostButton(props: ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button
      {...props}
      className={`inline-flex items-center justify-center gap-1.5 rounded-full border border-stone-200 bg-white px-4 py-2 text-xs font-medium text-stone-700 hover:border-stone-300 hover:text-stone-900 disabled:cursor-not-allowed disabled:bg-stone-100 disabled:text-stone-400 ${focus} ${props.className ?? ""}`}
    />
  );
}

export function Card({ children, className = "" }: { children: ReactNode; className?: string }) {
  return <section className={`rounded-2xl border border-stone-200 bg-white p-5 hover:shadow-md ${className}`}>{children}</section>;
}

export function Field({
  label,
  children,
  hint,
}: {
  label: string;
  children: ReactNode;
  hint?: string;
}) {
  return (
    <label className="flex min-w-0 flex-col gap-1 text-xs font-medium text-stone-700">
      {label}
      {children}
      {hint ? <span className="font-normal text-stone-500">{hint}</span> : null}
    </label>
  );
}

export const inputClass =
  "h-9 rounded-lg border border-stone-200 bg-white px-3 text-sm text-stone-900 placeholder:text-stone-400 disabled:bg-stone-100";

export function AsOf({ date }: { date?: Date | null }) {
  if (!date) {
    return <p className="text-sm text-stone-500">as_of —</p>;
  }
  return <p className="text-sm text-stone-500">as_of {date.toISOString()}</p>;
}

export function PageHeader({
  title,
  actions,
  asOf,
}: {
  title: string;
  actions?: ReactNode;
  asOf?: Date | null;
}) {
  return (
    <div className="mb-6 flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
      <div>
        <h1 className="text-2xl font-bold tracking-tight text-stone-900">{title}</h1>
        <AsOf date={asOf} />
      </div>
      {actions ? <div className="flex flex-wrap gap-2">{actions}</div> : null}
    </div>
  );
}

export function JsonWell({ value }: { value: unknown }) {
  const text =
    typeof value === "string"
      ? value
      : JSON.stringify(value, null, 2);
  return (
    <pre className="max-h-[32rem] overflow-auto rounded-xl border border-stone-200 bg-stone-50 p-4 font-mono text-xs leading-relaxed text-stone-800">
      {text}
    </pre>
  );
}

export function EmptyState({ title, body }: { title: string; body: string }) {
  return (
    <Card className="bg-stone-50 hover:shadow-none">
      <h2 className="text-base font-semibold text-stone-900">{title}</h2>
      <p className="mt-2 text-sm text-stone-500">{body}</p>
    </Card>
  );
}
