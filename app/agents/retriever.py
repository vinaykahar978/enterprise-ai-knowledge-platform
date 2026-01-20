from app.agents.base import Agent
from app.context.context_models import KnowledgeContext
from app.services.query_service import retrieve_relevant_chunks


class RetrieverAgent(Agent):
    def run(self, question: str, context: KnowledgeContext):
        return retrieve_relevant_chunks(
            query=question,
            context=context,
        )
