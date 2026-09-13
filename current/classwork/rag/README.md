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
