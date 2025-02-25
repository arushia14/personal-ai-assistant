import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Function to load and process PDFs
def load_pdfs(pdf_files):
    documents = []
    for pdf in pdf_files:
        loader = PyPDFLoader(pdf)
        documents.extend(loader.load())
    return documents

# Function to create an in-memory vector database
def create_vector_db(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    
    # Generate embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vector_db = FAISS.from_documents(texts, embeddings)
    
    return vector_db

# Load PDFs and create vector database
pdf_files = ["data/pdf1.pdf"]  # Update with your PDFs
documents = load_pdfs(pdf_files)
vector_db = create_vector_db(documents)
