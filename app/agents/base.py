class Agent:
    """
    Base interface for all agents.
    """

    def run(self, *args, **kwargs):
        raise NotImplementedError("Agent must implement run()")
