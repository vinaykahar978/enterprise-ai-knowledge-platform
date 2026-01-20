from fastapi import APIRouter
from pydantic import BaseModel
from app.services.query_service import retrieve_relevant_chunks
from app.context.context_models import KnowledgeContext

router = APIRouter(prefix="/query", tags=["query"])


class QueryRequest(BaseModel):
    question: str
    context: KnowledgeContext

@router.post("/")
def query_knowledge(request: QueryRequest):
    results = retrieve_relevant_chunks(
        query=request.question,
        context=request.context,
    )


    return {
        "question": request.question,
        "results": results,
    }
