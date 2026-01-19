from fastapi import APIRouter
from pydantic import BaseModel
from app.services.query_service import retrieve_relevant_chunks

router = APIRouter(prefix="/query", tags=["query"])


class QueryRequest(BaseModel):
    question: str
    top_k: int = 5


@router.post("/")
def query_knowledge(request: QueryRequest):
    results = retrieve_relevant_chunks(
        query=request.question,
        top_k=request.top_k,
    )

    return {
        "question": request.question,
        "results": results,
    }
