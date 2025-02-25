import os
import openai
from dotenv import load_dotenv
from components.document_loader import vector_db

# Load API keys from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def get_response(query):
    """Retrieves context from PDFs and queries OpenAI for an answer"""
    
    # Retrieve relevant document chunks
    retriever = vector_db.as_retriever()
    docs = retriever.get_relevant_documents(query)
    context = "\n".join([doc.page_content for doc in docs])

    # Construct the prompt
    prompt = f"""
    Use the following extracted context from PDFs to answer the user's question:
    {context}

    Question: {query}
    Answer:
    """

    # Query OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
