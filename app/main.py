from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging
from app.routes.health import router as health_router

setup_logging()

app = FastAPI(title=settings.app_name)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Enterprise AI Platform is running",
        "environment": settings.environment,
    }
