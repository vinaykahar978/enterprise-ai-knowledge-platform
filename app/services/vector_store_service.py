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

def query_similar_chunks(
    embedding: list[float],
    top_k: int = 5,
):
    response = index.query(
        vector=embedding,
        top_k=top_k,
        include_metadata=True,
    )

    results = []

    for match in response.matches:
        results.append({
            "chunk_id": match.id,
            "score": match.score,
            "document_id": match.metadata.get("document_id"),
            "chunk_index": match.metadata.get("chunk_index"),
            "text": match.metadata.get("text"),
        })

    return results

