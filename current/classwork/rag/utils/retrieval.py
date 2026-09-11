# utils/retrieval.py
import google.generativeai as genai
import chromadb
from typing import List, Dict, Any
import numpy as np
from rank_bm25 import BM25Okapi


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
    # Generate query embedding using Gemini API
    response = genai.embed_content(
        model="models/text-embedding-004",
        content=query
    )
    query_embedding = response['embedding']

    # Query the collection with the generated embedding
    results = collection.query(
        query_embeddings=[query_embedding],
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
        return reciprocal_rank_fusion(semantic_results, bm25_results, k)
    elif method == "weighted":
        return weighted_fusion(semantic_results, bm25_results)
    else:
        raise ValueError(f"Unknown fusion method: {method}")


def reciprocal_rank_fusion(
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


def weighted_fusion(
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
