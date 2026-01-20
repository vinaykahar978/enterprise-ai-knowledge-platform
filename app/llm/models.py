from pydantic import BaseModel
from typing import Optional


class LLMRequest(BaseModel):
    prompt: str
    model: str = "gpt-4.1-mini"
    max_tokens: int = 512


class LLMResponse(BaseModel):
    text: str
    model: str
    estimated_cost: float
