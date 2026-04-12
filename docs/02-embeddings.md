```markdown
# 02 - Embeddings & Similarity Search

## What are Embeddings?

Embeddings are dense vector representations of text (or other data) that capture semantic meaning.  
Similar texts have vectors that are close in high-dimensional space.

### Popular Embedding Models (2026)

| Model                        | Provider       | Dimension | Strengths                     | Best For                  |
|-----------------------------|----------------|-----------|-------------------------------|---------------------------|
| text-embedding-3-large      | OpenAI         | 3072      | Highest quality               | General purpose           |
| text-embedding-ada-002      | OpenAI         | 1536      | Fast & cheap                  | Most projects             |
| voyage-3                    | Voyage AI      | 1024      | Excellent for long documents  | Enterprise                |
| snowflake-arctic-embed      | Snowflake      | 1024      | Strong open-source            | Local deployment          |
| bge-m3                      | BAAI           | 1024      | Multilingual + dense + sparse | Multilingual apps         |
| nomic-embed-text            | Nomic          | 768       | Excellent local model         | Privacy-focused           |

## How Similarity Search Works

Common distance metrics:
- **Cosine Similarity** (most popular for text)
- Euclidean Distance
- Dot Product

**Formula (Cosine Similarity):**
$$    
\text{similarity} = \frac{A \cdot B}{|A| \cdot |B|}
    $$

## Chunking Strategies

- Fixed-size chunking (simple but often poor)
- Recursive Character Text Splitter (LangChain)
- Semantic Chunking (based on sentence embeddings)
- Hierarchical Chunking
- Agentic Chunking (advanced)

**Tip**: Always experiment with chunk size (256–1024 tokens) and overlap (10–20%).

## Best Practices
- Use the same embedding model for both indexing and querying
- Normalize vectors when using cosine similarity
- Consider hybrid search (dense + sparse) for better recall

**Next:** Learn about storing these embeddings in [03-vector-dbs.md](./03-vector-dbs.md)