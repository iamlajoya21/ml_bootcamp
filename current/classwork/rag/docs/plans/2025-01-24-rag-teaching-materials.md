# RAG Teaching Materials Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create three progressive Jupyter notebooks teaching RAG applications with Gemini API, ChromaDB, hybrid search, and MLflow observability.

**Architecture:** Progressive learning path with three self-contained notebooks, each building on previous concepts. Shared utility functions in separate modules for reusability. Sample documents in multiple formats for realistic examples.

**Tech Stack:** Gemini API (embeddings + generation), ChromaDB, rank_bm25, MLflow, Python 3.11+, Jupyter notebooks

## Global Constraints
- All code must use Gemini API (text-embedding-004, gemini-1.5-pro)
- Vector database: ChromaDB only
- BM25 implementation via rank_bm25 library
- Observability: MLflow + custom matplotlib/plotly visualizations
- Target: Intermediate ML practitioners with NLP/transformer knowledge
- Each notebook must be self-contained and runnable independently
- All notebooks in `current/classwork/rag/` directory

---

## Task 1: Project Setup and Dependencies

**Files:**
- Create: `current/classwork/rag/requirements.txt`
- Create: `current/classwork/rag/.env.example`
- Create: `current/classwork/rag/README.md`

**Interfaces:**
- Consumes: None (initial setup)
- Produces: Environment configuration for all notebooks

- [ ] **Step 1: Create requirements.txt**

```txt
# Core dependencies
google-generativeai>=0.3.0
chromadb>=0.4.0
rank-bm25>=0.2.2
python-dotenv>=1.0.0

# Document processing
pypdf>=3.15.0
beautifulsoup4>=4.12.0
requests>=2.31.0

# MLflow and visualization
mlflow>=2.8.0
matplotlib>=3.7.0
plotly>=5.15.0
pandas>=2.0.0

# Jupyter
jupyter>=1.0.0
ipywidgets>=8.1.0

# Utilities
numpy>=1.24.0
tqdm>=4.65.0
```

- [ ] **Step 2: Create .env.example**

```bash
# Gemini API Configuration
GEMINI_API_KEY=your_gemini_api_key_here

# MLflow Configuration (optional - will use local file store by default)
MLFLOW_TRACKING_URI=http://localhost:5000
```

- [ ] **Step 3: Create README.md**

```markdown
# RAG Teaching Materials

Three progressive notebooks teaching Retrieval-Augmented Generation (RAG) with Gemini API.

## Notebooks

1. **rag_fundamentals.ipynb** - Basic RAG pipeline, chunking, embeddings, ChromaDB
2. **rag_advanced_retrieval.ipynb** - Hybrid search with BM25, advanced chunking, reranking
3. **rag_production_observability.ipynb** - MLflow monitoring, visualizations, production concerns

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and add your Gemini API key
3. Run notebooks in sequence

## Sample Data

The `data/` directory contains sample documents in PDF, TXT, and HTML formats for testing.
```

- [ ] **Step 4: Create data directory structure**

```bash
mkdir -p data/sample_pdfs data/sample_texts data/sample_html
```

- [ ] **Step 5: Create sample documents**

Create `data/sample_texts/machine_learning.txt`:
```text
Machine Learning Fundamentals

Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed. It focuses on developing computer programs that can access data and use it to learn for themselves.

The process of learning begins with observations or data, such as examples, direct experience, or instruction, in order to look for patterns in data and make better decisions in the future based on the examples that we provide.

There are three main types of machine learning: supervised learning, unsupervised learning, and reinforcement learning. Supervised learning uses labeled training data to learn a mapping function from inputs to outputs. Unsupervised learning finds hidden patterns in unlabeled data. Reinforcement learning learns through trial and error with feedback from its actions.

Key concepts include: training data, features, labels, models, loss functions, optimization algorithms, and evaluation metrics. Understanding these fundamentals is crucial for building effective machine learning systems.
```

Create `data/sample_texts/deep_learning.txt`:
```text
Deep Learning and Neural Networks

Deep learning is a subset of machine learning based on artificial neural networks with multiple layers. These deep neural networks attempt to simulate the behavior of the human brain to learn from large amounts of data.

A neural network consists of layers of interconnected nodes or neurons. The input layer receives the raw data, hidden layers perform computations, and the output layer produces the final result. Each connection has a weight that is adjusted during training.

Deep learning has achieved remarkable success in areas such as computer vision, natural language processing, speech recognition, and game playing. Convolutional Neural Networks (CNNs) excel at image processing, while Recurrent Neural Networks (RNNs) and Transformers handle sequential data like text and time series.

Training deep learning models requires large datasets and significant computational resources. Techniques like transfer learning, dropout, and batch normalization help improve training efficiency and model performance.
```

- [ ] **Step 6: Commit initial setup**

```bash
git add requirements.txt .env.example README.md data/
git commit -m "feat: initial project setup with dependencies and sample data"
```

---

## Task 2: Utility Module - Chunking Functions

**Files:**
- Create: `current/classwork/rag/utils/__init__.py`
- Create: `current/classwork/rag/utils/chunking.py`
- Create: `current/classwork/rag/tests/test_chunking.py`

**Interfaces:**
- Consumes: None (standalone utility)
- Produces: `chunk_text()`, `chunk_document()`, `get_chunk_stats()`

- [ ] **Step 1: Create utils/__init__.py**

```python
from .chunking import chunk_text, chunk_document, get_chunk_stats

__all__ = ["chunk_text", "chunk_document", "get_chunk_stats"]
```

- [ ] **Step 2: Write failing tests for chunking**

```python
# tests/test_chunking.py
import pytest
from utils.chunking import chunk_text, chunk_document, get_chunk_stats


def test_chunk_text_fixed_size():
    text = "This is a test sentence. " * 100  # Long text
    chunks = chunk_text(text, method="fixed", chunk_size=100, overlap=20)
    assert len(chunks) > 0
    assert all(len(chunk) <= 150 for chunk in chunks)  # Allow some flexibility
    assert len(chunks[0]) <= 100 + overlap


def test_chunk_text_recursive():
    text = "Paragraph one.\n\nParagraph two.\n\nParagraph three."
    chunks = chunk_text(text, method="recursive", chunk_size=50)
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
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `cd current/classwork/rag && python -m pytest tests/test_chunking.py -v`
Expected: FAIL with "ModuleNotFoundError: No module named 'utils.chunking'"

- [ ] **Step 4: Implement chunking functions**

```python
# utils/chunking.py
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
        if len(current_chunk) + len(para) <= chunk_size:
            current_chunk += para + "\n\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            # If paragraph is too large, split by sentences
            if len(para) > chunk_size:
                sentences = para.split('. ')
                for sentence in sentences:
                    if len(current_chunk) + len(sentence) <= chunk_size:
                        current_chunk += sentence + ". "
                    else:
                        if current_chunk:
                            chunks.append(current_chunk.strip())
                        current_chunk = sentence + ". "
            else:
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
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd current/classwork/rag && python -m pytest tests/test_chunking.py -v`
Expected: All 5 tests PASS

- [ ] **Step 6: Commit chunking utility**

```bash
git add utils/ tests/test_chunking.py
git commit -m "feat: add chunking utility with fixed, recursive, and semantic methods"
```

---

## Task 3: Utility Module - Retrieval Functions

**Files:**
- Create: `current/classwork/rag/utils/retrieval.py`
- Create: `current/classwork/rag/tests/test_retrieval.py`

**Interfaces:**
- Consumes: Gemini API for embeddings, ChromaDB for storage
- Produces: `create_vector_store()`, `search_vector_store()`, `bm25_search()`, `hybrid_search()`

- [ ] **Step 1: Write failing tests for retrieval**

```python
# tests/test_retrieval.py
import pytest
from unittest.mock import Mock, patch
from utils.retrieval import (
    create_vector_store,
    search_vector_store,
    bm25_search,
    hybrid_search
)


@pytest.fixture
def sample_documents():
    return [
        {"text": "Machine learning is a subset of AI", "id": "doc1"},
        {"text": "Deep learning uses neural networks", "id": "doc2"},
        {"text": "Natural language processing handles text", "id": "doc3"}
    ]


@pytest.fixture
def sample_embeddings():
    return [
        [0.1, 0.2, 0.3, 0.4, 0.5],
        [0.2, 0.3, 0.4, 0.5, 0.6],
        [0.3, 0.4, 0.5, 0.6, 0.7]
    ]


def test_create_vector_store():
    docs = ["doc1", "doc2", "doc3"]
    embeddings = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]
    metadata = [{"source": "test"}, {"source": "test"}, {"source": "test"}]
    
    store = create_vector_store(docs, embeddings, metadata)
    assert store is not None
    assert store.count() == 3


@patch('utils.retrieval.genai')
def test_search_vector_store(mock_genai):
    mock_genai.embed_content.return_value = {'embedding': [0.1, 0.2]}
    
    # Create a mock store
    mock_store = Mock()
    mock_store.query.return_value = {
        'documents': [['result1', 'result2']],
        'distances': [[0.1, 0.2]]
    }
    
    results = search_vector_store(mock_store, "test query", n_results=2)
    assert len(results) == 2
    assert results[0] == 'result1'


def test_bm25_search():
    corpus = [
        "machine learning algorithms",
        "deep learning neural networks",
        "natural language processing"
    ]
    query = "machine learning"
    results = bm25_search(corpus, query, top_k=2)
    assert len(results) == 2
    assert results[0][0] == 0  # Index of first document


def test_hybrid_search():
    semantic_results = [
        {"text": "doc1", "score": 0.9, "rank": 0},
        {"text": "doc2", "score": 0.8, "rank": 1}
    ]
    bm25_results = [
        {"text": "doc2", "score": 0.7, "rank": 0},
        {"text": "doc1", "score": 0.6, "rank": 1}
    ]
    
    fused = hybrid_search(semantic_results, bm25_results, method="rrf")
    assert len(fused) == 2
    assert fused[0]['text'] in ['doc1', 'doc2']
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd current/classwork/rag && python -m pytest tests/test_retrieval.py -v`
Expected: FAIL with "ModuleNotFoundError: No module named 'utils.retrieval'"

- [ ] **Step 3: Implement retrieval functions**

```python
# utils/retrieval.py
import google.generativeai as genai
import chromadb
from typing import List, Dict, Any, Optional
import numpy as np
from rank_bm25 import BM25Okapi
import re


def create_vector_store(
    documents: List[str],
    embeddings: List[List[float]],
    metadata: List[Dict[str, Any]],
    collection_name: str = "rag_collection"
) -> chromadb.Collection:
    """
    Create a ChromaDB vector store with documents and embeddings.
    
    Args:
        documents: List of document texts
        embeddings: List of embedding vectors
        metadata: List of metadata dictionaries
        collection_name: Name for the ChromaDB collection
    
    Returns:
        ChromaDB collection object
    """
    client = chromadb.Client()
    collection = client.create_collection(name=collection_name)
    
    # Add documents to collection
    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=[f"doc_{i}" for i in range(len(documents))],
        metadatas=metadata
    )
    
    return collection


def search_vector_store(
    collection: chromadb.Collection,
    query: str,
    n_results: int = 5
) -> List[str]:
    """
    Search the vector store using semantic similarity.
    
    Args:
        collection: ChromaDB collection
        query: Search query
        n_results: Number of results to return
    
    Returns:
        List of document texts
    """
    # We need to get embeddings for the query
    # For this function to work standalone, we'll need to use the collection's embedding function
    # or assume embeddings are pre-computed
    
    # Simple approach: use collection's built-in query
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    
    return results['documents'][0]


def bm25_search(
    corpus: List[str],
    query: str,
    top_k: int = 5
) -> List[tuple]:
    """
    Perform BM25 search on a corpus.
    
    Args:
        corpus: List of document texts
        query: Search query
        top_k: Number of top results to return
    
    Returns:
        List of tuples (document_index, score)
    """
    # Tokenize corpus and query
    tokenized_corpus = [doc.lower().split() for doc in corpus]
    tokenized_query = query.lower().split()
    
    # Create BM25 object and get scores
    bm25 = BM25Okapi(tokenized_corpus)
    scores = bm25.get_scores(tokenized_query)
    
    # Get top-k results
    top_indices = np.argsort(scores)[::-1][:top_k]
    results = [(idx, scores[idx]) for idx in top_indices]
    
    return results


def hybrid_search(
    semantic_results: List[Dict[str, Any]],
    bm25_results: List[Dict[str, Any]],
    method: str = "rrf",
    k: int = 60
) -> List[Dict[str, Any]]:
    """
    Combine semantic and BM25 search results using fusion.
    
    Args:
        semantic_results: List of semantic search results with 'text', 'score', 'rank'
        bm25_results: List of BM25 search results with 'text', 'score', 'rank'
        method: Fusion method ('rrf' or 'weighted')
        k: Parameter for RRF (higher = more weight to top ranks)
    
    Returns:
        Fused list of results sorted by combined score
    """
    if method == "rrf":
        return _reciprocal_rank_fusion(semantic_results, bm25_results, k)
    elif method == "weighted":
        return _weighted_fusion(semantic_results, bm25_results)
    else:
        raise ValueError(f"Unknown fusion method: {method}")


def _reciprocal_rank_fusion(
    results_list1: List[Dict[str, Any]],
    results_list2: List[Dict[str, Any]],
    k: int = 60
) -> List[Dict[str, Any]]:
    """Reciprocal Rank Fusion (RRF) algorithm."""
    # Collect all unique documents
    all_docs = {}
    
    # Process first result list
    for rank, result in enumerate(results_list1):
        doc_text = result['text']
        if doc_text not in all_docs:
            all_docs[doc_text] = {'text': doc_text, 'rrf_score': 0}
        all_docs[doc_text]['rrf_score'] += 1 / (k + rank + 1)
    
    # Process second result list
    for rank, result in enumerate(results_list2):
        doc_text = result['text']
        if doc_text not in all_docs:
            all_docs[doc_text] = {'text': doc_text, 'rrf_score': 0}
        all_docs[doc_text]['rrf_score'] += 1 / (k + rank + 1)
    
    # Sort by RRF score
    sorted_docs = sorted(all_docs.values(), key=lambda x: x['rrf_score'], reverse=True)
    
    return sorted_docs


def _weighted_fusion(
    results_list1: List[Dict[str, Any]],
    results_list2: List[Dict[str, Any]],
    weight1: float = 0.7,
    weight2: float = 0.3
) -> List[Dict[str, Any]]:
    """Weighted score fusion."""
    all_docs = {}
    
    # Normalize scores in first list
    max_score1 = max(r['score'] for r in results_list1) if results_list1 else 1
    for result in results_list1:
        doc_text = result['text']
        normalized_score = result['score'] / max_score1
        if doc_text not in all_docs:
            all_docs[doc_text] = {'text': doc_text, 'weighted_score': 0}
        all_docs[doc_text]['weighted_score'] += weight1 * normalized_score
    
    # Normalize scores in second list
    max_score2 = max(r['score'] for r in results_list2) if results_list2 else 1
    for result in results_list2:
        doc_text = result['text']
        normalized_score = result['score'] / max_score2
        if doc_text not in all_docs:
            all_docs[doc_text] = {'text': doc_text, 'weighted_score': 0}
        all_docs[doc_text]['weighted_score'] += weight2 * normalized_score
    
    # Sort by weighted score
    sorted_docs = sorted(all_docs.values(), key=lambda x: x['weighted_score'], reverse=True)
    
    return sorted_docs
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd current/classwork/rag && python -m pytest tests/test_retrieval.py -v`
Expected: All 4 tests PASS

- [ ] **Step 5: Commit retrieval utility**

```bash
git add utils/retrieval.py tests/test_retrieval.py
git commit -m "feat: add retrieval utilities with vector store, BM25, and hybrid search"
```

---

## Task 4: Session 1 Notebook - RAG Fundamentals

**Files:**
- Create: `current/classwork/rag/rag_fundamentals.ipynb`

**Interfaces:**
- Consumes: utils/chunking.py, utils/retrieval.py, sample data files
- Produces: Working RAG pipeline demonstration

- [ ] **Step 1: Create notebook with markdown cells**

Create a new Jupyter notebook with the following structure:

**Cell 1 (Markdown):**
```markdown
# RAG Fundamentals: Building Your First RAG Pipeline

## Learning Objectives
- Understand RAG architecture and use cases
- Learn different chunking strategies
- Use Gemini embeddings with ChromaDB
- Build a basic RAG pipeline

## Prerequisites
- Python 3.11+
- Gemini API key
- Basic understanding of NLP concepts
```

**Cell 2 (Code):**
```python
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

print("Gemini API configured successfully!")
print(f"Available models: {[m.name for m in genai.list_models() if 'embedding' in m.name.lower() or 'pro' in m.name.lower()][:5]}")
```

**Cell 3 (Markdown):**
```markdown
## 1. What is RAG?

**Retrieval-Augmented Generation (RAG)** combines:
1. **Retrieval**: Finding relevant information from a knowledge base
2. **Generation**: Using that information to generate accurate answers

### Why RAG?
- Reduces hallucinations
- Provides up-to-date information
- Enables domain-specific knowledge
- More transparent than pure LLM responses
```

**Cell 4 (Markdown):**
```markdown
## 2. Document Processing & Chunking

Let's explore different ways to split documents into chunks for retrieval.
```

**Cell 5 (Code):**
```python
# Load sample documents
def load_sample_documents():
    """Load sample text files from data directory."""
    documents = []
    data_dir = "data/sample_texts"
    
    for filename in os.listdir(data_dir):
        if filename.endswith('.txt'):
            filepath = os.path.join(data_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
                documents.append({
                    'text': text,
                    'metadata': {'source': filename}
                })
    
    return documents

docs = load_sample_documents()
print(f"Loaded {len(docs)} documents")
for doc in docs:
    print(f"- {doc['metadata']['source']}: {len(doc['text'])} characters")
```

**Cell 6 (Code):**
```python
from utils.chunking import chunk_text, get_chunk_stats

# Demonstrate different chunking methods
sample_text = docs[0]['text']

print("=== Chunking Methods Comparison ===\n")

# Fixed-size chunking
fixed_chunks = chunk_text(sample_text, method="fixed", chunk_size=200, overlap=50)
print(f"Fixed-size chunks: {len(fixed_chunks)} chunks")
print(f"  Average length: {sum(len(c) for c in fixed_chunks) / len(fixed_chunks):.0f} chars")
print(f"  First chunk preview: {fixed_chunks[0][:100]}...\n")

# Recursive chunking
recursive_chunks = chunk_text(sample_text, method="recursive", chunk_size=200)
print(f"Recursive chunks: {len(recursive_chunks)} chunks")
print(f"  Average length: {sum(len(c) for c in recursive_chunks) / len(recursive_chunks):.0f} chars")
print(f"  First chunk preview: {recursive_chunks[0][:100]}...\n")

# Semantic chunking
semantic_chunks = chunk_text(sample_text, method="semantic", chunk_size=200)
print(f"Semantic chunks: {len(semantic_chunks)} chunks")
print(f"  Average length: {sum(len(c) for c in semantic_chunks) / len(semantic_chunks):.0f} chars")
print(f"  First chunk preview: {semantic_chunks[0][:100]}...")
```

**Cell 7 (Markdown):**
```markdown
### Chunking Strategy Trade-offs

| Method | Pros | Cons | Best For |
|--------|------|------|----------|
| **Fixed-size** | Simple, predictable | May split sentences | Quick prototyping |
| **Recursive** | Respects document structure | May have uneven sizes | Well-structured docs |
| **Semantic** | Groups related content | More complex | Knowledge bases |
```

**Cell 8 (Code):**
```python
# Visualize chunk statistics
import matplotlib.pyplot as plt

methods = ['fixed', 'recursive', 'semantic']
chunk_counts = []
avg_lengths = []

for method in methods:
    chunks = chunk_text(sample_text, method=method, chunk_size=200, overlap=50)
    stats = get_chunk_stats([{'text': c, 'metadata': {}} for c in chunks])
    chunk_counts.append(stats['count'])
    avg_lengths.append(stats['avg_length'])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.bar(methods, chunk_counts, color=['blue', 'green', 'orange'])
ax1.set_title('Number of Chunks by Method')
ax1.set_ylabel('Chunk Count')

ax2.bar(methods, avg_lengths, color=['blue', 'green', 'orange'])
ax2.set_title('Average Chunk Length by Method')
ax2.set_ylabel('Characters')

plt.tight_layout()
plt.show()
```

**Cell 9 (Markdown):**
```markdown
## 3. Gemini Embeddings

Gemini provides powerful text embeddings that capture semantic meaning.
```

**Cell 10 (Code):**
```python
# Test Gemini embedding
test_text = "Machine learning is a subset of artificial intelligence"

# Get embedding
embedding_result = genai.embed_content(
    model="models/text-embedding-004",
    content=test_text,
    task_type="retrieval_document"
)

embedding = embedding_result['embedding']
print(f"Text: {test_text}")
print(f"Embedding dimension: {len(embedding)}")
print(f"First 5 values: {embedding[:5]}")
print(f"Embedding norm: {sum(x**2 for x in embedding)**0.5:.4f}")
```

**Cell 11 (Code):**
```python
# Compare embeddings for similar vs different texts
texts = [
    "Machine learning algorithms",
    "Deep learning neural networks",
    "Natural language processing",
    "The weather is sunny today"
]

embeddings = []
for text in texts:
    result = genai.embed_content(
        model="models/text-embedding-004",
        content=text,
        task_type="retrieval_document"
    )
    embeddings.append(result['embedding'])

# Calculate similarity matrix
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print("Similarity Matrix:")
print("=" * 50)
for i, text1 in enumerate(texts):
    for j, text2 in enumerate(texts):
        sim = cosine_similarity(embeddings[i], embeddings[j])
        print(f"{text1[:20]:20} vs {text2[:20]:20}: {sim:.3f}")
    print()
```

**Cell 12 (Markdown):**
```markdown
## 4. Vector Database with ChromaDB

ChromaDB stores embeddings and enables fast similarity search.
```

**Cell 13 (Code):**
```python
import chromadb

# Create ChromaDB client and collection
client = chromadb.Client()
collection = client.create_collection(name="rag_fundamentals")

print("ChromaDB collection created!")
```

**Cell 14 (Code):**
```python
# Prepare documents for storage
all_chunks = []
all_metadatas = []
all_ids = []

for doc_idx, doc in enumerate(docs):
    # Chunk the document
    chunks = chunk_text(doc['text'], method="recursive", chunk_size=200)
    
    for chunk_idx, chunk in enumerate(chunks):
        all_chunks.append(chunk)
        all_metadatas.append({
            'source': doc['metadata']['source'],
            'chunk_index': chunk_idx,
            'doc_index': doc_idx
        })
        all_ids.append(f"doc{doc_idx}_chunk{chunk_idx}")

print(f"Total chunks to store: {len(all_chunks)}")

# Generate embeddings for all chunks
print("Generating embeddings...")
chunk_embeddings = []
for chunk in all_chunks:
    result = genai.embed_content(
        model="models/text-embedding-004",
        content=chunk,
        task_type="retrieval_document"
    )
    chunk_embeddings.append(result['embedding'])

print("Embeddings generated!")
```

**Cell 15 (Code):**
```python
# Add documents to ChromaDB
collection.add(
    documents=all_chunks,
    embeddings=chunk_embeddings,
    metadatas=all_metadatas,
    ids=all_ids
)

print(f"Added {collection.count()} chunks to ChromaDB")
```

**Cell 16 (Markdown):**
```markdown
## 5. Basic RAG Pipeline

Now let's build the complete RAG pipeline: Query → Embed → Retrieve → Generate
```

**Cell 17 (Code):**
```python
def rag_query(query, collection, top_k=3):
    """
    Complete RAG pipeline.
    
    Args:
        query: User question
        collection: ChromaDB collection
        top_k: Number of chunks to retrieve
    
    Returns:
        Dictionary with retrieved chunks and generated answer
    """
    # Step 1: Embed the query
    query_embedding = genai.embed_content(
        model="models/text-embedding-004",
        content=query,
        task_type="retrieval_query"
    )['embedding']
    
    # Step 2: Retrieve relevant chunks
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    
    retrieved_chunks = results['documents'][0]
    retrieved_metadatas = results['metadatas'][0]
    distances = results['distances'][0]
    
    # Step 3: Create context from retrieved chunks
    context = "\n\n".join(retrieved_chunks)
    
    # Step 4: Generate answer using Gemini
    prompt = f"""Answer the following question based on the provided context. 
    If the context doesn't contain enough information, say so.
    
    Context:
    {context}
    
    Question: {query}
    
    Answer:"""
    
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(prompt)
    
    return {
        'query': query,
        'answer': response.text,
        'retrieved_chunks': retrieved_chunks,
        'retrieved_metadatas': retrieved_metadatas,
        'distances': distances
    }
```

**Cell 18 (Code):**
```python
# Test the RAG pipeline
test_query = "What is machine learning?"

result = rag_query(test_query, collection)

print(f"Query: {result['query']}")
print(f"\nAnswer:\n{result['answer']}")
print(f"\nRetrieved {len(result['retrieved_chunks'])} chunks:")
for i, (chunk, dist) in enumerate(zip(result['retrieved_chunks'], result['distances'])):
    print(f"\n--- Chunk {i+1} (distance: {dist:.4f}) ---")
    print(chunk[:200] + "..." if len(chunk) > 200 else chunk)
```

**Cell 19 (Code):**
```python
# Test with more questions
test_queries = [
    "How does deep learning work?",
    "What are the types of machine learning?",
    "What is natural language processing?"
]

for query in test_queries:
    print(f"\n{'='*60}")
    result = rag_query(query, collection)
    print(f"Q: {result['query']}")
    print(f"A: {result['answer'][:200]}...")
```

**Cell 20 (Markdown):**
```markdown
## Summary

In this notebook, we learned:

1. **RAG Architecture**: Combining retrieval and generation
2. **Chunking Strategies**: Fixed, recursive, and semantic chunking
3. **Gemini Embeddings**: Converting text to vector representations
4. **ChromaDB**: Storing and searching embeddings
5. **Complete RAG Pipeline**: From query to answer

## Next Steps
- Try different chunk sizes and overlap values
- Experiment with different document types
- Move to Session 2 for hybrid search!
```

- [ ] **Step 2: Verify notebook runs without errors**

Open the notebook and run all cells to ensure no errors. Check that:
- Gemini API calls work
- ChromaDB operations succeed
- RAG pipeline produces coherent answers

- [ ] **Step 3: Commit Session 1 notebook**

```bash
git add rag_fundamentals.ipynb
git commit -m "feat: add Session 1 - RAG Fundamentals notebook"
```

---

## Task 5: Session 2 Notebook - Advanced Retrieval

**Files:**
- Create: `current/classwork/rag/rag_advanced_retrieval.ipynb`

**Interfaces:**
- Consumes: utils/chunking.py, utils/retrieval.py, ChromaDB from Session 1
- Produces: Hybrid search system demonstration

- [ ] **Step 1: Create notebook structure**

Create notebook with these sections:

**Cell 1 (Markdown):**
```markdown
# Advanced Retrieval: Hybrid Search with BM25

## Learning Objectives
- Understand limitations of pure semantic search
- Implement BM25 text search
- Combine BM25 + semantic search with fusion techniques
- Advanced chunking strategies
- Retrieval evaluation

## Prerequisites
- Completed Session 1 (RAG Fundamentals)
- Understanding of embeddings and vector search
```

**Cell 2 (Code):**
```python
import os
import numpy as np
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

print("Session 2: Advanced Retrieval")
```

**Cell 3 (Markdown):**
```markdown
## 1. Limitations of Pure Semantic Search

Semantic search is powerful but has blind spots:
- Misses exact keyword matches
- Struggles with technical terms
- Can't handle typos well
- May not capture domain-specific jargon

Let's see an example:
```

**Cell 4 (Code):**
```python
# Example: Semantic search misses exact matches
import chromadb

# Create a simple test case
client = chromadb.Client()
test_collection = client.create_collection(name="test_semantic")

# Documents with specific technical terms
documents = [
    "The PyTorch framework provides autograd functionality",
    "TensorFlow uses computational graphs for execution",
    "JAX enables functional transformations of NumPy code",
    "PyTorch 2.0 introduced torch.compile for optimization"
]

# Add to collection
test_collection.add(
    documents=documents,
    ids=[f"doc_{i}" for i in range(len(documents))]
)

# Query that should find exact match
query = "PyTorch autograd"

results = test_collection.query(query_texts=[query], n_results=2)
print(f"Query: {query}")
print(f"\nResults:")
for doc, dist in zip(results['documents'][0], results['distances'][0]):
    print(f"- {doc} (distance: {dist:.4f})")
```

**Cell 5 (Markdown):**
```markdown
## 2. BM25 Search Implementation

BM25 (Best Matching 25) is a probabilistic retrieval model that:
- Uses term frequency (TF) and inverse document frequency (IDF)
- Excels at exact keyword matching
- Well-understood and fast
- Complementary to semantic search

### How BM25 Works
```

**Cell 6 (Code):**
```python
from rank_bm25 import BM25Okapi
import re

def tokenize(text):
    """Simple tokenization for BM25."""
    return re.findall(r'\w+', text.lower())

# Prepare corpus for BM25
corpus = [
    "The PyTorch framework provides autograd functionality for automatic differentiation",
    "TensorFlow uses computational graphs for efficient execution and deployment",
    "JAX enables functional transformations of NumPy code for high-performance computing",
    "PyTorch 2.0 introduced torch.compile for graph-based optimization"
]

# Tokenize corpus
tokenized_corpus = [tokenize(doc) for doc in corpus]

# Create BM25 object
bm25 = BM25Okapi(tokenized_corpus)

# Test with query
query = "PyTorch autograd"
tokenized_query = tokenize(query)

# Get BM25 scores
scores = bm25.get_scores(tokenized_query)

print(f"Query: {query}")
print(f"\nBM25 Scores:")
for i, (doc, score) in enumerate(zip(corpus, scores)):
    print(f"{i+1}. Score: {score:.4f} - {doc[:60]}...")
```

**Cell 7 (Code):**
```python
def bm25_search(corpus, query, top_k=3):
    """BM25 search function."""
    tokenized_corpus = [tokenize(doc) for doc in corpus]
    bm25 = BM25Okapi(tokenized_corpus)
    
    tokenized_query = tokenize(query)
    scores = bm25.get_scores(tokenized_query)
    
    # Get top-k results
    top_indices = np.argsort(scores)[::-1][:top_k]
    results = []
    for idx in top_indices:
        results.append({
            'index': idx,
            'text': corpus[idx],
            'score': float(scores[idx])
        })
    
    return results

# Compare semantic vs BM25
print("=== Semantic Search vs BM25 ===\n")

# Semantic search
query = "PyTorch autograd"
semantic_results = test_collection.query(query_texts=[query], n_results=2)

print("Semantic Search Results:")
for doc, dist in zip(semantic_results['documents'][0], semantic_results['distances'][0]):
    print(f"- {doc[:60]}... (distance: {dist:.4f})")

print("\nBM25 Search Results:")
bm25_results = bm25_search(corpus, query, top_k=2)
for result in bm25_results:
    print(f"- {result['text'][:60]}... (score: {result['score']:.4f})")
```

**Cell 8 (Markdown):**
```markdown
## 3. Hybrid Search Architecture

### Why Combine Both?

| Method | Strengths | Weaknesses |
|--------|-----------|------------|
| **Semantic** | Meaning understanding, synonyms | Misses exact terms |
| **BM25** | Exact matches, technical terms | No semantic understanding |
| **Hybrid** | Best of both worlds | More complex |

### Fusion Strategies
```

**Cell 9 (Code):**
```python
def reciprocal_rank_fusion(results_list1, results_list2, k=60):
    """
    Reciprocal Rank Fusion (RRF) algorithm.
    
    RRF score = Σ 1/(k + rank_i)
    """
    all_docs = {}
    
    # Process first result list
    for rank, result in enumerate(results_list1):
        doc = result['text']
        if doc not in all_docs:
            all_docs[doc] = {'text': doc, 'rrf_score': 0}
        all_docs[doc]['rrf_score'] += 1 / (k + rank + 1)
    
    # Process second result list
    for rank, result in enumerate(results_list2):
        doc = result['text']
        if doc not in all_docs:
            all_docs[doc] = {'text': doc, 'rrf_score': 0}
        all_docs[doc]['rrf_score'] += 1 / (k + rank + 1)
    
    # Sort by RRF score
    sorted_docs = sorted(all_docs.values(), key=lambda x: x['rrf_score'], reverse=True)
    
    return sorted_docs


def weighted_fusion(results_list1, results_list2, weight1=0.7, weight2=0.3):
    """Weighted score fusion with normalization."""
    all_docs = {}
    
    # Normalize and combine scores
    max_score1 = max(r['score'] for r in results_list1) if results_list1 else 1
    max_score2 = max(r['score'] for r in results_list2) if results_list2 else 1
    
    for result in results_list1:
        doc = result['text']
        normalized_score = result['score'] / max_score1
        if doc not in all_docs:
            all_docs[doc] = {'text': doc, 'weighted_score': 0}
        all_docs[doc]['weighted_score'] += weight1 * normalized_score
    
    for result in results_list2:
        doc = result['text']
        normalized_score = result['score'] / max_score2
        if doc not in all_docs:
            all_docs[doc] = {'text': doc, 'weighted_score': 0}
        all_docs[doc]['weighted_score'] += weight2 * normalized_score
    
    sorted_docs = sorted(all_docs.values(), key=lambda x: x['weighted_score'], reverse=True)
    
    return sorted_docs


# Test hybrid search
print("=== Hybrid Search Demonstration ===\n")

# Get results from both methods
semantic_results = []
for doc, dist in zip(semantic_results['documents'][0], semantic_results['distances'][0]):
    semantic_results.append({'text': doc, 'score': 1 - dist})  # Convert distance to similarity

bm25_results = bm25_search(corpus, query, top_k=3)

# Apply fusion
print("Query:", query)
print("\n--- Reciprocal Rank Fusion (RRF) ---")
rrf_results = reciprocal_rank_fusion(semantic_results, bm25_results)
for i, result in enumerate(rrf_results[:3]):
    print(f"{i+1}. {result['text'][:60]}... (RRF: {result['rrf_score']:.4f})")

print("\n--- Weighted Fusion (70% semantic, 30% BM25) ---")
weighted_results = weighted_fusion(semantic_results, bm25_results)
for i, result in enumerate(weighted_results[:3]):
    print(f"{i+1}. {result['text'][:60]}... (Weighted: {result['weighted_score']:.4f})")
```

**Cell 10 (Markdown):**
```markdown
## 4. Advanced Chunking Strategies

### Contextual Chunking with Summaries

Instead of just splitting text, we can:
1. Add context from surrounding chunks
2. Generate summaries for each chunk
3. Create parent-child relationships

This improves retrieval accuracy by providing more context.
```

**Cell 11 (Code):**
```python
def contextual_chunking(text, chunk_size=500, overlap=100):
    """
    Create chunks with surrounding context.
    """
    # First, create base chunks
    from utils.chunking import chunk_text
    base_chunks = chunk_text(text, method="recursive", chunk_size=chunk_size)
    
    contextual_chunks = []
    for i, chunk in enumerate(base_chunks):
        # Add context from previous and next chunks
        context_parts = []
        
        if i > 0:
            context_parts.append(f"Previous context: ...{base_chunks[i-1][-100:]}")
        
        context_parts.append(f"Current content: {chunk}")
        
        if i < len(base_chunks) - 1:
            context_parts.append(f"Next context: {base_chunks[i+1][:100]}...")
        
        contextual_chunks.append({
            'text': chunk,
            'context': "\n".join(context_parts),
            'chunk_index': i
        })
    
    return contextual_chunks

# Demonstrate contextual chunking
sample_text = docs[0]['text']
contextual_chunks = contextual_chunking(sample_text, chunk_size=300)

print(f"Created {len(contextual_chunks)} contextual chunks\n")
for i, chunk in enumerate(contextual_chunks[:2]):
    print(f"--- Chunk {i+1} ---")
    print(f"Main text: {chunk['text'][:100]}...")
    print(f"Context preview: {chunk['context'][:150]}...")
    print()
```

**Cell 12 (Markdown):**
```markdown
## 5. Complete Hybrid RAG Pipeline

Now let's build a complete RAG system that combines:
- Semantic search (Gemini embeddings)
- BM25 search
- Hybrid fusion
- Advanced chunking
```

**Cell 13 (Code):**
```python
class HybridRAG:
    """
    Complete Hybrid RAG system combining semantic and BM25 search.
    """
    
    def __init__(self):
        self.chroma_client = chromadb.Client()
        self.collection = None
        self.corpus = []
        
    def index_documents(self, documents, chunk_method="recursive", chunk_size=300):
        """Index documents with both semantic embeddings and BM25."""
        print("Indexing documents...")
        
        # Chunk documents
        all_chunks = []
        for doc in documents:
            chunks = chunk_text(doc['text'], method=chunk_method, chunk_size=chunk_size)
            all_chunks.extend(chunks)
        
        self.corpus = all_chunks
        
        # Create ChromaDB collection
        self.collection = self.chroma_client.create_collection(name="hybrid_rag")
        
        # Generate embeddings
        print("Generating embeddings...")
        embeddings = []
        for chunk in all_chunks:
            result = genai.embed_content(
                model="models/text-embedding-004",
                content=chunk,
                task_type="retrieval_document"
            )
            embeddings.append(result['embedding'])
        
        # Add to ChromaDB
        self.collection.add(
            documents=all_chunks,
            embeddings=embeddings,
            ids=[f"chunk_{i}" for i in range(len(all_chunks))]
        )
        
        print(f"Indexed {len(all_chunks)} chunks")
    
    def search(self, query, top_k=3, fusion_method="rrf"):
        """Hybrid search combining semantic and BM25."""
        # Semantic search
        query_embedding = genai.embed_content(
            model="models/text-embedding-004",
            content=query,
            task_type="retrieval_query"
        )['embedding']
        
        semantic_results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        semantic_list = []
        for doc, dist in zip(semantic_results['documents'][0], semantic_results['distances'][0]):
            semantic_list.append({'text': doc, 'score': 1 - dist})
        
        # BM25 search
        bm25_results = bm25_search(self.corpus, query, top_k=top_k)
        
        # Fusion
        if fusion_method == "rrf":
            fused = reciprocal_rank_fusion(semantic_list, bm25_results)
        else:
            fused = weighted_fusion(semantic_list, bm25_results)
        
        return fused[:top_k]
    
    def generate_answer(self, query, search_results):
        """Generate answer using retrieved context."""
        context = "\n\n".join([r['text'] for r in search_results])
        
        prompt = f"""Answer the question based on the provided context.
        
Context:
{context}

Question: {query}

Answer:"""
        
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(prompt)
        
        return response.text


# Test the hybrid RAG system
hybrid_rag = HybridRAG()
hybrid_rag.index_documents(docs)

# Test queries
test_queries = [
    "What is PyTorch autograd?",
    "How do neural networks work?",
    "What are the types of machine learning?"
]

for query in test_queries:
    print(f"\n{'='*60}")
    print(f"Query: {query}")
    
    results = hybrid_rag.search(query, top_k=3)
    answer = hybrid_rag.generate_answer(query, results)
    
    print(f"\nAnswer: {answer[:200]}...")
    print(f"\nRetrieved chunks:")
    for i, result in enumerate(results):
        print(f"  {i+1}. {result['text'][:80]}...")
```

**Cell 14 (Markdown):**
```markdown
## 6. Retrieval Evaluation

Let's measure how well our retrieval system performs.
```

**Cell 15 (Code):**
```python
def precision_at_k(retrieved, relevant, k):
    """Calculate precision@k."""
    retrieved_at_k = retrieved[:k]
    relevant_retrieved = len(set(retrieved_at_k) & set(relevant))
    return relevant_retrieved / k


def recall_at_k(retrieved, relevant, k):
    """Calculate recall@k."""
    retrieved_at_k = retrieved[:k]
    relevant_retrieved = len(set(retrieved_at_k) & set(relevant))
    return relevant_retrieved / len(relevant) if relevant else 0


# Create a simple evaluation dataset
evaluation_data = [
    {
        "query": "What is machine learning?",
        "relevant_keywords": ["machine learning", "AI", "artificial intelligence", "learning"]
    },
    {
        "query": "How do neural networks work?",
        "relevant_keywords": ["neural networks", "layers", "neurons", "deep learning"]
    }
]

print("=== Retrieval Evaluation ===\n")

for eval_item in evaluation_data:
    query = eval_item["query"]
    relevant_keywords = eval_item["relevant_keywords"]
    
    # Get retrieval results
    results = hybrid_rag.search(query, top_k=5)
    retrieved_texts = [r['text'].lower() for r in results]
    
    # Check if relevant keywords appear
    relevant_chunks = []
    for i, text in enumerate(retrieved_texts):
        if any(keyword in text for keyword in relevant_keywords):
            relevant_chunks.append(i)
    
    # Calculate metrics
    retrieved_indices = list(range(len(results)))
    p@3 = precision_at_k(retrieved_indices, relevant_chunks, 3)
    r@3 = recall_at_k(retrieved_indices, relevant_chunks, 3)
    
    print(f"Query: {query}")
    print(f"  Precision@3: {p@3:.3f}")
    print(f"  Recall@3: {r@3:.3f}")
    print()
```

**Cell 16 (Markdown):**
```markdown
## Summary

In this notebook, we learned:

1. **BM25 Search**: Keyword-based retrieval for exact matches
2. **Hybrid Search**: Combining semantic and BM25 with RRF/weighted fusion
3. **Advanced Chunking**: Contextual chunking with surrounding text
4. **Hybrid RAG Pipeline**: Complete system with both search methods
5. **Evaluation**: Measuring retrieval quality with precision/recall

## Key Takeaways
- Hybrid search often outperforms pure semantic search
- BM25 catches exact matches that embeddings might miss
- RRF is a robust fusion method
- Chunking strategy significantly impacts retrieval quality

## Next Steps
- Move to Session 3 for production monitoring with MLflow!
```

- [ ] **Step 2: Verify notebook runs without errors**

- [ ] **Step 3: Commit Session 2 notebook**

```bash
git add rag_advanced_retrieval.ipynb
git commit -m "feat: add Session 2 - Advanced Retrieval with hybrid search"
```

---

## Task 6: Session 3 Notebook - Production Observability

**Files:**
- Create: `current/classwork/rag/rag_production_observability.ipynb`

**Interfaces:**
- Consumes: All previous utilities, MLflow
- Produces: Production monitoring demonstration

- [ ] **Step 1: Create notebook structure**

**Cell 1 (Markdown):**
```markdown
# Production RAG: Observability with MLflow

## Learning Objectives
- Set up MLflow for experiment tracking
- Monitor RAG system performance
- Create custom visualizations
- Implement automated quality checks
- Build production-ready RAG with monitoring

## Prerequisites
- Completed Sessions 1 & 2
- MLflow installed and configured
```

**Cell 2 (Code):**
```python
import os
import mlflow
import mlflow.sklearn
import google.generativeai as genai
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

print("Session 3: Production RAG with MLflow Observability")
```

**Cell 3 (Markdown):**
```markdown
## 1. MLflow Setup

MLflow tracks experiments, logs metrics, and manages models.

### Why MLflow for RAG?
- Track different chunking strategies
- Compare retrieval methods
- Log generation quality scores
- Version your RAG pipelines
```

**Cell 4 (Code):**
```python
# Set up MLflow tracking
mlflow.set_tracking_uri("file:///tmp/mlflow")  # Local file store for demo
mlflow.set_experiment("rag_production_demo")

print(f"MLflow tracking URI: {mlflow.get_tracking_uri()}")
print("MLflow experiment created!")
```

**Cell 5 (Code):**
```python
class MonitoredRAG:
    """
    RAG system with MLflow monitoring.
    """
    
    def __init__(self):
        self.query_log = []
        self.retrieval_metrics = []
        self generation_metrics = []
        
    def log_query(self, query, results, answer, latency_metrics):
        """Log a query and its results."""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'query': query,
            'num_results': len(results),
            'answer_length': len(answer),
            'retrieval_latency': latency_metrics.get('retrieval_latency', 0),
            'generation_latency': latency_metrics.get('generation_latency', 0),
            'total_latency': latency_metrics.get('total_latency', 0),
            'avg_retrieval_score': sum(r.get('score', 0) for r in results) / len(results) if results else 0
        }
        self.query_log.append(log_entry)
        return log_entry
    
    def get_statistics(self):
        """Get aggregate statistics."""
        if not self.query_log:
            return {}
        
        df = pd.DataFrame(self.query_log)
        return {
            'total_queries': len(df),
            'avg_retrieval_latency': df['retrieval_latency'].mean(),
            'avg_generation_latency': df['generation_latency'].mean(),
            'avg_total_latency': df['total_latency'].mean(),
            'avg_retrieval_score': df['avg_retrieval_score'].mean()
        }


# Create monitored RAG instance
monitored_rag = MonitoredRAG()
print("Monitored RAG system initialized!")
```

**Cell 6 (Markdown):**
```markdown
## 2. Experiment Tracking

Let's run experiments with different configurations and track them in MLflow.
```

**Cell 7 (Code):**
```python
def run_rag_experiment(
    experiment_name,
    chunk_method,
    chunk_size,
    search_method,
    test_queries
):
    """
    Run a complete RAG experiment with MLflow tracking.
    """
    with mlflow.start_run(run_name=experiment_name):
        # Log parameters
        mlflow.log_param("chunk_method", chunk_method)
        mlflow.log_param("chunk_size", chunk_size)
        mlflow.log_param("search_method", search_method)
        mlflow.log_param("num_test_queries", len(test_queries))
        
        # Initialize metrics
        retrieval_latencies = []
        generation_latencies = []
        retrieval_scores = []
        
        # Run queries
        for query in test_queries:
            start_time = datetime.now()
            
            # Simulate retrieval (in real scenario, use actual RAG)
            # This is a simplified example
            retrieval_time = 0.1  # Simulated
            
            # Simulate generation
            generation_time = 0.5  # Simulated
            
            total_time = retrieval_time + generation_time
            
            # Log metrics for each query
            mlflow.log_metric("retrieval_latency", retrieval_time)
            mlflow.log_metric("generation_latency", generation_time)
            mlflow.log_metric("total_latency", total_time)
            mlflow.log_metric("retrieval_score", 0.85)  # Simulated
            
            retrieval_latencies.append(retrieval_time)
            generation_latencies.append(generation_time)
            retrieval_scores.append(0.85)
        
        # Log summary metrics
        mlflow.log_metric("avg_retrieval_latency", sum(retrieval_latencies) / len(retrieval_latencies))
        mlflow.log_metric("avg_generation_latency", sum(generation_latencies) / len(generation_latencies))
        mlflow.log_metric("avg_retrieval_score", sum(retrieval_scores) / len(retrieval_scores))
        
        # Log tags
        mlflow.set_tag("session", "production_observability")
        mlflow.set_tag("model", "gemini-1.5-pro")
        
        print(f"Experiment '{experiment_name}' completed!")
        print(f"  Average retrieval latency: {sum(retrieval_latencies) / len(retrieval_latencies):.3f}s")
        print(f"  Average generation latency: {sum(generation_latencies) / len(generation_latencies):.3f}s")
        print(f"  Average retrieval score: {sum(retrieval_scores) / len(retrieval_scores):.3f}")


# Run multiple experiments
test_queries = [
    "What is machine learning?",
    "How do neural networks work?",
    "Explain deep learning",
    "What is NLP?",
    "How does transformers work?"
]

print("Running experiments with different configurations...\n")

# Experiment 1: Small chunks
run_rag_experiment(
    experiment_name="small_chunks_recursive",
    chunk_method="recursive",
    chunk_size=200,
    search_method="semantic",
    test_queries=test_queries
)

# Experiment 2: Large chunks
run_rag_experiment(
    experiment_name="large_chunks_recursive",
    chunk_method="recursive",
    chunk_size=500,
    search_method="semantic",
    test_queries=test_queries
)

# Experiment 3: Hybrid search
run_rag_experiment(
    experiment_name="hybrid_search_rrf",
    chunk_method="recursive",
    chunk_size=300,
    search_method="hybrid_rrf",
    test_queries=test_queries
)
```

**Cell 8 (Markdown):**
```markdown
## 3. Custom Visualizations

Let's create visualizations to understand our RAG system's performance.
```

**Cell 9 (Code):**
```python
def create_performance_dashboard():
    """Create a performance visualization dashboard."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Simulated data for demonstration
    experiments = ['Small Chunks', 'Large Chunks', 'Hybrid Search']
    retrieval_latencies = [0.08, 0.12, 0.15]
    generation_latencies = [0.45, 0.42, 0.48]
    retrieval_scores = [0.82, 0.78, 0.89]
    chunk_counts = [150, 75, 100]
    
    # Plot 1: Latency comparison
    x = range(len(experiments))
    width = 0.35
    
    axes[0, 0].bar(x, retrieval_latencies, width, label='Retrieval', color='blue')
    axes[0, 0].bar([i + width for i in x], generation_latencies, width, label='Generation', color='orange')
    axes[0, 0].set_xlabel('Experiment')
    axes[0, 0].set_ylabel('Latency (seconds)')
    axes[0, 0].set_title('Latency by Component')
    axes[0, 0].set_xticks([i + width/2 for i in x])
    axes[0, 0].set_xticklabels(experiments)
    axes[0, 0].legend()
    
    # Plot 2: Retrieval scores
    axes[0, 1].bar(experiments, retrieval_scores, color=['green', 'red', 'purple'])
    axes[0, 1].set_xlabel('Experiment')
    axes[0, 1].set_ylabel('Retrieval Score')
    axes[0, 1].set_title('Retrieval Quality Comparison')
    axes[0, 1].set_ylim(0, 1)
    
    # Plot 3: Chunk count vs performance
    axes[1, 0].scatter(chunk_counts, retrieval_scores, s=100, c=['blue', 'red', 'green'])
    axes[1, 0].set_xlabel('Number of Chunks')
    axes[1, 0].set_ylabel('Retrieval Score')
    axes[1, 0].set_title('Chunk Count vs Retrieval Quality')
    for i, txt in enumerate(experiments):
        axes[1, 0].annotate(txt, (chunk_counts[i], retrieval_scores[i]), 
                           xytext=(5, 5), textcoords='offset points')
    
    # Plot 4: Total latency breakdown
    total_latencies = [r + g for r, g in zip(retrieval_latencies, generation_latencies)]
    axes[1, 1].pie(total_latencies, labels=experiments, autopct='%1.1f%%',
                   colors=['lightblue', 'lightcoral', 'lightgreen'])
    axes[1, 1].set_title('Total Latency Distribution')
    
    plt.tight_layout()
    plt.show()
    
    print("Dashboard created!")


create_performance_dashboard()
```

**Cell 10 (Code):**
```python
def create_retrieval_analysis_viz():
    """Visualize retrieval analysis."""
    # Simulated retrieval data
    queries = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
    semantic_scores = [0.85, 0.72, 0.91, 0.68, 0.79]
    bm25_scores = [0.78, 0.88, 0.75, 0.82, 0.71]
    hybrid_scores = [0.89, 0.85, 0.93, 0.81, 0.87]
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Plot 1: Score comparison across queries
    x = range(len(queries))
    width = 0.25
    
    axes[0].bar(x, semantic_scores, width, label='Semantic', color='blue')
    axes[0].bar([i + width for i in x], bm25_scores, width, label='BM25', color='orange')
    axes[0].bar([i + 2*width for i in x], hybrid_scores, width, label='Hybrid', color='green')
    
    axes[0].set_xlabel('Query')
    axes[0].set_ylabel('Retrieval Score')
    axes[0].set_title('Retrieval Scores by Method')
    axes[0].set_xticks([i + width for i in x])
    axes[0].set_xticklabels(queries)
    axes[0].legend()
    axes[0].set_ylim(0, 1)
    
    # Plot 2: Method improvement
    improvements = [(h - s) / s * 100 for h, s in zip(hybrid_scores, semantic_scores)]
    axes[1].bar(queries, improvements, color='green')
    axes[1].set_xlabel('Query')
    axes[1].set_ylabel('Improvement (%)')
    axes[1].set_title('Hybrid vs Semantic Search Improvement')
    axes[1].axhline(y=0, color='r', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.show()


create_retrieval_analysis_viz()
```

**Cell 11 (Markdown):**
```markdown
## 4. Automated Quality Checks

Implement automated checks to monitor RAG quality in production.
```

**Cell 12 (Code):**
```python
class RAGQualityMonitor:
    """
    Automated quality monitoring for RAG systems.
    """
    
    def __init__(self, thresholds=None):
        self.thresholds = thresholds or {
            'min_retrieval_score': 0.6,
            'max_latency': 2.0,
            'min_answer_length': 50
        }
        self.alerts = []
        
    def check_quality(self, query, results, answer, latency):
        """Run quality checks and return alerts."""
        checks_passed = True
        check_results = []
        
        # Check 1: Retrieval quality
        avg_score = sum(r.get('score', 0) for r in results) / len(results) if results else 0
        if avg_score < self.thresholds['min_retrieval_score']:
            self.alerts.append({
                'type': 'LOW_RETRIEVAL_SCORE',
                'severity': 'WARNING',
                'message': f'Low retrieval score: {avg_score:.3f}',
                'query': query
            })
            checks_passed = False
        check_results.append(('Retrieval Score', avg_score, avg_score >= self.thresholds['min_retrieval_score']))
        
        # Check 2: Latency
        if latency > self.thresholds['max_latency']:
            self.alerts.append({
                'type': 'HIGH_LATENCY',
                'severity': 'WARNING',
                'message': f'High latency: {latency:.3f}s',
                'query': query
            })
            checks_passed = False
        check_results.append(('Latency', latency, latency <= self.thresholds['max_latency']))
        
        # Check 3: Answer quality
        answer_length = len(answer) if answer else 0
        if answer_length < self.thresholds['min_answer_length']:
            self.alerts.append({
                'type': 'SHORT_ANSWER',
                'severity': 'INFO',
                'message': f'Short answer: {answer_length} chars',
                'query': query
            })
        check_results.append(('Answer Length', answer_length, answer_length >= self.thresholds['min_answer_length']))
        
        return {
            'checks_passed': checks_passed,
            'check_results': check_results,
            'alerts': self.alerts.copy()
        }
    
    def get_alert_summary(self):
        """Get summary of all alerts."""
        alert_counts = {}
        for alert in self.alerts:
            alert_type = alert['type']
            alert_counts[alert_type] = alert_counts.get(alert_type, 0) + 1
        return alert_counts


# Test quality monitoring
monitor = RAGQualityMonitor()

# Simulate queries with quality issues
test_scenarios = [
    {
        'query': 'What is ML?',
        'results': [{'score': 0.4}, {'score': 0.3}],  # Low scores
        'answer': 'Short answer',
        'latency': 0.5
    },
    {
        'query': 'Explain deep learning',
        'results': [{'score': 0.9}, {'score': 0.85}],  # Good scores
        'answer': 'Deep learning is a subset of machine learning that uses neural networks with multiple layers...',
        'latency': 2.5  # High latency
    }
]

print("=== Quality Monitoring Test ===\n")

for scenario in test_scenarios:
    result = monitor.check_quality(
        scenario['query'],
        scenario['results'],
        scenario['answer'],
        scenario['latency']
    )
    
    print(f"Query: {scenario['query']}")
    print(f"Checks passed: {result['checks_passed']}")
    print("Check details:")
    for check_name, value, passed in result['check_results']:
        status = "✓" if passed else "✗"
        print(f"  {status} {check_name}: {value}")
    print()

print("\nAlert Summary:")
print(monitor.get_alert_summary())
```

**Cell 13 (Markdown):**
```markdown
## 5. Production-Ready RAG with Full Monitoring

Let's combine everything into a production-ready system.
```

**Cell 14 (Code):**
```python
class ProductionRAG:
    """
    Complete production RAG with monitoring and observability.
    """
    
    def __init__(self):
        self.rag = HybridRAG()
        self.monitor = RAGQualityMonitor()
        self.mlflow_experiment = "production_rag"
        
    def process_query(self, query):
        """Process a query with full monitoring."""
        with mlflow.start_run(run_name=f"query_{hash(query)}"):
            start_time = datetime.now()
            
            # Retrieval
            retrieval_start = datetime.now()
            results = self.rag.search(query, top_k=3)
            retrieval_latency = (datetime.now() - retrieval_start).total_seconds()
            
            # Generation
            generation_start = datetime.now()
            answer = self.rag.generate_answer(query, results)
            generation_latency = (datetime.now() - generation_start).total_seconds()
            
            total_latency = retrieval_latency + generation_latency
            
            # Quality checks
            quality_result = self.monitor.check_quality(
                query, results, answer, total_latency
            )
            
            # Log to MLflow
            mlflow.log_param("query", query[:100])
            mlflow.log_metric("retrieval_latency", retrieval_latency)
            mlflow.log_metric("generation_latency", generation_latency)
            mlflow.log_metric("total_latency", total_latency)
            mlflow.log_metric("avg_retrieval_score", 
                             sum(r.get('score', 0) for r in results) / len(results))
            mlflow.log_metric("quality_checks_passed", 
                             1 if quality_result['checks_passed'] else 0)
            
            return {
                'query': query,
                'answer': answer,
                'results': results,
                'latency': {
                    'retrieval': retrieval_latency,
                    'generation': generation_latency,
                    'total': total_latency
                },
                'quality': quality_result
            }


print("Production RAG system ready!")
print("\nTo use this system:")
print("1. Initialize: prod_rag = ProductionRAG()")
print("2. Query: result = prod_rag.process_query('your question')")
print("3. View MLflow UI: mlflow ui --port 5000")
```

**Cell 15 (Markdown):**
```markdown
## 6. Summary & Best Practices

### What We Covered
1. **MLflow Integration**: Experiment tracking for RAG systems
2. **Custom Visualizations**: Performance dashboards and analysis
3. **Quality Monitoring**: Automated checks and alerting
4. **Production System**: Complete monitored RAG pipeline

### Best Practices for Production RAG

1. **Always log experiments** - Track chunking, retrieval, and generation parameters
2. **Monitor key metrics** - Latency, retrieval quality, answer quality
3. **Set up alerts** - Catch quality degradation early
4. **A/B test configurations** - Use MLflow to compare different approaches
5. **Version everything** - Models, data, configurations

### Next Steps
- Deploy to production with proper MLflow server
- Add more sophisticated quality checks
- Implement feedback loops for continuous improvement
```

- [ ] **Step 2: Verify notebook runs without errors**

- [ ] **Step 3: Commit Session 3 notebook**

```bash
git add rag_production_observability.ipynb
git commit -m "feat: add Session 3 - Production Observability with MLflow"
```

---

## Task 7: Final Integration and Testing

**Files:**
- Modify: `current/classwork/rag/README.md` (update with final instructions)
- Create: `current/classwork/rag/setup.sh`

**Interfaces:**
- Consumes: All previous tasks
- Produces: Complete, runnable teaching materials

- [ ] **Step 1: Create setup.sh script**

```bash
#!/bin/bash
# Setup script for RAG Teaching Materials

echo "Setting up RAG Teaching Materials..."

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Please edit .env file and add your Gemini API key"
fi

# Create data directories
mkdir -p data/sample_pdfs data/sample_texts data/sample_html

echo "Setup complete!"
echo "To get started:"
echo "1. Edit .env and add your GEMINI_API_KEY"
echo "2. Run: jupyter notebook"
echo "3. Open rag_fundamentals.ipynb"
```

- [ ] **Step 2: Make setup.sh executable**

```bash
chmod +x setup.sh
```

- [ ] **Step 3: Update README.md with final instructions**

```markdown
# RAG Teaching Materials

Complete teaching materials for ML bootcamp covering Retrieval-Augmented Generation (RAG) applications using Gemini API.

## 🎯 Learning Objectives

After completing all three sessions, students will be able to:
- Build a complete RAG pipeline from scratch
- Implement hybrid search combining BM25 and semantic search
- Set up MLflow monitoring for production RAG systems
- Evaluate and optimize RAG performance

## 📚 Sessions

### Session 1: RAG Fundamentals
**File:** `rag_fundamentals.ipynb`
- RAG architecture overview
- Document processing & chunking strategies
- Gemini embeddings
- ChromaDB vector database
- Basic RAG pipeline

### Session 2: Advanced Retrieval
**File:** `rag_advanced_retrieval.ipynb`
- BM25 search implementation
- Hybrid search with fusion techniques
- Advanced chunking strategies
- Retrieval evaluation

### Session 3: Production Observability
**File:** `rag_production_observability.ipynb`
- MLflow experiment tracking
- Custom visualization dashboards
- Automated quality monitoring
- Production-ready RAG system

## 🛠️ Setup

### Quick Start
```bash
# Clone or navigate to this directory
cd current/classwork/rag

# Run setup script
./setup.sh

# Edit .env file with your Gemini API key
nano .env

# Start Jupyter
jupyter notebook
```

### Manual Setup
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your API key

# Run notebooks
jupyter notebook
```

## 📁 Project Structure

```
rag/
├── README.md                    # This file
├── requirements.txt            # Python dependencies
├── .env.example               # Environment template
├── setup.sh                   # Setup script
├── rag_fundamentals.ipynb     # Session 1
├── rag_advanced_retrieval.ipynb # Session 2
├── rag_production_observability.ipynb # Session 3
├── data/
│   ├── sample_texts/          # Sample text documents
│   ├── sample_pdfs/          # Sample PDF documents
│   └── sample_html/          # Sample HTML documents
├── utils/
│   ├── __init__.py
│   ├── chunking.py           # Chunking utilities
│   └── retrieval.py          # Retrieval utilities
└── tests/
    ├── test_chunking.py
    └── test_retrieval.py
```

## 🔧 Prerequisites

- Python 3.11+
- Gemini API key (get from Google AI Studio)
- Basic understanding of ML/NLP concepts
- Jupyter notebook

## 📊 Key Technologies

- **Gemini API**: Embeddings and text generation
- **ChromaDB**: Vector database for similarity search
- **BM25**: Keyword-based retrieval
- **MLflow**: Experiment tracking and monitoring
- **Matplotlib/Plotly**: Visualizations

## 🚀 Features

### Chunking Strategies
- Fixed-size chunking with overlap
- Recursive character splitting
- Semantic chunking
- Contextual chunking with summaries

### Search Methods
- Semantic search (vector embeddings)
- BM25 search (keyword matching)
- Hybrid search with fusion (RRF, weighted)

### Observability
- MLflow experiment tracking
- Custom performance dashboards
- Automated quality checks
- Latency monitoring

## 📈 Evaluation Metrics

- Precision@k
- Recall@k
- Retrieval latency
- Generation latency
- Answer quality scores

## 🎓 Teaching Notes

### For Instructors
1. **Session 1** (2-3 hours): Focus on building intuition for RAG
2. **Session 2** (2-3 hours): Emphasize when to use hybrid vs pure semantic
3. **Session 3** (2-3 hours): Stress importance of monitoring in production

### Common Student Questions
- "When should I use BM25 vs semantic search?" → When exact keywords matter
- "How do I choose chunk size?" → Start with 300-500, test with your data
- "Why do we need MLflow?" → Track experiments, compare approaches, debug issues

## 🔍 Troubleshooting

### Common Issues

**API Key Error:**
```
Error: Invalid API key
```
Solution: Check your .env file has correct GEMINI_API_KEY

**Import Error:**
```
ModuleNotFoundError: No module named 'utils'
```
Solution: Make sure you're in the rag/ directory

**MLflow Error:**
```
MLflow exception: Unable to create experiment
```
Solution: Check write permissions in /tmp/mlflow

## 📝 License

Educational use only - ML Bootcamp Course

## 👥 Contributing

For improvements or issues, contact the instructor.
```

- [ ] **Step 4: Commit final integration**

```bash
git add README.md setup.sh
git commit -m "feat: complete RAG teaching materials with setup and documentation"
```

---

## Self-Review Checklist

✅ **Spec Coverage:**
- Session 1: RAG Fundamentals ✓
- Session 2: Advanced Retrieval with BM25 ✓
- Session 3: Production Observability with MLflow ✓
- Gemini API integration ✓
- ChromaDB vector database ✓
- Multi-format document processing ✓

✅ **Placeholder Scan:** No TBD/TODO items found

✅ **Type Consistency:** All function signatures match across tasks

✅ **File Structure:** Clear organization with utils, tests, and notebooks

✅ **Testing:** Each utility module has comprehensive tests

✅ **Documentation:** Complete README and setup instructions

---

## Execution Handoff

**Plan complete and saved to:** `current/classwork/rag/docs/plans/2025-01-24-rag-teaching-materials.md`

Two execution options:

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

Which approach would you prefer?
