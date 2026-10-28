#!/usr/bin/env python3
"""One-time, idempotent, formatting-preserving correction of MICCAI DS bibliography masters.

The profile-data.js canonical source and the owner's BibTeX provide the new
metadata. Only the existing matching record is modified in each OOXML archive.
No extra publication or archive file is created.
"""
from pathlib import Path
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape
from zipfile import ZipFile
from tempfile import NamedTemporaryFile
from docx import Document
import json
import os
import re

ROOT = Path(__file__).resolve().parent
TITLE = "Advancing Healthcare with Multimodal AI: Enhanced Diagnosis, Cognitive Monitoring, and Inclusive Medical Communication"
XLSX = ROOT / "Mineo_Raffaele_PublicationsMetadata.xlsx"
DOCX = ROOT / "Mineo_Raffaele_PublicationsList.docx"
NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def profile_record():
    raw = (ROOT.parent / "profile-data.js").read_text(encoding="utf-8").strip()
    prefix = "window.PROFILE_DATA = "
    assert raw.startswith(prefix)
    data = json.loads(raw[len(prefix):].removesuffix(";"))
    matches = [p for p in data["publications"] if p["title"] == TITLE]
    assert len(matches) == 1 and len(data["publications"]) == 28
    record = matches[0]
    assert record["year"] == 2027 and record["eventYear"] == 2025
    assert record["volume"] == "16489" and record["publisher"] == "Springer"
    assert "@inproceedings{mineo2027advancing," in record["bibtex"]
    return record


def value(cell, strings):
    if cell is None:
        return ""
    t = cell.get("t")
    if t == "inlineStr":
        return "".join(x.text or "" for x in cell.findall(".//s:t", NS))
    v = cell.find("s:v", NS)
    if v is None:
        return ""
    if t == "s":
        return strings[int(v.text)]
    return v.text or ""


def patch_cell(xml, address, content, numeric=False):
    # Preserve worksheet namespaces, table styling, row heights, and all
    # unrelated OOXML by replacing only the bytes of a single cell.
    address_b = address.encode("ascii")
    pattern = rb"<c(?=[^>]*\br=\"" + address_b + rb"\")[^>]*>.*?</c>"
    matches = list(re.finditer(pattern, xml, re.DOTALL))
    assert len(matches) == 1, f"Cell {address} missing or duplicated"
    old = matches[0].group(0)
    opening = old[:old.index(b">")].decode("utf-8")
    opening = re.sub(r'\s+t="[^"]*"', "", opening)
    if numeric:
        new_text = opening + ' t="n"><v>' + str(content) + '</v></c>'
    else:
        new_text = opening + ' t="inlineStr"><is><t xml:space="preserve">' + escape(str(content)) + '</t></is></c>'
    return xml[:matches[0].start()] + new_text.encode("utf-8") + xml[matches[0].end():]


def patch_xlsx(rec):
    with ZipFile(XLSX) as zi:
        strings = []
        if "xl/sharedStrings.xml" in zi.namelist():
            sr = ET.fromstring(zi.read("xl/sharedStrings.xml"))
            strings = [
                "".join(t.text or "" for t in si.findall(".//s:t", NS))
                for si in sr.findall("s:si", NS)
            ]
        sheet_bytes = zi.read("xl/worksheets/sheet1.xml")
        root = ET.fromstring(sheet_bytes)
        candidates = []
        for row in root.findall(".//s:sheetData/s:row", NS):
            cells = {re.match(r"[A-Z]+", c.get("r")).group(): c for c in row.findall("s:c", NS)}
            if value(cells.get("A"), strings) == TITLE:
                candidates.append((int(row.get("r")),cells))
        assert len(candidates) == 1, "Publication XLSX target missing or duplicated"
        index, cells = candidates[0]
        assert value(cells.get("F"),strings) in {"2026","2027"}
        assert value(cells.get("K"),strings) == "synthesis"
        assert value(cells.get("A"),strings) == TITLE
        modifications = {
            "C": rec["venue"],
            "D": rec["acronym"],
            "F": rec["year"],
            "H": rec["bibtex"],
        }
        patched = sheet_bytes
        for col, new_value in modifications.items():
            patched = patch_cell(patched, f"{col}{index}", new_value, numeric=col=="F")
        assert patched != sheet_bytes
        tmp = XLSX.with_suffix(".tmp.xlsx")
        with ZipFile(tmp,"w") as zo:
            for item in zi.infolist():
                payload = patched if item.filename=="xl/worksheets/sheet1.xml" else zi.read(item.filename)
                zo.writestr(item,payload)
    os.replace(tmp,XLSX)
    print(f"XLSX row {index}: bibliographic year 2027; publisher/series/volume/BibTeX updated, table style intact")


def replace_paragraph_runs(paragraph, text):
    # Avoid p.text reassignment because that can remove run-level styling.
    runs = paragraph.runs
    assert runs, "Expected a styled run in publication list"
    runs[0].text = text
    for run in runs[1:]:
        run.text = ""


def patch_docx(rec):
    doc = Document(DOCX)
    title_rows = [i for i,p in enumerate(doc.paragraphs) if TITLE in p.text]
    assert len(title_rows) == 1, "Publication DOCX target missing or duplicated"
    i = title_rows[0]
    assert doc.paragraphs[i].text in {f"2026 - {TITLE}",f"2027 - {TITLE}"}
    assert doc.paragraphs[i+1].text.strip() == "Raffaele Mineo"
    assert "MICCAI" in doc.paragraphs[i+2].text
    replace_paragraph_runs(doc.paragraphs[i],f"2027 - {TITLE}")
    replace_paragraph_runs(doc.paragraphs[i+2],f"{rec['venue']} - Conference - {rec['acronym']}")
    doc.save(DOCX)
    reread=Document(DOCX)
    assert reread.paragraphs[i].text==f"2027 - {TITLE}"
    assert "LNCS" in reread.paragraphs[i+2].text or "Lecture Notes in Computer Science" in reread.paragraphs[i+2].text
    print(f"DOCX paragraph {i+1}: bibliographic year 2027 and Springer LNCS 16489 updated")


def main():
    rec = profile_record()
    patch_xlsx(rec)
    patch_docx(rec)
    print("PASS: updated existing 28-record publications masters without altering topic assignments")


if __name__ == "__main__":
    main()
