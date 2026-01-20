from app.llm.models import LLMRequest, LLMResponse
from app.services.openai_client import call_openai  # existing helper


def call_llm_gateway(request: LLMRequest) -> LLMResponse:
    text = call_openai(
        prompt=request.prompt,
        model=request.model,
        max_tokens=request.max_tokens,
    )

    # Cost estimation placeholder (rough)
    estimated_cost = len(request.prompt) * 0.000001

    return LLMResponse(
        text=text,
        model=request.model,
        estimated_cost=estimated_cost,
    )
