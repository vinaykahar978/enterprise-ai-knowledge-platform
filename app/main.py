from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Enterprise AI Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://enterprise-ai-knowledge-platform.vercel.app/",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from app.core.config import settings
from app.core.logging import setup_logging
from app.routes.health import router as health_router
from app.middleware.request_id import request_id_middleware
from app.routes.documents.upload import router as document_router
from app.routes.documents.list import router as document_list_router
from app.routes.query.query import router as query_router
from app.routes.ask.ask import router as ask_router
from app.routes.admin.observability import router as admin_router


setup_logging()

app.include_router(health_router)
app.include_router(document_router)
app.include_router(document_list_router)
app.include_router(query_router)
app.include_router(ask_router)
app.include_router(admin_router)

@app.get("/")
def root():
    return {
        "message": "Enterprise AI Platform is running",
        "environment": settings.environment,
    }
