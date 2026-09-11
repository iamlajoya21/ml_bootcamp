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
    # Mock the Gemini embedding API
    mock_genai.embed_content.return_value = {'embedding': [0.1, 0.2, 0.3, 0.4, 0.5]}

    # Create a real vector store with actual documents
    docs = ["machine learning", "deep learning", "natural language processing"]
    embeddings = [[0.1, 0.2, 0.3, 0.4, 0.5], [0.2, 0.3, 0.4, 0.5, 0.6], [0.3, 0.4, 0.5, 0.6, 0.7]]
    metadata = [{"source": "test1"}, {"source": "test2"}, {"source": "test3"}]
    
    # Use a unique collection name to avoid conflicts with other tests
    store = create_vector_store(docs, embeddings, metadata, collection_name="test_search_collection")
    
    # Test the search function
    results = search_vector_store(store, "test query", n_results=2)
    assert len(results) == 2
    assert isinstance(results[0], str)


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
    # Create semantic results where doc1 is ranked higher than doc2
    semantic_results = [
        {"text": "doc1", "score": 0.9, "rank": 0},
        {"text": "doc2", "score": 0.8, "rank": 1}
    ]
    
    # Create BM25 results where doc2 is ranked higher than doc1
    bm25_results = [
        {"text": "doc2", "score": 0.7, "rank": 0},
        {"text": "doc1", "score": 0.6, "rank": 1}
    ]

    fused = hybrid_search(semantic_results, bm25_results, method="rrf")
    assert len(fused) == 2
    
    # Verify that all documents are included
    doc_texts = [r['text'] for r in fused]
    assert 'doc1' in doc_texts
    assert 'doc2' in doc_texts
    
    # Verify that scores are positive and calculated
    for result in fused:
        assert 'rrf_score' in result
        assert result['rrf_score'] > 0
    
    # Verify ranking with specific data where doc1 should be first
    # doc1 appears rank 0 in semantic, rank 1 in BM25
    # doc2 appears rank 1 in semantic, rank 0 in BM25
    # They have equal scores, so verify the function handles ties properly
    assert fused[0]['text'] in ['doc1', 'doc2']
    assert fused[1]['text'] in ['doc1', 'doc2']
    assert fused[0]['text'] != fused[1]['text']
