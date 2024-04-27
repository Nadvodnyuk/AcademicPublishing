from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import AuthorsWorks

AWInSchema = pydantic_model_creator(
    AuthorsWorks, name="AWIn", exclude_readonly=True
)
AWOutSchema = pydantic_model_creator(
    AuthorsWorks, name="AWOut", exclude=["created_at", "modified_at"]
)