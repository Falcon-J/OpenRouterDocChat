from pypdf import PdfReader
from pathlib import Path

class DocumentLoader:
    """Load text from multiple document types. Keep functions small and testable."""

    @staticmethod
    def load_pdf(path: str) -> str:
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"File not found: {path}")
        reader = PdfReader(path)
        pages = []
        for page in reader.pages:
            # extract_text() may return None
            txt = page.extract_text()
            if txt:
                pages.append(txt)
        text = "\n".join(pages).strip()
        if not text:
            raise ValueError("No extractable text found in PDF")
        return text

    @staticmethod
    def load_txt(path: str) -> str:
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"File not found: {path}")
        return p.read_text(encoding="utf-8")

    @staticmethod
    def chunk_text(text: str, chunk_size: int = 3000, overlap: int = 200) -> list:
        """Rudimentary chunker by characters (safe for tokens approx). Returns list of chunks."""
        if chunk_size <= overlap:
            raise ValueError("chunk_size must be greater than overlap")
        chunks = []
        start = 0
        length = len(text)
        while start < length:
            end = start + chunk_size
            chunks.append(text[start:end])
            start = end - overlap
        return chunks
