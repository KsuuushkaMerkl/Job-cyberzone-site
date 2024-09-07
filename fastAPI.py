from fastapi import FastAPI, UploadFile, File
from typing import Union
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from vacancy.endpoints import router as vacancy_router
from application.endpoints import router as application_router

from core.database import engine
from core.base_model import Base


app = FastAPI(
    title="Job cyberzone site"
)

app.include_router(vacancy_router, prefix="/vacancy", tags=["Vacancies"])
app.include_router(application_router, prefix="/application", tags=["Applications"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


app.mount("/static", StaticFiles(directory="static"))


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    with open("static/" + file.filename, "wb") as f:
        f.write(file.file.read())
    return {"filename": file.filename}
