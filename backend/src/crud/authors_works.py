from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.schemas.token import Status
from src.database.models import AuthorsWorks
from src.schemas.authors_works import AWOutSchema


async def get_authors_works_all():
    return await AWOutSchema.from_queryset(AuthorsWorks.all())


async def get_authors_works_by_author_id(author_id):
    return await AWOutSchema.from_queryset(AuthorsWorks.filter(author_id=author_id).all())


async def get_authors_works_by_work_id(work_id):
    return await AWOutSchema.from_queryset(AuthorsWorks.filter(work_id=work_id).all())


async def get_authors_works(authors_works_id) -> AWOutSchema:
    return await AWOutSchema.from_queryset_single(AuthorsWorks.get(id=authors_works_id))


async def create_authors_works(authors_works) -> AWOutSchema:
    authors_works_obj = await AuthorsWorks.create(**authors_works.dict(exclude_unset=True))

    return await AWOutSchema.from_tortoise_orm(authors_works_obj)


async def delete_aw(authors_works_id) -> Status:
    try:
        await AWOutSchema.from_queryset_single(AuthorsWorks.get(id=authors_works_id))
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"Instace {authors_works_id} not found")

    deleted_count = await AuthorsWorks.filter(id=authors_works_id).delete()
    if not deleted_count:
        raise HTTPException(
            status_code=404, detail=f"Instance not found in AuthorsWorks")
    return Status(
        message=f"Deleted AuthorsWorks instance{authors_works_id}")


async def delete_authors_works_by_author_id(author_id):
    try:
        await AWOutSchema.from_queryset_single(AuthorsWorks.get(author_id=author_id))
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"Author {author_id} not found")

    deleted_count = await AuthorsWorks.filter(author_id=author_id).delete()
    if not deleted_count:
        raise HTTPException(
            status_code=404, detail=f"Work {author_id} not found")
    return Status(message=f"Deleted AuthorsWorks instances with author id = {author_id}")


async def delete_authors_works_by_work_id(work_id) -> Status:
    try:
        await AWOutSchema.from_queryset_single(AuthorsWorks.get(work_id=work_id))
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"Work {work_id} not found in AuthorsWorks")

    deleted_count = await AuthorsWorks.filter(work_id=work_id).delete()
    if not deleted_count:
        raise HTTPException(
            status_code=404, detail=f"Work {work_id} not found in AuthorsWorks")
    return Status(message=f"Deleted AuthorsWorks instances with work id = {work_id}")


async def delete_authors_works(authors_works) -> Status:
    try:
        await AWOutSchema.from_queryset_single(AuthorsWorks.get(work_id=authors_works.work_id))
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"Work {authors_works.work_id} not found in AuthorsWorks")
    try:
        await AWOutSchema.from_queryset_single(AuthorsWorks.get(author_id=authors_works.author_id))
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"Author {authors_works.author_id} not found")

    deleted_count = await AuthorsWorks.filter(work_id=authors_works.work_id, author_id=authors_works.author_id).delete()
    if not deleted_count:
        raise HTTPException(
            status_code=404, detail=f"Instance not found in AuthorsWorks")
    return Status(
        message=f"Deleted AuthorsWorks instances with work = {authors_works.work_id} and author {authors_works.author_id}")
