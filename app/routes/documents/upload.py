from fastapi import APIRouter, UploadFile, File
from app.services.document_service import save_document

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    document = await save_document(file)
    return {
        "id": document["id"],
        "filename": document["filename"],
        "size": document["size"]
    }
