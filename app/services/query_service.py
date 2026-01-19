from app.services.embedding_service import embed_text
from app.services.vector_store_service import query_similar_chunks


def retrieve_relevant_chunks(
    query: str,
    top_k: int = 5,
):
    query_embedding = embed_text(query)

    results = query_similar_chunks(
        embedding=query_embedding,
        top_k=top_k,
    )

    return results
