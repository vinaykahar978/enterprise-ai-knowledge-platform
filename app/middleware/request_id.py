import uuid
import logging
from fastapi import Request


logger = logging.getLogger("request-id")


async def request_id_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())

    request.state.request_id = request_id

    logger.info(f"Incoming request {request.method} {request.url} | request_id={request_id}")

    response = await call_next(request)

    response.headers["X-Request-ID"] = request_id
    return response
