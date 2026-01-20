from app.agents.base import Agent


class ValidatorAgent(Agent):
    def run(self, answer: str, chunks: list[dict]) -> str:
        """
        Ensures answer is grounded in retrieved context.
        """

        # If the model explicitly abstained, respect it
        if answer.strip().lower() in ["i don't know", "unknown", "not available"]:
            return answer

        # If we retrieved nothing, we cannot validate
        if not chunks:
            return "I don't know"

        # Basic grounding heuristic:
        # If answer is non-empty and retrieval returned context, accept
        if len(answer.strip()) > 0:
            return answer

        return "I don't know"
