<<<<<<< HEAD
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
=======
🎨 Multimodal RAG Service (Memory Enabled)
******************************************************************************************************
A sophisticated Retrieval-Augmented Generation (RAG) system that combines Art History knowledge with Visual Analysis. This system uses a local vector database on the D: drive and maintains conversation memory across sessions.

🚀 Key Features
**********************************************
Multimodal Input: Processes both text queries and image uploads (e.g., analyzing the Mona Lisa).

Contextual Memory: Tracks conversations via session_id to handle follow-up questions like "Who caught him?".

Space Efficient: Built to run entirely on the D: Drive to bypass C: drive storage limits.

FastAPI Integration: Interactive Swagger UI for easy testing.

🛠️ Installation & Setup (D: Drive)
**************************************************************
Follow these steps to ensure all heavy AI libraries (Torch, Transformers) are stored on your secondary drive.

1. Initialize the Environment
2. Activation & Dependencies
📖 How to Use
1. Data Ingestion
Run this once to process your art_history.pdf into the searchable vector store:

2. Launch the Service
******************************
Start the FastAPI server:

API Docs: Open http://127.0.0.1:8000/docs in your browser.

🧪 Example API Call
You can test the service directly in the browser or via curl:

📂 Project Structure
***************************************************
agent.py: The logic "brain" handling LLM and RAG coordination.

ingest.py: Script for chunking PDFs and creating embeddings.

main.py: The API entry point and session manager.

chroma_db/: Persistent vector storage (on D:).

.venv/: Isolated Python environment.

Troubleshooting Tips
Disk Space: If you get "Out of Space" errors, ensure the .venv folder is deleted and recreated specifically on the D: drive.

Activation: Always check for the (.venv) prefix in your terminal before running scripts.

To get your project running on the D: drive and bypass your full C: drive, we followed a specific strategy to redirect Python's behavior.

Here is the step-by-step breakdown of the commands we used and why.

Step 1: The "Clean Slate" Command
Because previous installations failed due to space, we had to ensure no "broken" folders remained.

Command: rm -Recurse -Force .venv

Purpose: Force-deleted the corrupted environment folder on the D: drive.

Step 2: Creating the Environment on D:
We needed to tell the Python "engine" on your C: drive to build its "workspace" on your D: drive.

Command: &
python.exe -m venv .venv
bash   
(python -m venv .venv)
pip install python-dotenv
pip install -r requirements.txt
python -m pip install langchain langchain-community langchain-groq langchain-chroma langchain-huggingface sentence-transformers python-dotenv
python -m pip cache purge
pip install unstructured[all-docs] chromadb pillow
python -m pip install pypdf
>>>>>>> e1994a353c8517511383276eee28da5e18143b38
