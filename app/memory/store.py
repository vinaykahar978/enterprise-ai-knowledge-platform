from app.memory.models import SessionMemory, TaskMemory, VerifiedMemory

SESSION_MEMORY_STORE: dict[str, list[SessionMemory]] = {}
TASK_MEMORY_STORE: dict[str, TaskMemory] = {}
VERIFIED_MEMORY_STORE: list[VerifiedMemory] = []
