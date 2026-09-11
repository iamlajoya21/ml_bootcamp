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
