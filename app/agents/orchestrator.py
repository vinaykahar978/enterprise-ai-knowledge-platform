from app.agents.retriever import RetrieverAgent
from app.agents.reasoning import ReasoningAgent
from app.agents.validator import ValidatorAgent
from app.context.context_models import KnowledgeContext
from app.tools.gateway import execute_tool
from app.tools.audit import log_tool_execution
from app.memory.service import write_session_memory


async def run_agent_pipeline(
    question: str,
    context: dict | None = None,
):
    """
    Core agent orchestration pipeline.
    """

    knowledge_context = KnowledgeContext(**context) if context else KnowledgeContext()

    retriever = RetrieverAgent()
    reasoning = ReasoningAgent()
    validator = ValidatorAgent()

    chunks = retriever.run(question, knowledge_context)
    raw_answer = reasoning.run(question, chunks)
    final_answer = validator.run(raw_answer, chunks)

    write_session_memory(
        session_id="default",
        content=final_answer,
    )

    return {
        "answer": final_answer,
        "sources": chunks,
    }


def request_tool_execution(
    tool_name: str,
    params: dict,
    user_role: str,
):
    result = execute_tool(
        tool_name=tool_name,
        params=params,
        user_role=user_role,
    )

    log_tool_execution(
        tool_name=tool_name,
        user_role=user_role,
        status=result["status"],
    )

    return result
