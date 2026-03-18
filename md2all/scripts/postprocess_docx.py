#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from common import ASSETS_DIR, load_json

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
MC_NS = "http://schemas.openxmlformats.org/markup-compatibility/2006"
WP_NS = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
PIC_NS = "http://schemas.openxmlformats.org/drawingml/2006/picture"

ET.register_namespace("w", W_NS)
ET.register_namespace("m", M_NS)
ET.register_namespace("r", R_NS)
ET.register_namespace("mc", MC_NS)
ET.register_namespace("wp", WP_NS)
ET.register_namespace("a", A_NS)
ET.register_namespace("pic", PIC_NS)


def qn(tag: str) -> str:
    prefix, local = tag.split(":")
    namespace = {
        "w": W_NS,
        "m": M_NS,
    }[prefix]
    return f"{{{namespace}}}{local}"


def get_or_add(parent: ET.Element, tag: str) -> ET.Element:
    child = parent.find(qn(tag))
    if child is None:
        child = ET.SubElement(parent, qn(tag))
    return child


def remove_all(parent: ET.Element, tag: str) -> None:
    for child in list(parent.findall(qn(tag))):
        parent.remove(child)


def set_fonts(r_pr: ET.Element, font_zh: str, font_en: str) -> None:
    r_fonts = get_or_add(r_pr, "w:rFonts")
    for key in ("asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme"):
        r_fonts.attrib.pop(qn(f"w:{key}"), None)
    r_fonts.set(qn("w:ascii"), font_en)
    r_fonts.set(qn("w:hAnsi"), font_en)
    r_fonts.set(qn("w:cs"), font_en)
    r_fonts.set(qn("w:eastAsia"), font_zh)


def set_font_size(r_pr: ET.Element, size_pt: float) -> None:
    half_points = str(int(size_pt * 2))
    get_or_add(r_pr, "w:sz").set(qn("w:val"), half_points)
    get_or_add(r_pr, "w:szCs").set(qn("w:val"), half_points)


def set_color(r_pr: ET.Element, value: str) -> None:
    color = get_or_add(r_pr, "w:color")
    color.set(qn("w:val"), value)
    for key in ("themeColor", "themeTint", "themeShade"):
        color.attrib.pop(qn(f"w:{key}"), None)


def remove_child(parent: ET.Element, tag: str) -> None:
    child = parent.find(qn(tag))
    if child is not None:
        parent.remove(child)


def normalize_ppr(paragraph: ET.Element) -> ET.Element:
    ppr_nodes = [child for child in list(paragraph) if child.tag == qn("w:pPr")]
    if ppr_nodes:
        primary = ppr_nodes[0]
        for extra in ppr_nodes[1:]:
            for child in list(extra):
                primary.append(copy.deepcopy(child))
            paragraph.remove(extra)
    else:
        primary = ET.Element(qn("w:pPr"))
        paragraph.insert(0, primary)
    return primary


def get_paragraph_style_id(paragraph: ET.Element) -> str | None:
    for ppr in paragraph.findall(qn("w:pPr")):
        style = ppr.find(qn("w:pStyle"))
        if style is not None:
            return style.get(qn("w:val"))
    return None


def set_paragraph_spacing(ppr: ET.Element, before_pt: float, after_pt: float, line_spacing: float) -> None:
    remove_all(ppr, "w:spacing")
    spacing = get_or_add(ppr, "w:spacing")
    spacing.set(qn("w:before"), str(int(before_pt * 20)))
    spacing.set(qn("w:after"), str(int(after_pt * 20)))
    spacing.set(qn("w:line"), str(int(line_spacing * 240)))
    spacing.set(qn("w:lineRule"), "auto")


def set_paragraph_indent(ppr: ET.Element, first_line_twips: int = 0, first_line_chars: int = 0) -> None:
    remove_all(ppr, "w:ind")
    ind = get_or_add(ppr, "w:ind")
    ind.set(qn("w:firstLine"), str(first_line_twips))
    ind.set(qn("w:firstLineChars"), str(first_line_chars))


def set_paragraph_alignment(ppr: ET.Element, value: str) -> None:
    remove_all(ppr, "w:jc")
    get_or_add(ppr, "w:jc").set(qn("w:val"), value)


def align_to_word(value: str | None) -> str:
    mapping = {
        "left": "left",
        "center": "center",
        "right": "right",
        "justify": "both",
        "both": "both",
    }
    return mapping.get((value or "justify").lower(), "both")


def load_profile(template_id: str | None) -> dict:
    if not template_id:
        return {
            "body": {
                "font_zh": "SimSun",
                "font_en": "Times New Roman",
                "size_pt": 12,
                "line_spacing": 1.5,
                "space_before_pt": 0,
                "space_after_pt": 0,
                "first_line_twips": 420,
                "first_line_chars": 200,
                "align": "justify",
            },
            "headings": {
                "heading1": {"font_zh": "SimSun", "font_en": "Times New Roman", "size_pt": 15, "bold": True, "space_before_pt": 12, "space_after_pt": 6, "line_spacing": 1.5, "align": "left"},
                "heading2": {"font_zh": "SimSun", "font_en": "Times New Roman", "size_pt": 13, "bold": True, "space_before_pt": 12, "space_after_pt": 6, "line_spacing": 1.5, "align": "left"},
                "heading3": {"font_zh": "SimSun", "font_en": "Times New Roman", "size_pt": 12, "bold": True, "space_before_pt": 12, "space_after_pt": 6, "line_spacing": 1.5, "align": "left"},
            },
            "captions": {"font_zh": "SimSun", "font_en": "Times New Roman", "size_pt": 12, "space_before_pt": 6, "space_after_pt": 6, "line_spacing": 1.5, "align": "center"},
        }
    catalog = load_json(ASSETS_DIR / "reference-docx" / "template-catalog.json")
    for item in catalog["templates"]:
        if item["id"] == template_id:
            return load_json(ASSETS_DIR / "reference-docx" / item["profile"])
    raise KeyError(f"Unknown template: {template_id}")


def patch_style(styles_root: ET.Element, style_id: str, *, font_zh: str, font_en: str, size_pt: float | None = None,
                bold: bool | None = None, italic: bool | None = None, color: str | None = None,
                align: str | None = None, before_pt: float | None = None, after_pt: float | None = None,
                line_spacing: float | None = None, first_line_twips: int | None = None,
                first_line_chars: int | None = None, remove_bottom_border: bool = False) -> None:
    style = styles_root.find(f"./w:style[@w:styleId='{style_id}']", {"w": W_NS})
    if style is None:
        return
    r_pr = get_or_add(style, "w:rPr")
    set_fonts(r_pr, font_zh, font_en)
    if size_pt is not None:
        set_font_size(r_pr, size_pt)
    if bold is not None:
        if bold:
            get_or_add(r_pr, "w:b").set(qn("w:val"), "1")
            get_or_add(r_pr, "w:bCs").set(qn("w:val"), "1")
        else:
            get_or_add(r_pr, "w:b").set(qn("w:val"), "0")
            get_or_add(r_pr, "w:bCs").set(qn("w:val"), "0")
    if italic is not None:
        get_or_add(r_pr, "w:i").set(qn("w:val"), "1" if italic else "0")
        get_or_add(r_pr, "w:iCs").set(qn("w:val"), "1" if italic else "0")
    if color is not None:
        set_color(r_pr, color)
    p_pr = get_or_add(style, "w:pPr")
    if align is not None:
        set_paragraph_alignment(p_pr, align)
    if before_pt is not None or after_pt is not None or line_spacing is not None:
        set_paragraph_spacing(p_pr, before_pt or 0, after_pt or 0, line_spacing or 1.5)
    if first_line_twips is not None or first_line_chars is not None:
        set_paragraph_indent(p_pr, first_line_twips or 0, first_line_chars or 0)
    if remove_bottom_border:
        p_bdr = p_pr.find(qn("w:pBdr"))
        if p_bdr is not None:
            p_pr.remove(p_bdr)


def patch_styles(styles_xml: bytes, profile: dict) -> bytes:
    root = ET.fromstring(styles_xml)
    body = profile["body"]
    body_font_zh = body["font_zh"]
    body_font_en = body["font_en"]
    body_size = float(body["size_pt"])
    line_spacing = float(body["line_spacing"])
    first_line_twips = int(body.get("first_line_twips", 420))
    first_line_chars = int(body.get("first_line_chars", 200))
    body_align = align_to_word(body.get("align", "justify"))

    patch_style(root, "Normal", font_zh=body_font_zh, font_en=body_font_en, size_pt=body_size,
                align=body_align, before_pt=float(body.get("space_before_pt", 0)), after_pt=float(body.get("space_after_pt", 0)), line_spacing=line_spacing,
                first_line_twips=first_line_twips, first_line_chars=first_line_chars)
    patch_style(root, "BodyText", font_zh=body_font_zh, font_en=body_font_en, size_pt=body_size,
                align=body_align, before_pt=float(body.get("space_before_pt", 0)), after_pt=float(body.get("space_after_pt", 0)), line_spacing=line_spacing,
                first_line_twips=first_line_twips, first_line_chars=first_line_chars)
    patch_style(root, "FirstParagraph", font_zh=body_font_zh, font_en=body_font_en, size_pt=body_size,
                align=body_align, before_pt=float(body.get("space_before_pt", 0)), after_pt=float(body.get("space_after_pt", 0)), line_spacing=line_spacing,
                first_line_twips=first_line_twips, first_line_chars=first_line_chars)
    patch_style(root, "Compact", font_zh=body_font_zh, font_en=body_font_en, size_pt=body_size,
                align=body_align, before_pt=float(body.get("space_before_pt", 0)), after_pt=0, line_spacing=line_spacing,
                first_line_twips=0, first_line_chars=0)
    patch_style(root, "Title", font_zh=body_font_zh, font_en=body_font_en, size_pt=26,
                bold=False, italic=False, color="000000", align="left", before_pt=0, after_pt=12,
                line_spacing=1.15, first_line_twips=0, first_line_chars=0, remove_bottom_border=True)
    patch_style(root, "Subtitle", font_zh=body_font_zh, font_en=body_font_en, size_pt=14,
                bold=False, italic=False, color="000000", align="left", before_pt=0, after_pt=6,
                line_spacing=1.15, first_line_twips=0, first_line_chars=0)
    for style_key, style_id in (("heading1", "Heading1"), ("heading2", "Heading2"), ("heading3", "Heading3"), ("heading4", "Heading4")):
        config = profile.get("headings", {}).get(style_key)
        if not config:
            continue
        patch_style(root, style_id, font_zh=config["font_zh"], font_en=config["font_en"], size_pt=float(config["size_pt"]),
                    bold=bool(config["bold"]), italic=False, color="000000", align=align_to_word(config.get("align", "left")),
                    before_pt=float(config["space_before_pt"]), after_pt=float(config["space_after_pt"]),
                    line_spacing=float(config.get("line_spacing", line_spacing)), first_line_twips=0, first_line_chars=0)
    captions = profile.get("captions", {})
    for style_id in ("Caption", "ImageCaption", "TableCaption"):
        patch_style(root, style_id, font_zh=captions.get("font_zh", body_font_zh), font_en=captions.get("font_en", body_font_en),
                    size_pt=float(captions.get("size_pt", body_size)), bold=False, italic=False, color="000000",
                    align=align_to_word(captions.get("align", "center")),
                    before_pt=float(captions.get("space_before_pt", 6)), after_pt=float(captions.get("space_after_pt", 6)),
                    line_spacing=float(captions.get("line_spacing", line_spacing)), first_line_twips=0, first_line_chars=0)

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def build_empty_paragraph(style_id: str | None = None, align: str | None = None) -> ET.Element:
    paragraph = ET.Element(qn("w:p"))
    ppr = ET.SubElement(paragraph, qn("w:pPr"))
    if style_id:
        style = ET.SubElement(ppr, qn("w:pStyle"))
        style.set(qn("w:val"), style_id)
    if align:
        jc = ET.SubElement(ppr, qn("w:jc"))
        jc.set(qn("w:val"), align)
    return paragraph


def make_tc(width: int) -> ET.Element:
    tc = ET.Element(qn("w:tc"))
    tc_pr = ET.SubElement(tc, qn("w:tcPr"))
    tc_w = ET.SubElement(tc_pr, qn("w:tcW"))
    tc_w.set(qn("w:w"), str(width))
    tc_w.set(qn("w:type"), "dxa")
    return tc


def create_equation_table(paragraph: ET.Element, eq_number: str) -> ET.Element:
    tbl = ET.Element(qn("w:tbl"))
    tbl_pr = ET.SubElement(tbl, qn("w:tblPr"))
    tbl_w = ET.SubElement(tbl_pr, qn("w:tblW"))
    tbl_w.set(qn("w:w"), "5000")
    tbl_w.set(qn("w:type"), "pct")
    tbl_layout = ET.SubElement(tbl_pr, qn("w:tblLayout"))
    tbl_layout.set(qn("w:type"), "fixed")
    borders = ET.SubElement(tbl_pr, qn("w:tblBorders"))
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        node = ET.SubElement(borders, qn(f"w:{edge}"))
        node.set(qn("w:val"), "nil")
    look = ET.SubElement(tbl_pr, qn("w:tblLook"))
    look.set(qn("w:firstRow"), "0")
    look.set(qn("w:lastRow"), "0")
    look.set(qn("w:firstColumn"), "0")
    look.set(qn("w:lastColumn"), "0")
    look.set(qn("w:noHBand"), "1")
    look.set(qn("w:noVBand"), "1")
    look.set(qn("w:val"), "0000")

    grid = ET.SubElement(tbl, qn("w:tblGrid"))
    for width in (900, 6300, 1800):
        col = ET.SubElement(grid, qn("w:gridCol"))
        col.set(qn("w:w"), str(width))

    tr = ET.SubElement(tbl, qn("w:tr"))
    left = make_tc(900)
    left.append(build_empty_paragraph())
    tr.append(left)

    middle = make_tc(6300)
    ppr = normalize_ppr(paragraph)
    set_paragraph_alignment(ppr, "center")
    set_paragraph_indent(ppr, 0, 0)
    set_paragraph_spacing(ppr, 0, 0, 1.5)
    middle.append(paragraph)
    tr.append(middle)

    right = make_tc(1800)
    number_paragraph = build_empty_paragraph(None, "right")
    number_ppr = normalize_ppr(number_paragraph)
    set_paragraph_indent(number_ppr, 0, 0)
    set_paragraph_spacing(number_ppr, 0, 0, 1.5)
    run = ET.SubElement(number_paragraph, qn("w:r"))
    rpr = ET.SubElement(run, qn("w:rPr"))
    set_fonts(rpr, "SimSun", "Times New Roman")
    set_font_size(rpr, 12)
    ET.SubElement(run, qn("w:t")).text = eq_number
    right.append(number_paragraph)
    tr.append(right)

    return tbl


def extract_equation_number(paragraph: ET.Element) -> str | None:
    o_math_para = paragraph.find(qn("m:oMathPara"))
    if o_math_para is None:
        return None
    o_math = o_math_para.find(qn("m:oMath"))
    if o_math is None:
        return None
    children = list(o_math)
    consumed: list[ET.Element] = []
    tail_text = ""
    for child in reversed(children):
        if child.tag != qn("m:r"):
            break
        text_node = child.find(qn("m:t"))
        if text_node is None or text_node.text is None:
            break
        consumed.append(child)
        tail_text = text_node.text + tail_text
        stripped = tail_text.replace("\u2001", "").replace("\u2002", "").replace("\u2003", "").strip()
        if stripped.startswith("(") and stripped.endswith(")") and stripped[1:-1].replace(".", "").isdigit():
            eq_number = stripped
            for node in consumed:
                o_math.remove(node)
            return eq_number
    return None


def patch_document(document_xml: bytes, profile: dict) -> bytes:
    root = ET.fromstring(document_xml)
    body = root.find(qn("w:body"))
    if body is None:
        return document_xml
    body_config = profile["body"]
    body_align = align_to_word(body_config.get("align", "justify"))
    captions = profile.get("captions", {})

    for paragraph in body.findall(f".//{qn('w:p')}"):
        style_id = get_paragraph_style_id(paragraph)
        if style_id in {"Caption", "ImageCaption", "TableCaption"}:
            ppr = normalize_ppr(paragraph)
            set_paragraph_alignment(ppr, align_to_word(captions.get("align", "center")))
            set_paragraph_indent(ppr, 0, 0)
            set_paragraph_spacing(ppr, float(captions.get("space_before_pt", 6)), float(captions.get("space_after_pt", 6)),
                                  float(captions.get("line_spacing", body_config["line_spacing"])))
        elif style_id in {"BodyText", "FirstParagraph"}:
            if paragraph.find(qn("m:oMathPara")) is None:
                ppr = normalize_ppr(paragraph)
                set_paragraph_indent(ppr, int(body_config.get("first_line_twips", 420)), int(body_config.get("first_line_chars", 200)))
                set_paragraph_spacing(ppr, float(body_config.get("space_before_pt", 0)), float(body_config.get("space_after_pt", 0)),
                                      float(body_config["line_spacing"]))
                set_paragraph_alignment(ppr, body_align)

    body_children = list(body)
    for index, child in enumerate(body_children):
        if child.tag != qn("w:p"):
            continue
        style_id = get_paragraph_style_id(child)
        if style_id != "BodyText":
            continue
        eq_number = extract_equation_number(child)
        if not eq_number:
            continue
        table = create_equation_table(child, eq_number)
        body.remove(child)
        body.insert(index, table)

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def postprocess_docx(path: Path, template: str | None) -> None:
    profile = load_profile(template)
    with zipfile.ZipFile(path, "r") as source:
        members = {name: source.read(name) for name in source.namelist()}
    if "word/styles.xml" in members:
        members["word/styles.xml"] = patch_styles(members["word/styles.xml"], profile)
    if "word/document.xml" in members:
        members["word/document.xml"] = patch_document(members["word/document.xml"], profile)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as target:
        for name, data in members.items():
            target.writestr(name, data)


def main() -> int:
    parser = argparse.ArgumentParser(description="Post-process DOCX output to enforce md2all house styles.")
    parser.add_argument("docx", type=Path)
    parser.add_argument("--template")
    args = parser.parse_args()
    postprocess_docx(args.docx, args.template)
    print(args.docx)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
