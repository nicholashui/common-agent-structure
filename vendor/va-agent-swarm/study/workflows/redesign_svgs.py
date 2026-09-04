from __future__ import annotations

import glob
import os
import re
import xml.etree.ElementTree as ET


SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


PHASES: list[tuple[str, str]] = [
    ("CONCEPT", "#6366F1"),
    ("PRODUCTION", "#2563EB"),
    ("POST-PRODUCTION", "#0891B2"),
    ("REVIEW & QA", "#16A34A"),
    ("DISTRIBUTION", "#D97706"),
    ("POST-LAUNCH", "#DC2626"),
]


def _q(tag: str) -> str:
    return f"{{{SVG_NS}}}{tag}"


def _t(el: ET.Element) -> str:
    s = (el.text or "").strip()
    prev = None
    while s != prev:
        prev = s
        s = (
            s.replace("&amp;", "&")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&quot;", '"')
            .replace("&apos;", "'")
        )
    return s


def _f(el: ET.Element, key: str, default: float = 0.0) -> float:
    v = el.get(key)
    if v is None:
        return default
    try:
        return float(v)
    except ValueError:
        return default


def _hex_to_rgb(color: str) -> tuple[int, int, int]:
    c = color.strip()
    if c.startswith("#"):
        c = c[1:]
    if len(c) == 3:
        c = "".join(ch * 2 for ch in c)
    return int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)


def _rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    r, g, b = (max(0, min(255, int(v))) for v in rgb)
    return f"#{r:02X}{g:02X}{b:02X}"


def _mix(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    return (
        int(a[0] + (b[0] - a[0]) * t),
        int(a[1] + (b[1] - a[1]) * t),
        int(a[2] + (b[2] - a[2]) * t),
    )


def _lighten(color: str, t: float) -> str:
    return _rgb_to_hex(_mix(_hex_to_rgb(color), (255, 255, 255), t))


def _darken(color: str, t: float) -> str:
    return _rgb_to_hex(_mix(_hex_to_rgb(color), (0, 0, 0), t))


def _phase_anchor_x(i: int) -> float:
    return 40.0 + i * 228.0


def _read_svg_root(svg_path: str) -> ET.Element:
    with open(svg_path, "r", encoding="utf-8") as f:
        s = f.read()
    s = s.replace(
        'xmlns="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg"',
        'xmlns="http://www.w3.org/2000/svg"',
    )
    s = re.sub(
        r'(<svg\b[^>]*?)\s+xmlns="http://www\.w3\.org/2000/svg"\s+xmlns="http://www\.w3\.org/2000/svg"',
        r'\1 xmlns="http://www.w3.org/2000/svg"',
        s,
        flags=re.IGNORECASE,
    )
    return ET.fromstring(s)


def _extract_workflow(src_svg_path: str) -> dict:
    root = _read_svg_root(src_svg_path)
    texts = [el for el in root.iter() if el.tag == _q("text")]

    title = ""
    meta = ""
    critic = ""
    critic_sub = ""

    top_texts: list[tuple[float, float, str]] = []
    bottom_texts: list[tuple[float, float, str]] = []
    for el in texts:
        s = _t(el)
        if not s:
            continue
        x = _f(el, "x", -1)
        y = _f(el, "y", -1)
        if y <= 120:
            top_texts.append((y, x, s))
        if y >= 640:
            bottom_texts.append((y, x, s))

    for _, _, s in sorted(top_texts):
        if s.startswith("Workflow ") and "—" in s:
            title = s
            break
    if not title:
        for el in texts:
            if el.get("x") == "30" and el.get("y") == "38":
                title = _t(el)
                break

    top_other = [t for t in top_texts if t[2] != title]
    if top_other:
        meta = sorted(top_other)[0][2]
    if not meta:
        for el in texts:
            if el.get("x") == "30" and el.get("y") == "60":
                meta = _t(el)
                break

    bt = [t for t in bottom_texts if t[2] != "CRITIC LOOP"]
    bt_sorted = sorted(bt)
    if len(bt_sorted) >= 2:
        critic = bt_sorted[0][2]
        critic_sub = bt_sorted[1][2]
    if not critic:
        for el in texts:
            if el.get("x") == "135" and el.get("y") == "682":
                critic = _t(el)
                break
    if not critic_sub:
        for el in texts:
            if el.get("x") == "135" and el.get("y") == "702":
                critic_sub = _t(el)
                break

    phase_boxes: list[dict] = []
    for el in root.iter():
        if el.tag != _q("rect"):
            continue
        dash = (el.get("stroke-dasharray") or "").strip()
        if not dash:
            continue
        if el.get("rx") != "18":
            continue
        w = _f(el, "width", 0)
        h = _f(el, "height", 0)
        if w < 320 or h < 180:
            continue
        phase_boxes.append(
            {
                "x": _f(el, "x", 0),
                "y": _f(el, "y", 0),
                "w": w,
                "h": h,
            }
        )
    phase_boxes = sorted(phase_boxes, key=lambda b: (b["y"], b["x"]))[:6]

    phases: list[dict] = []
    if len(phase_boxes) == 6:
        for i in range(6):
            b = phase_boxes[i]
            steps: list[str] = []
            crew: list[str] = []
            for el in texts:
                s = _t(el)
                if not s or not s.startswith("•"):
                    continue
                x = _f(el, "x", -1)
                y = _f(el, "y", -1)
                if not (b["x"] <= x <= b["x"] + b["w"] and b["y"] <= y <= b["y"] + b["h"]):
                    continue
                s = s.lstrip("•").strip()
                if y < b["y"] + 160.0:
                    steps.append(s)
                else:
                    crew.append(s)

            def _clean(lines: list[str]) -> list[str]:
                out: list[str] = []
                for line in lines:
                    if line and line not in out:
                        out.append(line)
                return out

            phases.append({"name": PHASES[i][0], "color": PHASES[i][1], "steps": _clean(steps), "crew": _clean(crew)})
    else:
        for i in range(6):
            ax = _phase_anchor_x(i)
            steps = []
            crew = []
            for el in texts:
                x = _f(el, "x", -1)
                if abs(x - ax) > 2.0:
                    continue
                y = _f(el, "y", -1)
                s = _t(el)
                if not s:
                    continue
                if 170.0 <= y <= 420.0:
                    if s.startswith("•"):
                        s = s.lstrip("•").strip()
                    steps.append(s)
                if 470.0 <= y <= 640.0:
                    if s.startswith("•"):
                        s = s.lstrip("•").strip()
                    crew.append(s)

            def _clean(lines: list[str]) -> list[str]:
                out: list[str] = []
                for line in lines:
                    if line and line not in out:
                        out.append(line)
                return out

            phases.append({"name": PHASES[i][0], "color": PHASES[i][1], "steps": _clean(steps), "crew": _clean(crew)})

    return {
        "title": title,
        "meta": meta,
        "critic": critic,
        "critic_sub": critic_sub,
        "phases": phases,
    }


def _svg_el(tag: str, attrs: dict[str, str] | None = None, text: str | None = None) -> ET.Element:
    el = ET.Element(_q(tag), attrs or {})
    if text is not None:
        el.text = text
    return el


def _sub(el: ET.Element, tag: str, attrs: dict[str, str] | None = None, text: str | None = None) -> ET.Element:
    child = ET.SubElement(el, _q(tag), attrs or {})
    if text is not None:
        child.text = text
    return child


def _add_defs(svg: ET.Element) -> None:
    defs = _sub(svg, "defs")

    bg = _sub(defs, "linearGradient", {"id": "bg", "x1": "0", "y1": "0", "x2": "1", "y2": "1"})
    _sub(bg, "stop", {"offset": "0%", "stop-color": "#BFD2EA"})
    _sub(bg, "stop", {"offset": "55%", "stop-color": "#B8CAE6"})
    _sub(bg, "stop", {"offset": "100%", "stop-color": "#B1C5E3"})

    fog = _sub(defs, "linearGradient", {"id": "fog", "x1": "0", "y1": "0", "x2": "0", "y2": "1"})
    _sub(fog, "stop", {"offset": "0%", "stop-color": "#FFFFFF", "stop-opacity": "0.55"})
    _sub(fog, "stop", {"offset": "100%", "stop-color": "#FFFFFF", "stop-opacity": "0.0"})

    flt = _sub(
        defs,
        "filter",
        {
            "id": "softShadow",
            "x": "-20%",
            "y": "-20%",
            "width": "140%",
            "height": "140%",
        },
    )
    _sub(
        flt,
        "feDropShadow",
        {
            "dx": "0",
            "dy": "8",
            "stdDeviation": "10",
            "flood-color": "#0F172A",
            "flood-opacity": "0.18",
        },
    )

    mark = _sub(
        defs,
        "marker",
        {
            "id": "arrow",
            "viewBox": "0 0 10 10",
            "refX": "10",
            "refY": "5",
            "markerWidth": "7",
            "markerHeight": "7",
            "orient": "auto-start-reverse",
        },
    )
    _sub(mark, "path", {"d": "M 0 0 L 10 5 L 0 10 z", "fill": "#FFFFFF", "fill-opacity": "0.9"})


def _add_phase_gradients(svg: ET.Element) -> None:
    defs = svg.find(_q("defs"))
    if defs is None:
        return
    for name, color in PHASES:
        gid = "p" + re.sub(r"[^A-Za-z0-9]+", "", name).lower()
        lg = _sub(defs, "linearGradient", {"id": gid, "x1": "0", "y1": "0", "x2": "1", "y2": "1"})
        _sub(lg, "stop", {"offset": "0%", "stop-color": _lighten(color, 0.18)})
        _sub(lg, "stop", {"offset": "60%", "stop-color": color})
        _sub(lg, "stop", {"offset": "100%", "stop-color": _darken(color, 0.22)})


def _phase_gid(phase_name: str) -> str:
    return "p" + re.sub(r"[^A-Za-z0-9]+", "", phase_name).lower()


def _icon_camera(g: ET.Element, x: float, y: float, s: float, accent: str) -> None:
    _sub(g, "rect", {"x": f"{x}", "y": f"{y+12*s}", "width": f"{72*s}", "height": f"{44*s}", "rx": f"{10*s}", "fill": "#0F172A", "fill-opacity": "0.18"})
    _sub(g, "rect", {"x": f"{x+8*s}", "y": f"{y+18*s}", "width": f"{56*s}", "height": f"{34*s}", "rx": f"{9*s}", "fill": "#FFFFFF", "fill-opacity": "0.92"})
    _sub(g, "circle", {"cx": f"{x+30*s}", "cy": f"{y+35*s}", "r": f"{10*s}", "fill": accent, "fill-opacity": "0.95"})
    _sub(g, "circle", {"cx": f"{x+30*s}", "cy": f"{y+35*s}", "r": f"{5.5*s}", "fill": "#FFFFFF", "fill-opacity": "0.85"})
    _sub(g, "path", {"d": f"M {x+64*s} {y+24*s} L {x+86*s} {y+16*s} L {x+86*s} {y+52*s} L {x+64*s} {y+44*s} Z", "fill": "#FFFFFF", "fill-opacity": "0.92"})


def _icon_clapper(g: ET.Element, x: float, y: float, s: float, accent: str) -> None:
    _sub(g, "rect", {"x": f"{x}", "y": f"{y+22*s}", "width": f"{82*s}", "height": f"{48*s}", "rx": f"{10*s}", "fill": "#FFFFFF", "fill-opacity": "0.92"})
    _sub(g, "rect", {"x": f"{x}", "y": f"{y+10*s}", "width": f"{82*s}", "height": f"{20*s}", "rx": f"{10*s}", "fill": "#0F172A", "fill-opacity": "0.22"})
    for i in range(6):
        _sub(
            g,
            "path",
            {
                "d": f"M {x+6*s+i*12*s} {y+12*s} l {10*s} {16*s}",
                "stroke": "#FFFFFF",
                "stroke-width": f"{3*s}",
                "opacity": "0.75",
            },
        )
    _sub(g, "rect", {"x": f"{x+10*s}", "y": f"{y+34*s}", "width": f"{62*s}", "height": f"{10*s}", "rx": f"{5*s}", "fill": accent, "fill-opacity": "0.85"})


def _icon_wand(g: ET.Element, x: float, y: float, s: float, accent: str) -> None:
    _sub(g, "path", {"d": f"M {x+10*s} {y+70*s} L {x+72*s} {y+10*s}", "stroke": "#FFFFFF", "stroke-width": f"{10*s}", "stroke-linecap": "round", "opacity": "0.9"})
    _sub(g, "path", {"d": f"M {x+10*s} {y+70*s} L {x+72*s} {y+10*s}", "stroke": accent, "stroke-width": f"{5*s}", "stroke-linecap": "round", "opacity": "0.9"})
    _sub(g, "circle", {"cx": f"{x+72*s}", "cy": f"{y+10*s}", "r": f"{6*s}", "fill": "#FFFFFF", "fill-opacity": "0.95"})
    _sub(g, "circle", {"cx": f"{x+72*s}", "cy": f"{y+10*s}", "r": f"{3*s}", "fill": accent, "fill-opacity": "0.95"})
    for dx, dy, r in [(0, 0, 12), (-20, 20, 8), (18, 18, 7)]:
        _sub(
            g,
            "circle",
            {
                "cx": f"{x+72*s+dx*s}",
                "cy": f"{y+10*s+dy*s}",
                "r": f"{r*s*0.5}",
                "fill": "#FFFFFF",
                "fill-opacity": "0.75",
            },
        )


def _icon_check(g: ET.Element, x: float, y: float, s: float, accent: str) -> None:
    _sub(g, "circle", {"cx": f"{x+42*s}", "cy": f"{y+40*s}", "r": f"{30*s}", "fill": "#FFFFFF", "fill-opacity": "0.9"})
    _sub(g, "circle", {"cx": f"{x+42*s}", "cy": f"{y+40*s}", "r": f"{30*s}", "fill": accent, "fill-opacity": "0.18"})
    _sub(
        g,
        "path",
        {
            "d": f"M {x+28*s} {y+40*s} L {x+38*s} {y+50*s} L {x+58*s} {y+28*s}",
            "stroke": accent,
            "stroke-width": f"{7*s}",
            "stroke-linecap": "round",
            "stroke-linejoin": "round",
            "fill": "none",
        },
    )


def _icon_rocket(g: ET.Element, x: float, y: float, s: float, accent: str) -> None:
    _sub(
        g,
        "path",
        {
            "d": f"M {x+42*s} {y+10*s} C {x+62*s} {y+26*s}, {x+66*s} {y+52*s}, {x+42*s} {y+72*s} C {x+18*s} {y+52*s}, {x+22*s} {y+26*s}, {x+42*s} {y+10*s} Z",
            "fill": "#FFFFFF",
            "fill-opacity": "0.92",
        },
    )
    _sub(g, "circle", {"cx": f"{x+42*s}", "cy": f"{y+40*s}", "r": f"{9*s}", "fill": accent, "fill-opacity": "0.9"})
    _sub(g, "circle", {"cx": f"{x+42*s}", "cy": f"{y+40*s}", "r": f"{4*s}", "fill": "#FFFFFF", "fill-opacity": "0.85"})
    _sub(g, "path", {"d": f"M {x+42*s} {y+72*s} L {x+34*s} {y+86*s} L {x+42*s} {y+82*s} L {x+50*s} {y+86*s} Z", "fill": accent, "fill-opacity": "0.85"})
    _sub(g, "path", {"d": f"M {x+42*s} {y+86*s} C {x+38*s} {y+98*s}, {x+46*s} {y+98*s}, {x+42*s} {y+110*s}", "stroke": "#FFFFFF", "stroke-width": f"{6*s}", "stroke-linecap": "round", "opacity": "0.55"})


def _icon_reel(g: ET.Element, x: float, y: float, s: float, accent: str) -> None:
    _sub(g, "circle", {"cx": f"{x+42*s}", "cy": f"{y+42*s}", "r": f"{32*s}", "fill": "#FFFFFF", "fill-opacity": "0.9"})
    _sub(g, "circle", {"cx": f"{x+42*s}", "cy": f"{y+42*s}", "r": f"{32*s}", "fill": accent, "fill-opacity": "0.16"})
    _sub(g, "circle", {"cx": f"{x+42*s}", "cy": f"{y+42*s}", "r": f"{8*s}", "fill": accent, "fill-opacity": "0.9"})
    for a in [(42, 22), (60, 42), (42, 62), (24, 42)]:
        _sub(g, "circle", {"cx": f"{x+a[0]*s/1}", "cy": f"{y+a[1]*s/1}", "r": f"{6*s}", "fill": "#FFFFFF", "fill-opacity": "0.85"})
    _sub(g, "path", {"d": f"M {x+74*s} {y+66*s} C {x+92*s} {y+78*s}, {x+96*s} {y+96*s}, {x+86*s} {y+112*s}", "stroke": "#FFFFFF", "stroke-width": f"{7*s}", "stroke-linecap": "round", "opacity": "0.6", "fill": "none"})


def _add_scene(svg: ET.Element) -> None:
    _sub(svg, "rect", {"x": "0", "y": "0", "width": "1400", "height": "740", "fill": "url(#bg)"})
    _sub(svg, "rect", {"x": "0", "y": "0", "width": "1400", "height": "220", "fill": "url(#fog)"})

    accents = _sub(svg, "g", {"opacity": "0.95"})
    _sub(accents, "circle", {"cx": "170", "cy": "160", "r": "160", "fill": "#FFFFFF", "fill-opacity": "0.14"})
    _sub(accents, "circle", {"cx": "1210", "cy": "140", "r": "200", "fill": "#FFFFFF", "fill-opacity": "0.12"})
    _sub(accents, "circle", {"cx": "1100", "cy": "640", "r": "240", "fill": "#FFFFFF", "fill-opacity": "0.10"})


def _layout_boxes() -> list[dict]:
    box_w = 385.0
    box_h = 225.0
    gap_x = 32.0
    left = 58.0
    top1 = 140.0
    top2 = 410.0
    xs = [left + i * (box_w + gap_x) for i in range(3)]
    ys = [top1, top2]
    out: list[dict] = []
    idx = 0
    for r in range(2):
        for c in range(3):
            out.append({"i": idx, "x": xs[c], "y": ys[r], "w": box_w, "h": box_h})
            idx += 1
    return out


def _add_connectors(svg: ET.Element, boxes: list[dict]) -> None:
    g = _sub(svg, "g", {"opacity": "0.9"})

    def mid_right(b: dict) -> tuple[float, float]:
        return b["x"] + b["w"] + 10.0, b["y"] + b["h"] * 0.5

    def mid_left(b: dict) -> tuple[float, float]:
        return b["x"] - 10.0, b["y"] + b["h"] * 0.5

    def bottom_mid(b: dict) -> tuple[float, float]:
        return b["x"] + b["w"] * 0.5, b["y"] + b["h"] + 10.0

    def top_mid(b: dict) -> tuple[float, float]:
        return b["x"] + b["w"] * 0.5, b["y"] - 10.0

    a, b, c = boxes[0], boxes[1], boxes[2]
    x1, y1 = mid_right(a)
    x2, y2 = mid_left(b)
    _sub(
        g,
        "path",
        {
            "d": f"M {x1} {y1} L {x2} {y2}",
            "stroke": "#FFFFFF",
            "stroke-width": "3",
            "stroke-dasharray": "7 10",
            "fill": "none",
            "marker-end": "url(#arrow)",
        },
    )
    x1, y1 = mid_right(b)
    x2, y2 = mid_left(c)
    _sub(
        g,
        "path",
        {
            "d": f"M {x1} {y1} L {x2} {y2}",
            "stroke": "#FFFFFF",
            "stroke-width": "3",
            "stroke-dasharray": "7 10",
            "fill": "none",
            "marker-end": "url(#arrow)",
        },
    )

    d, e, f = boxes[3], boxes[4], boxes[5]
    x1, y1 = mid_right(d)
    x2, y2 = mid_left(e)
    _sub(
        g,
        "path",
        {
            "d": f"M {x1} {y1} L {x2} {y2}",
            "stroke": "#FFFFFF",
            "stroke-width": "3",
            "stroke-dasharray": "7 10",
            "fill": "none",
            "marker-end": "url(#arrow)",
        },
    )
    x3, y3 = mid_right(e)
    x4, y4 = mid_left(f)
    _sub(
        g,
        "path",
        {
            "d": f"M {x3} {y3} L {x4} {y4}",
            "stroke": "#FFFFFF",
            "stroke-width": "3",
            "stroke-dasharray": "7 10",
            "fill": "none",
            "marker-end": "url(#arrow)",
        },
    )

    x1, y1 = bottom_mid(c)
    x2, y2 = top_mid(d)
    xm1 = x1 + 120.0
    xm2 = x2 - 120.0
    path3 = f"M {x1} {y1} C {xm1} {y1+70.0} {xm2} {y2-70.0} {x2} {y2}"
    _sub(
        g,
        "path",
        {
            "d": path3,
            "stroke": "#FFFFFF",
            "stroke-width": "3",
            "stroke-dasharray": "7 10",
            "fill": "none",
            "marker-end": "url(#arrow)",
        },
    )


def _add_phase_box(svg: ET.Element, phase: dict, box: dict) -> None:
    x = box["x"]
    y = box["y"]
    w = box["w"]
    h = box["h"]
    name = phase["name"]
    color = phase["color"]
    gid = _phase_gid(name)

    g = _sub(svg, "g", {"filter": "url(#softShadow)"})
    _sub(
        g,
        "rect",
        {
            "x": f"{x}",
            "y": f"{y}",
            "width": f"{w}",
            "height": f"{h}",
            "rx": "18",
            "fill": "#FFFFFF",
            "fill-opacity": "0.10",
            "stroke": "#FFFFFF",
            "stroke-opacity": "0.80",
            "stroke-width": "2.5",
            "stroke-dasharray": "8 10",
        },
    )

    pill_w = min(260.0, w - 40.0)
    pill_x = x + 26.0
    pill_y = y - 18.0
    _sub(
        svg,
        "rect",
        {
            "x": f"{pill_x}",
            "y": f"{pill_y}",
            "width": f"{pill_w}",
            "height": "36",
            "rx": "18",
            "fill": "#FFFFFF",
            "fill-opacity": "0.90",
        },
    )
    _sub(
        svg,
        "rect",
        {
            "x": f"{pill_x+10}",
            "y": f"{pill_y+8}",
            "width": "20",
            "height": "20",
            "rx": "10",
            "fill": f"url(#{gid})",
            "opacity": "0.95",
        },
    )
    _sub(
        svg,
        "text",
        {
            "x": f"{pill_x+40}",
            "y": f"{pill_y+24}",
            "font-size": "16",
            "font-weight": "700",
            "fill": "#0F172A",
        },
        name.title(),
    )

    icon = _sub(svg, "g", {})
    ix = x + 20.0
    iy = y + 32.0
    s = 0.9
    if name == "CONCEPT":
        _icon_clapper(icon, ix, iy, s, color)
    elif name == "PRODUCTION":
        _icon_camera(icon, ix, iy, s, color)
    elif name == "POST-PRODUCTION":
        _icon_reel(icon, ix, iy, s, color)
    elif name == "REVIEW & QA":
        _icon_check(icon, ix, iy, s, color)
    elif name == "DISTRIBUTION":
        _icon_rocket(icon, ix, iy, s, color)
    else:
        _icon_wand(icon, ix, iy, s, color)

    tx = x + 125.0
    ty = y + 52.0
    _sub(
        svg,
        "text",
        {
            "x": f"{tx}",
            "y": f"{ty}",
            "font-size": "11",
            "font-weight": "700",
            "letter-spacing": "1",
            "fill": "#FFFFFF",
            "opacity": "0.95",
        },
        "KEY STEPS",
    )
    ty += 20.0
    for sline in phase["steps"][:6]:
        _sub(
            svg,
            "text",
            {
                "x": f"{tx}",
                "y": f"{ty}",
                "font-size": "12.5",
                "fill": "#0F172A",
                "opacity": "0.95",
            },
            "• " + sline,
        )
        ty += 18.0

    crew_y = y + 168.0
    _sub(
        svg,
        "path",
        {
            "d": f"M {tx} {crew_y} H {x+w-24}",
            "stroke": "#FFFFFF",
            "stroke-opacity": "0.55",
            "stroke-width": "1.5",
        },
    )
    _sub(
        svg,
        "text",
        {
            "x": f"{tx}",
            "y": f"{crew_y+22}",
            "font-size": "11",
            "font-weight": "700",
            "letter-spacing": "1",
            "fill": "#FFFFFF",
            "opacity": "0.95",
        },
        "CREW",
    )
    cy = crew_y + 44.0
    for cline in phase["crew"][:4]:
        _sub(
            svg,
            "text",
            {
                "x": f"{tx}",
                "y": f"{cy}",
                "font-size": "12",
                "fill": "#0F172A",
                "opacity": "0.95",
            },
            "• " + cline,
        )
        cy += 16.5


def _add_header(svg: ET.Element, wf: dict) -> None:
    _sub(
        svg,
        "text",
        {"x": "70", "y": "60", "font-size": "26", "font-weight": "800", "fill": "#0F172A"},
        wf["title"],
    )
    _sub(
        svg,
        "text",
        {"x": "70", "y": "86", "font-size": "14", "fill": "#0F172A", "opacity": "0.75"},
        wf["meta"],
    )


def _add_critic(svg: ET.Element, wf: dict) -> None:
    x = 70.0
    y = 675.0
    w = 1260.0
    h = 50.0
    _sub(
        svg,
        "rect",
        {
            "x": f"{x}",
            "y": f"{y}",
            "width": f"{w}",
            "height": f"{h}",
            "rx": "18",
            "fill": "#FFFFFF",
            "fill-opacity": "0.18",
            "stroke": "#FFFFFF",
            "stroke-opacity": "0.55",
            "stroke-width": "2",
            "filter": "url(#softShadow)",
        },
    )
    _sub(
        svg,
        "text",
        {
            "x": f"{x+20}",
            "y": f"{y+22}",
            "font-size": "11",
            "font-weight": "800",
            "letter-spacing": "1",
            "fill": "#FFFFFF",
            "opacity": "0.95",
        },
        "CRITIC LOOP",
    )
    _sub(
        svg,
        "text",
        {"x": f"{x+150}", "y": f"{y+22}", "font-size": "13", "fill": "#0F172A", "opacity": "0.92"},
        wf["critic"],
    )
    _sub(
        svg,
        "text",
        {"x": f"{x+150}", "y": f"{y+40}", "font-size": "12", "fill": "#0F172A", "opacity": "0.80"},
        wf["critic_sub"],
    )


def build_svg(wf: dict) -> str:
    svg = _svg_el(
        "svg",
        {
            "viewBox": "0 0 1400 740",
            "font-family": "Segoe UI, Arial, sans-serif",
            "shape-rendering": "geometricPrecision",
            "text-rendering": "geometricPrecision",
        },
    )
    _add_defs(svg)
    _add_phase_gradients(svg)
    _add_scene(svg)

    _add_header(svg, wf)

    boxes = _layout_boxes()
    _add_connectors(svg, boxes)
    for box in boxes:
        _add_phase_box(svg, wf["phases"][box["i"]], box)

    _add_critic(svg, wf)

    tree = ET.ElementTree(svg)
    ET.indent(tree, space="  ", level=0)
    out = ET.tostring(svg, encoding="unicode")
    out = out.replace("&#10;", "\n")
    return out


def redesign_svg(file_path: str) -> None:
    wf = _extract_workflow(file_path)
    svg_text = build_svg(wf)
    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(svg_text)


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    for file_path in sorted(glob.glob(os.path.join(here, "*.svg"))):
        redesign_svg(file_path)


if __name__ == "__main__":
    main()
