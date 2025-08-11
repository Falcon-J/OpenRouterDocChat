from src.loader import DocumentLoader
import pytest

def test_chunker_basic():
    text = 'a'*10000
    chunks = DocumentLoader.chunk_text(text, chunk_size=3000, overlap=200)
    assert len(chunks) > 0
    assert ''.join(chunks).replace('\n','').count('a') >= 10000
