# 09 - Retrievers in RAG

## What is a Retriever?

A **Retriever** is the component responsible for fetching the most relevant documents/chunks from the **Vector Store** based on the user's query.

It is the **bridge** between the user query and the context that will be sent to the LLM.  
A good retriever significantly improves the quality of the final answer.

## Why Retrievers Matter

- Convert raw similarity search into intelligent retrieval
- Support advanced techniques beyond simple top-k search
- Improve precision and recall
- Enable complex workflows (multi-step retrieval, routing, etc.)
- Make RAG systems more robust and production-ready

## Core Retriever Types

| Retriever Type                  | Description                                      | Complexity | Best For                              | Recommendation |
|--------------------------------|--------------------------------------------------|------------|---------------------------------------|----------------|
| **VectorStoreRetriever**       | Basic similarity search                          | Low        | Beginners, simple RAG                 | Starting Point |
| **MultiQueryRetriever**        | Generates multiple query variations              | Medium     | Ambiguous or complex questions        | Highly Recommended |
| **ContextualCompressionRetriever** | Compresses retrieved documents                | Medium     | Long context, reducing noise          | Excellent      |
| **ParentDocumentRetriever**    | Retrieves small chunks but returns parent docs   | Medium     | When fine-grained + full context needed | Advanced Use |
| **EnsembleRetriever**          | Combines multiple retrievers (vector + keyword)  | Medium     | Hybrid search                         | Production     |
| **SelfQueryRetriever**         | Uses LLM to convert query into structured filter | Medium     | Metadata-heavy datasets               | Great for filtering |
| **TimeWeightedRetriever**      | Considers recency of documents                   | Low        | Time-sensitive data                   | Specific cases |
| **BM25 / Keyword Retriever**   | Traditional keyword search                       | Low        | Hybrid setups                         | Complementary  |

## 1. Basic VectorStore Retriever

```python
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

vector_store = Chroma(..., embedding_function=OpenAIEmbeddings())

retriever = vector_store.as_retriever(
    search_type="similarity",      # or "mmr", "similarity_score_threshold"
    search_kwargs={"k": 6}         # top 6 documents
)

retrieved_docs = retriever.invoke("What is RAG?")