from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

loader=TextLoader('RAG/data/AI.txt',encoding='utf-8')

load_dotenv()

model=ChatOpenAI()

prompt=PromptTemplate(
    template='write a summary for the following poem - {poem}',
    input_variables=['poem']
)

parser=StrOutputParser()


docs=loader.load()
print(docs)
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)
print(type(docs))     #Type will be list



#chain
chain=prompt | model | parser
result=chain.invoke({'poem':docs[0].page_content})
print(result)