from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List
import os
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from vacancy.endpoints import router as vacancy_router
from application.endpoints import router as application_router

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

UPLOAD_DIRECTORY = "static/"

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

app.mount("/static", StaticFiles(directory=UPLOAD_DIRECTORY), name="static")

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
    try:
        with open(file_location, "wb") as f:
            f.write(file.file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")
    return {"filename": file.filename}

@app.get("/uploadfile/")
async def get_all_files() -> List[str]:
    files = os.listdir(UPLOAD_DIRECTORY)
    return files

@app.get("/uploadfile/{application_id}")
async def get_file(application_id: str):
    file_path = os.path.join(UPLOAD_DIRECTORY, application_id)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.delete("/uploadfile/")
async def delete_all_files():
    for filename in os.listdir(UPLOAD_DIRECTORY):
        file_path = os.path.join(UPLOAD_DIRECTORY, filename)
        os.remove(file_path)
    return {"detail": "All files deleted"}

@app.delete("/uploadfile/{application_id}")
async def delete_file(application_id: str):
    file_path = os.path.join(UPLOAD_DIRECTORY, application_id)
    if os.path.exists(file_path):
        os.remove(file_path)
        return {"detail": f"File {application_id} deleted"}
    else:
        raise HTTPException(status_code=404, detail="File not found")
