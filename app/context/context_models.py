from pydantic import BaseModel
from typing import List, Optional


class KnowledgeContext(BaseModel):
    """
    Defines what knowledge the AI is allowed to access.
    This is the MCP seed.
    """

    allowed_document_ids: Optional[List[str]] = None
    max_chunks: int = 5
    sensitivity: str = "internal"  # public | internal | confidential
