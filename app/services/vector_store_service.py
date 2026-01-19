from pinecone import Pinecone
from app.core.config import settings

# Create Pinecone client (NEW way)
pc = Pinecone(api_key=settings.pinecone_api_key)

# Get index handle
index = pc.Index(settings.pinecone_index_name)


def upsert_chunk_embedding(
    chunk_id: str,
    embedding: list[float],
    metadata: dict,
):
    index.upsert(
        vectors=[
            {
                "id": chunk_id,
                "values": embedding,
                "metadata": metadata,
            }
        ]
    )
