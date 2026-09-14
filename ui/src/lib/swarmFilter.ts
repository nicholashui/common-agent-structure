import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { useSession } from "../state/session";

export function useSwarmRoster(): { swarmId: string; roster: string[] | null } {
  const [search] = useSearchParams();
  const swarmId = search.get("swarm") || "";
  const session = useSession();
  const [roster, setRoster] = useState<string[] | null>(null);
  useEffect(() => {
    if (!swarmId) {
      setRoster(null);
      return;
    }
    let cancelled = false;
    session.client
      .getSwarm(swarmId)
      .then((payload) => {
        if (!cancelled) {
          setRoster(rosterAfterFetch(true, payload.member_ids));
        }
      })
      .catch(() => {
        if (!cancelled) {
          setRoster(rosterAfterFetch(false));
        }
      });
    return () => {
      cancelled = true;
    };
  }, [swarmId, session.client]);
  return { swarmId, roster };
}

export function swarmIdFromSearch(search: string): string {
  try {
    return new URLSearchParams(search.startsWith("?") ? search.slice(1) : search).get("swarm") || "";
  } catch {
    return "";
  }
}

export function rosterAfterFetch(ok: boolean, memberIds?: string[]): string[] | null {
  if (!ok) {
    return null;
  }
  return memberIds || [];
}

export function filterByRoster<T extends { agent_id?: string }>(rows: T[], roster: string[] | null): T[] {
  if (!roster) {
    return rows;
  }
  const allowed = new Set(roster);
  return rows.filter((row) => allowed.has(String(row.agent_id || "")));
}

export function withSwarmQuery(path: string, swarmId: string): string {
  if (!swarmId) {
    return path;
  }
  const join = path.includes("?") ? "&" : "?";
  return `${path}${join}swarm=${encodeURIComponent(swarmId)}`;
}
