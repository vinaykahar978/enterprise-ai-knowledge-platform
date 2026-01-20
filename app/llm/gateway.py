from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.openai_api_key)


def call_llm_gateway(
    prompt: str,
    model: str = "gpt-4o-mini",
    temperature: float = 0.2,
) -> dict:
    """
    Central LLM gateway.
    All model calls must go through this function.
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful enterprise AI assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
    )

    return {
        "model": model,
        "text": response.choices[0].message.content,
        "usage": response.usage,
    }
