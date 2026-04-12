# 04 - Advanced RAG Techniques

## Beyond Naive RAG

Basic RAG often suffers from poor retrieval quality. Advanced techniques solve these problems.

### 1. Query Transformations
- **Multi-Query Retriever**: Generate multiple versions of the query
- **HyDE (Hypothetical Document Embeddings)**: Generate a hypothetical answer first
- **Step-Back Prompting**: Ask a higher-level question first

### 2. Reranking
- Use a reranker model (Cohere Rerank, bge-reranker, FlashRank)
- Improves precision by re-scoring top-k results

### 3. Context Compression / Summarization
- Long-context compression
- LLM-based context summarizer before generation

### 4. Self-RAG & Adaptive RAG
- LLM critiques its own retrieval
- Dynamically decides whether to retrieve or not

### 5. Routing & Query Decomposition
- Route query to different indexes or tools
- Decompose complex questions into sub-questions

### 6. Corrective RAG (CRAG)
- Web search fallback when retrieval confidence is low
- Knowledge refinement step

### 7. Agentic RAG
- Use LangGraph or CrewAI to create multi-step reasoning workflows

## Popular Advanced Patterns (2026)
- **Parent-Document Retriever**
- **Sentence-Window Retrieval**
- **Auto-Merging Retriever**
- **Graph RAG**
- **Multi-Modal RAG**

**Pro Tip**: Combine 2–3 techniques based on your use case. Start simple and iterate.

**Next:** Learn how to properly evaluate your RAG system in [05-evaluation.md](./05-evaluation.md)