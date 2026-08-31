"""Write ADR-001..013 from the Phase 1 planning defaults."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs" / "adr"

ADRS = {
    "ADR-001": (
        "Runtime language and package boundaries",
        "Python 3.12+ (3.13 acceptable), one library package `casops`, one process per service under `services/`.",
    ),
    "ADR-002": (
        "Canonical JSON serialization and digest generation",
        "RFC 8785-style canonical JSON (sorted keys, compact separators, UTF-8) and SHA-256 lowercase hex digests.",
    ),
    "ADR-003": (
        "Operational, audit, artifact, and memory storage",
        "Filesystem agent folders + content-addressed `var/artifacts/`; SQLite for operational/audit/memory first slice; separate volumes for invariants, approvals, instruments, and held-out data.",
    ),
    "ADR-004": (
        "Signature and key-management model",
        "Host Ed25519 keys in `var/keys/` (never in agent folders). KMS is a later swap behind the same interface.",
    ),
    "ADR-005": (
        "Plugin I1–I3 sandbox technologies",
        "Adopt Wasmtime (I1), namespaces+seccomp (I2), Firecracker (I3). Missing OS support fails closed with `PLG_ISOLATION_TIER`; no silent downgrade.",
    ),
    "ADR-006": (
        "Authentication and capability-handle model",
        "Six actor classes; deny-by-default. Capability handles are signed, expiring, audience-bound tokens. No ambient credentials.",
    ),
    "ADR-007": (
        "Scheduler and cancellation architecture",
        "Deadline-aware scheduler with cancellation tokens on every DAG node. Shutdown honoured at node boundaries (FR-COR-004).",
    ),
    "ADR-008": (
        "Telemetry collector and encrypted spool",
        "OpenTelemetry SDK + Collector. Dual failure of exporter and local spool is containment stop (`OBS_AUDIT_UNAVAILABLE`).",
    ),
    "ADR-009": (
        "Memory indexing and deletion architecture",
        "Bitemporal records, derived-dependency index across eight paths, tombstone fan-out, post-deletion probes. Deletion never claims weight unlearning.",
    ),
    "ADR-010": (
        "Statistical implementation and independent verification",
        "Analysis plan is authoritative over floors. Adopt statsmodels/exact binomial; do not hand-roll inference. Screening schemas have no `pass` value.",
    ),
    "ADR-011": (
        "Model/tool/protocol adapter lifecycle",
        "Production binds only to `VERIFIED` capabilities. Deterministic local adapter is mandatory for CI. Digest change forces re-conformance.",
    ),
    "ADR-012": (
        "Corrigibility invariant storage mechanism (DEC-01)",
        "Separate signed corrigibility service with its own volume and credentials. Folder path `corrigibility/invariants.json` is a read-only projection.",
    ),
    "ADR-013": (
        "Instrument qualification data governance (DEC-06)",
        "Instrument registry is a separate service. Qualification records are append-only and agent-unwritable (`IQ-08`). Unqualified instruments may report, never gate (`IQ-01`).",
    ),
}


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    index_lines = ["# Architecture decision records\n", "Planning defaults applied from implementation_plan.md §24.\n"]
    for adr_id, (title, decision) in ADRS.items():
        path = ROOT / f"{adr_id.lower()}.md"
        path.write_text(
            f"# {adr_id}: {title}\n\n"
            f"**Status:** Accepted as coding-plan default (still formally open in the source plan until a signed decision log exists).\n\n"
            f"**Decision:** {decision}\n",
            encoding="utf-8",
        )
        index_lines.append(f"- [{adr_id}]({adr_id.lower()}.md) — {title}")
    (ROOT / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"wrote {len(ADRS)} ADRs")


if __name__ == "__main__":
    main()
