#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import ASSETS_DIR, load_json


def load_profile(template_id: str) -> dict:
    catalog = load_json(ASSETS_DIR / "reference-docx" / "template-catalog.json")
    for item in catalog["templates"]:
        if item["id"] == template_id:
            return load_json(ASSETS_DIR / "reference-docx" / item["profile"])
    raise KeyError(f"Unknown template: {template_id}")


def patch_profile(profile: dict, overrides: dict[str, str]) -> dict:
    patched = json.loads(json.dumps(profile))
    if overrides.get("font"):
        patched["body"]["font_zh"] = overrides["font"]
        patched["body"]["font_en"] = overrides["font"]
    if overrides.get("font_size"):
        patched["body"]["size_pt"] = float(overrides["font_size"])
    if overrides.get("margin_cm"):
        patched["page"]["margin_cm"] = float(overrides["margin_cm"])
    return patched


def generate_docx(profile: dict, output: Path) -> None:
    try:
        from docx import Document
        from docx.enum.style import WD_STYLE_TYPE
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        from docx.oxml import OxmlElement
        from docx.oxml.ns import qn
        from docx.shared import Cm, Pt
    except ImportError as exc:
        raise RuntimeError("python-docx is required to generate reference.docx templates") from exc

    def ensure_child(parent, tag: str):
        child = parent.find(qn(tag))
        if child is None:
            child = OxmlElement(tag)
            parent.append(child)
        return child

    def set_style_fonts(style, font_zh: str, font_en: str) -> None:
        style.font.name = font_en
        r_pr = style.element.get_or_add_rPr()
        r_fonts = ensure_child(r_pr, "w:rFonts")
        for key in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
            if qn(key) in r_fonts.attrib:
                del r_fonts.attrib[qn(key)]
        r_fonts.set(qn("w:ascii"), font_en)
        r_fonts.set(qn("w:hAnsi"), font_en)
        r_fonts.set(qn("w:cs"), font_en)
        r_fonts.set(qn("w:eastAsia"), font_zh)

    def set_spacing(style, line_spacing: float, space_before_pt: float, space_after_pt: float, align: str | None = None) -> None:
        style.paragraph_format.line_spacing = line_spacing
        style.paragraph_format.space_before = Pt(space_before_pt)
        style.paragraph_format.space_after = Pt(space_after_pt)
        if align == "center":
            style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif align == "left":
            style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif align == "justify":
            style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    def ensure_paragraph_style(document, name: str, base_name: str | None = None):
        try:
            style = document.styles[name]
        except KeyError:
            style = document.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        if base_name:
            try:
                style.base_style = document.styles[base_name]
            except KeyError:
                pass
        return style

    def configure_body_style(style, font_zh: str, font_en: str, size_pt: float, line_spacing: float, space_after_pt: float) -> None:
        set_style_fonts(style, font_zh, font_en)
        style.font.size = Pt(size_pt)
        set_spacing(style, line_spacing, 0, space_after_pt, align="justify")
        style.paragraph_format.first_line_indent = Pt(21)

    def configure_heading_style(style, font_zh: str, font_en: str, size_pt: float, bold: bool, space_before_pt: float, space_after_pt: float) -> None:
        set_style_fonts(style, font_zh, font_en)
        style.font.size = Pt(size_pt)
        style.font.bold = bold
        set_spacing(style, float(profile["body"]["line_spacing"]), space_before_pt, space_after_pt)

    def configure_caption_style(style, font_zh: str, font_en: str, size_pt: float, line_spacing: float) -> None:
        set_style_fonts(style, font_zh, font_en)
        style.font.size = Pt(size_pt)
        style.font.bold = False
        style.font.italic = False
        r_pr = style.element.get_or_add_rPr()
        for tag in ("w:i", "w:iCs"):
            node = r_pr.find(qn(tag))
            if node is not None:
                r_pr.remove(node)
        set_spacing(style, line_spacing, 6, 6, align="center")
        style.paragraph_format.first_line_indent = Pt(0)

    def configure_title_style(style, font_zh: str, font_en: str) -> None:
        set_style_fonts(style, font_zh, font_en)
        style.font.size = Pt(26)
        style.font.bold = False
        style.font.italic = False
        set_spacing(style, 1.15, 0, 12, align="left")
        style.paragraph_format.first_line_indent = Pt(0)
        r_pr = style.element.get_or_add_rPr()
        for tag in ("w:i", "w:iCs"):
            node = r_pr.find(qn(tag))
            if node is not None:
                r_pr.remove(node)
        color = ensure_child(r_pr, "w:color")
        color.set(qn("w:val"), "000000")
        p_pr = style.element.get_or_add_pPr()
        p_bdr = p_pr.find(qn("w:pBdr"))
        if p_bdr is not None:
            p_pr.remove(p_bdr)

    def configure_doc_defaults(document, font_zh: str, font_en: str, size_pt: float, line_spacing: float, space_after_pt: float) -> None:
        styles_element = document.styles.element
        doc_defaults = ensure_child(styles_element, "w:docDefaults")
        r_pr_default = ensure_child(doc_defaults, "w:rPrDefault")
        r_pr = ensure_child(r_pr_default, "w:rPr")
        r_fonts = ensure_child(r_pr, "w:rFonts")
        for key in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
            if qn(key) in r_fonts.attrib:
                del r_fonts.attrib[qn(key)]
        r_fonts.set(qn("w:ascii"), font_en)
        r_fonts.set(qn("w:hAnsi"), font_en)
        r_fonts.set(qn("w:cs"), font_en)
        r_fonts.set(qn("w:eastAsia"), font_zh)
        sz = ensure_child(r_pr, "w:sz")
        sz.set(qn("w:val"), str(int(size_pt * 2)))
        sz_cs = ensure_child(r_pr, "w:szCs")
        sz_cs.set(qn("w:val"), str(int(size_pt * 2)))
        lang = ensure_child(r_pr, "w:lang")
        lang.set(qn("w:val"), "en-US")
        lang.set(qn("w:eastAsia"), "zh-CN")
        p_pr_default = ensure_child(doc_defaults, "w:pPrDefault")
        p_pr = ensure_child(p_pr_default, "w:pPr")
        spacing = ensure_child(p_pr, "w:spacing")
        spacing.set(qn("w:before"), "0")
        spacing.set(qn("w:after"), str(int(space_after_pt * 20)))
        spacing.set(qn("w:line"), str(int(line_spacing * 240)))
        spacing.set(qn("w:lineRule"), "auto")

    document = Document()
    section = document.sections[0]
    margin_cm = float(profile["page"]["margin_cm"])
    section.top_margin = Cm(margin_cm)
    section.bottom_margin = Cm(margin_cm)
    section.left_margin = Cm(margin_cm)
    section.right_margin = Cm(margin_cm)

    body = profile["body"]
    configure_doc_defaults(
        document,
        body["font_zh"],
        body["font_en"],
        float(body["size_pt"]),
        float(body["line_spacing"]),
        float(body["space_after_pt"]),
    )

    normal = document.styles["Normal"]
    configure_body_style(
        normal,
        body["font_zh"],
        body["font_en"],
        float(body["size_pt"]),
        float(body["line_spacing"]),
        float(body["space_after_pt"]),
    )

    for style_name, base_name in (("Body Text", "Normal"), ("First Paragraph", "Body Text"), ("Compact", "Body Text")):
        style = ensure_paragraph_style(document, style_name, base_name)
        configure_body_style(
            style,
            body["font_zh"],
            body["font_en"],
            float(body["size_pt"]),
            float(body["line_spacing"]),
            0 if style_name == "Compact" else float(body["space_after_pt"]),
        )
        if style_name == "Compact":
            style.paragraph_format.first_line_indent = Pt(0)

    for style_name, heading_name in (("heading1", "Heading 1"), ("heading2", "Heading 2"), ("heading3", "Heading 3")):
        style = document.styles[heading_name]
        config = profile["headings"][style_name]
        configure_heading_style(
            style,
            config["font_zh"],
            config["font_en"],
            float(config["size_pt"]),
            bool(config["bold"]),
            float(config["space_before_pt"]),
            float(config["space_after_pt"]),
        )
        style.paragraph_format.first_line_indent = Pt(0)

    configure_title_style(document.styles["Title"], body["font_zh"], body["font_en"])

    for style_name, base_name in (("Caption", "Body Text"), ("Table Caption", "Caption"), ("Image Caption", "Caption")):
        style = ensure_paragraph_style(document, style_name, base_name)
        configure_caption_style(
            style,
            body["font_zh"],
            body["font_en"],
            float(body["size_pt"]),
            float(body["line_spacing"]),
        )

    document.save(output)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate or patch a reference.docx file from a built-in template profile.")
    parser.add_argument("--template", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--font")
    parser.add_argument("--font-size")
    parser.add_argument("--margin-cm")
    parser.add_argument("--dump-json", action="store_true")
    args = parser.parse_args()
    profile = load_profile(args.template)
    patched = patch_profile(profile, {"font": args.font or "", "font_size": args.font_size or "", "margin_cm": args.margin_cm or ""})
    if args.dump_json:
        print(json.dumps(patched, ensure_ascii=False, indent=2))
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    generate_docx(patched, args.output)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
