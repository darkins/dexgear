from pypdf import PdfReader
import sys

pdf_path = r"c:\www\dexgear\pdf\UltraLite-mk3_Hybrid_Win.pdf"
out_path = r"c:\www\dexgear\pdf\UltraLite-mk3_Hybrid_Win.txt"

reader = PdfReader(pdf_path)
with open(out_path, "w", encoding="utf-8") as out:
    out.write(f"Pages: {len(reader.pages)}\n\n")
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        out.write(f"--- PAGE {i} ---\n")
        if text:
            out.write(text)
        else:
            out.write("[No extractable text on this page]\n")
        out.write("\n\n")

print(f"Wrote extracted text to {out_path}")
