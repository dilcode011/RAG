# 06 - Document Loaders in RAG

## What are Document Loaders?

Document Loaders are the **first step** in any RAG pipeline.  
They are responsible for **loading raw documents** from various sources and converting them into a standard format (usually LangChain's `Document` object) that contains:

- `page_content`: The actual text
- `metadata`: Additional information (source, page number, file name, date, etc.)

Good document loading is crucial because **garbage in = garbage out** in RAG systems.

## Why Document Loaders Matter

- Handle different file formats (PDF, DOCX, TXT, Markdown, HTML, JSON, CSV, etc.)
- Preserve important metadata
- Support unstructured data (images, tables, charts in PDFs)
- Enable incremental loading & updates
- Work with web pages, databases, APIs, cloud storage, etc.

## Popular Document Loaders (2026)

### 1. Text-based Loaders
- `TextLoader` – Simple `.txt` files
- `DirectoryLoader` – Load entire folders recursively
- `JSONLoader` / `JSONLinesLoader`
- `CSVLoader`
- `MarkdownLoader`

### 2. Document Format Loaders
- `PyPDFLoader` (simple ,clean)
- `PyMuPDFLoader` (for layout and image data)
- `PDFPlumberLoader` (excellent for tables)
- `UnstructuredPDFLoader` / `AmazonTextractPDFLoader` (best for complex layouts, images, tables)
- `Docx2txtLoader` / `DocxLoader`
- `UnstructuredWordDocumentLoader` (want best structure extraction)

### 3. Web & API Loaders
- `WebBaseLoader` (BeautifulSoup)
- `AsyncHtmlLoader` + `Html2TextTransformer`
- `SeleniumURLLoader` (for JavaScript-heavy sites)
- `PlaywrightLoader` (most powerful for dynamic websites)
- `RSSFeedLoader`
- `GitHubLoader`, `NotionLoader`, `ConfluenceLoader`

### 4. Multimodal & Advanced Loaders
- `UnstructuredLoader` (supports 50+ file types)
- `LlamaParse` (best-in-class for complex PDFs – tables, layouts, images)
- `AzureAIDocumentIntelligenceLoader` (Microsoft)
- `AmazonTextractPDFLoader`

## Best Practices for Document Loading

1. **Choose the right loader**
   - Simple text → `TextLoader`
   - Complex PDFs with tables → `UnstructuredPDFLoader` or `LlamaParse`
   - Need speed → `PyMuPDFLoader`

2. **Always preserve metadata**
   ```python
   metadata = {
       "source": "file_path.pdf",
       "page": 5,
       "file_name": "research_paper.pdf",
       "upload_date": "2026-04-13"
   }