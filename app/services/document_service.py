import os
import uuid
from fastapi import UploadFile
from app.services.text_extraction_service import extract_text
from app.services.chunking_service import chunk_text


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

    # 🔹 CHUNKING
    chunks = chunk_text(extracted_text)

    chunk_records = []
    for index, chunk in enumerate(chunks):
        chunk_id = f"{document_id}_{index}"
        chunk_path = os.path.join("data/chunks", f"{chunk_id}.txt")

        with open(chunk_path, "w", encoding="utf-8") as f:
            f.write(chunk)

        chunk_records.append({
            "chunk_id": chunk_id,
            "document_id": document_id,
            "index": index,
            "path": chunk_path,
        })

    return {
        "id": document_id,
        "filename": file.filename,
        "size": len(contents),
        "text_path": text_path,
        "chunks": chunk_records,
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
