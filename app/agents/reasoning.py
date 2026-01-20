from app.agents.base import Agent
from app.services.prompt_service import build_rag_prompt
from app.llm.gateway import call_llm


class ReasoningAgent(Agent):
    def run(self, question: str, chunks: list[dict]):
        contexts = [c["text"] for c in chunks]
        prompt = build_rag_prompt(question, contexts)
        return call_llm(prompt)
