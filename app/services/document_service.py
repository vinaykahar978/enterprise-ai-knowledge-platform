import os
import uuid
from fastapi import UploadFile
from app.services.text_extraction_service import extract_text

DOCUMENTS_DIR = "data/documents"
TEXT_DIR = "data/text"

os.makedirs(DOCUMENTS_DIR, exist_ok=True)
os.makedirs(TEXT_DIR, exist_ok=True)


async def save_document(file: UploadFile):
    document_id = str(uuid.uuid4())
    file_path = os.path.join(DOCUMENTS_DIR, f"{document_id}_{file.filename}")

    contents = await file.read()

    with open(file_path, "wb") as f:
        f.write(contents)

    extracted_text = extract_text(file_path, file.filename)

    text_path = os.path.join(TEXT_DIR, f"{document_id}.txt")
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    return {
        "id": document_id,
        "filename": file.filename,
        "size": len(contents),
        "text_path": text_path,
    }


def list_documents():
    documents = []

    for filename in os.listdir(DOCUMENTS_DIR):
        path = os.path.join(DOCUMENTS_DIR, filename)

        if not os.path.isfile(path):
            continue

        documents.append({
            "filename": filename,
            "size": os.path.getsize(path),
        })

    return documents
