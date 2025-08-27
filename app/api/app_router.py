from pydantic import BaseModel
from typing import Union, Annotated
from fastapi import File, UploadFile, APIRouter
from app.services.llm_manager import LLM_Manager
from app.services.md_manager import MD_Manager

router = APIRouter()
# app = FastAPI()

@router.post("/upload-cv-profile/")
def upload_cv_profile(job_profile: str, file: Annotated[UploadFile , File(description="Upload your CV as PDF/Docx")]):
    obj_llm = LLM_Manager()
    obj_md = MD_Manager()
    # Read file content
    content = obj_md.pdf_to_markdown(file.file)

    obj_llm.process_document(content)
    return {"filename": file.filename, "type": file.content_type, "size": len(content), "message": content.decode('utf-8', errors='ignore')[:100] + '...'}