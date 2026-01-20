import logging
from app.llm.models import LLMRequest, LLMResponse

logger = logging.getLogger("llm_observability")


def log_llm_call(request: LLMRequest, response: LLMResponse):
    logger.info(
        f"LLM_CALL | model={response.model} | "
        f"cost={response.estimated_cost:.6f}"
    )
