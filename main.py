from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from agent import run_multimodal_agent
import uvicorn

app = FastAPI(title="Multimodal RAG Service (Memory Enabled)")

@app.post("/chat")
async def chat_endpoint(
    message: str = Form(...),
    file: UploadFile = File(None),
    # Added session_id so the agent knows which 'memory' to use
    session_id: str = Form("default_user") 
):
    try:
        file_bytes = None
        mime_type = "image/jpeg"
        
        if file:
            file_bytes = await file.read()
            mime_type = file.content_type

        # Now passing session_id to our updated agent logic
        response = await run_multimodal_agent(
            user_query=message, 
            image_bytes=file_bytes, 
            mime_type=mime_type,
            session_id=session_id
        )
        
        return {
            "status": "success", 
            "session_id": session_id,
            "agent_response": response
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)