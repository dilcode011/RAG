from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path='/RAG/data/dir',
    glob='*.pdf',
    loader_cls=PyPDFLoader   
)

docs=loader.load()


for document in docs:
    print(document.metadata)

#lazy load
### It is used to deal with large documents or lots of files
### Returns : A generator of Document objects

docs=loader.lazy_load()

print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)