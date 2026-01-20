import logging



logger = logging.getLogger("tool_audit")
TOOL_AUDIT_LOGS: list[dict] = []

def log_tool_execution(tool_name: str, user_role: str, status: str):
    entry = {
        "tool": tool_name,
        "role": user_role,
        "status": status,
    }
    TOOL_AUDIT_LOGS.append(entry)

    logger.info(
        f"Tool executed | tool={tool_name} | role={user_role} | status={status}"
    )
