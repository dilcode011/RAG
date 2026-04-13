from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
 
loader=PyPDFLoader('RAG/data/AI_Engineer.pdf')

docs=loader.load()
print(docs)
print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)

