def build_rag_prompt(question: str, contexts: list[str]) -> str:
    context_block = "\n\n".join(contexts)

    return f"""
You are an AI assistant that answers questions strictly using the provided context.
If the answer is not present in the context, respond with "I don't know".

Context:
{context_block}

Question:
{question}

Answer:
""".strip()
