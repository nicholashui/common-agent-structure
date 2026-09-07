"""Project CASOPS agent folders into var/acp/<id>/ Grok profiles."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from casops.acp.project import FIRST_SLICE_IDS, project_agent, write_binding
from casops.compose.folders import list_agent_ids, locate_agent_folder

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description="Project agent folders to Grok Build profiles")
    parser.add_argument("--agents-root", default=str(REPO / "agents"))
    parser.add_argument("--home-root", default=str(REPO / "var" / "acp"))
    parser.add_argument("--agent-id", action="append", dest="agent_ids")
    parser.add_argument("--first-slice", action="store_true")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--write-binding", action="store_true")
    args = parser.parse_args()
    agents_root = Path(args.agents_root)
    home_root = Path(args.home_root)
    ids = list(args.agent_ids or [])
    if args.all:
        ids = list_agent_ids(agents_root)
    elif args.first_slice or not ids:
        ids = list(FIRST_SLICE_IDS)
    rows = []
    for agent_id in ids:
        folder = locate_agent_folder(agents_root, agent_id)
        if folder is None:
            raise SystemExit(f"missing agent {agent_id}")
        if args.write_binding:
            write_binding(folder, agent_id)
        rows.append(project_agent(folder, home_root=home_root))
    print(json.dumps({"projected": rows}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
