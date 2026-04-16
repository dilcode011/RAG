# 08 - Vector Stores in RAG

## What is a Vector Store?

A **Vector Store** (also called Vector Database) is a specialized database designed to efficiently store, index, and search high-dimensional **vector embeddings**.

In RAG systems, vector stores are the **core retrieval engine**. They allow fast similarity search between the user query embedding and all stored document embeddings.

## Why Vector Stores Matter in RAG

- Enable **fast semantic search** (instead of keyword search)
- Support **similarity metrics** like cosine similarity
- Handle **millions to billions** of vectors efficiently
- Provide **metadata filtering**
- Support **hybrid search** (vector + keyword)
- Allow **real-time updates** and deletions

## Core Concepts

- **Embedding Vector**: Dense numerical representation of text (e.g., 1536 dimensions)
- **Similarity Search**: Finding the most similar vectors to a query vector
- **Top-k Retrieval**: Returning the k most relevant chunks
- **Metadata Filtering**: Filtering results based on source, date, page, etc.
- **Index**: Data structure that makes search fast (HNSW, IVF, Flat, etc.)

## Popular Vector Stores (2026 Comparison)

| Vector Store       | Type              | Open Source | Cloud Managed | Ease of Use | Advanced Filtering | Hybrid Search | Scalability       | Best For                          | Recommendation |
|--------------------|-------------------|-------------|---------------|-------------|--------------------|---------------|-------------------|-----------------------------------|----------------|
| **Chroma**         | Embedded/Local    | Yes         | Yes           | ★★★★★       | Good               | Yes           | Medium            | Learning & Prototyping            |  Best for Beginners |
| **FAISS**          | Library           | Yes         | No            | ★★★★        | Basic              | Yes           | High              | Local large-scale experiments     | Excellent for Speed |
| **Qdrant**         | Self-hosted       | Yes         | Yes           | ★★★★        | Excellent          | Yes           | High              | Production with complex filters   | Highly Recommended |
| **Pinecone**       | Fully Managed     | No          | Yes           | ★★★★★       | Good               | Yes           | Very High         | Production serverless             | Best for Production |
| **Weaviate**       | Self-hosted       | Yes         | Yes           | ★★★★        | Excellent          | Yes           | High              | Graph RAG + multimodal            | Advanced Use Cases |
| **LanceDB**        | Embedded          | Yes         | Yes           | ★★★★        | Good               | Yes           | High              | Multimodal & local + cloud        | Great Alternative |
| **Milvus**         | Self-hosted       | Yes         | Yes           | ★★★         | Very Good          | Yes           | Very High         | Enterprise-scale                  | Large Deployments |

### Quick Recommendation Guide

- **Just starting / Learning** → **Chroma**
- **Local & Maximum Speed** → **FAISS**
- **Best balance (2026)** → **Qdrant**
- **Production without ops** → **Pinecone**
- **Multimodal + Knowledge Graph** → **Weaviate**

