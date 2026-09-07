"""Operator CLI: packaged chat vs folder workshop. Does not rewrite corrigibility."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

from casops.acp.project import project_agent
from casops.acp.supervisor import grok_binary
from casops.compose.folders import locate_agent_folder

REPO = Path(__file__).resolve().parents[1]


def _folder(agents_root: Path, agent_id: str) -> Path:
    folder = locate_agent_folder(agents_root, agent_id)
    if folder is None:
        raise SystemExit(f"missing agent {agent_id}")
    return folder


def _grok() -> str:
    path = grok_binary()
    if not path:
        raise SystemExit("grok binary not found")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Talk to or improve a CASOPS agent folder via grok")
    parser.add_argument("mode", choices=("chat", "prompt", "workshop"))
    parser.add_argument("agent_id")
    parser.add_argument("-p", "--prompt", dest="prompt_text", default="")
    parser.add_argument("--agents-root", default=str(REPO / "agents"))
    parser.add_argument("--home-root", default=str(REPO / "var" / "acp"))
    args = parser.parse_args()
    agents_root = Path(args.agents_root)
    folder = _folder(agents_root, args.agent_id)
    grok = _grok()
    cwd = str(folder.resolve())
    if args.mode == "workshop":
        cmd = [
            grok,
            "--cwd",
            cwd,
            "--deny",
            "Write(corrigibility/**)",
            "--deny",
            "Edit(corrigibility/**)",
        ]
        print("workshop: folder is source of truth; corrigibility stays host-owned", file=sys.stderr)
        return subprocess.call(cmd)
    projected = project_agent(folder, home_root=Path(args.home_root))
    profile = projected["profile"]
    env = os.environ.copy()
    env["GROK_HOME"] = str(Path(projected["home"]) / "grok-home")
    env["GROK_SUBAGENTS"] = "0"
    if args.mode == "prompt":
        if not args.prompt_text.strip():
            raise SystemExit("prompt mode requires -p")
        cmd = [
            grok,
            "-p",
            args.prompt_text,
            "--cwd",
            cwd,
            "--agent-profile",
            profile,
        ]
        return subprocess.call(cmd, env=env)
    cmd = [grok, "--cwd", cwd, "--agent-profile", profile]
    return subprocess.call(cmd, env=env)


if __name__ == "__main__":
    raise SystemExit(main())
