from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Works
from backend.src.schemas.worksSchema import WorkOutSchema
from src.schemas.token import Status


async def get_works():
    return await WorkOutSchema.from_queryset(Works.all())


async def get_work(work_id) -> WorkOutSchema:
    return await WorkOutSchema.from_queryset_single(Works.get(id=work_id))


async def create_work(work, current_user) -> WorkOutSchema:
    work_dict = work.dict(exclude_unset=True)
    work_dict["author_id"] = current_user.id
    work_obj = await Works.create(**work_dict)
    return await WorkOutSchema.from_tortoise_orm(work_obj)


async def update_work(work_id, work, current_user) -> WorkOutSchema:
    try:
        db_work = await WorkOutSchema.from_queryset_single(Works.get(id=work_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Work {work_id} not found")

    if db_work.author.id == current_user.id:
        await Works.filter(id=work_id).update(**work.dict(exclude_unset=True))
        return await WorkOutSchema.from_queryset_single(Works.get(id=work_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_work(work_id, current_user) -> Status:
    try:
        db_work = await WorkOutSchema.from_queryset_single(Works.get(id=work_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Work {work_id} not found")

    if db_work.author.id == current_user.id:
        deleted_count = await Works.filter(id=work_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Work {work_id} not found")
        return Status(message=f"Deleted work {work_id}")

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")
