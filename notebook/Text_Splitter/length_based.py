from langchain.text_splitter import CharacterTextSplitter

text=""" 
Artificial Intelligence (AI) is the ability of machines to perform tasks that usually require human intelligence. It includes learning from data, recognizing patterns, and making decisions. AI systems can improve their performance over time using experience. It is widely used in everyday life, such as voice assistants, recommendation systems, and self-driving cars. AI works through techniques like machine learning and deep learning. It helps automate repetitive tasks and increases efficiency. AI can analyze large amounts of data quickly and accurately. It is used in fields like healthcare, education, and business. However, AI also raises concerns about privacy and job loss. Overall, AI is a powerful technology that is transforming the modern world.
"""
splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,      #Chunk overlap means repeating some part of text between two chunks (pieces) so that important information is not lost. 

    separator=""
)

result=splitter.split_text(text)
print(result)





#Text Splitter with Document loader

from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('/workspaces/RAG/data/dir/unit 3 notes.pdf')

docs=loader.load()

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)

result=splitter.split_documents(docs)
print(result)