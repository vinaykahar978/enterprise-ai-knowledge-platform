import logging

logger = logging.getLogger("tool_audit")


def log_tool_execution(
    tool_name: str,
    user_role: str,
    status: str,
):
    logger.info(
        f"Tool executed | tool={tool_name} | role={user_role} | status={status}"
    )
