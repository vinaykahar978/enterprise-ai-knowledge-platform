"""

DEPRECATED MODULE

This service previously handled direct answer generation using OpenAI.
It has been intentionally disabled to enforce LLM governance via:

- Agent Orchestration
- Context Control Plane
- LLM Gateway with Observability

Do NOT use this module.




from openai import OpenAI
from app.core.config import settings
from app.services.query_service import retrieve_relevant_chunks
from app.services.prompt_service import build_rag_prompt

client = OpenAI(api_key=settings.openai_api_key)


def generate_answer(question: str, top_k: int = 5):
    retrieved_chunks = retrieve_relevant_chunks(
        query=question,
        top_k=top_k,
    )

    contexts = [chunk["text"] for chunk in retrieved_chunks]

    prompt = build_rag_prompt(
        question=question,
        contexts=contexts,
    )

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    return {
        "answer": response.choices[0].message.content,
        "sources": retrieved_chunks,
    }
"""

raise RuntimeError(
    "answer_service is deprecated. "
    "Use agent orchestrator + llm gateway instead."
)