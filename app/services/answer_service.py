"""
DEPRECATED MODULE

This service previously handled direct answer generation using OpenAI.
It has been intentionally disabled to enforce LLM governance via:

- Agent Orchestration
- Context Control Plane
- LLM Gateway with Observability

Do NOT use this module.
"""

raise RuntimeError(
    "answer_service is deprecated. "
    "Use agent orchestrator + llm gateway instead."
)
