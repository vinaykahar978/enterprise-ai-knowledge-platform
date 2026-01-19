from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging
from app.routes.health import router as health_router
from app.middleware.request_id import request_id_middleware

setup_logging()

app = FastAPI(title=settings.app_name)

app.middleware("http")(request_id_middleware)
app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Enterprise AI Platform is running",
        "environment": settings.environment,
    }
