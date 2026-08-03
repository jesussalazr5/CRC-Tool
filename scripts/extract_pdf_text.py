from pathlib import Path

from pypdf import PdfReader

pdf_path = Path(__file__).resolve().parent.parent / "pdf" / "cfc20261t4.pdf"
out_path = Path(__file__).resolve().parent.parent / "pdf" / "_extracted_utf8.txt"
reader = PdfReader(str(pdf_path))

with open(out_path, "w", encoding="utf-8") as f:
    for i, page in enumerate(reader.pages, start=1):
        f.write(f"\n===== PAGE {i} =====\n")
        f.write(page.extract_text())
