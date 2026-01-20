from fastapi import APIRouter
from pydantic import BaseModel
from app.services.answer_service import generate_answer
from app.context.context_models import KnowledgeContext

router = APIRouter(prefix="/ask", tags=["ask"])


class AskRequest(BaseModel):
    question: str
    context: KnowledgeContext


@router.post("/")
def ask_question(request: AskRequest):
    return generate_answer(
        question=request.question,
        context=request.context,
    )

