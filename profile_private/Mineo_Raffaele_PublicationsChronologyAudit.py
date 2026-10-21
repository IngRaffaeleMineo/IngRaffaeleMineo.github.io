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
    print("XLSX headers:", headers)
    print("XLSX year columns:", year_columns, "topic columns:", topic_columns)
    for i, row in enumerate(rows[1:], 2):
        years = [row.get(k) for k in year_columns]
        topic = [row.get(k) for k in topic_columns]
        print("XLSX record", i, repr(row.get("A", "")[:80]), years, topic)
    return rows, year_columns, topic_columns


def inspect_docx():
    with ZipFile(ROOT / "Mineo_Raffaele_PublicationsList.docx") as z:
        root = ET.fromstring(z.read("word/document.xml"))
    paragraphs = []
    for p in root.findall(".//w:body/w:p", NS_W):
        val = "".join((t.text or "") for t in p.findall(".//w:t", NS_W)).strip()
        if val:
            paragraphs.append(val)
    print("DOCX paragraphs:", len(paragraphs))
    for i, line in enumerate(paragraphs):
        print("DOCX", i, repr(line[:170]))
    return paragraphs


if __name__ == "__main__":
    inspect_xlsx()
    inspect_docx()
