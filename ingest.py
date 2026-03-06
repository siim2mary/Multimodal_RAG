import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def ingest_docs():
    # 1. Load the PDF you created
    loader = PyPDFLoader("data/art_history.pdf")
    data = loader.load()

    # 2. Split into chunks so the AI can "digest" it
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    chunks = text_splitter.split_documents(data)

    # 3. Initialize the Embedding model (This runs on your CPU)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 4. Create the Database
    print("Building Knowledge Base...")
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )
    print("Success! You can now run the agent.")

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    ingest_docs()