"""ISSUE-0002 proof records for Chat and Run. Not an eval pass."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from casops.contracts.canonical import sha256_file, sha256_json

OBS_FILES = (
    "telemetry.json",
    "redaction.json",
    "sampling.json",
    "slo.json",
    "evidence_graph.schema.json",
    "decision_record.schema.json",
)


def _json_dict(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def observability_view(folder: Path) -> dict[str, Any]:
    root = folder / "observability"
    present = {name: (root / name).is_file() for name in OBS_FILES}
    telemetry = _json_dict(root / "telemetry.json")
    redaction = _json_dict(root / "redaction.json")
    sampling = _json_dict(root / "sampling.json")
    return {
        "status": "NOT_APPLIED",
        "reason": "Chat/Run do not load observability/*.json; OTLP exporter is not wired.",
        "files_present": present,
        "exporter_declared": telemetry.get("exporter"),
        "exporter_wired": False,
        "content_capture": telemetry.get("content_capture") or "metadata_only",
        "redaction_mode": redaction.get("mode") or "metadata_only",
        "tail_sampling": bool(sampling.get("tail_sampling")),
        "mandatory_retention": bool(sampling.get("mandatory_retention")),
    }


def _prompt_digest(folder: Path, reference: str) -> str | None:
    path = folder / reference
    if not path.is_file():
        return None
    return sha256_file(path)


def _io_binding(
    *,
    message: str,
    history: list[dict[str, str]],
    io: dict[str, Any],
    packed: dict[str, Any],
    folder: Path,
    path_id: str,
) -> dict[str, Any]:
    public = packed.get("public") if isinstance(packed.get("public"), dict) else {}
    reference = str(public.get("prompt_reference") or packed.get("prompt_reference") or "")
    inputs = [str(item) for item in (io.get("inputs") or []) if str(item).strip()]
    outputs = [str(item) for item in (io.get("outputs") or []) if str(item).strip()]
    output_status = "not_applicable" if path_id == "chat" else "not_produced"
    output_reason = (
        "Chat emits reply text only; declared output buses are not written."
        if path_id == "chat"
        else "Run seals an artifact; declared output buses are not written."
    )
    return {
        "operator_message": {"status": "bound" if message.strip() else "missing", "chars": len(message or "")},
        "chat_history": {
            "status": "bound" if history else "empty",
            "turns": len(history),
        },
        "declared_inputs": [{"id": name, "status": "name_only", "fetched": False} for name in inputs],
        "declared_inputs_fetched": False,
        "declared_outputs": [
            {"id": name, "status": output_status, "applicable": False, "reason": output_reason} for name in outputs
        ],
        "prompt_file": {
            "reference": reference,
            "digest": _prompt_digest(folder, reference) if reference else None,
            "packed": True,
        },
        "system_tokens": public.get("system_tokens"),
        "system_digest": sha256_json({"system": packed.get("system") or ""}),
    }


def build_chat_proof(
    *,
    agent_id: str,
    folder: Path,
    spec: dict[str, Any],
    io: dict[str, Any],
    packed: dict[str, Any],
    completion: dict[str, Any],
    adapter: str,
    max_tokens: int,
    max_tokens_source: str,
    message: str,
    history: list[dict[str, str]],
) -> dict[str, Any]:
    policy = spec.get("model_policy") if isinstance(spec.get("model_policy"), dict) else {}
    binding = _io_binding(
        message=message,
        history=history,
        io=io,
        packed=packed,
        folder=folder,
        path_id="chat",
    )
    output = {
        "kind": "reply",
        "digest": completion.get("digest") or "",
        "finish_reason": completion.get("finish_reason") or "",
        "truncated": bool(completion.get("truncated")),
        "content_chars": int(completion.get("content_chars") or len(str(completion.get("text") or ""))),
        "declared_outputs_produced": False,
    }
    record = {
        "inputs": {
            "operator_message": True,
            "chat_history_turns": len(history),
            "declared_inputs_fetched": False,
            "prompt_reference": binding["prompt_file"]["reference"],
            "prompt_digest": binding["prompt_file"]["digest"],
        },
        "actions": ["pack_chat_context", "complete", "strip_chat_echo"],
        "constraints": [
            "no_memory_writes",
            "no_plugins",
            "no_t3",
            "no_network_grant",
            "no_dag_execute",
            "no_eval_pass",
        ],
        "codes": [],
        "outcomes": [{"kind": "chat_reply", "digest": output["digest"], "chars": output["content_chars"]}],
    }
    proof = {
        "path_id": "chat",
        "not_a_dag_run": True,
        "agent_id": agent_id,
        "eval": {
            "verdict": "NOT_RUN",
            "pass": False,
            "reason": "unqualified_instruments",
        },
        "io_binding": binding,
        "spec_applied": {
            "packed_system": True,
            "prompt_reference": binding["prompt_file"]["reference"],
            "profile_projected": adapter == "grok_acp",
            "dag_executed": False,
        },
        "model": {
            "adapter": adapter,
            "provider": str(completion.get("provider") or ""),
            "folder_model_policy_provider": str(policy.get("provider") or ""),
            "folder_model_policy_used_for_routing": False,
            "max_tokens": max_tokens,
            "max_tokens_source": max_tokens_source,
        },
        "output": output,
        "negative": {
            "memory_writes": [],
            "plugins_executed": False,
            "t3_enabled": False,
            "network_granted": False,
            "folder_network_access": bool(policy.get("network_access")),
        },
        "observability": observability_view(folder),
        "decision_record": record,
    }
    proof["digest"] = sha256_json(
        {key: proof[key] for key in ("path_id", "io_binding", "model", "output", "negative", "eval")}
    )
    return proof


def build_run_proof(
    *,
    agent_id: str,
    folder: Path,
    spec: dict[str, Any],
    io: dict[str, Any],
    node_ids: list[str],
    artifact: dict[str, Any],
    adapter: str,
    root_trace_id: str,
) -> dict[str, Any]:
    policy = spec.get("model_policy") if isinstance(spec.get("model_policy"), dict) else {}
    inputs = [str(item) for item in (io.get("inputs") or []) if str(item).strip()]
    outputs = [str(item) for item in (io.get("outputs") or []) if str(item).strip()]
    record = {
        "inputs": {
            "operator_message": False,
            "declared_inputs_fetched": False,
            "execution_json": True,
        },
        "actions": ["attest_run_start", "compile_dag", "execute_nodes", "seal_artifact"],
        "constraints": ["no_memory_writes", "no_plugins", "no_t3", "no_network_grant", "no_eval_pass"],
        "codes": [],
        "outcomes": [{"kind": "sealed_artifact", "id": artifact.get("id"), "digest": artifact.get("digest")}],
    }
    proof = {
        "path_id": "execute",
        "not_a_dag_run": False,
        "agent_id": agent_id,
        "eval": {"verdict": "NOT_RUN", "pass": False, "reason": "unqualified_instruments"},
        "io_binding": {
            "operator_message": {"status": "not_used", "chars": 0},
            "chat_history": {"status": "not_used", "turns": 0},
            "declared_inputs": [{"id": name, "status": "name_only", "fetched": False} for name in inputs],
            "declared_inputs_fetched": False,
            "declared_outputs": [
                {
                    "id": name,
                    "status": "not_produced",
                    "applicable": False,
                    "reason": "Run seals an artifact; declared output buses are not written.",
                }
                for name in outputs
            ],
        },
        "spec_applied": {
            "packed_system": True,
            "dag_executed": True,
            "node_ids": list(node_ids),
        },
        "model": {
            "adapter": adapter,
            "folder_model_policy_provider": str(policy.get("provider") or ""),
            "folder_model_policy_used_for_routing": False,
        },
        "output": {
            "kind": "sealed_artifact",
            "id": artifact.get("id"),
            "digest": artifact.get("digest"),
            "declared_outputs_produced": False,
        },
        "negative": {
            "memory_writes": [],
            "plugins_executed": False,
            "t3_enabled": False,
            "network_granted": False,
            "folder_network_access": bool(policy.get("network_access")),
        },
        "observability": observability_view(folder),
        "decision_record": record,
        "root_trace_id": root_trace_id,
    }
    proof["digest"] = sha256_json(
        {key: proof[key] for key in ("path_id", "io_binding", "output", "negative", "eval")}
    )
    return proof


def persist_proof(agent_id: str, proof: dict[str, Any]) -> str | None:
    path_id = str(proof.get("path_id") or "chat")
    digest = str(proof.get("digest") or sha256_json(proof))[:16]
    raw = os.environ.get("CASOPS_PROOF_ROOT", "").strip()
    root = Path(raw) if raw else Path.cwd() / "logs" / "proof"
    folder = root / path_id / agent_id
    try:
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / f"{digest}.json"
        path.write_text(json.dumps(proof, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except OSError:
        return None
    try:
        return path.resolve().relative_to(Path.cwd().resolve()).as_posix()
    except ValueError:
        return path.name
