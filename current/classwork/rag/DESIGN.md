# RAG Teaching Materials Design

## Overview
Teaching materials for ML bootcamp covering Retrieval-Augmented Generation (RAG) applications using Gemini API. Designed for intermediate students with prior NLP/transformer knowledge.

## Target Audience
- Intermediate ML practitioners
- Familiar with BERT, transformers, and basic NLP concepts
- Ready to learn production-grade RAG systems

## Technical Stack
- **Embeddings & Generation:** Gemini API (text-embedding-004, gemini-1.5-pro)
- **Vector Database:** ChromaDB
- **BM25 Search:** rank_bm25 library
- **Observability:** MLflow + custom visualizations
- **Data Formats:** PDF, TXT, HTML documents

## Structure: 3 Sessions

### Session 1: `rag_fundamentals.ipynb` (2-3 hours)
**Objective:** Build a basic RAG pipeline from scratch

**Topics:**
1. RAG architecture overview
2. Document processing & chunking strategies
   - Fixed-size chunking with overlap
   - Recursive character splitting
   - Semantic chunking
3. Gemini embeddings
4. ChromaDB setup and similarity search
5. Basic RAG pipeline (query → embed → retrieve → generate)

**Deliverable:** Working RAG system with simple chunking

---

### Session 2: `rag_advanced_retrieval.ipynb` (2-3 hours)
**Objective:** Enhance retrieval with hybrid search and advanced techniques

**Topics:**
1. BM25 search implementation
2. Hybrid search architecture
   - Reciprocal Rank Fusion (RRF)
   - Score-based fusion
3. Advanced chunking strategies
   - Contextual chunking with summaries
   - Parent-child relationships
4. Reranking with cross-encoders
5. Retrieval evaluation metrics

**Deliverable:** Hybrid search system combining BM25 + semantic search

---

### Session 3: `rag_production_observability.ipynb` (2-3 hours)
**Objective:** Add production monitoring and observability

**Topics:**
1. MLflow integration for experiment tracking
2. Custom visualization dashboards
   - Retrieval quality metrics
   - Performance monitoring
   - Error analysis
3. Automated quality checks
4. A/B testing framework
5. End-to-end production demo

**Deliverable:** Production-ready RAG with MLflow monitoring

---

## Directory Structure
```
current/classwork/rag/
├── DESIGN.md
├── rag_fundamentals.ipynb
├── rag_advanced_retrieval.ipynb
├── rag_production_observability.ipynb
├── data/
│   ├── sample_pdfs/
│   ├── sample_texts/
│   └── sample_html/
├── utils/
│   ├── chunking.py
│   ├── retrieval.py
│   └── visualization.py
└── requirements.txt
```

## Key Design Decisions
1. **Progressive complexity** - Each session builds on previous knowledge
2. **Self-contained notebooks** - Can be run independently
3. **Real-world data** - Multi-format documents for practical experience
4. **Production focus** - Emphasis on monitoring and observability
5. **Gemini-native** - All examples use Gemini API for consistency

## Success Criteria
- Students can build a complete RAG pipeline
- Students understand trade-offs between chunking strategies
- Students can implement hybrid search with BM25 + semantic
- Students can set up MLflow monitoring for RAG systems
- Students can evaluate and optimize RAG performance