from app.tools.registry import TOOLS_REGISTRY


class ToolExecutionError(Exception):
    pass


def execute_tool(
    tool_name: str,
    params: dict,
    user_role: str,
):
    tool = TOOLS_REGISTRY.get(tool_name)

    if not tool:
        raise ToolExecutionError("Tool not registered")

    # Permission enforcement
    required_permission = tool["permission"]

    if required_permission == "write" and user_role != "admin":
        raise ToolExecutionError("Unauthorized tool execution")

    # Simulated execution (IMPORTANT)
    return {
        "tool": tool_name,
        "status": "simulated_success",
        "params": params,
    }
