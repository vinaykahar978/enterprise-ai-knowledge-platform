from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.orchestrator import run_agent_pipeline

router = APIRouter(prefix="/ask", tags=["ask"])


class AskRequest(BaseModel):
    question: str
    context: dict | None = None


@router.post("")
async def ask_question(req: AskRequest):
    return await run_agent_pipeline(
        question=req.question,
        context=req.context,
    )
