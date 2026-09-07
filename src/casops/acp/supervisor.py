"""On-demand one grok (or fake ACP) process per agent_id."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from casops.acp.client import StdioAcpClient
from casops.acp.debug import AcpProcessLog
from casops.acp.project import acp_home, project_agent
from casops.compose.folders import locate_agent_folder
from casops.contracts.canonical import sha256_json
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

ADAPTERS = ("host_llm", "grok_acp")


def grok_binary() -> str | None:
    override = os.environ.get("CASOPS_GROK_BIN", "").strip()
    if override:
        return override
    return shutil.which("grok")


def resolve_chat_adapter(settings_adapter: str | None = None, *, profile_ready: bool = False) -> str:
    env = os.environ.get("CASOPS_CHAT_ADAPTER", "").strip().lower()
    if env in ADAPTERS:
        return env
    chosen = (settings_adapter or "").strip().lower()
    if chosen in ADAPTERS:
        return chosen
    if profile_ready and grok_binary():
        return "grok_acp"
    return "host_llm"


def _command_for(profile: Path, home: Path) -> list[str]:
    raw = os.environ.get("CASOPS_ACP_COMMAND", "").strip()
    if raw:
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            parsed = None
        if isinstance(parsed, list) and all(isinstance(item, str) for item in parsed):
            return list(parsed)
        return [sys.executable, raw] if raw.endswith(".py") else raw.split()
    grok = grok_binary()
    if not grok:
        raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="grok binary not found")
    return [
        grok,
        "agent",
        "--no-leader",
        "--always-approve",
        "--agent-profile",
        str(profile),
        "stdio",
    ]


@dataclass
class AcpHandle:
    agent_id: str
    home: Path
    profile: Path
    proc: subprocess.Popen[str]
    client: StdioAcpClient
    debug: AcpProcessLog | None = None
    session_id: str | None = None
    primed: bool = False


@dataclass
class AcpSupervisor:
    agents_root: Path
    home_root: Path
    handles: dict[str, AcpHandle] = field(default_factory=dict)

    def project(self, agent_id: str) -> dict[str, Any]:
        folder = locate_agent_folder(self.agents_root, agent_id)
        if folder is None:
            raise CasopsError(ErrorCode.INH_PARENT_MISSING)
        return project_agent(folder, home_root=self.home_root)

    def profile_ready(self, agent_id: str) -> bool:
        profile = acp_home(self.home_root, agent_id) / "profile.md"
        return profile.is_file()

    def ensure(self, agent_id: str) -> AcpHandle:
        existing = self.handles.get(agent_id)
        if existing and existing.proc.poll() is None:
            return existing
        folder = locate_agent_folder(self.agents_root, agent_id)
        if folder is None:
            raise CasopsError(ErrorCode.INH_PARENT_MISSING)
        projected = project_agent(folder, home_root=self.home_root)
        profile = Path(projected["profile"])
        home = Path(projected["home"])
        grok_home = home / "grok-home"
        grok_home.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["GROK_HOME"] = str(grok_home)
        env["GROK_SUBAGENTS"] = "0"
        command = _command_for(profile, home)
        debug = AcpProcessLog(agent_id)
        debug.event(
            "spawn",
            profile=str(profile),
            cwd=str(folder.resolve()),
            grok_home=str(grok_home),
            command=command,
        )
        proc = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            cwd=str(folder.resolve()),
            env=env,
        )
        debug.event("spawned", pid=proc.pid)
        debug.attach_stderr(proc)
        client = StdioAcpClient(proc, debug=debug.event)
        try:
            client.initialize(agent_id=agent_id)
            session_id = client.session_new(cwd=str(folder.resolve()), agent_id=agent_id, task_id=agent_id)
        except Exception as exc:
            debug.event("initialize_failed", error=str(exc))
            client.close()
            debug.close()
            raise
        debug.event("session", session_id=session_id, pid=proc.pid)
        handle = AcpHandle(
            agent_id=agent_id,
            home=home,
            profile=profile,
            proc=proc,
            client=client,
            debug=debug,
            session_id=session_id,
            primed=False,
        )
        self.handles[agent_id] = handle
        return handle

    def chat(
        self,
        agent_id: str,
        *,
        message: str,
        system: str,
        history: list[dict[str, str]],
        task_id: str,
    ) -> dict[str, Any]:
        handle = self.ensure(agent_id)
        session_id = handle.session_id
        if not session_id:
            raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="ACP session missing")
        if handle.primed:
            prompt_text = message
        else:
            parts: list[str] = []
            if system.strip():
                parts.append(system.strip())
            if history:
                parts.append("## Conversation")
                for turn in history:
                    label = "Operator" if turn.get("role") == "user" else "Agent"
                    parts.append(f"{label}: {turn.get('content', '')}")
            parts.append("## Operator message")
            parts.append(message)
            prompt_text = "\n\n".join(parts)
            handle.primed = True
        result = handle.client.prompt(session_id, prompt_text, casops={"agent_id": agent_id, "task_id": task_id})
        result["adapter"] = "grok_acp"
        result["pid"] = handle.proc.pid
        result["session_id"] = session_id
        result["digest"] = sha256_json({"agent_id": agent_id, "text": result.get("text"), "session_id": session_id})
        return result

    def adapter_view(self, agent_id: str, *, selected: str) -> dict[str, Any]:
        handle = self.handles.get(agent_id)
        alive = bool(handle and handle.proc.poll() is None)
        return {
            "agent_id": agent_id,
            "kind": selected,
            "grok_available": bool(grok_binary()),
            "profile_ready": self.profile_ready(agent_id),
            "pid": handle.proc.pid if alive and handle else None,
            "session_id": handle.session_id if alive and handle else None,
            "healthy": alive,
            "home": str(acp_home(self.home_root, agent_id).as_posix()),
        }

    def stop(self, agent_id: str) -> None:
        handle = self.handles.pop(agent_id, None)
        if handle:
            if handle.debug:
                handle.debug.event("stop", pid=handle.proc.pid, session_id=handle.session_id)
            if handle.session_id:
                handle.client.session_close(handle.session_id)
            handle.client.close()
            if handle.debug:
                handle.debug.close()

    def stop_all(self) -> None:
        for agent_id in list(self.handles):
            self.stop(agent_id)
