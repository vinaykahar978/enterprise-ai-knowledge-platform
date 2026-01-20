from app.memory.models import SessionMemory, TaskMemory, VerifiedMemory
from app.memory.store import (
    SESSION_MEMORY_STORE,
    TASK_MEMORY_STORE,
    VERIFIED_MEMORY_STORE,
)


def write_session_memory(session_id: str, content: str):
    memory = SessionMemory(session_id=session_id, content=content)
    SESSION_MEMORY_STORE.setdefault(session_id, []).append(memory)


def read_session_memory(session_id: str):
    return SESSION_MEMORY_STORE.get(session_id, [])


def write_task_memory(task_id: str, state: dict):
    TASK_MEMORY_STORE[task_id] = TaskMemory(task_id=task_id, state=state)


def read_task_memory(task_id: str):
    return TASK_MEMORY_STORE.get(task_id)


def write_verified_memory(fact: str, approved_by: str):
    VERIFIED_MEMORY_STORE.append(
        VerifiedMemory(fact=fact, approved_by=approved_by)
    )


def read_verified_memory():
    return VERIFIED_MEMORY_STORE
