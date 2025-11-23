# src/utils.py
from PyPDF2 import PdfReader


def extract_text_from_pdf(path: str) -> str:
    """Extract text from a PDF file. Returns raw text concatenated from pages."""
    reader = PdfReader(path)
    texts = []
    for page in reader.pages:
        try:
            t = page.extract_text()
        except Exception:
            t = None
        if t:
            texts.append(t)
    return "\n\n".join(texts)