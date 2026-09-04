import { Link } from "react-router-dom";
import { CharacterizationBadge } from "../components/EvalFixtures";
import { ErrorBanner } from "../components/RecoveryBanner";
import { StatusPill } from "../components/StatusPill";
import { Card, GhostButton, JsonWell, PageHeader } from "../components/ui";
import { chatFixtureHref, clipPreview, fixtureMessage, fixtureTitle, runTabHref } from "../lib/fixtures";
import { useAgentId, useAsync } from "../lib/hooks";
import { pillForValidation, validationIsPass } from "../lib/honesty";
import { pretty } from "../lib/json";
import { useSession } from "../state/session";

export function ValidationPage() {
  const agentId = useAgentId();
  const session = useSession();
  const { data, error, asOf } = useAsync(async () => {
    const [report, suite, evals] = await Promise.all([
      session.client.getValidationReport(agentId),
      session.client.getRegressionSuite(agentId),
      session.client.getEvalFixtures(agentId),
    ]);
    return { report, suite, evals };
  }, [session.client, agentId]);
  const report = data?.report;
  const pass = validationIsPass(report ?? null);
  const indicative = report?.verdict === "INDICATIVE" || report?.honesty === "INDICATIVE";
  const notRun = report?.verdict === "NOT_RUN" || report?.pass === false;
  const cases = data?.evals.fixtures ?? [];

  return (
    <div>
      <PageHeader title="Validation" asOf={asOf} />
      <ErrorBanner error={error} />
      {report ? (
        <Card className={pass ? "border-emerald-200" : "border-amber-200 bg-stone-50 hover:shadow-none"}>
          <div className="mb-3 flex flex-wrap items-center gap-2">
            <StatusPill status={pillForValidation(report)} />
            {indicative ? (
              <span className="rounded-full bg-violet-50 border border-violet-200 px-2.5 py-1 text-xs text-violet-700">
                Screening — not a release pass
              </span>
            ) : null}
          </div>
          <p className="font-mono text-sm text-stone-800">{report.verdict}</p>
          <p className="mt-2 text-sm text-stone-700">{report.reason}</p>
          {notRun && !pass ? (
            <p className="mt-3 text-sm text-stone-600">This is not a green pass. Unqualified instruments cannot gate or pass (IQ-01).</p>
          ) : null}
          {report.instruments?.length ? (
            <ul className="mt-3 list-disc pl-5 text-sm text-stone-600">
              {report.instruments.map((item) => (
                <li key={item} className="font-mono text-xs">
                  {item}
                </li>
              ))}
            </ul>
          ) : null}
          <div className="mt-4">
            <JsonWell value={pretty(report)} />
          </div>
        </Card>
      ) : null}
      <Card className="mt-5">
        <div className="mb-3 flex flex-wrap items-center gap-2" data-testid="validation-characterization">
          <h2 className="text-sm font-semibold">Characterization cases</h2>
          <CharacterizationBadge />
        </div>
        <p className="mb-3 text-sm text-stone-600">
          {data?.evals.note ||
            "Fixtures are CHARACTERIZATION / policy checks. Not an eval pass. casops-eval remains NOT_RUN while instruments are unqualified."}
        </p>
        {cases.length ? (
          <ul className="space-y-3">
            {cases.map((item) => {
              const message = fixtureMessage(item);
              const chat = item.path === "chat" && message;
              return (
                <li
                  key={item.filename || item.id}
                  className="rounded-xl border border-stone-200 bg-stone-50 p-3"
                  data-testid="validation-case"
                >
                  <div className="flex flex-wrap items-center gap-2">
                    <span className="font-mono text-xs text-stone-800">{item.id}</span>
                    <span className="rounded-full border border-stone-200 bg-white px-2 py-0.5 font-mono text-[10px] text-stone-500">
                      {item.path}
                    </span>
                    <span className="rounded-full border border-amber-200 bg-amber-50 px-2 py-0.5 text-[10px] text-amber-800">
                      {item.honesty || "CHARACTERIZATION"}
                    </span>
                  </div>
                  <p className="mt-2 text-sm font-medium text-stone-800">{fixtureTitle(item)}</p>
                  {message ? <p className="mt-1 text-sm text-stone-600">{clipPreview(message, 180)}</p> : null}
                  {!message && item.path === "run" ? (
                    <p className="mt-1 text-sm text-stone-500">Sealed Runtime.execute. No operator Chat message.</p>
                  ) : null}
                  <div className="mt-3 flex flex-wrap gap-2">
                    {chat ? (
                      <Link to={chatFixtureHref(agentId, item.id)}>
                        <GhostButton type="button">Load in Chat</GhostButton>
                      </Link>
                    ) : null}
                    {item.path === "run" ? (
                      <Link to={runTabHref(agentId)}>
                        <GhostButton type="button">Open Run</GhostButton>
                      </Link>
                    ) : null}
                  </div>
                </li>
              );
            })}
          </ul>
        ) : (
          <p className="text-sm text-stone-500">No characterization fixtures on disk for this agent.</p>
        )}
      </Card>
      <Card className="mt-5">
        <h2 className="mb-3 text-sm font-semibold">Regression suite</h2>
        <ul className="text-sm text-stone-700">
          {(data?.suite.fixtures ?? []).map((name) => (
            <li key={name} className="font-mono text-xs">
              {name}
            </li>
          ))}
        </ul>
        <p className="mt-3 text-xs text-stone-500">
          This list is filenames under evals/regression/, not evals/fixtures/. CLI remains casops-eval. See
          user_guide.v1.md §13.
        </p>
      </Card>
    </div>
  );
}
