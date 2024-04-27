from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.schemas.token import Status
from src.database.models import Authors, AuthorsWorks
from src.schemas.authors import AuthorOutSchema
import src.crud.authors_works as crudAW


async def get_authors():
    return await AuthorOutSchema.from_queryset(Authors.all())


async def get_author(author_id) -> AuthorOutSchema:
    return await AuthorOutSchema.from_queryset_single(Authors.get(id=author_id))


async def get_ex_author(author) -> AuthorOutSchema:
    return await AuthorOutSchema.from_queryset_single(Authors.get(code=author.code))


async def create_author(author) -> AuthorOutSchema:
    existing_author = await Authors.filter(full_name=author.full_name, code=author.code).first()
    if existing_author:
        # Если автор уже существует, обновляем его данные
        await Authors.filter(full_name=author.full_name, code=author.code).update(**author.dict(exclude_unset=True))
        ex_author = await Authors.filter(full_name=author.full_name, code=author.code).first()
        return await AuthorOutSchema.from_tortoise_orm(ex_author)
    try:
        author_obj = await Authors.create(**author.dict(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(
            status_code=401, detail=f"Sorry, that username already exists.")

    return await AuthorOutSchema.from_tortoise_orm(author_obj)


async def delete_author(author_id) -> Status:
    author_works = await AuthorsWorks.filter(author_id=author_id).first()

    # Если запись существует, удаляем связанные записи в таблице AuthorsWorks
    if author_works:
        await crudAW.delete_authors_works_by_author_id(author_id)
        
    try:
        await AuthorOutSchema.from_queryset_single(Authors.get(id=author_id))
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"Author {author_id} not found")

    deleted_count = await Authors.filter(id=author_id).delete()
    if not deleted_count:
        raise HTTPException(
            status_code=404, detail=f"Author {author_id} not found")
    return Status(message=f"Deleted author {author_id}")
