import { FormEvent, useEffect, useState } from "react";
import { Link, useNavigate, useParams, useSearchParams } from "react-router-dom";
import { Card, Field, GhostButton, PrimaryButton, inputClass } from "../components/ui";
import { DryRunControl } from "../components/ActorStrip";
import { ErrorBanner } from "../components/RecoveryBanner";
import type { ProgramRecord, ProgramScene, ProgramSequencePayload } from "../api/types";
import { displayRelativePath } from "../lib/paths";
import {
  CUT_STATES,
  OVERVIEW_PANELS,
  PROGRAM_FIRST_AGENT_HOP,
  PROGRAM_FIRST_CALLED,
  PROGRAM_LOCK_LABELS,
  PROGRAM_LOCKS,
  PROGRAM_PHASES,
  type OverviewPanelId,
  resolveOverviewPanel,
  finishReady,
  generationListLockable,
  spawnMissingLocks,
  spawnReady,
} from "../lib/programs";
import { useSession } from "../state/session";

export function ProgramOverviewPage() {
  const params = useParams();
  const programId = params.programId ? decodeURIComponent(params.programId) : "";
  const session = useSession();
  const navigate = useNavigate();
  const [search, setSearch] = useSearchParams();
  const panel = resolveOverviewPanel(search.get("fn"));
  const current = OVERVIEW_PANELS.find((item) => item.id === panel) || OVERVIEW_PANELS[2];
  const [record, setRecord] = useState<ProgramRecord | null>(null);
  const [sequence, setSequence] = useState<ProgramSequencePayload | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const [busy, setBusy] = useState(false);
  const [sceneTitle, setSceneTitle] = useState("Scene 1");
  const [segmentPurpose, setSegmentPurpose] = useState("Opening beat");

  useEffect(() => {
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
      .getProgramSequence(programId)
      .then(setSequence)
      .catch(() => setSequence(null));
  }, [programId, session.client]);

  const locks = record?.locks || {};
  const canSpawn = spawnReady(locks);
  const missingSpawn = spawnMissingLocks(locks);
  const scenes: ProgramScene[] = record?.generation_list?.scenes || [];
  const fused = sequence?.compile?.fused_request ?? sequence?.sequence?.fused_request ?? null;
  const segmentCount = scenes.reduce((sum, scene) => sum + (scene.segments?.length || 0), 0);
  const childCount = (record?.project_ids || []).length;
  const phase = record?.phase || "w0";

  function openFn(id: OverviewPanelId) {
    setSearch({ fn: id }, { replace: true });
  }

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
    const next = scenes.concat([
      { id: `sc${scenes.length + 1}`, title: sceneTitle.trim() || `Scene ${scenes.length + 1}`, segments: [] },
    ]);
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
      setRecord({ ...(record || {}), ...result });
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setBusy(false);
    }
  }

  return (
    <div data-testid="program-overview">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <div>
          <h2 className="text-lg font-semibold text-stone-800 dark:text-stone-100">{record?.name || programId}</h2>
          <p className="text-xs text-stone-500">
            Overflow · {current.label} · {displayRelativePath(record?.folder) || `program/${programId}`} · {scenes.length}{" "}
            scene{scenes.length === 1 ? "" : "s"} · {segmentCount} segment{segmentCount === 1 ? "" : "s"} · {childCount}{" "}
            project{childCount === 1 ? "" : "s"} · CHARACTERIZATION
          </p>
          <p className="font-mono text-[11px] text-stone-400" data-testid="program-folder">
            {displayRelativePath(record?.folder)}
          </p>
          <p className="font-mono text-[11px] text-stone-400" data-testid="program-list-ref">
            {displayRelativePath(record?.generation_list_ref)}
          </p>
        </div>
        <div className="flex flex-wrap items-center gap-2">
          <DryRunControl />
          <GhostButton type="button" onClick={() => navigate(`/programs/${encodeURIComponent(programId)}/chat`)}>
            Chat
          </GhostButton>
          <GhostButton type="button" onClick={() => navigate(`/programs/${encodeURIComponent(programId)}/workflow`)}>
            Workflow
          </GhostButton>
        </div>
      </div>
      <nav
        className="mb-4 flex flex-wrap gap-2"
        aria-label="Overview functions"
        data-testid="program-overview-fns"
        role="tablist"
      >
        {OVERVIEW_PANELS.map((item) => {
          const on = panel === item.id;
          return (
            <button
              key={item.id}
              type="button"
              role="tab"
              id={`overview-tab-${item.id}`}
              aria-selected={on}
              aria-controls={`overview-panel-${item.id}`}
              data-testid={`program-overview-fn-${item.id}`}
              className={`rounded-full px-3 py-1 text-xs ${
                on
                  ? "bg-stone-900 text-white dark:bg-stone-100 dark:text-stone-900"
                  : "border border-stone-200 text-stone-600 dark:border-stone-700 dark:text-stone-300"
              }`}
              onClick={() => openFn(item.id)}
            >
              {item.label}
            </button>
          );
        })}
      </nav>
      <ErrorBanner error={error} />
      {!record && !error ? (
        <p className="text-sm text-stone-500">Loading overview…</p>
      ) : record ? (
        <div
          role="tabpanel"
          id={`overview-panel-${panel}`}
          aria-labelledby={`overview-tab-${panel}`}
          data-testid={`program-overview-panel-${panel}`}
        >
          {panel === "phase" ? (
            <Card>
              <div className="flex flex-wrap items-start justify-between gap-3">
                <div>
                  <h3 className="text-sm font-semibold text-stone-900 dark:text-stone-100">Phase</h3>
                  <p className="mt-1 text-[11px] text-stone-500">{current.blurb}</p>
                  <p className="mt-1 text-[11px] text-stone-500">
                    First hop <span className="font-mono">{record.first_agent_hop || PROGRAM_FIRST_AGENT_HOP}</span>
                    {" · "}
                    first-called <span className="font-mono">{record.first_called || PROGRAM_FIRST_CALLED}</span>.
                  </p>
                </div>
                <span className="rounded-full bg-indigo-50 px-2.5 py-0.5 font-mono text-[11px] font-semibold text-indigo-800 dark:bg-indigo-950 dark:text-indigo-200">
                  {phase.toUpperCase()}
                </span>
              </div>
              <ol className="mt-3 flex flex-wrap gap-1" data-testid="program-phase-strip">
                {PROGRAM_PHASES.map((item, index) => {
                  const active = phase === item.id;
                  const done = PROGRAM_PHASES.findIndex((row) => row.id === phase) > index;
                  return (
                    <li key={item.id}>
                      <button
                        type="button"
                        data-testid={`program-phase-${item.id}`}
                        disabled={busy}
                        onClick={() => void savePatch({ phase: item.id })}
                        className={`rounded-full px-3 py-1 text-[11px] ${
                          active
                            ? "bg-indigo-600 text-white"
                            : done
                              ? "bg-emerald-50 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-200"
                              : "border border-stone-200 text-stone-500 dark:border-stone-700"
                        }`}
                      >
                        {item.label.replace(/^W\d+\s/, "")}
                      </button>
                    </li>
                  );
                })}
              </ol>
            </Card>
          ) : null}

          {panel === "locks" ? (
            <Card>
              <h3 className="text-sm font-semibold text-stone-900 dark:text-stone-100">Locks</h3>
              <p className="mt-1 text-[11px] text-stone-500">{current.blurb}</p>
              <p className="mt-1 text-[11px] text-stone-500">Click to toggle. List lock needs every scene to have a segment.</p>
              <div className="mt-3 flex flex-wrap gap-2" data-testid="program-lock-chips">
                {PROGRAM_LOCKS.map((key) => {
                  const on = Boolean(locks[key]);
                  return (
                    <button
                      key={key}
                      type="button"
                      data-testid={`program-lock-${key}`}
                      aria-pressed={on}
                      disabled={busy || (key === "generation_list" && !on && !generationListLockable(scenes))}
                      onClick={() => void onToggleLock(key)}
                      className={`rounded-full px-3 py-1 text-[11px] ${
                        on
                          ? "bg-emerald-700 text-white"
                          : "border border-stone-200 text-stone-600 dark:border-stone-700 dark:text-stone-300"
                      }`}
                    >
                      {PROGRAM_LOCK_LABELS[key]}
                    </button>
                  );
                })}
              </div>
              {canSpawn ? (
                <GhostButton type="button" className="mt-4" onClick={() => openFn("spawn")}>
                  Open Spawn
                </GhostButton>
              ) : (
                <p className="mt-4 text-[11px] text-stone-500">
                  Spawn waits on: {missingSpawn.map((key) => PROGRAM_LOCK_LABELS[key as keyof typeof PROGRAM_LOCK_LABELS] || key).join(", ")}
                </p>
              )}
            </Card>
          ) : null}

          {panel === "list" ? (
            <Card>
              <div className="mb-3 flex flex-wrap items-baseline justify-between gap-2">
                <div>
                  <h3 className="text-sm font-semibold text-stone-900 dark:text-stone-100">Generation list</h3>
                  <p className="mt-1 text-[11px] text-stone-500">{current.blurb}</p>
                </div>
              </div>
              <div data-testid="program-generation-list" className="overflow-x-auto">
                {scenes.length === 0 ? (
                  <p className="text-sm text-stone-500">No scenes yet. Add a scene, then segments.</p>
                ) : (
                  <table className="w-full min-w-[36rem] border-collapse text-left text-sm">
                    <thead>
                      <tr className="border-b border-stone-200 text-[11px] uppercase tracking-wide text-stone-500 dark:border-stone-700">
                        <th className="py-2 pr-3 font-medium">Scene</th>
                        <th className="py-2 pr-3 font-medium">Segment</th>
                        <th className="py-2 pr-3 font-medium">Purpose</th>
                        <th className="py-2 pr-3 font-medium">s</th>
                        <th className="py-2 pr-3 font-medium">Status</th>
                        <th className="py-2 font-medium">Project</th>
                      </tr>
                    </thead>
                    <tbody>
                      {scenes.map((scene, sceneIndex) => {
                        const segs = scene.segments || [];
                        if (!segs.length) {
                          return (
                            <tr key={scene.id} data-testid={`program-scene-${scene.id}`} className="border-b border-stone-100 dark:border-stone-800">
                              <td className="py-2 pr-3 align-top">
                                <span className="font-mono text-[11px] text-stone-400">{scene.id}</span>
                                <div className="font-medium">{scene.title || scene.id}</div>
                              </td>
                              <td colSpan={5} className="py-2 text-xs text-amber-700">
                                No segments — list lock blocked
                                <GhostButton
                                  type="button"
                                  className="ml-2"
                                  data-testid={`program-add-segment-${scene.id}`}
                                  disabled={busy}
                                  onClick={() => void onAddSegment(sceneIndex)}
                                >
                                  Add segment
                                </GhostButton>
                              </td>
                            </tr>
                          );
                        }
                        return segs.map((segment, segIndex) => (
                          <tr
                            key={segment.id}
                            data-testid={`program-segment-${segment.id}`}
                            className="border-b border-stone-100 dark:border-stone-800"
                          >
                            {segIndex === 0 ? (
                              <td className="py-2 pr-3 align-top" rowSpan={segs.length} data-testid={`program-scene-${scene.id}`}>
                                <span className="font-mono text-[11px] text-stone-400">{scene.id}</span>
                                <div className="font-medium">{scene.title || scene.id}</div>
                                <GhostButton
                                  type="button"
                                  className="mt-1"
                                  data-testid={`program-add-segment-${scene.id}`}
                                  disabled={busy}
                                  onClick={() => void onAddSegment(sceneIndex)}
                                >
                                  Add segment
                                </GhostButton>
                              </td>
                            ) : null}
                            <td className="py-2 pr-3 font-mono text-[11px]">{segment.id}</td>
                            <td className="py-2 pr-3">{segment.purpose || "—"}</td>
                            <td className="py-2 pr-3 font-mono text-[11px]">{segment.duration_s ?? 6}</td>
                            <td className="py-2 pr-3 text-xs text-stone-500">{segment.status || "planned"}</td>
                            <td className="py-2">
                              {segment.project_slug ? (
                                <Link className="font-mono text-xs text-indigo-600" to={`/projects/${encodeURIComponent(segment.project_slug)}/chat`}>
                                  {segment.project_slug}
                                </Link>
                              ) : (
                                <span className="text-xs text-stone-400">—</span>
                              )}
                            </td>
                          </tr>
                        ));
                      })}
                    </tbody>
                  </table>
                )}
              </div>
              <form className="mt-4 flex flex-wrap items-end gap-2 border-t border-stone-100 pt-3 dark:border-stone-800" onSubmit={(event) => void onAddScene(event)}>
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
          ) : null}

          {panel === "spawn" ? (
            <Card>
              <h3 className="text-sm font-semibold text-stone-900 dark:text-stone-100">Spawn projects</h3>
              <p className="mt-1 text-[11px] text-stone-500">{current.blurb}</p>
              <p className="mt-1 text-[11px] text-stone-500" data-testid="program-spawn-hint">
                {canSpawn
                  ? "List and visual bible are locked. Spawn creates one Project per segment."
                  : `Missing locks: ${missingSpawn.map((key) => PROGRAM_LOCK_LABELS[key as keyof typeof PROGRAM_LOCK_LABELS] || key).join(", ")}`}
              </p>
              <div className="mt-3 flex flex-wrap gap-2">
                <PrimaryButton type="button" data-testid="program-spawn" disabled={busy || !canSpawn} onClick={() => void onSpawn()}>
                  Spawn projects
                </PrimaryButton>
                {!canSpawn ? (
                  <GhostButton type="button" onClick={() => openFn("locks")}>
                    Open Locks
                  </GhostButton>
                ) : null}
              </div>
              <ul className="mt-3 grid gap-1 text-sm" data-testid="program-children">
                {(record.project_ids || []).map((id) => (
                  <li key={id}>
                    <Link className="font-mono text-xs text-indigo-600" to={`/projects/${encodeURIComponent(id)}/chat`}>
                      project/{id}
                    </Link>
                  </li>
                ))}
                {(record.preview || []).map((row) => (
                  <li key={row.slug} className="font-mono text-[11px] text-stone-500">
                    preview {row.slug}
                  </li>
                ))}
                {(record.project_ids || []).length === 0 && (record.preview || []).length === 0 ? (
                  <li className="text-sm text-stone-500">No child projects yet.</li>
                ) : null}
              </ul>
            </Card>
          ) : null}

          {panel === "bible" ? (
            <Card>
              <h3 className="text-sm font-semibold text-stone-900 dark:text-stone-100">Bible / storyboard</h3>
              <p className="mt-1 text-[11px] text-stone-500">{current.blurb}</p>
              <p className="mt-3 font-mono text-[11px] text-stone-500" data-testid="program-bible-ref">
                {displayRelativePath(record.bible_ref)}
              </p>
              <p className="font-mono text-[11px] text-stone-500" data-testid="program-storyboard-ref">
                {displayRelativePath(record.storyboard_ref)}
              </p>
              <p className="mt-2 text-[11px] text-stone-500">Fail-closed still tags do not succeed.</p>
              <p className="mt-2 text-[11px] text-stone-500">
                Visual bible {locks.visual_bible ? "locked" : "open"} · Storyboard {locks.storyboard ? "locked" : "open"}
              </p>
              <GhostButton type="button" className="mt-3" onClick={() => openFn("locks")}>
                Open Locks
              </GhostButton>
            </Card>
          ) : null}

          {panel === "cut" ? (
            <Card>
              <h3 className="text-sm font-semibold text-stone-900 dark:text-stone-100">Cut / finish</h3>
              <p className="mt-1 text-[11px] text-stone-500">{current.blurb}</p>
              <p className="mt-2 font-mono text-[11px] text-stone-500" data-testid="program-fused">
                fused_request: {fused === null || fused === undefined ? "null" : String(fused)}
              </p>
              <p className="font-mono text-[11px] text-stone-500">{displayRelativePath(record.sequence_ref)}</p>
              <div className="mt-3 flex flex-wrap gap-2" data-testid="program-cut-states">
                {CUT_STATES.map((state) => (
                  <GhostButton key={state} type="button" data-testid={`program-cut-${state}`} disabled={busy} onClick={() => void onFinish(state)}>
                    {state.replace("_", " ")}
                  </GhostButton>
                ))}
              </div>
              <div className="mt-2 flex flex-wrap gap-2">
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
          ) : null}

          {panel === "delivery" ? (
            <Card>
              <h3 className="text-sm font-semibold text-stone-900 dark:text-stone-100">Delivery</h3>
              <p className="mt-1 text-[11px] text-stone-500">{current.blurb}</p>
              <p className="mt-3 font-mono text-[11px] text-stone-500" data-testid="program-delivery-ref">
                {displayRelativePath(record.delivery_ref)}
              </p>
              <p className="font-mono text-[11px] text-stone-500" data-testid="program-delivery-spec">
                {displayRelativePath(`${record.delivery_ref || "program/" + record.code + "/delivery/"}specifications.yaml`)}
              </p>
              <p className="mt-2 text-[11px] text-stone-500">Delivery lock {locks.delivery ? "on" : "off"}.</p>
            </Card>
          ) : null}
        </div>
      ) : null}
    </div>
  );
}
