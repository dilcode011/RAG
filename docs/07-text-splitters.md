# 07 - Text Splitters in RAG

## What are Text Splitters?

Text Splitters are responsible for **breaking large documents into smaller chunks** before generating embeddings and storing them in a vector database.

This is one of the **most critical steps** in a RAG pipeline because:
- LLMs have limited context windows
- Chunk size directly impacts retrieval quality and cost
- Poor splitting = irrelevant or incomplete context

**Good chunking = Better retrieval accuracy**

## Why Text Splitting Matters

- Prevents exceeding LLM context limits
- Improves semantic relevance of retrieved chunks
- Balances between too much noise and too little information
- Affects embedding quality and retrieval speed
- Influences final answer quality significantly

## Popular Text Splitters (2026)

| Splitter                          | Splitting Strategy                  | Best For                              | Pros                              | Cons                              | Recommended |
|-----------------------------------|-------------------------------------|---------------------------------------|-----------------------------------|-----------------------------------|-------------|
| `RecursiveCharacterTextSplitter` | Recursive (by separators)           | Most general use cases                | Simple, effective, customizable   | Can break sentences               |  Best     |
| `CharacterTextSplitter`           | Fixed character length              | Simple text                           | Very fast                         | Poor semantic boundaries          | Good       |
| `TokenTextSplitter`               | By tokens (tiktoken)                | When using OpenAI/Claude models       | Precise token control             | Slower                            | Excellent  |
| `SemanticChunker`                 | Based on semantic similarity        | High-quality retrieval                | Best semantic coherence           | Slower & more expensive           | Advanced   |
| `MarkdownHeaderTextSplitter`      | By Markdown headers                 | Documentation & Markdown files        | Preserves structure               | Only for Markdown                 | For MD     |
| `HTMLHeaderTextSplitter`          | By HTML headers                     | Web pages & HTML                      | Keeps hierarchy                   | HTML-specific                     | For HTML   |
| `RecursiveJsonSplitter`           | For JSON data                       | Structured JSON documents             | Maintains structure               | JSON only                         | For JSON   |
| `CodeSplitter`                    | By language syntax                  | Source code (.py, .js, etc.)          | Preserves code blocks             | Language-specific                 | For Code   |
