## Design: Session 2 Notebook - Advanced Retrieval

### Overview
Create a Jupyter notebook teaching advanced retrieval techniques for RAG applications, focusing on hybrid search with BM25.

### Requirements
- Create `rag_advanced_retrieval.ipynb` with 16 cells (8 markdown, 8 code)
- Follow exact cell contents from task brief
- Use existing utilities: `utils/chunking.py`, `utils/retrieval.py`
- Ensure compatibility with existing codebase patterns

### Architecture
The notebook will follow the same structure as Session 1 (`rag_fundamentals.ipynb`) with consistent metadata and cell organization.

### Components
1. **Setup Cell**: Import libraries, configure Gemini API
2. **Limitations Demo**: Show pure semantic search limitations
3. **BM25 Implementation**: Implement BM25 search using rank_bm25
4. **Hybrid Search**: Implement fusion strategies (RRF, weighted)
5. **Advanced Chunking**: Contextual chunking with surrounding context
6. **Complete Pipeline**: HybridRAG class combining all components
7. **Evaluation**: Retrieval metrics (precision@k, recall@k)

### Compatibility Considerations
- Use existing `chunk_text` function from `utils/chunking.py`
- Maintain consistent import patterns with Session 1
- Follow notebook metadata conventions from existing notebook
- Adjust code if needed to work with existing utilities while preserving educational content

### Success Criteria
- Notebook runs without errors
- All cells execute correctly with existing utilities
- Educational content remains intact
- Follows exact specification from brief