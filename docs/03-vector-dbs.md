# 03 - Vector Databases

## What is a Vector Database?

A specialized database optimized for storing and querying high-dimensional vectors efficiently.

## Popular Vector Databases (2026)

| Database     | Type          | Open Source | Cloud Offering      | Strengths                          | Best Use Case                  |
|--------------|---------------|-------------|---------------------|------------------------------------|--------------------------------|
| Chroma       | Local/Embedded| Yes         | Yes                 | Easiest for beginners              | Learning & prototyping         |
| FAISS        | Library       | Yes         | No                  | Extremely fast                     | Large-scale local search       |
| Pinecone     | Managed       | No          | Yes                 | Serverless, scalable               | Production apps                |
| Qdrant       | Self-hosted   | Yes         | Yes                 | Filtering + payloads               | Advanced filtering             |
| Weaviate     | Self-hosted   | Yes         | Yes                 | Graph-like relations               | Knowledge graph + RAG          |
| Milvus       | Self-hosted   | Yes         | Yes                 | Massive scale                      | Enterprise                     |
| LanceDB      | Embedded      | Yes         | Yes                 | Great for multimodal               | Local + cloud hybrid           |

## Key Features to Consider
- **Filtering** (metadata filtering)
- **Hybrid Search** (vector + keyword)
- **Payload / Metadata** storage
- **Scalability**
- **Real-time updates**
- **Observability**

## When to Choose What?

- **Learning**: Start with **Chroma**
- **Local & Fast**: **FAISS** or **LanceDB**
- **Production (managed)**: **Pinecone**
- **Advanced filtering**: **Qdrant**
- **Multimodal**: **Weaviate** or **LanceDB**

## Basic Operations
1. Create collection/index
2. Add vectors + metadata
3. Query with filter
4. Delete / Update documents

**Next:** Move to advanced RAG techniques in [04-advanced-rag.md](./04-advanced-rag.md)