from app.llm.gateway import call_llm_gateway
from app.llm.observability import log_llm_call


class ReasoningAgent:
    def run(self, question: str, chunks: list[dict]) -> str:
        """
        Generates an answer using retrieved chunks.
        """

        context_text = "\n\n".join(
            f"- {c['text']}" for c in chunks
        )

        prompt = f"""
You are an enterprise AI assistant.
Answer the question using ONLY the context below.

Context:
{context_text}

Question:
{question}

Answer:
"""

        response = call_llm_gateway(prompt)

        log_llm_call(
            request={"prompt": prompt},
            response=response,
        )

        return response["text"]
