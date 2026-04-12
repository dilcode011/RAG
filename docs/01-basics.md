# 01 - RAG Fundamentals

## What is Retrieval-Augmented Generation (RAG)?

RAG is a technique that combines **retrieval** from an external knowledge base with **generation** by a Large Language Model (LLM).  
Instead of relying only on the LLM’s parametric knowledge, RAG fetches relevant context at inference time and feeds it to the LLM.

### Why RAG?
- Reduces hallucinations
- Provides up-to-date information
- Enables domain-specific answers without fine-tuning
- Improves transparency (you can see what documents were used)
- Cost-effective compared to fine-tuning

## Core Architecture of RAG

1. **Ingestion Pipeline**
   - Load documents (PDF, TXT, HTML, Markdown, etc.)
   - Split into chunks
   - Generate embeddings
   - Store in Vector Database

2. **Retrieval**
   - Convert user query into embedding
   - Perform similarity search (cosine, dot product, etc.)
   - Return top-k relevant chunks

3. **Augmentation**
   - Combine retrieved chunks with the user query

4. **Generation**
   - Send augmented prompt to LLM
   - Get final answer

## Simple RAG Flow
## Key Challenges in Basic RAG
- Poor chunking strategy
- Irrelevant retrieval results
- Context window limits
- Hallucinations even with context
- Slow response time

## Next Steps
→ Learn about Embeddings in [02-embeddings.md](./02-embeddings.md)  
→ Explore Vector Databases in [03-vector-dbs.md](./03-vector-dbs.md)

---