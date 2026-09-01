import { useCallback, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { CasopsHttpError } from "../api/types";

export function useAgentId(): string {
  const { agentId } = useParams();
  return agentId ? decodeURIComponent(agentId) : "";
}

export function useAsync<T>(fn: () => Promise<T>, deps: unknown[]) {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<CasopsHttpError | Error | null>(null);
  const [loading, setLoading] = useState(true);
  const [asOf, setAsOf] = useState<Date | null>(null);

  const reload = useCallback(() => {
    let cancelled = false;
    setLoading(true);
    fn()
      .then((value) => {
        if (!cancelled) {
          setData(value);
          setError(null);
          setAsOf(new Date());
        }
      })
      .catch((err: unknown) => {
        if (!cancelled) {
          setError(err instanceof Error ? err : new Error(String(err)));
          setAsOf(new Date());
        }
      })
      .finally(() => {
        if (!cancelled) {
          setLoading(false);
        }
      });
    return () => {
      cancelled = true;
    };
  }, deps);

  useEffect(() => {
    return reload();
  }, [reload]);

  return { data, error, loading, asOf, reload, setData };
}
