import pdfplumber

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract raw text from syllabus PDF using pdfplumber"""
    import io
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)
