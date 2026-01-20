from fastapi import APIRouter
from app.memory.store import (
    SESSION_MEMORY_STORE,
    TASK_MEMORY_STORE,
    VERIFIED_MEMORY_STORE,
)
from app.tools.audit import TOOL_AUDIT_LOGS

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/memory")
def get_memory_state():
    return {
        "session_memory": SESSION_MEMORY_STORE,
        "task_memory": TASK_MEMORY_STORE,
        "verified_memory": VERIFIED_MEMORY_STORE,
    }

@router.get("/tools")
def get_tool_logs():
    return TOOL_AUDIT_LOGS