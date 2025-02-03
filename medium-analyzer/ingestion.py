import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

if __name__ == "__main__":
    print("Ingesting...")
    
    loader = TextLoader("./mediumblog1.txt", encoding="utf-8")
    documents = loader.load()
    
    print("splitting...")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    chunks = text_splitter.split_documents(documents)
    
    print(f"chunks: {len(chunks)} chunks")
    
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    
    print("ingesting...")
    PineconeVectorStore.from_documents(chunks, embeddings, index_name=os.getenv("INDEX_NAME"))
    
    print("done")
