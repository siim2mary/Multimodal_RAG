🎨 Multimodal RAG Service (Memory Enabled)
******************************************************************************************************
# 🧠 Multimodal RAG AI System (FastAPI + Memory + ChromaDB)

An end-to-end **Multimodal Retrieval-Augmented Generation (RAG)** system built with **FastAPI**, supporting:

- 💬 Text-based queries
- 🖼️ Image understanding (Multimodal LLM)
- 📄 PDF-based knowledge retrieval (RAG)
- 🧠 Session-based conversational memory
- ⚡ High-performance inference using Groq LLMs

---

## 🚀 Key Features

- ✅ Multimodal Input (Text + Image)
- ✅ Document Search using RAG (PDF → Vector DB)
- ✅ Semantic Retrieval (ChromaDB + Embeddings)
- ✅ Context-aware Conversations (Session Memory)
- ✅ FastAPI REST API
- ✅ Async LLM Inference
- ✅ Production-ready modular design

---

## 🏗️ System Architecture
      ┌──────────────────────┐
      │     User Input       │
      │  Text + Image + ID   │
      └─────────┬────────────┘
                │
                ▼
      ┌──────────────────────┐
      │     FastAPI API      │
      │     (/chat)          │
      └─────────┬────────────┘
                │
                ▼
      ┌──────────────────────┐
      │   Multimodal Agent   │
      └─────────┬────────────┘
                │
 ┌──────────────┼──────────────┐
 ▼              ▼              ▼
 Memory Image Input Retriever
(Session) (Base64) (ChromaDB)
│
▼
Relevant Chunks
│
▼
LLM (Groq)
│
▼
Final Response

---

## 📂 Project Structure
├── main.py # FastAPI API
├── agent.py # Multimodal RAG + Memory logic
├── ingest.py # PDF → Vector DB pipeline
├── data/
│ └── art_history.pdf
├── chroma_db/ # Auto-created vector database
├── .env # API keys
├── requirements.txt
└── README.md

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/siim2mary/Multimodal_RAG.git
cd Multimodal_RAG
2. Create Virtual Environment
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
3. Install Dependencies
pip install -r requirements.txt
🔐 Environment Setup

Create a .env file:
GROQ_API_KEY=your_groq_api_key_here
📄 Step 1: Build Knowledge Base (RAG)

Run ingestion pipeline:
python ingest.py
🔍 What Happens Here
Loads PDF (art_history.pdf)
Splits into chunks
Converts text → embeddings
Stores in ChromaDB
HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
📁 Output:
chroma_db/
▶️ Step 2: Run FastAPI Server
uvicorn main:app --reload
Open:

API: http://127.0.0.1:8000
Docs: http://127.0.0.1:8000/docs
📡 API Usage
🔹 POST /chat
Request (Form Data)
| Field      | Type   | Required | Description    |
| ---------- | ------ | -------- | -------------- |
| message    | string | ✅        | User query     |
| file       | image  | ❌        | Optional image |
| session_id | string | ❌        | Memory session |
📥 Example Request
curl -X POST "http://127.0.0.1:8000/chat" \
-F "message=Who stole the Mona Lisa?" \
-F "session_id=user_1"
📤 Example Response
{
  "status": "success",
  "session_id": "user_1",
  "agent_response": "The Mona Lisa was stolen by Vincenzo Peruggia in 1911..."
}
🧠 How the System Works
1. RAG Retrieval
Query → embedding
Search in ChromaDB
Top 2 relevant chunks retrieved
docs = vector_db.similarity_search(user_query, k=2)
2. Context Injection

Retrieved content is injected into prompt:
"You are a helpful assistant. Use the following context..."
3. Memory Handling
Uses RunnableWithMessageHistory
Stores chat per session_id
store[session_id] = ChatMessageHistory()
4. Multimodal Input
Image converted to Base64
Passed to LLM as input
"image_url": {"url": f"data:{mime_type};base64,..."}
5. LLM Response

Powered by Groq LLM:
meta-llama/llama-4-scout-17b-16e-instruct
🧩 Core Components
🔹 ingest.py
PDF loading
Chunking
Embeddings
Vector DB creation
🔹 agent.py
RAG retrieval
Memory handling
Multimodal processing
LLM orchestration
🔹 main.py
API layer
Request handling
Response formatting
📦 Tech Stack
Backend: FastAPI
LLM: Groq (LLaMA 4)
Embeddings: HuggingFace MiniLM
Vector DB: ChromaDB
Framework: LangChain
Language: Python
🚀 Future Enhancements
📄 Upload multiple PDFs dynamically
🧠 Hybrid search (BM25 + Vector)
⚡ Streaming responses
🔐 Authentication (JWT)
🐳 Docker deployment
☁️ Deploy on Railway / AWS
🛑 Important Notes
Run ingest.py before using API
Ensure chroma_db/ exists
Works on CPU (no GPU required)
Keep .env secure
🤝 Contributing

Pull requests are welcome!

📄 License

MIT License

👩‍💻 Author

Simmy Xavier
AI Researcher | Machine Learning Engineer