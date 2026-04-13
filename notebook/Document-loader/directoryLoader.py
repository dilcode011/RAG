
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path='/RAG/data/dir',
    glob='*.pdf',
    loader_cls=PyPDFLoader   
)

docs=loader.load()
print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)




# Python source code files are common in RAG applications, especially when building code assistants, documentation bots, or repository-aware RAG systems.

### Python File Loaders Comparison

| Loader                        | What It Loads                          | Key Features                              | Best Use Case                          | Recommended |
|-------------------------------|----------------------------------------|-------------------------------------------|----------------------------------------|-------------|
| `PythonLoader`                | Single `.py` file                      | Extracts code + comments, preserves structure | Single script analysis                 | ⭐ Yes      |
| `DirectoryLoader` + `glob="**/*.py"` | All `.py` files in directory (recursive) | Fast, supports metadata, progress bar     | Entire codebase / project              | ⭐ Best     |
| `TextLoader`                  | Any text file (including `.py`)        | Simple, lightweight                       | Quick prototyping                      | Good       |
| `UnstructuredPythonLoader`    | `.py` files with advanced parsing      | Better handling of classes, functions     | Code understanding & summarization     | Advanced   |
| `GitLoader`                   | Python files from GitHub repository    | Loads directly from remote repo           | Open-source project RAG                | Excellent  |
| `NotebookLoader`              | Jupyter `.ipynb` files                 | Converts notebooks to clean text          | Learning repos & tutorials             | For Notebooks |

### Glob Patterns for Loading Python Files

You can combine `DirectoryLoader` with these glob patterns:

| Glob Pattern          | What It Loads                                      | Example Use Case                     |
|-----------------------|----------------------------------------------------|--------------------------------------|
| `**/*.py`             | All `.py` files recursively (recommended)          | Full project codebase                |
| `*.py`                | Only `.py` files in root directory                 | Main scripts only                    |
| `src/**/*.py`         | All Python files inside `src/` folder              | Source code only                     |
| `**/*test*.py`        | Test files only                                    | Testing documentation                |
| `**/*.py` + `exclude` | All `.py` except certain folders                   | Skip `venv/`, `__pycache__/`         |

