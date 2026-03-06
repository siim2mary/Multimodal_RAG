import os
import base64
from dotenv import load_dotenv

# LangChain components
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

# New Imports for RAG (PDF Search)
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

# --- 1. MEMORY & DATABASE SETUP ---
store = {}

# Initialize Embeddings once (it runs on your CPU)
# Used for: Turning the user's question into a vector to search the DB
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# --- 2. AGENT FUNCTION ---
async def run_multimodal_agent(user_query: str, image_bytes: bytes = None, mime_type: str = "image/jpeg", session_id: str = "default_user"):
    
    # --- RAG STEP: SEARCH THE PDF ---
    # Load the database you created in ingest.py
    vector_db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
    
    # Search for the 2 most relevant paragraphs from your PDF
    docs = vector_db.similarity_search(user_query, k=2)
    context_text = "\n".join([d.page_content for d in docs])

    # Initialize LLM
    llm = ChatGroq(
        model_name="meta-llama/llama-4-scout-17b-16e-instruct", 
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.2 # Lower temperature is better for factual RAG answers
    )

    # Updated Prompt: Now includes {context} from the PDF
    prompt = ChatPromptTemplate.from_messages([
        ("system", f"You are a helpful assistant. Use the following context from the uploaded documents to answer the user: \n\n {context_text}"),
        MessagesPlaceholder(variable_name="history"),
        MessagesPlaceholder(variable_name="input")
    ])

    chain = prompt | llm

    with_message_history = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )

    # --- 3. MULTIMODAL CONTENT PREPARATION ---
    content = [{"type": "text", "text": user_query}]
    
    if image_bytes:
        image_b64 = base64.b64encode(image_bytes).decode("utf-8")
        content.append({
            "type": "image_url",
            "image_url": {"url": f"data:{mime_type};base64,{image_b64}"}
        })

    user_message = [HumanMessage(content=content)]

    # --- 4. EXECUTION ---
    try:
        config = {"configurable": {"session_id": session_id}}
        response = await with_message_history.ainvoke(
            {"input": user_message}, 
            config=config
        )
        return response.content
        
    except Exception as e:
        return f"Agent Error: {str(e)}"

# --- 5. TEST BLOCK ---
if __name__ == "__main__":
    import asyncio
    async def test():
        # Test query that requires PDF knowledge
        ans = await run_multimodal_agent("Who stole the Mona Lisa in 1911?", session_id="test_rag")
        print(f"Agent Response: {ans}")
    
    asyncio.run(test())