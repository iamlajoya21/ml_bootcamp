import google.generativeai as genai
import chromadb
from typing import List, Dict, Any, Optional
import numpy as np
from rank_bm25 import BM25Okapi


def create_vector_store(
    documents: List[str],
    embeddings: List[List[float]],
    metadatas: Optional[List[Dict[str, Any]]] = None,
    collection_name: str = "rag_collection",
    client: Optional[chromadb.Client] = None
) -> chromadb.Collection:
    """Create or update a ChromaDB vector store collection."""
    if client is None:
        client = chromadb.Client()

    # Use get_or_create_collection to prevent runtime errors on existing collections
    collection = client.get_or_create_collection(name=collection_name)

    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=[f"doc_{i}" for i in range(len(documents))],
        metadatas=metadatas
    )

    return collection


def search_vector_store(
    collection: chromadb.Collection,
    query: str,
    n_results: int = 5,
    embedding_model: str = "models/gemini-embedding-001"
) -> List[Dict[str, Any]]:
    """Search the vector store using semantic similarity, returning standardized result dicts."""
    response = genai.embed_content(
        model=embedding_model,
        content=query
    )
    query_embedding = response['embedding']

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents", "distances", "metadatas"]
    )

    docs = results.get('documents', [[]])[0]
    distances = results.get('distances', [[]])[0]
    metadatas = results.get('metadatas', [[]])[0] or [{}] * len(docs)
    ids = results.get('ids', [[]])[0]

    formatted_results = []
    for rank, (doc_id, doc, dist, meta) in enumerate(zip(ids, docs, distances, metadatas)):
        formatted_results.append({
            "id": doc_id,
            "text": doc,
            "score": float(1.0 / (1.0 + dist)),  # Inverse distance score
            "rank": rank + 1,
            "metadata": meta
        })

    return formatted_results


def bm25_search(
    corpus: List[str],
    query: str,
    top_k: int = 5,
    metadatas: Optional[List[Dict[str, Any]]] = None
) -> List[Dict[str, Any]]:
    """Perform BM25 search on a corpus and return structured dictionary outputs."""
    tokenized_corpus = [doc.lower().split() for doc in corpus]
    tokenized_query = query.lower().split()

    bm25 = BM25Okapi(tokenized_corpus)
    scores = bm25.get_scores(tokenized_query)

    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []
    for rank, idx in enumerate(top_indices):
        results.append({
            "id": f"doc_{idx}",
            "text": corpus[idx],
            "score": float(scores[idx]),
            "rank": rank + 1,
            "metadata": metadatas[idx] if metadatas else {}
        })

    return results


def hybrid_search(
    semantic_results: List[Dict[str, Any]],
    bm25_results: List[Dict[str, Any]],
    method: str = "rrf",
    k: int = 60,
    weight1: float = 0.7,
    weight2: float = 0.3
) -> List[Dict[str, Any]]:
    """Combine semantic and BM25 search results using RRF or weighted score fusion."""
    if method == "rrf":
        return reciprocal_rank_fusion(semantic_results, bm25_results, k=k)
    elif method == "weighted":
        return weighted_fusion(semantic_results, bm25_results, weight1=weight1, weight2=weight2)
    else:
        raise ValueError(f"Unknown fusion method: {method}")


def reciprocal_rank_fusion(
    results_list1: List[Dict[str, Any]],
    results_list2: List[Dict[str, Any]],
    k: int = 60
) -> List[Dict[str, Any]]:
    """Reciprocal Rank Fusion (RRF) algorithm preserving document payloads."""
    all_docs: Dict[str, Dict[str, Any]] = {}

    for rank, result in enumerate(results_list1):
        doc_text = result['text']
        if doc_text not in all_docs:
            all_docs[doc_text] = {
                'text': doc_text,
                'metadata': result.get('metadata', {}),
                'rrf_score': 0.0
            }
        all_docs[doc_text]['rrf_score'] += 1.0 / (k + rank + 1)

    for rank, result in enumerate(results_list2):
        doc_text = result['text']
        if doc_text not in all_docs:
            all_docs[doc_text] = {
                'text': doc_text,
                'metadata': result.get('metadata', {}),
                'rrf_score': 0.0
            }
        all_docs[doc_text]['rrf_score'] += 1.0 / (k + rank + 1)

    return sorted(all_docs.values(), key=lambda x: x['rrf_score'], reverse=True)


def weighted_fusion(
    results_list1: List[Dict[str, Any]],
    results_list2: List[Dict[str, Any]],
    weight1: float = 0.7,
    weight2: float = 0.3
) -> List[Dict[str, Any]]:
    """Weighted score normalization and fusion preserving metadata."""
    all_docs: Dict[str, Dict[str, Any]] = {}

    max_score1 = max((r['score'] for r in results_list1), default=1.0) or 1.0
    for result in results_list1:
        doc_text = result['text']
        normalized_score = result['score'] / max_score1
        if doc_text not in all_docs:
            all_docs[doc_text] = {
                'text': doc_text,
                'metadata': result.get('metadata', {}),
                'weighted_score': 0.0
            }
        all_docs[doc_text]['weighted_score'] += weight1 * normalized_score

    max_score2 = max((r['score'] for r in results_list2), default=1.0) or 1.0
    for result in results_list2:
        doc_text = result['text']
        normalized_score = result['score'] / max_score2
        if doc_text not in all_docs:
            all_docs[doc_text] = {
                'text': doc_text,
                'metadata': result.get('metadata', {}),
                'weighted_score': 0.0
            }
        all_docs[doc_text]['weighted_score'] += weight2 * normalized_score

    return sorted(all_docs.values(), key=lambda x: x['weighted_score'], reverse=True)
