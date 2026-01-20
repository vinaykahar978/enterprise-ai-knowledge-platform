import logging

logger = logging.getLogger(__name__)

# ✅ DEFINE AT MODULE LEVEL
LLM_CALL_LOGS: list[dict] = []


def log_llm_call(request: dict, response: dict):
    entry = {
        "model": response.get("model"),
        "usage": response.get("usage"),
    }

    LLM_CALL_LOGS.append(entry)

    logger.info(
        f"LLM_CALL | model={entry['model']} | usage={entry['usage']}"
    )
