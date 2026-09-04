import { useEffect, useMemo, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { DryRunControl, OperatorContractFields } from "../components/ActorStrip";
import { ConfirmDialog } from "../components/ConfirmDialog";
import { ErrorBanner } from "../components/RecoveryBanner";
import { MarkdownBody } from "../components/MarkdownBody";
import { Card, EmptyState, GhostButton, JsonWell, PageHeader, PrimaryButton, inputClass } from "../components/ui";
import type { AgentFileFolder, AgentFileItem, AgentFileRow } from "../api/types";
import { useAgentId, useAsync } from "../lib/hooks";
import { pretty } from "../lib/json";
import { isJsonPath, isMarkdownPath } from "../lib/markdown";
import { useSession } from "../state/session";

function folderOf(path: string): string {
  return path.split("/")[0] ?? "";
}

function FilePreview({ path, text }: { path: string; text: string }) {
  if (isMarkdownPath(path)) {
    return (
      <div
        className="h-[60vh] min-h-[28rem] overflow-auto rounded-xl border border-stone-200 bg-white p-5"
        data-testid="files-preview"
      >
        <MarkdownBody text={text} />
      </div>
    );
  }
  if (isJsonPath(path)) {
    return (
      <div data-testid="files-preview">
        <JsonWell value={pretty(text)} />
      </div>
    );
  }
  return (
    <pre
      className="h-[60vh] min-h-[28rem] overflow-auto rounded-xl border border-stone-200 bg-stone-50 p-4 font-mono text-xs leading-relaxed text-stone-800"
      data-testid="files-preview"
    >
      {text}
    </pre>
  );
}

function pickDefaultPath(folders: AgentFileFolder[]): string {
  const preferred = folders
    .flatMap((folder) => folder.files)
    .find((file) => file.path === "prompts/primary.md" && file.kind === "text");
  if (preferred) {
    return preferred.path;
  }
  const first = folders.flatMap((folder) => folder.files).find((file) => file.kind === "text");
  return first?.path ?? "";
}

export function FilesPage() {
  const agentId = useAgentId();
  const session = useSession();
  const [params, setParams] = useSearchParams();
  const requested = params.get("path") ?? "";
  const tree = useAsync(() => session.client.listAgentFiles(agentId), [session.client, agentId]);
  const folders = tree.data?.folders ?? [];
  const allFiles = useMemo(() => folders.flatMap((folder) => folder.files), [folders]);
  const [activeFolder, setActiveFolder] = useState("");
  const [item, setItem] = useState<AgentFileItem | null>(null);
  const [draft, setDraft] = useState("");
  const [loadError, setLoadError] = useState<Error | null>(null);
  const [saveError, setSaveError] = useState<Error | null>(null);
  const [notice, setNotice] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const [confirm, setConfirm] = useState(false);
  const [view, setView] = useState<"preview" | "source">("preview");

  const selectedPath = requested || (tree.data ? pickDefaultPath(folders) : "");
  const selectedMeta: AgentFileRow | undefined = allFiles.find((file) => file.path === selectedPath);
  const filesInFolder = folders.find((folder) => folder.name === (activeFolder || folderOf(selectedPath)))?.files ?? [];
  const dirty = item !== null && draft !== (item.content ?? "");
  const blocked = !session.mutationReady
    ? session.stale
      ? "Connection is stale. Refresh first."
      : !session.healthOk
        ? "Control plane is unavailable."
        : session.containment
          ? "Containment is on. Mutations stay disabled."
          : "Enter a mutation reason, then save."
    : null;
  const canSave = Boolean(item?.writable) && dirty && session.mutationReady && !busy;

  useEffect(() => {
    if (!tree.data) {
      return;
    }
    const nextPath = requested || pickDefaultPath(tree.data.folders);
    const nextFolder = folderOf(nextPath) || tree.data.folders.find((folder) => folder.present)?.name || "prompts";
    setActiveFolder(nextFolder);
    if (nextPath && !requested) {
      setParams({ path: nextPath }, { replace: true });
    }
  }, [tree.data, requested, setParams]);

  useEffect(() => {
    setView("preview");
  }, [selectedPath]);

  useEffect(() => {
    if (!selectedPath) {
      setItem(null);
      setDraft("");
      return;
    }
    let cancelled = false;
    setLoadError(null);
    setNotice(null);
    session.client
      .getAgentFile(agentId, selectedPath)
      .then((body) => {
        if (cancelled) {
          return;
        }
        setItem(body);
        setDraft(body.content ?? "");
      })
      .catch((err: unknown) => {
        if (cancelled) {
          return;
        }
        setItem(null);
        setDraft("");
        setLoadError(err instanceof Error ? err : new Error(String(err)));
      });
    return () => {
      cancelled = true;
    };
  }, [session.client, agentId, selectedPath]);

  function selectPath(path: string) {
    setParams({ path });
    setActiveFolder(folderOf(path));
    setView("preview");
    setSaveError(null);
    setNotice(null);
  }

  async function save() {
    if (!item || !canSave) {
      return;
    }
    setConfirm(false);
    setBusy(true);
    setSaveError(null);
    setNotice(null);
    try {
      const body = await session.client.putAgentFile(agentId, item.path, draft);
      setNotice(body.saved ? `Saved ${body.path}` : `Dry-run only — ${body.path} was not written`);
      if (body.saved) {
        setItem({ ...item, content: draft, bytes: body.bytes, sha256: body.sha256 ?? item.sha256 });
        tree.reload();
      }
    } catch (err) {
      setSaveError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setBusy(false);
    }
  }

  function onSaveClick() {
    if (session.dryRun) {
      void save();
      return;
    }
    setConfirm(true);
  }

  return (
    <div>
      <PageHeader
        title="Files"
        asOf={tree.asOf}
        actions={
          <>
            <DryRunControl />
            <GhostButton type="button" disabled={!selectedPath || busy} onClick={() => selectPath(selectedPath)}>
              Reload
            </GhostButton>
            <PrimaryButton type="button" disabled={!canSave} onClick={onSaveClick} data-testid="files-save">
              {session.stale ? "Stale — Refresh First" : session.mutationLabel("Save file", "Preview save")}
            </PrimaryButton>
          </>
        }
      />
      <p className="mb-4 text-sm text-stone-500">
        On-disk folders under <span className="font-mono">agents/&lt;id&gt;/</span>. Existing tabs show host slices
        (policy, attestation, incidents), not these files. Writes need mutation headers. Host-owned corrigibility and
        generated locks stay read-only. This does not enable T3, network, plugin execution, or memory writes.
      </p>
      <div className="mb-5">
        <OperatorContractFields />
      </div>
      <ErrorBanner error={loadError ?? saveError ?? tree.error} />
      {notice ? <p className="mb-4 text-sm text-emerald-800">{notice}</p> : null}
      {blocked && dirty ? <p className="mb-4 text-sm text-amber-800">{blocked}</p> : null}
      {tree.data ? (
        <div className="grid grid-cols-1 gap-5 lg:grid-cols-[16rem_minmax(0,1fr)]">
          <Card className="lg:max-h-[70vh] lg:overflow-auto">
            <div data-testid="files-folders">
            <h2 className="mb-3 text-sm font-semibold">Folders</h2>
            <div className="flex flex-wrap gap-1 lg:flex-col">
              {folders.map((folder) => (
                <button
                  key={folder.name}
                  type="button"
                  className={`rounded-lg px-2 py-1 text-left text-xs ${
                    folder.name === activeFolder
                      ? "bg-indigo-600 text-white"
                      : folder.present
                        ? "text-stone-700 hover:bg-stone-100"
                        : "text-stone-400"
                  }`}
                  onClick={() => setActiveFolder(folder.name)}
                >
                  {folder.name}
                  <span className="ml-1 opacity-70">{folder.present ? folder.files.length : "—"}</span>
                </button>
              ))}
            </div>
            <h2 className="mb-2 mt-4 text-sm font-semibold">Files</h2>
            <ul className="space-y-1" data-testid="files-list">
              {filesInFolder.length ? (
                filesInFolder.map((file) => (
                  <li key={file.path}>
                    <button
                      type="button"
                      className={`block w-full truncate rounded-lg px-2 py-1 text-left font-mono text-xs ${
                        file.path === selectedPath ? "bg-stone-900 text-white" : "text-stone-700 hover:bg-stone-100"
                      }`}
                      onClick={() => selectPath(file.path)}
                    >
                      {file.path.slice(activeFolder.length + 1) || file.path}
                    </button>
                  </li>
                ))
              ) : (
                <li className="text-xs text-stone-400">No files in this folder.</li>
              )}
            </ul>
            </div>
          </Card>
          <Card>
            {selectedPath ? (
              <p className="mb-2 font-mono text-xs text-stone-400" data-testid="files-path">
                {selectedPath}
              </p>
            ) : null}
            {item ? (
              <>
                <div className="mb-3 flex flex-wrap items-center gap-2 text-xs">
                  <span className="font-mono text-sm text-stone-900">{item.path}</span>
                  <span
                    className={`rounded-full border px-2 py-0.5 ${
                      item.writable ? "border-emerald-200 bg-emerald-50 text-emerald-800" : "border-stone-200 bg-stone-50 text-stone-500"
                    }`}
                    data-testid="files-writable"
                  >
                    {item.writable ? "writable" : item.host_owned ? "host-owned read-only" : "read-only"}
                  </span>
                  <span className="text-stone-400">{item.bytes} bytes</span>
                  {item.kind === "text" ? (
                    <span className="ml-auto flex gap-1">
                      <GhostButton
                        type="button"
                        className={view === "preview" ? "!bg-stone-900 !text-white" : ""}
                        data-testid="files-view-preview"
                        onClick={() => setView("preview")}
                      >
                        Preview
                      </GhostButton>
                      <GhostButton
                        type="button"
                        className={view === "source" ? "!bg-stone-900 !text-white" : ""}
                        data-testid="files-view-source"
                        onClick={() => setView("source")}
                      >
                        Source
                      </GhostButton>
                    </span>
                  ) : null}
                </div>
                {item.kind === "text" ? (
                  view === "preview" ? (
                    <FilePreview path={item.path} text={draft} />
                  ) : (
                    <textarea
                      data-testid="files-editor"
                      className={`${inputClass} min-h-[28rem] h-[60vh] w-full resize-y py-3 font-mono text-xs leading-relaxed`}
                      value={draft}
                      disabled={!item.writable}
                      onChange={(event) => setDraft(event.target.value)}
                      spellCheck={false}
                    />
                  )
                ) : (
                  <EmptyState title="Not a text file" body={`${item.path} is ${item.kind} and cannot be edited here.`} />
                )}
                {selectedMeta && !item.writable ? (
                  <p className="mt-3 text-xs text-stone-500">
                    Host-owned or binary files can be viewed when they are text, but PUT is rejected.
                  </p>
                ) : null}
              </>
            ) : selectedPath ? (
              <p className="text-sm text-stone-500">Loading {selectedPath}…</p>
            ) : (
              <EmptyState
                title="Select a file"
                body="Choose a configuration folder on the left, then a file. Missing folders are listed as empty."
              />
            )}
          </Card>
        </div>
      ) : null}
      <ConfirmDialog
        open={confirm}
        title="Write this file?"
        body={
          <p>
            This PUTs <span className="font-mono">{item?.path}</span> into the agent folder. Dry-run is off, so the
            host will persist the bytes if the mutation contract is accepted.
          </p>
        }
        confirmLabel="Save file"
        onCancel={() => setConfirm(false)}
        onConfirm={() => void save()}
      />
    </div>
  );
}
