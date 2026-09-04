from __future__ import annotations

import glob
import os
import xml.etree.ElementTree as ET


SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


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


def _q(tag: str) -> str:
    return f"{{{SVG_NS}}}{tag}"


def _find_first_background_rect(svg: ET.Element) -> ET.Element | None:
    for el in svg.findall(_q("rect")):
        if el.get("width") == "1400" and el.get("height") == "740" and el.get("x") in (None, "0"):
            return el
    return None


def _ensure_defs(svg: ET.Element) -> ET.Element:
    defs = svg.find(_q("defs"))
    if defs is None:
        defs = ET.Element(_q("defs"))
        svg.insert(0, defs)
    return defs


def _add_or_replace(defs: ET.Element, element: ET.Element) -> None:
    element_id = element.get("id")
    if element_id:
        for existing in list(defs):
            if existing.get("id") == element_id:
                defs.remove(existing)
    defs.append(element)


def _make_linear_gradient(grad_id: str, stops: list[tuple[str, str]]) -> ET.Element:
    lg = ET.Element(
        _q("linearGradient"),
        {
            "id": grad_id,
            "x1": "0",
            "y1": "0",
            "x2": "1",
            "y2": "1",
        },
    )
    for offset, color in stops:
        stop = ET.SubElement(lg, _q("stop"), {"offset": offset, "stop-color": color})
        _ = stop
    return lg


def _make_drop_shadow(filter_id: str, dy: str, std: str, opacity: str) -> ET.Element:
    flt = ET.Element(
        _q("filter"),
        {
            "id": filter_id,
            "x": "-20%",
            "y": "-20%",
            "width": "140%",
            "height": "140%",
        },
    )
    ET.SubElement(
        flt,
        _q("feDropShadow"),
        {
            "dx": "0",
            "dy": dy,
            "stdDeviation": std,
            "flood-color": "#0F172A",
            "flood-opacity": opacity,
        },
    )
    return flt


def enhance_svg(path: str) -> None:
    tree = ET.parse(path)
    svg = tree.getroot()

    defs = _ensure_defs(svg)
    _add_or_replace(
        defs,
        _make_linear_gradient(
            "bg",
            [
                ("0%", "#F8FAFC"),
                ("55%", "#EEF2FF"),
                ("100%", "#ECFEFF"),
            ],
        ),
    )
    _add_or_replace(defs, _make_drop_shadow("cardShadow", dy="10", std="12", opacity="0.14"))
    _add_or_replace(defs, _make_drop_shadow("softShadow", dy="6", std="8", opacity="0.12"))
    _add_or_replace(
        defs,
        _make_linear_gradient(
            "crewBg",
            [
                ("0%", "#F8FAFC"),
                ("100%", "#EEF2FF"),
            ],
        ),
    )
    _add_or_replace(
        defs,
        _make_linear_gradient(
            "footerBg",
            [
                ("0%", "#FFFBEB"),
                ("100%", "#FFF7ED"),
            ],
        ),
    )

    bg_rect = _find_first_background_rect(svg)
    if bg_rect is not None:
        bg_rect.set("fill", "url(#bg)")

        insert_at = list(svg).index(bg_rect) + 1
        decor = ET.Element(_q("g"), {"opacity": "0.9"})
        ET.SubElement(
            decor,
            _q("circle"),
            {"cx": "1180", "cy": "135", "r": "210", "fill": "#6366F1", "fill-opacity": "0.08"},
        )
        ET.SubElement(
            decor,
            _q("circle"),
            {"cx": "260", "cy": "160", "r": "250", "fill": "#22C55E", "fill-opacity": "0.06"},
        )
        ET.SubElement(
            decor,
            _q("circle"),
            {"cx": "1045", "cy": "640", "r": "280", "fill": "#06B6D4", "fill-opacity": "0.06"},
        )
        ET.SubElement(
            decor,
            _q("rect"),
            {"x": "0", "y": "0", "width": "1400", "height": "220", "fill": "#FFFFFF", "opacity": "0.50"},
        )
        svg.insert(insert_at, decor)

    phase_colors: set[str] = set()
    for el in svg.iter():
        if el.get("fill") and el.get("fill").startswith("#"):
            if el.tag == _q("path"):
                phase_colors.add(el.get("fill"))

    for color in sorted(phase_colors):
        grad_id = f"phase{color[1:]}"
        _add_or_replace(
            defs,
            _make_linear_gradient(
                grad_id,
                [
                    ("0%", _lighten(color, 0.10)),
                    ("60%", color.upper()),
                    ("100%", _darken(color, 0.18)),
                ],
            ),
        )

    for el in svg.iter():
        if el.tag == _q("path") and el.get("fill") in phase_colors:
            el.set("fill", f"url(#phase{el.get('fill')[1:]})")

    for el in svg.findall(_q("rect")):
        if el.get("x") and el.get("y") and el.get("width") and el.get("height"):
            if el.get("y") == "80" and el.get("width") == "218" and el.get("height") == "555":
                el.set("filter", "url(#cardShadow)")
                if el.get("stroke") is None:
                    el.set("stroke", "#E2E8F0")
            if el.get("y") == "445" and el.get("width") == "198" and el.get("height") == "180":
                el.set("fill", "url(#crewBg)")
                el.set("stroke", "#E2E8F0")
            if el.get("y") == "660" and el.get("width") == "1350" and el.get("height") == "60":
                el.set("fill", "url(#footerBg)")
                el.set("filter", "url(#softShadow)")
                el.set("stroke", "#FED7AA")

    for el in svg.findall(_q("polygon")):
        if el.get("fill") == "#94A3B8":
            el.set("fill", "#64748B")
            el.set("opacity", "0.75")

    svg.set("shape-rendering", "geometricPrecision")
    svg.set("text-rendering", "geometricPrecision")

    ET.indent(tree, space="  ", level=0)
    tree.write(path, encoding="utf-8", xml_declaration=False)


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    for file_path in sorted(glob.glob(os.path.join(here, "*.svg"))):
        enhance_svg(file_path)


if __name__ == "__main__":
    main()

