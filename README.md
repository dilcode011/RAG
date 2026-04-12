# RAG Learning Journey 
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-⚡-green.svg)](https://python.langchain.com/)
[![Status](https://img.shields.io/badge/Status-Active_Learning-orange.svg)]()

**Repository for learning Retrieval-Augmented Generation (RAG) from scratch**  

This repo is my **personal learning playground** for mastering RAG systems.  
It contains:
- Code examples & Jupyter notebooks
- Step-by-step implementations (from naive RAG → advanced production-grade RAG)
- Detailed notes & explanations
- Mini-projects & full applications
- Evaluation scripts, benchmarks, and experiments
- Resources, papers, and best practices

**Goal**: Go from zero to building production-ready RAG applications while documenting everything publicly.

---

##  Features

- **Beginner-friendly** notebooks that explain every line
- **Progressive difficulty** – each folder builds on the previous one
- **Multiple frameworks** covered (LangChain, LlamaIndex, Haystack, LangGraph)
- **Real-world datasets** & evaluation metrics (RAGAS, ARES, DeepEval)
- **Modern tech stack** (2026 standards): OpenAI, Grok, Claude, local LLMs (Ollama), vector DBs, etc.
- **Clean project structure** ready for GitHub + future portfolio use

---

## Repository Structure

```bash
rag-learning-journey/
├── README.md                
├── .gitignore
│
├── docs/                     # Detailed documentation & theory
│   ├── 01-basics.md
│   ├── 02-embeddings.md
│   ├── 03-vector-dbs.md
│   ├── 04-advanced-rag.md
│   └── 05-evaluation.md
│
├── notebooks/                # Jupyter notebooks (main learning area)
│   ├── 01-naive-rag/
│   ├── 02-langchain-rag/
│   ├── 03-llamaindex-rag/
│   ├── 04-advanced-techniques/
│   └── 05-multi-modal-rag/
│
├── src/                      # Reusable Python modules & utilities
│   ├── rag/                  # Core RAG classes
│   ├── evaluation/
│   └── utils/
│
├── projects/                 # End-to-end applications
│   ├── 01-pdf-chatbot/
│   ├── 02-youtube-rag/
│   ├── 03-agentic-rag/
│   └── 04-production-rag/
│
├── data/                     # Sample datasets (PDFs, CSVs, etc.)
├── experiments/              # Quick experiments & ablation studies
├── resources/                # Papers, cheat sheets, links
└── requirements.txt
