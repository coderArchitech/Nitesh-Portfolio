"""Build <base>.html (for PDF printing) and <base>.docx from a content module.
Usage: python3 build.py <content_module> <out-dir> <base-name>
"""
import html, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
C = importlib.import_module(sys.argv[1])
from docx import Document
from docx.shared import Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

out = sys.argv[2]
BASE = sys.argv[3]
os.makedirs(out, exist_ok=True)
BOLD = re.compile(r"\*\*(.+?)\*\*")

# ---------------- HTML ----------------
def md(s):
    return BOLD.sub(r"<b>\1</b>", html.escape(s))

parts = []
contact = " | ".join(
    f'<a href="{html.escape(u)}">{html.escape(t)}</a>' if u else html.escape(t) for t, u in C.CONTACT)
parts.append(f"<header><h1>{C.NAME}</h1><div class='headline'>{html.escape(C.HEADLINE)}</div><div class='contact'>{contact}</div></header>")
parts.append(f"<h2>Professional Summary</h2><p class='summary'>{md(C.SUMMARY)}</p>")
HIGHLIGHTS = getattr(C, "HIGHLIGHTS", None)
if HIGHLIGHTS:
    parts.append("<h2>Key Impact</h2><ul class='impact'>" + "".join(
        f"<li><b>{html.escape(k)}:</b> {md(v)}</li>" for k, v in HIGHLIGHTS) + "</ul>")
parts.append("<h2>Core Skills</h2><div class='skills'>" + "".join(
    f"<p><b>{html.escape(k)}:</b> {html.escape(v)}</p>" for k, v in C.SKILLS) + "</div>")
parts.append("<h2>Professional Experience</h2>")
for r in C.ROLES:
    block = [f"<div class='role'><div class='role-head'><span><b>{html.escape(r['title'])}</b> | <b>{html.escape(r['company'])}</b></span>"
             f"<span class='when'>{html.escape(r['where'])} | {html.escape(r['when'])}</span></div>"]
    if r.get("scope"):
        block.append(f"<p class='scope'>{html.escape(r['scope'])}</p>")
    for head, bullets in r["groups"]:
        if head:
            block.append(f"<div class='group'>{html.escape(head)}</div>")
        block.append("<ul>" + "".join(f"<li>{md(b)}</li>" for b in bullets) + "</ul>")
    block.append("</div>")
    parts.append("".join(block))
parts.append("<div class='role'><div class='role-head'><span><b>Earlier Experience</b></span><span class='when'>2016 – 2020</span></div><ul>"
             + "".join(f"<li><b>{html.escape(t)}</b> <span class='muted'>({html.escape(w)})</span>: {md(d)}</li>" for t, w, d in C.EARLIER)
             + "</ul></div>")
parts.append("<h2>Selected Projects</h2><ul class='projects'>" + "".join(
    f"<li><b>{html.escape(n)}</b> (<a href='{u}'>{html.escape(l)}</a>): {md(d)}</li>" for n, l, u, d in C.PROJECTS) + "</ul>")
deg, uni, yrs = C.EDUCATION
parts.append(f"<h2>Education</h2><div class='role-head'><span><b>{deg}</b><br/>{uni}</span><span class='when'>{yrs}</span></div>")

CSS = """
@page{size:A4;margin:12mm 14mm}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Carlito,Calibri,'Liberation Sans',Arial,sans-serif;font-size:10.2pt;line-height:1.3;color:#111}
a{color:inherit;text-decoration:none}
header{text-align:center;margin-bottom:6pt}
h1{font-size:20pt;letter-spacing:.2pt;margin-bottom:2pt}
.headline{font-weight:700;font-size:10.6pt;margin-bottom:2pt}
.contact{font-size:9.6pt}
h2{font-size:11pt;text-transform:uppercase;letter-spacing:.3pt;border-bottom:1.2px solid #111;padding-bottom:1.5pt;margin:9pt 0 4pt}
.summary{text-align:left}
.skills p{margin-bottom:1.2pt}
.role{margin-bottom:6pt}
li{break-inside:avoid}
.role-head,.scope,.group,h2{break-after:avoid}
.role-head{display:flex;justify-content:space-between;gap:12pt;align-items:baseline}
.when{font-style:italic;white-space:nowrap;font-size:9.8pt}
.scope{font-style:italic;margin:1pt 0 2pt;color:#333}
.group{font-weight:700;font-size:9.6pt;color:#333;margin:3pt 0 1pt;text-transform:uppercase;letter-spacing:.3pt}
ul{padding-left:13pt}
li{margin-bottom:1.3pt}
.muted{color:#444}
.projects li{margin-bottom:2pt}
.impact{display:grid;grid-template-columns:1fr 1fr;column-gap:16pt;padding-left:13pt}
.impact li{margin-bottom:1.5pt}
"""
with open(os.path.join(out, BASE + ".html"), "w", encoding="utf-8") as f:
    f.write(f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>{C.NAME} - Resume</title><style>{CSS}</style></head><body>{''.join(parts)}</body></html>")

# ---------------- DOCX ----------------
doc = Document()
sec = doc.sections[0]
sec.page_height, sec.page_width = Mm(297), Mm(210)
sec.top_margin = sec.bottom_margin = Mm(12)
sec.left_margin = sec.right_margin = Mm(14)
st = doc.styles["Normal"]
st.font.name = "Calibri"; st.font.size = Pt(10)
st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
st.paragraph_format.space_after = Pt(0)
st.paragraph_format.line_spacing = 1.05
TEXT_W = Mm(210 - 28)

def runs(p, s, size=None, italic=False):
    pos = 0
    for m in BOLD.finditer(s):
        if m.start() > pos:
            r = p.add_run(s[pos:m.start()]); r.italic = italic
            if size: r.font.size = size
        r = p.add_run(m.group(1)); r.bold = True; r.italic = italic
        if size: r.font.size = size
        pos = m.end()
    if pos < len(s):
        r = p.add_run(s[pos:]); r.italic = italic
        if size: r.font.size = size

def heading(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(3)
    r = p.add_run(text.upper()); r.bold = True; r.font.size = Pt(11)
    pPr = p._p.get_or_add_pPr(); bdr = OxmlElement("w:pBdr"); b = OxmlElement("w:bottom")
    for k, v in (("w:val", "single"), ("w:sz", "8"), ("w:space", "1"), ("w:color", "111111")):
        b.set(qn(k), v)
    bdr.append(b); pPr.append(bdr)

def left_right(left, right, bold_left=True):
    p = doc.add_paragraph()
    p.paragraph_format.tab_stops.add_tab_stop(TEXT_W, WD_TAB_ALIGNMENT.RIGHT)
    runs(p, left if not bold_left else f"**{left}**")
    r = p.add_run("\t" + right); r.italic = True; r.font.size = Pt(9.5)
    p.paragraph_format.keep_with_next = True
    return p

def bullet(s):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(1)
    runs(p, s)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(C.NAME); r.bold = True; r.font.size = Pt(20)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(C.HEADLINE); r.bold = True; r.font.size = Pt(10.5)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(" | ".join(t for t, _ in C.CONTACT)); r.font.size = Pt(9.5)

heading("Professional Summary")
runs(doc.add_paragraph(), C.SUMMARY)
if HIGHLIGHTS:
    heading("Key Impact")
    for k, v in HIGHLIGHTS:
        bullet(f"**{k}:** {v}")
heading("Core Skills")
for k, v in C.SKILLS:
    q = doc.add_paragraph(); q.paragraph_format.space_after = Pt(1); runs(q, f"**{k}:** {v}")
heading("Professional Experience")
for role in C.ROLES:
    lr = left_right(f"**{role['title']}** | **{role['company']}**", f"{role['where']} | {role['when']}", bold_left=False)
    lr.paragraph_format.space_before = Pt(5)
    if role.get("scope"):
        q = doc.add_paragraph(); runs(q, role["scope"], italic=True); q.paragraph_format.keep_with_next = True
    for head, bullets in role["groups"]:
        if head:
            q = doc.add_paragraph(); q.paragraph_format.space_before = Pt(3)
            rr = q.add_run(head.upper()); rr.bold = True; rr.font.size = Pt(9.5); rr.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
            q.paragraph_format.keep_with_next = True
        for b in bullets:
            bullet(b)
lr = left_right("Earlier Experience", "2016 – 2020"); lr.paragraph_format.space_before = Pt(5)
for t, w, d in C.EARLIER:
    bullet(f"**{t}** ({w}): {d}")
heading("Selected Projects")
for n, l, u, d in C.PROJECTS:
    bullet(f"**{n}** ({l}): {d}")
heading("Education")
deg, uni, yrs = C.EDUCATION
left_right(deg, yrs)
doc.add_paragraph(uni)
doc.save(os.path.join(out, BASE + ".docx"))
print("built", out)
