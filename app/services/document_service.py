import os
import uuid
from fastapi import UploadFile

DOCUMENTS_DIR = "data/documents"

os.makedirs(DOCUMENTS_DIR, exist_ok=True)


async def save_document(file: UploadFile):
    document_id = str(uuid.uuid4())
    file_path = os.path.join(DOCUMENTS_DIR, f"{document_id}_{file.filename}")

    contents = await file.read()

    with open(file_path, "wb") as f:
        f.write(contents)

    return {
        "id": document_id,
        "filename": file.filename,
        "size": len(contents),
        "path": file_path
    }

def list_documents():
    documents = []

    for filename in os.listdir(DOCUMENTS_DIR):
        path = os.path.join(DOCUMENTS_DIR, filename)
        size = os.path.getsize(path)

        documents.append({
            "filename": filename,
            "size": size
        })

    return documents
