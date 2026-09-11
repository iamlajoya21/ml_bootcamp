import pytest
from utils.chunking import chunk_text, chunk_document, get_chunk_stats


def test_chunk_text_fixed_size():
    text = "This is a test sentence. " * 100  # Long text
    chunks = chunk_text(text, method="fixed", chunk_size=100, overlap=20)
    assert len(chunks) > 0
    assert all(len(chunk) <= 150 for chunk in chunks)  # Allow some flexibility
    assert len(chunks[0]) <= 100 + 20


def test_chunk_text_recursive():
    text = "Paragraph one.\n\nParagraph two.\n\nParagraph three."
    chunks = chunk_text(text, method="recursive", chunk_size=30)
    assert len(chunks) >= 2
    assert "Paragraph one" in chunks[0]


def test_chunk_text_semantic():
    text = "Machine learning is great. It has many applications. Deep learning is a subset of ML. It uses neural networks."
    chunks = chunk_text(text, method="semantic", chunk_size=100)
    assert len(chunks) >= 1
    assert any("machine learning" in chunk.lower() for chunk in chunks)


def test_chunk_document_txt():
    # Create a temporary text file
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("Test document content for chunking.")
        temp_path = f.name
    
    chunks = chunk_document(temp_path)
    assert len(chunks) >= 1
    assert "Test document content" in chunks[0]['text']


def test_get_chunk_stats():
    chunks = [
        {"text": "Short", "metadata": {}},
        {"text": "Medium length text here", "metadata": {}},
        {"text": "This is a longer piece of text for testing", "metadata": {}}
    ]
    stats = get_chunk_stats(chunks)
    assert stats['count'] == 3
    assert stats['avg_length'] > 0
    assert stats['min_length'] == len("Short")
    assert stats['max_length'] == len("This is a longer piece of text for testing")


def test_chunk_text_overlap_validation():
    """Test that overlap >= chunk_size raises ValueError."""
    text = "Test text for validation"
    with pytest.raises(ValueError):
        chunk_text(text, method="fixed", chunk_size=100, overlap=100)
    with pytest.raises(ValueError):
        chunk_text(text, method="fixed", chunk_size=100, overlap=150)


def test_chunk_text_size_validation():
    """Test that chunk_size <= 0 raises ValueError."""
    text = "Test text for validation"
    with pytest.raises(ValueError):
        chunk_text(text, method="fixed", chunk_size=0, overlap=0)
    with pytest.raises(ValueError):
        chunk_text(text, method="fixed", chunk_size=-10, overlap=0)
