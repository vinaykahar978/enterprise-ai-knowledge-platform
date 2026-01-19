from fastapi import APIRouter
from app.services.document_service import list_documents

router = APIRouter(prefix="/documents", tags=["documents"])


@router.get("/")
def get_documents():
    return list_documents()
