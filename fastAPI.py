from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

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


@app.on_event("startup")
def start():
    Base.metadata.create_all(engine)
