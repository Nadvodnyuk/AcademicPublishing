from typing import List
from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.schemas.token import Status
from src.database.models import AuthorsWorks, Works
from src.schemas.works import WorkOutSchema
import src.crud.authors_works as crudAW
from tortoise.expressions import Q


async def get_works():
    return await WorkOutSchema.from_queryset(Works.all())


async def get_work(work_id) -> WorkOutSchema:
    return await WorkOutSchema.from_queryset_single(Works.get(id=work_id))


async def create_work(work) -> WorkOutSchema:
    try:
        work_obj = await Works.create(**work.dict(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(
            status_code=401, detail=f"Sorry, that work name already exists.")

    return await WorkOutSchema.from_tortoise_orm(work_obj)


async def update_work(work_id, work) -> WorkOutSchema:
    try:
        await WorkOutSchema.from_queryset_single(Works.get(id=work_id))
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"Work {work_id} not found")

    await Works.filter(id=work_id).update(**work.dict(exclude_unset=True))
    return await WorkOutSchema.from_queryset_single(Works.get(id=work_id))


async def delete_work(work_id) -> Status:
    author_works = await AuthorsWorks.filter(work_id=work_id).first()

    # Если запись существует, удаляем связанные записи в таблице AuthorsWorks
    if author_works:
        await crudAW.delete_authors_works_by_work_id(work_id)

    try:
        await WorkOutSchema.from_queryset_single(Works.get(id=work_id))
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"Work {work_id} not found")

    deleted_count = await Works.filter(id=work_id).delete()
    if not deleted_count:
        raise HTTPException(
            status_code=404, detail=f"Work {work_id} not found")
    return Status(message=f"Deleted work {work_id}")


async def search_works(query: str) -> List[WorkOutSchema]:
    try:
        year = None
        try:
            year = int(query)
        except ValueError:
            pass  # Если не удалось преобразовать в число, пропускаем

        results = await Works.filter(
            Q(field__icontains=query) |
            Q(title__icontains=query) |
            Q(event__icontains=query) |
            Q(status__icontains=query) |
            Q(abstract__icontains=query) |
            Q(key_words__icontains=query) |
            Q(intro__icontains=query) |
            Q(aim__icontains=query) |
            Q(materials_methods__icontains=query) |
            Q(results__icontains=query) |
            Q(conclusion__icontains=query) |
            Q(literature__icontains=query) |
            (Q(year=year) if year is not None else Q())  
        ).all()
        print(results)
        return [await WorkOutSchema.from_tortoise_orm(work) for work in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
