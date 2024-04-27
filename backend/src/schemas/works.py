from typing import Optional
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Works

WorkInSchema = pydantic_model_creator(
    Works, name="WorkIn", exclude_readonly=True
)

WorkOutSchema = pydantic_model_creator(
    Works, name="WorkOut", exclude=["created_at", "modified_at"]
)

class UpdateWork(BaseModel):
    status: Optional[str]