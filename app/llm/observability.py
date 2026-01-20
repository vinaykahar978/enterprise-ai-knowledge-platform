import logging
from app.llm.models import LLMRequest, LLMResponse
from app.llm.observability import LLM_CALL_LOGS

LLM_CALL_LOGS: list[dict] = []

logger = logging.getLogger("llm_observability")

@router.get("/llm")
def get_llm_usage():
    return LLM_CALL_LOGS


def log_llm_call(request: LLMRequest, response: LLMResponse):
    entry = {
        "model": response.model,
        "cost": response.estimated_cost,
        "prompt_length": len(request.prompt),
    }
    LLM_CALL_LOGS.append(entry)

    logger.info(
        f"LLM_CALL | model={response.model} | cost={response.estimated_cost:.6f}"
    )

