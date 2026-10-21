#!/usr/bin/env python3
"""Read-only chronology audit for publication support masters.

Uses OOXML zip contents rather than rewriting DOCX/XLSX archives.
"""
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
import json
import re

ROOT = Path(__file__).resolve().parent
NS_S = {"x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
NS_W = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
YEAR_RE = re.compile(r"\b(?:19|20)\d{2}\b")


def validate_descending(values, label):
    for previous, current in zip(values, values[1:]):
        if previous < current:
            raise AssertionError(
                f"{label} is not reverse chronological: {previous} followed by {current}"
            )


def year(text):
    match = YEAR_RE.search(str(text))
    return int(match.group()) if match else None


def inspect_xlsx():
    with ZipFile(ROOT / "Mineo_Raffaele_PublicationsMetadata.xlsx") as z:
        names = set(z.namelist())
        strings = []
        if "xl/sharedStrings.xml" in names:
            root = ET.fromstring(z.read("xl/sharedStrings.xml"))
            strings = ["".join((t.text or "") for t in item.findall(".//x:t", NS_S))
                       for item in root.findall("x:si", NS_S)]
        sheet = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
        rows = []
        for node in sheet.findall(".//x:sheetData/x:row", NS_S):
            cells = {}
            for cell in node.findall("x:c", NS_S):
                column = re.match(r"[A-Z]+", cell.get("r", "")).group()
                v = cell.find("x:v", NS_S)
                if cell.get("t") == "inlineStr":
                    value = "".join((t.text or "") for t in cell.findall(".//x:t", NS_S))
                elif v is not None:
                    value = strings[int(v.text)] if cell.get("t") == "s" else v.text
                else:
                    value = ""
                cells[column] = str(value or "")
            rows.append(cells)
    if not rows:
        raise RuntimeError("No rows in publication workbook")
    headers = rows[0]
    year_columns = [k for k, v in headers.items() if re.search(r"\byear\b|anno", v, re.I)]
    topic_columns = [k for k, v in headers.items() if re.search(r"topic", v, re.I)]
    assert year_columns == ["F"], f"Unexpected publication-year columns: {year_columns}"
    assert "K" in topic_columns, "Missing research-topic key"
    grouped = {}
    for row in rows[1:]:
        if not row.get("A", "").strip():
            continue
        key = row.get("K", "").strip()
        y = year(row.get("F", ""))
        assert key and y is not None, f"Missing topic/year: {row.get('A')}"
        grouped.setdefault(key, []).append(y)
    assert sum(map(len, grouped.values())) == 28, "Unexpected XLSX publication count"
    for key, years in grouped.items():
        validate_descending(years, f"XLSX {key}")
    print("XLSX chronological topic groups:", grouped)
    return grouped


def inspect_docx():
    with ZipFile(ROOT / "Mineo_Raffaele_PublicationsList.docx") as z:
        root = ET.fromstring(z.read("word/document.xml"))
    paragraphs = []
    for p in root.findall(".//w:body/w:p", NS_W):
        val = "".join((t.text or "") for t in p.findall(".//w:t", NS_W)).strip()
        if val:
            paragraphs.append(val)
    raw = (ROOT.parent / "profile-data.js").read_text(encoding="utf-8")
    prefix = "window.PROFILE_DATA = "
    assert raw.startswith(prefix), "Unexpected profile-data.js format"
    profile = json.loads(raw[len(prefix):].strip().removesuffix(";"))
    topic_titles = {t["title"]: t["key"] for t in profile["publicationTopics"]}
    grouped = {}
    current_key = None
    for line in paragraphs:
        if line in topic_titles:
            current_key = topic_titles[line]
            grouped.setdefault(current_key, [])
        match = re.match(r"^((?:19|20)[0-9]{2})(?:/[0-9]{1,2})? - ", line)
        if match:
            assert current_key is not None, f"DOCX item outside research group: {line[:80]}"
            grouped[current_key].append(int(match.group(1)))
    assert sum(map(len, grouped.values())) == 28, "Unexpected DOCX publication count"
    for key, years in grouped.items():
        validate_descending(years, f"DOCX {key}")
    print("DOCX chronological topic groups:", grouped)
    return grouped


if __name__ == "__main__":
    xlsx = inspect_xlsx()
    docx = inspect_docx()
    assert xlsx == docx, "DOCX/XLSX chronological grouping differs"
    print("PASS: DOCX and XLSX preserve 28 records, topic groups and reverse chronology")
