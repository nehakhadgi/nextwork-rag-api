
# Containerized RAG API with Docker

A production-ready Retrieval-Augmented Generation (RAG) API built with FastAPI and containerized using Docker. This system queries a local vector store (Chroma DB) to supply context to Ollama's local LLM (TinyLlama) for private, zero-cloud dependency question-answering.

## Features
- **Local LLM Execution:** Powered by Ollama (TinyLlama model).
- **FastAPI Backend:** Fully typed REST endpoints for low-latency querying.
- **Vector Database:** Context storage and semantic retrieval using Chroma DB.
- **Dockerized Architecture:** Seamlessly containerized for isolated, reproducible deployments across different environments.

## Local Setup & Quickstart

1. Clone the repository:
   ```bash
   git clone 
   cd nextwork-rag-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate # On macOS/Linux
   ```

3. Install requirements:
   ```bash
   pip install fastapi uvicorn chromadb ollama
   ```

4. Populate the vector database:
   ```bash
   python embed.py
   ```

5. Build and run the container:
   ```bash
   docker build -t rag-app .
   docker run -p 8000:8000 rag-app
   ```
