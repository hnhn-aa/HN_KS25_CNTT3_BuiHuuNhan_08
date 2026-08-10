from pydantic import BaseModel, Field
from schemas.category import CategoryResponse

class DishUpdate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    price: float = Field(..., gt=0)
    category_id: int

class DishResponse(BaseModel):
    id: int
    name: str
    price: float
    category: CategoryResponse