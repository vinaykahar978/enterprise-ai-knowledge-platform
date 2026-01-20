from app.context.context_models import KnowledgeContext
from app.context.context_resolver import resolve_context
from app.services.embedding_service import embed_text
from app.services.vector_store_service import query_similar_chunks


def retrieve_relevant_chunks(
    query: str,
    context: KnowledgeContext,
):
    resolved_context = resolve_context(context)

    query_embedding = embed_text(query)

    results = query_similar_chunks(
        embedding=query_embedding,
        top_k=resolved_context.max_chunks,
    )

    # Optional filtering by document_id
    if resolved_context.allowed_document_ids:
        results = [
            r for r in results
            if r["document_id"] in resolved_context.allowed_document_ids
        ]

    return results
