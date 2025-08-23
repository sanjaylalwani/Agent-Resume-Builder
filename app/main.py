from typing import Union, Annotated
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/upload-cv-profile/")
async def upload_cv_profile(job_profile: str, file: Annotated[UploadFile , File(description="Upload your CV as PDF/Docx")]):
    # Read file content
    content = await file.read()
    
    # Example: Save file locally
    with open(f"data/{file.filename}", "wb") as f:
        f.write(content)

    return {"filename": file.filename, "type": file.content_type, "size": len(content), "message": content.decode('utf-8', errors='ignore')[:100] + '...'}