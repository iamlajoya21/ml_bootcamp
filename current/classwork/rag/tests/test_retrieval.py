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
