from app.agents.base import Agent


class ValidatorAgent(Agent):
    def run(self, answer: str, chunks: list[dict]):
        """
        Ensures answer is grounded in retrieved context.
        """
        for chunk in chunks:
            if chunk["text"][:50] in answer:
                return answer

        return "I don't know"
