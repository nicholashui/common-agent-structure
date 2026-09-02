"""Generate spec/svg wireframes for every Control UI screen in spec/ui.v1.md."""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "spec" / "svg"

# Tokens from spec/common-style.html
WHITE = "#ffffff"
STONE_50 = "#fafaf9"
STONE_100 = "#f5f5f4"
STONE_200 = "#e7e5e4"
STONE_300 = "#d6d3d1"
STONE_400 = "#a8a29e"
STONE_500 = "#78716c"
STONE_700 = "#44403c"
STONE_800 = "#292524"
STONE_900 = "#1c1917"
INDIGO_50 = "#eef2ff"
INDIGO_100 = "#e0e7ff"
INDIGO_200 = "#c7d2fe"
INDIGO_600 = "#4f46e5"
INDIGO_700 = "#4338ca"
VIOLET_50 = "#f5f3ff"
VIOLET_200 = "#ddd6fe"
VIOLET_600 = "#7c3aed"
VIOLET_700 = "#6d28d9"
AMBER_50 = "#fffbeb"
AMBER_200 = "#fde68a"
AMBER_500 = "#f59e0b"
AMBER_700 = "#b45309"
EMERALD_50 = "#ecfdf5"
EMERALD_200 = "#a7f3d0"
EMERALD_500 = "#10b981"
EMERALD_700 = "#047857"
RED_50 = "#fef2f2"
RED_200 = "#fecaca"
RED_500 = "#ef4444"
RED_600 = "#dc2626"
SKY_50 = "#f0f9ff"
SKY_200 = "#bae6fd"

NAV = [
    ("Fleet", "01"),
    ("Overview", "02"),
    ("Structure", "03"),
    ("Compose", "04"),
    ("Run", "05"),
    ("Trace", "06"),
    ("Capabilities", "07"),
    ("Protocols", "08"),
    ("Memory", "09"),
    ("Plugins", "10"),
    ("Cache", "11"),
    ("Safety", "12"),
    ("Improvement", "13"),
    ("Validation", "14"),
    ("Corrigibility", "15"),
    ("Settings", "16"),
]

W, H = 1280, 800
NAV_W = 208
TOP = 56
STRIP = 52
CX = NAV_W
CY = TOP + STRIP
CW = W - NAV_W
CH = H - CY


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def r(x, y, w, h, fill, rx=12, stroke=None, sw=1) -> str:
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}"{s}/>'


def t(x, y, text, *, size=13, fill=STONE_900, weight=500, family="Inter, system-ui, sans-serif", anchor="start") -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" fill="{fill}" font-size="{size}" font-weight="{weight}" '
        f'font-family="{family}" text-anchor="{anchor}">{esc(text)}</text>'
    )


def mono(x, y, text, *, size=11, fill=STONE_700, anchor="start") -> str:
    return t(x, y, text, size=size, fill=fill, weight=500, family="ui-monospace, Consolas, monospace", anchor=anchor)


def pill(x, y, label, *, bg, border, fg, pulse=False) -> str:
    w = 11 * len(label) + 28
    dot = EMERALD_500 if "Live" in label or "Complete" in label or "Verified" in label else fg
    if "NOT" in label or "Unavail" in label or "off" in label.lower() or "Preview" in label:
        dot = STONE_400
    if "Failed" in label or "Recovery" in label:
        dot = RED_500
    if "Running" in label:
        dot = "#3b82f6"
    pulse_cls = ' class="pulse"' if pulse else ""
    return (
        f'{r(x, y, w, 22, bg, rx=999, stroke=border)}'
        f'<circle cx="{x + 11}" cy="{y + 11}" r="3.2" fill="{dot}"{pulse_cls}/>'
        f'{t(x + 20, y + 15, label, size=11, fill=fg, weight=500)}'
    )


def btn(x, y, w, h, label, *, fill=STONE_900, fg=WHITE, stroke=None) -> str:
    return r(x, y, w, h, fill, rx=999, stroke=stroke) + t(
        x + w / 2, y + h / 2 + 4.5, label, size=12, fill=fg, weight=500, anchor="middle"
    )


def icon_bot(x, y, s=18, fill=INDIGO_600) -> str:
    return (
        f'<circle cx="{x}" cy="{y - 2}" r="{s * 0.22}" fill="{fill}"/>'
        f'<rect x="{x - s * 0.28}" y="{y + 2}" width="{s * 0.56}" height="{s * 0.38}" rx="3" fill="{fill}"/>'
    )


def chrome(selected: str, *, crumb: str, title: str, subtitle: str = "") -> str:
    parts = [
        f'<rect width="{W}" height="{H}" fill="{WHITE}"/>',
        # top nav
        f'<rect x="0" y="0" width="{W}" height="{TOP}" fill="{WHITE}"/>',
        f'<line x1="0" y1="{TOP}" x2="{W}" y2="{TOP}" stroke="{STONE_200}" stroke-width="1"/>',
        r(16, 14, 28, 28, INDIGO_600, rx=8),
        f'<path d="M24 22 L36 28 L24 34 Z" fill="{WHITE}" opacity="0.9"/>',
        t(52, 34, "caso", size=14, fill=STONE_900, weight=600),
        t(108, 34, "Control UI", size=12, fill=STONE_400, weight=500),
        r(300, 12, 340, 32, STONE_50, rx=10, stroke=STONE_200),
        mono(314, 33, "casops.template.baseline_safe ▾", size=12, fill=STONE_700),
        pill(980, 17, "Live", bg=EMERALD_50, border=EMERALD_200, fg=EMERALD_700, pulse=True),
        t(1088, 34, "as_of just now", size=11, fill=STONE_400),
        # left nav
        f'<rect x="0" y="{TOP}" width="{NAV_W}" height="{H - TOP}" fill="{STONE_50}"/>',
        f'<line x1="{NAV_W}" y1="{TOP}" x2="{NAV_W}" y2="{H}" stroke="{STONE_200}"/>',
    ]
    y = TOP + 16
    for name, _ in NAV:
        active = name == selected
        if active:
            parts.append(r(10, y - 6, NAV_W - 20, 28, WHITE, rx=8, stroke=INDIGO_200))
            parts.append(r(10, y - 6, 3, 28, INDIGO_600, rx=2, stroke=None))
        color = STONE_900 if active else STONE_500
        wt = 600 if active else 500
        parts.append(t(24, y + 13, name, size=13, fill=color, weight=wt))
        y += 34
    # actor strip
    parts += [
        f'<rect x="{CX}" y="{TOP}" width="{CW}" height="{STRIP}" fill="{STONE_50}"/>',
        f'<line x1="{CX}" y1="{TOP + STRIP}" x2="{W}" y2="{TOP + STRIP}" stroke="{STONE_200}"/>',
        t(CX + 16, TOP + 20, "MUTATION CONTRACT", size=9, fill=STONE_400, weight=600),
        r(CX + 16, TOP + 26, 150, 22, WHITE, rx=8, stroke=STONE_200),
        t(CX + 26, TOP + 41, "host_service ▾", size=11, fill=STONE_800),
        r(CX + 176, TOP + 26, 220, 22, WHITE, rx=8, stroke=STONE_200),
        t(CX + 186, TOP + 41, "reason: operator-walkthrough", size=11, fill=STONE_500),
        r(CX + 406, TOP + 26, 150, 22, WHITE, rx=8, stroke=STONE_200),
        t(CX + 416, TOP + 41, "parent: none", size=11, fill=STONE_500),
        r(CX + 568, TOP + 26, 118, 22, INDIGO_50, rx=999, stroke=INDIGO_200),
        t(CX + 627, TOP + 41, "dry-run ON", size=11, fill=INDIGO_700, weight=600, anchor="middle"),
        t(CX + 16, TOP + 14, crumb, size=11, fill=STONE_400),
    ]
    # page header
    parts.append(t(CX + 24, CY + 36, title, size=22, fill=STONE_900, weight=700))
    if subtitle:
        parts.append(t(CX + 24, CY + 58, subtitle, size=13, fill=STONE_500))
    return "\n".join(parts)


def wrap(name: str, title: str, desc: str, body: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">
  <title id="title">{esc(title)}</title>
  <desc id="desc">{esc(desc)}</desc>
  <defs>
    <style>
      text {{ font-family: Inter, system-ui, sans-serif; }}
      .pulse {{ animation: p 1.4s ease-in-out infinite; }}
      @keyframes p {{ 0%,100% {{ opacity:1 }} 50% {{ opacity:.35 }} }}
    </style>
  </defs>
{body}
</svg>
"""


def screen_fleet() -> str:
    body = [chrome("Fleet", crumb="Fleet", title="Fleet", subtitle="Every agent the host can load. Cards refresh every 15s while this tab is visible.")]
    cards = [
        ("casops.template.baseline_safe", "BaselineSafeTemplate", "complete", "mem none", "dbb02c86"),
        ("casops.local.reviewer", "Reviewer", "running", "mem working", "a91c0e12"),
        ("casops.local.research", "ResearchOnly", "queued", "mem none", "—"),
    ]
    x0, y0 = CX + 24, CY + 78
    for i, (aid, role, st, mem, hsh) in enumerate(cards):
        x = x0 + (i % 3) * 340
        y = y0 + (i // 3) * 250
        body += [
            r(x, y, 324, 228, WHITE, rx=16, stroke=STONE_200),
            r(x + 16, y + 16, 40, 40, INDIGO_50, rx=12, stroke=INDIGO_100),
            icon_bot(x + 36, y + 36),
            t(x + 68, y + 34, aid.split(".")[-1], size=14, fill=STONE_900, weight=600),
            r(x + 68, y + 42, 92, 18, INDIGO_50, rx=6, stroke=INDIGO_200),
            t(x + 78, y + 55, "Common v3.0", size=10, fill=INDIGO_700, weight=600),
            t(x + 16, y + 80, role, size=12, fill=STONE_500),
            mono(x + 16, y + 102, aid, size=10, fill=STONE_400),
            r(x + 16, y + 118, 90, 52, STONE_50, rx=10, stroke=STONE_100),
            t(x + 28, y + 138, "Hash", size=10, fill=STONE_400),
            mono(x + 28, y + 156, hsh, size=11, fill=STONE_800),
            r(x + 116, y + 118, 90, 52, STONE_50, rx=10, stroke=STONE_100),
            t(x + 128, y + 138, "Run", size=10, fill=STONE_400),
            t(x + 128, y + 156, st, size=12, fill=EMERALD_700 if st == "complete" else INDIGO_700, weight=600),
            r(x + 216, y + 118, 90, 52, STONE_50, rx=10, stroke=STONE_100),
            t(x + 228, y + 138, "Memory", size=10, fill=STONE_400),
            t(x + 228, y + 156, mem, size=11, fill=STONE_700),
            btn(x + 16, y + 186, 88, 28, "Open", fill=STONE_900),
            btn(x + 112, y + 186, 140, 28, "Compose preview", fill=WHITE, fg=STONE_700, stroke=STONE_200),
        ]
    return wrap("fleet", "Fleet screen", "Grid of agent cards with status pills, compose hash, and Open / Compose preview actions.", "\n".join(body))


def screen_overview() -> str:
    body = [chrome("Overview", crumb="Fleet / casops.template.baseline_safe / Overview", title="Overview", subtitle="Attestation, structure summary, last run, and validation honesty.")]
    x, y = CX + 24, CY + 78
    body += [
        r(x, y, 1024, 88, INDIGO_50, rx=16, stroke=INDIGO_200),
        t(x + 20, y + 32, "Host attestation", size=14, fill=INDIGO_700, weight=600),
        t(x + 20, y + 54, "status: host_reference  ·  invariant_set_id: inv-casops-v3", size=12, fill=STONE_700),
        mono(x + 20, y + 74, "digest  dd6f875c24bb2faa7b9757f5c48a86812d798cba…", size=11, fill=STONE_500),
        r(x, y + 104, 500, 200, WHITE, rx=16, stroke=STONE_200),
        t(x + 20, y + 132, "Structure", size=14, fill=STONE_900, weight=600),
        t(x + 20, y + 158, "structure_id   casops.common_agent.v3", size=12, fill=STONE_700),
        t(x + 20, y + 180, "schema_version  3.0", size=12, fill=STONE_700),
        t(x + 20, y + 202, "folder          agents/_template_v3", size=12, fill=STONE_700),
        t(x + 20, y + 224, "spec_bytes      2345", size=12, fill=STONE_700),
        r(x + 524, y + 104, 500, 200, WHITE, rx=16, stroke=STONE_200),
        t(x + 544, y + 132, "Last run (this session)", size=14, fill=STONE_900, weight=600),
        pill(x + 544, y + 148, "Complete", bg=EMERALD_50, border=EMERALD_200, fg=EMERALD_700),
        mono(x + 544, y + 196, "tr_b5db3e8836d1cf2e", size=12),
        t(x + 544, y + 220, "adapter local_deterministic  ·  memory_writes []", size=12, fill=STONE_500),
        t(x + 544, y + 244, "Open trace →", size=12, fill=INDIGO_600, weight=600),
        r(x, y + 320, 1024, 140, STONE_50, rx=16, stroke=AMBER_200),
        t(x + 20, y + 352, "Validation report", size=14, fill=STONE_900, weight=600),
        pill(x + 20, y + 368, "NOT_RUN", bg=STONE_100, border=STONE_200, fg=STONE_500),
        t(x + 140, y + 384, "pass: false   ·   reason: unqualified_instruments", size=13, fill=AMBER_700, weight=500),
        t(x + 20, y + 424, "Emerald pass styling is forbidden while instruments INS-01…08 are UNQUALIFIED.", size=12, fill=STONE_500),
        btn(x + 20, y + 480, 150, 32, "Compose preview", fill=INDIGO_600),
        btn(x + 184, y + 480, 88, 32, "Run", fill=STONE_900),
    ]
    return wrap("overview", "Agent overview screen", "Attestation banner, structure summary, last run, and NOT_RUN validation honesty.", "\n".join(body))


def screen_structure() -> str:
    body = [chrome("Structure", crumb="Fleet / casops.template.baseline_safe / Structure", title="Structure", subtitle="Folder contract versus resolved composition.")]
    x, y = CX + 24, CY + 78
    body += [
        r(x, y, 500, 470, STONE_50, rx=16, stroke=STONE_200),
        t(x + 20, y + 32, "GET …/structure", size=12, fill=STONE_400, weight=600),
        mono(x + 20, y + 64, "{", size=12),
        mono(x + 36, y + 86, '"agent_id": "casops.template.baseline_safe",', size=12),
        mono(x + 36, y + 108, '"structure_id": "casops.common_agent.v3",', size=12),
        mono(x + 36, y + 130, '"schema_version": "3.0",', size=12),
        mono(x + 36, y + 152, '"folder": "agents/_template_v3",', size=12),
        mono(x + 36, y + 174, '"spec_bytes": 2345', size=12),
        mono(x + 20, y + 196, "}", size=12),
        r(x + 524, y, 500, 470, WHITE, rx=16, stroke=VIOLET_200),
        t(x + 544, y + 32, "GET …/resolved", size=12, fill=VIOLET_600, weight=600),
        t(x + 544, y + 64, "MRO", size=14, fill=STONE_900, weight=600),
        r(x + 544, y + 80, 280, 40, VIOLET_50, rx=12, stroke=VIOLET_200),
        t(x + 560, y + 106, "casops.template.baseline_safe", size=12, fill=VIOLET_700, weight=600),
        t(x + 544, y + 150, "compose_hash", size=12, fill=STONE_400),
        r(x + 544, y + 162, 220, 22, INDIGO_50, rx=6, stroke=INDIGO_200),
        mono(x + 556, y + 178, "dbb02c8628847eea…", size=11, fill=INDIGO_700),
        t(x + 544, y + 220, "Lock excerpt", size=12, fill=STONE_400),
        t(x + 544, y + 244, "production_bindable: true", size=12, fill=STONE_700),
        t(x + 544, y + 266, "adapter: local_deterministic", size=12, fill=STONE_700),
        t(x + 544, y + 288, "wrote_locks: n/a (GET)", size=12, fill=STONE_500),
    ]
    return wrap("structure", "Structure screen", "Two columns: raw structure JSON and resolved MRO with compose hash.", "\n".join(body))


def screen_compose() -> str:
    body = [chrome("Compose", crumb="Fleet / casops.template.baseline_safe / Compose", title="Compose preview", subtitle="Prospective lock. This screen never implies files were written.")]
    x, y = CX + 24, CY + 78
    findings = [
        ("folder validated", True),
        ("invariants attested", True),
        ("mro=casops.template.baseline_safe", True),
        ("capabilities=True", True),
        ("plugins_validated=0", True),
        ("preview: no locks written", True),
    ]
    body += [
        btn(x, y, 160, 32, "Compose preview", fill=INDIGO_600),
        pill(x + 176, y + 5, "Preview only", bg=STONE_100, border=STONE_200, fg=STONE_500),
        r(x + 320, y, 728, 32, INDIGO_50, rx=8, stroke=INDIGO_200),
        mono(x + 336, y + 21, "compose_hash  dbb02c8628847eeaee10cdf5b9f8c68adaea5e45…", size=12, fill=INDIGO_700),
        r(x, y + 52, 500, 420, WHITE, rx=16, stroke=STONE_200),
        t(x + 20, y + 80, "Findings", size=14, fill=STONE_900, weight=600),
    ]
    for i, (label, ok) in enumerate(findings):
        yy = y + 108 + i * 36
        fill = EMERALD_50 if ok else RED_50
        br = EMERALD_200 if ok else RED_200
        fg = EMERALD_700 if ok else RED_600
        mark = "✓" if ok else "×"
        body += [
            r(x + 20, yy, 460, 28, fill, rx=8, stroke=br),
            t(x + 36, yy + 19, f"{mark}  {label}", size=12, fill=fg, weight=500),
        ]
    body += [
        r(x + 524, y + 52, 500, 200, WHITE, rx=16, stroke=INDIGO_200),
        t(x + 544, y + 84, "MRO node", size=14, fill=STONE_900, weight=600),
        r(x + 560, y + 108, 420, 96, WHITE, rx=16, stroke=INDIGO_200, sw=2),
        r(x + 576, y + 124, 32, 32, INDIGO_50, rx=10, stroke=INDIGO_200),
        icon_bot(x + 592, y + 140, 16),
        t(x + 620, y + 138, "casops.template.baseline_safe", size=13, fill=STONE_900, weight=600),
        t(x + 620, y + 158, "Linked to host compose  ·  indigo solid border", size=11, fill=INDIGO_600),
        pill(x + 620, y + 170, "Complete", bg=EMERALD_50, border=EMERALD_200, fg=EMERALD_700),
        r(x + 524, y + 268, 500, 204, RED_50, rx=16, stroke=RED_200),
        t(x + 544, y + 300, "Errors", size=14, fill=RED_600, weight=600),
        t(x + 544, y + 328, "[]  empty — compose may proceed to Run", size=13, fill=STONE_700),
        t(x + 544, y + 360, "wrote_locks: false", size=13, fill=STONE_700, weight=600),
        t(x + 544, y + 388, "If this were true, show an amber host-contract warning.", size=12, fill=STONE_500),
    ]
    return wrap("compose", "Compose preview screen", "Findings checklist, MRO canvas node, empty errors, wrote_locks false badge.", "\n".join(body))


def screen_run() -> str:
    body = [chrome("Run", crumb="Fleet / casops.template.baseline_safe / Run", title="Run", subtitle="Execute baseline_safe. No chat transcript — sealed adapter output only.")]
    x, y = CX + 24, CY + 78
    body += [
        r(x, y, 420, 280, WHITE, rx=16, stroke=INDIGO_200, sw=2),
        t(x + 20, y + 32, "DAG  ·  GET …/runtime/plan", size=12, fill=INDIGO_600, weight=600),
        r(x + 120, y + 80, 180, 72, WHITE, rx=16, stroke=INDIGO_200, sw=2),
        t(x + 210, y + 112, "run.root", size=13, fill=STONE_900, weight=600, anchor="middle"),
        t(x + 210, y + 132, "tr_b5db3e88", size=11, fill=STONE_400, anchor="middle"),
        f'<line x1="{x + 210}" y1="{y + 152}" x2="{x + 210}" y2="{y + 188}" stroke="{INDIGO_200}" stroke-width="2"/>',
        r(x + 120, y + 188, 180, 64, INDIGO_50, rx=16, stroke=INDIGO_200),
        t(x + 210, y + 216, "node.model", size=13, fill=INDIGO_700, weight=600, anchor="middle"),
        t(x + 210, y + 236, "model_1", size=11, fill=STONE_500, anchor="middle"),
        r(x + 444, y, 300, 280, WHITE, rx=16, stroke=STONE_200),
        t(x + 464, y + 32, "Context budget", size=14, fill=STONE_900, weight=600),
        mono(x + 464, y + 60, "GET …/runtime/context-budget", size=11, fill=STONE_400),
        t(x + 464, y + 92, "policy / task / memory / tools", size=12, fill=STONE_700),
        t(x + 464, y + 114, "pinned: safety, corrigibility", size=12, fill=STONE_700),
        r(x + 444, y + 148, 260, 36, STONE_50, rx=8),
        t(x + 460, y + 172, "Disclosure collapsed", size=12, fill=STONE_500),
        r(x + 768, y, 256, 280, WHITE, rx=16, stroke=STONE_200),
        t(x + 788, y + 32, "Cache", size=14, fill=STONE_900, weight=600),
        t(x + 788, y + 60, "tiers  [T0]", size=12, fill=STONE_700),
        pill(x + 788, y + 76, "T3 off", bg=STONE_100, border=STONE_200, fg=STONE_500),
        t(x + 788, y + 128, "No Enable T3 control — no API.", size=11, fill=STONE_400),
        btn(x + 788, y + 220, 140, 28, "Invalidate", fill=WHITE, fg=STONE_700, stroke=STONE_200),
        btn(x, y + 300, 100, 36, "Run", fill=STONE_900),
        r(x + 120, y + 300, 904, 196, WHITE, rx=16, stroke=STONE_200),
        t(x + 140, y + 332, "Last result", size=14, fill=STONE_900, weight=600),
        pill(x + 140, y + 348, "Complete", bg=EMERALD_50, border=EMERALD_200, fg=EMERALD_700),
        mono(x + 140, y + 396, "root   tr_b5db3e8836d1cf2e", size=12),
        mono(x + 140, y + 416, "art    art_48fb91808379", size=12),
        t(x + 140, y + 444, "containment_stop null   ·   memory_writes []   ·   adapter local_deterministic", size=12, fill=STONE_500),
        t(x + 140, y + 470, "Open trace →", size=13, fill=INDIGO_600, weight=600),
        t(x + 520, y + 396, "sealed text", size=11, fill=STONE_400),
        mono(x + 520, y + 416, "deterministic:c3ba620011e4", size=12, fill=STONE_800),
    ]
    return wrap("run", "Run screen", "DAG canvas, context budget, T3-off cache, Run button, sealed result without a chat transcript.", "\n".join(body))


def screen_trace() -> str:
    body = [chrome("Trace", crumb="Fleet / casops.template.baseline_safe / Trace", title="Trace", subtitle="One root span. Replay and counterfactual are mutations. No memory-write control.")]
    x, y = CX + 24, CY + 78
    body += [
        r(x, y, 640, 460, WHITE, rx=16, stroke=STONE_200),
        t(x + 20, y + 32, "Span tree", size=14, fill=STONE_900, weight=600),
        pill(x + 120, y + 16, "Complete", bg=EMERALD_50, border=EMERALD_200, fg=EMERALD_700),
        r(x + 40, y + 64, 560, 56, INDIGO_50, rx=12, stroke=INDIGO_200),
        t(x + 56, y + 88, "tr_b5db3e8836d1cf2e", size=13, fill=STONE_900, weight=600),
        t(x + 56, y + 108, "run.root   ·   parent_id null   ·   THE root", size=11, fill=STONE_500),
        f'<line x1="{x + 68}" y1="{y + 120}" x2="{x + 68}" y2="{y + 152}" stroke="{STONE_300}" stroke-width="2"/>',
        r(x + 80, y + 152, 520, 48, WHITE, rx=12, stroke=STONE_200),
        t(x + 96, y + 172, "sp_3ffcae3a2e482f78", size=12, fill=STONE_800, weight=600),
        t(x + 96, y + 190, "node.model  ·  node_id model_1", size=11, fill=STONE_500),
        btn(x + 20, y + 400, 100, 32, "Replay", fill=STONE_900),
        r(x + 132, y + 400, 200, 32, WHITE, rx=999, stroke=STONE_200),
        t(x + 148, y + 421, "counterfactual: route", size=11, fill=STONE_500),
        btn(x + 344, y + 400, 140, 32, "Counterfactual", fill=WHITE, fg=INDIGO_700, stroke=INDIGO_200),
        r(x + 664, y, 360, 220, WHITE, rx=16, stroke=STONE_200),
        t(x + 684, y + 32, "Root cause", size=14, fill=STONE_900, weight=600),
        t(x + 684, y + 64, "GET …/root-cause", size=12, fill=STONE_400),
        t(x + 684, y + 96, "cause     none", size=13, fill=STONE_700),
        t(x + 684, y + 118, "adapter   local_deterministic", size=13, fill=STONE_700),
        r(x + 664, y + 240, 360, 220, WHITE, rx=16, stroke=STONE_200),
        t(x + 684, y + 272, "Evidence graph", size=14, fill=STONE_900, weight=600),
        t(x + 684, y + 304, "GET …/artifacts/{id}/evidence-graph", size=11, fill=STONE_400),
        t(x + 684, y + 336, "claims[0].support", size=12, fill=STONE_700),
        mono(x + 684, y + 358, "deterministic_adapter", size=12),
        t(x + 684, y + 390, "unsupported  []", size=12, fill=STONE_500),
    ]
    return wrap("trace", "Trace inspector screen", "Root span tree, replay and counterfactual controls, root-cause and evidence panels.", "\n".join(body))


def screen_capabilities() -> str:
    body = [chrome("Capabilities", crumb="Fleet / casops.template.baseline_safe / Capabilities", title="Capabilities", subtitle="Unverified claims stay amber. Never paint them green.")]
    x, y = CX + 24, CY + 78
    rows = [
        ("model.local_deterministic", "VERIFIED", True),
        ("model.batch_invariant_kernels", "UNVERIFIED", False),
        ("plugin.wasm.i1", "UNVERIFIED", False),
    ]
    body += [
        btn(x, y, 100, 32, "Verify", fill=INDIGO_600),
        t(x + 120, y + 21, "POST …/capabilities/verify", size=12, fill=STONE_400),
        r(x, y + 52, 1024, 420, WHITE, rx=16, stroke=STONE_200),
        t(x + 24, y + 84, "Capability", size=12, fill=STONE_400, weight=600),
        t(x + 520, y + 84, "Status", size=12, fill=STONE_400, weight=600),
        t(x + 720, y + 84, "Production bindable", size=12, fill=STONE_400, weight=600),
        f'<line x1="{x + 16}" y1="{y + 96}" x2="{x + 1008}" y2="{y + 96}" stroke="{STONE_200}"/>',
    ]
    for i, (cap, st, ok) in enumerate(rows):
        yy = y + 120 + i * 56
        body.append(mono(x + 24, yy + 8, cap, size=13, fill=STONE_800))
        if ok:
            body.append(pill(x + 520, yy - 10, "VERIFIED", bg=EMERALD_50, border=EMERALD_200, fg=EMERALD_700))
            body.append(t(x + 720, yy + 8, "yes", size=13, fill=EMERALD_700, weight=600))
        else:
            body.append(pill(x + 520, yy - 10, "UNVERIFIED", bg=AMBER_50, border=AMBER_200, fg=AMBER_700))
            body.append(t(x + 720, yy + 8, "no — amber, not green", size=13, fill=AMBER_700))
    body.append(t(x + 24, y + 430, "Disclosure: GET …/runtime/capabilities (same matrix, raw JSON)", size=12, fill=STONE_400))
    return wrap("capabilities", "Capabilities screen", "Matrix table with VERIFIED emerald and UNVERIFIED amber rows plus Verify action.", "\n".join(body))


def screen_protocols() -> str:
    body = [chrome("Protocols", crumb="Fleet / casops.template.baseline_safe / Protocols", title="Protocols", subtitle="Read-only. There is no PATCH on the v3 plane.")]
    x, y = CX + 24, CY + 78
    body += [
        r(x, y, 1024, 480, STONE_50, rx=16, stroke=STONE_200),
        t(x + 24, y + 36, "GET …/protocols", size=12, fill=STONE_400, weight=600),
        mono(x + 24, y + 72, "{", size=13),
        mono(x + 40, y + 96, '"agent_id": "casops.template.baseline_safe",', size=13),
        mono(x + 40, y + 120, '"protocols": "{ \\"schema_version\\": \\"3.0\\", … }",', size=13),
        mono(x + 40, y + 144, '"pinned": ["agent_message", "event"]', size=13),
        mono(x + 24, y + 168, "}", size=13),
        t(x + 24, y + 220, "No edit, import, or save control on this screen.", size=13, fill=STONE_500),
    ]
    return wrap("protocols", "Protocols screen", "Read-only JSON well for GET protocols with no edit controls.", "\n".join(body))


def screen_memory() -> str:
    body = [chrome("Memory", crumb="Fleet / casops.template.baseline_safe / Memory", title="Memory", subtitle="Tenant and subject are required. Empty other-tenant results are success, not errors.")]
    x, y = CX + 24, CY + 78
    body += [
        r(x, y, 1024, 64, AMBER_50, rx=12, stroke=AMBER_200),
        t(x + 20, y + 28, "policy.mode = none", size=14, fill=AMBER_700, weight=600),
        t(x + 20, y + 48, "Write candidate disabled  ·  MEM_TRUST_TIER  ·  hierarchy H0", size=12, fill=STONE_700),
        t(x + 20, y + 96, "Scope", size=12, fill=STONE_400, weight=600),
        r(x, y + 108, 200, 32, WHITE, rx=8, stroke=STONE_200),
        t(x + 12, y + 129, "tenant  t1", size=12, fill=STONE_800),
        r(x + 216, y + 108, 200, 32, WHITE, rx=8, stroke=STONE_200),
        t(x + 228, y + 129, "subject  s1", size=12, fill=STONE_800),
        r(x + 432, y + 108, 240, 32, WHITE, rx=8, stroke=STONE_200),
        t(x + 444, y + 129, "text filter (optional)", size=12, fill=STONE_400),
        btn(x + 688, y + 108, 88, 32, "Query", fill=STONE_900),
        btn(x + 788, y + 108, 140, 32, "Write candidate", fill=STONE_100, fg=STONE_400, stroke=STONE_200),
        r(x, y + 160, 1024, 220, WHITE, rx=16, stroke=STONE_200),
        t(x + 20, y + 188, "Results in this scope", size=13, fill=STONE_900, weight=600),
        t(x + 20, y + 220, "memory_id", size=11, fill=STONE_400),
        t(x + 280, y + 220, "text", size=11, fill=STONE_400),
        t(x + 700, y + 220, "actions", size=11, fill=STONE_400),
        f'<line x1="{x + 16}" y1="{y + 232}" x2="{x + 1008}" y2="{y + 232}" stroke="{STONE_200}"/>',
        t(x + 20, y + 280, "No rows in this scope", size=14, fill=STONE_500),
        t(x + 20, y + 304, "Empty list is a successful isolation miss — do not toast “not found”.", size=12, fill=STONE_400),
        btn(x, y + 404, 180, 32, "Enqueue consolidate", fill=WHITE, fg=STONE_800, stroke=STONE_200),
        r(x + 196, y + 404, 828, 32, STONE_50, rx=8, stroke=STONE_200),
        t(x + 212, y + 425, "queued: true   ·   queue_depth: 1   ·   Serving path enqueues only. Worker drains offline.", size=12, fill=STONE_500),
    ]
    return wrap("memory", "Memory screen", "Policy none disables writes; tenant/subject scope bar; successful empty results; enqueue consolidate.", "\n".join(body))


def screen_plugins() -> str:
    body = [chrome("Plugins", crumb="Fleet / casops.template.baseline_safe / Plugins", title="Plugins", subtitle="Validate without executing. executed must stay false.")]
    x, y = CX + 24, CY + 78
    body += [
        btn(x, y, 180, 32, "Validate without exec", fill=INDIGO_600),
        r(x, y + 52, 1024, 420, WHITE, rx=16, stroke=STONE_200),
        t(x + 24, y + 84, "id", size=11, fill=STONE_400, weight=600),
        t(x + 220, y + 84, "isolation", size=11, fill=STONE_400, weight=600),
        t(x + 420, y + 84, "validated", size=11, fill=STONE_400, weight=600),
        t(x + 560, y + 84, "executed", size=11, fill=STONE_400, weight=600),
        f'<line x1="{x + 16}" y1="{y + 96}" x2="{x + 1008}" y2="{y + 96}" stroke="{STONE_200}"/>',
        t(x + 24, y + 140, "(empty registry)", size=13, fill=STONE_500),
        t(x + 24, y + 168, "count: 0   ·   executed: false", size=12, fill=STONE_400),
        t(x + 24, y + 220, "Isolation legend", size=12, fill=STONE_400, weight=600),
        pill(x + 24, y + 236, "I0", bg=STONE_100, border=STONE_200, fg=STONE_500),
        pill(x + 88, y + 236, "I1 WASM", bg=INDIGO_50, border=INDIGO_200, fg=INDIGO_700),
        pill(x + 196, y + 236, "I2 process", bg=VIOLET_50, border=VIOLET_200, fg=VIOLET_700),
        pill(x + 324, y + 236, "I3 guest", bg=AMBER_50, border=AMBER_200, fg=AMBER_700),
        t(x + 24, y + 292, "No upload .py. No execute button. Network requires I3. Unsigned cannot be I0/I1.", size=12, fill=STONE_500),
        r(x + 24, y + 320, 976, 48, RED_50, rx=10, stroke=RED_200),
        t(x + 40, y + 350, "If executed: true ever appears — host contract break. Show this red banner.", size=12, fill=RED_600, weight=600),
    ]
    return wrap("plugins", "Plugins screen", "Empty registry, validate-without-exec action, isolation legend, executed-false contract.", "\n".join(body))


def screen_cache() -> str:
    body = [chrome("Cache", crumb="Fleet / casops.template.baseline_safe / Cache", title="Cache", subtitle="Stats and invalidate only. No Enable T3 control — the public plane has no such route.")]
    x, y = CX + 24, CY + 78
    body += [
        btn(x, y, 120, 32, "Invalidate", fill=WHITE, fg=STONE_800, stroke=STONE_200),
        r(x, y + 52, 480, 420, WHITE, rx=16, stroke=STONE_200),
        t(x + 24, y + 84, "GET …/cache/stats", size=12, fill=STONE_400, weight=600),
        t(x + 24, y + 120, "entries", size=12, fill=STONE_400),
        t(x + 200, y + 120, "0", size=20, fill=STONE_900, weight=700),
        t(x + 24, y + 160, "tiers", size=12, fill=STONE_400),
        r(x + 200, y + 144, 48, 24, STONE_100, rx=8, stroke=STONE_200),
        t(x + 212, y + 161, "T0", size=12, fill=STONE_800, weight=600),
        t(x + 24, y + 200, "t3_enabled", size=12, fill=STONE_400),
        pill(x + 200, y + 184, "T3 off", bg=STONE_100, border=STONE_200, fg=STONE_500),
        t(x + 24, y + 248, "telemetry.hits / misses", size=12, fill=STONE_400),
        t(x + 24, y + 272, "0  /  0", size=16, fill=STONE_800, weight=600),
        r(x + 504, y + 52, 520, 420, STONE_50, rx=16, stroke=STONE_200),
        t(x + 524, y + 88, "Why there is no Enable T3 button", size=14, fill=STONE_900, weight=600),
        t(x + 524, y + 120, "FR-CACHE-004: T3 stays off until an independent", size=13, fill=STONE_500),
        t(x + 524, y + 142, "equivalence verifier and false-reuse ≤ 0.5% pass.", size=13, fill=STONE_500),
        t(x + 524, y + 174, "ui.v1 does not invent a host route.", size=13, fill=STONE_500),
        t(x + 524, y + 220, "Invalidate → POST …/cache/invalidate", size=13, fill=STONE_700),
    ]
    return wrap("cache", "Cache screen", "T0 stats, T3-off pill, invalidate action, and an explicit note that Enable T3 is absent.", "\n".join(body))


def screen_safety() -> str:
    body = [chrome("Safety", crumb="Fleet / casops.template.baseline_safe / Safety", title="Safety", subtitle="Incidents list and a confirmed red-team fixture. Not a pentest console.")]
    x, y = CX + 24, CY + 78
    body += [
        btn(x, y, 180, 32, "Run red-team fixture", fill=STONE_900),
        r(x, y + 52, 1024, 280, WHITE, rx=16, stroke=STONE_200),
        t(x + 24, y + 84, "Incidents", size=14, fill=STONE_900, weight=600),
        t(x + 24, y + 112, "GET …/safety/incidents", size=12, fill=STONE_400),
        t(x + 24, y + 160, "No incidents recorded for this agent.", size=13, fill=STONE_500),
        r(x + 280, y + 200, 464, 96, WHITE, rx=16, stroke=STONE_200),
        t(x + 512, y + 232, "Run red-team fixture?", size=14, fill=STONE_900, weight=600, anchor="middle"),
        t(x + 512, y + 252, "POST …/safety/redteam", size=12, fill=STONE_400, anchor="middle"),
        btn(x + 360, y + 262, 88, 26, "Cancel", fill=WHITE, fg=STONE_700, stroke=STONE_200),
        btn(x + 456, y + 262, 100, 26, "Confirm", fill=STONE_900),
    ]
    return wrap("safety", "Safety screen", "Empty incidents table and a confirm dialog for the red-team fixture.", "\n".join(body))


def screen_improvement() -> str:
    body = [chrome("Improvement", crumb="Fleet / casops.template.baseline_safe / Improvement", title="Improvement", subtitle="Human-in-the-loop kanban. No promote-to-production. agent_runtime cannot approve.")]
    x, y = CX + 24, CY + 78
    cols = [
        ("Proposed", STONE_50, [("c2", "PROPOSED")]),
        ("Evaluated", VIOLET_50, [("c1", "EVALUATED")]),
        ("Approved", EMERALD_50, []),
        ("Rolled back", AMBER_50, []),
    ]
    body.append(t(x, y + 8, "Kanban  ·  GET …/improvement/candidates", size=12, fill=STONE_400))
    for i, (name, bg, cards) in enumerate(cols):
        xx = x + i * 256
        body += [
            r(xx, y + 28, 244, 280, bg, rx=16, stroke=STONE_200),
            t(xx + 16, y + 56, name, size=13, fill=STONE_900, weight=600),
        ]
        if not cards:
            body.append(t(xx + 16, y + 120, "Empty", size=12, fill=STONE_400))
        for j, (cid, st) in enumerate(cards):
            yy = y + 76 + j * 88
            body += [
                r(xx + 12, yy, 220, 80, WHITE, rx=12, stroke=STONE_200),
                t(xx + 24, yy + 24, cid, size=13, fill=STONE_900, weight=600),
                t(xx + 24, yy + 44, st, size=11, fill=STONE_500),
                t(xx + 24, yy + 66, "Evaluate   Approve   Rollback", size=11, fill=INDIGO_600),
            ]
    body += [
        r(x, y + 324, 1024, 160, WHITE, rx=16, stroke=STONE_200),
        t(x + 20, y + 352, "Ledger  ·  GET …/improvement/ledger", size=14, fill=STONE_900, weight=600),
        t(x + 20, y + 384, "type", size=11, fill=STONE_400),
        t(x + 160, y + 384, "cid", size=11, fill=STONE_400),
        t(x + 280, y + 384, "actor", size=11, fill=STONE_400),
        t(x + 20, y + 412, "evaluate", size=12, fill=STONE_700),
        t(x + 160, y + 412, "c1", size=12, fill=STONE_700),
        t(x + 280, y + 412, "host_service", size=12, fill=STONE_700),
        t(x + 20, y + 456, "Approve is hidden when actor is agent_runtime (IMP_SELF_APPROVAL).", size=12, fill=RED_600),
    ]
    return wrap("improvement", "Improvement screen", "Four-column kanban plus ledger table; approve gated on actor class.", "\n".join(body))


def screen_validation() -> str:
    body = [chrome("Validation", crumb="Fleet / casops.template.baseline_safe / Validation", title="Validation", subtitle="Honesty first. NOT_RUN and screening must not look like a pass.")]
    x, y = CX + 24, CY + 78
    body += [
        r(x, y, 1024, 200, STONE_50, rx=16, stroke=AMBER_200),
        t(x + 24, y + 40, "GET …/validation/report", size=12, fill=STONE_400, weight=600),
        t(x + 24, y + 72, "verdict", size=28, fill=STONE_900, weight=700),
        pill(x + 24, y + 88, "NOT_RUN", bg=STONE_100, border=STONE_200, fg=STONE_500),
        t(x + 24, y + 140, "pass: false", size=16, fill=AMBER_700, weight=600),
        t(x + 24, y + 168, "reason: unqualified_instruments   ·   INS-01 … INS-08", size=13, fill=STONE_700),
        r(x, y + 220, 500, 140, VIOLET_50, rx=16, stroke=VIOLET_200),
        t(x + 20, y + 252, "Screening", size=14, fill=VIOLET_700, weight=600),
        pill(x + 20, y + 268, "INDICATIVE — not a release pass", bg=VIOLET_50, border=VIOLET_200, fg=VIOLET_700),
        t(x + 20, y + 320, "Honesty INDICATIVE. pass stays false.", size=12, fill=STONE_700),
        r(x + 524, y + 220, 500, 140, WHITE, rx=16, stroke=STONE_200),
        t(x + 544, y + 252, "MEASURED_LOCAL", size=14, fill=STONE_900, weight=600),
        t(x + 544, y + 280, "Emerald only if pass: true after confirmatory", size=12, fill=STONE_500),
        t(x + 544, y + 302, "and qualified instruments.", size=12, fill=STONE_500),
        r(x, y + 380, 1024, 100, WHITE, rx=16, stroke=STONE_200),
        t(x + 20, y + 412, "Regression suite  ·  GET …/regression/suite", size=14, fill=STONE_900, weight=600),
        t(x + 20, y + 444, "fixtures:  (none in template)", size=13, fill=STONE_500),
    ]
    return wrap("validation", "Validation screen", "Large NOT_RUN honesty panel, INDICATIVE screening note, regression suite list.", "\n".join(body))


def screen_corrigibility() -> str:
    body = [chrome("Corrigibility", crumb="Fleet / casops.template.baseline_safe / Corrigibility", title="Corrigibility", subtitle="Host-owned. The agent folder cannot rewrite this. No edit controls.")]
    x, y = CX + 24, CY + 78
    body += [
        r(x, y, 1024, 88, INDIGO_50, rx=16, stroke=INDIGO_200),
        t(x + 24, y + 36, "The agent folder cannot rewrite this.", size=16, fill=INDIGO_700, weight=600),
        t(x + 24, y + 60, "Host-owned invariant store  ·  GET …/corrigibility/attestation", size=13, fill=STONE_700),
        r(x, y + 112, 1024, 360, STONE_50, rx=16, stroke=STONE_200),
        mono(x + 24, y + 148, "status              host_reference", size=13),
        mono(x + 24, y + 176, "invariant_set_id    inv-casops-v3", size=13),
        mono(x + 24, y + 204, "digest              dd6f875c24bb2faa7b9757f5c48a86812d798cba2194e81a…", size=13),
        mono(x + 24, y + 232, "signature           (expand to reveal)", size=13, fill=STONE_400),
        t(x + 24, y + 280, "No edit, rotate, or disable control on this screen.", size=13, fill=STONE_500),
        r(x + 24, y + 312, 976, 64, RED_50, rx=12, stroke=RED_200),
        t(x + 40, y + 340, "Containment (IMP_CORRIGIBILITY): Recovery banner, mutations disabled except Reload attestation.", size=12, fill=RED_600, weight=600),
        t(x + 40, y + 360, "Status pill: Recovery / Failed — never a green Live while containment_required.", size=12, fill=RED_600),
    ]
    return wrap("corrigibility", "Corrigibility screen", "Host-owned attestation JSON, no edit controls, containment recovery note.", "\n".join(body))


def screen_settings() -> str:
    body = [chrome("Settings", crumb="Settings", title="Settings", subtitle="Operator machine only. Never store production secrets in this UI.")]
    x, y = CX + 24, CY + 78
    fields = [
        ("Control plane base URL", "http://127.0.0.1:18080"),
        ("Poll interval", "15 seconds"),
        ("Default actor", "host_service"),
        ("Default dry-run", "ON"),
        ("Known agent IDs", "casops.template.baseline_safe"),
    ]
    body.append(r(x, y, 1024, 420, WHITE, rx=16, stroke=STONE_200))
    for i, (label, value) in enumerate(fields):
        yy = y + 28 + i * 64
        body += [
            t(x + 24, yy + 8, label, size=12, fill=STONE_400, weight=600),
            r(x + 24, yy + 16, 640, 32, STONE_50, rx=8, stroke=STONE_200),
            t(x + 36, yy + 37, value, size=13, fill=STONE_800),
        ]
    body += [
        r(x + 24, y + 348, 976, 48, AMBER_50, rx=10, stroke=AMBER_200),
        t(x + 40, y + 378, "Never store production secrets, host Ed25519 keys, or AWS credentials in this UI.", size=12, fill=AMBER_700, weight=600),
    ]
    return wrap("settings", "Settings screen", "Base URL, poll interval, default actor and dry-run, known agent IDs, secrets warning.", "\n".join(body))


def screen_shell() -> str:
    """Dedicated shell chrome annotation (section 5)."""
    body = [chrome("Fleet", crumb="Shell", title="Shell frame", subtitle="Sticky nav, agent switcher, Live pill, actor strip. Content area is a placeholder.")]
    x, y = CX + 24, CY + 90
    body += [
        r(x, y, 1024, 280, STONE_50, rx=16, stroke=STONE_200),
        t(x + 32, y + 48, "This frame is shared by every agent screen.", size=16, fill=STONE_900, weight=600),
        t(x + 32, y + 80, "Top: caso mark · agent switcher · Live pill · as_of", size=13, fill=STONE_700),
        t(x + 32, y + 104, "Strip: actor · reason · expected-parent · dry-run ON (default)", size=13, fill=STONE_700),
        t(x + 32, y + 128, "Left: 16 destinations with indigo rail on the selected item", size=13, fill=STONE_700),
        t(x + 32, y + 168, "Stale projection disables primary mutations (Stale — Refresh First).", size=13, fill=STONE_500),
        t(x + 32, y + 192, "agent_runtime hides Approve. Empty reason disables POST/DELETE.", size=13, fill=STONE_500),
    ]
    return wrap("shell", "App shell", "Shared Control UI chrome: top nav, left nav, mutation contract strip.", "\n".join(body))


SCREENS = [
    ("00-shell.svg", screen_shell),
    ("01-fleet.svg", screen_fleet),
    ("02-overview.svg", screen_overview),
    ("03-structure.svg", screen_structure),
    ("04-compose.svg", screen_compose),
    ("05-run.svg", screen_run),
    ("06-trace.svg", screen_trace),
    ("07-capabilities.svg", screen_capabilities),
    ("08-protocols.svg", screen_protocols),
    ("09-memory.svg", screen_memory),
    ("10-plugins.svg", screen_plugins),
    ("11-cache.svg", screen_cache),
    ("12-safety.svg", screen_safety),
    ("13-improvement.svg", screen_improvement),
    ("14-validation.svg", screen_validation),
    ("15-corrigibility.svg", screen_corrigibility),
    ("16-settings.svg", screen_settings),
]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in SCREENS:
        path = OUT / name
        path.write_text(fn(), encoding="utf-8")
        print(f"wrote {path.relative_to(REPO)}")


if __name__ == "__main__":
    main()
