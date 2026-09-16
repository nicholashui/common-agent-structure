import { FormEvent, useEffect, useMemo, useState } from "react";
import { Link, NavLink, useLocation, useNavigate, useParams } from "react-router-dom";
import { Card, Field, GhostButton, PrimaryButton, inputClass } from "../components/ui";
import { DryRunControl } from "../components/ActorStrip";
import { ErrorBanner } from "../components/RecoveryBanner";
import type { ProgramCommItem, ProgramComms, ProgramRecord, ProgramScene, ProgramSequencePayload } from "../api/types";
import { displayRelativePath } from "../lib/paths";
import {
  PROGRAM_FIRST_AGENT_HOP,
  PROGRAM_FIRST_CALLED,
  PROGRAM_LOCKS,
  PROGRAM_PHASES,
  CUT_STATES,
  finishReady,
  generationListLockable,
  spawnMissingLocks,
  spawnReady,
} from "../lib/programs";
import { PROGRAM_INSTANCE_TABS } from "../shell/nav";
import { useSession } from "../state/session";

function tabFromPath(pathname: string): "overview" | "workflow" | "chat" {
  if (pathname.endsWith("/chat")) {
    return "chat";
  }
  if (pathname.endsWith("/workflow")) {
    return "workflow";
  }
  return "overview";
}

export function ProgramViewPage() {
  const params = useParams();
  const programId = params.programId ? decodeURIComponent(params.programId) : "";
  const session = useSession();
  const navigate = useNavigate();
  const location = useLocation();
  const tab = tabFromPath(location.pathname);
  const [record, setRecord] = useState<ProgramRecord | null>(null);
  const [comms, setComms] = useState<ProgramComms | null>(null);
  const [sequence, setSequence] = useState<ProgramSequencePayload | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const [busy, setBusy] = useState(false);
  const [sceneTitle, setSceneTitle] = useState("Scene 1");
  const [segmentPurpose, setSegmentPurpose] = useState("Opening beat");

  function load() {
    if (!programId) {
      return;
    }
    session.client
      .getProgram(programId)
      .then((payload) => {
        setRecord(payload);
        setError(null);
      })
      .catch((err) => setError(err instanceof Error ? err : new Error(String(err))));
    session.client
      .listProgramComms(programId)
      .then(setComms)
      .catch(() => setComms(null));
    session.client
      .getProgramSequence(programId)
      .then(setSequence)
      .catch(() => setSequence(null));
  }

  useEffect(() => {
    load();
  }, [programId, session.client]);

  const locks = record?.locks || {};
  const canSpawn = spawnReady(locks);
  const missingSpawn = spawnMissingLocks(locks);
  const scenes: ProgramScene[] = record?.generation_list?.scenes || [];
  const hops: ProgramCommItem[] = comms?.items || [];

  async function savePatch(body: Record<string, unknown>) {
    if (!programId || !record) {
      return;
    }
    setBusy(true);
    setError(null);
    try {
      const saved = await session.client.saveProgram(programId, { name: record.name, ...body });
      if (saved.dry_run) {
        setError(new Error("Dry-run is on. Uncheck Dry-run in the header to write program/<code>."));
        setRecord({ ...record, ...body, dry_run: true });
        return;
      }
      setRecord(saved);
      const seq = await session.client.getProgramSequence(programId);
      setSequence(seq);
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setBusy(false);
    }
  }

  async function onToggleLock(key: string) {
    const next = !locks[key];
    if (key === "generation_list" && next && !generationListLockable(scenes)) {
      setError(new Error("cannot lock generation_list: empty scenes"));
      return;
    }
    await savePatch({ locks: { ...locks, [key]: next } });
  }

  async function onAddScene(event: FormEvent) {
    event.preventDefault();
    const next = scenes.concat([{ id: `sc${scenes.length + 1}`, title: sceneTitle.trim() || `Scene ${scenes.length + 1}`, segments: [] }]);
    await savePatch({ generation_list: { scenes: next } });
  }

  async function onAddSegment(sceneIndex: number) {
    const next = scenes.map((scene, index) => {
      if (index !== sceneIndex) {
        return scene;
      }
      const segments = [...(scene.segments || [])];
      segments.push({
        id: `seg${scenes.reduce((sum, row) => sum + (row.segments?.length || 0), 0) + 1}`,
        purpose: segmentPurpose.trim() || "Beat",
        duration_s: 6,
        status: "planned",
      });
      return { ...scene, segments };
    });
    await savePatch({ generation_list: { scenes: next } });
  }

  async function onSpawn() {
    if (!programId) {
      return;
    }
    setBusy(true);
    setError(null);
    try {
      const spawned = await session.client.spawnProgram(programId);
      if (spawned.dry_run) {
        setError(new Error("Dry-run is on. Uncheck Dry-run to write child project/<slug> folders."));
        setRecord({ ...record, ...spawned });
        return;
      }
      setRecord(spawned);
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setBusy(false);
    }
  }

  async function onFinish(kind: string) {
    if (!programId) {
      return;
    }
    setBusy(true);
    setError(null);
    try {
      const result = await session.client.finishProgram(programId, kind);
      setRecord({ ...record, ...result });
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setBusy(false);
    }
  }

  const base = `/programs/${encodeURIComponent(programId)}`;
  const fused = sequence?.compile?.fused_request ?? sequence?.sequence?.fused_request ?? null;

  const workflowNodes = useMemo(() => {
    const seen: string[] = [];
    for (const hop of hops) {
      for (const party of [hop.from, hop.to]) {
        if (party && !seen.includes(party)) {
          seen.push(party);
        }
      }
    }
    return seen;
  }, [hops]);

  return (
    <div data-testid="program-view">
      <div className="mb-2 flex flex-wrap items-center justify-between gap-2">
        <h2 className="text-lg font-semibold text-stone-800 dark:text-stone-100">{record?.name || programId || "Program"}</h2>
        <div className="flex flex-wrap items-center gap-2">
          <DryRunControl />
          <GhostButton type="button" onClick={() => navigate("/programs/new")}>
            New program
          </GhostButton>
        </div>
      </div>
      <nav className="mb-4 flex flex-wrap gap-2 text-xs" aria-label="Program sections">
        {PROGRAM_INSTANCE_TABS.map((item) => {
          const to = item.path ? `${base}/${item.path}` : base;
          return (
            <NavLink
              key={item.id}
              to={to}
              end={item.id === "overview"}
              className={({ isActive }) =>
                `rounded-full px-3 py-1 ${isActive ? "bg-stone-900 text-white dark:bg-stone-100 dark:text-stone-900" : "border border-stone-200 text-stone-600 dark:border-stone-700"}`
              }
            >
              {item.label}
            </NavLink>
          );
        })}
      </nav>
      <ErrorBanner error={error} />
      {!record && !error ? (
        <p className="text-sm text-stone-500">Loading program…</p>
      ) : record ? (
        <div className="grid gap-4">
          {tab === "overview" ? (
            <>
              <Card>
                <p className="text-xs font-medium text-stone-500">ISSUE-0013 filmmaking · CHARACTERIZATION</p>
                <p className="mt-1 text-sm text-stone-700 dark:text-stone-200">
                  First agent hop <span className="font-mono">{record.first_agent_hop || PROGRAM_FIRST_AGENT_HOP}</span>
                  . First-called <span className="font-mono">{record.first_called || PROGRAM_FIRST_CALLED}</span>
                  . Screenwriter is W1, not first-called. Child clip Auto Pilot still starts at intent-analysis then{" "}
                  <span className="font-mono">video.promptengineer</span>.
                </p>
                <div className="mt-3 grid max-w-xl gap-3">
                  <Field label="Program Code">
                    <input className={`${inputClass} font-mono`} value={record.code} readOnly disabled data-testid="program-code" />
                  </Field>
                  <Field label="Program Name">
                    <input className={inputClass} value={record.name} readOnly disabled data-testid="program-name" />
                  </Field>
                  <p className="font-mono text-xs text-stone-500" data-testid="program-folder">
                    {displayRelativePath(record.folder)}
                  </p>
                  <p className="font-mono text-xs text-stone-500" data-testid="program-list-ref">
                    {displayRelativePath(record.generation_list_ref)}
                  </p>
                </div>
              </Card>
              <Card>
                <h3 className="mb-2 text-sm font-semibold">Phases W0–W6</h3>
                <div className="flex flex-wrap gap-2" data-testid="program-phase-strip">
                  {PROGRAM_PHASES.map((phase) => {
                    const active = (record.phase || "w0") === phase.id;
                    return (
                      <button
                        key={phase.id}
                        type="button"
                        data-testid={`program-phase-${phase.id}`}
                        className={`rounded-full px-3 py-1 text-xs ${active ? "bg-indigo-600 text-white" : "border border-stone-200 text-stone-600 dark:border-stone-700"}`}
                        onClick={() => void savePatch({ phase: phase.id })}
                        disabled={busy}
                      >
                        {phase.label}
                      </button>
                    );
                  })}
                </div>
              </Card>
              <Card>
                <h3 className="mb-2 text-sm font-semibold">Locks</h3>
                <div className="flex flex-wrap gap-2" data-testid="program-lock-chips">
                  {PROGRAM_LOCKS.map((key) => {
                    const on = Boolean(locks[key]);
                    return (
                      <button
                        key={key}
                        type="button"
                        data-testid={`program-lock-${key}`}
                        aria-pressed={on}
                        className={`rounded-full px-3 py-1 font-mono text-xs ${on ? "bg-emerald-700 text-white" : "border border-stone-200 text-stone-600 dark:border-stone-700"}`}
                        onClick={() => void onToggleLock(key)}
                        disabled={busy || (key === "generation_list" && !locks[key] && !generationListLockable(scenes))}
                      >
                        {key}
                      </button>
                    );
                  })}
                </div>
              </Card>
              <Card>
                <h3 className="mb-2 text-sm font-semibold">Generation list</h3>
                <p className="mb-3 text-xs text-stone-500">
                  One scene may have many segments. One segment = one Project. Cannot lock generation_list while a scene has zero segments. Spawn needs generation_list and visual_bible.
                </p>
                <div data-testid="program-generation-list" className="grid gap-3">
                  {scenes.length === 0 ? <p className="text-sm text-stone-500">No scenes yet.</p> : null}
                  {scenes.map((scene, sceneIndex) => (
                    <div key={scene.id} className="rounded-xl border border-stone-200 p-3 dark:border-stone-700" data-testid={`program-scene-${scene.id}`}>
                      <p className="font-mono text-xs text-stone-500">{scene.id}</p>
                      <p className="text-sm font-medium">{scene.title || scene.id}</p>
                      <ul className="mt-2 grid gap-1 text-sm">
                        {(scene.segments || []).map((segment) => (
                          <li key={segment.id} data-testid={`program-segment-${segment.id}`}>
                            <span className="font-mono text-xs">{segment.id}</span> · {segment.purpose || "segment"}
                            {segment.project_slug ? (
                              <Link className="ml-2 text-indigo-600" to={`/projects/${encodeURIComponent(segment.project_slug)}/chat`}>
                                {segment.project_slug}
                              </Link>
                            ) : null}
                          </li>
                        ))}
                      </ul>
                      <GhostButton type="button" className="mt-2" data-testid={`program-add-segment-${scene.id}`} onClick={() => void onAddSegment(sceneIndex)} disabled={busy}>
                        Add segment
                      </GhostButton>
                    </div>
                  ))}
                </div>
                <form className="mt-3 flex flex-wrap items-end gap-2" onSubmit={(event) => void onAddScene(event)}>
                  <Field label="Scene title">
                    <input className={inputClass} value={sceneTitle} onChange={(event) => setSceneTitle(event.target.value)} data-testid="program-scene-title" />
                  </Field>
                  <Field label="Segment purpose">
                    <input className={inputClass} value={segmentPurpose} onChange={(event) => setSegmentPurpose(event.target.value)} data-testid="program-segment-purpose" />
                  </Field>
                  <PrimaryButton type="submit" data-testid="program-add-scene" disabled={busy}>
                    Add scene
                  </PrimaryButton>
                </form>
              </Card>
              <Card>
                <h3 className="mb-2 text-sm font-semibold">Spawn child Projects</h3>
                <p className="mb-2 text-xs text-stone-500" data-testid="program-spawn-hint">
                  {canSpawn ? "List and visual bible are locked." : `Missing locks: ${missingSpawn.join(", ")}`}
                </p>
                <PrimaryButton type="button" data-testid="program-spawn" disabled={busy || !canSpawn} onClick={() => void onSpawn()}>
                  Spawn projects
                </PrimaryButton>
                <ul className="mt-3 grid gap-1 text-sm" data-testid="program-children">
                  {(record.project_ids || []).map((id) => (
                    <li key={id}>
                      <Link className="font-mono text-indigo-600" to={`/projects/${encodeURIComponent(id)}/chat`}>
                        project/{id}
                      </Link>
                    </li>
                  ))}
                  {(record.preview || []).map((row) => (
                    <li key={row.slug} className="font-mono text-xs text-stone-500">
                      preview {row.slug}
                    </li>
                  ))}
                </ul>
              </Card>
              <Card>
                <h3 className="mb-2 text-sm font-semibold">Visual bible / storyboard</h3>
                <p className="font-mono text-xs text-stone-500" data-testid="program-bible-ref">
                  {displayRelativePath(record.bible_ref)}
                </p>
                <p className="font-mono text-xs text-stone-500" data-testid="program-storyboard-ref">
                  {displayRelativePath(record.storyboard_ref)}
                </p>
                <p className="mt-1 text-xs text-stone-500">Lock visual_bible and storyboard chips above. Fail-closed still tags do not succeed. Dry-run writes no sheet files.</p>
              </Card>
              <Card>
                <h3 className="mb-2 text-sm font-semibold">NLE / finish</h3>
                <p className="mb-2 font-mono text-xs text-stone-500" data-testid="program-fused">
                  fused_request: {fused === null || fused === undefined ? "null" : String(fused)}
                </p>
                <p className="mb-2 font-mono text-xs text-stone-500">{displayRelativePath(record.sequence_ref)}</p>
                <div className="mb-2 flex flex-wrap gap-2" data-testid="program-cut-states">
                  {CUT_STATES.map((state) => (
                    <GhostButton
                      key={state}
                      type="button"
                      data-testid={`program-cut-${state}`}
                      disabled={busy}
                      onClick={() => void onFinish(state)}
                    >
                      {state}
                    </GhostButton>
                  ))}
                </div>
                <div className="flex flex-wrap gap-2">
                  <GhostButton type="button" data-testid="program-picture-lock" disabled={busy} onClick={() => void onFinish("picture_lock")}>
                    Picture lock
                  </GhostButton>
                  <GhostButton type="button" data-testid="program-finish-color" disabled={busy || !finishReady(locks)} onClick={() => void onFinish("color")}>
                    Color
                  </GhostButton>
                  <GhostButton type="button" data-testid="program-finish-mix" disabled={busy || !finishReady(locks)} onClick={() => void onFinish("mix")}>
                    Mix
                  </GhostButton>
                  <GhostButton type="button" data-testid="program-finish-graphics" disabled={busy || !finishReady(locks)} onClick={() => void onFinish("graphics")}>
                    Graphics
                  </GhostButton>
                </div>
              </Card>
              <Card>
                <h3 className="mb-2 text-sm font-semibold">Delivery</h3>
                <p className="font-mono text-xs text-stone-500" data-testid="program-delivery-ref">
                  {displayRelativePath(record.delivery_ref)}
                </p>
                <p className="font-mono text-xs text-stone-500" data-testid="program-delivery-spec">
                  {displayRelativePath(`${record.delivery_ref || "program/" + record.code + "/delivery/"}specifications.yaml`)}
                </p>
                <p className="mt-1 text-xs text-stone-500">No live upload. Trailer is not a silent spawn.</p>
              </Card>
            </>
          ) : null}
          {tab === "workflow" ? (
            <Card data-testid="program-workflow">
              <h3 className="mb-2 text-sm font-semibold">Program workflow</h3>
              <p className="mb-3 text-xs text-stone-500">
                Host-mediated. First hop {PROGRAM_FIRST_AGENT_HOP}. First-called {PROGRAM_FIRST_CALLED}. Default layout Force on Project Workflow stays unchanged for children.
              </p>
              <ol className="grid gap-2 text-sm">
                {workflowNodes.map((node, index) => (
                  <li key={node} className="rounded-lg border border-stone-200 px-3 py-2 font-mono text-xs dark:border-stone-700">
                    {index + 1}. {node}
                  </li>
                ))}
              </ol>
            </Card>
          ) : null}
          {tab === "chat" ? (
            <Card data-testid="program-chat">
              <h3 className="mb-2 text-sm font-semibold">Program Chat hops</h3>
              <p className="mb-3 text-xs text-stone-500">
                live: false. Child five human locks stay on Project Chat: promptengineer, director, cinematographer, mua_makeup, continuity.
              </p>
              <ol className="grid gap-2">
                {hops.map((hop) => (
                  <li key={hop.id} className="rounded-xl border border-stone-200 p-3 text-sm dark:border-stone-700" data-testid={`program-hop-${hop.id}`}>
                    <p className="font-mono text-xs text-stone-500">
                      {hop.from} → {hop.to} · {hop.kind}
                    </p>
                    <p className="mt-1">{hop.text}</p>
                  </li>
                ))}
              </ol>
            </Card>
          ) : null}
        </div>
      ) : null}
    </div>
  );
}
