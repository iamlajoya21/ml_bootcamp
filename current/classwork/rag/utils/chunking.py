import os
from typing import List, Dict, Any


def chunk_text(
    text: str, 
    method: str = "fixed", 
    chunk_size: int = 500, 
    overlap: int = 50
) -> List[str]:
    """
    Chunk text using specified method.
    
    Args:
        text: Input text to chunk
        method: 'fixed', 'recursive', or 'semantic'
        chunk_size: Target size for each chunk
        overlap: Number of characters to overlap between chunks
    
    Returns:
        List of text chunks
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    if overlap < 0 or (method == "fixed" and overlap >= chunk_size):
        raise ValueError("overlap must be non-negative and less than chunk_size")
    
    if method == "fixed":
        return _fixed_size_chunking(text, chunk_size, overlap)
    elif method == "recursive":
        return _recursive_chunking(text, chunk_size)
    elif method == "semantic":
        return _semantic_chunking(text, chunk_size)
    else:
        raise ValueError(f"Unknown method: {method}")


def _fixed_size_chunking(text: str, chunk_size: int, overlap: int) -> List[str]:
    """Split text into fixed-size chunks with overlap."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks


def _recursive_chunking(text: str, chunk_size: int) -> List[str]:
    """Recursively split text by paragraphs, then sentences."""
    # First try splitting by paragraphs
    paragraphs = text.split('\n\n')
    
    chunks = []
    current_chunk = ""
    
    for para in paragraphs:
        # Check if adding this paragraph would exceed chunk_size
        if len(current_chunk) + len(para) + 2 <= chunk_size:  # +2 for \n\n
            current_chunk += para + "\n\n"
        else:
            # Save current chunk if it has content
            if current_chunk:
                chunks.append(current_chunk.strip())
            
            # If paragraph is too large, split by sentences
            if len(para) > chunk_size:
                sentences = para.split('. ')
                current_chunk = ""
                for sentence in sentences:
                    if len(current_chunk) + len(sentence) + 2 <= chunk_size:
                        current_chunk += sentence + ". "
                    else:
                        if current_chunk:
                            chunks.append(current_chunk.strip())
                        current_chunk = sentence + ". "
            else:
                # Start new chunk with this paragraph
                current_chunk = para + "\n\n"
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks


def _semantic_chunking(text: str, chunk_size: int) -> List[str]:
    """Chunk based on sentence boundaries and semantic similarity."""
    # Simple semantic chunking: split by sentences, then group similar ones
    sentences = text.split('. ')
    chunks = []
    current_chunk = []
    current_length = 0
    
    for sentence in sentences:
        sentence_length = len(sentence)
        
        if current_length + sentence_length <= chunk_size:
            current_chunk.append(sentence)
            current_length += sentence_length
        else:
            if current_chunk:
                chunks.append('. '.join(current_chunk) + '.')
            current_chunk = [sentence]
            current_length = sentence_length
    
    if current_chunk:
        chunks.append('. '.join(current_chunk) + '.')
    
    return chunks


def chunk_document(
    file_path: str, 
    method: str = "fixed", 
    chunk_size: int = 500, 
    overlap: int = 50
) -> List[Dict[str, Any]]:
    """
    Chunk a document file.
    
    Args:
        file_path: Path to the document
        method: Chunking method
        chunk_size: Target chunk size
        overlap: Overlap size
    
    Returns:
        List of dictionaries with 'text' and 'metadata' keys
    """
    # Read file based on extension
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == '.txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    elif ext == '.pdf':
        try:
            import pypdf
            reader = pypdf.PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
        except ImportError:
            raise ImportError("pypdf is required for PDF processing")
    elif ext in ['.html', '.htm']:
        try:
            from bs4 import BeautifulSoup
            import requests
            
            if file_path.startswith('http'):
                response = requests.get(file_path)
                soup = BeautifulSoup(response.content, 'html.parser')
            else:
                with open(file_path, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f.read(), 'html.parser')
            
            text = soup.get_text(separator=' ', strip=True)
        except ImportError:
            raise ImportError("beautifulsoup4 and requests are required for HTML processing")
    else:
        raise ValueError(f"Unsupported file extension: {ext}")
    
    # Chunk the text
    text_chunks = chunk_text(text, method, chunk_size, overlap)
    
    # Create chunk objects with metadata
    chunks = []
    for i, chunk_text_content in enumerate(text_chunks):
        chunk = {
            'text': chunk_text_content,
            'metadata': {
                'source': file_path,
                'chunk_index': i,
                'chunk_method': method,
                'chunk_size': chunk_size,
                'overlap': overlap
            }
        }
        chunks.append(chunk)
    
    return chunks


def get_chunk_stats(chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Get statistics about chunks.
    
    Args:
        chunks: List of chunk dictionaries
    
    Returns:
        Dictionary with chunk statistics
    """
    if not chunks:
        return {
            'count': 0,
            'avg_length': 0,
            'min_length': 0,
            'max_length': 0,
            'total_length': 0
        }
    
    lengths = [len(chunk['text']) for chunk in chunks]
    
    return {
        'count': len(chunks),
        'avg_length': sum(lengths) / len(lengths),
        'min_length': min(lengths),
        'max_length': max(lengths),
        'total_length': sum(lengths)
    }