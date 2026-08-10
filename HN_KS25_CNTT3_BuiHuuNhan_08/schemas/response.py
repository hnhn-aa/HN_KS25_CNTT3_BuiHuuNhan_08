from pydantic import BaseModel
from typing import Optional, Any

class APIResponse(BaseModel):
    statusCode: int
    error: Optional[str] = None
    message: str
    data: Optional[Any] = None