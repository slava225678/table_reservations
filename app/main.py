from fastapi import FastAPI

from app.core.config import settings
from app.routers.routers import main_router

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description
)

app.include_router(main_router)


@app.get("/")
def read_root():
    return {"message": "Table reservations API"}
