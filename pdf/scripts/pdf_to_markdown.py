"""
Convert live12-manual-en.pdf to markdown using PyMuPDF.
Detects heading levels by font size, preserves structure.
"""

import fitz  # PyMuPDF
import re
import sys
from pathlib import Path

PDF_PATH = Path(__file__).parent.parent / "live12-manual-en.pdf"
OUT_PATH = Path(__file__).parent.parent / "live12-manual-en.md"


def clean_text(text: str) -> str:
    """Normalise whitespace and remove control chars."""
    text = text.replace("\x00", "")
    text = re.sub(r"\r\n|\r", "\n", text)
    # Collapse multiple spaces (but not newlines)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def classify_heading(size: float, thresholds: dict) -> int | None:
    """Return heading level 1-4 based on font size, or None for body text."""
    if size >= thresholds["h1"]:
        return 1
    if size >= thresholds["h2"]:
        return 2
    if size >= thresholds["h3"]:
        return 3
    if size >= thresholds["h4"]:
        return 4
    return None


def get_size_thresholds(doc: fitz.Document, sample_pages: int = 20) -> dict:
    """Sample font sizes from the document to derive heading thresholds."""
    sizes = []
    for page_num in range(min(sample_pages, len(doc))):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if block.get("type") != 0:
                continue
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    s = round(span["size"], 1)
                    sizes.append(s)

    if not sizes:
        return {"h1": 20, "h2": 16, "h3": 13, "h4": 11}

    sizes_sorted = sorted(set(sizes), reverse=True)
    # Pick thresholds from the top distinct sizes
    unique = [s for s in sizes_sorted if s > 9]
    h1 = unique[0] if len(unique) > 0 else 20
    h2 = unique[1] if len(unique) > 1 else 16
    h3 = unique[2] if len(unique) > 2 else 13
    h4 = unique[3] if len(unique) > 3 else 11

    print(f"  Font thresholds → h1≥{h1}  h2≥{h2}  h3≥{h3}  h4≥{h4}")
    return {"h1": h1, "h2": h2, "h3": h3, "h4": h4}


def extract_page_markdown(page: fitz.Page, thresholds: dict) -> str:
    """Extract a single page's text as markdown."""
    blocks = page.get_text("dict")["blocks"]
    lines_out: list[str] = []

    for block in blocks:
        if block.get("type") != 0:  # skip image blocks
            continue

        block_lines: list[str] = []
        for line in block.get("lines", []):
            spans = line.get("spans", [])
            if not spans:
                continue

            # Dominant font size for the line (max span size)
            dominant_size = max(s["size"] for s in spans)
            line_text = " ".join(s["text"] for s in spans).strip()
            line_text = clean_text(line_text)

            if not line_text:
                continue

            level = classify_heading(dominant_size, thresholds)
            if level:
                prefix = "#" * level
                block_lines.append(f"\n{prefix} {line_text}\n")
            else:
                block_lines.append(line_text)

        if block_lines:
            # Join body lines within a block as a paragraph
            paragraph = " ".join(
                l for l in block_lines if not l.startswith("\n#")
            )
            headings = [l for l in block_lines if l.startswith("\n#")]
            for h in headings:
                lines_out.append(h)
            if paragraph.strip():
                lines_out.append(paragraph.strip())

    return "\n\n".join(lines_out)


def convert(pdf_path: Path, out_path: Path) -> None:
    print(f"Opening: {pdf_path}")
    doc = fitz.open(str(pdf_path))
    total = len(doc)
    print(f"  Pages: {total}")

    thresholds = get_size_thresholds(doc)

    pages_md: list[str] = []
    for i, page in enumerate(doc):
        if i % 50 == 0:
            print(f"  Processing page {i + 1}/{total}…")
        md = extract_page_markdown(page, thresholds)
        if md.strip():
            pages_md.append(md)

    doc.close()

    full_md = "\n\n---\n\n".join(pages_md)

    # Post-processing: collapse 3+ blank lines into 2
    full_md = re.sub(r"\n{3,}", "\n\n", full_md)

    out_path.write_text(full_md, encoding="utf-8")
    size_kb = out_path.stat().st_size / 1024
    print(f"\nSaved → {out_path}  ({size_kb:.0f} KB)")


if __name__ == "__main__":
    if not PDF_PATH.exists():
        print(f"ERROR: PDF not found at {PDF_PATH}", file=sys.stderr)
        sys.exit(1)
    convert(PDF_PATH, OUT_PATH)
