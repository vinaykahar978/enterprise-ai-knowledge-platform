from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.openai_api_key)


def embed_text(text: str) -> list[float]:
    """
    Generate 512-dim embeddings using text-embedding-3-small
    """
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
    )
    embedding = response.data[0].embedding

    assert len(embedding) == 1536, f"Embedding dim mismatch: {len(embedding)}"


    return embedding

