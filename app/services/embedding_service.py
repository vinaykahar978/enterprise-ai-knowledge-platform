from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.openai_api_key)


def embed_text(text: str) -> list[float]:
    """
    Generate embedding using text-embedding-3-small (512 dims)
    """
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding
