import os
from pydantic import BaseModel
from typing import Union, Annotated
from fastapi import File, UploadFile, APIRouter
from app.services.llm_manager import LLM_Manager
from app.services.md_manager import MD_Manager
from app.services.prompt_manager import generate_prompt

router = APIRouter()
# app = FastAPI()

@router.post("/upload-cv-profile/")
def upload_cv_profile(job_profile: str, file: Annotated[UploadFile , File(description="Upload your CV as PDF/Docx")]):
    obj_llm = LLM_Manager()
    obj_md = MD_Manager()
    # Read file content
    # md_file = file.filename
    
    base, _ = os.path.splitext(file.filename)
    md_file = base + ".md"
    content = obj_md.pdf_to_markdown(file.file, md_file)

    print(content)

    # Generate prompt
    prompt = generate_prompt(resume=content, job_profile=job_profile)
    print(prompt)

    response = obj_llm.generate_text_response(prompt)
    return {"filename": file.filename, "type": file.content_type, "size": len(content), "message": response}