from app.agents.retriever import RetrieverAgent
from app.agents.reasoning import ReasoningAgent
from app.agents.validator import ValidatorAgent
from app.context.context_models import KnowledgeContext


def run_agentic_flow(question: str, context: KnowledgeContext):
    retriever = RetrieverAgent()
    reasoning = ReasoningAgent()
    validator = ValidatorAgent()

    chunks = retriever.run(question, context)
    raw_answer = reasoning.run(question, chunks)
    final_answer = validator.run(raw_answer, chunks)

    return {
        "answer": final_answer,
        "sources": chunks,
    }
