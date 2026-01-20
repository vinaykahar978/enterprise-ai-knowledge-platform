from app.agents.base import Agent
from app.llm.models import LLMRequest
from app.llm.gateway import call_llm_gateway
from app.llm.observability import log_llm_call
from app.services.prompt_service import build_rag_prompt


class ReasoningAgent(Agent):
    def run(self, question: str, chunks: list[dict]):
        contexts = [c["text"] for c in chunks]
        prompt = build_rag_prompt(question, contexts)

        request = LLMRequest(prompt=prompt)
        response = call_llm_gateway(request)

        log_llm_call(request, response)

        return response.text
