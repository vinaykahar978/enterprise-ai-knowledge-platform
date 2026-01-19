from fastapi import APIRouter
from pydantic import BaseModel
from app.services.answer_service import generate_answer

router = APIRouter(prefix="/ask", tags=["ask"])


class AskRequest(BaseModel):
    question: str
    top_k: int = 5


@router.post("/")
def ask_question(request: AskRequest):
    return generate_answer(
        question=request.question,
        top_k=request.top_k,
    )
