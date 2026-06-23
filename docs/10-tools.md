# 10 - Tools in RAG Systems

## What are Tools in RAG?

**Tools** are external functions or APIs that an LLM can call to perform specific tasks.  
In RAG, tools extend the capabilities of the system beyond just retrieving documents — allowing the LLM to search the web, run code, query databases, call calculators, etc.

Tools + RAG = **Agentic RAG** (one of the most powerful patterns in 2026).

## Why Use Tools with RAG?

- Overcome limitations of static knowledge bases
- Enable real-time information (web search, APIs)
- Perform calculations, data analysis, or actions
- Create multi-step reasoning workflows
- Build intelligent agents that can decide when to retrieve vs use tools

## Tool Types in RAG/Agent Systems

| Tool Type                    | Description                                      | Common Examples                     | Use Case in RAG                     |
|-----------------------------|--------------------------------------------------|-------------------------------------|-------------------------------------|
| **Retrieval Tool**          | Search your vector store                         | Custom RAG retriever                | Core knowledge retrieval            |
| **Web Search Tool**         | Search internet in real-time                     | Tavily, SerpAPI, DuckDuckGo         | Up-to-date information              |
| **Code Interpreter**        | Run Python code safely                           | LangChain PythonREPL                | Math, data analysis                 |
| **Calculator / Math**       | Perform calculations                             | Built-in or LLM-math                | Numerical questions                 |
| **Database Tool**           | Query SQL/NoSQL databases                        | SQLDatabaseChain                    | Structured data                     |
| **API Tools**               | Call external APIs                               | Weather, Stock, GitHub, Gmail       | Real-world actions                  |
| **Custom Tools**            | Your own functions                               | Email sender, PDF generator         | Domain-specific logic               |

## Creating Tools in LangChain

### 1. Simple Custom Tool

```python
from langchain_core.tools import tool

@tool
def get_current_weather(location: str) -> str:
    """Get the current weather for a location."""
    # Call weather API here
    return f"Sunny, 28°C in {location}"

tools = [get_current_weather]