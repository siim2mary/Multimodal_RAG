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
