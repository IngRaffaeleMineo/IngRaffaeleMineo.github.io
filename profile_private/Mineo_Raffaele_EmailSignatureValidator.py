"""Regression checks for Outlook-friendly full and short DOCX signatures."""
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt

HERE = Path(__file__).resolve().parent
FULL = HERE / "Mineo_Raffaele_EmailSignature.docx"
SHORT = HERE / "Mineo_Raffaele_EmailSignature_Short.docx"


def all_text(doc):
    return "\n".join("".join(t.text or "" for t in p._p.iter(qn("w:t"))) for p in doc.paragraphs)


def check(path, n_paragraphs, n_soft_breaks, n_links, full):
    doc = Document(path)
    assert len(doc.paragraphs) == n_paragraphs, f"Wrong paragraph count: {path}"
    assert not doc.tables and not doc.inline_shapes, "No tables/images in Outlook signatures"
    assert sum(len(list(p._p.iter(qn("w:br")))) for p in doc.paragraphs) == n_soft_breaks
    text = all_text(doc)
    assert "Raffaele Mineo" in text and "Eng. Ph.D." in text
    assert "Italian National PhD in Artificial Intelligence - Health and Life Sciences" in text
    assert "Research Fellow" in text and "University of Catania" in text
    assert "---" not in text and "My Life is The Research" not in text and "🙃" not in text
    assert "EEAI" not in text
    if full:
        for phrase in ("Member, IEEE", "Organizing Committee", "Associate Editor", "Lead Guest Editor", "Area Chair", "MICCAI", "ICASSP", "IJCNN", "FG", "ISBI 2027", "DIEEI", "Polo Tecnologico"):
            assert phrase in text, f"Full signature missing: {phrase}"
        assert text.index("Organizing Committee") < text.index("Associate Editor") < text.index("Lead Guest Editor") < text.index("Area Chair")
        assert text.index("MICCAI") < text.index("ICASSP") < text.index("IJCNN") < text.index("FG")
        assert doc.paragraphs[0].paragraph_format.space_after == Pt(3.5)
    else:
        assert all(t not in text for t in ("Organizing Committee", "Associate Editor", "Area Chair", "Polo Tecnologico"))

    link_nodes = [node for p in doc.paragraphs for node in p._p.iter(qn("w:hyperlink"))]
    assert len(link_nodes) == n_links, f"Expected {n_links} hyperlinks"
    relations = {rel.target_ref for rel in doc.part.rels.values() if rel.reltype.endswith("/hyperlink")}
    assert "mailto:raffaele.mineo@phd.unict.it" in relations
    assert "https://ingraffaelemineo.github.io/" in relations

    seen_name = False
    for p in doc.paragraphs:
        assert p.paragraph_format.space_before in (None, Pt(0))
        assert p.paragraph_format.space_after in (None, Pt(0), Pt(3.5))
        assert abs(p.paragraph_format.line_spacing - 1.0) < 0.001
        for r in p._p.iter(qn("w:r")):
            part_text = "".join(t.text or "" for t in r.iter(qn("w:t")))
            rPr = r.find(qn("w:rPr"))
            if rPr is None or not part_text:
                continue
            f = rPr.find(qn("w:rFonts"))
            assert f is not None and f.get(qn("w:ascii")) == "Segoe UI", part_text
            b = rPr.find(qn("w:b"))
            is_bold = b is not None and b.get(qn("w:val")) != "0"
            assert is_bold == (part_text == "Raffaele Mineo"), f"Unexpected bold: {part_text}"
            if is_bold:
                seen_name = True
            size = rPr.find(qn("w:sz"))
            assert size is not None and int(size.get(qn("w:val"))) == (20 if is_bold else 18)
            color = rPr.find(qn("w:color"))
            assert color is not None
            expected_color = "404040" if is_bold else ("365F7D" if r.getparent().tag == qn("w:hyperlink") else "606060")
            assert color.get(qn("w:val")) == expected_color, (part_text, expected_color)
            underline = rPr.find(qn("w:u"))
            if underline is not None:
                assert underline.get(qn("w:val")) == "none", part_text
    assert seen_name
    print(f"PASS {path.name}: {n_paragraphs} paragraphs, {n_soft_breaks} soft breaks, {n_links} links")


if __name__ == "__main__":
    check(FULL, 3, 7, 2, full=True)
    check(SHORT, 1, 3, 2, full=False)
