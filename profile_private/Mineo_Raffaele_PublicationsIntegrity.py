from pathlib import Path

from docx import Document
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent
XLSX = ROOT / "Mineo_Raffaele_PublicationsMetadata.xlsx"
DOCX = ROOT / "Mineo_Raffaele_PublicationsList.docx"

FORBIDDEN_TITLE = "Memory-Augmented Prompt Tuning for Self-Supervised Continual Learning in Medical Imaging"
FORBIDDEN_TOKEN = "MAPT"


def clean_xlsx() -> bool:
    wb = load_workbook(XLSX)
    ws = wb["Foglio1"]
    changed = False

    rows_to_delete = []
    for row in range(2, ws.max_row + 1):
        title = str(ws.cell(row=row, column=1).value or "")
        if title == FORBIDDEN_TITLE or FORBIDDEN_TOKEN in title:
            rows_to_delete.append(row)

    for row in reversed(rows_to_delete):
        ws.delete_rows(row, 1)
        changed = True

    last_row = 1
    for row in range(2, ws.max_row + 1):
        if ws.cell(row=row, column=1).value not in (None, ""):
            last_row = row
            if ws.row_dimensions[row].height != 15:
                ws.row_dimensions[row].height = 15
                changed = True

    if "Tabella1" in ws.tables:
        expected_ref = f"A1:K{last_row}"
        if ws.tables["Tabella1"].ref != expected_ref:
            ws.tables["Tabella1"].ref = expected_ref
            changed = True

        style = ws.tables["Tabella1"].tableStyleInfo
        if style is not None:
            if style.name != "TableStyleMedium14":
                style.name = "TableStyleMedium14"
                changed = True
            if not style.showRowStripes:
                style.showRowStripes = True
                changed = True

    if changed:
        wb.save(XLSX)
    return changed


def remove_paragraph(paragraph) -> None:
    element = paragraph._element
    element.getparent().remove(element)
    paragraph._p = paragraph._element = None


def clean_docx() -> bool:
    doc = Document(DOCX)
    paragraphs = list(doc.paragraphs)
    target_indexes = [
        i
        for i, p in enumerate(paragraphs)
        if FORBIDDEN_TITLE in p.text or FORBIDDEN_TOKEN in p.text
    ]
    if not target_indexes:
        return False

    # PublicationList uses three consecutive paragraphs per record:
    # title/year, authors, and venue/type/link.
    to_remove = set()
    for index in target_indexes:
        to_remove.update(range(index, min(index + 3, len(paragraphs))))

    for index in sorted(to_remove, reverse=True):
        remove_paragraph(paragraphs[index])

    doc.save(DOCX)
    return True


def main() -> None:
    xlsx_changed = clean_xlsx()
    docx_changed = clean_docx()
    print(f"XLSX changed: {xlsx_changed}")
    print(f"DOCX changed: {docx_changed}")


if __name__ == "__main__":
    main()
