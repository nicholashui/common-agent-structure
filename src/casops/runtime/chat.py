"""Operator chat: pack identity + operational prompt under context.json budgets."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from casops.compose.skills import resolve_skills
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

_MAX_HISTORY = 20
_MAX_MESSAGE_CHARS = 32_000
_DEFAULT_SEGMENTS = {
    "policy": 512,
    "task": 768,
    "memory": 0,
    "tools": 0,
    "evidence": 256,
    "output": 512,
}
_PROMPT_STOP = (
    "## Developer",
    "## Task",
    "## Output schema",
    "## Output",
    "## Tests",
    "## Harness",
    "## Research patterns",
    "## Bindings",
    "## Self-evaluation loop",
    "## Refine policy",
    "## Collaboration",
    "## Tools",
)
_HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)


def normalize_history(raw: Any) -> list[dict[str, str]]:
    if not isinstance(raw, list):
        return []
    turns: list[dict[str, str]] = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        role = str(item.get("role") or "").strip().lower()
        content = str(item.get("content") or "").strip()
        if role not in {"user", "assistant"} or not content:
            continue
        turns.append({"role": role, "content": content})
    return turns[-_MAX_HISTORY:]


def require_message(message: str) -> str:
    text = (message or "").strip()
    if not text:
        raise CasopsError(ErrorCode.CTX_BUDGET, detail="chat message required")
    if len(text) > _MAX_MESSAGE_CHARS:
        raise CasopsError(ErrorCode.CTX_BUDGET, detail="chat message exceeds context budget")
    return text


def load_prompt(folder: Path, spec: dict[str, Any]) -> tuple[str, str]:
    ref = str(spec.get("prompt_reference") or "prompts/primary.md")
    candidate = folder / ref
    if candidate.is_file():
        return candidate.read_text(encoding="utf-8"), ref
    primary = folder / "prompts" / "primary.md"
    if primary.is_file():
        return primary.read_text(encoding="utf-8"), "prompts/primary.md"
    return "", ref


def build_chat_system(*, prompt: str, io: dict[str, Any]) -> str:
    parts: list[str] = []
    if prompt.strip():
        parts.append(prompt.strip())
    inputs = io.get("inputs") if isinstance(io.get("inputs"), list) else []
    outputs = io.get("outputs") if isinstance(io.get("outputs"), list) else []
    parts.append("## Declared input requirements")
    parts.append(", ".join(str(item) for item in inputs) if inputs else "(none declared)")
    parts.append("## Declared output requirements")
    parts.append(", ".join(str(item) for item in outputs) if outputs else "(none declared)")
    parts.append("## Human operator")
    parts.append(
        "The operator may send free-text chat messages. Treat the latest operator message as your input "
        "and reply in natural language. Do not require peer-agent critique payloads unless the operator provides them."
    )
    return "\n\n".join(parts)


def build_chat_prompt(
    *,
    system: str,
    io: dict[str, Any],
    history: list[dict[str, str]],
    message: str,
) -> str:
    parts = [build_chat_system(prompt=system, io=io)]
    if history:
        parts.append("## Conversation")
        for turn in history:
            label = "Operator" if turn.get("role") == "user" else "Agent"
            parts.append(f"{label}: {turn.get('content', '')}")
    parts.append("## Operator message")
    parts.append(message)
    return "\n\n".join(parts)


def estimate_tokens(text: str) -> int:
    if not text:
        return 0
    return max(1, (len(text) + 3) // 4)


def clip_to_tokens(text: str, budget: int) -> tuple[str, bool]:
    stripped = (text or "").strip()
    if budget <= 0:
        return "", bool(stripped)
    if estimate_tokens(stripped) <= budget:
        return stripped, False
    limit = max(0, budget * 4)
    cut = stripped[:limit]
    if "\n" in cut:
        cut = cut.rsplit("\n", 1)[0]
    return cut.rstrip(), True


def load_context_budget(folder: Path) -> dict[str, Any]:
    path = folder / "runtime" / "context.json"
    payload: dict[str, Any] = {}
    if path.is_file():
        try:
            loaded = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(loaded, dict):
                payload = loaded
        except (OSError, json.JSONDecodeError):
            payload = {}
    raw = payload.get("segments") if isinstance(payload.get("segments"), dict) else {}
    segments = dict(_DEFAULT_SEGMENTS)
    for key, default in _DEFAULT_SEGMENTS.items():
        value = raw.get(key)
        if isinstance(value, int) and value >= 0:
            segments[key] = value
    compaction = str(payload.get("compaction") or "disabled")
    return {"segments": segments, "compaction": compaction}


def operational_prompt(raw: str) -> str:
    text = _HTML_COMMENT.sub("", raw or "").strip()
    if not text:
        return ""
    prefixed = "\n" + text
    system_at = prefixed.find("\n## System")
    if system_at >= 0:
        text = prefixed[system_at + 1 :].strip()
    elif "## Identity" in text or "## Responsibility" in text:
        kept: list[str] = []
        seen_section = False
        for line in text.splitlines():
            if line.startswith("### Domain distillation"):
                break
            if line.startswith("## ") and line not in {"## Identity", "## Responsibility"}:
                if seen_section:
                    break
            if line.startswith("## Identity") or line.startswith("## Responsibility"):
                seen_section = True
            kept.append(line)
            if sum(len(item) for item in kept) > 2400:
                break
        text = "\n".join(kept).strip()
    stop_at = len(text)
    for heading in _PROMPT_STOP:
        found = text.find("\n" + heading)
        if found > 0:
            stop_at = min(stop_at, found)
    return text[:stop_at].strip()


def _json_dict(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def _skill_description(folder: Path) -> str:
    path = folder / "skills" / "SKILL.md"
    if not path.is_file():
        return ""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return ""
    if not text.startswith("---"):
        first = text.strip().splitlines()[:1]
        return first[0][:200] if first else ""
    end = text.find("\n---", 3)
    block = text[3:end] if end > 0 else ""
    for line in block.splitlines():
        if line.lower().startswith("description:"):
            return line.split(":", 1)[1].strip()[:240]
    return ""


def _enabled_skills(folder: Path) -> list[dict[str, str]]:
    resolved = resolve_skills([folder])
    rows: list[dict[str, str]] = []
    description = _skill_description(folder)
    for item in resolved.get("enabled") or []:
        skill_id = str(item.get("skill_id") or "").strip()
        if not skill_id:
            continue
        rows.append({"skill_id": skill_id, "description": description})
    return rows


def _policy_text(folder: Path, spec: dict[str, Any], skills: list[dict[str, str]]) -> str:
    persona = _json_dict(folder / "identity" / "persona.json")
    role = str(spec.get("role") or spec.get("agent_id") or "").strip()
    agent_id = str(spec.get("agent_id") or "").strip()
    voice = str(persona.get("voice") or "neutral").strip()
    owns = spec.get("does_not_own") if isinstance(spec.get("does_not_own"), list) else []
    denied = [str(item).strip() for item in owns if str(item).strip()][:8]
    skill_line = ", ".join(item["skill_id"] for item in skills) if skills else "(none enabled — do not load SKILL.md)"
    parts = [
        f"You are {role} (`{agent_id}`)." if role else f"You are `{agent_id}`.",
        f"Voice: {voice}.",
        "Does not own: " + "; ".join(denied) if denied else "Does not own: host credentials, production activation, other agents' exclusive outputs.",
        f"Enabled skills: {skill_line}.",
        "Host chat: treat the latest operator message as free-text input and reply in natural language. "
        "Do not require peer-agent critique payloads unless the operator provides them. "
        "Do not call tools, write memory, enable T3, or request network.",
    ]
    return "\n".join(parts)


def _evidence_text(io: dict[str, Any]) -> str:
    inputs = io.get("inputs") if isinstance(io.get("inputs"), list) else []
    outputs = io.get("outputs") if isinstance(io.get("outputs"), list) else []
    return (
        "Peer buses are optional in operator chat.\n"
        f"Inputs: {', '.join(str(item) for item in inputs) if inputs else '(none)'}\n"
        f"Outputs: {', '.join(str(item) for item in outputs) if outputs else '(none)'}"
    )


def _output_text(folder: Path, spec: dict[str, Any], prompt: str) -> str:
    at = prompt.find("## Output schema")
    if at >= 0:
        return prompt[at : at + 1200].strip()
    ref = str(spec.get("rubric_reference") or "rubrics/primary.md")
    path = folder / ref
    if path.is_file():
        try:
            return path.read_text(encoding="utf-8")[:1200].strip()
        except OSError:
            return ""
    return ""


def _segment(name: str, text: str, budget: int) -> dict[str, Any]:
    clipped_text, clipped = clip_to_tokens(text, budget)
    return {
        "name": name,
        "budget": budget,
        "tokens": estimate_tokens(clipped_text),
        "clipped": clipped,
        "included": bool(clipped_text),
        "text": clipped_text,
    }


def pack_chat_context(
    folder: Path,
    spec: dict[str, Any],
    io: dict[str, Any],
    *,
    message: str,
    history: list[dict[str, str]],
) -> dict[str, Any]:
    budget = load_context_budget(folder)
    segments_budget: dict[str, int] = budget["segments"]
    prompt, prompt_ref = load_prompt(folder, spec)
    skills = _enabled_skills(folder)
    omitted: list[str] = []
    if not skills:
        omitted.append("skills/SKILL.md")
    if segments_budget.get("memory", 0) <= 0:
        omitted.append("memory")
    if segments_budget.get("tools", 0) <= 0:
        omitted.append("tools")
    omitted.append("prompts/primary.md#Developer")
    policy = _segment("policy", _policy_text(folder, spec, skills), segments_budget["policy"])
    task = _segment("task", operational_prompt(prompt), segments_budget["task"])
    memory = _segment("memory", "", segments_budget["memory"])
    tools = _segment("tools", "", segments_budget["tools"])
    evidence = _segment("evidence", _evidence_text(io), segments_budget["evidence"])
    output = _segment("output", _output_text(folder, spec, prompt), segments_budget["output"])
    packed = [policy, task, evidence, output]
    system_parts = [item["text"] for item in packed if item["text"]]
    system = "\n\n".join(system_parts)
    max_input = spec.get("budget_policy") if isinstance(spec.get("budget_policy"), dict) else {}
    max_input_tokens = max_input.get("max_input_tokens")
    if not isinstance(max_input_tokens, int) or max_input_tokens < 64:
        max_input_tokens = 2048
    kept_history = list(history)
    history_clipped = False
    message_tokens = estimate_tokens(message)
    while kept_history and estimate_tokens(system) + message_tokens + sum(
        estimate_tokens(turn["content"]) for turn in kept_history
    ) > max_input_tokens:
        kept_history.pop(0)
        history_clipped = True
    public_segments = [
        {key: item[key] for key in ("name", "budget", "tokens", "clipped", "included")}
        for item in (policy, task, memory, tools, evidence, output)
    ]
    return {
        "system": system,
        "history": kept_history,
        "message": message,
        "public": {
            "tokenizer": "chars_div_4",
            "compaction": budget["compaction"],
            "max_input_tokens": max_input_tokens,
            "prompt_reference": prompt_ref,
            "skills": skills,
            "omitted": omitted,
            "segments": public_segments,
            "history_turns": len(kept_history),
            "history_clipped": history_clipped,
            "system_tokens": estimate_tokens(system),
        },
    }
