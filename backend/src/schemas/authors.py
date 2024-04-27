from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Authors

AuthorInSchema = pydantic_model_creator(
    Authors, name="AuthorIn", exclude_readonly=True
)
AuthorOutSchema = pydantic_model_creator(
    Authors, name="AuthorOut", exclude=["created_at", "modified_at"]
)