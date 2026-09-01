import { ErrorBanner } from "../components/RecoveryBanner";
import { StatusPill } from "../components/StatusPill";
import { Card, JsonWell, PageHeader } from "../components/ui";
import { useAgentId, useAsync } from "../lib/hooks";
import { pillForValidation, validationIsPass } from "../lib/honesty";
import { pretty } from "../lib/json";
import { useSession } from "../state/session";

export function ValidationPage() {
  const agentId = useAgentId();
  const session = useSession();
  const { data, error, asOf } = useAsync(async () => {
    const [report, suite] = await Promise.all([
      session.client.getValidationReport(agentId),
      session.client.getRegressionSuite(agentId),
    ]);
    return { report, suite };
  }, [session.client, agentId]);
  const report = data?.report;
  const pass = validationIsPass(report ?? null);
  const indicative = report?.verdict === "INDICATIVE" || report?.honesty === "INDICATIVE";
  const notRun = report?.verdict === "NOT_RUN" || report?.pass === false;

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
        <h2 className="mb-3 text-sm font-semibold">Regression suite</h2>
        <ul className="text-sm text-stone-700">
          {(data?.suite.fixtures ?? []).map((name) => (
            <li key={name} className="font-mono text-xs">
              {name}
            </li>
          ))}
        </ul>
        <p className="mt-3 text-xs text-stone-500">CLI remains casops-eval. See user_guide.v1.md §13.</p>
      </Card>
    </div>
  );
}
