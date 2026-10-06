from docx import Document
from docx.shared import Pt, Inches
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

OUT = "Mineo_Raffaele_EmailSignature.docx"

doc = Document()
sec = doc.sections[0]
sec.top_margin = Inches(0.45)
sec.bottom_margin = Inches(0.45)
sec.left_margin = Inches(0.55)
sec.right_margin = Inches(0.55)

normal = doc.styles["Normal"]
normal.font.name = "Arial"
normal.font.size = Pt(10.5)
normal.paragraph_format.space_after = Pt(0)
normal.paragraph_format.line_spacing = 1.0

def add_line(parts=None, before=0, after=0):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = 1.0
    if parts:
        for text, bold, italic in parts:
            r = p.add_run(text)
            r.bold = bold
            r.italic = italic
            r.font.name = "Arial"
            r.font.size = Pt(10.5)
    return p

# Exact opening format: one paragraph containing only "---",
# with Word paragraph spacing before and after, and no blank paragraphs.
add_line([("---", False, False)], before=6, after=6)

add_line([("Dr. ", False, False), ("Raffaele Mineo", True, False), (", Eng.", False, False)])
add_line([("Italian National PhD in Artificial Intelligence - Health and Life Sciences", False, True)])
add_line([("Member", False, True), (", IEEE", False, False)])
add_line([("Research Fellow", False, True), (", ", False, False), ("PeRCeiVe.Ai Lab", True, False)])
add_line([("Department of Industrial, Electrical, Electronic and Computer Engineering (DIEEI)", False, False)])
add_line([("University of Catania, Catania, Italy", False, False)], after=6)

add_line([("Associate Editor", True, False), (", ", False, False), ("Frontiers in Communication", False, True)])
add_line([("Lead Guest Editor", True, False), (", ", False, False), ("Springer Cognitive Computation", False, True)])
add_line([("Area Chair", True, False), (", ", False, False), ("Medical Image Computing and Computer-Assisted Intervention (MICCAI)", False, True)])
add_line([("Area Chair", True, False), (", ", False, False), ("International Joint Conference on Neural Networks (IJCNN)", False, True)])
add_line([("Area Chair", True, False), (", ", False, False), ("IEEE International Conference on Automatic Face and Gesture Recognition (FG)", False, True)], after=6)

add_line([("Polo Tecnologico, Via Santa Sofia 102, 95123 Catania, Italy", False, False)])

def add_hyperlink(paragraph, text, url):
    part = paragraph.part
    rid = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), rid)

    new_run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    rPr.append(color)
    rPr.append(underline)
    new_run.append(rPr)

    t = OxmlElement("w:t")
    t.text = text
    new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)

p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(6)
p.add_run("Web: ")
add_hyperlink(p, "https://IngRaffaeleMineo.GitHub.io/", "https://IngRaffaeleMineo.GitHub.io/")

p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(0)
r = p.add_run("My Life is The Research, and I am truly lucky to be able to live it to the fullest")
r.italic = True
r.font.name = "Arial"
r.font.size = Pt(10.5)
r = p.add_run(" 🙃")
r.italic = False
r.font.name = "Segoe UI Emoji"
r.font.size = Pt(10.5)

doc.core_properties.title = "Raffaele Mineo Email Signature"
doc.core_properties.subject = "Formatted academic email signature"
doc.core_properties.author = "Raffaele Mineo"

doc.save(OUT)
