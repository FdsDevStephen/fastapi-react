from pylatex import Document, NoEscape

def generate_pdf_report(tex_content: str) -> str:
    doc = Document()
    doc.preamble.append(NoEscape(r'\title{Generated Report}'))
    doc.preamble.append(NoEscape(r'\author{Ollama LLM}'))
    doc.preamble.append(NoEscape(r'\date{\today}'))
    doc.append(NoEscape(r'\maketitle'))

    doc.append(NoEscape(tex_content))

    pdf_path = "report.pdf"
    doc.generate_pdf(pdf_path, clean_tex=False)
    return pdf_path
