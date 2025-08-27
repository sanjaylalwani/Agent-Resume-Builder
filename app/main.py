from fastapi import FastAPI
from app.api.app_router import router as cv_router


app = FastAPI()
app.include_router(cv_router)
